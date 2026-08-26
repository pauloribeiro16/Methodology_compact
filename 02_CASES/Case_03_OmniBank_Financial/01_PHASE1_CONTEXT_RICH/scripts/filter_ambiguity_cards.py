#!/usr/bin/env python3
"""
filter_ambiguity_cards.py — Sprint 0.5 stub.

Filters L3 JSON sidecar `ambiguity_cards[]` to Case_03-applicable regs
(GDPR, NIS 2, CRA, DORA, AI Act).

Case_03 specifics (MAX, all 5 regs applicable):
- For Case_03, the filter is a no-op — all 38 sub-domains are in scope
  because all 5 case-applicable regs cover every sub-domain.
- Total expected in-scope cards: ~1490 (all sub-domains × all cards).
- After (clause_id, article_ref) dedup, expect ~700-900 unique cards.

TODO Sprint 0.5:
- Parse each D-XX.Y.json sidecar for `ambiguity_cards[]`.
- For each card, extract: clause_id, regulation, severity (S1-S3),
  category (one of 4 Berry lens), regulated party, short description.
- Filter to Case_03 applicable regs (GDPR + NIS 2 + CRA + DORA + AI Act).
- Write filtered cards to validation/filtered_ambiguity.json.
- Update 05b_Ambiguity_Register.md with the count.

Usage:
    python3 scripts/filter_ambiguity_cards.py
"""
from __future__ import annotations

from pathlib import Path

CORPUS = Path("/home/epmq-cyber/Área de Trabalho/projects/Methodology-main/00_METHODOLOGY/PREPROCESSING_by_domain/domains")
OUT = Path(__file__).resolve().parent.parent / "validation" / "filtered_ambiguity.json"
APPLICABLE = {"GDPR", "NIS2", "CRA", "DORA", "AI_Act"}


def main() -> int:
    print("TODO: Sprint 0.5 — filter_ambiguity_cards.py")
    print(f"  CORPUS     = {CORPUS}")
    print(f"  OUTPUT     = {OUT}")
    print(f"  APPLICABLE = {sorted(APPLICABLE)}")
    print()
    print("Case_03 is MAX — filter is no-op:")
    print("  All 5 applicable regs cover all 38 sub-domains.")
    print("  Expected total in-scope cards: ~1490 (all sub-domains).")
    print()
    print("Sprint 0.5 plan:")
    print("  1. Walk all 38 D-XX.Y.json sidecars")
    print("  2. For each sidecar, iterate ambiguity_cards[]")
    print("  3. Filter by regulation ∈ APPLICABLE (no-op for Case_03)")
    print("  4. Dedupe by (clause_id, article_ref)")
    print("  5. Write filtered cards to validation/filtered_ambiguity.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
