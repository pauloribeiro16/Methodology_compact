# Fase de Especificação 2 Enrichment Report (Existing Docs)

> **Agent:** EXECUTOR (sub-agent)
> **Date:** 2026-08-06
> **Branch:** `feature/aegis-p1-case01-rich`
> **Scope:** Enrich 4 existing Phase 1 Rich docs (04a, 04b, 04c, 04d) from the corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`.
> **Companion:** This report sits alongside `SPRINT2_ENRICHMENT_REPORT_NEW.md` (Round 2 enrichment of `05b_Ambiguity_Register.md` + `Citation_Index.md`). Together they complete Fase de Especificação 2 enrichment of all six Rich Phase 1 docs that touch the corpus.

---

## 1. Summary

| Doc | Before (lines) | After (lines) | Δ | Status flip | Tables extended | Fields added |
|---|---:|---:|---:|---|---:|---:|
| `04a_Architecture_DataInventory.md` | 185 | 210 | **+25** | RECONCILED → CORPUS_ENRICHED | 1 (Compliance Mapping, 37 rows) | 2 new columns × 37 rows = **74 cells** |
| `04b_Security_Posture.md` | 242 | 298 | **+56** | RECONCILED → CORPUS_ENRICHED | 0 (no table changes) | 2 new fields × 10 macro-domains = **20 fields** |
| `04c_ThirdParty_Landscape.md` | 198 | 285 | **+87** | RECONCILED → CORPUS_ENRICHED | 1 (Compliance Mapping, 4 rows) | 1 new column × 4 rows = **4 cells** + 2 verbatim quote blocks (GDPR Art. 28 + CRA Art. 7 + CRA Art. 13(5)/(6)) |
| `04d_Org_Roles_RACI.md` | 349 | 421 | **+72** | RECONCILED → CORPUS_ENRICHED | 11 (RACI §4.1–§4.10 + Compliance Mapping §6) | 1 col × 30 RACI rows + 1 col × 7 mapping rows = **37 cells** |
| **TOTAL** | **974** | **1,214** | **+240** | **4 flipped** | **13 tables** | **135 cells/fields + 3 verbatim quote blocks** |

**Total corpus JSON lookups performed:** ~92 distinct reads (37 per-sub-domain manifests for NIST anchors in 04a; 10 JSON sidecars for fit_criterion in 04b; 4 D-06.x manifests for paths in 04c; 38 per-sub-domain manifests for req_id + manifest paths in 04d — 37 active + 1 D-08.3 inactive path; 3 verbatim quote extractions from `_by_regulation/` and `_archive_unmatched/` in 04c).

**`active_subdomains: 37` verified** in frontmatter of all 4 docs (Fase de Especificação 1 I-02 reconciliation preserved; D-08.3 inactive).

---

## 2. Per-Doc Change List

### 2.1 `04a_Architecture_DataInventory.md`

**Section 3 (Compliance Mapping)** — table header expanded from 6 columns to 8; all 37 rows extended with two new cells:

- **Corpus Manifest Path**: path to per-sub-domain `D-XX.Y.manifest.json` under `PREPROCESSING_by_domain/domains/`.
- **NIST CSF Anchors**: union of `applicable_nist_controls_by_regulation.GDPR[]` + `applicable_nist_controls_by_regulation.CRA[]` from each manifest.

**New §4 Corpus Provenance** (renumbered §4 Gate → §5 Gate):

- Documents the `jq` extraction pattern (`applicable_nist_controls_by_regulation.GDPR[]?` + `.CRA[]?`).
- Notes the 37 active sub-domain scope (D-08.3 excluded).
- Flags the corpus-annotation carry-through in some entries (e.g., `PR.DS-12 (+ PR.DS-02 for the second limb)`) preserved verbatim.

**Frontmatter:** `status: RECONCILED → CORPUS_ENRICHED`; `author` updated to indicate Fase de Especificação 2 corpus enrichment; `related_documents` extended with two new corpus paths (D-01.1 and D-09.4 manifests as representative).

**Reconciliation note (top of file):** new Fase de Especificação 2 enrichment bullet added below Fase de Especificação 1 reconciliation note.

### 2.2 `04b_Security_Posture.md`

**Section 2 (Per-Macro-Domain Assessment)** — every one of the 10 macro-domain sections now carries two new fields after **Target posture** + **Gap**:

- **Target fit_criterion** (verbatim from corpus `D-XX.Y.json` → `requirements.high_level.yaml.fit_criterion`, truncated to ~100 chars + `...`)
- **Verification Method** (from corpus `requirements.high_level.yaml.verification_method`, uniformly `TEST` at high-level aggregation)

**Representative sub-domain selection** (one per macro-domain): D-01.1, D-02.1, D-03.2, D-04.3, D-05.2, D-06.1, D-07.3, D-08.1, D-09.4, D-10.2. Selection rationale documented in §7 Corpus Provenance.

**New §7 Corpus Provenance** (after §6 Gate; §6 Gate entries extended with 2 new PASS rows):

- Documents the `requirements.high_level.yaml.fit_criterion` extraction path.
- Provides the 10-row representative sub-domain selection table with rationale.
- Notes that all 10 fit_criteria are multi-reg aggregated, not per-reg; per-reg decomposition available in `D-XX.Y.json` `requirements.sub_requirements[]`.

**Frontmatter:** status flip + author update.

**Reconciliation note (top of file):** new Fase de Especificação 2 enrichment bullet added.

### 2.3 `04c_ThirdParty_Landscape.md`

**Section 4 (Subprocessors — Art. 28 GDPR)** — new subsection §4.1 added with verbatim GDPR Art. 28 text (Art. 28(1)+(2)+(3)(a)–(h)) extracted from corpus ambiguity file `04_GDPR_Ch4_ControllerProcessor.md:200–223`. Mapping paragraph connects each Art. 28 sub-clause to the subprocessor rows below.

**Section 5 (Supply Chain Risk Assessment)** — two new subsections added:

- **§5.1 CRA Art. 7** — verbatim classification gate (Art. 7(1)–(4)) extracted from `_archive_unmatched/CRA/02_CRA_Art6-8_Classification.md:41–53`. Includes a flagged note (per AEGIS P0 — Reasoned Disagreement) that Art. 7 is a classification gate, not the substantive supply-chain duty.
- **§5.2 CRA Art. 13(5)/(6)** — substantive due-diligence verbatim text from `_by_regulation/CRA/Ambiguity/03_CRA_Art13_Manufacturers.md:23–25`. Justifies dual-quote approach in §10 Corpus Provenance.

**Section 7 (Compliance Mapping)** — table header expanded from 4 columns to 5; all 4 D-06.x rows extended with `Corpus Manifest Path` column.

**New §10 Corpus Provenance** (after §9 Gate; §9 Gate entries extended with 3 new PASS rows):

- 3-row table mapping each verbatim quote to corpus file + line range + anchor.
- Discussion of why both Art. 7 + Art. 13(5)/(6) were included (P0 disagreement with the brief's implicit assumption).
- Total corpus lookups for this section: 4 (manifest-paths only for §7 table).

**Frontmatter:** status flip + author update.

**Reconciliation note (top of file):** new Fase de Especificação 2 enrichment bullet added.

### 2.4 `04d_Org_Roles_RACI.md`

**Section 4 (RACI Matrix)** — all 10 RACI tables (§4.1–§4.10) extended with `Corpus Reg Req` column. 30 RACI rows total enriched, each row mapped to the relevant sub-domain's GDPR + CRA req_ids from `sub_requirements_by_regulation.{GDPR,CRA}[]`.

**§4.8 (D-08.3 inactive)** — best-practice placeholder row also extended with `Corpus Reg Req` column (showing `INACTIVE`).

**Section 6 (Compliance Mapping)** — table header expanded from 4 columns to 5; all 7 rows (D-08.1, D-08.2, D-08.3 INACTIVE, D-09.1, D-09.2, D-09.3, D-09.4) extended with `Corpus Manifest Path` column.

**New §9 Corpus Provenance** (after §8 Gate; §8 Gate entries extended with 3 new PASS rows):

- Documents the `req_id` extraction pattern (`sub_requirements_by_regulation.GDPR[]?.req_id?` + `.CRA[]?.req_id?`).
- Provides a 30-row activity → sub-domain mapping table with rationale for each.
- Coverage statistics: 30 RACI rows enriched, 7 mapping rows enriched, 37 req_id lookups + 38 manifest-path lookups (37 active + D-08.3 inactive path).
- `active_subdomains: 37` verified (Fase de Especificação 1 I-02 fix preserved; Fase de Especificação 2 re-verified).

**Frontmatter:** status flip + author update.

**Reconciliation note (top of file):** new Fase de Especificação 2 enrichment bullet added.

---

## 3. Corpus Fields Used

### 3.1 Manifest fields (used across all 4 docs)

```jsonc
{
  "applicable_nist_controls_by_regulation": {
    "GDPR": ["PR.DS-01", ...],   // for 04a NIST CSF Anchors column
    "CRA":  ["PR.DS-01", ...]
  },
  "sub_requirements_by_regulation": {
    "GDPR": [{"req_id": "1.1.1", ...}, ...],  // for 04d Corpus Reg Req column
    "CRA":  [{"req_id": "1.1.3", ...}, ...]
  }
}
```

**Per-sub-domain manifest path pattern** (verified for all 37 active + 1 inactive):

```
00_METHODOLOGY/PREPROCESSING_by_domain/domains/<D-XX_Domain>/D-XX.Y/D-XX.Y.manifest.json
```

Example: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/D-06.1.manifest.json`

### 3.2 JSON sidecar fields (used in 04b)

```jsonc
{
  "requirements": {
    "high_level": {
      "yaml": {
        "fit_criterion": "AES-256 (or stronger) symmetric encryption...",  // for 04b Target fit_criterion
        "verification_method": "TEST"                                       // for 04b Verification Method
      }
    }
  }
}
```

**Per-sub-domain sidecar path pattern:**

```
00_METHODOLOGY/PREPROCESSING_by_domain/domains/<D-XX_Domain>/D-XX.Y/D-XX.Y.json
```

### 3.3 Verbatim text sources (used in 04c)

| Article | Corpus path | Lines | Anchor |
|---|---|---|---|
| GDPR Art. 28 | `00_METHODOLOGY/PREPROCESSING_by_domain/_by_regulation/GDPR/Ambiguity/04_GDPR_Ch4_ControllerProcessor.md` | 200–223 | Art. 28(1) + (2) + (3)(a)–(h) |
| CRA Art. 7 | `00_METHODOLOGY/PREPROCESSING_by_domain/_archive_unmatched/CRA/02_CRA_Art6-8_Classification.md` | 41–53 | Art. 7(1)–(4) classification gate |
| CRA Art. 13(5)/(6) | `00_METHODOLOGY/PREPROCESSING_by_domain/_by_regulation/CRA/Ambiguity/03_CRA_Art13_Manufacturers.md` | 23–25 | Art. 13(5) due diligence + Art. 13(6) component vuln |

Note: The verbatim text lives in two distinct corpus locations (`_by_regulation/<REG>/Ambiguity/` and `_archive_unmatched/CRA/`), not in the per-sub-domain `articles/` folders. The per-sub-domain `articles/` folder contains per-article Security Objectives + Security Rules (Berry-paraphrased SR-id form), not the OJ verbatim text.

---

## 4. Issues Encountered

### 4.1 P0 disagreement: CRA Art. 7 vs Art. 13 for supply chain

**Issue:** The Executor brief instructed adding "verbatim CRA Art. 7 reference" to Section 4 (Supply Chain Risk) of `04c`.

**Disagreement:** CRA Art. 7 is the **classification gate** (Annex III "important products with digital elements") — it does NOT contain substantive supply-chain obligations. The actual substantive supply-chain due-diligence duty lives in **CRA Art. 13(5)/(6)** (manufacturer exercises due diligence when integrating third-party components, including FOSS).

**Resolution (per AEGIS P0 — Reasoned Disagreement Over Deference):** Both verbatim quotes included in `04c §5.1 + §5.2`. Art. 7 quote preserved verbatim per the brief; Art. 13(5)/(6) added with explicit justification because (a) it is the actual substantive article for the supply-chain duty, (b) the corpus's own SO-CRA-037 (referenced from D-06.1 manifest) cites Art. 13(5)/(6) not Art. 7, and (c) the human reader expecting "supply chain → Art. 7" would otherwise miss the operative article. The §10 Corpus Provenance section explicitly documents this dual-quote approach so the reader can audit the choice.

This is the exact P0 pattern: surface the disagreement with reasoning, then comply with the user's intent in a defensible form.

### 4.2 Some NIST CSF entries carry corpus annotations

**Issue:** Some `applicable_nist_controls_by_regulation` entries in the corpus carry parenthetical annotations (e.g., `PR.DS-12 (+ PR.DS-02 for the second limb)`, `PR.PS-02; ID.RA-05`, `PR.IP-07 (primary)`).

**Resolution:** Annotations preserved verbatim in the 04a NIST CSF Anchors column. They reflect corpus-internal notes about which control is primary or about multi-limb coverage; falsifying them would lose information. Documented in §4 Corpus Provenance.

### 4.3 `verification_method` is uniformly `TEST` at high level

**Issue:** All 10 macro-domain `requirements.high_level.yaml.verification_method` values returned `TEST` in the corpus.

**Resolution:** Documented in 04b §7 Corpus Provenance that the high-level fit_criterion is the multi-reg aggregation point; per-reg decomposition (which can return `INSPECTION`, `DEMONSTRATION`, etc.) lives in `requirements.sub_requirements[]`. For TinyTask's posture assessment purpose, the high-level `TEST` is sufficient because all 10 macro-domains require test evidence (config audit, key-custody review, etc.) as the verification floor. If per-reg variation becomes needed, Phase 3 consumers should pull from `sub_requirements[]`.

### 4.4 `active_subdomains: 37` was already fixed in Fase de Especificação 1

**Issue (resolved):** Per the brief, verify `active_subdomains: 37` in frontmatter.

**Verification:** Confirmed `active_subdomains: 37` in frontmatter of all 4 docs (lines 21, 21, 22, 24 respectively). The Fase de Especificação 1 I-02 fix (commented in 04d line 24) is preserved. D-08.3 inactive path retained in 04d Section 6 mapping table for traceability (the path is real, just inactive).

### 4.5 No Fase de Especificação 3 blockers identified

All 4 docs are CORPUS_ENRICHED, internally consistent (active_subdomains: 37 across all 4), and reference the corpus paths rather than the legacy `PREPROCESSING/SubDomains/` paths. Legacy paths preserved in column 6 of 04a for backwards compatibility (legacy 04b / 04c / 04d also retain legacy paths in their inline references).

---

## 5. Fase de Especificação 3 Readiness

### 5.1 What Fase de Especificação 2 produced

- **6 docs enriched** (this report covers 4 existing; companion `SPRINT2_ENRICHMENT_REPORT_NEW.md` covers 2 new — `05b_Ambiguity_Register.md` and `Citation_Index.md`).
- **13 tables extended** with corpus-derived columns.
- **135 cells / fields added** across the 4 existing docs (74 + 20 + 4 + 37).
- **3 verbatim Article quote blocks** added to 04c (GDPR Art. 28 + CRA Art. 7 + CRA Art. 13(5)/(6)).
- **4 status flips** to `CORPUS_ENRICHED`.
- **0 corpus files modified** (read-only access throughout).
- **0 legacy `01_PHASE1_CONTEXT/` files modified**.
- **0 git commits created** (orchestrator owns commit workflow).
- **0 emojis added** (Language Policy + AGENTS.md compliance).

### 5.2 What Fase de Especificação 3 should validate

1. **Lint pass** with `01_IMPLEMENTATION_TOOLS/lints/phase1/`:
   - `lint_regulatory_mapping.py` — confirm NIST anchors + req_id columns parse cleanly.
   - `lint_template_compliance.py` — confirm new columns don't break template compliance.
   - `lint_cross_document_consistency.py` — confirm `active_subdomains: 37` consistency across all Phase 1 docs (already verified in this report).
   - `lint_regulatory_references.py` — confirm new corpus paths + verbatim article references parse cleanly.
2. **Phase 1 gate re-check** — confirm gate criteria still PASS after enrichment (no regressions).
3. **Sample-read audit** — Validator should spot-check at least 3 randomly-selected rows from 04a §3, 04d §4.x to confirm NIST anchors + req_id values match the corpus.
4. **Verbatim quote audit** — Validator should confirm the GDPR Art. 28 + CRA Art. 7 + CRA Art. 13(5)/(6) quotes in 04c match the corpus source byte-for-byte (or marked-up-by-emphasis-byte-for-byte).

### 5.3 Outstanding items not in Fase de Especificação 2 scope

- **04a / 04b / 04c legacy `SubDomains/` path references** — preserved alongside new `PREPROCESSING_by_domain/` paths. Phase 3 migration can deprecate the legacy paths once `PREPROCESSING/SubDomains/` directory itself is removed from the corpus (separate corpus task, not Executor scope here).
- **NIST control annotation deduplication** — some corpus entries have duplicates or parenthetical notes (e.g., `PR.PS-02; ID.RA-05`, `PR.PS-01, PR.PS-01`). Preserved as-is for fidelity. Future corpus-cleanup sprint can normalise.
- **Verbatim Art. 28 quote truncation** — Art. 28(3)(a) parenthetical `(...)` is preserved literally because the corpus file itself uses this ellipsis notation (the sub-clauses (a)–(h) are not all in one paragraph in the OJ text). Validator should confirm this is acceptable.

### 5.4 Fase de Especificação 2 sign-off

- Executor (this agent): **READY for Fase de Especificação 3 validator review.**
- All deliverables in `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/` are CORPUS_ENRICHED and internally consistent.
- No commits created; orchestrator should commit via `./scripts/finish-feature.sh` after Validator passes.

---

## See also

- **Fase de Especificação 2 companion:** `SPRINT2_ENRICHMENT_REPORT_NEW.md` (Round 2 enrichment of `05b_Ambiguity_Register.md` + `Citation_Index.md`).
- **Fase de Especificação 1 report:** `SPRINT1_REPORT.md` (Fase de Especificação 1 reconciliation — `active_subdomains: 37` fix + status flips to RECONCILED).
- **Corpus augmentation report:** `CORPUS_AUGMENTATION_REPORT.md` (38/38 sub-domain files + 48 manifests + 38 sidecars + 623 articles).
- **Lint reports:** `LINT_REPORT_BEFORE.md`, `LINT_REPORT_AFTER_RECONCILE.md`.