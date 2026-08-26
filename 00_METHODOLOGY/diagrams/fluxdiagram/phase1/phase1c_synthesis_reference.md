---
document_id: AEGIS-DIAG-P1C-REFERENCE
title: "Phase 1C — Synthesis Reference: Conflict Framework & Compound Event Methodology"
phase: Phase 1C (reference companion)
version: 1.2
created: 2026-06-15
updated: 2026-07-13
status: ACTIVE
parent_diagram: phase1c_consolidation.md
source: Cross-case analysis (Doc 07 from all 3 cases)
related_documents:
  - phase1c_consolidation.md
  - phase1c_proportionality_synthesis.md
  - ../../../PHASE1_STRATEGY.md
  - ../../../REFERENCE/proportionality_model.md
  - ../../PROMPTS/P1C-LLM-01-OVERLAP-CLASSIFICATION.md
  - ../../PROMPTS/P1C-LLM-02-COMPOUND-EVENT.md
  - ../../PROMPTS/P1C-LLM-03-STRATEGIC-SYNTHESIS.md
  - ../../../PREPROCESSING/SubDomains/index.md
changes: |
  v1.2 (2026-07-13): Status CREATED → ACTIVE. Version 1.1 → 1.2. Added Legacy ID Cross-walk (LLM-H marked REMOVED) and Authority Caveat section. Cross-references to PROMPTS/ prompt templates (3 LLMs).
  v1.1 (2026-07-13): Bumped version + updated date + status CREATED → ACTIVE. Renamed phase to "Phase 1C (reference companion)" for clarity. Added cross-references to phase1c_synthesis.md and phase1c_proportionality_synthesis.md.
changes: |
  v1.1 (2026-07-13):
  - Bumped version + updated date
  - Added cross-references to phase1c_synthesis.md and phase1c_proportionality_synthesis.md (v1.1 additions)
  - Renamed phase to "Phase 1C (reference companion)" for clarity
---

# Phase 1C — Synthesis Reference

**Version:** 1.0 — 2026-06-15
**Companion to:** [`phase1c_consolidation.md`](phase1c_consolidation.md) (flow diagrams + LLM spec tables)
**Sources:** Doc 07 from Case 01, Case 02, Case 03 + Template 07

---

## Overview

This file is the **reference companion** to the Phase 1C detailed flow diagrams. It contains the analytical frameworks that LLM-E and LLM-F use to classify regulatory interactions and identify compound events:

1. **Conflict Classification Framework** — the 3-type taxonomy (Synergistic / Structural / Contextual) with identification criteria and resolution patterns
2. **Compound Event Methodology** — how to identify, verify, and resolve events that trigger multiple regulations
3. **Strategic Tensions Catalog** — all tensions identified across the 3 case studies
4. **Cross-Case Scaling Analysis** — how synthesis complexity grows with regulation count

---

## 1. Conflict Classification Framework

### 1.1 Overview

When two or more regulations cover the same sub-domain, their relationship falls into exactly one of three types. This classification determines how the overlap is resolved:

```
2+ regs cover same sub-domain
         │
    ┌────┴────┐
    │         │
Requirements  Requirements
compatible?   differ?
    │              │
   YES            YES
    │         ┌────┴────┐
    │     Always     Only when
    │    differ?    same event?
    │         │         │
    ▼         ▼         ▼
SYNERGISTIC  STRUCTURAL  CONTEXTUAL
            TENSION      TENSION
```

### 1.2 Type 1: Synergistic (Complementarity)

**Definition:** Two or more regulations reinforce each other with compatible requirements. Implementing the highest standard satisfies all regulations simultaneously.

**Identification criteria:**
- Same sub-domain covered by 2+ regulations
- Requirements are aligned (same security goal)
- No tension between scope, frequency, or depth
- Implementing the strictest NI requirement satisfies all

**Examples from case studies:**

| Sub-Domain | Regulations | Why Synergistic | Resolution |
|---|---|---|---|
| D-01.1 Data at Rest Encryption | GDPR + CRA + NIS 2 + DORA + AI Act | All require encryption; AES-256 satisfies all | Single encryption standard |
| D-01.2 Data in Transit Encryption | GDPR + CRA + NIS 2 + DORA + AI Act | All require TLS; TLS 1.3 satisfies all | Single TLS configuration |
| D-03.1 Identity Lifecycle | GDPR + CRA | Both require access management | Unified IAM |
| D-05.1 Data Minimization | GDPR + CRA | Both require minimal data collection | Single data classification scheme |
| D-10.3 Compliance Testing | GDPR + CRA + NIS 2 + AI Act | All require periodic compliance checks | Unified audit calendar |

**Count per case:**

| Case | Synergistic sub-domains | % of covered sub-domains |
|---|---|---|
| Case 01 (2 regs) | ~15 | ~43% |
| Case 02 (4 regs) | ~18 | ~51% |
| Case 03 (5 regs) | ~20 | ~53% |

**Resolution:** Implement once at the highest NI standard. Document the compliance mapping for each regulation. This is a one-time design decision, not a per-event decision.

---

### 1.3 Type 2: Structural Tension

**Definition:** Two or more regulations permanently differ in scope, frequency, or depth for the same sub-domain. The difference exists regardless of specific events — it is inherent in how the regulations are written.

**Identification criteria:**
- Same sub-domain covered by 2+ regulations
- Requirements differ in scope (what is covered), frequency (how often), or depth (how thoroughly)
- The difference is permanent (not dependent on a specific event)
- Resolvable at design level via unified framework

**Examples from case studies:**

| Sub-Domain | Regulations | What Differs | Resolution |
|---|---|---|---|
| D-07.1 Secure-by-Design | GDPR (NI=2 "appropriate") vs CRA (NI=3 "secure by default") | Intensity: GDPR is vague, CRA is prescriptive | Follow CRA higher bar |
| D-09.1 Security Policies | GDPR + CRA + NIS 2 + AI Act | Scope: each reg requires different policy elements | Unified ISMS with regulation-specific annexes |
| D-09.2 Risk Assessments | GDPR (DPIA) + CRA (risk assessment) + NIS 2 (risk analysis) + DORA (ICT risk) + AI Act (FRIA) | Trigger: different triggers for similar assessments | Unified assessment framework (IPSARA) |
| D-10.1 Continuous Monitoring | CRA + NIS 2 + DORA + AI Act | Depth: different monitoring requirements | Layered monitoring with reg-specific dashboards |
| D-05.3 vs D-10.2 | GDPR (right to erasure) vs DORA/AI Act (immutable logs) | Requirement: erasure contradicts retention | Cryptographic sharding (see §2.4) |

**Count per case:**

| Case | Structural tensions | Notable examples |
|---|---|---|
| Case 01 (2 regs) | ~2 | D-07.1 (GDPR vs CRA intensity), D-09.2 (DPIA vs CRA assessment) |
| Case 02 (4 regs) | ~6 | Above + D-09.1 (4-reg policy scope), D-10.1 (monitoring depth), D-08.1 (awareness scope) |
| Case 03 (5 regs) | ~8 | Above + D-05.3 vs D-10.2 (erasure vs retention), D-06.1 (vendor assessment scope) |

**Resolution:** Unified framework with regulation-specific annexes. Resolve once at ISMS design level. Example: a single risk assessment document that satisfies GDPR DPIA + CRA risk assessment + NIS 2 risk analysis + DORA ICT risk assessment + AI Act FRIA — one process, five regulatory outputs.

---

### 1.4 Type 3: Contextual Tension

**Definition:** Two or more regulations may conflict, but ONLY when the same factual event triggers obligations from both simultaneously. The conflict is not inherent in the regulations — it emerges from the interaction between the company's operational profile and the regulatory trigger conditions.

**Identification criteria:**
- Same sub-domain covered by 2+ regulations
- Requirements have different triggers, deadlines, or formats
- Conflict only materializes when a single factual event satisfies multiple trigger conditions
- NOT resolvable at design level — must be resolved per-event

**Examples from case studies:**

| Sub-Domain | Regulations | What Conflicts | When It Triggers |
|---|---|---|---|
| D-04.3 Regulatory Notification | GDPR (72h) + CRA (24h) + NIS 2 (24h) + DORA (4h) + AI Act (15d) | All have different reporting deadlines for incidents | Single cyber incident involving personal data + product vulnerability + service disruption |

**Count per case:** Contextual Tensions remain at 1 across all cases — only D-04.3 produces contextual tension at scale. This is because incident notification is the only sub-domain where multiple regulations impose different deadlines for the SAME factual event.

| Case | Contextual tensions | Which sub-domain |
|---|---|---|
| Case 01 | 1 | D-04.3 (GDPR 72h vs CRA 24h) |
| Case 02 | 1 | D-04.3 (GDPR 72h vs CRA 24h vs NIS 2 24h vs AI Act 15d) |
| Case 03 | 1 | D-04.3 (GDPR 72h vs CRA 24h vs NIS 2 24h vs DORA 4h vs AI Act 15d) |

**Resolution:** Per-event via compound event analysis (LLM-F). The most common resolution is **Max-SLA Routing** — the shortest deadline (DORA 4h) satisfies all longer deadlines. See §2.4 for full resolution pattern catalog.

**Key insight:** Contextual Tensions are rare (only 1 sub-domain) but CRITICAL when they occur. Structural Tensions are common (6-8 sub-domains) but resolved once at design level. Synergistic overlaps are the majority (50%+) and represent implementation efficiency opportunities.

---

## 2. Compound Event Methodology

### 2.1 Definition

A **compound event** is a single factual incident that simultaneously triggers obligations from two or more regulations. It exists when:

1. **Same factual event:** One real-world incident (not two separate incidents)
2. **Multiple regulatory triggers:** The event satisfies the trigger conditions of 2+ regulatory clauses
3. **Tension created:** The triggered obligations have incompatible deadlines, formats, or requirements

A compound event does NOT exist when:
- Only one regulation is triggered (even if the event is severe)
- Multiple regulations are triggered but their requirements are complementary (no tension)
- Multiple regulations are triggered in different sub-domains with no interaction

### 2.2 Positive Identification Criteria

An event IS a compound event when ALL three conditions are met:

| # | Criterion | Test | Example |
|---|---|---|---|
| 1 | Same factual event | Is this ONE incident, not two? | "Attacker exploits vulnerability AND exfiltrates data" = one incident |
| 2 | Multiple triggers | Does this event satisfy trigger conditions of 2+ regs? | Triggers GDPR Art. 33 (breach) AND CRA Art. 14 (vulnerability) |
| 3 | Tension exists | Are the triggered obligations incompatible? | GDPR requires 72h notification, CRA requires 24h → temporal conflict |

### 2.3 Negative Exclusion Criteria

An event is NOT a compound event when ANY of these apply:

| # | Criterion | Test | Example |
|---|---|---|---|
| 1 | Single regulation | Does only one reg apply? | "Employee emails customer list to wrong recipient" → GDPR only (no exploited vulnerability for CRA) |
| 2 | Complementary | Multiple regs triggered but no tension? | "User requests data erasure" → GDPR Art. 17 + CRA Art. 15, but same right, same timeline → no conflict |
| 3 | Different sub-domains | Multiple regs triggered in non-interacting sub-domains? | "Vendor contract renewal" → NIS 2 supply chain + GDPR processor terms, but different processes, no interaction |

**Why negative examples matter:** They demonstrate the LLM's discrimination ability. An LLM that classifies everything as a compound event is useless. The negative examples show that the LLM can distinguish between events that trigger multiple regs WITH tension and events that trigger multiple regs WITHOUT tension.

### 2.4 Tension Type Taxonomy

When a compound event IS identified, the tension falls into one of 5 types:

| Tension Type | Code | Definition | Example | Typical Severity |
|---|---|---|---|---|
| **Temporal Conflict** | TEMPORAL_CONFLICT | Different reporting deadlines for the same incident | GDPR 72h vs CRA 24h vs DORA 4h | CRITICAL |
| **Requirement Conflict** | REQUIREMENT_CONFLICT | Contradictory requirements that cannot both be satisfied | GDPR right to erasure vs DORA immutable audit logs | CRITICAL |
| **Frequency Mismatch** | FREQUENCY_MISMATCH | Different assessment frequencies for the same activity | GDPR annual DPIA vs CRA per-release risk assessment | MEDIUM |
| **Trigger Mismatch** | TRIGGER_MISMATCH | Different triggers for similar assessment obligations | GDPR DPIA (high-risk processing) vs AI Act FRIA (high-risk AI) vs DORA ICT risk | MEDIUM |
| **Intensity Gap** | INTENSITY_GAP | Different NI for the same sub-domain (one stricter than other) | GDPR "appropriate measures" (NI=2) vs CRA "secure by default" (NI=3) | LOW |

### 2.5 Resolution Pattern Catalog

Each tension type has established resolution patterns:

| Pattern | Applies To | How It Works | Example |
|---|---|---|---|
| **Max-SLA Routing** | TEMPORAL_CONFLICT | Implement the shortest deadline — it satisfies all longer deadlines automatically | DORA 4h initial notification satisfies GDPR 72h, CRA 24h, NIS 2 24h |
| **Cryptographic Sharding** | REQUIREMENT_CONFLICT (erasure vs retention) | Destroy the identity link (satisfies erasure) while retaining anonymized data (satisfies retention) | Customer requests erasure: delete PII fields, retain anonymized audit log with cryptographic hash |
| **Unified Assessment** | TRIGGER_MISMATCH, FREQUENCY_MISMATCH | Single assessment document with multiple regulatory outputs | IPSARA framework: one risk assessment → DPIA (GDPR) + FRIA (AI Act) + ICT risk assessment (DORA) |
| **Higher-Bar Compliance** | INTENSITY_GAP | Implement the strictest requirement (highest NI) — it satisfies all less strict requirements | CRA "secure by default" (NI=3) satisfies GDPR "appropriate measures" (NI=2) |

---

## 3. Compound Event Catalog (Cross-Case)

### 3.1 All Compound Events from Case Studies

| Event | Case | Regulations Triggered | Sub-Domain | Tension Type | Severity | Resolution |
|---|---|---|---|---|---|---|
| Attacker exploits vuln + exfiltrates personal data | 01, 02, 03 | GDPR + CRA | D-04.3 | TEMPORAL_CONFLICT | HIGH/CRITICAL | Max-SLA Routing (24h) |
| Cyberattack + data exfil + service disruption + AI model | 03 | GDPR + CRA + NIS 2 + DORA + AI Act | D-04.3 | TEMPORAL_CONFLICT | CRITICAL | Max-SLA Routing (4h DORA) |
| Cyberattack + data exfil + payment disruption | 03 | GDPR + CRA + NIS 2 + DORA | D-04.3 | TEMPORAL_CONFLICT | CRITICAL | Max-SLA Routing (4h) |
| AI trading malfunction + unauthorized transactions | 03 | GDPR + DORA + AI Act | D-04.3 | TEMPORAL_CONFLICT | HIGH | DORA 4h + GDPR 72h + AI Act 15d |
| Customer erasure request vs immutable audit logs | 03 | GDPR + DORA | D-05.3 vs D-10.2 | REQUIREMENT_CONFLICT | CRITICAL | Cryptographic Sharding |
| New AI credit scoring model launch | 03 | GDPR + CRA + NIS 2 + DORA + AI Act | D-09.2 | TRIGGER_MISMATCH | MEDIUM | Unified Assessment (IPSARA) |
| Product design for new feature | 01, 02, 03 | GDPR + CRA (+ AI Act) | D-07.1 | INTENSITY_GAP | LOW | Higher-Bar (CRA NI=3) |
| Product launch with high-risk data processing | 01, 02 | GDPR + CRA | D-09.2 | FREQUENCY_MISMATCH | MEDIUM | Unified assessment |
| Ransomware encrypts banking + customer data | 03 | GDPR + NIS 2 + DORA | D-04.2 | None (complementary) | — | Unified BCP/DRP |
| Supply chain vendor breach | 02, 03 | GDPR + NIS 2 (+ DORA) | D-06.1 | Structural | — | Unified vendor assessment |

### 3.2 All Negative Examples from Case Studies

| Scenario | Case | Why NOT Compound | Discrimination Rule |
|---|---|---|---|
| Employee emails customer list to wrong recipient | 01, 02, 03 | GDPR only — no exploited product vulnerability for CRA | CRA trigger requires exploited vuln, not just data exposure |
| XSS vulnerability with no data access | 01, 02 | CRA only — no personal data involved | GDPR trigger requires personal data breach |
| Customer changes address | 03 | GDPR only — routine processing, no security incident | No other reg trigger for routine data update |
| AI model accuracy drift | 03 | AI Act only — no personal data breach, no security incident | No GDPR/DORA/NIS 2 trigger for model degradation |
| Internal IT system outage | 03 | DORA only — no personal data involved | No GDPR trigger without personal data |
| Vendor contract renewal | 03 | NIS 2 only — no data processing change | No GDPR trigger for contract management |
| User requests data erasure | 01 | Both GDPR + CRA triggered but same right, same timeline | Multiple regs but NO tension = not compound |

### 3.3 Compound Event Scaling Formula

| Regulations (N) | Overlap Pairs C(N,2) | Compound Events (est.) | Negative Examples (est.) |
|---|---|---|---|
| 2 | 1 | 3 | 3 |
| 3 | 3 | 5 | 3-4 |
| 4 | 6 | 6-8 | 4 |
| 5 | 10 | 10-12 | 4 |

**Key insight:** Compound events grow approximately linearly with regulation count, NOT combinatorially. This is because most regulatory overlaps are Synergistic (no tension) or Structural (permanent, not event-driven). Only Contextual Tensions produce compound events, and Contextual Tensions are rare (typically only D-04.3).

---

## 4. Strategic Tensions Catalog (Cross-Case)

All strategic tensions identified across the 3 case studies, with resolution status:

| Tension ID | Case | Sub-Domain | Regulations | Conflict Type | Severity | Resolution |
|---|---|---|---|---|---|---|
| T-H-001 | 01, 02, 03 | D-04.3 | GDPR 72h vs CRA 24h | TEMPORAL_CONFLICT | CRITICAL (03) / HIGH (01, 02) | Max-SLA Routing — 24h workflow |
| T-H-002 | 03 | D-05.3 vs D-10.2 | GDPR erasure vs DORA immutable logs | REQUIREMENT_CONFLICT | CRITICAL | Cryptographic Sharding |
| T-H-003 | 02, 03 | D-04.3 | NIS 2 24h vs DORA 4h | TEMPORAL_CONFLICT | CRITICAL | Max-SLA Routing — DORA 4h |
| T-M-001 | 01, 02, 03 | D-09.2 | GDPR DPIA vs CRA risk assessment | FREQUENCY_MISMATCH | MEDIUM | Unified assessment |
| T-M-002 | 02, 03 | D-09.2 | GDPR DPIA vs AI Act FRIA | TRIGGER_MISMATCH | MEDIUM | Unified Assessment (IPSARA) |
| T-M-003 | 03 | D-09.2 | GDPR + CRA + NIS 2 + DORA + AI Act (5 assessments) | TRIGGER_MISMATCH | MEDIUM | IPSARA Framework |
| T-L-001 | 01, 02, 03 | D-07.1 | GDPR NI=2 vs CRA NI=3 | INTENSITY_GAP | LOW | Higher-Bar (CRA) |
| T-L-002 | 02, 03 | D-04.3 | NIS 2 24h vs DORA 24h | Alignment | LOW | Unified 24h workflow |

**Severity escalation pattern:** Tensions that are HIGH in Case 01 (2 regs) become CRITICAL in Case 03 (5 regs) because more regulations pile onto the same factual event. The D-04.3 notification tension is HIGH with 2 regs (72h vs 24h) but CRITICAL with 5 regs (72h vs 24h vs 24h vs 4h vs 15d) because the operational complexity of satisfying 5 different deadlines simultaneously is far greater.

---

## 5. Cross-Case Scaling Analysis

### 5.1 How Synthesis Complexity Grows

| Metric | Formula / Driver | Case 01 (2 regs) | Case 02 (4 regs) | Case 03 (5 regs) | Growth Pattern |
|---|---|---|---|---|---|
| Overlap pairs | C(N, 2) | 1 | 6 | 10 | Quadratic |
| Avg regs/sub-domain | Covered sub-domains / total clauses | 1.4 | 3.2 | 3.7 | Linear |
| Synergistic sub-domains | Count of compatible overlaps | ~15 | ~18 | ~20 | Sub-linear |
| Structural tensions | Count of permanent differences | ~2 | ~6 | ~8 | Linear |
| Contextual tensions | Count of event-driven conflicts | 1 | 1 | 1 | Constant |
| Compound events (positive) | Event scenarios identified | 3 | 6 | 10 | Linear |
| Negative examples | Near-miss scenarios | 3 | 4 | 4 | Sub-linear |
| Strategic tensions | Tensions formalized | 1 | 3 | 4 | Linear |
| CRITICAL tensions | Count of CRITICAL severity | 0 | 1 | 2 | Linear |
| LLM reasoning invocations | 4 steps × 1 pass | 4 | 4 | 4 | Constant |
| Phase 2 artifacts | Artifacts passed forward | 5 | 7 | 9 | Linear |

### 5.2 Key Scaling Insights

**1. Overlap pairs grow quadratically, but compound events grow linearly.** C(5,2) = 10 overlap pairs, but only ~10 compound events (not 45). This is because most overlaps are Synergistic (no tension) or Structural (permanent, not event-driven). The methodology's 3-type classification prevents over-reporting of conflicts.

**2. Contextual Tensions remain constant at 1.** Only D-04.3 (incident notification) produces contextual tension. This is a structural property of EU regulations: they are designed to be compatible, and reporting deadline differences are the main source of event-driven conflict.

**3. Severity escalates with regulation count, even when tension count does not.** The D-04.3 tension is HIGH with 2 regs but CRITICAL with 5 regs. More regulations means more deadlines to satisfy simultaneously, which increases operational complexity even though the tension type is the same.

**4. Synergistic overlaps are the majority and represent the biggest efficiency opportunity.** With 5 regulations, ~53% of covered sub-domains are Synergistic. Each Synergistic overlap is an implementation efficiency gain — one control satisfies multiple regulations.

**5. The methodology scales gracefully.** The LLM reasoning steps remain at 4 regardless of regulation count (single-pass synthesis). The deterministic steps (coverage matrix, dashboard, overlap calculation) scale computationally but do not require additional reasoning. The main scaling challenge is KB size — more regulations means more regulation text + implementing acts in the knowledge base.

---

## Summary: How to Use This File

| If you need to... | Read this section |
|---|---|
| Classify a regulatory overlap | §1 — Conflict Classification Framework |
| Identify whether an event is compound | §2.2 (positive criteria) + §2.3 (negative criteria) |
| Classify a tension type | §2.4 — Tension Type Taxonomy |
| Find the resolution for a tension | §2.5 — Resolution Pattern Catalog |
| See all compound events from case studies | §3.1 — Positive examples |
| See why certain events are NOT compound | §3.2 — Negative examples |
| See all strategic tensions across cases | §4 — Strategic Tensions Catalog |
| Understand how complexity scales with regs | §5 — Cross-Case Scaling Analysis |

---

**See also:**
- [`phase1c_consolidation.md`](phase1c_consolidation.md) — Flow diagrams + LLM spec tables (companion)
- [`phase1b_regulatory_mapping.md`](phase1b_regulatory_mapping.md) — Phase 1B detail (predecessor)
- [`phase1b_nuances_and_reasoning.md`](phase1b_nuances_and_reasoning.md) — Phase 1B reference (Doc 05 vs Doc 07 analysis)
- [`../phase1_contextual_definition.md`](../phase1_contextual_definition.md) — Phase 1 overview (parent)
- [`../../../TEMPLATES/07_Structured_Compliance_Matrix.md`](../../../TEMPLATES/07_Structured_Compliance_Matrix.md) — Doc 07 template
- [`../../PROMPTS/P1C-LLM-01-OVERLAP-CLASSIFICATION.md`](../../PROMPTS/P1C-LLM-01-OVERLAP-CLASSIFICATION.md) — Canonical prompt (v1.2)
- [`../../PROMPTS/P1C-LLM-02-COMPOUND-EVENT.md`](../../PROMPTS/P1C-LLM-02-COMPOUND-EVENT.md) — Canonical prompt (v1.2)
- [`../../PROMPTS/P1C-LLM-03-STRATEGIC-SYNTHESIS.md`](../../PROMPTS/P1C-LLM-03-STRATEGIC-SYNTHESIS.md) — Canonical prompt (v1.2)

---

## Legacy ID Cross-walk (v1.2, 2026-07-13)

| Legacy | Canonical | Invocation | Stage | Function |
|---|---|---|---|---|
| LLM-E | `P1C-LLM-01-OVERLAP-CLASSIFICATION` | per_domain_lane | Map (per-domain) | Activates Regulatory Baseline CONDITIONAL entries per domain. **NO re-classification** of frozen Regulatory Baseline relationships. |
| LLM-F | `P1C-LLM-02-COMPOUND-EVENT` | global_reduce | Reduce (runs 2nd) | Identifies cross-domain compound events. **NO resolution design** — resolution goes to Phase 2B. |
| LLM-G | `P1C-LLM-03-STRATEGIC-SYNTHESIS` | global_reduce | Reduce (runs 1st) | Cross-lane strategic implications. Consumes Doc 07b (deterministic) as constraint. |
| LLM-H | (REMOVED) | — | — | Gap aggregation + remediation moved out of Phase 1 scope (per `PHASE1_STRATEGY.md`). |

## Authority Caveat (v1.2)

The Synergistic / Structural Tension / Contextual Tension taxonomy in this reference file is the **classification target** for `P1C-LLM-01-OVERLAP-CLASSIFICATION`. The actual classification is **read-only from the Regulatory Baseline** (`SubDomains/D-XX.Y.md §1 CRDA`); the LLM only **activates** Regulatory Baseline CONDITIONAL entries based on company facts. The LLM does NOT re-classify or invent new relationships.

The CRDA → CRDA-deep authority chain is:

1. `REGULATORY_BASELINE.md` — architectural contract (frozen)
2. `PREPROCESSING/SubDomains/D-XX.Y.md` — Phase 1 consumption package
3. `PREPROCESSING/CrossRegulation/DeepAnalysis/D-XX.Y.md` — OJ-verified evidence
4. `PREPROCESSING/CrossRegulation/DomainAnalysis/D-XX.Y.md` — lighter overview
