---
document_id: AEGIS-CAMPAIGN-LEDGER-ZERO-F1
title: Ledger Zero Campaign — F1 Phase Report (verify_rich C2+C3 to 8/8 PASS)
phase: Cross-phase
version: 1.0
created: 2026-09-06
updated: 2026-09-06
author: Executor (F1)
status: EXECUTED
---

# LEDGER-ZERO F1 — verify_rich Case_02 + Case_03 → 8/8 PASS

Scope held: edits only under `02_CASES/Case_02_SecureBorder_Solutions/` and
`02_CASES/Case_03_OmniBank_Financial/` (+ this report, per campaign plan §Phases).
`validation/build_control_set.py` (pre-existing uncommitted human work), `kg/**`,
`domains/**`, other cases, `progress.json` and git history all untouched. No commits made.

**Result: C2 8/8 PASS (exit 0) · C3 8/8 PASS (exit 0) · audit 100/100/100 ·
mermaid 192/192 · dashboards 16/16.**

---

## 1. Per-FAIL adjudication table

| Item | Adjudication (evidence → fix) | Fix location |
|---|---|---|
| **C2 CHK-4** dangling `BPR-D-02.2-001` | The Doc28 threat×flow row was **imported verbatim from C3's Doc29 §4 matrix** in commit 9185041 (identical row added to both cases; the id is valid only in C3's 78-control universe). C2's frozen v6.0 catalog has no D-02.2 BPR (April-era `SPRINT3_4_REPORT.md` shows an old-generation `BPR-D-02.2-001 = "Patch SLA test"`, not carried into v6.0). The row's own intent — STRIDE Tampering, "Build Pipeline → Production", "Pipeline poisoning", anchors ASVS V14.1 (build and deploy) / SAMM I-SB-A (secure build) — is owned in C2 by **`CR-D-07.3-001`** ("Secure CI/CD pipeline … signed builds, and integrity verification", NIS2-C11; realised by UC-10 CI/CD Security Gate, NODE-PROC-010, GATE-D-07.3-001). Rejected: CR-D-06.2-001 (SBOM documentation ≠ tamper-resistance), CR-D-02.2-001 (runtime product patching, not build pipeline). | Doc28_Risk_Analysis.md:224 |
| **C2 CHK-4** dangling `BPR-D-10.2-002` | Only C2 rule owning explainability is **`BPR-D-10.2-001`** ("Implement AI explainability reports for each border control decision with confidence scores and contributing factors", EU AI_Act Art. 13). FR-76/FR-82's requirement text restates it verbatim. `-002` is a suffix typo from the Volere wave (commit 0a0122b). | Doc29 FR rows (see CHK-6) |
| **C2 CHK-6** FR-76/FR-82 malformed Source Rule | Same typo; **`BPR-D-10.2-002` → `BPR-D-10.2-001`**. Corroborated: Doc26 GATE-AI-04 "AI Explainability Review" already verifies `CR-D-10.2-001, BPR-D-10.2-001` against **FR-76, FR-82**; RULE_FREEZE + P2 TRACEABILITY_AUDIT list D-10.2's BPR as `-001` only. | requirements/Doc29_Functional_Requirements.md:158,164 |
| **C2 F5-C2-03** (duplicates "if alive") | Not alive: CHK-2 reports `duplicated rows=none` (fixed by an earlier wave). No action. | — |
| **C3 CHK-3** NFR census (F5-C3-02, HIGH) | **DIAGNOSIS OVERTURNED — no truncation, no stale claim.** Doc31's body defines **56 physical cards** using per-category LOCAL ids: CONF NFR-01..12, INT 01..10, AVAIL 01..12, PRIV 01..10, ACC 01..06, COMP 01..06 (=56, matching §3's summary). The id scheme is the document's declared design (`NFR-{Category}-{Number}`, Doc31 §2). Git evidence: initial snapshot 231ed3c (`24_Non_Functional_Requirements.md`) already contained **56 `#### NFR-` headings** and the identical "Total NFRs 56" summary; card headings are **byte-identical** to today's. The "12 cards" reading was a **checker artifact**: `parse_cards()` keyed cards by bare id, collapsing the 6 category sections into 12 dict keys (max per-category range). Fix = checker-side (see §2); no document content authored. Neither prescribed branch ("correct summary to 12" / "real truncation → STOP") applied — the corpus was right, the linter was wrong. | scripts/verify_rich.py (checker) |
| **C3 CHK-6** raw-article Source Rules | With the census fixed, **all 56 cards** are now checked (previously only 12 collapsed survivors). 5 cards carried raw citations; mapped 1:1 to the C3 rules owning the cited duties (anchors cross-checked against control_set `source` fields): INT NFR-10 + ACC NFR-05 `AI-C09, AI-C10, DORA-C38` → **`CR-D-10.2-001, CR-D-09.4-001`** (control_set: CR-D-10.2-001 source "AI-C09, C10" = AI traceability; CR-D-09.4-001 source incl. DORA-C38 = AI decision logs). PRIV NFR-07 `GDPR Art. 35` → **`CR-D-09.2-001`** (IPSARA/DPIA; same mapping as the fixed FR-63 precedent). PRIV NFR-09 `AI Act Art. 14` → **`CR-D-08.2-001, BPR-D-12.3-001`** (AI-C14 human reviewers CR + dedicated Art. 14 oversight BPR). COMP NFR-06 `AI Act Art. 14, Art. 28, Art. 73` → **`BPR-D-12.3-001, CR-D-06.1-001, CR-D-04.3-001`** (Art. 14 oversight; Art. 28 third-party/supply-chain — same mapping as the fixed FR-64 precedent; Art. 73 serious-incident notification via CR-D-04.3-001, source AI-C26/C29). Article citations were **not** kept inline: C3's checker requires each comma-token to resolve exactly in the 78-control universe (no parentheticals); the article provenance remains traceable via the cited rules' `source` fields in Doc19/control_set (e.g. BPR-D-12.3-001 source is literally "EU AI Act Art. 14"). | requirements/Doc31 (5 cards) |
| **F5-C3-01** stale "63 rules" | Updated to **78 (38 CR + 40 BPR)**: Doc26 frontmatter complexity, §2 summary (Total Rules / Rules Allocated; Total Allocations recount 78→83 node-slots), §5.1 per-domain tallies (D-02 4→6 BPR, D-08 3→4, D-10 3→4; TOTAL 25→40 BPR, 63→78) + placement note, §7 SC1 cells ×3; Doc22 frontmatter complexity; plus two live summary cells of the same claim class found beyond the ledger's list: Doc27 §7 SC1 "All 63 rules via gates"→78 (true: baseline §3 confirms 78/78 via gates) and Doc29 §10 SC1 "63/63"→78/78 (CHK-7 78/78). Version-history rows kept as historical (renumber precedent). | Doc22, Doc26, Doc27, Doc29 |
| **F5-C3-03** BPR-D-12.1-001 allocation | Row already appended by commit 113ba05 but **inconsistent** (description "AI lifecycle management per CRA-C20 (AI Act Art. 9)" vs control_set "AI bias testing per NIST AI RMF 2.0"; parked in §3.10 D-10 on a node nothing else references). control_set sub_domain = **D-02.4**; Doc27 verifies it under **GATE-D-02-04** (D-02, with CR-D-02.4-001 + BPR-D-02.4-001). Fix: moved into **§3.2 (D-02), NODE-D-02-02** with the control_set description; §5.2 NODE-D-02-02 4→5 (+BPR-D-12.1); removed the orphan NODE-D-08-01.1 utilization row (its only content was the mangled pre-renumber "AI Act Art. 14" citation; the node exists nowhere else in the case). | Doc26 §3.2, §5.1, §5.2 |
| **F5-C3-04** dangling UC-99 | **Adjudicated against the suggested mapping** (see §4 ESCALATIONS): the "(real-time risk scoring)" fragment was introduced by commit 113ba05 as a partial fix ("UC-99→UC-25") and, after the F1 RENUMBER (18f326c), collides falsely with the real UC-25 "Payment Limits Management". Original intent (initial snapshot 231ed3c): `UC-99: Authenticate Admin(istrator)` — a relationships-only phantom in the **documented UC-98..118 phantom family** (Doc23 §2 census + §3 note: phantoms "keep UC- ids and participate in «include» relationships"). Mapping UC-99 to UC-33/UC-04 would contradict the node's own purpose text ("Ensures only authenticated admins configure encryption") and invent traceability. Fix: restored the phantom id in the 5 relationship rows + 1 mermaid node label. Consistent with P7 Item 4 (phantoms ratified as-is) and F2's planned consolidated phantom note. | Doc23 (5 rows + mermaid) |

## 2. Re-pointing registry

| # | Doc:line (pre-edit) | Old | New | Why |
|---|---|---|---|---|
| 1 | C2 Doc28:224 | `BPR-D-02.2-001` | `CR-D-07.3-001` | C3-imported id; C2 owner of build-pipeline integrity (signed builds) |
| 2 | C2 Doc29:158 (FR-76) | `BPR-D-10.2-002` | `BPR-D-10.2-001` | Suffix typo; GATE-AI-04 already binds FR-76 to `-001` |
| 3 | C2 Doc29:164 (FR-82) | `BPR-D-10.2-002` | `BPR-D-10.2-001` | Same |
| 4 | C3 Doc31 INT NFR-10 | `AI-C09, AI-C10, DORA-C38` | `CR-D-10.2-001, CR-D-09.4-001` | Anchor-exact per control_set sources |
| 5 | C3 Doc31 ACC NFR-05 | `AI-C09, AI-C10, DORA-C38` | `CR-D-10.2-001, CR-D-09.4-001` | Same |
| 6 | C3 Doc31 PRIV NFR-07 | `GDPR Art. 35` | `CR-D-09.2-001` | DPIA owner (IPSARA); FR-63 precedent |
| 7 | C3 Doc31 PRIV NFR-09 | `AI Act Art. 14` | `CR-D-08.2-001, BPR-D-12.3-001` | Human-oversight owners (AI-C14) |
| 8 | C3 Doc31 COMP NFR-06 | `AI Act Art. 14, Art. 28, Art. 73` | `BPR-D-12.3-001, CR-D-06.1-001, CR-D-04.3-001` | Art. 14 / Art. 28 / Art. 73 owners |
| 9 | C3 Doc23:68-70,118-119,445 | `UC-25 (real-time risk scoring): …` | `UC-99: …` | Restore documented phantom (113ba05 chimera reverted) |
| 10 | C3 Doc26:174 | BPR-D-12.1-001 row in §3.10 (D-10), node NODE-D-08-01.1 | Row in §3.2 (D-02), node NODE-D-02-02, control_set description | Consistency with control_set sub_domain + GATE-D-02-04 |
| 11 | C3 Doc26:239 | `NODE-D-08-01.1 | 1 | CR-D-08.2-001 (CR-D-08.2-001 (AI Act Art. 14 …) — human oversight)` (mangled) | Row removed | Orphan node; mangled nested parenthetical from 113ba05 |
| 12 | C3 Doc26:249 | NODE-CS-02: `CR-D-02.1-001 (AI-C09, AI-C10), CR-D-09.1-001 (DORA-C38)` | `CR-D-10.2-001 (AI-C09, AI-C10), CR-D-09.4-001 (DORA-C38)` | Correct anchor owners for AI Decision Audit Trail |
| 13 | C3 Doc22:17, Doc26:16 | `63 rules` (complexity frontmatter) | `78 rules` | F5-C3-01 |
| 14 | C3 Doc26 §2/§5.1/§7, Doc27:856, Doc29:549 | 63-rule population claims | 78 (38 CR + 40 BPR) | F5-C3-01 |

Checker change (C3 `scripts/verify_rich.py` only): `parse_cards()` now keys NFR
cards as `{Category}:{id}` (per Doc31 §2's declared `NFR-{Category}-{Number}`
scheme), so CHK-3 counts the true 56 and CHK-6 validates **all 56** Source Rules
(previously 12 collapsed survivors). This is strictly stronger, not a gate loosening.

## 3. Gate outputs (verbatim, final runs)

```
$ cd Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION && python3 scripts/verify_rich.py
verify_rich.py — Case_02_SecureBorder_Solutions (Phase 3, PORT-PARITY-2 F5)
[PASS] CHK-0 sources: control_set.yaml v6.0: 63 controls (38 CR + 25 BPR)
[PASS] CHK-1 frontmatter (8 fields): 9 DocNN docs checked; violations: none
[PASS] CHK-2 FR census: unique FR ids=84, Doc29 metadata totalFRs=84, duplicated rows=none
[PASS] CHK-3 NFR census: unique NFR ids=56, Doc30 metadata totalNFRs=56
[PASS] CHK-4 rule refs / dangling: distinct rule refs=63 across P3 docs; dangling (not in control_set 63)=none
[PASS] CHK-5 UC census: unique UC ids=36, packages=7 ['AI', 'DEV', 'DP', 'GOV', 'IAM', 'SEC', 'TRN'], metadata totalUseCases=36 (v1.0 release row claims 44 — historical, informational)
[PASS] CHK-6 corr-008 cross-refs: FR 'Source Rule' malformed=none; gate->rule dangling=none; gate->FR dangling=none
[PASS] CHK-7 rule traceability coverage: rules referenced by >=1 P3 doc: 63/63; uncovered=none; FR-level Source Rule only covers 24 rules (see RICH_LINT_BASELINE.md finding F5-C2-01)
summary: 8 checks, 0 FAIL, 8 PASS        # exit 0

$ cd Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION && python3 scripts/verify_rich.py
verify_rich.py — Case_03_OmniBank_Financial (Phase 3, PORT-PARITY-2 F5)
[PASS] CHK-0 sources: control_set.yaml v2.0: 78 controls (38 CR + 40 BPR incl. 4 D-12.x AI-specific)
[PASS] CHK-1 frontmatter (8 fields): 9 DocNN docs checked; violations: none
[PASS] CHK-2 FR census: FR cards=72, Doc30 summary 'Total FRs'=72
[PASS] CHK-3 NFR census: NFR cards=56, Doc31 summary 'Total NFRs'=56
[PASS] CHK-4 rule refs / dangling: distinct rule refs=78; dangling (not in control_set 78)=none
[PASS] CHK-5 UC census: UC cards=0; catalog claim=33 (informational)
[PASS] CHK-6 corr-008 cross-refs: FR/NFR/UC Source Rule unresolved=none; gate Rules Verified unresolved=none
[PASS] CHK-7 rule traceability coverage: rules referenced by >=1 P3 doc: 78/78; uncovered=none; FR-level Source Rule covers 49 rules
summary: 8 checks, 0 FAIL, 8 PASS        # exit 0

$ python3 scripts/traceability_audit.py all      # exit 0
| Case   | obj→ctrl            | ctrl→obj        | uc→obj_or_ctrl  |
| Case_01| 104/104 = 100.0%    | 46/46 = 100.0%  | 100/100 = 100.0%|
| Case_02| —                   | 63/63 = 100.0%  | 88/88 = 100.0%  |
| Case_03| 42/42 = 100.0%      | 78/78 = 100.0%  | 107/107 = 100.0%|

$ python3 /tmp/mermaid_check.py      # TOTAL 192 · FAIL 0 · OK 192   (exit 0)
$ python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py   # all 16 dashboard(s) passed smoke (exit 0)
```

C2 metadata consistency (CHK-5 informational): `totalUseCases=36` matches the 36
unique UC ids; the v1.0 release row's "44 UCs" is explicitly historical — no action.

## 4. Files changed (all inside allowed scope)

| File | Δ |
|---|---|
| `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc28_Risk_Analysis.md` | 1 line (re-point #1) |
| `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/requirements/Doc29_Functional_Requirements.md` | 2 lines (#2-3) |
| `02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/requirements/Doc31_Non_Functional_Requirements.md` | 5 Source Rule rows (#4-8) |
| `02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/Doc23_Use_Case_Relationships.md` | 6 lines (#9) |
| `02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/Doc26_Requirements_Allocation.md` | 13 lines (#10-14 + counts) |
| `02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/Doc22_Use_Cases_Catalog.md` | 1 line (#13) |
| `02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/Doc27_Compliance_Gates_Report.md` | 1 line (#14) |
| `02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/Doc29_Risk_Analysis.md` | 1 line (#14) |
| `02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/scripts/verify_rich.py` | parse_cards category-qualify + docstring |
| `02_CASES/LEDGER_ZERO_2026-09-06_REPORT_F1.md` | this report |

Side effect to note: `scripts/traceability_audit.py` (the mandated verification
instrument) regenerated `00_METHODOLOGY/validation/TRACEABILITY_AUDIT_2026-09-05.md`,
adding the previously missing Case_01/Case_03 sections — all rows 100%, populations
C2 63/88, C3 78/107. Kept as the tool's own output; no manual edit.

## 5. ESCALATIONS / Orchestrator attention

1. **F5-C3-02 diagnosis overturned (was HIGH "suspected truncation")** — git
   archaeology proves all 56 NFR cards existed from the initial snapshot with
   per-category local ids; the "12 cards" census was a checker parsing artifact.
   **No content was lost or restored; no escalation on content.** Ledger §5 rows
   for F5-C3-02 should be re-dispositioned accordingly at F9 close-out. The
   GENERATED census notes that still describe "12 NFR cards" (RULE_FREEZE.md §3,
   RICH_LINT_BASELINE.md) are superseded by this report — left untouched as
   v0 snapshot artefacts, per campaign convention.
2. **Prior commit 113ba05 over-claimed and left residue** — its message asserts
   "C3-02 Doc31 summary 56→12" (never landed; would have been wrong),
   "C3-04 UC-99→UC-25" (created a chimera that collided with real UC-25 after the
   renumber; reverted here) and "C3-03 BPR-D-12.1-001 appended" (appended
   inconsistently + mangled two §5.2 rows; corrected here). Recommend the
   Orchestrator treat 113ba05's message as unreliable when auditing history.
3. **UC-99 adjudication deviates from the task's tentative hint** (UC-33 /
   OmniScore): evidence shows UC-99 was never a card id — it is a member of the
   documented UC-98..118 phantom family; restoring it is the only evidence-
   consistent fix. If the human prefers UC-99 mapped to a real UC instead, that is
   a P7 call (would need a real "Authenticate Administrator" card, which no current
   catalog card provides).
4. **Out-of-F1-scope observations** (renumber/drift residue, not touched):
   - Doc23 §2 census stale post-renumber ("Total Use Cases 93 (UC-01..93)";
     "PROC-01..40" / "CAP-01..07" ranges vs current PROC-39..50 / CAP-08..10).
   - Frontmatter "62 use cases" persists across Doc22/25/27/28/29/31 (Doc31's own
     complexity line still says "62 use cases, 56 NFRs" — the 56 is correct).
   - Doc25 NODE-CS-002 still cites raw "AI-C09, AI-C10" (not rule-shaped, so not
     flagged by CHK-4); Doc26 §6 lists only the 38 CR→UC rows (BPR→UC coverage
     lives in Doc21/25/27/31; CHK-7 confirms 78/78).
   - C2 FR-level Source Rule covers 24/63 rules (known F5-C2-01 baseline).
   - Doc26 §2 "Nodes Used 28/28" predates F1 and uses a different node-id space
     than Doc25 (NODE-D-XX vs NODE-PROC-XXX) — candidate for a future census item.
5. `validation/build_control_set.py` remains in its pre-existing modified state
   (human work, 22 inserted lines) — not touched, not staged, not committed.

No commits were made (per campaign invariant); working tree left for Orchestrator
verification between phases.
