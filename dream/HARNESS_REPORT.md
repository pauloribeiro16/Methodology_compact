# Harness Audit — Methodology_compact

_Generated 2026-08-27 by `scripts/dream/harness_audit.py` — auto-discovers the registry (hooks, MCP, subagents, commands, skills, scripts). Source for usage: `~/.zcode/cli/db/db.sqlite` (transcripts in `rollout/` are pruned to ~24h, the db is the historical truth). Static + live health probes below._

## Registry

| Name | Category | 7d | 14d | Verdict | Notes |
|---|---|---:|---:|---|---|
| `hook:SessionStart:brief_hook.sh` | hook | 9 | 9 | **INSUFFICIENT-DATA** |  |
| `hook:SessionStart:case_context_hook.sh` | hook | 5 | 5 | **INSUFFICIENT-DATA** |  |
| `hook:UserPromptSubmit:kg-reminder.sh` | hook | 27 | 27 | **INSUFFICIENT-DATA** |  |
| `hook:PreToolUse:guard-protected-files.sh` | hook | 4 | 4 | **INSUFFICIENT-DATA** |  |
| `hook:PreToolUse:guard-bash.sh` | hook | 5 | 5 | **INSUFFICIENT-DATA** |  |
| `mcp:skillnet` | mcp | 0 | 0 | **WEAK** |  |
| `agent:web-frontend` | subagent | 4 | 4 | **HEALTHY** |  |
| `cmd:/case` | command | 162 | 203 | **HEALTHY** |  |
| `cmd:/doc-check` | command | 1 | 1 | **WEAK** |  |
| `cmd:/dream` | command | 82 | 82 | **HEALTHY** |  |
| `skill:case-context-loader` | skill | 2 | 2 | **WEAK** |  |
| `skill:doc-conventions` | skill | 0 | 0 | **WEAK** |  |
| `repo-skill:case-context-loader` | repo-skill | 2 | 2 | **INSUFFICIENT-DATA** |  |
| `repo-skill:doc-conventions` | repo-skill | 0 | 0 | **INSUFFICIENT-DATA** |  |
| `script:install_skills.sh` | script | 5 | 5 | **INSUFFICIENT-DATA** |  |
| `script:kg.sh` | script | 190 | 196 | **INSUFFICIENT-DATA** |  |
| `script:rename_case_files.py` | script | 7 | 7 | **INSUFFICIENT-DATA** |  |
| `dream:adoption_audit.py` | dream-script | 15 | 15 | **INSUFFICIENT-DATA** |  |
| `dream:harness_audit.py` | dream-script | 5 | 5 | **INSUFFICIENT-DATA** |  |
| `dream:reconcile.py` | dream-script | 9 | 9 | **INSUFFICIENT-DATA** |  |
| `dream:transcript_lib.py` | dream-script | 10 | 10 | **INSUFFICIENT-DATA** |  |

## Health (static)

| Severity | Target | Message |
|---|---|---|
| OK | `/home/epmq-cyber/.zcode/cli/config.json` | valid JSON |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/.zcode/config.json` | valid JSON |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/dream/brief_hook.sh` | bash -n clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/dream/case_context_hook.sh` | bash -n clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/.zcode/hooks/kg-reminder.sh` | bash -n clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/.zcode/hooks/guard-protected-files.sh` | bash -n clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/.zcode/hooks/guard-bash.sh` | bash -n clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/install_skills.sh` | bash -n clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/kg.sh` | bash -n clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/rename_case_files.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/dream/adoption_audit.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/dream/harness_audit.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/dream/reconcile.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/dream/transcript_lib.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/AGENTS.md` | 230 lines |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/00_METHODOLOGY/AGENTS.md` | 142 lines |
| OK | `/home/epmq-cyber/.zcode/AGENTS.md` | 53 lines |

## Health (live)

| Severity | Target | Detail | ms |
|---|---|---|---|
| OK | `kg.sh audit` | # graph: /home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/kg/E3_2026-08-23/graphify-out/graph.json | 66 |
| OK | `skillnet MCP handshake` | 2 tools | 137 |
| OK | `dashboard smoke --no-shots` | all passed | 11557 |

## AGENTS.md triage

| Path | Lines | Version | Hash | Changed since last audit |
|---|---|---|---|---|
| `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/AGENTS.md` | 231 | 4.6 | `0c207cd17056a8c0` | no |
| `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/00_METHODOLOGY/AGENTS.md` | 143 | 2.1 | `22ae3791d2bcf87a` | no |
| `/home/epmq-cyber/.zcode/AGENTS.md` | 53 |  | `ea97049744d41fd5` | no |

## Proposed patches (P7 — never auto-applied)

_Each DEAD item without a plan gets a wiring-or-removal proposal. Each WEAK item gets a triggers/documentation proposal._

### WEAK items (<3 uses per week)
- `mcp:skillnet` — refine description / add a task-pattern line, or remove from mandates. Current usage: 0 this week, 0 over 14d.
- `cmd:/doc-check` — refine description / add a task-pattern line, or remove from mandates. Current usage: 1 this week, 1 over 14d.
- `skill:case-context-loader` — refine description / add a task-pattern line, or remove from mandates. Current usage: 2 this week, 2 over 14d.
- `skill:doc-conventions` — refine description / add a task-pattern line, or remove from mandates. Current usage: 0 this week, 0 over 14d.
