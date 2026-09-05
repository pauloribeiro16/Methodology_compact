# GLOBAL PROJECT STATE — AEGIS Methodology Implementation

**Last Updated:** 2026-09-05
**Version:** 7.0 (ALT-ANCHOR — UNMAPPED_* retired across 3 cases; 5 frozen referential sources + 800-53r5 generator; 3 gates v0.4 PASS; REALIZATION-CLASS; PORT-PARITY-2 — cross-case content parity: C3 P1 v1.6 layer + corr-013, P2 waves C2+C3, P3 rich v0 C2+C3, 16/16 smoke, all gates PASS)
**Scope:** All Cases

---

## 1. PORTFOLIO OVERVIEW

### 1.1 Case Studies

| Case ID | Name | Complexity | Status | Phase 1 | Phase 2 | Phase 3 | Phase 3 RICH | Quality Gate |
|---------|------|------------|--------|---------|---------|---------|--------------|--------------|
| **Case_01** | TinyTask SaaS | Low | 🟢 Active | ✅ Complete | ✅ Complete | ✅ Complete (v2.0) | 🟡 PASS_WITH_FINDINGS (v2 — see VALIDATOR_SPRINT5 2026-08-24 v2) | 78.6% (SC1-SC5) |
| **Case_02** | SecureBorder Solutions | High | 🟢 Active — PORT-PARITY-2 complete (2026-09-04) | ✅ Complete + parity (521n/1205l, Folios I–VIII) | ✅ Complete + P2 wave (278n/356l, P2 dashboard) | ✅ Complete (84.1%) + rich layer v0 (verify_rich 2 FAIL/6 PASS — findings queued) | 🟡 v0 generated (narrative docs + lint) | gates PASS |
| **Case_03** | OmniBank Financial Systems | Maximum | 🟢 Active — PORT-PARITY-2 complete (2026-09-04) | ✅ Complete + v1.6 layer (749n/2054l, 119 EV, corr-013, Folios I–VIII) | ✅ Complete + P2 wave (242n/340l, AUD-P2-005b 10 orphans) | ✅ Complete (100%) + rich layer v0 (verify_rich 3 FAIL/5 PASS — findings queued) | 🟡 v0 generated (narrative docs + lint) | gates PASS |

### 1.2 Overall Metrics

| Metric | Value |
|--------|-------|
| Total Cases | 3 |
| Active Cases | 3 |
| Completed Phases | 9 (Phase 1: Case 01/02/03, Phase 2: Case 01/02/03, Phase 3: Case 01/02/03) |
| In Progress | — |
| Linting Status | ✅ All structural lints pass (Case_01, Case_02, Case_03) |
| Use Cases (Case_01) | 35 total (10 CRITICAL, 19 HIGH, 5 MEDIUM, 1 LOW) |
| Use Cases (Case_02) | 44 total (14 CRITICAL, 22 HIGH, 6 MODERATE, 2 LOW) |
| Review Issues | 19 found, 19 fixed |

---

## 2. METHODOLOGY STRUCTURE (v2.0)

### 2.1 Directory Layout

```
Methodology/
│
├── 00_METHODOLOGY/           # Core methodology docs
│   ├── Taxonomy/
│   ├── diagrams/
│   │   ├── Class_Models/
│   │   └── fluxdiagram/
│   └── Templates/
│
├── 01_IMPLEMENTATION_TOOLS/  # Tools and scripts
│   ├── lints/
│   ├── scripts/
│   └── skills/
│
├── 02_CASES/                 # Case implementations
│   ├── Case_01_TinyTask_SaaS/
│   ├── Case_02_SecureBorder_Solutions/
│   └── Case_03_OmniBank_Financial/
│
├── 03_REFERENCE_MATERIAL/    # Reference documentation
│   ├── Regulatory_References/
│   ├── Framework_Mappings/
│   └── Historical/
│
└── 04_ADMIN/                 # Project administration
    └── meeting_notes/
```

### 2.2 Key Changes in v2.0

| Change | Before | After | Rationale |
|--------|--------|-------|-----------|
| **Root folders** | Unstructured | 00_ to 04_ numbered | Clear ordering |
| **Casos/** | `Casos/` | `02_CASES/` | English naming |
| **class-diagrams/** | Root level | `00_METHODOLOGY/diagrams/Class_Models/` | Integrated |
| **lints/** | Root level | `01_IMPLEMENTATION_TOOLS/lints/` | Tools section |
| **Dados/** | Root level | `03_REFERENCE_MATERIAL/Historical/` | Reference section |

---

## 3. PHASE COMPLETION STATUS

### 3.1 Phase 1 — Contextual Definition

| Case | Status | Documents | Linting | Excel |
|------|--------|-----------|---------|-------|
| Case_01 | ✅ Complete | 8/8 | ✅ 4/4 passed | ✅ Generated |
| Case_02 | ✅ Complete | 8/8 | ⏳ Not run | ✅ Generated |
| Case_03 | ✅ Complete | 8/8 | ⏳ Not run | ✅ Generated |

### 3.2 Phase 2 — Elaboration & Secure Design

| Case | Status | Documents | Linting | Excel |
|------|--------|-----------|---------|-------|
| Case_01 | ⏳ Pending | 0/5 | ⏳ Not run | ⏳ Not generated |
| Case_02 | ✅ Complete | 5/5 | ⏳ Not run | ✅ Generated |
| Case_03 | ✅ Complete | 5/5 | ⏳ Not run | ✅ Generated |

### 3.3 Phase 3 — UC-Centric Iterative Decomposition & Risk Integration

| Case | Status | Documents | Quality Gate | Notes |
|------|--------|-----------|--------------|-------|
| Case_01 | ✅ COMPLETE | 12/12 | 78.6% | UC-centric iterative decomposition complete |
| Case_02 | ✅ COMPLETE | 12/12 | 85.2% | UC-centric iterative decomposition complete |
| Case_03 | ✅ COMPLETE | 12/12 | 99.2% | UC-centric iterative decomposition complete |

**Phase 3 Restructuring Notes (2026-04-05):**
- Phase 3 workflow changed from flat FR iteration to UC-centric iterative decomposition
- New documents: 13a_Use_Case_Relationships.md, 13b_Use_Case_Variability.md
- Use cases now span multiple abstraction levels (L0→L1→L2) with `«include»`, `«refine»`, `«extend»` relationships
- New lint scripts: lint_13a_relationships.py, lint_13b_variability.py
- Updated class model: UseCaseRelationship, RelationshipType, VariabilityType enums added
- New stop conditions: SC2 (Relationship Completeness), SC3 (Detail Sufficiency), SC4 (Variability Complete)

---

## 4. CHANGE LOG CENTRAL

### 4.1 Recent Changes

| Date | Type | Affected Cases | Description | Impact |
|------|------|----------------|-------------|--------|
| 2026-09-04 | CAMPAIGN (PORT-PARITY-2) | Case_02 + Case_03 | Cross-case content propagation from Case_01: corr-013 (C3 P2 Doc16–21→Doc15–20, 206 refs); C3 P1 v1.6 layer (ontology maturity_model, 749n/2054l, 119 EvidenceItems, dashboards Folios I–VIII); P2 waves (phase2_ontology + graphs + P2 dashboards + control_set canonical at root); P3 rich v0 (scripts + narrative docs GENERATED + RICH_LINT); Case_02 P1 Maturity back-ports. 16/16 smoke; all 5 case gates PASS. Human-review queue: 02_CASES/PORT_PARITY2_REPORT.md | High |
| 2026-08-31 | VISUALISATIONS (v2.4) | Case_02 (Full Dashboard Parity) | Parity Folios I–VIII em `Case_02_P1_Dashboard.html`: 521 nodes / 1205 links (70 AdjustedGoals de Doc13 §8, 10 DataSubjectCategory, 1071 ambiguidade Doc09, 45 NistControl via REG_CHAIN + PF + AI-RMF, 59 EvidenceItems, 8 audits). Validator v2.4 (9 gates + strict PASS). Folio I patched (SecureBorder, 450 emp, 4/5 regs, 34 tiers, 70 AGs, 8 audits). Folio VIII AI-RMF table parsing. Smoke 11/11 dashboards PASS. | High (Case_02 atinge 100% de paridade com Case_01 nos 8 Folios) |
| 2026-08-27 | METHODOLOGY (v1.6) | Case_01 (+ cross-case referencial) | Maturity redesign: `00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md` v1.0 + `EvidenceItem` nodes (47 seed + 10 PF = 57 total) + Folio VIII (4 KPI tiles + tier-bar Function + 2 radares ECharts CSF/PF + callout pedagógico). Validator v1.6: 4 gates PASS (no Tier scalars on sub-domínio, sources[] resolved, proportionality_tier non-null). Legacy `#maturity` section em `Case_01_Dashboard.html` removido. | High (referencial único agora CSF 2.0 §3.4, documentado e auditado) |
| 2026-08-27 | METHODOLOGY (v2.3) | Case_02 (+ AI-RMF anchors) | Maturity redesign: `00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md` v1.0 (referencial partilhado) + `phase1_ontology.yaml` v2.3 + `compact.json` schema 1.1 + `scripts/build_p1_graph.py` (de-novo, 19 node types, 311 links, 59 EvidenceItems — 34 Coverage + 25 Capability: 10 CSF + 10 PF + 5 AI-RMF, 15 NistControl). Validator v2.3: 4 gates PASS. `00_VISUALISATIONS/Case_02/Case_02_P1_Maturity.html` (Folio VIII standalone) + `build_case02_dashboard.py`. Smoke 10/10 dashboards. Doc05 v1.3 + Doc12 v1.3 com nota v2.3. AI-RMF anchors aplicáveis (SecureBorder é AI Act provider) — Framework=AI na tabela Scale A, sem radar dedicado. | High (Case_02 agora alinhado com Case_01 no mesmo modelo; AI Act coberto por anchors AI-RMF) |
| 2026-05-06 | TOOLS | All | self_review.py regex bugs fixed (FR/NFR/CR/BPR/NODE false positives) | High |
| 2026-05-06 | TOOLS | All | quality_gate.py coverage calculation fixed (canonical FR-NN format, cross-doc search) | High |
| 2026-05-06 | PHASE 3 | Case_02 | Duplicate FRs renumbered (FR-80/81/82/84 → FR-85-90), quality gate: 98.9% → 85.2% | High |
| 2026-05-06 | PHASE 3 | Case_03 | Phase 3 marked complete (99.2% quality gate) | High |
| 2026-04-05 | PHASE 2 | Case_01 | Rule ID format: RULE-D- → CR-D- (23) + BPR-D- (15) in Doc 11 + all cross-refs | High |
| 2026-04-05 | PHASE 3 | Case_01 | Doc 13a Use Case Relationships created (60 relationships, OCL validated) | High |
| 2026-04-05 | PHASE 3 | Case_01 | Doc 13b Use Case Variability created (12 variants: 3 alt, 5 spec, 4 option) | High |
| 2026-04-05 | PHASE 3 | Case_01 | Doc 14 track enum: TECHNOLOGY/PROCESS/CAPABILITY_SUBREQ (49 nodes) | High |
| 2026-04-05 | PHASE 3 | Case_01 | Doc 16 stop conditions SC1-SC5 added (all PASS) | High |
| 2026-04-05 | PHASE 3 | Case_01 | Doc 25 mitigation feedback loop (8 controls → 3 new + 5 refined UCs) | High |
| 2026-04-05 | TOOLS | All | lint_14_nodes.py: removed legacy track values (BUILD/BUY/CONFIGURE/OUTSOURCE) | Medium |
| 2026-04-05 | TOOLS | All | lint_15_allocation.py: rule ID pattern updated (CR-D-/BPR-D-) | Medium |
| 2026-04-05 | TOOLS | All | 5 security hooks created (secrets, md-lint, merge-conflict, no-debug, pre-push-evals) | High |
| 2026-04-05 | GIT | All | 3 commits pushed to origin/main (initial + v2.0 alignment + verification fixes) | High |
| 2026-04-04 | TOOLS | All | quality_gate.py patched: deduplicated rule ID counting (Coverage: 66.3% → 100%) | High |
| 2026-04-04 | TOOLS | All | doc-coauthoring skill updated with AEGIS methodology context | Medium |
| 2026-04-04 | RENAME | Case_02 | BP- → BPR- prefix rename across 6 files (Rules Catalog + 5 Phase 3 docs) | Medium |
| 2026-04-04 | PHASE 3 | Case_02 | 22_Traceability_Matrix.xlsx created (8 sheets, full traceability chain) | High |
| 2026-04-04 | PHASE 3 | Case_02 | 25_Risk_Analysis.md created (62 threats, 20 risks, 13 controls) | High |
| 2026-04-04 | PHASE 3 | Case_02 | 17_Functional_Tree.md created (71 nodes, 5 levels) | High |
| 2026-04-04 | PHASE 3 | Case_02 | 16_Compliance_Gates_Report.md created (48 gates) | High |
| 2026-04-04 | PHASE 3 | Case_02 | 23_Functional_Requirements.md created (72 FRs, 100% technology-agnostic) | High |
| 2026-04-04 | PHASE 3 | Case_02 | 24_Non_Functional_Requirements.md created (56 NFRs, 100% measurable) | High |
| 2026-04-04 | PHASE 3 | Case_02 | 15_Requirements_Allocation.md created (53 rules → 27 nodes, 89 derivations) | High |
| 2026-04-04 | PHASE 3 | Case_02 | 14_Architectural_Nodes.md created (27 nodes) | High |
| 2026-04-04 | PHASE 3 | Case_02 | 13_Use_Cases_Catalog.md created (44 UCs across 7 categories) | High |
| 2026-04-04 | TOOLS | All | Lint restructuring: per-phase runners + 9 per-document scripts | High |
| 2026-04-03 | METHODOLOGY | All | Framework Crosswalk: 4 frameworks mapped to AEGIS taxonomy (CSF, ISO, SSDF, AI SSDF) | High |
| 2026-04-03 | TOOLS | All | extract_frameworks.py script created for reusable xlsx→Markdown extraction | Medium |
| 2026-04-03 | QWEN.md | All | Change Verification Protocol added | Medium |
| 2026-04-03 | EVALS | Case_01 | 9 consistency evals created + ground truth YAML | High |
| 2026-04-03 | FIXES | Case_01 | 26 FRs Source UC/NFR corrected in FR catalog | High |
| 2026-04-03 | FIXES | Case_01 | Risk Analysis: Residual Risk column + 5 THR-TRN threats | High |
| 2026-04-03 | FIXES | Case_01 | Traceability Matrix v2.0 regenerated with correct data | High |
| 2026-04-03 | FIXES | Case_01 | Annexes A-D: UC names, Level 2 flows, dependencies fixed | High |
| 2026-04-03 | FIXES | Case_01 | ~20 docs missing DOCUMENT PURPOSE/VERSION HISTORY added | Medium |
| 2026-04-03 | FIXES | Case_01 | 4 docs missing frontmatter fixed | Medium |
| 2026-04-03 | FIXES | Case_01 | Broken frontmatter refs to 02_Regulatory_Mapping_Master.xlsx | Medium |
| 2026-04-03 | TOOLS | All | Lint regex fixed to accept ## headings | Low |
| 2026-04-03 | STATE | Case_02, Case_03 | Phase 2 completion recorded for both cases | High |
| 2026-04-03 | RENAME | Case_02 | `Case_02_Medium_Complexity` → `Case_02_SecureBorder_Solutions` | Medium |
| 2026-04-03 | GLOBAL | All | GLOBAL_PROJECT_STATE.md updated (v3.0) | High |
| 2026-04-02 | PHASE 3 | Case_01 | Use Cases Review & Revision (v2.1) | High |
| 2026-04-02 | STRUCTURE | All | Directory restructure (v2.0) | High |
| 2026-04-02 | TOOLS | All | Linting tools integrated | Medium |
| 2026-04-02 | DOCS | All | README files created for all sections | Low |
| 2026-04-02 | STATE | Case_01 | PROJECT_STATE.md updated | Medium |

### 4.2 Previous Changes (v1.0)

| Date | Type | Affected Cases | Description | Impact |
|------|------|----------------|-------------|--------|
| 2026-04-01 | PHASE 1 | Case_01 | Phase 1 completed for TinyTask | High |
| 2026-04-01 | TOOLS | All | Excel generation scripts created | Medium |
| 2026-04-01 | DOCS | Case_01 | Initial Phase 1 documents | High |

---

## 4F. LANE CARDS (2026-09-05)

- **Schemas:** rubric v1.4 §5C — PROC card (SSDF-style) + CAP card (C2M2/ArchiMate-style);
  chain RULE → CAP → PROC → UC normative.
- **Pilot:** 4 cards per case (C1 Doc32 · C2 Doc31 · C3 Doc32), content faithful to the
  catalogue cards + frozen SAMM/ASVS anchors; CAP maturity bound to Scale A, values
  deferred to next EvidenceItem refresh.
- **Diagrams (v1.5 §5C.4):** one Mermaid diagram per lane card — PROC flowchart TD, CAP graph LR — 12/12 in the pilot docs; derived from catalogue scenarios/extensions.
- **Full population (2026-09-05):** 102/102 cards (C1 18 · C2 37 · C3 47) with diagrams + articulation tables + catalogue cross-refs.
- **Remaining:** bind CAP maturity to EvidenceItems; KG reflection.

---

## 4E. LANE NAMING CAMPAIGN (2026-09-05)

- **Decision (P7):** `UC-*` reserved for TECHNOLOGY; `PROC-NN` / `CAP-NN` for PROCESS /
  CAPABILITY (rubric v1.3 §5B). Registry: `LANE_NAMING_CENSUS_v0.md` (incl. 31 MIXED
  adjudications with justifications).
- **Applied:** 102 renames (C1 18 · C2 37 · C3 47), ~1.855 downstream references via
  single-pass `scripts/rename_lane_ids.py`; zero leftovers; 3 gates PASS; C1 xlsx
  regenerated; catalogs bumped.
- **Lane counts:** C1 T40/P17/C1 · C2 T36/P27/C10 · C3 T46/P40/C7.
- **Next (deferred):** lane artefacts (process models, capability cards) remain open —
  see ledger §2/§3.

---

## 4D. PHASE 3 PRODUCT-FIRST — partial closure (2026-09-05)

- **OWASP threat×flow (item 6)**: Case_02 `Doc28_Risk_Analysis.md` §5 and Case_03
  `Doc29_Risk_Analysis.md` §4 gain a new `Threat × Flow matrix` sub-section. Columns:
  Threat ID × Actor · Asset/Trust Boundary · Flow/Direction · STRIDE · ASVS/SAMM anchor ·
  CR/BPR · Notes. Anchored via ALT-ANCHOR §3 to the frozen referentials under
  `CONTROLS/OWASP_ASVS/` and `CONTROLS/OWASP_SAMM/`. 10 rows per case. 3 gates PASS.
- **Volere FR/NFR pilot (item 7)**: Case_02 `Doc29_Functional_Requirements.md` gains a
  `Fit Criterion` column with measurable thresholds. 6 FRs in operator-aligned topics
  + 1 repeatability (FR-72, AI domain) received Fit Criteria. Schema proven on a
  second domain. **25 orphan FRs still pending** (F5-C2-01 HIGH) → follow-on wave.
- **P7 Briefing Pack (items 1–4)**: `00_METHODOLOGY/validation/P7_BRIEFING_PACK_2026-09-05.md`
  — 4 items (OBL-D-06.2-001 / verify_rich FAILs / D-07.2 coverage / phantom refs) with
  A/B/C options and recommendations. Human decisions pending.
- **Out of scope (per user)**: ontologies, dashboards/folios, realisation_class tag waves C2/C3,
  KG reflection.

---

## 4C. ALT-ANCHOR CAMPAIGN (2026-09-05)

- **What:** the `UNMAPPED_*` marker family is RETIRED; rule elements without a PF/CSF
  subcategory are now anchored to sibling referentials via `ALT-ANCHOR (ref1; ref2; …)`
  (terminal `NO-ANALOGUE` when none cover). Frozen referential set: NIST SP 800-53r5 ·
  NIST SSDF (SP 800-218) · OWASP ASVS 4.0.3 · OWASP SAMM v2 · ISO 27002:2022 (last
  resort). Spec: `00_METHODOLOGY/ALT_ANCHOR_CRITERION.md` v1.0; sources:
  `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/{NIST_80053R5,NIST_SSDF,OWASP_ASVS,OWASP_SAMM,NIST_CSF_2.0}/`.
- **Applied:** Case_01/02/03 P2 (and C2/C3 P3 NIST_ANCHORS.md) — UNMAPPED_PF/CSF
  occurrences all replaced by ALT-ANCHOR (C1 48 → 0, C2 62 → 0, C3 107 → 0).
  Generator `scripts/build_alt_anchor_columns.py` injects the 800-53r5 column in the
  three matrices from the PF JSON crosswalks (30 + 38 + 38 rows; idempotent).
- **Gates:** all three `check_unmapped.py` upgraded to v0.4 — RETIRED-token hard check
  + ALT-ANCHOR anchor-set validation against frozen sources + CSF 2.0 hard check (was
  WARN-only in C2/C3). All three PASS. CSF 1.1 remnants in C2/C3 waivers documented.
- **Orphans inventory:** C3 10 OBL orphans — 9 MITIGADO (BPR sibling), 1 GAP
  (`OBL-D-06.2-001`) → P7. C2 14 PO + 40 SO orphans LEGIT (informational duplicates;
  audit dedup improvement deferred).
- **Deferred (per P7 documents-only + scope decisions):** ontologies, dashboards,
  data mirrors, KG reflection, CSF 1.1 → 2.0 normalisation, C2 audit dedup.

---

## 4B. REALIZATION-CLASS CAMPAIGN (2026-09-05)

- **What:** new mandatory Phase 2 rule attribute `realization_class` {TECHNOLOGY, PROCESS, CAPABILITY} (+ optional secondary) — methodology rubric `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` v1.2, corr-008 registered (`00_METHODOLOGY/AGENTS.md` v2.2). Bridges Phase 2 rules to the Phase 3 node-track triad and the maturity model (CAPABILITY ↔ Scale A / EvidenceItem).
- **Applied:** Case_01 only — 46 rules tagged in Doc18 (fields 25/26, Anexo A, Anexo D) + `control_set.yaml` + `12_Rules_Catalog.xlsx`; generator v1.1 regeneration-stable. Final distribution: T17 / P23 / C6, 9 secondaries. Validator blind audit 41/46 → 2 adjudicated fixes. Gates PASS unchanged.
- **Deferred (documents-only scope, human decision 2026-09-05):** `phase2_ontology.yaml` application; dashboards + `data/` mirrors regeneration; KG reflection; C2/C3 waves; Phase 3 realization lanes.

---

## 5. PENDING CHANGES

| Priority | Change | Affected Cases | Description |
|----------|--------|----------------|-------------|
| HIGH | Phase 3 v2.0 Restructure | Case_02, Case_03 | Apply same Class Model v2.0 alignment (relationships, variability, stop conditions, track enum, mitigation loop) |
| MEDIUM | Lint Phase 2 docs | Case_02, Case_03 | Run new per-document lint scripts |
| LOW | Lint Automation | All | Add pre-commit lint hooks |

---

## 6. DOCUMENT LOCATIONS

| Document | Path |
|----------|------|
| **Global Project State** | `02_CASES/GLOBAL_PROJECT_STATE.md` |
| **Central Change Log** | `02_CASES/CHANGE_LOG_CENTRAL.md` |
| **Session Handoff** | `02_CASES/SESSION_HANDOFF.md` |
| **Case 01 State** | `02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md` |
| **Case 02 State** | `02_CASES/Case_02_SecureBorder_Solutions/PROJECT_STATE.md` |
| **Case 03 State** | `02_CASES/Case_03_OmniBank_Financial/PROJECT_STATE.md` |
| **Restructure Summary** | `04_ADMIN/RESTRUCTURE_SUMMARY.md` |
| **Use Cases Review** | `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/13_Use_Cases_Review_Report.md` |

---

## 7. CONTACTS & OWNERS

| Role | Responsibility | Contact |
|------|----------------|---------|
| AEGIS Methodology Lead | Overall implementation | aegis-lead@methodology.pt |
| Compliance Lead | Phase 1-2 implementation | compliance@methodology.pt |
| Security Architect | Phase 2-3 technical review | security-arch@methodology.pt |
| Tooling Lead | Linting and scripts | tools@methodology.pt |

---

**Document Version:** 6.3 (Phase 3 RICH Mode re-verification per VALIDATOR_SPRINT5 v2 — Case_01 PASS_WITH_FINDINGS recorded)
**Last Reviewed:** 2026-08-24
**Next Review:** Phase 3 v2.0 Restructure (Case_02, Case_03); Phase 3 RICH Mode commitments + follow-on contract sprint (Case_01)

---

## 8. PHASE 3 RICH MODE — VALIDATION LOG (per case)

### 8.1 Case_01 TinyTask SaaS — Validator verdict: **PASS_WITH_FINDINGS v2 (2026-08-24 worktree re-verification)**

> Validator v2 corrects v1 (which incorrectly concluded FAIL by checking only `git log`). v2 verifies the **worktree** (untracked files = deliverable per AGENTS.md Branch Policy). v1 findings F-V-1..8 are INVALIDATED.

| Layer | Claimed | Validator v2 verified | State |
|---|---|---|---|
| Cards (UC=35/FR=30/NFR=46/DN=30/NODE=49/GATE=30/RISK=10/THR=38/SYNTH=8) | 276 | **276** | PASS |
| 17-field cards / 12-field cards | 121 / 155 | **121 / 155** | PASS |
| Cells (17×121 + 12×155) | 3,917 | **3,917** | PASS |
| KG EXTRACTED chains spot-check | ≥10 PASS | 12 spot-checked, 10 PASS + 2 INFERRED (F-S2-01 / CH-13 cross-domain) | PASS |
| Rich lint runner | 0 FAILs | 6/7 PASS, 1 FAIL (Doc 13 §-naming; F-S5-01) — documented expected gap | PASS_WITH_FINDINGS |
| Legacy lint regression | none | 7/7 PASS (no regression) | PASS |
| `22_Traceability_Matrix.xlsx` | 10 sheets | **10 sheets, 330 rows** | PASS |
| `18_Functional_Tree.drawio` | non-empty | **19,698 bytes (42 vertices, 41 edges)** | PASS |
| Enum freeze (46 rules + 31 goals) | match | **match** (Doc 11/10 cross-verified) | PASS |
| Orphan CR-D refs as findings | 7 (F-S1-01..07) | 7 (all tagged in Doc 14/16 cards) | PASS |
| F-register status | mostly closed | F-00a..F-00f RESOLVED/CLOSED, F-S1-01..07 informatively referenced, **F-S1-09 OPEN** (KG re-run needed) | PASS_WITH_FINDINGS |
| Sprint 5 verdict | PASS_WITH_FINDINGS | **PASS_WITH_FINDINGS** | PASS |
| Legacy diff (`03_PHASE3/`, `02_PHASE2/`, `01_PHASE1/`, PREPROCESSING) | empty | **empty** | PASS |

Source: `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/validation/VALIDATOR_SPRINT5.md` v2.0 + `02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md` §9.

### 8.2 Case_02 / Case_03 — Phase 3 RICH Mode

Not started at 2026-08-24. No `03_PHASE3_DECOMPOSITION_RICH/` folder exists for either case. Recommended for follow-on contracts after Case_01 orchestrator commits + follow-on KG re-run (F-S1-09).
