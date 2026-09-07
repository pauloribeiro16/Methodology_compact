#!/usr/bin/env python3
"""build_master_dashboard_data.py — AEGIS Master Dashboard data layer.

Parses the corpus (Phase 1/2/3 artefacts of the 3 cases) into a single JSON
document that powers UNIFIED/AEGIS_Master_Dashboard.html. The JSON is a
DERIVED VIEW: generated from the documents, never hand-maintained.

Usage:
  python3 scripts/build_master_dashboard_data.py                 # write data/aegis_master_data.json
  python3 scripts/build_master_dashboard_data.py --dry-run       # validate parsing, no write
  python3 scripts/build_master_dashboard_data.py --inject PATH   # also inject into an HTML template
                                                                 # (replaces the literal `/*__MASTER_DATA__*/null`)

stdlib-only. Deterministic ordering. Missing sources -> null + warnings[].
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DEFAULT = REPO / "00_METHODOLOGY" / "00_VISUALISATIONS" / "data" / "aegis_master_data.json"
AUDIT_REPORT = REPO / "00_METHODOLOGY" / "validation" / "TRACEABILITY_AUDIT_2026-09-05.md"

CASES = {
    "Case_01_TinyTask_SaaS": {
        "root": "02_CASES/Case_01_TinyTask_SaaS",
        "p3_dir": "03_PHASE3_DECOMPOSITION_RICH",
        "catalog": "03_PHASE3_DECOMPOSITION_RICH/Doc20_Use_Cases_Catalog.md",
        "lane_cards": "03_PHASE3_DECOMPOSITION_RICH/Doc32_Process_Capability_Cards.md",
        "regs": ["GDPR", "CRA"],
        "tier": "Low",
        "product_section": r"## §2 Functional",
        "compliance_section": r"## §3 Security",
    },
    "Case_02_SecureBorder_Solutions": {
        "root": "02_CASES/Case_02_SecureBorder_Solutions",
        "p3_dir": "03_PHASE3_DECOMPOSITION",
        "catalog": "03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md",
        "lane_cards": "03_PHASE3_DECOMPOSITION/Doc31_Process_Capability_Cards.md",
        "regs": ["GDPR", "CRA", "NIS 2", "AI Act"],
        "tier": "High",
        "product_section": r"## 6\. PRODUCT",
        "compliance_section": r"## 7\. DOMAIN DECOMPOSITION",
    },
    "Case_03_OmniBank_Financial": {
        "root": "02_CASES/Case_03_OmniBank_Financial",
        "p3_dir": "03_PHASE3_DECOMPOSITION",
        "catalog": "03_PHASE3_DECOMPOSITION/Doc22_Use_Cases_Catalog.md",
        "lane_cards": "03_PHASE3_DECOMPOSITION/Doc32_Process_Capability_Cards.md",
        "regs": ["GDPR", "CRA", "NIS 2", "DORA", "AI Act"],
        "tier": "Maximum",
        "product_section": r"## 4\. PRODUCT",
        "compliance_section": r"## 3\. COMPLIANCE",
    },
}


def read(rel):
    p = REPO / rel
    if not p.exists():
        return None
    return p.read_text(encoding="utf-8")


def glob_first(root_rel, pattern):
    hits = sorted((REPO / root_rel).rglob(pattern))
    return str(hits[0].relative_to(REPO)) if hits else None


def frontmatter(text):
    if not text:
        return {}
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    out = {}
    if m:
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, _, v = line.partition(":")
                out[k.strip()] = v.strip().strip('"')
    return out


def cut_sections(text):
    """Split a document into (heading, body) chunks at ## level."""
    chunks, cur_h, cur = [], None, []
    for line in (text or "").split("\n"):
        if re.match(r"^## ", line):
            chunks.append((cur_h, "\n".join(cur)))
            cur_h, cur = line, []
        else:
            cur.append(line)
    chunks.append((cur_h, "\n".join(cur)))
    return chunks


def parse_catalog(case, cfg, warn):
    """UC inventory + packages from the case catalog. Grammar-tolerant."""
    text = read(f"{cfg['root']}/{cfg['catalog']}")
    if not text:
        warn.append(f"{case}: catalog missing ({cfg['catalog']})")
        return {"packages": [], "ucs": []}
    fm = frontmatter(text)
    chunks = cut_sections(text)

    def in_family(head, family):
        if head is None:
            return False
        pat = cfg[family]
        return re.search(pat, head, re.I) is not None

    packages, ucs, cur_pkg = [], [], None
    pkg_re = re.compile(r"^###\s+(?:§?\d+\.\d+\s+)?(?:\d+\.\d+\s+)?((?:PKG|PKG-)[-\w]*(?:\s*[—:-]\s*[^(\n]+)?[^(\n]*)")
    pkg_name_re = re.compile(r"^###\s+(?:§?\d+\.\d+\s+)?(?:\d+\.\d+\s+)?(PKG-[\w-]+)")
    for head, body in chunks:
        family = None
        if in_family(head, "product_section"):
            family = "product"
        elif in_family(head, "compliance_section"):
            family = "compliance"
        for line in body.split("\n"):
            # Track PKG section as we walk the body (cut_sections splits at ## only)
            m_pkg = pkg_re.match(line) if line.startswith("### ") else None
            if m_pkg:
                cur_pkg = m_pkg.group(1).strip()
                continue
            m = re.match(r"^#### (?:Use-Case: \{([^}]+)\}|(UC-\d+))\s*[—-]?\s*(.*)$", line)
            if m:
                uid = (m.group(1) or m.group(2)).strip()
                title = (m.group(3) or "").strip()
                ucs.append({"id": uid, "title": title, "package": cur_pkg, "lane": "UC"})
                continue
            m2 = re.match(r"^#### (UC-\d+)\s+—\s+(.*)$", line)  # C1 compliance grammar
            if m2:
                ucs.append({"id": m2.group(1), "title": m2.group(2).strip(), "package": cur_pkg, "lane": "UC"})
                continue
            if family == "compliance":
                m3 = re.match(r"^\|\s*(UC-\d+)\s*\|\s*([^|]+?)\s*\|", line)  # C2 compliance table rows
                if m3:
                    ucs.append({"id": m3.group(1), "title": m3.group(2).strip(), "package": cur_pkg, "lane": "UC"})
    # de-dup (defensive) + lane classification by id prefix
    seen, dedup = set(), []
    for u in ucs:
        if u["id"] in seen:
            continue
        seen.add(u["id"])
        u["lane"] = "UC" if u["id"].startswith("UC") else u["id"].split("-")[0]
        dedup.append(u)
    # package list from PKG headers seen (walk the body lines of every chunk)
    pk_seen, pkgs = set(), []
    for _, body in chunks:
        for line in body.split("\n"):
            if not line.startswith("### "):
                continue
            mn = pkg_name_re.match(line)
            if not mn:
                continue
            name = mn.group(1)
            if name and name not in pk_seen:
                pk_seen.add(name)
                pkgs.append(name)
    return {"packages": pkgs, "ucs": dedup, "frontmatter_version": fm.get("version")}


def parse_lane_cards(case, cfg, warn):
    """PROC/CAP cards from the per-case lane-cards doc (§5C.1/§5C.2 fields)."""
    text = read(f"{cfg['root']}/{cfg['lane_cards']}")
    if not text:
        warn.append(f"{case}: lane cards doc missing ({cfg['lane_cards']})")
        return {"proc": [], "cap": []}
    out = {"proc": [], "cap": []}
    cur = None
    for line in text.split("\n"):
        m = re.match(r"^## (PROC-\d+)\s+—\s+(.*)$", line)
        if m:
            cur = {"id": m.group(1), "title": m.group(2).strip(), "fields": {}}
            out["proc"].append(cur)
            continue
        m = re.match(r"^## (CAP-\d+)\s+—\s+(.*)$", line)
        if m:
            cur = {"id": m.group(1), "title": m.group(2).strip(), "fields": {}}
            out["cap"].append(cur)
            continue
        if cur:
            fm_ = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|$", line)
            if fm_ and fm_.group(1) != "Field":
                cur["fields"][fm_.group(1)] = fm_.group(2)
    for kind in ("proc", "cap"):
        for c in out[kind]:
            f = c.pop("fields")
            keep = ["Owner", "Trigger", "Activities", "Roles", "SLA / Timing", "Span",
                    "Maturity", "Realises", "Anchors", "Evidence"]
            c.update({k: f.get(k) for k in keep})
    return out


def parse_p1(case, cfg, warn):
    status = {}
    pj = read(f"{cfg['root']}/progress.json")
    if pj:
        try:
            data = json.loads(pj)
            for k, v in (data.get("phases") or {}).items():
                status[k] = {x: v.get(x) for x in ("status", "gate", "completed_at")}
        except json.JSONDecodeError:
            warn.append(f"{case}: progress.json unparsable")
    else:
        warn.append(f"{case}: progress.json missing")
    g = glob_first(cfg["root"], "phase1_graph.json")
    nodes = links = None
    if g:
        try:
            gd = json.loads(read(g))
            nodes, links = len(gd.get("nodes", [])), len(gd.get("links", []))
        except json.JSONDecodeError:
            warn.append(f"{case}: {g} unparsable")
    else:
        warn.append(f"{case}: phase1_graph.json not found")
    o = glob_first(cfg["root"], "phase1_ontology.yaml")
    ev_total = ev_cap = None
    if o:
        ot = read(o)
        ev_total = len(re.findall(r"^\s*-?\s*id:\s*EV-", ot, re.M))
        ev_cap = len(re.findall(r"scale:\s*capability", ot))
    return {"status": status.get("phase_1", status.get("phase_1_rich")),
            "graph": {"nodes": nodes, "links": links},
            "evidence_items": ev_total, "evidence_capability_scale": ev_cap,
            "ontology_file": o}


# ---------------------------------------------------------------------------
# Realization-class heuristic (deterministic, fallback only).
#
# The REALIZATION-CLASS campaign (rubric 00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md
# §2 closed enum {TECHNOLOGY, PROCESS, CAPABILITY}; campaign commits 762c095,
# 599a8ba, 113ba05 on 2026-09-05) tags rules explicitly in Case_01 control_set.yaml.
# For Case_02/Case_03 the YAMLs are generated and the field is parked per ledger
# §2 (phase2_ontology.yaml application is on the P7 queue, frozen). The dashboard
# needs honest numbers NOW without authoring new content, so we apply a
# deterministic derivation anchored to the campaign decisions and rubric §8
# worked examples (CR-D-08.1-001 / CR-D-08.2-001 CAPABILITY; CR-D-01.1-001 /
# CR-D-03.2-001 TECHNOLOGY; CR-D-04.3-001 PROCESS).
#
# Existing YAML tags (when present) ALWAYS take precedence; the heuristic is the
# fallback only — the rule-level "_heuristic" flag and the case-level "rc_source"
# string expose the provenance so the dashboard can render it.
# ---------------------------------------------------------------------------
RC_HEURISTIC_GOVERNANCE = {"D-09.1", "D-09.2", "D-09.3", "D-09.4", "D-09.5"}
RC_HEURISTIC_DATA_PROT_TECH = {"D-01.1", "D-01.2", "D-01.3"}
RC_HEURISTIC_VULN_DEV = "D-02."      # CR-D-02.* -> PROCESS (patching pipelines with
                                     # constitutive human triage; rubric §8 borderline 1)
RC_HEURISTIC_IAM = "D-03."          # CR-D-03.* -> TECHNOLOGY (enforced at IdP)
RC_HEURISTIC_SECDEV_GATES = "D-07." # CR-D-07.* -> PROCESS
RC_HEURISTIC_INCIDENT_NOTIFY = "D-04.3"  # CR-D-04.3 -> PROCESS (workflow with SLA clocks)


def derive_realization_class(rule_entry):
    """Derive (class, heuristic_flag) for a control_set entry lacking realization_class.

    Returns (class_string, True) when the heuristic decides; returns (existing_class, False)
    when the YAML already carries the field (caller should not normally call this in that
    case, but the check is defensive). class_string is one of TECHNOLOGY|PROCESS|CAPABILITY.

    Heuristic precedence (first match wins):
      1. D-08.*                       -> CAPABILITY  (training/competence = standing ability)
      2. D-09.1..D-09.5               -> CAPABILITY  (governance rules)
      3. D-01.1 / D-01.2 / D-01.3     -> TECHNOLOGY  (data protection via artefact property)
      4. D-04.3                       -> PROCESS     (incident notification SLA workflow)
      5. BPR-* prefix                 -> PROCESS     (best practice = coordinated activity)
      6. CR-D-02.* (vuln/secdev)      -> PROCESS     (patching pipelines + human triage)
      7. CR-D-03.* (IAM)              -> TECHNOLOGY  (enforced at the IdP)
      8. CR-D-07.* (secdev gates)     -> PROCESS
      9. else                         -> PROCESS     (safe default; _heuristic flag set)

    Anchored to REALIZATION-CLASS campaign commits 762c095 / 599a8ba / 113ba05 (2026-09-05)
    and rubric §8 worked examples. See 00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md §2.
    """
    rid = (rule_entry.get("id") or "").strip()
    sub = (rule_entry.get("sub_domain") or "").strip()
    # 1. Training / competence — standing ability (rubric §8: CR-D-08.1/08.2-001)
    if sub.startswith("D-08."):
        return ("CAPABILITY", True)
    # 2. Governance rules (rubric §8: CR-D-09.1-001 / CR-D-09.2-001)
    if sub in RC_HEURISTIC_GOVERNANCE:
        return ("CAPABILITY", True)
    # 3. Data protection built into the artefact (rubric §8: CR-D-01.1-001)
    if sub in RC_HEURISTIC_DATA_PROT_TECH:
        return ("TECHNOLOGY", True)
    # 4. Incident notification workflow with SLA clocks (rubric §8: CR-D-04.3-001)
    if sub == RC_HEURISTIC_INCIDENT_NOTIFY:
        return ("PROCESS", True)
    # 5. Best-practice rules are coordinated activities by definition
    if rid.startswith("BPR-"):
        return ("PROCESS", True)
    # 6. Vulnerability / secure development pipelines (rubric §8 borderline 1: CR-D-02.2-001)
    if rid.startswith("CR-") and sub.startswith(RC_HEURISTIC_VULN_DEV):
        return ("PROCESS", True)
    # 7. IAM enforced at the IdP, automated tests (rubric §8: CR-D-03.2-001)
    if rid.startswith("CR-") and sub.startswith(RC_HEURISTIC_IAM):
        return ("TECHNOLOGY", True)
    # 8. Secure-development gates are coordinated workflows
    if rid.startswith("CR-") and sub.startswith(RC_HEURISTIC_SECDEV_GATES):
        return ("PROCESS", True)
    # 9. Safe default
    return ("PROCESS", True)


def parse_p2(case, cfg, warn):
    """Parse Phase 2 control_set.yaml.

    Realization-class provenance (P7 honesty): Case_01 carries the field in YAML
    (rc_source="yaml"); Case_02/Case_03 do not, so values are derived via
    derive_realization_class() and rc_source is "heuristic" or "mixed" when
    some rules have explicit tags and others do not. See
    00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md §2 and campaign commits
    762c095 / 599a8ba / 113ba05 (2026-09-05).
    """
    cs = glob_first(cfg["root"], "control_set.yaml")
    rules, rc_counts = [], {"TECHNOLOGY": 0, "PROCESS": 0, "CAPABILITY": 0, "other": 0}
    explicit_count = heuristic_count = 0
    if cs:
        t = read(cs)
        ids = re.findall(r'^\s*-?\s*(?:rule_)?id:\s*"?([A-Z]{2,}-D-[\d.]+-\d+)"?', t, re.M)
        classes = re.findall(r'realization_class:\s*"?(\w+)"?', t)
        # Also capture sub_domain per entry (Case_01 uses "domain:", C2/C3 use "sub_domain:")
        domains = re.findall(r'^\s*-?\s*(?:sub_)?domain:\s*"?([D]-[\d.]+)"?', t, re.M)
        for i, rid in enumerate(ids):
            sub = domains[i] if i < len(domains) else ""
            entry = {"id": rid, "sub_domain": sub}
            rc_raw = classes[i] if i < len(classes) else None
            if rc_raw and rc_raw in rc_counts:
                rc = rc_raw
                heuristic = False
                explicit_count += 1
            else:
                rc, heuristic = derive_realization_class(entry)
                heuristic_count += 1
            key = rc if rc in rc_counts else "other"
            rc_counts[key] += 1
            rules.append({"id": rid, "realization_class": rc, "_heuristic": heuristic,
                          "sub_domain": sub})
    else:
        warn.append(f"{case}: control_set.yaml not found")
    if explicit_count and heuristic_count:
        rc_source = "mixed"
    elif heuristic_count:
        rc_source = "heuristic"
    elif explicit_count:
        rc_source = "yaml"
    else:
        rc_source = "none"
    tensions = set()
    for pat in ("*Tension*", "*tension*"):
        pass
    for cand in sorted((REPO / cfg["root"]).rglob("*Tension*")):
        t = cand.read_text(encoding="utf-8", errors="ignore")
        tensions |= set(re.findall(r"\bT-\d{3}\b", t))
    return {"rules_total": len(rules), "realization_class": rc_counts,
            "rc_source": rc_source, "rc_explicit": explicit_count,
            "rc_heuristic": heuristic_count,
            "rules_sample": rules[:5], "rules_file": cs, "tensions": sorted(tensions)}


def parse_p3_gates(case, cfg, warn):
    gates = {}
    vr = REPO / cfg["root"] / cfg["p3_dir"] / "scripts" / "verify_rich.py"
    if vr.exists():
        r = subprocess.run([sys.executable, str(vr)], capture_output=True, text=True, timeout=120)
        m = re.search(r"summary: (.+)", r.stdout + r.stderr)
        gates["verify_rich"] = {"summary": m.group(1) if m else f"exit {r.returncode}",
                                "pass": r.returncode == 0}
    else:
        warn.append(f"{case}: verify_rich.py missing")
    return gates


def parse_annexes(case, cfg):
    ann = REPO / cfg["root"] / cfg["p3_dir"] / "annexes"
    out = {"use_case_diagrams_plantuml": None, "svg_files": None,
           "sequence_diagrams": None}
    a = ann / "A_Use_Case_Diagrams.md"
    b = ann / "B_Sequence_Diagrams.md"
    sv = ann / "svg"
    if a.exists():
        out["use_case_diagrams_plantuml"] = len(re.findall(r"```plantuml", a.read_text(encoding="utf-8")))
    if b.exists():
        out["sequence_diagrams"] = len(re.findall(r"```mermaid\nsequenceDiagram", b.read_text(encoding="utf-8")))
    if sv.exists():
        out["svg_files"] = len(list(sv.glob("*.svg")))
    return out


def parse_fr_nfr(case, cfg):
    req = REPO / cfg["root"] / cfg["p3_dir"] / "requirements"
    fr = nfr = None
    if req.exists():
        for f in sorted(req.glob("*Functional_Requirements.md")):
            ft = f.read_text(encoding="utf-8")
            fr = max(fr or 0, len(set(re.findall(r"\bFR-\d+\b", ft))), len(re.findall(r"^#### FR-", ft, re.M)))
        for f in sorted(req.glob("*Non_Functional_Requirements.md")):
            ft = f.read_text(encoding="utf-8")
            nfr = max(nfr or 0, len(set(re.findall(r"\bNFR-\d+\b", ft))), len(re.findall(r"^#### NFR-", ft, re.M)))
    return {"fr_ids": fr, "nfr_ids": nfr}


def parse_risks(case, cfg, warn):
    muc = set()
    for cand in sorted(x for x in (REPO / cfg["root"]).rglob("*.md") if x.is_file()):
        muc |= set(re.findall(r"\bMUC-[A-Z0-9-]+\b", cand.read_text(encoding="utf-8", errors="ignore")))
    return {"muc_ids": sorted(muc), "muc_count": len(muc)}


def parse_audit(warn):
    res = {}
    t = read(str(AUDIT_REPORT.relative_to(REPO))) if AUDIT_REPORT.exists() else None
    if not t:
        warn.append("traceability audit report missing")
        return res
    for case, row in re.findall(r"^\| (Case_\d\d)[^|]*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|", t, re.M):
        res[case] = {"obj_to_ctrl": row0(row), "ctrl_to_obj": row0(row, 1), "uc_to_obj": row0(row, 2)}
    return res


def row0(cell, idx=0):
    m = re.search(r"(\d+)/(\d+) = ([\d.]+)%", cell if isinstance(cell, str) else "")
    return None


def audit_row(t, case):
    m = re.search(rf"^\| {case} \|([^|]*)\|([^|]*)\|([^|]*)\|", t, re.M)
    if not m:
        return None
    vals = []
    for c in m.groups():
        mm = re.search(r"(\d+)/(\d+) = ([\d.]+)%", c)
        vals.append({"covered": int(mm.group(1)), "total": int(mm.group(2)), "pct": float(mm.group(3))} if mm else None)
    keys = ["obj_to_ctrl", "ctrl_to_obj", "uc_to_obj"]
    return dict(zip(keys, vals))


def build(warn):
    data = {"meta": {}, "cases": {}, "crosscase": {}}
    try:
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True,
                                text=True, cwd=REPO).stdout.strip()
    except Exception:
        commit = None
    data["meta"] = {"generated_at": dt.datetime.now().isoformat(timespec="seconds"),
                    "git_commit": commit, "warnings": warn}
    audit_t = read(str(AUDIT_REPORT.relative_to(REPO)))
    for case, cfg in CASES.items():
        c = {"profile": {"tier": cfg["tier"], "regulations": cfg["regs"]}}
        c["phases"] = {
            "P1": parse_p1(case, cfg, warn),
            "P2": parse_p2(case, cfg, warn),
        }
        cat = parse_catalog(case, cfg, warn)
        lane = parse_lane_cards(case, cfg, warn)
        p3 = {
            "catalog": cat,
            "lane_cards": lane,
            "annexes": parse_annexes(case, cfg),
            "fr_nfr": parse_fr_nfr(case, cfg),
            "risks": parse_risks(case, cfg, warn),
            "gates": parse_p3_gates(case, cfg, warn),
            # Flat aliases expected by AEGIS_Master_Dashboard.html:
            "use_cases": cat["ucs"],
            "proc_cards": lane["proc"],
            "cap_cards":  lane["cap"],
            "requirements": {
                "fr_ids": (parse_fr_nfr(case, cfg) or {}).get("fr_ids"),
                "nfr_ids": (parse_fr_nfr(case, cfg) or {}).get("nfr_ids"),
            },
            "threats": (parse_risks(case, cfg, warn) or {}).get("muc_ids") or [],
            "drill_available": False,
        }
        c["phases"]["P3"] = p3
        c["audit"] = audit_row(audit_t, case.replace("Case_0", "Case_0").replace("Case_01", "Case_01")) if audit_t else None
        if audit_t:
            m = re.search(rf"^\| Case_\d\d \|", audit_t, re.M)
        data["cases"][case] = c
    # crosscase
    data["crosscase"] = {
        "uc_totals": {c: len(data["cases"][c]["phases"]["P3"]["catalog"]["ucs"]) for c in CASES},
        "proc_totals": {c: len(data["cases"][c]["phases"]["P3"]["lane_cards"]["proc"]) for c in CASES},
        "cap_totals": {c: len(data["cases"][c]["phases"]["P3"]["lane_cards"]["cap"]) for c in CASES},
        "audit": {c: data["cases"][c].get("audit") for c in CASES},
    }
    # audit rows properly per case key used in the report (Case_01 style)
    if audit_t:
        for case in CASES:
            data["cases"][case]["audit"] = audit_row(audit_t, case.replace("_TinyTask_SaaS", "").replace("_SecureBorder_Solutions", "").replace("_OmniBank_Financial", ""))
    return data


def inject(html_path, data):
    p = Path(html_path)
    t = p.read_text(encoding="utf-8")
    placeholder = "/*__MASTER_DATA__*/null"
    if placeholder not in t:
        raise SystemExit(f"placeholder {placeholder} not found in {p}")
    blob = json.dumps(data, ensure_ascii=False, indent=1)
    t = t.replace(placeholder, blob, 1)
    p.write_text(t, encoding="utf-8")
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(OUT_DEFAULT))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--inject", default=None, help="HTML template to inject the JSON into")
    args = ap.parse_args()

    warn = []
    data = build(warn)
    data["meta"]["warnings"] = sorted(set(warn))

    # light validation
    errs = []
    for case, c in data["cases"].items():
        ids = [u["id"] for u in c["phases"]["P3"]["catalog"]["ucs"]]
        if len(ids) != len(set(ids)):
            errs.append(f"{case}: duplicate UC ids")
        if not ids:
            errs.append(f"{case}: 0 UCs parsed — grammar mismatch?")
    if errs:
        print("VALIDATION ERRORS:", *errs, sep="\n  ")
        sys.exit(2)

    blob = json.dumps(data, ensure_ascii=False, indent=1)
    print(f"parsed: {sum(data['crosscase']['uc_totals'].values())} UCs, "
          f"{sum(data['crosscase']['proc_totals'].values())} PROC, "
          f"{sum(data['crosscase']['cap_totals'].values())} CAP, "
          f"warnings={len(data['meta']['warnings'])}")
    if args.dry_run:
        print("dry-run: no write")
        return
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(blob, encoding="utf-8")
    print(f"wrote {out} ({len(blob)} bytes)")
    if args.inject:
        inject(args.inject, data)
        print(f"injected into {args.inject}")


if __name__ == "__main__":
    main()
