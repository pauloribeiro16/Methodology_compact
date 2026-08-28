---
document_id: AEGIS-P3-RICH-README
title: Phase 1 Rich Mode — Case_03 (OmniBank Financial Systems)
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Sprint 0 Executor (README) + Sprint 3 update
status: ACTIVE
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
inactive_documented: []
track: B
tier: MAX
scale: MAX
sibling_of: ../01_PHASE1_CONTEXT_RICH/
corpus_source: ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/
---

# Phase 1 Rich Mode — Case_03 (OmniBank Financial Systems)

## 1. Purpose

This folder is the **Rich version** of Phase 1 for **OmniBank Financial Systems S.A.** — the MAX-complexity case in the AEGIS methodology (5/5 regulations applicable, 38/38 sub-domains active, ECB-supervised bank with AI Act high-risk credit scoring).

It is **enriched with corpus data** from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` — a **fully populated** corpus with 10 domain manifests + 38 sub-domain manifests + 38 JSON sidecars + 38 merged Markdown + 623 verbatim regulatory article files.

**Goal:** deliver a Phase 1 Scope Declaration that is **10× deeper** than the legacy `01_PHASE1_CONTEXT/`, with **explicit corpus linkage** for every claim and 4 new Rich-only docs (ambiguity register, proportionality profile, adjusted objectives, citation index).

## 2. Relationship to legacy

The legacy case (`../01_PHASE1_CONTEXT_RICH/`) is **read-only** and **stays frozen**. This Rich folder may cross-reference it but must not modify it. The legacy case is **Phase 1 + Phase 2 COMPLETE** (38 obligations derived, 4 strategic tensions resolved).

| Aspect | Legacy `01_PHASE1_CONTEXT/` | Rich `01_PHASE1_CONTEXT_RICH/` |
|--------|----------------------------|--------------------------------|
| Status | Frozen (Phase 1+2 complete 2026-04-03) | Sprint 0 (planning + skeleton) 2026-08-06 |
| Doc 06 format | `.ods` + `.xlsx` only (no `.md`) | Will add `.md` companion (Sprint 1) |
| Total clauses | 150 (28+26+29+38+29) | Same 150 + corpus IDs cross-referenced |
| Strategic tensions | 4 (T-001..T-004) resolved in Phase 2 | Same 4 + potentially more from corpus (Sprint 2) |
| Sub-domains | 38/38 (MAX) | Same 38/38 (MAX) |
| Sprint plan | n/a | 8 sprints (0, 0.5, 0.6, 1, 2, 3, 4, 5) |

**Substitution rule:** When the Rich version is complete (Sprint 5), the case's Rich variant is the one consumed by future Phase 2/3 work. The legacy variant stays as a research artifact.

## 3. Case profile (MAX tier)

| Attribute | Value |
|-----------|-------|
| **Company** | OmniBank Financial Systems S.A. |
| **Location** | Frankfurt, Germany (EU); ECB-supervised |
| **Size** | Large (5,000+ employees, >€1.5B revenue) |
| **Scale (Track B)** | **MAX** |
| **Sector** | Banking / Financial Services (Consumer Credit + Risk Management) |
| **Product** | Mobile banking app + web platform; **OmniScore AI** (High-Risk credit scoring per AI Act Annex III) |
| **Data types** | Customer PII, financial transactions, credit scores, behavioural data |
| **Special category data** | NO (financial data, not GDPR Art. 9) |
| **AI/ML systems** | YES — OmniScore AI Platform |
| **ISO 27001** | Certified (mature baseline) |
| **Applicable regs** | **GDPR** (CONTROLLER, 28 clauses) + **CRA** (MANUFACTURER Standard, 26) + **NIS 2** (ESSENTIAL_ENTITY, 29) + **DORA** (FINANCIAL_ENTITY, 38) + **AI Act** (PROVIDER HIGH-RISK, 29) |
| **Total clauses** | **150** |
| **Sub-domains covered** | **38/38 (100%)** — ALL active, including D-07.4, D-08.3, D-09.3 (which are NOT_ADDRESSED in smaller cases) |
| **Strategic tensions** | 4 declared (T-001..T-004) + potentially more from corpus |

### Per-regulation clause distribution

| Regulation | Clauses | Sub-domains Covered | % of 38 |
|------------|--------:|--------------------:|--------:|
| **GDPR** | 28 | 30 | 78.9% |
| **CRA** | 26 | 36 | 94.7% |
| **NIS 2** | 29 | 27 | 71.1% |
| **DORA** | 38 | 30 | 78.9% |
| **AI Act** | 29 | 15 | 39.5% |
| **TOTAL** | **150** | **38** (union) | **100%** |

### 4 declared strategic tensions (resolved in legacy Phase 2)

| Tension ID | Type | Severity | Sub-Domain(s) | Resolution | Status |
|------------|------|----------|---------------|------------|--------|
| T-001 | TEMPORAL_CONFLICT | CRITICAL | D-04.3 | Max-SLA Routing (24h universal workflow) | ✅ RESOLVED |
| T-002 | REQUIREMENT_CONFLICT | CRITICAL | D-05.3 vs D-10.2 | Cryptographic Sharding | ✅ RESOLVED |
| T-003 | FREQUENCY_MISMATCH | MEDIUM | D-09.2 | IPSARA Unified Assessment Framework | ✅ RESOLVED |
| T-004 | INTENSITY_GAP | LOW | D-07.1 | Follow CRA secure-by-default standard | ✅ RESOLVED |

**Sprint 2 prediction:** 1-3 additional tensions may be surfaced from corpus `emergent_tensions` (likely from D-09.1 DORA Art. 5-16 overlap and D-09.2 DPIA+FRIA+ICT risk triple overlap).

## 4. Goals

1. **10× enrichment depth** — every doc length × 3-10 average, with ~250 cross-doc links to corpus (estimated)
2. **Self-consistency** — `lint_cross_document_consistency.py` returns 0 errors (currently 1 FAIL)
3. **Corpus linkage** — every claim traceable to a corpus file (L1/L2/L3/L5)
4. **MAX tier proportionality** — most sub-domains get RIGOROUS depth (top 10 by clause density)
5. **Anti-hallucination** — every citation verified by `lint_regulatory_references.py` (currently 729/729 valid in legacy)
6. **DORA + AI Act dual driver** — DORA ICT Risk Framework + AI Act OmniScore high-risk are the two distinctive regulatory pressures

## 5. Sprint plan

| Sprint | Theme | Deliverables |
|--------|-------|--------------|
| **0** | Planning + Skeleton | This README, 14 placeholder docs, 3 script stubs, lint baseline, corpus field map |
| **0.5** | Corpus Linkage | Each placeholder filled with at least 1 cross-link to L1/L2/L3/L5 |
| **0.6** | **DORA ICT Risk Framework dedicated** | Map DORA Art. 5-16 to D-09.1; update Doc 04d + Doc 07b + Doc 07c |
| **1** | Reconciliation | Generate Doc 06 `.md` companion (lint blocker I-C03-01); register T-001..T-004 in ontology; fix 5 obligated_party values; fill 1 missing Doc 04 section |
| **2** | Deep enrichment | Full content per doc, 4 new Rich-only docs complete (05b, 07b, 07c, Citation_Index), xlsx companion generated |
| **3** | Ambiguity resolution | 05b_Ambiguity_Register filled (top 20 by cards); corpus-emergent tensions cross-linked; 4 declared tensions verified |
| **4** | Quality gate | All 6 lints pass against Rich folder; cross-doc consistency check |
| **5** | Final polish | Cross-case consistency (compare with Case_01 + Case_02 Rich if exists) |

**Sprint 0.6 special note:** DORA ICT Risk Framework (Art. 5-16) gets a dedicated sprint because DORA is a defining characteristic of Case_03 (38 DORA clauses, 30/38 sub-domains, 1 of 5 declared tensions T-003 IPSARA). Without Sprint 0.6, Doc 04d (RACI), Doc 07b (Proportionality), and Doc 07c (Adjusted Objectives) will not adequately capture DORA's role.

## 6. File inventory (14 placeholder docs + orchestration files)

### 6.1 Phase 1 Documents (14 placeholders)

| # | Doc | New in Rich? | Status (Sprint 0) | Lines (target) | Doc ID prefix |
|---|-----|--------------|-------------------|----------------|---------------|
| 00 | `00_Taxonomy_Reference.md` | no (was in `00_COMMON/`) | placeholder | 50-60 | AEGIS-P3-RICH-00-TAX |
| 01 | `Doc02_INTAKE_FORM.md` | no | placeholder | 50-60 | AEGIS-P3-RICH-01-INTAKE |
| 04 | `Doc03_Company_Context_Assessment.md` | no | placeholder | 50-60 | AEGIS-P3-RICH-04-CCA |
| 04a | `Doc04_Architecture_DataInventory.md` | no | placeholder | 50-60 | AEGIS-P3-RICH-04a-ARCH |
| 04b | `Doc05_Security_Posture.md` | no | placeholder | 50-60 | AEGIS-P3-RICH-04b-SEC |
| 04c | `Doc06_ThirdParty_Landscape.md` | no | placeholder | 50-60 | AEGIS-P3-RICH-04c-3P |
| 04d | `Doc07_Org_Roles_RACI.md` | no | placeholder | 50-60 | AEGIS-P3-RICH-04d-RACI |
| 05 | `Doc08_Regulatory_Applicability.md` | no | placeholder | 50-60 | AEGIS-P3-RICH-05-APP |
| **05b** | `Doc09_Ambiguity_Register.md` | **YES** | placeholder | 50-60 | AEGIS-P3-RICH-05b-AMBIG |
| 06 | `Doc10_Clause_Mapping_Matrix.md` | no (CRITICAL: only .ods/.xlsx exist) | placeholder | 50-60 | AEGIS-P3-RICH-06-MAP |
| 07 | `Doc12_Structured_Compliance_Matrix.md` | no | placeholder | 50-60 | AEGIS-P3-RICH-07-MATRIX |
| **07b** | `Doc13_Proportionality_Profile.md` | **YES** | placeholder | 50-60 | AEGIS-P3-RICH-07b-PROP |
| **07c** | `Doc14_Adjusted_Goals.md` | **YES** | placeholder | 50-60 | AEGIS-P3-RICH-07c-ADJ |
| **Citation** | `Citation_Index.md` | **YES** | placeholder | 50-60 | AEGIS-P3-RICH-CITATION |

### 6.2 Orchestration files

| File | Purpose | Lines (target) |
|------|---------|----------------|
| `README.md` | this file | 200+ |
| `corpus_field_map.md` | case-03 specific corpus field mapping | 500+ |
| `validation/LINT_REPORT_BEFORE.md` | Sprint 0 lint baseline | 200+ |

### 6.3 Script stubs (3)

| File | Purpose | Sprint |
|------|---------|--------|
| `scripts/generate_corpus_links.py` | Auto-generate per-doc links to L1/L2/L3/L5 | Sprint 0.5 |
| `scripts/filter_ambiguity_cards.py` | Filter L3 ambiguity cards to Case_03-applicable regs | Sprint 0.5 |
| `scripts/regenerate_ontology.py` | Regenerate ontology (resolve T-001..T-004) | Sprint 1 |

### 6.4 Generated artefact (Sprint 1+)

| File | Purpose |
|------|---------|
| `Case_03_Phase1_RICH.xlsx` | 14-sheet Excel workbook (parallel to legacy `Case_03_Phase1.xlsx`) |

## 7. Validation strategy

The Rich version is validated by the same 6 Phase 1 lints as the legacy case, plus additional cross-doc consistency + corpus coverage checks.

### 7.1 Sprint 0 baseline (this sprint)

| Lint | Status | Detail |
|------|--------|--------|
| `run_phase1_lints.py` (orchestrator) | PARTIAL FAIL | 5/6 pass, 1 FAIL (cross-doc consistency), 29 warnings |
| `lint_company_context.py` | PASS | 1 warn (12/13 sections) |
| `lint_regulatory_mapping.py` | PASS | 1 warn (only 1 domain in 02_Regulatory_Mapping_Master.md) |
| `lint_regulatory_references.py` (Anti-Hallucination) | PASS | 0 warns (729/729 references valid) |
| `lint_regulatory_ground_truth.py` | PASS | 10 warns (T-001..T-004 ontology + 5 obligated_party values) |
| `lint_cross_document_consistency.py` | **FAIL** | **Doc 06 missing `.md`** |
| `lint_template_compliance.py` | PASS | 17 warns (by-design extra sections for MAX) |

**Top 5 Sprint 1 priorities:**
1. Generate Doc 06 `.md` companion (resolves FAIL — I-C03-01)
2. Register T-001..T-004 in ground-truth ontology (I-C03-02)
3. Fix 5 obligated_party values in `02_Regulatory_Mapping_Master.md` (I-C03-03)
4. Fill 1 missing Doc 04 section (I-C03-05)
5. Verify DORA-specific role entries (Sprint 0.6)

### 7.2 Validator subagent (Sprints 1, 2, 3, 4)

A Validator sub-agent runs at the end of Sprints 1, 2, 3, 4 to provide independent review of:
- Frontmatter validity (YAML schema)
- Cross-reference completeness (every claim traceable)
- Lint pass status
- Corpus traceability (L1/L2/L3/L5 references)

### 7.3 Track B specifics (MAX tier)

- **Tier MAX** triggers: 5/5 applicable regs + 38/38 sub-domains + >250 employees + €1.5B+ revenue + AI Act high-risk.
- **Most sub-domains → RIGOROUS depth** (top 10 by clause density). Documented in `corpus_field_map.md §5.2`.
- **All 8 conditional blocks (B1-B8) activated** — B1 (AI Act), B2 (NIS 2 SOC), B3 (DORA Financial), B4 (Security Org ≥50), B5 (Special Category — NOT applicable for Case_03, but still documented), B6 (Supply Chain), B7 (CRA Classification), B8 (Multi-Actor Roles).
- **All 4 interaction scans required** — TC (Temporal Conflict), RC (Requirement Conflict), TM (Trigger Mismatch), NA (Negative Analysis).
- **Critical sub-domains flagged**: D-09.1 (DORA ICT Risk Framework), D-09.4 (DORA Art. 17-19 records), D-04.3 (T-001 Temporal), D-09.2 (T-003 IPSARA), D-06.3 (DORA Art. 30 CTPP).

## 8. Cross-references — how this folder uses the corpus

The corpus is at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` (verified 2026-08-06 — **fully populated**).

| Layer | Path | Count | Used by |
|-------|------|------:|---------|
| **L1 — Domain Manifests** | `domains/D-XX_<Name>/D-XX.manifest.json` | 10 | Doc 00, Doc 04, Doc 07 (overview) |
| **L2 — Sub-domain Manifests** | `domains/D-XX_<Name>/D-XX.Y/D-XX.Y.manifest.json` | 38 | Doc 04a, Doc 04c, Doc 04d, Doc 06 |
| **L3 — JSON Sidecars** | `domains/D-XX_<Name>/D-XX.Y/D-XX.Y.json` | 38 | Doc 04b, Doc 05b, Doc 07b, Doc 07c |
| **L4 — Merged Markdown** | `domains/D-XX_<Name>/D-XX.Y/D-XX.Y.md` | 38 | Doc 04b, Doc 05b (when L3 insufficient) |
| **L5 — Verbatim Articles** | `domains/D-XX_<Name>/D-XX.Y/articles/<REG>_Art_<N>.md` | 623 | Doc 04c, Doc 06, Citation_Index |

**Total corpus linkage cells potentially added across Sprint 2 (estimate):** ~250 cells in 4 existing docs + ~1200 ambiguity cards (top 20 sub-domains) + ~40 unique citations + 4 corpus-field-map sections.

## 9. Track B case comparison (cross-case context)

| Case | Tier | Active sub-domains | Total cards | Total clauses | Notes |
|------|------|-------------------:|------------:|--------------:|-------|
| **Case_01 (TinyTask SaaS)** | MEDIUM | 37/38 (D-08.3 INACTIVE) | ~702 | 28 + 26 = 54 | MICRO size; 2 regs (GDPR + CRA) |
| **Case_02 (SecureBorder Solutions)** | MEDIUM | 35/38 (D-08.3 + 3 NOT_ADDRESSED) | ~600 | 28 + 26 + 29 + 29 = 112 | MEDIUM size; 4 regs |
| **Case_03 (OmniBank Financial)** | **MAX** | **38/38** | **1490** | **150** | **MAX size; 5 regs; banking + AI** |

**Case_03 is the maximum-completeness test:**
- All 38 sub-domains active (vs 37 for Case_01, 35 for Case_02)
- 5/5 regulations applicable (vs 2, 4)
- 2.1× more ambiguity cards than Case_01, 2.5× more than Case_02
- 4+ strategic tensions (vs 4, 3)
- Banking sector: DORA + ECB supervision + ISO 27001 = highest regulatory density
- AI Act high-risk (OmniScore) = extra cross-regulation tension with GDPR (DPIA + FRIA overlap)

## 10. Sprint 0.6 — DORA ICT Risk Framework (dedicated sprint)

DORA Art. 5-16 ICT Risk Management Framework is the **defining characteristic** of Case_03:
- 38 DORA clauses (most of any single regulation)
- 30/38 sub-domains (DORA participation)
- D-09.1 has 43 DORA clauses alone (largest single domain for any regulation)
- T-003 (IPSARA Unified Assessment) is DORA-specific
- DORA Art. 28-30 CTPP register is mandatory for Case_03 (NOT for Case_01/C02)

**Sprint 0.6 specific deliverables:**
1. **Doc 04d** — register DORA-specific roles (CRO, DORA ICT Risk Officer, DORA Operational Resilience Lead)
2. **Doc 07b** — DORA-specific RIGOROUS depth for D-09.1 + D-09.4
3. **Doc 07c** — DORA-specific ICT Risk objectives (per D-09.1 sub-requirements)
4. **Doc 05b** — DORA-specific ambiguity cards (D-09.1 131 cards, D-09.4 116 cards)
5. **Doc 04a** — DORA Art. 28-30 CTPP register alignment (cross-ref to D-09.3)
6. **Doc 06** — DORA 38 clauses fully mapped to corpus sub-domains (DORA bare `CLx-y` prefix disambiguation)

**Sprint 0.6 outputs feed into Sprint 1 reconciliation** (the lint baseline 5 obligated_party values include DORA-specific roles).

## 11. Tooling

- **Extractor**: `/tmp/extract_case03_corpus.py` — produces `/tmp/case03_corpus.json` with per-sub-domain data (38 sub-domains × 5 case-applicable regs).
- **Stub scripts** (in `scripts/`):
  - `generate_corpus_links.py` — Sprint 0.5: auto-generate per-doc links to L1/L2/L3/L5.
  - `filter_ambiguity_cards.py` — Sprint 0.5: filter L3 ambiguity cards to Case_03-applicable regs (all 5 = no filter).
  - `regenerate_ontology.py` — Sprint 1: re-generate the ground-truth ontology after T-001..T-004 reconciliation.

## 12. Sprint status dashboard

| Sprint | Status | Output | Lint delta |
|--------|:------:|--------|:----------:|
| **Sprint 0** | ✅ | Skeleton + lint baseline + corpus_field_map | 5/6 PASS, 29W (1 FAIL on Doc 06 missing) |
| **Sprint 0.5** | ✅ | Doc 07b Track B MAX (38 sub-domains, 31 RIGOROUS + 7 STANDARD) | (covered by Sprint 1) |
| **Sprint 0.6** | ✅ | Doc 06b DORA ICT Risk Framework (26 articles, 5 tensions incl. T-005 TLPT) | (covered by Sprint 1) |
| **Sprint 1** | ✅ | Reconciliation (10 docs + ontology, 29W→6W, Doc 06 generated) | 6/6 PASS, **6W** (−79%) |
| **Sprint 2** | ✅ | Corpus enrichment (4 docs + 2 NEW + Excel 14 sheets) | 6/6 PASS, 6W (held) |
| **Sprint 3** | 🚧 | Final docs + Validator review + corpus cross-check (Doc 07b §14) | 6/6 PASS (target) |

**Aggregate lint outcome (Sprint 3 final):** 6/6 PASS, 0 errors, 6 warnings (all non-blocking — see `validation/LINT_REPORT_AFTER_RECONCILE.md` §3 for full diff vs baseline).

## 13. Navigation — file inventory

| Path | Type | Sprint | Doc ID | Highlight |
|------|------|:------:|--------|-----------|
| `00_Taxonomy_Reference.md` | doc | 0 | AEGIS-P3-RICH-00-TAX | D-01..D-10 macro-domains |
| `Doc02_INTAKE_FORM.md` | doc | 0 | AEGIS-P3-RICH-01-INTAKE | OmniBank intake snapshot |
| `Doc03_Company_Context_Assessment.md` | doc | 1 | AEGIS-P3-RICH-04-CCA | S = MAX, 5,000+ emp, ISO 27001 |
| `Doc04_Architecture_DataInventory.md` | doc | 2 | AEGIS-P3-RICH-04a-ARCH | 38 sub-domains × corpus manifest path |
| `Doc05_Security_Posture.md` | doc | 2 | AEGIS-P3-RICH-04b-SEC | ISO 27001 + DORA Art. 5-16 baseline |
| `Doc06_ThirdParty_Landscape.md` | doc | 2 | AEGIS-P3-RICH-04c-3P | **DORA Art. 28-30 CTPP register** (Case_03-specific) |
| `Doc07_Org_Roles_RACI.md` | doc | 1 | AEGIS-P3-RICH-04d-RACI | 38 active sub-domains (D-08.3 ACTIVE under NIS 2 + DORA) |
| `Doc08_Regulatory_Applicability.md` | doc | 1 | AEGIS-P3-RICH-05-APP | 5/5 regulations applicable |
| `Doc09_Ambiguity_Register.md` | doc | 2 | AEGIS-P3-RICH-05b-AMBIG | **1,490 ambiguity cards** (NEW in Rich) |
| `Doc10_Clause_Mapping_Matrix.md` | doc | 1 | AEGIS-P3-RICH-06-MAP | 150 clauses (28+26+29+38+29) |
| `Doc12_Structured_Compliance_Matrix.md` | doc | 1 | AEGIS-P3-RICH-07-MATRIX | 4 strategic tensions (T-001..T-004) + T-005 |
| **`Doc11_DORA_ICT_Risk_Framework.md`** | doc | 0.6 | AEGIS-P3-RICH-06b-DORA | **NEW — DORA-specific** (26 articles, 5 tensions) — not in legacy |
| **`Doc13_Proportionality_Profile.md`** | doc | 0.5+3 | AEGIS-P3-07b | **NEW — Track B MAX** (38 sub-domains vs Case_02's 35); §14 Sprint 3 cross-check |
| `Doc14_Adjusted_Goals.md` | doc | 2 | AEGIS-P3-RICH-07c-ADJ | Tensions resolved (T-001 max-SLA, T-002 cryptographic sharding, T-003 IPSARA, T-004 CRA-following) |
| `Citation_Index.md` | doc | 2 | AEGIS-P3-RICH-CITATION | Master citation registry |
| `phase1_ontology.yaml` | ontology | 1 | — | 5 tensions + obligated_party enum normalised |
| `corpus_field_map.md` | map | 0 | — | corpus L1/L2/L3 → case fields (500+ lines) |
| `Case_03_Phase1_RICH.xlsx` | excel | 2 | — | 14 sheets parallel to legacy `.xlsx` |
| `README.md` | doc | 0+3 | AEGIS-P3-RICH-README | This file |
| `scripts/generate_corpus_links.py` | script | 0 | — | Sprint 0.5 stub |
| `scripts/filter_ambiguity_cards.py` | script | 0 | — | Sprint 0.5 stub |
| `scripts/regenerate_ontology.py` | script | 0 | — | Sprint 1 stub |
| `validation/LINT_REPORT_BEFORE.md` | report | 0 | — | Sprint 0 baseline (5/6 PASS, 29W, 1 FAIL) |
| `validation/LINT_REPORT_AFTER_RECONCILE.md` | report | 1 | — | Sprint 1 reconciliation (6/6 PASS, 6W) |
| `validation/SPRINT1_REPORT.md` | report | 1 | — | Sprint 1 completion |
| `validation/SPRINT2_ENRICHMENT_REPORT_EXISTING.md` | report | 2 | — | Sprint 2 enrichment of existing docs |
| `validation/SPRINT2_ENRICHMENT_REPORT_NEW.md` | report | 2 | — | Sprint 2 NEW docs (06b + 05b) |
| `validation/SPRINT3_REPORT.md` | report | 3 | — | Sprint 3 final summary |
| `validation/VALIDATOR_SPRINT3.md` | review | 3 | — | Validator sub-agent verdict (Sprint 3) |
| **`PROJECT_STATE.md`** | doc | 3 | AEGIS-P3-RICH-STATE | **NEW** — Phase 1 Rich Mode status snapshot |
| **`RICH_VS_LEGACY.md`** | doc | 3 | AEGIS-P3-RICH-DIFF | **NEW** — Diff summary (Rich vs legacy) |

**Highlights (Rich vs legacy):**
- **38 sub-domains** vs Case_02's 35 (Case_02 has D-08.3 + 3 NOT_ADDRESSED) — Case_03 is MAX
- **5/5 applicable regulations** vs Case_02's 4 (no DORA) and Case_01's 2 (no DORA / NIS 2 / AI Act)
- **Doc 06b** (NEW in Rich) — DORA ICT Risk Framework dedicated doc, **not in legacy**
- **Doc 07b** (NEW in Rich) — Track B MAX proportionality profile, **not in legacy**
- **Doc 07c** (NEW in Rich) — Adjusted Objectives with tensions resolved (placeholder for Sprint 4 fill)
- **Doc 05b** (NEW in Rich) — 1,490 ambiguity cards
- **Citation_Index.md** (NEW in Rich) — master citation registry
- **Excel Case_03_Phase1_RICH.xlsx** — 14-sheet workbook parallel to legacy

## 14. See also

- `validation/LINT_REPORT_BEFORE.md` — Sprint 0 lint baseline (5/6 PASS, 1 FAIL on Doc 06 missing)
- `corpus_field_map.md` — exact corpus field → case field mapping (500+ lines)
- `../PROJECT_STATE.md` — case profile (Phase 1+2 COMPLETE, 38 obligations derived, 4 tensions resolved)
- `../01_PHASE1_CONTEXT_RICH/` — legacy version (read-only, Phase 2 complete)
- `../../../00_METHODOLOGY/PHASE1_STRATEGY.md` — Phase 1 strategy (Track B tier definition in §8)
- `../../../00_METHODOLOGY/REGULATORY_BASELINE.md` — frozen corpus contract
- `../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/STRUCTURE_REFERENCE.md` — corpus data dictionary
