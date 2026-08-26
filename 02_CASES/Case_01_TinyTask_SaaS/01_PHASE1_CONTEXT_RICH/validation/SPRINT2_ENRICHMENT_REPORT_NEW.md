# Sprint 2 Enrichment Report (Round 2)

> **Updated 2026-08-06** — this report supersedes the prior version, which was generated before the corpus augmentation commit (c101676, "Corpus augmentation (38/38 sub-domain .md, 48 manifests, 38 sidecars, 623 articles)"). All numbers reflect the post-augmentation corpus.

## 1. Summary

Enriched two NEW Rich Phase 1 docs from the corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`:

| Doc | Status | Lines | Task |
|-----|--------|-------|------|
| `05b_Ambiguity_Register.md` | PLACEHOLDER → CORPUS_ENRICHED | 64 → 918 | Task 1 |
| `Citation_Index.md` | PLACEHOLDER → CORPUS_ENRICHED | 57 → 132 | Task 2 |

Both files were flipped from `status: PLACEHOLDER` to `status: CORPUS_ENRICHED` (Task 3). No other Rich docs modified. No corpus files modified. No legacy Phase 1 docs touched.

## 2. Methodology

### 2.1 Sub-domain scoping

The Executor prompt listed 31 active sub-domains, but `04a_Architecture_DataInventory.md` (lines 21–22) canonically declares `active_subdomains: 37; inactive_subdomains: [D-08.3]`. The 37-sub-domain reading matches the Compliance Mapping table (lines 119–156, which lists D-01.1–D-10.3 with D-08.3 omitted). **Per principle P0, I used the 37-sub-domain reading from the canonical doc** rather than the 31 listed in the prompt.

The six sub-domains in the corpus but missing from the prompt's `ACTIVE_SD` are: D-02.4, D-06.4, D-07.2, D-07.3, D-07.4, D-09.3. They are all GDPR + CRA applicable and were therefore included.

### 2.2 Ambiguity card extraction

For each of 37 active sub-domains:
- Loaded `D-XX.Y/D-XX.Y.json`
- Filtered `ambiguity_cards[]` by `regulation ∈ {GDPR, CRA}` (Case_01 `applicable_regs`)
- Preserved all instance-level fields verbatim: `phrase`, `severity`, `variant_readings[]`, `analysis_text`

### 2.3 Citation index extraction

Scanned all `.md` files in `01_PHASE1_CONTEXT_RICH/` with regex `(GDPR|CRA|NIS\s*2|DORA|AI\s*Act)\s+(Art\.?\s*\d+(\([0-9a-z]+\))*|Annex\s+[IVX]+|Recital\s+\d+)`. Excluded meta-docs (`README.md`, `corpus_field_map.md`, `phase1_ontology.yaml`, `Case_01_Phase1_RICH.xlsx`).

For each unique (regulation, reference) pair, computed:
- Which Rich docs cite it
- The first corpus match by glob `**/<REG>_<TYPE>_<ID>.md`

## 3. Doc 05b statistics

- **Total in-scope ambiguity cards:** 417 (276 GDPR + 141 CRA)
- **Sub-domains with ≥1 in-scope card:** 37/37 (every active sub-domain has at least one card)
- **Per-instance severity:** S1=0, S2=251, S3=252 (across 503 instances total)
- **Top 20 cards documented:** severity-sorted, sub-domain-grouped, verbatim corpus phrasing preserved
- **Per-sub-domain distribution** (selected, top 5 by card count): D-09.1 (53), D-04.3 (34), D-09.4 (33), D-05.1 (27), D-03.1 (21) / D-06.3 (23) / D-09.2 (23)

### 3.1 Card-variant notes

Two corpus card variants encountered:
- **`GDPR-light`**: structured `variant_readings[]` array with `{id, reading, source}` triples.
- **`source-locus`** (most CRA cards): variant readings embedded as Markdown tables inside `instances[].analysis_text`; `variant_readings[]` is empty.

Both variants preserved verbatim in the §3 Top 20 section; readers must consult `analysis_text` for CRA cards to extract R1/R2/R3 readings.

### 3.2 Recommended disambiguation priorities

Top 5 by case impact (severity × cross-SD propagation × TinyTask-specific risk):
1. **GDPR-CP02 / Art. 25(1)** — PbD "state of the art" anchors all design-time decisions.
2. **GDPR-CP15 / Art. 32(1)** — canonical security obligation; "state of the art" + "appropriate" + 4-element list ambiguity.
3. **GDPR-CP19 / Art. 34(1)** — high-risk threshold (3 undefined qualifiers) is the breach-notification litigation question.
4. **CRA-CL02 / Art. 6(a) proviso** — "properly installed/maintained" must be defensible against CRA market-surveillance audits.
5. **GDPR-RT16 / Art. 21(1)** — objection grounds trigger controller balancing test; EDPB Guidelines are the only authoritative reading.

## 4. Citation Index statistics

- **Rich docs scanned:** 13
- **Total reference mentions:** 29
- **Unique (reg, reference) pairs:** 18
- **Unique article filenames:** 15
- **Found in corpus:** 12/15
- **Coverage gaps:** 3 (see §6 below)

### 4.1 Per-regulation breakdown

| Regulation | Unique refs | Found in corpus |
|------------|-------------|-----------------|
| GDPR | 9 | 9 |
| CRA | 8 | 6 |
| NIS 2 | 1 | 0 (not applicable) |

### 4.2 Most-cited references

| Reference | Citing docs |
|-----------|-------------|
| GDPR Art. 32 | 5 |
| CRA Annex I | 4 |
| GDPR Art. 28 | 2 |
| GDPR Art. 30 | 2 |
| GDPR Art. 33 | 2 |
| CRA Art. 14 | 2 |

## 5. Coverage gaps (corpus augmentation targets)

| Gap | Cited in | Reason |
|-----|----------|--------|
| CRA Annex I | 04b, 04c, 04d, 05b | Corpus contains CRA Articles only — no Annexes. High-value augmentation target (essential cybersecurity requirements). |
| CRA Annex VII | 04d | Same as above (conformity-assessment procedures). |
| NIS 2 Annex I | 01_INTAKE_FORM | NIS 2 not applicable to Case_01 — reference appears in scope-exclusion context only. Corpus gap is non-blocking. |

## 6. Issues encountered

### 6.1 Sub-domain count discrepancy (resolved)

Executor prompt listed 31 active sub-domains; canonical doc (04a) declares 37. Resolved by following the canonical doc.

### 6.2 No Annex files in corpus

The corpus (c101676) contains 623 CRA Articles + GDPR Articles + NIS 2 Articles + DORA Articles + AI Act Articles, but no Annex files. CRA Annex I and VII (both heavily cited) are coverage gaps. This is **a corpus-level issue**, not an Executor error. Recommendation: add `CRA_Annex_I.md` and `CRA_Annex_VII.md` to the corpus in a future corpus-augmentation sprint.

### 6.3 Self-reference in cross-citation map

`05b_Ambiguity_Register.md` legitimately contains corpus references (it documents verbatim ambiguity cards). These appear in `Citation_Index.md` §5 as self-references. This is correct, not a bug — the index scans every doc in the folder.

## 7. Constraints honoured

- [x] No legacy `01_PHASE1_CONTEXT/` files modified (read-only)
- [x] No corpus files modified
- [x] No other Rich docs modified (only 05b, Citation_Index, this report)
- [x] No git commits (orchestrator will commit)
- [x] Inline Python used (written to /tmp/, executed, not committed)
- [x] Verbatim corpus phrasing preserved in 05b §3 (R1/R2/R3 readings, analysis_text, ambiguous phrases)
- [x] Status flipped PLACEHOLDER → CORPUS_ENRICHED on both target files

## 8. Sprint 3 readiness (Round 2 partial)

**PARTIAL_READY**:
- [x] 05b Ambiguity Register CORPUS_ENRICHED (417 cards catalogued, top 20 documented with verbatim phrasing)
- [x] Citation Index CORPUS_ENRICHED (18 unique refs mapped, 3 coverage gaps identified)
- [ ] All ambiguities resolved — deferred to Sprint 3 (human review required per §4 priority)
- [ ] Spot-check audit on 10% of citations — deferred to Sprint 3 (human verification)
- [ ] CRA Annex I/VII corpus augmentation — out-of-scope for Sprint 2; recommend corpus-side fix

**Status flip summary:**
- 05b_Ambiguity_Register.md: PLACEHOLDER → CORPUS_ENRICHED ✓
- Citation_Index.md: PLACEHOLDER → CORPUS_ENRICHED ✓
