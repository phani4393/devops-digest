"""Hacker News top-stories fetcher via the free Firebase API (no key)."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import List

from .. import config
from ..models import Article
from .http import get

API = "https://hacker-news.firebaseio.com/v0"


def fetch_hackernews(limit: int | None = None) -> List[Article]:
    """Fetch top HN stories as Article objects.

    Topic assignment happens later via keyword matching; HN is a firehose so
    we just pull the top N and let the filter stage decide what's relevant.
    """
    if not config.HN_ENABLED:
        return []

    limit = limit or config.HN_STORY_LIMIT
    resp = get(f"{API}/topstories.json")
    if resp is None:
        return []

    try:
        ids = resp.json()[:limit]
    except ValueError:
        return []

    out: List[Article] = []
    for story_id in ids:
        item_resp = get(f"{API}/item/{story_id}.json")
        if item_resp is None:
            continue
        try:
            item = item_resp.json()
        except ValueError:
            continue
        if not item or item.get("type") != "story":
            continue
        title = (item.get("title") or "").strip()
        url = item.get("url") or f"https://news.ycombinator.com/item?id={story_id}"
        if not title:
            continue
        published = None
        if item.get("time"):
            published = datetime.fromtimestamp(item["time"], tz=timezone.utc)
        out.append(
            Article(
                title=title,
                url=url,
                source="Hacker News",
                published=published,
                raw_summary=title,  # HN has no body; title carries the signal
                points=int(item.get("score", 0)),
                comments=int(item.get("descendants", 0)),
            )
        )
    print(f"  [hn] {len(out)} stories")
    return out
