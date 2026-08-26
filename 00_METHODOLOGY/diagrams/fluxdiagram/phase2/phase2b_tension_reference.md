---
document_id: AEGIS-DIAG-P2B-REFERENCE
title: "Phase 2B — Tension Catalog & Resolution Patterns (Reference)"
phase: 2B
version: 1.0
created: 2026-06-16
status: CREATED
parent_diagram: phase2b_strategic_tensions.md
source: Cross-case analysis (Doc 09 from all 3 cases)
---

# Phase 2B — Tension Catalog & Resolution Patterns (Reference)

**Version:** 1.0 — 2026-06-16
**Companion to:** [`phase2b_strategic_tensions.md`](phase2b_strategic_tensions.md) (flow diagrams)
**Sources:** Doc 09 from Case 01, Case 02, Case 03

---

## Overview

This file is the **reference companion** to the Phase 2B detailed flow diagrams. It contains:

1. **7-Type Tension Catalog** — full taxonomy with detection criteria and cross-case examples
2. **7 Resolution Patterns** — reusable design patterns mapped to tension types
3. **Compound Event Methodology** — positive and negative examples
4. **Tension Scaling Analysis** — how tension count scales (non-monotonic) with regulation count

---

## 1. 7-Type Tension Catalog

### TT-01: Temporal Conflict

| Field | Value |
|-------|-------|
| **Definition** | Two or more regulations require action within incompatible timeframes for the same event |
| **Detection** | Compare deadlines in same sub-domain; flag if delta > 0 |
| **Severity escalation** | CRITICAL when deadlines span multiple orders of magnitude (4h vs 15d) |
| **Typical sub-domains** | D-04.3 (incident notification) |
| **Example** | GDPR 72h (Art. 33) vs CRA 24h (Art. 14(1)) vs NIS 2 24h (Art. 23(4)) vs DORA 4h (RTS Art. 18) vs AI Act 15d (Art. 73(1)(a)) |
| **Resolution** | Max-SLA Routing (shortest deadline) |

### TT-02: Requirement Conflict

| Field | Value |
|-------|-------|
| **Definition** | One regulation requires X, another prohibits X for the same data/asset |
| **Detection** | Compare obligation text; flag if requirements are semantically incompatible |
| **Severity** | CRITICAL (direct contradiction) |
| **Typical sub-domains** | D-05.3 (erasure) vs D-10.2 (audit logs) |
| **Example** | GDPR Art. 17 (right to erasure) vs DORA Art. 10 (immutable audit logs) |
| **Resolution** | Cryptographic Sharding (separate PII from log content) |

### TT-03: Resource Conflict

| Field | Value |
|-------|-------|
| **Definition** | Same resource (budget, personnel, infrastructure) is demanded by multiple obligations with insufficient capacity |
| **Detection** | Compare resource implications across obligations |
| **Severity** | MEDIUM–HIGH (depends on resource scarcity) |
| **Typical sub-domains** | D-09.1 (documentation), D-04.1 (incident response capability) |
| **Example** | GDPR Art. 30 + CRA Art. 24 + NIS 2 Art. 21 + DORA Art. 9 all require documentation — duplicative if not consolidated |
| **Resolution** | Unified ISMS with regulation-specific annexes |

### TT-04: Implementation Conflict

| Field | Value |
|-------|-------|
| **Definition** | Two regulations require technically incompatible implementation approaches |
| **Detection** | Compare technical standards/protocols required |
| **Severity** | HIGH |
| **Typical sub-domains** | D-01.1, D-01.2 (encryption) |
| **Example** | TLS 1.2 (some legacy requirement) vs TLS 1.3 (current best practice) |
| **Resolution** | Higher-Bar Compliance (implement strictest) |

### TT-05: Intensity Gap

| Field | Value |
|-------|-------|
| **Definition** | Same sub-domain covered by 2+ regulations with different Normative Intensity (NI delta ≥ 0.5) |
| **Detection** | Compute NI delta; flag if ≥ 0.5 |
| **Severity** | LOW (easily resolved by following higher bar) |
| **Typical sub-domains** | D-07.1 (secure-by-design) |
| **Example** | GDPR Art. 25 "appropriate measures" (NI=2) vs CRA Art. 13(2) "secure by default" (NI=3) |
| **Resolution** | Higher-Bar Compliance (CRA NI=3 satisfies GDPR NI=2) |

### TT-06: Frequency Mismatch

| Field | Value |
|-------|-------|
| **Definition** | Same activity assessed/audited at different frequencies by different regulations |
| **Detection** | Compare obligationType (CONTINUOUS, PERIODIC, TRIGGERED, ONE_TIME) |
| **Severity** | MEDIUM |
| **Typical sub-domains** | D-09.2 (risk assessment), D-10.3 (compliance testing) |
| **Example** | GDPR DPIA per-processing vs CRA risk assessment per-release vs DORA ICT risk annual |
| **Resolution** | Unified Assessment (IPSARA framework) |

### TT-07: Trigger Mismatch

| Field | Value |
|-------|-------|
| **Definition** | Similar obligations triggered by different conditions in different regulations |
| **Detection** | Compare trigger conditions; flag if obligations are similar but triggers differ |
| **Severity** | MEDIUM |
| **Typical sub-domains** | D-09.2 (risk assessment) |
| **Example** | GDPR DPIA (high-risk processing) vs AI Act FRIA (high-risk AI) vs DORA ICT risk (financial entity) |
| **Resolution** | Unified Assessment (single process, multiple outputs) |

---

## 2. 7 Resolution Patterns

### Max-SLA Routing

| Field | Value |
|-------|-------|
| **Applies to** | TT-01 (Temporal Conflict) |
| **Logic** | Implement the shortest deadline; longer deadlines are automatically satisfied |
| **Example** | DORA 4h initial notification satisfies GDPR 72h, CRA 24h, NIS 2 24h, AI Act 15d |
| **When to use** | When deadlines are the ONLY difference; requirements are otherwise compatible |
| **Cross-case** | All 3 cases (T-H-001 / T-001 / T-H-001) |

### Cryptographic Sharding

| Field | Value |
|-------|-------|
| **Applies to** | TT-02 (Requirement Conflict — erasure vs retention) |
| **Logic** | Destroy the identity link (satisfies erasure) while retaining anonymised data (satisfies retention) |
| **Example** | Customer requests erasure: delete PII fields, retain anonymised audit log with cryptographic hash |
| **When to use** | When both requirements are absolute and non-negotiable |
| **Cross-case** | Case 02 (T-002) + Case 03 (T-H-002) |

### Unified ISMS with Annexes

| Field | Value |
|-------|-------|
| **Applies to** | TT-03 (Resource Conflict — documentation) |
| **Logic** | Single ISMS document with regulation-specific annexes; core content satisfies all regs |
| **Example** | One ISMS with GDPR Annex, CRA Annex, NIS 2 Annex, DORA Annex, AI Act Annex |
| **When to use** | When multiple regs require overlapping documentation (policies, procedures, records) |
| **Cross-case** | Case 02 (T-004) + Case 03 |

### Higher-Bar Compliance

| Field | Value |
|-------|-------|
| **Applies to** | TT-04, TT-05 (Implementation Conflict, Intensity Gap) |
| **Logic** | Implement the strictest standard; it satisfies all less strict requirements |
| **Example** | CRA "secure by default" (NI=3) satisfies GDPR "appropriate measures" (NI=2) |
| **When to use** | When standards differ in depth/strength but not in scope |
| **Cross-case** | Case 01 (T-M-002), Case 03 (T-L-001) |

### Unified Assessment (IPSARA)

| Field | Value |
|-------|-------|
| **Applies to** | TT-06, TT-07 (Frequency Mismatch, Trigger Mismatch) |
| **Logic** | Single assessment process with multiple regulatory outputs |
| **Example** | IPSARA (Integrated Privacy, Security, AI, Risk Assessment): one process produces DPIA (GDPR) + FRIA (AI Act) + ICT risk (DORA) + risk assessment (CRA) |
| **When to use** | When similar assessments are required by multiple regs with different triggers/frequencies |
| **Cross-case** | All 3 cases (T-M-001 / T-003) |

### Integrated SOC Platform

| Field | Value |
|-------|-------|
| **Applies to** | TT-03 (Resource Conflict — monitoring) |
| **Logic** | Single SOC platform with multi-regulation dashboards |
| **Example** | One SIEM feeds GDPR breach detection, CRA vulnerability monitoring, NIS 2 incident detection, DORA ICT risk monitoring |
| **When to use** | When multiple regs require security monitoring capability |
| **Cross-case** | Case 02 (T-005) |

### Unified Supplier Questionnaire

| Field | Value |
|-------|-------|
| **Applies to** | TT-03 (Resource Conflict — supply chain) |
| **Logic** | Single supplier assessment with per-regulation outputs |
| **Example** | One questionnaire covers NIS 2 supplier security, GDPR processor terms, DORA ICT third-party requirements |
| **When to use** | When multiple regs require supplier/vendor assessments |
| **Cross-case** | Case 02 (T-006) |

---

## 3. Compound Event Methodology

### Positive Identification

A **compound event** is a single factual incident that triggers obligations from 2+ regulations simultaneously. All three conditions must hold:

| # | Criterion | Test |
|---|-----------|------|
| 1 | Same factual event | ONE incident, not two |
| 2 | Multiple triggers | Event satisfies 2+ regulatory trigger conditions |
| 3 | Tension exists | Triggered obligations are incompatible (deadline, format, requirement) |

### Negative Exclusion

An event is NOT compound when ANY applies:

| # | Criterion | Example |
|---|-----------|---------|
| 1 | Only one regulation triggered | "Employee emails customer list to wrong recipient" → GDPR only (no exploited vuln for CRA) |
| 2 | Multiple regs but no tension | "User requests data erasure" → GDPR + CRA but same right, same timeline |
| 3 | Different sub-domains | "Vendor contract renewal" → NIS 2 + GDPR but different processes |

### Cross-Case Compound Events

| Event | Case | Regulations | Tension Type | Resolution |
|-------|------|-------------|--------------|------------|
| Vuln exploited + data exfiltrated | 01, 02, 03 | GDPR + CRA | TT-01 (72h vs 24h) | Max-SLA (24h) |
| Cyberattack + data exfil + service disruption + AI | 03 | GDPR + CRA + NIS 2 + DORA + AI Act | TT-01 (4h deadline) | Max-SLA (4h DORA) |
| Customer erasure vs immutable logs | 03 | GDPR + DORA | TT-02 | Cryptographic Sharding |
| New AI credit scoring model launch | 03 | GDPR + CRA + NIS 2 + DORA + AI Act | TT-07 | Unified Assessment |
| Supplier breach notification chain | 02, 03 | NIS 2 + DORA + GDPR | TT-01 (24h vs 72h) | Max-SLA (NIS 2 24h) |
| Vulnerability in open-source dependency | 01, 02 | CRA + NIS 2 | TT-06 (per-release vs periodic) | Unified Assessment (per-release) |
| Employee departs with customer data | 01, 02, 03 | GDPR + CRA | TT-02 (erasure vs evidence) | Cryptographic Sharding (revoke access) |
| AI model retrained on personal data | 02, 03 | GDPR + AI Act | TT-07 (DPIA vs FRIA trigger) | Unified Assessment (DPIA + FRIA) |
| Cross-border data transfer during incident | 02, 03 | GDPR + NIS 2 + DORA | TT-01 (notification vs transfer assessment) | Max-SLA + SCC update |
| Third-party processor breach | 01, 02, 03 | GDPR + NIS 2 + DORA | TT-03 (parallel supplier assessments) | Unified Supplier Questionnaire |

---

## 4. Tension Scaling Analysis

| Metric | Formula | Case 01 (2 regs) | Case 02 (4 regs) | Case 03 (5 regs) | Growth Pattern |
|--------|---------|-------------------|-------------------|-------------------|----------------|
| Overlap pairs | C(N, 2) | 1 | 6 | 10 | Quadratic |
| Tensions detected | Overlap + semantics | 4 | 8 | 4 | Sub-linear (plateaus) |
| Contextual tensions | Event-driven | 1 | 2 | 1 | Constant (~1-2) |
| Structural tensions | Permanent | 2 | 6 | 3 | Sub-linear |
| Compound events | Identified scenarios | 3 | 8+ | 10+ | Linear |
| Resolution patterns used | Distinct patterns | 3 | 6 | 5 | Logarithmic (plateaus at 7) |
| Tensions per obligation | Tensions / obligations | 0.17 | 0.21 | 0.11 | Constant (~0.1-0.2) |
| Novel resolutions (non-pattern) | Count | 0 | 0 | 1 | Rare (only MAX tier) |

**Non-monotonic insight:** Case 03 (5 regs) has FEWER tensions than Case 02 (4 regs) because:
- DORA's lex specialis rule transforms some Contextual tensions (erasure vs logs) into Structural ones
- More regulations = more opportunities for Higher-Bar Compliance (which RESOLVES tensions at design level)
- The combinatorial explosion of overlap pairs (C(5,2)=10) is absorbed by Synergistic resolutions (no tension), not by Contextual ones

---

## 5. ID Format Inconsistency

| Case | Format | Example |
|------|--------|---------|
| Case 01 | `TENSION-H/M/L-NNN` | `TENSION-H-001` |
| Case 02 | Flat `T-NNN` | `T-001` |
| Case 03 | `TENSION-H/M/L-NNN` | `TENSION-H-001` |

**Not resolved.** Both formats appear in the documents. The severity prefix (H/M/L) is more informative; the flat format is more compact.

---

## 6. Strategic Tensions Catalog (Cross-Case)

This catalog assigns stable cross-case IDs (T-H-NNN, T-M-NNN, T-L-NNN) to the recurring tensions observed in Doc 09 across all three cases. IDs are decoupled from the per-case numbering (Case 02 flat `T-NNN`, Cases 01/03 `TENSION-H/M/L-NNN`) so they can be referenced from methodology-level artefacts without ambiguity.

| Tension ID | Name | Type | Severity | Cases | Resolution |
|------------|------|------|----------|-------|------------|
| T-H-001 | Notification deadline conflict | TT-01 | HIGH | 01, 02, 03 | Max-SLA Routing |
| T-H-002 | Erasure vs retention | TT-02 | HIGH | 02, 03 | Cryptographic Sharding |
| T-M-001 | Documentation overlap | TT-03 | MEDIUM | 01, 02, 03 | Unified ISMS |
| T-M-002 | Assessment frequency | TT-06 | MEDIUM | 01, 02, 03 | Unified Assessment |
| T-M-003 | Assessment trigger | TT-07 | MEDIUM | 02, 03 | Unified Assessment |
| T-L-001 | Secure design intensity | TT-05 | LOW | 01, 03 | Higher-Bar Compliance |
| T-L-002 | Encryption standard | TT-04 | LOW | 02 | Higher-Bar Compliance |

### T-H-001 — Notification deadline conflict

GDPR (72h), CRA (24h), NIS 2 (24h), DORA (4h) and AI Act (15d) impose different notification windows for what is frequently the same security incident. Max-SLA Routing resolves this by implementing the shortest applicable deadline, which automatically satisfies every longer deadline as a by-product. The tension is universal across cases because every active regulation in the 5-regulation set carries an incident-notification obligation, and the deadline spread (4h to 15d) is large enough to be operationally non-trivial.

### T-H-002 — Erasure vs retention

GDPR Art. 17 grants data subjects a right to erasure, while DORA Art. 10 and CRA Art. 24 require immutable audit logs for forensic and compliance purposes — a direct semantic contradiction on the same data. Cryptographic Sharding resolves it by separating PII from log content: when a customer exercises erasure rights, the identity link is destroyed (satisfying GDPR) while anonymised records are retained (satisfying DORA/CRA). The tension is structural and only materialises in MEDIUM and MAX tiers where immutable-log obligations are in force.

### T-M-001 — Documentation overlap

GDPR Art. 30, CRA Art. 24, NIS 2 Art. 21, DORA Art. 9 and AI Act Art. 17 each require overlapping documentation (policies, procedures, records of processing). A Unified ISMS with regulation-specific annexes consolidates this into a single source of truth with tailored views per regulation, eliminating duplication while preserving regulatory traceability. Proportionality governs annex depth: Case 01 uses lightweight annexes, while Case 03 requires the full DORA-compliant policy stack.

### T-M-002 — Assessment frequency

GDPR DPIAs (per-processing), CRA risk assessments (per-release), DORA ICT risk assessments (annual) and NIS 2 risk reviews (periodic) assess the same underlying risk surface at different cadences. The Unified Assessment pattern (IPSARA) runs one assessment process that emits multiple regulatory outputs, ensuring freshness without duplicated effort; the operational cadence is set by the shortest interval. This tension is present in every case but absorbs cleanly into a single process, which is why it ranks MEDIUM rather than HIGH.

### T-M-003 — Assessment trigger

GDPR DPIAs are triggered by "high-risk processing", AI Act FRIAs by "high-risk AI systems", and DORA ICT risk assessments by "major ICT-related changes" — semantically overlapping but formally distinct conditions that risk either duplicate or missed assessments. A single Unified Assessment with a consolidated trigger condition (any of the above) ensures every qualifying change is assessed once, with outputs routed to the relevant regulations. The tension is most visible in cases deploying AI or undergoing major architectural changes, hence its restriction to Cases 02 and 03.

### T-L-001 — Secure design intensity

GDPR Art. 25 mandates "appropriate technical and organisational measures" (NI=2), while CRA Art. 13(2) demands "secure by default" (NI=3) — a higher bar covering the same design ground. Higher-Bar Compliance resolves this trivially: implementing CRA's stricter NI=3 obligation automatically satisfies GDPR's NI=2 expectation with no additional design work. The tension is marked LOW because the resolution is mechanical and imposes minimal marginal cost beyond already-planned CRA compliance.

### T-L-002 — Encryption standard

In Case 02, NIS 2 references state-of-the-art encryption (TLS 1.2 acceptable) while DORA's RTS mandates stricter key management and TLS 1.3 for critical functions. Higher-Bar Compliance resolves this by adopting DORA's stricter standards enterprise-wide, which subsumes NIS 2's baseline as a subset. Marked LOW because the cost is bounded, the stricter standard is already industry best practice, and the tension does not propagate to other sub-domains.

---

## Summary: How to Use This File

| If you need to... | Read this section |
|---|---|
| Classify a tension type | §1 — 7-Type Tension Catalog |
| Find a resolution for a tension | §2 — 7 Resolution Patterns |
| Identify compound events | §3 — Compound Event Methodology |
| Understand non-monotonic scaling | §4 — Tension Scaling Analysis |
| Resolve ID format ambiguity | §5 — ID Format Inconsistency |

---

**See also:**
- [`phase2b_strategic_tensions.md`](phase2b_strategic_tensions.md) — Flow diagrams (companion)
- [`../phase2_elaboration_secure_design.md`](../phase2_elaboration_secure_design.md) — Phase 2 overview (parent)
- [`phase2a_obligation_derivation.md`](phase2a_obligation_derivation.md) — Phase 2A (predecessor)
- [`phase2c_goals_and_rules.md`](phase2c_goals_and_rules.md) — Phase 2C (successor)
- [`../../../TEMPLATES/09_Strategic_Tensions_Report.md`](../../../TEMPLATES/09_Strategic_Tensions_Report.md) — Doc 09 template
