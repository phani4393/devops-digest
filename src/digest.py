"""DevOps Digest entry point.

Pipeline:
  fetch (HN + RSS + Reddit)  ->  dedupe vs seen state  ->  classify + rank
  ->  select top-N per topic  ->  summarize (free)  ->  LinkedIn angles
  ->  deliver (Telegram + markdown archive)  ->  mark seen

Run locally:
    python -m src.digest            # full run
    python -m src.digest --dry-run  # no Telegram, no state writes, prints digest

Everything is free. Telegram is optional; without it you still get the archive.
"""

from __future__ import annotations

import argparse
import sys
from typing import Dict, List

# Load a local .env (if present) so TELEGRAM_* and DD_* vars are available
# without manual exports. Does nothing in CI where secrets are real env vars.
try:  # pragma: no cover - optional dependency / optional file
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# Ensure emoji/unicode in the digest print cleanly on any console (Windows
# defaults to cp1252, which can't encode the topic emoji).
try:  # pragma: no cover - environment dependent
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

from . import config, state
from .delivery import archive, formatter, linkedin_feed
from .delivery.telegram_bot import TelegramBot
from .models import Article
from .processors import filter_rank, linkedin_angle, summarizer
from .sources.hackernews import fetch_hackernews
from .sources.rss import fetch_all_rss, fetch_reddit


def fetch_all() -> List[Article]:
    print("Fetching sources...")
    articles: List[Article] = []
    articles.extend(fetch_hackernews())
    articles.extend(fetch_all_rss())
    articles.extend(fetch_reddit())

    # Collapse duplicate URLs that appear in more than one feed, keeping the
    # copy with the richest summary / highest points.
    unique: Dict[str, Article] = {}
    for art in articles:
        existing = unique.get(art.id)
        if existing is None:
            unique[art.id] = art
            continue
        if len(art.raw_summary) > len(existing.raw_summary) or art.points > existing.points:
            unique[art.id] = art
    deduped = list(unique.values())
    print(f"Collected {len(articles)} items ({len(deduped)} unique URLs)")
    return deduped


def build_digest(dry_run: bool = False) -> Dict[str, List[Article]]:
    articles = fetch_all()

    if not dry_run:
        before = len(articles)
        articles = state.filter_unseen(articles)
        print(f"Dropped {before - len(articles)} previously-seen items")

    print("Classifying and ranking...")
    scored = filter_rank.classify_and_score(articles)
    by_topic = filter_rank.select_per_topic(scored)

    selected = [a for items in by_topic.values() for a in items]
    print(f"Selected {len(selected)} items across {len(config.TOPICS)} topics")

    if selected:
        print(f"Summarizing with backend: {config.SUMMARIZER}")
        summarizer.summarize_all(selected)
        linkedin_angle.generate_all(selected)

    return by_topic


def deliver(by_topic: Dict[str, List[Article]], dry_run: bool = False) -> None:
    selected = [a for items in by_topic.values() for a in items]

    markdown = formatter.build_markdown(by_topic)
    archive_path = archive.write_archive(markdown)
    print(f"Archive written: {archive_path}")

    if config.LINKEDIN_FEED_ENABLED and selected:
        feed_path = linkedin_feed.write_linkedin_feed(by_topic)
        print(f"LinkedIn feed written: {feed_path}")

    messages = formatter.build_telegram_messages(by_topic)

    if dry_run:
        print("\n" + "=" * 60 + "\nDRY RUN — digest preview\n" + "=" * 60)
        print(markdown)
        return

    if not selected:
        print("No new items this week — skipping Telegram send.")
        return

    if TelegramBot.is_configured():
        bot = TelegramBot()
        ok = bot.send_messages(messages)
        print("Telegram: sent" if ok else "Telegram: completed with errors")
    else:
        print("Telegram not configured (set TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID).")
        print("Digest saved to archive only.")

    state.mark_seen(selected)
    print(f"Marked {len(selected)} items as seen.")


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="DevOps Digest")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and build the digest but don't send to Telegram or update state.",
    )
    args = parser.parse_args(argv)

    by_topic = build_digest(dry_run=args.dry_run)
    deliver(by_topic, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
