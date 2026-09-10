---
document_id: AEGIS-CAMPAIGN-UC-SEPARATION
title: UC Separation Campaign — Use-Case Catalogs Hold Use Cases Only
phase: 3
version: 1.1
created: 2026-09-05
updated: 2026-09-05
author: Orchestrator
status: EXECUTED
---

# UC SEPARATION Campaign — "use-case catalogs hold use cases only"

> **STATUS: EXECUTED 2026-09-05** — F0 `c266074` · F1 `32f45f7` · F2 `47ad056` · F3 `d498347` · F4 bookkeeping. Phase reports: `UC_SEPARATION_2026-09-05_REPORT_F{1,2,3}.md`. 6 borderline UC titles escalated to the P7 queue (ledger §5).

Human diagnosis 2026-09-05: Case_03 `Doc22_Use_Cases_Catalog.md` mixes packages,
UC, CAP and PROC in the same sections; most remaining §6 "UC" cards are
control-register entries, not use cases (e.g. UC-58 "Audit Manager Maintains
Immutable Audit Logs", UC-57 "SOC Manager Deploys AI-Powered Threat Detection").
Exploration confirmed: 93 cards in two disjoint populations — 62 summary compliance
cards (17 UC + 38 PROC + 7 CAP) interleaved inside PKG-D-01..10, and 31
fully-dressed product cards in PKG-A..F — plus stale self-claimed stats ("62 UCs /
10 packages" vs actual 93 cards / 16 packages) and a heading-grammar split
(`## ` summary vs `#### Use-Case: {}` fully-dressed).

## Locked decisions (human, 2026-09-05 — FINAL)

1. The 15 non-genuine §6 `UC-*` cards → re-lane to `PROC-*`/`CAP-*` (zero content
   invention; full cards authored in Doc32 per §5C schemas).
2. Doc22 (and case use-case catalogs generally) = use cases only; PROC/CAP cards
   live exclusively in `DocNN_Process_Capability_Cards.md`.
3. Scope: all 3 cases (C1 Doc20, C2 Doc21, C3 Doc22).
4. `PROC-39`/`PROC-40` re-adjudicated back to `UC-66`/`UC-92` (genuine actor→system
   form; recovers the skipped numbers). Numbers 39/40 retired; Case_03 PROC
   numbering continues at 41. Codified in rubric v1.8 §5B rule 6.
5. `UC-33`/`UC-34` stay UC → dedicated **PKG-DS (Privacy & Data-subject UCs)**,
   elevated to fully-dressed RUP form (Bike4All template).
6. `UC-08`/`UC-26`/`UC-58` → `CAP-08..10` (C2M2/ArchiMate); the other 12 →
   `PROC-41..52` (SSDF).

## Classification rule (frozen)

- **UC**: an actor operates the platform via UI/API; event-driven interaction with
  an observable system response.
- **CAP**: persistent/continuous behaviour of the system or the organization.
- **PROC**: a role's operational activity (trigger → activities → outcome).

Validator applies the rule per card; more than 2 surprises per case → stop and
escalate to the human (P7).

## ID map (Case_03 §6)

UC-02→PROC-41 · UC-03→PROC-42 · UC-06→PROC-43 · UC-15→PROC-44 · UC-17→PROC-45 ·
UC-21→PROC-46 · UC-22→PROC-47 · UC-44→PROC-48 · UC-46→PROC-49 · UC-47→PROC-50 ·
UC-57→PROC-51 · UC-61→PROC-52 · UC-08→CAP-08 · UC-26→CAP-09 · UC-58→CAP-10 ·
PROC-39→UC-66 · PROC-40→UC-92. UC-33/34 keep UC (PKG-DS).

## Phases

- **F0** — rubric v1.8 (§5B rule 6 lane-pure catalogs; §5C.5 UC-ovals-only) + this
  plan + ledger entry. DONE (this commit).
- **F1** — Case_03: re-lane the 15 IDs (word-boundary script + grep census);
  PROC-39/40 → UC-66/92 (incl. UC-63 alt-flow 5.1); Doc22 v3.0 (§6 replaced by a
  compliance index D-01..D-10 → Doc32; TOC renumbered; metadata/metrics corrected to
  33 UCs / 7 packages; frontmatter outputs fixed; top pointer to Annex A/B); PKG-DS
  section with UC-33/34 fully-dressed; Doc32 +15 full cards (12 PROC SSDF + 3 CAP
  C2M2) with §5C.4 flowcharts, −2 PROC-39/40 companions; annex A 7→8 diagrams (UC
  ovals only; PKG-DS added; system-wide extended); annex B 31→33 sequences (UC-33/34;
  empty B.1 placeholder removed). Gates + traceability audit + dashboard smoke.
- **F2** — Case_01: remove 18 stubs (17 PROC + 1 CAP) from Doc20 (full cards already
  in C1 Doc32); TOC/metrics corrected (23 UCs); annex A (12 diagrams) non-UC ovals
  cleanup; audit the 23 `U.C.x.y.z` titles against the classification rule. Gates.
- **F3** — Case_02: remove 5 PROC stubs from Doc21 (Doc31 already holds 27 PROC +
  10 CAP full cards); TOC/metrics corrected (21 UCs); annex A (6 diagrams) cleanup;
  audit the 21 titles. Gates.
- **F4** — Bookkeeping: CHANGE_LOG_CENTRAL, GLOBAL_PROJECT_STATE, PROJECT_STATE +
  progress.json ×3 cases, memory; ledger → EXECUTED.

## Expected end-state counts

- C3: Doc22 = 33 UCs (31 product + 2 PKG-DS), 0 non-UC cards; Doc32 = 50 PROC +
  10 CAP + 60 mermaid diagrams; annex A = 8 useCaseDiagrams (UC ovals only);
  annex B = 33 sequenceDiagrams.
- C1: Doc20 = 23 UCs, 0 PROC/CAP headings. C2: Doc21 = 21 UCs, 0 PROC headings.
- All case gates PASS; `traceability_audit.py` 100/100/100; dashboard smoke 9/9.

## Constraints

- `validation/build_control_set.py` carries uncommitted human work (v1.1
  `realization_class` parsing) — untouched, unreverted, uncommitted by this campaign.
- `kg/E3_2026-08-23/graphify-out/graph.json` frozen — no KG rebuild; `kg.sh` queries
  keep operating on build E3 (documented limitation, as in prior campaigns).
- One Executor at a time; Orchestrator verifies gates/diff/counts between phases.
- Phase reports: `02_CASES/UC_SEPARATION_2026-09-05_REPORT_F<N>.md`.
- Commits: `[EXECUTOR] F0..F4 UC separation ...`, one per phase.
