---
document_id: AEGIS-P2-RICH-DIFF
title: Rich vs Legacy — Diff Summary (Phase 2)
phase: 2
version: 1.0
created: 2026-08-07
updated: 2026-08-07
author: Sprint 3 Executor (diff-summary-builder)
status: FINAL
case: Case_01_TinyTask_SaaS
tier: MICRO
sibling_of: ../02_PHASE2_RULES/
branch: feature/aegis-p2-case01-rich
sprint: 3
---

# Rich vs Legacy — Diff Summary (Phase 2)

> Side-by-side comparison of Phase 2 Rich (`02_PHASE2_RULES_RICH/`) vs legacy Phase 2 (`02_PHASE2_RULES/`, as-shipped).
> Used to onboard reviewers. Mirrors `../01_PHASE1_CONTEXT_RICH/RICH_VS_LEGACY.md`.
>
> **State at time of writing:** Sprints 0-3 complete; Sprints 4-5 (field enrichment) pending.

---

## §1 Comparison Summary

| Metric | Legacy `02_PHASE2_RULES/` | Rich `02_PHASE2_RULES_RICH/` | Δ |
|--------|--------------------------:|-----------------------------:|---|
| Phase 2 `.md` documents | 5 | 4 + 3 orchestration | +2 net |
| Phase 2 doc lines | 1,819 | 1,414 | −405 (enrichment pending) |
| Orchestration docs | 0 | 3 (README 255, PROJECT_STATE 205, RICH_VS_LEGACY 219) | +679 lines |
| Validation reports | 0 | 5 (1,273 lines) | +5 |
| Total `.md` lines | 1,819 | **3,366** | **+1,547 (+85%)** |
| Excel sheets | 4 | **14** | **+10** |
| Excel size | 12.7KB | 42.6KB | +29.9KB |
| Tension detail | summary table | 4 × 8 fields, 12 root-cause paragraphs | +32 cells |
| Obligations | 30 | 30 (reconciled, NI re-derived) | 0 |
| Goals | 30 claimed / 31 actual rows | **31** (11 PG + 20 SG, recounted) | +1 corrected |
| Rules | 46 (30 CR + 16 BPR) | 46 (30 CR + 16 BPR) | 0 |
| Source clauses | 53 in traceability matrix | **54** (28 GDPR + 26 CRA, incl. unmapped CRA-C12) | +1 surfaced |
| Data-integrity findings | 0 recorded | **10** (F-01…F-10) | +10 |
| Effort/Cost/Timeline fields | absent | absent (by directive) | 0 |

**Headline:** the Rich folder is not yet larger than legacy *at Phase 2 document level* — Sprints 0-3 built the *scaffolding* (reconciliation tables, expanded tensions, 14-sheet workbook, orchestration docs), which is where the **+1,547 line (+85%)** total growth comes from. The 5-10× growth in the documents themselves arrives in Sprint 5 when 15-field detail cards are populated across 107 cards.

---

## §2 Per-Document Diff

| Doc | Legacy lines | Rich lines | Δ | Diff summary |
|-----|-------------:|-----------:|--:|--------------|
| `08_Obligation_Derivation.md` | 382 | 300 | −82 | Rewritten as a Sprint 1 **reconciliation** doc: obligation count verification, OBL↔goal map (30 rows), OBL↔CR map (30 rows), NI propagation (30 rows), ID integrity, ontology cross-ref (54 clauses), 6 findings. Detail cards deferred to Sprint 5. |
| `09_Strategic_Tensions_Report.md` | 481 | **686** | **+205** | Fully expanded: classification model (structural vs contextual), 4 tensions × 8 fields, **3+ root-cause paragraphs each with verbatim article text**, 12 resolution options, 16 implementation steps, 12 verification criteria, traceability matrix, Phase 1 Doc 07c cross-reference. |
| `10_Privacy_Security_Objectives.md` | 364 | 196 | −168 | Rewritten as a Sprint 1 reconciliation doc: goal recount (11 PG + 20 SG = 31 vs the stale "12 + 18 = 30" summary), goal↔obligation map (31 rows), PG/SG sub-domain coverage, risk-profile redistribution, 5 findings. Detail cards deferred to Sprint 5. |
| `11_Rules_Catalog.md` | 395 | 232 | −163 | Rewritten as a Sprint 1 reconciliation doc: rule counts, CR↔obligation map (30 rows), BPR sub-domain distribution (8 sub-domains), framework source distribution (ISO/NIST/OWASP/CIS), NATIVE vs INHERITED (40/6), NI distribution, 3 findings. Detail cards deferred to Sprints 4-5. |
| `12_Rules_Catalog.md` | 197 | — | — | Legacy companion markdown for the workbook; superseded in Rich Mode by the workbook's own README sheet (Sheet 1). |
| `12_Rules_Catalog.xlsx` | 4 sheets | **14 sheets** | **+10** | See §4. |
| `README.md` | — | 255 | NEW | Orientation, status dashboard, deliverables map, 15-field schema, domain profile, sprint plan, invariants, §8 final status. |
| `PROJECT_STATE.md` | — | 205 | NEW | Status, deliverables, sprint history + verdicts, schema, branch, constraints, open findings. |
| `RICH_VS_LEGACY.md` | — | 219 | NEW | Sprint 3 diff summary (this file). |
| `validation/*.md` | — | 1,273 (5 files) | NEW | LINT_REPORT_BEFORE (121), SPRINT0 (151), SPRINT1 (383), SPRINT2 (329), SPRINT3 (289). |

> **Why three documents shrank.** Legacy Docs 08/10/11 contain the full catalog tables. The Rich versions replace those with *verification* tables that prove the catalog is internally consistent, and defer the enriched per-row cards to Sprints 4-5. The catalog data itself is preserved in full in `12_Rules_Catalog.xlsx` Sheets 2-4, parsed directly from the legacy sources.

---

## §3 Field Additions

Legacy rules carry **11 fields**; the Rich 15-field schema adds operational and traceability dimensions.

| Legacy rule field (11) | Present in Rich | Notes |
|------------------------|:---------------:|-------|
| Rule ID | ✅ | Sheet 2 |
| Rule Description | ✅ | → schema field 2 (expanded to multi-paragraph in Sprint 5) |
| Source | ✅ | → schema field 5 (Source Article) |
| Sub-Domain | ✅ | → schema field 1 |
| Normative Intensity | ✅ | Sheet 6, re-derived under DR-002 |
| Priority | ✅ | → schema field 15 |
| Verification | ✅ | → schema field 8, Sheet 10 |
| Implementation | ✅ | Sheet 7 (NATIVE/INHERITED) |
| Related Goals | ✅ | → schema field 11 (Dependencies) |
| implementation_tier | ✅ | Sheet 4 |
| proportional_priority | ✅ | Sheet 2 |

| New in the 15-field schema | Sprint | Source |
|----------------------------|:------:|--------|
| Scope (field 3) | 5 | Phase 1 Doc 07b §4 |
| Out of Scope (field 4) | 5 | Phase 1 Doc 07b §4 |
| NIST CSF Anchors (field 6) | 5 | Corpus L2 manifests |
| Verification Criteria — 3+ bullets (field 7) | 4 → 5 | Corpus L3 sidecars |
| Owner (field 9) | 4 → 5 | Phase 1 Doc 04d RACI |
| Status (field 10) | 5 | Sprint 5 |
| Risk if not met (field 12) | 5 | Legacy Doc 10 risk profile |
| Affected Stakeholders (field 13) | 4 → 5 | Workbook Sheet 12 |
| Maturity Score (field 14) | 4 → 5 | Phase 1 Doc 04b |
| Regulatory Reporting (case-specific) | 5 | CNPD 72h / ENISA 24h |
| External Auditor (case-specific) | 5 | AWS SOC 2 / ISO 27001 |
| Supervisory Body (case-specific) | 5 | CNPD + ENISA + PT CSIRT |

**Net:** 11 base fields → **15 schema fields + 3 case-specific** = 18 per card. Sprint 3 has added the 4 Sprint-4 stub columns (Owner, Verification Criteria, Maturity Score, Affected Stakeholders) to workbook Sheet 2 as placeholders.

**Deliberately excluded:** Effort, Cost, Timeline — absent from every Rich document and all 14 workbook sheets, per the Phase 2 Rich directive.

---

## §4 New Content

### Multi-paragraph tensions (delivered, Sprint 2)

| Tension | Legacy treatment | Rich treatment |
|---------|------------------|----------------|
| T-001 (D-04.3 notification timing, HIGH contextual) | summary row + short rationale | 8 fields; 3-paragraph root cause quoting GDPR Art. 33 and CRA Art. 14 verbatim; 3 resolution options; 4 implementation steps; 3 verification criteria; max-SLA 24h routing |
| T-M-001 (D-09.2 risk-assessment frequency, MEDIUM structural) | summary row | 8 fields; unified dual-output DPIA + CRA assessment |
| T-M-002 (D-07.1 secure-by-design intensity, MEDIUM structural) | summary row | 8 fields; follow-the-higher-bar decision (CRA NI=3 subsumes GDPR NI=2) |
| T-L-001 (DORA logs vs GDPR erasure, INACTIVE) | summary row | 8 fields; documented as inactive for Case_01 with re-evaluation trigger |

Plus: structural-vs-contextual classification model, cross-regulatory trigger table (5 regulations), 6 tension types from the AEGIS Class Model, and an explicit cross-reference reconciling the *different* T-001…T-004 ID set used by Phase 1 Rich Doc 07c.

### 14-sheet workbook (delivered, Sprint 3)

| # | Sheet | Content | New vs legacy |
|--:|-------|---------|:-------------:|
| 1 | README | Workbook metadata, sheet index, provenance, data-integrity notes | NEW |
| 2 | Rules_Catalog | 46 rules, 11 legacy fields + 4 Sprint 4 stub columns | expanded |
| 3 | Goals_Catalog | 31 goal rows (11 PG + 20 SG) | NEW |
| 4 | Obligations_Catalog | 30 obligations with clauses, NI, obligatedParty, tier, evidence depth | NEW |
| 5 | Tensions_Catalog | 4 tensions with resolution type, chosen resolution, stakeholders | NEW |
| 6 | NI_Propagation | 30 NI derivations, DR-002 recomputed vs legacy, divergences flagged | NEW |
| 7 | Implementation_Modes | NATIVE 40 / INHERITED 6, with AWS + Firebase provider breakdown | NEW |
| 8 | Sub_Domain_Coverage | 30 obligation-bearing + 1 BPR-only + 7 not applicable = 38 | NEW |
| 9 | Framework_Sources | 16 BPR by ISO 27001 (5) / NIST (7) / OWASP (3) / CIS (1) | NEW |
| 10 | Verification_Methods | INSPECT 22 / TEST 14 / DEMONSTRATE 10 / ANALYZE 0 | NEW |
| 11 | Source_Clauses | 54 clauses with article ref, sub-domain, NI, mapped obligation | NEW |
| 12 | Affected_Stakeholders | 8 external + 4 internal, with obligations owed to each | NEW |
| 13 | Schema_15_Fields | Canonical schema + 3 case-specific fields + exclusions | NEW |
| 14 | Sprint_History | Sprint 0-5 metrics and outputs | NEW |

Legacy sheets COVER / COMPLIANCE_RULES / BEST_PRACTICE_RULES / SUMMARY_DASHBOARD are subsumed by Sheets 1, 2 and the analytical sheets. **All workbook figures are parsed from the source documents at build time**, not transcribed, so the workbook cannot silently drift from the markdown.

### Detail cards (planned, Sprints 4-5)

| Document | Cards | Fields | Sprint |
|----------|------:|-------:|:------:|
| `08_Obligation_Derivation.md` | 30 obligations | 450 | 5 |
| `10_Privacy_Security_Objectives.md` | 31 goals | 465 | 5 |
| `11_Rules_Catalog.md` | 46 rules | 690 | 4 (structure) → 5 (content) |
| **Total** | **107** | **1,605** | — |

---

## §5 Frontmatter Changes

| Dimension | Legacy | Rich |
|-----------|--------|------|
| `document_id` | `AEGIS-P2-08`, `AEGIS-P2-09`, … | `AEGIS-P2-RICH-08`, `AEGIS-P2-RICH-09`, `AEGIS-P2-RICH-README`, `AEGIS-P2-RICH-STATE`, `AEGIS-P2-RICH-DIFF`, `AEGIS-P2-RICH-12` |
| `status` | static (`APPROVED` / `FINAL`) | escalating: `SKELETON → RECONCILED → CORPUS_ENRICHED → DEEP_ENRICHED` |
| `status_history` | absent | present on enriched docs (date, status, sprint, author per transition) |
| `sprint` | absent | integer sprint number on every doc |
| `sprint_role` | absent | e.g. `multi_paragraph_tension_expansion`, `final_docs_and_excel` |
| `branch` | absent | `feature/aegis-p2-case01-rich` on every doc |
| `sibling_of` | absent | `../02_PHASE2_RULES/` |
| `expected_*` counters | absent | `expected_obligations: 30`, `expected_fields_per_card: 15`, `expected_tensions: 4`, … |
| `fields_excluded` | absent | `[Effort Estimate, Cost Estimate, Target Timeline]` |
| `sprint_N_verdict` | absent | e.g. `PASS_WITH_FINDINGS` recorded inline |
| `tension_ids_preserved` | absent | `[TENSION-H-001, TENSION-M-001, TENSION-M-002, TENSION-L-001]` |

Current per-document status: Doc 08 `RECONCILED` · Doc 09 `CORPUS_ENRICHED` · Doc 10 `RECONCILED` · Doc 11 `RECONCILED` · README `ACTIVE` · PROJECT_STATE `ACTIVE` · this file `FINAL`.

---

## §6 Invariants

| Invariant | Status | Evidence |
|-----------|:------:|----------|
| Legacy `02_PHASE2_RULES/` unmodified | ✅ | All 8 legacy files retain their pre-sprint mtimes; Rich work is confined to `02_PHASE2_RULES_RICH/` |
| Phase 1 files unmodified | ✅ | `01_PHASE1_CONTEXT/` and `01_PHASE1_CONTEXT_RICH/` read-only throughout |
| Phase 3 files unmodified | ✅ | Not touched in any sprint |
| Corpus unmodified | ✅ | No writes to `00_METHODOLOGY/PREPROCESSING_by_domain/` |
| No Effort/Cost/Timeline | ✅ | Absent from all 4 docs, 3 orchestration files and 14 workbook sheets |
| `AEGIS-P2-RICH-*` IDs | ✅ | All 7 Rich documents |
| No git commits by executors | ✅ | Orchestrator owns the commit workflow (per `AGENTS.md`) |
| Legacy inconsistencies reported, not silently fixed | ✅ | 10 findings F-01…F-10 recorded across Sprint 1 and Sprint 3 reports |

**Tension ID preservation:** the legacy IDs `TENSION-H-001` / `M-001` / `M-002` / `L-001` are carried through as `T-001` / `T-M-001` / `T-M-002` / `T-L-001` with an explicit legacy-ID column, so no cross-reference from Phase 3 breaks.

---

## §7 Sprint Progress

| Sprint | Theme | Status | Verdict |
|--------|-------|:------:|---------|
| 0 | Skeleton + lint baseline | ✅ COMPLETE | PASS |
| 1 | Reconciliation Doc 08↔10↔11 | ✅ COMPLETE | CONDITIONAL_PASS (F-01, F-02, F-04) |
| 2 | Multi-paragraph tensions | ✅ COMPLETE | PASS (32/32 cells) |
| 3 | Final docs + Excel + README + RICH_VS_LEGACY | ✅ COMPLETE | PASS (F-10 raised) |
| 4 | Adjusted fields per row | ⏳ PENDING | — |
| 5 | DEEP enrichment (15 × 107) | ⏳ PENDING | — |
| Validator | Sprint 5 verdict | ⏳ PENDING | — |

**4 of 7 complete.** The documentation and analytical layer is final. What remains is field population:

1. **Sprint 4** — add 6 columns to the Doc 08/10/11 tables (structure only). Workbook Sheet 2 already carries 4 of them as stubs.
2. **Sprint 5** — populate 15 fields × 107 cards (1,605 fields), flip frontmatter to `DEEP_ENRICHED` / v2.0, then Validator review.

**Blocking on human arbiter before Sprint 5:** F-01/F-03 (phantom `PG-D-01.3-001`), F-02 (dual PG+SG coverage), F-04a/F-04b (goal count), F-10 (NI divergence). None blocks Sprint 4.

---

## §8 See also

- `README.md` — orientation + status dashboard + §8 final status
- `PROJECT_STATE.md` — project state, sprint history, open findings
- `12_Rules_Catalog.xlsx` — 14-sheet workbook (Sheet 1 is its own index)
- `validation/SPRINT1_REPORT.md` — reconciliation detail and findings F-01…F-09
- `validation/SPRINT2_REPORT.md` — tension expansion detail
- `validation/SPRINT3_REPORT.md` — Sprint 3 final report and finding F-10
- `../02_PHASE2_RULES/` — legacy Phase 2 (read-only)
- `../01_PHASE1_CONTEXT_RICH/RICH_VS_LEGACY.md` — Phase 1 equivalent of this document
