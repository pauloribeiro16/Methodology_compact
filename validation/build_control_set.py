#!/usr/bin/env python3
"""
AEGIS Control Set Generator — build_control_set.py (v1.0)
Parses Doc18_Rules_Catalog.md and generates control_set.yaml.
Standard library only.
"""

import os
import re
import yaml

DOC18_PATH = "02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/Doc18_Rules_Catalog.md"
OUTPUT_YAML = "02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/control_set.yaml"

def parse_doc18():
    if not os.path.exists(DOC18_PATH):
        raise FileNotFoundError(f"Doc18 not found at {DOC18_PATH}")

    with open(DOC18_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    cards = re.findall(r"(### (?:CR|BPR)-D-\d+\.\d+-\d+.*?)(?=\n### (?:CR|BPR)-D-\d+\.\d+-\d+|\n---|\Z)", content, flags=re.DOTALL)
    
    controls = []
    
    for c in cards:
        lines = [line.strip() for line in c.strip().split("\n") if line.strip()]
        header = lines[0]
        
        m_head = re.search(r"### ((?:CR|BPR)-D-\d+\.\d+-\d+) — (.*)", header)
        if not m_head:
            continue
            
        rule_id = m_head.group(1)
        title = m_head.group(2).strip()
        is_cr = rule_id.startswith("CR")
        
        register = "OBLIGATION" if is_cr else "BEST_PRACTICE"
        
        # Extract fields
        subdomain = ""
        source_raw = ""
        ni_val = 3.0 if is_cr else 2.0
        ni_bucket = "MUST" if is_cr else "SHOULD"
        
        csf_status = "PARTIAL"
        priv_status = "PARTIAL"
        missing_text = ""
        evidence_text = ""
        
        verif_method = "TEST"
        owner = "CTO + Lead Dev"
        
        trace_legal = []
        ag_phase1 = ""
        obligations = []
        objectives = []
        trace_gaps = []
        
        anchors_csf = []
        anchors_pf = []
        pf_gaps = []
        iso_anchors = []
        ssdf_anchors = []
        
        for line in lines:
            if "Sub-Domain:" in line:
                m_sub = re.search(r"D-\d+\.\d+", line)
                if m_sub:
                    subdomain = m_sub.group(0)
            elif "Source Article:" in line or "Source:" in line:
                source_raw = line.split(":", 1)[1].strip()
            elif "Verification Method:" in line:
                verif_method = line.split(":", 1)[1].strip()
            elif "Owner:" in line:
                owner = line.split(":", 1)[1].strip()
            elif "21. **Implementation Status (CSF):**" in line:
                st = line.split(":", 1)[1].strip()
                csf_status = st.split()[0]
                if "evidence:" in st.lower():
                    evidence_text = st
                elif "missing:" in st.lower():
                    missing_text = st
            elif "22. **Implementation Status (Privacy):**" in line:
                st = line.split(":", 1)[1].strip()
                priv_status = st.split()[0]
            elif line.startswith("- Legal:"):
                leg = line.split(":", 1)[1].strip()
                trace_legal = [x.strip() for x in leg.split(";") if x.strip()]
            elif line.startswith("- Phase 1:"):
                ag_phase1 = line.split(":", 1)[1].strip().split()[0]
            elif line.startswith("- Obligation:"):
                obl = line.split(":", 1)[1].strip()
                obligations = [x.strip() for x in obl.split(",") if x.strip() and x.strip() != "N/A"]
            elif line.startswith("- Objective:"):
                obj = line.split(":", 1)[1].strip()
                objectives = [x.strip() for x in obj.split(",") if x.strip() and x.strip() != "N/A"]
            elif line.startswith("- CSF:"):
                c_val = line.split(":", 1)[1].strip()
                anchors_csf = [x.strip() for x in c_val.split(",") if x.strip()]
            elif line.startswith("- PF:"):
                p_val = line.split(":", 1)[1].strip()
                anchors_pf = [x.strip() for x in p_val.split(",") if x.strip()]
            elif line.startswith("- PF Gap:"):
                pf_gaps.append(line.split(":", 1)[1].strip())
            elif line.startswith("- ISO 27001:"):
                i_val = line.split(":", 1)[1].strip()
                iso_anchors = [x.strip() for x in i_val.split(",") if x.strip()]
            elif line.startswith("- SSDF:"):
                s_val = line.split(":", 1)[1].strip()
                if s_val != "-":
                    ssdf_anchors = [x.strip() for x in s_val.split(",") if x.strip()]

        if not subdomain:
            m_sub = re.search(r"D-\d+\.\d+", rule_id)
            if m_sub:
                subdomain = m_sub.group(0)

        c_entry = {
            "id": rule_id,
            "register": register,
            "domain": subdomain,
            "title": title,
            "ni": {"value": ni_val, "bucket": ni_bucket},
            "legal": trace_legal if trace_legal else ([source_raw] if source_raw else []),
            "trace": {
                "phase1": ag_phase1 if ag_phase1 else f"AG-{subdomain.split('.')[0]}",
                "obligations": obligations if obligations else ([f"OBL-{rule_id[3:]}"] if is_cr else []),
                "objectives": objectives,
                "gaps": trace_gaps
            },
            "anchors": {
                "csf": anchors_csf,
                "pf": anchors_pf,
                "pf_gaps": pf_gaps,
                "airmf": "N/A (non-AI scope)",
                "iso": iso_anchors,
                "ssdf": ssdf_anchors
            },
            "status": {
                "csf": csf_status,
                "privacy": priv_status,
                "missing": missing_text,
                "evidence": evidence_text
            },
            "verification": {
                "method": verif_method,
                "owner": owner
            }
        }
        controls.append(c_entry)
        
    data = {
        "control_set": {
            "case": "Case_01_TinyTask_SaaS",
            "source": "Doc18_Rules_Catalog.md",
            "total_controls": len(controls),
            "controls": controls
        }
    }
    
    with open(OUTPUT_YAML, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        
    print(f"Generated control_set.yaml cleanly with {len(controls)} controls!")

if __name__ == "__main__":
    parse_doc18()
