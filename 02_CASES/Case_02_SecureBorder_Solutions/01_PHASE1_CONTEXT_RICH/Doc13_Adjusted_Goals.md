---
document_id: AEGIS-P2-RICH-07c-ADJ
title: Adjusted Goals per Sub-Domain (Rich Mode)
phase: 1
version: 3.0
created: 2026-08-06
updated: 2026-08-28
author: Sprint 4 Executor (adjusted-objectives-builder); Sprint 5 Executor (DEEP enrichment); Port Fase 1 (corr-008 AG- migration)
status: DEEP_ENRICHED
status_history:
  - { date: 2026-08-06, status: DRAFT, sprint: 0, by: 'Sprint 0 skeleton' }
  - { date: 2026-08-06, status: RECONCILED, sprint: 1, by: 'Sprint 1 reconciliation' }
  - { date: 2026-08-06, status: CORPUS_ENRICHED, sprint: 2, by: 'Sprint 2 corpus enrichment' }
  - { date: 2026-08-06, status: ADJUSTED_OBJECTIVES, sprint: 4, by: 'Sprint 4 adjusted objectives' }
  - { date: 2026-08-06, status: DEEP_ENRICHED, sprint: 5, by: 'Sprint 5 DEEP enrichment' }
  - { date: 2026-08-28, status: AG_MIGRATED, by: 'Port Fase 1 (corr-008): PG-/SG- → AG-D-XX.Y-001/-002; renamed Adjusted_Goals per corr-010' }
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 35
inactive_subdomains: [D-07.4, D-08.3, D-09.3]
id_format: AG-D-XX.Y-NNN (canonical Phase 1 per corr-008; privacy set -001, security set -002; legacy PG-/SG- aliases in Appendix A)
detail_cards: 70
tensions_expanded: 3
fields_excluded: [Effort Estimate, Cost Estimate, Target Timeline]
cross_checked_against: [Doc12_Proportionality_Profile.md, proportionality_model.md]
---

# Adjusted Goals per Sub-Domain (Rich Mode)

> Phase 1 adjusted goals — generic baseline + company-tailored AG sets (privacy `-001` / security `-002`) + Track B tier + tensions resolved.
> 35 active sub-domains × (1 privacy + 1 security goal) = 70 adjusted goals + 3 resolved tensions + 35 Track B decision rows.
>
> **corr-008 AG- migration (v3.0, 2026-08-28, port Fase 1):** all legacy `PG-D-XX.Y` / `SG-D-XX.Y` goal IDs migrated to the canonical `AG-D-XX.Y-NNN` format (PG → `-001`, SG → `-002`). Legacy aliases preserved in Appendix A. This closes the corr-007/008 prefix violation flagged by `../01_PHASE1_CONTEXT_RICH/validation/P1_cross_case_mirror_v0.md` and aligns the filename with corr-010 (`Adjusted_Goals`).

## §1 Generic Baseline (preserved from corpus)

The table below preserves the corpus-extracted **High-Level Security Objective (HSO)** and **per-regulation Sub-Objective (Sub-SO)** identifiers for each active sub-domain. Each Sub-SO ID points to the corpus file at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`. The full Sub-SO objective text is preserved verbatim in the corpus source.

| Sub-Domain | HSO | GDPR Sub-SO | CRA Sub-SO | NIS 2 Sub-SO | AI_Act Sub-SO | Corpus Path |
|------------|-----|-------------|------------|--------------|---------------|-------------|
| D-01.1 (Data at Rest Encryption) | `SO-D-01.1.HL` | `SO-D-01.1.GDPR` | `SO-D-01.1.CRA` | `SO-D-01.1.NIS2` | `—` | `domains/D-01_Data-Protection/D-01.1/D-01.1.json` |
| D-01.2 (Data in Transit Encryption) | `SO-D-01.2.HL` | `SO-D-01.2.GDPR` | `SO-D-01.2.CRA` | `—` | `—` | `domains/D-01_Data-Protection/D-01.2/D-01.2.json` |
| D-01.3 (Cryptographic Key Management) | `SO-D-01.3.HL` | `SO-D-01.3.GDPR` | `SO-D-01.3.CRA` | `—` | `—` | `domains/D-01_Data-Protection/D-01.3/D-01.3.json` |
| D-01.4 (Data Integrity Mechanisms) | `SO-D-01.4.HL` | `SO-D-01.4.GDPR` | `SO-D-01.4.CRA` | `—` | `SO-D-01.4.AI_Act` | `domains/D-01_Data-Protection/D-01.4/D-01.4.json` |
| D-02.1 (Vulnerability Identification) | `SO-D-02.1.HL` | `SO-D-02.1.GDPR` | `SO-D-02.1.CRA` | `SO-D-02.1.NIS2` | `SO-D-02.1.AI_Act` | `domains/D-02_Vulnerability-Management/D-02.1/D-02.1.json` |
| D-02.2 (Patch Management & Updates) | `SO-D-02.2.HL` | `—` | `SO-D-02.2.CRA` | `—` | `—` | `domains/D-02_Vulnerability-Management/D-02.2/D-02.2.json` |
| D-02.3 (Coordinated Vulnerability Disclosure) | `SO-D-02.3.HL` | `—` | `SO-D-02.3.CRA` | `SO-D-02.3.NIS2` | `—` | `domains/D-02_Vulnerability-Management/D-02.3/D-02.3.json` |
| D-02.4 (Threat-Led Penetration Testing) | `SO-D-02.4.HL` | `—` | `SO-D-02.4.CRA` | `—` | `SO-D-02.4.AI_Act` | `domains/D-02_Vulnerability-Management/D-02.4/D-02.4.json` |
| D-03.1 (Identity Lifecycle Management) | `SO-D-03.1.HL` | `SO-D-03.1.GDPR` | `SO-D-03.1.CRA` | `SO-D-03.1.NIS2` | `—` | `domains/D-03_Access-Control/D-03.1/D-03.1.json` |
| D-03.2 (Multi-Factor Authentication) | `SO-D-03.2.HL` | `SO-D-03.2.GDPR` | `SO-D-03.2.CRA` | `SO-D-03.2.NIS2` | `—` | `domains/D-03_Access-Control/D-03.2/D-03.2.json` |
| D-03.3 (Authorisation & Least Privilege) | `SO-D-03.3.HL` | `SO-D-03.3.GDPR` | `SO-D-03.3.CRA` | `SO-D-03.3.NIS2` | `—` | `domains/D-03_Access-Control/D-03.3/D-03.3.json` |
| D-03.4 (Secure System Defaults) | `SO-D-03.4.HL` | `SO-D-03.4.GDPR` | `SO-D-03.4.CRA` | `—` | `—` | `domains/D-03_Access-Control/D-03.4/D-03.4.json` |
| D-04.1 (Incident Detection & Triage) | `SO-D-04.1.HL` | `SO-D-04.1.GDPR` | `SO-D-04.1.CRA` | `SO-D-04.1.NIS2` | `—` | `domains/D-04_Incident-Response/D-04.1/D-04.1.json` |
| D-04.2 (Incident Containment & Response) | `SO-D-04.2.HL` | `SO-D-04.2.GDPR` | `SO-D-04.2.CRA` | `SO-D-04.2.NIS2` | `—` | `domains/D-04_Incident-Response/D-04.2/D-04.2.json` |
| D-04.3 (Incident Notification & Reporting) | `SO-D-04.3.HL` | `SO-D-04.3.GDPR` | `SO-D-04.3.CRA` | `SO-D-04.3.NIS2` | `SO-D-04.3.AI_Act` | `domains/D-04_Incident-Response/D-04.3/D-04.3.json` |
| D-04.4 (Incident Recovery & Lessons Learned) | `SO-D-04.4.HL` | `SO-D-04.4.GDPR` | `SO-D-04.4.CRA` | `SO-D-04.4.NIS2` | `—` | `domains/D-04_Incident-Response/D-04.4/D-04.4.json` |
| D-05.1 (Data Minimisation) | `SO-D-05.1.HL` | `SO-D-05.1.GDPR` | `SO-D-05.1.CRA` | `—` | `SO-D-05.1.AIACT` | `domains/D-05_Data-Lifecycle/D-05.1/D-05.1.json` |
| D-05.2 (Retention & Archiving) | `SO-D-05.2.HL` | `SO-D-05.2.GDPR` | `SO-D-05.2.CRA` | `—` | `SO-D-05.2.AIACT` | `domains/D-05_Data-Lifecycle/D-05.2/D-05.2.json` |
| D-05.3 (Right to Erasure) | `SO-D-05.3.HL` | `SO-D-05.3.GDPR` | `SO-D-05.3.CRA` | `—` | `—` | `domains/D-05_Data-Lifecycle/D-05.3/D-05.3.json` |
| D-05.4 (Data Portability) | `SO-D-05.4.HL` | `SO-D-05.4.GDPR` | `—` | `—` | `—` | `domains/D-05_Data-Lifecycle/D-05.4/D-05.4.json` |
| D-06.1 (Vendor Risk Assessment) | `SO-D-06.1.HL` | `SO-D-06.1.GDPR` | `SO-D-06.1.CRA` | `SO-D-06.1.NIS2` | `—` | `domains/D-06_Supply-Chain/D-06.1/D-06.1.json` |
| D-06.2 (Software Bill of Materials (software bill of materials)) | `SO-D-06.2.HL` | `—` | `SO-D-06.2.CRA` | `—` | `—` | `domains/D-06_Supply-Chain/D-06.2/D-06.2.json` |
| D-06.3 (Contractual Security Obligations) | `SO-D-06.3.HL` | `SO-D-06.3.GDPR` | `SO-D-06.3.CRA` | `SO-D-06.3.NIS2` | `—` | `domains/D-06_Supply-Chain/D-06.3/D-06.3.json` |
| D-06.4 (Third-Party Boundary Management) | `SO-D-06.4.HL` | `SO-D-06.4.GDPR` | `SO-D-06.4.CRA` | `SO-D-06.4.NIS2` | `—` | `domains/D-06_Supply-Chain/D-06.4/D-06.4.json` |
| D-07.1 (Secure-by-Design Principles) | `SO-D-07.1.HL` | `SO-D-07.1.GDPR` | `SO-D-07.1.CRA` | `SO-D-07.1.NIS2` | `SO-D-07.1.AIACT` | `domains/D-07_Secure-Development/D-07.1/D-07.1.json` |
| D-07.2 (Secure Coding Practices) | `SO-D-07.2.HL` | `—` | `SO-D-07.2.CRA` | `—` | `SO-D-07.2.AIACT` | `domains/D-07_Secure-Development/D-07.2/D-07.2.json` |
| D-07.3 (CI/CD Pipeline Security) | `SO-D-07.3.HL` | `—` | `SO-D-07.3.CRA` | `SO-D-07.3.NIS2` | `—` | `domains/D-07_Secure-Development/D-07.3/D-07.3.json` |
| D-08.1 (General Security Awareness) | `SO-D-08.1.HL` | `SO-D-08.1.GDPR` | `SO-D-08.1.CRA` | `SO-D-08.1.NIS2` | `—` | `domains/D-08_Human-Factors/D-08.1/D-08.1.json` |
| D-08.2 (Role-Specific Competence) | `SO-D-08.2.HL` | `SO-D-08.2.GDPR` | `SO-D-08.2.CRA` | `SO-D-08.2.NIS2` | `SO-D-08.2.AIACT` | `domains/D-08_Human-Factors/D-08.2/D-08.2.json` |
| D-09.1 (Information Security Policies) | `SO-D-09.1.HL` | `SO-D-09.1.GDPR` | `SO-D-09.1.CRA` | `SO-D-09.1.NIS2` | `SO-D-09.1.AI_Act` | `domains/D-09_Governance-Documentation/D-09.1/D-09.1.json` |
| D-09.2 (Impact & Risk Assessments) | `SO-D-09.2.HL` | `SO-D-09.2.GDPR` | `SO-D-09.2.CRA` | `SO-D-09.2.NIS2` | `SO-D-09.2.AI_Act` | `domains/D-09_Governance-Documentation/D-09.2/D-09.2.json` |
| D-09.4 (Records of Processing) | `SO-D-09.4.HL` | `SO-D-09.4.GDPR` | `SO-D-09.4.CRA` | `SO-D-09.4.NIS2` | `SO-D-09.4.AI_Act` | `domains/D-09_Governance-Documentation/D-09.4/D-09.4.json` |
| D-10.1 (Continuous Security Monitoring) | `SO-D-10.1.HL` | `SO-D-10.1.GDPR` | `SO-D-10.1.CRA` | `SO-D-10.1.NIS2` | `SO-D-10.1.AI_Act` | `domains/D-10_Monitoring-Audit/D-10.1/D-10.1.json` |
| D-10.2 (Audit Logging & Traceability) | `SO-D-10.2.HL` | `SO-D-10.2.GDPR` | `SO-D-10.2.CRA` | `—` | `SO-D-10.2.AI_Act` | `domains/D-10_Monitoring-Audit/D-10.2/D-10.2.json` |
| D-10.3 (Compliance Testing) | `SO-D-10.3.HL` | `SO-D-10.3.GDPR` | `SO-D-10.3.CRA` | `SO-D-10.3.NIS2` | `SO-D-10.3.AI_Act` | `domains/D-10_Monitoring-Audit/D-10.3/D-10.3.json` |

**Total rows:** 35 (35 active sub-domains).

## §2 Adjusted Privacy Goals (PG) per Sub-Domain

Adjusted Privacy Goals are Case_02-specific restatements of the corpus generic GDPR Sub-SO. For sub-domains without a GDPR participant (e.g., D-06.2 software bill of materials, D-07.2 secure coding), the PG row is marked `N/A` because no GDPR privacy objective applies — the corresponding security obligation is captured in §3 (Adjusted Security Goals) under the regulating framework.

**Tier source:** Doc 07b §3 (RIGOROUS for the 8 critical sub-domains; STANDARD for the remaining 27). **Priority:** MUST for all 35 active sub-domains per Doc 07b §3 (no SHOULD/COULD rows exist; all sub-domains are `priority=MUST` corpus-wide).

| Sub-Domain | Generic GDPR Sub-SO | Adjusted PG (Case_02-specific) | Tier | Priority | Details | | NIST Anchors | | NIST Anchors |
|------------|---------------------|---------------------------------|------|----------|---------| | --- | | --- |
| D-01.1 (Data at Rest Encryption) | `SO-D-01.1.GDPR` | All biometric reference datas and watchlist data at rest in eGate kiosks are protected by hardware cryptographic module-backed industry-standard authenticated encryption encryption with classified-key cipher strength, dedicated key-rotation policy (quarterly), cryptographic sharding separating biometric↔identity mapping, cryptographic module certified to applicable assurance level Level 3 hardware cryptographic module, and tamper-evident key-lineage logging — meeting GDPR Art. 9 (special category biometric) + Art. 32 risk-anchored floor + CRA state-of-the-art baseline on a single artefact. | RIGOROUS | MUST | [AG-D-01.1-001](#ag-d-d01-1-001) | | — | | — |
| D-01.2 (Data in Transit Encryption) | `SO-D-01.2.GDPR` | All biometric and watchlist data in transit across kiosk↔cloud and kiosk↔government links is protected by modern transport security with mutual transport authentication on internal on-device↔backend, hardware cryptographic module-signed certificates, cipher suite allowlist (no RC4/3DES), and a documented transit-encryption policy anchored to GDPR Art. 32(1)(a)/(b). | STANDARD | MUST | [AG-D-01.2-001](#ag-d-d01-2-001) | | — | | — |
| D-01.3 (Cryptographic Key Management) | `SO-D-01.3.GDPR` | Cryptographic key custody for biometric reference datas uses an hardware cryptographic module-anchored architecture with classified-key cipher strength per Art. 9 biometric sensitivity, key-lineage logging to tamper-evident audit log, functional-role-based access control separation (key-material custodian vs operational-environment custodian as distinct roles with distinct credentials), separation of biometric key material from non-biometric key material, and a documented de-attribution test procedure — meeting GDPR's Art. 4(5) pseudonymisation test on a single artefact. | RIGOROUS | MUST | [AG-D-01.3-001](#ag-d-d01-3-001) | | — | | — |
| D-01.4 (Data Integrity Mechanisms) | `SO-D-01.4.GDPR` | Data integrity of biometric + watchlist records is protected by cryptographic integrity check-SHA256 on all biometric data, DB constraints + signed audit log, checksum validation on data restore, and GDPR Art. 5(1)(f) integrity principle documentation in the DPIA. | STANDARD | MUST | [AG-D-01.4-001](#ag-d-d01-4-001) | | — | | — |
| D-02.1 (Vulnerability Identification) | `SO-D-02.1.GDPR` | Personal-data-impacting vulnerabilities identified by dependency vulnerability scanner + npm audit in CI, OSS advisories feed, and a monthly vulnerability review board with CISO + CTO participation; vulnerability findings link to the DPIA risk register per GDPR Art. 35. | STANDARD | MUST | [AG-D-02.1-001](#ag-d-d02-1-001) | | — | | — |
| D-02.2 (Patch Management & Updates) | — | N/A — non-privacy sub-domain (CRA-only product-level patching). Personal data integrity protected by the integrity sub-domain (D-01.4) and the patch cadence satisfies GDPR Art. 32(1)(d) `regular testing` as a side-effect of CRA Art. 13(8) vulnerability handling. | STANDARD | MUST | [AG-D-02.2-001](#ag-d-d02-2-001) | | — | | — |
| D-02.3 (Coordinated Vulnerability Disclosure) | — | N/A — non-privacy sub-domain (CRA + NIS 2 product/entity-level CVD). Personal-data-impacting vulnerabilities reach the controller via the processor→controller breach notification chain (D-04.3) within GDPR's 72h clock. | STANDARD | MUST | [AG-D-02.3-001](#ag-d-d02-3-001) | | — | | — |
| D-02.4 (Threat-Led Penetration Testing) | — | N/A — non-privacy sub-domain (CRA + AI_Act + NIS 2 threat-led testing). Personal-data exposure from pen-test artefacts is governed by the controller's data-handling policy (D-04.4) and the test-environment segregation. | STANDARD | MUST | [AG-D-02.4-001](#ag-d-d02-4-001) | | — | | — |
| D-03.1 (Identity Lifecycle Management) | `SO-D-03.1.GDPR` | Personal-data access identity lifecycle managed by a dedicated IAM (dedicated identity governance platform/dedicated identity provider — native, NOT Firebase INHERIT) with provisioning protocol provisioning, quarterly access reviews covering biometric-data scopes (NIS 2 Art. 21(2)(i) workforce-side joiner-mover-leaver), and DPO oversight on biometric scope authorisations per GDPR Art. 30 controller capacity. | STANDARD | MUST | [AG-D-03.1-001](#ag-d-d03-1-001) | | — | | — |
| D-03.2 (Multi-Factor Authentication) | `SO-D-03.2.GDPR` | Personal-data access (including biometric-data scopes) requires phishing-resistant multi-factor authentication (hardware-backed second-factor authenticator/hardware-backed second-factor authenticator) for kiosk admin access; SMS+time-based one-time password fallback for read-only scopes; Art. 32(1) appropriate-and-proportionate multi-factor authentication aligned to biometric data sensitivity. | STANDARD | MUST | [AG-D-03.2-001](#ag-d-d03-2-001) | | — | | — |
| D-03.3 (Authorisation & Least Privilege) | `SO-D-03.3.GDPR` | Personal-data access (biometric scope) is governed by role-based access control with least-privilege for kiosk operators + attribute-based access control for biometric-data access (purpose-bound) + segregation of duties (operator vs auditor); documented per GDPR Art. 5(1)(c) data minimisation principle. | STANDARD | MUST | [AG-D-03.3-001](#ag-d-d03-3-001) | | — | | — |
| D-03.4 (Secure System Defaults) | `SO-D-03.4.GDPR` | N/A — non-privacy sub-domain (CRA secure-by-default). Personal-data exposure from insecure defaults is mitigated by the secure-defaults control itself (debug ports disabled, default passwords rotated, signed firmware required) — discharges GDPR Art. 25(2) privacy by default on the same artefact. | STANDARD | MUST | [AG-D-03.4-001](#ag-d-d03-4-001) | | — | | — |
| D-04.1 (Incident Detection & Triage) | `SO-D-04.1.GDPR` | Personal-data breach detection via 24/7 SOC + Security Information and Event Management + AI-driven anomaly detection on on-device pipeline; playbooks per scenario including biometric-data breach (CRA Art. 14(3) severe incident); GDPR Art. 32(1)(d) `regular testing` of detection capability. | STANDARD | MUST | [AG-D-04.1-001](#ag-d-d04-1-001) | | — | | — |
| D-04.2 (Incident Containment & Response) | `SO-D-04.2.GDPR` | Personal-data breach containment via documented documented incident response procedure (GDPR Art. 32 processor-side), chain-of-custody evidence pack, CSIRT coordination procedure; Art. 32(1)(c) `restore in timely manner` anchored to RTO 24h. | STANDARD | MUST | [AG-D-04.2-001](#ag-d-d04-2-001) | | — | | — |
| D-04.3 (Incident Notification & Reporting) | `SO-D-04.3.GDPR` | Personal-data breach notification to controller and supervisory authority via **multi-reg max-SLA 24h routing** (resolves T-001): single workflow satisfies GDPR Art. 33(2) processor→controller `without undue delay` + CRA Art. 14(1-2) AEV + NIS 2 Art. 23(4)(a) significant incident + AI_Act Art. 73(3) 2-day widespread infringement; CEO/board liability (NIS 2 Art. 20). | RIGOROUS | MUST | [AG-D-04.3-001](#ag-d-d04-3-001) | | — | | — |
| D-04.4 (Incident Recovery & Lessons Learned) | `SO-D-04.4.GDPR` | Personal-data restoration and recovery via RTO 24h, RPO 1h; immutable backup with 10-year retention; quarterly restore drill (ISO 27001 A.17); GDPR Art. 32(1)(b)(c) `restore availability and access in timely manner`. | STANDARD | MUST | [AG-D-04.4-001](#ag-d-d04-4-001) | | — | | — |
| D-05.1 (Data Minimisation) | `SO-D-05.1.GDPR` | Personal-data minimisation enforced at field-level in schema; biometric reference data deleted after match (seconds, ephemeral); data minimisation review per release per AI_Act Art. 10 data governance + GDPR Art. 5(1)(c). | STANDARD | MUST | [AG-D-05.1-001](#ag-d-d05-1-001) | | — | | — |
| D-05.2 (Retention & Archiving) | `SO-D-05.2.GDPR` | Personal-data retention policy (per data type): biometric ephemeral (seconds); audit logs 10 years (CRA Art. 13(13) + NIS 2); watchlist per government policy; documented per GDPR Art. 5(1)(e) storage limitation. | STANDARD | MUST | [AG-D-05.2-001](#ag-d-d05-2-001) | | — | | — |
| D-05.3 (Right to Erasure) | `SO-D-05.3.GDPR` | Right-to-erasure endpoint + cryptographic sharding — destroy biometric↔identity mapping, retain anonymised audit trail (resolves T-002 GDPR Art. 17 vs AI_Act Art. 19(1) log retention — AI_Act Art. 12 governs transparency; AI_Act is not a D-05.3 participant); GDPR Art. 17 erasure per data subject request. | STANDARD | MUST | [AG-D-05.3-001](#ag-d-d05-3-001) | | — | | — |
| D-05.4 (Data Portability) | `SO-D-05.4.GDPR` | Data portability endpoint (JSON export) per GDPR Art. 20; covers audit-log-controller capacity; machine-readable format documented per Art. 20(3). | STANDARD | MUST | [AG-D-05.4-001](#ag-d-d05-4-001) | | — | | — |
| D-06.1 (Vendor Risk Assessment) | `SO-D-06.1.GDPR` | Personal-data processor (biometric sub-processor) agreements per GDPR Art. 28; due diligence on each processor covers Art. 28(1) `sufficient guarantees`; biometric-specific safeguards documented. | RIGOROUS | MUST | [AG-D-06.1-001](#ag-d-d06-1-001) | | — | | — |
| D-06.2 (Software Bill of Materials (software bill of materials)) | — | N/A — non-privacy sub-domain (CRA-only software bill of materials). Personal-data exposure from vulnerable components is mitigated by the software bill of materials-anchored vulnerability tracking (D-02.1). | STANDARD | MUST | [AG-D-06.2-001](#ag-d-d06-2-001) |
| D-06.3 (Contractual Security Obligations) | `SO-D-06.3.GDPR` | Personal-data contractual chain via DPA template + supplier security clauses; GDPR Art. 28(3) 8-element DPA list enforced; multi-tier sub-processor flowdown; right-to-audit clauses. | RIGOROUS | MUST | [AG-D-06.3-001](#ag-d-d06-3-001) | | — | | — |
| D-06.4 (Third-Party Boundary Management) | `SO-D-06.4.GDPR` | Personal-data boundary management via network segmentation (SecureBorder/Cloud/Government); mutual transport authentication on all boundaries; zero-trust kiosk↔cloud; documented per GDPR Art. 32(1)(b) `ongoing confidentiality`. | STANDARD | MUST | [AG-D-06.4-001](#ag-d-d06-4-001) | | — | | — |
| D-07.1 (Secure-by-Design Principles) | `SO-D-07.1.GDPR` | Personal-data protection by design via privacy-by-design (GDPR Art. 25(1)) integrated with AI_Act risk management system (Art. 9); unified SDLC covers high-risk AI; threat modelling per feature (STRIDE + AI-specific extensions). | RIGOROUS | MUST | [AG-D-07.1-001](#ag-d-d07-1-001) | | — | | — |
| D-07.2 (Secure Coding Practices) | — | N/A — non-privacy sub-domain (CRA + AI_Act secure coding). Personal-data protection from vulnerable code is discharged via the secure-coding controls themselves (static application security testing/dynamic application security testing in CI). | STANDARD | MUST | [AG-D-07.2-001](#ag-d-d07-2-001) | | — | | — |
| D-07.3 (CI/CD Pipeline Security) | — | N/A — non-privacy sub-domain (NIS 2 + CRA pipeline security). Personal-data integrity through the pipeline is protected by the pipeline-security controls themselves (signed artefacts, software bill of materials gate). | RIGOROUS | MUST | [AG-D-07.3-001](#ag-d-d07-3-001) | | — | | — |
| D-08.1 (General Security Awareness) | `SO-D-08.1.GDPR` | Annual security awareness training includes GDPR-specific module (data subject rights, breach recognition, biometric-data handling); phishing simulation quarterly; kiosk-specific security guide; documented per GDPR Art. 39 DPO-informed training. | STANDARD | MUST | [AG-D-08.1-001](#ag-d-d08-1-001) | | — | | — |
| D-08.2 (Role-Specific Competence) | `SO-D-08.2.GDPR` | DPO role-specific competence (Art. 37(1)(c) mandatory) — DPO training + AI Governance Lead training per AI_Act Art. 14 human oversight + SOC analyst certification; continuing professional education. | STANDARD | MUST | [AG-D-08.2-001](#ag-d-d08-2-001) | | — | | — |
| D-09.1 (Information Security Policies) | `SO-D-09.1.GDPR` | Personal-data policies integrated in ISO 27001 certified ISMS (Doc 04 §10.4); unified policies with regulation-specific annexes; annual surveillance audit; DPO oversight. | STANDARD | MUST | [AG-D-09.1-001](#ag-d-d09-1-001) | | — | | — |
| D-09.2 (Impact & Risk Assessments) | `SO-D-09.2.GDPR` | Personal-data impact assessment via unified DPIA (GDPR Art. 35) + FRIA (AI_Act Art. 27) single process with dual output; cross-impact CRDA analysis; threshold-trigger criteria per Art. 35(3) and Art. 27(1). | STANDARD | MUST | [AG-D-09.2-001](#ag-d-d09-2-001) | | — | | — |
| D-09.4 (Records of Processing) | `SO-D-09.4.GDPR` | Records of processing activities (RoPA) cover personal-data processing per GDPR Art. 30; DPO oversight; immutable storage; 10-year retention. | STANDARD | MUST | [AG-D-09.4-001](#ag-d-d09-4-001) | | — | | — |
| D-10.1 (Continuous Security Monitoring) | `SO-D-10.1.GDPR` | Personal-data security monitoring via 24/7 SOC with Security Information and Event Management; AI-driven anomaly detection on on-device pipeline; biometric-data scope alerts; documented per GDPR Art. 32(1)(d) `regular testing`. | RIGOROUS | MUST | [AG-D-10.1-001](#ag-d-d10-1-001) | | — | | — |
| D-10.2 (Audit Logging & Traceability) | `SO-D-10.2.GDPR` | Personal-data audit log via tamper-evident log (GDPR Art. 30 controller capacity); 10-year retention; cryptographic hash chain; documented per Art. 5(2) accountability principle. | STANDARD | MUST | [AG-D-10.2-001](#ag-d-d10-2-001) | | — | | — |
| D-10.3 (Compliance Testing) | `SO-D-10.3.GDPR` | Personal-data compliance testing via annual ISO 27001 surveillance audit + DPIA re-assessment + GDPR Art. 35(11) review on material change; CISO sign-off. | STANDARD | MUST | [AG-D-10.3-001](#ag-d-d10-3-001) | | — | | — |

**Total rows:** 35.

## §3 Adjusted Security Goals (SG) per Sub-Domain

Adjusted Security Goals are Case_02-specific restatements of the corpus generic non-GDPR Sub-SO. The source regulation per row is whichever of CRA / NIS 2 / AI_Act carries the substantive obligation at that sub-domain (chosen by the strictest applicable floor — typically CRA state-of-the-art baseline discharges the others, except where AI_Act Annex III imposes a separate AI-specific duty). D-05.4 is GDPR-only (Art. 20 data portability) and therefore has no SG row.

| Sub-Domain | Generic Sub-SO (source reg) | Adjusted SG (Case_02-specific) | Tier | Priority | Details | | NIST Anchors | | NIST Anchors |
|------------|------------------------------|---------------------------------|------|----------|---------| | --- | | --- |
| D-01.1 (Data at Rest Encryption) | `SO-D-01.1.CRA` (CRA) | Annex I Part I (2)(e) `render unintelligible` test is met via hardware cryptographic module-backed industry-standard authenticated encryption for all stored data on the eGate kiosk (personal or other per Art. 3(47) cross-reference); Annex VII technical documentation references the hardware cryptographic module architecture; CRA conformity assessment module selected per critical-product classification. | RIGOROUS | MUST | [AG-D-01.1-002](#ag-d-d01-1-002) | | — | | — |
| D-01.2 (Data in Transit Encryption) | `SO-D-01.2.CRA` (CRA) | CRA Annex I Part I (2)(e) extends to data in transit with state-of-the-art mechanisms; NIS 2 Art. 21(2)(h) cryptography policy covers transit; the hardware cryptographic module-signed cert chain and cipher-suite allowlist discharge both on a single kiosk-edge artefact. | STANDARD | MUST | [AG-D-01.2-002](#ag-d-d01-2-002) | | — | | — |
| D-01.3 (Cryptographic Key Management) | `SO-D-01.3.CRA` (CRA) | CRA Annex I Part I (2)(e) `state-of-the-art mechanisms` baseline applies to key custody as well as ciphertext; the de-attribution test procedure is part of CRA conformity assessment technical documentation. | RIGOROUS | MUST | [AG-D-01.3-002](#ag-d-d01-3-002) | | — | | — |
| D-01.4 (Data Integrity Mechanisms) | `SO-D-01.4.AI_Act` (AI_Act) | AI_Act Art. 15 (accuracy + robustness + cybersecurity) requires data integrity for high-risk AI training/inference data; AI_Act Art. 10 (data governance) requires data-quality checks; CRA Annex I Part I (2)(d) `integrity` baseline discharged by cryptographic integrity check + signed audit log. | STANDARD | MUST | [AG-D-01.4-002](#ag-d-d01-4-002) | | — | | — |
| D-02.1 (Vulnerability Identification) | `SO-D-02.1.CRA` (CRA) | CRA Art. 13(8) `without delay` vulnerability handling during support period; CRA Art. 14(1) actively-exploited vulnerability (AEV) reporting; the dependency vulnerability scanner + npm audit + monthly vuln review board satisfies CRA software bill of materials-anchored vulnerability tracking on a single artefact. | STANDARD | MUST | [AG-D-02.1-002](#ag-d-d02-1-002) | | — | | — |
| D-02.2 (Patch Management & Updates) | `SO-D-02.2.CRA` (CRA) | CRA-aligned patch SLA: critical 24h, high 7d (matches Doc 07 SI-002 24h max-SLA per T-001 resolution); secure OTA update pipeline with hardware cryptographic module-signed firmware; CRA Art. 13(8) 5y support period + Art. 13(9) 10y update availability tail. | STANDARD | MUST | [AG-D-02.2-002](#ag-d-d02-2-002) | | — | | — |
| D-02.3 (Coordinated Vulnerability Disclosure) | `SO-D-02.3.CRA` (CRA) | CRA Art. 14 single point of contact + Art. 16 dissemination with delay grounds; security.txt at /.well-known/security.txt + CVD page + 24h acknowledgement SLA; CRA-Art. 14(1-2) AEV reporting aligned with NIS 2 Art. 23(4)(a) on a single workflow. | STANDARD | MUST | [AG-D-02.3-002](#ag-d-d02-3-002) | | — | | — |
| D-02.4 (Threat-Led Penetration Testing) | `SO-D-02.4.AI_Act` (AI_Act) | AI_Act Art. 9 risk management system requires adversarial testing + robustness testing; AI_Act Art. 72 post-market monitoring feeds the threat-led pen test schedule; CRA Annex I Part I (2)(c) `attack surface minimisation` is tested via annual external pen test; certified penetration testing practitioners-accredited testers. | STANDARD | MUST | [AG-D-02.4-002](#ag-d-d02-4-002) | | — | | — |
| D-03.1 (Identity Lifecycle Management) | `SO-D-03.1.CRA` (CRA) | CRA Art. 13(2) secure-by-default kiosk identity config + CRA Art. 14(1) AEV scope covers compromised credentials; NIS 2 Art. 21(2)(i) `joiner-mover-leaver` lifecycle discharged via provisioning protocol on the same artefact. | STANDARD | MUST | [AG-D-03.1-002](#ag-d-d03-1-002) | | — | | — |
| D-03.2 (Multi-Factor Authentication) | `SO-D-03.2.CRA` (CRA) | CRA Art. 13(2) secure installation requires multi-factor authentication on first-boot setup; NIS 2 Art. 21(2)(g) training covers multi-factor authentication; hardware multi-factor authentication tokens (hardware-backed second-factor authenticator) discharge both on a single artefact. | STANDARD | MUST | [AG-D-03.2-002](#ag-d-d03-2-002) | | — | | — |
| D-03.3 (Authorisation & Least Privilege) | `SO-D-03.3.NIS2` (NIS 2) | NIS 2 Art. 21(2)(i) access control policy + Art. 21(2)(d) supply-chain scope; role-based access control + attribute-based access control + separation of duties enforced on a single access-management artefact. | STANDARD | MUST | [AG-D-03.3-002](#ag-d-d03-3-002) | | — | | — |
| D-03.4 (Secure System Defaults) | `SO-D-03.4.CRA` (CRA) | CRA Art. 13(2) secure-by-default kiosk config: debug ports disabled, default passwords rotated, signed firmware required; CRA conformity assessment includes defaults check. | STANDARD | MUST | [AG-D-03.4-002](#ag-d-d03-4-002) | | — | | — |
| D-04.1 (Incident Detection & Triage) | `SO-D-04.1.CRA` (CRA) | CRA Art. 14(3) severe-incident detection duty; AI-driven on-device anomaly detection covers AI_Act Art. 72 post-market monitoring + Art. 73 serious-incident detection on a single SOC workflow. | STANDARD | MUST | [AG-D-04.1-002](#ag-d-d04-1-002) | | — | | — |
| D-04.2 (Incident Containment & Response) | `SO-D-04.2.CRA` (CRA) | CRA Art. 21 manufacturer-equivalent trigger + CRA Art. 14(3) severe-incident containment; documented incident response procedure aligns with CRA + NIS 2 on a single CSIRT workflow. | STANDARD | MUST | [AG-D-04.2-002](#ag-d-d04-2-002) | | — | | — |
| D-04.3 (Incident Notification & Reporting) | `SO-D-04.3.CRA` (CRA) | CRA Art. 14(1-2) AEV notification + Art. 14(3) severe-incident notification + Art. 14(8) user notification; the max-SLA 24h routing workflow is RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4. | RIGOROUS | MUST | [AG-D-04.3-002](#ag-d-d04-3-002) | | — | | — |
| D-04.4 (Incident Recovery & Lessons Learned) | `SO-D-04.4.NIS2` (NIS 2) | NIS 2 Art. 21(2)(c) business continuity + Art. 21(2)(d) supply-chain DR; 10y retention anchors CRA Art. 13(13) + NIS 2 Art. 21(2) on a single DR artefact. | STANDARD | MUST | [AG-D-04.4-002](#ag-d-d04-4-002) | | — | | — |
| D-05.1 (Data Minimisation) | `SO-D-05.1.CRA` (CRA) | CRA Art. 13(3) intended purpose + reasonably foreseeable use; CRA Art. 13(5) supply-chain data minimisation; biometric ephemeral pattern documented in Annex VII technical file. | STANDARD | MUST | [AG-D-05.1-002](#ag-d-d05-1-002) | | — | | — |
| D-05.2 (Retention & Archiving) | `SO-D-05.2.AIACT` (AI_Act) | AI_Act Art. 19(1) `at least six months` automatic logging retention; the 10y retention is above the AI_Act floor; CRA Art. 13(13) technical documentation retention aligned. | STANDARD | MUST | [AG-D-05.2-002](#ag-d-d05-2-002) | | — | | — |
| D-05.3 (Right to Erasure) | `SO-D-05.3.CRA` (CRA) | CRA Art. 13(5) `deletes` = cryptographic erasure (key destruction) where data is replicated; physical destruction only for single-copy storage media; CRA Art. 13(8) `without delay` from awareness. | STANDARD | MUST | [AG-D-05.3-002](#ag-d-d05-3-002) | | — | | — |
| D-05.4 (Data Portability) | — | N/A — GDPR-only sub-domain (data portability is GDPR Art. 20 with no CRA/NIS 2/AI_Act parallel); SG row omitted (PG only). | — | — | [AG-D-05.4-002 (N/A)](#ag-d-d05-4-002) |
| D-06.1 (Vendor Risk Assessment) | `SO-D-06.1.NIS2` (NIS 2) | NIS 2 Art. 21(2)(d) supply-chain risk assessment (direct supplier scope per Art. 21(3) three-prong); annual supplier audit; RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4. | RIGOROUS | MUST | [AG-D-06.1-002](#ag-d-d06-1-002) | | — | | — |
| D-06.2 (Software Bill of Materials (software bill of materials)) | `SO-D-06.2.CRA` (CRA) | CRA Art. 13(11) software bill of materials per release; machine-readable software bill of materials format format; signed software bill of materials attached to firmware; vulnerability tracking against software bill of materials is the only applicable regulatory floor (CRA is the sole authority at D-06.2). | STANDARD | MUST | [AG-D-06.2-002](#ag-d-d06-2-002) |
| D-06.3 (Contractual Security Obligations) | `SO-D-06.3.NIS2` (NIS 2) | NIS 2 Art. 21(2)(d) contractual chain + Art. 21(3) supplier assessment three-prong; GDPR Art. 46 transfer safeguards for non-EU suppliers; RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4. | RIGOROUS | MUST | [AG-D-06.3-002](#ag-d-d06-3-002) | | — | | — |
| D-06.4 (Third-Party Boundary Management) | `SO-D-06.4.NIS2` (NIS 2) | NIS 2 Art. 21(2)(d) supply-chain boundary + Art. 21(2)(e) network security; mutual transport authentication + segmentation discharge both on a single network-security artefact. | STANDARD | MUST | [AG-D-06.4-002](#ag-d-d06-4-002) | | — | | — |
| D-07.1 (Secure-by-Design Principles) | `SO-D-07.1.AIACT` (AI_Act) | AI_Act Art. 9 risk management system + Art. 13 transparency + Art. 14 human oversight; CRA Art. 13(1)+(2) secure-by-default + risk assessment propagation across 6 lifecycle phases; RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4. | RIGOROUS | MUST | [AG-D-07.1-002](#ag-d-d07-1-002) | | — | | — |
| D-07.2 (Secure Coding Practices) | `SO-D-07.2.CRA` (CRA) | CRA Annex I Part I (2)(c) attack-surface minimisation via secure coding standards (application security maturity model at industry-standard level for AI components); static application security testing (static application security testing tool) + dynamic application security testing in CI; pre-commit secret scanning; CRA Art. 13(11) software bill of materials-anchored vulnerability tracking. | STANDARD | MUST | [AG-D-07.2-002](#ag-d-d07-2-002) | | — | | — |
| D-07.3 (CI/CD Pipeline Security) | `SO-D-07.3.NIS2` (NIS 2) | NIS 2 Art. 21(2)(d) supply-chain security + CRA Art. 13(11) software bill of materials; signed CI artefacts + pipeline-as-code + supply-chain integrity controls Level 3; software bill of materials gate blocks on critical vulns; RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4. | RIGOROUS | MUST | [AG-D-07.3-002](#ag-d-d07-3-002) | | — | | — |
| D-08.1 (General Security Awareness) | `SO-D-08.1.NIS2` (NIS 2) | NIS 2 Art. 21(2)(g) basic cyber hygiene + Art. 21(2)(f) training; CRA Art. 13(2) installation/use training included; phishing simulation + kiosk-specific guide on a single training programme. | STANDARD | MUST | [AG-D-08.1-002](#ag-d-d08-1-002) | | — | | — |
| D-08.2 (Role-Specific Competence) | `SO-D-08.2.NIS2` (NIS 2) | NIS 2 Art. 21(2)(g) role-specific competence + AI_Act Art. 4 AI literacy; SOC analyst certification + DPO + AI Lead training on a single competence framework. | STANDARD | MUST | [AG-D-08.2-002](#ag-d-d08-2-002) | | — | | — |
| D-09.1 (Information Security Policies) | `SO-D-09.1.AI_Act` (AI_Act) | AI_Act Art. 9 risk-management policies + Art. 13 transparency policies + CRA Art. 13(8) support policies + NIS 2 Art. 21(1) framework policies + GDPR Art. 5(2) accountability; ISO 27001 certified ISMS discharges all four on a single policy artefact. | STANDARD | MUST | [AG-D-09.1-002](#ag-d-d09-1-002) | | — | | — |
| D-09.2 (Impact & Risk Assessments) | `SO-D-09.2.AI_Act` (AI_Act) | AI_Act Art. 27 FRIA + Art. 9 risk-management system; CRA Art. 13(2) risk assessment + NIS 2 Art. 21(1) risk analysis; the unified DPIA+FRIA process discharges all four on a single impact-assessment artefact (resolves T-003). | STANDARD | MUST | [AG-D-09.2-002](#ag-d-d09-2-002) | | — | | — |
| D-09.4 (Records of Processing) | `SO-D-09.4.AI_Act` (AI_Act) | AI_Act Art. 12 record-keeping + CRA Art. 13(12) technical documentation + NIS 2 Art. 21(2)(a) risk-assessment records + GDPR Art. 30 RoPA; DPO oversight + immutable storage on a single record-keeping artefact. | STANDARD | MUST | [AG-D-09.4-002](#ag-d-d09-4-002) | | — | | — |
| D-10.1 (Continuous Security Monitoring) | `SO-D-10.1.AI_Act` (AI_Act) | AI_Act Art. 72 post-market monitoring + Art. 73 serious-incident detection + NIS 2 Art. 21(2)(g) continuous monitoring + CRA Art. 14(3) severe-incident detection; 24/7 SOC + AI model drift detection on a single monitoring artefact; RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4. | RIGOROUS | MUST | [AG-D-10.1-002](#ag-d-d10-1-002) | | — | | — |
| D-10.2 (Audit Logging & Traceability) | `SO-D-10.2.AI_Act` (AI_Act) | AI_Act Art. 12 logging capability + Art. 19(1) `at least six months` automatic retention + CRA Art. 13(14) logging + NIS 2 Art. 21(2)(h) cryptography-policy logging; tamper-evident + 10y retention above the Art. 19(1) floor on a single log artefact. | STANDARD | MUST | [AG-D-10.2-002](#ag-d-d10-2-002) | | — | | — |
| D-10.3 (Compliance Testing) | `SO-D-10.3.AI_Act` (AI_Act) | AI_Act Art. 43 conformity assessment re-assessment + Art. 72 post-market re-evaluation + CRA Art. 24(3) OSS steward extension + NIS 2 Art. 21(2) controls test + GDPR Art. 28(3)(h) processor audit; annual ISO 27001 surveillance + AI_Act conformity re-assessment on a single compliance-test programme. | STANDARD | MUST | [AG-D-10.3-002](#ag-d-d10-3-002) | | — | | — |

**Total rows:** 35 (D-05.4 GDPR-only has SG = `N/A`).

## §4 Tensions Resolved (multi-paragraph, 3 tensions)

Three strategic tensions were identified in Doc 07 §5.5; all are resolved in Doc 07b §4 and §5. The multi-paragraph expansions below restate the tensions with full root-cause analysis, source citations, resolution options, and implementation criteria. The summary table follows the multi-paragraph treatment.

### T-001 (D-04.3) — GDPR 72h vs NIS 2 24h vs CRA 24h vs AI_Act 15d/2d temporal conflict

**Root Cause Analysis (multi-paragraph):**

The temporal conflict originates from four regulators imposing notification clocks on different parties, starting at different events, expiring at different recipients, and tracking different incident categories. **GDPR Art. 33(1)** imposes a 72-hour clock on the controller (the government border authority), running from the moment the controller becomes aware of a personal-data breach, and notifying the supervisory authority (DPA). **GDPR Art. 33(2)** imposes a separate clock on the processor (SecureBorder) to notify the controller "without undue delay" — a clock without a fixed numeric deadline, typically interpreted as 24-48 hours. **CRA Art. 14(1)-(2)** imposes a 24-hour early-warning clock on the manufacturer (SecureBorder) to CSIRT/ENISA for actively-exploited vulnerabilities, with a 72-hour follow-up notification and a 14-day final report after the corrective measure is available. **CRA Art. 14(3)-(5)** imposes a 24-hour early-warning clock on the manufacturer for severe incidents affecting product security, with a 72-hour follow-up and a 1-month final report. **NIS 2 Art. 23(4)(a)** imposes a 24-hour early-warning clock on the essential entity (or supplier in the case of SecureBorder) to the CSIRT, with a 72-hour notification, a 1-month intermediate report, and a final report on incident handling. **AI_Act Art. 73(2)** imposes a 15-day clock on the provider for serious incidents (default), **Art. 73(3)** imposes a 2-day clock for widespread infringement or incidents listed in Art. 3(49)(b), and **Art. 73(4)** imposes a 10-day clock for death of a person.

**Why this is a 4-way tension, not a 2-way or 3-way conflict:** Each regulation tracks a different obligated party (controller vs processor vs manufacturer vs essential entity vs provider), a different starting event (personal-data breach vs actively-exploited vulnerability vs severe product-security incident vs significant service incident vs serious AI incident), a different recipient (DPA vs ENISA vs CSIRT vs Notified Body vs market surveillance authority), and a different incident category. The 72h GDPR Art. 33(1) clock is the *longest* of the four; the CRA/NIS 2 24h clock is the *shortest* primary artefact; the AI_Act 15d default is the *most lenient* but the 2d widespread-infringement sub-clock is the *most aggressive*. The conflict is structural, not a wording divergence: a single incident at SecureBorder can simultaneously trigger all four regimes, each on a different timeline, to a different recipient, with a different content requirement.

**Source Citations:** GDPR-C25 (Art. 33), CRA-C20 (Art. 14), NIS2-CL26 (Art. 23), AI_Act Art. 73(2-4). Corpus paths: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/D-04.3.json`.

**Resolution Options Considered:**

1. **Multi-reg max-SLA 24h routing — CHOSEN.** Single workflow with a 24h clock; AI_Act 15d default and 2d widespread-infringement sub-workflow attached; documented incident response procedure drives the 24h decision-window. Per-recipient evidence packs (DPA / ENISA / CSIRT / Notified Body) preserve evidence-layer segregation. RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4.
2. **Separate workflows per reg — REJECTED.** Operational duplication, four incident commanders, four clocks to manage, four evidence packs, four audit trails. Failure mode is high.
3. **AI_Act separate cadence (15d/2d) — REJECTED.** The 15d default is too long for biometric data; the 2d sub-clock is shorter than the 24h clock and would force a different cadence. Adopt the 2d clock as a sub-workflow within the max-SLA 24h pipeline.

**Implementation:** Single incident workflow with 24h clock; AI_Act 2d widespread-infringement sub-workflow attached; documented incident response procedure gates the 24h notification decision; per-recipient evidence packs (DPA / ENISA / CSIRT / Notified Body) with per-recipient content; quarterly incident response exercise verifies the 24h delivery to all four channels on a single timeline.

**Verification Criteria:** Tabletop exercise demonstrating 24h delivery to DPA, ENISA, CSIRT, and Notified Body on a single timeline; quarterly review of the routing pipeline; annual audit (RIGOROUS tier) confirming the evidence-layer segregation.

**Risk if not resolved:** HIGH — Late notification triggers GDPR Art. 83(4) fine (up to €10M or 2% turnover), CRA Art. 56 fine (up to €15M or 2.5% turnover), NIS 2 Art. 20 management liability (CEO/board personally), and AI_Act Art. 99 fine (up to €15M or 3% turnover). Four simultaneous fines on a single incident.

**Stakeholder Alignment:** CISO + DPO + Legal Counsel + CEO + AI Governance Lead. Status: AGREED.

**Status:** AGREED

---

### T-002 (D-05.3 ↔ D-10.2) — GDPR Art. 17 erasure vs AI_Act Art. 19(1) log retention (D-10.2; AI_Act is NOT a D-05.3 participant)

**Root Cause Analysis (multi-paragraph):**

The conflict arises from two regulators imposing irreconcilable obligations on the same data: erasure on request versus retention for accountability. **GDPR Art. 17** grants the data subject the right to obtain from the controller "the erasure without undue delay of personal data concerning him or her" when the grounds in Art. 17(1) apply (no longer necessary, consent withdrawn, objection sustained, unlawful processing, legal obligation). The right is enforceable against the controller (the government border authority for SecureBorder's biometric processing) and against the processor (SecureBorder) by DPA. **AI_Act Art. 19(1)** (governing high-risk AI providers) sets the retention floor at "at least six months" for automatic logging of events over the system's lifecycle — the logs include biometric-data scope events. The conflict is at the data-subject layer: GDPR Art. 17 demands that biometric data be erased; AI_Act Art. 19(1) demands that the logs (which contain or reference biometric data) be retained for at least six months. **Note:** AI_Act Art. 12 covers transparency obligations for providers and deployers of certain AI systems; it is NOT a D-05.3 (Right to Erasure) participant. Erasure is GDPR Art. 17 only; AI_Act Art. 19(1) governs LOGGING retention which is D-10.2, not D-05.3.

**Why this is a structural conflict, not a wording divergence:** Erasure and retention are reciprocal obligations on the same physical or logical record. The OJ text does not provide a carve-out — Art. 17(3) lists exceptions (legal obligation, public interest, public health, archiving, legal claims) but AI_Act logging is not on that list. AI_Act Art. 19(1) does not provide an erasure exemption. A literal reading makes the two obligations mutually exclusive on a single artefact.

**Source Citations:** GDPR-C17 (Art. 17), AI_Act Art. 19(1) (logging retention; Art. 12 governs transparency and is NOT a D-05.3 participant). Corpus paths: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.3/D-05.3.json` and `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/D-10.2.json`.

**Resolution Options Considered:**

1. **Cryptographic sharding — CHOSEN.** hardware cryptographic module-backed key custody with biometric↔identity mapping stored as a separate cryptographic layer. On erasure request, destroy the biometric-shard key; the audit log retains only an anonymised trail (no biometric identifier, no identity mapping). AI_Act Art. 19(1) ≥6-month retention is met (the anonymised log is retained above the Art. 19(1) floor). GDPR Art. 17 erasure is met (the biometric data is no longer recoverable; the identity mapping is destroyed). The two obligations are discharged on different artefacts. **Note:** AI_Act Art. 12 governs transparency (not logging) and is NOT a D-05.3 participant.
2. **Anonymise the biometric data on creation — REJECTED.** Loses the identifying functionality required for border control; technically and legally infeasible.
3. **Hold all erasure requests for the AI_Act 6-month period — REJECTED.** GDPR Art. 12(3) requires one-month response; AI_Act 6-month retention exceeds the deadline. Direct breach of GDPR.
4. **Delegate to the controller — REJECTED.** The controller (government) is the GDPR-addressable party, but the controller cannot alter the AI_Act logging requirement on the processor.

**Implementation:** hardware cryptographic module-backed key custody with biometric-shard key destruction on erasure; AI_Act log retains only non-identifying trail (timestamps, action types, request IDs) for the 10-year retention period (above the Art. 19(1) floor); standard tier on both D-05.3 and D-10.2 rows; quarterly verification of the cryptographic sharding.

**Verification Criteria:** Erasure endpoint demonstrates biometric↔identity mapping destroyed via hardware cryptographic module key destruction; audit log retains anonymised trail; re-identification attempt fails (documented test); AI_Act log integrity verified via hash chain.

**Risk if not resolved:** HIGH — GDPR Art. 83(5) fine (up to €20M or 4% turnover) for Art. 17 failure; AI_Act Art. 99 fine (up to €15M or 3% turnover) for Art. 19(1) logging-retention failure. Biometric Art. 9 sensitivity amplifies the GDPR fine.

**Stakeholder Alignment:** DPO + CISO + AI Governance Lead + Legal Counsel. Status: AGREED.

**Status:** AGREED

---

### T-003 (D-09.2) — GDPR Art. 35 DPIA vs AI_Act Art. 27 FRIA trigger mismatch

**Root Cause Analysis (multi-paragraph):**

The trigger mismatch arises from two regulators imposing impact assessment obligations on the same processing operation but with different trigger criteria, different content templates, different recipients, and different review cadences. **GDPR Art. 35(1)** requires a DPIA where processing is "likely to result in a high risk to the rights and freedoms of natural persons". **Art. 35(3)** lists nine mandatory triggers (systematic + extensive evaluation, large-scale special-category data, systematic monitoring of public area) — large-scale Art. 9 data is an automatic trigger per Art. 35(3)(b). The DPIA content (Art. 35(7)) is a systematic description of the processing, an assessment of the necessity and proportionality, an assessment of the risks to data subjects, and the measures envisaged to address those risks. The recipient is the supervisory authority (DPA) on request.

**AI_Act Art. 27(1)** requires a FRIA "before the use of [a high-risk AI system]" — the trigger is the high-risk classification of the AI system, not the risk profile of the processing. The content (Art. 27(4)) includes the categories of natural persons affected, the categories of harms, the oversight measures, the risk-mitigation measures, and an assessment of the residual risk. The recipient is the market surveillance authority (Notified Body for Annex III §1 biometric).

**Why this is a trigger mismatch, not a content overlap:** The DPIA trigger is risk-based (processing × risk profile); the FRIA trigger is system-classification-based (AI system × Annex III listing). GuardianGate is *both* an Art. 9 processor (automatic DPIA trigger) and an Annex III high-risk AI system (automatic FRIA trigger). The two assessments are *both required*, but they answer different questions: the DPIA asks "is this processing proportionate to the risk?"; the FRIA asks "does this AI system respect fundamental rights?" The two content templates are not interchangeable.

**Why this is a structural conflict:** A naive implementation would run two separate impact assessments on the same feature release, doubling effort and risking divergent findings. Worse, a naive reading could conflate the two and produce a single assessment that fails to address either articulation correctly.

**Source Citations:** GDPR-C35 (Art. 35), AI_Act Art. 27 + Art. 9. Corpus paths: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/D-09.2.json`.

**Resolution Options Considered:**

1. **Unified DPIA+FRIA single process with dual output — CHOSEN.** A single assessment process triggers on the more restrictive of the two criteria (Annex III high-risk AI), produces a single artefact body, and emits two outputs: a GDPR Art. 35(7) DPIA output and an AI_Act Art. 27(4) FRIA output. Per-recipient outputs are preserved verbatim. Cross-impact CRDA analysis identifies any divergence between the two assessments. Annual review per Art. 35(11) + AI_Act Art. 72 post-market monitoring.
2. **Two separate assessments — REJECTED.** Operational duplication, risk of divergent findings, doubled effort per release.
3. **DPIA only with FRIA addendum — REJECTED.** Could fail to address the AI_Act-specific content if the DPIA is the primary artefact.

**Implementation:** Unified DPIA+FRIA single process with dual output; per-recipient outputs preserved verbatim (GDPR Art. 35(7) + AI_Act Art. 27(4)); standard tier on D-09.2; annual review with DPO + AI Governance Lead sign-off.

**Verification Criteria:** Cross-impact CRDA analysis identifies any divergence between DPIA and FRIA outputs; per-recipient outputs preserved verbatim; annual review documented; AI_Act conformity re-assessment (D-10.3) references the unified artefact.

**Risk if not resolved:** MEDIUM — GDPR Art. 35(3)(b) automatic DPIA trigger failure (Art. 83(4) fine up to €10M); AI_Act Art. 27(1) FRIA failure (Art. 99 fine up to €15M). The harm is amplified because Annex III high-risk AI is a regulatory hot-zone.

**Stakeholder Alignment:** DPO + AI Governance Lead + Legal Counsel + CTO. Status: AGREED.

**Status:** AGREED

---

### Tensions Summary Table

| Tension ID | Sub-Domain | Type | Severity | Source 1 | Source 2 | Resolution | Implementation |
|------------|------------|------|----------|----------|----------|------------|----------------|
| **T-001** | D-04.3 (Regulatory Notification) | TEMPORAL_CONFLICT | **CRITICAL** | GDPR Art. 33(2) processor→controller `without undue delay` (72h clock) | CRA Art. 14(1-2) AEV 24h + NIS 2 Art. 23(4)(a) significant-incident 24h + AI_Act Art. 73(3) widespread-infringement 2-day | Max-SLA 24h routing — single workflow satisfies all four; AI_Act 15d limb separate | Multi-reg max-SLA 24h notification pipeline with per-recipient evidence packs (DPA / MSA / CSIRT / Notified Body); RIGOROUS tier; CEO/board liability acknowledged |
| **T-002** | D-05.3 (Right to Erasure) ↔ D-10.2 (Audit Logging) | REQUIREMENT_CONFLICT | **CRITICAL** | GDPR Art. 17 erasure on request | AI_Act Art. 19(1) ≥6-month retention (Art. 12 = transparency, NOT a D-05.3 participant) | Cryptographic sharding — destroy biometric↔identity mapping, retain anonymised audit trail | hardware cryptographic module-backed key custody with biometric-shard key destruction on erasure; AI_Act log retains only non-identifying trail; standard tier on both rows |
| **T-003** | D-09.2 (Impact & Risk Assessments) | TRIGGER_MISMATCH (structural) | MEDIUM | GDPR Art. 35 DPIA (trigger: high-risk processing) | AI_Act Art. 27 FRIA (trigger: high-risk AI placement) | Unified assessment — single process with dual output (Privacy Impact + Fundamental Rights Impact) | DPIA + FRIA single artefact; per-recipient outputs preserved verbatim (GDPR Art. 35(7) + AI_Act Art. 27(4)); standard tier |

**Cross-references:** Doc 07 §5.5 (tension identification); Doc 07b §4 (per-sub-domain realisation); Doc 07b §5 (cross-check vs critical analysis).

## §5 Track B Decision Trail (35 rows)

Track B decision table per Doc 07b §4: the deterministic decision table `(S=MEDIUM, I=BUILD_REQUIRED, P=MUST) → STANDARD baseline` is applied to all 35 active sub-domains, with explicit RIGOROUS overrides for the 8 critical sub-domains listed below. The columns are: `S = MEDIUM` (Case_02 scale); `I` = inheritance pattern (BUILD vs INHERIT); `P` = priority (MUST vs SHOULD vs COULD); `Tier` = per Doc 07b §3; `Rationale` = concise override reason.

| Sub-Domain | S | I | P | Tier | Rationale |
|------------|---|---|---|------|-----------|
| D-01.1 (Data at Rest Encryption) | MEDIUM | BUILD | MUST | RIGOROUS | Biometric Art. 9 — hardware cryptographic module-backed KMS, de-attribution test, cryptographic module certified to highest applicable assurance level |
| D-01.2 (Data in Transit Encryption) | MEDIUM | BUILD | MUST | STANDARD | modern transport security + hardware cryptographic module-signed certs; cipher-suite allowlist |
| D-01.3 (Cryptographic Key Management) | MEDIUM | BUILD | MUST | RIGOROUS | Biometric key custody — classified-key cipher, key-lineage logging |
| D-01.4 (Data Integrity Mechanisms) | MEDIUM | BUILD | MUST | STANDARD | cryptographic integrity check + signed audit log + DB constraints |
| D-02.1 (Vulnerability Identification) | MEDIUM | BUILD | MUST | STANDARD | dependency vulnerability scanner + npm audit + monthly vuln review board |
| D-02.2 (Patch Management & Updates) | MEDIUM | BUILD | MUST | STANDARD | CRA Art. 13(8) 5y support + Art. 13(9) 10y update retention |
| D-02.3 (Coordinated Vulnerability Disclosure) | MEDIUM | BUILD | MUST | STANDARD | security.txt + CVD + 24h acknowledgement SLA |
| D-02.4 (Threat-Led Penetration Testing) | MEDIUM | BUILD | MUST | STANDARD | Annual external pen test + red team on on-device matching |
| D-03.1 (Identity Lifecycle Management) | MEDIUM | BUILD | MUST | STANDARD | Native IAM (dedicated identity governance platform/dedicated identity provider); provisioning protocol provisioning; quarterly access reviews |
| D-03.2 (Multi-Factor Authentication) | MEDIUM | BUILD | MUST | STANDARD | Hardware multi-factor authentication (hardware-backed second-factor authenticator); phishing-resistant |
| D-03.3 (Authorisation & Least Privilege) | MEDIUM | BUILD | MUST | STANDARD | role-based access control + attribute-based access control; separation of duties enforced |
| D-03.4 (Secure System Defaults) | MEDIUM | BUILD | MUST | STANDARD | CRA secure-by-default; debug disabled |
| D-04.1 (Incident Detection & Triage) | MEDIUM | BUILD | MUST | STANDARD | 24/7 SOC + Security Information and Event Management + AI-driven anomaly detection |
| D-04.2 (Incident Containment & Response) | MEDIUM | BUILD | MUST | STANDARD | documented incident response procedure (GDPR Art. 32 processor) |
| D-04.3 (Incident Notification & Reporting) | MEDIUM | BUILD | MUST | RIGOROUS | **RIGOROUS** — 4-reg max-SLA 24h routing (T-001); CEO/board liability |
| D-04.4 (Incident Recovery & Lessons Learned) | MEDIUM | BUILD | MUST | STANDARD | RTO 24h, RPO 1h; 10y audit retention |
| D-05.1 (Data Minimisation) | MEDIUM | BUILD | MUST | STANDARD | Biometric ephemeral (seconds); release-time review |
| D-05.2 (Retention & Archiving) | MEDIUM | BUILD | MUST | STANDARD | 10y audit log retention (CRA + NIS 2) |
| D-05.3 (Right to Erasure) | MEDIUM | BUILD | MUST | STANDARD | Cryptographic sharding — destroy biometric↔identity mapping (T-002) |
| D-05.4 (Data Portability) | MEDIUM | BUILD | MUST | STANDARD | JSON export endpoint per GDPR Art. 20 |
| D-06.1 (Vendor Risk Assessment) | MEDIUM | BUILD | MUST | RIGOROUS | **RIGOROUS** — NIS 2 supply chain + biometric processor agreements |
| D-06.2 (Software Bill of Materials (software bill of materials)) | MEDIUM | BUILD | MUST | STANDARD | machine-readable software bill of materials format software bill of materials per release (CRA) |
| D-06.3 (Contractual Security Obligations) | MEDIUM | BUILD | MUST | RIGOROUS | **RIGOROUS** — NIS 2 + GDPR Art. 28 contractual chain |
| D-06.4 (Third-Party Boundary Management) | MEDIUM | BUILD | MUST | STANDARD | Network segmentation + mutual transport authentication boundaries |
| D-07.1 (Secure-by-Design Principles) | MEDIUM | BUILD | MUST | RIGOROUS | **RIGOROUS** — AI_Act risk mgmt (Art. 9) + CRA secure-by-default |
| D-07.2 (Secure Coding Practices) | MEDIUM | BUILD | MUST | STANDARD | static application security testing/dynamic application security testing in CI; AI-specific secure coding |
| D-07.3 (CI/CD Pipeline Security) | MEDIUM | BUILD | MUST | RIGOROUS | **RIGOROUS** — NIS 2 SDLC pipeline security; supply-chain integrity controls Level 3 |
| D-08.1 (General Security Awareness) | MEDIUM | BUILD | MUST | STANDARD | Annual awareness + quarterly phishing simulation |
| D-08.2 (Role-Specific Competence) | MEDIUM | BUILD | MUST | STANDARD | DPO + AI Lead + SOC analyst competence |
| D-09.1 (Information Security Policies) | MEDIUM | BUILD | MUST | STANDARD | ISO 27001 certified ISMS; unified policies |
| D-09.2 (Impact & Risk Assessments) | MEDIUM | BUILD | MUST | STANDARD | Unified DPIA + FRIA (T-003); cross-impact CRDA |
| D-09.4 (Records of Processing) | MEDIUM | BUILD | MUST | STANDARD | RoPA all 4 regs; immutable; DPO oversight |
| D-10.1 (Continuous Security Monitoring) | MEDIUM | BUILD | MUST | RIGOROUS | **RIGOROUS** — NIS 2 monitoring + AI_Act post-market (Art. 72); T-009 (monitoring opt-out: CRA Annex I (2)(l) vs GDPR Art. 32(2) vs NIS 2 Art. 21(2)(b)) resolved via layered monitoring split |
| D-10.2 (Audit Logging & Traceability) | MEDIUM | BUILD | MUST | STANDARD | Tamper-evident; 10y retention; hash chain |
| D-10.3 (Compliance Testing) | MEDIUM | BUILD | MUST | STANDARD | Annual ISO 27001 + AI_Act + NIS 2 controls test |

**Total rows:** 35 (8 RIGOROUS + 27 STANDARD).

## §6 Cross-References

- **Doc 04** (`Doc03_Company_Context_Assessment.md`) — company context (S = MEDIUM, FTE 5–8, ISO 27001 certified, 4 applicable regs).
- **Doc 05** (`Doc08_Regulatory_Applicability.md`) — applicability + scope_overlap for INHERIT pattern (no INHERITABLE rows for Case_02).
- **Doc 05b** (`Doc09_Ambiguity_Register.md`) — Berry-lens ambiguity register (215 distinct substantive cards; 20 documented as Top-20 in §3).
- **Doc 07** (`Doc11_Structured_Compliance_Matrix.md`) — coverage matrix (35/38 = 92.1%); §5.5 strategic tensions T-001/002/003.
- **Doc 07b** (`Doc12_Proportionality_Profile.md`) — Track B tier assignment (8 RIGOROUS + 27 STANDARD); per-sub-domain realisation of §4/§5 of this document.
- **Legacy Phase 1** (`01_PHASE1_CONTEXT/`) — frozen base; this Rich doc extends, not replaces.
- **Phase 2 / Phase 3** — Doc 10 (`Doc16_Privacy_Security_Goals.md`), Doc 11 (`Doc18_Rules_Catalog.md`), Doc 14 (`14_Architectural_Nodes.md`), Doc 15 (`15_Allocation.md`) consume this adjusted-objectives catalog as input.

## §7 Validation

- **35 sub-domains × 1 PG + 1 SG = 70 adjusted objectives** documented in §2 + §3 (D-05.4 has PG only; AG-D-05.4-002 placeholder documents N/A).
- **70 DEEP detail cards** documented in §8 (35 PG + 35 SG) with 15 fields each (NO Effort/Cost/Timeline per task directive).
- **3 tensions resolved** with multi-paragraph treatment per §4 (T-001 max-SLA 24h routing, T-002 cryptographic sharding, T-003 unified DPIA+FRIA).
- **T-009 (D-10.1 monitoring opt-out)** documented in Doc15_Strategic_Tensions_Report.md §4.2; layered monitoring split (analytics opt-out, security-event mandatory) resolves CRA Annex I (2)(l) vs GDPR Art. 32(2) vs NIS 2 Art. 21(2)(b).
- **Track B decision table applied** to all 35 active sub-domains per §5; 8 RIGOROUS overrides documented with rationale.
- **No tier was changed** vs Doc 07b §3 (Sprint 4 fills content; Sprint 0.5 set tiers; Sprint 5 deepens content).
- **§2/§3 tables extended** with "Details" anchor column pointing to §8 detail cards (35 PG + 35 SG anchors).
- **Cross-check with Doc 07b §11 (Sprint 3 Corpus Cross-Check)**: 14 of 14 in-scope rows verified against corpus baseline `verification_method` (TEST) and tier definition (RIGOROUS / STANDARD). F-01 (S-input scale contradiction) flagged in Doc 07b §11.3 is upstream of this document and unresolved at the time of writing.

## §8 DEEP Detail Cards (70 cards: 35 PG + 35 SG)

> Each card has 15 fields per the Sprint 5 directive. **NO Effort/Cost/Timeline fields** per task constraint.
> Click anchors from §2/§3 tables to navigate to cards below.

### AG-D-01.1-001 — Data at Rest Encryption

**Description (multi-paragraph):**

**Context:** SecureBorder's eGate kiosks process biometric facial templates (GDPR Art. 9 special category data) on behalf of government border control authorities. As a processor of large-scale biometric data, SecureBorder must apply data-at-rest encryption whose strength is anchored to the risk-of-processing (Art. 32(1) five preamble factors) and reaches the strictest applicable floor across GDPR Art. 32, CRA Annex I Part I (2)(e), and NIS 2 Art. 21(2)(h). The CRA state-of-the-art baseline is the strictest floor and discharges the other two regimes on a single artefact.

**Scope:** This objective covers all stored data on the eGate kiosk — biometric reference datas, watchlist records, audit logs, and supporting configuration. Cipher strength target is industry-standard authenticated encryption (or stronger) with hardware cryptographic module-backed key custody at cryptographic module certified to applicable assurance level Level 3. Key-rotation policy is quarterly, and cryptographic sharding separates biometric↔identity mapping. The objective includes Annex VII technical documentation anchors for the CRA conformity assessment.

**Boundaries:** Out of scope: data in transit (covered by D-01.2), key-management architecture (covered by D-01.3), and integrity-only controls (covered by D-01.4). Edge cases: ephemeral biometric reference datas (cleared within seconds of match) are in scope of the cipher requirement but not the retention requirement (D-05.2 covers retention). Watchlist data sourced from government authorities is in scope; the encryption obligation does not extend to the government's own back-end systems outside SecureBorder's stack.

**Source Article:** GDPR Art. 9(2)(g) + Art. 32(1)(a)/(b) | CRA Annex I Part I (2)(e) | NIS 2 Art. 21(2)(h)
**NIST CSF Anchors:** PR.DS-01
**Verification Criteria (operational):**
- industry-standard authenticated encryption (or stronger) cipher confirmed on every at-rest eGate kiosk datastore via cryptographic configuration audit
- CRA conformity assessment technical documentation (Annex VII) names hardware cryptographic module architecture per Annex I Part I (2)(e)
- Tamper-evident key-lineage log demonstrates every key creation, rotation, and destruction event tied to biometric key custodian

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-01.3 (key custody), D-02.1 (vuln identification)
**Risk if not met:** HIGH — Biometric data breach exposure; GDPR Art. 83(5) up to €20M or 4% turnover + CRA Art. 56 + AI_Act Art. 99 fines
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA, CSIRT), Internal: CISO, CTO, DPO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-01.2-001 — Data in Transit Encryption

**Description (multi-paragraph):**

**Context:** biometric reference datas and watchlist data traverse three network boundaries: kiosk↔cloud, kiosk↔government, and on-device↔backend. Each link requires transit encryption whose strength is anchored to the data class (biometric) and the regulatory floor (GDPR Art. 32, CRA Annex I Part I (2)(e), NIS 2 Art. 21(2)(h)). modern transport security with mutual transport authentication satisfies the strictest floor; cipher-allowlist enforcement prevents inherited weakness.

**Scope:** All transit links originating from or terminating at the eGate kiosk population. The objective includes cipher-suite policy, certificate provisioning, and rekey cadence. NIS 2 Art. 21(2)(h) cryptography policy + CRA Annex I state-of-the-art baseline are discharged on a single transit-encryption artefact.

**Boundaries:** Out of scope: at-rest encryption (D-01.1), key custody (D-01.3), and integrity of in-transit payloads (D-01.4). Edge cases: roadside or airport-network kiosks where the local link is physically secured are still bound by the cipher-allowlist policy because the regulatory floor is unaffected by physical security.

**Source Article:** GDPR Art. 32(1)(a)/(b) | CRA Annex I Part I (2)(e) | NIS 2 Art. 21(2)(h)
**NIST CSF Anchors:** PR.DS-02
**Verification Criteria (operational):**
- modern transport security with mutual transport authentication enforced on all kiosk↔cloud and kiosk↔government endpoints; cipher-allowlist documented and enforced
- hardware cryptographic module-signed certificate chain validated on every on-device↔backend link; weak ciphers (RC4, 3DES) absent from production
- Documented transit-encryption policy cites GDPR Art. 32(1)(a)/(b) and aligns with CRA Annex I Part I (2)(e)

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** DONE
**Dependencies:** D-01.3 (key custody), D-06.4 (boundary mgmt)
**Risk if not met:** HIGH — Man-in-the-middle attack on biometric data in transit; GDPR + CRA + NIS 2 fines
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA), Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-01.3-001 — Cryptographic Key Management

**Description (multi-paragraph):**

**Context:** Cryptographic key custody for biometric reference datas is the most sensitive single artefact in the SecureBorder stack: a key compromise exposes every template ever processed. GDPR Art. 4(5) pseudonymisation test, CRA functional-role-based access control separation, and the de-attribution test procedure together set the bar. hardware cryptographic module-anchored key custody with cryptographic module certified to applicable assurance level Level 3 certification is the canonical implementation.

**Scope:** All cryptographic key material handling biometric data, including master keys, key-encryption keys, and per-kiosk session keys. Functional role-based access control separates key-material custodian from operational-environment custodian. Key-lineage logging to tamper-evident audit log covers every key lifecycle event (creation, rotation, destruction, escrow). CRA Annex VII technical documentation references the hardware cryptographic module architecture for conformity assessment.

**Boundaries:** Out of scope: cipher algorithm selection (D-01.1) and integrity-only controls (D-01.4). Edge cases: ephemeral session keys (rotated per session) are in scope but their lineage is per-session; legacy key material retired before the biometric scope was activated is out of scope.

**Source Article:** GDPR Art. 4(5) + Art. 32(1)(a) | CRA Annex I Part I (2)(e) | NIS 2 Art. 21(2)(h)
**NIST CSF Anchors:** PR.DS-01, PR.AA-03, PR.AA-04, PR.AA-05
**Verification Criteria (operational):**
- hardware cryptographic module-anchored key custody demonstrably separated between biometric and non-biometric key material (functional role-based access control)
- Key-lineage logging to tamper-evident audit log captures every key lifecycle event with custodian identity
- De-attribution test procedure documented and executed at least once per year (GDPR Art. 4(5) pseudonymisation)

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-01.1 (at-rest), D-01.2 (transit)
**Risk if not met:** HIGH — Key compromise exposes every biometric reference data; Art. 9 + integrity principle breach
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA), Internal: CISO, DPO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-01.4-001 — Data Integrity Mechanisms

**Description (multi-paragraph):**

**Context:** Data integrity of biometric and watchlist records is anchored to GDPR Art. 5(1)(f) integrity principle and CRA Annex I Part I (2)(d) integrity baseline. AI_Act Art. 15 robustness + cybersecurity plus Art. 10 data governance apply to high-risk AI training/inference data. cryptographic integrity check-SHA256 on all biometric data, DB constraints, and signed audit log discharge the three regimes on a single artefact.

**Scope:** All biometric and watchlist records at the field level, plus the audit log integrity chain. Checksum validation on data restore is part of the D-04.4 recovery discipline but is anchored here. AI_Act Art. 10 data-quality checks apply to any update set.

**Boundaries:** Out of scope: at-rest encryption (D-01.1), transit integrity (D-01.2), and key custody (D-01.3). Edge cases: training data integrity for the on-device model is in scope via AI_Act Art. 10; runtime inference data is in scope via AI_Act Art. 15.

**Source Article:** GDPR Art. 5(1)(f) | CRA Annex I Part I (2)(d) | AI_Act Art. 10 + Art. 15
**NIST CSF Anchors:** PR.DS-01, PR.DS-02, PR.DS-10
**Verification Criteria (operational):**
- cryptographic integrity check-SHA256 (or stronger) integrity checks on all biometric and watchlist data with cryptographic verification
- DB constraints + signed audit log reject any biometric or watchlist record failing integrity checks
- Checksum validation executed on every data restore with evidence of test execution and pass/fail outcome

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** DONE
**Dependencies:** D-01.1 (at-rest), D-10.2 (audit log)
**Risk if not met:** MEDIUM — Tampered biometric data leads to false matches and integrity principle breach
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, AI Supervisory Authority), Internal: CTO, DPO
**Maturity Score:** Current 3/4 → Target 3/4
**Implementation Priority:** P0

### AG-D-02.1-001 — Vulnerability Identification

**Description (multi-paragraph):**

**Context:** Personal-data-impacting vulnerabilities identified via dependency vulnerability scanner + npm audit in CI, OSS advisories feed, and a monthly vulnerability review board with CISO + CTO participation. CRA Art. 13(8) (without delay handling) + Art. 14(1) (AEV reporting), NIS 2 Art. 21(2)(e), and AI_Act Art. 9 risk-management system all bind. Vulnerability findings link to the DPIA risk register per GDPR Art. 35.

**Scope:** All OSS components in the eGate stack, firmware, and back-end services. The scope includes any library used in the on-device matching pipeline. Personal-data-impacting vulnerabilities are flagged for DPIA register entry.

**Boundaries:** Out of scope: vulnerability disclosure contacts (D-02.3), patch implementation (D-02.2), and threat-led testing (D-02.4). Edge cases: vulnerabilities in third-party AI models are tracked but patching is governed by vendor update cadence (D-02.2).

**Source Article:** CRA Art. 13(8) + Art. 14(1) | NIS 2 Art. 21(2)(e) | AI_Act Art. 9
**NIST CSF Anchors:** ID.RA-01, ID.RA-03
**Verification Criteria (operational):**
- dependency vulnerability scanner + npm audit scans integrated into CI with high-severity findings blocking merge gate
- Monthly vulnerability review board with CISO + CTO produces documented minutes and tracked remediation actions
- Vulnerability findings linked to the DPIA risk register per GDPR Art. 35 risk assessment

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-06.2 (software bill of materials), D-09.2 (DPIA risk link)
**Risk if not met:** HIGH — Unidentified CVE exploited; CRA Art. 14 AEV reporting + GDPR Art. 32(1)(d) failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (ENISA, CSIRT), Internal: CISO, CTO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-02.2-001 — Patch Management & Updates

**Description (multi-paragraph):**

**Context:** Patch management for the eGate stack is anchored to CRA Art. 13(8) (5-year support period) + Art. 13(9) (10-year update availability). The 24h max-SLA patch cadence for critical vulnerabilities (aligning with T-001 incident timelines) is the operational floor. Secure OTA update pipeline with hardware cryptographic module-signed firmware prevents unauthorised firmware deployment.

**Scope:** All deployed eGate kiosks and back-end services. Personal data integrity is protected by the integrity sub-domain (D-01.4) and the patch cadence satisfies GDPR Art. 32(1)(d) regular testing as a side-effect of CRA Art. 13(8) vulnerability handling.

**Boundaries:** Out of scope: vulnerability identification (D-02.1), vulnerability disclosure (D-02.3), and incident response (D-04.x). Edge cases: emergency out-of-band patches bypass the standard cadence but must still receive hardware cryptographic module signing before deployment.

**Source Article:** CRA Art. 13(8) + Art. 13(9)
**NIST CSF Anchors:** PR.PS-02, PR.IR-03
**Verification Criteria (operational):**
- Critical patch SLA ≤24h (CRA Art. 13(8) without delay) verified via patch-cadence report
- Secure OTA update pipeline with hardware cryptographic module-signed firmware images prevents rollback to unsigned versions
- Vulnerability tracking against software bill of materials detects newly disclosed CVEs within defined cadence

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** IN_PROGRESS
**Dependencies:** D-02.1 (vuln ID), D-06.2 (software bill of materials)
**Risk if not met:** HIGH — Unpatched critical CVE; CRA Art. 13(8) without delay breach + security update retention failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (ENISA), Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-02.3-001 — Coordinated Vulnerability Disclosure

**Description (multi-paragraph):**

**Context:** Coordinated vulnerability disclosure meets CRA Art. 14 (single point of contact + dissemination with delay grounds) and NIS 2 Art. 23(4)(a) (significant incident reporting). security.txt at /.well-known/security.txt + CVD page + 24h acknowledgement SLA cover the operational layer. Personal-data-impacting vulnerabilities reach the controller via the processor→controller breach notification chain (D-04.3) within GDPR's 72h clock.

**Scope:** All externally disclosed vulnerabilities affecting SecureBorder products or substantively similar products. The scope includes the published CVD policy page, the security.txt record, and the acknowledgement SLA.

**Boundaries:** Out of scope: vulnerability identification (D-02.1), patch implementation (D-02.2), and incident notification timelines (D-04.3). Edge cases: vulnerabilities disclosed during the AI_Act post-market monitoring (D-10.1) are in scope via the same CVD page.

**Source Article:** CRA Art. 14(1-2) + Art. 16 | NIS 2 Art. 23(4)(a)
**NIST CSF Anchors:** GV.PO-01, RS.CO-03
**Verification Criteria (operational):**
- security.txt published at /.well-known/security.txt with valid contact and 24h acknowledgement SLA
- CVD policy page lists ISO/IEC 29147 conformant disclosure process with translation to CRA Art. 14 reporting
- Receipt acknowledgement demonstrated within 24h for the most recent in-scope disclosure

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-02.1 (vuln ID), D-04.3 (incident reporting)
**Risk if not met:** MEDIUM — Unmanaged vulnerability disclosure; CRA Art. 14 AEV reporting failure
**Affected Stakeholders:** Researchers (security community), Regulators (ENISA, CSIRT), Internal: CISO, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-02.4-001 — Threat-Led Penetration Testing

**Description (multi-paragraph):**

**Context:** Threat-led penetration testing meets CRA Annex I Part I (2)(c) attack-surface minimisation baseline, AI_Act Art. 9 risk-management (adversarial/robustness testing), and NIS 2 Art. 21(2)(e) testing. Personal-data exposure from pen-test artefacts is governed by the controller's data-handling policy (D-04.4) and the test-environment segregation.

**Scope:** Annual external pen test + red team exercise on on-device matching pipeline. certified penetration testing practitioners-accredited testers. The objective includes adversarial input testing, model poisoning scenarios, and biometric spoofing.

**Boundaries:** Out of scope: routine vulnerability identification (D-02.1), patch management (D-02.2), and incident response (D-04.x). Edge cases: production vs. test environment separation must be validated separately (covered by D-04.4 recovery drill).

**Source Article:** CRA Annex I Part I (2)(c) | AI_Act Art. 9 + Art. 72 | NIS 2 Art. 21(2)(e)
**NIST CSF Anchors:** ID.RA-01, ID.RA-04, PR.PS-06
**Verification Criteria (operational):**
- Annual external pen test by certified penetration testing practitioners-accredited testers with publicly available executive summary
- Red team exercise on on-device matching pipeline covers adversarial inputs, model poisoning, and biometric spoofing
- Threat-led pen test scope aligned with NIS 2 Art. 21(2)(e) and CRA Annex I Part I (2)(c)

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** IN_PROGRESS
**Dependencies:** D-02.1 (vuln ID), D-07.1 (secure-by-design)
**Risk if not met:** MEDIUM — Undiscovered attack surface; AI_Act Art. 9 risk-management + CRA Annex I (2)(c) failure
**Affected Stakeholders:** Travelers (data subjects), Internal: CTO, CISO, AI Governance Lead
**Maturity Score:** Current 2/4 → Target 3/4
**Implementation Priority:** P1

### AG-D-03.1-001 — Identity Lifecycle Management

**Description (multi-paragraph):**

**Context:** Identity lifecycle management meets CRA Art. 13(2) secure-by-default kiosk identity config, NIS 2 Art. 21(2)(i) joiner-mover-leaver discipline, and GDPR Art. 30 controller capacity. Native IAM (dedicated identity governance platform/dedicated identity provider) is mandatory — Firebase INHERIT pattern is NOT used because biometric data scope requires dedicated identity. provisioning protocol provisioning plus quarterly access reviews cover the discipline.

**Scope:** All human identities with access to biometric-data scopes or on-device matching pipelines. The objective includes leaver event propagation within 24h and joiner event provisioning within 24h.

**Boundaries:** Out of scope: multi-factor authentication mechanism (D-03.2), authorisation model (D-03.3), and secure defaults (D-03.4). Edge cases: contractor identities require elevated exit-event review and may have separate retention rules.

**Source Article:** CRA Art. 13(2) | NIS 2 Art. 21(2)(i) | GDPR Art. 30
**NIST CSF Anchors:** PR.AA-01, PR.AA-02, PR.AA-03
**Verification Criteria (operational):**
- Native IAM (dedicated identity governance platform/dedicated identity provider) deployed with provisioning protocol provisioning; Firebase INHERIT pattern NOT used
- Quarterly access reviews cover all biometric-data scopes with documented sign-off by DPO
- Joiner-mover-leaver lifecycle discharged via provisioning protocol for joiner events within 24h of HR record creation

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-03.2 (multi-factor authentication), D-03.3 (authorisation)
**Risk if not met:** HIGH — Orphaned accounts access biometric data; GDPR Art. 32 + CRA Art. 13(2) failure
**Affected Stakeholders:** Internal: All employees with biometric access, Internal: HR, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-03.2-001 — Multi-Factor Authentication

**Description (multi-paragraph):**

**Context:** Multi-factor authentication for biometric-data scopes meets CRA Art. 13(2) secure installation multi-factor authentication, NIS 2 Art. 21(2)(g) training coverage, and GDPR Art. 32(1) appropriate-and-proportionate multi-factor authentication. Hardware multi-factor authentication tokens (hardware-backed second-factor authenticator/hardware-backed second-factor authenticator) satisfy the strictest phishing-resistant requirement; SMS+time-based one-time password is allowed for read-only scopes only.

**Scope:** All human identities with admin or write access to biometric-data scopes. Kiosk admin access requires hardware multi-factor authentication. Read-only scopes may use SMS+time-based one-time password fallback.

**Boundaries:** Out of scope: identity lifecycle (D-03.1), authorisation model (D-03.3), and audit logging (D-10.2). Edge cases: emergency break-glass accounts must be logged (D-10.2) and reviewed (D-03.1).

**Source Article:** CRA Art. 13(2) | NIS 2 Art. 21(2)(g) | GDPR Art. 32(1)
**NIST CSF Anchors:** PR.AA-01, PR.AA-03, PR.AA-05
**Verification Criteria (operational):**
- Hardware multi-factor authentication (hardware-backed second-factor authenticator/hardware-backed second-factor authenticator) required for all kiosk admin access; SMS+time-based one-time password only for read-only scopes
- Phishing-resistant multi-factor authentication enforced at the policy layer; legacy factors documented and excluded
- multi-factor authentication coverage report demonstrates 100% of biometric-data admin roles enrolled in hardware multi-factor authentication

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-03.1 (identity), D-03.4 (secure defaults)
**Risk if not met:** HIGH — Credential compromise on biometric scopes; Art. 9 + ISO 27001 A.9.4 failure
**Affected Stakeholders:** Internal: All employees with biometric access, Internal: CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-03.3-001 — Authorisation & Least Privilege

**Description (multi-paragraph):**

**Context:** Authorisation and least privilege meet NIS 2 Art. 21(2)(i) access control policy, GDPR Art. 5(1)(c) data minimisation principle, and CRA secure-by-default via D-03.4. role-based access control + attribute-based access control + segregation of duties enforced on a single access-management artefact.

**Scope:** All biometric-data scopes and on-device matching pipeline access. Operator vs auditor separation of duties enforced via named-role conflict matrix. attribute-based access control binds access to purpose (e.g., investigation, audit, support).

**Boundaries:** Out of scope: identity lifecycle (D-03.1), multi-factor authentication mechanism (D-03.2), and audit logging (D-10.2). Edge cases: read-only audit access for legal counsel may require named-role carve-out with documented justification.

**Source Article:** NIS 2 Art. 21(2)(i) | GDPR Art. 5(1)(c) + Art. 32(1)(b)
**NIST CSF Anchors:** PR.AA-01, PR.AA-03, PR.AA-05
**Verification Criteria (operational):**
- role-based access control with least-privilege for kiosk operators; attribute-based access control for biometric-data access (purpose-bound)
- Segregation of duties between operator and auditor enforced via named-role conflict matrix
- Quarterly access review captured per ISO 27001 A.9 with biometric-data scope coverage

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-03.1 (identity), D-10.2 (audit log)
**Risk if not met:** HIGH — Privilege escalation on biometric data; GDPR Art. 5(1)(c) + NIS 2 Art. 21(2)(i) failure
**Affected Stakeholders:** Internal: All employees with biometric access, Internal: CISO, DPO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-03.4-001 — Secure System Defaults

**Description (multi-paragraph):**

**Context:** Secure system defaults meet CRA Art. 13(2) secure-by-default kiosk config and GDPR Art. 25(2) privacy by default. Debug ports disabled, default passwords rotated, signed firmware required. Privacy-by-default check confirms GDPR Art. 25(2) data minimisation defaults applied at kiosk deployment.

**Scope:** All eGate kiosk configuration settings and default user/role provisioning. The objective includes any device shipped to airport operators.

**Boundaries:** Out of scope: identity lifecycle (D-03.1), multi-factor authentication mechanism (D-03.2), and authorisation model (D-03.3). Edge cases: kiosk configurations for non-airport venues (e.g., border-crossing buildings) may have additional default settings validated separately.

**Source Article:** CRA Art. 13(2) | GDPR Art. 25(2)
**NIST CSF Anchors:** PR.PS-01, PR.DS-10
**Verification Criteria (operational):**
- CRA secure-by-default kiosk config document: debug ports disabled, default passwords rotated, signed firmware required
- Auto-configuration verification in CI gates any commit that re-enables debug ports or default credentials
- Privacy-by-default check confirms GDPR Art. 25(2) data minimisation defaults applied at kiosk deployment

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** IN_PROGRESS
**Dependencies:** D-07.3 (CI/CD pipeline), D-03.1 (identity)
**Risk if not met:** MEDIUM — Default credentials/product config exploitable; CRA Art. 13(2) + GDPR Art. 25(2) failure
**Affected Stakeholders:** Travelers (data subjects), Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-04.1-001 — Incident Detection & Triage

**Description (multi-paragraph):**

**Context:** Incident detection and triage meets CRA Art. 14(3) severe-incident detection, NIS 2 Art. 21(2)(g) continuous monitoring, AI_Act Art. 72 post-market monitoring + Art. 73 serious-incident, and GDPR Art. 32(1)(d) regular testing. 24/7 SOC with Security Information and Event Management + AI-driven anomaly detection on on-device pipeline. Personal-data breach detection includes biometric-data breach (CRA Art. 14(3) severe incident) handling.

**Scope:** All events on the eGate stack, on-device pipeline, and back-end services. The objective includes AI model drift detection as a separate signal class.

**Boundaries:** Out of scope: incident containment (D-04.2), notification (D-04.3), recovery (D-04.4), and audit logging (D-10.2). Edge cases: anonymous incidents (no personal data) follow the same triage but have limited notification obligations.

**Source Article:** CRA Art. 14(3) | NIS 2 Art. 21(2)(g) | AI_Act Art. 72 + Art. 73 | GDPR Art. 32(1)(d)
**NIST CSF Anchors:** DE.CM-01, DE.CM-09, DE.AE-02
**Verification Criteria (operational):**
- 24/7 SOC with Security Information and Event Management integrating on-device anomaly detection; mean-time-to-detect (MTTD) tracked quarterly
- Incident playbooks per scenario include biometric-data breach (CRA Art. 14(3) severe incident) handling
- Detection capability tested annually via incident response exercise with documented detection outcomes

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-10.1 (continuous monitoring), D-10.2 (audit log)
**Risk if not met:** HIGH — Delayed incident detection; CRA Art. 14(3) severe-incident + AI_Act Art. 73 failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA, CSIRT), Internal: CISO, SOC
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-04.2-001 — Incident Containment & Response

**Description (multi-paragraph):**

**Context:** Incident containment and response meets CRA Art. 14(3) severe-incident containment + Art. 21 manufacturer-equivalent trigger, NIS 2 Art. 21(2)(c) business continuity, and GDPR Art. 32(1)(c) restore in timely manner. Documented documented incident response procedure (GDPR Art. 32 processor-side) + chain-of-custody evidence pack + CSIRT coordination procedure.

**Scope:** All confirmed-or-suspected personal-data and security incidents. The objective includes the chain-of-custody log per incident and the CSIRT coordination checklist.

**Boundaries:** Out of scope: detection (D-04.1), notification (D-04.3), recovery (D-04.4), and audit logging (D-10.2). Edge cases: government-controlled incidents (where government is controller) require controller-coordinated containment.

**Source Article:** CRA Art. 14(3) + Art. 21 | NIS 2 Art. 21(2)(c) | GDPR Art. 32(1)(c)
**NIST CSF Anchors:** RS.MI-01, RS.MI-02, RC.RP-01
**Verification Criteria (operational):**
- Documented documented incident response procedure covers GDPR Art. 32 processor-side containment and CRA Art. 14(3) severe-incident
- Chain-of-custody evidence pack template validated by Legal Counsel; sample pack on file
- CSIRT coordination procedure with named contacts and back-up channels tested in last tabletop

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-04.1 (detection), D-04.3 (notification)
**Risk if not met:** HIGH — Uncontained breach spreads; GDPR Art. 32(1)(c) + CRA Art. 14(3) failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA), Internal: CISO, SOC, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-04.3-001 — Incident Notification & Reporting

**Description (multi-paragraph):**

**Context:** Incident notification and reporting meets GDPR Art. 33(2) processor→controller without undue delay + Art. 33(1) controller→SA 72h, CRA Art. 14(1-2) AEV + Art. 14(3) severe-incident + Art. 14(8) user notification, NIS 2 Art. 23(4)(a) significant-incident, and AI_Act Art. 73(2-4) 3-tier serious-incident. Multi-reg max-SLA 24h routing resolves T-001 (4-reg temporal conflict). CEO/board liability per NIS 2 Art. 20.

**Scope:** All confirmed incidents requiring external notification. The scope includes the routing pipeline, per-recipient evidence packs, and the 24h clock governance.

**Boundaries:** Out of scope: detection (D-04.1), containment (D-04.2), and recovery (D-04.4). Edge cases: incidents where the controller (government) requests delayed notification require delay-grounds documentation per CRA Art. 14(2).

**Source Article:** GDPR Art. 33(2) + Art. 33(1) | CRA Art. 14(1-2) + Art. 14(3) + Art. 14(8) | NIS 2 Art. 23(4)(a) | AI_Act Art. 73(2-3)
**NIST CSF Anchors:** RS.CO-02, RS.MA-01, RS.MA-01
**Verification Criteria (operational):**
- Multi-reg max-SLA 24h notification routing pipeline tested quarterly with all four recipients (DPA / MSA / CSIRT / Notified Body)
- AI_Act 2-day widespread-infringement sub-workflow demonstrably triggered within 4h of incident categorisation
- Tabletop exercise demonstrates 24h delivery to DPA, ENISA, CSIRT, and Notified Body on a single timeline

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-04.1 (detection), D-04.2 (containment), D-10.2 (audit log)
**Risk if not met:** CRITICAL — Late notification to 4 regulators; GDPR Art. 83(4) + CRA Art. 56 + NIS 2 Art. 20 management liability + AI_Act Art. 99 fines
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA, CSIRT, Notified Body), Internal: CEO, CISO, DPO, Legal
**Maturity Score:** Current 2/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-04.4-001 — Incident Recovery & Lessons Learned

**Description (multi-paragraph):**

**Context:** Incident recovery and lessons-learned meets NIS 2 Art. 21(2)(c) business continuity + Art. 21(2)(d) supply-chain DR, CRA Art. 13(13) technical documentation retention, and GDPR Art. 32(1)(b)(c) restore availability and access in timely manner. RTO 24h, RPO 1h; immutable backup with 10-year retention; quarterly restore drill (ISO 27001 A.17).

**Scope:** All eGate stack components and back-end services. The objective includes the lessons-learned report within 30 days of every significant incident.

**Boundaries:** Out of scope: detection (D-04.1), containment (D-04.2), and notification (D-04.3). Edge cases: cross-region failover adds 4h to RTO but must be validated separately.

**Source Article:** NIS 2 Art. 21(2)(c) + Art. 21(2)(d) | CRA Art. 13(13) | GDPR Art. 32(1)(b)(c)
**NIST CSF Anchors:** RC.RP-01, RC.RP-03, RC.RP-04
**Verification Criteria (operational):**
- RTO 24h, RPO 1h demonstrated via quarterly restore drill with documented evidence of time-to-restore
- Immutable backup with 10-year retention anchored to CRA Art. 13(13) and NIS 2 Art. 21(2)(c)
- Lessons-learned report produced within 30 days of every significant incident with management review

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-04.2 (containment), D-09.1 (policies)
**Risk if not met:** HIGH — Extended downtime; NIS 2 Art. 21(2)(c) BCP + 10y retention breach
**Affected Stakeholders:** Travelers (data subjects), Airport operators, Internal: CISO, CTO, Operations
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-05.1-001 — Data Minimisation

**Description (multi-paragraph):**

**Context:** Data minimisation meets GDPR Art. 5(1)(c) data minimisation principle, CRA Art. 13(3) intended purpose + Art. 13(5) supply-chain data minimisation, and AI_Act Art. 10 data governance. Personal-data minimisation enforced at field-level in schema; biometric reference data deleted after match (seconds, ephemeral); data minimisation review per release.

**Scope:** All data fields collected at the eGate kiosk and propagated to the back-end. The objective includes any field marked for ephemeral processing.

**Boundaries:** Out of scope: retention policy (D-05.2), erasure (D-05.3), and portability (D-05.4). Edge cases: law-enforcement preservation requests may temporarily override minimisation with documented chain-of-custody.

**Source Article:** GDPR Art. 5(1)(c) | CRA Art. 13(3) + Art. 13(5) | AI_Act Art. 10
**NIST CSF Anchors:** PR.DS-10, ID.AM-03
**Verification Criteria (operational):**
- Field-level enforcement in schema rejects any field flagged for ephemeral processing (biometric reference data)
- biometric reference data deletion verified via hardware cryptographic module key destruction within seconds of match operation
- Data minimisation review per release with DPO sign-off demonstrates alignment with AI_Act Art. 10 + GDPR Art. 5(1)(c)

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** DONE
**Dependencies:** D-09.2 (DPIA), D-07.1 (secure-by-design)
**Risk if not met:** MEDIUM — Over-collection of biometric data; GDPR Art. 5(1)(c) + Art. 9 + AI_Act Art. 10
**Affected Stakeholders:** Travelers (data subjects), Internal: DPO, CTO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-05.2-001 — Retention & Archiving

**Description (multi-paragraph):**

**Context:** Retention and archiving meets GDPR Art. 5(1)(e) storage limitation, CRA Art. 13(13) technical documentation retention, and AI_Act Art. 19(1) at least six months automatic logging retention. Personal-data retention policy (per data type): biometric ephemeral; audit logs 10 years; watchlist per government policy.

**Scope:** All data classes held by SecureBorder. The objective includes the documented retention per class and the destruction verification.

**Boundaries:** Out of scope: data minimisation (D-05.1), erasure (D-05.3), and portability (D-05.4). Edge cases: AI_Act 10-year retention is above the Art. 19(1) floor — explicitly documented.

**Source Article:** GDPR Art. 5(1)(e) | CRA Art. 13(13) | AI_Act Art. 19(1) + Art. 12
**NIST CSF Anchors:** PR.DS-10, ID.AM-03, PR.PS-02
**Verification Criteria (operational):**
- Retention policy per data type: biometric ephemeral; audit logs 10 years; watchlist per government policy
- AI_Act Art. 19(1) ≥6-month automatic logging retention satisfied with 10y retention (above-floor)
- Quarterly retention audit demonstrates data destruction within policy windows

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** DONE
**Dependencies:** D-05.1 (minimisation), D-09.4 (RoPA)
**Risk if not met:** MEDIUM — Retention beyond policy; GDPR Art. 5(1)(e) + AI_Act Art. 19(1) floor
**Affected Stakeholders:** Travelers (data subjects), Internal: DPO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-05.3-001 — Right to Erasure

**Description (multi-paragraph):**

**Context:** Right to erasure meets GDPR Art. 17 erasure + Art. 19 notification obligation, and CRA Art. 13(5) deletes (cryptographic erasure where replicated) + Art. 13(8) without delay. Erasure endpoint + cryptographic sharding — destroy biometric↔identity mapping, retain anonymised audit trail (resolves T-002 GDPR Art. 17 vs AI_Act Art. 19(1) log retention — AI_Act Art. 12 governs transparency, NOT erasure; AI_Act is not a D-05.3 Right to Erasure participant).

**Scope:** All personal data subject to erasure requests. The objective includes the hardware cryptographic module key destruction mechanism and the anonymised audit trail.

**Boundaries:** Out of scope: data minimisation (D-05.1), retention (D-05.2), and portability (D-05.4). Edge cases: government-preserved records require controller-coordinated processing.

**Source Article:** GDPR Art. 17 + Art. 19 | CRA Art. 13(5) + Art. 13(8)
**NIST CSF Anchors:** PR.DS-10, PR.DS-10
**Verification Criteria (operational):**
- Erasure endpoint destroys biometric↔identity mapping via hardware cryptographic module key destruction (cryptographic sharding)
- Anonymised audit trail retained per AI_Act Art. 19(1) ≥6-month retention floor without re-identification (Art. 12 governs transparency; logging retention is D-10.2, not D-05.3)
- Right-to-erasure request fulfilled within GDPR Art. 12(3) one-month deadline

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** IN_PROGRESS
**Dependencies:** D-01.3 (key custody), D-10.2 (audit log)
**Risk if not met:** HIGH — Right-to-erasure failure; GDPR Art. 17 + Art. 83(5) fines + biometric Art. 9 sensitivity
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA), Internal: DPO, CISO
**Maturity Score:** Current 2/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-05.4-001 — Data Portability

**Description (multi-paragraph):**

**Context:** Data portability meets GDPR Art. 20 data portability right + Art. 20(3) machine-readable format. JSON export endpoint operational per Art. 20. Covers audit-log-controller capacity where legally required.

**Scope:** Personal data provided by the data subject or generated by the service. The objective includes the machine-readable format and the response time.

**Boundaries:** Out of scope: data minimisation (D-05.1), retention (D-05.2), and erasure (D-05.3). Edge cases: portability of derived inferences (e.g., watchlist match outcomes) is not in scope — only directly-provided or service-generated data.

**Source Article:** GDPR Art. 20
**NIST CSF Anchors:** PR.DS-10, PR.DS-10
**Verification Criteria (operational):**
- JSON export endpoint operational per GDPR Art. 20 with documented machine-readable format
- Data portability response time within 30 days for standard request; tested with 1 sample per release
- Audit-log-controller capacity supported alongside data portability where legally required

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** DONE
**Dependencies:** D-09.4 (RoPA)
**Risk if not met:** MEDIUM — Data portability failure; GDPR Art. 20 + Art. 83(4) fines
**Affected Stakeholders:** Travelers (data subjects), Internal: DPO, CTO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P2

### AG-D-06.1-001 — Vendor Risk Assessment

**Description (multi-paragraph):**

**Context:** Vendor risk assessment meets NIS 2 Art. 21(2)(d) supply-chain risk assessment + Art. 21(3) supplier-assessment three-prong, and GDPR Art. 28(1) sufficient guarantees. Personal-data processor (biometric sub-processor) agreements per GDPR Art. 28; due diligence on each processor covers Art. 28(1) sufficient guarantees; biometric-specific safeguards documented.

**Scope:** All tier-1 suppliers with access to biometric data or critical infrastructure. The objective includes annual supplier audit and per-processor due-diligence artefacts.

**Boundaries:** Out of scope: contractual security obligations (D-06.3), software bill of materials (D-06.2), and boundary management (D-06.4). Edge cases: government-supplied components are excluded from the software bill of materials gate but are in scope for the risk assessment.

**Source Article:** NIS 2 Art. 21(2)(d) + Art. 21(3) | GDPR Art. 28
**NIST CSF Anchors:** GV.SC-01, GV.SC-02, GV.SC-04
**Verification Criteria (operational):**
- NIS 2 Art. 21(2)(d) supplier risk assessment documented for each tier-1 supplier with annual refresh
- GDPR Art. 28(1) sufficient-guarantees due-diligence questionnaire + certification audit on file per biometric sub-processor
- Annual supplier audit demonstrates control coverage for tier-1 biometric and cloud suppliers

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-06.3 (contractual), D-06.4 (boundary)
**Risk if not met:** HIGH — Unmanaged supplier exposes biometric data; NIS 2 Art. 21(2)(d) + GDPR Art. 28 failure
**Affected Stakeholders:** Suppliers (biometric sub-processors), Regulators (DPA, CSIRT), Internal: CISO, Procurement, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-06.2-001 — Software Bill of Materials (software bill of materials)

**Description (multi-paragraph):**

**Context:** Software Bill of Materials meets CRA Art. 13(11) software bill of materials per release. machine-readable software bill of materials format format; signed software bill of materials attached to firmware; vulnerability tracking against software bill of materials is the only applicable regulatory floor (CRA is the sole authority at D-06.2). Personal-data exposure from vulnerable components is mitigated by the software bill of materials-anchored vulnerability tracking (D-02.1).

**Scope:** All OSS and commercial components in the eGate firmware. The objective includes the per-release software bill of materials and the CVE-to-component mapping.

**Boundaries:** Out of scope: vendor risk assessment (D-06.1), contractual obligations (D-06.3), and patching (D-02.2). Edge cases: AI model components may require model-bill-of-materials (MBOM) separately documented.

**Source Article:** CRA Art. 13(11)
**NIST CSF Anchors:** ID.AM-02, GV.SC-02
**Verification Criteria (operational):**
- machine-readable software bill of materials format software bill of materials per release generated, signed, and attached to firmware artefact
- Vulnerability tracking against software bill of materials with documented CVE-to-component mapping for every disclosed vuln
- CRA Art. 13(11) software bill of materials-anchored vulnerability tracking demonstrated for last 3 releases

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** DONE
**Dependencies:** D-02.1 (vuln ID), D-07.3 (CI/CD)
**Risk if not met:** MEDIUM — Untracked OSS vulnerability; CRA Art. 13(11) + unexpected CVE exposure
**Affected Stakeholders:** Suppliers (OSS, commercial), Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-06.3-001 — Contractual Security Obligations

**Description (multi-paragraph):**

**Context:** Contractual security obligations meet NIS 2 Art. 21(2)(d) contractual chain + Art. 21(3) supplier assessment three-prong, and GDPR Art. 28(3) 8-element DPA list + Art. 46 transfer safeguards. Personal-data contractual chain via DPA template + supplier security clauses; GDPR Art. 28(3) 8-element DPA list enforced; multi-tier sub-processor flowdown; right-to-audit clauses.

**Scope:** All processor contracts and supplier security clauses. The objective includes the DPA template, sub-processor flowdown clauses, and audit rights.

**Boundaries:** Out of scope: vendor risk assessment (D-06.1), software bill of materials (D-06.2), and boundary management (D-06.4). Edge cases: government procurement contracts may require carve-out for standard government terms with documented residual risk.

**Source Article:** NIS 2 Art. 21(2)(d) + Art. 21(3) | GDPR Art. 28(3) + Art. 46
**NIST CSF Anchors:** GV.SC-02, GV.SC-03, GV.SC-04
**Verification Criteria (operational):**
- DPA template with GDPR Art. 28(3) 8-element list enforced across all processor contracts
- NIS 2 Art. 21(2)(d) contractual chain with multi-tier sub-processor flowdown and right-to-audit clauses
- Annual contract review demonstrates compliance with GDPR Art. 46 transfer safeguards for non-EU suppliers

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-06.1 (vendor risk), D-09.4 (RoPA)
**Risk if not met:** HIGH — Sub-processor breach without DPA; GDPR Art. 28(3) + Art. 46 transfer safeguards failure
**Affected Stakeholders:** Suppliers (all processors), Regulators (DPA, CSIRT), Internal: CISO, Legal, Procurement
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-06.4-001 — Third-Party Boundary Management

**Description (multi-paragraph):**

**Context:** Third-party boundary management meets NIS 2 Art. 21(2)(d) supply-chain boundary + Art. 21(2)(e) network security, and CRA Annex I Part I (2)(e) state-of-the-art transit. Personal-data boundary management via network segmentation (SecureBorder/Cloud/Government); mutual transport authentication on all boundaries; zero-trust kiosk↔cloud; documented per GDPR Art. 32(1)(b) ongoing confidentiality.

**Scope:** All network boundaries between SecureBorder, cloud, and government back-end. The objective includes the segmentation policy and the zero-trust enforcement.

**Boundaries:** Out of scope: vendor risk assessment (D-06.1), software bill of materials (D-06.2), and contractual obligations (D-06.3). Edge cases: emergency remote access requires documented break-glass procedure with elevated logging.

**Source Article:** NIS 2 Art. 21(2)(d) + Art. 21(2)(e) | CRA Annex I Part I (2)(e) | GDPR Art. 32(1)(b)
**NIST CSF Anchors:** GV.SC-02, GV.SC-03, GV.SC-04
**Verification Criteria (operational):**
- Network segmentation between SecureBorder / Cloud / Government validated via pen-test verification
- mutual transport authentication enforced on all boundaries; zero-trust kiosk↔cloud architecture verified quarterly
- Documented network topology reviewed annually against NIS 2 Art. 21(2)(e) network security baseline

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** DONE
**Dependencies:** D-06.1 (vendor risk), D-01.2 (transit)
**Risk if not met:** HIGH — Lateral movement from compromised boundary; NIS 2 Art. 21(2)(e) + AI_Act Art. 15
**Affected Stakeholders:** Government back-end, Cloud providers, Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-07.1-001 — Secure-by-Design Principles

**Description (multi-paragraph):**

**Context:** Secure-by-design principles meet AI_Act Art. 9 risk-management + Art. 13 transparency + Art. 14 human oversight, CRA Art. 13(1)+(2) secure-by-default + risk assessment propagation across 6 lifecycle phases, and GDPR Art. 25(1) privacy by design. Personal-data protection by design via privacy-by-design integrated with AI_Act risk management system; unified SDLC covers high-risk AI; threat modelling per feature (STRIDE + AI-specific extensions).

**Scope:** All SecureBorder features and products. The objective includes threat modelling per feature and the AI_Act risk-management system implementation.

**Boundaries:** Out of scope: secure coding practices (D-07.2), CI/CD pipeline security (D-07.3), and information security policies (D-09.1). Edge cases: features added via partnership or acquisition require separate re-modelling within the integration timeline.

**Source Article:** AI_Act Art. 9 + Art. 13 + Art. 14 | CRA Art. 13(1) + Art. 13(2) | GDPR Art. 25(1) + Art. 35
**NIST CSF Anchors:** PR.PS-06, PR.PS-02, PR.PS-01
**Verification Criteria (operational):**
- AI_Act risk management system (Art. 9) documented with iterative risk assessment across 6 lifecycle phases
- CRA Art. 13(1)+(2) secure-by-default design verified via threat modelling per feature (STRIDE + AI extensions)
- Unified SDLC for high-risk AI gates code merge on privacy-by-design (GDPR Art. 25(1)) checks

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CTO
**Status:** IN_PROGRESS
**Dependencies:** D-09.2 (DPIA), D-07.2 (secure coding)
**Risk if not met:** HIGH — Insecure high-risk AI in production; AI_Act Art. 9 + Art. 13 + Art. 14 failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (AI Supervisory Authority, ENISA, DPA), Internal: CTO, AI Governance Lead, DPO
**Maturity Score:** Current 2/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-07.2-001 — Secure Coding Practices

**Description (multi-paragraph):**

**Context:** Secure coding practices meet CRA Annex I Part I (2)(c) attack-surface minimisation, AI_Act Art. 15 robustness, and NIS 2 Art. 21(2)(d) supply-chain security. static application security testing (static application security testing tool) + dynamic application security testing in CI; pre-commit secret scanning; application security maturity model at industry-standard level for AI components. Personal-data protection from vulnerable code is discharged via the secure-coding controls themselves.

**Scope:** All code in the eGate stack and back-end services. The objective includes the secure coding standards and the CI gating.

**Boundaries:** Out of scope: secure-by-design (D-07.1), CI/CD pipeline (D-07.3), and patch management (D-02.2). Edge cases: AI model code (e.g., inference wrappers) follows the same standards but with additional model-specific checks.

**Source Article:** CRA Annex I Part I (2)(c) | AI_Act Art. 15 | NIS 2 Art. 21(2)(d)
**NIST CSF Anchors:** PR.PS-06, PR.PS-02, PR.PS-01
**Verification Criteria (operational):**
- static application security testing (static application security testing tool) + dynamic application security testing in CI blocking merge on high-severity findings
- application security maturity model at industry-standard level secure coding standards applied for AI components with documented verification
- Pre-commit secret scanning demonstrated to catch 100% of test tokens in last regression exercise

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** DONE
**Dependencies:** D-07.1 (secure-by-design), D-07.3 (CI/CD)
**Risk if not met:** MEDIUM — Vulnerable code in production; CRA Annex I Part I (2)(c) + AI_Act Art. 15
**Affected Stakeholders:** Travelers (data subjects), Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-07.3-001 — CI/CD Pipeline Security

**Description (multi-paragraph):**

**Context:** CI/CD pipeline security meets NIS 2 Art. 21(2)(d) supply-chain security and CRA Art. 13(11) software bill of materials. Signed CI artefacts + pipeline-as-code + supply-chain integrity controls Level 3; software bill of materials gate blocks on critical vulns. Personal-data integrity through the pipeline is protected by the pipeline-security controls themselves (signed artefacts, software bill of materials gate).

**Scope:** All CI/CD pipelines producing eGate firmware and back-end artefacts. The objective includes the supply-chain integrity controls Level 3 evidence and the software bill of materials gate.

**Boundaries:** Out of scope: secure-by-design (D-07.1), secure coding (D-07.2), and software bill of materials (D-06.2). Edge cases: emergency hotfix pipelines may bypass the software bill of materials gate but require documented exception and accelerated remediation.

**Source Article:** NIS 2 Art. 21(2)(d) | CRA Art. 13(11)
**NIST CSF Anchors:** PR.PS-02, ID.RA-01, PR.PS-06
**Verification Criteria (operational):**
- Signed CI artefacts with pipeline-as-code; supply-chain integrity controls Level 3 evidence generated per release
- software bill of materials gate blocks release on critical/high CVE without documented exception
- NIS 2 SDLC pipeline security attested in annual ISO 27001 surveillance audit

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CTO
**Status:** IN_PROGRESS
**Dependencies:** D-06.2 (software bill of materials), D-02.1 (vuln ID)
**Risk if not met:** HIGH — Supply-chain attack via CI/CD; NIS 2 Art. 21(2)(d) + CRA Art. 13(11) failure
**Affected Stakeholders:** Regulators (ENISA, CSIRT), Internal: CTO, CISO
**Maturity Score:** Current 2/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-08.1-001 — General Security Awareness

**Description (multi-paragraph):**

**Context:** General security awareness meets NIS 2 Art. 21(2)(e) basic cyber hygiene + Art. 21(2)(g) training, CRA Art. 13(2) installation/use training, and GDPR Art. 39 DPO-informed training. Annual security awareness training includes GDPR-specific module (data subject rights, breach recognition, biometric-data handling); phishing simulation quarterly; kiosk-specific security guide; documented per GDPR Art. 39.

**Scope:** All SecureBorder employees handling eGate kiosk operations or biometric data. The objective includes the GDPR-specific module and the phishing simulation cadence.

**Boundaries:** Out of scope: role-specific competence (D-08.2). Edge cases: contractor workforce may require condensed training with documented compliance.

**Source Article:** NIS 2 Art. 21(2)(e) + Art. 21(2)(g) | CRA Art. 13(2) | GDPR Art. 39
**NIST CSF Anchors:** PR.AT-01, PR.AT-02, PR.PS-01
**Verification Criteria (operational):**
- Annual security awareness training covers GDPR, NIS 2, and CRA with documented module completion
- Phishing simulation quarterly with click-rate tracked and reported to CISO
- Kiosk-specific security guide distributed to all kiosk operators with annual refresh

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-09.1 (policies)
**Risk if not met:** MEDIUM — Social engineering compromise; NIS 2 Art. 21(2)(g) + GDPR Art. 39(1)(b) failure
**Affected Stakeholders:** Internal: All employees, Internal: CISO, HR
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-08.2-001 — Role-Specific Competence

**Description (multi-paragraph):**

**Context:** Role-specific competence meets NIS 2 Art. 21(2)(g) role-specific competence, AI_Act Art. 4 AI literacy + Art. 14 human oversight, and GDPR Art. 37(1)(c) DPO mandatory + Art. 39(1)(b) DPO awareness. DPO role-specific competence (Art. 37(1)(c) mandatory) — DPO training + AI Governance Lead training per AI_Act Art. 14 human oversight + SOC analyst certification; continuing professional education.

**Scope:** All Security, Privacy, AI, and SOC roles. The objective includes the certification maintenance and the continuing education hours.

**Boundaries:** Out of scope: general security awareness (D-08.1). Edge cases: management board training is handled at the board briefing level (Doc 04 §3.2 + §10.3) — not a training-based competency.

**Source Article:** NIS 2 Art. 21(2)(g) | AI_Act Art. 4 + Art. 14 | GDPR Art. 37(1)(c) + Art. 39(1)(b)
**NIST CSF Anchors:** PR.AT-02, PR.AT-01, GV.RR-02
**Verification Criteria (operational):**
- DPO training refresh annual; AI Governance Lead per AI_Act Art. 14 human oversight
- SOC analyst certification (GCIH/equivalent) maintained for ≥80% of SOC team
- Continuing professional education hours documented per Art. 4 AI literacy requirement

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-08.1 (awareness), D-09.1 (policies)
**Risk if not met:** MEDIUM — Unqualified role-holder; AI_Act Art. 4 + Art. 14 + DPO Art. 37(1)(c) failure
**Affected Stakeholders:** Internal: Security, Privacy, AI, SOC roles, Internal: CISO, DPO, HR
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-09.1-001 — Information Security Policies

**Description (multi-paragraph):**

**Context:** Information security policies meet AI_Act Art. 9 risk-management policies + Art. 13 transparency policies, CRA Art. 13(8) support policies, NIS 2 Art. 21(1) framework policies, and GDPR Art. 5(2) accountability + Art. 24 controller responsibility. Personal-data policies integrated in ISO 27001 certified ISMS (Doc 04 §10.4); unified policies with regulation-specific annexes; annual surveillance audit; DPO oversight.

**Scope:** All SecureBorder policies and procedures. The objective includes the AI_Act risk-management and transparency policies.

**Boundaries:** Out of scope: impact assessments (D-09.2), records of processing (D-09.4), and policies for specific sub-domains (D-08.x). Edge cases: government-mandated policies may require explicit acknowledgement with documented residual risk.

**Source Article:** AI_Act Art. 9 + Art. 13 | CRA Art. 13(8) | NIS 2 Art. 21(1) | GDPR Art. 5(2) + Art. 24
**NIST CSF Anchors:** GV.PO-01, GV.PO-02, GV.RR-02
**Verification Criteria (operational):**
- ISO 27001 certified ISMS policies current with annual surveillance audit passing
- AI_Act Art. 9 risk-management policies + Art. 13 transparency policies documented
- Unified policy set with regulation-specific annexes for GDPR + CRA + NIS 2 + AI_Act

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-09.2 (DPIA), D-09.4 (RoPA)
**Risk if not met:** LOW — ISO 27001 certified; policies maintained; failure unlikely
**Affected Stakeholders:** Regulators (DPA, ENISA, CSIRT, AI Supervisory Authority), Internal: CISO, DPO, Legal
**Maturity Score:** Current 4/4 → Target 4/4
**Implementation Priority:** P2

### AG-D-09.2-001 — Impact & Risk Assessments

**Description (multi-paragraph):**

**Context:** Impact and risk assessments meet GDPR Art. 35 DPIA, AI_Act Art. 27 FRIA + Art. 9 risk-management, CRA Art. 13(2) risk assessment, and NIS 2 Art. 21(1) risk analysis. Personal-data impact assessment via unified DPIA (GDPR Art. 35) + FRIA (AI_Act Art. 27) single process with dual output; cross-impact CRDA analysis; threshold-trigger criteria per Art. 35(3) and Art. 27(1) (resolves T-003).

**Scope:** All SecureBorder products and processing operations. The objective includes the unified DPIA+FRIA process and the dual output.

**Boundaries:** Out of scope: information security policies (D-09.1), records of processing (D-09.4), and compliance testing (D-10.3). Edge cases: rapid-deployment features may require abbreviated assessment with documented residual risk.

**Source Article:** GDPR Art. 35 | AI_Act Art. 27 + Art. 9 | CRA Art. 13(2) | NIS 2 Art. 21(1)
**NIST CSF Anchors:** ID.RA-01, ID.RA-04, ID.RA-05
**Verification Criteria (operational):**
- Unified DPIA + FRIA single process with dual output documented per GDPR Art. 35 + AI_Act Art. 27
- Threshold-trigger criteria per GDPR Art. 35(3) and AI_Act Art. 27(1) documented
- Annual impact assessment review with DPO + AI Governance Lead sign-off

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** IN_PROGRESS
**Dependencies:** D-09.1 (policies), D-09.4 (RoPA)
**Risk if not met:** HIGH — DPIA/FRIA missing for high-risk AI; GDPR Art. 35(3) + AI_Act Art. 27(1) failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, AI Supervisory Authority), Internal: DPO, AI Governance Lead, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-09.4-001 — Records of Processing

**Description (multi-paragraph):**

**Context:** Records of processing meet GDPR Art. 30 RoPA, AI_Act Art. 12 record-keeping, CRA Art. 13(12) technical documentation, and NIS 2 Art. 21(2)(a) risk-assessment records. Records of processing activities (RoPA) cover personal-data processing per GDPR Art. 30; DPO oversight; immutable storage; 10-year retention.

**Scope:** All processing activities involving personal data. The objective includes the immutable storage and the 10-year retention.

**Boundaries:** Out of scope: information security policies (D-09.1), impact assessments (D-09.2), and audit logging (D-10.2). Edge cases: government-controlled processing requires controller-coordinated RoPA entry.

**Source Article:** GDPR Art. 30 | AI_Act Art. 12 | CRA Art. 13(12) | NIS 2 Art. 21(2)(a)
**NIST CSF Anchors:** ID.AM-08, PR.DS-10, GV.PO-02
**Verification Criteria (operational):**
- RoPA covering all 4 applicable regulations with immutable storage and 10-year retention
- DPO oversight on RoPA updates; quarterly reconciliation with AI_Act Art. 12 record-keeping
- GDPR Art. 30 records of processing activities current and accessible to supervisory authority on request

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** DONE
**Dependencies:** D-09.1 (policies), D-05.2 (retention)
**Risk if not met:** MEDIUM — Missing RoPA entry; GDPR Art. 30 + AI_Act Art. 12 record-keeping failure
**Affected Stakeholders:** Regulators (DPA, AI Supervisory Authority), Internal: DPO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-10.1-001 — Continuous Security Monitoring

**Description (multi-paragraph):**

**Context:** Continuous security monitoring meets AI_Act Art. 72 post-market monitoring + Art. 73 serious-incident detection, NIS 2 Art. 21(2)(g) continuous monitoring, CRA Art. 14(3) severe-incident detection, and GDPR Art. 32(1)(d) regular testing. Personal-data security monitoring via 24/7 SOC with Security Information and Event Management; AI-driven anomaly detection on on-device pipeline; biometric-data scope alerts; documented per GDPR Art. 32(1)(d).

**Scope:** All eGate stack components and back-end services. The objective includes the AI model drift detection and the serious-incident detection.

**Boundaries:** Out of scope: incident detection (D-04.1), audit logging (D-10.2), and compliance testing (D-10.3). Edge cases: 24/7 SOC must be staffed or contracted; minimum competency and clearance requirements apply.

**Source Article:** AI_Act Art. 72 + Art. 73 | NIS 2 Art. 21(2)(g) | CRA Art. 14(3) | GDPR Art. 32(1)(d)
**NIST CSF Anchors:** DE.CM-01, DE.CM-09, DE.AE-02
**Verification Criteria (operational):**
- 24/7 SOC with Security Information and Event Management + AI model drift detection; Uptime SLA ≥99.95% evidenced
- AI_Act Art. 72 post-market monitoring + Art. 73 serious-incident detection integrated on single Security Information and Event Management
- Quarterly NCR (non-conformity) review with documented remediation and effectiveness validation

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-04.1 (incident detection), D-10.2 (audit log)
**Risk if not met:** HIGH — AI model drift undetected; AI_Act Art. 72 + Art. 73 + NIS 2 Art. 21(2)(g) failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA, CSIRT, AI Supervisory Authority), Internal: CISO, SOC, AI Governance Lead
**Maturity Score:** Current 2/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-10.2-001 — Audit Logging & Traceability

**Description (multi-paragraph):**

**Context:** Audit logging and traceability meets AI_Act Art. 12 logging capability + Art. 19(1) at least six months automatic retention, CRA Art. 13(14) logging, NIS 2 Art. 21(2)(h) cryptography-policy logging, and GDPR Art. 5(2) accountability + Art. 30 controller capacity. Personal-data audit log via tamper-evident log (GDPR Art. 30 controller capacity); 10-year retention; cryptographic hash chain; documented per Art. 5(2).

**Scope:** All SecureBorder events with audit-relevant content. The objective includes the tamper-evident hash chain and the 10-year retention above the Art. 19(1) floor.

**Boundaries:** Out of scope: incident detection (D-04.1), records of processing (D-09.4), and compliance testing (D-10.3). Edge cases: high-volume streaming events may use tiered storage with hot/cold split.

**Source Article:** AI_Act Art. 12 + Art. 19(1) | CRA Art. 13(14) | NIS 2 Art. 21(2)(h) | GDPR Art. 5(2) + Art. 30
**NIST CSF Anchors:** PR.DS-01, PR.PS-04, DE.CM-01
**Verification Criteria (operational):**
- Tamper-evident audit log with cryptographic hash chain; 10-year retention above AI_Act Art. 19(1) floor
- CRA Art. 13(14) logging + NIS 2 Art. 21(2)(h) cryptography-policy logging on single log artefact
- GDPR Art. 5(2) accountability principle demonstrated via quarterly audit log review

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-09.1 (policies), D-09.4 (RoPA)
**Risk if not met:** MEDIUM — Audit log tamper; GDPR Art. 5(2) accountability + AI_Act Art. 12 failure
**Affected Stakeholders:** Regulators (DPA, AI Supervisory Authority), Internal: CISO, DPO, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-10.3-001 — Compliance Testing

**Description (multi-paragraph):**

**Context:** Compliance testing meets AI_Act Art. 43 conformity assessment re-assessment + Art. 72 post-market re-evaluation, CRA Art. 24(3) OSS steward extension, NIS 2 Art. 21(2) controls test, and GDPR Art. 28(3)(h) processor audit + Art. 35(11) DPIA on material change. Personal-data compliance testing via annual ISO 27001 surveillance audit + DPIA re-assessment + GDPR Art. 35(11) review on material change; CISO sign-off.

**Scope:** All SecureBorder compliance obligations. The objective includes the annual ISO 27001 surveillance audit and the AI_Act conformity re-assessment.

**Boundaries:** Out of scope: continuous monitoring (D-10.1), audit logging (D-10.2), and information security policies (D-09.1). Edge cases: rapid-deployment material changes may require accelerated compliance testing with documented residual risk.

**Source Article:** AI_Act Art. 43 + Art. 72 | CRA Art. 24(3) | NIS 2 Art. 21(2) | GDPR Art. 28(3)(h) + Art. 35(11)
**NIST CSF Anchors:** PR.PS-02, ID.RA-05, DE.AE-02
**Verification Criteria (operational):**
- Annual ISO 27001 surveillance audit + AI_Act conformity re-assessment + NIS 2 controls test on integrated programme
- GDPR Art. 35(11) DPIA-on-change review executed for material changes
- CISO sign-off on annual compliance-test report with C-suite acknowledgement

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-09.1 (policies), D-10.1 (monitoring)
**Risk if not met:** MEDIUM — Compliance drift; ISO 27001 surveillance + AI_Act re-assessment failure
**Affected Stakeholders:** Regulators (DPA, ENISA, CSIRT, AI Supervisory Authority, Notified Body), Internal: CISO, DPO, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P2

### AG-D-01.1-002 — Data at Rest Encryption

**Description (multi-paragraph):**

**Context:** CRA Annex I Part I (2)(e) `render unintelligible` test is met via hardware cryptographic module-backed industry-standard authenticated encryption for all stored data on the eGate kiosk (personal or other per Art. 3(47) cross-reference). Annex VII technical documentation references the hardware cryptographic module architecture. NIS 2 Art. 21(2)(h) cryptography policy covers the at-rest dimension. CRA conformity assessment module selected per critical-product classification.

**Scope:** All stored data on the eGate kiosk population. The objective includes the Annex VII technical documentation and the conformity assessment module selection.

**Boundaries:** Out of scope: data in transit (D-01.2), key custody (D-01.3), and integrity (D-01.4). Edge cases: legacy lounges with pre-CRA hardware may require grandfather clause aligned with the 5-year support period.

**Source Article:** GDPR Art. 9(2)(g) + Art. 32(1)(a)/(b) | CRA Annex I Part I (2)(e) | NIS 2 Art. 21(2)(h)
**NIST CSF Anchors:** PR.DS-01
**Verification Criteria (operational):**
- industry-standard authenticated encryption (or stronger) cipher confirmed on every at-rest eGate kiosk datastore via cryptographic configuration audit
- CRA conformity assessment technical documentation (Annex VII) names hardware cryptographic module architecture per Annex I Part I (2)(e)
- Tamper-evident key-lineage log demonstrates every key creation, rotation, and destruction event tied to biometric key custodian

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-01.3 (key custody), D-02.1 (vuln identification)
**Risk if not met:** HIGH — Biometric data breach exposure; GDPR Art. 83(5) up to €20M or 4% turnover + CRA Art. 56 + AI_Act Art. 99 fines
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA, CSIRT), Internal: CISO, CTO, DPO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-01.2-002 — Data in Transit Encryption

**Description (multi-paragraph):**

**Context:** CRA Annex I Part I (2)(e) extends to data in transit with state-of-the-art mechanisms. NIS 2 Art. 21(2)(h) cryptography policy covers transit. The hardware cryptographic module-signed cert chain and cipher-suite allowlist discharge both on a single kiosk-edge artefact. CRA conformity assessment validates the transit encryption.

**Scope:** All transit links originating from or terminating at the eGate kiosk. The objective includes the cipher-allowlist and the certificate provisioning.

**Boundaries:** Out of scope: at-rest encryption (D-01.1), key custody (D-01.3), and integrity (D-01.4). Edge cases: emergency cryptographic revision may temporarily relax cipher-allowlist for transit but must be documented.

**Source Article:** GDPR Art. 32(1)(a)/(b) | CRA Annex I Part I (2)(e) | NIS 2 Art. 21(2)(h)
**NIST CSF Anchors:** PR.DS-02
**Verification Criteria (operational):**
- modern transport security with mutual transport authentication enforced on all kiosk↔cloud and kiosk↔government endpoints; cipher-allowlist documented and enforced
- hardware cryptographic module-signed certificate chain validated on every on-device↔backend link; weak ciphers (RC4, 3DES) absent from production
- Documented transit-encryption policy cites GDPR Art. 32(1)(a)/(b) and aligns with CRA Annex I Part I (2)(e)

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** DONE
**Dependencies:** D-01.3 (key custody), D-06.4 (boundary mgmt)
**Risk if not met:** HIGH — Man-in-the-middle attack on biometric data in transit; GDPR + CRA + NIS 2 fines
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA), Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-01.3-002 — Cryptographic Key Management

**Description (multi-paragraph):**

**Context:** CRA Annex I Part I (2)(e) state-of-the-art mechanisms baseline applies to key custody as well as ciphertext. The de-attribution test procedure is part of CRA conformity assessment technical documentation. NIS 2 Art. 21(2)(h) cryptography policy includes key custody.

**Scope:** All key material handling biometric data. The objective includes the de-attribution test procedure and the hardware cryptographic module architecture documentation.

**Boundaries:** Out of scope: cipher algorithm selection (D-01.1), integrity (D-01.4), and at-rest encryption (D-01.1). Edge cases: legacy key material may require grandfather key-rotation cadence aligned with the 5-year support period.

**Source Article:** GDPR Art. 4(5) + Art. 32(1)(a) | CRA Annex I Part I (2)(e) | NIS 2 Art. 21(2)(h)
**NIST CSF Anchors:** PR.DS-01, PR.AA-03, PR.AA-04, PR.AA-05
**Verification Criteria (operational):**
- hardware cryptographic module-anchored key custody demonstrably separated between biometric and non-biometric key material (functional role-based access control)
- Key-lineage logging to tamper-evident audit log captures every key lifecycle event with custodian identity
- De-attribution test procedure documented and executed at least once per year (GDPR Art. 4(5) pseudonymisation)

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-01.1 (at-rest), D-01.2 (transit)
**Risk if not met:** HIGH — Key compromise exposes every biometric reference data; Art. 9 + integrity principle breach
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA), Internal: CISO, DPO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-01.4-002 — Data Integrity Mechanisms

**Description (multi-paragraph):**

**Context:** AI_Act Art. 15 (accuracy + robustness + cybersecurity) requires data integrity for high-risk AI training/inference data. AI_Act Art. 10 (data governance) requires data-quality checks. CRA Annex I Part I (2)(d) integrity baseline discharged by cryptographic integrity check + signed audit log. NIS 2 Art. 21(2)(e) baseline on data integrity.

**Scope:** All biometric and watchlist records at the field level. The objective includes the AI_Act training-data integrity checks.

**Boundaries:** Out of scope: at-rest encryption (D-01.1), transit integrity (D-01.2), and key custody (D-01.3). Edge cases: AI training data integrity is verified separately from runtime inference data.

**Source Article:** GDPR Art. 5(1)(f) | CRA Annex I Part I (2)(d) | AI_Act Art. 10 + Art. 15
**NIST CSF Anchors:** PR.DS-01, PR.DS-02, PR.DS-10
**Verification Criteria (operational):**
- cryptographic integrity check-SHA256 (or stronger) integrity checks on all biometric and watchlist data with cryptographic verification
- DB constraints + signed audit log reject any biometric or watchlist record failing integrity checks
- Checksum validation executed on every data restore with evidence of test execution and pass/fail outcome

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** DONE
**Dependencies:** D-01.1 (at-rest), D-10.2 (audit log)
**Risk if not met:** MEDIUM — Tampered biometric data leads to false matches and integrity principle breach
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, AI Supervisory Authority), Internal: CTO, DPO
**Maturity Score:** Current 3/4 → Target 3/4
**Implementation Priority:** P0

### AG-D-02.1-002 — Vulnerability Identification

**Description (multi-paragraph):**

**Context:** CRA Art. 13(8) without delay vulnerability handling during support period; CRA Art. 14(1) actively-exploited vulnerability (AEV) reporting. NIS 2 Art. 21(2)(e) baseline on risk assessment. AI_Act Art. 9 risk-management system includes vulnerability identification. The dependency vulnerability scanner + npm audit + monthly vuln review board satisfies CRA software bill of materials-anchored vulnerability tracking on a single artefact.

**Scope:** All OSS components in the eGate stack. The objective includes the monthly vulnerability review board and the software bill of materials-anchored tracking.

**Boundaries:** Out of scope: vulnerability disclosure (D-02.3), patch implementation (D-02.2), and threat-led testing (D-02.4). Edge cases: government-supplied AI models are tracked but not patched by SecureBorder.

**Source Article:** CRA Art. 13(8) + Art. 14(1) | NIS 2 Art. 21(2)(e) | AI_Act Art. 9
**NIST CSF Anchors:** ID.RA-01, ID.RA-03
**Verification Criteria (operational):**
- dependency vulnerability scanner + npm audit scans integrated into CI with high-severity findings blocking merge gate
- Monthly vulnerability review board with CISO + CTO produces documented minutes and tracked remediation actions
- Vulnerability findings linked to the DPIA risk register per GDPR Art. 35 risk assessment

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-06.2 (software bill of materials), D-09.2 (DPIA risk link)
**Risk if not met:** HIGH — Unidentified CVE exploited; CRA Art. 14 AEV reporting + GDPR Art. 32(1)(d) failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (ENISA, CSIRT), Internal: CISO, CTO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-02.2-002 — Patch Management & Updates

**Description (multi-paragraph):**

**Context:** CRA-aligned patch SLA: critical 24h, high 7d (matches Doc 07 SI-002 24h max-SLA per T-001 resolution). Secure OTA update pipeline with hardware cryptographic module-signed firmware. CRA Art. 13(8) 5-year support period + Art. 13(9) 10-year update availability tail. NIS 2 Art. 21(2)(d) supply-chain security for firmware updates.

**Scope:** All eGate kiosks and back-end services. The objective includes the hardware cryptographic module-signed firmware and the OTA update pipeline.

**Boundaries:** Out of scope: vulnerability identification (D-02.1), vulnerability disclosure (D-02.3), and incident response (D-04.x). Edge cases: emergency out-of-band patches bypass the standard cadence but must still receive hardware cryptographic module signing.

**Source Article:** CRA Art. 13(8) + Art. 13(9)
**NIST CSF Anchors:** PR.PS-02, PR.IR-03
**Verification Criteria (operational):**
- Critical patch SLA ≤24h (CRA Art. 13(8) without delay) verified via patch-cadence report
- Secure OTA update pipeline with hardware cryptographic module-signed firmware images prevents rollback to unsigned versions
- Vulnerability tracking against software bill of materials detects newly disclosed CVEs within defined cadence

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** IN_PROGRESS
**Dependencies:** D-02.1 (vuln ID), D-06.2 (software bill of materials)
**Risk if not met:** HIGH — Unpatched critical CVE; CRA Art. 13(8) without delay breach + security update retention failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (ENISA), Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-02.3-002 — Coordinated Vulnerability Disclosure

**Description (multi-paragraph):**

**Context:** CRA Art. 14 single point of contact + Art. 16 dissemination with delay grounds. Security.txt at /.well-known/security.txt + CVD page + 24h acknowledgement SLA. CRA Art. 14(1-2) AEV reporting aligned with NIS 2 Art. 23(4)(a) on a single workflow.

**Scope:** All externally disclosed vulnerabilities affecting SecureBorder products. The objective includes the security.txt and the CVD page.

**Boundaries:** Out of scope: vulnerability identification (D-02.1), patch implementation (D-02.2), and incident notification (D-04.3). Edge cases: anonymised disclosures follow the same process but require additional investigator coordination.

**Source Article:** CRA Art. 14(1-2) + Art. 16 | NIS 2 Art. 23(4)(a)
**NIST CSF Anchors:** GV.PO-01, RS.CO-03
**Verification Criteria (operational):**
- security.txt published at /.well-known/security.txt with valid contact and 24h acknowledgement SLA
- CVD policy page lists ISO/IEC 29147 conformant disclosure process with translation to CRA Art. 14 reporting
- Receipt acknowledgement demonstrated within 24h for the most recent in-scope disclosure

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-02.1 (vuln ID), D-04.3 (incident reporting)
**Risk if not met:** MEDIUM — Unmanaged vulnerability disclosure; CRA Art. 14 AEV reporting failure
**Affected Stakeholders:** Researchers (security community), Regulators (ENISA, CSIRT), Internal: CISO, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-02.4-002 — Threat-Led Penetration Testing

**Description (multi-paragraph):**

**Context:** AI_Act Art. 9 risk-management system requires adversarial testing + robustness testing. AI_Act Art. 72 post-market monitoring feeds the threat-led pen test schedule. CRA Annex I Part I (2)(c) attack surface minimisation is tested via annual external pen test. certified penetration testing practitioners-accredited testers.

**Scope:** Annual external pen test + red team exercise on on-device matching pipeline. The objective includes the adversarial input testing and the biometric spoofing test.

**Boundaries:** Out of scope: vulnerability identification (D-02.1), patch management (D-02.2), and incident response (D-04.x). Edge cases: production vs. test environment separation must be validated separately.

**Source Article:** CRA Annex I Part I (2)(c) | AI_Act Art. 9 + Art. 72 | NIS 2 Art. 21(2)(e)
**NIST CSF Anchors:** ID.RA-01, ID.RA-04, PR.PS-06
**Verification Criteria (operational):**
- Annual external pen test by certified penetration testing practitioners-accredited testers with publicly available executive summary
- Red team exercise on on-device matching pipeline covers adversarial inputs, model poisoning, and biometric spoofing
- Threat-led pen test scope aligned with NIS 2 Art. 21(2)(e) and CRA Annex I Part I (2)(c)

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** IN_PROGRESS
**Dependencies:** D-02.1 (vuln ID), D-07.1 (secure-by-design)
**Risk if not met:** MEDIUM — Undiscovered attack surface; AI_Act Art. 9 risk-management + CRA Annex I (2)(c) failure
**Affected Stakeholders:** Travelers (data subjects), Internal: CTO, CISO, AI Governance Lead
**Maturity Score:** Current 2/4 → Target 3/4
**Implementation Priority:** P1

### AG-D-03.1-002 — Identity Lifecycle Management

**Description (multi-paragraph):**

**Context:** CRA Art. 13(2) secure-by-default kiosk identity config + CRA Art. 14(1) AEV scope covers compromised credentials. NIS 2 Art. 21(2)(i) joiner-mover-leaver lifecycle discharged via provisioning protocol on the same artefact. AI_Act Art. 14 human oversight requires identity lifecycle for oversight roles.

**Scope:** All human identities with access to biometric-data scopes. The objective includes the provisioning protocol provisioning and the quarterly access reviews.

**Boundaries:** Out of scope: multi-factor authentication mechanism (D-03.2), authorisation model (D-03.3), and secure defaults (D-03.4). Edge cases: contractor identities require elevated exit-event review.

**Source Article:** CRA Art. 13(2) | NIS 2 Art. 21(2)(i) | GDPR Art. 30
**NIST CSF Anchors:** PR.AA-01, PR.AA-02, PR.AA-03
**Verification Criteria (operational):**
- Native IAM (dedicated identity governance platform/dedicated identity provider) deployed with provisioning protocol provisioning; Firebase INHERIT pattern NOT used
- Quarterly access reviews cover all biometric-data scopes with documented sign-off by DPO
- Joiner-mover-leaver lifecycle discharged via provisioning protocol for joiner events within 24h of HR record creation

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-03.2 (multi-factor authentication), D-03.3 (authorisation)
**Risk if not met:** HIGH — Orphaned accounts access biometric data; GDPR Art. 32 + CRA Art. 13(2) failure
**Affected Stakeholders:** Internal: All employees with biometric access, Internal: HR, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-03.2-002 — Multi-Factor Authentication

**Description (multi-paragraph):**

**Context:** CRA Art. 13(2) secure installation requires multi-factor authentication on first-boot setup. NIS 2 Art. 21(2)(g) training covers multi-factor authentication. Hardware multi-factor authentication tokens (hardware-backed second-factor authenticator) discharge both on a single artefact. AI_Act Art. 14 human oversight requires multi-factor authentication for oversight roles.

**Scope:** All human identities with admin or write access. The objective includes the hardware multi-factor authentication tokens and the phishing-resistant requirement.

**Boundaries:** Out of scope: identity lifecycle (D-03.1), authorisation model (D-03.3), and audit logging (D-10.2). Edge cases: emergency break-glass accounts must be logged and reviewed.

**Source Article:** CRA Art. 13(2) | NIS 2 Art. 21(2)(g) | GDPR Art. 32(1)
**NIST CSF Anchors:** PR.AA-01, PR.AA-03, PR.AA-05
**Verification Criteria (operational):**
- Hardware multi-factor authentication (hardware-backed second-factor authenticator/hardware-backed second-factor authenticator) required for all kiosk admin access; SMS+time-based one-time password only for read-only scopes
- Phishing-resistant multi-factor authentication enforced at the policy layer; legacy factors documented and excluded
- multi-factor authentication coverage report demonstrates 100% of biometric-data admin roles enrolled in hardware multi-factor authentication

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-03.1 (identity), D-03.4 (secure defaults)
**Risk if not met:** HIGH — Credential compromise on biometric scopes; Art. 9 + ISO 27001 A.9.4 failure
**Affected Stakeholders:** Internal: All employees with biometric access, Internal: CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-03.3-002 — Authorisation & Least Privilege

**Description (multi-paragraph):**

**Context:** NIS 2 Art. 21(2)(i) access control policy + Art. 21(2)(d) supply-chain scope. role-based access control + attribute-based access control + separation of duties enforced on a single access-management artefact. CRA secure-by-default baseline via D-03.4. AI_Act Art. 14 human oversight requires purpose-bound access.

**Scope:** All biometric-data scopes and on-device matching pipeline access. The objective includes the named-role conflict matrix and the attribute-based access control binding.

**Boundaries:** Out of scope: identity lifecycle (D-03.1), multi-factor authentication mechanism (D-03.2), and audit logging (D-10.2). Edge cases: read-only audit access for legal counsel may require named-role carve-out.

**Source Article:** NIS 2 Art. 21(2)(i) | GDPR Art. 5(1)(c) + Art. 32(1)(b)
**NIST CSF Anchors:** PR.AA-01, PR.AA-03, PR.AA-05
**Verification Criteria (operational):**
- role-based access control with least-privilege for kiosk operators; attribute-based access control for biometric-data access (purpose-bound)
- Segregation of duties between operator and auditor enforced via named-role conflict matrix
- Quarterly access review captured per ISO 27001 A.9 with biometric-data scope coverage

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-03.1 (identity), D-10.2 (audit log)
**Risk if not met:** HIGH — Privilege escalation on biometric data; GDPR Art. 5(1)(c) + NIS 2 Art. 21(2)(i) failure
**Affected Stakeholders:** Internal: All employees with biometric access, Internal: CISO, DPO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-03.4-002 — Secure System Defaults

**Description (multi-paragraph):**

**Context:** CRA Art. 13(2) secure-by-default kiosk config: debug ports disabled, default passwords rotated, signed firmware required. CRA conformity assessment includes defaults check. AI_Act Art. 14 baseline on safe defaults.

**Scope:** All eGate kiosk configuration settings. The objective includes the auto-configuration verification in CI.

**Boundaries:** Out of scope: identity lifecycle (D-03.1), multi-factor authentication mechanism (D-03.2), and authorisation model (D-03.3). Edge cases: kiosk configurations for non-airport venues may have additional default settings.

**Source Article:** CRA Art. 13(2) | GDPR Art. 25(2)
**NIST CSF Anchors:** PR.PS-01, PR.DS-10
**Verification Criteria (operational):**
- CRA secure-by-default kiosk config document: debug ports disabled, default passwords rotated, signed firmware required
- Auto-configuration verification in CI gates any commit that re-enables debug ports or default credentials
- Privacy-by-default check confirms GDPR Art. 25(2) data minimisation defaults applied at kiosk deployment

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** IN_PROGRESS
**Dependencies:** D-07.3 (CI/CD pipeline), D-03.1 (identity)
**Risk if not met:** MEDIUM — Default credentials/product config exploitable; CRA Art. 13(2) + GDPR Art. 25(2) failure
**Affected Stakeholders:** Travelers (data subjects), Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-04.1-002 — Incident Detection & Triage

**Description (multi-paragraph):**

**Context:** CRA Art. 14(3) severe-incident detection duty. AI-driven on-device anomaly detection covers AI_Act Art. 72 post-market monitoring + Art. 73 serious-incident detection on a single SOC workflow. NIS 2 Art. 21(2)(g) continuous monitoring.

**Scope:** All events on the eGate stack and back-end services. The objective includes the AI model drift detection.

**Boundaries:** Out of scope: incident containment (D-04.2), notification (D-04.3), recovery (D-04.4), and audit logging (D-10.2). Edge cases: anonymous incidents follow the same triage but have limited notification obligations.

**Source Article:** CRA Art. 14(3) | NIS 2 Art. 21(2)(g) | AI_Act Art. 72 + Art. 73 | GDPR Art. 32(1)(d)
**NIST CSF Anchors:** DE.CM-01, DE.CM-09, DE.AE-02
**Verification Criteria (operational):**
- 24/7 SOC with Security Information and Event Management integrating on-device anomaly detection; mean-time-to-detect (MTTD) tracked quarterly
- Incident playbooks per scenario include biometric-data breach (CRA Art. 14(3) severe incident) handling
- Detection capability tested annually via incident response exercise with documented detection outcomes

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-10.1 (continuous monitoring), D-10.2 (audit log)
**Risk if not met:** HIGH — Delayed incident detection; CRA Art. 14(3) severe-incident + AI_Act Art. 73 failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA, CSIRT), Internal: CISO, SOC
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-04.2-002 — Incident Containment & Response

**Description (multi-paragraph):**

**Context:** CRA Art. 21 manufacturer-equivalent trigger + CRA Art. 14(3) severe-incident containment. documented incident response procedure aligns with CRA + NIS 2 on a single CSIRT workflow. AI_Act Art. 73 serious-incident containment.

**Scope:** All confirmed-or-suspected personal-data and security incidents. The objective includes the chain-of-custody log and the CSIRT coordination checklist.

**Boundaries:** Out of scope: detection (D-04.1), notification (D-04.3), recovery (D-04.4), and audit logging (D-10.2). Edge cases: government-controlled incidents require controller-coordinated containment.

**Source Article:** CRA Art. 14(3) + Art. 21 | NIS 2 Art. 21(2)(c) | GDPR Art. 32(1)(c)
**NIST CSF Anchors:** RS.MI-01, RS.MI-02, RC.RP-01
**Verification Criteria (operational):**
- Documented documented incident response procedure covers GDPR Art. 32 processor-side containment and CRA Art. 14(3) severe-incident
- Chain-of-custody evidence pack template validated by Legal Counsel; sample pack on file
- CSIRT coordination procedure with named contacts and back-up channels tested in last tabletop

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-04.1 (detection), D-04.3 (notification)
**Risk if not met:** HIGH — Uncontained breach spreads; GDPR Art. 32(1)(c) + CRA Art. 14(3) failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA), Internal: CISO, SOC, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-04.3-002 — Incident Notification & Reporting

**Description (multi-paragraph):**

**Context:** CRA Art. 14(1-2) AEV notification + Art. 14(3) severe-incident notification + Art. 14(8) user notification. The max-SLA 24h routing workflow is RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4. GDPR Art. 33(2) processor→controller without undue delay. NIS 2 Art. 23(4)(a) significant-incident 24h. AI_Act Art. 73(2-4) 3-tier serious-incident.

**Scope:** All confirmed incidents requiring external notification. The objective includes the routing pipeline and per-recipient evidence packs.

**Boundaries:** Out of scope: detection (D-04.1), containment (D-04.2), and recovery (D-04.4). Edge cases: incidents where the controller requests delayed notification require delay-grounds documentation per CRA Art. 14(2).

**Source Article:** GDPR Art. 33(2) + Art. 33(1) | CRA Art. 14(1-2) + Art. 14(3) + Art. 14(8) | NIS 2 Art. 23(4)(a) | AI_Act Art. 73(2-3)
**NIST CSF Anchors:** RS.CO-02, RS.MA-01, RS.MA-01
**Verification Criteria (operational):**
- Multi-reg max-SLA 24h notification routing pipeline tested quarterly with all four recipients (DPA / MSA / CSIRT / Notified Body)
- AI_Act 2-day widespread-infringement sub-workflow demonstrably triggered within 4h of incident categorisation
- Tabletop exercise demonstrates 24h delivery to DPA, ENISA, CSIRT, and Notified Body on a single timeline

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-04.1 (detection), D-04.2 (containment), D-10.2 (audit log)
**Risk if not met:** CRITICAL — Late notification to 4 regulators; GDPR Art. 83(4) + CRA Art. 56 + NIS 2 Art. 20 management liability + AI_Act Art. 99 fines
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA, CSIRT, Notified Body), Internal: CEO, CISO, DPO, Legal
**Maturity Score:** Current 2/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-04.4-002 — Incident Recovery & Lessons Learned

**Description (multi-paragraph):**

**Context:** NIS 2 Art. 21(2)(c) business continuity + Art. 21(2)(d) supply-chain DR. 10-year retention anchors CRA Art. 13(13) + NIS 2 Art. 21(2) on a single DR artefact. AI_Act Art. 72 post-market monitoring includes recovery.

**Scope:** All eGate stack components and back-end services. The objective includes the lessons-learned report.

**Boundaries:** Out of scope: detection (D-04.1), containment (D-04.2), and notification (D-04.3). Edge cases: cross-region failover adds 4h to RTO but must be validated separately.

**Source Article:** NIS 2 Art. 21(2)(c) + Art. 21(2)(d) | CRA Art. 13(13) | GDPR Art. 32(1)(b)(c)
**NIST CSF Anchors:** RC.RP-01, RC.RP-03, RC.RP-04
**Verification Criteria (operational):**
- RTO 24h, RPO 1h demonstrated via quarterly restore drill with documented evidence of time-to-restore
- Immutable backup with 10-year retention anchored to CRA Art. 13(13) and NIS 2 Art. 21(2)(c)
- Lessons-learned report produced within 30 days of every significant incident with management review

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-04.2 (containment), D-09.1 (policies)
**Risk if not met:** HIGH — Extended downtime; NIS 2 Art. 21(2)(c) BCP + 10y retention breach
**Affected Stakeholders:** Travelers (data subjects), Airport operators, Internal: CISO, CTO, Operations
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-05.1-002 — Data Minimisation

**Description (multi-paragraph):**

**Context:** CRA Art. 13(3) intended purpose + reasonably foreseeable use. CRA Art. 13(5) supply-chain data minimisation. Biometric ephemeral pattern documented in Annex VII technical file. AI_Act Art. 10 data governance.

**Scope:** All data fields collected at the eGate kiosk. The objective includes the field-level enforcement in schema.

**Boundaries:** Out of scope: retention policy (D-05.2), erasure (D-05.3), and portability (D-05.4). Edge cases: law-enforcement preservation requests may temporarily override minimisation.

**Source Article:** GDPR Art. 5(1)(c) | CRA Art. 13(3) + Art. 13(5) | AI_Act Art. 10
**NIST CSF Anchors:** PR.DS-10, ID.AM-03
**Verification Criteria (operational):**
- Field-level enforcement in schema rejects any field flagged for ephemeral processing (biometric reference data)
- biometric reference data deletion verified via hardware cryptographic module key destruction within seconds of match operation
- Data minimisation review per release with DPO sign-off demonstrates alignment with AI_Act Art. 10 + GDPR Art. 5(1)(c)

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** DONE
**Dependencies:** D-09.2 (DPIA), D-07.1 (secure-by-design)
**Risk if not met:** MEDIUM — Over-collection of biometric data; GDPR Art. 5(1)(c) + Art. 9 + AI_Act Art. 10
**Affected Stakeholders:** Travelers (data subjects), Internal: DPO, CTO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-05.2-002 — Retention & Archiving

**Description (multi-paragraph):**

**Context:** AI_Act Art. 19(1) at least six months automatic logging retention. The 10-year retention is above the AI_Act floor. CRA Art. 13(13) technical documentation retention aligned. NIS 2 Art. 21(2)(a) risk-assessment records retention.

**Scope:** All data classes held by SecureBorder. The objective includes the documented retention per class and the destruction verification.

**Boundaries:** Out of scope: data minimisation (D-05.1), erasure (D-05.3), and portability (D-05.4). Edge cases: AI_Act 10-year retention is above the Art. 19(1) floor — explicitly documented.

**Source Article:** GDPR Art. 5(1)(e) | CRA Art. 13(13) | AI_Act Art. 19(1) + Art. 12
**NIST CSF Anchors:** PR.DS-10, ID.AM-03, PR.PS-02
**Verification Criteria (operational):**
- Retention policy per data type: biometric ephemeral; audit logs 10 years; watchlist per government policy
- AI_Act Art. 19(1) ≥6-month automatic logging retention satisfied with 10y retention (above-floor)
- Quarterly retention audit demonstrates data destruction within policy windows

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** DONE
**Dependencies:** D-05.1 (minimisation), D-09.4 (RoPA)
**Risk if not met:** MEDIUM — Retention beyond policy; GDPR Art. 5(1)(e) + AI_Act Art. 19(1) floor
**Affected Stakeholders:** Travelers (data subjects), Internal: DPO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-05.3-002 — Right to Erasure

**Description (multi-paragraph):**

**Context:** CRA Art. 13(5) deletes = cryptographic erasure (key destruction) where data is replicated. Physical destruction only for single-copy storage media. CRA Art. 13(8) without delay from awareness. The cryptographic sharding is part of CRA conformity assessment technical documentation.

**Scope:** All personal data subject to erasure requests. The objective includes the hardware cryptographic module key destruction mechanism.

**Boundaries:** Out of scope: data minimisation (D-05.1), retention (D-05.2), and portability (D-05.4). Edge cases: government-preserved records require controller-coordinated processing.

**Source Article:** GDPR Art. 17 + Art. 19 | CRA Art. 13(5) + Art. 13(8)
**NIST CSF Anchors:** PR.DS-10, PR.DS-10
**Verification Criteria (operational):**
- Erasure endpoint destroys biometric↔identity mapping via hardware cryptographic module key destruction (cryptographic sharding)
- Anonymised audit trail retained per AI_Act Art. 19(1) ≥6-month retention floor without re-identification (Art. 12 governs transparency; logging retention is D-10.2, not D-05.3)
- Right-to-erasure request fulfilled within GDPR Art. 12(3) one-month deadline

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** IN_PROGRESS
**Dependencies:** D-01.3 (key custody), D-10.2 (audit log)
**Risk if not met:** HIGH — Right-to-erasure failure; GDPR Art. 17 + Art. 83(5) fines + biometric Art. 9 sensitivity
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA), Internal: DPO, CISO
**Maturity Score:** Current 2/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-05.4-002 — Data Portability

**Description (multi-paragraph):**

**Context:** D-05.4 is GDPR-only (Art. 20 data portability) with no CRA/NIS 2/AI_Act parallel. The objective is met by the JSON export endpoint per GDPR Art. 20. No SG row is required because no other regulation imposes a portability duty on the eGate stack.

**Scope:** Personal data provided by the data subject or generated by the service. The objective includes the machine-readable format and the response time.

**Boundaries:** Out of scope: data minimisation (D-05.1), retention (D-05.2), and erasure (D-05.3). Edge cases: portability of derived inferences (e.g., watchlist match outcomes) is not in scope — only directly-provided or service-generated data.

**Source Article:** GDPR Art. 20
**NIST CSF Anchors:** PR.DS-10, PR.DS-10
**Verification Criteria (operational):**
- JSON export endpoint operational per GDPR Art. 20 with documented machine-readable format
- Data portability response time within 30 days for standard request; tested with 1 sample per release
- Audit-log-controller capacity supported alongside data portability where legally required

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** DONE
**Dependencies:** D-09.4 (RoPA)
**Risk if not met:** MEDIUM — Data portability failure; GDPR Art. 20 + Art. 83(4) fines
**Affected Stakeholders:** Travelers (data subjects), Internal: DPO, CTO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P2

### AG-D-06.1-002 — Vendor Risk Assessment

**Description (multi-paragraph):**

**Context:** NIS 2 Art. 21(2)(d) supply-chain risk assessment (direct supplier scope per Art. 21(3) three-prong). Annual supplier audit. RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4. CRA Art. 13(1) supply-chain duty.

**Scope:** All tier-1 suppliers with access to biometric data or critical infrastructure. The objective includes the annual supplier audit and per-processor due-diligence artefacts.

**Boundings:** Out of scope: contractual security obligations (D-06.3), software bill of materials (D-06.2), and boundary management (D-06.4). Edge cases: government-supplied components are excluded from the software bill of materials gate but are in scope for the risk assessment.

**Source Article:** NIS 2 Art. 21(2)(d) + Art. 21(3) | GDPR Art. 28
**NIST CSF Anchors:** GV.SC-01, GV.SC-02, GV.SC-04
**Verification Criteria (operational):**
- NIS 2 Art. 21(2)(d) supplier risk assessment documented for each tier-1 supplier with annual refresh
- GDPR Art. 28(1) sufficient-guarantees due-diligence questionnaire + certification audit on file per biometric sub-processor
- Annual supplier audit demonstrates control coverage for tier-1 biometric and cloud suppliers

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-06.3 (contractual), D-06.4 (boundary)
**Risk if not met:** HIGH — Unmanaged supplier exposes biometric data; NIS 2 Art. 21(2)(d) + GDPR Art. 28 failure
**Affected Stakeholders:** Suppliers (biometric sub-processors), Regulators (DPA, CSIRT), Internal: CISO, Procurement, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-06.2-002 — Software Bill of Materials (software bill of materials)

**Description (multi-paragraph):**

**Context:** CRA Art. 13(11) software bill of materials per release. machine-readable software bill of materials format format. Signed software bill of materials attached to firmware. Vulnerability tracking against software bill of materials is the only applicable regulatory floor (CRA is the sole authority at D-06.2). NIS 2 Art. 21(2)(d) requires software bill of materials as evidence of supply-chain security.

**Scope:** All OSS and commercial components in the eGate firmware. The objective includes the per-release software bill of materials and the CVE-to-component mapping.

**Boundaries:** Out of scope: vendor risk assessment (D-06.1), contractual obligations (D-06.3), and patching (D-02.2). Edge cases: AI model components may require model-bill-of-materials separately.

**Source Article:** CRA Art. 13(11)
**NIST CSF Anchors:** ID.AM-02, GV.SC-02
**Verification Criteria (operational):**
- machine-readable software bill of materials format software bill of materials per release generated, signed, and attached to firmware artefact
- Vulnerability tracking against software bill of materials with documented CVE-to-component mapping for every disclosed vuln
- CRA Art. 13(11) software bill of materials-anchored vulnerability tracking demonstrated for last 3 releases

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** DONE
**Dependencies:** D-02.1 (vuln ID), D-07.3 (CI/CD)
**Risk if not met:** MEDIUM — Untracked OSS vulnerability; CRA Art. 13(11) + unexpected CVE exposure
**Affected Stakeholders:** Suppliers (OSS, commercial), Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-06.3-002 — Contractual Security Obligations

**Description (multi-paragraph):**

**Context:** NIS 2 Art. 21(2)(d) contractual chain + Art. 21(3) supplier assessment three-prong. GDPR Art. 46 transfer safeguards for non-EU suppliers. RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4. CRA Art. 13(1) supply-chain contractual duty.

**Scope:** All processor contracts and supplier security clauses. The objective includes the DPA template and sub-processor flowdown clauses.

**Boundaries:** Out of scope: vendor risk assessment (D-06.1), software bill of materials (D-06.2), and boundary management (D-06.4). Edge cases: government procurement contracts may require carve-out with documented residual risk.

**Source Article:** NIS 2 Art. 21(2)(d) + Art. 21(3) | GDPR Art. 28(3) + Art. 46
**NIST CSF Anchors:** GV.SC-02, GV.SC-03, GV.SC-04
**Verification Criteria (operational):**
- DPA template with GDPR Art. 28(3) 8-element list enforced across all processor contracts
- NIS 2 Art. 21(2)(d) contractual chain with multi-tier sub-processor flowdown and right-to-audit clauses
- Annual contract review demonstrates compliance with GDPR Art. 46 transfer safeguards for non-EU suppliers

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-06.1 (vendor risk), D-09.4 (RoPA)
**Risk if not met:** HIGH — Sub-processor breach without DPA; GDPR Art. 28(3) + Art. 46 transfer safeguards failure
**Affected Stakeholders:** Suppliers (all processors), Regulators (DPA, CSIRT), Internal: CISO, Legal, Procurement
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-06.4-002 — Third-Party Boundary Management

**Description (multi-paragraph):**

**Context:** NIS 2 Art. 21(2)(d) supply-chain boundary + Art. 21(2)(e) network security. mutual transport authentication + segmentation discharge both on a single network-security artefact. CRA Annex I Part I (2)(e) state-of-the-art transit.

**Scope:** All network boundaries between SecureBorder, cloud, and government. The objective includes the segmentation policy and the zero-trust enforcement.

**Boundaries:** Out of scope: vendor risk assessment (D-06.1), software bill of materials (D-06.2), and contractual obligations (D-06.3). Edge cases: emergency remote access requires documented break-glass procedure.

**Source Article:** NIS 2 Art. 21(2)(d) + Art. 21(2)(e) | CRA Annex I Part I (2)(e) | GDPR Art. 32(1)(b)
**NIST CSF Anchors:** GV.SC-02, GV.SC-03, GV.SC-04
**Verification Criteria (operational):**
- Network segmentation between SecureBorder / Cloud / Government validated via pen-test verification
- mutual transport authentication enforced on all boundaries; zero-trust kiosk↔cloud architecture verified quarterly
- Documented network topology reviewed annually against NIS 2 Art. 21(2)(e) network security baseline

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** DONE
**Dependencies:** D-06.1 (vendor risk), D-01.2 (transit)
**Risk if not met:** HIGH — Lateral movement from compromised boundary; NIS 2 Art. 21(2)(e) + AI_Act Art. 15
**Affected Stakeholders:** Government back-end, Cloud providers, Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-07.1-002 — Secure-by-Design Principles

**Description (multi-paragraph):**

**Context:** AI_Act Art. 9 risk-management system + Art. 13 transparency + Art. 14 human oversight. CRA Art. 13(1)+(2) secure-by-default + risk assessment propagation across 6 lifecycle phases. RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4.

**Scope:** All SecureBorder features and products. The objective includes threat modelling per feature and the AI_Act risk-management system implementation.

**Boundaries:** Out of scope: secure coding practices (D-07.2), CI/CD pipeline security (D-07.3), and information security policies (D-09.1). Edge cases: features added via partnership or acquisition require separate re-modelling.

**Source Article:** AI_Act Art. 9 + Art. 13 + Art. 14 | CRA Art. 13(1) + Art. 13(2) | GDPR Art. 25(1) + Art. 35
**NIST CSF Anchors:** PR.PS-06, PR.PS-02, PR.PS-01
**Verification Criteria (operational):**
- AI_Act risk management system (Art. 9) documented with iterative risk assessment across 6 lifecycle phases
- CRA Art. 13(1)+(2) secure-by-default design verified via threat modelling per feature (STRIDE + AI extensions)
- Unified SDLC for high-risk AI gates code merge on privacy-by-design (GDPR Art. 25(1)) checks

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CTO
**Status:** IN_PROGRESS
**Dependencies:** D-09.2 (DPIA), D-07.2 (secure coding)
**Risk if not met:** HIGH — Insecure high-risk AI in production; AI_Act Art. 9 + Art. 13 + Art. 14 failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (AI Supervisory Authority, ENISA, DPA), Internal: CTO, AI Governance Lead, DPO
**Maturity Score:** Current 2/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-07.2-002 — Secure Coding Practices

**Description (multi-paragraph):**

**Context:** CRA Annex I Part I (2)(c) attack-surface minimisation via secure coding standards (application security maturity model at industry-standard level for AI components). static application security testing (static application security testing tool) + dynamic application security testing in CI. Pre-commit secret scanning. CRA Art. 13(11) software bill of materials-anchored vulnerability tracking. AI_Act Art. 15 robustness via secure coding.

**Scope:** All code in the eGate stack and back-end services. The objective includes the secure coding standards and the CI gating.

**Boundaries:** Out of scope: secure-by-design (D-07.1), CI/CD pipeline (D-07.3), and patch management (D-02.2). Edge cases: AI model code follows the same standards with additional model-specific checks.

**Source Article:** CRA Annex I Part I (2)(c) | AI_Act Art. 15 | NIS 2 Art. 21(2)(d)
**NIST CSF Anchors:** PR.PS-06, PR.PS-02, PR.PS-01
**Verification Criteria (operational):**
- static application security testing (static application security testing tool) + dynamic application security testing in CI blocking merge on high-severity findings
- application security maturity model at industry-standard level secure coding standards applied for AI components with documented verification
- Pre-commit secret scanning demonstrated to catch 100% of test tokens in last regression exercise

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CTO
**Status:** DONE
**Dependencies:** D-07.1 (secure-by-design), D-07.3 (CI/CD)
**Risk if not met:** MEDIUM — Vulnerable code in production; CRA Annex I Part I (2)(c) + AI_Act Art. 15
**Affected Stakeholders:** Travelers (data subjects), Internal: CTO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-07.3-002 — CI/CD Pipeline Security

**Description (multi-paragraph):**

**Context:** NIS 2 Art. 21(2)(d) supply-chain security + CRA Art. 13(11) software bill of materials. Signed CI artefacts + pipeline-as-code + supply-chain integrity controls Level 3. software bill of materials gate blocks on critical vulns. RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4.

**Scope:** All CI/CD pipelines producing eGate firmware and back-end artefacts. The objective includes the supply-chain integrity controls Level 3 evidence and the software bill of materials gate.

**Boundaries:** Out of scope: secure-by-design (D-07.1), secure coding (D-07.2), and software bill of materials (D-06.2). Edge cases: emergency hotfix pipelines may bypass the software bill of materials gate but require documented exception.

**Source Article:** NIS 2 Art. 21(2)(d) | CRA Art. 13(11)
**NIST CSF Anchors:** PR.PS-02, ID.RA-01, PR.PS-06
**Verification Criteria (operational):**
- Signed CI artefacts with pipeline-as-code; supply-chain integrity controls Level 3 evidence generated per release
- software bill of materials gate blocks release on critical/high CVE without documented exception
- NIS 2 SDLC pipeline security attested in annual ISO 27001 surveillance audit

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CTO
**Status:** IN_PROGRESS
**Dependencies:** D-06.2 (software bill of materials), D-02.1 (vuln ID)
**Risk if not met:** HIGH — Supply-chain attack via CI/CD; NIS 2 Art. 21(2)(d) + CRA Art. 13(11) failure
**Affected Stakeholders:** Regulators (ENISA, CSIRT), Internal: CTO, CISO
**Maturity Score:** Current 2/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-08.1-002 — General Security Awareness

**Description (multi-paragraph):**

**Context:** NIS 2 Art. 21(2)(g) basic cyber hygiene + Art. 21(2)(f) training. CRA Art. 13(2) installation/use training included. Phishing simulation + kiosk-specific guide on a single training programme. AI_Act Art. 4 AI literacy baseline.

**Scope:** All SecureBorder employees handling eGate kiosk operations or biometric data. The objective includes the GDPR-specific module and the phishing simulation cadence.

**Boundaries:** Out of scope: role-specific competence (D-08.2). Edge cases: contractor workforce may require condensed training with documented compliance.

**Source Article:** NIS 2 Art. 21(2)(e) + Art. 21(2)(g) | CRA Art. 13(2) | GDPR Art. 39
**NIST CSF Anchors:** PR.AT-01, PR.AT-02, PR.PS-01
**Verification Criteria (operational):**
- Annual security awareness training covers GDPR, NIS 2, and CRA with documented module completion
- Phishing simulation quarterly with click-rate tracked and reported to CISO
- Kiosk-specific security guide distributed to all kiosk operators with annual refresh

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-09.1 (policies)
**Risk if not met:** MEDIUM — Social engineering compromise; NIS 2 Art. 21(2)(g) + GDPR Art. 39(1)(b) failure
**Affected Stakeholders:** Internal: All employees, Internal: CISO, HR
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-08.2-002 — Role-Specific Competence

**Description (multi-paragraph):**

**Context:** NIS 2 Art. 21(2)(g) role-specific competence + AI_Act Art. 4 AI literacy. SOC analyst certification + DPO + AI Lead training on a single competence framework. CRA Art. 13(2) installation/use training for relevant roles.

**Scope:** All Security, Privacy, AI, and SOC roles. The objective includes the certification maintenance and the continuing education hours.

**Boundaries:** Out of scope: general security awareness (D-08.1). Edge cases: management board training is handled at the board briefing level, not a training-based competency.

**Source Article:** NIS 2 Art. 21(2)(g) | AI_Act Art. 4 + Art. 14 | GDPR Art. 37(1)(c) + Art. 39(1)(b)
**NIST CSF Anchors:** PR.AT-02, PR.AT-01, GV.RR-02
**Verification Criteria (operational):**
- DPO training refresh annual; AI Governance Lead per AI_Act Art. 14 human oversight
- SOC analyst certification (GCIH/equivalent) maintained for ≥80% of SOC team
- Continuing professional education hours documented per Art. 4 AI literacy requirement

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-08.1 (awareness), D-09.1 (policies)
**Risk if not met:** MEDIUM — Unqualified role-holder; AI_Act Art. 4 + Art. 14 + DPO Art. 37(1)(c) failure
**Affected Stakeholders:** Internal: Security, Privacy, AI, SOC roles, Internal: CISO, DPO, HR
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-09.1-002 — Information Security Policies

**Description (multi-paragraph):**

**Context:** AI_Act Art. 9 risk-management policies + Art. 13 transparency policies. CRA Art. 13(8) support policies. NIS 2 Art. 21(1) framework policies. ISO 27001 certified ISMS discharges all four on a single policy artefact.

**Scope:** All SecureBorder policies and procedures. The objective includes the AI_Act risk-management and transparency policies.

**Boundaries:** Out of scope: impact assessments (D-09.2), records of processing (D-09.4), and policies for specific sub-domains (D-08.x). Edge cases: government-mandated policies may require explicit acknowledgement with documented residual risk.

**Source Article:** AI_Act Art. 9 + Art. 13 | CRA Art. 13(8) | NIS 2 Art. 21(1) | GDPR Art. 5(2) + Art. 24
**NIST CSF Anchors:** GV.PO-01, GV.PO-02, GV.RR-02
**Verification Criteria (operational):**
- ISO 27001 certified ISMS policies current with annual surveillance audit passing
- AI_Act Art. 9 risk-management policies + Art. 13 transparency policies documented
- Unified policy set with regulation-specific annexes for GDPR + CRA + NIS 2 + AI_Act

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-09.2 (DPIA), D-09.4 (RoPA)
**Risk if not met:** LOW — ISO 27001 certified; policies maintained; failure unlikely
**Affected Stakeholders:** Regulators (DPA, ENISA, CSIRT, AI Supervisory Authority), Internal: CISO, DPO, Legal
**Maturity Score:** Current 4/4 → Target 4/4
**Implementation Priority:** P2

### AG-D-09.2-002 — Impact & Risk Assessments

**Description (multi-paragraph):**

**Context:** AI_Act Art. 27 FRIA + Art. 9 risk-management system. CRA Art. 13(2) risk assessment + NIS 2 Art. 21(1) risk analysis. The unified DPIA+FRIA process discharges all four on a single impact-assessment artefact (resolves T-003).

**Scope:** All SecureBorder products and processing operations. The objective includes the unified DPIA+FRIA process and the dual output.

**Boundaries:** Out of scope: information security policies (D-09.1), records of processing (D-09.4), and compliance testing (D-10.3). Edge cases: rapid-deployment features may require abbreviated assessment with documented residual risk.

**Source Article:** GDPR Art. 35 | AI_Act Art. 27 + Art. 9 | CRA Art. 13(2) | NIS 2 Art. 21(1)
**NIST CSF Anchors:** ID.RA-01, ID.RA-04, ID.RA-05
**Verification Criteria (operational):**
- Unified DPIA + FRIA single process with dual output documented per GDPR Art. 35 + AI_Act Art. 27
- Threshold-trigger criteria per GDPR Art. 35(3) and AI_Act Art. 27(1) documented
- Annual impact assessment review with DPO + AI Governance Lead sign-off

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** IN_PROGRESS
**Dependencies:** D-09.1 (policies), D-09.4 (RoPA)
**Risk if not met:** HIGH — DPIA/FRIA missing for high-risk AI; GDPR Art. 35(3) + AI_Act Art. 27(1) failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, AI Supervisory Authority), Internal: DPO, AI Governance Lead, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-09.4-002 — Records of Processing

**Description (multi-paragraph):**

**Context:** AI_Act Art. 12 record-keeping + CRA Art. 13(12) technical documentation + NIS 2 Art. 21(2)(a) risk-assessment records. DPO oversight + immutable storage on a single record-keeping artefact.

**Scope:** All processing activities involving personal data. The objective includes the immutable storage and the 10-year retention.

**Boundaries:** Out of scope: information security policies (D-09.1), impact assessments (D-09.2), and audit logging (D-10.2). Edge cases: government-controlled processing requires controller-coordinated RoPA entry.

**Source Article:** GDPR Art. 30 | AI_Act Art. 12 | CRA Art. 13(12) | NIS 2 Art. 21(2)(a)
**NIST CSF Anchors:** ID.AM-08, PR.DS-10, GV.PO-02
**Verification Criteria (operational):**
- RoPA covering all 4 applicable regulations with immutable storage and 10-year retention
- DPO oversight on RoPA updates; quarterly reconciliation with AI_Act Art. 12 record-keeping
- GDPR Art. 30 records of processing activities current and accessible to supervisory authority on request

**Verification Method:** TEST + DEMONSTRATE
**Owner:** DPO
**Status:** DONE
**Dependencies:** D-09.1 (policies), D-05.2 (retention)
**Risk if not met:** MEDIUM — Missing RoPA entry; GDPR Art. 30 + AI_Act Art. 12 record-keeping failure
**Affected Stakeholders:** Regulators (DPA, AI Supervisory Authority), Internal: DPO, CISO
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-10.1-002 — Continuous Security Monitoring

**Description (multi-paragraph):**

**Context:** AI_Act Art. 72 post-market monitoring + Art. 73 serious-incident detection + NIS 2 Art. 21(2)(g) continuous monitoring + CRA Art. 14(3) severe-incident detection. 24/7 SOC + AI model drift detection on a single monitoring artefact. RIGOROUS — TEST + ANALYZE + external audit per Track B §6.4.

**Scope:** All eGate stack components and back-end services. The objective includes the AI model drift detection and the serious-incident detection.

**Boundaries:** Out of scope: incident detection (D-04.1), audit logging (D-10.2), and compliance testing (D-10.3). Edge cases: 24/7 SOC must be staffed or contracted with minimum competency requirements.

**Source Article:** AI_Act Art. 72 + Art. 73 | NIS 2 Art. 21(2)(g) | CRA Art. 14(3) | GDPR Art. 32(1)(d)
**NIST CSF Anchors:** DE.CM-01, DE.CM-09, DE.AE-02
**Verification Criteria (operational):**
- 24/7 SOC with Security Information and Event Management + AI model drift detection; Uptime SLA ≥99.95% evidenced
- AI_Act Art. 72 post-market monitoring + Art. 73 serious-incident detection integrated on single Security Information and Event Management
- Quarterly NCR (non-conformity) review with documented remediation and effectiveness validation

**Verification Method:** TEST + ANALYZE + external audit
**Owner:** CISO
**Status:** IN_PROGRESS
**Dependencies:** D-04.1 (incident detection), D-10.2 (audit log)
**Risk if not met:** HIGH — AI model drift undetected; AI_Act Art. 72 + Art. 73 + NIS 2 Art. 21(2)(g) failure
**Affected Stakeholders:** Travelers (data subjects), Regulators (DPA, ENISA, CSIRT, AI Supervisory Authority), Internal: CISO, SOC, AI Governance Lead
**Maturity Score:** Current 2/4 → Target 4/4
**Implementation Priority:** P0

### AG-D-10.2-002 — Audit Logging & Traceability

**Description (multi-paragraph):**

**Context:** AI_Act Art. 12 logging capability + Art. 19(1) at least six months automatic retention + CRA Art. 13(14) logging + NIS 2 Art. 21(2)(h) cryptography-policy logging. Tamper-evident + 10-year retention above the Art. 19(1) floor on a single log artefact.

**Scope:** All SecureBorder events with audit-relevant content. The objective includes the tamper-evident hash chain and the 10-year retention.

**Boundaries:** Out of scope: incident detection (D-04.1), records of processing (D-09.4), and compliance testing (D-10.3). Edge cases: high-volume streaming events may use tiered storage with hot/cold split.

**Source Article:** AI_Act Art. 12 + Art. 19(1) | CRA Art. 13(14) | NIS 2 Art. 21(2)(h) | GDPR Art. 5(2) + Art. 30
**NIST CSF Anchors:** PR.DS-01, PR.PS-04, DE.CM-01
**Verification Criteria (operational):**
- Tamper-evident audit log with cryptographic hash chain; 10-year retention above AI_Act Art. 19(1) floor
- CRA Art. 13(14) logging + NIS 2 Art. 21(2)(h) cryptography-policy logging on single log artefact
- GDPR Art. 5(2) accountability principle demonstrated via quarterly audit log review

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-09.1 (policies), D-09.4 (RoPA)
**Risk if not met:** MEDIUM — Audit log tamper; GDPR Art. 5(2) accountability + AI_Act Art. 12 failure
**Affected Stakeholders:** Regulators (DPA, AI Supervisory Authority), Internal: CISO, DPO, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P1

### AG-D-10.3-002 — Compliance Testing

**Description (multi-paragraph):**

**Context:** AI_Act Art. 43 conformity assessment re-assessment + Art. 72 post-market re-evaluation + CRA Art. 24(3) OSS steward extension + NIS 2 Art. 21(2) controls test. Annual ISO 27001 surveillance + AI_Act conformity re-assessment on a single compliance-test programme.

**Scope:** All SecureBorder compliance obligations. The objective includes the annual ISO 27001 surveillance audit and the AI_Act conformity re-assessment.

**Boundaries:** Out of scope: continuous monitoring (D-10.1), audit logging (D-10.2), and information security policies (D-09.1). Edge cases: rapid-deployment material changes may require accelerated compliance testing.

**Source Article:** AI_Act Art. 43 + Art. 72 | CRA Art. 24(3) | NIS 2 Art. 21(2) | GDPR Art. 28(3)(h) + Art. 35(11)
**NIST CSF Anchors:** PR.PS-02, ID.RA-05, DE.AE-02
**Verification Criteria (operational):**
- Annual ISO 27001 surveillance audit + AI_Act conformity re-assessment + NIS 2 controls test on integrated programme
- GDPR Art. 35(11) DPIA-on-change review executed for material changes
- CISO sign-off on annual compliance-test report with C-suite acknowledgement

**Verification Method:** TEST + DEMONSTRATE
**Owner:** CISO
**Status:** DONE
**Dependencies:** D-09.1 (policies), D-10.1 (monitoring)
**Risk if not met:** MEDIUM — Compliance drift; ISO 27001 surveillance + AI_Act re-assessment failure
**Affected Stakeholders:** Regulators (DPA, ENISA, CSIRT, AI Supervisory Authority, Notified Body), Internal: CISO, DPO, Legal
**Maturity Score:** Current 3/4 → Target 4/4
**Implementation Priority:** P2


## §N Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2026-08-06 | Sprint 0 Executor | Placeholder; 53 lines; structure plan only. |
| 1.0 | 2026-08-06 | Sprint 4 Executor | Full content fill (V-03 fix): §1 generic baseline (35 rows × 7 columns from corpus), §2 adjusted PG (35 rows), §3 adjusted SG (35 rows; D-05.4 GDPR-only has SG = N/A), §4 tensions resolved (T-001/002/003), §5 Track B decision trail (35 rows; 8 RIGOROUS + 27 STANDARD), §6 cross-references, §7 validation. **70 adjusted objectives** (35 PG + 35 SG). All 35 active sub-domains covered; 3 inactive sub-domains (D-07.4, D-08.3, D-09.3) excluded. |
| 2.0 | 2026-08-06 | Sprint 5 Executor | **DEEP enrichment without Effort/Cost/Timeline.** §2/§3 tables extended with "Details" anchor column (35 PG + 35 SG anchors). §4 Tensions Resolved: 3 tensions expanded to multi-paragraph form (T-001 4-way temporal conflict, T-002 cryptographic sharding, T-003 unified DPIA+FRIA). **§8 NEW: 70 DEEP detail cards** (35 PG + 35 SG) — each with 15 fields: Description (multi-paragraph), Source Article, NIST CSF Anchors, Verification Criteria (operational), Verification Method, Owner, Status, Dependencies, Risk if not met, Affected Stakeholders, Maturity Score, Implementation Priority. D-01.x (RIGOROUS) anchored to biometric Art. 9 hardware cryptographic module-backed architecture. D-04.3 RIGOROUS — 4-reg max-SLA 24h routing. D-06.x RIGOROUS — NIS 2 supply chain + biometric processor agreements. D-07.x RIGOROUS — AI_Act Annex III conformity + CRA + supply-chain integrity controls Level 3. D-10.x RIGOROUS — 24/7 SOC + ISO 27001 monitoring. Total file growth: 247 → ~1,500 lines. **Excluded** Effort/Cost/Timeline per user directive. |
| 3.0 | 2026-08-28 | Executor (port Fase 1) | **corr-008 AG- migration + corr-010 rename.** File renamed `07c_Adjusted_Objectives.md` → `Doc13_Adjusted_Goals.md`. All `PG-D-XX.Y[...]` → `AG-D-XX.Y-001`, `SG-D-XX.Y[...]` → `AG-D-XX.Y-002` (70 goal IDs, 141 references incl. anchors); Appendix A added with the bijective legacy alias map; `sprint:` frontmatter keys removed; phantom suffixed references in Doc11/Doc30 (`PG-D-XX.Y-001` with no unsuffixed source) reconciled to the same canonical form. |

## Appendix A — Legacy ID aliases (corr-007 → corr-008 AG- migration)

Bijective map applied 2026-08-28 (port Fase 1). Old IDs are DEPRECATED — kept here for traceability with Doc16 Appendix A (P2 PO/SO aliases) and P3 references.

| Legacy (corr-007) | Canonical (corr-008) |
|---|---|
| `PG-D-XX.Y` / `PG-D-XX.Y-001` | `AG-D-XX.Y-001` (privacy set) |
| `SG-D-XX.Y` / `SG-D-XX.Y-001` | `AG-D-XX.Y-002` (security set) |

Example: `PG-D-01.1` → `AG-D-01.1-001`; `SG-D-01.1` → `AG-D-01.1-002`. Anchor slugs follow (`#pg-d-d011` → `#ag-d-d011-001`).

## §N See also

- **Doc 04** (`Doc03_Company_Context_Assessment.md`)
- **Doc 05** (`Doc08_Regulatory_Applicability.md`)
- **Doc 05b** (`Doc09_Ambiguity_Register.md`)
- **Doc 07** (`Doc11_Structured_Compliance_Matrix.md`)
- **Doc 07b** (`Doc12_Proportionality_Profile.md`)
- **Corpus source** (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/`)
