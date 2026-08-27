---
document_id: AEGIS-P3-RICH-15
title: Requirements Allocation — TinyTask SaaS (Phase 3 RICH)
phase: 3
version: 2.0
created: 2026-08-24
updated: 2026-08-24
author: Sprint 4 Executor (paulo@methodology.pt)
status: DEEP_ENRICHED
sprint: 5
deep_enrichment_date: 2026-08-24
detail_cards_count: 30
cells_count: 455
fields_per_card: 17|12|tiered
tier_distribution: "DN cards (19 with 17 fields + 11 with 12 fields)"
sprint_role: deep_enrichment_per_card
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [14_Architectural_Nodes.md, 11_Rules_Catalog.md, 13_Use_Cases_Catalog.md, RULE_FREEZE.md]
outputs: [16_Compliance_Gates_Report.md, 17_Functional_Tree.md]
related_documents: [14_Architectural_Nodes.md, 16_Compliance_Gates_Report.md, CORPUS_LINKAGE.md, RULE_FREEZE.md]
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Implementation Status, Priority, Stakeholders, Reporting]
freeze_total_dn_rows: 30
freeze_total_rules_with_dn: 30
reconciliation_note: "30 DN rows (1:1 with CR); no orphan refs in legacy Doc 15; BPR rules have no DN rows (Doc 15 §4)."
sprint5_note: "Sprint 5: DEEP enrichment — 30 cards (19×17 fields + 11×12 fields) = 455 cells. Frontmatter status DEEP_ENRICHED, version 2.0."
---

# Requirements Allocation — TinyTask SaaS (Phase 3 RICH)

> **Status:** ADJUSTED_FIELDS (Sprint 4). 30 DN rows, 1:1 with 30 CR (per Doc 15 §4). 16 BPR have no DN rows (BPR are best-practice, not binding allocations).

---

## §1 Reconciliation Notes

The Requirements Allocation document maps each Compliance Rule (CR) to a Derivation Node (DN), which then anchors the rule to one or more Architectural Nodes from `14_Architectural_Nodes.md`. Per Doc 15 §4, DN rows are **1:1 with CR** (not with BPR — best-practice rules do not get allocation rows by design).

**Authoritative sources:**
- `RULE_FREEZE.md` §1 — 30 CR (DN rows); 16 BPR (no DN).
- `14_Architectural_Nodes.md` §2-§4 — 49 nodes for allocation target.
- `CORPUS_LINKAGE.md` §7 — DN-to-D-XX.Y mapping.
- `13_Use_Cases_Catalog.md` §3 — UCs referenced.

**Gate criteria (legacy §1):**
- Every CR is allocated to ≥1 DN (verified by §2 below).
- Every DN points to ≥1 architectural node (verified by §2 below).
- Verification method defined (TEST/INSPECT/DEMONSTRATE).

---

## §2 DN Allocation Table (30 rows, 1:1 with CR)

| DN | Rule | D-sub | Title | Target nodes | Primary UC | Verification | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|----|------|-------|-------|--------------|-----------|--------------|-------|-----------------------|----------|----------|--------------|-----------|
| DN-01 | CR-D-01.1-001 | D-01.1 | Data at Rest Encryption | NODE-SYS-010 | U.C.1.1.1 | TEST | | | | | | |
| DN-02 | CR-D-01.2-001 | D-01.2 | Data in Transit Encryption | NODE-SYS-011 | U.C.3.1.1 | TEST | | | | | | |
| DN-03 | CR-D-01.3-001 | D-01.3 | Cryptographic Key Management | NODE-SYS-010, NODE-SYS-011 | U.C.1.1.1 | TEST | | | | | | |
| DN-04 | CR-D-01.4-001 | D-01.4 | Data Integrity Mechanisms | NODE-SYS-016 | U.C.1.1.2 | TEST | | | | | | |
| DN-05 | CR-D-02.1-001 | D-02.1 | Vulnerability-Free Release | NODE-PROC-017, NODE-SYS-009 | U.C.2.1.1 | TEST | | | | | | |
| DN-06 | CR-D-02.2-001 | D-02.2 | Automated Patch Deployment | NODE-PROC-015 | U.C.4.3.1 | INSPECT | | | | | | |
| DN-07 | CR-D-02.3-001 | D-02.3 | Coordinated Vulnerability Disclosure | NODE-PROC-016 | U.C.2.3.1 | INSPECT | | | | | | |
| DN-08 | CR-D-03.1-001 | D-03.1 | Authentication & Access Control | NODE-SYS-006, NODE-SYS-007 | U.C.3.1.1 | TEST | | | | | | |
| DN-09 | CR-D-03.2-001 | D-03.2 | Administrative MFA | NODE-SYS-007 | U.C.3.1.2 | TEST | | | | | | |
| DN-10 | CR-D-03.3-001 | D-03.3 | Authorisation & Least Privilege | NODE-ROLE-004 | U.C.3.2.1 | INSPECT | | | | | | |
| DN-11 | CR-D-03.4-001 | D-03.4 | Secure System Defaults | NODE-SYS-008 | U.C.3.3.1 | TEST | | | | | | |
| DN-12 | CR-D-04.1-001 | D-04.1 | Exploit Severity Limitation | NODE-SYS-005, NODE-PROC-002, NODE-ROLE-010 | U.C.2.4.1 | TEST | | | | | | |
| DN-13 | CR-D-04.2-001 | D-04.2 | Availability Restoration & DoS Resilience | NODE-SYS-005 | U.C.2.4.2 | TEST | | | | | | |
| DN-14 | CR-D-04.3-001 | D-04.3 | Dual Regulatory Incident Notification | NODE-SYS-004, NODE-PROC-001, NODE-ROLE-008 | U.C.2.5.1 | DEMONSTRATE | | | | | | |
| DN-15 | CR-D-04.4-001 | D-04.4 | Data Restoration and Recovery | NODE-SYS-015, NODE-PROC-003 | U.C.2.6.1 | TEST | | | | | | |
| DN-16 | CR-D-05.1-001 | D-05.1 | Data Minimisation | NODE-PROC-007 | U.C.1.4.1 | INSPECT | | | | | | |
| DN-17 | CR-D-05.2-001 | D-05.2 | Storage Limitation & Retention | NODE-PROC-007 | U.C.1.4.1 | INSPECT | | | | | | |
| DN-18 | CR-D-05.3-001 | D-05.3 | Complete and Secure Data Erasure | NODE-SYS-015, NODE-PROC-003 | U.C.1.2.1 | TEST | | | | | | |
| DN-19 | CR-D-05.4-001 | D-05.4 | Structured Data Portability | NODE-SYS-014 | U.C.1.5.1 | TEST | | | | | | |
| DN-20 | CR-D-06.1-001 | D-06.1 | Processor Due Diligence | NODE-PROC-011, NODE-ROLE-009 | U.C.5.4.1 | INSPECT | | | | | | |
| DN-21 | CR-D-06.2-001 | D-06.2 | Software Bill of Materials | NODE-SYS-013 | U.C.5.6.1 | TEST | | | | | | |
| DN-22 | CR-D-06.3-001 | D-06.3 | Contractual Processor Security | NODE-PROC-012, NODE-ROLE-011 | U.C.5.5.1 | INSPECT | | | | | | |
| DN-23 | CR-D-07.1-001 | D-07.1 | Security and Privacy by Design | NODE-PROC-007, NODE-PROC-009, NODE-PROC-010, NODE-ROLE-003 | U.C.4.1.1 | DEMONSTRATE | | | | | | |
| DN-24 | CR-D-08.1-001 | D-08.1 | Annual Security Awareness | NODE-PROC-018, NODE-ROLE-005 | U.C.6.1.1 | INSPECT | | | | | | |
| DN-25 | CR-D-08.2-001 | D-08.2 | Role-Specific Security Competence | NODE-PROC-019, NODE-ROLE-002, NODE-ROLE-003 | U.C.6.2.1 | INSPECT | | | | | | |
| DN-26 | CR-D-09.1-001 | D-09.1 | Security Governance & Technical Documentation | NODE-PROC-004, NODE-ROLE-001, NODE-ROLE-012 | U.C.5.1.1, U.C.5.1.2 | INSPECT | | | | | | |
| DN-27 | CR-D-09.2-001 | D-09.2 | Unified Risk Assessment | NODE-PROC-005, NODE-ROLE-006 | U.C.4.5.1, U.C.5.2.1 | DEMONSTRATE | | | | | | |
| DN-28 | CR-D-09.4-001 | D-09.4 | Processing & Breach Records | NODE-SYS-014, NODE-SYS-017, NODE-PROC-006, NODE-ROLE-007 | U.C.5.3.1, U.C.2.5.1 | INSPECT | | | | | | |
| DN-29 | CR-D-10.2-001 | D-10.2 | Audit Logging & Traceability | NODE-SYS-001, NODE-SYS-002, NODE-SYS-003 | U.C.3.5.1 | TEST | | | | | | |
| DN-30 | CR-D-10.3-001 | D-10.3 | Control Effectiveness Testing | NODE-SYS-009, NODE-PROC-020 | U.C.3.6.1 | INSPECT | | | | | | |

---

### DN-01 — Data at Rest Encryption [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-01.1-001 to NODE-SYS-010: enforces AES-256 at-rest encryption for all production personal-data stores.
**Scope:** Production primary + analytics stores.
**Out of Scope:** Ephemeral dev databases.
**Source:** CR-D-01.1-001 + U.C.1.1.1 + BPR-D-01.1-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1
**Verification Criteria:**
- Encryption verified on every store.
- KMS-managed keys.
- Annual key rotation.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-010, NODE-SYS-016
**Risk if not met:** H — unencrypted = GDPR Art. 32.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- DN-01 t=dn allocationType=DIRECT status=TODO -->

### DN-02 — Data in Transit Encryption [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-01.2-001 to NODE-SYS-011: enforces TLS 1.2+ for all data-in-transit.
**Scope:** All public endpoints.
**Out of Scope:** Internal mTLS (separate control).
**Source:** CR-D-01.2-001 + U.C.3.1.1 + BPR-D-01.2-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02, PR.DS-10 | PF: CT.DM-P1, CT.DM-P3
**Verification Criteria:**
- TLS 1.2+ enforced.
- Cipher suite policy.
- HSTS enabled.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-011
**Risk if not met:** H — weak TLS = transit breach.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- DN-02 t=dn allocationType=DIRECT status=TODO -->

### DN-03 — Cryptographic Key Management [priority=MEDIUM, fields=12, allocType=INHERITED]

**Description:** Allocation of CR-D-01.3-001 to NODE-SYS-010/011 (INHERITED): key management follows AWS KMS policy.
**Scope:** All KMS-managed keys.
**Out of Scope:** Customer-managed keys (separate).
**Source:** CR-D-01.3-001 + U.C.1.1.1 (INHERITED)
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-10 | PF: PR.DS-P1
**Verification Criteria:**
- Keys managed via KMS.
- Annual rotation.
- Access logged.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-010, NODE-SYS-011
**Risk if not met:** M — key compromise = decrypt risk.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Allocation Type:** INHERITED

<!-- DN-03 t=dn allocationType=INHERITED status=TODO -->

### DN-04 — Data Integrity Mechanisms [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-01.4-001 to NODE-SYS-016: HMAC-SHA-256 integrity on critical records.
**Scope:** Production critical records.
**Out of Scope:** Derived / cache.
**Source:** CR-D-01.4-001 + U.C.1.1.2
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02, PR.DS-10 | PF: CT.DM-P1, CT.DM-P3
**Verification Criteria:**
- 100% critical records covered.
- Tamper logs in SIEM.
- Algorithm pinned.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-016
**Risk if not met:** H — undetected tampering = integrity breach.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- DN-04 t=dn allocationType=DIRECT status=TODO -->

### DN-05 — Vulnerability-Free Release [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-02.1-001 to NODE-PROC-017 / NODE-SYS-009: scans + pentest before release.
**Scope:** All production releases.
**Out of Scope:** Pre-alpha.
**Source:** CR-D-02.1-001 + U.C.2.1.1 + BPR-D-02.1-001
**NIST CSF Anchors:** CSF: GV.OV-02, ID.AM-02, ID.RA-01 | PF: ID.RA-P3, ID.RA-P5
**Verification Criteria:**
- 0 critical at release.
- Findings triaged.
- Pentest annual.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-PROC-017, NODE-SYS-009
**Risk if not met:** H — unpatched vuln = CRA trigger.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- DN-05 t=dn allocationType=DIRECT status=TODO -->

### DN-06 — Automated Patch Deployment [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-02.2-001 to NODE-PROC-015: critical patches within 24h.
**Scope:** Production + staging.
**Out of Scope:** Third-party managed.
**Source:** CR-D-02.2-001 + U.C.4.3.1 + BPR-D-02.2-001
**NIST CSF Anchors:** CSF: GV.OV-02, ID.RA-01, PR.IR-03 | PF: —
**Verification Criteria:**
- Critical median ≤24h.
- Auto-rollback tested.
- Patch log.
**Verification Method:** INSPECT
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-PROC-015
**Risk if not met:** H — unpatched = CRA trigger.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- DN-06 t=dn allocationType=DIRECT status=TODO -->

### DN-07 — Coordinated Vulnerability Disclosure [priority=MEDIUM, fields=12, allocType=DIRECT]

**Description:** Allocation of CR-D-02.3-001 to NODE-PROC-016: receive + triage + respond to external reports.
**Scope:** External researchers.
**Out of Scope:** Customer support.
**Source:** CR-D-02.3-001 + U.C.2.3.1
**NIST CSF Anchors:** CSF: GV.PO-01, GV.SC-04, RS.CO-03 | PF: —
**Verification Criteria:**
- security.txt present.
- Median first response ≤72h.
- CVE for confirmed.
**Verification Method:** INSPECT
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-PROC-016
**Risk if not met:** M — slow disclosure damages trust.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Allocation Type:** DIRECT

<!-- DN-07 t=dn allocationType=DIRECT status=TODO -->

### DN-08 — Authentication & Access Control [priority=HIGH, fields=17, allocType=INHERITED]

**Description:** Allocation of CR-D-03.1-001 to NODE-SYS-006/007 (INHERITED): central IdP + PAM.
**Scope:** All human identities.
**Out of Scope:** Service accounts.
**Source:** CR-D-03.1-001 + U.C.3.1.1 + BPR-D-03.1-001
**NIST CSF Anchors:** CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: —
**Verification Criteria:**
- 100% auth via IdP.
- Lockout after 5 fails.
- Audit log.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-006, NODE-SYS-007
**Risk if not met:** H — auth bypass = total compromise.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** INHERITED
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- DN-08 t=dn allocationType=INHERITED status=TODO -->

### DN-09 — Administrative MFA [priority=HIGH, fields=17, allocType=INHERITED]

**Description:** Allocation of CR-D-03.2-001 to NODE-SYS-007: FIDO2 MFA + session recording (INHERITED).
**Scope:** Privileged roles.
**Out of Scope:** Standard users.
**Source:** CR-D-03.2-001 + U.C.3.1.2 + BPR-D-03.2-001
**NIST CSF Anchors:** CSF: PR.AA-03, PR.AA-04, PR.AA-05 | PF: —
**Verification Criteria:**
- 100% privileged MFA.
- Session recording.
- Quarterly review.
**Verification Method:** DEMONSTRATE
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-007
**Risk if not met:** H — privileged compromise = total takeover.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** INHERITED
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- DN-09 t=dn allocationType=INHERITED status=TODO -->

### DN-10 — Authorisation & Least Privilege [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-03.3-001 to NODE-ROLE-004: RBAC + quarterly access reviews.
**Scope:** All internal staff.
**Out of Scope:** Customer self-service.
**Source:** CR-D-03.3-001 + U.C.3.2.1
**NIST CSF Anchors:** CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: CT.PO-P1
**Verification Criteria:**
- Quarterly review (NFR-25).
- Deprovision ≤24h.
- Privilege creep detected.
**Verification Method:** INSPECT
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-ROLE-004
**Risk if not met:** M — privilege drift = insider risk.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- DN-10 t=dn allocationType=DIRECT status=TODO -->

### DN-11 — Secure System Defaults [priority=MEDIUM, fields=12, allocType=DIRECT]

**Description:** Allocation of CR-D-03.4-001 to NODE-SYS-008: CIS-aligned hardened baseline.
**Scope:** Production hosts.
**Out of Scope:** Dev environments.
**Source:** CR-D-03.4-001 + U.C.3.3.1 + BPR-D-03.4-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.SC-03, PR.DS-10 | PF: CT.DP-P4, CT.PO-P4
**Verification Criteria:**
- ≥95% CIS compliance.
- Drift detection.
- Deviations documented.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-008
**Risk if not met:** M — misconfig = top breach vector.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Allocation Type:** DIRECT

<!-- DN-11 t=dn allocationType=DIRECT status=TODO -->

### DN-12 — Exploit Severity Limitation [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-04.1-001 to NODE-SYS-005/002/010: fail-safe design + WAF + Security Engineer.
**Scope:** Production components.
**Out of Scope:** UI graceful degradation.
**Source:** CR-D-04.1-001 + U.C.2.4.1
**NIST CSF Anchors:** CSF: DE.AE-02, DE.CM-01, DE.CM-09 | PF: CM.AW-P7
**Verification Criteria:**
- Containment ≤30min.
- Fail-safe verified.
- WAF rules tuned.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-005, NODE-PROC-002, NODE-ROLE-010
**Risk if not met:** H — uncontrolled exploit = breach.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- DN-12 t=dn allocationType=DIRECT status=TODO -->

### DN-13 — Availability Restoration & DoS Resilience [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-04.2-001 to NODE-SYS-005: WAF + auto-scaling for DoS.
**Scope:** Production APIs.
**Out of Scope:** Edge DDoS (cloud SLA).
**Source:** CR-D-04.2-001 + U.C.2.4.2
**NIST CSF Anchors:** CSF: DE.CM-09, PR.DS-10, PR.IR-03 | PF: CT.DM-P10, PR.PO-P7
**Verification Criteria:**
- Chaos test quarterly.
- Availability ≥99.9%.
- Runbook published.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-005
**Risk if not met:** M — sustained outage = GDPR + revenue.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- DN-13 t=dn allocationType=DIRECT status=TODO -->

### DN-14 — Dual Regulatory Incident Notification [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-04.3-001 to NODE-SYS-004 + NODE-PROC-001 + NODE-ROLE-008: ENISA 24h + CNPD 72h.
**Scope:** All confirmed incidents.
**Out of Scope:** Suspected-only.
**Source:** CR-D-04.3-001 + U.C.2.5.1 + BPR-D-04.3-001/002
**NIST CSF Anchors:** CSF: RS.CO-02, RS.MA-01, RS.MA-02 | PF: CM.AW-P7, CM.AW-P8, CM.PO-P1
**Verification Criteria:**
- ENISA ≤24h.
- CNPD ≤72h.
- Tabletop quarterly.
**Verification Method:** DEMONSTRATE
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-004, NODE-PROC-001, NODE-ROLE-008
**Risk if not met:** H — late = dual fine.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- DN-14 t=dn allocationType=DIRECT status=TODO -->

### DN-15 — Data Restoration and Recovery [priority=MEDIUM, fields=12, allocType=DIRECT]

**Description:** Allocation of CR-D-04.4-001 to NODE-SYS-015 + NODE-PROC-003: backup + restore.
**Scope:** Production backups.
**Out of Scope:** Long-term archival.
**Source:** CR-D-04.4-001 + U.C.2.6.1
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-10, PR.IR-03 | PF: —
**Verification Criteria:**
- RTO ≤24h, RPO ≤1h.
- Quarterly drill.
- Runbook signed off.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-015, NODE-PROC-003
**Risk if not met:** H — failed restore = data loss.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Allocation Type:** DIRECT

<!-- DN-15 t=dn allocationType=DIRECT status=TODO -->

### DN-16 — Data Minimisation [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-05.1-001 to NODE-PROC-007: data-minimisation review at design.
**Scope:** All new features.
**Out of Scope:** Pre-existing data.
**Source:** CR-D-05.1-001 + U.C.1.4.1
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P4, ID.IM-P6
**Verification Criteria:**
- Annual review (NFR-39).
- Design gate.
- Processor cascade.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-PROC-007
**Risk if not met:** H — over-collection = Art. 5(1)(c).
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- DN-16 t=dn allocationType=DIRECT status=TODO -->

### DN-17 — Storage Limitation & Retention [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-05.2-001 to NODE-PROC-007: retention policies + deletion automation.
**Scope:** All personal data.
**Out of Scope:** Anonymised data.
**Source:** CR-D-05.2-001 + U.C.1.4.1
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P4, ID.IM-P6
**Verification Criteria:**
- Retention policy documented.
- Auto-deletion verified.
- Annual review.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-PROC-007
**Risk if not met:** M — over-retention = Art. 5(1)(e).
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- DN-17 t=dn allocationType=DIRECT status=TODO -->

### DN-18 — Complete and Secure Data Erasure [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-05.3-001 to NODE-SYS-015 + NODE-PROC-003: cryptographic erasure.
**Scope:** Primary + backup + logs.
**Out of Scope:** Legal-hold data.
**Source:** CR-D-05.3-001 + U.C.1.2.1 + BPR-D-05.3-001
**NIST CSF Anchors:** CSF: GV.SC-04, PR.DS-10, PR.DS-02 | PF: CT.DM-P4, CT.DM-P5
**Verification Criteria:**
- Erasure receipt.
- NIST SP 800-88 verification.
- Processor cascade.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-015, NODE-PROC-003
**Risk if not met:** H — incomplete = Art. 17 violation.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- DN-18 t=dn allocationType=DIRECT status=TODO -->

### DN-19 — Structured Data Portability [priority=MEDIUM, fields=12, allocType=DIRECT]

**Description:** Allocation of CR-D-05.4-001 to NODE-SYS-014: schema-documented export endpoint.
**Scope:** Personal-data export.
**Out of Scope:** Real-time streaming.
**Source:** CR-D-05.4-001 + U.C.1.5.1
**NIST CSF Anchors:** CSF: PR.DS-10, PR.AA-03, PR.DS-02 | PF: CT.DM-P1, CT.DM-P6
**Verification Criteria:**
- Schema versioned.
- Auth + rate limit.
- JSON schema valid.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-014
**Risk if not met:** M — Art. 20 gap.
**Affected Stakeholders:** Customer, DPO, Auditor
**Allocation Type:** DIRECT

<!-- DN-19 t=dn allocationType=DIRECT status=TODO -->

### DN-20 — Processor Due Diligence [priority=MEDIUM, fields=12, allocType=DIRECT]

**Description:** Allocation of CR-D-06.1-001 to NODE-PROC-011 + NODE-ROLE-009: pre-engagement questionnaire + annual review.
**Scope:** All data processors.
**Out of Scope:** Non-data vendors.
**Source:** CR-D-06.1-001 + U.C.5.4.1
**NIST CSF Anchors:** CSF: GV.SC-01, GV.SC-02, GV.SC-03 | PF: ID.IM-P2
**Verification Criteria:**
- Questionnaire pre-engagement.
- Annual review (NFR-40).
- Findings tracked.
**Verification Method:** INSPECT
**Owner:** Procurement Lead
**Status:** TODO
**Dependencies:** NODE-PROC-011, NODE-ROLE-009
**Risk if not met:** H — substandard processor = Art. 28.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Allocation Type:** DIRECT

<!-- DN-20 t=dn allocationType=DIRECT status=TODO -->

### DN-21 — Software Bill of Materials [priority=MEDIUM, fields=12, allocType=DIRECT]

**Description:** Allocation of CR-D-06.2-001 to NODE-SYS-013: SBOM per release in CycloneDX/SPDX.
**Scope:** All production releases.
**Out of Scope:** Internal tooling.
**Source:** CR-D-06.2-001 + U.C.5.6.1
**NIST CSF Anchors:** CSF: GV.SC-02, GV.SC-03, ID.RA-01 | PF: —
**Verification Criteria:**
- SBOM per release (NFR-45).
- Format validated.
- Customer portal tested.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-SYS-013
**Risk if not met:** M — missing SBOM = CRA Art. 13.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Allocation Type:** DIRECT

<!-- DN-21 t=dn allocationType=DIRECT status=TODO -->

### DN-22 — Contractual Processor Security [priority=MEDIUM, fields=12, allocType=DIRECT]

**Description:** Allocation of CR-D-06.3-001 to NODE-PROC-012 + NODE-ROLE-011: DPA lifecycle.
**Scope:** All data processors.
**Out of Scope:** Non-data vendors.
**Source:** CR-D-06.3-001 + U.C.5.5.1
**NIST CSF Anchors:** CSF: GV.OC-03, GV.SC-02, GV.SC-03 | PF: —
**Verification Criteria:**
- 100% active processors DPA.
- Annual review.
- Art. 28 clauses.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-PROC-012, NODE-ROLE-011
**Risk if not met:** H — missing DPA = Art. 28.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Allocation Type:** DIRECT

<!-- DN-22 t=dn allocationType=DIRECT status=TODO -->

### DN-23 — Security and Privacy by Design [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-07.1-001 to NODE-PROC-007/009/010 + NODE-ROLE-003: SSDLC + threat model.
**Scope:** All production code.
**Out of Scope:** Internal tooling.
**Source:** CR-D-07.1-001 + U.C.4.1.1 + BPR-D-07.1-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.RA-01, PR.DS-10 | PF: CT.DP-P2, CT.DP-P4, GV.PO-P2
**Verification Criteria:**
- Threat model per feature.
- Review checklist.
- Quarterly metrics.
**Verification Method:** DEMONSTRATE
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-PROC-007, NODE-PROC-009, NODE-PROC-010, NODE-ROLE-003
**Risk if not met:** M — design flaws late = costly.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- DN-23 t=dn allocationType=DIRECT status=TODO -->

### DN-24 — Annual Security Awareness [priority=MEDIUM, fields=12, allocType=DIRECT]

**Description:** Allocation of CR-D-08.1-001 to NODE-PROC-018 + NODE-ROLE-005: training delivery.
**Scope:** All staff.
**Out of Scope:** External.
**Source:** CR-D-08.1-001 + U.C.6.1.1
**NIST CSF Anchors:** CSF: PR.AT-01, PR.AT-02, PR.PS-01 | PF: GV.AT-P1, GV.AT-P2
**Verification Criteria:**
- 100% completion (NFR-36).
- Refreshed annually.
- Quiz required.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-PROC-018, NODE-ROLE-005
**Risk if not met:** M — untrained staff = phishing risk.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor
**Allocation Type:** DIRECT

<!-- DN-24 t=dn allocationType=DIRECT status=TODO -->

### DN-25 — Role-Specific Security Competence [priority=MEDIUM, fields=12, allocType=DIRECT]

**Description:** Allocation of CR-D-08.2-001 to NODE-PROC-019 + NODE-ROLE-002/003: role curricula.
**Scope:** Engineers, ops, DPO.
**Out of Scope:** General awareness.
**Source:** CR-D-08.2-001 + U.C.6.2.1
**NIST CSF Anchors:** CSF: GV.RR-02, GV.RR-04, PR.AT-02 | PF: GV.AT-P1, GV.AT-P2
**Verification Criteria:**
- Role curricula defined.
- Completion tracked.
- Refreshed annually.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-PROC-019, NODE-ROLE-002, NODE-ROLE-003
**Risk if not met:** M — role gaps = competency risk.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor
**Allocation Type:** DIRECT

<!-- DN-25 t=dn allocationType=DIRECT status=TODO -->

### DN-26 — Security Governance & Technical Documentation [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-09.1-001 to NODE-PROC-004 + NODE-ROLE-001/012: ISMS + governance.
**Scope:** All internal policies.
**Out of Scope:** Customer terms.
**Source:** CR-D-09.1-001 + U.C.5.1.1/U.C.5.1.2 + BPR-D-09.1-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.PO-02, GV.OV-01 | PF: CM.PO-P1, GV.PO-P1
**Verification Criteria:**
- Annual policy review.
- Technical docs current.
- ISMS maintained.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-PROC-004, NODE-ROLE-001, NODE-ROLE-012
**Risk if not met:** M — governance gap = audit finding.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- DN-26 t=dn allocationType=DIRECT status=TODO -->

### DN-27 — Unified Risk Assessment [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-09.2-001 to NODE-PROC-005 + NODE-ROLE-006: DPIA + risk register.
**Scope:** All high-risk processing.
**Out of Scope:** Low-risk routine.
**Source:** CR-D-09.2-001 + U.C.4.5.1/U.C.5.2.1
**NIST CSF Anchors:** CSF: ID.RA-01, ID.RA-04, ID.RA-05 | PF: ID.RA-P3, ID.RA-P4, ID.RA-P5
**Verification Criteria:**
- Pre-launch DPIA.
- Annual full review.
- Risk register maintained.
**Verification Method:** DEMONSTRATE
**Owner:** Risk Owner
**Status:** TODO
**Dependencies:** NODE-PROC-005, NODE-ROLE-006
**Risk if not met:** H — missing DPIA = Art. 35.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- DN-27 t=dn allocationType=DIRECT status=TODO -->

### DN-28 — Processing & Breach Records [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-09.4-001 to NODE-SYS-014/017 + NODE-PROC-006 + NODE-ROLE-007: RoPA + breach register.
**Scope:** All processing + breaches.
**Out of Scope:** Anonymised.
**Source:** CR-D-09.4-001 + U.C.5.3.1/U.C.2.5.1
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P8
**Verification Criteria:**
- RoPA ≤7d update.
- Breach register ≤24h.
- DPO review monthly.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** NODE-SYS-014, NODE-SYS-017, NODE-PROC-006, NODE-ROLE-007
**Risk if not met:** H — Art. 30 violation.
**Affected Stakeholders:** Customer, DPO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- DN-28 t=dn allocationType=DIRECT status=TODO -->

### DN-29 — Audit Logging & Traceability [priority=MEDIUM, fields=12, allocType=DIRECT]

**Description:** Allocation of CR-D-10.2-001 to NODE-SYS-001/002/003: SIEM + WORM store.
**Scope:** All production logs.
**Out of Scope:** Dev logs.
**Source:** CR-D-10.2-001 + U.C.3.5.1 + BPR-D-10.2-001
**NIST CSF Anchors:** CSF: DE.CM-01, GV.PO-02, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9
**Verification Criteria:**
- 100% auth events.
- ≥12mo retention.
- WORM enforced.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-SYS-001, NODE-SYS-002, NODE-SYS-003
**Risk if not met:** H — log gap = accountability breach.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Allocation Type:** DIRECT

<!-- DN-29 t=dn allocationType=DIRECT status=TODO -->

### DN-30 — Control Effectiveness Testing [priority=HIGH, fields=17, allocType=DIRECT]

**Description:** Allocation of CR-D-10.3-001 to NODE-SYS-009 + NODE-PROC-020: pentest + control review.
**Scope:** All production controls.
**Out of Scope:** Dev.
**Source:** CR-D-10.3-001 + U.C.3.6.1 + BPR-D-10.3-001/002
**NIST CSF Anchors:** CSF: DE.AE-02, GV.OV-03, ID.RA-05 | PF: ID.RA-P3, ID.RA-P5
**Verification Criteria:**
- Annual pentest.
- Findings remediated.
- Controls catalog updated.
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** NODE-SYS-009, NODE-PROC-020
**Risk if not met:** M — untested controls = drift.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Allocation Type:** DIRECT
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- DN-30 t=dn allocationType=DIRECT status=TODO -->


## §3 Verification method distribution

| Method | DN count | % | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|--------|---------:|--:|-------|-----------------------|----------|----------|--------------|-----------|
| TEST | 15 | 50% | | | | | | |
| INSPECT | 11 | 37% | | | | | | |
| DEMONSTRATE | 4 | 13% | | | | | | |
| **TOTAL** | **30** | **100%** | | | | | | |

---

## §4 Cross-references

- `14_Architectural_Nodes.md` §2-§4 — node catalogue
- `16_Compliance_Gates_Report.md` §2 — gates (1:1 with DN)
- `CORPUS_LINKAGE.md` §7 — DN-to-D-XX.Y mapping
- `RULE_FREEZE.md` §1 — CR freeze (DN mirrors CR)
- `13_Use_Cases_Catalog.md` §3 — UC catalogue
- `NIST_ANCHORS.md` §1 — per-rule NIST anchors

---

**End of Requirements Allocation (Phase 3 RICH, ADJUSTED_FIELDS, Sprint 4)**
