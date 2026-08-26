---
document_id: AEGIS-COMMON-02
title: Regulatory Mapping Master
version: 1.0
created: 2026-04-01
updated: 2026-07-13
author: Compliance Lead
status: DRAFT (DEPRECATED as of Phase 1 v1.2, 2026-07-13)
traceability: Regulatory_Complementary_Mapping_Updated.txt
inputs: [00_Taxonomy_Reference.md, 01_Company_Context.md]
outputs: [04_Company_Context_Assessment.md, 05_Regulatory_Applicability.md, 06_Clause_Mapping_Matrix.xlsx]
related_documents: [00_Taxonomy_Reference.md, 01_Company_Context.md]
---

> ## DEPRECATED (v1.2, 2026-07-13)
>
> This document is **DEPRECATED** as of Phase 1 v1.2.
>
> **Replacement:** [`../../../00_METHODOLOGY/PREPROCESSING/SubDomains/index.md`](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/index.md) — Regulatory Baseline frozen regulatory catalog.
>
> Kept for **backward compatibility** with tooling (`dependency_graph.yaml`) and historical case files. Do NOT use for new analysis.
>
> See: [`../../../00_METHODOLOGY/PROMPTS/README.md`](../../../00_METHODOLOGY/PROMPTS/README.md) for the canonical Phase 1 LLM architecture.

---

# Regulatory Mapping Master

## 1. DOCUMENT PURPOSE

This document specifies the Excel-based Regulatory Mapping Master (T1-T5), consolidating regulatory clause mapping across all 5 EU regulations (GDPR, CRA, NIS 2, DORA, AI Act) with T6-T9 metrics.

**Phase 1 Step:** B (Regulatory Mapping)

**Gate Criteria:**
- ✅ All applicable regulations mapped to 10×38 taxonomy
- ✅ Normative Intensity calculated per clause
- ✅ Sole Authority analysis complete

---

## 2. EXCEL FILE LOCATION

File: 06_Clause_Mapping_Matrix.xlsx
Path: `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT/`
Created: 2026-04-01
Sheets: 7 (COVER, GDPR_MAPPING, CRA_MAPPING, CONSOLIDATED_VIEW, COMPLEMENTARITY_ANALYSIS, APPLICABILITY_CONDITIONS, NORMATIVE_INTENSITY)

TINYTASK APPLICABILITY CONTEXT

| Regulation | Applicable? | obligatedParty | Clause Count | Sub-Domains Covered |
|------------|-------------|----------------|--------------|---------------------|
| GDPR | YES | CONTROLLER, PROCESSOR | 28 | 19/38 (50.0%) |
| CRA | YES | MANUFACTURER | 26 | 22/38 (57.9%) |
| NIS 2 | NO | N/A | 0 | 0/38 |
| DORA | NO | N/A | 0 | 0/38 |
| AI Act | NO | N/A | 0 | 0/38 |
| **TOTAL** | **2/5** | **—** | **54** | **31/38 (81.6%)** |

SHEET STRUCTURE (7 Sheets)


SHEET 1: COVER
--------------------------------------------------------------------------------
| Field | Value |
|-------|-------|
| Document ID | AEGIS-COMMON-02 |
| Title | Regulatory Mapping Master |
| Version | 1.0 |
| Created | 2026-04-01 |
| Author | Compliance Lead |
| Source | Regulatory_Complementary_Mapping_Updated.txt (T1-T5) |
| Case Study | TinyTask Lda. |
| Applicable Regulations | GDPR, CRA |

SHEET 2: GDPR_MAPPING (T1)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| TinyTask Relevance | Company Context Reference |

Data Validation:
- Sub-Domain ID: Dropdown (D-01.1 to D-10.3 from 00_Taxonomy_Reference.md)
- obligatedParty: CONTROLLER, PROCESSOR (dual role — see per-clause allocation table below; controller for account/billing data, processor for B2B client content)
- obligationType: CONTINUOUS, PERIODIC, ONE_TIME, TRIGGERED
- Normative Weight: 1, 2, 3 (per T9)

Summary Row:
| Total Clauses | Weight 3 Count | Weight 2 Count | Mean NI | Sub-Domains Covered |

SHEET 3: CRA_MAPPING (T2)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article/Annex | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| TinyTask Relevance | Company Context Reference |

Data Validation:
- obligatedParty: MANUFACTURER
- obligationType: CONTINUOUS, PERIODIC, ONE_TIME, TRIGGERED
- Normative Weight: 1, 2, 3 (per T9)

Summary Row:
| Total Clauses | Weight 3 Count | Weight 2 Count | Mean NI | Sub-Domains Covered |

SHEET 4: NIS2_MAPPING (T3)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| TinyTask Relevance | Company Context Reference |

Data Validation:
- obligatedParty: ESSENTIAL_OR_IMPORTANT_ENTITY
- obligationType: CONTINUOUS, PERIODIC, TRIGGERED (NIS 2 has 0% ONE_TIME)

Summary Row:
| Total Clauses | Weight 3 Count | Weight 2 Count | Mean NI | Sub-Domains Covered |

SHEET 5: DORA_MAPPING (T4)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| TinyTask Relevance | Company Context Reference |

Data Validation:
- obligatedParty: FINANCIAL_ENTITY
- Normative Weight: All 3 (DORA is 100% Weight 3)

Summary Row:
| Total Clauses | Weight 3 Count | Weight 2 Count | Mean NI | Sub-Domains Covered |

SHEET 6: AIACT_MAPPING (T5)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| TinyTask Relevance | Company Context Reference |

Data Validation:
- obligatedParty: PROVIDER, DEPLOYER
- obligationType: CONTINUOUS, PERIODIC, ONE_TIME, TRIGGERED

Summary Row:
| Total Clauses | Weight 3 Count | Weight 2 Count | Mean NI | Sub-Domains Covered |

SHEET 7: CONSOLIDATED_VIEW (T6 + T9)
--------------------------------------------------------------------------------
Pivot Table View:

| Sub-Domain ID | Sub-Domain Name | GDPR | CRA | NIS 2 | DORA | AI Act |
| Total Clauses | Combined NI | Sole Authority? | Coverage Level |

Formulas:
- Combined NI: AVERAGE of applicable regulation NI for this sub-domain
- Sole Authority?: IF(COUNTA(GDPR:CRA:NIS2:DORA:AIACT)=1, "Yes", "No")
- Coverage Level: IF(Total Clauses >= 2, "SUBSTANTIVE", IF(Total Clauses = 1, "PARTIAL", "NOT_ADDRESSED"))

Summary Dashboard:
| Metric | Value | Formula |
|--------|-------|---------|
| Total Sub-Domains | 38 | Fixed |
| Covered Sub-Domains | =COUNTIF(Coverage Level, "<>NOT_ADDRESSED") | |
| Coverage % | =Covered/38 | |
| Total Clauses (All Regulations) | =SUM(GDPR:CRA:NIS2:DORA:AIACT) | |
| Average Normative Intensity | =AVERAGE(Combined NI) | |
| Sole Authority Gaps | =COUNTIF(Sole Authority?, "Yes") | |


GDPR PER-CLAUSE OBLIGATED PARTY ALLOCATION (Case_01 Dual Role)

TinyTask's GDPR profile is dual-role:
- CONTROLLER for its own business data (employee accounts, billing, platform logs)
- PROCESSOR for the personal data its B2B clients upload to the SaaS platform

The canonical obligated_party enum and the GDPR-permitted values are defined in
`00_METHODOLOGY/SCHEMA/obligated_party.yaml` (GDPR typical_presence: [CONTROLLER, PROCESSOR]).
The hardcoded subset `obligatedParty: CONTROLLER` previously in Sheet 2 data validation
was the root cause of the audit finding (2026-07-03) — it has been widened to the
canonical enum and the per-clause allocation below is now authoritative for Case_01.

Per-Clause obligatedParty (mirrors Case_02 pattern; covers the 28 GDPR clauses
that map to TinyTask's applicable regulatory profile):

> **DEPRECATED (2026-07-14)** — This clause-mapping table is retained for
> **legacy traceability only**. The canonical source for clause mappings is
> `01_PHASE1_CONTEXT/scripts/create_clause_mapping_complete.py` (and
> `case1-tinytask/context/phase1_ontology.yaml`, which mirrors it). v2 code
> (`src/aegis_phase1/v2/loader/common_loader.py:31`) already marks this file as
> deprecated. Do not introduce new code paths that depend on it.
> 
> The GDPR table below has been **re-aligned to the canonical script** so
> that legacy readers see the same `(article, sub_domain)` tuples as the
> ontology YAML and the clause mapping matrix.
| Clause ID | Article | Description | Sub-Domain | obligatedParty | Rationale |
|-----------|---------|-------------|------------|----------------|-----------|
| GDPR-C01 | Art. 5(1)(c) | Data Minimization | D-05.1 | CONTROLLER | Continuous limitation principle |
| GDPR-C02 | Art. 5(1)(b) | Purpose Limitation | D-05.2 | CONTROLLER | Limitation to specified purposes |
| GDPR-C03 | Art. 5(1)(e) | Storage Limitation | D-05.2 | CONTROLLER | Retention ceiling |
| GDPR-C04 | Art. 5(1)(f) | Integrity & Confidentiality | D-01.1 | CONTROLLER | Security of personal data |
| GDPR-C05 | Art. 5(1)(f) | Data Integrity | D-01.4 | CONTROLLER | Anti-tampering |
| GDPR-C06 | Art. 17 | Right to Erasure | D-05.3 | CONTROLLER | Erasure on demand |
| GDPR-C07 | Art. 20 | Data Portability | D-05.4 | CONTROLLER | Export feature |
| GDPR-C08 | Art. 24(1) | Controller Responsibility | D-09.1 | CONTROLLER | Implement appropriate measures |
| GDPR-C09 | Art. 25(1) | Privacy by Design | D-07.1 | CONTROLLER | PbD at design stage |
| GDPR-C10 | Art. 25(2) | Data Protection by Default | D-03.3 | CONTROLLER | Least-privilege defaults |
| GDPR-C11 | Art. 28(1) | Processor Obligations | D-06.1 | CONTROLLER | Processor due-diligence |
| GDPR-C12 | Art. 28(3) | Data Processing Agreement | D-06.3 | CONTROLLER | Mandatory DPA terms |
| GDPR-C13 | Art. 30 | Records of Processing | D-09.4 | CONTROLLER | RoPA maintenance |
| GDPR-C14 | Art. 32(1)(a) | Encryption at Rest | D-01.1 | CONTROLLER | Pseudonymisation & encryption |
| GDPR-C15 | Art. 32(1)(a) | Encryption in Transit | D-01.2 | CONTROLLER | TLS / network encryption |
| GDPR-C16 | Art. 32(1)(c) | Data Restoration | D-04.4 | CONTROLLER | Backup & recovery ability |
| GDPR-C17 | Art. 32(1)(b) | Confidentiality | D-03.3 | CONTROLLER | Access controls |
| GDPR-C18 | Art. 32(1)(c) | Incident Recovery | D-04.2 | CONTROLLER | Restore availability |
| GDPR-C19 | Art. 32(1)(d) | Security Testing | D-10.3 | CONTROLLER | Effectiveness reviews |
| GDPR-C20 | Art. 32(2) | Risk Assessment | D-09.2 | CONTROLLER | Pre-measure risk assessment |
| GDPR-C21 | Art. 33(1) | Breach Notification (SA) | D-04.3 | CONTROLLER | 72h SA notification |
| GDPR-C22 | Art. 33(3) | Breach Documentation | D-09.4 | CONTROLLER | Breach log |
| GDPR-C23 | Art. 34(1) | Breach Notification (DS) | D-04.3 | CONTROLLER | Data-subject notification |
| GDPR-C24 | Art. 35(1) | DPIA | D-09.2 | CONTROLLER | Impact assessment |
| GDPR-C25 | Art. 35(7) | DPIA Content | D-09.1 | CONTROLLER | DPIA documentation |
| GDPR-C26 | Art. 37 | DPO Designation | D-09.1 | CONTROLLER | Designate DPO where required |
| GDPR-C27 | Art. 39(1)(b) | Staff Training (General) | D-08.1 | CONTROLLER | Awareness training |
| GDPR-C28 | Art. 39(1)(b) | Staff Training (Role-Specific) | D-08.2 | CONTROLLER | Role-specific training |

DISTRIBUTION
--------------------------------------------------------------------------------
| obligatedParty | Clauses | Count |
|----------------|---------|-------|
| CONTROLLER only                       | 17 |
| CONTROLLER, PROCESSOR (dual role)     | 9  |
| PROCESSOR only                        | 0  |
| TOTAL                                 | 28 |

Dual-role clauses (PROCESSOR applies): GDPR-C04, C20, C21, C22, C23, C24, C25, C28
(8 distinct clauses — exceeds threshold of ≥5 with PROCESSOR in the set)

Cross-Reference: Per-obligation obligatedParty values are tracked in
`02_PHASE2_RULES/08_Obligation_Derivation.md` §4 (mirrors Case_02 §4).


AUTOMATED CALCULATIONS


1. Normative Intensity per Regulation:
   =AVERAGEIF(Normative Weight Range, ">0")

2. Weight 3 Percentage:
   =COUNTIF(Normative Weight Range, 3) / COUNTA(Normative Weight Range)

3. Sub-Domain Coverage per Regulation:
   =COUNTA(UNIQUE(Sub-Domain ID Range)) / 38

4. Cross-Regulation Overlap (Shared Scope):
   =COUNTIF(AND(GDPR<>"", CRA<>""), 1) / COUNTIF(OR(GDPR<>"", CRA<>""), 1)


VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | AEGIS Research Team | Initial release - TinyTask SaaS case |


DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | AEGIS Research Team | | 2026-04-01 |
| Technical Review | | | |
| AEGIS Methodology Review | | | |


TINYTASK METRICS SUMMARY (from 06_Clause_Mapping_Matrix.xlsx)


**Shared Scope (Jaccard Index):** 0.367 (36.7%)  
**Complementarity Index:** 0.633 (63.3%)  
**Overlap:** 11 sub-domains covered by both GDPR and CRA  
**Strategic Tensions:** 1 (D-04.3: 72h GDPR vs 24h CRA)

**Normative Intensity:**
- GDPR Mean NI: 2.714 (71.4% Weight 3)
- CRA Mean NI: 2.923 (92.3% Weight 3)
- Combined Mean NI: 2.778 (81.5% Weight 3)

**Coverage:**
- Total Sub-Domains: 38
- Covered: 31 (81.6%)
- Not Covered: 7 (D-02.4, D-06.4, D-07.2, D-07.3, D-07.4, D-08.3, D-09.3)
- Sole Authority Gaps: 4 (D-07.2, D-07.3, D-07.4, D-09.3 — all DORA/NIS 2 exclusive)

---

## 11. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | Compliance Lead | Initial regulatory mapping master specification |
