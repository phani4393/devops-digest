"""Assign topics, score relevance, and rank candidate articles.

Scoring blends four free signals:
  1. Topic keyword matches (how strongly it fits a lane)
  2. Personal-context boosts (Salesforce/AWS/Terraform/Datadog/...)
  3. Source prior (a feed curated for a lane gets a small nudge)
  4. Popularity + freshness (HN points, recency decay)

No external services involved — pure Python over the fetched text.
"""

from __future__ import annotations

import math
import re
from functools import lru_cache
from typing import Dict, List

from .. import config
from ..models import Article


@lru_cache(maxsize=2048)
def _term_pattern(term: str) -> "re.Pattern[str]":
    """Compile a whole-token matcher for a keyword/phrase.

    Using word boundaries avoids false positives like 'rce' inside 'source',
    'aws' inside 'aware', or 'rag' inside 'storage'. Terms that already end in
    punctuation (e.g. 'cve-') are matched as a prefix instead.
    """
    if term.endswith("-"):
        return re.compile(r"\b" + re.escape(term), re.IGNORECASE)
    return re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)


def _contains(text: str, term: str) -> bool:
    return _term_pattern(term).search(text) is not None


def _topic_scores(article: Article) -> Dict[str, float]:
    """Return per-topic keyword score and record matched terms."""
    text = article.text
    title = article.title.lower()
    scores: Dict[str, float] = {}
    for topic, keywords in config.TOPIC_KEYWORDS.items():
        score = 0.0
        for kw in keywords:
            if _contains(text, kw):
                # Title hits count double — the headline is the strongest signal.
                weight = 2.0 if _contains(title, kw) else 1.0
                score += weight
                article.matched_terms.append(kw)
        if score:
            scores[topic] = score
    return scores


def _context_boost(article: Article) -> float:
    text = article.text
    return sum(bonus for term, bonus in config.CONTEXT_BOOSTS.items() if _contains(text, term))


def _popularity_freshness(article: Article) -> float:
    # Gentle log boost for HN points; recency decay over the lookback window.
    pop = math.log1p(max(0, article.points)) * 0.5
    age = article.age_hours()
    # Linear-ish decay: fresh items keep ~1.0, week-old items approach ~0.
    freshness = max(0.0, 1.0 - (age / max(1, config.LOOKBACK_HOURS)))
    return pop + freshness


def classify_and_score(articles: List[Article]) -> List[Article]:
    """Assign each article a topic + relevance score; drop non-matches."""
    kept: List[Article] = []
    for article in articles:
        article.matched_terms = []
        topic_scores = _topic_scores(article)

        # Fall back to the source's declared topics if no keyword hit, but only
        # with a weak prior so curated feeds still surface their best content.
        source_topics = _source_topics(article.source)
        if not topic_scores and source_topics:
            topic_scores = {t: 0.5 for t in source_topics}

        if not topic_scores:
            continue  # irrelevant to all four lanes

        # Pick the strongest lane for this article.
        best_topic = max(topic_scores, key=topic_scores.get)
        base = topic_scores[best_topic]

        # Small nudge if the source was curated for the chosen lane.
        source_prior = 0.5 if best_topic in source_topics else 0.0

        # Light penalty for link-only posts (typical of Reddit RSS, which has
        # no body): they carry little signal and shouldn't crowd out articles
        # with real summaries in the curated lanes.
        thin_penalty = 0.0
        if article.source.startswith("r/") and len(article.raw_summary) < 80:
            thin_penalty = 1.0

        article.topic = best_topic
        article.relevance = (
            base
            + _context_boost(article)
            + source_prior
            + _popularity_freshness(article)
            - thin_penalty
        )
        # de-dupe matched terms for display
        article.matched_terms = sorted(set(article.matched_terms))
        kept.append(article)

    return kept


def _source_topics(source_name: str) -> List[str]:
    for src in config.RSS_SOURCES:
        if src.name == source_name:
            return src.topics
    if source_name.startswith("r/"):
        return config.REDDIT_SUBS.get(source_name[2:], [])
    return []


# ---------------------------------------------------------------------------
# Triage tagging (act / watch / fyi)
# ---------------------------------------------------------------------------
# A busy reader scans the digest and sorts each item into "do something now",
# "keep an eye on this", or "nice to know". We derive that cheaply from signals
# we already compute: items that touch the day-job stack are "act", strong
# topic matches are "watch", everything else is "fyi".
def assign_triage(article: Article) -> str:
    """Classify an article's scan-priority: 'act', 'watch', or 'fyi'."""
    text = article.text
    # Touches the actual day-job stack -> act on it.
    if any(_contains(text, term) for term in config.CONTEXT_BOOSTS):
        return "act"
    # Actively exploited / urgent security signals -> act.
    if any(_contains(text, urgent) for urgent in config.TRIAGE_URGENT_TERMS):
        return "act"
    # A solid topic match (more than a bare source-prior) -> watch.
    if len(article.matched_terms) >= config.TRIAGE_WATCH_MIN_MATCHES:
        return "watch"
    return "fyi"


# ---------------------------------------------------------------------------
# Near-duplicate clustering
# ---------------------------------------------------------------------------
_TITLE_NOISE = re.compile(r"[^a-z0-9 ]+")
_TITLE_STOP = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with",
    "as", "at", "by", "is", "are", "new", "how", "why",
}


def _title_tokens(title: str) -> set:
    cleaned = _TITLE_NOISE.sub(" ", title.lower())
    return {w for w in cleaned.split() if w and w not in _TITLE_STOP}


def _title_similarity(a: str, b: str) -> float:
    """Jaccard similarity over significant title tokens (0.0–1.0)."""
    ta, tb = _title_tokens(a), _title_tokens(b)
    if not ta or not tb:
        return 0.0
    inter = len(ta & tb)
    union = len(ta | tb)
    return inter / union if union else 0.0


def dedupe_near_identical(articles: List[Article]) -> List[Article]:
    """Collapse articles whose titles are near-identical, keeping the best copy.

    Operates on an already relevance-sorted list; the first (highest-ranked)
    representative of each cluster is kept, later duplicates are dropped. The
    overlap threshold is tunable via DD_DUP_TITLE_THRESHOLD.
    """
    threshold = config.DUP_TITLE_THRESHOLD
    kept: List[Article] = []
    for art in articles:
        if any(_title_similarity(art.title, k.title) >= threshold for k in kept):
            continue
        kept.append(art)
    return kept


def select_per_topic(articles: List[Article]) -> Dict[str, List[Article]]:
    """Filter by lookback + min relevance, dedupe, then take top-N per lane."""
    by_topic: Dict[str, List[Article]] = {t: [] for t in config.TOPICS}

    for article in articles:
        if article.topic not in by_topic:
            continue
        if article.age_hours() > config.LOOKBACK_HOURS:
            continue
        if article.relevance < config.MIN_RELEVANCE:
            continue
        by_topic[article.topic].append(article)

    for topic in by_topic:
        ranked = sorted(by_topic[topic], key=lambda a: a.relevance, reverse=True)
        # Drop near-identical stories *before* taking the top-N so duplicates
        # don't consume lane slots (e.g. the same CVE from two feeds).
        ranked = dedupe_near_identical(ranked)
        for art in ranked:
            art.triage = assign_triage(art)
        by_topic[topic] = ranked[: config.MAX_PER_TOPIC]

    return by_topic
