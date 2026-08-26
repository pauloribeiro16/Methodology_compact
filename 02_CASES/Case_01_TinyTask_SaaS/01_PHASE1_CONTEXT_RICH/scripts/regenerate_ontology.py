#!/usr/bin/env python3
"""
regenerate_ontology.py — Sprint 0 stub

Regenerates the case-specific taxonomy cross-reference table from the
live corpus. Reads 38 sub-domain manifests (L2) under
PREPROCESSING_by_domain/domains/ and emits a Markdown table suitable for
inclusion in 00_Taxonomy_Reference.md (Rich Mode).

Output: stdout Markdown + validation/ontology_snapshot.json (Goal G4).

To be implemented in Sprint 2 (Corpus Enrichment).
"""
from __future__ import annotations

import json
from pathlib import Path

CORPUS_ROOT = Path("00_METHODOLOGY/PREPROCESSING_by_domain/domains")
SNAPSHOT_PATH = Path("validation/ontology_snapshot.json")


def load_subdomain_manifests() -> list[dict]:
    """Load all 38 L2 sub-domain manifests from the corpus."""
    return []


def write_snapshot(manifests: list[dict]) -> None:
    """Write JSON snapshot for reproducibility (Goal G4)."""
    SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_PATH.write_text(json.dumps(manifests, indent=2, sort_keys=True))


if __name__ == "__main__":
    print("TODO: Sprint 2 — regenerate 00_Taxonomy_Reference.md table from corpus L2 manifests")
