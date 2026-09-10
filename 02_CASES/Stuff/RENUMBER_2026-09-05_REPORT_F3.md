---
document_id: AEGIS-RENUMBER-F3-REPORT
title: RENUMBER F3 Executor Report — Case_02 flat renumbering
phase: 3
version: 1.0
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
---

# RENUMBER F3 Report — Case_02_SecureBorder_Solutions (2026-09-05)

Rubric: `REALIZATION_CLASS_RUBRIC.md` v1.10 §5B rule 7. Plan: `RENUMBER_CAMPAIGN_2026-09-05.md`.
Registry: `00_METHODOLOGY/validation/RENUMBER_REGISTRY_2026-09-05.md` (Case_02 section filled:
36-row old→new table + group-grammar mappings + legacy protection list + re-anchor list).

## Method

Census first (Doc21 `#### Use-Case: {U.C.x.y.z}` headings §6 + §7 tables + subtree grep
md/py/csv): **36 live dotted ids** — 15 compliance (§7, same dotted grammar as product;
`UC-DP..UC-TRN` are domain labels, not UC ids — unchanged) → **UC-01..UC-15**; 21 product
(§6, U.C.8..12) → **UC-16..UC-36**, ascending natural by numeric components. Two-phase
word-boundary rename (dotted id → `TMP-UC-NN` → `UC-NN`), line-oriented, 12 files changed,
618 lines replaced, zero content deletions. `PROC-01..27` / `CAP-01..10` untouched.

Compound grammars handled deterministically (full table in the registry): ranges
`U.C.1–U.C.7`/`U.C.1–7` → `UC-01..UC-15`; `U.C.8–12`/`U.C.8+`/`U.C.8.x–12.x`/`U.C.8.*–U.C.12.*`
→ `UC-16..UC-36`; wildcards `U.C.8.x`/`U.C.8.x.y`/`U.C.8.*` → `UC-16..UC-22`, `U.C.10.x` →
`UC-27..UC-30`, `U.C.11.x` → `UC-31..UC-33`; sub-ranges with retired endpoints resolve inside
the live span (`U.C.9.1.1–9.5.1` → `UC-23..UC-26`; `U.C.12.1.1–12.4.1` → `UC-34..UC-36`);
bare continuation tails (`…UC-24/9.3.1/9.4.1`, `…UC-27/10.3.1/10.5.1`, `UC-16/8.4.1`,
Annex A chain `8.4.1/8.1.1 → 8.2.1 …`) mapped explicitly.

Historical provenance protected (kept the ids they named): Doc31 "Formerly" column (37 rows),
Doc27 "(formerly U.C.x.y.z)" tree annotations, Doc21 §6.6 "Formerly" blockquote + Lane Naming
section + §6 v1.3 nomenclature blockquote + id-grammar template line, all version-history
rows (incl. Doc21 v1.0 "(44 UCs: …)" release row), Doc23 v1.1 row pairing
"U.C.10.1.1/PROC-24", and frozen records under `**/validation/` +
`02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md`. `progress.json` immutable — untouched.
`validation/build_control_set.py` remains modified from prior uncommitted human work —
untouched. Mermaid/PlantUML fences byte-preserved.

## Files changed

- Doc21 v1.5→**v1.6**: §6 heading re-anchored (`UC-16..UC-36`), §9 detail headings
  (`UC-01`/`UC-05`), all §7/§8/§10–§13 live ids renamed; v1.6 version-history row; RENUMBER
  paragraph appended to the Lane Naming section. §2 metadata `totalUseCases=36` (already
  correct) now matches the census exactly.
- Doc22, Doc23, Doc24, Doc27, Doc28, Doc29, Doc30, Doc31: live ids + range grammars renamed;
  Doc31 articulation gains a v1.2 RENUMBER note ("Formerly" column and PROC/CAP ids
  unchanged); Doc31 frontmatter 1.1→1.2.
- PROJECT_STATE.md §7.1 (live next-steps table): 3 stale refs to ids retired by LANE NAMING
  re-anchored to their owning lane cards — `U.C.2.7.1`→`PROC-08`, `U.C.6.3.1`→`PROC-20`,
  `U.C.2.8.1`→`PROC-09`.
- `scripts/build_traceability_matrix_rich.py`: `UC_RE` → `\bUC-\d{2}\b`, §11 section parser →
  new-id headings, COVER source label updated (syntax-checked); xlsx regenerated (9 sheets;
  stats: 63 rules / 84 FRs / 56 NFRs / 38 gates).
- `scripts/verify_rich.py`: CHK-5 moved to the flat id space — now reports
  `unique UC ids=36 … metadata totalUseCases=36 (v1.0 release row claims 44 — historical,
  informational)`. The 44-claim the old CHK-5 parsed lives in the protected v1.0
  version-history row (informational by design; pass/fail unaffected).
- `annexes/A_Use_Case_Diagrams.md` v1.1→**v1.2**: 6 ` ```plantuml ` blocks updated (ovals
  `UC-16..UC-36`; internal aliases `UC811`-style and §1 package ovals kept); all 6 SVGs
  re-rendered via `https://www.plantuml.com/plantuml/svg/~h<hex>` with browser UA; each
  validated `<svg` prefix + >500 B (5940–14047 B). Filenames unchanged (A_s1 system-wide
  byte-stable).
- `annexes/B_Sequence_Diagrams.md` v1.1→**v1.2**: 21 headings now
  `## §N — Use-Case — {UC-NN}`. Old→new mapping strictly monotonic
  (U.C.8.1.1→UC-16 … U.C.12.3.1→UC-36), so no reordering; §1..§21 ↔ UC-16..UC-36 verified,
  and Doc21's 21 `> **Sequence diagram:** → Annex B §N` pointers remain 1:1.

## Gates (verbatim summaries)

| Gate | Result |
|---|---|
| `verify_rich.py` | `8 checks, 2 FAIL, 6 PASS` — CHK-4 dangling `BPR-D-02.2-001`/`BPR-D-10.2-002` + CHK-6 `FR-76`/`FR-82` → `BPR-D-10.2-002`: exactly the C2 pre-existing baseline FAILs, unchanged |
| `scripts/traceability_audit.py Case_02` | `63/63 = 100.0%` ctrl→obj · `88/88 = 100.0%` uc→obj_or_ctrl; all gap lists 0 |
| `/tmp/mermaid_check.py` | `# TOTAL 192 · FAIL 0 · OK 192` (same block count as F1/F2 baseline) |
| `test_dashboards.py` | `# all 16 dashboard(s) passed smoke` |

Visual spot-check: headless Chromium screenshot of
`A_s2_pkg_8_traveller_egate_journey_7_use_case.svg` draws correctly — PKG-8 rectangle,
UC-16..UC-22 ovals with titles, Traveler/BCO/SOC/DPO/NBA actors and `<<extend>>` edges.

## Residuals / escalations

- Residual dotted-id occurrences after rename are exclusively protected historical
  provenance (Doc31 Formerly column, Doc27 formerly-annotations, Doc21 §6.6 blockquote +
  Lane Naming + v1.3 nomenclature note + version rows, Doc23 v1.1 pairing row, frozen
  `**/validation/` records). **0 live old-id references remain** (0 `TMP-UC-*` leftovers).
- `Doc21` MUC-07 inventory row cites `U.C.2.4.2`, an id that never existed in C2's live
  catalog (Case_01-family reference; the doc itself already carries a parenthetical noting
  it does not exist) — left verbatim, informational.
- Stale count claims in live prose predating UC SEPARATION (Doc22 §"47 compliance / 26
  product", Doc27 §3.1/tree "47/26") were not touched — id tokens renamed only; the counts
  describe the pre-SEPARATION tree and are flagged here for a future F4/Validator pass.
- Known limitation (plan-documented): KG build E3 frozen — `kg.sh` does not resolve
  UC-01..36 until the next rebuild.
- Side effect outside case scope (tool-owned, same as F2): `scripts/traceability_audit.py`
  regenerated `00_METHODOLOGY/validation/TRACEABILITY_AUDIT_2026-09-05.md` (Case_02 100%
  with the new ids).
- None blocking; no escalations.
