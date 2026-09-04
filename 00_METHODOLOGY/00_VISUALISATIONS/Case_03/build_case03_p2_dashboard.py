#!/usr/bin/env python3
"""
build_case03_p2_dashboard.py — Build Case_03_P2_Dashboard.html (PORT-PARITY-2 F4)

Mirrors build_case01_p2_dashboard.py's idempotent inliner pattern, extended with
an identity-patch stage (same discipline as F3's build_case03_dashboard.py and
the sibling build_case02_p2_dashboard.py):

  1. Read Case_01_P2_Dashboard.html (the F4 content-wave template).
  2. Strip any existing inlined phase2-graph-data JSON (idempotence).
  3. Apply the Case_01 → Case_03 identity/number replacement table — every
     entry asserts its expected occurrence count; a miss aborts the build.
     All numbers are the MECHANICAL counts from Case_03's
     data/phase2_graph.json (38 OBL / 38 OBJ on the AG- id space / 78 CTRL /
     5 TENS / 10 obligation orphans via the AG chain, AUD-P2-005b).
  4. Inline Case_03's data/phase2_graph.json before </body>.
  5. Write Case_03_P2_Dashboard.html.

Usage:
    python3 00_METHODOLOGY/00_VISUALISATIONS/Case_03/build_case03_p2_dashboard.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # 00_VISUALISATIONS/Case_03/
TEMPLATE = HERE.parent / "Case_01" / "Case_01_P2_Dashboard.html"
OUT_HTML = HERE / "Case_03_P2_Dashboard.html"
GRAPH_JSON = (
        HERE.parent.parent.parent
        / "02_CASES" / "Case_03_OmniBank_Financial"
        / "02_PHASE2_RULES_RICH" / "data" / "phase2_graph.json"
)

# ---------------------------------------------------------------------------
# Identity / number replacement table (old, new, expected_count)
# ---------------------------------------------------------------------------
R: list[tuple[str, str, int]] = [
    # --- head / masthead identity ---
    ("<title>Case 01 · Phase 2 — Dashboard · Security Posture (CSF 2.0 strict)</title>",
     "<title>Case 03 · Phase 2 — Dashboard · Security Posture (CSF 2.0 strict)</title>", 1),
    ('<div class="seal">01</div>', '<div class="seal">03</div>', 1),
    ("<h1>Case 01 &middot; Phase 2 &mdash; Security Posture (CSF 2.0 strict)</h1>",
     "<h1>Case 03 &middot; Phase 2 &mdash; Security Posture (CSF 2.0 strict)</h1>", 1),
    ("<div class=\"sub\">TinyTask Lda. &middot; Lisbon, PT &middot; AEGIS Phase 2 Rich Mode</div>",
     "<div class=\"sub\">OmniBank Financial Systems S.A. &middot; Frankfurt, DE &middot; AEGIS Phase 2 Rich Mode</div>", 1),
    ("<div><strong>Auditors</strong> AUD-P2-005 (orphan)</div>",
     "<div><strong>Auditors</strong> AUD-P2-005/005b (orphans) &middot; dual tension id space: AUD-P2-009</div>", 1),

    # --- static strap (no-JS fallback; numbers = mechanical counts) ---
    ("<div class=\"strap\" id=\"header-strap\">— AEGIS Phase 2 — 34 obligations, 31 objectives, 46 controls, 4 tensions, 4 orphan obligations (AUD-P2-005).</div>",
     "<div class=\"strap\" id=\"header-strap\">— AEGIS Phase 2 — 38 obligations, 38 objectives (AG- id space), 78 controls, 5 tensions, 10 orphan obligations (AUD-P2-005b, AG chain).</div>", 1),

    # --- Folio asides (row counts + source sections) ---
    ("<span class=\"aside\">34 rows &middot; Doc14 &sect;5</span>",
     "<span class=\"aside\">38 rows &middot; Doc15</span>", 1),
    ("<span class=\"aside\">46 rows &middot; Doc18 port</span>",
     "<span class=\"aside\">78 rows &middot; Doc19 port</span>", 1),
    ("<span class=\"aside\">31 rows &middot; Doc16 &sect;6</span>",
     "<span class=\"aside\">38 rows &middot; Doc17 &sect;3/&sect;4 (AG)</span>", 1),
    ("<span class=\"aside\">4 rows &middot; Doc15 &sect;5</span>",
     "<span class=\"aside\">5 rows &middot; Doc16 &sect;4</span>", 1),

    # --- KPI card subs (source-doc refs per case) ---
    ("<div class=\"sub\">Doc14 &sect;5 &middot; per AEGIS sub-domain</div>",
     "<div class=\"sub\">Doc15 &middot; per AEGIS sub-domain</div>", 1),
    ("<div class=\"sub\">Doc15 &sect;5</div>",
     "<div class=\"sub\">Doc16 &sect;4</div>", 1),
    ("Compare with P1 Folio I for context (P1 lists 2/5 applicable).",
     "Compare with P1 Folio I for context (Case_03 P1 lists 5/5 applicable).", 1),

    # --- orphan pane (Folio I) ---
    ("<p class=\"mat-pane-sub\">These obligations have no <code>ComplianceRule</code> addressing them. Mitigation: <code>BPR-D-07.2-001</code> covers D-07.2 with <code>N/A</code> marker. Carried from F-07 (Sprint 6+).</p>",
     "<p class=\"mat-pane-sub\">Obligations with no <code>ComplianceRule</code> addressing them via the Case_03 AG chain (control_set@related_goals → Doc17 objective → source obligation): mechanically <strong>10</strong> (AUD-P2-005b). Contributing factor: 26 AG ids referenced by <code>related_goals</code> have no Doc17 objective row (AUD-P2-007), so those CRs contribute no obligation coverage.</p>", 1),

    # --- Folio VIII KPI sub ---
    ("<div class=\"sub\">Doc14 &sect;5 &middot; 4 orphans (AUD-P2-005)</div>",
     "<div class=\"sub\">Doc15 &middot; 10 orphans (AUD-P2-005b)</div>", 1),

    # --- footer identity ---
    ("<div>AEGIS Case_01 &middot; Phase 2 &middot; Security Posture &middot; <code id=\"foot-gen\">—</code></div>",
     "<div>AEGIS Case_03 &middot; Phase 2 &middot; Security Posture &middot; <code id=\"foot-gen\">—</code></div>", 1),

    # --- JS: strap fallbacks (identity + mechanical numbers) + dynamic orphan tail ---
    ('(COMPANY.name || "TinyTask Lda.") + " · " +',
     '(COMPANY.name || "OmniBank Financial Systems S.A.") + " · " +', 1),
    ('(COMPANY.jurisdiction || "Lisbon, PT") + " · " +',
     '(COMPANY.jurisdiction || "Frankfurt, DE") + " · " +', 1),
    ('(INV.obligations_total || 34) + " obligations, " +',
     '(INV.obligations_total || 38) + " obligations, " +', 1),
    ('(INV.objectives_total || 31) + " objectives, " +',
     '(INV.objectives_total || 38) + " objectives (AG), " +', 1),
    ('(INV.controls_total || 46) + " controls, " +',
     '(INV.controls_total || 78) + " controls, " +', 1),
    ('(INV.tensions_total || 4) + " tensions, " +',
     '(INV.tensions_total || 5) + " tensions, " +', 1),
    ('"4 orphans (AUD-P2-005).";',
     'oblOrphanN + " orphan obligations (AUD-P2-005b).";', 1),

    # --- JS: obligation-orphan selection (audit-kind aware; C1 took audits[0]) ---
    ("    const strap = $(\"header-strap\");",
     "    // Obligation-coverage orphans only (AUD-P2-005 / AUD-P2-005b scheme)\n"
     "    const oblOrphanN = (G.audits || [])\n"
     "      .filter(a => /^AUD-P2-005b?$/.test(a.id) && /obligation/i.test(a.title))\n"
     "      .reduce((s, a) => s + (a.node_ids || []).length, 0);\n"
     "    const strap = $(\"header-strap\");", 1),
    ("    const orphans = (G.audits && G.audits.length && arrify(G.audits[0].node_ids)) || [];",
     "    const orphans = arrify(((G.audits || []).find(a => /^AUD-P2-005b?$/.test(a.id) && /obligation/i.test(a.title)) || {}).node_ids) || [];", 1),
    ("    const orphanCount = (G.audits || []).reduce((acc, a) => acc + ((a.node_ids || []).length), 0);",
     "    const orphanCount = orphans.length; // obligation-coverage orphans only", 1),
    ('orphanCount + " obligations have no CR (mitigated by BPR-D-07.2-001 with N/A marker).";',
     'orphanCount + " obligations have no CR via the AG chain (AUD-P2-005b).";', 1),

    # --- JS: orphan-count fallbacks (C1 hard-coded its own 4) ---
    ('$("mat-count-orphans").textContent = orphans.length || 4;',
     '$("mat-count-orphans").textContent = orphans.length;', 1),
    ('$("mat-kpi-gap").textContent = orphans.length || 4;',
     '$("mat-kpi-gap").textContent = orphans.length;', 1),

    # --- JS: date fallback ---
    ('(G.meta && G.meta.generated_date) || "2026-08-31";',
     '(G.meta && G.meta.generated_date) || "2026-09-04";', 1),

    # --- JS: source documents (per-case corpus) ---
    ('''    const sources = [
      { id: "Doc14_Obligation_Derivation.md", desc: "30 obligation cards × 17 fields (post-Sprint 6+ fix: 34 total)" },
      { id: "Doc15_Strategic_Tensions_Report.md", desc: "4 tensions (T-001, T-M-001, T-M-002, T-L-001)" },
      { id: "Doc16_Privacy_Security_Objectives.md", desc: "11 PO + 20 SO × 17 fields" },
      { id: "Doc17_Privacy_Security_Goals_NIST_Implications.md", desc: "PO → CSF; SO → CSF + PF (AI RMF N/A)" },
      { id: "Doc18_Rules_Catalog.md", desc: "30 CR + 16 BPR × 24 fields" },
      { id: "control_set.yaml", desc: "Doc18 port (machine-readable; source-of-truth for builder)" }
    ];''',
     '''    const sources = [
      { id: "Doc15_Obligation_Derivation.md", desc: "38 obligation canonical rows" },
      { id: "Doc16_Strategic_Tensions_Report.md", desc: "5 tensions (4 cards TENSION-{H,M,L}-NNN + T-005 §4.1 note; AUD-P2-009)" },
      { id: "Doc17_Privacy_Security_Objectives.md", desc: "12 PO + 26 SO canonical AG rows (§3/§4; doc summaries claim 11/22 — AUD-P2-010)" },
      { id: "Doc18_Privacy_Security_Goals_NIST_Implications.md", desc: "AG → CSF/PF/AI RMF implications" },
      { id: "Doc19_Rules_Catalog.md", desc: "38 CR + 40 BPR (78 controls; the '**' assert)" },
      { id: "control_set.yaml", desc: "Doc19 port (machine-readable; P2 ROOT canonical; source-of-truth for builder)" }
    ];''', 1),

    # --- JS: source link path ---
    ("02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/",
     "02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/", 1),

    # --- CSS: CRITICAL severity pill (C3 tension severities include CRITICAL) ---
    (".p2-table .severity-HIGH { background: rgba(138,42,42,0.10); color: var(--bad); font-weight: 600; }",
     ".p2-table .severity-HIGH { background: rgba(138,42,42,0.10); color: var(--bad); font-weight: 600; }\n"
     ".p2-table .severity-CRITICAL { background: rgba(138,42,42,0.18); color: var(--bad); font-weight: 700; }", 1),
    (".drill-detail .severity-pill-HIGH { background: rgba(138,42,42,0.18); color: var(--bad); font-weight: 700; }",
     ".drill-detail .severity-pill-HIGH { background: rgba(138,42,42,0.18); color: var(--bad); font-weight: 700; }\n"
     ".drill-detail .severity-pill-CRITICAL { background: rgba(138,42,42,0.24); color: var(--bad); font-weight: 700; }", 1),
]


def main() -> int:
    if not TEMPLATE.exists():
        print(f"[ERROR] template not found: {TEMPLATE}", file=sys.stderr)
        return 2
    if not GRAPH_JSON.exists():
        print(f"[ERROR] graph JSON not found: {GRAPH_JSON}\n"
              "Run scripts/build_p2_graph.py first.", file=sys.stderr)
        return 2

    html = TEMPLATE.read_text(encoding="utf-8")
    html = re.sub(r'<script type="application/json" id="phase2-graph-data">[\s\S]*?</script>',
                  "", html)

    for old, new, n in R:
        found = html.count(old)
        if found != n:
            print(f"[ERROR] replacement expects {n} occurrence(s), found {found}:\n"
                  f"  {old[:100]}...", file=sys.stderr)
            return 1
        html = html.replace(old, new)

    graph = json.loads(GRAPH_JSON.read_text(encoding="utf-8"))
    json_str = json.dumps(graph, ensure_ascii=False).replace("</", "<\\/")
    block = ('<script type="application/json" id="phase2-graph-data">'
             + json_str + '</script>')
    if "</body>" not in html:
        print("[ERROR] no </body> found", file=sys.stderr)
        return 1
    html = html.replace("</body>", block + "\n</body>", 1)
    OUT_HTML.write_text(html, encoding="utf-8")

    counts = graph.get("invariants", {}).get("counts", {})
    print(f"[build_case03_p2_dashboard] wrote {OUT_HTML} ({OUT_HTML.stat().st_size / 1024:.1f} KB)")
    print(f"[build_case03_p2_dashboard] nodes={counts.get('nodes_total')} "
          f"links={counts.get('links_total')} audits={len(graph.get('audits', []))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
