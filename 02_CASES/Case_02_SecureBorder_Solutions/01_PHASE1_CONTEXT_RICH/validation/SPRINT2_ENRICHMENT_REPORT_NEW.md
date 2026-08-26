# SPRINT2 ENRICHMENT REPORT — NEW DOCS

**Date:** 2026-08-06  
**Sprint:** 2 — Corpus Enrichment  
**Case:** Case_02_SecureBorder_Solutions  
**Scope:** 2 new Rich-only docs (05b_Ambiguity_Register + Citation_Index) + Excel regeneration  
**Executor role:** Sprint 2 enrichment of placeholder → full content  

---

## 1. Summary

Sprint 2 filled the 2 Rich-only docs that were Sprint-0 placeholders, and regenerated the Excel companion for Case_02. Both placeholders (`05b_Ambiguity_Register.md` and `Citation_Index.md`) transitioned from `status: DRAFT (placeholder)` to `status: CORPUS_ENRICHED` with substantive content.

**Line-count delta (new docs):**

| Doc | Pre-Sprint 2 | Post-Sprint 2 | Δ |
|---|---:|---:|---:|
| `05b_Ambiguity_Register.md` | 52 | 633 | +581 |
| `Citation_Index.md` | 53 | 128 | +75 |

**Total:** 105 → 761 (+656 lines)

---

## 2. Per-Doc Change List

### 2.1 `05b_Ambiguity_Register.md` (Sprint 2 fill)

**Pre-Sprint-2 state:** 52-line placeholder with status `DRAFT (placeholder)`, planned-content outline only.

**Post-Sprint-2 content:**

- **§1 Summary** — Berry lens (4 categories VAG/POLY/SCOPE/COORD × severity S1-S3), aggregate counts.
- **§2 Per-Sub-Domain Breakdown** — table of 38 rows (sorted by card count desc); total 1071 cards across all 38 sub-domains (filtered to GDPR + CRA + NIS 2 + AI_Act).
- **§3 Top-20 Cards** — verbatim corpus text per card including: regulation, clause_id, article_ref, title, Berry type, severity, verbatim phrase, analysis, R1/R2/R3 variant readings.
- **§4 Recommended Disambiguation** — 7 conventions for the Case-02 reading choice per ambiguous term (state of the art, appropriate, deletes, sufficient guarantees, incident, substantial public interest, high-risk AI).
- **N. Version History + See also** — v1.0 row + cross-references to corpus + Berry framework.

**Line count:** 52 → 633 (+581 lines).

### 2.2 `Citation_Index.md` (Sprint 2 fill)

**Pre-Sprint-2 state:** 53-line placeholder with status `DRAFT (placeholder)`, planned-content outline only.

**Post-Sprint-2 content:**

- **§1 Summary** — index scope, aggregate counts (41 unique regulatory references found in Rich docs; corpus coverage GDPR=14, CRA=6, NIS 2=4, AI_Act=9; 4 coverage gaps).
- **§2 GDPR Citations** — 14 references → corpus verbatim file paths + frontmatter titles.
- **§3 CRA Citations** — 6 references → corpus verbatim file paths + frontmatter titles.
- **§4 NIS 2 Citations** — 4 references → corpus verbatim file paths + frontmatter titles.
- **§5 AI_Act Citations** — 9 references → corpus verbatim file paths + frontmatter titles.
- **§6 DORA Citations** — informational only (DORA does not apply to Case_02).
- **§7 Coverage Gaps** — 4 gaps reported with suggested actions: `NIS 2 Art. 3`, `AI_Act Annex III`, `AI_Act Art. 16`, `AI_Act Art. 25`.
- **§8 Coverage Statistics** — corpus file counts per regulation (GDPR=218, CRA=117, NIS 2=49, AI_Act=70, DORA=169).
- **N. Version History + See also** — v1.0 row + cross-references to corpus + NIST CSF + anti-hallucination lint.

**Line count:** 53 → 128 (+75 lines).

### 2.3 `Case_02_Phase1_RICH.xlsx` (Sprint 2 regenerate)

**Source:** Copy of legacy `Case_02_Phase1.xlsx` (13 sheets) + corpus enrichment.

**Sprint 2 changes:**

- **New sheet `CORPUS_SUMMARY`** — Sprint 2 enrichment summary (inserted at position 0).
- **New column `Corpus Source`** added to all 12 data sheets (SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, MATURITY, SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES).
- **New sheet `Corpus Cross-Reference`** — 38 rows (one per sub-domain) with: Sub-domain ID, name, Participants (Case_02), Applicable Articles per regulation, NIST CSF per regulation, Manifest path, JSON sidecar path, Articles folder path, Status (Case_02).

**Final sheet list (15 sheets):**

```
CORPUS_SUMMARY, COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA,
THIRD_PARTIES, ROLES_RACI, MATURITY, SUBDOMAINS, REG_CHAIN, COMPLIANCE,
GAPS, PRIORITIES, Corpus Cross-Reference
```

---

## 3. Cross-Doc Consistency

- **`case: Case_02_SecureBorder_Solutions`** — consistent across both new docs.
- **`applicable_regs: [GDPR, CRA, NIS 2, AI_Act]`** — consistent.
- **`active_subdomains: 35`** — consistent.
- **`status: CORPUS_ENRICHED`** — both new docs transition from `DRAFT (placeholder)` to corpus-enriched.

---

## 4. AEGIS P-Principle Conformance

- **P0 Reasoned Disagreement** — Ambiguity Register (05b) surfaces the *open* Berry cards for Phase 2/3 resolution; the recommended Case-02 reading is the strict-but-defensible interpretation, not the loose one.
- **P1 Compliant ≠ Secure** — Citation_Index is the anti-hallucination control; it ties every Rich-doc regulatory reference to a frozen corpus verbatim file.
- **P6 Start From Reality** — Both new docs use only corpus-sourced data; no fabricated content.
- **P5 Change Propagation** — Only the 2 target placeholders + Excel modified; no other files affected.

---

## 5. Status

**Sprint 2 fill of new docs + Excel regeneration: COMPLETE.**

- 2 new docs transitioned from `DRAFT (placeholder)` to `status: CORPUS_ENRICHED` with substantive content.
- 1 Excel companion regenerated with `Corpus Source` columns + 2 new sheets.