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

            # ----- R8 — P1 sub-tabs + new folios -----
            page.evaluate("window.MASTER_DASHBOARD.activatePhase('p1')")
            page.wait_for_timeout(800)
            # 1) subtab-bar present with 4 buttons
            sub_count = page.evaluate("document.querySelectorAll('#panel-p1 .sub-tab').length")
            print(f"  {ck}/R8 sub-tab buttons: {sub_count}", "OK" if sub_count == 4 else "FAIL")
            if sub_count != 4: ok = False
            # 2) click each sub-tab and verify the matching sub-panel becomes .active
            for letter in ("a", "b", "c", "d"):
                page.evaluate(
                    f"document.querySelector('#panel-p1 .sub-tab[data-sub=\"{letter}\"]').click()"
                )
                page.wait_for_timeout(400)
                active = page.evaluate(
                    f"document.querySelector('#panel-p1 .sub-panel[data-sub=\"{letter}\"]').classList.contains('active')"
                )
                ok_str = "OK" if active else "FAIL"
                print(f"  {ck}/R8 sub-tab '{letter}' active: {ok_str}")
                if not active: ok = False
            # 3) expected folios per sub-panel
            folio_checks = {
                "b": "folio07-controls-table",
                "c": "folio11-gaps-table",
                "d": "folio14-goals-table",
            }
            for letter, fid in folio_checks.items():
                page.evaluate(
                    f"document.querySelector('#panel-p1 .sub-tab[data-sub=\"{letter}\"]').click()"
                )
                page.wait_for_timeout(400)
                fid_present = page.evaluate(f"document.getElementById('{fid}') != null")
                print(f"  {ck}/R8 folio {fid}: present={fid_present}", "OK" if fid_present else "FAIL")
                if not fid_present: ok = False
            # 4) widget counts per sub-tab
            page.evaluate("document.querySelector('#panel-p1 .sub-tab[data-sub=\"b\"]').click()")
            page.wait_for_timeout(800)
            js_query = (
                "(function(){var c=MASTER_DATA.cases['" + KEY_MAP[ck] + "'].phases.P1;"
                "return {"
                " controls: (c.nist_controls && c.nist_controls.controls) ? c.nist_controls.controls.length : 0,"
                " gaps:     (c.posture_gaps && c.posture_gaps.gaps) ? c.posture_gaps.gaps.length : 0,"
                " goals:    (c.adjusted_goals && c.adjusted_goals.goals) ? c.adjusted_goals.goals.length : 0"
                "};})()"
            )
            counts = page.evaluate(js_query)
            print(f"  {ck}/R8 controls={counts['controls']}, gaps={counts['gaps']}, goals={counts['goals']}")
            # C3 should have many controls (>5); C1/C2 may have 0 (their Doc13 has no NIST table).
            if ck == "case_03" and counts['controls'] < 5:
                ok = False
            if counts['gaps'] < 1: ok = False
            if counts['goals'] < 1: ok = False

            # ----- R8 — 3 screenshots per case (Overview / Controls / Ambiguity) -----
            page.evaluate("document.querySelector('#panel-p1 .sub-tab[data-sub=\"a\"]').click()")
            page.wait_for_timeout(800)
            page.screenshot(path=str(SHOT_DIR / f"master_{ck}_p1_overview.png"), full_page=False)
            page.evaluate("document.querySelector('#panel-p1 .sub-tab[data-sub=\"b\"]').click()")
            page.wait_for_timeout(800)
            page.screenshot(path=str(SHOT_DIR / f"master_{ck}_p1_controls.png"), full_page=False)
            page.evaluate("document.querySelector('#panel-p1 .sub-tab[data-sub=\"c\"]').click()")
            page.wait_for_timeout(800)
            page.screenshot(path=str(SHOT_DIR / f"master_{ck}_p1_ambiguity.png"), full_page=False)

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
