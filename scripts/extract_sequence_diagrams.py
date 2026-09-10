#!/usr/bin/env python3
"""
extract_sequence_diagrams.py — move inline sequenceDiagram blocks from the UC
catalogs to `annexes/B_Sequence_Diagrams.md` (one per case), leaving a 1-line
pointer in the catalogue card (rubric v1.7 §5C.5).

WARNING (2026-09-10, rubric v1.11): catalogue cards now EMBED derived verbatim
copies of their sequence diagrams (the pointer line is retired). Running this
script with --apply on the current catalogues would STRIP those embedded copies
and re-insert pointer lines, regressing the embed decision. The annexes remain
the editable sources; embeds must stay byte-identical to them. Do not run
against the post-v1.11 catalogues unless intentionally reverting the decision.

Usage:
  python3 scripts/extract_sequence_diagrams.py <Case_01|Case_02|Case_03|all> [--apply]

Idempotent: re-running on an already-extracted catalog finds 0 blocks.
Only sequenceDiagram blocks are touched (flowcharts §5C.4 are lane-card content,
not catalog content).
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

CASES = {
    "Case_01": {
        "catalog": REPO / "02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/Doc20_Use_Cases_Catalog.md",
        "annex": REPO / "02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/annexes/B_Sequence_Diagrams.md",
    },
    "Case_02": {
        "catalog": REPO / "02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md",
        "annex": REPO / "02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/annexes/B_Sequence_Diagrams.md",
    },
    "Case_03": {
        "catalog": REPO / "02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/Doc22_Use_Cases_Catalog.md",
        "annex": REPO / "02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/annexes/B_Sequence_Diagrams.md",
    },
}

CARD_RE = re.compile(r"^####\s+([A-Za-z0-9.\-]+)\s*[—:]\s*(.+?)\s*$", re.M)
SEQ_RE = re.compile(r"```mermaid\nsequenceDiagram\n.*?```", re.S)


def last_card_header_before(text, pos):
    """Find the nearest `#### <id> — Title` header before pos."""
    best = None
    for m in CARD_RE.finditer(text, 0, pos):
        best = m
    return best


def process(catalog, annex, apply):
    text = catalog.read_text(encoding="utf-8")
    blocks = list(SEQ_RE.finditer(text))
    if not blocks:
        print(f"  {catalog.name}: 0 sequenceDiagram blocks (already extracted?)")
        return 0
    entries = []
    # Build replacement text walking blocks in reverse to keep offsets stable
    new_text = text
    for idx, m in enumerate(reversed(blocks), 1):
        n = len(blocks) - idx + 1  # section number in original order
        block = m.group(0)
        hdr = last_card_header_before(text, m.start())
        card_id = hdr.group(1) if hdr else "UNKNOWN"
        card_title = hdr.group(2) if hdr else ""
        section = f"## §{n} — {card_id} — {card_title}\n\n{block}\n"
        entries.append((n, card_id, card_title, section))
        pointer = f"> **Sequence diagram:** → Annex B §{n} (B_Sequence_Diagrams.md)\n"
        start, end = m.span()
        new_text = new_text[:start] + pointer.strip() + new_text[end:]
    if apply:
        annex.parent.mkdir(parents=True, exist_ok=True)
        if annex.exists():
            ann = annex.read_text(encoding="utf-8")
            # append new sections before any existing content tail? simple: append
            ann = ann.rstrip() + "\n\n" + "\n".join(e[3] for e in sorted(entries, key=lambda x: x[0])) + "\n"
        else:
            ann = ("---\n"
                   f"document_id: AEGIS-P3-ANNEX-B\n"
                   f"title: Sequence Diagrams Annex\n"
                   f"phase: 3\n"
                   f"version: 1.0\n"
                   f"created: 2026-09-05\n"
                   f"updated: 2026-09-05\n"
                   f"author: Executor\n"
                   f"status: ACTIVE\n"
                   "---\n\n"
                   "# Annex B — Sequence Diagrams\n\n"
                   "> Extracted from the catalogue cards per rubric v1.7 §5C.5 "
                   "(sequence diagrams are annex-only). One section per product UC card.\n"
                   "> **Render note:** Mermaid ≥ v11 recommended.\n\n"
                   + "\n".join(e[3] for e in sorted(entries, key=lambda x: x[0])) + "\n")
        annex.write_text(ann, encoding="utf-8")
        catalog.write_text(new_text, encoding="utf-8")
    print(f"  {catalog.name}: {len(blocks)} sequenceDiagrams extracted → {annex.name} ({'APPLIED' if apply else 'DRY-RUN'})")
    return len(blocks)


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    apply = "--apply" in sys.argv
    sel = list(CASES.items()) if target == "all" else [(target, CASES[target])]
    grand = 0
    for name, cfg in sel:
        print(f"{name}:")
        grand += process(cfg["catalog"], cfg["annex"], apply)
    print(f"---\ntotal: {grand} ({'APPLIED' if apply else 'DRY-RUN'})")


if __name__ == "__main__":
    main()
