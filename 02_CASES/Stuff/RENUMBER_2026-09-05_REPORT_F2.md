---
document_id: AEGIS-RENUMBER-F2-REPORT
title: RENUMBER F2 Executor Report — Case_01 flat renumbering
phase: 3
version: 1.0
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
---

# RENUMBER F2 Report — Case_01_TinyTask_SaaS (2026-09-05)

Rubric: `REALIZATION_CLASS_RUBRIC.md` v1.10 §5B rule 7. Plan: `RENUMBER_CAMPAIGN_2026-09-05.md`.
Registry: `00_METHODOLOGY/validation/RENUMBER_REGISTRY_2026-09-05.md` (Case_01 section filled:
40-row old→new table + group-grammar mappings + legacy protection list).

## Method

Two-phase word-boundary rename (dotted id → `TMP-UC-NN` → `UC-NN`), line-oriented, applied to
all `.md`+`.py` in the case subtree (20 files with id changes; 879/872 lines replaced, zero
content deletions). Census before rename: **40 live dotted ids** (17 compliance U.C.1..6 →
UC-01..17, 23 product U.C.7..11 → UC-18..40, ascending natural by numeric components) —
matches the plan exactly.

Compound grammars handled deterministically (documented in the registry):
- Ranges `U.C.1-6`/`U.C.1–6` → `UC-01..UC-17`; `U.C.7-11`/`U.C.7–11` → `UC-18..UC-40`.
- Wildcards `U.C.k.*`, `U.C.k.l.*`, `U.C.k.x`, `U.C.k.l.x` → the member id range of the
  package/sub-package (e.g. `U.C.7.1.*` → `UC-18..UC-20`); bare package refs likewise
  (Annex A package ovals now e.g. `UC-18..UC-22\nAccount & Access`).
- Special cases: `U.C.5.1.*` → `PROC-10`; `U.C.6.*` → `PROC-15..17` (package 6 has no live
  UCs — its three cards are PROC lane cards).

Historical provenance protected (kept the ids they named): Doc20 frontmatter
sprint6/rewrite-protocol notes, Doc20 §6.1 ID-continuity + §6.2 new-IDs tables (a one-line
RENUMBER-supersedes header note was added, content kept verbatim), Doc32 "Formerly" column,
freeze lines in PROJECT_STATEs, the 18 legacy lane-card dotted ids and their `UC-x.y.z`
spelling in `Phase_3_Functional_Decomposition_Synthesis.md`, and all frozen records under
`03_PHASE3_DECOMPOSITION_RICH/validation/` (SPRINT/VALIDATOR/LINT/RICH_LINT reports —
frozen historical baselines, left untouched per the frozen-record rule). `progress.json`
immutable — untouched. Mermaid/PlantUML fence lines byte-preserved (Annex B: 23 fences, all
with clean `\n` after the fence token).

## Files changed

- Doc20–Doc24, Doc26, Doc27, Doc32, Doc21/22 incl., NIST_ANCHORS, CORPUS_LINKAGE,
  RULE_FREEZE §5 enumeration, Phase_3 synthesis (live ids only), requirements Doc28–Doc31.
- Doc20 v3.2→**v3.3**: §1/§2/§3 heading ranges re-anchored, Lane Naming section gains a
  v3.2→v3.3 RENUMBER paragraph, §6.1 supersede note. Doc32 v1.1→**v1.2** + articulation
  RENUMBER note (Formerly column untouched). Annex A v0.7→**v0.8**, Annex B v1.0→**v1.1**,
  both with RENUMBER notes.
- `scripts/build_traceability_matrix_rich.py`: data tuples renamed; `startswith("U.C.k.")`
  package classification rewritten as new-id tuple checks (syntax-checked); xlsx regenerated
  (12 sheets, 386 rows).
- `annexes/A_Use_Case_Diagrams.md`: 11 ` ```plantuml ` blocks updated (ovals `UC-01..UC-40`;
  internal aliases `UC711`-style kept); all 11 SVGs re-rendered via
  `https://www.plantuml.com/plantuml/svg/~h<hex>` with browser UA; each validated `<svg`
  prefix + >500 B (2193–16182 B). Filenames unchanged.
- `annexes/B_Sequence_Diagrams.md`: 23 headings now `## §N — Use-Case — {UC-NN}`. The
  old→new mapping is strictly monotonic (U.C.7.1.1→UC-18 … U.C.11.3.1→UC-40), so section
  order needed no reordering; §1..§23 ↔ UC-18..UC-40 verified, and Doc20's 23
  `> **Sequence diagram:** → Annex B §N` pointers remain 1:1.

## Gates (verbatim summaries)

| Gate | Result |
|---|---|
| `verify_rich.py` | `[verify_xlsx] sheets=12 … total_rows=386` · `[ok] verify_xlsx PASS` — exit 0 (C1 baseline PASS, no regressions) |
| `scripts/traceability_audit.py Case_01` | `104/104 = 100.0% | 46/46 = 100.0% | 100/100 = 100.0%`; gap lists all 0 |
| `/tmp/mermaid_check.py` | `# TOTAL 192 · FAIL 0 · OK 192` (same block count as F1 baseline) |
| `test_dashboards.py` | `# all 16 dashboard(s) passed smoke` |

Visual spot-check: headless Chromium screenshot of `A_s7_pkg_dp_data_protection_u_c_1.svg`
draws correctly — PKG-DP rectangle, UC-01..UC-04 ovals with titles, DPO/Member/Free-tier
actors and edges.

## Residuals / escalations

- Residual dotted-id occurrences after rename are exclusively protected historical
  provenance (Doc20 §6.1/§6.2 + frontmatter notes, Doc32 Formerly table, legacy lane-card
  ids in "(legacy)" annotations, PROJECT_STATE freeze lines, `validation/` frozen reports).
  **0 live old-id references remain.**
- Known limitation (plan-documented): KG build E3 frozen — `kg.sh` does not resolve UC-01..40
  until the next rebuild.
- Side effect outside case scope: `scripts/traceability_audit.py` regenerates
  `00_METHODOLOGY/validation/TRACEABILITY_AUDIT_2026-09-05.md` on every run (tool-owned
  report refresh; Case_01 now 100% with the new ids). `validation/build_control_set.py`
  remains modified from prior uncommitted human work — untouched.
- None blocking; no escalations.
