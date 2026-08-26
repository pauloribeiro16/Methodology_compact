#!/usr/bin/env python3
"""
filter_ambiguity_cards.py — Sprint 0 stub

Filters corpus ambiguity cards (L3 JSON sidecars under
PREPROCESSING_by_domain/domains/) to surface only those relevant to a
given case, based on applicable regulations and activated sub-domains.

Emits a case-specific subset for the Ambiguity Register (05b).

To be implemented in Sprint 2 (Corpus Enrichment).
"""
from __future__ import annotations

from pathlib import Path

CORPUS_ROOT = Path("00_METHODOLOGY/PREPROCESSING_by_domain/domains")


def load_ambiguity_cards(subdomain: str) -> list[dict]:
    """Load ambiguity cards for a single sub-domain from its L3 JSON."""
    return []


def filter_for_case(subdomains: list[str], regulations: list[str]) -> list[dict]:
    """Return ambiguity cards relevant to the given case scope."""
    return []


if __name__ == "__main__":
    print("TODO: Sprint 2 — filter corpus ambiguity cards for this case's applicable scope")
