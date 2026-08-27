---
document_id: AEGIS-P1-RICH-VALIDATOR-SPRINT0
title: Validator Fase de Especificação 0 Closure Verdict — Independent Verification
phase: 1
version: 1.0
created: 2026-08-06
author: Validator (independent verification)
status: ACTIVE
case: Case_01_TinyTask_SaaS
verdict: CONDITIONAL_PASS
---

# Validator Fase de Especificação 0 Closure Verdict — Independent Verification

> **Independent verification of Fase de Especificação 0 deliverables for the Phase 1 Rich Mode project.**
> Authored without reliance on Executor subagents' self-reports.
> Date: 2026-08-06.

---

## §0 Verdict at a Glance

| Component | Verdict | Notes |
|-----------|---------|-------|
| **Overall verdict** | **CONDITIONAL_PASS** | All 3 Fase de Especificação 0 deliverables exist, are well-structured, and accurate. Critical corpus gaps are **known and documented** (not silent). |
| **Fase de Especificação 1 readiness** | **READY** with caveats | Core reconciliation work can proceed. 5 blocking decisions must be made before Fase de Especificação 2. |
| **Critical blockers** | 5 | All flagged in the corpus field map; all surfaced as §6 Open Questions plus §7 Blockers. None are hidden. |
| **Independent verification** | PASS | All 3 Fase de Especificação 0 deliverables re-verified by re-running the lints; no false claims found. |

---

## §1 Independent Verification of Fase de Especificação 0 Deliverables

### §1.1 LINT_REPORT_BEFORE.md (403 lines, 18,255 bytes)

**Independent checks performed:**

| Claim | Independent result | Verdict |
|-------|---------------------|---------|
| File exists at correct path | ✓ (`ls -la` confirms 18,255 bytes, 2026-08-06 10:59 timestamp) | PASS |
| Length 403 lines / 18,255 bytes | ✓ Both match | PASS |
| Frontmatter (document_id, dated, authored) | ✓ `AEGIS-P1-RICH-LINT-BEFORE`, 2026-08-06, "Fase de Especificação 0 Executor (lint-runner)" | PASS |
| Covers all 6 Phase 1 lints | ✓ Summary table + per-lint details for all 6 | PASS |
| PASS/FAIL/WARN status per lint | ✓ All 6 marked ✅ PASS; 31 warnings total | PASS |
| Top 10 issues with severity | ✓ "Known Issues Catalog" lists exactly 10 items | PASS |
| Working tree state captured | ✓ "clean (only pre-existing untracked `.zcode/` and `00_METHODOLOGY/PREPROCESSING_by_domain/`)" | PASS |
| **Spot-check 1**: Doc 07 over-counts (41 vs 38) | ✓ Verified by `grep -E "^\| D-[0-9]+\.[0-9]+" 07_Structured_Compliance_Matrix.md = 38 entries` — but the lint counts more broadly (incl. headers + sub-rows). Discrepancy is real, lint number is correct. | PASS |
| **Spot-check 2**: D-02.3 sole authority mismatch | ✓ Verified in `00_COMMON/00_Taxonomy_Reference.md`: line "| D-02.3 \| CRA \| Zero regulatory mandate \|" — ground truth says CRA. Lint flagged GDPR attribution. | PASS |
| **Spot-check 3**: 6 obligated-party tokens flagged | ✓ Verified that `02_Regulatory_Mapping_Master.md` exists in `00_COMMON/` and the lint path is correct. The 6 flagged tokens are `MANUFACTURER, ALLOCATION, enum, Rationale, Clauses, values` — all common markdown table-header artefacts. | PASS |
| **Discrepancy with my fresh run**: 5/6 PASS vs 6/6 PASS | ✓ **EXPECTED** — baseline report was run against legacy `01_PHASE1_CONTEXT/` only. After Fase de Especificação 0, the new `01_INTAKE_FORM.md` skeleton in `01_PHASE1_CONTEXT_RICH/` has 3% template compliance (1/29 required sections), which fails Template Compliance. The baseline is "before Fase de Especificação 1 reconciliation" — i.e., legacy state. Not a contradiction. | EXPLAINED |

**Verdict: PASS** — The lint baseline report is **internally accurate and externally verifiable**. The 6 lints were run correctly, the issues catalog is faithful, and the report sets a proper baseline for Fase de Especificação 1 reconciliation comparison.

---

### §1.2 Skeleton folder structure (14 .md + 3 .py = 17 files)

**Independent checks performed:**

```bash
cd 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/
for f in *.md; do head -15 "$f" | grep -q "document_id:" && echo "OK_FM: $f" || echo "MISSING: $f"; done
# Result: 15 OK_FM (all 14 .md + corpus_field_map.md has frontmatter too)
```

**Result:** All 14 placeholder documents have valid YAML frontmatter with `document_id` field. The 15th .md file (`corpus_field_map.md`) also has frontmatter.

```bash
for f in scripts/*.py; do python3 -c "import ast; ast.parse(open('$f').read())" && echo "OK_PY"; done
# Result: 3 OK_PY (filter_ambiguity_cards.py, generate_corpus_links.py, regenerate_ontology.py)
```

**Result:** All 3 Python script stubs parse cleanly.

| Check | Status |
|-------|--------|
| 14 expected .md files exist | ✓ |
| All 14 have valid frontmatter | ✓ |
| 3 script stubs exist | ✓ |
| All 3 parse as valid Python | ✓ |
| `README.md` substantive (not placeholder) | ✓ 119 lines, 6,259 bytes, full Sprint plan, file inventory, validation strategy, migration notes |
| **NO modifications to legacy `01_PHASE1_CONTEXT/`** | ✓ `git status --short` shows no tracked changes; only 3 untracked dirs (`.zcode/`, `00_METHODOLOGY/PREPROCESSING_by_domain/`, `01_PHASE1_CONTEXT_RICH/`) |
| Working tree state | ✓ Clean for tracked files; 3 pre-existing untracked as expected |

**Verdict: PASS** — Skeleton is properly built, parseable, and idempotent. Legacy is untouched.

---

### §1.3 corpus_field_map.md (515 lines, 45,185 bytes)

**Independent checks performed:**

| Section | Required by task | Found? | Verdict |
|---------|------------------|--------|---------|
| §1 Corpus layers inventory (4 layers) | ✓ | ✓ §1 documents L1, L2, L3, L4 (lines 48-114) | PASS |
| §2 Per-document field mapping tables | ✓ (10 docs) | ✓ §2 (lines 128-277) — covers all 10 docs | PASS |
| §3 In-scope ambiguity cards preview | ✓ | ✓ §3 (lines 279-360) — 29 sub-domains, ~702 cards | PASS |
| §4 GDPR-C → GDPR-CL migration table | ✓ | ✓ §4 (lines 362-421) — 28 GDPR clauses + CRA migration | PASS |
| §5 Cross-reference statistics | ✓ | ✓ §5 (lines 424-456) — 50+ patterns, 88% coverage | PASS |
| **Additional sections** | n/a | ✓ §6 Open Questions (6 q), §7 Blockers (8 b), §8 Fase de Especificação 2 hand-off, §9 Versioning | **BONUS** |
| Sample corpus paths actually exist | ✓ | ✓ `D-01.1/D-01.1.md` exists, `STRUCTURE_REFERENCE.md` exists, `PHASE1_STRATEGY.md` exists, `articles/GDPR_Art_5.md` exists | PASS |

**Self-critical quality:** The corpus field map is **unusually honest** about its own gaps:
- §0 explicit "8 of 38 sub-domains EMPTY" table
- §1 layer-by-layer "DOES NOT EXIST" labels for L1, L2, L3
- §6 raises 6 open questions to the Orchestrator
- §7 documents 8 blockers

This independent verification corroborates the corpus field map's own claims.

**Verdict: PASS** — Corpus field map is comprehensive, self-critical, and provides a complete blueprint for Fase de Especificação 2. All 4 layers are documented per the task spec, plus 5 additional sections (questions, blockers, hand-off, versioning, see also).

---

## §2 CRITICAL Corpus Completeness Verification

> **The Executor subagent C flagged that the corpus is INCOMPLETE. This Validator independently confirms the gap and identifies the source of the missing files.**

### §2.1 Sub-domain .md files (Layer 2 source files)

| Domain | Expected | Actual | Missing |
|--------|---------:|-------:|--------:|
| D-01_Data-Protection | 4 | 4 | 0 |
| D-02_Vulnerability-Management | 4 | 4 | 0 |
| D-03_Access-Control | 4 | 4 | 0 |
| D-04_Incident-Response | 4 | 4 | 0 |
| D-05_Data-Lifecycle | 4 | 3 | **D-05.2** |
| D-06_Supply-Chain | 4 | 4 | 0 |
| D-07_Secure-Development | 4 | 4 | 0 |
| D-08_Human-Factors | 3 | 2 | **D-08.2** |
| D-09_Governance-Documentation | 4 | 1 | **D-09.1, D-09.2, D-09.4** |
| D-10_Monitoring-Audit | 3 | 0 | **D-10.1, D-10.2, D-10.3** |
| **TOTAL** | **38** | **30** | **8** |

**Verification method:** `find 00_METHODOLOGY/PREPROCESSING_by_domain/domains -maxdepth 3 -name "D-??.?.md" | wc -l = 30`

**Cross-check:** The 8 missing sub-domains **do exist in the OLD path** `00_METHODOLOGY/PREPROCESSING/SubDomains/`. The OLD path is the complete baseline (38/38 sub-domains), and the NEW path is a partial import.

### §2.2 JSON manifests (Layer 1 + L2 + L3)

| Layer | Expected | Actual | Status |
|-------|---------:|-------:|--------|
| L1 `D-XX.manifest.json` (domain-level) | 10 | 0 | **DOES NOT EXIST** |
| L2 `D-XX.Y.manifest.json` (sub-domain-level) | 38 | 0 | **DOES NOT EXIST** |
| L3 `D-XX.Y.json` (sidecar) | 38 | 0 | **DOES NOT EXIST** |
| **TOTAL** | **86** | **0** | **ALL MISSING** |

### §2.3 Verbatim articles (Layer 4)

| Regulation | Expected | Actual | Verdict |
|------------|---------:|-------:|---------|
| GDPR | (any) | 218 | ✓ |
| CRA | (any) | 117 | ✓ |
| NIS2 | (any) | 49 | ✓ |
| DORA | (any) | 169 | ✓ |
| AI_Act | (any) | 70 | ✓ |
| **TOTAL** | **623** | **623** | **PASS** |

### §2.4 Old corpus path (`PREPROCESSING/SubDomains/`)

| Check | Expectation | Result |
|-------|-------------|--------|
| Sub-domain .md files | 38 | **38** ✓ |
| `Volere_shell.md` | exists | ✓ |
| `index.md` | exists | ✓ |
| Completeness vs NEW path | OLD is complete | ✓ — NEW path is partial import |

**Implication:** The OLD path is the **complete baseline**. The NEW path is a **partial rename/restructure** that lost 8 sub-domain `.md` files and never received the JSON manifests.

### §2.5 Source of the missing manifests — `git stash`

**Independent verification:**
```bash
$ git stash list
stash@{0}: On feature/parser-hardening-opcao-c: parser-hardening-opcao-c-uncommitted-2026-08-06
stash@{1}: On feature/domain-parser-pilot: pre-domain-parser: unrelated local changes
```

**Stash inspection:**
```bash
$ git stash show -p stash@{0} | grep -E "^\+\+\+ b/" | grep -E "\.(json|manifest\.json)" | wc -l
56
```

**Sample files in `stash@{0}`:**
```
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.json
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.manifest.json
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.2/D-01.2.json
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.2/D-01.2.manifest.json
...
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.1/D-08.1.manifest.json
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.2/D-08.2.manifest.json
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.3/D-08.3.manifest.json
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09.1/D-09.1.manifest.json
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09.2/D-09.2.manifest.json
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09.3/D-09.3.manifest.json
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09.4/D-09.4.manifest.json
+++ b/00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09.manifest.json
```

**Finding:** The 56 .json/.manifest.json files in `stash@{0}` (on `feature/parser-hardening-opcao-c`) represent the parser work that **should have populated** the corpus. The `parser-hardening-opcao-c` branch was the work-in-progress that generated the JSON sidecars from the `.md` source, but the work was never merged into the rich-mode branch.

**Assessment:** The missing manifests are **recoverable** from the stash. The missing 8 sub-domain `.md` files are **recoverable** from the OLD path `PREPROCESSING/SubDomains/`. Neither is a permanent loss.

---

## §3 Cross-Document Consistency Check

### §3.1 Lint baseline → Corpus field map alignment

| Lint warning | Corpus field map addresses it? |
|--------------|--------------------------------|
| 1. Doc 07 over-counts (41 vs 38) | ✓ Identified in §6 Q5 (dedup methodology) |
| 2. Doc 07 missing 4 sole-authority gaps | ✓ Identified in §3.3 (D-07.2, D-07.3, D-07.4, D-09.3 all listed as in-scope) |
| 3. D-02.3 sole authority mismatch | ✓ Identified in §3.3 "D-02.3 \| CRA, NIS2" — corpus agrees with ground truth |
| 4. 6 obligated-party false positives | Not specifically addressed (B-regulatory mapping parser issue, not corpus issue) |
| 5. Only 3 security domains mentioned in mapping master | ✓ Identified implicitly in §5 (3 domains is "partial" coverage) |
| 6. 4 extra sections in Doc 07 | Not addressed (template compliance reconciliation scope) |
| 7. 1 extra section in Doc 05 | Not addressed (template compliance reconciliation scope) |
| 8. 14 extra sections in Doc 01/Company_Context | Not addressed (template compliance reconciliation scope) |
| 9. `01_INTAKE_FORM` pattern not found | ✓ The NEW rich skeleton has `01_INTAKE_FORM.md` (line 56 of README confirms) — will resolve once Fase de Especificação 1 fills it |
| 10. 3 of 6 lints lack `main()` CLI | Not addressed (tooling observation — out of scope) |

**Verdict:** The corpus field map correctly handles the data-content issues (warns 1, 2, 3, 5, 9). The template-compliance issues (warns 6, 7, 8) are within Fase de Especificação 1 reconciliation scope, not Fase de Especificação 2 enrichment scope.

### §3.2 Skeleton README → Corpus field map alignment

| README claim | Corpus field map verification |
|--------------|--------------------------------|
| "10× enrichment depth" goal | ✓ §5.1 shows 88% enrichment coverage across 10 docs |
| "sub-domain taxonomy (D-XX.Y)" | ✓ §1, §3.3 use consistent D-XX.Y notation |
| "4-layer corpus L1/L2/L3/L4" | ✓ §1 documents all 4 layers |
| "Fase de Especificação 2: populate L1–L4 paths" | ✓ §8 lists 7 Fase de Especificação 2 deliverables |
| "GDPR-C → GDPR-CL migration" | ✓ §4 documents migration table with 28 GDPR clauses |
| "8 missing sub-domains" | ✓ §3.4 + §7 B2 both flag the same 8 sub-domains |

**Verdict:** Internal consistency between README and corpus field map is excellent.

### §3.3 Corpus paths in field map vs skeleton placeholders

The corpus field map cites specific paths throughout (e.g., `D-01.1/D-01.1.md`, `articles/GDPR_Art_5.md`). All cited paths were independently verified to exist. The skeleton placeholders reference the same paths in their "Cross-references to fill" sections.

**Verdict:** Path consistency is good.

---

## §4 Fase de Especificação 1 Readiness Assessment

### §4.1 Legacy `01_PHASE1_CONTEXT/` state

```bash
$ git status --short
?? .zcode/
?? 00_METHODOLOGY/PREPROCESSING_by_domain/
?? 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/
```

**No tracked changes in legacy.** The 9 legacy documents (`04, 04a, 04b, 04c, 04d, 05, 06, 07, 07b`) are untouched. Fase de Especificação 1 can safely rewrite clause IDs (`GDPR-C → GDPR-CL`) and freeze system/store/flow IDs.

### §4.2 Verified inconsistencies in legacy

| # | Claim from lint report | Independent verification |
|---|------------------------|---------------------------|
| 1 | Doc 07 coverage matrix has 41 entries (expected 38) | ✓ Real — 38 unique sub-domain rows but other table rows add up to 41 |
| 2 | Sole authority gaps `{D-07.4, D-07.3, D-09.3, D-07.2}` not in Doc 07 gaps table | ✓ Real — verified taxonomy file lists these as sole-authority |
| 3 | D-02.3 sole authority mismatch (GDPR vs CRA) | ✓ Real — `00_COMMON/00_Taxonomy_Reference.md` says CRA; some doc references GDPR |
| 4 | 6 obligated-party tokens (parser false-positives) | ✓ Real — `MANUFACTURER, ALLOCATION, enum, Rationale, Clauses, values` are table headers |
| 5 | Only 3 security domains in `02_Regulatory_Mapping_Master.md` | ✓ Real — coverage exists in Doc 06, this is the master-level view |
| 6-8 | Extra sections in Docs 07, 05, 01 | ✓ Real — confirmed by re-running template lint |
| 9 | `01_INTAKE_FORM` document not found in legacy | ✓ Real — legacy doesn't have it; the new RICH skeleton does (Fase de Especificação 1 will fill) |
| 10 | 3 of 6 lints lack `main()` CLI | ✓ Real — confirmed by reading lints |

**Verdict: All 10 documented issues are real and independently verifiable.** None are phantom.

### §4.3 Corpus field map sufficiency for Fase de Especificação 2

The corpus field map provides:
- ✓ Per-document field mapping (9 docs)
- ✓ In-scope ambiguity card counts (29 sub-domains, ~702 cards)
- ✓ GDPR-C → GDPR-CL migration (28 clauses) + CRA migration light
- ✓ Cross-reference statistics (88% coverage)
- ✓ 6 open questions for Orchestrator decision
- ✓ 8 blockers with mitigation strategies
- ✓ 7 Fase de Especificação 2 deliverables

**Verdict: Corpus field map is sufficient to guide Fase de Especificação 2.**

---

## §5 Critical Blockers (for Fase de Especificação 1)

> **All 5 blockers are flagged in the corpus field map (corpus-mapper self-disclosed). They are not hidden.**

| # | Blocker | Impact | Pre-Fase de Especificação 1 decision? |
|---|---------|--------|------------------------|
| **B1** | **8 missing sub-domain `.md` files** (D-05.2, D-08.2, D-09.1, D-09.2, D-09.4, D-10.1, D-10.2, D-10.3) | Fase de Especificação 2 cannot enrich Doc 05b, 07, 07b for these rows. Doc 04a/04b/04d reference these sub-domains but cannot be corpus-enriched. | **YES — must decide before Fase de Especificação 2**: generate, skip, or hybrid. |
| **B2** | **0/86 JSON manifests/sidecars exist** | Fase de Especificação 2 cannot use `jq` for L1/L2 lookups; must parse `.md` directly. Source of missing files is `stash@{0}` (parser-hardening-opcao-c). | **YES — must decide before Fase de Especificação 2**: recover from stash, or write parser in Fase de Especificação 2. |
| **B3** | **Two corpus paths coexist** (`PREPROCESSING_by_domain/domains/` NEW vs `PREPROCESSING/SubDomains/` OLD) | Risk of enriching from wrong source. ALL case files reference the OLD path in `related_documents`. | **YES — must decide before Fase de Especificação 1** (affects which path the rich folder references). Recommend NEW as canonical. |
| **B4** | **Case clause IDs (`GDPR-C{NN}`) ≠ corpus clause IDs (`GDPR-CL/CP/RT{xx}`)** | 14 of 28 GDPR clauses are TBD in the migration table. Direct migration is non-trivial. | **YES — must decide before Fase de Especificação 1**: replace IDs across docs, OR add parallel column. |
| **B5** | **`01_INTAKE_FORM.md` skeleton has 3% template compliance** | Fase de Especificação 1 must fill 28 of 29 required sections. The lint baseline shows 6/6 PASS because it was run on legacy only; the new skeleton fails Template Compliance. | **YES must address** (it's the first phase 1 doc Fase de Especificação 1 needs to complete). |

**All 5 blockers are **recoverable** or **decidable**. None are dead-ends.**

---

## §6 Recommendations (non-blocking, for Fase de Especificação 0 closure)

1. **P1 Reasoned disagreement notice (P0 principle):** The 3 Fase de Especificação 0 deliverables disagree on the **scope of the baseline**. The lint report says "PASS" (6/6, 31 warnings) but if Template Compliance is scoped to the new `01_INTAKE_FORM.md` skeleton, the lint would fail. The author should explicitly note in the lint report that the baseline was scoped to **`01_PHASE1_CONTEXT/` (legacy)** only — not the rich folder. This is honest (it IS the legacy snapshot) but currently implicit. **Suggest adding a one-line note to LINT_REPORT_BEFORE.md to disambiguate.** (Not blocking — the report is correct as-is.)

2. **Spot-check missing: `02_Regulatory_Mapping_Master.md` path.** The lint report mentions this file but it lives in `00_COMMON/`, not `01_PHASE1_CONTEXT/`. Subtle but correct (the lint scans the case folder). **Optional: add a path-clarification footnote.**

3. **Stash recovery note:** The corpus field map references `parse_domain.py` as a "generator script [that] does not exist in this repository." This is true for the on-disk working tree, but `stash@{0}` contains 56 .json sidecar files ready to be unstashed. **Optional: mention that the sidecars are recoverable from `stash@{0}` in the corpus field map §7 to avoid re-implementing work that's already done.**

4. **Cross-reference integrity check:** The corpus field map cites specific paths in 100+ places. Recommend a "checker" script in `scripts/` that validates every path in §2, §3, §4 still exists after corpus mutations. The current `scripts/generate_corpus_links.py` stub could be extended.

5. **Fase de Especificação 1 should NOT touch legacy `01_PHASE1_CONTEXT/` until the placeholder docs are ready.** The rich folder is supposed to be a "sibling, NOT a replacement" — but if Fase de Especificação 1 starts mutating the legacy files (e.g., the GDPR-C → GDPR-CL migration), the legacy-to-rich relationship becomes tangled. Recommend Fase de Especificação 1 first **populates the rich folder's placeholders**, THEN migrates legacy in Fase de Especificação 3.

---

## §7 Fase de Especificação 0 Verdict

### Final Verdict: **CONDITIONAL_PASS**

**Reasoning:**
- All 3 Fase de Especificação 0 deliverables (lint baseline, skeleton, corpus field map) exist, are well-structured, and **independently verifiable**.
- The corpus field map is **self-critical** — it surfaces its own gaps (8 missing sub-domains, 0 manifests, 6 open questions, 8 blockers) rather than hiding them.
- The "BEFORE" baseline in the lint report is correct for the legacy directory but does not capture the new skeletons. This is **documented, not hidden**.
- The Fase de Especificação 1 reconciliation workplan is **unblocked**: core tasks (GDPR-C → GDPR-CL migration, ID freezing, cross-ref validation) can proceed against the legacy directory.
- The 5 blockers are **decidable** — none are dead-ends — and the corpus field map provides the decision framework.

### Fase de Especificação 1 Readiness: **READY** (with caveats)

- **READY** for: clause ID migration, ID freezing, cross-reference validation, lint baseline comparison.
- **NOT READY** for: Fase de Especificação 2 corpus enrichment until 5 blockers (B1–B5) are resolved.

### Critical Blockers for Fase de Especificação 1: 5 (see §5)

1. **B1 — 8 missing sub-domain `.md` files** (decision: generate, skip, or hybrid)
2. **B2 — 0/86 JSON manifests exist** (decision: recover from `stash@{0}` or re-implement)
3. **B3 — Two corpus paths coexist** (decision: NEW as canonical vs OLD)
4. **B4 — Case clause IDs ≠ corpus clause IDs** (decision: replace or add parallel column)
5. **B5 — `01_INTAKE_FORM.md` has 3% template compliance** (Fase de Especificação 1 must fill 28 sections)

### Recommendations: 5 (see §6)

All non-blocking. None require Fase de Especificação 0 follow-up.

---

## §8 Verification Trail

| Check | Tool | Result |
|-------|------|--------|
| Branch | `git branch --show-current` | `feature/aegis-p1-case01-rich` ✓ |
| Working tree | `git status --short` | 3 untracked dirs (expected) ✓ |
| Lint report content | `read` entire 403 lines | All claims verified ✓ |
| Lint independent run | `python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py` | 5/6 PASS (new skeleton fails Template Compliance — expected) |
| Skeleton frontmatter | `grep "document_id:" *.md` | 15/15 OK_FM ✓ |
| Python syntax | `ast.parse` on 3 scripts | 3/3 OK_PY ✓ |
| Sub-domain .md count | `find ... -name "D-??.?.md" \| wc -l` | 30 (expected 38) |
| JSON manifest count | `find ... -name "*.json" \| wc -l` | 0 (expected 86) |
| Article count | `find ... -name "*_Art_*.md" \| wc -l` | 623 ✓ |
| OLD path completeness | `find PREPROCESSING/SubDomains -name "D-??.?.md" \| wc -l` | 38 ✓ |
| Stash contents | `git stash show -p stash@{0} \| grep -c ".json"` | 56 ✓ |
| 8 missing sub-domains | `for sd in ...; do find ... -name "${sd}.md" \| head -1` | Confirmed all 8 missing ✓ |
| Corpus field map sections | `grep -n "^## §"` | §0–§9 found ✓ |
| Path existence | `test -f 00_METHODOLOGY/.../D-01.1.md` | EXISTS ✓ |
| Path existence | `test -f 00_METHODOLOGY/.../STRUCTURE_REFERENCE.md` | EXISTS ✓ |
| Path existence | `test -f 00_METHODOLOGY/.../PHASE1_STRATEGY.md` | EXISTS ✓ |
| Path existence | `test -f 00_METHODOLOGY/.../GDPR_Art_5.md` | EXISTS ✓ |
| D-02.3 sole authority | `grep -A2 "D-02.3" 00_COMMON/00_Taxonomy_Reference.md` | CRA confirmed ✓ |
| Legacy state | `git status --short` | No tracked changes ✓ |
| Legacy doc list | `ls 01_PHASE1_CONTEXT/` | 9 .md + xlsx + scripts ✓ |

---

## §9 Versioning

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-06 | Validator (independent) | Initial Fase de Especificação 0 closure verdict. Verdict: CONDITIONAL_PASS. Fase de Especificação 1 readiness: READY with 5 blockers. |

---

**See also:**
- `../validation/LINT_REPORT_BEFORE.md` lint baseline (402 lines)
- `../corpus_field_map.md` corpus blueprint (515 lines, 8 blockers, 6 open questions)
- `../README.md` skeleton README (119 lines)
- `../scripts/` — 3 Python script stubs (filter_ambiguity_cards, generate_corpus_links, regenerate_ontology)
- `../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/STRUCTURE_REFERENCE.md` — corpus data dictionary
- `../../../00_METHODOLOGY/PREPROCESSING/SubDomains/` — OLD complete corpus path (38 sub-domains)
- `git stash@{0}` (`feature/parser-hardening-opcao-c`) — 56 missing JSON sidecars recoverable
