---
document_id: AEGIS-P1-RICH-SPRINT4-REPORT
title: Sprint 4 Report — Adjusted Objectives
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-10
author: Sprint 4 Executor
sprint_8_note: Sprint 8 Executor (corr-009 ao-migration historical-context)
status: HISTORICAL
historical_note: Historical report from corr-007 era. Current 07c version is v4.0 with AO ID model (corr-008 supersedes corr-007). Content below preserved verbatim; see `07c_Adjusted_Objectives.md` §9 Version History for the v4.0 AO ID migration entry.
sprint: 4
sprint_role: adjusted_objectives_per_subdomain
case: Case_01_TinyTask_SaaS
---

# Sprint 4 — Adjusted Objectives

## §1 Summary

- **NEW Doc 07c** — 292 lines, 74 adjusted objectives (37 PG + 37 SG) + 4 tensions resolved with max-SLA routing + 37-row Track B decision trail + generic baseline preserved
- **Doc 07b extended** — version 1.3, +§12 (Track B decision table) + §13 (tensions cross-reference) + §14 (corpus provenance). Added 179 lines (was 209, now 378)
- **Doc 04 updated** — BG catalog §4 now has "Linked Adjusted Objectives (Doc 07c)" column for BG-01..BG-05
- **README updated** — Sprint 4 row added to Sprint Status Dashboard
- **RICH_VS_LEGACY updated** — 07c row added + 07b line count delta updated + totals recalculated
- **Lints: 6/6 PASS, 44 warnings** (unchanged — RICH folder is lint-safe per lints scope: legacy `01_PHASE1_CONTEXT/` + `00_COMMON/` only)

## §2 Per-doc change list

| Doc | Status | Lines added | Description |
|-----|--------|------------:|-------------|
| `07c_Adjusted_Objectives.md` | NEW | +292 | Adjusted objectives per sub-domain (PG + SG + tensions + decision trail) |
| `07b_Proportionality_Profile.md` | v1.2 → v1.3 | +179 | +§12 (37-row decision table) + §13 (tensions cross-ref) + §14 (corpus provenance) |
| `04_Company_Context_Assessment.md` | updated | +5 (table row expansion) | BG-01..BG-05 now have "Linked Adjusted Objectives (Doc 07c)" column |
| `README.md` | updated | +1 (table row) | Sprint 4 row in Sprint Status Dashboard |
| `RICH_VS_LEGACY.md` | updated | +3 (rows) + 2 (totals) | 07c entry + 07b line count + total lines recalculated |

**Total Sprint 4 output:** 478 lines added, 1 new doc (Doc 07c).

## §3 Track B Decision Table applied (37 rows)

> Per `proportionality_model.md §5.1` (MUST) + §5.2 (SHOULD/COULD drop-one-tier + FTE≤1.0 → DEFERRED).

**Distribution:**

| Tier | Count | Decision rule |
|------|------:|---------------|
| LIGHTWEIGHT | 31 | §5.1 row MICRO col BUILD_REQUIRED |
| MINIMAL | 5 | §5.1 row MICRO col INHERITABLE |
| DEFERRED | 1 | §5.2 drop-one-tier + MICRO + FTE=0.85 ≤ 1.0 |
| **TOTAL** | **37** | |

**Floor-rule check:** Every MUST ≥ MINIMAL per §5.3 ✅. The only DEFERRED row (D-02.4) is SHOULD (not MUST), satisfying §5.3's prohibition on MUST → DEFERRED.

**MINIMAL rows:** D-03.1, D-03.2, D-06.1, D-06.4, D-08.1 (all INHERITABLE — Firebase Auth baseline, AWS/Stripe/Firebase boundaries, vendor docs).

**DEFERRED row:** D-02.4 (Threat-Led Penetration Testing) — OJ has no mandate for default-class CRA manufacturer; reference NIST SP 800-115 only.

## §4 Tensions resolved (4)

| ID | Sub-Domain(s) | Type | Severity | Resolution | Source 1 | Source 2 |
|----|---------------|------|----------|------------|----------|----------|
| T-001 | D-04.3 | timing | HIGH | max-SLA routing — 24h internal | GDPR-C25 (Art. 33 72h) | CRA-C20 (Art. 20 24h) |
| T-002 | D-06.1, D-06.3 | scope | MEDIUM | Unified vendor mgmt (DPA + SBOM) | GDPR-C21 (Art. 28 processor clauses) | CRA-C07 (Art. 7 supply chain) |
| T-003 | D-09.4, D-09.1 | requirement | MEDIUM | Integrated documentation (DPIA + CRA-RA) | GDPR-C13/C22 (Art. 13/30 ROPA) | CRA-C13 (Art. 13 technical doc) |
| T-004 | D-08.2 | intensity | LOW | Competency matrix (GDPR + CRA) | GDPR-C28 (Art. 37 DPO competence) | CRA-C21 (Art. 21 sec competence) |

**IDs preserved from legacy** Phase 2 `09_Strategic_Tensions_Report.md` (TENSION-H-001, TENSION-M-001, TENSION-M-002, TENSION-L-001) + `phase1_ontology.yaml` (T-001..T-004). Sprint 4 adopts the canonical `T-NNN` form throughout the Rich Mode.

**Invariant preserved:** Tensions are resolved through operational procedures + design decisions; the regulatory `fit_criterion` and the tier assignment are NOT modified (per `proportionality_model.md §1`).

## §5 Validation

| Check | Status | Notes |
|-------|--------|-------|
| Doc 07c created | ✅ | 292 lines |
| Doc 07b §12-§14 added | ✅ | v1.2 → v1.3 (+179 lines) |
| Doc 04 BG cross-refs added | ✅ | 5 BGs linked |
| README updated | ✅ | Sprint 4 row |
| RICH_VS_LEGACY updated | ✅ | 07c entry + 07b delta + totals |
| Lints 6/6 PASS | ✅ | 44 warnings (unchanged — RICH folder not scanned) |
| 37 sub-domains × 2 goals = 74 adjusted objectives | ✅ | All 37 covered |
| 4 tensions resolved with max-SLA routing | ✅ | T-001..T-004 preserved |
| Track B decision table applied (37 rows) | ✅ | Matches Doc 07b §4 verbatim |
| Floor rule preserved (no MUST below MINIMAL) | ✅ | 36 MUST at LIGHTWEIGHT/MINIMAL, 1 SHOULD at DEFERRED |
| Generic baseline preserved (§1) | ✅ | HSO + Sub-SOs copied verbatim from corpus, no Track B modification |
| Tension IDs match legacy (T-001..T-004) | ✅ | Same IDs in Doc 07c §4, Doc 07b §13, phase1_ontology.yaml |

## §6 Cross-References Index (Sprint 4 deliverables)

| Doc | References Out | References In |
|-----|----------------|---------------|
| 07c (NEW) | 07b §4 (tier), 07 §3 (priority), 04 §2 (scale), phase1_ontology.yaml (tensions + clauses), 10_Privacy_Security_Goals.md legacy (format), proportionality_model.md §1+§5+§6 | 04 §4 (BG cross-ref), 07b §13 (tensions cross-ref), 11_Rules_Catalog.md (Phase 2 consumer) |
| 07b (v1.3) | 04 §2/§5, 05 §5, 07 §3, proportionality_model.md §1+§5+§6, corpus JSON sidecars | 07c §1+§5 (decision trail + baseline), 08/11/14 (Phase 2/3 outputs) |
| 04 (BG §4) | 07c §2/§3/§4 (linked adjusted objectives per BG) | — |

## §7 Sprint 5 readiness / NEXT steps

- **Phase 2 (rules/requirements)** can now consume Doc 07c adjusted objectives — 74 PG/SG statements ready for translation into specific rules in `11_Rules_Catalog.md`
- **Phase 3 (architecture)** can consume Doc 07b §12 decision trail for tier-driven architectural choices in `14_Architectural_Nodes.md`
- **Validator review recommended** — see `VALIDATOR_SPRINT4.md` (Executor self-verification)

## §8 Outstanding (P7 — Human Decisions Required)

1. **Doc 07c PG/SG statements** need business + technical validation (CEO + CTO sign-off) — currently Executor-drafted from Doc 07b §4 `example_controls` column. May need security architect review for technical accuracy.
2. **Tensions T-002, T-003, T-004** resolution approaches (unified vendor mgmt, integrated documentation, competency matrix) need security architect sign-off. T-001 max-SLA 24h is operational and may need CTO sign-off on internal SLA commitment.
3. **Doc 04 BG cross-refs** need CEO confirmation that BG-01..BG-05 priorities remain valid as drafted.
4. **(Optional)** Legacy Phase 2 `10_Privacy_Security_Goals.md` and `09_Strategic_Tensions_Report.md` could be deprecated in favour of Doc 07c + Doc 07b §13. Currently Doc 07c frontmatter notes "supersedes" but the legacy docs are NOT physically deprecated — decision pending.

---

## §9 Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-06 | Sprint 4 Executor | Initial release — Sprint 4 deliverables report (Doc 07c + Doc 07b §12-§14 + Doc 04 cross-refs) |

---

## §10 See also

- `07c_Adjusted_Objectives.md` — Sprint 4 NEW doc (74 adjusted objectives)
- `07b_Proportionality_Profile.md` — extended with §12-§14
- `04_Company_Context_Assessment.md` §4 — BG cross-refs added
- `README.md` — Sprint 4 status
- `RICH_VS_LEGACY.md` — updated diff summary
- `validation/VALIDATOR_SPRINT4.md` — Executor self-verification (Validator review pending)
- `validation/SPRINT3_REPORT.md` — prior sprint baseline (6/6 PASS, 44W)
- `01_IMPLEMENTATION_TOOLS/lints/reports/lint_report_phase1_20260806_123331.md` — Sprint 4 lint baseline (6/6 PASS, 44W unchanged)
