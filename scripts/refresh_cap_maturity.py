#!/usr/bin/env python3
"""
refresh_cap_maturity.py — fill CAP card Maturity fields per rubric §5C.2.

Method: each CAP card has a Maturity row. If P1 phase1_graph.json contains an
EvidenceItem with scale=capability and a matching claim, use current/target.
Otherwise fill `PLANNED (1)` with note "evidence pending P1 Folio VIII refresh".

Usage: python3 scripts/refresh_cap_maturity.py <Case_01|Case_02|Case_03|all>
"""
import re
import sys
import json
from pathlib import Path

CARDS = {
    "Case_01": "02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/Doc32_Process_Capability_Cards.md",
    "Case_02": "02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc31_Process_Capability_Cards.md",
    "Case_03": "02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/Doc32_Process_Capability_Cards.md",
}
P1 = {
    "Case_01": "02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json",
    "Case_02": "02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json",
    "Case_03": "02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json",
}


def derive_maturity(card_id, p1_graph):
    """Find a P1 EvidenceItem whose claim references the CAP id; return maturity_cur/tgt if found."""
    if not p1_graph: return None, None
    for n in p1_graph.get("nodes", []):
        if n.get("kind") == "EvidenceItem" and n.get("scale") == "capability":
            claim = n.get("claim", "")
            if card_id.split(":")[-1].strip() in claim or card_id.lower() in claim.lower():
                return n.get("maturity_cur"), n.get("maturity_tgt")
    return None, None


def refresh_case(case, path, p1_path):
    if not Path(path).exists():
        print(f"  {case}: file missing")
        return 0
    p1 = json.loads(Path(p1_path).read_text()) if Path(p1_path).exists() else None
    text = Path(path).read_text(encoding="utf-8")
    # find CAP cards: `## CAP-NN — ...` blocks
    blocks = list(re.finditer(r"(## CAP-\d+ — [^\n]*\n.*?)(?=^## |\Z)", text, re.S | re.M))
    n_changed = 0
    new_blocks = []
    last_end = 0
    for m in blocks:
        new_blocks.append(text[last_end:m.start()])
        block = m.group(0)
        card_id = m.group(1).split("—")[0].strip()
        if "Maturity" in block:
            m2 = re.search(r"\|\s*Maturity\s*\|([^|\n]+)\|", block)
            cur_val = m2.group(1).strip() if m2 else ""
            # Treat as unfilled if missing, dash, or only contains prose description
            # (a "concrete" value contains a digit 1-4 followed by /, or a Maturity level token).
            has_concrete = bool(re.search(r"\b[1-4]/[1-4]\b|\bPLANNED\b", cur_val))
            if not cur_val or cur_val == "—" or not has_concrete:
                cur, tgt = derive_maturity(card_id, p1)
                if cur is not None:
                    new_val = f" {cur}/{tgt} (current/target) — posture model v1.6 Scale A"
                else:
                    new_val = " PLANNED (1) — Scale A posture model v1.6; current/target pending P1 Folio VIII refresh + EvidenceItem bind"
                new_block = re.sub(r"\|\s*Maturity\s*\|[^|\n]+\|", f"| Maturity |{new_val} |", block, 1)
                n_changed += 1
                block = new_block
        new_blocks.append(block)
        last_end = m.end()
    new_blocks.append(text[last_end:])
    new_text = "".join(new_blocks)
    if n_changed:
        Path(path).write_text(new_text, encoding="utf-8")
    print(f"  {case}: {len(blocks)} CAP cards, {n_changed} maturity values filled")


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    sel = list(CARDS.items()) if target == "all" else [(target, CARDS[target])]
    for case, p in sel:
        refresh_case(case, p, P1[case])


if __name__ == "__main__":
    main()
