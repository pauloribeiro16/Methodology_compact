---
document_id: AEGIS-CAMPAIGN-UC-SEPARATION-F3-REPORT
title: UC SEPARATION — F3 Report (Case_02)
phase: 3
version: 1.0
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: GENERATED
case: Case_02_SecureBorder_Solutions
---

# UC SEPARATION — F3 Report (Case_02, 2026-09-05)

Executor report for Phase F3 of the UC SEPARATION campaign
(`02_CASES/UC_SEPARATION_CAMPAIGN_2026-09-05.md`). Scope: Case_02 use-case catalog becomes
lane-pure (UC cards only), all content preserved, **no id renames**. Rubric basis:
`00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` v1.8 — §5B rule 6 (lane-pure catalogs),
§5C.5 (annex A = UC ovals only), §5C.1/§5C.2/§5C.4 (lane card schemas/diagrams, read-only
reference). Patterns: F1 (Case_03, 32f45f7) and F2 (Case_01, 47ad056).

**Bottom line:** Doc21 v1.5 holds 0 PROC/CAP cards and 0 lane rows in UC sections (21
product UCs + 15 compliance UCs + §6.6/§7.0 lane registers); annex A cleared to UC ovals
only (6 diagrams); annex B 21/21 pointer↔section↔card 1:1; all 5 relocated/named ids
unchanged; `verify_rich` improves 3 FAIL → 2 FAIL (F3 fixes the baseline CHK-1 finding);
remaining 2 FAILs are pre-existing human-decision findings, byte-identical to the HEAD
baseline (proven via `git archive` run); traceability audit 100/100; dashboards 16/16;
no content loss; no blocking escalations.

---

## 1. Census (grep, word-boundary) — before → after

### 1.1 Structure

| Check | Before | After | Verdict |
|---|---|---|---|
| Doc21 lines | 4249 | 3429 (−820 net) | restructure |
| Doc21 `#### Use-Case: {U.C.…}` product cards (§6) | 21 | **21** | unchanged |
| Doc21 `#### Use-Case: {PROC-…}` stubs (§6) | 5 | **0** | DONE |
| Doc21 `### 9.x PROC-…` detailed headings (§9) | 5 | **0** | DONE (moved to Doc31) |
| Doc21 §7 domain-table lane rows | 32 | **0** | DONE (register §7.0) |
| Doc21 "Sequence diagram:" pointers | 26 | **21** | 5 PROC pointers left with the stubs |
| Doc31 `## PROC-` / `## CAP-` full cards | 27 / 10 | 27 / 10 | unchanged (1:1 title match verified pre-deletion) |
| Doc31 mermaid | 37 (27 flowchart + 10 graph) | 37 | unchanged |
| Doc31 detailed narratives | 0 | **5** | received from Doc21 §9 (verbatim) |
| Annex A useCaseDiagram blocks | 6 | **6** | all UC-ovals-only now |
| Annex A PROC-/CAP- ovals inside blocks | 5 ovals + 6 lane edges (§3–§6) | **0** | DONE |
| Annex B sequenceDiagram sections | 26 (incl. stale B.1 placeholder header) | **21** | 5 PROC sections removed per §5C.5 |
| VISUALISATIONS hits for all C2 lane ids | 0 | 0 | untouched (smoke still run: 16/16) |

### 1.2 Per-id whole-case `.md` occurrences (Case_02)

| id | before | after | | id | before | after |
|---|---|---|---|---|---|---|
| PROC-23 | 18 | 22 | | PROC-26 | 33 | 29 |
| PROC-24 | 31 | 28 | | PROC-27 | 21 | 20 |
| PROC-25 | 34 | 29 | | | | |

Ids stay live everywhere (Doc31 cards + Doc21 §6.6/§7.0/§13 + Doc22/23/27); deltas come
from stub removal offset by the new register/index mentions and the Doc31 relocation notes.

### 1.3 P5 impact (KG build E3 — frozen, documented limitation)

No id changed, so no `kg.sh impact` rename sweep applies (F2 precedent). The 37 lane ids'
nodes are unaffected; deleted Doc21 content was Doc21-side duplication/register of Doc31
content. No >50-node scenario; no escalation.

---

## 2. Title audit (task 2) — 21 product UC cards vs the frozen classification rule

All 21 `#### Use-Case: {U.C.8+}` titles are genuine actor→platform, event-driven use cases
with observable system responses (scan/capture/match/release, console session, queue
triage, override, OTA, admin config, audit export, dashboards). **0 surprises requiring
adjudication → no new PROC-28+/CAP-11+ ids created, no renames.**

Two borderline observations (flagged, NOT adjudicated — F2 residual #5 precedent; both were
LANE NAMING-adjudicated to the UC lane, and re-laning would be an id rename, outside F3
scope): **U.C.10.5.1 Offline/Failover Mode** and **U.C.11.5.1 Watchlist Cache Sync** lean
toward persistent system behaviour (CAP definition); both retain actor-facing flows (Ops
Lead consumes failover reconciliation / sync versions). Human call (P7) if they should
become CAP-11/CAP-12 in a later campaign.

Compliance-UC audit (task 3): C2's compliance UCs (15 U.C. rows in §7 + 2 detailed cards in
§9) **were** interleaved with PROC/CAP content in the same sections → separated this pass:
§7 domain tables now hold U.C. rows only (lane rows → §7.0 register; UC-TRN folded — 0
UCs, C1 PKG-TRN precedent); §9 keeps the 2 detailed compliance UCs only (mirrors C1 §3 /
C3 PKG-DS lane-purity).

---

## 3. Doc21 v1.3 → v1.5 (`03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md`)

1. **5 PROC stub cards deleted** (§6.2–§6.5) after verifying 1:1 id+title mirroring with
   Doc31 full cards (§5C.1-covered fields already there). Their §5C.1-absent fields are
   preserved **verbatim** in the new **§6.6 Lane Card Register (PROC-23..27 → Doc31)**:
   per card — Brief Description, Preconditions, Post-conditions, FURPS+, full Security &
   Compliance Annex (Provenance/Constrained by/Rules/Threats/NIST anchors) + package,
   priority, rules, Doc31 pointer, Formerly ids (F2 §3.0 register precedent).
2. **32 §7 lane rows removed** (PROC-01..22, CAP-01..10); **§7.0 Compliance Domain Index**
   inserted: overview table per domain (UCs retained, lane cards → Doc31, rules covered
   verbatim-union) + **lane-card compliance register** — all 32 rows verbatim (Description,
   Primary Actor, Related Rules/Goals/PSOs, Priority, Regulation, SLA — fields Doc31 does
   not carry). **§7.7 UC-TRN folded into §7.0** (0 UCs, 5 CAP cards; C1 precedent).
3. **5 §9 PROC detailed cards moved verbatim to Doc31** (narrative: Main Flow, Alt Flows,
   Exceptions, Business Rules BR-*, FR/NFR links, Tension References — none of it existed
   in Doc31); §9 retitled note + keeps U.C.1.2.1 (9.1) and U.C.3.3.1 (9.2).
4. **PKG tables/§6.0**: PROC rows removed; package counts 5/5/5/4 → **4/4/3/3**; "Drives"
   cells reworded to UC ranges.
5. **Metrics corrected to true UC counts**: §2 `totalUseCases` 44 → **36 (21 product +
   15 compliance)**; §14 Total 36, Level 1 36, Level 2 detailed 2, priorities recomputed
   over the 36 (19 C / 15 H / 2 M / 0 L, with product/compliance split); §12 Priority
   Distribution recomputed over its original compliance scope (8 C / 6 H / 1 M / 0 L — the
   pre-existing counts were also internally wrong: 14/22/6/2 vs 17/25/5/1 listed); §13
   gains a note that PROC-/CAP- attributions refer to Doc31 lane cards.
6. **TOC/numbering hygiene**: §7 children 9.1–9.7 → 7.0–7.7; §10 child 8.1 → 10.1; §11
   child 9.1 → 11.1; §12 children 5.1/10.2 → 12.1/12.2; §13 children 11.1–11.3 → 13.1–13.3.
7. **Frontmatter/version**: v1.3 → **v1.5** (history already carried a v1.4 row — pre-existing
   frontmatter inconsistency fixed); outputs → DocNN names + Doc31 (C3 F1 precedent);
   related_documents += annexes A/B; **top pointer block to annexes A/B + Doc31 added**
   after the title; v1.5 version-history row; Lane Naming gains the v1.4→v1.5 paragraph;
   Lane Cards cross-reference rewritten (catalog UC-only; 27 PROC + 10 CAP in Doc31).

## 4. Doc31 v1.0 → v1.1 (`03_PHASE3_DECOMPOSITION/Doc31_Process_Capability_Cards.md`)

1. **`case: Case_02_SecureBorder_Solutions` frontmatter field added** — fixes the corpus's
   last CHK-1 violation (baseline finding F5-C2-04); verify_rich CHK-1 now fully PASS.
2. **5 detailed narratives received verbatim** under PROC-05/07/19/20/14 cards as
   `### Detailed narrative (from Doc21 §9, verbatim — UC SEPARATION 2026-09-05)`.
3. **Articulation table re-anchored** (F2 precedent): "Catalogue anchor" was `Doc21: ?` for
   all 37 rows → `Doc21 §7.0 Compliance Domain Index (register row)` (32 rows) /
   `Doc21 §6.6 Lane Card Register` (5 rows); downstream ref counts recomputed on the
   post-F3 tree, word-boundary convention (calibrated against HEAD; 2 pre-existing rows
   were off-by-1 on HEAD — stale, noted).
4. Header note rewritten (exclusive lane home per §5B rule 6; relocations recorded);
   `traceability:` rubric reference v1.4 → v1.8; version 1.1.

## 5. Annexes

### 5.1 Annex A (`annexes/A_Use_Case_Diagrams.md`, v1.0 → v1.1)

- §3–§6: all 5 PROC ovals removed with their actor edges and the `UC1041 ..> PROC24`
  extend edge; orphan actors removed (Compliance Analyst §3; Dev Lead/DPO/AI Market
  Surveillance §5; Border Control Officer §6); per-oval PROC note blocks removed.
- §1 system-wide: package oval counts 5/5/5/4 → **4/4/3/3**; §3–§6 titles carry true UC
  counts; prose reworded (lane sequencing kept as prose pointers to Doc31, allowed —
  §5C.5 bans ovals/actors, not mentions).
- Verification: **6 blocks; ZERO `PROC-`/`CAP-` ids inside any block; ZERO orphan actors;
  zero undefined aliases** (script-checked); element budget footer recounted (11/12/8/8/7/11);
  frontmatter `reconciliation_note` added.

### 5.2 Annex B (`annexes/B_Sequence_Diagrams.md`, v1.1)

- **5 PROC sections removed** (§12 PROC-23, §13 PROC-24, §18 PROC-25, §21 PROC-26, §26
  PROC-27): lane cards do not carry sequence diagrams (§5C.5) — their diagrams are the
  §5C.4 flowcharts in Doc31 (the flows remain preserved there as derived views).
- Remaining sections renumbered **§1..§21 ordered by id**; stale "B.1 Critical Path
  Sequences" PLACEHOLDER block deleted and `[CASE_NAME]` header replaced with proper
  8-field frontmatter, Status PLACEHOLDER → ACTIVE (C3 F1 precedent).
- Verification (programmatic): **21 pointers ↔ 21 sections ↔ 21 §6 cards, 1:1 aligned,
  ordered, zero PROC in annex B.**

---

## 6. Verification results (verbatim)

### 6.1 `verify_rich.py` — baseline (pre-F3, working tree at session start)

```
[PASS] CHK-0 sources: control_set.yaml v6.0: 63 controls (38 CR + 25 BPR)
[FAIL] CHK-1 frontmatter (8 fields): 9 DocNN docs checked; violations: ["Doc31_Process_Capability_Cards.md: missing ['case']"]
[PASS] CHK-2 FR census: unique FR ids=84, Doc29 metadata totalFRs=84, duplicated rows=none
[PASS] CHK-3 NFR census: unique NFR ids=56, Doc30 metadata totalNFRs=56
[FAIL] CHK-4 rule refs / dangling: distinct rule refs=65 across P3 docs; dangling (not in control_set 63)=['BPR-D-02.2-001', 'BPR-D-10.2-002']
[PASS] CHK-5 UC census: detailed U.C.* ids=37, packages=7 ['AI', 'DEV', 'DP', 'GOV', 'IAM', 'SEC', 'TRN'], catalog metadata claims 44 UCs (informational — mixed U.C.*/UC-* id spaces)
[FAIL] CHK-6 corr-008 cross-refs: FR 'Source Rule' malformed=['FR-76 -> BPR-D-10.2-002 (not in control_set)', 'FR-82 -> BPR-D-10.2-002 (not in control_set)']; gate->rule dangling=none; gate->FR dangling=none
[PASS] CHK-7 rule traceability coverage: rules referenced by >=1 P3 doc: 63/63; uncovered=none; FR-level Source Rule only covers 24 rules (see RICH_LINT_BASELINE.md finding F5-C2-01)
summary: 8 checks, 3 FAIL, 5 PASS
EXIT=1
```

Baseline re-proven from `git archive HEAD → /tmp/f3base` + run there: identical
(8 checks, 3 FAIL, 5 PASS) — the 3 FAILs are pre-existing, none introduced by the session.

### 6.2 `verify_rich.py` — post-F3

```
[PASS] CHK-0 sources: control_set.yaml v6.0: 63 controls (38 CR + 25 BPR)
[PASS] CHK-1 frontmatter (8 fields): 9 DocNN docs checked; violations: none
[PASS] CHK-2 FR census: unique FR ids=84, Doc29 metadata totalFRs=84, duplicated rows=none
[PASS] CHK-3 NFR census: unique NFR ids=56, Doc30 metadata totalNFRs=56
[FAIL] CHK-4 rule refs / dangling: distinct rule refs=65 across P3 docs; dangling (not in control_set 63)=['BPR-D-02.2-001', 'BPR-D-10.2-002']
[PASS] CHK-5 UC census: detailed U.C.* ids=42, packages=7 ['AI', 'DEV', 'DP', 'GOV', 'IAM', 'SEC', 'TRN'], catalog metadata claims 44 UCs (informational — mixed U.C.*/UC-* id spaces)
[FAIL] CHK-6 corr-008 cross-refs: FR 'Source Rule' malformed=['FR-76 -> BPR-D-10.2-002 (not in control_set)', 'FR-82 -> BPR-D-10.2-002 (not in control_set)']; gate->rule dangling=none; gate->FR dangling=none
[PASS] CHK-7 rule traceability coverage: rules referenced by >=1 P3 doc: 63/63; uncovered=none; FR-level Source Rule only covers 24 rules (see RICH_LINT_BASELINE.md finding F5-C2-01)
summary: 8 checks, 2 FAIL, 6 PASS
EXIT=1
```

**Delta:** CHK-1 FAIL → PASS (F3 fixed baseline finding F5-C2-04). CHK-4/CHK-6 unchanged —
the two dangling BPRs live in Doc28 (THR-DEV-01 row) and Doc29 (FR-76/FR-82), untouched by
F3; identical before/after. CHK-5 informational: "42 detailed U.C.* ids" = 37 real ids +
the 5 Formerly ids quoted in the §6.6 provenance note; "claims 44 UCs" is read from the
v1.0 **version-history row** (kept verbatim — history is not rewritten; the live §2
`totalUseCases` is now 36).

### 6.3 Other gates

| Gate | Baseline (pre-F3) | Post-F3 | Verdict |
|---|---|---|---|
| `02_PHASE2_RULES_RICH/validation/check_unmapped.py` | `GATE PASS (check_unmapped.py, Case_02 v0.4)`, EXIT=0 | identical, EXIT=0 | PASS, no regression |
| `python3 scripts/traceability_audit.py Case_02` (repo root) | ctrl→obj — (n/a) · 63/63 = 100.0% · uc→obj 81/81 = 100.0%, EXIT=0 | 63/63 = 100.0% · **86/86 = 100.0%** (co-occurrence set grew with the relocated narratives/index — zero dangling), EXIT=0 | PASS, no regression |
| `00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py` | `# all 16 dashboard(s) passed smoke`, EXIT=0 | identical, EXIT=0 | PASS, no regression (VISUALISATIONS untouched) |

### 6.4 Mermaid sanity

```
Doc21: mermaid=1 (useCaseDiagram §5.1 — kept in the catalog by campaign decision; UC ovals only, verified)
Doc31: mermaid=37 kinds={'flowchart': 27, 'graph': 10} (§5C.4 shape intact)
Annex A: mermaid=6 kinds={'useCaseDiagram': 6}; PROC/CAP inside blocks: NONE; orphan actors: NONE
Annex B: mermaid=21 kinds={'sequenceDiagram': 21}; pointers↔sections↔cards 1:1 PASS
MERMAID SANITY: PASS
```

---

## 7. Files changed (git numstat; no commits made)

| File | +N | −N |
|---|---|---|
| 03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md | 175 | 995 |
| 03_PHASE3_DECOMPOSITION/Doc31_Process_Capability_Cards.md | 392 | 43 |
| 03_PHASE3_DECOMPOSITION/annexes/B_Sequence_Diagrams.md | 30 | 91 |
| 03_PHASE3_DECOMPOSITION/annexes/A_Use_Case_Diagrams.md | 39 | 66 |

Total: +636 / −1195. All edits under `02_CASES/Case_02_SecureBorder_Solutions/` as scoped.
One instrument-owned file outside the case was overwritten by running the audit itself:
`00_METHODOLOGY/validation/TRACEABILITY_AUDIT_2026-09-05.md` (same behaviour as F1/F2).
Nothing under kg/, domains/, other cases, VISUALISATIONS; `validation/build_control_set.py`
untouched (still carries the human's pre-existing uncommitted v1.1 work in git status).

---

## 8. Residuals / known limitations

1. **Pre-existing gate FAILs (documented, human-decision items, untouched):** verify_rich
   CHK-4 (BPR-D-02.2-001 in Doc28, BPR-D-10.2-002 in Doc28/29 — not in control_set) and
   CHK-6 (FR-76/FR-82 Source Rule → BPR-D-10.2-002). Byte-identical to the HEAD baseline.
2. **Downstream narrative staleness (expected, F4/human):** Doc22 §2.1/§4 still frame lane
   cards under use-case-relationship headings; Doc23 variability rows for PROC-03/23/24/25/26;
   Doc27 references; phase `PROJECT_STATE.md` / `progress.json` count tables (F4 bookkeeping
   phase). Ids remain valid — no dangling references (swept).
3. **§10/§11 matrices keep their 32 lane rows each** (46→47 rows total incl. 15 U.C. rows):
   the UC↔BusinessGoal and UC↔Stakeholder mappings for lane ids exist **only** there —
   removing them would violate zero content loss; the ids stay live via Doc31. §13 rule
   coverage attributions to lane ids likewise kept (valid via Doc31), with a pointer note.
4. **CHK-5 informational quirks:** "claims 44 UCs" reads the verbatim v1.0 history row;
   "42 detailed U.C.* ids" includes the 5 Formerly ids in the §6.6 provenance note
   (Formerly provenance is kept corpus-wide, F1/F2 precedent).
5. **KG build E3 frozen** — no rebuild; graph nodes for the removed Doc21 stubs/rows point
   at content now in the §6.6/§7.0 registers and Doc31 (documented limitation, as in
   F1/F2). No id changed, so no rename sweep applied.
6. **Historical version-history rows kept verbatim** (v1.0 "44 UCs", v1.4 package ranges
   naming PROC-24/25 as UC ranges) — history is not rewritten.
7. **Doc31 "Piloted set: 4 of 37" phrase kept** (historical statement; Coverage section
   already states 37/37).

## 9. Escalations

None blocking. Judgement calls, all following F1/F2 precedent and documented above:
(a) §9's 5 PROC detailed cards re-laned to Doc31 (beyond the letter of "5 §6 stubs") —
required by the campaign end-state "Doc21 = 21 UCs, **0 PROC headings**" plus zero content
loss; (b) §7's 32 lane rows → verbatim §7.0 register (C1 §3.0 precedent); (c) annex B's 5
PROC sequence sections removed + B.1 placeholder/frontmatter hygiene (C3 F1 precedent;
§5C.5 lane-card diagram rule); (d) §12/§14 metrics recomputed (pre-existing internal
drift noted); (e) two borderline product titles flagged for the human (P7) — U.C.10.5.1,
U.C.11.5.1.
