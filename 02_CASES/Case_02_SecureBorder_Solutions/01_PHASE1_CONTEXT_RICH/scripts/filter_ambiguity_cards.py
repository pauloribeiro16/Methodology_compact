#!/usr/bin/env python3
"""
filter_ambiguity_cards.py — Sprint 0.5 stub.

Filters L2 Regulation/<REG>/Ambiguity/ clause cards to Case_02-applicable regs
(GDPR, NIS2, CRA, AI_Act; excludes DORA).

Outputs a JSON file with per-regulation card counts and CSVs the cards
themselves for ingest into 05b_Ambiguity_Register.md.

TODO Sprint 0.5:
- Parse each Regulation/<REG>/Ambiguity/ folder for clause card files.
- Filter to Case_02 applicable regs.
- For each card, extract: clause_id, severity (S1-S3), category (one of 4 Berry lens),
  regulated party, and short description.
- Write JSON to validation/filtered_ambiguity.json.
- Update 05b_Ambiguity_Register.md with the count.

Usage:
    python3 scripts/filter_ambiguity_cards.py
"""
from __future__ import annotations

from pathlib import Path

CORPUS = Path("/home/epmq-cyber/Área de Trabalho/projects/Methodology-main/00_METHODOLOGY/PREPROCESSING/Regulation")
OUT = Path(__file__).resolve().parent.parent / "validation" / "filtered_ambiguity.json"
APPLICABLE = {"GDPR", "NIS2", "CRA", "AI_Act"}


def main() -> int:
    print("TODO: Sprint 0.5 — filter_ambiguity_cards.py")
    print(f"  CORPUS    = {CORPUS}")
    print(f"  OUTPUT    = {OUT}")
    print(f"  APPLICABLE = {sorted(APPLICABLE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
