---
document_id: AEGIS-P3-RICH-25
title: Risk Analysis — TinyTask SaaS (Phase 3 RICH)
phase: 3
version: 2.0
created: 2026-08-24
updated: 2026-08-24
author: Fase de Especificação 4 Executor (paulo@methodology.pt)
status: DEEP_ENRICHED
deep_enrichment_date: 2026-08-24
detail_cards_count: 48
cells_count: 626
fields_per_card: 17|12|tiered
tier_distribution: "RISK (10×17 fields) + THR (38×12 fields)"
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [13_Use_Cases_Catalog.md, 23_Functional_Requirements.md, RULE_FREEZE.md]
outputs: [22_Traceability_Matrix.xlsx]
related_documents: [13_Use_Cases_Catalog.md, 23_Functional_Requirements.md, CORPUS_LINKAGE.md §9]
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Implementation Status, Priority, Stakeholders, Reporting]
freeze_total_risks: 10
freeze_total_threats: 38
reconciliation_note: "10 risks + 38 threats freeze; F-S1-09 reports KG contamination on RISK-01 (label mismatch); Fase de Especificação 5 detail card fill."
sprint5_note: "Fase de Especificação 5: DEEP enrichment — 48 cards (10×17 fields + 38×12 fields) = 626 cells. Frontmatter status DEEP_ENRICHED, version 2.0."
---

# Risk Analysis — TinyTask SaaS (Phase 3 RICH)

> **Status:** ADJUSTED_FIELDS. 10 risk cards + 38 threat cards freeze. Fase de Especificação 5 deep-fills per-card schema.

---

## §1 Reconciliation Notes

Risk Analysis covers operational risks (RISK-01..RISK-10) and threat models (THR-01..THR-38). Risks are evaluated on likelihood × impact (per legacy §3) and trace to mitigations via Compliance Gates (Doc 16).

**Authoritative sources:**
- `RULE_FREEZE.md` §7.1 — 10 risks + 38 threats freeze.
- `CORPUS_LINKAGE.md` §9 — full risk/threat-to-D-XX.Y mapping.
- `13_Use_Cases_Catalog.md` §3 — UCs that mitigate risks.
- `16_Compliance_Gates_Report.md` §2 — gate-based mitigations.

**F-S1-09 disposition (KG contamination):** The Graphify KG carries 14 Case_02 contamination nodes (including RISK-01 labelled "Biometric Spoofing at eGate"). The markdown source for RISK-01 is generic ("Unauthorized access to personal data via spoofing"). KG re-run in isolation is Fase de Especificação 5 work; the markdown itself is correct.

---

## §2 Risk Catalogue (10 operational risks)

| ID | Risk | D-sub | Likelihood | Impact | Inherent | Mitigation UC | Mitigation Gate | Residual | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|----|------|-------|:----------:|:------:|:--------:|---------------|-----------------|:--------:|-------|-----------------------|----------|----------|--------------|-----------|
| RISK-01 | Unauthorized access to personal data via spoofing | D-03.2 | Medium | High | High | UC-10 (MFA) | GATE-CR-D-03.2-001 | Low | | | | | | |
| RISK-02 | Insecure code reaches production (no SSDLC) | D-07.2 | Medium | High | High | PROC-08, UC-14 | (BPR-D-07.2-001) — BPR-anchored closure (P7 2026-09-06) | Low | | | | | | |
| RISK-03 | Exploit severity not contained post-detection | D-04.1 | Low | High | Medium | UC-06 | GATE-CR-D-04.1-001 | Low | | | | | | |
| RISK-04 | DoS outage affects availability SLA | D-04.2 | Medium | High | High | UC-07 | GATE-CR-D-04.2-001 | Medium | | | | | | |
| RISK-05 | High-risk processing without DPIA | D-09.2 | Low | High | Medium | PROC-09, PROC-12 | GATE-CR-D-09.2-001 | Low | | | | | | |
| RISK-06 | Processor without sufficient guarantees | D-06.1 | Medium | High | High | PROC-14 | GATE-CR-D-06.1-001 | Low | | | | | | |
| RISK-07 | Incomplete erasure leaves residual PII | D-05.3 | Low | Critical | Medium | UC-01 | GATE-CR-D-05.3-001 | Low | | | | | | |
| RISK-08 | Over-collection of personal data | D-05.1 | Medium | Medium | Medium | UC-03 | GATE-CR-D-05.1-001 | Low | | | | | | |
| RISK-09 | RoPA out of date (post-incident discovery) | D-09.4 | Low | Medium | Low | PROC-13 | GATE-CR-D-09.4-001 | Low | | | | | | |
| RISK-10 | Coordinated disclosure not initiated | D-02.3 | Low | High | Medium | PROC-04 | GATE-CR-D-02.3-001 | Low | | | | | | |

---

## §3 Threat Catalogue (38 threats)

| Threat family | Count | Examples | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|---------------|------:|---------|-------|-----------------------|----------|----------|--------------|-----------|
| THR-01..04 | 4 | Data at rest, in transit, key mgmt, integrity (D-01.x) | | | | | | |
| THR-05..10 | 6 | Vulnerability, patch, disclosure (D-02.x) | | | | | | |
| THR-11..16 | 6 | Auth, MFA, RBAC, defaults (D-03.x) | | | | | | |
| THR-17..23 | 7 | Severity, DoS, notification, restoration (D-04.x) | | | | | | |
| THR-24..27 | 4 | Minimisation, retention, erasure, portability (D-05.x) | | | | | | |
| THR-28..30 | 3 | Processor DD, SBOM, DPA (D-06.x) | | | | | | |
| THR-31..33 | 3 | Security by design, SAST/DAST (D-07.x) | | | | | | |
| THR-34..35 | 2 | Awareness, role-specific training (D-08.x) | | | | | | |
| THR-36..37 | 2 | Risk assessment, processing records (D-09.x) | | | | | | |
| THR-38 | 1 | Audit logging (D-10.2) | | | | | | |
| **TOTAL** | **38** | | | | | | | |

Detailed threat cards (17-field schema) fill in Fase de Especificação 5. Each threat maps to one or more Risks (§2) and one or more Mitigations (UCs + Gates).

---

### RISK-01 — Unauthorized access to personal data via spoofing [priority=HIGH, fields=17]

**Description:** Threat actor gains unauthorized access to personal data by spoofing authentication credentials.
**Scope:** All authentication flows.
**Out of Scope:** Physical access threats.
**Source:** UC-10 + GATE-CR-D-03.2-001
**NIST CSF Anchors:** CSF: PR.AA-01, PR.AA-03 | PF: —
**Likelihood × Impact / Score:**
- Likelihood: Medium.
- Impact: High (personal data exposure).
- Score: High → Residual: Low.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** DN-08, DN-09
**Risk if not met:** H — personal data breach.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Treatment:** Mitigate via MFA + IdP + PAM (DN-08/09)
**Residual Risk:** Low
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- RISK-01 t=risk status=TODO -->

### RISK-02 — Insecure code reaches production (no SSDLC) [priority=HIGH, fields=17]

**Description:** Code with security defects reaches production due to absent or weak SSDLC.
**Scope:** All production code releases.
**Out of Scope:** Internal tooling.
**Source:** PROC-08, UC-14 + BPR-D-07.2-001 — BPR-anchored closure (P7 2026-09-06)
**NIST CSF Anchors:** CSF: PR.PS-01, PR.PS-02 | PF: —
**Likelihood × Impact / Score:**
- Likelihood: Medium.
- Impact: High (breach).
- Score: High → Residual: Low.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** DN-23, NODE-SYS-012
**Risk if not met:** H — exploit in production.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Treatment:** Mitigate via SSDLC + SAST/DAST + CI/CD gates (DN-23)
**Residual Risk:** Low
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- RISK-02 t=risk status=TODO -->

### RISK-03 — Exploit severity not contained post-detection [priority=HIGH, fields=17]

**Description:** Once an exploit is detected, blast radius is not contained within SLA.
**Scope:** Production components.
**Out of Scope:** Pre-detection window.
**Source:** UC-06 + GATE-CR-D-04.1-001
**NIST CSF Anchors:** CSF: DE.AE-02, DE.CM-09 | PF: CM.AW-P7
**Likelihood × Impact / Score:**
- Likelihood: Low.
- Impact: High.
- Score: Medium → Residual: Low.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** DN-12, NODE-SYS-005
**Risk if not met:** H — uncontrolled exploit = breach.
**Affected Stakeholders:** Operations Lead, Incident Commander
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Treatment:** Mitigate via WAF + fail-safe + Security Engineer (DN-12)
**Residual Risk:** Low
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- RISK-03 t=risk status=TODO -->

### RISK-04 — DoS outage affects availability SLA [priority=HIGH, fields=17]

**Description:** Application-layer DoS causes outage exceeding availability SLA.
**Scope:** Production APIs.
**Out of Scope:** Edge DDoS (cloud SLA).
**Source:** UC-07 + GATE-CR-D-04.2-001
**NIST CSF Anchors:** CSF: DE.CM-09, PR.IR-03 | PF: CT.DM-P10
**Likelihood × Impact / Score:**
- Likelihood: Medium.
- Impact: High.
- Score: High → Residual: Medium.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** DN-13, NODE-SYS-005
**Risk if not met:** M — sustained outage.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Treatment:** Mitigate via WAF + auto-scaling + chaos testing (DN-13)
**Residual Risk:** Medium
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- RISK-04 t=risk status=TODO -->

### RISK-05 — High-risk processing without DPIA [priority=HIGH, fields=17]

**Description:** High-risk processing launches without completed DPIA.
**Scope:** All new high-risk features.
**Out of Scope:** Bug fixes.
**Source:** PROC-09, PROC-12 + GATE-CR-D-09.2-001
**NIST CSF Anchors:** CSF: ID.RA-01, ID.RA-04 | PF: ID.RA-P3, ID.RA-P4
**Likelihood × Impact / Score:**
- Likelihood: Low.
- Impact: High.
- Score: Medium → Residual: Low.
**Verification Method:** DEMONSTRATE
**Owner:** Risk Owner
**Status:** TODO
**Dependencies:** DN-27, NODE-PROC-005
**Risk if not met:** H — Art. 35 violation.
**Affected Stakeholders:** Risk Owner, DPO, Compliance Manager
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Treatment:** Mitigate via DPIA gate + Risk Owner sign-off (DN-27)
**Residual Risk:** Low
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- RISK-05 t=risk status=TODO -->

### RISK-06 — Processor without sufficient guarantees [priority=HIGH, fields=17]

**Description:** Processor with insufficient security/privacy guarantees exposes personal data.
**Scope:** All data processors.
**Out of Scope:** Non-data vendors.
**Source:** PROC-14 + GATE-CR-D-06.1-001
**NIST CSF Anchors:** CSF: GV.SC-01, GV.SC-02 | PF: ID.IM-P2
**Likelihood × Impact / Score:**
- Likelihood: Medium.
- Impact: High.
- Score: High → Residual: Low.
**Verification Method:** INSPECT
**Owner:** Procurement Lead
**Status:** TODO
**Dependencies:** DN-20, NODE-PROC-011
**Risk if not met:** H — Art. 28 violation.
**Affected Stakeholders:** Procurement Lead, DPO, Legal Counsel, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Treatment:** Mitigate via due-diligence questionnaire + DPA + annual review (DN-20/22)
**Residual Risk:** Low
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- RISK-06 t=risk status=TODO -->

### RISK-07 — Incomplete deletion leaves residual data [priority=HIGH, fields=17]

**Description:** Erasure operation leaves residual personal data across stores.
**Scope:** All personal data stores.
**Out of Scope:** Anonymised.
**Source:** UC-01 + GATE-CR-D-05.3-001
**NIST CSF Anchors:** CSF: GV.SC-04, PR.DS-10 | PF: CT.DM-P4, CT.DM-P5
**Likelihood × Impact / Score:**
- Likelihood: Low.
- Impact: Critical.
- Score: Medium → Residual: Low.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** DN-18, NODE-SYS-015
**Risk if not met:** H — Art. 17 violation.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Treatment:** Mitigate via cryptographic erasure + audit (DN-18)
**Residual Risk:** Low
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- RISK-07 t=risk status=TODO -->

### RISK-08 — Over-collection of personal data [priority=HIGH, fields=17]

**Description:** System collects more personal data than necessary for the purpose.
**Scope:** All data collection flows.
**Out of Scope:** Anonymised.
**Source:** UC-03 + GATE-CR-D-05.1-001
**NIST CSF Anchors:** CSF: GV.PO-02 | PF: ID.IM-P1, ID.IM-P4
**Likelihood × Impact / Score:**
- Likelihood: Medium.
- Impact: Medium.
- Score: Medium → Residual: Low.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** DN-16, NODE-PROC-007
**Risk if not met:** M — Art. 5(1)(c) violation.
**Affected Stakeholders:** Customer, DPO, Compliance Manager
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Treatment:** Mitigate via data-minimisation review + design gate (DN-16)
**Residual Risk:** Low
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- RISK-08 t=risk status=TODO -->

### RISK-09 — RoPA out of date post-incident discovery [priority=HIGH, fields=17]

**Description:** RoPA discovered outdated after an incident reveals unrecorded processing.
**Scope:** All processing activities.
**Out of Scope:** Anonymised.
**Source:** PROC-13 + GATE-CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08 | PF: ID.IM-P1, ID.IM-P8
**Likelihood × Impact / Score:**
- Likelihood: Low.
- Impact: Medium.
- Score: Low → Residual: Low.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** DN-28, NODE-PROC-006
**Risk if not met:** M — Art. 30 violation.
**Affected Stakeholders:** DPO, Compliance Manager, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Treatment:** Mitigate via RoPA maintenance + breach register cascade (DN-28)
**Residual Risk:** Low
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- RISK-09 t=risk status=TODO -->

### RISK-10 — Coordinated disclosure not initiated [priority=HIGH, fields=17]

**Description:** Confirmed vulnerability not disclosed via coordinated process.
**Scope:** All confirmed vulnerabilities.
**Out of Scope:** Internal findings.
**Source:** PROC-04 + GATE-CR-D-02.3-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.SC-04 | PF: —
**Likelihood × Impact / Score:**
- Likelihood: Low.
- Impact: High.
- Score: Medium → Residual: Low.
**Verification Method:** INSPECT
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** DN-07, NODE-PROC-016
**Risk if not met:** M — CRA reputation + ENISA.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Treatment:** Mitigate via CVD process + security.txt + CVE assignment (DN-07)
**Residual Risk:** Low
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- RISK-10 t=risk status=TODO -->

### THR-DP-01 — Spoofing identity at authentication [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Identifiability threat against D-01.1; mitigated via Mitigate via MFA + IdP (DN-08/09).
**Scope:** D-sub D-01.1; UC-09 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-09 + D-01.1 + LINDDUN-Identifiability
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Identifiability.
- Scope: D-01.1.
- Treatment: Mitigate via MFA + IdP (DN-08/09).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-09
**Risk if not met:** M — mitigated via Mitigate via MFA + IdP (DN-08/09).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DP-01 t=thr status=TODO -->

### THR-DP-02 — Tampering with data at rest [priority=MEDIUM, fields=12]

**Description:** STRIDE-Tampering threat against D-01.1; mitigated via Mitigate via AES-256 + KMS (DN-01).
**Scope:** D-sub D-01.1; PROC-01 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-01 + D-01.1 + STRIDE-Tampering
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Tampering.
- Scope: D-01.1.
- Treatment: Mitigate via AES-256 + KMS (DN-01).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-01
**Risk if not met:** M — mitigated via Mitigate via AES-256 + KMS (DN-01).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DP-02 t=thr status=TODO -->

### THR-DP-03 — Disclosure in transit [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Disclosure threat against D-01.2; mitigated via Mitigate via TLS 1.2+ (DN-02).
**Scope:** D-sub D-01.2; UC-09 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-09 + D-01.2 + LINDDUN-Disclosure
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Disclosure.
- Scope: D-01.2.
- Treatment: Mitigate via TLS 1.2+ (DN-02).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-09
**Risk if not met:** M — mitigated via Mitigate via TLS 1.2+ (DN-02).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DP-03 t=thr status=TODO -->

### THR-DP-04 — Key compromise [priority=MEDIUM, fields=12]

**Description:** STRIDE-Information threat against D-01.3; mitigated via Mitigate via KMS + rotation (DN-03).
**Scope:** D-sub D-01.3; PROC-01 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-01 + D-01.3 + STRIDE-Information
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Information.
- Scope: D-01.3.
- Treatment: Mitigate via KMS + rotation (DN-03).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-01
**Risk if not met:** M — mitigated via Mitigate via KMS + rotation (DN-03).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DP-04 t=thr status=TODO -->

### THR-DEV-01 — Known vulnerability in dependency [priority=MEDIUM, fields=12]

**Description:** STRIDE-Information threat against D-02.1; mitigated via Mitigate via SCA + weekly scans (DN-05).
**Scope:** D-sub D-02.1; PROC-03 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-03 + D-02.1 + STRIDE-Information
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Information.
- Scope: D-02.1.
- Treatment: Mitigate via SCA + weekly scans (DN-05).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-03
**Risk if not met:** M — mitigated via Mitigate via SCA + weekly scans (DN-05).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DEV-01 t=thr status=TODO -->

### THR-DEV-02 — Unpatched CVE in production [priority=MEDIUM, fields=12]

**Description:** STRIDE-Elevation threat against D-02.2; mitigated via Mitigate via auto patch ≤24h (DN-06).
**Scope:** D-sub D-02.2; UC-05 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-05 + D-02.2 + STRIDE-Elevation
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Elevation.
- Scope: D-02.2.
- Treatment: Mitigate via auto patch ≤24h (DN-06).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-05
**Risk if not met:** M — mitigated via Mitigate via auto patch ≤24h (DN-06).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DEV-02 t=thr status=TODO -->

### THR-DEV-03 — Undisclosed zero-day [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Non-compliance threat against D-02.3; mitigated via Mitigate via CVD process (DN-07).
**Scope:** D-sub D-02.3; PROC-04 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-04 + D-02.3 + LINDDUN-Non-compliance
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Non-compliance.
- Scope: D-02.3.
- Treatment: Mitigate via CVD process (DN-07).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-04
**Risk if not met:** M — mitigated via Mitigate via CVD process (DN-07).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DEV-03 t=thr status=TODO -->

### THR-DEV-04 — Compromised third-party component [priority=MEDIUM, fields=12]

**Description:** STRIDE-Tampering threat against D-02.1; mitigated via Mitigate via SBOM + monitoring (DN-21).
**Scope:** D-sub D-02.1; PROC-03 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-03 + D-02.1 + STRIDE-Tampering
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Tampering.
- Scope: D-02.1.
- Treatment: Mitigate via SBOM + monitoring (DN-21).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-03
**Risk if not met:** M — mitigated via Mitigate via SBOM + monitoring (DN-21).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DEV-04 t=thr status=TODO -->

### THR-DEV-05 — Malicious package in registry [priority=MEDIUM, fields=12]

**Description:** STRIDE-Tampering threat against D-02.2; mitigated via Mitigate via SCA + pinned versions (DN-05).
**Scope:** D-sub D-02.2; UC-14 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-14 + D-02.2 + STRIDE-Tampering
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Tampering.
- Scope: D-02.2.
- Treatment: Mitigate via SCA + pinned versions (DN-05).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-14
**Risk if not met:** M — mitigated via Mitigate via SCA + pinned versions (DN-05).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DEV-05 t=thr status=TODO -->

### THR-DEV-06 — Stale firmware/OS [priority=MEDIUM, fields=12]

**Description:** STRIDE-Elevation threat against D-02.2; mitigated via Mitigate via quarterly patch cycle (DN-06).
**Scope:** D-sub D-02.2; UC-08 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-08 + D-02.2 + STRIDE-Elevation
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Elevation.
- Scope: D-02.2.
- Treatment: Mitigate via quarterly patch cycle (DN-06).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-08
**Risk if not met:** M — mitigated via Mitigate via quarterly patch cycle (DN-06).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DEV-06 t=thr status=TODO -->

### THR-IAM-01 — Credential stuffing [priority=MEDIUM, fields=12]

**Description:** STRIDE-Spoofing threat against D-03.1; mitigated via Mitigate via MFA + lockout (DN-08).
**Scope:** D-sub D-03.1; UC-09 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-09 + D-03.1 + STRIDE-Spoofing
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Spoofing.
- Scope: D-03.1.
- Treatment: Mitigate via MFA + lockout (DN-08).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-09
**Risk if not met:** M — mitigated via Mitigate via MFA + lockout (DN-08).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-IAM-01 t=thr status=TODO -->

### THR-IAM-02 — Privileged session hijack [priority=MEDIUM, fields=12]

**Description:** STRIDE-Elevation threat against D-03.2; mitigated via Mitigate via FIDO2 + PAM (DN-09).
**Scope:** D-sub D-03.2; UC-10 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-10 + D-03.2 + STRIDE-Elevation
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Elevation.
- Scope: D-03.2.
- Treatment: Mitigate via FIDO2 + PAM (DN-09).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-10
**Risk if not met:** M — mitigated via Mitigate via FIDO2 + PAM (DN-09).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-IAM-02 t=thr status=TODO -->

### THR-IAM-03 — Privilege escalation via misconfig [priority=MEDIUM, fields=12]

**Description:** STRIDE-Elevation threat against D-03.3; mitigated via Mitigate via RBAC + reviews (DN-10).
**Scope:** D-sub D-03.3; UC-11 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-11 + D-03.3 + STRIDE-Elevation
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Elevation.
- Scope: D-03.3.
- Treatment: Mitigate via RBAC + reviews (DN-10).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-11
**Risk if not met:** M — mitigated via Mitigate via RBAC + reviews (DN-10).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-IAM-03 t=thr status=TODO -->

### THR-IAM-04 — Default credentials in production [priority=MEDIUM, fields=12]

**Description:** STRIDE-Spoofing threat against D-03.4; mitigated via Mitigate via hardened baseline (DN-11).
**Scope:** D-sub D-03.4; UC-12 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-12 + D-03.4 + STRIDE-Spoofing
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Spoofing.
- Scope: D-03.4.
- Treatment: Mitigate via hardened baseline (DN-11).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-12
**Risk if not met:** M — mitigated via Mitigate via hardened baseline (DN-11).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-IAM-04 t=thr status=TODO -->

### THR-IAM-05 — Session token theft [priority=MEDIUM, fields=12]

**Description:** STRIDE-Spoofing threat against D-03.1; mitigated via Mitigate via TLS + 30-min timeout (DN-02).
**Scope:** D-sub D-03.1; UC-09 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-09 + D-03.1 + STRIDE-Spoofing
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Spoofing.
- Scope: D-03.1.
- Treatment: Mitigate via TLS + 30-min timeout (DN-02).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-09
**Risk if not met:** M — mitigated via Mitigate via TLS + 30-min timeout (DN-02).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-IAM-05 t=thr status=TODO -->

### THR-IAM-06 — Orphaned account post-termination [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Link threat against D-03.3; mitigated via Mitigate via deprovision ≤24h (DN-10).
**Scope:** D-sub D-03.3; UC-11 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-11 + D-03.3 + LINDDUN-Link
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Link.
- Scope: D-03.3.
- Treatment: Mitigate via deprovision ≤24h (DN-10).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-11
**Risk if not met:** M — mitigated via Mitigate via deprovision ≤24h (DN-10).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-IAM-06 t=thr status=TODO -->

### THR-SEC-01 — Active exploit in production [priority=MEDIUM, fields=12]

**Description:** STRIDE-Tampering threat against D-04.1; mitigated via Mitigate via WAF + fail-safe (DN-12).
**Scope:** D-sub D-04.1; UC-06 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-06 + D-04.1 + STRIDE-Tampering
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Tampering.
- Scope: D-04.1.
- Treatment: Mitigate via WAF + fail-safe (DN-12).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-06
**Risk if not met:** M — mitigated via Mitigate via WAF + fail-safe (DN-12).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-SEC-01 t=thr status=TODO -->

### THR-SEC-02 — DoS attack [priority=MEDIUM, fields=12]

**Description:** STRIDE-DoS threat against D-04.2; mitigated via Mitigate via rate-limit + scrub (DN-13).
**Scope:** D-sub D-04.2; UC-07 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-07 + D-04.2 + STRIDE-DoS
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-DoS.
- Scope: D-04.2.
- Treatment: Mitigate via rate-limit + scrub (DN-13).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-07
**Risk if not met:** M — mitigated via Mitigate via rate-limit + scrub (DN-13).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-SEC-02 t=thr status=TODO -->

### THR-SEC-03 — Delayed incident notification [priority=MEDIUM, fields=12]

**Description:** STRIDE-Repudiation threat against D-04.3; mitigated via Mitigate via dual-regulator SLA (DN-14).
**Scope:** D-sub D-04.3; PROC-05 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-05 + D-04.3 + STRIDE-Repudiation
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Repudiation.
- Scope: D-04.3.
- Treatment: Mitigate via dual-regulator SLA (DN-14).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-05
**Risk if not met:** M — mitigated via Mitigate via dual-regulator SLA (DN-14).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-SEC-03 t=thr status=TODO -->

### THR-SEC-04 — Failed data restoration [priority=MEDIUM, fields=12]

**Description:** STRIDE-DoS threat against D-04.4; mitigated via Mitigate via RTO/RPO drill (DN-15).
**Scope:** D-sub D-04.4; UC-08 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-08 + D-04.4 + STRIDE-DoS
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-DoS.
- Scope: D-04.4.
- Treatment: Mitigate via RTO/RPO drill (DN-15).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-08
**Risk if not met:** M — mitigated via Mitigate via RTO/RPO drill (DN-15).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-SEC-04 t=thr status=TODO -->

### THR-SEC-05 — Undetected breach [priority=MEDIUM, fields=12]

**Description:** STRIDE-Repudiation threat against D-04.3; mitigated via Mitigate via SIEM + breach register (DN-29).
**Scope:** D-sub D-04.3; PROC-05 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-05 + D-04.3 + STRIDE-Repudiation
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Repudiation.
- Scope: D-04.3.
- Treatment: Mitigate via SIEM + breach register (DN-29).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-05
**Risk if not met:** M — mitigated via Mitigate via SIEM + breach register (DN-29).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-SEC-05 t=thr status=TODO -->

### THR-SEC-06 — Incomplete forensic evidence [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Detectability threat against D-04.4; mitigated via Mitigate via WORM + retention (DN-29).
**Scope:** D-sub D-04.4; UC-08 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-08 + D-04.4 + LINDDUN-Detectability
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Detectability.
- Scope: D-04.4.
- Treatment: Mitigate via WORM + retention (DN-29).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-08
**Risk if not met:** M — mitigated via Mitigate via WORM + retention (DN-29).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-SEC-06 t=thr status=TODO -->

### THR-SEC-07 — Coordination gap with regulators [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Non-compliance threat against D-04.3; mitigated via Mitigate via templates + tabletop (DN-14).
**Scope:** D-sub D-04.3; PROC-05 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-05 + D-04.3 + LINDDUN-Non-compliance
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Non-compliance.
- Scope: D-04.3.
- Treatment: Mitigate via templates + tabletop (DN-14).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-05
**Risk if not met:** M — mitigated via Mitigate via templates + tabletop (DN-14).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-SEC-07 t=thr status=TODO -->

### THR-DAT-01 — Over-collection of personal data [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Identifiability threat against D-05.1; mitigated via Mitigate via data-minimisation (DN-16).
**Scope:** D-sub D-05.1; UC-03 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-03 + D-05.1 + LINDDUN-Identifiability
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Identifiability.
- Scope: D-05.1.
- Treatment: Mitigate via data-minimisation (DN-16).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-03
**Risk if not met:** M — mitigated via Mitigate via data-minimisation (DN-16).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DAT-01 t=thr status=TODO -->

### THR-DAT-02 — Over-retention of personal data [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Detectability threat against D-05.2; mitigated via Mitigate via retention policy (DN-17).
**Scope:** D-sub D-05.2; UC-03 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-03 + D-05.2 + LINDDUN-Detectability
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Detectability.
- Scope: D-05.2.
- Treatment: Mitigate via retention policy (DN-17).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-03
**Risk if not met:** M — mitigated via Mitigate via retention policy (DN-17).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DAT-02 t=thr status=TODO -->

### THR-DAT-03 — Incomplete erasure [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Detectability threat against D-05.3; mitigated via Mitigate via cryptographic erasure (DN-18).
**Scope:** D-sub D-05.3; UC-01 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-01 + D-05.3 + LINDDUN-Detectability
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Detectability.
- Scope: D-05.3.
- Treatment: Mitigate via cryptographic erasure (DN-18).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-01
**Risk if not met:** M — mitigated via Mitigate via cryptographic erasure (DN-18).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DAT-03 t=thr status=TODO -->

### THR-DAT-04 — Portability format gap [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Link threat against D-05.4; mitigated via Mitigate via JSON/CSV/PDF (DN-19).
**Scope:** D-sub D-05.4; UC-04 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-04 + D-05.4 + LINDDUN-Link
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Link.
- Scope: D-05.4.
- Treatment: Mitigate via JSON/CSV/PDF (DN-19).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-04
**Risk if not met:** M — mitigated via Mitigate via JSON/CSV/PDF (DN-19).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DAT-04 t=thr status=TODO -->

### THR-SUP-01 — Substandard processor [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Non-compliance threat against D-06.1; mitigated via Mitigate via due diligence (DN-20).
**Scope:** D-sub D-06.1; PROC-14 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-14 + D-06.1 + LINDDUN-Non-compliance
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Non-compliance.
- Scope: D-06.1.
- Treatment: Mitigate via due diligence (DN-20).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-14
**Risk if not met:** M — mitigated via Mitigate via due diligence (DN-20).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-SUP-01 t=thr status=TODO -->

### THR-SUP-02 — Missing SBOM [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Detectability threat against D-06.2; mitigated via Mitigate via SBOM per release (DN-21).
**Scope:** D-sub D-06.2; UC-17 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-17 + D-06.2 + LINDDUN-Detectability
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Detectability.
- Scope: D-06.2.
- Treatment: Mitigate via SBOM per release (DN-21).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-17
**Risk if not met:** M — mitigated via Mitigate via SBOM per release (DN-21).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-SUP-02 t=thr status=TODO -->

### THR-SUP-03 — Missing DPA [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Non-compliance threat against D-06.3; mitigated via Mitigate via DPA lifecycle (DN-22).
**Scope:** D-sub D-06.3; CAP-01 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** CAP-01 + D-06.3 + LINDDUN-Non-compliance
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Non-compliance.
- Scope: D-06.3.
- Treatment: Mitigate via DPA lifecycle (DN-22).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** CAP-01
**Risk if not met:** M — mitigated via Mitigate via DPA lifecycle (DN-22).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-SUP-03 t=thr status=TODO -->

### THR-DEV2-01 — Design defect shipped [priority=MEDIUM, fields=12]

**Description:** STRIDE-Information threat against D-07.1; mitigated via Mitigate via SSDLC + threat model (DN-23).
**Scope:** D-sub D-07.1; PROC-08 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-08 + D-07.1 + STRIDE-Information
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Information.
- Scope: D-07.1.
- Treatment: Mitigate via SSDLC + threat model (DN-23).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-08
**Risk if not met:** M — mitigated via Mitigate via SSDLC + threat model (DN-23).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DEV2-01 t=thr status=TODO -->

### THR-DEV2-02 — SAST/DAST gap [priority=MEDIUM, fields=12]

**Description:** STRIDE-Tampering threat against D-07.2; mitigated via Mitigate via CI/CD gates (DN-05/23).
**Scope:** D-sub D-07.2; UC-14 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-14 + D-07.2 + STRIDE-Tampering
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Tampering.
- Scope: D-07.2.
- Treatment: Mitigate via CI/CD gates (DN-05/23).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-14
**Risk if not met:** M — mitigated via Mitigate via CI/CD gates (DN-05/23).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DEV2-02 t=thr status=TODO -->

### THR-DEV2-03 — Code review bypass [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Unawareness threat against D-07.1; mitigated via Mitigate via 2-person review (DN-23).
**Scope:** D-sub D-07.1; PROC-08 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-08 + D-07.1 + LINDDUN-Unawareness
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Unawareness.
- Scope: D-07.1.
- Treatment: Mitigate via 2-person review (DN-23).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-08
**Risk if not met:** M — mitigated via Mitigate via 2-person review (DN-23).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-DEV2-03 t=thr status=TODO -->

### THR-TRN-01 — Untrained staff (phishing) [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Unawareness threat against D-08.1; mitigated via Mitigate via 100% training (DN-24).
**Scope:** D-sub D-08.1; PROC-15 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-15 + D-08.1 + LINDDUN-Unawareness
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Unawareness.
- Scope: D-08.1.
- Treatment: Mitigate via 100% training (DN-24).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-15
**Risk if not met:** M — mitigated via Mitigate via 100% training (DN-24).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-TRN-01 t=thr status=TODO -->

### THR-TRN-02 — Role-specific knowledge gap [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Unawareness threat against D-08.2; mitigated via Mitigate via role curricula (DN-25).
**Scope:** D-sub D-08.2; PROC-16 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-16 + D-08.2 + LINDDUN-Unawareness
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Unawareness.
- Scope: D-08.2.
- Treatment: Mitigate via role curricula (DN-25).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-16
**Risk if not met:** M — mitigated via Mitigate via role curricula (DN-25).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-TRN-02 t=thr status=TODO -->

### THR-GOV-01 — Missing DPIA for high-risk launch [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Non-compliance threat against D-09.2; mitigated via Mitigate via DPIA gate (DN-27).
**Scope:** D-sub D-09.2; PROC-12 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-12 + D-09.2 + LINDDUN-Non-compliance
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Non-compliance.
- Scope: D-09.2.
- Treatment: Mitigate via DPIA gate (DN-27).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-12
**Risk if not met:** M — mitigated via Mitigate via DPIA gate (DN-27).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-GOV-01 t=thr status=TODO -->

### THR-GOV-02 — Outdated RoPA [priority=MEDIUM, fields=12]

**Description:** LINDDUN-Detectability threat against D-09.4; mitigated via Mitigate via RoPA maintenance (DN-28).
**Scope:** D-sub D-09.4; PROC-13 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** PROC-13 + D-09.4 + LINDDUN-Detectability
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: LINDDUN-Detectability.
- Scope: D-09.4.
- Treatment: Mitigate via RoPA maintenance (DN-28).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** PROC-13
**Risk if not met:** M — mitigated via Mitigate via RoPA maintenance (DN-28).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-GOV-02 t=thr status=TODO -->

### THR-AUD-01 — Log tampering [priority=MEDIUM, fields=12]

**Description:** STRIDE-Repudiation threat against D-10.2; mitigated via Mitigate via WORM + SIEM (DN-29).
**Scope:** D-sub D-10.2; UC-13 use case.
**Out of Scope:** Out-of-scope threats documented in §3 (STRIDE + LINDDUN matrix).
**Source:** UC-13 + D-10.2 + STRIDE-Repudiation
**NIST CSF Anchors:** CSF: per NFR catalogue | PF: per NIST_ANCHORS.md
**Verification Criteria:**
- Threat type: STRIDE-Repudiation.
- Scope: D-10.2.
- Treatment: Mitigate via WORM + SIEM (DN-29).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** UC-13
**Risk if not met:** M — mitigated via Mitigate via WORM + SIEM (DN-29).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- THR-AUD-01 t=thr status=TODO -->


## §4 Mitigation linkage

Every Risk in §2 maps to:
- ≥1 Compliance Gate (Doc 16 §2) — TEST/INSPECT/DEMONSTRATE verification.
- ≥1 Use Case (Doc 13 §3) — operational mitigation.

No risk is "untreated" (every risk has both gate + UC mitigation). Fase de Especificação 5 will populate full mitigation evidence per risk card.

---

## §5 Cross-references

- `13_Use_Cases_Catalog.md` §3 — UC catalogue (mitigations)
- `16_Compliance_Gates_Report.md` §2 — gates (verification)
- `23_Functional_Requirements.md` §2 — FR catalogue
- `24_Non_Functional_Requirements.md` §2 — NFR catalogue
- `CORPUS_LINKAGE.md` §9 — risk/threat-to-D-XX.Y
- `RULE_FREEZE.md` §7.1 — risk/threat counts
- `KG_CHAINS.md` §1 CH-12 — NODE-PROC-001 → CR-D-04.3 (incident response)

---

**End of Risk Analysis (Phase 3 RICH, ADJUSTED_FIELDS, Fase de Especificação 4)**
