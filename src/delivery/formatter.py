"""Render the selected articles into Telegram messages and a markdown archive."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, List

from .. import config
from ..models import Article

# Telegram hard-limits a message at 4096 chars; stay well under to be safe.
_TELEGRAM_LIMIT = 3800

# Scan-priority badges for the triage tag.
_TRIAGE_BADGE = {
    "act": "🔴 ACT",
    "watch": "🟡 WATCH",
    "fyi": "⚪ FYI",
}


def _triage_badge(article: Article) -> str:
    return _TRIAGE_BADGE.get(article.triage, "")


def _escape_md(text: str) -> str:
    """Escape the characters that break Telegram's legacy Markdown."""
    for ch in ("_", "*", "`", "["):
        text = text.replace(ch, f"\\{ch}")
    return text


def _header() -> str:
    today = datetime.now(timezone.utc).strftime("%b %d, %Y")
    return f"🗞️ *DevOps Digest* — {today}\n_Cybersecurity · AI · DevSecOps · SRE_"


def build_telegram_messages(by_topic: Dict[str, List[Article]]) -> List[str]:
    """Build a list of Telegram-sized messages (split by length)."""
    messages: List[str] = []
    current = _header()

    for topic in config.TOPICS:
        items = by_topic.get(topic, [])
        if not items:
            continue
        section = f"\n\n{config.TOPIC_LABELS[topic]}\n" + "━" * 16
        block = section
        for i, art in enumerate(items, 1):
            badge = _triage_badge(art)
            badge_prefix = f"{badge} " if badge else ""
            entry = (
                f"\n\n{badge_prefix}{i}. [{_escape_md(art.title)}]({art.url})"
                f"\n_{art.source}_"
                f"\n{_escape_md(art.summary)}"
            )
            if art.why_it_matters:
                entry += f"\n🎯 _{_escape_md(art.why_it_matters)}_"
            entry += f"\n💡 {_escape_md(art.linkedin_angle)}"
            # Flush the current message if adding this entry would overflow.
            if len(current) + len(block) + len(entry) > _TELEGRAM_LIMIT:
                messages.append(current + block)
                current = ""
                block = section  # repeat the section header in the new message
            block += entry
        current += block

    if current.strip():
        messages.append(current)
    return messages


def build_markdown(by_topic: Dict[str, List[Article]]) -> str:
    """Build an Obsidian-friendly markdown document for the archive."""
    now = datetime.now(timezone.utc)
    lines: List[str] = [
        f"# DevOps Digest — {now.strftime('%Y-%m-%d')}",
        "",
        "> Cybersecurity · AI News & Tools · DevSecOps · SRE",
        f"> Generated {now.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
    ]

    total = 0
    for topic in config.TOPICS:
        items = by_topic.get(topic, [])
        if not items:
            continue
        lines.append(f"## {config.TOPIC_LABELS[topic]}")
        lines.append("")
        for i, art in enumerate(items, 1):
            total += 1
            badge = _triage_badge(art)
            heading = f"### {i}. [{art.title}]({art.url})"
            if badge:
                heading = f"### {badge} · {i}. [{art.title}]({art.url})"
            lines.append(heading)
            meta = f"*{art.source}*"
            if art.published:
                meta += f" · {art.published.strftime('%Y-%m-%d')}"
            if art.points:
                meta += f" · {art.points} pts"
            lines.append(meta)
            lines.append("")
            if art.summary:
                lines.append(art.summary)
                lines.append("")
            if art.why_it_matters:
                lines.append(f"**🎯 Why it matters:** {art.why_it_matters}")
                lines.append("")
            lines.append(f"**LinkedIn angle:** {art.linkedin_angle}")
            if art.matched_terms:
                lines.append("")
                lines.append(f"<sub>matched: {', '.join(art.matched_terms)}</sub>")
            lines.append("")

    if total == 0:
        lines.append("_No new articles matched this week._")

    lines.append("")
    lines.append(f"---\n*{total} items · DevOps Digest*")
    return "\n".join(lines)
