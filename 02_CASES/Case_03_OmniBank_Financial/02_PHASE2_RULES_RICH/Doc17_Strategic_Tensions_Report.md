---
document_id: AEGIS-P2-09
title: Strategic Tensions Report
phase: 2
version: 1.0
created: 2026-04-03
updated: 2026-04-03
author: Compliance Lead
status: DRAFT
inputs: [08_Obligation_Derivation.md, 07_Structured_Compliance_Matrix.md]
outputs: [10_Privacy_Security_Objectives.md]
traceability: AEGIS Class Model -> StrategicTension, ConflictResolution classes
related_documents: 03_Design_Decisions_Log.md
---

# Strategic Tensions Report

## 1. DOCUMENT PURPOSE

Consolidates strategic tensions analysis (Step C1-C5), detecting conflicts between obligations from 5 regulations (GDPR, CRA, NIS 2, DORA, AI Act), documenting resolutions, and assigning risk owners.

**Alignment with Class Model:**
- `StrategicTension` - Detected conflicts between obligations
- `ConflictResolution` - Resolution strategies for each tension
- `RegulatoryObligation` - Source obligations in conflict

**Phase 2 Step:** C (Strategic Tensions Analysis)

**Gate Criteria:** All CRITICAL priority tensions resolved with documented rationale

---

## 2. STRATEGIC TENSIONS METADATA

| Attribute | Value |
|-----------|-------|
| tensionsReportId | STR-TENSION-OMNIBANK-2026-001 |
| analysisDate | 2026-04-03 |
| basedOnObligationDerivation | DERIV-OMNIBANK-2026-001 |
| analyzedBy | Compliance Lead |
| phase2Step | C1+C2+C3+C4+C5 |
| caseComplexity | MAXIMUM (5/5 regulations) |

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
| **Example** | GDPR Art.17 erasure vs DORA Art.11 immutable logs in D-05.3/D-10.2 | GDPR 72h vs CRA 24h vs NIS 2 24h vs DORA 4h vs AI Act 15d notification in D-04.3 (only when same event triggers multiple) |

### 3.2 Why This Distinction Matters

The tension between notification obligations is **not** about the same regulatory concept. Each regulation has a distinct trigger:

| Regulation | Trigger | Subject Obligated | Recipient |
|------------|---------|-------------------|-----------|
| **GDPR Art. 33** | Personal data breach | Controller | Data protection authority |
| **CRA Art. 14(1-2)** | Actively exploited vulnerability | Manufacturer | ENISA + CSIRT |
| **CRA Art. 14(3-5)** | Severe security incident | Manufacturer | CSIRT + ENISA |
| **NIS 2 Art. 23** | Significant incident | Essential entity | National CSIRT |
| **DORA Art. 19** | Major ICT-related incident | Financial entity | Financial competent authority |
| **AI Act Art. 73** | Serious incident involving high-risk AI | Provider | Market surveillance authority |

**Scenario A — distinct events, no overlap.** A personal data breach affecting customer records (GDPR triggers) may not involve an exploited product vulnerability (CRA does not trigger) or a major ICT-related incident (DORA does not trigger). In this case there is **no tension** — just parallel, independent obligations.

**Scenario B — 5-regulation compound event.** An attacker exploits a vulnerability in OmniBank's AI-driven fraud detection system, causing a wrongful transaction block AND exfiltrating customer personal data AND disrupting core banking services. The **same factual event** triggers GDPR (personal data breach → 72h), CRA (exploited vulnerability → 24h ENISA), NIS 2 (significant incident → 24h CSIRT), DORA (major ICT-related incident → 4h post-classification), and AI Act (serious AI incident → 15d MSA). **This is the contextual tension.**

The tension is not "the clauses contradict" — it is "the same event generates multiple notification obligations with different deadlines, to different authorities, with different report formats."

### 3.3 Tension Types (Extended)

| Tension Type | Description | Detection Pattern | Examples |
|--------------|-------------|-------------------|----------|
| TEMPORAL_CONFLICT | Conflicting timeframes for the same or overlapping event | 72h vs 24h vs 4h vs 15d notification | TENSION-H-001 (contextual) |
| REQUIREMENT_CONFLICT | Contradictory requirements | Erasure vs immutable log retention | TENSION-H-002 (structural) |
| RESOURCE_CONFLICT | Competing for same resource | Budget, personnel, documentation overhead | — |
| IMPLEMENTATION_CONFLICT | Incompatible implementations | Different encryption standards | — |
| INTENSITY_GAP | Different normative force | NI=2 vs NI=3 | TENSION-L-001 (structural) |
| FREQUENCY_MISMATCH | Different occurrence patterns | ONE_TIME vs CONTINUOUS vs PERIODIC | TENSION-M-001 (structural) |

### 3.4 Tension Severity Levels

| Severity | Description | Action Required |
|----------|-------------|-----------------|
| CRITICAL | Direct contradiction, market access at risk | Mandatory resolution before Phase 2 Gate |
| HIGH | Significant conflict, compliance at risk | Documented resolution with mitigation strategy |
| MEDIUM | Potential conflict, manageable with controls | Track and monitor |
| LOW | Minor tension, operational resolution | Note in decision log |

### 3.5 Detection Criteria Applied to OmniBank

| Criterion | Threshold | Applied to OmniBank |
|-----------|-----------|---------------------|
| **Same Sub-Domain** | ≥2 regulations map to same D-XX.X | ✅ 38 sub-domains with multi-regulation coverage across 5 regulations |
| **Different obligationType** | CONTINUOUS vs TRIGGERED vs ONE_TIME vs PERIODIC | ✅ Mixed types in 15 sub-domains |
| **Different obligatedParty** | CONTROLLER vs MANUFACTURER vs ESSENTIAL_ENTITY vs FINANCIAL_ENTITY vs PROVIDER | ✅ 5 different parties across obligations |
| **Normative Intensity Delta** | NI_A - NI_B ≥ 0.5 | ✅ D-07.1: GDPR NI=2 vs CRA NI=3 (Delta=1.0) |
| **Timing Mismatch** | Different deadlines (e.g., 72h vs 24h vs 4h) | ✅ D-04.3 (4h DORA vs 24h CRA/NIS 2 vs 72h GDPR vs 15d AI Act) |
| **Retention Mismatch** | Different retention periods | ✅ D-10.2 (DORA immutable logs vs GDPR erasure right) |

---

## 4. STRATEGIC TENSIONS CATALOG

### 4.1 Tension Classification Summary

| Tension ID | Type | Severity | Nature | Always Active? | Overlap Condition | Resolution Type |
|---|---|---|---|---|---|---|
| TENSION-H-001 | TEMPORAL_CONFLICT | CRITICAL | **Contextual** | No | Same event triggers 5 different notification obligations (GDPR 72h, CRA 24h, NIS 2 24h, DORA 4h, AI Act 15d) | OPERATIONAL_PROCEDURE |
| TENSION-H-002 | REQUIREMENT_CONFLICT | CRITICAL | **Structural** | Yes | N/A — GDPR erasure and DORA immutable logs permanently coexist | DESIGN_DECISION |
| TENSION-M-001 | FREQUENCY_MISMATCH | MEDIUM | **Structural** | Yes | N/A — assessment triggers permanently satisfied by bank business model | DESIGN_DECISION |
| TENSION-L-001 | INTENSITY_GAP | LOW | **Structural** | Yes | N/A — secure-by-design always active during design phase | DESIGN_DECISION |

**Total Tensions:** 4
**Contextual:** 1 (TENSION-H-001 — resolved via operational procedure)
**Structural:** 3 (TENSION-H-002, TENSION-M-001, TENSION-L-001 — resolved via design decisions)

### 4.2 CRITICAL Priority Tensions

#### TENSION-H-001: Incident Notification Timelines (D-04.3) -- TEMPORAL_CONFLICT

| Attribute | Value |
|-----------|-------|
| Tension ID | TENSION-H-001 |
| Conflict Type | TEMPORAL_CONFLICT |
| Severity | CRITICAL |
| Sub-Domain | D-04.3 (Incident Escalation) |
| Obligation ID | OBL-D-04.3-001 |
| Source Clauses | 11 clauses across 5 regulations |
| All NI | 3 (Mandatory) |
| Detected By | C1 (Sub-Domain Scan) + C3 (Cross-Regulation Conflict Detection) |
| Tension Nature | **CONTEXTUAL** — not always active; depends on event overlap |
| Always Active? | No |
| Overlap Condition | Same factual event triggers notifications from 2+ regulations |

**Conflict Description:**

Each of the 5 regulations prescribes different incident notification timelines, triggers, and recipients for the same class of security incidents:

| Regulation | Deadline | Recipient | Trigger Condition |
|------------|----------|-----------|-------------------|
| GDPR Art.33 | 72 hours | Supervisory Authority | Personal data breach likely to result in risk |
| CRA Art.14(1-2) | 24h early warning + 72h notification + **14 days after corrective measure available** | ENISA / CSIRT | Actively exploited vulnerability |
| CRA Art.14(3-5) | 24h early warning + 72h notification + **1 month** | ENISA / CSIRT | Severe incident affecting product security |
| NIS 2 Art.23 | 24h early warning + 72h notification + 1 month final report | CSIRT / Competent Authority | Significant impact on service provision |
| DORA Art.19 + RTS | **4h after classification (max 24h after discovery)** + 72h intermediate + 1 month final | Competent Authority | Major ICT-related incident (per RTS Art. 6) |
| AI Act Art.73 | **15 days** (default) / **2 days** (widespread) / **10 days** (death) | Market Surveillance Authority | High-risk AI system serious incident |

**Root Cause:** Each regulation was drafted independently with different trigger conditions, notification recipients, and deadline structures. DORA's deadlines are specified in the RTS (Delegated Regulation 2025/301), not in the regulation text itself (Art. 19(4) defers to Art. 20). The regulatory overlap creates an operational impossibility if treated as separate workflows — an incident triggering all 5 regulations would require 5 different notification processes with 5 different timelines.

**Resolution: Max-SLA Routing**

The most stringent timeline (24h, or 4h post-classification for DORA) serves as the universal SLA. A single automated incident detection and classification workflow routes notifications to all relevant authorities within the tightest window, satisfying all regulations simultaneously.

| Resolution Element | Implementation Detail |
|--------------------|----------------------|
| Universal SLA | 4h post-classification (DORA RTS), max 24h after discovery, for initial notification to all authorities |
| **Resolution Type** | **OPERATIONAL_PROCEDURE** — Max-SLA Routing per-incident |
| Automated Detection | Centralized audit-log driven incident classification within 4 hours |
| Pre-approved Templates | Notification templates pre-vetted for each authority (SA, CSIRT, ENISA, Competent Authority, MSA) |
| Escalation Path | 4h/24h initial → 72h detailed → 1 month final (covers DORA, NIS 2, CRA Art.14(3-5)); CRA Art.14(1-2): 14 days post-fix |
| AI Act Compliance | 15d default / 2d widespread / 10d death — continuous monitoring feed integrated into centralized audit log platform |
| CRA Dual Flow | Art.14(1-2) (vulns): 14d post-fix final report; Art.14(3-5) (incidents): 1 month final report — tracked separately. **Note:** Art. 15 is voluntary reporting, not a mandatory compliance obligation. |

**Risk Owner:** CISO
**Status:** RESOLVED

---

#### TENSION-H-002: Erasure vs Immutable Logs (D-05.3 vs D-10.2) -- REQUIREMENT_CONFLICT

| Attribute | Value |
|-----------|-------|
| Tension ID | TENSION-H-002 |
| Conflict Type | REQUIREMENT_CONFLICT |
| Severity | CRITICAL |
| Sub-Domains | D-05.3 (Data Retention) vs D-10.2 (Audit Logging) |
| Obligation IDs | OBL-D-05.3-001 vs OBL-D-10.2-001 |
| Source Clauses | 8 clauses across 4 regulations |
| Avg NI | 3.000 |
| Detected By | C2 (Cross-Domain Conflict) + C3 (Cross-Regulation Conflict Detection) |
| Tension Nature | **STRUCTURAL** — always active; GDPR Art.17 and DORA Art.11 permanently coexist |
| Always Active? | Yes |
| Overlap Condition | N/A — GDPR Art.17 and DORA Art.11 permanently coexist |

**Conflict Description:**

GDPR grants data subjects the right to erasure (Art.17), requiring complete deletion of personal data upon request. Simultaneously, AI Act (Art.12), DORA (Art.11), and CRA (Art.14) mandate immutable audit log retention for regulatory purposes. These obligations are mutually exclusive under a conventional logging architecture:

| Regulation | Requirement | Sub-Domain | NI |
|------------|-------------|------------|-----|
| GDPR Art.17 | Erasure of personal data on request | D-05.3 | 3 |
| AI Act Art.12 | 6-year log retention for high-risk AI systems | D-10.2 | 3 |
| DORA Art.11 | Immutable audit logs for all ICT activities | D-10.2 | 3 |
| CRA Art.14 | Activity logging for digital products | D-10.2 | 3 |

**Root Cause:** GDPR's erasure right is a fundamental privacy obligation that assumes data can be selectively deleted. AI Act, DORA, and CRA require log immutability for accountability, forensics, and regulatory audit purposes. A traditional centralized log architecture cannot simultaneously delete specific PII and maintain an immutable audit trail.

**Resolution: Cryptographic Sharding**

Personal Identifiable Information (PII) is separated from log content at ingestion time. Logs contain only cryptographic hashes and non-PII operational data. PII is stored separately with per-subject encryption keys. Upon erasure request, the subject's encryption key is destroyed, rendering their PII cryptographically unrecoverable while the audit log hash chain remains intact and verifiable.

| Resolution Element | Implementation Detail |
|--------------------|----------------------|
| PII Separation | Log pipeline splits PII from operational data at ingestion |
| **Resolution Type** | **DESIGN_DECISION** — Cryptographic Sharding (permanent design choice) |
| Key Management | Per-subject encryption keys in dedicated HSM |
| Hash Chains | Cryptographic hash chains ensure log integrity without PII |
| Erasure Mechanism | Key destruction = cryptographic erasure (satisfies GDPR Art.17) |
| Audit Verification | Hash chain verification independent of PII (satisfies AI Act/DORA/CRA) |
| Retention Period | 6 years (AI Act maximum) for hash chains; PII deleted on request |

**Risk Owner:** DPO + CISO (joint)
**Status:** RESOLVED

---

### 4.2 MEDIUM Priority Tensions

#### TENSION-M-001: Risk Assessment Trigger Divergence (D-09.2) -- FREQUENCY_MISMATCH

| Attribute | Value |
|-----------|-------|
| Tension ID | TENSION-M-001 |
| Conflict Type | FREQUENCY_MISMATCH |
| Severity | MEDIUM |
| Sub-Domain | D-09.2 (Risk Management) |
| Obligation ID | OBL-D-09.2-001 |
| Source Clauses | 9 clauses across 5 regulations |
| Avg NI | 2.889 |
| Detected By | C4 (Frequency Mismatch Detection) |
| Tension Nature | **STRUCTURAL** — always active; assessment triggers permanently satisfied by bank business model |
| Always Active? | Yes |
| Overlap Condition | N/A — assessment triggers permanently satisfied by bank business model |

**Conflict Description:**

Each regulation prescribes different frequencies and triggers for risk assessments covering related but distinct scopes:

| Regulation | Assessment Type | Frequency | Trigger | NI |
|------------|----------------|-----------|---------|-----|
| GDPR Art.35 | Data Protection Impact Assessment (DPIA) | ONE_TIME per processing operation | Before high-risk processing begins | 3 |
| AI Act Art.43 | Fundamental Rights Impact Assessment (FRIA) | ONE_TIME before deployment | Before placing high-risk AI system on market | 3 |
| CRA Art.9 | Cybersecurity risk assessment | ONE_TIME before placing on market | Before market entry | 3 |
| NIS 2 Art.21 | Incident handling and risk management | CONTINUOUS | Ongoing operational requirement | 3 |
| DORA Art.6 | ICT risk management framework | PERIODIC (at least annual) | Regular review cycle | 2 |

**Root Cause:** Each regulation addresses risk assessment from its own regulatory lens -- GDPR focuses on data processing, AI Act on fundamental rights, CRA on product security, NIS 2 on operational resilience, and DORA on ICT risk. While the scopes differ, the assessment activities overlap significantly (threat modeling, impact analysis, control evaluation).

**Resolution: IPSARA Unified Assessment Framework**

A single Integrated Privacy, Security, AI, and Regulatory Assessment (IPSARA) framework with 4 modular sections replaces 5 separate regulatory assessments. Each module maps to its regulatory requirement, but data collection, threat analysis, and control evaluation are shared:

**Resolution Type:** DESIGN_DECISION — IPSARA Framework (permanent process)

| IPSARA Module | Regulatory Mapping | Update Frequency |
|---------------|-------------------|------------------|
| Module A: Data Processing & Privacy | GDPR DPIA | Per new processing operation |
| Module B: AI Fundamental Rights | AI Act FRIA | Per new AI system deployment |
| Module C: Product Security | CRA risk assessment | Per product release |
| Module D: Operational Resilience | NIS 2 + DORA ICT risk | Continuous (with annual comprehensive review) |

**Risk Owner:** CISO + DPO + AI Governance Lead
**Status:** RESOLVED

---

### 4.3 LOW Priority Tensions

#### TENSION-L-001: Secure-by-Design Intensity Gap (D-07.1) -- INTENSITY_GAP

| Attribute | Value |
|-----------|-------|
| Tension ID | TENSION-L-001 |
| Conflict Type | INTENSITY_GAP |
| Severity | LOW |
| Sub-Domain | D-07.1 (Secure Development Lifecycle) |
| Obligation ID | OBL-D-07.1-001 |
| Source Clauses | 4 clauses across 2 regulations |
| NI Delta | 1.000 |
| Detected By | C5 (Intensity Gap Analysis) |
| Tension Nature | **STRUCTURAL** — always active; secure-by-design always active during design phase |
| Always Active? | Yes |
| Overlap Condition | N/A — secure-by-design always active during design phase |

**Conflict Description:**

GDPR and CRA both address secure-by-design principles but with different normative intensity levels:

| Regulation | Requirement | NI | Wording |
|------------|-------------|-----|---------|
| GDPR Art.25 | "appropriate technical and organisational measures" for data protection by design | 2 (Recommended) | Should implement |
| CRA Annex I | "secure by default" configuration for digital products | 3 (Mandatory) | Shall implement |

**Root Cause:** GDPR frames secure-by-design as a best practice ("appropriate measures"), while CRA mandates it as a baseline requirement ("secure by default"). The NI Delta of 1.000 represents the maximum possible intensity gap.

**Resolution: Follow CRA Standard**

The CRA "secure by default" standard establishes a higher bar that inherently satisfies GDPR's "appropriate measures" requirement. Implementing CRA-compliant secure-by-design automatically satisfies GDPR Art.25:

| Resolution Element | Implementation Detail |
|--------------------|----------------------|
| Secure Defaults | All products ship with security controls enabled by default |
| **Resolution Type** | **DESIGN_DECISION** — Follow CRA Standard (permanent choice) |
| Configuration Lock | Critical security settings cannot be disabled without explicit admin action |
| Documentation | Security-by-design rationale documented for both CRA and GDPR auditors |
| Evidence | CRA conformity assessment serves as evidence for GDPR Art.25 compliance |

**Risk Owner:** CTO
**Status:** RESOLVED

---

## 5. DETAILED TENSION ANALYSIS

### 5.1 TENSION-H-001: Incident Notification Timelines

**Attributes:**

| Attribute | Value |
|-----------|-------|
| Tension ID | TENSION-H-001 |
| Conflict Type | TEMPORAL_CONFLICT |
| Severity | CRITICAL |
| Sub-Domain | D-04.3 (Incident Escalation) |
| Obligation ID | OBL-D-04.3-001 |
| Source Clauses | GDPR Art.33, CRA Art.14(1-2), CRA Art.14(3-5), NIS 2 Art.23, DORA Art.19 + RTS Art.6, AI Act Art.73 |
| Clause Count | 15 |
| NI (All) | 3 |
| Tension Nature | **CONTEXTUAL** — not always active; depends on event overlap |
| Always Active? | No |
| Overlap Condition | Same factual event triggers notifications from 2+ regulations |

**Root Cause:** Each of the 5 regulations was drafted by different legislative bodies with distinct incident classification frameworks. GDPR focuses on personal data breaches, CRA distinguishes actively exploited vulnerabilities (Art.14(1-2)) from severe incidents (Art.14(3-5)), NIS 2 on essential entity incidents, DORA on ICT-related incidents in financial services (with deadlines specified in RTS 2025/301), and AI Act on high-risk AI system malfunctions (3 tiers: 15d/2d/10d). CRA Art. 15 is "Voluntary reporting" — not a mandatory obligation. The trigger conditions overlap but are not identical, and the notification timelines differ by a factor of 3 (24h vs 72h), with DORA's 4h post-classification being the most stringent.

**Resolution Strategy:**

| Resolution Element | Detail |
|--------------------|--------|
| Strategy Name | Max-SLA Routing |
| Principle | Most stringent deadline (4h post-classification / 24h after discovery) governs all notifications |
| **Resolution Type** | **OPERATIONAL_PROCEDURE** — Max-SLA Routing per-incident |
| Implementation | Single automated workflow with authority-specific templates; CRA dual-flow tracking (Art.14 vs Art.15); AI Act 3-tier escalation (15d/2d/10d) |
| Evidence Required | Notification timestamps, delivery confirmations, template versions, corrective measure availability dates (CRA Art.14) |
| Verification | Quarterly drill testing with all 5 authority types; CRA post-fix clock validation |

**Resolution Evidence:**

| Evidence Type | Description |
|---------------|-------------|
| E-001 | Automated incident classification SOP (centralized audit-log integration) with 5-regulation routing |
| E-002 | Pre-approved notification templates for SA, ENISA, CSIRT, Competent Authority (DORA), MSA |
| E-003 | SLA monitoring dashboard showing 4h/24h compliance for all notification types |
| E-004 | Quarterly drill test results with authority feedback |
| E-005 | CRA dual-flow tracker: Art.14 (14d post-fix) vs Art.15 (1 month) — separate clocks |
| E-006 | AI Act 3-tier escalation: 15d default / 2d widespread / 10d death — causal link documentation |

**Risk Owner:** CISO
**Status:** RESOLVED

---

### 5.2 TENSION-H-002: Erasure vs Immutable Logs

**Attributes:**

| Attribute | Value |
|-----------|-------|
| Tension ID | TENSION-H-002 |
| Conflict Type | REQUIREMENT_CONFLICT |
| Severity | CRITICAL |
| Sub-Domains | D-05.3 (Data Retention) vs D-10.2 (Audit Logging) |
| Obligation IDs | OBL-D-05.3-001 vs OBL-D-10.2-001 |
| Source Clauses | GDPR Art.17, AI Act Art.12, DORA Art.11, CRA Art.14 |
| Clause Count | 8 |
| Avg NI | 3.000 |
| Tension Nature | **STRUCTURAL** — always active; GDPR Art.17 and DORA Art.11 permanently coexist |
| Always Active? | Yes |
| Overlap Condition | N/A — GDPR Art.17 and DORA Art.11 permanently coexist |

**Root Cause:** GDPR Art.17 establishes the "right to be forgotten" as a fundamental data subject right, requiring complete erasure of personal data when requested or when processing is no longer necessary. Conversely, AI Act Art.12 mandates 6-year retention of logs for high-risk AI systems, DORA Art.11 requires immutable audit logs for all ICT activities in financial services, and CRA Art.14 requires activity logging for digital products. Under a traditional centralized logging architecture, it is impossible to selectively delete PII while maintaining an immutable, cryptographically verifiable audit trail.

**Resolution Strategy:**

| Resolution Element | Detail |
|--------------------|--------|
| Strategy Name | Cryptographic Sharding |
| Principle | PII separation at ingestion; key destruction = erasure |
| **Resolution Type** | **DESIGN_DECISION** — Cryptographic Sharding (permanent design choice) |
| Implementation | Log pipeline with PII separation, HSM key management, hash chains |
| Evidence Required | Architecture diagrams, key management SOP, erasure verification reports |
| Verification | Annual pen test of erasure mechanism; hash chain integrity audit |

**Resolution Evidence:**

| Evidence Type | Description |
|---------------|-------------|
| E-005 | Log pipeline architecture diagram showing PII separation point |
| E-006 | HSM key management SOP with per-subject key lifecycle |
| E-007 | Cryptographic hash chain implementation documentation |
| E-008 | Erasure verification test results (key destruction = PII unrecoverable) |
| E-009 | Annual pen test report confirming erasure mechanism integrity |
| E-010 | Hash chain integrity audit results (independent of PII) |

**Risk Owner:** DPO + CISO (joint)
**Status:** RESOLVED

---

### 5.3 TENSION-M-001: Risk Assessment Trigger Divergence

**Attributes:**

| Attribute | Value |
|-----------|-------|
| Tension ID | TENSION-M-001 |
| Conflict Type | FREQUENCY_MISMATCH |
| Severity | MEDIUM |
| Sub-Domain | D-09.2 (Risk Management) |
| Obligation ID | OBL-D-09.2-001 |
| Source Clauses | GDPR Art.35, AI Act Art.43, CRA Art.9, NIS 2 Art.21, DORA Art.6 |
| Clause Count | 9 |
| Avg NI | 2.889 |
| Tension Nature | **STRUCTURAL** — always active; assessment triggers permanently satisfied by bank business model |
| Always Active? | Yes |
| Overlap Condition | N/A — assessment triggers permanently satisfied by bank business model |

**Root Cause:** Each regulation addresses risk assessment from its own domain perspective -- GDPR from data protection, AI Act from fundamental rights, CRA from product security, NIS 2 from operational resilience, and DORA from ICT risk management. While the scopes differ, the core assessment activities (threat identification, impact analysis, control evaluation, residual risk calculation) are substantially overlapping. Running 5 separate assessments would create redundant work, inconsistent findings, and assessment fatigue.

**Resolution Strategy:**

| Resolution Element | Detail |
|--------------------|--------|
| Strategy Name | IPSARA Unified Assessment Framework |
| Principle | Single framework with 4 modular sections mapping to regulatory requirements |
| **Resolution Type** | **DESIGN_DECISION** — IPSARA Framework (permanent process) |
| Implementation | Integrated platform with shared data collection and module-specific outputs |
| Evidence Required | IPSARA framework documentation, module mapping tables, assessment outputs |
| Verification | Annual review of framework completeness against all 5 regulatory requirements |

**Resolution Evidence:**

| Evidence Type | Description |
|---------------|-------------|
| E-011 | IPSARA Framework documentation with 4-module structure |
| E-012 | Module mapping table: IPSARA sections to GDPR/CRA/NIS2/DORA/AI Act |
| E-013 | Shared data collection template (threat catalog, asset inventory, control baseline) |
| E-014 | Module-specific output templates (DPIA report, FRIA report, CRA assessment, ICT risk review) |
| E-015 | Annual framework completeness review against regulatory requirements |

**Risk Owner:** CISO + DPO + AI Governance Lead
**Status:** RESOLVED

---

### 5.4 TENSION-L-001: Secure-by-Design Intensity Gap

**Attributes:**

| Attribute | Value |
|-----------|-------|
| Tension ID | TENSION-L-001 |
| Conflict Type | INTENSITY_GAP |
| Severity | LOW |
| Sub-Domain | D-07.1 (Secure Development Lifecycle) |
| Obligation ID | OBL-D-07.1-001 |
| Source Clauses | GDPR Art.25, CRA Annex I |
| Clause Count | 4 |
| NI Delta | 1.000 |
| Tension Nature | **STRUCTURAL** — always active; secure-by-design always active during design phase |
| Always Active? | Yes |
| Overlap Condition | N/A — secure-by-design always active during design phase |

**Root Cause:** GDPR Art.25 uses flexible, principle-based language ("appropriate technical and organisational measures") allowing organizations to determine what constitutes adequate data protection by design. CRA Annex I uses prescriptive, mandatory language ("secure by default") requiring specific technical configurations. The NI Delta of 1.000 represents the maximum intensity gap in the methodology.

**Resolution Strategy:**

| Resolution Element | Detail |
|--------------------|--------|
| Strategy Name | Follow Higher Bar (CRA Standard) |
| Principle | CRA "secure by default" (NI=3) inherently satisfies GDPR "appropriate measures" (NI=2) |
| **Resolution Type** | **DESIGN_DECISION** — Follow CRA Standard (permanent choice) |
| Implementation | CRA-conformant secure-by-design with documentation mapping to both regulations |
| Evidence Required | CRA conformity assessment report, GDPR Art.25 compliance evidence |
| Verification | CRA audit serves as dual-purpose evidence for both regulations |

**Resolution Evidence:**

| Evidence Type | Description |
|---------------|-------------|
| E-016 | CRA conformity assessment report documenting secure-by-default compliance |
| E-017 | Secure-by-design implementation specification (defaults, configuration locks) |
| E-018 | GDPR Art.25 compliance mapping table referencing CRA assessment |
| E-019 | Product security configuration baseline documentation |

**Risk Owner:** CTO
**Status:** RESOLVED

---

## 6. TENSION SUMMARY BY TYPE

| Conflict Type | Count | Sub-Domains | Regulations Involved |
|---------------|-------|-------------|----------------------|
| TEMPORAL_CONFLICT | 1 | D-04.3 | All 5 (GDPR, CRA, NIS 2, DORA, AI Act) |
| REQUIREMENT_CONFLICT | 1 | D-05.3, D-10.2 | GDPR, AI Act, DORA, CRA |
| FREQUENCY_MISMATCH | 1 | D-09.2 | All 5 (GDPR, CRA, NIS 2, DORA, AI Act) |
| INTENSITY_GAP | 1 | D-07.1 | GDPR, CRA |
| **TOTAL** | **4** | **5 sub-domains** | **5 regulations** |

### 6.1 Tension Summary by Nature

| Nature | Count | Tensions | Resolution Pattern |
|--------|-------|----------|-------------------|
| **Contextual** | 1 | TENSION-H-001 | OPERATIONAL_PROCEDURE (per-incident) |
| **Structural** | 3 | TENSION-H-002, TENSION-M-001, TENSION-L-001 | DESIGN_DECISION (permanent) |
| **TOTAL** | **4** | -- | -- |

### 6.2 Tension Summary by Resolution Type

| Resolution Type | Count | Tensions | Timing |
|-----------------|-------|----------|--------|
| OPERATIONAL_PROCEDURE | 1 | TENSION-H-001 | Per-incident (contextual) |
| DESIGN_DECISION | 3 | TENSION-H-002, TENSION-M-001, TENSION-L-001 | Once at design/planning phase (structural) |

---

## 7. TENSION SUMMARY BY SEVERITY

| Severity | Count | Percentage | Resolution Required |
|----------|-------|------------|---------------------|
| CRITICAL | 2 | 50% | Immediate architectural decision |
| HIGH | 0 | 0% | -- |
| MEDIUM | 1 | 25% | Unified framework design |
| LOW | 1 | 25% | Follow higher bar |
| **TOTAL** | **4** | **100%** | **All resolved** |

---

## 8. RISK OWNERS REGISTER

| Risk Owner ID | Role | Assigned Tensions | Contact | Escalation Path |
|---------------|------|-------------------|---------|-----------------|
| RO-001 | CISO | T-001, T-002 (joint) | ciso@omnibankeu.com | CEO |
| RO-002 | DPO | T-002 (joint), T-003 (joint) | dpo@omnibankeu.com | CRO |
| RO-003 | CTO | T-004 | cto@omnibankeu.com | CEO |
| RO-004 | AI Governance Lead | T-003 (joint) | ai-governance@omnibankeu.com | CRO |

### 8.1 Risk Owner Responsibilities

| Risk Owner | Primary Responsibilities | Tension-Specific Duties |
|------------|-------------------------|------------------------|
| RO-001 (CISO) | Overall security posture, incident management | T-001: Unified incident notification platform; T-002: Cryptographic sharding implementation |
| RO-002 (DPO) | Data protection compliance, privacy rights | T-002: Erasure mechanism validation; T-003: DPIA module in IPSARA |
| RO-003 (CTO) | Technology strategy, development standards | T-004: Secure-by-default implementation across all products |
| RO-004 (AI Governance Lead) | AI Act compliance, AI risk management | T-003: FRIA module in IPSARA, AI system risk assessments |

---

## 9. CROSS-REGULATORY TRIGGER OVERLAY ANALYSIS

For Case 3 (OmniBank: GDPR + CRA + NIS 2 + DORA + AI Act), the number of possible trigger overlap scenarios is the most complex of all three cases. This section documents when contextual tensions would activate.

### 9.1 Notification Trigger Overlay (TENSION-H-001 Context)

| Compound Event Scenario | Triggers GDPR? | Triggers CRA? | Triggers NIS 2? | Triggers DORA? | Triggers AI Act? | Tension Activated? | Resolution |
|-------------------------|---------------|---------------|-----------------|----------------|------------------|-------------------|------------|
| Personal data breach (no product vuln, no AI) | ✅ Yes | ❌ No | ❌ No | ❌ No | ❌ No | No tension — GDPR only (72h to AP) | Standard breach workflow |
| Exploited product vuln (no personal data) | ❌ No | ✅ Yes | ❌ No | ❌ No | ❌ No | No tension — CRA only (24h ENISA) | Standard vuln response |
| Significant incident (no data breach, no vuln) | ❌ No | ❌ No | ✅ Yes | ❌ No | ❌ No | No tension — NIS 2 only (24h CSIRT) | Standard incident response |
| Major ICT incident (no data breach) | ❌ No | ❌ No | ❌ No | ✅ Yes | ❌ No | No tension — DORA only (4h post-classification) | DORA ICT incident workflow |
| AI accuracy degradation (no breach, no vuln) | ❌ No | ❌ No | ❌ No | ❌ No | ✅ Yes | No tension — AI Act only (15d MSA) | AI post-market monitoring |
| **Exploited vuln + personal data exfiltration** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No | ❌ No | **TENSION-H-001 ACTIVATED** (3-reg) | Max-SLA Routing (24h) |
| **Major ICT incident + personal data breach** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes | ❌ No | **TENSION-H-001 ACTIVATED** (3-reg) | Max-SLA Routing (4h) |
| **Exploited vuln + personal data + AI misidentification** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes | **TENSION-H-001 ACTIVATED** (4-reg) | Max-SLA Routing (24h) |
| **Major ICT incident + exploited vuln + data breach** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No | **TENSION-H-001 ACTIVATED** (4-reg) | Max-SLA Routing (4h) |
| **Full 5-reg compound: vuln + breach + ICT disruption + AI failure** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | **TENSION-H-001 ACTIVATED** (5-reg) | Max-SLA Routing (4h) |

### 9.2 Erasure vs Retention Overlay (TENSION-H-002 Context)

Unlike Case 2 where this tension is contextual, in Case 3 the erasure vs retention tension is **structural** — DORA Art.11 mandates immutable audit logs for all ICT activities in financial services, and this obligation permanently coexists with GDPR Art.17 erasure rights. The tension is always active for any OmniBank system that processes personal data and generates audit logs.

| Erasure Request Scenario | GDPR Triggered? | DORA Retention Active? | AI Act Retention Active? | CRA Logging Active? | Tension Activated? | Resolution |
|--------------------------|----------------|------------------------|--------------------------|--------------------|--------------------|------------|
| Customer requests erasure of transaction data (no audit logs) | ✅ Yes | ❌ No | ❌ No | ❌ No | No tension | Standard erasure |
| Customer requests erasure — data exists in ICT audit logs | ✅ Yes | ✅ Yes | ❌ No | ❌ No | **TENSION-H-002 ACTIVE** (structural) | Cryptographic sharding |
| Customer requests erasure — data exists in AI activity logs | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No | **TENSION-H-002 ACTIVE** (DORA+AI Act) | Cryptographic sharding |
| Customer requests erasure — data exists in product activity logs | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | **TENSION-H-002 ACTIVE** (DORA+AI+CRA) | Cryptographic sharding |
| Regulatory audit exception (Art. 17(3)(b)) | ✅ Yes (exempted) | ✅ Yes | ✅ Yes | ✅ Yes | No tension — GDPR Art.17(3)(b) exemption | Retain per regulatory obligation |

### 9.3 Cross-Case Implication

The number of compound event scenarios grows with the number of applicable regulations:

- **Case 1 (TinyTask: 2 regs):** 1 contextual tension, 3 compound events
- **Case 2 (SecureBorder: 4 regs):** 2 contextual tensions, 8+ compound events
- **Case 3 (OmniBank: 5 regs):** 1 contextual tension, 10+ compound events

Case 3 has fewer contextual tensions (1) than Case 2 (2) because the erasure vs logging tension is **structural** in Case 3 (DORA's immutable log mandate permanently coexists with GDPR's erasure right), while it was **contextual** in Case 2 (only activated when a traveler's data existed in AI logs). The addition of DORA transforms this tension from contextual to structural — it is always active for a financial entity, not just when specific events overlap.

The structural tensions also increase: Case 1 has 0 structural tensions (both are contextual), Case 2 has 6 structural tensions, and Case 3 has 3 structural tensions. Each new regulation adds permanent coexistence conflicts with existing obligations.

---

## 10. RESOLUTION DASHBOARD

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Tensions Detected | 4 | -- | -- |
| CRITICAL Priority | 2 | 100% resolved before gate | RESOLVED |
| HIGH Priority | 0 | 100% resolved before gate | N/A |
| MEDIUM Priority | 1 | Framework documented | RESOLVED |
| LOW Priority | 1 | Higher bar selected | RESOLVED |
| Resolved | 4 | 100% | COMPLETE |
| Pending | 0 | 0 | COMPLETE |
| Resolution Rate | 100% | >= 100% | PASS |

### 10.1 Gate Verification

| Gate Criterion | Required | Actual | Status |
|----------------|----------|--------|--------|
| All CRITICAL tensions resolved | Yes | 2/2 resolved | PASS |
| All resolutions have documented rationale | Yes | 4/4 with rationale | PASS |
| All tensions have assigned risk owners | Yes | 4/4 assigned | PASS |
| Resolution evidence identified | Yes | 19 evidence items | PASS |
| **Phase 2 Gate** | **--** | **--** | **PASS** |

---

## 11. DESIGN DECISIONS LOGGED

| Decision ID | Related Tension | Decision Date | Decision Maker | Decision Summary | Alternatives Considered | Rationale | Status |
|-------------|-----------------|---------------|----------------|------------------|------------------------|-----------|--------|
| D-014 | T-001 | 2026-04-03 | CISO | 24h universal incident notification workflow satisfies all 5 regulations | Separate workflows per regulation; tiered SLA approach | Single workflow reduces complexity; 24h covers strictest requirement; pre-approved templates ensure quality | APPROVED |
| D-015 | T-002 | 2026-04-03 | DPO + CISO | Cryptographic sharding resolves erasure vs immutable log retention | Separate log systems; time-bound retention exceptions; anonymization pipeline | Cryptographic separation maintains audit integrity while enabling verifiable erasure; satisfies both GDPR and audit requirements | APPROVED |
| D-016 | T-003 | 2026-04-03 | CISO + DPO + AI Governance Lead | IPSARA unified assessment replaces 5 separate regulatory assessments | Separate assessments per regulation; hybrid assessment (shared + specific) | 4-module framework eliminates redundancy while maintaining regulatory specificity; shared data collection reduces assessment burden by ~60% | APPROVED |
| D-017 | T-004 | 2026-04-03 | CTO | Follow CRA secure-by-default standard (higher bar satisfies GDPR) | GDPR-only approach; parallel secure-by-design implementations | CRA standard is more prescriptive and comprehensive; satisfying CRA automatically satisfies GDPR Art.25; single standard simplifies development | APPROVED |

---

## 12. KEY OBSERVATIONS

1. **All 5 regulations contribute to tensions** -- This confirms the maximum complexity profile of Case 3 (OmniBank). Every regulation appears in at least one tension, demonstrating that the 5-regulation overlap creates genuine architectural conflicts, not just theoretical ones.

2. **T-001 (notification timelines) is the most operationally challenging tension** -- It requires a unified incident management platform capable of classifying incidents, routing notifications to 5 different authority types, and meeting the strictest 24-hour SLA for all. This is a significant infrastructure investment but is manageable with existing centralized audit-log capabilities.

3. **T-002 (erasure vs logs) is the most architecturally significant tension** -- It requires a fundamental redesign of the logging pipeline, introduction of HSM-based key management, and cryptographic hash chain implementation. This is not a superficial control change but a core architectural decision that affects data infrastructure across the organization.

4. **All 4 tensions resolved** -- The Phase 2 Gate criterion (all CRITICAL priority tensions resolved with documented rationale) is satisfied. Each tension has a documented resolution strategy, implementation approach, evidence requirements, and assigned risk owner.

5. **OmniBank's existing ISO 27001/BSI foundation reduces implementation risk** -- The organization's established information security management system provides a foundation for implementing all 4 tension resolutions. The incident management platform (T-001) builds on existing ISO 27001 incident management controls. The cryptographic sharding architecture (T-002) aligns with existing encryption standards. The IPSARA framework (T-003) extends existing risk assessment processes. The CRA secure-by-default standard (T-004) is consistent with existing secure development lifecycle practices.

6. **No HIGH severity tensions detected** -- The tension distribution (2 CRITICAL, 1 MEDIUM, 1 LOW) with no HIGH severity tensions indicates that while there are genuine architectural conflicts, none represent unresolvable contradictions. All tensions have clear resolution patterns.

7. **Resolution patterns are reusable** -- The 4 resolution strategies (Max-SLA Routing, Cryptographic Sharding, IPSARA Framework, Follow Higher Bar) are potentially reusable across other maximum-complexity cases, providing a playbook for future AEGIS implementations.

---

## 13. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-03 | Compliance Lead | Initial Strategic Tensions Report -- 4 tensions detected and resolved (2 CRITICAL, 1 MEDIUM, 1 LOW); Phase 2 Gate PASS |
| 1.1 | 2026-04-11 | Compliance Lead | T-001: Corrected CRA dual flows (Art.14 vulns 14d post-fix vs Art.15 incidents 1mo), added DORA RTS deadlines (4h/72h/1mo per Delegated Reg 2025/301), added AI Act 3-tier reporting (15d/2d/10d death), updated source clauses from 11 to 15, added evidence items E-005/E-006 |
 | 1.2 | 2026-04-11 | Compliance Lead | **C1 fix:** Corrected CRA Art. 15 → Art. 14(3-5) throughout T-001 (Art. 15 is voluntary, not mandatory). Updated Source Clauses, Resolution table (Escalation Path, CRA Dual Flow), Root Cause text. Art. 15 now explicitly noted as voluntary reporting. |
 | 2.0 | 2026-04-16 | Compliance Lead | **Structural/Contextual tension model:** Replaced flat tension model with Structural vs Contextual classification. Added §3 Tension Classification Model (Nature, 5-regulation trigger table, Scenarios A/B, extended tension types). Added §4.1 Tension Classification Summary table. Added Nature/Always Active?/Overlap Condition attributes to all 4 tensions (§4 catalog + §5 detail). Added Resolution Type (OPERATIONAL_PROCEDURE vs DESIGN_DECISION) to all resolution tables. Added §6.1 Summary by Nature, §6.2 Summary by Resolution Type. Added §9 Cross-Regulatory Trigger Overlay Analysis (10 compound scenarios, erasure vs retention overlay, cross-case implications). Reclassified: 1 contextual (TENSION-H-001) + 3 structural (TENSION-H-002, TENSION-M-001, TENSION-L-001). Renumbered §9–§13 → §10–§14. |

---

## 14. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Compliance Lead | [Name] | _______________ | 2026-04-03 |
| CISO | [Name] | _______________ | 2026-04-03 |
| DPO | [Name] | _______________ | 2026-04-03 |
| CTO | [Name] | _______________ | 2026-04-03 |
| Quality Assurance | [Name] | _______________ | 2026-04-03 |
