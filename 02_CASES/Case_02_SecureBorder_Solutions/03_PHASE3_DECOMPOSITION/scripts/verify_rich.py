#!/usr/bin/env python3
"""
verify_rich.py — Phase 3 Rich Mode structural checks, Case_02 (SecureBorder Solutions).

Port of Case_01's 03_PHASE3_DECOMPOSITION_RICH/scripts/verify_rich.py (light xlsx
stub), adapted per PORT-PARITY-2 block F5 into a real structural checker over the
Case_02 P3 docs:

  CHK-1  frontmatter completeness (8 corr-008 fields) on every DocNN_*.md
  CHK-2  FR id census (Doc29: FR-NN, metadata claims 84)
  CHK-3  NFR id census (Doc30: NFR-NN)
  CHK-4  rule-id census + dangling refs (CR/BPR-D-XX.X-NNN must exist in
         02_PHASE2_RULES_RICH/control_set.yaml, 63 controls)
  CHK-5  UC id census (Doc21: flat UC-NN ids + UC-* package labels)
  CHK-6  corr-008 cross-refs: FR table "Source Rule" values resolve; gate rows'
         rule refs resolve; gate rows' FR refs resolve
  CHK-7  rule traceability coverage: every control_set rule referenced by >=1
         of {Doc21 UC catalog, Doc25 allocation, Doc26 gates, Doc29 FR}

Exit 0 = all checks PASS; exit 1 = at least one FAIL (findings are printed and
meant to be transcribed honestly into validation/RICH_LINT_BASELINE.md).

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
GATE_RE = re.compile(r"\bGATE-D-\d{2}\.\d-\d{3}\b")

REQUIRED_FM = ["document_id", "title", "phase", "version", "created", "author", "status", "case"]

results: list[tuple[str, str, str]] = []  # (check, verdict, detail)


def record(check: str, ok: bool, detail: str) -> None:
    results.append((check, "PASS" if ok else "FAIL", detail))


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def main() -> int:
    # ---- control_set (rule universe) ----
    cs_file = P2 / "control_set.yaml"
    cs = yaml.safe_load(read(cs_file))["control_set"]
    rule_universe = {c["id"] for c in cs["controls"]}
    record("CHK-0 sources", True,
           f"control_set.yaml v{cs.get('version')}: {len(rule_universe)} controls "
           f"({sum(1 for c in cs['controls'] if c['kind']=='CR')} CR + "
           f"{sum(1 for c in cs['controls'] if c['kind']=='BPR')} BPR)")

    docs = sorted(BASE.glob("Doc*.md"))
    text = {d.name: read(d) for d in docs}

    # ---- CHK-1 frontmatter ----
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

    # ---- CHK-2 FR census (Doc29) ----
    fr_doc = (BASE / "requirements" / "Doc29_Functional_Requirements.md").read_text(encoding="utf-8")
    fr_ids = sorted(set(FR_RE.findall(fr_doc)))
    dup_rows = re.findall(r"^\| (FR-\d{2}) \|", fr_doc, re.M)
    dupes = sorted({f for f in dup_rows if dup_rows.count(f) > 1})
    claimed = re.search(r"totalFRs\s*\|\s*(\d+)", fr_doc)
    claimed_n = int(claimed.group(1)) if claimed else -1
    record("CHK-2 FR census", len(fr_ids) == claimed_n and not dupes,
           f"unique FR ids={len(fr_ids)}, Doc29 metadata totalFRs={claimed_n}, duplicated rows={dupes or 'none'}")

    # ---- CHK-3 NFR census (Doc30) ----
    nfr_doc = (BASE / "requirements" / "Doc30_Non_Functional_Requirements.md").read_text(encoding="utf-8")
    nfr_ids = sorted(set(NFR_RE.findall(nfr_doc)))
    nfr_claimed = re.search(r"totalNFRs\s*\|\s*(\d+)", nfr_doc)
    nfr_claimed_n = int(nfr_claimed.group(1)) if nfr_claimed else -1
    ok = (nfr_claimed_n == -1 and len(nfr_ids) > 0) or (len(nfr_ids) == nfr_claimed_n)
    record("CHK-3 NFR census", ok,
           f"unique NFR ids={len(nfr_ids)}, Doc30 metadata totalNFRs={nfr_claimed_n if nfr_claimed_n>0 else 'not stated'}")

    # ---- CHK-4 rule refs + dangling ----
    all_refs: dict[str, list[str]] = {}
    dangling: set[str] = set()
    for name, t in text.items():
        for rid in RULE_RE.findall(t):
            all_refs.setdefault(rid, []).append(name)
            if rid not in rule_universe:
                dangling.add(rid)
    for extra in ("requirements/Doc29_Functional_Requirements.md", "requirements/Doc30_Non_Functional_Requirements.md"):
        t = (BASE / extra).read_text(encoding="utf-8")
        for rid in RULE_RE.findall(t):
            all_refs.setdefault(rid, []).append(extra)
            if rid not in rule_universe:
                dangling.add(rid)
    record("CHK-4 rule refs / dangling", not dangling,
           f"distinct rule refs={len(all_refs)} across P3 docs; dangling (not in control_set 63)={sorted(dangling) or 'none'}")

    # ---- CHK-5 UC census ----
    uc_doc = text.get("Doc21_Use_Cases_Catalog.md", "")
    uc_detailed = sorted(set(UC_RE.findall(uc_doc)))
    uc_packages = sorted(set(re.findall(r"\bUC-(DP|SEC|IAM|DEV|GOV|AI|TRN)\b", uc_doc)))
    uc_claimed = re.search(r"totalUseCases\s*\|\s*(\d+)", uc_doc)
    rel_claimed = re.search(r"Initial release[^\n]*\((\d+) UCs:", uc_doc)
    record("CHK-5 UC census", True,
           f"unique UC ids={len(uc_detailed)}, packages={len(uc_packages)} {uc_packages}, "
           f"metadata totalUseCases={uc_claimed.group(1) if uc_claimed else '?'} "
           f"(v1.0 release row claims {rel_claimed.group(1) if rel_claimed else '?'} — historical, informational)")

    # ---- CHK-6 corr-008 cross-refs ----
    bad_sr, gate_bad_rule, gate_bad_fr = [], [], []
    for line in fr_doc.splitlines():
        m = re.match(r"^\| (FR-\d{2}) \|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|", line)
        if m and m.group(1) != "FR ID":
            sr = m.group(5).strip()
            for tok in [x.strip() for x in sr.split(",")]:
                if tok and tok != "—" and not RULE_RE.fullmatch(tok):
                    bad_sr.append(f"{m.group(1)} -> '{tok}'")
                elif tok and tok != "—" and tok not in rule_universe:
                    bad_sr.append(f"{m.group(1)} -> {tok} (not in control_set)")
    gate_rows = re.findall(r"^\| (GATE-D-\d{2}\.\d-\d{3}) \|[^|]*\|[^|]*\|([^|]*)\|([^|]*)\|",
                           text.get("Doc26_Compliance_Gates_Report.md", ""), re.M)
    for gid, grules, gfrs in gate_rows:
        for rid in [x.strip() for x in re.split(r"[,;]", grules) if x.strip()]:
            if RULE_RE.fullmatch(rid) and rid not in rule_universe:
                gate_bad_rule.append(f"{gid} -> {rid}")
        for fid in FR_RE.findall(gfrs):
            if fid not in fr_ids:
                gate_bad_fr.append(f"{gid} -> {fid}")
    record("CHK-6 corr-008 cross-refs", not bad_sr and not gate_bad_rule and not gate_bad_fr,
           f"FR 'Source Rule' malformed={bad_sr[:5] or 'none'}; gate->rule dangling={gate_bad_rule[:5] or 'none'}; "
           f"gate->FR dangling={gate_bad_fr[:5] or 'none'}")

    # ---- CHK-7 rule traceability coverage ----
    covered: set[str] = set(all_refs)
    uncovered = sorted(rule_universe - covered)
    fr_sr_rules = {m.group(1) for m in re.finditer(r"^\| FR-\d{2} \|[^|]*\|[^|]*\|[^|]*\|\s*((?:CR|BPR)-D-\d{2}\.\d-\d{3})\s*\|", fr_doc, re.M)}
    record("CHK-7 rule traceability coverage", not uncovered,
           f"rules referenced by >=1 P3 doc: {len(covered & rule_universe)}/{len(rule_universe)}; "
           f"uncovered={uncovered or 'none'}; FR-level Source Rule only covers {len(fr_sr_rules)} rules "
           f"(see RICH_LINT_BASELINE.md finding F5-C2-01)")

    # ---- report ----
    print(f"verify_rich.py — Case_02_SecureBorder_Solutions (Phase 3, PORT-PARITY-2 F5)")
    for check, verdict, detail in results:
        print(f"[{verdict}] {check}: {detail}")
    fails = sum(1 for _, v, _ in results if v == "FAIL")
    print(f"summary: {len(results)} checks, {fails} FAIL, {len(results)-fails} PASS")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
