# Dream — offline conversation processing

> Pattern: **offline conversation consolidation**. Background jobs re-read session transcripts + the project's memory store and reorganize them (deduplicate, refresh, prune). The general idea appears in the AI memory literature (e.g. as "memory consolidation" in long-running agents). Adapted here as a deterministic-first, propose-only subsystem with an LLM-assisted nightly step and a guarded self-tune layer.

---

## What lives here

| File | Purpose | How it's produced |
|---|---|---|
| `ADOPTION_REPORT.md` | Deterministic audit of KG usage, mandated-skill invocations, case progress, and **proposed amendments to AGENTS.md** (propose-only per P7) | `scripts/dream/adoption_audit.py` |
| `RECONCILIATION.md` | Git history vs state files drift; hardcoded main-repo path references; progress.json consistency; drift escalation markers when set unchanged ≥2 cycles | `scripts/dream/reconcile.py` |
| `LESSONS.md` | Human-curated gotchas, anti-patterns, workarounds — a compact replacement for the `known_bugs.md` that the main repo has but the compact lost | started by hand, appended by the dream |
| `SELF_TUNE_LOG.md` | Append-only ledger of every `[DREAM SELF-TUNE]` commit (what changed, why) | appended by `auto_tune.py` and `regression_check.py` |
| `STALE_PROPOSALS.md` | Archive of AGENTS.md amendment proposals seen ≥5 consecutive nightly cycles without resolution; awaits human verdict | `scripts/dream/stale_archive.py` |
| `STATE/` | Cursor files (gitignored) — hook log, bash_use log, intents, applied-tunes log, regression failures/reverts log | written by hooks and the nightly job |

The shared parser is `scripts/dream/transcript_lib.py`. The session-start brief is `scripts/dream/brief.sh` (≤40 lines, registered as a ZCode `SessionStart` hook in `.zcode/config.json`).

---

## P7 rule (non-negotiable, refined 2026-09-03)

The dream **never edits** `AGENTS.md`, `00_METHODOLOGY/AGENTS.md`, `PROJECT_STATE.md`, `GLOBAL_PROJECT_STATE.md`, `progress.json`, `dependency_graph.yaml`, or any other methodology/state file directly. Every output is either a report or a *proposed diff* that the human applies manually. The dream can commit the `dream/*.md` files itself (so its outputs are versioned), and it can update the project's memory store (`~/.zcode/cli/memories/...`) because that is its own substrate.

**Self-tune exception (Phase 2 of the auto-edit plan, 2026-09-03):** the dream MAY auto-edit its own infrastructure, but ONLY through the `self_tune.py` scope guard, which enforces an explicit deny-list (P7-protected files) that takes priority over an allow-list (Dream infrastructure files). Every auto-edit MUST pass `py_compile` + `--help` (Python) or `bash -n` + source smoke (Bash) before commit, and every commit MUST use the `[DREAM SELF-TUNE]` prefix.

---

## Architecture: 8-step nightly pipeline

| Step | What | Code |
|---|---|---|
| 1 | Deterministic reports | `scripts/dream/adoption_audit.py` + `scripts/dream/reconcile.py` |
| 2 | Read + diff vs prior commit | orchestrator-side (LLM) |
| 3 | Append net-new LESSONS entries | orchestrator-side (LLM) |
| 4 | `brief.sh` + line-budget check (≤40) | `scripts/dream/brief.sh` |
| 5 | Commit `dream/*` updates with `[DREAM YYYY-MM-DD]` | orchestrator-side |
| 6 | Memory consolidation | orchestrator-side (LLM) |
| 7 | **Self-tune pass** — apply mechanical edits from intents | `scripts/dream/auto_tune.py` |
| 8 | **Stale-proposal archive** — move ≥5-cycle amendments to `dream/STALE_PROPOSALS.md` | `scripts/dream/stale_archive.py` |

End-to-end entry point: `bash scripts/dream/run_nightly.sh` (or `--self-test` for dry-run validation).

---

## Self-tune layer

The dream can self-edit its own infrastructure. Three sub-systems enforce safety:

1. **`scripts/dream/self_tune.py`** — scope guard + validators
   - Allow-list: `scripts/dream/*.{py,sh}`, `.zcode/hooks/*.sh`, `dream/LESSONS.md`, `dream/MEMORY_PATCHES/*.md`, `dream/STATE/*`, `dream/SELF_TUNE_LOG.md`, `dream/STALE_PROPOSALS.md`, new `dream/*.md`
   - Deny-list (wins): `AGENTS.md`, `00_METHODOLOGY/AGENTS.md`, `02_CASES/*/PROJECT_STATE.md`, `02_CASES/GLOBAL_PROJECT_STATE.md`, `02_CASES/*/progress.json`, `00_METHODOLOGY/dependency_graph.yaml`, `00_METHODOLOGY/PREPROCESSING_by_domain/domains/**`
   - Pre-commit validation: `py_compile` + `--help` for Python, `bash -n` + source smoke for Bash
   - Commit prefix enforcer: refuses anything not starting with `[DREAM SELF-TUNE]`

2. **`scripts/dream/auto_tune.py`** — applies mechanical intents
   - Reads intents from `dream/STATE/self_tune_intents.json` (one JSON per line)
   - Intent generators: `drift_escalation`, `amendment_parser_blindspot_annotation`, `self_tune_log_append`
   - Each change validated via `self_tune.validate_file`; rollback on validation failure

3. **`scripts/dream/regression_check.py`** — watchdog + auto-revert
   - Walks the last N days of `[DREAM SELF-TUNE]` commits
   - Re-runs the regression suite (syntax check + `--self-test`)
   - If any commit fails: logs to `dream/STATE/regression_failures.log`, runs `git revert --no-edit`, appends the revert to `dream/SELF_TUNE_LOG.md`

---

## Run manually

```bash
# Step 1: deterministic reports
python3 scripts/dream/adoption_audit.py     # writes dream/ADOPTION_REPORT.md
python3 scripts/dream/reconcile.py          # writes dream/RECONCILIATION.md

# Step 4: brief (read-only)
bash scripts/dream/brief.sh                 # stdout, ≤40 lines

# Step 7-8: self-tune + stale-archive (auto-edit pass)
python3 scripts/dream/auto_tune.py --dry-run     # preview only
python3 scripts/dream/stale_archive.py --dry-run # preview only

# End-to-end pipeline (all 8 steps in one go)
bash scripts/dream/run_nightly.sh --dry-run

# Validators
python3 scripts/dream/self_tune.py --self-test        # scope + commit guard
python3 scripts/dream/auto_tune.py --self-test        # intent generators
python3 scripts/dream/stale_archive.py --self-test    # archive mechanics
python3 scripts/dream/regression_check.py --self-test # revert mechanics
```

## Run nightly (ZCode scheduled job)

A daily automation at 23:55 (Mon-Fri; cron `55 23 * * 1-5`) runs `bash scripts/dream/run_nightly.sh`. The orchestrator prompt handles steps 2, 3, 5, 6 (LLM-driven); the deterministic scripts handle steps 1, 4, 7, 8. Steps 7-8 are new as of 2026-09-03.

## What the dream is **not**

- Not an autonomous AGI. The orchestrator (LLM) still drives intent emission; the dream executes and validates them.
- Not a token-saving mechanism. The brief is short; the consolidation step is heavy but off-session.
- Not magic. The audit is regex-and-JSON over transcripts; reconciliation is `git log` + `grep`. Both fail in interesting ways and the reports say so explicitly.
- Not a state-file editor. P7 still blocks writes to methodology/state files; this is the non-negotiable line.

## Why this exists

Adoption is measured, not assumed. The KG has a `.kg_usage.log`; the dream makes the rest of the methodology measurable the same way. If a step is in the pre-flight but never appears in any transcript, the report proposes either wiring it up (e.g. via hook) or removing it from the pre-flight text. That closes the loop between "the methodology says X" and "X actually happens".

The self-tune layer (added 2026-09-03) closes a second loop: when the dream detects a recurring failure mode in its own heuristics (parser blindspots, drift stagnation), it can mechanically patch its own scripts instead of asking the human to do it.

## Sources / background

The "offline memory consolidation" idea is shared across long-running-agent designs; the closest publicly documented implementations live at:

- Memory consolidation in long-running agents — general background (search: "ai agent offline memory consolidation")
- SkillNet paper for the skills-as-assets framing that this repo also uses: https://arxiv.org/abs/2603.04448
- Critical take ("memory debt management"): https://ai.plainenglish.io/claude-dreaming-is-not-self-improvement-it-is-memory-debt-management-with-better-branding-d31de83b2437
