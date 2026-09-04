---
document_id: AEGIS-C02-P2-TRACEABILITY-AUDIT
title: Case_02 Traceability Audit (v0 — PORT-PARITY-2)
phase: 3
version: 0.0
created: 2026-09-04
updated: 2026-09-04
author: PORT-PARITY-2 Executor (generated)
status: GENERATED
case: Case_02_SecureBorder_Solutions
---

# Case_02 Traceability Audit (v0 — PORT-PARITY-2)

**Generated:** 2026-09-04
**Case:** Case_02_SecureBorder_Solutions (SecureBorder Solutions B.V., MEDIUM-LARGE tier, 4 applicable regulations: GDPR, CRA, NIS 2, AI Act)
**Scope:** Phase 3 (Doc21–Doc30 + requirements/Doc29–Doc30) against the Phase 2 rule universe (control_set.yaml, 63 controls = 38 CR + 25 BPR; Doc18_Rules_Catalog.md §4/§5)
**Mode:** STRICT on id resolution (zero unknown orphans required); coverage gaps reported as findings
**Generator:** `../03_PHASE3_DECOMPOSITION/scripts/audit_traceability_v0.py` (mechanical parse; no content invented)

> **GENERATED v0 (PORT-PARITY-2) — pending human review.** Mechanically derived from Doc21–Doc30, requirements/Doc29–Doc30, and ../02_PHASE2_RULES_RICH/control_set.yaml; verify before relying on it.

> Section structure follows Case_03's `../Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md` (the two audits are layer-aligned: C3 audits P1+P2 canonical layers; this C2 v0 audits the P3 layer against the P2 rule universe — the piece C3's audit does not cover).

## 1. Summary

| Metric | Count |
|---|---:|
| Rule universe (control_set.yaml v6.0) | 63 (38 CR + 25 BPR) |
| P3 docs scanned | 10 |
| Distinct rules referenced somewhere in P3 | 63/63 |
| Rules referenced by Doc21 UC catalog | 61/63 |
| Rules referenced by Doc25 allocation | 62/63 |
| Rules verified by Doc26 gates | 46/63 (CR-only layer: gates verify CRs) |
| Rules cited by Doc29 FR 'Source Rule' | 10/63 |
| FRs total / with rule / with '—' | 84 / 59 / 25 |
| Unique gates (Doc26 §5 rows) | 38 |

## 2. Coverage Matrix (rule × P3 layer)

Legend: ✓ = referenced by ≥1 row of that layer; — = none. UC = Doc21; ALLOC = Doc25; GATE = Doc26; FR = Doc29 Source Rule.

| Sub-domain | Rule | Kind | UC | ALLOC | GATE | FR |
|---|---|---|:--:|:--:|:--:|:--:|
| D-01.1 | BPR-D-01.1-001 | BPR | ✓ | ✓ | — | — |
| D-01.3 | BPR-D-01.2-001 | BPR | ✓ | ✓ | — | — |
| D-02.1 | BPR-D-02.1-001 | BPR | ✓ | ✓ | — | — |
| D-02.4 | BPR-D-02.4-001 | BPR | ✓ | ✓ | ✓ | — |
| D-02.4 | BPR-D-02.4-002 | BPR | ✓ | ✓ | ✓ | — |
| D-02.1 | BPR-D-02.5-001 | BPR | ✓ | ✓ | — | — |
| D-03.1 | BPR-D-03.1-001 | BPR | ✓ | ✓ | — | — |
| D-03.1 | BPR-D-03.1-002 | BPR | ✓ | ✓ | ✓ | — |
| D-03.1 | BPR-D-03.5-001 | BPR | ✓ | ✓ | — | — |
| D-04.1 | BPR-D-04.1-001 | BPR | — | ✓ | — | — |
| D-04.2 | BPR-D-04.2-001 | BPR | ✓ | ✓ | ✓ | — |
| D-04.1 | BPR-D-04.5-001 | BPR | ✓ | ✓ | — | — |
| D-05.1 | BPR-D-05.1-001 | BPR | ✓ | ✓ | ✓ | — |
| D-05.1 | BPR-D-05.5-001 | BPR | ✓ | ✓ | — | — |
| D-06.1 | BPR-D-06.5-001 | BPR | ✓ | ✓ | — | — |
| D-07.3 | BPR-D-07.1-001 | BPR | ✓ | ✓ | — | — |
| D-07.1 | BPR-D-07.1-002 | BPR | ✓ | ✓ | ✓ | — |
| D-07.3 | BPR-D-07.5-001 | BPR | ✓ | ✓ | — | — |
| D-08.1 | BPR-D-08.4-001 | BPR | ✓ | ✓ | — | — |
| D-09.1 | BPR-D-09.1-001 | BPR | ✓ | ✓ | — | — |
| D-09.1 | BPR-D-09.5-001 | BPR | ✓ | ✓ | — | — |
| D-10.1 | BPR-D-10.1-001 | BPR | — | — | — | — |
| D-10.2 | BPR-D-10.2-001 | BPR | ✓ | ✓ | ✓ | — |
| D-10.1 | BPR-D-10.4-001 | BPR | ✓ | ✓ | — | — |
| D-10.1 | BPR-D-10.5-001 | BPR | ✓ | ✓ | ✓ | — |
| D-01.1 | CR-D-01.1-001 | CR | ✓ | ✓ | ✓ | ✓ |
| D-01.2 | CR-D-01.2-001 | CR | ✓ | ✓ | ✓ | — |
| D-01.3 | CR-D-01.3-001 | CR | ✓ | ✓ | ✓ | — |
| D-01.4 | CR-D-01.4-001 | CR | ✓ | ✓ | ✓ | — |
| D-02.1 | CR-D-02.1-001 | CR | ✓ | ✓ | ✓ | ✓ |
| D-02.2 | CR-D-02.2-001 | CR | ✓ | ✓ | ✓ | — |
| D-02.3 | CR-D-02.3-001 | CR | ✓ | ✓ | ✓ | — |
| D-02.4 | CR-D-02.4-001 | CR | ✓ | ✓ | ✓ | — |
| D-03.1 | CR-D-03.1-001 | CR | ✓ | ✓ | ✓ | ✓ |
| D-03.2 | CR-D-03.2-001 | CR | ✓ | ✓ | ✓ | — |
| D-03.3 | CR-D-03.3-001 | CR | ✓ | ✓ | ✓ | — |
| D-03.4 | CR-D-03.4-001 | CR | ✓ | ✓ | ✓ | — |
| D-04.1 | CR-D-04.1-001 | CR | ✓ | ✓ | ✓ | ✓ |
| D-04.2 | CR-D-04.2-001 | CR | ✓ | ✓ | ✓ | — |
| D-04.3 | CR-D-04.3-001 | CR | ✓ | ✓ | ✓ | — |
| D-04.4 | CR-D-04.4-001 | CR | ✓ | ✓ | ✓ | — |
| D-05.1 | CR-D-05.1-001 | CR | ✓ | ✓ | ✓ | ✓ |
| D-05.2 | CR-D-05.2-001 | CR | ✓ | ✓ | ✓ | — |
| D-05.3 | CR-D-05.3-001 | CR | ✓ | ✓ | ✓ | — |
| D-05.4 | CR-D-05.4-001 | CR | ✓ | ✓ | ✓ | — |
| D-06.1 | CR-D-06.1-001 | CR | ✓ | ✓ | ✓ | ✓ |
| D-06.2 | CR-D-06.2-001 | CR | ✓ | ✓ | ✓ | — |
| D-06.3 | CR-D-06.3-001 | CR | ✓ | ✓ | ✓ | — |
| D-06.4 | CR-D-06.4-001 | CR | ✓ | ✓ | ✓ | — |
| D-07.1 | CR-D-07.1-001 | CR | ✓ | ✓ | ✓ | ✓ |
| D-07.2 | CR-D-07.2-001 | CR | ✓ | ✓ | ✓ | — |
| D-07.3 | CR-D-07.3-001 | CR | ✓ | ✓ | ✓ | — |
| D-07.4 | CR-D-07.4-001 | CR | ✓ | ✓ | ✓ | — |
| D-08.1 | CR-D-08.1-001 | CR | ✓ | ✓ | ✓ | ✓ |
| D-08.2 | CR-D-08.2-001 | CR | ✓ | ✓ | ✓ | — |
| D-08.3 | CR-D-08.3-001 | CR | ✓ | ✓ | ✓ | — |
| D-09.1 | CR-D-09.1-001 | CR | ✓ | ✓ | ✓ | ✓ |
| D-09.2 | CR-D-09.2-001 | CR | ✓ | ✓ | ✓ | — |
| D-09.3 | CR-D-09.3-001 | CR | ✓ | ✓ | ✓ | — |
| D-09.4 | CR-D-09.4-001 | CR | ✓ | ✓ | ✓ | — |
| D-10.1 | CR-D-10.1-001 | CR | ✓ | ✓ | ✓ | ✓ |
| D-10.2 | CR-D-10.2-001 | CR | ✓ | ✓ | ✓ | — |
| D-10.3 | CR-D-10.3-001 | CR | ✓ | ✓ | ✓ | — |

## 3. Forward Orphans (P3 references to unknown rule ids)

None — every CR-/BPR-D id referenced across Doc21–Doc30 + Doc29/Doc30 resolves against control_set.yaml (0 dangling).

## 4. Backward Orphans (catalog rules never referenced in P3)

None.

| Rule ID | Kind | Sub-domain |
|---|---|---|

**Note:** backward orphans at P3 are concentrated in Doc29's Source Rule column (only 10 rules cited at FR level). Doc25 (allocation) and Doc26 (gates) close most of the gap at the catalogue level; the FR-level gap is the material finding (F5-C2-01 in ../03_PHASE3_DECOMPOSITION/validation/RICH_LINT_BASELINE.md).

## 5. FR-level Source Rule census (Doc29)

- FRs with a resolvable Source Rule: 59/84
- FRs with Source Rule `—` (unmapped): 25 (FR-03, FR-04, FR-09, FR-12, FR-13, FR-26, FR-36, FR-41, FR-42, FR-45, FR-49, FR-51, …)
- Distinct rules reached at FR level: 10 (remaining 53 not FR-traced)

## 6. Gate-layer census (Doc26 §5)

- Unique gate rows: 38 (GATE-D-XX.X-NNN id space)
- Distinct rules verified by ≥1 gate: 46
- Gates reference only CR ids — BPR rules have no dedicated gate in Doc26 (consistent with Doc18's gate criteria being CR-scoped; recorded here as an observation, not an error).

- Gate→rule references that do not resolve: none.

## 7. Findings Summary

| # | Severity | Finding |
|---|---|---|
| F5-C2-01 | HIGH | FR-level rule traceability sparse: 25/84 Doc29 FRs carry Source Rule `—`; only 10 distinct rules cited at FR level. Fix requires Doc29 content edits (out of F5 touch-scope). |
| F5-C2-02 | MEDIUM | Stale count claims in P3 docs (Doc25 “53 rules (38 CR + 15 BP)” / “all 53 compliance rules”; Doc27/Doc21 “44 UCs” vs 47 U.C.* detailed ids + 62 UC-* references) — pre-date the P2 renumbering to 63 controls. |
| F5-C2-03 | LOW | Doc29 contains duplicated FR rows (FR-71, FR-72 appear twice). |
| F5-C2-04 | LOW | Doc21–Doc28 frontmatter lacks the `case:` field (8-field corr-008 completeness: 7/8). |
| F5-C2-05 | INFO | Mixed UC id spaces in Doc21 (U.C.X.Y.Z detailed cards vs UC-SECUREBORDER-2026-NNN catalog id vs UC-XX package labels) — resolves contextually; no dangling refs found. |

## 8. Verification

Re-run with:

```bash
python3 02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/scripts/audit_traceability_v0.py
python3 02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/scripts/verify_rich.py
```
