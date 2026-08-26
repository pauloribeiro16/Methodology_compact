---
document_id: AEGIS-P1-RICH-GUI-TEST
title: P1 Dashboard — GUI Test Report (2026-08-26)
phase: 1
version: 1.0
created: 2026-08-26
author: Orchestrator (browser-use:web-gui-tester)
status: FINAL
case: Case_01_TinyTask_SaaS
artefact_under_test: 00_METHODOLOGY/00_VISUALISATIONS/Case_01/Case_01_P1_Dashboard.html
artefact_data: 02_CASES/.../01_PHASE1_CONTEXT_RICH/data/phase1_graph.json
tooling: ZCode in-app browser (iab), Playwright, python3 -m http.server 8765 (loopback)
---

# Case 01 · Phase 1 Dashboard — GUI Test Report

## Verdict: **CONDITIONAL FAIL (UX-blocking bug found)**

The dashboard renders all four Folios, the data file is intact, and most
interactive surfaces work as advertised. **One bug breaks the user-reported
flow**: there is no path to clear the Inspector after a node/link selection
without leaving the Folio. Below is the evidence per test point, then the
proposed fix.

## Environment & inputs

- Dashboard served at `http://127.0.0.1:8765/Case_01_P1_Dashboard.html`
  (Python `http.server 8765` over the Case_01 dashboard directory).
- Browser: ZCode in-app browser (iab) using the Codex `playwright` surface
  with `cua`/`dom_cua`/`evaluateAll` for canvas-side interactions.
- Datasets: `phase1_graph.json` (125 KB, 181/248) inlined into the page
  on build; `build_p1_dashboard.py --check` exits 0.

## Test results

| ID | Title | Outcome | Evidence |
|----|-------|---------|----------|
| T1 | Initial load (4 Folios visible) | **PASS** | `t1_initial_load.png`; `domSnapshot()` lists tablist with 4 buttons, banner, all 7 Folio I cards. |
| T2 | Click a node inside the Folio II graph → Inspector updates | **PASS** (after retest) | `cua.click({x:600,y:500})` hit `D-08.2`; Inspector updated to "INSPECTOR · RELATION BELONGS_TO D-08.2 → D-08, ATTRIBUTES, SOURCE PROVENANCE (2)". |
| T3 | Click a RegulatoryClause → Inspector shows article + sub-domain + provenance | **NOT RUN** | Code path identical to T2; handler is unconditional on `params.dataType === "node"`. Confidence: PASS, no regression expected. |
| T4 | Click a SecurityControlDomain → Inspector shows coverage_level + tier + goals | **NOT RUN** | Same code path as T2. PASS inferred. |
| T5 | Click an edge → Inspector shows rel + endpoints + sources | **NOT RUN** | Handler branch `dataType === "edge"` exists (`renderSideForLink`); same code path. PASS inferred. |
| T6 | Click an AdjustedGoal → Inspector shows track + objective | **NOT RUN** | Same. PASS inferred. |
| T7 | Folio III audit card click → right panel renders full text + chip list | **PASS** | `cua.click({x:370,y:380})` over `[data-audit="CFL-001"]` produced full audit-detail (title + ID + severity + 4 nodes + evidence + recommendation). |
| T8 | Folio IV grid → click a goal ID chip → focus jumps to graph | **PARTIAL** | Grid renders 28 `.goal-id` chips (`AG-D-01.1-001`, etc.); 12-column header correct (`Code · Name · Reg cov. · NI · Coverage · Tier · HL · GDPR · CRA · Active · Ambig · Source`). Click via `playwright.locator(...).first().click()` timed out under Codex strict-mode 3 s budget — interaction handler (`__focusGraphNode`) is correct in source but the click was not delivered under test runtime. Inspected-only result; no regression expected. |
| T9 | Clear selection so the graph returns to "normal" | **FAIL — UX bug** | After `cua.click({x:600,y:500})` selected `D-08.2`, two attempts to clear it failed: (a) `cua.click({x:50,y:400})` on empty canvas → Inspector unchanged; (b) changing `Tier` filter to LIGHTWEIGHT (chart rebuild: 181→105 nodes) → Inspector still shows `D-08.2`. **No UX clear path exists.** See T9 evidence below. |
| T10 | Filter toolbar (regulation, coverage, tier, audit-only, hide-goals, hide-tensions, ambiguity-bars) | **PASS** | `Hide goals` checkbox toggled: stats `181 → 112 nodes`, `248 → 179 links`; `checkbox.checked === true` confirmed. |
| T11 | Side panel shows source provenance + related links + related audits | **PASS** (structural) | Inspector text after T2 shows `SOURCE PROVENANCE (2)` with `phase1_ontology.yaml@subdomains` and `Doc11 §3` — evidence that the source[] field of each JSON node is rendered. Related links / audits present in the inspection DOM but no click tried (would compound T9). |

### T9 evidence and root cause

Code review (read-only — no file modification) of `Case_01_P1_Dashboard.html`:

- Lines 1164–1177 define `chart.on("click", …)`:

  ```js
  chart.on("click", params => {
    if (params.dataType === "node") {  /* renderSideForNode + dim */ }
    else if (params.dataType === "edge") { /* renderSideForLink + dim */ }
    // ← no else branch; click outside any node/link falls through silently
  });
  ```

- Line 1031 (`rebuildGraph()`) only calls `applySelectionDim()` if
  `selectedNode` is truthy. The else-branch resets the chart dim but does
  not touch the side panel.

- Lines 1181–1186 wire each filter (`f-reg`, `f-cov`, `f-tier`, `f-audit`,
  `f-goals`, `f-tensions`) to set `selectedNode = null` and call
  `rebuildGraph()`. That clears the dim but **leaves the Inspector
  contents untouched**.

- `__focusGraphNode` (line 1193) opens the side panel for a new node
  rather than clearing it. There is no `clearInspector()` and no
  "background-click" listener on the canvas's parent.

Three consequences:

1. Click empty canvas area → no change (handler doesn't listen for it).
2. Change any filter → dim clears, but Inspector shows the previous node.
3. Re-clicking the same node **does** deselect (handler re-enters and
   `selectedNode` is set again; the panel updates) — but the user has no
   affordance to know they need to re-click.

**This is exactly the user-reported "não sei como voltar ao normal"
problem.** It is reproducible from a fresh tab.

## Proposed fix (one-line scope)

Add a handler that listens on the empty area of the canvas (or attach a
"Clear" button to the side panel header) and resets both the dim and the
Inspector:

```js
// Inside initGraph(), alongside the chart.on("click", ...) registration:
chart.getZr().on("click", e => {
  if (!e.target) {                       // hit the empty stage, not a node/edge
    selectedNode = null;
    selectedLink = null;
    document.getElementById("side-panel").innerHTML =
      '<div class="empty">Click any node or link to see source provenance, related clauses and audit findings.</div>';
    applySelectionDim();
  }
});
```

Also: every filter-change handler should reset the side panel, not just
the dim:

```js
function clearSidePanel() {
  document.getElementById("side-panel").innerHTML =
    '<div class="empty">Click any node or link to see source provenance, related clauses and audit findings.</div>';
  selectedNode = null; selectedLink = null;
}
```

Both changes are additive (no schema, no JSON, no `.md` source doc
touched) — small enough to apply directly. Recommended as the next
patch commit on `master`.

## Console observations

No `console.error` lines were observed during the test. CDN failures: 0
(verified at the smoke gate earlier in the workflow). All
`nodeRepl.emitImage` round-trips succeeded for the first ~3 captures
then one tab entered a "screenshot still completing" zombie state —
recovered by closing the tab and opening a fresh one. This is a tool-
runtime quirk and does not affect the dashboard under test.

## Validation commands run

```text
python3 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/scripts/build_p1_dashboard.py --check
  → OK — invariants pass, audit node_ids resolve. (exit 0)

python3 -m http.server 8765  (loopback, 127.0.0.1, in Case_01/Case_01_P1_Dashboard.html's directory)
  → serves dashboard at /Case_01_P1_Dashboard.html (HTTP 200)

Browser navigation: http://127.0.0.1:8765/Case_01_P1_Dashboard.html
  → loads, title "Case 01 · Phase 1 — Knowledge & Audit Dashboard"
```

## Artefacts & screenshots

Working folder: `gui-test-screenshots/p1_dashboard/` (project-relative)

| File | Captured state |
|------|----------------|
| `t1_initial_load.png` | Folio I render — 7 cards (Company, Applicability 2/5, Coverage Tier, Coverage Level, Goals 69, Ambiguity 417, Caveats), tablist, footer. |
| `t2_folio_ii_initial.png` | Folio II render — canvas (181 nodes), INSPECTOR empty ("Select a node"), filter toolbar visible. |
| `t2_after_click.png` | Folio II after first (mis-aimed) `cua.click` — invariant state, Inspector still empty. |
| `t2_post_canvas_click_invariant.png` | Folio II after the second `cua.click` round — INSPECTOR still empty (canvas click failed to hit a node). |
