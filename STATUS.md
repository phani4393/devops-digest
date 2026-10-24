# Project Status

_Last updated: 2026-10-24_

## Current status: ✅ Working MVP

The full pipeline is implemented and verified end to end locally.

| Area | Status | Notes |
|------|--------|-------|
| Source fetching | ✅ Done | Hacker News API, vendor/news RSS, Reddit `.rss` |
| Topic classification | ✅ Done | 4 lanes, word-boundary keyword matching |
| Relevance ranking | ✅ Done | keywords + personal-stack boosts + popularity/freshness |
| Free summarization | ✅ Done | extractive (default) + optional local Ollama |
| LinkedIn angle hooks | ✅ Done | per-item content framing |
| Dedupe / seen state | ✅ Done | persistent JSON, verified across runs |
| Telegram delivery | ✅ Done | optional; graceful skip when unconfigured |
| Markdown archive | ✅ Done | dated, Obsidian-ready |
| GitHub Actions cron | ✅ Done | weekly Sunday 7PM CT + manual trigger |
| Documentation | ✅ Done | README, FAQ, STATUS, ROADMAP |

## Verified behavior

- `python -m src.digest --dry-run` builds the digest, writes the archive, and
  prints a preview with no network writes. Exit 0.
- `python -m src.digest` (full run) selected 20 items across 4 lanes, wrote the
  archive, detected missing Telegram config and skipped gracefully, and recorded
  20 items as seen.
- A second consecutive run dropped previously-seen items, confirming dedupe
  persistence.

## Known limitations

- **Reddit RSS is best-effort.** Reddit rate-limits (`429`) and sometimes blocks
  (`403`) requests coming from datacenter IPs such as GitHub Actions runners.
  When that happens those subreddits are skipped; the HN and blog feeds carry
  the digest on their own. Not a blocker, just reduced Reddit coverage in CI.
- **Hugging Face RSS** occasionally drops the TLS connection. It's one feed among
  many and a failure there doesn't affect the rest of the run.
- **Extractive summaries** are good but not abstractive. For sharper summaries,
  enable the free local Ollama backend (`DD_SUMMARIZER=ollama`).
- **Full-text not fetched.** Summaries are built from the feed-provided
  excerpt/title, not the full article body. Link-only sources (some Reddit
  posts) therefore get thinner summaries.

## How to run locally

```bash
pip install -r requirements.txt
python -m src.digest --dry-run   # preview, no side effects
python -m src.digest             # full run (sends + records state)
```

See `README.md` for Telegram setup, configuration, and the GitHub Actions
schedule.
