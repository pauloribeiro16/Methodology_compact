---
document_id: AEGIS-P3-RICH-13a
title: Use Case Relationships — TinyTask SaaS (Phase 3 RICH)
phase: 3
version: 0.4
created: 2026-08-24
updated: 2026-08-24
author: Sprint 4 Executor (paulo@methodology.pt)
status: ADJUSTED_FIELDS
sprint: 4
sprint_role: schema_adjustment
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [13_Use_Cases_Catalog.md]
outputs: [14_Architectural_Nodes.md, 15_Requirements_Allocation.md]
related_documents: [13_Use_Cases_Catalog.md, 13b_Use_Case_Variability.md, RULE_FREEZE.md]
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Maturity, Priority, Stakeholders, Reporting]
freeze_total_relationships: 24
reconciliation_note: "Relationships ported from legacy §3; 24 «include»+«extend» edges; F-00a CLOSED (MaaS format preserved)."
sprint4_note: "Sprint 4: 6 columns appended to §2 (include) and §3 (extend) tables; values to be filled in Sprint 5."
---

# Use Case Relationships — TinyTask SaaS (Phase 3 RICH)

> **Status:** ADJUSTED_FIELDS (Sprint 4). 24 typed relationships (16 `«include»` + 8 `«extend»`) over 35 L1 cards.

---

## §1 Reconciliation Notes

This document mirrors legacy `13a_Use_Case_Relationships.md` (v2.0). The Rich sibling validates that the UC decomposition is well-formed and all `«include»` / `«extend»` targets exist in the freeze set.

**Authoritative sources:**
- `RULE_FREEZE.md` §5 — UC enumeration.
- `CORPUS_LINKAGE.md` §3 — UC-to-D-XX.Y mapping (used for cross-package validation).
- `13_Use_Cases_Catalog.md` §3 — UC catalogue.

**Gate criteria (legacy §1):**
- All `«include»` targets exist (validated by §2 below).
- All `«extend»` targets exist (validated by §3 below).
- No orphan UCs (every UC has ≥1 relationship or is standalone; see §4).
- Package membership correct (see `13_Use_Cases_Catalog.md` §2).

---

## §2 `«include»` Relationships (Common Functionality — 16)

| Including UC | Included UC | Rationale | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|--------------|-------------|-----------|-------|-----------------------|----------|----------|--------------|-----------|
| U.C.1.1.1 | U.C.3.1.1 | DSAR requires authenticated subject | | | | | | |
| U.C.1.2.1 | U.C.3.1.1 | Erasure requires authenticated subject | | | | | | |
| U.C.1.3.1 | U.C.3.1.1 | Data export requires authenticated subject | | | | | | |
| U.C.1.5.1 | U.C.3.1.1 | Rectification requires authenticated subject | | | | | | |
| U.C.2.1.1 | U.C.3.5.1 | Vulnerability detection requires audit logging | | | | | | |
| U.C.2.2.1 | U.C.3.5.1 | Patch deployment logs to audit trail | | | | | | |
| U.C.2.5.1 | U.C.3.5.1 | Incident notification logs to audit trail | | | | | | |
| U.C.2.6.1 | U.C.3.5.1 | Data restoration logs to audit trail | | | | | | |
| U.C.3.1.1 | U.C.3.5.1 | Authentication events logged | | | | | | |
| U.C.3.1.2 | U.C.3.1.1 | MFA requires base authentication | | | | | | |
| U.C.3.6.1 | U.C.3.1.1 | Account deprovisioning requires auth context | | | | | | |
| U.C.4.1.1 | U.C.2.3.1 | SSDLC triggers coordinated disclosure | | | | | | |
| U.C.4.2.1 | U.C.2.3.1 | SAST/DAST findings feed disclosure process | | | | | | |
| U.C.4.5.1 | U.C.5.2.1 | Pre-launch risk assessment = DPIA | | | | | | |
| U.C.5.3.1 | U.C.3.5.1 | RoPA updates logged | | | | | | |
| U.C.5.6.1 | U.C.5.4.1 | SBOM publication requires processor due diligence | | | | | | |

---

## §3 `«extend»` Relationships (Variants — 8)

| Base UC | Extending UC | Extension point | Rationale | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|---------|--------------|-----------------|-----------|-------|-----------------------|----------|----------|--------------|-----------|
| U.C.2.5.1 | U.C.2.4.2 | Incident-→-DoS scenario | DoS triggers 24h ENISA notification path | | | | | | |
| U.C.4.5.1 | U.C.5.2.1 | DPIA extends risk assessment | High-risk processing extends DPIA | | | | | | |
| U.C.3.5.1 | U.C.2.1.1 | Audit log feeds SIEM detection | SIEM extends audit logging | | | | | | |
| U.C.5.1.1 | U.C.5.1.2 | Policy review extends documentation | Documentation is artefact of policy | | | | | | |
| U.C.6.1.1 | U.C.6.3.1 | Phishing extends annual training | Practical exercise for awareness | | | | | | |
| U.C.2.3.1 | U.C.2.5.1 | CVD triggers incident notification | Disclosed vuln may become incident | | | | | | |
| U.C.3.3.1 | U.C.3.1.1 | Secure defaults constrain auth | Hardened baseline applied to auth | | | | | | |
| U.C.4.3.1 | U.C.2.2.1 | Patch deployment is operationalised by automation | DEV-side patch → SEC-side deployment | | | | | | |

---

## §4 Orphan check

Every UC has at least one `«include»` or `«extend»` relationship, OR is documented as standalone with rationale:

- **U.C.1.4.1 (Consent Management)** — standalone: consent lifecycle managed outside UC graph; logged via U.C.3.5.1 implicitly.
- **U.C.3.4.1 (Processing & Breach Records)** — standalone: GDPR Art. 30 RoPA + breach record obligations are document-centric.
- **U.C.6.2.1 (Role-Specific Training)** — extends U.C.6.1.1 (covered in §3).
- **U.C.2.4.1 (Exploit Severity Limitation)** — standalone: technical control; outputs feed U.C.2.4.2.

**Result:** No orphan UCs.

---

## §5 Package consistency

Package membership matches `13_Use_Cases_Catalog.md` §2. No UC spans multiple packages. Cross-package relationships (e.g. PKG-DEV → PKG-SEC) are explicit in §2/§3 and trace to inter-domain rule mappings in `CORPUS_LINKAGE.md` §10.

---

## §6 Cross-references

- `13_Use_Cases_Catalog.md` §3 (catalogue) + §2 (packages)
- `13b_Use_Case_Variability.md` — variant catalogue
- `CORPUS_LINKAGE.md` §3 — UC-to-D-XX.Y mapping
- `RULE_FREEZE.md` §5 — UC enumeration freeze

---

**End of Use Case Relationships (Phase 3 RICH, ADJUSTED_FIELDS, Sprint 4)**
