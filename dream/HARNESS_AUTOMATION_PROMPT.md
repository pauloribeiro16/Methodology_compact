You are the weekly Harness Audit job for the Methodology_compact repo at
/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact.

GOAL (auto-discovers the registry, deterministic + LLM analysis of
verdicts, propose-only — stricter than v1):

1. cd /home/epmq-cyber/Área\ de\ Trabalho/projects/Methodology_compact
2. Run the deterministic pipeline:
     python3 scripts/dream/harness_audit.py
3. Read the generated dream/HARNESS_REPORT.md. The report is the source
   of truth for the registry (22 items: hooks, MCP, subagents, commands,
   skills, scripts, dream-pipeline). Two independent axes per item:
     - Eixo USO: HEALTHY (≥3 uses/wk), WEAK (<3), DEAD (0 uses for 2
       consecutive weeks), INSUFFICIENT-DATA (no db signal AND <1 day old).
     - Eixo QUALIDADE: OK · ALERTS · CRITICAL · N/A — derived from
       `db.tool_usage` (success%, retries, p50 ms) per the item's
       primary tool_name (MCP for `mcp:*`, Agent for subagents, Skill for
       skills; commands/scripts/hooks stay N/A at per-item granularity
       and defer to the global "Saúde operacional" table).
4. Read the new "Saúde operacional" table and the "Eficácia do pipeline
   dream" table. Surface anything that flips to CRITICAL or that
   represents a meaningful regression since the previous report (compare
   against `git log --format=%s -n 1 -- dream/HARNESS_REPORT.md` and
   re-read the predecessor via `git show HEAD~1:dream/HARNESS_REPORT.md`
   if available).
5. For each DEAD item, write ONE specific reason (not "wire into pre-
   flight" boilerplate) based on what the report's numbers + the
   item's SKILL.md / .md frontmatter actually say. For each WEAK item,
   surface the proposed patch from the report. Do NOT invent new
   implementations.
6. Check dream/HARNESS_REPORT.md 'Health (live)' table:
     - kg.sh audit OK
     - skillnet MCP handshake OK
     - dashboard smoke --no-shots OK
   If any is FAIL or WARN, call it out (the static check inside
   harness_audit.py may already be WARN; do not panic — just report).
7. Commit dream/HARNESS_REPORT.md with message:
     [HARNESS YYYY-MM-DD] weekly audit (N healthy, M weak, K dead,
                                  D live-probe-failures, E cri)
   where the E cri counter is items at QUALIDADE=CRITICAL this cycle.
8. One-line summary at the end: which items flipped verdicts since last
   week, what needs human attention, and any operational anomalies (e.g.
   a previously 99% tool dipping to <80%).

P7 (NON-NEGOTIABLE):
- Never edit AGENTS.md, 00_METHODOLOGY/AGENTS.md, PROJECT_STATE.md,
  GLOBAL_PROJECT_STATE.md, progress.json, dependency_graph.yaml, or any
  state file.
- Never edit the memory store at ~/.zcode/cli/memories/projects/
  methodology_compact-1839a9d8746b19ef/memory/ directly.
- Never modify ~/.zcode/cli/db/db.sqlite (read-only by file:// mode).
- Outputs are committed reports and P7-proposed patches in the same
  report file. The human applies the patches.

NOTE: this automation runs Sunday 23:00 (created by `CronCreate`).
dream/STATE/ is gitignored, so only HARNESS_REPORT.md is committed.
You may see dream/ADOPTION_REPORT.md and dream/RECONCILIATION.md
present — do not touch them.
