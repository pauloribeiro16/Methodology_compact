---
document_id: AEGIS-DIAG-P3B-REFERENCE
title: "Phase 3B — Requirements & Allocation Reference: Nodes, NFRs, FRs, Allocation & Traceability"
phase: 3B
version: 1.0
created: 2026-06-17
status: CREATED
parent_diagram: phase3b_requirements.md
source: Cross-case analysis (Doc 14, 15, 16, 23, 24 from all 3 cases)
---

# Phase 3B — Requirements & Allocation Reference

**Version:** 1.0 — 2026-06-17
**Companion to:** [`phase3b_requirements.md`](phase3b_requirements.md) (flow diagrams + LLM spec tables)
**Sources:** Doc 14 + Doc 15 + Doc 16 + Doc 23 + Doc 24 from Case 01, Case 02, Case 03

---

## Overview

This file is the **reference companion** to the Phase 3B detailed flow diagrams. It contains the analytical frameworks and catalogs that LLM-E (node decomposition, NFR/FR derivation) and the deterministic allocation/gate steps rely on:

1. **Node Decomposition Patterns Catalog** — how security UCs map to architectural nodes, by node type and decomposition level
2. **NFR Quality Attribute Taxonomy** — confidentiality / integrity / availability / accountability / privacy with measurement templates and tier-based targets
3. **FR Derivation Patterns** — how UC + NFR + Rule combine into testable FRs
4. **Allocation Type Decision Matrix** — when to use DIRECT / SHARED / INHERITED
5. **Verification Method Selection Guide** — TEST / INSPECT / DEMONSTRATE / ANALYZE
6. **8-Level Traceability Verification Rules** — forward and reverse checks for full-chain integrity
7. **Cross-Case Node & Requirement Catalog** — how node, FR, NFR, allocation, and gate counts scale across complexity tiers
8. **Node Hierarchy Guidelines** — parent-child rules, cross-track relationships, orphan prevention, multi-parent rules, hierarchy-validation checks, class-model cross-references
9. **Verification Methodology Detail** — evidence catalog per method, frequency options, ownership, audit-trail artifacts, cross-case verification distribution
10. **Acceptance Criteria Derivation Patterns** — derivation formula, 10-pattern catalog, worked examples per tier, anti-patterns, quality checklist

---

## 1. Node Decomposition Patterns Catalog

How security UCs map to architectural nodes, organized by node type:

### 1.1 Process Node Patterns

| Pattern | Triggered by sub-domain | Typical UCs | Example node |
|---------|------------------------|-------------|--------------|
| Incident Response Process | D-04.1, D-04.2 | Incident detected, incident responded to | NODE-PROC-001 |
| Vulnerability Management Process | D-02.1, D-02.2, D-02.3 | Vuln scan, patch deployed | NODE-PROC-002 |
| DSAR Handling Process | D-05.3, D-05.4 | Access request, erasure request | NODE-PROC-005 |
| Secure SDLC Process | D-07.1, D-07.2, D-07.3 | Code scan, security gate | NODE-PROC-011 |
| Policy Management Process | D-09.1 | Policy review | NODE-PROC-015 |
| Risk Assessment Process | D-09.2, D-09.3 | Risk assessment, DPIA | NODE-PROC-016 |

### 1.2 IT System Node Patterns

| Pattern | Triggered by sub-domain | Typical UCs | Example node |
|---------|------------------------|-------------|--------------|
| SIEM Platform | D-10.1, D-04.1 | Monitoring, incident detection | NODE-SYS-001 |
| Identity Provider | D-03.1, D-03.2 | Authentication, registration | NODE-SYS-005 |
| Encryption Service | D-01.1, D-01.2 | Data protection | NODE-SYS-004 |
| Vulnerability Scanner | D-02.1 | Vuln scan | NODE-SYS-002 |
| CI/CD Platform | D-07.3 | Security gate, deployment | NODE-SYS-012 |
| GRC Platform | D-09.1, D-09.2 | Policy, risk, compliance | NODE-SYS-015 |

### 1.3 Human Role Node Patterns

| Pattern | Triggered by sub-domain | Required competencies | Example node |
|---------|------------------------|-----------------------|--------------|
| CISO/CISO role | D-04.1, D-09.1 | Security leadership, risk management | NODE-ROLE-001 |
| Security Analyst | D-04.1, D-10.1 | SIEM, incident response | NODE-ROLE-002 |
| DPO | D-05.3, D-05.4 | GDPR, privacy law | NODE-ROLE-007 |
| Security Engineer | D-07.2 | SAST/DAST, secure coding | NODE-ROLE-004 |
| Compliance Lead | D-09.1, D-10.3 | Regulatory compliance | NODE-ROLE-008 |

### 1.4 Decomposition Level Guidelines

| Level | Scope | When to use | Example |
|-------|-------|-------------|---------|
| L1 | Enterprise-wide | Core security capabilities (1 per domain) | SIEM Platform, Identity Provider |
| L2 | Process/System level | Specific tools or procedures | Vulnerability Scanner, DSAR Process |
| L3 | Detailed implementation | Sub-components or specialized roles | MFA Service, Security Analyst |

---

## 2. NFR Quality Attribute Taxonomy

A taxonomy of NFR quality attributes with measurement criteria templates:

### 2.1 Confidentiality (NFR-01 to NFR-07)

| Attribute | Regulatory source | Measurement template | Target (LOW tier) | Target (MAX tier) |
|-----------|------------------|---------------------|-------------------|-------------------|
| Data-at-rest encryption | GDPR Art.32, CRA Annex I | % of personal data encrypted | 100% AES-128 | 100% AES-256 |
| Data-in-transit encryption | GDPR Art.32 | % of external comms encrypted | 100% TLS 1.2 | 100% TLS 1.3 |
| Access control | GDPR Art.32 | % of access authenticated | 100% | 100% + MFA |
| Credential protection | CRA Annex I.3 | Credential leaks per year | 0 | 0 |

### 2.2 Integrity (NFR-08 to NFR-14)

| Attribute | Regulatory source | Measurement template | Target (LOW) | Target (MAX) |
|-----------|------------------|---------------------|--------------|--------------|
| Data accuracy | GDPR Art.5(1)(d) | % of inputs validated | 95% | 100% |
| Write authorization | GDPR Art.32 | % of writes logged | 100% | 100% + real-time |

### 2.3 Availability (NFR-15 to NFR-21)

| Attribute | Regulatory source | Measurement template | Target (LOW) | Target (MAX) |
|-----------|------------------|---------------------|--------------|--------------|
| Service uptime | CRA, DORA | % uptime per year | 99.5% | 99.99% |
| Incident response time | GDPR Art.33, DORA | Mean time to detect | 4 hours | 15 minutes |
| Recovery time | DORA Art.11 | RTO | 24 hours | 2 hours |

### 2.4 Accountability (NFR-22 to NFR-28)

| Attribute | Regulatory source | Measurement template | Target (LOW) | Target (MAX) |
|-----------|------------------|---------------------|--------------|--------------|
| Audit logging | GDPR Art.30, DORA Art.10 | % of admin actions logged | 100% | 100% + immutable |
| Log retention | CRA, DORA | Months retained | 12 | 60+ |

### 2.5 Privacy (NFR-29 to NFR-35)

| Attribute | Regulatory source | Measurement template | Target (LOW) | Target (MAX) |
|-----------|------------------|---------------------|--------------|--------------|
| Data minimization | GDPR Art.5(1)(c) | % of fields with business justification | 90% | 100% |
| Consent management | GDPR Art.7 | % of processing with valid consent | 95% | 100% |
| Erasure capability | GDPR Art.17 | Erasure requests fulfilled within SLA | 30 days | 7 days |

---

## 3. FR Derivation Patterns

How UC + NFR + Rule combine into FRs:

| Pattern | UC source | NFR source | Rule source | Resulting FR pattern |
|---------|-----------|------------|-------------|---------------------|
| Authentication FR | UC: User Authenticates | NFR: Auth within 5s | Rule: MFA required | "System shall authenticate users with MFA within 5 seconds" |
| Encryption FR | UC: Data Stored | NFR: AES-256 at rest | Rule: GDPR Art.32 | "System shall encrypt all personal data at rest using AES-256" |
| Notification FR | UC: Incident Detected | NFR: Notify within 24h | Rule: CRA Art.14 | "System shall notify authorities within 24 hours of breach awareness" |
| Logging FR | UC: Access Modified | NFR: All actions logged | Rule: GDPR Art.30 | "System shall log all access modifications with timestamp and actor" |
| Vulnerability FR | UC: Vuln Scan | NFR: Weekly scan | Rule: CRA Annex I | "System shall execute vulnerability scans weekly and report CVSS scores" |

---

## 4. Allocation Type Decision Matrix

When to use DIRECT vs SHARED vs INHERITED:

| Scenario | Allocation type | Rationale | Example |
|----------|----------------|-----------|---------|
| Rule maps to exactly 1 node | DIRECT | Single implementation point | Encryption rule → Encryption Service |
| Rule spans process + system | SHARED | Requires both tool and procedure | Vuln rule → Scanner + Process |
| Rule satisfied by cloud provider | INHERITED | Company doesn't implement directly | Encryption rule → inherited from AWS |
| Rule satisfied by parent node | INHERITED | Child inherits parent's control | Access rule → inherited from IdP |

---

## 5. Verification Method Selection Guide

| Requirement type | Method | When | Evidence |
|-----------------|--------|------|----------|
| Configuration check | TEST | Automated, repeatable | Test output, config screenshot |
| Process review | INSPECT | Manual, documentation-based | Policy doc, procedure manual |
| Capability demo | DEMONSTRATE | Live observation | Demo recording, observation log |
| Architecture analysis | ANALYZE | Design-level verification | Architecture review, threat model |

---

## 6. 8-Level Traceability Verification Rules

The full chain and its verification rules:

| Level | Entity | ID Pattern | Forward check | Reverse check |
|-------|--------|------------|---------------|---------------|
| 1 | Regulation | GDPR, CRA, ... | Each reg has ≥1 clause | Each clause traces to ≥1 reg |
| 2 | Clause | GDPR-C04 | Each clause has ≥1 rule | Each rule traces to ≥1 clause |
| 3 | Rule | CR-D-XX.Y-NNN | Each rule has ≥1 goal | Each goal traces to ≥1 rule |
| 4 | Goal | GOAL-PRIV-NN | Each goal has ≥1 UC | Each UC traces to ≥1 goal |
| 5 | Use Case | UC-NN | Each UC has ≥1 node | Each node traces to ≥1 UC |
| 6 | Node | NODE-XXX-NNN | Each node has ≥1 FR/NFR | Each FR/NFR traces to ≥1 node |
| 7 | FR/NFR | FR-NN / NFR-NN | Each FR/NFR has ≥1 gate | Each gate traces to ≥1 FR/NFR |
| 8 | Gate | GATE-D-XX.Y-NNN | Each gate has ≥1 allocation | Each allocation traces to ≥1 gate |

Verification: ALL forward AND reverse checks must pass for 100% traceability.

---

## 7. Cross-Case Node & Requirement Catalog

| Artifact | Case 01 | Case 02 | Case 03 | Growth Pattern |
|----------|---------|---------|---------|----------------|
| Process nodes | 20 | ~30 | ~30 | Linear with UC count |
| IT System nodes | 17 | ~25 | ~25 | Linear with UC count |
| Human Role nodes | 12 | ~15 | ~15 | Constant (~12-15) |
| Total nodes | 49 | ~70 | ~70 | Linear with UC count |
| FRs | 61 | ~80 | ~72 | Linear with UC count |
| NFRs | 46 | ~56 | ~50 | Sub-linear (plateaus at quality attributes) |
| DIRECT allocations | ~70% | ~65% | ~65% | Constant ratio |
| SHARED allocations | ~20% | ~25% | ~25% | Constant ratio |
| INHERITED allocations | ~10% | ~10% | ~10% | Constant ratio |
| Compliance gates | ~46 | ~63 | ~63 | Linear with rule count |

---

## 8. Node Hierarchy Guidelines

Guidelines for building and validating the parent-child node hierarchy in Doc 14 (Architectural Nodes):

### 8.1 Parent-Child Rules

| Rule | Description |
|------|-------------|
| HC-01 | An L1 node can have L2 children. An L2 node can have L3 children. L3 nodes are leaves (no children). |
| HC-02 | Parent-child relationships are established by functional dependency (e.g., MFA Service is child of Identity Provider because it depends on IdP authentication). |
| HC-03 | A node can have multiple children. Multi-parent nodes are allowed only when the child genuinely depends on two parents (e.g., a Cross-Border Data Transfer node may be child of both PKG-DP and PKG-GOV). |
| HC-04 | No circular parent-child relationships (A→B→A forbidden). |
| HC-05 | An L1 category cannot be a child of another L1 category. |

### 8.2 Cross-Track Relationships

Can a node of one track be a child of a node of another track?

| Parent track | Child track | Allowed? | Example |
|-------------|-------------|----------|---------|
| PROCESS | TECHNOLOGY | Yes | "Incident Response Process" (PROCESS) parents "SIEM Platform" (TECHNOLOGY) — the process uses the SIEM |
| TECHNOLOGY | PROCESS | Rare | "CI/CD Platform" (TECH) parents "Security Gate Process" (PROCESS) — the process runs on the platform |
| PROCESS | CAPABILITY_SUBREQ | Yes | "Risk Assessment Process" (PROCESS) parents "Security Analyst" (ROLE) — the process is performed by the analyst |
| TECHNOLOGY | CAPABILITY_SUBREQ | Yes | "IdP" (TECH) parents "Identity Admin" (ROLE) — the admin operates the IdP |
| CAPABILITY_SUBREQ | Any | Rare | A role rarely parents other nodes (roles don't contain systems) |

### 8.3 Orphan Prevention

Every node in Doc 14 must have:
- A parent (except L1 categories), AND
- At least one related UC (from Doc 13), AND
- At least one related rule (from Doc 11)

| Check | Detection | Action |
|-------|-----------|--------|
| No parent | L2/L3 node with parentNode = null | Flag as orphan, assign parent |
| No UC | Node not in any UC's relatedNodes | Flag as orphan, link to relevant UC |
| No rule | Node not in any allocation (Doc 15) | Flag as orphan, allocate |

### 8.4 Multi-Parent Rules

Multi-parent is allowed only when:
1. The child genuinely depends on BOTH parents functionally
2. Both parents are in different tracks (e.g., PROCESS + TECHNOLOGY)
3. The relationship is documented in Doc 14 §3 (Node Definition Structure)

Example: A "Secure Data Backup" node may be child of both "Data Protection Process" (PROCESS) and "Storage System" (TECHNOLOGY). The backup process runs on the storage system.

### 8.5 Hierarchy-Validation Checks

Before finalizing Doc 14, run these checks:

| Check ID | Check | Pass criterion |
|----------|-------|----------------|
| HV-01 | Every L2 has exactly one L1 parent | 100% |
| HV-02 | Every L3 has exactly one L2 parent (or multi-parent with documentation) | 100% |
| HV-03 | No cycles in parent-child graph | 100% |
| HV-04 | Track transitions are valid per §8.2 | 100% |
| HV-05 | Every node has ≥1 UC and ≥1 rule | 100% |
| HV-06 | OCL "Orphan Prevention" passes | 100% |
| HV-07 | OCL "Level Consistency" passes for all «refine» relationships | 100% |

### 8.6 Cross-Reference to Class Model

The node hierarchy must satisfy the class model OCL constraints. See [`phase3_decomposition.md`](../phase3_decomposition.md) (class model) for:
- `DecompositionLevel` enum: L0_BOUNDARY, L1_PRIMARY, L2_SUBFLOW, LN_ATOMIC
- `Track` enum: TECHNOLOGY, PROCESS, CAPABILITY_SUBREQ
- `FunctionalNode` class: `nodeId`, `name`, `description`, `Track track`, `DecompositionLevel level`, `verificationMethod`, `sourceUseCaseId`

---

## 9. Verification Methodology Detail

Detailed guidance on selecting and operating verification methods for compliance gates:

### 9.1 Evidence Catalog per Verification Method

| Method | Evidence type | Example artifacts |
|--------|--------------|-------------------|
| **TEST** | Automated test output | Test results (JUnit, pytest, etc.), config screenshots, CI/CD pipeline output, CI reports |
| **INSPECT** | Manual review documentation | Policy documents, procedure manuals, checklist completion records, audit reports |
| **DEMONSTRATE** | Live demonstration record | Demo recording, observation log, attendee sign-off, screen capture |
| **ANALYZE** | Architecture/design analysis | Architecture review document, threat model output, design rationale, gap analysis |

### 9.2 Frequency Options

| Frequency | When used | Example |
|-----------|-----------|---------|
| ONE_TIME | Run once, result is permanent | SBOM generation per release |
| PERIODIC | Run on a schedule (daily, weekly, monthly, quarterly, annual) | Access review (quarterly), risk assessment (annual) |
| CONTINUOUS | Always running, real-time | Security monitoring (24/7), logging |
| EVENT_DRIVEN | Triggered by an event | Incident notification, breach response |

### 9.3 Ownership per Verification Method

| Method | Who runs it | Who signs off | When |
|--------|-------------|---------------|------|
| **TEST** | Engineer (automated) | Tech lead or Security Engineer | Per release / per commit |
| **INSPECT** | Auditor or Compliance Lead | CISO or DPO | Per review cycle |
| **DEMONSTRATE** | Operations or Security Team | CTO or CISO | Per capability / annual |
| **ANALYZE** | Architect or Security Architect | CTO or CISO | Per design change |

### 9.4 Audit-Trail Artifacts

For regulatory evidence, each gate execution should produce:

| Artifact | Content | Retention |
|----------|---------|-----------|
| Gate execution log | Timestamp, who, result, method | Per regulation (GDPR 6yr, CRA 10yr, DORA 5yr) |
| Evidence reference | Specific doc/screenshot/recording | Same as above |
| Acceptance criteria result | Each criterion: PASS/FAIL/PARTIAL | Same as above |
| Remediation record | If FAILED/PARTIAL: plan, owner, due date | Until remediated + 1yr |

### 9.5 Cross-Case Verification Method Distribution

| Case | TEST | INSPECT | DEMONSTRATE | ANALYZE | Total |
|------|------|---------|--------------|----------|-------|
| Case 01 | 22 (48%) | 12 (26%) | 12 (26%) | 0 (0%) | 46 |
| Case 02 | 28 (44%) | 15 (24%) | 12 (19%) | 8 (13%) | 63 |
| Case 03 | 30 (48%) | 15 (24%) | 12 (19%) | 6 (9%) | 63 |

**Pattern:** TEST dominates (automated, repeatable). ANALYZE appears only in HIGH/MAX tiers (requires architecture review). INSPECT and DEMONSTRATE are stable ratios.

---

## 10. Acceptance Criteria Derivation Patterns

Patterns and anti-patterns for deriving testable acceptance criteria from rules, nodes, and verification methods:

### 10.1 The Derivation Formula

```
Acceptance Criterion = Rule Obligation (what) + Node Capability (where/who) + Testable Threshold (how to verify)
```

### 10.2 Pattern Catalog (10 patterns)

| # | Pattern | Rule type | Node type | Criterion template |
|---|---------|-----------|-----------|-------------------|
| 1 | **Encryption** | Data protection | IT System | "{Algorithm} enabled on {scope}, verified by config check" |
| 2 | **Access Control** | IAM | IT System | "{Role} has {permission}, verified by IdP config" |
| 3 | **MFA** | IAM | IT System | "{Account type} requires MFA, verified by IdP policy" |
| 4 | **Audit Logging** | Monitoring | IT System | "{Event type} logged with {fields}, log retention ≥{months}" |
| 5 | **Breach Notification** | Incident Response | Process | "Notification procedure executes within {hours}h, demonstrated in tabletop" |
| 6 | **Vulnerability Management** | Security Operations | IT System | "Scans run {frequency}, critical vulns patched within {hours}h" |
| 7 | **SBOM** | Supply Chain | IT System | "SBOM generated per release in {format}, stored in {repo}" |
| 8 | **Secure SDLC** | Secure Development | Process | "Code review + SAST + DAST on every PR, verified by CI gate" |
| 9 | **Risk Assessment** | Governance | Process | "Risk assessment conducted {frequency}, output reviewed by {role}" |
| 10 | **Training** | Human Factors | Process | "Training completed by {audience} within {timeframe}, completion ≥{pct}%" |

### 10.3 Worked Examples by Tier

**LOW tier (startup, Case 01):**
- Rule: CR-D-01.1-001 (encrypt data at rest)
- Node: NODE-SYS-004 (Encryption Service, INHERITED from AWS)
- Criterion: "AES-256 enabled on all S3 buckets containing personal data, verified by AWS Config check (TEST)"

**HIGH tier (enterprise, Case 02):**
- Rule: CR-D-01.1-001 (encrypt data at rest)
- Node: NODE-SYS-004 (Encryption Service, NATIVE)
- Criterion: "AES-256-GCM enabled on all data stores, key rotation every 90 days, verified by quarterly key audit (TEST + INSPECT)"

**MAX tier (bank, Case 03):**
- Rule: CR-D-01.1-001 + DORA Art. 9 (encrypt data at rest + ICT security)
- Node: NODE-SYS-004 (Encryption Service, NATIVE + HSM)
- Criterion: "AES-256-GCM with HSM-backed key management, key rotation every 30 days, access to keys audited in real-time, verified by automated TEST + monthly INSPECT + annual third-party ANALYZE"

### 10.4 Anti-Patterns (What NOT to do)

| Anti-pattern | Why it's wrong | Fix |
|--------------|----------------|-----|
| "Data is protected" | No measurable criterion | "AES-256 enabled, verified by TEST" |
| "Appropriate measures taken" | Vague, not testable | Specify algorithm, scope, verification |
| "System is secure" | Not a single acceptance criterion | Break into per-control criteria |
| "Compliant with GDPR Art. 32" | References the requirement, not the test | "All 4 GDPR Art. 32 requirements satisfied (pseudonymisation, encryption, resilience, testing)" |
| "Passed QA" | No evidence reference | "QA report ID QA-2026-042, signed by QALead" |

### 10.5 Criterion Quality Checklist

Before finalizing a gate's acceptance criterion, verify:

- [ ] Contains a specific measureable value (number, algorithm, frequency)
- [ ] References a specific evidence artifact (test ID, doc name, recording)
- [ ] Identifies the verification method (TEST/INSPECT/DEMONSTRATE/ANALYZE)
- [ ] Identifies the responsible party (who runs the verification)
- [ ] Is testable by a person who did NOT write the rule
- [ ] Can be PASS/FAIL (binary outcome, not "depends")

---

## Summary: How to Use This File

| If you need to... | Read this section |
|---|---|
| Decompose a UC into nodes | §1 — Node Decomposition Patterns |
| Derive NFRs from goals | §2 — NFR Quality Attribute Taxonomy |
| Derive FRs from UC + NFR + Rule | §3 — FR Derivation Patterns |
| Decide allocation type | §4 — Allocation Type Decision Matrix |
| Select verification method | §5 — Verification Method Selection |
| Verify traceability chain | §6 — 8-Level Traceability Verification |
| Estimate node/FR/NFR counts | §7 — Cross-Case Node & Requirement Catalog |
| Build or validate the node hierarchy | §8 — Node Hierarchy Guidelines |
| Choose evidence, frequency, and ownership for a gate | §9 — Verification Methodology Detail |
| Derive a testable acceptance criterion | §10 — Acceptance Criteria Derivation Patterns |

---

**See also:**
- [`phase3b_requirements.md`](phase3b_requirements.md) — Flow diagrams + LLM spec tables (companion)
- [`../phase3_decomposition.md`](../phase3_decomposition.md) — Phase 3 overview (parent)
- [`phase3a_iterative_cycle.md`](phase3a_iterative_cycle.md) — Phase 3A iterative cycle (predecessor, produces Doc 13)
- [`../phase1/phase1c_synthesis_reference.md`](../phase1/phase1c_synthesis_reference.md) — Phase 1C reference (analogue)
- [`../phase2/phase2c_framework_reference.md`](../phase2/phase2c_framework_reference.md) — Phase 2C reference (analogue)
- [`../../../TEMPLATES/14_Architectural_Nodes.md`](../../../TEMPLATES/14_Architectural_Nodes.md) — Doc 14 template
- [`../../../TEMPLATES/15_Requirements_Allocation.md`](../../../TEMPLATES/15_Requirements_Allocation.md) — Doc 15 template
- [`../../../TEMPLATES/16_Compliance_Gates_Report.md`](../../../TEMPLATES/16_Compliance_Gates_Report.md) — Doc 16 template
- [`../../../TEMPLATES/23_Functional_Requirements.md`](../../../TEMPLATES/23_Functional_Requirements.md) — Doc 23 template
- [`../../../TEMPLATES/24_Non_Functional_Requirements.md`](../../../TEMPLATES/24_Non_Functional_Requirements.md) — Doc 24 template
