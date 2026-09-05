---
document_id: AEGIS-METHODOLOGY-ALT-ANCHOR-CRITERION
title: ALT-ANCHOR Criterion — Multi-Referential Anchoring for Framework Gaps
phase: Cross-phase
version: 1.0
created: 2026-09-05
updated: 2026-09-05
author: Orchestrator (Executor duties in-conversation)
status: ACTIVE
---

# ALT-ANCHOR Criterion

> **Core Principle:** A framework-mapping gap is not a dead end. When a rule element has
> no subcategory in a target framework (PF 1.0, CSF 2.0), the element is anchored to the
> sibling referential that DOES cover it. The old `UNMAPPED_*` marker family is RETIRED —
> it described the hole without pointing at the ground next to it.

---

## §1 Vocabulary (replaces the UNMAPPED_* family)

| Marker | Meaning | Grammar |
|---|---|---|
| `ALT-ANCHOR (ref1; ref2; …)` | No subcategory exists in the framework being mapped (PF or CSF); the element is covered by one or more sibling referentials from the frozen set. | refs separated by `;`, referential prefix + id, e.g. `(800-53r5 IA-2(1); ASVS V3.5)` |
| `ALT-ANCHOR (NO-ANALOGUE)` | No referential in the frozen set honestly covers the element. Terminal state; goes to the P7 human queue. Never force an anchor. | no refs inside the parentheses |

**RETIRED markers (forbidden in live case docs):** `UNMAPPED_PF`, `UNMAPPED_CSF`,
`UNMAPPED_AIRMF`, `UNMAPPED_PRIVACY`, bare `UNMAPPED`. Historical validation reports and
the retirement notes themselves are the only allowed contexts (waived by the gates).

## §2 Frozen referential set

| Prefix | Referential | Frozen source | Valid id forms |
|---|---|---|---|
| `800-53r5` | NIST SP 800-53 Rev. 5 | `CONTROLS/NIST_80053R5/*.json` (719 ids) | `XX-n`, `XX-n(k)`; legacy aliases `IP-3`, `DM-1` (r4-retired families, accepted as citation ids only) |
| `SSDF` | NIST SSDF (SP 800-218 v1.1) | `CONTROLS/NIST_SSDF/SSDF.json` (21 practices / 47 tasks) | `PO.n[.k]`, `PS.n[.k]`, `PW.n[.k]`, `RV.n[.k]` |
| `ASVS` | OWASP ASVS 4.0.3 | `CONTROLS/OWASP_ASVS/ASVS_sections.json` (14 chapters / 71 sections) | `Vn`, `Vn.k` (chapter or section granularity) |
| `SAMM` | OWASP SAMM v2 | `CONTROLS/OWASP_SAMM/SAMM_streams.json` (5/15/30) | `F-PP-S[-L]` full code (e.g. `G-EG-A`, `G-EG-A-2`); bare `EG`/`VR` forms are INVALID |
| `ISO` | ISO/IEC 27002:2022 | crosswalk in `REALIZATION_CLASS_RUBRIC.md` §7 | `A.5.x`… clause ids; LAST RESORT only |

A gate validating an anchor accepts an id iff it resolves in the frozen source
(or, for 800-53r5, the two registered legacy aliases).

## §3 Per-class anchor hierarchy (routing by realization_class)

1. **TECHNOLOGY** → `800-53r5` first (control families), then `SSDF` (secure-development
   specifics), then `ASVS` (application-verification specificity). 
2. **PROCESS** → `800-53r5` first (program/IR/CM families), then `SAMM` (activity-stream
   level), `SSDF` where the process is development-lifecycle work.
3. **CAPABILITY** → `SAMM` first (governance practices; the SAMM level ties to maturity
   model v1.6 Scale A / EvidenceItem), then `800-53r5` (PL/CA/AT/PM families), `ISO`
   as last resort.

**Selection honesty:** an anchor must state what the referential control actually covers.
A partial overlap is acceptable when declared in the surrounding justification text
(already present in the case docs). If the overlap would be cosmetic → `NO-ANALOGUE`.

## §4 Dedup rule

One anchor decision per **rule-element** (canonical gap element), propagated to every
occurrence site (matrix §1 row, matrix secondary mirrors, rule card field 20/21,
objective cards, NIST_ANCHORS.md). The canonical decision table lives in
`00_METHODOLOGY/validation/ALT_ANCHOR_CENSUS_v0.md`.

## §5 The 800-53r5 matrix column (generated view)

Every matrix row carrying PF/CSF ids gains an `800-53r5` column whose content is the
union of the crosswalks of the PF ids in that row, sourced from the
`related_refs`/`informative_references` fields of `CONTROLS/NIST_PF/**/*.json`.

**Generator contract (anti-drift, mechanical):**
- Script `scripts/build_alt_anchor_columns.py` is the ONLY writer of this column.
- Source of truth: the PF JSONs (and, where a row has no PF id, the CSF id → the frozen
  `CONTROLS/NIST_CSF_2.0/` list has no 800-53 mapping, so the column reads `— (see ALT-ANCHOR cells)`).
- Idempotent: re-running on a written file produces a zero diff.
- Abort-on-unknown: if a PF id has no JSON or a crosswalk id is not in `NIST_80053R5/`
  (or the two legacy aliases), the script exits non-zero without writing.
- The column is a generated view — hand edits will be overwritten by design.

## §6 Case-spec delegation

The three case-scoped specs (`02_PHASE2_RULES_RICH/SPEC_NIST_MATRIX_UNIFIED.md` in
Case_01/02/03) remain the case-local operating detail; their marker vocabulary sections
are superseded by this document from v1.0. Where they conflict, this document wins.

## §7 Governance

- Adding a referential to the frozen set, changing a class route, or redefining a marker
  requires human approval (P7), via the Orchestrator.
- The `NO-ANALOGUE` set is re-presented to the human at each campaign close.

**Version history**

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 2026-09-05 | Orchestrator | Initial release — decisions locked with the human 2026-09-05 (ALT-ANCHOR campaign) |
