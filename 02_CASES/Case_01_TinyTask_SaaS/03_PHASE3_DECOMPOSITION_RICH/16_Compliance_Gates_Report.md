---
document_id: AEGIS-P3-RICH-16
title: Compliance Gates Report — TinyTask SaaS (Phase 3 RICH)
phase: 3
version: 2.0
created: 2026-08-24
updated: 2026-08-24
author: Sprint 4 Executor (paulo@methodology.pt)
status: DEEP_ENRICHED
sprint: 5
deep_enrichment_date: 2026-08-24
detail_cards_count: 30
cells_count: 445
fields_per_card: 17|12|tiered
tier_distribution: "GATE cards (17 with 17 fields + 13 with 12 fields)"
sprint_role: deep_enrichment_per_card
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [15_Requirements_Allocation.md, 14_Architectural_Nodes.md, 11_Rules_Catalog.md, RULE_FREEZE.md]
outputs: [17_Functional_Tree.md, 18_Functional_Tree.drawio]
related_documents: [15_Requirements_Allocation.md, 14_Architectural_Nodes.md, RULE_FREEZE.md, CORPUS_LINKAGE.md]
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Maturity, Priority, Stakeholders, Reporting]
freeze_total_gates: 30
freeze_total_crs: 30
reconciliation_note: "30 GATE rows (1:1 with CR); SC1 stale 38-rule claim RESOLVED; 4 orphan refs flagged F-S1-04/05/06/07."
sprint5_note: "Sprint 5: DEEP enrichment — 30 cards (17×17 fields + 13×12 fields) = 445 cells. Frontmatter status DEEP_ENRICHED, version 2.0."
---

# Compliance Gates Report — TinyTask SaaS (Phase 3 RICH)

> **Status:** ADJUSTED_FIELDS (Sprint 4). 30 GATE rows, 1:1 with 30 CR (per Doc 16 §5). All gates `PLANNED`; Sprint 5 verifies PASS/FAIL.

---

## §1 Reconciliation Notes

Compliance Gates are verification checkpoints anchored to Derivation Nodes (Doc 15) and ultimately to Compliance Rules (CR per RULE_FREEZE.md §1). One Gate per CR (30 gates). Legacy §5B SC1's stale "23 CR + 15 BPR = 38" claim is **RESOLVED** (F-00d RESOLVED in `RULE_FREEZE.md` §3.4) — freeze value is **30 CR + 16 BPR = 46 rules**.

**Authoritative sources:**
- `RULE_FREEZE.md` §1 — 30 CR (gate rows).
- `15_Requirements_Allocation.md` §2 — DN rows (gates mirror DN).
- `14_Architectural_Nodes.md` §2-§4 — node catalogue.
- `CORPUS_LINKAGE.md` §8 — Gate-to-D-XX.Y mapping.
- `KG_CHAINS.md` §1 CH-11 — GATE-D-04-03 → CR-D-04.3.

**Gate criteria (legacy §1):**
- All gates defined with verification method (TEST/INSPECT/DEMONSTRATE).
- AssetContext + ComplianceAnalysis documented per gate.
- Stop Conditions SC1-SC5 satisfied.

---

## §2 Gate Definitions (30 rows, 1:1 with CR)

| Gate ID | Rule | D-sub | Verification | Status | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|---------|------|-------|--------------|:------:|-------|-----------------------|----------|----------|--------------|-----------|
| GATE-CR-D-01.1-001 | CR-D-01.1-001 | D-01.1 | TEST | PLANNED | CTO | | | | | |
| GATE-CR-D-01.2-001 | CR-D-01.2-001 | D-01.2 | TEST | PLANNED | CTO | | | | | |
| GATE-CR-D-01.3-001 | CR-D-01.3-001 | D-01.3 | TEST | PLANNED | CTO | | | | | |
| GATE-CR-D-01.4-001 | CR-D-01.4-001 | D-01.4 | TEST | PLANNED | CTO | | | | | |
| GATE-CR-D-02.1-001 | CR-D-02.1-001 | D-02.1 | TEST | PLANNED | Lead Dev | | | | | |
| GATE-CR-D-02.2-001 | CR-D-02.2-001 | D-02.2 | INSPECT | PLANNED | Lead Dev | | | | | |
| GATE-CR-D-02.3-001 | CR-D-02.3-001 | D-02.3 | INSPECT | PLANNED | Lead Dev | | | | | |
| GATE-CR-D-03.1-001 | CR-D-03.1-001 | D-03.1 | TEST | PLANNED | CTO | | | | | |
| GATE-CR-D-03.2-001 | CR-D-03.2-001 | D-03.2 | TEST | PLANNED | CTO | | | | | |
| GATE-CR-D-03.3-001 | CR-D-03.3-001 | D-03.3 | INSPECT | PLANNED | IAM Admin | | | | | |
| GATE-CR-D-03.4-001 | CR-D-03.4-001 | D-03.4 | TEST | PLANNED | Ops Lead | | | | | |
| GATE-CR-D-04.1-001 | CR-D-04.1-001 | D-04.1 | TEST | PLANNED | Security Eng | | | | | |
| GATE-CR-D-04.2-001 | CR-D-04.2-001 | D-04.2 | TEST | PLANNED | Ops Lead | | | | | |
| GATE-CR-D-04.3-001 | CR-D-04.3-001 | D-04.3 | DEMONSTRATE | PLANNED | Incident Commander | | | | | |
| GATE-CR-D-04.4-001 | CR-D-04.4-001 | D-04.4 | TEST | PLANNED | Ops Lead | | | | | |
| GATE-CR-D-05.1-001 | CR-D-05.1-001 | D-05.1 | INSPECT | PLANNED | DPO | | | | | |
| GATE-CR-D-05.2-001 | CR-D-05.2-001 | D-05.2 | INSPECT | PLANNED | DPO | | | | | |
| GATE-CR-D-05.3-001 | CR-D-05.3-001 | D-05.3 | TEST | PLANNED | DPO | | | | | |
| GATE-CR-D-05.4-001 | CR-D-05.4-001 | D-05.4 | TEST | PLANNED | DPO | | | | | |
| GATE-CR-D-06.1-001 | CR-D-06.1-001 | D-06.1 | INSPECT | PLANNED | Procurement | | | | | |
| GATE-CR-D-06.2-001 | CR-D-06.2-001 | D-06.2 | TEST | PLANNED | Lead Dev | | | | | |
| GATE-CR-D-06.3-001 | CR-D-06.3-001 | D-06.3 | INSPECT | PLANNED | Legal Counsel | | | | | |
| GATE-CR-D-07.1-001 | CR-D-07.1-001 | D-07.1 | DEMONSTRATE | PLANNED | Lead Dev | | | | | |
| GATE-CR-D-08.1-001 | CR-D-08.1-001 | D-08.1 | INSPECT | PLANNED | DPO | | | | | |
| GATE-CR-D-08.2-001 | CR-D-08.2-001 | D-08.2 | INSPECT | PLANNED | DPO | | | | | |
| GATE-CR-D-09.1-001 | CR-D-09.1-001 | D-09.1 | INSPECT | PLANNED | Compliance Mgr | | | | | |
| GATE-CR-D-09.2-001 | CR-D-09.2-001 | D-09.2 | DEMONSTRATE | PLANNED | Risk Owner | | | | | |
| GATE-CR-D-09.4-001 | CR-D-09.4-001 | D-09.4 | INSPECT | PLANNED | DPO | | | | | |
| GATE-CR-D-10.2-001 | CR-D-10.2-001 | D-10.2 | TEST | PLANNED | CTO | | | | | |
| GATE-CR-D-10.3-001 | CR-D-10.3-001 | D-10.3 | INSPECT | PLANNED | Security Eng | | | | | |

---

### GATE-CR-D-01.1-001 — Data at Rest Encryption [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-01.1-001: Data at Rest Encryption.
**Scope:** Production stores.
**Out of Scope:** Ephemeral dev.
**Source:** CR-D-01.1-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1
**Verification Criteria:**
- Encryption verified on every store.
- KMS-managed keys.
- Annual rotation.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** CTO
**Dependencies:** NODE-SYS-010, DN-01
**Risk if not met:** H — unencrypted = GDPR Art. 32.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Maturity Score:** Cur 3/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- GATE-CR-D-01.1-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-01.2-001 — Data in Transit Encryption [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-01.2-001: Data in Transit Encryption.
**Scope:** All public endpoints.
**Out of Scope:** Internal mTLS.
**Source:** CR-D-01.2-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02, PR.DS-10 | PF: CT.DM-P1, CT.DM-P3
**Verification Criteria:**
- TLS 1.2+ enforced.
- Cipher suite policy.
- HSTS enabled.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** CTO
**Dependencies:** NODE-SYS-011, DN-02
**Risk if not met:** H — weak TLS = transit breach.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Maturity Score:** Cur 3/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- GATE-CR-D-01.2-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-01.3-001 — Cryptographic Key Management [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-01.3-001: Cryptographic Key Management.
**Scope:** All KMS-managed keys.
**Out of Scope:** Customer keys.
**Source:** CR-D-01.3-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-10 | PF: PR.DS-P1
**Verification Criteria:**
- Keys managed via KMS.
- Annual rotation.
- Access logged.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** CTO
**Dependencies:** DN-03
**Risk if not met:** M — key compromise = decrypt risk.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-01.3-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-01.4-001 — Data Integrity Mechanisms [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-01.4-001: Data Integrity Mechanisms.
**Scope:** Production critical records.
**Out of Scope:** Cache.
**Source:** CR-D-01.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02, PR.DS-10 | PF: CT.DM-P1, CT.DM-P3
**Verification Criteria:**
- 100% critical records.
- Tamper logs in SIEM.
- Algorithm pinned.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** CTO
**Dependencies:** NODE-SYS-016, DN-04
**Risk if not met:** H — undetected tampering = integrity breach.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Maturity Score:** Cur 3/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- GATE-CR-D-01.4-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-02.1-001 — Vulnerability-Free Release [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-02.1-001: Vulnerability-Free Release.
**Scope:** All production releases.
**Out of Scope:** Pre-alpha.
**Source:** CR-D-02.1-001
**NIST CSF Anchors:** CSF: GV.OV-02, ID.AM-02, ID.RA-01 | PF: ID.RA-P3, ID.RA-P5
**Verification Criteria:**
- 0 critical at release.
- Findings triaged.
- Pentest annual.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** Lead Developer
**Dependencies:** DN-05
**Risk if not met:** H — unpatched vuln = CRA trigger.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- GATE-CR-D-02.1-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-02.2-001 — Automated Patch Deployment [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-02.2-001: Automated Patch Deployment.
**Scope:** Production + staging.
**Out of Scope:** Third-party managed.
**Source:** CR-D-02.2-001
**NIST CSF Anchors:** CSF: GV.OV-02, ID.RA-01, PR.IR-03 | PF: —
**Verification Criteria:**
- Critical median ≤24h.
- Auto-rollback tested.
- Patch log.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** Lead Developer
**Dependencies:** DN-06
**Risk if not met:** H — unpatched = CRA trigger.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- GATE-CR-D-02.2-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-02.3-001 — Coordinated Vulnerability Disclosure [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-02.3-001: Coordinated Vulnerability Disclosure.
**Scope:** External researchers.
**Out of Scope:** Customer support.
**Source:** CR-D-02.3-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.SC-04, RS.CO-03 | PF: —
**Verification Criteria:**
- security.txt present.
- Median first response ≤72h.
- CVE for confirmed.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** Lead Developer
**Dependencies:** DN-07
**Risk if not met:** M — slow disclosure damages trust.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-02.3-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-03.1-001 — Authentication & Access Control [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-03.1-001: Authentication & Access Control.
**Scope:** All human identities.
**Out of Scope:** Service accounts.
**Source:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: —
**Verification Criteria:**
- 100% auth via IdP.
- Lockout after 5 fails.
- Audit log.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** CTO
**Dependencies:** DN-08
**Risk if not met:** H — auth bypass = total compromise.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Maturity Score:** Cur 3/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- GATE-CR-D-03.1-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-03.2-001 — Administrative MFA [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-03.2-001: Administrative MFA.
**Scope:** Privileged roles.
**Out of Scope:** Standard users.
**Source:** CR-D-03.2-001
**NIST CSF Anchors:** CSF: PR.AA-03, PR.AA-04, PR.AA-05 | PF: —
**Verification Criteria:**
- 100% privileged MFA.
- Session recording.
- Quarterly review.
**Verification Method:** DEMONSTRATE
**Status:** PLANNED
**Owner:** CTO
**Dependencies:** DN-09
**Risk if not met:** H — privileged compromise = total takeover.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Maturity Score:** Cur 3/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- GATE-CR-D-03.2-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-03.3-001 — Authorisation & Least Privilege [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-03.3-001: Authorisation & Least Privilege.
**Scope:** All internal staff.
**Out of Scope:** Customer self-service.
**Source:** CR-D-03.3-001
**NIST CSF Anchors:** CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: CT.PO-P1
**Verification Criteria:**
- Quarterly review.
- Deprovision ≤24h.
- Privilege creep detected.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** CTO
**Dependencies:** DN-10
**Risk if not met:** M — privilege drift = insider risk.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-03.3-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-03.4-001 — Secure System Defaults [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-03.4-001: Secure System Defaults.
**Scope:** Production hosts.
**Out of Scope:** Dev environments.
**Source:** CR-D-03.4-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.SC-03, PR.DS-10 | PF: CT.DP-P4, CT.PO-P4
**Verification Criteria:**
- ≥95% CIS compliance.
- Drift detection.
- Deviations documented.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** Operations Lead
**Dependencies:** DN-11
**Risk if not met:** M — misconfig = top breach vector.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-03.4-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-04.1-001 — Exploit Severity Limitation [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-04.1-001: Exploit Severity Limitation.
**Scope:** Production components.
**Out of Scope:** UI graceful degradation.
**Source:** CR-D-04.1-001
**NIST CSF Anchors:** CSF: DE.AE-02, DE.CM-01, DE.CM-09 | PF: CM.AW-P7
**Verification Criteria:**
- Containment ≤30min.
- Fail-safe verified.
- WAF rules tuned.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** Operations Lead
**Dependencies:** DN-12
**Risk if not met:** H — uncontrolled exploit = breach.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Maturity Score:** Cur 1/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- GATE-CR-D-04.1-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-04.2-001 — Availability Restoration & DoS Resilience [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-04.2-001: Availability Restoration & DoS Resilience.
**Scope:** Production APIs.
**Out of Scope:** Edge DDoS.
**Source:** CR-D-04.2-001
**NIST CSF Anchors:** CSF: DE.CM-09, PR.DS-10, PR.IR-03 | PF: CT.DM-P10, PR.PO-P7
**Verification Criteria:**
- Chaos test quarterly.
- Availability ≥99.9%.
- Runbook published.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** Operations Lead
**Dependencies:** DN-13
**Risk if not met:** M — sustained outage = GDPR + revenue.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-04.2-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-04.3-001 — Dual Regulatory Incident Notification [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-04.3-001: Dual Regulatory Incident Notification.
**Scope:** All confirmed incidents.
**Out of Scope:** Suspected-only.
**Source:** CR-D-04.3-001
**NIST CSF Anchors:** CSF: RS.CO-02, RS.MA-01, RS.MA-02 | PF: CM.AW-P7, CM.AW-P8, CM.PO-P1
**Verification Criteria:**
- ENISA ≤24h.
- CNPD ≤72h.
- Tabletop quarterly.
**Verification Method:** DEMONSTRATE
**Status:** PLANNED
**Owner:** Operations Lead
**Dependencies:** DN-14
**Risk if not met:** H — late = dual fine.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- GATE-CR-D-04.3-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-04.4-001 — Data Restoration and Recovery [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-04.4-001: Data Restoration and Recovery.
**Scope:** Production backups.
**Out of Scope:** Long-term archival.
**Source:** CR-D-04.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-10, PR.IR-03 | PF: —
**Verification Criteria:**
- RTO ≤24h, RPO ≤1h.
- Quarterly drill.
- Runbook signed off.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** Operations Lead
**Dependencies:** DN-15
**Risk if not met:** H — failed restore = data loss.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-04.4-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-05.1-001 — Data Minimisation [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-05.1-001: Data Minimisation.
**Scope:** All new features.
**Out of Scope:** Pre-existing data.
**Source:** CR-D-05.1-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P4, ID.IM-P6
**Verification Criteria:**
- Annual review.
- Design gate.
- Processor cascade.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** DPO
**Dependencies:** DN-16
**Risk if not met:** H — over-collection = Art. 5(1)(c).
**Affected Stakeholders:** Customer, DPO, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- GATE-CR-D-05.1-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-05.2-001 — Storage Limitation & Retention [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-05.2-001: Storage Limitation & Retention.
**Scope:** All personal data.
**Out of Scope:** Anonymised data.
**Source:** CR-D-05.2-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P4, ID.IM-P6
**Verification Criteria:**
- Retention policy.
- Auto-deletion verified.
- Annual review.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** DPO
**Dependencies:** DN-17
**Risk if not met:** M — over-retention = Art. 5(1)(e).
**Affected Stakeholders:** Customer, DPO, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- GATE-CR-D-05.2-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-05.3-001 — Complete and Secure Data Erasure [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-05.3-001: Complete and Secure Data Erasure.
**Scope:** Primary + backup + logs.
**Out of Scope:** Legal-hold.
**Source:** CR-D-05.3-001
**NIST CSF Anchors:** CSF: GV.SC-04, PR.DS-10, PR.DS-02 | PF: CT.DM-P4, CT.DM-P5
**Verification Criteria:**
- Erasure receipt.
- NIST SP 800-88.
- Processor cascade.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** DPO
**Dependencies:** DN-18
**Risk if not met:** H — incomplete = Art. 17.
**Affected Stakeholders:** Customer, DPO, Auditor
**Maturity Score:** Cur 1/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- GATE-CR-D-05.3-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-05.4-001 — Structured Data Portability [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-05.4-001: Structured Data Portability.
**Scope:** Personal-data export.
**Out of Scope:** Real-time streaming.
**Source:** CR-D-05.4-001
**NIST CSF Anchors:** CSF: PR.DS-10, PR.AA-03, PR.DS-02 | PF: CT.DM-P1, CT.DM-P6
**Verification Criteria:**
- Schema versioned.
- Auth + rate limit.
- JSON schema valid.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** DPO
**Dependencies:** DN-19
**Risk if not met:** M — Art. 20 gap.
**Affected Stakeholders:** Customer, DPO, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-05.4-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-06.1-001 — Processor Due Diligence [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-06.1-001: Processor Due Diligence.
**Scope:** All data processors.
**Out of Scope:** Non-data vendors.
**Source:** CR-D-06.1-001
**NIST CSF Anchors:** CSF: GV.SC-01, GV.SC-02, GV.SC-03 | PF: ID.IM-P2
**Verification Criteria:**
- Questionnaire pre-engagement.
- Annual review.
- Findings tracked.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** Procurement Lead
**Dependencies:** DN-20
**Risk if not met:** H — substandard = Art. 28.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-06.1-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-06.2-001 — Software Bill of Materials [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-06.2-001: Software Bill of Materials.
**Scope:** All production releases.
**Out of Scope:** Internal tooling.
**Source:** CR-D-06.2-001
**NIST CSF Anchors:** CSF: GV.SC-02, GV.SC-03, ID.RA-01 | PF: —
**Verification Criteria:**
- SBOM per release.
- Format validated.
- Customer portal tested.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** Lead Developer
**Dependencies:** DN-21
**Risk if not met:** M — missing SBOM = CRA Art. 13.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-06.2-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-06.3-001 — Contractual Processor Security [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-06.3-001: Contractual Processor Security.
**Scope:** All data processors.
**Out of Scope:** Non-data vendors.
**Source:** CR-D-06.3-001
**NIST CSF Anchors:** CSF: GV.OC-03, GV.SC-02, GV.SC-03 | PF: —
**Verification Criteria:**
- 100% active DPA.
- Annual review.
- Art. 28 clauses.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** Compliance Manager
**Dependencies:** DN-22
**Risk if not met:** H — missing DPA = Art. 28.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-06.3-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-07.1-001 — Security and Privacy by Design [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-07.1-001: Security and Privacy by Design.
**Scope:** All production code.
**Out of Scope:** Internal tooling.
**Source:** CR-D-07.1-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.RA-01, PR.DS-10 | PF: CT.DP-P2, CT.DP-P4, GV.PO-P2
**Verification Criteria:**
- Threat model per feature.
- Review checklist.
- Quarterly metrics.
**Verification Method:** DEMONSTRATE
**Status:** PLANNED
**Owner:** Lead Developer
**Dependencies:** DN-23
**Risk if not met:** M — design flaws late = costly.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- GATE-CR-D-07.1-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-08.1-001 — Annual Security Awareness [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-08.1-001: Annual Security Awareness.
**Scope:** All staff.
**Out of Scope:** External.
**Source:** CR-D-08.1-001
**NIST CSF Anchors:** CSF: PR.AT-01, PR.AT-02, PR.PS-01 | PF: GV.AT-P1, GV.AT-P2
**Verification Criteria:**
- 100% completion.
- Refreshed annually.
- Quiz required.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** Compliance Manager
**Dependencies:** DN-24
**Risk if not met:** M — untrained = phishing risk.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-08.1-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-08.2-001 — Role-Specific Security Competence [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-08.2-001: Role-Specific Security Competence.
**Scope:** Engineers, ops, DPO.
**Out of Scope:** General awareness.
**Source:** CR-D-08.2-001
**NIST CSF Anchors:** CSF: GV.RR-02, GV.RR-04, PR.AT-02 | PF: GV.AT-P1, GV.AT-P2
**Verification Criteria:**
- Role curricula.
- Completion tracked.
- Refreshed annually.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** Compliance Manager
**Dependencies:** DN-25
**Risk if not met:** M — role gaps = competency risk.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-08.2-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-09.1-001 — Security Governance & Technical Documentation [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-09.1-001: Security Governance & Technical Documentation.
**Scope:** All internal policies.
**Out of Scope:** Customer terms.
**Source:** CR-D-09.1-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.PO-02, GV.OV-01 | PF: CM.PO-P1, GV.PO-P1
**Verification Criteria:**
- Annual policy review.
- Technical docs current.
- ISMS maintained.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** Compliance Manager
**Dependencies:** DN-26
**Risk if not met:** M — governance gap = audit finding.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- GATE-CR-D-09.1-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-09.2-001 — Unified Risk Assessment [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-09.2-001: Unified Risk Assessment.
**Scope:** All high-risk processing.
**Out of Scope:** Low-risk routine.
**Source:** CR-D-09.2-001
**NIST CSF Anchors:** CSF: ID.RA-01, ID.RA-04, ID.RA-05 | PF: ID.RA-P3, ID.RA-P4, ID.RA-P5
**Verification Criteria:**
- Pre-launch DPIA.
- Annual full review.
- Risk register maintained.
**Verification Method:** DEMONSTRATE
**Status:** PLANNED
**Owner:** Risk Owner
**Dependencies:** DN-27
**Risk if not met:** H — missing DPIA = Art. 35.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Maturity Score:** Cur 1/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- GATE-CR-D-09.2-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-09.4-001 — Processing & Breach Records [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-09.4-001: Processing & Breach Records.
**Scope:** All processing + breaches.
**Out of Scope:** Anonymised.
**Source:** CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P8
**Verification Criteria:**
- RoPA ≤7d update.
- Breach register ≤24h.
- DPO review monthly.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** DPO
**Dependencies:** DN-28
**Risk if not met:** H — Art. 30 violation.
**Affected Stakeholders:** Customer, DPO, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- GATE-CR-D-09.4-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-10.2-001 — Audit Logging & Traceability [priority=MEDIUM, fields=12, gateState=PLANNED]

**Description:** Verification gate for CR-D-10.2-001: Audit Logging & Traceability.
**Scope:** All production logs.
**Out of Scope:** Dev logs.
**Source:** CR-D-10.2-001
**NIST CSF Anchors:** CSF: DE.CM-01, GV.PO-02, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9
**Verification Criteria:**
- 100% auth events.
- ≥12mo retention.
- WORM enforced.
**Verification Method:** TEST
**Status:** PLANNED
**Owner:** CTO
**Dependencies:** DN-29
**Risk if not met:** H — log gap = accountability breach.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Gate State:** PLANNED

<!-- GATE-CR-D-10.2-001 t=gate status=PLANNED state=PLANNED -->

### GATE-CR-D-10.3-001 — Control Effectiveness Testing [priority=HIGH, fields=17, gateState=PLANNED]

**Description:** Verification gate for CR-D-10.3-001: Control Effectiveness Testing.
**Scope:** All production controls.
**Out of Scope:** Dev.
**Source:** CR-D-10.3-001
**NIST CSF Anchors:** CSF: DE.AE-02, GV.OV-03, ID.RA-05 | PF: ID.RA-P3, ID.RA-P5
**Verification Criteria:**
- Annual pentest.
- Findings remediated.
- Controls catalog updated.
**Verification Method:** INSPECT
**Status:** PLANNED
**Owner:** Operations Lead
**Dependencies:** DN-30
**Risk if not met:** M — untested controls = drift.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Gate State:** PLANNED
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- GATE-CR-D-10.3-001 t=gate status=PLANNED state=PLANNED -->


## §3 Stop Conditions (SC1-SC5)

| SC | Description | Status | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|----|-------------|:------:|-------|-----------------------|----------|----------|--------------|-----------|
| SC1 | All CR + BPR rules mapped to ≥1 UC | **RESOLVED** — 46/46 (legacy "38" was stale; freeze = 46) | | | | | | |
| SC2 | All UCs covered by ≥1 FR/NFR | RESOLVED — 35 L1 + 27 L2 expansions = 62 refs | | | | | | |
| SC3 | All complex UCs refined to L2 | RESOLVED — 8 complex UCs identified (F-S1-11 CLOSED) | | | | | | |
| SC4 | All gates have explicit verification method | RESOLVED — 30/30 (see §2) | | | | | | |
| SC5 | All risks mapped to mitigation via gate | RESOLVED — see `25_Risk_Analysis.md` §4 | | | | | | |

---

## §4 Orphan rule refs (legacy → freeze)

| Orphan ref (legacy) | Closest freeze rule | Finding | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|---------------------|---------------------|---------|-------|-----------------------|----------|----------|--------------|-----------|
| CR-D-02.4-001 | CR-D-02.2-001 (Patches) | F-S1-04 OPEN | | | | | | |
| CR-D-06.4-001 | CR-D-06.3-001 (DPAs) | F-S1-05 OPEN | | | | | | |
| CR-D-08.3-001 | CR-D-08.1-001 (Training) | F-S1-06 OPEN | | | | | | |
| CR-D-09.3-001 | (orphan by design — DORA sole authority) | F-S1-07 OPEN | | | | | | |

See `RULE_FREEZE.md` §3.2 + §9 for full F-register.

---

## §5 Cross-references

- `15_Requirements_Allocation.md` §2 — DN rows (gates mirror DN 1:1)
- `14_Architectural_Nodes.md` §2-§4 — node catalogue
- `RULE_FREEZE.md` §1 — CR freeze
- `CORPUS_LINKAGE.md` §8 — Gate-to-D-XX.Y mapping
- `KG_CHAINS.md` §1 CH-11 — GATE-D-04-03 → CR-D-04.3
- `25_Risk_Analysis.md` §4 — risk mitigation → gate linkage

---

**End of Compliance Gates Report (Phase 3 RICH, ADJUSTED_FIELDS, Sprint 4)**
