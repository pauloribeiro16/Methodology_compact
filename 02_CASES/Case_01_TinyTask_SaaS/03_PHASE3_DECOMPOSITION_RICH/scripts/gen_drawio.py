#!/usr/bin/env python3
"""
gen_drawio.py — Phase 3 Rich Mode (Sprint 3, REAL)

Reads the ```mermaid``` block in `17_Functional_Tree.md` and emits a parseable
.drawio XML at `18_Functional_Tree.drawio`. Supports simple flowcharts:

    ROOT(L0) -> PKG-X(L1)
    PKG-X(L1) -> UC-A(L2)
    ROOT(L0):::root -> PKG-X(L1)

Cells are plain rounded rectangles with cell IDs and labels. Edges connect
parents to children. Output opens cleanly in VSCode's Draw.io Integration
extension.

Usage:
  python3 scripts/gen_drawio.py
  python3 scripts/gen_drawio.py --input 17_Functional_Tree.md --output 18_Functional_Tree.drawio
"""
from __future__ import annotations

import argparse
import re
import sys
import xml.sax.saxutils as su
from pathlib import Path
from typing import Dict, List, Tuple

RE_MERMAID = re.compile(r"```mermaid[^\n]*\n(.*?)```", re.DOTALL)
# node tokens like "ROOT(L0)", "PKG-DP(L1)", "UC01[L2]" or "UC01(L2)\nlabel"
RE_NODE_DEF = re.compile(r"([A-Za-z][A-Za-z0-9_\-]*)\s*(?:\[\s*([^\]]+?)\s*\]|\(\s*([^\)]+?)\s*\)|\(([^)]+)\))")
RE_EDGE = re.compile(r"([A-Za-z][A-Za-z0-9_\-]*)\s*(?:-->|->)\s*([A-Za-z][A-Za-z0-9_\-]*)")
RE_LEVEL = re.compile(r"\bL(\d+)\b")


def parse_mermaid(text: str) -> Tuple[Dict[str, Tuple[str, str]], List[Tuple[str, str]]]:
    """Return ({node_id: (label, level)}, [(src, tgt), ...])."""
    m = RE_MERMAID.search(text)
    if not m:
        raise ValueError("No mermaid code block found")
    block = m.group(1)

    nodes: Dict[str, Tuple[str, str]] = {}
    edges: List[Tuple[str, str]] = []

    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith(("graph", "flowchart", "subgraph", "end", "%%")):
            continue
        # find edges (a -> b)
        for em in RE_EDGE.finditer(line):
            edges.append((em.group(1), em.group(2)))
        # find node labels: "ID[L0 text]" or "ID(L0)"
        # Match ID followed by [ ... ] or ( ... )
        for nm in re.finditer(r"([A-Za-z][A-Za-z0-9_\-]*)\s*\[([^\]]+)\]|\b([A-Za-z][A-Za-z0-9_\-]*)\s*\(([^)]+)\)", line):
            node_id = nm.group(1) or nm.group(3)
            label = (nm.group(2) or nm.group(4) or "").strip()
            # strip surrounding quotes
            label = label.strip('"').strip("'")
            # level extraction
            lv_m = RE_LEVEL.search(label) or RE_LEVEL.search(node_id)
            level = lv_m.group(1) if lv_m else ""
            # clean label (drop "L0" marker)
            clean_label = RE_LEVEL.sub("", label).strip() or node_id
            nodes[node_id] = (clean_label, level)
    return nodes, edges


def render_drawio(nodes: Dict[str, Tuple[str, str]], edges: List[Tuple[str, str]]) -> str:
    """Render a minimal parseable .drawio XML document."""
    # layout: simple vertical grid per level
    level_x = {"0": 400, "1": 200, "2": 600, "3": 800}
    level_y_offset = {"0": 40, "1": 200, "2": 400, "3": 600}
    y_step = 60

    # Group nodes by level for vertical placement
    by_level: Dict[str, List[Tuple[str, str]]] = {}
    for nid, (lbl, lvl) in nodes.items():
        by_level.setdefault(lvl or "0", []).append((nid, lbl))

    coords: Dict[str, Tuple[int, int]] = {}
    for lvl, items in by_level.items():
        x = int(level_x.get(lvl, 1000))
        y0 = int(level_y_offset.get(lvl, 800))
        for i, (nid, _) in enumerate(items):
            coords[nid] = (x, y0 + i * y_step)

    cells: List[str] = []
    # mxfile header
    cells.append('<mxfile host="app.diagrams.net">')
    cells.append('  <diagram id="phase3-rich-functional-tree" name="Phase3 Rich Functional Tree">')
    cells.append('    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="900" math="0" shadow="0">')
    cells.append('      <root>')
    cells.append('        <mxCell id="0"/>')
    cells.append('        <mxCell id="1" parent="0"/>')

    # node cells
    for nid, (lbl, lvl) in nodes.items():
        x, y = coords.get(nid, (100, 100))
        style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;"
        if lvl == "0":
            style += "fillColor=#d5e8d4;strokeColor=#82b366;fontSize=16;fontStyle=1;"
        elif lvl == "1":
            style += "fillColor=#fff2cc;strokeColor=#d6b656;fontSize=13;fontStyle=1;"
        else:
            style += "fontSize=11;"
        label_xml = su.escape(lbl).replace("\n", "&#10;")
        cells.append(
            f'        <mxCell id="{su.escape(nid)}" value="{label_xml}" '
            f'style="{style}" vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="{y}" width="160" height="40" as="geometry"/></mxCell>'
        )

    # edge cells
    for i, (src, tgt) in enumerate(edges, start=1):
        if src not in coords or tgt not in coords:
            continue
        cells.append(
            f'        <mxCell id="e{i}" style="endArrow=classic;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" '
            f'edge="1" parent="1" source="{su.escape(src)}" target="{su.escape(tgt)}">'
            f'<mxGeometry relative="1" as="geometry"/></mxCell>'
        )

    cells.append('      </root>')
    cells.append('    </mxGraphModel>')
    cells.append('  </diagram>')
    cells.append('</mxfile>')
    return "\n".join(cells) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate .drawio from Mermaid in 17_Functional_Tree.md")
    parser.add_argument("--input", default=None,
                        help="Path to 17_Functional_Tree.md (default: ../17_Functional_Tree.md)")
    parser.add_argument("--output", default=None,
                        help="Path to output .drawio (default: ../18_Functional_Tree.drawio)")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent.parent
    input_path = Path(args.input) if args.input else base / "17_Functional_Tree.md"
    output_path = Path(args.output) if args.output else base / "18_Functional_Tree.drawio"

    text = input_path.read_text(encoding="utf-8")
    nodes, edges = parse_mermaid(text)
    if not nodes:
        print(f"[warn] no nodes parsed from {input_path}; check ```mermaid``` block exists")
        return 1
    xml = render_drawio(nodes, edges)
    output_path.write_text(xml, encoding="utf-8")
    print(f"[ok] wrote {output_path}: nodes={len(nodes)} edges={len(edges)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
