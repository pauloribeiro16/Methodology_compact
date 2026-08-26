# LESSONS — compact repo gotchas and workarounds

> Curated by hand + appended by the nightly dream. The compact repo lost the main repo's `known_bugs.md`; this file replaces it for the parts that affect work here.

Format: each item is `- [tag] one-line takeaway — context`. Keep ≤40 items; rotate oldest out.

## Tooling

- [KG-quoting] `bash scripts/kg.sh <subcmd> | head` triggers `BrokenPipeError` in stdlib Python — cosmetic only, doesn't affect the data. Use `| sed -n '1,15p'` if it bothers you. — 2026-08-26.
- [KG-nist] `kg.sh nist PR.AC-01` returns "no node labelled" — post 2026-08-24 NIST-id dedup, only some sub-controls have file-derived labels. Workaround: `where "PR.AC"` first to find canonical IDs. — 2026-08-26.
- [KG-trace] `kg.sh trace` with ambiguous labels prints "warning: source match was ambiguous" and proceeds silently on the best score. Use fully qualified labels (`GDPR Art. 32(1)(c)`, not `GDPR Art. 32`). — 2026-08-26.
- [KG-conf] `conceptually_related_to` can carry EXTRACTED confidence. Always quote `(relation, confidence)` as a pair when citing downstream. — 2026-08-26.
- [hook] The kg-reminder hook fires once per session per `~/.cache/zcode-graphify-reminder/<SESSION_ID>` sentinel; cold cache = reminder. Delete the sentinel to force re-fire. — 2026-08-26.

## Repo / paths

- [paths] `02_CASES/GLOBAL_PROJECT_STATE.md` and `02_CASES/README.md` contain ~119 references to `01_IMPLEMENTATION_TOOLS/` and a typo (`01_PHASE1_CONTEXT_RICH`). The compact repo doesn't have these — read with filter. — 2026-08-26.
- [naming] Case_01 uses `03_PHASE3_DECOMPOSITION_RICH/`; Cases 02/03 use `03_PHASE3_DECOMPOSITION/`. The dream's reconcile.py handles both via regex; the load_case_context.sh iterates `[0-9][0-9]_*`. — 2026-08-26.
- [progress] Case_03/progress.json declares `phase: 2` but has a `03_PHASE3_DECOMPOSITION/` folder — minor inconsistency surfaced by reconcile.py. — 2026-08-26.
- [AGENTS-replaced] The compact AGENTS.md (v4.2, 192 lines) replaces the main repo's 194-line AGENTS.md that referenced scripts/kg.sh etc. The compact one is intentionally minimal; consult `00_METHODOLOGY/AGENTS.md` for scoped methodology rules. — 2026-08-26.
- [memory] The project's memory store (`~/.zcode/cli/memories/projects/methodology_compact-1839a9d8746b19ef/memory/`) has `tooling-gap.md` saying KG/lints aren't available — that's true for lints but wrong for KG as of 2026-08-26. The dream's first nightly run will correct this. — 2026-08-26.

## Adoption / process

- [skills-not-firing] `case-context-loader` and `doc-conventions` are mandatory in pre-flight but produced zero detected invocations across the audited sessions. The SessionStart brief.sh now runs the case loader output indirectly; skills remain human/Skill-tool-triggered. — 2026-08-26.
- [impact-real-usage] `kg.sh impact` appears only 1× in transcripts but the canonical `.kg_usage.log` shows 18 KG calls total — agents often invoke via Bash with the subcommand embedded in input, not in the visible text. Audit reconciliation uses `.kg_usage.log` as ground truth. — 2026-08-26.
- [amendments-proposed] ADOPTION_REPORT.md produces ≤5 AGENTS.md amendment proposals per run; the human applies them. The dream never edits AGENTS.md directly (P7). — 2026-08-26.

## Harness (increments) — 2026-08-26

- [guards-blocklist-narrow] `.zcode/hooks/guard-protected-files.sh` deny only the specific READ-ONLY artefacts (domain corpus dir + 2 KG files + .git/**). Blocking `kg/**` would have broken `kg.sh` cache writes. Tested: 3 deny / 3 allow scenarios pass. — 2026-08-26.
- [bash-hook-no-deny-log] `.zcode/hooks/guard-bash.sh` separates concerns: deny on 6 narrow destructive commands (rm -rf /, git reset --hard, force-push to main/master, curl|sh, fork bomb) AND always-log to `dream/STATE/bash_use.log` (the log is consumed by `adoption_audit.py`). Denials are NOT logged (they don't run); allows are. Pattern: "logging never blocks, blocking never logs" — keeps the audit independent from the guard. — 2026-08-26.
- [PreToolUse-parallel-most-restrictive] ZCode docs: when multiple hooks match (e.g. `Write|Edit` matcher + a generic guard), they run in parallel and the most-restrictive decision wins. We registered 2 independent PreToolUse entries (1 per guard); a future `if` filter on the Bash matcher would let them be even more targeted. — 2026-08-26.
- [plugin-install-gui-only] ZCode v3.9.1 on Linux has no CLI-only install path for marketplace plugins — `zcode --help` opens the GUI process. session-report (claude-plugins-official) is present in `~/.zcode/cli/plugins/marketplaces/.../plugins/session-report/skills/` but cannot be installed headless. **Workaround**: install via Settings → Plugin Management → Discover → click `session-report` (2 clicks). If the resulting tool works, the lesson becomes "plugin install is 2 GUI clicks, not a script action". — 2026-08-26.
- [skills-disabled-reversible] Moved 12 stale/duplicate skills to `~/.zcode/skills.disabled/` instead of deleting: `langchain`, `langgraph`, `langfuse`, `llm-observability-stack`, `algorithmic-art`, `slack-gif-creator`, `brand-guidelines`, `web-artifacts-builder`, `docx`, `pdf`, `pptx`, `xlsx`. The Office copies are duplicates of the `document-skills` plugin copies; the others are off-brand. Restoration = `mv ~/.zcode/skills.disabled/<name> ~/.zcode/skills/` + ZCode restart. — 2026-08-26.
- [command-arghint-vs-required] Slash commands in ZCode support `$ARGUMENTS` (whole string) and `$1`-`$N` (positional) but `$ARGUMENTS` is the more forgiving default. `/case` with no arg = show all; `/doc-check` requires a path; `/dream` accepts optional `--since`. — 2026-08-26.

## Renaming (2026-08-26)

- [rename-convention-DocNN] New case-file convention: deliverables are `DocNN_Nome.md` (zero-padded, continuous per case, PascalCase underscores, acronyms in caps); operational files are PascalCase without prefix (`Project_State.md`, `Sprint3_Report.md`); `README.md` is preserved. Migration applied to 95 files (92 deliverables + 3 operational) — `git mv` only, zero content diff. Snapshot at `02_CASES.original-2026-08-26/` (gitignored) is the safety net for rollback. — 2026-08-26.
- [rename-subletter-absorbed] Sub-letter variants (`04a`, `04b`, `04c`, `04d`, `05b`, `07c`, `10b`, `13a`, `13b`) are absorbed into a continuous `DocNN` sequence — they no longer carry their own numeric prefix because the new prefix is sequence-position not content-derived. Cross-case divergent filenames (Goals vs Objectives, Adjusted_Goals vs Adjusted_Objectives) collapsed to a single name because titles were identical. — 2026-08-26.
- [rename-links-functional-only] Per user decision, only **functional** markdown links were auto-updated (14 broken links in `Case_02/01_PHASE1_CONTEXT_RICH/README.md`). Prose mentions of old filenames ("Doc 11", "11_Rules_Catalog") are intentionally left untouched — they are methodological/historical terms that don't break tooling. Trade-off: historical numbering drifts away from new filename numbering. — 2026-08-26.
- [rename-tooling-stable] `skills/case-context-loader/scripts/load_case_context.sh` reads `PROJECT_STATE.md` from case root and phase root — those files were NOT renamed (they're case/phase governance, not deliverables), so the script works unchanged. `scripts/dream/brief.sh` mentions the script by name (no path), also unaffected. Skill `~/.zcode/skills/doc-conventions/SKILL.md` (user-scope) updated to reflect the new convention. — 2026-08-26.
- [rename-script-reusable] `scripts/rename_case_files.py` is now in the repo — `python3 scripts/rename_case_files.py plan` regenerates `dream/RENAME_MAPPING.tsv`; `... apply` runs `git mv` per line. Idempotent (re-running skips entries whose source no longer exists). Useful if the corpus grows and you want to keep DocNN continuous. — 2026-08-26.
