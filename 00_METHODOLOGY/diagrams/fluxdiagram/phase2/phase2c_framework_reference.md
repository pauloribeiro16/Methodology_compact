---
document_id: AEGIS-DIAG-P2C-REFERENCE
title: "Phase 2C — Framework Reference & Traceability"
phase: 2C
version: 1.0
created: 2026-06-16
status: CREATED
parent_diagram: phase2c_goals_and_rules.md
source: Cross-case analysis (Doc 10 + Doc 11 from all 3 cases)
---

# Phase 2C — Framework Reference & Traceability

**Version:** 1.0 — 2026-06-16
**Companion to:** [`phase2c_goals_and_rules.md`](phase2c_goals_and_rules.md) (flow diagrams)
**Sources:** Doc 10 + Doc 11 from Case 01, Case 02, Case 03

---

## Overview

This file is the **reference companion** to the Phase 2C detailed flow diagrams. It contains:

1. **Framework Mapping Tables** — per-rule cross-references to ISO 27001, NIST CSF, NIST 800-53, OWASP ASVS, NIST SSDF
2. **Traceability Chain Verification** — how to verify the full Clause → Obligation → Goal → Rule chain
3. **Priority Threshold Reference** — NI-to-priority mapping with cross-case inconsistency
4. **Implementation Mode Reference** — NATIVE / INHERITED / HYBRID definitions and cross-case distribution

---

## 1. Framework Mapping Tables

### ISO 27001:2022

| Sub-Domain | ISO 27001 Control | Rule(s) Supported |
|------------|-------------------|-------------------|
| D-01.1 (Data at Rest) | A.8.24 (Cryptography) | BPR-D-01.1-001 |
| D-01.2 (Data in Transit) | A.8.24 (Cryptography) | BPR-D-01.2-001 |
| D-02.1 (Vulnerability Mgmt) | A.8.8 (Technical vulnerabilities) | BPR-D-02.1-001 |
| D-03.1 (Access Control) | A.9.2 (User access management) | BPR-D-03.1-001 |
| D-03.2 (Authentication) | A.9.4 (System access control) | BPR-D-03.2-001 |
| D-04.1 (Incident Response) | A.5.24 (Incident management) | BPR-D-04.1-001 |
| D-04.3 (Notification) | A.5.25 (Incident assessment) | BPR-D-04.3-001 |
| D-05.1 (Minimisation) | A.8.10 (Information deletion) | BPR-D-05.1-001 |
| D-05.3 (Erasure) | A.8.10 (Information deletion) | BPR-D-05.3-001 |
| D-06.1 (Supplier Security) | A.5.19 (Supplier relationships) | BPR-D-06.1-001 |
| D-06.2 (SBOM) | A.8.25 (Secure development lifecycle) | BPR-D-06.2-001 |
| D-07.1 (Secure Design) | A.8.25 (Secure development lifecycle) | BPR-D-07.1-001 |
| D-07.2 (Secure Coding) | A.8.28 (Secure coding) | BPR-D-07.2-001 |
| D-08.1 (Training) | A.6.3 (Information security awareness) | BPR-D-08.1-001 |
| D-09.1 (Policies) | A.5.1 (Policies for information security) | BPR-D-09.1-001 |
| D-09.2 (Risk Assessment) | A.5.7 (Threat intelligence) | BPR-D-09.2-001 |
| D-10.1 (Logging) | A.8.15 (Logging) | BPR-D-10.1-001 |
| D-10.2 (Audit Trail) | A.8.16 (Monitoring activities) | BPR-D-10.2-001 |
| D-10.3 (Compliance Testing) | A.5.36 (Compliance with policies) | BPR-D-10.3-001 |

### NIST CSF 2.0

| Sub-Domain | NIST CSF Category | Rule(s) Supported |
|------------|-------------------|-------------------|
| D-01.1 (Data at Rest) | PR.DS-1 (Data-at-rest protected) | BPR-D-01.1-001 |
| D-01.2 (Data in Transit) | PR.DS-2 (Data-in-transit protected) | BPR-D-01.2-001 |
| D-02.1 (Vulnerability Mgmt) | ID.RA-1 (Vulnerabilities identified) | BPR-D-02.1-001 |
| D-03.1 (Access Control) | PR.AA-1 (Identities managed) | BPR-D-03.1-001 |
| D-04.1 (Incident Response) | RS.MA-1 (Incidents triaged) | BPR-D-04.1-001 |
| D-04.3 (Notification) | RS.CO-2 (Incidents reported externally) | BPR-D-04.3-001 |
| D-05.1 (Minimisation) | PR.DS-1 (Data minimization) | BPR-D-05.1-001 |
| D-06.1 (Supplier Security) | GV.SC-1 (Supply chain risk managed) | BPR-D-06.1-001 |
| D-07.1 (Secure Design) | PR.PT-1 (Audit log records generated) | BPR-D-07.1-001 |
| D-08.1 (Training) | PR.AT-1 (All users aware of risks) | BPR-D-08.1-001 |
| D-09.1 (Policies) | GV.PO-1 (Organizational policy established) | BPR-D-09.1-001 |
| D-10.1 (Logging) | DE.CM-1 (Network monitored) | BPR-D-10.1-001 |

### NIST 800-53 Rev 5

| Sub-Domain | NIST 800-53 Control | Rule(s) Supported |
|------------|---------------------|-------------------|
| D-01.1 (Data at Rest) | SC-28 (Protection of Information at Rest) | BPR-D-01.1-001 |
| D-02.1 (Vulnerability Mgmt) | RA-5 (Vulnerability Monitoring and Scanning) | BPR-D-02.1-001 |
| D-03.1 (Access Control) | AC-2 (Account Management) | BPR-D-03.1-001 |
| D-04.1 (Incident Response) | IR-4 (Incident Handling) | BPR-D-04.1-001 |
| D-09.1 (Policies) | PM-9 (Risk Management Strategy) | BPR-D-09.1-001 |
| D-10.2 (Audit Trail) | AU-6 (Audit Record Review, Analysis, and Reporting) | BPR-D-10.2-001 |

### OWASP ASVS v4.0

| Sub-Domain | OWASP ASVS Section | Rule(s) Supported |
|------------|---------------------|-------------------|
| D-02.1 (Vulnerability Mgmt) | V1 (Architecture) | BPR-D-02.1-001 |
| D-03.1 (Access Control) | V4 (Access Control) | BPR-D-03.1-001 |
| D-03.2 (Authentication) | V2 (Authentication) | BPR-D-03.2-001 |
| D-05.1 (Minimisation) | V5 (Validation, Sanitization, Encoding) | BPR-D-05.1-001 |
| D-07.2 (Secure Coding) | V14 (Code Architecture) | BPR-D-07.2-001 |

### NIST SSDF v1.1

| Sub-Domain | NIST SSDF Practice | Rule(s) Supported |
|------------|---------------------|-------------------|
| D-06.2 (SBOM) | PO.5.1 (Identify and confirm critical software) | BPR-D-06.2-001 |
| D-07.1 (Secure Design) | PO.5.1 (Design software to meet security requirements) | BPR-D-07.1-001 |
| D-07.2 (Secure Coding) | PW.4 (Protect All Forms of Code from Unauthorised Access) | BPR-D-07.2-001 |
| D-07.3 (Security Testing) | PW.8 (Confirm That Code Does Not Contain Vulnerabilities) | BPR-D-07.3-001 |

---

## 2. Traceability Chain Verification

### Full Chain

```
RegulatoryClause (Doc 06)
    → RegulatoryObligation (Doc 08)
        → PrivacyGoal / SecurityGoal (Doc 10)
            → ComplianceRule / BestPracticeRule (Doc 11)
```

### Verification Method

| Step | Forward Check | Reverse Check |
|------|---------------|---------------|
| Clause → Obligation | For each clause in Doc 06, find ≥1 obligation in Doc 08 | For each obligation in Doc 08, trace back to ≥1 clause |
| Obligation → Goal | For each obligation in Doc 08, find ≥1 goal in Doc 10 | For each goal in Doc 10, trace back to ≥1 obligation |
| Goal → Rule | For each goal in Doc 10, find ≥1 rule in Doc 11 | For each rule in Doc 11, trace back to ≥1 goal |
| Clause → Rule (full) | For each clause in Doc 06, trace forward to ≥1 rule | For each rule in Doc 11, trace back to ≥1 clause |

### Cross-Case Traceability

| Case | Clauses | Obligations | Goals | Rules | Chain Complete? |
|------|---------|-------------|-------|-------|----------------|
| Case 01 | 54 | 23 | 30 | 46 | Yes |
| Case 02 | 112 | 38 | 38 | 63 | Yes |
| Case 03 | 150 | 38 | 33 | 63 | Yes |

---

## 3. Priority Threshold Reference

### NI-to-Priority Mapping

| NI Range | Priority | Treatment | Typical Source |
|----------|----------|-----------|----------------|
| NI ≥ 2.8 | CRITICAL | Mandatory, immediate implementation | "Shall" + high-impact clauses |
| NI 2.5–2.8 | HIGH | Required, next planning cycle | "Shall" or "Should" + medium-impact |
| NI 2.0–2.5 | MEDIUM | Recommended, schedule for review | "Should" clauses |
| NI < 2.0 | LOW | Advisory, monitor for changes | "May" clauses |

### Cross-Case Inconsistency

| Case | P1 Threshold | P2 Threshold | P3 Threshold | Notes |
|------|-------------|--------------|--------------|-------|
| Case 01 | NI >= 2.5 | NI >= 2.0 | NI < 2.0 | Standard thresholds |
| Case 02 | NI >= 2.8 | NI >= 2.5 | NI >= 2.0 | Stricter (financial sector) |
| Case 03 | NI >= 2.5 | NI >= 2.0 | NI < 2.0 | Standard thresholds |

**Not resolved.** The methodology does not prescribe one threshold set. Case 02's stricter thresholds reflect the higher regulatory burden for financial entities (DORA).

---

## 4. Implementation Mode Reference

### Definitions

| Mode | Definition | When Used |
|------|-----------|-----------|
| **AUTOMATED** | Rule enforced entirely by technical controls (no manual intervention) | Encryption, access control, logging, SBOM generation |
| **MANUAL** | Rule enforced entirely by human processes (no automation) | Policy documentation, training, supplier questionnaires |
| **HYBRID** | Rule enforced by a combination of technical and human controls | Incident response (automated detection + human triage), risk assessment (automated scanning + human review) |

### Cross-Case Distribution

| Case | AUTOMATED | MANUAL | HYBRID | Total |
|------|-----------|--------|--------|-------|
| Case 01 | 22 (48%) | 12 (26%) | 12 (26%) | 46 |
| Case 02 | 30 (48%) | 18 (29%) | 15 (24%) | 63 |
| Case 03 | 32 (51%) | 16 (25%) | 15 (24%) | 63 |

---

## 5. Summary: How to Use This File

| If you need to... | Read this section |
|---|---|
| Map a rule to an ISO 27001 control | §1 — Framework Mapping Tables |
| Verify the full traceability chain | §2 — Traceability Chain Verification |
| Understand priority thresholds | §3 — Priority Threshold Reference |
| Assign implementation modes | §4 — Implementation Mode Reference |

---

**See also:**
- [`phase2c_goals_and_rules.md`](phase2c_goals_and_rules.md) — Flow diagrams (companion)
- [`../phase2_elaboration_secure_design.md`](../phase2_elaboration_secure_design.md) — Phase 2 overview (parent)
- [`phase2a_obligation_derivation.md`](phase2a_obligation_derivation.md) — Phase 2A (predecessor)
- [`phase2b_tension_reference.md`](phase2b_tension_reference.md) — Phase 2B reference (tension catalog)
- [`../../../TEMPLATES/10_Privacy_Security_Goals.md`](../../../TEMPLATES/10_Privacy_Security_Goals.md) — Doc 10 template
- [`../../../TEMPLATES/11_Rules_Catalog.md`](../../../TEMPLATES/11_Rules_Catalog.md) — Doc 11 template
