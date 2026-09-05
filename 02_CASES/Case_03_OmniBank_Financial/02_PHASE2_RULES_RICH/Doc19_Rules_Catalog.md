> **Note:** This is a Rich-Mode copy of the Phase 2 rules catalog. The canonical version (with Block D extensions: tri-maturidade CSF+PF+AI RMF, fields 19-24) lives in `../02_PHASE2_RULES_RICH/Doc19_Rules_Catalog.md`. This Rich copy preserves the original 17-field schema for reference; consult `../02_PHASE2_RULES_RICH/Doc19_Rules_Catalog.md` for the live operational document. *(legacy design text — superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0, port Fase 4)*

---
document_id: AEGIS-P2-11
title: AEGIS Control Set — Rich Mode (Case_03)
phase: 2
version: 2.0
created: 2026-04-03
updated: 2026-08-28
author: Compliance Lead
status: CONTROL_SET_V1
inputs: [Doc15_Obligation_Derivation.md, Doc16_Strategic_Tensions_Report.md, Doc17_Privacy_Security_Objectives.md]
outputs: [Phase 3 inputs]
traceability: AEGIS Class Model → RulesCatalog, AbstractRule, ComplianceRule, BestPracticeRule classes
related_documents: 12_Rules_Catalog.xlsx, 00_Taxonomy_Reference.md
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI_Act]
normative_intensity_rule: AVG_with_AI_MUST_override
dr_002_resolution: >
  DR-002 definido como AVG (não MAX). MAX mata diferenciação (AP-P2-09).
  AVG preserva SHOULD. Adicionalmente, qualquer CR com AI-C* nas source
  clauses é forçado MUST (NI=3) — alinhamento com a baseline AI Act
  (todas as 29 cláusulas AI Act são NI=3 → MUST). DORA também é MUST
  uniforme (todas as 38 DORA cláusulas são NI=3). Aplicado
  retroactivamente a todos os 78 cartões.
ni_avg_rule_note: |
  AVG(NI) per regulation source clauses. AI-C* presence forces MUST (NI=3)
  to preserve AI Act signal (baseline). DORA clauses are uniformly NI=3
  (all 38); NIS2 clauses uniformly NI=3 (all 29); GDPR has 10 NI=2 +
  18 NI=3; CRA has 2 NI=2 + 24 NI=3. DORA + AI are MUST-preserved by source.
frameworks_mapped: [NIST_CSF_2.0, NIST_Privacy_FW_1.0, NIST_AI_RMF_1.0]
expected_fields_per_card: 15
fields_per_card: 15
maturity_dual_mode: triple   # CSF + Privacy + AI RMF (3 independent scores per control) *(legacy design text — superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0, port Fase 4)*
# Case_03 Doc 11 is table-only; fields_per_card counts visible columns. Block D added 6 columns to the table (CSF/PF/AI RMF subcats + 3 maturity scores); the 9→10 increment in Block B was the NI (recomputed) column. *(legacy design text — superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0, port Fase 4)*
---

# Rules Catalog

## 1. DOCUMENT PURPOSE

> **CONTROL SET v1 (port Fase 5, 2026-08-28).** Corrected 24-field schema
> mapping for this table-format catalog: F12-14 Framework anchors CSF/PF/AIRMF
> (Field 24 part 1) · F21 Implementation Status (CSF) · F22 Implementation
> Status (Privacy) · F23 Implementation Status (AI RMF) / Traceability ·
> F23/F24 Traceability (Legal → AG-D → related goals/CRs) and Framework
> Anchors cross-reference (→ Doc20 §1 aggregate: ISO 27001, SSDF). Posture
> statuses are the deterministic legacy backfill per
> IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md §4. Case_03 rule inventory:
> 38 CR (MUST) + 40 BPR (SHOULD) = 78 controls; 5-regulation axis incl. DORA
> (recorded per-row in Source and the regulations columns; coverage via CSF).

This document is the primary output of Phase 2 (Elaboration & Secure Design) for Case 03 — OmniBank Financial Systems (Maximum Complexity). It consolidates all compliance rules and best practices derived from regulatory obligations into a machine-readable, implementable catalog.

The Rules Catalog serves as the bridge between Phase 2 obligation derivation and Phase 3 decomposition. Each rule is traceable to its source obligation, regulatory clause(s), sub-domain, priority, verification method, and implementation mode.

This is the largest Phase 2 document due to OmniBank's maximum complexity profile: 5000+ employees, €800M revenue, cross-border EU operations, AI-driven credit scoring, and full regulatory coverage across all 5 frameworks (GDPR, CRA, NIS 2, DORA, AI Act).

---

## 2. RULES CATALOG METADATA

| Field | Value |
|-------|-------|
| **rulesCatalogId** | RULES-OMNIBANK-2026-001 |
| **caseId** | CASE-03-OMNIBANK |
| **complexity** | Maximum |
| **companyProfile** | Cross-border financial institution with AI-driven services |
| **phase2Status** | COMPLETE |
| **totalComplianceRules** | 38 |
| **totalBestPracticeRules** | 25 |
| **totalRules** | 63 |
| **subDomainCoverage** | 38/38 (100%) |
| **regulationsCovered** | GDPR, CRA, NIS 2, DORA, AI Act (5/5) |
| **tensionsResolved** | 4 (T-001, T-002, T-003, T-004) |
| **soleAuthorityGaps** | 2 sub-domains (D-03.4: CRA, D-05.4: GDPR) |
| **derivationMethod** | 1:1 obligation-to-rule mapping |
| **frameworkArticulation** | ISO 27001:2022, NIST CSF 2.0, NIST Privacy FW 1.0, NIST AI RMF 1.0, hardened-default baseline |

---

<!-- W2 fix: CM.AW-P7 removed — wrong semantic for SOC detection; replaced with ID.RA-P3 per PF 1.0 risk assessment -->
<!-- W3 fix: PR.DS-10 removed — wrong semantic for minimisation/erasure -->

## 3. RULE DEFINITION STRUCTURE

Each rule in this catalog is defined by the following fields:

| Field | Type | Description |
|-------|------|-------------|
| **Rule ID** | string | Unique identifier: `CR-D-XX.Y-NNN` (Compliance Rule) or `BPR-D-XX.Y-NNN` (Best Practice Rule) |
| **Rule Description** | text | Concise statement of what must be implemented |
| **Source** | list | Regulatory clause identifiers (e.g., GDPR-C04, CRA-C07, DORA-C09) |
| **Sub-Domain** | string | Canonical taxonomy reference (e.g., D-01.1, D-03.2) |
| **NI** | float [1.0–3.0] | Normative Intensity — weighted importance of source clauses |
| **Priority** | string | P1 (NI >= 2.5), P2 (NI 2.0–2.499), P3 (Best Practice) |
| **Verification** | string | TEST, INSPECT, DEMONSTRATE, or ANALYZE |
| **Implementation** | string | NATIVE (built in-house), INHERITED (cloud/third-party), HYBRID (combination) |
| **Related Goals** | list | References to goals from Doc17_Privacy_Security_Objectives.md |
| **Notes** | text | Additional context: tension resolution, sole authority, special conditions |

---

## 4. COMPLIANCE RULES CATALOG

### D-01: Data Protection & Encryption

|---------|-----------------|--------|------------|----|----------|-------------|----------------|---------------|-------------------------------|-------------|------------|----------------|---------------|------------------|----------------|
| CR-D-01.1-001 | Personal, financial, and AI data in persistent storage protected by confidentiality mechanisms with segregated cryptographic material management. Apply field-level confidentiality for PII and AI training datasets. | GDPR-C04, C14; CRA-C07; NIS2-C18; DORA-C09; AI-C17 | D-01.1 | 2.667 | P1 | TEST | NATIVE | AG-D-01.1-001, AG-D-05.2-001, AG-D-01.4-001 | 3 (MUST AVG=2.667; AI-C present forces MUST) | PR.DS-01 | PR.DS-P1; CT.DP-P2 | GOVERN-1.6; MEASURE-2.7; MEASURE-2.5 | PARTIAL | PARTIAL | PARTIAL | GDPR-C04, C14; CRA-C07; NIS2-C18; DORA-C09; AI-C17 → AG-D-01.1-001/-002 → AG-D-01.1-001, AG-D-05.2-001, AG-D-01.4-001 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-01.2-001 | Data crossing network boundaries protected by confidentiality mechanisms appropriate to channel classification for internal, external, and API communications. Enforce strict transport security and certificate validation for critical endpoints. | GDPR-C15; CRA-C08; DORA-C10 | D-01.2 | 2.667 | P1 | TEST | NATIVE | AG-D-01.1-001, AG-D-05.4-001 | 2 (SHOULD AVG=2.667) | PR.DS-02 | PR.DS-P2 | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | GDPR-C15; CRA-C08; DORA-C10 → AG-D-01.2-001/-002 → AG-D-01.1-001, AG-D-05.4-001 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-01.3-001 | Cryptographic material custody with segregated lifecycle controls (generation, rotation, revocation, destruction). Separate material by data classification and regulatory domain. | CRA-C15; DORA-C17 | D-01.3 | 3.000 | P1 | INSPECT | NATIVE | AG-D-01.1-001, AG-D-01.3-001 | 3 (MUST AVG=3.000) | PR.DS-01 | PR.DS-P1; CT.DP-P2 | MEASURE-2.7; GOVERN-1.6 | PARTIAL | PARTIAL | PARTIAL | CRA-C15; DORA-C17 → AG-D-01.3-001/-002 → AG-D-01.1-001, AG-D-01.3-001 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-01.4-001 | Ensure data integrity controls and AI system resilience against manipulation, adversarial attacks, and unauthorized model modification. Implement integrity checksums and model versioning. | GDPR-C05; CRA-C09; AI-C18 | D-01.4 | 2.667 | P1 | TEST | NATIVE | AG-D-05.2-001, AG-D-01.4-001, AG-D-02.4-002 | 3 (MUST AVG=2.667; AI-C present forces MUST) | PR.DS-01; PR.DS-02 | PR.DS-P1; CT.DM-P1; CT.DM-P3 | MEASURE-2.6; MEASURE-2.7; MANAGE-2.3 | PARTIAL | PARTIAL | PARTIAL | GDPR-C05; CRA-C09; AI-C18 → AG-D-01.4-001/-002 → AG-D-05.2-001, AG-D-01.4-001, AG-D-02.4-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

*All rules STRUCTURAL (always active)*

### D-02: Vulnerability Management

|---------|-----------------|--------|------------|----|----------|-------------|----------------|---------------|-------------------------------|-------------|------------|----------------|---------------|------------------|----------------|
| CR-D-02.1-001 | Maintain zero known exploitable vulnerabilities in production systems. Implement continuous AI data governance and model vulnerability assessment. Deploy automated vulnerability scanning across all attack surfaces. | CRA-C01, C17; NIS2-C12; DORA-C08; AI-C03, C16 | D-02.1 | 3.000 | P1 | DEMONSTRATE | NATIVE | AG-D-02.1-002, AG-D-02.4-002, AG-D-04.1-002 | 3 (MUST AVG=3.000; AI-C present forces MUST) | ID.RA-01; ID.RA-08 | ID.RA-P3; ID.RA-P5 | MEASURE-2.1; MEASURE-2.3; MANAGE-1.3 | PARTIAL | PARTIAL | PARTIAL | CRA-C01, C17; NIS2-C12; DORA-C08; AI-C03, C16 → AG-D-02.1-001/-002 → AG-D-02.1-002, AG-D-02.4-002, AG-D-04.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-02.2-001 | Operate automated patch management with 72-hour SLA for critical vulnerabilities. Include AI model patches, dependency updates, and firmware updates in the patching scope. | CRA-C04, C19; NIS2-C12; DORA-C13 | D-02.2 | 3.000 | P1 | TEST | NATIVE | AG-D-02.1-002, AG-D-04.2-002 | 3 (MUST AVG=3.000) | PR.PS-02 | ALT-ANCHOR (SSDF PS.1; 800-53r5 SI-2) (no PF 1.0 analogue for product patch and OTA update management) | MANAGE-2.3 | PARTIAL | PARTIAL | PARTIAL | CRA-C04, C19; NIS2-C12; DORA-C13 → AG-D-02.2-001/-002 → AG-D-02.1-002, AG-D-04.2-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-02.3-001 | Maintain coordinated vulnerability disclosure policy with public-facing intake. Report critical incidents to ENISA/CSIRT within 24 hours. Include AI model vulnerabilities in disclosure scope. | CRA-C21, C26 | D-02.3 | 3.000 | P1 | INSPECT | NATIVE | AG-D-02.1-002, AG-D-04.1-002 | 3 (MUST AVG=3.000) | ID.RA-08 | ID.IM-P7; GV.PO-P5 | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | CRA-C21, C26 → AG-D-02.3-001/-002 → AG-D-02.1-002, AG-D-04.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-02.4-001 | Execute annual Threat-Led Penetration Testing (TLPT) per DORA RTS. Include comprehensive AI bias testing, adversarial robustness testing, and model inversion resistance assessment. | DORA-C27, C29; AI-C04 | D-02.4 | 3.000 | P1 | DEMONSTRATE | NATIVE | AG-D-02.1-002, AG-D-02.4-002, AG-D-04.1-002 | 3 (MUST AVG=3.000; AI-C present forces MUST) | ID.IM-02; ID.RA-03 | ID.RA-P3; ID.RA-P4; ID.RA-P5 | MEASURE-1.1; MEASURE-2.1; MEASURE-2.3; MAP-3.3; MEASURE-2.7 | PARTIAL | PARTIAL | PARTIAL | DORA-C27, C29; AI-C04 → AG-D-02.4-001/-002 → AG-D-02.1-002, AG-D-02.4-002, AG-D-04.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

*All rules STRUCTURAL (always active)*

### D-03: Access Control

|---------|-----------------|--------|------------|----|----------|-------------|----------------|---------------|-------------------------------|-------------|------------|----------------|---------------|------------------|----------------|
| CR-D-03.1-001 | Deploy unified identity management with MFA across all systems, cloud services, and AI platforms. Integrate with enterprise SSO and support phishing-resistant authentication mechanisms. | CRA-C05; NIS2-C16, C19; DORA-C11, C15; AI-C15 | D-03.1 | 3.000 | P1 | INSPECT | HYBRID | AG-D-03.1-002, AG-D-03.4-002 | 3 (MUST AVG=3.000; AI-C present forces MUST) | PR.AA-01; PR.AA-03; PR.AA-05 | CT.PO-P1 | GOVERN-1.4; MAP-3.4; GOVERN-2.1 | PARTIAL | PARTIAL | PARTIAL | CRA-C05; NIS2-C16, C19; DORA-C11, C15; AI-C15 → AG-D-03.1-001/-002 → AG-D-03.1-002, AG-D-03.4-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-03.2-001 | Enforce MFA for all privileged access, remote access, and AI system access. Require step-up authentication for high-risk financial transactions and model parameter changes. | CRA-C06; NIS2-C17; DORA-C16 | D-03.2 | 2.667 | P1 | TEST | HYBRID | AG-D-03.1-002, AG-D-03.4-002 | 2 (SHOULD AVG=2.667) | PR.AA-03 | ALT-ANCHOR (800-53r5 IA-2(1); ASVS V3.3) (no PF 1.0 MFA subcategory) | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | CRA-C06; NIS2-C17; DORA-C16 → AG-D-03.2-001/-002 → AG-D-03.1-002, AG-D-03.4-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-03.3-001 | Implement least privilege enforcement with quarterly access reviews for all systems. Include AI model access, training data access, and inference API access in review scope. | GDPR-C10, C17; NIS2-C20; DORA-C14 | D-03.3 | 3.000 | P1 | INSPECT | NATIVE | AG-D-03.1-002, AG-D-03.4-002, AG-D-03.3-002 | 3 (MUST AVG=3.000) | PR.AA-05; PR.AA-01 | CT.PO-P1 | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | GDPR-C10, C17; NIS2-C20; DORA-C14 → AG-D-03.3-001/-002 → AG-D-03.1-002, AG-D-03.4-002, AG-D-03.3-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-03.4-001 | Maintain secure default configuration per hardened-default baseline for all systems. Disable unused services, ports, and protocols. Harden AI inference endpoints and model serving infrastructure. **[SOLE AUTHORITY: CRA]** | CRA-C03 | D-03.4 | 3.000 | P1 | TEST | NATIVE | AG-D-03.4-002 | 3 (MUST AVG=3.000) | PR.PS-01 | CT.DP-P4; CT.PO-P4 | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | CRA-C03 → AG-D-03.4-001/-002 → AG-D-03.4-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

*All rules STRUCTURAL (always active)*

### D-04: Incident Response

|---------|-----------------|--------|------------|----|----------|-------------|----------------|---------------|-------------------------------|---------------------|-------------|------------|----------------|---------------|------------------|----------------|
| CR-D-04.1-001 | Operate 24/7 Security Operations Center (SOC) with automated incident detection, triage, and escalation. Include AI anomaly detection for model drift and adversarial attacks. | CRA-C13; NIS2-C28; DORA-C18, C21 | D-04.1 | 3.000 | P1 | DEMONSTRATE | NATIVE | AG-D-04.1-002, AG-D-10.1-002, AG-D-04.1-002 | 3 (MUST AVG=3.000) | STRUCTURAL — always active | DE.AE-02; DE.CM-01; DE.CM-09 | ID.RA-P3 | MEASURE-2.4; MEASURE-2.7 | PARTIAL | PARTIAL | PARTIAL | CRA-C13; NIS2-C28; DORA-C18, C21 → AG-D-04.1-001/-002 → AG-D-04.1-002, AG-D-10.1-002, AG-D-04.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-04.2-001 | Maintain business continuity program with 99.99% uptime SLA. Execute tested disaster recovery with RTO <= 4h and RPO <= 1h for critical financial systems. Include AI system failover and model recovery procedures. | GDPR-C18; CRA-C11; NIS2-C05; DORA-C19, C22, C24 | D-04.2 | 2.833 | P1 | DEMONSTRATE | NATIVE | AG-D-04.2-002, AG-D-04.1-002, AG-D-04.4-002 | 2 (SHOULD AVG=2.833) | STRUCTURAL — always active | RS.MI-01; RS.MI-02 | PR.PO-P7; CT.DM-P10 | MANAGE-2.3 <!-- U1 fill: RESPOND-1.* not in AI RMF 1.0; substituted MANAGE-2.3 --> | PARTIAL | PARTIAL | PARTIAL | GDPR-C18; CRA-C11; NIS2-C05; DORA-C19, C22, C24 → AG-D-04.2-001/-002 → AG-D-04.2-002, AG-D-04.1-002, AG-D-04.4-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-04.3-001 | Execute 24-hour universal incident notification workflow across all regulatory bodies (GDPR, CRA, NIS 2, DORA, AI Act). Resolves tension T-001 (conflicting notification timelines). Unified template with regulation-specific annexes. **[TENSION RESOLVED: T-001]** | GDPR-C21, C23; CRA-C25; NIS2-C25, C26, C27; DORA-C35, C36, C37; AI-C26, C29 | D-04.3 | 3.000 | P1 | TEST | NATIVE | AG-D-04.1-002, AG-D-10.1-002 | 3 (MUST AVG=3.000; AI-C present forces MUST) | **CONTEXTUAL** — multi-path notification activated when compound event satisfies triggers from 2+ of 5 regulations. DORA 4h initial report satisfies shortest deadline; GDPR 72h, CRA 24h, NIS 2 24h, AI Act 15d follow. See TENSION-H-001. | RS.CO-02; RS.CO-03 | CM.AW-P7; CM.PO-P2; CM.PO-P1; GV.PO-P5 | MANAGE-2.3; MANAGE-4.3; GOVERN-1.1 | PARTIAL | PARTIAL | PARTIAL | GDPR-C21, C23; CRA-C25; NIS2-C25, C26, C27; DORA-C35, C36, C37; AI-C26, C29 → AG-D-04.3-001/-002 → AG-D-04.1-002, AG-D-10.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-04.4-001 | Deploy redundant backup systems with automated failover for all critical data and AI models. Implement geographic distribution across EU data centers with sovereignty controls. | GDPR-C16; NIS2-C06; DORA-C23, C25 | D-04.4 | 2.750 | P1 | DEMONSTRATE | NATIVE | AG-D-04.2-002, AG-D-04.4-002 | 2 (SHOULD AVG=2.750) | STRUCTURAL — always active | RC.RP-01; RC.RP-03; RC.RP-05 | ALT-ANCHOR (800-53r5 CP-9; CP-10) (no PF 1.0 backup and DR recovery subcategory) | MANAGE-2.3 <!-- U1 fill: RECOVER-1.* not in AI RMF 1.0; substituted MANAGE-2.3 --> | PARTIAL | PARTIAL | PARTIAL | GDPR-C16; NIS2-C06; DORA-C23, C25 → AG-D-04.4-001/-002 → AG-D-04.2-002, AG-D-04.4-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-05: Data Lifecycle

|---------|-----------------|--------|------------|----|----------|-------------|----------------|---------------|-------------------------------|---------------------|-------------|------------|----------------|---------------|------------------|----------------|
| CR-D-05.1-001 | Enforce data minimization across all processing activities. Ensure AI training data relevance, representativeness, and freedom from prohibited bias proxies. Document data collection purposes. | GDPR-C01; CRA-C10; AI-C05, C06 | D-05.1 | 3.000 | P1 | INSPECT | NATIVE | AG-D-01.1-001, AG-D-02.4-002, AG-D-05.1-001 | 3 (MUST AVG=3.000; AI-C present forces MUST) | — | ID.AM-02; ID.AM-03 | CT.PO-P4; CT.DP-P4; ID.RA-P3 | GOVERN-1.4; MAP-2.1; MEASURE-2.11; MAP-2.2 | PARTIAL | PARTIAL | PARTIAL | GDPR-C01; CRA-C10; AI-C05, C06 → AG-D-05.1-001/-002 → AG-D-01.1-001, AG-D-02.4-002, AG-D-05.1-001 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-05.2-001 | Enforce tiered retention policy: 10-year retention for financial records (MiFID II), 5-year for operational records, 6-month for AI training logs and model inference records. Automated deletion upon expiry. | GDPR-C02, C03; AI-C07 | D-05.2 | 3.000 | P1 | INSPECT | NATIVE | AG-D-05.2-001, AG-D-05.1-001 | 3 (MUST AVG=3.000; AI-C present forces MUST) | — | PR.DS-01; PR.PS-06 | CT.PO-P4; CT.DM-P5 | MAP-2.1; MEASURE-2.4; MEASURE-2.11 | PARTIAL | PARTIAL | PARTIAL | GDPR-C02, C03; AI-C07 → AG-D-05.2-001/-002 → AG-D-05.2-001, AG-D-05.1-001 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-05.3-001 | Enable cryptographic sharding-based erasure within 30 days of request or retention expiry. Applies to PII, AI training data contributions, and model inference records. Resolves tension T-002 (GDPR erasure vs. NIS 2/DORA retention). **[TENSION RESOLVED: T-002]** | GDPR-C06; CRA-C16 | D-05.3 | 3.000 | P1 | TEST | NATIVE | AG-D-05.2-001, AG-D-05.1-001 | 3 (MUST AVG=3.000) | CONTEXTUAL — activated by erasure request when personal data exists in DORA-mandated audit logs. Cryptographic sharding resolves TENSION-H-002. | PR.DS-10 | CT.DM-P4; CT.DM-P5 | MAP-1.3; MANAGE-2.3 | PARTIAL | PARTIAL | PARTIAL | GDPR-C06; CRA-C16 → AG-D-05.3-001/-002 → AG-D-05.2-001, AG-D-05.1-001 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-05.4-001 | Enable data export in machine-readable formats within regulatory SLAs (GDPR: 30 days). Include AI model decisions, training data lineage, and credit scoring factors. **[SOLE AUTHORITY: GDPR]** | GDPR-C07 | D-05.4 | 3.000 | P1 | TEST | NATIVE | AG-D-05.4-001, AG-D-05.1-001 | 3 (MUST AVG=3.000) | — | — (não mapeado a CSF 2.0 — sem subcategoria directa) | CT.DM-P1; CT.DM-P6 | N/A (non-AI scope) | N/A — não mapeado a CSF 2.0 | PARTIAL | N/A (non-AI scope) | GDPR-C07 → AG-D-05.4-001/-002 → AG-D-05.4-001, AG-D-05.1-001 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-06: Supply Chain

|---------|-----------------|--------|------------|----|----------|-------------|----------------|---------------|-------------------------------|-------------|------------|----------------|---------------|------------------|----------------|
| CR-D-06.1-001 | Operate comprehensive vendor risk management program covering all DORA, NIS 2, and GDPR requirements. Assess all ICT third-party providers (TPPs) pre-engagement and annually. Include AI model providers and data suppliers. | GDPR-C11; NIS2-C08, C23; DORA-C30, C32 | D-06.1 | 3.000 | P1 | INSPECT | HYBRID | AG-D-06.1-002, AG-D-06.1-002 | 3 (MUST AVG=3.000) | GV.SC-04; GV.SC-07; ID.RA-10 | ID.IM-P2 | GOVERN-2.1; GOVERN-2.2 | PARTIAL | PARTIAL | PARTIAL | GDPR-C11; NIS2-C08, C23; DORA-C30, C32 → AG-D-06.1-001/-002 → AG-D-06.1-002, AG-D-06.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-06.2-001 | Maintain Software Bill of Materials (SBOM) for all products, services, and dependencies. Track open-source, commercial, and AI model dependencies. Update SBOM with each release and dependency change. **[SOLE AUTHORITY: CRA]** | CRA-C18 | D-06.2 | 3.000 | P1 | INSPECT | NATIVE | AG-D-06.1-002 | 3 (MUST AVG=3.000) | GV.SC-09 | ID.IM-P7 | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | CRA-C18 → AG-D-06.2-001/-002 → AG-D-06.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-06.3-001 | Enforce contractual security obligations with all third parties, including cloud providers, AI vendors, and data processors. Include audit rights, breach notification SLAs, and regulatory cooperation clauses. | GDPR-C12; NIS2-C09; DORA-C31 | D-06.3 | 3.000 | P1 | INSPECT | HYBRID | AG-D-06.1-002, AG-D-06.1-002 | 3 (MUST AVG=3.000) | GV.SC-05; GV.SC-06 | GV.PO-P5 | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | GDPR-C12; NIS2-C09; DORA-C31 → AG-D-06.3-001/-002 → AG-D-06.1-002, AG-D-06.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-06.4-001 | Manage third-party concentration risk with documented exit strategies for all critical vendors. Include AI model provider alternatives and data migration plans. Test exit strategies annually. | NIS2-C24; DORA-C33, C34 | D-06.4 | 3.000 | P1 | INSPECT | NATIVE | AG-D-06.1-002, AG-D-06.1-002, AG-D-06.4-002 | 3 (MUST AVG=3.000) | DE.CM-06; PR.IR-01 | ALT-ANCHOR (800-53r5 PE-3; PE-6) (no PF 1.0 analogue for third-party boundary isolation) | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | NIS2-C24; DORA-C33, C34 → AG-D-06.4-001/-002 → AG-D-06.1-002, AG-D-06.1-002, AG-D-06.4-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

*All rules STRUCTURAL (always active)*

### D-07: Secure Development

|---------|-----------------|--------|------------|----|----------|-------------|----------------|---------------|-------------------------------|---------------------|-------------|------------|----------------|---------------|------------------|----------------|
| CR-D-07.1-001 | Implement privacy by design and security by design per CRA secure-by-default standard across all development activities. Resolves tension T-004 (secure-by-default vs. privacy minimization). Include AI model governance and ethical design reviews. **[TENSION RESOLVED: T-004]** | GDPR-C09; CRA-C02, C22 | D-07.1 | 2.667 | P1 | INSPECT | NATIVE | AG-D-01.3-001, AG-D-03.4-002, AG-D-07.2-002 | 2 (SHOULD AVG=2.667) | STRUCTURAL — always active. Follow CRA higher bar (NI=3) satisfies GDPR (NI=2). See TENSION-L-001. | PR.PS-06; ID.RA-01 | GV.PO-P2; CT.PO-P4; CT.DP-P2; CT.DP-P5 | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | GDPR-C09; CRA-C02, C22 → AG-D-07.1-001/-002 → AG-D-01.3-001, AG-D-03.4-002, AG-D-07.2-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-07.2-001 | Enforce industry secure-coding standards with mandatory static and dynamic analysis mechanisms in all development pipelines. Include AI code repositories, model training scripts, and data pipeline code. | NIS2-C11; DORA-C20 | D-07.2 | 3.000 | P1 | DEMONSTRATE | NATIVE | AG-D-07.2-002, AG-D-07.3-002 | 3 (MUST AVG=3.000) | — | PR.PS-06 | ALT-ANCHOR (SSDF PW.1; 800-53r5 SA-8) (no PF 1.0 secure-SDLC subcategory) | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | NIS2-C11; DORA-C20 → AG-D-07.2-001/-002 → AG-D-07.2-002, AG-D-07.3-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-07.3-001 | Maintain CI/CD pipeline with automated security gates (SAST, DAST, SCA, secrets detection, IaC scanning). Block deployment on critical findings. Include ML pipeline security gates for model training and deployment. | NIS2-C11; DORA-C20 | D-07.3 | 3.000 | P1 | DEMONSTRATE | NATIVE | AG-D-07.2-002, AG-D-07.3-002 | 3 (MUST AVG=3.000) | — | PR.PS-06; PR.PS-02 | PR.PO-P4 | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | NIS2-C11; DORA-C20 → AG-D-07.3-001/-002 → AG-D-07.2-002, AG-D-07.3-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-07.4-001 | Operate formal change management with dual control approval and independent oversight for all production changes. Include AI model changes, parameter updates, and retraining triggers. | NIS2-C10; DORA-C06 | D-07.4 | 3.000 | P1 | INSPECT | NATIVE | AG-D-07.2-002, AG-D-07.3-002 | 3 (MUST AVG=3.000) | — | ID.RA-07 | ID.RA-P3 | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | NIS2-C10; DORA-C06 → AG-D-07.4-001/-002 → AG-D-07.2-002, AG-D-07.3-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-08: Human Factors

|---------|-----------------|--------|------------|----|----------|-------------|----------------|---------------|-------------------------------|-------------|------------|----------------|---------------|------------------|----------------|
| CR-D-08.1-001 | Deliver annual security awareness training to all 5000+ employees with role-specific modules for developers, operations, and management. Track completion and effectiveness metrics. | GDPR-C27; NIS2-C14 | D-08.1 | 3.000 | P2 | INSPECT | NATIVE | AG-D-08.2-002, AG-D-08.1-002 | 3 (MUST AVG=3.000) | PR.AT-01 | GV.AT-P1; GV.AT-P2 | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | GDPR-C27; NIS2-C14 → AG-D-08.1-001/-002 → AG-D-08.2-002, AG-D-08.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-08.2-001 | Maintain role-specific security competence programs with mandatory certification for privileged roles. Implement AI human oversight procedures with designated human reviewers for high-risk AI decisions. | GDPR-C28; NIS2-C15; AI-C14, C24 | D-08.2 | 3.000 | P1 | INSPECT | NATIVE | AG-D-02.4-002, AG-D-08.2-002, AG-D-08.1-002 | 3 (MUST AVG=3.000; AI-C present forces MUST) | PR.AT-02 | GV.AT-P1; GV.AT-P2 | MAP-3.5; GOVERN-2.1; GOVERN-2.2; GOVERN-3.1 | PARTIAL | PARTIAL | PARTIAL | GDPR-C28; NIS2-C15; AI-C14, C24 → AG-D-08.2-001/-002 → AG-D-02.4-002, AG-D-08.2-002, AG-D-08.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-08.3-001 | Provide management board training on DORA and NIS 2 requirements. Establish ICT risk oversight with board-level accountability and quarterly reporting. Include AI governance and regulatory compliance briefing. | NIS2-C02; DORA-C02 | D-08.3 | 3.000 | P1 | INSPECT | NATIVE | AG-D-08.2-002, AG-D-09.1-001 | 3 (MUST AVG=3.000) | GV.RR-01; PR.AT-02 | ALT-ANCHOR (SAMM G-EG-A-1; 800-53r5 AT-2) (no PF 1.0 board-training subcategory) | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | NIS2-C02; DORA-C02 → AG-D-08.3-001/-002 → AG-D-08.2-002, AG-D-09.1-001 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

*All rules STRUCTURAL (always active)*

### D-09: Governance & Documentation

|---------|-----------------|--------|------------|----|----------|-------------|----------------|---------------|-------------------------------|---------------------|-------------|------------|----------------|---------------|------------------|----------------|
| CR-D-09.1-001 | Maintain unified Information Security Management System (ISMS) covering all 5 regulatory frameworks (GDPR, CRA, NIS 2, DORA, AI Act). Preserve documentation for minimum 10 years. Include AI governance framework and model documentation. | GDPR-C08, C25, C26; CRA-C24; NIS2-C01, C03; DORA-C01, C03; AI-C08, C12, C13, C20, C23 | D-09.1 | 2.846 | P1 | INSPECT | NATIVE | AG-D-09.1-001, AG-D-09.4-001, AG-D-09.3-002 | 3 (MUST AVG=2.846; AI-C present forces MUST) | — | GV.PO-01; GV.PO-02 | GV.PO-P1; GV.PO-P5; CM.PO-P1 | GOVERN-1.1; GOVERN-1.3; GOVERN-2.1 | PARTIAL | PARTIAL | PARTIAL | GDPR-C08, C25, C26; CRA-C24; NIS2-C01, C03; DORA-C01, C03; AI-C08, C12, C13, C20, C23 → AG-D-09.1-001/-002 → AG-D-09.1-001, AG-D-09.4-001, AG-D-09.3-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-09.2-001 | Execute unified Integrated Privacy and Security Risk Assessments (IPSARA) combining DPIA, FRIA, cybersecurity risk assessment, and ICT risk assessment. Resolves tension T-003 (assessment overlap). Include AI risk assessment per AI Act requirements. **[TENSION RESOLVED: T-003]** | GDPR-C20, C24; CRA-C23; NIS2-C04; DORA-C04; AI-C01, C02, C22, C28 | D-09.2 | 2.889 | P1 | INSPECT | NATIVE | AG-D-09.1-001, AG-D-09.4-001, AG-D-09.3-002 | 3 (MUST AVG=2.889; AI-C present forces MUST) | STRUCTURAL — always active. All 5 assessment triggers (GDPR DPIA, CRA risk assessment, NIS 2 risk analysis, DORA ICT risk, AI Act FRIA) permanently satisfied by bank business model. IPSARA framework unifies. | ID.RA-04; ID.RA-05; GV.RM-06 | ID.RA-P3; ID.RA-P4; ID.RA-P5 | GOVERN-1.5; MAP-5.1; MANAGE-1.2 | PARTIAL | PARTIAL | PARTIAL | GDPR-C20, C24; CRA-C23; NIS2-C04; DORA-C04; AI-C01, C02, C22, C28 → AG-D-09.2-001/-002 → AG-D-09.1-001, AG-D-09.4-001, AG-D-09.3-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-09.3-001 | Maintain comprehensive asset and ICT inventory with automated discovery and continuous reconciliation. Include AI models, training datasets, inference endpoints, and model registry entries. | NIS2-C07; DORA-C05 | D-09.3 | 3.000 | P1 | INSPECT | NATIVE | AG-D-09.4-001, AG-D-09.3-002 | 3 (MUST AVG=3.000) | — | ID.AM-01; ID.AM-02; ID.AM-07 | ID.IM-P1; ID.IM-P4; ID.IM-P6; ID.IM-P8 | N/A (non-AI scope) | PARTIAL | PARTIAL | N/A (non-AI scope) | NIS2-C07; DORA-C05 → AG-D-09.3-001/-002 → AG-D-09.4-001, AG-D-09.3-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-09.4-001 | Maintain records of processing activities, AI system traceability documentation, and regulatory compliance documentation. Include model cards, data sheets, and AI decision logs. | GDPR-C13, C22; DORA-C38; AI-C11 | D-09.4 | 3.000 | P1 | INSPECT | NATIVE | AG-D-09.4-001, AG-D-09.3-002 | 3 (MUST AVG=3.000; AI-C present forces MUST) | — | ID.AM-07; GV.OC-03 | ID.IM-P1; ID.IM-P4; ID.IM-P6; ID.IM-P8; CM.PO-P1 | GOVERN-1.4; MAP-1.1; MAP-3.4 | PARTIAL | PARTIAL | PARTIAL | GDPR-C13, C22; DORA-C38; AI-C11 → AG-D-09.4-001/-002 → AG-D-09.4-001, AG-D-09.3-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-10: Monitoring & Audit

|---------|-----------------|--------|------------|----|----------|-------------|----------------|---------------|-------------------------------|---------------------|-------------|------------|----------------|---------------|------------------|----------------|
| CR-D-10.1-001 | Deploy 24/7 continuous security monitoring with AI-powered threat detection across all systems, networks, and AI pipelines. Include real-time model drift detection, adversarial attack detection, and data exfiltration monitoring. | CRA-C12; NIS2-C21, C29; DORA-C07; AI-C19, C25 | D-10.1 | 3.000 | P1 | TEST | HYBRID | AG-D-10.1-002, AG-D-04.1-002, AG-D-10.1-002 | 3 (MUST AVG=3.000; AI-C present forces MUST) | — | DE.CM-01; DE.CM-09; DE.AE-02 | CM.AW-P7 | MANAGE-4.1; MEASURE-3.1; MEASURE-4.1; GOVERN-1.5; MEASURE-2.4 | PARTIAL | PARTIAL | PARTIAL | CRA-C12; NIS2-C21, C29; DORA-C07; AI-C19, C25 → AG-D-10.1-001/-002 → AG-D-10.1-002, AG-D-04.1-002, AG-D-10.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-10.2-001 | Maintain immutable audit logs with PII data separation and AI system traceability. Implement cryptographic sharding for log integrity. Ensure log retention per regulatory requirements (min. 5 years for financial, 6 months for AI inference). **[TENSION RESOLVED: T-002]** | CRA-C14; NIS2-C22; DORA-C12; AI-C09, C10 | D-10.2 | 3.000 | P1 | TEST | HYBRID | AG-D-10.1-002, AG-D-04.1-002, AG-D-10.1-002 | 3 (MUST AVG=3.000; AI-C present forces MUST) | STRUCTURAL — always active. DORA immutable log retention runs concurrently with potential erasure requests (TENSION-H-002). Cryptographic sharding enables both. | PR.PS-04; DE.AE-03; RS.AN-06 | CT.DM-P9 | MEASURE-2.4; MEASURE-3.1; GOVERN-1.6 | PARTIAL | PARTIAL | PARTIAL | CRA-C14; NIS2-C22; DORA-C12; AI-C09, C10 → AG-D-10.2-001/-002 → AG-D-10.1-002, AG-D-04.1-002, AG-D-10.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| CR-D-10.3-001 | Execute annual penetration testing, TLPT, resilience testing, and periodic AI model evaluation. Include red team exercises for AI systems, adversarial robustness testing, and model inversion attack simulations. | GDPR-C19; CRA-C20; NIS2-C13; DORA-C26, C28; AI-C21, C27 | D-10.3 | 2.857 | P1 | DEMONSTRATE | NATIVE | AG-D-10.1-002, AG-D-04.1-002, AG-D-10.1-002 | 3 (MUST AVG=2.857; AI-C present forces MUST) | — | ID.IM-01; ID.IM-02; ID.IM-03 | ALT-ANCHOR (800-53r5 CA-2; CA-7) (no PF 1.0 compliance-testing subcategory) | MEASURE-1.1; MEASURE-2.1; MEASURE-2.3; MEASURE-2.7; MAP-3.3 | PARTIAL | PARTIAL | PARTIAL | GDPR-C19; CRA-C20; NIS2-C13; DORA-C26, C28; AI-C21, C27 → AG-D-10.3-001/-002 → AG-D-10.1-002, AG-D-04.1-002, AG-D-10.1-002 | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

---

## 5. BEST PRACTICE RULES

Best practice rules supplement compliance rules with framework-specific implementation guidance. They carry Priority P3 and articulate the AEGIS methodology with established industry standards.

### D-01: Data Protection & Encryption

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|-----------------|---------------------|------------|----------|-------------|----------------|------------------------|-----------------|-------------|------------|----------------|---------------|------------------|----------------|
| BPR-D-01.1-001 | Implement industry-standard symmetric encryption with authenticated mode for all data at rest. Use authenticated encryption for financial data per industry block-cipher standards. | ISO 27001:2022 A.8.24; documented storage cryptographic standard | D-01.1 | P3 | INSPECT | NATIVE | CR-D-01.1-001 | 2 (SHOULD P3 AVG=2.000) | PR.DS-01; PR.DS-10 | PR.DS-P1; CT.DP-P2 | N/A (non-AI scope) | PARTIAL | PARTIAL | ISO 27001:2022 A.8.24; documented storage cryptographic standard → AG-D-01.1-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-01.2-001 | Deploy modern transport cryptographic standard with forward secrecy. Disable deprecated protocol versions and weak cipher suites. Implement certificate transparency monitoring and stapling. | documented transport cryptographic standard; SC-8 | D-01.2 | P3 | TEST | NATIVE | CR-D-01.2-001 | 2 (SHOULD P3 AVG=2.000) | PR.DS-02 | PR.DS-P2 | N/A (non-AI scope) | PARTIAL | PARTIAL | documented transport cryptographic standard; SC-8 → AG-D-01.2-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-01.3-001 | Implement cryptographic material custody with segregated lifecycle per industry key-management standards. Use validated modules and automate material rotation with defined cryptographic periods. | documented key-management standard | D-01.3 | P3 | INSPECT | NATIVE | CR-D-01.3-001 | 2 (SHOULD P3 AVG=2.000) | PR.DS-01 | PR.DS-P1; CT.DP-P2 | N/A (non-AI scope) | PARTIAL | PARTIAL | documented key-management standard → AG-D-01.3-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-01.4-001 | Deploy data integrity controls using cryptographic hash functions (SHA-256+). Implement file integrity monitoring (FIM) for critical system files and AI model artifacts. | ISO 27001:2022 A.8.28; NIST SC-28 | D-01.4 | P3 | TEST | NATIVE | CR-D-01.4-001 | 2 (SHOULD P3 AVG=2.000) | PR.DS-01; PR.DS-02 | PR.DS-P1; CT.DM-P1; CT.DM-P3 | N/A (non-AI scope) | PARTIAL | PARTIAL | ISO 27001:2022 A.8.28; NIST SC-28 → AG-D-01.4-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-02: Vulnerability Management

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|-----------------|---------------------|------------|----------|-------------|----------------|------------------------|-----------------|-------------|------------|----------------|---------------|------------------|----------------|
| BPR-D-02.1-001 | Execute quarterly vulnerability scanning covering all external and internal assets. Use authenticated scanning with CVSS v3.1 scoring. Remediate Critical/High within SLA. | industry security testing standards (V1); NIST RA-5; CIS Control 7 | D-02.1 | P3 | DEMONSTRATE | NATIVE | CR-D-02.1-001 | 2 (SHOULD P3 AVG=2.000) | ID.RA-01; DE.CM-01 | ID.RA-P3; ID.RA-P5 | N/A (non-AI scope) | PARTIAL | PARTIAL | industry security testing standards (V1); NIST RA-5; CIS Control 7 → AG-D-02.1-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-02.2-001 | Maintain machine-readable bill-of-materials (SPDX and industry-standard structured formats) for all products. Automate BoM generation in CI/CD pipeline. Monitor BoM components for known vulnerabilities. | documented supply-chain risk standard; EO 14028 | D-06.2 | P3 | INSPECT | NATIVE | CR-D-06.2-001 | 2 (SHOULD P3 AVG=2.000) | GV.SC-09 | ID.IM-P7 | N/A (non-AI scope) | PARTIAL | PARTIAL | documented supply-chain risk standard; EO 14028 → AG-D-06.2-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-02.3-001 | Implement vulnerability management program with risk-based prioritization. Integrate threat intelligence feeds for exploitability assessment. Track vulnerability metrics (MTTD, MTTR). | ISO 27001:2022 A.8.8; NIST SI-2 | D-02.2 | P3 | INSPECT | NATIVE | CR-D-02.2-001 | 2 (SHOULD P3 AVG=2.000) | PR.PS-02 | ALT-ANCHOR (SSDF PW.7; 800-53r5 RA-5; SAMM V-ST-A) (no PF 1.0 analogue for CVD best practice) | N/A (non-AI scope) | PARTIAL | PARTIAL | ISO 27001:2022 A.8.8; NIST SI-2 → AG-D-02.2-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-02.4-001 | Execute annual TLPT per DORA RTS with TIBER-EU methodology. Include scope definition, threat intelligence-led red team testing, and remediation tracking. | DORA RTS on TLPT; TIBER-EU | D-02.4 | P3 | DEMONSTRATE | NATIVE | CR-D-02.4-001 | 2 (SHOULD P3 AVG=2.000) | ID.IM-02; ID.RA-03 | ID.RA-P3; ID.RA-P4; ID.RA-P5 | N/A (non-AI scope) | PARTIAL | PARTIAL | DORA RTS on TLPT; TIBER-EU → AG-D-02.4-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-03: Access Control

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|-----------------|---------------------|------------|----------|-------------|----------------|------------------------|-----------------|-------------|------------|----------------|---------------|------------------|----------------|
| BPR-D-03.1-001 | Implement Role-Based Access Control (RBAC) with defined roles, permissions, and separation of duties. Automate provisioning/deprovisioning via HR system integration. | ISO 27001:2022 A.9.2; NIST AC-2 | D-03.1 | P3 | INSPECT | HYBRID | CR-D-03.1-001 | 2 (SHOULD P3 AVG=2.000) | PR.AA-01; PR.AA-05 | CT.PO-P1 | N/A (non-AI scope) | PARTIAL | PARTIAL | ISO 27001:2022 A.9.2; NIST AC-2 → AG-D-03.1-001/-002 → related CRs: HYBRID | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-03.2-001 | Deploy phishing-resistant authentication mechanisms for MFA across all user-facing applications. Support hardware security tokens for privileged accounts. Implement phishing-resistant authentication per documented identity assurance framework AAL3. | documented identity assurance framework (IA-2); industry phishing-resistant auth standards | D-03.2 | P3 | TEST | HYBRID | CR-D-03.2-001 | 2 (SHOULD P3 AVG=2.000) | PR.AA-03 | ALT-ANCHOR (800-53r5 IA-2(1); ASVS V3.3) (no PF 1.0 MFA subcategory — best practice) | N/A (non-AI scope) | PARTIAL | PARTIAL | documented identity assurance framework (IA-2); industry phishing-resistant auth standards → AG-D-03.2-001/-002 → related CRs: HYBRID | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-03.3-001 | Implement Privileged Access Management (PAM) with just-in-time access, session recording, and credential vaulting. Apply zero trust principles to all privileged operations. | NIST AC-6; CIS Control 6 | D-03.3 | P3 | INSPECT | NATIVE | CR-D-03.3-001 | 2 (SHOULD P3 AVG=2.000) | PR.AA-05; PR.AA-01 | CT.PO-P1 | N/A (non-AI scope) | PARTIAL | PARTIAL | NIST AC-6; CIS Control 6 → AG-D-03.3-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-03.4-001 | Apply hardened-default baseline Level 2 for all server, network, and cloud configurations. Automate configuration compliance scanning with documented open-source configuration tool or equivalent. | hardened-default baseline v8 | D-03.4 | P3 | TEST | NATIVE | CR-D-03.4-001 | 2 (SHOULD P3 AVG=2.000) | PR.PS-01 | CT.DP-P4; CT.PO-P4 | N/A (non-AI scope) | PARTIAL | PARTIAL | hardened-default baseline v8 → AG-D-03.4-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-04: Incident Response

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|-----------------|---------------------|------------|----------|-------------|----------------|------------------------|-----------------|-------------|------------|----------------|---------------|------------------|----------------|
| BPR-D-04.1-001 | Develop and maintain incident response playbooks covering all incident types (data breach, ransomware, AI model compromise, supply chain attack). Align with ISO 27001 incident management. | ISO 27001:2022 A.5.24, A.5.26; NIST IR-8 | D-04.1 | P3 | INSPECT | NATIVE | CR-D-04.1-001 | 2 (SHOULD P3 AVG=2.000) | DE.AE-02; DE.CM-01 | CM.AW-P7 | N/A (non-AI scope) | PARTIAL | PARTIAL | ISO 27001:2022 A.5.24, A.5.26; NIST IR-8 → AG-D-04.1-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-04.2-001 | Maintain Business Continuity Plan (BCP) and Disaster Recovery Plan (DRP) per ISO 22301. Test BCP annually with full-scale exercises. Test DRP semi-annually with failover drills. | ISO 22301:2019; NIST CP-2, CP-10 | D-04.2 | P3 | DEMONSTRATE | NATIVE | CR-D-04.2-001 | 2 (SHOULD P3 AVG=2.000) | RS.MI-01; RS.MI-02 | PR.PO-P7; CT.DM-P10 | N/A (non-AI scope) | PARTIAL | PARTIAL | ISO 22301:2019; NIST CP-2, CP-10 → AG-D-04.2-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-04.3-001 | Conduct tabletop exercises quarterly for incident response teams. Include cross-functional participants (security, legal, compliance, communications, AI governance). Track lessons learned and remediation. | NIST CSF 2.0 RS.MA-01; NIST IR-3 | D-04.3 | P3 | DEMONSTRATE | NATIVE | CR-D-04.3-001 | 2 (SHOULD P3 AVG=2.000) | RS.CO-02; RS.CO-03 | CM.AW-P7; CM.PO-P2; CM.PO-P1; GV.PO-P5 | N/A (non-AI scope) | PARTIAL | PARTIAL | NIST CSF 2.0 RS.MA-01; NIST IR-3 → AG-D-04.3-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-04.4-001 | Implement automated backup verification with regular restore testing. Maintain immutable backups isolated from production. Test backup integrity quarterly with full restore drills. | NIST CP-9; ISO 27001:2022 A.8.13 | D-04.4 | P3 | DEMONSTRATE | NATIVE | CR-D-04.4-001 | 2 (SHOULD P3 AVG=2.000) | RC.RP-01; RC.RP-03; RC.RP-05 | ALT-ANCHOR (800-53r5 CP-9; CP-10) (no PF 1.0 backup and DR recovery subcategory — best practice) | N/A (non-AI scope) | PARTIAL | PARTIAL | NIST CP-9; ISO 27001:2022 A.8.13 → AG-D-04.4-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-05: Data Lifecycle

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|-----------------|---------------------|------------|----------|-------------|----------------|------------------------|-----------------|-------------|------------|----------------|---------------|------------------|----------------|
| BPR-D-05.1-001 | Implement data classification schema with automated data discovery and tagging. Apply classification-based handling rules for storage, transmission, and destruction. | ISO 27001:2022 A.8.2, A.8.3; NIST AC-16 | D-05.1 | P3 | INSPECT | NATIVE | CR-D-05.1-001 | 2 (SHOULD P3 AVG=2.000) | PR.DS-10; ID.AM-03 | CT.PO-P4; CT.DP-P4; ID.RA-P3 | N/A (non-AI scope) | PARTIAL | PARTIAL | ISO 27001:2022 A.8.2, A.8.3; NIST AC-16 → AG-D-05.1-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-05.3-001 | Execute media sanitization per documented media sanitization standard (Clear, Purge, Destroy). Apply cryptographic erase for encrypted data. Document sanitization for audit trail. | documented media sanitization standard | D-05.3 | P3 | INSPECT | NATIVE | CR-D-05.3-001 | 2 (SHOULD P3 AVG=2.000) | PR.DS-10 | CT.DM-P4; CT.DM-P5 | N/A (non-AI scope) | PARTIAL | PARTIAL | documented media sanitization standard → AG-D-05.3-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-05.4-001 | Implement automated data lifecycle management with policy-based retention and deletion. Support GDPR-compliant data portability with standardized export formats (JSON, CSV). | ISO 27001:2022 A.8.10; NIST AC-4 | D-05.4 | P3 | TEST | NATIVE | CR-D-05.4-001 | 2 (SHOULD P3 AVG=2.000) | — (não mapeado a CSF 2.0 — sem subcategoria directa) | CT.DM-P1; CT.DM-P6 | N/A (non-AI scope) | N/A — não mapeado a CSF 2.0 | PARTIAL | ISO 27001:2022 A.8.10; NIST AC-4 → AG-D-05.4-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-06: Supply Chain

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|-----------------|---------------------|------------|----------|-------------|----------------|------------------------|-----------------|-------------|------------|----------------|---------------|------------------|----------------|
| BPR-D-06.1-001 | Assess vendor security using Standardized Information Gathering (SIG) or Cloud Controls Matrix (CAIQ). Require documented third-party security attestation or ISO 27001 certification for critical vendors. | SIG Lite v7; CSA CAIQ v4 | D-06.1 | P3 | INSPECT | HYBRID | CR-D-06.1-001 | 2 (SHOULD P3 AVG=2.000) | GV.SC-04; GV.SC-07 | ID.IM-P2 | N/A (non-AI scope) | PARTIAL | PARTIAL | SIG Lite v7; CSA CAIQ v4 → AG-D-06.1-001/-002 → related CRs: HYBRID | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-06.3-001 | Include minimum security requirements in all vendor contracts: right to audit, breach notification within 24h, data processing agreements, subcontractor controls, and regulatory cooperation. | ISO 27001:2022 A.5.19, A.5.20; NIST SA-9 | D-06.3 | P3 | INSPECT | HYBRID | CR-D-06.3-001 | 2 (SHOULD P3 AVG=2.000) | GV.SC-05; GV.SC-06 | GV.PO-P5 | N/A (non-AI scope) | PARTIAL | PARTIAL | ISO 27001:2022 A.5.19, A.5.20; NIST SA-9 → AG-D-06.3-001/-002 → related CRs: HYBRID | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-06.4-001 | Develop vendor exit strategies with data migration plans, service transition procedures, and alternative provider identification. Test exit procedures annually for critical vendors. | Managed Hosting Best Practices; documented supply-chain risk standard | D-06.4 | P3 | INSPECT | NATIVE | CR-D-06.4-001 | 2 (SHOULD P3 AVG=2.000) | DE.CM-06; PR.IR-01 | ALT-ANCHOR (800-53r5 PE-3; PE-6) (no PF 1.0 analogue for third-party boundary isolation — best practice) | N/A (non-AI scope) | PARTIAL | PARTIAL | Managed Hosting Best Practices; documented supply-chain risk standard → AG-D-06.4-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-07: Secure Development

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|-----------------|---------------------|------------|----------|-------------|----------------|------------------------|-----------------|-------------|------------|----------------|---------------|------------------|----------------|
| BPR-D-07.1-001 | Implement industry secure software development framework practices across all development teams. Include Prepare, Protect, Produce, and Respond activities. Integrate with existing SDLC. | documented secure software development framework | D-07.1 | P3 | INSPECT | NATIVE | CR-D-07.1-001 | 2 (SHOULD P3 AVG=2.000) | PR.PS-06; ID.RA-01 | GV.PO-P2; CT.PO-P4; CT.DP-P2; CT.DP-P5 | N/A (non-AI scope) | PARTIAL | PARTIAL | documented secure software development framework → AG-D-07.1-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-07.2-001 | Deploy static and dynamic analysis tools per industry security testing standards Level 2 requirements in CI/CD pipeline. Enforce quality gates blocking deployment on High/Critical findings. Include dependency scanning and secrets detection. | industry security testing standards (V3, V4); V14; NIST SI-2 | D-07.2 | P3 | DEMONSTRATE | NATIVE | CR-D-07.2-001 | 2 (SHOULD P3 AVG=2.000) | PR.PS-06 | ALT-ANCHOR (SSDF PW.1; 800-53r5 SA-8) (no PF 1.0 secure-SDLC subcategory — best practice) | N/A (non-AI scope) | PARTIAL | PARTIAL | industry security testing standards (V3, V4); V14; NIST SI-2 → AG-D-07.2-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-07.3-001 | Implement infrastructure-as-code (IaC) scanning with documented open-source IaC scanner or equivalent. Scan container images for vulnerabilities and misconfigurations before deployment. | documented container security standard; hardened-default baseline Control 16 | D-07.3 | P3 | TEST | NATIVE | CR-D-07.3-001 | 2 (SHOULD P3 AVG=2.000) | PR.PS-06; PR.PS-02 | PR.PO-P4 | N/A (non-AI scope) | PARTIAL | PARTIAL | documented container security standard; hardened-default baseline Control 16 → AG-D-07.3-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-07.4-001 | Apply change management controls with peer review, automated testing, and dual approval for production deployments. Maintain change advisory board (CAB) for high-risk changes. | ISO 27001:2022 A.8.29, A.8.32; NIST CM-3 | D-07.4 | P3 | INSPECT | NATIVE | CR-D-07.4-001 | 2 (SHOULD P3 AVG=2.000) | ID.RA-07 | ID.RA-P3 | N/A (non-AI scope) | PARTIAL | PARTIAL | ISO 27001:2022 A.8.29, A.8.32; NIST CM-3 → AG-D-07.4-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-08: Human Factors

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|-----------------|---------------------|------------|----------|-------------|----------------|------------------------|-----------------|-------------|------------|----------------|---------------|------------------|----------------|
| BPR-D-08.1-001 | Deliver security awareness training per SANS security awareness framework. Include phishing simulations, social engineering defense, secure coding for developers, and AI ethics for data science teams. | SANS Security Awareness; ISO 27001:2022 A.6.3 | D-08.1 | P3 | INSPECT | NATIVE | CR-D-08.1-001 | 2 (SHOULD P3 AVG=2.000) | PR.AT-01 | GV.AT-P1; GV.AT-P2 | N/A (non-AI scope) | PARTIAL | PARTIAL | SANS Security Awareness; ISO 27001:2022 A.6.3 → AG-D-08.1-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-08.2-001 | Establish security competence framework with role-based certification paths. Require CISSP/CISM for security roles, cloud certifications for operations, and AI governance training for ML teams. | NIST NICE Framework; ISO 27001:2022 A.6.3 | D-08.2 | P3 | INSPECT | NATIVE | CR-D-08.2-001 | 2 (SHOULD P3 AVG=2.000) | PR.AT-02 | GV.AT-P1; GV.AT-P2 | N/A (non-AI scope) | PARTIAL | PARTIAL | NIST NICE Framework; ISO 27001:2022 A.6.3 → AG-D-08.2-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-08.3-001 | Provide executive cyber risk reporting with board-level dashboards. Include regulatory compliance status, risk metrics, incident trends, and AI governance indicators. | NIST CSF 2.0 GV.OC; ISO 27001:2022 A.5.1 | D-08.3 | P3 | INSPECT | NATIVE | CR-D-08.3-001 | 2 (SHOULD P3 AVG=2.000) | GV.RR-01; PR.AT-02 | ALT-ANCHOR (SAMM G-EG-A-1; 800-53r5 AT-2) (no PF 1.0 board-training subcategory — best practice) | N/A (non-AI scope) | PARTIAL | PARTIAL | NIST CSF 2.0 GV.OC; ISO 27001:2022 A.5.1 → AG-D-08.3-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-09: Governance & Documentation

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|-----------------|---------------------|------------|----------|-------------|----------------|------------------------|-----------------|-------------|------------|----------------|---------------|------------------|----------------|
| BPR-D-09.1-001 | Implement ISMS per ISO 27001:2022 with risk assessment, treatment plan, statement of applicability, and management review. Integrate regulatory compliance requirements into ISMS scope. | ISO 27001:2022; ISO 27002:2022 | D-09.1 | P3 | INSPECT | NATIVE | CR-D-09.1-001 | 2 (SHOULD P3 AVG=2.000) | GV.PO-01; GV.PO-02 | GV.PO-P1; GV.PO-P5 | N/A (non-AI scope) | PARTIAL | PARTIAL | ISO 27001:2022; ISO 27002:2022 → AG-D-09.1-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-09.2-001 | Conduct risk assessments per ISO 27005 methodology. Include asset-based risk analysis, threat modeling, vulnerability assessment, and residual risk calculation. Include AI-specific risk factors. | ISO 27005:2022; documented risk assessment standard | D-09.2 | P3 | INSPECT | NATIVE | CR-D-09.2-001 | 2 (SHOULD P3 AVG=2.000) | ID.RA-04; ID.RA-05; GV.RM-06 | ID.RA-P3; ID.RA-P4; ID.RA-P5 | N/A (non-AI scope) | PARTIAL | PARTIAL | ISO 27005:2022; documented risk assessment standard → AG-D-09.2-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-09.3-001 | Maintain AI governance framework per NIST AI Risk Management Framework (AI RMF). Include AI risk mapping, measurement, and management. Document AI system inventory with risk categorization. | NIST AI RMF 1.0 | D-09.2 | P3 | INSPECT | NATIVE | CR-D-09.2-001 | 2 (SHOULD P3 AVG=2.000) | GV.PO-01; GV.PO-02 | GV.PO-P1; GV.PO-P5 | GOVERN-1.1; GOVERN-1.4; GOVERN-1.5 | PARTIAL | PARTIAL | NIST AI RMF 1.0 → AG-D-09.2-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-09.4-001 | Implement AI transparency documentation per IEEE 7000 standard. Include model cards, data sheets, algorithmic impact assessments, and stakeholder transparency reports. | IEEE 7000-2021 | D-09.1 | P3 | INSPECT | NATIVE | CR-D-09.1-001 | 2 (SHOULD P3 AVG=2.000) | GV.PO-01; GV.PO-02 | GV.PO-P1; GV.PO-P5 | GOVERN-1.1; GOVERN-1.4; GOVERN-1.5 | PARTIAL | PARTIAL | IEEE 7000-2021 → AG-D-09.1-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-10: Monitoring & Audit

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|-----------------|---------------------|------------|----------|-------------|----------------|------------------------|-----------------|-------------|------------|----------------|---------------|------------------|----------------|
| BPR-D-10.1-001 | Deploy centralized audit-log/automated-orchestration platform with automated threat correlation, incident orchestration, and response playbooks. Integrate with all data sources: network, endpoint, cloud, application, and AI system logs. | documented incident response standard; SI-4 | D-10.1 | P3 | TEST | HYBRID | CR-D-10.1-001 | 2 (SHOULD P3 AVG=2.000) | DE.CM-01; DE.CM-09; DE.AE-02 | CM.AW-P7 | N/A (non-AI scope) | PARTIAL | PARTIAL | documented incident response standard; SI-4 → AG-D-10.1-001/-002 → related CRs: HYBRID | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-10.2-001 | Implement centralized log management per documented log management standard. Ensure log integrity with cryptographic hashing. Separate PII-bearing logs with access controls. Retain logs per regulatory requirements. | documented log management standard; AU-2, AU-3, AU-11 | D-10.2 | P3 | TEST | HYBRID | CR-D-10.2-001 | 2 (SHOULD P3 AVG=2.000) | PR.PS-04; DE.AE-03; RS.AN-06 | CT.DM-P9 | N/A (non-AI scope) | PARTIAL | PARTIAL | documented log management standard; AU-2, AU-3, AU-11 → AG-D-10.2-001/-002 → related CRs: HYBRID | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-10.3-001 | Execute penetration testing per industry security testing framework v4. Include web application, API, infrastructure, and AI system testing. Engage independent third-party testers annually. | industry security testing framework (v4); PT-ES | D-10.3 | P3 | DEMONSTRATE | NATIVE | CR-D-10.3-001 | 2 (SHOULD P3 AVG=2.000) | ID.IM-01; ID.IM-02; ID.IM-03 | ALT-ANCHOR (800-53r5 CA-2; CA-7) (no PF 1.0 compliance-testing subcategory — best practice) | N/A (non-AI scope) | PARTIAL | PARTIAL | industry security testing framework (v4); PT-ES → AG-D-10.3-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

### D-12: AI-Specific Best Practices

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|-----------------|---------------------|------------|----------|-------------|----------------|------------------------|-----------------|-------------|------------|----------------|---------------|------------------|----------------|
| BPR-D-12.1-001 | Implement AI bias testing per NIST AI RMF 2.0. Test for demographic parity, equalized odds, and predictive parity across protected attributes. Document bias test results in model cards. | NIST AI RMF 2.0; NIST IR 8437 | D-02.4 | P3 | DEMONSTRATE | NATIVE | CR-D-02.4-001 | 2 (SHOULD P3 AVG=2.000) | ID.IM-02; ID.RA-03 | ID.RA-P3; ID.RA-P4; ID.RA-P5 | MEASURE-2.11 | PARTIAL | PARTIAL | NIST AI RMF 2.0; NIST IR 8437 → AG-D-02.4-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-12.2-001 | Deploy AI model monitoring for drift detection, performance degradation, and data quality. Implement automated retraining triggers and model rollback procedures. | NIST AI RMF 1.0 (Measure); MLOps Best Practices | D-10.1 | P3 | TEST | NATIVE | CR-D-10.1-001 | 2 (SHOULD P3 AVG=2.000) | DE.CM-01; DE.CM-09; DE.AE-02 | CM.AW-P7 | MANAGE-4.1; MEASURE-3.1 | PARTIAL | PARTIAL | NIST AI RMF 1.0 (Measure); MLOps Best Practices → AG-D-10.1-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-12.3-001 | Implement AI human oversight procedures per EU AI Act guidelines. Define human intervention thresholds, override mechanisms, and escalation paths for high-risk AI decisions (credit scoring). | EU AI Act Art. 14; European Commission AI Act Guidelines | D-08.2 | P3 | INSPECT | NATIVE | CR-D-08.2-001 | 2 (SHOULD P3 AVG=2.000) | PR.AT-02 | GV.AT-P1; GV.AT-P2 | MAP-3.5; GOVERN-2.1; GOVERN-3.1 | PARTIAL | PARTIAL | EU AI Act Art. 14; European Commission AI Act Guidelines → AG-D-08.2-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |
| BPR-D-12.4-001 | Maintain AI adversarial robustness testing per MITRE ATLAS framework. Test for data poisoning, model evasion, model inversion, membership inference, and prompt injection attacks. | MITRE ATLAS; NIST AI RMF (Manage) | D-02.1 | P3 | DEMONSTRATE | NATIVE | CR-D-02.1-001 | 2 (SHOULD P3 AVG=2.000) | ID.RA-01; ID.RA-08 | ID.RA-P3; ID.RA-P5 | MEASURE-2.7 | PARTIAL | PARTIAL | MITRE ATLAS; NIST AI RMF (Manage) → AG-D-02.1-001/-002 → related CRs: NATIVE | CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc20 §1 aggregate view |

---

## 6. RULES DASHBOARD

### Summary Statistics

| Metric | Value |
|--------|-------|
| **Total Compliance Rules (CR)** | 38 |
| **Total Best Practice Rules (BPR)** | 25 |
| **Total Rules** | 63 |
| **Sub-Domain Coverage** | 38/38 (100%) |
| **Regulations Covered** | 5/5 (GDPR, CRA, NIS 2, DORA, AI Act) |
| **Strategic Tensions Resolved** | 4/4 (T-001, T-002, T-003, T-004) |
| **Sole Authority Gaps Identified** | 2 (D-03.4: CRA, D-05.4: GDPR, D-06.2: CRA) |

### Rules by Domain

| Domain | Sub-Domains | Compliance Rules | Best Practice Rules | Total Rules |
|--------|-------------|-----------------|-------------------|-------------|
| D-01: Data Protection & Encryption | 4 | 4 | 4 | 8 |
| D-02: Vulnerability Management | 4 | 4 | 4 | 8 |
| D-03: Access Control | 4 | 4 | 4 | 8 |
| D-04: Incident Response | 4 | 4 | 4 | 8 |
| D-05: Data Lifecycle | 4 | 4 | 3 | 7 |
| D-06: Supply Chain | 4 | 4 | 3 | 7 |
| D-07: Secure Development | 4 | 4 | 4 | 8 |
| D-08: Human Factors | 3 | 3 | 3 | 6 |
| D-09: Governance & Documentation | 4 | 4 | 4 | 8 |
| D-10: Monitoring & Audit | 3 | 3 | 3 | 6 |
| D-12: AI-Specific Best Practices | (cross-domain) | 0 | 4 | 4 |
| **TOTAL** | **38** | **38** | **25** | **63** |

### Rules by Priority

| Priority | Criteria | Count | Percentage |
|----------|----------|-------|------------|
| P1 | NI >= 2.5 | 37 | 58.7% |
| P2 | NI 2.0–2.499 | 1 | 1.6% |
| P3 | Best Practice | 25 | 39.7% |
| **TOTAL** | **63** | **100%** |

### Rules by Verification Method

| Verification Method | Count | Description |
|--------------------|-------|-------------|
| INSPECT | 25 | Review of documentation, configurations, policies |
| TEST | 16 | Technical testing of controls |
| DEMONSTRATE | 12 | Operational demonstration, exercises, simulations |
| ANALYZE | 10 | Analysis of data, logs, metrics |

### Rules by Implementation Mode

| Implementation Mode | Count | Percentage | Description |
|-------------------|-------|------------|-------------|
| NATIVE | 46 | 73.0% — Built/operated in-house by OmniBank |
| HYBRID | 17 | 27.0% — Combination of in-house and cloud/third-party |
| INHERITED | 0 | 0.0% — Fully inherited from cloud providers |

---

## 7. SUB-DOMAIN COVERAGE MATRIX

All 38 sub-domains are covered by at least one compliance rule:

| Sub-Domain | Compliance Rule | Best Practice Rules | Status |
|------------|----------------|-------------------|--------|
| D-01.1 | CR-D-01.1-001 | BPR-D-01.1-001 | COVERED |
| D-01.2 | CR-D-01.2-001 | BPR-D-01.2-001 | COVERED |
| D-01.3 | CR-D-01.3-001 | BPR-D-01.3-001 | COVERED |
| D-01.4 | CR-D-01.4-001 | BPR-D-01.4-001 | COVERED |
| D-02.1 | CR-D-02.1-001 | BPR-D-02.1-001, BPR-D-12.4-001 | COVERED |
| D-02.2 | CR-D-02.2-001 | BPR-D-02.3-001 | COVERED |
| D-02.3 | CR-D-02.3-001 | — | COVERED |
| D-02.4 | CR-D-02.4-001 | BPR-D-02.4-001, BPR-D-12.1-001 | COVERED |
| D-03.1 | CR-D-03.1-001 | BPR-D-03.1-001 | COVERED |
| D-03.2 | CR-D-03.2-001 | BPR-D-03.2-001 | COVERED |
| D-03.3 | CR-D-03.3-001 | BPR-D-03.3-001 | COVERED |
| D-03.4 | CR-D-03.4-001 | BPR-D-03.4-001 | COVERED [SOLE: CRA] |
| D-04.1 | CR-D-04.1-001 | BPR-D-04.1-001 | COVERED |
| D-04.2 | CR-D-04.2-001 | BPR-D-04.2-001 | COVERED |
| D-04.3 | CR-D-04.3-001 | BPR-D-04.3-001 | COVERED [TENSION RESOLVED] |
| D-04.4 | CR-D-04.4-001 | BPR-D-04.4-001 | COVERED |
| D-05.1 | CR-D-05.1-001 | BPR-D-05.1-001 | COVERED |
| D-05.2 | CR-D-05.2-001 | — | COVERED |
| D-05.3 | CR-D-05.3-001 | BPR-D-05.3-001 | COVERED [TENSION RESOLVED] |
| D-05.4 | CR-D-05.4-001 | BPR-D-05.4-001 | COVERED [SOLE: GDPR] |
| D-06.1 | CR-D-06.1-001 | BPR-D-06.1-001 | COVERED |
| D-06.2 | CR-D-06.2-001 | BPR-D-02.2-001 | COVERED [SOLE: CRA] |
| D-06.3 | CR-D-06.3-001 | BPR-D-06.3-001 | COVERED |
| D-06.4 | CR-D-06.4-001 | BPR-D-06.4-001 | COVERED |
| D-07.1 | CR-D-07.1-001 | BPR-D-07.1-001 | COVERED [TENSION RESOLVED] |
| D-07.2 | CR-D-07.2-001 | BPR-D-07.2-001 | COVERED |
| D-07.3 | CR-D-07.3-001 | BPR-D-07.3-001 | COVERED |
| D-07.4 | CR-D-07.4-001 | BPR-D-07.4-001 | COVERED |
| D-08.1 | CR-D-08.1-001 | BPR-D-08.1-001 | COVERED |
| D-08.2 | CR-D-08.2-001 | BPR-D-08.2-001, BPR-D-12.3-001 | COVERED |
| D-08.3 | CR-D-08.3-001 | BPR-D-08.3-001 | COVERED |
| D-09.1 | CR-D-09.1-001 | BPR-D-09.1-001, BPR-D-09.4-001 | COVERED |
| D-09.2 | CR-D-09.2-001 | BPR-D-09.2-001, BPR-D-09.3-001 | COVERED [TENSION RESOLVED] |
| D-09.3 | CR-D-09.3-001 | — | COVERED |
| D-09.4 | CR-D-09.4-001 | — | COVERED |
| D-10.1 | CR-D-10.1-001 | BPR-D-10.1-001, BPR-D-12.2-001 | COVERED |
| D-10.2 | CR-D-10.2-001 | BPR-D-10.2-001 | COVERED [TENSION RESOLVED] |
| D-10.3 | CR-D-10.3-001 | BPR-D-10.3-001 | COVERED |

---

## 8. RULES BY SUB-DOMAIN DISTRIBUTION

Each sub-domain's rule density reveals where the regulatory burden concentrates. With 5 regulations applying to every sub-domain, Case 3 shows a much more even distribution than Case 1 (which had 18 uncovered sub-domains).

| Sub-Domain | Compliance Rules | Best Practice Rules | Total | Avg NI | Dominant Type | Primary Regulations |
|------------|-----------------|---------------------|-------|--------|---------------|-------------------|
| D-01.1 | CR-D-01.1-001 | BPR-D-01.1-001 | 2 | 2.667 | Compliance | All 5 |
| D-01.2 | CR-D-01.2-001 | BPR-D-01.2-001 | 2 | 2.667 | Compliance | GDPR, CRA, DORA |
| D-01.3 | CR-D-01.3-001 | BPR-D-01.3-001 | 2 | 3.000 | Compliance | CRA, DORA |
| D-01.4 | CR-D-01.4-001 | BPR-D-01.4-001 | 2 | 2.667 | Compliance | GDPR, CRA, AI Act |
| D-02.1 | CR-D-02.1-001 | BPR-D-02.1-001 | 2 | 3.000 | Compliance | CRA, NIS 2, DORA, AI Act |
| D-02.2 | CR-D-02.2-001 | BPR-D-02.3-001 | 2 | 3.000 | Compliance | CRA, NIS 2, DORA |
| D-02.3 | CR-D-02.3-001 | — | 1 | 3.000 | Compliance | CRA only |
| D-02.4 | CR-D-02.4-001 | BPR-D-02.4-001, BPR-D-12.1-001 | 3 | 3.000 | Mixed | DORA, AI Act |
| D-03.1 | CR-D-03.1-001 | BPR-D-03.1-001 | 2 | 3.000 | Compliance | CRA, NIS 2, DORA, AI Act |
| D-03.2 | CR-D-03.2-001 | BPR-D-03.2-001 | 2 | 2.667 | Compliance | CRA, NIS 2, DORA |
| D-03.3 | CR-D-03.3-001 | BPR-D-03.3-001 | 2 | 3.000 | Compliance | GDPR, NIS 2, DORA |
| D-03.4 | CR-D-03.4-001 | BPR-D-03.4-001 | 2 | 3.000 | Mixed | CRA only [SOLE] |
| D-04.1 | CR-D-04.1-001 | BPR-D-04.1-001 | 2 | 3.000 | Compliance | CRA, NIS 2, DORA |
| D-04.2 | CR-D-04.2-001 | BPR-D-04.2-001 | 2 | 2.833 | Compliance | GDPR, CRA, NIS 2, DORA |
| D-04.3 | CR-D-04.3-001 | BPR-D-04.3-001 | 2 | 3.000 | Compliance | All 5 [T-001] |
| D-04.4 | CR-D-04.4-001 | BPR-D-04.4-001 | 2 | 2.750 | Compliance | GDPR, NIS 2, DORA |
| D-05.1 | CR-D-05.1-001 | BPR-D-05.1-001 | 2 | 3.000 | Compliance | GDPR, CRA, AI Act |
| D-05.2 | CR-D-05.2-001 | — | 1 | 3.000 | Compliance | GDPR, AI Act |
| D-05.3 | CR-D-05.3-001 | BPR-D-05.3-001 | 2 | 3.000 | Compliance | GDPR, CRA [T-002] |
| D-05.4 | CR-D-05.4-001 | BPR-D-05.4-001 | 2 | 3.000 | Compliance | GDPR only [SOLE] |
| D-06.1 | CR-D-06.1-001 | BPR-D-06.1-001 | 2 | 3.000 | Compliance | GDPR, NIS 2, DORA |
| D-06.2 | CR-D-06.2-001 | BPR-D-02.2-001 | 2 | 3.000 | Compliance | CRA only [SOLE] |
| D-06.3 | CR-D-06.3-001 | BPR-D-06.3-001 | 2 | 3.000 | Compliance | GDPR, NIS 2, DORA |
| D-06.4 | CR-D-06.4-001 | BPR-D-06.4-001 | 2 | 3.000 | Compliance | NIS 2, DORA |
| D-07.1 | CR-D-07.1-001 | BPR-D-07.1-001 | 2 | 2.667 | Mixed | GDPR, CRA [T-004] |
| D-07.2 | CR-D-07.2-001 | BPR-D-07.2-001 | 2 | 3.000 | Compliance | NIS 2, DORA |
| D-07.3 | CR-D-07.3-001 | BPR-D-07.3-001 | 2 | 3.000 | Compliance | NIS 2, DORA |
| D-07.4 | CR-D-07.4-001 | BPR-D-07.4-001 | 2 | 3.000 | Compliance | NIS 2, DORA |
| D-08.1 | CR-D-08.1-001 | BPR-D-08.1-001 | 2 | 3.000 | Compliance | GDPR, NIS 2 |
| D-08.2 | CR-D-08.2-001 | BPR-D-08.2-001, BPR-D-12.3-001 | 3 | 3.000 | Mixed | GDPR, NIS 2, AI Act |
| D-08.3 | CR-D-08.3-001 | BPR-D-08.3-001 | 2 | 3.000 | Compliance | NIS 2, DORA |
| D-09.1 | CR-D-09.1-001 | BPR-D-09.1-001, BPR-D-09.4-001 | 3 | 2.846 | Mixed | All 5 |
| D-09.2 | CR-D-09.2-001 | BPR-D-09.2-001, BPR-D-09.3-001 | 3 | 2.889 | Mixed | All 5 [T-003] |
| D-09.3 | CR-D-09.3-001 | — | 1 | 3.000 | Compliance | NIS 2, DORA |
| D-09.4 | CR-D-09.4-001 | — | 1 | 3.000 | Compliance | GDPR, DORA, AI Act |
| D-10.1 | CR-D-10.1-001 | BPR-D-10.1-001, BPR-D-12.2-001 | 3 | 3.000 | Mixed | CRA, NIS 2, DORA, AI Act |
| D-10.2 | CR-D-10.2-001 | BPR-D-10.2-001 | 2 | 3.000 | Compliance | CRA, NIS 2, DORA, AI Act [T-002] |
| D-10.3 | CR-D-10.3-001 | BPR-D-10.3-001 | 2 | 2.857 | Mixed | All 5 |
| **TOTAL** | **38** | **25** | **63** | **2.934** | **Compliance** | **5/5 regulations** |

**Distribution Analysis:**
- **Highest density sub-domains (3 rules each):** D-02.4, D-08.2, D-09.1, D-09.2, D-10.1 — all AI Act + DORA overlap areas
- **Lowest density sub-domains (1 rule each):** D-02.3, D-05.2, D-09.3, D-09.4 — single or dual regulation coverage
- **Sole Authority sub-domains:** D-03.4 (CRA), D-05.4 (GDPR), D-06.2 (CRA) — if these regulations were excluded, these sub-domains would have zero regulatory mandate
- **Tension-resolved sub-domains:** D-04.3 (T-001), D-05.3 (T-002), D-09.2 (T-003), D-07.1 (T-004), D-10.2 (T-002)

---

## 9. IMPLEMENTATION MODE DISTRIBUTION

Rules are classified by how OmniBank implements them: **NATIVE** (built/operated in-house), **HYBRID** (combination of in-house and cloud/third-party), or **INHERITED** (fully inherited from cloud providers).

### 9.1 By Implementation Mode

| Implementation Mode | Compliance Rules | Best Practice Rules | Total | % of Total | Description |
|-------------------|-----------------|---------------------|-------|------------|-------------|
| **NATIVE** | 28 | 18 | 46 | 73.0% | Built and operated in-house by OmniBank |
| **HYBRID** | 10 | 7 | 17 | 27.0% | Combination of in-house controls and cloud/third-party services |
| **INHERITED** | 0 | 0 | 0 | 0.0% | Fully inherited from cloud providers (none for OmniBank) |
| **TOTAL** | **38** | **25** | **63** | **100%** | — |

### 9.2 HYBRID Rules Detail

| Rule ID | Sub-Domain | Hybrid Components | Third-Party Provider |
|---------|------------|-------------------|---------------------|
| CR-D-03.1-001 | D-03.1 | Identity management with cloud IdP | External cloud identity providers |
| CR-D-03.2-001 | D-03.2 | MFA with cloud-based authenticator | External cloud MFA services |
| CR-D-06.1-001 | D-06.1 | Vendor risk assessment with third-party scoring | External vendor-scoring platforms |
| CR-D-06.3-001 | D-06.3 | Contractual security with cloud providers | External cloud providers (multiple vendors) |
| CR-D-10.1-001 | D-10.1 | Centralized audit-log platform with managed threat intelligence | External managed audit-log platforms |
| CR-D-10.2-001 | D-10.2 | Audit logging with cloud storage | External cloud audit/monitoring services |
| BPR-D-03.1-001 | D-03.1 | RBAC with cloud IdP integration | External cloud identity providers |
| BPR-D-03.2-001 | D-03.2 | Phishing-resistant authentication with cloud identity | External cloud identity providers |
| BPR-D-06.1-001 | D-06.1 | Vendor assessment platforms | Industry vendor-assessment platforms |
| BPR-D-10.1-001 | D-10.1 | Centralized audit-log/automated-orchestration platform | External managed automated-orchestration platforms |
| BPR-D-10.2-001 | D-10.2 | Cloud log management | External cloud monitoring services |

### 9.3 Implementation Mode Rationale

**Why 0% INHERITED:** Unlike cloud-native companies (e.g., small SaaS vendors with full external cloud-provider infrastructure), OmniBank operates a hybrid on-premise + cloud architecture with strict ECB/BaFin data sovereignty requirements. Even cloud-hosted services are configured and managed by OmniBank's own security teams, so they are classified as HYBRID rather than INHERITED.

**Why 73% NATIVE:** OmniBank's very high security maturity (dedicated security org of 100+ people, ISO 27001 certified) means most controls are built and operated internally. This includes the SOC, incident response, security architecture, AI governance, and compliance processes. *(legacy design text — superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0, port Fase 4)*

**Why 27% HYBRID:** Identity management, vendor risk scoring, and centralized audit-log/cloud logging require specialized third-party platforms that are not feasible to build in-house at scale.

---

## 10. TRACEABILITY MATRIX

### Rules to Goals

Each compliance rule maps to one or more privacy or security goals from Doc17_Privacy_Security_Objectives.md:

| Goal ID | Goal Type | Goal Description | Related Rules |
|---------|-----------|-----------------|---------------|
| AG-D-01.1-001 | Privacy | Encrypt all personal/financial/AI data at rest | CR-D-01.1-001 |
| AG-D-01.2-001 | Privacy | Data crossing network boundaries protected by confidentiality mechanisms | CR-D-01.2-001 |
| AG-D-01.3-001 | Privacy | Cryptographic material custody with documented lifecycle | CR-D-01.3-001 |
| AG-D-01.4-001 | Privacy | Data integrity and AI system resilience | CR-D-01.4-001 |
| AG-D-05.1-001 | Privacy | Data minimization; AI training data relevance | CR-D-05.1-001 |
| AG-D-05.2-001 | Privacy | Enforce tiered retention (5-10yr financial, 6mo AI) | CR-D-05.2-001 |
| AG-D-05.3-001 | Privacy | Cryptographic sharding-based erasure within 30 days | CR-D-05.3-001 |
| AG-D-05.4-001 | Privacy | Data export in machine-readable formats within SLAs | CR-D-05.4-001 |
| AG-D-07.1-001 | Privacy | Privacy/security by design per CRA standard | CR-D-07.1-001 |
| AG-D-09.1-001 | Privacy | Unified ISMS covering all 5 regulatory frameworks | CR-D-09.1-001 |
| AG-D-09.2-001 | Privacy | IPSARA unified risk assessments | CR-D-09.2-001 |
| AG-D-09.4-001 | Privacy | Records of processing, AI traceability | CR-D-09.4-001 |
| AG-D-02.1-002 | Security | Zero known exploitable vulnerabilities; AI data governance | CR-D-02.1-001 |
| AG-D-02.2-002 | Security | Automated patch management with 72h SLA | CR-D-02.2-001 |
| AG-D-02.3-002 | Security | Coordinated vulnerability disclosure policy | CR-D-02.3-001 |
| AG-D-02.4-002 | Security | Annual TLPT; AI bias testing | CR-D-02.4-001 |
| AG-D-03.1-002 | Security | Unified identity management with MFA | CR-D-03.1-001 |
| AG-D-03.2-002 | Security | MFA for privileged, remote, and AI access | CR-D-03.2-001 |
| AG-D-03.3-002 | Security | Least privilege with quarterly access reviews | CR-D-03.3-001 |
| AG-D-03.4-002 | Security | Secure default configuration per hardened-default baseline | CR-D-03.4-001 |
| AG-D-04.1-002 | Security | 24/7 SOC with automated detection and triage | CR-D-04.1-001 |
| AG-D-04.2-002 | Security | Business continuity with 99.99% uptime | CR-D-04.2-001 |
| AG-D-04.3-002 | Security | 24h universal incident notification workflow | CR-D-04.3-001 |
| AG-D-04.4-002 | Security | Redundant backup systems with automated failover | CR-D-04.4-001 |
| AG-D-06.1-002 | Security | Comprehensive vendor risk management | CR-D-06.1-001 |
| AG-D-06.2-002 | Security | Maintain SBOM for all products | CR-D-06.2-001 |
| AG-D-06.3-002 | Security | Contractual security obligations with all third parties | CR-D-06.3-001 |
| AG-D-06.4-002 | Security | Third-party concentration risk management | CR-D-06.4-001 |
| AG-D-07.2-002 | Security | Secure coding per industry standards | CR-D-07.2-001 |
| AG-D-07.3-002 | Security | CI/CD pipeline with automated security gates | CR-D-07.3-001 |
| AG-D-07.4-002 | Security | Formal change management with dual control | CR-D-07.4-001 |
| AG-D-08.1-002 | Security | Annual security awareness training for 5000+ employees | CR-D-08.1-001 |
| AG-D-08.2-002 | Security | Role-specific security competence; AI human oversight | CR-D-08.2-001 |
| AG-D-08.3-002 | Security | Management board DORA/NIS 2 training | CR-D-08.3-001 |
| AG-D-09.3-002 | Security | Comprehensive asset/ICT inventory | CR-D-09.3-001 |
| AG-D-10.1-002 | Security | 24/7 continuous monitoring with AI threat detection | CR-D-10.1-001 |
| AG-D-10.2-002 | Security | Immutable audit logs with PII separation | CR-D-10.2-001 |
| AG-D-10.3-002 | Security | Annual pentesting, TLPT, periodic AI evaluation | CR-D-10.3-001 |

**Mapping statistics:** 38 compliance rules → 33 goals (12 Privacy + 22 Security). Some rules map to multiple goals (e.g., CR-D-01.4-001 maps to both AG-D-01.4-001 and AG-D-02.1-002 for AI integrity).

### Rules to Obligations (1:1 Mapping)

Each of the 38 compliance rules maps to exactly one obligation from Doc15_Obligation_Derivation.md:

| Obligation ID | Rule ID | Sub-Domain |
|--------------|---------|------------|
| OBL-D-01.1-001 | CR-D-01.1-001 | D-01.1 |
| OBL-D-01.2-001 | CR-D-01.2-001 | D-01.2 |
| OBL-D-01.3-001 | CR-D-01.3-001 | D-01.3 |
| OBL-D-01.4-001 | CR-D-01.4-001 | D-01.4 |
| OBL-D-02.1-001 | CR-D-02.1-001 | D-02.1 |
| OBL-D-02.2-001 | CR-D-02.2-001 | D-02.2 |
| OBL-D-02.3-001 | CR-D-02.3-001 | D-02.3 |
| OBL-D-02.4-001 | CR-D-02.4-001 | D-02.4 |
| OBL-D-03.1-001 | CR-D-03.1-001 | D-03.1 |
| OBL-D-03.2-001 | CR-D-03.2-001 | D-03.2 |
| OBL-D-03.3-001 | CR-D-03.3-001 | D-03.3 |
| OBL-D-03.4-001 | CR-D-03.4-001 | D-03.4 |
| OBL-D-04.1-001 | CR-D-04.1-001 | D-04.1 |
| OBL-D-04.2-001 | CR-D-04.2-001 | D-04.2 |
| OBL-D-04.3-001 | CR-D-04.3-001 | D-04.3 |
| OBL-D-04.4-001 | CR-D-04.4-001 | D-04.4 |
| OBL-D-05.1-001 | CR-D-05.1-001 | D-05.1 |
| OBL-D-05.2-001 | CR-D-05.2-001 | D-05.2 |
| OBL-D-05.3-001 | CR-D-05.3-001 | D-05.3 |
| OBL-D-05.4-001 | CR-D-05.4-001 | D-05.4 |
| OBL-D-06.1-001 | CR-D-06.1-001 | D-06.1 |
| OBL-D-06.2-001 | CR-D-06.2-001 | D-06.2 |
| OBL-D-06.3-001 | CR-D-06.3-001 | D-06.3 |
| OBL-D-06.4-001 | CR-D-06.4-001 | D-06.4 |
| OBL-D-07.1-001 | CR-D-07.1-001 | D-07.1 |
| OBL-D-07.2-001 | CR-D-07.2-001 | D-07.2 |
| OBL-D-07.3-001 | CR-D-07.3-001 | D-07.3 |
| OBL-D-07.4-001 | CR-D-07.4-001 | D-07.4 |
| OBL-D-08.1-001 | CR-D-08.1-001 | D-08.1 |
| OBL-D-08.2-001 | CR-D-08.2-001 | D-08.2 |
| OBL-D-08.3-001 | CR-D-08.3-001 | D-08.3 |
| OBL-D-09.1-001 | CR-D-09.1-001 | D-09.1 |
| OBL-D-09.2-001 | CR-D-09.2-001 | D-09.2 |
| OBL-D-09.3-001 | CR-D-09.3-001 | D-09.3 |
| OBL-D-09.4-001 | CR-D-09.4-001 | D-09.4 |
| OBL-D-10.1-001 | CR-D-10.1-001 | D-10.1 |
| OBL-D-10.2-001 | CR-D-10.2-001 | D-10.2 |
| OBL-D-10.3-001 | CR-D-10.3-001 | D-10.3 |

### Strategic Tension Resolution

| Tension ID | Tension Description | Resolved By Rule | Resolution Approach |
|------------|-------------------|-----------------|-------------------|
| T-001 | Conflicting incident notification timelines across 5 regulations | CR-D-04.3-001 | Unified 24h notification workflow with regulation-specific annexes |
| T-002 | GDPR erasure right vs. NIS 2/DORA retention requirements | CR-D-05.3-001, CR-D-10.2-001 | Cryptographic sharding-based erasure with PII-separated audit logs |
| T-003 | Overlapping risk assessment requirements (DPIA, FRIA, cyber, ICT) | CR-D-09.2-001 | Unified IPSARA methodology combining all assessment types |
| T-004 | CRA secure-by-default vs. GDPR data minimization conflict | CR-D-07.1-001 | Privacy/security by design integration with secure defaults that minimize data collection |

---

## 11. PHASE 2 GATE CHECKLIST

| Gate Criterion | Status | Evidence |
|---------------|--------|---------|
| All obligations derived from Phase 1 clauses | PASS | Doc15_Obligation_Derivation.md — 38 obligations |
| All strategic tensions identified and resolved | PASS | Doc16_Strategic_Tensions_Report.md — 4 tensions resolved |
| All privacy/security goals defined | PASS | Doc17_Privacy_Security_Objectives.md — 27 goals |
| 1:1 obligation-to-rule mapping achieved | PASS | 38 obligations → 38 compliance rules |
| All 38 sub-domains covered | PASS | Coverage matrix — 38/38 (100%) |
| Best practice rules defined for all domains | PASS | 25 best practice rules across all 10 domains + AI |
| Verification method assigned to each rule | PASS | TEST/INSPECT/DEMONSTRATE/ANALYZE assigned |
| Implementation mode assigned to each rule | PASS | NATIVE/HYBRID assigned |
| Priority assigned based on NI | PASS | P1/P2/P3 assigned per NI thresholds |
| Traceability to goals and obligations | PASS | Full traceability matrix documented |
| Excel catalog synchronized | PASS | 12_Rules_Catalog.xlsx — all 63 rules |
| Phase 2 documents internally consistent | PASS | Cross-reference check passed |

**Phase 2 Gate Result: PASS (12/12 criteria met)**

---

## 12. KEY OBSERVATIONS

1. **Maximum Complexity Profile:** OmniBank presents the highest complexity of all AEGIS cases with 5000+ employees, cross-border EU operations, AI-driven credit scoring, and full coverage of all 5 regulatory frameworks. This results in the largest rules catalog (63 rules vs. ~40-50 for lower complexity cases).

2. **DORA Dominance:** DORA contributes the highest density of rules due to its comprehensive ICT risk management requirements for financial entities. 12 of 38 compliance rules reference DORA clauses, reflecting the regulatory intensity of the financial sector.

3. **Zero Coverage Gaps:** All 38 sub-domains have at least one compliance rule. This is achieved through the 1:1 obligation-to-rule derivation method, ensuring complete regulatory coverage. Two sub-domains (D-03.4, D-05.4) have sole authority from single regulations.

4. **Four Strategic Tensions Resolved:** The unified incident notification workflow (T-001), cryptographic sharding erasure (T-002), unified IPSARA assessments (T-003), and privacy/security by design integration (T-004) represent the most complex tension resolutions in the AEGIS methodology.

5. **High NATIVE Implementation Ratio:** 73% of rules are implemented natively by OmniBank, reflecting the financial institution's mature in-house security capabilities. 27% are hybrid, primarily for cloud infrastructure and identity services.

6. **AI-Specific Rules:** Four dedicated AI best practice rules (BPR-D-12.x) supplement compliance rules with NIST AI RMF, adversarial robustness testing, bias testing, and human oversight procedures. AI considerations are also embedded in 10+ compliance rules across multiple domains.

7. **Framework Articulation Depth:** Best practice rules articulate with 4 NIST frameworks (NIST CSF 2.0, NIST Privacy FW 1.0, NIST AI RMF 1.0, NIST AI RMF 1.0 Measure sub-function) plus ISO 27001:2022, hardened-default baseline, and IEEE 7000. This provides comprehensive implementation guidance for each compliance rule.

8. **Regulatory Clause Density:** The rules catalog covers approximately 120+ unique regulatory clauses across 5 regulations. The highest-density rules (CR-D-09.1-001, CR-D-09.2-001, CR-D-04.3-001) each reference 10+ source clauses, demonstrating the consolidation value of the AEGIS methodology.

---


## Annex A — CSF 2.0 Function Index (generated, port Fase 5)

| Function | Controls anchoring at least one subcategory of the function |
|---|---|
| GV (GOVERN) | 7 controls: CR-D-06.1-001, CR-D-06.2-001, CR-D-06.3-001, CR-D-08.3-001, CR-D-09.1-001, CR-D-09.2-001, CR-D-09.4-001 |
| ID (IDENTIFY) | 11 controls: CR-D-02.1-001, CR-D-02.3-001, CR-D-02.4-001, CR-D-05.1-001, CR-D-06.1-001, CR-D-07.1-001, CR-D-07.4-001, CR-D-09.2-001… |
| PR (PROTECT) | 19 controls: CR-D-01.1-001, CR-D-01.2-001, CR-D-01.3-001, CR-D-01.4-001, CR-D-02.2-001, CR-D-03.1-001, CR-D-03.2-001, CR-D-03.3-001… |
| DE (DETECT) | 4 controls: CR-D-04.1-001, CR-D-06.4-001, CR-D-10.1-001, CR-D-10.2-001 |
| RS (RESPOND) | 3 controls: CR-D-04.2-001, CR-D-04.3-001, CR-D-10.2-001 |
| RC (RECOVER) | 1 controls: CR-D-04.4-001 |

## Annex B — Framework anchors (ISO 27001 / SSDF)

Rule-level ISO 27001 and SSDF anchors are aggregated in `Doc20_Framework_Mapping_Matrix.md` §1 (columns `ISO 27001`, `SSDF`). This catalog inlines CSF/PF/AIRMF only (F24).

## Annex C — Statutory Source Index

Per-regulation touch count across the 78 controls:

- **GDPR:** 20 controls
- **CRA:** 22 controls
- **NIS 2:** 25 controls
- **DORA:** 27 controls
- **AI Act:** 15 controls


## Annex A — CSF 2.0 Function Index (generated, port Fase 5)

| Function | Controls anchoring at least one subcategory of the function |
|---|---|
| GV (GOVERN) | 7 controls: CR-D-06.1-001, CR-D-06.2-001, CR-D-06.3-001, CR-D-08.3-001, CR-D-09.1-001, CR-D-09.2-001, CR-D-09.4-001 |
| ID (IDENTIFY) | 11 controls: CR-D-02.1-001, CR-D-02.3-001, CR-D-02.4-001, CR-D-05.1-001, CR-D-06.1-001, CR-D-07.1-001, CR-D-07.4-001, CR-D-09.2-001… |
| PR (PROTECT) | 19 controls: CR-D-01.1-001, CR-D-01.2-001, CR-D-01.3-001, CR-D-01.4-001, CR-D-02.2-001, CR-D-03.1-001, CR-D-03.2-001, CR-D-03.3-001… |
| DE (DETECT) | 4 controls: CR-D-04.1-001, CR-D-06.4-001, CR-D-10.1-001, CR-D-10.2-001 |
| RS (RESPOND) | 3 controls: CR-D-04.2-001, CR-D-04.3-001, CR-D-10.2-001 |
| RC (RECOVER) | 1 controls: CR-D-04.4-001 |

## Annex B — Framework anchors (ISO 27001 / SSDF)

Rule-level ISO 27001 and SSDF anchors are aggregated in `Doc20_Framework_Mapping_Matrix.md` §1 (columns `ISO 27001`, `SSDF`). This catalog inlines CSF/PF/AIRMF only (F24).

## Annex C — Statutory Source Index

Per-regulation touch count across the 78 controls:

- **GDPR:** 20 controls
- **CRA:** 22 controls
- **NIS 2:** 25 controls
- **DORA:** 27 controls
- **AI Act:** 15 controls

## 13. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.0 | 2026-08-28 | Executor (port Fase 5) | **Control Set v1.** Catalog tables carry the corrected 24-field schema mapping: maturity columns → Implementation Status (F21/F22, deterministic backfill per posture model §4), Traceability (F23: Legal → AG-D → related goals/CRs) and Framework Anchors (F24 → Doc20 §1) added; Annexes A–C appended; `validation/build_control_set.py` generates control_set.yaml (78 controls; Case_01 `'**'` status-parsing bug fixed and asserted). |

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.0 | 2026-08-28 | Executor (port Fase 5) | **Control Set v1.** Catalog tables carry the corrected 24-field schema mapping: maturity columns → Implementation Status (F21/F22, deterministic backfill per posture model §4), Traceability (F23: Legal → AG-D → related goals/CRs) and Framework Anchors (F24 → Doc20 §1) added; Annexes A–C appended; `validation/build_control_set.py` generates control_set.yaml (78 controls; Case_01 `'**'` status-parsing bug fixed and asserted). |

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.1 | 2026-04-16 | Compliance Lead | Added Activation Condition column to D-04, D-05, D-07, D-09, D-10 tables. CONTEXTUAL conditions for CR-D-04.3-001 (TENSION-H-001), CR-D-05.3-001 (TENSION-H-002). STRUCTURAL conditions with tension notes for CR-D-07.1-001 (TENSION-L-001), CR-D-09.2-001, CR-D-10.2-001. All remaining domains (D-01, D-02, D-03, D-06, D-08) marked as all-structural. |
| 1.0 | 2026-04-03 | Compliance Lead | Initial creation — Phase 2, Step E. 38 compliance rules + 25 best practice rules = 63 total rules for Case 03 OmniBank. All 38 sub-domains covered. 4 strategic tensions resolved. |

---

## 14. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Compliance Lead** |
| **CISO** |
| **DPO** |
| **CTO** |
| **Methodology Owner** |
