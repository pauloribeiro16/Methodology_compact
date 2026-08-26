---
document_id: AEGIS-METHODOLOGY-AGENTS
title: AGENTS.md — Scoped Instructions for 00_METHODOLOGY
phase: Cross-phase
version: 2.0
created: 2026-06-15
updated: 2026-08-26
status: ACTIVE
---

# AGENTS.md — 00_METHODOLOGY

Scoped instructions for the methodology core directory. The root `AGENTS.md` governs the whole repository. This file adds rules specific to `00_METHODOLOGY/`.

> **Tooling reminder.** The lint runner, eval suite, and `kg.sh` live in the main AEGIS repo and are **not available here**. Validation against the full suite must happen there. In this compact repo, validation is manual and follows the ID hierarchy and conventions below.

---

## Project Structure (actual)

```
00_METHODOLOGY/
├── AGENTS.md                       This file
├── dependency_graph.yaml           Manual impact map for ID-bearing documents
├── PREPROCESSING_by_domain/        Domain corpus (the regulatory baseline, frozen per sub-domain)
│   ├── domains/index.md            Index of D-01…D-10 + their sub-domains
│   ├── domains/D-0X_*/             One folder per domain (e.g. D-01_Data-Protection)
│   │   └── D-0X.Y*/                Sub-domain folder; contains D-0X.Y.md, _index.md, .manifest.json, articles/
│   ├── CONTROLS/                   NIST controls (reference, not authoritative corpus IDs)
│   │   ├── NIST_AI_RMF/{GOVERN,MAP,MEASURE,MANAGE}
│   │   └── NIST_PF/{GOVERN-P,IDENTIFY-P,PROTECT-P,COMMUNICATE-P,CONTROL-P}
│   └── MAPPINGS/OVERLAYS/          Cross-framework overlay documents
├── diagrams/                       All methodology diagrams (Mermaid)
│   ├── Class_Models/               Static structure
│   └── fluxdiagram/{phase1,phase2,phase3}/   Dynamic behaviour, by phase
├── 00_NIS2_Mapping/                NIS 2 ↔ NIST CSF × SP 800-53r5 mapping xlsx + build scripts
└── 00_VISUALISATIONS/              HTML dashboards + Case_01 workbook
```

**All diagram work happens under `diagrams/`.** Do not create diagrams at the repo root or in case folders.

**Note:** the corpus sub-domain IDs follow the shape `D-0X.Y` (e.g. `D-01.3`). Case-level IDs add a phase prefix (see next section).

---

## ID Hierarchy (corr-008)

Authoritative schema for all AEGIS IDs.

| Prefix | Phase / Scope | Source document |
|---|---|---|
| `SO-D-XX.Y.{HL,GDPR,CRA,NIS2,DORA,AI_Act}` | Corpus — READ-ONLY, frozen baseline | domain `D-0X.Y.md` |
| `AO-D-XX.X-NNN` | Phase 1 — Adjusted Objectives | Doc 07c |
| `PO-D-XX.X-NNN` | Phase 2 — Privacy Objectives | Doc 10 §1.1 |
| `SO-D-XX.X-NNN` | Phase 2 — Security Objectives (distinct from corpus SO namespace) | Doc 10 §1.2 |
| `RULE-D-XX.X-NNN` | Phase 2 — Rules | Doc 11 |
| `REQ-D-XX.X-NNN` | Phase 3 — Requirements | Doc 23/24 |

**DEPRECATED legacy IDs (corr-007).** `PG-D-`, `SG-D-`, `CR-D-`, `BPR-D-` — see legacy alias tables in Doc 10 §7.5 and Doc 11 §11.5. **New content MUST use corr-008.**

> ⚠️ The cross-document ID validator (`01_IMPLEMENTATION_TOOLS/scripts/validate_aegis_ids.py`) lives in the main repo. In this compact repo, manually verify: ID prefix matches the doc that hosts it, no orphans in `grep -r`, no duplicates.

---

## Boundaries

### ✅ Always

- Follow the root AGENTS.md design principles P0–P7
- Read the relevant case's `PROJECT_STATE.md` (chain: case root → phase root) before editing case artefacts
- When changing an ID-bearing document, consult `00_METHODOLOGY/dependency_graph.yaml` and `grep -r` the ID across the affected subtree (P5)
- Maintain source-faithfulness: every regulatory claim cites Article + paragraph
- Distinguish the two security-rationale perspectives (P1): compliance rationale ≠ security rationale
- Use Mermaid for all diagrams and respect `diagrams/README.md` style rules
- Update the `diagrams/README.md` decision log when adding diagrams

### ⚠️ Ask First

- Moving files between directories (cross-references multiply)
- Changing diagram structure or node IDs in `fluxdiagram/`
- Adding new sub-domains under `PREPROCESSING_by_domain/domains/` (frozen baseline mutation)
- Modifying the root `AGENTS.md` (affects all agents)

### 🚫 Never

- Edit `Case_0X/progress.json` directly (this is a structured snapshot, not a free-form note)
- Create diagrams outside `diagrams/`
- Duplicate class-diagram logic in flow diagrams (different abstraction level)
- Add new emojis to documents unless explicitly requested
- Introduce new ID prefixes without consulting Orchestrator
- Bypass P0 (disagreement articulation) or P7 (human arbitration)

---

## Code Style

- **Language policy:** AEGIS documents in **English only**. User conversation may match the user's language.
- **Mermaid:** `flowchart TD` for process flows, `classDiagram` for class diagrams. Add a one-line comment above each diagram block.
- **Markdown tables:** align with pipes for readability in raw form.
- **File naming:** `NN_Topic_Name.md` (templates), `phase{N}_{purpose}.md` (case artefacts).
- **Frontmatter:** every methodology document has YAML frontmatter (id, title, phase, version, created, updated, author, status).
- **Python (when needed):** PEP 8, type hints, descriptive names — applies to the 18 `.py` files under `00_NIS2_Mapping/`.

---

## Diagram rules

See `diagrams/README.md` for the full guide. Highlights:

- **Class diagrams** show entities/relationships (static); **flow diagrams** show process/decisions (dynamic)
- Standard node IDs reused across phase detail files: `P1`, `TAX`, `OUT`, `D08`/`D09`/…, `GATEB`/`GATEC`/…
- Node text = 1–5 words, no bullets, no parenthetical conditions
- LLM badges inline as `[LLM]` after the name (e.g. `"Interpretation [LLM]"`)
- Rule IDs (`DR-XX`, `TT-XX`) belong only in Step Reference tables, never as nodes
- Structure of detail files is fixed: Frontmatter → Overview → Diagram 1 (process) → Diagram 2 (decision) → Step Reference → Rule/Concept detail → Gate criteria → Cross-case → What it does NOT show → Colour note → See also

---

**Version:** 2.0 (compact-repo rewrite, 2026-08-26)
**See also:** [`../AGENTS.md`](../AGENTS.md) (root), [`diagrams/README.md`](diagrams/README.md) (diagram decisions)
