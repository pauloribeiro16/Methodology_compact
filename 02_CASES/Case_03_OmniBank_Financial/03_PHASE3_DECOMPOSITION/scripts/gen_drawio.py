#!/usr/bin/env python3
"""
gen_drawio.py — Phase 3 Rich Mode functional-tree diagram, Case_03 (OmniBank
Solutions). PORT-PARITY-2 block F5 port of Case_01's script of the same name.

Reads the ```mermaid``` block in Doc28_Functional_Tree.md and emits a parseable
.drawio XML at 18_Functional_Tree.drawio (Doc27 frontmatter already lists
`18_Functional_Tree.drawio` under outputs; the file did not exist until now —
nothing is overwritten).

Usage:
  python3 scripts/gen_drawio.py
  python3 scripts/gen_drawio.py --input Doc28_Functional_Tree.md --output 18_Functional_Tree.drawio
"""
from __future__ import annotations

import argparse
import re
import sys
import xml.sax.saxutils as su
from pathlib import Path
from typing import Dict, List, Tuple

RE_MERMAID = re.compile(r"```mermaid[^\n]*\n(.*?)```", re.DOTALL)
RE_EDGE = re.compile(r"([A-Za-z][A-Za-z0-9_\-]*)\s*(?:-->|->)\s*\[?([A-Za-z][A-Za-z0-9_\-]*)")
RE_NODE_DEF = re.compile(r"([A-Za-z][A-Za-z0-9_\-]*)\s*(?:\[[^\]]*\]|\([^\)]*\))")


def parse_mermaid(text: str) -> Tuple[Dict[str, str], List[Tuple[str, str]]]:
    """Return ({node_id: label}, [(src, tgt), ...]) from the first mermaid block."""
    m = RE_MERMAID.search(text)
    if not m:
        raise ValueError("No mermaid code block found")
    block = m.group(1)

    nodes: Dict[str, str] = {}
    edges: List[Tuple[str, str]] = []

    def note(nid: str, raw: str) -> None:
        label = raw.strip().strip('"').strip("'")
        nodes.setdefault(nid, label or nid)

    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith(("graph", "flowchart", "subgraph", "end", "%%")):
            continue
        # edges: A --> B[label ...]  (label may contain spaces/brackets)
        for em in re.finditer(r"([A-Za-z][A-Za-z0-9_\-]*)\s*-->\s*([A-Za-z][A-Za-z0-9_\-]*)(\[([^\]]*)\])?", line):
            src, tgt, _, lbl = em.groups()
            edges.append((src, tgt))
            note(tgt, lbl or "")
            note(src, "")
        # standalone node definitions with labels
        for nm in re.finditer(r"\b([A-Za-z][A-Za-z0-9_\-]*)\s*\[([^\]]+)\]", line):
            note(nm.group(1), nm.group(2))
    # strip mermaid class/syntax residue from labels
    clean: Dict[str, str] = {}
    for nid, lbl in nodes.items():
        lbl = re.sub(r":::\w+", "", lbl)
        lbl = lbl.replace("[T]", " [T]").replace("[P]", " [P]").replace("[P→T]", " [P→T]")
        # Case_03 mermaid nests track tags inside node brackets: '[D-01: ... [T]]' — re-close them
        lbl = re.sub(r"\s*\[T$", " [T]", lbl)
        lbl = re.sub(r"\s*\[P$", " [P]", lbl)
        lbl = re.sub(r"\s*\[P→T$", " [P→T]", lbl)
        clean[nid] = lbl.strip() or nid
    return clean, edges


def render_drawio(nodes: Dict[str, str], edges: List[Tuple[str, str]]) -> str:
    """Render a minimal parseable .drawio XML document (level-grid layout)."""
    by_root: Dict[str, List[str]] = {}
    for src, tgt in edges:
        by_root.setdefault(src, []).append(tgt)

    coords: Dict[str, Tuple[int, int]] = {}
    coords["ROOT"] = (520, 40)

    roots = [n for n in nodes if n != "ROOT" and any(s == "ROOT" for s, t in edges if t == n)]
    x = 40
    for root in roots:
        coords[root] = (x, 160)
        x += 300
        y = 280
        for child in by_root.get(root, []):
            coords[child] = (coords[root][0] - 40, y)
            y += 60

    for nid in nodes:
        coords.setdefault(nid, (40 + (len(coords) % 8) * 160, 800))

    cells: List[str] = []
    cells.append('<mxfile host="app.diagrams.net">')
    cells.append('  <diagram id="case03-phase3-functional-tree" name="Case_03 Functional Tree">')
    cells.append('    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="1000" math="0" shadow="0">')
    cells.append('      <root>')
    cells.append('        <mxCell id="0"/>')
    cells.append('        <mxCell id="1" parent="0"/>')

    for nid, lbl in nodes.items():
        x_, y_ = coords.get(nid, (100, 100))
        style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;"
        if nid == "ROOT":
            style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=14;fontStyle=1;"
            w, h = 260, 50
        elif any(s == "ROOT" for s, t in edges if t == nid):
            style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;fontStyle=1;"
            w, h = 220, 46
        else:
            w, h = 240, 36
        label_xml = su.escape(lbl).replace("\n", "&#10;")
        cells.append(
            f'        <mxCell id="{su.escape(nid)}" value="{label_xml}" '
            f'style="{style}" vertex="1" parent="1">'
            f'<mxGeometry x="{x_}" y="{y_}" width="{w}" height="{h}" as="geometry"/></mxCell>'
        )

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
    parser = argparse.ArgumentParser(description="Generate .drawio from Mermaid in Doc28_Functional_Tree.md (Case_02)")
    parser.add_argument("--input", default=None, help="Path to functional-tree .md (default: ../Doc28_Functional_Tree.md)")
    parser.add_argument("--output", default=None, help="Output .drawio (default: ../18_Functional_Tree.drawio)")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent.parent
    input_path = Path(args.input) if args.input else base / "Doc28_Functional_Tree.md"
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
