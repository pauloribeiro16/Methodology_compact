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
- [impact-real-usage] `kg.sh impact` appears only 1× in transcripts but the canonical `.kg_usage.log` shows 18 KG calls total — agents often invoke via Bash with the subcommand embedded in the input, not in the visible text. Audit reconciliation uses `.kg_usage.log` as ground truth. — 2026-08-26.
- [amendments-proposed] ADOPTION_REPORT.md produces ≤5 AGENTS.md amendment proposals per run; the human applies them. The dream never edits AGENTS.md directly (P7). — 2026-08-26.
