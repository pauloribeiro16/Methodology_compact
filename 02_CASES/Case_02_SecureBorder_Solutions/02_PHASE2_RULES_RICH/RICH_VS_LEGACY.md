---
document_id: AEGIS-P2-RICH-DIFF-CASE02
title: Rich vs Legacy — Diff Summary (Phase 2, Case_02)
phase: 2
version: 1.0
created: 2026-08-08
updated: 2026-08-08
author: Rich-Symmetry Executor
status: FINAL
case: Case_02_SecureBorder_Solutions
tier: HIGH
sibling_of: ../02_PHASE2_RULES/
branch: feature/aegis-p2-case02-csf-pf-airmf
---

# Rich vs Legacy — Diff Summary (Phase 2, Case_02)

> Side-by-side comparison of Phase 2 Rich (`02_PHASE2_RULES_RICH/`) vs legacy Phase 2 (`02_PHASE2_RULES/`, as-shipped) for **Case_02 (SecureBorder Solutions)**.
> Mirrors `../Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md` (Case_01).
>
> **State at time of writing:** All 7 blocos (A→G) merged into `main` on `feature/aegis-p2-case02-csf-pf-airmf`. Validator Tier 1+2 PASS_WITH_FINDINGS (7 findings closed).

---

## §1 Comparison Summary

| Metric | Legacy `02_PHASE2_RULES/` | Rich `02_PHASE2_RULES_RICH/` | Δ |
|--------|--------------------------:|-----------------------------:|---|
| Phase 2 `.md` documents | 5 | 5 (legacy copies) + 7 orchestration/rich | +7 net |
| Phase 2 doc lines | 2,390 | 2,390 (verbatim copies) | 0 |
| Orchestration docs | 0 | 7 (README, PROJECT_STATE, RICH_VS_LEGACY, SPEC, 10b, Doc 13) | +7 |
| Validation reports | 1 (none) | 9 (8 new + 1 existing VALIDATOR_BLOCOG) | +8 |
| Doc 13 unified matrix | (absent) | **ACTIVE** (3 frameworks) | NEW |
| Excel sheets | n/a | 10 (legacy + 6 new from Bloco F) | +6 |
| Triple-maturity cells | n/a | 165 (3 × 55 cards) | NEW |
| Compliance Rules (CR) | 38 unique | 38 unique | 0 |
| Best Practice Rules (BPR) | 17 unique | 17 unique | 0 |
| Obligations (Doc 08) | 38 | 38 | 0 |
| Privacy Goals (PG) | 10 | 10 | 0 |
| Security Goals (SG) | 37 | 37 | 0 |
| Tensions | 6 | 6 | 0 |
| Frameworks in scope | n/a | **3 (CSF + PF + AI RMF)** | NEW (Case_02 has no placeholder) |
| AI RMF placeholder | n/a | **NOT PLACEHOLDER — ACTIVE** | distinguishes Case_02 from Case_01 |
| DR-002 resolution | AVG + AI MUST override | AVG + AI MUST override | unchanged |
| Track B distribution | 7 RIGOROUS + 27 STANDARD + 1 DEFERRED + 3 LIGHTWEIGHT | same | unchanged |
| Active sub-domains | 35/38 (3 DEFERRED) | 35/38 | unchanged |
| Source clauses | GDPR (28) + CRA (26) + NIS 2 (29) + AI_Act (29) = 112 | 112 | 0 |
| Data-integrity findings | 0 recorded | **7** (FN-01..FN-07, all closed by Bloco G fix) | +7 |
| Effort/Cost/Timeline fields | absent | absent (by directive) | 0 |

**Headline:** Unlike Case_01 (which has only CSF + Privacy FW with AI RMF as placeholder), Case_02 has **all 3 frameworks ACTIVE** — Doc 13 columns for CSF, Privacy FW, and AI RMF are fully populated. The AI RMF placeholder convention from Case_01 does NOT apply.

---

## §2 Per-Document Diff

| Doc | Legacy lines | Rich lines | Δ | Diff summary |
|-----|-------------:|-----------:|--:|--------------|
| `08_Obligation_Derivation.md` | 754 | 754 | 0 | **Verbatim copy** of legacy; canonical lives in `../02_PHASE2_RULES/`. Rich copy preserves reference. |
| `09_Strategic_Tensions_Report.md` | 640 | 640 | 0 | **Verbatim copy** of legacy. |
| `10_Privacy_Security_Goals.md` | 394 | 394 | 0 | **Verbatim copy** of legacy. |
| `11_Rules_Catalog.md` | 602 | 602+ | +banner | **Verbatim copy** + Rich banner pointing to canonical. Block D extensions (fields 19-24, tri-maturidade) live in the canonical `../02_PHASE2_RULES/11_Rules_Catalog.md`. |
| `12_Rules_Catalog.xlsx` | 28KB | 28KB | 0 | **Verbatim copy** of legacy binary. |
| `13_Framework_Mapping_Matrix.md` | — | ~2,400 | NEW | Unified matrix over 3 frameworks (CSF + PF + AI RMF), 6 sub-sections, 55 card mappings, 165 triple-maturity cells. Bloco C + D + F outputs. |
| `10b_Privacy_Security_Goals_NIST_Implications.md` | — | ~400 | NEW | 47 PG/SG × 3 frameworks (CSF + PF + AI RMF) implication catalog. |
| `SPEC_NIST_MATRIX_UNIFIED.md` | — | ~1,000 | NEW | 17-decision specification (adapted from Case_01 SPEC for Case_02 3-framework scenario). |
| `README.md` | — | this repo | NEW | Orientation, dashboard, schema, domain profile, bloco plan. |
| `PROJECT_STATE.md` | — | ~200 | NEW | Project state snapshot (Case_02 specific). |
| `RICH_VS_LEGACY.md` | — | this file | NEW | Case_02-specific Rich vs legacy diff summary. |
| `validation/*.md` | — | ~2,800 | NEW | 9 reports: LINT_BEFORE + SPRINT0-5_Case02 + VALIDATOR_BLOCOG + VALIDATOR_SPRINT5. |

> **Why Doc 08/09/10/11 are byte-identical copies.** The Case_02 contract applied Bloco D field extensions to the canonical `../02_PHASE2_RULES/11_Rules_Catalog.md` (18 fields per card). The Rich copy preserves the legacy 17-field schema for reference; consult `../02_PHASE2_RULES/11_Rules_Catalog.md` for the live operational document.

---

## §3 Field Additions

Legacy rules carry **17 fields**; the Rich 18-field schema adds triple-maturity dimensions.

| Legacy rule field (17) | Present in Rich | Notes |
|------------------------|:---------------:|-------|
| Rule ID | ✅ | Sheet 2 |
| Rule Description | ✅ | field 2 |
| Source | ✅ | field 5 (Source Article) |
| Sub-Domain | ✅ | field 1 |
| Normative Intensity | ✅ | Sheet 6, re-derived under AVG+AI MUST |
| Priority | ✅ | field 15 |
| Verification | ✅ | field 10 |
| Implementation | ✅ | Sheet 7 (NATIVE/INHERITED) |
| Related Goals | ✅ | field 13 (Dependencies) |
| implementation_tier | ✅ | Sheet 4 |
| proportional_priority | ✅ | Sheet 2 |

| New in the Rich 18-field schema (Bloco B + D) | Source |
|----------------------------------------------|--------|
| 7. Privacy FW Anchors | corpus L2 manifests |
| 8. AI RMF Anchors | corpus L2 manifests |
| 16. Maturity (CSF) | Doc 13 §4-5 |
| 17. Maturity (Privacy) | Doc 13 §4-5 |
| 18. Maturity (AI RMF) | Doc 13 §4-5 |

**Net:** 17 base fields → **18 schema fields** for Case_02 (1 extra field for AI RMF maturity vs Case_01's 17 fields × 107 cards). The triple-maturity model is the defining difference vs Case_01.

**Deliberately excluded:** Effort, Cost, Timeline — absent from every Rich document and all workbook sheets, per the Phase 2 Rich directive.

---

## §4 New Content

### Doc 13 unified matrix (delivered, Bloco C + D + F)

| # | Sub-section | Content |
|--:|-------------|---------|
| 1 | Matriz Unificada | 55 rows (38 CR + 17 BPR) × columns CSF, Privacy FW, AI RMF, ISO 27001, SSDF |
| 2 | Govern Consolidada | 6 conceitos × 3 frameworks |
| 3 | Mapeamento n:m | 55 YAML blocks with rule_id, NI, csf_subcats, priv_subcats, ai_rmf_subcats |
| 4 | Modelo Maturidade | Tiers 1-4 + 0-4 por-subcat (CSF + PF + AI RMF) |
| 5 | Aplicação Case_02 | Per-rule maturity assessment |
| 6 | Gap Analysis | Subcats não cobertas por framework |
| 7 | Visualizações | V1 matriz, V2 mapa por Function, V3 Mermaid, V4 heatmap |
| 8 | Bloco G findings | FN-01..FN-07 reconciliation |

Plus 6 new Excel sheets added (Unified_Matrix, Govern_Consolidated, Mapping_nm, Maturity_Dual, Cov_Function, Heatmap_Maturity).

### 10b PG/SG implications (delivered, Bloco B)

| Goal type | Count | Frameworks |
|-----------|------:|------------|
| Privacy Goals (PG) | 10 | CSF + Privacy FW (primary) + AI RMF where applicable |
| Security Goals (SG) | 37 | CSF (primary) + AI RMF for AI-security-relevant |
| **Total** | **47** | 3 frameworks × 47 = 141 implication rows |

### Triple-maturity cells

| Framework | Cells | Notes |
|-----------|------:|-------|
| CSF 2.0 | 55 | 0-4 scale per control |
| Privacy FW 1.0 | 55 | 0-4 scale per control |
| AI RMF 1.0 | 55 | 0-4 scale per control |
| **Total** | **165** | triple-maturity per control (D11) |

---

## §5 Frontmatter Changes

| Dimension | Legacy | Rich (Case_02) |
|-----------|--------|----------------|
| `document_id` | `AEGIS-P2-08`, `AEGIS-P2-09`, … | Rich orchestration: `AEGIS-P2-RICH-*-CASE02`; Doc 13: `AEGIS-P2-RICH-13-CASE02` |
| `status` | `DRAFT` (legacy) | Rich orchestration: `ACTIVE` / `FINAL`; legacy copies: `DRAFT` (unchanged) |
| `branch` | absent | `feature/aegis-p2-case02-csf-pf-airmf` on every rich doc |
| `sibling_of` | absent | `../02_PHASE2_RULES/` |
| `frameworks_in_scope` | n/a | `[NIST_CSF_2.0, NIST_Privacy_FW_1.1, NIST_AI_RMF_1.0]` (all 3 ACTIVE) |
| `frameworks_placeholder` | n/a | `[]` (NO placeholder — distinct from Case_01) |
| `normative_intensity_rule` | `AVG_with_AI_MUST_override` | unchanged |
| `maturity_dual_mode` | `triple` (CSF + Privacy + AI RMF) | unchanged |

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
| 3 frameworks ACTIVE | ✅ | No AI RMF placeholder column; all 55 cards mapped to 3 frameworks |
| Legacy inconsistencies reported, not silently fixed | ✅ | 7 findings FN-01..FN-07 recorded, all closed by Bloco G fix |

---

## §7 Bloco Progress

| Bloco | Theme | Status | Verdict |
|-------|-------|:------:|---------|
| A | Crosswalk DRAFT → ACTIVE | ✅ COMPLETE | PASS |
| B | NI formal (AVG + AI MUST) | ✅ COMPLETE | PASS |
| C | Doc 13 unified matrix | ✅ COMPLETE | PASS_WITH_FINDINGS |
| D | Doc 11 fields 19-24 (tri-maturidade) | ✅ COMPLETE | PASS_WITH_FINDINGS |
| E | 04b deprecated for maturity | ✅ COMPLETE | PASS |
| F | 4 visualizações + Excel 10 sheets | ✅ COMPLETE | PASS_WITH_FINDINGS |
| G fix | FN-01..FN-07 closure | ✅ COMPLETE | PASS (all findings closed) |
| Validator | Tier 1+2 | ✅ COMPLETE | PASS_WITH_FINDINGS |

**8 of 8 complete.** All Tier 1+2 acceptance criteria met; 7 findings raised, all closed by Bloco G fix.

---

## §8 See also

- `README.md` — orientation + status dashboard + §8 final status
- `PROJECT_STATE.md` — project state snapshot (Case_02 specific)
- `13_Framework_Mapping_Matrix.md` — unified matrix over 3 frameworks (the main deliverable)
- `SPEC_NIST_MATRIX_UNIFIED.md` — 17-decision specification
- `10b_Privacy_Security_Goals_NIST_Implications.md` — 47 PG/SG implications
- `12_Rules_Catalog.xlsx` — 10-sheet workbook
- `validation/VALIDATOR_BLOCOG.md` — Validator Tier 1+2 verdict (PASS_WITH_FINDINGS, 7 findings closed)
- `validation/SPRINT*_REPORT.md` — bloco completion reports
- `../02_PHASE2_RULES/` — legacy Phase 2 (read-only, contains canonical with Bloco D extensions)
- `../../Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md` — Case_01 equivalent