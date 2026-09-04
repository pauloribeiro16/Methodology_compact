# PORT-PARITY-2 · Block F3b — Case_03 Phase 1 Dashboards Report

> **Campaign:** PORT-PARITY-2, block F3b
> **Task:** build the Case_03 P1 Dashboard (Folios I–VIII) + standalone P1 Maturity page from the verified F3a graph data
> **Executor:** Executor agent · **Date:** 2026-09-04
> **Method (REGRA DE OURO):** started from `00_METHODOLOGY/00_VISUALISATIONS/Case_02/Case_02_P1_Dashboard.html` + `Case_02_P1_Maturity.html` (read-only templates); every number derived programmatically from `data/phase1_graph.json` (749 nodes / 2054 links / 9 audits); the JSON blob is inlined verbatim in BOTH shapes (`<script type="application/json" id="phase1-graph-data">` + `window.PHASE1_GRAPH_DATA = {...}`). No data edited.
> **Result:** ALL GATES PASS (exit 0). Working tree left uncommitted for orchestrator verification.

---

## 1. Files created/changed

| File | Action |
|---|---|
| `00_METHODOLOGY/00_VISUALISATIONS/Case_03/build_case03_dashboard.py` | **created** — inliner/patcher modelled on `Case_02/build_case02_dashboard.py`. Every patch is asserted (expected-occurrence count or the build fails). Reads Case_02 templates, strips their Case_02 JSON blobs, applies identity+data patches, inlines the Case_03 graph, writes both Case_03 HTML files. Idempotent (regenerates from templates). |
| `00_METHODOLOGY/00_VISUALISATIONS/Case_03/Case_03_P1_Dashboard.html` | **created** (2.1 MB incl. inlined graph, both shapes) |
| `00_METHODOLOGY/00_VISUALISATIONS/Case_03/Case_03_P1_Maturity.html` | **created** (standalone Folio VIII, 2 radars CSF⬡ + PF⬠; AI-RMF = anchors in Scale A table with `Framework=AI`, no third radar — locked decision honoured) |
| `00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py` | **extended** — `REQUIRED_DASHBOARDS` explicit entries for both Case_03 files (fail-fast if missing; on full-suite runs they must be in the rglob discovery set) + `check_case03_identity_purge()` static check (Case_02 identity tokens outside the inlined JSON blob = build failure). Default suite now runs 14 dashboards (12 prior + 2 new). |
| `02_CASES/.../validation/snapshots/*.png` | **created** (gitignored by repo policy, `.gitignore:10` — visual evidence kept local) |

## 2. Numbers injected (all derived from `phase1_graph.json` at build time)

| Where | Value | Derivation |
|---|---|---|
| Header strap / footer | 749 nodes · 2054 links · 9 audits · 1490 ambiguity cards · generated 2026-09-04 · schema `phase1_graph.json v2.1-port` | `len(nodes/links/audits)`, `ambiguity.stats_total.cards_in_scope`, `meta.generated`, `meta.schema_version` |
| Masthead | "Case 03 · Phase 1", seal 03, sub "OmniBank Financial Systems S.A. · Germany (EU)" | company_context node label + attrs.hq |
| Folio I Company card | LARGE scale · 5,000+ employees · >€1.5B revenue · MAXIMUM complexity; HQ Germany (EU); Banking and Financial Services (ECB-supervised); mobile app + web platform + OmniScore; hybrid stack | company_context attrs (`scale/employees/revenue_eur/hq/sector/stack`) + Doc03 §2; "MAXIMUM" from Doc13 §2 (complexity tier) |
| Folio I Applicability | **5 / 5**, all YES — GDPR controller+processor (PII incl. biometric); CRA manufacturer (app+web); NIS2 essential entity (Annex I banking, 5,000+); DORA financial entity (credit institution Art. 2(1)); AI Act provider+deployer (Annex III credit scoring) | Regulation node attrs (`applicable`, `obligated_party`, `reason`) — DORA YES is the headline inversion vs Case_02 |
| Folio I Coverage Tier (label retargeted Doc12 §4 → **Doc13 §4**) | 38 active w/ tier; **RIGOROUS 31 / STANDARD 7** | SD attrs `proportionality_tier`, `active` |
| Folio I Coverage Level (label retargeted Doc11 §3 → **Doc12 §3**) | 38 scored; **SUBSTANTIVE 27 / PARTIAL 11 / NOT_ADDRESSED 0** | SD attrs `coverage_level` (⚠ brief said 38/0 — real graph is 27/11/0, see §5) |
| Folio I Adjusted Goals | **76** across 2 tracks (Doc14 §2); Privacy 38 (AG-D-XX.Y-001) / Security 38 (-002); tensions **4 of 5** resolved as clause-pair edges; priority **56 CRITICAL · 18 HIGH · 2 MEDIUM** | AG attrs `track`, `implementation_priority`; `HAS_TENSION_WITH` link count; Tension node count |
| Folio I Ambiguity | **1490** cards; S1 0 / S2 0 / S3 0; "Top-20 by regulation: GDPR 5 · CRA 4 · NIS2 4 · DORA 4 · AI Act 3" | `ambiguity.stats_total.by_severity` + `by_regulation` |
| Folio I Caveats prose | describes the 9 real audits: NEW-C03-01..06 (5 structural + 1 blocking-ambiguity: 119 EV seed, 76 AGs, 1490-card scope, 121 NIST anchors 79 CSF+38 PF+4 AI-RMF, 31/7 split, DORA axis 38 clauses + 4/5 tensions) + CFL-C03-001, BLN-C03-001, CVG-C03-001 (D-07.2 coverage withheld, 37/38) | audits[] |
| Folio III header | "9 findings" | `len(audits)` |
| Folio IV | footnote → Doc13 §4 (38 proportionality rows) + Doc12 §3; "no DEFERRED rows — 31 RIGOROUS / 7 STANDARD"; I/P tooltips → Doc13 §4; risk cell **prose-safe** (Case_03 `risk_if_not_met` is free prose, not HIGH/MEDIUM enums → truncated 34 chars + full text as tooltip; enum path kept) | SD attrs |
| Folio V legend | Stakeholders **15** · Business Goals **0** · Company 1 · Regulations 5 · Clauses **150** · Sub-Domains 38 · Adjusted Goals **76** | node-type counts (Case_03 has **no BusinessGoal nodes** and no DEFINES/COVERS edges — data-honest 0, see §5) |
| Folio VI | "65 activities · 15 roles"; Active only (65) | RaciActivity/RaciRole counts; **roles fully data-driven** (thead + ROLES/ROLE_HEADERS/COL_INDEX built from graph RaciRole nodes — Case_03's 15 roles incl. CRO/DORA-Risk/Fraud, no hardcoded list) |
| Folio VII | 25 systems / 12 stores / 25 flows / **33 vendors**; flow map edges from real rels (**FLOWS_BETWEEN**, HOSTS; removed the Case_02-fabricated FLOW→STORE triples); PDC layer from **CAPTURES**; coverage-map counts **derived from EvidenceItem `sources[]`** (Case_03 has no INVOLVES/INVOLVES_STORE/INVOLVES_FLOW rels) | node counts + links |
| Folio VIII (dashboard) | KPIs **119 EVI / 37 Coverage / 82 Capability / 82 Gaps (observed=False) / 37 observed**; CSF fn-bar GV 17 · ID 4 · PR 5 · DE 11 · RS 1 (=38) | EvidenceItem attrs; CITES_OUTCOME |
| Both, maturity classification | **Case_03 NIST outcome syntax**: CSF dotted w/o `-P` suffix (GV.RM-04), PF dotted WITH `-P<lvl>` (GV.RM-P1), AI-RMF dashed (MANAGE-2.1). Case_02's dash-prefix PF map matches nothing and its dot-prefix `csfFunction` swallows PF outcomes into the CSF radar → reclassified via `isPfOutcome` (/-P\d$/) + `isAirmfOutcome`; PF radar axes = dotted prefixes | EvidenceItem outcomes + NistControl `framework` attrs (CITES_OUTCOME cross-check: 38 CSF / 38 PF / 6 AI) |
| PF-anchor column (Scale B, both files) | Case_02's hardcoded 19-entry PF_ANCHORS table → **data-derived** per-sub-domain PF capability outcome | PF capability EvidenceItems (38/38) |
| Maturity page | CASE 03 tag; h1 "OmniBank Financial Systems S.A. · Phase 1 — Maturity Folio"; sub "...GERMANY (EU)... v2.1-port maturity_model"; strap; AI-RMF callout rewritten (6 anchors, outcome MANAGE-2.1, D-02.1/D-07.1/D-07.2/D-07.3/D-09.2/D-10.1, provider+deployer); disclaimer id-family extended with DORA-C* (Case_02 vendor names removed); `DATA_PATH_C02`→`DATA_PATH_C03` + Case_03 fetch path | audits + Doc08 Q39/Q73 |

## 3. Gate outputs (2026-09-04)

```
=== GATE 1: test_dashboards.py --only "Case_03_P1_Dashboard" ===
✓ | Case 03 · Phase 1 — Knowledge & Aud | CANV 0 | SVG 0 | ROWS 0 | ERR 0 | CDN 0
# all 1 dashboard(s) passed smoke        EXIT=0   (0 pageerrors; Folio I is tab-gated canvas-free,
                                                   same profile as Case_02's P1 dashboard)

=== GATE 2: test_dashboards.py --only "Case_03_P1_Maturity" ===
✓ | Case 03 · Phase 1 — Maturity (CSF 2 | CANV 2 | ROWS 238 | ERR 0 | CDN 0
# all 1 dashboard(s) passed smoke        EXIT=0   (2 radar canvases = CSF + PF, no third radar)

=== GATE 3: full suite ===
# smoke for 14 dashboard(s)  →  # all 14 dashboard(s) passed smoke   EXIT=0
(12 prior + Case_03_P1_Dashboard + Case_03_P1_Maturity; identity purge line: OK)

=== GATE 4: grep proof ===
$ grep -c "SecureBorder\|SECUREBORDER\|Case 02\|Case_02" Case_03_P1_Dashboard.html
2            ← both lines are the two single-line inlined JSON blobs (each contains 2 hits)
$ grep -o ... | sort | uniq -c →  4 Case_02
Identity check OUTSIDE the JSON blobs (template + JS only): 0 hits for SecureBorder /
SECUREBORDER / Case 02 / Case_02 / The Hague / GuardianGate / TinyTask / B.V. / 450,
in BOTH Case_03 files. Same result asserted on every suite run via
check_case03_identity_purge().
```

The 4 in-blob occurrences are **verbatim F3a audit prose**, not identity leaks:
- `NEW-C03-04.detail`: "…Case_03's primary NIST source is Doc14 §5, unlike Case_02's…" (REG_CHAIN comparison)
- `BLN-C03-001.detail`: "…matches Case_01/Case_02 structure." (macro-domain baseline)
Both render in Folio III as data. Editing them would hand-modify the committed data layer (violates REGRA DE OURO); the brief's premise "the graph legitimately contains none of those" is inaccurate for these two audit strings. **Orchestrator: please ratify as accepted in-blob provenance references, or commission an F3a data-layer edit.**

## 4. Screenshots (all in `02_CASES/.../validation/snapshots/`, gitignored dir) — visually verified

| File | Visual confirmation |
|---|---|
| `folio_1_exec.png` | Masthead Case 03 + OmniBank; KPI tiles non-empty (5/5 all-YES card, 38/38 tier + 27/11/0 cov bars, 76 AGs, 1490 ambiguity w/ Top-20 by-reg line); 5 audit-kind badges (5 STR/1 BAM/1 CFL/1 BLN/1 CVG); 46 invariant rows; 9-audit caveat prose |
| `folio_2_graph.png` (+`_detail_folio2_graph.png`) | Force graph drawn (sub-domain hubs D-01.1…D-10.3 + clause/evidence satellites, edges visible); toolbar with RIGOROUS/STANDARD tier filter; 431 nodes / 443 links visible; inspector panel present |
| `folio_3_audits.png` | All 9 audits rendered grouped into existing kinds only (STR 5, CVG, BAM, CFL, BLN); audit cards carry Case_03 titles/severities; "9 FINDINGS" header |
| `folio_4_grid.png` | 38 rows · 19 columns DataTables (page 1 of 3); Privacy/Security goal-id chips; tier/coverage colour classes; risk prose truncated w/ tooltip; BUILD_REQUIRED+MUST / INHERITABLE+MUST I/P pills; NIST count + shield; "Ambig in scope" now numeric **"94 / 94"** (after fix); D-07.2 row shows "—" reg-cov (CVG-C03-001 case) |
| `folio_5_story.png` | Pipeline drawn: 15 stakeholders, OmniBank node, 5 regs, 150-clause wall, MAPS_TO/YIELDS/BELONGS_TO edges, 4 tension dashes, 12 GAP diamonds; ambiguity bars numeric ("D-04.3 (94)", "D-09.4 (106)"); legend 15/0/1/5/150/38/76; 297 nodes · 282 edges · 4 tensions · 4 gaps |
| `folio_6_raci.png` | **20 columns = 5 fixed + 15 data-derived roles (CEO, CTO, CRO, CISO, DPO, AI-Gov, Comp, IA, SOC, Legal, HR, Proc, DORA-Risk, Fraud, Board)**; 65 rows; "65 of 65 activities shown"; colour-coded R/A/C/I badges incl. composite A/R; honest empty state "No GAP-RACI audits in this dataset." |
| `folio_7_arch.png` | Flow map drawn (25 SYS → 12 STORE → 25 FLOW columns + edges, DSC/PDC nodes right); vendor risk register with 33 real Case_03 vendors (AWS, Azure, Salesforce, …, Schneider Electric); pills 25/12/25/33; sub-domain × touch-points bar chart **non-empty** (EV-sources derivation works) |
| `folio_8_maturity.png` (+`_detail_folio8_radar_csf/pf.png`, `_detail_folio8_fnbar.png`) | KPIs 119/37/82/82; fn-bar GV 17 · ID 4 · PR 5 · DE 11 · RS 1; **CSF radar polygon present** (GV 17 / DE 11 spikes); **PF radar polygon present** (CT/CM/GV weighted — would have been flat-at-origin with the Case_02 prefix map); capability table shows Framework=AI rows; Scale A/B tables + citation audit render, **0 unresolved sources** |
| `folio_viii_maturity.png` (+`_detail_mat_radar_csf/pf.png`, `_detail_mat_fullpage.png`) | Standalone page: CASE 03 + OmniBank h1; pills 119/37/82/37/82; fn-bar total 38; **both radars render full-size polygons** (after fix, canvas 770×340); AI-RMF callout (6× MANAGE-2.1, no third radar); 37 coverage rows / 82 capability rows / 0 src-bad; no pageerrors |

JS probes during shooting: **0 console errors, 0 page errors on both pages** across all tab activations.

## 5. Divergences from the block brief (reasoned, per P0)

1. **Coverage counts**: brief said "38 SUBSTANTIVE / 0 NOT_ADDRESSED"; the graph says **27 SUBSTANTIVE / 11 PARTIAL / 0 NOT_ADDRESSED** (`attrs.coverage_level`). Graph wins (REGRA DE OURO; the numbers are also re-derived at runtime by `buildExec()`).
2. **BusinessGoal = 0**: Case_03 has no BusinessGoal nodes and no DEFINES/COVERS edges, so the Folio V legend shows "Business Goals 0" and the STK/REG columns have fewer edges. Data-honest; pipeline still renders 282 edges.
3. **`risk_if_not_met` is prose** (38 distinct free-text values), not Case_02's HIGH/MEDIUM enums → risk cell renders truncated prose + tooltip instead of a colour pill (enum path preserved).
4. **In-blob "Case_02" ×2** (gate 4): verbatim F3a audit prose, ratified-or-edit decision requested (§3).
5. **Template fixes made for Case_03 (worth back-porting to Case_02 later — NOT done here, out of scope):**
   a. Standalone maturity radars initialise while `#maturity-view` is `display:none` → 0-width canvas, **radars never paint** (verified on Case_02: canvas `[0, 340]`). Case_03 now calls `chart.resize()` after reveal (canvas `[770, 340]`, polygons visible).
   b. "38 active active SDs" duplicated label in the Coverage KPI sub → now "38".
   c. Case_02's `frameworkOf()` has a latent JS bug (`outcome.startsWith(("GV-",…))` — comma expression → only tests "CT-"); superseded by Case_03's regex-based classification.
6. **Ambiguity `in_scope` shape**: Case_03 uses boolean `in_scope` + `total` (Case_02: numeric count) → normalised in GRID so Folio II/V bars and Folio IV column show the in-scope count ("94 / 94"), not "true".
7. Footer "See validation/…" pointer now targets `PORT_PARITY2_F3B_REPORT.md` (this file) instead of Case_02's `P1_graph_json_validation.md`.
8. Task brief's "audits (8 → 9)" and "footer 521·1205·8 → 749·2054·9" applied as stated; "tier counts 31 RIGOROUS / 7 STANDARD per Doc13 §4" confirmed against graph attrs; "AdjustedGoal 70 → 76: 38 Privacy / 38 Security" confirmed; "ambiguity 1071 → real count" = **1490**; "Folios V legend 5 regs/111 clauses/70 AGs → 5/150/76" applied.

## 6. Orchestrator decisions requested

1. Ratify the 2 in-blob audit-prose "Case_02" references (§3/§5.4) — accept as provenance, or commission an F3a text edit + graph rebuild.
2. Note Case_02 dashboard latent bugs (§5.5a/b/c) — recommend a small follow-up block to back-port the three fixes to the Case_02 templates.
3. Coverage prose in brief (38/0) vs graph (27/11/0) — confirm the graph reading stands (recommended; it matches Doc12 §3-derived attrs and audit NEW-C03-05).
