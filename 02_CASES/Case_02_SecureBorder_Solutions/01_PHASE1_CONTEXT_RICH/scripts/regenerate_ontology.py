#!/usr/bin/env python3
"""
regenerate_ontology.py — Sprint 1 stub.

Re-generates the ground-truth ontology used by
lint_regulatory_ground_truth.py after the 3 Phase 1 lint warnings are
reconciled:

  - T-006 / T-007 / T-008 not in ontology (extend)
  - 4 obligated_party values not in regulation's allowed set (extend)
  - Regulation name drift (GDPR vs `GDPR`, `NIS 2` vs `NIS2`) (normalise)

TODO Sprint 1:
- Extend the ontology to include T-006/007/008 (Med-resource tension rows).
- Extend the obligated_party tables per regulation to include MANUFACTURER,
  ESSENTIAL_ENTITY_SUPPLIER, PROVIDER, Rationale as aliases.
- Normalise regulation name strings to canonical enum {GDPR, NIS2, CRA, DORA, AI_Act}.
- Re-run lint_regulatory_ground_truth.py and verify 0 warnings.

Usage:
    python3 scripts/regenerate_ontology.py
"""
from __future__ import annotations

from pathlib import Path

LINT_DIR = Path("/home/epmq-cyber/Área de Trabalho/projects/Methodology-main/01_IMPLEMENTATION_TOOLS/lints/phase1")
ONTOLOGY_ASSUMED = LINT_DIR / "ground_truth_ontology.yaml"
APPLICABLE = {"GDPR", "CRA", "NIS 2", "AI_Act"}


def main() -> int:
    print("TODO: Sprint 1 — regenerate_ontology.py")
    print(f"  LINT_DIR  = {LINT_DIR}")
    print(f"  ONTOLOGY (assumed) = {ONTOLOGY_ASSUMED}")
    if not ONTOLOGY_ASSUMED.exists():
        print("  WARN: ontology file not found at expected path; locate first.")
    print(f"  APPLICABLE = {sorted(APPLICABLE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
