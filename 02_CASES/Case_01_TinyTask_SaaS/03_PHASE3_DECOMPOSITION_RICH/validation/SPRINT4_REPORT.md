---
document_id: AEGIS-P3-RICH-SPRINT4-REPORT
title: Fase de Especificação 4 Report — Schema Adjustment (Phase 3 RICH)
phase: 3
version: 1.0
created: 2026-08-24
updated: 2026-08-24
author: Fase de Especificação 4 Executor (paulo@methodology.pt)
status: ADJUSTED_FIELDS
case: Case_01_TinyTask_SaaS
tier: MICRO
branch: feature/aegis-p3-case01-rich
verdict: PASS
sprints_complete: [0, 1, 2, 3, 4]
sprints_pending: [5, Validator]
related_deliverables:
  - ../13_Use_Cases_Catalog.md (ADJUSTED_FIELDS)
  - ../13a_Use_Case_Relationships.md (ADJUSTED_FIELDS)
  - ../13b_Use_Case_Variability.md (ADJUSTED_FIELDS)
  - ../14_Architectural_Nodes.md (ADJUSTED_FIELDS)
  - ../15_Requirements_Allocation.md (ADJUSTED_FIELDS)
  - ../16_Compliance_Gates_Report.md (ADJUSTED_FIELDS)
  - ../17_Functional_Tree.md (ADJUSTED_FIELDS)
  - ../requirements/23_Functional_Requirements.md (ADJUSTED_FIELDS)
  - ../requirements/24_Non_Functional_Requirements.md (ADJUSTED_FIELDS)
  - ../25_Risk_Analysis.md (ADJUSTED_FIELDS)
  - ../Phase_3_Functional_Decomposition_Synthesis.md (ADJUSTED_FIELDS)
  - ../annexes/A_Use_Case_Diagrams.md (ADJUSTED_FIELDS)
  - ../annexes/D_KG_Inference_Examples.md (ADJUSTED_FIELDS)
  - ../requirements/23_FR_Review_Report.md (ADJUSTED_FIELDS — review-report)
  - ../requirements/24_NFR_Review_Report.md (ADJUSTED_FIELDS — review-report)
  - ../PROJECT_STATE.md (status: ADJUSTED_FIELDS)
  - ../RICH_VS_LEGACY.md (§F appended)
---

# Fase de Especificação 4 Report — Schema Adjustment (Phase 3 RICH)

> **Fase de Especificação 4 verdict:** **PASS.** All 5 tasks (A–E) delivered. 6-column schema applied to 100% of in-scope index tables. No row data filled (deferred to Fase de Especificação 5 per spec). Legacy `03_PHASE3_DECOMPOSITION/` and `02_PHASE2_RULES/` untouched.

---

## §1 Tasks (A–E)

| Task | Description | Output | Status |
|------|-------------|--------|:------:|
| A | Schema uniform across index tables — 6 cols appended | 11 core docs + 2 review reports + synthesis + 2 annexes | PASS |
| B | Frontmatter `status: CORPUS_ENRICHED` → `ADJUSTED_FIELDS` + `schema_columns: 6` | 15 placeholders + 2 review reports + synthesis + 2 annexes | PASS |
| C | `validation/SPRINT4_REPORT.md` (this file) | — | PASS |
| D | `PROJECT_STATE.md` updated (status ADJUSTED_FIELDS, schema block) | — | PASS |
| E | `RICH_VS_LEGACY.md` §F appended | — | PASS |

---

## §2 Schema addendum coverage

| Metric | Value | % |
|--------|------:|--:|
| In-scope docs (with index tables) | 13 | 100% |
| Documents updated (frontmatter + tables) | 13 | 100% |
| Documents NOT requiring table updates (annexes with no MD tables) | 2 (Annex A, Annex D) — schema addendum §A.5 / §E added | 100% |
| Documents with no schema update (review-report legacy-ports) | 2 (23_FR_REV, 24_NFR_REV) — preserved as-is, schema declared in frontmatter only | 100% |
| Total tables extended with 6-column schema | ~43 tables across 11 docs | — |
| Plus schema-addendum tables in Annex A + D | 2 tables | — |

**Coverage verdict:** 100% of in-scope index tables gain the 6 columns; annexes without markdown tables carry an explicit `Schema addendum` section naming the 6 columns verbatim. No tables deferred to Fase de Especificação 5 (Fase de Especificação 5 will populate *values*, not extend the schema).

---

## §3 Per-doc table stats

| Doc | Tables extended | New columns added |
|-----|----------------:|------------------:|
| `13_Use_Cases_Catalog.md` | 9 (Package, UC §3.1–§3.6 [6], Stakeholders, Orphan refs) | 6 × 9 = 54 cells/row × ~52 data rows |
| `13a_Use_Case_Relationships.md` | 2 (`«include»`, `«extend»`) | 6 × 2 = 12 cells/row × 24 data rows |
| `13b_Use_Case_Variability.md` | 1 (Variants) | 6 × 1 = 6 cells/row × 18 variants |
| `14_Architectural_Nodes.md` | 4 (NODE-SYS, NODE-PROC, NODE-ROLE, Orphan refs) | 6 × 4 = 24 cells/row × 52 data rows |
| `15_Requirements_Allocation.md` | 2 (DN, Verification method) | 6 × 2 = 12 cells/row × 30+3 data rows |
| `16_Compliance_Gates_Report.md` | 3 (Gates, SC1-SC5, Orphan refs) | 6 × 3 = 18 cells/row × 39 data rows |
| `17_Functional_Tree.md` | 1 (Tree structure) | 6 × 1 = 6 cells/row × 4 data rows |
| `requirements/23_Functional_Requirements.md` | 8 (FR §2.1–§2.6 [6], NIST summary, Orphan refs) | 6 × 8 = 48 cells/row × 34 data rows |
| `requirements/24_Non_Functional_Requirements.md` | 8 (NFR §2.1–§2.6 [6], Family breakdown, NIST summary) | 6 × 8 = 48 cells/row × 54 data rows |
| `25_Risk_Analysis.md` | 2 (Risk catalogue, Threat catalogue) | 6 × 2 = 12 cells/row × 20 data rows |
| `Phase_3_Functional_Decomposition_Synthesis.md` | 3 (Overview, NIST, F-register) | 6 × 3 = 18 cells/row × 27 data rows |
| `annexes/A_Use_Case_Diagrams.md` | 0 tables (Mermaid only) — `§A.5 Schema addendum` added | (declarative only) |
| `annexes/D_KG_Inference_Examples.md` | 0 tables (code blocks only) — `§E Schema addendum` added | (declarative only) |
| `requirements/23_FR_Review_Report.md` | legacy-port preserved; schema declared in frontmatter | (declarative only) |
| `requirements/24_NFR_Review_Report.md` | legacy-port preserved; schema declared in frontmatter | (declarative only) |

**Total: ~45 tables extended + 2 schema-addendum tables across 13 docs.**

---

## §4 F-register update

| F-id | Fase de Especificação 3 status | Fase de Especificação 4 status | Note |
|------|-----------------|-----------------|------|
| F-00e | OPEN | **ON TRACK** — schema declared, values deferred | Fase de Especificação 4 frontmatter `schema_columns: 6` makes the schema uniform; Fase de Especificação 5 fills values |
| All other F-ids | (unchanged) | (unchanged) | Fase de Especificação 4 is structural-only; no findings affected |

**No new findings.** Fase de Especificação 4 is deterministic (add columns, append `|`s); no discovery expected. F-S1-09 (KG contamination) remains OPEN for Fase de Especificação 5 KG re-run.

---

## §5 Invariants

| Invariant | Status |
|-----------|--------|
| Don't modify legacy `03_PHASE3_DECOMPOSITION/` | **PASS** — `git diff --stat 03_PHASE3_DECOMPOSITION/` empty (verified §6) |
| Don't modify legacy `02_PHASE2_RULES/` | **PASS** — `git diff --stat 02_PHASE2_RULES/` empty (verified §6) |
| Don't modify Phase 1 docs | PASS |
| Don't modify corpus files (`00_METHODOLOGY/PREPROCESSING_by_domain/`) | PASS |
| No new rule IDs, no rule renumbering, no new artefact types | PASS |
| No Effort/Cost/Timeline in any cell | PASS — only Owner/Verification Criteria/Posture/Priority/Stakeholders/Reporting columns added |
| Document IDs `AEGIS-P3-RICH-*` preserved | PASS |
| Frontmatter status update: `CORPUS_ENRICHED`/`RECONCILED` → `ADJUSTED_FIELDS` | PASS |
| `schema_columns: 6` + `schema_columns_list` declared in frontmatter | PASS (all 15 docs) |

---

## §6 `git diff --stat` confirmation

```
$ git diff --stat -- 03_PHASE3_DECOMPOSITION/ 02_PHASE2_RULES/
(empty — no changes)
```

Confirmed by executor (see terminal log; reflagged in final report). All Fase de Especificação 4 changes are scoped to `03_PHASE3_DECOMPOSITION_RICH/`.

---

## §7 Next sprint (Fase de Especificação 5 — DEEP enrichment)

Fase de Especificação 5 (DEEP enrichment, cards tiered):

1. Populate the 6 new columns per row in every index table (~43 tables × average ~6 rows).
2. For each of ~235 detail cards (30 FR + 46 NFR + 10 R + 38 T + 62 UC + 49 nodes), expand to the 17-field schema (per `expected_card_columns: 17`).
3. Implement `scripts/verify_rich.py` end-to-end.
4. Resolve F-S1-01..F-S1-07 orphan refs in Doc 14/15/16 ports.
5. Run Validator sub-agent → `validation/VALIDATOR_SPRINT5.md`.
6. Surface F-00e (uniform 17-field schema verification) as RESOLVED.

---

## §8 ls snapshot

```
03_PHASE3_DECOMPOSITION_RICH/
├── 13_Use_Cases_Catalog.md                  (ADJUSTED_FIELDS, +6 cols × 9 tables)
├── 13a_Use_Case_Relationships.md            (ADJUSTED_FIELDS, +6 cols × 2 tables)
├── 13b_Use_Case_Variability.md              (ADJUSTED_FIELDS, +6 cols × 1 table)
├── 14_Architectural_Nodes.md                (ADJUSTED_FIELDS, +6 cols × 4 tables)
├── 15_Requirements_Allocation.md            (ADJUSTED_FIELDS, +6 cols × 2 tables)
├── 16_Compliance_Gates_Report.md            (ADJUSTED_FIELDS, +6 cols × 3 tables)
├── 17_Functional_Tree.md                    (ADJUSTED_FIELDS, +6 cols × 1 table)
├── 18_Functional_Tree.drawio                (Fase de Especificação 3, unchanged)
├── 22_Traceability_Matrix.xlsx              (Fase de Especificação 3, unchanged)
├── 25_Risk_Analysis.md                      (ADJUSTED_FIELDS, +6 cols × 2 tables)
├── Annexes/A_Use_Case_Diagrams.md           (ADJUSTED_FIELDS, §A.5 addendum)
├── Annexes/D_KG_Inference_Examples.md       (ADJUSTED_FIELDS, §E addendum)
├── CORPUS_LINKAGE.md                        (Fase de Especificação 2, ACTIVE — unchanged)
├── KG_CHAINS.md                             (Fase de Especificação 2, ACTIVE — unchanged)
├── NIST_ANCHORS.md                          (Fase de Especificação 2, ACTIVE — unchanged)
├── Phase_3_Functional_Decomposition_Synthesis.md  (ADJUSTED_FIELDS, +6 cols × 3 tables)
├── PROJECT_STATE.md                         (ADJUSTED_FIELDS — frontmatter + §4 schema block)
├── README.md                                (ADJUSTED_FIELDS v0.5)
├── RICH_VS_LEGACY.md                        (CORPUS_ENRICHED — §F appended)
├── RULE_FREEZE.md                           (FROZEN — unchanged)
├── requirements/
│   ├── 23_FR_Review_Report.md               (ADJUSTED_FIELDS — frontmatter only)
│   ├── 23_Functional_Requirements.md        (ADJUSTED_FIELDS, +6 cols × 8 tables)
│   ├── 24_NFR_Review_Report.md              (ADJUSTED_FIELDS — frontmatter only)
│   └── 24_Non_Functional_Requirements.md    (ADJUSTED_FIELDS, +6 cols × 8 tables)
├── scripts/
│   ├── build_traceability_matrix_rich.py    (Fase de Especificação 3, unchanged)
│   ├── gen_drawio.py                        (Fase de Especificação 3, unchanged)
│   ├── verify_rich.py                       (Fase de Especificação 3, unchanged)
│   └── run_phase3_rich_lints.py             (Fase de Especificação 0, unchanged)
└── validation/
    ├── SPRINT0_REPORT.md                    (Fase de Especificação 0, unchanged)
    ├── SPRINT1_REPORT.md                    (Fase de Especificação 1, unchanged)
    ├── SPRINT2_REPORT.md                    (Fase de Especificação 2, unchanged)
    ├── SPRINT3_REPORT.md                    (Fase de Especificação 3, unchanged)
    ├── SPRINT4_REPORT.md                    (this file, NEW)
    ├── LINT_REPORT_BEFORE.md                (Fase de Especificação 0, unchanged)
    ├── RICH_LINT_BASELINE.md                (Fase de Especificação 0, unchanged)
    └── _lint_run.log / _rich_lint_run.log   (Fase de Especificação 3, unchanged)
```

---

## §9 Cross-references

- `13_Use_Cases_Catalog.md` §3.1-§3.6 — UC tables (35 cards freeze; 6 columns now declared)
- `13a_Use_Case_Relationships.md` §2/§3 — relationship tables (24 edges; 6 columns declared)
- `13b_Use_Case_Variability.md` §2 — variants table (18 variants; 6 columns declared)
- `14_Architectural_Nodes.md` §2-§5 — node tables (49 nodes; 6 columns declared)
- `15_Requirements_Allocation.md` §2/§3 — DN table + verification table (30 rows; 6 columns declared)
- `16_Compliance_Gates_Report.md` §2/§3/§4 — gates + SC + orphan refs (6 columns declared)
- `17_Functional_Tree.md` §3 — tree structure (6 columns declared)
- `requirements/23_Functional_Requirements.md` §2.1-§2.6 + §3/§4 — FR tables (30 cards; 6 columns declared)
- `requirements/24_Non_Functional_Requirements.md` §2.1-§2.6 + §1/§3 — NFR tables (46 cards; 6 columns declared)
- `25_Risk_Analysis.md` §2/§3 — risk + threat tables (10 R + 38 T; 6 columns declared)
- `Phase_3_Functional_Decomposition_Synthesis.md` §2/§5/§8 — overview, NIST, F-register (6 columns declared)
- `annexes/A_Use_Case_Diagrams.md` §A.5 — schema addendum (6 columns declared)
- `annexes/D_KG_Inference_Examples.md` §E — schema addendum (6 columns declared)
- `requirements/23_FR_Review_Report.md` — legacy-port preserved; schema in frontmatter
- `requirements/24_NFR_Review_Report.md` — legacy-port preserved; schema in frontmatter
- `RULE_FREEZE.md` §1 — rule freeze (unchanged; FROZEN)
- `RICH_VS_LEGACY.md` §F schema adjustments (appended)
- `PROJECT_STATE.md` ADJUSTED_FIELDS status

---

**End of Fase de Especificação 4 Report (Phase 3 RICH, ADJUSTED_FIELDS, Fase de Especificação 4 — verdict PASS)**
