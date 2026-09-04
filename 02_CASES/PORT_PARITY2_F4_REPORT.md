# PORT-PARITY-2 · Block F4 Report — Phase 2 content wave → Case_02 + Case_03

**Executor:** AEGIS Executor (campaign PORT-PARITY-2, block F4)
**Date:** 2026-09-04
**Base:** Case_01 Phase 2 content wave (2026-08-31, commit 7be0b3b) + F3b latent-fix list
**Git:** tree left dirty by design — NO commits made (orchestrator verifies and commits)

---

## 1. Deliverables per case

### Case_02_SecureBorder_Solutions (4 applicable regs: GDPR, CRA, NIS 2, AI Act)

| Artefact | Path (relative to `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/`) |
|---|---|
| Ontology v1.0 | `phase2_ontology.yaml` (phase1_reference → `../01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` v2.3) |
| Graph builder | `scripts/build_p2_graph.py` v1.0 |
| Validator | `scripts/build_p2_dashboard.py` v1.0 (7 checks, ported from Case_01) |
| Graph data | `data/phase2_graph.json` + `data/phase2_ontology.compact.json` v1.1 (emitted from the YAML) |
| P2 dashboard | `00_METHODOLOGY/00_VISUALISATIONS/Case_02/Case_02_P2_Dashboard.html` (286 KB) via `build_case02_p2_dashboard.py` (same dir) |
| control_set canonical | `control_set.yaml` at P2 ROOT (63 controls = 38 CR + 25 BPR); `validation/` copy = byte-identical mirror |

**Graph:** **278 nodes / 356 links / 4 audits.**
Nodes: CompanyContext 1, Obligation 38 (Doc14 §3.3 canonical tables), PrivacyOperationalObjective 34 + SecurityOperationalObjective 55 (Doc16 §3.1/§4.1 canonical rows — historic doc name `Doc16_Privacy_Security_Goals.md` kept), ComplianceRule 38 + BestPracticeRule 25 (control_set@kind), Tension 9 (Doc15 §4.1 + §4.2-4.4 cards, T-001..T-009, severities up to CRITICAL), NistSubcategory 78 (pattern-classified anchors).
Links: MAPS_TO 193, YIELDS 89 (Doc16 source-obligation columns), MITIGATES 64 (CR direct via `traceability`/`related_goals`; BPR derived transitively via `related_goals`→CR, flagged `derived:true`), GENERATES 10 (tension cards' obligation/sub-domain pairing). 0 dangling.

**Audits:** AUD-P2-004 — 14 PO without CR/BPR (medium); AUD-P2-005 — 40 SO without CR/BPR (medium); AUD-P2-006 — 2 CR without CSF/PF anchors (low); AUD-P2-007 — 17 anchor tokens in csf/pf/airmf fields matching no framework pattern (UNMAPPED_PF justifications, `CT.DM-P10`, comment-embedded ids) — quoted verbatim, not linked. **Orphan obligations: 0** — all 38 obligations are referenced by ≥1 CR in `control_set.yaml@traceability` (mechanically verified; the C1-style AUD-P2-005 obligation-orphan audit does not fire).

### Case_03_OmniBank_Financial (5 regs: + DORA)

| Artefact | Path (relative to `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/`) |
|---|---|
| Ontology v1.0 | `phase2_ontology.yaml` (phase1_reference → `../01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` v2.1-port) |
| Graph builder | `scripts/build_p2_graph.py` v1.0 |
| Validator | `scripts/build_p2_dashboard.py` v1.0 |
| Graph data | `data/phase2_graph.json` + `data/phase2_ontology.compact.json` v1.1 |
| P2 dashboard | `00_METHODOLOGY/00_VISUALISATIONS/Case_03/Case_03_P2_Dashboard.html` (285 KB) via `build_case03_p2_dashboard.py` |
| control_set canonical | `control_set.yaml` at P2 ROOT (78 controls = 38 CR + 40 BPR — the '**' assert); `validation/` copy = byte-identical mirror |

**Graph:** **242 nodes / 340 links / 6 audits.**
Nodes: CompanyContext 1, Obligation 38 (Doc15 canonical tables), Objectives 38 on the case's real **AG- id space** (Doc17 §3 privacy = 12 canonical rows; §4 security = 38 unique rows minus the 12 shared with §3 = 26; class assignment follows the catalog section, no renumbering), ComplianceRule 38 + BestPracticeRule 40 (NATIVE BPRs carry no objective links, by construction), Tension 5 (4 cards with their verbatim TENSION-{H,M,L}-NNN ids + T-005/TENSION-M-002 emitted from the §4.1 note; canonical set T-001..T-005 per the doc's own declaration, matching phase1@case_invariants.tensions=5), NistSubcategory 82 (tokens classified by their OWN pattern regardless of carrying field — recovers PF ids sitting in BPR csf fields).
Links: MAPS_TO 196, YIELDS 38 (Doc17 source-obligations columns), MITIGATES 99 (control_set@related_goals AG ids; AG ids with no Doc17 row withheld → AUD-P2-007), GENERATES 7. 0 dangling.

**Audits:** AUD-P2-005 — 10 security objectives without CR/BPR (medium); **AUD-P2-005b — 10 obligations without a CR addressing them via the AG chain (high)** — the real Case_03 orphan-obligation finding; AUD-P2-007 — 26 AG goal ids referenced by `related_goals` have no Doc17 objective row (medium; root cause of 005b); AUD-P2-008 — 18 non-conforming anchor tokens (low); AUD-P2-009 — dual tension id space provenance note (low); **AUD-P2-010 — mechanical canonical-count correction** (medium): Doc17 §3 lists 12 privacy rows vs its own summary claiming 11; §4 has 26 unique security AGs vs summary claiming 22; 26 AG ids appear twice in §4 tables (deduped, first occurrence wins). P2 PROJECT_STATE's `total_obligations: 38` matches the mechanical count in both cases (validator check 7 PASS).

## 2. control_set.yaml canonical-location decision

**Canonical = P2 ROOT** (matches Case_01). `validation/build_control_set.py` (both cases) now writes ROOT + a byte-identical `validation/control_set.yaml` mirror, so the repo-root posture gates and `check_unmapped.py` (which read `BUILD.parent/control_set.yaml`) keep passing **unchanged** (the root posture gate scripts were out of allowed touch-scope anyway). Regenerated both; diff root↔mirror = empty; counts re-verified (63 and 78). `check_unmapped.py` was NOT modified.

## 3. Back-port to Case_02 (3 latent F3b findings — direct HTML edit, template-script fixes survive `build_case02_dashboard.py` re-runs)

Applied to `00_METHODOLOGY/00_VISUALISATIONS/Case_02/Case_02_P1_Maturity.html`, porting Case_03's proven code:
1. **frameworkOf()** — broken `outcome.startsWith(("GV-","ID-",...))` (tuple arg = only first tested, and PF ids are dotted) → Case_03's AI-RMF regex + `/-P\d+$/` PF test; **csfFunction()** gained the `frameworkOf(outcome) !== "CSF"` guard.
2. **"N active active SDs" label** — `activeSDs + " active"` → `String(activeSDs)` (span label already reads "active SDs"); verified rendering "34 active SDs" (Case_02 is 34 active in the injected P1 graph v2.3 data — the count itself is data-driven and was already correct).
3. **Standalone radars never painted** — Case_03's resize-after-reveal block (`["mat-radar-csf","mat-radar-pf"].forEach(...)`) added after `#maturity-view` is unhidden; verified both radars now draw (screenshot).

`build_case02_dashboard.py` itself untouched; smoke re-run green.

## 4. Gates (all re-run after changes)

| Gate | Result |
|---|---|
| `Case_02/.../scripts/build_p2_graph.py --summary` | 278n/356l/4 audits, compact emitted |
| `Case_03/.../scripts/build_p2_graph.py --summary` | 242n/340l/6 audits, compact emitted |
| `Case_02/.../scripts/build_p2_dashboard.py --check --strict` | **exit 0 — PASS (7/7 checks)** |
| `Case_03/.../scripts/build_p2_dashboard.py --check --strict` | **exit 0 — PASS (7/7 checks)** |
| `test_dashboards.py` full smoke | **16/16 PASS** + identity purge OK |
| check_unmapped C1 / C2 / C3 | **3× exit 0 GATE PASS** (v0.3) |
| posture gate case02 / case03 (repo-root) | **2× exit 0 GATE PASS** |
| Identity grep (C2 + C3 P2 dashboards) | 0 leaks outside data blob (TinyTask/TINYTASK/Case 01/Case_01/Lisbon + sibling-case tokens, template AND blob); also applied in-suite via `IDENTITY_PURGE` |

## 5. Screenshots (Playwright, Chromium 1440×1000, all read back as images)

Case_02 `02_PHASE2_RULES_RICH/validation/snapshots/`: `p2_folio1_exec.png` (re-shot post-patch), `p2_folio8_posture_full.png`, `p2_folio8_radar_csf.png`, `p2_folio8_radar_pf.png`, `p2_folio3_rules.png`.
Case_03 `02_PHASE2_RULES_RICH/validation/snapshots/`: `p2_folio1_exec.png` (re-shot), `p2_folio8_posture_full.png`, `p2_folio8_radar_csf.png`, `p2_folio8_radar_pf.png`, `p2_folio5_tensions.png`.
Case_02 `01_PHASE1_CONTEXT_RICH/validation/snapshots/`: `p1_folio1_exec_f4.png`, `p1_maturity_full_f4.png`, `p1_maturity_radar_csf_f4.png`.
Case_03 `01_PHASE1_CONTEXT_RICH/validation/snapshots/`: `p1_folio1_exec_f4.png`, `p1_maturity_full_f4.png`.

**Visually confirmed:** C2 Folio I — masthead/seal 02/SecureBorder identity, strap "38 obligations, 89 objectives, 63 controls, 9 tensions, 0 orphan obligations", KPIs 38/89 (34 PO+55 SO)/63 (38 CR+25 BPR)/9, regs table GDPR/CRA/NIS2/AI Act, obligations-by-domain 4×7+3×2=38, donut + CSF bar drawn. C2 Folio VIII — posture pills 38/89/63/9/**0 ORPHANS**, tier-bar GV18/ID16/PR28/DE11/RS4/RC0, **both radars draw**, rules table 63 rows non-empty with anchors/statuses. C3 Folio I — seal 03/OmniBank/Frankfurt, 38/38 (12 PO+26 SO)/78 (38 CR+40 BPR)/5, 5 regs incl. DORA, "4/5 → 5/5 applicable" fix visible. C3 Folio VIII — pills with **10 ORPHANS**, "Doc15 · 10 orphans (AUD-P2-005b)", tier-bar GV7/ID11/PR19/DE4/RS3/RC1, radars draw. C3 Tensions folio — 5 rows with CRITICAL styling, T-005 note-derived title, footer "242 nodes · 340 links · 6 audits". C2 P1 Maturity — both radars painted (fix), "34 active SDs" label. C3 P1 dashboard renders (749n/2054l).

## 6. Scope notes

* Touched only: both cases' `02_PHASE2_RULES_RICH/**` (new root control_set, phase2_ontology.yaml, data/, scripts/, validation/build_control_set.py, validation/snapshots/), `00_VISUALISATIONS/Case_02/**`, `00_VISUALISATIONS/Case_03/**`, `00_VISUALISATIONS/tests/test_dashboards.py`. No DocNN deliverable content changed — builders PARSE the docs.
* `test_dashboards.py`: REQUIRED_DASHBOARDS now pins the two P2 dashboards; F3b purge check generalised to `IDENTITY_PURGE` (4 entries, back-compat alias kept); suite discovers **16**.
* Not touched (orchestrator's call): case/phase PROJECT_STATE.md and progress.json (their `total_obligations: 38` already matches; the Doc17-summary discrepancies live in graph audits AUD-P2-010, not doc edits).
