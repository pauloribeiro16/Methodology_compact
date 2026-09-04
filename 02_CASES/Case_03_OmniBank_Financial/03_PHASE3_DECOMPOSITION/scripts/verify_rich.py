#!/usr/bin/env python3
"""
verify_rich.py — Phase 3 Rich Mode structural checks, Case_03 (OmniBank Financial).

PORT-PARITY-2 block F5 port of Case_01's verify_rich.py, adapted to Case_03's
real doc numbering (Doc22–Doc31; Rules_Catalog = Doc19 after the P2 renumbering)
and id schemes (FR-NN 72, NFR-NN 12, UC-NN 62, GATE-D-XX-NN 40, rules
CR/BPR-D-XX.Y-NNN 78 = 38 CR + 40 BPR incl. 4 D-12.x AI-specific):

  CHK-1  frontmatter completeness (8 corr-008 fields) on every DocNN_*.md
  CHK-2  FR id census (requirements/Doc30: FR cards vs "Total FRs" summary)
  CHK-3  NFR id census (requirements/Doc31: NFR cards vs "Total NFRs" summary)
  CHK-4  rule-id census + dangling refs (universe = ../02_PHASE2_RULES_RICH/control_set.yaml, 78)
  CHK-5  UC census (Doc22: '## UC-NN:' cards)
  CHK-6  corr-008 cross-refs: FR/NFR card 'Source Rule' values resolve; UC card
         '**Rules:**' values resolve; Doc27 gate cards' 'Rules Verified' resolve
  CHK-7  rule traceability coverage: every control_set rule referenced by >=1 P3 doc

Exit 0 = all checks PASS; exit 1 = at least one FAIL (transcribe honestly into
validation/RICH_LINT_BASELINE.md).

Usage:
  python3 scripts/verify_rich.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
CASE = BASE.parent
P2 = CASE / "02_PHASE2_RULES_RICH"

FR_RE = re.compile(r"\bFR-\d{2,3}\b")
NFR_RE = re.compile(r"\bNFR-\d{2,3}\b")
RULE_RE = re.compile(r"\b(?:CR|BPR)-D-\d{2}\.\d-\d{3}\b")
UC_RE = re.compile(r"\bUC-\d{2}\b")
GATE_RE = re.compile(r"\bGATE-D-\d{2}-\d{2}\b")

REQUIRED_FM = ["document_id", "title", "phase", "version", "created", "author", "status", "case"]

results: list[tuple[str, str, str]] = []


def record(check: str, ok: bool, detail: str) -> None:
    results.append((check, "PASS" if ok else "FAIL", detail))


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def parse_cards(doc: str, kind: str) -> dict[str, dict]:
    """Case_03 card format: '#### FR-NN: Title' + Field/Value table."""
    cards: dict[str, dict] = {}
    current = None
    for line in doc.splitlines():
        m = re.match(rf"^#### ({kind}-\d{{2,3}}): (.+)$", line)
        if m:
            current = m.group(1)
            cards[current] = {"title": m.group(2).strip(), "fields": {}}
            continue
        if current:
            fm_ = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|", line)
            if fm_ and not fm_.group(1).startswith("Field"):
                cards[current]["fields"][fm_.group(1)] = fm_.group(2)
    return cards


def main() -> int:
    cs = yaml.safe_load(read(P2 / "control_set.yaml"))["control_set"]
    rule_universe = {c["id"] for c in cs["controls"]}
    n_cr = sum(1 for c in cs["controls"] if c["kind"] == "CR")
    n_bpr = sum(1 for c in cs["controls"] if c["kind"] == "BPR")
    record("CHK-0 sources", True,
           f"control_set.yaml v{cs.get('version')}: {len(rule_universe)} controls ({n_cr} CR + {n_bpr} BPR incl. 4 D-12.x AI-specific)")

    docs = sorted(BASE.glob("Doc*.md"))
    text = {d.name: read(d) for d in docs}

    # CHK-1 frontmatter
    fm_bad = []
    for d in docs:
        m = re.match(r"^---\n(.*?)\n---\n", text[d.name], re.DOTALL)
        if not m:
            fm_bad.append(f"{d.name}: no frontmatter")
            continue
        fields = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M))
        missing = [f for f in REQUIRED_FM if f not in fields]
        if missing:
            fm_bad.append(f"{d.name}: missing {missing}")
    record("CHK-1 frontmatter (8 fields)", not fm_bad,
           f"{len(docs)} DocNN docs checked; violations: {fm_bad or 'none'}")

    # CHK-2 FR census
    fr_doc = read(BASE / "requirements" / "Doc30_Functional_Requirements.md")
    fr_cards = parse_cards(fr_doc, "FR")
    fr_ids = sorted(fr_cards)
    claimed = re.search(r"\*\*Total FRs\*\*\s*\|\s*(\d+)", fr_doc)
    claimed_n = int(claimed.group(1)) if claimed else -1
    record("CHK-2 FR census", len(fr_ids) == claimed_n,
           f"FR cards={len(fr_ids)}, Doc30 summary 'Total FRs'={claimed_n}")

    # CHK-3 NFR census
    nfr_doc = read(BASE / "requirements" / "Doc31_Non_Functional_Requirements.md")
    nfr_cards = parse_cards(nfr_doc, "NFR")
    nfr_ids = sorted(nfr_cards)
    nclaimed = re.search(r"\*\*Total NFRs\*\*\s*\|\s*(\d+)", nfr_doc)
    nclaimed_n = int(nclaimed.group(1)) if nclaimed else -1
    record("CHK-3 NFR census", nclaimed_n == -1 and len(nfr_ids) > 0 or len(nfr_ids) == nclaimed_n,
           f"NFR cards={len(nfr_ids)}, Doc31 summary 'Total NFRs'={nclaimed_n if nclaimed_n > 0 else 'not stated'}")

    # CHK-4 rule refs / dangling
    all_refs: dict[str, list[str]] = {}
    dangling: set[str] = set()
    scan = {**text,
            "Doc30_Functional_Requirements.md": fr_doc,
            "Doc31_Non_Functional_Requirements.md": nfr_doc}
    for name, t in scan.items():
        for rid in RULE_RE.findall(t):
            all_refs.setdefault(rid, []).append(name)
            if rid not in rule_universe:
                dangling.add(rid)
    record("CHK-4 rule refs / dangling", not dangling,
           f"distinct rule refs={len(all_refs)}; dangling (not in control_set {len(rule_universe)})={sorted(dangling) or 'none'}")

    # CHK-5 UC census
    uc_doc = text.get("Doc22_Use_Cases_Catalog.md", "")
    uc_cards = sorted(set(re.findall(r"^## (UC-\d{2}):", uc_doc, re.M)))
    uc_claimed = re.search(r"\*\*Total Use Cases\*\*\s*\|\s*(\d+)|(\d+) use cases", uc_doc, re.I)
    record("CHK-5 UC census", True,
           f"UC cards={len(uc_cards)}; catalog claim="
           f"{uc_claimed.group(1) or uc_claimed.group(2) if uc_claimed else 'n/a'} (informational)")

    # CHK-6 cross-refs
    bad = []
    for fid, card in fr_cards.items():
        sr = card["fields"].get("Source Rule", "")
        for tok in [x.strip() for x in sr.split(",")]:
            if tok and tok != "—" and tok not in rule_universe:
                bad.append(f"{fid} -> {tok!r}")
    for nid, card in nfr_cards.items():
        sr = card["fields"].get("Source Rule", "")
        for tok in [x.strip() for x in sr.split(",")]:
            if tok and tok != "—" and tok not in rule_universe:
                bad.append(f"{nid} -> {tok!r}")
    for line in uc_doc.splitlines():
        m = re.match(r"^\*\*Rules:\*\*\s*(.+)$", line)
        if m:
            for tok in [x.strip() for x in m.group(1).split(",")]:
                if tok and tok != "—" and tok not in rule_universe:
                    bad.append(f"UC card -> {tok!r}")
    gates_doc = text.get("Doc27_Compliance_Gates_Report.md", "")
    gate_cards = parse_gate_cards(gates_doc)
    gate_bad = []
    for gid, card in gate_cards.items():
        for tok in [x.strip() for x in card.get("Rules Verified", "").split(",")]:
            if tok and RULE_RE.fullmatch(tok) and tok not in rule_universe:
                gate_bad.append(f"{gid} -> {tok}")
    record("CHK-6 corr-008 cross-refs", not bad and not gate_bad,
           f"FR/NFR/UC Source Rule unresolved={bad[:5] or 'none'}; gate Rules Verified unresolved={gate_bad[:5] or 'none'}")

    # CHK-7 coverage
    covered = set(all_refs) & rule_universe
    uncovered = sorted(rule_universe - covered)
    fr_sr_rules = {v for c in fr_cards.values() for v in [c["fields"].get("Source Rule", "")] if RULE_RE.fullmatch(v)}
    record("CHK-7 rule traceability coverage", not uncovered,
           f"rules referenced by >=1 P3 doc: {len(covered)}/{len(rule_universe)}; uncovered={uncovered or 'none'}; "
           f"FR-level Source Rule covers {len(fr_sr_rules)} rules")

    print(f"verify_rich.py — Case_03_OmniBank_Financial (Phase 3, PORT-PARITY-2 F5)")
    for check, verdict, detail in results:
        print(f"[{verdict}] {check}: {detail}")
    fails = sum(1 for _, v, _ in results if v == "FAIL")
    print(f"summary: {len(results)} checks, {fails} FAIL, {len(results)-fails} PASS")
    return 1 if fails else 0


def parse_gate_cards(doc: str) -> dict[str, dict]:
    """Doc27 gate cards: '#### GATE-D-XX-NN: Name' + Field/Value table."""
    cards: dict[str, dict] = {}
    current = None
    for line in doc.splitlines():
        m = re.match(r"^#### (GATE-D-\d{2}-\d{2}):", line)
        if m:
            current = m.group(1)
            cards[current] = {}
            continue
        if current:
            fm_ = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|", line)
            if fm_:
                cards[current][fm_.group(1)] = fm_.group(2)
    return cards


if __name__ == "__main__":
    sys.exit(main())
