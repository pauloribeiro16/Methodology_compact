# Dream — offline conversation processing

> Pattern: **offline conversation consolidation**. Background jobs re-read session transcripts + the project's memory store and reorganize them (deduplicate, refresh, prune). The general idea appears in the AI memory literature (e.g. as "memory consolidation" in long-running agents). Adapted here as a deterministic-first, propose-only subsystem with an LLM-assisted nightly step.

---

## What lives here

| File | Purpose | How it's produced |
|---|---|---|
| `ADOPTION_REPORT.md` | Deterministic audit of KG usage, mandated-skill invocations, case progress, and **proposed amendments to AGENTS.md** (propose-only per P7) | `scripts/dream/adoption_audit.py` |
| `RECONCILIATION.md` | Git history vs state files drift; hardcoded main-repo path references; progress.json consistency | `scripts/dream/reconcile.py` |
| `LESSONS.md` | Human-curated gotchas, anti-patterns, workarounds — a compact replacement for the `known_bugs.md` that the main repo has but the compact lost | started by hand, appended by the dream |
| `STATE/` | Cursor files (gitignored) — last-processed timestamp, hook log, etc. | written by hooks and the daily job |

The shared parser is `scripts/dream/transcript_lib.py`. The session-start brief is `scripts/dream/brief.sh` (≤40 lines, registered as a ZCode `SessionStart` hook in `.zcode/config.json`).

## P7 rule (non-negotiable)

The dream **never edits** `AGENTS.md`, `00_METHODOLOGY/AGENTS.md`, `PROJECT_STATE.md`, `GLOBAL_PROJECT_STATE.md`, `progress.json`, `dependency_graph.yaml`, or any other methodology/state file directly. Every output is either a report or a *proposed diff* that the human applies manually. The dream can commit the `dream/*.md` files itself (so its outputs are versioned), and it can update the project's memory store (`~/.zcode/cli/memories/...`) because that is its own substrate.

## Run manually

```bash
python3 scripts/dream/adoption_audit.py     # writes dream/ADOPTION_REPORT.md
python3 scripts/dream/reconcile.py          # writes dream/RECONCILIATION.md
bash scripts/dream/brief.sh                 # stdout, ~32 lines
```

## Run nightly (ZCode scheduled job)

A daily automation at 18:00 (Europe/Lisbon, the user's tz) runs the deterministic scripts, then performs LLM-assisted memory consolidation: re-reads the memory store at `~/.zcode/cli/memories/projects/methodology_compact-1839a9d8746b19ef/memory/`, corrects stale entries (the original store says lints and KG are not available here — both wrong as of 2026-08-26), prunes duplicates, appends new facts learned in the day's sessions, refreshes `MEMORY.md`, and commits the new `dream/*.md` outputs.

## What the dream is **not**

- Not a self-improvement loop. It does not change the agent's behaviour — only the memory and the candidate patches that the human reviews.
- Not a token-saving mechanism. The brief is short; the consolidation step is heavy but off-session.
- Not magic. The audit is regex-and-JSON over transcripts; reconciliation is `git log` + `grep`. Both fail in interesting ways and the reports say so explicitly.

## Why this exists

Adoption is measured, not assumed. The KG has a `.kg_usage.log`; the dream makes the rest of the methodology measurable the same way. If a step is in the pre-flight but never appears in any transcript, the report proposes either wiring it up (e.g. via hook) or removing it from the pre-flight text. That closes the loop between "the methodology says X" and "X actually happens".

## Sources / background

The "offline memory consolidation" idea is shared across long-running-agent designs; the closest publicly documented implementations live at:

- Memory consolidation in long-running agents — general background (search: "ai agent offline memory consolidation")
- SkillNet paper for the skills-as-assets framing that this repo also uses: https://arxiv.org/abs/2603.04448
- Critical take ("memory debt management"): https://ai.plainenglish.io/claude-dreaming-is-not-self-improvement-it-is-memory-debt-management-with-better-branding-d31de83b2437
