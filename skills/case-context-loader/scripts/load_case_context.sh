#!/usr/bin/env bash
# load_case_context.sh — compact status chain for AEGIS case studies.
#
# Prints: GLOBAL_PROJECT_STATE header -> case PROJECT_STATE header ->
# progress.json phase summary -> each phase's PROJECT_STATE header.
#
# Usage:
#   load_case_context.sh              # all cases, brief
#   load_case_context.sh Case_01      # one case (also: 01, tinytask, ...)
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
CASES_DIR="$REPO_ROOT/02_CASES"
GLOBAL="$CASES_DIR/GLOBAL_PROJECT_STATE.md"

hdr() { printf '\n%s\n%s\n' "────────────────────────────────────────────────────────" "  $1" "────────────────────────────────────────────────────────"; }

resolve_case() {
  local sel="$1" d name
  for d in "$CASES_DIR"/Case_*/; do
    [ -d "$d" ] || continue
    name="$(basename "$d")"
    # exact/prefix/substring match, case-insensitive
    if [[ "${name,,}" == *"${sel,,}"* ]]; then echo "${d%/}"; return 0; fi
  done
  return 1
}

phase_summary() {
  python3 - "$1" <<'PY'
import json, sys
try:
    d = json.load(open(sys.argv[1]))
except Exception as e:
    print(f"  (progress.json unreadable: {e})"); raise SystemExit
print(f"  case={d.get('case','?')}  current_phase={d.get('phase','?')}")
for k, v in sorted(d.get("phases", {}).items()):
    print(f"  {k}: status={v.get('status','?')} gate={v.get('gate','?')} completed={v.get('completed_at','—')}")
ac = d.get("active_contracts") or []
if ac:
    print(f"  active_contracts: {', '.join(str(c) for c in ac[:5])}")
PY
}

show_case() {
  local case_dir="$1" brief="${2:-full}"
  local name; name="$(basename "$case_dir")"
  hdr "$name"
  if [ -f "$case_dir/PROJECT_STATE.md" ]; then
    head -n 8 "$case_dir/PROJECT_STATE.md" | sed 's/^/  /'
  else
    echo "  (no PROJECT_STATE.md at case root)"
  fi
  if [ -f "$case_dir/progress.json" ]; then
    echo "  ── progress.json:"
    phase_summary "$case_dir/progress.json" | sed 's/^/  /'
  fi
  if [ "$brief" = "full" ]; then
    local pd
    for pd in "$case_dir"/[0-9][0-9]_*/; do
      [ -d "$pd" ] || continue
      if [ -f "$pd/PROJECT_STATE.md" ]; then
        echo "  ── $(basename "$pd"):"
        head -n 6 "$pd/PROJECT_STATE.md" | sed 's/^/     /'
      fi
    done
  fi
}

[ -d "$CASES_DIR" ] || { echo "load_case_context: no 02_CASES at $REPO_ROOT" >&2; exit 1; }

hdr "GLOBAL PROJECT STATE"
[ -f "$GLOBAL" ] && head -n 10 "$GLOBAL" | sed 's/^/  /' || echo "  (missing)"

sel="${1:-all}"
if [ "$sel" = "all" ]; then
  for d in "$CASES_DIR"/Case_*/; do [ -d "$d" ] && show_case "${d%/}" brief; done
else
  case_dir="$(resolve_case "$sel")" || { echo "load_case_context: no case matches '$sel'" >&2; exit 1; }
  show_case "$case_dir" full
fi
