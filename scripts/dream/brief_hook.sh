#!/usr/bin/env bash
# brief_hook.sh — thin SessionStart hook wrapper for brief.sh.
#
# Runs the plain-Markdown brief.sh, captures stdout, and emits a strict JSON
# envelope that the ZCode harness parses into `additionalContext`.
#
# Always exits 0 (per the hook contract). Output truncated to 4000 chars to
# respect hook context budget.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

plain=$(bash "$REPO_ROOT/scripts/dream/brief.sh")
plain=${plain:0:4000}

python3 -c "
import json, sys
text = sys.argv[1]
print(json.dumps({
    'hookSpecificOutput': {
        'hookEventName': 'SessionStart',
        'additionalContext': text,
    }
}))
" "$plain"
