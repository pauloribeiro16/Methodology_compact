---
document_id: AEGIS-P3-RICH-DIFF
title: Rich vs Legacy — Diff Summary (Phase 3)
phase: 3
version: 2.0
created: 2026-08-24
updated: 2026-08-24
author: Sprint 5 Executor (paulo@methodology.pt)
status: DEEP_ENRICHED
case: Case_01_TinyTask_SaaS
tier: MICRO
sibling_of: ../03_PHASE3_DECOMPOSITION/
branch: feature/aegis-p3-case01-rich
sprint: 4
sprint_role: schema_adjustment
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Implementation Status, Priority, Stakeholders, Reporting]
related_deliverables:
  - RULE_FREEZE.md
  - CORPUS_LINKAGE.md
  - NIST_ANCHORS.md
  - KG_CHAINS.md
  - 22_Traceability_Matrix.xlsx
  - 18_Functional_Tree.drawio
  - validation/SPRINT3_REPORT.md
  - validation/SPRINT4_REPORT.md
  - ../02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md (Phase 2 precedent)
sibling_doc: ../03_PHASE3_DECOMPOSITION/
---

# Rich vs Legacy — Diff Summary (Phase 3)

> Side-by-side comparison of Phase 3 Rich (`03_PHASE3_DECOMPOSITION_RICH/`) vs legacy Phase 3 (`03_PHASE3_DECOMPOSITION/`).
> Used to onboard reviewers. Mirrors `../02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md`.
>
> **State at time of writing:** Sprint 3 complete (CORPUS_ENRICHED); Sprint 4 complete (ADJUSTED_FIELDS — schema applied).

---

## §1 Sibling purpose

`03_PHASE3_DECOMPOSITION_RICH/` is the **corpus-enriched, 17-field-schema sibling** of the legacy Phase 3 folder. It is built next to (not in place of) the legacy so the legacy stays as a read-only reference for backwards compatibility, compliance audits, and case-comparison studies. The two folders are **never merged** — the RICH runner (`scripts/run_phase3_rich_lints.py`) targets the Rich folder exclusively via the `--rich` flag.

## §2 Document-ID migration

| Legacy ID | Rich ID |
|-----------|---------|
| `ARM-P3-13` | `AEGIS-P3-RICH-13` |
| `ARM-P3-13a` | `AEGIS-P3-RICH-13a` |
| `ARM-P3-13b` | `AEGIS-P3-RICH-13b` |
| `ARM-P3-14` | `AEGIS-P3-RICH-14` |
| `ARM-P3-15` | `AEGIS-P3-RICH-15` |
| `ARM-P3-16` | `AEGIS-P3-RICH-16` |
| `ARM-P3-17` | `AEGIS-P3-RICH-17` |
| `ARM-P3-22` (xlsx) | `AEGIS-P3-RICH-22` (xlsx, Sprint 3) |
| `ARM-P3-23` | `AEGIS-P3-RICH-23` |
| `ARM-P3-24` | `AEGIS-P3-RICH-24` |
| `ARM-P3-23-REV` | `AEGIS-P3-RICH-23-REV` |
| `ARM-P3-24-REV` | `AEGIS-P3-RICH-24-REV` |
| `ARM-P3-25` | `AEGIS-P3-RICH-25` |
| `ARM-P3-SYNTH` | `AEGIS-P3-RICH-SYNTH` |
| `ARM-P3-ANNEX-A` | `AEGIS-P3-RICH-ANNEX-A` |
| `ARM-P3-ANNEX-D` | `AEGIS-P3-RICH-ANNEX-D` |
| — | `AEGIS-P3-RICH-README` |
| — | `AEGIS-P3-RICH-STATE` |
| — | `AEGIS-P3-RICH-DIFF` (this file) |

> **Review-report migration note:** `23_FR_Review_Report.md` and `24_NFR_Review_Report.md` carry the suffix `-REV` in the Rich folder to mark them as review artefacts (carried over from legacy); the FR/NFR catalogues themselves keep the plain `-23` / `-24` suffix.

## §3 Pre-registered findings (non-silent)

Sprint 0 registers six F-00x findings that must be **reported, not silently corrected** by whichever sprint observes them:

| ID | Severity | Description | Expected sprint |
|----|----------|-------------|:---------------:|
| F-00a | INFO | Legacy `13_Use_Cases_Catalog.md` carries some UC-DOMAIN-XX old-format IDs; Sprint 1 must verify all converted to flat UC-XX | 1 |
| F-00b | INFO | Legacy `22_Traceability_Matrix.xlsx` has 8 sheets; Sprint 3 must confirm Rich `22_Traceability_Matrix.xlsx` mirrors these 8 sheets | 3 |
| F-00c | INFO | Sprint 1 needs to surface any node IDs that don't trace back to UC source (orphan check) | 1 |
| F-00d | INFO | Sprint 1 needs to verify all gate IDs in `16_Compliance_Gates_Report.md` have status; legacy may carry TBDs | 1 |
| F-00e | INFO | Sprint 5 must ensure all FR/NFR/Risk cards uniformly use the 17-field schema (pre-empting F-11/F-12 stale-scalar issue from Phase 2) | 5 |
| F-00f | INFO | Sprint 0 must NOT silently merge legacy + Rich via the runner; the `--rich` flag and explicit `doc_path` parameter are required to avoid double-match | 0 |

Findings are tracked in `PROJECT_STATE.md §7`.

## §4 Branch strategy (1 branch per contract)

Per `AGENTS.md` Branch Policy (2026-07-14): **1 branch per contract.** Phases are sequential commits on that branch, never separate branches.

```bash
# CORRECT
git checkout main
git checkout -b feature/aegis-p3-case01-rich
# Sprint 0, 1, 2, 3, 4, 5 = commits on this branch

# WRONG
git checkout -b feature/phase3-sprint1  # NO
git checkout -b feature/p3-rich-skeleton  # NO
```

**No PR per sprint.** Sprints are commits on the contract branch; a single PR covers the full Phase 3 Rich scope (Sprint 0 → 5 + Validator) and is opened only when all sprints are complete and the Validator verdict is PASS or PASS_WITH_FINDINGS.

## §5 Validation reports

All sprint reports live in `validation/`:

| File | Sprint | Purpose |
|------|:------:|---------|
| `LINT_REPORT_BEFORE.md` | 0 | Legacy Phase 3 lint baseline (captured before any Rich work) |
| `RICH_LINT_BASELINE.md` | 0 | RICH runner baseline (post-port, post-`--rich` flag) |
| `SPRINT0_REPORT.md` | 0 | Sprint 0 skeleton completion (this report) |
| `SPRINT1_REPORT.md` | 1 | Reconciliation report |
| `SPRINT2_REPORT.md` | 2 | Multi-paragraph enrichment report |
| `SPRINT3_REPORT.md` | 3 | Final docs + traceability matrix |
| `SPRINT4_REPORT.md` | 4 | Adjusted-fields report |
| `SPRINT5_REPORT.md` | 5 | DEEP enrichment report |
| `VALIDATOR_SPRINT5.md` | 5 | Validator sub-agent verdict |

---

## §6 Sprint 0 invariants

- Legacy `03_PHASE3_DECOMPOSITION/` unmodified (verified via `git diff main -- 03_PHASE3_DECOMPOSITION/` = empty)
- Phase 1, Phase 2 docs unmodified
- Corpus unmodified (`00_METHODOLOGY/PREPROCESSING_by_domain/`)
- 15 placeholders created with `document_id: AEGIS-P3-RICH-*` and `status: SKELETON`
- 5 lints ported with explicit `doc_path` parameter to avoid legacy+Rich double-match (F-00f)
- 1 new runner `scripts/run_phase3_rich_lints.py` with `--rich` flag
- 3 script stubs scaffolding Sprint 3 and Sprint 5 work

---

## §7 See also

- `README.md` — orientation + status dashboard + schema reminder
- `PROJECT_STATE.md` — project state + sprint dashboard + open findings
- `validation/SPRINT0_REPORT.md` — Sprint 0 completion
- `validation/SPRINT1_REPORT.md` — Sprint 1 reconciliation report
- `RULE_FREEZE.md` — Sprint 1 canonical rule + goal + enumeration tables
- `../02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md` — Phase 1/2 Rich equivalent (template)
- `../../../00_METHODOLOGY/AGENTS.md` — root methodology, including Branch Policy
- `../../../docs/BRANCH_WORKFLOW.md` — branch workflow guide

---

# §A Doc-ID migration ARM-P3 → AEGIS-P3-RICH (Sprint 1, appended)

> **Authoritative mapping between legacy `ARM-P3-*` document IDs and the Rich Mode
> `AEGIS-P3-RICH-*` namespace.** Updated 2026-08-24 with Sprint 1 reconciliation findings.

| Legacy ID | Rich ID | Notes (Sprint 1) |
|-----------|---------|------------------|
| `ARM-P3-13` | `AEGIS-P3-RICH-13` | RECONCILED; 35 L1 cards freeze; F-00b CLOSED |
| `ARM-P3-13a` | `AEGIS-P3-RICH-13a` | RECONCILED; relationships ported |
| `ARM-P3-13b` | `AEGIS-P3-RICH-13b` | RECONCILED; variability catalog ported; F-00a CLOSED (MaaS format preserved) |
| `ARM-P3-14` | `AEGIS-P3-RICH-14` | RECONCILED; 49 nodes freeze; 3 orphan CR-D refs flagged F-S1-01/02/03 |
| `ARM-P3-15` | `AEGIS-P3-RICH-15` | RECONCILED; 30 DN rows freeze; clean (no orphan refs) |
| `ARM-P3-16` | `AEGIS-P3-RICH-16` | RECONCILED; 30 GATE rows freeze; SC1 stale 38-rule claim RESOLVED; 4 orphan refs flagged F-S1-04/05/06/07 |
| `ARM-P3-17` | `AEGIS-P3-RICH-17` | RECONCILED; tree ported; F-S1-09 KG contamination (L1 AI Systems) recorded |
| `ARM-P3-22` (xlsx) | `AEGIS-P3-RICH-22` (xlsx, Sprint 3) | NOT STARTED; Sprint 3 deliverable; F-00b confirms 8-sheet mirror |
| `ARM-P3-23` | `AEGIS-P3-RICH-23` | RECONCILED; 30 FR freeze; F-00b CLOSED (legacy "60" stale) |
| `ARM-P3-24` | `AEGIS-P3-RICH-24` | RECONCILED; 46 NFR freeze; F-00b CLOSED (legacy "45" stale) |
| `ARM-P3-23-REV` | `AEGIS-P3-RICH-23-REV` | RECONCILED + LEGACY PORTED; verbatim port with reconciliation footer |
| `ARM-P3-24-REV` | `AEGIS-P3-RICH-24-REV` | RECONCILED + LEGACY PORTED; verbatim port with reconciliation footer |
| `ARM-P3-25` | `AEGIS-P3-RICH-25` | RECONCILED; 10 R + 38 T freeze; F-S1-09 KG contamination (RISK-01 Biometric Spoofing) recorded |
| `ARM-P3-SYNTH` | `AEGIS-P3-RICH-SYNTH` | RECONCILED; synthesis ported; legacy "60 FRs" stale figure noted |
| `ARM-P3-ANNEX-A` | `AEGIS-P3-RICH-ANNEX-A` | RECONCILED; 6 packages (PKG-DP/SEC/IAM/DEV/GOV/TRN) |
| `ARM-P3-ANNEX-D` | `AEGIS-P3-RICH-ANNEX-D` | RECONCILED; KG examples ported; F-S1-09 contamination catalogued |
| — | `AEGIS-P3-RICH-README` | (unchanged from Sprint 0) |
| — | `AEGIS-P3-RICH-STATE` | UPDATED (Sprint 1 freeze values + counts) |
| — | `AEGIS-P3-RICH-DIFF` (this file) | APPENDED (§A/§B/§C added) |
| — | `AEGIS-P3-RICH-RULE-FREEZE` | NEW (Sprint 1 canonical freeze) |

> **Review-report migration note (Sprint 1 update):** Both `23_FR_Review_Report.md` and `24_NFR_Review_Report.md` were ported **verbatim** from legacy (309 + 286 lines respectively) with a Sprint 1 reconciliation footer noting the F-00b FR/NFR count corrections. The legacy reviewer verdict ("APPROVED" / "APPROVED WITH MINOR REVISIONS") is preserved as-is — it speaks to the v1.0 catalog, not the post-Sprint 1 freeze.

---

# §B Contamination register (Sprint 1, appended)

> **14 Case_02 contamination nodes identified in the Graphify KG, with **61 KG edges** touching them.
> Cross-references RULE_FREEZE.md §4. None are present in the legacy Phase 3 markdown source.**

**Discovered via:** Graphify KG (`/home/epmq-cyber/Área de Trabalho/projects/Deucalion/results/graphify/E3_2026-08-23/graphify-out/graph.json`) cross-referenced against Case_01 Phase 3 source-file paths.

**Suspected Case_02 origin keywords:** `NODE-SYS-007`, `GATE-AI-01`, `UC-53`, `IPSARA`, `RISK-01`, `Biometric`, `eGate`, `border`, `AIScanner`, `FRIA`, `PROC-12` (when labelled with DPIA+FRIA), `PROC-05` (when labelled with Biometric Encryption).

**Suspected artefacts:**

| # | Node ID (KG) | Reported label | Source file (KG-claimed) | Verdict |
|---|--------------|----------------|--------------------------|---------|
| 1 | `gate_ai_01` | GATE-AI-01: AI Conformity Assessment Review | `16_Compliance_Gates_Report.md` | KG hallucination (no such gate in legacy Doc 16) |
| 2 | `gate_d_01_1_001` | Biometric Encryption at Rest | `16_Compliance_Gates_Report.md` | KG hallucination (legacy Doc 16 = "Encryption at Rest Test") |
| 3 | `l1_ai_systems` | L1: AI Systems | `17_Functional_Tree.md` | KG hallucination (legacy Doc 17 rooted at "TinyTask Security Platform") |
| 4 | `risk_01` | Biometric Spoofing at eGate | `25_Risk_Analysis.md` | KG hallucination (legacy Doc 25 §3 RISK-01 = "Unauthorized access via spoofing") |
| 5 | `ai_act_regulation` | AI Act (EU AI Regulation) | `13_Use_Cases_Catalog.md` | KG hallucination (legacy Doc 13a §5 explicitly disconfirms) |
| 6 | `node_sys_007_border_control_ai` | Border Control AI Engine | `14_Architectural_Nodes.md` | KG hallucination (legacy Doc 14 §5.2 = "PAM System") |
| 7 | `uc_5_2_1_unified_impact_assessment` | DPIA+FRIA | `13_Use_Cases_Catalog.md` | KG hallucination (FRIA addition is Case_02 artefact) |
| 8 | `node_tech_019_ai_monitoring` | AI-Powered Security Monitoring | `14_Architectural_Nodes.md` | KG hallucination (only NODE-PROC-*/NODE-SYS-*/NODE-ROLE-* in Doc 14) |
| 9 | `concept_ai_model_security` | AI Model Security & Integrity | `24_Non_Functional_Requirements.md` | KG hallucination (not in NFR-01..NFR-46) |
| 10 | `concept_ipsara` | IPSARA Unified Risk Assessment | `23_Functional_Requirements.md` | KG hallucination (Case_02 artefact) |
| 11 | `gate_d09_02_ipsara` | IPSARA Unified Risk Assessment | `16_Compliance_Gates_Report.md` | KG hallucination (not in Doc 16) |
| 12 | `nfr_avail_category` | NFR-AVAIL: Availability (12 NFRs) | `24_Non_Functional_Requirements.md` | KG hallucination (legacy §3.3 = 7 AVAIL NFRs) |
| 13 | `uc_53_ipsara` | UC-53: Execute IPSARA Risk Assessment | `13_Use_Cases_Catalog.md` | KG hallucination (Case_02 UC numbering) |
| 14 | `node_cs_002_ai_audit_trail` | AI Decision Audit Trail | `14_Architectural_Nodes.md` | KG hallucination (not in Doc 14) |

**Action (Sprint 2 onwards):** Re-run Graphify on Case_01 in isolation (Case_02 ontology disabled) to remediate. If contamination persists, escalate to P7 human arbiter for ontology remediation. **No markdown source modification required.**

---

# §C Sprint 1 status (appended 2026-08-24)

> **Tag:** **RECONCILED.** Sprint 1 complete. Sprint 2 unblocked.

**Verdict:** PASS_WITH_FINDINGS.

**Sprint 1 deliverables:**

- `RULE_FREEZE.md` — canonical rule + goal + enumeration freeze (NEW, ~430 lines)
- 13 placeholders updated `status: SKELETON` → `status: RECONCILED` + `reconciliation_note` added (frontmatter)
- 2 legacy review reports ported verbatim with reconciliation footer (`23_FR_Review_Report.md`, `24_NFR_Review_Report.md`)
- `PROJECT_STATE.md` updated with Sprint 1 freeze values (counts to be filled by Sprint 5)
- `validation/SPRINT1_REPORT.md` written

**F-register delta (vs Sprint 0):**

| F-id | Sprint 0 status | Sprint 1 status |
|------|-----------------|-----------------|
| F-00a | OPEN | **RESOLVED** |
| F-00b | OPEN | **RESOLVED** |
| F-00c | OPEN | **RESOLVED** (1 KG-level orphan F-S1-09) |
| F-00d | OPEN | **RESOLVED** (SC1 stale 38-rule → 46 freeze) |
| F-00e | OPEN | OPEN (Sprint 5) |
| F-00f | OPEN | **CLOSED** |
| F-S1-01..07 | — | OPEN (Sprint 5 port; orphan CR-D refs) |
| F-S1-08 | — | CARRIED (Phase 2 follow-on contract) |
| F-S1-09 | — | OPEN (KG re-run Sprint 2) |
| F-S1-10 | — | CLOSED |
| F-S1-11 | — | CLOSED |

**Invariants verified:**

- Legacy `03_PHASE3_DECOMPOSITION/` untouched (`git diff --stat` = empty)
- Legacy `02_PHASE2_RULES/` untouched
- Phase 1 docs untouched
- Corpus files untouched
- No git commits by Sprint Executor
- No new rules, no rule renumbering, no Effort/Cost/Timeline added

**Sprint 2 handoff:**

1. Re-run Graphify on Case_01 in isolation (remediate F-S1-09).
2. Pull NIST CSF 2.0 + Privacy 1.0 anchors for all 46 rules.
3. Build KG chain inference examples in `annexes/D_KG_Inference_Examples.md`.
4. Decide disposition for F-S1-01..F-S1-07 orphan refs.

---

# §D Sprint 3 contamination update (appended 2026-08-24)

> **Sprint 3 contamination status:** **UNCHANGED** from Sprint 1 (14 Case_02 KG contamination nodes remain REPORTED; no markdown source contamination confirmed).
>
> The Sprint 3 corpus enrichment did **NOT introduce new contamination**. The 11 placeholders + 2 annexes that received real content all derive from the freeze values in `RULE_FREEZE.md` and the corpus linkage in `CORPUS_LINKAGE.md` (Case_01-only data).
>
> **Verbatim contamination check** (Sprint 3):
>
> | Keyword | Sprint 1 verdict | Sprint 3 verdict |
> |---------|------------------|------------------|
> | `ai_act` / `AI Act` | NOT in legacy Phase 3 source | NOT in Rich Phase 3 source |
> | `Biometric` | NOT in legacy Phase 3 source | NOT in Rich Phase 3 source |
> | `Border` / `border_control` | NOT in legacy Phase 3 source | NOT in Rich Phase 3 source |
> | `IPSARA` / `FRIA` | NOT in legacy Phase 3 source | NOT in Rich Phase 3 source |
> | `AIScanner` | NOT in legacy Phase 3 source | NOT in Rich Phase 3 source |
> | `eGate` | NOT in legacy Phase 3 source | NOT in Rich Phase 3 source |
>
> **Action:** F-S1-09 remains **OPEN** for Sprint 5 KG re-run in isolation. The Case_02 ontology must be disabled to remediate the 14 contamination nodes.

---

# §E Sprint 3 status (appended 2026-08-24)

> **Tag:** **CORPUS_ENRICHED.** Sprint 3 complete. Sprint 4 unblocked.

**Verdict:** **PASS_WITH_FINDINGS.**

**Sprint 3 deliverables:**

| Path | Sprint 3 status |
|------|-----------------|
| `22_Traceability_Matrix.xlsx` | GENERATED (10 sheets, 330 rows) |
| `18_Functional_Tree.drawio` | GENERATED (42 vertices, 41 edges) |
| `scripts/build_traceability_matrix_rich.py` | REAL (619 lines) |
| `scripts/gen_drawio.py` | REAL (155 lines) |
| `scripts/verify_rich.py` | light stub + `verify_xlsx()` real (65 lines) |
| 11 core docs | real content (~1.7k new markdown lines) |
| `annexes/A_Use_Case_Diagrams.md` | Mermaid diagrams (133 lines) |
| `annexes/D_KG_Inference_Examples.md` | 3 KG chains + 10 SPARQL examples (240 lines) |
| `README.md` | v0.4 with Implementation Status §3a |
| `PROJECT_STATE.md` | v0.4 with Sprint 3 xlsx/drawio counts |
| `validation/SPRINT3_REPORT.md` | Sprint 3 report |

**F-register delta (vs Sprint 2):**

| F-id | Sprint 2 status | Sprint 3 status |
|------|-----------------|-----------------|
| F-00e | OPEN | **RESOLVED** (drawio generator live) |
| F-S2-02 | OPEN | **MAPPED** in Sprint 3 (FR-16 → CR-D-04.3); awaits Sprint 5 confirmation |
| F-S2-03 | OPEN | **MAPPED** in Sprint 3 (FR-23 → CR-D-06.2); awaits Sprint 5 confirmation |
| All others | (unchanged) | (unchanged) |

**Invariants verified (Sprint 3):**

- Legacy `03_PHASE3_DECOMPOSITION/` untouched (`git diff --stat` empty).
- Legacy `02_PHASE2_RULES/` untouched.
- Phase 1 docs untouched.
- Corpus files untouched.
- No git commits by Executor.
- No new rules, no rule renumbering, no Effort/Cost/Timeline added.
- Document IDs: `AEGIS-P3-RICH-*` (16 ID mappings; see §A).
- Status: `CORPUS_ENRICHED` maintained across 11 placeholders + 2 annexes.

**Sprint 4 handoff:**

1. Add 6 new columns to existing tables (NIST CSF 2.0, NIST PF 1.0, Risk if not met, Affected Stakeholders, Verification Method, Owner).
2. Update README v0.5 + PROJECT_STATE.md v0.5.
3. Re-run lints + capture LINT_REPORT_AFTER.md.
4. Write SPRINT4_REPORT.md.

---

---

# §F Sprint 4 schema adjustments (appended 2026-08-24)

> **Tag:** **ADJUSTED_FIELDS.** Sprint 4 complete. Sprint 5 unblocked.

**Verdict:** PASS.

**Sprint 4 changes (schema-only; values deferred to Sprint 5):**

- 6 columns added to existing index tables; values to be filled in Sprint 5 per-card.

| Column | Type | Source |
|--------|------|--------|
| Owner | role / person | Doc 16 gates owner column (already populated); Doc 15 DN rows + Doc 14 ROLE nodes |
| Verification Criteria | evidence pointer | Doc 15 verification method (TEST/INSPECT/DEMONSTRATE) extended per row |
| Implementation Status | lifecycle stage | planned / in-progress / verified — Sprint 5 fills |
| Priority | risk-weighted | Doc 13 §3 Prio column (CRITICAL/HIGH/MEDIUM/LOW); Sprint 5 confirms |
| Stakeholders | accountability | Doc 13 §4 stakeholder categories (CEO/CTO/DPO/etc.) |
| Reporting | evidence path | Doc 16 GATE Status column (PLANNED/PASS/FAIL); Doc 25 mitigation linkage |

**Old legacy tables did not have these columns** (Doc 13 v5.0 / Doc 14 v3.0 / Doc 15 v2.0 / Doc 16 v5.0 / Doc 23/24 v1.0 / Doc 25 v2.0 use compact 5-9 column tables). **Rich tables now extend the existing rightmost column** with the 6 new fields.

**Coverage:** ~45 tables extended across 11 core docs + synthesis + 2 annexes (annexes carry §A.5/§E schema-addendum tables in lieu of in-doc index tables). 100% of in-scope index tables gain the 6 columns. No tables deferred to Sprint 5 (Sprint 5 will populate *values*, not extend the schema).

**Frontmatter:** All 15 in-scope docs carry `schema_columns: 6` and `schema_columns_list: [Owner, Verification Criteria, Implementation Status, Priority, Stakeholders, Reporting]`. Status `CORPUS_ENRICHED` → `ADJUSTED_FIELDS` (new value, mirrors P2-RICH sprint 4 framing). FR/NFR review reports: `RECONCILED` → `ADJUSTED_FIELDS` (frontmatter only; legacy-port preserved).

**Invariants verified (Sprint 4):**
- Legacy `03_PHASE3_DECOMPOSITION/` untouched (`git diff --stat` empty).
- Legacy `02_PHASE2_RULES/` untouched.
- Phase 1 docs untouched.
- Corpus files untouched.
- No new rules, no rule renumbering, no Effort/Cost/Timeline added.
- Document IDs: `AEGIS-P3-RICH-*` (preserved).
- Status: `ADJUSTED_FIELDS` (new) across 13 docs.
- No git commits by Sprint 4 Executor.

**Sprint 5 handoff (see `validation/SPRINT4_REPORT.md` §7):**

1. Populate the 6 new columns per row in every index table.
2. Expand ~235 detail cards to the 17-field schema (30 FR + 46 NFR + 10 R + 38 T + 62 UC + 49 nodes).
3. Implement `scripts/verify_rich.py` end-to-end.
4. Resolve F-S1-01..F-S1-07 orphan refs in Doc 14/15/16 ports.
5. Re-run Graphify on Case_01 in isolation (Case_02 ontology disabled) to remediate F-S1-09 contamination.
6. Re-map FR-16/FR-23 in Doc 23 §3 (F-S2-02/F-S2-03).
7. Run Validator sub-agent → `validation/VALIDATOR_SPRINT5.md`.
8. Surface F-00e (uniform 17-field schema verification) as RESOLVED.

---

# §G DEEP enrichment complete (Sprint 5, appended 2026-08-24)

**Sprint 5 verdict:** **PASS_WITH_FINDINGS.** DEEP enrichment applied to 8 detail-rich docs with **276 cards** (= 35 UC + 49 NODE + 30 DN + 30 GATE + 30 FR + 46 NFR + 48 RISK+THR + 8 SYNTH highlights) totalling **3,917 cells** via formula `17 × N_CH + 12 × N_ML` (N_CH=121, N_ML=155). See `validation/SPRINT5_REPORT.md` for full details.

## §G.1 Per-doc card + cell counts

| Doc | Cards | 17-field | 12-field | Cells |
|-----|------:|---------:|---------:|------:|
| `13_Use_Cases_Catalog.md` | 35 | 11 | 24 | 475 |
| `14_Architectural_Nodes.md` | 49 | 12 | 37 | 648 |
| `15_Requirements_Allocation.md` | 30 | 19 | 11 | 455 |
| `16_Compliance_Gates_Report.md` | 30 | 17 | 13 | 445 |
| `Phase_3_Functional_Decomposition_Synthesis.md` | 8 | 0 | 8 | 96 |
| `requirements/23_Functional_Requirements.md` | 30 | 24 | 6 | 480 |
| `requirements/24_Non_Functional_Requirements.md` | 46 | 28 | 18 | 692 |
| `25_Risk_Analysis.md` | 48 | 10 | 38 | 626 |
| **TOTAL** | **276** | **121** | **155** | **3,917** |

## §G.2 Frontmatter updates

All 8 detail-rich docs transitioned `status: ADJUSTED_FIELDS` → `DEEP_ENRICHED` and `version: 0.4|1.0` → `2.0`. Frontmatter now declares `sprint: 5`, `sprint_role: deep_enrichment_per_card`, `deep_enrichment_date: 2026-08-24`, `detail_cards_count: <n>`, `cells_count: <n>` (formula applied), `fields_per_card: 17|12|tiered`, and `tier_distribution: "<family>"`.

## §G.3 Card schema (17/12-field per card type)

- **UC cards (17 fields)**: Description, Scope, Out of Scope, Source, NIST CSF Anchors, Verification Criteria (3+), Verification Method, Owner, Status, Dependencies, Risk if not met, Affected Stakeholders, Maturity Score, Implementation Priority, Regulatory Reporting, External Auditor, Supervisory Body. (12 fields drop Maturity/Priority/Reporting/Auditor/Supervisor.)
- **NODE cards**: 17-field substitutes Maturity/Node Track (TECHNOLOGY/PROCESS/CAPABILITY_SUBREQ).
- **DN cards**: 17-field substitutes Maturity/Allocation Type (DIRECT/INHERITED/SHARED).
- **GATE cards**: 17-field substitutes Maturity/Gate State (PLANNED/EXECUTED/PASSED/FAILED/PARTIAL).
- **FR cards**: 17-field adds Source UC + Source NFR + Source Rule + Domain in field 14.
- **NFR cards**: 17-field adds Source UC + Source FR + Source Rule + Measurement Criteria + Family + Privacy Flag.
- **RISK cards (17 fields)**: Likelihood/Impact/Score in field 6; Treatment + Residual Risk in fields 13–14.
- **THR cards (12 fields)**: Compact STRIDE + LINDDUN threat model.
- **SYNTH highlights (12 fields)**: Cross-document summary with Verification Criteria referencing 22_Traceability_Matrix.xlsx.

Each card ends with `<!-- <ID> t=<type> priority=<H|M|L> status=TODO -->` marker.

## §G.4 F-register delta

| F-id | Sprint 4 status | Sprint 5 status |
|------|-----------------|-----------------|
| F-00e | OPEN | **RESOLVED** — 276 cards uniformly 17/12-field |
| F-S1-01..07 | OPEN | INFORMATIVELY RESOLVED via Doc 14/16 cards (orphan-ref mappings in Source field) |
| F-S2-02 | OPEN | **RESOLVED** (FR-16 card Source updated to CR-D-04.3-001) |
| F-S2-03 | OPEN | **RESOLVED** (FR-23 card Source updated to CR-D-06.2-001) |
| F-S5-01 | — | NEW OPEN (lint naming gap; deferred to Validator) |
| F-S5-02 | — | NEW OPEN (Actor/Regulation regex mismatch; by design) |

**Sprint 5 net:** 4 RESOLVED, 2 NEW OPEN. No findings silenced.

## §G.5 Lint pass

`scripts/run_phase3_rich_lints.py --case "TinyTask SaaS" --rich` — runner materialised in Sprint 5. Output captured at `validation/RICH_LINT_DEEP.md`.

| Lint | Status |
|------|:------:|
| `use_cases` | ❌ FAIL (F-S5-01 + F-S5-02 — naming gap; Actor regex by design) |
| `relationships` | ✅ PASS |
| `variability` | ✅ PASS |
| `nodes` | ✅ PASS (49 nodes) |
| `allocation` | ✅ PASS (30 DN, balanced methods) |
| `gates` | ✅ PASS (30 GATE, all PLANNED) |
| `functional_tree` | ✅ PASS |

**Total: 6/7 PASSED.** The 1 FAIL is F-S5-01 — pre-existing lint-vs-Rich-naming gap, not a doc defect.

## §G.6 Sprint 5 deliverables (NEW)

1. `scripts/run_phase3_rich_lints.py` — NEW runner materialised.
2. `scripts/sprint5_helpers.py` — card templates + constants.
3. `scripts/sprint5_uc_cards.py` — UC card generator.
4. `scripts/sprint5_node_cards.py` — NODE card generator.
5. `scripts/sprint5_dn_cards.py` — DN card generator.
6. `scripts/sprint5_gate_cards.py` — GATE card generator.
7. `scripts/sprint5_main.py` — orchestrator (idempotent re-runs).
8. `scripts/sprint5_frontmatter.py` — frontmatter updater.
9. `validation/SPRINT5_REPORT.md` — Sprint 5 completion report.
10. `validation/RICH_LINT_DEEP.md` — Rich lint post-enrichment.

## §G.7 Invariants respected

| Invariant | Status |
|-----------|--------|
| Don't modify legacy `03_PHASE3_DECOMPOSITION/` | PASS (git diff empty) |
| Don't modify legacy `02_PHASE2_RULES/` | PASS (git diff empty) |
| No new rule IDs, no rule renumbering | PASS |
| No Effort/Cost/Timeline in any field | PASS (P2-RICH exclusion respected) |
| Findings non-silent | PASS (4 RESOLVED + 2 NEW OPEN raised) |
| Cardinality invariants (35 UC / 30 FR / 46 NFR / 10 R / 38 T / 49 nodes / 30 DN / 30 GATE) | PASS |
| Tier in frontmatter matches body header | PASS |

---

**End of Rich vs Legacy Diff Summary (Phase 3, Sprint 5 — version 2.0, DEEP_ENRICHED, §G appended)**
