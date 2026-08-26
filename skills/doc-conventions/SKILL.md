---
name: doc-conventions
description: "Use before writing or editing any AEGIS methodology document in Methodology_compact (case deliverables Docs 01-25, domain D-XX.Y files, rules catalogs, requirements). Covers the corr-008 ID hierarchy, deprecated IDs, mandatory YAML frontmatter, file naming, and citation rules. Trigger phrases: write a doc, edit a document, create requirement, new rule ID, add frontmatter, validate document conventions."
---

# AEGIS Document Conventions

Executable core of the document conventions for the AEGIS compact repo.
Authoritative source: `00_METHODOLOGY/AGENTS.md` (ID hierarchy + code style) —
this skill mirrors the parts needed while writing. When in doubt, the
`00_METHODOLOGY/AGENTS.md` version wins.

## ID Hierarchy (corr-008) — mandatory

| Prefix | Phase / Scope | Source document |
|---|---|---|
| `SO-D-XX.Y.{HL,GDPR,CRA,NIS2,DORA,AI_Act}` | Corpus — READ-ONLY, frozen baseline | domain `D-0X.Y.md` |
| `AO-D-XX.X-NNN` | Phase 1 — Adjusted Objectives | Doc 07c |
| `PO-D-XX.X-NNN` | Phase 2 — Privacy Objectives | Doc 10 §1.1 |
| `SO-D-XX.X-NNN` | Phase 2 — Security Objectives (distinct from corpus SO namespace) | Doc 10 §1.2 |
| `RULE-D-XX.X-NNN` | Phase 2 — Rules | Doc 11 |
| `REQ-D-XX.X-NNN` | Phase 3 — Requirements | Doc 23/24 |

**DEPRECATED (corr-007):** `PG-D-`, `SG-D-`, `CR-D-`, `BPR-D-` — legacy alias
tables live in Doc 10 §7.5 and Doc 11 §11.5. **Never introduce deprecated
prefixes in new content.**

## Frontmatter — every methodology document

```yaml
---
document_id: <AEGIS-ID>
title: <title>
phase: <1|2|3|Cross-phase>
version: <semver>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
author: <agent or human>
status: <DRAFT|ACTIVE|DEPRECATED>
---
```

## File naming

- Case artefacts / templates: `NN_Topic_Name.md` (e.g. `11_Rules_Catalog.md`)
- Phase scripts: `phase{N}_{purpose}.md`
- Domain corpus: `D-XX.Y.md` + `_index.md` + `.manifest.json` + `articles/`

## Citation rules (source-faithfulness)

- Every regulatory claim cites **Article + paragraph** (e.g. `GDPR Art. 32(1)(c)`),
  never a bare `Art. 32` — this also matters for KG `trace` disambiguation
  (see `kg/GRAPHIFY.md`, Query workarounds §2).
- Distinguish the two rationale axes (P1): **compliance rationale ≠ security
  rationale** — state which one each requirement serves.
- KG-derived relations cited downstream must quote **(relation, confidence)
  as a pair**; INFERRED edges are hypotheses, mark `[INFERRED — needs
  verification]`, never audit evidence.

## Pre-write checklist

1. Correct ID prefix for the hosting document (table above)?
2. Frontmatter complete (all 8 fields)?
3. File name follows `NN_Topic_Name.md`?
4. Regulatory claims cite Art. + paragraph?
5. If the doc mentions existing IDs: `scripts/kg.sh impact <ID>` run first (P5)?
6. English only (language policy); conversation may match the user's language.
