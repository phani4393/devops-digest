"""Pluggable, free summarization.

Two backends, both $0:
  - "extractive" (default): frequency-based sentence scoring, pure stdlib.
    No keys, no network, works everywhere including GitHub Actions.
  - "ollama": calls a locally running Ollama server (free, local models).
    Used only if DD_SUMMARIZER=ollama and a server is reachable; otherwise it
    transparently falls back to extractive so the pipeline never breaks.
"""

from __future__ import annotations

import re
from collections import Counter
from typing import List

from .. import config
from ..models import Article
from ..sources.http import get_session

# Tiny English stopword set — enough for extractive scoring without a dependency.
_STOPWORDS = set(
    """a an the and or but if then else for of to in on at by with without from
    as is are was were be been being this that these those it its it's they them
    their there here we you your our i he she his her not no yes do does did has
    have had will would can could should may might must about into over under
    more most some any all each via using use used new how why what when which who""".split()
)

_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
_WORD_RE = re.compile(r"[a-zA-Z][a-zA-Z0-9'-]+")


# Hard cap on how much raw text we score. Some feeds (e.g. CISA advisories)
# dump huge, highly repetitive bodies; scoring all of it is slow and pointless.
_MAX_INPUT_CHARS = 4000


def _split_sentences(text: str) -> List[str]:
    text = re.sub(r"\s+", " ", text).strip()[:_MAX_INPUT_CHARS]
    if not text:
        return []
    sentences: List[str] = []
    seen: set[str] = set()
    for raw in _SENTENCE_RE.split(text):
        s = raw.strip()
        if not s:
            continue
        # Drop exact-duplicate sentences (common in boilerplate advisories).
        key = s.lower()
        if key in seen:
            continue
        seen.add(key)
        sentences.append(s)
    return sentences


def extractive_summary(text: str, max_sentences: int) -> str:
    """Rank sentences by normalized word-frequency and keep the top ones."""
    sentences = _split_sentences(text)
    if len(sentences) <= max_sentences:
        return " ".join(sentences)

    freq: Counter = Counter()
    for word in _WORD_RE.findall(text.lower()):
        if word not in _STOPWORDS and len(word) > 2:
            freq[word] += 1
    if not freq:
        return " ".join(sentences[:max_sentences])

    peak = max(freq.values())
    scored = []
    for idx, sentence in enumerate(sentences):
        words = [w for w in _WORD_RE.findall(sentence.lower()) if w not in _STOPWORDS]
        if not words:
            continue
        score = sum(freq[w] / peak for w in words) / len(words)
        scored.append((score, idx, sentence))

    scored.sort(reverse=True)
    chosen = sorted(scored[:max_sentences], key=lambda t: t[1])  # restore order
    return " ".join(s for _, _, s in chosen)


def _ollama_summary(text: str, max_sentences: int) -> str | None:
    """Summarize via a local Ollama server. Returns None if unavailable."""
    prompt = (
        f"Summarize the following in at most {max_sentences} concise sentences "
        f"for a senior DevOps/security engineer. Be factual, no preamble.\n\n{text}"
    )
    try:
        resp = get_session().post(
            f"{config.OLLAMA_HOST}/api/generate",
            json={"model": config.OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=config.HTTP_TIMEOUT,
        )
        resp.raise_for_status()
        out = resp.json().get("response", "").strip()
        return out or None
    except Exception as exc:  # noqa: BLE001 - any failure -> graceful fallback
        print(f"  [warn] ollama summary failed, falling back to extractive: {exc}")
        return None


def summarize(article: Article) -> str:
    """Produce a summary for an article using the configured backend."""
    source_text = article.raw_summary or article.title
    max_s = config.SUMMARY_SENTENCES

    if config.SUMMARIZER == "ollama":
        result = _ollama_summary(source_text, max_s)
        if result:
            return result

    return extractive_summary(source_text, max_s)


def summarize_all(articles: List[Article]) -> None:
    """Fill in .summary for every article in place."""
    for article in articles:
        article.summary = summarize(article)
