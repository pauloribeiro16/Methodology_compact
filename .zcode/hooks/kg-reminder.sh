#!/usr/bin/env bash
# .zcode/hooks/kg-reminder.sh
# -----------------------------
# Contract AEGIS-GRAPHIFY-REMINDER-001 (2026-08-25).
#
# graphify reminder — fires once per session when an AEGIS ID is detected in
# a UserPromptSubmit prompt. Reads the prompt from stdin (ZCode passes the
# prompt content as the hook input) and exits 0 silently if the user has
# already seen the reminder this session.
#
# Design (see plan):
#   - Event:  UserPromptSubmit
#   - Match:  IDs in AGENTS.md Reference Index P5 scope:
#            SR-NIS2-XXX, SO-NIS2-XXX, RULE-D-XX.X, REQ-D-XX.X, D-XX.Y,
#            NIST-CSF, NIST-PF
#   - Action: injects a single additionalContext line reminding about
#            `scripts/kg.sh where <ID> (from repo root)`.
#   - Cooldown: per-session sentinel in $XDG_CACHE_HOME/zcode-graphify-reminder/
#   - Exit:   always 0 (non-blocking; reminder only).
#   - Timeout: 5s (enforced by the caller; this script is sub-second).

set -euo pipefail

PROMPT=$(cat)
SESSION_ID="${ZCODE_SESSION_ID:-${CLAUDE_SESSION_ID:-default}}"
CACHE_DIR="${XDG_CACHE_HOME:-${HOME}/.cache}/zcode-graphify-reminder"
mkdir -p "$CACHE_DIR"
SENTINEL="$CACHE_DIR/${SESSION_ID}"

# Exit silently if already reminded this session.
[ -f "$SENTINEL" ] && exit 0

# Defensive: confirm there is an AEGIS ID in the prompt.
# (The matcher in config.json already filters, but a defensive grep
# ensures we never emit a reminder when ZCode invokes the hook on a
# prompt that no longer contains an ID — e.g. after edits.)
echo "$PROMPT" | grep -qE 'SR-NIS2-[0-9]+|SO-NIS2-[0-9]+|RULE-D-[0-9.]+|REQ-D-[0-9.]+|D-[0-9]+\.[0-9]+|NIST-(CSF|PF)' || exit 0

# Mark the session as reminded.
touch "$SENTINEL"

# Emit the reminder as JSON for ZCode to inject as additionalContext.
cat <<'EOF'
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "graphify reminder: AEGIS IDs detected in this turn. Per AGENTS.md P5, the Knowledge Graph should be queried before proposing changes. Try: scripts/kg.sh where <ID> (from repo root). This reminder fires once per session."
  }
}
EOF