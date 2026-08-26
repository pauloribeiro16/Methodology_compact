---
document_id: AEGIS-P3-RICH-13
title: Use Cases Catalog — TinyTask SaaS (Phase 3 RICH)
phase: 3
version: 2.0
created: 2026-08-24
updated: 2026-08-24
author: Sprint 4 Executor (paulo@methodology.pt)
status: DEEP_ENRICHED
sprint: 5
deep_enrichment_date: 2026-08-24
detail_cards_count: 35
cells_count: 475
fields_per_card: 17|12|tiered
tier_distribution: "UC cards (11 CRITICAL/HIGH + 24 MEDIUM/LOW)"
sprint_role: deep_enrichment_per_card
case: Case_01_TinyTask_SaaS
tier: MICRO
sibling_of: ../02_PHASE2_RULES_RICH/
branch: feature/aegis-p3-case01-rich
sibling_doc: ../03_PHASE3_DECOMPOSITION/
inputs: [11_Rules_Catalog.md, ../02_PHASE2_RULES_RICH/11_Rules_Catalog.md, ../02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md, RULE_FREEZE.md, NIST_ANCHORS.md]
outputs: [14_Architectural_Nodes.md, 15_Requirements_Allocation.md, 23_Functional_Requirements.md, 24_Non_Functional_Requirements.md, 25_Risk_Analysis.md, Phase_3_Functional_Decomposition_Synthesis.md]
related_documents: [13a_Use_Case_Relationships.md, 13b_Use_Case_Variability.md, annexes/A_Use_Case_Diagrams.md, RULE_FREEZE.md, CORPUS_LINKAGE.md, NIST_ANCHORS.md]
expected_documents: 13
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Maturity, Priority, Stakeholders, Reporting]
freeze_total_use_cases_l1: 35
freeze_total_use_cases_references: 62
freeze_total_rules: 46
corpus_linked: true
nist_anchors: "see NIST_ANCHORS.md §3.1 (per-UC)"
reconciliation_note: "UCs reconciled to L1=35 cards, 62 total L1+L2 references; F-00b CLOSED; 7 in-freeze CR-D refs preserved from legacy §5; F-S1 orphan refs (D-07.3/07.4/10.1) flagged for Sprint 5 port."
sprint5_note: "Sprint 5: DEEP enrichment — 35 cards (11×17 fields + 24×12 fields) = 475 cells. Frontmatter status DEEP_ENRICHED, version 2.0."
---

# Use Cases Catalog — TinyTask SaaS (Phase 3 RICH)

> **Status:** ADJUSTED_FIELDS (Sprint 4). 35 L1 cards freeze, 62 L1+L2 references freeze.
> Sprint 5 will deep-fill the 17-field per-card schema. Source of truth: `RULE_FREEZE.md` + `CORPUS_LINKAGE.md` §3.

---

## §1 Reconciliation Notes

This document's structure mirrors legacy `13_Use_Cases_Catalog.md` (v5.0, MaaS-style). The Rich sibling retains the `U.C.X.Y.Z` format (F-00a RESOLVED) and reconciles:

- **35 L1 cards** (atomic + actionable) — see §3 catalogue below.
- **62 L1+L2 references** (35 L1 + 27 L2 expansions) per Doc 16 §5B SC2 — preserved in 22_Traceability_Matrix.xlsx.
- **6 packages** (PKG-DP/SEC/IAM/DEV/GOV/TRN) — see §2.
- **6 stakeholder categories** (internal: CEO, CTO, Lead Dev, Ops Lead, DPO; external: customers, processors, supervisory body) — see §4.

**Authoritative sources:**
- `../02_PHASE2_RULES_RICH/11_Rules_Catalog.md` §4 (CR) + §5 (BPR) — 46 rules.
- `RULE_FREEZE.md` §1 — canonical rule freeze.
- `NIST_ANCHORS.md` §3.1 — per-UC NIST CSF 2.0 + PF 1.0 anchors.
- `KG_CHAINS.md` §1 — KG inference chains touching UCs (CH-09: FR-29 → UC-25 → CR-D-04.3).

---

## §2 Package Structure (6 packages)

| Package ID | Name | UC Count | D-subdomains | Primary regs | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|------------|------|---------:|--------------|--------------|-------|-----------------------|----------|----------|--------------|-----------|
| PKG-DP | Data Protection | 6 | D-01.1/01.4/05.1/05.2/05.3/05.4 | GDPR | | | | | | |
| PKG-SEC | Security Operations | 7 | D-02.x/04.x | CRA, GDPR | | | | | | |
| PKG-IAM | Identity & Access | 7 | D-03.x/09.4/10.x | CRA | | | | | | |
| PKG-DEV | Secure Development | 5 | D-07.x/02.2/04.1/09.2 | CRA | | | | | | |
| PKG-GOV | Governance & Compliance | 7 | D-06.x/09.x | GDPR, CRA | | | | | | |
| PKG-TRN | Training & Awareness | 3 | D-08.x | GDPR | | | | | | |
| **TOTAL** | | **35** | | | | | | | | |

---

## §3 Use Case Catalog (35 L1 cards)

> Format: `U.C.X.Y.Z | PKG | D-XX.X | Title | Primary CR/PO/SO | CSF | PF | Priority`
> Detail cards (17-field schema) filled in Sprint 5.

### §3.1 PKG-DP (Data Protection) — 6

| UC ID | D | Title | Primary rule | CSF | PF | Prio | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|-------|---|-------|--------------|-----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| U.C.1.1.1 | D-01.1 | Data Subject Access Request (DSAR) | CR-D-01.1-001 / PO-D-01.1-001 | PR.DS-01, PR.DS-10, PR.PS-04 | PR.DS-P1 | CRITICAL | | | | | | |
| U.C.1.1.2 | D-01.4 | Data Subject Rectification | CR-D-01.4-001 / PO-D-01.4-001 | PR.DS-01, PR.DS-02, PR.DS-10 | CT.DM-P1, CT.DM-P3 | HIGH | | | | | | |
| U.C.1.2.1 | D-05.3 | Data Subject Erasure | CR-D-05.3-001 / PO-D-05.3-001 | GV.SC-04, PR.DS-10, PR.DS-02 | CT.DM-P4, CT.DM-P5 | CRITICAL | | | | | | |
| U.C.1.3.1 | D-05.1 | Data Subject Data Export (portability) | CR-D-05.4-001 / PO-D-05.4-001 | PR.DS-10, PR.AA-03, PR.DS-02 | CT.DM-P1, CT.DM-P6 | HIGH | | | | | | |
| U.C.1.4.1 | D-05.2 | Consent Management | CR-D-05.1-001 / PO-D-05.1-001 | GV.OC-03, GV.PO-01, ID.AM-03 | CT.DP-P4, CT.PO-P4, ID.RA-P3 | HIGH | | | | | | |
| U.C.1.5.1 | D-05.4 | Structured Data Portability | CR-D-05.4-001 / PO-D-05.4-001 | PR.DS-10, PR.AA-03, PR.DS-02 | CT.DM-P1, CT.DM-P6 | MEDIUM | | | | | | |

### §3.2 PKG-SEC (Security Operations) — 7

| UC ID | D | Title | Primary rule | CSF | PF | Prio | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|-------|---|-------|--------------|-----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| U.C.2.1.1 | D-02.1 | Vulnerability-Free Release | CR-D-02.1-001 / SO-D-02.1-001 | GV.OV-02, ID.AM-02, ID.RA-01 | ID.RA-P3, ID.RA-P5 | CRITICAL | | | | | | |
| U.C.2.2.1 | D-02.2 | Automated Patch Deployment | CR-D-02.2-001 / SO-D-02.2-001 | GV.OV-02, ID.RA-01, PR.IR-03 | — | CRITICAL | | | | | | |
| U.C.2.3.1 | D-02.3 | Coordinated Vulnerability Disclosure | CR-D-02.3-001 / SO-D-02.3-001 | GV.PO-01, GV.SC-04, RS.CO-03 | — | HIGH | | | | | | |
| U.C.2.4.1 | D-04.1 | Exploit Severity Limitation | CR-D-04.1-001 / SO-D-04.1-001 | DE.AE-02, DE.CM-01, DE.CM-09 | CM.AW-P7 | CRITICAL | | | | | | |
| U.C.2.4.2 | D-04.2 | DoS Resilience | CR-D-04.2-001 / SO-D-04.2-001 | DE.CM-09, PR.DS-10, PR.IR-03 | CT.DM-P10, PR.PO-P7 | HIGH | | | | | | |
| U.C.2.5.1 | D-04.3 | Incident Notification (24h ENISA, 72h GDPR) | CR-D-04.3-001 / SO-D-04.3-001 | RS.CO-02, RS.MA-01, RS.MA-02 | CM.AW-P7, CM.AW-P8, CM.PO-P1 | CRITICAL | | | | | | |
| U.C.2.6.1 | D-04.4 | Data Restoration & Recovery | CR-D-04.4-001 / SO-D-04.4-001 | PR.DS-01, PR.DS-10, PR.IR-03 | — | HIGH | | | | | | |

### §3.3 PKG-IAM (Identity & Access) — 7

| UC ID | D | Title | Primary rule | CSF | PF | Prio | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|-------|---|-------|--------------|-----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| U.C.3.1.1 | D-03.1 | User Authentication | CR-D-03.1-001 / SO-D-03.1-001 | ID.AM-01, PR.AA-01, PR.AA-03 | — | CRITICAL | | | | | | |
| U.C.3.1.2 | D-03.2 | MFA for Privileged Accounts | CR-D-03.2-001 / SO-D-03.2-001 | PR.AA-03, PR.AA-04, PR.AA-05 | — | CRITICAL | | | | | | |
| U.C.3.2.1 | D-03.3 | Authorisation / Least Privilege | CR-D-03.3-001 / SO-D-03.3-001 | ID.AM-01, PR.AA-01, PR.AA-03 | CT.PO-P1 | HIGH | | | | | | |
| U.C.3.3.1 | D-03.4 | Secure System Defaults | CR-D-03.4-001 / SO-D-03.4-001 | GV.PO-01, GV.SC-03, PR.DS-10 | CT.DP-P4, CT.PO-P4 | HIGH | | | | | | |
| U.C.3.4.1 | D-09.4 | Processing & Breach Records | CR-D-09.4-001 / PO-D-09.4-001 | GV.PO-02, ID.AM-08, PR.DS-10 | ID.IM-P1, ID.IM-P8 | HIGH | | | | | | |
| U.C.3.5.1 | D-10.2 | Audit Logging | CR-D-10.2-001 / SO-D-10.2-001 | DE.CM-01, GV.PO-02, PR.DS-01 | CT.DM-P4, CT.DM-P9 | HIGH | | | | | | |
| U.C.3.6.1 | D-10.3 | Control Effectiveness Testing | CR-D-10.3-001 / SO-D-10.3-001 | DE.AE-02, GV.OV-03, ID.RA-05 | ID.RA-P3, ID.RA-P5 | MEDIUM | | | | | | |

### §3.4 PKG-DEV (Secure Development) — 5

| UC ID | D | Title | Primary rule | CSF | PF | Prio | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|-------|---|-------|--------------|-----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| U.C.4.1.1 | D-07.1 | Security by Design (SSDLC) | CR-D-07.1-001 / PO-D-07.1-001 | GV.PO-02, ID.RA-01, PR.DS-10 | CT.DP-P2, CT.DP-P4, GV.PO-P2 | HIGH | | | | | | |
| U.C.4.2.1 | D-07.2 | SAST/DAST in CI/CD | BPR-D-07.2-001 | ID.RA-04, ID.RA-05, PR.PS-01 | — | HIGH | | | | | | |
| U.C.4.3.1 | D-02.2 | Security Patch Deployment | CR-D-02.2-001 / SO-D-02.2-001 | GV.OV-02, ID.RA-01, PR.IR-03 | — | CRITICAL | | | | | | |
| U.C.4.4.1 | D-04.1 | Fail-Safe Design | CR-D-04.1-001 / SO-D-04.1-001 | DE.AE-02, DE.CM-01, DE.CM-09 | CM.AW-P7 | HIGH | | | | | | |
| U.C.4.5.1 | D-09.2 | Pre-Launch Risk Assessment | CR-D-09.2-001 / PO-D-09.2-001 | ID.RA-01, ID.RA-04, ID.RA-05 | ID.RA-P3, ID.RA-P4, ID.RA-P5 | CRITICAL | | | | | | |

### §3.5 PKG-GOV (Governance & Compliance) — 7

| UC ID | D | Title | Primary rule | CSF | PF | Prio | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|-------|---|-------|--------------|-----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| U.C.5.1.1 | D-09.1 | Annual Policy Review | CR-D-09.1-001 / PO-D-09.1-001 | GV.PO-01, GV.PO-02, GV.RM-04 | CM.PO-P1, GV.PO-P1, GV.PO-P5 | HIGH | | | | | | |
| U.C.5.1.2 | D-09.1 | Technical Documentation Maintenance | CR-D-09.1-001 / SO-D-09.1-001 | GV.PO-01, GV.PO-02, GV.OV-01 | CM.PO-P1, GV.PO-P1 | HIGH | | | | | | |
| U.C.5.2.1 | D-09.2 | DPIA Pre-Launch | CR-D-09.2-001 / PO-D-09.2-001 | ID.RA-01, ID.RA-04, ID.RA-05 | ID.RA-P3, ID.RA-P4, ID.RA-P5 | CRITICAL | | | | | | |
| U.C.5.3.1 | D-09.4 | RoPA Maintenance | CR-D-09.4-001 / PO-D-09.4-001 | GV.PO-02, ID.AM-08, PR.DS-10 | ID.IM-P1, ID.IM-P4, ID.IM-P6 | HIGH | | | | | | |
| U.C.5.4.1 | D-06.1 | Processor Due Diligence | CR-D-06.1-001 / SO-D-06.1-001 | GV.SC-01, GV.SC-02, GV.SC-03 | ID.IM-P2 | HIGH | | | | | | |
| U.C.5.5.1 | D-06.3 | DPAs Binding Processors | CR-D-06.3-001 / SO-D-06.3-001 | GV.OC-03, GV.SC-02, GV.SC-03 | — | HIGH | | | | | | |
| U.C.5.6.1 | D-06.2 | SBOM Publication | CR-D-06.2-001 / SO-D-06.2-001 | GV.SC-02, GV.SC-03, ID.AM-02 | — | HIGH | | | | | | |

### §3.6 PKG-TRN (Training & Awareness) — 3

| UC ID | D | Title | Primary rule | CSF | PF | Prio | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|-------|---|-------|--------------|-----|----|----|-------|-----------------------|----------|----------|--------------|-----------|
| U.C.6.1.1 | D-08.1 | Annual Awareness Training | CR-D-08.1-001 / SO-D-08.1-001 | PR.AT-01, PR.AT-02, PR.PS-01 | GV.AT-P1, GV.AT-P2 | MEDIUM | | | | | | |
| U.C.6.2.1 | D-08.2 | Role-Specific Training | CR-D-08.2-001 / SO-D-08.2-001 | GV.RR-02, GV.RR-04, PR.AT-02 | GV.AT-P1, GV.AT-P2 | MEDIUM | | | | | | |
| U.C.6.3.1 | D-08.1 | Phishing Simulation | CR-D-08.1-001 / SO-D-08.1-001 | PR.AT-01, PR.AT-02, PR.PS-01 | GV.AT-P1, GV.AT-P2 | LOW | | | | | | |

---

## §4 Stakeholders (from Phase 1)

| ID | Role | Type | Responsibilities | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|----|------|------|----------------|-------|-----------------------|----------|----------|--------------|-----------|
| SH-INT-001 | CEO | Internal | Business decisions, risk acceptance (0.05 FTE) | | | | | | |
| SH-INT-002 | CTO | Internal | Technical architecture, security oversight (0.2 FTE) | | | | | | |
| SH-INT-003 | Lead Developer | Internal | Secure development, code review (0.3 FTE) | | | | | | |
| SH-INT-004 | Operations Lead | Internal | Infrastructure, incident response (0.2 FTE) | | | | | | |
| SH-INT-005 | DPO/Compliance | Internal | GDPR compliance, DPO function (0.1 FTE) | | | | | | |
| SH-EXT-001 | Customers (B2B) | External | Data subjects | | | | | | |
| SH-EXT-002 | Processors (hosting, email) | External | Data processing under DPA | | | | | | |
| SH-EXT-003 | Supervisory body (CNPD in PT) | External | GDPR Art. 51 authority | | | | | | |

---

## §5 Orphan rule references (legacy → freeze mapping)

| Orphan ref (legacy) | Doc 14/16 source | Closest freeze rule | Finding | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|---------------------|------------------|---------------------|---------|-------|-----------------------|----------|----------|--------------|-----------|
| CR-D-07.3-001 | Doc 14 (NODE-PROC-013) | BPR-D-07.2-001 (SAST/DAST) | F-S1-01 OPEN | | | | | | |
| CR-D-07.4-001 | Doc 14 (NODE-PROC-014) | BPR-D-07.2-001 | F-S1-02 OPEN | | | | | | |
| CR-D-10.1-001 | Doc 14 (NODE-SYS-001 SIEM) | CR-D-10.2-001 (Audit Logging) | F-S1-03 OPEN | | | | | | |
| CR-D-02.4-001 | Doc 16 | CR-D-02.2-001 (Patches) | F-S1-04 OPEN | | | | | | |
| CR-D-06.4-001 | Doc 16 | CR-D-06.3-001 (DPAs) | F-S1-05 OPEN | | | | | | |
| CR-D-08.3-001 | Doc 16 | CR-D-08.1-001 (Training) | F-S1-06 OPEN | | | | | | |
| CR-D-09.3-001 | Doc 16 | (orphan by design — DORA sole authority) | F-S1-07 OPEN | | | | | | |

See `RULE_FREEZE.md` §3.2 + §9 for full F-register.

---

## §6 Cross-references

- `RULE_FREEZE.md` §1 (46 rules), §2 (31 goals), §3 (drift table), §5 (UC enumeration)
- `CORPUS_LINKAGE.md` §3 (UC-to-D-XX.Y mapping)
- `NIST_ANCHORS.md` §3.1 (per-UC NIST anchors)
- `KG_CHAINS.md` §1 (CH-09: FR-29 → UC-25 → CR-D-04.3)
- `13a_Use_Case_Relationships.md` — `«include»` / `«extend»` graph
- `13b_Use_Case_Variability.md` — variant catalogue
- `annexes/A_Use_Case_Diagrams.md` — Mermaid diagrams (Sprint 3 fill)

---
### UC-1.1.1 — Data Subject Access Request (DSAR) [priority=CRITICAL, fields=17]

**Description:** Customer submits a verifiable DSAR via web form or email; system retrieves, assembles, and exports all personal data linked to the data subject identifier within 30 days.
**Scope:** Authenticated DSARs from data subjects (customers); portable export; JSON + CSV + PDF formats.
**Out of Scope:** Law-enforcement requests (separate process); subject-of-record disputes (legal counsel triage).
**Source:** GDPR Art. 15 + CR-D-05.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1
**Verification Criteria:**
- Sample of 10 DSARs completed within 30 calendar days.
- Output contains all data fields declared in RoPA §3.
- DSAR audit log entry present (PR.DS-10).
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** FR-07, NFR-21, NFR-22, NFR-26, NODE-SYS-014, NODE-PROC-006
**Risk if not met:** H — non-response within 30d triggers CNPD enforcement (Art. 83 GDPR fine up to 4% revenue).
**Affected Stakeholders:** Customer, DPO, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Implementation Priority:** HIGH
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- UC-1.1.1 t=uc priority=CRITICAL status=TODO -->

### UC-1.1.2 — Data Subject Rectification [priority=HIGH, fields=12]

**Description:** Customer requests correction of inaccurate personal data; system applies the correction across primary, backup, and analytics stores.
**Scope:** Customer-initiated correction requests; logged audit trail of edits.
**Out of Scope:** Third-party data correction (delegated to processor DPA).
**Source:** GDPR Art. 16 + CR-D-01.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02, PR.DS-10 | PF: CT.DM-P1, CT.DM-P3
**Verification Criteria:**
- All linked stores updated within 30 days.
- Hash/HMAC integrity preserved post-edit.
- Notification to processors via DPA within 7d.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** FR-11, NFR-06, NFR-28, NODE-SYS-016
**Risk if not met:** H — inaccurate data is a GDPR Art. 5(1)(d) breach.
**Affected Stakeholders:** Customer, DPO, Auditor

<!-- UC-1.1.2 t=uc priority=HIGH status=TODO -->

### UC-1.2.1 — Data Subject Erasure [priority=CRITICAL, fields=17]

**Description:** Customer requests deletion (right to be forgotten); system performs cryptographic erasure across primary store, backups, and downstream analytics within 30 days; emits erasure receipt.
**Scope:** All personal data linked to subject ID across primary, backups, logs, analytics.
**Out of Scope:** Legal-hold data (suspended until hold released); aggregated anonymised data (already unlinked).
**Source:** GDPR Art. 17 + CR-D-05.3-001
**NIST CSF Anchors:** CSF: GV.SC-04, PR.DS-10, PR.DS-02 | PF: CT.DM-P4, CT.DM-P5
**Verification Criteria:**
- Primary + backup + log stores fully erased within 30d.
- Cryptographic erasure verification (NIST SP 800-88) recorded.
- Third-party processors notified; DPAs cascade within 30d.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** FR-08, NFR-08, NFR-23, NODE-SYS-015, NODE-PROC-003
**Risk if not met:** H — incomplete erasure is GDPR Art. 17 violation + reputational damage.
**Affected Stakeholders:** Customer, DPO, Auditor
**Maturity Score:** Cur 1/4 → Tgt 4/4
**Implementation Priority:** HIGH
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- UC-1.2.1 t=uc priority=CRITICAL status=TODO -->

### UC-1.3.1 — Data Subject Data Export (portability) [priority=HIGH, fields=12]

**Description:** Customer requests a portable copy of their personal data in a structured, machine-readable format (JSON/CSV/PDF).
**Scope:** Personal data provided by the customer + observed usage data.
**Out of Scope:** Derived/inferred data not directly attributable to subject.
**Source:** GDPR Art. 20 + CR-D-05.4-001
**NIST CSF Anchors:** CSF: PR.DS-10, PR.AA-03, PR.DS-02 | PF: CT.DM-P1, CT.DM-P6
**Verification Criteria:**
- Export delivered ≤30 days with all declared fields.
- JSON + CSV + PDF all generated without manual steps.
- Customer authentication enforced prior to export.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** FR-09, NFR-24, NODE-SYS-014
**Risk if not met:** H — GDPR Art. 20 violation.
**Affected Stakeholders:** Customer, DPO, Auditor

<!-- UC-1.3.1 t=uc priority=HIGH status=TODO -->

### UC-1.4.1 — Consent Management [priority=HIGH, fields=12]

**Description:** Customer grants, modifies, or withdraws consent for each processing purpose; system records consent state and timestamps.
**Scope:** Marketing, analytics, third-party sharing purposes.
**Out of Scope:** Service-essential processing (legitimate interest, no consent).
**Source:** GDPR Art. 6(1)(a) + CR-D-05.1-001
**NIST CSF Anchors:** CSF: GV.OC-03, GV.PO-01, ID.AM-03 | PF: CT.DP-P4, CT.PO-P4, ID.RA-P3
**Verification Criteria:**
- Consent capture rate = 100% of new users.
- Withdrawal propagated to processors within 7 days (NFR-27).
- Audit log immutable for consent events.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** FR-10, NFR-26, NFR-27, NODE-PROC-007
**Risk if not met:** H — non-propagated withdrawal = GDPR Art. 7(3) violation.
**Affected Stakeholders:** Customer, DPO, Auditor

<!-- UC-1.4.1 t=uc priority=HIGH status=TODO -->

### UC-1.5.1 — Structured Data Portability [priority=MEDIUM, fields=12]

**Description:** System exposes a documented data-export schema and a machine-readable endpoint so customers and integrators can extract personal data without bespoke format negotiation.
**Scope:** Schema versioning; field-level documentation; rate-limited endpoint.
**Out of Scope:** Real-time streaming (batch only).
**Source:** GDPR Art. 20 + CR-D-05.4-001
**NIST CSF Anchors:** CSF: PR.DS-10, PR.AA-03, PR.DS-02 | PF: CT.DM-P1, CT.DM-P6
**Verification Criteria:**
- Schema documented and version-pinned.
- Endpoint authenticated; rate limit enforced.
- Sample export passes JSON Schema validator.
**Verification Method:** TEST
**Owner:** DPO
**Status:** TODO
**Dependencies:** FR-09, NFR-24, NODE-SYS-014
**Risk if not met:** M — minor GDPR Art. 20 risk if endpoint unavailable.
**Affected Stakeholders:** Customer, DPO, Auditor

<!-- UC-1.5.1 t=uc priority=MEDIUM status=TODO -->



### UC-2.1.1 — Vulnerability-Free Release [priority=CRITICAL, fields=17]

**Description:** Before each release, automated scanners detect known vulnerabilities in source, dependencies, and containers; release is blocked on critical findings.
**Scope:** Production releases only; SAST + SCA + container scan.
**Out of Scope:** Pre-alpha internal builds.
**Source:** CR-D-02.1-001
**NIST CSF Anchors:** CSF: GV.OV-02, ID.AM-02, ID.RA-01 | PF: ID.RA-P3, ID.RA-P5
**Verification Criteria:**
- 0 critical findings at release (Sprint 5 baseline).
- All SCA findings prioritised by CVSS + EPSS.
- Release audit log entry per build (PR.DS-01).
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** FR-17, FR-20, NFR-46, NODE-PROC-017, NODE-SYS-009
**Risk if not met:** H — unremediated critical = CRA Art. 14 actively-exploited obligation.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Implementation Priority:** HIGH
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- UC-2.1.1 t=uc priority=CRITICAL status=TODO -->

### UC-2.2.1 — Automated Patch Deployment [priority=CRITICAL, fields=17]

**Description:** Critical security patches applied within 24h; high within 7d; automated pipeline rolls back on health-check failure.
**Scope:** Production + staging environments.
**Out of Scope:** Third-party managed services (delegated to vendor SLA).
**Source:** CR-D-02.2-001
**NIST CSF Anchors:** CSF: GV.OV-02, ID.RA-01, PR.IR-03 | PF: —
**Verification Criteria:**
- Critical CVE patch median ≤24h measured monthly.
- Auto-rollback validated via chaos test (1×/quarter).
- Patch audit log immutable.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** FR-18, NFR-12, NODE-PROC-015
**Risk if not met:** H — extended exposure window = CRA Art. 14 incident trigger.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Implementation Priority:** HIGH
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- UC-2.2.1 t=uc priority=CRITICAL status=TODO -->

### UC-2.3.1 — Coordinated Vulnerability Disclosure [priority=HIGH, fields=12]

**Description:** Process to receive, triage, and respond to vulnerability reports from external researchers; publish CVE + remediation.
**Scope:** External researchers; published security.txt + dedicated mailbox.
**Out of Scope:** Customer support tickets (separate flow).
**Source:** CR-D-02.3-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.SC-04, RS.CO-03 | PF: —
**Verification Criteria:**
- security.txt present at /.well-known/security.txt.
- Median first response ≤72h from receipt.
- Disclosure policy published; CVE assigned for confirmed issues.
**Verification Method:** INSPECT
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** NODE-PROC-016, FR-13
**Risk if not met:** M — slow disclosure damages researcher trust + CRA reputation.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- UC-2.3.1 t=uc priority=HIGH status=TODO -->

### UC-2.4.1 — Exploit Severity Limitation [priority=CRITICAL, fields=17]

**Description:** Active exploit detected → fail-safe design kicks in: WAF rules + rate limits + automated rollback limit blast radius within 30 minutes.
**Scope:** Production traffic; runtime WAF + circuit breakers.
**Out of Scope:** DDoS at network edge (cloud provider responsibility).
**Source:** CR-D-04.1-001
**NIST CSF Anchors:** CSF: DE.AE-02, DE.CM-01, DE.CM-09 | PF: CM.AW-P7
**Verification Criteria:**
- Median exploit-containment ≤30min measured quarterly.
- Fail-safe design documented + chaos-tested annually.
- 0 undetected active exploits for >24h.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** FR-15, NFR-17, NODE-SYS-005, NODE-PROC-002
**Risk if not met:** H — uncontrolled exploit = GDPR breach + CRA Art. 14(4).
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Maturity Score:** Cur 1/4 → Tgt 4/4
**Implementation Priority:** HIGH
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- UC-2.4.1 t=uc priority=CRITICAL status=TODO -->

### UC-2.4.2 — DoS Resilience [priority=HIGH, fields=12]

**Description:** Application-layer DoS detected → automatic rate-limit + challenge + upstream scrubbing; RTO/RPO targets preserved.
**Scope:** L7 DoS; volumetric DoS delegated to CDN/edge.
**Out of Scope:** Edge-layer DDoS (cloud provider SLA).
**Source:** CR-D-04.2-001
**NIST CSF Anchors:** CSF: DE.CM-09, PR.DS-10, PR.IR-03 | PF: CT.DM-P10, PR.PO-P7
**Verification Criteria:**
- Chaos DoS test quarterly; recovery <24h.
- Availability ≥99.9% measured monthly.
- Runbook for L7 attack published.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** FR-19, NFR-10, NFR-16, NODE-SYS-005
**Risk if not met:** M — sustained outage = GDPR availability principle + revenue loss.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- UC-2.4.2 t=uc priority=HIGH status=TODO -->

### UC-2.5.1 — Incident Notification (24h ENISA, 72h GDPR) [priority=CRITICAL, fields=17]

**Description:** Confirmed security incident triggers dual notification: ≤24h ENISA for CRA-relevant vulnerabilities; ≤72h CNPD for personal-data breaches.
**Scope:** All confirmed incidents; severity matrix; pre-drafted templates.
**Out of Scope:** Suspected-only incidents (handled in triage).
**Source:** CR-D-04.3-001 (GDPR Art. 33 + CRA Art. 14)
**NIST CSF Anchors:** CSF: RS.CO-02, RS.MA-01, RS.MA-02 | PF: CM.AW-P7, CM.AW-P8, CM.PO-P1
**Verification Criteria:**
- ENISA notification median ≤24h; CNPD ≤72h.
- Tabletop exercise quarterly (NFR-17).
- Breach register entry ≤24h post-detection (NFR-43).
**Verification Method:** DEMONSTRATE
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** FR-16, NFR-29, NFR-44, NODE-SYS-004, NODE-PROC-001, NODE-ROLE-008
**Risk if not met:** H — late notification = GDPR Art. 83 fine + CRA sanctions.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Implementation Priority:** HIGH
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- UC-2.5.1 t=uc priority=CRITICAL status=TODO -->

### UC-2.6.1 — Data Restoration & Recovery [priority=HIGH, fields=12]

**Description:** Backup restore tested quarterly; RTO ≤24h, RPO ≤1h; restoration procedure documented and rehearsed.
**Scope:** Primary + backup data stores; recovery scenarios documented.
**Out of Scope:** Long-term archival restore (separate SLA).
**Source:** CR-D-04.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-10, PR.IR-03 | PF: —
**Verification Criteria:**
- Quarterly restore test passes RTO/RPO.
- Backup integrity verification (NFR-07) weekly.
- Recovery runbook signed off by Ops Lead.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** FR-19, NFR-14, NFR-15, NFR-16, NODE-SYS-015, NODE-PROC-003
**Risk if not met:** H — failed restore = data loss + GDPR availability breach.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- UC-2.6.1 t=uc priority=HIGH status=TODO -->



### UC-3.1.1 — User Authentication [priority=CRITICAL, fields=17]

**Description:** All users authenticate via central IdP; password + lockout + 30-min session timeout enforced for staff; rate-limited login.
**Scope:** Staff + customer authentication; central IdP.
**Out of Scope:** Service-account auth (uses mTLS, separate process).
**Source:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: —
**Verification Criteria:**
- Account lockout after 5 failed attempts (NFR-02).
- 30-min idle session timeout enforced.
- 100% authentication events logged (NFR-09).
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** FR-02, FR-06, NFR-01, NFR-02, NODE-SYS-006, NODE-SYS-011
**Risk if not met:** H — auth bypass = GDPR + CRA critical control failure.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Maturity Score:** Cur 3/4 → Tgt 4/4
**Implementation Priority:** HIGH
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- UC-3.1.1 t=uc priority=CRITICAL status=TODO -->

### UC-3.1.2 — MFA for Privileged Accounts [priority=CRITICAL, fields=17]

**Description:** Privileged accounts (admin, IAM, ops) require FIDO2-based MFA on every session; PAM records session activity.
**Scope:** Privileged staff; service admins.
**Out of Scope:** Standard users (MFA optional).
**Source:** CR-D-03.2-001
**NIST CSF Anchors:** CSF: PR.AA-03, PR.AA-04, PR.AA-05 | PF: —
**Verification Criteria:**
- 100% privileged sessions MFA-protected (NFR-01).
- PAM session recording for all admin actions.
- Quarterly access review of privileged accounts.
**Verification Method:** DEMONSTRATE
**Owner:** CTO
**Status:** TODO
**Dependencies:** FR-03, NFR-01, NODE-SYS-007
**Risk if not met:** H — privileged-account compromise = total system takeover risk.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Maturity Score:** Cur 3/4 → Tgt 4/4
**Implementation Priority:** HIGH
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- UC-3.1.2 t=uc priority=CRITICAL status=TODO -->

### UC-3.2.1 — Authorisation / Least Privilege [priority=HIGH, fields=12]

**Description:** Role-based access control (RBAC) with least-privilege principle; quarterly access reviews per role.
**Scope:** All internal staff; role taxonomy documented.
**Out of Scope:** Customer self-service roles.
**Source:** CR-D-03.3-001
**NIST CSF Anchors:** CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: CT.PO-P1
**Verification Criteria:**
- RBAC matrix documented and reviewed quarterly (NFR-25).
- Privilege creep detected via quarterly diff.
- Deprovisioning within 24h of termination (FR-04).
**Verification Method:** INSPECT
**Owner:** CTO
**Status:** TODO
**Dependencies:** FR-05, NFR-25, NODE-ROLE-004
**Risk if not met:** M — privilege creep = insider risk + GDPR Art. 32 violation.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- UC-3.2.1 t=uc priority=HIGH status=TODO -->

### UC-3.3.1 — Secure System Defaults [priority=HIGH, fields=12]

**Description:** Hardened-default baseline (CIS Control 4) applied to all production systems; deviations require security sign-off.
**Scope:** Production servers, containers, cloud accounts.
**Out of Scope:** Dev environments (relaxed baseline).
**Source:** CR-D-03.4-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.SC-03, PR.DS-10 | PF: CT.DP-P4, CT.PO-P4
**Verification Criteria:**
- CIS benchmark ≥95% compliance measured quarterly.
- All deviations documented and time-bound.
- Baseline re-evaluated on every new service.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** FR-06, NODE-SYS-008
**Risk if not met:** M — misconfiguration = most common breach vector.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- UC-3.3.1 t=uc priority=HIGH status=TODO -->

### UC-3.4.1 — Processing & Breach Records [priority=HIGH, fields=12]

**Description:** Records of Processing Activities (RoPA) maintained; breach register with detection + notification timestamps.
**Scope:** All processing activities involving personal data.
**Out of Scope:** Anonymised processing (no records needed).
**Source:** CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P8
**Verification Criteria:**
- RoPA updated within 7d of any processing change (NFR-35).
- Breach register entry within 24h of detection (NFR-43).
- RoPA accessible to DPO and supervisory body on request.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** FR-27, NFR-33, NFR-35, NODE-SYS-014, NODE-SYS-017
**Risk if not met:** M — outdated RoPA = GDPR Art. 30 violation.
**Affected Stakeholders:** Customer, DPO, Auditor

<!-- UC-3.4.1 t=uc priority=HIGH status=TODO -->

### UC-3.5.1 — Audit Logging [priority=HIGH, fields=12]

**Description:** Comprehensive audit logs (auth, admin, data access) shipped to SIEM with WORM storage; retention ≥12 months.
**Scope:** All production systems; SIEM integration.
**Out of Scope:** Dev environment logs (shorter retention).
**Source:** CR-D-10.2-001
**NIST CSF Anchors:** CSF: DE.CM-01, GV.PO-02, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9
**Verification Criteria:**
- 100% auth + admin events logged (NFR-09).
- Log retention ≥12 months (NFR-37).
- WORM storage prevents tampering (NFR-32).
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** FR-26, NFR-32, NFR-37, NODE-SYS-001/002/003
**Risk if not met:** H — incomplete logs = GDPR accountability gap.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- UC-3.5.1 t=uc priority=HIGH status=TODO -->

### UC-3.6.1 — Control Effectiveness Testing [priority=MEDIUM, fields=12]

**Description:** Annual penetration test + control-effectiveness review; findings tracked through to remediation.
**Scope:** External pentest + internal review; controls catalog.
**Out of Scope:** Bug bounty (separate programme).
**Source:** CR-D-10.3-001
**NIST CSF Anchors:** CSF: DE.AE-02, GV.OV-03, ID.RA-05 | PF: ID.RA-P3, ID.RA-P5
**Verification Criteria:**
- Annual pentest report published.
- 100% critical findings remediated within SLA.
- Controls catalog updated with test outcomes.
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** FR-28, NFR-46, NODE-SYS-009, NODE-PROC-020
**Risk if not met:** M — untested controls = undetected drift.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- UC-3.6.1 t=uc priority=MEDIUM status=TODO -->



### UC-4.1.1 — Security by Design (SSDLC) [priority=HIGH, fields=12]

**Description:** Secure SDLC gates integrated into development workflow: threat model, secure coding review, dependency checks.
**Scope:** All production code; threat model template.
**Out of Scope:** Internal tooling (relaxed SSDLC).
**Source:** CR-D-07.1-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.RA-01, PR.DS-10 | PF: CT.DP-P2, CT.DP-P4, GV.PO-P2
**Verification Criteria:**
- Threat model attached to every new feature RFC.
- Secure code review checklist signed off pre-merge.
- Quarterly SSDLC metrics dashboard reviewed.
**Verification Method:** DEMONSTRATE
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** FR-20, FR-21, NODE-PROC-007, NODE-PROC-009, NODE-PROC-010
**Risk if not met:** M — design flaws discovered late = costly remediation.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- UC-4.1.1 t=uc priority=HIGH status=TODO -->

### UC-4.2.1 — SAST/DAST in CI/CD [priority=HIGH, fields=12]

**Description:** SAST + DAST executed automatically on every PR; builds fail on critical findings.
**Scope:** All production repositories; CI/CD pipeline integration.
**Out of Scope:** Legacy repositories without CI integration.
**Source:** CR-D-07.2-001 (BPR)
**NIST CSF Anchors:** CSF: ID.RA-04, ID.RA-05, PR.PS-01 | PF: —
**Verification Criteria:**
- 100% PRs scanned before merge.
- Critical findings block merge.
- False-positive review process documented.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** FR-20, FR-21, NODE-SYS-012, NODE-PROC-008, NODE-PROC-013
**Risk if not met:** H — unscanned code = CRA + GDPR design defect risk.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- UC-4.2.1 t=uc priority=HIGH status=TODO -->

### UC-4.3.1 — Security Patch Deployment [priority=CRITICAL, fields=17]

**Description:** Security patches deployed via the change management process; emergency patch path documented for critical CVEs.
**Scope:** All production services; emergency vs normal patch flows.
**Out of Scope:** Third-party managed services (delegated to vendor).
**Source:** CR-D-02.2-001
**NIST CSF Anchors:** CSF: GV.OV-02, ID.RA-01, PR.IR-03 | PF: —
**Verification Criteria:**
- Median critical-patch deploy ≤24h.
- Change request signed off before production.
- Auto-rollback validated.
**Verification Method:** INSPECT
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** FR-18, FR-22, NFR-12, NODE-PROC-014, NODE-PROC-015
**Risk if not met:** H — unpatched = CRA Art. 14 active-exploit trigger.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Maturity Score:** Cur 2/4 → Tgt 4/4
**Implementation Priority:** HIGH
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- UC-4.3.1 t=uc priority=CRITICAL status=TODO -->

### UC-4.4.1 — Fail-Safe Design [priority=HIGH, fields=12]

**Description:** Components fail closed: misconfigurations, missing dependencies, or unexpected inputs default to safe state.
**Scope:** All production components; design pattern documented.
**Out of Scope:** UI-level graceful degradation (still user-visible).
**Source:** CR-D-04.1-001
**NIST CSF Anchors:** CSF: DE.AE-02, DE.CM-01, DE.CM-09 | PF: CM.AW-P7
**Verification Criteria:**
- Architecture review checklist includes fail-safe.
- Chaos test injects failures quarterly.
- No incident last 12m caused by fail-open design.
**Verification Method:** DEMONSTRATE
**Owner:** CTO
**Status:** TODO
**Dependencies:** FR-15, NODE-SYS-005
**Risk if not met:** M — fail-open = exploit amplification risk.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- UC-4.4.1 t=uc priority=HIGH status=TODO -->

### UC-4.5.1 — Pre-Launch Risk Assessment [priority=CRITICAL, fields=17]

**Description:** DPIA + cybersecurity risk assessment completed before any high-risk processing launches; signed off by Risk Owner.
**Scope:** All new features involving personal data or new attack surface.
**Out of Scope:** Bug fixes with no new risk surface.
**Source:** CR-D-09.2-001
**NIST CSF Anchors:** CSF: ID.RA-01, ID.RA-04, ID.RA-05 | PF: ID.RA-P3, ID.RA-P4, ID.RA-P5
**Verification Criteria:**
- DPIA completed before launch (NFR-31).
- Risk register entry per high-risk finding.
- DPO + Risk Owner sign-off before deploy.
**Verification Method:** DEMONSTRATE
**Owner:** Risk Owner
**Status:** TODO
**Dependencies:** FR-25, NFR-31, NFR-41, NODE-PROC-005, NODE-ROLE-006
**Risk if not met:** H — unassessed launch = GDPR Art. 35 violation.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Maturity Score:** Cur 1/4 → Tgt 4/4
**Implementation Priority:** HIGH
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- UC-4.5.1 t=uc priority=CRITICAL status=TODO -->



### UC-5.1.1 — Annual Policy Review [priority=HIGH, fields=12]

**Description:** Annual review of all security + privacy policies; updates documented and communicated.
**Scope:** All internal policies; ISO 27001 Annex A controls.
**Out of Scope:** Customer-facing terms (separate legal cycle).
**Source:** CR-D-09.1-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.PO-02, GV.RM-04 | PF: CM.PO-P1, GV.PO-P1, GV.PO-P5
**Verification Criteria:**
- All policies reviewed annually (NFR-38).
- Review minutes stored immutably.
- Changes communicated to staff within 7d.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** FR-25, NFR-38, NODE-PROC-004, NODE-ROLE-001
**Risk if not met:** M — stale policy = governance gap.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor

<!-- UC-5.1.1 t=uc priority=HIGH status=TODO -->

### UC-5.1.2 — Technical Documentation Maintenance [priority=HIGH, fields=12]

**Description:** Technical documentation (architecture, threat model, controls) maintained current; under change control.
**Scope:** Architecture diagrams, threat models, controls catalog.
**Out of Scope:** Code-level inline docs (separate).
**Source:** CR-D-09.1-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.PO-02, GV.OV-01 | PF: CM.PO-P1, GV.PO-P1
**Verification Criteria:**
- Documentation updated within 30d of change.
- CRA Annex I technical file current.
- Reviewed by CTO at least annually.
**Verification Method:** INSPECT
**Owner:** CTO
**Status:** TODO
**Dependencies:** NODE-ROLE-002, FR-25
**Risk if not met:** M — outdated docs = CRA Art. 31 compliance gap.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor

<!-- UC-5.1.2 t=uc priority=HIGH status=TODO -->

### UC-5.2.1 — DPIA Pre-Launch [priority=CRITICAL, fields=17]

**Description:** DPIA mandatory before any high-risk processing; documented risk treatment plan.
**Scope:** All high-risk processing (GDPR Art. 35 list + company policy).
**Out of Scope:** Low-risk routine processing.
**Source:** CR-D-09.2-001
**NIST CSF Anchors:** CSF: ID.RA-01, ID.RA-04, ID.RA-05 | PF: ID.RA-P3, ID.RA-P4, ID.RA-P5
**Verification Criteria:**
- DPIA completed before high-risk launch (NFR-31).
- Risk Owner + DPO sign-off recorded.
- Residual risk accepted by CEO where applicable.
**Verification Method:** DEMONSTRATE
**Owner:** Risk Owner
**Status:** TODO
**Dependencies:** FR-25, NFR-31, NODE-PROC-005, NODE-ROLE-006
**Risk if not met:** H — missing DPIA = GDPR Art. 35 violation + Art. 83 fine.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor
**Maturity Score:** Cur 1/4 → Tgt 4/4
**Implementation Priority:** HIGH
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- UC-5.2.1 t=uc priority=CRITICAL status=TODO -->

### UC-5.3.1 — RoPA Maintenance [priority=HIGH, fields=12]

**Description:** Records of Processing Activities (RoPA) maintained current; updated within 7 days of processing change.
**Scope:** All processing activities; controllers + processors listed.
**Out of Scope:** One-off ad-hoc processing.
**Source:** CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P4, ID.IM-P6
**Verification Criteria:**
- RoPA update ≤7d post-change (NFR-35).
- Annual full review completed.
- RoPA accessible to supervisory body on request.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** FR-27, NFR-33, NFR-35, NODE-SYS-014, NODE-PROC-006
**Risk if not met:** M — outdated RoPA = GDPR Art. 30 violation.
**Affected Stakeholders:** Customer, DPO, Auditor

<!-- UC-5.3.1 t=uc priority=HIGH status=TODO -->

### UC-5.4.1 — Processor Due Diligence [priority=HIGH, fields=12]

**Description:** Processor security + privacy due diligence before engagement; annual review thereafter.
**Scope:** All third-party processors with personal-data access.
**Out of Scope:** Non-data processors (e.g., office cleaning).
**Source:** CR-D-06.1-001
**NIST CSF Anchors:** CSF: GV.SC-01, GV.SC-02, GV.SC-03 | PF: ID.IM-P2
**Verification Criteria:**
- Security questionnaire completed pre-engagement.
- Annual vendor security assessment (NFR-40).
- Findings tracked to remediation.
**Verification Method:** INSPECT
**Owner:** Procurement Lead
**Status:** TODO
**Dependencies:** FR-28, NFR-40, NODE-PROC-011, NODE-ROLE-009
**Risk if not met:** H — substandard processor = GDPR Art. 28 violation.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor

<!-- UC-5.4.1 t=uc priority=HIGH status=TODO -->

### UC-5.5.1 — DPAs Binding Processors [priority=HIGH, fields=12]

**Description:** Data Processing Agreements (DPAs) signed with all processors before data transfer; reviewed annually.
**Scope:** All processors with personal-data access.
**Out of Scope:** Non-data vendors.
**Source:** CR-D-06.3-001
**NIST CSF Anchors:** CSF: GV.OC-03, GV.SC-02, GV.SC-03 | PF: —
**Verification Criteria:**
- 100% active processors have signed DPAs.
- DPAs reviewed annually.
- GDPR Art. 28 mandatory clauses present.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** NODE-PROC-012, NODE-ROLE-011
**Risk if not met:** H — missing DPA = GDPR Art. 28 violation.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor

<!-- UC-5.5.1 t=uc priority=HIGH status=TODO -->

### UC-5.6.1 — SBOM Publication [priority=HIGH, fields=12]

**Description:** Software Bill of Materials (SBOM) generated per release in CycloneDX/SPDX format; published to customer portal.
**Scope:** All production releases.
**Out of Scope:** Internal tooling releases.
**Source:** CR-D-06.2-001
**NIST CSF Anchors:** CSF: GV.SC-02, GV.SC-03, ID.RA-01 | PF: —
**Verification Criteria:**
- SBOM generated per release (NFR-45).
- CycloneDX/SPDX format validated.
- Customer portal access tested.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** FR-23, NFR-45, NODE-SYS-013
**Risk if not met:** M — missing SBOM = CRA Art. 13 transparency gap.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- UC-5.6.1 t=uc priority=HIGH status=TODO -->



### UC-6.1.1 — Annual Awareness Training [priority=MEDIUM, fields=12]

**Description:** All staff complete annual security + privacy awareness training; completion tracked.
**Scope:** All employees + long-term contractors.
**Out of Scope:** Customers (separate).
**Source:** CR-D-08.1-001
**NIST CSF Anchors:** CSF: PR.AT-01, PR.AT-02, PR.PS-01 | PF: GV.AT-P1, GV.AT-P2
**Verification Criteria:**
- 100% completion rate (NFR-36).
- Training refreshed annually.
- Quiz pass required.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** FR-29, NFR-36, NODE-PROC-018
**Risk if not met:** M — untrained staff = phishing risk + GDPR Art. 39 gap.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor

<!-- UC-6.1.1 t=uc priority=MEDIUM status=TODO -->

### UC-6.2.1 — Role-Specific Training [priority=MEDIUM, fields=12]

**Description:** Role-specific security training for engineers, ops, DPO; curriculum aligned with responsibilities.
**Scope:** Engineers, ops, DPO, IAM admin.
**Out of Scope:** General awareness (covered in UC-6.1.1).
**Source:** CR-D-08.2-001
**NIST CSF Anchors:** CSF: GV.RR-02, GV.RR-04, PR.AT-02 | PF: GV.AT-P1, GV.AT-P2
**Verification Criteria:**
- Role curricula documented per role.
- Completion tracked per role.
- Updated annually.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** FR-29, NFR-36, NODE-PROC-019, NODE-ROLE-002, NODE-ROLE-003
**Risk if not met:** M — role gaps = competency risk.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor

<!-- UC-6.2.1 t=uc priority=MEDIUM status=TODO -->

### UC-6.3.1 — Phishing Simulation [priority=LOW, fields=12]

**Description:** Quarterly phishing simulation; click-rate tracked + re-education for repeat offenders.
**Scope:** All staff with email.
**Out of Scope:** External addresses.
**Source:** CR-D-08.1-001
**NIST CSF Anchors:** CSF: PR.AT-01, PR.AT-02, PR.PS-01 | PF: GV.AT-P1, GV.AT-P2
**Verification Criteria:**
- Quarterly simulation executed.
- Click rate trend reported quarterly.
- Re-education for repeat clickers.
**Verification Method:** TEST
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** FR-30, NFR-01
**Risk if not met:** L — phishing is a leading breach vector; sim reduces risk.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor

<!-- UC-6.3.1 t=uc priority=LOW status=TODO -->




**End of Use Cases Catalog (Phase 3 RICH, ADJUSTED_FIELDS, Sprint 4)**
