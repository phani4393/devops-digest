"""Shared data model for a curated article."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional


@dataclass
class Article:
    """A single candidate article flowing through the pipeline."""

    title: str
    url: str
    source: str
    published: Optional[datetime] = None
    raw_summary: str = ""          # summary/content as provided by the source
    points: int = 0                # HN points / Reddit score if available
    comments: int = 0

    # Filled in by later stages:
    topic: Optional[str] = None    # assigned lane
    relevance: float = 0.0         # ranking score
    summary: str = ""              # generated (extractive/ollama) summary
    linkedin_angle: str = ""       # content hook for the autoposter
    matched_terms: List[str] = field(default_factory=list)

    @property
    def id(self) -> str:
        """Stable identifier for dedupe (normalized URL, fallback to title)."""
        key = (self.url or self.title).strip().lower()
        # Strip common tracking/query noise so the same story dedupes cleanly.
        key = key.split("?")[0].rstrip("/")
        return hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]

    @property
    def text(self) -> str:
        """Combined title + summary used for keyword matching."""
        return f"{self.title}\n{self.raw_summary}".lower()

    def age_hours(self, now: Optional[datetime] = None) -> float:
        if not self.published:
            return 1e9  # treat unknown dates as very old
        now = now or datetime.now(timezone.utc)
        pub = self.published
        if pub.tzinfo is None:
            pub = pub.replace(tzinfo=timezone.utc)
        return max(0.0, (now - pub).total_seconds() / 3600.0)
