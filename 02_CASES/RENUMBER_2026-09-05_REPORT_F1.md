---
document_id: AEGIS-RENUMBER-F1-REPORT
title: RENUMBER F1 Executor Report — Case_03 flat renumbering
phase: 3
version: 1.0
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
---

# RENUMBER F1 Report — Case_03_OmniBank_Financial (2026-09-05)

Rubric: `REALIZATION_CLASS_RUBRIC.md` v1.10 §5B rule 7. Plan: `RENUMBER_CAMPAIGN_2026-09-05.md`.
Registry: `00_METHODOLOGY/validation/RENUMBER_REGISTRY_2026-09-05.md` (Case_03 filled; C1/C2 placeholders).

## Method

Two-phase word-boundary rename (old → `TMP-<new>` → new), line-oriented, applied to all
`.md` in the case subtree. Compound forms handled: slash chains (`UC-63/64/65/66/67/68`),
dot ranges (`UC-63..93`, `PROC-41..52`), en-dash ranges (`UC-67–81`, `UC-84–85`, `UC-90–93`,
`UC-86–89`), dotted children (`UC-33.1`→`UC-01.1`, `UC-34.1`→`UC-02.1`). Mermaid/PlantUML
fence lines untouched — every ` ```mermaid ` line preserved byte-for-byte (fence check: 33 in
Annex B, all with clean `\n` after the fence token).

Historical lines protected (kept the ids they named): Doc22 version rows ≤3.0, Doc22 v2.1/v3.0
blockquote notes, Lane Naming v2.2→v3.0 paragraph, PROJECT_STATE UC-Separation line, Doc32
header provenance + Coverage line, Annex B v2.0 note, Annex A PKG-DS history line. Doc22 §4.1
actor "Drives" en-dash ranges and the §4 heading / Annex A "source of truth" range labels were
updated (they state CURRENT numbering). `Formerly` columns/lines untouched.

## Census (whole-word occurrences, md+json+py, before → after)

| Lane | Before (old ids) | After (new ids) |
|---|---|---|
| UC-33→UC-01 | 61 | UC-01: 63 (incl. dotted children) |
| UC-34→UC-02 | 35 | UC-02: 33 |
| UC-63→UC-03 | 46 | UC-03: 45 |
| UC-64→UC-04 | 45 | UC-04: 46 |
| UC-65..92 (24 ids) | 434 | renamed 1:1 (UC-05..UC-32 live) |
| UC-93→UC-33 | 8 | UC-33: 15 |
| PROC-41..52 (12 ids) | 287 | PROC-39..50 live (PROC-39: 34, PROC-50: 27, …) |

Residual old-id occurrences after rename: **0 live**. Remaining matches are exclusively
protected historical provenance (Doc22 §9 rows ≤3.0 + blockquotes, Doc32 header/coverage,
Annex B v2.0 note, PROJECT_STATE UC-Separation line, RICH_LINT_BASELINE UC-99 finding) or
out-of-map legacy labels (`UC-48-Online`, `UC-48-Classroom`, `UC-49-AI`, `UC-52-DORA` —
never members of the 33/12 renamed sets).

## Files changed (git: 611 lines replaced, 611 inserted; zero deletions of content)

- Doc22–Doc29 (8 docs), Doc30/Doc31 (requirements), Doc32 — id tokens + Doc22 v3.1 bump
  (metadata `phase3Status`, version-history row, Lane Naming v3.0→v3.1 note), Doc32 v1.2
  bump + RENUMBER note + registry pointer in articulation paragraph.
- `annexes/A_Use_Case_Diagrams.md` (v1.2): 8 ` ```plantuml ` blocks updated (oval labels
  `UC-01..33`; aliases `UC33/UC63/…` kept); range labels updated.
- `annexes/svg/A_s1..A_s8.svg` — all 8 re-rendered via
  `https://www.plantuml.com/plantuml/svg/~h<hex>` with browser UA; each response validated
  `<svg` prefix and >500 B: 16157 / 13270 / 15205 / 10878 / 11399 / 12433 / 9385 / 4031 B.
  Filenames unchanged.
- `annexes/B_Sequence_Diagrams.md` (v2.1): 33 headings `## §N — Use-Case — {UC-NN}` re-anchored.
  Section order preserved without reordering: the old→new mapping is strictly ascending
  (UC-33→01 … UC-93→33), so §N↔UC-NN alignment holds; Doc22's 33 `> **Sequence diagram:** →
  Annex B §N` pointers re-verified 1:1 (33/33, spot-checked §3↔UC-03, §33↔UC-33).
- NEW: `00_METHODOLOGY/validation/RENUMBER_REGISTRY_2026-09-05.md`.

Untouched, as mandated: `validation/build_control_set.py`, `kg/**`, `domains/**`, other
cases, `progress.json`. No commits made (read-only git).

## Gates (verbatim summaries)

| Gate | Result |
|---|---|
| `verify_rich.py` | `summary: 8 checks, 2 FAIL, 6 PASS` — FAILs are CHK-3 (NFR census 12 vs 56) + CHK-6 (NFR-06/07/09 citations) = the documented pre-existing baseline; no new failures |
| `check_unmapped.py` | `GATE PASS (check_unmapped.py, Case_03 v0.4)` |
| `check_implementation_posture_case03.py` | `GATE PASS (check_implementation_posture.py, Case_03 v0.3)` |
| `scripts/traceability_audit.py Case_03` | `42/42 = 100.0% | 78/78 = 100.0% | 107/107 = 100.0%` |
| `/tmp/mermaid_check.py` | `# TOTAL 192 · FAIL 0 · OK 192` (same block count as baseline; annex A is PlantUML, not mermaid) |
| `test_dashboards.py` | `# all 16 dashboard(s) passed smoke` |

Visual spot-check: headless Chromium screenshot of `A_s8_pkg_ds_privacy_data_subject_ucs_uc_33_uc.svg`
draws correctly — PKG-DS rectangle, UC-01/UC-02 ovals, DPO/Data Subject actors and edges.

## Escalations / residuals

- None blocking. Known limitation (plan-documented): KG build E3 is frozen and does not
  resolve the new ids; `kg.sh impact` output for renamed UC/PROC ids will lag until the next
  KG rebuild.
- Doc22 `DocNN:LINE` catalogue anchors in Doc32 articulation table remain valid: all Doc22
  edits after the anchored card lines were appended below §9 (line positions of §3.2/§4 cards
  unchanged).
