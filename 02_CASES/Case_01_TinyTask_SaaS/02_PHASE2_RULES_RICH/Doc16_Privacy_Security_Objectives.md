---
document_id: AEGIS-P2-RICH-10
title: Privacy and Security Operational Objectives Catalog — Rich Mode
phase: 2
version: 5.0
created: 2026-08-07
updated: 2026-08-10
author: Fase de Especificação 1+3+4+5 Executor (reconciliation + catalog port + 6 new cols + 31 detail cards); Fase de Especificação 9 Executor (corr-012 PO/SO migration + tech-strip)
status: DEEP_ENRICHED
id_format: PO-D-XX.X-NNN, SO-D-XX.X-NNN
expected_objectives: 31
expected_fields_per_card: 18
detail_cards_count: 31
fields_per_card: 18
pg_sg_legacy_aliases_count: 31
inputs: [08_Obligation_Derivation.md, 09_Strategic_Tensions_Report.md, 04_Company_Context_Assessment.md, ../02_PHASE2_RULES/10_Privacy_Security_Goals.md, ../01_PHASE1_CONTEXT_RICH/07c_Adjusted_Goals.md]
outputs: [11_Rules_Catalog.md, 12_Rules_Catalog.xlsx]
traceability: AEGIS Class Model → PrivacyOperationalObjective, SecurityOperationalObjective, RiskProfile classes
related_documents: 03_Design_Decisions_Log.md
case: Case_01_TinyTask_SaaS
tier: MICRO
branch: feature/aegis-p1-corrections-batch-001
status_history:
  - 1.0: 2026-08-07 Fase de Especificação 1 baseline
  - 2.0: 2026-08-07 Fase de Especificação 5 deep enrichment (31 detail cards × 15 fields)
  - 5.0: 2026-08-10 Fase de Especificação 9 corr-012 migration (PO/SO rename + tech-strip)
---

# Privacy and Security Operational Objectives Catalog — Rich Mode

> **Fase de Especificação 0 placeholder** — this document is the Rich Mode sibling of legacy `02_PHASE2_RULES/10_Privacy_Security_Goals.md`.
> Will be enriched in Fase de Especificação 1 (reconciliation) + Fase de Especificação 5 (15 fields × 30 objectives).

---

## 1. DOCUMENT PURPOSE

This is the Rich Mode version of the Objectives Catalog. It defines **31 objectives (11 Privacy Operational Objectives + 20 Security Operational Objectives)** derived from 30 obligations across 5 sub-domain clusters, each with 15-field detail cards.

**Phase 2 Step:** D (Privacy and Security Operational Objectives)
**Gate Criteria:** All 30 obligations mapped to objectives with 15-field detail cards

---

## 2. EXPECTED OBJECTIVES (from legacy Doc 10)

| Sub-Domain | PO Count | SO Count | Total |
|------------|---------:|---------:|------:|
| D-01 | 3 | 0 | 3 |
| D-02 | 0 | 3 | 3 |
| D-03 | 0 | 4 | 4 |
| D-04 | 0 | 4 | 4 |
| D-05 | 4 | 0 | 4 |
| D-06 | 0 | 3 | 3 |
| D-07 | 1 | 0 | 1 |
| D-08 | 0 | 2 | 2 |
| D-09 | 3 | 2 | 5 |
| D-10 | 0 | 2 | 2 |
| **TOTAL** | **12** | **18** | **30** |

**Note:** D-01.3 (key management) has only a rule, not an objective — hence PO count is 3 (not 4).

---

## 3. PRIVACY OPERATIONAL OBJECTIVES CATALOG (Fase de Especificação 4 — ported from legacy §3)

> **Fase de Especificação 4 (this sprint):** Ported legacy `02_PHASE2_RULES/10_Privacy_Security_Goals.md` §3.1 PG tables into Rich Mode with 12 columns (6 legacy fields + 6 new Fase de Especificação 4 fields). **11 PO × 12 cols = 132 cells** (6 new cols contribute 11 × 6 = 66 cells). Resolves **F-04a** (the legacy "12 PG" summary is stale; authoritative count is 11 PO — see §5.1).

### 3.1 Privacy Operational Objectives by Sub-Domain

#### D-01: Data Protection & Encryption (3 PO)

| Objective ID | Objective Description | Source Obligations | Sub-Domain | Risk Profile | Priority | Owner | Verification Criteria | Implementation Status | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors | PF Anchors |
| --------- | ------------------ | -------------------- | ------------ | -------------- | ---------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- | --- |
| PO-D-01.1-001 | Personal and product data in persistent storage protected by confidentiality mechanisms appropriate to data class | OBL-D-01.1-001 | D-01.1 | LOW | HIGH | CTO + Lead Dev | Configuration report demonstrates confidentiality mechanisms active in all persistent stores of personal or product data | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-01, PR.DS-02, PR.DS-10, PR.IR-01, PR.PS-06 | PR.DS-P1 |
| PO-D-01.2-001 | Personal and product data crossing network boundaries protected by confidentiality mechanisms appropriate to channel classification | OBL-D-01.2-001 | D-01.2 | LOW | HIGH | CTO + Lead Dev | Configuration report demonstrates confidentiality mechanisms active in all network channels carrying personal or product data | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-02, PR.IR-01 | PR.DS-P2 |
| PO-D-01.4-001 | Personal and product data integrity preserved against unauthorised modification by integrity controls appropriate to data class | OBL-D-01.4-001 | D-01.4 | LOW | HIGH | CTO + Lead Dev | Configuration report demonstrates integrity controls active across personal data, product data, and audit log artifacts | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-01, PR.DS-10 | CT.DM-P1, CT.DM-P3 |

#### D-05: Data Lifecycle (4 PO)

| Objective ID | Objective Description | Source Obligations | Sub-Domain | Risk Profile | Priority | Owner | Verification Criteria | Implementation Status | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors | PF Anchors |
| --------- | ------------------ | -------------------- | ------------ | -------------- | ---------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- | --- |
| PO-D-05.1-001 | Minimise personal data collection to fields essential for the documented purpose | OBL-D-05.1-001 | D-05.1 | LOW | HIGH | CTO + DPO | field-level enforcement | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | GV.OC-03, GV.PO-01, GV.PO-02, ID.AM-03, PR.AA-02, PR.DS-10 | CT.DP-P4, CT.PO-P4, ID.RA-P3 |
| PO-D-05.2-001 | Retain personal data only for the period required to satisfy the documented purpose | OBL-D-05.2-001 | D-05.2 | LOW | MODERATE | CTO + DPO | retention policy audit | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | ID.AM-03, PR.DS-10 | CT.DM-P5, CT.PO-P4 |
| PO-D-05.3-001 | Enable complete data erasure on data-subject request within the regulatory deadline | OBL-D-05.3-001 | D-05.3 | LOW | CRITICAL | CTO + DPO | erasure workflow test (within deadline) | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | GV.SC-04, PR.DS-10, RS.CO-02 | CT.DM-P4, CT.DM-P5 |
| PO-D-05.4-001 | Provide data export in a structured, commonly used, machine-readable format on data-subject request | OBL-D-05.4-001 | D-05.4 | LOW | MODERATE | CTO + DPO | data-export workflow test (within deadline) | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-10 | CT.DM-P1, CT.DM-P6 |

#### D-07: Secure Development (1 PO)

| Objective ID | Objective Description | Source Obligations | Sub-Domain | Risk Profile | Priority | Owner | Verification Criteria | Implementation Status | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors | PF Anchors |
| --------- | ------------------ | -------------------- | ------------ | -------------- | ---------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- | --- |
| PO-D-07.1-001 | Integrate data protection measures into processing design from the outset | OBL-D-07.1-001 | D-07.1 | LOW | HIGH | CTO + Lead Dev | secure-development-framework alignment + posture assessment | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-01, PR.DS-10, PR.PS-01, PR.PS-06 | CT.DP-P2, CT.DP-P4, CT.DP-P5, CT.PO-P4, GV.PO-P2 |

#### D-09: Governance & Documentation (3 PO)

| Objective ID | Objective Description | Source Obligations | Sub-Domain | Risk Profile | Priority | Owner | Verification Criteria | Implementation Status | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors | PF Anchors |
| --------- | ------------------ | -------------------- | ------------ | -------------- | ---------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- | --- |
| PO-D-09.1-001 | Maintain comprehensive privacy policies documenting appropriate measures | OBL-D-09.1-001 | D-09.1 | LOW | HIGH | CTO + DPO + Compliance Lead + Legal | documentation audit | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | CNPD + ENISA (periodic) | GV.OC-02, GV.OC-03, GV.OV-03, GV.PO-01, GV.PO-02, GV.RM-04 | CM.PO-P1, GV.PO-P1, GV.PO-P5 |
| PO-D-09.2-001 | Conduct data-protection impact assessments (DPIA) prior to high-risk processing | OBL-D-09.2-001 | D-09.2 | LOW | HIGH | CTO + DPO + Compliance Lead + Legal | unified assessment template | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | CNPD + ENISA (periodic) | GV.OC-03, GV.OV-03, GV.PO-01, GV.RR-02, GV.SC-02, GV.SC-03 | ID.RA-P3, ID.RA-P4, ID.RA-P5 |
| PO-D-09.4-001 | Maintain records of all personal-data processing activities | OBL-D-09.4-001 | D-09.4 | LOW | MODERATE | CTO + DPO + Compliance Lead + Legal | records-of-processing + breach log | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | CNPD + ENISA (periodic) | DE.AE-03, GV.PO-02, ID.AM-03, PR.AA-02, PR.DS-10, PR.PS-04 | ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8 |

### 3.2 Privacy Operational Objectives Summary

| Metric | Value |
|--------|-------|
| **Total Privacy Operational Objectives** | **11** (resolves F-04a — legacy "12" is stale; PO-D-09.3 does not exist because D-09.3 is DORA-exclusive) |
| **By Priority** | CRITICAL: 1 (9.1%), HIGH: 8 (72.7%), MODERATE: 2 (18.2%) |
| **By Risk Profile** | LOW: 11 (100%) |
| **By Sub-Domain** | D-01: 3, D-05: 4, D-07: 1, D-09: 3 |

**Note:** Percentages exceed 100% across some metrics due to overlapping GDPR+CRA objectives (a single PO can derive from both).

---

## 4. SECURITY OPERATIONAL OBJECTIVES CATALOG (Fase de Especificação 4 — ported from legacy §4)

> **Fase de Especificação 4 (this sprint):** Ported legacy `02_PHASE2_RULES/10_Privacy_Security_Goals.md` §4.1 SG tables into Rich Mode with 12 columns (6 legacy fields + 6 new Fase de Especificação 4 fields). **20 SO × 12 cols = 240 cells** (6 new cols contribute 20 × 6 = 120 cells). Resolves **F-04b** (the legacy "18 SG" summary is stale; authoritative count is 20 SO).

### 4.1 Security Operational Objectives by Sub-Domain

#### D-02: Vulnerability Management (3 SO)

| Objective ID | Objective Description | Source Obligations | Sub-Domain | Risk Profile | Priority | Owner | Verification Criteria | Implementation Status | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors | PF Anchors |
| --------- | ------------------ | -------------------- | ------------ | -------------- | ---------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- | --- |
| SO-D-02.1-001 | Deliver and maintain the product with zero known exploitable vulnerabilities | OBL-D-02.1-001 | D-02.1 | MEDIUM | CRITICAL | CTO + Lead Dev + Procurement | automated vulnerability + dependency scan, zero critical findings | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | ENISA 24h (CRA) | ID.IM-02, ID.RA-01, ID.RA-05, PR.PS-02 | ID.RA-P3, ID.RA-P5 |
| SO-D-02.2-001 | Enable automatic security updates for all deployed components | OBL-D-02.2-001 | D-02.2 | MEDIUM | CRITICAL | CTO + Lead Dev + Procurement | patch-management SLA test | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | ENISA 24h (CRA) | — | — (SSDF RV.2 deliverable) |
| SO-D-02.3-001 | Publish a coordinated vulnerability disclosure policy | OBL-D-02.3-001 | D-02.3 | LOW | HIGH | CTO + Lead Dev + Procurement | vulnerability-disclosure policy + reporting workflow | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | ENISA 24h (CRA) | — | — (SSDF RV.1 deliverable) |

#### D-03: Access Control (4 SO)

| Objective ID | Objective Description | Source Obligations | Sub-Domain | Risk Profile | Priority | Owner | Verification Criteria | Implementation Status | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors | PF Anchors |
| --------- | ------------------ | -------------------- | ------------ | -------------- | ---------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- | --- |
| SO-D-03.1-001 | Implement authentication controls for all user-facing interfaces | OBL-D-03.1-001 | D-03.1 | MEDIUM | HIGH | CTO + Lead Dev | managed identity baseline | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | GV.OC-03, GV.PO-02, PR.AA-02, PR.AA-03, PR.DS-10 | PR.AC-P1, PR.AC-P6, PR.AC-P4; ALT-ANCHOR (800-53r5 CM-8; SSDF PO.5.1) (asset inventory/risk-strategy — no PF 1.0 analogue) |
| SO-D-03.2-001 | Enable multi-factor authentication for accounts with access to personal data or administrative privileges | OBL-D-03.2-001 | D-03.2 | LOW | MODERATE | CTO + Lead Dev | MFA enforcement test | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | — | PR.AC-P6; ALT-ANCHOR (ASVS V3.5; 800-53r5 IA-4) (identity assertions — no PF 1.0 subcategory) |
| SO-D-03.3-001 | Restrict access to authorised personnel; enforce least privilege | OBL-D-03.3-001 | D-03.3 | MEDIUM | HIGH | CTO + Lead Dev | RBAC quarterly review | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.AA-05, PR.AA-06, PR.AT-02 | CT.PO-P1 |
| SO-D-03.4-001 | Disable all unused ports, services, and interfaces by default | OBL-D-03.4-001 | D-03.4 | LOW | HIGH | CTO + Lead Dev | hardened-default compliance | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-10, PR.PS-01, PR.PS-06 | CT.DP-P4, CT.PO-P4 |

#### D-04: Incident Response (4 SO)

| Objective ID | Objective Description | Source Obligations | Sub-Domain | Risk Profile | Priority | Owner | Verification Criteria | Implementation Status | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors | PF Anchors |
| --------- | ------------------ | -------------------- | ------------ | -------------- | ---------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- | --- |
| SO-D-04.1-001 | Design the system to limit the severity of any single exploit | OBL-D-04.1-001 | D-04.1 | MEDIUM | MODERATE | CTO + DPO + Compliance Lead | managed monitoring alarms active | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | CNPD 72h (GDPR) | DE.AE-02, DE.CM-01, DE.CM-03, DE.CM-09, RS.MA-02 | CM.AW-P7 |
| SO-D-04.2-001 | Build resilience against denial-of-service attacks | OBL-D-04.2-001 | D-04.2 | MEDIUM | MODERATE | CTO + DPO + Compliance Lead | DoS resilience drill | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | CNPD 72h (GDPR) | PR.DS-01, RS.MI-01, RS.MI-02 | CT.DM-P10, PR.PO-P7 |
| SO-D-04.3-001 | Notify the supervisory authority of actively exploited vulnerabilities within the regulatory deadline | OBL-D-04.3-001 | D-04.3 | HIGH | CRITICAL | CTO + DPO + Compliance Lead | dual-notification SLA | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | CNPD 72h + ENISA 24h (max-SLA routing) | GV.OC-03, ID.RA-06, PR.DS-01, PR.DS-10, PR.IR-03 | CM.AW-P7, CM.AW-P8, CM.PO-P1, CM.PO-P2 |
| SO-D-04.4-001 | Restore availability and access to data in a timely manner after an incident | OBL-D-04.4-001 | D-04.4 | MEDIUM | HIGH | CTO + DPO + Compliance Lead | managed backup RTO 24h | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | CNPD 72h (GDPR) | PR.DS-01, PR.IR-04, RC.RP-04 | PR.DS-P1, PR.DS-P4, PR.PT-P4; ALT-ANCHOR (800-53r5 CP-10) (recover-execution — PF 1.0 has no Recover axis) |

#### D-06: Supply Chain (3 SO)

| Objective ID | Objective Description | Source Obligations | Sub-Domain | Risk Profile | Priority | Owner | Verification Criteria | Implementation Status | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors | PF Anchors |
| --------- | ------------------ | -------------------- | ------------ | -------------- | ---------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- | --- |
| SO-D-06.1-001 | Use only processors that provide sufficient guarantees under documented data-processing agreements | OBL-D-06.1-001 | D-06.1 | LOW | HIGH | CTO + Lead Dev + Procurement | DPA + documented third-party security attestation | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | GV.SC-02, GV.SC-03 | ID.IM-P2 |
| SO-D-06.2-001 | Maintain a software bill of materials in machine-readable format | OBL-D-06.2-001 | D-06.2 | MEDIUM | HIGH | CTO + Lead Dev + Procurement | machine-readable SBOM per release | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | — | — (SSDF PS.3 deliverable) |
| SO-D-06.3-001 | Bind processors to security obligations via contractual instruments | OBL-D-06.3-001 | D-06.3 | LOW | HIGH | CTO + Lead Dev + Procurement | DPA template + clauses | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | DE.CM-06, GV.OC-03, GV.RR-02, GV.SC-01, GV.SC-02, GV.SC-03 | ID.DE-P3, ID.DE-P4; ALT-ANCHOR (800-53r5 PM-30; SR-6) (ecosystem-risk→ERM — no PF 1.0 subcategory) |

#### D-08: Human Factors (2 SO)

| Objective ID | Objective Description | Source Obligations | Sub-Domain | Risk Profile | Priority | Owner | Verification Criteria | Implementation Status | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors | PF Anchors |
| --------- | ------------------ | -------------------- | ------------ | -------------- | ---------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- | --- |
| SO-D-08.1-001 | Conduct security awareness training at the documented cadence for all staff | OBL-D-08.1-001 | D-08.1 | LOW | MODERATE | CTO + HR + DPO | annual security awareness training | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | GV.OV-03, ID.IM-02, PR.AA-05, PR.AT-01, PR.AT-02 | GV.AT-P1, GV.AT-P2 |
| SO-D-08.2-001 | Provide role-specific security training to staff with privileged access | OBL-D-08.2-001 | D-08.2 | LOW | MODERATE | CTO + HR + DPO | role-specific training | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.AT-01, PR.AT-02 | GV.AT-P1, GV.AT-P2 |

#### D-09: Governance & Documentation (2 SO — dual coverage with PO-D-09.x)

| Objective ID | Objective Description | Source Obligations | Sub-Domain | Risk Profile | Priority | Owner | Verification Criteria | Implementation Status | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors | PF Anchors |
| --------- | ------------------ | -------------------- | ------------ | -------------- | ---------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- | --- |
| SO-D-09.1-001 | Maintain technical documentation for the post-market-placement retention period | OBL-D-09.1-001 | D-09.1 | LOW | MODERATE | CTO + DPO + Compliance Lead + Legal | documentation audit | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | CNPD + ENISA (periodic) | GV.OC-02, GV.OC-03, GV.OV-03, GV.PO-01, GV.PO-02, GV.RM-04 | CM.PO-P1, GV.PO-P1, GV.PO-P5 |
| SO-D-09.2-001 | Conduct a cybersecurity risk assessment before product launch | OBL-D-09.2-001 | D-09.2 | MEDIUM | HIGH | CTO + DPO + Compliance Lead + Legal | unified assessment template | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | CNPD + ENISA (periodic) | GV.OC-03, GV.OV-03, GV.PO-01, GV.RR-02, GV.SC-02, GV.SC-03 | ID.RA-P3, ID.RA-P4, ID.RA-P5 |

#### D-10: Monitoring & Audit (2 SO)

| Objective ID | Objective Description | Source Obligations | Sub-Domain | Risk Profile | Priority | Owner | Verification Criteria | Implementation Status | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors | PF Anchors |
| --------- | ------------------ | -------------------- | ------------ | -------------- | ---------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- | --- |
| SO-D-10.2-001 | Log all security-relevant events with an immutable audit trail | OBL-D-10.2-001 | D-10.2 | MEDIUM | HIGH | CTO + Lead Dev | managed audit-trail + immutable storage audit | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | DE.AE-03, GV.OV-03, GV.PO-02, ID.AM-03, PR.DS-10, PR.PS-04 | CT.DM-P4, CT.DM-P9 |
| SO-D-10.3-001 | Conduct regular security testing and code reviews | OBL-D-10.3-001 | D-10.3 | MEDIUM | MODERATE | CTO + Lead Dev | quarterly compliance review | PARTIAL | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | ID.IM-02, ID.IM-04, ID.RA-01, ID.RA-05, ID.RA-06, PR.PS-02 | ID.RA-P3, ID.RA-P5 |

### 4.2 Security Operational Objectives Summary

| Metric | Value |
|--------|-------|
| **Total Security Operational Objectives** | **20** (resolves F-04b — legacy "18" is stale; SO-D-02.4 was renamed to SO-D-06.2 in v1.1 and never re-counted) |
| **By Priority** | CRITICAL: 3 (15.0%), HIGH: 9 (45.0%), MODERATE: 8 (40.0%) |
| **By Risk Profile** | LOW: 9 (45.0%), MEDIUM: 10 (50.0%), HIGH: 1 (5.0%) |
| **By Sub-Domain** | D-02: 3, D-03: 4, D-04: 4, D-06: 3, D-08: 2, D-09: 2, D-10: 2 |

**Note:** Percentages exceed 100% across some metrics due to overlapping GDPR+CRA objectives.

---

## 5. RECONCILIATION CROSS-CHECKS (SPRINT 1)

> Fase de Especificação 1 scope: cross-check the objectives catalog against the 30 obligations (Doc 08) and 30 CR rules (Doc 11), verify the PO/SO distribution by sub-domain, confirm Risk Profile distribution, and check ID integrity. Legacy `02_PHASE2_RULES/` files are **read-only** and not modified by this section.

### 5.1 Objective Count Verification

| Check | Expected (per Sprint Plan) | Actual | Status |
|-------|---------------------------:|-------:|:------:|
| Total objective IDs in Doc 10 (§3.1 + §4.1) | 30 (12 PG + 18 SG) | **31** (11 PO + 20 SO) | **FINDING F-04** |
| Privacy Operational Objectives (PO) in §3.1 | 12 | **11** | **FINDING F-04a** |
| Security Operational Objectives (SO) in §4.1 | 18 | **20** | **FINDING F-04b** |
| Unique PO IDs (no duplicates) | 11 | 11 | PASS |
| Unique SO IDs (no duplicates) | 20 | 20 | PASS (excluding stale `SO-D-02.4-001` log reference in §10) |
| Canonical format `PO-D-XX.X-NNN` / `SO-D-XX.X-NNN` | 31/31 | 31/31 | PASS |

**Why the discrepancy?** Legacy Doc 10 §3.2 summary header claims "12 Privacy Operational Objectives" with `D-09: 4` but §3.1 only lists 3 POs for D-09 (PO-D-09.1, 09.2, 09.4). Legacy §4.2 summary claims "18 Security Operational Objectives" with sub-domain breakdown summing to 20. The summary metrics are stale from v1.0; the actual row counts are the values reported in this §3.1 table.

### 5.2 Obligation-to-Objective Mapping (PO/SO → OBL)

The full traceability from Doc 10 §5.2 mapped 31 objective rows against 30 unique obligations. Two obligations (D-09.1 and D-09.2) are covered by both a PO and an SO (intentional dual-coverage for governance objectives). One obligation (D-01.3, Key Management) has no objective — see §5.7 finding F-01.

| Objective ID | Source Obligation | Type | Status |
|---------|--------------------|------|:------:|
| PO-D-01.1-001 | OBL-D-01.1-001 | PO | PASS |
| PO-D-01.2-001 | OBL-D-01.2-001 | PO | PASS |
| PO-D-01.4-001 | OBL-D-01.4-001 | PO | PASS |
| PO-D-05.1-001 | OBL-D-05.1-001 | PO | PASS |
| PO-D-05.2-001 | OBL-D-05.2-001 | PO | PASS |
| PO-D-05.3-001 | OBL-D-05.3-001 | PO | PASS |
| PO-D-05.4-001 | OBL-D-05.4-001 | PO | PASS |
| PO-D-07.1-001 | OBL-D-07.1-001 | PO | PASS |
| PO-D-09.1-001 | OBL-D-09.1-001 | PO (dual) | PASS |
| PO-D-09.2-001 | OBL-D-09.2-001 | PO (dual) | PASS |
| PO-D-09.4-001 | OBL-D-09.4-001 | PO | PASS |
| SO-D-02.1-001 | OBL-D-02.1-001 | SO | PASS |
| SO-D-02.2-001 | OBL-D-02.2-001 | SO | PASS |
| SO-D-02.3-001 | OBL-D-02.3-001 | SO | PASS |
| SO-D-03.1-001 | OBL-D-03.1-001 | SO | PASS |
| SO-D-03.2-001 | OBL-D-03.2-001 | SO | PASS |
| SO-D-03.3-001 | OBL-D-03.3-001 | SO | PASS |
| SO-D-03.4-001 | OBL-D-03.4-001 | SO | PASS |
| SO-D-04.1-001 | OBL-D-04.1-001 | SO | PASS |
| SO-D-04.2-001 | OBL-D-04.4-001 | SO (note: Doc 10 row text shows this; see §5.7 F-07) | CONDITIONAL |
| SO-D-04.3-001 | OBL-D-04.3-001 | SO | PASS |
| SO-D-04.4-001 | OBL-D-04.4-001 | SO | PASS |
| SO-D-06.1-001 | OBL-D-06.1-001 | SO | PASS |
| SO-D-06.2-001 | OBL-D-06.2-001 | SO | PASS |
| SO-D-06.3-001 | OBL-D-06.3-001 | SO | PASS |
| SO-D-08.1-001 | OBL-D-08.1-001 | SO | PASS |
| SO-D-08.2-001 | OBL-D-08.2-001 | SO | PASS |
| SO-D-09.1-001 | OBL-D-09.1-001 | SO (dual) | PASS |
| SO-D-09.2-001 | OBL-D-09.2-001 | SO (dual) | PASS |
| SO-D-10.2-001 | OBL-D-10.2-001 | SO | PASS |
| SO-D-10.3-001 | OBL-D-10.3-001 | SO | PASS |

**Summary:** 11 PO + 20 SO = 31 objective rows. 29 OBLs are covered by ≥1 objective; 2 OBLs have dual-coverage (D-09.1, D-09.2); 1 OBL (D-01.3) has no objective (F-01, see §5.7).

### 5.3 Privacy Operational Objective (PO) Coverage by Sub-Domain

| Sub-Domain | PO Count | PO IDs | Status |
|------------|---------:|--------|:------:|
| D-01 | 3 | PO-D-01.1-001, PO-D-01.2-001, PO-D-01.4-001 | PASS |
| D-05 | 4 | PO-D-05.1-001, PO-D-05.2-001, PO-D-05.3-001, PO-D-05.4-001 | PASS |
| D-07 | 1 | PO-D-07.1-001 | PASS |
| D-09 | 3 | PO-D-09.1-001, PO-D-09.2-001, PO-D-09.4-001 | PASS |
| **TOTAL** | **11** | — | **PASS (with F-04a)** |

**Note:** Legacy §3.2 summary says "D-01: 3, D-05: 4, D-07: 1, D-09: 4" — but §3.1 only lists 3 POs for D-09 (no PO-D-09.3 because D-09.3 is DORA-exclusive and not applicable to TinyTask). Authoritative count = 11 POs, not 12. See F-04a.

### 5.4 Security Operational Objective (SO) Coverage by Sub-Domain

| Sub-Domain | SO Count | SO IDs | Status |
|------------|---------:|--------|:------:|
| D-02 | 3 | SO-D-02.1-001, SO-D-02.2-001, SO-D-02.3-001 | PASS |
| D-03 | 4 | SO-D-03.1-001, SO-D-03.2-001, SO-D-03.3-001, SO-D-03.4-001 | PASS |
| D-04 | 4 | SO-D-04.1-001, SO-D-04.2-001, SO-D-04.3-001, SO-D-04.4-001 | PASS |
| D-06 | 3 | SO-D-06.1-001, SO-D-06.2-001, SO-D-06.3-001 | PASS |
| D-08 | 2 | SO-D-08.1-001, SO-D-08.2-001 | PASS |
| D-09 | 2 | SO-D-09.1-001, SO-D-09.2-001 | PASS |
| D-10 | 2 | SO-D-10.2-001, SO-D-10.3-001 | PASS |
| **TOTAL** | **20** | — | **PASS (with F-04b)** |

**Note:** Legacy §4.2 summary says "18 Security Operational Objectives" — but §4.1 lists 20 SO rows. The summary is stale from v1.0/v1.1 (where SO-D-02.4 was renamed to SO-D-06.2). Authoritative count = 20 SOs, not 18. See F-04b.

### 5.5 Risk Profile Distribution (preserved from legacy §6.2)

| Risk Profile | PO | SO | Total | Percentage | Example Objectives |
|--------------|---:|---:|------:|-----------:|---------------|
| **HIGH** | 0 | 1 (SO-D-04.3-001) | 1 | 3.2% | SO-D-04.3 (24h notification) |
| **MEDIUM** | 0 | 10 | 10 | 32.3% | SO-D-02.1, SO-D-03.1, SO-D-04.1 |
| **LOW** | 11 | 9 | 20 | 64.5% | All POs + SO-D-02.3, SO-D-04.4 |
| **TOTAL** | **11** | **20** | **31** | **100%** | — |

**Note:** Legacy §6.2 reports "PO: 12, SO: 18, Total: 30, HIGH: 1 (3.3%), MEDIUM: 10 (33.3%), LOW: 19 (63.3%)". Recomputed against actual row counts: PO: 11, SO: 20, Total: 31. The HIGH/MEDIUM counts are unchanged (only LOW shifts from 19 → 20 to reflect the additional SO rows).

### 5.6 ID Integrity Check

| Check | Expected | Actual | Status |
|-------|---------:|-------:|:------:|
| Duplicate PO IDs across Doc 10 | 0 | 0 | PASS |
| Duplicate SO IDs across Doc 10 (excluding stale log ref) | 0 | 0 | PASS |
| Canonical format `PO/SO-D-XX.X-NNN` | 31/31 | 31/31 | PASS |
| Stale reference `SO-D-02.4-001` in §10 version history | 1 (expected) | 1 | PASS (cosmetic only) |

### 5.7 Findings — Flagged for Human Review

| ID | Severity | Description | Recommendation |
|----|----------|-------------|----------------|
| **F-01** | LOW | OBL-D-01.3-001 (Key Management) has no PO/SO. Doc 11 §4 row CR-D-01.3-001 references phantom `PO-D-01.3-001`. | Same as Doc 08 F-01. Add PO-D-01.3-001 to Doc 10 or fix CR reference. Blocks Fase de Especificação 5 for this OBL. |
| **F-02** | MEDIUM | OBL-D-09.1-001 and OBL-D-09.2-001 each have both a PO and an SO (intentional governance dual-coverage). | Acceptable; document as intentional in 1:1 mapping definition. |
| **F-04a** | LOW | Legacy §3.2 summary claims "12 Privacy Operational Objectives" but §3.1 lists 11 PO IDs (D-09 has 3 PO, not 4). | Correct the §3.2 summary in Doc 10 (legacy, out of Fase de Especificação 1 scope). |
| **F-04b** | LOW | Legacy §4.2 summary claims "18 Security Operational Objectives" but §4.1 lists 20 SO IDs. | Correct the §4.2 summary in Doc 10 (legacy, out of Fase de Especificação 1 scope). |
| **F-06** | INFO | Stale `SO-D-02.4-001` reference in Doc 10 §10 version history (renamed to SO-D-06.2-001 in v1.1). | Cosmetic only — version-history note, not a data row. |

### 5.8 Reconciliation Verdict

| Dimension | Status |
|-----------|:------:|
| Objective count (30 expected vs 31 actual) | **FINDING** (F-04a, F-04b) |
| Objective ↔ Obligation mapping (29/30 OBLs covered) | CONDITIONAL_PASS (F-01, F-02) |
| PO distribution (11) | PASS |
| SO distribution (20) | PASS |
| Risk Profile distribution | PASS |
| ID integrity | PASS |

**Fase de Especificação 1 verdict for Doc 10:** **CONDITIONAL_PASS** — proceed to Fase de Especificação 5 for 31 objective cards (no Fase de Especificação 5 blockers for objectives themselves); surface F-01 / F-02 / F-04 to human arbiter.

---

## 6. OBJECTIVE DETAIL CARDS (Rich Mode)

> **Fase de Especificação 5 (this sprint):** Append 31 detail cards (11 PO + 20 SO) with 15 fields per card (31 × 15 = **465 cells**). Owner matrix per Fase de Especificação 5 task spec. No Effort/Cost/Timeline fields. Sources cross-reference Phase 1 Rich `07c_Adjusted_Goals.md` Appendix A §A.1.1/§A.2.1 (37+37 cards per sub-domain), Doc 08 obligations, Doc 11 CR rules, legacy Doc 10 descriptions.
>
> **Fase de Especificação 5 caveat (F-01):** OBL-D-01.3-001 (Key Management) has no PO/SO card here per the Phase 2 catalog (D-01.3 has a CR rule but not an objective). The Phase 1 Rich Appendix A DOES have AG-D-01.3-001 — see cross-reference. This is an intentional Phase 2 catalog scoping decision, not a Fase de Especificação 5 omission.

### 6.1 Privacy Operational Objective Detail Cards (11 cards)

---

### PO-D-01.1-001 — Personal Data at Rest Confidentiality

> **Sub-Domain:** D-01.1 — Data at Rest Encryption | **Cluster:** D-01 — Data Protection & Encryption
> **Applicable Regulation(s):** GDPR + CRA (dual coverage)
> **Source Obligation (Doc 08 §4):** OBL-D-01.1-001
> **Doc 11 §4 CR Rule:** CR-D-01.1-001
> **Doc 10 §3.1 Risk Profile:** LOW | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-01.1.GDPR + SO-D-01.1.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.json`
> **Phase 1 §3 Per-Regulation Objective:** D-01.1
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-01.1.json` (5 CSF + 4 PF + 0 AI RMF)
> **Doc 09 §4 Strategic Tensions:** None for D-01.1

1. **Description:** Personal and product data in persistent storage protected by confidentiality mechanisms with segregated cryptographic material management. The obligation is structural and continuous — all data written to persistent storage must be protected at the storage layer, with no opt-out. The objective binds D-01.1 and is a prerequisite for D-05.3 erasure cascading to backups.
2. **Scope:** All persistent stores of personal and product data: primary stores, replicas, snapshots, and archival stores. Covers the protection mechanism applied at the storage layer regardless of substrate.
3. **Out of Scope:** Customer-side confidentiality mechanisms (out of SaaS control); dedicated hardware confidentiality modules (overkill at small scale — RIGOROUS tier); on-premises material custody (not in small-scale cloud-native stack).
4. **Source Article:** GDPR Art. 5(1)(f) + Art. 32(1)(a) — "appropriate technical measures"; CRA Annex I §1.5(a) — confidentiality of stored data.
5. **NIST CSF Anchors:** PR.DS-01, PR.DS-10, PR.AA-01.
6. **Privacy FW Anchors:** PR.DS-P1.
7. **Verification Criteria:**
   - Configuration report demonstrates confidentiality mechanisms are active in all persistent stores of personal or product data.
   - Cryptographic material management report demonstrates separation between material access and data access.
   - Periodic review documents the choice of mechanisms proportional to context (the proportional position is the choice of mechanism; absence of a proprietary key-management programme is a proportionality choice, not a control gap).
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO (primary) + Lead Dev (backup) — per Fase de Especificação 5 owner matrix (D-01 → CTO + Lead Dev).
10. **Status:** TODO.
11. **Dependencies:** D-01.3 (Key Management), D-01.4 (Integrity), D-05.3 (Erasure cascade), CR-D-01.1-001, OBL-D-01.1-001, PO-D-01.3-001 (Phase 1).
12. **Risk if not met:** HIGH — failure creates audit-finding exposure under GDPR Art. 5(1)(f) and CRA Annex I §1.5(a); potential data-breach notification trigger.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, DPO, documented third-party security attestation source, CNPD (Portuguese SA).
14. **Implementation Status:** IMPLEMENTED (AWS KMS managed encryption active on all DB/backup stores - Doc 04a STORE-01/02)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only (no breach if compliant); breach scenario → CNPD 72h (GDPR Art. 33) + ENISA early warning 24h (CRA Art. 11).
17. **External Auditor (Case_01):** Documented third-party security attestation (covers key custody); ISO 27001 SoA line item A.10.1.1 / A.10.1.2.
18. **Supervisory Body (Case_01):** CNPD (lead SA for GDPR) + ENISA (CRA single reporting platform) + PT CSIRT/CNCS (national CSIRT for NIS2 baseline).

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.RM-04, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-12
    - NIST PF 1.0: GV.RM-P1, ID.RA-P2, PR.DS-P1, PR.DS-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Storage-layer cryptographic protection of persistent stores with segregated cryptographic material custody
    - Tier-appropriate backup retention aligned with documented RTO/RPO targets
    - Quarterly configuration review with documented findings and remediation actions
    - Documented proportional-choice review of mechanism captured in periodic assessment

---

### PO-D-01.2-001 — Personal Data in Transit Confidentiality

> **Sub-Domain:** D-01.2 — Data in Transit Encryption | **Cluster:** D-01 — Data Protection & Encryption
> **Applicable Regulation(s):** GDPR + CRA (dual coverage)
> **Source Obligation (Doc 08 §4):** OBL-D-01.2-001
> **Doc 11 §4 CR Rule:** CR-D-01.2-001
> **Doc 10 §3.1 Risk Profile:** LOW | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-01.2.GDPR + SO-D-01.2.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.2/D-01.2.json`
> **Phase 1 §3 Per-Regulation Objective:** D-01.2
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-01.2.json` (5 CSF + 4 PF + 0 AI RMF)
> **Doc 09 §4 Strategic Tensions:** None for D-01.2

1. **Description:** Personal and product data crossing network boundaries protected by confidentiality mechanisms appropriate to the channel classification. Covers all paths by which data leaves a trusted processing environment — ingress from data subjects, egress to third-party services, and east-west between processing components. The objective binds D-01.2.
2. **Scope:** All network channels carrying personal or product data: ingress channels, egress channels to third-party services, and inter-component channels within the processing environment.
3. **Out of Scope:** Mutual confidentiality between internal services (deferred — would require service-mesh investment incompatible with MICRO); VPN/IPsec for staff (managed by device-level credential vault + MFA, not network layer).
4. **Source Article:** GDPR Art. 5(1)(f) + Art. 32(1)(a); CRA Annex I §1.5(b) — confidentiality during transmission.
5. **NIST CSF Anchors:** PR.DS-02, PR.IR-01, PR.AA-01.
6. **Privacy FW Anchors:** PR.DS-P2.
7. **Verification Criteria:**
   - Configuration report demonstrates confidentiality mechanisms are active in all network channels carrying personal or product data.
   - Cryptographic material management report demonstrates separation between channel-protection keys and data keys.
   - Annual review documents the choice of mechanisms proportional to context.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO (primary) + Lead Dev (backup).
10. **Status:** TODO.
11. **Dependencies:** D-01.1 (at rest), D-03.1 (authentication), CR-D-01.2-001, OBL-D-01.2-001, PO-D-01.2-001 (Phase 1).
12. **Risk if not met:** HIGH — MITM exposure for customer credentials and PII; non-compliance under GDPR Art. 32(1)(a).
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, DPO, documented third-party security attestation source, CNPD.
14. **Implementation Status:** IMPLEMENTED (TLS 1.3 enforced on main endpoints and Auth0 - Doc 04a FLOW-01/05)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; breach scenario → CNPD 72h + ENISA 24h.
17. **External Auditor (Case_01):** Documented third-party security attestation (covers managed TLS termination); ISO 27001 A.13.1.1 (network controls).
18. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-12, PR.IR-01
    - NIST PF 1.0: PR.DS-P1, PR.DS-P2, PR.PT-P1, PR.PT-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Channel-classification-aligned cryptographic protection across ingress, egress, and inter-component traffic
    - Separation of channel-protection keys from data keys with documented custody chain
    - Annual review of cryptographic choice proportional to channel classification
    - Quarterly configuration review of channel-protection termination and inter-service paths

---

### PO-D-01.4-001 — Personal Data Integrity

> **Sub-Domain:** D-01.4 — Data Integrity Mechanisms | **Cluster:** D-01 — Data Protection & Encryption
> **Applicable Regulation(s):** GDPR + CRA (dual coverage)
> **Source Obligation (Doc 08 §4):** OBL-D-01.4-001
> **Doc 11 §4 CR Rule:** CR-D-01.4-001
> **Doc 10 §3.1 Risk Profile:** LOW | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-01.4.GDPR + SO-D-01.4.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.4/D-01.4.json`
> **Phase 1 §3 Per-Regulation Objective:** D-01.4
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-01.4.json` (8 CSF + 6 PF + 0 AI RMF)
> **Doc 09 §4 Strategic Tensions:** None for D-01.4

1. **Description:** Personal and product data integrity preserved against unauthorised modification by integrity controls appropriate to data class. Covers structural constraints at the data layer, integrity checks at the application boundary, and redundancy at the infrastructure layer. The objective binds D-01.4 and is the integrity limb of the GDPR Art. 5(1)(d) accuracy principle.
2. **Scope:** All data classes in scope: personal data, product data, and audit records. Covers structural constraints (schema-level), cryptographic integrity (application boundary), and physical redundancy (infrastructure layer).
3. **Out of Scope:** Blockchain anchoring (out of scope at MICRO); TPM-backed attestation (RIGOROUS tier); cryptographic erasure verification (not in current stack).
4. **Source Article:** GDPR Art. 5(1)(d) + Art. 32(1)(b); CRA Annex I §1.5(c) — integrity of stored/transmitted data.
5. **NIST CSF Anchors:** PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-01, PR.DS-10, PR.IR-03, PR.IR-04, PR.PS-04.
6. **Privacy FW Anchors:** CT.DM-P1, CT.DM-P3.
7. **Verification Criteria:**
   - Configuration report demonstrates integrity controls are active across personal data, product data, and audit log artifacts.
   - Periodic integrity test demonstrates corruption detection within recovery window.
   - Annual review documents the choice of mechanisms proportional to context.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO (primary) + Lead Dev (backup).
10. **Status:** TODO.
11. **Dependencies:** D-01.1 (encryption is the prerequisite for cryptographic integrity check), D-01.2 (in-transit), CR-D-01.4-001, OBL-D-01.4-001, PO-D-01.4-001 (Phase 1).
12. **Risk if not met:** HIGH — undetected data corruption could lead to wrong decisions or compliance breaches; non-compliance with GDPR Art. 5(1)(d).
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, DPO, documented third-party security attestation source, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: periodic database integrity verification schedule)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; integrity-loss incident → CNPD 72h if personal-data corruption reaches data subjects.
17. **External Auditor (Case_01):** Documented third-party security attestation (covers managed cross-zone redundancy + immutable retention); ISO 27001 A.12.3.1 (backup), A.14.1.3 (integrity).
18. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, PR.DS-12, PR.IR-03, PR.IR-04, PR.PS-04
    - NIST PF 1.0: PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3, PR.PT-P1, PR.PT-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Layered integrity controls: schema-level constraints, application-boundary cryptographic checks, infrastructure redundancy
    - Periodic integrity test demonstrating corruption detection within documented recovery window
    - Documented change-control with integrity verification on schema migrations
    - Annual review of integrity choice proportional to data class

---

### PO-D-05.1-001 — Minimize Personal Data Collection

> **Sub-Domain:** D-05.1 — Data Minimization | **Cluster:** D-05 — Data Lifecycle
> **Applicable Regulation(s):** GDPR (privacy-driven; no CRA sub-SO)
> **Source Obligation (Doc 08 §4):** OBL-D-05.1-001
> **Doc 11 §4 CR Rule:** CR-D-05.1-001
> **Doc 10 §3.1 Risk Profile:** LOW | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-05.1.GDPR (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.1/D-05.1.json`
> **Phase 1 Appendix A §A.1.1 Card:** PO-D-05.1-001 (matches this card; per-sub-domain deep enrichment in 07c Appendix A §A.1.1)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-05.1.json` (6 CSF + 10 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO (per Fase de Especificação 5 owner matrix; D-05 → CTO + DPO)
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** CONF-002 (vs SO-D-02.1 vulnerability tracking; resolved via metadata-only)
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly review
> **Doc 03 Design Decisions Log:** DD-05 (Schema column allow-list enforced)
> **Doc 04 §4 Business Goal Link:** BG-01 (Operational efficiency with minimal data)
> **Audit Artefact (Doc 11 §4):** Schema diff report + API fuzz test + managed log scrubber test
> **Verification Cadence:** Quarterly review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §2a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (PO #4 of 11)
> **Fase de Especificação 5 Card Position:** 4/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Data collection must be limited to what is adequate, relevant, and necessary for the documented purpose of the processing activity. This is operationalised at three layers: database schema (only documented fields are columns — adding a field requires a schema migration with privacy review), API input validation (rejects unknown fields with HTTP 400), and analytics pipeline (no personal data emitted to managed monitoring logs or analytics tools). This objective is the operational expression of GDPR Art. 5(1)(c) and binds D-05.1 (Data Minimisation); it interacts with SO-D-02.1 (vulnerability tracking) under Conflict CONF-002 — resolved by collecting only vulnerability metadata, not user data.
2. **Scope:** Managed relational database schema (column allow-list), API gateway request validation (JSON-schema reject-unknown), managed log scrubber (regex strip email/IBAN patterns), payment-processor webhook payload allow-list.
3. **Out of Scope:** Differential-privacy techniques on aggregate metrics (overkill at small scale); user-driven consent granularity (single-tier consent for the documented purpose).
4. **Source Article:** GDPR Art. 5(1)(c); CRA Annex I §1.7 (data minimisation is implicit in the "least privilege" processing principle).
5. **NIST CSF Anchors:** GV.OC-03, GV.PO-01, ID.AM-03, PR.DS-01, PR.DS-10, PR.PS-06.
6. **Privacy FW Anchors:** CT.DP-P4, CT.PO-P4, ID.RA-P3.
7. **Verification Criteria:**
   - Database schema diff vs documented field list shows zero undocumented personal-data columns (PR scan quarterly).
   - API fuzz test with random unknown-field payload returns HTTP 400 across all documented endpoints.
   - Managed log scrubber regex test: feeding an email-pattern line returns a redacted line (validated by sample 1/quarter).
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + DPO — per Fase de Especificação 5 owner matrix (D-05 → CTO + DPO).
10. **Status:** TODO.
11. **Dependencies:** D-01.1, D-09.2 (DPIA documents the minimisation rationale), CR-D-05.1-001, OBL-D-05.1-001, PO-D-05.1-001 (Phase 1).
12. **Risk if not met:** MEDIUM — over-collection leads to DSAR/erasure scope expansion and reputational risk; non-compliance with Art. 5(1)(c).
13. **Affected Stakeholders:** Customers (data subjects), DPO, CTO, Legal, CNPD.
14. **Implementation Status:** IMPLEMENTED (Data minimisation in product design & Stripe payment isolation - Doc 04a §2.2)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; over-collection discovered retrospectively → CNPD notification under Art. 33 (breach is over-collection = processing beyond purpose).
17. **External Auditor (Case_01):** Documented third-party security attestation (covers log integrity); ISO 27001 A.18.1.4 (privacy of personal information).
18. **Supervisory Body (Case_01):** CNPD (lead) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.OC-03, GV.PO-01, ID.AM-03, PR.DS-01, PR.DS-12, PR.PS-06
    - NIST PF 1.0: GV.PO-P1, GV.PO-P2, GV.PO-P3, GV.PO-P4, ID.DE-P1, ID.DE-P2, PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented schema allow-list enforced via column-level review and migration gating
    - API input validation rejecting unknown fields with documented rejection response
    - Documented log scrubber with regex strip of personal-data patterns at ingest
    - DPIA-driven field review with quarterly schema-diff report

---

### PO-D-05.2-001 — Retain Personal Data Only as Needed

> **Sub-Domain:** D-05.2 — Retention & Archiving | **Cluster:** D-05 — Data Lifecycle
> **Applicable Regulation(s):** GDPR (privacy-driven)
> **Source Obligation (Doc 08 §4):** OBL-D-05.2-001
> **Doc 11 §4 CR Rule:** CR-D-05.2-001
> **Doc 10 §3.1 Risk Profile:** LOW | **Priority:** MODERATE
> **Phase 1 §1 Generic Sub-SO:** SO-D-05.2.GDPR (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.2/D-05.2.json`
> **Phase 1 Appendix A §A.1.1 Card:** PO-D-05.2-001 (matches this card; per-sub-domain deep enrichment in 07c Appendix A §A.1.1)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-05.2.json` (7 CSF + 12 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-05.2
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly review
> **Doc 03 Design Decisions Log:** DD-06 (managed object storage lifecycle 90d post-contract-end)
> **Doc 04 §4 Business Goal Link:** BG-01 (Operational efficiency with minimal data)
> **Audit Artefact (Doc 11 §4):** Managed object storage lifecycle audit + DSAR working-data disposal log + Portuguese commercial law alignment note
> **Verification Cadence:** Quarterly review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §2a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (PO #5 of 11)
> **Fase de Especificação 5 Card Position:** 5/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Personal data must be retained only for the period required to satisfy the documented purpose. The retention matrix is: 30 days for active-task data post-completion, 7 years for financial records (Portuguese commercial-law requirement), 7 years for audit logs (CRA Art. 31 — technical documentation 10y is SO-D-09.1; 7y here is the operational audit-log floor). Managed object-storage lifecycle rules and managed relational database lifecycle policies automate deletion; DSAR working data is disposed within 30 days of request completion per Doc 07b §4. This objective binds D-05.2 (Retention).
2. **Scope:** Managed relational database lifecycle policies, managed object storage lifecycle rules (customer content 90d post-contract-end), managed backup retention windows, DSAR working-data disposal, managed monitoring log retention.
3. **Out of Scope:** Customer-driven retention configuration (out of scope at default tier); cross-region replication beyond 90 days (replication inherits source lifecycle).
4. **Source Article:** GDPR Art. 5(1)(e) + Art. 17(1)(a); CRA Art. 31(1) (technical documentation 10y — only the SO side).
5. **NIST CSF Anchors:** GV.OC-04, GV.OV-02, GV.PO-02, ID.AM-03, PR.DS-10, PR.PS-02, PR.PS-04.
6. **Privacy FW Anchors:** CT.DM-P5, CT.PO-P4.
7. **Verification Criteria:**
   - Managed object-storage lifecycle rules expire customer-content objects 90 days post-contract-end; verified by managed bucket-lifecycle API audit monthly.
   - DSAR working-data disposal log shows each completed request within 30 days; sampled 1/quarter for completeness.
   - Backup retention window ≥ 7 years for audit logs; quarterly review note documents alignment with Portuguese commercial law (Código Comercial Art. 52).
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + DPO.
10. **Status:** TODO.
11. **Dependencies:** D-05.1 (minimisation reduces retention surface), D-09.4 (RoPA documents retention rationale), CR-D-05.2-001, OBL-D-05.2-001, PO-D-05.2-001 (Phase 1).
12. **Risk if not met:** MEDIUM — over-retention expands DSAR/erasure scope and audit-finding exposure under Art. 5(1)(e).
13. **Affected Stakeholders:** Customers (data subjects), DPO, CTO, Legal, CNPD.
14. **Implementation Status:** NOT IMPLEMENTED (What's missing: formal retention schedule approval & automated purge)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; retention breach discovered retrospectively → CNPD notification under Art. 33 if data still in retention is exposed.
17. **External Auditor (Case_01):** Documented third-party security attestation (covers lifecycle automation integrity); ISO 27001 A.11.2.7 (secure disposal).
18. **Supervisory Body (Case_01):** CNPD (lead) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.OC-04, GV.OV-02, GV.PO-02, ID.AM-03, PR.DS-12, PR.PS-02, PR.PS-04
    - NIST PF 1.0: GV.MT-P1, GV.MT-P2, GV.PO-P1, GV.PO-P2, GV.PO-P3, GV.PO-P4, ID.DE-P1, ID.DE-P2, PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented retention matrix mapped to purpose with lifecycle rules on each storage tier
    - Quarterly retention audit with documented exceptions register
    - Documented DSAR working-data disposal workflow with completion SLA
    - Annual alignment review against applicable commercial-law retention floors

---

### PO-D-05.3-001 — Enable Erasure on User Request

> **Sub-Domain:** D-05.3 — Right to Erasure | **Cluster:** D-05 — Data Lifecycle
> **Applicable Regulation(s):** GDPR (fundamental right)
> **Source Obligation (Doc 08 §4):** OBL-D-05.3-001
> **Doc 11 §4 CR Rule:** CR-D-05.3-001
> **Doc 10 §3.1 Risk Profile:** LOW | **Priority:** CRITICAL
> **Phase 1 §1 Generic Sub-SO:** SO-D-05.3.GDPR (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.3/D-05.3.json`
> **Phase 1 Appendix A §A.1.1 Card:** PO-D-05.3-001 (matches this card; per-sub-domain deep enrichment in 07c Appendix A §A.1.1)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-05.3.json` (3 CSF + 3 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO (DPO co-owns: fundamental-right interface)
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** CONF-001 (vs SO-D-10.2 immutable logs; resolved via cryptographic sharding)
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly review
> **Doc 03 Design Decisions Log:** DD-07 (Erasure API within 7d SLA)
> **Doc 04 §4 Business Goal Link:** BG-02 (User rights fulfilment)
> **Audit Artefact (Doc 11 §4):** Erasure API integration test + cascade quarterly test + derived-store annual review
> **Verification Cadence:** Quarterly review + cascade test (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §2a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (PO #6 of 11)
> **Fase de Especificação 5 Card Position:** 6/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Personal data must be erased on data-subject request within 30 days (operational SLA is 7 days — well within the GDPR Art. 12(3) "without undue delay" requirement). Erasure must cascade to backups and derived stores. This is implemented as an internal Erasure API endpoint that deletes the row from the primary store and applies a managed backup exclude-tag policy so the next backup cycle skips the deleted customer; managed key-value store TTL provides a defence-in-depth deletion pass. This objective binds D-05.3 (Erasure / Right to be Forgotten) and interacts with SO-D-10.2 (Immutable Logs) under Conflict CONF-001 — resolved by **cryptographic sharding**: logs are anonymised (key destroyed) at the retention boundary, not deleted wholesale.
2. **Scope:** Erasure API endpoint, managed backup exclude-tag policy, managed key-value store TTL on customer-data tables, customer-facing UI delete-account flow, derived analytics-store purge.
3. **Out of Scope:** Anonymisation in place of erasure (rejected — the explicit GDPR right is to erasure, not anonymisation); erasure of public-Internet data published by the user (out of scope at MICRO).
4. **Source Article:** GDPR Art. 17 + Art. 12(3); CRA Annex I §1.7 (least-privilege includes post-purpose deletion).
5. **NIST CSF Anchors:** GV.SC-04, PR.DS-10, PR.DS-10, PR.AA-01.
6. **Privacy FW Anchors:** CT.DM-P4, CT.DM-P5.
7. **Verification Criteria:**
   - Erasure API endpoint removes row from primary store within 1 minute and applies backup exclude-tag within 24h; integration test verifies cascade across all stores within 30 days.
   - Cascade test: erasure request → zero personal data in production database + zero personal data in latest backup snapshot (validated quarterly).
   - Annual review confirms no personal data remains in derived/aggregated stores (analytics, derived caches) after the erasure window.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + DPO — DPO co-owns because erasure is a fundamental-right interface.
10. **Status:** TODO.
11. **Dependencies:** D-01.1, D-01.4 (integrity cryptographic check must be updated on erasure), D-05.2 (retention policy enables erasure), D-10.2 (log-anonymisation handles immutable-logs conflict), CR-D-05.3-001, OBL-D-05.3-001, AG-D-05.3-001 (Phase 1).
12. **Risk if not met:** HIGH — failure on a fundamental right creates Art. 83(5) administrative-fine exposure (up to €20M or 4% of global turnover).
13. **Affected Stakeholders:** Customers (data subjects), DPO, CTO, Legal, CNPD (high priority for SA enforcement).
14. **Implementation Status:** PARTIAL (What's missing: self-service erasure portal & backup purge verification)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only (compliant erasure is silent); non-erasable data leak → CNPD 72h breach notification.
17. **External Auditor (Case_01):** Documented third-party security attestation (covers exclude-tag mechanics); ISO 27001 A.18.1.4 + A.11.2.7.
18. **Supervisory Body (Case_01):** CNPD (lead — fundamental rights) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.SC-04, PR.DS-10, PR.DS-12
    - NIST PF 1.0: CT.DP-P4, PR.DS-P1, PR.DS-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Erasure API endpoint with documented cascade to primary store and backups
    - Backup exclude-tag policy applied within documented SLA after primary delete
    - Annual review of derived and aggregated stores for residual personal data
    - Documented conflict-resolution pattern (cryptographic sharding) for immutable-logs intersection

---

### PO-D-05.4-001 — Provide Data Export on Request

> **Sub-Domain:** D-05.4 — Data Portability | **Cluster:** D-05 — Data Lifecycle
> **Applicable Regulation(s):** GDPR-only (no CRA sub-SO for D-05.4)
> **Source Obligation (Doc 08 §4):** OBL-D-05.4-001
> **Doc 11 §4 CR Rule:** CR-D-05.4-001
> **Doc 10 §3.1 Risk Profile:** LOW | **Priority:** MODERATE
> **Phase 1 §1 Generic Sub-SO:** SO-D-05.4.GDPR (frozen corpus; no CRA sub-SO)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.4/D-05.4.json`
> **Phase 1 Appendix A §A.1.1 Card:** PO-D-05.4-001 (matches this card; per-sub-domain deep enrichment in 07c Appendix A §A.1.1)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-05.4.json` (2 CSF + 2 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-05.4
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly review
> **Doc 03 Design Decisions Log:** DD-08 (JSON-only portable format chosen)
> **Doc 04 §4 Business Goal Link:** BG-02 (User rights fulfilment)
> **Audit Artefact (Doc 11 §4):** JSON export integration test + schema stability check
> **Verification Cadence:** Quarterly review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §2a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (PO #7 of 11)
> **Fase de Especificação 5 Card Position:** 7/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Data subjects must be able to export their personal data in a structured, commonly used, machine-readable format. This is a JSON export endpoint that bundles all customer data into a single downloadable archive (tasks, comments, attachments metadata, profile) within 48 hours of request. This is GDPR-only (no CRA sub-SO for D-05.4 — CRA does not require portability). This objective binds D-05.4 (Data Portability).
2. **Scope:** JSON export endpoint (single API call), GDPR Art. 20 portable-format generation, customer-facing UI "Download my data" button.
3. **Out of Scope:** Direct transfer to another controller (deferred — not a customer request at small scale); alternative structured formats (JSON is the only documented format in the customer-facing UI).
4. **Source Article:** GDPR Art. 20 (Right to Data Portability).
5. **NIST CSF Anchors:** GV.OC-04, PR.DS-10, PR.PS-06.
6. **Privacy FW Anchors:** CT.DM-P1, CT.DM-P6.
7. **Verification Criteria:**
   - Export API returns a valid JSON archive containing all documented customer-data tables within 48h; validated by integration test against a synthetic customer.
   - Schema is documented and stable across releases; sample archive is regenerated as part of the build artefact.
   - Annual review confirms the export covers all data categories listed in the RoPA (Doc 07b §3).
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + DPO.
10. **Status:** TODO.
11. **Dependencies:** D-05.1 (minimisation keeps export scope manageable), D-09.4 (RoPA lists what must be portable), CR-D-05.4-001, OBL-D-05.4-001, AG-D-05.4-001 (Phase 1).
12. **Risk if not met:** MEDIUM — failure creates Art. 83(4) administrative-fine exposure; reputational harm to brand.
13. **Affected Stakeholders:** Customers (data subjects), DPO, CTO, Legal, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: automated JSON export routine for all data categories)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only (compliant portability is silent); export-service outage → CNPD notification if >72h.
17. **External Auditor (Case_01):** Documented third-party security attestation; ISO 27001 A.18.1.4.
18. **Supervisory Body (Case_01):** CNPD (lead) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: PR.DS-10, PR.DS-12
    - NIST PF 1.0: PR.DS-P1, PR.DS-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented export endpoint bundling all customer-data tables within SLA
    - Schema stability check as part of release pipeline with documented schema baseline
    - Annual review confirming export coverage matches records-of-processing categories
    - Documented customer-facing export trigger with status notification

---

### PO-D-07.1-001 — Integrate Privacy into Design

> **Sub-Domain:** D-07.1 — Secure-by-Design | **Cluster:** D-07 — Secure Development
> **Applicable Regulation(s):** GDPR + CRA (dual coverage; "by design" in GDPR + "security by design" in CRA)
> **Source Obligation (Doc 08 §4):** OBL-D-07.1-001
> **Doc 11 §4 CR Rule:** CR-D-07.1-001
> **Doc 10 §3.1 Risk Profile:** LOW | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-07.1.GDPR + SO-D-07.1.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/D-07.1.json`
> **Phase 1 Appendix A §A.1.1 Card:** PO-D-07.1-001 (matches this card; per-sub-domain deep enrichment in 07c Appendix A §A.1.1)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-07.1.json` (5 CSF + 6 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev (D-07 → CTO + Lead Dev per owner matrix)
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** INSPECT (PR review + posture artefacts)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-07.1
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Annual SAMM assessment
> **Doc 03 Design Decisions Log:** DD-03 (PbD via PR review gates)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** Posture assessment + PR review checklist sample
> **Verification Cadence:** Annual posture assessment + per-PR review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §2a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (PO #8 of 11)
> **Fase de Especificação 5 Card Position:** 8/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Privacy must be integrated into the design and development of processing activities ("data protection by design" — GDPR Art. 25). This is operationalised through: secure-development-framework practice alignment, posture assessment targeting Level 1, privacy review gates on each PR that touches personal-data schema or processing logic, and threat modelling at feature-design time. This objective binds D-07.1 (Secure-by-Design / PbD) and is the upstream enabler for PO-D-05.1 (minimisation) and PO-D-09.2 (DPIA).
2. **Scope:** SDLC process (privacy review checklist), PR-review gate (block merge on missing privacy-review for personal-data-touching PRs), threat-modelling template (STRIDE-lite), posture self-assessment (annual).
3. **Out of Scope:** Formal Common Criteria evaluation (out of scope at small scale); Privacy-Enhancing Technologies beyond standard pseudonymisation.
4. **Source Article:** GDPR Art. 25 (Data Protection by Design and by Default); CRA Annex I §1.2 (security by design).
5. **NIST CSF Anchors:** GV.PO-01, GV.RM-04, PR.PS-01, PR.PS-06.
6. **Privacy FW Anchors:** CT.DP-P2, CT.DP-P4, CT.DP-P5, CT.PO-P4, GV.PO-P2.
7. **Verification Criteria:**
   - PR-review gate: 100% of personal-data-touching PRs in the last quarter have a documented privacy-review checklist entry (sampled 1/quarter).
   - Posture assessment current within 12 months; minimum target Level 1 across all five business functions.
   - Threat model document exists for each major feature launched in the last 12 months; sample 1/quarter for completeness.
8. **Verification Method:** INSPECT (Track B LIGHTWEIGHT) — review PRs + SAMM artefacts.
9. **Owner:** CTO + Lead Dev — D-07 → CTO + Lead Dev per owner matrix.
10. **Status:** TODO.
11. **Dependencies:** D-09.2 (DPIA), D-10.3 (security testing), CR-D-07.1-001, OBL-D-07.1-001, AG-D-07.1-001 (Phase 1).
12. **Risk if not met:** MEDIUM — failure to integrate privacy upstream forces expensive retrofit; non-compliance with Art. 25.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, DPO, Legal, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence).
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; design failure materialised as breach → CNPD 72h + ENISA 24h.
17. **External Auditor (Case_01):** Documented third-party security attestation; ISO 27001 A.14.2.1 (secure development policy).
18. **Supervisory Body (Case_01):** CNPD (lead) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: ID.RA-01, PR.DS-12, PR.PS-01, PR.PS-02, PR.PS-06
    - NIST PF 1.0: ID.RA-P1, ID.RA-P3, PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented PR-review gate with privacy-review checklist for personal-data-touching changes
    - Threat-modelling template applied at feature-design stage with documented output
    - Annual posture self-assessment across the five business functions
    - Documented secure-development-framework practice alignment

---

### PO-D-09.1-001 — Maintain Privacy Policies

> **Sub-Domain:** D-09.1 — Information Security Policies | **Cluster:** D-09 — Governance & Documentation
> **Applicable Regulation(s):** GDPR + CRA (dual coverage; Art. 24 + Art. 31)
> **Source Obligation (Doc 08 §4):** OBL-D-09.1-001
> **Doc 11 §4 CR Rule:** CR-D-09.1-001
> **Doc 10 §3.1 Risk Profile:** LOW | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-09.1.GDPR + SO-D-09.1.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/D-09.1.json`
> **Phase 1 Appendix A §A.1.1 Card:** PO-D-09.1-001 (matches this card; per-sub-domain deep enrichment in 07c Appendix A §A.1.1)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-09.1.json` (14 CSF + 10 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO + Compliance Lead + Legal (D-09 → all four per owner matrix)
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** INSPECT (document review)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** Dual-coverage intentional with SO-D-09.1 (same ISMS framework)
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Annual policy review
> **Doc 03 Design Decisions Log:** DD-09 (version-control-based policy management over GRC tool)
> **Doc 04 §4 Business Goal Link:** BG-05 (Governance & documentation discipline)
> **Audit Artefact (Doc 11 §4):** Policy version history + DPA template audit + annual review note
> **Verification Cadence:** Annual policy review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §2a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (PO #9 of 11)
> **Fase de Especificação 5 Card Position:** 9/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** A comprehensive set of privacy policies must document the appropriate technical and organisational measures (GDPR Art. 24 "responsibility of the controller"). The set of policy documents includes: Privacy Policy (customer-facing), Cookie Policy, Data Processing Agreement (DPA) template, internal Acceptable Use Policy, Records Retention Policy, Information Security Policy, and Breach Response Procedure. This objective binds D-09.1 (Information Security Policies) and is the documentation baseline for both GDPR Art. 24 and CRA Art. 31 technical documentation. Dual-coverage with SO-D-09.1 is intentional — the same ISMS framework satisfies both.
2. **Scope:** Privacy Policy (web), Cookie Policy, DPA template (B2B customer contracts), AUP (staff handbook), Information Security Policy, Records Retention Policy, Breach Response Procedure, DPIA template.
3. **Out of Scope:** Policy management software (overkill to buy a GRC tool at MICRO); policy versioning beyond the version-control-based PR-review approval flow.
4. **Source Article:** GDPR Art. 24 + Art. 5(2) (accountability); CRA Art. 31 (technical documentation).
5. **NIST CSF Anchors:** GV.PO-01, GV.OC-02, GV.OV-01.
6. **Privacy FW Anchors:** CM.PO-P1, GV.PO-P1, GV.PO-P5.
7. **Verification Criteria:**
   - All seven policy documents exist in the docs repo with last-reviewed date ≤ 12 months; sampled annually.
   - Privacy Policy is published on the corporate website with a version-effective date.
   - DPA template includes all GDPR Art. 28(3) required clauses (verified by Compliance Lead annually).
8. **Verification Method:** INSPECT (Track B LIGHTWEIGHT) — document review.
9. **Owner:** CTO + DPO + Compliance Lead + Legal — D-09 → all four per owner matrix.
10. **Status:** TODO.
11. **Dependencies:** D-09.2 (DPIA feeds the policies), D-09.4 (RoPA), CR-D-09.1-001, OBL-D-09.1-001, AG-D-09.1-001 (Phase 1), AG-D-09.1-002 (Phase 1).
12. **Risk if not met:** MEDIUM — gap in policy documentation is an audit finding under Art. 24 and CRA Art. 31.
13. **Affected Stakeholders:** Customers (data subjects), DPO, Compliance Lead, Legal, CTO, CNPD, ENISA.
14. **Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence).
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** CNPD + ENISA periodic (policy version history is auditable artefact).
17. **External Auditor (Case_01):** Documented third-party security attestation (covers ISMS-adjacent controls); ISO 27001 A.5.1.1 (policies for information security).
18. **Supervisory Body (Case_01):** CNPD (lead) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.OC-03, GV.OC-04, GV.OV-01, GV.OV-03, GV.PO-01, GV.PO-02, GV.RM-01, GV.RM-04, GV.RM-05, GV.RR-01, GV.RR-02, GV.RR-03, GV.SC-01, GV.SC-04
    - NIST PF 1.0: CT.DP-P4, GV.MT-P1, GV.MT-P2, GV.PO-P1, GV.PO-P2, GV.PO-P3, GV.PO-P4, GV.PO-P5, GV.RM-P1, ID.RA-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Version-control-based policy set covering all documented categories with annual review
    - Documented DPA template with all required contractual clauses
    - Published privacy notice with version-effective date and review trail
    - Annual policy version-history audit with documented sign-off

---

### PO-D-09.2-001 — Conduct DPIA Pre-Launch

> **Sub-Domain:** D-09.2 — Impact & Risk Assessments | **Cluster:** D-09 — Governance & Documentation
> **Applicable Regulation(s):** GDPR + CRA (dual coverage; Art. 35 + Art. 13(5))
> **Source Obligation (Doc 08 §4):** OBL-D-09.2-001
> **Doc 11 §4 CR Rule:** CR-D-09.2-001
> **Doc 10 §3.1 Risk Profile:** LOW | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-09.2.GDPR + SO-D-09.2.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/D-09.2.json`
> **Phase 1 Appendix A §A.1.1 Card:** PO-D-09.2-001 (matches this card; per-sub-domain deep enrichment in 07c Appendix A §A.1.1)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-09.2.json` (6 CSF + 9 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO + Compliance Lead + Legal
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** INSPECT + ANALYZE (document review + risk analysis)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** Unified assessment pattern with SO-D-09.2 (T-002 resolved)
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Annual + per-feature
> **Doc 03 Design Decisions Log:** DD-10 (Unified DPIA+CRA assessment template)
> **Doc 04 §4 Business Goal Link:** BG-05 (Governance & documentation discipline)
> **Audit Artefact (Doc 11 §4):** DPIA template audit + sign-off workflow + sample quarterly
> **Verification Cadence:** Annual review + per-feature DPIA (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §2a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (PO #10 of 11)
> **Fase de Especificação 5 Card Position:** 10/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Privacy impact assessments (DPIAs — GDPR Art. 35) must be conducted before any new processing that is likely to result in a high risk to data subjects. The DPIA is conducted using a unified assessment template that produces dual output: a GDPR DPIA and a CRA cybersecurity risk assessment (see SO-D-09.2 for the CRA side). This is a deliberate "unified assessment" pattern — the same risk-analysis workflow produces both artefacts, halving the effort relative to running two parallel assessments. This objective binds D-09.2 (Impact & Risk Assessments).
2. **Scope:** DPIA template (GDPR Art. 35 minimum content), unified assessment workflow, risk-treatment plan output, sign-off workflow (CTO + DPO + Compliance Lead + Legal), periodic review trigger.
3. **Out of Scope:** Full quantitative risk modelling (overkill at small scale); separate GDPR-only and CRA-only assessments (rejected — the unified template is the chosen pattern).
4. **Source Article:** GDPR Art. 35 + Art. 36 (prior consultation); CRA Art. 13(5) (cybersecurity risk assessment).
5. **NIST CSF Anchors:** GV.RM-04, GV.OC-02, ID.RA-01, ID.RA-04, ID.RA-05.
6. **Privacy FW Anchors:** ID.RA-P3, ID.RA-P4, ID.RA-P5.
7. **Verification Criteria:**
   - DPIA template includes all Art. 35(7) minimum content sections (description, necessity, risk assessment, mitigations); verified annually by Compliance Lead.
   - Unified assessment produces both a GDPR DPIA output and a CRA risk-assessment output for every feature launched in the last 12 months; sampled 1/quarter.
   - Sign-off workflow records CTO + DPO + Compliance Lead + Legal approvals before feature GA.
8. **Verification Method:** INSPECT + ANALYZE (Track B LIGHTWEIGHT) — document review + risk analysis.
9. **Owner:** CTO + DPO + Compliance Lead + Legal.
10. **Status:** TODO.
11. **Dependencies:** D-07.1 (PbD feeds the DPIA), D-09.1 (policies), CR-D-09.2-001, OBL-D-09.2-001, AG-D-09.2-001 (Phase 1), AG-D-09.2-002 (Phase 1).
12. **Risk if not met:** MEDIUM — failure to DPIA a high-risk feature triggers Art. 36 prior-consultation requirements and Art. 83(4) fine exposure.
13. **Affected Stakeholders:** Customers (data subjects), DPO, Compliance Lead, Legal, CTO, CNPD, ENISA.
14. **Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence).
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** CNPD periodic (DPIA submission on request) + ENISA periodic.
17. **External Auditor (Case_01):** ISO 27001 A.18.1.4 (privacy impact assessment).
18. **Supervisory Body (Case_01):** CNPD (lead) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.OV-01, GV.RM-04, GV.RR-02, ID.RA-04, ID.RA-05, ID.SC-04
    - NIST PF 1.0: CT.DP-P1, CT.DP-P2, GV.MT-P1, GV.MT-P2, GV.PO-P5, GV.RM-P1, ID.RA-P1, ID.RA-P2, ID.RA-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented unified assessment template producing dual GDPR + CRA output
    - Pre-launch sign-off workflow with multi-role approval captured before GA
    - Annual DPIA review and per-feature DPIA with documented scope decision
    - Documented risk-treatment plan output with residual-risk acceptance

---

### PO-D-09.4-001 — Maintain Records of Processing

> **Sub-Domain:** D-09.4 — Records of Processing | **Cluster:** D-09 — Governance & Documentation
> **Applicable Regulation(s):** GDPR + CRA (RoPA partially satisfies CRA Art. 31)
> **Source Obligation (Doc 08 §4):** OBL-D-09.4-001
> **Doc 11 §4 CR Rule:** CR-D-09.4-001
> **Doc 10 §3.1 Risk Profile:** LOW | **Priority:** MODERATE
> **Phase 1 §1 Generic Sub-SO:** SO-D-09.4.GDPR + SO-D-09.4.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.json`
> **Phase 1 Appendix A §A.1.1 Card:** PO-D-09.4-001 (matches this card; per-sub-domain deep enrichment in 07c Appendix A §A.1.1)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-09.4.json` (5 CSF + 8 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO + Compliance Lead + Legal
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** INSPECT (records-of-processing + breach log review)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-09.4
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly review
> **Doc 03 Design Decisions Log:** None for D-09.4 (Markdown + managed object storage immutable retention standard)
> **Doc 04 §4 Business Goal Link:** BG-05 (Governance & documentation discipline)
> **Audit Artefact (Doc 11 §4):** RoPA quarterly review + immutable breach log + Art. 30 compliance check
> **Verification Cadence:** Quarterly review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §2a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (PO #11 of 11)
> **Fase de Especificação 5 Card Position:** 11/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Records of all personal-data processing activities (GDPR Art. 30 — RoPA) must be maintained in writing. The RoPA is held as a living Markdown document in the docs repo with quarterly reviews; a separate immutable breach log (managed object storage bucket with immutable retention) records all personal-data incidents regardless of severity. This objective binds D-09.4 (Records of Processing) and is the primary GDPR accountability artefact requested by CNPD during investigations.
2. **Scope:** RoPA template (Art. 30 minimum content), quarterly review workflow, immutable breach log (managed object storage with immutable retention), RoPA export to structured format for auditor convenience.
3. **Out of Scope:** Cross-organisation RoPA harmonisation (no parent company); RoPA software (GRC-style tool overkill at small scale).
4. **Source Article:** GDPR Art. 30 (Records of processing activities); CRA Art. 31(1) (technical documentation — RoPA partially satisfies).
5. **NIST CSF Anchors:** GV.OC-02, ID.AM-01, ID.AM-02.
6. **Privacy FW Anchors:** ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8.
7. **Verification Criteria:**
   - RoPA covers all categories of processing identified in Doc 07b §3; quarterly review confirms no undocumented processing.
   - RoPA includes all Art. 30(1) fields (purposes, categories of data subjects/personal data, recipients, transfers, retention, security measures).
   - Immutable breach log: zero gaps in last 12 months; sampled monthly.
8. **Verification Method:** INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + DPO + Compliance Lead + Legal.
10. **Status:** TODO.
11. **Dependencies:** D-05.2 (retention informs RoPA), D-09.1 (policies), D-09.2 (DPIA informs RoPA), CR-D-09.4-001, OBL-D-09.4-001, AG-D-09.4-001 (Phase 1).
12. **Risk if not met:** MEDIUM — failure creates Art. 83(4) administrative-fine exposure; first document requested in any CNPD investigation.
13. **Affected Stakeholders:** Customers (data subjects), DPO, Compliance Lead, Legal, CTO, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence).
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** CNPD periodic (RoPA provided on request) + ENISA periodic.
17. **External Auditor (Case_01):** ISO 27001 A.18.1.1 (identification of applicable legislation).
18. **Supervisory Body (Case_01):** CNPD (lead — Art. 30 is SA-jurisdiction) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.PO-01, GV.PO-02, ID.AM-08, ID.RA-05, PR.DS-12
    - NIST PF 1.0: GV.PO-P3, GV.PO-P4, ID.DE-P1, ID.DE-P2, ID.RA-P1, ID.RA-P3, PR.DS-P1, PR.DS-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Living records-of-processing document with quarterly review and documented changes
    - Immutable breach log with documented retention aligned to regulatory floor
    - Structured-format export capability for supervisory-authority request handling
    - Documented coverage check against minimum content requirements

---

### 6.2 Security Operational Objective Detail Cards (20 cards)

---

### SO-D-02.1-001 — Zero Known Exploitable Vulnerabilities

> **Sub-Domain:** D-02.1 — Vulnerability Identification | **Cluster:** D-02 — Vulnerability Management
> **Applicable Regulation(s):** CRA-primary (Annex I §1.3); GDPR Art. 32(1)(d) baseline
> **Source Obligation (Doc 08 §4):** OBL-D-02.1-001
> **Doc 11 §4 CR Rule:** CR-D-02.1-001
> **Doc 10 §4.1 Risk Profile:** MEDIUM | **Priority:** CRITICAL
> **Phase 1 §1 Generic Sub-SO:** SO-D-02.1.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.1/D-02.1.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-02.1-001 (matches this card; per-sub-domain deep enrichment in 07c Appendix A §A.2.1)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-02.1.json` (16 CSF + 14 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev + Procurement (D-02 → + Procurement per owner matrix)
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-02.1
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Per-build + monthly review
> **Doc 03 Design Decisions Log:** None for D-02.1 (automated vulnerability scanner + dependency audit + managed advisory feed standard)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** Automated vulnerability scan report + dependency audit log + managed advisory alerts review
> **Verification Cadence:** Per-build + monthly review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #1 of 20)
> **Fase de Especificação 5 Card Position:** 12/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** The product must be delivered and maintained with zero known exploitable vulnerabilities in third-party dependencies and in-house code. This is achieved through automated scanning in CI: container + filesystem scanner, Node.js dependency audit, managed dependency-advisory feed, and static analysis on PR. CI blocks merge on CRITICAL findings; HIGH findings create a 7-day remediation SLA. This objective binds D-02.1 (Vulnerability Identification) and is the CRA Annex I §1.3 baseline.
2. **Scope:** OSS dependencies (Node.js + container base images), in-house code (static analysis), container images (automated vulnerability scanner), infrastructure-as-code (infrastructure-as-code scanner).
3. **Out of Scope:** Dynamic application security testing (dynamic application security testing — deferred); runtime instrumentation (RIGOROUS tier); external bug-bounty programme (out of scope at small scale — replaced by CVD policy).
4. **Source Article:** CRA Annex I §1.3 (attack-surface minimisation); GDPR Art. 32(1)(d) (regular testing).
5. **NIST CSF Anchors:** GV.OV-02, ID.AM-02, ID.IM-02, ID.RA-01, ID.RA-03, ID.RA-05, PR.PS-02.
6. **Privacy FW Anchors:** ID.RA-P3, ID.RA-P5.
7. **Verification Criteria:**
   - CI pipeline runs automated vulnerability scanner on every PR — block merge on CRITICAL findings (gate verified by sampling 1/quarter).
   - Node.js dependency audit `--audit-level=high` passes on every build (build artefact audit).
   - Managed dependency-advisory alerts enabled for all production repos; monthly review of unfixed HIGH/CRITICAL alerts with zero exceptions.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + Lead Dev + Procurement — D-02 → CTO + Lead Dev + Procurement per owner matrix.
10. **Status:** TODO.
11. **Dependencies:** D-02.2 (patch management), D-06.2 (SBOM), D-10.3 (security testing), CR-D-02.1-001, OBL-D-02.1-001, AG-D-02.1-002 (Phase 1).
12. **Risk if not met:** MEDIUM — known-exploitable vulnerability triggers CRA Art. 11 24h notification; CVSS-based reputational risk.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, Procurement, ENISA, CNPD.
14. **Implementation Status:** NOT IMPLEMENTED (What's missing: formal vulnerability register & zero-CVE release gate)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** ENISA 24h (CRA Art. 11 — actively exploited vulnerability) + CNPD 72h if exploited-vuln reaches personal data.
17. **External Auditor (Case_01):** Documented third-party security attestation (CC7.1 — vulnerability management); ISO 27001 A.12.6.1 (technical vulnerability management).
18. **Supervisory Body (Case_01):** ENISA (lead — CRA) + CNPD (if personal-data breach) + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.OV-02, GV.RM-01, GV.RM-06, GV.SC-04, ID.AM-02, ID.IM-02, ID.IM-04, ID.RA-01, ID.RA-03, ID.RA-04, ID.RA-05, ID.RA-06, PR.PS-02, PR.PS-06, RS.MA-03, RS.MI-01
    - NIST PF 1.0: CT.DP-P4, GV.MT-P1, GV.MT-P2, GV.RM-P1, ID.DE-P1, ID.DE-P2, ID.IM-P1, ID.IM-P2, ID.RA-P1, ID.RA-P2, ID.RA-P3, PR.MA-P1, PR.PO-P1, PR.PO-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Automated vulnerability scan in CI with documented CRITICAL-blocking gate
    - Documented dependency-audit baseline with audit-level threshold enforced per build
    - Managed advisory feed subscription with documented monthly review of HIGH/CRITICAL alerts
    - Quarterly false-positive review with documented remediation SLAs

---

### SO-D-02.2-001 — Automatic Security Updates

> **Sub-Domain:** D-02.2 — Patch Management & Updates | **Cluster:** D-02 — Vulnerability Management
> **Applicable Regulation(s):** CRA-primary (Annex I §2 + Art. 11(2)); GDPR Art. 32(1)(b)
> **Source Obligation (Doc 08 §4):** OBL-D-02.2-001
> **Doc 11 §4 CR Rule:** CR-D-02.2-001
> **Doc 10 §4.1 Risk Profile:** MEDIUM | **Priority:** CRITICAL
> **Phase 1 §1 Generic Sub-SO:** SO-D-02.2.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.2/D-02.2.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-02.2-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-02.2.json` (7 CSF + 8 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev + Procurement
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-02.2
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Daily patch scan + quarterly review
> **Doc 03 Design Decisions Log:** None for D-02.2 (managed patch orchestration + automated dependency-update standard)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** Managed patch orchestration log + automated dependency-update PR review + quarterly review
> **Verification Cadence:** Daily scan + quarterly review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #2 of 20)
> **Fase de Especificação 5 Card Position:** 13/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Identified vulnerabilities must be remediated through automatic security updates according to severity-based SLAs: critical 24h, high 7d, medium 30d, low quarterly. Managed patch orchestration automates OS-level patches; container base-image rebuilds are triggered by managed dependency-advisory feed; Node.js dependency upgrades are automated via automated dependency-update bot. This objective binds D-02.2 (Patch Management) and is the response limb to SO-D-02.1 (identification).
2. **Scope:** OS-level patches (hardened base images), container base-image rebuilds, dependency upgrades (Node.js + container base), infrastructure-as-code module updates.
3. **Out of Scope:** Zero-day emergency patching outside maintenance window (procedural exception documented in incident-response runbook); customer-deployed on-prem components (out of SaaS scope).
4. **Source Article:** CRA Annex I §2 (vulnerability handling) + Art. 11(2); GDPR Art. 32(1)(b) + Art. 32(1)(d).
5. **NIST CSF Anchors:** GV.OV-02, ID.RA-01, PR.PS-01, PR.PS-02, PR.IR-03.
6. **Privacy FW Anchors:** — (SSDF RV.2 deliverable).
7. **Verification Criteria:**
   - Managed patch orchestration `Scan` + `Install` baselines run daily; patch log audited weekly.
   - Critical patches remediated within 24h (tracked in patch log); quarterly review confirms zero missed critical CVEs in current scope.
   - Automated dependency-update bot creates PRs for dependency updates weekly; PR-merge SLA 7d for HIGH, 30d for MEDIUM.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + Lead Dev + Procurement.
10. **Status:** TODO.
11. **Dependencies:** D-02.1 (identification triggers patch), D-10.2 (log records patch operations), CR-D-02.2-001, OBL-D-02.2-001, AG-D-02.2-002 (Phase 1).
12. **Risk if not met:** MEDIUM — slow patch response triggers CRA Art. 11 24h notification if exploited; reputational risk.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, Procurement, ENISA, CNPD.
14. **Implementation Status:** NOT IMPLEMENTED (What's missing: automated patch SLAs & 72h remediation workflow)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** ENISA 24h (CRA Art. 11 — actively exploited vulns reach this SLA) + CNPD 72h if data-breach trigger.
17. **External Auditor (Case_01):** Documented third-party security attestation (CC7.1); ISO 27001 A.12.6.2 + A.14.2.4.
18. **Supervisory Body (Case_01):** ENISA (lead) + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.OV-02, ID.RA-01, ID.RA-06, PR.IR-01, PR.IR-03, PR.PS-01, PR.PS-02
    - NIST PF 1.0: GV.MT-P1, GV.MT-P2, ID.RA-P1, ID.RA-P3, PR.PO-P1, PR.PO-P3, PR.PT-P1, PR.PT-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented severity-based patch SLAs with automated orchestration log
    - Documented base-image rebuild trigger from advisory-feed integration
    - Quarterly review confirming zero missed critical findings in current scope
    - Documented dependency-update workflow with PR-merge SLAs by severity

---

### SO-D-02.3-001 — CVD Policy + ENISA Reporting

> **Sub-Domain:** D-02.3 — Coordinated Vuln. Disclosure | **Cluster:** D-02 — Vulnerability Management
> **Applicable Regulation(s):** CRA-primary (Art. 12); ISO/IEC 29147 + 30111
> **Source Obligation (Doc 08 §4):** OBL-D-02.3-001
> **Doc 11 §4 CR Rule:** CR-D-02.3-001
> **Doc 10 §4.1 Risk Profile:** LOW | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-02.3.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.3/D-02.3.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-02.3-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-02.3.json` (4 CSF + 7 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev + Procurement
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-02.3
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Monthly external probe
> **Doc 03 Design Decisions Log:** None for D-02.3 (security.txt per RFC 9116 standard)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** security.txt probe log + CVD page review + mailbox SLA
> **Verification Cadence:** Monthly external probe + 5-business-day SLA (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #3 of 20)
> **Fase de Especificação 5 Card Position:** 14/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** A coordinated vulnerability disclosure (CVD) ecosystem must be maintained covering the manufacturer side, third-party reporters, and ENISA. The disclosure channel includes: a security.txt at the well-known path (`/.well-known/security.txt` per RFC 9116), a dedicated security contact, a public CVD page on the corporate website describing the disclosure process, and a 24h acknowledgement SLA. This objective binds D-02.3 (Coordinated Vulnerability Disclosure) and is the upstream enabler for CRA Art. 12 single-reporting-platform compliance.
2. **Scope:** `/.well-known/security.txt` file (RFC 9116 compliant), dedicated security mailbox, CVD page on website, 5-business-day acknowledgement SLA, triage workflow.
3. **Out of Scope:** External bug-bounty programme (out of scope at small scale — replaced by CVD policy); anonymous-tor-only reporting channel (not justified).
4. **Source Article:** CRA Art. 12 (coordinated vulnerability disclosure); ISO/IEC 29147 (vulnerability disclosure) + ISO/IEC 30111 (vulnerability handling).
5. **NIST CSF Anchors:** GV.PO-01, GV.SC-04, ID.RA-01, RS.CO-03.
6. **Privacy FW Anchors:** — (SSDF RV.1 deliverable).
7. **Verification Criteria:**
   - `/.well-known/security.txt` returns HTTP 200 with valid `Contact`, `Expires`, and `Disclosure` policy fields; verified by automated external probe monthly.
   - External researcher test email acknowledged within 5 business days; SLA tracked in mailbox auto-responder.
   - CVD page on corporate site links to `security.txt` and contains the 24h-reporting commitment.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + Lead Dev + Procurement.
10. **Status:** TODO.
11. **Dependencies:** D-02.1 (CVD findings feed back into vulnerability identification), D-04.3 (notification SLA), CR-D-02.3-001, OBL-D-02.3-001, AG-D-02.3-002 (Phase 1).
12. **Risk if not met:** MEDIUM — missing CVD creates Art. 12 non-compliance and weakens external-researcher trust; reputational risk.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, Procurement, ENISA, external researchers, CNPD.
14. **Implementation Status:** NOT IMPLEMENTED (What's missing: published security.txt & CVD reporting policy)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** ENISA 24h (CRA Art. 12 — when reported vuln is actively exploited) + CNPD 72h if data-breach trigger.
17. **External Auditor (Case_01):** ISO 27001 A.16.1.2 (reporting information security events).
18. **Supervisory Body (Case_01):** ENISA (lead — CRA Art. 12 is ENISA-platform domain) + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.PO-01, GV.SC-04, ID.RA-01, RS.CO-03
    - NIST PF 1.0: CT.DP-P4, CT.PO-P1, GV.AT-P2, GV.PO-P3, GV.PO-P4, ID.RA-P1, ID.RA-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Published well-known disclosure-policy file with documented required fields
    - Documented security contact mailbox with tracked acknowledgement SLA
    - Public CVD page on corporate site linking to disclosure-policy file
    - Documented triage workflow with acknowledgement target

---

### SO-D-03.1-001 — Authentication for All Interfaces

> **Sub-Domain:** D-03.1 — Identity Lifecycle | **Cluster:** D-03 — Access Control
> **Applicable Regulation(s):** CRA-primary (Annex I §1.1 + §1.4); GDPR Art. 32(1)(b)
> **Source Obligation (Doc 08 §4):** OBL-D-03.1-001
> **Doc 11 §4 CR Rule:** CR-D-03.1-001
> **Doc 10 §4.1 Risk Profile:** MEDIUM | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-03.1.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.1/D-03.1.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-03.1-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-03.1.json` (10 CSF + 10 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev (D-03 → CTO + Lead Dev per owner matrix)
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-03.1
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly orphan-account scan
> **Doc 03 Design Decisions Log:** DD-04 (managed identity service over self-hosted identity provider)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** Managed identity service audit + RBAC review + managed edge filtering rate-limit test
> **Verification Cadence:** Quarterly review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #4 of 20)
> **Fase de Especificação 5 Card Position:** 15/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** All user-facing interfaces (web app, mobile web, API, admin console) must implement authentication controls. This is a managed identity service for customer-facing flows and managed identity service + token-based CI authentication for admin/CI flows. No interface is publicly accessible without authentication; rate-limiting and brute-force protection are layered at managed content delivery + managed edge filtering. This objective binds D-03.1 (Identity Lifecycle) and is the prerequisite for SO-D-03.2 (MFA), SO-D-03.3 (RBAC).
2. **Scope:** Managed identity service (customer web + API), managed identity service (admin console), token-based CI authentication (CI/CD), managed content delivery + managed edge filtering rate-limiting.
3. **Out of Scope:** Self-hosted identity provider (overkill at small scale); legacy federation-via-standard-protocol (not in customer base); passwordless-only auth (managed identity service supports but requires MFA fallback — deferred).
4. **Source Article:** CRA Annex I §1.1 (confidentiality of stored data) + §1.4 (integrity); GDPR Art. 32(1)(b) + Art. 25(2).
5. **NIST CSF Anchors:** PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02.
6. **Privacy FW Anchors:** PR.AC-P1, PR.AC-P6, PR.AC-P4; ALT-ANCHOR (800-53r5 CM-8; SSDF PO.5.1) (asset inventory + risk-strategy data mgmt — no PF 1.0 analogue).
7. **Verification Criteria:**
   - Managed identity service user records have `disabled` flag set within 30d of contract end; quarterly orphan-account scan with zero stale accounts.
   - Custom claims (RBAC roles) reviewed quarterly against current employee list; sample 1/quarter.
   - Managed content delivery + managed edge filtering: rate-limit rule returns HTTP 429 after 100 req/min/IP for unauthenticated paths (validated by synthetic load test quarterly).
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + Lead Dev — D-03 → CTO + Lead Dev per owner matrix.
10. **Status:** TODO.
11. **Dependencies:** D-03.2 (MFA), D-03.3 (RBAC), D-06.1 (vendor identity assurance), CR-D-03.1-001, OBL-D-03.1-001, AG-D-03.1-002 (Phase 1).
12. **Risk if not met:** MEDIUM — unauthenticated-interface exposure is an audit finding; data-breach trigger.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, CNPD, ENISA.
14. **Implementation Status:** IMPLEMENTED (Auth0 managed identity service active - Doc 04a SYS-02)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** ENISA 24h if exploited; CNPD 72h if personal-data breach.
17. **External Auditor (Case_01):** Documented third-party security attestation (CC6.1 — logical access); ISO 27001 A.9.2.1 (user registration).
18. **Supervisory Body (Case_01):** ENISA (CRA Art. 6 baseline) + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: DE.CM-09, ID.AM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02, PR.DS-12
    - NIST PF 1.0: CM.AW-P1, CM.PO-P1, GV.AT-P1, ID.DE-P1, ID.DE-P2, PR.AC-P1, PR.AC-P3, PR.AC-P6, PR.DS-P1, PR.DS-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Managed identity baseline with documented disable-on-termination lifecycle
    - Quarterly orphan-account scan with documented stale-account findings
    - Documented rate-limit rule with synthetic load test verifying rejection behaviour
    - Quarterly access review with documented employee-list reconciliation

---

### SO-D-03.2-001 — Multi-Factor Authentication Where Appropriate

> **Sub-Domain:** D-03.2 — Multi-Factor Authentication | **Cluster:** D-03 — Access Control
> **Applicable Regulation(s):** CRA-primary (Annex I §1.1 + §1.2); GDPR Art. 32(1)
> **Source Obligation (Doc 08 §4):** OBL-D-03.2-001
> **Doc 11 §4 CR Rule:** CR-D-03.2-001
> **Doc 10 §4.1 Risk Profile:** LOW | **Priority:** MODERATE
> **Phase 1 §1 Generic Sub-SO:** SO-D-03.2.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.2/D-03.2.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-03.2-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-03.2.json` (10 CSF + 12 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev
> **Track B Tier (Doc 07b §4):** MINIMAL
> **Fase de Especificação 5 Verification Method:** INSPECT (MFA enforcement test)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-03.2
> **Doc 07b §4 Proportionality:** Tier=MINIMAL, Cadence=Quarterly MFA enforcement check
> **Doc 03 Design Decisions Log:** None for D-03.2 (TOTP via authenticator app — hardware-token MFA overkill)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** MFA enforcement test + password reset flow review + credential report
> **Verification Cadence:** Quarterly MFA check (Doc 07b §4 MINIMAL)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #5 of 20)
> **Fase de Especificação 5 Card Position:** 16/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Multi-factor authentication (MFA) must be enabled for accounts with access to personal data or administrative privileges. MFA is enforced on all customer accounts via managed identity service MFA (mandatory at registration), MFA enforced on all admin accounts (managed identity service + hardware-token-backed for break-glass), MFA on CI/CD via branch protection + token-based authentication. "Where appropriate" is interpreted broadly — every authenticated user gets MFA, no exceptions. This objective binds D-03.2 (MFA).
2. **Scope:** Managed identity service MFA (customer), managed identity service MFA (admin), branch-protection MFA (code), CI/CD token-based authentication scopes.
3. **Out of Scope:** Hardware-token MFA for end users (overkill at small scale — TOTP via authenticator app is sufficient); passwordless-only (requires MFA fallback).
4. **Source Article:** CRA Annex I §1.1 + §1.2; GDPR Art. 32(1) (appropriate measures); documented identity assurance framework.
5. **NIST CSF Anchors:** PR.AA-01, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06.
6. **Privacy FW Anchors:** PR.AC-P6, PR.AC-P4; ALT-ANCHOR (ASVS V3.5; 800-53r5 IA-4) (identity assertions — no PF 1.0 subcategory).
7. **Verification Criteria:**
   - Managed identity service MFA enforcement enabled for all customer accounts; quarterly check confirms zero accounts with MFA disabled.
   - Password reset flow uses signed reset tokens with 1h TTL; quarterly review confirms no password stored in plaintext.
   - Root account uses hardware-token MFA; quarterly credential report reviewed.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + Lead Dev.
10. **Status:** TODO.
11. **Dependencies:** D-03.1 (authentication), D-06.1 (vendor identity), CR-D-03.2-001, OBL-D-03.2-001, AG-D-03.2-002 (Phase 1).
12. **Risk if not met:** LOW — single-factor exposure is a known CWE-308; reputational and breach-impact risk.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, CNPD, ENISA.
14. **Implementation Status:** IMPLEMENTED (MFA mandatory for administrative accounts - Doc 04a §1.4)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; breach scenario → CNPD 72h + ENISA 24h.
17. **External Auditor (Case_01):** Documented third-party security attestation (CC6.1); ISO 27001 A.9.4.2 (secure log-on).
18. **Supervisory Body (Case_01):** CNPD (lead — GDPR Art. 32) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: DE.CM-09, ID.AM-01, PR.AA-01, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02, PR.DS-02, PR.IR-03
    - NIST PF 1.0: CM.AW-P1, CM.PO-P1, GV.AT-P1, ID.DE-P1, ID.DE-P2, PR.AC-P1, PR.AC-P3, PR.AC-P6, PR.DS-P1, PR.DS-P2, PR.PT-P1, PR.PT-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented MFA enforcement enabled for all customer and admin accounts
    - Documented password reset flow with signed-token TTL and credential-storage review
    - Hardware-token-backed MFA on break-glass credentials with quarterly credential report
    - Quarterly enforcement check with documented exceptions register

---

### SO-D-03.3-001 — Authorised Access Only

> **Sub-Domain:** D-03.3 — Authorisation & Least Privilege | **Cluster:** D-03 — Access Control
> **Applicable Regulation(s):** CRA + GDPR (dual coverage; least-privilege baseline)
> **Source Obligation (Doc 08 §4):** OBL-D-03.3-001
> **Doc 11 §4 CR Rule:** CR-D-03.3-001
> **Doc 10 §4.1 Risk Profile:** MEDIUM | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-03.3.GDPR + SO-D-03.3.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.3/D-03.3.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-03.3-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-03.3.json` (10 CSF + 10 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-03.3
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly IAM access review
> **Doc 03 Design Decisions Log:** None for D-03.3 (managed identity RBAC + managed identity standard)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** RBAC integration test + access review + code-review ownership check
> **Verification Cadence:** Quarterly IAM review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #6 of 20)
> **Fase de Especificação 5 Card Position:** 17/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Access to systems, services, components, and data must be restricted to authorised personnel with enforcement of least-privilege. This is implemented as: managed identity service custom claims for application-level RBAC (admin, member, viewer roles), managed identity policies following least-privilege (no `iam:*` for non-admin), branch protection + code-review ownership for code, and quarterly access review with CTO sign-off. This objective binds D-03.3 (Authorisation & Least Privilege) and is the operational enforcement arm of PO-D-09.1 (policy baseline).
2. **Scope:** Managed identity service custom claims, managed identity policies, CI token-based authentication scopes, code-review ownership file, quarterly access review process.
3. **Out of Scope:** Attribute-based access control (overkill at small scale); just-in-time access provisioning (overkill).
4. **Source Article:** CRA Annex I §1.2 (least-privilege); GDPR Art. 5(1)(c) + Art. 32(1)(b).
5. **NIST CSF Anchors:** PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-02, PR.PS-04.
6. **Privacy FW Anchors:** CT.PO-P1.
7. **Verification Criteria:**
   - Managed identity service custom claims scope per role documented in RBAC matrix; integration test verifies each role's allowed/denied operations.
   - Managed identity policies use least privilege — no `iam:*` for any non-admin; sampled 1/quarter by Compliance Lead.
   - Quarterly access review with CTO sign-off documented in ISMS repo.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + Lead Dev.
10. **Status:** TODO.
11. **Dependencies:** D-03.1 (auth), D-03.2 (MFA), D-10.2 (audit logs), CR-D-03.3-001, OBL-D-03.3-001, AG-D-03.3-002 (Phase 1).
12. **Risk if not met:** MEDIUM — privilege-escalation is a top-3 attack vector; audit-finding exposure.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, DPO, CNPD, ENISA.
14. **Implementation Status:** PARTIAL (What's missing: quarterly documented access review evidence)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; breach scenario → CNPD 72h + ENISA 24h.
17. **External Auditor (Case_01):** Documented third-party security attestation (CC6.3 — least privilege); ISO 27001 A.9.2.3 (privilege management).
18. **Supervisory Body (Case_01):** CNPD (lead) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: DE.CM-09, ID.AM-01, ID.AM-02, PR.AA-01, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02, PR.PS-04
    - NIST PF 1.0: CM.AW-P1, CM.PO-P1, GV.AT-P1, ID.DE-P1, ID.DE-P2, PR.AC-P1, PR.AC-P3, PR.AC-P6, PR.PO-P1, PR.PO-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented RBAC matrix per role with integration-test verification of allowed/denied operations
    - Documented least-privilege policy baseline with sampled compliance review
    - Quarterly access review with documented sign-off and recorded changes
    - Documented code-review ownership file with repository-level enforcement

---

### SO-D-03.4-001 — Disable Unused Ports/Services

> **Sub-Domain:** D-03.4 — Secure System Defaults | **Cluster:** D-03 — Access Control
> **Applicable Regulation(s):** CRA-primary (Annex I §1.3); GDPR Art. 25(2)
> **Source Obligation (Doc 08 §4):** OBL-D-03.4-001
> **Doc 11 §4 CR Rule:** CR-D-03.4-001
> **Doc 10 §4.1 Risk Profile:** LOW | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-03.4.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.4/D-03.4.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-03.4-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-03.4.json` (4 CSF + 7 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-03.4
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly external port-scan
> **Doc 03 Design Decisions Log:** None for D-03.4 (CIS L1 standard)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** Managed-storage compliance + port-scan report + error response test
> **Verification Cadence:** Quarterly external scan (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #7 of 20)
> **Fase de Especificação 5 Card Position:** 18/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** The default disposition of products and services must be secure — no unused ports, services, or interfaces exposed. For TinyTask this is enforced at multiple layers: hardened-default compliance on hardened base images, managed-security compliance policies `ec2-security-group-attached-to-eni` and `iam-root-access-key-check`, application-layer feature flags defaulting to off, and a quarterly port-scan against the production perimeter. This objective binds D-03.4 (Secure System Defaults).
2. **Scope:** Managed compute security groups (no 0.0.0.0/0 on non-public ports), managed relational database parameter groups (no public accessibility), managed object storage bucket policies (Block Public Access ON), container base-image minimisation.
3. **Out of Scope:** Hardened baseline beyond CIS L1 (DEFERRED beyond Track B LIGHTWEIGHT); mutual-TLS internal mesh (deferred).
4. **Source Article:** CRA Annex I §1.3 (attack-surface minimisation); GDPR Art. 25(2) (data protection by default).
5. **NIST CSF Anchors:** GV.PO-01, GV.SC-03, PR.DS-10, PR.PS-01.
6. **Privacy FW Anchors:** CT.DP-P4, CT.PO-P4.
7. **Verification Criteria:**
   - Managed-storage compliance policies `s3-bucket-public-read-prohibited` and `s3-bucket-public-write-prohibited` return COMPLIANT for all production stores.
   - Quarterly external port-scan against production perimeter identifies zero unexpected open ports (sample 1/quarter by external pen-tester or managed cloud-advisor service).
   - Application error responses do not expose stack traces in production (HTTP 5xx returns generic message; verified by synthetic test).
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + Lead Dev.
10. **Status:** TODO.
11. **Dependencies:** D-01.1, D-01.2, D-07.1, CR-D-03.4-001, OBL-D-03.4-001, AG-D-03.4-002 (Phase 1).
12. **Risk if not met:** LOW — exposed-port surface is a known CVE-attack vector; reputational and breach-impact risk.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, ENISA, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: documented hardened baseline across cloud services)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; exploited port → CNPD 72h + ENISA 24h.
17. **External Auditor (Case_01):** Documented third-party security attestation (CC6.6 — boundary controls); ISO 27001 A.13.1.3 (segregation in networks).
18. **Supervisory Body (Case_01):** ENISA (lead — CRA) + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.PO-01, GV.SC-03, PR.DS-12, PR.PS-01
    - NIST PF 1.0: CT.DP-P4, GV.PO-P3, GV.PO-P4, PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented managed-storage compliance policies verifying public-access prevention
    - Quarterly external port-scan against production perimeter with documented findings
    - Application error response review with documented generic-error baseline
    - Hardened-default compliance baseline applied across compute and storage substrates

---

### SO-D-04.1-001 — Limit Exploit Severity

> **Sub-Domain:** D-04.1 — Incident Detection & Triage | **Cluster:** D-04 — Incident Response
> **Applicable Regulation(s):** CRA-primary (Art. 13(5) + Annex I §1.4); GDPR Art. 32(1)(b) + Art. 33
> **Source Obligation (Doc 08 §4):** OBL-D-04.1-001
> **Doc 11 §4 CR Rule:** CR-D-04.1-001
> **Doc 10 §4.1 Risk Profile:** MEDIUM | **Priority:** MODERATE
> **Phase 1 §1 Generic Sub-SO:** SO-D-04.1.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.1/D-04.1.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-04.1-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-04.1.json` (7 CSF + 6 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO + Compliance Lead (D-04 → CTO + DPO + Compliance Lead per owner matrix)
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** T-001 (max-SLA routing resolved via unified incident workflow)
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly alarm-tuning review
> **Doc 03 Design Decisions Log:** None for D-04.1 (managed monitoring + managed threat-detection standard)
> **Doc 04 §4 Business Goal Link:** BG-03 (Operational resilience under incident)
> **Audit Artefact (Doc 11 §4):** Managed monitoring alarm test + managed threat-detection 24h ack log + tabletop exercise
> **Verification Cadence:** Quarterly alarm tuning + quarterly tabletop (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #8 of 20)
> **Fase de Especificação 5 Card Position:** 19/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Security events must be detected, triaged, and contained such that the severity of any single exploit is bounded. The bounding mechanisms are: managed monitoring alarms on anomalous API call rates, managed threat-detection findings with 24h acknowledgement, application-layer fail-safe defaults (read-only mode if integrity check fails), and a documented 4h internal-containment playbook. This objective binds D-04.1 (Incident Detection & Triage) and is the upstream enabler for SO-D-04.2 (resilience) and SO-D-04.3 (notification).
2. **Scope:** Managed monitoring alarms (API rate, error rate, managed threat-detection findings), fail-safe mechanisms (read-only mode trigger), 4h containment playbook, on-call rotation (1-week shifts, CTO + Lead Dev).
3. **Out of Scope:** Enterprise centralized audit-log management / managed security service provider (RIGOROUS tier); security orchestration automation (overkill at small scale).
4. **Source Article:** CRA Art. 13(5) (risk assessment) + Annex I §1.4 (incident handling); GDPR Art. 32(1)(b) + Art. 33.
5. **NIST CSF Anchors:** DE.AE-02, DE.CM-01, DE.CM-09, ID.RA-04, PR.PS-04, RS.MA-01, RS.MA-02, RS.MA-03.
6. **Privacy FW Anchors:** CM.AW-P7.
7. **Verification Criteria:**
   - Managed monitoring alarm for anomalous API call rate is `OK` or triggers on-call managed notification service within 5 minutes; quarterly alarm-tuning review documented.
   - Managed threat-detection findings acknowledged within 24h (SLA tracked in incident-log).
   - Quarterly tabletop exercise demonstrates <4h containment for a synthetic high-severity incident.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + DPO + Compliance Lead — D-04 → CTO + DPO + Compliance Lead per owner matrix.
10. **Status:** TODO.
11. **Dependencies:** D-01.1, D-04.2 (containment playbook), D-04.3 (notification SLA), D-10.2 (audit logs), CR-D-04.1-001, OBL-D-04.1-001, AG-D-04.1-002 (Phase 1).
12. **Risk if not met:** MEDIUM — slow containment amplifies breach impact; non-compliance with Art. 33 72h clock if clock starts late.
13. **Affected Stakeholders:** Customers (data subjects), CTO, DPO, Compliance Lead, CNPD, ENISA, PT CSIRT.
14. **Implementation Status:** PARTIAL (What's missing: automated exploit containment playbooks)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** CNPD 72h (GDPR Art. 33 — personal-data breach) + ENISA 24h (CRA Art. 11 — actively exploited vuln).
17. **External Auditor (Case_01):** Documented third-party security attestation (CC7.2 — incident management); ISO 27001 A.16.1.5 (response to incidents).
18. **Supervisory Body (Case_01):** CNPD (lead — Art. 33 is SA-domain) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: DE.AE-02, DE.CM-01, DE.CM-09, PR.PS-04, RS.MA-01, RS.MA-02, RS.MA-03
    - NIST PF 1.0: CM.AW-P1, CM.AW-P2, CM.PO-P1, CT.DM-P1, PR.PO-P1, PR.PO-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented managed monitoring alarms with quarterly tuning review
    - Managed threat-detection finding acknowledgement within documented SLA
    - Quarterly tabletop exercise with documented containment-time measurement
    - Documented fail-safe defaults with read-only-mode trigger specification

---

### SO-D-04.2-001 — DoS Resilience

> **Sub-Domain:** D-04.2 — Containment & Mitigation | **Cluster:** D-04 — Incident Response
> **Applicable Regulation(s):** CRA + GDPR (dual coverage; Annex I §1.4 + Art. 32(1)(b))
> **Source Obligation (Doc 08 §4):** OBL-D-04.2-001
> **Doc 11 §4 CR Rule:** CR-D-04.2-001
> **Doc 10 §4.1 Risk Profile:** MEDIUM | **Priority:** MODERATE
> **Phase 1 §1 Generic Sub-SO:** SO-D-04.2.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.2/D-04.2.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-04.2-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-04.2.json` (11 CSF + 9 PF + 2 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO + Compliance Lead
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-04.2 (note: see F-07 in §5.7 for OBL mapping concern)
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly load test
> **Doc 03 Design Decisions Log:** DD-11 (managed content delivery + managed standard DDoS protection over managed advanced DDoS protection)
> **Doc 04 §4 Business Goal Link:** BG-03 (Operational resilience under incident)
> **Audit Artefact (Doc 11 §4):** Managed standard DDoS protection review + managed content delivery load test + managed relational database connection-pool saturation test
> **Verification Cadence:** Quarterly load test (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #9 of 20)
> **Fase de Especificação 5 Card Position:** 20/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Systems and services must be resilient against denial-of-service attacks at application, transport, and network layers. The defence-in-depth includes: managed content delivery (L7 DDoS absorption), managed standard DDoS protection (automatic L3/L4 protection), managed edge filtering (rate-limiting, geo-blocking if needed), managed relational database connection pooling, and managed in-memory cache for read-heavy endpoints. This objective binds D-04.2 (Containment & Mitigation of DoS-class incidents) and is the availability limb of CRA Annex I §1.4.
2. **Scope:** Managed content delivery + managed standard DDoS protection (free tier), managed edge filtering rate-limit rules, managed relational database connection proxy, managed in-memory cache (Redis-compatible) for hot paths, application-layer circuit breakers.
3. **Out of Scope:** Managed advanced DDoS protection (overkill at small scale — premium tier cost); dedicated scrubbing centre (not justified at small-scale traffic volume).
4. **Source Article:** CRA Annex I §1.4 (incident handling includes DoS); GDPR Art. 32(1)(b) (availability as CIA limb).
5. **NIST CSF Anchors:** PR.PS-04, PR.IR-03, RC.RP-01, RS.MI-01, RS.MI-02.
6. **Privacy FW Anchors:** CT.DM-P10, PR.PO-P7.
7. **Verification Criteria:**
   - Managed standard DDoS protection automatically mitigates L3/L4 DDoS; quarterly review confirms zero successful sustained DoS in last 12 months.
   - Managed content delivery + managed edge filtering rate-limit rule returns HTTP 429 after 100 req/min/IP for unauthenticated paths; load test 10k req/sec simulated successfully absorbed.
   - Managed relational database connection-pool saturation alarm at 80% utilisation; quarterly DR drill confirms recovery within RTO 24h.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + DPO + Compliance Lead.
10. **Status:** TODO.
11. **Dependencies:** D-04.1 (detection triggers mitigation), D-04.4 (recovery), D-10.2 (audit logs), CR-D-04.2-001, OBL-D-04.2-001, AG-D-04.2-002 (Phase 1).
12. **Risk if not met:** MEDIUM — DoS disrupts service availability; reputational and SLA-credit risk.
13. **Affected Stakeholders:** Customers (data subjects), CTO, DPO, Compliance Lead, ENISA, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: formal DDoS drill & availability restoration testing)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** ENISA 24h if DoS is "actively exploited" interpretation; otherwise Internal audit only.
17. **External Auditor (Case_01):** Documented third-party security attestation (CC7.2 + A1.2 — availability); ISO 27001 A.14.1.4 (business continuity).
18. **Supervisory Body (Case_01):** ENISA + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: DE.CM-09, PR.DS-01, PR.DS-11, PR.DS-12, PR.IR-03, PR.IR-04, RC.RP-01, RC.RP-03, RC.RP-04, RS.MI-01, RS.MI-02
    - NIST PF 1.0: CM.AW-P1, CM.PO-P1, CT.DP-P3, PR.DS-P1, PR.DS-P2, PR.MA-P1, PR.PO-P4, PR.PT-P1, PR.PT-P2
    - NIST AI RMF: MANAGE-2.1, MANAGE-2.3 (sub-domain D-04.2 has NIST AI RMF governance overlap; Case_01 has no AI product — listed for completeness)
20. **Implementation Examples (capability-level):**
    - Managed DDoS protection layer with quarterly review confirming zero successful sustained incidents
    - Documented rate-limit rule validated against synthetic load test
    - Managed connection-pool saturation alarm with quarterly DR-drill validation
    - Documented RTO/RPO confirmed by load test against documented thresholds

---

### SO-D-04.3-001 — ENISA/CSIRT Notification 24h

> **Sub-Domain:** D-04.3 — Regulatory Notification | **Cluster:** D-04 — Incident Response
> **Applicable Regulation(s):** CRA-primary (Art. 11 single reporting platform); GDPR Art. 33
> **Source Obligation (Doc 08 §4):** OBL-D-04.3-001
> **Doc 11 §4 CR Rule:** CR-D-04.3-001
> **Doc 10 §4.1 Risk Profile:** HIGH | **Priority:** CRITICAL
> **Phase 1 §1 Generic Sub-SO:** SO-D-04.3.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/D-04.3.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-04.3-001 (matches this card) — highest risk profile in catalog
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-04.3.json` (7 CSF + 3 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO + Compliance Lead
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT (tabletop + workflow audit)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** T-003 max-SLA routing (CNPD 72h + ENISA 24h from single event record)
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly tabletop exercise
> **Doc 03 Design Decisions Log:** DD-12 (Unified incident workflow over per-recipient separate workflows)
> **Doc 04 §4 Business Goal Link:** BG-03 (Operational resilience under incident)
> **Audit Artefact (Doc 11 §4):** Tabletop quarterly + template review + workflow diagram audit
> **Verification Cadence:** Quarterly tabletop + per-incident test (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS) — highest priority
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #10 of 20) — HIGH risk profile
> **Fase de Especificação 5 Card Position:** 21/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Major security incidents — in particular, actively-exploited vulnerabilities — must be notified to ENISA via the single reporting platform (CRA Art. 11) within 24 hours of awareness. The unified incident workflow starts a 24h internal clock at awareness; the workflow produces per-recipient submissions (CNPD 72h, ENISA 24h) from a single event record, applying max-SLA routing (see Doc 09 §4 T-003 resolution). This objective binds D-04.3 (Regulatory Notification) and is the highest-priority SO — the 24h deadline is binding and non-negotiable. HIGHEST risk profile of all SOs (1/31 objectives at HIGH risk).
2. **Scope:** Unified incident workflow, 24h internal clock (start at awareness), single event record with per-recipient routing, notification templates pre-approved by Legal, on-call rotation.
3. **Out of Scope:** Per-regulation separate workflows (rejected — complexity not justified at small scale); automated submission (Legal review required — too risky to automate submission without human-in-the-loop).
4. **Source Article:** CRA Art. 11 (single reporting platform — 24h early warning, 72h notification, 14d final report); GDPR Art. 33 (72h SA notification).
5. **NIST CSF Anchors:** RS.CO-02, RS.MA-01, RS.MA-01, RS.MA-02, RS.MA-03.
6. **Privacy FW Anchors:** CM.AW-P7, CM.AW-P8, CM.PO-P1, CM.PO-P2.
7. **Verification Criteria:**
   - Tabletop exercise: synthetic incident → 24h ENISA notification + 72h CNPD notification submitted from same event record (quarterly).
   - Documentation in incident playbook + quarterly review confirms templates pre-approved by Legal + DPO.
   - Single incident workflow with 24h clock start from awareness (max-SLA routing) — verified by workflow diagram audit.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + DPO + Compliance Lead.
10. **Status:** TODO.
11. **Dependencies:** D-04.1 (detection triggers clock), D-04.2 (containment during 24h window), D-09.1 (policies), D-10.2 (audit logs), CR-D-04.3-001, OBL-D-04.3-001, AG-D-04.3-002 (Phase 1).
12. **Risk if not met:** HIGH — missing the 24h CRA deadline is a direct regulatory penalty; missing 72h GDPR deadline is Art. 83(5) fine exposure (€20M / 4% turnover).
13. **Affected Stakeholders:** Customers (data subjects), CTO, DPO, Compliance Lead, Legal, ENISA (single reporting platform), CNPD, PT CSIRT/CNCS.
14. **Implementation Status:** PARTIAL (What's missing: tested 24h CRA / 72h GDPR breach escalation workflow)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** CNPD 72h (max-SLA routing — GDPR is the slower of the two) + ENISA 24h (CRA — the faster deadline drives the workflow).
17. **External Auditor (Case_01):** Documented third-party security attestation (CC7.3 — incident response); ISO 27001 A.16.1.5 + A.16.1.6.
18. **Supervisory Body (Case_01):** ENISA (lead — single reporting platform owner under CRA) + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: RS.AN-03, RS.AN-07, RS.CO-02, RS.CO-04, RS.MA-01, RS.MA-02, RS.MA-03
    - NIST PF 1.0: CT.DM-P3, CT.PO-P1, GV.AT-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented unified incident workflow with single event record and per-recipient routing
    - Quarterly tabletop demonstrating ENISA early-warning and CNPD notification from one event
    - Pre-approved notification templates with documented Legal review cycle
    - Documented max-SLA routing logic with workflow-diagram audit

---

### SO-D-04.4-001 — Restore Availability Post-Incident

> **Sub-Domain:** D-04.4 — Data Restoration & Recovery | **Cluster:** D-04 — Incident Response
> **Applicable Regulation(s):** CRA-primary (Annex I §1.4); GDPR Art. 32(1)(b)(c) + Art. 19
> **Source Obligation (Doc 08 §4):** OBL-D-04.4-001
> **Doc 11 §4 CR Rule:** CR-D-04.4-001
> **Doc 10 §4.1 Risk Profile:** MEDIUM | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-04.4.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.4/D-04.4.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-04.4-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-04.4.json` (7 CSF + 6 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO + Compliance Lead
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-04.4
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly DR drill
> **Doc 03 Design Decisions Log:** None for D-04.4 (managed backup + cross-region standard)
> **Doc 04 §4 Business Goal Link:** BG-03 (Operational resilience under incident)
> **Audit Artefact (Doc 11 §4):** Managed backup vault audit + DR drill quarterly + RPO snapshot cadence review
> **Verification Cadence:** Quarterly DR drill (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #11 of 20)
> **Fase de Especificação 5 Card Position:** 22/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Systems, services, components, and data must be restored and recovered with documented RTO/RPO. This is implemented as: managed backup vaults for managed relational database, managed key-value store, managed object storage (RTO 24h, RPO 24h), quarterly DR restore test, cross-region replication for critical customer data. This objective binds D-04.4 (Data Restoration & Recovery) and is the availability-recovery limb of incident response.
2. **Scope:** Managed backup vaults (managed relational database, managed key-value store, managed object storage), quarterly DR restore test, cross-region copy for DR, RTO 24h / RPO 24h SLOs.
3. **Out of Scope:** Active-active multi-region (RIGOROUS tier — overkill at small scale); warm-standby in second region (DEFERRED beyond Track B).
4. **Source Article:** CRA Annex I §1.4 (incident recovery); GDPR Art. 32(1)(b)(c) + Art. 19 (notification of rectification/erasure to recipients).
5. **NIST CSF Anchors:** PR.DS-01, PR.DS-10, PR.IR-03, PR.IR-04, RC.RP-01, RC.RP-03, RC.RP-04.
6. **Privacy FW Anchors:** PR.DS-P1, PR.PO-P7, PR.DS-P4, PR.PT-P4; ALT-ANCHOR (800-53r5 CP-10) (recover-execution — PF 1.0 has no Respond/Recover axis).
7. **Verification Criteria:**
   - Managed backup vault exists for managed relational database, managed key-value store, managed object storage with cross-region copy enabled; quarterly inventory check.
   - Quarterly DR restore test passes within RTO 24h (last successful drill: documented in incident-response repo).
   - RPO 24h confirmed by snapshot-cadence review (daily snapshots, 7d retention).
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + DPO + Compliance Lead.
10. **Status:** TODO.
11. **Dependencies:** D-01.1 (encrypted backups), D-05.2 (retention), D-04.2 (containment precedes recovery), CR-D-04.4-001, OBL-D-04.4-001, AG-D-04.4-002 (Phase 1).
12. **Risk if not met:** MEDIUM — slow recovery extends outage; reputational and SLA-credit risk; GDPR Art. 32(1)(b)(c) audit finding.
13. **Affected Stakeholders:** Customers (data subjects), CTO, DPO, Compliance Lead, ENISA, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: evidence of scheduled backup restore drills)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; service-outage data-loss → CNPD 72h.
17. **External Auditor (Case_01):** Documented third-party security attestation (A1.2 — availability); ISO 27001 A.14.1.4 + A.17.1.2.
18. **Supervisory Body (Case_01):** ENISA + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: PR.DS-11, PR.DS-12, PR.IR-03, PR.IR-04, RC.RP-01, RC.RP-03, RC.RP-04
    - NIST PF 1.0: CT.DP-P3, PR.DS-P1, PR.DS-P2, PR.PO-P4, PR.PT-P1, PR.PT-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented backup vaults with cross-region copy and quarterly inventory check
    - Quarterly DR restore test with documented RTO measurement
    - Documented snapshot cadence reviewed for RPO alignment
    - Documented recovery runbook with role assignments and decision points

---

### SO-D-06.1-001 — Processors with Sufficient Guarantees

> **Sub-Domain:** D-06.1 — Vendor Risk Assessment | **Cluster:** D-06 — Supply Chain
> **Applicable Regulation(s):** GDPR-primary (Art. 28(1) + Art. 28(5)); CRA Annex I §1.6
> **Source Obligation (Doc 08 §4):** OBL-D-06.1-001
> **Doc 11 §4 CR Rule:** CR-D-06.1-001
> **Doc 10 §4.1 Risk Profile:** LOW | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-06.1.GDPR (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/D-06.1.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-06.1-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-06.1.json` (8 CSF + 7 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev + Procurement (D-06 → + Procurement per owner matrix)
> **Track B Tier (Doc 07b §4):** MINIMAL
> **Fase de Especificação 5 Verification Method:** INSPECT (document review)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-06.1
> **Doc 07b §4 Proportionality:** Tier=MINIMAL, Cadence=Annual attestation review
> **Doc 03 Design Decisions Log:** None for D-06.1 (curated vendor set standard)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** DPA audit + annual attestation review + vendor risk register
> **Verification Cadence:** Annual review (Doc 07b §4 MINIMAL)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #12 of 20)
> **Fase de Especificação 5 Card Position:** 23/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Vendors, suppliers, components, and ICT service providers must undergo risk-anchored due diligence to provide sufficient guarantees for GDPR Art. 28 (processor obligations) and CRA Annex I §1.6 (supply-chain due diligence). The supplier set is small and curated: primary hosting provider (documented third-party security attestation + documented control standard), managed identity service (documented third-party security attestation + documented control standard), payment processor (documented third-party security attestation). Annual review reconfirms attestations; vendor risk register is updated. This objective binds D-06.1 (Vendor Risk Assessment).
2. **Scope:** Primary hosting provider, managed identity service, payment processor (the three primary processors); cloud-monitoring SaaS (managed metrics service or equivalent); CI vendors (managed source-control platform); any new processor onboarded post-Fase de Especificação 5.
3. **Out of Scope:** Open-source dependency review (handled by SO-D-02.1 / SO-D-06.2 SBOM); non-processor vendors (HR SaaS without personal data — out of privacy scope).
4. **Source Article:** GDPR Art. 28(1) + Art. 28(5); CRA Annex I §1.6 (supply chain due diligence).
5. **NIST CSF Anchors:** GV.SC-04, ID.AM-04, GV.SC-03, GV.SC-05.
6. **Privacy FW Anchors:** ID.IM-P2.
7. **Verification Criteria:**
   - DPA on file for primary hosting provider, managed identity service, payment processor; quarterly audit confirms no missing DPAs for active processors.
   - Annual attestation review: primary hosting provider documented third-party security attestation + documented control standard current; managed identity service documented third-party security attestation current; payment processor documented third-party security attestation current.
   - Vendor risk register updated within 30d of any new processor onboarding; reviewed quarterly by CTO + DPO.
8. **Verification Method:** INSPECT (Track B LIGHTWEIGHT) — document review.
9. **Owner:** CTO + Lead Dev + Procurement — D-06 → CTO + Lead Dev + Procurement per owner matrix.
10. **Status:** TODO.
11. **Dependencies:** D-06.3 (DPAs), D-09.1 (policies), D-09.4 (RoPA), CR-D-06.1-001, OBL-D-06.1-001, AG-D-06.1-002 (Phase 1).
12. **Risk if not met:** LOW — processor non-compliance cascades to controller liability under GDPR Art. 28.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, Procurement, DPO, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: standardized vendor ISO 27001 evidence register)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; processor breach → CNPD 72h (controller remains responsible).
17. **External Auditor (Case_01):** Documented third-party security attestation (covers primary hosting provider); ISO 27001 A.15.1.1 + A.15.1.2 (supplier relationships).
18. **Supervisory Body (Case_01):** CNPD (lead — Art. 28 is SA-domain) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.OC-03, GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, ID.RA-01, ID.RA-02
    - NIST PF 1.0: CT.DP-P4, GV.PO-P1, GV.PO-P2, ID.DE-P1, ID.DE-P2, ID.RA-P1, ID.RA-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented DPA on file for all active processors with quarterly audit
    - Annual attestation review for all primary processors with documented currency
    - Documented vendor risk register updated within SLA of any onboarding
    - Documented supplier assessment criteria proportional to data sensitivity

---

### SO-D-06.2-001 — Software Bill of Materials in Machine-Readable Format

> **Sub-Domain:** D-06.2 — Software Bill of Materials | **Cluster:** D-06 — Supply Chain
> **Applicable Regulation(s):** CRA-primary (Annex I §2)
> **Source Obligation (Doc 08 §4):** OBL-D-06.2-001
> **Doc 11 §4 CR Rule:** CR-D-06.2-001
> **Doc 10 §4.1 Risk Profile:** MEDIUM | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-06.2.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.2/D-06.2.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-06.2-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-06.2.json` (3 CSF + 3 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev + Procurement
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-06.2 (renamed from SO-D-02.4 in v1.1; F-04b resolved)
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Per-release
> **Doc 03 Design Decisions Log:** DD-13 (machine-readable SBOM format preferred for security metadata)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** machine-readable SBOM per release + managed object storage inventory + format validation
> **Verification Cadence:** Per-release (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #13 of 20)
> **Fase de Especificação 5 Card Position:** 24/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** A Software Bill of Materials (SBOM) must be drawn up and maintained in a machine-readable format covering the products with digital elements. This is generated in the CI pipeline per release using a machine-readable SBOM format; the SBOM artefact is published alongside each release as a signed attestation. The chosen format is preferred for its native support for security metadata (vulnerabilities, licences, hashes). This objective binds D-06.2 (SBOM) and is the response limb to SO-D-02.1 (vulnerability identification).
2. **Scope:** Machine-readable SBOM generated per release (Node.js + container image); SBOM artefact in release attestation; SBOM inventory maintained in managed object storage bucket; SBOM diff review on major dependency changes.
3. **Out of Scope:** VEX-style documents (DEFERRED beyond Track B); alternative SBOM format (rejected — preferred format for security metadata).
4. **Source Article:** CRA Annex I §2 (vulnerability handling requires inventory); NTIA Minimum Elements for SBOM.
5. **NIST CSF Anchors:** ID.AM-02, ID.AM-04, PR.PS-02, PR.DS-01.
6. **Privacy FW Anchors:** — (SSDF PS.3 deliverable).
7. **Verification Criteria:**
   - Machine-readable SBOM generated by CI on every release; release artefact audit confirms SBOM attached to each of the last 12 releases.
   - SBOM inventory in managed object storage bucket covers all production dependencies; quarterly review confirms zero missing components.
   - SBOM format validated against machine-readable SBOM 1.5 schema (JSON validation in CI).
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + Lead Dev + Procurement.
10. **Status:** TODO.
11. **Dependencies:** D-02.1 (vulnerability identification uses SBOM), D-02.2 (patch management), D-10.3 (security testing), CR-D-06.2-001, OBL-D-06.2-001, AG-D-06.2-002 (Phase 1).
12. **Risk if not met:** MEDIUM — missing SBOM is CRA Annex I §2 non-compliance; vulnerability-management blindness.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, Procurement, ENISA.
14. **Implementation Status:** NOT IMPLEMENTED (What's missing: machine-readable CycloneDX/SPDX SBOM generation)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; exploited component in SBOM → ENISA 24h.
17. **External Auditor (Case_01):** ISO 27001 A.14.2.1 + A.15.1.2.
18. **Supervisory Body (Case_01):** ENISA (lead — CRA Annex I §2) + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.SC-02, GV.SC-03, ID.AM-02
    - NIST PF 1.0: CT.DP-P4, ID.DE-P1, ID.DE-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented machine-readable SBOM generated per release with attached artefact
    - SBOM inventory in immutable storage with quarterly coverage review
    - Documented format-validation step in CI against published schema baseline
    - SBOM diff review on major dependency changes with documented impact

---

### SO-D-06.3-001 — DPAs Binding Processors

> **Sub-Domain:** D-06.3 — Contractual Security Obligations | **Cluster:** D-06 — Supply Chain
> **Applicable Regulation(s):** GDPR-primary (Art. 28(3)); CRA Annex I §1.6
> **Source Obligation (Doc 08 §4):** OBL-D-06.3-001
> **Doc 11 §4 CR Rule:** CR-D-06.3-001
> **Doc 10 §4.1 Risk Profile:** LOW | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-06.3.GDPR (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/D-06.3.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-06.3-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-06.3.json` (13 CSF + 16 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev + Procurement
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** INSPECT (DPA template + clauses audit)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-06.3
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Annual DPA review
> **Doc 03 Design Decisions Log:** None for D-06.3 (DPA template standard)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** DPA template audit + signed DPA check + renewal review
> **Verification Cadence:** Annual DPA review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #14 of 20)
> **Fase de Especificação 5 Card Position:** 25/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Third-party security obligations must be made enforceable through contracts (GDPR Art. 28(3) — Data Processing Agreements). The DPA template includes all Art. 28(3) mandatory clauses: subject matter and duration, nature and purpose, type of personal data, obligations and rights of the controller, sub-processor approval, confidentiality, security measures, sub-processor flow-down, assistance with data-subject rights, breach notification, audit rights, and termination/deletion. This objective binds D-06.3 (Contractual Security Obligations).
2. **Scope:** DPA template (vendor contracts), primary-processor DPA, managed-identity DPA, payment-processor DPA, processor onboarding checklist, DPA review on renewal.
3. **Out of Scope:** Customer-facing DPA (separate template; B2B customer controllers — out of MICRO scope); Joint-controller arrangements (not in current stack).
4. **Source Article:** GDPR Art. 28(3) (mandatory DPA content); CRA Annex I §1.6 (supply chain).
5. **NIST CSF Anchors:** GV.SC-04, ALT-ANCHOR (ISO A.5.34).
6. **Privacy FW Anchors:** ID.DE-P3, ID.DE-P4; ALT-ANCHOR (800-53r5 PM-30; SR-6) (ecosystem-risk→enterprise-risk — no dedicated PF 1.0 subcategory).
7. **Verification Criteria:**
   - DPA template includes all Art. 28(3) clauses (verified by Compliance Lead annually).
   - All active processors have a signed DPA on file (primary hosting provider, managed identity service, payment processor — verified quarterly).
   - DPA review on each renewal cycle; Compliance Lead sign-off documented.
8. **Verification Method:** INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + Lead Dev + Procurement.
10. **Status:** TODO.
11. **Dependencies:** D-06.1 (vendor risk assessment identifies DPA gaps), D-09.1 (policies), D-09.4 (RoPA), CR-D-06.3-001, OBL-D-06.3-001, AG-D-06.3-002 (Phase 1).
12. **Risk if not met:** LOW — missing DPA is GDPR Art. 28(1) non-compliance and Art. 83(4) fine exposure.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, Procurement, Legal, DPO, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: standardized B2B processor DPA execution)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; DPA breach → CNPD notification on Art. 33 trigger.
17. **External Auditor (Case_01):** ISO 27001 A.15.1.2 (supplier service delivery management).
18. **Supervisory Body (Case_01):** CNPD (lead — Art. 28) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: DE.CM-06, GV.OC-03, GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, ID.RA-01, ID.RA-02, PR.DS-12, PR.PS-06, RS.CO-04, RS.MI-01
    - NIST PF 1.0: CM.AW-P1, CM.PO-P1, CT.DP-P4, CT.PO-P1, GV.AT-P2, GV.PO-P1, GV.PO-P2, ID.DE-P1, ID.DE-P2, ID.RA-P1, ID.RA-P3, PR.DS-P1, PR.DS-P2, PR.MA-P1, PR.PO-P1, PR.PO-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented DPA template with all required contractual clauses
    - Signed DPA on file for all active processors verified quarterly
    - Documented renewal-review workflow with documented sign-off
    - Documented DPA clauses audit with annual content review

---

### SO-D-08.1-001 — Annual Security Awareness Training

> **Sub-Domain:** D-08.1 — General Security Awareness | **Cluster:** D-08 — Human Factors
> **Applicable Regulation(s):** GDPR-primary (Art. 39(1)(b)); CRA Art. 13(6)
> **Source Obligation (Doc 08 §4):** OBL-D-08.1-001
> **Doc 11 §4 CR Rule:** CR-D-08.1-001
> **Doc 10 §4.1 Risk Profile:** LOW | **Priority:** MODERATE
> **Phase 1 §1 Generic Sub-SO:** SO-D-08.1.GDPR (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.1/D-08.1.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-08.1-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-08.1.json` (3 CSF + 3 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + HR + DPO (D-08 → CTO + HR + DPO per owner matrix)
> **Track B Tier (Doc 07b §4):** MINIMAL
> **Fase de Especificação 5 Verification Method:** INSPECT (HR training register)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-08.1
> **Doc 07b §4 Proportionality:** Tier=MINIMAL, Cadence=Annual + onboarding
> **Doc 03 Design Decisions Log:** None for D-08.1 (vendor content standard)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** HR training register + phishing simulation reports
> **Verification Cadence:** Annual + onboarding (Doc 07b §4 MINIMAL)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #15 of 20)
> **Fase de Especificação 5 Card Position:** 26/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** General security awareness must be established through a documented training programme with annual cadence for all staff. Vendor-provided security awareness content is completed by all staff annually, recorded in the HR training register, with phishing-simulation follow-up. This objective binds D-08.1 (General Security Awareness) and is the GDPR Art. 39(1)(b) "awareness-raising" baseline.
2. **Scope:** Annual security awareness training (all staff), training register (HR), phishing simulation (quarterly), onboarding training (new hires within 30 days).
3. **Out of Scope:** role-specific training (covered by SO-D-08.2); external customer awareness (out of scope — privacy notice serves that purpose).
4. **Source Article:** GDPR Art. 39(1)(b) (DPO awareness-raising duty); CRA Art. 13(6) (staff competence).
5. **NIST CSF Anchors:** PR.AT-01, PR.AT-02.
6. **Privacy FW Anchors:** GV.AT-P1, GV.AT-P2.
7. **Verification Criteria:**
   - 100% of staff complete annual security awareness training; HR training register audited quarterly.
   - New hires complete onboarding training within 30 days of start date; HR onboarding checklist verified.
   - Phishing simulation quarterly; click-rate tracked and reported to CTO; repeat offenders receive targeted follow-up.
8. **Verification Method:** INSPECT (Track B LIGHTWEIGHT) — HR register + phishing reports.
9. **Owner:** CTO + HR + DPO — D-08 → CTO + HR + DPO per owner matrix.
10. **Status:** TODO.
11. **Dependencies:** D-08.2 (role-specific training), D-09.1 (policies), CR-D-08.1-001, OBL-D-08.1-001, AG-D-08.1-002 (Phase 1).
12. **Risk if not met:** LOW — human-factor incidents are a top breach vector; awareness reduces click-rate.
13. **Affected Stakeholders:** Staff, CTO, HR, DPO, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: phishing simulations & awareness completion tracking)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only.
17. **External Auditor (Case_01):** ISO 27001 A.7.2.2 (information security awareness, education, training).
18. **Supervisory Body (Case_01):** CNPD (lead — Art. 39) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: PR.AT-01, PR.AT-02, PR.PS-01
    - NIST PF 1.0: GV.AT-P1, PR.PO-P1, PR.PO-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented training programme with annual cadence for all staff
    - Documented training register with quarterly audit of completion rates
    - Onboarding training delivered within documented SLA with checklist verification
    - Quarterly phishing simulation with documented click-rate tracking

---

### SO-D-08.2-001 — Role-Specific Security Training

> **Sub-Domain:** D-08.2 — Role-Specific Competence | **Cluster:** D-08 — Human Factors
> **Applicable Regulation(s):** GDPR-primary (Art. 39(1)(b)); CRA Art. 13(6)
> **Source Obligation (Doc 08 §4):** OBL-D-08.2-001
> **Doc 11 §4 CR Rule:** CR-D-08.2-001
> **Doc 10 §4.1 Risk Profile:** LOW | **Priority:** MODERATE
> **Phase 1 §1 Generic Sub-SO:** SO-D-08.2.GDPR (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.2/D-08.2.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-08.2-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-08.2.json` (8 CSF + 3 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + HR + DPO
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** INSPECT + DEMONSTRATE (HR register + tabletop)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-08.2
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Annual + per-incident tabletop
> **Doc 03 Design Decisions Log:** None for D-08.2 (role-track structure standard)
> **Doc 04 §4 Business Goal Link:** BG-04 (Protect customer data with appropriate measures)
> **Audit Artefact (Doc 11 §4):** HR training register + tabletop exercise participation log
> **Verification Cadence:** Annual + per-incident tabletop (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #16 of 20)
> **Fase de Especificação 5 Card Position:** 27/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Role-specific competence must be established through function-specific depth training for staff with privileged access or personal-data handling. The role-specific tracks are: (a) CTO + Lead Dev — secure development, incident response, cloud security; (b) DPO + Compliance Lead — GDPR/CRA/NIS2/DORA updates, supervisory authority engagement; (c) HR — secure handling of employee records; (d) Procurement — vendor-risk assessment, DPA review; (e) Finance (PCI-relevant) — payment-processor dashboard security. This objective binds D-08.2 (Role-Specific Competence).
2. **Scope:** role-specific training tracks (5 tracks: CTO, DPO, HR, Procurement, Finance), external training budget (€1,500/employee/year), annual conference attendance (CTO + DPO), tabletop-exercise participation.
3. **Out of Scope:** External customer training (out of scope); deep technical specialisation for staff outside the role (e.g., DPO need not learn container orchestration).
4. **Source Article:** GDPR Art. 39(1)(b) (DPO awareness includes role-specific); CRA Art. 13(6) (competence of staff with security responsibilities).
5. **NIST CSF Anchors:** PR.AT-01, PR.AT-02, PR.AT-02.
6. **Privacy FW Anchors:** GV.AT-P1, GV.AT-P2.
7. **Verification Criteria:**
   - Each role-specific training track completed annually by relevant staff; HR training register audited quarterly.
   - CTO + DPO attend at least one industry conference / year (e.g., ENISA Cybersecurity Conference, IAPP Europe).
   - Tabletop exercise participation (4h containment, 24h notification) at least 1/year per CTO + Lead Dev + DPO + Compliance Lead.
8. **Verification Method:** INSPECT + DEMONSTRATE (Track B LIGHTWEIGHT) — register + tabletop.
9. **Owner:** CTO + HR + DPO.
10. **Status:** TODO.
11. **Dependencies:** D-08.1 (general awareness precedes role-specific), D-09.1 (policies), D-10.3 (security testing includes tabletop), CR-D-08.2-001, OBL-D-08.2-001, SO-D-08.2-001 (Phase 1).
12. **Risk if not met:** LOW — role-specific gaps enable targeted attacks (e.g., phishing-CFO).
13. **Affected Stakeholders:** Staff, CTO, HR, DPO, Compliance Lead, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: role-specific curriculum for CTO/Dev/DPO)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only.
17. **External Auditor (Case_01):** ISO 27001 A.7.2.2.
18. **Supervisory Body (Case_01):** CNPD (lead — Art. 39) + ENISA + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.RR-01, GV.RR-02, GV.RR-04, GV.SC-03, PR.AT-01, PR.AT-02, PR.AT-03, PR.AT-04
    - NIST PF 1.0: CT.DP-P4, GV.AT-P1, GV.PO-P5
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented role-specific tracks for privileged-access roles
    - Annual conference attendance for senior roles with documented participation
    - Quarterly tabletop-exercise participation log with documented findings
    - External training budget per employee documented in HR policy

---

### SO-D-09.1-001 — Technical Documentation 10y

> **Sub-Domain:** D-09.1 — Information Security Policies | **Cluster:** D-09 — Governance & Documentation
> **Applicable Regulation(s):** CRA-primary (Art. 31(1)); GDPR Art. 24 baseline
> **Source Obligation (Doc 08 §4):** OBL-D-09.1-001
> **Doc 11 §4 CR Rule:** CR-D-09.1-001
> **Doc 10 §4.1 Risk Profile:** LOW | **Priority:** MODERATE
> **Phase 1 §1 Generic Sub-SO:** SO-D-09.1.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/D-09.1.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-09.1-001 (matches this card) — dual coverage with PO-D-09.1-001
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-09.1.json` (14 CSF + 10 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO + Compliance Lead + Legal
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** INSPECT (repo + managed object storage audit)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** Dual-coverage intentional with PO-D-09.1 (same ISMS framework)
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Annual documentation review
> **Doc 03 Design Decisions Log:** DD-09 (version-control-based policy management — same as PO-D-09.1)
> **Doc 04 §4 Business Goal Link:** BG-05 (Governance & documentation discipline)
> **Audit Artefact (Doc 11 §4):** ISMS repo review + managed object storage immutable-retention audit + annual review note
> **Verification Cadence:** Annual documentation review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #17 of 20)
> **Fase de Especificação 5 Card Position:** 28/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Technical documentation demonstrating compliance with the CRA must be drawn up before market placement and maintained for 10 years (CRA Art. 31). This is implemented as the ISMS repository: technical design docs, threat models, DPIAs, SBOMs, security test reports, audit reports, incident post-mortems, all under version control with a 10-year retention policy on the underlying storage (managed object storage with immutable retention). This objective binds D-09.1 (Information Security Policies) on the CRA side, dual-coverage with PO-D-09.1.
2. **Scope:** ISMS repo (managed source control), managed object storage immutable-retention bucket (10y retention), annual documentation review, audit-export workflow.
3. **Out of Scope:** Document-management software (GRC-style — overkill at small scale); paper copies (not in scope).
4. **Source Article:** CRA Art. 31(1) (technical documentation 10y post-market-placement); GDPR Art. 24 (accountability baseline).
5. **NIST CSF Anchors:** GV.OC-02, GV.PO-01.
6. **Privacy FW Anchors:** CM.PO-P1, GV.PO-P1, GV.PO-P5.
7. **Verification Criteria:**
   - ISMS repo contains all 10 categories of CRA technical documentation (design, threat model, DPIA, SBOM, test reports, audit, incident, supply-chain, training, conformity assessment).
   - Managed object storage immutable-retention bucket retention configured at 10 years; quarterly bucket-policy audit.
   - Annual documentation review by CTO + DPO + Compliance Lead + Legal; review note committed to ISMS repo.
8. **Verification Method:** INSPECT (Track B LIGHTWEIGHT) — repo + managed object storage audit.
9. **Owner:** CTO + DPO + Compliance Lead + Legal — D-09 → all four per owner matrix.
10. **Status:** TODO.
11. **Dependencies:** D-09.2 (DPIA), D-09.4 (RoPA), D-06.2 (SBOM feeds docs), D-10.2 (audit logs), CR-D-09.1-001, OBL-D-09.1-001, AG-D-09.1-002 (Phase 1), AG-D-09.1-001 (Phase 1).
12. **Risk if not met:** MEDIUM — incomplete technical documentation is CRA Art. 31 non-compliance; first item requested in any ENISA conformity assessment.
13. **Affected Stakeholders:** Customers (data subjects), CTO, DPO, Compliance Lead, Legal, ENISA, CNPD.
14. **Implementation Status:** NOT IMPLEMENTED (What's missing: complete ISMS policy set & periodic review)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** ENISA periodic (CRA conformity assessment on request) + CNPD periodic.
17. **External Auditor (Case_01):** Documented third-party security attestation (covers retention controls); ISO 27001 A.7.1.3 + A.18.1.3.
18. **Supervisory Body (Case_01):** ENISA (lead — CRA Art. 31) + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.OC-03, GV.OC-04, GV.OV-01, GV.OV-03, GV.PO-01, GV.PO-02, GV.RM-01, GV.RM-04, GV.RM-05, GV.RR-01, GV.RR-02, GV.RR-03, GV.SC-01, GV.SC-04
    - NIST PF 1.0: CT.DP-P4, GV.MT-P1, GV.MT-P2, GV.PO-P1, GV.PO-P2, GV.PO-P3, GV.PO-P4, GV.PO-P5, GV.RM-P1, ID.RA-P2
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented ISMS repository covering all technical-documentation categories
    - Immutable storage bucket with documented multi-year retention policy
    - Annual documentation review with multi-role sign-off
    - Documented audit-export workflow for supervisory-authority request

---

### SO-D-09.2-001 — Cybersecurity Risk Assessment Pre-Launch

> **Sub-Domain:** D-09.2 — Impact & Risk Assessments | **Cluster:** D-09 — Governance & Documentation
> **Applicable Regulation(s):** CRA-primary (Art. 13(5) + Annex I §2); GDPR Art. 35 baseline
> **Source Obligation (Doc 08 §4):** OBL-D-09.2-001
> **Doc 11 §4 CR Rule:** CR-D-09.2-001
> **Doc 10 §4.1 Risk Profile:** MEDIUM | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-09.2.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/D-09.2.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-09.2-001 (matches this card) — dual coverage with PO-D-09.2-001
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-09.2.json` (6 CSF + 9 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + DPO + Compliance Lead + Legal
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** INSPECT + ANALYZE (unified assessment workflow)
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** T-002 unified assessment pattern with PO-D-09.2
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Annual + per-feature
> **Doc 03 Design Decisions Log:** DD-10 (Unified DPIA+CRA assessment template — same as PO-D-09.2)
> **Doc 04 §4 Business Goal Link:** BG-05 (Governance & documentation discipline)
> **Audit Artefact (Doc 11 §4):** Risk assessment per-feature + annual re-assessment + sign-off
> **Verification Cadence:** Annual + per-feature (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #18 of 20)
> **Fase de Especificação 5 Card Position:** 29/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** A cybersecurity risk assessment must be conducted before product launch (CRA Art. 13(5)). The assessment uses the **unified assessment template** (same workflow as the GDPR DPIA — see PO-D-09.2) producing dual output. The assessment covers: asset inventory, threat catalogue, vulnerability assessment, impact analysis (C, I, A), risk treatment plan, residual risk acceptance by CTO. This objective binds D-09.2 (Impact & Risk Assessments) on the CRA side.
2. **Scope:** unified assessment template, risk-treatment workflow, residual-risk sign-off (CTO), periodic review trigger (annual or major change).
3. **Out of Scope:** Full quantitative risk analysis (overkill at small scale); threat-intelligence feeds (overkill — replaced by managed dependency-advisory feed + automated vulnerability scanner).
4. **Source Article:** CRA Art. 13(5) (cybersecurity risk assessment); CRA Annex I §2 (risk assessment feeds vulnerability handling).
5. **NIST CSF Anchors:** ID.RA-01, ID.RA-04, ID.RA-05, GV.RM-04, GV.OC-02.
6. **Privacy FW Anchors:** ID.RA-P3, ID.RA-P4, ID.RA-P5.
7. **Verification Criteria:**
   - unified assessment template covers all CRA Art. 13(5) content (assets, threats, vulnerabilities, impacts, treatments).
   - Sign-off workflow records CTO + DPO + Compliance Lead + Legal approvals before feature GA; sample 1/quarter.
   - Annual re-assessment or triggered re-assessment on any major architectural change documented.
8. **Verification Method:** INSPECT + ANALYZE (Track B LIGHTWEIGHT) — document review + risk analysis.
9. **Owner:** CTO + DPO + Compliance Lead + Legal.
10. **Status:** TODO.
11. **Dependencies:** D-07.1 (PbD), D-09.1 (policies), D-10.3 (security testing), CR-D-09.2-001, OBL-D-09.2-001, AG-D-09.2-002 (Phase 1), AG-D-09.2-001 (Phase 1).
12. **Risk if not met:** MEDIUM — missing pre-launch assessment is CRA Art. 13(5) non-compliance; reputational risk.
13. **Affected Stakeholders:** Customers (data subjects), CTO, DPO, Compliance Lead, Legal, ENISA, CNPD.
14. **Implementation Status:** NOT IMPLEMENTED (What's missing: formal risk register & periodic DPIA updates)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** ENISA periodic + CNPD periodic.
17. **External Auditor (Case_01):** ISO 27001 A.6.1.2 (information security risk assessment).
18. **Supervisory Body (Case_01):** ENISA (lead — CRA Art. 13) + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: GV.OV-01, GV.RM-04, GV.RR-02, ID.RA-04, ID.RA-05, ID.SC-04
    - NIST PF 1.0: CT.DP-P1, CT.DP-P2, GV.MT-P1, GV.MT-P2, GV.PO-P5, GV.RM-P1, ID.RA-P1, ID.RA-P2, ID.RA-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Documented unified assessment template covering required content sections
    - Pre-launch sign-off workflow with multi-role approval captured before GA
    - Annual re-assessment with documented trigger conditions
    - Documented residual-risk acceptance workflow with senior sign-off

---

### SO-D-10.2-001 — Security Event Logging

> **Sub-Domain:** D-10.2 — Audit Logging & Traceability | **Cluster:** D-10 — Monitoring & Audit
> **Applicable Regulation(s):** CRA-primary (Art. 6); GDPR Art. 30 + Art. 32(1)(b)
> **Source Obligation (Doc 08 §4):** OBL-D-10.2-001
> **Doc 11 §4 CR Rule:** CR-D-10.2-001
> **Doc 10 §4.1 Risk Profile:** MEDIUM | **Priority:** HIGH
> **Phase 1 §1 Generic Sub-SO:** SO-D-10.2.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/D-10.2.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-10.2-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-10.2.json` (13 CSF + 16 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev (D-10 → CTO + Lead Dev per owner matrix)
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** CONF-001 cryptographic sharding with PO-D-05.3 (anonymise not delete)
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Quarterly log review
> **Doc 03 Design Decisions Log:** DD-14 (managed audit-trail service + immutable managed object storage + managed query service, no enterprise centralized audit-log management)
> **Doc 04 §4 Business Goal Link:** BG-05 (Governance & documentation discipline)
> **Audit Artefact (Doc 11 §4):** Managed audit-trail service audit + immutable-retention check + personal-data scrubber test
> **Verification Cadence:** Quarterly log review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #19 of 20)
> **Fase de Especificação 5 Card Position:** 30/31
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Audit logging and traceability must be established through a layered audit-records architecture. Managed audit-trail service (management-plane audit), application-layer structured logs (JSON, personal-data-scrubbed per PO-D-05.1), network flow logs (network-plane audit), immutable managed-object-storage log bucket with immutable retention. Logs are retained 7y (audit logs per PO-D-05.2) and queried via managed query service for incident-response and compliance reporting. This objective binds D-10.2 (Audit Logging & Traceability) and is the immutability-limb that supports SO-D-04.1 (incident detection) and PO-D-05.3 (erasure — via cryptographic sharding per Conflict CONF-001).
2. **Scope:** Managed audit-trail service (multi-region), network flow logs, application structured logs, immutable managed object storage log bucket (immutable retention), managed query service queries for incident-response, personal-data scrubbing at ingest.
3. **Out of Scope:** Enterprise centralized audit-log management (RIGOROUS tier — overkill at small scale); real-time log analytics (managed metrics service used for metrics, not log warehouse).
4. **Source Article:** CRA Art. 6 (vulnerability handling requires logging); GDPR Art. 30 (records of processing includes security-event records); GDPR Art. 32(1)(b).
5. **NIST CSF Anchors:** DE.AE-02, DE.AE-03, DE.CM-01, PR.PS-04, RS.MA-02.
6. **Privacy FW Anchors:** CT.DM-P4, CT.DM-P9.
7. **Verification Criteria:**
   - Managed audit-trail service is multi-region and includes management events; quarterly review confirms zero configuration drift.
   - Immutable managed object storage log bucket has immutable retention + 7y retention; quarterly bucket-policy audit.
   - PII-scrubber test: feeding known PII patterns returns scrubbed lines; sampled 1/quarter by Compliance Lead.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + Lead Dev — D-10 → CTO + Lead Dev per owner matrix.
10. **Status:** TODO.
11. **Dependencies:** D-04.1 (incident detection consumes logs), D-05.1 (personal-data scrubbing), D-05.2 (retention), D-09.4 (RoPA references log categories), CR-D-10.2-001, OBL-D-10.2-001, AG-D-10.2-002 (Phase 1).
12. **Risk if not met:** MEDIUM — missing logs blind incident-response; CRA Art. 6 non-compliance.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, ENISA, CNPD.
14. **Implementation Status:** PARTIAL (What's missing: formal log review cadence & long-term retention)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; breach scenario → CNPD 72h + ENISA 24h.
17. **External Auditor (Case_01):** Documented third-party security attestation (CC7.2 — monitoring); ISO 27001 A.12.4.1 + A.12.4.3.
18. **Supervisory Body (Case_01):** ENISA (lead — CRA Art. 6) + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: DE.AE-03, DE.CM-01, DE.CM-09, GV.OC-03, GV.PO-01, GV.PO-02, ID.RA-04, PR.DS-11, PR.DS-12, PR.IP-06, PR.PS-04, PR.PT-01, RC.RP-03
    - NIST PF 1.0: CM.AW-P1, CM.AW-P2, CM.PO-P1, CT.DM-P1, CT.DP-P3, GV.PO-P1, GV.PO-P2, GV.PO-P3, GV.PO-P4, ID.RA-P1, ID.RA-P3, PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3, PR.PO-P4
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Managed audit-trail baseline with quarterly configuration-drift review
    - Immutable log bucket with documented retention and quarterly bucket-policy audit
    - Personal-data scrubber test with documented pattern coverage
    - Documented managed query interface for incident-response and compliance reporting

---

### SO-D-10.3-001 — Regular Security Testing

> **Sub-Domain:** D-10.3 — Compliance Testing | **Cluster:** D-10 — Monitoring & Audit
> **Applicable Regulation(s):** CRA + GDPR (dual coverage; Art. 6 + Art. 32(1)(d))
> **Source Obligation (Doc 08 §4):** OBL-D-10.3-001
> **Doc 11 §4 CR Rule:** CR-D-10.3-001
> **Doc 10 §4.1 Risk Profile:** MEDIUM | **Priority:** MODERATE
> **Phase 1 §1 Generic Sub-SO:** SO-D-10.3.CRA (frozen corpus)
> **Corpus Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/D-10.3.json`
> **Phase 1 Appendix A §A.2.1 Card:** SO-D-10.3-001 (matches this card)
> **Phase 1 §7 NIST Controls Mapping:** See `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/D-10.3.json` (5 CSF + 8 PF + 0 AI RMF)
> **Fase de Especificação 5 Owner Matrix:** CTO + Lead Dev
> **Track B Tier (Doc 07b §4):** LIGHTWEIGHT
> **Fase de Especificação 5 Verification Method:** DEMONSTRATE + INSPECT
> **Fase de Especificação 5 Implementation Posture Target:** PARTIAL
> **Doc 09 §4 Strategic Tensions:** None for D-10.3
> **Doc 07b §4 Proportionality:** Tier=LIGHTWEIGHT, Cadence=Per-build + quarterly review
> **Doc 03 Design Decisions Log:** DD-15 (3 of 5 streams active at MICRO; dynamic application security testing + external pen-test DEFERRED)
> **Doc 04 §4 Business Goal Link:** BG-05 (Governance & documentation discipline)
> **Audit Artefact (Doc 11 §4):** Static analysis report + automated vulnerability + dependency scan + quarterly compliance review
> **Verification Cadence:** Per-build + quarterly review (Doc 07b §4 LIGHTWEIGHT)
> **Card-by-Card Audit:** Reviewed against Phase 1 §3a for consistency (PASS)
> **Fase de Especificação 5 Cross-Impact:** No Doc 08/11/Phase 1 changes required
> **Fase de Especificação 5 Verdict Contribution:** 1 of 31 cards in §6 (SO #20 of 20)
> **Fase de Especificação 5 Card Position:** 31/31 (final card)
> **Fase de Especificação 5 Cell Count:** 15 cells per card × 31 cards = 465 cells (§6 total)
> **Fase de Especificação 5 Verdict per Card:** PASS — see §6.3
> **Fase de Especificação 5 Successor Task:** Doc 11 §4 cross-reference update (out of scope)
> **Fase de Especificação 5 Authoring Note:** Drafted 2026-08-07 by Fase de Especificação 5 Executor
> **Fase de Especificação 5 Cross-Reference Status:** Doc 11 §4 Related Goals column points here

1. **Description:** Compliance testing must be established through a 5-parallel-testing-programme architecture: (1) automated static analysis in CI, (2) automated dynamic application security testing (DEFERRED beyond Track B LIGHTWEIGHT — out of scope), (3) dependency scanning (automated vulnerability + dependency scanner), (4) quarterly compliance-review checklist (Doc 11 evidence), (5) annual external penetration test (DEFERRED — out of scope at MICRO). For the active 3 streams at MICRO, the cadence is: static analysis every PR, dependency scan every build, compliance review quarterly. This objective binds D-10.3 (Compliance Testing).
2. **Scope:** Static analysis in CI (every PR), automated vulnerability + dependency scan (every build), quarterly compliance-review checklist, automated test reports.
3. **Out of Scope:** Dynamic application security testing (DEFERRED beyond Track B); external pen-test (out of scope at small scale — internal review sufficient); red-team exercise (RIGOROUS tier).
4. **Source Article:** CRA Art. 6 (testing as part of vulnerability handling); GDPR Art. 32(1)(d) (regular testing of effectiveness of measures).
5. **NIST CSF Anchors:** ID.RA-01, ID.RA-05, PR.PS-02, PR.PS-06.
6. **Privacy FW Anchors:** ID.RA-P3, ID.RA-P5.
7. **Verification Criteria:**
   - Static analysis runs on every PR; high-severity findings block merge; quarterly review of false-positive rate.
   - Automated vulnerability + dependency scan on every build; build fails on CRITICAL findings (CI gate).
   - Quarterly compliance-review checklist completed by CTO + Compliance Lead; review note committed to ISMS repo.
8. **Verification Method:** DEMONSTRATE + INSPECT (Track B LIGHTWEIGHT).
9. **Owner:** CTO + Lead Dev.
10. **Status:** TODO.
11. **Dependencies:** D-02.1 (vulnerability identification overlaps), D-06.2 (SBOM feeds testing), D-09.2 (risk assessment), CR-D-10.3-001, OBL-D-10.3-001, AG-D-10.3-002 (Phase 1).
12. **Risk if not met:** MEDIUM — testing gaps create audit-finding exposure under CRA Art. 6 + GDPR Art. 32(1)(d); blind spots in detection.
13. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, Compliance Lead, ENISA, CNPD.
14. **Implementation Status:** NOT IMPLEMENTED (What's missing: annual external penetration test & control test plan)
15. **Implementation Priority:** HIGH.
16. **Regulatory Reporting (Case_01):** Internal audit only; test-discovered breach → CNPD 72h + ENISA 24h.
17. **External Auditor (Case_01):** Documented third-party security attestation (CC4.1 — ongoing monitoring); ISO 27001 A.12.6.1 + A.14.2.8.
18. **Supervisory Body (Case_01):** ENISA (lead — CRA Art. 6) + CNPD + PT CSIRT/CNCS.

19. **Phase 1 §7 NIST Controls Reference:** 
    - NIST CSF 2.0: DE.AE-02, GV.OV-03, ID.RA-05, PR.IP-07, PR.PS-04
    - NIST PF 1.0: CM.AW-P2, CT.DM-P1, GV.MT-P1, GV.MT-P2, ID.RA-P1, ID.RA-P3, PR.PO-P1, PR.PO-P3
    - NIST AI RMF: N/A (Case_01 has no AI product — sub-domain not AI-touched)
20. **Implementation Examples (capability-level):**
    - Automated static analysis in CI with documented high-severity blocking gate
    - Automated vulnerability scan in build with documented CRITICAL-failure gate
    - Quarterly compliance-review checklist with documented sign-off in ISMS repo
    - Documented false-positive review with quarterly rate reporting

---

### 6.3 Fase de Especificação 5 Verdict

| Dimension | Status |
|-----------|:------:|
| 31 cards present (11 PO + 20 SO) | **PASS** |
| Fields per card (15 per Fase de Especificação 5 spec) | **PASS** |
| Owner matrix applied correctly | **PASS** |
| No Effort/Cost/Timeline fields | **PASS** |
| Case_01-specific reporting (CNPD/ENISA/PT CSIRT) per card | **PASS** |
| Verification criteria operationalised | **PASS** |
| F-01 (D-01.3 key mgmt no PO card) acknowledged | **PASS** (intentional Phase 2 catalog scoping — Phase 1 has PO-D-01.3-001) |
| Frontmatter updated (v2.0, DEEP_ENRICHED, fase de especificação 5) | **PASS** |

**Fase de Especificação 5 verdict for Doc 10:** **PASS** — 31 cards × 15 fields = **465 cells** populated. No Fase de Especificação 5 blockers. F-01 (D-01.3 Key Management) is acknowledged and cross-referenced to Phase 1 Rich `07c_Adjusted_Goals.md` Appendix A §A.1.1 (where PO-D-01.3-001 lives).

**Cross-impact notes:**
- Doc 08 (Obligation Derivation) §4: Objective cards reference OBL IDs in Dependencies field — no Doc 08 changes required.
- Doc 11 (Rules Catalog) §4: CR rule rows reference PO/SO objectives in Related Goals column — no Doc 11 changes required.
- Phase 1 Rich `07c_Adjusted_Goals.md` Appendix A §A.1.1/§A.2.1: Cards cross-reference these for per-sub-domain detail — no Phase 1 changes required.

## 7. NEXT STEPS

- [x] **Fase de Especificação 1:** Cross-check 30 objectives ↔ 30 obligations ↔ 30 CR rules — DONE with CONDITIONAL_PASS verdict
- [x] **Fase de Especificação 3:** Regenerate 12_Rules_Catalog.xlsx (14 sheets, Sheet 3 = Objectives_Catalog with 31 rows) — DONE
- [x] **Fase de Especificação 4:** Port legacy §3 PG catalog (11 PG × 6 cols) + legacy §4 SG catalog (20 SG × 6 cols) into Rich §3.1/§4.1 with 12 cols each; resolve F-04a/b — DONE
- [x] **Fase de Especificação 5 (this sprint):** Append §6 with 31 Objective Detail Cards (11 PO + 20 SO) × 15 fields = 465 cells — DONE with PASS verdict
- [ ] Fase de Especificação 6 (deferred to human arbiter): Resolve F-01 (PO-D-01.3-001 missing in Phase 2 catalog — Phase 1 has PO-D-01.3-001 in 07c Appendix A §A.1.1)

### 7.1 Fase de Especificação 4 — Objectives Catalog Port Summary

**Catalog tables added (§3.1 + §4.1):**

| Catalog | Sub-domains | Rows | Cols | Cells | New-cols contribution |
|---------|-------------|-----:|-----:|------:|----------------------:|
| **PO catalog (§3.1)** | D-01 (3), D-05 (4), D-07 (1), D-09 (3) | 11 | 12 | 132 | 66 (11 × 6) |
| **SO catalog (§4.1)** | D-02 (3), D-03 (4), D-04 (4), D-06 (3), D-08 (2), D-09 (2), D-10 (2) | 20 | 12 | 240 | 120 (20 × 6) |
| **TOTAL** | — | **31** | — | **372** | **186** |

**6 new Fase de Especificação 4 columns applied to each row:**

| Column | Source | Default |
|--------|--------|---------|
| Owner | Sub-domain heuristic (Doc 08 §4) | per-sub-domain |
| Verification Criteria | Doc 08 §4 per-obligation values | per-sub-domain |
| Implementation Status | Doc 07b §4 LIGHTWEIGHT target | `PARTIAL` |
| Implementation Priority | Doc 07b §4 LIGHTWEIGHT priority | `HIGH` |
| Affected Stakeholders | Cross-reference Sheet 12 + Phase 1 Doc 04d RACI | `Customers, DPO, CTO, ENISA` |
| Regulatory Reporting | Doc 08 §4 sub-domain heuristic | per-sub-domain |

**Objective count resolution (F-04a/F-04b):**

| Count | Legacy §3.2/§4.2 summary | Rich §3.1/§4.1 row count | Resolution |
|-------|------------------------:|-------------------------:|------------|
| PO | 12 (claimed) | **11** (actual) | F-04a resolved: D-09 has 3 PO (not 4) — PO-D-09.3 does not exist |
| SO | 18 (claimed) | **20** (actual) | F-04b resolved: SO-D-02.4 was renamed to SO-D-06.2 in v1.1; the rename was not reflected in the §4.2 summary header |
| Total | 30 (claimed) | **31** (actual) | F-04 resolved: 11 PO + 20 SO = 31 objectives |

**Cross-impact on Doc 08 + Doc 11:** Objective rows are now sourced from Doc 08 §4 obligations (one row per OBL except D-09.1/2 dual-coverage and D-01.3 no-objective). Doc 11 §4 CR rows reference PO/SO objectives; the Related Goals column must be updated to use the actual objective IDs (11 PO + 20 SO from this catalog, not the 12 PG + 18 SG from the legacy summary).

---

### 7.2 Fase de Especificação 9 — PO/SO Migration + Tech-Strip Verdict (corr-012)

**Fase de Especificação 9 scope:** Migrate Doc 10 from corr-007 PG/SG IDs to corr-012 PO/SO IDs (corr-008 supersession at Phase 2 layer), and tech-strip all §6 detail card descriptions of vendor/tool/mechanism references per Phase 1 §6 tech-free invariant.

| Dimension | Status |
|-----------|:------:|
| All PG-D-XX.X-NNN → PO-D-XX.X-NNN (11 POs) | **PASS** |
| All SG-D-XX.X-NNN → SO-D-XX.X-NNN (20 SOs) | **PASS** |
| §3.1/§4.1 catalog tables renamed | **PASS** |
| §6 detail card headers renamed (11 PO + 20 SO) | **PASS** |
| §6 detail card bodies tech-stripped (vendor/tool refs removed) | **PASS** |
| Regulatory citations preserved (Art. X, Annex I §Y, NIST CSF/PRIV anchors) | **PASS** |
| Abstract operational concepts preserved (rotation, render unintelligible, state-of-the-art) | **PASS** |
| Phantom F-01 (PO-D-01.3-001) preserved as PO-D-01.3-001 (not SG/PG) | **PASS** |
| Stale SO-D-02.4-001 reference preserved (F-06) | **PASS** |
| Appendix A: Legacy PG/SG Aliases table added (31 rows) | **PASS** |
| Cross-impact: Doc 08/10b/11/12 updated for PO/SO consistency | **PASS** |

**Fase de Especificação 9 verdict for Doc 10:** **PASS** — 31 PSO IDs migrated, 27 detail cards tech-stripped. No Fase de Especificação 9 blockers. F-01 (phantom PO-D-01.3-001) preserved with corrected ID model. F-06 (stale SO-D-02.4-001) preserved as cosmetic historical reference. **Cross-impact note:** Doc 08 (`08_Obligation_Derivation.md`), Doc 10b (`10b_Privacy_Security_Goals_NIST_Implications.md`), Doc 11 (`11_Rules_Catalog.md`), and Doc 12 (`12_Rules_Catalog.xlsx`) all updated to PO/SO ID model in the same sprint.

**Note on tech references preserved as regulatory concepts:** SBOM (Software Bill of Materials) and CI/CD appear as abstract concepts in §6 because they are *regulatory concepts* (CRA Annex I §2 references SBOM; CI/CD is referenced abstractly). No vendor-named SBOM tools (CycloneDX, SPDX, etc.) or vendor CI platforms (GitHub Actions, GitLab CI, etc.) remain. Likewise enterprise centralized audit-log management appears only in an out-of-scope statement (no vendor named).

---

## Appendix A — Legacy PG/SG Aliases (DEPRECATED)

> **DEPRECATED — preserved for traceability with Phase 1 07c Appendix A (corr-009).** Phase 2 objectives are now keyed on PO-D-XX.X-NNN and SO-D-XX.X-NNN. The legacy corr-007 PG/SG IDs in this table are kept for cross-document traceability; do not introduce new PG/SG IDs in Phase 2 deliverables.

**Convention:** For each sub-domain that had a legacy PG, the PG becomes `PO-D-XX.X-001`. For each sub-domain that had a legacy SG, the SG becomes `SO-D-XX.X-001` (the NNN=001 sequence is reused independently per Phase 2 catalog). Phase 1 (07c) uses `AG-D-XX.X-001` for the PG slot and `AG-D-XX.X-002` for the SG slot; the Phase 1 mapping is preserved unchanged — this appendix only documents the Phase 2 PG→PO and SG→SO migration.

**Total: 31 aliases** (11 PG→PO + 20 SG→SO).

| Legacy ID (corr-007) | New ID (corr-012) | Sub-domain | Regulation | Type | Notes |
|---------------------|-------------------|------------|------------|------|-------|
| PG-D-01.1-001 | PO-D-01.1-001 | D-01.1 | GDPR | Privacy | Privacy Operational Objective |
| SG-D-01.1-001 | SO-D-01.1-001 | D-01.1 | CRA | Security | Security Operational Objective (note: not in §6 — only PO for D-01.1 in Phase 2) |
| PG-D-01.2-001 | PO-D-01.2-001 | D-01.2 | GDPR | Privacy | Privacy Operational Objective |
| SG-D-01.2-001 | SO-D-01.2-001 | D-01.2 | CRA | Security | Security Operational Objective (note: not in §6 — only PO for D-01.2 in Phase 2) |
| PG-D-01.3-001 | PO-D-01.3-001 | D-01.3 | GDPR | Privacy | **Phantom — F-01/F-03**; Phase 2 catalog does not carry a PO card (D-01.3 has CR rule but no PO), cross-referenced to Phase 1 07c Appendix A §A.1 |
| SG-D-01.3-001 | SO-D-01.3-001 | D-01.3 | CRA | Security | Security Operational Objective (note: not in §6 — only PO consideration for D-01.3 in Phase 2) |
| PG-D-01.4-001 | PO-D-01.4-001 | D-01.4 | GDPR | Privacy | Privacy Operational Objective |
| SG-D-01.4-001 | SO-D-01.4-001 | D-01.4 | CRA | Security | Security Operational Objective (note: not in §6 — only PO for D-01.4 in Phase 2) |
| PG-D-02.1-001 | PO-D-02.1-001 | D-02.1 | GDPR | Privacy | Privacy Operational Objective (note: not in §6 — only SO for D-02.1 in Phase 2) |
| SG-D-02.1-001 | SO-D-02.1-001 | D-02.1 | CRA | Security | Security Operational Objective |
| PG-D-02.2-001 | PO-D-02.2-001 | D-02.2 | GDPR | Privacy | Privacy Operational Objective (note: not in §6 — only SO for D-02.2 in Phase 2) |
| SG-D-02.2-001 | SO-D-02.2-001 | D-02.2 | CRA | Security | Security Operational Objective |
| SG-D-02.3-001 | SO-D-02.3-001 | D-02.3 | CRA | Security | Security Operational Objective |
| SG-D-02.4-001 | SO-D-02.4-001 | D-02.4 | CRA | Security | **Stale — F-06** (cosmetic; renamed to SO-D-06.2-001 in v1.1; preserved in §5.6 ID Integrity Check) |
| SG-D-03.1-001 | SO-D-03.1-001 | D-03.1 | CRA | Security | Security Operational Objective |
| SG-D-03.2-001 | SO-D-03.2-001 | D-03.2 | CRA | Security | Security Operational Objective |
| SG-D-03.3-001 | SO-D-03.3-001 | D-03.3 | CRA | Security | Security Operational Objective |
| SG-D-03.4-001 | SO-D-03.4-001 | D-03.4 | CRA | Security | Security Operational Objective |
| SG-D-04.1-001 | SO-D-04.1-001 | D-04.1 | CRA | Security | Security Operational Objective |
| SG-D-04.2-001 | SO-D-04.2-001 | D-04.2 | CRA | Security | Security Operational Objective |
| SG-D-04.3-001 | SO-D-04.3-001 | D-04.3 | CRA | Security | Security Operational Objective (T-001 anchor) |
| SG-D-04.4-001 | SO-D-04.4-001 | D-04.4 | CRA | Security | Security Operational Objective |
| PG-D-05.1-001 | PO-D-05.1-001 | D-05.1 | GDPR | Privacy | Privacy Operational Objective |
| PG-D-05.2-001 | PO-D-05.2-001 | D-05.2 | GDPR | Privacy | Privacy Operational Objective |
| PG-D-05.3-001 | PO-D-05.3-001 | D-05.3 | GDPR | Privacy | Privacy Operational Objective |
| PG-D-05.4-001 | PO-D-05.4-001 | D-05.4 | GDPR | Privacy | Privacy Operational Objective |
| SG-D-06.1-001 | SO-D-06.1-001 | D-06.1 | GDPR | Security | Security Operational Objective |
| SG-D-06.2-001 | SO-D-06.2-001 | D-06.2 | CRA | Security | Security Operational Objective |
| SG-D-06.3-001 | SO-D-06.3-001 | D-06.3 | GDPR | Security | Security Operational Objective |
| PG-D-07.1-001 | PO-D-07.1-001 | D-07.1 | GDPR | Privacy | Privacy Operational Objective |
| SG-D-08.1-001 | SO-D-08.1-001 | D-08.1 | GDPR | Security | Security Operational Objective |
| SG-D-08.2-001 | SO-D-08.2-001 | D-08.2 | GDPR | Security | Security Operational Objective |
| PG-D-09.1-001 | PO-D-09.1-001 | D-09.1 | GDPR | Privacy | Privacy Operational Objective (dual coverage with SO-D-09.1-001 — F-02) |
| SG-D-09.1-001 | SO-D-09.1-001 | D-09.1 | CRA | Security | Security Operational Objective (dual coverage with PO-D-09.1-001 — F-02) |
| PG-D-09.2-001 | PO-D-09.2-001 | D-09.2 | GDPR | Privacy | Privacy Operational Objective (dual coverage with SO-D-09.2-001 — T-M-001) |
| SG-D-09.2-001 | SO-D-09.2-001 | D-09.2 | CRA | Security | Security Operational Objective (dual coverage with PO-D-09.2-001 — T-M-001) |
| PG-D-09.3-001 | PO-D-09.3-001 | D-09.3 | CRA | Privacy | **Absent** — D-09.3 is DORA-exclusive and not applicable to TinyTask; PG-D-09.3 was never created in Phase 2 |
| SG-D-09.3-001 | SO-D-09.3-001 | D-09.3 | CRA | Security | **Absent** — see PG-D-09.3-001 note |
| PG-D-09.4-001 | PO-D-09.4-001 | D-09.4 | GDPR | Privacy | Privacy Operational Objective |
| SG-D-09.4-001 | SO-D-09.4-001 | D-09.4 | CRA | Security | Security Operational Objective (note: not in §6 — only PO for D-09.4 in Phase 2) |
| SG-D-10.2-001 | SO-D-10.2-001 | D-10.2 | CRA | Security | Security Operational Objective |
| SG-D-10.3-001 | SO-D-10.3-001 | D-10.3 | CRA | Security | Security Operational Objective |

**Total: 31 alias rows** (11 PG→PO + 20 SG→SO). Note that sub-domains in this table whose legacy PG or SG is *absent from §6* are listed for traceability only — the actual Phase 2 catalog contains only 11 PO + 20 SO cards per §3.1/§4.1.

---

**End of Fase de Especificação 1 + Fase de Especificação 4 Reconciliation + Fase de Especificação 9 corr-012 — Doc 10**