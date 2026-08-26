---
document_id: AEGIS-P2-RICH-README
title: Phase 1 Rich Mode — Case_02 (SecureBorder Solutions)
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Sprint 0 Executor (README); Sprint 3 Executor (status + navigation)
status: ACTIVE
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 35
inactive_documented: [D-08.3 INACTIVE, 3 NOT_ADDRESSED]
track: B
tier: MEDIUM
---

# Phase 1 Rich Mode — Case_02 (SecureBorder Solutions)

## Purpose

This folder is the **Rich version** of Phase 1 for the SecureBorder Solutions case. It is a **sibling** of `../01_PHASE1_CONTEXT/` (the legacy version) and is **enriched with corpus data** from `00_METHODOLOGY/PREPROCESSING/SubDomains/`, `00_METHODOLOGY/PREPROCESSING/Regulation/`, `00_METHODOLOGY/PREPROCESSING/CrossRegulation/`, and `00_METHODOLOGY/PREPROCESSING/AMBIGUITY_ANALYSIS/`.

**Goal**: deliver a Phase 1 Scope Declaration that is **10× deeper** than the legacy version, with **explicit corpus linkage** (every claim is traceable to a frozen baseline fact) and **3 new Rich-only docs** (ambiguity register, proportionality profile, adjusted objectives, citation index).

## Relationship to legacy

The legacy case (`../01_PHASE1_CONTEXT/`) is **read-only** and **stays frozen**. This Rich folder may cross-reference it but must not modify it. All Phase 1 lints pass against the legacy version (6/6, 30 warnings — all catalogued in `validation/LINT_REPORT_BEFORE.md`).

**Substitution rule**: when the Rich version is complete, the case's Rich variant is the one consumed by Phase 2/3. The legacy variant stays as a research artifact. **As of Sprint 3 this substitution has NOT been made** — the Rich folder holds a CONDITIONAL_PASS with 2 blocking items (see dashboard below) and `07c` is still a placeholder. Phase 2/3 continue to consume the legacy folder.

## Case profile

| Attribute | Value |
|-----------|-------|
| **Company** | SecureBorder Solutions B.V. |
| **Location** | Netherlands (EU) |
| **Size** | 450 employees, €120M revenue |
| **Scale (Track B)** | **MEDIUM** |
| **Sector** | Defense / Security / Critical Infrastructure |
| **Product** | eGate kiosks with Edge AI (GuardianGate) |
| **Data types** | Biometric templates, passport data, judicial watchlist data |
| **Special category data** | YES (biometric, GDPR Art. 9) |
| **AI / ML systems** | YES — High-Risk AI (Annex III: border control) |
| **ISO 27001** | Certified |
| **Applicable regs** | GDPR (CONTROLLER + PROCESSOR), CRA (MANUFACTURER), NIS 2 (ESSENTIAL_ENTITY_SUPPLIER), AI_Act (PROVIDER) |
| **Total clauses** | 112 (GDPR 28 + CRA 26 + NIS 2 29 + AI_Act 29) |
| **Active sub-domains** | 35 / 38 (D-08.3 INACTIVE + 3 NOT_ADDRESSED) |
| **Strategic tensions** | 3 (T-001 Temporal, T-002 Cryptographic, T-003 TRIGGER_MISMATCH) |

## Goals

1. **10× enrichment depth** — every doc length × 3 average, with ~300 cross-doc links to corpus
2. **Self-consistency** — `lint_cross_document_consistency.py` returns 0 warnings
3. **Corpus linkage** — every claim traceable to a corpus file (L1, L2, L3, L4)
4. **Tier proportionality** — Track B MEDIUM = standard depth for most sub-domains, RIGOROUS for top-5 clause-density
5. **Anti-hallucination** — every citation verified by `lint_regulatory_references.py` (currently 453/453 valid in legacy)
6. **Mutual exclusion with legacy** — Rich version is the new source of truth; legacy is frozen

## Sprint status dashboard

| Sprint | Status | Output |
|--------|--------|--------|
| **Sprint 0** | ✅ | Skeleton + lint baseline + `corpus_field_map.md` |
| **Sprint 0.5** | ✅ | Doc 07b Track B (35 sub-domains, 8 RIGOROUS + 27 STANDARD) |
| **Sprint 1** | ✅ | Reconciliation (10 docs + ontology) |
| **Sprint 2** | ✅ | Corpus enrichment (4 docs + 2 NEW + Excel 15 sheets) |
| **Sprint 3** | ✅ | Final docs + Validator review (verdict: CONDITIONAL_PASS) |
| Sprint 4 | ⬜ | Adjusted Objectives — `07c` is still a placeholder |

**Sprint 3 verdict: CONDITIONAL_PASS.** Two blocking items must be adjudicated before this folder supersedes the legacy one:

1. **Scale input (F-01, `07b` §11.3)** — Doc 07b assigns `S = MEDIUM`, but `proportionality_model.md` §2 puts 450 employees / €120M revenue in **LARGE** on both axes. Under `S = LARGE`, all 35 rows would be RIGOROUS rather than 8 RIGOROUS + 27 STANDARD.
2. **Active sub-domain set (V-02, `validation/VALIDATOR_SPRINT3.md`)** — `05b` and `07b` disagree on *which* 3 sub-domains are excluded, though both total 35.

See `validation/VALIDATOR_SPRINT3.md` for the full verdict and `validation/SPRINT3_REPORT.md` for the change list.

### Original sprint plan (Sprint 0 intent, retained for reference)

The Sprint 0 plan below was superseded during execution — themes were resequenced (ambiguity work landed in Sprint 2, not Sprint 3) and Sprints 4–5 were not run.

| Sprint | Planned theme |
|--------|---------------|
| 0 | Planning + Skeleton |
| 0.5 | Corpus Linkage |
| 1 | Reconciliation |
| 2 | Deep enrichment |
| 3 | Ambiguity resolution |
| 4 | Quality gate |
| 5 | Final polish |

## Navigation

### Phase 1 documents (16 `.md`)

| # | Doc | New in Rich? | Status | Lines |
|---|-----|--------------|--------|------:|
| 00 | [`00_Taxonomy_Reference.md`](Doc01_Taxonomy_Reference.md) | no (was in `00_COMMON/`) | RECONCILED | 256 |
| 01 | [`01_INTAKE_FORM.md`](Doc02_INTAKE_FORM.md) | no (renamed from `01_Company_Context.md`) | RECONCILED | 611 |
| 04 | [`04_Company_Context_Assessment.md`](Doc03_Company_Context_Assessment.md) | no | RECONCILED | 337 |
| 04a | [`04a_Architecture_DataInventory.md`](Doc04_Architecture_DataInventory.md) | no | ENRICHED (Sprint 2) | 316 |
| 04b | [`04b_Security_Posture.md`](Doc05_Security_Posture.md) | no | ENRICHED (Sprint 2) | 379 |
| 04c | [`04c_ThirdParty_Landscape.md`](Doc06_ThirdParty_Landscape.md) | no | ENRICHED (Sprint 2) | 303 |
| 04d | [`04d_Org_Roles_RACI.md`](Doc07_Org_Roles_RACI.md) | no | ENRICHED (Sprint 2) | 414 |
| 05 | [`05_Regulatory_Applicability.md`](Doc08_Regulatory_Applicability.md) | no | RECONCILED | 443 |
| **05b** | [`05b_Ambiguity_Register.md`](Doc09_Ambiguity_Register.md) | **YES** | COMPLETE (Sprint 2) | 632 |
| 06 | [`06_Clause_Mapping_Matrix.md`](Doc10_Clause_Mapping_Matrix.md) | no | RECONCILED | 301 |
| 07 | [`07_Structured_Compliance_Matrix.md`](Doc12_Structured_Compliance_Matrix.md) | no | RECONCILED | 444 |
| **07b** | [`07b_Proportionality_Profile.md`](Doc13_Proportionality_Profile.md) | **YES** | ACTIVE + cross-checked (Sprint 3) | 308 |
| **07c** | [`07c_Adjusted_Objectives.md`](Doc13_Adjusted_Objectives.md) | **YES** | ⚠️ **PLACEHOLDER** — Sprint 4 | 53 |
| **—** | [`Citation_Index.md`](Citation_Index.md) | **YES** | COMPLETE (Sprint 2) | 127 |
| — | [`corpus_field_map.md`](Corpus_Field_Map.md) | yes | DRAFT (Sprint 0) | 211 |
| — | `README.md` | this file | ACTIVE | — |

### Supporting artefacts

| Path | Purpose | Lines / size |
|------|---------|-------------:|
| [`phase1_ontology.yaml`](phase1_ontology.yaml) | Rich ground-truth ontology v1.1 (adds T-006/007/008) | 1766 |
| [`Case_02_Phase1_RICH.xlsx`](Case_02_Phase1_RICH.xlsx) | Excel companion — 15 sheets | 15 sheets |
| [`RICH_VS_LEGACY.md`](RICH_VS_LEGACY.md) | Rich ↔ legacy diff summary (Sprint 3) | — |
| [`PROJECT_STATE.md`](PROJECT_STATE.md) | Localised Phase 1 Rich project state (Sprint 3) | — |
| `scripts/generate_corpus_links.py` | Corpus link generator | 36 (stub) |
| `scripts/filter_ambiguity_cards.py` | Ambiguity-card filter | 40 (stub) |
| `scripts/regenerate_ontology.py` | Ontology regeneration | 43 (stub) |

### Validation reports

| Path | Contents |
|------|----------|
| [`validation/LINT_REPORT_BEFORE.md`](validation/LINT_REPORT_BEFORE.md) | Sprint 0 baseline — legacy folder, 6/6 PASS, 30 warnings |
| [`validation/SPRINT1_REPORT.md`](validation/SPRINT1_REPORT.md) | Sprint 1 reconciliation report |
| [`validation/LINT_REPORT_AFTER_RECONCILE.md`](validation/LINT_REPORT_AFTER_RECONCILE.md) | Sprint 1 lint report (**synthetic mirror** — see caveat below) |
| [`validation/SPRINT2_ENRICHMENT_REPORT_EXISTING.md`](validation/SPRINT2_ENRICHMENT_REPORT_EXISTING.md) | Sprint 2 — 4 enriched docs |
| [`validation/SPRINT2_ENRICHMENT_REPORT_NEW.md`](validation/SPRINT2_ENRICHMENT_REPORT_NEW.md) | Sprint 2 — 2 new docs |
| [`validation/VALIDATOR_SPRINT3.md`](validation/VALIDATOR_SPRINT3.md) | Sprint 3 independent verdict |
| [`validation/SPRINT3_REPORT.md`](validation/SPRINT3_REPORT.md) | Sprint 3 summary |

### Excel sheet index (`Case_02_Phase1_RICH.xlsx`)

`CORPUS_SUMMARY` · `COVER` · `SYSTEMS` · `DATA_STORES` · `DATA_FLOWS` · `PERSONAL_DATA` · `THIRD_PARTIES` · `ROLES_RACI` · `MATURITY` · `SUBDOMAINS` · `REG_CHAIN` · `COMPLIANCE` · `GAPS` · `PRIORITIES` · `Corpus Cross-Reference`

## Lint status

Reproducible command and result as of Sprint 3:

```bash
python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_02_SecureBorder_Solutions"
# 6/6 passed, 0 errors, 33 warnings
```

⚠️ **Warning-count caveat.** `run_phase1_lints.py` is **case-scoped, not folder-scoped** — it scans the whole case (53 documents: legacy + Rich + `00_COMMON/`), so it cannot report a Rich-only figure. The "6 warnings" in `LINT_REPORT_AFTER_RECONCILE.md` was produced against a **synthetic mirror** at `/tmp/opencode/case02_rich_lint_target/`, where Rich content was copied into a stand-in `01_PHASE1_CONTEXT/` and legacy files such as `02_Regulatory_Mapping_Master.md` were absent. Several of the warnings counted as "fixed" disappeared because a file was **not copied**, not because a defect was repaired — notably, the T-006/007/008 ontology warnings persist in the real repo because the lints load the ontology from `00_COMMON/phase1_ontology.yaml`, not from the Rich copy. Treat 33 as the authoritative number and −80% as **not reproducible**.

## Validation strategy

The Rich version is validated by the same 6 Phase 1 lints as the legacy case, plus an additional cross-doc consistency check at the end of each sprint.

### 6 Phase 1 lints (apply to legacy; future sprints apply to Rich)

| Lint | Purpose | Used in Sprint |
|------|---------|----------------|
| `lint_company_context.py` | Validates 38-question / layered intake format | 0, 2, 4 |
| `lint_regulatory_mapping.py` | Validates per-regulation ↔ clause mapping | 0, 2, 4 |
| `lint_regulatory_references.py` | Anti-hallucination (453 refs in legacy) | 0, 2, 4 |
| `lint_regulatory_ground_truth.py` | Validates against frozen baseline (ontology, obligated_party) | 0, 1, 4 |
| `lint_cross_document_consistency.py` | Cross-doc regulation name + count consistency | 0, 2, 4 |
| `lint_template_compliance.py` | Structural coverage of templates | 0, 2, 4 |

### Validator subagent

A Validator sub-agent will run at the end of Sprint 1, 2, 3, 4 to provide an independent review of:
- Frontmatter validity
- Cross-reference completeness
- Lint pass status
- Corpus traceability

### Track B specifics

- **Tier MEDIUM** ≤ 50-250 employees / €10M-€50M revenue. SecureBorder is at the upper edge (450 emp, €120M); we classify MEDIUM because (a) 4 applicable regs is HIGH territory, but (b) the architecture is well-bounded (Hybrid Edge + Cloud), and (c) only 3 strategic tensions (vs 8 in the Phase 2 case).
  - ⚠️ **DISPUTED (Sprint 3, finding F-01).** This rationale does not survive cross-check against `proportionality_model.md` §2, which defines `MEDIUM = ≤250 employees, <€50M` and `LARGE = >250 employees, ≥€50M`. At 450 employees and €120M, SecureBorder exceeds **both** MEDIUM ceilings (1.8× employees, 2.4× revenue) and is not "at the upper edge" of MEDIUM — it is squarely LARGE. Doc 04 §2 itself records size as "Medium-Large". Criteria (a)–(c) above are not inputs to the §2 table. Under `S = LARGE`, §5.1 yields RIGOROUS for all 35 rows. **Pending orchestrator adjudication** — see `07b_Proportionality_Profile.md` §11.3 F-01.
- **Most sub-domains → STANDARD depth** — one paragraph per sub-domain, one row per clause.
- **Critical sub-domains → RIGOROUS depth** — full per-pair analysis, all ambiguous clauses quoted. Top 5 by clause density: D-09.1, D-06.3, D-09.2, D-09.4, D-06.4.
- **Inactive sub-domains (D-08.3 + 3 NOT_ADDRESSED) → NOTE-ONLY** — a single line acknowledging non-applicability.

## Cross-references — how this folder uses `00_METHODOLOGY/PREPROCESSING/`

| Layer | Path | Used by |
|-------|------|---------|
| **L1 (SubDomains)** | `00_METHODOLOGY/PREPROCESSING/SubDomains/D-<XX>_<Name>/D-<XX>.<Y>.md` | Doc 04..07, 05b, 07b, 07c, Citation_Index |
| **L2 (Regulation)** | `00_METHODOLOGY/PREPROCESSING/Regulation/<REG>/02_SecurityRules_NIST.md` | Doc 05, 06, 07, Citation_Index |
| **L2 (Articles)** | `00_METHODOLOGY/PREPROCESSING/Regulation/<REG>/Articles/Art_N.md` | Doc 06, Citation_Index |
| **L2 (Ambiguity)** | `00_METHODOLOGY/PREPROCESSING/Regulation/<REG>/Ambiguity/clause_cards.md` | Doc 05b |
| **L3 (DomainAnalysis)** | `00_METHODOLOGY/PREPROCESSING/CrossRegulation/DomainAnalysis/D-<XX>_<Name>/D-<XX>.<Y>.md` | Doc 04a, 07b |
| **L3 (DeepAnalysis)** | `00_METHODOLOGY/PREPROCESSING/CrossRegulation/DeepAnalysis/D-<XX>_<Name>/D-<XX>.<Y>.md` | Doc 05b, 07c |
| **L4 (HSO)** | `00_METHODOLOGY/PREPROCESSING/00_Hierarchical_SecurityObjectives.md` | Doc 01, 05, 07b, 07c |
| **L4 (CSF)** | `00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md` | Doc 06, 07 |
| **L4 (Ambiguity)** | `00_METHODOLOGY/PREPROCESSING/AMBIGUITY_ANALYSIS/01_Framework.md` | Doc 05b |

## Tooling

- **Extractor**: `/tmp/extract_case02_corpus.py` — produces `/tmp/case02_corpus.json` with per-sub-domain data.
- **Stub scripts** (in `scripts/`):
  - `generate_corpus_links.py` — Sprint 0.5: auto-generate per-doc links to L1/L2/L3/L4.
  - `filter_ambiguity_cards.py` — Sprint 0.5: filter L2 Ambiguity/ cards to Case_02-applicable regs.
  - `regenerate_ontology.py` — Sprint 1: re-generate the ground-truth ontology after warning reconciliation.

## See also

- `validation/LINT_REPORT_BEFORE.md` — Sprint 0 lint baseline (6/6 PASS, 30 warnings)
- `corpus_field_map.md` — exact corpus field → case field mapping
- `../PROJECT_STATE.md` — case profile (defensive: contains 8 strategic tensions, of which 3 are Phase 1 tensions T-001/002/003)
- `../01_PHASE1_CONTEXT/` — legacy version (read-only)
- `00_METHODOLOGY/PHASE1_STRATEGY.md` — Phase 1 strategy (Track B MEDIUM tier definition in §8)
- `00_METHODOLOGY/REGULATORY_BASELINE.md` — frozen corpus contract
