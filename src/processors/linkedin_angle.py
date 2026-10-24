"""Generate a short 'LinkedIn angle' hook for each article.

The digest doubles as content fuel for the LinkedIn autoposter, so every item
carries a one-line framing you can riff on. This is free and deterministic:
it derives the hook from the topic + whether the item touches your stack, with
light variety so a digest doesn't read like a template.
"""

from __future__ import annotations

from .. import config
from ..models import Article
from .filter_rank import _contains

# Per-topic framings that read like the start of a thought-leadership post.
_TOPIC_HOOKS = {
    "cybersecurity": [
        "Security teams: here's what this means for your threat model.",
        "A reminder that the attack surface keeps shifting — here's the takeaway.",
        "If you own security posture, this is worth a 2-minute read.",
    ],
    "ai": [
        "The AI tooling landscape moved again — here's why it matters for builders.",
        "Another signal that the way we ship software is changing.",
        "Worth bookmarking if you're wiring AI into real workflows.",
    ],
    "devsecops": [
        "Shifting security left isn't a slogan — this is what it looks like in practice.",
        "For anyone hardening their pipeline, there's a concrete lesson here.",
        "Supply-chain and IaC security keep maturing. Here's the practical angle.",
    ],
    "sre": [
        "Reliability is a feature. Here's a pattern worth stealing.",
        "For the on-call crowd: a useful take on keeping systems healthy.",
        "Observability and SLOs done right — a quick field note.",
    ],
}

# When an item touches the day-job stack, make the hook personal and specific.
_STACK_TERMS = ("salesforce", "copado", "aws", "terraform", "datadog")


def _stack_mentioned(article: Article) -> list[str]:
    text = article.text
    return [t for t in _STACK_TERMS if _contains(text, t)]


def generate_angle(article: Article) -> str:
    stack = _stack_mentioned(article)
    if stack:
        pretty = "/".join(s.capitalize() if s != "aws" else "AWS" for s in stack)
        return (
            f"Directly relevant to {pretty} work — a strong hook for a post "
            f"tying this to real-world {pretty} experience."
        )

    hooks = _TOPIC_HOOKS.get(article.topic or "", [])
    if not hooks:
        return "A useful data point for your next post."
    # Deterministic pick so re-runs are stable: hash the id to an index.
    idx = int(article.id, 16) % len(hooks)
    return hooks[idx]


def generate_all(articles) -> None:
    for article in articles:
        article.linkedin_angle = generate_angle(article)
