#!/usr/bin/env python3
"""
generate_corpus_links.py — Sprint 0 stub

Generates corpus-link references from case files to
PREPROCESSING_by_domain/domains/. Scans every .md file in this folder,
identifies sub-domain IDs (D-XX.Y pattern), and emits the 4-layer corpus
paths (L1/L2/L3/L4) into validation/corpus_links_report.json.

To be implemented in Sprint 2 (Corpus Enrichment).
"""
from __future__ import annotations

import re
from pathlib import Path

CORPUS_ROOT = Path("00_METHODOLOGY/PREPROCESSING_by_domain/domains")
SUBDOMAIN_PATTERN = re.compile(r"\bD-(\d{1,2})\.(\d{1,2})\b")


def discover_subdomains(text: str) -> set[str]:
    """Return set of D-XX.Y sub-domain IDs found in text."""
    return {m.group(0) for m in SUBDOMAIN_PATTERN.finditer(text)}


if __name__ == "__main__":
    print("TODO: Sprint 2 — generate corpus links from case fields to corpus JSON paths")
