---
document_id: AEGIS-P3-RICH-23
title: Functional Requirements — TinyTask SaaS (Phase 3 RICH)
phase: 3
version: 2.0
created: 2026-08-24
updated: 2026-08-24
author: Fase de Especificação 4 Executor (paulo@methodology.pt)
status: DEEP_ENRICHED
deep_enrichment_date: 2026-08-24
detail_cards_count: 30
cells_count: 480
fields_per_card: 17|12|tiered
tier_distribution: "FR cards (24 with 17 fields + 6 with 12 fields)"
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [13_Use_Cases_Catalog.md, 24_Non_Functional_Requirements.md, 11_Rules_Catalog.md, RULE_FREEZE.md]
outputs: [25_Risk_Analysis.md, 22_Traceability_Matrix.xlsx]
related_documents: [24_Non_Functional_Requirements.md, 15_Requirements_Allocation.md, RULE_FREEZE.md, NIST_ANCHORS.md, CORPUS_LINKAGE.md]
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Implementation Status, Priority, Stakeholders, Reporting]
freeze_total_frs: 30
reconciliation_note: "30 FR freeze (F-00b RESOLVED — legacy 60 figure was stale); FR-16/FR-23 semantic remap flagged F-S2-02/F-S2-03 for Fase de Especificação 5."
sprint5_note: "Fase de Especificação 5: DEEP enrichment — 30 cards (24×17 fields + 6×12 fields) = 480 cells. Frontmatter status DEEP_ENRICHED, version 2.0."
---

# Functional Requirements — TinyTask SaaS (Phase 3 RICH)

> **Status:** ADJUSTED_FIELDS. 30 FR cards freeze. Fase de Especificação 5 deep-fills the 17-field per-card schema.

---

## §1 Reconciliation Notes

This document specifies technology-agnostic functional requirements (FR-01..FR-30) derived from Use Cases (Doc 13) and Non-Functional Requirements (Doc 24). FR IDs use the canonical `FR-NN` format.

**Authoritative sources:**
- `RULE_FREEZE.md` §6 — 30 FR freeze.
- `NIST_ANCHORS.md` §3.2 — per-FR NIST CSF 2.0 + PF 1.0.
- `CORPUS_LINKAGE.md` §4 — FR-to-D-XX.Y mapping.
- `KG_CHAINS.md` §1 CH-09 — FR-29 → UC-25 → CR-D-04.3 (KG node label mismatch F-S2-01).

**Legacy drift disposition:**
- Legacy `60 FRs` figure is **stale** (F-00b RESOLVED) — freeze is 30.
- FR-16 (regulatory notification) → mapped to CR-D-04.3-001 in this sprint (legacy Doc 23 §3 had CR-D-01.1-001; F-S2-02 OPEN for Fase de Especificação 5 confirmation).
- FR-23 (SBOM) → mapped to CR-D-06.2-001 in this sprint (legacy Doc 23 §3 had CR-D-02.1-001; F-S2-03 OPEN for Fase de Especificação 5 confirmation).

---

## §2 Functional Requirements Catalogue (30 cards)

> **Format:** `FR-NN | Domain | Requirement statement | Source UCs | Source NFRs | Source CR | Verification | Priority | NIST`
> Card detail (17-field schema) fills in Fase de Especificação 5.

### §2.1 IAM domain (FR-01..FR-06)

| FR ID | Requirement (abbreviated) | UCs | NFRs | CR | Verif | Prio | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-------|---------------------------|-----|------|----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| FR-01 | Register + provision new users | UC-11, UC-13 | NFR-02 | CR-D-03.1-001 | TEST | HIGH | | | | | | |
| FR-02 | Authenticate + lock after 5 fails + log all attempts | UC-09 | NFR-01..07/20/32/34 | CR-D-03.1-001 | TEST | CRITICAL | | | | | | |
| FR-03 | MFA for privileged accounts | UC-12 | NFR-01 | CR-D-03.1-001 | DEMONSTRATE | HIGH | | | | | | |
| FR-04 | Deprovision accounts within 24h of termination | PROC-07 | NFR-02 | CR-D-03.1-001 | INSPECT | HIGH | | | | | | |
| FR-05 | Assign roles based on job function | UC-13 | NFR-02, NFR-09 | CR-D-03.1-001 | TEST | HIGH | | | | | | |
| FR-06 | Password reset + 30-min session timeout | UC-09, PROC-06 | NFR-06, NFR-07 | — | TEST | MEDIUM | | | | | | |

### §2.2 DP domain (FR-07..FR-12)

| FR ID | Requirement | UCs | NFRs | CR | Verif | Prio | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-------|-------------|-----|------|----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| FR-07 | DSAR via web/email; report in JSON/CSV/PDF ≤30d | PROC-01 | NFR-21, NFR-22 | CR-D-01.1-001 | TEST | HIGH | | | | | | |
| FR-08 | Erasure request; delete primary+backup+logs ≤30d | UC-01 | NFR-03, NFR-23 | CR-D-01.1-001 | TEST | CRITICAL | | | | | | |
| FR-09 | Data export in portable format | UC-02 | NFR-04, NFR-24 | CR-D-01.1-001 | TEST | HIGH | | | | | | |
| FR-10 | Consent preferences + records | UC-03 | NFR-26 | — | TEST | CRITICAL | | | | | | |
| FR-11 | Rectification of inaccurate data | UC-04 | NFR-08, NFR-28 | CR-D-01.1-001 | TEST | HIGH | | | | | | |
| FR-12 | Object to processing + restriction request | UC-03 | NFR-27, NFR-30 | CR-D-01.1-001 | TEST | MEDIUM | | | | | | |

### §2.3 SEC domain (FR-13..FR-19)

| FR ID | Requirement | UCs | NFRs | CR | Verif | Prio | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-------|-------------|-----|------|----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| FR-13 | Collect + correlate security events + alerts | PROC-03, UC-08 | NFR-10, NFR-32 | CR-D-02.1-001 | INSPECT | CRITICAL | | | | | | |
| FR-14 | Notify on-call ≤15min; escalate ≤15min | PROC-03 | NFR-17 | CR-D-04.1-001 | TEST | CRITICAL | | | | | | |
| FR-15 | Contain incident ≤4h; preserve evidence | UC-05 | NFR-09/17/32 | CR-D-04.1-001 | DEMONSTRATE | CRITICAL | | | | | | |
| FR-16 | Regulatory notification 24h CRA / 72h GDPR | U.C.1.6.1 (legacy), UC-05 | NFR-17/29/41/44 | CR-D-04.3-001 (F-S2-02) | TEST | CRITICAL | | | | | | |
| FR-17 | Weekly vulnerability scans; prioritise by risk | PROC-04 | NFR-10, NFR-46 | CR-D-02.1-001 | TEST | HIGH | | | | | | |
| FR-18 | Critical patches ≤24h; high ≤7d | UC-06 | NFR-03, NFR-12 | CR-D-02.1-001 | INSPECT | CRITICAL | | | | | | |
| FR-19 | Quarterly access review + BCP activation (RTO 24h) | PROC-05, UC-08 | NFR-02/14..19 | CR-D-03.1-001 | INSPECT | CRITICAL | | | | | | |

### §2.4 DEV domain (FR-20..FR-23)

| FR ID | Requirement | UCs | NFRs | CR | Verif | Prio | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-------|-------------|-----|------|----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| FR-20 | SAST + dep vuln scan + secret detection per commit | PROC-08, UC-14, UC-15 | NFR-05, NFR-07, NFR-12 | CR-D-07.1-001 | TEST | HIGH | | | | | | |
| FR-21 | Security gates before merge; block on critical | UC-15 | NFR-05/07/11/12 | CR-D-02.1-001 | TEST | CRITICAL | | | | | | |
| FR-22 | Change request submission + approval | UC-16 | — (process) | — | TEST | MEDIUM | | | | | | |
| FR-23 | Generate SBOM per release | PROC-09 | NFR-40, NFR-45 | CR-D-06.2-001 (F-S2-03) | TEST | HIGH | | | | | | |

### §2.5 GOV domain (FR-24..FR-28)

| FR ID | Requirement | UCs | NFRs | CR | Verif | Prio | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-------|-------------|-----|------|----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| FR-24 | Regulatory notifications + log timestamps | U.C.5.7.1 (legacy) | NFR-33, NFR-41, NFR-44 | — | TEST | CRITICAL | | | | | | |
| FR-25 | Annual policy review + periodic RA + DPIA | PROC-10, PROC-12, UC-17 | NFR-31, NFR-36 | CR-D-06.1-001 | INSPECT | HIGH | | | | | | |
| FR-26 | Monthly audit log review; retention (1y + 3y archive) | PROC-13 | NFR-13/32/33/37 | CR-D-06.1-001 | INSPECT | HIGH | | | | | | |
| FR-27 | Compliance reports on demand ≤7d; RoPA update ≤7d | PROC-14 | NFR-35/38/39/40/42/43 | CR-D-06.1-001 | TEST | HIGH | | | | | | |
| FR-28 | Annual vendor security assessments | CAP-01 | NFR-05 | CR-D-02.1-001 | INSPECT | MEDIUM | | | | | | |

### §2.6 TRN domain (FR-29..FR-30)

| FR ID | Requirement | UCs | NFRs | CR | Verif | Prio | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-------|-------------|-----|------|----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| FR-29 | Annual security awareness + role-specific training | PROC-15, PROC-16 | NFR-36 | CR-D-08.1-001 | TEST | MEDIUM | | | | | | |
| FR-30 | Quarterly phishing simulations | PROC-17 | NFR-01 | — | TEST | LOW | | | | | | |

---

### FR-01 — Register + Provision New Users [priority=HIGH, fields=17]

**Description:** System shall register new users and provision them with the appropriate role and access scope.
**Scope:** All internal staff and customer accounts.
**Out of Scope:** Service-account registration (separate mTLS flow).
**Source UC:** UC-11, UC-13
**Source NFR:** NFR-02
**Source Rule:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: PR.AA-01 | PF: —
**Verification Criteria:**
- Provisioning tested for 5 roles.
- Approval workflow enforced.
- Audit log entry.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NFR-02, NODE-SYS-006
**Risk if not met:** H — unauth'd provisioning = total compromise.
**Affected Stakeholders:** CTO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** IAM
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-01 t=fr status=TODO -->

### FR-02 — Authenticate + Lock After 5 Fails + Log [priority=HIGH, fields=17]

**Description:** System authenticates users via central IdP, locks accounts after 5 failed attempts, logs all attempts.
**Scope:** All human authentication flows.
**Out of Scope:** Service-account auth.
**Source UC:** UC-09
**Source NFR:** NFR-01..07/20/32/34
**Source Rule:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: PR.AA-01, PR.AA-03 | PF: —
**Verification Criteria:**
- Lockout after 5 fails (NFR-02).
- 30-min session timeout.
- 100% events logged (NFR-09).
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-006
**Risk if not met:** H — auth bypass = GDPR breach.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** IAM
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-02 t=fr status=TODO -->

### FR-03 — MFA for Privileged Accounts [priority=HIGH, fields=17]

**Description:** Privileged accounts shall use FIDO2-based MFA on every session.
**Scope:** Privileged staff; admins.
**Out of Scope:** Standard users.
**Source UC:** UC-12
**Source NFR:** NFR-01
**Source Rule:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: PR.AA-03, PR.AA-04, PR.AA-05 | PF: —
**Verification Criteria:**
- 100% privileged MFA.
- Session recording.
- Quarterly review.
**Verification Method:** DEMONSTRATE
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-007
**Risk if not met:** H — privileged compromise = takeover.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** IAM
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- FR-03 t=fr status=TODO -->

### FR-04 — Deprovision Accounts Within 24h of Termination [priority=HIGH, fields=17]

**Description:** Upon termination, accounts shall be deprovisioned within 24h, including all access tokens and roles.
**Scope:** All internal staff.
**Out of Scope:** External customer accounts (separate flow).
**Source UC:** PROC-07
**Source NFR:** NFR-02
**Source Rule:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: PR.AA-01 | PF: —
**Verification Criteria:**
- Deprovisioning tested <24h.
- All access tokens revoked.
- Audit log entry.
**Verification Method:** INSPECT
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-ROLE-004
**Risk if not met:** M — orphan account = insider risk.
**Affected Stakeholders:** IAM Admin, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** IAM
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-04 t=fr status=TODO -->

### FR-05 — Assign Roles Based on Job Function [priority=HIGH, fields=17]

**Description:** System shall assign roles based on documented job functions with least-privilege.
**Scope:** All internal roles.
**Out of Scope:** Customer self-service roles.
**Source UC:** UC-13
**Source NFR:** NFR-02, NFR-09
**Source Rule:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: PR.AA-01, PR.AA-03 | PF: CT.PO-P1
**Verification Criteria:**
- RBAC matrix documented.
- Quarterly review (NFR-25).
- Privilege creep detected.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-ROLE-004
**Risk if not met:** M — privilege drift = insider risk.
**Affected Stakeholders:** IAM Admin, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** IAM
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-05 t=fr status=TODO -->

### FR-06 — Password Reset + 30-min Session Timeout [priority=MEDIUM, fields=12]

**Description:** Users may reset passwords via secure flow; sessions timeout after 30 min idle.
**Scope:** All internal staff.
**Out of Scope:** Service accounts.
**Source UC:** UC-09, PROC-06
**Source NFR:** NFR-06, NFR-07
**Source Rule:** (best practice; no CR)
**NIST CSF Anchors:** CSF: PR.AA-01 | PF: —
**Verification Criteria:**
- Reset flow tested.
- 30-min timeout enforced.
- Audit log entry.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-006
**Risk if not met:** M — long session = theft risk.
**Affected Stakeholders:** CTO, Auditor
**Domain:** IAM

<!-- FR-06 t=fr status=TODO -->

### FR-07 — DSAR via Web/Email; JSON/CSV/PDF ≤30d [priority=HIGH, fields=17]

**Description:** Customer DSARs shall be accepted via web/email and answered within 30 days in JSON/CSV/PDF.
**Scope:** Authenticated DSARs from data subjects.
**Out of Scope:** Law-enforcement requests.
**Source UC:** PROC-01
**Source NFR:** NFR-21, NFR-22
**Source Rule:** CR-D-05.4-001
**NIST CSF Anchors:** CSF: PR.DS-10 | PF: PR.DS-P1
**Verification Criteria:**
- Sample 10 DSARs ≤30d.
- All declared fields exported.
- Audit log.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-014
**Risk if not met:** H — non-response = CNPD fine.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** DP
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- FR-07 t=fr status=TODO -->

### FR-08 — Erasure Request; Primary+Backup+Logs ≤30d [priority=HIGH, fields=17]

**Description:** Customer erasure requests shall delete data across primary, backup, and log stores within 30 days.
**Scope:** All personal data stores.
**Out of Scope:** Legal-hold data.
**Source UC:** UC-01
**Source NFR:** NFR-03, NFR-23
**Source Rule:** CR-D-05.3-001
**NIST CSF Anchors:** CSF: PR.DS-10, GV.SC-04 | PF: CT.DM-P4, CT.DM-P5
**Verification Criteria:**
- All stores erased ≤30d.
- Cryptographic verification (NFR-08).
- Processor cascade.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-015, NODE-PROC-003
**Risk if not met:** H — incomplete = Art. 17.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** DP
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- FR-08 t=fr status=TODO -->

### FR-09 — Data Export in Portable Format [priority=HIGH, fields=17]

**Description:** Customer data shall be exportable in JSON + CSV + PDF portable formats.
**Scope:** Customer data.
**Out of Scope:** Derived/inferred data.
**Source UC:** UC-02
**Source NFR:** NFR-04, NFR-24
**Source Rule:** CR-D-05.4-001
**NIST CSF Anchors:** CSF: PR.DS-10, PR.AA-03 | PF: CT.DM-P1, CT.DM-P6
**Verification Criteria:**
- All 3 formats generated.
- Schema documented.
- Auth + rate limit.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-014
**Risk if not met:** H — Art. 20 violation.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** DP
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- FR-09 t=fr status=TODO -->

### FR-10 — Consent Preferences + Records [priority=HIGH, fields=17]

**Description:** Customers shall be able to grant, modify, or withdraw consent per purpose; consent records immutable.
**Scope:** All processing purposes.
**Out of Scope:** Service-essential processing.
**Source UC:** UC-03
**Source NFR:** NFR-26
**Source Rule:** (consent — best practice; no CR)
**NIST CSF Anchors:** CSF: GV.PO-01 | PF: CT.DP-P4
**Verification Criteria:**
- 100% capture rate.
- Withdrawal cascade ≤7d (NFR-27).
- Audit log.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-PROC-007
**Risk if not met:** H — non-cascade = Art. 7(3).
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** DP
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- FR-10 t=fr status=TODO -->

### FR-11 — Rectification of Inaccurate Data [priority=HIGH, fields=17]

**Description:** Customer-initiated corrections shall be applied across all linked stores.
**Scope:** Customer data across stores.
**Out of Scope:** Third-party data.
**Source UC:** UC-04
**Source NFR:** NFR-08, NFR-28
**Source Rule:** CR-D-01.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02 | PF: CT.DM-P1, CT.DM-P3
**Verification Criteria:**
- All stores updated ≤30d.
- HMAC integrity preserved.
- Processor notified.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-016
**Risk if not met:** H — inaccurate = Art. 5(1)(d).
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** DP
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- FR-11 t=fr status=TODO -->

### FR-12 — Object to Processing + Restriction Request [priority=MEDIUM, fields=12]

**Description:** Customers shall be able to object to processing or request restriction within 30 days.
**Scope:** All processing purposes.
**Out of Scope:** Service-essential processing.
**Source UC:** UC-03
**Source NFR:** NFR-27, NFR-30
**Source Rule:** CR-D-05.1-001
**NIST CSF Anchors:** CSF: GV.PO-01 | PF: CT.DM-P5
**Verification Criteria:**
- Object flow tested.
- Restriction cascade ≤30d.
- Audit log.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-PROC-007
**Risk if not met:** M — Art. 18 + Art. 21 gap.
**Affected Stakeholders:** Customer, DPO, Auditor
**Domain:** DP

<!-- FR-12 t=fr status=TODO -->

### FR-13 — Collect + Correlate Security Events + Alerts [priority=HIGH, fields=17]

**Description:** SIEM shall collect and correlate security events; alert on suspicious patterns.
**Scope:** All production events.
**Out of Scope:** Dev events.
**Source UC:** PROC-03, UC-08
**Source NFR:** NFR-10, NFR-32
**Source Rule:** CR-D-02.1-001
**NIST CSF Anchors:** CSF: DE.CM-01, DE.AE-02 | PF: CT.DM-P4
**Verification Criteria:**
- ≥99.9% uptime (NFR-10).
- 100% auth events.
- Correlation rules reviewed.
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-001/002/003
**Risk if not met:** H — log loss = accountability.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** SEC
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-13 t=fr status=TODO -->

### FR-14 — Notify On-Call ≤15min; Escalate ≤15min [priority=HIGH, fields=17]

**Description:** Confirmed incidents trigger on-call notification within 15 min and escalation within 15 min.
**Scope:** All security incidents.
**Out of Scope:** Customer support.
**Source UC:** PROC-03
**Source NFR:** NFR-17
**Source Rule:** CR-D-04.1-001
**NIST CSF Anchors:** CSF: RS.CO-02, RS.MA-01 | PF: CM.AW-P7
**Verification Criteria:**
- On-call notification ≤15min.
- Escalation path tested.
- Audit log.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-PROC-001
**Risk if not met:** H — slow response = breach amplification.
**Affected Stakeholders:** Operations Lead, Incident Commander
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** SEC
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-14 t=fr status=TODO -->

### FR-15 — Contain Incident ≤4h; Preserve Evidence [priority=HIGH, fields=17]

**Description:** Incident containment within 4 hours with evidence preservation.
**Scope:** All confirmed incidents.
**Out of Scope:** Suspected-only.
**Source UC:** UC-05
**Source NFR:** NFR-09/17/32
**Source Rule:** CR-D-04.1-001
**NIST CSF Anchors:** CSF: DE.CM-09, RS.MA-01 | PF: CM.AW-P7
**Verification Criteria:**
- Containment median ≤30min.
- Evidence preserved WORM.
- Tabletop annually.
**Verification Method:** DEMONSTRATE
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-005
**Risk if not met:** H — uncontrolled exploit = breach.
**Affected Stakeholders:** Operations Lead, Incident Commander
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** SEC
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-15 t=fr status=TODO -->

### FR-16 — Regulatory Notification 24h CRA / 72h GDPR [priority=HIGH, fields=17]

**Description:** System shall notify ENISA within 24h and CNPD within 72h of qualifying incidents.
**Scope:** All confirmed security incidents.
**Out of Scope:** Suspected-only.
**Source UC:** UC-05
**Source NFR:** NFR-17/29/41/44
**Source Rule:** CR-D-04.3-001 (F-S2-02 RESOLVED)
**NIST CSF Anchors:** CSF: RS.CO-02, RS.MA-02 | PF: CM.AW-P7, CM.AW-P8
**Verification Criteria:**
- ENISA ≤24h.
- CNPD ≤72h.
- Templates pre-drafted.
**Verification Method:** TEST
**Owner:** Incident Commander
**Status:** TODO
**Dependencies:** NODE-SYS-004, NODE-ROLE-008
**Risk if not met:** H — late = dual fine.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** SEC
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-16 t=fr status=TODO -->

### FR-17 — Weekly Vulnerability Scans; Risk-Prioritised [priority=HIGH, fields=17]

**Description:** Weekly automated vulnerability scans with findings triaged by risk.
**Scope:** Production + staging.
**Out of Scope:** Dev.
**Source UC:** PROC-04
**Source NFR:** NFR-10, NFR-46
**Source Rule:** CR-D-02.1-001
**NIST CSF Anchors:** CSF: ID.RA-01, ID.RA-04 | PF: ID.RA-P3, ID.RA-P5
**Verification Criteria:**
- Weekly cadence (NFR-46).
- Findings prioritised CVSS+EPSS.
- Remediation tracked.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-PROC-017
**Risk if not met:** H — missed vuln = CRA trigger.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** SEC
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- FR-17 t=fr status=TODO -->

### FR-18 — Critical Patches ≤24h; High ≤7d [priority=HIGH, fields=17]

**Description:** Critical security patches deployed within 24h; high within 7 days.
**Scope:** Production services.
**Out of Scope:** Third-party managed.
**Source UC:** UC-06
**Source NFR:** NFR-03, NFR-12
**Source Rule:** CR-D-02.2-001
**NIST CSF Anchors:** CSF: GV.OV-02, PR.IR-03 | PF: —
**Verification Criteria:**
- Critical median ≤24h (NFR-12).
- Auto-rollback tested.
- Audit log.
**Verification Method:** INSPECT
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-PROC-015
**Risk if not met:** H — unpatched = CRA trigger.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** SEC
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- FR-18 t=fr status=TODO -->

### FR-19 — Quarterly Access Review + BCP Activation (RTO 24h) [priority=HIGH, fields=17]

**Description:** Quarterly access review + Business Continuity Plan activation within RTO 24h.
**Scope:** All internal access; BCP scope.
**Out of Scope:** Customer self-service.
**Source UC:** PROC-05, UC-08
**Source NFR:** NFR-02/14..19
**Source Rule:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: PR.AA-01, PR.IR-03 | PF: —
**Verification Criteria:**
- Quarterly review documented.
- BCP activation tested.
- RTO ≤24h (NFR-14).
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-015, NODE-PROC-003
**Risk if not met:** H — failed BCP = data loss.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** SEC
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-19 t=fr status=TODO -->

### FR-20 — SAST + Dep Vuln Scan + Secret Detection per Commit [priority=HIGH, fields=17]

**Description:** Every commit shall trigger SAST, dependency vulnerability scan, and secret detection.
**Scope:** All production repositories.
**Out of Scope:** Legacy repos without CI.
**Source UC:** PROC-08, UC-14, UC-15
**Source NFR:** NFR-05, NFR-07, NFR-12
**Source Rule:** CR-D-07.1-001
**NIST CSF Anchors:** CSF: ID.RA-04, ID.RA-05 | PF: —
**Verification Criteria:**
- 100% PRs scanned.
- Critical blocks merge.
- Secret leak alerts.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-SYS-012
**Risk if not met:** H — unscanned code = CRA Art. 13.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** DEV
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- FR-20 t=fr status=TODO -->

### FR-21 — Security Gates Before Merge; Block on Critical [priority=HIGH, fields=17]

**Description:** Security gates block merge on critical findings; documented override path.
**Scope:** All production repos.
**Out of Scope:** Throwaway experiments.
**Source UC:** UC-15
**Source NFR:** NFR-05/07/11/12
**Source Rule:** CR-D-02.1-001
**NIST CSF Anchors:** CSF: PR.PS-01, PR.PS-02 | PF: —
**Verification Criteria:**
- Critical blocks merge.
- Override signed off.
- Override rate monitored.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-SYS-012
**Risk if not met:** H — bypassed gate = unscanned code.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** DEV
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- FR-21 t=fr status=TODO -->

### FR-22 — Change Request Submission + Approval [priority=MEDIUM, fields=12]

**Description:** Production changes shall be submitted via change request with documented approval.
**Scope:** All production changes.
**Out of Scope:** Dev-only changes.
**Source UC:** UC-16
**Source NFR:** (process — no NFR)
**Source Rule:** (process; no CR)
**NIST CSF Anchors:** CSF: GV.PO-02 | PF: —
**Verification Criteria:**
- 100% changes approved.
- Emergency path documented.
- Audit log.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-PROC-014
**Risk if not met:** M — unmanaged change = outage.
**Affected Stakeholders:** Lead Developer, Operations Lead, Auditor
**Domain:** DEV

<!-- FR-22 t=fr status=TODO -->

### FR-23 — Generate SBOM per Release [priority=HIGH, fields=17]

**Description:** Every release shall generate a SBOM in CycloneDX/SPDX format published to customer portal.
**Scope:** All production releases.
**Out of Scope:** Internal tooling.
**Source UC:** PROC-09
**Source NFR:** NFR-40, NFR-45
**Source Rule:** CR-D-06.2-001 (F-S2-03 RESOLVED)
**NIST CSF Anchors:** CSF: GV.SC-02, GV.SC-03 | PF: —
**Verification Criteria:**
- SBOM per release (NFR-45).
- Format validated.
- Portal tested.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-SYS-013
**Risk if not met:** M — missing SBOM = CRA Art. 13.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** DEV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- FR-23 t=fr status=TODO -->

### FR-24 — Regulatory Notifications + Log Timestamps [priority=HIGH, fields=17]

**Description:** System shall send regulatory notifications and log timestamps immutably.
**Scope:** All confirmed incidents.
**Out of Scope:** Suspected-only.
**Source UC:** U.C.5.7.1 (legacy)
**Source NFR:** NFR-33, NFR-41, NFR-44
**Source Rule:** CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02, PR.DS-10 | PF: ID.IM-P1
**Verification Criteria:**
- 100% notifications logged.
- Timestamps WORM.
- Audit log.
**Verification Method:** TEST
**Owner:** Incident Commander
**Status:** TODO
**Dependencies:** NODE-SYS-017
**Risk if not met:** H — late = Art. 33 fine.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** GOV
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-24 t=fr status=TODO -->

### FR-25 — Annual Policy Review + Periodic RA + DPIA [priority=HIGH, fields=17]

**Description:** Annual policy review, periodic risk assessment, DPIA before high-risk launch.
**Scope:** All policies, risks, DPIAs.
**Out of Scope:** Bug fixes.
**Source UC:** PROC-10, PROC-12, UC-17
**Source NFR:** NFR-31, NFR-36
**Source Rule:** CR-D-06.1-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.PO-02 | PF: CM.PO-P1
**Verification Criteria:**
- Annual review.
- DPIA pre-launch (NFR-31).
- Risk register current.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-PROC-004, NODE-PROC-005
**Risk if not met:** M — governance gap.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** GOV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-25 t=fr status=TODO -->

### FR-26 — Monthly Audit Log Review; Retention (1y + 3y archive) [priority=HIGH, fields=17]

**Description:** Audit logs reviewed monthly; retained 1 year + 3 years archive.
**Scope:** All production logs.
**Out of Scope:** Dev logs.
**Source UC:** PROC-13
**Source NFR:** NFR-13/32/33/37
**Source Rule:** CR-D-06.1-001
**NIST CSF Anchors:** CSF: DE.CM-01, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9
**Verification Criteria:**
- Monthly review.
- Retention 1y+3y.
- WORM enforced.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-SYS-001/002
**Risk if not met:** M — log gap = accountability gap.
**Affected Stakeholders:** Compliance Manager, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** GOV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- FR-26 t=fr status=TODO -->

### FR-27 — Compliance Reports on Demand ≤7d; RoPA Update ≤7d [priority=HIGH, fields=17]

**Description:** Compliance reports available on demand within 7 days; RoPA updates within 7 days of change.
**Scope:** All compliance artefacts.
**Out of Scope:** Archived reports.
**Source UC:** PROC-14
**Source NFR:** NFR-35/38/39/40/42/43
**Source Rule:** CR-D-06.1-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08 | PF: ID.IM-P1, ID.IM-P4
**Verification Criteria:**
- Reports ≤7d.
- RoPA ≤7d update (NFR-35).
- DPO sign-off.
**Verification Method:** TEST
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-SYS-014, NODE-PROC-006
**Risk if not met:** M — outdated RoPA = Art. 30.
**Affected Stakeholders:** Compliance Manager, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Domain:** GOV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- FR-27 t=fr status=TODO -->

### FR-28 — Annual Vendor Security Assessments [priority=MEDIUM, fields=12]

**Description:** Annual security assessment of all third-party processors with personal-data access.
**Scope:** All data processors.
**Out of Scope:** Non-data vendors.
**Source UC:** CAP-01
**Source NFR:** NFR-05
**Source Rule:** CR-D-02.1-001
**NIST CSF Anchors:** CSF: GV.SC-01, GV.SC-02 | PF: ID.IM-P2
**Verification Criteria:**
- Annual assessment.
- Findings tracked.
- Remediation verified.
**Verification Method:** INSPECT
**Owner:** Procurement Lead
**Status:** TODO
**Dependencies:** NODE-PROC-011
**Risk if not met:** H — substandard = Art. 28.
**Affected Stakeholders:** Procurement Lead, Compliance Manager, Auditor
**Domain:** GOV

<!-- FR-28 t=fr status=TODO -->

### FR-29 — Annual Security Awareness + Role-Specific Training [priority=MEDIUM, fields=12]

**Description:** All staff complete annual awareness + role-specific training.
**Scope:** All staff.
**Out of Scope:** External.
**Source UC:** PROC-15, PROC-16
**Source NFR:** NFR-36
**Source Rule:** CR-D-08.1-001
**NIST CSF Anchors:** CSF: PR.AT-01, PR.AT-02 | PF: GV.AT-P1, GV.AT-P2
**Verification Criteria:**
- 100% completion (NFR-36).
- Refreshed annually.
- Quiz required.
**Verification Method:** TEST
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-PROC-018, NODE-PROC-019
**Risk if not met:** M — untrained = phishing risk.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor
**Domain:** TRN

<!-- FR-29 t=fr status=TODO -->

### FR-30 — Quarterly Phishing Simulations [priority=MEDIUM, fields=12]

**Description:** Quarterly phishing simulation; click-rate tracked; re-education for repeat offenders.
**Scope:** All staff with email.
**Out of Scope:** External.
**Source UC:** PROC-17
**Source NFR:** NFR-01
**Source Rule:** (process; no CR)
**NIST CSF Anchors:** CSF: PR.AT-01, PR.AT-02 | PF: GV.AT-P1, GV.AT-P2
**Verification Criteria:**
- Quarterly simulation.
- Click rate trend.
- Re-education.
**Verification Method:** TEST
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-PROC-018
**Risk if not met:** L — phishing = leading breach vector.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor
**Domain:** TRN

<!-- FR-30 t=fr status=TODO -->


## §3 NIST anchors (per FR)

See `NIST_ANCHORS.md` §3.2 for the full table. Summary:

| Domain | FRs with CSF anchors | FRs with PF anchors | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|--------|---------------------:|--------------------:|-------|-----------------------|----------|----------|--------------|-----------|
| IAM | 5/6 (FR-01..05) | 0/6 | | | | | | |
| DP | 6/6 (FR-07..12) | 6/6 | | | | | | |
| SEC | 7/7 (FR-13..19) | 4/7 | | | | | | |
| DEV | 3/4 (FR-20, FR-21, FR-23) | 0/4 | | | | | | |
| GOV | 4/5 (FR-25..28) | 1/5 (FR-25) | | | | | | |
| TRN | 1/2 (FR-29) | 1/2 (FR-29) | | | | | | |
| **TOTAL** | **26/30 (87%)** | **12/30 (40%)** | | | | | | |

---

## §4 Orphan rule refs (legacy → freeze)

| Orphan ref (legacy) | Closest freeze rule | Finding | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|---------------------|---------------------|---------|-------|-----------------------|----------|----------|--------------|-----------|
| FR-16 → CR-D-01.1-001 (legacy Doc 23) | CR-D-04.3-001 (notification) | F-S2-02 OPEN | | | | | | |
| FR-23 → CR-D-02.1-001 (legacy Doc 23) | CR-D-06.2-001 (SBOM) | F-S2-03 OPEN | | | | | | |

---

## §5 Cross-references

- `24_Non_Functional_Requirements.md` — NFR catalogue (46 cards)
- `13_Use_Cases_Catalog.md` §3 — UC catalogue
- `15_Requirements_Allocation.md` §2 — DN rows
- `16_Compliance_Gates_Report.md` §2 — Gate rows
- `RULE_FREEZE.md` §6 — FR freeze
- `NIST_ANCHORS.md` §3.2 — per-FR NIST
- `CORPUS_LINKAGE.md` §4 — FR-to-D-XX.Y
- `KG_CHAINS.md` §1 CH-09 — FR-29 → UC-25

---

**End of Functional Requirements (Phase 3 RICH, ADJUSTED_FIELDS, Fase de Especificação 4)**
