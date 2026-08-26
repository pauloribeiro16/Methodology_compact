# Sprint 2 — Corpus Enrichment Report (New Docs + Excel)

**Case:** Case_03_OmniBank_Financial
**Sprint:** 2 (Corpus Enrichment — New Docs + Excel)
**Date:** 2026-08-06
**Author:** Executor
**Branch:** feature/aegis-p1-case03-rich
**Status:** CORPUS_ENRICHED on both new docs + Excel regenerated

---

## 1. Scope

This report documents the Sprint 2 deliverable of the **2 NEW docs** (`05b_Ambiguity_Register.md` + `Citation_Index.md`) and the **regenerated Excel** (`Case_03_Phase1_RICH.xlsx`). The 4 existing docs are covered in `SPRINT2_ENRICHMENT_REPORT_EXISTING.md`.

## 2. Excel Regeneration

### `Case_03_Phase1_RICH.xlsx`

| Metric | Before (Legacy) | After (Rich) |
|---|---:|---:|
| Sheets | 13 | 14 (added Corpus Cross-Reference) |
| Sheet list | COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, MATURITY, SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES | (same 13) + **Corpus Cross-Reference** |
| Total rows (existing sheets) | unchanged | unchanged |
| Total rows (Corpus Cross-Reference) | n/a | 39 (header + 38 sub-domain rows) |
| Total cols (Corpus Cross-Reference) | n/a | 18 |

**Enrichment details:**
- Copied legacy `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT/Case_03_Phase1.xlsx` to `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Case_03_Phase1_RICH.xlsx` (legacy file NOT modified).
- Added "Corpus Source" column to 7 data sheets (SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, MATURITY) with cross-reference pointers to the corresponding Rich docs.
- Added new sheet **Corpus Cross-Reference** with 38 rows (one per active sub-domain) and 18 columns:
  1. Sub-domain ID
  2. Sub-domain Name
  3. Participants (GDPR, CRA, NIS 2, DORA, AI Act)
  4. AI Act Status (present / partial / absent)
  5. GDPR Articles (list)
  6. CRA Articles (list)
  7. NIS 2 Articles (list)
  8. DORA Articles (list)
  9. AI Act Articles (list)
  10. NIST Anchors (GDPR)
  11. NIST Anchors (CRA)
  12. NIST Anchors (NIS 2)
  13. NIST Anchors (DORA)
  14. NIST Anchors (AI Act)
  15. NIST Anchors Combined (Unique)
  16. Manifest Path
  17. JSON Sidecar Path
  18. Articles Folder Path

**Per sub-domain (sample row, D-09.4):**
- Sub-domain ID: D-09.4
- Sub-domain Name: Records of Processing
- Participants: GDPR, NIS2, CRA, DORA, AI_Act (5 regulations)
- AI Act Status: present
- GDPR Articles: 15 (Art. 5(1)(a), 5(2), 12(1), 12(3), 12(5), 12(6), 13(1), 14(1)–(2), 21(1), 21(3), 23(1), 30(1)+(2), 30(5), 31, 33(1))
- CRA Articles: 19 (Art. 7(3)–(4), 13(1), 13(3), 13(4), 13(8), 13(17), 13(21), 14(2)(b), 14(2)(c), 14(5)(a), 14(8), 21, 32(2), 32(3), 32(5))
- NIS 2 Articles: 17 (Art. 21(1)–(4), 23(1), 24(1)–(2))
- DORA Articles: 49 (Art. 5(1)–(2), 7–16, 17(3), 18(3), 19(1)–(6), 21(1)–(3), 23, 28(1)–(4), 30(1)+(3))
- AI Act Articles: 0 (not in D-09.4 manifest)
- NIST Anchors Combined (Unique): GV.PO-01, GV.PO-02, ID.AM-08, ID.AM-08 (primary), ID.RA-05, PR.DS-12
- Manifest Path: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.manifest.json`
- JSON Sidecar Path: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.json`
- Articles Folder Path: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles`

## 3. New Doc — `05b_Ambiguity_Register.md` (AEGIS-P3-RICH-05b-AMBIG)

| Metric | Before (Placeholder) | After (Filled) |
|---|---:|---:|
| Lines | 57 | 1,026 |
| Status | PLACEHOLDER | CORPUS_ENRICHED |
| §1 Summary | absent | present (1,490 cards, 38 sub-domains) |
| §2 Per-Sub-Domain Breakdown | absent | present (38 rows + macro-domain aggregation) |
| §3 Top 20 Cards | absent | present (verbatim corpus + R1/R2/R3 readings) |
| §4 Recommended Disambiguation | absent | present (HIGH/MEDIUM/LOW priority tracks) |

**Enrichment details:**
- Aggregated 1,490 ambiguity cards from the corpus JSON sidecars across 38 sub-domains, filtered to Case_03 applicable regulations (GDPR + CRA + NIS 2 + DORA + AI Act).
- Per-sub-domain card counts documented (D-09.1 highest at 131; D-02.2 lowest at 9).
- Top 20 cards selected by **(severity × case-impact)** with diversity across sub-domains; each card reproduces the corpus entry verbatim with title, article ref, type, card variant, obligated party, obligation type, Berry anchor, and per-instance variant readings.
- Recommended disambiguation §4 documents resolution tracks (HIGH/MEDIUM/LOW) with RACI ownership.

**Macro-domain aggregation:**
- D-01 Data Protection: 108 cards
- D-02 Vulnerability Management: 118 cards
- D-03 Access Control: 149 cards
- D-04 Incident Response: 212 cards (highest — driven by D-04.3 multi-deadline notification)
- D-05 Data Lifecycle: 78 cards
- D-06 Supply Chain: 148 cards
- D-07 Secure Development: 75 cards
- D-08 Human Factors: 79 cards
- D-09 Governance & Documentation: 395 cards (highest macro — driven by D-09.1 + D-09.4)
- D-10 Monitoring & Audit: 128 cards

**Case_03-specific notes:**
- DORA contributes major share (38 clauses + Art. 5-16 ICT risk + Art. 17-19 incidents + Art. 28-30 ICT register)
- AI Act contributes Annex III high-risk cards (OmniScore AI Platform)
- GDPR + CRA + NIS 2 contribute baseline
- Top 20 prioritisation: HIGH = D-04.3 multi-deadline routing + D-06.3 contract templates + D-09.4 records of processing; MEDIUM = D-01.x encryption + D-06.1 vendor due diligence; LOW = remaining.

## 4. New Doc — `Citation_Index.md` (AEGIS-P3-RICH-CITATION)

| Metric | Before (Placeholder) | After (Filled) |
|---|---:|---:|
| Lines | 55 | 259 |
| Status | PLACEHOLDER | CORPUS_ENRICHED |
| Total unique citations | n/a | 122 across 6 Rich docs |
| Citations matched to corpus | n/a | ~115 (94%) |
| DECLARATION_GAP entries | n/a | 7 (6%) |
| Corpus verbatim article files | n/a | 137 unique (REG, Art.) pairs |

**Enrichment details:**
- §1 Citation Methodology + per-regulation breakdown table (GDPR 43, CRA 22, NIS 2 10, DORA 29, AI Act 18).
- §2 Per-regulation citation index (5 sub-sections: §2.1 GDPR, §2.2 CRA, §2.3 NIS 2, §2.4 DORA, §2.5 AI Act) with each unique citation linked to its corpus verbatim article file.
- §3 Coverage Gaps: 7 DECLARATION_GAP entries flagged (AI Act Art. 25 missing in corpus; sub-clause granularity for several GDPR/CRA/NIS 2/DORA articles).
- §4 Cross-reference matrix mapping each Phase 1 Rich doc to its top-cited articles + primary corpus source.

**Anti-hallucination:** Every regulatory reference is either (a) linked to a corpus verbatim article file, or (b) marked as DECLARATION_GAP with mitigation. No reference is presented without corpus backing.

## 5. Frontmatter Status

Both new docs transitioned from `PLACEHOLDER` to `CORPUS_ENRICHED`.

## 6. Sprint 2 Completion

**Status:** COMPLETE for the new docs + Excel scope.

**Combined Sprint 2 deliverable (with `SPRINT2_ENRICHMENT_REPORT_EXISTING.md`):**
- 4 existing docs enriched (04a, 04b, 04c, 04d)
- 2 new docs filled (05b, Citation_Index.md)
- 1 Excel regenerated (Case_03_Phase1_RICH.xlsx)
- All 6 Phase 1 Rich docs status = CORPUS_ENRICHED

---

## N-1. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-08-06 | Executor | Sprint 2 corpus enrichment report for 2 new docs + Excel. |
