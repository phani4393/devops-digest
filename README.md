# DevOps Digest 🗞️

A free, set-it-and-forget-it personal knowledge curator. Every week it scans
free sources, ranks what matters for **your** stack, summarizes it with **no
paid APIs**, and delivers a digest to Telegram plus a dated Obsidian-ready
Markdown archive.

Four focus lanes:

- 🛡️ **Cybersecurity** — CVEs, zero-days, breaches, cloud/SaaS security
- 🤖 **AI News & Tools** — LLMs, agents, dev tooling, local models
- 🔐 **DevSecOps** — supply chain/SBOM, IaC security, CI/CD security, AWS/Salesforce DevOps
- 📈 **SRE / Reliability** — SLOs, incidents, observability, Datadog/OpenTelemetry

It also tags each item with a **LinkedIn angle** so the digest doubles as
content fuel for your posting pipeline.

## Why it's free

| Piece | Tool | Cost |
|-------|------|------|
| Sources | Hacker News API, Reddit `.rss`, vendor blog RSS | $0, no keys |
| Summaries | Extractive (pure Python) — optional local Ollama | $0, no keys |
| Delivery | Telegram Bot API | $0 |
| Archive | Local Markdown (Obsidian/Notion) | $0 |
| Scheduling | GitHub Actions cron | $0 (free tier) |

The only accounts you *might* set up are a Telegram bot token + chat ID, both
free. Without them, the digest still writes the Markdown archive.

## How it works

```
fetch (HN + RSS + Reddit)
  → dedupe vs "seen" state        (no repeats across weeks)
  → classify + score              (topic keywords + personal-stack boosts)
  → top-N per topic lane
  → summarize (free, pluggable)
  → add LinkedIn angles
  → deliver (Telegram + Markdown archive)
  → mark seen
```

Relevance scoring blends: topic keyword matches (title hits count double),
personal-context boosts (Salesforce, AWS, Terraform, Datadog, Copado, claims),
a small source prior, and popularity/freshness. Keyword matching uses word
boundaries, so `aws` won't match "aware" and `rce` won't match "source".

## Quick start

```bash
pip install -r requirements.txt

# Dry run: builds the digest, writes the archive, prints a preview.
# No Telegram, no state changes. Great for a first look.
python -m src.digest --dry-run

# Full run: sends to Telegram (if configured) and records seen items.
python -m src.digest
```

### Optional: Telegram delivery

1. Message [@BotFather](https://t.me/BotFather) → `/newbot` → copy the token.
2. Message [@userinfobot](https://t.me/userinfobot) → copy your chat ID.
3. Copy `.env.example` to `.env` and fill both in (or export them as env vars).

### Optional: local Ollama summaries (still free)

Prefer LLM-style summaries? Run a local model — no API cost:

```bash
ollama serve
ollama pull llama3.2
DD_SUMMARIZER=ollama python -m src.digest --dry-run
```

If Ollama isn't reachable it silently falls back to the extractive summarizer,
so the pipeline never breaks.

## Automate it (GitHub Actions)

`.github/workflows/weekly-digest.yml` runs every **Sunday 7:00 PM CT** and can
be triggered manually. To enable Telegram in CI, add two repo secrets:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

The workflow commits the updated `state/seen.json` and the new `archive/*.md`
back to the repo so dedupe persists and your archive builds up over time.

## Configuration

Everything is tunable via environment variables (see `.env.example` and
`src/config.py`). Common ones:

| Variable | Default | Purpose |
|----------|---------|---------|
| `DD_SUMMARIZER` | `extractive` | `extractive` or `ollama` |
| `DD_SUMMARY_SENTENCES` | `2` | sentences per summary |
| `DD_MAX_PER_TOPIC` | `5` | items per lane in the digest |
| `DD_LOOKBACK_HOURS` | `168` | how far back to consider (1 week) |
| `DD_MIN_RELEVANCE` | `1.0` | minimum score to include |
| `DD_ARCHIVE_DIR` | `archive` | where Markdown archives are written |

### Customizing topics & sources

- **Topics / keywords / personal boosts**: edit the dicts in `src/config.py`.
- **RSS feeds**: add `FeedSource(...)` entries to `RSS_SOURCES`.
- **Subreddits**: add to `REDDIT_SUBS` (note: Reddit RSS can rate-limit from
  CI IPs — it's treated as best-effort and never blocks a run).

## Project layout

```
src/
  config.py              topics, keywords, sources, tuning
  models.py              Article dataclass
  digest.py              orchestrator + CLI (python -m src.digest)
  state.py               persistent "seen" dedupe
  sources/
    http.py              resilient HTTP helper
    hackernews.py        HN top stories (free Firebase API)
    rss.py               RSS/Atom + Reddit .rss fetchers
  processors/
    filter_rank.py       topic assignment + relevance scoring
    summarizer.py        extractive (default) + optional Ollama
    linkedin_angle.py    per-item content hook
  delivery/
    telegram_bot.py      Telegram send
    formatter.py         Telegram messages + Markdown builder
    archive.py           dated Markdown writer
.github/workflows/
  weekly-digest.yml      Sunday cron + manual trigger
```

## Notes

- Hugging Face's RSS occasionally drops the TLS connection; it's just one of
  many feeds and a failure there doesn't affect the rest of the digest.
- Reddit RSS is best-effort from datacenter IPs; the curated blog + HN feeds
  carry the digest on their own.

## FAQ

**Is this really free?**
Yes. The default run uses no paid APIs and needs no keys. The only optional
accounts are a Telegram bot (free) and — if you want LLM-style summaries — a
local Ollama install (free). GitHub Actions runs on the free tier.

**Do I need a Telegram bot to use it?**
No. Without Telegram, every run still writes a dated Markdown file to
`archive/`. Telegram is just a convenient delivery channel. Set it up later if
you want push notifications.

**How do I change the topics?**
Edit `src/config.py`. `TOPICS` defines the lanes, `TOPIC_KEYWORDS` controls what
gets matched into each, and `CONTEXT_BOOSTS` is where you list your own stack so
relevant items rank higher. Add RSS feeds to `RSS_SOURCES` and subreddits to
`REDDIT_SUBS`.

**The digest included something off-topic / missed something I wanted. Why?**
Ranking is keyword + popularity based, not an LLM judgment, so it's a heuristic.
Tune `TOPIC_KEYWORDS`, raise `DD_MIN_RELEVANCE`, or add the exact terms you care
about. For sharper relevance, enabling the Ollama backend helps.

**Why are some Reddit sources empty in GitHub Actions?**
Reddit rate-limits (`429`) and sometimes blocks (`403`) requests from datacenter
IPs like CI runners. Those subreddits are skipped when that happens; the Hacker
News and vendor-blog feeds still produce a full digest. Running locally usually
gets Reddit content fine.

**Why extractive summaries instead of ChatGPT/Claude?**
To keep it 100% free with zero keys. Extractive summarization picks the most
representative sentences — no API cost, no rate limits, runs anywhere. If you
want abstractive summaries, set `DD_SUMMARIZER=ollama` and run a free local
model; it falls back to extractive automatically if Ollama isn't reachable.

**Will I get the same article twice?**
No. Seen article IDs are stored in `state/seen.json` and filtered out on later
runs. In CI the GitHub Action commits that file back so dedupe persists across
weeks. Old entries are pruned after `DD_SEEN_RETENTION_DAYS` (default 45).

**How often does it run?**
Weekly, Sunday 7:00 PM CT, via `.github/workflows/weekly-digest.yml`. You can
also trigger it manually from the Actions tab (`workflow_dispatch`), or change
the `cron` expression to any cadence you like.

**Can I run it on a schedule without GitHub?**
Yes — any cron/Task Scheduler that runs `python -m src.digest` works. GitHub
Actions is just the free, zero-maintenance option.

**Does it store or send my data anywhere?**
It only talks to the public sources it fetches and, if configured, the Telegram
API to send your digest. There's no analytics or third-party telemetry. Your
Telegram token lives in `.env` locally or in GitHub repo secrets in CI.

**Python version?**
Developed/tested on 3.11+ (CI pins 3.11). Only two dependencies: `requests` and
`feedparser`.

## Contributing

Issues and PRs are welcome. Good first contributions:

- Add or fix a source feed in `src/config.py`.
- Improve topic keywords for a lane.
- Pick an item off the [ROADMAP](ROADMAP.md).

Please keep the "no paid dependencies" principle intact — anything added should
have a free path that works without API keys.

## Project docs

- [STATUS.md](STATUS.md) — current state, verified behavior, known limitations
- [ROADMAP.md](ROADMAP.md) — pending items and future scope

## License

MIT — see [LICENSE](LICENSE).
