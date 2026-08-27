---
title: "AEGIS Implementation Posture Model (CSF 2.0 / PF 1.0 Strict)"
version: "2.0"
date: "2026-08-27"
status: "APPROVED"
supersedes: "MATURITY_MODEL_CSF_STRICT.md v1.0"
---

# AEGIS Implementation Posture Model (CSF 2.0 / PF 1.0 Strict)

> **Core Principle:** Regulatory compliance and technical security governance in AEGIS require observable evidence of operational controls rather than abstract numerical "maturity" scores. This document defines the strict 3-state **Implementation Posture** framework replacing legacy 0-4 maturity scales and T1-T4 Tiers across all AEGIS documentation.

---

## §1 Overview & Motivation

NIST CSF 2.0 Tiers (Tier 1 Partial to Tier 4 Adaptive) describe enterprise-wide risk management processes, not control-level compliance maturity. Numerical scoring models (0-4) introduce subjective ambiguity and false precision in regulatory audits.

AEGIS establishes **Implementation Posture** as a deterministic, evidence-backed classification per control and per security/privacy objective.

---

## §2 The 3 Implementation States

Every control, rule, or objective in the AEGIS corpus MUST be assigned exactly one of the following three implementation states:

| Implementation State | Definition | Required Attributes |
|----------------------|------------|---------------------|
| `IMPLEMENTED` | The control or objective is fully operational in production. | **Evidence Pointer** mandatory (e.g., `[EVID-DOC-01: Identity baseline standard operational]`). |
| `PARTIAL` | The control or objective is partially operational or in active deployment. | **"What's Missing" Note** mandatory explaining specific gaps and remaining requirements. |
| `NOT IMPLEMENTED` | The control or objective is planned or required but not currently operational. | **"What's Missing" Note** mandatory detailing required initial deployment steps. |

### Special Category: Non-Applicable / Deliverables
- **Statutory Obligations / Product-Security Deliverables (SSDF):** Marked as `N/A — product-security deliverable (SSDF <ID>)` or `N/A — statutory obligation`.

---

## §3 Evidence & Gap Requirements

1. **Rule of Evidence:** An `IMPLEMENTED` status without an explicit, verifiable evidence pointer (document reference, automated check result, architectural node link) is invalid and fails audit gate checks.
2. **Rule of Deficit:** Any control marked `PARTIAL` or `NOT IMPLEMENTED` MUST include an explicit description of remaining work ("What's missing") anchored to the control's verification criteria.

---

## §4 Deterministic Legacy Backfill Rules

To migrate legacy AEGIS documents from 0-4 numerical scoring to Implementation Posture without loss of analytical context, the following deterministic mapping MUST be applied:

| Legacy Score (cur / tgt) | Target Implementation Posture | Backfill Action & Description |
|--------------------------|--------------------------------|-------------------------------|
| `cur 3/4 → tgt 3/4` (or Target Met) | `IMPLEMENTED` | Assign `IMPLEMENTED` + populate evidence pointer derived from card verification criteria / architectural node. |
| `cur 1/4 → tgt 3/4` (or `cur 2/4`) | `PARTIAL` | Assign `PARTIAL` + populate "What's missing" note derived from verification criteria delta and target profile requirements. |
| `cur 0/4` | `NOT IMPLEMENTED` | Assign `NOT IMPLEMENTED` + populate "What's missing" note describing full implementation requirements. |
| `N/A` (SSDF / Statutory) | `N/A — product-security deliverable` | Retain explicit SSDF deliverable or statutory obligation reference. |

---

## §5 Qualitative Posture per NIST Function

At the NIST CSF Function level (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER), implementation posture is expressed as a **Qualitative Implementation Context Narrative**, summarizing:
1. Operational strengths in production controls.
2. Active remediation efforts for `PARTIAL` controls.
3. Roadmap priorities for `NOT IMPLEMENTED` controls.

*Numerical averages, maturity heatmaps, and Tier designations (T1-T4) are prohibited at Function level.*

---

## §9 Declassification of Legacy Vocabulary

The following terms and concepts are formally **superseded and prohibited** in AEGIS Markdown documentation:

- ❌ `Maturity Score`, `Maturity Level`, `Current Maturity`, `Target Maturity`
- ❌ `Tier 1 (Partial)`, `Tier 2 (Risk Informed)`, `Tier 3 (Repeatable)`, `Tier 4 (Adaptive)`
- ❌ Numerical maturity scales (`0/4`, `1/4`, `2/4`, `3/4`, `4/4`)
- ❌ Heatmap calculations based on numerical maturity averages

All references MUST use **Implementation Posture**, **Implementation Status**, **Qualitative Context**, or **Evidence Pointers**.
