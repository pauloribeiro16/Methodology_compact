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
# Covers the ID shapes actually in use across the 3 cases:
#   SR-<REG>-NNN  (REG = GDPR|DORA|AIACT|CRA|NIS|NIS2)
#   SO-D-XX.Y     (Phase 2 Security Objectives, also legacy SO-D-NNN)
#   RULE-D-XX.X   (Phase 2 Rules Catalog)
#   REQ-D-XX.X    (Phase 3 Requirements)
#   D-XX.Y        (domain corpus, NIST-style sub-domains)
#   NIST-CSF / NIST-PF
echo "$PROMPT" | grep -qE 'SR-(GDPR|DORA|AIACT|CRA|NIS|NIS2)-[0-9]+|SO-D-[0-9]+(\.[0-9]+)?|RULE-D-[0-9.]+|REQ-D-[0-9.]+|D-[0-9]+\.[0-9]+|NIST-(CSF|PF)' || exit 0

# Mark the session as reminded.
touch "$SENTINEL"

# Append one JSON line per fire to dream/STATE/hook.log so the adoption
# audit can correlate prompts that triggered the reminder. Non-blocking
# on failure (logging is best-effort; the primary purpose of the hook
# is the additionalContext above).
TS="$(date -Iseconds 2>/dev/null || date)"
HOOK_LOG="${CLAUDE_PROJECT_DIR:-.}/dream/STATE/hook.log"
mkdir -p "$(dirname "$HOOK_LOG")" 2>/dev/null || true
# Extract first detected ID for the log (best-effort). Mirrors the regex
# above, so IDs not matched here are silently logged with first_id="".
FIRST_ID="$(printf '%s' "$PROMPT" | grep -oE 'SR-(GDPR|DORA|AIACT|CRA|NIS|NIS2)-[0-9]+|SO-D-[0-9]+(\.[0-9]+)?|RULE-D-[0-9.]+|REQ-D-[0-9.]+|D-[0-9]+\.[0-9]+|NIST-(CSF|PF)' | head -1 || true)"
FIRST_ID="${FIRST_ID:-}"

# Heredoc-based JSON writer: avoids pipefail quirks with stdin redirection.
TS="$TS" SESSION_ID="$SESSION_ID" FIRST_ID="$FIRST_ID" HOOK_LOG="$HOOK_LOG" python3 - <<'PY' 2>/dev/null || true
import json, os, sys
record = {
    "ts": os.environ.get("TS", ""),
    "hook": "kg-reminder",
    "session": os.environ.get("SESSION_ID", ""),
    "first_id": os.environ.get("FIRST_ID", ""),
}
with open(os.environ["HOOK_LOG"], "a", encoding="utf-8") as f:
    f.write(json.dumps(record, ensure_ascii=False) + "\n")
PY

# Emit the reminder as JSON for ZCode to inject as additionalContext.
cat <<'EOF'
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "graphify reminder: AEGIS IDs detected in this turn. Per AGENTS.md P5, the Knowledge Graph should be queried before proposing changes. Try: scripts/kg.sh where <ID> (from repo root). This reminder fires once per session."
  }
}
EOF