---
document_id: AEGIS-P2-RICH-06-CLAUSES
title: Clause Mapping Matrix (Rich Mode)
phase: 1
version: 1.2
created: 2026-07-09
updated: 2026-08-28
author: Compliance Lead (Rich copy: Sprint 1 Executor, 2026-08-06)
status: RECONCILED
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 35
inactive_documented: [D-08.3 INACTIVE, 3 NOT_ADDRESSED]
inputs: [04_Company_Context_Assessment.md, 05_Regulatory_Applicability.md]
outputs: [07_Structured_Compliance_Matrix.md]
traceability: AEGIS Class Model → RegulatoryClause, DomainCoverageEntry classes
related_documents: [00_Taxonomy_Reference.md]
reconciliation:
  sprint: 1
  role: reconciliation
  base_doc: ../01_PHASE1_CONTEXT/06_Clause_Mapping_Matrix.md (legacy, frozen)
  notes: |
    Sprint 1 reconciliation (Case_02, 2026-08-06):
    - Frontmatter updated to AEGIS-P2-RICH-* convention (P2 = Case_02).
    - status: DRAFT → RECONCILED.
    - **I-01 partial FIX**: §8 Cross-Reference (GDPR + CRA + NIS 2 + AI_Act clauses) added with
      case-form ↔ corpus-form shim table. Canonical: case-form preserved; corpus-form added as
      parallel reference. Tension IDs T-006/T-007/T-008 extended in phase1_ontology.yaml (v1.0→v1.1).
    - Body §1–§7 preserved verbatim. §8 added with the cross-reference table.
---

<!-- RECONCILIATION BANNER (Sprint 1, 2026-08-06):
     This is the Rich Mode copy of AEGIS-P1-06.
     Source: ../01_PHASE1_CONTEXT/06_Clause_Mapping_Matrix.md.
     Body §1–§7 unchanged from legacy. §8 (Cross-Reference) added by Sprint 1 reconciliation.
     See SPRINT1_REPORT.md for the full fix list.
-->

# Clause Mapping Matrix

## 1. DOCUMENT PURPOSE

This document specifies the Excel-based Clause Mapping Matrix (Step B2), mapping regulatory clauses to the 10×38 taxonomy with Normative Intensity and gap analysis.

**Note:** The actual matrix is maintained in Excel format (`06_Clause_Mapping_Matrix.xlsx`). This document provides the specification and summary.

**Phase 1 Step:** B (Clause Mapping)

---

## 2. EXCEL STRUCTURE (7 Sheets)

### Sheet 1: COVER
| Field | Value |
|-------|-------|
| Document ID | AEGIS-P1-06 |
| Title | Clause Mapping Matrix — SecureBorder Solutions |
| Version | 1.0 |
| Created | 2026-07-09 |
| Author | Compliance Lead |
| Applicable Regulations | GDPR, CRA, NIS 2, AI_Act |

### Sheet 2: GDPR_MAPPING (T1)
**Columns:** Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description | obligatedParty | obligationType | Normative Weight | Justification | SecureBorder Relevance

**Summary for SecureBorder:**

| Metric | Value |
|--------|-------|
| Total GDPR Clauses | 28 |
| Applicable to SecureBorder | 28 |
| Weight 3 (Mandatory) | 27 (96.4%) |
| Weight 2 (Conditional) | 1 (3.6%) |
| Mean NI | 2.964 |

### Sheet 3: CRA_MAPPING (T2)
**Columns:** Clause ID | Article/Annex | Sub-Domain ID | Sub-Domain Name | Description | obligatedParty | obligationType | Normative Weight | Justification | SecureBorder Relevance

**Summary for SecureBorder:**

| Metric | Value |
|--------|-------|
| Total CRA Clauses | 26 |
| Applicable to SecureBorder | 26 |
| Weight 3 (Mandatory) | 24 (92.3%) |
| Weight 2 (Conditional) | 2 (7.7%) |
| Mean NI | 2.923 |

### Sheet 4: NIS2_MAPPING (T3)
**Columns:** Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description | obligatedParty | obligationType | Normative Weight | Justification | SecureBorder Relevance

**Summary for SecureBorder:**

| Metric | Value |
|--------|-------|
| Total NIS 2 Clauses | 29 |
| Applicable to SecureBorder | 29 (essential entity supplier) |
| Weight 3 (Mandatory) | 26 (89.7%) |
| Weight 2 (Conditional) | 3 (10.3%) |
| Mean NI | 2.897 |

### Sheet 5: AIACT_MAPPING (T5)
**Columns:** Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description | obligatedParty | obligationType | Normative Weight | Justification | SecureBorder Relevance

**Summary for SecureBorder:**

| Metric | Value |
|--------|-------|
| Total AI_Act Clauses | 28 (AI-C19 removed per D1, 2026-08-13 — SecureBorder is PROVIDER only) |
| Applicable to SecureBorder | 28 (High-Risk AI per Annex III — border control) |
| Weight 3 (Mandatory) | 27 (96.4%) |
| Weight 2 (Conditional) | 1 (3.6%) |
| Mean NI | 2.964 |

### Sheet 6: DORA
**Status:** Not applicable for SecureBorder — see `05_Regulatory_Applicability.md` §3.4 (not a financial entity per DORA Art. 2).

### Sheet 7: CONSOLIDATED_VIEW (T6 + T9)
**Pivot Table:** Sub-Domain coverage across applicable regulations (4 pivots: GDPR, CRA, NIS 2, AI_Act).

---

## 3. CLAUSE-TO-SUB-DOMAIN MAPPING SUMMARY

### GDPR Mapping (28 clauses → 10×38 taxonomy)

| Sub-Domain | Clause Count | Clauses |
|------------|--------------|---------|
| D-01 (Encryption) | 4 | GDPR-C06, C12, C14, C15 |
| D-04 (Incident Response) | 4 | GDPR-C18, C19, C20, C21 |
| D-05 (Data Lifecycle) | 7 | GDPR-C01, C02, C03, C04, C05, C08, C27 |
| D-06 (Supply Chain) | 1 | GDPR-C10 (Art. 28 — processor obligations) |
| D-07 (Secure Development) | 1 | GDPR-C09 (Art. 25 — DP by design) |
| D-08 (Human Factors) | 1 | GDPR-C26 (Art. 37 DPO) |
| D-09 (Governance) | 8 | GDPR-C07, C11, C13, C22, C23, C24, C25, C28 |
| D-10 (Monitoring) | 2 | GDPR-C16, C17 |

**Totals:** 4 + 4 + 7 + 1 + 1 + 1 + 8 + 2 = 28 ✓

### CRA Mapping (26 clauses → 10×38 taxonomy — Manufacturer + Critical Class)

| Sub-Domain | Clause Count | Clauses |
|------------|--------------|---------|
| D-01 (Encryption) | 2 | CRA-C18, C26 |
| D-02 (Vuln Management) | 4 | CRA-C04, C05, C10, C12 |
| D-03 (Access Control) | 2 | CRA-C03, C25 |
| D-04 (Incident Response) | 2 | CRA-C14, C15 |
| D-05 (Data Lifecycle) | 1 | CRA-C24 |
| D-06 (Supply Chain) | 5 | CRA-C11, C19, C20, C21, C22 |
| D-09 (Governance) | 5 | CRA-C01, C02, C08, C13, C23 |
| D-10 (Monitoring) | 4 | CRA-C06, C07, C16, C17 |

### NIS 2 Mapping (29 clauses → 10×38 taxonomy)

| Sub-Domain | Clause Count | Clauses |
|------------|--------------|---------|
| D-01 (Encryption) | 2 | NIS2-C07, C10 |
| D-02 (Vuln Management) | 2 | NIS2-C06, C19 |
| D-03 (Access Control) | 2 | NIS2-C08, C09 |
| D-04 (Incident Response) | 7 | NIS2-C03, C04, C20, C24, C25, C26, C27 |
| D-06 (Supply Chain) | 2 | NIS2-C05, C14 |
| D-07 (Secure Development) | 3 | NIS2-C21, C22, C23 |
| D-08 (Human Factors) | 3 | NIS2-C11, C12, C13 |
| D-09 (Governance) | 6 | NIS2-C01, C02, C15, C28, C29 |
| D-10 (Monitoring) | 2 | NIS2-C17, C18 |

**Totals:** 2 + 2 + 2 + 7 + 2 + 3 + 3 + 6 + 2 = 29 ✓

### AI_Act Mapping (28 clauses → 10×38 taxonomy — High-Risk AI)

| Sub-Domain | Clause Count | Clauses |
|------------|--------------|---------|
| D-01 (Encryption & Integrity) | 2 | AI-C17, C18 |
| D-03 (Access Control) | 0 | — (AI-C19 Art. 26 deployer obligations removed per D1, 2026-08-13: SecureBorder is PROVIDER only; deployer duty falls on the border-control authority) |
| D-04 (Incident Response) | 3 | AI-C25, C26, C27 (Art. 73 three-tier reporting) |
| D-06 (Supply Chain) | 2 | AI-C28, C29 (Art. 25 downstream) |
| D-07 (Secure Development) | 2 | AI-C06, C07 (Art. 10 data governance) |
| D-08 (Human Factors) | 3 | AI-C12, C14, C15 (Art. 13/14 oversight) |
| D-09 (Governance) | 11 | AI-C01, C02, C03, C04, C05, C08, C11, C13, C16, C20, C24 |
| D-10 (Monitoring) | 5 | AI-C09, C10, C21, C22, C23 |

**Totals:** 2 + 0 + 3 + 2 + 2 + 3 + 11 + 5 = 28 ✓ (AI-C11/C23 deduplicated from duplicate D-09/D-09-Records row that was present in v1.0; both legitimately belong to D-09 governance sub-domain since the binding obligation is documentation/registration, with monitoring as implementation. AI-C19 removed per D1, 2026-08-13.)

---

## 4. GAP ANALYSIS SUMMARY

| Gap ID | Sub-Domain | Sole-Reg | Clause | Gap Description | Risk Level |
|--------|------------|----------|--------|-----------------|------------|
| GAP-001 | D-07.2 | DORA | Art. 9 | No direct DORA binding for secure coding (mitigated by NIS 2 Art. 21(2)(s) SDL) | LOW |
| GAP-002 | D-07.4 | DORA | Art. 9 | No direct DORA binding for change management (mitigated by NIS 2 Art. 21(2)(m)) | LOW |
| GAP-003 | D-09.3 | DORA | Art. 9 | No direct DORA binding for asset inventories (mitigated by NIS 2 Art. 21(2)(l)) | LOW |

**Note:** All 3 gaps are DORA-exclusive in the strict sense (sole authority of DORA). Since DORA does not apply to SecureBorder (not a financial entity), these sub-domains would be formally uncovered by binding EU regulation. However, in practice:

- **D-07.2 (Secure Coding):** Covered by NIS 2 Art. 21(2)(s) (Secure system development lifecycle) and CRA Annex I §1 (Secure by design)
- **D-07.4 (Change Management):** Covered by NIS 2 Art. 21(2)(m)
- **D-09.3 (Asset Inventories):** Covered by NIS 2 Art. 21(2)(l) (Asset inventories and management)

The methodology recommends Level 2 frameworks (ISO 27001 A.8, A.14; NIST SSDF) for organisational coverage. ISO 27001 A.8 (asset management) and A.14 (secure development) already address all three.

---

## 5. NORMATIVE INTENSITY SUMMARY (T9)

| Regulation | Mean NI | Weight 3 % | Weight 2 % | Weight 1 % |
|------------|---------|------------|------------|------------|
| GDPR | 2.964 | 96.4% | 3.6% | 0.0% |
| CRA | 2.923 | 92.3% | 7.7% | 0.0% |
| NIS 2 | 2.897 | 89.7% | 10.3% | 0.0% |
| AI_Act | 2.964 | 96.4% | 3.6% | 0.0% |
| **COMBINED (SecureBorder)** | **2.937** | **93.7%** | **6.3%** | **0.0%** |

**Total Applicable Clauses:** 111 (GDPR 28 + CRA 26 + NIS 2 29 + AI_Act 28 — AI-C19 removed per D1)

---

## 6. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-09 | Compliance Lead | Initial release — SecureBorder Solutions, 4 applicable regulations (112 total clauses), HIGH complexity tier |
| 1.2 | 2026-08-28 | Executor (port Fase 0) | AI-C19 (Art. 26(1) deployer) removed per D1 (2026-08-13) — propagated to Sheet 5 metrics, AI_Act mapping table, totals and §8 shim markers. 112 → 111 clauses, AI_Act 29 → 28. |

---

## 7. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-07-09 |
| Technical Review | | | |
| AEGIS Methodology Review | | | |

---

## 8. CROSS-REFERENCE (Sprint 1 — I-01 partial FIX)

> **Purpose:** This section provides a clause-ID shim table for the 111 applicable clauses (GDPR 28 + CRA 26 + NIS 2 29 + AI_Act 28), mapping case-form IDs (e.g. `GDPR-C01`) to corpus-form article references (e.g. `Art. 5(1)(c)`). Added in Sprint 1 to support cross-doc traceability and corpus linkage.

### 8.1 GDPR Clause ID Shim (28 clauses)

| Case-form ID | Article (corpus-form) | Sub-Domain | Party role | Sub-domain context |
|--------------|----------------------|------------|------------|--------------------|
| GDPR-C01 | Art. 5(1)(c) | D-05.1 | controller | Data minimisation |
| GDPR-C02 | Art. 5(1)(e) | D-05.2 | controller | Storage limitation |
| GDPR-C03 | Art. 6 | D-05.2 | controller | Lawfulness |
| GDPR-C04 | Art. 32(1)(a) | D-01.1 | controller-processor | Encryption at rest |
| GDPR-C05 | Art. 5(1)(f) | D-01.4 | controller | Integrity |
| GDPR-C06 | Art. 17 | D-05.3 | controller-processor | Erasure |
| GDPR-C07 | Art. 20 | D-05.4 | controller | Portability |
| GDPR-C08 | Art. 24(1) | D-09.1 | controller | Responsibility of controller (case-canonical) |
| GDPR-C09 | Art. 25 | D-07.1 | controller | Privacy by design/default |
| GDPR-C10 | Art. 32 + Art. 29 | D-03.3 | controller-processor | Authorisation |
| GDPR-C11 | Art. 28(1) | D-06.1 | controller-processor | Processor selection |
| GDPR-C12 | Art. 28(3) (a)-(h) | D-06.3 | controller-processor | DPA clauses |
| GDPR-C13 | Art. 30(1)/(2) | D-09.4 | controller-processor | Records of processing |
| GDPR-C14 | Art. 32(1)(b) | D-01.2 | controller-processor | Encryption in transit |
| GDPR-C15 | Art. 32(1)(b) | D-01.2 | controller-processor | Encryption in transit |
| GDPR-C16 | Art. 32(1)(c) | D-04.4 | controller-processor | Timely restore |
| GDPR-C17 | Art. 32 + Art. 29 | D-03.3 | controller-processor | Authorisation (combined) |
| GDPR-C18 | Art. 33(3)(d) | D-04.2 | controller-processor | Measures taken |
| GDPR-C19 | Art. 32(1)(d) | D-10.3 | controller-processor | Testing/evaluating |
| GDPR-C20 | Art. 35 | D-09.2 | controller | DPIA |
| GDPR-C21 | Art. 33(1) | D-04.3 | controller | 72h notification |
| GDPR-C22 | Art. 30 | D-09.4 | controller-processor | Records of processing |
| GDPR-C23 | Art. 34 | D-04.3 | controller | Data-subject breach communication |
| GDPR-C24 | Art. 35 (cont.) | D-09.2 | controller | DPIA (continuation) |
| GDPR-C25 | Art. 24 + Art. 30 | D-09.1 | controller | Responsibility + records |
| GDPR-C26 | Art. 30 (cont.) | D-09.1 | controller | Records (continuation) |
| GDPR-C27 | Art. 39(1)(b) | D-08.1 | controller-processor | DPO awareness/training |
| GDPR-C28 | Art. 37 | D-08.2 | controller-processor | DPO designation |

> Note: Party-role entries in this table are descriptive (`controller`, `controller-processor`) and do NOT use the lint's obligated_party enum. The canonical obligated-party enum (CONTROLLER, PROCESSOR, JOINT_CONTROLLER) per `00_METHODOLOGY/SCHEMA/obligated_party.yaml` is maintained in the legacy `02_Regulatory_Mapping_Master.md` (DEPRECATED) and `02_PHASE2_RULES/`.

### 8.2 CRA, NIS 2, AI_Act Clause ID Shim (83 clauses)

The full 26 + 29 + 28 clause tables are too long to inline here. Sprint 2 will generate them programmatically from `00_METHODOLOGY/PREPROCESSING/Regulation/{CRA,NIS2,AI_Act}/Articles/Art_*.md` and `02_SecurityRules_NIST.md`. Sprint 1 markers:

- **CRA (26 clauses)**: `CRA-C01..CRA-C26` per legacy §3.2 mapping (5 sheets in xlsx). Canonical corpus-form: see `00_METHODOLOGY/PREPROCESSING/Regulation/CRA/Articles/`.
- **NIS 2 (29 clauses)**: `NIS2-C01..NIS2-C29` per legacy §3.3. Canonical corpus-form: `00_METHODOLOGY/PREPROCESSING/Regulation/NIS2/Articles/`.
- **AI_Act (28 clauses)**: `AI-C01..AI-C29` minus AI-C19 (removed per D1, 2026-08-13 — SecureBorder is PROVIDER only). Canonical corpus-form: `00_METHODOLOGY/PREPROCESSING/Regulation/AI_Act/Articles/`.

### 8.3 Tension IDs Reference

The Doc 07 matrix references 8 strategic tensions. The Phase 1 ontology (`phase1_ontology.yaml v1.1`) declares T-001 through T-008:

- T-001 — TIMING (D-04.3) — GDPR (72h) vs CRA (24h) vs NIS 2 (24h)
- T-002 — TIMING (D-04.3) — NIS 2 vs CRA 24h overlap
- T-003 — SCOPE (D-09.2) — GDPR DPIA vs AI_Act FRIA
- T-004 — REQUIREMENT (D-10.3) — CRA vs AI_Act conformity assessment
- T-005 — SCOPE (D-06.1/D-06.2/D-06.3) — SBOM vs supplier security
- T-006 — RESOURCE_CONFLICT (D-06.1) — Supplier security assessment (Sprint 1 extension)
- T-007 — RESOURCE_CONFLICT (D-07.1) — Product design SDLC (Sprint 1 extension)
- T-008 — RESOURCE_CONFLICT (D-08.1) — Annual security awareness training (Sprint 1 extension)

T-006, T-007, T-008 were previously NOT in the ontology (T-001–T-005 only); the Rich copy of `phase1_ontology.yaml` extends the ontology to v1.1 with these 3 added. See `phase1_ontology.yaml` header section.

---

**Next Document:** 07_Structured_Compliance_Matrix.md
**Gate Status:** ⏳ PENDING REVIEW
