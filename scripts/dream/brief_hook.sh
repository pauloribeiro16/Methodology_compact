#!/usr/bin/env bash
# brief_hook.sh — thin SessionStart hook wrapper for brief.sh.
#
# Runs the plain-Markdown brief.sh, captures stdout, prepends a unique
# sentinel so the orchestrator can confirm the hook actually reached the
# model, and emits a strict JSON envelope that the ZCode harness parses
# into `additionalContext`.
#
# Always exits 0 (per the hook contract). Output truncated to 4000 chars to
# respect hook context budget.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

plain=$(bash "$REPO_ROOT/scripts/dream/brief.sh")
plain=${plain:0:4000}

# Unique-per-run sentinel. If this exact token appears in the model's
# incoming context for the current turn, the hook is being honoured.
# If it does NOT appear, the harness is dropping additionalContext silently
# (e.g. provider/version mismatch).
SENTINEL="__DREAM_HOOK_SENTINEL_$$_$(date +%s)__"

python3 - "$SENTINEL" "$plain" <<'PY'
import json, sys
sentinel, text = sys.argv[1], sys.argv[2]
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": f"[dream-brief-hook-fired marker={sentinel}]\n{text}",
    }
}))
PY
