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
Case Study: OmniBank Financial Systems S.A.


EXCEL FILE LOCATION

File: 06_Clause_Mapping_Matrix.xlsx
Path: `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT/`
Created: 2026-04-01
Version: 1.0 (Pending)
Sheets: 10 (COVER, GDPR_MAPPING, CRA_MAPPING, NIS2_MAPPING, DORA_MAPPING, AIACT_MAPPING, CONSOLIDATED_VIEW, COMPLEMENTARITY_ANALYSIS, APPLICABILITY_CONDITIONS, NORMATIVE_INTENSITY)
Note: ALL 5 regulations applicable — maximum regulatory coverage

OMNIBANK APPLICABILITY CONTEXT

| Regulation | Applicable? | obligatedParty | Clause Count | Sub-Domains Covered |
|------------|-------------|----------------|--------------|---------------------|
| GDPR | YES | CONTROLLER + PROCESSOR | 28 | 19/38 (50.0%) |
| CRA | YES | MANUFACTURER | 26 | 22/38 (57.9%) |
| NIS 2 | YES | ESSENTIAL_ENTITY | 29 | 24/38 (63.2%) |
| DORA | YES | FINANCIAL_ENTITY | 38 | 29/38 (76.3%) |
| AI Act | YES | PROVIDER (High-Risk) | 29 | 13/38 (34.2%) |
| **TOTAL** | **5/5** | **—** | **150** | **38/38 (100%)** |

SHEET STRUCTURE (10 Sheets)


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
| Case Study | OmniBank Financial Systems S.A. |
| Applicable Regulations | GDPR, CRA, NIS 2, DORA, AI Act |

SHEET 2: GDPR_MAPPING (T1)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| OmniBank Relevance | Company Context Reference |

Data Validation:
- obligatedParty: CONTROLLER, PROCESSOR, JOINT_CONTROLLER (canonical — see `00_METHODOLOGY/SCHEMA/obligated_party.yaml`); multi-value sets allowed (e.g. `CONTROLLER, PROCESSOR`)
- obligationType: CONTINUOUS, PERIODIC, ONE_TIME, TRIGGERED
- Normative Weight: 1, 2, 3 (per T9)

Per-Clause obligatedParty Re-Derivation (2026-07-03):
This re-derivation addresses the historical bug where every GDPR clause was
hardcoded as CONTROLLER, even though OmniBank is a PROCESSOR for
regulatory reporting to BaFin/ECB (per `01_Company_Context.md` Layer 1 §3.1,
Layer 3 Q73/Q75, and §7 Role Matrix: "GDPR | CONTROLLER + PROCESSOR | Art. 32
security, Art. 33 breach notification"). The canonical enum
(`00_METHODOLOGY/SCHEMA/obligated_party.yaml` — audit note 2026-07-03) and
the atomic-clause analysis for GDPR Ch. 4 (Controller/Processor) confirm that
several GDPR clauses apply to both controllers and processors. Article→role
classification follows the regulatory text of Art. 4(7)/(8), Art. 28(1)-(3),
Art. 29, Art. 30(1)/(2), Art. 31, Art. 32(1), Art. 33(1)/(2), Art. 37, and
Art. 39(1)(b). The classification below is mirrored in
`08_Obligation_Derivation.md` (Obligated Party column) and
`phase1_ontology.yaml` (`obligated_party: [controller, processor]`).

| Clause ID | Article (aegis-internal mapping) | Target Sub-Domain | obligatedParty | Rationale |
|-----------|----------------------------------|-------------------|----------------|-----------|
| GDPR-C01 | Art. 5(1)(a-b,d) Lawfulness/fairness | D-05.1 | CONTROLLER | Principle — controller-only |
| GDPR-C02 | Art. 5(1)(c) Data minimisation | D-05.2 | CONTROLLER | Principle — controller-only |
| GDPR-C03 | Art. 5(1)(e) Storage limitation | D-05.2 | CONTROLLER | Principle — controller-only |
| GDPR-C04 | Art. 5(1)(f) Integrity & confidentiality | D-01.1 | CONTROLLER, PROCESSOR | Art. 5(1)(f) binds both |
| GDPR-C05 | Art. 5(2) Accountability | D-01.4 | CONTROLLER | Principle — controller-only |
| GDPR-C06 | Art. 6 Lawfulness of processing | D-05.3 | CONTROLLER | Lawfulness basis — controller-only |
| GDPR-C07 | Art. 7 Conditions for consent | D-05.4 | CONTROLLER | Controller-only |
| GDPR-C08 | Art. 9 Special categories (not applicable) | — | N/A | Financial data not Art. 9 — N/A per `01_Company_Context.md` B5 |
| GDPR-C09 | Art. 12 Transparent information | D-07.1 | CONTROLLER | Controller-only transparency |
| GDPR-C10 | Art. 32 Security / Art. 29 Processing under authority | D-03.3 | CONTROLLER, PROCESSOR | Art. 32 §1 + Art. 29 bind both |
| GDPR-C11 | Art. 28(1) Processor selection | D-06.1 | CONTROLLER, PROCESSOR | Controller selects processor; processor bound by DPA |
| GDPR-C12 | Art. 28(3) DPA clauses (a)-(h) | D-06.3 | CONTROLLER, PROCESSOR | 8 mandatory DPA clauses bind both parties |
| GDPR-C13 | Art. 30(1) Records of processing (controller) | D-09.4 | CONTROLLER, PROCESSOR | Art. 30(1) controller; Art. 30(2) processor |
| GDPR-C14 | Art. 17 Right to erasure | D-01.1 | CONTROLLER, PROCESSOR | Art. 17 triggered via Art. 28(3)(g) processor return/deletion |
| GDPR-C15 | Art. 32 Security of processing (in-transit) | D-01.2 | CONTROLLER, PROCESSOR | Art. 32 §1(b) confidentiality binds both |
| GDPR-C16 | Art. 32(1)(c) Timely restore availability | D-04.4 | CONTROLLER, PROCESSOR | Art. 32(1)(c) explicitly addresses both parties |
| GDPR-C17 | Art. 32 / Art. 29 Authorisation | D-03.3 | CONTROLLER, PROCESSOR | Combined coverage — least privilege + processing under authority |
| GDPR-C18 | Art. 33(3)(d) Measures taken | D-04.2 | CONTROLLER, PROCESSOR | Containment/mitigation obligations bind processor |
| GDPR-C19 | Art. 32(1)(d) Testing/evaluating effectiveness | D-10.3 | CONTROLLER, PROCESSOR | Art. 32(1)(d) explicitly addresses both parties |
| GDPR-C20 | Art. 25 Privacy by design/default | D-09.2 | CONTROLLER | Controller-only design obligation |
| GDPR-C21 | Art. 28(1) Processor clauses (assist with breach) | D-04.3 | CONTROLLER, PROCESSOR | Art. 28(3)(f) processor assists controller with breach response |
| GDPR-C22 | Art. 30(2) Records of processing (processor) | D-09.4 | PROCESSOR | Art. 30(2) processor-only records |
| GDPR-C23 | Art. 31 Cooperation with supervisory authority | D-04.3 | CONTROLLER, PROCESSOR | Both must cooperate per Art. 31 |
| GDPR-C24 | Art. 35 DPIA (continuation) | D-09.2 | CONTROLLER | DPIA controller-only |
| GDPR-C25 | Art. 30(2) Processor records — strict obligation | D-09.1 | PROCESSOR | Art. 30(2) processor records + financial reporting scope |
| GDPR-C26 | Art. 30 Records (continuation) | D-09.1 | CONTROLLER, PROCESSOR | Records bind both (Art. 30(1)+(2)) |
| GDPR-C27 | Art. 39(1)(b) DPO awareness/training | D-08.1 | CONTROLLER, PROCESSOR | Art. 39 binds both controller and processor DPO |
| GDPR-C28 | Art. 37 DPO designation (large-scale) | D-08.2 | CONTROLLER, PROCESSOR | Art. 37(1)(b) — large-scale systematic monitoring mandates DPO for both |

Re-Derivation Summary:
- Clauses PROCESSOR-only: 2 (C22, C25) — Art. 30(2) processor records + strict processor records (financial reporting scope to BaFin/ECB)
- Clauses CONTROLLER-only: 8 (C01, C02, C03, C05, C06, C07, C09, C20, C24) — principles, lawfulness, consent, transparency, DPIA
- Clauses CONTROLLER + PROCESSOR: 17 (C04, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C21, C23, C26, C27, C28) — Art. 32, Art. 28, Art. 30(1)+(2), Art. 33(3)(d), Art. 31, Art. 37, Art. 39
- Clauses N/A: 1 (C08 — Art. 9 special categories not applicable; financial data is not Art. 9)
- **Total PROCESSOR touch-points: 19 clauses** (well above the ≥5 threshold)

Summary Row:
| Total Clauses | Weight 3 Count | Weight 2 Count | Mean NI | Sub-Domains Covered |

SHEET 3: CRA_MAPPING (T2)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article/Annex | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| OmniBank Relevance | Company Context Reference |

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
| OmniBank Relevance | Company Context Reference |

Data Validation:
- obligatedParty: ESSENTIAL_ENTITY
- obligationType: CONTINUOUS, PERIODIC, TRIGGERED (NIS 2 has 0% ONE_TIME)
- Normative Weight: 1, 2, 3 (per T9)

Summary Row:
| Total Clauses | Weight 3 Count | Weight 2 Count | Mean NI | Sub-Domains Covered |

SHEET 5: DORA_MAPPING (T4)
--------------------------------------------------------------------------------
Columns:
| Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description |
| obligatedParty | obligationType | Normative Weight | Justification |
| OmniBank Relevance | Company Context Reference |

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
| OmniBank Relevance | Company Context Reference |

Data Validation:
- obligatedParty: PROVIDER (High-Risk AI)
- obligationType: CONTINUOUS, PERIODIC, ONE_TIME, TRIGGERED
- Normative Weight: 1, 2, 3 (per T9)

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
| Covered Sub-Domains | 38 | 100% coverage |
| Coverage % | 100% | =Covered/38 |
| Total Clauses (All Regulations) | 150 | =SUM(GDPR:CRA:NIS2:DORA:AIACT) |
| Average Normative Intensity | 2.858 | =AVERAGE(Combined NI) |
| Sole Authority Gaps | 0 | All covered |


AUTOMATED CALCULATIONS


1. Normative Intensity per Regulation:
   =AVERAGEIF(Normative Weight Range, ">0")

2. Weight 3 Percentage:
   =COUNTIF(Normative Weight Range, 3) / COUNTA(Normative Weight Range)

3. Sub-Domain Coverage per Regulation:
   =COUNTA(UNIQUE(Sub-Domain ID Range)) / 38

4. Cross-Regulation Overlap (Shared Scope):
   =COUNTIF(AND(GDPR<>"", CRA<>""), 1) / COUNTIF(OR(GDPR<>"", CRA<>""), 1)


OMNIBANK-SPECIFIC NOTES


**DORA Applicability (Financial Entity):**
- All 38 DORA clauses applicable
- 100% Weight 3 (unconditional mandatory obligations)
- ICT risk management framework mandatory (Art. 5-6)
- Third-party risk management (Art. 28)
- Incident reporting (Art. 17-19)

**NIS 2 Essential Entity:**
- 24h early warning mandatory
- Management liability (board can be held liable)
- Supply chain security obligations

**AI Act High-Risk (Annex III - Credit Scoring):**
- Conformity assessment before market placement
- Post-market monitoring system mandatory
- Human oversight required (Art. 14)
- Fundamental Rights Impact Assessment (FRIA)

**GDPR Financial Data:**
- Customer PII + financial transaction data
- Large-scale processing (DPIA mandatory)
- Data residency: EU only (ECB/BaFin)

**CRA Mobile App:**
- Mobile banking app is digital product
- Standard class (not critical like SecureBorder)
- Self-declaration of conformity (not notified body)


VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | Compliance Lead | Initial release - OmniBank Financial Systems case |


DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Technical Review | | | |
| AEGIS Methodology Review | | | |


METRICS SUMMARY (from 06_Clause_Mapping_Matrix.xlsx) - PENDING


**Shared Scope (Jaccard Index):** 0.72 (high overlap among GDPR, NIS 2, DORA)  
**Complementarity Index:** 0.85 (regulations reinforce each other across domains)  
**Overlap:** 28 sub-domains covered by ≥2 regulations (73.7%)  
**Strategic Tensions:** 4 identified tensions (see 09_Strategic_Tensions_Report.md)

**Normative Intensity:**
- GDPR Mean NI: 2.714 (71.4% Weight 3)
- CRA Mean NI: 2.923 (92.3% Weight 3)
- NIS 2 Mean NI: 2.862 (89.7% Weight 3)
- DORA Mean NI: 3.000 (100.0% Weight 3)
- AI Act Mean NI: 2.793 (82.8% Weight 3)
- Combined Mean NI: 2.858 (88.0% Weight 3)

**Coverage:**
- Total Sub-Domains: 38
- Covered: 38 (100%)
- Not Covered: 0
- Sole Authority Gaps: 0 (all covered by ≥1 regulation)
