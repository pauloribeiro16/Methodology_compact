---
document_id: AEGIS-P3-RICH-FIX-TIER12
title: Tier 1+2 Fix Report — Case_03
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Sprint Fix Executor
status: FIXED
case: Case_03_OmniBank_Financial
---

# Tier 1+2 Fix Report

## §1 Gaps Fixed (2 MEDIUM + 2 LOW)

### MEDIUM

- **Gap 1: BG-005/006/007/008 → Doc 07 §6.1 mapping added (uptime, expansion, ISO 27001+DORA, AI bias)**
  - File: `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/07_Structured_Compliance_Matrix.md:312-315`
  - Added 4 explicit BG rows to the §6.1 Business Goal Alignment table (BG-005 99.99% uptime SLA, BG-006 3 EU markets expansion, BG-007 ISO 27001 + DORA unified ISMS, BG-008 AI bias <1%).
  - Added 4 explicit `### BG-XXX → Doc 07 §6.1 mapping` sub-sections immediately after §6.1, each carrying:
    - Affected sub-domains (D-XX.Y list)
    - PG/SG references (PG-D-XX.X-NNN / SG-D-XX.X-NNN IDs)
    - Verification criteria reinforcement paragraph (regulatory anchors + Doc 07c card cross-references)
  - Same approach as Case_02 MEDIUM 1 fix.

- **Gap 2: KPI verification criteria added to Doc 07c PG/SG cards (D-04.4 RTO 24h, D-09.2 DPIA+FRIA, D-10.3 quarterly review, D-07.1 AI bias <1%)**
  - File: `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/07c_Adjusted_Objectives.md`
  - 6 sub-domains × 2 cards (PG + SG) = **12 cards updated** with a new `KPI:` Verification Criteria bullet:
    - **D-04.1** (PG/SG): KPI: MTTD <15min measured monthly; alert response time P95 <5min for critical alerts; SOC 24/7 staffing validated per shift roster
    - **D-04.4** (PG/SG): KPI: Quarterly DR test verifies RTO ≤24h (target ≤4h) and RPO ≤1h (target 15min) — measured in disaster simulation report (per BG-005)
    - **D-07.1** (PG/SG): KPI: Monthly bias audit on OmniScore AI Platform; bias metrics must remain <1% across all protected characteristics (per AI Act Art. 10 + BG-008)
    - **D-09.2** (PG/SG): KPI: Annual DPIA + FRIA review cycle; quantified risk reduction targets per GDPR Art. 35(7) and AI Act Art. 27(4) — IPSARA unified discharge
    - **D-10.1** (PG/SG): KPI: 24/7 SOC staffing validated quarterly; alert response time P95 <5min; AI model drift detection latency <1h
    - **D-10.3** (PG/SG): KPI: Quarterly compliance review covering all 5 regulations; documented in compliance dashboard with closure rate per BG-007

### LOW

- **Gap 3: status_history field added to Doc 07c (7 entries including 0.6 DORA) and corpus_field_map.md (2 entries)**
  - File: `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/07c_Adjusted_Objectives.md:11-18` — frontmatter now carries 7-entry `status_history` array: DRAFT (Sprint 0) → DRAFT (Sprint 0.5 Doc 07b Track B MAX) → DRAFT (Sprint 0.6 DORA ICT Risk Framework) → RECONCILED (Sprint 1) → CORPUS_ENRICHED (Sprint 2) → ADJUSTED_OBJECTIVES (Sprint 4 V-02/03/04 fix) → DEEP_ENRICHED (Sprint 5).
  - File: `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/corpus_field_map.md:8-11` — frontmatter `status` promoted from DRAFT → ACTIVE; new 2-entry `status_history`: DRAFT (Sprint 0) → ACTIVE (Sprint 2 corpus enrichment).

- **Gap 4: Doc 07b frontmatter applicable_regs added [GDPR, CRA, NIS 2, DORA, AI Act]**
  - File: `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md:11` — new frontmatter line `applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]`. Body §2 already carried it; frontmatter now canonical-consistent with all other Rich docs.

## §2 Lint Status

```
python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_03_OmniBank_Financial"
```

Result: **6/6 PASS, 0 errors, 32 warnings** (warning count unchanged from pre-fix baseline; no regressions introduced).

| Lint | Status | Warnings |
|------|--------|---------:|
| lint_company_context | ✅ PASS | 1 |
| lint_regulatory_mapping | ✅ PASS | 1 |
| lint_regulatory_references (Anti-Hallucination) | ✅ PASS | 0 |
| lint_regulatory_ground_truth | ✅ PASS | 9 |
| lint_cross_document_consistency | ✅ PASS | 0 |
| lint_template_compliance | ✅ PASS | 21 |

Fresh report: `01_IMPLEMENTATION_TOOLS/lints/reports/lint_report_phase1_20260806_223700.md`

## §3 Outstanding

- Tier 3 evaluation pending (Regulatory + Track B + Traceability)
- Cross-case comparison pending (Case_01 + Case_02 + Case_03 — three-case synthesis)
