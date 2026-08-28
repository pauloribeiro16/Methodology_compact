---
document_id: AEGIS-CASE02-VALIDATOR-UNMAPPED-AUDIT
title: "VALIDATOR UNMAPPED Audit v0 — Case_02 (port Fase 3)"
phase: 2
version: 1.0
created: 2026-08-28
updated: 2026-08-28
author: Validator (port campaign, Case_01→Case_02)
status: ACTIVE
case: Case_02_SecureBorder_Solutions
---

# VALIDATOR UNMAPPED Audit v0 — Case_02

Recipe source: `../Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/validation/VALIDATOR_UNMAPPED_AUDIT_v0.md`
(census → per-category content verdicts → repairs → residual ledger).
Counting basis: `grep -o` token occurrences (stated explicitly; the Case_01
audit's 925-vs-869 header/table discrepancy is not replicated).

## §1 Source-of-truth adjudication

Canonical frozen lists (ACTIVE, 2026-08-28):
- **Privacy FW 1.0**: `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/NIST_PF/*.json`
  (100 subcategories). Any PF 1.1/IPD draft is DEPRECATED for mapping decisions.
- **AI RMF 1.0**: `CONTROLS/NIST_AI_RMF/{GOVERN,MAP,MEASURE,MANAGE}/*.json` —
  **72 subcategories (19 GOVERN + 18 MAP + 22 MEASURE + 13 MANAGE)**. This is
  the frozen AI RMF list that the Case_01 SPEC §4.3 explicitly deferred to
  "the Case_02/03 contract"; established here.
- **CSF 2.0**: `00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md` (frozen).

## §2 Corpus-wide census (baseline, PORT_census_v0 §1) → verdicts

| Variant | Occurrences | Verdict | Disposition |
|---|---|---|---|
| UNMAPPED_AIRMF | 91 | SEMANTICALLY WRONG (used as "no AI-C* mapping exists" filler; 86 in Doc19, 4 in Doc18 prose/cards, 1 in Doc16) | REPAIR: rows without AI dimension → `N/A (non-AI scope)`; rows WITH AI dimension → real anchors from the frozen list |
| UNMAPPED_PF | 61 | MIXED: 7 genuine element-level gaps; 21+ corrupted slot-fillers (repeated `UNMAPPED_PF;UNMAPPED_PF;…` next to real anchors); 2 cells with CSF IDs sitting in the PF column (CR-D-04.4, CR-D-10.3); §2 pseudo-ranges `UNMAPPED_PF..P4/P3/P9` (FORBIDDEN pattern) | REPAIR: slot-fillers collapsed to real anchors; pure gaps kept WITH mandatory justification; pseudo-ranges resolved to canonical IDs |
| UNMAPPED_CSF | 20 | LEGITIMATE (1 real gap: CR-D-05.4 data portability — CSF 2.0 has no portability subcategory, per `Framework_Crosswalk_ARM.md` §3.D-05.4; rest are prose/mermaid mentions of that gap or legit documentation) | KEEP (justified). Doc17 GV.SC-03 mixed cell: redundant token dropped (mapping exists) |
| UNMAPPED_PRIVACY | 13 | RETIRED (token violates §4.6 vocabulary) | ZERO TOLERANCE: 3 real cells → `PR.PO-P4` (canonical, aligned with Doc18 card fields); prose mentions re-labelled as retired |
| `UNMAPPED_` bare | 3 | prose | kept (documentation) |
| **Total** | **188** | | |

## §3 Repairs applied (port Fase 3, commit "port Case_02 Fase 3")

### Doc19_Framework_Mapping_Matrix.md (authoritative aggregate)
1. §1 matrix + §8/V1 mirrors: 21 CR rows without AI-C* → `N/A (non-AI scope)`;
   §3 card blocks `airmf_subcategories: [...]` likewise (38 cells total).
2. **CR-D-07.1-001** (AI_Act in regulation set, no AI-C* literal; privacy-by-design
   + secure-by-default product development): anchored to **MEASURE-2.7** ("AI
   system security and resilience are evaluated and documented") — matrix, card
   block and heatmap note updated.
3. **CR-D-07.3-001 / BPR-D-07.5-001**: `UNMAPPED_PRIVACY` cells → **PR.PO-P4**
   (canonical; matches the Doc18 card fields; card rationale rewritten — the old
   "PR.PO-P4 is a redirect" note was wrong, PR.PO-P4 is in the frozen list).
4. §2.4 Privacy FW row: 3× `UNMAPPED_PF` → **GV.PO-P1** + explicit note (PF 1.0
   frozen mirror has no dedicated roles subcategory; element gap recorded).
5. §2.6 pseudo-ranges → **GV.MT-P6 (melhoria), GV.MT-P1 (revisão)** (canonical
   texts verified against the frozen JSONs).
6. §6 pseudo-range `UNMAPPED_PF..P9` → justified `UNMAPPED_PF`.
7. 7 pure UNMAPPED_PF gaps kept WITH justification (matrix, V1 mirrors and 7 card
   blocks via `unmapped_pf_justification`): no PF 1.0 analogue for product
   patch/OTA (CR-D-02.2), MFA (CR-D-03.2), backup/DR (CR-D-04.4), physical
   third-party boundary isolation (CR-D-06.4), secure-SDLC (CR-D-07.2),
   board-training (CR-D-08.3), compliance-testing (CR-D-10.3).
8. §1/§2 header notes rewritten to the §4.6 vocabulary.

### Doc18_Rules_Catalog.md (rule-level, aligned to Doc19 §1)
- Corrupted slot-fillers collapsed (`PR.DS-P2;UNMAPPED_PF` → `PR.DS-P2`; etc.)
  across ~18 rows; 2 mis-celled rows corrected (CSF IDs found in the PF column:
  CR-D-04.4, CR-D-10.3 → justified UNMAPPED_PF, note points to Doc19 §1).
- 7 pure gaps carry the same justifications as Doc19.
- 29 cells `N/A — não mapeado a AI RMF` (Portuguese legacy form) standardised to
  `N/A (non-AI scope)`.

### Doc16 / Doc17 / SPEC
- Doc16 SO-D-01.2-002 (AI_Act axis, AI communications confidentiality — HAS AI
  dimension): `UNMAPPED_AIRMF` → **MEASURE-2.7**.
- Doc17 PO/SO-D-09.4: mixed cell `GV.SC-03, UNMAPPED_CSF` → `GV.SC-03` (mapping
  exists; token redundant).
- SPEC §4 preamble rewritten to point at new **§4.6 marker vocabulary** (added,
  mirroring Case_01 SPEC v1.1 §4.6 adapted to Case_02's 3-framework matrix);
  §4.5 rule 4, §10.1 R3 and the glossary row updated; frozen AI RMF source now
  the 72-subcat JSON list above.

## §4 Residual ledger (post-repair, all justified)

| Token | Residual | Where |
|---|---|---|
| UNMAPPED_PF | 7 rules × (matrix + V1 + card) — all with justification | Doc19, Doc18 |
| UNMAPPED_CSF | 1 real gap (CR-D-05.4 portability) + documentation mentions | Doc19, Doc17 (0) |
| UNMAPPED_PRIVACY | 0 cells; prose mentions marked RETIRED only | — |
| UNMAPPED_AIRMF | 0 cells; prose mentions marked RETIRED only | — |
| N/A (non-AI scope) | 21 CR + 8 BPR-class rules (no AI dimension) — canonical form | Doc19, Doc18 |

## §5 Honest split (matrix §1)

- 38 CR: 17 with real AI RMF anchors (AI-C* source clauses), 21 `N/A (non-AI
  scope)`, 1 additionally anchored post-adjudication (CR-D-07.1 → MEASURE-2.7,
  counted within the 21 → 20 N/A + 18 anchored effective).
- 0 tokens hide empty slots (the Case_01 "27/30 mapped" failure mode is absent
  here post-repair).

## §6 Open items

1. **CSF waiver candidates**: none found in Case_02 (no pre-existing CSF drift
   like Case_01's ID.AM-08); waiver dict for the Case_02 gate starts EMPTY.
2. Doc18's AI RMF anchors live in card table columns (fields 13-15 region);
   cross-checked for the adjudicated rules only — full per-card spot check
   happens via `build_control_set.py` in Fase 5.
3. GATE v0.3 (Fase 6) will enforce: 0 UNMAPPED_PRIVACY, 0 UNMAPPED_AIRMF,
   0 pseudo-ranges, justification on every residual UNMAPPED_PF, frozen-list
   membership for all anchors.

## §7 Verdict

GATE-adjudicated state REACHED (port Fase 3 complete). Enforcement is
mechanised in Fase 6.
