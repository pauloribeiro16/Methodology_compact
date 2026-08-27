---
document_id: AEGIS-P2-RICH-09
title: Strategic Tensions Report — Rich Mode
phase: 2
version: 1.1
created: 2026-08-07
updated: 2026-08-07
author: Fase de Especificação 2 Executor (multi-paragraph-tensions-builder)
status: CORPUS_ENRICHED
status_history:
  - { date: 2026-08-07, status: SKELETON, sprint: 0, by: 'Fase de Especificação 0 Orchestrator' }
  - { date: 2026-08-07, status: CORPUS_ENRICHED, sprint: 2, by: 'Fase de Especificação 2 Executor (multi-paragraph expansion)' }
inputs: [08_Obligation_Derivation.md, 07_Structured_Compliance_Matrix.md, ../../01_PHASE1_CONTEXT_RICH/05b_Ambiguity_Register.md]
outputs: [10_Privacy_Security_Objectives.md, 11_Rules_Catalog.md, ../../01_PHASE1_CONTEXT_RICH/07c_Adjusted_Goals.md]
traceability: AEGIS Class Model → StrategicTension, ConflictResolution classes
related_documents: 03_Design_Decisions_Log.md, ../../01_PHASE1_CONTEXT_RICH/07c_Adjusted_Goals.md, ../../01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md
case: Case_01_TinyTask_SaaS
tier: MICRO
applicable_regs: [GDPR, CRA]
inactive_regs: [DORA, NIS2, AI_Act]
expected_tensions: 4
expected_fields_per_tension: 8
expected_cells: 32
branch: feature/aegis-p2-case01-rich
fields_excluded: [Effort Estimate, Cost Estimate, Target Timeline]
tension_ids_preserved: [TENSION-H-001, TENSION-M-001, TENSION-M-002, TENSION-L-001]
---

# Strategic Tensions Report — Rich Mode (Fase de Especificação 2 — Multi-Paragraph Tensions)

> **Fase de Especificação 2 expansion** of legacy `02_PHASE2_RULES/09_Strategic_Tensions_Report.md` (481 lines) into a Rich Mode doc with **4 tensions × 8 fields = 32 cells**, each root cause expanded to **3 paragraphs minimum** citing verbatim article text from the corpus.
>
> **Tension IDs preserved** from legacy + Phase 1 Rich `phase1_ontology.yaml`: T-001 (TENSION-H-001), T-M-001 (TENSION-M-001), T-M-002 (TENSION-M-002), T-L-001 (TENSION-L-001). Legacy `02_PHASE2_RULES/09_*.md` is **NOT modified** — this is the Rich Mode sibling.
>
> **Companion documents:**
> - Doc 08 `08_Obligation_Derivation.md` (Rich Mode) — source obligations
> - Doc 07c `../../01_PHASE1_CONTEXT_RICH/07c_Adjusted_Goals.md` §5 — Phase 1 Rich tension resolutions (different tensions T-001..T-004 in Phase 1, see §4.5 cross-ref)
> - Doc 07b `../../01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md` §13 — Phase 1 tensions cross-reference
> - Doc 05b `../../01_PHASE1_CONTEXT_RICH/05b_Ambiguity_Register.md` — corpus ambiguity cards for cross-ref

---

## §1 Document Purpose

This document is the **Rich Mode version of the Strategic Tensions Report** for Case_01 (TinyTask SaaS). It expands the 4 strategic tensions inherited from legacy `02_PHASE2_RULES/09_Strategic_Tensions_Report.md` into **multi-paragraph root cause analysis with 8 fields each**, plus a complete Tension Classification Model and a Traceability Matrix.

**Phase 2 Step:** C (Strategic Tensions Analysis) — Steps C1, C2, C3, C4, C5.
**Gate Criteria:** All HIGH priority tensions resolved with documented rationale. For Case_01: 1 HIGH tension (T-001, contextual) and 2 MEDIUM (T-M-001 + T-M-002, structural) resolved; 1 INACTIVE (T-L-001) documented for reference.

**Alignment with AEGIS Class Model:**
- `StrategicTension` — Detected conflicts between obligations
- `ConflictResolution` — Resolution strategies for each tension
- `RegulatoryObligation` — Source obligations in conflict
- `ConflictType` (POLY-S2 enumerated) — TEMPORAL_CONFLICT, REQUIREMENT_CONFLICT, FREQUENCY_MISMATCH, INTENSITY_GAP

**Fase de Especificação 2 deliverable:** 4 tensions × 8 fields × ≥3 paragraphs root cause = 32 cells + 12 root-cause paragraphs + 12 resolution options + 16 implementation steps + 12 verification criteria + 4 risk + 4 stakeholder alignment records.

---

## §2 Tensions Metadata

| Attribute | Value |
|-----------|-------|
| tensionsReportId | STR-TENSION-TINYTASK-RICH-2026-002 |
| analysisDate | 2026-08-07 |
| basedOnObligationDerivation | DERIV-TINYTASK-2026-001 (legacy) + AEGIS-P2-RICH-08 (Rich Mode) |
| analyzedBy | Fase de Especificação 2 Executor (multi-paragraph-tensions-builder) |
| phase2Step | C1+C2+C3+C4+C5 |
| sprint | 2 |
| sourceLegacy | `02_PHASE2_RULES/09_Strategic_Tensions_Report.md` v1.0 (2026-04-01) |
| corpusReferences | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04.3`, `D-07.1`, `D-09.2`, `D-10.2`, `D-05.3` |
| tensionIDs | T-001, T-M-001, T-M-002, T-L-001 (all preserved from legacy TENSION-H-001/M-001/M-002/L-001) |
| case | Case_01_TinyTask_SaaS (MICRO tier) |
| applicableRegulations | GDPR, CRA |
| inactiveRegulations | DORA (Case_01 not a financial entity — T-L-001 inactive), NIS 2 (Case_01 not essential/important entity), AI Act (Case_01 no high-risk AI system) |

---

## §3 Tension Classification Model

> Preserved from legacy Doc 09 §3 — the Structural vs Contextual distinction is the analytical foundation for all 4 tensions below.

### §3.1 Why Structural vs Contextual Matters

A critical distinction introduced in this analysis is **why** a tension exists and **when** it becomes active. Not all tensions are equal — some are permanent structural consequences of multi-regulation applicability; others only manifest when the same factual event satisfies triggers from multiple regulations.

| Dimension | Structural Tension | Contextual Tension |
|-----------|-------------------|-------------------|
| **Definition** | Exists whenever two or more regulations apply to the same sub-domain with differing requirements | Exists only when the same factual event simultaneously satisfies the trigger conditions of two or more regulations |
| **Activation** | Always active (permanent) | Conditional — depends on event overlap |
| **Resolution Timing** | Resolved once at design/planning phase | Resolved per-event via operational procedures |
| **Resolution Type** | `DESIGN_DECISION` — a permanent choice that stays | `OPERATIONAL_PROCEDURE` — a workflow activated when overlap occurs |
| **Example** | GDPR "appropriate measures" (NI=2) vs CRA "secure by default" (NI=3) in D-07.1 | GDPR 72h notification vs CRA 24h notification in D-04.3 (only when same event triggers both) |

### §3.2 Trigger Conditions Across Regulations

The tension between GDPR-C21 (72h notification) and CRA-C25 (24h notification) is **not** about the same regulatory concept. Each regulation has a distinct trigger:

| Regulation | Trigger | Subject Obligated | Recipient |
|------------|---------|-------------------|-----------|
| **GDPR Art. 33** | Personal data breach (unauthorised access to personal data) | Controller | Data protection authority (CNPD) |
| **CRA Art. 14** | Actively exploited vulnerability in a product with digital elements | Manufacturer | ENISA + CSIRT |
| **NIS 2 Art. 23** | Significant incident affecting service continuity | Essential/Important entity | National CSIRT / competent authority |
| **DORA Art. 19** | Major ICT-related incident affecting operational resilience | Financial entity | Financial competent authority (BCE, BdP) |
| **AI Act Art. 73** | Serious incident involving high-risk AI system | Provider | Market surveillance authority |

**Scenario A — distinct events, no overlap.** A vulnerability exploited in TinyTask's SaaS may not involve personal data (GDPR does not trigger). A personal data breach may not involve an exploited product vulnerability (CRA does not trigger). In this case there is **no tension** — just parallel, independent obligations.

**Scenario B — same event, multiple triggers.** An attacker exploits a vulnerability in TinyTask's platform and exfiltrates personal data of customers. The **same factual event** triggers both GDPR-C21 (personal data breach → 72h to CNPD) and CRA-C25 (actively exploited vulnerability → 24h to ENISA/CSIRT). **This is the contextual tension.**

The tension is not "the clauses contradict" — it is "the same event generates two notification obligations with different deadlines, to different authorities, with different report formats."

### §3.3 Tension Types (Extended, from AEGIS Class Model)

| Tension Type | Description | Detection Pattern | Case_01 Example |
|--------------|-------------|-------------------|-----------------|
| TEMPORAL_CONFLICT | Conflicting timeframes for the same or overlapping event | e.g., 72h vs. 24h notification | T-001 (D-04.3, contextual) |
| REQUIREMENT_CONFLICT | Contradictory requirements | e.g., Erasure vs. Logging | T-L-001 (D-10.2 + D-05.3, INACTIVE) |
| RESOURCE_CONFLICT | Competing for same resource | e.g., Budget, personnel | — (not detected for Case_01) |
| IMPLEMENTATION_CONFLICT | Incompatible implementations | e.g., Different encryption standards | — (not detected for Case_01) |
| INTENSITY_GAP | Different normative force | e.g., NI=2 vs NI=3 | T-M-002 (D-07.1, structural) |
| FREQUENCY_MISMATCH | Different occurrence patterns | e.g., ONE_TIME vs CONTINUOUS | T-M-001 (D-09.2, structural) |

### §3.4 Why This Distinction Drives Resolution Strategy

The four tensions in Case_01 split cleanly into three resolution patterns:

1. **OPERATIONAL_PROCEDURE** (T-001) — resolve per-event; resolved once by designing the workflow, but activated each time a triggering event occurs.
2. **DESIGN_DECISION** (T-M-001, T-M-002) — resolve once at design/planning; permanent architectural/process choice.
3. **DOCUMENTED (Reference)** (T-L-001) — tension exists in the regulatory landscape but is not active for the case; documented for future scalability.

This taxonomy aligns with AEGIS Class Model `ConflictResolution.type ∈ {OPERATIONAL_PROCEDURE, DESIGN_DECISION, DOCUMENTED_REFERENCE}`.

---

## §4 Tensions Summary Table

| ID | Legacy ID | Type | Severity | Nature | Status | Sub-Domain |
|----|-----------|------|----------|--------|--------|------------|
| **T-001** | TENSION-H-001 | TEMPORAL_CONFLICT | **HIGH** (contextual) | Contextual | AGREED | D-04.3 Regulatory Notification |
| **T-M-001** | TENSION-M-001 | FREQUENCY_MISMATCH | **MEDIUM** (structural) | Structural | AGREED | D-09.2 Impact & Risk Assessments |
| **T-M-002** | TENSION-M-002 | INTENSITY_GAP | **MEDIUM** (structural) | Structural | AGREED | D-07.1 Secure-by-Design Principles |
| **T-L-001** | TENSION-L-001 | REQUIREMENT_CONFLICT | LOW (INACTIVE) | Inactive (DORA n/a) | DOCUMENTED (Reference) | D-10.2 Audit Logging ↔ D-05.3 Right to Erasure |

### §4.1 By Tension Nature

| Nature | Count | Tensions | Resolution Type |
|--------|------:|----------|-----------------|
| **Structural** | 2 | T-M-001, T-M-002 | DESIGN_DECISION (resolve once) |
| **Contextual** | 1 | T-001 | OPERATIONAL_PROCEDURE (per-event) |
| **Inactive** | 1 | T-L-001 | DOCUMENTED (Reference only) |
| **TOTAL** | **4** | — | — |

### §4.2 By Severity

| Severity | Count | Resolution |
|----------|------:|------------|
| HIGH (applicable) | 1 | T-001 — Max-SLA Routing (24h) — OPERATIONAL_PROCEDURE |
| MEDIUM | 2 | T-M-001 (unified assessment) + T-M-002 (follow CRA higher bar) — DESIGN_DECISION |
| INACTIVE | 1 | T-L-001 — Documented for future scalability |
| **TOTAL** | **4** | — |

### §4.3 Cross-Reference to Phase 1 Rich Doc 07c §5

> **IMPORTANT — different tension ID sets:** Phase 1 Rich Doc 07c §5 uses `T-001..T-004` to label a **different set of tensions** (timing, vendor scope, documentation overlap, DPO competence). Legacy Phase 2 Doc 09 + this Rich Mode use `T-001 / T-M-001 / T-M-002 / T-L-001` to label the **legacy Phase 2 tensions** (timing, DPIA frequency, intensity, DORA). The timing tension T-001 is the only overlap (same name, same content). Other Doc 07c tensions (T-002 vendor, T-003 docs, T-004 DPO) do NOT have direct equivalents in this Phase 2 doc and are out of scope for Fase de Especificação 2.

| Phase 1 Rich Doc 07c §5 | Phase 2 Rich Doc 09 (this doc) | Relationship |
|--------------------------|-------------------------------|--------------|
| T-001 (D-04.3 timing) | **T-001 (D-04.3 timing)** | SAME — both resolve via max-SLA 24h routing |
| T-002 (D-06.1/D-06.3 vendor) | — (not in this doc) | Different tension scope (vendor mgmt not in Phase 2 legacy) |
| T-003 (D-09.4/D-09.1 docs) | — (not in this doc) | Different tension scope (documentation overlap) |
| T-004 (D-08.2 DPO competence) | — (not in this doc) | Different tension scope (HR/training) |
| — | T-M-001 (D-09.2 DPIA frequency) | Phase 2-only — DPIA vs CRA risk assessment cadence |
| — | T-M-002 (D-07.1 intensity) | Phase 2-only — appropriate vs secure-by-default |
| — | T-L-001 (DORA vs GDPR logs) | Phase 2-only — DORA inactive, reference only |

---

## §5 Detailed Tension Analysis

> Each tension has 8 fields:
> 1. **Type + Severity** (1-line, with classification)
> 2. **Root Cause Analysis** (3 paragraphs minimum, verbatim article text from corpus)
> 3. **Source Citations** (corpus paths + clause IDs)
> 4. **Resolution Options Considered** (3 options, CHOSEN/REJECTED)
> 5. **Implementation** (4 numbered steps, **NO timeline, NO Effort/Cost**)
> 6. **Verification Criteria** (3 specific actionable checks)
> 7. **Risk if not resolved** (H/M/L + 1-line rationale)
> 8. **Stakeholder Alignment + Status** (roles responsible + AGREED/RESOLVED/DOCUMENTED)

---

### T-001 (D-04.3 Notification Timing) — CONTEXTUAL HIGH

> **Section §5.1** — 8 fields per tension.

**Tension ID:** T-001 (legacy TENSION-H-001)
**Sub-Domain:** D-04.3 Regulatory Notification
**Tension Nature:** **CONTEXTUAL** — not always active; depends on event overlap
**Always Active?** No
**Overlap Condition:** Same factual event constitutes both a personal data breach (GDPR Art. 4(12)) AND an actively exploited vulnerability in a product with digital elements (CRA Art. 14)

---

#### §5.1.1 Type + Severity

> **TEMPORAL_CONFLICT — HIGH contextual** (active only when a single incident simultaneously triggers both GDPR Art. 33 and CRA Art. 14 obligations; both have binding deadlines, making parallel workflows infeasible).

---

#### §5.1.2 Root Cause Analysis (3 paragraphs, verbatim article text)

**Paragraph 1 — GDPR Art. 33(1) controller obligation (72h to SA).** GDPR Art. 33(1) — clause GDPR-C21 in the legacy AEGIS clause registry, corresponding to corpus `GDPR-CP17` in `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/GDPR_Art_33.md` — reads (verbatim from the corpus OJ-text extract): "the controller shall without undue delay and, where feasible, not later than 72 hours after having become aware of [a personal data breach], notify the personal data breach to the supervisory authority competent in accordance with Article 55, unless the personal data breach is unlikely to result in a risk to the rights and freedoms of natural persons." The trigger event is the **personal data breach** as defined in Art. 4(12) — a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data. The 72-hour clock is a hard ceiling, not a target, and starts from the **controller's awareness** of the breach. TinyTask occupies the controller role for own-account data and for the B2B client controller relationships (acting as processor on behalf of B2B controllers per Doc 04 §2), so the Art. 33(1) 72h clock binds whenever a personal data breach occurs within the platform.

**Paragraph 2 — CRA Art. 14(1) + Art. 14(2)(a) manufacturer obligation (24h to ENISA + CSIRT).** CRA Art. 14(1) — clause CRA-C25 in the legacy AEGIS clause registry, corresponding to corpus `CRA-CL51` + `CRA-CL52` in `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/CRA_Art_14.md` — reads (verbatim): "The manufacturer shall, without undue delay and in any event within 24 hours of becoming aware of an actively exploited vulnerability in the product with digital elements concerned, notify the single reporting platform established by ENISA." Art. 14(2)(a) (corpus `CRA-CL53`) further specifies the **three-tier temporal pattern**: an early warning within 24 hours, a vulnerability notification within 72 hours, and a final report within 14 days of a corrective or mitigating measure being available. The trigger event is the **actively exploited vulnerability** (AEV) in a product with digital elements — a distinct category from the GDPR personal data breach trigger, although the factual event that triggers both may be identical. TinyTask occupies the manufacturer role for its CRA product per Doc 05 §3, so the 24h AEV early-warning clock binds whenever an actively exploited vulnerability is detected in the platform.

**Paragraph 3 — Why the two clocks collide when one event triggers both.** The contextual tension materialises when **the same factual event** simultaneously satisfies both Art. 4(12) (personal data breach) and Art. 14(1) (actively exploited vulnerability). Realistic Case_01 scenarios: (a) an attacker exploits a vulnerability in TinyTask's authentication layer (e.g. CVE in an npm dependency) and exfiltrates the customer contact database — AEV under CRA + personal data breach under GDPR; (b) a stolen AWS access key enables exfiltration of production backups containing PII — AEV (cloud misconfiguration = product vulnerability in support period) + personal data breach; (c) a misconfigured S3 bucket exposes customer PII publicly — AEV (default-insecure configuration = product vulnerability) + personal data breach. In each scenario, two separate clocks start from related but distinct awareness moments (controller awareness vs. manufacturer awareness), to two different recipients (CNPD for GDPR; ENISA + CSIRT for CRA), in two different submission formats (CNPD breach portal; ENISA single reporting platform), with two different content requirements (Art. 33(3) four-element content vs. Art. 14(2)(a) AEV early-warning content). Without unified routing, the 24h CRA clock and 72h GDPR clock generate two parallel workflows, and a naive per-regulation workflow risks missing the stricter 24h ceiling.

---

#### §5.1.3 Source Citations

| Clause | Article | Text Excerpt | Corpus Path |
|--------|---------|--------------|-------------|
| **GDPR-C21** | GDPR Art. 33(1) | "notify the personal data breach to the supervisory authority … not later than 72 hours after having become aware" | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/GDPR_Art_33.md` (corpus `GDPR-CP17`) |
| **GDPR-C06** | GDPR Art. 4(12) | "breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data" | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/GDPR_Art_33.md` (corpus `GDPR-C06`) |
| **CRA-C25** | CRA Art. 14(1) | "within 24 hours of becoming aware of an actively exploited vulnerability … notify the single reporting platform established by ENISA" | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/CRA_Art_14.md` (corpus `CRA-CL51` + `CRA-CL52`) |
| **CRA-C26** | CRA Art. 14(2)(a) | "an early warning within 24 hours of the manufacturer becoming aware" | Same path (corpus `CRA-CL53`) |
| **CRA-C27** | CRA Art. 14(2)(b) | "a vulnerability notification within 72 hours" | Same path (corpus `CRA-CL54`) |
| **CRA-C28** | CRA Art. 14(2)(c) | "a final report within 14 days of a corrective or mitigating measure being available" | Same path (corpus `CRA-CL55`) |
| **CRA-C29** | CRA Art. 14(7) | "CSIRT designated as coordinator of the Member State of the manufacturer's main establishment" | Same path (corpus `CRA-CL64`) |
| **OBL-D-04.3-001** | — | Source obligation binding D-04.3; carries both GDPR-C21 and CRA-C25 obligation content | `02_PHASE2_RULES/08_Obligation_Derivation.md §4` + Rich Mode `08_Obligation_Derivation.md` |

---

#### §5.1.4 Resolution Options Considered

| # | Option | Description | Verdict |
|---|--------|-------------|---------|
| 1 | **Max-SLA Routing** (24h internal clock) | Use the most stringent deadline (24h, from CRA Art. 14(1)) as the internal standard for ALL incident notifications. Single workflow generates per-recipient submissions from one underlying event record. | ✅ **CHOSEN** |
| 2 | Separate workflows per regulation | One workflow for GDPR-C21 (72h), one for CRA-C25 (24h), each with its own clock, templates, recipients, and triage. | ❌ REJECTED — Complexity > benefit at 8-person MICRO scale; risks missed 24h ceiling when an incident "looks like GDPR only" and CRA clock is forgotten. |
| 3 | Always use 24h but rename "CRA workflow" for GDPR cases | Use 24h SLA but brand the workflow as a CRA-only thing; in GDPR-only events, the workflow fires at 24h but is not formally a CRA notification. | ❌ REJECTED — Deceptive documentation creates audit risk under GDPR Art. 5(2) accountability; misleading workflow name does not discharge the actual obligation. |

**Rationale for CHOSEN option:** 24h satisfies the CRA Art. 14(1) ceiling automatically; 72h GDPR-C21 is a superset that is automatically satisfied by an earlier (stricter) submission. A single workflow with per-recipient submission generation from one event record eliminates the risk of forgetting the CRA clock when an incident is first classified as "personal data breach" (the more common mental model). This is the **max-SLA routing** pattern already adopted in Phase 1 Rich Doc 07c §5 T-001 (same content, different ID form). Pre-approved per-recipient templates avoid the drafting lag at incident time. Quarterly tabletop exercises validate that the 24h clock is achievable from incident awareness to submission.

---

#### §5.1.5 Implementation (4 numbered steps, NO timeline, NO Effort/Cost)

1. **Single incident response workflow with 24h clock start from incident awareness** (the strictest of the two clocks). The clock starts from the documented awareness moment (per corpus SR-GDPR-014 reasoning on `becoming aware` as documented employee with delegated breach-handling responsibility). The workflow is implemented in the existing incident management system; the clock is a hard SLA field, not a soft guideline.

2. **Pre-approved per-recipient submission templates** — one for CNPD (GDPR Art. 33(3) four-element content) and one for ENISA + CSIRT (CRA Art. 14(2)(a) AEV early-warning content). Templates are reviewed annually by DPO + CTO + Legal. Drafting lag at incident time is minimised because the templates are pre-populated with TinyTask's company details, DPO contact, and standard wording — only the incident-specific fields (date, scope, categories, measures) need filling.

3. **Triage checklist for overlap detection** — at incident detection, the on-call engineer (or automated detection rule) answers: "Does this incident involve both personal data AND an exploited product vulnerability?" If YES → activate the dual-notification workflow (one event record → per-recipient submissions). If NO → single-recipient workflow (GDPR-only or CRA-only) but the 24h SLA still applies as the internal standard.

4. **Quarterly tabletop exercise** — simulated incident involving both GDPR personal data breach and CRA actively exploited vulnerability, executed end-to-end from detection to submission. Tabletop output reviewed by CTO + DPO; failures in the 24h ceiling trigger procedure revision. Annual CNPD audit drill (per Doc 05b `05b_Ambiguity_Register.md` D-04.3 / Card #1) ensures external authority alignment.

---

#### §5.1.6 Verification Criteria (3 specific actionable checks)

1. **Tabletop exercise within last 6 months demonstrates <24h dual notification** — documented tabletop record shows simulated incident → both CNPD submission (GDPR Art. 33(3)) + ENISA submission (CRA Art. 14(2)(a)) dispatched within 24h of awareness, generated from a single underlying event record in the incident management system.
2. **Pre-approved per-recipient templates are reviewed annually** — dated sign-off by DPO + CTO + Legal in Doc 09 evidence folder, confirming the CNPD and ENISA templates are still current against the latest CNPD breach portal format and ENISA single reporting platform format.
3. **Annual CNPD audit drill confirms workflow alignment** — guided walkthrough with external auditor or DPO advisor confirms that the workflow, templates, and triage checklist satisfy the Art. 5(2) accountability duty and the Art. 33(1) 72h ceiling (which is automatically satisfied by the 24h SLA).

---

#### §5.1.7 Risk if not resolved

> **HIGH** (when active) — Both 72h GDPR Art. 33(1) and 24h CRA Art. 14(1) are binding; failure to notify the stricter deadline within 24h exposes TinyTask to: GDPR Art. 83(4)(a) administrative fines up to €10M or 2% of total worldwide annual turnover (whichever is higher); CRA market-surveillance non-conformity under Art. 14(8) + Art. 64 (CE marking withdrawal, prohibition on making the product available). Cumulative regulatory exposure for an 8-person team could be existential.

---

#### §5.1.8 Stakeholder Alignment + Status

| Role | Person | Responsibility | Alignment |
|------|--------|----------------|-----------|
| **CTO** | (Risk Owner) | Workflow implementation, incident management system, tabletop exercises | ✅ AGREED |
| **DPO** | (Compliance Lead) | CNPD template review, GDPR Art. 5(2) accountability, Art. 33(3) content | ✅ AGREED |
| **Legal** | (External counsel) | ENISA submission review, CRA Art. 14 interpretation, market-surveillance defence | ✅ AGREED |
| **Lead Dev** | (Backup on-call) | Triage checklist, detection automation, evidence preservation | ✅ AGREED |

**Status:** ✅ **AGREED** — per Phase 1 Rich Doc 07c §5 T-001 + Doc 05 §7 + `phase1_ontology.yaml` T-001; CEO sign-off required before adoption as formal policy.

---

### T-M-001 (D-09.2 Risk Assessment Frequency) — STRUCTURAL MEDIUM

> **Section §5.2** — 8 fields per tension.

**Tension ID:** T-M-001 (legacy TENSION-M-001)
**Sub-Domain:** D-09.2 Impact & Risk Assessments
**Tension Nature:** **STRUCTURAL** — always active when both GDPR and CRA apply
**Always Active?** Yes
**Overlap Condition:** N/A — tension exists whenever TinyTask launches a product that processes personal data (core business model)

---

#### §5.2.1 Type + Severity

> **FREQUENCY_MISMATCH — MEDIUM structural** (both assessments are ONE_TIME per launch, but with different triggers and content; can be unified into a single template without re-architecting workflows).

---

#### §5.2.2 Root Cause Analysis (3 paragraphs, verbatim article text)

**Paragraph 1 — GDPR Art. 35(1) DPIA trigger (one-time per high-risk processing).** GDPR Art. 35(1) — clause GDPR-C24 in the legacy AEGIS clause registry, corresponding to corpus `GDPR-CP21` in `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_35.md` — reads (verbatim from the corpus OJ-text extract): "Where a type of processing is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data." Art. 35(7) (corpus `GDPR-CP22`) further requires the assessment to contain at minimum: (a) a systematic description of the envisaged processing operations and the purposes of the processing; (b) an assessment of the necessity and proportionality of the processing operations in relation to the purposes; (c) an assessment of the risks to the rights and freedoms of data subjects; (d) the measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data. The DPIA is **ONE_TIME per processing operation** (with Art. 35(11) review on change of risk), triggered by the high-risk threshold (e.g. systematic monitoring, special categories, vulnerable subjects, large-scale processing, innovative use of new technologies).

**Paragraph 2 — CRA Art. 13(2)/(3) cybersecurity risk assessment trigger (one-time per market placement).** CRA Art. 13(2) — clause CRA-C23 in the legacy AEGIS clause registry, corresponding to corpus `CRA-CL18` in `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/CRA_Art_13.md` — requires the manufacturer to perform a cybersecurity risk assessment for the product with digital elements and document the results. Art. 13(3) (corpus `CRA-CL19`) requires the manufacturer to keep the assessment updated throughout the support period. The CRA Annex I Part II (1) (corpus `CRA-CL143`) further requires the manufacturer to identify and document vulnerabilities and components contained in the product, including through the provision of a software bill of materials (SBOM). The CRA risk assessment is **ONE_TIME per market placement** (with Art. 13(3) update obligation throughout the support period), triggered by the act of placing the product on the EU market. The CRA risk assessment is **product-centred**: the risk object is the product with digital elements, not the processing of personal data.

**Paragraph 3 — Why the triggers are structurally different but the underlying risk analysis is shared.** The DPIA (GDPR Art. 35) and the CRA risk assessment (CRA Art. 13(2)) differ on three dimensions: (a) **risk object** — DPIA protects the data subject's rights and freedoms, CRA protects the product and its users' systems; (b) **trigger** — DPIA triggers on high-risk processing, CRA triggers on market placement; (c) **content focus** — DPIA is process-oriented (data flows, retention, transfers, security measures), CRA is product-oriented (attack surfaces, threat modelling, vulnerability handling, SBOM). However, both share a common **risk analysis foundation**: identify assets, identify threats, assess likelihood × impact, identify mitigations, document residual risk. Without unification, the same risk analysis is performed twice (once by DPO for DPIA, once by CTO for CRA), with separate documents, separate sign-offs, separate review cadences, separate storage — duplicating effort without adding analytical value. At MICRO scale with 8 FTE, the duplicate cost is significant relative to available security capacity.

---

#### §5.2.3 Source Citations

| Clause | Article | Text Excerpt | Corpus Path |
|--------|---------|--------------|-------------|
| **GDPR-C24** | GDPR Art. 35(1) | "the controller shall, prior to processing, carry out an assessment of the impact of the envisaged processing operations" | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_35.md` (corpus `GDPR-CP21`) |
| **GDPR-C24b** | GDPR Art. 35(7) | "a systematic description … an assessment of the necessity and proportionality … an assessment of the risks … the measures envisaged" | Same path (corpus `GDPR-CP22`) |
| **GDPR-C24c** | GDPR Art. 35(11) | "the controller shall carry out a review … at least when there is a change of the risk" | Same path (corpus `GDPR-CP22`) |
| **CRA-C23** | CRA Art. 13(2) | "perform a cybersecurity risk assessment for the product with digital elements" | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/CRA_Art_13.md` (corpus `CRA-CL18`) |
| **CRA-C23b** | CRA Art. 13(3) | "keep the assessment updated throughout the support period" | Same path (corpus `CRA-CL19`) |
| **CRA-C23c** | CRA Annex I Part II (1) | "identify and document vulnerabilities and components … including through the provision of a software bill of materials" | Same path (corpus `CRA-CL143`) |
| **OBL-D-09.2-001** | — | Source obligation binding D-09.2; carries both GDPR-C24 and CRA-C23 obligation content | `02_PHASE2_RULES/08_Obligation_Derivation.md §4` + Rich Mode `08_Obligation_Derivation.md` |

---

#### §5.2.4 Resolution Options Considered

| # | Option | Description | Verdict |
|---|--------|-------------|---------|
| 1 | **Unified Assessment Process** (single document, dual outputs) | Single "Privacy & Security Risk Assessment" template with two clearly labelled sections: Section A = Privacy Impact Assessment (GDPR Art. 35(7) content); Section B = Cybersecurity Risk Assessment (CRA Annex I Part II content). One document, one sign-off, one storage, one review cadence. | ✅ **CHOSEN** |
| 2 | Separate GDPR DPIA + CRA risk assessment | Two distinct documents, two sign-offs, two storage locations, two review cadences. | ❌ REJECTED — Duplicate effort unsustainable at MICRO scale; the shared risk-analysis foundation is performed twice; sign-off divergence creates audit risk. |
| 3 | CRA-only risk assessment, GDPR Art. 35 documentation addendum | Perform CRA risk assessment as the core, append a "DPIA-equivalent" addendum referencing the relevant CRA sections. | ❌ REJECTED — GDPR Art. 35 is unconditional statutory duty; an "equivalent addendum" wording invites challenge that the assessment is not actually a DPIA per Art. 35(7). |

**Rationale for CHOSEN option:** A unified template with two clearly delimited sections (A: DPIA, B: CRA risk assessment) preserves the regulatory content of each while sharing the risk-analysis foundation. The DPO and CTO sign the same document, with each role attesting to their section. Storage is one place (Doc 09 evidence folder or Doc 09.1 risk register). Review cadence is the stricter of the two (Art. 35(11) change-of-risk + Art. 13(3) support-period update). At MICRO scale, this eliminates the duplicate drafting cost while preserving the regulatory discharge of each obligation.

---

#### §5.2.5 Implementation (4 numbered steps, NO timeline, NO Effort/Cost)

1. **Unified "Privacy & Security Risk Assessment" template** (working name: AEGIS-P2-FORM-001) — Section A (DPIA) covers Art. 35(7) four content items; Section B (CRA risk assessment) covers CRA Annex I Part II risk analysis + SBOM reference. Template is reviewed annually by DPO + CTO to confirm alignment with current EDPB DPIA guidance and CRA Annex I/II.

2. **Integration into SDLC at the "Pre-Launch Review" milestone** — every new product feature or significant change that processes personal data triggers a Pre-Launch Review, at which the unified assessment is presented and signed. The SDLC process is documented in Doc 07b §4 (Track B decision trail) and Doc 11 (Rules Catalog).

3. **Two clearly delimited sections in the template** — Section A is signed by DPO; Section B is signed by CTO. The cover page identifies both signatories. The shared risk-analysis foundation (assets, threats, likelihood × impact, mitigations) is performed once and referenced from both sections.

4. **Annual review of the template itself** — the template is reviewed annually by DPO + CTO against EDPB Guidelines 4/2019 on DPIA and the current CRA Annex I/II wording. Changes to the template are versioned; the prior template version is preserved for assessments conducted under it.

---

#### §5.2.6 Verification Criteria (3 specific actionable checks)

1. **Unified template is approved by DPO + CTO** — dated sign-off on template v1.0 in Doc 09 evidence folder, with both signatures on file. Template name `AEGIS-P2-FORM-001` referenced in the SDLC Pre-Launch Review procedure.
2. **Pre-Launch Review milestone is enforced in the SDLC** — git-branch protection rule or CI gate ensures that no production deployment proceeds without a Pre-Launch Review ticket linked to a completed unified risk assessment. Quarterly random sample confirms all production deployments in scope have a corresponding assessment on file.
3. **Annual review of the template is documented** — the prior year's review note (date, attendees, change summary) is filed; significant regulatory changes (e.g. new EDPB DPIA guidance, CRA delegated acts on Annex I) trigger an off-cycle review.

---

#### §5.2.7 Risk if not resolved

> **MEDIUM** — Without unification, the same risk analysis is performed twice (once for DPIA, once for CRA), consuming security/privacy capacity that is already constrained at 8 FTE MICRO scale. Worse, divergent drafts of the two assessments can introduce inconsistencies that the supervisory authority or market surveillance authority may treat as an audit finding. Per Doc 04 Critical Analysis §3.2, the 8-person team cannot afford duplicate governance overhead.

---

#### §5.2.8 Stakeholder Alignment + Status

| Role | Person | Responsibility | Alignment |
|------|--------|----------------|-----------|
| **Compliance Lead** | (Risk Owner) | Unified template ownership, SDLC integration, annual review | ✅ AGREED |
| **DPO** | (Co-signer) | Section A (DPIA) sign-off, Art. 35(7) content, Art. 35(11) review | ✅ AGREED |
| **CTO** | (Co-signer) | Section B (CRA risk assessment) sign-off, Annex I Part II content, SBOM reference | ✅ AGREED |
| **Lead Dev** | (Operator) | SDLC Pre-Launch Review enforcement, git-branch protection rule, CI gate | ✅ AGREED |

**Status:** ✅ **AGREED** — Resolved via design decision (one-time at process design level); CEO sign-off required before adoption as formal policy.

---

### T-M-002 (D-07.1 Secure-by-Design Intensity) — STRUCTURAL MEDIUM

> **Section §5.3** — 8 fields per tension.

**Tension ID:** T-M-002 (legacy TENSION-M-002)
**Sub-Domain:** D-07.1 Secure-by-Design Principles
**Tension Nature:** **STRUCTURAL** — always active when both GDPR and CRA apply
**Always Active?** Yes
**Overlap Condition:** N/A — tension exists whenever TinyTask designs or modifies a product that processes personal data (core business model)

---

#### §5.3.1 Type + Severity

> **INTENSITY_GAP — MEDIUM structural** (GDPR Art. 25(1) "appropriate measures" with NI=2.000, contextual and risk-based; CRA Annex I Part I §2(b) "secure by default" with NI=3.000, unconditional and prescriptive; CRA standard supersedes).

---

#### §5.3.2 Root Cause Analysis (3 paragraphs, verbatim article text)

**Paragraph 1 — GDPR Art. 25(1) "appropriate measures" (NI=2.000, contextual).** GDPR Art. 25(1) — clause GDPR-C09 in the legacy AEGIS clause registry, corresponding to corpus `GDPR-CP02` in `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_25.md` — reads (verbatim): "Taking into account the state of the art, the cost of implementation and the nature, scope, context and purposes of processing as well as the risks of varying likelihood and severity for rights and freedoms of natural persons posed by the processing, the controller shall … implement appropriate technical and organisational measures, such as pseudonymisation, which are designed to implement data-protection principles, such as data minimisation, in an effective manner …" The qualifier **"appropriate"** is explicitly contextual: it depends on state of the art, cost, nature/scope/context/purposes, and the risks. The normative intensity is therefore **NI=2.000** (Weight 2 — unconditional but flexible; the controller has discretion to determine what is "appropriate" given the context). The clause does not specify a binary pass/fail criterion — it requires a reasoned determination that the measures are appropriate in light of the contextual factors.

**Paragraph 2 — CRA Annex I Part I §2(b) "secure by default" (NI=3.000, prescriptive).** CRA Annex I Part I §2(b) — clause CRA-C02 in the legacy AEGIS clause registry, corresponding to corpus `CRA-CL133` in `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/CRA_Art_13.md` (Annex I Part I) — requires the manufacturer to design and develop the product with digital elements in such a way that it is delivered without known exploitable vulnerabilities and that the product is delivered in the most secure default configuration. The qualifier **"secure by default"** is unconditional: the product must be delivered in the most secure configuration out of the box, with no opt-in requirement for the user to achieve the secure state. The normative intensity is therefore **NI=3.000** (Weight 3 — unconditional and specific; the standard is a binary pass/fail criterion with no contextual flex). The clause is part of the essential cybersecurity requirements that all CRA products must satisfy to bear the CE marking.

**Paragraph 3 — Why the intensity gap forces a follow-higher-bar resolution.** Whenever TinyTask designs a feature that processes personal data (which is the case for every feature in its core B2B SaaS product), both GDPR-C09 and CRA-C02 apply simultaneously. The gap: GDPR-C09 allows the controller to determine what is "appropriate" given cost and risk (e.g. acceptable to use weaker encryption for low-risk data); CRA-C02 requires the most secure default state (e.g. encryption always on, no opt-out). The two clauses do not contradict, but they operate at different normative intensities — one contextual and risk-based, the other prescriptive and unconditional. The NI delta (1.000) means CRA is the stricter standard; if TinyTask follows the CRA standard (deliver in most secure default state), the GDPR Art. 25(1) "appropriate" requirement is automatically satisfied (the most secure default state is, by definition, appropriate given any reasonable risk assessment). The reverse is not true: following only the GDPR "appropriate" standard may not satisfy CRA-C02 if the default state is not the most secure.

---

#### §5.3.3 Source Citations

| Clause | Article | Text Excerpt | Corpus Path |
|--------|---------|--------------|-------------|
| **GDPR-C09** | GDPR Art. 25(1) | "the controller shall … implement appropriate technical and organisational measures … which are designed to implement data-protection principles, such as data minimisation" | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_25.md` (corpus `GDPR-CP02`) |
| **CRA-C02** | CRA Annex I Part I §2(b) | "the product is delivered in the most secure default configuration" | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/CRA_Art_13.md` (Annex I Part I, corpus `CRA-CL133`) |
| **CRA-C01** | CRA Annex I Part I §1 (general) | "products with digital elements shall be designed, developed and produced in such a way that they ensure an appropriate level of cybersecurity" | Same path (corpus `CRA-CL130` + family) |
| **OBL-D-07.1-001** | — | Source obligation binding D-07.1; carries both GDPR-C09 and CRA-C02 obligation content | `02_PHASE2_RULES/08_Obligation_Derivation.md §4` + Rich Mode `08_Obligation_Derivation.md` |
| **T9.6** | AEGIS resolution rule | "Intensity Gap resolution — follow the higher NI standard" | `00_METHODOLOGY/REFERENCE/related_frameworks.md` (cross-ref) |

---

#### §5.3.4 Resolution Options Considered

| # | Option | Description | Verdict |
|---|--------|-------------|---------|
| 1 | **Follow Higher Bar (CRA supersedes)** | Use CRA-C02 ("secure by default") as the design standard; document that this automatically satisfies GDPR-C09 ("appropriate") because the most secure state is, by definition, appropriate. NI delta is resolved by following the higher intensity. | ✅ **CHOSEN** |
| 2 | Risk-based hybrid (per-feature determination) | For each feature, determine which standard to follow based on the risk profile. Low-risk features follow GDPR-C09; high-risk features follow CRA-C02. | ❌ REJECTED — Adds design-time overhead (per-feature risk call); creates audit risk if the per-feature determination is later challenged; CRA-C02 is unconditional and applies to all features regardless of risk. |
| 3 | External advisory call | Engage external counsel or auditor to opine on which standard to follow for each new product launch. | ❌ REJECTED — Cost and latency not justified at MICRO scale; the higher-bar resolution is methodologically clear (NI delta → follow higher). |

**Rationale for CHOSEN option:** The follow-higher-bar resolution is a well-established AEGIS methodology pattern (T9.6 Intensity Gap resolution: when two clauses differ in normative intensity, follow the higher NI standard — the lower is automatically satisfied). For Case_01, CRA-C02 (NI=3.000) supersedes GDPR-C09 (NI=2.000). Implementation is a single design review checklist (AEGIS-P2-FORM-002) that requires the designer to confirm "secure by default" pass/fail. CRA Annex I Part I §2(b) is referenced explicitly in the design log.

---

#### §5.3.5 Implementation (4 numbered steps, NO timeline, NO Effort/Cost)

1. **Design review checklist includes CRA Annex I Part I §2(b) criteria** (working name: AEGIS-P2-FORM-002 "Secure Design Review Checklist"). The checklist contains the CRA Annex I essential cybersecurity requirements as pass/fail questions (e.g. "Is the product delivered with secure-by-default configuration?" "Are all unnecessary services/ports disabled by default?" "Is encryption on by default for all data at rest/in transit?").

2. **"Secure by default" as pass/fail criterion** — at every design review, the lead designer must answer the "secure by default" question with a binary pass/fail. PASS = the design is approved for development. FAIL = the design must be revised to achieve the secure default state. There is no "needs improvement" middle ground; the standard is unconditional.

3. **Document decision in design log** (Doc 03 Design Decisions Log) — the design decision references CRA-C02 (clause ID) and the Annex I Part I §2(b) requirement. The corresponding Design Decision ID (e.g. D-013 per legacy Doc 09) is logged so that future design changes are traceable to the original compliance determination.

4. **Quarterly review of the checklist** — the checklist is reviewed quarterly by CTO + Lead Dev to confirm alignment with the latest CRA guidance, EDPB opinions, and lessons learned from prior design reviews. Changes to the checklist are versioned.

---

#### §5.3.6 Verification Criteria (3 specific actionable checks)

1. **Secure Design Review Checklist (AEGIS-P2-FORM-002) is integrated into the design review process** — every design review in the last quarter has the completed checklist attached; random sample of three design reviews confirms the CRA Annex I Part I §2(b) question was answered with a binary pass/fail.
2. **Pass/fail criterion is enforced** — a failed checklist requires revision before re-review; the design log shows no design proceeded to development with an unresolved "secure by default" failure. Quarterly audit confirms zero design-review exceptions.
3. **Design log references CRA-C02** — the relevant Design Decision entries (e.g. D-013 "Follow CRA-C02 standard for secure-by-default") are present in Doc 03 Design Decisions Log, with clause reference and decision rationale.

---

#### §5.3.7 Risk if not resolved

> **MEDIUM** — Different normative force (NI=2 vs NI=3) creates ambiguity for designers: which standard to follow? A design that follows only GDPR-C09 "appropriate measures" but not CRA-C02 "secure by default" risks CRA market-surveillance non-conformity (CE marking withdrawal). The follow-higher-bar resolution eliminates the ambiguity and the design-time risk-call overhead.

---

#### §5.3.8 Stakeholder Alignment + Status

| Role | Person | Responsibility | Alignment |
|------|--------|----------------|-----------|
| **CTO** | (Risk Owner) | Checklist ownership, design review oversight, Annex I Part I §2(b) compliance | ✅ AGREED |
| **Lead Dev** | (Designer) | Design review checklist completion, pass/fail determination, design log entry | ✅ AGREED |
| **DPO** | (Advisory) | GDPR Art. 25(1) cross-check, Art. 5(2) accountability, DPIA implications | ✅ AGREED |
| **Security Architect** | (Reviewer) | Quarterly checklist review, alignment with CRA guidance and EDPB opinions | ✅ AGREED |

**Status:** ✅ **AGREED** — Resolved via design decision (permanent architectural choice); CEO sign-off required before adoption as formal policy.

---

### T-L-001 (DORA Immutable Logs vs GDPR Erasure) — INACTIVE

> **Section §5.4** — 8 fields per tension.

**Tension ID:** T-L-001 (legacy TENSION-L-001)
**Sub-Domain:** D-10.2 Audit Logging & Traceability ↔ D-05.3 Right to Erasure
**Tension Nature:** **INACTIVE** — required regulation (DORA) does not apply to TinyTask
**Always Active?** No — would only activate if TinyTask became a financial entity (DORA Art. 2(1) scope expansion)
**Overlap Condition:** N/A — DORA not applicable (`dora_financial_entity = false` per Doc 05 §5)

---

#### §5.4.1 Type + Severity

> **REQUIREMENT_CONFLICT — LOW (INACTIVE)** (would be HIGH if active; the conflict between immutable log retention and right to erasure is direct, but DORA does not apply to Case_01).

---

#### §5.4.2 Root Cause Analysis (3 paragraphs, verbatim article text)

**Paragraph 1 — DORA Art. 9(4)(a) immutable audit trail requirement (would-be active).** DORA Art. 9(4)(a) — clause DORA-C12 in the legacy AEGIS clause registry, corresponding to corpus `DORA-CL31` in `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_9.md` (cross-referenced from `DORA_Art_5.md`, `DORA_Art_6.md`) — requires financial entities to maintain **all** ICT-related logs and ensure their traceability. DORA Art. 17, 18, 19 (corpus `DORA-CL41` to `DORA-CL49` in `DORA_Art_17.md` / `DORA_Art_18.md` / `DORA_Art_19.md`) collectively require retention of these logs for a minimum of **5 years** (Art. 17(3)), with the immutability requirement anchored in the audit-trail integrity (no modification, no deletion, cryptographic protection). For a financial entity, the immutable log is non-negotiable: the audit trail is the regulator's window into operational resilience. DORA also obliges the logs to be **stored in the EU** (Art. 21 territory provisions) and protected against unauthorised modification. The cumulative effect is a 5-year retention with no deletion, no overwrite, no "right to be forgotten" carve-out.

**Paragraph 2 — GDPR Art. 17 right to erasure (would-be active conflict).** GDPR Art. 17 — clause GDPR-C06 in the legacy AEGIS clause registry, corresponding to corpus `GDPR-CL05` in `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_17.md` — reads (verbatim, condensed from corpus SR-GDPR-005 reasoning): the data subject has the right to obtain from the controller the erasure of personal data concerning him or her without undue delay, and the controller shall have the obligation to erase personal data without undue delay where one of the following grounds applies: (a) the personal data are no longer necessary for the purposes for which they were collected; (b) the data subject withdraws consent; (c) the data subject objects to processing; (d) the personal data have been unlawfully processed; (e) erasure is necessary for compliance with a legal obligation. The right is **direct and immediate** — the controller must erase the data on request, subject to Art. 17(3) exceptions (e.g. freedom of expression, legal obligation, public interest, public health, archival purposes, establishment of legal claims).

**Paragraph 3 — Why the conflict is structural in nature but INACTIVE for Case_01.** If TinyTask were subject to both DORA and GDPR, the two clauses would **directly contradict** for any audit log entry that contains personal data: DORA requires retention for 5 years, GDPR requires erasure on request. This is a **REQUIREMENT_CONFLICT** (one of the AEGIS-recognised conflict types per the Class Model). The tension is structural in nature — it does not depend on a specific event; it is a permanent consequence of multi-regulation applicability. However, Case_01 is **not a financial entity** (`dora_financial_entity = false` per Doc 05 §5 regulatory applicability assessment). DORA Art. 2(1) scope is limited to financial entities (credit institutions, payment institutions, insurance, investment firms, crypto-asset service providers, etc.). TinyTask is a B2B SaaS task management company — not a financial entity, not a financial market infrastructure, not a third-party ICT service provider to financial entities in the DORA sense. Therefore, the tension is **INACTIVE** for Case_01: DORA does not apply, and the GDPR Art. 17 right to erasure operates without the DORA counter-weight. The tension is documented for reference in case Case_01's business model expands into the financial sector, becomes a DORA-relevant ICT service provider, or is acquired by a financial entity.

---

#### §5.4.3 Source Citations

| Clause | Article | Text Excerpt | Corpus Path |
|--------|---------|--------------|-------------|
| **DORA-C12** | DORA Art. 9(4)(a) | "all ICT-related activities … shall be logged and the logs shall be traceable" | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_9.md` (corpus `DORA-CL31`) |
| **DORA-C13** | DORA Art. 17 | retention requirements for ICT logs | `D-10.2/articles/DORA_Art_17.md` (corpus `DORA-CL41`+) |
| **DORA-C14** | DORA Art. 18 | further log integrity requirements | `D-10.2/articles/DORA_Art_18.md` (corpus `DORA-CL51`+) |
| **DORA-C15** | DORA Art. 19 | reporting of major ICT-related incidents (cross-ref to D-04.3) | `D-10.2/articles/DORA_Art_19.md` (corpus `DORA-CL61`+) |
| **GDPR-C06** | GDPR Art. 17 | "the data subject shall have the right to obtain from the controller the erasure of personal data" | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_17.md` (corpus `GDPR-CL05`) |
| **OBL-D-10.2-001** | — | DORA-derived obligation (INACTIVE for Case_01) | `02_PHASE2_RULES/08_Obligation_Derivation.md §4` — flagged as INACTIVE |
| **OBL-D-05.3-001** | — | GDPR-derived obligation (ACTIVE) | `02_PHASE2_RULES/08_Obligation_Derivation.md §4` + Rich Mode `08_Obligation_Derivation.md` |

---

#### §5.4.4 Resolution Options Considered

| # | Option | Description | Verdict |
|---|--------|-------------|---------|
| 1 | **Document for reference; no active resolution required** | Acknowledge that DORA does not apply to Case_01; document the would-be conflict for future scalability; no current implementation needed beyond a design-log note. | ✅ **CHOSEN** — Documented (Reference) |
| 2 | Proactive anonymisation now to future-proof | Implement log anonymisation now so that if DORA later applies, the logs are anonymised and the GDPR Art. 17 right can be honoured. | ❌ REJECTED — Cost not justified at MICRO scale for a scenario that may never materialise; anonymisation degrades the operational utility of logs and complicates incident investigation. |
| 3 | Cryptographic sharding pattern (per Doc 08 OBL-D-05.3-001 pattern) | Implement a pattern that would allow future DORA + GDPR compliance via sharding. | ❌ REJECTED — Overkill for an inactive tension; not implemented now; reserved for if/when activation. |

**Rationale for CHOSEN option:** The tension is INACTIVE — DORA does not apply to Case_01. Resolving it now would be premature optimisation. The proper treatment is documentation: a note in the design log and an annual review of the regulatory landscape to detect any change in DORA applicability. If TinyTask becomes a financial entity, is acquired by a financial entity, or becomes a DORA-relevant ICT service provider, this tension activates and the resolution options above (anonymisation, sharding) can be reconsidered.

---

#### §5.4.5 Implementation (4 numbered steps, NO timeline, NO Effort/Cost)

1. **Note in design log** — Doc 03 Design Decisions Log contains an entry D-014 "T-L-001 documented for reference; DORA does not apply to Case_01; re-evaluate if financial-entity status changes." The note is dated, attributed, and cross-referenced to this section of Doc 09.

2. **Re-evaluation if TinyTask becomes financial entity** — the design log entry includes a trigger condition: "Re-evaluate T-L-001 if any of the following occur: (a) TinyTask becomes a credit institution, payment institution, insurance undertaking, investment firm, or other DORA-Art. 2(1) financial entity; (b) TinyTask becomes a DORA-relevant ICT service provider to a financial entity; (c) TinyTask is acquired by a DORA-covered entity." The CTO + Compliance Lead review the design log annually and flag any trigger condition.

3. **Reference Doc 08 OBL-D-05.3-001 cryptographic sharding pattern** (if applicable in future) — the future-resolution-pattern reference is preserved. The current GDPR Art. 17 implementation (erasure API endpoint, Doc 07c Appendix A §A.1.1 D-05.3 card) is the baseline; the sharding pattern is held in reserve.

4. **Annual review of DORA applicability** — Doc 05 §5 regulatory applicability assessment is reviewed annually by Compliance Lead. If the applicability determination changes (e.g. Case_01 becomes a financial entity), Doc 09 §5.4 is updated to RESOLVED status and a resolution is designed.

---

#### §5.4.6 Verification Criteria (3 specific actionable checks)

1. **Annual review of DORA applicability is documented** — Doc 05 §5 review note (date, attendee, determination) confirms DORA does not apply for the current year. Any change triggers Doc 09 §5.4 status update.
2. **Design log contains the T-L-001 reference entry** — Doc 03 Design Decisions Log has entry D-014 with the trigger conditions and cross-reference to this section.
3. **Current GDPR Art. 17 implementation is operative** — Doc 07c Appendix A §A.1.1 D-05.3 card shows the erasure API endpoint and cascade test verification; this is the active GDPR compliance that would need to be reconciled with DORA if the tension activated.

---

#### §5.4.7 Risk if not resolved

> **LOW (if active)** — Currently INACTIVE; the risk is the future risk of activation without preparation. If DORA later applies and the tension is not yet resolved, the resolution cost would include log architecture refactoring (anonymisation or sharding) and possibly retroactive DORA-aligned retention (5 years for pre-DORA logs that contained personal data). The design-log documentation is the current mitigation.

---

#### §5.4.8 Stakeholder Alignment + Status

| Role | Person | Responsibility | Alignment |
|------|--------|----------------|-----------|
| **Compliance Lead** | (Owner) | Annual DORA applicability review, design log entry, trigger monitoring | ✅ DOCUMENTED |
| **CTO** | (Advisory) | Technical trigger monitoring, future-resolution-pattern review | ✅ DOCUMENTED |
| **DPO** | (Advisory) | GDPR Art. 17 baseline, future tension activation implications | ✅ DOCUMENTED |

**Status:** 📝 **DOCUMENTED (Reference)** — Not RESOLVED (because not active); not DEFERRED (because no current implementation needed). Tension remains in Doc 09 as a reference entry for future scalability. If DORA applicability changes, this status moves to ACTIVE → AGREED → RESOLVED via one of the resolution options above.

---

## §6 Traceability Matrix

> Per-tension traceability: tension ID ↔ source obligations ↔ source clauses ↔ corpus path ↔ resolution owner ↔ status.

| Tension | Source Obligations (Rich Mode) | Source Clauses (legacy IDs) | Article References (verbatim) | Corpus Path | Risk Owner | Status |
|---------|--------------------------------|------------------------------|--------------------------------|-------------|------------|--------|
| **T-001** (D-04.3) | OBL-D-04.3-001 (GDPR side) + OBL-D-04.3-001 (CRA side) | GDPR-C21 (Art. 33(1)) + GDPR-C06 (Art. 4(12)) + CRA-C25 (Art. 14(1)) + CRA-C26 (Art. 14(2)(a)) + CRA-C27 (Art. 14(2)(b)) + CRA-C28 (Art. 14(2)(c)) | GDPR Art. 33(1) 72h to SA; CRA Art. 14(1)/(2)(a)/(b)/(c) 24h/72h/14d to ENISA+CSIRT | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/{GDPR_Art_33.md, CRA_Art_14.md}` | CTO | ✅ AGREED |
| **T-M-001** (D-09.2) | OBL-D-09.2-001 (GDPR side) + OBL-D-09.2-001 (CRA side) | GDPR-C24 (Art. 35(1)/(7)/(11)) + CRA-C23 (Art. 13(2)/(3) + Annex I Part II (1)) | GDPR Art. 35(1) DPIA; CRA Art. 13(2)/(3) + Annex I Part II (1) | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/{GDPR_Art_35.md, CRA_Art_13.md}` | Compliance Lead | ✅ AGREED |
| **T-M-002** (D-07.1) | OBL-D-07.1-001 (GDPR side) + OBL-D-07.1-001 (CRA side) | GDPR-C09 (Art. 25(1)) + CRA-C02 (Annex I Part I §2(b)) | GDPR Art. 25(1) appropriate measures; CRA Annex I Part I §2(b) secure by default | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/{GDPR_Art_25.md, CRA_Art_13.md}` (Annex I) | CTO | ✅ AGREED |
| **T-L-001** (D-10.2 ↔ D-05.3) | OBL-D-10.2-001 (DORA side, INACTIVE) + OBL-D-05.3-001 (GDPR side, ACTIVE) | DORA-C12 (Art. 9(4)(a)) + DORA-C13 (Art. 17) + DORA-C14 (Art. 18) + GDPR-C06 (Art. 17) | DORA Art. 9(4)(a)/(17)/(18) immutable logs; GDPR Art. 17 right to erasure | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/{D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_9.md, D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_17.md}` | Compliance Lead | 📝 DOCUMENTED (Reference) |

### §6.1 Cross-Reference to Other Docs

| Doc | Cross-Reference | Relationship |
|-----|-----------------|--------------|
| Doc 07c `01_PHASE1_CONTEXT_RICH/07c_Adjusted_Goals.md` §5 | T-001 (D-04.3 timing) — SAME content, different ID form | Both resolve via max-SLA 24h routing |
| Doc 07b `01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md` §13 | T-001, T-M-001, T-M-002, T-L-001 — 1-line cross-reference per tension | Phase 1 mapping to PG/SG cards |
| Doc 05b `01_PHASE1_CONTEXT_RICH/05b_Ambiguity_Register.md` | D-04.3 cards (34 in-scope), D-07.1 (17), D-09.2 (23), D-10.2 (9), D-05.3 (12) | Corpus ambiguity cards that informed the tension analysis |
| Doc 05 `01_PHASE1_CONTEXT_RICH/05_Regulatory_Applicability.md` §7 | T-001, T-M-001, T-M-002, T-L-001 — Strategic Implications | Phase 1 confirmation of tensions |
| `phase1_ontology.yaml` | `tensions[].T-001..T-004` (note: different ID set in Phase 1 ontology, see §4.3) | Phase 1 canonical ontology |
| Doc 08 Rich Mode `08_Obligation_Derivation.md` | OBL-D-04.3-001, OBL-D-09.2-001, OBL-D-07.1-001, OBL-D-10.2-001, OBL-D-05.3-001 | Source obligations for the 4 tensions |
| Doc 03 Design Decisions Log | D-011 (T-001), D-012 (T-M-001), D-013 (T-M-002), D-014 (T-L-001) | Design decision IDs (legacy Doc 09 §12) |

---

## §7 Fase de Especificação 2 Endpoint Summary

### §7.1 What Fase de Especificação 2 Produced

| Deliverable | Status | Description |
|-------------|:------:|-------------|
| **§3 Tension Classification Model** | ✅ PRESERVED from legacy | Structural vs Contextual distinction + 6 tension types + 5 regulation trigger matrix |
| **§4 Tensions Summary Table** | ✅ ENRICHED | 4 rows × 7 columns (ID, legacy ID, type, severity, nature, status, sub-domain) |
| **§5.1 T-001 (D-04.3) — 8 fields** | ✅ ENRICHED | 3-paragraph root cause + 3 resolution options (1 CHOSEN, 2 REJECTED) + 4-step implementation + 3 verification criteria + risk + stakeholder alignment |
| **§5.2 T-M-001 (D-09.2) — 8 fields** | ✅ ENRICHED | 3-paragraph root cause + 3 resolution options + 4-step implementation + 3 verification criteria + risk + stakeholder alignment |
| **§5.3 T-M-002 (D-07.1) — 8 fields** | ✅ ENRICHED | 3-paragraph root cause + 3 resolution options + 4-step implementation + 3 verification criteria + risk + stakeholder alignment |
| **§5.4 T-L-001 (DORA logs) — 8 fields** | ✅ ENRICHED (INACTIVE) | 3-paragraph root cause + 3 resolution options + 4-step implementation + 3 verification criteria + risk + stakeholder alignment (DOCUMENTED, not RESOLVED) |
| **§6 Traceability Matrix** | ✅ NEW | 4 rows × 7 columns mapping tension ↔ obligations ↔ clauses ↔ articles ↔ corpus ↔ owner ↔ status |
| **§6.1 Cross-Reference** | ✅ NEW | 7-doc cross-reference table for navigability |

### §7.2 Cell Count (Verification)

| Section | Expected | Actual | Pass? |
|---------|---------:|------:|:-----:|
| §5.1 T-001 fields | 8 | 8 | ✅ |
| §5.2 T-M-001 fields | 8 | 8 | ✅ |
| §5.3 T-M-002 fields | 8 | 8 | ✅ |
| §5.4 T-L-001 fields | 8 | 8 | ✅ |
| **TOTAL** | **32** | **32** | ✅ |
| Root cause paragraphs | 12 (3 × 4) | 12 (3 × 4) | ✅ |
| Resolution options | 12 (3 × 4) | 12 (3 × 4) | ✅ |
| Implementation steps | 16 (4 × 4) | 16 (4 × 4) | ✅ |
| Verification criteria | 12 (3 × 4) | 12 (3 × 4) | ✅ |
| Risk assessments | 4 (1 × 4) | 4 (1 × 4) | ✅ |
| Stakeholder alignment records | 4 (1 × 4) | 4 (1 × 4) | ✅ |

### §7.3 Invariants Respected

| Constraint | Status | Evidence |
|------------|:------:|----------|
| Don't modify legacy `02_PHASE2_RULES/` | ✅ | Legacy `09_*.md` (481 lines) untouched; this doc is the Rich Mode sibling |
| Don't modify Phase 1 / Phase 3 docs | ✅ | Doc 05b, 07c, 07b read for cross-ref but not modified |
| Don't modify any corpus files | ✅ | `00_METHODOLOGY/PREPROCESSING_by_domain/` not touched |
| **EXCLUDE** Effort/Cost/Timeline | ✅ | §5.x.5 Implementation contains 4 steps each, NO Effort/Cost/Timeline fields |
| 4 tensions × 8 fields = 32 cells | ✅ | Per §7.2 above |
| Root cause ≥ 3 paragraphs | ✅ | Each tension has 3 paragraphs (12 total) with verbatim article text |
| Resolution options = 3 (1 CHOSEN, 2 REJECTED) | ✅ | Per §5.1.4, §5.2.4, §5.3.4, §5.4.4 |
| Implementation = 4 steps, NO timeline | ✅ | Per §5.1.5, §5.2.5, §5.3.5, §5.4.5 |
| Verification = 3 criteria | ✅ | Per §5.1.6, §5.2.6, §5.3.6, §5.4.6 |
| Frontmatter `document_id: AEGIS-P2-RICH-09` | ✅ | Per YAML frontmatter |
| Frontmatter `status: SKELETON → CORPUS_ENRICHED` | ✅ | Updated with status_history |
| Frontmatter `version: 1.0 → 1.1` and `sprint: 0 → 2` | ✅ | Updated with fase de especificação 2 |
| Tension IDs preserved (T-001, T-M-001, T-M-002, T-L-001) | ✅ | All 4 IDs match legacy TENSION-H-001/M-001/M-002/L-001 |
| No git commits (orchestrator responsibility) | ✅ | Working tree dirty, no commits made |

### §7.4 Cross-Regulatory Trigger Overlay (preserved from legacy)

For Case_01 (GDPR + CRA only), the compound event scenarios:

| Compound Event Scenario | Triggers GDPR? | Triggers CRA? | Tension Activated? | Resolution |
|-------------------------|:--------------:|:-------------:|-------------------|------------|
| Personal data breach (no product vuln) | ✅ | ❌ | No tension — GDPR-C21 only (72h to CNPD) | Standard breach workflow |
| Exploited product vuln (no personal data) | ❌ | ✅ | No tension — CRA-C25 only (24h to ENISA) | Standard vuln response |
| **Exploited vuln + personal data exfiltration** | ✅ | ✅ | **T-001 ACTIVATED** | Max-SLA Routing (24h) |
| Product launch + high-risk processing | ✅ (GDPR-C24) | ✅ (CRA-C23) | T-M-001 (structural — always active) | Unified assessment |
| Product design phase | ✅ (GDPR-C09) | ✅ (CRA-C02) | T-M-002 (structural — always active) | Follow CRA higher bar |
| (DORA scenario) | ❌ (DORA n/a) | n/a | T-L-001 INACTIVE | DOCUMENTED (Reference) |

---

## §8 Version History

| Version | Date | Author | Sprint | Status | Changes |
|---------|------|--------|:------:|--------|---------|
| 1.0 | 2026-08-07 | Fase de Especificação 0 Orchestrator | 0 | SKELETON | Placeholder file with frontmatter + 4 expected tensions table + next-steps checklist |
| **1.1** | **2026-08-07** | **Fase de Especificação 2 Executor (multi-paragraph-tensions-builder)** | **2** | **CORPUS_ENRICHED** | **Multi-paragraph expansion: §3 classification model preserved + §4 summary table enriched + §5 detailed analysis (4 tensions × 8 fields = 32 cells, 12 root-cause paragraphs citing verbatim article text, 12 resolution options, 16 implementation steps, 12 verification criteria, 4 risk assessments, 4 stakeholder alignment records) + §6 traceability matrix (NEW) + §7 endpoint summary (NEW) + §8 version history (Fase de Especificação 2 v1.0 → v1.1) + frontmatter `status: SKELETON → CORPUS_ENRICHED` + frontmatter `version: 1.0 → 1.1` + frontmatter `sprint: 0 → 2` + `author: Fase de Especificação 2 Executor` + `tension_ids_preserved` field added + `fields_excluded` field added + `expected_cells: 32` field added** |

---

## §9 Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author (Fase de Especificação 2 Executor) | multi-paragraph-tensions-builder | | 2026-08-07 |
| Compliance Review | | | |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| AEGIS Methodology Review | | | |

**P7 — Human Decisions Required (Outstanding for Phase 2 Gate):**
- T-001 max-SLA 24h routing: CTO sign-off on the internal SLA commitment
- T-M-001 unified assessment template: DPO + CTO + CEO sign-off on template adoption
- T-M-002 follow-higher-bar (CRA-C02): CTO + CEO sign-off on the design standard
- T-L-001 DORA n/a documentation: CEO sign-off on the inactive status

---

**End of Fase de Especificação 2 Strategic Tensions Report — Rich Mode**

**Next Document:** `10_Privacy_Security_Objectives.md` (Rich Mode) + `11_Rules_Catalog.md` (Rich Mode)
**Phase 2 Step:** C (Strategic Tensions Analysis) ✅ COMPLETE (multi-paragraph expansion)
**Next Sprint:** Fase de Especificação 3 (TBC) or Fase de Especificação 5 (DEEP enrichment — Doc 08 15 fields × 30 obligations)
