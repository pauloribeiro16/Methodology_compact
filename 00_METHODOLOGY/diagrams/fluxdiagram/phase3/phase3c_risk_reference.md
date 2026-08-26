---
document_id: AEGIS-DIAG-P3C-REFERENCE
title: "Phase 3C — Threat Modeling Reference (Catalogs & Patterns)"
phase: 3C
version: 1.0
created: 2026-06-16
status: CREATED
parent_diagram: phase3c_threat_modeling.md
source: 00_METHODOLOGY/TEMPLATES/25_Risk_Analysis.md
---

# Phase 3C — Threat Modeling Reference (Catalogs & Patterns)

**Version:** 1.0 — 2026-06-16
**Companion to:** [`phase3c_threat_modeling.md`](phase3c_threat_modeling.md) (flow diagrams)
**Sources:** Doc 25 template + class model [`../phase3_risk_analysis.md`](../phase3_risk_analysis.md)

---

## Overview

This file is the **reference companion** to the Phase 3C threat modeling flow diagrams. It contains:

1. **STRIDE Pattern Catalog** — typical threats per UC type
2. **LINDDUN Pattern Catalog** — privacy threats per data type
3. **Risk Matrix Reference** — 4×4 matrix with score thresholds
4. **D3FEND Mapping Catalog** — mitigations → MITRE D3FEND techniques
5. **Mitigation Strategy Selection Guide** — when to use each strategy
6. **KG Inference Examples** — cross-case patterns
7. **Threat Scaling Analysis** — how threat counts scale

The flow diagrams in [`phase3c_threat_modeling.md`](phase3c_threat_modeling.md) reference the threat modeling process, decision branches, and 3 convergence criteria. This file provides the catalog knowledge (patterns, mappings, thresholds) that the process draws upon when identifying threats, scoring risks, and selecting mitigations.

---

## 1. STRIDE Pattern Catalog

Typical threats by UC package/type:

### 1.1 Authentication UCs (PKG-IAM)

| Category | Typical threat | Example |
|----------|---------------|---------|
| S | Credential stuffing | Attacker uses leaked credentials from other breaches |
| S | Password spraying | Attacker tries common passwords across many accounts |
| T | Session token modification | Attacker modifies JWT in transit |
| R | User denies login action | No audit trail of authentication event |
| I | Session token in logs | Token leaked to error logs |
| D | Auth endpoint flooding | Attacker overwhelms login service |
| E | Auth bypass via parameter tampering | Attacker modifies role claim in token |

### 1.2 Data Protection UCs (PKG-DP)

| Category | Typical threat | Example |
|----------|---------------|---------|
| S | DSAR request as another user | Attacker requests another user's data |
| T | Erasure request targets wrong data | Race condition in deletion logic |
| R | Consent withdrawal not logged | User denies giving consent |
| I | DSAR report sent to wrong party | Email address typo exposes data |
| D | DSAR endpoint overwhelmed | Flood of fake DSAR requests |
| E | User erases another user's data | IDOR in erasure endpoint |

### 1.3 Security Operations UCs (PKG-SEC)

| Category | Typical threat | Example |
|----------|---------------|---------|
| S | False vulnerability report | Attacker submits fake CVE to waste resources |
| T | Alert thresholds modified | Attacker changes detection rules to hide activity |
| R | Alert action not logged | No audit of who dismissed an alert |
| I | SIEM data exposed | Monitoring dashboard accessible to unauthorized user |
| D | Alert flood | Attacker generates noise to hide real alerts |
| E | Monitoring disabled | Attacker gains admin to disable SIEM |

### 1.4 Secure Development UCs (PKG-DEV)

| Category | Typical threat | Example |
|----------|---------------|---------|
| S | Malicious code as legitimate developer | Compromised developer credentials |
| T | SAST results modified | Attacker changes scan output to pass build |
| R | Code commit not attributed | Anonymous commit accepted |
| I | Source code in CI/CD logs | Secrets or IP in build output |
| D | CI/CD pipeline flooded | Attacker blocks deployments |
| E | Security gate bypassed | Developer uses admin to skip gate |

### 1.5 Governance UCs (PKG-GOV)

| Category | Typical threat | Example |
|----------|---------------|---------|
| S | Fake compliance report | Attacker submits fraudulent attestation |
| T | Audit log modification | Attacker edits logs to hide actions |
| R | Compliance decision not logged | No record of who approved exception |
| I | Compliance data exposed | Report accessible without authorization |
| D | DPO overwhelmed with fake requests | Flood of bogus DSARs |
| E | Unauthorized policy modification | Low-privilege user changes governance doc |

### 1.6 Training UCs (PKG-TRN)

| Category | Typical threat | Example |
|----------|---------------|---------|
| S | Training completed as another person | User delegates training to colleague |
| T | Training records modified | HR modifies completion records |
| R | Training not attested | No proof user completed training |
| I | Training content exposes sensitive data | Internal info in training materials |
| D | Training platform unavailable | Scheduled training missed |
| E | User marks training complete without attending | Bypass of training gate |

---

## 2. LINDDUN Pattern Catalog

Typical privacy threats by data type:

### 2.1 Personal Data (GDPR Art. 4(1))

| Category | Typical threat | GDPR article |
|----------|---------------|--------------|
| L | Cross-session correlation | Art. 5(1)(c) |
| I | Re-identification from anonymized data | Art. 4(1) |
| N | Consent not provable | Art. 7(1) |
| D | Processing invisible to data subject | Art. 15 |
| D | Data disclosed to unauthorized party | Art. 32 |
| U | Data subject unaware of processing | Art. 13 |
| N | No legal basis for processing | Art. 6 |

### 2.2 Sensitive Data (GDPR Art. 9)

| Category | Typical threat | GDPR article |
|----------|---------------|--------------|
| L | Health data correlation across services | Art. 9 |
| I | Identification from biometric data | Art. 9 |
| N | Explicit consent not captured | Art. 9(2) |
| D | Sensitive data not accessible to data subject | Art. 15 |
| D | Sensitive data breached | Art. 32 + Art. 34 |
| U | Data subject not informed of sensitive processing | Art. 13 |
| N | Sensitive processing without explicit consent | Art. 9 |

### 2.3 Children's Data (GDPR Art. 8)

| Category | Typical threat | GDPR article |
|----------|---------------|--------------|
| L | Child's activities tracked across services | Art. 8 + Art. 5(1)(c) |
| I | Child identifiable from behavioral data | Art. 8 + Art. 4(1) |
| N | Parental consent not verifiable | Art. 8(2) |
| D | Child unaware of data collection | Art. 8 + Art. 13 |
| D | Child's data shared with third party | Art. 8 + Art. 32 |
| U | Child not informed in age-appropriate way | Art. 12 + Art. 8 |
| N | Processing without parental consent | Art. 8 |

---

## 3. Risk Matrix Reference (4×4)

```
                IMPACT
          Low(1)  Med(2)  High(3)  Crit(4)
        ┌─────────────────────────────────┐
    L(1)│   1      2       3        4    │
    M(2)│   2      4       6        8    │
L   H(3)│   3      6       9       12    │
    C(4)│   4      8      12       16    │
        └─────────────────────────────────┘
```

### 3.1 Score Interpretation

| Score | Risk Level | Required Treatment | Action |
|-------|-----------|-------------------|--------|
| 12-16 | HIGH/CRITICAL | MITIGATE (mandatory) | Design control, iterate if SC5 fails |
| 6-11 | MEDIUM | MITIGATE or ACCEPT | Cost-benefit analysis |
| 2-5 | LOW | ACCEPT or TRANSFER | Document decision |
| 1 | MINIMAL | ACCEPT | No action needed |

### 3.2 Likelihood Scale

| Value | Label | Definition |
|-------|-------|------------|
| 1 | Low | Unlikely to occur in the system's lifetime |
| 2 | Medium | Could occur but not expected |
| 3 | High | Likely to occur at least once |
| 4 | Critical | Certain to occur or already occurring |

### 3.3 Impact Scale

| Value | Label | Definition |
|-------|-------|------------|
| 1 | Low | Minor inconvenience, no regulatory consequence |
| 2 | Medium | Operational disruption, possible complaint |
| 3 | High | Regulatory action, material harm to data subjects |
| 4 | Critical | Fundamental rights violation, mass harm, enforcement |

---

## 4. D3FEND Mapping Catalog

MITRE D3FEND technique mappings for common mitigations:

| Mitigation | D3FEND ID | D3FEND Technique | Phase 3C → Decomposition |
|-----------|-----------|------------------|--------------------------|
| Multi-factor authentication | D3-MA | Multi-Factor Authentication | NEW UC: MFA Enrollment |
| Data encryption at rest | D3-DE | Data Encryption | STRENGTHEN: existing FR |
| Rate limiting | D3-TL | Traffic Limiting | NEW UC: Rate Limiting |
| Data minimization | D3-DP | Data Partitioning | STRENGTHEN: DSAR FRs |
| Secret detection | D3-SD | Secret Detection | NEW UC: CI/CD Secret Scan |
| Write-once logging | D3-IL | Immutable Logging | ARCH_CHANGE: Audit Repository |
| Access control review | D3-ACR | Access Control Review | NEW UC: Quarterly Review |
| Network segmentation | D3-NI | Network Isolation | ARCH_CHANGE: new network node |
| Vulnerability scanning | D3-VM | Vulnerability Monitoring | STRENGTHEN: existing Vuln UC |
| Privilege separation | D3-PS | Privilege Separation | NEW UC: Privilege Audit |
| Input validation | D3-IV | Input Validation | STRENGTHEN: existing FR |
| Backup verification | D3-BV | Backup Verification | NEW UC: Backup Test |

### 4.1 D3FEND Coverage by Case

| Case | D3FEND techniques used | Coverage |
|------|------------------------|----------|
| Case 01 | 6 | MFA, DE, TL, DP, SD, IL |
| Case 02 | 10 | + ACR, NI, VM, PS |
| Case 03 | 12 | + IV, BV |

---

## 5. Mitigation Strategy Selection Guide

Decision logic for choosing the right strategy:

```
Q1: Do existing FRs/NFRs fully cover this risk?
    YES → STRENGTHEN_EXISTING (enhance acceptance criteria)
    NO → Q2

Q2: Is the risk inherent to the current architecture?
    YES → ARCHITECTURAL_CHANGE (new node, possibly new UC)
    NO → Q3

Q3: Is the needed capability a new function not covered by any FR?
    YES → NEW_FUNCTIONAL_NODE (new UC, new node, new gate)
    NO → Q4

Q4: Is the risk operational (people, process, policy)?
    YES → PROCESS_CONTROL (new process node)
    NO → Review (may need escalation)
```

### 5.1 Strategy Comparison

| Strategy | Cost | Time | Feedback to Decomp | Residual Risk |
|----------|------|------|--------------------|----------------| 
| NEW_FUNCTIONAL_NODE | High | Long | Yes (full iteration) | LOW |
| STRENGTHEN_EXISTING | Medium | Short | Yes (refinement) | LOW-MEDIUM |
| ARCHITECTURAL_CHANGE | High | Long | Yes (new node) | LOW |
| PROCESS_CONTROL | Low | Short | Optional | MEDIUM |

### 5.2 Cross-Case Strategy Distribution

| Case | NEW_FUNCTIONAL_NODE | STRENGTHEN_EXISTING | ARCHITECTURAL_CHANGE | PROCESS_CONTROL | Total |
|------|---------------------|----------------------|-----------------------|-------------------|-------|
| Case 01 | 3 | 3 | 1 | 1 | 8 |
| Case 02 | 5 | 4 | 2 | 1 | 12 |
| Case 03 | 4 | 3 | 2 | 1 | 10 |

---

## 6. KG Inference Examples

Cross-case patterns the knowledge graph uses to infer threats:

### 6.1 Case 01 Examples

| Inference ID | Source pattern | Inferred threat | Confidence |
|--------------|---------------|-----------------|------------|
| INF-THR-01 | UC-14 (auth) + AST-01 (credentials) | Credential stuffing | HIGH |
| INF-THR-02 | UC-01 (DSAR) + GDPR Art. 15 | Data exfiltration via DSAR | MEDIUM |
| INF-THR-03 | NODE-SYS-006 (API Gateway) + STRIDE-T | SQL/NoSQL injection | HIGH |
| INF-THR-04 | NODE-SYS-012 (CI/CD) + STRIDE-T | Supply chain compromise | HIGH |
| INF-THR-05 | UC-28 (Audit Log Review) + AST-08 | Log injection attack | MEDIUM |

### 6.2 Case 02 Examples

| Inference ID | Source pattern | Inferred threat | Confidence |
|--------------|---------------|-----------------|------------|
| INF-THR-06 | UC-IAM-01 (MFA) + STRIDE-S | MFA bypass via SIM swapping | MEDIUM |
| INF-THR-07 | NODE-SYS-002 (Vuln Scanner) + STRIDE-T | Scanner result poisoning | LOW |
| INF-THR-08 | UC-SEC-12 (TLPT) + DORA Art. 26 | Test bypass detection | HIGH |
| INF-THR-09 | UC-AI-03 (FRIA) + AI Act Art. 27 | AI model adversarial input | MEDIUM |
| INF-THR-10 | Cross-package: DSAR + AI processing | AI-driven data subject identification | HIGH |

### 6.3 Case 03 Examples

| Inference ID | Source pattern | Inferred threat | Confidence |
|--------------|---------------|-----------------|------------|
| INF-THR-11 | NODE-SYS-005 (HSM) + STRIDE-T | Key extraction via side channel | MEDIUM |
| INF-THR-12 | DORA Art. 28 + 3rd party provider | Third-party ICT risk cascade | HIGH |
| INF-THR-13 | UC-32 (Regulatory Notification) + 4h deadline | Notification race condition | MEDIUM |
| INF-THR-14 | Cross-border data + DORA Art. 26 | Cross-jurisdiction enforcement gap | MEDIUM |
| INF-THR-15 | AI model (credit scoring) + GDPR | Automated discrimination | HIGH |

---

## 7. Threat Scaling Analysis

How threat counts scale with company complexity:

| Metric | Formula | Case 01 (2 regs) | Case 02 (4 regs) | Case 03 (5 regs) | Growth Pattern |
|--------|---------|-------------------|-------------------|-------------------|----------------|
| Assets | f(architecture) | 10 | 15 | 20 | Linear with node count |
| STRIDE threats | UCs × 6 × coverage_rate | ~30 | ~40 | ~38 | Linear with UC count |
| LINDDUN threats | privacy_UCs × 7 | 7 | 7 | 7 | Constant (GDPR-bound) |
| Total threats | STRIDE + LINDDUN + KG | ~38 | ~50+ | ~50+ | Sub-linear (plateaus) |
| Risks | threats × risk_emergence_rate | 10 | 15 | 12 | Sub-linear |
| HIGH/CRITICAL risks | risks × severity_rate | 7 (70%) | 10 (67%) | 8 (67%) | Constant ratio (~65-70%) |
| Mitigations | HIGH_risks × 1.0 | 8 | 12 | 10 | Linear with HIGH risks |
| KG inferences | f(KG_coverage) | 15 | 24 | 21 | Sub-linear |
| Feedback iterations | f(mitigations × new_UCs) | 1-2 | 2-3 | 2-3 | Logarithmic |
| New UCs from mitigations | f(mitigations) | 3 | 5 | 4 | Linear with mitigations |
| Coverage % | covered / total | 100% | 90% | 92% | High (with feedback) |

**Key insight:** Threat modeling converges: with the feedback loop, coverage reaches near-100% regardless of case complexity. The non-monotonic insight is that Case 02 has MORE HIGH risks than Case 03 (more regulations = more overlap opportunities), but Case 03's DORA-specific controls pre-empt several threat scenarios.

---

## Summary: How to Use This File

| If you need to... | Read this section |
|---|---|
| Identify typical threats for a UC type | §1 — STRIDE Pattern Catalog |
| Identify privacy threats for a data type | §2 — LINDDUN Pattern Catalog |
| Score a risk (likelihood × impact) | §3 — Risk Matrix Reference |
| Map a mitigation to D3FEND | §4 — D3FEND Mapping Catalog |
| Select the right mitigation strategy | §5 — Mitigation Strategy Selection Guide |
| Find KG inference examples | §6 — KG Inference Examples |
| Estimate threat counts for a new case | §7 — Threat Scaling Analysis |

---

**See also:**
- [`phase3c_threat_modeling.md`](phase3c_threat_modeling.md) — Flow diagrams (companion)
- [`../phase3_risk_analysis.md`](../phase3_risk_analysis.md) — Phase 3C overview (parent)
- [`../../Class_Models/phase3_risk_analysis.md`](../../Class_Models/phase3_risk_analysis.md) — Static structure
- [`../../../TEMPLATES/25_Risk_Analysis.md`](../../../TEMPLATES/25_Risk_Analysis.md) — Doc 25 template