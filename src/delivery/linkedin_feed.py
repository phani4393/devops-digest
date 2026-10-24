"""Export selected digest items as a LinkedIn content feed.

This bridges DevOps Digest -> the `linkedin-autoposter` project. We write a
JSON file whose items match the autoposter's `TopicSuggestion` shape
(topic, category, angle, trending_context, source_articles) so the autoposter
can optionally consume our ranked, deduped items instead of re-researching RSS
from scratch.

The autoposter's taxonomy only has three categories
(cybersecurity / artificial-intelligence / devsecops), so our SRE lane is
folded into devsecops. Topic slugs mirror the autoposter's keyword mappings.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Dict, List

from .. import config
from ..models import Article

# DevOps Digest lane -> autoposter category.
_CATEGORY_MAP: Dict[str, str] = {
    "cybersecurity": "cybersecurity",
    "ai": "artificial-intelligence",
    "devsecops": "devsecops",
    "sre": "devsecops",  # autoposter has no SRE category
}

# Keyword -> autoposter topic slug (mirrors topic_researcher.topic_mappings).
# First match wins, so order from most to least specific.
_TOPIC_SLUGS: List[tuple[str, str]] = [
    ("zero-trust", "zero-trust-architecture"),
    ("ransomware", "ransomware-defense"),
    ("prompt injection", "prompt-injection"),
    ("supply chain", "supply-chain-security"),
    ("kubernetes", "kubernetes-security"),
    ("container", "container-security"),
    ("vulnerability", "vulnerability-management"),
    ("breach", "incident-response"),
    ("incident", "incident-response"),
    ("identity", "identity-access-management"),
    ("ai agent", "ai-agents"),
    ("agentic", "ai-agents"),
    ("llm", "llm-security"),
    ("generative ai", "generative-ai"),
    ("cicd", "cicd-security"),
    ("ci/cd", "cicd-security"),
    ("pipeline", "cicd-security"),
    ("secret", "secrets-management"),
    ("terraform", "infrastructure-as-code"),
    ("iac", "infrastructure-as-code"),
    ("api", "api-security"),
    ("cloud", "cloud-security"),
    ("observability", "observability"),
    ("slo", "reliability-engineering"),
    ("reliability", "reliability-engineering"),
]

# Fallback topic slug per category when no keyword matches.
_CATEGORY_FALLBACK: Dict[str, str] = {
    "cybersecurity": "threat-detection",
    "artificial-intelligence": "ai-in-security",
    "devsecops": "shift-left-security",
}


# For AI-category items, prefer AI-specific slugs before infra ones like
# "kubernetes-security" (an AI story about llm-d on k8s is still an AI topic).
_AI_PRIORITY_SLUGS: List[tuple[str, str]] = [
    ("prompt injection", "prompt-injection"),
    ("ai agent", "ai-agents"),
    ("agentic", "ai-agents"),
    ("llm", "llm-security"),
    ("generative ai", "generative-ai"),
]


def _topic_slug(article: Article, category: str) -> str:
    text = article.text
    if category == "artificial-intelligence":
        for keyword, slug in _AI_PRIORITY_SLUGS:
            if keyword in text:
                return slug
    for keyword, slug in _TOPIC_SLUGS:
        if keyword in text:
            return slug
    return _CATEGORY_FALLBACK.get(category, "security-automation")


def _angle(article: Article) -> str:
    """Prefer the already-generated LinkedIn angle; fall back to a template."""
    if article.linkedin_angle:
        return article.linkedin_angle
    head = article.title.split(":")[0]
    return f"Why {head} matters for engineering teams"


def _to_suggestion(article: Article) -> dict:
    category = _CATEGORY_MAP.get(article.topic or "", "devsecops")
    return {
        "topic": _topic_slug(article, category),
        "category": category,
        "angle": _angle(article),
        "trending_context": (
            f"Recent news context:\n- {article.title} ({article.source})\n"
            f"{article.summary}".strip()
        ),
        "source_articles": [article.url],
        # Extra fields the autoposter ignores but are handy for debugging/reuse:
        "title": article.title,
        "url": article.url,
        "source": article.source,
        "digest_topic": article.topic,
        "relevance": round(article.relevance, 3),
    }


def write_linkedin_feed(by_topic: Dict[str, List[Article]]) -> str:
    """Write feed/linkedin-feed.json and return its path.

    De-duplicates topic slugs so the autoposter gets variety (one suggestion
    per topic slug), keeping the highest-relevance item for each.
    """
    selected = [a for items in by_topic.values() for a in items]
    selected.sort(key=lambda a: a.relevance, reverse=True)

    seen_slugs: set[str] = set()
    suggestions: List[dict] = []
    for art in selected:
        s = _to_suggestion(art)
        if s["topic"] in seen_slugs:
            continue
        seen_slugs.add(s["topic"])
        suggestions.append(s)

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "devops-digest",
        "count": len(suggestions),
        "suggestions": suggestions,
    }

    out_dir = config.LINKEDIN_FEED_DIR
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "linkedin-feed.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
    return path
