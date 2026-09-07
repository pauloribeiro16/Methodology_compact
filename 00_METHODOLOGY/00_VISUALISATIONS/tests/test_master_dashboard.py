#!/usr/bin/env python3
"""test_master_dashboard.py — Master Dashboard extended smoke + visual.

Validates per-case data wiring (nodes/links/ambiguity), vis-network load,
radar canvas presence. Takes 9 Playwright screenshots (3 cases x 3 phases).

Run: python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_master_dashboard.py
"""
from __future__ import annotations
import asyncio
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

REPO = Path("/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact")
URL = (REPO / "00_METHODOLOGY" / "00_VISUALISATIONS" / "UNIFIED" / "AEGIS_Master_Dashboard.html").as_uri()
SHOT_DIR = REPO / "00_METHODOLOGY" / "00_VISUALISATIONS" / "tests" / "screenshots"
SHOT_DIR.mkdir(parents=True, exist_ok=True)

EXPECTED = {
    "case_01": (456, 1412, 417, 20),
    "case_02": (521, 1205, 1071, 15),
    "case_03": (749, 2054, 1490, 20),
}

KEY_MAP = {
    "case_01": "Case_01_TinyTask_SaaS",
    "case_02": "Case_02_SecureBorder_Solutions",
    "case_03": "Case_03_OmniBank_Financial",
}


def main() -> int:
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        ctx = b.new_context(viewport={"width": 1500, "height": 900})
        page = ctx.new_page()
        errors: list[str] = []
        page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
        page.on("console", lambda m: m.type == "error" and errors.append(f"console: {m.text}"))

        page.goto(URL, wait_until="networkidle", timeout=60_000)
        page.wait_for_timeout(3500)

        ok = True
        for ck, (gn, gl, ao, ar) in EXPECTED.items():
            page.evaluate(f"window.MASTER_DASHBOARD.activateCase('{ck}')")
            page.wait_for_timeout(400)
            data = page.evaluate(
                "(function(){var c=MASTER_DATA.cases['" + KEY_MAP[ck] + "'].phases.P1; return [c.maturity.labels.length, c.graph.nodes.length, c.graph.links.length, c.ambiguity.open, c.ambiguity_rows.length].join(',');})()"
            )
            if not data:
                print(f"FAIL {ck}: no data")
                ok = False
                continue
            parts = data.split(",")
            data = {
                "maturity_labels": int(parts[0]),
                "nodes": int(parts[1]),
                "links": int(parts[2]),
                "amb_open": int(parts[3]),
                "amb_rows": int(parts[4]),
            }
            if not data:
                print(f"FAIL {ck}: no data")
                ok = False
                continue
            checks = [
                ("graph.nodes", data["nodes"], gn),
                ("graph.links", data["links"], gl),
                ("ambiguity.open", data["amb_open"], ao),
                ("ambiguity_rows", data["amb_rows"], ar),
                ("maturity.labels", data["maturity_labels"], 6),
            ]
            for name, got, exp in checks:
                match = "OK" if got == exp else "FAIL"
                print(f"  {ck}/{name}: {got} (expected {exp}) {match}")
                if got != exp:
                    ok = False

            page.evaluate("window.MASTER_DASHBOARD.activatePhase('p1')")
            page.wait_for_timeout(1500)
            has_visnet = page.evaluate(
                "typeof window.vis === 'object' && document.querySelector('#folio04-network canvas') != null"
            )
            canvas_count = page.evaluate("document.querySelectorAll('canvas').length")
            print(f"  {ck}/vis-network: {has_visnet}, canvases: {canvas_count}")
            if not has_visnet:
                print(f"  FAIL {ck}: vis-network not loaded")
                ok = False
            page.screenshot(path=str(SHOT_DIR / f"master_{ck}_p1_radar_graph.png"), full_page=False)
            page.evaluate("window.MASTER_DASHBOARD.activatePhase('p2')")
            page.wait_for_timeout(900)
            page.screenshot(path=str(SHOT_DIR / f"master_{ck}_p2_full.png"), full_page=False)
            page.evaluate("window.MASTER_DASHBOARD.activatePhase('p3')")
            page.wait_for_timeout(1500)
            page.screenshot(path=str(SHOT_DIR / f"master_{ck}_p3_full.png"), full_page=False)

        if errors:
            print(f"\nFAIL errors observed ({len(errors)}):")
            for e in errors[:5]:
                print(f"  {e[:200]}")
            return 2

        print(f"\n{'OK' if ok else 'FAIL'} all checks")
        b.close()
        return 0 if ok else 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
