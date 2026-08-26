# Sprint 2 — Corpus Enrichment Report (Existing Docs)

**Case:** Case_03_OmniBank_Financial
**Sprint:** 2 (Corpus Enrichment — Existing Docs)
**Date:** 2026-08-06
**Author:** Executor
**Branch:** feature/aegis-p1-case03-rich
**Status:** CORPUS_ENRICHED on all 4 docs

---

## 1. Scope

This report documents the Sprint 2 corpus enrichment of the **4 existing Phase 1 Rich docs** (`04a`, `04b`, `04c`, `04d`). Two new docs (`05b` + `Citation_Index.md`) are covered in `SPRINT2_ENRICHMENT_REPORT_NEW.md`. The Excel regeneration is documented in `SPRINT2_ENRICHMENT_REPORT_NEW.md` §2.

## 2. Corpus Source

All enrichment draws from the corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` (38 sub-domain folders, each with `*.manifest.json` + `*.json` sidecar + `articles/` folder).

## 3. Doc-by-Doc Summary

### 3.1 `04a_Architecture_DataInventory.md` (AEGIS-P3-RICH-04a-ARCH)

| Metric | Before | After |
|---|---:|---:|
| Lines | 276 | 334 |
| §3 Compliance Mapping table columns | 6 | 8 (added Corpus Manifest Path + NIST CSF Anchors) |
| §3 Compliance Mapping table rows | 38 | 38 (extended with 2 columns) |
| §4 Corpus Provenance section | absent | present (38 sub-domains) |
| Frontmatter status | RECONCILED | CORPUS_ENRICHED |
| Frontmatter version | 1.1 | 1.2 |

**Enrichment details:**
- §3 Compliance Mapping table: each of 38 sub-domains extended with 2 new columns:
  - **Corpus Manifest Path** — relative path to per-sub-domain `*.manifest.json` in the corpus
  - **NIST CSF Anchors** — combined unique NIST controls from GDPR + CRA + NIS 2 + DORA + AI Act participants
- New §4 Corpus Provenance section added: 38-row table with Sub-domain ID + Name + Participants + AI Act status + Manifest Path + JSON Sidecar Path + Articles Folder + Applicable Regs + NIST Anchors Count.
- §4 Gate renumbered to §5.
- §N-1 Version History renumbered to §N-2; §N Document Approval renumbered to §N-1.
- Added Sprint 2 entry to Version History.

### 3.2 `04b_Security_Posture.md` (AEGIS-P3-RICH-04b-SEC)

| Metric | Before | After |
|---|---:|---:|
| Lines | 257 | 465 |
| §2.1 Corpus-Derived Target fit_criteria section | absent | present (10 macro-domains + 38 sub-domains) |
| Sub-requirement count documented | n/a | 134 sub-requirements across 38 sub-domains |
| Frontmatter status | RECONCILED | CORPUS_ENRICHED |
| Frontmatter version | 1.1 | 1.2 |

**Enrichment details:**
- New §2.1 Corpus-Derived Target fit_criteria section added between §2 Per-Domain Assessment and §3 Summary Dashboard.
- §2.1 contains:
  - Per-macro-domain summary table (10 rows): Sub-Domains count + Sub-Reqs count + Verification Method(s) + composite fit_criterion
  - Per-sub-domain detailed fit_criteria table (38 rows): Req ID + Sub-Domain + Priority + Verification + truncated fit_criterion
- All fit_criteria are MUST priority; verification methods: TEST (default) + INSPECT (D-05, D-07 only).
- Aggregate totals: 14 (D-01) + 12 (D-02) + 14 (D-03) + 17 (D-04) + 9 (D-05) + 13 (D-06) + 12 (D-07) + 11 (D-08) + 18 (D-09) + 14 (D-10) = 134 sub-requirements across 38 sub-domains.
- Added Sprint 2 entry to Version History.

### 3.3 `04c_ThirdParty_Landscape.md` (AEGIS-P3-RICH-04c-3P)

| Metric | Before | After |
|---|---:|---:|
| Lines | 281 | 346 |
| §2.1 Subprocessor GDPR Art. 28 Verbatim Anchor section | absent | present |
| §6.1 Supply Chain Risk Cross-Regulation Corpus References section | absent | present |
| §8 Compliance Mapping table columns | 4 | 5 (added Corpus Manifest Path) |
| Frontmatter status | RECONCILED | CORPUS_ENRICHED |
| Frontmatter version | 1.1 | 1.2 |

**Enrichment details:**
- New §2.1 Subprocessor GDPR Art. 28 Verbatim Anchor section: references verbatim GDPR Art. 28 text from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/articles/GDPR_Art_28.md`; lists the 8 mandatory Art. 28(3)(a)–(h) DPA clauses (via SO-GDPR-021 + SO-GDPR-022 anchor); 12 SR rule titles extracted from the corpus JSON sidecar.
- New §6.1 Supply Chain Risk Cross-Regulation Corpus References section: cross-references CRA Art. 13 + NIS 2 Art. 21(2)(d) + DORA Art. 30 + CRA Art. 7 + AI Act Art. 25 (declared gap) verbatim corpus files.
- §8 Compliance Mapping table: each of D-06.1..D-06.4 rows extended with Corpus Manifest Path column.
- AI Act Art. 25 declared as **DECLARATION_GAP** (no corpus verbatim file exists under `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`); mitigation noted in §6.1.
- Added Sprint 2 entry to Version History.

### 3.4 `04d_Org_Roles_RACI.md` (AEGIS-P3-RICH-04d-RACI)

| Metric | Before | After |
|---|---:|---:|
| Lines | 455 | 458 |
| §4 RACI tables Corpus Reg Req column | absent | present (10 sub-section tables × ~5-7 activity rows = ~50 rows extended) |
| §6 Compliance Mapping table Corpus Manifest Path column | absent | present (7 sub-domain rows: D-08.1, D-08.2, D-08.3, D-09.1, D-09.2, D-09.3, D-09.4) |
| Frontmatter status | RECONCILED | CORPUS_ENRICHED |
| Frontmatter version | 1.1 | 1.2 |

**Enrichment details:**
- Each §4.x RACI table extended with Corpus Reg Req column: maps each activity row to the corpus sub-domain it covers and pulls the relevant regulatory article references (GDPR Art. X + NIS 2 Art. Y + CRA Art. Z + DORA Art. W + AI Act Art. V).
- §6 Compliance Mapping table (D-08.x + D-09.x) extended with Corpus Manifest Path column; 7 sub-domains mapped to their `*.manifest.json` paths in the corpus.
- Active_subdomains: 38 (verified unchanged from Sprint 1).
- Added Sprint 2 entry to Version History.

## 4. Frontmatter Status

All 4 docs transitioned from `RECONCILED` (Sprint 1 baseline) to `CORPUS_ENRICHED` (Sprint 2 deliverable). The status line in frontmatter + the comment line at top of each doc reflect the new state.

## 5. Proportionality (P2)

The enrichment is **proportionate for a MAXIMUM-tier credit institution** (5 applicable regulations, 38 active sub-domains, 5,000+ employees, ECB-supervised). The corpus adds substantive value without over-engineering:
- No new mandatory columns added to data tables beyond the 2-3 corpus-anchored columns (NIST + Manifest Path + Reg Req)
- No new sections added beyond what is needed for corpus cross-referencing (§4 Corpus Provenance, §2.1 Corpus fit_criteria, §2.1 + §6.1 Supply Chain references)
- The corpus is the **frozen regulatory baseline** — Case_03 docs draw from it without modifying it

## 6. Anti-Pattern Check (P0 + P5)

- **P0 (Reasoned Disagreement):** No decisions required reasoning against the user's input; this is pure enrichment.
- **P5 (Change Propagation):** Change propagation cost analysis:
  - 4 docs affected (target — within the <=3 ripple constraint)
  - 0 corpus files modified (constraint satisfied)
  - 0 legacy files modified (constraint satisfied)
  - 2 new docs filled (separate report)
  - 1 Excel regenerated (separate report)
  - Propagation within target scope.

## 7. Sprint 2 Completion

**Status:** COMPLETE for the 4 existing docs scope.

**Next sprint (Sprint 3):** Phase 2 strategic-tensions resolution — resolve top 10 HIGH-priority ambiguity cards from `05b_Ambiguity_Register.md`.

---

## N-1. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-08-06 | Executor | Sprint 2 corpus enrichment report for 4 existing docs. |
