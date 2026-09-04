# PORT-PARITY-2 — Campaign Report

**Executed:** 2026-09-04 (single-session, orchestrator + 3 verified Executor subagents)
**Scope:** full structural + content propagation of Case_01 waves to Case_02/Case_03 (Phases 1–3, dashboards, scripts, gates)
**Result:** ✅ COMPLETE — 16 commits, all 5 case gates PASS, smoke 16/16, P3 verify_rich honest FAILs queued for human review

---

## 1. What was propagated

| Block | Case_02 | Case_03 |
|---|---|---|
| Baseline (uncommitted Sprint 10/11 work gated + committed) | ✅ 49aa5e4 (link count 505→1205 corrected) | n/a |
| F1 source fixes (Case_01: Folio IV "Maturity EV", NEW-08 v1.6, prose) | ✅ inherits (2f29a7d) | ✅ inherits |
| corr-013 P2 renumber | **not needed** (already Doc14–Doc20) | ✅ Doc16–21 → Doc15–20, 206 refs (6e29834) |
| P1 v1.6 data layer (ontology maturity_model, graph, builder, validator v2.4) | ✅ (was already at parity) | ✅ 749n/2054l/9 audits, 119 EvidenceItems (75bd626) |
| P1 dashboards Folios I–VIII + standalone Maturity | ✅ (parity, 2026-08-31) | ✅ + build_case03_dashboard.py (549d1de) |
| P2 wave (phase2_ontology, build_p2_*, graph, dashboard, control_set at root) | ✅ 278n/356l (468c500) | ✅ 242n/340l (491cf74) |
| P3 rich layer v0 (scripts, 4 narrative docs GENERATED + banner, RICH_LINT, functional tree, TRACEABILITY_AUDIT for C2) | ✅ (e73dfed) | ✅ (637ccc5) |
| Bookkeeping (progress.json, case PS, CHANGE_LOG 6.8, GLOBAL 6.8) | ✅ | ✅ |

**Known deviations (locked with user before execution):** AI-RMF = anchors without radar (all cases); EvidenceItems mechanical + audit flags; P3 docs GENERATED v0 with "pending human review" banner; corr-013 executed; fix-at-source first.

## 2. Verification performed (orchestrator, independent of subagents)

- All 5 gates re-run after every block: `check_unmapped` ×3 + `check_implementation_posture` ×2 — **ALL PASS**.
- Smoke suite full run: **16/16 dashboards** (14 prior + Case_03 P1 ×2, then +P2 ×2).
- Graph JSON deep-checks: 0 dangling links, 0 forbidden maturity scalars on sub-domains, 38/38 active sub-domains with evidence (C3), invariants = counts.
- Screenshots read back as images (force graph, Folio VIII radars CSF+PF on P1+P2, identity strings).
- Diff-scope audit after each subagent: only the allowed paths touched.

## 3. 🔴 Human review queue (P7) — decide these

1. **Case_03 orphan obligations (AUD-P2-005b): 10 obligations unreachable via the AG chain** (root cause AUD-P2-007: 26 `related_goals` AG ids with no Doc17 row). Fix = content edit in Doc17/Doc15 — needs your adjudication (add rows vs. accept gap).
2. **Case_02 objective-coverage orphans: 14 PO / 40 SO without objective link** (audited, not fixed). Catalog-level rule coverage is 63/63.
3. **verify_rich FAILs (honest, not suppressed):**
   - C2: 25/84 FRs carry Source Rule "—"; only 10/63 rules traced at requirement level; stale "53 rules" claims; duplicated FR-71/72 rows.
   - C3: Doc31 claims 56 NFRs but defines 12 cards (**suspected truncation** — check git history of Doc31); 5 FRs cite raw articles instead of rule ids; Doc26 stale "63 rules" vs frozen 78; BPR-D-12.1-001 unallocated; dangling UC-99.
4. **D-07.2 (Case_03) coverage**: no clause anchor → Coverage EvidenceItem withheld + CVG-C03-001 audit. Decide: clause anchor vs. Sub-SO-only coverage.
5. **F3a minor adjudications accepted by orchestrator** (veto if wrong): T-005 no HAS_TENSION_WITH edge (single-clause tension); capability `observed=false` everywhere (Doc13 §4 = PARTIAL; consistent with port Fase 4 backfill); 3 id-style warnings (STK-/ROLE-/ThirdParty hyphen styles — same family Case_02 already warns).
6. **Phantom refs left untouched** (pre-existing, not made worse): C3 `Doc20_NIST_Framework_Inputs` (2 hits — doc doesn't exist in C3); C1 Doc05 legacy basename refs already fixed this campaign.
7. **corr-013b (registered debt):** C3 P3 renumber Doc22–31 → Doc21–30 — recommend it rides the future P3 RICH campaign, not overnight work.
8. **Naming parity (optional):** C2 Doc16 is `Privacy_Security_Goals` vs C1/C3 `Objectives`. Renaming is a corr-010-class change — deferred.

## 4. Registered debt / nits (non-blocking)

- C3 `phase1_ontology.compact.json` has `schema_version: null` (content complete; validator passes — cosmetic).
- C3 P2 after corr-013 ends at Doc20 while P3 starts at Doc22 (Doc21 gap) — accepted cosmetic until corr-013b.
- Historical reports (PORT_census_v0, VALIDATOR_UNMAPPED_AUDIT_v0, SPRINT*) intentionally keep old doc numbers — point-in-time records.
- KG E3 `graph.json` predates all renames — rebuild is a main-repo activity (per protocol).
- Gate waiver lists were extended with provenance tokens (`model_csf_strict`, `maturity_cur/tgt`, `maturity redesign`, `P1_Maturity.html`) — the /maturi/ ban now correctly allows rule-defining and provenance text; strictness otherwise unchanged.

## 5. Commit index

| Commit | Block |
|---|---|
| 49aa5e4 | F0 Case_02 P1 parity baseline |
| 7be0b3b | F0 Case_01 P2 wave baseline |
| 5888cf7 / 3eddf3c / de6928e | F0 dream / harness / UNIFIED |
| 2f29a7d | F1 source fixes Case_01+02 |
| 6e29834 / bf811e2 | F2 corr-013 C3 / gate waiver harmonisation |
| 75bd626 | F3a C3 P1 data layer |
| 549d1de | F3b C3 P1 dashboards |
| 468c500 / 491cf74 | F4 P2 wave C2 / C3 |
| e73dfed / 637ccc5 | F5 P3 rich v0 C2 / C3 |
| (this commit) | F6 bookkeeping + report |
