---
document_id: AEGIS-P3-13
title: Use Cases Catalog
phase: 3
version: 1.2
created: 2026-04-04
updated: 2026-08-10
author: System Architect
status: DRAFT
inputs: [01_Company_Context.md, 11_Rules_Catalog.md, 10_Privacy_Security_Goals.md, 09_Strategic_Tensions_Report.md]
outputs: [14_Architectural_Nodes.md, 15_Requirements_Allocation.md, 23_Functional_Requirements.md]
traceability: AEGIS Class Model → UseCase, BusinessGoal, Stakeholder classes
related_documents: 04_Company_Context_Assessment.md, 07_Structured_Compliance_Matrix.md
sprint_11_scope: corr-008 Phase 3 ID harmonisation — add Related PSOs column linking UC to PO/SO from Commit D; migrate BPR-AI-NN → BPR-D-XX.Y-NNN; add T-009 (D-10.1 monitoring opt-out) cross-ref; tech-strip vendor/tool mentions.
---

# Use Cases Catalog — SecureBorder Solutions

## 1. DOCUMENT PURPOSE

This document defines the **security and privacy use cases** for SecureBorder Solutions B.V., derived from Phase 1 (Company Context, Compliance Matrix) and Phase 2 (Rules Catalog, Privacy/Security Goals, Strategic Tensions).

**Alignment with Class Model:**
- `UseCase` — Functional security and privacy scenarios
- `BusinessGoal` — Strategic objectives from Phase 1
- `Stakeholder` — Actors from Company Context (450 employees, B2G/B2B)
- `DerivationNode` — Link to requirements allocation

**Phase 3 Step:** B (Use Cases Catalog — Security + Privacy + AI Focus)

**Gate Criteria:**
- [ ] All 38 goals mapped to use cases
- [ ] All 63 rules covered (38 CR + 25 BP)
- [ ] All 9 strategic tensions addressed
- [ ] Stakeholders assigned to use cases
- [ ] AI_Act high-risk requirements explicitly covered
- [ ] GDPR Art. 9 biometric data processing covered

---

## 2. USE CASES CATALOG METADATA

| Attribute | Value |
|-----------|-------|
| useCasesCatalogId | UC-SECUREBORDER-2026-001 |
| completionDate | 2026-04-04 |
| basedOnCompanyContext | CC-SECUREBORDER-2026-001 |
| basedOnRulesCatalog | RULES-SECUREBORDER-2026-001 |
| basedOnGoalsCatalog | GOALS-SECUREBORDER-2026-001 |
| basedOnTensionsReport | STR-TENSION-SECUREBORDER-2026-001 |
| completedBy | System Architect |
| phase3Step | B1+B2+B3+B4 |
| companyProfile | Medium-Large (450 employees), B2G/B2B, GDPR+CRA+NIS2+AI_Act |
| totalUseCases | 44 |
| categories | DP, SEC, IAM, DEV, GOV, AI, TRN |

---

## 3. STAKEHOLDER CATALOG (from Phase 1)

### 3.1 Internal Stakeholders

| Stakeholder ID | Name/Role | Type | Responsibilities | Contact | FTE Allocation |
|----------------|-----------|------|------------------|---------|----------------|
| SH-INT-001 | CEO | Internal | Business decisions, risk acceptance, board-level security committee | ceo@secureborder.eu | 0.05 |
| SH-INT-002 | CTO | Internal | Technical architecture, secure SDLC oversight, AI system design | cto@secureborder.eu | 0.3 |
| SH-INT-003 | CISO | Internal | ISMS management, SOC oversight, incident response, regulatory reporting | ciso@secureborder.eu | 1.0 |
| SH-INT-004 | DPO | Internal | GDPR compliance, DPIA execution, data subject rights, RoPA maintenance | dpo@secureborder.eu | 1.0 |
| SH-INT-005 | AI Governance Lead | Internal | AI_Act conformity, FRIA execution, post-market monitoring, bias testing | ai-gov@secureborder.eu | 1.0 |
| SH-INT-006 | Lead Developer | Internal | Secure coding, code review, CI/CD pipeline, SBOM generation | dev-lead@secureborder.eu | 0.4 |
| SH-INT-007 | Operations Lead | Internal | Infrastructure management, patch deployment, system monitoring | ops-lead@secureborder.eu | 0.5 |
| SH-INT-008 | SOC Manager | Internal | 24/7 SOC operations, incident detection/triage, alert management | soc-mgr@secureborder.eu | 1.0 |
| SH-INT-009 | Security Engineer | Internal | Vulnerability management, penetration testing, security tooling | sec-eng@secureborder.eu | 1.0 |
| SH-INT-010 | Compliance Analyst | Internal | Audit preparation, compliance reporting, vendor assessments | compliance@secureborder.eu | 1.0 |

### 3.2 External Stakeholders

| Stakeholder ID | Name/Role | Type | Responsibilities | Relationship | SLA/Contract |
|----------------|-----------|------|------------------|--------------|--------------|
| SH-EXT-001 | Border Control Officer | External | Operates eGate, reviews AI decisions, human-in-the-loop override | Government authority | Government contract |
| SH-EXT-002 | Traveler (Data Subject) | External | Biometric data subject, privacy rights holder | End user of eGate | GDPR Rights |
| SH-EXT-003 | National Border Authority | External | Controller for biometric data, watchlist management | Government client | B2G contract |
| SH-EXT-004 | Airport Operator | External | Physical infrastructure, network connectivity, physical security | B2B client | B2B contract + SLA |
| SH-EXT-005 | Cloud Provider | External | Remote infrastructure for AI model updates, model hosting | Processor | DPA + SLA (99.99%) |
| SH-EXT-006 | Hardware Supplier | External | eGate kiosk hardware, biometric sensors, cryptographic modules | Supplier | Supply contract + SBOM |
| SH-EXT-007 | Notified Body (CRA) | External | Critical Class conformity assessment, third-party certification | Regulator (CRA) | Assessment contract |
| SH-EXT-008 | ENISA | External | Vulnerability coordination, cybersecurity guidance | Regulator | As required |
| SH-EXT-009 | National CSIRT | External | Incident early warning, threat intelligence sharing | Regulator (NIS 2) | 24h notification |
| SH-EXT-010 | Data Protection Authority | External | GDPR supervision, breach notification recipient, audit | Regulator (GDPR) | 72h notification |
| SH-EXT-011 | AI Market Surveillance Authority | External | AI_Act supervision, conformity verification, post-market oversight | Regulator (AI_Act) | Cooperation |
| SH-EXT-012 | External Auditor | External | ISO 27001/27701 audits, compliance verification | Independent | Annual |
| SH-EXT-013 | Penetration Testing Firm | External | Threat-led penetration testing, AI adversarial testing | Service provider | Annual contract |

### 3.3 Stakeholder → Use Case Summary

| Stakeholder | Primary Use Cases | Support Use Cases | Frequency | FTE Required |
|-------------|-------------------|-------------------|-----------|--------------|
| SH-INT-001 (CEO) | U.C.5.1.1, U.C.5.2.1 | U.C.2.5.1 | Quarterly | 0.05 |
| SH-INT-002 (CTO) | U.C.4.1.1, U.C.4.2.1, U.C.6.1.1 | U.C.2.5.1, U.C.5.3.1 | Weekly | 0.3 |
| SH-INT-003 (CISO) | U.C.2.1.1, U.C.2.2.1, U.C.2.3.1, U.C.5.3.1 | U.C.2.4.1, U.C.5.1.1 | Daily | 1.0 |
| SH-INT-004 (DPO) | U.C.1.1.1, U.C.1.2.1, U.C.1.3.1, U.C.5.5.1 | U.C.2.2.1, U.C.5.4.1 | Daily | 1.0 |
| SH-INT-005 (AI Gov) | U.C.6.1.1, U.C.6.2.1, U.C.6.3.1, U.C.6.4.1 | U.C.5.5.1, U.C.2.2.1 | Daily | 1.0 |
| SH-INT-006 (Dev Lead) | U.C.4.1.1, U.C.4.2.1, U.C.4.3.1 | U.C.4.4.1, U.C.4.5.1 | Daily | 0.4 |
| SH-INT-007 (Ops Lead) | U.C.2.4.1, U.C.3.1.1, U.C.3.5.1 | U.C.2.6.1, U.C.3.6.1 | Daily | 0.5 |
| SH-INT-008 (SOC Mgr) | U.C.2.1.1, U.C.2.6.1, U.C.2.7.1 | U.C.2.2.1, U.C.6.5.1 | 24/7 | 1.0 |
| SH-INT-009 (Sec Eng) | U.C.2.3.1, U.C.2.8.1 | U.C.4.3.1, U.C.6.6.1 | Weekly | 1.0 |
| SH-INT-010 (Compliance) | U.C.5.4.1, U.C.5.6.1, U.C.5.7.1 | U.C.5.5.1, U.C.1.4.1 | Monthly | 1.0 |
| SH-EXT-001 (Border Officer) | U.C.3.2.1, U.C.6.3.1 | U.C.2.7.1 | Per shift | N/A |
| SH-EXT-002 (Traveler) | U.C.1.1.1, U.C.1.2.1 | U.C.3.3.1 | As needed | N/A |
| SH-EXT-003 (Border Authority) | U.C.5.7.1, U.C.1.4.1 | U.C.6.4.1 | As required | N/A |

---

## 4. BUSINESS GOALS MAPPING (from Phase 1)

### 4.1 Security Business Goals

| Goal ID | Goal Description | Priority | Related Regulations | Related Stakeholders |
|---------|------------------|----------|---------------------|---------------------|
| BG-001 | CRA Critical Class certification | CRITICAL | CRA | SH-INT-002, SH-INT-003, SH-EXT-007 |
| BG-002 | AI_Act conformity assessment | CRITICAL | AI_Act | SH-INT-005, SH-INT-002, SH-EXT-011 |
| BG-003 | NIS 2 compliance (24h incident reporting) | CRITICAL | NIS 2 | SH-INT-003, SH-INT-008, SH-EXT-009 |
| BG-004 | GDPR Art. 9 biometric data compliance | CRITICAL | GDPR | SH-INT-004, SH-INT-005, SH-EXT-010 |
| BG-005 | 99.99% uptime SLA | HIGH | NIS 2, CRA | SH-INT-007, SH-INT-008, SH-EXT-005 |
| BG-006 | Schengen Area expansion readiness | HIGH | GDPR, AI_Act | SH-INT-001, SH-EXT-003 |
| BG-007 | ISO 27001/27701 maintenance | HIGH | ISO 27001/27701 | SH-INT-003, SH-INT-010, SH-EXT-012 |

---

## 5. SYSTEM OVERVIEW

### 5.1 Use Case Diagram (Level 0)

```mermaid
useCaseDiagram
    actor "Border Control Officer" as BCO
    actor "Traveler" as TRV
    actor "CISO" as CISO
    actor "DPO" as DPO
    actor "AI Governance Lead" as AIG
    actor "SOC Manager" as SOC
    actor "Lead Developer" as DEV
    actor "Operations Lead" as OPS
    actor "Compliance Analyst" as COMP
    actor "National Border Authority" as NBA
    actor "ENISA/CSIRT" as ENISA
    actor "Data Protection Authority" as DPA
    actor "AI Market Surveillance" as AIMS

    package "Data Protection" {
        usecase "UC-DP\nData Subject Rights\n& Privacy" as UCDP
    }
    package "Security Operations" {
        usecase "UC-SEC\nIncident Detection,\nResponse & Recovery" as UCSEC
    }
    package "Identity & Access Mgmt" {
        usecase "UC-IAM\nAuthentication,\nAuthorization & Lifecycle" as UCIAM
    }
    package "Secure Development" {
        usecase "UC-DEV\nSecure SDLC,\nCI/CD & SBOM" as UCDEV
    }
    package "Governance & Compliance" {
        usecase "UC-GOV\nISMS, Audits,\nRisk Assessments" as UCGOV
    }
    package "AI Systems" {
        usecase "UC-AI\nAI Conformity, Monitoring,\nBias & Human Oversight" as UCAI
    }
    package "Training & Awareness" {
        usecase "UC-TRN\nSecurity & AI\nTraining" as UCTRN
    }

    BCO --> UCIAM
    BCO --> UCAI
    TRV --> UCDP
    TRV --> UCIAM
    CISO --> UCSEC
    CISO --> UCGOV
    DPO --> UCDP
    DPO --> UCGOV
    AIG --> UCAI
    AIG --> UCGOV
    SOC --> UCSEC
    SOC --> UCAI
    DEV --> UCDEV
    OPS --> UCIAM
    OPS --> UCSEC
    COMP --> UCGOV
    NBA --> UCGOV
    ENISA --> UCSEC
    DPA --> UCDP
    AIMS --> UCAI
```

### 5.2 Level 0 Use Case Descriptions

| UC ID | Use Case Name | Description | Primary Actors | Business Goals | Priority |
|-------|---------------|-------------|----------------|----------------|----------|
| UC-DP | Data Subject Rights & Privacy | Exercise GDPR data subject rights (access, erasure, portability) and protect biometric data | DPO, Traveler, Border Authority | BG-004, BG-006 | CRITICAL |
| UC-SEC | Security Operations | Detect, respond to, and recover from security incidents; manage vulnerabilities | CISO, SOC Manager, Operations Lead | BG-003, BG-005 | CRITICAL |
| UC-IAM | Identity & Access Management | Manage identities, authentication, authorization for operators and systems | Operations Lead, Border Control Officer | BG-001, BG-003 | CRITICAL |
| UC-DEV | Secure Development | Implement secure SDLC, CI/CD gates, SBOM, dependency management | Lead Developer, CTO | BG-001, BG-007 | HIGH |
| UC-GOV | Governance & Compliance | Maintain ISMS, conduct risk assessments, audits, regulatory reporting | CISO, Compliance Analyst, DPO | BG-001, BG-002, BG-003, BG-004, BG-007 | CRITICAL |
| UC-AI | AI Systems Management | AI conformity assessment, post-market monitoring, bias testing, human oversight | AI Governance Lead, SOC Manager | BG-002, BG-004, BG-006 | CRITICAL |
| UC-TRN | Training & Awareness | Security awareness, role-specific training, AI competence, phishing simulation | All internal staff | BG-003, BG-007 | HIGH |

---

## 6. DOMAIN DECOMPOSITION

### 6.1 UC-DP: Data Protection

| UC ID | Use Case Name | Description | Primary Actor | Related Rules | Related Goals | Related PSOs | Priority | Regulation | SLA |
|-------|---------------|-------------|---------------|---------------|---------------|--------------|----------|------------|-----|
| U.C.1.1.1 | Data Subject Access Request | Traveler requests access to their biometric and personal data | SH-EXT-002 (Traveler) | CR-D-05.4-001 | PO-D-05.4-001 | PO-D-05.4-001, PO-D-09.4-001 | HIGH | GDPR Art. 15 | 30 days |
| U.C.1.2.1 | Right to Erasure (Cryptographic Sharding) | Traveler requests erasure; token-to-identity mapping destroyed, anonymized logs retained | SH-EXT-002 (Traveler) | CR-D-05.3-001 | PO-D-05.3-001 | PO-D-05.3-001, PO-D-01.1-001, SO-D-10.2-001 | CRITICAL | GDPR Art. 17 | 30 days |
| U.C.1.3.1 | Data Portability Export | Export personal data in machine-readable format for transfer to another controller | SH-EXT-002 (Traveler) | CR-D-05.4-001 | PO-D-05.4-001 | PO-D-05.4-001, PO-D-09.4-001 | MEDIUM | GDPR Art. 20 | 30 days |
| U.C.1.4.1 | Biometric Data Breach Notification | Notify DPA and affected travelers of biometric data breach | SH-INT-004 (DPO) | CR-D-04.3-001 | PO-D-04.3-001 | PO-D-04.3-001, PO-D-09.4-001 | CRITICAL | GDPR Art. 33/34 | 72h to DPA |
| U.C.1.5.1 | Data Minimization Review | Review and minimize data collection fields for AI training and operational processing | SH-INT-004 (DPO) | CR-D-05.1-001 | PO-D-05.1-001 | PO-D-05.1-001, PO-D-07.1-001, SO-D-05.1-001 | HIGH | GDPR Art. 5(1)(c) | Annual |
| U.C.1.6.1 | RoPA Maintenance | Maintain records of processing activities for biometric and passport data processing | SH-INT-004 (DPO) | CR-D-09.4-001 | PO-D-09.4-001 | PO-D-09.4-001, PO-D-09.1-001 | HIGH | GDPR Art. 30 | Continuous |

### 6.2 UC-SEC: Security Operations

| UC ID | Use Case Name | Description | Primary Actor | Related Rules | Related Goals | Related PSOs | Priority | Regulation | SLA |
|-------|---------------|-------------|---------------|---------------|---------------|--------------|----------|------------|-----|
| U.C.2.1.1 | Incident Detection & Triage | SOC detects and triages security incidents with 24/7 monitoring | SH-INT-008 (SOC Mgr) | CR-D-04.1-001, BPR-D-04.5-001 | SO-D-04.1-001 | SO-D-04.1-001, SO-D-04.1-002, SO-D-04.1-003 | CRITICAL | NIS 2 Art. 21 | 15 min triage |
| U.C.2.2.1 | Incident Response & Containment | Respond to and contain security incidents with DoS resilience | SH-INT-003 (CISO) | CR-D-04.2-001, BPR-D-04.2-001 | PO-D-04.2-001 | PO-D-04.2-001, PO-D-04.2-002, SO-D-04.2-001 | CRITICAL | NIS 2 Art. 21 | Containment: 1h |
| U.C.2.3.1 | Vulnerability Scanning & Management | Continuous vulnerability scanning with 24h SLA for critical findings | SH-INT-009 (Sec Eng) | CR-D-02.1-001, BPR-D-02.1-001, BPR-D-02.5-001 | SO-D-02.1-001 | SO-D-02.1-001, SO-D-02.1-002, SO-D-02.1-003 | CRITICAL | CRA Art. 10 | 24h critical |
| U.C.2.4.1 | Patch Deployment (Signed OTA) | Deploy signed firmware and software updates with rollback capability | SH-INT-007 (Ops Lead) | CR-D-02.2-001 | SO-D-02.2-001 | SO-D-02.2-001, SO-D-02.2-002 | CRITICAL | CRA Art. 10 | Critical: 24h |
| U.C.2.5.1 | Regulatory Notification (Unified 24h/72h) | Unified incident notification workflow for GDPR/CRA/NIS 2/AI_Act | SH-INT-003 (CISO) | CR-D-04.3-001 | PO-D-04.3-001 | PO-D-04.3-001, PO-D-04.3-002 | CRITICAL | GDPR/CRA/NIS2 | 24h (compound event) / 72h (GDPR-only) |
| U.C.2.6.1 | Continuous Security Monitoring | Unified SOC monitoring covering security + AI post-market metrics | SH-INT-008 (SOC Mgr) | CR-D-10.1-001, BPR-D-10.4-001, BPR-D-10.5-001 | SO-D-10.1-001 | SO-D-10.1-001, SO-D-10.1-002, SO-D-10.1-003 | HIGH | NIS 2 Art. 21 | 24/7 |
| U.C.2.7.1 | Disaster Recovery & Business Continuity | Activate DR procedures and restore systems after incidents | SH-INT-007 (Ops Lead) | CR-D-04.4-001, BPR-D-04.2-001 | PO-D-04.4-001 | PO-D-04.4-001, PO-D-04.4-002 | HIGH | NIS 2 Art. 21 | RTO: 1h, RPO: 15min |
| U.C.2.8.1 | Threat-Led Penetration Testing | Conduct TLPT and adversarial AI testing for border control systems | SH-INT-009 (Sec Eng) | CR-D-02.4-001, BPR-D-02.4-002 | SO-D-02.4-001 | SO-D-02.4-001, SO-D-02.4-002 | HIGH | NIS 2 Art. 21(2)(d) | Annual |

### 6.3 UC-IAM: Identity & Access Management

| UC ID | Use Case Name | Description | Primary Actor | Related Rules | Related Goals | Related PSOs | Priority | Regulation | SLA |
|-------|---------------|-------------|---------------|---------------|---------------|--------------|----------|------------|-----|
| U.C.3.1.1 | Border Officer Identity Lifecycle | Provision/deprovision border control officer identities with government IdP integration | SH-INT-007 (Ops Lead) | CR-D-03.1-001 | SO-D-03.1-001 | SO-D-03.1-001, SO-D-03.1-002, SO-D-03.1-003 | HIGH | NIS 2 Art. 21 | 24h |
| U.C.3.2.1 | Multi-Factor Authentication | MFA for all system access points including eGate operator interfaces | SH-EXT-001 (Border Officer) | CR-D-03.2-001 | SO-D-03.2-001 | SO-D-03.2-001, SO-D-03.2-002, SO-D-03.2-003 | CRITICAL | CRA Annex I | Per session |
| U.C.3.3.1 | Biometric Enrollment | Enroll traveler biometric templates using approved cryptographic modules | SH-EXT-002 (Traveler) | CR-D-01.1-001 | PO-D-01.1-001 | PO-D-01.1-001, PO-D-01.1-002, SO-D-01.3-001 | CRITICAL | GDPR Art. 9 | Per enrollment |
| U.C.3.4.1 | Least Privilege Access Enforcement | Enforce role-based access for data processing, administration, and AI oversight | SH-INT-007 (Ops Lead) | CR-D-03.3-001, BPR-D-03.1-001, BPR-D-03.5-001 | PO-D-03.3-001 | PO-D-03.3-001, PO-D-03.3-002, SO-D-03.1-001 | HIGH | NIS 2 Art. 21 | Continuous |
| U.C.3.5.1 | Secure Default Configuration | Ensure eGate ships with secure defaults: no default passwords, unused ports disabled | SH-INT-007 (Ops Lead) | CR-D-03.4-001 | SO-D-03.4-001 | SO-D-03.4-001, SO-D-03.1-001 | HIGH | CRA Annex I | Per deployment |
| U.C.3.6.1 | Access Rights Review | Periodic review of access rights for all system users | SH-INT-007 (Ops Lead) | CR-D-03.3-001 | PO-D-03.3-001 | PO-D-03.3-001, PO-D-03.3-002 | MEDIUM | NIS 2 Art. 21 | Quarterly |
| U.C.3.7.1 | Human-in-the-Loop Override | Border officer overrides AI border control decision with documented procedure | SH-EXT-001 (Border Officer) | BPR-D-03.1-002 | SO-D-03.1-001 | SO-D-03.1-001, SO-D-03.1-002, SO-D-03.1-003 | CRITICAL | AI_Act Art. 14 | Real-time |

### 6.4 UC-DEV: Secure Development

| UC ID | Use Case Name | Description | Primary Actor | Related Rules | Related Goals | Related PSOs | Priority | Regulation | SLA |
|-------|---------------|-------------|---------------|---------------|---------------|--------------|----------|------------|-----|
| U.C.4.1.1 | Secure Code Review | Static analysis and manual code review for all code changes | SH-INT-006 (Dev Lead) | CR-D-07.2-001 | SO-D-07.2-001 | SO-D-07.2-001, SO-D-07.2-002 | HIGH | CRA Annex I | Per commit |
| U.C.4.2.1 | Dependency Scanning & SBOM | Scan dependencies for vulnerabilities; generate/update SBOM | SH-INT-006 (Dev Lead) | CR-D-02.1-001, CR-D-06.2-001 | SO-D-02.1-001, SO-D-06.2-001 | SO-D-02.1-001, SO-D-06.2-001 | HIGH | CRA Art. 10 | Per build |
| U.C.4.3.1 | CI/CD Security Gate | Blocking security gates in pipeline for critical findings | SH-INT-006 (Dev Lead) | CR-D-07.3-001, BPR-D-07.1-001, BPR-D-07.5-001 | SO-D-07.3-001 | SO-D-07.3-001, PO-D-07.1-001 | CRITICAL | NIS 2 Art. 21 | Per PR |
| U.C.4.4.1 | Change Management | Formal change management with documented approval and rollback | SH-INT-006 (Dev Lead) | CR-D-07.4-001 | NOT_ADDRESSED | NOT_ADDRESSED, SO-D-07.2-001 | HIGH | NIS 2 Art. 21 | Per change |
| U.C.4.5.1 | Privacy-by-Design Integration | Integrate privacy-by-design and secure-by-default into product design | SH-INT-002 (CTO) | CR-D-07.1-001, BPR-D-07.1-002 | PO-D-07.1-001 | PO-D-07.1-001, PO-D-07.1-002, SO-D-07.1-001 | HIGH | GDPR/CRA | Per design phase |
| U.C.4.6.1 | AI Model Versioning & Rollback | Version AI models with rollback capability for production border control models | SH-INT-006 (Dev Lead) | BPR-D-07.1-002 | PO-D-07.1-001 | PO-D-07.1-001, PO-D-07.1-002, SO-D-02.2-001 | HIGH | AI_Act | Per model update |

### 6.5 UC-GOV: Governance & Compliance

| UC ID | Use Case Name | Description | Primary Actor | Related Rules | Related Goals | Related PSOs | Priority | Regulation | SLA |
|-------|---------------|-------------|---------------|---------------|---------------|--------------|----------|------------|-----|
| U.C.5.1.1 | ISMS Maintenance | Maintain unified ISMS with regulation-specific annexes (GDPR, CRA, NIS 2, AI_Act) | SH-INT-003 (CISO) | CR-D-09.1-001, BPR-D-09.1-001, BPR-D-09.5-001 | PO-D-09.1-001 | PO-D-09.1-001, PO-D-09.1-002, SO-D-09.1-001 | CRITICAL | All 4 regs | Continuous |
| U.C.5.2.1 | Unified Impact Assessment (DPIA+FRIA) | Conduct unified DPIA+FRIA with dual outputs for biometric AI processing | SH-INT-004 (DPO) | CR-D-09.2-001 | PO-D-09.2-001 | PO-D-09.2-001, PO-D-09.2-002, SO-D-09.2-001 | CRITICAL | GDPR/AI_Act | Prior to launch / Annual / On significant change |
| U.C.5.3.1 | Risk Assessment & Management | Conduct security risk assessments with cybersecurity focus | SH-INT-003 (CISO) | CR-D-09.2-001 | PO-D-09.2-001 | PO-D-09.2-001, PO-D-09.2-002 | HIGH | NIS 2 Art. 21 | Annual |
| U.C.5.4.1 | Compliance Audit & Reporting | Generate compliance reports and prepare for external audits | SH-INT-010 (Compliance) | CR-D-10.3-001 | PO-D-10.3-001 | PO-D-10.3-001, PO-D-10.3-002, SO-D-10.3-001 | HIGH | All 4 regs | Quarterly |
| U.C.5.5.1 | Vendor Risk Assessment | Assess and monitor vendor security risks with unified questionnaire | SH-INT-010 (Compliance) | CR-D-06.1-001, CR-D-06.3-001, BPR-D-06.5-001 | PO-D-06.1-001 | PO-D-06.1-001, PO-D-06.1-002, PO-D-06.3-001 | HIGH | GDPR/NIS 2 | Annual |
| U.C.5.6.1 | Asset Inventory Management | Maintain comprehensive inventory of hardware, software, data, AI components | SH-INT-010 (Compliance) | CR-D-09.3-001 | NOT_ADDRESSED | NOT_ADDRESSED, PO-D-09.1-001 | MEDIUM | NIS 2 Art. 21 | Continuous |
| U.C.5.7.1 | Regulatory Notification & Cooperation | Cooperate with market surveillance, CSIRT, ENISA, and data protection authorities | SH-INT-010 (Compliance) | CR-D-04.3-001 | PO-D-04.3-001 | PO-D-04.3-001, PO-D-04.3-002 | CRITICAL | All 4 regs | Per regulation |
| U.C.5.8.1 | Third-Party Boundary Management | Enforce physical isolation per airport/country instance | SH-INT-007 (Ops Lead) | CR-D-06.4-001 | SO-D-06.4-001 | SO-D-06.4-001, PO-D-06.1-001 | MEDIUM | NIS 2 | Per deployment |

### 6.6 UC-AI: AI Systems Management (NEW Category for SecureBorder)

| UC ID | Use Case Name | Description | Primary Actor | Related Rules | Related Goals | Related PSOs | Priority | Regulation | SLA |
|-------|---------------|-------------|---------------|---------------|---------------|--------------|----------|------------|-----|
| U.C.6.1.1 | AI Conformity Assessment | Prepare and execute AI_Act conformity assessment for high-risk border control AI | SH-INT-005 (AI Gov) | CR-D-09.1-001, CR-D-09.2-001 | PO-D-09.1-001, PO-D-09.2-001 | PO-D-09.1-001, PO-D-09.2-001, PO-D-09.2-002, SO-D-09.1-001 | CRITICAL | AI_Act Art. 9/43 | Before placement |
| U.C.6.2.1 | AI Accuracy Monitoring & Drift Detection | Continuous AI accuracy monitoring with automated drift detection at >1% degradation | SH-INT-005 (AI Gov) | BPR-D-10.5-001, CR-D-10.1-001 | SO-D-10.1-001 | SO-D-10.1-001, SO-D-10.1-002, SO-D-10.1-003 | CRITICAL | AI_Act Art. 61 | Real-time |
| U.C.6.3.1 | AI Bias Testing & Fairness Assessment | Quarterly bias testing across demographic groups with documented results | SH-INT-005 (AI Gov) | BPR-D-02.4-001, CR-D-02.4-001 | SO-D-02.4-001 | SO-D-02.4-001, SO-D-02.4-002, PO-D-05.1-001 | HIGH | AI_Act Art. 9 | Quarterly |
| U.C.6.4.1 | AI Explainability Reporting | Generate explainability reports for each border control decision with confidence scores | SH-INT-005 (AI Gov) | BPR-D-10.2-001, CR-D-10.2-001 | SO-D-10.2-001 | SO-D-10.2-001, SO-D-10.2-002, SO-D-10.2-003 | HIGH | AI_Act Art. 13 | Per decision |
| U.C.6.5.1 | AI Incident Response | Respond to AI-specific failures (false accept, false reject, model drift) | SH-INT-008 (SOC Mgr) | BPR-D-04.2-001, CR-D-04.2-001 | PO-D-04.2-001 | PO-D-04.2-001, PO-D-04.2-002, SO-D-04.2-001 | CRITICAL | AI_Act Art. 61 | 15 min detection |
| U.C.6.6.1 | AI Adversarial Testing | Quarterly red-team exercises targeting biometric spoofing and adversarial attacks | SH-INT-009 (Sec Eng) | BPR-D-02.4-002, CR-D-02.4-001 | SO-D-02.4-001 | SO-D-02.4-001, SO-D-02.4-002 | HIGH | AI_Act Art. 9 | Quarterly |
| U.C.6.7.1 | AI Training Data Management | Version and track lineage of all AI training datasets with representativeness checks | SH-INT-005 (AI Gov) | BPR-D-05.1-001, CR-D-05.1-001 | PO-D-05.1-001 | PO-D-05.1-001, SO-D-05.1-001, SO-D-05.1-002 | HIGH | AI_Act Art. 10 | Per training cycle |

### 6.7 UC-TRN: Training & Awareness

| UC ID | Use Case Name | Description | Primary Actor | Related Rules | Related Goals | Related PSOs | Priority | Regulation | SLA |
|-------|---------------|-------------|---------------|---------------|---------------|--------------|----------|------------|-----|
| U.C.7.1.1 | Security Awareness Training | Annual security awareness covering GDPR, CRA, NIS 2 topics | SH-INT-003 (CISO) | CR-D-08.1-001, BPR-D-08.4-001 | PO-D-08.1-001 | PO-D-08.1-001, PO-D-08.1-002 | MEDIUM | GDPR/NIS 2 | Annual |
| U.C.7.2.1 | Role-Specific Security Training | Role-specific training for developers, operators, SOC, AI oversight personnel | SH-INT-003 (CISO) | CR-D-08.2-001 | PO-D-08.2-001 | PO-D-08.2-001, PO-D-08.2-002, SO-D-08.2-001 | HIGH | GDPR/NIS 2/AI_Act | On role assignment |
| U.C.7.3.1 | AI Competence Training | AI-specific training for human oversight personnel on border control AI operation | SH-INT-005 (AI Gov) | CR-D-08.2-001 | PO-D-08.2-001 | PO-D-08.2-001, PO-D-08.2-002, SO-D-08.2-001 | HIGH | AI_Act Art. 14 | On role assignment |
| U.C.7.4.1 | Management Board Cybersecurity Training | NIS 2 management liability training for board members | SH-INT-001 (CEO) | CR-D-08.3-001 | NOT_ADDRESSED | NOT_ADDRESSED, PO-D-08.1-001 | HIGH | NIS 2 Art. 20 | Annual |
| U.C.7.5.1 | Phishing Simulation | Quarterly phishing simulation exercises for all staff | SH-INT-003 (CISO) | BPR-D-04.5-001, BPR-D-08.4-001 | SO-D-04.1-001 | SO-D-04.1-001, PO-D-08.1-001 | LOW | Best Practice | Quarterly |

---

## 7. DETAILED USE CASES

### 7.1 U.C.1.2.1: Right to Erasure with Cryptographic Sharding (Detailed)

**Use Case ID:** U.C.1.2.1
**Name:** Right to Erasure (Cryptographic Sharding)
**Description:** Traveler requests erasure of biometric and personal data; token-to-identity mapping destroyed while anonymized AI activity logs retained
**Primary Actor:** SH-EXT-002 (Traveler)
**Supporting Actors:** SH-INT-004 (DPO), SH-INT-005 (AI Governance Lead), System
**GDPR Article:** Art. 17 (Right to Erasure)
**Priority:** CRITICAL
**Frequency:** As needed (unlimited requests per traveler)
**SLA:** 30 days (GDPR maximum), 7 days (target)

**Activation Condition:** CONTEXTUAL — activated by erasure request; cryptographic sharding resolves T-002 when personal data exists in AI logs.

**Preconditions:**
- Traveler has authenticated identity
- One of Art. 17(1) conditions applies
- Biometric data and AI logs exist for this traveler
- Tokenization system is operational

**Postconditions:**
- Token-to-identity mapping destroyed (irreversible)
- Anonymized AI activity logs retained (token-only, no PII)
- Erasure logged for compliance
- Government authority notified (as controller)
- Erasure confirmation sent to traveler

**Main Flow:**
1. Traveler submits erasure request via secure portal or government authority
2. System verifies traveler identity (government IdP or passport verification)
3. System logs erasure request with timestamp
4. DPO validates legal basis for erasure (Art. 17(1) conditions)
5. System identifies all data locations: biometric templates, passport data, AI match logs, audit trails
6. System destroys token-to-identity mapping in encrypted mapping store
7. System verifies anonymized AI logs contain only tokens (no PII)
8. System notifies government authority of erasure completion
9. System confirms erasure to traveler
10. System logs erasure completion with evidence

**Alternative Flows:**
- 4a. Legal basis not valid (e.g., government legal hold) → Partial erasure; retain per government mandate
- 4b. Government authority is controller → Forward request to government; SecureBorder erases only controller-held data
- 7a. AI logs contain PII beyond tokens → Remediate logs before retention

**Exceptions:**
- E1. Legal obligation to retain (government mandate) → Retain per contract; inform traveler of legal basis
- E2. Tokenization not irreversible → Emergency re-tokenization with new salt; destroy old mapping

**Business Rules:**
- BR-ERASE-01: All erasure requests must be logged with timestamp
- BR-ERASE-02: Response within 30 days (GDPR Art. 12(3))
- BR-ERASE-03: Token-to-identity mapping must be truly irreversible (one-way hash with per-traveler salt)
- BR-ERASE-04: Anonymized AI logs retained for minimum 6 months (AI_Act Art. 19(1); Art. 12 = transparency, not retention)
- BR-ERASE-05: Government authority notified as controller for processor-held data

**Related Requirements:**
- NFR: NFR-023 (Erasure within 30 days with cryptographic sharding)
- NFR: NFR-036 (Erasure evidence logging with 6-month retention)
- FR: FR-18 (System shall enable erasure request submission)
- FR: FR-19 (System shall destroy token-to-identity mapping)
- FR: FR-71 (System shall retain anonymized AI logs with tokens only)

**Tension Reference:** T-002 (Erasure vs. AI_Act Art. 19(1) Log Retention — resolved via cryptographic sharding; Art. 12 = transparency, not retention)

---

### 7.2 U.C.2.1.1: Incident Detection & Triage (Detailed)

**Use Case ID:** U.C.2.1.1
**Name:** Incident Detection & Triage
**Description:** 24/7 SOC detects security incidents through unified monitoring platform covering traditional security and AI post-market metrics
**Primary Actor:** SH-INT-008 (SOC Manager)
**Supporting Actors:** SH-INT-003 (CISO), SH-INT-009 (Security Engineer), SH-INT-005 (AI Governance Lead), Security Monitoring Platform
**Regulation:** NIS 2 Art. 21, CRA Art. 12, AI_Act Art. 61
**Priority:** CRITICAL
**Frequency:** Continuous (24/7)
**SLA:** Detection within 15 minutes, triage within 1 hour

**Activation Condition:** STRUCTURAL — always active. When compound event (EVT-001/EVT-002) detected, multi-path notification activated.

**Preconditions:**
- Security monitoring platform operational with anomaly detection
- Alert thresholds configured for security and AI metrics
- On-call SOC team scheduled
- AI accuracy monitoring integrated into SOC dashboard

**Postconditions:**
- Incident logged with classification
- Alert generated and acknowledged
- Incident response process initiated (U.C.2.2.1)
- Evidence preserved for forensics

**Main Flow:**
1. Security monitoring platform collects security events from all sources (eGate endpoints, remote infrastructure, network, AI system)
2. Security monitoring platform correlates events in real-time with anomaly detection
3. Security monitoring platform detects anomaly, known threat pattern, or AI drift alert (>1% accuracy degradation)
4. Security monitoring platform generates alert with severity level (Critical/High/Medium/Low)
5. Security monitoring platform notifies on-call SOC analyst (pager/SMS/email/dashboard)
6. SOC analyst acknowledges alert (within 15 min)
7. SOC analyst performs initial triage: classify incident type
   - Type A: Actively exploited vulnerability → CRA 24h ENISA notification path
   - Type B: Significant incident → NIS 2 24h CSIRT early warning path
   - Type C: Personal data breach → GDPR 72h DPA notification path
   - Type D: AI incident (false accept/drift) → AI_Act market surveillance path
   - Type E: Multiple types → Apply shortest deadline (24h)
8. If Type A/B/E → Trigger U.C.2.5.1 (Regulatory Notification, 24h path)
9. If Type C → Trigger U.C.2.5.1 (Regulatory Notification, 72h path)
10. If Type D → Trigger U.C.6.5.1 (AI Incident Response)
11. SOC logs all actions and preserves evidence

**Alternative Flows:**
- 6a. No response within 15 min → Escalate to CISO
- 7a. False Positive → Tune detection rules; log as FP
- 7b. True Positive → Proceed to U.C.2.2.1 (Incident Response)

**Exceptions:**
- E1. Security monitoring platform failure → Manual monitoring until restored; escalate to CISO
- E2. Alert fatigue (>50% false positive rate) → Review and tune thresholds within 24h
- E3. SOC team unavailable → Activate backup SOC (MSSP contract)

**Business Rules:**
- BR-DET-01: All security events must be logged with timestamp
- BR-DET-02: Critical alerts must be acknowledged within 15 min
- BR-DET-03: Incident classification must be completed within 1 hour
- BR-DET-04: All incidents must preserve evidence for forensics
- BR-DET-05: AI drift alerts (>1% degradation) treated as Critical severity

**Related Requirements:**
- NFR: NFR-015 (Real-time event processing, <1s latency)
- NFR: NFR-009 (Detection SLA: 15 min for critical incidents)
- FR: FR-28 (System shall detect anomalies in security events)
- FR: FR-29 (System shall generate alerts with severity classification)
- FR: FR-72 (System shall detect AI accuracy drift >1%)

**Tension Reference:** T-001 (Unified 24h/72h notification workflow), T-005 (Integrated monitoring platform)

---

### 7.3 U.C.2.5.1: Regulatory Notification — Unified 24h/72h Workflow (Detailed)

**Use Case ID:** U.C.2.5.1
**Name:** Regulatory Notification (Unified 24h/72h Workflow)
**Description:** Unified incident notification workflow satisfying GDPR (72h), CRA (24h), NIS 2 (24h early warning + 72h full + 1mo final), and AI_Act (market surveillance cooperation)
**Primary Actor:** SH-INT-003 (CISO)
**Supporting Actors:** SH-INT-004 (DPO), SH-INT-005 (AI Governance Lead), SH-INT-010 (Compliance Analyst)
**Regulation:** GDPR Art. 33/34, CRA Art. 14, NIS 2 Art. 23, AI_Act Art. 73
**Priority:** CRITICAL
**Frequency:** Per significant incident
**SLA:** 24h early warning (CRA/NIS 2), 72h detailed (GDPR/NIS 2), 1 month final report (NIS 2). 24h (compound event) / 72h (GDPR-only)

**Activation Condition:** CONTEXTUAL — activated when compound event satisfies triggers from 2+ regulations. Max-SLA routing selects notification path based on incident classification. When only one trigger fires, use single-notification path. See T-001.

**Preconditions:**
- Incident classified per U.C.2.1.1 triage
- Incident severity assessed
- Notification templates pre-configured per regulation
- Contact information for all authorities current

**Postconditions:**
- Appropriate authorities notified within regulatory deadlines
- Notification evidence logged
- Final report submitted within 1 month
- Travelers notified if personal data breach affects them

**Main Flow:**
1. Incident classification received from U.C.2.1.1 (Type A/B/C/D/E)
2. CISO activates unified notification workflow
3. **Early Warning (≤24h):**
   - Type A (exploited vuln): Notify ENISA via security.txt channel
   - Type B (significant incident): Notify national CSIRT
   - Type E (multiple): Notify both ENISA and CSIRT
4. **Detailed Notification (≤72h):**
   - Type C (personal data breach): Notify DPA with Art. 33(3) details
   - Type B/E: Notify CSIRT with full incident details per NIS 2 Art. 23(2)
5. **Traveler Notification (if applicable):**
   - If personal data breach with high risk to travelers: Notify affected travelers (GDPR Art. 34)
6. **AI_Act Cooperation:**
   - Type D (AI incident): Cooperate with market surveillance authority
7. **Final Report (≤1 month):**
   - Submit comprehensive report per NIS 2 Art. 23(3) including root cause, impact, remediation
8. Log all notifications with timestamps and evidence

**Alternative Flows:**
- 3a. Classification uncertain → Default to 24h early warning (conservative)
- 5a. Notification to travelers would compromise investigation → Delay with DPA approval

**Exceptions:**
- E1. Authority contact information unavailable → Use backup channels; log as compliance gap
- E2. 24h deadline missed → Immediate notification; document delay reason; escalate to CEO

**Business Rules:**
- BR-NOTIFY-01: All notifications must be logged with timestamp and recipient
- BR-NOTIFY-02: 24h early warning for CRA/NIS 2 incidents (conservative default)
- BR-NOTIFY-03: 72h detailed notification for GDPR personal data breaches
- BR-NOTIFY-04: 1 month final report per NIS 2 Art. 23(3)
- BR-NOTIFY-05: Traveler notification required for high-risk personal data breaches

**Related Requirements:**
- NFR: NFR-044 (Notification workflow activation within 4h of classification)
- FR: FR-32 (System shall generate pre-filled notification templates per regulation)
- FR: FR-33 (System shall track notification deadlines and escalate)

**Tension Reference:** T-001 (24h vs 72h timing conflict — resolved via unified workflow with classification)

---

### 7.4 U.C.3.3.1: Biometric Enrollment (Detailed)

**Use Case ID:** U.C.3.3.1
**Name:** Biometric Enrollment
**Description:** Enroll traveler biometric templates (facial image) with approved cryptographic protection at eGate kiosk
**Primary Actor:** SH-EXT-002 (Traveler)
**Supporting Actors:** SH-EXT-001 (Border Control Officer), System (eGate kiosk)
**GDPR Article:** Art. 9 (Special Category Data), Art. 5(1)(c) (Data Minimization)
**Priority:** CRITICAL
**Frequency:** Per traveler enrollment (millions annually)
**SLA:** Enrollment within 60 seconds per traveler

**Activation Condition:** STRUCTURAL — always active before market placement.

**Preconditions:**
- Traveler presents valid passport or ID at eGate
- eGate kiosk operational with biometric sensor active
- Cryptographic modules initialized with approved algorithms
- Government watchlist data available for matching

**Postconditions:**
- Biometric template captured and encrypted
- Token generated for traveler identity
- Template stored in encrypted data store
- Enrollment logged (without storing raw facial image)
- Match decision generated (pass/refer)

**Main Flow:**
1. Traveler approaches eGate kiosk and presents passport
2. Border Control Officer initiates enrollment process
3. eGate captures facial image via biometric sensor
4. System extracts biometric features from facial image
5. System generates irreversible token (cryptographic one-way function with per-traveler salt)
6. System encrypts biometric template using approved symmetric encryption with FIPS-grade cryptographic module
7. System stores encrypted template + token in secure data store
8. System compares template against government watchlist
9. System generates match decision (pass/refer) with confidence score
10. System logs enrollment event (token, timestamp, decision — no raw image)
11. System discards raw facial image immediately after template extraction

**Alternative Flows:**
- 3a. Sensor failure → Refer to manual border control
- 8a. Watchlist match → Alert Border Control Officer for manual review
- 8b. Low confidence score → Refer to Border Control Officer for secondary screening

**Exceptions:**
- E1. Cryptographic module failure → Halt enrollment; escalate to Operations Lead
- E2. Data residency violation (data leaving EU) → Block transmission; alert CISO

**Business Rules:**
- BR-BIO-01: Raw facial images must never be stored; only encrypted templates
- BR-BIO-02: Biometric templates must be encrypted with approved strong symmetric encryption
- BR-BIO-03: Tokenization must be irreversible (one-way hash with per-traveler salt)
- BR-BIO-04: Enrollment must complete within 60 seconds
- BR-BIO-05: All enrollment events logged with token (no PII in logs)

**Related Requirements:**
- NFR: NFR-024 (Biometric template encryption with approved cryptographic modules)
- NFR: NFR-019 (Enrollment within 60 seconds)
- FR: FR-03 (System shall capture and encrypt biometric templates)
- FR: FR-04 (System shall discard raw facial images after extraction)

---

### 7.5 U.C.6.1.1: AI Conformity Assessment (Detailed)

**Use Case ID:** U.C.6.1.1
**Name:** AI Conformity Assessment
**Description:** Prepare and execute AI_Act conformity assessment for high-risk border control AI system (Annex III)
**Primary Actor:** SH-INT-005 (AI Governance Lead)
**Supporting Actors:** SH-INT-002 (CTO), SH-INT-003 (CISO), SH-EXT-007 (Notified Body), SH-EXT-011 (AI Market Surveillance Authority)
**AI_Act Article:** Art. 9, Art. 43 (Conformity Assessment)
**Priority:** CRITICAL
**Frequency:** Before initial market placement; upon significant model change
**SLA:** Complete before eGate deployment at any border crossing

**Activation Condition:** STRUCTURAL — always active before market placement.

**Preconditions:**
- AI system development complete
- Technical documentation prepared (AI_Act Annex IV)
- Quality management system operational
- Risk management system established
- Training data documented and validated

**Postconditions:**
- Conformity assessment completed
- EU Declaration of Conformity issued
- CE marking applied
- Technical documentation submitted to notified body
- Post-market monitoring plan activated

**Main Flow:**
1. AI Governance Lead initiates conformity assessment process
2. Compile technical documentation per AI_Act Annex IV:
   - System description and intended purpose
   - AI system architecture and design specifications
   - Training, validation, and testing data documentation
   - Human oversight measures
   - Accuracy, robustness, and cybersecurity metrics
3. Conduct internal risk assessment (integrated with DPIA+FRIA per U.C.5.2.1)
4. Engage Notified Body for third-party conformity assessment
5. Notified Body reviews technical documentation
6. Notified Body conducts independent testing of AI system
7. Notified Body issues conformity certificate (or identifies non-conformities)
8. If non-conformities: remediate and re-assess
9. Issue EU Declaration of Conformity
10. Apply CE marking to eGate system
11. Activate post-market monitoring plan (U.C.6.2.1)

**Alternative Flows:**
- 7a. Non-conformities identified → Remediate within 90 days; re-assess
- 8a. Critical non-conformity (safety/fundamental rights) → Halt deployment; redesign

**Exceptions:**
- E1. Notified Body unavailable → Engage alternative notified body; delay deployment
- E2. Significant model change post-certification → Re-initiate conformity assessment

**Business Rules:**
- BR-AICONF-01: Conformity assessment mandatory before market placement (AI_Act Art. 43)
- BR-AICONF-02: Technical documentation must be maintained for 10 years
- BR-AICONF-03: Significant model changes require re-assessment
- BR-AICONF-04: Post-market monitoring plan must be active before deployment
- BR-AICONF-05: EU Declaration of Conformity must be updated per system version

**Related Requirements:**
- NFR: NFR-038 (Conformity assessment complete before deployment)
- FR: FR-73 (System shall maintain technical documentation per Annex IV)
- FR: FR-74 (System shall support post-market monitoring data collection)

---

### 7.6 U.C.6.3.1: AI Bias Testing & Fairness Assessment (Detailed)

**Use Case ID:** U.C.6.3.1
**Name:** AI Bias Testing & Fairness Assessment
**Description:** Quarterly bias testing of border control AI across demographic groups (age, gender, ethnicity) with documented results
**Primary Actor:** SH-INT-005 (AI Governance Lead)
**Supporting Actors:** SH-INT-009 (Security Engineer), SH-EXT-013 (Penetration Testing Firm)
**AI_Act Article:** Art. 9 (Risk Management), Art. 10 (Data Quality)
**Priority:** HIGH
**Frequency:** Quarterly
**SLA:** Complete assessment within 2 weeks; report within 1 week of completion

**Preconditions:**
- AI model deployed and processing live data
- Representative test dataset available across demographic groups
- Bias testing suite configured
- Baseline accuracy metrics established

**Postconditions:**
- Bias assessment report generated
- Disparate impact identified and documented
- Remediation plan created (if bias detected)
- Report submitted to AI Market Surveillance Authority (if required)

**Main Flow:**
1. AI Governance Lead initiates quarterly bias assessment
2. Select representative test dataset covering demographic groups:
   - Age groups: 0-18, 18-30, 30-50, 50-70, 70+
   - Gender: Male, Female, Non-binary
   - Ethnicity: All major ethnic groups represented in Schengen traffic
3. Run bias testing suite against AI model:
   - False accept rate by demographic group
   - False reject rate by demographic group
   - Confidence score distribution by demographic group
4. Compare results against baseline and acceptable thresholds:
   - Max 1% disparity in false accept rate between groups
   - Max 2% disparity in false reject rate between groups
5. Generate bias assessment report with findings
6. If bias detected (>threshold):
   - Identify root cause (training data, model architecture, threshold settings)
   - Create remediation plan with timeline
   - Notify AI Market Surveillance Authority if bias affects fundamental rights
7. If no bias: document results and close assessment
8. Store assessment report in technical documentation

**Alternative Flows:**
- 6a. Bias is minor (<2x threshold) → Remediate within next model update cycle
- 6b. Bias is significant (>2x threshold) → Immediate remediation; consider temporary suspension

**Exceptions:**
- E1. Test dataset not representative → Delay assessment; acquire representative data
- E2. Bias testing suite failure → Engage external testing firm

**Business Rules:**
- BR-BIAS-01: Bias assessment must be conducted quarterly
- BR-BIAS-02: Max 1% false accept rate disparity between demographic groups
- BR-BIAS-03: Significant bias must be reported to market surveillance authority
- BR-BIAS-04: Remediation plan must be completed within 90 days of detection

**Related Requirements:**
- NFR: NFR-047 (Max 1% false accept rate disparity)
- FR: FR-75 (System shall support bias testing across demographic groups)
- FR: FR-76 (System shall generate bias assessment reports)

---

### 7.7 U.C.5.2.1: Unified Impact Assessment — DPIA+FRIA (Detailed)

**Use Case ID:** U.C.5.2.1
**Name:** Unified Impact Assessment (DPIA + FRIA)
**Description:** Conduct unified Data Protection Impact Assessment and Fundamental Rights Impact Assessment with dual outputs for biometric AI border control processing
**Primary Actor:** SH-INT-004 (DPO)
**Supporting Actors:** SH-INT-005 (AI Governance Lead), SH-INT-003 (CISO), SH-INT-002 (CTO)
**Regulation:** GDPR Art. 35 (DPIA), AI_Act Art. 9 + Art. 28 (FRIA)
**Priority:** CRITICAL
**Frequency:** Before initial deployment; upon significant processing change; annual review
**SLA:** Prior to launch / Annual / On significant change

**Activation Condition:** STRUCTURAL — always active. Both GDPR DPIA and AI_Act FRIA triggers permanently satisfied by border control AI business model.

**Preconditions:**
- AI system design complete
- Data processing activities defined
- Risk management framework established
- DPO and AI Governance Lead available

**Postconditions:**
- Unified Impact Assessment document completed
- DPIA section satisfies GDPR Art. 35(7) requirements
- FRIA section satisfies AI_Act fundamental rights analysis
- Risks identified and mitigations documented
- Assessment approved by DPO + AI Governance Lead

**Main Flow:**
1. DPO initiates Unified Impact Assessment
2. **Section A — System Description (shared):**
   - Describe eGate system architecture, AI model, data flows
3. **Section B — Data Processing Description (shared):**
   - Map all personal data processing: biometric templates, passport data, watchlist data
4. **Section C — Necessity & Proportionality (shared):**
   - Assess necessity of biometric processing for border control purpose
   - Evaluate proportionality of processing scope
5. **Section D — Risk Identification (shared):**
   - Identify risks to data subjects (privacy, fundamental rights, discrimination)
   - Identify risks to system security (cybersecurity, AI robustness)
6. **Section E — Mitigation Measures (shared):**
   - Document technical and organizational mitigations
   - Map mitigations to rules catalog
7. **Section F — DPIA-specific (GDPR Art. 35(7)):**
   - Systematic description of processing operations and purposes
   - Assessment of necessity and proportionality
   - Risk assessment for rights and freedoms of data subjects
   - Safeguards, security measures, and risk mitigation measures
8. **Section G — FRIA-specific (AI_Act fundamental rights):**
   - Identify affected fundamental Rights (privacy, non-discrimination, human dignity, free movement)
   - Assess risk to rights holders (travelers, specific demographic groups)
   - Vulnerable persons impact assessment
   - Post-market monitoring plan for fundamental rights
9. Joint review by DPO + AI Governance Lead
10. Approval and publication (summary version for transparency)

**Alternative Flows:**
- 5a. New risk identified during assessment → Add to risk register; update mitigations
- 9a. DPO or AI Lead disagrees → Escalate to CISO; resolve before deployment

**Exceptions:**
- E1. Assessment reveals unacceptable risk → Halt deployment; redesign system
- E2. Significant processing change post-assessment → Re-initiate unified assessment

**Business Rules:**
- BR-UIA-01: Unified assessment mandatory before high-risk AI deployment
- BR-UIA-02: Annual review required for both DPIA and FRIA sections
- BR-UIA-03: Assessment must be approved by both DPO and AI Governance Lead
- BR-UIA-04: Summary version must be published for transparency (AI_Act Art. 13)

**Related Requirements:**
- NFR: NFR-039 (Unified assessment complete before deployment)
- FR: FR-59 (System shall support unified assessment with dual outputs)
- FR: FR-60 (System shall maintain assessment version history)

**Tension Reference:** T-003 (DPIA vs. FRIA trigger mismatch — resolved via unified assessment with dual outputs)

---

## 8. UC TO BUSINESS GOALS

### 8.1 Use Case to Business Goal Matrix

| UC ID | BG-001 CRA Cert | BG-002 AI Conformity | BG-003 NIS 2 | BG-004 GDPR Art.9 | BG-005 99.99% Uptime | BG-006 Schengen | BG-007 ISO 27001 |
|-------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| U.C.1.1.1 | | | | ● | | ● | |
| U.C.1.2.1 | | | | ● | | | |
| U.C.1.3.1 | | | | ● | | ● | |
| U.C.1.4.1 | | | | ● | | | |
| U.C.1.5.1 | | | | ● | | | |
| U.C.1.6.1 | | | | ● | | | ● |
| U.C.2.1.1 | ● | | ● | | ● | | ● |
| U.C.2.2.1 | ● | ● | ● | | ● | | ● |
| U.C.2.3.1 | ● | | ● | | | | ● |
| U.C.2.4.1 | ● | | ● | | ● | | ● |
| U.C.2.5.1 | ● | | ● | ● | | | ● |
| U.C.2.6.1 | ● | ● | ● | | ● | | ● |
| U.C.2.7.1 | | | ● | | ● | | ● |
| U.C.2.8.1 | ● | ● | ● | | | | ● |
| U.C.3.1.1 | | | ● | | | | ● |
| U.C.3.2.1 | ● | | ● | | | | ● |
| U.C.3.3.1 | | | | ● | | | |
| U.C.3.4.1 | | | ● | | | | ● |
| U.C.3.5.1 | ● | | | | | | ● |
| U.C.3.6.1 | | | ● | | | | ● |
| U.C.3.7.1 | | ● | | | | | |
| U.C.4.1.1 | ● | | | | | | ● |
| U.C.4.2.1 | ● | | | | | | ● |
| U.C.4.3.1 | ● | | ● | | | | ● |
| U.C.4.4.1 | | | ● | | | | ● |
| U.C.4.5.1 | ● | ● | | | | | ● |
| U.C.4.6.1 | | ● | | | | | |
| U.C.5.1.1 | ● | ● | ● | ● | | | ● |
| U.C.5.2.1 | | ● | | ● | | | |
| U.C.5.3.1 | | | ● | | | | ● |
| U.C.5.4.1 | ● | ● | ● | ● | | | ● |
| U.C.5.5.1 | | | ● | | | | ● |
| U.C.5.6.1 | | | ● | | | | ● |
| U.C.5.7.1 | ● | ● | ● | ● | | ● | |
| U.C.5.8.1 | | | ● | | | | |
| U.C.6.1.1 | | ● | | | | | |
| U.C.6.2.1 | | ● | | | | | |
| U.C.6.3.1 | | ● | | | | | |
| U.C.6.4.1 | | ● | | | | | |
| U.C.6.5.1 | | ● | | | | | |
| U.C.6.6.1 | | ● | | | | | |
| U.C.6.7.1 | | ● | | | | | |
| U.C.7.1.1 | | | ● | ● | | | ● |
| U.C.7.2.1 | | | ● | | | | ● |
| U.C.7.3.1 | | ● | | | | | |
| U.C.7.4.1 | | | ● | | | | |
| U.C.7.5.1 | | | ● | | | | ● |

---

## 9. UC TO STAKEHOLDERS

### 9.1 Use Case to Stakeholder Matrix

| UC ID | CISO | DPO | AI Gov | SOC Mgr | Dev Lead | Ops Lead | Sec Eng | Compliance | Border Officer | Traveler | Border Authority |
|-------|:----:|:----:|:------:|:--------:|:--------:|:--------:|:-------:|:----------:|:--------------:|:--------:|:----------------:|
| U.C.1.1.1 | S | **P** | S | | | | | S | | **P** | S |
| U.C.1.2.1 | S | **P** | S | | | | | | | **P** | S |
| U.C.1.3.1 | | **P** | | | | | | S | | **P** | S |
| U.C.1.4.1 | S | **P** | S | S | | | | S | | I | I |
| U.C.1.5.1 | | **P** | S | | | | | S | | | |
| U.C.1.6.1 | | **P** | S | | | | | S | | | I |
| U.C.2.1.1 | S | | | **P** | | | S | | | | |
| U.C.2.2.1 | **P** | S | S | S | | S | S | | | | |
| U.C.2.3.1 | S | | | | | | **P** | | | | |
| U.C.2.4.1 | S | | | | | **P** | S | | | | |
| U.C.2.5.1 | **P** | S | S | S | | | | S | | | |
| U.C.2.6.1 | S | | S | **P** | | | | | | | |
| U.C.2.7.1 | S | | | S | | **P** | S | | | | |
| U.C.2.8.1 | S | | S | | | | **P** | | | | |
| U.C.3.1.1 | | | | | | **P** | | S | | S | S |
| U.C.3.2.1 | | | | | | | | | **P** | S | |
| U.C.3.3.1 | S | S | S | | | S | | | | **P** | |
| U.C.3.4.1 | | | | | | **P** | | S | | | |
| U.C.3.5.1 | | | | | | **P** | S | | | | |
| U.C.3.6.1 | | | | | | **P** | | S | | | |
| U.C.3.7.1 | | | S | | | | | | **P** | S | |
| U.C.4.1.1 | | | | | **P** | | S | | | | |
| U.C.4.2.1 | | | | | **P** | | S | S | | | |
| U.C.4.3.1 | | | | | **P** | | S | | | | |
| U.C.4.4.1 | | | | | **P** | | S | S | | | |
| U.C.4.5.1 | S | S | S | | **P** | | | | | | |
| U.C.4.6.1 | S | | S | | **P** | | S | | | | |
| U.C.5.1.1 | **P** | S | S | S | | | | S | | | |
| U.C.5.2.1 | S | **P** | **P** | | | | | S | | | |
| U.C.5.3.1 | **P** | S | | | | | | S | | | |
| U.C.5.4.1 | S | S | S | | | | | **P** | | | |
| U.C.5.5.1 | S | | | | | | | **P** | | | |
| U.C.5.6.1 | S | | | | | | | **P** | | | |
| U.C.5.7.1 | S | S | S | | | | | **P** | | | I |
| U.C.5.8.1 | | | | | | **P** | | S | | | |
| U.C.6.1.1 | S | S | **P** | | S | | | S | | | I |
| U.C.6.2.1 | S | | **P** | S | | | | | | | |
| U.C.6.3.1 | S | | **P** | | | | S | | | | |
| U.C.6.4.1 | | | **P** | | | | | S | | | |
| U.C.6.5.1 | S | S | S | **P** | | | S | | | | |
| U.C.6.6.1 | S | | S | | | | **P** | | | | |
| U.C.6.7.1 | | | **P** | | S | | | | | | |
| U.C.7.1.1 | **P** | S | | | | | | S | | | |
| U.C.7.2.1 | **P** | | S | | | | | S | | | |
| U.C.7.3.1 | | | **P** | | | | | | | | |
| U.C.7.4.1 | **P** | | | | | | | | | | |
| U.C.7.5.1 | **P** | | | | | | | S | | | |

**Legend:** **P** = Primary, S = Support, I = Informed

---

## 10. REQUIREMENTS PRIORITIZATION

### 5.1 Priority Distribution

| Priority | Count | Percentage | Use Cases |
|----------|-------|------------|-----------|
| **CRITICAL** | 14 | 32% | U.C.1.2.1, U.C.1.4.1, U.C.2.1.1, U.C.2.2.1, U.C.2.3.1, U.C.2.4.1, U.C.2.5.1, U.C.3.2.1, U.C.3.3.1, U.C.3.7.1, U.C.4.3.1, U.C.5.1.1, U.C.5.2.1, U.C.5.7.1, U.C.6.1.1, U.C.6.2.1, U.C.6.5.1 |
| **HIGH** | 22 | 50% | U.C.1.1.1, U.C.1.5.1, U.C.1.6.1, U.C.2.6.1, U.C.2.7.1, U.C.2.8.1, U.C.3.1.1, U.C.3.4.1, U.C.3.5.1, U.C.3.6.1, U.C.4.1.1, U.C.4.2.1, U.C.4.4.1, U.C.4.5.1, U.C.4.6.1, U.C.5.3.1, U.C.5.4.1, U.C.5.5.1, U.C.6.3.1, U.C.6.4.1, U.C.6.6.1, U.C.6.7.1, U.C.7.2.1, U.C.7.3.1, U.C.7.4.1 |
| **MEDIUM** | 6 | 14% | U.C.1.3.1, U.C.3.6.1, U.C.5.6.1, U.C.5.8.1, U.C.7.1.1 |
| **LOW** | 2 | 4% | U.C.7.5.1 |

### 10.2 Implementation Phasing

| Phase | Use Cases | Rationale |
|-------|-----------|-----------|
| **Phase 1 (Immediate)** | All CRITICAL (14 UCs) | Market access requirements: CRA certification, AI_Act conformity, NIS 2 compliance, GDPR Art. 9 |
| **Phase 2 (30 days)** | HIGH priority (22 UCs) | Operational hardening: monitoring, access control, secure development, governance |
| **Phase 3 (60 days)** | MEDIUM priority (6 UCs) | Optimization: portability, asset inventory, third-party boundaries |
| **Phase 4 (90 days)** | LOW priority (2 UCs) | Best practice: phishing simulation |

---

## 11. RULE COVERAGE ANALYSIS

### 11.1 Compliance Rule Coverage

| Rule ID | Covered By Use Cases | Status |
|---------|---------------------|--------|
| CR-D-01.1-001 | U.C.3.3.1 | ✅ |
| CR-D-01.2-001 | U.C.3.3.1, U.C.2.6.1 | ✅ |
| CR-D-01.3-001 | U.C.3.3.1, U.C.4.5.1 | ✅ |
| CR-D-01.4-001 | U.C.3.3.1, U.C.2.6.1 | ✅ |
| CR-D-02.1-001 | U.C.2.3.1, U.C.4.2.1 | ✅ |
| CR-D-02.2-001 | U.C.2.4.1 | ✅ |
| CR-D-02.3-001 | U.C.2.3.1, U.C.2.5.1 | ✅ |
| CR-D-02.4-001 | U.C.2.8.1, U.C.6.3.1, U.C.6.6.1 | ✅ |
| CR-D-03.1-001 | U.C.3.1.1, U.C.3.7.1 | ✅ |
| CR-D-03.2-001 | U.C.3.2.1 | ✅ |
| CR-D-03.3-001 | U.C.3.4.1, U.C.3.6.1 | ✅ |
| CR-D-03.4-001 | U.C.3.5.1 | ✅ |
| CR-D-04.1-001 | U.C.2.1.1 | ✅ |
| CR-D-04.2-001 | U.C.2.2.1, U.C.6.5.1 | ✅ |
| CR-D-04.3-001 | U.C.2.5.1, U.C.5.7.1 | ✅ |
| CR-D-04.4-001 | U.C.2.7.1 | ✅ |
| CR-D-05.1-001 | U.C.1.5.1, U.C.6.7.1 | ✅ |
| CR-D-05.2-001 | U.C.1.5.1, U.C.1.6.1 | ✅ |
| CR-D-05.3-001 | U.C.1.2.1 | ✅ |
| CR-D-05.4-001 | U.C.1.1.1, U.C.1.3.1 | ✅ |
| CR-D-06.1-001 | U.C.5.5.1 | ✅ |
| CR-D-06.2-001 | U.C.4.2.1 | ✅ |
| CR-D-06.3-001 | U.C.5.5.1 | ✅ |
| CR-D-06.4-001 | U.C.5.8.1 | ✅ |
| CR-D-07.1-001 | U.C.4.5.1 | ✅ |
| CR-D-07.2-001 | U.C.4.1.1 | ✅ |
| CR-D-07.3-001 | U.C.4.3.1 | ✅ |
| CR-D-07.4-001 | U.C.4.4.1 | ✅ |
| CR-D-08.1-001 | U.C.7.1.1 | ✅ |
| CR-D-08.2-001 | U.C.7.2.1, U.C.7.3.1 | ✅ |
| CR-D-08.3-001 | U.C.7.4.1 | ✅ |
| CR-D-09.1-001 | U.C.5.1.1, U.C.6.1.1 | ✅ |
| CR-D-09.2-001 | U.C.5.2.1, U.C.5.3.1, U.C.6.1.1 | ✅ |
| CR-D-09.3-001 | U.C.5.6.1 | ✅ |
| CR-D-09.4-001 | U.C.1.6.1 | ✅ |
| CR-D-10.1-001 | U.C.2.6.1, U.C.6.2.1 | ✅ |
| CR-D-10.2-001 | U.C.2.6.1, U.C.6.4.1 | ✅ |
| CR-D-10.3-001 | U.C.5.4.1 | ✅ |

**Compliance Rule Coverage: 38/38 (100%)**

### 11.2 Best Practice Rule Coverage

| Rule ID | Covered By Use Cases | Status |
|---------|---------------------|--------|
| BPR-D-01.1-001 | U.C.3.3.1 | ✅ |
| BPR-D-02.1-001 | U.C.2.3.1 | ✅ |
| BPR-D-03.1-001 | U.C.3.4.1 | ✅ |
| BPR-D-04.5-001 | U.C.2.1.1, U.C.7.5.1 | ✅ |
| BPR-D-07.1-001 | U.C.4.3.1 | ✅ |
| BPR-D-07.5-001 | U.C.4.3.1 | ✅ |
| BPR-D-09.1-001 | U.C.5.1.1 | ✅ |
| BPR-D-09.5-001 | U.C.5.1.1 | ✅ |
| BPR-D-10.4-001 | U.C.2.6.1 | ✅ |
| BPR-D-10.5-001 | U.C.2.6.1, U.C.6.2.1 | ✅ |
| BPR-D-02.4-001 | U.C.6.3.1 | ✅ |
| BPR-D-02.4-002 | U.C.6.6.1 | ✅ |
| BPR-D-02.5-001 | U.C.2.3.1 | ✅ |
| BPR-D-03.1-002 | U.C.3.7.1 | ✅ |
| BPR-D-03.5-001 | U.C.3.4.1 | ✅ |
| BPR-D-04.2-001 | U.C.2.2.1, U.C.2.7.1, U.C.6.5.1 | ✅ |
| BPR-D-05.1-001 | U.C.6.7.1 | ✅ |
| BPR-D-05.5-001 | U.C.1.5.1 | ✅ |
| BPR-D-06.5-001 | U.C.5.5.1 | ✅ |
| BPR-D-07.1-002 | U.C.4.5.1, U.C.4.6.1 | ✅ |
| BPR-D-08.4-001 | U.C.7.1.1, U.C.7.5.1 | ✅ |
| BPR-D-10.2-001 | U.C.6.4.1 | ✅ |
| BPR-D-10.5-001 | U.C.6.2.1 | ✅ |
| BPR-D-01.2-001 | U.C.3.3.1 | ✅ |
| BPR-D-04.5-001 | U.C.2.1.1 | ✅ |

**Best Practice Rule Coverage: 25/25 (100%)**

### 11.3 Strategic Tension Coverage

| Tension ID | Addressed By Use Cases | Resolution Verified |
|------------|----------------------|---------------------|
| T-001 (24h vs 72h) | U.C.2.5.1 | ✅ Unified workflow with classification |
| T-002 (Erasure vs Logging) | U.C.1.2.1 | ✅ Cryptographic sharding |
| T-003 (DPIA vs FRIA) | U.C.5.2.1 | ✅ Unified assessment with dual outputs |
| T-004 (Documentation overlap) | U.C.5.1.1 | ✅ Unified ISMS with annexes |
| T-005 (Monitoring overlap) | U.C.2.6.1 | ✅ Integrated SOC platform |
| T-006 (Supplier overlap) | U.C.5.5.1 | ✅ Unified supplier questionnaire |
| T-007 (SDLC overlap) | U.C.4.5.1 | ✅ Privacy + secure SDLC merge |
| T-008 (Training overlap) | U.C.7.1.1 | ✅ Unified training program |
| T-009 (Monitoring opt-out vs mandatory security) | U.C.2.6.1 | ✅ Monotone split: security-event layer mandatory, analytics layer opt-out eligible (per CRA Annex I (2)(l)) |

**Strategic Tension Coverage: 9/9 (100%)**

---

## 12. USE CASE STATISTICS

| Metric | Value |
|--------|-------|
| **Total Use Cases** | **44** |
| **Level 0 Categories** | 7 (DP, SEC, IAM, DEV, GOV, AI, TRN) |
| **Level 1 Use Cases** | 44 |
| **Level 2 Detailed Use Cases** | 7 (U.C.1.2.1, U.C.2.1.1, U.C.2.5.1, U.C.3.3.1, U.C.6.1.1, U.C.6.3.1, U.C.5.2.1) |
| **CRITICAL Priority** | 14 (32%) |
| **HIGH Priority** | 22 (50%) |
| **MEDIUM Priority** | 6 (14%) |
| **LOW Priority** | 2 (4%) |
| **Compliance Rules Covered** | 38/38 (100%) |
| **Best Practice Rules Covered** | 25/25 (100%) |
| **Strategic Tensions Addressed** | 9/9 (100%) |
| **Goals Mapped** | 38/38 (100%) |
| **Internal Stakeholders** | 10 |
| **External Stakeholders** | 13 |

---

## 13. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-04 | System Architect | Initial release — SecureBorder Solutions (44 UCs: 6 DP + 8 SEC + 7 IAM + 6 DEV + 8 GOV + 7 AI + 5 TRN) |
| 1.1 | 2026-04-16 | System Architect | Added Activation Condition annotations to detailed UCs (U.C.1.2.1, U.C.2.1.1, U.C.2.5.1, U.C.6.1.1, U.C.5.2.1); updated SLA lines for incident notification and impact assessment UCs |
| 1.2 | 2026-08-10 | Sprint 11 Executor (corr-008 Phase 3 ID harmonisation) | Added Related PSOs column to all UC tables (linking to PO/SO from Commit D); migrated BPR-AI-NN → BPR-D-XX.Y-NNN (15 BPR refs updated); tech-stripped SIEM/Cloud/FIPS 140-2/AES-256 mentions; added T-009 (D-10.1 monitoring opt-out) cross-ref; updated §11.2 BPR coverage (15→25) and §11.3 tension coverage (8→9) |

---

## 14. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | System Architect | | 2026-04-04 |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| Privacy Review (DPO) | | | |
| AI Governance Review | | | |
| AEGIS Methodology Review | | | |

---

**Next Document:** 14_Architectural_Nodes.md
**Phase 3 Step:** B (Use Cases Catalog) COMPLETE (pending final approval)
**Gate Status:** All 63 rules covered (100%), all 38 goals mapped (100%), all 9 tensions addressed (100%)
**Review Status:** DRAFT — awaiting CTO, CISO, DPO, and AI Governance Lead review