#!/usr/bin/env python3
"""
build_alt_anchor_columns.py — ALT-ANCHOR campaign generator (v1.0)

Injects/updates the generated `800-53r5` column in the §1 unified-matrix table of the
three case framework-mapping matrices. Content = union of the NIST SP 800-53 Rev. 5
crosswalks of the PF 1.0 ids present in each row, sourced from the frozen
CONTROLS/NIST_PF/**/*.json files. The column is a GENERATED VIEW:

  * this script is the only writer;
  * re-running on an already-written file produces a zero diff (idempotent);
  * aborts without writing if any PF id lacks a JSON or any crosswalk 800-53 id is
    not in CONTROLS/NIST_80053R5/ (legacy aliases IP-3/DM-1 accepted).

Usage:  python3 scripts/build_alt_anchor_columns.py [--check]
        --check  exits 1 if a re-run would change files (drift detector).

Scope: §1 table only (main unified matrix). Secondary mirrors/cards are NOT touched.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTROLS = REPO / "00_METHODOLOGY" / "PREPROCESSING_by_domain" / "CONTROLS"

MATRICES = {
    "Case_01": REPO / "02_CASES" / "Case_01_TinyTask_SaaS" / "02_PHASE2_RULES_RICH" / "Doc19_Framework_Mapping_Matrix.md",
    "Case_02": REPO / "02_CASES" / "Case_02_SecureBorder_Solutions" / "02_PHASE2_RULES_RICH" / "Doc19_Framework_Mapping_Matrix.md",
    "Case_03": REPO / "02_CASES" / "Case_03_OmniBank_Financial" / "02_PHASE2_RULES_RICH" / "Doc20_Framework_Mapping_Matrix.md",
}

PF_RE = re.compile(r"\b(?:ID|GV|CT|CM|PR)\.(?:IM|BE|RA|DE|PO|RM|AT|MT|DM|DP|AW|AC|DS|MA|PT|IR|PS|AA)-P\d+\b")
XREF_RE = re.compile(r"SP 800-53 Rev\. 5:\s*([^\"\n]+)")
R5_ID_RE = re.compile(r"^[A-Z]{2}-[0-9]+(\([0-9]+\))?$")
LEGACY_ALIASES = {"IP-3", "DM-1"}
NEW_COL = "800-53r5"


def load_pf_xref():
    """PF subcategory id -> sorted set of 800-53r5 ids from its JSON crosswalks."""
    xref = {}
    for f in sorted(CONTROLS.glob("NIST_PF/**/*.json")):
        try:
            d = json.loads(f.read_text())
        except json.JSONDecodeError:
            continue
        sid = d.get("control_id") or d.get("subcategory_id")
        if not sid:
            continue
        refs = set()
        for item in d.get("informative_references", []):
            if "SP 800-53 Rev. 5:" not in str(item):
                continue
            for part in XREF_RE.search(str(item)).group(1).split(","):
                pid = part.strip().split(" ")[0].strip("();")
                if R5_ID_RE.match(pid):
                    refs.add(pid)
        xref[sid] = refs
    return xref


def load_r5_ids():
    ids = {}
    for f in CONTROLS.glob("NIST_80053R5/??.json"):
        for c in json.loads(f.read_text())["controls"]:
            ids[c["id"]] = c["name"]
    return ids


def cell_80053(pf_ids, xref, r5):
    out = []
    for pid in sorted(pf_ids):
        if pid not in xref:
            raise SystemExit(f"ABORT: PF id {pid} has no frozen JSON (no silent drift)")
        for r in xref[pid]:
            if r not in r5 and r not in LEGACY_ALIASES:
                raise SystemExit(f"ABORT: crosswalk id {r} (from {pid}) not in NIST_80053R5")
            if r not in out:
                out.append(r)
    return " / ".join(out) if out else "—"


def process(path, xref, r5, check_only):
    lines = path.read_text().split("\n")
    # locate §1 header: first table header line containing a PF-column marker
    hdr_idx = None
    for i, ln in enumerate(lines):
        if ln.startswith("|") and re.search(r"(Privacy FW 1\.0|Privacy FW)", ln):
            hdr_idx = i
            break
    if hdr_idx is None:
        raise SystemExit(f"ABORT: §1 header with PF column not found in {path.name}")
    hdr = [c.strip() for c in re.split(r"(?<!\\)\|", lines[hdr_idx].strip().strip("|"))]
    pf_col = next(i for i, c in enumerate(hdr) if "Privacy FW" in c)
    new_hdr = hdr

    if NEW_COL in new_hdr:
        col = new_hdr.index(NEW_COL)
        if col != pf_col + 1:
            raise SystemExit(f"ABORT: {path.name}: {NEW_COL} column in unexpected position {col}")
        mode = "update"
    else:
        new_hdr.insert(pf_col + 1, NEW_COL)
        col = pf_col + 1
        mode = "insert"

    sep_re = re.compile(r"^\|[-: |]+\|$")
    i = hdr_idx + 1
    if not sep_re.match(lines[i].strip()):
        raise SystemExit(f"ABORT: separator row not found under header in {path.name}")
    rows_changed = 0
    out = lines[:]
    # cells split on UNESCAPED pipes only (cells may contain \| literals)
    def split_row(s):
        s = s.strip().strip("|")
        return [c.strip() for c in re.split(r"(?<!\\)\|", s)]
    if mode == "insert":
        sep_parts = split_row(lines[i])
        col_char = ":" if sep_parts[min(col, len(sep_parts) - 1)].startswith(":") else "-"
        sep_parts = sep_parts[:col] + [col_char * 3] + sep_parts[col:]
        new_sep = "|" + "|".join(p if p.strip() else "---" for p in sep_parts) + "|"
    else:
        new_sep = lines[i]
    # body rows: skip blank lines inside the table block
    j = i + 1
    while j < len(lines):
        stripped = lines[j].strip()
        if stripped == "":
            j += 1
            continue
        if not stripped.startswith("|"):
            break
        cells = split_row(lines[j])
        pf_ids = set(PF_RE.findall(lines[j]))
        refs = cell_80053(pf_ids, xref, r5)
        if mode == "insert":
            new_cells = cells[:col] + [refs] + cells[col:]
        else:
            new_cells = cells
        while len(new_cells) < len(new_hdr):
            new_cells.append("—")
        if len(new_cells) > len(new_hdr):
            overflow = new_cells[len(new_hdr) - 1:]
            new_cells = new_cells[:len(new_hdr) - 1] + [" | ".join(overflow)]
        new_line = "| " + " | ".join(new_cells) + " |"
        if new_line != lines[j]:
            rows_changed += 1
        out[j] = new_line
        j += 1
    out[hdr_idx] = "| " + " | ".join(new_hdr) + " |"
    out[i] = new_sep
    result = "\n".join(out)
    if result != path.read_text():
        if check_only:
            print(f"DRIFT: {path} would change ({rows_changed} rows)")
            return False
        path.write_text(result)
        print(f"{path.name} [{path.parent.parent.parent.name}]: {mode}, {rows_changed} rows changed")
    else:
        print(f"{path.name}: zero diff (idempotent re-run)")
    return True


def main():
    check_only = "--check" in sys.argv
    xref = load_pf_xref()
    r5 = load_r5_ids()
    if not xref or not r5:
        raise SystemExit("ABORT: frozen sources not found")
    ok = all(process(p, xref, r5, check_only) for p in MATRICES.values())
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
