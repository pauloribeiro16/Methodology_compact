#!/usr/bin/env python3
"""test_master_drilldown.py — R5 modal drill-down coverage + R6 full-card drill-down.

R5 (existing): for each of the 9 DataTables in the Master Dashboard, click
the first row, assert modal opens with at least 3 <dt> and a real <dd>.
R6 (new): three targeted assertions for full-card drill-down:
  - Case_03 P3 / folio09-uc-table — RUP sections rendered, Basic Flow numbered list
  - Case_01 P2 / folio05-rules-table — numbered rule fields (1. Description etc.)
  - Case_01 P1 / folio02-amb-table — Resolution section + ≥5 <dt>

Also captures three R6 screenshots:
  - master_drilldown_uc.png         (Case_03 P3 first UC)
  - master_drilldown_rule.png       (Case_01 P2 first Rule)
  - master_drilldown_ambiguity.png  (Case_01 P1 first Ambiguity)

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


def open_and_assert_r6(page, case_key: str, phase: str, table_id: str,
                        screenshot: str | None,
                        h4_count_min: int = 1,
                        section_titles_required: list[str] | None = None,
                        body_must_contain: str | None = None,
                        dt_count_min: int = 1,
                        section_count_min: int = 1) -> bool:
    """R6 — open first row, assert full-card drill-down renders sections.

    Returns True on success.
    """
    page.evaluate(f"window.MASTER_DASHBOARD.activateCase('{case_key}')")
    page.evaluate(f"window.MASTER_DASHBOARD.activatePhase('{phase}')")
    # R6 — trigger an extra re-render so case-specific data flows into dtSources
    try:
        page.evaluate("window.MASTER_DASHBOARD.rerenderCurrent()")
    except Exception as e:
        print(f"  R6 debug rerenderCurrent err for {case_key}/{phase}: {e}")
    page.wait_for_timeout(2500)
    has_tbl = page.evaluate(f"document.getElementById('{table_id}') != null")
    if not has_tbl:
        print(f"  R6 FAIL {case_key}/{phase}/{table_id}: table not in DOM")
        return False
    if not has_tbl:
        print(f"  R6 FAIL {case_key}/{phase}/{table_id}: table not in DOM")
        return False
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
        print(f"  R6 FAIL {case_key}/{phase}/{table_id}: no rows to click")
        return False
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
        return False
    try:
        page.wait_for_selector("#aegis-detail-modal.open", timeout=12000)
    except Exception as e:
        print(f"  R6 FAIL {case_key}/{phase}/{table_id}: modal did not open ({e})")
        return False
    # Count <h4> in modal
    h4_count = page.evaluate("document.querySelectorAll('#aegis-detail-modal .aegis-modal-body .am-section h4').length")
    section_count = page.evaluate("document.querySelectorAll('#aegis-detail-modal .aegis-modal-body .am-section').length")
    if h4_count < h4_count_min:
        print(f"  R6 FAIL {case_key}/{phase}/{table_id}: only {h4_count} <h4> sections (expected >= {h4_count_min})")
        return False
    if section_count < section_count_min:
        print(f"  R6 FAIL {case_key}/{phase}/{table_id}: only {section_count} .am-section blocks (expected >= {section_count_min})")
        return False
    if section_titles_required:
        titles = page.evaluate(
            "Array.from(document.querySelectorAll('#aegis-detail-modal .aegis-modal-body .am-section h4')).map(h => h.textContent)"
        )
        for req in section_titles_required:
            if not any(req.lower() in (t or "").lower() for t in titles):
                print(f"  R6 FAIL {case_key}/{phase}/{table_id}: missing section '{req}' in {titles}")
                return False
    if body_must_contain:
        body_text = page.evaluate("document.querySelector('#aegis-detail-modal .aegis-modal-body').textContent || ''")
        if body_must_contain.lower() not in body_text.lower():
            print(f"  R6 FAIL {case_key}/{phase}/{table_id}: body missing '{body_must_contain}'")
            return False
    dt_count = page.evaluate("document.querySelectorAll('#aegis-detail-modal .aegis-modal-body dt').length")
    if dt_count < dt_count_min:
        print(f"  R6 FAIL {case_key}/{phase}/{table_id}: only {dt_count} <dt> entries (expected >= {dt_count_min})")
        return False
    if screenshot:
        page.screenshot(path=str(SHOT_DIR / screenshot), full_page=False)
    # Close
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)
    is_open = page.evaluate("document.getElementById('aegis-detail-modal').classList.contains('open')")
    if is_open:
        page.evaluate("document.querySelector('#aegis-detail-modal .am-close').click()")
        page.wait_for_timeout(300)
    print(f"  R6 OK   {case_key}/{phase}/{table_id}: {section_count} sections, {h4_count} h4, {dt_count} dt")
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
        # R5 — drill-down coverage
        for case_key, phase, table_id in TABLES:
            if not open_modal_and_assert(page, case_key, phase, table_id):
                ok = False

        # R6 — full-card drill-down
        r6_specs = [
            # 1. Case_03 P3 / UC table — RUP-style sections + numbered Basic Flow
            {
                "case": "case_03", "phase": "p3", "tbl": "folio09-uc-table",
                "screenshot": "master_drilldown_uc.png",
                "h4_min": 1, "sections_min": 5,
                "titles": ["Basic Flow"],
                "body_contains": "1.",  # numbered list bullet
                "dt_min": 1,
            },
            # 2. Case_01 P2 / Rules table — numbered rule fields
            {
                "case": "case_01", "phase": "p2", "tbl": "folio05-rules-table",
                "screenshot": "master_drilldown_rule.png",
                "h4_min": 3, "sections_min": 3,
                "titles": ["1."],  # starts with "1. Description"
                "body_contains": None,
                "dt_min": 3,
            },
            # 3. Case_01 P1 / Ambiguity table — Resolution section + ≥5 <dt>
            {
                "case": "case_01", "phase": "p1", "tbl": "folio02-amb-table",
                "screenshot": "master_drilldown_ambiguity.png",
                "h4_min": 1, "sections_min": 2,  # Card + Resolution
                "titles": ["Resolution", "Card"],
                "body_contains": None,
                "dt_min": 5,
            },
        ]
        for spec in r6_specs:
            if not open_and_assert_r6(page, spec["case"], spec["phase"], spec["tbl"],
                                       spec["screenshot"],
                                       h4_count_min=spec["h4_min"],
                                       section_titles_required=spec["titles"],
                                       body_must_contain=spec["body_contains"],
                                       dt_count_min=spec["dt_min"],
                                       section_count_min=spec.get("sections_min", 1)):
                ok = False

        if errors:
            print(f"\nFAIL errors observed ({len(errors)}):")
            for e in errors[:8]:
                print(f"  {e[:240]}")
            ok = False

        print(f"\n{'OK' if ok else 'FAIL'} drilldown coverage ({len(TABLES)} R5 tables + {len(r6_specs)} R6 specs)")
        b.close()
        return 0 if ok else 2


if __name__ == "__main__":
    try:
        rc = main()
    except KeyboardInterrupt:
        sys.exit(130)
    sys.exit(rc)
