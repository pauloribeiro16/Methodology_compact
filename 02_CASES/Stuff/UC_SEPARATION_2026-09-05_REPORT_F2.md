---
document_id: AEGIS-CAMPAIGN-UC-SEPARATION-F2-REPORT
title: UC SEPARATION — F2 Report (Case_01)
phase: 3
version: 1.0
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: GENERATED
case: Case_01_TinyTask_SaaS
---

# UC SEPARATION — F2 Report (Case_01, 2026-09-05)

Executor report for Phase F2 of the UC SEPARATION campaign
(`02_CASES/UC_SEPARATION_CAMPAIGN_2026-09-05.md`). Scope: Case_01 use-case catalog becomes
lane-pure (UC cards only), all content preserved, **no id renames**. Rubric basis:
`00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` v1.8 — §5B rule 6 (lane-pure catalogs),
§5C.5 (annex A = UC ovals only), §5C.1/§5C.2 (lane card schemas, read-only reference).

**Bottom line:** Doc20 v3.2 holds 0 PROC/CAP cards (23 product UCs + 17 compliance UCs +
§3.0 Compliance Domain Index); annex A cleared to UC ovals only (11 diagrams); annex B
23/23 pointer↔section 1:1; all gates PASS identical to the pre-F2 baseline; ids unchanged;
no content loss; no blocking escalations.

---

## 1. Census (grep, word-boundary) — before → after

### 1.1 Structure

| Check | Before | After | Verdict |
|---|---|---|---|
| Doc20 `#### Use-Case:` cards (§2, U.C.7–11) | 23 | 23 | unchanged |
| Doc20 `#### PROC-` / `#### CAP-` stub headings | 17 / 1 | **0 / 0** | DONE |
| Doc20 lane rows in §3 package tables | 18 | 0 | DONE |
| Doc20 `#### U.C.` compliance cards (§3) | 17 | 17 | unchanged (lane-pure §3) |
| Doc20 "Sequence diagram:" pointers | 23 | 23 | unchanged |
| Doc32 `##` lane cards | 18 (17 PROC + 1 CAP) | 18 | unchanged (1:1 title match verified pre-deletion) |
| Doc32 mermaid | 18 (17 flowchart + 1 graph) | 18 | unchanged |
| Annex A useCaseDiagram blocks | 12 | **11** (§12 note-only, see §4) | §5C.5 cleanup |
| Annex A PROC-/CAP- ovals/mentions inside blocks | 18 ovals + 6 range labels (§1) | **0** | DONE |
| Annex B sequenceDiagram sections | 23 | 23 | unchanged |
| Doc20 lines | 3272 | 3131 | −141 net |

### 1.2 Per-id case-wide `.md` occurrences (whole `Case_01_TinyTask_SaaS/`)

| id | before | after | | id | before | after |
|---|---|---|---|---|---|---|
| PROC-01 | 41 | 35 | | PROC-10 | 24 | 22 |
| PROC-02 | 17 | 17 | | PROC-11 | 20 | 20 |
| PROC-03 | 41 | 39 | | PROC-12 | 32 | 32 |
| PROC-04 | 26 | 26 | | PROC-13 | 33 | 33 |
| PROC-05 | 55 | 55 | | PROC-14 | 37 | 37 |
| PROC-06 | 15 | 13 | | PROC-15 | 27 | 22 |
| PROC-07 | 22 | 22 | | PROC-16 | 20 | 19 |
| PROC-08 | 37 | 35 | | PROC-17 | 18 | 17 |
| PROC-09 | 29 | 29 | | CAP-01 | 38 | 41 |

Ids stay live everywhere (they are Doc32 lane ids); small deltas come from stub-card
removal offset by the §3.0 index re-mentioning the ids (by design) and Doc32 articulation
recounts. `00_METHODOLOGY/00_VISUALISATIONS/`: **0 hits for all 18 ids before and after**
→ dashboards untouched.

### 1.3 P5 impact (KG build E3 — frozen, documented limitation)

No id changed, so no `kg.sh impact` rename sweep applies (unlike F1). The 18 ids' nodes
are unaffected; the deleted stubs were Doc20-side duplicates of Doc32 content. No >50-node
scenario exists; no escalation.

---

## 2. Doc20 v3.1 → v3.2 (`03_PHASE3_DECOMPOSITION_RICH/Doc20_Use_Cases_Catalog.md`)

1. **18 stub cards deleted** (PROC-01..17, CAP-01 from §3.1–§3.6) after verifying 1:1
   mirroring with Doc32 (same 18 ids, same 18 titles). Their §5C-covered content
   (Trigger / Activities / Roles / SLA / Realises / Anchors / Evidence) is already in the
   Doc32 full cards (built in LANE NAMING, commit 0f63be3).
2. **§3.0 Compliance Domain Index** inserted, mirroring C3's §3 pattern:
   - overview table — per package (PKG-DP/SEC/IAM/DEV/GOV/TRN): domain focus, UCs in this
     catalog, lane cards (→ Doc32), rules covered (verbatim from the former table rows);
   - **lane-card compliance register** — per lane card, verbatim preservation of the
     fields the §5C.1/§5C.2 schemas do NOT carry: Stakeholders, Preconditions, Extensions,
     Postconditions, and the full Security & Compliance Annex (Owner, Status, Verification
     Method, Verification Criteria, Dependencies FR/NFR/NODE, Risk if not met,
     Implementation Status, Regulatory Reporting, External Auditor / Supervisory Body,
     Functional UCs constrained, Misuse cases addressed) + D-XX.Y domain + priority.
     Rationale: these fields existed **only** in the Doc20 stubs (verified by corpus-wide
     grep); dropping them would violate the campaign's zero-content-loss principle. This
     is the F1 "Priority row" precedent applied at field-block scale. Per-card CSF/PF
     anchors are in `NIST_ANCHORS.md` §3.1 (verified present for all 35 L1 ids) — table
     anchor columns were therefore safe to delete.
3. **§3 heading/intro** rewritten: lane-pure; 17 genuine UCs retained with original
   `U.C.X.Y.Z` ids; 18 non-UC cards → Doc32. Package headers retitled with true UC counts
   (4/4/5/3/1) + lane-card pointers. **§3.6 (PKG-TRN) folded into the index** — its 3
   cards are all PROC; zero UCs remained (same treatment as annex A §12).
4. **Task 4 (C3 UC-33/34 analog):** the 17 compliance-lane UCs are genuine
   actor→platform use cases and already had their dedicated section — §3, which after
   stub removal contains UC cards only (no more interleaving with lane cards). No PKG-DS
   style move needed; §3.0 index marks PKG-TRN as the 0-UC package.
5. **Metrics/count corrections** to live claims: header line ("35 security/compliance
   use cases" → "17 … + 18 lane cards in Doc32"); §3 intro ("35 … retained" → "of the 35,
   17 retained"); §6.1 trailing claim ("All 35 IDs preserved verbatim" → 17 UC ids live in
   §3.1–§3.5 + 18 lane ids in Doc32, indexed from §3.0). Frontmatter `freeze_*` values and
   historical notes (reconciliation_note, sprint6_note) left verbatim — history is not
   rewritten.
6. **Top pointer to annexes A/B added** after the header block (was missing; C3 parity).
7. **Version/history:** v3.1 → v3.2; Lane Naming section gains the v3.1→v3.2 UC SEPARATION
   paragraph; Lane Cards cross-reference rewritten ("live exclusively in Doc32 … catalogue
   holds UC cards only"); §6.3 cross-refs gain annex B + Doc32 entries; frontmatter
   outputs += Doc32, related_documents += annex B; end-of-file marker updated.

**Metrics nuance (documented, not a conflict):** the campaign's "23 UCs" is the §2 product
set (`#### Use-Case:` cards, fully-dressed). The catalog also retains the 17 compliance-lane
UCs sanctioned by task 4 (C3's UC-33/34 analog) — so total UC cards = 23 + 17 = 40, of
which 23 are the product surface. `verify_rich`-style "catalog claim" semantics for C1 is
the 23 `#### Use-Case:` cards; no metric in Doc20 now states a false total.

---

## 3. Doc32 v1.0 → v1.1 (`03_PHASE3_DECOMPOSITION_RICH/Doc32_Process_Capability_Cards.md`)

1. **`case: Case_01_TinyTask_SaaS` frontmatter field added** (CHK-1 8-field completeness,
   C3's F1 lesson). Cards themselves: **zero content changes** (no adjudications arose).
2. **Articulation table re-anchored**: the 18 "Catalogue anchor" cells pointed at
   `Doc20_Use_Cases_Catalog.md:<line>` targets inside the deleted stubs (already
   line-stale pre-F2); re-anchored to `Doc20 §3.0 Compliance Domain Index (PKG-xx)` and
   downstream ref counts recomputed on the post-F2 tree (counting convention calibrated
   exactly against the pre-existing rows on HEAD). F1 did the same when it restructured
   Doc22. Deliberate small extension of task 9's letter — the alternative was 18 rows
   pointing at deleted content.
3. **Header note updated**: the LANE-NAMING-era companion model ("narrative stays in
   Doc20") is superseded by §5B rule 6 — Doc32 is now the only lane artefact for these 18
   ids. Version bumped to 1.1 accordingly.

---

## 4. Annexes

### 4.1 Annex A (`annexes/A_Use_Case_Diagrams.md`, v0.5 → v0.6)

- §7–§11: all 17 PROC ovals + 1 CAP oval removed with their actor edges; orphan actors
  removed (DPO in §9; Risk Owner in §10; DPO/CTO/RO in §11); titles/notes updated to UC
  counts + "lane cards → Doc32".
- §11 substance note added: PKG-GOV reduces to its single UC (U.C.5.6.1); the governance
  lane (PROC-10..14, CAP-01) is diagrammed only in Doc32 §5C.4 flowcharts — recorded here
  per task 7 ("note it in the report, do not invent UCs").
- §12 (PKG-TRN): all 3 ovals were PROC — a UC-ovals-only diagram would be empty, so the
  block is replaced by a note; **annex A goes 12 → 11 useCaseDiagram blocks** (C3 removed
  its empty B.1 placeholder under the same principle).
- §1 system-wide: 6 security package ovals relabelled to UC ids only (e.g.
  "PROC-01..02, U.C.1.*" → "U.C.1.*"); PKG-TRN oval + edge removed (0 UCs) with a note.
- Verification: 11 blocks; **zero `PROC-`/`CAP-` occurrences inside any block**; zero
  orphan actors (script-checked); frontmatter reconciliation_note extended; §13
  cross-refs updated.

### 4.2 Annex B (`annexes/B_Sequence_Diagrams.md`) — no changes needed

Programmatic 1:1 check: 23 `> **Sequence diagram:** → Annex B §N` pointers in Doc20 ↔ 23
sections §1..§23 ↔ 23 §2 cards, aligned on index + id + title → **PASS** (C1 was already
id-ordered by the UML campaign; F1-style rebuild not required).

---

## 5. Verification results (verbatim)

### 5.1 Post-change structure checks

```
Doc20: Use-Case:=23, PROC heads=0, CAP heads=0, lane rows=0, U.C. cards=17, pointers=23
Annex A: mermaid=11 kinds={'useCaseDiagram': 11}; PROC/CAP inside blocks: NONE; orphan actors: NONE
Annex B: mermaid=23 kinds={'sequenceDiagram': 23}; pointers↔sections↔cards 1:1 PASS
Doc32:  mermaid=18 kinds={'flowchart': 17, 'graph': 1}; cards 18/18
Doc20:  mermaid=0 (diagrams annex-only per §5C.5)
MERMAID SANITY: PASS
```

### 5.2 Gates (baseline established pre-change FIRST; all four re-run post-change)

| Gate | Baseline (pre-F2) | Post-F2 | Verdict |
|---|---|---|---|
| `python3 03_PHASE3_DECOMPOSITION_RICH/scripts/verify_rich.py` | `[ok] verify_xlsx PASS`, 12 sheets, total_rows=386, EXIT=0 | identical, EXIT=0 | PASS, no regression |
| `python3 scripts/traceability_audit.py Case_01` (repo root) | 104/104 = 100.0% · 46/46 = 100.0% · 102/102 = 100.0% | identical (104/104, 46/46, 102/102), EXIT=0 | PASS, no regression |
| `python3 02_PHASE2_RULES_RICH/validation/check_unmapped.py` | `GATE PASS (v0.4 real: UNMAPPED, Posture, Frontmatter, Control Set YAML verified)`, EXIT=0 (pre-existing WARNs on Doc19 draft-1.1 PF ids) | identical, EXIT=0 | PASS, no regression |
| `python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py` | `# all 16 dashboard(s) passed smoke`, EXIT=0 | identical, EXIT=0 | PASS, no regression |

No gate failed at any point, so the `git archive HEAD → /tmp` baseline-fallback was not
needed. `RICH_LINT_BASELINE.md` pins no card counts → no baseline edit required (and none
made). `validation/build_control_set.py` untouched (campaign constraint; still shows the
human's pre-existing uncommitted v1.1 work in git status).

---

## 6. Files changed (git numstat; no commits made)

| File | +N | −N |
|---|---|---|
| 03_PHASE3_DECOMPOSITION_RICH/Doc20_Use_Cases_Catalog.md | 239 | 381 |
| 03_PHASE3_DECOMPOSITION_RICH/Doc32_Process_Capability_Cards.md | 25 | 23 |
| 03_PHASE3_DECOMPOSITION_RICH/annexes/A_Use_Case_Diagrams.md | 24 | 84 |

Total: +288 / −488. All edits under `02_CASES/Case_01_TinyTask_SaaS/` as scoped. One
instrument-owned file outside the case was touched by running the audit itself:
`00_METHODOLOGY/validation/TRACEABILITY_AUDIT_2026-09-05.md` (the script overwrites its
report per invocation — same behaviour as F1). Nothing under kg/, domains/, other cases,
VISUALISATIONS; `validation/build_control_set.py` untouched.

---

## 7. Residuals / known limitations

1. **Pre-existing downstream staleness (LANE NAMING-era, outside F2 edit scope):** Doc26
   §"35 security U.C.s", `CORPUS_LINKAGE.md` §3 heading ("35 L1 cards"),
   `NIST_ANCHORS.md` §3.1 heading ("Use Case cards (35 L1)" — content correctly lists
   PROC/CAP ids), `Phase_3_Functional_Decomposition_Synthesis.md` §4.3, phase
   `PROJECT_STATE.md` count tables, `progress.json` note. Ids remain valid; re-wording is
   F4/human work.
2. **Doc21/Doc22** still describe the re-laned cards under use-case relationship/variability
   framing (direct analog of C3 F1 residual #1).
3. **Doc32 "Piloted set: 4 of 18" phrase** kept (historical statement; Coverage section
   already states 18/18).
4. **KG build E3 frozen** — no rebuild; graph nodes for Doc20 §3 stubs point at content
   that moved to the §3.0 index/Doc32 (documented limitation as in prior campaigns).
5. **Borderline §3 UC titles (observation, NOT adjudicated):** U.C.2.4.2 DoS Resilience,
   U.C.3.2.1 Authorisation / Least Privilege, U.C.3.3.1 Secure System Defaults, and
   U.C.4.4.1 Fail-Safe Design lean toward the PROC definition (scheduled security
   activities). They were adjudicated to the UC lane by the LANE NAMING census, F2's audit
   mandate covers the 23 product titles only, and re-laning them would be an id rename —
   explicitly excluded from this phase. Flagged for the human (P7).

## 8. Escalations

None blocking. The two judgement calls above (compliance register in §3.0 to honour zero
content loss; articulation re-anchor in Doc32) are reasoned deviations from the task
brief's letter, both following F1 precedent, and are documented in §2/§3. The 23-vs-40 UC
count nuance is an interpretation note (§2 item 6), not a conflict with the locked plan.
