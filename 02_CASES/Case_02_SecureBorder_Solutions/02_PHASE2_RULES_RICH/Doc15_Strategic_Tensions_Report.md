---
document_id: AEGIS-P2-09
title: Strategic Tensions Report
phase: 2
version: 1.1
created: 2026-04-03
updated: 2026-08-13
author: Compliance Lead
status: DRAFT
inputs: [Doc14_Obligation_Derivation.md, Doc11_Structured_Compliance_Matrix.md]
outputs: [Doc16_Privacy_Security_Goals.md]
traceability: AEGIS Class Model → StrategicTension, ConflictResolution classes
related_documents: 03_Design_Decisions_Log.md
---

# Strategic Tensions Report

## 1. DOCUMENT PURPOSE

This document consolidates the strategic tensions analysis (Step C1+C2+C3+C4+C5), detecting conflicts between obligations, documenting resolutions, and assigning risk owners.

**Alignment with Class Model:**
- `StrategicTension` - Detected conflicts between obligations
- `ConflictResolution` - Resolution strategies for each tension
- `RegulatoryObligation` - Source obligations in conflict

**Phase 2 Step:** C (Strategic Tensions Analysis)

**Gate Criteria:** All HIGH priority tensions resolved with documented rationale

---

## 2. STRATEGIC TENSIONS METADATA

| Attribute | Value |
|-----------|-------|
| tensionsReportId | STR-TENSION-SECUREBORDER-2026-001 |
| analysisDate | 2026-04-03 |
| basedOnObligationDerivation | DERIV-SECUREBORDER-2026-001 |
| analyzedBy | Compliance Lead |
| phase2Step | C1+C2+C3+C4+C5 |
| companyContextId | CC-SECUREBORDER-2026-001 |

---

## 3. TENSION CLASSIFICATION MODEL

### 3.1 Tension Nature: Structural vs Contextual

A critical distinction introduced in this analysis is **why** a tension exists and **when** it becomes active. Not all tensions are equal — some are permanent structural consequences of multi-regulation applicability; others only manifest when the same factual event satisfies triggers from multiple regulations.

| Dimension | Structural Tension | Contextual Tension |
|-----------|-------------------|-------------------|
| **Definition** | Exists whenever two or more regulations apply to the same sub-domain with differing requirements | Exists only when the same factual event simultaneously satisfies the trigger conditions of two or more regulations |
| **Activation** | Always active (permanent) | Conditional — depends on event overlap |
| **Resolution Timing** | Resolved once at design/planning phase | Resolved per-event via operational procedures |
| **Resolution Type** | `DESIGN_DECISION` — a permanent choice that stays | `OPERATIONAL_PROCEDURE` — a workflow activated when overlap occurs |
| **Example** | GDPR "appropriate measures" vs CRA "secure by default" in D-07.1 | GDPR 72h notification vs CRA 24h notification vs NIS 2 24h warning in D-04.3 (only when same event triggers multiple) |

### 3.2 Why This Distinction Matters

The tension between notification obligations is **not** about the same regulatory concept. Each regulation has a distinct trigger:

| Regulation | Trigger | Subject Obligated | Recipient |
|------------|---------|-------------------|-----------|
| **GDPR Art. 33** | Personal data breach (unauthorised access to personal data) | Controller | Data protection authority (AP) |
| **CRA Art. 14(1-2)** | Actively exploited vulnerability in a product with digital elements | Manufacturer | ENISA + CSIRT |
| **CRA Art. 14(3-5)** | Severe security incident affecting product users | Manufacturer | CSIRT + ENISA |
| **NIS 2 Art. 23** | Significant incident affecting service continuity | Essential/Important entity | National CSIRT / competent authority |
| **AI_Act Art. 73** | Serious incident involving high-risk AI system | Provider | Market surveillance authority |

**Scenario A — distinct events, no overlap.** A vulnerability exploited in SecureBorder's edge firmware may not involve personal data (GDPR does not trigger). A personal data breach may not involve an exploited product vulnerability (CRA does not trigger). In this case there is **no tension** — just parallel, independent obligations.

**Scenario B — same event, multiple triggers.** An attacker exploits a vulnerability in the GuardianGate AI model, causing a misidentification that results in a wrongful denial of entry AND exfiltrates biometric template data. The **same factual event** triggers GDPR (personal data breach → 72h), CRA (exploited vulnerability → 24h ENISA), NIS 2 (significant incident → 24h CSIRT), and AI_Act (serious AI incident → 15d/2d MSA). **This is the contextual tension.**

The tension is not "the clauses contradict" — it is "the same event generates multiple notification obligations with different deadlines, to different authorities, with different report formats."

### 3.3 Tension Types (Extended)

| Tension Type | Description | Detection Pattern | Examples |
|--------------|-------------|-------------------|----------|
| TEMPORAL_CONFLICT | Conflicting timeframes for the same or overlapping event | e.g., 72h vs. 24h vs. 15d notification | T-001 (contextual) |
| REQUIREMENT_CONFLICT | Contradictory requirements | e.g., Erasure vs. Logging retention | T-002 (contextual) |
| RESOURCE_CONFLICT | Competing for same resource | e.g., Budget, personnel, documentation overhead | T-004–T-008 (structural) |
| IMPLEMENTATION_CONFLICT | Incompatible implementations | e.g., Different encryption standards | — |
| INTENSITY_GAP | Different normative force | e.g., NI=2 vs NI=3 | — |
| FREQUENCY_MISMATCH | Different occurrence patterns | e.g., ONE_TIME vs CONTINUOUS | — |
| SCOPE_CONFLICT | Overlapping or competing scope definitions | e.g., User opt-out vs mandatory monitoring | T-009 (contextual) |
| TRIGGER_MISMATCH | Different trigger conditions | e.g., DPIA vs FRIA triggers | T-003 (structural) |

### 3.4 Tension Severity Levels

| Severity | Description | Action Required |
|----------|-------------|-----------------|
| CRITICAL | Direct contradiction, market access at risk | Mandatory resolution before Phase 2 Gate |
| HIGH | Significant conflict, compliance at risk | Documented resolution with mitigation strategy |
| MEDIUM | Potential conflict, manageable with controls | Track and monitor |
| LOW | Minor tension, operational resolution | Note in decision log |

### 3.5 Detection Criteria Applied to SecureBorder

| Criterion | Threshold | Applied to SecureBorder |
|-----------|-----------|------------------------|
| **Same Sub-Domain** | ≥2 regulations map to same D-XX.X | ✅ 35 sub-domains with multi-regulation coverage |
| **Different obligationType** | CONTINUOUS vs TRIGGERED vs ONE_TIME vs PERIODIC | ✅ Mixed types in 12 sub-domains |
| **Different obligatedParty** | CONTROLLER vs MANUFACTURER vs ESSENTIAL_ENTITY vs PROVIDER | ✅ 4 different parties across obligations |
| **Normative Intensity Delta** | NI_A - NI_B ≥ 0.5 | ✅ All obligations are NI=3.000 (no delta) |
| **Timing Mismatch** | Different deadlines (e.g., 72h vs 24h) | ✅ D-04.3 (24h CRA/NIS 2 vs 72h GDPR vs 15d AI_Act) |
| **Retention Mismatch** | Different retention periods | ✅ D-10.2 (AI_Act 6-month vs GDPR erasure) |

---

## 4. STRATEGIC TENSIONS CATALOG

### 4.1 Tension Classification Summary

| Tension ID | Tension Type | Severity | Nature | Always Active? | Overlap Condition | Resolution Type |
|------------|--------------|----------|--------|----------------|-------------------|-----------------|
| T-001 | TEMPORAL_CONFLICT | **CRITICAL** | **Contextual** | No | Same event = personal data breach AND/OR exploited vulnerability AND/OR significant incident AND/OR serious AI incident | OPERATIONAL_PROCEDURE |
| T-002 | REQUIREMENT_CONFLICT | **CRITICAL** | **Contextual** | No | Traveler requests erasure of personal data present in AI activity logs | OPERATIONAL_PROCEDURE |
| T-003 | TRIGGER_MISMATCH | HIGH | **Structural** | Yes | N/A — border control AI with biometric processing permanently satisfies both DPIA and FRIA triggers | DESIGN_DECISION |
| T-004 | RESOURCE_CONFLICT | HIGH | **Structural** | Yes | N/A — 4 regulations permanently require documentation | DESIGN_DECISION |
| T-005 | RESOURCE_CONFLICT | MEDIUM | **Structural** | Yes | N/A — continuous monitoring permanently required by 3 regulations | DESIGN_DECISION |
| T-006 | RESOURCE_CONFLICT | MEDIUM | **Structural** | Yes | N/A — supply chain obligations permanently overlap | DESIGN_DECISION |
| T-007 | RESOURCE_CONFLICT | MEDIUM | **Structural** | Yes | N/A — design phase permanently triggers both regs | DESIGN_DECISION |
| T-008 | RESOURCE_CONFLICT | LOW | **Structural** | Yes | N/A — training permanently required | DESIGN_DECISION |
| T-009 | SCOPE_CONFLICT | MEDIUM | **Contextual** | No | Traveler opts out of analytics while security-event monitoring remains mandatory | OPERATIONAL_PROCEDURE |

### 4.2 CRITICAL Priority Tensions

#### T-001: Incident Notification Timing Conflict — CONTEXTUAL

| Field | Value |
|-------|-------|
| **Tension ID** | T-001 |
| **Tension Type** | TEMPORAL_CONFLICT |
| **Tension Nature** | **CONTEXTUAL** — not always active; depends on event overlap |
| **Always Active?** | No |
| **Overlap Condition** | Same factual event constitutes a personal data breach (GDPR) AND/OR an actively exploited vulnerability (CRA) AND/OR a significant incident (NIS 2) AND/OR a serious AI incident (AI_Act) |
| **Severity** | CRITICAL |
| **Sub-Domain** | D-04.3 (Regulatory Notification) |
| **Conflicting Obligations** | OBL-D-04.3-001 (consolidated notification obligation) |
| **Source Regulations** | GDPR Art. 33(1) vs CRA Art. 14(1-2) & Art. 14(3-5) vs NIS 2 Art. 23(1) vs AI_Act Art. 73 |
| **Conflict Description** | Four regulations impose different incident/vulnerability notification timelines: GDPR requires breach notification to supervisory authority within **72 hours**. CRA has **two distinct flows** within Art. 14: (a) actively exploited vulnerabilities → 24h/72h/14-days-post-fix to ENISA (Art. 14(1-2)); (b) severe security incidents → 24h/72h/1-month to CSIRT/ENISA (Art. 14(3-5)). **Note:** CRA Art. 15 is "Voluntary reporting" — not a mandatory obligation. NIS 2 requires early warning to CSIRT within **24 hours** of significant incident + 72h notification + 1 month final report (Art. 23). AI_Act requires serious incident reporting within **15 days** (or **2 days** for widespread infringement) (Art. 73). |
| **Timing Details** | GDPR: 72h to SA<br>CRA Art.14(1-2) (vulns): 24h early warning → 72h notification → **14 days after corrective measure available**<br>CRA Art.14(3-5) (incidents): 24h early warning → 72h notification → **1 month** (Note: Art. 15 is **voluntary reporting**, not mandatory)<br>NIS 2: 24h early warning → 72h full notification → 1 month final report<br>AI_Act: 15 days (default) / 2 days (widespread) |
| **Risk if Unresolved** | Non-compliance with shortest deadline (24h) means non-compliance with CRA and NIS 2. Using 72h for all incidents violates CRA/NIS 2. Market access risk for CRA Critical Class certification. |
| **Detection Method** | Timing mismatch analysis on OBL-D-04.3-001 source clauses |

**Resolution Strategy: Max-SLA Routing with Incident Classification**

| Field | Value |
|-------|-------|
| **Resolution Type** | OPERATIONAL_PROCEDURE — activated per-incident when overlap condition is detected |
| **Resolution Description** | Implement a unified incident notification workflow that routes all incidents through the 24h channel (satisfying CRA and NIS 2 early warning), with extended 72h detailed notification for GDPR breaches. The 24h workflow is a superset that satisfies all regulations. |
| **Detection Mechanism** | Incident triage checklist within 4h: "Does this incident satisfy triggers from 2+ regulations?" → If YES, activate multi-path notification workflow |
| **Implementation Approach** | 1. **Classify** every security event within 4h: Is it (a) actively exploited vulnerability (CRA Art.14(1-2))? (b) severe security incident (CRA Art.14(3-5))? (c) significant incident (NIS 2)? (d) personal data breach (GDPR)? (e) AI serious incident (AI_Act)?<br>2. **Route** based on classification:<br>&nbsp;&nbsp;- (a) CRA vuln → 24h ENISA → 72h ENISA → 14d after corrective measure available<br>&nbsp;&nbsp;- (b) CRA incident → 24h CSIRT → 72h full → 1 month final<br>&nbsp;&nbsp;- (c) NIS 2 incident → 24h CSIRT early warning → 72h full → 1 month final<br>&nbsp;&nbsp;- (d) GDPR breach → 72h SA (+ 24h if also a/b/c)<br>&nbsp;&nbsp;- (e) AI incident → 15d MSA (2d if widespread)<br>3. **Default to 24h** when classification is uncertain (conservative approach) |
| **Workflow Diagram** | ```
Event Detected → Triage (≤4h)
  ├── Actively Exploited Vuln (CRA Art.14(1-2))?
  │   → 24h ENISA → 72h ENISA → 14d post-fix final
  ├── Severe Security Incident (CRA Art.14(3-5))?
  │   → 24h CSIRT → 72h full → 1mo final
  ├── Significant Incident (NIS 2)?
  │   → 24h CSIRT early warning → 72h full → 1mo final
  ├── Personal Data Breach (GDPR)?
  │   → 72h SA (+ 24h if also qualifies as above)
  ├── AI Serious Incident (AI_Act)?
  │   → 15d MSA (or 2d if widespread)
  └── Uncertain? → Default 24h Early Warning (covers all)
``` |
| **Satisfies GDPR?** | ✅ Yes — 72h notification still available; 24h early warning is additional (not conflicting) |
| **Satisfies CRA Art.14(1-2)?** | ✅ Yes — 24h ENISA notification for actively exploited vulnerabilities; 14-day final report post-fix |
| **Satisfies CRA Art.14(3-5)?** | ✅ Yes — 24h CSIRT early warning for severe incidents; 1-month final report |
| **Satisfies CRA Art.15?** | N/A — Art. 15 is voluntary reporting; no compliance obligation |
| **Satisfies NIS 2?** | ✅ Yes — 24h early warning + 72h notification + 1 month final report |
| **Satisfies AI_Act?** | ✅ Yes — 15-day (or 2-day for widespread) market surveillance notification |
| **Residual Risk** | LOW — Conservative default (24h for uncertain) ensures compliance; CRA 14-day post-fix clock is the most nuanced — must track when corrective measures become available |
| **Risk Owner** | CISO (incident response owner) |
| **Implementation Priority** | P1 (CRITICAL — required for market access) |

---

#### T-002: Data Erasure vs. AI Log Retention Conflict — CONTEXTUAL

| Field | Value |
|-------|-------|
| **Tension ID** | T-002 |
| **Tension Type** | REQUIREMENT_CONFLICT |
| **Tension Nature** | **CONTEXTUAL** — not always active; activated when a traveler requests erasure of personal data that exists in AI activity logs |
| **Always Active?** | No |
| **Overlap Condition** | Traveler submits erasure request (GDPR Art. 17 trigger) AND the personal data to be erased exists within AI activity logs retained under AI_Act Art. 19(1) (Art. 12 = transparency, NOT a D-05.3 participant) |
| **Severity** | CRITICAL |
| **Sub-Domain** | D-05.3 (Right to Erasure) vs D-10.2 (Audit Logging & Traceability) |
| **Conflicting Obligations** | OBL-D-05.3-001 (erasure) vs OBL-D-10.2-001 (logging with 6-month retention) |
| **Source Regulations** | GDPR Art. 17 (Right to Erasure) vs AI_Act Art. 19(1) (≥6-month log retention; Art. 12 covers transparency and is NOT a D-05.3 participant) |
| **Conflict Description** | GDPR Art. 17 grants data subjects the right to erasure of personal data "without undue delay" when requested. AI_Act Art. 19(1) requires retention of AI activity logs for a minimum of 6 months. For SecureBorder's border control AI system, match decisions, confidence scores, and operator actions are logged — and these logs contain personal data (biometric match results linked to traveler identity). Erasing personal data on request would destroy the audit trail required by AI_Act. **Note:** AI_Act Art. 12 covers transparency obligations for certain AI systems; it is NOT a D-05.3 (Right to Erasure) participant. Erasure is GDPR Art. 17 only; AI_Act Art. 19(1) governs LOGGING retention which is D-10.2, not D-05.3. |
| **Retention Details** | GDPR: Erasure "without undue delay" (typically interpreted as within 30 days)<br>AI_Act Art. 19(1): Minimum 6-month retention of AI logs (Art. 12 = transparency, not retention)<br>Government contracts: 10-year retention for audit trails |
| **Risk if Unresolved** | GDPR violation: fines up to €20M or 4% global revenue. AI_Act violation: withdrawal from market, conformity certificate suspension. Both are market access risks. | |
| **Detection Method** | Cross-sub-domain analysis: D-05.3 (erasure) vs D-10.2 (logging) retention requirements |

**Resolution Strategy: Cryptographic Sharding with Anonymization**

| Field | Value |
|-------|-------|
| **Resolution Type** | OPERATIONAL_PROCEDURE (Cryptographic Sharding) — activated per-erasure-request when personal data exists in AI logs |
| **Resolution Description** | Implement cryptographic sharding: separate personal identifiers from AI activity logs using tokenization. When erasure is requested, destroy the token-to-identity mapping while retaining the anonymized AI activity log. The log remains useful for AI_Act compliance (accuracy monitoring, bias detection, post-market surveillance) without containing personal data. |
| **Implementation Approach** | 1. **Tokenize** at ingestion: Replace traveler identity with irreversible token in AI logs<br>2. **Store mapping separately**: Token→Identity mapping in encrypted, access-controlled store with separate retention policy<br>3. **On erasure request**: Destroy token→identity mapping (satisfies GDPR Art. 17)<br>4. **Retain anonymized logs**: AI activity logs with tokens only (satisfies AI_Act Art. 19(1) ≥6-month retention floor)<br>5. **Government data**: For government-contracted processing (where SecureBorder is processor), erasure requests go to the government authority (controller); SecureBorder maintains logs per contract terms |
| **Data Flow** | ```
Traveler → [Facial Image] → AI Match → [Token: T-XXXX] → Log Entry
Token T-XXXX → [Encrypted Mapping] → Traveler Identity (separate store)

On Erasure Request:
  Destroy: Token→Identity mapping
  Retain: Anonymized log entries (T-XXXX only, no PII)
``` |
| **Satisfies GDPR?** | ✅ Yes — Personal data (identity mapping) is erased; anonymized logs are no longer personal data |
| **Satisfies AI_Act?** | ✅ Yes — AI activity logs retained for 6+ months with full traceability (token-based) |
| **Satisfies Government Contracts?** | ✅ Yes — Government retains identity mapping as controller; SecureBorder maintains anonymized logs |
| **Residual Risk** | LOW — Tokenization must be truly irreversible; use one-way hash with per-traveler salt |
| **Risk Owner** | DPO (GDPR compliance) + AI Governance Lead (AI_Act compliance) |
| **Implementation Priority** | P1 (CRITICAL — both regulations carry market access risk) |

---

#### T-003: DPIA vs. FRIA Trigger Mismatch — STRUCTURAL

| Field | Value |
|-------|-------|
| **Tension ID** | T-003 |
| **Tension Type** | TRIGGER_MISMATCH |
| **Tension Nature** | **STRUCTURAL** — always active when both GDPR and AI_Act apply |
| **Always Active?** | Yes |
| **Overlap Condition** | N/A — border control AI processing biometric data permanently satisfies both GDPR DPIA trigger (high-risk processing, Art. 35) and AI_Act FRIA trigger (high-risk AI system, Art. 9). These triggers are permanently satisfied by SecureBorder's business model. |
| **Severity** | HIGH |
| **Sub-Domain** | D-09.2 (Impact & Risk Assessments) |
| **Conflicting Obligations** | OBL-D-09.2-001 (consolidated impact assessment obligation) |
| **Source Regulations** | GDPR Art. 35 (DPIA) vs AI_Act Art. 9 + Art. 28 (FRIA — Fundamental Rights Impact Assessment) |
| **Conflict Description** | GDPR DPIA is triggered by high-risk personal data processing (Art. 35), particularly large-scale processing of special category data (biometrics — Art. 9). AI_Act FRIA is triggered by placement of high-risk AI systems on the market (Art. 9) and requires ongoing fundamental rights monitoring (Art. 28). Both assessments cover overlapping ground (privacy impact, data protection, risk to individuals) but have different triggers, scopes, and update frequencies. For SecureBorder, both are mandatory: biometric processing triggers DPIA, and border control AI triggers FRIA. |
| **Trigger Details** | GDPR DPIA: Triggered by high-risk processing (ONE_TIME before processing begins, then reviewed when processing changes)<br>AI_Act FRIA: Triggered by high-risk AI placement (ONE_TIME before market placement, then ongoing post-market monitoring) |
| **Risk if Unresolved** | Duplicate effort, inconsistent assessments, audit confusion. Missing either assessment results in non-compliance. |
| **Detection Method** | Same sub-domain (D-09.2), different trigger conditions, overlapping scope |

**Resolution Strategy: Unified Assessment with Dual Outputs**

| Field | Value |
|-------|-------|
| **Resolution Type** | DESIGN_DECISION — resolved once at process design level |
| **Resolution Description** | Create a single unified assessment process that produces both DPIA and FRIA outputs. The unified assessment shares common sections (system description, data flows, risk identification, mitigation measures) while maintaining regulation-specific sections (GDPR Art. 35(7) DPIA content requirements, AI_Act FRIA fundamental rights analysis). |
| **Implementation Approach** | 1. **Unified Assessment Structure:**<br>&nbsp;&nbsp;- Section A: System Description (shared)<br>&nbsp;&nbsp;- Section B: Data Processing Description (shared)<br>&nbsp;&nbsp;- Section C: Necessity & Proportionality (shared)<br>&nbsp;&nbsp;- Section D: Risk Identification (shared)<br>&nbsp;&nbsp;- Section E: Mitigation Measures (shared)<br>&nbsp;&nbsp;- Section F: DPIA-specific (GDPR Art. 35(7) compliance)<br>&nbsp;&nbsp;- Section G: FRIA-specific (fundamental rights analysis per AI_Act)<br>2. **Trigger Alignment:** Initiate unified assessment when EITHER trigger fires (whichever comes first)<br>3. **Review Cycle:** Annual review satisfies both regulations' ongoing requirements<br>4. **Approval:** Single approval by DPO + AI Governance Lead |
| **Assessment Structure** | ```
Unified Impact Assessment (UIA)
├── Shared Sections (A-E): System, Data, Necessity, Risks, Mitigations
├── DPIA Section (F): GDPR Art. 35(7) compliance
│   ├── Systematic description of processing
│   ├── Necessity and proportionality
│   ├── Risk assessment for data subjects
│   └── Safeguards and measures
└── FRIA Section (G): Fundamental Rights Impact
    ├── Affected fundamental rights identification
    ├── Risk to rights holders
    ├── Vulnerable persons impact
    └── Post-market monitoring plan
``` |
| **Satisfies GDPR?** | ✅ Yes — DPIA section meets Art. 35(7) requirements |
| **Satisfies AI_Act?** | ✅ Yes — FRIA section meets fundamental rights impact requirements |
| **Efficiency Gain** | ~40% reduction in duplicate effort (shared sections A-E) |
| **Residual Risk** | LOW — Unified assessment must be carefully structured to meet both regulations' specific requirements |
| **Risk Owner** | DPO + AI Governance Lead (joint ownership) |
| **Implementation Priority** | P1 (HIGH — both assessments mandatory before market placement) |

---

### 4.2 HIGH Priority Tensions

#### T-004: Multi-Regulation Documentation Overlap — STRUCTURAL

| Field | Value |
|-------|-------|
| **Tension ID** | T-004 |
| **Tension Type** | RESOURCE_CONFLICT |
| **Tension Nature** | **STRUCTURAL** — always active when 4 regulations apply |
| **Always Active?** | Yes |
| **Overlap Condition** | N/A — documentation obligations from 4 regulations are permanently active |
| **Severity** | HIGH |
| **Sub-Domain** | D-09.1 (Information Security Policies) |
| **Conflicting Obligations** | OBL-D-09.1-001 (consolidated documentation obligation) |
| **Source Regulations** | GDPR-C08/C25/C26, CRA-C24, NIS2-C01, AI-C08/C12/C13/C20/C23 |
| **Conflict Description** | Four regulations require comprehensive technical documentation with overlapping but distinct requirements. GDPR requires privacy policies and DPIA documentation. CRA requires 10-year technical documentation for Critical Class products. NIS 2 requires security policies and risk analysis documentation. AI_Act requires technical documentation, transparency information, instructions for use, and quality management system documentation. Creating and maintaining four separate documentation sets creates significant overhead and risk of inconsistency. |
| **Risk if Unresolved** | Documentation inconsistency, audit findings, resource waste, version control issues |
| **Detection Method** | Same sub-domain (D-09.1), 10 source clauses from 4 regulations |

**Resolution Strategy: Unified ISMS with Regulation-Specific Annexes**

| Field | Value |
|-------|-------|
| **Resolution Type** | DESIGN_DECISION — resolved once by unified ISMS framework |
| **Resolution Description** | Leverage SecureBorder's existing ISO 27001 certification as the foundation for a unified Information Security Management System (ISMS). Each regulation's specific documentation requirements are maintained as annexes to the core ISMS, avoiding duplication of common controls. |
| **Implementation Approach** | 1. **Core ISMS** (ISO 27001): Common security policies, risk management, asset management<br>2. **GDPR Annex**: Privacy policies, RoPA, DPIA records, DPO designation<br>3. **CRA Annex**: Technical documentation (10-year), conformity assessment records, SBOM<br>4. **NIS 2 Annex**: Security policies, risk analysis, incident procedures<br>5. **AI_Act Annex**: Technical documentation, transparency info, QMS, conformity assessment<br>6. **Cross-Reference Matrix**: Map each regulatory requirement to ISMS document location |
| **Satisfies All?** | ✅ Yes — ISO 27001 provides foundation; annexes address regulation-specific requirements |
| **Residual Risk** | LOW — Existing ISO 27001 certification significantly reduces implementation effort |
| **Risk Owner** | CISO (ISMS owner) |
| **Implementation Priority** | P1 (HIGH — documentation required for all 4 regulations) |

---

#### T-005: AI Post-Market Monitoring vs. Continuous Security Monitoring Overlap — STRUCTURAL

| Field | Value |
|-------|-------|
| **Tension ID** | T-005 |
| **Tension Type** | RESOURCE_CONFLICT |
| **Tension Nature** | **STRUCTURAL** — always active when 3 regulations require continuous monitoring |
| **Always Active?** | Yes |
| **Overlap Condition** | N/A — continuous monitoring obligations from CRA, NIS 2, and AI_Act are permanently active |
| **Severity** | MEDIUM |
| **Sub-Domain** | D-10.1 (Continuous Security Monitoring) |
| **Conflicting Obligations** | OBL-D-10.1-001 (consolidated monitoring obligation) |
| **Source Regulations** | CRA-C12, NIS2-C21, NIS2-C29, AI-C25, AI-C21 |
| **Conflict Description** | AI_Act requires post-market monitoring (AI-C21) and AI-specific monitoring systems (AI-C25). NIS 2 requires continuous security monitoring (NIS2-C21, NIS2-C29). CRA requires attack surface minimization (CRA-C12). These overlap significantly — AI monitoring IS security monitoring for an AI-powered security product. Maintaining separate monitoring systems is wasteful. (Note: AI-C19 Art. 26 deployer obligations excluded per D1 — SecureBorder is PROVIDER only; deployer duty falls on border-control authority.) |
| **Risk if Unresolved** | Duplicate monitoring infrastructure, alert fatigue, resource waste |
| **Detection Method** | Same sub-domain (D-10.1), 5 source clauses from 3 regulations |

**Resolution Strategy: Integrated Monitoring Platform**

| Field | Value |
|-------|-------|
| **Resolution Type** | DESIGN_DECISION — resolved once by integrated platform |
| **Resolution Description** | Implement a single integrated monitoring platform (SOC) that covers both security monitoring and AI post-market monitoring. AI-specific metrics (accuracy drift, bias detection, false match rates) are integrated into the existing SOC dashboard alongside traditional security metrics (intrusion detection, vulnerability scanning, access logs). |
| **Implementation Approach** | 1. Extend existing 24/7 SOC to include AI monitoring metrics<br>2. AI accuracy and bias alerts routed through same incident management workflow<br>3. Post-market monitoring reports satisfy both AI_Act and NIS 2 requirements<br>4. Unified alerting and escalation procedures |
| **Satisfies All?** | ✅ Yes — Integrated platform covers all monitoring requirements |
| **Residual Risk** | LOW — SOC already exists; AI metrics extension is incremental |
| **Risk Owner** | CISO (SOC owner) + AI Governance Lead (AI monitoring) |
| **Implementation Priority** | P2 (MEDIUM — can be phased in) |

---

#### T-006: Supply Chain Security Documentation Overlap — STRUCTURAL

| Field | Value |
|-------|-------|
| **Tension ID** | T-006 |
| **Tension Type** | RESOURCE_CONFLICT |
| **Tension Nature** | **STRUCTURAL** — always active when GDPR and NIS 2 supply chain obligations overlap |
| **Always Active?** | Yes |
| **Overlap Condition** | N/A — supply chain obligations permanently overlap for all suppliers |
| **Severity** | MEDIUM |
| **Sub-Domain** | D-06.1 (Vendor Risk Assessment) |
| **Conflicting Obligations** | OBL-D-06.1-001 (consolidated vendor risk obligation) |
| **Source Regulations** | GDPR-C11, NIS2-C08, NIS2-C23 |
| **Conflict Description** | GDPR requires processor security assessments (Art. 28). NIS 2 requires supplier security assessments and vendor risk management (Art. 21(2)(g), Art. 21(3)). For SecureBorder's suppliers (cloud provider, hardware suppliers), both assessments cover overlapping ground (security controls, incident response, access management). |
| **Risk if Unresolved** | Duplicate assessments, supplier fatigue, inconsistent findings |
| **Detection Method** | Same sub-domain (D-06.1), 3 source clauses from 2 regulations |

**Resolution Strategy: Unified Supplier Security Questionnaire**

| Field | Value |
|-------|-------|
| **Resolution Type** | DESIGN_DECISION — resolved once by unified assessment process |
| **Resolution Description** | Create a single supplier security questionnaire that covers both GDPR processor requirements and NIS 2 supplier security requirements. Each supplier receives one comprehensive assessment covering all applicable regulations. |
| **Implementation Approach** | 1. Unified questionnaire with regulation-tagged sections<br>2. GDPR section: Art. 28 processor obligations, DPA compliance<br>3. NIS 2 section: Supply chain security, incident notification, access controls<br>4. Single assessment cycle per supplier (annual or upon significant change) |
| **Satisfies All?** | ✅ Yes — Unified assessment covers both GDPR and NIS 2 requirements |
| **Residual Risk** | LOW — Standard practice in supplier management |
| **Risk Owner** | CISO (vendor risk owner) |
| **Implementation Priority** | P2 (MEDIUM — can align with annual review cycle) |

---

### 4.3 MEDIUM Priority Tensions

#### T-007: Secure Development Lifecycle Overlap — STRUCTURAL

| Field | Value |
|-------|-------|
| **Tension ID** | T-007 |
| **Tension Type** | RESOURCE_CONFLICT |
| **Tension Nature** | **STRUCTURAL** — always active when GDPR and CRA apply during design phase |
| **Always Active?** | Yes |
| **Overlap Condition** | N/A — design phase permanently triggers both regulations |
| **Severity** | MEDIUM |
| **Sub-Domain** | D-07.1 (Secure-by-Design Principles) |
| **Conflicting Obligations** | OBL-D-07.1-001 (consolidated secure design obligation) |
| **Source Regulations** | GDPR-C09, CRA-C02, CRA-C22 |
| **Conflict Description** | GDPR privacy-by-design and CRA secure-by-default overlap in product design requirements. Both require security considerations from the start of development. |
| **Resolution Strategy** | Unified secure development lifecycle (SDLC) integrating privacy-by-design and secure-by-default principles. Already partially implemented via ISO 27001 secure SDLC. |
| **Risk Owner** | CTO (development owner) |
| **Implementation Priority** | P2 (MEDIUM) |

---

#### T-008: Security Training Overlap — STRUCTURAL

| Field | Value |
|-------|-------|
| **Tension ID** | T-008 |
| **Tension Type** | RESOURCE_CONFLICT |
| **Tension Nature** | **STRUCTURAL** — always active when GDPR and NIS 2 require security training |
| **Always Active?** | Yes |
| **Overlap Condition** | N/A — training obligations permanently overlap |
| **Severity** | LOW |
| **Sub-Domain** | D-08.1 (General Security Awareness) |
| **Conflicting Obligations** | OBL-D-08.1-001 |
| **Source Regulations** | GDPR-C27, NIS2-C14 |
| **Conflict Description** | Both GDPR and NIS 2 require security awareness training for staff. Training programs overlap significantly. |
| **Resolution Strategy** | Unified security awareness training program covering both GDPR data protection and NIS 2 cybersecurity topics. Annual training cycle satisfies both. |
| **Risk Owner** | HR (training owner) |
| **Implementation Priority** | P3 (LOW — easily unified) |

---

#### T-009: Monitoring Opt-Out vs Mandatory Security Monitoring — CONTEXTUAL

| Field | Value |
|-------|-------|
| **Tension ID** | T-009 |
| **Tension Type** | SCOPE_CONFLICT |
| **Tension Nature** | **CONTEXTUAL** — not always active; activated when a traveler exercises the CRA Annex I (2)(l) opt-out |
| **Always Active?** | No |
| **Overlap Condition** | Traveler requests opt-out of monitoring features while the same monitoring infrastructure is required by GDPR Art. 32(2) and NIS 2 Art. 21(2)(b) for security-event detection |
| **Severity** | MEDIUM |
| **Sub-Domain** | D-10.1 (Continuous Security Monitoring) |
| **Conflicting Obligations** | OBL-D-10.1-001 (continuous monitoring) vs CRA Annex I (2)(l) (user opt-out) |
| **Source Regulations** | CRA Annex I (2)(l) vs GDPR Art. 32(2) vs NIS 2 Art. 21(2)(b) |
| **Conflict Description** | CRA Annex I Part I (2)(l) provides a user-visible opt-out mechanism for monitoring where the user can reasonably be expected to be subjected to such monitoring. GDPR Art. 32(2) requires a five-event risk-enumeration that assumes continuous security monitoring (no opt-out). NIS 2 Art. 21(2)(b) requires appropriate-and-proportionate measures including continuous monitoring. The tension is between user opt-out (CRA) and continuous security obligation (GDPR + NIS 2). |
| **Detection Method** | Cross-sub-domain analysis: D-10.1 monitoring scope vs CRA Annex I (2)(l) opt-out rights |

**Resolution Strategy: Layered Monitoring with Split Opt-Out Scope**

| Field | Value |
|-------|-------|
| **Resolution Type** | OPERATIONAL_PROCEDURE — engineered monotone split between opt-out-eligible analytics and non-opt-out security monitoring |
| **Resolution Description** | Split monitoring into two layers: (a) security-event monitoring (mandatory, no opt-out) — anomaly detection, security incident detection, audit-log scope; (b) usage analytics (opt-out eligible per CRA Annex I (2)(l)) — UX telemetry, performance metrics, traveler-experience analytics. The split is monotone: opt-out does not affect the security-event layer. |
| **Implementation Approach** | 1. **Monitoring split**: (a) security-event monitoring (CRA/GDPR/NIS 2 mandatory, no opt-out); (b) usage analytics (CRA opt-out available)<br>2. **UI disclosure**: explicit toggle for analytics; documented in product disclosure<br>3. **DPA communication**: include opt-out scope in controller-to-processor agreements<br>4. **Audit trail**: opt-out events logged in the security-event channel (not the analytics channel) for accountability |
| **Satisfies CRA Annex I (2)(l)?** | ✅ Yes — opt-out available for analytics layer |
| **Satisfies GDPR Art. 32(2)?** | ✅ Yes — security-event monitoring remains continuously active regardless of opt-out |
| **Satisfies NIS 2 Art. 21(2)(b)?** | ✅ Yes — appropriate-and-proportionate continuous monitoring preserved on security-event layer |
| **Residual Risk** | LOW — risk of accidental opt-out extension to security-event layer; mitigated by monotone split enforcement + quarterly verification |
| **Risk Owner** | CISO (security monitoring) + DPO (opt-out rights) + Product Owner (analytics toggle) |
| **Implementation Priority** | P2 (MEDIUM — required for CRA Annex I (2)(l) conformity) |

**Verification Criteria:**
- Product UI exposes analytics opt-out toggle
- Security-event monitoring operates regardless of analytics opt-out (verified by negative-test)
- DPA template documents opt-out scope (analytics only, security-event excluded)
- Annual review confirms opt-out does not degrade GDPR Art. 32(2) baseline

**Risk if not resolved:** MEDIUM — CRA non-conformity on Annex I (2)(l); user trust degradation; possible market surveillance authority action.

**Status:** AGREED — per phase1_ontology.yaml F-03

---

### 4.5 Tensions Summary Dashboard

| Tension ID | Sub-Domain | Type | Severity | Nature | Resolution Type | Status | Risk Owner |
|------------|------------|------|----------|--------|-----------------|--------|------------|
| T-001 | D-04.3 | TEMPORAL_CONFLICT | CRITICAL | **Contextual** | OPERATIONAL_PROCEDURE | ✅ RESOLVED | CISO |
| T-002 | D-05.3 vs D-10.2 | REQUIREMENT_CONFLICT | CRITICAL | **Contextual** | OPERATIONAL_PROCEDURE | ✅ RESOLVED | DPO + AI Lead |
| T-003 | D-09.2 | TRIGGER_MISMATCH | HIGH | **Structural** | DESIGN_DECISION | ✅ RESOLVED | DPO + AI Lead |
| T-004 | D-09.1 | RESOURCE_CONFLICT | HIGH | **Structural** | DESIGN_DECISION | ✅ RESOLVED | CISO |
| T-005 | D-10.1 | RESOURCE_CONFLICT | MEDIUM | **Structural** | DESIGN_DECISION | ✅ RESOLVED | CISO + AI Lead |
| T-006 | D-06.1 | RESOURCE_CONFLICT | MEDIUM | **Structural** | DESIGN_DECISION | ✅ RESOLVED | CISO |
| T-007 | D-07.1 | RESOURCE_CONFLICT | MEDIUM | **Structural** | DESIGN_DECISION | ✅ RESOLVED | CTO |
| T-008 | D-08.1 | RESOURCE_CONFLICT | LOW | **Structural** | DESIGN_DECISION | ✅ RESOLVED | HR |
| T-009 | D-10.1 | SCOPE_CONFLICT | MEDIUM | **Contextual** | OPERATIONAL_PROCEDURE | ✅ RESOLVED | CISO + DPO + Product Owner |

**Total Tensions:** 9
**Contextual:** 3 (T-001, T-002, T-009 — resolved via operational procedures)
**Structural:** 6 (T-003–T-008 — resolved via design decisions)

---

## 5. RESOLUTION IMPLEMENTATION PLAN

### 5.1 Priority Order

| Priority | Tension | Resolution | Estimated Effort | Dependencies |
|----------|---------|------------|------------------|--------------|
| P1 | T-001 (24h vs 72h) | Incident classification workflow | 2 weeks | SOC procedures |
| P1 | T-002 (Erasure vs Logging) | Cryptographic sharding | 4 weeks | Tokenization system |
| P1 | T-003 (DPIA vs FRIA) | Unified assessment template | 3 weeks | DPO + AI Lead alignment |
| P1 | T-004 (Documentation) | ISMS annex structure | 4 weeks | ISO 27001 foundation |
| P2 | T-005 (Monitoring) | SOC AI metrics extension | 6 weeks | SOC platform |
| P2 | T-006 (Supplier) | Unified questionnaire | 2 weeks | Vendor risk program |
| P2 | T-007 (SDLC) | Privacy+Secure SDLC merge | 4 weeks | Development process |
| P3 | T-008 (Training) | Unified training program | 1 week | HR training calendar |

### 5.2 Resolution Verification Criteria

| Tension | Verification Method | Success Criteria |
|---------|--------------------|------------------|
| T-001 | TEST | Incident response drill: 24h notification achieved for all incident types |
| T-002 | TEST + INSPECT | Erasure request processed; anonymized logs retained and auditable |
| T-003 | INSPECT | Unified assessment document reviewed and approved by DPO + AI Lead |
| T-004 | INSPECT | ISMS documentation reviewed; cross-reference matrix complete |
| T-005 | DEMONSTRATE | SOC dashboard shows both security and AI metrics |
| T-006 | INSPECT | Supplier questionnaire covers both GDPR and NIS 2 requirements |
| T-007 | INSPECT | SDLC documentation includes privacy-by-design and secure-by-default |
| T-008 | INSPECT | Training curriculum covers both GDPR and NIS 2 topics |

---

## 6. PHASE 2 GATE C CRITERIA

| Criterion | Status | Evidence |
|-----------|--------|----------|
| All tensions detected | ✅ PASS | Section 4 (8 tensions identified) |
| CRITICAL tensions resolved | ✅ PASS | T-001, T-002 resolved with documented strategies |
| HIGH tensions resolved | ✅ PASS | T-003, T-004 resolved with documented strategies |
| Resolution strategies documented | ✅ PASS | Section 5 (implementation plan) |
| Risk owners assigned | ✅ PASS | Section 4 (all tensions have owners) |
| Verification criteria defined | ✅ PASS | Section 5.2 |

**Gate C Status:** ✅ **PASS** — Ready for Gate D (Privacy and Security Goals)

---

## 7. REGULATORY OVERLAP ANALYSIS (4-Regulation Jaccard Index)

### 7.1 Pairwise Overlap Matrix

With 4 applicable regulations, there are 6 pairwise combinations. The Jaccard Index measures overlap: J(A,B) = |A∩B| / |A∪B|.

| Regulation Pair | Intersection | Union | Jaccard Index | Interpretation | Tension Risk |
|-----------------|-------------|-------|---------------|----------------|--------------|
| **GDPR ↔ CRA** | 11 sub-domains | 31 sub-domains | 0.355 | Moderate overlap | MEDIUM — different focus areas |
| **GDPR ↔ NIS 2** | 14 sub-domains | 29 sub-domains | 0.483 | High overlap | HIGH — operational + data protection |
| **GDPR ↔ AI_Act** | 10 sub-domains | 27 sub-domains | 0.370 | Moderate overlap | MEDIUM — data governance overlap |
| **CRA ↔ NIS 2** | 16 sub-domains | 30 sub-domains | **0.533** | **Highest overlap** | HIGH — both technical security |
| **CRA ↔ AI_Act** | 9 sub-domains | 32 sub-domains | 0.281 | Lower overlap | LOW — product vs AI governance |
| **NIS 2 ↔ AI_Act** | 11 sub-domains | 34 sub-domains | 0.324 | Moderate overlap | MEDIUM — operational + AI |

**Key Insight:** CRA ↔ NIS 2 has the highest overlap (0.533) because both mandate technical security controls (vulnerability management, access control, incident response, monitoring). This creates the most tension risk — conflicting technical requirements between product security and operational security.

### 7.2 Triple Regulation Overlap Analysis

| Sub-Domain | 3+ Regulations | Tension Type | Severity | Resolution Required |
|------------|----------------|--------------|----------|---------------------|
| D-04.3 Regulatory Notification | GDPR + CRA + NIS 2 + AI_Act (4) | TEMPORAL_CONFLICT | CRITICAL | Max-SLA routing (24h/72h) |
| D-09.1 Information Security Policies | GDPR + CRA + NIS 2 + AI_Act (4) | RESOURCE_CONFLICT | HIGH | Unified ISMS |
| D-09.2 Impact & Risk Assessments | GDPR + CRA + NIS 2 + AI_Act (4) | TRIGGER_MISMATCH | HIGH | Unified DPIA+FRIA |
| D-10.3 Compliance Testing | GDPR + CRA + NIS 2 + AI_Act (4) | RESOURCE_CONFLICT | MEDIUM | Unified testing program |
| D-01.1 Data at Rest Encryption | GDPR + CRA + NIS 2 + AI_Act (4) | None (reinforcement) | — | Single standard satisfies all |
| D-01.2 Data in Transit Encryption | GDPR + CRA + NIS 2 (3) | None (reinforcement) | — | Single standard satisfies all |
| D-02.1 Vulnerability Identification | CRA + NIS 2 + AI_Act (3) | None (reinforcement) | — | Unified vuln management |
| D-03.1 Identity Lifecycle | CRA + NIS 2 + AI_Act (3) | None (reinforcement) | — | Unified IAM |
| D-10.1 Continuous Monitoring | CRA + NIS 2 + AI_Act (3) | RESOURCE_CONFLICT | MEDIUM | Integrated SOC |
| D-10.2 Audit Logging | CRA + NIS 2 + AI_Act (3) | REQUIREMENT_CONFLICT | CRITICAL | Cryptographic sharding |

**Triple+ Overlap Tension Density:** 6/17 sub-domains with 3+ regulation coverage have tensions (35.3%)

### 7.3 Quadruple Overlap (All 4 Regulations)

Only 5 sub-domains are covered by all 4 regulations simultaneously:

| Sub-Domain | Combined NI | Tension Count | Resolution Complexity |
|------------|-------------|---------------|----------------------|
| D-01.1 Data at Rest Encryption | 3.000 | 0 | LOW — cumulative reinforcement |
| D-04.3 Regulatory Notification | 3.000 | 1 (T-001) | HIGH — timing conflict across 4 regulations |
| D-09.1 Information Security Policies | 3.000 | 1 (T-004) | MEDIUM — documentation overlap |
| D-09.2 Impact & Risk Assessments | 3.000 | 1 (T-003) | HIGH — trigger mismatch |
| D-10.3 Compliance Testing | 3.000 | 0 | LOW — cumulative reinforcement |

**Quadruple Overlap Tension Rate:** 3/5 sub-domains (60%) have tensions requiring resolution

---

## 8. TENSION DENSITY BY DOMAIN

### 8.1 Tension Distribution Across 10 Domains

| Domain | Sub-Domains | Tensions | Density | Primary Tension Types |
|--------|-------------|----------|---------|----------------------|
| D-01 Data Protection | 4 | 0 | 0.0% | — |
| D-02 Vulnerability Mgmt | 4 | 0 | 0.0% | — |
| D-03 Access Control | 4 | 0 | 0.0% | — |
| D-04 Incident Response | 4 | 1 | 25.0% | TEMPORAL_CONFLICT (T-001) |
| D-05 Data Lifecycle | 4 | 1 | 25.0% | REQUIREMENT_CONFLICT (T-002) |
| D-06 Supply Chain | 4 | 1 | 25.0% | RESOURCE_CONFLICT (T-006) |
| D-07 Secure Development | 4 | 1 | 25.0% | RESOURCE_CONFLICT (T-007) |
| D-08 Human Factors | 3 | 1 | 33.3% | RESOURCE_CONFLICT (T-008) |
| D-09 Governance | 4 | 2 | 50.0% | RESOURCE_CONFLICT (T-004), TRIGGER_MISMATCH (T-003) |
| D-10 Monitoring | 3 | 2 | 66.7% | RESOURCE_CONFLICT (T-005), REQUIREMENT_CONFLICT (T-002) |

**Highest Tension Density:** D-10 Monitoring & Audit (66.7%) — AI_Act logging vs GDPR erasure creates cross-domain tension with D-05

### 8.2 Cross-Domain Tensions

Some tensions span multiple sub-domains:

| Tension | Primary Sub-Domain | Secondary Sub-Domain | Cross-Domain Type |
|---------|-------------------|---------------------|-------------------|
| T-002 (Erasure vs Logging) | D-05.3 Right to Erasure | D-10.2 Audit Logging | Retention conflict |
| T-005 (Monitoring overlap) | D-10.1 Continuous Monitoring | D-04.1 Incident Detection | Operational overlap |

---

## 9. CROSS-REGULATORY TRIGGER OVERLAY ANALYSIS

For Case 2 (SecureBorder: GDPR + CRA + NIS 2 + AI_Act), the number of possible trigger overlap scenarios is significant. This section documents when contextual tensions would activate.

### 9.1 Notification Trigger Overlay (T-001 Context)

| Compound Event Scenario | Triggers GDPR? | Triggers CRA? | Triggers NIS 2? | Triggers AI_Act? | Tension Activated? | Resolution |
|-------------------------|---------------|---------------|-----------------|------------------|-------------------|------------|
| Personal data breach (no product vuln) | ✅ Yes | ❌ No | ❌ No | ❌ No | No tension — GDPR only (72h to AP) | Standard breach workflow |
| Exploited product vuln (no personal data) | ❌ No | ✅ Yes | ❌ No | ❌ No | No tension — CRA only (24h ENISA) | Standard vuln response |
| Significant incident (no data breach, no vuln) | ❌ No | ❌ No | ✅ Yes | ❌ No | No tension — NIS 2 only (24h CSIRT) | Standard incident response |
| AI accuracy degradation (no breach, no vuln) | ❌ No | ❌ No | ❌ No | ✅ Yes | No tension — AI_Act only (15d MSA) | AI post-market monitoring |
| **Exploited vuln + personal data exfiltration** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No | **T-001 ACTIVATED** (3-reg) | Max-SLA Routing (24h) |
| **Exploited vuln + personal data + AI misidentification** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | **T-001 ACTIVATED** (4-reg) | Max-SLA Routing (24h) |
| AI serious incident + personal data breach | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes | **T-001 ACTIVATED** (3-reg) | Max-SLA Routing (24h) |
| Product design (pre-market) | ✅ Yes (GDPR-C09) | ✅ Yes (CRA-C02) | ❌ No | ✅ Yes (AI-C09) | T-007 (structural — always active) | Unified SDLC |

### 9.2 Erasure vs Logging Overlay (T-002 Context)

| Erasure Request Scenario | GDPR Triggered? | AI_Act Retention Active? | Tension Activated? | Resolution |
|--------------------------|----------------|-------------------------|-------------------|------------|
| Traveler requests erasure of account data (no AI logs) | ✅ Yes | ❌ No | No tension | Standard erasure |
| Traveler requests erasure — data exists in AI activity logs | ✅ Yes | ✅ Yes | **T-002 ACTIVATED** | Cryptographic sharding |
| Government authority requests data retention (SecureBorder as processor) | ✅ Yes (Art. 17 exemption) | ✅ Yes | No tension — GDPR Art. 17(3)(b) exemption | Retain per government contract |
| Employee requests erasure of HR data (no AI logs) | ✅ Yes | ❌ No | No tension | Standard erasure |

### 9.3 Cross-Case Implication

The number of compound event scenarios grows with the number of applicable regulations:
- **Case 1 (TinyTask: 2 regs):** 1 contextual tension, 3 compound events
- **Case 2 (SecureBorder: 4 regs):** 2 contextual tensions, 8+ compound events
- **Case 3 (OmniBank: 5 regs):** Estimated 1-2 contextual tensions, 10+ compound events

The structural tensions also increase with each regulation added, as each new regulation brings its own documentation, assessment, monitoring, and design standards.

---

## 10. RESOLUTION VERIFICATION CRITERIA

### 10.1 Test Plans for Each Resolution

| Tension | Resolution | Verification Method | Test Scenario | Success Criteria |
|---------|------------|--------------------|---------------|------------------|
| T-001 | Max-SLA Routing (24h/72h) | DEMONSTRATE | Simulate personal data breach; measure notification time | 24h early warning sent; 72h detailed notification sent |
| T-002 | Cryptographic Sharding | TEST + INSPECT | Submit erasure request; verify identity mapping destroyed; verify anonymized logs retained | Identity mapping destroyed; AI logs retained with tokens only |
| T-003 | Unified DPIA+FRIA | INSPECT | Review unified assessment document | Both GDPR Art. 35(7) and AI_Act FRIA sections complete |
| T-004 | Unified ISMS | INSPECT | Audit ISMS documentation | All 4 regulation annexes present and cross-referenced |
| T-005 | Integrated SOC | DEMONSTRATE | Review SOC dashboard | Both security and AI metrics visible; unified alerting |
| T-006 | Unified Supplier Assessment | INSPECT | Review supplier questionnaire | Both GDPR Art. 28 and NIS 2 Art. 21 sections present |
| T-007 | Unified SDLC | INSPECT | Review SDLC documentation | Privacy-by-design and secure-by-default both documented |
| T-008 | Unified Training | INSPECT | Review training curriculum | Both GDPR data protection and NIS 2 cybersecurity topics covered |

### 10.2 Resolution Effectiveness Metrics

| Metric | Target | Current Status |
|--------|--------|----------------|
| Tensions resolved | 100% (8/8) | ✅ 8/8 |
| CRITICAL tensions resolved | 100% (2/2) | ✅ 2/2 |
| Resolution test plans defined | 100% (8/8) | ✅ 8/8 |
| Risk owners assigned | 100% (8/8) | ✅ 8/8 |
| Implementation timeline defined | 100% (8/8) | ✅ 8/8 |

---

## 11. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-03 | Compliance Lead | Initial release - SecureBorder Solutions case (8 tensions, all resolved) |
| 1.1 | 2026-04-03 | Compliance Lead | Expanded: 6-pair Jaccard Index analysis, triple/quadruple overlap, tension density by domain, cross-domain tensions, resolution verification test plans |
| 1.2 | 2026-04-11 | Compliance Lead | T-001: Corrected CRA dual flows (Art.14 vulns 14d post-fix vs Art.15 incidents 1mo), added AI_Act Art.73 (15d/2d), updated workflow with 5-regulation routing, added CRA 14d post-fix clock nuance |
 | 1.3 | 2026-04-11 | Compliance Lead | **C1 fix:** Corrected CRA Art. 15 → Art. 14(3-5) throughout T-001 (Art. 15 is voluntary, not mandatory). Updated Source Regulations, Conflict Description, Timing Details, Workflow Diagram, and Satisfaction checks. Art. 15 now explicitly noted as N/A. |
| 2.0 | 2026-04-16 | Compliance Lead | **Structural/Contextual tension model:** Replaced flat tension model with Structural vs Contextual classification. Added §3 Tension Classification Model (Nature, Activation, Resolution Type). Added Nature/Always Active?/Overlap Condition attributes to all 8 tensions. Added §9 Cross-Regulatory Trigger Overlay Analysis. Reclassified: 2 contextual (T-001, T-002) + 6 structural (T-003–T-008). |

---

## 8. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-03 |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| AEGIS Methodology Review | | | |

---

**Next Document:** Doc16_Privacy_Security_Goals.md
**Gate Status:** ✅ PASS — Ready for Privacy and Security Goals Definition
