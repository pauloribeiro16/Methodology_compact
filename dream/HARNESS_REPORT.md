# Harness Audit — Methodology_compact

_Generated 2026-08-27 by `scripts/dream/harness_audit.py` — auto-discovers the registry (hooks, MCP, subagents, commands, skills, scripts). Source for usage: `~/.zcode/cli/db/db.sqlite` (transcripts in `rollout/` are pruned to ~24h, the db is the historical truth). Static + live health probes below._

## Registry

| Name | Category | 7d | 14d | Verdict | Notes |
|---|---|---:|---:|---|---|
| `hook:SessionStart:brief_hook.sh` | hook | 9 | 9 | **INSUFFICIENT-DATA** |  |
| `hook:SessionStart:case_context_hook.sh` | hook | 5 | 5 | **INSUFFICIENT-DATA** |  |
| `hook:UserPromptSubmit:kg-reminder.sh` | hook | 27 | 27 | **INSUFFICIENT-DATA** |  |
| `hook:PreToolUse:guard-protected-files.sh` | hook | 4 | 4 | **INSUFFICIENT-DATA** |  |
| `hook:PreToolUse:guard-bash.sh` | hook | 8 | 8 | **INSUFFICIENT-DATA** |  |
| `mcp:skillnet` | mcp | 0 | 0 | **DEAD** |  |
| `agent:web-frontend` | subagent | 4 | 4 | **HEALTHY** |  |
| `cmd:/case` | command | 164 | 205 | **HEALTHY** |  |
| `cmd:/doc-check` | command | 2 | 2 | **DEAD** |  |
| `cmd:/dream` | command | 90 | 90 | **HEALTHY** |  |
| `cmd:/harness-audit` | command | 10 | 10 | **INSUFFICIENT-DATA** |  |
| `skill:case-context-loader` | skill | 2 | 2 | **DEAD** |  |
| `skill:doc-conventions` | skill | 0 | 0 | **DEAD** |  |
| `repo-skill:case-context-loader` | repo-skill | 2 | 2 | **INSUFFICIENT-DATA** |  |
| `repo-skill:doc-conventions` | repo-skill | 0 | 0 | **INSUFFICIENT-DATA** |  |
| `script:install_skills.sh` | script | 5 | 5 | **INSUFFICIENT-DATA** |  |
| `script:kg.sh` | script | 193 | 199 | **INSUFFICIENT-DATA** |  |
| `script:rename_case_files.py` | script | 7 | 7 | **INSUFFICIENT-DATA** |  |
| `dream:adoption_audit.py` | dream-script | 15 | 15 | **INSUFFICIENT-DATA** |  |
| `dream:harness_audit.py` | dream-script | 10 | 10 | **INSUFFICIENT-DATA** |  |
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
| OK | `kg.sh audit` | # graph: /home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/kg/E3_2026-08-23/graphify-out/graph.json | 71 |
| OK | `skillnet MCP handshake` | 2 tools | 159 |
| OK | `dashboard smoke --no-shots` | all passed | 11492 |

## AGENTS.md triage

| Path | Lines | Version | Hash | Changed since last audit |
|---|---|---|---|---|
| `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/AGENTS.md` | 231 | 4.6 | `0c207cd17056a8c0` | no |
| `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/00_METHODOLOGY/AGENTS.md` | 143 | 2.1 | `22ae3791d2bcf87a` | no |
| `/home/epmq-cyber/.zcode/AGENTS.md` | 53 |  | `ea97049744d41fd5` | no |

## Proposed patches (P7 — never auto-applied)

_Each DEAD item without a plan gets a wiring-or-removal proposal. Each WEAK item gets a triggers/documentation proposal._

### DEAD items (0 uses in 2 consecutive audits)
- `mcp:skillnet` — decide: wire into pre-flight, improve triggers, or remove. Current usage: 0 over 14d.
- `cmd:/doc-check` — decide: wire into pre-flight, improve triggers, or remove. Current usage: 2 over 14d.
- `skill:case-context-loader` — decide: wire into pre-flight, improve triggers, or remove. Current usage: 2 over 14d.
- `skill:doc-conventions` — decide: wire into pre-flight, improve triggers, or remove. Current usage: 0 over 14d.
