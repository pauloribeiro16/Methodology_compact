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

## 2. DEFERRED BY HUMAN DECISION (2026-09-05, documents-only scope) — Realization Class follow-ups

Committed as `2948fb8` (rubric v1.2 + C1 tag wave, T17/P23/C6, 9 secondaries). Deferred:
- [ ] **`phase2_ontology.yaml` application** (enum `RealizationClass` + attrs)
  - **C1**: untouched since `2948fb8`; freeze respected.
  - **C2**: `phase2_ontology.yaml` was **created** by `468c500` (PORT-PARITY-2 F4, 2026-09-04), BEFORE the Realization Class freeze. Unchanged since. Confirmed: **no `realization_class` / `RealizationClass` entry** in the file → freeze respected retroactively. See `PHASE2_ONTOLOGY_HISTORY.md` in C2 P2 root.
  - **C3**: same as C2, file created by `491cf74` (PORT-PARITY-2 F4). No `realization_class` entry. See `PHASE2_ONTOLOGY_HISTORY.md` in C3 P2 root.
  - Net: zero ontological regression. The freeze stands for all post-`2948fb8` work; reopening requires a new P7 decision.
- [ ] Tag waves C2 (55 rules) and C3 (78 rules)
- [x] **Phase 3 LANE NAMING** — **DONE 2026-09-05**: `UC-*` reserved for TECHNOLOGY; 102 non-technology UCs re-laned to `PROC-NN` (82) / `CAP-NN` (18) across the 3 cases (C1 18 / C2 37 / C3 47); ~1.855 downstream references renamed single-pass (`scripts/rename_lane_ids.py` + registry `00_METHODOLOGY/validation/LANE_NAMING_CENSUS_v0.md`); 3 gates PASS; C1 xlsx regenerated; C1 Doc20 §6.1 freeze superseded (P7).
- [~] Phase 3 realization lanes + lane views of allocation — **CARDS 100% POPULATED 2026-09-05** (18/37/47 per case, each with Mermaid diagram §5C.4 + articulation table binding to catalogue and downstream docs; catalogue cross-refs added): card schemas published (rubric v1.4 §5C) + 4 lane cards per case (C1 Doc32: PROC-01/05/09 + CAP-01; C2 Doc31: PROC-05/14 + CAP-02/06; C3 Doc32: PROC-10/28 + CAP-02/04). Diagrams added 2026-09-05 (rubric v1.5 §5C.4): one Mermaid diagram per card — PROC → flowchart TD (activities + decision branches), CAP → graph LR (span + realises); 12/12 inserted, structural validation clean. Remaining: populate the other ~80 PROC/CAP ids + bind CAP maturity to EvidenceItems.
- [ ] Dashboards + `data/` mirrors regeneration (`phase2_graph.json`, `phase2_ontology.compact.json`)
- [ ] KG reflection of `realization_class` (next KG rebuild)
- [ ] Objectives (PO/SO) + obligations tagging (pilot was RULEs-only)

## 3. Phase 3 product-first restructure — PARTIALLY DONE

Massification committed (f1a5049 + fda4cf5 + 433b1b2: C1 23 UCs, C2 26, C3 31, Bike4All template). Remaining:
- [x] OWASP risk Doc28/29 (threat×flow) — **DONE 2026-09-05** (Case_02 Doc28 §5 + Case_03 Doc29 §4: new `Threat × Flow matrix` anchored to OWASP ASVS v4.0.3 + OWASP SAMM v2; 10 rows each; 3 gates PASS unchanged)
- [ ] Fase B FR/NFR in Volere format (user rule: light table + testable Fit Criterion, anchored to Source UC, mapped to NIST+CR/BPR; homes = existing requirements/DocNN; pilot 1 package/case; 25 orphan FRs C2)
- [x] Bookkeeping of that campaign — **DONE 2026-09-05** (this commit)
- **P7 queue:** MUC-C3-06 (human decision), métricas §2/§14

## 4. PORT-PARITY-2 verification fix wave — PARKED

Independent verdict CLEAN-WITH-FINDINGS (`02_CASES/PORT_PARITY2_VERIFICATION_REPORT.md`); fix wave parked:
- [ ] MAJOR-1 — Doc31 false positive (validator logic, not content)
- [ ] MAJOR-3 — dangling links
- [ ] MAJOR-4 — 6th gate C1
- [ ] Case_02 handoff remainder (verify against post-PORT-PARITY-2 state before acting): Folio I title-case strings, stale re-inline Maturity.html, final screenshots

## 5. P7 human-review queue (accumulated)

- [ ] Orphan obligations: C3 10 · C2 14 PO/40 SO — being resolved by ALT-ANCHOR Fase 4 (verdicts LEGIT/MITIGADO/GAP; real GAPs return here)
- [ ] verify_rich FAILs: C2 2 FAIL/6 PASS · C3 3 FAIL/5 PASS (honest baselines, findings queued)
- [ ] D-07.2 coverage decision (4 orphan obligations C1, mitigated by BPR-D-07.2-001 N/A marker)
- [ ] Phantom refs left untouched (PORT-PARITY-2 deliberate)
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
