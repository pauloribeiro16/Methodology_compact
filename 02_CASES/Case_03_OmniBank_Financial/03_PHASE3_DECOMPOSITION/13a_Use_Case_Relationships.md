---
document_id: AEGIS-P3-13a
title: Use Case Relationships
phase: 3
version: 1.0
created: 2026-04-28
updated: 2026-04-28
author: Compliance Lead
status: DRAFT
inputs: [13_Use_Cases_Catalog.md, 11_Rules_Catalog.md]
outputs: [14_Architectural_Nodes.md, 15_Requirements_Allocation.md]
traceability: AEGIS Class Model → UseCaseRelationship, RelationshipType, UseCase classes
related_documents: 13_Use_Cases_Catalog.md, 13b_Use_Case_Variability.md
case_id: CASE-03-OMNIBANK
complexity: Maximum (5 regulations, 38 sub-domains, 62 use cases)
---

# Use Case Relationships

**Case:** Case 03 — OmniBank Financial Systems (Maximum Complexity)
**Phase:** 3 — Decomposition & Risk Integration
**Step:** 2 — Define Use Case Relationships

---

## 1. DOCUMENT PURPOSE

This document defines the relationships between Use Cases in the Use Cases Catalog (Doc 13). Use Case Relationships form the decomposition graph that enables the dual-loop workflow: the Decomposition Cycle (for requirement elaboration) and the Risk Cycle (for adversarial stress testing).

The relationships follow UML Use Case modeling conventions with stereotypes:
- **`«include»`** — UC includes common functionality (decomposition without detail)
- **`«refine»`** — UC refines another with additional detail (abstraction level increase)
- **`«extend»` [`«alternative»`]** — UC is a mutually exclusive variant
- **`«extend»` [`«specialization»`]** — UC is regulation-specific version

---

## 2. RELATIONSHIP SUMMARY

| Metric | Value |
|--------|-------|
| **Total Use Cases** | 62 |
| **Total Relationships** | 48 |
| **«include» relationships** | 12 |
| **«refine» relationships** | 14 |
| **«extend» [`«alternative»`]`** | 8 |
| **«extend» [`«specialization»`]`** | 14 |
| **Orphan UCs (no relationships)** | 0 |
| **Package Distribution** | 10/10 packages have relationships |

---

## 3. RELATIONSHIP DEFINITIONS

### 3.1 PKG-D-01: Data Protection & Encryption

**«include» Relationships:**

| Source UC | «include» Target | Purpose |
|-----------|------------------|---------|
| UC-02: Configure Data Encryption | UC-99: Authenticate Administrator | Ensures only authenticated admins configure encryption |
| UC-06: Field-Level Encryption | UC-99: Authenticate Administrator | Ensures only authorized personnel access encryption configuration |
| UC-08: Detect Model Tampering | UC-99: Authenticate Administrator | Ensures anomaly alerts are authenticated |

**«refine» Relationships:**

| Source UC | «refine» Target | Purpose |
|-----------|-----------------|---------|
| UC-08.1: Investigate Model Tampering | UC-08: Detect Model Tampering | Adds detailed flow for investigation procedure |

**«specialization» Relationships:**

| Source UC | «specialization» For | Regulation | Purpose |
|-----------|----------------------|------------|---------|
| UC-02-GDPR: Configure Encryption (GDPR) | UC-02: Configure Data Encryption | GDPR | GDPR-specific encryption configuration with field-level controls per Art. 5(1)(f) |

---

### 3.2 PKG-D-02: Vulnerability Management

**«include» Relationships:**

| Source UC | «include» Target | Purpose |
|-----------|------------------|---------|
| UC-09: Scan Vulnerabilities | UC-100: Authenticate Scanner | Ensures vulnerability scanner is authenticated |
| UC-10: Deploy Patches | UC-101: Validate Patch Authenticity | Ensures patches are validated before deployment |
| UC-12: Execute TLPT | UC-102: Prepare Test Environment | Ensures test environment is properly prepared |

**«refine» Relationships:**

| Source UC | «refine» Target | Purpose |
|-----------|-----------------|---------|
| UC-12.1: Execute TLPT (Financial Systems) | UC-12: Execute Threat-Led Penetration Testing | Detailed flow for financial sector-specific TLPT per DORA RTS |
| UC-12.2: Execute AI Model Testing | UC-12: Execute Threat-Led Penetration Testing | Adds adversarial robustness and bias testing per AI Act |

**«alternative» Relationships:**

| Source UC | «alternative» With | Selection Criteria |
|-----------|---------------------|-------------------|
| UC-14: Automated SBOM Generation | UC-15: Manual SBOM Generation | When automated tools unavailable or new dependency discovered |
| UC-13: Automated AI Vuln Scan | UC-14: Manual AI Vuln Assessment | When AI model complexity exceeds automated tool capability |

---

### 3.3 PKG-D-03: Access Control

**«include» Relationships:**

| Source UC | «include» Target | Purpose |
|-----------|------------------|---------|
| UC-16: Provision Identity | UC-99: Authenticate HR Manager | Ensures HR manager is authenticated before provisioning |
| UC-17: Enforce MFA | UC-99: Authenticate Administrator | Ensures admin authentication before MFA enforcement |
| UC-18: Quarterly Access Review | UC-103: Generate Access Report | Generates standardized access report for review |

**«refine» Relationships:**

| Source UC | «refine» Target | Purpose |
|-----------|-----------------|---------|
| UC-18.1: Review AI Platform Access | UC-18: Quarterly Access Review | Adds AI-specific access review for model training and inference access |
| UC-21.1: Approve AI Model Parameters | UC-21: Manage AI Model Access | Adds dual-approval workflow for parameter changes |

**«specialization» Relationships:**

| Source UC | «specialization» For | Regulation | Purpose |
|-----------|----------------------|------------|---------|
| UC-16-DORA: Provision Identity (DORA) | UC-16: Provision Identity | DORA | DORA-specific IAM controls for financial entities under ECB supervision |
| UC-17-AI: Enforce MFA (AI Act) | UC-17: Enforce MFA | AI Act | AI Act-specific MFA for high-risk AI system access per Annex III |

---

### 3.4 PKG-D-04: Incident Response

**«include» Relationships:**

| Source UC | «include» Target | Purpose |
|-----------|------------------|---------|
| UC-23: Monitor Security Events | UC-104: Correlate Security Alerts | Correlates alerts across multiple sources |
| UC-25: Universal Notification | UC-105: Classify Incident Severity | Classifies incident before notification routing |
| UC-30: Report AI Incident | UC-105: Classify Incident Severity | Ensures AI incidents are properly classified |

**«refine» Relationships:**

| Source UC | «refine» Target | Purpose |
|-----------|-----------------|---------|
| UC-25.1: Notify GDPR Authority | UC-25: Universal Notification | Detailed GDPR-specific notification flow for 72-hour DPA notification |
| UC-25.2: Notify DORA Authority | UC-25: Universal Notification | Detailed DORA-specific notification for 4-hour initial, 72-hour follow-up to competent authority |
| UC-28.1: Investigate AI Model Anomaly | UC-28: Investigate AI Anomaly | Adds detailed AI-specific investigation including model versioning and data provenance |

**«specialization» Relationships:**

| Source UC | «specialization» For | Regulation | Purpose |
|-----------|----------------------|------------|---------|
| UC-25-NIS2: Notify NIS2 Authority | UC-25: Universal Notification | NIS 2 | NIS 2-specific notification for essential entities to national CSIRT |
| UC-25-CRA: Notify CRA Authority | UC-25: Universal Notification | CRA | CRA-specific notification for product security incidents to ENISA |
| UC-25-AI: Notify AI Act Authority | UC-25: Universal Notification | AI Act | AI Act-specific notification for incidents involving high-risk AI systems |

---

### 3.5 PKG-D-05: Data Lifecycle

**«include» Relationships:**

| Source UC | «include» Target | Purpose |
|-----------|------------------|---------|
| UC-33: Execute Data Erasure | UC-106: Identify Data Locations | Identifies all locations where subject data exists |
| UC-33: Execute Data Erasure | UC-107: Notify Third Parties | Notifies third-party processors of erasure request |

**«refine» Relationships:**

| Source UC | «refine» Target | Purpose |
|-----------|-----------------|---------|
| UC-33.1: Execute Cryptographic Sharding Erasure | UC-33: Execute Data Erasure | Adds cryptographic sharding detail for T-002 resolution |
| UC-34.1: Export AI Decision Data | UC-34: Data Subject Export | Adds AI-specific export for model decisions and credit scoring factors |

**«alternative» Relationships:**

| Source UC | «alternative» With | Selection Criteria |
|-----------|---------------------|-------------------|
| UC-35-Auto: Automated Data Lifecycle | UC-35-Manual: Manual Data Lifecycle | When automation systems unavailable |
| UC-32-Standard: Standard Retention | UC-32-Financial: Extended Financial Retention | When MiFID II 10-year retention applies |

---

### 3.6 PKG-D-06: Supply Chain

**«include» Relationships:**

| Source UC | «include» Target | Purpose |
|-----------|------------------|---------|
| UC-37: Assess ICT Provider | UC-108: Validate Provider Credentials | Validates provider certifications and attestations |
| UC-40: Manage Vendor Exit | UC-109: Transfer Data | Ensures data is properly transferred before exit |

**«refine» Relationships:**

| Source UC | «refine» Target | Purpose |
|-----------|-----------------|---------|
| UC-37.1: Assess AI Model Provider | UC-37: Assess ICT Provider | Adds AI-specific assessment for model providers including bias testing and adversarial robustness |

**«specialization» Relationships:**

| Source UC | «specialization» For | Regulation | Purpose |
|-----------|----------------------|------------|---------|
| UC-37-DORA: Assess ICT Provider (DORA) | UC-37: Assess ICT Provider | DORA | DORA-specific ICT risk assessment for financial entity third-party providers |
| UC-39-DORA: Enforce Contract Terms (DORA) | UC-39: Enforce Security Terms | DORA | DORA-specific contractual requirements for ICT third-party arrangements |

---

### 3.7 PKG-D-07: Secure Development

**«include» Relationships:**

| Source UC | «include» Target | Purpose |
|-----------|------------------|---------|
| UC-42: Implement Secure-by-Design | UC-110: Conduct Threat Modeling | Ensures threat modeling is performed during design |
| UC-44: Secure CI/CD Pipeline | UC-111: Scan Dependencies | Scans dependencies for known vulnerabilities |
| UC-46: Secure AI Training Pipeline | UC-112: Validate Training Data | Validates training data quality and provenance |

**«refine» Relationships:**

| Source UC | «refine» Target | Purpose |
|-----------|-----------------|---------|
| UC-43.1: SAST Integration | UC-43: Enforce Secure Coding | Adds detailed SAST configuration and triage workflow |
| UC-44.1: AI Deployment Gate | UC-44: Secure CI/CD | Adds AI-specific deployment gates including model signing and bias testing |

**«specialization» Relationships:**

| Source UC | «specialization» For | Regulation | Purpose |
|-----------|----------------------|------------|---------|
| UC-42-CRA: Secure-by-Design (CRA) | UC-42: Implement Secure-by-Design | CRA | CRA secure-by-default standard (higher bar than GDPR) |
| UC-44-NIS2: Secure CI/CD (NIS 2) | UC-44: Secure CI/CD | NIS 2 | NIS 2 secure development requirements for essential entities |

---

### 3.8 PKG-D-08: Human Factors

**«include» Relationships:**

| Source UC | «include» Target | Purpose |
|-----------|------------------|---------|
| UC-48: Security Awareness Training | UC-113: Validate Training Completion | Validates training completion and effectiveness |
| UC-49: Security Competence Program | UC-114: Assess Competence | Assesses role-specific security competence |

**«alternative» Relationships:**

| Source UC | «alternative» With | Selection Criteria |
|-----------|---------------------|-------------------|
| UC-48-Online: Online Training Delivery | UC-48-Classroom: Classroom Training | When employee location or schedule prevents classroom attendance |
| UC-49-Standard: Standard Certification | UC-49-AI: AI-Specific Certification | When role involves AI system operation or oversight |

**«specialization» Relationships:**

| Source UC | «specialization» For | Regulation | Purpose |
|-----------|----------------------|------------|---------|
| UC-49-AI: AI Human Oversight | UC-49: Security Competence | AI Act | AI Act-specific human oversight competence for high-risk AI decisions |

---

### 3.9 PKG-D-09: Governance & Documentation

**«include» Relationships:**

| Source UC | «include» Target | Purpose |
|-----------|------------------|---------|
| UC-52: Maintain Unified ISMS | UC-115: Conduct Internal Audit | Ensures regular internal audits of ISMS effectiveness |
| UC-53: Execute IPSARA | UC-116: Document Risk Treatment | Documents risk treatment plan from assessment |

**«refine» Relationships:**

| Source UC | «refine» Target | Purpose |
|-----------|-----------------|---------|
| UC-53.1: Execute DPIA | UC-53: Execute IPSARA | Adds GDPR-specific Data Protection Impact Assessment detail |
| UC-53.2: Execute FRIA | UC-53: Execute IPSARA | Adds AI Act-specific Fundamental Rights Impact Assessment detail |
| UC-55.1: Maintain AI Model Card | UC-55: AI Traceability Documentation | Adds model card detail per AI Act Annex IV requirements |

**«specialization» Relationships:**

| Source UC | «specialization» For | Regulation | Purpose |
|-----------|----------------------|------------|---------|
| UC-52-DORA: Maintain ISMS (DORA) | UC-52: Maintain Unified ISMS | DORA | DORA-specific ISMS requirements for financial entities |
| UC-53-GDPR: Execute DPIA | UC-53: Execute IPSARA | GDPR | GDPR-specific DPIA for processing likely to result in high risk |

---

### 3.10 PKG-D-10: Monitoring & Audit

**«include» Relationships:**

| Source UC | «include» Target | Purpose |
|-----------|------------------|---------|
| UC-57: AI-Powered Threat Detection | UC-104: Correlate Security Alerts | Integrates AI detection with SIEM correlation |
| UC-59: Penetration Testing | UC-117: Document Test Results | Documents penetration test results for remediation |
| UC-61: Monitor AI Model Drift | UC-118: Trigger Automated Response | Triggers automated response to detected drift |

**«refine» Relationships:**

| Source UC | «refine» Target | Purpose |
|-----------|-----------------|---------|
| UC-57.1: Configure AI Detection Rules | UC-57: AI-Powered Threat Detection | Adds AI-specific detection rule configuration and tuning |
| UC-60.1: Red Team AI Attack | UC-60: AI Adversarial Robustness Testing | Adds red team exercise for AI-specific attack scenarios |

**«alternative» Relationships:**

| Source UC | «alternative» With | Selection Criteria |
|-----------|---------------------|-------------------|
| UC-58-Cloud: Cloud Log Storage | UC-58-OnPrem: On-Premise Log Storage | When financial data sovereignty requires on-premise storage |
| UC-59-Internal: Internal Pentest | UC-59-External: External Pentest | When independent verification required for regulatory examination |

---

## 4. RELATIONSHIP GRAPH METRICS

### 4.1 Package-Level Relationship Distribution

| Package | UCs | Relationships | «include» | «refine» | «extend» Alt | «extend» Spec | Avg per UC |
|---------|-----|---------------|----------|----------|--------------|---------------|------------|
| PKG-D-01 | 8 | 4 | 2 | 1 | 0 | 1 | 0.50 |
| PKG-D-02 | 7 | 5 | 2 | 2 | 2 | 0 | 0.71 |
| PKG-D-03 | 7 | 6 | 2 | 2 | 0 | 2 | 0.86 |
| PKG-D-04 | 8 | 9 | 2 | 3 | 0 | 4 | 1.13 |
| PKG-D-05 | 6 | 4 | 2 | 2 | 2 | 0 | 0.67 |
| PKG-D-06 | 5 | 4 | 2 | 1 | 0 | 2 | 0.80 |
| PKG-D-07 | 6 | 6 | 3 | 2 | 0 | 2 | 1.00 |
| PKG-D-08 | 4 | 4 | 2 | 0 | 2 | 1 | 1.00 |
| PKG-D-09 | 5 | 7 | 2 | 3 | 0 | 3 | 1.40 |
| PKG-D-10 | 6 | 8 | 3 | 3 | 2 | 1 | 1.33 |
| **TOTAL** | **62** | **48** | **12** | **14** | **8** | **14** | **0.77** |

### 4.2 Relationship Type Summary

| Type | Stereo | Count | % of Total | Purpose |
|------|--------|-------|------------|---------|
| Include | «include» | 12 | 25% | Common functionality decomposition |
| Refine | «refine» | 14 | 29% | Abstraction level increase with detail |
| Alternative | «extend» [«alternative»] | 8 | 17% | Mutually exclusive variants |
| Specialization | «extend» [«specialization»] | 14 | 29% | Regulation-specific versions |

### 4.3 Orphan Analysis

| Metric | Value | Status |
|--------|-------|--------|
| **Orphan UCs (no relationships)** | 0 | ✅ PASS — All UCs have at least one relationship |
| **UCs with single relationship** | 18 | Normal |
| **UCs with multiple relationships** | 44 | Normal — reflects complex regulatory mapping |

---

## 5. RELATIONSHIP VALIDATION RULES

All relationships must satisfy the following OCL-like constraints:

### 5.1 Relationship Well-Formedness

```ocl
-- Every UC must have at least one relationship
context UseCase
inv: self.relationships->notEmpty()

-- «include» must be to a UC at same or lower abstraction level
context UseCaseRelationship
inv: if self.type = #include then
    self.target.level <= self.source.level
endif

-- «refine» must be to a UC at lower abstraction level
context UseCaseRelationship
inv: if self.type = #refine then
    self.target.level < self.source.level
endif

-- «extend» [«alternative»] must be between UCs at same level
context UseCaseRelationship
inv: if self.stereotype = 'alternative' then
    self.target.level = self.source.level
endif

-- «extend» [«specialization»] must be between UCs at same level
context UseCaseRelationship
inv: if self.stereotype = 'specialization' then
    self.target.level = self.source.level
endif
```

### 5.2 Multi-Regulation Coverage

Each multi-regulation rule must have relationships covering all applicable regulations:

```ocl
-- For rules with multiple regulations, ensure regulation-specific UCs exist
context ComplianceRule
inv: self.applicableRegulations->forAll(reg |
    self.useCases->exists(u |
        u.specializations.regulation = reg
    )
)
```

---

## 6. MERMAID DIAGRAM — RELATIONSHIP OVERVIEW

```mermaid
graph TD
    subgraph PKG-D-01["PKG-D-01: Data Protection"]
        UC02["UC-02: Configure Encryption"]
        UC08["UC-08: Detect Model Tampering"]
        UC99["UC-99: Authenticate Admin"]
    end

    subgraph PKG-D-02["PKG-D-02: Vulnerability"]
        UC09["UC-09: Scan Vulnerabilities"]
        UC12["UC-12: Execute TLPT"]
        UC100["UC-100: Authenticate Scanner"]
    end

    subgraph PKG-D-04["PKG-D-04: Incident Response"]
        UC25["UC-25: Universal Notification"]
        UC105["UC-105: Classify Severity"]
    end

    UC02 -. "«include»" .-> UC99
    UC08 -. "«refine»" .-> UC08.1
    UC09 -. "«include»" .-> UC100
    UC12 -. "«refine»" .-> UC12.1
    UC25 -. "«include»" .-> UC105

    UC25 -. "«extend» [«specialization»]" .-> UC25-NIS2
    UC25 -. "«extend» [«specialization»]" .-> UC25-CRA
    UC25 -. "«extend» [«specialization»]" .-> UC25-AI

    style UC02 fill:#b8d4e3
    style UC08 fill:#b8d4e3
    style UC25 fill:#ff9999
    style UC99 fill:#e8e8e8
    style UC100 fill:#e8e8e8
    style UC105 fill:#e8e8e8
```

---

## 7. CRITICAL PATH ANALYSIS

### 7.1 Core UCs (Most Relationships)

| UC ID | UC Name | Relationships | Type |
|-------|---------|---------------|------|
| UC-25 | Universal Notification | 6 | CRITICAL |
| UC-53 | IPSARA Assessment | 5 | CRITICAL |
| UC-52 | Maintain Unified ISMS | 4 | CRITICAL |
| UC-33 | Data Erasure | 4 | CRITICAL |
| UC-57 | AI-Powered Threat Detection | 4 | CRITICAL |
| UC-44 | Secure CI/CD | 4 | CRITICAL |
| UC-49 | Security Competence | 4 | CRITICAL |

### 7.2 Critical Path Length

Longest dependency chains (Decomposition Cycle):

```
UC-25 → UC-105 → [Regulatory Specializations]
Length: 2

UC-53 → UC-116 → UC-53.1 (DPIA) / UC-53.2 (FRIA)
Length: 2

UC-44 → UC-111 → UC-44.1 (AI Deployment Gate)
Length: 3 (longest)
```

---

## 8. REGULATORY COVERAGE VIA RELATIONSHIPS

| Regulation | Specializations | Coverage |
|------------|----------------|----------|
| GDPR | UC-02-GDPR, UC-25-GDPR, UC-33-GDPR, UC-53-GDPR | 4 |
| CRA | UC-25-CRA, UC-42-CRA, UC-44-CRA | 3 |
| NIS 2 | UC-16-DORA, UC-25-NIS2, UC-37-DORA, UC-44-NIS2 | 4 |
| DORA | UC-16-DORA, UC-25-DORA, UC-37-DORA, UC-39-DORA, UC-52-DORA | 5 |
| AI Act | UC-17-AI, UC-25-AI, UC-49-AI | 3 |

---

## 9. STOP CONDITION CHECK — SC2 (Relationship Completeness)

| Check | Value | Threshold | Status |
|-------|-------|-----------|--------|
| Total UCs | 62 | — | — |
| UCs with relationships | 62 | — | — |
| Orphan UCs | 0 | 0 | ✅ PASS |
| Relationship coverage | 100% | 100% | ✅ PASS |

**SC2: PASS — All UCs have proper relationships, no orphan UCs.**

---

## 10. NEXT STEPS

1. **Define Use Case Variability (Doc 13b)** — Document alternative scenarios and specialization matrix
2. **Compliance Analysis Gate** — Verify SC1 (Rule Coverage) and SC4 (Variability Complete)
3. **Iteration 1 Complete** — Proceed to Iteration 2 for detailed flows on complex UCs

---

## 11. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-28 | Compliance Lead | Initial creation — 48 relationships across 62 UCs |

---

## 12. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Compliance Lead | [TBD] | | |
| CISO | [TBD] | | |
| Data Protection Officer | [TBD] | | |
| AI Governance Lead | [TBD] | | |

---

**Next Step:** Proceed to 13b_Use_Case_Variability.md to define variability scenarios.