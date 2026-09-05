---
document_id: AEGIS-VALID-RENUMBER-REGISTRY
title: RENUMBER Registry — Flat 1..N Lane Ids (old→new per case)
phase: 3
version: 1.0
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
---

# RENUMBER Registry — old→new lane id mapping (3 cases)

Rubric: `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` v1.10 §5B rule 7 (compact
renumbering — flat 1..N per lane per case, no gaps, no retired numbers, dotted
`U.C.x.y.z` flattened). Campaign plan: `02_CASES/RENUMBER_CAMPAIGN_2026-09-05.md`.

Rules:
- Renames applied in **two phases** (old → `TMP-<new>` → new), word-boundary exact.
- Historical "formerly" provenance values (`> Formerly UC-NN —` lines, Doc32 "Formerly"
  column, version-history prose describing past numbering) are **not** renamed — they
  keep the ids they named at the time.
- This file is the authoritative old→new traceability record.

---

## Case_03_OmniBank_Financial — F1 (2026-09-05, DONE)

### UC lane (33): flat UC-01..UC-33

| Old | New |
|---|---|
| UC-33 | UC-01 |
| UC-34 | UC-02 |
| UC-63 | UC-03 |
| UC-64 | UC-04 |
| UC-65 | UC-05 |
| UC-66 | UC-06 |
| UC-67 | UC-07 |
| UC-68 | UC-08 |
| UC-69 | UC-09 |
| UC-70 | UC-10 |
| UC-71 | UC-11 |
| UC-72 | UC-12 |
| UC-73 | UC-13 |
| UC-74 | UC-14 |
| UC-75 | UC-15 |
| UC-76 | UC-16 |
| UC-77 | UC-17 |
| UC-78 | UC-18 |
| UC-79 | UC-19 |
| UC-80 | UC-20 |
| UC-81 | UC-21 |
| UC-82 | UC-22 |
| UC-83 | UC-23 |
| UC-84 | UC-24 |
| UC-85 | UC-25 |
| UC-86 | UC-26 |
| UC-87 | UC-27 |
| UC-88 | UC-28 |
| UC-89 | UC-29 |
| UC-90 | UC-30 |
| UC-91 | UC-31 |
| UC-92 | UC-32 |
| UC-93 | UC-33 |

Dotted child variants found in census: `UC-33.1`, `UC-34.1` → renamed consistently to
`UC-01.1`, `UC-02.1`. No other dotted variants exist in Case_03.

### PROC lane (12): PROC-39..50 freed and filled

| Old | New |
|---|---|
| PROC-41 | PROC-39 |
| PROC-42 | PROC-40 |
| PROC-43 | PROC-41 |
| PROC-44 | PROC-42 |
| PROC-45 | PROC-43 |
| PROC-46 | PROC-44 |
| PROC-47 | PROC-45 |
| PROC-48 | PROC-46 |
| PROC-49 | PROC-47 |
| PROC-50 | PROC-48 |
| PROC-51 | PROC-49 |
| PROC-52 | PROC-50 |

Unchanged lanes: `PROC-01..38`, `CAP-01..10`.

---

## Case_01_TinyTask_SaaS — F2 (PENDING)

| Old | New |
|---|---|
| *(to be filled by F2 census — U.C.x.y.z → UC-01..17 compliance, UC-18..40 product)* | |

## Case_02_* — F3 (PENDING)

| Old | New |
|---|---|
| *(to be filled by F3 census — 15 compliance → UC-01..15, U.C.8..12 product → UC-16..36)* | |
