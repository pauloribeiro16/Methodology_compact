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
- [ ] `phase2_ontology.yaml` application (enum RealizationClass + attrs) — ⚠ human reversed an agent re-restoration 2×; ontologies OFF-limits until reopened
- [ ] Tag waves C2 (55 rules) and C3 (78 rules)
- [ ] Phase 3 realization lanes + lane views of allocation (process models, capability cards anchored to maturity model v1.6)
- [ ] Dashboards + `data/` mirrors regeneration (`phase2_graph.json`, `phase2_ontology.compact.json`)
- [ ] KG reflection of `realization_class` (next KG rebuild)
- [ ] Objectives (PO/SO) + obligations tagging (pilot was RULEs-only)

## 3. Phase 3 product-first restructure — PARTIALLY DONE

Massification committed (f1a5049 + fda4cf5 + 433b1b2: C1 23 UCs, C2 26, C3 31, Bike4All template). Remaining:
- [ ] OWASP risk Doc28/29 (threat×flow) — C2/C3
- [ ] Fase B FR/NFR in Volere format (user rule: light table + testable Fit Criterion, anchored to Source UC, mapped to NIST+CR/BPR; homes = existing requirements/DocNN; pilot 1 package/case; 25 orphan FRs C2)
- [ ] Bookkeeping of that campaign
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
- [ ] Folio IV MATURITY column "—" debt (gridMaturityClass deferred case)
- [ ] Case_01 UNMAPPED leftovers (folded into ALT-ANCHOR where markers; still open): `NIST_ANCHORS.md` goals_anchored 27/31 under-count, Doc18:3104

## 6. On-demand / dormant (no action unless asked)

- P1 dashboard expansion Fases C–E (RACI done; B done; C–E on demand)
- P1 ontology Document-class (v1.5+)
- Andar-1 orchestration results consolidation (4-model comparison, 2026-09-01)
- Dream nightly consolidation (cron active; propose-only)

---

**Rule:** before starting any new campaign, check this ledger for collisions
(especially §2 — ontologies/dashboards stay frozen until the human reopens them).
