---
document_id: AEGIS-METH-P0-AUDIT
title: "Phase 0 — Baseline Corpus Audit"
phase: 0
version: 1.0
created: 2026-08-27
updated: 2026-08-27
author: AEGIS Orchestrator
status: ACTIVE
classification: METHODOLOGY-META — not a numbered deliverable
sources:
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/PRODUCTION_FLOW.md (v1.0)
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/PARSE_DOMAIN_EXECUTION_BRIEF.md
related_documents:
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/PRODUCTION_FLOW.md
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/PARSE_DOMAIN_EXECUTION_BRIEF.md
  - ../../../00_METHODOLOGY/dependency_graph.yaml
  - ../../../00_METHODOLOGY/diagrams/fluxdiagram/phase1/phase1_rich_extension.md
---

# Phase 0 — Baseline Corpus Audit (v0)

**Version:** 1.0 — 2026-08-27
**Status:** ✅ Active
**Scope:** the frozen regulatory-baseline corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/` — read-only baseline feeding Phase 1 / 2 / 3 across all three cases.

---

## 1. Inventory

| Component | Path | Count | Per-component | Status |
|-----------|------|------:|---------------|--------|
| Domain docs | `domains/D-XX/D-XX.Y/D-XX.Y.md` | 38 | D-01..D-07 = 4 each; D-08 = 3; D-09 = 4; D-10 = 3 | DRAFT v0.1 (38/38) |
| Domain manifests | `domains/D-XX/D-XX.manifest.json` | 10 | one per domain | schema 1.0.0, generated 2026-08-04 |
| Article sidecars | `domains/D-XX/D-XX.Y/articles/*` | 623 | 66/57/47/108/38/55/38/34/120/60 | frozen copies |
| NIST AI RMF | `CONTROLS/NIST_AI_RMF/` | 72 JSONs | GOVERN 19 / MAP 18 / MEASURE 22 / MANAGE 13 | structured (control_id…source_version) |
| NIST PF | `CONTROLS/NIST_PF/` | 100 JSONs | GOVERN-P 20 / CONTROL-P 19 / PROTECT-P 30 / IDENTIFY-P 21 / COMMUNICATE-P 10 | structured |
| Overlays | `MAPPINGS/OVERLAYS/OVERLAY_*.md` | 4 | AI_Act_v2024, NIST_AI_RMF_1.0, NIST_CSF_2.0, NIST_PF_1.1 | source-of-truth paths cited |
| Index | `domains/index.md` | 1 | 20 lines, listing-only (no version/date) | n/a |
| Parser brief | `PARSE_DOMAIN_EXECUTION_BRIEF.md` | 1 | 28,341 bytes (PT-language executor brief for D-01.1 pilot) | **NOT executed in this repo** |
| Source spreadsheets | `nist_ai_rmf_playbook.xlsx`, `NIST-Privacy-Framework-V1.0-Core.xlsx` | 2 | binary | source for CONTROLS/ JSONs |

**Provenance in git:** the entire corpus was added by single snapshot commit `231ed3c` (2026-08-26). No subsequent edits to any file under `domains/`, `CONTROLS/`, `MAPPINGS/`.

**Protected by guard:** the workspace hook `guard-protected-files.sh` denies `Write|Edit` on `00_METHODOLOGY/PREPROCESSING_by_domain/domains/**` and on the KG build artefacts. This v0 audit and the companion `PRODUCTION_FLOW.md` are *outside* that protected scope.

---

## 2. Classification

| Class | Count | What it is |
|-------|------:|------------|
| **BASELINE-FROZEN** | 38 + 10 + 623 | the `domains/` corpus (D-XX.Y.md + .manifest.json + articles/); read-only by design |
| **CONTROLS-DATA** | 172 | `CONTROLS/{NIST_AI_RMF,NIST_PF}/*.json`; structured per-control data |
| **OVERLAY-META** | 4 | `MAPPINGS/OVERLAYS/OVERLAY_*.md`; cross-framework mappings with source citations |
| **TOOLING-MISSING** | 2 | (a) `reorg_by_domain_md.py` — credited as the generator inside every D-XX.Y.md but absent from the repo; (b) `parse_domain.py` + `filter.py` — declared outputs of `PARSE_DOMAIN_EXECUTION_BRIEF.md`, also absent |
| **SOURCES-MISSING** | ≥2 | `Taxonomia.txt`, `Regulatory_Complementary_Mapping_Updated.txt` — referenced as upstream of the corpus (Case_01 Doc01 frontmatter; `00_COMMON/02_Regulatory_Mapping_Master.md`); `find` reports zero `.txt` files anywhere in the repo |
| **METADATA-INDEX** | 1 | `domains/index.md` — listing only, no build instructions, no version stamp |

---

## 3. Document Health

### 3.1 Frontmatter format — non-parseable in 38/38 docs
The 38 D-XX.Y.md files do NOT use the canonical leading-`---` YAML header that all Phase 1 / 2 / 3 deliverables use. Instead they place a pseudo-frontmatter **after** the H1 title and a separator:

```
# Part 1

---

document_id: AEGIS-PREPROC-SD-D-05.3
title: ...
phase: Pre-processing (Regulatory Baseline)
version: 0.1
...
```

This format is not parseable by any YAML library. It works visually, but means:
- No automated tool can ingest the corpus metadata (status, version, derivation).
- `doc-conventions` skill's pre-write checklist (8 mandatory fields) cannot be validated.

### 3.2 Conventional fields absent in 38/38 docs
- `inputs:` — 0 hits as frontmatter (2 body-text occurrences in `D-06.4` and `D-04.4` only).
- `outputs:` — 0 hits as frontmatter.
- `source:` — used inside the pseudo-frontmatter as a list (see `D-05.3.derivation`), but inconsistently across domains.

### 3.3 Status/version fields
- `status: DRAFT` in 38/38 D-XX.Y.md (none promoted to `ACTIVE` or `FROZEN`).
- `version: 0.1` in 38/38.
- `chain_version: v2.1` declared (cross-reference to a generator state).

### 3.4 Refs to deleted layout — pervasive
Every `D-XX.Y.md` body cites paths to the OLD flat `PREPROCESSING/` layout that was reorganised into the per-domain tree. Patterns observed:

| Pattern | Targets | Status |
|---------|---------|--------|
| `../../Regulation/{GDPR,CRA}/01_SecurityObjectives.md` | none in repo | DANGLING |
| `../../Regulation/{GDPR,CRA}/02_SecurityRules_NIST.md` | none in repo | DANGLING |
| `../../CrossRegulation/{DomainAnalysis,DeepAnalysis}/D-XX/...` | thousands of hits | DANGLING |
| `00_METHODOLOGY/PREPROCESSING/SubDomains/...` | none — replaced by `domains/D-XX_Y/...` | DANGLING (now obsolete; Case_01 Doc04-07 still cite the old paths) |

A direct `find -name '01_SecurityObjectives.md'` repo-wide returns zero hits. The corpus works as-is because the body content is inlined; the broken refs are decorative.

### 3.5 No tooling, no execution trail
- `reorg_by_domain_md.py` — credited inline in every merged D-XX.Y.md as "Generated by reorg_by_domain_md.py from PREPROCESSING/". File does not exist anywhere in the repo (only `scripts/dream/harness_audit.py` and `scripts/kg.sh` live under `scripts/`).
- `parse_domain.py` / `filter.py` — declared as outputs of the parser pilot in `PARSE_DOMAIN_EXECUTION_BRIEF.md`. No such files. No `scripts/parser/`, `scripts/domain/`, or `scripts/preproc/` directory.
- `SCHEMA_domain_json.md` / `SCHEMA/obligated_party.yaml` — referenced by the brief; not found.

---

## 4. Consumer Map

Approximate citation counts (grep across the whole repo) bucketed by consumer:

| Bucket | Approx hits | Examples |
|--------|------------:|----------|
| Methodology | ~10 | `dependency_graph.yaml:26,102` (corpus as protected dependency); `AGENTS.md`; `kg/GRAPHIFY.md` |
| Case_01 Phase 1 (RICH) | ~30 | Doc02, Doc04–10, Doc12–17, Doc19 cite `domains/D-XX.Y/` or `PREPROCESSING_by_domain/`; Doc13 heaviest (`Doc13_Adjusted_Goals.md:113,1427–1437,1453`) |
| Case_01 Phase 2/3 | many | Rules_Catalog etc., mostly via `kg.sh` indirection |
| Case_02 | ~23 | corpus used in applicability / mapping |
| Case_03 | ~26 | corpus used (Case_03 has all 5/5 regulations) |
| Dashboards / KG / scripts | ~10 | `GDPR_Dashboard.html`, `CRA_Dashboard.html`, `NIS2` inspect scripts, guard hook |
| Controls + overlays | ~388 | Doc13 sprint 10/11 NIST layers (corr-016, §3-expansion); Doc19 / Doc20 NIST inputs; Doc15 / Doc17 tensions; Case SPEC_NIST_MATRIX_UNIFIED |

**Total consumer weight:** ~800 unique citations. The corpus is the most-consumed artefact of the repo, and the least documented.

**KG linkage:** the E3 graph contains `D-05.3` exactly once (i.e., not per-subdomain) — `bash scripts/kg.sh where 'D-05.3'` resolves instead to Case_01 Phase-2/3 documents. The KG links to per-case derivations, not directly to the baseline corpus nodes.

---

## 5. Tooling & Source Gaps (the actual problem)

The corpus is content-complete (38/38 docs, 623 article copies, 172 control JSONs) but **reproduction is impossible from this repo alone**:

1. **Generator script missing** (`reorg_by_domain_md.py`) — the corpus is a black-box snapshot.
2. **Raw source texts missing** (no `.txt` anywhere) — `Taxonomia.txt` is referenced but not present.
3. **Parser pilot unexecuted** — the brief describes a deterministic parser (`parse_domain.py` + `filter.py` + `SCHEMA_domain_json.md`) but the artefact directory does not exist; the brief is also PT-language, suggesting the executor was a PT-speaking LLM session.
4. **No version stamp on `domains/index.md`** — even the index doesn't declare its own generation date.

These four gaps are why the corpus is treated as **frozen baseline**: the cost of regenerating it (rebuild script + re-source the raw files) is not amortised across the project yet.

---

## 6. Recommendations (not blocking v0)

These are **out of scope** for this v0 audit (would require touching `domains/**`, which is guard-protected), but should be tracked:

1. **Re-house `reorg_by_domain_md.py` under `scripts/`** when the source becomes available; until then, mark it explicitly as "untracked generator" in `PRODUCTION_FLOW.md`.
2. **Execute `PARSE_DOMAIN_EXECUTION_BRIEF.md`** as a separate sprint (with a human-in-the-loop per the brief's own design). Output `scripts/parse_domain.py` + `scripts/filter.py` + `scripts/SCHEMA_domain_json.md`; pilot against `D-01.1`.
3. **Promote one D-XX.Y.md** from DRAFT v0.1 to ACTIVE v1.0 as a pilot (pick D-05.3 — it's the one with `version: 0.1` + full SO hierarchy already in place). Would require lifting the `domains/**` guard for that single file or moving ACTIVE-state metadata to an out-of-tree sidecar.
4. **Re-source the missing `.txt` files** or formally deprecate the `source:` claim in the frontmatter strings (Case_01 Doc01 + `00_COMMON/02_Regulatory_Mapping_Master.md`).
5. **Cross-link CONTROLS/ + OVERLAYS/** into the case-level consumption map (Doc13 §3 already has the NIST layer; Doc19/20 should reference OVERLAY_*.md by name once we have a `PRODUCTION_FLOW.md` for Phase 2).

---

## 7. Audit Trail

- v0 of this audit was produced 2026-08-27 in support of writing `PRODUCTION_FLOW.md` for the Phase 0 baseline.
- Companion artefact: `00_METHODOLOGY/PREPROCESSING_by_domain/PRODUCTION_FLOW.md` (sibling).
- Methodology-side pointer: `00_METHODOLOGY/diagrams/fluxdiagram/phase1/phase1_rich_extension.md` (mentions S0–S3 in its Scope section).
- Case-side consumer pointer: `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/PRODUCTION_FLOW.md` (Layer 1 §2 now links upward to the Phase 0 baseline).
