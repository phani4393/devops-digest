"""RSS / Atom feed fetching for curated vendor blogs and news sites."""

from __future__ import annotations

from datetime import datetime, timezone
from time import mktime
from typing import List

import feedparser

from .. import config
from ..models import Article
from .http import get


def _parse_published(entry) -> datetime | None:
    for attr in ("published_parsed", "updated_parsed"):
        tm = getattr(entry, attr, None)
        if tm:
            try:
                return datetime.fromtimestamp(mktime(tm), tz=timezone.utc)
            except (OverflowError, ValueError):
                continue
    return None


def _clean_summary(entry) -> str:
    import re
    import html

    raw = getattr(entry, "summary", "") or ""
    # feedparser gives HTML in summaries; strip tags crudely without a dep.
    text = re.sub(r"<[^>]+>", " ", raw)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    text = _collapse_repeats(text)
    # Keep raw summaries bounded; advisories/changelogs can be enormous.
    return text[:1200]


def _collapse_repeats(text: str) -> str:
    """Collapse immediately-repeated phrases common in advisory feeds.

    Some feeds (e.g. CISA) repeat the same remediation block dozens of times.
    This squashes a phrase that repeats back-to-back down to a single copy.
    """
    import re

    # Collapse any 10-120 char chunk repeated 2+ times in a row.
    pattern = re.compile(r"(.{10,120}?)(?:\s*\1){1,}")
    prev = None
    while prev != text:
        prev = text
        text = pattern.sub(r"\1", text)
    return text.strip()


def fetch_source(source: config.FeedSource) -> List[Article]:
    """Fetch a single RSS/Atom feed into Article objects."""
    resp = get(source.url)
    if resp is None:
        return []

    parsed = feedparser.parse(resp.content)
    articles: List[Article] = []
    for entry in parsed.entries[: config.MAX_ITEMS_PER_FEED]:
        title = getattr(entry, "title", "").strip()
        link = getattr(entry, "link", "").strip()
        if not title or not link:
            continue
        articles.append(
            Article(
                title=title,
                url=link,
                source=source.name,
                published=_parse_published(entry),
                raw_summary=_clean_summary(entry),
            )
        )
    return articles


def fetch_all_rss() -> List[Article]:
    """Fetch every configured RSS source."""
    out: List[Article] = []
    for source in config.RSS_SOURCES:
        items = fetch_source(source)
        print(f"  [rss] {source.name}: {len(items)} items")
        out.extend(items)
    return out


def fetch_reddit() -> List[Article]:
    """Fetch configured subreddits via their free public .rss endpoints.

    Reddit rate-limits aggressively (HTTP 429). We space requests out and
    retry once after a short backoff; any still-failing sub is skipped so the
    rest of the digest is unaffected.
    """
    import time

    out: List[Article] = []
    for i, sub in enumerate(config.REDDIT_SUBS):
        if i:
            time.sleep(2)  # be polite between subreddits
        url = f"https://www.reddit.com/r/{sub}/.rss"
        resp = get(url)
        if resp is None:
            time.sleep(5)
            resp = get(url)  # one retry after a longer pause
        if resp is None:
            continue
        parsed = feedparser.parse(resp.content)
        count = 0
        for entry in parsed.entries[: config.MAX_ITEMS_PER_FEED]:
            title = getattr(entry, "title", "").strip()
            link = getattr(entry, "link", "").strip()
            if not title or not link:
                continue
            out.append(
                Article(
                    title=title,
                    url=link,
                    source=f"r/{sub}",
                    published=_parse_published(entry),
                    raw_summary=_clean_summary(entry),
                )
            )
            count += 1
        print(f"  [reddit] r/{sub}: {count} items")
    return out
