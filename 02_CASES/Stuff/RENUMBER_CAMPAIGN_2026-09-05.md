---
document_id: AEGIS-CAMPAIGN-RENUMBER
title: Renumber Campaign — Flat 1..N Lane Ids, Zero Legacy (3 Cases)
phase: 3
version: 1.1
created: 2026-09-05
updated: 2026-09-05
author: Orchestrator
status: EXECUTED
---

# RENUMBER Campaign — "flat 1..N per lane, zero legacy"

> **STATUS: EXECUTED 2026-09-05** — F0 `bbe7a02` · F1 `18f326c` · F2 `3545c19` ·
> F3 `13945cf` · F4 bookkeeping. Reports: `RENUMBER_2026-09-05_REPORT_F{1,2,3}.md`.
> Registry: `00_METHODOLOGY/validation/RENUMBER_REGISTRY_2026-09-05.md`.

Human request 2026-09-05: after the UC→PROC/CAP re-lanes the ids grew large and
gapped (C3 UCs jump 34→63, PROC 39/40 retired, C1/C2 still use the legacy dotted
`U.C.x.y.z`). Decision: **renumber every lane flat 1..N per case** — no gaps, no
retired numbers, no legacy schemes. Codified in rubric v1.10 §5B rule 7 (supersedes
the "retired numbers are NOT reused" clause).

## Locked decisions (human, 2026-09-05 — FINAL)

1. Flat 1..N per lane per case (UC-01..NN, PROC-01..NN, CAP-01..NN).
2. Dotted `U.C.x.y.z` flattened to `UC-NN` in C1 and C2.
3. Order: compliance-lane UCs first (ascending), then product UCs (ascending
   natural). Consequence: C1 compliance → UC-01..17, product → UC-18..40;
   C3 PKG-DS UC-33/34 → UC-01/02.
4. Historical "formerly" provenance keeps the ids it named; all LIVE references
   move to the new ids. Old→new registry is the traceability record.

## Exact mappings (C3) / rules (C1, C2)

- C3 UC (33): UC-33→01, UC-34→02, UC-63→03, then UC-64→04 … UC-93→33 (one line each).
- C3 PROC (12): PROC-41→39, 42→40, 43→41 … 52→50. PROC-01..38 and CAP-01..10 untouched.
- C1 UC (40): U.C.1..6 (17 compliance) → UC-01..17; U.C.7..11 (23 product) → UC-18..40.
  C1 PROC-01..17 + CAP-01 untouched.
- C2 UC (36): 15 compliance → UC-01..15; U.C.8..12 (21 product) → UC-16..36.
  C2 PROC-01..27 + CAP-01..10 untouched.
- Registry: `00_METHODOLOGY/validation/RENUMBER_REGISTRY_2026-09-05.md` (per-case
  old→new tables, built by census before any rename).

## Phases

- **F0** — rubric v1.10 + this plan + ledger entry. DONE (this commit).
- **F1** — Case_03: two-phase rename (word-boundary) across the case subtree; annex A
  8 PlantUML sources updated → SVGs re-rendered (plantuml.com); annex B 33 headings +
  Doc22 pointers 1:1 (preserve `\n` after fence); Doc22 metadata/metrics/Lane sections;
  Doc32 articulation re-anchored. Gates: verify_rich, check_unmapped, posture,
  traceability_audit 100/100/100, mermaid render 192/192, smoke 16/16.
- **F2** — Case_01: flatten U.C.x.y.z → UC-01..40; Doc20/21+…, Doc32, annexes A
  (11 PlantUML → SVGs) + B (23); gates.
- **F3** — Case_02: flatten → UC-01..36; Doc21/Doc31, annexes A (7 PlantUML → SVGs)
  + B (21); gates.
- **F4** — Bookkeeping: CHANGE_LOG 1.8, GLOBAL v8.1, ledger, PROJECT_STATEs ×3, memory.

## Invariants

- Zero content loss — only ids change; provenance chains keep historical ids.
- Two-phase rename mandatory (UC-93→UC-33 while old UC-33 still exists).
- 0 live old-id references at the end (registry + provenance excepted).
- `validation/build_control_set.py` (uncommitted human work) untouched; `progress.json`
  immutable; KG build E3 frozen (kg.sh won't resolve new ids — documented limitation).
- Every rewritten mermaid block passes the real-render check (`/tmp/mermaid_check.py`);
  SVGs visually spot-checked.
- Commits: `[EXECUTOR] F0..F4 RENUMBER ...`; reports `02_CASES/RENUMBER_2026-09-05_REPORT_F<N>.md`.
