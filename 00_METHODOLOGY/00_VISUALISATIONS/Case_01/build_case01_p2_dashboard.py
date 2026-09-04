#!/usr/bin/env python3
"""
build_case01_p2_dashboard.py — Inline phase2_graph.json into Case_01_P2_Dashboard.html

Idempotent pattern (mirrors build_case02_dashboard.py):
  1. Read data/phase2_graph.json (must already exist; run build_p2_graph.py first).
  2. Read Case_01_P2_Dashboard.html (template).
  3. Strip any existing <script type="application/json" id="phase2-graph-data"> ... </script>.
  4. Inject fresh JSON block before </body>.
  5. Write back to same HTML path.

Usage:
    cd 02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH
    python3 scripts/build_p2_graph.py --summary
    python3 ../../../../00_METHODOLOGY/00_VISUALISATIONS/Case_01/build_case01_p2_dashboard.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent  # 00_VISUALISATIONS/Case_01/
HTML = ROOT / "Case_01_P2_Dashboard.html"
# Walk up: Case_01/ → 00_VISUALISATIONS/ → 00_METHODOLOGY/ → Methodology_compact/
GRAPH_JSON = (
        ROOT.parent.parent.parent
        / "02_CASES"
        / "Case_01_TinyTask_SaaS"
        / "02_PHASE2_RULES_RICH"
        / "data"
        / "phase2_graph.json"
)


def main() -> int:
        if not HTML.exists():
                print(f"[ERROR] HTML not found: {HTML}", file=sys.stderr)
                return 2
        if not GRAPH_JSON.exists():
                print(f"[ERROR] Graph JSON not found: {GRAPH_JSON}", file=sys.stderr)
                print("Run build_p2_graph.py first.", file=sys.stderr)
                return 2

        graph = json.loads(GRAPH_JSON.read_text(encoding="utf-8"))
        html = HTML.read_text(encoding="utf-8")

        # 1. Strip any existing JSON block (idempotent)
        pattern = re.compile(
                r'<script type="application/json" id="phase2-graph-data">[\s\S]*?</script>',
                re.MULTILINE,
        )
        html_stripped = pattern.sub("", html)

        # 2. Build fresh JSON block
        json_str = json.dumps(graph, ensure_ascii=False)
        # Escape any closing </script in JSON (defensive — JSON shouldn't have one)
        json_str_safe = json_str.replace("</", "<\\/")

        block = (
                '<script type="application/json" id="phase2-graph-data">'
                + json_str_safe
                + '</script>'
        )

        # 3. Inject before </body>
        if "</body>" not in html_stripped:
                print("[ERROR] no </body> found in HTML", file=sys.stderr)
                return 1
        html_out = html_stripped.replace("</body>", block + "\n</body>", 1)

        # 4. Write back
        HTML.write_text(html_out, encoding="utf-8")

        counts = graph.get("invariants", {}).get("counts", {})
        size_kb = HTML.stat().st_size / 1024
        print(f"[build_case01_p2_dashboard] wrote {HTML} ({size_kb:.1f} KB)")
        print(f"[build_case01_p2_dashboard] nodes={counts.get('nodes_total')} links={counts.get('links_total')} "
              f"audits={len(graph.get('audits', []))}")
        return 0


if __name__ == "__main__":
        sys.exit(main())