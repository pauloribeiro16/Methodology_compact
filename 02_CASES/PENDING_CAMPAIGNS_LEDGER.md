# Master Pending Campaigns Ledger — AEGIS

> **Purpose:** one durable file with EVERY unfinished campaign / parked fix-wave /
> deferred decision, so nothing is lost between sessions. The ALT-ANCHOR campaign has
> its own detailed execution plan: `00_METHODOLOGY/validation/ALT_ANCHOR_CAMPAIGN_PLAN.md`.
> **Update this ledger at every phase boundary or scope change.**
> Human (P7) decisions are FINAL — items marked **P7** wait for the human.

**Created:** 2026-09-05 · **Maintainer:** Orchestrator

---

## 1. IN EXECUTION — ALT-ANCHOR (2026-09-05)

Death of the `UNMAPPED_*` marker family → `ALT-ANCHOR (ref1; …)` / `ALT-ANCHOR (NO-ANALOGUE)`;
frozen referential set 800-53r5 · SSDF · OWASP ASVS · OWASP SAMM (+ISO 27002 last resort);
full 800-53r5 column on the 3 framework matrices via idempotent generator; orphans inventory.
**Decisions locked:** see plan file §1 (all FINAL).
**Progress:** Fase 0 in progress — C1 raw census extracted; C2/C3 census + element dedup pending.
**Detail:** `00_METHODOLOGY/validation/ALT_ANCHOR_CAMPAIGN_PLAN.md`.

## 1B. IN EXECUTION — UC SEPARATION (2026-09-05)

Human diagnosis: case use-case catalogs mix packages/UC/CAP/PROC (Doc22 §6 compliance
cards are control-register entries wearing UC ids, e.g. UC-58 "Maintains Immutable
Audit Logs"). Plan: catalogs hold UC cards only; 15 fake C3 UCs re-laned to PROC-41..52
/ CAP-08..10; PROC-39/40 re-adjudicated back to UC-66/92; UC-33/34 → PKG-DS
fully-dressed; all 3 cases; annex A diagrams = UC ovals only (rubric v1.8 §5B/§5C.5).
**Decisions locked:** `02_CASES/UC_SEPARATION_CAMPAIGN_2026-09-05.md` (all FINAL).
**Status: EXECUTED 2026-09-05** — F0 c266074 · F1 32f45f7 · F2 47ad056 · F3 d498347 · F4 bookkeeping. End state: 3 catalogs lane-pure (C3 33 UCs / C1 23+17 / C2 36), lane cards in Doc32/Doc31 (C3 50 PROC + 10 CAP), annexes A UC-ovals-only (11/6/8) + B (23/21/33); gates: only pre-existing FAILs remain (proven via HEAD-archive baselines); audit 100/100/100; dashboards 16/16. Residuals: 6 borderline UC titles → §5 P7 queue; Doc23/24-style relationship/variability docs still narrate re-laned cards under UC framing (future wave if wanted); C1 `progress.json` immutable-by-rule (untouched).
**Render fix 2026-09-05 (`f3c62b9`):** all diagram blocks render-validated — Mermaid has
no `useCaseDiagram` (#4628), so the 26 UC diagrams became **PlantUML + SVG hybrid**
(human decision; rubric v1.9 §5C.5) and sequence syntax was repaired (`;` separators,
`OFF` keyword). Mermaid check 192/192 OK · smoke 16/16 · audit 100/100/100.

## 1C. IN EXECUTION — RENUMBER (2026-09-05)

Human decision: lane ids grew large/gapped through the re-lanes (C3 UC jump 34→63, PROC
39/40 retired, C1/C2 legacy dotted `U.C.x.y.z`). Renumber every lane **flat 1..N per
case** — no gaps, no retired numbers, dotted flattened to UC-NN (C3: UC 33→01..93→33 +
PROC-41..52→39..50; C1 → UC-01..40; C2 → UC-01..36). Registry:
`00_METHODOLOGY/validation/RENUMBER_REGISTRY_2026-09-05.md`. Rubric v1.10 §5B rule 7.
**Decisions locked:** `02_CASES/RENUMBER_CAMPAIGN_2026-09-05.md` (all FINAL).
**Status: EXECUTED 2026-09-05** — F0 bbe7a02 · F1 18f326c · F2 3545c19 · F3 13945cf ·
F4 bookkeeping. End state: flat ids everywhere (C3 UC-01..33 / PROC-01..50 / CAP-01..10;
C1 UC-01..40; C2 UC-01..36); registry filled for all 3 cases; SVGs re-rendered; audit
100/100/100; mermaid 192/192; smoke 16/16; residual old ids = provenance/history only.
Known residual: 6 borderline UC titles (§5) unchanged — their ids are now the renumbered
ones (C1 UC-07/UC-12 etc.); re-adjudication would be a NEW renumber if ever ratified.

## 1D. IN EXECUTION — LEDGER-ZERO (2026-09-06) — phased closure of ALL open items

Human: "resolver isso tudo de forma faseada". Plan: `02_CASES/LEDGER_ZERO_CAMPAIGN_2026-09-06.md`.
**P7 decisions locked 2026-09-06:** (1) 6 borderline UC titles re-laned (C1 UC-07/12/13/16→PROC-18..21; C2 UC-30/36→CAP-11..12); (2) OBL-D-06.2-001 → Option A dual-duty documentado; (3) D-07.2 → Option B mitigação aceite; (4) phase2_ontology descongelada (enum + mirrors ×3); (5) MUC-C3-06 → decision gate em F2 (default: ratificar Doc22 §6B.7 como canónica).
**Phase map of absorbed items:** §2 mirrors/ontology → F7 · §2 CAP maturity bind → F4 · §3 P7 queue (MUC-C3-06) → F2 · §4 C2 handoff remainder → F5 · §5 orphans OBL/D-07.2 → F2 · §5 verify_rich FAILs → F1 · §5 borderline 6 → F3 · §5 P1 dashboard drifts → F6 · §6 KG reflection → F8.
**Progress:** F0 done (`d6c1333`) · F1 done (`4aecc0a`, verify_rich C2+C3 8/8) · F2 done 2026-09-06 (P7 ratifications paperwork: OBL Option A + D-07.2 Option B + MUC-C3-06 canonical + phantom-refs note ×3 RULE_FREEZE + §5 marks) — F3 next.

## 2. DEFERRED BY HUMAN DECISION (2026-09-05, documents-only scope) — Realization Class follow-ups

Committed as `2948fb8` (rubric v1.2 + C1 tag wave, T17/P23/C6, 9 secondaries). Deferred:
- [ ] **`phase2_ontology.yaml` application** (enum `RealizationClass` + attrs)
  - **C1**: untouched since `2948fb8`; freeze respected.
  - **C2**: `phase2_ontology.yaml` was **created** by `468c500` (PORT-PARITY-2 F4, 2026-09-04), BEFORE the Realization Class freeze. Unchanged since. Confirmed: **no `realization_class` / `RealizationClass` entry** in the file → freeze respected retroactively. See `PHASE2_ONTOLOGY_HISTORY.md` in C2 P2 root.
  - **C3**: same as C2, file created by `491cf74` (PORT-PARITY-2 F4). No `realization_class` entry. See `PHASE2_ONTOLOGY_HISTORY.md` in C3 P2 root.
  - Net: zero ontological regression. The freeze stands for all post-`2948fb8` work; reopening requires a new P7 decision.
- [x] Tag waves C2 (55 rules) and C3 (78 rules) — **DONE 2026-09-05** (commit `762c095`+`599a8ba`+`113ba05`): all 141 rules now carry `realization_class` derived from airmf/csf/pf/verification heuristic; audit 100/100/100
- [x] **Phase 3 LANE NAMING** (TRACEABILITY audit complete: `00_METHODOLOGY/validation/TRACEABILITY_AUDIT_2026-09-05.md` — 100/100/100 across 3 cases; instrument `scripts/traceability_audit.py` v0.1)
- [ ] — **DONE 2026-09-05**: `UC-*` reserved for TECHNOLOGY; 102 non-technology UCs re-laned to `PROC-NN` (82) / `CAP-NN` (18) across the 3 cases (C1 18 / C2 37 / C3 47); ~1.855 downstream references renamed single-pass (`scripts/rename_lane_ids.py` + registry `00_METHODOLOGY/validation/LANE_NAMING_CENSUS_v0.md`); 3 gates PASS; C1 xlsx regenerated; C1 Doc20 §6.1 freeze superseded (P7).
- [~] Phase 3 realization lanes + lane views of allocation — **CARDS 100% POPULATED 2026-09-05** (18/37/47 per case, each with Mermaid diagram §5C.4 + articulation table binding to catalogue and downstream docs; catalogue cross-refs added): card schemas published (rubric v1.4 §5C) + 4 lane cards per case (C1 Doc32: PROC-01/05/09 + CAP-01; C2 Doc31: PROC-05/14 + CAP-02/06; C3 Doc32: PROC-10/28 + CAP-02/04). Diagrams: §5C.4 flowcharts (per card) + §5C.5 UML use case diagrams (annex A: 25 — system-wide + per package, actors stick-figure) + sequence diagrams annex-only (annex B: 80 extracted from catalogs, cards keep 1-line pointer). Added 2026-09-05 (rubric v1.5 §5C.4 + v1.7 §5C.5): — PROC → flowchart TD (activities + decision branches), CAP → graph LR (span + realises); 12/12 inserted, structural validation clean. Remaining: populate the other ~80 PROC/CAP ids + bind CAP maturity to EvidenceItems.
- [ ] Dashboards + `data/` mirrors regeneration (`phase2_graph.json`, `phase2_ontology.compact.json`)
- [ ] KG reflection of `realization_class` (next KG rebuild)
- [x] Objectives (PO/SO) + obligations tagging — **DONE 2026-09-05** (commit `599a8ba`+`113ba05`): majority-vote `realization_class_derived` for 98 objs (C2 Doc16 70/124, C3 Doc15+17 28/135); 138 no-rule annotations recorded for honest downstream rework

## 3. Phase 3 product-first restructure — PARTIALLY DONE

Massification committed (f1a5049 + fda4cf5 + 433b1b2: C1 23 UCs, C2 26, C3 31, Bike4All template). Remaining:
- [x] OWASP risk Doc28/29 (threat×flow) — **DONE 2026-09-05** (Case_02 Doc28 §5 + Case_03 Doc29 §4: new `Threat × Flow matrix` anchored to OWASP ASVS v4.0.3 + OWASP SAMM v2; 10 rows each; 3 gates PASS unchanged)
- [x] Fase B FR/NFR in Volere format — **DONE 2026-09-05 (commit `0a0122b`)**: closed all 25 orphan FRs in Doc29 C2 (F5-C2-01 HIGH); 2 HARD cards (FR-66 multi-reg notification, FR-77 AI IR with ≤15 min) carry `// HARD: provisional threshold pending drill data` note (no invented numbers). Doc29 v1.1; gates PASS.
- [x] Bookkeeping of that campaign — **DONE 2026-09-05** (this commit)
- **P7 queue:** MUC-C3-06 (human decision), métricas §2/§14

## 4. PORT-PARITY-2 verification fix wave — PARKED

Independent verdict CLEAN-WITH-FINDINGS (`02_CASES/PORT_PARITY2_VERIFICATION_REPORT.md`); fix wave parked:
- [ ] MAJOR-1 — Doc31 false positive (validator logic, not content)
- [ ] MAJOR-3 — dangling links
- [ ] MAJOR-4 — 6th gate C1
- [ ] Case_02 handoff remainder (verify against post-PORT-PARITY-2 state before acting): Folio I title-case strings, stale re-inline Maturity.html, final screenshots

## 5. P7 human-review queue (accumulated)

- [ ] UC-lane borderline titles (UC SEPARATION 2026-09-05; ids valid — re-laning = future id rename if ratified): C1 U.C.2.4.2 DoS Resilience, U.C.3.2.1 Authorisation/Least Privilege, U.C.3.3.1 Secure System Defaults, U.C.4.4.1 Fail-Safe Design (lean PROC); C2 U.C.10.5.1 Offline/Failover Mode, U.C.11.5.1 Watchlist Cache Sync (lean CAP)

- [x] Orphan obligations — **DONE 2026-09-06 (LEDGER-ZERO F2, P7 decision 2, Option A)**: OBL-D-06.2-001 (C3 SBOM/PS.3 orphan) closed via dual-duty anchor `BPR-D-02.2-001`, documented in C3 Doc19 §7/§8 + Doc20 §1 (+ Doc15/Doc17 pointers); no new rule. Remaining C3 9 / C2 14 PO/40 SO orphan verdicts stay queued under ALT-ANCHOR Fase 4 (real GAPs return here).
- [x] verify_rich FAILs — **FULLY CLOSED 2026-09-05** (DERIVED-REFRESH + FR/NFR Phase B + F5 fixes 113ba05): F5-C2-01 (25 orphan FRs closed), F5-C2-03 (variants table suffix), F5-C2-02 (stale counts), F5-C3-01 (totals), F5-C3-02 (Doc31 56→12), F5-C3-03 (BPR-D-12.1-001), F5-C3-04 (UC-99→UC-25), F5-C3-06 (AI Act Art. 14→CR-D-08.2-001), F5-C2-04/C3-05 (`case:` frontmatter). All 10 known-pattern FAILs closed.
- [x] D-07.2 coverage decision — **DONE 2026-09-06 (LEDGER-ZERO F2, P7 decision 3, Option B)**: 4 orphan obligations C1 (OBL-D-07.2/07.3/07.4-001, OBL-D-10.1-001) formally closed via BPR-anchored closure through `BPR-D-07.2-001` (ASVS V3 CI/CD anchor); N/A marker withdrawn; Doc14/Doc18/Doc23/Doc27 + PROJECT_STATE audit row updated (AUD-P2-005 RESOLVED). No new rules.
- [x] Phantom refs left untouched — **DONE 2026-09-06 (LEDGER-ZERO F2, briefing Item 4, ratified)**: all phantom reference lineages (F-01/F-03 PO-D-01.3-001/PG-D-01.3-001; the 2 PORT-PARITY-2 cross-case citations; C1 historical cleanup nodes) ratified as intentional/documented — see `00_METHODOLOGY/validation/P7_BRIEFING_PACK_2026-09-05.md` Item 4. Consolidated note added to RULE_FREEZE.md ×3. No further action.
- [ ] P1 dashboard: 4 upstream drifts (KG-vs-view) + 2 cosmetic items
- [x] Folio IV MATURITY column "—" debt — **DONE in `2f29a7d`** (gridMaturityClass retired; evidence_ids badge in EV column)
- [x] Case_01 `NIST_ANCHORS.md` goals_anchored — **DONE in ALT-ANCHOR C3 write-back** (now 28/31, residual 3 deferred)

## 5B. PORT-PARITY-2 fix wave (residual from `02_CASES/PORT_PARITY2_VERIFICATION_REPORT.md`)

- [x] **MAJOR-1** (Doc31 NFR false positive) — **closed by rebuttal**: validator `parse_cards` id-collision artifact, not a content defect (see verification report §74). No fix needed.
- [x] **MAJOR-3** (C1 Doc19 stale references to `02b_Proportionality_Profile.md` / `04b_Security_Posture.md`) — **DONE 2026-09-05** (this commit): legacy names rewritten to point at `CONTROLS/NIST_PF/` and `Doc11 fields`; prose waiver added.
- [x] **MAJOR-4** (C1 gate `/maturi/` false positive on Doc05/Doc12 metadata) — **DONE 2026-09-05** (this commit): gate waiver for `maturity_cur`/`maturity_tgt`/`MATURITY_MODEL_*` metadata identifiers (regex refined).

## 6. On-demand / dormant (no action unless asked)

- P1 dashboard expansion Fases C–E (RACI done; B done; C–E on demand)
- P1 ontology Document-class (v1.5+)
- Andar-1 orchestration results consolidation (4-model comparison, 2026-09-01)
- Dream nightly consolidation (cron active; propose-only)

---

**Rule:** before starting any new campaign, check this ledger for collisions
(especially §2 — ontologies/dashboards stay frozen until the human reopens them).
