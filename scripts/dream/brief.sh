#!/usr/bin/env bash
# brief.sh — compact session-start brief (<=40 lines).
# Designed to be invoked by the SessionStart hook AND manually.
# Reads from dream/ outputs if present (deterministic, no LLM).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

line() { printf "%s\n" "$1"; }

# --- 1. Last commits ---
line "## Last commits"
git -C "$REPO_ROOT" log --pretty=format:"- %h %ad %s" --date=short -n 4 2>/dev/null \
  | sed 's/ *$//' | head -4 || line "  (git log unavailable)"

# --- 2. KG adoption snapshot ---
line ""
line "## KG adoption (last 7d from scripts/.kg_usage.log)"
if [ -f "$REPO_ROOT/scripts/.kg_usage.log" ]; then
  awk -F'\t' '{print $3}' "$REPO_ROOT/scripts/.kg_usage.log" 2>/dev/null \
    | awk '{print $1}' | sort | uniq -c | sort -rn | head -8 \
    | awk '{printf "  %3d  %s\n", $1, $2}' || true
  TOTAL=$(wc -l < "$REPO_ROOT/scripts/.kg_usage.log")
  line "  (total calls: $TOTAL)"
else
  line "  (no log yet)"
fi

# --- 3. Reconciliation drift ---
line ""
line "## State-file drift"
DRIFT_FILE="$REPO_ROOT/dream/RECONCILIATION.md"
if [ -f "$DRIFT_FILE" ]; then
  # Count drift rows in the "State files behind git" table.
  # The table rows start with "| 02_CASES/" (or similar) after the header divider.
  # Match either `| .02_CASES/` (legacy commit format) or `| 02_CASES/` (modern).
  drift_count=$(grep -cE "^\|[ ]+\.?02_CASES/" "$DRIFT_FILE" 2>/dev/null || true)
  drift_count=${drift_count:-0}
  if [ "${drift_count:-0}" -gt 0 ] 2>/dev/null; then
    line "  $drift_count PROJECT_STATE.md file(s) behind git touch — see $DRIFT_FILE"
  else
    line "  none"
  fi
else
  line "  (run scripts/dream/reconcile.py to populate)"
fi

# --- 4. Adoption report flags ---
line ""
line "## Mandated-skill usage"
AUDIT_FILE="$REPO_ROOT/dream/ADOPTION_REPORT.md"
if [ -f "$AUDIT_FILE" ]; then
  case_skills=$(grep -c "case-context-loader" "$AUDIT_FILE" 2>/dev/null || echo 0)
  doc_skills=$(grep -c "doc-conventions" "$AUDIT_FILE" 2>/dev/null || echo 0)
  line "  case-context-loader refs: $case_skills"
  line "  doc-conventions refs:     $doc_skills"
else
  line "  (run scripts/dream/adoption_audit.py to populate)"
fi

# --- 5. Case context (very brief) ---
line ""
line "## Cases (run skills/case-context-loader/scripts/load_case_context.sh <case> for full chain)"
for d in "$REPO_ROOT/02_CASES"/Case_*; do
  [ -d "$d" ] || continue
  name=$(basename "$d")
  status="?"
  if [ -f "$d/progress.json" ]; then
    status=$(python3 -c "import json,sys; d=json.load(open(sys.argv[1])); ps=d.get('phases',{}); print(','.join(f\"{k.split('_')[1]}={v.get('status','?')[:1].upper()}\" for k,v in sorted(ps.items())))" "$d/progress.json" 2>/dev/null || echo "?")
  fi
  line "  $name  [$status]"
done

# --- 6. Pending lessons ---
line ""
line "## Pending human-only items"
[ -f "$REPO_ROOT/dream/LESSONS.md" ] \
  && grep -E "^\- \[" "$REPO_ROOT/dream/LESSONS.md" 2>/dev/null | head -3 \
  || line "  (none)"

# --- 7. One-line actionable ---
line ""
line "Pre-flight: confirm intent+mode+case/phase | case-context-loader | id-impact? | skills OK?"
