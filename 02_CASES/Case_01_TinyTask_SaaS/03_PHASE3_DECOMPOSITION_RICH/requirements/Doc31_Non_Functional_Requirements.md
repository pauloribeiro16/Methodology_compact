---
document_id: AEGIS-P3-RICH-24
title: Non-Functional Requirements — TinyTask SaaS (Phase 3 RICH)
phase: 3
version: 2.0
created: 2026-08-24
updated: 2026-08-24
author: Sprint 4 Executor (paulo@methodology.pt)
status: DEEP_ENRICHED
sprint: 5
deep_enrichment_date: 2026-08-24
detail_cards_count: 46
cells_count: 692
fields_per_card: 17|12|tiered
tier_distribution: "NFR cards (28 with 17 fields + 18 with 12 fields)"
sprint_role: deep_enrichment_per_card
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [11_Rules_Catalog.md, 23_Functional_Requirements.md, RULE_FREEZE.md]
outputs: [25_Risk_Analysis.md, 22_Traceability_Matrix.xlsx]
related_documents: [23_Functional_Requirements.md, RULE_FREEZE.md, NIST_ANCHORS.md, CORPUS_LINKAGE.md]
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Implementation Status, Priority, Stakeholders, Reporting]
freeze_total_nfrs: 46
reconciliation_note: "46 NFR freeze (F-00b RESOLVED); 100% measurable per §4.1 of legacy; SPRINT5 detail card fill."
sprint5_note: "Sprint 5: DEEP enrichment — 46 cards (28×17 fields + 18×12 fields) = 692 cells. Frontmatter status DEEP_ENRICHED, version 2.0."
---

# Non-Functional Requirements — TinyTask SaaS (Phase 3 RICH)

> **Status:** ADJUSTED_FIELDS (Sprint 4). 46 NFR cards freeze. Sprint 5 deep-fills the 17-field per-card schema.

---

## §1 Reconciliation Notes

Non-Functional Requirements (NFR-01..NFR-46) specify measurable quality attributes (confidentiality, integrity, availability, privacy, accountability, compliance) for the TinyTask platform. All 46 NFRs are 100% measurable per legacy §4.1.

**Authoritative sources:**
- `RULE_FREEZE.md` §7 — 46 NFR freeze.
- `NIST_ANCHORS.md` §3.3 — per-NFR NIST CSF 2.0 + PF 1.0.
- `CORPUS_LINKAGE.md` §5 — NFR-to-D-XX.Y mapping.

**Family breakdown (per legacy Doc 24 §3):**

| Family | Count | Notes | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|--------|------:|-------|-------|-----------------------|----------|----------|--------------|-----------|
| CONF (Confidentiality) | 9 | Encryption + access control measurables | | | | | | |
| AVAIL (Availability) | 7 | RTO/RPO targets | | | | | | |
| INT (Integrity) | 8 | Hash, MAC, backup integrity | | | | | | |
| PRIV (Privacy) | 11 | DSAR, consent, retention | | | | | | |
| ACC (Accountability) | 6 | Audit, RoPA, breach records | | | | | | |
| COMP (Compliance) | 5 | Policy review, training | | | | | | |
| **TOTAL** | **46** | 100% measurable | | | | | | |

---

## §2 NFR Catalogue (46 cards)

> **Format:** `NFR-NN | Family | Measurable criterion | Target value | Linked FRs | Source CR | D-sub`
> Card detail (17-field schema) fills in Sprint 5.

### §2.1 CONF (Confidentiality) — NFR-01..NFR-09

| NFR | Criterion | Target | FRs | CR | D | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-----|-----------|--------|-----|----|---|-------|-----------------------|----------|----------|--------------|-----------|
| NFR-01 | Privileged session MFA success rate | 100% | FR-03 | CR-D-03.1-001 | D-01.1 | | | | | | |
| NFR-02 | Account lockout after failed attempts | 5 | FR-02, FR-04, FR-05 | CR-D-03.1-001 | D-01.1 | | | | | | |
| NFR-03 | Personal data encrypted at rest (AES-256+) | 100% of records | FR-08, FR-18 | CR-D-01.1-001 | D-01.1 | | | | | | |
| NFR-04 | TLS 1.2+ for all data in transit | 100% of endpoints | FR-02, FR-09 | CR-D-01.2-001 | D-01.2 | | | | | | |
| NFR-05 | TLS for service-to-service communication | 100% | FR-20, FR-21, FR-28 | CR-D-01.2-001 | D-01.2 | | | | | | |
| NFR-06 | HMAC integrity on critical records | 100% | FR-06 | CR-D-01.4-001 | D-01.4 | | | | | | |
| NFR-07 | Backup integrity verification (weekly) | 100% | FR-06, FR-20, FR-21 | CR-D-01.4-001 | D-01.4 | | | | | | |
| NFR-08 | Cryptographic erasure verification | 100% | FR-11 | CR-D-05.3-001 | D-05.3 | | | | | | |
| NFR-09 | Session logging coverage | 100% | FR-02, FR-05, FR-15 | CR-D-03.1-001 | D-05.3 | | | | | | |

### §2.2 AVAIL (Availability) — NFR-10..NFR-16

| NFR | Criterion | Target | FRs | CR | D | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-----|-----------|--------|-----|----|---|-------|-----------------------|----------|----------|--------------|-----------|
| NFR-10 | SIEM uptime | ≥99.9% | FR-13, FR-17 | CR-D-02.1-001 | D-04.2 | | | | | | |
| NFR-11 | CI/CD build availability | ≥99.5% | FR-21 | CR-D-02.1-001 | D-09.1 | | | | | | |
| NFR-12 | Patch deployment SLA — critical | ≤24h | FR-18, FR-20, FR-21 | CR-D-02.2-001 | D-02.2 | | | | | | |
| NFR-13 | Audit log query SLA | ≤5s p95 | FR-26 | CR-D-10.2-001 | D-04.2 | | | | | | |
| NFR-14 | Backup restore time (RTO) | ≤24h | FR-19 | CR-D-04.4-001 | D-04.4 | | | | | | |
| NFR-15 | Data loss tolerance (RPO) | ≤1h | FR-19 | CR-D-04.4-001 | D-04.4 | | | | | | |
| NFR-16 | BCP activation time | ≤24h | FR-19 | CR-D-04.4-001 | D-04.4 | | | | | | |
| NFR-17 | Alert response SLA — on-call | ≤15min | FR-14, FR-15, FR-16, FR-19 | CR-D-04.1-001 | D-04.2 | | | | | | |

### §2.3 INT (Integrity) — NFR-17..NFR-24

| NFR | Criterion | Target | FRs | CR | D | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-----|-----------|--------|-----|----|---|-------|-----------------------|----------|----------|--------------|-----------|
| NFR-18 | Forensic evidence retention | ≥1 year | FR-19 | CR-D-04.4-001 | D-04.4 | | | | | | |
| NFR-19 | Backup retention | ≥90 days | FR-19 | CR-D-04.4-001 | D-04.4 | | | | | | |
| NFR-20 | Database transaction integrity (ACID) | 100% | FR-02 | CR-D-01.4-001 | D-01.4 | | | | | | |
| NFR-21 | DSAR report completeness | 100% of fields | FR-07 | CR-D-05.4-001 | D-05.4 | | | | | | |
| NFR-22 | DSAR report generation time | ≤30 days | FR-07 | CR-D-05.4-001 | D-05.4 | | | | | | |
| NFR-23 | Erasure verification audit | 100% | FR-08 | CR-D-05.3-001 | D-05.3 | | | | | | |
| NFR-24 | Data export format portability | JSON + CSV + PDF | FR-09 | CR-D-05.4-001 | D-05.4 | | | | | | |

### §2.4 PRIV (Privacy) — NFR-25..NFR-35

| NFR | Criterion | Target | FRs | CR | D | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-----|-----------|--------|-----|----|---|-------|-----------------------|----------|----------|--------------|-----------|
| NFR-25 | RBAC role review cadence | Quarterly | FR-05 | CR-D-03.3-001 | D-03.3 | | | | | | |
| NFR-26 | Consent capture rate | 100% | FR-10 | CR-D-05.1-001 | D-05.1 | | | | | | |
| NFR-27 | Consent withdrawal response time | ≤7 days | FR-12 | CR-D-05.2-001 | D-05.2 | | | | | | |
| NFR-28 | Rectification SLA | ≤30 days | FR-11 | CR-D-05.4-001 | D-05.4 | | | | | | |
| NFR-29 | Breach notification SLA (GDPR) | ≤72h | FR-16 | CR-D-04.3-001 | D-04.3 | | | | | | |
| NFR-30 | Object-to-processing SLA | ≤30 days | FR-12 | CR-D-05.1-001 | D-05.1 | | | | | | |
| NFR-31 | DPIA completion before high-risk launch | 100% | FR-25 | CR-D-09.2-001 | D-09.2 | | | | | | |
| NFR-32 | Audit log immutability | WORM storage | FR-02, FR-15, FR-26 | CR-D-10.2-001 | D-10.2 | | | | | | |
| NFR-33 | Regulatory communication logging | 100% | FR-24, FR-26 | CR-D-09.4-001 | D-09.4 | | | | | | |
| NFR-34 | Strong cipher usage | TLS 1.3 / AES-256 | FR-02 | CR-D-01.2-001 | D-01.2 | | | | | | |
| NFR-35 | Records of Processing Activities update | ≤7 days | FR-27 | CR-D-09.4-001 | D-09.4 | | | | | | |

### §2.5 ACC (Accountability) — NFR-36..NFR-41

| NFR | Criterion | Target | FRs | CR | D | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-----|-----------|--------|-----|----|---|-------|-----------------------|----------|----------|--------------|-----------|
| NFR-36 | Training completion rate | 100% | FR-25, FR-29 | CR-D-08.1-001 | D-09.1 | | | | | | |
| NFR-37 | Audit log retention | ≥12 months | FR-26 | CR-D-10.2-001 | D-10.2 | | | | | | |
| NFR-38 | Policy review cadence | Annual | FR-27 | CR-D-09.1-001 | D-09.1 | | | | | | |
| NFR-39 | Data minimisation review | Annual | FR-27 | CR-D-05.1-001 | D-09.1 | | | | | | |
| NFR-40 | Vendor security assessment | Annual | FR-23, FR-27 | CR-D-09.1-001 | D-09.1 | | | | | | |
| NFR-41 | Risk assessment cadence | Pre-launch + annual | FR-16, FR-24 | CR-D-09.2-001 | D-09.2 | | | | | | |

### §2.6 COMP (Compliance) — NFR-42..NFR-46

| NFR | Criterion | Target | FRs | CR | D | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-----|-----------|--------|-----|----|---|-------|-----------------------|----------|----------|--------------|-----------|
| NFR-42 | Compliance report generation | ≤7 days on demand | FR-27 | CR-D-09.1-001 | D-09.1 | | | | | | |
| NFR-43 | Breach register SLA (entry) | ≤24h post-detection | FR-27 | CR-D-09.4-001 | D-09.4 | | | | | | |
| NFR-44 | ENISA notification SLA (CRA) | ≤24h | FR-16, FR-24 | CR-D-04.3-001 | D-04.3 | | | | | | |
| NFR-45 | SBOM publication | Per release | FR-23 | CR-D-06.2-001 | D-06.2 | | | | | | |
| NFR-46 | Vulnerability scan cadence | Weekly | FR-17 | CR-D-02.1-001 | D-02.1 | | | | | | |

---

### NFR-01 — Privileged Session MFA Success Rate [priority=HIGH, fields=17]

**Description:** 100% of privileged sessions successfully use MFA.
**Scope:** Privileged staff sessions.
**Out of Scope:** Standard user sessions.
**Source UC:** U.C.3.1.2
**Source FR:** FR-03
**Source Rule:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: PR.AA-03, PR.AA-04 | PF: —
**Measurement Criteria:**
- 100% success measured monthly.
- Audit log.
- Quarterly report.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-007
**Risk if not met:** H — privileged compromise = takeover.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** CONF
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- NFR-01 t=nfr status=TODO family=CONF -->

### NFR-02 — Account Lockout After Failed Attempts [priority=HIGH, fields=17]

**Description:** Account locked after 5 failed authentication attempts.
**Scope:** All human authentication.
**Out of Scope:** Service accounts.
**Source UC:** U.C.3.1.1, U.C.3.2.1, U.C.3.5.1
**Source FR:** FR-02, FR-04, FR-05
**Source Rule:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: PR.AA-01, PR.AA-03 | PF: —
**Measurement Criteria:**
- Lockout after 5 fails.
- Audit log entry.
- Reset procedure documented.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-006
**Risk if not met:** H — credential stuffing.
**Affected Stakeholders:** Customer, CTO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** CONF
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NFR-02 t=nfr status=TODO family=CONF -->

### NFR-03 — Personal Data Encrypted at Rest (AES-256+) [priority=HIGH, fields=17]

**Description:** 100% of personal-data records encrypted at rest with AES-256 or higher.
**Scope:** Production data stores.
**Out of Scope:** Ephemeral dev databases.
**Source UC:** U.C.1.1.1, U.C.2.6.1
**Source FR:** FR-08, FR-18
**Source Rule:** CR-D-01.1-001
**NIST CSF Anchors:** CSF: PR.DS-01 | PF: PR.DS-P1
**Measurement Criteria:**
- 100% stores encrypted.
- Algorithm = AES-256-GCM.
- KMS-managed keys.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-010
**Risk if not met:** H — unencrypted = GDPR Art. 32.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** CONF
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-03 t=nfr status=TODO family=CONF -->

### NFR-04 — TLS 1.2+ for All Data in Transit [priority=HIGH, fields=17]

**Description:** 100% of data-in-transit endpoints use TLS 1.2+.
**Scope:** All public endpoints.
**Out of Scope:** Internal mTLS.
**Source UC:** U.C.3.1.1, U.C.1.3.1
**Source FR:** FR-02, FR-09
**Source Rule:** CR-D-01.2-001
**NIST CSF Anchors:** CSF: PR.DS-02 | PF: CT.DM-P1
**Measurement Criteria:**
- 100% endpoints TLS 1.2+.
- HSTS enabled.
- Cipher suite pinned.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-011
**Risk if not met:** H — weak TLS = transit breach.
**Affected Stakeholders:** Customer, CTO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** CONF
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-04 t=nfr status=TODO family=CONF -->

### NFR-05 — TLS for Service-to-Service Communication [priority=MEDIUM, fields=12]

**Description:** 100% of internal service-to-service traffic uses TLS.
**Scope:** Internal microservices.
**Out of Scope:** Dev traffic.
**Source UC:** U.C.4.1.1, U.C.4.2.1, U.C.4.3.1, U.C.5.5.1
**Source FR:** FR-20, FR-21, FR-28
**Source Rule:** CR-D-01.2-001
**NIST CSF Anchors:** CSF: PR.DS-02 | PF: —
**Measurement Criteria:**
- 100% internal TLS.
- mTLS where feasible.
- Cert rotation annual.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-SYS-011
**Risk if not met:** M — internal sniffing.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Family:** CONF
**Privacy Flag:** non-PRIV

<!-- NFR-05 t=nfr status=TODO family=CONF -->

### NFR-06 — HMAC Integrity on Critical Records [priority=HIGH, fields=17]

**Description:** 100% of critical records carry HMAC integrity verification.
**Scope:** Production critical records.
**Out of Scope:** Cache / derived.
**Source UC:** U.C.1.1.2
**Source FR:** FR-11
**Source Rule:** CR-D-01.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02 | PF: CT.DM-P1, CT.DM-P3
**Measurement Criteria:**
- 100% critical records covered.
- Algorithm = HMAC-SHA-256.
- Tamper logs in SIEM.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-016
**Risk if not met:** H — undetected tampering.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** CONF
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-06 t=nfr status=TODO family=CONF -->

### NFR-07 — Backup Integrity Verification (Weekly) [priority=MEDIUM, fields=12]

**Description:** 100% of backups verified for integrity weekly.
**Scope:** Production backups.
**Out of Scope:** Dev backups.
**Source UC:** U.C.4.1.1, U.C.4.2.1, U.C.4.3.1
**Source FR:** FR-06, FR-20, FR-21
**Source Rule:** CR-D-01.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02 | PF: —
**Measurement Criteria:**
- Weekly verification.
- Restore test quarterly.
- Audit log.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-015
**Risk if not met:** H — corrupted backup = data loss.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Family:** CONF
**Privacy Flag:** non-PRIV

<!-- NFR-07 t=nfr status=TODO family=CONF -->

### NFR-08 — Cryptographic Erasure Verification [priority=HIGH, fields=17]

**Description:** 100% of erasure operations verified cryptographically per NIST SP 800-88.
**Scope:** All erasure flows.
**Out of Scope:** Logical-only deletes (not NIST).
**Source UC:** U.C.1.1.2
**Source FR:** FR-11
**Source Rule:** CR-D-05.3-001
**NIST CSF Anchors:** CSF: GV.SC-04, PR.DS-10 | PF: CT.DM-P4, CT.DM-P5
**Measurement Criteria:**
- 100% erasure verified.
- Audit log.
- Processor cascade.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-015
**Risk if not met:** H — incomplete = Art. 17.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** CONF
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-08 t=nfr status=TODO family=CONF -->

### NFR-09 — Session Logging Coverage [priority=MEDIUM, fields=12]

**Description:** 100% of user sessions logged to SIEM.
**Scope:** All production sessions.
**Out of Scope:** Dev sessions.
**Source UC:** U.C.3.1.1, U.C.3.2.1, U.C.3.5.1
**Source FR:** FR-02, FR-05, FR-15
**Source Rule:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: DE.CM-01, PR.DS-01 | PF: CT.DM-P4
**Measurement Criteria:**
- 100% sessions logged.
- Audit log.
- Quarterly review.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-001
**Risk if not met:** H — log gap = accountability.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Family:** CONF
**Privacy Flag:** non-PRIV

<!-- NFR-09 t=nfr status=TODO family=CONF -->

### NFR-10 — SIEM Uptime [priority=HIGH, fields=17]

**Description:** SIEM platform uptime ≥99.9%.
**Scope:** Production SIEM.
**Out of Scope:** Dev SIEM.
**Source UC:** U.C.2.1.1, U.C.2.6.1
**Source FR:** FR-13, FR-17
**Source Rule:** CR-D-02.1-001
**NIST CSF Anchors:** CSF: DE.CM-01 | PF: CT.DM-P4
**Measurement Criteria:**
- ≥99.9% measured monthly.
- Audit log.
- Runbook for outage.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-001
**Risk if not met:** H — log loss = accountability.
**Affected Stakeholders:** Operations Lead, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** AVAIL
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NFR-10 t=nfr status=TODO family=AVAIL -->

### NFR-11 — CI/CD Build Availability [priority=MEDIUM, fields=12]

**Description:** CI/CD build pipeline availability ≥99.5%.
**Scope:** Production CI/CD.
**Out of Scope:** Dev CI/CD.
**Source UC:** U.C.4.3.1
**Source FR:** FR-21
**Source Rule:** CR-D-02.1-001
**NIST CSF Anchors:** CSF: PR.PS-01, PR.PS-02 | PF: —
**Measurement Criteria:**
- ≥99.5% measured monthly.
- Runbook for outage.
- Audit log.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-SYS-012
**Risk if not met:** M — pipeline down = deploy delays.
**Affected Stakeholders:** Lead Developer, Auditor
**Family:** AVAIL
**Privacy Flag:** non-PRIV

<!-- NFR-11 t=nfr status=TODO family=AVAIL -->

### NFR-12 — Patch Deployment SLA — Critical [priority=HIGH, fields=17]

**Description:** Critical security patches deployed within 24 hours.
**Scope:** Production services.
**Out of Scope:** Third-party managed.
**Source UC:** U.C.4.3.1, U.C.4.1.1, U.C.4.2.1
**Source FR:** FR-18, FR-20, FR-21
**Source Rule:** CR-D-02.2-001
**NIST CSF Anchors:** CSF: GV.OV-02, PR.IR-03 | PF: —
**Measurement Criteria:**
- Median ≤24h measured monthly.
- Audit log.
- Remediation tracked.
**Verification Method:** INSPECT
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-PROC-015
**Risk if not met:** H — unpatched = CRA Art. 14.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** AVAIL
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- NFR-12 t=nfr status=TODO family=AVAIL -->

### NFR-13 — Audit Log Query SLA [priority=MEDIUM, fields=12]

**Description:** Audit log queries return within 5s at p95.
**Scope:** Production audit log store.
**Out of Scope:** Dev queries.
**Source UC:** U.C.5.3.1
**Source FR:** FR-26
**Source Rule:** CR-D-10.2-001
**NIST CSF Anchors:** CSF: DE.CM-01 | PF: CT.DM-P4
**Measurement Criteria:**
- p95 ≤5s measured monthly.
- Index tuning annual.
- Audit log.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-002
**Risk if not met:** M — slow queries = forensic gap.
**Affected Stakeholders:** Operations Lead, Compliance Manager, Auditor
**Family:** AVAIL
**Privacy Flag:** non-PRIV

<!-- NFR-13 t=nfr status=TODO family=AVAIL -->

### NFR-14 — Backup Restore Time (RTO) [priority=HIGH, fields=17]

**Description:** Backup restoration completes within 24h (RTO).
**Scope:** Production data stores.
**Out of Scope:** Long-term archival.
**Source UC:** U.C.2.5.1, U.C.2.6.1
**Source FR:** FR-19
**Source Rule:** CR-D-04.4-001
**NIST CSF Anchors:** CSF: PR.IR-03 | PF: —
**Measurement Criteria:**
- RTO ≤24h quarterly drill.
- Audit log.
- Runbook signed off.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-015, NODE-PROC-003
**Risk if not met:** H — failed restore = data loss.
**Affected Stakeholders:** Operations Lead, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** AVAIL
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NFR-14 t=nfr status=TODO family=AVAIL -->

### NFR-15 — Data Loss Tolerance (RPO) [priority=HIGH, fields=17]

**Description:** Maximum data loss tolerance is 1 hour (RPO).
**Scope:** Production data stores.
**Out of Scope:** Long-term archival.
**Source UC:** U.C.2.5.1, U.C.2.6.1
**Source FR:** FR-19
**Source Rule:** CR-D-04.4-001
**NIST CSF Anchors:** CSF: PR.DS-10, PR.IR-03 | PF: —
**Measurement Criteria:**
- RPO ≤1h quarterly drill.
- Continuous replication.
- Audit log.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-015, NODE-PROC-003
**Risk if not met:** H — exceeds RPO = data loss.
**Affected Stakeholders:** Operations Lead, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** AVAIL
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NFR-15 t=nfr status=TODO family=AVAIL -->

### NFR-16 — BCP Activation Time [priority=MEDIUM, fields=12]

**Description:** BCP activation completes within 24h.
**Scope:** BCP scope.
**Out of Scope:** DR-only incidents.
**Source UC:** U.C.2.5.1, U.C.2.6.1
**Source FR:** FR-19
**Source Rule:** CR-D-04.4-001
**NIST CSF Anchors:** CSF: PR.IR-01, PR.IR-03 | PF: —
**Measurement Criteria:**
- BCP activation ≤24h.
- Annual test.
- Audit log.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-PROC-003
**Risk if not met:** H — BCP gap = prolonged outage.
**Affected Stakeholders:** Operations Lead, CEO, Auditor
**Family:** AVAIL
**Privacy Flag:** non-PRIV

<!-- NFR-16 t=nfr status=TODO family=AVAIL -->

### NFR-17 — Alert Response SLA — On-Call [priority=HIGH, fields=17]

**Description:** On-call alert response within 15 minutes.
**Scope:** All security incidents.
**Out of Scope:** Customer support.
**Source UC:** U.C.2.1.1, U.C.2.2.1, U.C.2.5.1, U.C.2.6.1
**Source FR:** FR-14, FR-15, FR-16, FR-19
**Source Rule:** CR-D-04.1-001
**NIST CSF Anchors:** CSF: RS.CO-02, RS.MA-01 | PF: CM.AW-P7
**Measurement Criteria:**
- Median ≤15min measured monthly.
- Escalation path tested.
- Audit log.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-001
**Risk if not met:** H — slow response = breach amplification.
**Affected Stakeholders:** Operations Lead, Incident Commander
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** AVAIL
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NFR-17 t=nfr status=TODO family=AVAIL -->

### NFR-18 — Forensic Evidence Retention [priority=HIGH, fields=17]

**Description:** Forensic evidence retained for ≥1 year.
**Scope:** All confirmed security incidents.
**Out of Scope:** Suspected-only.
**Source UC:** U.C.2.5.1, U.C.2.6.1
**Source FR:** FR-19
**Source Rule:** CR-D-04.4-001
**NIST CSF Anchors:** CSF: PR.DS-10, PR.IR-04 | PF: —
**Measurement Criteria:**
- ≥1y retention measured quarterly.
- Audit log.
- WORM enforced.
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-002
**Risk if not met:** M — premature deletion = investigation gap.
**Affected Stakeholders:** Operations Lead, Compliance Manager, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** INT
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NFR-18 t=nfr status=TODO family=INT -->

### NFR-19 — Backup Retention [priority=MEDIUM, fields=12]

**Description:** Backup data retained for ≥90 days.
**Scope:** Production data stores.
**Out of Scope:** Dev backups.
**Source UC:** U.C.2.5.1, U.C.2.6.1
**Source FR:** FR-19
**Source Rule:** CR-D-04.4-001
**NIST CSF Anchors:** CSF: PR.DS-10 | PF: —
**Measurement Criteria:**
- ≥90-day retention.
- Audit log.
- Monthly review.
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-015
**Risk if not met:** M — insufficient retention.
**Affected Stakeholders:** Operations Lead, Auditor
**Family:** INT
**Privacy Flag:** non-PRIV

<!-- NFR-19 t=nfr status=TODO family=INT -->

### NFR-20 — Database Transaction Integrity (ACID) [priority=HIGH, fields=17]

**Description:** 100% of database transactions satisfy ACID properties.
**Scope:** Production data stores.
**Out of Scope:** Dev databases.
**Source UC:** U.C.3.1.1
**Source FR:** FR-02
**Source Rule:** CR-D-01.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02 | PF: CT.DM-P1
**Measurement Criteria:**
- 100% ACID verified.
- Chaos test annually.
- Audit log.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-010
**Risk if not met:** H — data corruption.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** INT
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-20 t=nfr status=TODO family=INT -->

### NFR-21 — DSAR Report Completeness [priority=HIGH, fields=17]

**Description:** 100% of DSAR reports include all declared fields.
**Scope:** All DSAR responses.
**Out of Scope:** Suspected-only.
**Source UC:** U.C.1.1.1
**Source FR:** FR-07
**Source Rule:** CR-D-05.4-001
**NIST CSF Anchors:** CSF: PR.DS-10 | PF: PR.DS-P1
**Measurement Criteria:**
- Field completeness checked per DSAR.
- Audit log.
- Quarterly review.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-014
**Risk if not met:** H — incomplete DSAR = Art. 15.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** INT
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-21 t=nfr status=TODO family=INT -->

### NFR-22 — DSAR Report Generation Time [priority=HIGH, fields=17]

**Description:** DSAR reports generated within 30 days.
**Scope:** All DSAR requests.
**Out of Scope:** Suspected-only.
**Source UC:** U.C.1.1.1
**Source FR:** FR-07
**Source Rule:** CR-D-05.4-001
**NIST CSF Anchors:** CSF: PR.DS-10 | PF: PR.DS-P1
**Measurement Criteria:**
- ≤30 days measured monthly.
- Audit log.
- Quarterly review.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-014
**Risk if not met:** H — late DSAR = Art. 12(3).
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** INT
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-22 t=nfr status=TODO family=INT -->

### NFR-23 — Erasure Verification Audit [priority=HIGH, fields=17]

**Description:** 100% of erasure operations audited.
**Scope:** All erasure flows.
**Out of Scope:** Logical-only deletes.
**Source UC:** U.C.1.2.1
**Source FR:** FR-08
**Source Rule:** CR-D-05.3-001
**NIST CSF Anchors:** CSF: GV.SC-04 | PF: CT.DM-P4, CT.DM-P5
**Measurement Criteria:**
- 100% audit coverage.
- Audit log.
- Quarterly review.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-015, NODE-PROC-003
**Risk if not met:** H — unverified erasure = Art. 17.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** INT
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-23 t=nfr status=TODO family=INT -->

### NFR-24 — Data Export Format Portability [priority=MEDIUM, fields=12]

**Description:** Data exports support JSON + CSV + PDF formats.
**Scope:** All DSAR exports.
**Out of Scope:** Proprietary formats.
**Source UC:** U.C.1.3.1
**Source FR:** FR-09
**Source Rule:** CR-D-05.4-001
**NIST CSF Anchors:** CSF: PR.DS-10 | PF: CT.DM-P1, CT.DM-P6
**Measurement Criteria:**
- All 3 formats supported.
- Sample exports validated.
- Audit log.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-014
**Risk if not met:** M — Art. 20 gap.
**Affected Stakeholders:** Customer, DPO, Auditor
**Family:** INT
**Privacy Flag:** PRIV

<!-- NFR-24 t=nfr status=TODO family=INT -->

### NFR-25 — RBAC Role Review Cadence [priority=HIGH, fields=17]

**Description:** RBAC role reviews conducted quarterly.
**Scope:** All internal staff.
**Out of Scope:** Customer self-service.
**Source UC:** U.C.3.2.1
**Source FR:** FR-05
**Source Rule:** CR-D-03.3-001
**NIST CSF Anchors:** CSF: PR.AA-01, PR.AA-03 | PF: CT.PO-P1
**Measurement Criteria:**
- Quarterly review documented.
- Audit log.
- Privilege creep detected.
**Verification Method:** INSPECT
**Owner:** IAM Admin
**Status:** TODO
**Dependencies:** NODE-ROLE-004
**Risk if not met:** M — privilege drift = insider risk.
**Affected Stakeholders:** IAM Admin, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** PRIV
**Privacy Flag:** PRIV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NFR-25 t=nfr status=TODO family=PRIV -->

### NFR-26 — Consent Capture Rate [priority=HIGH, fields=17]

**Description:** 100% of new users have consent captured at signup.
**Scope:** All new user signups.
**Out of Scope:** Legacy users (separate migration).
**Source UC:** U.C.1.4.1
**Source FR:** FR-10
**Source Rule:** CR-D-05.1-001
**NIST CSF Anchors:** CSF: GV.PO-01 | PF: CT.DP-P4
**Measurement Criteria:**
- 100% capture rate.
- Audit log.
- Quarterly review.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-PROC-007
**Risk if not met:** H — uncaptured consent = Art. 6.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** PRIV
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-26 t=nfr status=TODO family=PRIV -->

### NFR-27 — Consent Withdrawal Response Time [priority=HIGH, fields=17]

**Description:** Consent withdrawal propagated to processors within 7 days.
**Scope:** All processors.
**Out of Scope:** Aggregated anonymised.
**Source UC:** U.C.1.4.1
**Source FR:** FR-12
**Source Rule:** CR-D-05.2-001
**NIST CSF Anchors:** CSF: GV.PO-02 | PF: CT.DM-P5
**Measurement Criteria:**
- ≤7 days measured monthly.
- Audit log.
- Quarterly review.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-PROC-007
**Risk if not met:** H — non-cascade = Art. 7(3).
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** PRIV
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-27 t=nfr status=TODO family=PRIV -->

### NFR-28 — Rectification SLA [priority=HIGH, fields=17]

**Description:** Customer rectification requests applied within 30 days.
**Scope:** All customer data stores.
**Out of Scope:** Third-party data.
**Source UC:** U.C.1.5.1
**Source FR:** FR-11
**Source Rule:** CR-D-05.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02 | PF: CT.DM-P1, CT.DM-P3
**Measurement Criteria:**
- ≤30 days measured monthly.
- Audit log.
- Quarterly review.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-016
**Risk if not met:** H — late = Art. 16.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** PRIV
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-28 t=nfr status=TODO family=PRIV -->

### NFR-29 — Breach Notification SLA (GDPR) [priority=HIGH, fields=17]

**Description:** Personal-data breach notifications to CNPD within 72 hours.
**Scope:** All confirmed personal-data breaches.
**Out of Scope:** Suspected-only.
**Source UC:** U.C.2.5.1
**Source FR:** FR-16
**Source Rule:** CR-D-04.3-001
**NIST CSF Anchors:** CSF: RS.CO-02 | PF: CM.AW-P7
**Measurement Criteria:**
- ≤72h measured per incident.
- Audit log.
- Tabletop annually.
**Verification Method:** DEMONSTRATE
**Owner:** Incident Commander
**Status:** TODO
**Dependencies:** NODE-SYS-004, NODE-ROLE-008
**Risk if not met:** H — late = Art. 83 fine.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** PRIV
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-29 t=nfr status=TODO family=PRIV -->

### NFR-30 — Object-to-Processing SLA [priority=HIGH, fields=17]

**Description:** Customer object-to-processing requests handled within 30 days.
**Scope:** All customer object requests.
**Out of Scope:** Suspected-only.
**Source UC:** U.C.1.4.1
**Source FR:** FR-12
**Source Rule:** CR-D-05.1-001
**NIST CSF Anchors:** CSF: GV.PO-02 | PF: CT.DM-P5
**Measurement Criteria:**
- ≤30 days measured monthly.
- Audit log.
- Quarterly review.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-PROC-007
**Risk if not met:** H — late = Art. 21 violation.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** PRIV
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-30 t=nfr status=TODO family=PRIV -->

### NFR-31 — DPIA Completion Before High-Risk Launch [priority=HIGH, fields=17]

**Description:** 100% of high-risk features complete DPIA before launch.
**Scope:** All new high-risk features.
**Out of Scope:** Bug fixes.
**Source UC:** U.C.5.2.1
**Source FR:** FR-25
**Source Rule:** CR-D-09.2-001
**NIST CSF Anchors:** CSF: ID.RA-01 | PF: ID.RA-P3, ID.RA-P4
**Measurement Criteria:**
- 100% DPIA pre-launch.
- Risk Owner sign-off.
- Audit log.
**Verification Method:** DEMONSTRATE
**Owner:** Risk Owner
**Status:** TODO
**Dependencies:** NODE-PROC-005, NODE-ROLE-006
**Risk if not met:** H — missing DPIA = Art. 35.
**Affected Stakeholders:** Risk Owner, DPO, Compliance Manager, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** PRIV
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-31 t=nfr status=TODO family=PRIV -->

### NFR-32 — Audit Log Immutability [priority=MEDIUM, fields=12]

**Description:** Audit logs stored in WORM (Write-Once-Read-Many) storage.
**Scope:** Production audit logs.
**Out of Scope:** Dev logs.
**Source UC:** U.C.3.1.1, U.C.2.2.1, U.C.5.3.1
**Source FR:** FR-02, FR-15, FR-26
**Source Rule:** CR-D-10.2-001
**NIST CSF Anchors:** CSF: PR.DS-01 | PF: CT.DM-P4, CT.DM-P9
**Measurement Criteria:**
- WORM enforced.
- Tamper-evidence quarterly.
- Audit log.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-002
**Risk if not met:** H — log tampering = Art. 5(1)(f).
**Affected Stakeholders:** Compliance Manager, CTO, Auditor
**Family:** PRIV
**Privacy Flag:** PRIV

<!-- NFR-32 t=nfr status=TODO family=PRIV -->

### NFR-33 — Regulatory Communication Logging [priority=MEDIUM, fields=12]

**Description:** 100% of regulatory communications logged.
**Scope:** All regulatory communications.
**Out of Scope:** Customer support.
**Source UC:** U.C.5.3.1, U.C.2.5.1
**Source FR:** FR-24, FR-26
**Source Rule:** CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02 | PF: ID.IM-P1
**Measurement Criteria:**
- 100% logged.
- Audit log.
- Monthly review.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-SYS-017
**Risk if not met:** M — untracked communications.
**Affected Stakeholders:** Compliance Manager, DPO, Auditor
**Family:** PRIV
**Privacy Flag:** non-PRIV

<!-- NFR-33 t=nfr status=TODO family=PRIV -->

### NFR-34 — Strong Cipher Usage [priority=MEDIUM, fields=12]

**Description:** System uses TLS 1.3 / AES-256 strong ciphers.
**Scope:** All data flows.
**Out of Scope:** Legacy weak ciphers.
**Source UC:** U.C.3.1.1
**Source FR:** FR-02
**Source Rule:** CR-D-01.2-001
**NIST CSF Anchors:** CSF: PR.DS-02 | PF: CT.DM-P1
**Measurement Criteria:**
- Strong cipher policy enforced.
- Weak ciphers disabled.
- Audit log.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-011
**Risk if not met:** M — weak cipher risk.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Family:** PRIV
**Privacy Flag:** non-PRIV

<!-- NFR-34 t=nfr status=TODO family=PRIV -->

### NFR-35 — Records of Processing Activities Update [priority=HIGH, fields=17]

**Description:** RoPA updated within 7 days of any processing change.
**Scope:** All processing activities.
**Out of Scope:** Anonymised.
**Source UC:** U.C.5.4.1
**Source FR:** FR-27
**Source Rule:** CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08 | PF: ID.IM-P1, ID.IM-P4
**Measurement Criteria:**
- ≤7 days measured per change.
- DPO sign-off.
- Audit log.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-014, NODE-PROC-006
**Risk if not met:** H — outdated RoPA = Art. 30.
**Affected Stakeholders:** Compliance Manager, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** PRIV
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-35 t=nfr status=TODO family=PRIV -->

### NFR-36 — Training Completion Rate [priority=HIGH, fields=17]

**Description:** 100% of staff complete assigned training.
**Scope:** All staff.
**Out of Scope:** External.
**Source UC:** U.C.6.1.1, U.C.6.2.1
**Source FR:** FR-29
**Source Rule:** CR-D-08.1-001
**NIST CSF Anchors:** CSF: PR.AT-01, PR.AT-02 | PF: GV.AT-P1, GV.AT-P2
**Measurement Criteria:**
- 100% completion.
- Refreshed annually.
- Audit log.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-PROC-018, NODE-PROC-019
**Risk if not met:** M — untrained = phishing risk.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** ACC
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NFR-36 t=nfr status=TODO family=ACC -->

### NFR-37 — Audit Log Retention [priority=MEDIUM, fields=12]

**Description:** Audit logs retained for ≥12 months.
**Scope:** Production audit logs.
**Out of Scope:** Dev logs.
**Source UC:** U.C.5.3.1
**Source FR:** FR-26
**Source Rule:** CR-D-10.2-001
**NIST CSF Anchors:** CSF: PR.DS-10 | PF: CT.DM-P4, CT.DM-P9
**Measurement Criteria:**
- ≥12-month retention.
- Audit log.
- Monthly review.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-SYS-002
**Risk if not met:** M — premature deletion.
**Affected Stakeholders:** Compliance Manager, CTO, Auditor
**Family:** ACC
**Privacy Flag:** non-PRIV

<!-- NFR-37 t=nfr status=TODO family=ACC -->

### NFR-38 — Policy Review Cadence [priority=MEDIUM, fields=12]

**Description:** All policies reviewed annually.
**Scope:** All internal policies.
**Out of Scope:** Customer-facing terms.
**Source UC:** U.C.5.4.1
**Source FR:** FR-27
**Source Rule:** CR-D-09.1-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.PO-02 | PF: CM.PO-P1, GV.PO-P1
**Measurement Criteria:**
- Annual review documented.
- Audit log.
- Quarterly review.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-PROC-004
**Risk if not met:** M — stale policy = governance gap.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Family:** ACC
**Privacy Flag:** non-PRIV

<!-- NFR-38 t=nfr status=TODO family=ACC -->

### NFR-39 — Data Minimisation Review [priority=MEDIUM, fields=12]

**Description:** Data minimisation reviewed annually.
**Scope:** All processing activities.
**Out of Scope:** Anonymised.
**Source UC:** U.C.5.4.1
**Source FR:** FR-27
**Source Rule:** CR-D-05.1-001
**NIST CSF Anchors:** CSF: GV.PO-02 | PF: ID.IM-P1, ID.IM-P4
**Measurement Criteria:**
- Annual review.
- Audit log.
- Quarterly review.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-PROC-007
**Risk if not met:** M — over-collection.
**Affected Stakeholders:** DPO, Compliance Manager, Auditor
**Family:** ACC
**Privacy Flag:** PRIV

<!-- NFR-39 t=nfr status=TODO family=ACC -->

### NFR-40 — Vendor Security Assessment [priority=MEDIUM, fields=12]

**Description:** Annual security assessment of all data vendors.
**Scope:** All data vendors.
**Out of Scope:** Non-data vendors.
**Source UC:** U.C.5.6.1, U.C.5.4.1
**Source FR:** FR-23, FR-27
**Source Rule:** CR-D-09.1-001
**NIST CSF Anchors:** CSF: GV.SC-01, GV.SC-02 | PF: ID.IM-P2
**Measurement Criteria:**
- Annual assessment.
- Findings tracked.
- Remediation verified.
**Verification Method:** INSPECT
**Owner:** Procurement Lead
**Status:** TODO
**Dependencies:** NODE-PROC-011
**Risk if not met:** H — substandard vendor.
**Affected Stakeholders:** Procurement Lead, Compliance Manager, Auditor
**Family:** ACC
**Privacy Flag:** non-PRIV

<!-- NFR-40 t=nfr status=TODO family=ACC -->

### NFR-41 — Risk Assessment Cadence [priority=MEDIUM, fields=12]

**Description:** Risk assessment before high-risk launch + annual cycle.
**Scope:** All high-risk features.
**Out of Scope:** Bug fixes.
**Source UC:** U.C.4.5.1, U.C.5.2.1
**Source FR:** FR-16, FR-24
**Source Rule:** CR-D-09.2-001
**NIST CSF Anchors:** CSF: ID.RA-01, ID.RA-04 | PF: ID.RA-P3, ID.RA-P4
**Measurement Criteria:**
- Pre-launch + annual.
- Risk register maintained.
- Audit log.
**Verification Method:** DEMONSTRATE
**Owner:** Risk Owner
**Status:** TODO
**Dependencies:** NODE-PROC-005
**Risk if not met:** H — missing assessment.
**Affected Stakeholders:** Risk Owner, DPO, Compliance Manager, Auditor
**Family:** ACC
**Privacy Flag:** non-PRIV

<!-- NFR-41 t=nfr status=TODO family=ACC -->

### NFR-42 — Compliance Report Generation [priority=MEDIUM, fields=12]

**Description:** Compliance reports available within 7 days on demand.
**Scope:** All compliance artefacts.
**Out of Scope:** Archived reports.
**Source UC:** U.C.5.4.1
**Source FR:** FR-27
**Source Rule:** CR-D-09.1-001
**NIST CSF Anchors:** CSF: GV.PO-02 | PF: CM.PO-P1, GV.PO-P1
**Measurement Criteria:**
- ≤7 days measured per request.
- Audit log.
- Quarterly review.
**Verification Method:** TEST
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-SYS-014
**Risk if not met:** M — late report = governance gap.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Family:** COMP
**Privacy Flag:** non-PRIV

<!-- NFR-42 t=nfr status=TODO family=COMP -->

### NFR-43 — Breach Register SLA (Entry) [priority=HIGH, fields=17]

**Description:** Breach register entry within 24h post-detection.
**Scope:** All confirmed security incidents.
**Out of Scope:** Suspected-only.
**Source UC:** U.C.5.4.1
**Source FR:** FR-27
**Source Rule:** CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02 | PF: ID.IM-P1, ID.IM-P8
**Measurement Criteria:**
- ≤24h entry per incident.
- Audit log.
- Monthly review.
**Verification Method:** INSPECT
**Owner:** Incident Commander
**Status:** TODO
**Dependencies:** NODE-SYS-017
**Risk if not met:** M — missed entry = accountability gap.
**Affected Stakeholders:** Incident Commander, DPO, Compliance Manager, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** COMP
**Privacy Flag:** PRIV
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NFR-43 t=nfr status=TODO family=COMP -->

### NFR-44 — ENISA Notification SLA (CRA) [priority=HIGH, fields=17]

**Description:** ENISA notification within 24h of actively-exploited vulnerability.
**Scope:** All confirmed CRA-relevant vulnerabilities.
**Out of Scope:** Suspected-only.
**Source UC:** U.C.2.5.1
**Source FR:** FR-16, FR-24
**Source Rule:** CR-D-04.3-001
**NIST CSF Anchors:** CSF: RS.CO-02 | PF: CM.AW-P7, CM.AW-P8
**Measurement Criteria:**
- ≤24h measured per incident.
- Audit log.
- Tabletop annually.
**Verification Method:** DEMONSTRATE
**Owner:** Incident Commander
**Status:** TODO
**Dependencies:** NODE-SYS-004, NODE-ROLE-008
**Risk if not met:** H — late = CRA sanctions.
**Affected Stakeholders:** Incident Commander, Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** COMP
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- NFR-44 t=nfr status=TODO family=COMP -->

### NFR-45 — SBOM Publication [priority=HIGH, fields=17]

**Description:** SBOM published per release.
**Scope:** All production releases.
**Out of Scope:** Internal tooling.
**Source UC:** U.C.4.5.1, U.C.5.6.1
**Source FR:** FR-23
**Source Rule:** CR-D-06.2-001
**NIST CSF Anchors:** CSF: GV.SC-02, GV.SC-03 | PF: —
**Measurement Criteria:**
- Per-release publication.
- Format validated.
- Audit log.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-SYS-013
**Risk if not met:** M — missing SBOM = CRA Art. 13.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Family:** COMP
**Privacy Flag:** non-PRIV
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- NFR-45 t=nfr status=TODO family=COMP -->

### NFR-46 — Vulnerability Scan Cadence [priority=MEDIUM, fields=12]

**Description:** Vulnerability scans executed weekly.
**Scope:** Production + staging.
**Out of Scope:** Dev.
**Source UC:** U.C.2.3.1
**Source FR:** FR-17
**Source Rule:** CR-D-02.1-001
**NIST CSF Anchors:** CSF: ID.RA-01, ID.RA-04 | PF: ID.RA-P3, ID.RA-P5
**Measurement Criteria:**
- Weekly cadence.
- Findings triaged.
- Audit log.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-PROC-017
**Risk if not met:** M — missed vuln.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Family:** COMP
**Privacy Flag:** non-PRIV

<!-- NFR-46 t=nfr status=TODO family=COMP -->


## §3 NIST anchors (per NFR)

See `NIST_ANCHORS.md` §3.3 for the full table. Summary:

| Family | NFRs with CSF anchors | NFRs with PF anchors | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|--------|----------------------:|---------------------:|-------|-----------------------|----------|----------|--------------|-----------|
| CONF | 9/9 | 5/9 | | | | | | |
| AVAIL | 8/8 | 5/8 | | | | | | |
| INT | 8/8 | 4/8 | | | | | | |
| PRIV | 11/11 | 9/11 | | | | | | |
| ACC | 6/6 | 4/6 | | | | | | |
| COMP | 6/6 | 6/6 | | | | | | |
| **TOTAL** | **46/46 (100%)** | **30/46 (65%)** | | | | | | |

---

## §4 Cross-references

- `23_Functional_Requirements.md` — FR catalogue (30 cards)
- `13_Use_Cases_Catalog.md` §3 — UC catalogue
- `RULE_FREEZE.md` §7 — NFR freeze
- `NIST_ANCHORS.md` §3.3 — per-NFR NIST
- `CORPUS_LINKAGE.md` §5 — NFR-to-D-XX.Y

---

**End of Non-Functional Requirements (Phase 3 RICH, ADJUSTED_FIELDS, Sprint 4)**
