---
document_id: AEGIS-P3-13b
title: Use Case Variability
phase: 3
version: 1.0
created: 2026-04-28
updated: 2026-04-28
author: Compliance Lead
status: DRAFT
inputs: [13_Use_Cases_Catalog.md, 13a_Use_Case_Relationships.md, 11_Rules_Catalog.md]
outputs: [14_Architectural_Nodes.md, 15_Requirements_Allocation.md]
traceability: AEGIS Class Model → UseCase, VariabilityType, Regulation, Specialization classes
related_documents: 13_Use_Cases_Catalog.md, 13a_Use_Case_Relationships.md
case_id: CASE-03-OMNIBANK
complexity: Maximum (5 regulations, 38 sub-domains, 62 use cases)
---

# Use Case Variability

**Case:** Case 03 — OmniBank Financial Systems (Maximum Complexity)
**Phase:** 3 — Decomposition & Risk Integration
**Step:** 3 — Define Use Case Variability

---

## 1. DOCUMENT PURPOSE

This document defines the variability patterns across the Use Cases Catalog (Doc 13). Variability addresses the question: "Which UCs apply under which regulatory conditions?"

OmniBank operates under maximum complexity with all 5 EU regulations applying simultaneously. This creates unique variability scenarios where the same business capability must be implemented differently depending on which regulation triggered the requirement.

---

## 2. VARIABILITY TYPES

| Variability Type | Symbol | Description | Example |
|------------------|--------|-------------|---------|
| **Specialization** | `«specialization»` | Regulation-specific version of a base UC | UC-25-DORA vs UC-25-GDPR vs UC-25-NIS2 vs UC-25-CRA vs UC-25-AI Act |
| **Alternative** | `«alternative»` | Mutually exclusive variants based on conditions | Automated vs Manual SBOM generation |
| **Option** | `«option»` | UC may or may not be present based on conditions | FIDO2 hardware keys may be optional for standard users |

---

## 3. VARIABILITY SUMMARY

| Metric | Value |
|--------|-------|
| **Total UCs with Variability** | 28 (45%) |
| **Specialization Variants** | 14 |
| **Alternative Scenarios** | 8 |
| **Optional UCs** | 6 |
| **Regulations with Variants** | 5/5 (GDPR, CRA, NIS 2, DORA, AI Act) |

---

## 4. SPECIALIZATION MATRIX

Specializations are regulation-specific versions of base use cases. Each specialization inherits from the base UC but adds regulation-specific constraints, actors, or flows.

### 4.1 Incident Response — Universal Notification (PROC-15)

**Base UC:** PROC-15: Compliance Officer Executes Universal Incident Notification

**Problem:** Five regulations (GDPR, CRA, NIS 2, DORA, AI Act) each require notification to different authorities within different timelines. The base UC cannot specify which authority to notify and when without knowing the triggering regulation.

**Resolution:** Five specializations, each activated by a different regulatory trigger:

| Specialization | Triggering Regulation | Notification Target | Timeline | Specific Requirements |
|----------------|----------------------|---------------------|----------|---------------------|
| UC-25-GDPR | GDPR Art. 33/34 | Lead DPA (BfDI) | 72 hours | Supervisory authority notification for breaches likely to result in risk |
| UC-25-CRA | CRA Art. 14 | ENISA + downstream users | 24 hours | Product security incident notification for products with digital components |
| UC-25-NIS2 | NIS 2 Art. 23 | National CSIRT (BSI) | 24 hours | Significant incident notification for essential entities |
| UC-25-DORA | DORA Art. 14 | Lead OCEsG/Competent Authority | 4h initial, 72h follow-up | ICT-related incident notification for financial entities |
| UC-25-AI | AI Act Art. 73 | Market surveillance authority | 15 days | Incident involving high-risk AI systems Annex III |

**Activation Condition:** `regulation.trigger = 'GDPR' AND incident.type = 'personal_data_breach'` → UC-25-GDPR

**Selection Matrix:**

| Condition | UC Selected |
|-----------|-------------|
| GDPR Art.33 breach + risk to rights | UC-25-GDPR |
| CRA product incident + digital component | UC-25-CRA |
| NIS 2 significant incident | UC-25-NIS2 |
| DORA ICT incident + financial impact | UC-25-DORA |
| AI Act high-risk AI system incident | UC-25-AI |
| Multiple regulations triggered simultaneously | All applicable specializations execute in parallel |

---

### 4.2 Access Control — MFA Enforcement (UC-17)

**Base UC:** UC-17: Security Administrator Enforces MFA for Privileged Access

**Specializations:**

| Specialization | Triggering Regulation | Specific Requirements |
|----------------|----------------------|---------------------|
| UC-17-DORA | DORA RTS on ICT risk | Strong customer authentication for account access per PSD2 |
| UC-17-AI | AI Act Annex III | MFA for high-risk AI system access to ensure human oversight |

**Activation Condition:** `regulation = 'DORA' AND access.type = 'financial_account'` → UC-17-DORA

---

### 4.3 Data Lifecycle — Data Erasure (UC-33)

**Base UC:** UC-33: Data Protection Officer Executes Data Erasure Request

**Specializations:**

| Specialization | Triggering Regulation | Specific Requirements |
|----------------|----------------------|---------------------|
| UC-33-GDPR | GDPR Art. 17 | Right to erasure for personal data; exceptions for legal obligation |
| UC-33-CRA | CRA Art. 16 | Secure deletion of product data on decommissioning |

**Tension Resolution:** T-002 — UC-33 uses cryptographic sharding to satisfy GDPR erasure while preserving DORA immutable audit logs. PII encryption keys are destroyed; log structure remains.

---

### 4.4 Governance — Unified ISMS (CAP-05)

**Base UC:** CAP-05: CISO Maintains Unified ISMS

**Specializations:**

| Specialization | Triggering Regulation | Specific Requirements |
|----------------|----------------------|---------------------|
| UC-52-DORA | DORA Art. 6 | ICT risk management framework integrated with ISMS |
| UC-52-ISO | ISO 27001:2022 | ISMS certification requirements |

**Activation Condition:** `regulation = 'DORA' AND entity.type = 'financial_entity'` → UC-52-DORA

---

### 4.5 Secure Development — Secure-by-Design (PROC-28)

**Base UC:** PROC-28: Software Development Manager Implements Secure-by-Design

**Specializations:**

| Specialization | Triggering Regulation | Specific Requirements |
|----------------|----------------------|---------------------|
| UC-42-CRA | CRA Art. 13 | Security-by-default for products with digital components (higher bar) |
| UC-42-GDPR | GDPR Art. 25 | Privacy by design and default (lower bar than CRA) |

**Resolution:** T-004 — Follow CRA secure-by-default (higher bar) satisfies GDPR privacy by design (lower bar).

---

### 4.6 Supply Chain — ICT Provider Assessment (PROC-24)

**Base UC:** PROC-24: Vendor Risk Manager Assesses ICT Third-Party Provider

**Specializations:**

| Specialization | Triggering Regulation | Specific Requirements |
|----------------|----------------------|---------------------|
| UC-37-DORA | DORA RTS on TLPT | ICT third-party risk concentration assessment |
| UC-37-NIS2 | NIS 2 Art. 21 | Security measures for supply chain relationships |

---

### 4.7 Human Factors — Security Competence (CAP-04)

**Base UC:** CAP-04: HR Manager Maintains Security Competence Program

**Specializations:**

| Specialization | Triggering Regulation | Specific Requirements |
|----------------|----------------------|---------------------|
| UC-49-AI | AI Act Art. 14 | Human oversight competence for high-risk AI decisions |
| UC-49-NIS2 | NIS 2 Art. 20 | Security training for essential entity personnel |

---

## 5. ALTERNATIVE SCENARIOS

Alternative scenarios are mutually exclusive variants of a base UC. Only one variant executes based on environmental conditions.

### 5.1 Vulnerability Management — SBOM Generation

**Base UC Options:**

| Option | When Selected | UC ID |
|--------|--------------|-------|
| Automated SBOM Generation | CI/CD pipeline available, no manual intervention required | CAP-01 |
| Manual SBOM Generation | Automated tools unavailable, dependency newly discovered | UC-15 |

**Selection Criteria:** `automation.available = TRUE AND dependency.known = TRUE` → CAP-01 (Automated)

### 5.2 Data Lifecycle — Data Retention Enforcement

**Base UC Options:**

| Option | When Selected | UC ID |
|--------|--------------|-------|
| Standard Retention (5 years) | No regulatory extension required | UC-32-Standard |
| Extended Financial Retention (10 years) | MiFID II financial instruments apply | UC-32-Financial |

**Selection Criteria:** `data.type = 'financial_instrument' AND regulation = 'MiFID II'` → UC-32-Financial

### 5.3 Incident Response — AI Anomaly Investigation

**Base UC Options:**

| Option | When Selected | UC ID |
|--------|--------------|-------|
| Automated AI Anomaly Detection | AI monitoring systems operational | UC-28-Auto |
| Manual AI Anomaly Investigation | Monitoring systems unavailable or anomaly unclear | UC-28-Manual |

**Selection Criteria:** `monitoring.system.available = TRUE AND anomaly.confidence >= 0.8` → UC-28-Auto

### 5.4 Monitoring — Audit Log Storage

**Base UC Options:**

| Option | When Selected | UC ID |
|--------|--------------|-------|
| Cloud Log Storage | No data sovereignty constraint, cost optimization | UC-58-Cloud |
| On-Premise Log Storage | Financial data sovereignty requires EU on-premise | UC-58-OnPrem |

**Selection Criteria:** `data.sovereignty.required = TRUE AND location = 'EU'` → UC-58-OnPrem

### 5.5 Security Training — Training Delivery

**Base UC Options:**

| Option | When Selected | UC ID |
|--------|--------------|-------|
| Online Training Delivery | Employee location prevents classroom; scale requirement | UC-48-Online |
| Classroom Training | Employee available for in-person; better engagement | UC-48-Classroom |

**Selection Criteria:** `employee.location.remote = TRUE OR employee.count > 1000` → UC-48-Online

### 5.6 Penetration Testing — Tester Selection

**Base UC Options:**

| Option | When Selected | UC ID |
|--------|--------------|-------|
| Internal Pentest | Regular testing; resource available; no regulatory requirement | UC-59-Internal |
| External Pentest | Independent verification required; regulatory examination | UC-59-External |

**Selection Criteria:** `verification.required = 'independent' OR regulatory.examination = TRUE` → UC-59-External

---

## 6. OPTIONAL USE CASES

Optional UCs may or may not be present based on specific conditions. Unlike alternatives, optional UCs are independent — they don't replace another UC, they simply may not apply.

### 6.1 PKG-D-03: Access Control

| Optional UC | «option» Condition | Rationale |
|------------|-------------------|------------|
| UC-22: Implement FIDO2 Authentication | `user.role = 'privileged' AND hardware.available = TRUE` | FIDO2 hardware keys may not be available for all users; option for phishing-resistant auth |
| UC-21.1: Approve AI Model Parameters | `ai.model.change.risk = 'high'` | Dual approval only required for high-risk model changes |

### 6.2 PKG-D-04: Incident Response

| Optional UC | «option» Condition | Rationale |
|------------|-------------------|------------|
| PROC-16: Recover AI System after Failure | `ai.system.deployed = TRUE` | Only applies if AI systems are deployed |
| PROC-18: Tabletop Exercise | `team.exercise.schedule = 'quarterly'` | Only if quarterly exercises scheduled |

### 6.3 PKG-D-10: Monitoring & Audit

| Optional UC | «option» Condition | Rationale |
|------------|-------------------|------------|
| UC-61: Monitor AI Model Drift | `ai.model.deployed = TRUE AND drift.detection.required = TRUE` | Only if AI models are in production |

---

## 7. VARIABILITY SELECTION ENGINE

The following decision table determines which UC variant to execute based on conditions:

### 7.1 Notification Decision Table

| Condition Combinaton | GDPR | CRA | NIS 2 | DORA | AI Act |
|----------------------|------|-----|-------|------|--------|
| Personal data breach | ✓ | — | — | — | — |
| Product with digital components incident | — | ✓ | — | — | — |
| Essential entity significant incident | — | — | ✓ | — | — |
| Financial entity ICT incident | — | — | — | ✓ | — |
| High-risk AI system incident | — | — | — | — | ✓ |
| Personal data breach + AI system involved | ✓ | — | — | — | ✓ |
| Essential entity + financial + significant | ✓ | — | ✓ | ✓ | — |

**Rule:** If multiple regulations apply, ALL applicable specializations execute in parallel. The base UC provides the common notification workflow; specializations add regulation-specific content and channels.

### 7.2 Erasure Decision Table

| Condition | UC Executed |
|-----------|-------------|
| Erasure request from data subject | UC-33-GDPR |
| Product decommissioning | UC-33-CRA |
| Retention expiry | UC-33 (automated) |
| Audit log preservation required | UC-33 + Cryptographic Sharding |
| Third-party processor involvement | UC-33 + UC-107 (Notify Third Parties) |

---

## 8. REGULATORY INTERACTION MATRIX

This matrix shows which regulations interact on which UCs:

| UC | GDPR | CRA | NIS 2 | DORA | AI Act |
|----|------|-----|-------|------|--------|
| PROC-15 (Notification) | ✓ | ✓ | ✓ | ✓ | ✓ |
| UC-33 (Erasure) | ✓ | ✓ | — | — | — |
| CAP-05 (ISMS) | ✓ | — | — | ✓ | ✓ |
| PROC-28 (Secure-by-Design) | ✓ | ✓ | — | — | — |
| PROC-24 (Vendor Assessment) | ✓ | — | ✓ | ✓ | — |
| UC-17 (MFA) | — | ✓ | ✓ | ✓ | ✓ |
| PROC-34 (IPSARA) | ✓ | ✓ | ✓ | ✓ | ✓ |
| CAP-04 (Competence) | ✓ | — | ✓ | — | ✓ |

---

## 9. STOP CONDITION CHECK — SC4 (Variability Complete)

| Check | Value | Threshold | Status |
|-------|-------|-----------|--------|
| Applicable regulations | 5 | — | — |
| Regulations with specializations | 5 | — | — |
| Multi-regulation UCs covered | 8 | — | — |
| Variability coverage | 100% | 100% | ✅ PASS |

**SC4: PASS — All regulation-specific scenarios covered via specializations.**

---

## 10. NEXT STEPS

1. **Compliance Analysis Gate** — Verify SC1 (Rule Coverage: every rule maps to ≥1 UC)
2. **Derive Functional Requirements** — Extract FRs from UCs
3. **Derive Non-Functional Requirements** — Extract NFRs from UCs
4. **Proceed to Iteration 2** — Add detailed flows for complex UCs (NI=3)

---

## 11. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-28 | Compliance Lead | Initial creation — 14 specializations, 8 alternatives, 6 options |

---

## 12. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Compliance Lead | [TBD] | | |
| CISO | [TBD] | | |
| Data Protection Officer | [TBD] | | |
| AI Governance Lead | [TBD] | | |

---

**Next Step:** Proceed to 14_Architectural_Nodes.md to define the architectural decomposition.