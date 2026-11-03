"""Generate a one-line 'why it matters' impact note for each article.

A time-pressed reader wants the practical "so what" before deciding whether to
click. This is the single highest-leverage addition for scan-ability: lead with
what changed and why the reader should care.

Two backends, mirroring the summarizer:
  - deterministic (default): free, no deps. Derives the line from the triage
    tag, the stack terms it touches, and topic-specific framing.
  - ollama (optional): if DD_SUMMARIZER=ollama and a local server is reachable,
    ask the model for a single impact sentence; falls back silently otherwise.
"""

from __future__ import annotations

from typing import List

from .. import config
from ..models import Article
from ..sources.http import get_session
from .filter_rank import _contains

# Stack terms worth calling out by name in the impact line.
_STACK_TERMS = (
    "salesforce", "copado", "aws", "terraform", "datadog",
    "kubernetes", "eks", "lambda", "github actions", "opentelemetry",
)


def _pretty_stack(terms: List[str]) -> str:
    def nice(t: str) -> str:
        if t == "aws":
            return "AWS"
        if t == "eks":
            return "EKS"
        if t == "opentelemetry":
            return "OpenTelemetry"
        if t == "github actions":
            return "GitHub Actions"
        return t.capitalize()

    pretty = [nice(t) for t in terms]
    if len(pretty) == 1:
        return pretty[0]
    if len(pretty) == 2:
        return f"{pretty[0]} and {pretty[1]}"
    return ", ".join(pretty[:-1]) + f", and {pretty[-1]}"


# Topic-specific "why it matters" framings, chosen deterministically.
_TOPIC_IMPACT = {
    "cybersecurity": [
        "Check whether your exposure matches this before an attacker does.",
        "Worth a scan if you own patching or security posture.",
        "Signals where attacker attention is heading next.",
    ],
    "ai": [
        "Changes what's possible (or cheaper) in your AI tooling.",
        "A shift in the LLM/agent stack worth tracking for your builds.",
        "May alter how you wire AI into real workflows.",
    ],
    "devsecops": [
        "Relevant if you're hardening a pipeline or supply chain.",
        "A concrete pattern for shifting security left.",
        "Could tighten (or unblock) your CI/CD and IaC security.",
    ],
    "sre": [
        "Useful for on-call load, SLOs, or observability cost.",
        "A reliability pattern worth borrowing.",
        "May cut toil or your telemetry bill.",
    ],
}


def _deterministic(article: Article) -> str:
    stack = [t for t in _STACK_TERMS if _contains(article.text, t)]
    if stack:
        return (
            f"Touches your {_pretty_stack(stack)} stack — likely actionable, "
            f"not just interesting."
        )

    if article.triage == "act":
        return "Time-sensitive: likely needs a decision or action soon."

    hooks = _TOPIC_IMPACT.get(article.topic or "", [])
    if not hooks:
        return "A useful data point for your week."
    idx = int(article.id, 16) % len(hooks)
    return hooks[idx]


def _ollama(article: Article) -> str | None:
    """Ask a local Ollama model for a single impact sentence. None if down."""
    source_text = article.summary or article.raw_summary or article.title
    prompt = (
        "In ONE short sentence, state why the following item matters to a "
        "senior DevOps/security engineer who values their time. Start with the "
        "practical impact, no preamble, no restating the headline.\n\n"
        f"{source_text}"
    )
    try:
        resp = get_session().post(
            f"{config.OLLAMA_HOST}/api/generate",
            json={"model": config.OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=config.HTTP_TIMEOUT,
        )
        resp.raise_for_status()
        out = resp.json().get("response", "").strip()
        # Keep it to a single sentence/line.
        if out:
            out = out.replace("\n", " ").strip()
            return out
        return None
    except Exception as exc:  # noqa: BLE001 - any failure -> graceful fallback
        print(f"  [warn] ollama why-it-matters failed, using deterministic: {exc}")
        return None


def generate(article: Article) -> str:
    if config.SUMMARIZER == "ollama":
        result = _ollama(article)
        if result:
            return result
    return _deterministic(article)


def generate_all(articles: List[Article]) -> None:
    """Fill in .why_it_matters for every article in place."""
    for article in articles:
        article.why_it_matters = generate(article)
