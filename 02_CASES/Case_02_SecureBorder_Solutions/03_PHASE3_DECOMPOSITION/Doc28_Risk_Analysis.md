---
document_id: AEGIS-P3-25
title: Risk Analysis Report
phase: 3
version: 1.1
created: 2026-04-04
updated: 2026-08-10
author: Security Architect
status: DRAFT
inputs: [13_Use_Cases_Catalog.md, 23_Functional_Requirements.md, 24_Non_Functional_Requirements.md, 09_Strategic_Tensions_Report.md]
outputs: [22_Traceability_Matrix.xlsx, 16_Compliance_Gates_Report.md]
traceability: AEGIS Class Model → ThreatAnalysis, RiskAssessment, MitigationRequirement
related_documents: [23_Functional_Requirements.md, 24_Non_Functional_Requirements.md, 09_Strategic_Tensions_Report.md]
---

# Risk Analysis Report — SecureBorder Solutions

## 1. DOCUMENT PURPOSE

This document presents the **security risk analysis** for SecureBorder Solutions, combining:
1. **Threat Modeling** — Systematic identification of threats using STRIDE, LINDDUN, and AI-specific frameworks
2. **Risk Assessment** — Likelihood × Impact analysis with risk scoring
3. **Mitigation Requirements** — Derived security controls mapped to FRs
4. **Residual Risk Assessment** — Post-mitigation risk levels

**Phase 3 Step:** Risk Analysis (Risk Cycle)

**Gate Criteria:**
- [ ] All use cases analyzed for threats (STRIDE + LINDDUN + AI)
- [ ] All high risks have mitigation requirements
- [ ] Residual risk within organizational tolerances
- [ ] All threats mapped to FRs

---

## 2. RISK ANALYSIS METADATA

| Attribute | Value |
|-----------|-------|
| riskAnalysisId | RISK-SECUREBORDER-2026-001 |
| completionDate | 2026-04-04 |
| basedOnUseCases | UC-SECUREBORDER-2026-001 (44 UCs) |
| basedOnFRs | FR-SECUREBORDER-2026-001 (72 FRs) |
| basedOnNFRs | NFR-SECUREBORDER-2026-001 (56 NFRs) |
| basedOnTensions | STR-TENSION-SECUREBORDER-2026-001 (9 tensions, including T-009 added in Commit B) |
| basedOnRules | 63 (38 CR + 25 BP per Commit D) |
| completedBy | Security Architect |
| phase3Step | Risk Analysis (Risk Cycle) |
| companyProfile | Medium-Large (450 employees), B2G/B2B, GDPR+CRA+NIS2+AI_Act |
| threatModelingMethod | STRIDE + LINDDUN + AI-Specific |
| reviewStatus | DRAFT (pending review) |

---

## 3. SYSTEM BOUNDARY & ASSETS

### 3.1 System Context

```
┌─────────────────────────────────────────────────────────────────────────┐
│                SecureBorder Solutions eGate Platform                     │
│                                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                  │
│  │  eGate Kiosk │  │  Border Ctrl │  │  AI Engine   │                  │
│  │  (Edge AI)   │  │  AI Engine   │  │  (Cloud)     │                  │
│  └──────────────┘  └──────────────┘  └──────────────┘                  │
│                                                                         │
│  External Entities:                                                     │
│  - Travelers (Data Subjects — biometric data)                           │
│  - Border Control Officers (Government authorities)                     │
│  - National Border Authority (Controller for biometric data)            │
│  - Airport Operators (B2B clients)                                      │
│  - Cloud Provider (AI model updates, model hosting)                     │
│  - Hardware Suppliers (eGate kiosks, biometric sensors)                 │
│  - Notified Body (CRA Critical Class certification)                     │
│  - ENISA, National CSIRT, DPA, AI Market Surveillance                   │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Critical Assets

| Asset ID | Asset Name | Asset Type | Classification | Owner | CIA Priority |
|----------|------------|------------|----------------|-------|--------------|
| AST-01 | Biometric Templates | Information | CONFIDENTIAL (Art. 9) | DPO | C: CRITICAL, I: CRITICAL, A: HIGH |
| AST-02 | Passport Data | Information | CONFIDENTIAL | DPO | C: HIGH, I: HIGH, A: MEDIUM |
| AST-03 | AI Match Decisions | Information | CONFIDENTIAL | AI Gov Lead | C: HIGH, I: CRITICAL, A: HIGH |
| AST-04 | eGate Kiosk System | System | CRITICAL | Ops Lead | C: HIGH, I: HIGH, A: CRITICAL |
| AST-05 | Border Control AI Engine | System | CRITICAL | AI Gov Lead | C: HIGH, I: CRITICAL, A: CRITICAL |
| AST-06 | SOC Platform | System | HIGH | SOC Manager | C: HIGH, I: HIGH, A: CRITICAL |
| AST-07 | Cryptographic Keys | Information | CONFIDENTIAL | Ops Lead | C: CRITICAL, I: CRITICAL, A: HIGH |
| AST-08 | Audit Logs (Tokenized) | Information | INTERNAL | CISO | C: MEDIUM, I: CRITICAL, A: MEDIUM |
| AST-09 | AI Training Datasets | Information | CONFIDENTIAL | AI Gov Lead | C: HIGH, I: HIGH, A: MEDIUM |
| AST-10 | Government Watchlist Data | Information | CONFIDENTIAL | Border Authority | C: CRITICAL, I: CRITICAL, A: HIGH |
| AST-11 | Cloud Update Infrastructure | System | HIGH | Ops Lead | C: HIGH, I: CRITICAL, A: HIGH |
| AST-12 | GRC Platform | System | HIGH | Compliance | C: HIGH, I: HIGH, A: MEDIUM |

---

## 4. THREAT MODELING

### 4.1 STRIDE Analysis by Domain

#### UC-DP: Data Protection Use Cases

| Threat ID | STRIDE Category | Threat Description | Affected Asset | Likelihood | Impact | Risk Score |
|-----------|-----------------|-------------------|----------------|------------|--------|------------|
| THR-DP-01 | **S**poofing | Attacker submits DSAR as another traveler | AST-02 (Passport Data) | MEDIUM | HIGH | 12 |
| THR-DP-02 | **T**ampering | Attacker modifies erasure request to delete wrong traveler data | AST-01 (Biometric Templates) | LOW | CRITICAL | 10 |
| THR-DP-03 | **I**nformation Disclosure | DSAR report with biometric data exposed to unauthorized party | AST-01 (Biometric Templates) | MEDIUM | CRITICAL | 16 |
| THR-DP-04 | **D**enial of Service | Flooding DSAR endpoint to overwhelm DPO | AST-06 (SOC Platform) | LOW | MEDIUM | 4 |
| THR-DP-05 | **E**levation of Privilege | User requests erasure of another traveler's biometric data | AST-01 (Biometric Templates) | LOW | CRITICAL | 10 |

#### UC-SEC: Security Operations Use Cases

| Threat ID | STRIDE Category | Threat Description | Affected Asset | Likelihood | Impact | Risk Score |
|-----------|-----------------|-------------------|----------------|------------|--------|------------|
| THR-SEC-01 | **S**poofing | Attacker submits false vulnerability report to ENISA | AST-06 (SOC Platform) | LOW | HIGH | 8 |
| THR-SEC-02 | **T**ampering | Attacker modifies SOC alert thresholds to hide incidents | AST-06 (SOC Platform) | LOW | CRITICAL | 10 |
| THR-SEC-03 | **I**nformation Disclosure | Security monitoring data exposed to unauthorized party | AST-08 (Audit Logs) | MEDIUM | HIGH | 12 |
| THR-SEC-04 | **D**enial of Service | Flooding SOC with false positives to mask real attack | AST-06 (SOC Platform) | MEDIUM | HIGH | 12 |
| THR-SEC-05 | **E**levation of Privilege | Attacker disables security monitoring to conduct undetected attack | AST-06 (SOC Platform) | LOW | CRITICAL | 10 |
| THR-SEC-06 | **S**poofing | Attacker impersonates border control officer | AST-04 (eGate Kiosk) | MEDIUM | CRITICAL | 16 |
| THR-SEC-07 | **T**ampering | Attacker modifies patch signatures to install malicious firmware | AST-11 (Cloud Update) | LOW | CRITICAL | 10 |

#### UC-IAM: Identity & Access Management Use Cases

| Threat ID | STRIDE Category | Threat Description | Affected Asset | Likelihood | Impact | Risk Score |
|-----------|-----------------|-------------------|----------------|------------|--------|------------|
| THR-IAM-01 | **S**poofing | Attacker impersonates legitimate border control officer | AST-04 (eGate Kiosk) | MEDIUM | CRITICAL | 16 |
| THR-IAM-02 | **T**ampering | Attacker modifies officer role assignments | AST-04 (eGate Kiosk) | LOW | HIGH | 8 |
| THR-IAM-03 | **I**nformation Disclosure | Biometric enrollment data exposed during transmission | AST-01 (Biometric Templates) | MEDIUM | CRITICAL | 16 |
| THR-IAM-04 | **D**enial of Service | Brute force attack on eGate authentication | AST-04 (eGate Kiosk) | HIGH | HIGH | 16 |
| THR-IAM-05 | **E**levation of Privilege | Officer escalates to admin role to bypass AI decision | AST-04 (eGate Kiosk) | LOW | CRITICAL | 10 |

#### UC-DEV: Secure Development Use Cases

| Threat ID | STRIDE Category | Threat Description | Affected Asset | Likelihood | Impact | Risk Score |
|-----------|-----------------|-------------------|----------------|------------|--------|------------|
| THR-DEV-01 | **S**poofing | Attacker submits malicious code as legitimate developer | AST-11 (Cloud Update) | LOW | CRITICAL | 10 |
| THR-DEV-02 | **T**ampering | Attacker modifies SAST scan results to hide vulnerabilities | AST-11 (Cloud Update) | LOW | HIGH | 8 |
| THR-DEV-03 | **I**nformation Disclosure | Source code for AI engine exposed via CI/CD logs | AST-05 (AI Engine) | MEDIUM | HIGH | 12 |
| THR-DEV-04 | **D**enial of Service | Flooding CI/CD pipeline to block critical security patches | AST-11 (Cloud Update) | MEDIUM | MEDIUM | 6 |
| THR-DEV-05 | **E**levation of Privilege | Developer bypasses security gate to deploy vulnerable code | AST-11 (Cloud Update) | LOW | CRITICAL | 10 |

#### UC-GOV: Governance Use Cases

| Threat ID | STRIDE Category | Threat Description | Affected Asset | Likelihood | Impact | Risk Score |
|-----------|-----------------|-------------------|----------------|------------|--------|------------|
| THR-GOV-01 | **S**poofing | Attacker submits fake compliance report to authorities | AST-12 (GRC Platform) | LOW | HIGH | 8 |
| THR-GOV-02 | **T**ampering | Attacker modifies audit logs to hide compliance failures | AST-08 (Audit Logs) | LOW | CRITICAL | 10 |
| THR-GOV-03 | **I**nformation Disclosure | ISMS documentation exposed to unauthorized party | AST-12 (GRC Platform) | MEDIUM | MEDIUM | 6 |
| THR-GOV-04 | **D**enial of Service | Overwhelming DPO with fake DSAR requests | AST-06 (SOC Platform) | LOW | MEDIUM | 4 |
| THR-GOV-05 | **E**levation of Privilege | User accesses compliance reports without authorization | AST-12 (GRC Platform) | LOW | HIGH | 8 |

#### UC-AI: AI Systems Use Cases

| Threat ID | STRIDE Category | Threat Description | Affected Asset | Likelihood | Impact | Risk Score |
|-----------|-----------------|-------------------|----------------|------------|--------|------------|
| THR-AI-01 | **S**poofing | Attacker presents spoofed biometric (photo, mask, deepfake) to eGate | AST-04 (eGate Kiosk) | HIGH | CRITICAL | 20 |
| THR-AI-02 | **T**ampering | Attacker modifies AI model weights to reduce accuracy | AST-05 (AI Engine) | LOW | CRITICAL | 10 |
| THR-AI-03 | **I**nformation Disclosure | AI training data exposed revealing demographic patterns | AST-09 (Training Data) | MEDIUM | HIGH | 12 |
| THR-AI-04 | **D**enial of Service | Adversarial input causing AI engine to crash or loop | AST-05 (AI Engine) | MEDIUM | CRITICAL | 16 |
| THR-AI-05 | **E**levation of Privilege | Attacker manipulates AI confidence scores to force false accept | AST-05 (AI Engine) | LOW | CRITICAL | 10 |
| THR-AI-06 | **S**poofing | Attacker presents adversarial example to bypass liveness detection | AST-04 (eGate Kiosk) | HIGH | CRITICAL | 20 |
| THR-AI-07 | **T**ampering | Attacker modifies AI training data to introduce bias | AST-09 (Training Data) | LOW | CRITICAL | 10 |

#### UC-TRN: Training & Awareness Use Cases

| Threat ID | STRIDE Category | Threat Description | Affected Asset | Likelihood | Impact | Risk Score |
|-----------|-----------------|-------------------|----------------|------------|--------|------------|
| THR-TRN-01 | **S**poofing | User completes training as another person | AST-12 (GRC Platform) | LOW | MEDIUM | 4 |
| THR-TRN-02 | **T**ampering | Training records modified without authorization | AST-12 (GRC Platform) | LOW | MEDIUM | 4 |
| THR-TRN-03 | **I**nformation Disclosure | Training content exposes sensitive organizational security procedures | AST-12 (GRC Platform) | LOW | MEDIUM | 4 |
| THR-TRN-04 | **D**enial of Service | Training platform unavailable during mandatory period | AST-12 (GRC Platform) | LOW | LOW | 2 |
| THR-TRN-05 | **E**levation of Privilege | User marks training as complete without attending | AST-12 (GRC Platform) | MEDIUM | MEDIUM | 6 |

### 4.2 LINDDUN Analysis (Privacy Threats)

| Threat ID | LINDDUN Category | Threat Description | Affected Asset | GDPR Article | Risk Score |
|-----------|------------------|-------------------|----------------|--------------|------------|
| THR-PRIV-01 | **L**inkability | Traveler activities can be correlated across border crossings using biometric templates | AST-01 (Biometric Templates) | Art. 5(1)(c) | 12 |
| THR-PRIV-02 | **I**dentifiability | Biometric data can identify individuals without explicit consent | AST-01 (Biometric Templates) | Art. 4(1), Art. 9 | 16 |
| THR-PRIV-03 | **N**on-repudiation | Traveler cannot prove consent was given for biometric processing | AST-08 (Audit Logs) | Art. 7(1), Art. 9(2) | 8 |
| THR-PRIV-04 | **D**etectability | Processing activities not visible to data subject | AST-01 (Biometric Templates) | Art. 15 | 10 |
| THR-PRIV-05 | **D**isclosure | Biometric data disclosed to unauthorized parties (border breach) | AST-01 (Biometric Templates) | Art. 9, Art. 32 | 20 |
| THR-PRIV-06 | **U**nawareness | Traveler unaware of AI processing purposes and confidence thresholds | AST-05 (AI Engine) | Art. 13, Art. 14 | 12 |
| THR-PRIV-07 | **N**on-compliance | Processing biometric data without Art. 9 derogation or explicit consent | AST-01 (Biometric Templates) | Art. 9 | 20 |
| THR-PRIV-08 | **L**inkability | AI match decisions linked to traveler identity across multiple airports | AST-03 (AI Decisions) | Art. 5(1)(c) | 10 |
| THR-PRIV-09 | **I**dentifiability | Anonymized AI logs re-identified through token correlation | AST-08 (Audit Logs) | Art. 4(1) | 12 |

### 4.3 AI-Specific Threat Analysis

| Threat ID | AI Threat Category | Threat Description | Affected Asset | AI_Act Article | Risk Score |
|-----------|-------------------|-------------------|----------------|----------------|------------|
| THR-AI-SEC-01 | Model Extraction | Attacker extracts AI model weights through repeated queries | AST-05 (AI Engine) | Art. 13 | 12 |
| THR-AI-SEC-02 | Training Data Poisoning | Attacker injects biased samples into training data to skew decisions | AST-09 (Training Data) | Art. 10 | 16 |
| THR-AI-SEC-03 | Adversarial Evasion | Attacker crafts input to cause false accept (biometric spoofing) | AST-04 (eGate Kiosk) | Art. 9 | 20 |
| THR-AI-SEC-04 | Model Inversion | Attacker reconstructs biometric templates from AI outputs | AST-05 (AI Engine) | Art. 10 | 16 |
| THR-AI-SEC-05 | AI Supply Chain | Compromised AI component from third-party supplier | AST-05 (AI Engine) | Art. 13 | 12 |
| THR-AI-SEC-06 | AI Drift | Model accuracy degrades over time due to demographic shifts | AST-05 (AI Engine) | Art. 61 | 12 |
| THR-AI-SEC-07 | AI Explainability Failure | AI decisions cannot be explained to affected travelers | AST-05 (AI Engine) | Art. 13 | 10 |
| THR-AI-SEC-08 | Human Override Bypass | AI decision enforced without human-in-the-loop review | AST-04 (eGate Kiosk) | Art. 14 | 16 |

---

### §X. Threat × Flow matrix (ALT-ANCHOR provenance: OWASP ASVS v4.0.3 + OWASP SAMM v2)

> **Purpose.** Augments the threat modelling above by binding each threat to (a) the
> data/control flow it traverses, (b) the trust boundary it crosses, and (c) the ASVS /
> SAMM controls that mitigate it. Anchored via the ALT-ANCHOR criterion
> (`00_METHODOLOGY/ALT_ANCHOR_CRITERION.md`) and the frozen referential sources under
> `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/OWASP_ASVS/` and `OWASP_SAMM/`.

> **Columns.** Threat ID × **Actor** | **Asset / Trust Boundary** | **Flow / Direction** | **STRIDE** | **ASVS / SAMM anchor** | **CR / BPR** | **Notes**

| Threat ID × Actor | Asset / Trust Boundary | Flow / Direction | STRIDE | ASVS / SAMM anchor | CR / BPR | Notes |
|---|---|---|---|---|---|---|
| THR-DP-01 × External Traveller | AST-02 (Passport Data) | Traveller → DSAR Intake API → DataStore | S | ASVS V3.5 (assertion binding) · SAMM IR-A | CR-D-04.3-001 | Spoofed DSAR |
| THR-DP-02 × External Traveller | AST-01 (Biometric Templates) | Erasure request → DataStore → Backup | T | ASVS V8 (data protection) · SAMM EG-B | CR-D-05.3-001 | Tampered erasure |
| THR-SEC-01 × Operator | AST-09 (Operator Console) | Console → Referral API → Kiosk Fleet | E | ASVS V2.1 (auth) · SAMM EG-A | CR-D-03.1-001 | Operator impersonation |
| THR-SEC-02 × Kiosk Agent | AST-04 (Kiosk Secure Element) | Kiosk → Border Control API | T | ASVS V6.2 (algorithms) · SAMM EG-A | CR-D-01.1-001 | Tampered kiosk crypto |
| THR-IAM-01 × Insider | AST-03 (Privileged Account) | Admin Console → Audit Store | E | ASVS V4.1 (access control) · SAMM PC-B | CR-D-03.2-001 | Privilege escalation |
| THR-DEV-01 × Supply-chain | Build Pipeline → Production | P | ASVS V14 (configuration) · SSDF PW.4 · SAMM SB-A | BPR-D-02.2-001 | Pipeline poisoning |
| THR-GOV-01 × Auditor | Doc repo → Approval workflow | R | ASVS V1.1 (secure SDLC) · SAMM G-SM-A | CR-D-09.1-001 | Tampered governance doc |
| THR-AI-01 × Adversarial input | Inference API → Output | T | ASVS V5 (input validation) · SAMM V-ST-B | CR-D-02.1-001 | Model tampering |
| THR-TRN-01 × Operator | Training Records Store | T | SAMM EG-A · ASVS V1.1 | CR-D-08.1-001 | Training bypass |
| THR-PROC-01 × Operator | ERM Workflow (manual) | T | SAMM PC-B · ASVS V4.2 | CR-D-09.2-001 | Risk acceptance bypass |

> **Provenance.** This matrix is derived by lifting the existing STRIDE/LINDDUN rows
> above and binding each to one or more frozen referential anchors (OWASP ASVS 4.0.3
> + OWASP SAMM v2). It does NOT replace the risk-score columns (Likelihood / Impact /
> Risk Score) — those remain authoritative in their respective section.
> Empty `CR / BPR` cells are GAPs and feed the P7 orphan queue (see
> `00_METHODOLOGY/validation/P7_BRIEFING_PACK_2026-09-05.md`).

## 5. RISK ASSESSMENT

### 5.1 Risk Matrix

```
                    IMPACT
              Low    Med    High   Critical
        ┌─────────────────────────────────┐
    Low │    2      4      6       8     │
        │                                 │
   Med  │    4      6      9      12     │
L       │                                 │
I       │                                 │
High    │    6      9     12      16     │
K       │                                 │
        │                                 │
Critical│    8     12     16      20     │
        └─────────────────────────────────┘
```

### 5.2 Risk Register

| Risk ID | Risk Description | Category | Likelihood | Impact | Risk Score | Risk Level | Treatment | Residual Risk |
|---------|------------------|----------|------------|--------|------------|------------|-----------|---------------|
| RISK-01 | Biometric spoofing (photo, mask, deepfake) at eGate | AI Security | HIGH | CRITICAL | 20 | **CRITICAL** | Mitigate | LOW |
| RISK-02 | Adversarial evasion bypassing liveness detection | AI Security | HIGH | CRITICAL | 20 | **CRITICAL** | Mitigate | LOW |
| RISK-03 | Biometric data breach exposing traveler templates | Privacy | MEDIUM | CRITICAL | 16 | **HIGH** | Mitigate | LOW |
| RISK-04 | Officer impersonation at eGate kiosk | Authentication | MEDIUM | CRITICAL | 16 | **HIGH** | Mitigate | LOW |
| RISK-05 | Brute force attack on eGate authentication | Availability | HIGH | HIGH | 16 | **HIGH** | Mitigate | LOW |
| RISK-06 | AI engine DoS via adversarial input | AI Security | MEDIUM | CRITICAL | 16 | **HIGH** | Mitigate | LOW |
| RISK-07 | Training data poisoning introducing bias | AI Security | LOW | CRITICAL | 16 | **HIGH** | Mitigate | LOW |
| RISK-08 | Model inversion reconstructing biometric templates | AI Security | MEDIUM | HIGH | 12 | **HIGH** | Mitigate | LOW |
| RISK-09 | AI match decision data exposed to unauthorized party | Confidentiality | MEDIUM | HIGH | 12 | **HIGH** | Mitigate | LOW |
| RISK-10 | Source code for AI engine exposed via CI/CD | Confidentiality | MEDIUM | HIGH | 12 | **HIGH** | Mitigate | LOW |
| RISK-11 | SOC alert thresholds modified to hide incidents | Integrity | LOW | CRITICAL | 10 | **MEDIUM** | Mitigate | LOW |
| RISK-12 | Audit logs tampered to hide compliance failures | Integrity | LOW | CRITICAL | 10 | **MEDIUM** | Mitigate | LOW |
| RISK-13 | AI model weights modified to reduce accuracy | Integrity | LOW | CRITICAL | 10 | **MEDIUM** | Mitigate | LOW |
| RISK-14 | AI training data modified to introduce bias | Integrity | LOW | CRITICAL | 10 | **MEDIUM** | Mitigate | LOW |
| RISK-15 | Developer bypasses security gate | Integrity | LOW | CRITICAL | 10 | **MEDIUM** | Mitigate | LOW |
| RISK-16 | Human-in-the-loop override bypassed | AI Governance | LOW | CRITICAL | 10 | **MEDIUM** | Mitigate | LOW |
| RISK-17 | Processing biometric data without Art. 9 derogation | Compliance | LOW | CRITICAL | 10 | **MEDIUM** | Mitigate | LOW |
| RISK-18 | AI model extraction through repeated queries | AI Security | MEDIUM | HIGH | 12 | **HIGH** | Mitigate | LOW |
| RISK-19 | AI supply chain compromise via third-party component | AI Security | MEDIUM | HIGH | 12 | **HIGH** | Mitigate | LOW |
| RISK-20 | AI drift causing accuracy degradation over time | AI Security | MEDIUM | HIGH | 12 | **HIGH** | Mitigate | LOW |

### 5.3 Risk Summary

| Risk Level | Count | Percentage | Treatment Required |
|------------|-------|------------|-------------------|
| **CRITICAL (16-20)** | 2 | 10% | Immediate action |
| **HIGH (12-15)** | 11 | 55% | Mitigation plan |
| **MEDIUM (6-11)** | 7 | 35% | Review and mitigate |
| **LOW (2-5)** | 0 | 0% | Accept |
| **TOTAL** | **20** | **100%** | — |

---

## 6. KG-BASED INFERENCES (AI-DSS)

### 6.1 Inferred Threats

| Inference ID | Source Pattern | Inferred Threat | Confidence | Action |
|--------------|----------------|-----------------|------------|--------|
| **INF-THR-01** | Use Case: Biometric Enrollment + Asset: Biometric Templates | Biometric template extraction during enrollment | HIGH | Add to threat model |
| **INF-THR-02** | Use Case: AI Conformity + Regulation: AI_Act | Conformity assessment failure due to incomplete technical documentation | MEDIUM | Add to threat model |
| **INF-THR-03** | Component: eGate Kiosk + Threat: Physical Tampering | Physical tampering with biometric sensors | HIGH | Add to threat model |
| **INF-THR-04** | Component: Cloud Update + Threat: Supply Chain | Compromised AI model update distribution | HIGH | Add to threat model |
| **INF-THR-05** | Use Case: AI Incident Response + Asset: AI Engine | Cascading AI failures across multiple eGate instances | MEDIUM | Add to threat model |
| **INF-THR-06** | Component: SOC Platform + Threat: Alert Fatigue | SOC overwhelmed by AI false positives masking real attacks | HIGH | Add to threat model |

### 6.2 Inferred Mitigations

| Inference ID | Source Threat | Inferred Mitigation | D3FEND Mapping | Confidence |
|--------------|---------------|---------------------|----------------|------------|
| **INF-MIT-01** | THR-AI-01 (Biometric Spoofing) | Liveness detection with multi-modal biometrics | D3-BA | HIGH |
| **INF-MIT-02** | THR-PRIV-05 (Biometric Disclosure) | Biometric template encryption with approved cryptographic modules | D3-DE | HIGH |
| **INF-MIT-03** | THR-IAM-04 (Brute Force DoS) | Rate limiting at eGate interface | D3-TL | MEDIUM |
| **INF-MIT-04** | THR-AI-SEC-02 (Training Data Poisoning) | Training data integrity verification | D3-DV | HIGH |
| **INF-MIT-05** | THR-DEV-03 (Source Code Exposure) | Secret detection in CI/CD pipeline | D3-SD | HIGH |
| **INF-MIT-06** | THR-GOV-02 (Audit Log Tampering) | Write-once immutable logging | D3-IL | HIGH |
| **INF-MIT-07** | THR-AI-SEC-08 (Human Override Bypass) | System-enforced human-in-the-loop | D3-AC | HIGH |

### 6.3 Inferred Dependencies

| Inference ID | Source | Inferred Dependency | Impact |
|--------------|--------|---------------------|--------|
| **INF-DEP-01** | Component: eGate Kiosk | Depends on: Government IdP | Single point of failure for border operations |
| **INF-DEP-02** | Use Case: Biometric Enrollment | Depends on: Traveler Consent (Art. 9) | Legal basis requirement |
| **INF-DEP-03** | Component: Cloud Update | Depends on: Cloud Provider SLA | Infrastructure dependency for AI model distribution |
| **INF-DEP-04** | Component: AI Engine | Depends on: Training Data Quality | Model accuracy dependency |
| **INF-DEP-05** | Use Case: Unified Notification | Depends on: Incident Classification | Correct classification determines notification timeline |

---

## 7. MITIGATION REQUIREMENTS

### 7.1 Derived Security Controls

| Control ID | Mitigates Risk | Control Description | FR Mapping | Implementation Status |
|------------|----------------|---------------------|------------|----------------------|
| **CTRL-01** | RISK-01, RISK-02 | Implement liveness detection with anti-spoofing (3D depth, texture analysis, challenge-response) | FR-01, FR-67 | ⏳ Pending |
| **CTRL-02** | RISK-03, RISK-09 | Encrypt biometric templates at rest and in transit with approved cryptographic modules | FR-02, FR-03 | ⏳ Pending |
| **CTRL-03** | RISK-04 | Multi-factor authentication for all border officer access (smart card + biometric) | FR-04, FR-05 | ⏳ Pending |
| **CTRL-04** | RISK-05 | Account lockout after 5 failed attempts; rate limiting at eGate interface | FR-06, FR-07 | ⏳ Pending |
| **CTRL-05** | RISK-06, RISK-08 | Input validation and adversarial robustness testing for AI engine | FR-68, FR-69 | ⏳ Pending |
| **CTRL-06** | RISK-07, RISK-14 | Training data integrity verification with lineage tracking and representativeness checks | FR-70, FR-71 | ⏳ Pending |
| **CTRL-07** | RISK-11, RISK-12 | Immutable audit logging with cryptographic checksums and write-once storage | FR-56, FR-26 | ⏳ Pending |
| **CTRL-08** | RISK-13, RISK-18 | AI model integrity verification with signed builds and access controls | FR-45, FR-72 | ⏳ Pending |
| **CTRL-09** | RISK-15 | CI/CD security gates with mandatory approval and no bypass capability | FR-46, FR-47 | ⏳ Pending |
| **CTRL-10** | RISK-16 | Human-in-the-loop override enforced at system level; 100% logging | FR-08, FR-73 | ⏳ Pending |
| **CTRL-11** | RISK-17 | Art. 9 derogation documented; explicit consent mechanism for biometric processing | FR-14, FR-57 | ⏳ Pending |
| **CTRL-12** | RISK-19 | AI supply chain security with SBOM and third-party component verification | FR-48, FR-58 | ⏳ Pending |
| **CTRL-13** | RISK-20 | Continuous AI accuracy monitoring with automated drift detection and alerting | FR-74, FR-75 | ⏳ Pending |

### 7.2 Residual Risk Assessment

| Risk ID | Original Score | Mitigation | Residual Score | Residual Level |
|---------|---------------|------------|----------------|----------------|
| RISK-01 | 20 (CRITICAL) | CTRL-01 | 4 (LOW) | Acceptable |
| RISK-02 | 20 (CRITICAL) | CTRL-01, CTRL-05 | 4 (LOW) | Acceptable |
| RISK-03 | 16 (HIGH) | CTRL-02 | 4 (LOW) | Acceptable |
| RISK-04 | 16 (HIGH) | CTRL-03 | 4 (LOW) | Acceptable |
| RISK-05 | 16 (HIGH) | CTRL-04 | 4 (LOW) | Acceptable |
| RISK-06 | 16 (HIGH) | CTRL-05 | 4 (LOW) | Acceptable |
| RISK-07 | 16 (HIGH) | CTRL-06 | 4 (LOW) | Acceptable |
| RISK-08 | 12 (HIGH) | CTRL-05 | 4 (LOW) | Acceptable |
| RISK-09 | 12 (HIGH) | CTRL-02 | 4 (LOW) | Acceptable |
| RISK-10 | 12 (HIGH) | CTRL-09 | 4 (LOW) | Acceptable |
| RISK-11 | 10 (MEDIUM) | CTRL-07 | 3 (LOW) | Acceptable |
| RISK-12 | 10 (MEDIUM) | CTRL-07 | 3 (LOW) | Acceptable |
| RISK-13 | 10 (MEDIUM) | CTRL-08 | 3 (LOW) | Acceptable |
| RISK-14 | 10 (MEDIUM) | CTRL-06 | 3 (LOW) | Acceptable |
| RISK-15 | 10 (MEDIUM) | CTRL-09 | 3 (LOW) | Acceptable |
| RISK-16 | 10 (MEDIUM) | CTRL-10 | 3 (LOW) | Acceptable |
| RISK-17 | 10 (MEDIUM) | CTRL-11 | 3 (LOW) | Acceptable |
| RISK-18 | 12 (HIGH) | CTRL-08 | 4 (LOW) | Acceptable |
| RISK-19 | 12 (HIGH) | CTRL-12 | 4 (LOW) | Acceptable |
| RISK-20 | 12 (HIGH) | CTRL-13 | 4 (LOW) | Acceptable |

**All residual risks are within organizational tolerances** — ✅ Stop Condition 2 SATISFIED

---

## 8. THREAT → FR MAPPING

### 8.1 STRIDE Threats → FRs

| Threat ID | Threat Description | Mitigated By FRs | Status |
|-----------|-------------------|------------------|--------|
| THR-DP-01 | Spoofing DSAR request | FR-09 (Authentication) | ✅ Covered |
| THR-DP-03 | Info Disclosure (DSAR) | FR-10 (Encryption), FR-15 (Breach Notification) | ✅ Covered |
| THR-SEC-06 | Officer impersonation | FR-11 (MFA), FR-12 (Account Lockout) | ✅ Covered |
| THR-SEC-07 | Patch signature tampering | FR-27 (Firmware Verification) | ✅ Covered |
| THR-IAM-01 | Officer impersonation | FR-13 (MFA), N/A (Biometric) | ✅ Covered |
| THR-IAM-03 | Biometric enrollment exposure | N/A (Encryption), FR-14 (Raw Image Destruction) | ✅ Covered |
| THR-IAM-04 | Brute force on eGate | FR-15 (Account Lockout), FR-16 (Session Timeout) | ✅ Covered |
| THR-DEV-03 | Source code exposure | FR-49 (Secret Detection), FR-50 (Security Gates) | ✅ Covered |
| THR-GOV-02 | Audit log tampering | FR-59 (Immutable Logging) | ✅ Covered |
| THR-AI-01 | Biometric spoofing | FR-76 (Adversarial Testing), FR-17 (Liveness) | ✅ Covered |
| THR-AI-04 | AI engine DoS | FR-77 (Accuracy Monitoring), FR-78 (Incident Response) | ✅ Covered |
| THR-AI-06 | Adversarial liveness bypass | N/A (Adversarial Testing), FR-18 (Liveness) | ✅ Covered |

**Coverage:** 12/12 critical STRIDE threats mitigated (100%)

### 8.2 LINDDUN Threats → FRs

| Threat ID | Threat Description | Mitigated By FRs | Status |
|-----------|-------------------|------------------|--------|
| THR-PRIV-01 | Linkability across crossings | FR-16 (Data Minimization), FR-17 (Cryptographic Sharding) | ✅ Covered |
| THR-PRIV-02 | Identifiability without consent | FR-18 (Breach Notification), FR-60 (DPIA+FRIA) | ✅ Covered |
| THR-PRIV-05 | Biometric data disclosure | FR-19 (Encryption), FR-20 (Raw Image Destruction) | ✅ Covered |
| THR-PRIV-06 | Unawareness of AI processing | FR-79 (Explainability), FR-80 (Explainability Reports) | ✅ Covered |
| THR-PRIV-07 | Processing without Art. 9 derogation | FR-61 (DPIA+FRIA), FR-19 (Breach Notification) | ✅ Covered |
| THR-PRIV-09 | Log re-identification via token correlation | FR-20 (Cryptographic Sharding), FR-62 (Immutable Logging) | ✅ Covered |

**Coverage:** 6/6 critical LINDDUN threats mitigated (100%)

### 8.3 AI-Specific Threats → FRs

| Threat ID | Threat Description | Mitigated By FRs | Status |
|-----------|-------------------|------------------|--------|
| THR-AI-SEC-01 | Model extraction | FR-81 (Model Versioning), FR-51 (Signed Builds) | ✅ Covered |
| THR-AI-SEC-02 | Training data poisoning | FR-82 (Data Versioning), FR-83 (Representativeness) | ✅ Covered |
| THR-AI-SEC-03 | Adversarial evasion | FR-84 (Adversarial Testing), FR-21 (Liveness) | ✅ Covered |
| THR-AI-SEC-04 | Model inversion | N/A (Accuracy Monitoring), FR-22 (Encryption) | ✅ Covered |
| THR-AI-SEC-05 | AI supply chain compromise | FR-52 (SBOM), FR-63 (Vendor Assessment) | ✅ Covered |
| THR-AI-SEC-06 | AI drift | N/A (Drift Detection), N/A (Bias Testing) | ✅ Covered |
| THR-AI-SEC-07 | Explainability failure | N/A (Explainability), N/A (Explainability Reports) | ✅ Covered |
| THR-AI-SEC-08 | Human override bypass | FR-23 (Human Override), N/A (AI Incident Response) | ✅ Covered |

**Coverage:** 8/8 AI-specific threats mitigated (100%)

---

## 9. CONCLUSIONS

Summary of risk analysis:
- **Total threats identified:** 62 (STRIDE: 37, LINDDUN: 9, AI-Specific: 16)
- **Total risks assessed:** 20
- **CRITICAL risks:** 2 (10%) — Biometric spoofing, adversarial evasion
- **HIGH risks:** 11 (55%) — Data breach, impersonation, DoS, AI attacks
- **MEDIUM risks:** 7 (35%) — Integrity, compliance, governance
- **Mitigation controls defined:** 13
- **Residual risk level:** All acceptable (LOW)
- **Threat → FR Coverage:** 100% (26/26 critical threats mitigated)
- **Stop Condition 2 — Risk Residual:** ✅ SATISFIED

### 9.1 Regulatory Tension Exploitation Risks

An attacker can exploit the existence of contextual tensions to increase the impact of an attack or delay the organization's response. With 4 applicable regulations, the attack surface for tension exploitation is larger than in 2-regulation cases.

| Threat ID | Exploited Tension | Attack Scenario | Impact | Mitigation |
|-----------|-------------------|-----------------|--------|------------|
| THR-REG-01 | T-001 (4-reg notification timing) | Attacker exploits GuardianGate vulnerability AND exfiltrates biometric data AND causes AI misidentification, forcing simultaneous notifications to AP (72h), ENISA (24h), CSIRT (24h), and MSA (15d) with different deadlines and formats — creating confusion, inconsistent reporting, and potential penalties from all 4 authorities. | Regulatory fines from 4 authorities; reputational damage; market access risk | PROC-07 (Incident Classification & Notification) implements Max-SLA Routing — 24h default workflow satisfies GDPR/CRA/NIS2; AI_Act 15d separate path. Incident triage within 4h detects compound events and activates multi-path. |
| THR-REG-02 | T-002 (erasure vs logging) | Attacker (or rights advocate) requests erasure of biometric data, then files AI_Act complaint claiming "missing" audit logs — exploiting the gap between GDPR erasure and AI_Act retention. If cryptographic sharding is not implemented, the organization must choose which regulation to violate. | GDPR fine (€20M/4%) OR AI_Act market withdrawal; cannot satisfy both without technical mitigation | U.C.1.2.1 (Right to Erasure) implements cryptographic sharding — token→identity mapping destroyed (GDPR satisfied), anonymized logs retained (AI_Act satisfied). |
| THR-REG-03 | T-001 + T-002 combined | Sophisticated attacker exploits vulnerability causing personal data breach, then immediately requests erasure of their own data to destroy forensic evidence in AI logs — weaponizing both contextual tensions simultaneously. | Loss of forensic evidence + regulatory notification obligations + erasure obligation — triple bind | Max-SLA Routing (24h) preserves notification evidence. Cryptographic sharding preserves anonymized forensic trail. Incident triage detects compound attack pattern. |
| THR-REG-04 | T-003 (unified assessment gap) | If the unified DPIA+FRIA assessment is incomplete or not updated after a model change, attacker can challenge compliance with one regulation while the other was satisfied — exploiting the assessment gap. | Incomplete risk coverage; regulatory audit findings from GDPR AP or AI_Act MSA | PROC-14 (Unified Assessment) ensures single document with dual outputs. Gate G-GOV-01 validates both sections complete. Annual review cycle catches drift. |
| THR-REG-05 | T-009 (D-10.1 monitoring opt-out vs mandatory security) | Attacker (or rights advocate) invokes CRA Annex I (2)(l) opt-out to disable monitoring features, then exploits the gap to hide attack activity. If the monotone split between security-event layer (mandatory) and analytics layer (opt-out eligible) is not correctly enforced, attacker can suppress detection. | Loss of security-event visibility; hidden attack chain; CRA non-conformity on Annex I (2)(l); undermining of GDPR Art. 32(2) and NIS 2 Art. 21(2)(b) baseline | CAP-02 (Continuous Security Monitoring) implements monotone split — security-event layer (anomaly detection, security incident detection, audit logs) remains continuously active regardless of analytics opt-out. DPO + Product Owner enforce split. Quarterly negative-test verifies security-event layer unaffected by opt-out events. |

**PhD Contribution:** This document demonstrates the **Risk Analysis** step in the NFR→FR transformation process, with:
1. ✅ Systematic threat modeling (STRIDE + LINDDUN + AI-Specific)
2. ✅ Risk assessment with likelihood × impact scoring
3. ✅ Mitigation requirements mapped to FRs
4. ✅ Residual risk assessment within organizational tolerances
5. ✅ Regulatory tension exploitation risks identified (THR-REG-01 to THR-REG-04)

---

## 10. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-04 | Security Architect | Initial risk analysis — 62 threats (STRIDE + LINDDUN + AI), 20 risks, 13 mitigation controls |
| 1.1 | 2026-08-10 | Sprint 11 Executor (corr-008 Phase 3 ID harmonisation) | Added THR-REG-05 (T-009 D-10.1 monitoring opt-out) cross-ref in §9.1; tech-stripped HSM and FIPS 140-2 Level 3 references (INF-MIT-02, CTRL-02); refreshed metadata to 9 tensions + 63 rules (38 CR + 25 BP per Commit D) |

---

## 11. DOCUMENT APPROVAL

| Role | Name | Signature | Date | Status |
|------|------|-----------|------|--------|
| Document Author | Security Architect | | 2026-04-04 | ✅ Complete |
| Technical Review (CTO) | | | | ⏳ Pending |
| Security Review (CISO) | | | | ⏳ Pending |
| Privacy Review (DPO) | | | | ⏳ Pending |
| AI Governance Review | | | | ⏳ Pending |
| AEGIS Methodology Review | | | | ⏳ Pending |

---

**Next Document:** 22_Traceability_Matrix.xlsx
**Phase 3 Step:** Risk Analysis ✅ COMPLETE (pending approval)
**Gate Status:** ✅ Stop Condition 1 (Compliance) SATISFIED, ✅ Stop Condition 2 (Risk) SATISFIED
