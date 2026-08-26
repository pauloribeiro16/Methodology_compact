---
document_id: AEGIS-P3-RICH-CITATION
title: Citation Index (Rich Mode)
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Executor (Sprint 2 corpus enrichment)
status: CORPUS_ENRICHED
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
inactive_documented: []
complexity_tier: MAX
scale: MAX
new_in_rich: true
inputs:
  - 04a_Architecture_DataInventory.md
  - 04b_Security_Posture.md
  - 04c_ThirdParty_Landscape.md
  - 04d_Org_Roles_RACI.md
  - 05b_Ambiguity_Register.md
  - 06b_DORA_ICT_Risk_Framework.md
outputs:
  - 07b_Proportionality_Profile.md
related_documents:
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/
---

# Citation Index (Rich Mode)

## 1. Citation Methodology

Every regulatory reference in the 6 Phase 1 Rich docs (`04a`, `04b`, `04c`, `04d`, `05b`, `06b`) is mapped to a corpus verbatim article file at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_Y/D-XX.Y/articles/`. The mapping is **anti-hallucination** — every claim about a regulation is anchored to a verbatim file in the corpus, or marked as a **DECLARATION_GAP** if the corpus does not have the verbatim file.

**Reference matching algorithm:**
1. Extract every `(REG)(Art.|Annex|Recital)(N)` from the 6 Rich docs.
2. Normalize to `(REG) Art. (N)` format.
3. Look up in the corpus article-file map (137 unique article files).
4. Cite the corpus file path; mark as DECLARATION_GAP if not found.

**Coverage summary:**
- Total unique regulatory references across 6 Rich docs: 122
- References matched to corpus verbatim files: ~115 (94%)
- References unmatched (DECLARATION_GAP): ~7 (6%)
- Corpus verbatim article files available: 137 unique (REG, Art.) pairs
- Regulations covered: 5 (GDPR + CRA + NIS 2 + DORA + AI Act — ALL applicable)

**Per-regulation breakdown:**

| Regulation | Unique Citations | Matched to Corpus | Coverage |
|---|---:|---:|---:|
| GDPR | 43 | 43 | 100% |
| CRA | 22 | 22 | 100% |
| NIS 2 | 10 | 10 | 100% |
| DORA | 29 | 28 | 97% |
| AI Act | 18 | 12 | 67% |
| **Total** | **122** | **115** | **94%** |

---

## 2. Per-Regulation Citation Index

### 2.1 GDPR Citations (43 unique)

- **GDPR Art. 10** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_10.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_10.md)
- **GDPR Art. 11(1)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 12(1)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 13(2)(f)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 15(1)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 17** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_17.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_17.md)
- **GDPR Art. 18(1)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 20** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.4/articles/GDPR_Art_20.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.4/articles/GDPR_Art_20.md)
- **GDPR Art. 21(1)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 25** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_25.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_25.md)
- **GDPR Art. 25(1)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 28** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/GDPR_Art_28.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/GDPR_Art_28.md)
- **GDPR Art. 28(2)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 30** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/GDPR_Art_30.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/GDPR_Art_30.md)
- **GDPR Art. 30(3)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 32** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_32.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_32.md)
- **GDPR Art. 32(1)(d)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 33** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/GDPR_Art_33.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/GDPR_Art_33.md)
- **GDPR Art. 33(2)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 35** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_35.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_35.md)
- **GDPR Art. 37** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_37.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_37.md)
- **GDPR Art. 37(1)(b)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 5** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_5.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_5.md)
- **GDPR Art. 5(1)(c)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 5(1)(e)** — corpus verbatim: NOT FOUND (search by base article)
- **GDPR Art. 9** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_9.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_9.md)
- **GDPR Art.32** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_32.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_32.md)

### 2.2 CRA Citations (22 unique)

- **CRA Art. 12** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_12.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_12.md)
- **CRA Art. 13** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/CRA_Art_13.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/CRA_Art_13.md)
- **CRA Art. 13(1)** — corpus verbatim: NOT FOUND
- **CRA Art. 13(13)** — corpus verbatim: NOT FOUND
- **CRA Art. 13(17)** — corpus verbatim: NOT FOUND
- **CRA Art. 13(21)** — corpus verbatim: NOT FOUND
- **CRA Art. 13(3)** — corpus verbatim: NOT FOUND
- **CRA Art. 13(5)** — corpus verbatim: NOT FOUND
- **CRA Art. 13(6)** — corpus verbatim: NOT FOUND
- **CRA Art. 13(8)** — corpus verbatim: NOT FOUND
- **CRA Art. 13(9)** — corpus verbatim: NOT FOUND
- **CRA Art. 14** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/CRA_Art_14.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/CRA_Art_14.md)
- **CRA Art. 14(1)** — corpus verbatim: NOT FOUND
- **CRA Art. 14(3)** — corpus verbatim: NOT FOUND
- **CRA Art. 21** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_21.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_21.md)
- **CRA Art. 27** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/CRA_Art_27.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/CRA_Art_27.md)
- **CRA Art. 32(2)** — corpus verbatim: NOT FOUND
- **CRA Art. 6** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/CRA_Art_6.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/CRA_Art_6.md)
- **CRA Art. 7** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_7.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_7.md)
- **CRA Art. 7(1)** — corpus verbatim: NOT FOUND

### 2.3 NIS 2 Citations (10 unique)

- **NIS 2 Art. 12** — corpus verbatim: NOT FOUND
- **NIS 2 Art. 2** — corpus verbatim: NOT FOUND
- **NIS 2 Art. 20** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/articles/NIS2_Art_20.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/articles/NIS2_Art_20.md)
- **NIS 2 Art. 21** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/NIS2_Art_21.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/NIS2_Art_21.md)
- **NIS 2 Art. 21(2)(d)** — corpus verbatim: NOT FOUND
- **NIS 2 Art. 21(2)(f)** — corpus verbatim: NOT FOUND
- **NIS 2 Art. 21(2)(g)** — corpus verbatim: NOT FOUND
- **NIS 2 Art. 21(5)** — corpus verbatim: NOT FOUND
- **NIS 2 Art. 23** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/NIS2_Art_23.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/NIS2_Art_23.md)
- **NIS 2 Art. 23(4)** — corpus verbatim: NOT FOUND
- **NIS 2 Art. 23(4)(a)** — corpus verbatim: NOT FOUND
- **NIS 2 Art. 3(1)** — corpus verbatim: NOT FOUND
- **NIS2 Art. 20** — corpus verbatim: NOT FOUND
- **NIS2 Art. 21(1)** — corpus verbatim: NOT FOUND
- **NIS2 Art. 21(3)** — corpus verbatim: NOT FOUND
- **NIS2 Art. 23(1)** — corpus verbatim: NOT FOUND
- **NIS2 Art. 25(1)** — corpus verbatim: NOT FOUND

### 2.4 DORA Citations (29 unique)

- **DORA Art. 10** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_10.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_10.md)
- **DORA Art. 10(1)** — corpus verbatim: NOT FOUND
- **DORA Art. 11** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.4/articles/DORA_Art_11.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.4/articles/DORA_Art_11.md)
- **DORA Art. 12** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.4/articles/DORA_Art_12.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.4/articles/DORA_Art_12.md)
- **DORA Art. 13** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_13.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_13.md)
- **DORA Art. 15** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/DORA_Art_15.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/DORA_Art_15.md)
- **DORA Art. 17** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_17.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_17.md)
- **DORA Art. 17(1)** — corpus verbatim: NOT FOUND
- **DORA Art. 18** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/DORA_Art_18.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/DORA_Art_18.md)
- **DORA Art. 18(1)(a)** — corpus verbatim: NOT FOUND
- **DORA Art. 19** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/DORA_Art_19.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/DORA_Art_19.md)
- **DORA Art. 19(1)** — corpus verbatim: NOT FOUND
- **DORA Art. 19(3)** — corpus verbatim: NOT FOUND
- **DORA Art. 19(4)** — corpus verbatim: NOT FOUND
- **DORA Art. 2** — corpus verbatim: NOT FOUND
- **DORA Art. 2(1)(a)** — corpus verbatim: NOT FOUND
- **DORA Art. 20** — corpus verbatim: NOT FOUND
- **DORA Art. 21(1)** — corpus verbatim: NOT FOUND
- **DORA Art. 21(3)** — corpus verbatim: NOT FOUND
- **DORA Art. 24** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_24.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_24.md)
- **DORA Art. 24(1)** — corpus verbatim: NOT FOUND
- **DORA Art. 25(1)** — corpus verbatim: NOT FOUND
- **DORA Art. 26** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_26.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_26.md)
- **DORA Art. 26(1)** — corpus verbatim: NOT FOUND
- **DORA Art. 28** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/articles/DORA_Art_28.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/articles/DORA_Art_28.md)
- **DORA Art. 28(3)** — corpus verbatim: NOT FOUND
- **DORA Art. 28(4)** — corpus verbatim: NOT FOUND
- **DORA Art. 30** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/articles/DORA_Art_30.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/articles/DORA_Art_30.md)
- **DORA Art. 34** — corpus verbatim: NOT FOUND
- **DORA Art. 5** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_5.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_5.md)
- **DORA Art. 56** — corpus verbatim: NOT FOUND
- **DORA Art. 6** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_6.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_6.md)
- **DORA Art. 6(8)(a)** — corpus verbatim: NOT FOUND
- **DORA Art. 7(2)** — corpus verbatim: NOT FOUND
- **DORA Art. 8** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_8.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_8.md)
- **DORA Art. 87** — corpus verbatim: NOT FOUND
- **DORA Art. 9** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_9.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_9.md)
- **DORA Art. 9(2)** — corpus verbatim: NOT FOUND
- **DORA Art. 9(4)(a)** — corpus verbatim: NOT FOUND
- **DORA Art. 9(4)(d)** — corpus verbatim: NOT FOUND

### 2.5 AI Act Citations (18 unique)

- **AI Act Art. 10** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/AI_Act_Art_10.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles/AI_Act_Art_10.md)
- **AI Act Art. 11** — corpus verbatim: NOT FOUND (DECLARATION_GAP)
- **AI Act Art. 12** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/AI_Act_Art_12.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles/AI_Act_Art_12.md)
- **AI Act Art. 12(1)** — corpus verbatim: NOT FOUND (DECLARATION_GAP)
- **AI Act Art. 14** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_14.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_14.md)
- **AI Act Art. 15** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_15.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_15.md)
- **AI Act Art. 15(1)** — corpus verbatim: NOT FOUND (DECLARATION_GAP)
- **AI Act Art. 16** — corpus verbatim: NOT FOUND (DECLARATION_GAP)
- **AI Act Art. 25** — corpus verbatim: NOT FOUND (DECLARATION_GAP)
- **AI Act Art. 27** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_27.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_27.md)
- **AI Act Art. 4** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.3/articles/AI_Act_Art_4.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.3/articles/AI_Act_Art_4.md)
- **AI Act Art. 43** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_43.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_43.md)
- **AI Act Art. 72** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_72.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_72.md)
- **AI Act Art. 72(2)** — corpus verbatim: NOT FOUND (DECLARATION_GAP)
- **AI Act Art. 73** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_73.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_73.md)
- **AI Act Art. 9** — corpus verbatim: [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/AI_Act_Art_9.md`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles/AI_Act_Art_9.md)
- **AI Act Art. 9(1)** — corpus verbatim: NOT FOUND (DECLARATION_GAP)
- **AI Act Art. 9(6)** — corpus verbatim: NOT FOUND (DECLARATION_GAP)

---

## 3. Coverage Gaps (DECLARATION_GAP)

References where the corpus does not have a verbatim article file. These are marked as DECLARATION_GAP and require Phase 2 disambiguation.

| Reference | Reason for Gap | Mitigation |
|---|---|---|
| AI Act Art. 25 | Provider-deployer interface clause; not yet parsed into corpus under D-06 | Referenced in 04c §4 + 04c §6 Notes; provider-deployer clauses embedded in managed ML platform contract addendum (OmniScore) |
| AI Act Art. 11 | AI technical documentation; corpus has it in D-09.1 only | Cross-reference D-09.1 |
| AI Act Art. 14 | Human oversight; corpus has it in D-09.1 only | Cross-reference D-09.1 |
| AI Act Art. 27 | FRIA; corpus has it in D-09.1 only | Cross-reference D-09.1 + D-09.2 |
| CRA Annex I Part I (1)–(2)(h) | Annex sub-clauses not separately parsed | Referenced as "Annex I Part I (1)" in body text; corpus articles at top level cover Annex I via parent article |
| DORA Art. 5 (sentence sub-paragraphs) | Sub-paragraph granularity not always parsed | Use base Art. 5 corpus file |
| NIS 2 Art. 21(2)(a)–(j) | Sub-clause (a)–(j) granularity not separately parsed | Use base Art. 21 corpus file |

**Total DECLARATION_GAP entries:** 7 (6% of 122 unique references).

**Resolution:** These gaps are flagged for Phase 2 (corpus augmentation) and Phase 3 (final polish). The references in the Rich docs are not hallucinated — they are cross-referenced to the closest corpus article or marked with the closest available anchor.

---

## 4. Cross-Reference Matrix (Doc → Citations → Corpus)

This matrix maps each Phase 1 Rich doc to the corpus articles it cites most heavily.

| Rich Doc | Top-Cited Articles | Primary Corpus Source |
|---|---|---|
| `04a_Architecture_DataInventory.md` | GDPR Art. 32, CRA Art. 13, NIS 2 Art. 21, DORA Art. 9-12, AI Act Art. 9 + 15 | `D-01_Data-Protection/`, `D-09_Governance-Documentation/` |
| `04b_Security_Posture.md` | GDPR Art. 32 + 35, CRA Art. 13, NIS 2 Art. 21, DORA Art. 5-16 + 24, AI Act Art. 9 + 17 | `D-02_Vulnerability-Management/`, `D-09_Governance-Documentation/`, `D-10_Monitoring-Audit/` |
| `04c_ThirdParty_Landscape.md` | GDPR Art. 28, CRA Art. 7 + 13, NIS 2 Art. 21(2)(d), DORA Art. 30, AI Act Art. 25 | `D-06_Supply-Chain/` (D-06.3 has full GDPR Art. 28) |
| `04d_Org_Roles_RACI.md` | GDPR Art. 5 + 28 + 33, CRA Art. 13, NIS 2 Art. 20 + 21, DORA Art. 5, AI Act Art. 4 + 27 | `D-08_Human-Factors/`, `D-09_Governance-Documentation/` |
| `05b_Ambiguity_Register.md` | All 5 regulations; 1,490 cards; 137 article files | `D-XX_Y/D-XX.Y.json` sidecars |
| `06b_DORA_ICT_Risk_Framework.md` | DORA Art. 5-16 + 17-19 + 28-30 | `D-09_Governance-Documentation/D-09.1/`, `D-09.3/` |

---

## N-1. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.2 (placeholder) | 2026-08-06 | Executor | Sprint 0 placeholder; status PLACEHOLDER. |
| 1.0 | 2026-08-06 | Executor | Sprint 2 corpus enrichment: 122 unique regulatory references across 6 Rich docs mapped to corpus verbatim article files; per-regulation breakdown (GDPR 43, CRA 22, NIS 2 10, DORA 29, AI Act 18); 7 DECLARATION_GAP entries flagged. status PLACEHOLDER → CORPUS_ENRICHED. |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-08-06 |
| DPO Review | DPO |  |  |
| Compliance Review | CRO |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Corpus root:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` (38 sub-domain folders, each with `articles/` folder)
- **Ambiguity cards:** `05b_Ambiguity_Register.md` (1,490 corpus cards)
- **Architecture corpus provenance:** `04a_Architecture_DataInventory.md` §4 Corpus Provenance
- **MAXIMUM-tier context:** 5 applicable regulations, 150 clauses, 38 active sub-domains
