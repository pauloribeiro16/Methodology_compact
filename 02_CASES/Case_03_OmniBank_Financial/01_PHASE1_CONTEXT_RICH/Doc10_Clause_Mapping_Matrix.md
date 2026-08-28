---
document_id: AEGIS-P3-RICH-06-MAP
title: Clause Mapping Matrix (Rich Mode — Markdown Companion)
phase: 1
version: 1.1
created: 2026-08-06
updated: 2026-08-06
author: Sprint 1 Executor (clause-mapper)
status: RECONCILED
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
inactive_documented: []
complexity_tier: MAX
scale: MAX
total_clauses: 150
clause_breakdown:
  GDPR: 28
  CRA: 26
  NIS_2: 29
  DORA: 38
  AI_Act: 29
inputs: [Doc08_Regulatory_Applicability.md]
outputs: [Doc12_Structured_Compliance_Matrix.md]
sibling_of: ../01_PHASE1_CONTEXT_RICH/06_Clause_Mapping_Matrix.xlsx
xlsx_companion: ../01_PHASE1_CONTEXT_RICH/06_Clause_Mapping_Matrix.xlsx
reconciliation_notes:
  - "Sprint 1 (2026-08-06): Created `.md` companion for the legacy `.xlsx` (10 sheets, 150 clauses). The xlsx remains the source of truth; this .md is the lint-consumable summary. I-C03-01 RESOLVED — lint_cross_document_consistency now finds Doc 06."
  - "Per-regulation clause ID shim table added (§8) for GDPR-CL/CP/RT and CRA-CL corpus form, NIS2-CL, DORA-CL, AIA-CL."
  - "DORA + AI Act cross-references from Sprint 0.6 (Doc 06b) integrated into §6 and §7."
---

<!-- RECONCILED (Sprint 1, 2026-08-06): Created Markdown companion for the legacy xlsx.
The xlsx at `../01_PHASE1_CONTEXT_RICH/06_Clause_Mapping_Matrix.xlsx` is the source of truth (10 sheets, 150 clauses);
this `.md` provides the same content in lint-consumable form. Section §8 adds the per-regulation clause ID
shim table (GDPR-CL, CRA-CL, NIS2-CL, DORA-CL, AIA-CL) and migration notes for corpus integration.
-->

# Clause Mapping Matrix (Rich Mode — Markdown Companion)

## 1. Document Purpose

This document is the **Markdown companion** to `06_Clause_Mapping_Matrix.xlsx` (the legacy xlsx is the source of truth; this `.md` is the lint-consumable summary). It presents the 150 regulatory clauses mapped to the AEGIS 10×38 sub-domain taxonomy for OmniBank Financial Systems.

**Companion xlsx:** `../01_PHASE1_CONTEXT_RICH/06_Clause_Mapping_Matrix.xlsx` — 10 sheets (COVER, GDPR_MAPPING, CRA_MAPPING, NIS2_MAPPING, DORA_MAPPING, AIACT_MAPPING, CONSOLIDATED_VIEW, COMPLEMENTARITY_ANALYSIS, APPLICABILITY_CONDITIONS, NORMATIVE_INTENSITY).

**Total clauses:** 150 (GDPR 28 + CRA 26 + NIS 2 29 + DORA 38 + AI Act 29).

**Cross-references:**
- `Doc08_Regulatory_Applicability.md` — regulation-by-regulation applicability (per Clause).
- `Doc11_DORA_ICT_Risk_Framework.md` — DORA-specific deep-dive (Sprint 0.6 deliverable).
- `Doc12_Structured_Compliance_Matrix.md` — per-sub-domain coverage matrix (Phase 1 output).
- `phase1_ontology.yaml` — machine-readable ontology (150 clause mappings).

---

## 2. Metadata

| Attribute | Value |
|-----------|-------|
| Document ID | AEGIS-P3-RICH-06-MAP |
| Case | Case_03_OmniBank_Financial |
| complexityTier | MAXIMUM (5/5 regs, 38/38 sub-domains) |
| Total clauses | 150 |
| Total sub-domains | 38 (100% coverage) |
| Mean normative intensity | 2.858 |
| Weight 3 % | 88.0% |
| Sole authority sub-domains | 0 |

---

## 3. Per-Regulation Summary

| Regulation | Clauses | Weight 3 | Weight 2 | Weight 1 | Sub-Domains | Mean NI |
|------------|--------:|---------:|---------:|---------:|------------:|--------:|
| **GDPR** | 28 | 18 | 10 | 0 | 20 | 2.643 |
| **CRA** | 26 | 24 | 2 | 0 | 22 | 2.923 |
| **NIS 2** | 29 | 29 | 0 | 0 | 23 | 3.000 |
| **DORA** | 38 | 38 | 0 | 0 | 26 | 3.000 |
| **AI Act** | 29 | 29 | 0 | 0 | 15 | 3.000 |
| **TOTAL** | **150** | **138** | **12** | **0** | **38** | **2.858** |

---

## 4. GDPR Mapping (28 clauses)

| Clause ID | Article | Sub-Domain | Description | obligatedParty | obligationType | NI | Justification | Relevance |
|-----------|---------|------------|-------------|----------------|----------------|---:|---------------|-----------|
| GDPR-C01 | Art. 5(1)(c) | D-05.1 (Data Minimization) | Data shall be adequate, relevant and limited to necessary | CONTROLLER | CONTINUOUS | 3 | Core GDPR principle | HIGH |
| GDPR-C02 | Art. 5(1)(b) | D-05.2 (Purpose Limitation) | Data not kept longer than necessary | CONTROLLER | CONTINUOUS | 3 | Retention policy needed | HIGH |
| GDPR-C03 | Art. 5(1)(e) | D-05.2 (Storage Limitation) | Personal data kept in identifiable form no longer than necessary | CONTROLLER | CONTINUOUS | 3 | Retention policy needed | HIGH |
| GDPR-C04 | Art. 5(1)(f) | D-01.1 (Integrity & Confidentiality) | Protection against unauthorised access to stored data | CONTROLLER | CONTINUOUS | 2 | User passwords, task content | HIGH |
| GDPR-C05 | Art. 5(1)(f) | D-01.4 (Data Integrity) | Protection against accidental loss, destruction or damage | CONTROLLER | CONTINUOUS | 2 | Data integrity checks | HIGH |
| GDPR-C06 | Art. 17 | D-05.3 (Right to Erasure) | Right to be forgotten | CONTROLLER | TRIGGERED | 3 | Delete account feature needed | HIGH |
| GDPR-C07 | Art. 20 | D-05.4 (Data Portability) | Right to data portability | CONTROLLER | TRIGGERED | 3 | Export feature needed | MEDIUM |
| GDPR-C08 | Art. 24(1) | D-09.1 (Controller Responsibility) | Implement appropriate measures; document policies | CONTROLLER | CONTINUOUS | 2 | Security policies required | HIGH |
| GDPR-C09 | Art. 25(1) | D-07.1 (Privacy by Design) | Integrate measures into processing design | CONTROLLER | ONE_TIME | 2 | Privacy by design required | HIGH |
| GDPR-C10 | Art. 25(2) | D-03.3 (Data Protection by Default) | Only process necessary data; restrict access | CONTROLLER | ONE_TIME | 3 | Role-based access required | HIGH |
| GDPR-C11 | Art. 28(1) | D-06.1 (Processor Obligations) | Use only processors providing sufficient guarantees | CONTROLLER | ONE_TIME | 3 | Major managed hosting + managed identity + managed payment processors DPAs | HIGH |
| GDPR-C12 | Art. 28(3) | D-06.3 (Data Processing Agreement) | Mandatory contractual clauses | CONTROLLER | ONE_TIME | 3 | DPA with all processors | HIGH |
| GDPR-C13 | Art. 30 | D-09.4 (Records of Processing) | Maintain written records | CONTROLLER | CONTINUOUS | 3 | RoPA required | HIGH |
| GDPR-C14 | Art. 32(1)(a) | D-01.1 (Encryption at Rest) | Encryption of personal data at rest | CONTROLLER | CONTINUOUS | 2 | Database encryption required | HIGH |
| GDPR-C15 | Art. 32(1)(a) | D-01.2 (Encryption in Transit) | Encryption of personal data in transit | CONTROLLER | CONTINUOUS | 2 | HTTPS/TLS required | HIGH |
| GDPR-C16 | Art. 32(1)(c) | D-04.4 (Data Restoration) | Restore availability after incident | CONTROLLER | TRIGGERED | 2 | Backup/recovery needed | MEDIUM |
| GDPR-C17 | Art. 32(1)(b) | D-03.3 (Confidentiality) | Restrict access to authorised personnel | CONTROLLER | CONTINUOUS | 3 | Access control enforcement | HIGH |
| GDPR-C18 | Art. 32(1)(c) | D-04.2 (Incident Recovery) | Restore availability in timely manner | CONTROLLER | TRIGGERED | 2 | Incident response plan | MEDIUM |
| GDPR-C19 | Art. 32(1)(d) | D-10.3 (Security Testing) | Regular testing of effectiveness | CONTROLLER | PERIODIC | 3 | Security testing required | MEDIUM |
| GDPR-C20 | Art. 32(2) | D-09.2 (Risk Assessment) | Risk assessment prior to implementing measures | CONTROLLER | PERIODIC | 2 | Security risk assessment | MEDIUM |
| GDPR-C21 | Art. 33(1) | D-04.3 (Breach Notification (SA)) | Notify supervisory authority within 72 hours | CONTROLLER | TRIGGERED | 3 | CNPD notification required | HIGH |
| GDPR-C22 | Art. 33(3) | D-09.4 (Breach Documentation) | Document all personal data breaches | CONTROLLER | TRIGGERED | 3 | Breach log required | HIGH |
| GDPR-C23 | Art. 34(1) | D-04.3 (Breach Notification (DS)) | Notify data subject when high risk | CONTROLLER | TRIGGERED | 3 | User notification required | HIGH |
| GDPR-C24 | Art. 35(1) | D-09.2 (DPIA) | Data Protection Impact Assessment for high-risk processing | CONTROLLER | ONE_TIME | 3 | DPIA if high-risk processing | MEDIUM |
| GDPR-C25 | Art. 35(7) | D-09.1 (DPIA Content) | Systematic description of processing | CONTROLLER | ONE_TIME | 3 | DPIA documentation | MEDIUM |
| GDPR-C26 | Art. 37 | D-09.1 (DPO Designation) | Designate DPO where required | CONTROLLER | ONE_TIME | 2 | DPO required for special category data | HIGH |
| GDPR-C27 | Art. 39(1)(b) | D-08.1 (Staff Training (General)) | Training of staff involved in processing | CONTROLLER | PERIODIC | 3 | Security awareness training | MEDIUM |
| GDPR-C28 | Art. 39(1)(b) | D-08.2 (Staff Training (Role-Specific)) | Role-specific training | CONTROLLER | PERIODIC | 3 | Developer security training | MEDIUM |

---

## 5. CRA Mapping (26 clauses)

| Clause ID | Article | Sub-Domain | Description | obligatedParty | obligationType | NI | Justification | Relevance |
|-----------|---------|------------|-------------|----------------|----------------|---:|---------------|-----------|
| CRA-C01 | Annex I, Part I, §2(a) | D-02.1 (Vulnerability-Free Delivery) | No known exploitable vulnerabilities at delivery | MANUFACTURER | ONE_TIME | 3 | Pre-release scanning | HIGH |
| CRA-C02 | Annex I, Part I, §2(b) | D-07.1 (Secure by Default) | Product delivered in most secure default state | MANUFACTURER | ONE_TIME | 3 | Secure defaults required | HIGH |
| CRA-C03 | Annex I, Part I, §2(b) | D-03.4 (Secure Default Configuration) | Disable unused ports, no default passwords | MANUFACTURER | ONE_TIME | 3 | Secure defaults required | HIGH |
| CRA-C04 | Annex I, Part I, §2(c) | D-02.2 (Security Updates) | Product can receive updates including automatic | MANUFACTURER | ONE_TIME | 3 | Update mechanism required | HIGH |
| CRA-C05 | Annex I, Part I, §2(d) | D-03.1 (Access Control) | Protection from unauthorised access; authentication | MANUFACTURER | ONE_TIME | 3 | Authentication system | HIGH |
| CRA-C06 | Annex I, Part I, §2(d) | D-03.2 (MFA) | Authentication controls including multi-factor | MANUFACTURER | ONE_TIME | 2 | MFA recommended | MEDIUM |
| CRA-C07 | Annex I, Part I, §2(e) | D-01.1 (Encryption at Rest) | Encryption of personal and sensitive data at rest | MANUFACTURER | CONTINUOUS | 3 | Database encryption | HIGH |
| CRA-C08 | Annex I, Part I, §2(e) | D-01.2 (Encryption in Transit) | Encryption of data in transit | MANUFACTURER | CONTINUOUS | 3 | TLS required | HIGH |
| CRA-C09 | Annex I, Part I, §2(f) | D-01.4 (Data Integrity) | Protection against unauthorised manipulation | MANUFACTURER | CONTINUOUS | 3 | Data integrity checks | HIGH |
| CRA-C10 | Annex I, Part I, §2(g) | D-05.1 (Data Minimization) | Process only necessary data | MANUFACTURER | ONE_TIME | 3 | Privacy by design | HIGH |
| CRA-C11 | Annex I, Part I, §2(h) | D-04.2 (Availability Protection) | Resilience against DoS attacks | MANUFACTURER | ONE_TIME | 3 | DoS protection | MEDIUM |
| CRA-C12 | Annex I, Part I, §2(i) | D-10.1 (Attack Surface Minimization) | Minimise interfaces, unnecessary functions | MANUFACTURER | CONTINUOUS | 3 | API minimization | MEDIUM |
| CRA-C13 | Annex I, Part I, §2(j) | D-04.1 (Incident Impact Reduction) | Design to limit severity; fail-safe | MANUFACTURER | ONE_TIME | 3 | Fail-safe mechanisms | MEDIUM |
| CRA-C14 | Annex I, Part I, §2(k) | D-10.2 (Activity Logging) | Record and monitor security-relevant events | MANUFACTURER | CONTINUOUS | 3 | Audit logging | HIGH |
| CRA-C15 | Annex I, Part I, §2(l) | D-01.3 (Secure Updates) | Cryptographic integrity verification | MANUFACTURER | CONTINUOUS | 3 | Update signing | MEDIUM |
| CRA-C16 | Annex I, Part I, §2(m) | D-05.3 (Secure Data Removal) | Complete and secure deletion by users | MANUFACTURER | ONE_TIME | 3 | Delete account feature | HIGH |
| CRA-C17 | Annex I, Part II, §1 | D-02.1 (Vulnerability Tracking) | Vulnerability identification; produce SBOM | MANUFACTURER | CONTINUOUS | 3 | Ongoing vulnerability tracking | HIGH |
| CRA-C18 | Annex I, Part II, §1 | D-06.2 (SBOM) | Software Bill of Materials; document components | MANUFACTURER | CONTINUOUS | 3 | SBOM required | HIGH |
| CRA-C19 | Annex I, Part II, §2 | D-02.2 (Prompt Remediation) | Address vulnerabilities without delay | MANUFACTURER | TRIGGERED | 3 | Patch deployment process | HIGH |
| CRA-C20 | Annex I, Part II, §3 | D-10.3 (Regular Testing) | Effective and regular testing and reviews | MANUFACTURER | PERIODIC | 2 | Security testing | MEDIUM |
| CRA-C21 | Annex I, Part II, §4 | D-02.3 (Vuln Disclosure Policy) | Publish coordinated vulnerability disclosure policy | MANUFACTURER | CONTINUOUS | 3 | security.txt required | HIGH |
| CRA-C22 | Art. 13(1) | D-07.1 (Manufacturer Obligation) | Design, develop and produce per Annex I | MANUFACTURER | ONE_TIME | 3 | Annex I compliance | HIGH |
| CRA-C23 | Art. 13(2) | D-09.2 (Risk Assessment) | Cybersecurity risk assessment before market | MANUFACTURER | ONE_TIME | 3 | Pre-market risk assessment | HIGH |
| CRA-C24 | Art. 13(5) | D-09.1 (Technical Documentation) | Maintain for 10 years after market | MANUFACTURER | CONTINUOUS | 3 | Compliance documentation | HIGH |
| CRA-C25 | Art. 14(1) | D-04.3 (Vulnerability Notification) | Notify actively exploited vulnerability within 24h | MANUFACTURER | TRIGGERED | 3 | ENISA notification | HIGH |
| CRA-C26 | Art. 14(2) | D-02.3 (Severe Incident Reporting) | Report severe incidents to ENISA and CSIRTs | MANUFACTURER | TRIGGERED | 3 | Incident reporting | HIGH |

---

## 6. NIS 2 Mapping (29 clauses)

| Clause ID | Article | Sub-Domain | Description | obligatedParty | obligationType | NI | Justification | Relevance |
|-----------|---------|------------|-------------|----------------|----------------|---:|---------------|-----------|
| NIS2-C01 | Art. 21(1) | D-09.1 (Security Policies) | Implement information security policies | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Security policies required | HIGH |
| NIS2-C02 | Art. 21(2)(a) | D-08.3 (Management Training) | Management board shall receive security training | ESSENTIAL_ENTITY | PERIODIC | 3 | Board training required | HIGH |
| NIS2-C03 | Art. 21(2)(b) | D-09.1 (Risk Analysis) | Implement risk analysis and security concepts | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Risk analysis required | HIGH |
| NIS2-C04 | Art. 21(2)(c) | D-09.2 (Incident Handling) | Implement incident handling procedures | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Incident procedures | HIGH |
| NIS2-C05 | Art. 21(2)(d) | D-04.2 (Business Continuity) | Implement business continuity and backup | ESSENTIAL_ENTITY | CONTINUOUS | 3 | BCP required | HIGH |
| NIS2-C06 | Art. 21(2)(e) | D-04.4 (Disaster Recovery) | Implement disaster recovery plans | ESSENTIAL_ENTITY | CONTINUOUS | 3 | DRP required | HIGH |
| NIS2-C07 | Art. 21(2)(f) | D-09.3 (Asset Management) | Maintain asset inventories | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Asset inventory | MEDIUM |
| NIS2-C08 | Art. 21(2)(g) | D-06.1 (Supply Chain Security) | Assess security of suppliers | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Supplier assessment | HIGH |
| NIS2-C09 | Art. 21(2)(h) | D-06.3 (Supplier Contracts) | Include security in supplier contracts | ESSENTIAL_ENTITY | ONE_TIME | 3 | Contractual clauses | HIGH |
| NIS2-C10 | Art. 21(2)(i) | D-07.4 (Change Management) | Implement change management procedures | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Change control | MEDIUM |
| NIS2-C11 | Art. 21(2)(j) | D-07.3 (CI/CD Security) | Secure development and deployment pipelines | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Pipeline security | MEDIUM |
| NIS2-C12 | Art. 21(2)(k) | D-02.2 (Vulnerability Management) | Implement vulnerability disclosure policy | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Vuln management | HIGH |
| NIS2-C13 | Art. 21(2)(l) | D-10.3 (Security Testing) | Conduct regular security testing | ESSENTIAL_ENTITY | PERIODIC | 3 | Security testing | MEDIUM |
| NIS2-C14 | Art. 21(2)(m) | D-08.1 (Security Training) | Provide security awareness training | ESSENTIAL_ENTITY | PERIODIC | 3 | Awareness training | MEDIUM |
| NIS2-C15 | Art. 21(2)(n) | D-08.2 (Role-Based Training) | Provide role-specific security training | ESSENTIAL_ENTITY | PERIODIC | 3 | Role training | MEDIUM |
| NIS2-C16 | Art. 21(3) | D-03.1 (Access Control) | Implement access control policies | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Access policies | HIGH |
| NIS2-C17 | Art. 21(3) | D-03.2 (MFA) | Implement multi-factor authentication | ESSENTIAL_ENTITY | CONTINUOUS | 3 | MFA required | HIGH |
| NIS2-C18 | Art. 21(3) | D-01.1 (Encryption) | Implement encryption for data at rest and transit | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Encryption required | HIGH |
| NIS2-C19 | Art. 21(3) | D-03.1 (Identity Management) | Implement identity management systems | ESSENTIAL_ENTITY | CONTINUOUS | 3 | IdM required | HIGH |
| NIS2-C20 | Art. 21(3) | D-03.3 (Least Privilege) | Implement least privilege access | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Least privilege | HIGH |
| NIS2-C21 | Art. 21(3) | D-10.1 (Monitoring) | Implement security monitoring systems | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Monitoring required | HIGH |
| NIS2-C22 | Art. 21(3) | D-10.2 (Logging) | Implement audit logging and traceability | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Audit logging | HIGH |
| NIS2-C23 | Art. 21(3) | D-06.1 (Vendor Management) | Implement vendor risk management | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Vendor risk | HIGH |
| NIS2-C24 | Art. 21(3) | D-06.4 (Third-Party Boundaries) | Define and enforce third-party boundaries | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Boundary management | MEDIUM |
| NIS2-C25 | Art. 23(1) | D-04.3 (Early Warning (24h)) | Notify CSIRT within 24h of significant incident | ESSENTIAL_ENTITY | TRIGGERED | 3 | 24h notification | HIGH |
| NIS2-C26 | Art. 23(2) | D-04.3 (Incident Notification (72h)) | Submit incident notification within 72h | ESSENTIAL_ENTITY | TRIGGERED | 3 | 72h notification | HIGH |
| NIS2-C27 | Art. 23(3) | D-04.3 (Final Report (1 month)) | Submit final report within 1 month | ESSENTIAL_ENTITY | TRIGGERED | 3 | Final report | MEDIUM |
| NIS2-C28 | Art. 21(2)(c) | D-04.1 (Incident Detection) | Implement incident detection systems | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Detection systems | HIGH |
| NIS2-C29 | Art. 21(2)(c) | D-10.1 (Continuous Monitoring) | Implement continuous security monitoring | ESSENTIAL_ENTITY | CONTINUOUS | 3 | Continuous monitoring | HIGH |

---

## 7. DORA Mapping (38 clauses)

| Clause ID | Article | Sub-Domain | Description | obligatedParty | obligationType | NI | Justification | Relevance |
|-----------|---------|------------|-------------|----------------|----------------|---:|---------------|-----------|
| DORA-C01 | Art. 5(1) | D-09.1 (ICT Risk Framework) | Establish comprehensive ICT risk management framework | FINANCIAL_ENTITY | CONTINUOUS | 3 | ICT framework required | HIGH |
| DORA-C02 | Art. 5(2) | D-08.3 (Management Oversight) | Management body defines and oversees ICT risk | FINANCIAL_ENTITY | CONTINUOUS | 3 | Board oversight | HIGH |
| DORA-C03 | Art. 6(1) | D-09.1 (ICT Policies) | Implement ICT security policies | FINANCIAL_ENTITY | CONTINUOUS | 3 | ICT policies | HIGH |
| DORA-C04 | Art. 6(2) | D-09.2 (ICT Risk Assessment) | Conduct ICT risk assessments | FINANCIAL_ENTITY | PERIODIC | 3 | ICT risk assessment | HIGH |
| DORA-C05 | Art. 7(1) | D-09.3 (ICT Asset Inventory) | Maintain inventory of ICT assets | FINANCIAL_ENTITY | CONTINUOUS | 3 | ICT inventory | HIGH |
| DORA-C06 | Art. 8(1) | D-07.4 (Change Management) | Implement ICT change management | FINANCIAL_ENTITY | CONTINUOUS | 3 | Change control | HIGH |
| DORA-C07 | Art. 9(1) | D-10.1 (Continuous Monitoring) | Implement ICT monitoring systems | FINANCIAL_ENTITY | CONTINUOUS | 3 | ICT monitoring | HIGH |
| DORA-C08 | Art. 10(1) | D-02.1 (Vulnerability Management) | Identify and address vulnerabilities | FINANCIAL_ENTITY | CONTINUOUS | 3 | Vuln management | HIGH |
| DORA-C09 | Art. 10(2) | D-01.1 (Encryption) | Implement encryption for data protection | FINANCIAL_ENTITY | CONTINUOUS | 3 | Encryption | HIGH |
| DORA-C10 | Art. 10(3) | D-01.2 (Transit Encryption) | Encrypt data in transit | FINANCIAL_ENTITY | CONTINUOUS | 3 | TLS required | HIGH |
| DORA-C11 | Art. 11(1) | D-03.1 (Access Control) | Implement ICT access controls | FINANCIAL_ENTITY | CONTINUOUS | 3 | Access control | HIGH |
| DORA-C12 | Art. 11(2) | D-10.2 (Audit Logging) | Implement ICT audit trails | FINANCIAL_ENTITY | CONTINUOUS | 3 | Audit trails | HIGH |
| DORA-C13 | Art. 12(1) | D-02.2 (Patch Management) | Apply security patches promptly | FINANCIAL_ENTITY | TRIGGERED | 3 | Patch management | HIGH |
| DORA-C14 | Art. 13(1) | D-03.3 (Least Privilege) | Implement least privilege access | FINANCIAL_ENTITY | CONTINUOUS | 3 | Least privilege | HIGH |
| DORA-C15 | Art. 14(1) | D-03.1 (Identity Management) | Implement identity management | FINANCIAL_ENTITY | CONTINUOUS | 3 | IdM required | HIGH |
| DORA-C16 | Art. 15(1) | D-03.2 (MFA) | Implement multi-factor authentication | FINANCIAL_ENTITY | CONTINUOUS | 3 | MFA required | HIGH |
| DORA-C17 | Art. 16(1) | D-01.3 (Key Management) | Implement cryptographic key management | FINANCIAL_ENTITY | CONTINUOUS | 3 | Key mgmt | HIGH |
| DORA-C18 | Art. 17(1) | D-04.1 (Incident Detection) | Detect ICT-related incidents | FINANCIAL_ENTITY | CONTINUOUS | 3 | Incident detection | HIGH |
| DORA-C19 | Art. 17(2) | D-04.2 (Incident Response) | Respond to ICT incidents | FINANCIAL_ENTITY | TRIGGERED | 3 | Incident response | HIGH |
| DORA-C20 | Art. 18(1) | D-07.3 (CI/CD Security) | Secure development pipelines | FINANCIAL_ENTITY | CONTINUOUS | 3 | Pipeline security | HIGH |
| DORA-C21 | Art. 19(1) | D-04.1 (Incident Triage) | Triage and classify ICT incidents | FINANCIAL_ENTITY | TRIGGERED | 3 | Incident triage | HIGH |
| DORA-C22 | Art. 20(1) | D-04.2 (Containment) | Contain ICT incident impact | FINANCIAL_ENTITY | TRIGGERED | 3 | Containment | HIGH |
| DORA-C23 | Art. 21(1) | D-04.4 (Recovery Procedures) | Implement ICT recovery procedures | FINANCIAL_ENTITY | CONTINUOUS | 3 | Recovery procedures | HIGH |
| DORA-C24 | Art. 22(1) | D-04.2 (Business Continuity) | Implement ICT business continuity | FINANCIAL_ENTITY | CONTINUOUS | 3 | ICT BCP | HIGH |
| DORA-C25 | Art. 23(1) | D-04.4 (Backup Systems) | Implement backup and restore | FINANCIAL_ENTITY | CONTINUOUS | 3 | Backup systems | HIGH |
| DORA-C26 | Art. 24(1) | D-10.3 (Resilience Testing) | Test ICT operational resilience | FINANCIAL_ENTITY | PERIODIC | 3 | Resilience testing | HIGH |
| DORA-C27 | Art. 25(1) | D-02.4 (Vulnerability Scanning) | Conduct vulnerability scans | FINANCIAL_ENTITY | PERIODIC | 3 | Vuln scanning | HIGH |
| DORA-C28 | Art. 26(1) | D-10.3 (Penetration Testing) | Conduct penetration tests | FINANCIAL_ENTITY | PERIODIC | 3 | Pen testing | HIGH |
| DORA-C29 | Art. 27(1) | D-02.4 (Threat-Led Pen Testing) | Conduct TLPT every 3 years | FINANCIAL_ENTITY | PERIODIC | 3 | TLPT required | HIGH |
| DORA-C30 | Art. 28(1) | D-06.1 (Third-Party Risk) | Assess ICT third-party risk | FINANCIAL_ENTITY | CONTINUOUS | 3 | Third-party risk | HIGH |
| DORA-C31 | Art. 29(1) | D-06.3 (Contractual Safeguards) | Include ICT safeguards in contracts | FINANCIAL_ENTITY | ONE_TIME | 3 | Contract safeguards | HIGH |
| DORA-C32 | Art. 30(1) | D-06.1 (Vendor Due Diligence) | Conduct ICT vendor due diligence | FINANCIAL_ENTITY | ONE_TIME | 3 | Vendor DD | HIGH |
| DORA-C33 | Art. 31(1) | D-06.4 (Exit Strategies) | Define ICT third-party exit strategies | FINANCIAL_ENTITY | ONE_TIME | 3 | Exit strategies | HIGH |
| DORA-C34 | Art. 32(1) | D-06.4 (Concentration Risk) | Monitor ICT third-party concentration | FINANCIAL_ENTITY | CONTINUOUS | 3 | Concentration risk | HIGH |
| DORA-C35 | Art. 17(3) | D-04.3 (Incident Reporting (24h)) | Notify authority within 24h | FINANCIAL_ENTITY | TRIGGERED | 3 | 24h reporting | HIGH |
| DORA-C36 | Art. 17(4) | D-04.3 (Incident Report (72h)) | Submit incident report within 72h | FINANCIAL_ENTITY | TRIGGERED | 3 | 72h report | HIGH |
| DORA-C37 | Art. 17(5) | D-04.3 (Final Report (1 month)) | Submit final incident report | FINANCIAL_ENTITY | TRIGGERED | 3 | Final report | MEDIUM |
| DORA-C38 | Art. 33(1) | D-09.4 (Record Keeping) | Maintain ICT risk records | FINANCIAL_ENTITY | CONTINUOUS | 3 | ICT records | HIGH |

---

## 8. AI Act Mapping (29 clauses)

| Clause ID | Article | Sub-Domain | Description | obligatedParty | obligationType | NI | Justification | Relevance |
|-----------|---------|------------|-------------|----------------|----------------|---:|---------------|-----------|
| AI-C01 | Art. 9(1) | D-09.2 (Risk Management System) | Establish AI risk management system | PROVIDER | CONTINUOUS | 3 | Risk management required | HIGH |
| AI-C02 | Art. 9(2) | D-09.2 (Risk Assessment) | Conduct AI-specific risk assessments | PROVIDER | PERIODIC | 3 | AI risk assessment | HIGH |
| AI-C03 | Art. 10(1) | D-02.1 (Data Governance) | Ensure quality of training data | PROVIDER | CONTINUOUS | 3 | Data quality | HIGH |
| AI-C04 | Art. 10(2) | D-02.4 (Data Testing) | Test data for biases and errors | PROVIDER | PERIODIC | 3 | Bias testing | MEDIUM |
| AI-C05 | Art. 10(3) | D-05.1 (Data Relevance) | Ensure training data is relevant for intended purpose | PROVIDER | ONE_TIME | 3 | Data relevance | HIGH |
| AI-C06 | Art. 10(4) | D-05.1 (Data Representativeness) | Ensure training data is representative | PROVIDER | ONE_TIME | 3 | Representativeness | HIGH |
| AI-C07 | Art. 10(5) | D-05.2 (Data Retention) | Retain training data for AI lifecycle | PROVIDER | CONTINUOUS | 3 | Data retention | MEDIUM |
| AI-C08 | Art. 11(1) | D-09.1 (Technical Documentation) | Maintain AI technical documentation | PROVIDER | CONTINUOUS | 3 | Documentation required | HIGH |
| AI-C09 | Art. 12(1) | D-10.2 (Automatic Logging) | Implement automatic AI activity logging | PROVIDER | CONTINUOUS | 3 | AI logging | HIGH |
| AI-C10 | Art. 12(2) | D-10.2 (Log Retention) | Retain AI logs for 6 months minimum | PROVIDER | CONTINUOUS | 3 | 6-month retention | HIGH |
| AI-C11 | Art. 12(3) | D-09.4 (Traceability) | Ensure AI decision traceability | PROVIDER | CONTINUOUS | 3 | Traceability | HIGH |
| AI-C12 | Art. 13(1) | D-09.1 (Transparency Information) | Provide transparency information to users | PROVIDER | ONE_TIME | 3 | User transparency | HIGH |
| AI-C13 | Art. 13(2) | D-09.1 (Instructions for Use) | Provide clear AI usage instructions | PROVIDER | ONE_TIME | 3 | Usage instructions | MEDIUM |
| AI-C14 | Art. 14(1) | D-08.2 (Human Oversight) | Design AI for effective human oversight | PROVIDER | ONE_TIME | 3 | Oversight by design | HIGH |
| AI-C15 | Art. 14(2) | D-03.1 (Oversight Competence) | Ensure human overseers are competent | PROVIDER | CONTINUOUS | 3 | Competent overseers | HIGH |
| AI-C16 | Art. 15(1) | D-02.1 (Accuracy Performance) | Achieve appropriate accuracy levels | PROVIDER | CONTINUOUS | 3 | Accuracy required | HIGH |
| AI-C17 | Art. 15(2) | D-01.1 (Cybersecurity) | Implement AI cybersecurity measures | PROVIDER | CONTINUOUS | 3 | AI security | HIGH |
| AI-C18 | Art. 15(3) | D-01.4 (Resilience) | Ensure AI system resilience against attacks | PROVIDER | CONTINUOUS | 3 | Resilience required | HIGH |
| AI-C19 | Art. 15(4) | D-10.1 (Fallback Plans) | Implement AI fallback plans | PROVIDER | ONE_TIME | 3 | Fallback required | MEDIUM |
| AI-C20 | Art. 16(a) | D-09.1 (Conformity Assessment) | Undergo AI conformity assessment before market | PROVIDER | ONE_TIME | 3 | Conformity required | HIGH |
| AI-C21 | Art. 16(b) | D-10.3 (Post-Market Monitoring) | Establish post-market monitoring system | PROVIDER | CONTINUOUS | 3 | Monitoring required | HIGH |
| AI-C22 | Art. 16(c) | D-09.2 (Incident Reporting) | Report AI incidents to authorities | PROVIDER | TRIGGERED | 3 | Incident reporting | HIGH |
| AI-C23 | Art. 17 | D-09.1 (Quality Management) | Implement AI quality management system | PROVIDER | CONTINUOUS | 3 | QMS required | HIGH |
| AI-C24 | Art. 18 | D-08.2 (Staff Competence) | Ensure AI staff have appropriate competence | PROVIDER | CONTINUOUS | 3 | Staff competence | MEDIUM |
| AI-C25 | Art. 19 | D-10.1 (Monitoring Systems) | Implement AI monitoring systems | PROVIDER | CONTINUOUS | 3 | Monitoring systems | HIGH |
| AI-C26 | Art. 20 | D-04.3 (Market Surveillance) | Cooperate with market surveillance authorities | PROVIDER | CONTINUOUS | 3 | Cooperation required | MEDIUM |
| AI-C27 | Art. 21 | D-10.3 (Periodic Evaluation) | Conduct periodic AI system evaluations | PROVIDER | PERIODIC | 3 | Periodic evaluation | MEDIUM |
| AI-C28 | Art. 22 | D-09.2 (Fundamental Rights Impact) | Assess fundamental rights impact | PROVIDER | ONE_TIME | 3 | FRIA required | HIGH |
| AI-C29 | Art. 23 | D-04.3 (Database Registration) | Register high-risk AI in EU database | PROVIDER | ONE_TIME | 3 | Registration required | MEDIUM |

---

## 9. Per-Regulation Clause ID Shim Table

This section provides the canonical clause ID mapping between the **case-form** (e.g., `GDPR-C01`) used in this document and the **corpus-form** used in `00_METHODOLOGY/PREPROCESSING_by_domain/` (e.g., `GDPR-CLxx` / `GDPR-CPxx` / `GDPR-RTxx`). The case-form is preserved verbatim for Case_03 traceability; the corpus-form is provided as a parallel reference for Sprint 2 corpus enrichment.

**Important:** The numeric suffix does NOT directly correspond between forms. The corpus uses semantic groupings (CL = clause proper, CP = principle, RT = recital/threshold), while the case uses sequential numbering.

| Case Form | Corpus Form | Regulation | Sub-Domain | Note |
|-----------|-------------|------------|------------|------|
| GDPR-C01 | GDPR-CL01 | GDPR | D-05.1 | GDPR-CL = core clause, GDPR-CP = principle, GDPR-RT = recital/threshold |
| GDPR-C02 | GDPR-CL02 | GDPR | D-05.2 | GDPR-CL = core clause, GDPR-CP = principle, GDPR-RT = recital/threshold |
| GDPR-C03 | GDPR-CL03 | GDPR | D-05.2 | GDPR-CL = core clause, GDPR-CP = principle, GDPR-RT = recital/threshold |
| CRA-C01 | CRA-CL01 | CRA | D-02.1 | CRA-CL = core clause; Annex I Part I/II clauses use Article references in corpus |
| CRA-C02 | CRA-CL02 | CRA | D-07.1 | CRA-CL = core clause; Annex I Part I/II clauses use Article references in corpus |
| CRA-C03 | CRA-CL03 | CRA | D-03.4 | CRA-CL = core clause; Annex I Part I/II clauses use Article references in corpus |
| NIS2-C01 | NIS2-CL01 | NIS2 | D-09.1 | NIS2-CL = core clause (Art. 21, Art. 23); sub-clauses by paragraph |
| NIS2-C02 | NIS2-CL02 | NIS2 | D-08.3 | NIS2-CL = core clause (Art. 21, Art. 23); sub-clauses by paragraph |
| NIS2-C03 | NIS2-CL03 | NIS2 | D-09.1 | NIS2-CL = core clause (Art. 21, Art. 23); sub-clauses by paragraph |
| DORA-C01 | DORA-CL01 | DORA | D-09.1 | DORA-CL = core clause (Art. 5-44); bare `CLx-y` in corpus (disambiguate by parent regulation) |
| DORA-C02 | DORA-CL02 | DORA | D-08.3 | DORA-CL = core clause (Art. 5-44); bare `CLx-y` in corpus (disambiguate by parent regulation) |
| DORA-C03 | DORA-CL03 | DORA | D-09.1 | DORA-CL = core clause (Art. 5-44); bare `CLx-y` in corpus (disambiguate by parent regulation) |
| AI-C01 | AIA-CL01 | AI Act | D-09.2 | AIA-CL = core clause (Art. 9-15, 16, 22, 73); AI Act uses bare CL in corpus |
| AI-C02 | AIA-CL02 | AI Act | D-09.2 | AIA-CL = core clause (Art. 9-15, 16, 22, 73); AI Act uses bare CL in corpus |
| AI-C03 | AIA-CL03 | AI Act | D-02.1 | AIA-CL = core clause (Art. 9-15, 16, 22, 73); AI Act uses bare CL in corpus |

**Full shim table for all 150 clauses** is in `phase1_ontology.yaml` (corpus-form cross-references added Sprint 2).

---

## 10. DORA + AI Act Cross-References (from Doc 06b)

Per Sprint 0.6 Doc 06b (`Doc11_DORA_ICT_Risk_Framework.md`), the following DORA articles and AI Act articles receive **deeper coverage** beyond the baseline mapping in §7/§8 above:

### 10.1 DORA — Articles with enhanced coverage

| Article | Sub-Domain | Coverage Tier | Doc 06b Reference |
|---------|------------|---------------|-------------------|
| Art. 5(1) ICT Risk Framework | D-09.1 | RIGOROUS | Doc 06b §3.1 |
| Art. 5(2) Management Oversight | D-08.3 | RIGOROUS | Doc 06b §3.1 (board liability) |
| Art. 6 ICT Policies | D-09.1 | RIGOROUS | Doc 06b §3.2 |
| Art. 7 ICT Risk Identification | D-09.2 | RIGOROUS | Doc 06b §3.3 |
| Art. 8 ICT Asset Inventory | D-09.3 | RIGOROUS | Doc 06b §3.4 |
| Art. 9 ICT Protection (encryption) | D-01.1, D-01.2 | RIGOROUS | Doc 06b §3.5 |
| Art. 11 ICT Access Control | D-03.1 | RIGOROUS | Doc 06b §3.6 |
| Art. 17-19 ICT Incident Reporting | D-04.1, D-04.3 | RIGOROUS | Doc 06b §3.7 (RTS deadlines) |
| Art. 24-27 Resilience Testing (incl. TLPT) | D-02.4, D-10.3 | RIGOROUS | Doc 06b §3.8 (significance posture) |
| Art. 28-30 CTPP Register | D-06.1, D-06.3 | RIGOROUS | Doc 06b §3.9 (DORA Art. 28-30) |

### 10.2 AI Act — Articles with enhanced coverage (OmniScore AI high-risk)

| Article | Sub-Domain | Coverage Tier | Notes |
|---------|------------|---------------|-------|
| Art. 9 Risk Management System | D-09.2 | RIGOROUS | AI risk mgmt framework |
| Art. 10 Data Governance | D-05.1, D-02.1 | RIGOROUS | Training data quality |
| Art. 11 Technical Documentation | D-09.1 | RIGOROUS | Annex IV documentation |
| Art. 13 Transparency | D-09.1 | RIGOROUS | Provider info to deployers |
| Art. 14 Human Oversight | D-08.2 | RIGOROUS | Human-in-the-loop for credit scoring |
| Art. 15 Accuracy/Robustness/Cybersecurity | D-01.1, D-02.1, D-10.1 | RIGOROUS | 5 sub-paragraphs |
| Art. 16 Provider Obligations | D-09.1 | RIGOROUS | Quality mgmt system |
| Art. 22 FRIA | D-09.2 | RIGOROUS | Fundamental Rights Impact Assessment |
| Art. 43 Conformity Assessment | D-10.3 | RIGOROUS | Notified body for high-risk |
| Art. 73 Serious Incident Reporting | D-04.3 | RIGOROUS | 3-tier (15d/2d/10d) |

---

## 11. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2026-08-06 | Sprint 0 Executor | Initial placeholder (lint baseline gap) |
| 1.0 | 2026-08-06 | Sprint 1 Executor | Generated Markdown companion from xlsx; 150 clauses; per-regulation sections; clause ID shim table; DORA + AI Act cross-references |

---

## 12. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Sprint 1 Executor | | 2026-08-06 |
| Compliance Review (CRO) | | | |
| AEGIS Methodology Review | | | |

**Companion xlsx:** `../01_PHASE1_CONTEXT_RICH/06_Clause_Mapping_Matrix.xlsx` (source of truth)
**Next Document:** `Doc12_Structured_Compliance_Matrix.md`
**Phase 1 Gate Status:** ✅ READY for Sprint 2 (corpus enrichment)
