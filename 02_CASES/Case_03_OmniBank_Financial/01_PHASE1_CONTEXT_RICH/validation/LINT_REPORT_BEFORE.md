---
document_id: AEGIS-P3-RICH-LINT-BEFORE
title: Lint Baseline Report — Pre-Rich Enrichment (Case_03)
phase: 1
version: 1.1
created: 2026-08-06
author: Sprint 0 Executor (lint-runner)
status: DRAFT
case: Case_03_OmniBank_Financial
target: 01_PHASE1_CONTEXT/ (legacy)
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
inactive_documented: []
tool: run_phase1_lints.py
tool_version: 2026-04-04 lints restructuring
sprint: 0
sprint_role: baseline_capture
---

# Lint Baseline — Pre-Rich Enrichment (Case_03)

> Snapshot of Phase 1 lint state BEFORE Sprint 1 reconciliation.
> Generated 2026-08-06 by Sprint 0 Executor against `01_PHASE1_CONTEXT/`.
>
> **Two captures are recorded below:**
> 1. **§A Legacy-only baseline** (run before Sprint 0 placeholders were created)
> 2. **§B Post-Sprint-0-skeleton state** (run after the 14 placeholders were written)
>
> The legacy-only baseline (§A) is the authoritative "Pre-Rich Enrichment" snapshot. The post-skeleton state (§B) shows the Sprint 0 hand-off: which lints now succeed (Doc 06 placeholder resolved cross-doc consistency) and which now fail (template compliance — placeholders don't match canonical section names).

## Summary

| Lint | §A Legacy-only | §B Post-skeleton | Errors (A) | Warns (A) | Errors (B) | Warns (B) |
|------|----------------|------------------|-----------:|----------:|-----------:|----------:|
| `run_phase1_lints.py` (orchestrator) | **PARTIAL FAIL** | **PARTIAL FAIL** | 1 | 29 | 1 | 32 |
| `lint_company_context.py` | PASS | PASS | 0 | 1 | 0 | 1 |
| `lint_regulatory_mapping.py` | PASS | PASS | 0 | 1 | 0 | 1 |
| `lint_regulatory_references.py` (Anti-Hallucination) | PASS | PASS | 0 | 0 | 0 | 0 |
| `lint_regulatory_ground_truth.py` | PASS | PASS | 0 | 10 | 0 | 10 |
| `lint_cross_document_consistency.py` | **FAIL** | **PASS** | 1 | 0 | 0 | 0 |
| `lint_template_compliance.py` | PASS | **FAIL** | 0 | 17 | 30 | 20 |
| **TOTAL** | **5 / 6 PASS** | **5 / 6 PASS** | **1** | **29** | **30** | **32** |

**Headline:**
- §A: **5/6 lints PASS against the legacy `01_PHASE1_CONTEXT/` folder.** 1 lint FAILS (`lint_cross_document_consistency.py` — Doc 06 missing as `.md`).
- §B: After the Sprint 0 skeleton is in place, **the cross-doc consistency lint now PASSES** (the Doc 06 placeholder resolved it), but `lint_template_compliance.py` now FAILS because the placeholder `01_INTAKE_FORM.md` doesn't match the canonical 29-section Intake Form template. This is the expected behaviour (per Case_02 precedent): placeholders are stubs; Sprint 1+ fills them with real content matching templates.

## §A Legacy-only baseline (Pre-Sprint-0)

### A.1 Orchestrator (`run_phase1_lints.py`)

```
🔍 Phase 1 Lints — Case_03_OmniBank_Financial
📂 /home/epmq-cyber/Área de Trabalho/projects/Methodology-main/02_CASES/Case_03_OmniBank_Financial
============================================================

============================================================
📊 Summary: 5/6 passed
⚠️ 29 warning(s)
❌ 1 lint(s) failed
  Running: Company Context (38 questions)... ✅ PASSED
  Running: Regulatory Mapping... ✅ PASSED
  Running: Regulatory References (Anti-Hallucination)... ✅ PASSED
  Running: Regulatory Ground Truth... ✅ PASSED
  Running: Cross-Document Consistency... ❌ FAILED
  Running: Template Compliance... ✅ PASSED

📄 Reports generated:
   JSON: lints/reports/lint_report_phase1_20260806_164204.json
   Markdown: lints/reports/lint_report_phase1_20260806_164204.md
```

### A.2 `lint_cross_document_consistency.py` (FAIL — direct invocation)

```
Valid: False

Errors:
  ❌ Missing documents: 06_Clause_Mapping_Matrix

Metrics: {'doc04_found': True, 'doc05_found': True, 'doc06_found': False, 'doc07_found': True, 'applicable_regs_doc04': [], 'applicable_regs_doc05': [], 'clause_counts_doc05': {}, 'clause_counts_doc06': {}, 'coverage_counts_doc07': {}, 'gaps_found_doc07': 0, 'sole_authority_gaps_doc07': 0, 'consistency_checks_passed': 0, 'consistency_checks_total': 0}
```

**Root cause:** Case_03 stores Doc 06 as `06_Clause_Mapping_Matrix.ods` + `.xlsx` only — there is no `.md` companion. The lint's `_find_doc()` glob returns empty for `06_Clause_Mapping_Matrix` because it searches for `.md`. (Sprint 0 placeholder `06_Clause_Mapping_Matrix.md` resolves this.)

### A.3 Per-Lint Details

#### 1. `lint_company_context.py` — PASS (1 warn)

| Document | Warning |
|----------|---------|
| `04_Company_Context_Assessment.md` | Layered format: 12/13 sections found |

- Format detected: `layered` (AEGIS Intake Form v2.0)
- Documents found: 1
- Compliance score: **92 / 100**
- 1 missing section — needs Section enumeration review.

#### 2. `lint_regulatory_mapping.py` — PASS (1 warn)

| Document | Warning |
|----------|---------|
| `02_Regulatory_Mapping_Master.md` | Only 1 security domains mentioned (expected coverage across multiple domains) |

- regulations_found: 5, regulations_expected: 5
- total_clauses_mapped: 74; total_rows: 11
- Note: most clause data lives in `06_Clause_Mapping_Matrix.xlsx` (Doc 06), not in `02_Regulatory_Mapping_Master.md`.

#### 3. `lint_regulatory_references.py` (Anti-Hallucination) — PASS (0 warn)

- Total references found: **729**
- Valid references: 729 / 729
- Invalid references: 0
- Documents scanned: 31
- Regulations checked: 7
- **The largest reference corpus among all 3 cases.** Consistent with Case_03 being MAX (38/38 sub-domains, 5/5 regs, 150 clauses).

#### 4. `lint_regulatory_ground_truth.py` — PASS (10 warns)

##### Tension ID warnings (5)

| Document | Warning |
|----------|---------|
| `07_Structured_Compliance_Matrix.md` | Tension ID 'T-001' not found in ground truth ontology |
| `07_Structured_Compliance_Matrix.md` | Tension ID 'T-002' not found in ground truth ontology |
| `07_Structured_Compliance_Matrix.md` | Tension ID 'T-003' not found in ground truth ontology |
| `07_Structured_Compliance_Matrix.md` | Tension ID 'T-004' not found in ground truth ontology |
| `04b_Security_Posture.md` | Tension ID 'T-002' not found in ground truth ontology |

##### Obligated Party warnings (5)

| Document | Obligated Party | Regulation | Issue |
|----------|-----------------|------------|-------|
| `02_Regulatory_Mapping_Master.md` | 'Rationale' | GDPR | Not in regulation's allowed set |
| `02_Regulatory_Mapping_Master.md` | 'MANUFACTURER' | GDPR | Not valid for GDPR |
| `02_Regulatory_Mapping_Master.md` | 'ESSENTIAL_ENTITY' | GDPR | Not valid for GDPR |
| `02_Regulatory_Mapping_Master.md` | 'FINANCIAL_ENTITY' | GDPR | Not valid for GDPR |
| `02_Regulatory_Mapping_Master.md` | 'PROVIDER' | CRA | Not valid for CRA |

**Metrics:**
- documents_scanned: 10
- clause_references_found: 36 (all valid)
- subdomain_references_found: 534 (all valid)
- timeline_mentions_found: 53 (all valid)
- obligated_party_checks: 9; obligated_party_invalid: 5
- normative_intensity_checks: 11; normative_intensity_mismatches: 0
- sole_authority_checks: 12; sole_authority_mismatches: 0

#### 5. `lint_cross_document_consistency.py` — **FAIL** (1 error)

| Error | Detail |
|-------|--------|
| ❌ Missing documents | `06_Clause_Mapping_Matrix` |

**Metrics (all zero because validation aborted):**
- doc04_found: True; doc05_found: True; doc06_found: **False**; doc07_found: True
- applicable_regs_doc04: []; applicable_regs_doc05: []
- clause_counts_doc05: {}; clause_counts_doc06: {}
- coverage_counts_doc07: {}
- gaps_found_doc07: 0; sole_authority_gaps_doc07: 0
- consistency_checks_passed: 0 / consistency_checks_total: 0

**Sprint 1 fix options:**
- (a) Generate a Markdown companion `06_Clause_Mapping_Matrix.md` (parallel to xlsx), summarising the 150 clauses
- (b) Update the lint's `_find_doc()` to accept `.xlsx` when `.md` is missing (case-specific)
- **(Sprint 0 placeholder created at `06_Clause_Mapping_Matrix.md` as (a).)** Sprint 1 fills the 150-row summary.

#### 6. `lint_template_compliance.py` — PASS (17 warns)

All warnings are **"Extra section not in template"** — case-specific extensions are detected as deviations from the canonical template. These are **by-design** in Case_03 because the MAX complexity case requires richer sections than the template prescribes.

| Document | Extra Sections |
|----------|----------------|
| `04_Company_Context_Assessment.md` | `10. OMNIBANK-SPECIFIC CONSIDERATIONS` |
| `05_Regulatory_Applicability.md` | `9. KEY OBSERVATIONS`, `5.3 Compliance Boundary Diagram` |
| `07_Structured_Compliance_Matrix.md` | `5.1 Regulatory Overlap Summary`, `5.2 Complementarity Opportunities`, `5.3 Conflict Classification (Structural vs Contextual)`, `5.4 Compound Event Scenarios`, `5.5 Strategic Tensions Identified`, `6.1 Business Goal Alignment`, `6.2 Resource Implications`, `6.3 Risk Profile Assessment`, `8. TRACEABILITY SUMMARY` |
| `01_Company_Context.md` (in 00_COMMON) | `CHANGELOG`, `MAXIMUM Complexity Tier`, `N. COMPANY CONTEXT CLASS INSTANTIATION`, `N+1. VERSION HISTORY` |
| — | `Document not found for pattern: 01_INTAKE_FORM` |

**Metrics:**
- documents_checked: 4
- documents_passed: 4 (passing despite extras — template compliance is non-blocking)
- total_sections_required: 88; total_sections_found: 80
- average_compliance_pct: 0.9

## §B Post-Sprint-0-skeleton state

After Sprint 0 wrote 14 placeholder docs in `01_PHASE1_CONTEXT_RICH/`, the orchestrator was re-run. The state changed:

### B.1 What changed

| Lint | §A status | §B status | Cause |
|------|-----------|-----------|-------|
| `lint_cross_document_consistency.py` | **FAIL** (missing Doc 06) | **PASS** | Sprint 0 created `06_Clause_Mapping_Matrix.md` placeholder. Doc 06 is now found. |
| `lint_template_compliance.py` | **PASS** (17 warns) | **FAIL** (30 errors + 20 warns) | Sprint 0 placeholder `01_INTAKE_FORM.md` has 4 sections (`Status`, `Reference (legacy)`, `Planned content`, `Cross-references to fill`) that don't match the canonical 29-section Intake Form template. Expected behaviour per Case_02 precedent. |

### B.2 Post-Skeleton Orchestrator Output

```
🔍 Phase 1 Lints — Case_03_OmniBank_Financial
📂 /home/epmq-cyber/Área de Trabalho/projects/Methodology-main/02_CASES/Case_03_OmniBank_Financial
============================================================

============================================================
📊 Summary: 5/6 passed
⚠️ 32 warning(s)
❌ 1 lint(s) failed
  Running: Company Context (38 questions)... ✅ PASSED
  Running: Regulatory Mapping... ✅ PASSED
  Running: Regulatory References (Anti-Hallucination)... ✅ PASSED
  Running: Regulatory Ground Truth... ✅ PASSED
  Running: Cross-Document Consistency... ✅ PASSED
  Running: Template Compliance... ❌ FAILED

📄 Reports generated:
   JSON: lints/reports/lint_report_phase1_20260806_165526.json
   Markdown: lints/reports/lint_report_phase1_20260806_165526.md
```

### B.3 Cross-Document Consistency — Now PASS

```
Metrics: {
  'doc04_found': True, 'doc05_found': True, 'doc06_found': True, 'doc07_found': True,
  'applicable_regs_doc04': ['GDPR', 'CRA', 'NIS2', 'DORA', 'AI_Act'],
  'applicable_regs_doc05': ['GDPR', 'CRA', 'NIS2', 'DORA', 'AI_Act'],
  'clause_counts_doc05': {'GDPR': 28, 'CRA': 26, 'NIS2': 29, 'DORA': 38},
  'clause_counts_doc06': {},
  'coverage_counts_doc07': {'SUBSTANTIVE': 0, 'PARTIAL': 0, 'NOT_ADDRESSED': 0},
  'gaps_found_doc07': 0, 'sole_authority_gaps_doc07': 0,
  'consistency_checks_passed': 7, 'consistency_checks_total': 7
}
```

**Note:** `clause_counts_doc06` is `{}` because the Sprint 0 placeholder has no clause table yet (Sprint 1 fills it). The 7 consistency checks pass because all 4 docs are found with consistent `applicable_regs` lists.

### B.4 Template Compliance — Now FAIL (expected)

```
❌ 01_INTAKE_FORM: Only 0% template compliance (0/29 required sections, 2 conditional sections skipped)
❌ 01_INTAKE_FORM: Missing required section: '1. PURPOSE'
❌ 01_INTAKE_FORM: Missing required section: '2. LAYER 0 — COMPANY PROFILE (Static Facts)'
... (29 missing sections total)
```

**Expected** (per Case_02 precedent): placeholders are stubs. Sprint 1 replaces `01_INTAKE_FORM.md` with the legacy copy + reconciliation notes. Sprint 2 adds corpus enrichment cells.

## Known Issues Catalog (Sprint 1 must address)

1. **I-C03-01 (RESOLVED by Sprint 0 placeholder):** `06_Clause_Mapping_Matrix.md` was missing → now exists as placeholder. Sprint 1 fills the 150-row summary from `.xlsx`.
2. **I-C03-02 (HIGH — ontology):** 5 tension IDs (T-001..T-004) used in legacy docs are not in the ground-truth ontology. **Fix:** register the 4 tensions from `09_Strategic_Tensions_Report.md` in the ontology, OR rephrase to existing tension IDs.
3. **I-C03-03 (HIGH — obligated_party):** 5 obligated_party values in `02_Regulatory_Mapping_Master.md` are not valid for the regulation they cite. **Fix:** correct the obligated_party field per row, OR update the schema to allow cross-regulation roles.
4. **I-C03-04 (MEDIUM — template extras in legacy):** 17 extra sections across 4 legacy docs are flagged as not in template. **Fix:** register the extras as canonical in the template, OR leave as warnings.
5. **I-C03-05 (MEDIUM — Doc 04 layered coverage):** 12/13 sections found in `04_Company_Context_Assessment.md`. **Fix:** fill the missing section.
6. **I-C03-06 (MEDIUM — Doc 05 mapping coverage):** Only 1 domain mentioned in `02_Regulatory_Mapping_Master.md`. **Fix:** most coverage lives in `06_Clause_Mapping_Matrix.xlsx`; the `.md` should reference the xlsx or be retired.
7. **I-C03-07 (LOW — Doc 04 §10):** "10. OMNIBANK-SPECIFIC CONSIDERATIONS" is a case-specific section. **Fix:** rename to canonical `## 10. Cross-Cutting Considerations` and refile.
8. **I-C03-08 (NEW — placeholder template compliance):** Sprint 0 placeholders don't match canonical templates (especially `01_INTAKE_FORM.md`). **Fix:** Sprint 1+ replaces placeholders with real content matching templates.

## Lint Output Raw Logs (Legacy-only baseline)

### `lint_company_context.py`

```
PASSED — Layered format: 12/13 sections found, compliance_score=92
```

### `lint_regulatory_mapping.py`

```
PASSED — regulations_found: 5, regulations_expected: 5
WARNING: 02_Regulatory_Mapping_Master.md: Only 1 security domains mentioned
```

### `lint_regulatory_references.py`

```
PASSED — 729/729 references valid (0 invalid), 31 docs scanned, 7 regs checked
```

### `lint_regulatory_ground_truth.py`

```
PASSED — 36 clause refs (all valid), 534 subdomain refs (all valid), 53 timeline refs (all valid)
WARNING: 4× tension T-001..T-004 in Doc 07 + 1× T-002 in Doc 04b not in ontology
WARNING: 5× obligated_party in 02_Regulatory_Mapping_Master.md not valid for cited regulation
```

### `lint_cross_document_consistency.py`

```
FAILED — Missing documents: 06_Clause_Mapping_Matrix
        doc06_found: False
        consistency_checks_passed: 0/0
```

### `lint_template_compliance.py`

```
PASSED — 4/4 docs passed, 88 sections required, 80 sections found (90% compliance)
WARNING: 17 "extra section not in template" (by-design for MAX complexity)
```

## Top Issues for Sprint 1

1. **T-001..T-004 not in ground-truth ontology** (4 instances in Doc 07 + 1 in Doc 04b) — Sprint 1 must register these tensions in the ontology or refactor docs.
2. **5 obligated_party values not in regulation's allowed set** — cross-regulation roles mapped incorrectly in `02_Regulatory_Mapping_Master.md`.
3. **06_Clause_Mapping_Matrix.md was missing** — Cross-Document Consistency lint FAILS; **Sprint 0 placeholder resolved this** (I-C03-01 → DONE).
4. **By-design: 17 Section extras** in 4 legacy docs (MAX complexity case-specific extensions).
5. **By-design: 1 missing Doc 04 section** (12/13 sections — needs the 13th).
6. **(NEW) Placeholder template compliance** — 14 Sprint 0 placeholders don't match canonical templates (especially `01_INTAKE_FORM.md`). Sprint 1+ replaces with real content.

## See also

- `../corpus_field_map.md` — corpus linkage blueprint for Sprint 2
- `../README.md` — Rich folder orientation + Sprint plan
- `00_METHODOLOGY/PHASE1_STRATEGY.md` — Phase 1 strategy
- `01_IMPLEMENTATION_TOOLS/lints/reports/lint_report_phase1_20260806_164204.md` — full orchestrator report (legacy-only baseline)
- `01_IMPLEMENTATION_TOOLS/lints/reports/lint_report_phase1_20260806_165526.md` — full orchestrator report (post-Sprint-0-skeleton)
