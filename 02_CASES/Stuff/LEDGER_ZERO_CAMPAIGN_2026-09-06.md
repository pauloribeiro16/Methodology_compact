---
document_id: AEGIS-CAMPAIGN-LEDGER-ZERO
title: Ledger Zero Campaign — Phased Closure of All Open Items
phase: Cross-phase
version: 1.0
created: 2026-09-06
updated: 2026-09-06
author: Orchestrator
status: ACTIVE
---

# LEDGER-ZERO Campaign — phased closure of everything open

Human request 2026-09-06: "resolver isso tudo de forma faseada". This campaign closes
every open item in `02_CASES/PENDING_CAMPAIGNS_LEDGER.md`. Orchestration: one Executor
at a time, Orchestrator verifies gates/diff/counts between phases.

## P7 decisions locked (human, 2026-09-06 — FINAL)

1. **6 borderline UC titles → re-lane** per the frozen classification rule:
   C1 UC-07/UC-12/UC-13/UC-16 → PROC-18..21; C2 UC-30/UC-36 → CAP-11..12.
2. **OBL-D-06.2-001 (C3) → Option A**: document `BPR-D-02.2-001` as the deliberate
   cross-domain PS.3/SBOM anchor (dual-duty) in Doc19/Doc20 — no new rule.
3. **D-07.2 (C1) → Option B**: formally accept the `BPR-D-07.2-001` mitigation —
   withdraw the N/A marker, mark Doc23/Doc27 nodes "BPR-anchored closure", update
   Doc14 + PROJECT_STATE audit row. No new rules.
4. **phase2_ontology.yaml unfrozen**: apply the `RealizationClass` enum + attributes
   in all 3 cases and regenerate the P2 mirrors/dashboards (closes the 2026-09-05
   documents-only freeze).
5. **MUC-C3-06**: decision gate inside F2 — default is to ratify the definition and
   mitigation already recorded in Doc22 §6B.7 as canonical (P7 note resolved).

## Phases (dependency-ordered)

- **F0** — ledger §1D + this plan + decision record. DONE (this commit).
- **F1** — verify_rich C2+C3 → 8/8 PASS: C2 CHK-4 (dangling BPR-D-02.2-001 /
  BPR-D-10.2-002) + CHK-6 (FR-76/82 malformed Source Rule) + F5-C2-03 duplicates if
  alive; C3 CHK-3 (NFR census 12 cards vs claim 56 — adjudicate with git history;
  if genuine truncation, ESCALATE before authoring content) + CHK-6 (NFR-06/07/09
  Source Rules) + F5-C3-01 (stale "63 rules") + F5-C3-03 (BPR-D-12.1-001 missing in
  Doc26) + F5-C3-04 (dangling UC-99 → current id). Audit 100/100/100 maintained.
- **F2** — P7 ratifications (paperwork): OBL Option A edits; D-07.2 Option B edits;
  MUC-C3-06 ratification; consolidated phantom-refs formal note (F-01/F-03 lineage
  intentional) in RULE_FREEZE + ledger.
- **F3** — re-lane the 6 borderline ids (two-phase rename, registry append, full lane
  cards in Doc32/Doc31 per §5C.1/§5C.2, SVGs re-rendered, annexes re-anchored, gates).
- **F4** — CAP maturity → EvidenceItems: scale=capability EvidenceItems for the 21 CAP
  cards (C1 1 · C2 11 · C3 10), sources[] from existing corpus nodes only, no invented
  maturity values; P1 ontology v1.6→v1.7 ×3 + Folio VIII refresh ×3 (smoke + visual).
- **F5** — Case_02 handoff remainder: Folio I title-case strings, stale re-inline
  Maturity.html, final screenshots (Playwright).
- **F6** — P1 dashboard C1: 4 KG-vs-view drifts (regenerate view from canonical E3)
  + 2 cosmetic items; smoke + visual check.
- **F7** — P2: phase2_ontology.yaml ×3 (enum + attrs) + regenerate phase2_graph.json /
  phase2_ontology.compact.json + P2 dashboards refresh; smoke + validator.
- **F8** — KG rebuild E4 per kg/GRAPHIFY.md protocol (reflects realization_class +
  flat lane ids + new artefacts). If the graphifyy/Deucalion pipeline is unavailable
  in-session: prepare inputs + instruction, E3 stays canonical (ledger note).
- **F9** — close-out: ledger → zero open items (everything EXECUTED or P7-ratified
  with date), CHANGE_LOG, GLOBAL, PROJECT_STATEs ×3, memory, final campaign report.

## Invariants (all phases)

- One Executor at a time; Orchestrator verification between phases.
- `validation/build_control_set.py` (uncommitted human work) untouched; `progress.json`
  immutable; KG E3 frozen until F8.
- Two-phase renames; real-render check for every new/edited mermaid; zero content
  invention without escalation.
- Phase reports: `02_CASES/LEDGER_ZERO_2026-09-06_REPORT_F<N>.md`.
- Commits: `[EXECUTOR] F<N> ledger-zero ...` (~10).
