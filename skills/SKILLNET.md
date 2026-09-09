# SkillNet Integration — Methodology_compact

> **Status**: integrated 2026-08-26. Roles: **producer + consumer (phased)**.
> `evaluate`/`create` **deferred** — pending backend LLM decision (ollama local vs OpenAI-compatible key).

---

## What SkillNet is

Open infrastructure that treats **agent skills as software assets** — searchable,
installable, inspectable, evaluable, composable (zjunlp / Zhejiang University NLP;
MIT; paper arXiv:2603.04448; hub with 600K+ indexed GitHub skills). Skill format =
portable folder `SKILL.md + scripts/ + references/` (the same `SKILL.md` convention
that several open-agent projects adopted — the AEGIS skills in this repo follow it
too, so they are valid SkillNet skills and vice-versa).

## Roles adopted here

| Role | What | Status |
|---|---|---|
| **Producer** | AEGIS repeatable workflows packaged as versioned skills in `skills/` | active — 2 skills (below) |
| **Consumer** | Search/download external skills from the hub when case work needs them | active — MCP + CLI channels |
| Evaluator | 5-axis scoring (safety, completeness, executability, maintainability, cost) of our skills | **deferred** (needs LLM backend) |

### AEGIS skills in this repo

| Skill | Invoked when |
|---|---|
| `case-context-loader` | pre-flight of any case work — loads GLOBAL → case → phase state chain |
| `doc-conventions` | before writing/editing any methodology document (IDs, frontmatter, citations) |
| `writing-use-cases` | when drafting/reviewing UC cards or UC/sequence diagrams in any Phase 3 deliverable (Doc20/21/22, Doc31, Doc32, annexes A/B) |

Install into ZCode: `bash scripts/install_skills.sh` (symlinks into `~/.zcode/skills/`;
restart the session afterwards).

## Channels (consumer)

| Channel | Where | Needs key? |
|---|---|---|
| **MCP server** | registered in `.zcode/config.json` → `mcp.servers.skillnet` (workspace scope, auto-connects); tools: `search_skills`, `download_skill`, `health_check`, `import_best_skill`, `get_skill_rules` | no (for search/download) |
| **CLI** | `skillnet` (on PATH via `~/.local/bin/skillnet` → venv `~/.venvs/skillnet`); `search` (keyword/vector), `download`, `create`, `evaluate`, `analyze`, `orchestrate` | no for search/download; `create`/`evaluate`/`analyze` need `API_KEY`+`BASE_URL` |

Local footprint (outside the repo):
- venv: `~/.venvs/skillnet` (`pip install skillnet-ai`)
- MCP server clone: `~/.local/share/skillnet-mcp` (github.com/CycleChain/skillnet-mcp, Node stdio)
- upgrades: `~/.venvs/skillnet/bin/pip install -U skillnet-ai` and `git -C ~/.local/share/skillnet-mcp pull`

## Usage (search & download — no key)

```bash
skillnet search "markdown lint" --mode keyword     # or --mode vector (semantic)
skillnet search "xlsx" --limit 5 --sort-by stars
skillnet download <skill-url> -d <dest>            # URL comes from search results
```

Search results already carry the hub's pre-computed 5-axis evaluation scores and
stars — use them to prefer high-quality skills even without local `evaluate`.

## Deferred: evaluate / create (5 quality axes)

`skillnet evaluate <skill-dir>` scores **Safety, Completeness, Executability,
Maintainability, Cost-awareness**. Blocked on choosing an LLM backend
(`API_KEY`/`BASE_URL`, OpenAI-compatible; default model gpt-4o). Options:
local ollama (offline, free) vs external API (better quality). Decision pending.
When enabled: evaluate both AEGIS skills, record scores in this file, and re-run
after material skill changes.

## Safety rules (P7 — human is arbiter)

1. **External skills are third-party code + prompts.** Download to a review area,
   read `SKILL.md` and any scripts **before** installing into `~/.zcode/skills/`.
2. The human approves any external skill entering the AEGIS workflow — same rule
   as any other methodology scope decision.
3. Never commit downloaded third-party skills into this repo without review;
   keep them in `~/.zcode/skills/` or a gitignored folder.
4. `create_skill`/`evaluate_skill` via MCP share the same deferral as the CLI.

## Why this is not "a funny accessory"

Adoption is structural, not optional: the two AEGIS skills are wired into the
root `AGENTS.md` pre-flight (case work → `case-context-loader`; doc writing →
`doc-conventions`), the same pattern that made the KG stick (mandated P5 step +
usage log + reminder hook). External search is on-demand tooling for real gaps
(xlsx/docx/pdf generation for case deliverables), not a demo.

## Provenance

- SkillNet: https://github.com/zjunlp/SkillNet · paper arXiv:2603.04448 (Liang et al., 2026) · Explorer: skillnet.openkg.cn · MIT
- MCP server: https://github.com/CycleChain/skillnet-mcp (stdio, wraps the Python CLI)
- Paper results for context: +40% average reward, −30% execution steps with skills vs without (ALFWorld/WebShop/ScienceWorld)
