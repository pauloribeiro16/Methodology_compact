# Central Change Log — AEGIS Methodology Implementation

**Last Updated:** 2026-09-05
**Version:** 7.0 (ALT-ANCHOR — UNMAPPED_* retired in 3 cases; 5 frozen referentials + generator + 3 gates v0.4 PASS; REALIZATION-CLASS — Case_01 P2 realization_class tag wave documents-only; PORT-PARITY-2 — cross-case content parity: corr-013 C3 renumber, C3 P1 v1.6 layer 749n/2054l, P2 waves C2+C3, P3 rich v0 C2+C3, dashboards 16/16 smoke)
**Scope:** All Cases

---

## 0.6 2026-09-05 — ALT-ANCHOR (death of UNMAPPED + multi-referential anchoring)

| Item | Value |
|------|-------|
| Methodology | `00_METHODOLOGY/ALT_ANCHOR_CRITERION.md` v1.0 — `realization_class` extension: `ALT-ANCHOR (ref1; …)` / `ALT-ANCHOR (NO-ANALOGUE)` replaces the retired `UNMAPPED_*` marker family; frozen referentials 800-53r5/SSDF/ASVS/SAMM/ISO27002; class hierarchy anchoring (TECHNOLOGY/PROCESS/CAPABILITY) registered |
| Frozen sources | `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/{NIST_80053R5(719+2legacy)/NIST_SSDF(21p/47t)/OWASP_ASVS(14ch/71sec)/OWASP_SAMM(5/15/30)/NIST_CSF_2.0(106)}` + manifests citing official NIST/OWASP sources |
| Generator | `scripts/build_alt_anchor_columns.py` — injects `800-53r5` column from PF JSON crosswalks into the three matrices; idempotent (re-run = zero diff); single-writer anti-drift |
| Case write-back | C1 48, C2 62, C3 107 UNMAPPED occurrences → ALT-ANCHOR (all 3 cases P2 + C2/C3 NIST_ANCHORS P3) |
| Gates | `check_unmapped.py` v0.4 in all three cases — RETIRED-token hard check + ALT-ANCHOR anchor validation + CSF 2.0 hard check (was WARN-only in C2/C3). All three PASS. CSF 1.1 remnant waivers documented for the families retired in 2.0 (PR.IP, PR.PT, PR.AC, ID.SC, PR.AT-03/04, RS.CO-04, PR.DS-12) |
| Orphans inventory | C3 10 OBL orphans → 9 MITIGADO (BPR sibling) + 1 GAP (`OBL-D-06.2-001`) → P7 queue. C2 14 PO/40 SO → LEGIT (audit dedup improvement deferred) |
| Deferred | CSF 1.1→2.0 normalisation, C2 audit dedup, ontologies, dashboards, data mirrors, KG reflection |

---

## 0.5 2026-09-05 — REALIZATION-CLASS (Case_01 Phase 2 tag wave, documents-only)

| Item | Value |
|------|-------|
| Methodology | `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` v1.2 — new mandatory Phase 2 rule attribute `realization_class` {TECHNOLOGY, PROCESS, CAPABILITY} (+ optional secondary); normative decision tree (constitutive-step test, P/C structural indicators); ISO 27002:2022 indicative crosswalk; CAPABILITY anchored to maturity model v1.6 (Scale A / EvidenceItem); corr-008 registered in `00_METHODOLOGY/AGENTS.md` v2.2 |
| Validator | Rubric APPROVED_WITH_AMENDMENTS (A1–A7 applied, A8 deferred); blind 46-rule classification baseline; tag-wave audit 41/46 primary agreement → 2 adjudicated fixes |
| Case_01 P2 | Doc18: card fields 25/26 ×46, Anexo A column, Anexo D derived view, counters 24→26, v4.1; `control_set.yaml` 46 keys; `12_Rules_Catalog.xlsx` cols R/S; `validation/build_control_set.py` v1.1 emits fields (regeneration-stable) |
| Distribution | TECHNOLOGY 17 / PROCESS 23 / CAPABILITY 6; secondaries 9 (8→TECHNOLOGY, CR-D-09.2-001→PROCESS) |
| Gates | check_unmapped GATE PASS unchanged (52 UNMAPPED_PF); ID census 46/46 identical in all three locations; 3-way class agreement 46/46 |
| Deferred (P7 human decisions) | `phase2_ontology.yaml` application, dashboards/data mirrors regeneration, KG reflection, C2 (55) / C3 (78) waves, Phase 3 lanes |

---

## 0.4 2026-09-04 — PORT-PARITY-2 (cross-case content propagation Case_01 → Case_02/03)

| Item | Value |
|------|-------|
| Baseline | 5 commits gating+committing the uncommitted Sprint 10/11 parity work (incl. link count fix 505→1205) |
| Source fix (Case_01) | Folio IV "Maturity EV" column (v1.6 evidence_ids badge; gridMaturityClass retired); NEW-08 audit rewritten as evidence-coverage; Folio I prose 31 audits; JSON re-inlined |
| corr-013 (Case_03 only) | P2 renumber Doc16–21 → Doc15–20 (206 refs, single-pass census-driven; phantoms preserved); control_set.yaml regenerated; C2 already Doc14–20 — no renumber |
| Case_03 P1 | ontology v2.1-port (maturity_model + 7 promoted classes, DORA kept); compact.json 1.1; build_p1_graph 749n/2054l/9 audits; 119 EvidenceItems (37 cov + 38 CSF + 38 PF + 6 AI-RMF real); validator v2.4 strict PASS; dashboards Folios I–VIII + Maturity |
| Case_02+03 P2 wave | phase2_ontology v1.0 ×2; build_p2_graph (C2 278n/356l, C3 242n/340l) + validators strict PASS; P2 dashboards ×2; control_set canonical at P2 root; C2 TRACEABILITY_AUDIT.md |
| Case_02+03 P3 v0 | verify_rich ported + run (C2 2 FAIL/6 PASS; C3 3 FAIL/5 PASS — honest); RULE_FREEZE/KG_CHAINS/NIST_ANCHORS/CORPUS_LINKAGE GENERATED v0 + banner; RICH_LINT_BASELINE ×2; functional trees |
| Back-ports to Case_02 | P1 Maturity radars 0-width canvas fix + frameworkOf + 34-active label |
| Gates | 3× check_unmapped + 2× posture ALL PASS; smoke 16/16 (14 dashboards + 2 new); waiver harmonisation for v1.6 provenance lines (model_csf_strict/maturity scalars/maturity redesign/P1_Maturity.html) |
| Verification | subagent outputs independently verified by orchestrator (gates re-run, JSON deep-checks 0 dangling/0 forbidden scalars, screenshots read back) |
| Human-review queue | 02_CASES/PORT_PARITY2_REPORT.md — orphan obligations (C3: 10; C2: 14 PO/40 SO objective-coverage), verify_rich FAILs, D-07.2 coverage decision, phantom refs left untouched |
| Status | Campaign complete; P7 items queued for human |

---

## 0.3 2026-09-02 — Case_02 Complete Dashboard Parity (Folios I–VIII)

| Metric | Value |
|--------|-------|
| Files changed | `00_VISUALISATIONS/Case_02/Case_02_P1_Dashboard.html`, `00_VISUALISATIONS/Case_02/Case_02_P1_Maturity.html`, `00_VISUALISATIONS/Case_02/build_case02_dashboard.py`, `01_PHASE1_CONTEXT_RICH/scripts/build_p1_graph.py`, `01_PHASE1_CONTEXT_RICH/scripts/build_p1_dashboard.py`, `01_PHASE1_CONTEXT_RICH/data/phase1_graph.json`, `01_PHASE1_CONTEXT_RICH/PROJECT_STATE.md`, `CHANGE_LOG_CENTRAL.md` |
| Graph nodes & links | 521 nodes / 1205 links (70 AdjustedGoals from Doc13 §8, 10 DataSubjectCategories, 1071 ambiguity cards from Doc09, 45 NistControl via REG_CHAIN + PF + AI-RMF, 59 EvidenceItems, 8 enriched audits, 625 RACI edges, 71 APPLIES_TO edges) |
| Validator v2.4 | 9 check gates (ontology conformity, invariant parity, node ID resolution, maturity strictness, check_phase_c) + `--strict` PASS |
| Folio I (Exec) | Company card (SecureBorder B.V., 450 emp, 5–8 sec FTE, Edge AI/EU Cloud/Signed OTA/PKI), Applicability (4/5: GDPR, CRA, NIS2, AI Act), Tiers (34: 8 RIGOROUS / 26 STANDARD), Coverage (34 SUBSTANTIVE / 4 NOT_ADDRESSED), Adjusted Goals (70: 35 Privacy / 35 Security), Ambiguity (1071 in scope), Caveats (8 audits), Pipeline legend, Footer, JS label formatters |
| Folio II (Graph) | Toolbar Tier filter (RIGOROUS / STANDARD), ECharts force layout parameters optimized for 521 nodes (repulsion 350, edgeLength [80, 180], gravity 0.08, friction 0.6), Side Inspector typeLabels for CoverageGap, Stakeholder, EvidenceItem |
| Folio III (Audits) | 8 enriched audits with full schema (`title`, `detail`, `evidence`, `recommendation`), 5 canonical kind categories (`structural`, `cross_doc_conflict`, `broken_link`, `coverage_gap`, `blocking_ambiguity`), header `8 findings · click for full text` |
| Folio IV (Deep-Dive) | 2-track Adjusted Goals columns (`Privacy Goal` AG-D-XX.Y-001 and `Security Goal` AG-D-XX.Y-002 per Doc13 §8), DataTable column indexing synced |
| Folio V (Pipeline) | Layered pipeline updated for Case_02 counts (10 Stakeholders, 7 Business Goals, 5 Regulations, 111 Clauses, 38 Sub-domains, 70 Adjusted Goals, 9 Tensions, 12 Coverage Gaps) |
| Folio VI (RACI) | Complete 63 activities × 12 roles matrix (`CEO`, `CTO`, `CISO`, `DPO`, `AI-Gov`, `Comp`, `IA`, `SOC`, `Legal`, `HR`, `Proc`, `Board`), full R/A/C/I cell rendering + composite letter support, sorting and filtering across all 12 roles, sub-domain links |
| Folio VII (Architecture) | 13 Systems, 7 DataStores, 12 DataFlows, 22 ThirdParties / Vendors, risk ranking, compliance posture (DPA / Art. 28 / SBOM / Exit plan), interactive flow map and vendor dossier |
| Folio VIII (Maturity) | Integrated AI-RMF outcome parsing (`GOVERN-`, `MAP-`, `MEASURE-`, `MANAGE-`) into unified dashboard table alongside CSF 2.0 and NIST PF 1.0 anchors |
| Verification | `build_p1_dashboard.py --check --strict` PASS; Playwright smoke 12/12 dashboards PASS |
| Status | Case_02 Phase 1 Dashboard parity 100% complete |

---

## 0.2 2026-08-27 — Case_02 Maturity redesign v2.3 (campaign)

| Metric | Value |
|--------|-------|
| Files changed | 4 doc + 3 script + 1 dashboard — `01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` v2.2→v2.3 + `data/phase1_ontology.compact.json` schema 1.0→1.1 + `scripts/build_p1_graph.py` (de-novo, 19 node types from YAML+XLSX) + `scripts/build_p1_dashboard.py` (validator v2.3, 4 gates) + `Doc05_Security_Posture.md` v1.2→v1.3 + `Doc12_Proportionality_Profile.md` v1.0→v1.3 + `00_VISUALISATIONS/Case_02/Case_02_P1_Maturity.html` (Folio VIII standalone) + `build_case02_dashboard.py` (inline JSON for file://) |
| New doc | `00_METHODOLOGY/00_VISUALISATIONS/Case_02/Case_02_P1_Maturity.html` (Folio VIII standalone for Case_02) |
| New node types | EvidenceItem (57 seed: 34 Coverage + 25 Capability — 10 CSF + 10 PF + 5 AI-RMF); TierDecision deferred to P7 |
| New relations | HAS_EVIDENCE / CITES_OUTCOME / CITES_CLAUSE / DECIDED_AT / USED_IN (mirror Case_01 v1.6) |
| EvidenceItems seed | 59 total (57 EVIDENCE_ITEMS seed + 2 inferred; 34 Coverage + 25 Capability) |
| NistControl nodes | 15 (10 PF + 5 AI-RMF — CSF anchors implicit via Doc13 §7 crosswalk) |
| Validator gates (v2.3) | Gate 1 (no Tier scalars on sub-domain — passes: 0 hits) + Gate 2 (11 proportionality keys + evidence_ids — passes: 34/34 active SDs) + Gate 3 (proportionality_tier non-null — passes) + Gate 4 (sources[] resolved — passes: 0 unresolved) — `--check` PASS |
| Folio VIII rendering | 4 KPI tiles (59 / 34 / 25 / 3) + tier-bar Function (6 segments, GV/ID/PR/DE/RS/RC) + 2 radares ECharts (CSF hexagonal + PF pentagonal — primeiros radares do repo) + AI-RMF callout (SecureBorder AI Act provider; AI-RMF anchors without radar) + Citation discipline callout + 2 tabelas (Scale B com PF anchor + Scale A com Framework=CSF/PF/AI-RMF) |
| Counts | 35/35 active SDs with proportionality; 34/34 with evidence_ids; 4 NOT_ADDRESSED sub-domínios (D-06.4, D-07.4, D-08.3, D-09.3) explicit |
| Legacy cleanup | Doc05 banner atualizado para `DEPRECATED_FOR_MATURITY`; Doc12 nota v2.3 (frontmatter v1.3); Doc19 intocado (posture já resolvido lá) |
| Tier assignment | **NÃO feito** — P7 / human decision per §4 escada rule; Folio VIII mostra evidência apenas |
| Smoke 10/10 | `00_VISUALISATIONS/Case_02/Case_02_P1_Maturity.html` (118 ROWS, 0 ERR) joins the 9 dashboards — total 10/10 PASS |
| Verdict | PASS (validator v2.3 — 59 EvidenceItems, 34/34 sub-domínios activos com evidence_ids, 0 forbidden scalars, 0 unresolved sources) |

**AI Act applicable in Case_02**: SecureBorder is AI Act provider per `04_Company_Context_Assessment.md` §L217; AI-RMF anchors (GOVERN-1.2, MAP-2.1, MEASURE-3.2, MEASURE-4.1, MANAGE-5.2) added as Capability EvidenceItems. No radar (AI-RMF has 4 functions vs CSF's 6; mixing axes would mislead) — they appear in the Scale A table with `Framework=AI-RMF`.

**User complaint addressed (same as Case_01 round 1)**: "não vejo propriamente o referencial que é visto como o de referencia... parece ser muito ad-hoc" — referencial único agora declarado (NIST CSF 2.0 §3.4) na ontologia Case_02 v2.3. User complaint addressed (round 2): "não quero que te focques apenas no NIST CSF, também tens o PF" — AI-RMF anchors + PF anchors all in CSF+PF radares + AI-RMF table.

---

## 0.1 2026-08-27 — Case_01 Maturity redesign v1.6 (cross-phase)

| Metric | Value |
|--------|-------|
| Files changed | 4 doc + 3 script + 2 dashboard artefact — `00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md` (new, v1.0, 13 sections) + `phase1_ontology.yaml` v1.5→v1.6 + `phase1_ontology.compact.json` schema 1.0→1.1 + `scripts/build_p1_graph.py` (EVIDENCE_ITEMS seed 47 + emits) + `scripts/build_p1_dashboard.py` (check_phase_c v1.6, 4 gates) + `Case_01_P1_Dashboard.html` (Folio VIII CSS/JS) + `Case_01_Dashboard.html` (legacy `#maturity` removed) + `Doc05_Security_Posture.md` (banner v1.6) + `Doc12_Proportionality_Profile.md` (note v1.6) + Case_01 P1 PROJECT_STATE (Sprint 9 log) |
| New doc | `00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md` v1.0 (single normative reference for maturity across all phases/cases) |
| New node types | `EvidenceItem`, `TierDecision` (v1.6; TierDecision instantiated in later session per P7) |
| New relations | HAS_EVIDENCE / CITES_OUTCOME / CITES_CLAUSE / DECIDED_AT / USED_IN |
| New invariants | forbidden_in_subdomain_attrs, citation_required, scale_consistency |
| EvidenceItems seed | 47 (32 Coverage + 10 Capability CSF + 5 gap) → 57 after Phase 3a (+10 PF anchors) |
| NistControl PF nodes | 10 (framework=PF, anchored on OVERLAY_NIST_PF_1.1.md §2) |
| Validator gates (v1.6) | Gate 1 (no Tier scalars on sub-domain) + Gate 2 (12 proportionality keys, evidence_ids) + Gate 3 (sources[] resolved) + Gate 4 (proportionality_tier non-null) — `--check` PASS |
| Folio VIII rendering | 4 KPI tiles (mini-executive) + tier-bar Function (6 segments, paleta alinhada) + 2 radares ECharts lado a lado (CSF hexagonal + PF pentagonal — primeiros radares do repo) + callout pedagógico "How evidence works" + 2 tabelas (Scale B com coluna PF anchor + Scale A com coluna Framework) |
| Legacy cleanup | `#maturity` section em `Case_01_Dashboard.html` removido; Doc05 banner atualizado para `DEPRECATED_FOR_MATURITY`; Doc12 §4 nota v1.6 |
| Tier assignment | **NÃO feito** — P7 / human decision per §4 escada rule; Folio VIII mostra evidência apenas |
| Verdict | PASS (validator v1.6 — 57 EvidenceItems, 37/37 sub-domínios activos com evidence_ids, 0 forbidden scalars, 0 unresolved sources) |

**User complaint addressed:** "não vejo propriamente o referencial que é visto como o de referencia... parece ser muito ad-hoc, não vejo propriamente o referencial" — referencial único agora declarado: NIST CSF 2.0 §3.4 (citado verbatim em MATURITY_MODEL_CSF_STRICT.md §2). User complaint addressed (round 2): "não quero que te focques apenas no NIST CSF, também tens o PF" — Phase 3a seed adicionou 10 EvidenceItems PF + 10 NistControl PF; Folio VIII tem 2 radares lado a lado.

---

## 0. Sprint 6 (2026-08-26) — Case_01 Phase 3 RICH Product Baseline Rewrite

| Metric | Value |
|--------|-------|
| Files changed | 8 (Doc20, Doc21, Doc22, Doc26, RULE_FREEZE, 22_Traceability_Matrix.xlsx, 18_Functional_Tree.drawio, validation/VALIDATOR_SPRINT6.md) + scripts/build_traceability_matrix_rich.py + Case PROJECT_STATE.md + Case progress.json |
| New functional U.C.s (U.C.7-11) | 23 (Account&Access, Team&Task Core, Collaboration, Platform, Self-Service) |
| New misuse cases (MUC-01..08) | 8 (Sindre & Opdahl schema) |
| Security U.C.s (U.C.1-6) preserved | 35 — IDs verbatim (P5) |
| New relationships | 67 edges (35 «constrains» + 8 «threatens» + 24 «mitigated by» + 13 functional «include» + ?) |
| Total relationship edges | 91 |
| New variants | 8 (V-19..V-26 — functional plan tiers, MFA, notification batching, mobile offline, large export) |
| xlsx sheets | 10 → 12 (added FUNCUC_TO_SECUC, MUC_TO_MITIGATION) |
| drawio nodes / edges | 42 / 41 → 79 / 77 |
| Findings | F-S5-02 RESOLVED · F-NEW-S6-01 OPEN (KG E4 follow-up) |
| Verdict | PASS_WITH_FINDINGS (VALIDATOR_SPRINT6.md) |

**User complaint addressed:** "os casos de uso não fazem sentido nenhum... só vejo um conjunto de coisas que tem de ser feitas em termos de segurança mas não vejo nenhum caso de uso, era suposto poder criar task e essas tasks serem segurança" — Doc20 v3.0 now leads with 23 product U.C.s (signup, login, create task, assign task, comment, attachment, mobile sync, Stripe checkout, etc.) and 8 misuse cases; security/compliance U.C.s attach as constraints. IDs `U.C.X.Y.Z` preserved across all 35 security U.C.s and extended to packages 7-11 for the new functional surface.

**Backwards compatibility (P5):** 35 U.C.1-6 IDs unchanged. ~1264 U.C.* references in Phase 3 remain valid; zero remap downstream.

**Follow-up (logged, not in scope of this sprint):**
- **F-NEW-S6-01:** KG E4 incremental rebuild on Deucalion (~14h cluster) to surface the 23 functional U.C.7-11 + 8 MUC nodes in the Graphify KG (currently 0 nodes for these in the E3 build 2026-08-23). Human approval required (P7) before scheduling.

**Commits (5):**
1. `1661e5e [EXECUTOR] Doc20 v3.0: product UCs (U.C.7-11) + anatomy for U.C.1-6 + 8 MUCs — Case_01`
2. `18a637f [EXECUTOR] Doc21/22 v1.0: extended with constrains/threatens/mitigated_by + functional variants — Case_01`
3. `4256213 [EXECUTOR] xlsx 12-sheet + RULE_FREEZE v2.0 — Case_01`
4. `05d75e7 [EXECUTOR] Doc26 v2.0 + drawio regen (product-root tree) — Case_01`
5. (this commit) `[VALIDATOR] Sprint 6 validator + PROJECT_STATE + progress.json — Case_01`

---

## 0b. Port Campaign (2026-08-28) — Case_01→Case_02 upgrade (Fases 0–7)

| Metric | Value |
|--------|-------|
| Scope | Case_02_SecureBorder_Solutions P1+P2 (+ transversal refs), port of the Case_01 Aug-2026 campaign |
| Commits | 13 (`5bfd81f`..HEAD), `[EXECUTOR]/[VALIDATOR] port Case_02 FaseN` |
| Fase 0 | PORT_census_v0 (188 UNMAPPED baseline); D1 AI-C19 propagation (Doc10 v1.2, ontology v2.1, 112→111); state-chain repair |
| Fase 1 | corr-008 AG- migration (PG→-001, SG→-002, 70 goals); corr-010 rename Doc13_Adjusted_Goals; frontmatter DocNN repair (279 refs) |
| Fase 2 | P1 posture migration (Doc13 70 cards, Doc05 DEPRECATED_FOR_POSTURE, Doc08 counts); ontology v2.2 kg_ontology alignment |
| Fase 3 | UNMAPPED adjudication (PRIVACY/AIRMF retired; N/A non-AI scope ×21 CR; MEASURE-2.7/PR.PO-P4 anchors; 7 justified PF gaps); §4.6 vocabulary; frozen AI RMF 72-subcat list |
| Fase 4 | P2 posture (Doc19 52 controls non-uniform; SPEC supersession banner) |
| Fase 5 | Control Set v1: Doc18 v6.0, corrected 24-field schema, Annexes A–C, control_set.yaml 63 controls (status-parse fix) |
| Fase 6 | Sprint sweep P2/P3/00_COMMON; gates v0.3 ported — BOTH GATE PASS |
| Fase 7 | Case_02 PRODUCTION_FLOW v1.0; flow audit PASS_WITH_NOTES (mirror refresh) |
| Verdict | PASS — Case_02 P1+P2 now at the Case_01 Aug-2026 standard, adapted to 4-regulation scope |

---

## 0c. Port Campaign (2026-08-28) — Case_01→Case_03 upgrade (Fases 0–7)

| Metric | Value |
|--------|-------|
| Scope | Case_03_OmniBank_Financial P1+P2 (Maximum, 5/5 regs incl. DORA), port of the Case_01 Aug-2026 campaign |
| Commits | 11 (`c765800`..HEAD), `[EXECUTOR]/[VALIDATOR] port Case_03 FaseN` |
| Fase 0 | PORT_census_v0 (262 UNMAPPED baseline); tensions canonical = 5 (T-005 DORA TLPT added to Doc17); AI-C19 KEPT (PROVIDER+DEPLOYER); PF 1.0; corr-012 registered; state-chain repair |
| Fase 1 | Sprint sweep; legacy→DocNN map by content (377 refs, shifted slot map); Docs 16-20 DRAFT→ACTIVE |
| Fase 2 | P1 posture purge (Doc05, Doc08 158 cells, Doc13 76); ontology v2.0-port kg_ontology with DORA branch |
| Fase 3 | UNMAPPED adjudication (AIRMF/PRIVACY retired; 23 CR → N/A non-AI-scope; 15 CR real anchors; PF gaps justified); SPEC §4.6 |
| Fase 4 | P2 posture (Doc21 78 controls, 177 PARTIAL / 57 N/A); SPEC supersession banner |
| Fase 5 | Control Set v1: Doc20 v2.0, control_set.yaml 78 controls (38 CR + 40 BPR), F23 traceability with AG- |
| Fase 6 | Gates v0.3 ported — BOTH GATE PASS (CSF check WARN-only) |
| Fase 7 | PRODUCTION_FLOW v1.0; flow audit PASS_WITH_NOTES (3-case mirror) |
| Verdict | PASS — Case_03 P1+P2 at the Case_01 Aug-2026 standard, DORA-aware |

---

## 1. CHANGE LOG PURPOSE

## 1. CHANGE LOG PURPOSE

This document tracks all changes affecting multiple cases or the methodology structure itself.

### Decision Tree — When to Update Which Log

```
┌─────────────────────────────────────────────────────────────┐
│  CHANGE DETECTED IN AEGIS IMPLEMENTATION                      │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ What type of change?  │
              └───────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Case-Specific│  │  Affects 2+  │  │  Methodology │
│ Change       │  │  Cases       │  │  / Structure │
└──────────────┘  └──────────────┘  └──────────────┘
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Update:      │  │ Update:      │  │ Update:      │
│ - Case       │  │ - Central    │  │ - Central    │
│   PROJECT_   │  │   Change Log │  │   Change Log │
│   STATE.md   │  │              │  │ - Global     │
│              │  │ Optionally:  │  │   State      │
│ Optionally:  │  │ - Case logs  │  │ - QWEN.md    │
│ - Global     │  │   if case-   │  │   (if major) │
│   State (if  │  │   specific   │  │              │
│   milestone) │  │   details    │  │              │
│              │  │   needed     │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
```

### Detailed Decision Criteria

| Change Type | Update Case Log? | Update Central Log? | Update Global State? | Update QWEN.md? |
|-------------|------------------|---------------------|----------------------|-----------------|
| **Document typo fix** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Document section update** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Phase completion** | ✅ Yes | ✅ Yes (major) | ✅ Yes (status) | ❌ No |
| **Script/Tool update** | ✅ Yes | ✅ Yes (if reused) | ❌ No | ✅ Yes (if structural) |
| **Methodology change** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Directory structure change** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Template/guideline change** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **New case added** | N/A | ✅ Yes | ✅ Yes | ✅ Yes |
| **Case removed/archived** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

---

## 2. CENTRAL CHANGE LOG ENTRIES

### 2026-04-06 — Case_01 Consistency Fixes + Lint Script Audit

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION / TOOLING / DATA CONSISTENCY |
| **Affected Cases** | Case_01 (primary), GLOBAL_PROJECT_STATE, lint scripts |
| **Impact** | High |
| **Author** | Security Architect + ARM Lint Runner Agent |

**Description:**

Comprehensive audit and fix of Case_01 data inconsistencies, phantom references, and lint script bugs discovered through multi-agent cross-verification against an external review. The audit verified 5 critical claims against actual document content and script source code, finding that some review claims were exaggerated while others revealed real structural bugs.

**Lint Script Fixes:**
- **`lint_11_rules_catalog.py`** — Rewritten from dead code (defined wrong function name `lint_08_obligation_derivation`) to proper Rules Catalog validation with 11 checks: ID format, sub-domain, verification method, implementation mode, priority, NI, goal refs, source clauses, dashboard counts, duplicates, section completeness
- **`run_all_lints.py`** — No code change; lint_11 now imports correctly after fix

**Document Data Fixes (Case_01):**

| # | File | Issue | Fix |
|---|------|-------|-----|
| 1 | `11_Rules_Catalog.md` | Dashboard says 38 rules (23+15) but tables have 46 (30+16) | Updated 9 sections with correct counts |
| 2 | `15_Requirements_Allocation.md` | 10 phantom rule IDs (CR-D-02.4, 06.4, 07.2/3/4, 08.3, 09.3, 10.1) referencing non-existent rules | Removed all phantom derivation nodes |
| 3 | `13_Use_Cases_Catalog.md` | 4 UCs reference phantom rules | Replaced with existing equivalents |
| 4 | `14_Architectural_Nodes.md` | 8 nodes reference phantom rules | Replaced with existing equivalents |
| 5 | `16_Compliance_Gates_Report.md` | 8 gates reference phantom rules | Removed/replaced; counts 38→46 |
| 6 | `Phase_3_Functional_Decomposition_Synthesis.md` | 18 legacy RULE-COM/BST IDs (v1.0 format) | Normalized to 17 v2.0 CR-D/BPR-D IDs + 1 deprecated |
| 7 | `10_Privacy_Security_Goals.md` | Missing D-06 Supply Chain section; SG-D-02.4-001 wrong ID | Added D-06 section (3 goals); fixed ID to SG-D-06.2-001 |
| 8 | `25_Risk_Analysis.md` | Threat count 42 claimed, actual 38 | Corrected to 38 (31 STRIDE + 7 LINDDUN) |
| 9 | `23_Functional_Requirements.md` | INSPECT count 20 vs 22 in table | Corrected to 22; ANALYZE total corrected |
| 10 | `24_Non_Functional_Requirements.md` | Dangling NFR-SEC-04 reference | Replaced with NFR-INT-05 |
| 11 | `PROJECT_STATE.md` | Phase 2 shows "Pending" but docs exist | Updated to "Complete"; tension count 1→4 |
| 12 | `GLOBAL_PROJECT_STATE.md` | Case_01 Phase 2 shows "Pending" | Updated to "Complete" |
| 13 | 6 documents | Status placeholder "DRAFT \| REVIEW \| APPROVED" | Changed to single value "DRAFT" |
| 14 | `03_Design_Decisions_Log.md` | Circular dependency (Doc 07 in inputs) | Removed; fixed Next Document ref |
| 15 | `B_Sequence_Diagrams.md`, `C_Class_Diagrams.md` | Missing input dependencies | Added 23_Functional_Requirements.md and 01_Company_Context.md |

**Supporting Script Updates:**
- `create_rules_catalog_excel.py` — Updated counts 23→30, 15→16, 38→46
- `FASE2_DADOS_COMPILADOS.md` — Updated counts + verification note

**Verification Results (Post-Fix Lint Run):**

| Phase | Lints Passed | Warnings | Status |
|-------|-------------|----------|--------|
| Phase 1 | 3/3 | 3 | ✅ PASS |
| Phase 2 | 4/4 | 2 | ✅ PASS (was 3/4 — lint_11 now works) |
| Phase 3 | 7/7 | 7 | ✅ PASS |
| **Total** | **14/14** | **12** | ✅ ALL PASS |

**Review Claim Verification:**

| Claim | Review Said | Reality | Verdict |
|-------|------------|---------|---------|
| C1: Case_01 ≠ v2.0 | "Doesn't validate" | Track, relationships, SCs all correct | ❌ Exaggerated |
| C2: Coverage 45.7% | 21/46 mapped | Correct but mapped to UCs, not FRs | ⚠️ Partially correct |
| C3: Dual ID systems | Two systems coexist | FR/NFR match spec; only Synthesis had legacy IDs | ⚠️ Partially correct |
| C4: Obligation leak | Phase 1/2 overlap | Plausible conceptual issue | ⏳ Not verified |
| C5: KGs isolated | Not in pipeline | Confirmed — no KG queries in docs | ✅ Confirmed |
| lint_11 dead code | No validation | Confirmed — wrong function name | ✅ Confirmed |
| Enum outdated | BUILD/BUY still valid | Corrected — v2.0 enums present | ❌ Outdated |

**Files Modified:** 18 total
- **Documents:** 12 (Case_01)
- **Scripts:** 3 (lint_11, create_rules_catalog_excel.py, update_traceability_matrix.py)
- **State files:** 2 (PROJECT_STATE.md, GLOBAL_PROJECT_STATE.md)
- **Change logs:** 1 (CHANGE_LOG_CENTRAL.md)

---

### 2026-04-05 — Phase 3 Reformulation: UC-Centric Iterative Decomposition

| Field | Value |
|-------|-------|
| **Type** | METHODOLOGY / STRUCTURE |
| **Affected Cases** | All (Case_01, Case_02, Case_03) |
| **Impact** | High |
| **Author** | System Architect |

**Description:**

Phase 3 workflow fundamentally restructured from flat FR iteration to UC-centric iterative decomposition based on Sofia Azevedo's PhD thesis (4SRS method). Use cases are now the primary requirement specification artifact across multiple abstraction levels (L0→L1→L2), with formal relationships (`«include»`, `«refine»`, `«extend»`) and variability handling (alternatives, specializations, options).

**Key Changes:**
- **Iteration target:** Changed from Functional Nodes to Use Cases
- **Decomposition mechanism:** `«refine»` + `«include»` relationships replace flat tree hierarchy
- **Variability handling:** `«extend»` [«alternative»/«specialization»] + `«option»` for multi-regulation cases
- **Compliance gap response:** Refine UC or add UC instead of adding Functional Nodes
- **Risk cycle feedback:** Threats → new/refined UCs instead of mitigation nodes
- **New stop conditions:** SC2 (Relationship Completeness), SC3 (Detail Sufficiency), SC4 (Variability Complete)

**Documents Changed:**
- Updated: `CONTEXT_PHASE3.md` (complete rewrite with new workflow)
- Updated: `Class_Models/phase3_decomposition.md` (added UseCaseRelationship, RelationshipType, VariabilityType)
- Created: `TEMPLATES/13_Use_Cases_Catalog.md` (restructured template)
- Created: `TEMPLATES/13a_Use_Case_Relationships.md` (new document template)
- Created: `TEMPLATES/13b_Use_Case_Variability.md` (new document template)
- Updated: `lints/phase3/lint_13_use_cases.py` (added relationship, variability, level validation)
- Created: `lints/phase3/lint_13a_relationships.py` (new lint script)
- Created: `lints/phase3/lint_13b_variability.py` (new lint script)
- Updated: `lints/run_phase3_lints.py` (added new lint imports)

**Files Changed:** 9 files updated/created

**Impact on Cases:**
- Case_01: Needs restructuring (legacy Phase 3 docs → new structure)
- Case_02: Needs restructuring (legacy Phase 3 docs → new structure)
- Case_03: Will use new workflow from start (Phase 3 not yet started)

---

### 2026-04-04 — Case 02 Phase 3 Complete: 9 Documents + Quality Gate 98.9%

| Field | Value |
|-------|-------|
| **Type** | METHODOLOGY / MILESTONE |
| **Affected Cases** | Case_02 (SecureBorder Solutions) |
| **Impact** | High |
| **Author** | System Architect |

**Description:**

Completed all 9 Phase 3 documents for SecureBorder Solutions (High Complexity — 4 regulations: GDPR, CRA, NIS 2, AI Act). Quality Gate: 98.9% PASS (target: 85%).

**Documents Created:** 13_Use_Cases_Catalog.md (44 UCs), 14_Architectural_Nodes.md (27 nodes), 15_Requirements_Allocation.md (89 derivations), 16_Compliance_Gates_Report.md (48 gates), 17_Functional_Tree.md (71 nodes), 23_Functional_Requirements.md (72 FRs), 24_Non_Functional_Requirements.md (56 NFRs), 25_Risk_Analysis.md (62 threats, 20 risks), 22_Traceability_Matrix.xlsx (8 sheets).

**Files Changed:** 9 new documents + 1 Excel file

---

### 2026-04-04 — Quality Gate Fix: Deduplicated Rule ID Counting

| Field | Value |
|-------|-------|
| **Type** | TOOL FIX |
| **Affected Cases** | All |
| **Impact** | High |

**Description:** Patched `quality_gate.py` to deduplicate rule IDs. Was counting duplicates from summary tables (63/95 = 66.3%). Now counts unique IDs only (63/63 = 100%).

---

### 2026-04-04 — BP- → BPR- Prefix Rename

| Field | Value |
|-------|-------|
| **Type** | RENAME |
| **Affected Cases** | Case_02 |
| **Impact** | Medium |

**Description:** Renamed 33 best practice rule IDs from `BP-` to `BPR-` across 6 files. Quality gate script requires `BPR-` prefix.

---

### 2026-04-04 — doc-coauthoring Skill Updated with AEGIS Context

| Field | Value |
|-------|-------|
| **Type** | TOOL UPDATE |
| **Affected Cases** | All |
| **Impact** | Medium |

**Description:** Added AEGIS methodology context to doc-coauthoring skill: project structure, document naming, rule ID formats, taxonomy, skills reference.

---

### 2026-04-04 — Lint Restructuring: Per-Phase Runners + Per-Document Scripts

| Field | Value |
|-------|-------|
| **Type** | TOOLS / STRUCTURE |
| **Affected Cases** | All (Case_01, Case_02, Case_03) |
| **Impact** | High |
| **Author** | AEGIS Tooling Lead |

**Description:**

Restructured linting tools from a single monolithic runner into per-phase runners with auto-discovery of per-document lint scripts.

**Changes:**

1. **New Shared Utility:**
   - `lints/lint_utils.py` — Case resolution, lint runner, report generator

2. **Per-Phase Runners Created:**
   - `run_structural_lints.py` — Structural lints (document structure, Mermaid)
   - `run_phase1_lints.py` — Phase 1 lints (company context, regulatory mapping, references)
   - `run_phase2_lints.py` — Phase 2 lints (auto-discovers scripts)
   - `run_phase3_lints.py` — Phase 3 lints (auto-discovers scripts)

3. **Meta-Runner Refactored:**
   - `run_all_lints.py` — Now delegates to phase runners (backward compatible)

4. **Per-Document Lint Scripts Created (9 total):**
   - Phase 2: `lint_08_obligation_derivation.py`, `lint_09_strategic_tensions.py`, `lint_10_goals.py`, `lint_11_rules_catalog.py`
   - Phase 3: `lint_13_use_cases.py`, `lint_14_nodes.py`, `lint_15_allocation.py`, `lint_16_gates.py`, `lint_17_functional_tree.py`

5. **Documentation Updated:**
   - `00_METHODOLOGY/CONTEXT_TOOLS.md` — Section 2 rewritten with per-phase commands
   - `01_IMPLEMENTATION_TOOLS/lints/README.md` — Full rewrite with new structure
   - `README.md` — Linting section updated with new commands

**New Command Structure:**
```bash
# Per-phase (recommended)
python lints/run_structural_lints.py --case "TinyTask SaaS"
python lints/run_phase1_lints.py --case "TinyTask SaaS"
python lints/run_phase2_lints.py --case "SecureBorder Solutions"
python lints/run_phase3_lints.py --case "TinyTask SaaS"

# Single lint
python lints/run_phase1_lints.py --case "TinyTask SaaS" --select company_context

# All phases (backward compatible)
python lints/run_all_lints.py --case "TinyTask SaaS"
```

**Test Results:**
- `run_structural_lints.py` — Works (0/2 passed for TinyTask — expected doc issues)
- `run_phase1_lints.py` — Works (3/3 passed for TinyTask)
- `run_phase2_lints.py` — Works (auto-discovers 4 scripts)
- `run_phase3_lints.py` — Works (4/5 passed for TinyTask)
- `run_all_lints.py` — Backward compatible

**Files Created:**
- `01_IMPLEMENTATION_TOOLS/lints/lint_utils.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/run_structural_lints.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/run_phase2_lints.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/run_phase3_lints.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/phase2/lint_08_obligation_derivation.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/phase2/lint_09_strategic_tensions.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/phase2/lint_10_goals.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/phase2/lint_11_rules_catalog.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/phase3/lint_13_use_cases.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/phase3/lint_14_nodes.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/phase3/lint_15_allocation.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/phase3/lint_16_gates.py` (NEW)
- `01_IMPLEMENTATION_TOOLS/lints/phase3/lint_17_functional_tree.py` (NEW)

**Files Modified:**
- `01_IMPLEMENTATION_TOOLS/lints/run_all_lints.py` (refactored)
- `01_IMPLEMENTATION_TOOLS/lints/README.md` (rewritten)
- `00_METHODOLOGY/CONTEXT_TOOLS.md` (Section 2 updated)
- `README.md` (linting section updated)

---

### 2026-04-03 — Framework Crosswalk: 4 Frameworks Mapped to AEGIS Taxonomy

| Field | Value |
|-------|-------|
| **Type** | METHODOLOGY / TOOLS |
| **Affected Cases** | All (Case_01, Case_02, Case_03) |
| **Impact** | High |
| **Author** | AEGIS Methodology Lead |

**Description:**

Created the Framework Crosswalk document mapping 4 established security frameworks to the AEGIS 10×38 Security Control Domain Taxonomy. This provides traceability between regulatory obligations (Phase 1) and implementation guidance from industry frameworks.

**Deliverables Created:**

| File | Lines | Content |
|------|-------|---------|
| `Framework_Crosswalk_AEGIS.md` | 555 | 38 sub-domains × 5 frameworks mapping table |
| `extract_frameworks.py` | script | Reusable extraction tool for xlsx → Markdown |

**Framework Reference Files Extracted:**

| Framework | Source File | Output File | Lines | Controls Mapped |
|-----------|------------|-------------|-------|-----------------|
| **NIST CSF 2.0** | `csf2.xlsx` | `NIST_CSF/NIST_CSF_2.0.md` | 508 | 186 subcategories → 38 AEGIS sub-domains |
| **ISO 27001:2022** | `ISO-27001-Controls-List-Free-Download.xlsx` | `ISO_27001/ISO_27001_2022.md` | 220 | 97 controls → 38 AEGIS sub-domains |
| **NIST SSDF** | `nist.sp.800-218.ssdf-table.xlsx` | `NIST_SSDF/NIST_SSDF_SP_800-218.md` | 241 | 19 practices → 23 AEGIS sub-domains |
| **NIST AI SSDF** | `nist_aissdf.md` | `NIST_AI_SSDF/NIST_SP_800-218A_AI_SSDF.md` | 1,129 | AI-specific additions → 17 AEGIS sub-domains |
| **NIST 800-53 Rev 5** | `sp800-53r5-controls.xlsx` | `NIST_800-53/NIST_SP_800-53_Rev5.md` | 1,647 | 1,189 controls (extracted, not yet mapped) |

**Crosswalk Coverage Summary:**

| Framework | Sub-Domains Mapped | % | Strength |
|-----------|-------------------|---|----------|
| NIST CSF 2.0 | 38/38 | 100% | Risk management, incident response, monitoring |
| ISO 27001:2022 | 38/38 | 100% | Complete ISMS controls, physical security, policies |
| NIST SSDF | 23/38 | 61% | Secure development lifecycle, coding, testing |
| NIST AI SSDF | 17/38 | 45% | AI-specific: data integrity (PW.3), adversarial testing, model provenance |

**Key Findings:**

1. **ISO 27001 is the most complete framework** for AEGIS taxonomy — covers all 38 sub-domains with DIRECT matches
2. **NIST CSF 2.0 has 1 gap** — D-05.4 Data Portability (GDPR Art. 20 right, not a security control)
3. **SSDF is dev-focused** — strong on D-07 (Secure Development) but weak on D-01, D-03, D-04, D-05, D-06, D-08, D-09, D-10
4. **AI SSDF adds critical AI-specific practices** — PW.3 (training data integrity), adversarial testing, model weight protection, AI threat modeling
5. **Gaps are expected** — AEGIS taxonomy is regulation-derived (EU law), frameworks are implementation-derived (industry best practice)

**Why Frameworks Aren't 100% Compatible with AEGIS Taxonomy:**

| Reason | Example | Explanation |
|--------|---------|-------------|
| **Different scope** | D-05.4 Data Portability | Legal right (GDPR), not security control |
| **Different granularity** | CSF 186 subcategories vs AEGIS 38 sub-domains | CSF is risk-focused, AEGIS is regulation-focused |
| **Different origin** | SSDF 19 practices vs AEGIS 38 sub-domains | SSDF is SDLC-focused, AEGIS covers all security domains |
| **AI-specific gaps** | D-01.1 model weights | Traditional frameworks don't cover AI model security |

**QWEN.md Updated:**
- Added **Change Verification Protocol** section — mandates verification after every file change

**Files Changed:**
- `03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_AEGIS.md` (NEW — 555 lines)
- `03_REFERENCE_MATERIAL/Framework_Mappings/NIST_CSF/NIST_CSF_2.0.md` (NEW — 508 lines)
- `03_REFERENCE_MATERIAL/Framework_Mappings/ISO_27001/ISO_27001_2022.md` (NEW — 220 lines)
- `03_REFERENCE_MATERIAL/Framework_Mappings/NIST_SSDF/NIST_SSDF_SP_800-218.md` (NEW — 241 lines)
- `03_REFERENCE_MATERIAL/Framework_Mappings/NIST_AI_SSDF/NIST_SP_800-218A_AI_SSDF.md` (NEW — 1,129 lines)
- `03_REFERENCE_MATERIAL/Framework_Mappings/NIST_800-53/NIST_SP_800-53_Rev5.md` (NEW — 1,647 lines)
- `01_IMPLEMENTATION_TOOLS/scripts/extract_frameworks.py` (NEW — reusable extraction tool)
- `QWEN.md` (UPDATED — Change Verification Protocol added)
- `02_CASES/GLOBAL_PROJECT_STATE.md` (UPDATED — Framework Crosswalk section)
- `02_CASES/CHANGE_LOG_CENTRAL.md` (this entry)

---

### 2026-04-03 — Evals Implementation + Document Fixes (Case_01)

| Field | Value |
|-------|-------|
| **Type** | TOOLS / FIXES |
| **Affected Cases** | Case_01 |
| **Impact** | High |
| **Author** | AEGIS Methodology Lead |

**Description:**

Created 9 consistency evals and fixed all document issues found by evals and lints.

**Evals Created (9 total):**

| Eval | Category | What It Verifies |
|------|----------|-----------------|
| `eval_bidirectional_mapping.py` | consistency | FR↔UC and NFR↔FR mappings are consistent bidirectionally |
| `eval_count_consistency.py` | consistency | FR/NFR/UC counts by domain match grand totals |
| `eval_traceability_chain.py` | consistency | Full chain: Regulation→Clause→Rule→NFR→FR→UC→Gate |
| `eval_cross_document_refs.py` | consistency | All frontmatter references point to existing files |
| `eval_phase1_company_context.py` | consistency | All 38 questions answered, no placeholders |
| `eval_phase1_clause_mapping.py` | consistency | All 38 sub-domains covered with valid IDs |
| `eval_phase2_rules.py` | consistency | Rules have unique IDs, valid sub-domains, testable descriptions |
| `eval_phase3_risk_analysis.py` | consistency | All risks scored, mitigations mapped to FRs, residual risk calculated |
| `eval_regulatory_applicability.py` | regulatory | EU presence gate + NIS2/DORA/AI Act/GDPR/CRA applicability rules |

**Ground Truth Created:**
- `ground_truth/regulatory_rules.yaml` — NIS2 thresholds, DORA sectors, GDPR/CRA/AI Act rules, sole authority mapping, regulatory timelines

**Documents Fixed:**

| Document | Fix | Severity |
|----------|-----|----------|
| `23_Functional_Requirements.md` | 26 FRs Source UC/NFR corrected to match §4.1/§4.2 mappings | HIGH |
| `25_Risk_Analysis.md` | Residual Risk column added + 5 THR-TRN threats for Training domain | HIGH |
| `22_Traceability_Matrix.xlsx` | Regenerated v2.0 with correct data from source documents | HIGH |
| Annexes A-D | UC names corrected, 2 Level 2 flows added, dependencies fixed | HIGH |
| 4 docs | Missing frontmatter added | MEDIUM |
| ~20 docs | Missing DOCUMENT PURPOSE / VERSION HISTORY sections added | MEDIUM |
| 6 docs | Broken frontmatter refs to 02_Regulatory_Mapping_Master.xlsx removed | MEDIUM |
| Lint regex | Fixed to accept `##` headings in addition to `#` | LOW |

**Eval Results After Fixes:**
- 6/9 evals PASS
- 3/9 evals FAIL (only LOW/MEDIUM findings — auxiliary docs without frontmatter, legitimate GAP sub-domains)
- Lint: 3/5 PASS (45 warnings down from 54)

**Files Changed:**
- `01_IMPLEMENTATION_TOOLS/evals/` — 9 new eval modules + runner
- `01_IMPLEMENTATION_TOOLS/ground_truth/regulatory_rules.yaml` — new
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md`
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/25_Risk_Analysis.md`
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/22_Traceability_Matrix.xlsx`
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/annexes/A_Use_Case_Diagrams.md`
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/annexes/B_Sequence_Diagrams.md`
- `02_CASES/Case_01_TinyTask_SaaS/00_COMMON/*.md` (frontmatter fixes)
- `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT/*.md` (sections added)
- `02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES/*.md` (sections added)
- `01_IMPLEMENTATION_TOOLS/lints/structural/lint_document_structure.py` (regex fix)

---

### 2026-04-03 — Phase 2 Complete (Case_03: OmniBank Financial Systems)

| Field | Value |
|-------|-------|
| **Type** | PHASE_COMPLETION |
| **Affected Cases** | Case_03 |
| **Impact** | High |
| **Author** | Compliance Lead |

**Description:**

Phase 2 (Elaboration & Secure Design) completed for OmniBank Financial Systems — the maximum complexity case in the AEGIS methodology (5/5 regulations, 38/38 sub-domains).

**Deliverables:**
- `08_Obligation_Derivation.md` — 38 obligations derived from 150 clauses (3.95:1 ratio)
- `09_Strategic_Tensions_Report.md` — 4 tensions detected and resolved (2 CRITICAL, 1 MEDIUM, 1 LOW)
- `10_Privacy_Security_Goals.md` — 33 goals (11 Privacy + 22 Security)
- `11_Rules_Catalog.md` — 63 rules (38 compliance + 25 best practice)
- `outputs/12_Rules_Catalog.xlsx` — Machine-readable rules catalog (4 sheets)

**Key Metrics:**
- 100% sub-domain coverage (38/38) — maximum possible in AEGIS methodology
- Mean Obligation NI: 2.934
- All 4 strategic tensions resolved:
  - T-001 (CRITICAL): 24h universal incident notification workflow (Max-SLA Routing)
  - T-002 (CRITICAL): Cryptographic sharding for erasure vs. immutable logs
  - T-003 (MEDIUM): IPSARA unified assessment framework
  - T-004 (LOW): Follow CRA secure-by-default standard
- DORA dominates: 38 clauses (25.3%), 29/38 obligations (76.3%)
- 3 sole authority rules: D-03.4 (CRA), D-05.4 (GDPR), D-06.2 (CRA)

**Phase 2 Gate:** ✅ PASS

**Files Changed:**
- `02_CASES/Case_03_High_Complexity/02_PHASE2_RULES/08_Obligation_Derivation.md` (NEW)
- `02_CASES/Case_03_High_Complexity/02_PHASE2_RULES/09_Strategic_Tensions_Report.md` (NEW)
- `02_CASES/Case_03_High_Complexity/02_PHASE2_RULES/10_Privacy_Security_Goals.md` (NEW)
- `02_CASES/Case_03_High_Complexity/02_PHASE2_RULES/11_Rules_Catalog.md` (NEW)
- `02_CASES/Case_03_High_Complexity/02_PHASE2_RULES/outputs/12_Rules_Catalog.xlsx` (NEW)
- `02_CASES/Case_03_High_Complexity/PROJECT_STATE.md` (updated to Phase 2 COMPLETE)
- `02_CASES/GLOBAL_PROJECT_STATE.md` (updated Case_03 status)
- `02_CASES/CHANGE_LOG_CENTRAL.md` (this entry)

---

### 2026-04-02 — Phase 3 Complete (Case_01)

| Field | Value |
|-------|-------|
| **Type** | PHASE_COMPLETION |
| **Affected Cases** | Case_01 |
| **Impact** | High |
| **Author** | Security Architect |

**Description:**

Phase 3 (Functional Decomposition and Risk Integration) completed for TinyTask SaaS.

**Deliverables:**
- 22_Traceability_Matrix.xlsx (8 sheets, 70 traceability links)
- Annex A: Use Case Diagrams (10 Mermaid diagrams)
- Annex B: Sequence Diagrams (10 Mermaid diagrams)
- Annex C: Class Diagrams (7 Mermaid diagrams)
- Annex D: KG Inference Examples (10 SPARQL queries + results)

**Metrics:**
- 70 traceability links (Regulation → Clause → Rule → NFR → FR → UC → Gate)
- 37/37 NFRs satisfied (100%)
- 18/18 rules satisfied (100%)
- 35/35 gates PASS (100%)
- 34 Mermaid diagrams created
- Stop Condition 1: Compliance Coverage SATISFIED
- Stop Condition 2: Risk Residual SATISFIED

**Files Changed:**
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/22_Traceability_Matrix.xlsx` (NEW)
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/annexes/A_Use_Case_Diagrams.md` (UPDATED)
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/annexes/B_Sequence_Diagrams.md` (UPDATED)
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/annexes/C_Class_Diagrams.md` (UPDATED)
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/annexes/D_KG_Inference_Examples.md` (UPDATED)
- `02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md` (updated to Phase 3 100%)
- `02_CASES/GLOBAL_PROJECT_STATE.md` (updated)
- `02_CASES/CHANGE_LOG_CENTRAL.md` (this file)

---

### 2026-04-02 — v2.0 Methodology Restructure

| Field | Value |
|-------|-------|
| **Type** | STRUCTURE / METHODOLOGY |
| **Affected Cases** | All (Case_01, Case_02, Case_03) |
| **Impact** | High |
| **Author** | AEGIS Methodology Lead |

**Description:**

Complete restructure of the Methodology directory to improve organization and clarity.

**Changes:**

1. **New Directory Structure:**
   - `00_METHODOLOGY/` — Core methodology documentation
   - `01_IMPLEMENTATION_TOOLS/` — Linting, scripts, skills
   - `02_CASES/` — Case implementations (renamed from `Casos/`)
   - `03_REFERENCE_MATERIAL/` — Regulatory references, frameworks, historical
   - `04_ADMIN/` — Project administration

2. **Moved Files:**
   - `class-diagrams/` → `00_METHODOLOGY/Class_Models/`
   - `lints/` → `01_IMPLEMENTATION_TOOLS/lints/`
   - `Dados/` → `03_REFERENCE_MATERIAL/Historical/`
   - `Casos/` → `02_CASES/` (with renamed case folders)

3. **Renamed Case Folders:**
   - `Caso 1 - TinyTask SaaS (Low Complexity)` → `Case_01_TinyTask_SaaS`
   - `Caso 2 - Medium Complexity (TBD)` → `Case_02_Medium_Complexity`
   - `Caso 3 - High Complexity (TBD)` → `Case_03_High_Complexity`

4. **Updated Documentation:**
   - Created README.md for all main sections (6 files)
   - Updated PROJECT_STATE.md for Case_01 (added linting results)
   - Updated GLOBAL_PROJECT_STATE.md (v2.0 status)
   - Updated CHANGE_LOG_CENTRAL.md (this file)
   - Updated QWEN.md (directory structure section)
   - Created RESTRUCTURE_SUMMARY.md

5. **Symlinks Created:**
   - `lints/` → `01_IMPLEMENTATION_TOOLS/lints/`
   - `scripts/` → `01_IMPLEMENTATION_TOOLS/scripts/`

6. **Tooling Updates:**
   - Updated `run_all_lints.py` to use new `02_CASES/` path
   - Added case name matching for both old and new naming conventions

**Files Changed:**
- All PROJECT_STATE.md files (paths updated)
- GLOBAL_PROJECT_STATE.md (complete rewrite)
- CHANGE_LOG_CENTRAL.md (complete rewrite)
- QWEN.md (structure section updated)
- README.md (new - project overview)
- 00_METHODOLOGY/README.md (new)
- 01_IMPLEMENTATION_TOOLS/README.md (new)
- 02_CASES/README.md (new)
- 03_REFERENCE_MATERIAL/README.md (new)
- 04_ADMIN/README.md (new)
- 04_ADMIN/RESTRUCTURE_SUMMARY.md (new)

**Validation:**
- ✅ Linting tests pass (4/4 for Case_01)
- ✅ All symlinks functional
- ✅ Case matching works for both old and new names

---

### 2026-04-02 — Linting Tools Implementation

| Field | Value |
|-------|-------|
| **Type** | TOOLS |
| **Affected Cases** | All |
| **Impact** | Medium |
| **Author** | AEGIS Tooling Lead |

**Description:**

Implemented structural linting tools for automated document validation.

**Lints Created:**
1. `lint_document_structure.py` — Validates frontmatter and sections
2. `lint_mermaid_syntax.py` — Validates Mermaid diagram syntax
3. `lint_company_context.py` — Validates 38 questions (table + heading formats)
4. `lint_regulatory_mapping.py` — Validates regulatory mapping

**Test Results (Case_01):**
- ✅ 4/4 lints passed
- ⚠️ 22 warnings (informational)

**Files Changed:**
- `01_IMPLEMENTATION_TOOLS/lints/run_all_lints.py`
- `01_IMPLEMENTATION_TOOLS/lints/structural/`
- `01_IMPLEMENTATION_TOOLS/lints/phase1/`
- Updated case path to `02_CASES/`
- Added case name matching for old and new naming

---

### 2026-04-02 — Use Cases Review and Revision (Phase 3)

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION / PHASE 3 |
| **Affected Cases** | Case_01 |
| **Impact** | High |
| **Author** | Security Architect |

**Description:**

Comprehensive review and revision of Phase 3 Use Cases Catalog for TinyTask SaaS.

**Changes:**

1. **Review Report Created:**
   - Document: `13_Use_Cases_Review_Report.md`
   - Reviewer: Security Architect
   - Issues Found: 19 (3 Critical, 8 High, 8 Medium)
   - Categories: Completeness, Consistency, Feasibility, Regulatory Coverage

2. **Use Cases Catalog Updated (v2.1):**
   - **3 New Use Cases Added:**
     - UC-DP-06: Data Breach Notification (GDPR Art. 34)
     - UC-SEC-07: Business Continuity Activation (GDPR Art. 32, CRA)
     - UC-GOV-07: Regulatory Notification (CRA Art. 11, GDPR Art. 33)
   - **SLAs Corrected** (feasible for 8-person team):
     - UC-SEC-01: 1h → 4h (with MSSP)
     - UC-DP-01/02: 7 days target, 30 days max
     - UC-SEC-02: Containment 4h, Notification 72h
     - UC-SEC-04: Critical 24h, High 7 days
     - UC-IAM-06: 24 hours
     - UC-DP-06: 72 hours
     - UC-GOV-07: 24h (CRA), 72h (GDPR)
   - **Stakeholders Updated:**
     - Added SH-EXT-007: MSSP (Managed Security Service Provider)
     - Renamed SH-INT-005: "DPO/Compliance (part-time)"
     - Added FTE Allocation column
   - **Level 2 Detailed Flows:** 8 use cases with complete flows
     - UC-DP-01, UC-DP-02, UC-DP-06 (NEW)
     - UC-SEC-01, UC-SEC-07 (NEW)
     - UC-IAM-02, UC-DEV-03, UC-GOV-07 (NEW)
   - **Matrices Updated:**
     - UC → Business Goals (35 × 5)
     - UC → Stakeholders (35 × 10)
     - Prioritization (CRITICAL: 10, HIGH: 19, MEDIUM: 5, LOW: 1)

3. **Regulatory Coverage Improved:**
   - GDPR: Art. 18, 21, 33-34 now covered
   - CRA: Art. 11 now covered
   - Total: 35 use cases (GDPR: 24, CRA: 18, Both: 15)

**Files Changed:**
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/13_Use_Cases_Catalog.md` (v2.0 → v2.1)
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/13_Use_Cases_Review_Report.md` (NEW)
- `02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md` (updated)

**Validation:**
- ✅ All 19 review issues addressed
- ✅ SLAs feasible for micro-enterprise (with MSSP)
- ✅ Regulatory gaps closed
- ✅ Stakeholder assignments complete

---

### 2026-04-02 — Project State Documentation Updates

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION |
| **Affected Cases** | All |
| **Impact** | Medium |
| **Author** | AEGIS Methodology Lead |

**Description:**

Updated all PROJECT_STATE.md files to reflect v2.0 restructure.

**Changes:**
1. **Case_01 PROJECT_STATE.md:**
   - Updated document locations to new `02_CASES/` paths
   - Added linting status section (4/4 passed)
   - Updated change log with restructure entries
   - Added version 2.0 marker

2. **Case_02 PROJECT_STATE.md:**
   - Created new file (previously didn't exist)
   - Template for medium complexity case
   - Linting status: Not run (case not started)

3. **Case_03 PROJECT_STATE.md:**
   - Created new file (previously didn't exist)
   - Template for high complexity case
   - Linting status: Not run (case not started)

**Files Changed:**
- `02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md` (updated)
- `02_CASES/Case_02_Medium_Complexity/PROJECT_STATE.md` (created)
- `02_CASES/Case_03_High_Complexity/PROJECT_STATE.md` (created)

---

### 2026-04-02 — Regulatory Reference Files Relocation

| Field | Value |
|-------|-------|
| **Type** | STRUCTURE / REFERENCE_MATERIAL |
| **Affected Cases** | All |
| **Impact** | Low |
| **Author** | AEGIS Tooling Lead |

**Description:**

Moved regulation `.txt` files from project root to appropriate reference folder.

**Changes:**
1. **Files Moved:**
   - `GDPR.txt` → `03_REFERENCE_MATERIAL/Regulatory_References/GDPR/GDPR.txt`
   - `CRA.txt` → `03_REFERENCE_MATERIAL/Regulatory_References/CRA/CRA.txt`
   - `NIS2.txt` → `03_REFERENCE_MATERIAL/Regulatory_References/NIS2/NIS2.txt`
   - `DORA.txt` → `03_REFERENCE_MATERIAL/Regulatory_References/DORA/DORA.txt`
   - `AI_Act.txt` → `03_REFERENCE_MATERIAL/Regulatory_References/AI_Act/AI_Act.txt`
   - `CRA_Checklist.txt` → `03_REFERENCE_MATERIAL/Regulatory_References/CRA/CRA_Checklist.txt`

2. **Tooling Updates:**
   - Updated `lint_regulatory_references.py` to use new paths
   - Updated `REGULATION_BASE_PATH` constant

**Files Changed:**
- `01_IMPLEMENTATION_TOOLS/lints/phase1/lint_regulatory_references.py`
- `01_IMPLEMENTATION_TOOLS/lints/phase1/REGULATORY_REFERENCES_LINT.md`

**Validation:**
- ✅ Linting tests pass (regulatory_references lint still works)
- ✅ All 30 references validated successfully

---

### 2026-04-01 — Phase 1 Complete (Case_01)

| Field | Value |
|-------|-------|
| **Type** | PHASE_COMPLETION |
| **Affected Cases** | Case_01 |
| **Impact** | High |
| **Author** | Compliance Lead |

**Description:**

Phase 1 (Contextual Definition) completed for TinyTask SaaS case study.

**Deliverables:**
- 8 documents completed
- Excel matrix generated (7 sheets)
- 31/38 sub-domains covered (81.6%)
- 54 regulatory clauses mapped

**Files Changed:**
- All Phase 1 documents in Case_01
- PROJECT_STATE.md (Case_01)
- GLOBAL_PROJECT_STATE.md

---

### 2026-04-01 — Excel Generation Scripts

| Field | Value |
|-------|-------|
| **Type** | TOOLS |
| **Affected Cases** | All |
| **Impact** | Medium |
| **Author** | AEGIS Tooling Lead |

**Description:**

Created Python scripts for generating Excel matrices from Markdown data.

**Scripts Created:**
- `01_PHASE1_CONTEXT/scripts/generate_clause_mapping_excel.py`
- Generic script supporting all 5 regulations

**Features:**
- 7-sheet Excel workbook
- Dashboard with metrics
- Conditional formatting
- Formula-based calculations

---


### 2026-04-03 — Change Logger Module Created

| Field | Value |
|-------|-------|
| **Type** | TOOLS |
| **Affected Cases** | Case_01 |
| **Impact** | High |

**Description:**

Created automated change logging module. All scripts can now call log_change() to automatically update Central Change Log, Case PROJECT_STATE.md, and README.md when needed.

**Files Changed:**
- `01_IMPLEMENTATION_TOOLS/scripts/log_change.py`

---


### 2026-04-03 — Change Logger Module Created (Fixed)

| Field | Value |
|-------|-------|
| **Type** | TOOLS |
| **Affected Cases** | Case_01 |
| **Impact** | High |

**Description:**

Created automated change logging module with regex-based date handling and case name resolution.

**Files Changed:**
- `01_IMPLEMENTATION_TOOLS/scripts/log_change.py`

---


### 2026-04-03 — Change Logger Module Created (v2)

| Field | Value |
|-------|-------|
| **Type** | TOOLS |
| **Affected Cases** | Case_01 |
| **Impact** | High |

**Description:**

Created automated change logging module with regex-based date handling and case name resolution.

**Files Changed:**
- `01_IMPLEMENTATION_TOOLS/scripts/log_change.py`

---


### 2026-04-03 — Change Logger Module (v3 - Final)

| Field | Value |
|-------|-------|
| **Type** | TOOLS |
| **Affected Cases** | Case_01 |
| **Impact** | High |

**Description:**

Change logger module fixed with 5-column table format and regex date handling.

**Files Changed:**
- `01_IMPLEMENTATION_TOOLS/scripts/log_change.py`

---


### 2026-04-03 — CLI Logger Created

| Field | Value |
|-------|-------|
| **Type** | TOOLS |
| **Affected Cases** | Case_01 |
| **Impact** | Medium |

**Description:**

Command-line wrapper for change logging, usable by any agent

**Files Changed:**
- `01_IMPLEMENTATION_TOOLS/scripts/log_change_cli.py`

---


### 2026-04-04 — Test validation

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION |
| **Affected Cases** | All |
| **Impact** | Low |

**Description:**

Testing workflow gate integration

**Files Changed:**
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/25_Risk_Analysis.md`

---


### 2026-04-04 — Created 13_Use_Cases_Catalog.md for SecureBorder Solutions

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION |
| **Affected Cases** | All |
| **Impact** | Medium |

**Description:**

Phase 3.1 Task 1.1: Created Use Cases Catalog with 44 use cases across 7 categories (DP:6, SEC:8, IAM:7, DEV:6, GOV:8, AI:7, TRN:5). 100% rule coverage (38/38 CR + 15/15 BP), 100% goal mapping (38/38), 100% tension coverage (8/8). 7 detailed Level 2 use cases. Validation: sections pass, UC ID uniqueness fails expectedly (364 refs, 44 unique — validator counts all references not just definitions).

**Files Changed:**
- `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/13_Use_Cases_Catalog.md`

---


### 2026-04-04 — Created 14_Architectural_Nodes.md for SecureBorder Solutions

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION |
| **Affected Cases** | All |
| **Impact** | Medium |

**Description:**

Phase 3.1 Task 1.2: Created Architectural Nodes with 27 nodes (10 Process + 10 IT System + 7 Human Role). 100% use case coverage (44/44). Track distribution: BUILD 41%, BUY 30%, CONFIGURE 22%, OUTSOURCE 7%. Validation: PASS.

**Files Changed:**
- `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/14_Architectural_Nodes.md`

---


### 2026-04-04 — Created 15_Requirements_Allocation.md for SecureBorder Solutions

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION |
| **Affected Cases** | All |
| **Impact** | Medium |

**Description:**

Phase 3.2 Task 2.1: Created Requirements Allocation mapping 53 rules (38 CR + 15 BP) to 27 architectural nodes via 89 derivation nodes. 100% rule coverage. Allocation types: DIRECT 75%, SHARED 22%, INHERITED 3%. Verification: TEST 31%, INSPECT 47%, DEMONSTRATE 8%, ANALYZE 5%. Validation: PASS.

**Files Changed:**
- `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/15_Requirements_Allocation.md`

---


### 2026-04-04 — Created 24_Non_Functional_Requirements.md for SecureBorder Solutions

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION |
| **Affected Cases** | All |
| **Impact** | Medium |

**Description:**

Phase 3.2 Task 2.2 (reordered): Created NFR Catalog with 56 NFRs across 7 categories (7 CONF + 7 INT + 7 AVAIL + 9 PRIV + 7 ACC + 9 COMP + 10 AI). 100% measurable, 100% goal coverage (38/38), 100% rule coverage (53/53). Priority: 24 CRITICAL (43%), 28 HIGH (50%), 4 MEDIUM (7%). Validation: sections pass, NFR ID uniqueness fails expectedly (178 refs, 56 unique).

**Files Changed:**
- `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md`

---


### 2026-04-04 — Created 23_Functional_Requirements.md for SecureBorder Solutions

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION |
| **Affected Cases** | All |
| **Impact** | Medium |

**Description:**

Phase 3.3 Task 3.1: Created Functional Requirements with 72 FRs across 7 domains (IAM:13, DP:12, SEC:19, DEV:11, GOV:11, AI:12, TRN:6). 100% technology-agnostic. 100% UC coverage (44/44), 100% NFR coverage (56/56), 100% regulatory coverage (22/22). Priority: 28 CRITICAL (39%), 38 HIGH (53%), 5 MEDIUM (7%), 1 LOW (1%). Validation: sections pass, FR ID uniqueness fails expectedly (593 refs, 72 unique).

**Files Changed:**
- `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md`

---


### 2026-04-04 — Created 16_Compliance_Gates_Report.md for SecureBorder Solutions

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION |
| **Affected Cases** | All |
| **Impact** | Medium |

**Description:**

Phase 3.4 Task 4.1: Created Compliance Gates with 48 gates (40 domain + 8 AI-specific). 100% rule coverage (53/53). Verification: TEST 38%, INSPECT 42%, DEMONSTRATE 15%, ANALYZE 6%. All gates PLANNED. Validation: PASS.

**Files Changed:**
- `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/16_Compliance_Gates_Report.md`

---


### 2026-04-04 — Created 17_Functional_Tree.md for SecureBorder Solutions

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION |
| **Affected Cases** | All |
| **Impact** | Medium |

**Description:**

Phase 3.4 Task 4.2: Created Functional Tree with 71 nodes across 5 levels (7 L1 + 22 L2 + 42 L3). Track: BUILD 39%, BUY 30%, CONFIGURE 22%, OUTSOURCE 9%. 100% sub-domain coverage (38/38). Phase 3 Gate: PASS. Validation: PASS.

**Files Changed:**
- `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/17_Functional_Tree.md`

---


### 2026-04-04 — Created 25_Risk_Analysis.md for SecureBorder Solutions

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION |
| **Affected Cases** | All |
| **Impact** | Medium |

**Description:**

Phase 3.5 Task 5.1: Created Risk Analysis with 62 threats (STRIDE:37, LINDDUN:9, AI:16), 20 risks (2 CRITICAL, 11 HIGH, 7 MEDIUM), 13 mitigation controls. 100% threat→FR coverage (26/26). All residual risks LOW (acceptable). KG inferences: 6 threats, 7 mitigations, 5 dependencies. Validation: sections pass, ID uniqueness fails expectedly.

**Files Changed:**
- `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/25_Risk_Analysis.md`

---


### 2026-04-04 — Created 22_Traceability_Matrix.xlsx for SecureBorder Solutions

| Field | Value |
|-------|-------|
| **Type** | DOCUMENTATION |
| **Affected Cases** | All |
| **Impact** | High |

**Description:**

Phase 3.5 Task 5.2: Created Traceability Matrix Excel with 8 sheets (COVER, FULL_TRACEABILITY, NFR_TO_FR, FR_TO_UC, UC_TO_REGULATION, RULES_SATISFACTION, GATES_STATUS, COVERAGE_DASHBOARD). 53 rules SATISFIED, 56 NFRs mapped, 72 FRs traced, 44 UCs mapped, 48 gates defined, 20 risks mitigated. Quality Gate: 85.6% PASS (target 85%).

**Files Changed:**
- `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/22_Traceability_Matrix.xlsx`

---

## 3. PENDING CHANGES

| Priority | Change | Type | Affected Cases | Description |
|----------|--------|------|----------------|-------------|
| HIGH | Phase 2 Kickoff | Phase | Case_01 | Start obligation derivation |
| MEDIUM | Case_02 Profile | Case Setup | Case_02 | Define medium complexity profile |
| MEDIUM | Case_03 Profile | Case Setup | Case_03 | Define high complexity profile |
| LOW | Pre-commit Hooks | Tools | All | Add linting to pre-commit |
| LOW | QWEN.md Update | Documentation | All | Update structure section |

---

## 4. CHANGE STATISTICS

### 4.1 By Type

| Type | Count |
|------|-------|
| STRUCTURE | 1 |
| TOOLS | 2 |
| DOCUMENTATION | 1 |
| PHASE_COMPLETION | 1 |
| CASE_SETUP | 0 |
| **TOTAL** | **5** |

### 4.2 By Case

| Case | Changes |
|------|---------|
| All Cases | 3 (Structure, Tools, Documentation) |
| Case_01 | 2 (Phase 1 Complete, Linting) |
| Case_02 | 1 (Folder Rename) |
| Case_03 | 1 (Folder Rename) |

### 4.3 By Impact

| Impact | Count |
|--------|-------|
| High | 2 |
| Medium | 3 |
| Low | 0 |

### 4.4 v2.0 Restructure Summary

| Metric | Value |
|--------|-------|
| Folders Created | 15 |
| Folders Moved | 4 |
| Folders Deleted | 4 |
| README Files Created | 6 |
| State Docs Updated | 5 (3 cases + global + central) |
| Symlinks Created | 2 |
| Lint Tests Updated | 1 (run_all_lints.py) |
| Regulation Files Moved | 6 (to 03_REFERENCE_MATERIAL/) |

### 4.5 Regulation Files Relocation (2026-04-02)

| Metric | Value |
|--------|-------|
| Files Moved | 6 (.txt files) |
| Destination | 03_REFERENCE_MATERIAL/Regulatory_References/ |
| Lint Updated | 1 (lint_regulatory_references.py) |
| Validation Status | ✅ Passed (30/30 references) |

---

## 5. RELATED DOCUMENTS

| Document | Path |
|----------|------|
| **Global Project State** | `02_CASES/GLOBAL_PROJECT_STATE.md` |
| **Case 01 State** | `02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md` |
| **Case 02 State** | `02_CASES/Case_02_Medium_Complexity/PROJECT_STATE.md` |
| **Case 03 State** | `02_CASES/Case_03_High_Complexity/PROJECT_STATE.md` |
| **Session Handoff** | `02_CASES/SESSION_HANDOFF.md` |
| **Restructure Summary** | `04_ADMIN/RESTRUCTURE_SUMMARY.md` |

---

**Document Version:** 4.0 (Case 02 Phase 3 Complete)
**Last Reviewed:** 2026-04-04
**Next Review:** Case 03 Phase 3 Kickoff
