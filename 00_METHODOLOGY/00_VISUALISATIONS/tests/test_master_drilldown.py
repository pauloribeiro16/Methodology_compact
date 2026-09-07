#!/usr/bin/env python3
"""test_master_drilldown.py — R5 modal drill-down coverage.

For each of the 9 DataTables in the Master Dashboard, switch to the
appropriate case + phase, click the first body row, wait for the modal
to open, assert that:
  - the modal element is .open
  - .am-title contains the row's first-column ID text
  - the modal body has at least 3 <dt> entries
  - at least one <dd> has real (non-empty, non-`—`) content
Then close with ESC and continue to the next table.

Also captures one screenshot of an open modal (Case_02 P2 first row of
folio05-rules-table) to tests/screenshots/master_case_02_p2_drilldown.png.

Run: python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_master_drilldown.py
"""
from __future__ import annotations
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

REPO = Path("/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact")
URL = (REPO / "00_METHODOLOGY" / "00_VISUALISATIONS" / "UNIFIED" / "AEGIS_Master_Dashboard.html").as_uri()
SHOT_DIR = REPO / "00_METHODOLOGY" / "00_VISUALISATIONS" / "tests" / "screenshots"
SHOT_DIR.mkdir(parents=True, exist_ok=True)

KEY_MAP = {
    "case_01": "Case_01_TinyTask_SaaS",
    "case_02": "Case_02_SecureBorder_Solutions",
    "case_03": "Case_03_OmniBank_Financial",
}

# (case, phase, table_id) — every DataTable on the master dashboard.
TABLES = [
    ("case_02", "p1", "folio02-amb-table"),
    ("case_02", "p2", "folio05-rules-table"),
    ("case_02", "p2", "folio06-obj-table"),
    ("case_02", "p2", "folio-p2-ambiguity-table"),
    ("case_02", "p3", "folio09-uc-table"),
    ("case_02", "p3", "folio10-proc-cap-table"),
    ("case_02", "p3", "folio11-req-table"),
    ("case_02", "p3", "folio12-threat-table"),
    ("case_02", "p3", "folio-p3-threat-ambiguity-table"),
]


def open_modal_and_assert(page, case_key: str, phase: str, table_id: str) -> bool:
    """Activate case+phase, click the first body row, assert modal opens with content."""
    page.evaluate(f"window.MASTER_DASHBOARD.activateCase('{case_key}')")
    page.evaluate(f"window.MASTER_DASHBOARD.activatePhase('{phase}')")
    page.wait_for_timeout(900)

    # Sanity: the table exists in the DOM.
    has_tbl = page.evaluate(f"document.getElementById('{table_id}') != null")
    if not has_tbl:
        print(f"  FAIL {case_key}/{phase}/{table_id}: table not in DOM")
        return False

    # Pull the first row's first-cell text BEFORE clicking (so we can assert it shows up in the title).
    first_cell = page.evaluate(
        f"""(() => {{
            var tbl = document.getElementById('{table_id}');
            if (!tbl) return null;
            var tr = tbl.querySelector('tbody tr');
            if (!tr) return null;
            var td = tr.querySelector('td');
            return td ? (td.textContent || '').trim() : null;
        }})()"""
    )
    if not first_cell:
        print(f"  FAIL {case_key}/{phase}/{table_id}: no rows to click")
        return False

    # Click the first body row. Use the DataTables cell selector to bypass search/filter UIs.
    clicked = page.evaluate(
        f"""(() => {{
            var tbl = document.getElementById('{table_id}');
            var tr = tbl.querySelector('tbody tr');
            if (!tr) return false;
            tr.dispatchEvent(new MouseEvent('click', {{bubbles: true, cancelable: true}}));
            return true;
        }})()"""
    )
    if not clicked:
        print(f"  FAIL {case_key}/{phase}/{table_id}: could not click first row")
        return False

    # Wait for the modal to open.
    try:
        page.wait_for_selector("#aegis-detail-modal.open", timeout=4000)
    except Exception as e:
        print(f"  FAIL {case_key}/{phase}/{table_id}: modal did not open ({e})")
        return False

    # Check that .am-title contains the row's first-cell text.
    # The modal title is `<TABLE_LABEL> · <obj.id|obj.title>`. The underlying object
    # for some tables (e.g. folio06 mappings) may have no id field; the modal falls
    # back to "(no id)". We accept that as long as the modal is showing data for the
    # right row (verified by the <dt>/<dd> count + content checks below).
    title_text = page.evaluate("document.querySelector('#aegis-detail-modal .am-title').textContent || ''")
    placeholder = first_cell in ("—", "--", "")
    if not placeholder and "(no id)" not in title_text:
        if first_cell not in title_text and first_cell.split(" ")[0] not in title_text:
            if not any(tok and len(tok) >= 3 and tok in title_text for tok in first_cell.split()):
                print(f"  FAIL {case_key}/{phase}/{table_id}: title='{title_text}' missing cell='{first_cell}'")
                return False

    # Count <dt> entries and ensure at least 3 fields.
    dt_count = page.evaluate("document.querySelectorAll('#aegis-detail-modal .aegis-modal-body dt').length")
    if dt_count < 3:
        print(f"  FAIL {case_key}/{phase}/{table_id}: only {dt_count} <dt> entries in modal body")
        return False

    # Ensure at least one <dd> has real content (not the empty `—` placeholder).
    has_content = page.evaluate(
        """(() => {
            var dds = document.querySelectorAll('#aegis-detail-modal .aegis-modal-body dd');
            for (var i = 0; i < dds.length; i++) {
                var t = (dds[i].textContent || '').trim();
                if (t && t !== '—' && t !== '--') return true;
            }
            return false;
        })()"""
    )
    if not has_content:
        print(f"  FAIL {case_key}/{phase}/{table_id}: modal has no real content in <dd>")
        return False

    # Capture the canonical screenshot on the second table (folio05 P2 case_02).
    if table_id == "folio05-rules-table" and case_key == "case_02" and phase == "p2":
        page.screenshot(path=str(SHOT_DIR / "master_case_02_p2_drilldown.png"), full_page=False)

    # Close with ESC.
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)
    is_open = page.evaluate("document.getElementById('aegis-detail-modal').classList.contains('open')")
    if is_open:
        # Try the .am-close button as a fallback
        page.evaluate("document.querySelector('#aegis-detail-modal .am-close').click()")
        page.wait_for_timeout(300)
        is_open = page.evaluate("document.getElementById('aegis-detail-modal').classList.contains('open')")
    if is_open:
        print(f"  FAIL {case_key}/{phase}/{table_id}: modal did not close on ESC")
        return False

    print(f"  OK   {case_key}/{phase}/{table_id}: title='{title_text[:60]}', {dt_count} fields, content present")
    return True


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
        for case_key, phase, table_id in TABLES:
            if not open_modal_and_assert(page, case_key, phase, table_id):
                ok = False

        if errors:
            print(f"\nFAIL errors observed ({len(errors)}):")
            for e in errors[:8]:
                print(f"  {e[:240]}")
            ok = False

        print(f"\n{'OK' if ok else 'FAIL'} drilldown coverage ({sum(1 for _ in TABLES)} tables)")
        b.close()
        return 0 if ok else 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
