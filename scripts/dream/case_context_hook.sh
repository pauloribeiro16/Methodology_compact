#!/usr/bin/env bash
# case_context_hook.sh — SessionStart hook wrapper for the case-context-loader.
#
# Runs `loadcase_context.sh <case>` (with no arg = all cases brief). Wraps
# the stdout Markdown in the strict ZCode hook JSON envelope so the
# harness injects it into the conversation as additionalContext.
#
# This satisfies Dream amendment #1 ("Skills are pre-flight but never
# invoked") by making the case-context-loader skill fire automatically
# on SessionStart, alongside the existing brief_hook.sh.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

plain=$(bash "$REPO_ROOT/skills/case-context-loader/scripts/load_case_context.sh")
plain=${plain:0:6000}

python3 - "$plain" <<'PY'
import json, sys
text = sys.argv[1]
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": text,
    }
}))
PY