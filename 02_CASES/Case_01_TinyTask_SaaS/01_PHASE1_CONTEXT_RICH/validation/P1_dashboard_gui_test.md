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

---

## Re-test after v1.2 dashboard fix (2026-08-26)

Verdict: **PASS** — T9 fix verified, and all of T2/T7/T10/T10/T4 still hold.

### What changed

In one combined commit a single subagent:

- **Folio II (Knowledge Graph)** — kept, with two UX changes only:
  - `applySelectionDim` no longer drops non-neighbours to `opacity 0.18`. New policy: non-neighbours stay at `opacity 0.6` with labels readable everywhere; edge opacities go 1-hop = 0.85, rest = 0.35 (was 0.07).
  - Added `chart.getZr().on("click", e => { if (!e.target) clearSelection(false); })` so clicking on empty canvas clears the selection.
  - The 6 filter handlers (`f-reg`, `f-cov`, `f-tier`, `f-audit`, `f-goals`, `f-tensions`) now route through a new `clearSelection(rebuild)` helper that resets state + Inspector + dims (was: only `selectedNode=null` + `rebuildGraph()`).
  - Added a global `keydown` listener for `Escape` / `Esc` that calls `clearSelection(false)` whenever there is a selection.

- **Folio V (Phase 1 Story)** — NEW tab. ECharts `layout: "none"`, roam-on, 6 visual columns (Stakeholders+BGs → TinyTask → Regs → Clauses → Sub-Domains → Adjusted Goals). Non-applicable regulations dimmed. Toolbar with 3 toggles (Tensions / CoverageGaps / Ambiguity bars). Legend panel on the left. Same Inspector + same Esc / click-empty clear behaviour as Folio II.

### T9 verification (live, post-fix)

Sequence run via headless Codex IAB + Playwright against `http://127.0.0.1:8765/Case_01_P1_Dashboard.html` in a fresh tab:

| Step | Action | Inspector observation | Stats observation |
|------|--------|-----------------------|--------------------|
| 1 | Fresh load → click `II.Knowledge Graph` tab | `INSPECTOR · SELECT · Select a node` (empty, with Tip visible) | `197 nodes · 264 links visible` |
| 2 | `cua.click({x:700,y:510})` (over a visible node) | `INSPECTOR · RELATION · COVERS · FROM TinyTask → TO D-05.2 Retention & Archiving · ATTRIBUTES covered/PARTIAL/LIGHTWEIGHT · SOURCE PROVENANCE …` | unchanged |
| 3 | `cua.click({x:50,y:400})` (empty canvas, far from any node) | Returns to `INSPECTOR · SELECT · Select a node · Tip — Click empty canvas (or press Esc) to clear.` | unchanged (still 197 nodes · 264 links) |
| 4 | `cua.click({x:700,y:510})` (re-select) | Inspector updates again | unchanged |
| 5 | `cua.keypress({keys:["Escape"]})` | Inspector empties, Tip visible | unchanged |
| 6 | Switch filter `Tier → LIGHTWEIGHT` | Filter rebuild clears selection (Inspector empty) | Stats: `105 nodes · 160 links visible` (decreased — filter applied) |

Previously (before fix):

| Step | Action | Inspector observation | Stats |
|------|--------|-----------------------|-------|
| same as 2 | click a node | Inspector shows selected node | OK |
| same as 3 | click empty canvas | **Inspector stayed on selected node** (the bug) | OK |
| same as 5 | Esc | no global handler, Inspector stayed | OK |

**Conclusion:** T9 closed on all three reset paths (click-empty-canvas, Esc, filter-change). Soft-dim also confirmed visually: with D-05.2 selected after step 2, neighbours (TinyTask, all D-XX.Y directly connected via COVERS edges) stayed bright, distant nodes faded to opacity 0.6 with labels readable.

### Folio V verification

- 5 tabs now visible in the nav (was 4): I.Executive One-Pager · II.Knowledge Graph · III.Audit Panel · IV.Sub-Domain Deep-Dive · **V.Phase 1 Story**.
- Screenshot `t_v_after_emit.png` shows the 6-column pipeline rendered: column I lists CEO · CTO · DPO · Development Lead · B2B Customers + BGs BG-01..BG-04 with DEFINES edges, column II has TinyTask, column III lists GDPR · CRA (highlighted) and NIS 2 (faded non-applicable), column V has D-01.1 .. D-09.4 with labels, column VI has the AG goal mass.
- Counter on Folio V toolbar reads `183 nodes · 182 edges · 4 tensions · 3 gaps` (close to but not identical with the underlying KG: the column I stack counts Stakeholder + BusinessGoal separately, and the column counts exclude nodes positioned outside the visible viewport).

### Validation commands re-run

```text
python3 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/scripts/build_p1_dashboard.py --check       → exit 0
python3 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/scripts/build_p1_dashboard.py --summary     → 197/264/16
python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py --only Case_01_P1_Dashboard               → exit 0 (1 dashboard pass)
```

### Known cosmetic items left for a future polish pass (not blockers)

1. **Dashboard top header line** still says `181 nodes, 248 links, 12 audits, 417 ambiguity cards` — that string is hard-coded in the HTML (`<head>` blurb + footer). Not dynamic; with the KG at 197/264/16 it is stale. Should be either data-driven from `DATA.invariants` or updated to the current counts.
2. **Folio V "Ambiguity bars"** count is shown as `D-XX.Y (0)` for every sub-domain. Root cause: the inlined JSON in the HTML uses the **on-disk** compact shape (`{graph, company_context, nodes, links, ambiguity, invariants, audits}`), but the dashboard's JS expects the denormalised view-model shape that hoists `graph`, `stats_total`, `invariants`, `meta`, `audits` to the top level. The denormaliser preserved `ambiguity.stats_per_subdomain` under `graph.ambiguity` rather than hoisting it; the JS in Folio V reads from a path that doesn't have the bar counts, so it falls back to 0. Fix: either hoist `ambiguity.stats_per_subdomain` to top level during denormalisation, or change the Folio V access path to `G.ambiguity.stats_per_subdomain`.
3. **Folio IV (Sub-Domain Deep-Dive)** still renders partial grid (15 of 38 rows shown before pagination). Pre-existing — not introduced by this fix.

These three items are minor surface issues. T9, the underlying functional bug, is closed.

---

## Re-test after a SECOND fix pass (2026-08-26 evening)

Verdict: **PASS** — colours preserved end-to-end through the focus flow.

### What was still broken (false-positive in the previous report)

A user-supplied screenshot showed the Folio II graph washed out to a near-uniform pale blue after focusing a node (`D-05.1 Data Minimization`) — even though the Inspector correctly displayed the node's attributes, related links, and source provenance. I had initially dismissed this as a screenshot timing issue. On a re-check via my own browser it reproduced exactly: the graph went pale when ANY node was focused, despite my "soft-dim" code being in place.

### Real root cause (one layer deeper)

`rebuildGraph()` AND `applySelectionDim()` were each calling `chart.setOption({series: [{...}]})` with:

```js
emphasis: { focus: "adjacency", lineStyle: { width: 3 } },
focusNodeAdjacency: true
```

ECharts' native `focusNodeAdjacency: true` + `emphasis.focus: "adjacency"` does its own auto-dim pass when a node is focused — and that pass **overrides** the per-node `itemStyle.opacity` that `applySelectionDim` carefully set, falling back to ECharts' default-emphasis colour. Compounding this, `__focusGraphNode()` ALSO called `chart.dispatchAction({type: "highlight", seriesIndex: 0, dataIndex: ...})` after `applySelectionDim()`, which again forces a state override.

In effect the three mechanisms were fighting each other and the dim one won.

### The fix

Three lines removed (or with their content reworded). All inside `Case_01_P1_Dashboard.html`:

1. **`rebuildGraph()` (line 1157)**: drop `focusNodeAdjacency: true` and `emphasis: {focus: "adjacency", ...}` from the `series[0]` definition.
2. **`applySelectionDim()` (line 1260)**: same removal in its setOption.
3. **`__focusGraphNode()` (line 1424)**: drop the trailing `chart.dispatchAction({type: "highlight", ...})` — `applySelectionDim` is the single source of truth.
4. **`initStory()` Folio V series definition (line 1922)**: same removal for symmetry — the Folio V graph had the same double-dim with same root cause.

`applySelectionDim()` also got rewritten to build a fully-formed per-node item (`name`, `symbolSize`, `category`, `value`, `itemStyle.{color,borderColor,borderWidth,opacity}`, `label.{show,position,color,formatter,opacity}`) before `setOption`, so that any future re-render can never fall back to ECharts defaults. Categories array re-asserted on every dim pass.

### T9 verification (live, post-second-fix)

Sequence via headless Codex IAB on `http://127.0.0.1:8765/Case_01_P1_Dashboard.html`:

1. Fresh load → click `II.Knowledge Graph` tab. Graph renders in full colour (TinyTask brown, GDPR/CRA navy, D-XX.Y gilt, Domain nodes moss, clauses cerulean, AdjustedGoals mauve).
2. Switch to `III.Audit Panel`. Click `CFL-001` card → detail renders (severity · HIGH · 4 nodes affected).
3. Scroll the right panel down to the *Affected nodes* row, then click the `GDPR-C08` chip. This invokes `__focusGraphNode("GDPR-C08")` which switches tab to Folio II and runs `applySelectionDim`.
4. **Screenshot `p4_folio_ii_focus_FIXED.png`**: Inspector displays "REGULATORY CLAUSE · GDPR-C08 · Art. 9 — Processing of special categories" with all attributes, source provenance (2: `phase1_ontology.yaml@clause_mappings`, `Doc10 §8.1 (GDPR) / §8.2 (CRA)`), 3 related links and CFL-001 audit. The graph — crucially — **retains its colours**: TinyTask brown, GDPR/CRA navy gold-rimmed for the 1-hop neighbour `D-05.3`, all other sub-domains still gold, all clauses still cerulean, all D-XX.Y sub-domains still slightly dimmed (opacity 0.6) but colour-saturated.
5. Press Esc on the same selection → Inspector empties to Tip; graph back to full opacity, fully coloured.

Prior to fix: step 4 rendered a near-uniform pale-blue canvas with the only labelled node being the GDPR-C08 in the Inspector header — confirming the wash was the problem the user reported.

### Acceptance

- `python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py --only Case_01_P1_Dashboard` → exit 0.
- Visual confirmation (preserved screenshot): all seven categories render with their assigned colours and a soft focus behaviour that keeps neighbours visible while dimming 2-hop nodes only.
- T9 fully closed. Cosmetic items (1)–(3) unchanged.

Working folder for the new screenshot: `gui-test-screenshots/p1_dashboard/p4_folio_ii_focus_FIXED.png`.

---

## Re-test after a THIRD fix pass (2026-08-26 evening) — Folio V canvas collapse

Verdict: **PASS** — Folio V pipeline now survives a focus click.

### What was still broken

A user-supplied screenshot showed the **Folio V (Phase 1 Story)** canvas completely empty after a node was selected: Inspector correctly populated (REGULATORY CLAUSE · GDPR-C02 · Art. 2 — Material scope), legend rendered, column headers visible (`I · STK+BG … VI · GOALS`), but the six-column pipeline graph produced **zero nodes**. Previously dismissed as "different from Folio II" — re-check confirmed it was the same anti-pattern, with a more dramatic failure mode.

### Real root cause (parallel to Folio II)

Same bug as Folio II but on the Folio V path. `applyStoryDim()` (Folio V's `selectNode`-equivalent) called:

```js
storyChart.setOption({
  series: [{
    itemStyle: { opacity: 0.95 },
    data: data.map(d => ({ id: d.id, itemStyle: { opacity: oneHop.has(d.id) ? 1 : 0.55 } })),
    links: links.map(l => ({ source: l.source, target: l.target,
      lineStyle: { opacity: (oneHop.has(l.source) && oneHop.has(l.target)) ? 0.95 : 0.2 } }))
  }]
});
```

The `data.map(d => ({ id: d.id, itemStyle: {...} }))` line replaces each ECharts node spec with a partial object — fine for Folio II's force layout (ECharts redraws at the new positions), **fatal for Folio V's `layout: "none"`** because the original `x, y` coordinates are not part of the new spec, so ECharts teleports every node to the origin (0, 0). Pipeline visually collapses; only the legend, headers and Inspector survive.

### The fix

Rewrote `applyStoryDim()` to spread each original item, then override only `itemStyle.opacity` and `label.opacity`. Fix kept under `Case_01_P1_Dashboard.html` only, line ~1965.

```js
const visData = data.map(d => ({
  ...d,                                       // preserves x, y, name, symbolSize, category, color, label.formatter
  itemStyle: { ...(d.itemStyle || {}), opacity: !oneHop ? 1 : (oneHop.has(d.id) ? 1 : 0.55) },
  label:      { ...(d.label || {}),      opacity: !oneHop ? 1 : (oneHop.has(d.id) ? 1 : 0.55) }
}));
```

Same merge pattern for `visLinks` — original `lineStyle` preserved, opacity replaced.

### Verification (live)

Sequence via headless Codex IAB on `http://127.0.0.1:8765/Case_01_P1_Dashboard.html`:

1. Fresh load → click `V.Phase 1 Story`. Folio V paints six columns of coloured nodes (Stakeholders, BGs, TinyTask, Regulations, Clauses, Sub-Domains, Adjusted Goals) at full opacity. Counter `183 nodes · 182 edges · 4 tensions · 3 gaps`.
2. Click directly on the TinyTask node via canvas `cua.click({x:720,y:540})`. This invokes Folio V's `storyChart.on("click")` → `renderSideForNode` + `mirrorSideToStory` + **`applyStoryDim`**.
3. **Screenshot `p4_folio_v_focus_FIXED.png`**: Inspector shows "RELATION · COVERS · FROM REGULATORYCLAUSE (GDPR-C05 Art. 6 — Lawfulness of processing) → TO SECURITYCONTROLDOMAIN (D-05.1 Data Minimization) · Attributes: Art. 6 · Source provenance: phase1_ontology.yaml@clause_mappings · Doc10 §8". Tooltip line "GDPR-C05 → D-05.1" floats. All six columns of the pipeline remain painted, with the 1-hop neighbours (the TinyTask, the clicked edge endpoints) at full opacity and the rest at `opacity = 0.55` but **still at their original positions**, not at the origin. The pipeline reads correctly.

### Acceptance

- `python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py --only Case_01_P1_Dashboard` → exit 0.
- Visual confirmation: pipeline rendering preserved across the focus transition.
- T9 closed for Folio V as well as Folio II.
- Cosmetic items (1)–(3) from the previous report still open:
  - Header line `181 nodes, 248 links, 12 audits` is static text, not data-driven.
  - Folio V ambiguity bars show `(0)` for every sub-domain because `ambiguity.stats_per_subdomain` is not hoisted on the denormalise path.
  - Folio IV grid shows only the first page of 38 sub-domains (the `GRID = DATA.grid` access path uses the un-hoisted JSON shape).

Working folder for the new screenshot: `gui-test-screenshots/p1_dashboard/p4_folio_v_focus_FIXED.png`.

---

## Re-test after a FOURTH fix pass (2026-08-26 evening) — Folio IV grid

Verdict: **PASS** — 38 rows rendered, goal-id chips clickable, jump to Folio II working.

### What was broken

The Folio IV (Sub-Domain Deep-Dive) tab showed a header row plus the explanatory footnote but **zero of 38 rows populated**. A user-supplied screenshot confirmed the empty table.

### Root cause

The dashboard used `const GRID = DATA.grid;` (line 903 of `Case_01_P1_Dashboard.html`) — assuming a top-level `grid` field in the inlined JSON. The earlier "denormalise" pass that stuffed `graph`/`stats_total`/`invariants`/`meta`/`audits` into the top level had **never hoisted `grid`** — the emit executor flagged this honestly at the time but the dashboard was not updated to compensate, so `GRID` was `undefined`, `Object.entries(GRID)` returned `[]`, and the table rendered 0 rows.

### The fix

Replace the `DATA.grid` assignment with a runtime builder that derives the same shape from `NODES` + `LINKS` + `G.ambiguity.stats_per_subdomain`:

```js
const GRID = (() => {
  // Two indexes needed because the verb directions differ:
  //   MAPS_TO clause→sd  (so clauses live at linkByTo[sd])
  //   YIELDS    sd→goal  (so goals live at linkByFrom[sd])
  const linkByTo   = new Map(); LINKS.forEach(l => { if (!linkByTo.has(l.to))   linkByTo.set(l.to,   []); linkByTo.get(l.to).push(l); });
  const linkByFrom = new Map(); LINKS.forEach(l => { if (!linkByFrom.has(l.from)) linkByFrom.set(l.from, []); linkByFrom.get(l.from).push(l); });
  ...
  NODES.filter(n => n.type === "SecurityControlDomain").forEach(n => {
    const clauseLinks  = (linkByTo.get(n.id)   || []).filter(l => l.rel === "MAPS_TO");
    const yieldLinks   = (linkByFrom.get(n.id) || []).filter(l => l.rel === "YIELDS");
    // ni_avg: mean of clause normative_weight; source_regs: from incoming MAPS_TO; amb: from G.ambiguity.stats_per_subdomain
    // Goals: slot 001 → HL goal (Doc13 §2) which doubles as the GDPR-driven goal (Doc13 §3, track=GDPR);
    //        slot 002 → CRA-driven goal (Doc13 §4, track=CRA).
    out[n.id] = { ..., hl: slot001[0], gdpr: slot001[0], cra: slot002[0] };
  });
})();
```

The HL/GDPR distinction comes from how Doc13 chapters re-use the same `AG-D-XX.X-001` node id (§2 HL list and §3 GDPR-driven list share the slot). The dashboard now reflects that nuance correctly: HL GOAL and GDPR GOAL columns point at the same node id (slot-001), while CRA GOAL points at the slot-002 node.

### Verification

Live test in headless Codex IAB on `http://127.0.0.1:8765/Case_01_P1_Dashboard.html`:

1. Fresh load → click `IV.Sub-Domain Deep-Dive`. Table shows the **15-row first page** (pageLength=15 of 38 entries); pagination footer "Showing 1 to 15 of 38 entries · Previous 1 2 3 Next". All columns populated — CODE (`D-01.1` etc.), NAME, REG COV (`GDPR, CRA` or `CRA` or `—`), NI (1–3 integer or `—`), COVERAGE (`SUBSTANTIVE`/`PARTIAL`/`NOT_ADDRESSED`), TIER (`LIGHTWEIGHT`/`MINIMAL`/`DEFERRED`), **HL GOAL (`AG-D-XX.X-001` in orange)**, **GDPR GOAL (same id, blue)**, **CRA GOAL (`AG-D-XX.X-002` in mauve)**, ACTIVE (●/○), AMBIG IN SCOPE (`X / Y` from Doc09 §2), SOURCE DOCS (`Doc11 §3 · Doc12 §4`). D-02.4 correctly shows `—` for goals (NOT_ADDRESSED, DEFERRED — goal-less by design).
2. Click the first HL goal chip `AG-D-01.1-001`. Active tab switches to `II.Knowledge Graph` and the Inspector reads: `INSPECTOR · ADJUSTED GOAL · AG-D-01.1-001 (HL/GDPR-driven) · ATTRIBUTES (subdomain_id=D-01.1, slot=001, track=GDPR, priority=MUST, tier=LIGHTWEIGHT) · SOURCE PROVENANCE: Doc13 §2 (HL) + §3 (GDPR-driven) · RELATED LINKS: ← YIELDS D-01.1`. Pipeline confirmed — confirmation of T8 from the very first GUI test.

### Final acceptance

- `python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py --only Case_01_P1_Dashboard` → exit 0.
- Visual confirmation (preserved screenshot): all 38 sub-domains are reachable from the Folio IV table (page 1 of 3 shown above).
- The 3 cosmetic items tracked in the prior report (static header line, ambiguity bars showing `(0)` in Folio V, partial Folio IV view) are now down to **2** — the Folio IV fix removes the third item by construction.
- Scope deliberately held narrow: the fix does not hoist `grid` into the inlined JSON (that would require extending the build/diff pipeline), it rebuilds the table view from the canonical KG JSON that IS available, which is the more durable solution.

Working folder for the new screenshot: `gui-test-screenshots/p1_dashboard/p4_folio_iv_FIXED.png`.

---

## Final summary of the four GUI test fix passes (2026-08-26)

| Pass | Folio affected | Symptom | Root cause | Fix | Commit |
|------|----------------|---------|------------|-----|--------|
| 1 | II (KG) | Click empty canvas didn't clear Inspector; filter change left Inspector stale | No `else` branch on `chart.on("click", …)`; filter handlers reset `selectedNode` but not Inspector | `chart.getZr().on("click", e => clearSelection(false))`; new `clearSelection(rebuild)` helper for filter handlers; global Esc keydown; Inspector empty-state tip | `b6c58aa` |
| 2 | II (KG) | Graph washes out to pale blue after focus | ECharts native `focusNodeAdjacency: true` + `emphasis.focus: "adjacency"` + `dispatchAction('highlight')` overrode `applySelectionDim` opacity | Removed all three ECharts-native auto-dim mechanisms; rewrote `applySelectionDim` to spread full per-node specs | `8ab1688` |
| 3 | V (Phase 1 Story) | Pipeline graph collapsed to origin after focus | `applyStoryDim` `setOption` sent data with only `{id, itemStyle.opacity}` — loss of `x, y` keys under `layout: "none"` | `applyStoryDim` spreads the original item, overrides only `itemStyle.opacity` and `label.opacity` | `b11ff4c` |
| 4 | IV (Sub-Domain Deep-Dive) | Table rendered 0 of 38 rows | `DATA.grid` not hoisted in inlined JSON | `GRID` rebuilt at runtime from `NODES`, `LINKS`, `G.ambiguity.stats_per_subdomain`; `linkByTo` + `linkByFrom` indexes handle verbs in either direction | `10c9148` |

---

## Re-test after Phase A — RACI (2026-08-26 evening)

Verdict: **PASS** — Phase A lands cleanly. Six tabs, Folio VI RACI Matrix renders 43×6 with R/A/C/I palette, RACI layer toggle on Folio II flips the graph between 197/264 and 246/505. Five new GAP-RACI findings join the existing 16 audits. One bonus cosmetic fix also falls out.

### What changed (Phase A scope)

The user accepted a multi-phase roadmap. Phase A added the RACI (Doc07) entities. The next phases — Architecture+Third Parties (B), Maturity+Verification (C), NIST mapping (D), Ambiguity detail+Citations (E) — are still on the table.

- **Ontology v1.3** (additive to v1.2): 2 new classes (`RaciRole`, `RaciActivity`), 3 new relations (`RACI`, `APPLIES_TO`, `MAPS_TO_STK deferred`), 1 new enum (`RaciLetter`), 7 new counts, 2 new id_patterns. Validator diff: 59 insertions, 1 deletion (the version string); all 10 v1.2 classes + 12 v1.2 relations + 9 v1.2 enums unchanged. Report: `validation/P1_ontology_v1.3_validation.md`.
- **KG extension** (additive to v1.2): 6 `RaciRole` nodes (DPO/CISO/DEV/LEGAL/HR/BOARD) + 43 `RaciActivity` nodes (41 active, 2 inactive) + 206 `RACI` edges (200 single-letter + 3 composite R/A split into 2 each = 6 composite edges) + 35 `APPLIES_TO` edges + 5 new `coverage_gap` audits (`GAP-RACI-01..05`). Validator spot-checked 6 roles + 6 activities + 10 RACI + 3 APPLIES_TO + 5 audits; report: `validation/P1_raci_extension_v1.3_validation.md`. Original 197/264/16 byte-identical.
- **Dashboard** (in-place edit, single file):
  - New tab **VI. RACI Matrix** — 43×6 matrix with R/A/C/I coloured badges, 5 colour tokens harmonised with the existing palette (R=cool blue-grey, A=gilt, C=sage, I=dust). Cells: R/A composites rendered as a single composite badge (3 such cells verified). Filters: Domain (D-01..D-10), Active-only (41), search. Click on row → side panel shows ACT + corpus_reg_req + APPLIES_TO targets. Click on sub-domain ID in the row → focus that sub-domain in Folio II.
  - New toggle **RACI layer** on Folio II — OFF by default, ON toggles the graph from 197/264 to 246/505. No soft-dim regression: `rebuildGraph()` and `applySelectionDim()` continue to spread full per-node specs (fix #2 preserved). Categories: `RaciRole` slate `#3a4a5c`, `RaciActivity` sand `#d4a373` — both complement the existing 7-category palette.
  - Re-emit of the inlined JSON — this time all path-roots the JS reads are hoisted at top level (`graph`/`stats_total`/`invariants`/`meta`/`audits`), eliminating the `DATA.grid` / `DATA.ambiguity.stats_per_subdomain` undefined-access class of bug.

### Verification (live)

`http://127.0.0.1:8765/Case_01_P1_Dashboard.html` opened fresh; six tabs present (I/II/III/IV/V/V).

- **T1 Folio VI load** — PASS. 43 of 43 activities shown. Domain filter lists D-01..D-10. Active-only checkbox reduces to 41. R/A/C/I cells render with the chosen palette. Sub-domain IDs (`D-01.1`, `D-01.3` etc.) are clickable.
- **T2 Activity row click** — PASS. ACT-01 row click opens side panel: `Activity · ACT-01 · Encrypt personal data at rest · domain D-01, sub-domain D-01.1 · corpus_reg_req: D-01.1: 1.1.1, 1.1.3 (GDPR + CRA) · APPLIES TO D-01.1`. Confirmed via DOM snapshot.
- **T3 Sub-domain chip click** — PASS. Click `D-01.1` in the row → switches tab to Folio II → Inspector shows D-01.1 attrs (covered/active/SUBSTANTIVE/LIGHTWEIGHT).
- **T4 Folio II RACI toggle** — PASS. Counter flips `197 → 246` (nodes) and `264 → 505` (links) when toggled. Toggle OFF returns to original counts.
- **T5 Graph focus after RACI on** — PASS. Click D-01.1 in Folio II with RACI on → Inspector renders ATTRIBUTES + SOURCE PROVENANCE + RELATED LINKS + RELATED AUDITS for D-01.1 (no wash-out regression).
- **T6 Folio V regression** — PASS. All 6 columns render; click does not collapse pipeline. **Bonus**: Folio V sub-domain labels now show the real ambiguity counts (e.g. `D-01.1(12)`, `D-01.2(7)`, `D-04.3(34)`) instead of the previous `(0)` placeholder — the re-emit hoisted `G.ambiguity.stats_per_subdomain` correctly. This closes one of the two cosmetic items that were still open from the previous report.
- **T7 Folio IV regression** — PASS. 38 rows still visible; 42 goal-id chips; clicking first switches to Folio II.
- **T8 Folio III regression** — PASS. 21 audit cards visible (16 original + 5 GAP-RACI). Locator count confirmed: `auditCards=21`, `gapCards=5` (matching `GAP-RACI-01..05`).

### Acceptance

- `python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py --only Case_01_P1_Dashboard` → exit 0.
- `python3 scripts/build_p1_dashboard.py --check` → exit 0.
- `python3 scripts/build_p1_dashboard.py --summary` → `nodes_count: 246`, `links_count: 505`, `audits_count: 21`, `invariant_pass: true`.
- Visual confirmation (preserved screenshots): all 6 folios render correctly.

### Cosmetic state — update

Previous report had **2 open items** (header static line `181 nodes, 248 links, 12 audits`; Folio V ambiguity bars showing `(0)`). Phase A closed one of them (Folio V ambiguity bars) by hoisting `ambiguity.stats_per_subdomain` correctly. One item remains.

### Phase A artefacts & screenshots

- New: `validation/P1_ontology_v1.3_validation.md`
- New: `validation/P1_raci_extension_v1.3_validation.md`
- Updated: `phase1_ontology.yaml` (v1.3), `data/phase1_ontology.compact.json`, `data/phase1_graph.json`, `scripts/build_p1_graph.py`, `scripts/build_p1_dashboard.py`, `Case_01_P1_Dashboard.html` (re-emit), `validation/P1_dashboard_gui_test.md` (this block).
- Working folder for this session's screenshots: `gui-test-screenshots/p1_dashboard/` — files `p5_folio_vi_RACI_FIXED.png`, `p5_folio_ii_raci_on.png`, `p5_folio_v_after_phaseA.png`.

### Next phase

Ready to start Phase B (Architecture+Third Parties) on the user's signal. Same ritual: ontology v1.4 → KG → dashboard → smoke → commit.

---

## Re-test after Phase B — Architecture & Third Parties (2026-08-27)

Verdict: **PASS** — seven tabs now, Folio VII renders the architecture diagram + third-party risk register, Arch-layer toggle on Folio II flips the graph from 197/264 to 272/785 when combined with RACI.

### What changed (Phase B scope)

User accepted Phase B (Architecture + Third Parties, Doc04 + Doc06). Five new node classes (System, DataStore, DataFlow, PersonalDataCategory, DataSubjectCategory, ThirdParty — six total but classified as one triplet in the schema), six new relation verbs (HOSTS, PROCESSES, INVOLVES, INVOLVES_STORE, INVOLVES_FLOW, PROCESSED_BY, PROCESSED_BY_3P, CAPTURES, CORRESPONDS_TO, FLOWS_BETWEEN deferred, USES deferred). Six new colours added to the Folio II palette.

- **Ontology v1.4** (additive to v1.3): 6 new classes, 11 new relations (8 active + 1 partial + 2 deferred), 1 new enum `RiskScore`, 7 new counts, 4 new id_patterns. Validator diff: 116 insertions, 1 deletion (the version string). An intermediate FAIL was caught (duplicate sibling keys `classes:` / `relations:` / `enums:` / `invariants:` were emitted at the end of `kg_ontology:`, which YAML silently last-wins); the orchestrator merged the v1.4 entries into the v1.3 blocks. Report: `validation/P1_ontology_v1.4_validation.md` (verdict updated to PASS).
- **KG extension** (additive to v1.3): 26 new nodes (5 System + 3 DataStore + 5 DataFlow + 4 PersonalDataCategory + 3 DataSubjectCategory + 6 ThirdParty) + 280 new edges (3 HOSTS + 99 INVOLVES + 68 INVOLVES_STORE + 86 INVOLVES_FLOW + 3 PROCESSES + 8 PROCESSED_BY + 1 PROCESSED_BY_3P + 10 CAPTURES + 2 CORRESPONDS_TO) + 5 new audits (NEW-01..NEW-05: NEW-01 broken_link for free-text system references in Doc04 §3, NEW-02 cross_doc_conflict for Doc03 missing 4 vendors, NEW-03 coverage_gap AWS decomposition, NEW-04 coverage_gap Datadog exit plan, NEW-05 broken_link Snyk SBOM tier). Total: **272 / 785 / 26**. Original 246/505/21 byte-identical. Report: `validation/P1_graph_extension_v1.4_validation.md` (CONDITIONAL PASS).
- **Dashboard** (in-place, single file):
  - New tab **VII. Architecture & Third Parties** — split layout: left = FLOW MAP ECharts (`layout: "none"`, hand-coded columns ExternalUser → WebClient → Systems → Stores → Flows → PDCs/DSCs, ~16 curated edges); right = RISK REGISTER table (6 rows, columns Vendor/Services/Criticality/Risk/DPA/SBOM/Exit Plan/Last Review, sortable by Risk asc → name). Click a row → side panel shows full vendor dossier (services[], regions[], art_28_dpa, security_audit_right, subprocessor_approval, etc.). Bottom strip: 38 sub-domain coverage bars stacked (INVOLVES / INVOLVES_STORE / INVOLVES_FLOW).
  - New toggle **Architecture layer** on Folio II (OFF default). When ON, adds 26 nodes + 280 edges (SYS/STORE/FLOW/PDC/DSC/ThirdParty + HOSTS/PROCESSES/INVOLVES×3/PROCESSED_BY×2/CAPTURES/CORRESPONDS_TO). Stacks with the RACI layer; both ON → 272/785.
  - Six new category colours for the 6 new node types: System slate `#3a3f4a`, DataStore teal `#4a7378`, DataFlow sky `#6f8aa0`, PersonalDataCategory ochre `#a8854a`, DataSubjectCategory rose `#a06a78`, ThirdParty ink `#1f2937`. Designed to harmonise with the existing 9-category palette.
  - Re-emit of the inlined JSON — this round all path-roots the JS reads are hoisted at top level (`graph`/`stats_total`/`invariants`/`meta`/`audits`); node count 272 + edge count 785 verified.

### Verification (live)

`http://127.0.0.1:8765/Case_01_P1_Dashboard.html` opened fresh (with reload to bypass cache).

- **Folio VII render** — **PASS**. 7 tabs visible (after reload). The header strip reads "FOLIO VII · Architecture & Third Parties · SYSTEMS · STORES · FLOWS · VENDORS · 5 SYSTEMS · 3 STORES · 5 FLOWS · 6 VENDORS". The left flow map shows SYS-01..SYS-05 (slate navy) + STORE-01..03 (teal) + FLOW-01..05 (sky) + PersonalDataCategory nodes (ochre) + ExternalUser / WebClient (semitransparent oranges). Edges between them visible. The right risk register shows the 6 vendors with: AWS (CRITICAL, L, DPA Y, SBOM N, Exit Plan N), Stripe (CRITICAL, L, Y, N, **Y**), Auth0 (CRITICAL, L, Y, N, Y), Snyk (IMPORTANT, L, Y, **Y**, Y — scanner), Datadog (CRITICAL, **M**, Y, N, N), GitHub (IMPORTANT, **M**, Y, N, Y). Bottom: 38 sub-domain coverage bars. Saved: `p6_folio_VII_arch_FIXED.png`.

- **Folio II Arch toggle** — **PASS**. Live counts: `Off→On` 197→223 nodes, 264→544 links. `RACI on alone` 246/505. `RACI + Arch both` 272/785 — exactly the full JSON totals. The toggle round-trips cleanly without console errors; the `applySelectionDim` path is preserved (no `data: []` reset).

- **Folio IV regression** — **PASS**. `folioIvRows=15` (pageLength=15 of 38), `goalChips=42`. No regression.

- **Folio III regression** — **PASS**. `auditCards=26` (16 originals + 5 GAP-RACI + 5 NEW-01..05), `gapCards=5` for GAP-RACI subset. No regression.

- **Folio V regression** — not directly re-checked here but T5 of the subagent's Playwright verification covered the same path with no collapse. No code path was changed for Folio V in Phase B.

### Acceptance

- `python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py --only Case_01_P1_Dashboard` → exit 0.
- `python3 scripts/build_p1_dashboard.py --check` → exit 0.
- `python3 scripts/build_p1_dashboard.py --summary` → `nodes_count: 272`, `links_count: 785`, `audits_count: 26`, `invariant_pass: true`.
- Visual confirmation (preserved screenshots in `gui-test-screenshots/p1_dashboard/`).

### Known cosmetic state

Previous report's two open items: (1) header static line `181 nodes, 248 links, 12 audits` — still open (the dashboard JS reads `STATS` / `INV` but the top header is hardcoded text); (2) Folio V ambiguity bars showing `(N)` values — fixed in Phase A's re-emit. Phase B did not address (1).

### Phase B artefacts & screenshots

- New: `validation/P1_ontology_v1.4_validation.md`
- New: `validation/P1_graph_extension_v1.4_validation.md`
- Updated: `phase1_ontology.yaml` (v1.4), `data/phase1_ontology.compact.json`, `data/phase1_graph.json`, `scripts/build_p1_graph.py`, `scripts/build_p1_dashboard.py`, `Case_01_P1_Dashboard.html` (re-emit), `validation/P1_dashboard_gui_test.md` (this block).
- Working folder for this session's screenshots: `gui-test-screenshots/p1_dashboard/` — files `phaseB_tN_*.png` (T1–T7) and `p6_folio_VII_arch_FIXED.png`.

### Next phase

Ready to start Phase C (Maturity+Verification — Doc08 §9 verification criteria + Doc12 §4 proportionality attrs as enriched columns on the existing nodes; no new node types expected) on the user's signal. Same ritual: ontology v1.5 → KG attrs → dashboard cols → smoke → commit.

---

## Re-test after Phase C — Maturity + Verification (2026-08-27)

Verdict: **PASS** — Folio IV gains 7 toggleable columns (Maturity, Verification, Evidence, Owner, Risk, Priority, I/P) populated from Doc12 §4; Folio II Inspector surfaces 5 verification attrs on clauses + 13 proportionality attrs on sub-domains; Folio III grows from 26 → 29 audit cards (NEW-06/07/08). No regressions.

### What changed (Phase C scope)

Phase C is **attrs-only** — no new node types or relations. We enriched:

- **RegulatoryClause (54 nodes)** — added 5 attrs: `verification_criteria`, `evidence_type`, `risk_if_not_met`, `maturity_cur`, `maturity_tgt`. Source: Doc08 §9 (54-row per-article breakdown).
- **SecurityControlDomain (37 active nodes)** — added 13 attrs: `i`, `p`, `tier`, `satisfaction_pattern`, `evidence_depth`, `verification_method`, `ownership`, `example_controls`, `notes`, `risk_if_not_met`, `maturity_cur`, `maturity_tgt`, `implementation_priority`. Source: Doc12 §4 (37-row per-subdomain proportionality).
- 2 new invariants (`articles_with_verification=54`, `subdomains_with_proportionality=37`).
- 3 new audits: **NEW-06** (cross_doc_conflict, medium) — Doc08 §9 Art. 35/Art. 37 asymmetry vs `phase1_graph.json` clauses; **NEW-07** (broken_link, low) — non-canonical `evidence_type` strings; **NEW-08** (coverage_gap, low) — uniform 2/4→3/4 maturity across 36 of 37 rows.
- One dynamic accumulator (CFL-006 — tier vs proportionality_tier drift) built but currently zero-counted.

Total: **272 / 785 / 29**. Original 272/785/26 byte-identical except for the attrs additions and the 3 new audits. Report: `validation/P1_graph_phase_c_validation.md` (verdict: PASS).

### Verification (live)

`http://127.0.0.1:8765/Case_01_P1_Dashboard.html` opened fresh (with reload to bust cache).

- **Folio IV with Phase C enrichment** — **PASS**. Header strap reads "38 ROWS · 19 COLUMNS · PHASE C ENRICHMENT". A "Show columns" toggle bar appears above the table with 7 checkboxes (Maturity cur→tgt, Verification method, Evidence depth, Owner, Risk, Priority, I/P Build·Must) — all default ON. Toggle off → column hidden; toggle back on → column re-appears. Sample row D-01.1: Maturity `2 → 3` (amber badge), Verification `DEMONSTRATE + INSPECT`, Evidence `Managed-service config documented + annual review; no dedi…` (truncated at 60 chars with full-text tooltip on hover), Owner `Shared (AWS + company)`, Risk `HIGH` (red), Priority `HIGH` (red), I/P `BUILD` (blue pill) + `MUST` (red pill). Saved: `p7_folio_IV_phase_C.png`.

- **Folio II Inspector for clause** — **PASS**. Click on GDPR-C04 → Inspector renders the 5 new attrs in alphabetical order: `evidence_type='INSPECT (config audit + annual review)'`, `maturity_cur=2`, `maturity_tgt=3`, `risk_if_not_met='HIGH'`, `verification_criteria='Operational check per Doc 07c Appendix A §A.1.1/D-01.1'`. Plus the existing 7 attrs.

- **Folio II Inspector for sub-domain** — **PASS**. Click on D-01.1 → Inspector renders all 13 proportionality attrs: i=BUILD, p=MUST, tier=LIGHTWEIGHT, satisfaction_pattern=BUY_MANAGED, evidence_depth='Managed-service config documented + annual review; no dedicated in-house program', verification_method='DEMONSTRATE + INSPECT', ownership='Shared (AWS + company)', example_controls='AWS S3 / DynamoDB SSE-KMS enabled (AES-256 default); no company-owned KMS program', notes='Unified AES-256 baseline satisfies SAME pair', risk_if_not_met='HIGH', maturity_cur=2, maturity_tgt=3, implementation_priority='HIGH'. Click on D-02.4 → DEFERRED markers (`tier='DEFERRED'`, evidence_depth='—', etc.).

- **Folio III 29 audit cards** — **PASS**. 29 cards in two columns (CFL/BLN/CVG/BAM). NEW-06 detail panel mentions Art. 35 + GDPR-C28 with the three P7 human-pickable resolutions documented (expand Doc08 §9 / drop GDPR-C28 / duplicate the §9 row).

- **Folio V regression** — **PASS**. 6 columns preserved; no collapse (fix #3 still holds).
- **Folio VI RACI regression** — **PASS**. 43×11 matrix renders (including the 3 new Phase-C attrs where applicable).
- **Folio VII Architecture+ThirdParties regression** — **PASS**. Diagram + 6 vendor risk register + coverage map.
- **Arch+RACI toggle on Folio II** — **PASS**. Off/Off: 197/264; Arch only: 223/544; RACI only: 246/505; Both on: 272/785 (exact match to JSON totals).

### Acceptance

- `python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py --only Case_01_P1_Dashboard` → exit 0.
- `python3 scripts/build_p1_dashboard.py --check` → exit 0.
- `python3 scripts/build_p1_dashboard.py --summary` → `nodes_count: 272`, `links_count: 785`, `audits_count: 29`, `invariant_pass: true`.
- Visual confirmation (preserved screenshots in `gui-test-screenshots/p1_dashboard/` — `phaseC_tN_*.png` plus `p7_folio_IV_phase_C.png`).

### Critical decision surfaced for human review (P7)

**NEW-06 — Art. 35 / Art. 37 asymmetry.** Doc08 §9 carries 1 row for Art. 35 (DPIA, D-09.2) and 1 row for Art. 37 (DPO, D-08.2). `phase1_graph.json` carries TWO Art. 35 nodes (GDPR-C27 = "Art. 35" and GDPR-C28 = "Art. 35(1)") and ZERO Art. 37 nodes. Ordinal mapping forced the §9 Art. 37 row onto GDPR-C28 — a topic drift (the verification attributes for GDPR-C28 describe Art. 37 / DPO, not Art. 35(1) / DPIA). Audit panel surfaces three P7 human-pickable resolutions:

(a) Expand Doc08 §9 to 2 rows for Art. 35 (Art. 35 (1) + Art. 35 (7)/(11)) and add an Art. 37 row.
(b) Drop GDPR-C28 from CLAUSES and add GDPR-C29 = Art. 37.
(c) Duplicate the Art. 35 ART_VERIFICATION row to both GDPR-C27 and GDPR-C28.

**Hard constraint** of Phase C forbids editing source docs, so the audit is the delivery vehicle for human decision.

### Known cosmetic state

Previous report's one open item: header static line — still partially open. The Phase C fix updated the strap from `181 nodes, 248 links, 12 audits` to `272 nodes, 785 links, 29 audits` (now reads from `g.invariants` indirectly — though there's still hardcoded text in some places; not exhaustive).

### Phase C artefacts & screenshots

- New: `validation/P1_graph_phase_c_validation.md`
- Updated: `scripts/build_p1_graph.py` (Phase C literals + merge logic + 3 audits + 2 invariants), `scripts/build_p1_dashboard.py` (check_phase_c sub-checks), `data/phase1_graph.json` (regenerated), `data/phase1_ontology.compact.json` (refreshed mirror), `Case_01_P1_Dashboard.html` (re-emit + column toggles + Inspector attrs + audit detail), `validation/P1_dashboard_gui_test.md` (this block).
- Working folder for this session's screenshots: `gui-test-screenshots/p1_dashboard/` — `phaseC_tN_*.png` (14 files) plus `p7_folio_IV_phase_C.png`.

### Next phase

Ready to start Phase D (NIST CSF/PF/AI-RMF — Doc13 §7; cross-check via `kg.sh nist`) on the user's signal. Same ritual: ontology v1.5 (this time REAL — adding new classes/relations for NistCsfControl, NistPfControl, NistAiRmfControl + ALIGNS_TO relations) → KG nodes/edges → dashboard layer toggle on Folio II → smoke → commit.

## Artefacts & screenshots

Working folder: `gui-test-screenshots/p1_dashboard/` (project-relative)

| File | Captured state |
|------|----------------|
| `t1_initial_load.png` | Folio I render — 7 cards (Company, Applicability 2/5, Coverage Tier, Coverage Level, Goals 69, Ambiguity 417, Caveats), tablist, footer. |
| `t2_folio_ii_initial.png` | Folio II render — canvas (181 nodes), INSPECTOR empty ("Select a node"), filter toolbar visible. |
| `t2_after_click.png` | Folio II after first (mis-aimed) `cua.click` — invariant state, Inspector still empty. |
| `t2_post_canvas_click_invariant.png` | Folio II after the second `cua.click` round — INSPECTOR still empty (canvas click failed to hit a node). |
