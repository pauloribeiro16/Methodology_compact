# Harness Audit — Methodology_compact

_Generated 2026-08-27 by `scripts/dream/harness_audit.py` — auto-discovers the registry (hooks, MCP, subagents, commands, skills, scripts). Two-axis verdicts: **USO** (HEALTHY ≥3/wk · WEAK <3 · DEAD = 0×2wk · INSUFFICIENT-DATA = no db signal AND <1d old) and **QUALIDADE** (OK · ALERTS · CRITICAL · N/A) over the last 14d. Source for usage: `~/.zcode/cli/db/db.sqlite` (rollout transcripts are pruned to ~24h, the db is the historical truth)._

## Registry

| Name | Category | 7d | 14d | Eixo USO | Streak | Eixo QUALIDADE | Notes |
|---|---|---:|---:|---|---:|---|---|
| `hook:SessionStart:brief_hook.sh` | hook | 9 | 9 | **HEALTHY** | — | N/A |  |
| `hook:SessionStart:case_context_hook.sh` | hook | 5 | 5 | **HEALTHY** | — | N/A |  |
| `hook:UserPromptSubmit:kg-reminder.sh` | hook | 27 | 27 | **HEALTHY** | — | N/A |  |
| `hook:PreToolUse:guard-protected-files.sh` | hook | 4 | 4 | **HEALTHY** | — | N/A |  |
| `hook:PreToolUse:guard-bash.sh` | hook | 8 | 8 | **HEALTHY** | — | N/A |  |
| `mcp:skillnet` | mcp | 0 | 0 | **DEAD** | 6×0 | N/A |  |
| `agent:web-frontend` | subagent | 4 | 4 | **HEALTHY** | — | OK (95.4%) |  |
| `cmd:/case` | command | 164 | 205 | **HEALTHY** | — | N/A |  |
| `cmd:/doc-check` | command | 2 | 2 | **WEAK** | — | N/A |  |
| `cmd:/dream` | command | 110 | 110 | **HEALTHY** | — | N/A |  |
| `cmd:/harness-audit` | command | 15 | 15 | **HEALTHY** | — | N/A |  |
| `skill:case-context-loader` | skill | 2 | 2 | **WEAK** | — | OK (100.0%) |  |
| `skill:doc-conventions` | skill | 1 | 1 | **WEAK** | — | OK (100.0%) |  |
| `repo-skill:case-context-loader` | repo-skill | 2 | 2 | **WEAK** | — | OK (100.0%) |  |
| `repo-skill:doc-conventions` | repo-skill | 1 | 1 | **WEAK** | — | OK (100.0%) |  |
| `script:install_skills.sh` | script | 5 | 5 | **HEALTHY** | — | N/A |  |
| `script:kg.sh` | script | 197 | 203 | **HEALTHY** | — | N/A |  |
| `script:rename_case_files.py` | script | 7 | 7 | **HEALTHY** | — | N/A |  |
| `dream:adoption_audit.py` | dream-script | 16 | 16 | **HEALTHY** | — | N/A |  |
| `dream:harness_audit.py` | dream-script | 15 | 15 | **HEALTHY** | — | N/A |  |
| `dream:reconcile.py` | dream-script | 9 | 9 | **HEALTHY** | — | N/A |  |
| `dream:transcript_lib.py` | dream-script | 11 | 11 | **HEALTHY** | — | N/A |  |

## Saúde operacional (14d, por ferramenta)

| Tool | Usos | Ok% | Erros | Retried | Cancelled | p50 ms |
|---|---:|---:|---:|---:|---:|---:|
| `Bash` | 4669 | 97.7% | 107 | 0 | 0 | 1922 |
| `Read` | 1029 | 95.3% | 48 | 0 | 0 | 128 |
| `Edit` | 800 | 94.0% | 48 | 0 | 0 | 24 |
| `TodoWrite` | 543 | 100.0% | 0 | 0 | 0 | 16 |
| `mcp__node_repl__js` | 221 | 99.1% | 2 | 0 | 0 | 4585 |
| `Write` | 196 | 97.4% | 5 | 0 | 0 | 32 |
| `Agent` | 109 | 95.4% | 5 | 0 | 0 | 265452 |
| `AskUserQuestion` | 89 | 94.4% | 5 | 0 | 0 | 9 |
| `ExitPlanMode` | 83 | 24.1% | 63 | 0 | 0 | 5 |
| `WebFetch` | 36 | 94.4% | 2 | 0 | 0 | 25697 |
| `WebSearch` | 26 | 88.5% | 3 | 0 | 0 | 33852 |
| `Skill` | 24 | 100.0% | 0 | 0 | 0 | 40 |
| `TaskOutput` | 15 | 93.3% | 1 | 0 | 0 | 245179 |
| `TaskStop` | 9 | 88.9% | 1 | 0 | 0 | 21 |
| `CronUpdate` | 6 | 100.0% | 0 | 0 | 0 | 14 |
| `CronList` | 4 | 100.0% | 0 | 0 | 0 | 39 |
| `CronCreate` | 3 | 33.3% | 2 | 0 | 0 | 32 |
| `EnterPlanMode` | 2 | 100.0% | 0 | 0 | 0 | 13 |

## Eficácia do pipeline dream (8 ciclos)

_Sem commits nightly dream suficientes para estimar._

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
| OK | `kg.sh audit` | # graph: /home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/kg/E3_2026-08-23/graphify-out/graph.json | 69 |
| OK | `skillnet MCP handshake` | 2 tools | 141 |
| OK | `dashboard smoke --no-shots` | all passed | 11273 |

## AGENTS.md triage

| Path | Lines | Version | Hash | Changed since last audit |
|---|---|---|---|---|
| `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/AGENTS.md` | 231 | 4.6 | `0c207cd17056a8c0` | no |
| `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/00_METHODOLOGY/AGENTS.md` | 143 | 2.1 | `22ae3791d2bcf87a` | no |
| `/home/epmq-cyber/.zcode/AGENTS.md` | 53 |  | `ea97049744d41fd5` | no |

## Proposed patches (P7 — nunca auto-aplicados)

_Cada item DEAD/CRITICAL recebe proposta. Cada item WEAK/ALERTS recebe alvo de gatilho ou documentação. Cada decisão é humana._

### DEAD (0 usos em 2 auditorias consecutivas)
- `mcp:skillnet` — decidir: integrar no pre-flight, melhorar gatilhos, ou remover. Uso atual: 0 em 14d.
### WEAK (<3 usos/semana)
- `cmd:/doc-check` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 2/7d, 2/14d.
- `skill:case-context-loader` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 2/7d, 2/14d.
- `skill:doc-conventions` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 1/7d, 1/14d.
- `repo-skill:case-context-loader` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 2/7d, 2/14d.
- `repo-skill:doc-conventions` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 1/7d, 1/14d.
