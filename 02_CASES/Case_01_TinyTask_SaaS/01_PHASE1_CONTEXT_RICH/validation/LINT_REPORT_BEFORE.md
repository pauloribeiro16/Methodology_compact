---
document_id: AEGIS-P1-RICH-LINT-BEFORE
title: Lint Baseline Report — Pre-Rich Enrichment
phase: 1
version: 1.0
created: 2026-08-06
author: Fase de Especificação 0 Executor (lint-runner)
status: DRAFT
case: Case_01_TinyTask_SaaS
target: 01_PHASE1_CONTEXT/ (legacy)
---

# Lint Baseline — Pre-Rich Enrichment

> Snapshot of Phase 1 lint state BEFORE Fase de Especificação 1 reconciliation.
> Used as the comparison baseline for `LINT_REPORT_AFTER_RECONCILE.md`.

## Run Metadata

- **Branch:** `feature/aegis-p1-case01-rich`
- **Working tree:** clean (only pre-existing untracked `.zcode/` and `00_METHODOLOGY/PREPROCESSING_by_domain/` — not touched)
- **Target case:** `02_CASES/Case_01_TinyTask_SaaS/`
- **Target phase dir:** `01_PHASE1_CONTEXT/` (legacy)
- **Orchestrator command:**
  `python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_01_TinyTask_SaaS" --output /tmp/opencode/lint_reports`
- **Python:** 3.13 with `openpyxl` (no venv)
- **Individual lint invocations:** 3 of 6 lints (`lint_company_context`, `lint_regulatory_mapping`, `lint_regulatory_references`) lack a `main()`/`argparse` CLI — they were invoked by importing their `lint_*` function and calling it on the resolved case path (raw output captured under "Lint Output Raw Logs").

## Summary

| Lint | Status | Errors | Warnings |
|------|--------|--------|----------|
| `run_phase1_lints.py` (orchestrator) | ✅ PASS | 0 | 31 |
| `lint_company_context.py` | ✅ PASS | 0 | 0 |
| `lint_cross_document_consistency.py` | ✅ PASS | 0 | 2 |
| `lint_regulatory_ground_truth.py` | ✅ PASS | 0 | 8 |
| `lint_regulatory_mapping.py` | ✅ PASS | 0 | 1 |
| `lint_regulatory_references.py` | ✅ PASS | 0 | 0 |
| `lint_template_compliance.py` | ✅ PASS | 0 | 20 |

**Aggregate:** 6/6 individual lints PASSED, 0 errors, 31 warnings total.

## Per-Lint Details

### `run_phase1_lints.py` (orchestrator)
- **Status:** ✅ PASS (6/6 passed)
- **Errors:** 0
- **Warnings:** 31 (orchestrator-level aggregate)
- **Top issues:**
  1. Dispatches to all 6 lints and aggregates status; emits no lint-specific issues itself.

### `lint_company_context.py`
- **Status:** ✅ PASS
- **Errors:** 0
- **Warnings:** 0
- **Top issues:** none
- **Metrics:**
  - `format_detected`: `layered`
  - `documents_found`: 1
  - `compliance_score`: 100

### `lint_cross_document_consistency.py`
- **Status:** ✅ PASS
- **Errors:** 0
- **Warnings:** 2
- **Top issues:**
  1. Doc 07 coverage matrix has 41 entries (expected 38)
  2. Sole authority gaps `{D-07.4, D-07.3, D-09.3, D-07.2}` from ontology not found in Doc 07 gaps table
- **Metrics:**
  - Doc 04/05/06/07 all found
  - Applicable regs (Doc 04): GDPR, CRA
  - Applicable regs (Doc 05): GDPR, CRA
  - Clause counts (Doc 05): GDPR=28, CRA=26
  - Clause counts (Doc 06): GDPR=28, CRA=26
  - Coverage (Doc 07): SUBSTANTIVE=16, PARTIAL=19, NOT_ADDRESSED=6
  - Gaps found (Doc 07): 4
  - Sole-authority gaps (Doc 07): 0
  - Consistency checks: 7/7 passed

### `lint_regulatory_ground_truth.py`
- **Status:** ✅ PASS
- **Errors:** 0
- **Warnings:** 8
- **Top issues:**
  1. `00_Taxonomy_Reference.md`: Sub-domain D-02.3 sole authority is `'GDPR'` but ground truth says `'CRA'`
  2. `02_Regulatory_Mapping_Master.md`: Obligated party `'MANUFACTURER'` not valid for GDPR
  3. `02_Regulatory_Mapping_Master.md`: Obligated party `'ALLOCATION'` not valid for GDPR
  4. `02_Regulatory_Mapping_Master.md`: Obligated party `'enum'` not valid for GDPR
  5. `02_Regulatory_Mapping_Master.md`: Obligated party `'Rationale'` not valid for GDPR
  6. `02_Regulatory_Mapping_Master.md`: Obligated party `'Clauses'` not valid for CRA
  7. `02_Regulatory_Mapping_Master.md`: Obligated party `'values'` not valid for GDPR
  8. Found 1 sole authority attribution mismatches (summary)
- **Metrics:**
  - Documents scanned: 12
  - Clause references: 46 found, 46 valid, 0 invalid
  - Subdomain references: 516 found, 516 valid, 0 invalid
  - Timeline mentions: 32 found, 32 valid
  - Obligation-type checks: 4, invalid: 0
  - Obligated-party checks: 12, **invalid: 6**
  - Normative-intensity checks: 12, mismatches: 0
  - Sole-authority checks: 12, **mismatches: 1**

### `lint_regulatory_mapping.py`
- **Status:** ✅ PASS
- **Errors:** 0
- **Warnings:** 1
- **Top issues:**
  1. `02_Regulatory_Mapping_Master.md`: Only 3 security domains mentioned (expected coverage across multiple domains)
- **Metrics:**
  - Regulations found: 5 of 5 expected (NIS2, GDPR, AI Act, CRA, DORA)
  - Total clauses mapped: 28
  - Domains covered: 3
  - Documents found: 5
  - Excel sheets: 8
  - Total rows: 338

### `lint_regulatory_references.py`
- **Status:** ✅ PASS
- **Errors:** 0
- **Warnings:** 0
- **Top issues:** none
- **Metrics:**
  - Total references: 446
  - Valid references: 446
  - Invalid references: 0
  - Regulations checked: 7
  - Documents scanned: 39

### `lint_template_compliance.py`
- **Status:** ✅ PASS
- **Errors:** 0
- **Warnings:** 20
- **Top issues:**
  1. `05_Regulatory_Applicability`: Extra section not in template: `'5.3 Compliance Boundary Diagram'`
  2. `07_Structured_Compliance_Matrix`: Extra section not in template: `'5.2 Complementarity Opportunities'`
  3. `07_Structured_Compliance_Matrix`: Extra section not in template: `'5.3 Conflict Classification (Structural vs Contextual)'`
  4. `07_Structured_Compliance_Matrix`: Extra section not in template: `'5.4 Compound Event Scenarios'`
  5. `07_Structured_Compliance_Matrix`: Extra section not in template: `'5.1 Cross-Regulation Overlap'`
  6. `01_Company_Context`: Extra section not in template: `'CHANGELOG'`
  7. `01_Company_Context`: Extra section not in template: `'N. COMPANY CONTEXT CLASS INSTANTIATION'`
  8. `01_Company_Context`: Extra section not in template: `'N+1. VERSION HISTORY'`
  9. `01_Company_Context`: Extra section not in template: `'N. ARCHITECTURE INVENTORY'`
  10. `01_Company_Context`: Extra section not in template: `'10. STAKEHOLDERS'` (and subsections)
  11. Document not found for pattern: `01_INTAKE_FORM`
- **Metrics:**
  - Documents checked: 4
  - Documents passed: 4
  - Total sections required: 85
  - Total sections found: 80
  - Average compliance: 90%

## Known Issues Catalog

Distinct issues the Fase de Especificação 1 reconciliation must resolve (or document as accepted):

1. **Cross-document: Doc 07 coverage matrix over-counts (41 vs 38 expected).**
   Doc 07 lists 41 entries for the 38 sub-domains — possible duplicates or sub-domain mis-naming.

2. **Cross-document: 4 sole-authority gaps missing from Doc 07.**
   Ontology declares `{D-07.4, D-07.3, D-09.3, D-07.2}` as sole-authority gaps but Doc 07 gaps table does not list them.

3. **Ground truth: Sub-domain D-02.3 sole authority mismatch.**
   `00_Taxonomy_Reference.md` attributes D-02.3 to GDPR; ground truth says CRA.

4. **Ground truth: 6 obligated-party tokens in `02_Regulatory_Mapping_Master.md` are enum-like headers, not actual values.**
   Tokens detected as obligated parties but not valid for the named regulation: `MANUFACTURER`, `ALLOCATION`, `enum`, `Rationale`, `Clauses`, `values`. Indicates the parser is treating markdown table headers / enum metadata as obligated-party values.

5. **Mapping: only 3 security domains mentioned in `02_Regulatory_Mapping_Master.md`.**
   Expected broader coverage across multiple security domains.

6. **Template: 4 extra sections in `07_Structured_Compliance_Matrix` not in template.**
   `5.1 Cross-Regulation Overlap`, `5.2 Complementarity Opportunities`, `5.3 Conflict Classification (Structural vs Contextual)`, `5.4 Compound Event Scenarios`.

7. **Template: 1 extra section in `05_Regulatory_Applicability` not in template.**
   `5.3 Compliance Boundary Diagram`.

8. **Template: 14 extra sections in `01_Company_Context` not in template.**
   Including `CHANGELOG`, `N. ARCHITECTURE INVENTORY` and N.1–N.6 sub-sections, `10. STAKEHOLDERS` / `10.1 Stakeholder Influence Matrix`, `11. BUSINESS GOALS`, `MEDIUM Complexity Tier`, `N. COMPANY CONTEXT CLASS INSTANTIATION`, `N+1. VERSION HISTORY`.

9. **Template: intake form `01_INTAKE_FORM` document not found.**
   Expected pattern `01_INTAKE_FORM` not present in the case folder.

10. **Structural note: 3 of 6 Phase 1 lints have no `main()` CLI.**
    `lint_company_context.py`, `lint_regulatory_mapping.py`, `lint_regulatory_references.py` only expose `lint_*()` functions and must be invoked via the orchestrator (or by importing + calling manually). Not a bug per se, but a tooling-consistency observation for future Sprint work.

## Lint Output Raw Logs

### 1. `run_phase1_lints.py` (orchestrator)

```
$ python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py \
    --case "Case_01_TinyTask_SaaS" \
    --output /tmp/opencode/lint_reports

🔍 Phase 1 Lints — Case_01_TinyTask_SaaS
📂 /home/epmq-cyber/Área de Trabalho/projects/Methodology-main/02_CASES/Case_01_TinyTask_SaaS
============================================================

============================================================
📊 Summary: 6/6 passed
⚠️ 31 warning(s)
✅ All Phase 1 lints passed!
  Running: Company Context (38 questions)... ✅ PASSED
  Running: Regulatory Mapping... ✅ PASSED
  Running: Regulatory References (Anti-Hallucination)... ✅ PASSED
  Running: Regulatory Ground Truth... ✅ PASSED
  Running: Cross-Document Consistency... ✅ PASSED
  Running: Template Compliance... ✅ PASSED

� Reports generated:
   JSON: /tmp/opencode/lint_reports/lint_report_phase1_20260806_105905.json
   Markdown: /tmp/opencode/lint_reports/lint_report_phase1_20260806_105905.md
```

### 2. `lint_company_context.py`

> Note: this lint has no `argparse` CLI. Invoked by importing `lint_company_context` and calling it on the resolved case path.

```
$ python3 -c "
import sys, json
sys.path.insert(0, '01_IMPLEMENTATION_TOOLS/lints')
sys.path.insert(0, '01_IMPLEMENTATION_TOOLS/lints/phase1')
from lints.phase1.lint_company_context import lint_company_context
from pathlib import Path
print(json.dumps(lint_company_context(Path('02_CASES/Case_01_TinyTask_SaaS')),
                indent=2, ensure_ascii=False))
"

{
  "valid": true,
  "errors": [],
  "warnings": [],
  "metrics": {
    "format_detected": "layered",
    "documents_found": 1,
    "compliance_score": 100
  }
}
```

### 3. `lint_cross_document_consistency.py`

```
$ python3 01_IMPLEMENTATION_TOOLS/lints/phase1/lint_cross_document_consistency.py \
    --case "Case_01_TinyTask_SaaS"

Valid: True

Warnings:
  ⚠️ Doc 07 coverage matrix has 41 entries (expected 38)
  ⚠️ Sole authority gaps {'D-07.4', 'D-07.3', 'D-09.3', 'D-07.2'} from ontology not found in Doc 07 gaps table

Metrics: {'doc04_found': True, 'doc05_found': True, 'doc06_found': True, 'doc07_found': True, 'applicable_regs_doc04': ['GDPR', 'CRA'], 'applicable_regs_doc05': ['GDPR', 'CRA'], 'clause_counts_doc05': {'GDPR': 28, 'CRA': 26}, 'clause_counts_doc06': {'GDPR': 28, 'CRA': 26}, 'coverage_counts_doc07': {'SUBSTANTIVE': 16, 'PARTIAL': 19, 'NOT_ADDRESSED': 6}, 'gaps_found_doc07': 4, 'sole_authority_gaps_doc07': 0, 'consistency_checks_passed': 7, 'consistency_checks_total': 7}
```

### 4. `lint_regulatory_ground_truth.py`

```
$ python3 01_IMPLEMENTATION_TOOLS/lints/phase1/lint_regulatory_ground_truth.py \
    --case "Case_01_TinyTask_SaaS"

Valid: True

Warnings:
  �️ 00_Taxonomy_Reference.md: Sub-domain D-02.3 sole authority is 'GDPR' but ground truth says 'CRA'
  ⚠️ 02_Regulatory_Mapping_Master.md: Obligated party 'MANUFACTURER' not valid for GDPR
  ⚠️ 02_Regulatory_Mapping_Master.md: Obligated party 'ALLOCATION' not valid for GDPR
  ⚠️ 02_Regulatory_Mapping_Master.md: Obligated party 'enum' not valid for GDPR
  ⚠️ 02_Regulatory_Mapping_Master.md: Obligated party 'Rationale' not valid for GDPR
  ⚠️ 02_Regulatory_Mapping_Master.md: Obligated party 'Clauses' not valid for CRA
  ⚠️ 02_Regulatory_Mapping_Master.md: Obligated party 'values' not valid for GDPR
  ⚠️ Found 1 sole authority attribution mismatches

Metrics: {'documents_scanned': 12, 'clause_references_found': 46, 'clause_references_valid': 46, 'clause_references_invalid': 0, 'subdomain_references_found': 516, 'subdomain_references_valid': 516, 'subdomain_references_invalid': 0, 'timeline_mentions_found': 32, 'timeline_mentions_valid': 32, 'obligation_type_checks': 4, 'obligation_type_invalid': 0, 'obligated_party_checks': 12, 'obligated_party_invalid': 6, 'normative_intensity_checks': 12, 'normative_intensity_mismatches': 0, 'sole_authority_checks': 12, 'sole_authority_mismatches': 1}
```

### 5. `lint_regulatory_mapping.py`

> Note: this lint has no `argparse` CLI. Invoked by importing `lint_regulatory_mapping` and calling it on the resolved case path.

```
$ python3 -c "
import sys, json
sys.path.insert(0, '01_IMPLEMENTATION_TOOLS/lints')
sys.path.insert(0, '01_IMPLEMENTATION_TOOLS/lints/phase1')
from lints.phase1.lint_regulatory_mapping import lint_regulatory_mapping
from pathlib import Path
print(json.dumps(lint_regulatory_mapping(Path('02_CASES/Case_01_TinyTask_SaaS')),
                indent=2, ensure_ascii=False))
"

{
  "valid": true,
  "errors": [],
  "warnings": [
    "02_Regulatory_Mapping_Master.md: Only 3 security domains mentioned (expected coverage across multiple domains)"
  ],
  "metrics": {
    "regulations_found": 5,
    "regulations_expected": 5,
    "total_clauses_mapped": 28,
    "clauses_per_regulation": {},
    "domains_covered": 3,
    "documents_found": 5,
    "excel_sheets": 8,
    "regulations_list": [
      "CRA",
      "DORA",
      "GDPR",
      "NIS2",
      "AI Act"
    ],
    "total_rows": 338
  }
}
```

### 6. `lint_regulatory_references.py`

> Note: this lint has no `argparse` CLI. Invoked by importing `lint_regulatory_references` and calling it on the resolved case path.

```
$ python3 -c "
import sys, json
sys.path.insert(0, '01_IMPLEMENTATION_TOOLS/lints')
sys.path.insert(0, '01_IMPLEMENTATION_TOOLS/lints/phase1')
from lints.phase1.lint_regulatory_references import lint_regulatory_references
from pathlib import Path
print(json.dumps(lint_regulatory_references(Path('02_CASES/Case_01_TinyTask_SaaS')),
                indent=2, ensure_ascii=False))
"

{
  "valid": true,
  "errors": [],
  "warnings": [],
  "metrics": {
    "total_references": 446,
    "valid_references": 446,
    "invalid_references": 0,
    "regulations_checked": 7,
    "documents_scanned": 39
  }
}
```

### 7. `lint_template_compliance.py`

```
$ python3 01_IMPLEMENTATION_TOOLS/lints/phase1/lint_template_compliance.py \
    --case "Case_01_TinyTask_SaaS"

Valid: True

Warnings:
  ⚠️ 05_Regulatory_Applicability: Extra section not in template: '5.3 Compliance Boundary Diagram'
  ⚠️ 07_Structured_Compliance_Matrix: Extra section not in template: '5.2 Complementarity Opportunities'
  ⚠️ 07_Structured_Compliance_Matrix: Extra section not in template: '5.3 Conflict Classification (Structural vs Contextual)'
  ⚠️ 07_Structured_Compliance_Matrix: Extra section not in template: '5.4 Compound Event Scenarios'
  ⚠️ 07_Structured_Compliance_Matrix: Extra section not in template: '5.1 Cross-Regulation Overlap'
  �️ 01_Company_Context: Extra section not in template: 'CHANGELOG'
  �️ 01_Company_Context: Extra section not in template: 'N. COMPANY CONTEXT CLASS INSTANTIATION'
  ⚠️ 01_Company_Context: Extra section not in template: 'N+1. VERSION HISTORY'
  ⚠️ 01_Company_Context: Extra section not in template: 'N. ARCHITECTURE INVENTORY'
  ⚠️ 01_Company_Context: Extra section not in template: 'N.1 Systems'
  ⚠️ 01_Company_Context: Extra section not in template: 'N.2 Cloud Services'
  ⚠️ 01_Company_Context: Extra section not in template: 'N.3 Authentication & Identity Systems'
  ⚠️ 01_Company_Context: Extra section not in template: 'N.4 Data Stores'
  ⚠️ 01_Company_Context: Extra section not in template: 'N.5 Data Flows'
  ⚠️ 01_Company_Context: Extra section not in template: 'N.6 Data Subject Categories'
  ⚠️ 01_Company_Context: Extra section not in template: 'MEDIUM Complexity Tier'
  ⚠️ 01_Company_Context: Extra section not in template: '10. STAKEHOLDERS'
  ⚠️ 01_Company_Context: Extra section not in template: '10.1 Stakeholder Influence Matrix'
  ⚠️ 01_Company_Context: Extra section not in template: '11. BUSINESS GOALS'
  �️ Document not found for pattern: 01_INTAKE_FORM

Metrics: {'documents_checked': 4, 'documents_passed': 4, 'total_sections_required': 85, 'total_sections_found': 80, 'average_compliance_pct': 0.9}
```

## Verification

```
$ ls -la 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_BEFORE.md
-rw-r--r-- 1 epmq-cyber epmq-cyber [..] LINT_REPORT_BEFORE.md

$ wc -l 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_BEFORE.md
[see footer of file]

$ head -30 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_BEFORE.md
[front-matter + opening]
```

## Notes for Fase de Especificação 1

- **All 6 lints PASS** at the aggregate level, so no linter changes are blocking the rich-mode build.
- **31 warnings** must be triaged by Fase de Especificação 1:
  - **Template-compliance warnings (20)** are the largest category; most correspond to legacy documents being richer than the canonical template (extra architecture inventory, stakeholders section, etc.). Fase de Especificação 1 should decide whether to update the template or trim the documents.
  - **Ground-truth obligated-party warnings (6)** are likely parser false-positives caused by markdown table headers being scanned as obligated-party values — recommend investigating the regex before mutating `02_Regulatory_Mapping_Master.md`.
  - **The single sole-authority mismatch (D-02.3 GDPR vs CRA)** is a substantive content question for the orchestrator to arbitrate (P7).
  - **Cross-document warnings (2)** reflect real reconciliation work needed between the ontology and Doc 07.
  - **Mapping-coverage warning (1)** is a soft signal; the legacy file covers 3 of the canonical 38 security domains at the mapping-master level (full coverage exists in `06_Clause_Mapping_Matrix`).
- **Tooling observation:** 3 of 6 lints have no CLI. Future sprints may want to add a `main()` to `lint_company_context.py`, `lint_regulatory_mapping.py`, `lint_regulatory_references.py` for parity.
