---
document_id: AEGIS-P3-RICH-14
title: Architectural Nodes — TinyTask SaaS (Phase 3 RICH)
phase: 3
version: 2.0
created: 2026-08-24
updated: 2026-08-24
author: Fase de Especificação 4 Executor (paulo@methodology.pt)
status: DEEP_ENRICHED
deep_enrichment_date: 2026-08-24
detail_cards_count: 49
cells_count: 648
fields_per_card: 17|12|tiered
tier_distribution: "NODE cards (12 with 17 fields + 37 with 12 fields)"
sprint_role: deep_enrichment_per_card
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [13_Use_Cases_Catalog.md, 11_Rules_Catalog.md, RULE_FREEZE.md, CORPUS_LINKAGE.md]
outputs: [15_Requirements_Allocation.md, 16_Compliance_Gates_Report.md]
related_documents: [13_Use_Cases_Catalog.md, 15_Requirements_Allocation.md, CORPUS_LINKAGE.md, RULE_FREEZE.md]
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Implementation Status, Priority, Stakeholders, Reporting]
freeze_total_nodes: 49
freeze_total_node_tech: 17
freeze_total_node_proc: 20
freeze_total_node_role: 12
reconciliation_note: "49 nodes freeze (17 TECH + 20 PROC + 12 ROLE); 3 orphan CR-D refs flagged F-S1-01/02/03."
sprint5_note: "Fase de Especificação 5: DEEP enrichment — 49 cards (12×17 fields + 37×12 fields) = 648 cells. Frontmatter status DEEP_ENRICHED, version 2.0."
---

# Architectural Nodes — TinyTask SaaS (Phase 3 RICH)

> **Status:** ADJUSTED_FIELDS. 49 nodes: 17 NODE-SYS (TECH) + 20 NODE-PROC (PROC) + 12 NODE-ROLE.

---

## §1 Reconciliation Notes

This document consolidates all architectural nodes: Process (PROC), IT-System (TECH), and Human-Role (ROLE) per the ARM class model.

**Authoritative sources:**
- `RULE_FREEZE.md` §1 — 46 rules (CR + BPR).
- `CORPUS_LINKAGE.md` §6 — 49 nodes-to-D-XX.Y mapping.
- `NIST_ANCHORS.md` §3 — per-artefact NIST anchors.
- `KG_CHAINS.md` §1 — CH-12 (NODE-PROC-001 → CR-D-04.3).

**Gate criteria (legacy §1):**
- All nodes trace to ≥1 UC (`13_Use_Cases_Catalog.md` §3).
- All nodes map to ≥1 D-XX.Y sub-domain (`CORPUS_LINKAGE.md` §6).
- No node is standalone without UC link.

---

## §2 NODE-SYS (TECH) — 17

| Node ID | Type | D-subdomain | Purpose | Primary UC | Orphan ref? | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|---------|------|-------------|---------|-----------|-------------|-------|-----------------------|----------|----------|--------------|-----------|
| NODE-SYS-001 | TECH | D-10.2 | SIEM platform (log aggregation, correlation) | U.C.3.5.1, U.C.2.1.1 | CR-D-10.1-001 (F-S1-03) → CR-D-10.2-001 | | | | | | |
| NODE-SYS-002 | TECH | D-10.2 | Audit log store (immutable, ≥12 months) | U.C.3.5.1 | — | | | | | | |
| NODE-SYS-003 | TECH | D-10.2 | Log forwarder (TLS-protected transport) | U.C.3.5.1 | — | | | | | | |
| NODE-SYS-004 | TECH | D-04.3 | Incident management platform | U.C.2.5.1 | — | | | | | | |
| NODE-SYS-005 | TECH | D-04.1 | WAF / fail-safe gateway | U.C.2.4.1, U.C.4.4.1 | — | | | | | | |
| NODE-SYS-006 | TECH | D-03.1 | Identity Provider (IdP) | U.C.3.1.1 | — | | | | | | |
| NODE-SYS-007 | TECH | D-03.1 | Privileged Access Management (PAM) | U.C.3.1.2 | — | | | | | | |
| NODE-SYS-008 | TECH | D-03.4 | Configuration baseline (hardened-default) | U.C.3.3.1 | — | | | | | | |
| NODE-SYS-009 | TECH | D-10.3 | Penetration testing platform | U.C.3.6.1 | — | | | | | | |
| NODE-SYS-010 | TECH | D-01.1 | Encryption-at-rest (data store) | U.C.1.1.1 | — | | | | | | |
| NODE-SYS-011 | TECH | D-01.2 | TLS terminator (data in transit) | U.C.3.1.1 | — | | | | | | |
| NODE-SYS-012 | TECH | D-07.2 | CI/CD pipeline (SAST/DAST integration) | U.C.4.2.1 | CR-D-07.3-001 (F-S1-01) → BPR-D-07.2-001 | | | | | | |
| NODE-SYS-013 | TECH | D-06.2 | SBOM generator (CycloneDX/SPDX) | U.C.5.6.1 | — | | | | | | |
| NODE-SYS-014 | TECH | D-09.4 | Records-of-Processing store | U.C.5.3.1 | — | | | | | | |
| NODE-SYS-015 | TECH | D-04.4 | Backup & restore service | U.C.2.6.1 | — | | | | | | |
| NODE-SYS-016 | TECH | D-01.4 | Integrity verification (HMAC, checksums) | U.C.1.1.2 | — | | | | | | |
| NODE-SYS-017 | TECH | D-09.4 | Breach register | U.C.2.5.1, U.C.5.3.1 | — | | | | | | |

## §3 NODE-PROC (PROC) — 20

| Node ID | Type | D-subdomain | Purpose | Primary UC | Orphan ref? | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|---------|------|-------------|---------|-----------|-------------|-------|-----------------------|----------|----------|--------------|-----------|
| NODE-PROC-001 | PROC | D-04.3 | Unified Incident Response process | U.C.2.5.1 | — (CH-12 INFERRED link) | | | | | | |
| NODE-PROC-002 | PROC | D-04.1 | Exploit mitigation process | U.C.2.4.1 | — | | | | | | |
| NODE-PROC-003 | PROC | D-04.4 | Data restoration process | U.C.2.6.1 | — | | | | | | |
| NODE-PROC-004 | PROC | D-09.1 | Annual policy review process | U.C.5.1.1 | — | | | | | | |
| NODE-PROC-005 | PROC | D-09.2 | Risk assessment process | U.C.4.5.1, U.C.5.2.1 | — | | | | | | |
| NODE-PROC-006 | PROC | D-09.4 | RoPA maintenance process | U.C.5.3.1 | — | | | | | | |
| NODE-PROC-007 | PROC | D-07.1 | Secure SDLC process | U.C.4.1.1 | — | | | | | | |
| NODE-PROC-008 | PROC | D-07.2 | SAST/DAST execution process | U.C.4.2.1 | CR-D-07.3-001 (F-S1-01) → BPR-D-07.2-001 | | | | | | |
| NODE-PROC-009 | PROC | D-07.1 | Code review process | U.C.4.1.1 | — | | | | | | |
| NODE-PROC-010 | PROC | D-07.1 | Secret management process | U.C.4.1.1 | — | | | | | | |
| NODE-PROC-011 | PROC | D-06.1 | Processor due-diligence process | U.C.5.4.1 | — | | | | | | |
| NODE-PROC-012 | PROC | D-06.3 | DPA lifecycle process | U.C.5.5.1 | — | | | | | | |
| NODE-PROC-013 | PROC | D-07.2 | CI/CD security gate process | U.C.4.2.1 | CR-D-07.3-001 (F-S1-01) → BPR-D-07.2-001 | | | | | | |
| NODE-PROC-014 | PROC | D-07.2 | Change management process | U.C.4.3.1 | CR-D-07.4-001 (F-S1-02) → BPR-D-07.2-001 | | | | | | |
| NODE-PROC-015 | PROC | D-02.2 | Patch deployment process | U.C.4.3.1 | — | | | | | | |
| NODE-PROC-016 | PROC | D-02.3 | Coordinated Vulnerability Disclosure process | U.C.2.3.1 | — | | | | | | |
| NODE-PROC-017 | PROC | D-02.1 | Vulnerability scan process | U.C.2.1.1 | — | | | | | | |
| NODE-PROC-018 | PROC | D-08.1 | Annual awareness training process | U.C.6.1.1 | — | | | | | | |
| NODE-PROC-019 | PROC | D-08.2 | Role-specific training process | U.C.6.2.1 | — | | | | | | |
| NODE-PROC-020 | PROC | D-10.3 | Annual penetration testing process | U.C.3.6.1 | — | | | | | | |

## §4 NODE-ROLE (ROLE) — 12

| Node ID | Type | D-subdomain | Role | Responsibilities | Primary UC | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|---------|------|-------------|------|-----------------|-----------|-------|-----------------------|----------|----------|--------------|-----------|
| NODE-ROLE-001 | ROLE | D-09.1 | CEO | Business decisions, risk acceptance | U.C.5.1.1 | | | | | | |
| NODE-ROLE-002 | ROLE | D-08.2 | CTO | Technical architecture, security oversight | U.C.5.1.2 | | | | | | |
| NODE-ROLE-003 | ROLE | D-08.2 | Lead Developer | Secure development, code review | U.C.4.1.1, U.C.4.2.1 | | | | | | |
| NODE-ROLE-004 | ROLE | D-03.3 | IAM Admin | RBAC management, access reviews | U.C.3.2.1 | | | | | | |
| NODE-ROLE-005 | ROLE | D-08.1 | Operations Lead | Infrastructure, incident response | U.C.2.5.1 | | | | | | |
| NODE-ROLE-006 | ROLE | D-09.2 | Risk Owner | DPIA, risk assessment | U.C.4.5.1, U.C.5.2.1 | | | | | | |
| NODE-ROLE-007 | ROLE | D-09.4 | DPO | RoPA, breach records, supervisory liaison | U.C.5.3.1, U.C.2.5.1 | | | | | | |
| NODE-ROLE-008 | ROLE | D-04.3 | Incident Commander | 24h ENISA, 72h GDPR notification | U.C.2.5.1 | | | | | | |
| NODE-ROLE-009 | ROLE | D-06.1 | Procurement Lead | Processor due diligence | U.C.5.4.1 | | | | | | |
| NODE-ROLE-010 | ROLE | D-04.1 | Security Engineer | Exploit severity mitigation | U.C.2.4.1 | | | | | | |
| NODE-ROLE-011 | ROLE | D-06.3 | Legal Counsel | DPA lifecycle | U.C.5.5.1 | | | | | | |
| NODE-ROLE-012 | ROLE | D-09.1 | Compliance Manager | Annual policy review, audits | U.C.5.1.1 | | | | | | |

---

## §5 Orphan rule refs (legacy → freeze)

| Orphan ref (legacy) | Appears in | Closest freeze rule | Finding | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|---------------------|-----------|---------------------|---------|-------|-----------------------|----------|----------|--------------|-----------|
| CR-D-07.3-001 | NODE-SYS-012, NODE-PROC-008, NODE-PROC-013 | BPR-D-07.2-001 (SAST/DAST) | F-S1-01 OPEN | | | | | | |
| CR-D-07.4-001 | NODE-PROC-014 | BPR-D-07.2-001 | F-S1-02 OPEN | | | | | | |
| CR-D-10.1-001 | NODE-SYS-001 (SIEM) | CR-D-10.2-001 (Audit Logging) | F-S1-03 OPEN | | | | | | |

See `RULE_FREEZE.md` §3.2 + §9 for full F-register.

---

## §6 Cross-references

- `13_Use_Cases_Catalog.md` §3 — UC catalogue
- `15_Requirements_Allocation.md` §2 — DN rows
- `16_Compliance_Gates_Report.md` §2 — Gate rows
- `CORPUS_LINKAGE.md` §6 — full 49-node mapping
- `RULE_FREEZE.md` §1 — rule freeze
- `KG_CHAINS.md` §1 CH-12 — NODE-PROC-001 → CR-D-04.3

---
### NODE-ROLE-001 — CEO [track=CAPABILITY_SUBREQ, fields=17]

**Description:** Chief Executive Officer — accountable for risk acceptance and budget approval for security programme.
**Scope:** Strategic decisions; risk acceptance; final escalation.
**Out of Scope:** Day-to-day operational decisions.
**Source:** CR-D-09.1-001 (Risk acceptance)
**NIST CSF Anchors:** CSF: GV.PO-01, GV.PO-02, GV.RM-04 | PF: CM.PO-P1, GV.PO-P1, GV.PO-P5
**Verification Criteria:**
- Annual security budget approved.
- Risk acceptance documented.
- Annual policy review approved.
**Verification Method:** INSPECT
**Owner:** CEO
**Status:** TODO
**Dependencies:** U.C.5.1.1, NODE-PROC-004
**Risk if not met:** M — uninformed CEO = mis-prioritisation.
**Affected Stakeholders:** CEO, Board, Compliance Manager
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** CAPABILITY_SUBREQ
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NODE-ROLE-001 t=node level=L1_PRIMARY track=CAPABILITY_SUBREQ status=TODO -->

### NODE-ROLE-002 — CTO [track=CAPABILITY_SUBREQ, fields=17]

**Description:** Chief Technology Officer — accountable for technical architecture, security oversight, technical documentation.
**Scope:** All technical decisions; architecture review board chair.
**Out of Scope:** Business / commercial decisions.
**Source:** CR-D-09.1-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.PO-02, GV.OV-01 | PF: CM.PO-P1, GV.PO-P1
**Verification Criteria:**
- Technical documentation current.
- Architecture reviews attended.
- Security metrics reviewed.
**Verification Method:** INSPECT
**Owner:** CTO
**Status:** TODO
**Dependencies:** U.C.5.1.2, NODE-SYS-006
**Risk if not met:** M — uninformed CTO = tech drift.
**Affected Stakeholders:** CTO, Lead Developer, Compliance Manager
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** CAPABILITY_SUBREQ
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NODE-ROLE-002 t=node level=L1_PRIMARY track=CAPABILITY_SUBREQ status=TODO -->

### NODE-ROLE-003 — Lead Developer [track=ROLE, fields=12]

**Description:** Lead Developer — accountable for secure development, code review, SSDLC execution.
**Scope:** All production code; SSDLC gatekeeper.
**Out of Scope:** Non-prod tooling.
**Source:** CR-D-07.1-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.RA-01, PR.DS-10 | PF: CT.DP-P2, CT.DP-P4
**Verification Criteria:**
- Code reviews completed.
- Threat models attached.
- Security metrics tracked.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.4.1.1, U.C.4.2.1, NODE-PROC-007/009
**Risk if not met:** M — weak gate = defects ship.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-ROLE-003 t=node level=L1_PRIMARY track=ROLE status=TODO -->

### NODE-ROLE-004 — IAM Admin [track=ROLE, fields=12]

**Description:** Identity & Access Management administrator — RBAC, access reviews, deprovisioning.
**Scope:** All internal identities.
**Out of Scope:** Customer identities (separate).
**Source:** CR-D-03.3-001
**NIST CSF Anchors:** CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: CT.PO-P1
**Verification Criteria:**
- Quarterly access reviews (NFR-25).
- Deprovisioning ≤24h.
- Privilege creep detected.
**Verification Method:** INSPECT
**Owner:** IAM Admin
**Status:** TODO
**Dependencies:** U.C.3.2.1
**Risk if not met:** M — privilege drift = insider risk.
**Affected Stakeholders:** IAM Admin, CTO, Auditor

<!-- NODE-ROLE-004 t=node level=L1_PRIMARY track=ROLE status=TODO -->

### NODE-ROLE-005 — Operations Lead [track=ROLE, fields=12]

**Description:** Operations Lead — accountable for infrastructure, incident response coordination.
**Scope:** Production infrastructure; on-call rotation.
**Out of Scope:** Application code.
**Source:** CR-D-04.3-001
**NIST CSF Anchors:** CSF: RS.CO-02, RS.MA-01, RS.MA-02 | PF: CM.AW-P7
**Verification Criteria:**
- On-call coverage 24/7.
- Tabletop participation.
- Backup integrity verified.
**Verification Method:** DEMONSTRATE
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** U.C.2.5.1, NODE-SYS-004
**Risk if not met:** H — slow response = regulator fine.
**Affected Stakeholders:** Operations Lead, Incident Commander

<!-- NODE-ROLE-005 t=node level=L1_PRIMARY track=ROLE status=TODO -->

### NODE-ROLE-006 — Risk Owner [track=ROLE, fields=12]

**Description:** Risk Owner — accountable for DPIA execution, risk register, risk treatment plans.
**Scope:** All high-risk processing; risk register.
**Out of Scope:** Low-risk processing.
**Source:** CR-D-09.2-001
**NIST CSF Anchors:** CSF: ID.RA-01, ID.RA-04, ID.RA-05 | PF: ID.RA-P3, ID.RA-P4, ID.RA-P5
**Verification Criteria:**
- DPIA before high-risk launch.
- Risk register updated.
- Treatment plans tracked.
**Verification Method:** DEMONSTRATE
**Owner:** Risk Owner
**Status:** TODO
**Dependencies:** U.C.4.5.1, U.C.5.2.1, NODE-PROC-005
**Risk if not met:** H — missing DPIA = Art. 35 violation.
**Affected Stakeholders:** Risk Owner, DPO, Compliance Manager

<!-- NODE-ROLE-006 t=node level=L1_PRIMARY track=ROLE status=TODO -->

### NODE-ROLE-007 — DPO [track=ROLE, fields=12]

**Description:** Data Protection Officer — accountable for GDPR compliance, RoPA, breach records, supervisory liaison.
**Scope:** All personal-data processing.
**Out of Scope:** Non-personal-data processing.
**Source:** CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P8
**Verification Criteria:**
- RoPA maintained.
- Breach register entry ≤24h.
- Supervisory liaison documented.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** U.C.5.3.1, U.C.2.5.1, NODE-SYS-014, NODE-SYS-017
**Risk if not met:** H — DPO gap = Art. 37 violation.
**Affected Stakeholders:** DPO, Compliance Manager, CEO

<!-- NODE-ROLE-007 t=node level=L1_PRIMARY track=ROLE status=TODO -->

### NODE-ROLE-008 — Incident Commander [track=CAPABILITY_SUBREQ, fields=17]

**Description:** Incident Commander — accountable for regulatory notification within 24h ENISA + 72h GDPR deadlines.
**Scope:** All confirmed security incidents.
**Out of Scope:** Customer support.
**Source:** CR-D-04.3-001
**NIST CSF Anchors:** CSF: RS.CO-02, RS.MA-01, RS.MA-02 | PF: CM.AW-P7, CM.AW-P8, CM.PO-P1
**Verification Criteria:**
- Notification within SLA.
- Tabletop participation.
- Postmortem within 5d.
**Verification Method:** DEMONSTRATE
**Owner:** Incident Commander
**Status:** TODO
**Dependencies:** U.C.2.5.1, NODE-SYS-004, NODE-PROC-001
**Risk if not met:** H — late notification = regulator fine.
**Affected Stakeholders:** Incident Commander, DPO, Operations Lead
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** CAPABILITY_SUBREQ
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NODE-ROLE-008 t=node level=L1_PRIMARY track=CAPABILITY_SUBREQ status=TODO -->

### NODE-ROLE-009 — Procurement Lead [track=ROLE, fields=12]

**Description:** Procurement Lead — accountable for processor due diligence + DPA execution.
**Scope:** All data processors.
**Out of Scope:** Non-data vendors.
**Source:** CR-D-06.1-001
**NIST CSF Anchors:** CSF: GV.SC-01, GV.SC-02, GV.SC-03 | PF: ID.IM-P2
**Verification Criteria:**
- Questionnaire completed.
- DPA signed.
- Annual review (NFR-40).
**Verification Method:** INSPECT
**Owner:** Procurement Lead
**Status:** TODO
**Dependencies:** U.C.5.4.1, NODE-PROC-011
**Risk if not met:** H — substandard processor = Art. 28 violation.
**Affected Stakeholders:** Procurement Lead, DPO, Legal Counsel

<!-- NODE-ROLE-009 t=node level=L1_PRIMARY track=ROLE status=TODO -->

### NODE-ROLE-010 — Security Engineer [track=ROLE, fields=12]

**Description:** Security Engineer — accountable for exploit severity mitigation, WAF rules, vulnerability triage.
**Scope:** Active incidents + WAF tuning.
**Out of Scope:** Architecture decisions (CTO-owned).
**Source:** CR-D-04.1-001
**NIST CSF Anchors:** CSF: DE.AE-02, DE.CM-01, DE.CM-09 | PF: CM.AW-P7
**Verification Criteria:**
- Containment ≤30min median.
- WAF rules reviewed quarterly.
- Pentest findings remediated.
**Verification Method:** DEMONSTRATE
**Owner:** Security Engineer
**Status:** TODO
**Dependencies:** U.C.2.4.1, NODE-SYS-005, NODE-SYS-009
**Risk if not met:** H — uncontrolled exploit = breach.
**Affected Stakeholders:** Security Engineer, Operations Lead, CTO

<!-- NODE-ROLE-010 t=node level=L1_PRIMARY track=ROLE status=TODO -->

### NODE-ROLE-011 — Legal Counsel [track=ROLE, fields=12]

**Description:** Legal Counsel — accountable for DPA lifecycle, regulatory analysis.
**Scope:** All DPAs; regulatory interpretation.
**Out of Scope:** Operational security.
**Source:** CR-D-06.3-001
**NIST CSF Anchors:** CSF: GV.OC-03, GV.SC-02, GV.SC-03 | PF: —
**Verification Criteria:**
- 100% processors with DPA.
- Annual DPA review.
- Legal sign-off for template changes.
**Verification Method:** INSPECT
**Owner:** Legal Counsel
**Status:** TODO
**Dependencies:** U.C.5.5.1, NODE-PROC-012
**Risk if not met:** M — DPA gap = Art. 28 violation.
**Affected Stakeholders:** Legal Counsel, DPO, Procurement Lead

<!-- NODE-ROLE-011 t=node level=L1_PRIMARY track=ROLE status=TODO -->

### NODE-ROLE-012 — Compliance Manager [track=ROLE, fields=12]

**Description:** Compliance Manager — accountable for annual policy review, audit liaison, training programme.
**Scope:** All compliance artefacts.
**Out of Scope:** Engineering decisions.
**Source:** CR-D-09.1-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.PO-02, GV.OV-01 | PF: CM.PO-P1, GV.PO-P1
**Verification Criteria:**
- Annual review completed.
- Training completion 100% (NFR-36).
- Audit findings tracked.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** U.C.5.1.1, NODE-PROC-004, NODE-PROC-018
**Risk if not met:** M — governance gap = audit finding.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor

<!-- NODE-ROLE-012 t=node level=L1_PRIMARY track=ROLE status=TODO -->



### NODE-PROC-001 — Unified Incident Response process [track=PROCESS, fields=17]

**Description:** End-to-end process: detect → triage → contain → eradicate → recover → notify; covers both GDPR and CRA timelines.
**Scope:** All security incidents; pre-defined severity matrix.
**Out of Scope:** Customer support tickets.
**Source:** CR-D-04.3-001
**NIST CSF Anchors:** CSF: RS.CO-02, RS.MA-01, RS.MA-02 | PF: CM.AW-P7, CM.AW-P8, CM.PO-P1
**Verification Criteria:**
- Tabletop quarterly.
- Runbook signed off annually.
- Median MTTR tracked.
**Verification Method:** DEMONSTRATE
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** U.C.2.5.1, NODE-SYS-004, NODE-ROLE-008
**Risk if not met:** H — slow incident = dual-regulator fine.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** PROCESS
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NODE-PROC-001 t=node level=L1_PRIMARY track=PROCESS status=TODO -->

### NODE-PROC-002 — Exploit mitigation process [track=PROC, fields=12]

**Description:** Process to contain active exploit: isolate, patch, monitor, document.
**Scope:** Confirmed active exploits only.
**Out of Scope:** Theoretical vulnerabilities.
**Source:** CR-D-04.1-001
**NIST CSF Anchors:** CSF: DE.AE-02, DE.CM-01, DE.CM-09 | PF: CM.AW-P7
**Verification Criteria:**
- Containment ≤30min median.
- Postmortem within 5d.
- Lessons learned tracked.
**Verification Method:** DEMONSTRATE
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** U.C.2.4.1, NODE-SYS-005
**Risk if not met:** H — uncontrolled exploit = breach.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-PROC-002 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-003 — Data restoration process [track=PROC, fields=12]

**Description:** Process to restore data from backups with RTO/RPO targets; quarterly drill.
**Scope:** Production + critical backups.
**Out of Scope:** Archived data.
**Source:** CR-D-04.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-10, PR.IR-03 | PF: —
**Verification Criteria:**
- RTO ≤24h, RPO ≤1h (NFR-14,15).
- Quarterly drill.
- Runbook signed off.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** U.C.2.6.1, NODE-SYS-015
**Risk if not met:** H — failed restore = data loss.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- NODE-PROC-003 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-004 — Annual policy review process [track=PROC, fields=12]

**Description:** Process to review all security + privacy policies annually; documented updates; staff communication.
**Scope:** All internal policies.
**Out of Scope:** Customer-facing terms.
**Source:** CR-D-09.1-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.PO-02, GV.RM-04 | PF: CM.PO-P1, GV.PO-P1, GV.PO-P5
**Verification Criteria:**
- Annual review for 100% of policies.
- Update communication ≤7d.
- Review minutes stored immutably.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** U.C.5.1.1, NODE-ROLE-001, NODE-ROLE-012
**Risk if not met:** M — stale policy = governance gap.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor

<!-- NODE-PROC-004 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-005 — Risk assessment process [track=PROC, fields=12]

**Description:** Unified risk assessment process: identify, analyse, evaluate, treat; combines DPIA + cybersecurity risk.
**Scope:** Pre-launch + annual cycle.
**Out of Scope:** One-off ad-hoc.
**Source:** CR-D-09.2-001
**NIST CSF Anchors:** CSF: ID.RA-01, ID.RA-04, ID.RA-05 | PF: ID.RA-P3, ID.RA-P4, ID.RA-P5
**Verification Criteria:**
- Annual full review.
- Pre-launch per high-risk feature.
- Risk register maintained.
**Verification Method:** DEMONSTRATE
**Owner:** Risk Owner
**Status:** TODO
**Dependencies:** U.C.4.5.1, U.C.5.2.1, NODE-ROLE-006
**Risk if not met:** H — missed assessment = GDPR Art. 35.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor

<!-- NODE-PROC-005 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-006 — RoPA maintenance process [track=PROC, fields=12]

**Description:** Process to maintain RoPA; quarterly review + update ≤7d of any processing change.
**Scope:** All processing activities.
**Out of Scope:** Anonymised processing.
**Source:** CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P4, ID.IM-P6
**Verification Criteria:**
- Update ≤7d (NFR-35).
- Quarterly full review.
- DPO sign-off.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** U.C.5.3.1, NODE-SYS-014
**Risk if not met:** M — outdated RoPA = Art. 30 violation.
**Affected Stakeholders:** Customer, DPO, Auditor

<!-- NODE-PROC-006 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-007 — Secure SDLC process [track=PROCESS, fields=17]

**Description:** End-to-end SSDLC: requirements → design → code → test → release; security gates at each phase.
**Scope:** All production code.
**Out of Scope:** Internal tooling.
**Source:** CR-D-07.1-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.RA-01, PR.DS-10 | PF: CT.DP-P2, CT.DP-P4, GV.PO-P2
**Verification Criteria:**
- Threat model per feature.
- Pre-merge review checklist.
- Quarterly metrics.
**Verification Method:** DEMONSTRATE
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.4.1.1, NODE-PROC-009, NODE-PROC-010, NODE-ROLE-003
**Risk if not met:** M — design flaws discovered late = costly.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** PROCESS
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- NODE-PROC-007 t=node level=L1_PRIMARY track=PROCESS status=TODO -->

### NODE-PROC-008 — SAST/DAST execution process [track=PROC, fields=12]

**Description:** Process to execute SAST/DAST scans per build; triage findings; false-positive review.
**Scope:** All production repos.
**Out of Scope:** Legacy untracked code.
**Source:** CR-D-07.2-001 / CR-D-07.3-001 (orphan F-S1-01 → BPR-D-07.2-001)
**NIST CSF Anchors:** CSF: ID.RA-04, ID.RA-05, PR.PS-01 | PF: —
**Verification Criteria:**
- 100% PRs scanned.
- Triage SLA documented.
- False-positive review quarterly.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.4.2.1, NODE-SYS-012
**Risk if not met:** H — unscanned code = CRA + GDPR gap.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-PROC-008 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-009 — Code review process [track=PROC, fields=12]

**Description:** Two-person code review process; security checklist per review.
**Scope:** All production code changes.
**Out of Scope:** Hotfixes (separate emergency path).
**Source:** CR-D-07.1-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.RA-01, PR.DS-10 | PF: CT.DP-P2
**Verification Criteria:**
- 100% changes reviewed.
- Security checklist used.
- Review SLA documented.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.4.1.1, NODE-ROLE-003
**Risk if not met:** M — unreviewed code = defect risk.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-PROC-009 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-010 — Secret management process [track=PROC, fields=12]

**Description:** Process to manage secrets: vault, rotation, leak detection.
**Scope:** All production secrets.
**Out of Scope:** Local dev secrets.
**Source:** CR-D-07.1-001
**NIST CSF Anchors:** CSF: PR.AA-01, PR.DS-10 | PF: —
**Verification Criteria:**
- 100% secrets in vault.
- Quarterly rotation.
- Leak detection in CI.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.4.1.1, NODE-PROC-009
**Risk if not met:** H — leaked secret = credential compromise.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-PROC-010 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-011 — Processor due-diligence process [track=PROC, fields=12]

**Description:** Process to evaluate processor security + privacy pre-engagement; annual review.
**Scope:** All data processors.
**Out of Scope:** Non-data vendors.
**Source:** CR-D-06.1-001
**NIST CSF Anchors:** CSF: GV.SC-01, GV.SC-02, GV.SC-03 | PF: ID.IM-P2
**Verification Criteria:**
- Questionnaire pre-engagement.
- Annual review (NFR-40).
- Findings tracked.
**Verification Method:** INSPECT
**Owner:** Procurement Lead
**Status:** TODO
**Dependencies:** U.C.5.4.1, NODE-ROLE-009
**Risk if not met:** H — substandard processor = Art. 28 violation.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor

<!-- NODE-PROC-011 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-012 — DPA lifecycle process [track=PROC, fields=12]

**Description:** Process to draft, sign, and renew DPAs; annual review.
**Scope:** All data processors.
**Out of Scope:** Non-data vendors.
**Source:** CR-D-06.3-001
**NIST CSF Anchors:** CSF: GV.OC-03, GV.SC-02, GV.SC-03 | PF: —
**Verification Criteria:**
- 100% active processors with DPA.
- Annual review.
- GDPR Art. 28 clauses present.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** U.C.5.5.1, NODE-ROLE-011
**Risk if not met:** H — missing DPA = Art. 28 violation.
**Affected Stakeholders:** Compliance Manager, CEO, Auditor

<!-- NODE-PROC-012 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-013 — CI/CD security gate process [track=PROC, fields=12]

**Description:** Process to gate merges on critical security findings; emergency override procedure.
**Scope:** All production repos.
**Out of Scope:** Non-prod tooling.
**Source:** CR-D-07.2-001 / CR-D-07.3-001 (orphan F-S1-01 → BPR-D-07.2-001)
**NIST CSF Anchors:** CSF: ID.RA-04, ID.RA-05, PR.PS-01 | PF: —
**Verification Criteria:**
- Critical blocks merge.
- Override signed off.
- Override rate monitored.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.4.2.1, NODE-SYS-012
**Risk if not met:** H — bypassed gate = unscanned code.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-PROC-013 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-014 — Change management process [track=PROC, fields=12]

**Description:** Process to submit, review, approve production changes; emergency change path.
**Scope:** All production changes.
**Out of Scope:** Dev-only changes.
**Source:** CR-D-07.4-001 (orphan F-S1-02 → mapped to BPR-D-07.2-001)
**NIST CSF Anchors:** CSF: GV.PO-02, ID.RA-01, PR.DS-10 | PF: —
**Verification Criteria:**
- 100% changes approved.
- Emergency path documented.
- Approval audit logged.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.4.3.1, NODE-PROC-015
**Risk if not met:** M — unmanaged change = outage + breach.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-PROC-014 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-015 — Patch deployment process [track=PROCESS, fields=17]

**Description:** Process to deploy security patches with critical-first prioritisation; automated where possible.
**Scope:** Production + staging.
**Out of Scope:** Third-party managed services.
**Source:** CR-D-02.2-001
**NIST CSF Anchors:** CSF: GV.OV-02, ID.RA-01, PR.IR-03 | PF: —
**Verification Criteria:**
- Critical median ≤24h.
- Auto-rollback tested.
- Patch audit log.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.4.3.1, NODE-PROC-014
**Risk if not met:** H — unpatched = CRA Art. 14 trigger.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** PROCESS
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- NODE-PROC-015 t=node level=L1_PRIMARY track=PROCESS status=TODO -->

### NODE-PROC-016 — Coordinated Vulnerability Disclosure process [track=PROC, fields=12]

**Description:** Process to receive, triage, and respond to external researcher reports.
**Scope:** External researchers.
**Out of Scope:** Customer support.
**Source:** CR-D-02.3-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.SC-04, RS.CO-03 | PF: —
**Verification Criteria:**
- security.txt present.
- Median first response ≤72h.
- CVE for confirmed issues.
**Verification Method:** INSPECT
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.2.3.1
**Risk if not met:** M — slow disclosure damages trust.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-PROC-016 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-017 — Vulnerability scan process [track=PROC, fields=12]

**Description:** Process to run weekly vulnerability scans; triage findings; track remediation.
**Scope:** Production + staging.
**Out of Scope:** Dev.
**Source:** CR-D-02.1-001
**NIST CSF Anchors:** CSF: GV.OV-02, ID.AM-02, ID.RA-01 | PF: ID.RA-P3, ID.RA-P5
**Verification Criteria:**
- Weekly cadence (NFR-46).
- Findings triaged within SLA.
- Remediation tracked.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.2.1.1, NODE-SYS-009
**Risk if not met:** H — missed vuln = CRA trigger.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-PROC-017 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-018 — Annual awareness training process [track=PROC, fields=12]

**Description:** Process to deliver annual awareness training; completion tracking; re-education.
**Scope:** All employees.
**Out of Scope:** External.
**Source:** CR-D-08.1-001
**NIST CSF Anchors:** CSF: PR.AT-01, PR.AT-02, PR.PS-01 | PF: GV.AT-P1, GV.AT-P2
**Verification Criteria:**
- 100% completion (NFR-36).
- Refreshed annually.
- Quiz required.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** U.C.6.1.1, NODE-ROLE-005
**Risk if not met:** M — untrained staff = phishing risk.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor

<!-- NODE-PROC-018 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-019 — Role-specific training process [track=PROC, fields=12]

**Description:** Process to deliver role-specific security training.
**Scope:** Engineers, ops, DPO, IAM admin.
**Out of Scope:** General awareness.
**Source:** CR-D-08.2-001
**NIST CSF Anchors:** CSF: GV.RR-02, GV.RR-04, PR.AT-02 | PF: GV.AT-P1, GV.AT-P2
**Verification Criteria:**
- Role curricula defined.
- Completion tracked per role.
- Refreshed annually.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** U.C.6.2.1, NODE-ROLE-002, NODE-ROLE-003
**Risk if not met:** M — role gaps = competency risk.
**Affected Stakeholders:** All staff, Compliance Manager, Auditor

<!-- NODE-PROC-019 t=node level=L1_PRIMARY track=PROC status=TODO -->

### NODE-PROC-020 — Annual penetration testing process [track=PROC, fields=12]

**Description:** Process to commission annual external penetration test; remediate findings.
**Scope:** All production systems.
**Out of Scope:** Dev.
**Source:** CR-D-10.3-001
**NIST CSF Anchors:** CSF: DE.AE-02, GV.OV-03, ID.RA-05 | PF: ID.RA-P3, ID.RA-P5
**Verification Criteria:**
- Annual test report.
- Findings remediated within SLA.
- Tester scope documented.
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** U.C.3.6.1, NODE-SYS-009
**Risk if not met:** M — untested controls = drift.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- NODE-PROC-020 t=node level=L1_PRIMARY track=PROC status=TODO -->



### NODE-SYS-001 — SIEM platform [track=TECHNOLOGY, fields=17]

**Description:** Central SIEM ingesting auth, admin, network, and data-access events; correlation engine alerts on indicators.
**Scope:** Production + staging logs; 12-month retention.
**Out of Scope:** Dev environment logs.
**Source:** CR-D-10.2-001 / CR-D-10.1-001 (orphan F-S1-03 → CR-D-10.2-001)
**NIST CSF Anchors:** CSF: DE.CM-01, GV.PO-02, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9
**Verification Criteria:**
- ≥99.9% uptime (NFR-10).
- 100% auth events ingested.
- Correlation rules reviewed quarterly.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** U.C.3.5.1, U.C.2.1.1, NODE-SYS-002/003
**Risk if not met:** H — log loss = GDPR accountability gap.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** TECHNOLOGY
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NODE-SYS-001 t=node level=L1_PRIMARY track=TECHNOLOGY status=TODO -->

### NODE-SYS-002 — Audit log store [track=TECH, fields=12]

**Description:** Immutable WORM storage for audit logs; ≥12 months retention; append-only API.
**Scope:** Production audit events; tamper-evident.
**Out of Scope:** Application logs (separate short-term store).
**Source:** CR-D-10.2-001
**NIST CSF Anchors:** CSF: DE.CM-01, GV.PO-02, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9
**Verification Criteria:**
- WORM API enforced.
- ≥12-month retention (NFR-37).
- Quarterly tamper-evidence test.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** U.C.3.5.1, NODE-SYS-001/003
**Risk if not met:** H — log tampering = GDPR Art. 5(1)(f) breach.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-SYS-002 t=node level=L1_PRIMARY track=TECH status=TODO -->

### NODE-SYS-003 — Log forwarder [track=TECH, fields=12]

**Description:** TLS-protected forwarder shipping events to SIEM + WORM store; bounded retry queue.
**Scope:** Production hosts; agents managed centrally.
**Out of Scope:** Local-only debug logs.
**Source:** CR-D-10.2-001
**NIST CSF Anchors:** CSF: DE.CM-01, PR.DS-01 | PF: CT.DM-P4
**Verification Criteria:**
- TLS 1.2+ enforced.
- Backpressure handled gracefully.
- Agent update cycle ≤30d.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** U.C.3.5.1, NODE-SYS-001/002
**Risk if not met:** M — log gap = forensic blind spot.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-SYS-003 t=node level=L1_PRIMARY track=TECH status=TODO -->

### NODE-SYS-004 — Incident management platform [track=TECHNOLOGY, fields=17]

**Description:** Ticketing + runbook platform used during incidents; integrates SIEM alerts; supports regulatory notification workflow.
**Scope:** All security incidents; pre-drafted ENISA + CNPD templates.
**Out of Scope:** Customer support tickets.
**Source:** CR-D-04.3-001
**NIST CSF Anchors:** CSF: RS.CO-02, RS.MA-01, RS.MA-02 | PF: CM.AW-P7, CM.AW-P8, CM.PO-P1
**Verification Criteria:**
- ≥99.9% uptime.
- Pre-drafted templates current.
- Tabletop quarterly (NFR-17).
**Verification Method:** DEMONSTRATE
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** U.C.2.5.1, NODE-PROC-001, NODE-ROLE-008
**Risk if not met:** H — slow incident handling = CRA Art. 14 + GDPR Art. 33 fines.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** TECHNOLOGY
**Regulatory Reporting:** CNPD ≤72h (GDPR Art. 33) + ENISA ≤24h (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NODE-SYS-004 t=node level=L1_PRIMARY track=TECHNOLOGY status=TODO -->

### NODE-SYS-005 — WAF / fail-safe gateway [track=TECH, fields=12]

**Description:** Web Application Firewall at edge with fail-safe (fail-closed) mode on configuration error.
**Scope:** Public endpoints; rule pack + custom rules.
**Out of Scope:** Internal APIs (different perimeter).
**Source:** CR-D-04.1-001
**NIST CSF Anchors:** CSF: DE.AE-02, DE.CM-01, DE.CM-09 | PF: CM.AW-P7
**Verification Criteria:**
- Fail-safe mode verified quarterly.
- Custom rules reviewed quarterly.
- WAF log integrated with SIEM.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** U.C.2.4.1, U.C.4.4.1
**Risk if not met:** H — WAF bypass = active exploit risk.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-SYS-005 t=node level=L1_PRIMARY track=TECH status=TODO -->

### NODE-SYS-006 — Identity Provider (IdP) [track=TECHNOLOGY, fields=17]

**Description:** Central identity provider handling authentication for staff and customers; integrates MFA + PAM.
**Scope:** All human identities; OIDC / SAML.
**Out of Scope:** Service accounts (separate credentials).
**Source:** CR-D-03.1-001
**NIST CSF Anchors:** CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: —
**Verification Criteria:**
- ≥99.9% uptime.
- MFA enforcement configurable per role.
- Lockout after 5 fails (NFR-02).
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** U.C.3.1.1, NODE-SYS-007, NODE-SYS-011
**Risk if not met:** H — IdP outage = auth blackout + GDPR breach.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** TECHNOLOGY
**Regulatory Reporting:** Internal audit only (no external notification required)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD + ENISA / PT CSIRT (CNCS)

<!-- NODE-SYS-006 t=node level=L1_PRIMARY track=TECHNOLOGY status=TODO -->

### NODE-SYS-007 — Privileged Access Management (PAM) [track=TECH, fields=12]

**Description:** PAM tool for privileged sessions: MFA challenge + session recording + just-in-time elevation.
**Scope:** Privileged roles (admin, ops, IAM).
**Out of Scope:** Standard user sessions.
**Source:** CR-D-03.2-001
**NIST CSF Anchors:** CSF: PR.AA-03, PR.AA-04, PR.AA-05 | PF: —
**Verification Criteria:**
- 100% privileged sessions recorded.
- Just-in-time elevation default.
- Quarterly access review (NFR-25).
**Verification Method:** DEMONSTRATE
**Owner:** CTO
**Status:** TODO
**Dependencies:** U.C.3.1.2, NODE-SYS-006
**Risk if not met:** H — privileged compromise = total takeover.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-SYS-007 t=node level=L1_PRIMARY track=TECH status=TODO -->

### NODE-SYS-008 — Configuration baseline (hardened-default) [track=TECH, fields=12]

**Description:** CIS-aligned hardened baseline applied to production hosts; deviations require security sign-off.
**Scope:** Production hosts; baseline-as-code.
**Out of Scope:** Dev/test environments.
**Source:** CR-D-03.4-001
**NIST CSF Anchors:** CSF: GV.PO-01, GV.SC-03, PR.DS-10 | PF: CT.DP-P4, CT.PO-P4
**Verification Criteria:**
- ≥95% CIS compliance (NFR-37).
- Drift detection in place.
- Baseline version controlled.
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** U.C.3.3.1
**Risk if not met:** M — misconfig = most common breach vector.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- NODE-SYS-008 t=node level=L1_PRIMARY track=TECH status=TODO -->

### NODE-SYS-009 — Penetration testing platform [track=TECH, fields=12]

**Description:** External pentest engagement + internal testing toolkit (Burp, Nuclei, custom scripts).
**Scope:** Annual external + ad-hoc internal.
**Out of Scope:** Production mutation testing (separate).
**Source:** CR-D-10.3-001
**NIST CSF Anchors:** CSF: DE.AE-02, GV.OV-03, ID.RA-05 | PF: ID.RA-P3, ID.RA-P5
**Verification Criteria:**
- Annual pentest report published.
- Findings tracked to remediation.
- Tester scope documented.
**Verification Method:** INSPECT
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** U.C.3.6.1, U.C.2.1.1
**Risk if not met:** M — untested controls = undetected drift.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- NODE-SYS-009 t=node level=L1_PRIMARY track=TECH status=TODO -->

### NODE-SYS-010 — Encryption-at-rest (data store) [track=TECHNOLOGY, fields=17]

**Description:** AES-256 encryption-at-rest for primary database + object storage; key management via KMS.
**Scope:** Production data stores; managed keys.
**Out of Scope:** Ephemeral dev databases.
**Source:** CR-D-01.1-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1
**Verification Criteria:**
- 100% prod stores encrypted (NFR-03).
- Key rotation annual.
- Algorithm = AES-256-GCM.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** U.C.1.1.1, NODE-SYS-016
**Risk if not met:** H — unencrypted store = GDPR Art. 32 breach.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** TECHNOLOGY
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NODE-SYS-010 t=node level=L1_PRIMARY track=TECHNOLOGY status=TODO -->

### NODE-SYS-011 — TLS terminator (data in transit) [track=TECH, fields=12]

**Description:** Edge TLS terminator with TLS 1.2+ (preferred 1.3); HSTS enabled; cipher suite policy.
**Scope:** All public endpoints.
**Out of Scope:** Internal mTLS (separate).
**Source:** CR-D-01.2-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02, PR.DS-10 | PF: CT.DM-P1, CT.DM-P3
**Verification Criteria:**
- TLS 1.2+ enforced (NFR-04).
- HSTS enabled.
- Cipher suite policy applied.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** U.C.3.1.1
**Risk if not met:** H — weak TLS = data-in-transit breach.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor

<!-- NODE-SYS-011 t=node level=L1_PRIMARY track=TECH status=TODO -->

### NODE-SYS-012 — CI/CD pipeline (SAST/DAST) [track=TECHNOLOGY, fields=17]

**Description:** CI/CD pipeline integrating SAST, SCA, secret-detection, container scan, DAST.
**Scope:** All production repos; security gates on critical findings.
**Out of Scope:** Throwaway experiments.
**Source:** CR-D-07.2-001 / CR-D-07.3-001 (orphan F-S1-01 → BPR-D-07.2-001)
**NIST CSF Anchors:** CSF: ID.RA-04, ID.RA-05, PR.PS-01 | PF: —
**Verification Criteria:**
- 100% PRs scanned (UC-4.2.1).
- Critical blocks merge.
- Pipeline uptime ≥99.5% (NFR-11).
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.4.2.1, NODE-PROC-008, NODE-PROC-013
**Risk if not met:** H — unscanned code = CRA Art. 13 + GDPR Art. 25 gap.
**Affected Stakeholders:** Lead Developer, CTO, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** TECHNOLOGY
**Regulatory Reporting:** ENISA ≤24h if actively-exploited vulnerability (CRA Art. 14)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** ENISA / PT CSIRT (CNCS)

<!-- NODE-SYS-012 t=node level=L1_PRIMARY track=TECHNOLOGY status=TODO -->

### NODE-SYS-013 — SBOM generator [track=TECH, fields=12]

**Description:** Automated SBOM generation per release; CycloneDX/SPDX output; published to customer portal.
**Scope:** All production releases.
**Out of Scope:** Internal tooling releases.
**Source:** CR-D-06.2-001
**NIST CSF Anchors:** CSF: GV.SC-02, GV.SC-03, ID.RA-01 | PF: —
**Verification Criteria:**
- SBOM per release (NFR-45).
- Format validated.
- Customer portal tested.
**Verification Method:** TEST
**Owner:** Lead Developer
**Status:** TODO
**Dependencies:** U.C.5.6.1, NODE-SYS-012
**Risk if not met:** M — missing SBOM = CRA Art. 13 transparency gap.
**Affected Stakeholders:** Lead Developer, CTO, Auditor

<!-- NODE-SYS-013 t=node level=L1_PRIMARY track=TECH status=TODO -->

### NODE-SYS-014 — Records-of-Processing store [track=TECH, fields=12]

**Description:** Repository holding RoPA, DPIAs, processing records; access-controlled.
**Scope:** All RoPA + DPIA artefacts.
**Out of Scope:** Customer-facing exports (separate).
**Source:** CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P8
**Verification Criteria:**
- RoPA updated ≤7d (NFR-35).
- Access controlled by DPO.
- Backup included.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** U.C.5.3.1, U.C.1.5.1, NODE-PROC-006
**Risk if not met:** M — outdated RoPA = GDPR Art. 30 violation.
**Affected Stakeholders:** Customer, DPO, Auditor

<!-- NODE-SYS-014 t=node level=L1_PRIMARY track=TECH status=TODO -->

### NODE-SYS-015 — Backup & restore service [track=TECH, fields=12]

**Description:** Encrypted backup service with retention ≥90 days; restore tested quarterly.
**Scope:** Production data stores.
**Out of Scope:** Long-term archival.
**Source:** CR-D-04.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-10, PR.IR-03 | PF: —
**Verification Criteria:**
- ≥90-day retention (NFR-19).
- Restore test quarterly.
- Backup integrity verified weekly (NFR-07).
**Verification Method:** TEST
**Owner:** Operations Lead
**Status:** TODO
**Dependencies:** U.C.2.6.1, U.C.1.2.1, NODE-PROC-003
**Risk if not met:** H — failed restore = data loss.
**Affected Stakeholders:** Operations Lead, Lead Developer, Auditor

<!-- NODE-SYS-015 t=node level=L1_PRIMARY track=TECH status=TODO -->

### NODE-SYS-016 — Integrity verification (HMAC) [track=TECHNOLOGY, fields=17]

**Description:** HMAC/SHA-256 integrity verification on critical records; tamper-detection logs.
**Scope:** Production critical records (customer, financial).
**Out of Scope:** Cache / derived data.
**Source:** CR-D-01.4-001
**NIST CSF Anchors:** CSF: PR.DS-01, PR.DS-02, PR.DS-10 | PF: CT.DM-P1, CT.DM-P3
**Verification Criteria:**
- 100% critical records covered (NFR-06).
- Tamper-detection logs in SIEM.
- Algorithm = HMAC-SHA-256.
**Verification Method:** TEST
**Owner:** CTO
**Status:** TODO
**Dependencies:** U.C.1.1.2, NODE-SYS-001
**Risk if not met:** H — undetected tampering = integrity breach.
**Affected Stakeholders:** Customer, CTO, DPO, Lead Developer, Auditor
**Implementation Status:** PARTIAL (What's missing: operational evidence verification & automated review cadence)
**Node Track:** TECHNOLOGY
**Regulatory Reporting:** CNPD ≤72h if breach of personal data (GDPR Art. 33)
**External Auditor:** AWS SOC 2 (managed hosting attestation) / ISO 27001
**Supervisory Body:** CNPD (Comissão Nacional de Proteção de Dados)

<!-- NODE-SYS-016 t=node level=L1_PRIMARY track=TECHNOLOGY status=TODO -->

### NODE-SYS-017 — Breach register [track=TECH, fields=12]

**Description:** Central breach register: detection timestamp, classification, notification status, owner.
**Scope:** All confirmed security incidents.
**Out of Scope:** Suspected-only incidents.
**Source:** CR-D-09.4-001
**NIST CSF Anchors:** CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P8
**Verification Criteria:**
- Entry ≤24h post-detection (NFR-43).
- Status updated through lifecycle.
- DPO review monthly.
**Verification Method:** INSPECT
**Owner:** DPO
**Status:** TODO
**Dependencies:** U.C.2.5.1, U.C.5.3.1, NODE-SYS-014
**Risk if not met:** M — missed entry = GDPR accountability gap.
**Affected Stakeholders:** Customer, DPO, Auditor

<!-- NODE-SYS-017 t=node level=L1_PRIMARY track=TECH status=TODO -->




**End of Architectural Nodes (Phase 3 RICH, ADJUSTED_FIELDS, Fase de Especificação 4)**
