---
document_id: AEGIS-CAMPAIGN-UC-SEPARATION-F1-REPORT
title: UC SEPARATION — F1 Report (Case_03)
phase: 3
version: 1.0
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: GENERATED
case: Case_03_OmniBank_Financial
---

# UC SEPARATION — F1 Report (Case_03, 2026-09-05)

Executor report for Phase F1 of the UC SEPARATION campaign
(`02_CASES/UC_SEPARATION_CAMPAIGN_2026-09-05.md`). Scope: Case_03 use-case catalog becomes
lane-pure (UC cards only), all content preserved. Rubric basis:
`00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` v1.8 — §5B rule 6 (lane-pure catalogs), §5C.1
(PROC card schema), §5C.2 (CAP card schema), §5C.4 (lane card diagrams), §5C.5 (UML annex
conventions).

**Bottom line:** all target end-state counts reached; all runnable gates PASS or match the
pre-existing honest baseline; `traceability_audit.py` 100/100/100; dashboard smoke 16/16;
no content loss; no escalations.

---

## 1. P5 impact (KG) + census

### 1.1 `kg.sh impact` (KG build E3 — frozen, documented limitation)

| ID | Result |
|---|---|
| UC-58 | 4 impacted nodes at depth 2, all `[references]`: FR-37 (requirements/23_Functional_Requirements.md), NODE-CS-002 (14_Architectural_Nodes.md), NODE-CS-003 (14_Architectural_Nodes.md), GATE-D-05-03 (16_Compliance_Gates_Report.md) |
| UC-08 | No unique node match (build E3 predates the id) |
| UC-26 | No unique node match |
| PROC-39 | No unique node match |
| PROC-40 | No unique node match |

No >50-node impacts; no escalation required (P5). The 3 files referenced by UC-58's node are
all inside the rename scope and were renamed in the same pass.

### 1.2 Census (grep, word-boundary) — before → after

Files scanned: whole `02_CASES/Case_03_OmniBank_Financial/` + `00_METHODOLOGY/00_VISUALISATIONS/`.
**00_VISUALISATIONS had 0 hits for all 17 ids** → VISUALISATIONS untouched (dashboard smoke still
run: 16/16 PASS).

Live-reference counts per id (line-based, `grep -c` before; word-boundary occurrences after):

| Old id | Files before | Occurrences renamed | After (live refs) | After (provenance-only hits) |
|---|---|---|---|---|
| UC-02 | 10 | 18 | 0 | 2 (Doc32 provenance + articulation) |
| UC-03 | 8 | 12 | 0 | 2 |
| UC-06 | 10 | 20 | 0 | 2 |
| UC-15 | 5 | 5 | 0 | 2 |
| UC-17 | 11 | 27 | 0 | 2 |
| UC-21 | 7 | 19 | 0 | 2 |
| UC-22 | 9 | 15 | 0 | 2 |
| UC-44 | 9 | 23 | 0 | 2 |
| UC-46 | 9 | 17 | 0 | 2 |
| UC-47 | 6 | 7 | 0 | 2 |
| UC-57 | 9 | 19 | 0 | 2 |
| UC-61 | 11 | 23 | 0 | 2 |
| UC-08 | 10 | 20 | 0 | 2 |
| UC-26 | 7 | 11 | 0 | 2 |
| UC-58 | 11 | 31 | 0 | 2 |
| PROC-39 | 6 | 43 | 0 | 6 (Doc22 v3.0 row + lane-naming section, Doc32 coverage, annex A/B notes) |
| PROC-40 | 6 | 19 | 0 | 6 |

Full per-file before-counts: `/tmp/ucsep/census_before.txt` (session scratch; reproduced in the
campaign ledger discussion if needed). The rename pass applied **329 replacements across 13
files** (single pass, one mapping table, word-boundary regex `(?<![A-Za-z0-9._\-])ID(?![A-Za-z0-9_\-])`
— identical mechanism to `scripts/rename_lane_ids.py` v1.0, executed from a session copy with the
UC SEPARATION mapping since repo `scripts/` is outside the F1 edit scope).

Dotted/hyphenated derivative handling:

- Dotted sub-ids (UC-08.1→CAP-08.1, UC-17.1→PROC-45.1, UC-21.1→PROC-46.1, UC-44.1→PROC-48.1,
  UC-57.1→PROC-51.1, UC-61.1→PROC-52.1) renamed by the same pass (the prior campaign's regex
  treats "." as non-boundary; empirically identical to the LANE NAMING behaviour — PROC-11.1/29.1
  exist from UC-18.1/43.1).
- Hyphenated regulation-variants (UC-02-GDPR→PROC-41-GDPR, UC-58-Cloud→CAP-10-Cloud,
  UC-58-OnPrem→CAP-10-OnPrem, UC-17-DORA→PROC-45-DORA, UC-17-AI→PROC-45-AI,
  UC-44-NIS2→PROC-48-NIS2, UC-44-CRA→PROC-48-CRA) — renamed in a follow-up exact pass.
  **Deliberate extension beyond the LANE NAMING precedent** (that campaign left UC-25-NIS etc.
  unrenamed): F1's no-dangling criterion requires zero stale references. 12 variant replacements.
- Shorthand artifact fixed: annex A `UC-02/03` → `PROC-41/42` (bare "03" would have dangled).

Post-sweep: **55 remaining textual hits for the 17 old ids — all inside explicit
formerly/provenance/version-history notes** (Doc32 card provenance lines + articulation
"Formerly" column; Doc22 card provenance lines + v3.0 version row + Lane Naming section;
annex A/B header notes). Zero live references.

---

## 2. Doc22 v2.3 → v3.0 (`03_PHASE3_DECOMPOSITION/Doc22_Use_Cases_Catalog.md`)

1. **§6 summary stubs deleted**: 38 PROC-01..38 + 7 CAP-01..07 + 15 renamed stubs
   (PROC-41..52/CAP-08..10) + the UC-33/34 stubs (elevated). All 45 non-UC stubs' content is
   preserved: field-by-field derivation into Doc32 full cards (§3 below) + the §3 index.
2. **New §3 "Compliance Domain Index (PKG-D-01..D-10)"** with:
   - §3.1 Domain overview — Purpose / Primary Actors / Business Goals / Primary Regulations /
     lane-card count / priority distribution per domain (all taken verbatim from the former
     package headers and the former §5 PACKAGES table);
   - §3.2 Realisation index — per domain: Realised by (Doc32 lane cards in order), UCs in this
     catalog (PKG-D-05 → "UC-33, UC-34 (PKG-DS, §4.8)"), Rules covered (the exact CR/BPR ids the
     former package cards held, verbatim);
   - pointer line "Full process/capability cards: Doc32_Process_Capability_Cards.md".
3. **§4 (formerly §6B) product use cases** kept verbatim except: heading renumbered
   6B.0..6B.7 → 4.1..4.9 (alias "formerly §6B" in the §4 heading); provenance line added under
   UC-66 and UC-92 ("Re-adjudicated from PROC-39/40 to the UC lane per rubric v1.8 §5B rule 6
   (human decision 2026-09-05)"); package tables carry UC-66/UC-92 rows (via rename).
4. **New §4.8 PKG-DS — Privacy & Data-subject UCs (2)**: UC-33 "Data Protection Officer Executes
   Data Erasure Request" and UC-34 "Data Subject Requests Data Export" elevated to fully-dressed
   form (sections 1–10, same template as UC-63). Derived ONLY from the old stubs + their rules
   (Doc19 CR-D-05.3-001/BPR-D-05.3-001, CR-D-05.4-001/BPR-D-05.4-001) + sanctioned GDPR articles:
   Art. 17(1) erasure, Art. 17(2) propagation to copies/replications/backups + third-party
   information, Art. 15(3) copy, Art. 20 portability. Alternative flows with triggers: identity
   verification failure, legal-hold/retention conflict (UC-33), third-party data exclusion,
   items outside portability scope (UC-34). SLA numbers only where attested (30 days / 72h /
   60-day third-party verification per rule; otherwise "per rule"). NIST anchors per
   Doc20/NIST_ANCHORS (PR.DS-10; ALT-ANCHOR for CR-D-05.4-001; Privacy FW CT.DM-Px). No new ids
   invented; stub titles kept verbatim (note: the task brief's shorthand "DPO Executes..." was
   not adopted — the stub title is the source of truth).
5. **Top pointer block** after the title: annexes/A_Use_Case_Diagrams.md + annexes/B_Sequence_Diagrams.md.
6. **Section renumbering**: 1, 2, 3 (3.1, 3.2), 4 (4.1–4.9), 5 (5.1–5.3), 6 (6.1), 7, 8, 9, 10 +
   trailing Lane Naming / Lane Cards cross-reference. Stale child numbers (3.1/4.x/5.x/6.x) fixed.
   Cross-references updated in Doc22, Doc23 (2), Doc24 (5), annex A (3).
7. **Metadata/metrics**: frontmatter v3.0, outputs → Doc23/24/25/26/32; §2 totalUseCases 33
   (31 product + 2 PKG-DS), totalPackages 7, complianceDomains 10 (indexed, not UC packages),
   relationships/variability rows → Doc23/Doc24; §5.1 priority 17/11/5 = 33; §5.2 per-package
   distribution = 33 (PKG-C 6, PKG-A 6, PKG-B 6, PKG-D 5, PKG-E 4, PKG-F 4, PKG-DS 2);
   §5.3 rules matrix rebuilt from stub ground truth (distinct CR/BPR per domain + "Realised by");
   §6.1 UC counts recomputed over the 33 catalog UCs (GDPR 25, CRA 29, NIS 2 31, DORA 31,
   AI Act 31) with a method note; version history v3.0 row added.
8. **Trailing sections**: Lane Naming gains the v2.3→v3.0 re-lane paragraph (full mapping list);
   Lane Cards cross-reference now states 50 PROC + 10 CAP in Doc32 and UC-only catalog.
9. **Annex B pointers regenerated 1:1**: 33 `> **Sequence diagram:** → Annex B §N` lines,
   verified programmatically against the 33 annex sections (UC-33→§1 … UC-93→§33).

**Integrity note (fixed during verification):** a cell-edit initially fused the §3.1 PKG-D-05 and
PKG-D-06 rows (dropped newline); detected in the verification pass and repaired; row census and
`||` sweep confirm clean.

---

## 3. Doc32 v1.0 → v1.1 (`03_PHASE3_DECOMPOSITION/Doc32_Process_Capability_Cards.md`)

1. **+15 full cards**: PROC-41..52 (12, SSDF-style §5C.1: Trigger, Activities numbered, Roles,
   SLA/Timing, Realises with /AG-D goals, Anchors, Evidence) and CAP-08..10 (3, C2M2/ArchiMate
   §5C.2: Owner, Span, Maturity, Realises, Anchors, Evidence). Content derived faithfully from
   the former Doc22 stubs (Description → Activities/Span; Actors → Roles/Owner; Rules → Realises;
   SLA verbatim; Related Goals → Realises "/AG-D…"; Tension Resolution woven into Evidence/Span
   per house style — e.g. CAP-10 "Resolves T-002"). No thresholds/dates invented. Each card
   carries `> Formerly UC-NN — re-laned per rubric v1.8 §5B rule 6 (UC SEPARATION, 2026-09-05).`
   plus a `Priority` row (verbatim from the stub — deliberate 1-row extension of the schema to
   honour zero content loss; the stub is the only source of per-card priority).
2. **Maturity**: CAP-08..10 copy the CAP-01..07 row verbatim ("PLANNED (1) — Scale A posture
   model v1.6; current/target pending P1 Folio VIII refresh + EvidenceItem bind"). No values invented.
3. **Diagrams (§5C.4)**: 12 × `flowchart TD` (trigger → numbered activity nodes, role shifts as
   edge labels, description-derived decision branches, SLA on terminal node) + 3 × `graph LR`
   (CAP node left, span contributors right, Realises link as labelled edge) — 15 new diagrams,
   all structurally sane (balanced fences, quoted labels, known keywords).
4. **−2 companion cards**: PROC-39 and PROC-40 blocks (post-rename headings UC-66/UC-92) deleted
   with their 2 flowcharts — they return to Doc22 as fully-dressed UC-66/UC-92.
5. **Articulation table**: 2 stale rows removed; 15 rows added anchored to "Doc22 §3.2 (PKG-D-xx)"
   with live downstream ref counts computed post-restructure (e.g. PROC-41: 21, CAP-10: 36);
   intro note updated for the two registries (LANE NAMING + UC SEPARATION).
6. **Coverage**: "60/60 cards present (50 PROC + 10 CAP; 4 pilot + 43 LANE NAMING + 15 UC
   SEPARATION − 2 re-adjudicated to UC-66/UC-92)" + 15 new title lines, 2 removed.
7. **Frontmatter/header**: v1.1, updated 2026-09-05, header note rewritten (set composition +
   PROC-39/40 removal rationale); `case:` field added to Doc32 frontmatter (corr-008 8-field
   completeness — the only remaining CHK-1 violation, on a doc this campaign edits; verify_rich
   CHK-1 now fully PASS).

---

## 4. Annexes

### 4.1 Annex A (`annexes/A_Use_Case_Diagrams.md`, v1.0 → v1.1)

- §1 system-wide extended: package "PKG-DS — Privacy & Data-subject UCs" with UC-33/UC-34 ovals
  + actors Data Protection Officer / Data Subject.
- New §8 "PKG-DS: Privacy & Data-subject UCs (UC-33, UC-34)" useCaseDiagram (DPO/Data Subject →
  2 ovals; no same-package includes — documented rationale).
- §4/§7: oval aliases PROC39/PROC40 → UC66/UC92; §4 title tidied; notes updated to the
  re-adjudication wording; header note now cites Doc22 §4 (formerly §6B) and states the
  UC-ovals-only rule (§5C.5).
- **Verification**: 8 `useCaseDiagram` blocks; ZERO `PROC-`/`CAP-` occurrences inside any block
  (UC ovals only).

### 4.2 Annex B (`annexes/B_Sequence_Diagrams.md`, rebuilt as v2.0)

- Rebuilt **ordered by id** (rubric §5C.5): §1 UC-33, §2 UC-34, §3 UC-63 … §33 UC-93, with
  UC-66 (ex-PROC-39, old §4) and UC-92 (ex-PROC-40, old §30) restored in place.
- 2 NEW sequenceDiagrams for UC-33/UC-34 (lifelines consistent with the new cards' basic flows:
  Data Subject / DPO / OmniBank platform / IT Operations / Third parties; Art. 17(1)-(2),
  CR/BPR-05.3 and Art. 15(3)/Art. 20, CR/BPR-05.4 references).
- Empty "B.1 Critical Path Sequences" placeholder deleted; frontmatter added (was missing);
  header Status PLACEHOLDER → ACTIVE with a v2.0 change note.
- **Verification**: 33 `sequenceDiagram` blocks; headings §1..§33 strictly ordered by id;
  33/33 Doc22 pointer lines match their sections.

---

## 5. Verification results (verbatim)

### 5.1 Counts

| Check | Target | Actual | Verdict |
|---|---|---|---|
| Doc22 `^## UC-` / `^## PROC-` / `^## CAP-` headings | 0/0/0 | 0/0/0 | PASS |
| Doc22 `#### Use-Case: {UC-` cards | 33 | 33 | PASS |
| Doc22 Annex B pointer lines | 33 (1:1) | 33, all aligned | PASS |
| Doc32 PROC full cards | 50 | 50 | PASS |
| Doc32 CAP full cards | 10 | 10 | PASS |
| Doc32 mermaid diagrams | 60 | 60 (50 flowchart TD + 10 graph LR) | PASS |
| Annex A useCaseDiagram blocks | 8 | 8 | PASS |
| Annex B sequenceDiagram blocks | 33 | 33 | PASS |
| Annex A PROC-/CAP- inside useCase blocks | 0 | 0 | PASS |
| Dangling old-id references (17 ids + dotted/hyphen variants) | 0 live | 0 live (55 provenance-only) | PASS |
| PKG-DS fully-dressed cards | 2 (10 sections each) | UC-33: 10, UC-34: 10 | PASS |

### 5.2 `verify_rich.py` (03_PHASE3_DECOMPOSITION/scripts) — exit 1

```
[PASS] CHK-0 sources: control_set.yaml v2.0: 78 controls (38 CR + 40 BPR incl. 4 D-12.x AI-specific)
[PASS] CHK-1 frontmatter (8 fields): 9 DocNN docs checked; violations: none
[PASS] CHK-2 FR census: FR cards=72, Doc30 summary 'Total FRs'=72
[FAIL] CHK-3 NFR census: NFR cards=12, Doc31 summary 'Total NFRs'=56
[PASS] CHK-4 rule refs / dangling: distinct rule refs=78; dangling (not in control_set 78)=none
[PASS] CHK-5 UC census: UC cards=0; catalog claim=33 (informational)
[FAIL] CHK-6 corr-008 cross-refs: FR/NFR/UC Source Rule unresolved=["NFR-06 -> 'AI Act Art. 14'",
       "NFR-06 -> 'Art. 28'", "NFR-06 -> 'Art. 73'", "NFR-07 -> 'GDPR Art. 35'",
       "NFR-09 -> 'AI Act Art. 14'"]; gate Rules Verified unresolved=none
[PASS] CHK-7 rule traceability coverage: rules referenced by >=1 P3 doc: 78/78; uncovered=none;
       FR-level Source Rule covers 49 rules
summary: 8 checks, 2 FAIL, 6 PASS
```

The 2 FAILs are the baseline's pre-existing human-decision findings (RICH_LINT_BASELINE §4:
F5-C3-02, F5-C3-06) — unchanged by F1, not fixed per campaign discipline. Improvements vs the
pre-F1 state: CHK-1 now fully PASS (Doc32 `case:` field completed); CHK-5 catalog claim now
reads the correct 33.

### 5.3 Other gates

```
check_unmapped.py            → GATE PASS (check_unmapped.py, Case_03 v0.4)  EXIT=0
check_implementation_posture_case03.py → GATE PASS (check_implementation_posture.py, Case_03 v0.3) EXIT=0
build_control_set.py         → EXIT=0 (ran; NOT modified; regenerated control_set.yaml identical — no diff)
```

### 5.4 `traceability_audit.py all` (report written by the instrument to
`00_METHODOLOGY/validation/TRACEABILITY_AUDIT_2026-09-05.md`)

```
| Case   | obj→ctrl          | ctrl→obj          | uc→obj_or_ctrl    |
| Case_01| 104/104 = 100.0%  | 46/46 = 100.0%    | 102/102 = 100.0%  |
| Case_02| —                 | 63/63 = 100.0%    | 81/81 = 100.0%    |
| Case_03| 42/42 = 100.0%    | 78/78 = 100.0%    | 111/111 = 100.0%  |
```

Case_03: 100/100/100 — no change vs target (the co-occurrence model keeps every id linked; the
§3 index preserves all rule/goal mentions in Doc22).

### 5.5 Dashboard smoke (`test_dashboards.py`)

```
# all 16 dashboard(s) passed smoke   (EXIT=0; VISUALISATIONS untouched by F1)
```

### 5.6 Mermaid sanity

```
Doc22: mermaid=0 (diagrams are annex-only per §5C.5)
Doc32: mermaid=60, kinds={'flowchart': 50, 'graph': 10}, issues=none
Annex A: mermaid=8, kinds={'useCaseDiagram': 8}, issues=none
Annex B: mermaid=33, kinds={'sequenceDiagram': 33}, issues=none
MERMAID SANITY: PASS
```

---

## 6. Files changed (13; git numstat)

| File | +N | −N |
|---|---|---|
| 03_PHASE3_DECOMPOSITION/Doc22_Use_Cases_Catalog.md | 482 | 1091 |
| 03_PHASE3_DECOMPOSITION/Doc32_Process_Capability_Cards.md | 392 | 41 |
| 03_PHASE3_DECOMPOSITION/annexes/B_Sequence_Diagrams.md | 108 | 43 |
| 03_PHASE3_DECOMPOSITION/annexes/A_Use_Case_Diagrams.md | 49 | 16 |
| 03_PHASE3_DECOMPOSITION/requirements/Doc30_Functional_Requirements.md | 33 | 33 |
| 03_PHASE3_DECOMPOSITION/Doc23_Use_Case_Relationships.md | 30 | 30 |
| 03_PHASE3_DECOMPOSITION/Doc24_Use_Case_Variability.md | 18 | 18 |
| 03_PHASE3_DECOMPOSITION/Doc29_Risk_Analysis.md | 27 | 27 |
| 03_PHASE3_DECOMPOSITION/Doc25_Architectural_Nodes.md | 13 | 13 |
| 03_PHASE3_DECOMPOSITION/requirements/Doc31_Non_Functional_Requirements.md | 20 | 20 |
| 03_PHASE3_DECOMPOSITION/Doc28_Functional_Tree.md | 11 | 11 |
| 03_PHASE3_DECOMPOSITION/Doc27_Compliance_Gates_Report.md | 10 | 10 |
| 03_PHASE3_DECOMPOSITION/Doc26_Requirements_Allocation.md | 9 | 9 |

Total: 1201 insertions / 1362 deletions at report time (Doc22/Doc32/annex counts include the
post-verification cell fixes). Doc22: 4816 → 4209 lines. All changes under
`02_CASES/Case_03_OmniBank_Financial/`; nothing under kg/, VISUALISATIONS/, domains/, other
cases; `validation/build_control_set.py` untouched; no commits made (Orchestrator commits).

---

## 7. Residuals / known limitations

1. **Downstream narrative staleness (expected, F2-F4 / human):** Doc23/Doc24 still describe the
   re-laned cards under use-case-relationship/variability headings (now pointing at PROC-*/CAP-*
   ids); Doc28 line ~441 still claims "38 PROC + 7 CAP + 17 UC … = 93 total use cases, matching
   Doc22 v2.3" — stale after v3.0 (33 UCs; compliance corpus in Doc32). Doc25/26/27/29/30/31
   carry the renamed ids but their section framing is unchanged. Renames and §6B→§4 pointer
   fixes were applied everywhere; re-wording of downstream narrative was NOT in F1 scope.
2. **Pre-existing gate FAILs (documented, human-decision items):** verify_rich CHK-3 (Doc31
   "Total NFRs 56" vs 12 cards — F5-C3-02) and CHK-6 (NFR raw-article citations — F5-C3-06).
3. **KG build E3 frozen:** `kg.sh impact` returned "no unique node match" for UC-08/UC-26/
   PROC-39/PROC-40 (build predates the ids); UC-58's 4 impacted files were renamed in-pass. No
   KG rebuild was performed (campaign constraint).
4. **Historical version-history rows kept verbatim** (Doc22 v1.0 "62 UCs", Doc24 §6B mention) —
   history is not rewritten.
5. **UC-66 self-reference quirk:** Doc22 UC-66 §10 retains the pre-existing phrase
   "UC-66-audit chain" (a LANE NAMING-era artifact that was not renamed then because of the
   trailing hyphen; after re-adjudication it is semantically correct again). Left verbatim.
6. **Deliberate small deviations, documented:** (a) `Priority` row added to the 15 new Doc32
   cards (zero content loss; schema is otherwise §5C.1/§5C.2-exact); (b) hyphen-variant renames
   beyond the LANE NAMING precedent (no-dangling criterion); (c) Doc32 `case:` frontmatter field
   added (corr-008; CHK-1 now clean); (d) annex B gained an 8-field frontmatter it previously
   lacked; (e) PKG-DS card titles use the stub titles verbatim.
7. **Session-scratch tooling:** the rename/restructure scripts ran from `/tmp/ucsep/` (copies of
   `scripts/rename_lane_ids.py` mechanics) because repo `scripts/` is outside the F1 edit scope.
   The mapping table is recorded in §1.2 above and in the Doc22 Lane Naming section; if the
   Orchestrator wants it versioned, `scripts/lane_mappings/Case_03_UC_SEPARATION.json` is the
   natural home (P7 — human call, since scripts/ is outside F1 scope).

## 8. Escalations

None. No irreconcilable conflicts encountered; no content invented; no >50-node KG impacts.
