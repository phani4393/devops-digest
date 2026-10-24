"""Persistent 'seen' state so the same story never appears twice.

Stored as a small JSON file (committed by the GitHub Action) mapping an
article id -> ISO date first seen. Old entries are pruned after a retention
window so the file stays small.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from typing import Dict, Iterable, List

from . import config
from .models import Article


def _load() -> Dict[str, str]:
    path = config.SEEN_STATE_FILE
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError):
        return {}


def _save(seen: Dict[str, str]) -> None:
    path = config.SEEN_STATE_FILE
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(seen, fh, indent=2, sort_keys=True)


def _prune(seen: Dict[str, str]) -> Dict[str, str]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=config.SEEN_RETENTION_DAYS)
    kept: Dict[str, str] = {}
    for article_id, iso in seen.items():
        try:
            when = datetime.fromisoformat(iso)
        except ValueError:
            continue
        if when.tzinfo is None:
            when = when.replace(tzinfo=timezone.utc)
        if when >= cutoff:
            kept[article_id] = iso
    return kept


def filter_unseen(articles: Iterable[Article]) -> List[Article]:
    """Return only articles not already recorded as seen."""
    seen = _load()
    return [a for a in articles if a.id not in seen]


def mark_seen(articles: Iterable[Article]) -> None:
    """Record the given articles as seen and persist (with pruning)."""
    seen = _load()
    now = datetime.now(timezone.utc).isoformat()
    for article in articles:
        seen[article.id] = now
    _save(_prune(seen))
