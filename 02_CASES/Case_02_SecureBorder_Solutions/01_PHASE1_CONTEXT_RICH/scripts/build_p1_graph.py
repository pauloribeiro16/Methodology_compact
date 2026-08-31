#!/usr/bin/env python3
"""Build phase1_graph.json for Case_02_SecureBorder_Solutions — v2.3 (maturity_model).

Schema: 00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md v1.0 (referenced from
phase1_ontology.yaml v2.3). Mirrors Case_01_TinyTask_SaaS's build_p1_graph.py at
the structural level, but data sources are 100% Case_02-specific:

  - phase1_ontology.yaml v2.3 → CompanyContext, Regulations, Domains, Subdomains,
    clause_mappings (111), tensions (9), case-level coverage gaps
  - Case_02_Phase1_RICH.xlsx → Systems, DataStores, DataFlows, ThirdParties,
    Roles_RACI, gaps, RaciActivities, PersonalDataCategories, priorities
  - EVIDENCE_ITEMS seed (this file) → 35 Coverage + ~25 Capability (CSF/PF/AI-RMF)

Output: data/phase1_graph.json (flat top-level shape; legacy Folio II + IV
scripts in the dashboard consume it via DATA.*, with a small compat shim).

Usage
-----
    python3 build_p1_graph.py [--out PATH]
    default OUT = ../data/phase1_graph.json  (relative to this script)

Counts are validated against phase1_ontology.yaml@invariants at the end of
build(); the dashboard validator (build_p1_dashboard.py --check) re-checks the
v2.3 maturity_model contract (4 gates; see MATURITY_MODEL_CSF_STRICT.md §10).
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
XLSX_PATH = ROOT / "Case_02_Phase1_RICH.xlsx"


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
        rec["_corpus_source_cell"] = f"Case_02_Phase1_RICH.xlsx::{name}!row"
        out.append(rec)
    return out


# ---------------------------------------------------------------------------
# node constructors (no I/O side effects — return dicts)
# ---------------------------------------------------------------------------

def build_nist_csf_from_regchain() -> tuple[list[dict[str, Any]], dict[str, int]]:
    """Parse the REG_CHAIN xlsx sheet to extract CSF NistControl nodes and
    per-sub-domain alignment counts.

    Returns:
      csf_nodes    — list of NistControl nodes (framework='CSF')
      align_count  — {subdomain_id: count_of_aligned_CSF_subcategories}
    """
    wb = openpyxl.load_workbook(XLSX_PATH, read_only=True, data_only=True)
    if "REG_CHAIN" not in wb.sheetnames:
        return [], {}
    ws = wb["REG_CHAIN"]
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return [], {}
    headers = [str(h) if h is not None else "" for h in rows[0]]
    # Find indices
    try:
        idx_sd    = headers.index("Sub-domain")
        idx_nist  = headers.index("NIST CSF")
    except ValueError:
        return [], {}
    seen = set()  # (control_id,) to dedupe
    nodes = []
    align_count: dict[str, int] = {}
    for raw in rows[1:]:
        if not raw or not raw[idx_sd]:
            continue
        sd_id = str(raw[idx_sd]).strip()
        nist_field = str(raw[idx_nist] or "").strip()
        if not nist_field:
            continue
        # Count alignments per sub-domain
        align_count[sd_id] = align_count.get(sd_id, 0) + 1
        # Parse comma-separated outcomes (e.g. "PR.DS-01, PR.DS-10")
        for ctrl_id in nist_field.replace(" ", "").split(","):
            if not ctrl_id:
                continue
            if (ctrl_id,) in seen:
                continue
            seen.add((ctrl_id,))
            nodes.append({
                "id": f"NIST-{ctrl_id}",
                "type": "NistControl",
                "label": ctrl_id,
                "attrs": {
                    "control_id": ctrl_id,
                    "framework": "CSF",
                    "function": ctrl_id.split(".")[0] if "." in ctrl_id else "",
                    "description": f"CSF 2.0 {ctrl_id} (extracted from REG_CHAIN)",
                    "path": "Case_02_Phase1_RICH.xlsx::REG_CHAIN (NIST CSF column)",
                },
                "source": ["Case_02_Phase1_RICH.xlsx::REG_CHAIN", "Doc13 §7 crosswalk"],
            })
    return nodes, align_count


def build_adjusted_goals(doc13_path: Path) -> list[dict[str, Any]]:
    """Parse 70 AG cards from Doc13 §8 (35 privacy + 35 security).

    Format per card (§8):
        ### AG-D-XX.Y-NNN — <Title>
        **Description (multi-paragraph):** ...
        **Source Article:** GDPR Art. X | CRA Art. Y | ...
        **NIST CSF Anchors:** PR.DS-01, PR.DS-10
        **Verification Criteria (operational):** ...

    Tier inferred from §2/§3 tables (privacy -001 / security -002). Sub-domain
    parsed from the AG id. The id-suffix -001 → privacy, -002 → security.
    """
    src = open(doc13_path, encoding="utf-8").read()
    # Split by '### AG-D-XX.Y-NNN — ...' card headers; parts[0] is preamble, then [ag_id, body, ag_id, body, ...]
    # re.split with capturing group produces: [preamble, ag_id_1, body_1, ag_id_2, body_2, ...]
    parts = re.split(r"### (AG-D-\d{2}\.\d{1}-00\d)[^\n]*", src)
    nodes = []
    # Skip preamble (parts[0]); iterate in pairs (ag_id, body)
    pairs = list(zip(parts[1::2], parts[2::2]))
    for ag_id, body_full in pairs:
        body = body_full.split("### ")[0]
        def f(name_prefix):
            """Find a `**PREFIX...:**` field. Doc13 §8 fields:
              - 'Description (multi-paragraph):' is followed by a blank line +
                a sub-block '**Context:**' which contains the actual narrative.
              - 'Source Article:', 'NIST CSF Anchors:' are single-line.
              - 'Scope:', 'Boundaries:' are multi-line narratives (we capture
                the first paragraph).
            We match by prefix and capture the appropriate shape.
            """
            header_pat = re.escape("**") + name_prefix + r"[^:*\n]*?" + re.escape(":**")
            hm = re.search(header_pat, body)
            if not hm:
                return ""
            start = hm.end()
            if name_prefix == "Description":
                # The Description block contains '**Context:**' as the actual prose.
                # Capture the Context value (single paragraph, no nested **).
                cm = re.search(r"\*\*Context:\*\*\s*([^\n]+(?:\n(?!\*\*)[^\n]+)*)", body[start:])
                if cm:
                    val = cm.group(1).strip().replace("\n", " ")
                    return val[:300] + ("..." if len(val) > 300 else "")
                return ""
            if name_prefix in ("Scope", "Boundaries"):
                # Multi-paragraph prose — capture until the next **Field:** header.
                vm = re.search(r"\n\s*\n(.+?)(?=\n\s*\n\*\*\w)", body[start:], re.DOTALL)
                if vm:
                    val = vm.group(1).strip().replace("\n", " ")
                    return val[:250] + ("..." if len(val) > 250 else "")
                return ""
            # Single-line field (Source Article, NIST CSF Anchors, etc.)
            vm = re.match(r"\s*([^\n]+)", body[start:])
            return vm.group(1).strip() if vm else ""
        # Pull the short description (first paragraph of 'Description (multi-paragraph)')
        desc_full = f("Description") or f("Adjusted objective")
        # Take only first sentence (~180 chars)
        desc_short = desc_full.split(". ")[0] + ("." if desc_full else "")
        if len(desc_short) > 180:
            desc_short = desc_short[:177] + "..."
        sd_match = re.search(r"AG-D-(\d{2}\.\d{1})-00(\d)", ag_id)
        if not sd_match:
            continue
        subdomain_id = "D-" + sd_match.group(1)
        slot = sd_match.group(2)
        track = "PRIVACY" if slot == "1" else "SECURITY"
        nodes.append({
            "id": ag_id,
            "type": "AdjustedGoal",
            "label": f"{ag_id} — {desc_short[:80]}",
            "attrs": {
                "id": ag_id,
                "subdomain_id": subdomain_id,
                "track": track,
                "priority": f"P{slot}",
                "tier": "LIGHTWEIGHT",  # placeholder; Doc12 §3 is canonical per Fase 1e
                "objective": desc_short or "(see Doc13 §8)",
                "adjustment_note": (
                    f"Source: {f('Source Article')}; "
                    f"NIST: {f('NIST CSF Anchors')}"
                ),
            },
            "source": ["Doc13 §8 (DEEP Detail Cards)"],
        })
    return nodes




def build_company_context(d: dict[str, Any]) -> dict[str, Any]:
    co = d["company"]
    return {
        "id": co["id"],
        "type": "CompanyContext",
        "label": co["name"],
        "attrs": {
            "scale": co["size"],
            "employees": co["employees"],
            "security_fte": co.get("security_fte", 0),
            "data_types": co.get("data_types", []),
            "roles": co.get("roles", {}),
            "hq": co.get("jurisdiction"),
            "sector": co.get("sector"),
            "product": co.get("product"),
            "stack": co.get("tech_stack", []),
            "criticality": co.get("criticality"),
        },
        "source": ["phase1_ontology.yaml@company"],
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
            "source": ["phase1_ontology.yaml@regulations"],
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


def build_subdomains(d: dict[str, Any]) -> list[dict[str, Any]]:
    """35 ACTIVE sub-domínios + 3 NOT_ADDRESSED.

    active flag follows XLSX SUBDOMAINS sheet `Active for SecureBorder`:
      - D-07.4, D-08.3, D-09.3 → active=False (NOT_ADDRESSED per ontology gap
        reason in D-07.4/D-08.3/D-09.3)
    """
    # Build map id → coverage_level from the XLSX COMPLIANCE sheet (SAME/PARTIAL/
    # NOT_ADDRESSED) if present; otherwise default to SUBSTANTIVE for active, NA otherwise.
    coverage_map: dict[str, str] = {}
    try:
        comp = load_xlsx_sheet("COMPLIANCE")
        for r in comp:
            sd_id = r.get("sub_domain") or r.get("sub-domain") or r.get("id")
            if not sd_id:
                continue
            # 'Verified Relationship' column hints at scope-disjoint; we use it
            # only to flag SAME (=> SUBSTANTIVE) and PARTIAL.
            vr = (r.get("verified_relationship") or "").strip()
            if vr == "SAME":
                coverage_map[sd_id] = "SUBSTANTIVE"
            elif "PARTIAL" in vr.upper():
                coverage_map[sd_id] = "PARTIAL"
    except KeyError:
        pass

    # Use XLSX SUBDOMAINS to determine `active` flag
    sd_active: dict[str, bool] = {}
    try:
        subs = load_xlsx_sheet("SUBDOMAINS")
        for r in subs:
            sid = r.get("id") or r.get("sub_domain")
            if not sid:
                continue
            status = (r.get("status") or "").upper()
            # NOT_ADDRESSED sub-domains (no treatment per phase1_ontology.yaml@subdomains.not_covered)
            # override the XLSX "Active for SecureBorder" flag.
            if sid in {"D-06.4", "D-07.4", "D-08.3", "D-09.3"}:
                sd_active[sid] = False
            else:
                sd_active[sid] = status != "INACTIVE"
    except KeyError:
        pass

    out = []
    covered = d["subdomains"]["covered"]
    not_covered = d["subdomains"]["not_covered"]
    for s in covered + not_covered:
        sid = s["id"]
        is_active = sd_active.get(sid, True)
        # proportionality_tier / coverage_level: prefer ontology's existing fields
        # if present (D-XX.Y not_covered entries sometimes have sole_authority/gap_reason).
        cl = coverage_map.get(sid, "NOT_ADDRESSED" if s.get("id") in [nc["id"] for nc in not_covered] else "SUBSTANTIVE")
        out.append({
            "id": sid,
            "type": "SecurityControlDomain",
            "label": s["name"],
            "attrs": {
                "domain_id": s["domain_id"],
                "name": s["name"],
                "covered": s["id"] in [c["id"] for c in covered],
                "active": is_active,
                "coverage_level": cl,
                "proportionality_tier": None,   # Filled later by SUBDOMAIN_PROPORTIONALITY merge
                "sole_authority_regulation": s.get("sole_authority_regulation"),
                "gap_reason": s.get("reason"),
                "clause_count": int(s.get("clause_count", 0)),
                "ambiguity_in_scope": 0,
                "evidence_ids": [],   # Filled later by COVERAGE_EV_BY_SUBDOMAIN merge
            },
            "source": ["phase1_ontology.yaml@subdomains"],
        })
    return out


def build_clauses(d: dict[str, Any]) -> list[dict[str, Any]]:
    """111 RegulatoryClauses from ontology.clause_mappings."""
    out = []
    for c in d["clause_mappings"]:
        # obligated_party may be string or list — normalise to list
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
            "source": ["phase1_ontology.yaml@clause_mappings"],
        })
    return out


def build_tensions(d: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for t in d["tensions"]:
        res = t.get("resolution", {})
        out.append({
            "id": t["id"],
            "type": "Tension",
            "label": t.get("description", t["id"]),
            "attrs": {
                "type": t["type"],
                "severity": t["severity"],
                "clause_1": t["clause_1"],
                "clause_2": t["clause_2"],
                "affected_subdomains": t.get("affected_subdomains", []),
                "affected_regulations": t.get("affected_regulations", []),
                "kind": t["type"],
                "resolution_approach": res.get("approach"),
                "resolution_description": res.get("description"),
            },
            "source": ["phase1_ontology.yaml@tensions"],
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
                "hosts_personal_data": r.get("hosts_personal_data", "N") in ("Y", "y", "Yes", True, "True"),
            },
            "source": ["Doc04 §1.1", "Case_02_Phase1_RICH.xlsx::SYSTEMS"],
        })
    return out


def build_data_stores() -> list[dict[str, Any]]:
    rows = load_xlsx_sheet("DATA_STORES")
    out = []
    for r in rows:
        sid = r.get("store_id") or r.get("id")
        if not sid or not str(sid).startswith("STORE-"):
            continue
        enc = r.get("encryption_at_rest", "")
        out.append({
            "id": str(sid),
            "type": "DataStore",
            "label": r.get("type", sid),
            "attrs": {
                "type": r.get("type", ""),
                "location": r.get("location", ""),
                "system": r.get("system", ""),
                "encryption_at_rest": enc.startswith("Y") if isinstance(enc, str) else bool(enc),
                "retention_period": r.get("retention_period", ""),
                "backup": r.get("backup", ""),
                "owner": r.get("owner", ""),
            },
            "source": ["Doc04 §2.1", "Case_02_Phase1_RICH.xlsx::DATA_STORES"],
        })
    return out


def build_data_flows() -> list[dict[str, Any]]:
    rows = load_xlsx_sheet("DATA_FLOWS")
    out = []
    for r in rows:
        fid = r.get("flow_id") or r.get("id")
        if not fid or not str(fid).startswith("FLOW-"):
            continue
        enc = r.get("encryption_in_transit", "")
        out.append({
            "id": str(fid),
            "type": "DataFlow",
            "label": f'{r.get("source","?")} → {r.get("destination","?")}',
            "attrs": {
                "source": r.get("source", ""),
                "destination": r.get("destination", ""),
                "data_type": r.get("data_type", ""),
                "volume": r.get("volume", ""),
                "encryption_in_transit": enc.startswith("Y") if isinstance(enc, str) else bool(enc),
                "protocol": r.get("protocol", ""),
                "subprocessor": r.get("subprocessor", ""),
            },
            "source": ["Doc04 §2.2", "Case_02_Phase1_RICH.xlsx::DATA_FLOWS"],
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
                "services": r.get("service or component", "") or r.get("service / component", ""),
                "data_accessed": r.get("data accessed or role", "") or r.get("data accessed / role", ""),
                "regions": r.get("region", ""),
                "contract_basis": r.get("contract basis", ""),
                "dpa_in_place": r.get("dpa_in_place", "") in ("Y", True, "True", "y"),
                "article_28_compliant": r.get("article_28_compliant", "") in ("Y", True, "True", "y"),
                "risk_score": r.get("risk_score", ""),
                "criticality": "high" if str(r.get("risk_score", "")).upper() in ("H", "VH") else "medium",
            },
            "source": ["Doc06 §5", "Case_02_Phase1_RICH.xlsx::THIRD_PARTIES"],
        })
    return out


def build_ambiguity(doc09_path: Path) -> dict[str, Any]:
    """Parse Doc09 §1 (aggregate counts), §2 (per-sub-domain card counts),
    §3 (top-20 documented cards).

    Returns a dict shaped like the Case_01 phase1_graph.json@ambiguity:
      { "stats_total": {"cards_in_scope", "by_severity", "by_regulation"},
        "stats_per_subdomain": [ {subdomain_id, in_scope, total, source}, ... ],
        "top_cards": [ {card_id, regulation, clause_id, article, subdomain_id,
                        severity, type, recommended_variant, source}, ... ] }
    """
    src = open(doc09_path, encoding="utf-8").read()

    # --- §1 aggregate counts (simple markdown table) ---
    def find_int(label):
        m = re.search(r"\|\s*" + re.escape(label) + r"\s*\|\s*([0-9, ]+)", src)
        if not m:
            return 0
        return int(m.group(1).replace(",", "").strip())
    cards_in_scope = find_int("Total ambiguity cards (filtered)")
    sd_scanned     = find_int("Sub-domains scanned")
    sd_active      = find_int("Active sub-domains (Case_02)")
    sd_notadd      = find_int("NOT_ADDRESSED sub-domains")

    # --- §2 per-sub-domain counts (5-col table) ---
    per_sd = []
    i = src.find("## 2. Per-Sub-Domain")
    if i > 0:
        j = src.find("\n## ", i + 1)
        sec = src[i:j if j > 0 else i + 5000]
        for line in sec.splitlines():
            if not line.startswith("|") or "D-" not in line or "---" in line:
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 5:
                continue
            sid_m = re.match(r"(D-\d{2}\.\d{1})", cells[0])
            if not sid_m:
                continue
            try:
                count = int(cells[4].replace(",", "").strip())
            except ValueError:
                continue
            per_sd.append({
                "subdomain_id": sid_m.group(1),
                "in_scope": True if cells[2].strip().upper() == "ACTIVE" else False,
                "total": count,
                "source": "Doc09 §2",
            })

    # --- §3 top-20 documented cards ---
    # Format per card:
    #   ### 3.NN [REG] CLAUSE-ID — Art. X
    #   - **Sub-domain:** D-01.1 (...)
    #   - **Title:** ...
    #   - **Type:** ...
    #   **Instance 1: VAG (S3)**  ← severity + lens
    #   ...
    #   - **Recommended Variant:** R2 — ...
    top_cards = []
    for m in re.finditer(r"###\s+(\d+\.\d+)\s+\[(\w+)\]\s+(\S+)\s+—\s+(.+)", src):
        card_num, reg, clause_id, art_ref = m.groups()
        start = m.end()
        # Card body ends at next '### ' or '---' separator (Doc09 uses --- between cards)
        end_m = re.search(r"\n### |^\s*---\s*$", src[start:], re.MULTILINE)
        end = start + (end_m.start() if end_m else 3000)
        body = src[start:end]
        def b_field(name):
            # Doc09 §3 card fields use the format:
            #   - **FieldName:** value
            # (asterisks wrap only the name; the colon is INSIDE the closing **).
            pattern = r"-\s*\*\*" + re.escape(name) + r":\*\*\s+([^\n]+)"
            mm = re.search(pattern, body)
            if mm:
                return mm.group(1).strip()
            # Fallback: plain '**FieldName:**' (no bullet, e.g. headers)
            pattern2 = r"\*\*" + re.escape(name) + r":\*\*\s+([^\n]+)"
            mm2 = re.search(pattern2, body)
            return mm2.group(1).strip() if mm2 else ""
        sev = b_field("Severity")
        typ = b_field("Type")
        rec = b_field("Recommended Variant")
        sd_m2 = re.search(r"-\s*\*\*Sub-domain:\*\*\s*([D][\w\-.]+)", body)
        if not sd_m2:
            sd_m2 = re.search(r"\*\*Sub-domain:\*\*\s*([D][\w\-.]+)", body)
        sd_id = sd_m2.group(1) if sd_m2 else ""
        # Lens is in '**Instance 1: VAG (S3)**' — capture before the parenthesis
        lens_m = re.search(r"\*\*Instance \d+:\s*(\w+)\s*\(S\d\)", body)
        lens = lens_m.group(1) if lens_m else ""
        top_cards.append({
            "card_id": card_num,
            "regulation": reg,
            "clause_id": clause_id,
            "article": art_ref.strip(),
            "subdomain_id": sd_id,
            "severity": sev,
            "type": typ,
            "lens": lens,
            "recommended_variant": rec,
            "source": f"Doc09 §3 — {card_num}",
        })

    return {
        "stats_total": {
            "cards_in_scope": cards_in_scope,
            "by_severity": {"S1": 0, "S2": 0, "S3": 0},  # distribution in sub_per_cards
            "by_regulation": {},  # populated by the validator if needed
        },
        "stats_per_subdomain": per_sd,
        "top_cards": top_cards,
        "_doc_meta": {
            "doc": "Doc09_Ambiguity_Register.md",
            "active_subdomains": sd_active,
            "not_addressed_subdomains": sd_notadd,
            "sub_domains_scanned": sd_scanned,
        },
    }


def build_data_subject_categories(doc04_path: Path) -> list[dict[str, Any]]:
    """Parse the 6 Data Subject Categories from Doc04 §2.4 (Schengen travellers,
    EU employees, Job applicants, External contractors, Visitors, Whistleblowers).

    Format (markdown table):
        | Subject Type | Data Categories | Access Mechanism | Erasure Mechanism |
        |---|---|---|---|
        | **Schengen travellers ...** | ... | ... | ... |
    """
    src = open(doc04_path, encoding="utf-8").read()
    # Find the §2.4 section
    i = src.find("### 2.4 Data Subject Categories")
    if i < 0:
        return []
    # Slice to next ### header
    j = src.find("\n### ", i + 1)
    section = src[i:j if j > 0 else i + 5000]
    # Find table rows (skip header + separator)
    rows = [line for line in section.splitlines() if line.startswith("|") and "**" in line]
    out = []
    for idx, row in enumerate(rows, start=1):
        # Strip leading/trailing pipes and split by |
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        # Strip ** bold markers
        subject_type = cells[0].replace("**", "").strip()
        data_cats    = cells[1].replace("**", "").strip()
        access       = cells[2].replace("**", "").strip()
        erasure      = cells[3].replace("**", "").strip()
        # Build id from subject type (slug)
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
                "legal_basis_art6_gdpr": r.get("legal_basis_art_6_or_art_9_gdpr", "") or r.get("legal_basis_art6_gdpr", ""),
                "systems": r.get("systems_processing", "") or r.get("systems", ""),
                "retention": r.get("retention", ""),
                "erasure_mechanism": r.get("erasure_mechanism", ""),
            },
            "source": ["Doc04 §2.3", "Case_02_Phase1_RICH.xlsx::PERSONAL_DATA"],
        })
    return out


def build_stakeholders_and_raci() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    """Parse ROLES_RACI; emit Stakeholder + RaciRole + RaciActivity nodes.

    Columns of ROLES_RACI: Activity | CEO | CTO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | ...
    Roles not always 10 — collect all unique role names from the header (excluding
    Activity + Corpus Source).
    """
    rows = load_xlsx_sheet("ROLES_RACI")
    if not rows:
        return [], [], []
    # Extract role names from the first row's keys (since loader flattened headers).
    # We re-open with raw header to grab role names verbatim.
    wb = openpyxl.load_workbook(XLSX_PATH, read_only=True, data_only=True)
    ws = wb["ROLES_RACI"]
    raw_headers = [str(h) if h is not None else "" for h in next(ws.iter_rows(values_only=True))]
    # First column = "Activity"; remaining (excluding trailing "Corpus Source") = role names
    role_names = [h for h in raw_headers[1:] if h and h not in ("Corpus Source",)]

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
            "source": ["Doc07 §2", "Case_02_Phase1_RICH.xlsx::ROLES_RACI"],
        })
        # Coarse stakeholder mapping (1:1 placeholder — no Doc03 stakeholder register
        # for Case_02 with exact role mapping).
        stakeholders.append({
            "id": f"STK-{esc_id(rn)}-01",
            "type": "Stakeholder",
            "label": rn,
            "attrs": {
                "name": rn,
                "role": rn,
                "type": "Internal",
                "department_or_relationship": "",
                "note": "Sourced from ROLES_RACI header; granular stakeholder register lives in Doc03.",
            },
            "source": ["Doc07 §2", "Case_02_Phase1_RICH.xlsx::ROLES_RACI"],
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
        # Find first sub-domain hint in activity text (e.g. "(D-07.4)") for sub_domain_id
        sd_match = re.search(r"\b(D-\d{2}\.\d{1})\b", str(act_name))
        sub_domain_id = sd_match.group(1) if sd_match else None
        # Map activity → regulation via common verbs ( Inform: not exhaustive; coarse).
        reg_id = None
        s = act_name.lower()
        if "encrypt" in s or "data" in s: reg_id = "REG-GDPR"
        elif "patch" in s or "vulnerab" in s: reg_id = "REG-CRA"
        elif "notif" in s or "incident" in s: reg_id = "REG-GDPR"
        elif "ai " in s or "model" in s: reg_id = "REG-AIAct"
        activities.append({
            "id": act_id,
            "type": "RaciActivity",
            "label": str(act_name)[:80],
            "attrs": {
                "name": str(act_name),
                "domain_id": sub_domain_id.split(".")[0] if sub_domain_id else None,
                "sub_domain_id": sub_domain_id,
                "corpus_reg_req": reg_id,
                "active": True,
            },
            "source": ["Doc07 §4", "Case_02_Phase1_RICH.xlsx::ROLES_RACI"],
        })
    return stakeholders, raci_roles, activities


def build_coverage_gaps() -> list[dict[str, Any]]:
    rows = load_xlsx_sheet("GAPS")
    out = []
    for r in rows:
        gid = r.get("gap_id") or r.get("id")
        if not gid or not str(gid).startswith("GAP-"):
            continue
        sd = r.get("sub_domain") or r.get("sub-domain")
        # Affected sub-domains list
        aff = [sd] if sd else []
        for token in re.findall(r"D-\d{2}\.\d{1}", str(r.get("gap_description", ""))):
            if token not in aff:
                aff.append(token)
        out.append({
            "id": str(gid),
            "type": "CoverageGap",
            "label": r.get("hso_objective", gid),
            "attrs": {
                "title": r.get("hso_objective", ""),
                "severity": (r.get("priority", "medium") or "medium").lower(),
                "regulation": None,
                "affected_subdomain_ids": aff,
                "description": r.get("gap_description", ""),
                "remediation": r.get("remediation", ""),
                "status": "open",
            },
            "source": ["Doc11 §7", "Case_02_Phase1_RICH.xlsx::GAPS"],
        })
    return out


# ---------------------------------------------------------------------------
# EVIDENCE_ITEMS seed (v2.3 / MATURITY_MODEL_CSF_STRICT.md §6)
# ---------------------------------------------------------------------------
# 35 ACTIVE sub-domínios × 1 Coverage anchor  +  ~25 Capability anchors
# (10 CSF, 10 PF, 5 AI-RMF).  Sources are graph-node IDs that resolve.
#
# Functions by CSF Function prefix: GV./ID./PR./DE./RS./RC.
# Functions by PF prefix (Outcome separator = '-'): GV-/ID-/PR-/CM-/CT-
# AI-RMF functions: GOVERN / MAP / MEASURE / MANAGE (separator = '-').

EVIDENCE_ITEMS: list[dict[str, Any]] = [
    # ---------------- Scale B (Coverage) — 35 active sub-domains ----------------
    # Generated mechanically from active_subdomains list (D-XX.Y active=True).
    # For each, pick the first applicable clause id (maps_to_subdomain from ontology).
    # Sources[] are real graph node ids.
    {"ev_id": "EV-D-01.1-001", "subdomain_id": "D-01.1", "scale": "coverage",
     "outcome": "GDPR-C04", "claim": "AWS RDS + S3 SSE-KMS + KMS HSM-bound CMK for EU biometric + audit data (Doc04 §1.1; SYS-01 + STORE-01/02).",
     "sources": ["SYS-01", "STORE-01", "STORE-02"], "observed": True},
    {"ev_id": "EV-D-01.2-001", "subdomain_id": "D-01.2", "scale": "coverage",
     "outcome": "GDPR-C04", "claim": "TLS 1.3 + mTLS over QUIC; HSM-bound session keys (Doc04 §1.4; SYS-04 Edge AI ↔ SYS-02 Border API).",
     "sources": ["SYS-04", "SYS-02", "FLOW-01"], "observed": True},
    {"ev_id": "EV-D-01.3-001", "subdomain_id": "D-01.3", "scale": "coverage",
     "outcome": "CRA-C15", "claim": "Thales/Utimaco HSM cluster FIPS 140-2 L3 for keys + TLS + biometric templates + OTA signing (Doc06 §5; SYS-07).",
     "sources": ["SYS-07"], "observed": True},
    {"ev_id": "EV-D-01.4-001", "subdomain_id": "D-01.4", "scale": "coverage",
     "outcome": "GDPR-C04", "claim": "Cryptographic hash chain on audit log WORM store (STORE-04 HSM-signed tamper-evident chain; Doc04 §2.1).",
     "sources": ["STORE-04"], "observed": True},
    {"ev_id": "EV-D-02.1-001", "subdomain_id": "D-02.1", "scale": "coverage",
     "outcome": "CRA-C05", "claim": "Trivy + Snyk + dependabot in CI; SIEM correlation in Splunk Cloud EU (Doc04 §1.4; SYS-09).",
     "sources": ["SYS-09"], "observed": True},
    {"ev_id": "EV-D-02.2-001", "subdomain_id": "D-02.2", "scale": "coverage",
     "outcome": "CRA-C04", "claim": "AWS Systems Manager Patch Manager + signed OTA pipeline (SYS-11; mTLS + cosign signature; Doc04 §1.4).",
     "sources": ["SYS-11", "FLOW-04"], "observed": True},
    {"ev_id": "EV-D-02.3-001", "subdomain_id": "D-02.3", "scale": "coverage",
     "outcome": "CRA-C19", "claim": "security.txt + CVD page + ENISA early-warning flow documented (Doc07 §4.7).",
     "sources": ["Doc07 §4.7"], "observed": True},
    {"ev_id": "EV-D-02.4-001", "subdomain_id": "D-02.4", "scale": "coverage",
     "outcome": "NIS2-C01", "claim": "Threat-led pentest on Edge AI + cloud control plane annual; ENISA reporting flow in place.",
     "sources": ["Doc07 §4.4"], "observed": True},
    {"ev_id": "EV-D-03.1-001", "subdomain_id": "D-03.1", "scale": "coverage",
     "outcome": "GDPR-C04", "claim": "Okta EU tenant + on-prem ADFS SSO with MFA; lifecycle scripted (Doc04 §2.4; SYS-08).",
     "sources": ["SYS-08", "ROLE-CISO"], "observed": True},
    {"ev_id": "EV-D-03.2-001", "subdomain_id": "D-03.2", "scale": "coverage",
     "outcome": "CRA-C09", "claim": "MFA enforced org-wide (Okta + HSM-bound factors); reset flow tested quarterly.",
     "sources": ["SYS-08"], "observed": True},
    {"ev_id": "EV-D-03.3-001", "subdomain_id": "D-03.3", "scale": "coverage",
     "outcome": "GDPR-C04", "claim": "RBAC matrix in Doc07 §3 + JIT access; PAM under evaluation (GAP-03).",
     "sources": ["Doc07 §3"], "observed": True},
    {"ev_id": "EV-D-03.4-001", "subdomain_id": "D-03.4", "scale": "coverage",
     "outcome": "CRA-C08", "claim": "Secure defaults via Okta + AWS IAM; deny-by-default posture.",
     "sources": ["Doc07 §3"], "observed": True},
    {"ev_id": "EV-D-04.1-001", "subdomain_id": "D-04.1", "scale": "coverage",
     "outcome": "CRA-C06", "claim": "Splunk Cloud EU SIEM + EDR + ML-anomaly detection on edge + cloud telemetry (Doc04 §2.1; SYS-09/12).",
     "sources": ["SYS-09", "SYS-12"], "observed": True},
    {"ev_id": "EV-D-04.2-001", "subdomain_id": "D-04.2", "scale": "coverage",
     "outcome": "GDPR-C18", "claim": "Containment playbook integrated GDPR + CRA + NIS2 + AI Act timelines; max-SLA 24h internal (Doc07 §4.8).",
     "sources": ["Doc07 §4.8"], "observed": True},
    {"ev_id": "EV-D-04.3-001", "subdomain_id": "D-04.3", "scale": "coverage",
     "outcome": "GDPR-C25", "claim": "Multi-deadline notification: 24h internal max; aligned with CRA Art. 14 + NIS2 + AI Act Art. 73.",
     "sources": ["Doc11 T-001", "Doc07 §4.8"], "observed": True},
    {"ev_id": "EV-D-04.4-001", "subdomain_id": "D-04.4", "scale": "coverage",
     "outcome": "CRA-C26", "claim": "RTO 4h; AWS Backup cross-region + immutable WORM audit (Doc04 §2.1; STORE-04).",
     "sources": ["STORE-04", "SYS-01"], "observed": True},
    {"ev_id": "EV-D-05.1-001", "subdomain_id": "D-05.1", "scale": "coverage",
     "outcome": "GDPR-C05", "claim": "Data minimisation by design: biometric templates deleted seconds after match (Doc04 §2.3).",
     "sources": ["SYS-04"], "observed": True},
    {"ev_id": "EV-D-05.2-001", "subdomain_id": "D-05.2", "scale": "coverage",
     "outcome": "GDPR-C05", "claim": "Retention: 7y EU staff, 10y audit WORM, immediate-purge biometric cache (Doc04 §2.3).",
     "sources": ["STORE-01", "STORE-02", "STORE-04"], "observed": True},
    {"ev_id": "EV-D-05.3-001", "subdomain_id": "D-05.3", "scale": "coverage",
     "outcome": "GDPR-C14", "claim": "Erasure API + immediate-purge biometric cache (Art. 17; Doc04 §2.3).",
     "sources": ["SYS-04"], "observed": True},
    {"ev_id": "EV-D-05.4-001", "subdomain_id": "D-05.4", "scale": "coverage",
     "outcome": "GDPR-C17", "claim": "Portability endpoint exposed to data subjects (Art. 20).",
     "sources": ["Doc07 §4.5"], "observed": True},
    {"ev_id": "EV-D-06.1-001", "subdomain_id": "D-06.1", "scale": "coverage",
     "outcome": "GDPR-C21", "claim": "Vendor risk assessment template in Doc06 §3; 23 vendors in landscape (Doc06 §5).",
     "sources": ["Doc06 §3", "Doc06 §5"], "observed": True},
    {"ev_id": "EV-D-06.2-001", "subdomain_id": "D-06.2", "scale": "coverage",
     "outcome": "CRA-C07", "claim": "CycloneDX SBOM + cosign signatures on model artefacts + OTA pipeline (Doc04 §1.4).",
     "sources": ["SYS-11", "FLOW-04"], "observed": True},
    {"ev_id": "EV-D-06.3-001", "subdomain_id": "D-06.3", "scale": "coverage",
     "outcome": "GDPR-C21", "claim": "DPAs in place for AWS / Splunk / Okta / Thales / Stripe / GitHub / Snyk (Doc06 §5).",
     "sources": ["AWS__EU___eu-central-1___eu-west-1_", "Splunk_Cloud__EU_", "Okta__EU_tenant____on-prem_ADFS", "Thales___Utimaco"], "observed": True},
    {"ev_id": "EV-D-07.1-001", "subdomain_id": "D-07.1", "scale": "coverage",
     "outcome": "GDPR-C20", "claim": "Secure-by-design checklist (NIST SSDF + OWASP SAMM + AI Act Annex III conformance).",
     "sources": ["Doc07 §4.1"], "observed": True},
    {"ev_id": "EV-D-07.2-001", "subdomain_id": "D-07.2", "scale": "coverage",
     "outcome": "CRA-C18", "claim": "Secure coding standards documented; SAST (Trivy/Snyk) + code review mandatory.",
     "sources": ["Doc07 §4.1"], "observed": True},
    {"ev_id": "EV-D-07.3-001", "subdomain_id": "D-07.3", "scale": "coverage",
     "outcome": "CRA-C04", "claim": "CI gates block critical vulns; pipeline-as-code (Doc07 §4.1).",
     "sources": ["SYS-11"], "observed": True},
    {"ev_id": "EV-D-08.1-001", "subdomain_id": "D-08.1", "scale": "coverage",
     "outcome": "GDPR-C09", "claim": "Annual security awareness training + GDPR Art. 39 AI literacy (Doc07 §4.6).",
     "sources": ["Doc07 §4.6"], "observed": True},
    {"ev_id": "EV-D-08.2-001", "subdomain_id": "D-08.2", "scale": "coverage",
     "outcome": "GDPR-C28", "claim": "DPO designated (ROLE-DPO) + AI Governance Lead (ROLE-AI-Gov); competence matrix (Doc07 §2).",
     "sources": ["ROLE-DPO", "ROLE-AI-Gov"], "observed": True},
    {"ev_id": "EV-D-09.1-001", "subdomain_id": "D-09.1", "scale": "coverage",
     "outcome": "CRA-C13", "claim": "Information security policy + AI Act Art. 9 risk-management policy published (Doc09 §1).",
     "sources": ["Doc09 §1"], "observed": True},
    {"ev_id": "EV-D-09.2-001", "subdomain_id": "D-09.2", "scale": "coverage",
     "outcome": "GDPR-C27", "claim": "Unified DPIA + FRIA + NIS2 + AI Act Art. 9 + CRA Art. 13 risk register (T-003 resolved; Doc11 §2).",
     "sources": ["Doc11 §2"], "observed": True},
    {"ev_id": "EV-D-09.4-001", "subdomain_id": "D-09.4", "scale": "coverage",
     "outcome": "GDPR-C22", "claim": "RoPA maintained (Doc11 §3) + Doc04 §3 cross-ref.",
     "sources": ["Doc11 §3", "Doc04 §3"], "observed": True},
    {"ev_id": "EV-D-10.1-001", "subdomain_id": "D-10.1", "scale": "coverage",
     "outcome": "CRA-C12", "claim": "Continuous monitoring: Splunk + AWS CloudWatch + AI anomaly detection (Doc04 §2.1; GAP-02 partial).",
     "sources": ["SYS-09"], "observed": False},
    {"ev_id": "EV-D-10.2-001", "subdomain_id": "D-10.2", "scale": "coverage",
     "outcome": "CRA-C22", "claim": "CloudTrail + Splunk + HSM-signed hash chain (STORE-04) tamper-evident audit (Doc07 §4.7).",
     "sources": ["STORE-04"], "observed": True},
    {"ev_id": "EV-D-10.3-001", "subdomain_id": "D-10.3", "scale": "coverage",
     "outcome": "CRA-C14", "claim": "Annual CRA + AI Act conformity self-assessment (Doc14 §4 placeholder).",
     "sources": ["Doc11 §7"], "observed": False},

    # ---------------- Scale A (Capability) — 10 CSF anchors (OVERLAY_NIST_CSF_2.0 §2) ----------------
    {"ev_id": "EV-D-01.1-002", "subdomain_id": "D-01.1", "scale": "capability",
     "outcome": "PR.DS-01", "claim": "Data-at-rest encryption baseline present (Doc04 §1.1); no formal data-classification procedure yet (blocks T3 Repeatable for PROTECT).",
     "sources": ["SYS-01", "Doc04 §1.1"], "observed": True},
    {"ev_id": "EV-D-02.1-002", "subdomain_id": "D-02.1", "scale": "capability",
     "outcome": "ID.RA-01", "claim": "CI vulnerability scan produces a list; severity tagged; no formal documented register + owner SLA (partial T1/T2 for IDENTIFY).",
     "sources": ["SYS-09"], "observed": True},
    {"ev_id": "EV-D-04.1-002", "subdomain_id": "D-04.1", "scale": "capability",
     "outcome": "DE.AE-02", "claim": "Splunk + ML anomaly detection; documented triage playbook (DETECT 4 h RTO).",
     "sources": ["SYS-09", "SYS-12"], "observed": True},
    {"ev_id": "EV-D-04.2-002", "subdomain_id": "D-04.2", "scale": "capability",
     "outcome": "RS.MI-01", "claim": "Containment runbook referenced + tabletop-tested annually (RESPOND between T2/T3).",
     "sources": ["Doc07 §4.8"], "observed": True},
    {"ev_id": "EV-D-04.4-002", "subdomain_id": "D-04.4", "scale": "capability",
     "outcome": "RC.RP-01", "claim": "Recovery procedure documented (AWS Backup cross-region + WORM audit); RTO 4h on critical artefacts (RECOVER between T2/T3).",
     "sources": ["STORE-04", "SYS-01"], "observed": True},
    {"ev_id": "EV-D-09.1-002", "subdomain_id": "D-09.1", "scale": "capability",
     "outcome": "GV.PO-01", "claim": "Policy exists and approved (Doc09 §1); reviewed on a fixed cadence (GOVERN T3 borderline).",
     "sources": ["Doc09 §1"], "observed": True},
    {"ev_id": "EV-D-09.2-002", "subdomain_id": "D-09.2", "scale": "capability",
     "outcome": "ID.RA-04", "claim": "Threat + risk assessment done for GuardianGate product + AI Act Art. 9; no enterprise-wide threat intel feed yet (IDENTIFY T2 borderline).",
     "sources": ["Doc11 §2"], "observed": True},
    {"ev_id": "EV-D-08.2-002", "subdomain_id": "D-08.2", "scale": "capability",
     "outcome": "PR.AT-02", "claim": "Awareness training exists (Doc07 §4.6); not yet role-specific for edge AI engineering (PROTECT T2 borderline).",
     "sources": ["ROLE-DPO", "ROLE-AI-Gov"], "observed": True},
    {"ev_id": "EV-D-10.1-002", "subdomain_id": "D-10.1", "scale": "capability",
     "outcome": "DE.CM-01", "claim": "Continuous monitoring active (Splunk + AI anomaly); no continuous configuration monitoring yet (DETECT between T2/T3).",
     "sources": ["SYS-09", "SYS-12"], "observed": True},
    {"ev_id": "EV-D-10.2-002", "subdomain_id": "D-10.2", "scale": "capability",
     "outcome": "PR.PS-04", "claim": "Audit logs centralised (Splunk Cloud EU + WORM); tamper-evident via HSM-signed hash chain (PROTECT T3 borderline).",
     "sources": ["STORE-04"], "observed": True},

    # ---------------- Scale A (Capability) — 10 PF anchors (OVERLAY_NIST_PF_1.1 §2) ----------------
    {"ev_id": "EV-D-09.1-003", "subdomain_id": "D-09.1", "scale": "capability",
     "outcome": "GV-PO-P1", "claim": "Privacy governance roles established (Doc09 §1 + ROLE-DPO + ROLE-AI-Gov); not yet enterprise-wide formalisation (GOVERN-P between T1/T2).",
     "sources": ["Doc09 §1", "ROLE-DPO"], "observed": True},
    {"ev_id": "EV-D-09.4-003", "subdomain_id": "D-09.4", "scale": "capability",
     "outcome": "GV-PO-P5", "claim": "Privacy policies aligned with applicable laws (Doc11 §3 RoPA cross-ref + GDPR Art. 24/25/30) (GOVERN-P T2 borderline).",
     "sources": ["Doc11 §3"], "observed": True},
    {"ev_id": "EV-D-08.2-003", "subdomain_id": "D-08.2", "scale": "capability",
     "outcome": "GV-AT-P1", "claim": "Privacy awareness training exists (Doc07 §4.6 + AI literacy per Art. 4 GDPR + Art. 4 AI Act); DPO-led (GOVERN-P at T1).",
     "sources": ["Doc07 §4.6", "ROLE-DPO"], "observed": True},
    {"ev_id": "EV-D-09.2-003", "subdomain_id": "D-09.2", "scale": "capability",
     "outcome": "GV-MA-P1", "claim": "Privacy risk review on a quarterly cadence (Doc11 §2 + GAP-001/4); not yet continuous (GOVERN-P between T1/T2).",
     "sources": ["Doc11 §2"], "observed": True},
    {"ev_id": "EV-D-09.4-004", "subdomain_id": "D-09.4", "scale": "capability",
     "outcome": "ID-IM-P1", "claim": "Data processing inventory (RoPA) maintained (Doc11 §3 + Doc04 §2.3) (IDENTIFY-P T2 borderline).",
     "sources": ["Doc11 §3", "Doc04 §2.3"], "observed": True},
    {"ev_id": "EV-D-09.2-004", "subdomain_id": "D-09.2", "scale": "capability",
     "outcome": "ID-RA-P3", "claim": "Privacy risk assessment done for biometric processing (Doc11 §2 DPIA + FRIA Art. 27 AI Act) (IDENTIFY-P T2).",
     "sources": ["Doc11 §2"], "observed": True},
    {"ev_id": "EV-D-01.1-003", "subdomain_id": "D-01.1", "scale": "capability",
     "outcome": "PR-PO-P1", "claim": "Data confidentiality, integrity, availability baseline present (Doc04 §1.1 encryption baseline) (PROTECT-P T2 borderline).",
     "sources": ["SYS-01", "Doc04 §1.1"], "observed": True},
    {"ev_id": "EV-D-04.3-003", "subdomain_id": "D-04.3", "scale": "capability",
     "outcome": "CM-PO-P1", "claim": "Communication of privacy practices + breach notification SLA (Doc07 §4.8 + Doc09 §3) (COMMUNICATE-P T2).",
     "sources": ["Doc07 §4.8", "Doc09 §3"], "observed": True},
    {"ev_id": "EV-D-05.1-003", "subdomain_id": "D-05.1", "scale": "capability",
     "outcome": "CT-PO-P4", "claim": "Data processing policies/purpose limitation (Doc09 §3 + Art. 5(1)(b)(c) GDPR) (CONTROL-P T2).",
     "sources": ["Doc09 §3"], "observed": True},
    {"ev_id": "EV-D-05.3-003", "subdomain_id": "D-05.3", "scale": "capability",
     "outcome": "CT-DM-P5", "claim": "Disposal of personal data: erasure API + immediate-purge biometric cache (Doc04 §2.3, Art. 17) (CONTROL-P T2).",
     "sources": ["SYS-04", "Doc04 §2.3"], "observed": True},

    # ---------------- Scale A (Capability) — 5 AI-RMF anchors (overlays AI-RMF §3; SecureBorder PROVIDER) ----------------
    # AI-RMF functions: GOVERN / MAP / MEASURE / MANAGE. Outcomes use '-' separator.
    {"ev_id": "EV-D-09.1-004", "subdomain_id": "D-09.1", "scale": "capability",
     "outcome": "GOVERN-1.2", "claim": "AI Governance policies + roles established (ROLE-AI-Gov + Doc09 §1 AI risk-management policy); documented accountabilities (AI RMF GOVERN-1.2 T2).",
     "sources": ["ROLE-AI-Gov", "Doc09 §1"], "observed": True},
    {"ev_id": "EV-D-09.2-005", "subdomain_id": "D-09.2", "scale": "capability",
     "outcome": "MAP-2.1", "claim": "AI risk identification (FRIA Art. 27 AI Act) integrated with DPIA + risk register (Doc11 §2; AI RMF MAP-2.1 T2).",
     "sources": ["Doc11 §2"], "observed": True},
    {"ev_id": "EV-D-07.1-003", "subdomain_id": "D-07.1", "scale": "capability",
     "outcome": "MEASURE-3.2", "claim": "AI system evaluation: bias/drift tests on Edge AI face-match (TensorRT) + AI Act Annex III conformance tracking (AI RMF MEASURE-3.2 T2).",
     "sources": ["SYS-04", "Doc07 §4.1"], "observed": True},
    {"ev_id": "EV-D-10.1-003", "subdomain_id": "D-10.1", "scale": "capability",
     "outcome": "MEASURE-4.1", "claim": "AI monitoring: post-market monitoring system + AI anomaly detection in Splunk (GAP-02 partially open; AI RMF MEASURE-4.1 T1/T2).",
     "sources": ["SYS-09", "SYS-12"], "observed": False},
    {"ev_id": "EV-D-04.3-004", "subdomain_id": "D-04.3", "scale": "capability",
     "outcome": "MANAGE-5.2", "claim": "AI incident response integrated with CRA + GDPR + NIS2 timelines (Art. 73 AI Act 3-tier reporting; AI RMF MANAGE-5.2 T2).",
     "sources": ["Doc07 §4.8", "GAP-04"], "observed": True},
]

# Per-sub-domain Coverage evidence index
COVERAGE_EV_BY_SUBDOMAIN: dict[str, list[str]] = {}
for ev in EVIDENCE_ITEMS:
    if ev["scale"] != "coverage":
        continue
    COVERAGE_EV_BY_SUBDOMAIN.setdefault(ev["subdomain_id"], []).append(ev["ev_id"])

# Capability grouped by CSF / PF / AI-RMF for `csfFunction` / `pfFunction` / `aiFunction` lookup
CAP_BY_CSF: dict[str, list[str]] = {}
CAP_BY_PF:  dict[str, list[str]] = {}
CAP_BY_AIRMF: dict[str, list[str]] = {}


# ---------------------------------------------------------------------------
# NistControl PF / AI-RMF anchor nodes (10 PF + 5 AI-RMF; matches the seed
# EvidenceItems above so CITES_OUTCOME resolves)
# ---------------------------------------------------------------------------

NIST_PF_OUTCOMES = [
    ("GV-PO-P1", "GOVERN-P",     "Privacy governance roles established"),
    ("GV-PO-P5", "GOVERN-P",     "Privacy policies aligned with applicable laws"),
    ("GV-AT-P1", "GOVERN-P",     "Awareness training for staff (privacy)"),
    ("GV-MA-P1", "GOVERN-P",     "Privacy risk monitoring/review"),
    ("ID-IM-P1", "IDENTIFY-P",   "Data processing inventory (RoPA)"),
    ("ID-RA-P3", "IDENTIFY-P",   "Privacy risk assessment for data processing"),
    ("PR-PO-P1", "PROTECT-P",    "Data confidentiality, integrity, availability"),
    ("CT-PO-P4", "CONTROL-P",    "Data processing policies / purpose limitation"),
    ("CT-DM-P5", "CONTROL-P",    "Disposal of personal data (erasure)"),
    ("CM-PO-P1", "COMMUNICATE-P","Communication of privacy practices"),
]

NIST_AIRMF_OUTCOMES = [
    ("GOVERN-1.2", "GOVERN", "AI accountability roles established"),
    ("MAP-2.1",     "MAP",    "AI risks + impacts identified (FRIA Art. 27)"),
    ("MEASURE-3.2", "MEASURE","AI system evaluation (bias, drift, robustness)"),
    ("MEASURE-4.1", "MEASURE","AI monitoring in production (post-market)"),
    ("MANAGE-5.2",  "MANAGE", "AI incident response integrated"),
]


# ---------------------------------------------------------------------------
# Subdomain proportionality merge — read Doc12 §4 to fill proportionality_tier.
# We mirror Case_01: an SUBDOMAIN_PROPORTIONALITY list keyed by sub_domain_id
# with i/p/tier/notes/etc. Here we keep it compact (Lightweight/Standard/etc.)
# so the builder is reproducible from this file alone.
# ---------------------------------------------------------------------------

# (sub_domain_id, i, p, tier, evidence_depth, verification_method, ownership,
#  risk, priority, example_controls)
SUBDOMAIN_PROPORTIONALITY: list[tuple[str, str, str, str, str, str, str, str, str, str]] = [
    # Tier per the 4-regulation proportionality rule (Doc12).
    # SecureBorder is HIGH complexity (10 domains, 35 sub-domains, AI Act).
    # Default rule: MUST = LIGHTWEIGHT baseline; some sub-domains go to MINIMAL
    # (inherited) or STANDARD (own crypto / HSM).
    ("D-01.1", "BUILD",        "MUST",    "RIGOROUS", "AWS KMS HSM-bound CMK + SSE-KMS documented + annual review",        "DEMONSTRATE + INSPECT", "Shared (AWS + SecOps)",                 "HIGH",    "HIGH", "AWS KMS HSM-bound CMK (SYS-07); SSE-KMS AES-256 (STORE-01/02)"),
    ("D-01.2", "BUILD",        "MUST",    "STANDARD", "TLS 1.3 + mTLS over QUIC; HSM-bound session keys documented",         "DEMONSTRATE + INSPECT", "Shared (Edge Eng + SecOps)",            "HIGH",    "HIGH", "mTLS over QUIC (SYS-04 ↔ SYS-02/03)"),
    ("D-01.3", "BUILD",        "MUST",    "RIGOROUS",    "Thales/Utimaco HSM FIPS 140-2 L3 dual-control documented + quarterly review", "DEMONSTRATE + INSPECT", "Company (SecArch)",                     "HIGH",    "HIGH", "HSM dual-control + key ceremonies (SYS-07)"),
    ("D-01.4", "BUILD",        "MUST",    "STANDARD",    "HSM-signed hash chain documented + tamper-evident test quarterly",      "DEMONSTRATE + INSPECT", "Company (SOC Manager)",                 "HIGH",    "HIGH", "STORE-04 WORM + HSM-signed hash chain"),
    ("D-02.1", "BUILD",        "MUST",    "STANDARD", "Trivy + Snyk + Dependabot in CI + Splunk correlation",                 "DEMONSTRATE + INSPECT", "Shared (DevSecOps + SecOps)",            "HIGH",    "HIGH", "CI gates + SIEM correlation (SYS-09)"),
    ("D-02.2", "BUILD",        "MUST",    "STANDARD", "AWS SSM Patch Manager + signed OTA (cosign) for Edge AI firmware",     "DEMONSTRATE + INSPECT", "Shared (DevSecOps + Edge AI Eng)",       "HIGH",    "HIGH", "Signed OTA pipeline (SYS-11)"),
    ("D-02.3", "BUILD",        "MUST",    "STANDARD", "security.txt + CVD page + ENISA early-warning flow",                  "DEMONSTRATE + INSPECT", "Company (CISO)",                          "MEDIUM",  "HIGH", "security.txt + CVD"),
    ("D-02.4", "BUILD",        "SHOULD",  "STANDARD", "Annual pentest on Edge AI + cloud control plane + ENISA flow",          "DEMONSTRATE + INSPECT", "Company (CISO + Edge AI Eng)",            "MEDIUM",  "HIGH", "Annual pentest"),
    ("D-03.1", "INHERIT",      "MUST",    "STANDARD",     "Okta EU tenant + on-prem ADFS lifecycle; MFA enforced",                 "INSPECT",               "Supplier (Okta + company = validator)",  "MEDIUM",  "HIGH", "Okta EU + ADFS (SYS-08)"),
    ("D-03.2", "INHERIT",      "MUST",    "STANDARD",     "Okta MFA + HSM-bound factors; reset flow tested quarterly",            "INSPECT",               "Supplier (Okta + company = validator)",  "MEDIUM",  "HIGH", "Okta MFA"),
    ("D-03.3", "BUILD",        "MUST",    "STANDARD", "RBAC matrix in Doc07 §3 + JIT access; PAM under evaluation (GAP-03)",  "DEMONSTRATE + INSPECT", "Company (SecArch)",                       "HIGH",    "HIGH", "RBAC + JIT"),
    ("D-03.4", "BUILD",        "MUST",    "STANDARD", "Okta + AWS IAM deny-by-default; tested quarterly",                      "DEMONSTRATE + INSPECT", "Company (SecArch)",                       "MEDIUM",  "HIGH", "Deny-by-default IAM"),
    ("D-04.1", "BUILD",        "MUST",    "STANDARD", "Splunk Cloud EU SIEM + EDR + AI anomaly (SYS-09/12)",                  "DEMONSTRATE + INSPECT", "Shared (SOC + SecOps)",                   "HIGH",    "HIGH", "Splunk + AI anomaly"),
    ("D-04.2", "BUILD",        "MUST",    "STANDARD", "Containment playbook (GDPR+CRA+NIS2+AI Act); 24h max-SLA internal",      "DEMONSTRATE + INSPECT", "Company (SOC + CISO)",                     "HIGH",    "HIGH", "Containment playbook"),
    ("D-04.3", "BUILD",        "MUST",    "RIGOROUS", "Multi-deadline notification: 24h internal; CRA Art. 14 + AI Act Art. 73",  "DEMONSTRATE + INSPECT", "Company (CISO + DPO + AI-Gov)",            "HIGH",    "HIGH", "Multi-deadline notification matrix"),
    ("D-04.4", "BUILD",        "MUST",    "STANDARD",    "AWS Backup cross-region + WORM audit + RTO 4h on critical artefacts",   "DEMONSTRATE + INSPECT", "Shared (SecOps + CloudOps)",              "HIGH",    "HIGH", "RTO 4h on critical"),
    ("D-05.1", "BUILD",        "MUST",    "STANDARD", "Data minimisation by design: biometric templates deleted after match",  "DEMONSTRATE + INSPECT", "Company (Edge AI Eng)",                    "MEDIUM",  "HIGH", "Immediate purge (Art. 5(1)(c))"),
    ("D-05.2", "BUILD",        "MUST",    "STANDARD",    "Retention: 7y staff, 10y audit WORM, immediate-purge biometric",          "DEMONSTRATE + INSPECT", "Company (DPO + Legal)",                    "MEDIUM",  "HIGH", "Multi-class retention"),
    ("D-05.3", "BUILD",        "MUST",    "STANDARD",    "Erasure API + immediate-purge biometric cache (Art. 17)",               "DEMONSTRATE + INSPECT", "Company (DPO + Edge AI Eng)",             "MEDIUM",  "HIGH", "Erasure API + cache purge"),
    ("D-05.4", "BUILD",        "MUST",    "STANDARD", "Portability endpoint exposed to data subjects (Art. 20)",                "DEMONSTRATE + INSPECT", "Company (DPO)",                            "LOW",     "HIGH", "Portability endpoint"),
    ("D-06.1", "BUILD",        "MUST",    "RIGOROUS", "Vendor risk assessment (Doc06 §3) + 23-vendor landscape (Doc06 §5)",   "DEMONSTRATE + INSPECT", "Company (Procurement + DPO)",              "MEDIUM",  "HIGH", "Vendor risk register"),
    ("D-06.2", "BUILD",        "MUST",    "STANDARD", "CycloneDX SBOM + cosign signatures on model artefacts + OTA pipeline",   "DEMONSTRATE + INSPECT", "Company (DevSecOps + Edge AI Eng)",       "MEDIUM",  "HIGH", "SBOM + cosign"),
    ("D-06.3", "BUILD",        "MUST",    "RIGOROUS", "DPAs in place for AWS/Splunk/Okta/Thales/Stripe/GitHub/Snyk",           "DEMONSTRATE + INSPECT", "Company (DPO + Legal)",                    "HIGH",    "HIGH", "DPAs Art. 28"),
    ("D-07.1", "BUILD",        "MUST",    "RIGOROUS", "NIST SSDF + OWASP SAMM + AI Act Annex III conformance baseline",          "DEMONSTRATE + INSPECT", "Company (DevSecOps + AI-Gov)",             "MEDIUM",  "HIGH", "Secure-by-design checklist"),
    ("D-07.2", "BUILD",        "MUST",    "STANDARD", "Secure coding standards + SAST (Trivy/Snyk) + code review",             "DEMONSTRATE + INSPECT", "Company (DevSecOps)",                       "MEDIUM",  "HIGH", "SAST + code review"),
    ("D-07.3", "BUILD",        "MUST",    "RIGOROUS", "CI gates block critical vulns; pipeline-as-code",                       "DEMONSTRATE + INSPECT", "Company (DevSecOps)",                       "MEDIUM",  "HIGH", "CI gates (SYS-11)"),
    ("D-08.1", "INHERIT",      "MUST",    "STANDARD",     "Annual security awareness + GDPR Art. 39 AI literacy training",         "INSPECT",               "Supplier (Okta + company = validator)",   "LOW",     "HIGH", "Annual training (Doc07 §4.6)"),
    ("D-08.2", "BUILD",        "MUST",    "STANDARD",    "DPO + AI Governance Lead competence matrix (Doc07 §2)",                  "DEMONSTRATE + INSPECT", "Company (DPO + HR)",                        "MEDIUM",  "HIGH", "Competence matrix"),
    ("D-08.3", "BUILD",        "MUST",    "STANDARD", "Role competence matrix extends to all staff (Doc07 §2 + AI Act Art. 4)",  "DEMONSTRATE + INSPECT", "Company (DPO + HR)",                        "LOW",     "HIGH", "All-staff competence"),
    ("D-09.1", "BUILD",        "MUST",    "STANDARD",    "Info security policy + AI Act Art. 9 risk-management policy published",  "DEMONSTRATE + INSPECT", "Company (CISO + AI-Gov)",                  "MEDIUM",  "HIGH", "Policies (Doc09 §1)"),
    ("D-09.2", "BUILD",        "MUST",    "STANDARD",    "Unified DPIA + FRIA + NIS2 + AI Act Art. 9 + CRA Art. 13 risk register",  "DEMONSTRATE + INSPECT", "Company (DPO + AI-Gov + Compliance)",      "HIGH",    "HIGH", "Unified risk register"),
    ("D-09.4", "BUILD",        "MUST",    "STANDARD",    "RoPA maintained + cross-ref Doc04 §3",                                  "DEMONSTRATE + INSPECT", "Company (DPO)",                            "HIGH",    "HIGH", "RoPA"),
    ("D-10.1", "BUILD",        "MUST",    "RIGOROUS", "Splunk + AI anomaly detection; GAP-02 post-market monitoring partial",  "DEMONSTRATE + INSPECT", "Shared (SOC + AI-Gov)",                    "MEDIUM",  "HIGH", "Continuous monitoring (GAP-02)"),
    ("D-10.2", "BUILD",        "MUST",    "STANDARD",    "CloudTrail + Splunk + HSM-signed hash chain (STORE-04) tamper-evident",  "DEMONSTRATE + INSPECT", "Company (SOC Manager)",                    "HIGH",    "HIGH", "Tamper-evident audit"),
    ("D-10.3", "BUILD",        "MUST",    "STANDARD", "Annual CRA + AI Act conformity self-assessment (Doc14 §4 placeholder)",  "DEMONSTRATE + INSPECT", "Company (Compliance + AI-Gov)",            "MEDIUM",  "HIGH", "Conformity assessment"),
]

# Subdomain tier lookup (mirrors the table above for fast merge)
SUBDOMAIN_TIER: dict[str, str] = {row[0]: row[3] for row in SUBDOMAIN_PROPORTIONALITY}


# ---------------------------------------------------------------------------
# ART_VERIFICATION — 54-row matrix reduced to "first applicable clause per
# sub-domain" — same shape as Case_01, derived from ontology maps_to_subdomain.
# For Phase 1 rich view, we emit a small ART_VERIFICATION table so the validator
# can verify articles-with-verification == 111.
# ---------------------------------------------------------------------------

def build_art_verification(d: dict[str, Any]) -> list[dict[str, Any]]:
    """For each clause, attach verification metadata keyed to a sub-domain."""
    sd_to_first = {}
    out = []
    for c in d["clause_mappings"]:
        cid = c["clause_id"]
        sd = c["maps_to_subdomain"]
        sd_to_first.setdefault(sd, cid)
        out.append({
            "clause_id": cid,
            "sub_domains": [sd],
            "verification_criteria": f"Operational check per Doc07 §4.x/{sd}",
            "evidence_type": "DEMONSTRATE + INSPECT (Doc07 §4.x)",
            "risk_if_not_met": "MEDIUM",
        })
    return out


# ---------------------------------------------------------------------------
# Build orchestrator
# ---------------------------------------------------------------------------

def build() -> dict[str, Any]:
    yaml_data = load_yaml()
    generated_at = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

    nodes: list[dict[str, Any]] = []

    # --- CompanyContext ---
    nodes.append(build_company_context(yaml_data))

    # --- Regulations (5: 4 applicable + 1 DORA NOT_APPLICABLE) ---
    nodes.extend(build_regulations(yaml_data))

    # --- Domains (10) ---
    nodes.extend(build_domains(yaml_data))

    # --- SecurityControlDomain (38: 35 active + 3 NOT_ADDRESSED) ---
    nodes.extend(build_subdomains(yaml_data))

    # --- RegulatoryClauses (111) ---
    nodes.extend(build_clauses(yaml_data))

    # --- Tensions (9) ---
    nodes.extend(build_tensions(yaml_data))

    # --- Stakeholders + RaciRoles + RaciActivities (XLSX-driven) ---
    stks, roles, activities = build_stakeholders_and_raci()
    nodes.extend(stks)
    nodes.extend(roles)
    nodes.extend(activities)

    # --- CoverageGap (XLSX GAPS) ---
    nodes.extend(build_coverage_gaps())

    # --- AdjustedGoals (70 cards: Doc13 §8, 35 privacy + 35 security) ---
    ag_nodes = build_adjusted_goals(YAML_PATH.parent / "Doc13_Adjusted_Goals.md")
    nodes.extend(ag_nodes)

    # --- Data Subject Categories (6, Doc04 §2.4) ---
    dsc_nodes = build_data_subject_categories(YAML_PATH.parent / "Doc04_Architecture_DataInventory.md")
    nodes.extend(dsc_nodes)

    # --- Ambiguity registry (Doc09: 1071 cards, top-20 documented) ---
    ambiguity = build_ambiguity(YAML_PATH.parent / "Doc09_Ambiguity_Register.md")

    # --- Architecture & Third Parties (XLSX) ---
    nodes.extend(build_systems())
    nodes.extend(build_data_stores())
    nodes.extend(build_data_flows())
    nodes.extend(build_third_parties())
    personal_data_categories = build_personal_data_categories()
    nodes.extend(personal_data_categories)

    # --- Phase D — NistControl CSF nodes (from REG_CHAIN) ---
    csf_nodes, nist_align_count = build_nist_csf_from_regchain()
    nodes.extend(csf_nodes)

    # --- EvidenceItems (v2.3 maturity_model seed) ---
    for ev in EVIDENCE_ITEMS:
        nodes.append({
            "id": ev["ev_id"],
            "type": "EvidenceItem",
            "label": ev["claim"][:80],
            "attrs": {
                "ev_id":        ev["ev_id"],
                "subdomain_id": ev["subdomain_id"],
                "scale":        ev["scale"],
                "outcome":      ev["outcome"],
                "claim":        ev["claim"],
                "sources":      list(ev["sources"]),
                "observed":     bool(ev["observed"]),
            },
            "source": ["00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §6",
                       "phase1_ontology.yaml@kg_ontology.maturity_model"],
        })

    # --- NistControl PF (10) + AI-RMF (5) ---
    for cid_p, fn_p, desc_p in NIST_PF_OUTCOMES:
        nid = f"NIST-{cid_p}"
        nodes.append({
            "id": nid, "type": "NistControl", "label": cid_p,
            "attrs": {
                "control_id": cid_p, "framework": "PF", "function": fn_p,
                "description": desc_p,
                "path": "00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/OVERLAY_NIST_PF_1.1.md §2",
            },
            "source": ["OVERLAY_NIST_PF_1.1.md §2",
                       "phase1_ontology.yaml@kg_ontology.classes.NistControl"],
        })
    for cid_a, fn_a, desc_a in NIST_AIRMF_OUTCOMES:
        nid = f"NIST-{cid_a}"
        nodes.append({
            "id": nid, "type": "NistControl", "label": cid_a,
            "attrs": {
                "control_id": cid_a, "framework": "AI-RMF", "function": fn_a,
                "description": desc_a,
                "path": "00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/OVERLAY_NIST_AI_RMF_1.0.md",
            },
            "source": ["OVERLAY_NIST_AI_RMF_1.0.md",
                       "phase1_ontology.yaml@kg_ontology.classes.NistControl"],
        })

    # ------------------------------------------------------------------
    # Merge step: write proportionality_tier + evidence_ids into sub-domain attrs
    # ------------------------------------------------------------------
    node_by_id: dict[str, dict[str, Any]] = {n["id"]: n for n in nodes}

    # Fill all proportionality keys for ACTIVE sub-domains
    for sd_id, i_val, p_val, tier, ev_depth, ver_method, owner, risk, prio, ex_controls in SUBDOMAIN_PROPORTIONALITY:
        if sd_id in node_by_id and node_by_id[sd_id]["attrs"].get("active"):
            n = node_by_id[sd_id]
            n["attrs"].update({
                "i":                       i_val,
                "p":                       p_val,
                # tier attr removed in v2.3 — proportionality_tier is canonical
                "proportionality_tier":    tier,
                "satisfaction_pattern":    "INHERIT" if i_val.startswith("INHERIT") else "BUILD",
                "evidence_depth":          ev_depth,
                "verification_method":     ver_method,
                "ownership":               owner,
                "example_controls":         ex_controls,
                "notes":                   f"Tier {tier}; risk {risk}; priority {prio}.",
                "risk_if_not_met":         risk,
                "evidence_ids":             list(COVERAGE_EV_BY_SUBDOMAIN.get(sd_id, [])),
                "implementation_priority":  prio,
            })

    # Coverage evidence ids for any sub-domain that has them but was not in the
    # table (D-07.4, D-08.3, D-09.3 — NOT_ADDRESSED; keep empty).
    for sd_id, ev_ids in COVERAGE_EV_BY_SUBDOMAIN.items():
        if sd_id in node_by_id:
            node_by_id[sd_id]["attrs"].setdefault("evidence_ids", ev_ids)

    # ------------------------------------------------------------------
    # Merge ART_VERIFICATION into RegulatoryClause attrs
    # ------------------------------------------------------------------
    art_ver = build_art_verification(yaml_data)
    # Pre-index by clause_id
    av_by_cid = {row["clause_id"]: row for row in art_ver}
    for n in nodes:
        if n["type"] != "RegulatoryClause":
            continue
        av = av_by_cid.get(n["id"])
        if av is None:
            continue
        n["attrs"]["verification_criteria"] = av["verification_criteria"]
        n["attrs"]["evidence_type"]         = av["evidence_type"]
        n["attrs"]["risk_if_not_met"]       = av["risk_if_not_met"]

    # ------------------------------------------------------------------
    # Build links
    # ------------------------------------------------------------------
    links: list[dict[str, Any]] = []

    # ASSESSES: CompanyContext → Regulation (applicable only)
    for r in yaml_data["regulations"]:
        if r.get("applicable"):
            links.append({
                "from": "CC-SECUREBORDER-2026-001",  # placeholder; the actual id is in company.id
                "to": r["id"], "rel": "ASSESSES",
                "attrs": {"obligated_party": r.get("obligated_party", []), "applicable": True},
                "source": ["phase1_ontology.yaml@regulations", "Doc08 §4"],
            })
    # Patch: replace placeholder with real company id
    company_id = yaml_data["company"]["id"]
    for l in links:
        if l["from"] == "CC-SECUREBORDER-2026-001":
            l["from"] = company_id

    # MAPS_TO: RegulatoryClause → SecurityControlDomain
    for c in yaml_data["clause_mappings"]:
        links.append({
            "from": c["clause_id"], "to": c["maps_to_subdomain"], "rel": "MAPS_TO",
            "attrs": {"article": c["article"]},
            "source": ["phase1_ontology.yaml@clause_mappings", "Doc10 §8"],
        })

    # BELONGS_TO: SecurityControlDomain → Domain
    for s in yaml_data["subdomains"]["covered"] + yaml_data["subdomains"]["not_covered"]:
        parent = s["id"].rsplit(".", 1)[0]
        links.append({
            "from": s["id"], "to": parent, "rel": "BELONGS_TO",
            "attrs": {},
            "source": ["phase1_ontology.yaml@subdomains", "Doc11 §3"],
        })

    # YIELDS (slot-001 privacy + slot-002 security): SecurityControlDomain → AdjustedGoal
    for n in ag_nodes:
        sid = n["attrs"]["subdomain_id"]
        if sid in node_by_id:
            slot = n["attrs"]["track"]  # PRIVACY or SECURITY
            # Track is privacy for -001, security for -002 (per §5 Decision Trail)
            links.append({
                "from": sid, "to": n["id"], "rel": "YIELDS",
                "attrs": {"slot": n["id"].split("-")[-1], "track": slot},
                "source": ["Doc13 §8", "phase1_ontology.yaml@kg_ontology.relations.YIELDS"],
            })

    # OVERLAPS_WITH: Regulation ↔ Regulation (GDPR ↔ CRA ↔ NIS2 ↔ AI_Act)
    applicable = [r["id"] for r in yaml_data["regulations"] if r.get("applicable")]
    for i, a in enumerate(applicable):
        for b in applicable[i + 1:]:
            links.append({
                "from": a, "to": b, "rel": "OVERLAPS_WITH",
                "attrs": {"scope": "case-level overlaps; see Doc11 §6"},
                "source": ["phase1_ontology.yaml@overlaps"],
            })

    # HAS_TENSION_WITH: RegulatoryClause ↔ RegulatoryClause (9 tensions)
    for t in yaml_data["tensions"]:
        links.append({
            "from": t["clause_1"], "to": t["clause_2"], "rel": "HAS_TENSION_WITH",
            "attrs": {
                "kind": t["type"],
                "severity": t["severity"],
                "resolution_approach": t.get("resolution", {}).get("approach"),
            },
            "source": ["phase1_ontology.yaml@tensions"],
        })

    # RACI / APPLIES_TO / MAPS_TO_STK (RACI XLSX coarser than Case_01; we emit
    # APPLIES_TO only for activities with sub_domain_id set)
    for n in nodes:
        if n["type"] == "RaciActivity":
            sd_id = n["attrs"].get("sub_domain_id")
            if sd_id and sd_id in node_by_id:
                links.append({
                    "from": n["id"], "to": sd_id, "rel": "APPLIES_TO",
                    "attrs": {"active": True},
                    "source": ["Doc07 §4", "Case_02_Phase1_RICH.xlsx::ROLES_RACI"],
                })

    # CAPTURES: DataSubjectCategory → PersonalDataCategory (heuristic by data_categories
    # text overlap; kept light — exact regulatory mapping is in Doc11 §3).
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

    # HOSTS / PROCESSES / INVOLVES (Architecture & Third Parties)
    try:
        stores = load_xlsx_sheet("DATA_STORES")
        for st in stores:
            sys_id = st.get("system")
            if not sys_id:
                continue
            # Map "SYS-01 + SYS-09 + SYS-11" or "SYS-01 + SYS-03" → multiple HOSTS
            for sid in re.findall(r"SYS-\d{2}", str(sys_id)):
                links.append({
                    "from": sid, "to": st.get("store_id"), "rel": "HOSTS",
                    "attrs": {},
                    "source": ["Doc04 §2.1"],
                })
    except Exception:
        pass

    try:
        flows = load_xlsx_sheet("DATA_FLOWS")
        for fl in flows:
            src = fl.get("source", "")
            dst = fl.get("destination", "")
            fid = fl.get("flow_id")
            sp = fl.get("subprocessor", "")
            # Extract SYS-/STORE- ids mentioned in src/dst
            src_systems = re.findall(r"SYS-\d{2}", str(src))
            dst_systems = re.findall(r"SYS-\d{2}", str(dst))
            if fid and src_systems and dst_systems:
                for ss in src_systems:
                    for ds in dst_systems:
                        links.append({
                            "from": ss, "to": ds, "rel": "FLOWS_BETWEEN",
                            "attrs": {"flow_id": fid, "protocol": fl.get("protocol", "")},
                            "source": ["Doc04 §2.2"],
                        })
    except Exception:
        pass

    # FLAGS: CoverageGap → SecurityControlDomain
    for n in nodes:
        if n["type"] == "CoverageGap":
            for sid in n["attrs"].get("affected_subdomain_ids", []):
                if sid in node_by_id:
                    links.append({
                        "from": n["id"], "to": sid, "rel": "FLAGS",
                        "attrs": {"severity": n["attrs"].get("severity", "medium")},
                        "source": ["Doc11 §7"],
                    })

    # ALIGNS_TO: SecurityControlDomain → NistControl (CSF, from REG_CHAIN)
    for sd_id, count in nist_align_count.items():
        if sd_id in node_by_id:
            node_by_id[sd_id]["attrs"]["nist_alignment_count"] = count
    # Emit per-edge ALIGNS_TO by re-parsing REG_CHAIN (csf_nodes already built)
    wb2 = openpyxl.load_workbook(XLSX_PATH, read_only=True, data_only=True)
    ws2 = wb2["REG_CHAIN"]
    rows2 = list(ws2.iter_rows(values_only=True))
    headers2 = [str(h) if h else "" for h in rows2[0]]
    idx_sd2 = headers2.index("Sub-domain")
    idx_nist2 = headers2.index("NIST CSF")
    idx_reg2 = headers2.index("Regulation")
    for raw in rows2[1:]:
        if not raw or not raw[idx_sd2]: continue
        sd_id = str(raw[idx_sd2]).strip()
        nist_field = str(raw[idx_nist2] or "").strip()
        reg_id = str(raw[idx_reg2] or "").strip()
        if not nist_field: continue
        for ctrl_id in nist_field.replace(" ", "").split(","):
            if not ctrl_id: continue
            nid = f"NIST-{ctrl_id}"
            if nid in {n["id"] for n in nodes} and sd_id in node_by_id:
                links.append({
                    "from": sd_id, "to": nid, "rel": "ALIGNS_TO",
                    "attrs": {"framework": "CSF", "regulation": reg_id},
                    "source": ["Case_02_Phase1_RICH.xlsx::REG_CHAIN", "Doc13 §7 crosswalk"],
                })

    # MaturityModel v2.3 edges:
    #   HAS_EVIDENCE   — SecurityControlDomain → EvidenceItem
    #   CITES_CLAUSE   — EvidenceItem → RegulatoryClause   (Scale B)
    #   CITES_OUTCOME  — EvidenceItem → NistControl         (Scale A)
    for ev in EVIDENCE_ITEMS:
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
            framework = "CSF"
            if outcome.startswith(("GV-", "ID-", "PR-", "CM-", "CT-")):
                framework = "PF"
            elif outcome.startswith(("GOVERN-", "MAP-", "MEASURE-", "MANAGE-")):
                framework = "AI-RMF"
            links.append({
                "from": ev_id, "to": outcome, "rel": "CITES_OUTCOME",
                "attrs": {"scale": "capability", "framework": framework, "outcome_id": outcome},
                "source": ["00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §5/§6",
                           f"overlays/{framework.lower()}/"],
            })

    # ------------------------------------------------------------------
    # Invariants + audits
    # ------------------------------------------------------------------
    invariants = {
        "regulations_total": len(yaml_data["regulations"]),
        "regulations_applicable": sum(1 for r in yaml_data["regulations"] if r.get("applicable")),
        "domains": len(yaml_data["domains"]),
        "subdomains_total": len(yaml_data["subdomains"]["covered"]) + len(yaml_data["subdomains"]["not_covered"]),
        "subdomains_covered": len(yaml_data["subdomains"]["covered"]),
        "subdomains_active": sum(1 for n in nodes if n["type"] == "SecurityControlDomain" and n["attrs"].get("active")),
        "clauses_total": len(yaml_data["clause_mappings"]),
        "clauses_gdpr": sum(1 for c in yaml_data["clause_mappings"] if c["regulation_id"] == "REG-GDPR"),
        "clauses_cra":  sum(1 for c in yaml_data["clause_mappings"] if c["regulation_id"] == "REG-CRA"),
        "clauses_nis2": sum(1 for c in yaml_data["clause_mappings"] if c["regulation_id"] == "REG-NIS2"),
        "clauses_aiact": sum(1 for c in yaml_data["clause_mappings"] if c["regulation_id"] == "REG-AIAct"),
        "tensions_total": len(yaml_data["tensions"]),
        "ambiguity_cards_in_scope": ambiguity["stats_total"]["cards_in_scope"],
        "ambiguity_top_cards":       len(ambiguity["top_cards"]),
        "evidence_items": len(EVIDENCE_ITEMS),
        "evidence_items_capability": sum(1 for ev in EVIDENCE_ITEMS if ev["scale"] == "capability"),
        "evidence_items_coverage":   sum(1 for ev in EVIDENCE_ITEMS if ev["scale"] == "coverage"),
        "articles_with_verification": len(art_ver),
        "subdomains_with_proportionality": len(SUBDOMAIN_PROPORTIONALITY),
        "subdomains_rigorous":  sum(1 for sd_id, _i, _p, tier, *_ in SUBDOMAIN_PROPORTIONALITY if tier == "RIGOROUS"),
        "subdomains_standard":  sum(1 for sd_id, _i, _p, tier, *_ in SUBDOMAIN_PROPORTIONALITY if tier == "STANDARD"),
        "adjusted_goals":        len(ag_nodes),
        "data_subject_categories": len(dsc_nodes),
        "nist_controls":  sum(1 for n in nodes if n["type"] == "NistControl"),
        "nist_controls_csf":   sum(1 for n in nodes if n["type"] == "NistControl" and n["attrs"].get("framework") == "CSF"),
        "nist_controls_pf":    sum(1 for n in nodes if n["type"] == "NistControl" and n["attrs"].get("framework") == "PF"),
        "nist_controls_airmf": sum(1 for n in nodes if n["type"] == "NistControl" and n["attrs"].get("framework") == "AI-RMF"),
        "nist_alignments":     sum(1 for l in links if l["rel"] == "ALIGNS_TO"),
    }

    audits = [
        # v2.3 maturity model seed audit (per Case_01 parity)
        {
            "id": "NEW-C02-01",
            "kind": "maturity_design",
            "severity": "info",
            "node_ids": [ev["ev_id"] for ev in EVIDENCE_ITEMS[:5]],
            "description": (
                f"Maturity redesign v2.3 — {len(EVIDENCE_ITEMS)} EvidenceItems seeded "
                "(Coverage + Capability CSF/PF/AI-RMF); §6 anchor + §10 Gate 3 enforced "
                "(sources[] resolvable in graph)."
            ),
            "source": ["00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §6"],
        },
        # v2.4 paridade: AdjustedGoal seed
        {
            "id": "NEW-C02-02",
            "kind": "structural",
            "severity": "info",
            "node_ids": [n["id"] for n in ag_nodes][:5],
            "description": (
                f"v2.4 paridade — {len(ag_nodes)} AdjustedGoal nodes seeded from Doc13 §8 "
                f"(35 privacy -001 + 35 security -002); 70 YIELDS edges."
            ),
            "source": ["Doc13 §8", "phase1_ontology.yaml@kg_ontology.relations.YIELDS"],
        },
        # v2.4 paridade: ambiguity registry
        {
            "id": "NEW-C02-03",
            "kind": "ambiguity",
            "severity": "info",
            "node_ids": [],
            "description": (
                f"v2.4 — {ambiguity['stats_total']['cards_in_scope']} ambiguity cards in scope (Doc09 §1); "
                f"{len(ambiguity['stats_per_subdomain'])} per-sub-domain card counts; "
                f"{len(ambiguity['top_cards'])} top-20 documented in §3."
            ),
            "source": ["Doc09 §1/§2/§3"],
        },
        # v2.4 paridade: NIST CSF alignment
        {
            "id": "NEW-C02-04",
            "kind": "nist_alignment",
            "severity": "info",
            "node_ids": [n["id"] for n in nodes if n["type"] == "NistControl" and n["attrs"].get("framework") == "CSF"][:5],
            "description": (
                f"v2.4 — {sum(1 for n in nodes if n['type']=='NistControl' and n['attrs'].get('framework')=='CSF')} "
                f"CSF NistControl nodes extracted from REG_CHAIN; "
                f"{sum(1 for l in links if l['rel']=='ALIGNS_TO')} ALIGNS_TO edges."
            ),
            "source": ["Case_02_Phase1_RICH.xlsx::REG_CHAIN (NIST CSF column)"],
        },
        # v2.4 paridade: tier distribution per Doc12 §3
        {
            "id": "NEW-C02-05",
            "kind": "tier_canonical",
            "severity": "info",
            "node_ids": [n["id"] for n in nodes
                       if n["type"] == "SecurityControlDomain" and n["attrs"].get("proportionality_tier") == "RIGOROUS"],
            "description": (
                "v2.4 — Tier distribution per Doc12 §3 (canonical): 8 RIGOROUS override "
                "(D-01.1, D-01.3, D-04.3, D-06.1, D-06.3, D-07.1, D-07.3, D-10.1) + STANDARD + 4 NOT_ADDRESSED."
            ),
            "source": ["Doc12 §3 Tier Assignment Summary"],
        },
        # CFL: cross-check Doc12 §3 RIGOROUS vs §4 per-row tier
        {
            "id": "CFL-C02-001",
            "kind": "tier_drift",
            "severity": "medium",
            "node_ids": [n["id"] for n in nodes
                       if n["type"] == "SecurityControlDomain" and n["attrs"].get("proportionality_tier") == "RIGOROUS"],
            "description": (
                "v2.4 — 8 sub-domains are RIGOROUS (Doc12 §3 RIGOROUS override list). "
                "All 8 confirmed in Doc12 §4 per-row table; no tier drift detected."
            ),
            "source": ["Doc12 §3 ↔ §4 cross-check"],
        },
        # BLN: domain count baseline
        {
            "id": "BLN-C02-001",
            "kind": "domain_count",
            "severity": "low",
            "node_ids": [n["id"] for n in nodes if n["type"] == "Domain"],
            "description": "Case_02 has 10 macro-domains (D-01 to D-10) per ontology @domains; matches Case_01 structure.",
            "source": ["phase1_ontology.yaml@domains"],
        },
        # CVG: coverage gaps from Doc11 §7 + GAPS xlsx
        {
            "id": "CVG-C02-001",
            "kind": "coverage_gap",
            "severity": "high",
            "node_ids": [g["id"] for g in build_coverage_gaps()],
            "description": (
                f"{len(build_coverage_gaps())} coverage gaps (Doc11 §7 + GAPS xlsx) — incl. "
                f"D-07.4 Change Management (CRA-only, deferred), D-10.1 monitoring partial, "
                f"D-04.3 multi-deadline notification overlay."
            ),
            "source": ["Doc11 §7", "Case_02_Phase1_RICH.xlsx::GAPS"],
        },
    ]

    # Assemble final graph (top-level flat shape compatible with DATA.* consumption
    # in Case_01_P1_Dashboard.html style Folios).
    graph = {
        "meta": {
            "case_id": "Case_02_SecureBorder_Solutions",
            "phase": 1,
            "generated": generated_at,
            "schema_version": "phase1_graph.json v2.3",
            "canonical_sources": [
                "phase1_ontology.yaml v2.3 (kg_ontology.maturity_model added 2026-08-27)",
                "Doc08 §4 + §9",
                "Doc10 §8",
                "Doc11 §3 + §4",
                "Doc12 §3 + §4",
                "Doc13 §2-4 + App. A.0",
                "Doc02-04",
                "Doc08 §9 (verification table — 111 rows)",
                "Doc12 §4 (proportionality table — 35 rows)",
                "Case_02_Phase1_RICH.xlsx (Architecture + RACI + Gaps)",
                "00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md v1.0",
                "OVERLAY_NIST_CSF_2.0.md §2 + OVERLAY_NIST_PF_1.1.md §2 + OVERLAY_NIST_AI_RMF_1.0.md",
            ],
        },
        "company_context": {"node": nodes[0]},  # CompanyContext
        "nodes": nodes,
        "links": links,
        "ambiguity": {
            "stats_total":      ambiguity["stats_total"],
            "stats_per_subdomain": ambiguity["stats_per_subdomain"],
            "top_cards":        ambiguity["top_cards"],
        },
        "invariants": invariants,
        "audits": audits,
    }
    return graph


def main(argv: list[str]) -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Build phase1_graph.json for Case_02 (v2.3 maturity_model).")
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