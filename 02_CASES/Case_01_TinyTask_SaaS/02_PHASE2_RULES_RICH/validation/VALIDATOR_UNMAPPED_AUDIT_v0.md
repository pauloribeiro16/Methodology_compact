# VALIDATOR — UNMAPPED_* Audit v0 (Case_01 Phase 2)

**Date:** 2026-08-27
**Validator:** Orchestrator (content audit per `audit-content-not-wrappers` rule)
**Scope:** All `UNMAPPED_*` markers in `02_PHASE2_RULES_RICH` (Doc16, Doc18, Doc19, SPEC) + corpus-wide census
**Gate:** `validation/check_unmapped.py` — **GATE PASS** (exit 0)

---

## 1. Adjudication (source-of-truth dispute)

| Artefact | Status | Verdict |
|---|---|---|
| `NIST_PF_1.0_subcategories.md` (Methodology-main `_global/`) | ACTIVE | **CANONICAL** — official PF 1.0 (Jan 2020), 5 Functions / 18 Categories / **100 Subcategories**; mirrored 1:1 by `CONTROLS/NIST_PF/` |
| `NIST_Privacy_FW_1.1_subcategories.md` (Methodology-main `PREPROCESSING/`) | DEPRECATED | PF 1.1 = **Initial Public Draft (14 Apr 2025), non-final** — migration/crosswalk only; may NOT exclude or replace canonical IDs |

Doc19 v1.0 had excluded the families `PR.AC-P1..P6`, `PR.MA-P1/P2`, `PR.PT-P1..P4`, `ID.DE-P1..P5` as "redirects in v1.1" — based on the **draft**, contradicting its own frontmatter (which cites the canonical list). All four families are reinstated as ACTIVE mapping targets.

## 2. Marker semantics (now codified in SPEC §4.6)

| Marker | Meaning | Requirement |
|---|---|---|
| `UNMAPPED_PRIVACY` | whole rule has no PF anchor | short inline justification |
| `UNMAPPED_PF` | one element of a mapped rule lacks a PF 1.0 counterpart | `unmapped_pf_justification` (YAML) or inline `(...)` |
| `N/A (non-AI scope)` | rule has no AI dimension (Cases 02/03 AI RMF column) | — |
| `pending Case_02/03` | Case_01 AI RMF column placeholder (SPEC §4.3) | — |

Forbidden: pseudo-ranges (`UNMAPPED_PF..P4`), ID-substitution by tokens, justification-less tokens, draft-based family exclusions.

## 3. Corpus-wide census (925 occurrences → verdicts)

| Token | Occurrences | Verdict | Action |
|---|---|---|---|
| `UNMAPPED_CSF` | 352 (66 domain-corpus files + cases) | **LEGITIMATE** — collapses to 3 unique reasons: GDPR Art. 49 derogation (transfer-legality, not security), Art. 9 special-category consent (privacy construct), CRA Annex II §8 user-side instructions (information duty, not a control) | none (doc-level: domains/** is guard-protected and content is honest) |
| `UNMAPPED_PRIVACY` | 50 | **LEGITIMATE** — product-security trio (patch cadence, CVD, SBOM); PF 1.0 genuinely lacks patch/CVD/SBOM categories (the `PR.PS` family exists only in the draft) | none |
| `UNMAPPED_PF` | 280 (103 in Case_01 Phase 2) | **CORRUPTED** in majority: (a) draft-based exclusions of valid families; (b) find-and-replace substituted real IDs in §6.2/§6.3/§4.3 tables; (c) slot-filler tokens in §1/§7 without justification; (d) 1 occurrence propagated into the KG (build E3 `graph.json`) | **FIXED this audit (Case_01)**; Cases 02/03 pending |
| `UNMAPPED_AIRMF` | 237 (Cases 02/03) | **SEMANTICALLY WRONG** — appears exactly on rows whose source regulations exclude AI_Act; correct marker is `N/A (non-AI scope)` | **PENDING (Case_02/03 sessions)** |

## 4. Case_01 changes (this audit)

- **SPEC §4.2:** canonical numbers (100 subcats); draft-1.1 status documented. **§4.5/§4.6:** marker vocabulary + forbidden patterns + frozen-ID rule.
- **Doc19 §1:** 10 CR rows remapped to canonical IDs — `PR.AC-P1/P4/P6` (identity/MFA/least-privilege), `PR.PO-P3` (backups), `PR.PO-P7` (IR/recovery plans), `PR.DS-P2/P4` (in-transit, capacity), `PR.PT-P4` (resilience), `ID.DE-P1..P4` (ecosystem policies/contracts), `GV.PO-P3`, `GV.RM-P1`, `GV.MT-P1`, `GV.AT-P1`, `PR.DS-P1`. Remaining element-level tokens (45 total across Doc16/18/19, was 103) are genuine no-PF-1.0-analogues (logging, RS.MA reporting, RC.RP recover axis, SDLC, positive-risk, asset inventories, identity assertions), each justified.
- **Doc19 §2:** pseudo-ranges `UNMAPPED_PF..P3/P4` eliminated (real IDs or `-`).
- **Doc19 §4.3:** 18 maturity-scale rows de-tokenised (13 → canonical IDs; 5 → `N/A-PF (draft-1.1)` CSF-mirror scales, labelled).
- **Doc19 §6.2/§6.3:** all "covered by UNMAPPED_PF" circular rows restored to real IDs or justified gaps; "WITHDRAWN in PF 1.1" notes corrected (canonical PF 1.0 has no withdrawals).
- **Doc19 §7:** summary table synced with §1.
- **Doc16:** 4 PF-table rows + 4 detailed-card field-6 lines updated to match.
- **Doc18:** 6 cards (4 CR + 2 BPR) field 20 updated with canonical IDs + justifications.
- **Counts §1:** honest split — 13 rows fully mapped / 14 partially (justified element gaps) / 3 UNMAPPED_PRIVACY. (Was "27/30 mapped", hiding ~17 empty slots.)

**Verification:** `python3 validation/check_unmapped.py` → GATE PASS. Validated: zero ranges; every token justified; every PF id ∈ canonical 100; Doc19 AI RMF = 30/30 `pending Case_02/03` with zero real AI RMF ids.

## 5. Pre-existing drift discovered (waived, NOT fixed here)

CSF-side, unrelated to UNMAPPED: `ID.AM-08` (frozen CSF list tops at ID.AM-07; already documented Doc19 §6.1) ×15; `ID.SC-04` ×2, `PR.IP-06/07`, `PR.ST-01`→`PR.PT-01` (CSF 1.1 carry-overs in Doc16 §7 mirrors) ×4. Waived in the gate with warnings; recommend normalisation in a dedicated Block-D session.

## 6. Open items (human / next sessions)

1. **P7 — INFORMATION duties placement:** user-side instruction duties (e.g., SR-CRA-071, CRA Annex II §8) are information-provision obligations, not security controls. Keep in the security corpus flagged, or move to a separate compliance register? Human decision.
2. **Case_02 session:** PF false-unmapped repair (same recipe) + reclassify `UNMAPPED_AIRMF` → `N/A (non-AI scope)` on rows without AI_Act.
3. **Case_03 session:** idem.
4. **KG rebuild:** build E3 `graph.json` contains 1 corrupted `UNMAPPED_PF` occurrence (guard-protected; do not edit directly) — next graphify rebuild in the main repo must re-ingest the corrected sources.
5. **Stale input paths:** Doc19 frontmatter `inputs` cites `PREPROCESSING/...` layouts that moved to `PREPROCESSING_by_domain/` (provenance only; no ID impact).


---

## 7. Addendum: Implementation Posture Transition & Sprint Sweep

**Date:** 2026-08-27  
**Validator:** Validator & Executor (AEGIS Orchestration)

### Summary of Actions Taken:
1. **Implementation Posture Model v2.0 Finalization:**
   - Legacy numerical maturity scales (0–4 scores, T1–T4 Tiers) were completely removed across all Case_01 Phase 1, Phase 2, and Phase 3 markdown deliverables.
   - Replaced with qualitative Implementation Posture states (`IMPLEMENTED`, `PARTIAL`, `NOT IMPLEMENTED`, `N/A`).
   - Corrected uniformity anti-pattern across `Doc16` (31 SO/PO cards) and `Doc18` (46 CR cards) by deriving non-uniform, evidence-backed statuses citing concrete `Doc04a`/`Doc05` pointers for `IMPLEMENTED` cards and concise gap descriptions for `PARTIAL` / `NOT IMPLEMENTED` cards.
   - Updated `SPEC_NIST_MATRIX_UNIFIED.md` §7 and `Doc17` (`maturity_target_micro:` -> `posture_note_micro:`) while preserving historical audit lines (L1/L2/L3/D3).

2. **Validation Gate v0.2:**
   - Updated `validation/check_implementation_posture.py` to enforce zero tolerance for `/maturi/i` in Case_01 deliverables and verify non-uniformity across card status distributions.
   - Gate result: **`GATE PASS`**.

3. **Sprint Metadata Sweep:**
   - Swept legacy `sprint:` keys from YAML frontmatters and `(Sprint N)` from titles across deliverables (`Doc01` to `Doc31`, `SPEC`, `RULE_FREEZE`, `README.md`).
   - Historical reports in `validation/`, `RICH_VS_LEGACY.md`, and the change log in `PROJECT_STATE.md` were preserved for audit traceability.
