---
document_id: AEGIS-P3-13b
title: Use Case Variability
phase: 3
version: 1.1
created: 2026-04-28
updated: 2026-09-05
author: Compliance Lead
status: DRAFT
inputs: [13_Use_Cases_Catalog.md, 13a_Use_Case_Relationships.md, 11_Rules_Catalog.md]
outputs: [14_Architectural_Nodes.md, 15_Requirements_Allocation.md]
traceability: AEGIS Class Model → UseCase, VariabilityType, Regulation, Specialization classes
related_documents: 13_Use_Cases_Catalog.md, 13a_Use_Case_Relationships.md
case_id: CASE-03-OMNIBANK
case: Case_03_OmniBank_Financial
complexity: Maximum (5 regulations, 38 sub-domains, 93 use cases)
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
| **Specialization** | `«specialization»` | Regulation-specific version of a base UC | PROC-15-DORA vs PROC-15-GDPR vs PROC-15-NIS2 vs PROC-15-CRA vs PROC-15-AI Act |
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
| PROC-15-GDPR | GDPR Art. 33/34 | Lead DPA (BfDI) | 72 hours | Supervisory authority notification for breaches likely to result in risk |
| PROC-15-CRA | CRA Art. 14 | ENISA + downstream users | 24 hours | Product security incident notification for products with digital components |
| PROC-15-NIS2 | NIS 2 Art. 23 | National CSIRT (BSI) | 24 hours | Significant incident notification for essential entities |
| PROC-15-DORA | DORA Art. 14 | Lead OCEsG/Competent Authority | 4h initial, 72h follow-up | ICT-related incident notification for financial entities |
| PROC-15-AI | AI Act Art. 73 | Market surveillance authority | 15 days | Incident involving high-risk AI systems Annex III |

**Activation Condition:** `regulation.trigger = 'GDPR' AND incident.type = 'personal_data_breach'` → PROC-15-GDPR

**Selection Matrix:**

| Condition | UC Selected |
|-----------|-------------|
| GDPR Art.33 breach + risk to rights | PROC-15-GDPR |
| CRA product incident + digital component | PROC-15-CRA |
| NIS 2 significant incident | PROC-15-NIS2 |
| DORA ICT incident + financial impact | PROC-15-DORA |
| AI Act high-risk AI system incident | PROC-15-AI |
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
| CAP-05-DORA | DORA Art. 6 | ICT risk management framework integrated with ISMS |
| CAP-05-ISO | ISO 27001:2022 | ISMS certification requirements |

**Activation Condition:** `regulation = 'DORA' AND entity.type = 'financial_entity'` → CAP-05-DORA

---

### 4.5 Secure Development — Secure-by-Design (PROC-28)

**Base UC:** PROC-28: Software Development Manager Implements Secure-by-Design

**Specializations:**

| Specialization | Triggering Regulation | Specific Requirements |
|----------------|----------------------|---------------------|
| PROC-28-CRA | CRA Art. 13 | Security-by-default for products with digital components (higher bar) |
| PROC-28-GDPR | GDPR Art. 25 | Privacy by design and default (lower bar than CRA) |

**Resolution:** T-004 — Follow CRA secure-by-default (higher bar) satisfies GDPR privacy by design (lower bar).

---

### 4.6 Supply Chain — ICT Provider Assessment (PROC-24)

**Base UC:** PROC-24: Vendor Risk Manager Assesses ICT Third-Party Provider

**Specializations:**

| Specialization | Triggering Regulation | Specific Requirements |
|----------------|----------------------|---------------------|
| PROC-24-DORA | DORA RTS on TLPT | ICT third-party risk concentration assessment |
| PROC-24-NIS2 | NIS 2 Art. 21 | Security measures for supply chain relationships |

---

### 4.7 Human Factors — Security Competence (CAP-04)

**Base UC:** CAP-04: HR Manager Maintains Security Competence Program

**Specializations:**

| Specialization | Triggering Regulation | Specific Requirements |
|----------------|----------------------|---------------------|
| CAP-04-AI | AI Act Art. 14 | Human oversight competence for high-risk AI decisions |
| CAP-04-NIS2 | NIS 2 Art. 20 | Security training for essential entity personnel |

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
| Standard Retention (5 years) | No regulatory extension required | PROC-21-Standard |
| Extended Financial Retention (10 years) | MiFID II financial instruments apply | PROC-21-Financial |

**Selection Criteria:** `data.type = 'financial_instrument' AND regulation = 'MiFID II'` → PROC-21-Financial

### 5.3 Incident Response — AI Anomaly Investigation

**Base UC Options:**

| Option | When Selected | UC ID |
|--------|--------------|-------|
| Automated AI Anomaly Detection | AI monitoring systems operational | PROC-13-Auto |
| Manual AI Anomaly Investigation | Monitoring systems unavailable or anomaly unclear | PROC-13-Manual |

**Selection Criteria:** `monitoring.system.available = TRUE AND anomaly.confidence >= 0.8` → PROC-13-Auto

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
| Online Training Delivery | Employee location prevents classroom; scale requirement | PROC-31-Online |
| Classroom Training | Employee available for in-person; better engagement | PROC-31-Classroom |

**Selection Criteria:** `employee.location.remote = TRUE OR employee.count > 1000` → PROC-31-Online

### 5.6 Penetration Testing — Tester Selection

**Base UC Options:**

| Option | When Selected | UC ID |
|--------|--------------|-------|
| Internal Pentest | Regular testing; resource available; no regulatory requirement | PROC-36-Internal |
| External Pentest | Independent verification required; regulatory examination | PROC-36-External |

**Selection Criteria:** `verification.required = 'independent' OR regulatory.examination = TRUE` → PROC-36-External

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

## 7A. LANE VARIANTS

> Additive section (v1.1) — anchors channel and lifecycle variability to the re-laned ids
> of `LANE_NAMING_CENSUS_v0` (Case_03: T46/P40/C7). Regulation specializations remain in §4;
> this section covers operational variants within a single lane id.

### 7A.1 Channel Variants — PROC-01 (Data Subject Requests Data Encryption Status)

| Variant | Channel | Selection Criteria (per Doc22 §4.1 / Doc32 PROC-01 card) |
|---------|---------|----------------------------------------------------------|
| PROC-01-Branch | Branch desk, escalated to Security Administrator | Request filed in person; identity proven face-to-face |
| PROC-01-App | Self-service in SYS-02 mobile app | Authenticated customer; SCA-bound session |
| PROC-01-RM | Relationship manager via SYS-17 CRM | Affluent/corporate customer with assigned RM |

### 7A.2 Lifecycle Variants — PROC-10 (Provision User Identity)

| Variant | Lifecycle Event | Selection Criteria (per Doc32 PROC-10 card) |
|---------|-----------------|---------------------------------------------|
| PROC-10-Joiner | Joiner: full provisioning + baseline entitlements | New HR record with start date |
| PROC-10-Mover | Mover: entitlement delta, revoke-then-grant | Department/role change event |
| PROC-10-Leaver | Leaver: same-day deprovisioning (feeds PROC-13) | Termination event; audit evidence retained |

### 7A.3 Enforcement Path Variants — PROC-21 (Enforce Tiered Data Retention)

| Variant | Retention Path | Selection Criteria (per Doc22 §4.5) |
|---------|----------------|-------------------------------------|
| PROC-21-Standard | Standard retention path (5 years) | No regulatory extension required |
| PROC-21-Financial | Extended financial retention path (10 years) | MiFID II financial instruments apply (see §5.2) |

### 7A.4 Product Variants (PKG-A..F, per Doc22 §6B)

| Variant pair | Difference | Selection Criteria |
|--------------|------------|--------------------|
| UC-70 (retail) vs UC-86 (corporate) onboarding | Retail: remote eIDAS identity verification in-app (UC-69 step 3, §6B.2); Corporate: delegated-user model with SYS-21, joiner/mover/leaver for delegated users (§6B.5) | Customer segment = retail vs corporate |
| UC-77 regular vs UC-77 instant | Same SEPA use case; instant leg adds scheme deadline and immediate availability checks (§6B.3) | Customer selects instant transfer option |
| UC-78 (in-app) vs UC-91 (contact centre) card block | Alternative blocking channels: self-service in-app vs SYS-20 contact centre with recorded call (§6B.3 / §6B.6) | Channel availability and customer preference |
| UC-90 (in-app) vs UC-91 (voice) fraud response | Fraud alert confirm/deny pushed in-app vs confirmed via contact-centre call (§6B.6) | Alert channel reachable; SYS-11 routing |

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
| 1.1 | 2026-09-05 | Compliance Lead | Lane census alignment: stray pre-rename UC ids → PROC/CAP; §7A Lane Variants added (PROC-01, PROC-10, PROC-21, product variants per Doc22 §6B) |

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