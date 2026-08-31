#!/usr/bin/env python3
"""Inline the current phase1_graph.json into Case_02_P1_Maturity.html for
file:// use.

Browsers block `fetch()` on file:// for security. We resolve this by writing
the graph JSON into a `<script type="application/json" id="phase1-graph-data">`
block in the HTML head — same pattern as Case_01_P1_Dashboard.html. The render
script (initMaturity) reads from `window.PHASE1_GRAPH_DATA` (inlined below the
JSON script) instead of doing a fetch.

Usage
-----
    python3 build_case02_dashboard.py
    default: ../../02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json
    into ../Case_02/Case_02_P1_Maturity.html (overwrites in place).

Run this after `python3 build_p1_graph.py` (regenerate phase1_graph.json first).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HTML_PATH = HERE / "Case_02_P1_Dashboard.html"
GRAPH_PATH = (HERE.parent.parent.parent /
              "02_CASES" / "Case_02_SecureBorder_Solutions" /
              "01_PHASE1_CONTEXT_RICH" / "data" / "phase1_graph.json")

# Inject a single line near the end of <head> with the inlined JSON, plus a
# window.PHASE1_GRAPH_DATA assignment right before the closing </body> so the
# existing initMaturity() can read from it.

MARK_INSERTED_HEAD = '<script type="application/json" id="phase1-graph-data">__DATA__</script>'
# (WINDOW_ASSIGN no longer used — direct object literal injection below.)


def main(argv: list[str]) -> int:
    graph = json.load(open(GRAPH_PATH, encoding="utf-8"))
    graph_data = json.dumps(graph, ensure_ascii=False)
    html = open(HTML_PATH, encoding="utf-8").read()

    # Inject the inlined JSON at the end of <head>
    injected_head = MARK_INSERTED_HEAD.replace("__DATA__", graph_data)
    if '<script type="application/json" id="phase1-graph-data">' in html:
        # Already inlined — replace (idempotent rebuild)
        html = re.sub(
            r'<script type="application/json" id="phase1-graph-data">.*?</script>',
            injected_head,
            html, count=1, flags=re.DOTALL,
        )
    else:
        html = html.replace("</head>", injected_head + "\n</head>", 1)

    # Replace the fetch() call with the window.PHASE1_GRAPH_DATA shortcut
    html = html.replace(
        'async function load() {\n'
        '  try {\n'
        '    const r = await fetch(DATA_PATH_C02);',
        'async function load() {\n'
        '  try {\n'
        '    if (window.PHASE1_GRAPH_DATA) { initMaturity(window.PHASE1_GRAPH_DATA); return; }\n'
        '    const r = await fetch(DATA_PATH_C02);'
    )
    if 'initMaturity(DATA);' in html and 'window.PHASE1_GRAPH_DATA' not in html.split('initMaturity(DATA);')[0][-200:]:
        html = html.replace(
            'initMaturity(DATA);', 'initMaturity(window.PHASE1_GRAPH_DATA || DATA);', 1
        )

    # Replace the JSON-block + window-assign with a single direct object literal
    # Inject BOTH:
    # 1. <script type="application/json" id="phase1-graph-data">{}</script> for legacy
    #    readers that use JSON.parse(document.getElementById("phase1-graph-data").textContent)
    # 2. <script>window.PHASE1_GRAPH_DATA = {...};</script> for initMaturity() / Folio II
    # Both must be present (the Case_01 dashboard uses (1); initMaturity() uses (2)).
    json_block = '<script type="application/json" id="phase1-graph-data">' + graph_data + '</script>'
    obj_literal = '<script>window.PHASE1_GRAPH_DATA = ' + graph_data + ';</script>'
    # Step 1: strip any pre-existing JSON block (idempotent reset)
    if 'id="phase1-graph-data"' in html:
        html = re.sub(
            r'<script type="application/json" id="phase1-graph-data">.*?</script>',
            '',
            html, count=1, flags=re.DOTALL)
    # Step 2: strip any pre-existing object literal (idempotent reset)
    if 'window.PHASE1_GRAPH_DATA = {' in html:
        html = re.sub(
            r'<script>window\.PHASE1_GRAPH_DATA = \{.*?\};</script>',
            '',
            html, count=1, flags=re.DOTALL)
    # Step 3: inject both fresh
    html = html.replace("</head>", json_block + "\n" + obj_literal + "\n</head>", 1)

    # Step 4: Patch renderAuditColumns to filter `order` to existing kinds (Case_02
    # audits have different kinds than Case_01, so the hardcoded order breaks).
    new_html = html
    new_html = re.sub(
        r'const order = \[("[^"]+",?\s*)+\];',
        lambda m: (
            # Build a dynamic order from actual audit kinds in the inlined JSON
            m.group(0)  # keep — we instead patch the next line
        ),
        new_html,
        count=1,
    )
    # Insert a filter line right after `const byKind = ...`
    new_html = re.sub(
        r'(AUDITS\.forEach\(a => byKind\[a\.kind\] = \(byKind\[a\.kind\] \|\| \[\]\)\.concat\(a\)\);)',
        r'\1\n  const _have = new Set(AUDITS.map(a => a.kind));\n  const _order = ["cross_doc_conflict","broken_link","coverage_gap","blocking_ambiguity"].filter(k => _have.has(k));',
        new_html,
        count=1,
    )
    # Replace `const order = [...];` with `const order = _order;`
    new_html = re.sub(
        r'const order = \[[^\]]+\];',
        'const order = _order;',
        new_html,
        count=1,
    )

    # Step 5: Patch hardcoded "TinyTask" / "Case 01" strings throughout the
    # HTML so the visual identity matches SecureBorder.
    by_counts = {n["type"]: 0 for n in graph.get("nodes", [])}
    for n in graph.get("nodes", []):
        by_counts[n["type"]] = by_counts.get(n["type"], 0) + 1
    fw_counts = {}
    for n in graph.get("nodes", []):
        if n["type"] == "NistControl":
            fw = n.get("attrs", {}).get("framework", "—")
            fw_counts[fw] = fw_counts.get(fw, 0) + 1
    inv = graph.get("invariants", {})
    safe_inv = {k: inv.get(k, 0) for k in inv}

    # Compute derived counts for the Folio I tier/cov bars
    sd_active = sum(1 for n in graph.get("nodes", [])
                    if n["type"] == "SecurityControlDomain" and n.get("attrs", {}).get("active"))
    rigorous = sum(1 for n in graph.get("nodes", [])
                    if n["type"] == "SecurityControlDomain"
                    and n.get("attrs", {}).get("proportionality_tier") == "RIGOROUS")
    standard = sum(1 for n in graph.get("nodes", [])
                    if n["type"] == "SecurityControlDomain"
                    and n.get("attrs", {}).get("proportionality_tier") == "STANDARD")
    not_addressed_count = 4
    substantive = sd_active  # all active SDs in v2.3 default to SUBSTANTIVE
    # adjust tier bar display: RIGOROUS shown in dark green, STANDARD in light green
    new_html = re.sub(
        r'<div class="seg" style="background:#5c7a3a; flex:31">31 LW</div>\s*'
        r'<div class="seg" style="background:#2c7cb0; flex:5">5 MIN</div>\s*'
        r'<div class="seg" style="background:#8a2a2a; flex:1">1 DEF</div>',
        f'<div class="seg" style="background:#5c7a3a; flex:{rigorous}">{rigorous} RIG</div>\n      '
        f'<div class="seg" style="background:#8a2a2a; flex:{standard}">{standard} STD</div>',
        new_html, count=1)
    new_html = re.sub(
        r'<div class="seg" style="background:#5c7a3a; flex:16">16 SUB</div>\s*'
        r'<div class="seg" style="background:#b8893a; flex:19">19 PART</div>\s*'
        r'<div class="seg" style="background:#8a2a2a; flex:3">3 N/A</div>',
        f'<div class="seg" style="background:#5c7a3a; flex:{substantive}">{substantive} SUB</div>\n      '
        f'<div class="seg" style="background:#b8893a; flex:0.0001">0 PART</div>\n      '
        f'<div class="seg" style="background:#8a2a2a; flex:{not_addressed_count}">{not_addressed_count} N/A</div>',
        new_html, count=1)
    # Update header strap line: 272/785/29/417 → Case_02 actual counts
    # Compute header counts inline (the helper was in a different script)
    n_nodes = len(graph.get("nodes", []))
    n_links = len(graph.get("links", []))
    n_audits = len(graph.get("audits", []))
    n_amb = (graph.get("ambiguity") or {}).get("stats_total", {}).get("cards_in_scope", 0)
    new_html = re.sub(
        r'A knowledge-graph atlas of the regulatory landscape:\s*\d+\s*nodes,\s*\d+\s*links,\s*\d+\s*audits,\s*\d+\s*ambiguity cards',
        f'A knowledge-graph atlas for SecureBorder B.V.: {n_nodes} nodes, {n_links} links, {n_audits} audits, {n_amb} ambiguity cards',
        new_html, count=1)

    # Final identity patches — broad Case 01 → Case 02
    # Use HTML-entity-tolerant replacements (the H1 uses &middot; not ·).
    new_html = new_html.replace("Case 01 &middot; Phase 1", "Case 02 &middot; Phase 1")
    new_html = new_html.replace("Case 01 · Phase 1", "Case 02 · Phase 1")
    new_html = new_html.replace("TINYTASK LDA.", "SECUREBORDER B.V.")
    new_html = new_html.replace("LISBON, PT", "THE HAGUE, NL")

    open(HTML_PATH, "w", encoding="utf-8").write(new_html)
    print(f"wrote {HTML_PATH} ({len(graph_data)} bytes JSON inlined)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))