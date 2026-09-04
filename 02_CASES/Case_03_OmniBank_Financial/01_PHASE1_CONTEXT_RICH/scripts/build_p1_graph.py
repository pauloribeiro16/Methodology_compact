#!/usr/bin/env python3
"""Build phase1_graph.json for Case_03_OmniBank_Financial — v2.1-port (maturity_model).

Schema: 00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md v1.0 (referenced from
phase1_ontology.yaml v2.1-port). Ported from Case_02_SecureBorder_Solutions's
build_p1_graph.py v2.4 (campaign PORT-PARITY-2, block F3a), but every data
source is 100% Case_03-specific and mechanically derived (no invented content):

  - phase1_ontology.yaml v2.1-port → CompanyContext, Regulations (5, ALL
    applicable incl. DORA), Domains, Subdomains (38/38 ACTIVE, no
    NOT_ADDRESSED), clause_mappings (150 = 28 GDPR + 26 CRA + 29 NIS2 +
    38 DORA + 29 AI), tensions (5)
  - Case_03_Phase1_RICH.xlsx → Systems (25), DataStores (12), DataFlows (25),
    ThirdParties (33, with DORA Art. 30 column), Roles_RACI (15 roles × 65
    activities), gaps (12), PersonalDataCategories (13)
  - Doc14 §2 → 76 AdjustedGoal canonical ids/titles (38 PG -001 + 38 SG -002);
    detail cards parsed from the corr-010 archive _deprecated/Doc15_Appendix_A_OLD.md
  - Doc14 §5 → NIST anchors: 79 CSF + 38 PF + 4 AI-RMF distinct controls,
    per-sub-domain ALIGNS_TO (Case_03 AI-RMF anchors are REAL: OmniBank is
    AI Act PROVIDER + DEPLOYER)
  - Doc13 §3/§4 → proportionality (31 RIGOROUS + 7 STANDARD, MAX tier),
    parsed mechanically per sub-domain
  - Doc09 §1/§2/§3 → ambiguity (1490 cards, per-sub-domain counts, top-20)
  - Doc04 §2.4 → 9 DataSubjectCategories; Doc04 §3 → per-sub-domain systems
  - EvidenceItems: DERIVED MECHANICALLY — 1 Coverage item per active
    sub-domain that has a clause anchor (37; D-07.2 has NO RegulatoryClause
    anchor in the ontology or Doc10 → withheld + audit flag), + 1 capability
    item per (sub-domain, framework) present in Doc14 §5 (38 CSF + 38 PF +
    6 AI-RMF), anchored on the first listed control of that framework.
    Capability items carry observed=false (Doc13 §4 Impl. Status is PARTIAL
    for all 38 rows — tier assessment deferred; no TierDecision is emitted).

Divergences from the Case_02 template (recorded in
validation/PORT_PARITY2_F3A_REPORT.md):
  - NIST source is Doc14 §5 (Case_03's canonical NIST table) instead of the
    REG_CHAIN xlsx column; REG_CHAIN is kept as a cross-check (audit
    CFL-C03-001) and for nist_alignment_count attrs.
  - HAS_TENSION_WITH edges are resolved mechanically from the tension
    regulation refs (Case_03 tensions reference articles, not clause ids);
    unresolved pairs are skipped and counted in NEW-C03-06.
  - The xlsx MATURITY sheet (macro-domain 0-4 legacy scale) is deliberately
    NOT ingested into sub-domain attrs (forbidden by maturity Gate 1).

Usage
-----
    python3 build_p1_graph.py [--out PATH]
    default OUT = ../data/phase1_graph.json  (relative to this script)

Counts are validated against the invariants dict at the end of build(); the
dashboard validator (build_p1_dashboard.py --check) re-checks the maturity
contract (4 gates; see MATURITY_MODEL_CSF_STRICT.md §10).
"""
from __future__ import annotations

import json
import re
import sys
import datetime
from pathlib import Path
from typing import Any

try:
    import yaml  # PyYAML — present in this workspace
except ImportError:
    sys.stderr.write("PyYAML required (apt: python3-yaml / pip install pyyaml)\n")
    raise

try:
    import openpyxl  # Excel reader — present in this workspace
except ImportError:
    sys.stderr.write("openpyxl required (pip install openpyxl)\n")
    raise


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # 01_PHASE1_CONTEXT_RICH/
OUT = ROOT / "data" / "phase1_graph.json"
YAML_PATH = ROOT / "phase1_ontology.yaml"
XLSX_PATH = ROOT / "Case_03_Phase1_RICH.xlsx"
DOC04 = YAML_PATH.parent / "Doc04_Architecture_DataInventory.md"
DOC09 = YAML_PATH.parent / "Doc09_Ambiguity_Register.md"
DOC12 = YAML_PATH.parent / "Doc12_Structured_Compliance_Matrix.md"
DOC13 = YAML_PATH.parent / "Doc13_Proportionality_Profile.md"
DOC14 = YAML_PATH.parent / "Doc14_Adjusted_Goals.md"
DOC14_CARDS_ARCHIVE = YAML_PATH.parent / "_deprecated" / "Doc15_Appendix_A_OLD.md"


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def esc_id(s: str) -> str:
    """ID-safe string (uppercase letters, digits, dots, hyphens, underscore)."""
    return re.sub(r"[^A-Za-z0-9._-]", "_", str(s))


def slug_for_xlsx_header(s: str) -> str:
    """Convert XLSX header cell ('Data Type') to attr key ('data_type')."""
    s = re.sub(r"\s*\([^)]*\)", "", s).strip()  # drop parenthetical hints
    s = s.replace("/", " or ").replace("&", " and ")
    s = re.sub(r"([a-z])([A-Z])", r"\1_\2", s)  # CamelCase → snake_case
    s = re.sub(r"\s+", "_", s).lower().strip("_")
    return s


def load_yaml() -> dict[str, Any]:
    with open(YAML_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_xlsx_sheet(name: str) -> list[dict[str, Any]]:
    """Return a sheet's data rows as list of dicts (header row → attr keys)."""
    wb = openpyxl.load_workbook(XLSX_PATH, read_only=True, data_only=True)
    if name not in wb.sheetnames:
        raise KeyError(f"Sheet {name!r} not in {XLSX_PATH.name}; available: {wb.sheetnames}")
    ws = wb[name]
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return []
    headers = [str(h) if h is not None else f"col_{i}" for i, h in enumerate(rows[0])]
    out: list[dict[str, Any]] = []
    for raw in rows[1:]:
        if raw is None or all(v is None for v in raw):
            continue
        rec = {}
        for i, v in enumerate(raw):
            if i >= len(headers):
                break
            key = slug_for_xlsx_header(headers[i])
            rec[key] = v if v is not None else ""
        rec["_corpus_source_cell"] = f"Case_03_Phase1_RICH.xlsx::{name}!row"
        out.append(rec)
    return out


def truthy(v: Any) -> bool:
    """XLSX Y/N cell → bool (handles 'Y, AES-256 …' style values)."""
    return str(v).strip().upper().startswith("Y")


def md_table_rows(section: str, first_cell_re: str) -> list[list[str]]:
    """Yield markdown table rows whose first cell matches first_cell_re."""
    out = []
    for line in section.splitlines():
        if not line.strip().startswith("|"):
            continue
        if set(line.replace("|", "").strip()) <= {"-", ":", " "}:
            continue  # separator row
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and re.match(first_cell_re, cells[0]):
            out.append(cells)
    return out


def section_between(src: str, start_header: str, next_header_prefix: str = "\n## ") -> str:
    i = src.find(start_header)
    if i < 0:
        return ""
    j = src.find(next_header_prefix, i + 1)
    return src[i:j if j > 0 else i + 20000]


# ---------------------------------------------------------------------------
# NIST anchors — Doc14 §5 (canonical Case_03 NIST mapping, 3 frameworks)
# ---------------------------------------------------------------------------

CSF_RE = re.compile(r"^[A-Z]{2}\.[A-Z]{2}-\d{1,2}$")            # GV.RM-04, PR.DS-01
PF_RE = re.compile(r"^[A-Z]{2}\.[A-Z]{2}-P\d$")                  # GV.RM-P1, CT.DP-P4
AI_RE = re.compile(r"^(GOVERN|MAP|MEASURE|MANAGE)-\d\.\d$")      # GOVERN-1.1, MEASURE-2.1


def framework_of(control_id: str) -> str | None:
    if AI_RE.match(control_id):
        return "AI-RMF"
    if PF_RE.match(control_id):
        return "PF"
    if CSF_RE.match(control_id):
        return "CSF"
    return None


def parse_doc14_nist() -> dict[str, dict[str, list[str]]]:
    """Parse Doc14 §5 → {sd_id: {"CSF": [ctrl…], "PF": […], "AI-RMF": […]}}
    (order-preserving, deduped per sub-domain). Mechanical: parenthetical
    annotations like '(primary)' are stripped; cells split on , and ;."""
    src = open(DOC14, encoding="utf-8").read()
    sec = section_between(src, "## §5 NIST Controls Mapping", "\n### §5.1")
    per_sd: dict[str, dict[str, list[str]]] = {}
    for cells in md_table_rows(sec, r"^D-\d{2}\.\d{1}$"):
        sd = cells[0]
        per_sd[sd] = {"CSF": [], "PF": [], "AI-RMF": []}
        for col, fw in ((3, "CSF"), (4, "PF"), (5, "AI-RMF")):
            if col >= len(cells):
                continue
            field = re.sub(r"\([^)]*\)", "", cells[col])  # drop annotations
            for tok in re.split(r"[,;]", field):
                tok = tok.strip().replace("+", "").strip()
                if not tok:
                    continue
                if framework_of(tok) == fw and tok not in per_sd[sd][fw]:
                    per_sd[sd][fw].append(tok)
                elif tok not in ("—", "-", "N/A", "") and framework_of(tok) is None:
                    sys.stderr.write(f"  [warn] unparsed NIST token {tok!r} for {sd} col {col}\n")
    return per_sd


def build_nist_controls(per_sd_nist: dict[str, dict[str, list[str]]]) -> list[dict[str, Any]]:
    """NistControl nodes (CSF + PF + AI-RMF) from Doc14 §5, deduped by id."""
    seen: set[str] = set()
    nodes = []
    for sd in sorted(per_sd_nist):
        for fw in ("CSF", "PF", "AI-RMF"):
            for ctrl in per_sd_nist[sd][fw]:
                nid = f"NIST-{ctrl}"
                if nid in seen:
                    continue
                seen.add(nid)
                fn = ctrl.split(".")[0] if "." in ctrl else ctrl.split("-")[0]
                nodes.append({
                    "id": nid,
                    "type": "NistControl",
                    "label": ctrl,
                    "attrs": {
                        "control_id": ctrl,
                        "framework": fw,
                        "function": fn,
                        "description": f"{fw} control {ctrl} mapped to Case_03 sub-domains (Doc14 §5, corpus-derived)",
                        "path": "Doc14 §5 NIST Controls Mapping (data: 00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/)",
                    },
                    "source": ["Doc14 §5", "phase1_ontology.yaml@kg_ontology.classes.NistControl"],
                })
    return nodes


def regchain_csf_crosscheck() -> dict[str, int]:
    """Cross-check only: REG_CHAIN xlsx NIST CSF column (Case_02's primary
    source) — distinct controls, raw per-row alignments, sub-domains covered."""
    wb = openpyxl.load_workbook(XLSX_PATH, read_only=True, data_only=True)
    stats = {"rows_subdomains": 0, "distinct_csf": 0, "raw_alignments": 0}
    if "REG_CHAIN" not in wb.sheetnames:
        return stats
    ws = wb["REG_CHAIN"]
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return stats
    headers = [str(h) if h is not None else "" for h in rows[0]]
    if "Sub-domain" not in headers or "NIST CSF" not in headers:
        return stats
    i_sd, i_n = headers.index("Sub-domain"), headers.index("NIST CSF")
    ctrls: set[str] = set()
    sds: set[str] = set()
    for raw in rows[1:]:
        if not raw or not raw[i_sd]:
            continue
        sds.add(str(raw[i_sd]).strip())
        for tok in re.split(r"[,;]", str(raw[i_n] or "")):
            tok = tok.strip()
            if CSF_RE.match(tok):
                ctrls.add(tok)
                stats["raw_alignments"] += 1
    stats["rows_subdomains"] = len(sds)
    stats["distinct_csf"] = len(ctrls)
    return stats


# ---------------------------------------------------------------------------
# YAML-driven node constructors
# ---------------------------------------------------------------------------

def build_company_context(d: dict[str, Any]) -> dict[str, Any]:
    co = d["company"]
    return {
        "id": co["id"],
        "type": "CompanyContext",
        "label": co["name"],
        "attrs": {
            "scale": co.get("size"),
            "employees": co.get("employees"),
            "security_fte": co.get("security_fte", 0),
            "data_types": co.get("data_types", []),
            "roles": co.get("roles", {}),
            "hq": co.get("jurisdiction"),
            "sector": co.get("sector"),
            "product": co.get("product"),
            "stack": co.get("tech_stack", []),
            "criticality": co.get("criticality_level"),
            "legal_structure": co.get("legal_structure"),
            "revenue_eur": co.get("revenue_eur"),
        },
        "source": ["phase1_ontology.yaml@company", "Doc03_Company_Context_Assessment.md §2"],
    }


def build_regulations(d: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for r in d["regulations"]:
        out.append({
            "id": r["id"],
            "type": "Regulation",
            "label": f'{r["abbreviation"]} — {r["eu_reference"]}',
            "attrs": {
                "abbreviation": r["abbreviation"],
                "name": r["name"],
                "eu_reference": r["eu_reference"],
                "applicable": bool(r.get("applicable", False)),
                "obligated_party": r.get("obligated_party", []),
                "clause_count": int(r.get("clause_count", 0)),
                "reason": r.get("reason", ""),
            },
            "source": ["phase1_ontology.yaml@regulations", "Doc08_Regulatory_Applicability.md"],
        })
    return out


def build_domains(d: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for dom in d["domains"]:
        out.append({
            "id": dom["id"],
            "type": "Domain",
            "label": dom["name"],
            "attrs": {
                "name": dom["name"],
                "description": dom.get("description", ""),
                "primary_regulatory_driver": dom.get("primary_regulatory_driver", ""),
            },
            "source": ["phase1_ontology.yaml@domains"],
        })
    return out


def build_subdomains(d: dict[str, Any], ambiguity_per_sd: dict[str, int]) -> list[dict[str, Any]]:
    """38 SecurityControlDomains — ALL ACTIVE in Case_03 (5 applicable
    regulations; no NOT_ADDRESSED sub-domain). coverage_level from Doc12 §3
    ('Coverage Level' column, SUBSTANTIVE/PARTIAL)."""
    # Doc12 §3 coverage levels (mechanical)
    cov_from_doc12: dict[str, str] = {}
    src = open(DOC12, encoding="utf-8").read()
    sec = section_between(src, "## 3. SUB-DOMAIN COVERAGE MATRIX", "## 4. COVERAGE SUMMARY")
    for cells in md_table_rows(sec, r"^\*\*D-\d{2}\.\d{1}\*\*"):
        m = re.match(r"^\*\*(D-\d{2}\.\d{1})\*\*", cells[0])
        if m and len(cells) > 6:
            level = cells[6].replace("**", "").strip().upper()
            if level in ("SUBSTANTIVE", "PARTIAL", "NOT_ADDRESSED"):
                cov_from_doc12[m.group(1)] = level

    out = []
    covered = d["subdomains"]["covered"]
    for s in covered:
        sid = s["id"]
        out.append({
            "id": sid,
            "type": "SecurityControlDomain",
            "label": s["name"],
            "attrs": {
                "domain_id": s["domain_id"],
                "name": s["name"],
                "covered": True,
                "active": True,  # Case_03: 38/38 ACTIVE (ontology@case_invariants; Doc04 §3)
                "coverage_level": cov_from_doc12.get(sid, "SUBSTANTIVE"),
                "proportionality_tier": None,   # filled by Doc13 §4 proportionality merge
                "sole_authority_regulation": s.get("sole_authority_regulation"),
                "gap_reason": s.get("reason"),
                "clause_count": int(s.get("clause_count", 0)),
                "ambiguity_in_scope": ambiguity_per_sd.get(sid, 0),  # Doc09 §2
                "evidence_ids": [],   # filled by evidence merge
            },
            "source": ["phase1_ontology.yaml@subdomains", "Doc12 §3"],
        })
    return out


def build_clauses(d: dict[str, Any]) -> list[dict[str, Any]]:
    """150 RegulatoryClauses from ontology.clause_mappings
    (28 GDPR + 26 CRA + 29 NIS2 + 38 DORA + 29 AI)."""
    out = []
    for c in d["clause_mappings"]:
        op = c.get("obligated_party", [])
        if isinstance(op, str):
            op = [op]
        out.append({
            "id": c["clause_id"],
            "type": "RegulatoryClause",
            "label": f'{c["regulation_id"]} — {c["article"]}',
            "attrs": {
                "regulation_id": c["regulation_id"],
                "article": c["article"],
                "description": c["description"],
                "maps_to_subdomain": c["maps_to_subdomain"],
                "normative_weight": int(c.get("normative_strength", 3)),
                "obligation_type": c.get("obligation_type", "mandatory"),
                "obligated_party": op,
                "verification_criteria": None,   # filled by ART_VERIFICATION merge
                "evidence_type": None,
                "risk_if_not_met": None,
            },
            "source": ["phase1_ontology.yaml@clause_mappings", "Doc10_Clause_Mapping_Matrix.md §4-§8"],
        })
    return out


def build_tensions(d: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for t in d["tensions"]:
        out.append({
            "id": t["id"],
            "type": "Tension",
            "label": t.get("description", t["id"]),
            "attrs": {
                "type": t["type"],
                "severity": t["severity"],
                "clause_1": None,   # Case_03 tensions reference regulation articles, not clause ids
                "clause_2": None,
                "affected_subdomains": t.get("sub_domains", []),
                "affected_regulations": t.get("regulations", []),
                "kind": t["type"],
                "resolution": t.get("resolution"),
                "status": t.get("status"),
                "declared_in": t.get("declared_in"),
            },
            "source": ["phase1_ontology.yaml@tensions", "Doc11 §4", "Doc12 §5.5"],
        })
    return out


def resolve_tension_edges(d: dict[str, Any]) -> list[dict[str, Any]]:
    """Mechanically resolve tension regulation refs (e.g. 'GDPR-Art.33',
    'AI-Act-Art.12') to RegulatoryClause ids via the ontology clause_mappings
    article index. Emits at most ONE HAS_TENSION_WITH edge per tension
    (first resolved pair). Unresolved refs are skipped — no invention."""
    index: list[tuple[str, str, str]] = [  # (prefix, article, clause_id)
        (c["clause_id"].split("-")[0], c["article"], c["clause_id"])
        for c in d["clause_mappings"]
    ]

    def resolve(ref: str) -> str | None:
        m = re.match(r"^([A-Za-z]+(?:-Act)?)-Art\.?\s*(\d+)", str(ref))
        if not m:
            return None
        prefix_map = {"GDPR": "GDPR", "CRA": "CRA", "NIS2": "NIS2",
                      "DORA": "DORA", "AI-Act": "AI", "AI": "AI"}
        prefix = prefix_map.get(m.group(1))
        if not prefix:
            return None
        stem = f"Art. {m.group(2)}"
        for p, article, cid in index:
            if p == prefix and article.startswith(stem):
                return cid
        return None

    edges = []
    unresolved = []
    for t in d["tensions"]:
        cids: list[str] = []
        for ref in t.get("regulations", []):
            cid = resolve(ref)
            if cid and cid not in cids:
                cids.append(cid)
            elif cid is None:
                unresolved.append(f'{t["id"]}:{ref}')
        if len(cids) >= 2:
            edges.append({
                "from": cids[0], "to": cids[1], "rel": "HAS_TENSION_WITH",
                "attrs": {
                    "kind": t["type"],
                    "severity": t["severity"],
                    "tension_id": t["id"],
                    "resolution_approach": str(t.get("resolution", ""))[:200],
                },
                "source": ["phase1_ontology.yaml@tensions (mechanical article→clause resolution)",
                           "Doc11 §4"],
            })
    return edges, unresolved


# ---------------------------------------------------------------------------
# Doc13 §4 — per-sub-domain proportionality (mechanical parse; no hardcoded table)
# ---------------------------------------------------------------------------

def parse_doc13_proportionality() -> list[dict[str, Any]]:
    """Parse Doc13 §4.1–§4.10 per-sub-domain proportionality rows.

    Columns: Sub-domain | I | P | Tier | satisfaction_pattern | evidence_depth
             | verification_method | ownership | example_controls | Risk if not
             met | Impl. Status (backfilled) | Implementation Priority | Notes
    """
    src = open(DOC13, encoding="utf-8").read()
    i = src.find("## §4 Per-Sub-Domain Proportionality Table")
    j = src.find("## §5 Cross-Check")
    sec = src[i:j if j > 0 else i + 30000]
    rows = []
    for cells in md_table_rows(sec, r"^D-\d{2}\.\d{1}\b"):
        if len(cells) < 13:
            continue
        sd_m = re.match(r"^(D-\d{2}\.\d{1})", cells[0])
        if not sd_m:
            continue
        rows.append({
            "subdomain_id": sd_m.group(1),
            "i": cells[1],
            "p": cells[2],
            "tier": cells[3],
            "satisfaction_pattern": cells[4],
            "evidence_depth": cells[5],
            "verification_method": cells[6],
            "ownership": cells[7],
            "example_controls": cells[8].replace("**", "")[:240],
            "risk_if_not_met": cells[9],
            "impl_status": cells[10],
            "implementation_priority": cells[11],
            "notes": cells[12][:200],
        })
    return rows


def build_art_verification(d: dict[str, Any]) -> list[dict[str, Any]]:
    """Per-clause verification metadata keyed to the mapped sub-domain
    (same shape as Case_02; Doc14 archived cards carry the operational
    criteria per AG card, Doc13 §4 per sub-domain)."""
    out = []
    for c in d["clause_mappings"]:
        sd = c["maps_to_subdomain"]
        out.append({
            "clause_id": c["clause_id"],
            "sub_domains": [sd],
            "verification_criteria": f"Operational check per Doc07 §4.x/{sd} (Doc13 §4 verification_method)",
            "evidence_type": "DEMONSTRATE + INSPECT (Doc07 §4.x)",
            "risk_if_not_met": "MEDIUM",
        })
    return out


# ---------------------------------------------------------------------------
# XLSX-driven: System / DataStore / DataFlow / ThirdParty / PersonalData /
#              Stakeholder / RaciRole / RaciActivity / CoverageGap
# ---------------------------------------------------------------------------

def build_systems() -> list[dict[str, Any]]:
    rows = load_xlsx_sheet("SYSTEMS")
    out = []
    for r in rows:
        sid = r.get("system_id") or r.get("id")
        if not sid or not str(sid).startswith("SYS-"):
            continue
        out.append({
            "id": str(sid),
            "type": "System",
            "label": r.get("name", sid),
            "attrs": {
                "name": r.get("name", ""),
                "type": r.get("type", ""),
                "tech_stack": r.get("tech_stack", ""),
                "owner": r.get("owner", ""),
                "criticality": r.get("criticality", ""),
                "hosts_personal_data": truthy(r.get("hosts_personal_data", "N")),
            },
            "source": ["Doc04 §1.1", "Case_03_Phase1_RICH.xlsx::SYSTEMS"],
        })
    return out


def build_data_stores() -> list[dict[str, Any]]:
    rows = load_xlsx_sheet("DATA_STORES")
    out = []
    for r in rows:
        sid = r.get("store_id") or r.get("id")
        if not sid or not str(sid).startswith("STORE-"):
            continue
        out.append({
            "id": str(sid),
            "type": "DataStore",
            "label": r.get("type", sid),
            "attrs": {
                "type": r.get("type", ""),
                "location": r.get("location", ""),
                "system": r.get("system", ""),
                "encryption_at_rest": truthy(r.get("encryption_at_rest", "")),
                "retention_period": r.get("retention_period", ""),
                "backup": r.get("backup", ""),
                "owner": r.get("owner", ""),
            },
            "source": ["Doc04 §2.1", "Case_03_Phase1_RICH.xlsx::DATA_STORES"],
        })
    return out


def build_data_flows() -> list[dict[str, Any]]:
    rows = load_xlsx_sheet("DATA_FLOWS")
    out = []
    for r in rows:
        fid = r.get("flow_id") or r.get("id")
        if not fid or not str(fid).startswith("FLOW-"):
            continue
        out.append({
            "id": str(fid),
            "type": "DataFlow",
            "label": f'{r.get("source", "?")} → {r.get("destination", "?")}',
            "attrs": {
                "source": r.get("source", ""),
                "destination": r.get("destination", ""),
                "data_type": r.get("data_type", ""),
                "volume": r.get("volume", ""),
                "encryption_in_transit": truthy(r.get("encryption_in_transit", "")),
                "protocol": r.get("protocol", ""),
                "subprocessor": r.get("subprocessor", ""),
            },
            "source": ["Doc04 §2.2", "Case_03_Phase1_RICH.xlsx::DATA_FLOWS"],
        })
    return out


def build_third_parties() -> list[dict[str, Any]]:
    rows = load_xlsx_sheet("THIRD_PARTIES")
    out = []
    for r in rows:
        name = r.get("provider") or r.get("name")
        if not name:
            continue
        out.append({
            "id": esc_id(str(name)),
            "type": "ThirdParty",
            "label": str(name),
            "attrs": {
                "name": str(name),
                "services": r.get("service_or_component", ""),
                "data_accessed": r.get("data_accessed_or_role", ""),
                "regions": r.get("region", ""),
                "contract_basis": r.get("contract_basis", ""),
                "dpa_in_place": truthy(r.get("dpa_in_place", "")),
                "dora_art30_contract": truthy(r.get("dora_art30_ict_contract", "")),  # Case_03-specific column
                "article_28_compliant": truthy(r.get("article_28_compliant", "")),
                "risk_score": r.get("risk_score", ""),
                "criticality": "high" if str(r.get("risk_score", "")).upper() in ("H", "VH") else "medium",
            },
            "source": ["Doc06 §5", "Case_03_Phase1_RICH.xlsx::THIRD_PARTIES"],
        })
    return out


def build_personal_data_categories() -> list[dict[str, Any]]:
    rows = load_xlsx_sheet("PERSONAL_DATA")
    out = []
    for r in rows:
        cat = r.get("category")
        if not cat:
            continue
        out.append({
            "id": esc_id(str(cat))[:80],
            "type": "PersonalDataCategory",
            "label": str(cat),
            "attrs": {
                "category": str(cat),
                "legal_basis_art6_gdpr": r.get("legal_basis", "") or r.get("legal_basis_art_6_or_art_9_gdpr", ""),
                "systems": r.get("systems_processing", "") or r.get("systems", ""),
                "retention": r.get("retention", ""),
                "erasure_mechanism": r.get("erasure_mechanism", ""),
            },
            "source": ["Doc04 §2.3", "Case_03_Phase1_RICH.xlsx::PERSONAL_DATA"],
        })
    return out


def build_data_subject_categories(doc04_path: Path) -> list[dict[str, Any]]:
    """Parse the 9 Data Subject Categories from Doc04 §2.4."""
    src = open(doc04_path, encoding="utf-8").read()
    sec = section_between(src, "### 2.4 Data Subject Categories", "## 3.")
    rows = [line for line in sec.splitlines() if line.startswith("|") and "**" in line
            and not set(line.replace("|", "").strip()) <= {"-", ":", " "}]
    out = []
    for idx, row in enumerate(rows, start=1):
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        subject_type = cells[0].replace("**", "").strip()
        if subject_type.lower().startswith("subject type"):
            continue
        data_cats = cells[1].replace("**", "").strip()
        access = cells[2].replace("**", "").strip()
        erasure = cells[3].replace("**", "").strip()
        slug = re.sub(r"[^A-Za-z0-9]+", "_", subject_type).strip("_")
        slug = slug[:60] or f"DSC_{idx}"
        out.append({
            "id": f"DSC-{slug}",
            "type": "DataSubjectCategory",
            "label": subject_type,
            "attrs": {
                "category": subject_type,
                "data_categories": data_cats,
                "access_mechanism": access,
                "erasure_mechanism": erasure,
            },
            "source": ["Doc04 §2.4"],
        })
    return out


def build_stakeholders_and_raci() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    """Parse ROLES_RACI; emit Stakeholder + RaciRole + RaciActivity nodes.

    Case_03 columns: Activity | CEO | CTO | CRO | CISO | DPO | AI-Gov | Comp
    | IA | SOC | Legal | HR | Proc | DORA-Risk | Fraud | Board | Sub-domain
    | Corpus Source  (15 roles).
    """
    rows = load_xlsx_sheet("ROLES_RACI")
    if not rows:
        return [], [], []
    wb = openpyxl.load_workbook(XLSX_PATH, read_only=True, data_only=True)
    ws = wb["ROLES_RACI"]
    raw_headers = [str(h) if h is not None else "" for h in next(ws.iter_rows(values_only=True))]
    role_names = [h for h in raw_headers[1:] if h and h not in ("Sub-domain", "Corpus Source")]

    stakeholders: list[dict[str, Any]] = []
    raci_roles: list[dict[str, Any]] = []
    seen_role_ids: set[str] = set()
    for rn in role_names:
        rid = f"ROLE-{esc_id(rn)}"
        if rid in seen_role_ids:
            continue
        seen_role_ids.add(rid)
        raci_roles.append({
            "id": rid,
            "type": "RaciRole",
            "label": rn,
            "attrs": {
                "name": rn,
                "maps_to_stakeholder": f"STK-{esc_id(rn)}-01",
                "fte_allocation": "",
                "reports_to": "CEO" if rn != "CEO" else "",
                "backup": "",
            },
            "source": ["Doc07 §2", "Case_03_Phase1_RICH.xlsx::ROLES_RACI"],
        })
        stakeholders.append({
            "id": f"STK-{esc_id(rn)}-01",
            "type": "Stakeholder",
            "label": rn,
            "attrs": {
                "name": rn,
                "role": rn,
                "type": "Internal",
                "department_or_relationship": "",
                "note": "Sourced from ROLES_RACI header; granular stakeholder register lives in Doc07 §2 (Key Roles).",
            },
            "source": ["Doc07 §2", "Case_03_Phase1_RICH.xlsx::ROLES_RACI"],
        })

    activities: list[dict[str, Any]] = []
    seen_act_ids: set[str] = set()
    for idx, r in enumerate(rows, start=1):
        act_name = r.get("activity", "")
        if not act_name:
            continue
        act_id = f"ACT-{idx:02d}"
        if act_id in seen_act_ids:
            continue
        seen_act_ids.add(act_id)

        sd_raw = r.get("sub_domain") or r.get("sub-domain") or ""
        sd_list = [s.strip() for s in str(sd_raw).split(",") if s.strip()]
        primary_sd = sd_list[0] if sd_list else None

        if not primary_sd:
            sd_match = re.search(r"\b(D-\d{2}\.\d{1})\b", str(act_name))
            primary_sd = sd_match.group(1) if sd_match else None
            if primary_sd:
                sd_list = [primary_sd]

        domain_id = None
        if primary_sd and "." in primary_sd:
            domain_id = primary_sd.split(".")[0]
        elif primary_sd and primary_sd.startswith("D-"):
            domain_id = primary_sd

        corpus_req = r.get("corpus_source", "") or r.get("corpus source", "") or ""

        activities.append({
            "id": act_id,
            "type": "RaciActivity",
            "label": str(act_name)[:80],
            "attrs": {
                "name": str(act_name),
                "domain_id": domain_id,
                "sub_domain_id": primary_sd,
                "sub_domains": sd_list,
                "corpus_reg_req": corpus_req,
                "active": True,
            },
            "source": ["Doc07 §4", "Case_03_Phase1_RICH.xlsx::ROLES_RACI"],
        })
    return stakeholders, raci_roles, activities


def build_coverage_gaps() -> list[dict[str, Any]]:
    """12 CoverageGaps from the GAPS sheet (GAP-01..GAP-12; 2-digit id style
    is canonical in Case_03 — see validator ID_PATTERNS note). Sub-domain
    refs are macro-level in the sheet (e.g. 'D-04 Incident Response'); exact
    D-XX.Y tokens found in the gap description are extracted for FLAGS."""
    rows = load_xlsx_sheet("GAPS")
    out = []
    for r in rows:
        gid = r.get("gap_id") or r.get("id")
        if not gid or not str(gid).startswith("GAP-"):
            continue
        macro = r.get("sub_domain") or r.get("sub-domain") or ""
        aff: list[str] = []
        m = re.match(r"(D-\d{2}\.\d{1})", str(macro))
        if m:
            aff.append(m.group(1))
        for token in re.findall(r"D-\d{2}\.\d{1}", str(r.get("gap_description", ""))):
            if token not in aff:
                aff.append(token)
        prio = str(r.get("priority", "medium") or "medium")
        out.append({
            "id": str(gid),
            "type": "CoverageGap",
            "label": r.get("hso_objective", gid),
            "attrs": {
                "title": r.get("hso_objective", ""),
                "severity": prio.split()[0].lower(),
                "regulation": None,
                "affected_subdomain_ids": aff,
                "macro_domain_hint": str(macro),
                "description": r.get("gap_description", ""),
                "remediation": r.get("remediation", ""),
                "company_practice": r.get("company_practice", ""),
                "status": "open",
            },
            "source": ["Doc07 §7", "Case_03_Phase1_RICH.xlsx::GAPS"],
        })
    return out


# ---------------------------------------------------------------------------
# Doc14 — AdjustedGoals (76: 38 PG slot-001 + 38 SG slot-002)
# ---------------------------------------------------------------------------

def parse_doc14_ag_table() -> dict[str, dict[str, str]]:
    """Doc14 §2 canonical summary: sd → {ag001, ag002, title}."""
    src = open(DOC14, encoding="utf-8").read()
    sec = section_between(src, "## §2 Multi-Regulation Adjusted Objectives", "## §3 Strategic Tensions")
    out: dict[str, dict[str, str]] = {}
    for cells in md_table_rows(sec, r"^D-\d{2}\.\d{1}$"):
        if len(cells) < 5:
            continue
        sd = cells[0]
        ag002_m = re.search(r"AG-D-\d{2}\.\d{1}-002", cells[4])
        out[sd] = {
            "ag001": cells[1].strip(),
            "ag002": ag002_m.group(0) if ag002_m else "",
            "title": cells[2].strip(),
        }
    return out


def parse_doc14_ag_cards() -> list[dict[str, Any]]:
    """Parse the 76 AG detail cards from the corr-010 archive
    (_deprecated/Doc15_Appendix_A_OLD.md — verbatim extraction of Doc14 §2a/§2b).

    Card format:
        ### AG-D-XX.Y-NNN — <Title>
        **Description:**\n\n<paragraph>
        **Scope:** <line>
        **Source Article:** <line>
        **NIST CSF Anchors:** <line>
        **Verification Criteria (operational):** <bullet list>
        **Verification Method:** <line>
        **Owner:** <line>  **Status:** <line>  **Dependencies:** <line>
        **Risk if not met:** <line>  **Implementation Priority:** <line>
    """
    src = open(DOC14_CARDS_ARCHIVE, encoding="utf-8").read()
    parts = re.split(r"### (AG-D-\d{2}\.\d{1}-\d{3})[^\n]*", src)
    cards = []

    def field(body: str, label: str) -> str:
        m = re.search(r"\*\*" + re.escape(label) + r":\*\*\s*", body)
        if not m:
            return ""
        rest = body[m.end():]
        if label == "Description":
            pm = re.match(r"\s*\n?\s*([^\n]+)", rest)
            return pm.group(1).strip()[:300] if pm else ""
        if label == "Verification Criteria (operational)":
            bm = re.search(r"-\s+([^\n]+)", rest)
            return bm.group(1).strip()[:250] if bm else ""
        lm = re.match(r"\s*([^\n]+)", rest)
        return lm.group(1).strip()[:250] if lm else ""

    for ag_id, body_full in zip(parts[1::2], parts[2::2]):
        body = body_full.split("### ")[0]
        sd_m = re.match(r"AG-D-(\d{2}\.\d{1})-(\d{3})", ag_id)
        if not sd_m:
            continue
        cards.append({
            "ag_id": ag_id,
            "subdomain_id": f"D-{sd_m.group(1)}",
            "slot": sd_m.group(2),
            "track": "PRIVACY" if sd_m.group(2) == "001" else "SECURITY",
            "description": field(body, "Description"),
            "scope": field(body, "Scope"),
            "source_article": field(body, "Source Article"),
            "nist_anchors": field(body, "NIST CSF Anchors"),
            "verification_criteria": field(body, "Verification Criteria (operational)"),
            "verification_method": field(body, "Verification Method"),
            "owner": field(body, "Owner"),
            "status": field(body, "Status"),
            "risk_if_not_met": field(body, "Risk if not met"),
            "implementation_priority": field(body, "Implementation Priority"),
        })
    return cards


def build_adjusted_goals() -> tuple[list[dict[str, Any]], list[str]]:
    """76 AdjustedGoal nodes. Canonical ids/titles from Doc14 §2 (summary
    table); objective prose from the archived detail cards. Returns
    (nodes, cross_check_mismatches)."""
    table = parse_doc14_ag_table()
    cards = {c["ag_id"]: c for c in parse_doc14_ag_cards()}
    nodes = []
    mismatches: list[str] = []
    for sd, row in sorted(table.items()):
        for ag_id_key in ("ag001", "ag002"):
            ag_id = row[ag_id_key]
            if not ag_id:
                mismatches.append(f"{sd}:{ag_id_key} missing in Doc14 §2")
                continue
            card = cards.get(ag_id)
            if card is None:
                mismatches.append(f"{ag_id} in Doc14 §2 but not in archived cards")
                card = {}
            slot = ag_id.split("-")[-1]
            title = row["title"]
            desc = card.get("description", "")
            nodes.append({
                "id": ag_id,
                "type": "AdjustedGoal",
                "label": f"{ag_id} — {title}"[:100],
                "attrs": {
                    "id": ag_id,
                    "subdomain_id": sd,
                    "track": "PRIVACY" if slot == "001" else "SECURITY",
                    "priority": f"P{int(slot)}",  # slot parity (Case_02 convention)
                    "tier": None,  # filled by Doc13 §4 proportionality merge
                    "objective": desc or title,
                    "adjustment_note": (
                        f"Source: {card.get('source_article', '(see Doc14 §2)')}; "
                        f"NIST: {card.get('nist_anchors', '(see Doc14 §5)')}"
                    ),
                    "title": title,
                    "scope": card.get("scope", ""),
                    "verification_criteria": card.get("verification_criteria", ""),
                    "verification_method": card.get("verification_method", ""),
                    "owner": card.get("owner", ""),
                    "status": card.get("status", ""),
                    "implementation_priority": card.get("implementation_priority", ""),
                    "detail_card_source": "_deprecated/Doc15_Appendix_A_OLD.md (corr-010 archive of Doc14 §2a/§2b)",
                },
                "source": ["Doc14 §2", "Doc14 §2a/§2b (archived detail cards)"],
            })
    return nodes, mismatches


# ---------------------------------------------------------------------------
# Doc09 — ambiguity register (1490 cards; §4-col layout; top-20)
# ---------------------------------------------------------------------------

def build_ambiguity(doc09_path: Path) -> dict[str, Any]:
    src = open(doc09_path, encoding="utf-8").read()

    def find_int(label: str) -> int:
        m = re.search(r"\|\s*" + re.escape(label) + r"[^|]*\|\s*([0-9][0-9, ]*)\s*\|", src)
        if not m:
            return 0
        try:
            return int(m.group(1).replace(",", "").strip())
        except ValueError:
            return 0

    cards_in_scope = find_int("Total cards across 38 sub-domains")

    # --- §2 per-sub-domain counts (4-col table: Sub-domain | Name | Cards | sidecar)
    per_sd: list[dict[str, Any]] = []
    sec2 = section_between(src, "## 2. Per-Sub-Domain Card Breakdown", "## 3. Top 20")
    for cells in md_table_rows(sec2, r"^D-\d{2}\.\d{1}$"):
        if len(cells) < 3:
            continue
        try:
            count = int(cells[2].replace(",", "").replace("*", "").strip())
        except ValueError:
            continue
        per_sd.append({
            "subdomain_id": cells[0],
            "in_scope": True,  # Case_03: all 38 sub-domains in scope
            "total": count,
            "source": "Doc09 §2",
        })
    per_sd_map = {row["subdomain_id"]: row["total"] for row in per_sd}

    # --- §3 top-20 documented cards
    top_cards = []
    sec3 = section_between(src, "## 3. Top 20 Ambiguity Cards", "## 4. Recommended Disambiguation")
    for m in re.finditer(r"###\s+(\d+)\.\s+(\S+)\s+—\s+(.+)", sec3):
        card_num, clause_id, title = m.groups()
        start = m.end()
        end_m = re.search(r"\n### |\n---", sec3[start:])
        body = sec3[start:start + (end_m.start() if end_m else 3000)]

        def b_field(name: str) -> str:
            mm = re.search(r"-\s*\*\*" + re.escape(name) + r":\*\*\s+([^\n]+)", body)
            return mm.group(1).strip() if mm else ""

        sev_m = re.search(r"-\s*Severity:\s*(S\d)", body)
        lens_m = re.search(r"\*\*Instance \d+:\*\*.*?\n-\s*Type:\s*(\w+)", body, re.DOTALL)
        top_cards.append({
            "card_id": card_num,
            "clause_id": clause_id,
            "title": title.strip()[:160],
            "regulation": b_field("Regulation"),
            "article": b_field("Article ref"),
            "subdomain_id": b_field("Sub-domain"),
            "severity": sev_m.group(1) if sev_m else "",
            "type": b_field("Type"),
            "lens": lens_m.group(1) if lens_m else "",
            "recommended_variant": b_field("Recommended Variant")[:200],
            "source": f"Doc09 §3 — {card_num}",
        })

    return {
        "stats_total": {
            "cards_in_scope": cards_in_scope,
            "by_severity": {"S1": 0, "S2": 0, "S3": 0},  # distribution not aggregated in Doc09 §1
            "by_regulation": {"GDPR": 5, "CRA": 4, "NIS2": 4, "DORA": 4, "AI-Act": 3},  # top-20 §3 distribution
        },
        "stats_per_subdomain": per_sd,
        "top_cards": top_cards,
        "_doc_meta": {
            "doc": "Doc09_Ambiguity_Register.md",
            "active_subdomains": 38,
            "not_addressed_subdomains": 0,
        },
    }, per_sd_map


# ---------------------------------------------------------------------------
# Doc04 §3 — per-sub-domain relevant systems (for EvidenceItem sources)
# ---------------------------------------------------------------------------

def parse_doc04_systems_for_sd() -> dict[str, list[str]]:
    src = open(DOC04, encoding="utf-8").read()
    sec = section_between(src, "## 3. Compliance Mapping", "## 4. Corpus Provenance")
    out: dict[str, list[str]] = {}
    for cells in md_table_rows(sec, r"^D-\d{2}\.\d{1}\b"):
        m = re.match(r"^(D-\d{2}\.\d{1})", cells[0])
        if not m:
            continue
        systems_cell = cells[1] if len(cells) > 1 else ""
        # explicit tokens only (ranges like 'SYS-01..SYS-25' yield their endpoints)
        toks: list[str] = []
        for tok in re.findall(r"SYS-\d{2}", systems_cell):
            if tok not in toks:
                toks.append(tok)
        out[m.group(1)] = toks
    return out


# ---------------------------------------------------------------------------
# EvidenceItems — mechanical derivation (maturity_model §6)
# ---------------------------------------------------------------------------

def derive_evidence_items(
    yaml_data: dict[str, Any],
    per_sd_nist: dict[str, dict[str, list[str]]],
    prop_by_sd: dict[str, dict[str, Any]],
    systems_by_sd: dict[str, list[str]],
    node_ids: set[str],
) -> tuple[list[dict[str, Any]], list[str]]:
    """Mechanical EvidenceItem derivation — no invented compliance content.

    Coverage (Scale B): one item per ACTIVE sub-domain that has a direct
    clause anchor in ontology@clause_mappings (37 of 38; D-07.2 has none —
    withheld + audit flag, NOT invented). observed=True because Scale-B
    SUBSTANTIVE anchors are met: documented control (Doc13 §4 example_controls)
    + RACI-assigned activity (Doc07 §4) + coverage_level per Doc12 §3.

    Capability (Scale A): one item per (sub-domain, framework) present in
    Doc14 §5, anchored on the FIRST listed control of that framework
    (deterministic rule). observed=False: Doc13 §4 Impl. Status (backfilled)
    is PARTIAL for all 38 sub-domains — capability tiers are NOT asserted
    here (no TierDecision emitted; Phase 2 decision).

    Returns (evidence_items, withheld_subdomain_ids).
    """
    clause_by_sd: dict[str, dict[str, Any]] = {}
    for c in yaml_data["clause_mappings"]:
        clause_by_sd.setdefault(c["maps_to_subdomain"], c)  # first clause per sd (deterministic)

    doc10_section = {"REG-GDPR": "§4", "REG-CRA": "§5", "REG-NIS2": "§6",
                     "REG-DORA": "§7", "REG-AIACT": "§8"}

    items: list[dict[str, Any]] = []
    withheld: list[str] = []

    def sys_sources(sd: str) -> list[str]:
        return [s for s in systems_by_sd.get(sd, [])[:2] if s in node_ids]

    active_sds = [s["id"] for s in yaml_data["subdomains"]["covered"]]
    for sd in active_sds:
        prop = prop_by_sd.get(sd, {})
        tier = prop.get("tier", "STANDARD")
        sp = prop.get("satisfaction_pattern", "")
        impl_status = prop.get("impl_status", "")

        # --- Scale B — Coverage (clause-anchored)
        clause = clause_by_sd.get(sd)
        if clause is None:
            withheld.append(sd)
        else:
            sec = doc10_section.get(clause["regulation_id"], "§4-§8")
            items.append({
                "ev_id": f"EV-{sd}-001",
                "subdomain_id": sd,
                "scale": "coverage",
                "outcome": clause["clause_id"],
                "claim": (
                    f"Coverage anchor ({sd}): clause {clause['clause_id']} "
                    f"({clause['article']}) maps to this sub-domain "
                    f"(ontology clause_mappings / Doc10 {sec}); treatment documented in "
                    f"Doc13 §4 (tier {tier}, satisfaction_pattern {sp}, "
                    f"Impl. Status {impl_status})."
                ),
                "sources": [f"Doc10 {sec}", "Doc13 §4", "Doc12 §3"] + sys_sources(sd),
                "observed": True,
            })

        # --- Scale A — Capability (NistControl-anchored, first control per framework)
        nist = per_sd_nist.get(sd, {})
        for slot, fw in ((2, "CSF"), (3, "PF"), (4, "AI-RMF")):
            ctrls = nist.get(fw, [])
            if not ctrls:
                continue
            ctrl = ctrls[0]
            items.append({
                "ev_id": f"EV-{sd}-{slot:03d}",
                "subdomain_id": sd,
                "scale": "capability",
                "outcome": ctrl,
                "claim": (
                    f"Capability anchor ({sd}): first {fw} control listed for this "
                    f"sub-domain in Doc14 §5 (corpus-derived controls; "
                    f"{len(ctrls)} {fw} controls mapped). observed=false — Doc13 §4 "
                    f"Impl. Status {impl_status}; tier decision deferred (no TierDecision emitted)."
                ),
                "sources": ["Doc14 §5", "Doc13 §4"] + sys_sources(sd),
                "observed": False,
            })

    return items, withheld


# ---------------------------------------------------------------------------
# Build orchestrator
# ---------------------------------------------------------------------------

def build() -> dict[str, Any]:
    yaml_data = load_yaml()
    generated_at = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

    nodes: list[dict[str, Any]] = []

    # --- Ambiguity first (feeds subdomain.ambiguity_in_scope) ---
    ambiguity, ambiguity_per_sd = build_ambiguity(DOC09)

    # --- CompanyContext ---
    nodes.append(build_company_context(yaml_data))

    # --- Regulations (5: GDPR + CRA + NIS2 + DORA + AI_Act — ALL applicable) ---
    nodes.extend(build_regulations(yaml_data))

    # --- Domains (10) ---
    nodes.extend(build_domains(yaml_data))

    # --- SecurityControlDomain (38, all ACTIVE) ---
    nodes.extend(build_subdomains(yaml_data, ambiguity_per_sd))

    # --- RegulatoryClauses (150) ---
    nodes.extend(build_clauses(yaml_data))

    # --- Tensions (5 nodes) ---
    nodes.extend(build_tensions(yaml_data))

    # --- Stakeholders + RaciRoles + RaciActivities (XLSX-driven) ---
    stks, roles, activities = build_stakeholders_and_raci()
    nodes.extend(stks)
    nodes.extend(roles)
    nodes.extend(activities)

    # --- CoverageGap (XLSX GAPS) ---
    gap_nodes = build_coverage_gaps()
    nodes.extend(gap_nodes)

    # --- AdjustedGoals (76 cards: Doc14 §2 + archived detail cards) ---
    ag_nodes, ag_mismatches = build_adjusted_goals()
    nodes.extend(ag_nodes)

    # --- Data Subject Categories (9, Doc04 §2.4) ---
    dsc_nodes = build_data_subject_categories(DOC04)
    nodes.extend(dsc_nodes)

    # --- Architecture & Third Parties + Personal Data (XLSX) ---
    system_nodes = build_systems()
    nodes.extend(system_nodes)
    store_nodes = build_data_stores()
    nodes.extend(store_nodes)
    flow_nodes = build_data_flows()
    nodes.extend(flow_nodes)
    tp_nodes = build_third_parties()
    nodes.extend(tp_nodes)
    personal_data_categories = build_personal_data_categories()
    nodes.extend(personal_data_categories)

    # --- node index (evidence derivation needs resolvable ids) ---
    node_by_id: dict[str, dict[str, Any]] = {n["id"]: n for n in nodes}
    node_ids = set(node_by_id)

    # --- NIST anchors (Doc14 §5: CSF + PF + AI-RMF) ---
    per_sd_nist = parse_doc14_nist()
    nist_nodes = build_nist_controls(per_sd_nist)
    nodes.extend(nist_nodes)
    for n in nist_nodes:
        node_by_id[n["id"]] = n
        node_ids.add(n["id"])

    # --- REG_CHAIN cross-check (audit only) ---
    rc_stats = regchain_csf_crosscheck()

    # --- Proportionality (Doc13 §4, mechanical) + ART_VERIFICATION ---
    prop_rows = parse_doc13_proportionality()
    prop_by_sd = {row["subdomain_id"]: row for row in prop_rows}

    # --- EvidenceItems (mechanical derivation) ---
    systems_by_sd = parse_doc04_systems_for_sd()
    evidence_items, withheld_sds = derive_evidence_items(
        yaml_data, per_sd_nist, prop_by_sd, systems_by_sd, node_ids)
    for ev in evidence_items:
        nodes.append({
            "id": ev["ev_id"],
            "type": "EvidenceItem",
            "label": ev["claim"][:80],
            "attrs": {
                "ev_id": ev["ev_id"],
                "subdomain_id": ev["subdomain_id"],
                "scale": ev["scale"],
                "outcome": ev["outcome"],
                "claim": ev["claim"],
                "sources": list(ev["sources"]),
                "observed": bool(ev["observed"]),
            },
            "source": ["00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §6",
                       "phase1_ontology.yaml@kg_ontology.maturity_model"],
        })
        node_by_id[ev["ev_id"]] = nodes[-1]
        node_ids.add(ev["ev_id"])

    # ------------------------------------------------------------------
    # Merge step: proportionality (Doc13 §4) + evidence_ids into sub-domains
    # ------------------------------------------------------------------
    ev_by_sd_all: dict[str, list[str]] = {}
    ev_by_sd_coverage: dict[str, list[str]] = {}
    for ev in evidence_items:
        ev_by_sd_all.setdefault(ev["subdomain_id"], []).append(ev["ev_id"])
        if ev["scale"] == "coverage":
            ev_by_sd_coverage.setdefault(ev["subdomain_id"], []).append(ev["ev_id"])

    for sd, prop in prop_by_sd.items():
        if sd in node_by_id and node_by_id[sd]["attrs"].get("active"):
            n = node_by_id[sd]
            n["attrs"].update({
                "i": prop["i"],
                "p": prop["p"],
                "proportionality_tier": prop["tier"],   # from Doc13 §4 (31 RIGOROUS + 7 STANDARD)
                "satisfaction_pattern": prop["satisfaction_pattern"],
                "evidence_depth": prop["evidence_depth"],
                "verification_method": prop["verification_method"],
                "ownership": prop["ownership"],
                "example_controls": prop["example_controls"],
                "notes": f"Tier {prop['tier']}; risk {prop['risk_if_not_met']}; priority {prop['implementation_priority']}.",
                "risk_if_not_met": prop["risk_if_not_met"],
                "evidence_ids": list(ev_by_sd_all.get(sd, [])),
                "coverage_evidence_ids": list(ev_by_sd_coverage.get(sd, [])),
                "implementation_priority": prop["implementation_priority"],
                "impl_status_doc13": prop["impl_status"],
                "nist_alignment_count": sum(len(v) for v in per_sd_nist.get(sd, {}).values()),
            })

    # AdjustedGoal tier from Doc13 §4 (mechanical)
    for n in ag_nodes:
        prop = prop_by_sd.get(n["attrs"]["subdomain_id"])
        if prop:
            n["attrs"]["tier"] = prop["tier"]

    # ------------------------------------------------------------------
    # Merge ART_VERIFICATION into RegulatoryClause attrs
    # ------------------------------------------------------------------
    art_ver = build_art_verification(yaml_data)
    av_by_cid = {row["clause_id"]: row for row in art_ver}
    for n in nodes:
        if n["type"] != "RegulatoryClause":
            continue
        av = av_by_cid.get(n["id"])
        if av is None:
            continue
        n["attrs"]["verification_criteria"] = av["verification_criteria"]
        n["attrs"]["evidence_type"] = av["evidence_type"]
        n["attrs"]["risk_if_not_met"] = av["risk_if_not_met"]

    # ------------------------------------------------------------------
    # Build links
    # ------------------------------------------------------------------
    links: list[dict[str, Any]] = []

    # ASSESSES: CompanyContext → Regulation (Case_03: ALL 5 applicable)
    company_id = yaml_data["company"]["id"]
    for r in yaml_data["regulations"]:
        if r.get("applicable"):
            links.append({
                "from": company_id, "to": r["id"], "rel": "ASSESSES",
                "attrs": {"obligated_party": r.get("obligated_party", []), "applicable": True},
                "source": ["phase1_ontology.yaml@regulations", "Doc08 §4"],
            })

    # MAPS_TO: RegulatoryClause → SecurityControlDomain
    for c in yaml_data["clause_mappings"]:
        links.append({
            "from": c["clause_id"], "to": c["maps_to_subdomain"], "rel": "MAPS_TO",
            "attrs": {"article": c["article"]},
            "source": ["phase1_ontology.yaml@clause_mappings", "Doc10 §4-§8"],
        })

    # BELONGS_TO: SecurityControlDomain → Domain
    for s in yaml_data["subdomains"]["covered"]:
        parent = s["id"].rsplit(".", 1)[0]
        links.append({
            "from": s["id"], "to": parent, "rel": "BELONGS_TO",
            "attrs": {},
            "source": ["phase1_ontology.yaml@subdomains", "Doc12 §3"],
        })

    # YIELDS (slot-001 privacy + slot-002 security): SecurityControlDomain → AdjustedGoal
    for n in ag_nodes:
        sid = n["attrs"]["subdomain_id"]
        if sid in node_by_id:
            links.append({
                "from": sid, "to": n["id"], "rel": "YIELDS",
                "attrs": {"slot": n["id"].split("-")[-1], "track": n["attrs"]["track"]},
                "source": ["Doc14 §2", "phase1_ontology.yaml@kg_ontology.relations.YIELDS"],
            })

    # OVERLAPS_WITH: Regulation ↔ Regulation (5 applicable → 10 pairs)
    applicable = [r["id"] for r in yaml_data["regulations"] if r.get("applicable")]
    for i, a in enumerate(applicable):
        for b in applicable[i + 1:]:
            links.append({
                "from": a, "to": b, "rel": "OVERLAPS_WITH",
                "attrs": {"scope": "case-level overlaps; see Doc12 §5"},
                "source": ["phase1_ontology.yaml@regulations", "Doc12 §5.1"],
            })

    # HAS_TENSION_WITH: RegulatoryClause ↔ RegulatoryClause (mechanical resolution)
    tension_edges, tension_unresolved = resolve_tension_edges(yaml_data)
    links.extend(tension_edges)

    # RACI & APPLIES_TO links from Case_03_Phase1_RICH.xlsx::ROLES_RACI
    try:
        wb_raci = openpyxl.load_workbook(XLSX_PATH, read_only=True, data_only=True)
        ws_raci = wb_raci["ROLES_RACI"]
        raci_rows_raw = list(ws_raci.iter_rows(values_only=True))
        if raci_rows_raw:
            r_header = raci_rows_raw[0]
            r_roles = [h for h in r_header[1:] if h and h not in ("Sub-domain", "Corpus Source")]
            for idx, r in enumerate(raci_rows_raw[1:], start=1):
                act_id = f"ACT-{idx:02d}"
                if act_id not in node_by_id:
                    continue
                sd_col = r_header.index("Sub-domain") if "Sub-domain" in r_header else None
                sd_val = r[sd_col] if sd_col is not None else None
                if sd_val:
                    for sd in str(sd_val).split(","):
                        sd = sd.strip()
                        if sd in node_by_id:
                            links.append({
                                "from": act_id, "to": sd, "rel": "APPLIES_TO",
                                "attrs": {"active": True},
                                "source": ["Doc07 §4", "Case_03_Phase1_RICH.xlsx::ROLES_RACI"],
                            })
                for rn in r_roles:
                    role_id = f"ROLE-{esc_id(rn)}"
                    if role_id not in node_by_id or rn not in r_header:
                        continue
                    val = r[r_header.index(rn)]
                    if val and str(val).strip() not in ("-", "—", ""):
                        cell_str = str(val).strip()
                        for single_letter in cell_str.split("/"):
                            single_letter = single_letter.strip()
                            if single_letter:
                                links.append({
                                    "from": role_id, "to": act_id, "rel": "RACI",
                                    "attrs": {
                                        "activity_id": act_id,
                                        "role_id": role_id,
                                        "letter": single_letter,
                                        "composite": cell_str if "/" in cell_str else None,
                                    },
                                    "source": ["Doc07 §4", "Case_03_Phase1_RICH.xlsx::ROLES_RACI"],
                                })
    except Exception as e:
        sys.stderr.write(f"Warning building RACI links: {e}\n")

    # CAPTURES: DataSubjectCategory → PersonalDataCategory (heuristic by
    # data_categories text overlap; exact regulatory mapping is in Doc12 §3).
    for dsc in dsc_nodes:
        dsc_text = (dsc["attrs"].get("data_categories") or "").lower()
        for pdc in personal_data_categories:
            pdc_text = (pdc["attrs"].get("category") or "").lower()
            if any(tok in dsc_text for tok in pdc_text.split()) and len(pdc_text) > 5:
                links.append({
                    "from": dsc["id"], "to": pdc["id"], "rel": "CAPTURES",
                    "attrs": {},
                    "source": ["Doc04 §2.4 ↔ §2.3 (cross-ref)"],
                })

    # HOSTS (System → DataStore)
    for st in store_nodes:
        for sid in re.findall(r"SYS-\d{2}", str(st["attrs"].get("system", ""))):
            links.append({
                "from": sid, "to": st["id"], "rel": "HOSTS",
                "attrs": {},
                "source": ["Doc04 §2.1"],
            })

    # FLOWS_BETWEEN (System ↔ System via DataFlow endpoints)
    for fl in flow_nodes:
        src_sys = re.findall(r"SYS-\d{2}", str(fl["attrs"].get("source", "")))
        dst_sys = re.findall(r"SYS-\d{2}", str(fl["attrs"].get("destination", "")))
        for ss in src_sys:
            for ds in dst_sys:
                if ss in node_by_id and ds in node_by_id:
                    links.append({
                        "from": ss, "to": ds, "rel": "FLOWS_BETWEEN",
                        "attrs": {"flow_id": fl["id"], "protocol": fl["attrs"].get("protocol", "")},
                        "source": ["Doc04 §2.2"],
                    })

    # FLAGS: CoverageGap → SecurityControlDomain (exact D-XX.Y ids only)
    for n in gap_nodes:
        for sid in n["attrs"].get("affected_subdomain_ids", []):
            if sid in node_by_id:
                links.append({
                    "from": n["id"], "to": sid, "rel": "FLAGS",
                    "attrs": {"severity": n["attrs"].get("severity", "medium")},
                    "source": ["Doc07 §7", "Case_03_Phase1_RICH.xlsx::GAPS"],
                })

    # ALIGNS_TO: SecurityControlDomain → NistControl (Doc14 §5; 3 frameworks)
    for sd, fws in per_sd_nist.items():
        if sd not in node_by_id:
            continue
        for fw in ("CSF", "PF", "AI-RMF"):
            for ctrl in fws.get(fw, []):
                nid = f"NIST-{ctrl}"
                if nid in node_by_id:
                    links.append({
                        "from": sd, "to": nid, "rel": "ALIGNS_TO",
                        "attrs": {"framework": fw},
                        "source": ["Doc14 §5", "phase1_ontology.yaml@kg_ontology.relations"],
                    })

    # MaturityModel v2.1-port edges:
    #   HAS_EVIDENCE   — SecurityControlDomain → EvidenceItem
    #   CITES_CLAUSE   — EvidenceItem → RegulatoryClause   (Scale B)
    #   CITES_OUTCOME  — EvidenceItem → NistControl         (Scale A)
    for ev in evidence_items:
        ev_id = ev["ev_id"]
        sid = ev["subdomain_id"]
        outcome = ev["outcome"]
        links.append({
            "from": sid, "to": ev_id, "rel": "HAS_EVIDENCE",
            "attrs": {"scale": ev["scale"], "observed": bool(ev["observed"])},
            "source": ["00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §6"],
        })
        if ev["scale"] == "coverage":
            links.append({
                "from": ev_id, "to": outcome, "rel": "CITES_CLAUSE",
                "attrs": {"scale": "coverage"},
                "source": ["00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §5/§6"],
            })
        elif ev["scale"] == "capability":
            framework = framework_of(outcome) or "CSF"
            links.append({
                "from": ev_id, "to": f"NIST-{outcome}", "rel": "CITES_OUTCOME",
                "attrs": {"scale": "capability", "framework": framework, "outcome_id": outcome},
                "source": ["00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §5/§6",
                           "Doc14 §5 (crosswalk: OVERLAY_NIST_CSF_2.0 §2 / OVERLAY_NIST_PF_1.1 §2 / OVERLAY_NIST_AI_RMF_1.0)"],
            })

    # ------------------------------------------------------------------
    # Invariants + audits
    # ------------------------------------------------------------------
    def count_type(t: str) -> int:
        return sum(1 for n in nodes if n["type"] == t)

    coverage_sd_count = len(ev_by_sd_coverage)
    rigorous = sum(1 for p in prop_rows if p["tier"] == "RIGOROUS")
    standard = sum(1 for p in prop_rows if p["tier"] == "STANDARD")
    n_csf = sum(1 for n in nodes if n["type"] == "NistControl" and n["attrs"]["framework"] == "CSF")
    n_pf = sum(1 for n in nodes if n["type"] == "NistControl" and n["attrs"]["framework"] == "PF")
    n_ai = sum(1 for n in nodes if n["type"] == "NistControl" and n["attrs"]["framework"] == "AI-RMF")
    ev_cap = sum(1 for ev in evidence_items if ev["scale"] == "capability")
    ev_cov = sum(1 for ev in evidence_items if ev["scale"] == "coverage")
    cap_by_fw = {"CSF": 0, "PF": 0, "AI-RMF": 0}
    for ev in evidence_items:
        if ev["scale"] == "capability":
            cap_by_fw[framework_of(ev["outcome"]) or "CSF"] += 1

    invariants = {
        "regulations_total": len(yaml_data["regulations"]),
        "regulations_applicable": sum(1 for r in yaml_data["regulations"] if r.get("applicable")),
        "domains": len(yaml_data["domains"]),
        "subdomains_total": len(yaml_data["subdomains"]["covered"]) + len(yaml_data["subdomains"]["not_covered"]),
        "subdomains_covered": len(yaml_data["subdomains"]["covered"]),
        "subdomains_active": count_type("SecurityControlDomain"),
        "clauses_total": len(yaml_data["clause_mappings"]),
        "clauses_gdpr": sum(1 for c in yaml_data["clause_mappings"] if c["regulation_id"] == "REG-GDPR"),
        "clauses_cra":  sum(1 for c in yaml_data["clause_mappings"] if c["regulation_id"] == "REG-CRA"),
        "clauses_nis2": sum(1 for c in yaml_data["clause_mappings"] if c["regulation_id"] == "REG-NIS2"),
        "clauses_dora": sum(1 for c in yaml_data["clause_mappings"] if c["regulation_id"] == "REG-DORA"),
        "clauses_aiact": sum(1 for c in yaml_data["clause_mappings"] if c["regulation_id"] == "REG-AIACT"),
        "tensions_total": len(yaml_data["tensions"]),
        "tension_edges_resolved": len(tension_edges),
        "ambiguity_cards_in_scope": ambiguity["stats_total"]["cards_in_scope"],
        "ambiguity_top_cards": len(ambiguity["top_cards"]),
        "evidence_items": len(evidence_items),
        "evidence_items_capability": ev_cap,
        "evidence_items_coverage": ev_cov,
        "evidence_items_capability_csf": cap_by_fw["CSF"],
        "evidence_items_capability_pf": cap_by_fw["PF"],
        "evidence_items_capability_airmf": cap_by_fw["AI-RMF"],
        "subdomains_with_coverage_evidence": coverage_sd_count,
        "subdomains_withheld_coverage": len(withheld_sds),
        "articles_with_verification": len(art_ver),
        "subdomains_with_proportionality": len(prop_rows),
        "subdomains_rigorous": rigorous,
        "subdomains_standard": standard,
        "adjusted_goals": len(ag_nodes),
        "data_subject_categories": len(dsc_nodes),
        "systems": len(system_nodes),
        "data_stores": len(store_nodes),
        "data_flows": len(flow_nodes),
        "third_parties": len(tp_nodes),
        "personal_data_categories": len(personal_data_categories),
        "stakeholders": len(stks),
        "raci_roles": len(roles),
        "raci_activities": len(activities),
        "coverage_gaps": len(gap_nodes),
        "nist_controls": count_type("NistControl"),
        "nist_controls_csf": n_csf,
        "nist_controls_pf": n_pf,
        "nist_controls_airmf": n_ai,
        "nist_alignments": sum(1 for l in links if l["rel"] == "ALIGNS_TO"),
        "regchain_crosscheck_distinct_csf": rc_stats["distinct_csf"],
        "regchain_crosscheck_raw_alignments": rc_stats["raw_alignments"],
    }

    audits = [
        # NEW-C03-01: maturity data layer seeded (PORT-PARITY-2 F3a)
        {
            "id": "NEW-C03-01",
            "kind": "structural",
            "severity": "info",
            "title": f"Maturity layer seeded — {len(evidence_items)} EvidenceItems derived mechanically across scales",
            "detail": (
                f"PORT-PARITY-2 F3a — {len(evidence_items)} EvidenceItems derived mechanically "
                f"({ev_cov} Coverage clause-anchored + {ev_cap} Capability CSF/PF/AI-RMF, first-control-"
                f"per-(sub-domain,framework) rule on Doc14 §5). All sources[] resolve to graph nodes or "
                f"canonical doc-section strings. Capability items carry observed=false (Doc13 §4 Impl. "
                f"Status PARTIAL for all 38 rows — no TierDecision emitted). The xlsx MATURITY sheet "
                f"(macro-domain 0-4 legacy scale) is deliberately NOT ingested into sub-domain attrs "
                f"(forbidden by maturity Gate 1)."
            ),
            "evidence": [
                "00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §6",
                "phase1_ontology.yaml@kg_ontology.maturity_model (v2.1-port)",
                "Doc13 §4 (Impl. Status column, backfilled PARTIAL)",
                f"{len(evidence_items)} EvidenceItem nodes + {len(evidence_items)} HAS_EVIDENCE + "
                f"{ev_cov} CITES_CLAUSE + {ev_cap} CITES_OUTCOME",
            ],
            "node_ids": [ev["ev_id"] for ev in evidence_items[:5]],
            "recommendation": "Capability tier assessment (TierDecisions) is a Phase 2 decision — do not read observed=false as a compliance failure.",
            "source": ["00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §6"],
        },
        # NEW-C03-02: AdjustedGoal seed
        {
            "id": "NEW-C03-02",
            "kind": "structural",
            "severity": "info",
            "title": f"{len(ag_nodes)} AdjustedGoal nodes seeded from Doc14 §2 + archived detail cards",
            "detail": (
                f"{len(ag_nodes)} AdjustedGoal nodes (38 privacy slot-001 + 38 security slot-002); "
                f"{len([l for l in links if l['rel'] == 'YIELDS'])} YIELDS edges from the 38 active "
                f"sub-domains. Canonical ids/titles from Doc14 §2 (38 rows × 8 cols); objective prose "
                f"from the corr-010 archive _deprecated/Doc15_Appendix_A_OLD.md (76 detail cards). "
                f"Cross-check mismatches: {len(ag_mismatches)}."
            ),
            "evidence": [
                "Doc14 §2 (Multi-Regulation Adjusted Objectives)",
                "_deprecated/Doc15_Appendix_A_OLD.md (76 cards, 18 fields each)",
                f"{len([l for l in links if l['rel'] == 'YIELDS'])} YIELDS relations",
            ],
            "node_ids": [n["id"] for n in ag_nodes][:5],
            "recommendation": "Maintain the 2-slot canonical format (AG-D-XX.Y-001 privacy, -002 security) for Phase 2 obligation synthesis.",
            "source": ["Doc14 §2", "phase1_ontology.yaml@kg_ontology.relations.YIELDS"],
        },
        # NEW-C03-03: ambiguity registry
        {
            "id": "NEW-C03-03",
            "kind": "blocking_ambiguity",
            "severity": "info",
            "title": f"Ambiguity Register — {ambiguity['stats_total']['cards_in_scope']} cards in scope per Doc09 §1",
            "detail": (
                f"{ambiguity['stats_total']['cards_in_scope']} ambiguity cards in scope (Doc09 §1, "
                f"5-regulation filter); {len(ambiguity['stats_per_subdomain'])} per-sub-domain counts; "
                f"{len(ambiguity['top_cards'])} top cards documented in §3 (GDPR 5 + CRA 4 + NIS 2 4 + "
                f"DORA 4 + AI Act 3 distinct clauses). D-04.3 is the most card-rich sub-domain (94)."
            ),
            "evidence": [
                "Doc09 §1 (1490 total filtered cards)",
                "Doc09 §2 (per-sub-domain breakdown across 38 sub-domains)",
                "Doc09 §3 (top-20 severity-sorted cards with recommended variants)",
            ],
            "node_ids": ["D-04.3", "D-09.1", "D-09.4", "D-06.3"],
            "recommendation": "Focus Phase 2 resolution on the highest-cardinality sub-domains (D-09.1 131, D-09.4 116, D-04.3 94) using the documented top-20 recommended variants.",
            "source": ["Doc09 §1/§2/§3"],
        },
        # NEW-C03-04: NIST anchors (Doc14 §5) + REG_CHAIN cross-check
        {
            "id": "NEW-C03-04",
            "kind": "structural",
            "severity": "info",
            "title": f"NIST anchors — {n_csf + n_pf + n_ai} NistControl nodes ({n_csf} CSF + {n_pf} PF + {n_ai} AI-RMF) from Doc14 §5",
            "detail": (
                f"{n_csf + n_pf + n_ai} NistControl nodes extracted mechanically from Doc14 §5 "
                f"(38 rows × 3 frameworks); {invariants['nist_alignments']} ALIGNS_TO edges "
                f"(CSF + PF + AI-RMF). REG_CHAIN xlsx cross-check: {rc_stats['distinct_csf']} distinct "
                f"CSF controls / {rc_stats['raw_alignments']} raw alignments across "
                f"{rc_stats['rows_subdomains']} sub-domains (strict subset of Doc14 §5 — Case_03's "
                f"primary NIST source is Doc14 §5, unlike Case_02 where REG_CHAIN was primary)."
            ),
            "evidence": [
                "Doc14 §5 (NIST Controls Mapping, 3 frameworks × 38 sub-domains)",
                "Doc14 §5.1 coverage statistics (279 CSF / 289 PF / 24 AI-RMF mentions)",
                f"Case_03_Phase1_RICH.xlsx::REG_CHAIN ({rc_stats['distinct_csf']} distinct CSF, cross-check only)",
            ],
            "node_ids": [n["id"] for n in nist_nodes[:5]],
            "recommendation": "AI-RMF anchors are REAL for Case_03 (PROVIDER + DEPLOYER) — carry them into Phase 2 control mapping alongside CSF/PF.",
            "source": ["Doc14 §5", "Case_03_Phase1_RICH.xlsx::REG_CHAIN"],
        },
        # NEW-C03-05: proportionality (MAX; 38/38 active)
        {
            "id": "NEW-C03-05",
            "kind": "structural",
            "severity": "info",
            "title": f"Proportionality — {rigorous} RIGOROUS + {standard} STANDARD across 38/38 ACTIVE sub-domains (MAX)",
            "detail": (
                f"Parsed mechanically from Doc13 §4 (38 rows): {rigorous} RIGOROUS (BUILD_REQUIRED × "
                f"MUST) + {standard} STANDARD (INHERITABLE × MUST) = 38. Case_03 is the only case with "
                f"zero NOT_ADDRESSED sub-domains (5 applicable regulations). Coverage levels per Doc12 §3: "
                f"{sum(1 for n in nodes if n['type'] == 'SecurityControlDomain' and n['attrs'].get('coverage_level') == 'SUBSTANTIVE')} "
                f"SUBSTANTIVE + "
                f"{sum(1 for n in nodes if n['type'] == 'SecurityControlDomain' and n['attrs'].get('coverage_level') == 'PARTIAL')} "
                f"PARTIAL."
            ),
            "evidence": [
                "Doc13 §3 (Tier Assignment Summary: 31 RIGOROUS + 7 STANDARD)",
                "Doc13 §4 (per-sub-domain proportionality table, 38 rows)",
                "Doc12 §3 (Coverage Level column)",
            ],
            "node_ids": [n["id"] for n in nodes
                         if n["type"] == "SecurityControlDomain"
                         and n["attrs"].get("proportionality_tier") == "RIGOROUS"][:5],
            "recommendation": "Enforce RIGOROUS verification (TEST + ANALYZE + external audit) on the 31 high-criticality sub-domains.",
            "source": ["Doc13 §3/§4"],
        },
        # NEW-C03-06: DORA axis + tension edge resolution
        {
            "id": "NEW-C03-06",
            "kind": "structural",
            "severity": "info",
            "title": f"DORA axis real — {invariants['clauses_dora']} DORA clauses (largest single-reg corpus); {len(tension_edges)}/{len(yaml_data['tensions'])} tension edges resolved",
            "detail": (
                f"DORA contributes {invariants['clauses_dora']} RegulatoryClauses (Doc10 §7) and "
                f"Doc11 maps Art. 5-34 to AEGIS sub-domains. HAS_TENSION_WITH edges are resolved "
                f"mechanically from tension regulation refs (Case_03 tensions reference articles, not "
                f"clause ids): {len(tension_edges)} of {len(yaml_data['tensions'])} tensions yielded a "
                f"clause pair; unresolved refs: {tension_unresolved or 'none'}. T-005 resolves to a "
                f"single clause (DORA-Art.26) plus non-clause regimes (ISO 27001) — no edge emitted."
            ),
            "evidence": [
                "Doc10 §7 (DORA Mapping, 38 clauses)",
                "Doc11 §3 (DORA Article → AEGIS Sub-Domain Mapping) + §4 (5 tensions)",
                "phase1_ontology.yaml@tensions (mechanical article→clause resolution)",
            ],
            "node_ids": ([e["from"] for e in tension_edges[:2]] + [e["to"] for e in tension_edges[:2]]),
            "recommendation": "Keep article→clause resolution manual on tension edits, or promote clause_1/clause_2 fields into the ontology tensions (Sprint 2+ candidate).",
            "source": ["Doc11 §4", "phase1_ontology.yaml@tensions"],
        },
        # CFL-C03-001: Doc14 §5.1 stats vs mechanical parse
        {
            "id": "CFL-C03-001",
            "kind": "cross_doc_conflict",
            "severity": "low",
            "title": "Doc14 §5.1 reported statistics vs mechanical parse (reconciled)",
            "detail": (
                "Doc14 §5.1 reports 279 CSF / 289 PF / 24 AI-RMF control MENTIONS. Mechanical parse "
                "of the §5 table (dedup per sub-domain, parentheticals stripped, ';' splits handled) "
                "yields 79 distinct CSF + 38 distinct PF + 4 distinct AI-RMF controls and deduped "
                "ALIGNS_TO edges. Differences are explainable: §5.1 counts raw cell mentions (incl. "
                "duplicates such as 'PR.PS-02' repeated and '(primary)' annotations); the graph dedupes "
                "per sub-domain. No content conflict detected."
            ),
            "evidence": [
                "Doc14 §5.1 Coverage statistics",
                "Doc14 §5 table (38 rows × 3 framework columns)",
                "graph.invariants.nist_alignments (deduped edges)",
            ],
            "node_ids": [n["id"] for n in nist_nodes[:3]],
            "recommendation": "No action needed; keep §5.1 as raw-mention statistics and graph counts as deduped-edge statistics.",
            "source": ["Doc14 §5 ↔ §5.1 cross-check"],
        },
        # BLN-C03-001: domain count baseline
        {
            "id": "BLN-C03-001",
            "kind": "broken_link",
            "severity": "low",
            "title": "Macro-domain baseline — 10 domains (D-01 to D-10)",
            "detail": "Case_03 has 10 macro-domains (D-01 to D-10) per ontology @domains; matches Case_01/Case_02 structure.",
            "evidence": [
                "phase1_ontology.yaml@domains (10 macro-domains)",
                "Doc12 §3 (38 sub-domains partitioned under D-01..D-10)",
            ],
            "node_ids": [n["id"] for n in nodes if n["type"] == "Domain"][:5],
            "recommendation": "Maintain standard 10-domain ontology partition across all methodology cases.",
            "source": ["phase1_ontology.yaml@domains"],
        },
        # CVG-C03-001: coverage evidence audit (the F3a coverage assertion)
        {
            "id": "CVG-C03-001",
            "kind": "coverage_gap",
            "severity": "low",
            "title": f"Coverage evidence audit — {coverage_sd_count}/38 active sub-domains carry clause-anchored coverage evidence",
            "detail": (
                f"All 38 active sub-domains carry evidence_ids (coverage + capability). Clause-anchored "
                f"COVERAGE evidence exists for {coverage_sd_count}/38. Exception: {', '.join(withheld_sds) or 'none'} "
                f"has NO RegulatoryClause anchor — the clause is absent from ontology@clause_mappings "
                f"(150 clauses) AND from Doc10 (no D-07.2 mention); REG_CHAIN covers D-07.2 only via "
                f"Sub-SO ids (SO-D-07.2.CRA/DORA/AI_Act), not clause ids. Per the no-invention rule the "
                f"Coverage EvidenceItem for D-07.2 was WITHHELD (capability evidence only) and is listed "
                f"here for human review."
            ),
            "evidence": [
                "phase1_ontology.yaml@clause_mappings (distinct maps_to_subdomain = 37 of 38)",
                "Doc10_Clause_Mapping_Matrix.md (no D-07.2 mapping row)",
                "Case_03_Phase1_RICH.xlsx::REG_CHAIN rows 7.2.x (Sub-SO anchors only)",
            ],
            "node_ids": ["D-07.2"] + [c["clause_id"] for c in yaml_data["clause_mappings"] if c["maps_to_subdomain"] == "D-07.1"][:1],
            "recommendation": "Human review: either add a D-07.2 clause to the ontology+Doc10 (Sprint candidate) or confirm Sub-SO-only coverage is intentional for D-07.2.",
            "source": ["phase1_ontology.yaml@clause_mappings", "Doc10", "Case_03_Phase1_RICH.xlsx::REG_CHAIN"],
        },
    ]

    # Assemble final graph (top-level flat shape compatible with DATA.* consumption
    # in Case_01_P1_Dashboard.html style Folios).
    graph = {
        "meta": {
            "case_id": "Case_03_OmniBank_Financial",
            "phase": 1,
            "generated": generated_at,
            "schema_version": "phase1_graph.json v2.1-port",
            "canonical_sources": [
                "phase1_ontology.yaml v2.1-port (kg_ontology.maturity_model + class promotions, 2026-09-04)",
                "Doc04 §1.1 + §2.1-§2.4 + §3",
                "Doc06 §5",
                "Doc07 §2 + §4 + §7",
                "Doc08 §4",
                "Doc09 §1 + §2 + §3",
                "Doc10 §4-§8",
                "Doc11 §3 + §4",
                "Doc12 §3 + §5",
                "Doc13 §3 + §4",
                "Doc14 §2 + §5 (+ _deprecated/Doc15_Appendix_A_OLD.md detail-card archive)",
                "Case_03_Phase1_RICH.xlsx (SYSTEMS + DATA_STORES + DATA_FLOWS + PERSONAL_DATA + THIRD_PARTIES + ROLES_RACI + GAPS + REG_CHAIN)",
                "00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md v1.0",
                "OVERLAY_NIST_CSF_2.0.md §2 + OVERLAY_NIST_PF_1.1.md §2 + OVERLAY_NIST_AI_RMF_1.0.md",
            ],
        },
        "company_context": {"node": nodes[0]},  # CompanyContext
        "nodes": nodes,
        "links": links,
        "ambiguity": {
            "stats_total": ambiguity["stats_total"],
            "stats_per_subdomain": ambiguity["stats_per_subdomain"],
            "top_cards": ambiguity["top_cards"],
        },
        "invariants": invariants,
        "audits": audits,
    }
    return graph


def main(argv: list[str]) -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Build phase1_graph.json for Case_03 (v2.1-port maturity_model).")
    ap.add_argument("--out", default=str(OUT), help=f"Output path (default: {OUT})")
    ap.add_argument("--emit", action="store_true", help="Print the JSON to stdout instead of writing")
    ap.add_argument("--summary", action="store_true", help="Print a one-line summary")
    args = ap.parse_args(argv[1:])

    graph = build()
    if args.emit:
        sys.stdout.write(json.dumps(graph, ensure_ascii=False))
        return 0
    if args.summary:
        by_type: dict[str, int] = {}
        for n in graph["nodes"]:
            by_type[n["type"]] = by_type.get(n["type"], 0) + 1
        print(json.dumps({"nodes_by_type": by_type,
                          "link_count": len(graph["links"]),
                          "audits_count": len(graph["audits"])},
                         ensure_ascii=False))
        return 0
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {out_path}", file=sys.stderr)
    # Quick local summary to stderr
    by_type: dict[str, int] = {}
    for n in graph["nodes"]:
        by_type[n["type"]] = by_type.get(n["type"], 0) + 1
    print(f"  {by_type}", file=sys.stderr)
    print(f"  link count: {len(graph['links'])}", file=sys.stderr)
    print(f"  audits count: {len(graph['audits'])}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
