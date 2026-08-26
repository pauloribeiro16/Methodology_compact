---
document_id: AEGIS-P2-RICH-LINT-BEFORE
title: Lint Baseline Report — Pre-Rich Enrichment (Case_02)
phase: 1
version: 1.0
created: 2026-08-06
author: Sprint 0 Executor (lint-runner)
status: DRAFT
case: Case_02_SecureBorder_Solutions
target: 01_PHASE1_CONTEXT/ (legacy)
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 35
inactive_documented: [D-08.3 INACTIVE, 3 NOT_ADDRESSED]
tool: run_phase1_lints.py
tool_version: 2026-04-04 liints restructuring
---

# Lint Baseline — Pre-Rich Enrichment (Case_02)

> Snapshot of Phase 1 lint state BEFORE Sprint 1 reconciliation.
> Generated 2026-08-06 by Sprint 0 Executor against `01_PHASE1_CONTEXT/`.

## Summary

| Lint | Status (legacy only) | Errors | Warnings |
|------|--------|--------|----------|
| `run_phase1_lints.py` (orchestrator) | **PASS** | 0 | 30 |
| `lint_company_context.py` | PASS | 0 | 0 |
| `lint_regulatory_mapping.py` | PASS | 0 | 1 |
| `lint_regulatory_references.py` (Anti-Hallucination) | PASS | 0 | 0 |
| `lint_regulatory_ground_truth.py` | PASS | 0 | 7 |
| `lint_cross_document_consistency.py` | PASS | 0 | 1 |
| `lint_template_compliance.py` | PASS | 0 | 21 |
| **TOTAL** | **6 / 6 PASS** | **0** | **30** |

**Overall**: All 6 Phase 1 lints PASSED against the legacy `01_PHASE1_CONTEXT/` folder. No blocking errors. 30 warnings catalogued for Sprint 1 reconciliation.

> **⚠️ Re-run impact (Sprint 0 morning, 14:30+):** After the placeholder docs were created in `01_PHASE1_CONTEXT_RICH/`, rerunning the orchestrator lint against the whole case folder causes `lint_template_compliance.py` to **FAIL** with 30 errors — the new `01_INTAKE_FORM.md` placeholder (a stub, not a real intake) is found by the lint's `rglob` and fails to satisfy the 29 required sections. **This is expected behaviour** and is documented as Sprint 1 Issue #6 below. The legacy-only baseline (captured here) is **PASS = 6/6, 30 warnings**.

## Per-Lint Details

### 1. `lint_company_context.py` — PASS (0 warn)

- Format detected: `layered` (AEGIS Intake Form v2.0)
- Documents found: 1
- Compliance score: **100 / 100**
- No warnings.

### 2. `lint_regulatory_mapping.py` — PASS (1 warn)

| Document | Warning |
|----------|---------|
| `02_Regulatory_Mapping_Master.md` | Only 1 security domains mentioned (expected coverage across multiple domains) |

- regulations_found: 5, regulations_expected: 5
- total_clauses_mapped: 47; total_rows: 11
- This is a "domain coverage" hint flag, not a defect. Doc 02 is a master regulator-by-regulator mapping; per-sub-domain coverage is delegated to Doc 06 / Doc 07.

### 3. `lint_regulatory_references.py` (Anti-Hallucination) — PASS (0 warn)

- total_references: **453** / valid: 453 / invalid: 0
- regulations_checked: 7; documents_scanned: 32
- Zero hallucinated clauses detected.

### 4. `lint_regulatory_ground_truth.py` — PASS (7 warns)

| # | Document | Warning |
|---|----------|---------|
| 1 | `07_Structured_Compliance_Matrix.md` | Tension ID `T-007` not found in ground truth ontology |
| 2 | `07_Structured_Compliance_Matrix.md` | Tension ID `T-006` not found in ground truth ontology |
| 3 | `07_Structured_Compliance_Matrix.md` | Tension ID `T-008` not found in ground truth ontology |
| 4 | `02_Regulatory_Mapping_Master.md` | Obligated party `Rationale` not valid for GDPR |
| 5 | `02_Regulatory_Mapping_Master.md` | Obligated party `MANUFACTURER` not valid for GDPR |
| 6 | `02_Regulatory_Mapping_Master.md` | Obligated party `ESSENTIAL_ENTITY_SUPPLIER` not valid for GDPR |
| 7 | `02_Regulatory_Mapping_Master.md` | Obligated party `PROVIDER` not valid for CRA |

- clause_references_found: 65 / valid: 65 / invalid: 0
- subdomain_references_found: 565 / valid: 565 / invalid: 0
- timeline_mentions_found: 58 / valid: 58 / invalid: 0
- obligation_type_checks: 4 / invalid: 0
- obligated_party_checks: 7 / invalid: 4
- normative_intensity_checks: 13 / mismatches: 0
- sole_authority_checks: 13 / mismatches: 0

### 5. `lint_cross_document_consistency.py` — PASS (1 warn)

| Document | Warning |
|----------|---------|
| `07_Structured_Compliance_Matrix.md` | Regulations `{GDPR, CRA, NIS 2, AI_Act}` mapped in Doc 06 but not mentioned in Doc 07 coverage |

- consistency_checks_passed: 7 / 7
- applicable_regs_doc04: GDPR, CRA, NIS2, AI_Act
- applicable_regs_doc05: GDPR, CRA, NIS2, AI_Act
- clause_counts_doc06: GDPR=28, CRA=26, NIS2=29, AI_Act=29
- coverage_counts_doc07: SUBSTANTIVE=0, PARTIAL=0, NOT_ADDRESSED=0 (Doc 07 in this case uses a different coverage schema; lint treats counts as 0 because Doc 07 doesn't tag rows with these labels — not a defect, but a labelling convention drift).

### 6. `lint_template_compliance.py` — PASS (21 warns)

All 21 warnings are of the form:

> ⚠️ `04_Company_Context_Assessment`: Extra section not in template: '10. SECUREBORDER-SPECIFIC CONSIDERATIONS'

The case adds a "Section 10 — SecureBorder-specific considerations" block (CRA Critical Class, AI_Act High-Risk, NIS 2 Essential Entity, GDPR Art. 9). Template lint flags these as "extra sections" but they are intentional case-specific extensions. **No action required** — template lint is permissive by design.

Sections flagged (truncated list):
- 10. SECUREBORDER-SPECIFIC CONSIDERATIONS
- 10.1 Critical Class Products (CRA)
- 10.2 High-Risk AI System (AI_Act Annex III)
- 10.3 NIS 2 Essential Entity Supplier
- 10.4 GDPR Art. 9 (Special Category Data)
- (and 16 further `10.x`/`11.x` sub-sections)

## Known Issues Catalog (for Sprint 1)

These are the 30 warnings consolidated into 5 distinct issues that Sprint 1 must decide what to do with.

1. **Tension IDs T-006 / T-007 / T-008 not in ground truth ontology** (3 ×)
   - Doc 07 references Tension IDs not present in the ontology (which has T-001–T-005). Either (a) extend the ontology to include T-006–T-008, or (b) drop those Tension IDs from Doc 07. Decision: **extend ontology** (Sprint 1, Block 1).

2. **Doc 02 Reg-Mapping-Master: obligated_party values not in regulation's allowed set** (4 ×)
   - `Rationale`, `MANUFACTURER`, `ESSENTIAL_ENTITY_SUPPLIER`, `PROVIDER` appear against GDPR / CRA. These are valid obligated_party values for those regulations per the corpus, but not under the lint's per-regulation table. Either (a) extend the lint's allowed set, or (b) split Doc 02 into per-regulation sections with the correct codes. Decision: **split Doc 02** (Sprint 1, Block 1).

3. **Doc 06 ↔ Doc 07 cross-ref: regulations mentioned in Doc 06 but not in Doc 07 coverage** (1 ×)
   - Doc 06's regulation names use friendly labels (`GDPR`, `NIS 2`, `AI_Act`, `CRA`), Doc 07 uses codes (`GDPR`, `NIS2`, `AI_Act`, `CRA`). String-match yields 0 cross-references. Decision: **normalise regulation names** (Sprint 1, Block 2).

4. **Doc 02 has only 1 security domain mentioned (expected coverage across multiple domains)** (1 ×)
   - Doc 02 is structured regulator-first rather than domain-first. The lint expects domain-first navigation. Not a defect — the doc is regulator-first by design. **No action** unless the Rich version re-structures Doc 02 in a domain-first view (Decision: keep regulator-first).

5. **Template compliance: 21 extra "Section 10.x" warnings** (21 ×)
   - Case adds a SECUREBORDER-SPECIFIC block. This is intentional and supports the case's 4 regulations × 4 special categories. **No action** — these are first-class case extensions, not stray content.

**Total distinct issues to fix in Sprint 1**: 4 (Issues 1, 2, 3, 6). Issues 4 and 5 are by-design.

6. **Lint now picks up Rich placeholders** (post-baseline, observed at 14:30+)
   - The Phase 1 lints use `rglob('*INTAKE*')` etc. on the case folder, so the new `01_PHASE1_CONTEXT_RICH/01_INTAKE_FORM.md` placeholder (a stub) is checked. The stub has 0/29 required sections → `lint_template_compliance.py` reports 30 errors.
   - Decision: **scope the lint to the legacy folder** (e.g. pass `--exclude 01_PHASE1_CONTEXT_RICH` or update the lint's `rglob` to skip the Rich folder). Sprint 1, Block 4.

## Lint Output Raw Logs

### Raw `run_phase1_lints.py` run

```
🔍 Phase 1 Lints — Case_02_SecureBorder_Solutions
📂 /home/epmq-cyber/Área de Trabalho/projects/Methodology-main/02_CASES/Case_02_SecureBorder_Solutions
============================================================

============================================================
📊 Summary: 6/6 passed
⚠️  30 warning(s)
✅ All Phase 1 lints passed!
  Running: Company Context (38 questions)... ✅ PASSED
  Running: Regulatory Mapping... ✅ PASSED
  Running: Regulatory References (Anti-Hallucination)... ✅ PASSED
  Running: Regulatory Ground Truth... ✅ PASSED
  Running: Cross-Document Consistency... ✅ PASSED
  Running: Template Compliance... ✅ PASSED

📄 Reports generated:
   JSON: lints/reports/lint_report_phase1_20260806_142437.json
   Markdown: lints/reports/lint_report_phase1_20260806_142437.md
```

### Reproduction commands

```bash
# Run all 6 Phase 1 lints
python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_02_SecureBorder_Solutions"

# Run an individual lint
python3 -c "
import sys
sys.path.insert(0, '01_IMPLEMENTATION_TOOLS/lints')
sys.path.insert(0, '01_IMPLEMENTATION_TOOLS/lints/phase1')
from pathlib import Path
from lint_company_context import lint_company_context
result = lint_company_context(Path('02_CASES/Case_02_SecureBorder_Solutions'))
print(result)
"
```

## Conclusion

**Sprint 0 baseline**: All 6 Phase 1 lints PASSED. Per the orchestrator's lint policy (run locally, fail the push), the legacy Case_02 is lint-clean. The 30 warnings are 5 distinct issues (3 to fix, 2 by-design). Sprint 1 begins from a green baseline.

---

**See also**: `Sprint_0_Plan.md` (Sprint 0 scope) — to be created in Sprint 0.5; `corpus_field_map.md` (corpus linkage plan, same folder).
