#!/usr/bin/env bash
# guard-bash.sh — PreToolUse hook for Bash tool.
#
# Two responsibilities:
#   1. DENY (exit 2 + stderr reason) on a narrow set of destructive commands:
#      rm -rf /, rm -rf ~, git reset --hard, git push --force to main/master,
#      curl ... | sh, fork bombs.
#   2. ALWAYS LOG one JSON line per call to dream/STATE/bash_use.log
#      (logging never blocks — append fails silently).
#
# Why narrow: false positives are worse than a missed deny here (we can always
# override with the human's approval if a legitimate command hits).
set -uo pipefail

REPO_ROOT="${CLAUDE_PROJECT_DIR:-$PWD}"
LOG="$REPO_ROOT/dream/STATE/bash_use.log"
mkdir -p "$(dirname "$LOG")" 2>/dev/null || true

PAYLOAD="$(cat)"
CMD="$(python3 - <<'PY' <<<"$PAYLOAD"
import json, sys, re
try:
    d = json.loads(sys.stdin.read())
    cmd = (d.get("tool_input") or {}).get("command", "") or ""
    sys.stdout.write(cmd)
except Exception:
    sys.stdout.write("")
PY
)"
# Fallback
if [ -z "$CMD" ]; then
  CMD="$(printf '%s' "$PAYLOAD" | grep -oE '"command"[[:space:]]*:[[:space:]]*"[^"]+"' | head -1 | sed -E 's/.*"([^"]+)"$/\1/')"
fi

deny() {
  echo "guard-bash: DENIED — $1" >&2
  exit 2
}

# Narrow blocklist — anchored regexes against the full command string.
# We deliberately do NOT try to defeat encodings/obfuscations here; that's a
# job for the upstream permission system. These are the obvious footguns.
if printf '%s' "$CMD" | grep -qE '(^|[[:space:]])rm[[:space:]]+(-r[[:space:]]+|-rf[[:space:]]+|-fr[[:space:]]+)*(-[[:space:]]+)*(/|~|[[:space:]]*/)[[:space:]]*$'; then
  deny "rm -rf / or rm -rf ~"
fi
if printf '%s' "$CMD" | grep -qE '(^|[[:space:]])git[[:space:]]+reset[[:space:]]+--hard'; then
  deny "git reset --hard"
fi
if printf '%s' "$CMD" | grep -qE '(^|[[:space:]])git[[:space:]]+push[[:space:]]+(-f|--force(-with-lease)?)[[:space:]]+(origin[[:space:]]+)?(main|master)'; then
  deny "force-push to main/master"
fi
if printf '%s' "$CMD" | grep -qE '(curl|wget)[^|]*\|[[:space:]]*(sudo[[:space:]]+)?(ba)?sh([[:space:]]|$)'; then
  deny "curl/wget piped to shell"
fi
if printf '%s' "$CMD" | grep -qE ':[[:space:]]*\(\)[[:space:]]*\{[[:space:]]*:\|:[[:space:]]*&[[:space:]]*\}'; then
  deny "fork bomb pattern"
fi

# Append one JSON line to the audit log. Truncate the command to keep the
# log parseable; bash can be huge.
TS="$(date -Iseconds 2>/dev/null || date)"
TRUNC="$(printf '%s' "$CMD" | head -c 400)"
# Escape backslashes and quotes for valid JSON
ESC="$(printf '%s' "$TRUNC" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read())[1:-1])')"
LOG_LINE="{\"ts\":\"$TS\",\"truncated_command\":\"$ESC\"}"
printf '%s\n' "$LOG_LINE" >> "$LOG" 2>/dev/null || true

exit 0