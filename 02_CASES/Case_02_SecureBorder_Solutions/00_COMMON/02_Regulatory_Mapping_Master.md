> ## DEPRECATED (v1.2, 2026-07-13)
>
> This document is **DEPRECATED** as of Phase 1 v1.2.
>
> **Replacement:** see [`../../../00_METHODOLOGY/PREPROCESSING/SubDomains/index.md`](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/index.md) — Regulatory Baseline frozen regulatory catalog.
>
> Kept for **backward compatibility** with tooling (`dependency_graph.yaml`) and historical case files. Do NOT use for new analysis.
>
> See: [`../../../00_METHODOLOGY/PROMPTS/README.md`](../../../00_METHODOLOGY/PROMPTS/README.md) for the canonical Phase 1 LLM architecture.

---


AEGIS-COMMON-02: Regulatory Mapping Master

File Format: Excel (.xlsx) + Markdown Reference
Version: 1.0
Purpose: Consolidated T1-T5 regulatory clause mapping with T6-T9 metrics
Traceability: Regulatory_Complementary_Mapping_Updated.txt
Inputs: [00_Taxonomy_Reference.md, 01_Company_Context.md]
Outputs: [04_Company_Context_Assessment.md, 05_Regulatory_Applicability.md, 06_Clause_Mapping_Matrix.xlsx]
Case Study: SecureBorder Solutions B.V.


EXCEL FILE LOCATION

File: 06_Clause_Mapping_Matrix.xlsx
Path: `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT/`
Created: 2026-04-01
Version: 2.0 (Complete)
Sheets: 9 (COVER, GDPR_MAPPING, CRA_MAPPING, NIS2_MAPPING, AIACT_MAPPING, CONSOLIDATED_VIEW, COMPLEMENTARITY_ANALYSIS, APPLICABILITY_CONDITIONS, NORMATIVE_INTENSITY)
Note: DORA sheet excluded (not applicable)

SECUREBORDER APPLICABILITY CONTEXT

| Regulation | Applicable? | obligatedParty | Clause Count | Sub-Domains Covered |
|------------|-------------|----------------|--------------|---------------------|
| GDPR | YES | CONTROLLER + PROCESSOR | 28 | 19/38 (50.0%) |
| CRA | YES | MANUFACTURER (Critical Class) | 26 | 22/38 (57.9%) |
| NIS 2 | YES | ESSENTIAL_ENTITY_SUPPLIER | 29 | 24/38 (63.2%) |
| DORA | NO | N/A | 0 | 0/38 |
| AI Act | YES | PROVIDER (High-Risk) | 29 | 13/38 (34.2%) |
| **TOTAL** | **4/5** | **—** | **112** | **35/38 (92.1%)** |

SHEET STRUCTURE (9 Sheets)


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
| Case Study | SecureBorder Solutions B.V. |
| Applicable Regulations | GDPR, CRA, NIS 2, AI Act |

SHEET 2: GDPR_MAPPING (T1)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| SecureBorder Relevance | Company Context Reference |

Data Validation:
- obligatedParty: CONTROLLER, PROCESSOR, JOINT_CONTROLLER (canonical — see `00_METHODOLOGY/SCHEMA/obligated_party.yaml`); multi-value sets allowed (e.g. `CONTROLLER, PROCESSOR`)
- obligationType: CONTINUOUS, PERIODIC, ONE_TIME, TRIGGERED
- Normative Weight: 1, 2, 3 (per T9)

Per-Clause obligatedParty Re-Derivation (2026-07-03):
This re-derivation addresses the historical bug where every GDPR clause was
hardcoded as CONTROLLER, even though SecureBorder is a PROCESSOR for
government biometric data (per `01_Company_Context.md` Layer 1 §3.1 and
`05_Regulatory_Applicability.md` §3.1). The Regulatory Baseline source-of-truth
(`00_METHODOLOGY/PREPROCESSING/Regulation/GDPR/02_SecurityRules_NIST.md`) and the
canonical enum (`00_METHODOLOGY/SCHEMA/obligated_party.yaml` — audit note
2026-07-03) confirm that several GDPR clauses apply to both controllers
and processors. The classification below is mirrored in
`08_Obligation_Derivation.md` §12.1 traceability matrix.

| Clause ID | Article (aegis-internal mapping) | Target Sub-Domain | obligatedParty | Rationale |
|-----------|----------------------------------|-------------------|----------------|-----------|
| GDPR-C01 | Art. 5(1)(c) Data minimisation | D-05.1 | CONTROLLER | Principle — controller-only |
| GDPR-C02 | Art. 5(1)(e) Storage limitation | D-05.2 | CONTROLLER | Principle — controller-only |
| GDPR-C03 | Art. 6 Lawfulness | D-05.2 | CONTROLLER | Lawfulness basis — controller-only |
| GDPR-C04 | Art. 32 Security of processing | D-01.1 | CONTROLLER, PROCESSOR | Art. 32 §1 directly binds both |
| GDPR-C05 | Art. 5(1)(f) Integrity | D-01.4 | CONTROLLER | Principle — controller-only |
| GDPR-C06 | Art. 17 Right to erasure | D-05.3 | CONTROLLER, PROCESSOR | Erasure triggered via Art. 28(3)(g) processor return/deletion |
| GDPR-C07 | Art. 20 Data portability | D-05.4 | CONTROLLER | Data-subject right — controller-only |
| GDPR-C08 | Art. 24 Responsibility of controller | D-09.1 | CONTROLLER | Controller-only governance |
| GDPR-C09 | Art. 25 Privacy by design/default | D-07.1 | CONTROLLER | Controller-only design obligation |
| GDPR-C10 | Art. 32 Security / Art. 29 | D-03.3 | CONTROLLER, PROCESSOR | Least privilege + processing under authority |
| GDPR-C11 | Art. 28(1) Processor selection | D-06.1 | CONTROLLER, PROCESSOR | Controller selects processor; processor is bound by DPA |
| GDPR-C12 | Art. 28(3) DPA clauses (a)-(h) | D-06.3 | CONTROLLER, PROCESSOR | 8 mandatory DPA clauses bind both parties |
| GDPR-C13 | Art. 30(1)/(2) Records of processing | D-09.4 | CONTROLLER, PROCESSOR | Art. 30(2) explicitly obligates the processor |
| GDPR-C14 | Art. 32 Security of processing | D-01.1 | CONTROLLER, PROCESSOR | Art. 32 §1 directly binds both |
| GDPR-C15 | Art. 32 Security of processing | D-01.2 | CONTROLLER, PROCESSOR | Art. 32 §1(b) in-transit confidentiality binds both |
| GDPR-C16 | Art. 32(1)(c) Timely restore | D-04.4 | CONTROLLER, PROCESSOR | Art. 32(1)(c) explicitly addresses both parties |
| GDPR-C17 | Art. 32 / Art. 29 Authorisation | D-03.3 | CONTROLLER, PROCESSOR | Combined coverage |
| GDPR-C18 | Art. 33(3)(d) Measures taken | D-04.2 | CONTROLLER, PROCESSOR | Containment obligations bind processor |
| GDPR-C19 | Art. 32(1)(d) Testing/evaluating | D-10.3 | CONTROLLER, PROCESSOR | Art. 32(1)(d) explicitly addresses both parties |
| GDPR-C20 | Art. 35 DPIA | D-09.2 | CONTROLLER | DPIA is a controller obligation (per 05 §3.1 nuance) |
| GDPR-C21 | Art. 33(1) 72h supervisory authority | D-04.3 | CONTROLLER | Controller clock — 72h to SA |
| GDPR-C22 | Art. 30 Records of processing | D-09.4 | CONTROLLER, PROCESSOR | Art. 30(2) explicitly obligates the processor |
| GDPR-C23 | Art. 34 Data-subject breach communication | D-04.3 | CONTROLLER | High-risk data-subject notification — controller-only |
| GDPR-C24 | Art. 35 DPIA (continuation) | D-09.2 | CONTROLLER | DPIA controller-only |
| GDPR-C25 | Art. 24/30 Responsibility + records | D-09.1 | CONTROLLER | Governance/records — controller responsibility |
| GDPR-C26 | Art. 30 Records (continuation) | D-09.1 | CONTROLLER | Records — controller responsibility |
| GDPR-C27 | Art. 39(1)(b) DPO awareness/training | D-08.1 | CONTROLLER, PROCESSOR | Art. 39 binds both controller and processor DPO |
| GDPR-C28 | Art. 37 DPO designation | D-08.2 | CONTROLLER, PROCESSOR | Art. 37(1)(c) — large-scale Art. 9 processing mandates DPO for both |

Re-Derivation Summary:
- Clauses PROCESSOR-only: 0 (no clause in Case_02 is processor-exclusive; the processor role manifests in Art. 28/29/30/32/33(2)/37 obligations overlaid on shared sub-domains)
- Clauses CONTROLLER-only: 13 (C01, C02, C03, C05, C07, C08, C09, C20, C21, C23, C24, C25, C26)
- Clauses CONTROLLER + PROCESSOR: 15 (C04, C06, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C22, C27, C28)

Summary Row:
| Total Clauses | Weight 3 Count | Weight 2 Count | Mean NI | Sub-Domains Covered |

SHEET 3: CRA_MAPPING (T2)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article/Annex | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| SecureBorder Relevance | Company Context Reference |

Data Validation:
- obligatedParty: MANUFACTURER (Critical Class requires third-party assessment)
- obligationType: CONTINUOUS, PERIODIC, ONE_TIME, TRIGGERED
- Normative Weight: 1, 2, 3 (per T9)

Summary Row:
| Total Clauses | Weight 3 Count | Weight 2 Count | Mean NI | Sub-Domains Covered |

SHEET 4: NIS2_MAPPING (T3)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| SecureBorder Relevance | Company Context Reference |

Data Validation:
- obligatedParty: ESSENTIAL_ENTITY_SUPPLIER
- obligationType: CONTINUOUS, PERIODIC, TRIGGERED (NIS 2 has 0% ONE_TIME)
- Normative Weight: 1, 2, 3 (per T9)

Summary Row:
| Total Clauses | Weight 3 Count | Weight 2 Count | Mean NI | Sub-Domains Covered |

SHEET 5: AIACT_MAPPING (T5)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| SecureBorder Relevance | Company Context Reference |

Data Validation:
- obligatedParty: PROVIDER (High-Risk AI System per Annex III)
- obligationType: CONTINUOUS, PERIODIC, ONE_TIME, TRIGGERED
- Normative Weight: 1, 2, 3 (per T9)

Summary Row:
| Total Clauses | Weight 3 Count | Weight 2 Count | Mean NI | Sub-Domains Covered |

SHEET 6: CONSOLIDATED_VIEW (T6 + T9)
--------------------------------------------------------------------------------
Pivot Table View:

| Sub-Domain ID | Sub-Domain Name | GDPR | CRA | NIS 2 | AI Act |
| Total Clauses | Combined NI | Sole Authority? | Coverage Level |

Formulas:
- Combined NI: AVERAGE of applicable regulation NI for this sub-domain
- Sole Authority?: IF(COUNTA(GDPR:CRA:NIS2:AIACT)=1, "Yes", "No")
- Coverage Level: IF(Total Clauses >= 2, "SUBSTANTIVE", IF(Total Clauses = 1, "PARTIAL", "NOT_ADDRESSED"))

Summary Dashboard:
| Metric | Value | Formula |
|--------|-------|---------|
| Total Sub-Domains | 38 | Fixed |
| Covered Sub-Domains | =COUNTIF(Coverage Level, "<>NOT_ADDRESSED") | |
| Coverage % | =Covered/38 | |
| Total Clauses (All Regulations) | =SUM(GDPR:CRA:NIS2:AIACT) | |
| Average Normative Intensity | =AVERAGE(Combined NI) | |
| Sole Authority Gaps | =COUNTIF(Sole Authority?, "Yes") | |


AUTOMATED CALCULATIONS


1. Normative Intensity per Regulation:
   =AVERAGEIF(Normative Weight Range, ">0")

2. Weight 3 Percentage:
   =COUNTIF(Normative Weight Range, 3) / COUNTA(Normative Weight Range)

3. Sub-Domain Coverage per Regulation:
   =COUNTA(UNIQUE(Sub-Domain ID Range)) / 38

4. Cross-Regulation Overlap (Shared Scope):
   =COUNTIF(AND(GDPR<>"", CRA<>""), 1) / COUNTIF(OR(GDPR<>"", CRA<>""), 1)


SECUREBORDER-SPECIFIC NOTES


**Critical Class Products (CRA):**
- GuardianGate eGate systems require third-party conformity assessment
- Technical documentation must be maintained for 10 years post-market
- Vulnerability disclosure: 24h early warning for actively exploited vulnerabilities

**High-Risk AI (AI Act):**
- Annex III: Migration, asylum and border control management
- Conformity assessment required before placement on market
- Post-market monitoring system mandatory
- Human oversight requirement (Art. 14)

**NIS 2 Essential Entity Supplier:**
- Supply chain security obligations (Art. 21(2)(d))
- Incident notification within 24h to national CSIRT
- Management liability for non-compliance

**GDPR Special Category Data (Art. 9):**
- Biometric facial templates require explicit legal basis
- DPIA mandatory (large-scale processing of special category data)
- Data residency: EU/Schengen only per government contracts


VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | Compliance Lead | Initial release - SecureBorder Solutions case |


DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Technical Review | | | |
| AEGIS Methodology Review | | | |


METRICS SUMMARY (from 06_Clause_Mapping_Matrix.xlsx)


**Shared Scope (Jaccard Index):** 0.XX (XX.X%)  
**Complementarity Index:** 0.XX (XX.X%)  
**Overlap:** XX sub-domains covered by ≥2 regulations  
**Strategic Tensions:** X (list them)

**Normative Intensity:**
- GDPR Mean NI: 2.714 (71.4% Weight 3)
- CRA Mean NI: 2.923 (92.3% Weight 3)
- NIS 2 Mean NI: 2.862 (89.7% Weight 3)
- AI Act Mean NI: 2.793 (82.8% Weight 3)
- Combined Mean NI: 2.842 (86.5% Weight 3)

**Coverage:**
- Total Sub-Domains: 38
- Covered: 35 (92.1%)
- Not Covered: 3 (list them)
- Sole Authority Gaps: X (list them — DORA exclusive)
