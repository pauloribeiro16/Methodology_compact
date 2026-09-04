#!/usr/bin/env python3
"""test_dashboards.py — smoke for the static AEGIS visualisation dashboards.

Why this exists
---------------
The 9 dashboards under 00_METHODOLOGY/00_VISUALISATIONS/ are standalone HTML
files that depend on CDNs (Chart.js, ECharts, jQuery+DataTables, Google
Fonts). They are written by hand/agent with no build step and no tests.
This suite is the "lowest bar that catches breakage": for each page,
- open via file://
- wait for networkidle (tolerates slow CDNs but flags unreachable ones)
- assert the page rendered something (≥1 canvas or svg)
- collect console errors and page errors

Failures of CDNs are real failures of the dashboards — flag them.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

ROOT = Path.cwd()  # run from the repo root; the script is invoked there
VIS = ROOT / "00_METHODOLOGY" / "00_VISUALISATIONS"
TESTS_DIR = VIS / "tests"
SHOTS = TESTS_DIR / "screenshots"

# All dashboards, relative to repo root.
DASHBOARDS = sorted(p for p in (VIS).rglob("*.html"))

# --- PORT-PARITY-2 · block F3b: explicit entries ---------------------------
# The default suite discovers dashboards via rglob above; these entries pin
# the Case_03 parity dashboards so (a) they fail loudly if missing and (b)
# each carries a static Case_02-identity purge check (leaks OUTSIDE the
# inlined graph JSON blob are build failures; the blob itself is verbatim
# F3a data and may legitimately reference sibling cases in audit prose).
REQUIRED_DASHBOARDS = [
    "00_METHODOLOGY/00_VISUALISATIONS/Case_03/Case_03_P1_Dashboard.html",
    "00_METHODOLOGY/00_VISUALISATIONS/Case_03/Case_03_P1_Maturity.html",
]
CASE03_IDENTITY_TOKENS = [
    "SecureBorder", "SECUREBORDER", "Case 02", "Case_02",
    "The Hague", "GuardianGate", "TinyTask",
]


def check_case03_identity_purge() -> list[str]:
    """Return a list of purge-check failure strings (empty = pass)."""
    failures: list[str] = []
    for rel in REQUIRED_DASHBOARDS:
        path = ROOT / rel
        if not path.exists():
            failures.append(f"{rel}: file missing")
            continue
        html = path.read_text(encoding="utf-8")
        stripped = re.sub(
            r'<script type="application/json" id="phase1-graph-data">.*?</script>',
            "", html, flags=re.DOTALL)
        stripped = re.sub(
            r'<script>window\.PHASE1_GRAPH_DATA = \{.*?\};</script>',
            "", stripped, flags=re.DOTALL)
        for tok in CASE03_IDENTITY_TOKENS:
            if tok in stripped:
                failures.append(f"{rel}: identity leak outside JSON blob: {tok!r}")
    return failures


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--only", help="substring match on the dashboard path (case-insensitive)")
    p.add_argument("--no-shots", action="store_true", help="skip screenshot capture")
    p.add_argument("--timeout", type=int, default=30, help="per-page networkidle timeout (s)")
    args = p.parse_args()

    targets = DASHBOARDS
    if args.only:
        sub = args.only.lower()
        targets = [d for d in targets if sub in str(d.relative_to(ROOT)).lower()]
        if not targets:
            print(f"test_dashboards: --only {args.only!r} matched 0 dashboards")
            return 2

    if not args.no_shots:
        SHOTS.mkdir(parents=True, exist_ok=True)

    print(f"# smoke for {len(targets)} dashboard(s)")
    rows: list[dict] = []
    overall_ok = True

    # Explicit F3b entries: must exist — and, on full-suite runs, must be part
    # of the rglob discovery set (guards accidental exclusion).
    for req in REQUIRED_DASHBOARDS:
        if not (ROOT / req).exists():
            print(f"test_dashboards: REQUIRED dashboard missing: {req}")
            return 2
        if args.only is None and (ROOT / req) not in targets:
            print(f"test_dashboards: REQUIRED dashboard not in discovery set: {req}")
            return 2

    # Static identity-purge check (F3b) — independent of Playwright.
    purge_failures = check_case03_identity_purge()
    if purge_failures:
        overall_ok = False
        for f in purge_failures:
            print(f"test_dashboards: PURGE FAIL — {f}")
    else:
        print("# case03 identity purge: OK (0 Case_02 identity strings outside the inlined graph JSON)")

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1280, "height": 900})

        for html in targets:
            rel = str(html.relative_to(ROOT))
            url = html.as_uri()
            t0 = time.time()
            errors: list[tuple[str, str]] = []
            failed: list[tuple[str, str]] = []

            page = ctx.new_page()
            page.on("pageerror", lambda e: errors.append(("pageerror", str(e))))
            page.on("console", lambda m: m.type == "error" and errors.append(("console", m.text)))
            page.on("requestfailed", lambda r: failed.append((r.url, r.failure or "?")))

            try:
                page.goto(url, wait_until="networkidle", timeout=args.timeout * 1000)
            except PWTimeout:
                # networkidle is fragile with long-poll CDNs; degrade gracefully.
                errors.append(("timeout", f"networkidle not reached in {args.timeout}s"))

            # Give chart libraries a beat to initialise on top of networkidle.
            try:
                page.wait_for_timeout(500)
            except Exception:
                pass

            try:
                title = page.title()
            except Exception as e:
                title = f"<error: {e}>"
            try:
                canvases = page.locator("canvas").count()
            except Exception:
                canvases = -1
            try:
                svgs = page.locator("svg").count()
            except Exception:
                svgs = -1
            try:
                rows_in_tables = page.locator("table tbody tr").count()
            except Exception:
                rows_in_tables = -1
            try:
                body_text_len = len(page.locator("body").inner_text())
            except Exception:
                body_text_len = 0

            shot_path = None
            if not args.no_shots:
                try:
                    shot_path = SHOTS / (html.stem + ".png")
                    page.screenshot(path=str(shot_path), full_page=False)
                except Exception as e:
                    shot_path = f"<error: {e}>"

            page.close()

            # Heuristic for "rendered something meaningful":
            # - chart dashboards: >= 1 canvas or svg
            # - table dashboards:  ≥ 50 rendered rows
            # - tab/index pages:   body text ≥ 500 chars (navigation hubs)
            rendered = (
                (canvases + svgs) >= 1
                or rows_in_tables >= 50
                or body_text_len >= 500
            )
            ok = bool(title) and rendered and not [e for e in errors if e[0] == "pageerror"]
            if not ok:
                overall_ok = False

            rows.append({
                "path": rel,
                "ok": ok,
                "title": title,
                "canvases": canvases,
                "svgs": svgs,
                "rows": rows_in_tables,
                "body_text_len": body_text_len,
                "errors": errors,
                "failed_requests": failed[:5],
                "duration_s": round(time.time() - t0, 1),
                "screenshot": str(shot_path) if shot_path else None,
            })

        browser.close()

    # Render summary
    print()
    print(f"{'OK':<3} | {'TITLE':<35.35} | {'CANV':<4} | {'SVG':<3} | {'ROWS':<5} | {'ERR':<3} | {'CDN':<3} | PATH")
    print("-" * 130)
    for r in rows:
        title = (r["title"] or "")[:35]
        err = sum(1 for e in r["errors"] if e[0] == "pageerror")
        cdn = sum(1 for u, _ in r["failed_requests"] if "cdn" in u or "jsdelivr" in u or "googleapis" in u or "datatables" in u)
        mark = "✓" if r["ok"] else "✗"
        print(f"{mark}   | {title:<35.35} | {r['canvases']:<4} | {r['svgs']:<3} | {r.get('rows',0):<5} | {err:<3} | {cdn:<3} | {r['path']}")

    failures = [r for r in rows if not r["ok"]]
    if failures:
        print()
        print(f"# {len(failures)} failure(s):")
        for r in failures:
            print(f"  {r['path']}")
            for kind, msg in r["errors"]:
                print(f"    [{kind}] {msg[:200]}")
            for u, why in r["failed_requests"]:
                print(f"    [requestfailed] {u} :: {why}")
        return 1

    print()
    print(f"# all {len(rows)} dashboard(s) passed smoke")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)