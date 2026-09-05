---
document_id: AEGIS-METH-RC-RUBRIC-AMENDMENTS-A1-A8
title: Amendments A1–A8 for REALIZATION_CLASS_RUBRIC v1.0 (Adjudicated)
phase: Cross-phase
version: 0.1
created: 2026-09-05
updated: 2026-09-05
author: Validator
status: ACTIVE
---

# Amendments A1–A8 — REALIZATION_CLASS_RUBRIC v1.0

> Source: `REALIZATION_CLASS_RUBRIC_VALIDATOR_REPORT_v0.md` (verdict `APPROVED_WITH_AMENDMENTS`), renumbered and adjudicated by the Orchestrator, 2026-09-05. A1–A3 and A6 incorporate the Orchestrator's adjudications verbatim. All wording below is paste-ready for `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` at its next revision (proposed `version: 1.1`). Line references are to rubric v1.0.

---

## A1 — Constitutive-step test for the TECHNOLOGY disqualifier (ACCEPTED as adjudicated)

**Targets:** §2 class table, TECHNOLOGY row, *Disqualifier* cell (rubric L31: "Sustaining it requires recurring human triage, approval, notification or escalation decisions."); §3 Tie-break guidance, first bullet (rubric L67: "`TECHNOLOGY` vs `PROCESS`: if automation does the work…").

**Replacement — §2 Disqualifier cell:**

> Sustaining it requires recurring human triage, approval, notification or escalation decisions that are **constitutive** (§3 — their outcome changes what the control accepts or permits). Periodic re-verification and exception-path corrections do not disqualify.

**Replacement — §3 first tie-break bullet:**

> - `TECHNOLOGY` vs `PROCESS` — apply the **constitutive-step test** first. A recurring step is **constitutive** (Q1 = NO) only if its outcome changes what the control accepts or permits: an exception approval, a risk acceptance, or a containment / transfer authorisation. Operational test: the step appears in the card's **Verification Criteria**, not only in the Description's exception clause. A recurring step that only re-checks built state — periodic review, sign-off on findings, reconciliation sampling — is *periodic re-verification* and keeps Q1 = YES. Then: if the automated path alone satisfies all verification criteria → `TECHNOLOGY`; if constitutive human-coordinated steps remain (SLA clocks, notifications, approvals) → `PROCESS`.

*Note:* this makes rubric §8 Borderline 1 (`CR-D-02.2-001`) mechanically reproducible: the exception approval appears in that card's verification criteria; in `CR-D-03.2-001` it appears only in the Description.

**Tag: `APPLY-NOW`** — rubric-only edit; removes the main Q1 ambiguity before any rater classifies a single rule.

---

## A2 — Structural indicators for PROCESS vs CAPABILITY + CR-D-08.1/08.2 note (ACCEPTED as adjudicated)

**Target:** §3 Tie-break guidance, second bullet (rubric L68: "`PROCESS` vs `CAPABILITY`: ask what must be sustained between trigger events…").

**Replacement:**

> - `PROCESS` vs `CAPABILITY`: apply the **structural indicators**, then confirm with the between-events question. *CAPABILITY indicators*: a named owner of the standing ability; maintenance of workforce competence or role curriculum; authority to accept risk or approve policy; a review cadence over people, roles or authority. *PROCESS indicators*: an SLA or clock ("within 24h/72h/7 days"); a notification or escalation duty; a per-trigger activity sequence whose execution is itself the realization. Decide `CAPABILITY` only when a CAPABILITY indicator is constitutive — the rule would still bind if the procedure were executed but ownership, competence or authority lapsed; otherwise `PROCESS`. **Standing note (Doc18):** `CR-D-08.1-001` (Annual Security Awareness) and `CR-D-08.2-001` (Role-Specific Security Competence) are `CAPABILITY` even though their verification criteria are completion records — the records evidence the workforce's standing trained-ness, not a one-pass procedure.

**Tag: `APPLY-NOW`** — rubric-only edit; fixes the largest rater-drift source (all 8 hard borderlines in the dry-run sat on this seam).

---

## A3 — §4 Doc18 storage anchor: Anexo A + card fields 25/26 + exact counters (ACCEPTED as adjudicated)

**Target:** §4 storage table, first row (rubric L84: "One column in the catalog index/summary table + one field in each rule card").

**Replacement — storage table row:**

> | Rules catalog (Doc11-style, e.g. Doc18) | One `realization_class` column (+ `realization_class_secondary` where used) in **Anexo A** (per-control index); each rule card gains **field 25 `realization_class`** (mandatory) and **field 26 `realization_class_secondary`** (optional; rendered `—` when unused) |

**Insert after the storage table:**

> **Doc18 counter adjustment (campaign step).** When the fields are added: the Doc18 §3 schema table grows **24 → 26 rows** (row 25 `realization_class`, mandatory enum; row 26 `realization_class_secondary`, same enum, optional 0..1), and the Doc18 frontmatter counters change **`expected_fields_per_card: 24` → `26`** and **`fields_per_card: 24` → `26`** (25 mandatory + 1 optional; field 26 rendered `—` when unused). During the same pass the campaign may reconcile the cards' pre-existing numbering defects (92 duplicated "14. Implementation Priority" lines; no field numbered 13) against the schema table — a pre-existing Doc18 defect, not created by this rubric.

**Tag: `APPLY-NOW`** — rubric-only spec fix; the tagging campaign cannot start without the exact card-field contract and counters.

---

## A4 — §4 sync rule: legacy xlsx carried banner-noted, staleness not remediated (ACCEPTED as adjudicated)

**Targets:** §4 header line (rubric L80: "**Storage locations** (kept in sync; the Markdown catalog is authoritative):") and invariance sentence (rubric L89: "Mass re-tagging of a case is a campaign and must be consistent across all four storage locations (§4).").

**Replacement — invariance/sync sentence (replaces the L89 sentence):**

> **Sync rule.** The Markdown catalog is authoritative. Machine mirrors must carry the attribute when they are regenerated. For Case_01, the campaign adds the `realization_class` (and, where applicable, `realization_class_secondary`) column to the existing legacy `12_Rules_Catalog.xlsx` **without remediating its pre-existing staleness** — the sheet's 46 rule rows match Doc18; its NI and stub columns remain as-is, and the sheet carries a banner note marking it stale until regenerated. Cross-location consistency is required for the added columns only.

**Tag: `APPLY-NOW`** — rubric-only wording; encodes the adjudicated xlsx approach and prevents the campaign from scope-creeping into xlsx repair.

---

## A5 — §2 TECHNOLOGY definition covers physical artefact measures

**Target:** §2 class table, TECHNOLOGY row, *Definition* cell (rubric L31: "Realizable by a technical control (system/hardware/software build or configuration); no recurring human judgement needed to sustain it.") — aligns §2 with §7's folding of physical controls (rubric L124).

**Replacement:**

> Realizable by a technical or physical artefact measure (system/hardware/software build or configuration, or a physical control realised as an artefact property); no recurring constitutive human judgement needed to sustain it (§3).

**Tag: `APPLY-NOW`** — rubric-only consistency fix; zero case impact, rides the same revision.

---

## A6 — Preamble / §5 node-track claim: per-case factual statement (ACCEPTED as adjudicated; facts verified)

**Target:** preamble core-principle sentence, final clause (rubric L14: "— the AEGIS-native triad already used as node tracks in Phase 3 architectural nodes (Doc14/23/25 across cases).").

**Replacement — preamble clause:**

> — the AEGIS-native triad pre-figured in Phase 3: Case_01 `Doc23_Architectural_Nodes.md` labels each node with a `track=` field (values `TECH`/`TECHNOLOGY`, `PROC`/`PROCESS`, `ROLE`, `CAPABILITY_SUBREQ`); Case_02 `Doc24_Architectural_Nodes.md` and Case_03 `Doc25_Architectural_Nodes.md` express the same split through node-type sections (Process / IT System / Human Role / Technology / Capability Sub-Requirements) plus per-case Track Distribution tables (values `TECHNOLOGY`, `PROCESS`, `CAPABILITY_SUBREQ`, `IT_SYSTEM`, `HUMAN_ROLE`) rather than a literal per-node `track=` field. The Phase 3 lane campaign (§5) reconciles all these variants to the closed enum.

**Optional companion insert — §5 Forward pointer (rubric L105), append:**

> Existing Phase 3 track vocabulary (Case_01 per-node `track=` field; Case_02/03 section categories + Track Distribution tables) is reconciled to this enum by the lane campaign.

**Tag: `APPLY-NOW`** — rubric-only factual correction; wrong evidence must not survive into the campaign's lane-contract baseline.

---

## A7 — §6 dashboard path prefix

**Target:** §6 Visualisation bullet (rubric L112: "e.g. `00_VISUALISATIONS/Case_01/Case_01_P1_Dashboard.html`").

**Replacement:**

> - **Visualisation:** Folio VIII of the P1 dashboards (e.g. `00_METHODOLOGY/00_VISUALISATIONS/Case_01/Case_01_P1_Dashboard.html`).

**Tag: `APPLY-NOW`** — trivial rubric-only path fix; verified the file exists at the prefixed path.

---

## A8 — Additional worked examples for the two seams

**Target:** §8, after "Borderline 2" (rubric L152).

**Proposed insertion (paste at the first post-campaign rubric revision; select rule IDs and classes from the hard-borderline list in `REALIZATION_CLASS_RUBRIC_VALIDATOR_REPORT_v0.md` §6 at that time):**

> **Borderline 3 — [T/P lifecycle-seam rule, from Validator report §6].** *[Quote rule ID, primary class, secondary, and a card-anchored justification in the Borderline 1/2 format: why the lifecycle's recurring events make Q1 NO and Q2 YES.]*
>
> **Borderline 4 — [P/C standing-artefact seam rule, from Validator report §6].** *[Quote rule ID, primary class, and a card-anchored justification: why the realization is a standing maintained ability rather than a per-trigger sequence (Q2 NO → Q3 YES).]*

**Tag: `DEFER`** — quoting new exemplars before the Case_01 campaign would pre-commit borderline rules and bias the independent agreement-rate baseline; add at the first post-campaign revision.

---

## Summary

| Amendment | Theme | Tag |
|---|---|---|
| A1 | Constitutive-step test (TECHNOLOGY disqualifier) | `APPLY-NOW` |
| A2 | P/C structural indicators + CR-D-08.1/08.2 note | `APPLY-NOW` |
| A3 | Doc18 anchor Anexo A + card fields 25/26 + counters 24→26 | `APPLY-NOW` |
| A4 | Sync rule: legacy xlsx banner-noted, not remediated | `APPLY-NOW` |
| A5 | §2 TECHNOLOGY covers physical artefact measures | `APPLY-NOW` |
| A6 | Preamble/§5 node-track facts, per-case | `APPLY-NOW` |
| A7 | §6 dashboard path prefix | `APPLY-NOW` |
| A8 | Two further §8 borderlines | `DEFER` |

**APPLY-NOW: 7 · DEFER: 1.** No rule-classification data beyond the rubric's own public exemplars and the Orchestrator-adjudicated CR-D-08.1/08.2 note appears in this file.
