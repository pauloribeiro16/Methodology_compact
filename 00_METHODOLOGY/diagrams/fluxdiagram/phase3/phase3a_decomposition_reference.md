---
document_id: AEGIS-DIAG-P3A-REFERENCE
title: "Phase 3A — Decomposition Reference: UC Patterns, Relationships, Variability & Scaling"
phase: 3A
version: 1.0
created: 2026-06-17
status: CREATED
parent_diagram: phase3a_iterative_cycle.md
source: Cross-case analysis (Docs 13, 13a, 13b from all 3 cases)
---

# Phase 3A — Decomposition Reference

**Version:** 1.0 — 2026-06-17
**Companion to:** [`phase3a_iterative_cycle.md`](phase3a_iterative_cycle.md) (iteration process + convergence decision tree)
**Sources:** Docs 13, 13a, 13b from Case 01, Case 02, Case 03 + Templates 13/13a/13b

---

## Overview

This file is the **reference companion** to the Phase 3A detailed flow diagrams. It contains the catalogs and analytical material that the EVAL and DERIVE steps (the `[LLM]` steps in the iteration cycle) draw upon when deriving security use cases:

1. **UC Derivation Patterns Catalog** — recurring security use case patterns indexed by what they protect and which sub-domains trigger them
2. **Relationship Patterns Catalog** — when to use «include» vs «extend», with detection rules
3. **Variability Patterns Catalog** — recurring cross-regulation variant shapes
4. **Cross-Case UC Catalog** — which UC patterns are universal vs case-specific across the 3 cases
5. **Negative-Example Discrimination Catalog** — what looks like a new UC but is not (prevents over-decomposition)
6. **Iteration Progression Analysis** — how coverage accumulates across iterations
7. **Scaling Analysis with Growth Pattern** — how UC count, packages, relationships, and variants scale with regulation count

The flow diagrams in [`phase3a_iterative_cycle.md`](phase3a_iterative_cycle.md) reference iteration mechanics, the coverage matrix, and the 7 convergence criteria. This file provides the pattern knowledge that drives the LLM reasoning inside those iterations.

---

## 1. UC Derivation Patterns Catalog

### 1.1 Overview

Security use cases are not invented ad hoc. They cluster into recurring **patterns** organised by what they protect. Each pattern is triggered by one or more sub-domains from the canonical 10 x 38 taxonomy and the rules (CR / BPR) that Doc 11 attaches to those sub-domains. When the coverage matrix shows a GAP in a given sub-domain, the table below identifies the pattern that typically closes it, the actors involved, and a representative use case.

Patterns map onto the UC packages produced at convergence (PKG-IAM, PKG-DP, PKG-SEC, PKG-IR, PKG-DEV, PKG-GOV, PKG-TRN). One pattern generally maps to one package; a few (Monitoring, Notification) are cross-cutting and referenced via «include»/«extend» from many packages.

### 1.2 Pattern Catalog

| # | Pattern | Protects (Sub-Domains) | Trigger Rules (Doc 11) | Typical Actors | Example UC |
|---|---------|------------------------|------------------------|----------------|------------|
| 1 | Authentication UCs | D-03.1 Identity Lifecycle · D-03.2 Authentication | CR-D-03.1-* · CR-D-03.2-* | End User · Identity Admin | User Authenticates (MFA, password, SSO) |
| 2 | Access Control UCs | D-03.3 Authorization · D-03.4 Access Review | CR-D-03.3-* · CR-D-03.4-* | End User · Access Manager | Enforce Access Policy / Review Entitlements |
| 3 | Data Protection UCs | D-01.1 Data at Rest · D-01.2 Data in Transit · D-01.3 Key Management | CR-D-01.1-* · CR-D-01.2-* · CR-D-01.3-* | System (automated) · Security Officer | Encrypt Data at Rest and in Transit / Rotate Keys |
| 4 | Data Subject Rights UCs | D-05.3 Erasure · D-05.4 Data Subject Rights | CR-D-05.3-* · CR-D-05.4-* | Data Subject · DPO / Compliance | Process Data Subject Access Request (DSAR) |
| 5 | Incident Response UCs | D-04.1 Detection · D-04.2 Response · D-04.3 Notification | CR-D-04.1-* · CR-D-04.2-* · CR-D-04.3-* | Security Team · MSSP · DPO | Detect, Contain, and Report Incident |
| 6 | Vulnerability Management UCs | D-02.1 Vulnerability Scanning · D-02.2 Patch Management | CR-D-02.1-* · CR-D-02.2-* | Developer · Security Team | Scan, Triage, and Remediate Vulnerabilities |
| 7 | Secure Development UCs | D-07.1 Secure-by-Design · D-07.2 Secure Build · D-07.3 Secure Deployment | CR-D-07.1-* · CR-D-07.2-* · CR-D-07.3-* | Developer · Release Manager | Build and Sign Secure Release / Generate SBOM |
| 8 | Supply Chain UCs | D-06.1 Vendor Management · D-06.2 Component Verification | CR-D-06.1-* · CR-D-06.2-* | Procurement · Security Officer | Assess Vendor Security / Verify Component Provenance |
| 9 | Governance UCs | D-09.1 Security Policies · D-09.2 Risk Assessment | CR-D-09.1-* · CR-D-09.2-* | CISO · DPO · Executive Board | Maintain Security Policy / Execute Risk Assessment |
| 10 | Training UCs | D-08.1 Security Awareness · D-08.2 Specialized Training | CR-D-08.1-* · CR-D-08.2-* | All Staff · HR / Training Lead | Deliver Security Awareness and Role Training |
| 11 | Monitoring & Audit UCs | D-10.1 Continuous Monitoring · D-10.2 Audit Logging · D-10.3 Compliance Testing | CR-D-10.1-* · CR-D-10.2-* · CR-D-10.3-* | Security Team · Internal/External Auditor | Record Audit Logs / Run Compliance Audit |
| 12 | Business Continuity UCs | D-04.4 BCP/DRP | CR-D-04.4-* | Operations Lead · Crisis Management Team | Execute Disaster Recovery / Failover |

### 1.3 How Patterns Drive Iteration Order

The pattern catalog explains **why** the cycle converges in roughly 4-5 iterations regardless of company size. Iteration 1 closes the patterns that are obvious from the Rules Catalog (1, 2, 3, 11). Iteration 2 closes the reactive patterns (5, 6). Iteration 3 closes the lifecycle and governance patterns (7, 8, 9, 10, 12). Iteration 4 closes the remaining variants and cross-pattern relationships (pattern 4, plus relationship/variability gaps). The fixed pattern count is why UC count plateaus near the sub-domain count.

---

## 2. Relationship Patterns Catalog

### 2.1 include vs extend — When to Use Each

Use case relationships (Doc 13a) use two UML stereotypes. The decision is mechanical once the triggering condition is recognised:

- **«include»** — the base UC *always* invokes the target UC. Mandatory, unconditional. Models shared behaviour that several UCs reuse.
- **«extend»** — the extending UC *may* be invoked at an extension point in the base UC. Optional, conditional. Models variant or additional behaviour.

| Pattern | When to use | Example | Detection rule |
|---------|-------------|---------|----------------|
| Authentication include | Every UC that requires an authenticated actor «include»s the authentication UC | DSAR UCs «include» User Authenticates | If the UC primary/secondary actor is an End User or Data Subject → «include» the auth UC |
| Logging extend | Security-relevant UCs «extend» the audit-logging UC at the state-change extension point | Access change / config change «extend» Audit Logging | If the UC modifies access rights, data, or system configuration → «extend» logging |
| Notification extend | Incident UCs «extend» the regulatory-notification UC at the classification extension point | Breach detection «extend» Regulatory Notification | If the UC is incident-related (D-04.*) → «extend» notification |
| Approval include | UCs requiring management sign-off «include» the approval UC before committing | Policy update / risk acceptance «include» Management Approval | If the UC changes a governance artifact (policy, risk register, scope) → «include» approval |

### 2.2 Closure Criterion (Convergence C4)

A relationship graph is **closed** when every «include» and «extend» registered in Doc 13a resolves to an existing use case. No dangling references. The detection rules above are applied symmetrically: if a UC matches a detection trigger, the corresponding relationship must exist, or the iteration registers it before convergence.

---

## 3. Variability Patterns Catalog

### 3.1 Overview

Variability (Doc 13b) captures where a single base UC must behave differently depending on which regulation is active, what scenario is in play, or what optional capability the company offers. Variants are NOT new use cases — they are documented deviations of an existing UC. The three UML-style variability kinds are **ALTERNATIVE** (different path to the same goal), **SPECIALIZATION** (regulation-specific variant), and **OPTION** (optional feature).

### 3.2 Recurring Variability Shapes

| Pattern | Base UC | Variability Kind | Variant Trigger | Example Variants |
|---------|---------|------------------|-----------------|------------------|
| Notification timeline | Regulatory Notification | SPECIALIZATION | Different regulation = different deadline | GDPR 72h · CRA 24h · NIS 2 24h · DORA 4h · AI Act 15d |
| Risk assessment | Risk Assessment | SPECIALIZATION | Different regulation = different trigger | DPIA (GDPR high-risk) · FRIA (AI Act high-risk) · ICT risk (DORA) · CRA risk assessment |
| Audit frequency | Compliance Audit | SPECIALIZATION | Different regulation = different frequency | Annual (GDPR) · per-release (CRA) · continuous (DORA) |
| Encryption standard | Data Encryption | SPECIALIZATION | Different regulation = different standard expectation | AES-256 (GDPR "appropriate") · TLS 1.3 (CRA "state of the art") |
| Break-glass auth | User Authenticates | ALTERNATIVE | Emergency scenario requires bypass of normal control | Normal MFA path vs manager-override break-glass path |
| MFA enrollment | User Authenticates | OPTION | MFA is optional for some user classes | Standard password vs optional MFA enrollment |
| Reporting recipient | Regulatory Notification | SPECIALIZATION | Different regulation = different recipient authority | DPA/SA (GDPR) · CSIRT (NIS 2) · competent authority (DORA) · market surveillance (CRA) |

### 3.3 Closure Criterion (Convergence C5)

Every variant registered in Doc 13b must reference an existing base UC and carry a **presence condition** (the boolean that decides whether the variant is active for this case). No orphaned variants. A variant whose presence condition is false for all applicable cases is removed during the validation pass.

---

## 4. Cross-Case UC Catalog

### 4.1 ID Format Note

This catalog uses the **canonical sequential UC ID format** (`UC-NN`) that the parent diagram [`phase3a_iterative_cycle.md`](phase3a_iterative_cycle.md) establishes as the intended output format (see its "Use Case Structure" table, example `UC-14`). Actual case files may still carry legacy formats pending migration:

- **Case 01** — hierarchical `U.C.X.Y.Z` (e.g., `U.C.3.1` Authenticate Users) in Doc 13 v5.0 (DRAFT)
- **Case 02** — category-prefixed `UC-IAM-NN` / `UC-DP-NN` (legacy, pre-canonical)
- **Case 03** — sequential `UC-NN` (already canonical)

This mirrors the documented FR/NFR canonical-vs-legacy situation in the root `AGENTS.md`. The IDs below are **canonical-form representative IDs** that locate the pattern, not verbatim quotes of every legacy label.

### 4.2 UC Pattern Catalog Across Cases

| UC Pattern | Case 01 ID | Case 02 ID | Case 03 ID | Common? | Notes |
|------------|-----------|-----------|-----------|---------|-------|
| User Authenticates | UC-14 | UC-IAM-01 | UC-14 | Yes (all) | Universal — every case needs auth |
| Data Subject Access Request | UC-01 | UC-DP-01 | UC-01 | Yes (GDPR cases) | All 3 cases are GDPR-scoped |
| Regulatory Notification | UC-32 | UC-SEC-07 | UC-32 | Yes (all) | Variants per regulation (Doc 13b) |
| Audit Logging | UC-21 | UC-SEC-04 | UC-21 | Yes (all) | «extend» target for many UCs |
| SBOM Generation | UC-25 | UC-DEV-05 | UC-25 | Yes (CRA cases) | Cases 01 + 02 (CRA); Case 03 via DORA/ICT third-party |
| Vulnerability Remediation | UC-09 | UC-DEV-03 | UC-09 | Yes (CRA/NIS2) | |
| Risk Assessment Execution | UC-28 | UC-GOV-02 | UC-28 | Yes (all) | Variants: DPIA / FRIA / ICT risk |
| Security Awareness Training | UC-30 | UC-TRN-01 | UC-30 | Yes (all) | |
| TLPT Execution | — | UC-SEC-12 | UC-SEC-12 | HIGH/MAX only | DORA-specific (threat-led penetration testing) |
| FRIA Execution | — | UC-AI-03 | UC-AI-03 | AI Act cases | Fundamentally Important Rights Assessment |
| Vendor Security Assessment | UC-17 | UC-SEC-09 | UC-17 | Yes (all) | DORA tightens scope in Case 03 |
| Disaster Recovery Failover | UC-33 | UC-SEC-11 | UC-33 | Yes (all) | DORA adds TLPT-driven scenarios in Case 03 |

### 4.3 Universal vs Case-Specific

- **Universal (all 3 cases):** authentication, access control, data encryption, DSAR, audit logging, incident detection/notification, vulnerability management, risk assessment, training, vendor assessment, disaster recovery.
- **HIGH/MAX only:** TLPT Execution (DORA Art. 26-27), advanced ICT third-party oversight.
- **AI Act cases only:** FRIA Execution, AI model governance, serious-incident reporting (AI Act Art. 73).

This split explains why Case 01 converges with ~35 UCs while Cases 02 and 03 plateau near ~50: the extra UCs are regulation-specific (AI Act, DORA), not additional core security behaviour.

---

## 5. Negative-Example Discrimination Catalog

### 5.1 Purpose

The most common over-decomposition failure is creating a new use case for what is really a variant, an «extend», or an inherited control. The table below records scenarios that look like they need a new security UC but do not. It is the negative-space counterpart to the derivation patterns in section 1, analogous to the negative compound-event examples in Phase 1C.

### 5.2 Discrimination Rules

| Scenario | Looks like | Why it is NOT a new UC | Correct action |
|----------|-----------|------------------------|----------------|
| User changes password | New auth UC | Same UC, different internal flow | Refine existing User Authenticates with an «extend» for password change |
| Monthly vulnerability scan vs weekly | Two vuln UCs | Same UC, different frequency | One Vulnerability Remediation UC with a frequency parameter |
| GDPR breach vs CRA breach notification | Two notification UCs | Same UC, variant timeline | Variability in Regulatory Notification (Doc 13b) — SPECIALIZATION |
| Cloud provider handles encryption | New encryption UC | Control is already inherited from the cloud provider | Mark as INHERITED in the coverage matrix — no new UC |
| Employee onboarding | New IAM UC | Part of the provisioning/access-assignment UC | Refine existing Access Control UC with onboarding flow |
| Quarterly access review vs annual | Two access-review UCs | Same UC, different frequency | One Access Review UC with frequency variant |
| Test environment logging | New logging UC | Same logging control, lower retention | Variant of Audit Logging (retention parameter), not a new UC |
| Processor-to-controller breach notify | New notification UC | Same notification family, different recipient/timeline | Variant of Regulatory Notification (processor path) |

### 5.3 Discrimination Heuristic

> If two candidate UCs share the same actors, the same protected asset, and the same primary security goal, they are **one UC with a variant**, not two UCs. A new UC is justified only when at least one of {actor, asset, goal} is genuinely different.

Applying this heuristic is what keeps the UC count bounded by the sub-domain count (~38) rather than growing with the rule count (~46-63).

---

## 6. Iteration Progression Analysis

### 6.1 Coverage Growth Per Iteration

Coverage accumulates in a recognisable shape: a large first-iteration jump (the obvious core controls), then diminishing returns as the cycle moves into reactive, governance, and finally edge-case patterns.

| Iteration | Focus (patterns from section 1) | Typical coverage gained | Cumulative coverage |
|-----------|--------------------------------|-------------------------|---------------------|
| 1 | Core security: auth, encryption, logging (1, 2, 3, 11) | 40-50% | 40-50% |
| 2 | Incident response, vulnerability mgmt (5, 6) | 20-25% | 65-70% |
| 3 | Governance, training, supply chain (7, 8, 9, 10, 12) | 15-20% | 85-90% |
| 4 | Edge cases, variants, relationship gaps (4 + section 3 variants) | 8-12% | 95-98% |
| 5+ | Validation pass, gap confirmation (no new patterns) | 2-5% | 100% |

### 6.2 Cross-Case Iteration Estimates

| Case | Iterations to converge | Rationale |
|------|------------------------|-----------|
| Case 01 | 4 | 2 regs, 20 applicable sub-domains — fewer rules per sub-domain, fewer variants |
| Case 02 | 5 | 4 regs, 38 sub-domains — more rules per sub-domain plus AI Act variants |
| Case 03 | 5 | 5 regs, 38 sub-domains — most rules, but DORA lex specialis absorbs some NIS 2 obligations |

### 6.3 Convergence C7 (No New Gaps)

The last iteration must complete without identifying any new gap. If iteration N derives new UCs, iteration N+1 is required to confirm stability — even if N+1 finds nothing. This is why the typical case needs one more iteration than the "coverage hits 100%" iteration.

---

## 7. Scaling Analysis with Growth Pattern

### 7.1 Scaling Table

| Metric | Case 01 (2 regs) | Case 02 (4 regs) | Case 03 (5 regs) | Growth Pattern |
|--------|-------------------|-------------------|-------------------|----------------|
| Security UCs | 35 | ~50 | ~50 | Logarithmic (plateaus at sub-domain count) |
| Packages | 6 | 7+ | 7+ | Constant (~6-7) |
| Relationships | ~15 | ~26 | ~23 | Linear with UC count |
| Variants | ~5 | ~10 | ~8 | Sub-linear (regulation-driven) |
| UCs per package | 5.8 | ~7.1 | ~7.1 | Constant (~6-7) |
| Relationships per UC | 0.43 | 0.52 | 0.46 | Constant (~0.4-0.5) |
| Iterations to converge | 4 | 5 | 5 | Logarithmic |

### 7.2 Key Scaling Insights

**1. UC count plateaus at the sub-domain count, not the rule count.** There are 38 canonical sub-domains. Once each has at least one UC, adding more regulations adds rules per sub-domain (covered by variants and «include»/«extend») rather than new UCs. This is why Cases 02 and 03 (4-5 regs) converge near ~50 UCs despite having ~63 rules vs Case 01's 46.

**2. Package count is essentially constant (~6-7).** Packages mirror security domains (IAM, DP, SEC, IR, DEV, GOV, TRN). More regulations do not create new domains — they populate existing ones. Case 02 adds an AI package; Case 03 stays at ~7 because DORA maps onto existing domains.

**3. Relationships scale linearly with UC count, at a stable ratio (~0.4-0.5 per UC).** Roughly every second UC participates in one «include» or «extend». This ratio is stable because the relationship detection rules (section 2) are pattern-driven, not regulation-driven.

**4. Variants scale sub-linearly with regulation count.** Variants are driven by regulation-specific deadlines/standards (section 3). Case 02 has the most variants (~10) because AI Act + CRA + NIS 2 + GDPR each impose distinct notification/assessment variants. Case 03 has slightly fewer (~8) because DORA's lex specialis absorbs some NIS 2 obligations, collapsing two variants into one.

**5. Iterations to converge grow logarithmically.** Doubling the regulation count (2 -> 5) adds only one iteration. The cycle's fixed pattern catalog (section 1) bounds the work per iteration; more regulations mean more rules to check per pattern, not more patterns to discover.

---

## 8. Package Structure Rationale

### 8.1 Canonical Package Set

The AEGIS methodology defines a canonical set of UC packages, each mapped to one or more security domains (from the 10x38 taxonomy):

| Package ID | Package Name | Maps to Domains | Purpose |
|-----------|-------------|----------------|---------|
| PKG-DP | Data Protection | D-05 (Data Lifecycle) | Enable data subject rights and personal data protection |
| PKG-SEC | Security Operations | D-02 (Vulnerability), D-04 (Incident) | Detect, respond to, and recover from security incidents |
| PKG-IAM | Identity & Access | D-03 (Access Control) | Manage user identities and access control |
| PKG-DEV | Secure Development | D-06 (Supply Chain), D-07 (Secure Dev) | Build security into development lifecycle |
| PKG-GOV | Governance & Compliance | D-09 (Governance), D-10 (Monitoring) | Maintain compliance and manage risk |
| PKG-TRN | Training & Awareness | D-08 (Human Factors) | Security training for all users |
| PKG-IR | Incident Response | D-04 (sub-set) | Specialized incident response (DORA-critical entities) |
| PKG-AI | AI Governance | D-07 (sub-set) | AI-specific controls (AI Act cases only) |

### 8.2 Package-to-Sub-Domain Mapping

| Package | Sub-Domains Covered |
|---------|---------------------|
| PKG-DP | D-05.1, D-05.2, D-05.3, D-05.4 |
| PKG-SEC | D-02.1, D-02.2, D-02.3, D-04.1, D-04.2, D-04.3, D-04.4 |
| PKG-IAM | D-03.1, D-03.2, D-03.3, D-03.4 |
| PKG-DEV | D-06.1, D-06.2, D-07.1, D-07.2, D-07.3 |
| PKG-GOV | D-09.1, D-09.2, D-09.3, D-09.4, D-10.1, D-10.2, D-10.3 |
| PKG-TRN | D-08.1, D-08.2, D-08.3 |
| PKG-IR | D-04.1, D-04.2, D-04.3, D-04.4 (DORA-intensive) |
| PKG-AI | D-07.4, D-09.5 (AI Act-specific) |

### 8.3 When a New Package is Justified

A new package is created when:
1. A regulation adds a domain not covered by existing packages (e.g., PKG-AI added for AI Act)
2. A sub-domain has >5 UCs that don't fit naturally in existing packages
3. A company's operational model has a unique separation (e.g., PKG-IR for banks with dedicated SOC)

**Rule:** Do not create a new package for a single UC. Minimum 3 UCs required.

### 8.4 UC-to-Package Assignment Rules

| Rule | Description |
|------|-------------|
| Single-domain UCs | Assign to package whose sub-domain mapping includes the UC's primary sub-domain |
| Multi-domain UCs | Assign to the package of the primary sub-domain; use «include» for secondary |
| Regulation-specific variants | Stay in the same package as the base UC |
| Cross-cutting UCs (e.g., audit) | Assign to PKG-GOV (governance is the natural home) |

### 8.5 Cross-Case Package Density

| Case | Packages | Total UCs | Avg UCs per package | Notes |
|------|----------|-----------|---------------------|-------|
| Case 01 | 6 | 35 | 5.8 | No PKG-AI, no PKG-IR |
| Case 02 | 7 (includes PKG-AI) | ~50 | ~7.1 | AI Act triggers PKG-AI |
| Case 03 | 7 (includes PKG-IR) | ~50 | ~7.1 | DORA triggers PKG-IR |

---

## 9. Actor Catalog & SLA Derivation

### 9.1 Actor Catalog

Actors are derived from the stakeholder catalog in Doc 04 section 10 (Role Matrix). Each actor has a type (Human, System, External) and a role (Primary or Secondary) in the UC.

| Actor ID | Actor Name | Type | Source (Doc 04) | Typical UC role |
|----------|-----------|------|-----------------|-----------------|
| ACT-INT-001 | End User | Human | Internal stakeholder | Primary (data subject UCs) |
| ACT-INT-002 | Data Subject | Human | Internal stakeholder | Primary (GDPR data-rights UCs) |
| ACT-INT-003 | Developer | Human | Internal stakeholder | Primary (PKG-DEV UCs) |
| ACT-INT-004 | Operations | Human | Internal stakeholder | Primary (PKG-SEC, PKG-IAM UCs) |
| ACT-INT-005 | DPO/Compliance | Human | Internal stakeholder | Primary (PKG-DP, PKG-GOV UCs) |
| ACT-INT-006 | CTO | Human | Internal stakeholder | Secondary (governance UCs) |
| ACT-INT-007 | CEO | Human | Internal stakeholder | Secondary (incident response, governance) |
| ACT-INT-008 | Security Analyst | Human | Internal stakeholder | Primary (PKG-SEC UCs) |
| ACT-INT-009 | CISO | Human | Internal stakeholder | Secondary (security governance) |
| ACT-EXT-001 | MSSP (Managed Security) | System | External provider | Primary (24/7 monitoring, Case 01) |
| ACT-EXT-002 | Cloud Provider | System | External provider | Secondary (inherited controls) |
| ACT-EXT-003 | Regulator | Human | External authority | Primary (notification UCs) |
| ACT-EXT-004 | Auditor | Human | External authority | Primary (PKG-GOV audit UCs) |
| ACT-EXT-005 | Customer/Client | Human | External party | Primary (data subject UCs) |
| ACT-SYS-001 | IdP (Identity Provider) | System | Company system | Secondary (auth UCs) |
| ACT-SYS-002 | SIEM Platform | System | Company system | Secondary (monitoring UCs) |
| ACT-SYS-003 | CI/CD Platform | System | Company system | Primary (PKG-DEV security gate UC) |

### 9.2 SLA Derivation — Regulatory Deadline Reference Table

When deriving SLAs for UCs, start with the regulatory deadline (fastest) and adjust by company tier:

| Regulation | Obligation | Regulatory Deadline | LOW (Case 01) | HIGH (Case 02) | MAX (Case 03) |
|------------|-----------|---------------------|---------------|-----------------|----------------|
| GDPR Art. 33 | Breach notification to authority | 72 hours | 72h | 48h | 24h |
| GDPR Art. 34 | Breach notification to data subject | 72 hours (high risk) | 72h | 48h | 24h |
| GDPR Art. 15 | Data subject access request | 30 days (max) | 30d | 15d | 7d |
| GDPR Art. 17 | Erasure request | 30 days (max) | 30d | 15d | 7d |
| CRA Art. 11 | Incident notification (manufacturer) | 24 hours | 24h | 12h | 4h |
| CRA Art. 14 | Vulnerability notification | 24 hours | 24h | 12h | 4h |
| NIS 2 Art. 23 | Incident notification (essential entity) | 24 hours (early warning) | 24h | 12h | 4h |
| NIS 2 Art. 23 | Incident notification (full) | 72 hours | 72h | 48h | 24h |
| DORA Art. 19 | Major ICT incident (initial) | 4 hours (RTS) | N/A | 4h | 2h |
| DORA Art. 19 | Major ICT incident (intermediate) | 72 hours | N/A | 72h | 48h |
| DORA Art. 19 | Major ICT incident (final) | 1 month | N/A | 1m | 2w |
| AI Act Art. 73 | Serious incident notification | 15 days | N/A | 15d | 10d |
| AI Act Art. 73 | Serious incident (preliminary) | 2 days | N/A | 2d | 1d |
| Best Practice | Quarterly access review | 90 days | 90d | 90d | 90d |
| Best Practice | Annual risk assessment | 365 days | 365d | 365d | 365d |
| Best Practice | SBOM per release | Per release | Per release | Per release | Per release |

### 9.3 Tier-Proportional SLA Methodology

1. Start with the **regulatory deadline** (column 3) as the maximum.
2. For LOW tier, use the regulatory deadline as-is.
3. For HIGH tier, reduce by 25-50% (more capacity for 24/7 monitoring, MSSP).
4. For MAX tier, reduce by 50-75% (in-house SOC, automated pipelines).
5. Document the rationale in Doc 13 section 6 (SLA field): "GDPR 72h, reduced to 24h based on HIGH tier SLA methodology."

### 9.4 SLA-to-UC Binding Rules

| UC type | SLA binding |
|---------|-------------|
| Notification UC | SLA = regulatory deadline (non-negotiable) |
| Detection UC | SLA = detection time (e.g., 4h with MSSP) |
| Response UC | SLA = response time (e.g., contain within 24h) |
| Provisioning UC | SLA = provisioning time (e.g., 24h from request) |
| Periodic UC | SLA = frequency (e.g., quarterly) |
| Continuous UC | SLA = "24/7" or "continuous" |

---

## 10. Concrete Iteration Example (Case 01)

### 10.1 Case 01 Context

Company: TinyTask SaaS (8 employees, 2 regulations: GDPR + CRA)
Starting coverage: 0% (no UCs)
Target: 100% coverage (all applicable sub-domains have security UCs)

### 10.2 Iteration-by-Iteration Trace

#### Iteration 1 — Core Security Foundations

**Focus:** Authentication, encryption, logging (obvious gaps)
**Coverage before:** 0%
**Coverage after:** 45% (20/38 sub-domains with at least 1 UC)

| UC ID | Name | Package | Sub-domain | Rules covered |
|-------|------|---------|-----------|---------------|
| UC-14 | User Authenticates | PKG-IAM | D-03.1, D-03.2 | CR-D-03.1-001, CR-D-03.2-001 |
| UC-15 | User Registers Account | PKG-IAM | D-03.1 | CR-D-03.1-001 |
| UC-16 | User Enrolls in MFA | PKG-IAM | D-03.2 | CR-D-03.2-001 |
| UC-17 | User Resets Password | PKG-IAM | D-03.1 | CR-D-03.1-001 |
| UC-01 | Data Subject Access Request | PKG-DP | D-05.4 | CR-D-05.4-001 |
| UC-02 | Data Subject Erasure Request | PKG-DP | D-05.3 | CR-D-05.3-001 |
| UC-04 | User Manages Consent | PKG-DP | D-05.1 | CR-D-05.1-001 |
| UC-09 | Vulnerability Scan Executed | PKG-SEC | D-02.1 | CR-D-02.1-001 |
| UC-12 | Security Monitoring Performed | PKG-SEC | D-04.1, D-10.1 | CR-D-10.1-001 |
| UC-23 | Security Gate Executed | PKG-DEV | D-07.3 | CR-D-07.3-001 |
| UC-25 | SBOM Generated | PKG-DEV | D-06.2 | CR-D-06.2-001 |
| UC-26 | Policy Review Conducted | PKG-GOV | D-09.1 | CR-D-09.1-001 |
| UC-27 | Risk Assessment Conducted | PKG-GOV | D-09.2 | CR-D-09.2-001 |
| UC-33 | Security Awareness Training | PKG-TRN | D-08.1 | CR-D-08.1-001 |

**Relationships registered:** UC-01 «include» UC-14, UC-02 «include» UC-14, UC-17 «extend» UC-14

**Variants identified:** None yet (all 14 UCs are core, no regulation-specific variants)

#### Iteration 2 — Incident Response & Operational

**Focus:** Incident detection, response, notification, access management
**Coverage before:** 45%
**Coverage after:** 72% (27/38 sub-domains)

| UC ID | Name | Package | New sub-domains |
|-------|------|---------|----------------|
| UC-07 | Security Incident Detected | PKG-SEC | D-04.1 |
| UC-08 | Security Incident Responded | PKG-SEC | D-04.2 |
| UC-32 | Regulatory Notification Submitted | PKG-SEC | D-04.3 |
| UC-11 | Access Rights Reviewed | PKG-SEC | D-03.3 |
| UC-18 | Admin Provisions User | PKG-IAM | D-03.1 (refined) |
| UC-19 | Admin Deprovisions User | PKG-IAM | D-03.1 (refined) |
| UC-20 | Admin Assigns Role | PKG-IAM | D-03.3 (refined) |
| UC-28 | Audit Logs Reviewed | PKG-GOV | D-10.2 |
| UC-22 | Dependency Check Executed | PKG-DEV | D-02.1 (refined) |
| UC-21 | Code Security Scan Executed | PKG-DEV | D-07.2 |
| UC-31 | DPIA Executed | PKG-GOV | D-09.3 |
| UC-03 | Data Subject Exports Data | PKG-DP | D-05.4 (refined) |
| UC-05 | Data Subject Rectification | PKG-DP | D-05.2 |

**Variants identified:** UC-32 has 2 variants (GDPR 72h vs CRA 24h)

#### Iteration 3 — Supply Chain, Development, Edge Cases

**Focus:** Supplier security, business continuity, training depth
**Coverage before:** 72%
**Coverage after:** 90% (34/38 sub-domains)

| UC ID | Name | Package | New sub-domains |
|-------|------|---------|----------------|
| UC-30 | Vendor Security Assessed | PKG-GOV | D-06.1 |
| UC-13 | Business Continuity Activated | PKG-SEC | D-04.4 |
| UC-10 | Security Patch Deployed | PKG-SEC | D-02.2 |
| UC-24 | Change Request Submitted | PKG-DEV | D-07.4 |
| UC-29 | Compliance Report Generated | PKG-GOV | D-10.3 |
| UC-06 | Data Subject Breach Notification | PKG-DP | D-04.3 (data subject) |
| UC-34 | Role-Specific Training | PKG-TRN | D-08.2 |

**Variants identified:** UC-32 gets third variant (NIS 2 — but Case 01 doesn't apply, so skipped)

#### Iteration 4 — Gap Closure & Validation

**Focus:** Remaining 4 sub-domains + relationship closure + variant validation
**Coverage before:** 90%
**Coverage after:** 98% (37/38 sub-domains)

| UC ID | Name | Package | New sub-domains |
|-------|------|---------|----------------|
| UC-35 | Phishing Simulation | PKG-TRN | D-08.1 (refined) |
| UC-31a | Risk Treatment Plan | PKG-GOV | D-09.4 |

**Relationships validated:** All «include» and «extend» resolve to existing UCs (100% closure)

#### Iteration 5 — Confirmation Pass (C7)

**Focus:** Validate that last iteration found no new gaps
**Result:** Coverage matrix identical to Iteration 4 → C7 satisfied → CONVERGED

**Final state:** 35 UCs, 6 packages, 15 relationships, 2 variants → Cycle exits → Doc 13 ready for Phase 3B

### 10.3 Coverage Progression Visualization

```
Iteration 1: ████████████████████░░░░░░░░░░░░░░░░░░ 45%
Iteration 2: ██████████████████████████████░░░░░░░░ 72%
Iteration 3: ██████████████████████████████████████░ 90%
Iteration 4: ███████████████████████████████████████ 98%
Iteration 5: (confirmation — no change)              98% → CONVERGED
```

---

## Summary: How to Use This File

| If you need to... | Read this section |
|-------------------|-------------------|
| Identify which UC pattern closes a coverage gap | section 1 — UC Derivation Patterns Catalog |
| Decide between «include» and «extend» | section 2 — Relationship Patterns Catalog |
| Decide whether a regulation difference is a variant | section 3 — Variability Patterns Catalog |
| Check if a UC pattern is universal or case-specific | section 4 — Cross-Case UC Catalog |
| Avoid creating a redundant UC | section 5 — Negative-Example Discrimination Catalog |
| Estimate how many iterations a case will need | section 6 — Iteration Progression Analysis |
| Estimate UC/package/relationship counts for a new case | section 7 — Scaling Analysis |

---

**See also:**
- [`phase3a_iterative_cycle.md`](phase3a_iterative_cycle.md) — Iteration process + convergence decision tree (companion)
- [`../phase3_decomposition.md`](../phase3_decomposition.md) — Phase 3 overview (parent)
- [`phase3b_requirements.md`](phase3b_requirements.md) — Requirements & allocation (successor)
- [`../../../TEMPLATES/13_Use_Cases_Catalog.md`](../../../TEMPLATES/13_Use_Cases_Catalog.md) — Doc 13 template
- [`../../../TEMPLATES/13a_Use_Case_Relationships.md`](../../../TEMPLATES/13a_Use_Case_Relationships.md) — Doc 13a template
- [`../../../TEMPLATES/13b_Use_Case_Variability.md`](../../../TEMPLATES/13b_Use_Case_Variability.md) — Doc 13b template
- [`../phase1/phase1b_nuances_and_reasoning.md`](../phase1/phase1b_nuances_and_reasoning.md) — Phase 1B reference (analogous companion)
- [`../phase1/phase1c_synthesis_reference.md`](../phase1/phase1c_synthesis_reference.md) — Phase 1C synthesis reference (analogous companion)
