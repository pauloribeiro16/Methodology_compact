# ALT-ANCHOR Fase 1 — Executor Report (frozen referential sources)

**Date:** 2026-09-05 · **Executed in-conversation by Orchestrator** (subagent dispatch blocked by model concurrency limits)

## Deliverables — 5 referential dirs under `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/`

| Dir | Content | Count | Source (official) | Verification |
|---|---|---|---|---|
| `NIST_80053R5/` | 20 family JSONs (AC…SR) | **719 controls+enhancements** (id+name) | `nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf` | pdftotext of official PDF; baseline-col letters stripped; 88 PF-referenced ids ⊂ set (verified) |
| `NIST_SSDF/` | `SSDF.json` | **21 practices / 47 tasks** | `nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf` | all 47 task ids from official PDF definition lines; the commonly cited "42 tasks" is WRONG (manifest documents this) |
| `OWASP_ASVS/` | `ASVS_sections.json` | **14 chapters / 71 sections (V*.x)** | `github.com/OWASP/ASVS @ v4.0.3, 4.0/en/*.md` (official) | curl of all 14 official chapter markdowns; section headers parsed |
| `OWASP_SAMM/` | `SAMM_streams.json` | **5 functions / 15 practices / 30 streams** | `github.com/owaspsamm/core` (official model ymls, develop branch) | all 30 stream ymls + 15 practice ymls fetched and linked via model hashes |
| `NIST_CSF_2.0/` | `CSF_2.0.json` | **106 subcategories** | `nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf` | official CSF 2.0 final PDF; count matches the canonical 106 |

Each dir has `_MANIFEST.json` with source URLs, fetched date, counts and caveats.

## Caveats (honest, manifest-recorded)

- 800-53r5 **names** are informational (pdftotext extraction); **ids authoritative**. Two ids cited by PF crosswalks are r4-legacy families retired in r5: `IP-3` (Individual Participation), `DM-1` (Disclosure) — registered as `legacy_alias_ids` in the manifest, gates must accept them explicitly as legacy citations.
- SSDF task **names** may be truncated by the PDF 3-column layout; ids authoritative and complete.
- ASVS frozen at **section granularity (V*.x)** — anchors use sections (e.g. V3.5), not requirement level (V3.5.2). Valid ids = sections ∪ chapters.
- CSF 2.0 titles truncated; ids authoritative (all 106).
- Bonus fix discovered: the C1 gate's CSF check was silently SKIPPED (warning) because `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_CSF_2.0_subcategories.md` does not exist in this repo. `NIST_CSF_2.0/CSF_2.0.json` now provides the real frozen list — all three gates get a hard CSF check in Fase 3.

## Census anchor spot-check (against frozen lists)

800-53 anchors proposed in `ALT_ANCHOR_CENSUS_v0.md`: **ALL 24 OK** · SSDF: ALL OK ·
ASVS: V3.3/V3.5 OK (chapter-level ids also valid) · SAMM: use full function-prefix codes
(G-EG-A, VR-B — not bare "EG"/"VR"). Write-back must use prefixed stream codes.
