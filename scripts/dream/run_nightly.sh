#!/usr/bin/env bash
# run_nightly.sh — End-to-end Dream nightly pipeline.
#
# Steps (matches the orchestrator-side prompt):
#   1. Deterministic reports: adoption_audit.py + reconcile.py
#   2. Read ADOPTION_REPORT.md + RECONCILIATION.md; diff vs prior commit
#   3. Append net-new LESSONS entries (LLM step — skipped in --self-test)
#   4. brief.sh + line-budget check (≤40)
#   5. Commit dream/* updates with [DREAM YYYY-MM-DD] prefix
#   6. Memory consolidation (LLM step — skipped in --self-test)
#   7. SELF-TUNE PASS: auto_tune.py reads intents from
#      dream/STATE/self_tune_intents.json, applies them, commits with
#      [DREAM SELF-TUNE] prefix
#   8. STALE-PROPOSAL ARCHIVE: stale_archive.py moves amendments >=5 cycles
#      to dream/STALE_PROPOSALS.md
#
# Usage:
#   bash scripts/dream/run_nightly.sh              # full nightly run
#   bash scripts/dream/run_nightly.sh --dry-run    # preview only, no commits
#   bash scripts/dream/run_nightly.sh --self-test  # all --self-test flags + dry-run
#
# P7 boundary (enforced by self_tune.py):
#   - Steps 1-6 NEVER touch P7-protected files (read-only).
#   - Steps 7-8 may WRITE to dream/*, scripts/dream/*, .zcode/hooks/*
#     but ALWAYS via self_tune.py scope guard.

set -eo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

DRY_RUN=0
SELF_TEST=0
for arg in "$@"; do
  case "$arg" in
    --dry-run)   DRY_RUN=1 ;;
    --self-test) SELF_TEST=1 ;;
    *) echo "run_nightly: unknown arg: $arg" >&2; exit 2 ;;
  esac
done

DATE="$(date -I)"
DREAM_ARGS=()
if [ "$SELF_TEST" = "1" ]; then
  DREAM_ARGS+=(--self-test)
fi
if [ "$DRY_RUN" = "1" ]; then
  DREAM_ARGS+=(--dry-run)
fi

log() { echo "[run_nightly $(date -Iseconds)] $*"; }
fail() { echo "[run_nightly] FAIL: $*" >&2; exit 1; }

# --- Step 1: deterministic reports ---
log "Step 1: adoption_audit + reconcile"
python3 scripts/dream/adoption_audit.py
python3 scripts/dream/reconcile.py

# --- Step 2: read + compare (LLM step in production — skipped here) ---
# The orchestrator reads ADOPTION_REPORT.md + RECONCILIATION.md, diffs vs
# git log -- dream/, and decides what to log to LESSONS.md. This script
# only emits the deterministic parts.

# --- Step 3: LESSONS append (LLM step — skipped) ---
if [ "$SELF_TEST" = "0" ]; then
  log "Step 3: LESSONS append (LLM-driven, outside this script)"
fi

# --- Step 4: brief.sh + line-budget check ---
log "Step 4: brief.sh"
brief_out="$(bash scripts/dream/brief.sh 2>/dev/null || true)"
brief_lines="$(printf '%s\n' "$brief_out" | wc -l)"
log "brief.sh produced $brief_lines lines (limit 40)"
if [ "$brief_lines" -gt 40 ]; then
  log "WARNING: brief.sh exceeded 40 lines — investigate"
fi

# --- Step 5: dream/* commit (LLM step — orchestrator commits) ---
if [ "$SELF_TEST" = "0" ] && [ "$DRY_RUN" = "0" ]; then
  log "Step 5: orchestrator commits dream/* with [DREAM $DATE] prefix"
fi

# --- Step 6: memory consolidation (LLM step — skipped) ---
if [ "$SELF_TEST" = "0" ]; then
  log "Step 6: memory consolidation (LLM-driven, outside this script)"
fi

# --- Step 7: SELF-TUNE PASS ---
log "Step 7: auto_tune.py apply-intents"
if [ "$SELF_TEST" = "1" ]; then
  # In self-test mode, --self-test is handled by auto_tune.py itself
  python3 scripts/dream/auto_tune.py --self-test || fail "auto_tune self-test"
else
  python3 scripts/dream/auto_tune.py "${DREAM_ARGS[@]}" || fail "auto_tune apply-intents"
fi

# --- Step 8: STALE-PROPOSAL ARCHIVE ---
log "Step 8: stale_archive.py"
if [ "$SELF_TEST" = "1" ]; then
  python3 scripts/dream/stale_archive.py --self-test || fail "stale_archive self-test"
else
  python3 scripts/dream/stale_archive.py "${DREAM_ARGS[@]}" --threshold 5 || fail "stale_archive"
fi

log "DONE — all 8 steps completed"
