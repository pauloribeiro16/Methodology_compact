---
name: case-context-loader
description: "Use when starting any work on an AEGIS case study (Case_01/02/03) in the Methodology_compact repo. Loads the status chain GLOBAL_PROJECT_STATE → case PROJECT_STATE + progress.json → phase PROJECT_STATE and returns the current state of the case. Trigger phrases: start working on a case, what is the state of case X, continue case work, load case context."
---

# Case Context Loader

Loads the current status of an AEGIS case study before any work starts. This is
step 1 of the pre-flight checklist in the repo root `AGENTS.md`.

## When to Activate

- Starting or resuming work on any case (Case_01_TinyTask_SaaS, Case_02_SecureBorder_Solutions, Case_03_OmniBank_Financial)
- User asks "what is the state of case X" / "where was I"
- Before editing any case artefact (phases 1–3)

## Usage

From the repo root (or anywhere — the script resolves the repo by its own location):

```bash
skills/case-context-loader/scripts/load_case_context.sh            # all 3 cases, brief
skills/case-context-loader/scripts/load_case_context.sh Case_01     # one case, full chain
skills/case-context-loader/scripts/load_case_context.sh 03          # selector by number works too
```

The script prints, in order:

1. `02_CASES/GLOBAL_PROJECT_STATE.md` header (cross-case state, version)
2. The case's `PROJECT_STATE.md` header (phase status, gates, last update)
3. The case's `progress.json` phase summary (status / gate / completed_at per phase, active contracts)
4. Each phase folder's own `PROJECT_STATE.md` header (00_COMMON → 01_ → 02_ → 03_)

## Reading Order (manual fallback)

If the script is unavailable, read the chain manually:

1. `02_CASES/GLOBAL_PROJECT_STATE.md` — cross-case state
2. `02_CASES/Case_0X/PROJECT_STATE.md` + `02_CASES/Case_0X/progress.json`
3. `02_CASES/Case_0X/0N_PHASE*/PROJECT_STATE.md` for the phase being worked on

## Notes

- `progress.json` is a structured snapshot — **never edit it by hand** (boundary rule in `00_METHODOLOGY/AGENTS.md`).
- `GLOBAL_PROJECT_STATE.md` and `02_CASES/README.md` still contain references to the main-repo structure (they predate the compact extraction) — read with filter.
- Naming inconsistency: Case_01 uses `03_PHASE3_DECOMPOSITION_RICH/`; Cases 02/03 use `03_PHASE3_DECOMPOSITION/`.
