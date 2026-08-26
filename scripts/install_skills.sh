#!/usr/bin/env bash
# install_skills.sh — symlink repo skills into the ZCode user skills dir.
#
# Skills live versioned in <repo>/skills/<name>/ (SKILL.md + optional scripts/
# and references/). This script links each one into ~/.zcode/skills/ so the
# ZCode session picks them up as invocable skills.
#
# Idempotent: re-running refreshes links. Existing non-symlink entries of the
# same name are never overwritten (reported for manual resolution).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_SRC="$REPO_ROOT/skills"
DEST="${ZCODE_SKILLS_DIR:-$HOME/.zcode/skills}"

[ -d "$SKILLS_SRC" ] || { echo "install_skills: no skills/ at $REPO_ROOT" >&2; exit 1; }
mkdir -p "$DEST"

installed=0; skipped=0
for skill_dir in "$SKILLS_SRC"/*/; do
  [ -f "${skill_dir}SKILL.md" ] || continue
  name="$(basename "$skill_dir")"
  target="$DEST/$name"
  if [ -L "$target" ]; then
    if [ "$(readlink "$target")" = "${skill_dir%/}" ]; then
      echo "  = $name (already linked)"; continue
    fi
    rm "$target"
  elif [ -e "$target" ]; then
    echo "  ! $name exists in $DEST and is not a symlink — skipped (resolve manually)" >&2
    skipped=$((skipped+1)); continue
  fi
  ln -s "${skill_dir%/}" "$target"
  echo "  + $name -> ${skill_dir%/}"
  installed=$((installed+1))
done

echo "Done: $installed new link(s), $skipped conflict(s). Restart the ZCode session to pick up new skills."
