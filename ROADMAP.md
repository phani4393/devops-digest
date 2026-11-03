# Roadmap & Pending Items (Future Scope)

This is the backlog of ideas and improvements, roughly ordered by value vs
effort. Nothing here is required for the current MVP to work — it's all
"make it better" territory. Contributions welcome.

## 🔜 Near-term (high value, low effort)

- [ ] **Full-text extraction** — fetch the article page and pull the main body
  (e.g. `trafilatura` or `readability-lxml`) so summaries are richer than the
  RSS excerpt. Biggest single quality win.
- [ ] **Per-topic source weighting** — let each lane prefer certain feeds (e.g.
  SRE should lean on Grafana/Datadog over generic Reddit).
- [x] **De-duplicate near-identical stories** — the same CVE/story often appears
  across multiple feeds; cluster by title similarity and keep the best copy.
  Done: `filter_rank.dedupe_near_identical` collapses titles with ≥0.6 Jaccard
  overlap before the top-N cut, so duplicates no longer consume lane slots.
- [ ] **Config via YAML/TOML file** — move topics/sources/keywords out of
  `config.py` into an editable data file so non-developers can tune it.
- [ ] **`--topic` CLI filter** — run the digest for a single lane on demand.
- [x] **"Why it matters" impact line** — each item now carries a one-line
  practical "so what" (`processors/why_it_matters.py`), deterministic by
  default with an optional Ollama path. Shown in both the Telegram message and
  the markdown archive.
- [x] **Act / watch / FYI triage tags** — each item is tagged with a
  scan-priority badge (🔴 ACT / 🟡 WATCH / ⚪ FYI) derived from stack-boost and
  urgency signals, so a time-pressed reader can skim top-to-bottom.

## 🧭 Medium-term

- [ ] **Analytics-driven ranking (the only integration worth doing)** — if the
  companion `linkedin-autoposter` project's engagement data proves useful, feed
  "which topics performed" back into `CONTEXT_BOOSTS` so the digest learns what
  the audience responds to. This flows **analytics → digest only**. A direct
  content handoff was built and then intentionally removed: the autoposter is a
  deliberately dumb queue poster, and post writing is a human + Claude step, so
  machine-drafted posts would lower quality rather than add leverage. The digest
  informs you; you and Claude write.
- [ ] **Notion delivery** — optional push to a Notion database in addition to the
  Markdown archive (free Notion API).
- [ ] **Obsidian daily-note integration** — append to an existing vault note
  instead of a standalone file.
- [ ] **Scoring transparency** — include the numeric relevance score and its
  components in a `--debug` output to make tuning easier.
- [ ] **More sources** — GitHub Trending (by topic/language), Lobsters, dev.to
  tags, official AWS/Terraform/Salesforce release feeds.
- [x] **Sentiment / "why it matters" line** — done (see near-term section):
  a one-liner per item explaining the practical impact (deterministic by
  default, optional free/local Ollama model).

## 🌟 Longer-term / nice-to-have

- [ ] **Interactive Telegram commands** — `/digest`, `/topic sre`, `/more` to pull
  on demand, mirroring the macro-pulse-bot command pattern.
- [ ] **Weekly "theme" detection** — surface the recurring theme of the week
  (e.g. "supply-chain attacks dominated") as a digest intro.
- [ ] **Read/skip feedback loop** — thumbs up/down per item in Telegram that
  nudges future ranking (lightweight personalization).
- [ ] **De-dupe across the whole archive**, not just the rolling seen-window.
- [ ] **Multi-recipient / multi-channel** — Slack, email, RSS output of the
  digest itself.
- [ ] **Tests + CI lint** — add `pytest` coverage for the ranking/summarizer and
  a lint workflow.

## 🧪 Ideas being considered (not committed)

- Embedding-based relevance (free local embeddings) instead of keyword matching.
- A tiny static web page that publishes the latest digest from the archive.
- Trend charts: volume per topic over time from the accumulated archive.

---

Have an idea or found a bug? Open an issue describing the use case — concrete
examples of the content you wish the digest surfaced are especially helpful.
