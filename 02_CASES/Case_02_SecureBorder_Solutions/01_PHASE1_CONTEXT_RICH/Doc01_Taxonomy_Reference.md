---
document_id: AEGIS-P2-RICH-00-TAXONOMY
title: Security Control Domain Taxonomy Reference (Rich Mode)
phase: 1
version: 1.1
created: 2026-04-01
updated: 2026-08-06
author: AEGIS Research Team (Rich copy: Sprint 1 Executor, 2026-08-06)
status: RECONCILED
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 35
inactive_documented: [D-08.3 INACTIVE, 3 NOT_ADDRESSED]
source: Taxonomia.txt + Regulatory_Complementary_Mapping_Updated.txt (T6)
traceability: PhD Thesis Chapter 5, Section 5.7
inputs: []
outputs: [Doc02_INTAKE_FORM.md, Doc08_Regulatory_Applicability.md, Doc10_Clause_Mapping_Matrix.md]
reconciliation:
  sprint: 1
  role: reconciliation
  base_doc: ../00_COMMON/00_Taxonomy_Reference.md (legacy, frozen)
  notes: |
    Sprint 1 reconciliation (Case_02, 2026-08-06):
    - Frontmatter updated to AEGIS-P2-RICH-* convention (P2 = Case_02).
    - status: DRAFT → RECONCILED.
    - active_subdomains aligned to 35 (canonical for Case_02 per README.md).
    - applicable_regs aligned to [GDPR, CRA, NIS 2, AI_Act] (Case_02 omits DORA).
    - Body preserved verbatim (Sprint 1 is content-neutral; Sprint 2 adds corpus linkages).
    - Out of Sprint 1 scope: rule count update (legacy lists 38; canonical v2.0 = 46).
---

<!-- RECONCILIATION BANNER (Sprint 1, 2026-08-06):
     This is the Rich Mode copy of AEGIS-COMMON-00. Source: ../00_COMMON/00_Taxonomy_Reference.md.
     Body unchanged from legacy. Sprint 2 will add corpus linkages (L1 sub-domain .md refs).
     See SPRINT1_REPORT.md for the full fix list and LINT_REPORT_AFTER_RECONCILE.md for lint results.
-->

# Security Control Domain Taxonomy Reference

## 1. DOCUMENT PURPOSE

This document establishes the canonical 10×38 Sub-Domain taxonomy used throughout all AEGIS phases. It serves as the common vocabulary between regulations (GDPR, CRA, NIS 2, DORA, AI_Act) and implementation artifacts.

**Alignment with Class Model:** This document defines instances of the `SecurityControlDomain` class.

**Phase Usage:**
- Phase 1: Regulatory coverage mapping (T6)
- Phase 2: Rules Catalog organization
- Phase 3: Functional Node allocation

---

## 2. TAXONOMY STRUCTURE

| Domain ID | Domain Name | Sub-Domain Count | Primary Regulatory Driver |
|-----------|-------------|------------------|---------------------------|
| D-01 | Data Protection & Encryption | 4 | GDPR, CRA, AI_Act |
| D-02 | Vulnerability Management | 4 | CRA, DORA, NIS 2 |
| D-03 | Access Control | 4 | GDPR, NIS 2, CRA |
| D-04 | Incident Response | 4 | GDPR, NIS 2, CRA, AI_Act |
| D-05 | Data Lifecycle | 4 | GDPR, AI_Act |
| D-06 | Supply Chain | 4 | DORA, CRA, NIS 2 |
| D-07 | Secure Development | 4 | CRA, NIS 2, DORA |
| D-08 | Human Factors | 3 | NIS 2, DORA, GDPR |
| D-09 | Governance & Documentation | 4 | All regulations |
| D-10 | Monitoring & Audit | 3 | DORA, AI_Act, NIS 2 |
| **TOTAL** | **All Domains** | **38** | **5 regulations** |

---

## 3. SUB-DOMAIN CATALOG (38 Entries)

### D-01: Data Protection & Encryption

| Sub-Domain ID | Sub-Domain Name | Regulatory Driver | Normative Intensity (Max) | Sole Authority? |
|---------------|-----------------|-------------------|---------------------------|-----------------|
| D-01.1 | Data at Rest Encryption | GDPR-C04/C14, CRA-C07, NIS2-C18, AI-C17 | 3.000 | No |
| D-01.2 | Data in Transit Encryption | GDPR-C15, CRA-C08, NIS2-C19, AI-C17 | 3.000 | No |
| D-01.3 | Cryptographic Key Management | CRA-C15, NIS2-C18, AI-C17 | 3.000 | No |
| D-01.4 | Data Integrity Mechanisms | GDPR-C05, CRA-C09, AI-C17/C18 | 3.000 | No |

### D-02: Vulnerability Management

| Sub-Domain ID | Sub-Domain Name | Regulatory Driver | Normative Intensity (Max) | Sole Authority? |
|---------------|-----------------|-------------------|---------------------------|-----------------|
| D-02.1 | Vulnerability Identification | CRA-C01/C17, NIS2-C12, AI-C03/C16 | 3.000 | No |
| D-02.2 | Patch Management & Updates | CRA-C04/C19, NIS2-C12 | 3.000 | No |
| D-02.3 | Coordinated Vuln. Disclosure | CRA-C21/C26, NIS2-C13 | 3.000 | No |
| D-02.4 | Threat-Led Penetration Testing | NIS2-C13, AI-C04 | 3.000 | No |

### D-03: Access Control

| Sub-Domain ID | Sub-Domain Name | Regulatory Driver | Normative Intensity (Max) | Sole Authority? |
|---------------|-----------------|-------------------|---------------------------|-----------------|
| D-03.1 | Identity Lifecycle Management | CRA-C05, NIS2-C19, AI-C15 | 3.000 | No |
| D-03.2 | Multi-Factor Authentication | CRA-C06, NIS2-C20, AI-C15 | 3.000 | No |
| D-03.3 | Authorization & Least Privilege | GDPR-C10/C17, NIS2-C20 | 3.000 | No |
| D-03.4 | Secure System Defaults | CRA-C03 | 3.000 | **Yes (CRA)** |

### D-04: Incident Response

| Sub-Domain ID | Sub-Domain Name | Regulatory Driver | Normative Intensity (Max) | Sole Authority? |
|---------------|-----------------|-------------------|---------------------------|-----------------|
| D-04.1 | Incident Detection & Triage | CRA-C13, NIS2-C28/C29, AI-C25 | 3.000 | No |
| D-04.2 | Containment & Mitigation | GDPR-C18, CRA-C11, NIS2-C05 | 3.000 | No |
| D-04.3 | Regulatory Notification | GDPR-C21/C23, CRA-C25, NIS2-C25/C26/C27, AI-C26/C29 | 3.000 | No |
| D-04.4 | Data Restoration & Recovery | GDPR-C16, NIS2-C06/C07 | 3.000 | No |

### D-05: Data Lifecycle

| Sub-Domain ID | Sub-Domain Name | Regulatory Driver | Normative Intensity (Max) | Sole Authority? |
|---------------|-----------------|-------------------|---------------------------|-----------------|
| D-05.1 | Data Minimization | GDPR-C01, CRA-C10, AI-C05/C06/C08 | 3.000 | No |
| D-05.2 | Retention & Archiving | GDPR-C02/C03, AI-C07 | 3.000 | No |
| D-05.3 | Right to Erasure | GDPR-C06, CRA-C16 | 3.000 | No |
| D-05.4 | Data Portability | GDPR-C07 | 3.000 | **Yes (GDPR)** |

### D-06: Supply Chain

| Sub-Domain ID | Sub-Domain Name | Regulatory Driver | Normative Intensity (Max) | Sole Authority? |
|---------------|-----------------|-------------------|---------------------------|-----------------|
| D-06.1 | Vendor Risk Assessment | GDPR-C11, NIS2-C08/C23 | 3.000 | No |
| D-06.2 | Software Bill of Materials (SBOM) | CRA-C18 | 3.000 | **Yes (CRA)** |
| D-06.3 | Contractual Security Obligations | GDPR-C12, NIS2-C09 | 3.000 | No |
| D-06.4 | Third-Party Boundary Management | NIS2-C24 | 3.000 | **Yes (NIS 2)** |

### D-07: Secure Development

| Sub-Domain ID | Sub-Domain Name | Regulatory Driver | Normative Intensity (Max) | Sole Authority? |
|---------------|-----------------|-------------------|---------------------------|-----------------|
| D-07.1 | Secure-by-Design Principles | GDPR-C09, CRA-C02/C22, NIS2-C10 | 3.000 | No |
| D-07.2 | Secure Coding Practices | CRA-C02, NIS2-C11 | 3.000 | No |
| D-07.3 | CI/CD Pipeline Security | NIS2-C11 | 3.000 | **Yes (NIS 2)** |
| D-07.4 | Change Management | NIS2-C10 | 3.000 | **Yes (NIS 2)** |

### D-08: Human Factors

| Sub-Domain ID | Sub-Domain Name | Regulatory Driver | Normative Intensity (Max) | Sole Authority? |
|---------------|-----------------|-------------------|---------------------------|-----------------|
| D-08.1 | General Security Awareness | GDPR-C27, NIS2-C14 | 3.000 | No |
| D-08.2 | Role-Specific Competence | GDPR-C28, NIS2-C15, AI-C14/C15/C24 | 3.000 | No |
| D-08.3 | Management Board Training | NIS2-C02 | 3.000 | **Yes (NIS 2)** |

### D-09: Governance & Documentation

| Sub-Domain ID | Sub-Domain Name | Regulatory Driver | Normative Intensity (Max) | Sole Authority? |
|---------------|-----------------|-------------------|---------------------------|-----------------|
| D-09.1 | Information Security Policies | GDPR-C08/C25/C26, CRA-C24, NIS2-C01/C03, AI-C12/C13/C20/C23 | 3.000 | No |
| D-09.2 | Impact & Risk Assessments | GDPR-C20/C24, CRA-C23, NIS2-C04, AI-C01/C02/C22/C28 | 3.000 | No |
| D-09.3 | Asset Inventories | NIS2-C07 | 3.000 | **Yes (NIS 2)** |
| D-09.4 | Records of Processing | GDPR-C13/C22, AI-C11 | 3.000 | No |

### D-10: Monitoring & Audit

| Sub-Domain ID | Sub-Domain Name | Regulatory Driver | Normative Intensity (Max) | Sole Authority? |
|---------------|-----------------|-------------------|---------------------------|-----------------|
| D-10.1 | Continuous Security Monitoring | CRA-C12, NIS2-C29, AI-C25 | 3.000 | No |
| D-10.2 | Audit Logging & Traceability | CRA-C14, NIS2-C22, AI-C09/C10/C19 | 3.000 | No |
| D-10.3 | Compliance Testing | GDPR-C19, CRA-C20, NIS2-C13, AI-C21/C27 | 3.000 | No |

---

## 4. SOLE AUTHORITY SUMMARY

### 4.1 Global Sole Authority (All 5 Regulations)

| Sub-Domain | Sole Authority Regulation | Risk if Regulation Not Applicable |
|------------|---------------------------|-----------------------------------|
| D-02.3 | CRA | Zero regulatory mandate |
| D-03.4 | CRA | Zero regulatory mandate |
| D-05.4 | GDPR | Zero regulatory mandate |
| D-06.2 | CRA | Zero regulatory mandate |
| D-07.2 | CRA, NIS 2 | Zero regulatory mandate (if both excluded) |
| D-07.4 | NIS 2 | Zero regulatory mandate |
| D-08.3 | NIS 2 | Zero regulatory mandate |
| D-09.3 | NIS 2 | Zero regulatory mandate |

**Total:** 8/38 sub-domains (21.1%) have sole authority

**Note:** D-07.2 (Secure Coding) is covered by both CRA (CRA-C02) and NIS 2 (NIS2-C11) — not sole authority. D-07.4 (Change Management) is NIS 2 sole authority (NIS2-C10).

### 4.2 SecureBorder-Specific Sole Authority (GDPR + CRA + NIS 2 + AI_Act)

Since SecureBorder Solutions has **GDPR, CRA, NIS 2, and AI_Act** applicable (DORA does not apply), the sole authority gaps are:

| Sub-Domain | Sole Authority | SecureBorder Status | Gap Risk |
|------------|----------------|---------------------|----------|
| D-02.3 | CRA | ✅ APPLICABLE | **COVERED** |
| D-03.4 | CRA | ✅ APPLICABLE | **COVERED** |
| D-05.4 | GDPR | ✅ APPLICABLE | **COVERED** |
| D-06.2 | CRA | ✅ APPLICABLE | **COVERED** |
| D-07.2 | CRA, NIS 2 | ✅ APPLICABLE (both) | **COVERED** |
| D-07.4 | NIS 2 | ✅ APPLICABLE | **COVERED** |
| D-08.3 | NIS 2 | ✅ APPLICABLE | **COVERED** |
| D-09.3 | NIS 2 | ✅ APPLICABLE | **COVERED** |

**SecureBorder Coverage:** 8/8 sole authority sub-domains covered (100%)  
**SecureBorder Gaps:** 0/8 — All sole authority sub-domains are covered by applicable regulations!

**Mitigation:** No additional mitigation required — NIS 2 and CRA coverage ensures all sole authority gaps are addressed.

---

## 5. NORMATIVE INTENSITY REFERENCE (T9)

### 5.1 Global Normative Intensity (All 5 Regulations)

| Regulation | Mean NI | Weight 3 % | Weight 2 % | Weight 1 % | Total Clauses |
|------------|---------|------------|------------|------------|---------------|
| DORA | 3.000 | 100.0% | 0.0% | 0.0% | 38 |
| CRA | 2.923 | 92.3% | 7.7% | 0.0% | 26 |
| NIS 2 | 2.862 | 89.7% | 10.3% | 0.0% | 29 |
| AI_Act | 2.793 | 82.8% | 17.2% | 0.0% | 29 |
| GDPR | 2.714 | 71.4% | 28.6% | 0.0% | 28 |
| **COMBINED** | **2.858** | **88.0%** | **12.0%** | **0.0%** | **150** |

### 5.2 SecureBorder-Specific Normative Intensity (GDPR + CRA + NIS 2 + AI_Act)

| Regulation | Mean NI | Weight 3 % | Weight 2 % | Weight 1 % | Total Clauses | Sub-Domains Covered |
|------------|---------|------------|------------|------------|---------------|---------------------|
| **GDPR** | 2.714 | 71.4% | 28.6% | 0.0% | 28 | 19/38 (50.0%) |
| **CRA** | 2.923 | 92.3% | 7.7% | 0.0% | 26 | 22/38 (57.9%) |
| **NIS 2** | 2.862 | 89.7% | 10.3% | 0.0% | 29 | 24/38 (63.2%) |
| **AI_Act** | 2.793 | 82.8% | 17.2% | 0.0% | 29 | 13/38 (34.2%) |
| **SECUREBORDER COMBINED** | **2.842** | **86.5%** | **13.5%** | **0.0%** | **112** | **35/38 (92.1%)** |

**Key Insights for SecureBorder:**
- Higher NI than GDPR alone (2.842 vs 2.714) due to NIS 2 and CRA overlay
- 86.5% of obligations are unconditional (Weight 3)
- AI_Act contributes 29 clauses but only 13 sub-domains (governance-focused)
- NIS 2 adds critical operational requirements (incident response, supply chain)

---

## 6. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | AEGIS Research Team | Initial release - SecureBorder Solutions case |

---

## 7. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | AEGIS Research Team | | 2026-04-01 |
| AEGIS Methodology Review | | | |
| Technical Review (CTO) | | | |
| Business Review (CEO) | | | |

---

**Next Document:** 01_Company_Context.md  
**Dependency:** None (foundational reference)  
**Case Study:** SecureBorder Solutions (High Complexity)
