---
document_id: AEGIS-CASE03-VALIDATOR-UNMAPPED-AUDIT
title: "VALIDATOR UNMAPPED Audit v0 — Case_03 (port Fase 3)"
phase: 2
version: 1.0
created: 2026-08-28
updated: 2026-08-28
author: Validator (port campaign, Case_01→Case_03)
status: ACTIVE
case: Case_03_OmniBank_Financial
---

# VALIDATOR UNMAPPED Audit v0 — Case_03

Recipe: same as Case_02's `VALIDATOR_UNMAPPED_AUDIT_v0.md`. Counting basis:
`grep -o` token occurrences (stated). Baseline: `validation/PORT_census_v0.md`.

## §1 Source-of-truth

Frozen lists: Privacy FW 1.0 (`CONTROLS/NIST_PF/*.json`), AI RMF 1.0
(`CONTROLS/NIST_AI_RMF/*/*.json`, 72 subcats — established during the Case_02
port), CSF 2.0 (frozen list lives upstream; WARN-only check in the gate).
DORA: no framework column — `via_CSF` design decision preserved (Doc21 §0,
ontology invariant).

## §2 Census → verdicts

| Variant | Occ. | Verdict | Disposition |
|---|---|---|---|
| UNMAPPED_AIRMF | 140 | SEMANTICALLY WRONG. Clean split verified: 15 CR with AI-C* carry real frozen-list anchors; **no AI_Act-bearing row carries the token** (unlike Case_02's CR-D-07.1 case) | REPAIR: all cells → `N/A (non-AI scope)` (78 matrix/V1 cells + 56 card lists) |
| UNMAPPED_PF | 91 | MIXED: mixed real-anchor+token cells in Doc20 (collapsed); 7 CR + 7 BPR + card blocks = genuine element-level gaps | KEEP with mandatory justification; collapse slot-fillers |
| UNMAPPED_CSF | 20 | LEGITIMATE (1 real gap: CR-D-05.4 data portability — no CSF subcategory; D-08.1 user-side awareness note in Doc14) | KEEP justified |
| UNMAPPED_PRIVACY | 8 | RETIRED | 0 cells (only §6.2 verdict notes, relabelled `UNMAPPED_PF (CT.DP family …)`); prose marked retired |
| bare UNMAPPED_ | 3 | prose | kept |
| **Total** | **262** | | |

## §3 Repairs applied (port Fase 3)

1. **Doc21**: 78 `UNMAPPED_AIRMF` cells + 56 `airmf_subcategories` card lists →
   `N/A (non-AI scope)`; 24 PF cells justified per rule (matrix + V1 mirrors);
   16 card blocks gained `unmapped_pf_justification:` lines; §6.2 labels
   `UNMAPPED_PRIVACY (CT.DP family …)` → `UNMAPPED_PF (…)`;
   §1/§6.1 header notes rewritten to the §4.6 vocabulary.
2. **Doc20**: 51 Portuguese AI RMF placeholders (`— (não mapeado a AI RMF …)`,
   `N/A — não mapeado a AI RMF`) → `N/A (non-AI scope)`; mixed
   `PR.DS-P2; UNMAPPED_PF` cells collapsed; 14 pure PF cells justified
   (7 CR + 7 BPR; wording mirrors Doc21).
3. **Doc19**: mixed cell `GV.SC-03, UNMAPPED_CSF` → `GV.SC-03` (redundant token).
4. **SPEC**: §4.6 marker vocabulary section added (canonical, DORA-aware);
   §4.5 rule 5, R3 and glossary row updated.

## §4 Residual ledger (post-repair, deliverables)

| Token | Residual | Form |
|---|---|---|
| UNMAPPED_PF | 14 Doc20 cells + 24 Doc21 cells/notes + card tokens | ALL justified (parenthetical or `unmapped_pf_justification`) |
| UNMAPPED_CSF | CR-D-05.4 row + card lists + prose | Legitimate gap, documented |
| UNMAPPED_PRIVACY / UNMAPPED_AIRMF | 0 cells; prose mentions only (vocabulary notes, RETIRED markers) | — |
| N/A (non-AI scope) | 23 CR + BPR-class rules | canonical form |

## §5 Honest split (Doc21 §1)

38 CR = 15 with real AI RMF anchors (AI-C* sources) + 23 `N/A (non-AI scope)`.
0 tokens hide empty slots. DORA influence is recorded per-row in the
`regulations` column and anchored via CSF (via_CSF invariant) — never via an
invented DORA framework ID.

## §6 Verdict

GATE-adjudicated state REACHED (port Fase 3 complete). Enforcement mechanised
in Fase 6 (check_unmapped.py case03).
