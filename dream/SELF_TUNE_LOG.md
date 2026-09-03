# SELF_TUNE_LOG — Dream self-tuning history

> **Append-only ledger** of every auto-edit the Dream nightly applies to its
> own infrastructure (`scripts/dream/*`, `.zcode/hooks/*`, `dream/*`).
>
> **Rules (P7 non-negotiable)**:
> - The Dream MAY auto-edit the files above.
> - The Dream MUST NEVER touch: `AGENTS.md`, `00_METHODOLOGY/AGENTS.md`,
>   `02_CASES/*/PROJECT_STATE.md`, `02_CASES/GLOBAL_PROJECT_STATE.md`,
>   `02_CASES/*/progress.json`, `00_METHODOLOGY/dependency_graph.yaml`,
>   `00_METHODOLOGY/PREPROCESSING_by_domain/domains/**`.
> - Every auto-edit MUST pass validation
>   (`scripts/dream/self_tune.py validate <file>`) before commit.
> - Every commit MUST use the prefix `[DREAM SELF-TUNE]`.
>
> **Format**: one line per self-tune, most recent first. Fields:
> `- YYYY-MM-DD | <scope> | <action> | <reason>`

- _empty — first self-tune will be logged here on next nightly cycle_
