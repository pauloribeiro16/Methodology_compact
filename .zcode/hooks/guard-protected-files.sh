#!/usr/bin/env bash
# guard-protected-files.sh — PreToolUse hook for Write|Edit|MultiEdit|ApplyPatch.
#
# Deny (exit 2 + stderr reason) when the target path falls under one of:
#   - 00_METHODOLOGY/PREPROCESSING_by_domain/domains/**   (corpus baseline = READ-ONLY)
#   - kg/E3_2026-08-23/graphify-out/graph.json|graph.html (the build artefact)
#   - any .git/**                                         (git internal)
#
# NOT blocked: anything else (kg.sh writes kg/.../cache/last_query_stamp;
# new dirs in 02_CASES/, new scripts, etc.). Blocklist is intentionally
# narrow to avoid false positives that block normal work.
#
# Exit codes (per ZCode hook contract):
#   0 = allow
#   2 = deny (reason on stderr)
#   other = non-blocking error (logged by harness)
set -uo pipefail

REPO_ROOT="${CLAUDE_PROJECT_DIR:-$PWD}"

# Read the JSON payload ZCode sends on stdin.
PAYLOAD="$(cat)"

# Extract tool_input.file_path robustly: tolerate whitespace and missing key.
# Try with python3 first (most robust), fall back to grep if missing.
FILE_PATH="$(python3 - <<'PY' <<<"$PAYLOAD"
import json, sys
try:
    d = json.loads(sys.stdin.read())
    ti = d.get("tool_input") or {}
    fp = ti.get("file_path") or ti.get("path") or ""
    sys.stdout.write(fp)
except Exception:
    sys.stdout.write("")
PY
)"

# Fallback if python3 is not available (extremely rare on Linux):
if [ -z "$FILE_PATH" ]; then
  FILE_PATH="$(printf '%s' "$PAYLOAD" | grep -oE '"file_path"[[:space:]]*:[[:space:]]*"[^"]+"' | head -1 | sed -E 's/.*"([^"]+)"$/\1/')"
fi

# Normalise to absolute path under REPO_ROOT for matching.
case "$FILE_PATH" in
  /*) ABS="$FILE_PATH" ;;
  *)  ABS="$REPO_ROOT/$FILE_PATH" ;;
esac

# Build blocklist patterns as anchored regex against ABS.
deny() {
  echo "guard-protected-files: DENIED — $1" >&2
  exit 2
}

# 1. Corregir nomes para a blocklist (domínio vem antes do file)
if printf '%s' "$ABS" | grep -qE '(^|/)00_METHODOLOGY/PREPROCESSING_by_domain/domains/'; then
  deny "writes under 00_METHODOLOGY/PREPROCESSING_by_domain/domains/ are not allowed (corpus baseline is READ-ONLY)."
fi

# 2. KG build artefacts (strict, sem abranger kg/**; o CLI graphify escreve cache/)
case "$ABS" in
  */kg/E3_2026-08-23/graphify-out/graph.json|*/kg/E3_2026-08-23/graphify-out/graph.html)
    deny "the KG build artefacts (graph.json / graph.html) are read-only here; rebuild on Deucalion per kg/GRAPHIFY.md." ;;
esac

# 3. .git internals
case "$ABS" in
  */.git/*)
    deny ".git/** is owned by git; do not edit directly." ;;
esac

exit 0