---
document_id: AEGIS-P1-RICH-CIT
title: Citation Index (Rich Mode)
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Fase de Especificação 2 Executor (citation-index-builder)
status: CORPUS_ENRICHED
case: Case_01_TinyTask_SaaS
applicable_regs: [GDPR, CRA]
scope_docs_count: 13
---

# Citation Index (Rich Mode)

> Maps every regulatory reference in Case_01 Rich Phase 1 docs to corpus verbatim article files.
> Source: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX.Y/articles/<REG>_Art_<N>.md`
> Methodology: regex scan of all `.md` files in `01_PHASE1_CONTEXT_RICH/`, excluding meta-docs (`README.md`, `corpus_field_map.md`, `phase1_ontology.yaml`, `Case_01_Phase1_RICH.xlsx`).

## §1 Summary

| Metric | Value |
|--------|-------|
| Rich docs scanned | 13 |
| Total regulatory reference mentions | 29 |
| Unique (regulation, article) pairs | 18 |
| Unique article filenames | 15 |
| Found in corpus | 12 |
| Missing from corpus (coverage gaps) | 3 |
| Verbatim article copies in corpus | 623 |

## §2 GDPR Citations

> 9 unique GDPR articles referenced across Case_01 docs.

| Article | Cited in (count) | First corpus match |
|---------|------------------|--------------------|
| Art. 20 | 1 doc(s) | `domains/D-05_Data-Lifecycle/D-05.4/articles/GDPR_Art_20.md` |
| ↳ cited in | 07b_Proportionality_Profile.md | |
| Art. 28 | 2 doc(s) | `domains/D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_28.md` |
| ↳ cited in | 04c_ThirdParty_Landscape.md, 07b_Proportionality_Profile.md | |
| Art. 30 | 2 doc(s) | `domains/D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_30.md` |
| ↳ cited in | 04_Company_Context_Assessment.md, 04b_Security_Posture.md | |
| Art. 32 | 5 doc(s) | `domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_32.md` |
| ↳ cited in | 04b_Security_Posture.md, 04c_ThirdParty_Landscape.md, 04d_Org_Roles_RACI.md, 05_Regulatory_Applicability.md, 07b_Proportionality_Profile.md | |
| Art. 33 | 2 doc(s) | `domains/D-09_Governance-Documentation/D-09.4/articles/GDPR_Art_33.md` |
| ↳ cited in | 01_INTAKE_FORM.md, 04d_Org_Roles_RACI.md | |
| Art. 33(2) | 1 doc(s) | `domains/D-09_Governance-Documentation/D-09.4/articles/GDPR_Art_33.md` |
| ↳ cited in | 05_Regulatory_Applicability.md | |
| Art. 37 | 1 doc(s) | `domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_37.md` |
| ↳ cited in | 04d_Org_Roles_RACI.md | |
| Art. 37(1)(b) | 1 doc(s) | `domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_37.md` |
| ↳ cited in | 04d_Org_Roles_RACI.md | |
| Art. 5 | 1 doc(s) | `domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_5.md` |
| ↳ cited in | 04_Company_Context_Assessment.md | |

## §3 CRA Citations

> 8 unique CRA references (Articles + Annexes) across Case_01 docs.

| Reference | Cited in (count) | First corpus match |
|-----------|------------------|--------------------|
| Annex I | 4 doc(s) | `**NOT FOUND** (see §6)` |
| ↳ cited in | 04b_Security_Posture.md, 04c_ThirdParty_Landscape.md, 04d_Org_Roles_RACI.md, 05b_Ambiguity_Register.md | |
| Annex VII | 1 doc(s) | `**NOT FOUND** (see §6)` |
| ↳ cited in | 04d_Org_Roles_RACI.md | |
| Art. 13 | 1 doc(s) | `domains/D-07_Secure-Development/D-07.4/articles/CRA_Art_13.md` |
| ↳ cited in | 05_Regulatory_Applicability.md | |
| Art. 13(8) | 1 doc(s) | `domains/D-07_Secure-Development/D-07.4/articles/CRA_Art_13.md` |
| ↳ cited in | 05_Regulatory_Applicability.md | |
| Art. 14 | 2 doc(s) | `domains/D-09_Governance-Documentation/D-09.1/articles/CRA_Art_14.md` |
| ↳ cited in | 01_INTAKE_FORM.md, 04d_Org_Roles_RACI.md | |
| Art. 24 | 1 doc(s) | `domains/D-09_Governance-Documentation/D-09.1/articles/CRA_Art_24.md` |
| ↳ cited in | 01_INTAKE_FORM.md | |
| Art. 6(a) | 1 doc(s) | `domains/D-04_Incident-Response/D-04.3/articles/CRA_Art_6.md` |
| ↳ cited in | 05b_Ambiguity_Register.md | |
| Art. 7 | 1 doc(s) | `domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_7.md` |
| ↳ cited in | 01_INTAKE_FORM.md | |

## §4 Other Regulation Citations (negative-analysis context)

> Case_01's `applicable_regs = [GDPR, CRA]` per `05_Regulatory_Applicability.md`. References to NIS 2 / DORA / AI Act appear only in negative-analysis contexts (scope exclusion or out-of-applicability statements).

| Regulation | Reference | Cited in (count) | First corpus match |
|-----------|-----------|------------------|--------------------|
| NIS2 | Annex I | 1 doc(s) | `**NOT FOUND**` |
| ↳ cited in | 01_INTAKE_FORM.md | |

## §5 Cross-Citation Map (doc → refs)

> Which Rich docs cite which regulations (reverse lookup). Useful for impact analysis when a regulation is updated.

| Rich doc | GDPR refs | CRA refs | Other refs |
|----------|-----------|----------|------------|
| 01_INTAKE_FORM.md | Art. 33 | Art. 14, Art. 24, Art. 7 | Annex I |
| 04_Company_Context_Assessment.md | Art. 30, Art. 5 | — | — |
| 04b_Security_Posture.md | Art. 30, Art. 32 | Annex I | — |
| 04c_ThirdParty_Landscape.md | Art. 28, Art. 32 | Annex I | — |
| 04d_Org_Roles_RACI.md | Art. 32, Art. 33, Art. 37, Art. 37(1)(b) | Annex I, Annex VII, Art. 14 | — |
| 05_Regulatory_Applicability.md | Art. 32, Art. 33(2) | Art. 13, Art. 13(8) | — |
| 05b_Ambiguity_Register.md | — | Annex I, Art. 6(a) | — |
| 07b_Proportionality_Profile.md | Art. 20, Art. 28, Art. 32 | — | — |

## §6 Citation Audit — Coverage Gaps

> References cited in Case_01 docs but NOT found in the corpus. Each gap represents a candidate for corpus augmentation in a future sprint.

| Regulation | Reference | Cited in | Reason |
|-----------|-----------|----------|--------|
| NIS2 | Annex I | 01_INTAKE_FORM.md | NIS 2 is NOT applicable to Case_01 — reference appears in scope-exclusion context (01_INTAKE_FORM.md). Corpus does not include NIS 2 Annex files. |
| CRA | Annex I | 04b_Security_Posture.md, 04c_ThirdParty_Landscape.md, 04d_Org_Roles_RACI.md, 05b_Ambiguity_Register.md | CRA Annex I (essential cybersecurity requirements) is referenced heavily but the corpus only contains Articles, not Annexes. Future corpus augmentation target. |
| CRA | Annex VII | 04d_Org_Roles_RACI.md | CRA Annex VII (conformity assessment) — corpus gap, same as Annex I. |

## §7 Methodology

**Scan regex:** `(GDPR|CRA|NIS\s*2|DORA|AI\s*Act)\s+(Art(?:icle)?\.?\s*\d+(?:\([0-9a-z]+\))*|Annex\s+[IVX]+|Recital\s+\d+)`

**Files scanned:** 13 `.md` files in `01_PHASE1_CONTEXT_RICH/` (excluded `README.md`, `corpus_field_map.md`, `phase1_ontology.yaml`, `Case_01_Phase1_RICH.xlsx`).

**Corpus lookup:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/**/<REG>_Art_<N>.md` (623 files).

**Article normalisation:** sub-article references like `Art. 32(1)` and `Art. 32(1)(b)` are normalised to the parent article for corpus lookup (the corpus files are at article granularity, not sub-clause granularity).

**Annex normalisation:** `CRA Annex I` → filename `CRA_Annex_I.md` (which does NOT exist in the current corpus).

## §8 Gate Criteria (Fase de Especificação 3 readiness)

- [x] Index methodology documented (§7)
- [x] All 4 layers (L1-L4) represented — this doc focuses on L4 (verbatim article files); L1/L2/L3 citations are tracked inline in other docs
- [x] Cross-citation map complete (8 docs → 18 refs)
- [x] Coverage report identifies gaps (§6 — 3 gap(s))
- [ ] Spot-check audit log (deferred to Fase de Especificação 3 — requires human verification of 10% sample)