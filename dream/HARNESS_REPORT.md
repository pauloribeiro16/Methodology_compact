# Harness Audit — Methodology_compact

_Generated 2026-08-30 by `scripts/dream/harness_audit.py` — auto-discovers the registry (hooks, MCP, subagents, commands, skills, scripts). Two-axis verdicts: **USO** (HEALTHY ≥3/wk · WEAK <3 · DEAD = 0×2wk · INSUFFICIENT-DATA = no db signal AND <1d old) and **QUALIDADE** (OK · ALERTS · CRITICAL · N/A) over the last 14d. Source for usage: `~/.zcode/cli/db/db.sqlite` (rollout transcripts are pruned to ~24h, the db is the historical truth)._

## Registry

| Name | Category | 7d | 14d | Eixo USO | Streak | Eixo QUALIDADE | Notes |
|---|---|---:|---:|---|---:|---|---|
| `hook:SessionStart:brief_hook.sh` | hook | 9 | 9 | **HEALTHY** | — | N/A |  |
| `hook:SessionStart:case_context_hook.sh` | hook | 5 | 5 | **HEALTHY** | — | N/A |  |
| `hook:UserPromptSubmit:kg-reminder.sh` | hook | 27 | 27 | **HEALTHY** | — | N/A |  |
| `hook:PreToolUse:guard-protected-files.sh` | hook | 4 | 4 | **HEALTHY** | — | N/A |  |
| `hook:PreToolUse:guard-bash.sh` | hook | 8 | 8 | **HEALTHY** | — | N/A |  |
| `mcp:skillnet` | mcp | 6 | 6 | **HEALTHY** | — | ALERTS (ok 75.0%, 2 err, 0 retried) | matched mcp__skillnet__search_skills; matched mcp__skillnet__import_best_skill |
| `agent:web-frontend` | subagent | 6 | 6 | **HEALTHY** | — | OK (94.6%) |  |
| `cmd:/case` | command | 259 | 265 | **HEALTHY** | — | N/A |  |
| `cmd:/doc-check` | command | 2 | 2 | **WEAK** | — | N/A |  |
| `cmd:/dream` | command | 140 | 140 | **HEALTHY** | — | N/A |  |
| `cmd:/grill-me` | command | 14 | 14 | **HEALTHY** | — | N/A |  |
| `cmd:/harness-audit` | command | 19 | 19 | **HEALTHY** | — | N/A |  |
| `skill:case-context-loader` | skill | 2 | 2 | **WEAK** | — | OK (100.0%) |  |
| `skill:doc-conventions` | skill | 1 | 1 | **WEAK** | — | OK (100.0%) |  |
| `repo-skill:case-context-loader` | repo-skill | 2 | 2 | **WEAK** | — | OK (100.0%) |  |
| `repo-skill:doc-conventions` | repo-skill | 1 | 1 | **WEAK** | — | OK (100.0%) |  |
| `script:install_skills.sh` | script | 5 | 5 | **HEALTHY** | — | N/A |  |
| `script:kg.sh` | script | 257 | 257 | **HEALTHY** | — | N/A |  |
| `script:port_c3_fase4_doc21.py` | script | 4 | 4 | **HEALTHY** | — | N/A |  |
| `script:port_c3_fase5_doc20.py` | script | 4 | 4 | **HEALTHY** | — | N/A |  |
| `script:port_fase4_doc19_51.py` | script | 2 | 2 | **WEAK** | — | N/A |  |
| `script:port_fase4_doc19_part2.py` | script | 2 | 2 | **WEAK** | — | N/A |  |
| `script:port_fase4_doc19_part3.py` | script | 2 | 2 | **WEAK** | — | N/A |  |
| `script:port_fase4_spec.py` | script | 2 | 2 | **WEAK** | — | N/A |  |
| `script:port_fase5_annexes.py` | script | 1 | 1 | **WEAK** | — | N/A |  |
| `script:port_fase5_doc18.py` | script | 3 | 3 | **HEALTHY** | — | N/A |  |
| `script:rename_case_files.py` | script | 8 | 8 | **HEALTHY** | — | N/A |  |
| `dream:adoption_audit.py` | dream-script | 18 | 18 | **HEALTHY** | — | N/A |  |
| `dream:harness_audit.py` | dream-script | 19 | 19 | **HEALTHY** | — | N/A |  |
| `dream:reconcile.py` | dream-script | 15 | 15 | **HEALTHY** | — | N/A |  |
| `dream:transcript_lib.py` | dream-script | 11 | 11 | **HEALTHY** | — | N/A |  |

## Saúde operacional (14d, por ferramenta)

| Tool | Usos | Ok% | Erros | Retried | Cancelled | p50 ms |
|---|---:|---:|---:|---:|---:|---:|
| `Bash` | 6213 | 98.0% | 120 | 0 | 0 | 1290 |
| `Read` | 1371 | 95.3% | 65 | 0 | 0 | 141 |
| `Edit` | 1163 | 92.7% | 85 | 0 | 0 | 23 |
| `TodoWrite` | 659 | 99.8% | 1 | 0 | 0 | 16 |
| `Write` | 241 | 97.1% | 7 | 0 | 0 | 26 |
| `mcp__node_repl__js` | 233 | 98.7% | 3 | 0 | 0 | 4758 |
| `Agent` | 130 | 94.6% | 7 | 0 | 0 | 283049 |
| `AskUserQuestion` | 101 | 92.1% | 8 | 0 | 0 | 9 |
| `ExitPlanMode` | 96 | 18.8% | 78 | 0 | 0 | 4 |
| `WebFetch` | 37 | 97.3% | 1 | 0 | 0 | 25865 |
| `WebSearch` | 32 | 90.6% | 3 | 0 | 0 | 30664 |
| `Skill` | 27 | 100.0% | 0 | 0 | 0 | 41 |
| `TaskOutput` | 15 | 93.3% | 1 | 0 | 0 | 245179 |
| `mcp__skillnet__search_skills` | 7 | 71.4% | 2 | 0 | 0 | 3724 |
| `CronUpdate` | 6 | 100.0% | 0 | 0 | 0 | 14 |
| `CronCreate` | 4 | 50.0% | 2 | 0 | 0 | 40 |
| `CronList` | 4 | 100.0% | 0 | 0 | 0 | 39 |
| `TaskStop` | 4 | 100.0% | 0 | 0 | 0 | 30 |
| `EnterPlanMode` | 3 | 100.0% | 0 | 0 | 0 | 12 |
| `mcp__skillnet__import_best_skill` | 1 | 100.0% | 0 | 0 | 0 | 2729 |

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
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/port_c3_fase4_doc21.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/port_c3_fase5_doc20.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/port_fase4_doc19_51.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/port_fase4_doc19_part2.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/port_fase4_doc19_part3.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/port_fase4_spec.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/port_fase5_annexes.py` | AST parse clean |
| OK | `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/scripts/port_fase5_doc18.py` | AST parse clean |
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
| OK | `dashboard smoke --no-shots` | all passed | 13852 |

## AGENTS.md triage

| Path | Lines | Version | Hash | Changed since last audit |
|---|---|---|---|---|
| `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/AGENTS.md` | 231 | 4.6 | `0c207cd17056a8c0` | no |
| `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/00_METHODOLOGY/AGENTS.md` | 143 | 2.1 | `22ae3791d2bcf87a` | no |
| `/home/epmq-cyber/.zcode/AGENTS.md` | 53 |  | `ea97049744d41fd5` | no |

## Proposed patches (P7 — nunca auto-aplicados)

_Cada item DEAD/CRITICAL recebe proposta. Cada item WEAK/ALERTS recebe alvo de gatilho ou documentação. Cada decisão é humana._

### WEAK (<3 usos/semana)
- `cmd:/doc-check` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 2/7d, 2/14d.
- `skill:case-context-loader` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 2/7d, 2/14d.
- `skill:doc-conventions` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 1/7d, 1/14d.
- `repo-skill:case-context-loader` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 2/7d, 2/14d.
- `repo-skill:doc-conventions` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 1/7d, 1/14d.
- `script:port_fase4_doc19_51.py` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 2/7d, 2/14d.
- `script:port_fase4_doc19_part2.py` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 2/7d, 2/14d.
- `script:port_fase4_doc19_part3.py` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 2/7d, 2/14d.
- `script:port_fase4_spec.py` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 2/7d, 2/14d.
- `script:port_fase5_annexes.py` — refinar descrição / adicionar frase padrão ao AGENTS.md, ou remover dos mandatos. Uso: 1/7d, 1/14d.
### ALERTS (eixo QUALIDADE)
- `mcp:skillnet` — ALERTS (ok 75.0%, 2 err, 0 retried) — acompanhar; vira CRITICAL se não melhorar.
