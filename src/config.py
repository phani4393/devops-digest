"""Central configuration for DevOps Digest.

Everything here is free: no paid APIs, no keys required for the default path.
Topics, sources, and keyword weights are tuned for a Salesforce / AWS /
Terraform / Datadog engineer who also writes on LinkedIn.

Override any of these via environment variables where noted.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Dict, List


# ---------------------------------------------------------------------------
# Topics
# ---------------------------------------------------------------------------
# The four lanes the digest is organized around. Order here is display order.
TOPICS: List[str] = [
    "cybersecurity",
    "ai",
    "devsecops",
    "sre",
]

TOPIC_LABELS: Dict[str, str] = {
    "cybersecurity": "🛡️ Cybersecurity",
    "ai": "🤖 AI News & Tools",
    "devsecops": "🔐 DevSecOps",
    "sre": "📈 SRE / Reliability",
}

# Keywords that assign an article to a topic and drive its relevance score.
# Lowercased substring matches against title + summary. Keep these specific
# enough to avoid false positives (e.g. "ai" alone would match "email").
TOPIC_KEYWORDS: Dict[str, List[str]] = {
    "cybersecurity": [
        "cve-", "zero-day", "zero day", "ransomware", "malware", "phishing",
        "data breach", "exploit", "vulnerability", "vulnerabilities", "patch tuesday",
        "threat actor", "backdoor", "cyberattack", "infostealer", "botnet",
        "privilege escalation", "rce", "ddos", "credential", "mfa bypass",
        "supply chain attack", "nvd", "cisa", "cvss",
    ],
    "ai": [
        "llm", "large language model", "gpt", "claude", "gemini", "llama",
        "mistral", "openai", "anthropic", "hugging face", "huggingface",
        "fine-tun", "inference", "rag", "retrieval-augmented", "agent",
        "agentic", "diffusion", "transformer", "foundation model", "ollama",
        "copilot", "prompt", "embedding", "vector database", "mcp",
        "model context protocol",
    ],
    "devsecops": [
        "devsecops", "sbom", "supply chain", "sast", "dast", "iac", "terraform",
        "infrastructure as code", "ci/cd", "pipeline", "secrets management",
        "secret scanning", "sigstore", "slsa", "shift left", "container security",
        "image scanning", "opa", "open policy agent", "policy as code",
        "dependency", "snyk", "trivy", "gitops", "copado", "salesforce devops",
    ],
    "sre": [
        "sre", "site reliability", "slo", "sli", "error budget", "incident",
        "postmortem", "post-mortem", "on-call", "observability", "opentelemetry",
        "otel", "datadog", "prometheus", "grafana", "tracing", "latency",
        "uptime", "availability", "chaos engineering", "toil", "runbook",
        "reliability", "paging", "alert fatigue",
    ],
}

# Personal-context boost: articles mentioning the actual day-job stack get
# ranked higher so the digest surfaces what's immediately actionable.
# Maps a lowercased keyword -> score bonus added to an item's relevance.
CONTEXT_BOOSTS: Dict[str, float] = {
    "salesforce": 3.0,
    "copado": 3.0,
    "apex": 2.0,
    "aws": 2.0,
    "terraform": 2.5,
    "datadog": 3.0,
    "cloudformation": 1.5,
    "lambda": 1.5,
    "claims": 1.5,
    "opentelemetry": 2.0,
    "github actions": 1.5,
    "eks": 1.5,
    "kubernetes": 1.0,
}


# ---------------------------------------------------------------------------
# Sources (all free, no auth required)
# ---------------------------------------------------------------------------
@dataclass
class FeedSource:
    """An RSS/Atom feed source."""

    name: str
    url: str
    # Topics this feed is expected to be relevant to. Used as a fallback topic
    # when keyword matching is weak, and as a small relevance prior.
    topics: List[str] = field(default_factory=list)


# Curated free RSS/Atom feeds, grouped by the lane they mostly serve.
RSS_SOURCES: List[FeedSource] = [
    # --- Cybersecurity ---
    FeedSource("The Hacker News", "https://feeds.feedburner.com/TheHackersNews", ["cybersecurity"]),
    FeedSource("BleepingComputer", "https://www.bleepingcomputer.com/feed/", ["cybersecurity"]),
    FeedSource("Krebs on Security", "https://krebsonsecurity.com/feed/", ["cybersecurity"]),
    FeedSource("CISA Advisories", "https://www.cisa.gov/cybersecurity-advisories/all.xml", ["cybersecurity"]),
    FeedSource("Google Project Zero", "https://googleprojectzero.blogspot.com/feeds/posts/default", ["cybersecurity"]),

    # --- AI news & tools ---
    FeedSource("Hugging Face Blog", "https://huggingface.co/blog/feed.xml", ["ai"]),
    FeedSource("Google AI Blog", "https://blog.google/technology/ai/rss/", ["ai"]),
    FeedSource("MIT Tech Review AI", "https://www.technologyreview.com/topic/artificial-intelligence/feed", ["ai"]),
    FeedSource("Simon Willison", "https://simonwillison.net/atom/everything/", ["ai"]),

    # --- DevSecOps ---
    FeedSource("AWS Security Blog", "https://aws.amazon.com/blogs/security/feed/", ["devsecops", "cybersecurity"]),
    FeedSource("Snyk Blog", "https://snyk.io/blog/feed/", ["devsecops"]),
    FeedSource("HashiCorp Blog", "https://www.hashicorp.com/blog/feed.xml", ["devsecops"]),
    FeedSource("The New Stack", "https://thenewstack.io/feed/", ["devsecops", "sre"]),

    # --- SRE ---
    FeedSource("Google Cloud Blog", "https://cloudblog.withgoogle.com/rss/", ["sre"]),
    FeedSource("Datadog Blog", "https://www.datadoghq.com/blog/index.xml", ["sre"]),
    FeedSource("Grafana Blog", "https://grafana.com/blog/index.xml", ["sre"]),
]

# Reddit subreddits consumed via their public .rss endpoints (no auth, free).
REDDIT_SUBS: Dict[str, List[str]] = {
    "netsec": ["cybersecurity"],
    "cybersecurity": ["cybersecurity"],
    "LocalLLaMA": ["ai"],
    "MachineLearning": ["ai"],
    "devops": ["devsecops", "sre"],
    "sre": ["sre"],
    "aws": ["devsecops", "sre"],
    "Terraform": ["devsecops"],
}

# Hacker News: top stories are fetched via the free Firebase API and matched
# against TOPIC_KEYWORDS. No key required.
HN_ENABLED: bool = os.getenv("DD_HN_ENABLED", "true").lower() == "true"
HN_STORY_LIMIT: int = int(os.getenv("DD_HN_STORY_LIMIT", "120"))


# ---------------------------------------------------------------------------
# Selection / ranking
# ---------------------------------------------------------------------------
# How far back to consider articles, in hours (default: one week).
LOOKBACK_HOURS: int = int(os.getenv("DD_LOOKBACK_HOURS", "168"))

# Max items to include per topic lane in the final digest.
MAX_PER_TOPIC: int = int(os.getenv("DD_MAX_PER_TOPIC", "5"))

# Minimum relevance score an item must reach to be included at all.
MIN_RELEVANCE: float = float(os.getenv("DD_MIN_RELEVANCE", "1.0"))

# Max entries to read from any single feed (some feeds expose thousands of
# historical items; the lookback filter still applies afterward).
MAX_ITEMS_PER_FEED: int = int(os.getenv("DD_MAX_ITEMS_PER_FEED", "60"))

# Network politeness / resilience.
HTTP_TIMEOUT: int = int(os.getenv("DD_HTTP_TIMEOUT", "20"))
USER_AGENT: str = os.getenv(
    "DD_USER_AGENT",
    "DevOpsDigest/1.0 (+https://github.com/; personal knowledge curator)",
)


# ---------------------------------------------------------------------------
# Summarization
# ---------------------------------------------------------------------------
# "extractive" (default, free, no deps beyond stdlib) or "ollama" (free, local).
SUMMARIZER: str = os.getenv("DD_SUMMARIZER", "extractive").lower()
SUMMARY_SENTENCES: int = int(os.getenv("DD_SUMMARY_SENTENCES", "2"))

# Only used when SUMMARIZER == "ollama". Local Ollama server, free.
OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.2")


# ---------------------------------------------------------------------------
# Output / state
# ---------------------------------------------------------------------------
# Directory where dated markdown archives are written (Obsidian-friendly).
ARCHIVE_DIR: str = os.getenv("DD_ARCHIVE_DIR", "archive")

# JSON file tracking already-seen article IDs so stories don't repeat.
SEEN_STATE_FILE: str = os.getenv("DD_SEEN_STATE_FILE", "state/seen.json")

# LinkedIn autoposter handoff: write a JSON feed of ranked items in the
# autoposter's TopicSuggestion shape. Set DD_LINKEDIN_FEED=false to disable.
LINKEDIN_FEED_ENABLED: bool = os.getenv("DD_LINKEDIN_FEED", "true").lower() == "true"
LINKEDIN_FEED_DIR: str = os.getenv("DD_LINKEDIN_FEED_DIR", "feed")

# How many days of "seen" history to retain before pruning.
SEEN_RETENTION_DAYS: int = int(os.getenv("DD_SEEN_RETENTION_DAYS", "45"))
