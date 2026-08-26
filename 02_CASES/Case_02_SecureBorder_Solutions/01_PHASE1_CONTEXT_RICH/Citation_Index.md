---
document_id: AEGIS-P2-RICH-CITATION
title: Citation Index (Rich Mode)
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Executor (Sprint 2 Corpus Enrichment)
status: CORPUS_ENRICHED
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 35
inactive_documented: [D-08.3 INACTIVE, 3 NOT_ADDRESSED]
new_in_rich: true
inputs: [07c_Adjusted_Objectives.md]
outputs: []
---

# Citation Index

## 1. Summary

This index maps every regulatory reference used in the Case_02 Phase 1 Rich docs to its verbatim source article in the AEGIS corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`. It is the **anti-hallucination control** for the case: every `Art. N`, `Annex X`, or `Recital N` citation appearing in Case_02 Rich docs must resolve to a corpus file here.

- **Unique regulatory references in Rich docs:** 41
- **Corpus coverage (case-applicable regs):** GDPR=14, CRA=6, NIS 2=4, AI_Act=9
- **Coverage gaps (Rich ref → no corpus file):** 4

## 2. GDPR Citations

Each entry: Rich-doc reference → corpus verbatim file path + frontmatter title.

| Reference | Corpus file | Title (from frontmatter) |
|---|---|---|
| GDPR Art. 17 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/GDPR_Art_17.md` | GDPR Art. 17 — SecurityObjectives & SecurityRules |
| GDPR Art. 20 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.4/articles/GDPR_Art_20.md` | GDPR Art. 20 — SecurityObjectives & SecurityRules |
| GDPR Art. 28 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_28.md` | GDPR Art. 28 — SecurityObjectives & SecurityRules |
| GDPR Art. 30 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_30.md` | GDPR Art. 30 — SecurityObjectives & SecurityRules |
| GDPR Art. 32 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_32.md` | GDPR Art. 32 — SecurityObjectives & SecurityRules |
| GDPR Art. 33 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles/GDPR_Art_33.md` | GDPR Art. 33 — SecurityObjectives & SecurityRules |
| GDPR Art. 35 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_35.md` | GDPR Art. 35 — SecurityObjectives & SecurityRules |
| GDPR Art. 37 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_37.md` | GDPR Art. 37 — SecurityObjectives & SecurityRules |
| GDPR Art. 39 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_39.md` | GDPR Art. 39 — SecurityObjectives & SecurityRules |
| GDPR Art. 4 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_4.md` | GDPR Art. 4 — SecurityObjectives & SecurityRules |
| GDPR Art. 5 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_5.md` | GDPR Art. 5 — SecurityObjectives & SecurityRules |
| GDPR Art. 9 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_9.md` | GDPR Art. 9 — SecurityObjectives & SecurityRules |
| GDPR Art.32 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_32.md` | GDPR Art. 32 — SecurityObjectives & SecurityRules |
| GDPR Article 28 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_28.md` | GDPR Art. 28 — SecurityObjectives & SecurityRules |

## 3. CRA Citations

| Reference | Corpus file | Title (from frontmatter) |
|---|---|---|
| CRA Art. 13 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.4/articles/CRA_Art_13.md` | CRA Art. 13 — SecurityObjectives & SecurityRules |
| CRA Art. 14 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/CRA_Art_14.md` | CRA Art. 14 — SecurityObjectives & SecurityRules |
| CRA Art. 24 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/CRA_Art_24.md` | CRA Art. 24 — SecurityObjectives & SecurityRules |
| CRA Art. 32 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_32.md` | CRA Art. 32 — SecurityObjectives & SecurityRules |
| CRA Art. 7 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_7.md` | CRA Art. 7 — SecurityObjectives & SecurityRules |
| CRA Art. 8 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/CRA_Art_8.md` | CRA Art. 8 — SecurityObjectives & SecurityRules |

## 4. NIS 2 Citations

| Reference | Corpus file | Title (from frontmatter) |
|---|---|---|
| NIS 2 Art. 20 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/NIS2_Art_20.md` | NIS2 Art. 20 — SecurityObjectives & SecurityRules |
| NIS 2 Art. 21 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/NIS2_Art_21.md` | NIS2 Art. 21 — SecurityObjectives & SecurityRules |
| NIS 2 Art. 22 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/NIS2_Art_22.md` | NIS2 Art. 22 — SecurityObjectives & SecurityRules |
| NIS 2 Art. 23 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/NIS2_Art_23.md` | NIS2 Art. 23 — SecurityObjectives & SecurityRules |
| NIS 2 Art. 3 | _(no corpus file)_ | _(missing)_ |

## 5. AI_Act Citations

| Reference | Corpus file | Title (from frontmatter) |
|---|---|---|
| AI_Act Annex III | _(no corpus file)_ | _(missing)_ |
| AI_Act Art. 10 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/AI_Act_Art_10.md` | AI_Act Art. 10 — SecurityObjectives & SecurityRules |
| AI_Act Art. 12 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/AI_Act_Art_12.md` | AI_Act Art. 12 — SecurityObjectives & SecurityRules |
| AI_Act Art. 16 | _(no corpus file)_ | _(missing)_ |
| AI_Act Art. 25 | _(no corpus file)_ | _(missing)_ |
| AI_Act Art. 27 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_27.md` | AI_Act Art. 27 — SecurityObjectives & SecurityRules |
| AI_Act Art. 4 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.3/articles/AI_Act_Art_4.md` | AI_Act Art. 4 — SecurityObjectives & SecurityRules |
| AI_Act Art. 43 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/AI_Act_Art_43.md` | AI_Act Art. 43 — SecurityObjectives & SecurityRules |
| AI_Act Art. 5 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_5.md` | AI_Act Art. 5 — SecurityObjectives & SecurityRules |
| AI_Act Art. 72 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.2/articles/AI_Act_Art_72.md` | AI_Act Art. 72 — SecurityObjectives & SecurityRules |
| AI_Act Art. 73 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.2/articles/AI_Act_Art_73.md` | AI_Act Art. 73 — SecurityObjectives & SecurityRules |
| AI_Act Art. 9 | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.2/articles/AI_Act_Art_9.md` | AI_Act Art. 9 — SecurityObjectives & SecurityRules |

## 6. DORA Citations (informational only — DORA does not apply to Case_02)

DORA is excluded from Case_02's applicable_regs; DORA references appear only in the corpus as participants of certain sub-domains, and may surface in DeepAnalysis docs.

| Reference | Corpus file | Title (from frontmatter) |
|---|---|---|

## 7. Coverage Gaps

The following Rich-doc references could NOT be resolved to a corpus article file. These require follow-up: either the reference is a typo / variant form, or the corpus is missing the corresponding article split.

| Reference | Reason | Suggested action |
|---|---|---|
| AI_Act Art. 16 | No corpus file matches | Verify in corpus or fix reference |
| AI_Act Art. 25 | No corpus file matches | Verify in corpus or fix reference |
| DORA Art. 2 | No corpus file matches | Verify in corpus or fix reference |
| NIS 2 Art. 3 | No corpus file matches | Verify in corpus or fix reference |

## 8. Coverage Statistics (corpus file count by regulation)

| Regulation | Corpus article files |
|---|---:|
| GDPR | 218 |
| CRA | 117 |
| NIS 2 | 49 |
| AI_Act | 70 |
| DORA | 169 |

---

## N. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-08-06 | Executor | Sprint 2 fill: indexed 41 unique regulatory references from Rich docs; cross-referenced to 623 corpus article files; reported 4 coverage gap(s). |

## N. See also

- **Corpus source:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` (per-sub-domain `articles/` folders contain verbatim `<REG>_Art_<N>.md` files)
- **NIST CSF 2.0 lookup:** `00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md`
- **Anti-hallucination lint:** `01_IMPLEMENTATION_TOOLS/lints/lint_regulatory_references.py`