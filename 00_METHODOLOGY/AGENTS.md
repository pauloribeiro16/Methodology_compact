---
document_id: AEGIS-METHODOLOGY-AGENTS
title: AGENTS.md — Scoped Instructions for 00_METHODOLOGY
phase: Cross-phase
version: 1.0
created: 2026-06-15
status: ACTIVE
---

# AGENTS.md — 00_METHODOLOGY

Scoped agent instructions for the methodology core directory. The root `AGENTS.md` (at repo root) governs the entire repository. This file adds methodology-specific rules.

## Skills (Activate on Demand)

Skills are loaded via the `skill` tool. When a task matches a skill's description, call `skill({ name: "<name>" })` to load its instructions.

| Skill | When |
|-------|------|
| **agents-md-writer** | Creating/updating any AGENTS.md file |
| **customize-opencode** | Editing opencode.json, agents, subagents, skills, plugins |
| **codebase-architecture** | Refactoring or restructuring the methodology core |
| **sprint-contract** | Implementing changes that span 3+ files |
| **python-best-practices** | Writing or refactoring Python in `01_IMPLEMENTATION_TOOLS/` |

---

## Commands

### Lint & Validation (from repo root, venv activated)

```bash
source .venv/bin/activate
python 01_IMPLEMENTATION_TOOLS/lints/run_all_lints.py --case "Case_01_TinyTask_SaaS"
python 01_IMPLEMENTATION_TOOLS/evals/eval_runner.py 02_CASES/Case_01_TinyTask_SaaS
python 01_IMPLEMENTATION_TOOLS/evals/quality_gate.py --case "Case_01_TinyTask_SaaS"
python 01_IMPLEMENTATION_TOOLS/evals/workflow_gate.py --check --file "<filename>" --case "<case>"
```

### Knowledge Graph Navigation (Graphify KG)

```bash
scripts/kg.sh impact <SR-ID>      # RP-1: ripple cost before changing (escalate if >50)
scripts/kg.sh where "<topic>"     # N1:  find which documents cover a topic
scripts/kg.sh trace "<A>" "<B>"   # RP-4: shortest path with confidence per hop
scripts/kg.sh doc "<doc-label>"   # N6:  what depends on this document
scripts/kg.sh domain <D-XX>       # N3:  reading order for a domain
scripts/kg.sh map                  # N2:  thematic map (community index)
scripts/kg.sh hub                  # RP-7: top architectural hubs
scripts/kg.sh nist <ctrl>          # RP-3: reverse NIST index
scripts/kg.sh hyper "<topic>"      # L3:  navigate hyperedge clusters
scripts/kg.sh audit                # integrity metrics
scripts/kg.sh help                 # full reference
```

Full reasoning patterns and integrity rules: `00_METHODOLOGY/REFERENCE/graphify.md`.
Every call is logged to `scripts/.kg_usage.log` — adoption is measured, not assumed.

### Before Modifying Any Document

```bash
python 01_IMPLEMENTATION_TOOLS/evals/workflow_gate.py --check --file "<filename>" --case "<case>"
# If the change touches a requirement/sub-domain ID, also run:
scripts/kg.sh impact <ID>
```

**If FAIL → STOP.** Report what's missing. Do NOT proceed.
**If KG impact returns >50 affected nodes → ESCALATE to user before writing** (P5 with evidence).

### After Modifying Any Document

```bash
python 01_IMPLEMENTATION_TOOLS/evals/validate_doc.py --file "<filename>" --case "<case>"
```

### Phase Context Loading

```bash
# Read optimised context instead of full AGENTS.md (~85% token savings)
cat 00_METHODOLOGY/CONTEXT/CONTEXT_PHASE1.md   # Phase 1 work
cat 00_METHODOLOGY/CONTEXT/CONTEXT_PHASE2.md   # Phase 2 work
cat 00_METHODOLOGY/CONTEXT/CONTEXT_PHASE3.md   # Phase 3 work
cat 00_METHODOLOGY/CONTEXT/CONTEXT_TOOLS.md    # Running tools
```

**The Regulatory Baseline is not a phase** — it is the frozen, company-agnostic regulatory baseline (pre-processing). When working on the regulatory baseline (e.g. adding or amending a regulation), load its contract instead:

```bash
cat 00_METHODOLOGY/REGULATORY_BASELINE.md     # Regulatory Baseline contract (frozen baseline)
```

---

## Project Structure

```
00_METHODOLOGY/
├── PREPROCESSING/          Regulatory Baseline — frozen, company-agnostic regulatory baseline
│                             (see REGULATORY_BASELINE.md for the contract;
│                              mutation via GUIDES/add_new_regulation.md)
├── REGULATORY_BASELINE.md  ← Regulatory Baseline contract (what it is, freeze policy, interface to Phase 1)
├── CONTEXT/                Phase context files (~1,200-1,800 tokens each)
├── QUALITY/                Quality criteria + evaluation system (9 files)
├── GUIDES/                 Agent/project orchestration guides (4 files, incl. add_new_regulation.md)
├── TEMPLATES/              22+ document templates (Phase 1-3)
├── diagrams/               ⚠️ NEW (2026-06-15) — All methodology diagrams
│   ├── Class_Models/       Static structure (what exists)
│   └── fluxdiagram/        Dynamic behaviour (what happens)
├── AGENTS.md               ← This file (scoped instructions)
├── CHANGE_IMPACT_MAP.md    Ripple effects for structural changes
├── MANIFESTO.md
└── README.md
```

**All diagram work happens under `diagrams/`.** Do not create new diagrams at the old `Class_Models/` root level.

---

## Code Style

- **Language policy:** All AEGIS documents in **English only** (per Language Policy). User conversation may match user's language.
- **Mermaid diagrams:** Use `flowchart TD` for process flows, `classDiagram` for class diagrams. Add a one-line comment above each diagram block.
- **Markdown tables:** Align with pipes for readability in raw form.
- **File naming:** `phase{N}_{purpose}.md` or `NN_Topic_Name.md` for templates.
- **Frontmatter:** All methodology documents have YAML frontmatter (id, title, phase, version, created, updated, author, status).

---

## ID Hierarchy (corr-008)

> **Authoritative schema for all AEGIS IDs.** See `00_METHODOLOGY/REFERENCE/key_concepts.md §ID Hierarchy` for the full spec.

| Prefix | Phase | Source |
|--------|-------|--------|
| `SO-D-XX.Y.{HL,GDPR,CRA,NIS2,DORA,AI_Act}` | Corpus | READ-ONLY (frozen baseline) |
| `AO-D-XX.X-NNN` | Phase 1 | Doc 07c |
| `PO-D-XX.X-NNN` | Phase 2 | Doc 10 §1.1 |
| `SO-D-XX.X-NNN` | Phase 2 | Doc 10 §1.2 (distinct from corpus SO namespace) |
| `RULE-D-XX.X-NNN` | Phase 2 | Doc 11 |
| `REQ-D-XX.X-NNN` | Phase 3 | Doc 23/24 |

**DEPRECATED legacy IDs (corr-007).** `PG-D-`, `SG-D-`, `CR-D-`, `BPR-D-` → see legacy alias tables in Doc 10 §7.5 and Doc 11 §11.5. New content MUST use the corr-008 schema.

**Cross-document ID validator.** `01_IMPLEMENTATION_TOOLS/scripts/validate_aegis_ids.py` reports broken refs, orphans, and duplicates. Run before any case-level migration.

---

## Git Workflow

- **Branch strategy:** `main` for all methodology content. KG work uses dedicated branches.
- **Branch workflow (MANDATORY):** Use `./scripts/create-feature.sh`, `./scripts/finish-feature.sh`, `./scripts/merge-feature.sh`. Never commit directly to `main`.
- **Commit message format:** `[<AGENT>] <scope>: <action> — <case>` (e.g., `[EXECUTOR] Doc 08: Generated Obligation Derivation — Case_01`).
- **Pre-commit hook:** `./.hooks/pre-commit` runs automatically. Do not bypass with `--no-verify` unless emergency.

---

## Boundaries

### ✅ Always

- Load `CONTEXT/CONTEXT_PHASE{N}.md` before doing phase work
- Run `workflow_gate.py --check` before modifying any document
- When changing requirement/sub-domain IDs, also run `scripts/kg.sh impact <ID>` to quantify ripple cost (P5)
- Run `validate_doc.py` after modifying any document
- Use Mermaid for all diagrams (consistency)
- Update `diagrams/README.md` decision log when adding diagrams
- Add cross-references between related class and flow diagrams

### ⚠️ Ask First

- Moving files between directories (affects references in 17+ places)
- Changing the diagram structure (D14 was a structural change)
- Adding new files to `TEMPLATES/` (affects case generation)
- Modifying root `AGENTS.md` (affects all agents)

### 🚫 Never

- Commit directly to `main` (use the branch workflow)
- Edit `Case_0X/progress.json` directly (use the read_progress tool)
- Create diagrams outside `diagrams/` directory
- Duplicate class diagram logic in flow diagrams (different abstraction level)
- Show all dynamic elements at once in a flow diagram (progressive disclosure)
- Add emoji to files (unless explicitly requested)
- Skip lint/validation steps
- Bypass pre-commit hooks with `--no-verify` (unless emergency)

---

## Diagram Design Rules (from `diagrams/README.md`)

- **Class diagrams** show entities and relationships (static)
- **Flow diagrams** show process and decisions (dynamic)
- **Both** organised by phase
- **Flow diagrams:** `flowchart TD`, subgraphs for internal stages, progressive disclosure, matrix lookup for conditional blocks

### Node Style Rules (all fluxdiagram files)

- **Node text** = short label (1-5 words). Optionally one sub-line via `<br/>`. No bullets (`•`, `·`), no explanations, no conditions in parens
- **LLM badge** = inline as `[LLM]` after the name, no ID suffix. Example: `"Interpretation [LLM]"` (not `"[LLM-A]"`)
- **Deterministic label** = never. The grey colour already indicates it
- **Rule IDs (DR-XX, TT-XX, etc.)** = only in Step Reference tables, not inside nodes. Never as standalone nodes connected by arrows
- **Decision questions** = short, no preamble. `"Multi-reg on same sub-domain?"` not `"For each applicable clause, what derivation path?"`
- **One `end` per `subgraph`** = never leave a subgraph open or add redundant `end` statements
- **`subgraph` titles** = plain text, no quotes, no `<br/>`. Example: `subgraph P2A["Phase 2A — Obligation Derivation"]` is OK; no nested subgraphs unless absolutely necessary
- **Avoid `FIX`/`Re-derive`/`Re-resolve` feedback loops** in overview diagrams. They belong in detail files only. Loops make overview hard to read
- **Reuse standard node IDs** across the phase: `P1` (Phase 1 handoff), `TAX` (taxonomy), `OUT` (phase output), `D08`/`D09`/... (doc nodes), `GATEB`/`GATEC`/... (gates)
- **Class assignments** = at the bottom of each mermaid block, one `class` line per type. Don't scatter styling inline
- **Structure of all detail files** is fixed: Frontmatter, Overview, Diagram 1 (process), Diagram 2 (decision), Step Reference, Rule/Concept detail, Gate criteria, Cross-case, What it does NOT show, Colour note, See also

### Cross-file Consistency Rules

- **Same nomenclatura across all phase detail files** in `fluxdiagram/phaseN/`: node IDs (`P1`, `D08`, `GATEB`), colours, and section order must match
- **Step Reference tables** use the same columns in all files: `Step | Name | Type | Section | LLM`
- **Cross-references** between files use the relative path pattern `[`name`](relative/path.md)` — never absolute paths
- **Don't duplicate class diagram logic** in flow diagrams. Flow diagrams show process; class diagrams show entities

---

**Version:** 1.0 (2026-06-15)
**See also:** [`../AGENTS.md`](../AGENTS.md) (root), [`diagrams/README.md`](diagrams/README.md) (diagram decisions)
