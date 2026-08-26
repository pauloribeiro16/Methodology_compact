---
document_id: AEGIS-P2-RICH-DIFF-CASE03
title: Rich vs Legacy — Diff Summary (Phase 2, Case_03)
phase: 2
version: 1.0
created: 2026-08-08
updated: 2026-08-08
author: Rich-Symmetry Executor
status: FINAL
case: Case_03_OmniBank_Financial
tier: MAX
sibling_of: ../02_PHASE2_RULES/
branch: feature/aegis-p2-case03-csf-pf-airmf
---

# Rich vs Legacy — Diff Summary (Phase 2, Case_03)

> Side-by-side comparison of Phase 2 Rich (`02_PHASE2_RULES_RICH/`) vs legacy Phase 2 (`02_PHASE2_RULES/`, as-shipped) for **Case_03 (OmniBank Financial Systems)**.
> Mirrors `../Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md` (Case_01).
>
> **State at time of writing:** All 7 blocos (A reused from Case_02, B→G + Validator) merged into `main` on `feature/aegis-p2-case03-csf-pf-airmf`. Validator Tier 1+2 PASS_WITH_FINDINGS (4 findings addressed, 1 legacy discrepancy documented).

---

## §1 Comparison Summary

| Metric | Legacy `02_PHASE2_RULES/` | Rich `02_PHASE2_RULES_RICH/` | Δ |
|--------|--------------------------:|-----------------------------:|---|
| Phase 2 `.md` documents | 5 | 5 (legacy copies) + 7 orchestration/rich | +7 net |
| Phase 2 doc lines | 2,271 | 2,271 (verbatim copies) | 0 |
| Orchestration docs | 0 | 7 (README, PROJECT_STATE, RICH_VS_LEGACY, SPEC, 10b, Doc 13) | +7 |
| Validation reports | 1 (none) | 9 (8 new + 1 existing VALIDATOR_BLOCOG) | +8 |
| Doc 13 unified matrix | (absent) | **ACTIVE** (3 frameworks) | NEW |
| Excel sheets | n/a | 10 (legacy + 6 new from Bloco F) | +6 |
| Triple-maturity cells | n/a | 234 (3 × 78 cards) | NEW |
| Compliance Rules (CR) | 38 unique | 38 unique | 0 |
| Best Practice Rules (BPR) | 40 unique | 40 unique | 0 |
| Obligations (Doc 08) | 38 | 38 | 0 |
| Privacy Goals (PG) | 24 (76 - 52 SG) | 24 | 0 |
| Security Goals (SG) | 52 | 52 | 0 |
| Tensions | 7 | 7 | 0 |
| Frameworks in scope | n/a | **3 (CSF + PF + AI RMF); DORA via CSF coverage** | NEW (Case_03 has all 5 regulations) |
| DORA-specific framework | n/a | via CSF subcat coverage | NEW |
| AI RMF placeholder | n/a | **NOT PLACEHOLDER — ACTIVE** | distinguishes Case_03 from Case_01 |
| DR-002 resolution | AVG_with_AI_MUST + DORA uniformly MUST | same | unchanged |
| Track B distribution | 31 RIGOROUS + 7 STANDARD + 0 DEFERRED | same | unchanged |
| Active sub-domains | 38/38 (all active) | 38/38 | unchanged |
| Source clauses | GDPR (28) + CRA (26) + NIS 2 (29) + DORA (38) + AI Act (29) = 150 | 150 | 0 |
| Data-integrity findings | 0 recorded | **4 + 1** (FN-01..FN-05 addressed; F-01 legacy documented) | +5 |
| Effort/Cost/Timeline fields | absent | absent (by directive) | 0 |

**Headline:** Case_03 is the **MAX complexity** case (5 regulations applicable, 78 cards, all 38 sub-domains active). Unlike Case_01 (placeholder AI RMF) and Case_02 (HIGH with 4 regs), Case_03 has **all 3 NIST frameworks ACTIVE** + DORA covered via CSF. The Doc 13 unified matrix is the most complete of the 3 cases.

---

## §2 Per-Document Diff

| Doc | Legacy lines | Rich lines | Δ | Diff summary |
|-----|-------------:|-----------:|--:|--------------|
| `08_Obligation_Derivation.md` | 472 | 472 | 0 | **Verbatim copy** of legacy; canonical lives in `../02_PHASE2_RULES/`. |
| `09_Strategic_Tensions_Report.md` | 687 | 687 | 0 | **Verbatim copy** of legacy. |
| `10_Privacy_Security_Objectives.md` | 461 | 461 | 0 | **Verbatim copy** of legacy. Note: summary header says "33 goals" but row count is 76. |
| `11_Rules_Catalog.md` | 651 | 651+ | +banner | **Verbatim copy** + Rich banner pointing to canonical. Block D extensions (fields 19-24, tri-maturidade) live in the canonical `../02_PHASE2_RULES/11_Rules_Catalog.md`. |
| `12_Rules_Catalog.xlsx` | 24KB | 24KB | 0 | **Verbatim copy** of legacy binary. |
| `13_Framework_Mapping_Matrix.md` | — | ~2,800 | NEW | Unified matrix over 3 frameworks (CSF + PF + AI RMF), 6 sub-sections + 2 viz sections, 78 card mappings, 234 triple-maturity cells. |
| `10b_Privacy_Security_Goals_NIST_Implications.md` | — | ~500 | NEW | 76 PG/SG × 3 frameworks implication catalog. |
| `SPEC_NIST_MATRIX_UNIFIED.md` | — | ~1,100 | NEW | 17-decision specification (Case_03 MAX 5-framework scenario with DORA via CSF). |
| `README.md` | — | this repo | NEW | Orientation, dashboard, schema, domain profile, bloco plan. |
| `PROJECT_STATE.md` | — | ~240 | NEW | Project state snapshot (Case_03 specific). |
| `RICH_VS_LEGACY.md` | — | this file | NEW | Case_03-specific Rich vs legacy diff summary. |
| `validation/*.md` | — | ~2,900 | NEW | 9 reports. |

> **Why Doc 08/09/10/11 are byte-identical copies.** The Case_03 contract applied Bloco D field extensions to the canonical `../02_PHASE2_RULES/11_Rules_Catalog.md` (18 fields per card). The Rich copy preserves the legacy 17-field schema for reference.

---

## §3 Field Additions

Legacy rules carry **17 fields**; the Rich 18-field schema adds triple-maturity dimensions.

| Legacy rule field (17) | Present in Rich | Notes |
|------------------------|:---------------:|-------|
| Rule ID | ✅ | Sheet 2 |
| Rule Description | ✅ | field 2 |
| Source | ✅ | field 5 |
| Sub-Domain | ✅ | field 1 |
| Normative Intensity | ✅ | Sheet 6, re-derived under AVG+AI MUST + DORA MUST |
| Priority | ✅ | field 15 |
| Verification | ✅ | field 10 |
| Implementation | ✅ | Sheet 7 |
| Related Goals | ✅ | field 13 |
| implementation_tier | ✅ | Sheet 4 |
| proportional_priority | ✅ | Sheet 2 |

| New in the Rich 18-field schema (Bloco B + D) | Source |
|----------------------------------------------|--------|
| 7. Privacy FW Anchors | corpus L2 manifests |
| 8. AI RMF Anchors | corpus L2 manifests |
| 16. Maturity (CSF) | Doc 13 §4-5 |
| 17. Maturity (Privacy) | Doc 13 §4-5 |
| 18. Maturity (AI RMF) | Doc 13 §4-5 |

**Net:** 17 base fields → **18 schema fields** for Case_03. Triple-maturity model is the defining difference vs Case_01.

**Deliberately excluded:** Effort, Cost, Timeline — absent from every Rich document and all workbook sheets, per the Phase 2 Rich directive.

---

## §4 New Content

### Doc 13 unified matrix (delivered, Bloco C + D + F)

| # | Sub-section | Content |
|--:|-------------|---------|
| 1 | Matriz Unificada | 78 rows (38 CR + 40 BPR) × columns CSF, Privacy FW, AI RMF, ISO 27001, SSDF |
| 2 | Govern Consolidada | 6 conceitos × 3 frameworks |
| 3 | Mapeamento n:m | 78 YAML blocks with rule_id, NI, csf_subcats, priv_subcats, ai_rmf_subcats |
| 4 | Modelo Maturidade | Tiers 1-4 + 0-4 por-subcat (CSF + PF + AI RMF) |
| 5 | Aplicação Case_03 | Per-rule maturity assessment (78 cards × 3 frameworks) |
| 6 | Gap Analysis | Subcats não cobertas por framework |
| 7 | Visualizações | V1 matriz, V2 mapa por Function, V3 Mermaid, V4 heatmap |
| 8 | §6.5 inventory | Bloco G fix addition |

Plus 6 new Excel sheets added (Unified_Matrix, Govern_Consolidated, Mapping_nm, Maturity_Dual, Cov_Function, Heatmap_Maturity).

### 10b PG/SG implications (delivered, Bloco B)

| Goal type | Count | Frameworks |
|-----------|------:|------------|
| Privacy Goals (PG) | 24 | CSF + Privacy FW (primary) + AI RMF where applicable |
| Security Goals (SG) | 52 | CSF (primary) + AI RMF for AI-security-relevant |
| **Total** | **76** | 3 frameworks × 76 = 228 implication rows |

### Triple-maturity cells

| Framework | Cells | Notes |
|-----------|------:|-------|
| CSF 2.0 | 78 | 0-4 scale per control |
| Privacy FW 1.0 | 78 | 0-4 scale per control |
| AI RMF 1.0 | 78 | 0-4 scale per control |
| **Total** | **234** | triple-maturity per control (D11) |

---

## §5 Frontmatter Changes

| Dimension | Legacy | Rich (Case_03) |
|-----------|--------|----------------|
| `document_id` | `AEGIS-P2-08`, `AEGIS-P2-09`, … | Rich orchestration: `AEGIS-P2-RICH-*-CASE03`; Doc 13: `AEGIS-P2-RICH-13-CASE03` |
| `status` | `DRAFT` (legacy) | Rich orchestration: `ACTIVE` / `FINAL`; legacy copies: `DRAFT` (unchanged) |
| `branch` | absent | `feature/aegis-p2-case03-csf-pf-airmf` on every rich doc |
| `sibling_of` | absent | `../02_PHASE2_RULES/` |
| `frameworks_in_scope` | n/a | `[NIST_CSF_2.0, NIST_Privacy_FW_1.1, NIST_AI_RMF_1.0]` (all 3 ACTIVE; DORA via CSF) |
| `frameworks_placeholder` | n/a | `[]` (NO placeholder) |
| `applicable_regulations` | `[GDPR, CRA, NIS_2, DORA, AI_Act]` | unchanged |
| `normative_intensity_rule` | `AVG_with_AI_MUST_override` | unchanged (DORA uniformly NI=3 by source) |
| `maturity_dual_mode` | `triple` | unchanged |
| `ni_avg_rule_note` | absent | present (added by Bloco G fix) |

Current per-document status: Doc 08/09/10/11/12 `DRAFT` (legacy copies, unchanged) · Doc 13 `ACTIVE` · README `ACTIVE` · PROJECT_STATE `ACTIVE` · this file `FINAL` · 10b `ACTIVE` · SPEC `ACTIVE`.

---

## §6 Invariants

| Invariant | Status | Evidence |
|-----------|:------:|----------|
| Legacy `02_PHASE2_RULES/` unmodified | ✅ | All 5 legacy files retain their pre-Bloco mtimes |
| Phase 1 files unmodified | ✅ | `01_PHASE1_CONTEXT/` and `01_PHASE1_CONTEXT_RICH/` read-only throughout |
| Phase 3 files unmodified | ✅ | Not touched in any bloco |
| Corpus unmodified | ✅ | No writes to `00_METHODOLOGY/PREPROCESSING_by_domain/` |
| No Effort/Cost/Timeline | ✅ | Absent from all docs and workbook sheets |
| `AEGIS-P2-RICH-*` IDs | ✅ | All 7 Rich orchestration/extension docs |
| 3 frameworks ACTIVE | ✅ | No AI RMF placeholder column; all 78 cards mapped to 3 frameworks |
| DORA coverage via CSF | ✅ | Crosswalk notes DORA mapped to CSF subcats |
| Legacy inconsistencies reported, not silently fixed | ✅ | 4 findings FN-01..FN-05 addressed; F-01 (legacy Doc 10 goal count) documented |

---

## §7 Bloco Progress

| Bloco | Theme | Status | Verdict |
|-------|-------|:------:|---------|
| A | Crosswalk DRAFT → ACTIVE | ✅ REUSED (from Case_02) | PASS |
| B | NI formal (AVG + AI MUST + DORA MUST) | ✅ COMPLETE | PASS |
| C | Doc 13 unified matrix | ✅ COMPLETE | PASS_WITH_FINDINGS |
| D | Doc 11 fields 19-24 (tri-maturidade) | ✅ COMPLETE | PASS_WITH_FINDINGS |
| E | 04b deprecated for maturity | ✅ COMPLETE | PASS |
| F | 4 visualizações + Excel 10 sheets | ✅ COMPLETE | PASS_WITH_FINDINGS |
| G fix | FN-01..FN-05 closure | ✅ COMPLETE | PASS (all findings addressed) |
| Validator | Tier 1+2 | ✅ COMPLETE | PASS_WITH_FINDINGS |

**8 of 8 complete.** All Tier 1+2 acceptance criteria met; 4 findings raised, all addressed by Bloco G fix; 1 legacy discrepancy (F-01 goal count) documented in §4 of README.

---

## §8 See also

- `README.md` — orientation + status dashboard + §8 final status
- `PROJECT_STATE.md` — project state snapshot (Case_03 specific)
- `13_Framework_Mapping_Matrix.md` — unified matrix over 3 frameworks (the main deliverable)
- `SPEC_NIST_MATRIX_UNIFIED.md` — 17-decision specification
- `10b_Privacy_Security_Goals_NIST_Implications.md` — 76 PG/SG implications
- `12_Rules_Catalog.xlsx` — 10-sheet workbook
- `validation/VALIDATOR_BLOCOG.md` — Validator Tier 1+2 verdict (PASS_WITH_FINDINGS)
- `validation/SPRINT*_REPORT.md` — bloco completion reports
- `../02_PHASE2_RULES/` — legacy Phase 2 (read-only, contains canonical with Bloco D extensions)
- `../../Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md` — Case_01 equivalent
- `../../Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md` — Case_02 equivalent