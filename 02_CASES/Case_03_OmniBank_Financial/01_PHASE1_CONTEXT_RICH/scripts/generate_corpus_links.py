#!/usr/bin/env python3
"""
generate_corpus_links.py — Sprint 0.5 stub.

Auto-generates per-doc links from each Rich doc to the 4 corpus layers
(L1 Domain Manifests, L2 Sub-domain Manifests, L3 JSON sidecars,
L5 Verbatim Articles).

Target: placeholder docs in this folder.

TODO Sprint 0.5:
- Parse each .md placeholder's "## Cross-references to fill" section.
- For each L1/L2/L3/L5 reference, validate the corpus path exists.
- Replace placeholders with rendered markdown links + status badges.
- Update each placeholder's `Cross-references` section with verified
  paths + line counts.

Case_03 specifics (MAX):
- Corpus is FULLY populated (38/38 sub-domains, 48 manifests, 623 articles).
- 5 applicable regs (GDPR + CRA + NIS 2 + DORA + AI Act) — all sub-domains
  have at least one of these regs, so no INACTIVE rows.
- DORA + AI Act have specialised corpus paths (DORA bare CLx-y prefix,
  AI_Act semantic prefix).

Usage:
    python3 scripts/generate_corpus_links.py
"""
from __future__ import annotations

from pathlib import Path

CORPUS = Path("/home/epmq-cyber/Área de Trabalho/projects/Methodology-main/00_METHODOLOGY/PREPROCESSING_by_domain/domains")
RICH_FOLDER = Path(__file__).resolve().parent.parent
APPLICABLE = {"GDPR", "NIS2", "CRA", "DORA", "AI_Act"}


def main() -> int:
    print("TODO: Sprint 0.5 — generate_corpus_links.py")
    print(f"  CORPUS      = {CORPUS}")
    print(f"  RICH_FOLDER = {RICH_FOLDER}")
    print(f"  APPLICABLE  = {sorted(APPLICABLE)}")
    print()
    print("Sprint 0.5 plan:")
    print("  1. Read each placeholder's ## Cross-references to fill section")
    print("  2. Validate L1/L2/L3/L5 paths against corpus")
    print("  3. Render markdown links + badge (verified / missing)")
    print("  4. Append line counts per corpus artefact")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
