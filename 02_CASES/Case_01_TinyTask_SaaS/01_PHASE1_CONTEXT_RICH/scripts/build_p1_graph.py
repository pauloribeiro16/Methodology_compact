#!/usr/bin/env python3
"""Build phase1_graph.json from Case_01 Phase 1 Rich source documents.

This is the EXECUTOR's generator script. It reads no external files — all source
data is encoded inline as Python literals, derived by manual reading of the
Phase 1 Rich corpus (phase1_ontology.yaml v1.1, Doc02-03, Doc08, Doc09 §1-3,
Doc10 §8, Doc11 §3-4, Doc12 §3-4, Doc13 §2-4 + App. A.0).

The output JSON schema is defined in the orchestrator brief. Invariant
totals: regs=5, applicable=2, domains=10, subdomains=38 (covered=31,
active=37), clauses=54, goals=69, tensions=4, ambiguity cards=417.

This script is intentionally split from `build_p1_dashboard.py` so that the
JSON can be regenerated or reviewed independently of the dashboard inlining.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "phase1_graph.json"

# ---------------------------------------------------------------------------
# 1. Meta + company context
# ---------------------------------------------------------------------------

META = {
    "case_id": "Case_01_TinyTask_SaaS",
    "phase": 1,
    "generated": "2026-08-26",
    "schema_version": "1.0",
    # NOTE: Sprint 7 (RACI Phase A — Doc07) — canonical_sources[0] bumped
    # 1.2 → 1.3 (ontology v1.3 adds RaciRole/RaciActivity classes + RACI/APPLIES_TO
    # relations). The other 7 entries are retained verbatim; no entry was added
    # or reordered.
    "canonical_sources": [
        "phase1_ontology.yaml@01_PHASE1_CONTEXT_RICH v1.3",
        "Doc08 §4 + §9",
        "Doc10 §8",
        "Doc11 §3 + §4",
        "Doc12 §3 + §4",
        "Doc13 §2-4 + App. A.0",
        "Doc09 §1-3",
        "Doc02-03",
        # Phase C — Doc08 §9 + Doc12 §4 extension (no new sources; existing
        # 'Doc08 §4 + §9' / 'Doc12 §3 + §4' entries already point to the
        # right sections — appended here as standalone record).
        "Doc08 §9 (verification table — 54 rows)",
        "Doc12 §4 (proportionality table — 37 rows)",
        # Phase D — Doc13 §7 NIST Controls Mapping (35 sub-domain × 1-3 NIST
        # frameworks = 513 alignment rows; 117 unique control IDs).
        "Doc13 §7 (NIST CSF 2.0 + PF 1.0 + AI RMF mapping — 513 rows)",
    ],
}

COMPANY = {
    "node": {
        "id": "CC-TINYTASK-2026-001",
        "type": "CompanyContext",
        "label": "TinyTask Lda.",
        "attrs": {
            "scale": "MICRO",
            "tier_v1_1": "MEDIUM",
            "employees": 8,
            "security_fte": 0.85,
            "hq": "Lisbon, PT (EU)",
            "sector": "Technology / Software B2B SaaS",
            "product": "Team Organizer",
            "stack": ["AWS eu-west-1", "Firebase Auth", "Stripe", "GitHub Actions"],
            "data_types": [
                "email",
                "name",
                "password",
                "task_content",
                "ip_address (server logs)",
            ],
            "roles": {
                "GDPR": ["CONTROLLER", "PROCESSOR"],
                "CRA": ["MANUFACTURER (Default class)"],
            },
            "criticality": "Non-Critical",
        },
        "source": ["Doc02 §2/§3", "Doc03 §4", "phase1_ontology.yaml@company"],
    }
}

# ---------------------------------------------------------------------------
# 2. Regulations (5)
# ---------------------------------------------------------------------------

REGULATIONS = [
    {
        "id": "REG-GDPR",
        "type": "Regulation",
        "label": "GDPR — Reg. (EU) 2016/679",
        "attrs": {
            "abbreviation": "GDPR",
            "name": "General Data Protection Regulation",
            "eu_reference": "Regulation (EU) 2016/679",
            "applicable": True,
            "obligated_party": ["CONTROLLER", "PROCESSOR"],
            "clause_count": 28,
            "reason": "processes_personal_data = true (dual role: CONTROLLER + PROCESSOR)",
        },
        "source": ["Doc08 §3.1 + §4", "phase1_ontology.yaml@regulations[REG-GDPR]"],
    },
    {
        "id": "REG-CRA",
        "type": "Regulation",
        "label": "CRA — Reg. (EU) 2024/2847",
        "attrs": {
            "abbreviation": "CRA",
            "name": "Cyber Resilience Act",
            "eu_reference": "Regulation (EU) 2024/2847",
            "applicable": True,
            "obligated_party": ["MANUFACTURER"],
            "clause_count": 26,
            "reason": "places_digital_products_eu = true",
        },
        "source": ["Doc08 §3.2 + §4", "phase1_ontology.yaml@regulations[REG-CRA]"],
    },
    {
        "id": "REG-NIS2",
        "type": "Regulation",
        "label": "NIS 2 — Dir. (EU) 2022/2555",
        "attrs": {
            "abbreviation": "NIS 2",
            "name": "Network and Information Systems Directive 2",
            "eu_reference": "Directive (EU) 2022/2555",
            "applicable": False,
            "obligated_party": [],
            "clause_count": 0,
            "reason": "below_threshold (8 employees < 50 threshold)",
        },
        "source": ["Doc08 §3.3 + §4", "phase1_ontology.yaml@regulations[REG-NIS2]"],
    },
    {
        "id": "REG-DORA",
        "type": "Regulation",
        "label": "DORA — Reg. (EU) 2022/2554",
        "attrs": {
            "abbreviation": "DORA",
            "name": "Digital Operational Resilience Act",
            "eu_reference": "Regulation (EU) 2022/2554",
            "applicable": False,
            "obligated_party": [],
            "clause_count": 0,
            "reason": "not_financial_entity",
        },
        "source": ["Doc08 §3.4 + §4", "phase1_ontology.yaml@regulations[REG-DORA]"],
    },
    {
        "id": "REG-AIACT",
        "type": "Regulation",
        "label": "AI Act — Reg. (EU) 2024/1689",
        "attrs": {
            "abbreviation": "AI Act",
            "name": "Artificial Intelligence Act",
            "eu_reference": "Regulation (EU) 2024/1689",
            "applicable": False,
            "obligated_party": [],
            "clause_count": 0,
            "reason": "no_ai_systems (aiact_high_risk_system = false)",
        },
        "source": ["Doc08 §3.5 + §4", "phase1_ontology.yaml@regulations[REG-AIACT]"],
    },
]

# ---------------------------------------------------------------------------
# 3. Domains (10) + Sub-domains (38)
# ---------------------------------------------------------------------------

# Each domain record: id, label, primary_regulatory_driver
DOMAINS = [
    ("D-01", "Data Protection & Encryption", "GDPR", 4),
    ("D-02", "Vulnerability Management", "CRA", 4),
    ("D-03", "Access Control", "GDPR", 4),
    ("D-04", "Incident Response", "GDPR", 4),
    ("D-05", "Data Lifecycle", "GDPR", 4),
    ("D-06", "Supply Chain", "DORA", 4),
    ("D-07", "Secure Development", "CRA", 4),
    ("D-08", "Human Factors", "NIS2", 3),
    ("D-09", "Governance & Documentation", "GDPR", 4),
    ("D-10", "Monitoring & Audit", "DORA", 3),
]

# Subdomain definitions: id, name, source_regs (in ontology), covered,
# coverage_level (Doc11 §3), proportional_tier (Doc12 §3), inactive flag,
# sole_authority (for not-covered)
SUBDOMAIN_DEFS = [
    # D-01: covered 4/4
    ("D-01.1", "Data at Rest Encryption", ["GDPR", "CRA"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-01.2", "Data in Transit Encryption", ["GDPR", "CRA"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-01.3", "Cryptographic Key Management", ["CRA"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-01.4", "Data Integrity Mechanisms", ["GDPR", "CRA"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    # D-02: 3/4 covered, D-02.4 NOT_ADDRESSED
    ("D-02.1", "Vulnerability Identification", ["CRA"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    ("D-02.2", "Patch Management & Updates", ["CRA"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    ("D-02.3", "Coordinated Vuln. Disclosure", ["CRA"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    ("D-02.4", "Threat-Led Penetration Testing", [], False, "NOT_ADDRESSED", "DEFERRED", False, "DORA"),
    # D-03: 4/4 covered
    ("D-03.1", "Identity Lifecycle Management", ["CRA"], True, "SUBSTANTIVE", "MINIMAL", False, None),
    ("D-03.2", "Multi-Factor Authentication", ["CRA"], True, "SUBSTANTIVE", "MINIMAL", False, None),
    ("D-03.3", "Authorization & Least Privilege", ["GDPR"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    ("D-03.4", "Secure System Defaults", ["CRA"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    # D-04: 4/4 covered
    ("D-04.1", "Incident Detection & Triage", ["CRA"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-04.2", "Containment & Mitigation", ["GDPR", "CRA"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-04.3", "Regulatory Notification", ["GDPR", "CRA"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-04.4", "Data Restoration & Recovery", ["GDPR"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    # D-05: 4/4 covered
    ("D-05.1", "Data Minimization", ["GDPR"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-05.2", "Retention & Archiving", ["GDPR"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    ("D-05.3", "Right to Erasure", ["GDPR"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-05.4", "Data Portability", ["GDPR"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    # D-06: 3/4 covered, D-06.4 NOT_ADDRESSED
    ("D-06.1", "Vendor Risk Assessment", ["GDPR"], True, "PARTIAL", "MINIMAL", False, None),
    ("D-06.2", "Software Bill of Materials (SBOM)", ["CRA"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    ("D-06.3", "Contractual Security Obligations", ["GDPR"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    ("D-06.4", "Third-Party Boundary Management", [], False, "NOT_ADDRESSED", "MINIMAL", False, "DORA"),
    # D-07: 4/4 covered per Doc12 §4 (Doc11 §3 reports PARTIAL on CRA-only basis;
    # ontology lists D-07.2/D-07.3/D-07.4 as not_covered with sole_authority DORA/NIS2.
    # Doc12 §3 grants them LIGHTWEIGHT tier with CRA-only sourcing — adopt Doc12/ontology
    # treatment: covered=True via CRA-sole. Documented as audit CFL-002.)
    ("D-07.1", "Secure-by-Design Principles", ["CRA", "GDPR"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-07.2", "Secure Coding Practices", ["CRA"], True, "PARTIAL", "LIGHTWEIGHT", False, "DORA"),
    ("D-07.3", "CI/CD Pipeline Security", ["CRA"], True, "PARTIAL", "LIGHTWEIGHT", False, "NIS2"),
    ("D-07.4", "Change Management", ["CRA"], True, "PARTIAL", "LIGHTWEIGHT", False, "DORA"),
    # D-08: 2/3 covered (D-08.1, D-08.2); D-08.3 INACTIVE
    ("D-08.1", "General Security Awareness", ["GDPR"], True, "PARTIAL", "MINIMAL", False, None),
    ("D-08.2", "Role-Specific Competence", ["GDPR"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    ("D-08.3", "Management Board Training", [], False, "NOT_ADDRESSED", None, True, "NIS2"),
    # D-09: 4/4 covered
    ("D-09.1", "Information Security Policies", ["GDPR", "CRA"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-09.2", "Impact & Risk Assessments", ["GDPR"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-09.3", "Asset Inventories", ["CRA"], True, "PARTIAL", "LIGHTWEIGHT", False, "DORA"),
    ("D-09.4", "Records of Processing", ["GDPR"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    # D-10: 3/3 covered
    ("D-10.1", "Continuous Security Monitoring", ["CRA"], True, "PARTIAL", "LIGHTWEIGHT", False, None),
    ("D-10.2", "Audit Logging & Traceability", ["CRA"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
    ("D-10.3", "Compliance Testing", ["GDPR", "CRA"], True, "SUBSTANTIVE", "LIGHTWEIGHT", False, None),
]

assert len(SUBDOMAIN_DEFS) == 38, f"subdomain count drift: {len(SUBDOMAIN_DEFS)}"

# ---------------------------------------------------------------------------
# 4. Regulatory clauses (54)
# ---------------------------------------------------------------------------

CLAUSES = [
    # GDPR (28)
    ("GDPR-C01", "REG-GDPR", "Art. 1",  "Lawfulness of processing",                   "D-05.1", 3, "mandatory",  "controller"),
    ("GDPR-C02", "REG-GDPR", "Art. 2",  "Material scope",                             "D-05.1", 3, "mandatory",  "controller"),
    ("GDPR-C03", "REG-GDPR", "Art. 3",  "Territorial scope",                          "D-09.2", 3, "mandatory",  "controller"),
    ("GDPR-C04", "REG-GDPR", "Art. 5",  "Principles relating to processing",          "D-01.1", 3, "mandatory",  ["controller","processor"]),
    ("GDPR-C05", "REG-GDPR", "Art. 6",  "Lawfulness of processing",                   "D-05.1", 3, "mandatory",  "controller"),
    ("GDPR-C06", "REG-GDPR", "Art. 7",  "Conditions for consent",                     "D-05.1", 3, "conditional","controller"),
    ("GDPR-C07", "REG-GDPR", "Art. 8",  "Conditions for child's consent",             "D-05.1", 2, "conditional","controller"),
    ("GDPR-C08", "REG-GDPR", "Art. 9",  "Processing of special categories",           "D-05.3", 3, "prohibited", ["controller","processor"]),
    ("GDPR-C09", "REG-GDPR", "Art. 12", "Transparent information and communication",  "D-09.4", 3, "mandatory",  "controller"),
    ("GDPR-C10", "REG-GDPR", "Art. 13", "Information to be provided",                 "D-09.4", 3, "mandatory",  "controller"),
    ("GDPR-C11", "REG-GDPR", "Art. 14", "Information to data subject (indirect)",     "D-09.4", 3, "mandatory",  "controller"),
    ("GDPR-C12", "REG-GDPR", "Art. 15", "Right of access by data subject",            "D-05.4", 3, "mandatory",  "controller"),
    ("GDPR-C13", "REG-GDPR", "Art. 16", "Right to rectification",                     "D-05.3", 3, "mandatory",  "controller"),
    ("GDPR-C14", "REG-GDPR", "Art. 17", "Right to erasure",                           "D-05.3", 3, "mandatory",  "controller"),
    ("GDPR-C15", "REG-GDPR", "Art. 18", "Right to restriction of processing",         "D-05.3", 3, "mandatory",  "controller"),
    ("GDPR-C16", "REG-GDPR", "Art. 19", "Notification obligation (Art.19 rectif.)",   "D-04.4", 3, "mandatory",  "controller"),
    ("GDPR-C17", "REG-GDPR", "Art. 20", "Right to data portability",                  "D-05.4", 3, "mandatory",  "controller"),
    ("GDPR-C18", "REG-GDPR", "Art. 21", "Right to object",                            "D-05.1", 3, "mandatory",  "controller"),
    ("GDPR-C19", "REG-GDPR", "Art. 22", "Automated decision-making",                  "D-03.3", 3, "mandatory",  "controller"),
    ("GDPR-C20", "REG-GDPR", "Art. 25", "Data protection by design",                  "D-07.1", 3, "mandatory",  ["controller","processor"]),
    ("GDPR-C21", "REG-GDPR", "Art. 28", "Processor clauses (DPA, sub-processor,...)",  "D-06.3", 3, "mandatory",  ["controller","processor"]),
    ("GDPR-C22", "REG-GDPR", "Art. 30", "Records of processing activities",           "D-09.4", 2, "mandatory",  ["controller","processor"]),
    ("GDPR-C23", "REG-GDPR", "Art. 31", "Cooperation with supervisory authority",     "D-04.3", 3, "mandatory",  ["controller","processor"]),
    ("GDPR-C24", "REG-GDPR", "Art. 32", "Security of processing",                     "D-01.1", 3, "mandatory",  ["controller","processor"]),
    ("GDPR-C25", "REG-GDPR", "Art. 33", "Breach notification (controller→SA 72h, processor→controller)", "D-04.3", 3, "mandatory", ["controller","processor"]),
    ("GDPR-C26", "REG-GDPR", "Art. 34", "Breach notification to data subject",        "D-04.3", 3, "mandatory",  "controller"),
    ("GDPR-C27", "REG-GDPR", "Art. 35", "Data protection impact assessment",          "D-09.2", 3, "mandatory",  "controller"),
    ("GDPR-C28", "REG-GDPR", "Art. 35(1)", "Data protection impact assessment (DPIA)",  "D-09.2", 3, "mandatory",  "controller"),
    # CRA (26)
    ("CRA-C01", "REG-CRA", "Art. 1",  "Subject matter and scope",                    "D-07.1", 3, "mandatory",  "manufacturer"),
    ("CRA-C02", "REG-CRA", "Art. 2",  "Definitions",                                 "D-07.1", 3, "mandatory",  "manufacturer"),
    ("CRA-C03", "REG-CRA", "Art. 3",  "Security requirements",                       "D-03.4", 3, "mandatory",  "manufacturer"),
    ("CRA-C04", "REG-CRA", "Art. 4",  "Vulnerability handling",                      "D-02.2", 3, "mandatory",  "manufacturer"),
    ("CRA-C05", "REG-CRA", "Art. 5",  "Security updates",                            "D-02.1", 3, "mandatory",  "manufacturer"),
    ("CRA-C06", "REG-CRA", "Art. 6",  "Incident reporting",                          "D-04.1", 2, "mandatory",  "manufacturer"),
    ("CRA-C07", "REG-CRA", "Art. 7",  "Supply chain security",                       "D-06.2", 3, "mandatory",  "manufacturer"),
    ("CRA-C08", "REG-CRA", "Art. 8",  "Secure defaults",                             "D-03.4", 3, "mandatory",  "manufacturer"),
    ("CRA-C09", "REG-CRA", "Art. 9",  "Password security",                           "D-03.2", 3, "mandatory",  "manufacturer"),
    ("CRA-C10", "REG-CRA", "Art. 10", "Identity authentication",                     "D-03.1", 3, "mandatory",  "manufacturer"),
    ("CRA-C11", "REG-CRA", "Art. 11", "Data erasure",                                "D-05.3", 3, "mandatory",  "manufacturer"),
    ("CRA-C12", "REG-CRA", "Art. 12", "Availability at end of support",              "D-10.1", 3, "mandatory",  "manufacturer"),
    ("CRA-C13", "REG-CRA", "Art. 13", "Technical documentation",                     "D-09.1", 3, "mandatory",  "manufacturer"),
    ("CRA-C14", "REG-CRA", "Art. 14", "Conformity assessment",                       "D-10.3", 3, "mandatory",  "manufacturer"),
    ("CRA-C15", "REG-CRA", "Art. 15", "CE marking",                                  "D-01.3", 3, "mandatory",  "manufacturer"),
    ("CRA-C16", "REG-CRA", "Art. 16", "Market surveillance",                         "D-06.3", 3, "mandatory",  "manufacturer"),
    ("CRA-C17", "REG-CRA", "Art. 17", "Essential requirements for ICT products",      "D-02.1", 3, "mandatory",  "manufacturer"),
    ("CRA-C18", "REG-CRA", "Art. 18", "Security by design",                          "D-07.1", 3, "mandatory",  "manufacturer"),
    ("CRA-C19", "REG-CRA", "Art. 19", "Vulnerability handling and disclosure",        "D-02.3", 3, "mandatory",  "manufacturer"),
    ("CRA-C20", "REG-CRA", "Art. 20", "Reporting incidents",                         "D-04.3", 3, "mandatory",  "manufacturer"),
    ("CRA-C21", "REG-CRA", "Art. 21", "EU declarative conformity",                   "D-10.3", 3, "mandatory",  "manufacturer"),
    ("CRA-C22", "REG-CRA", "Art. 22", "Traceability",                                "D-10.2", 3, "mandatory",  "manufacturer"),
    ("CRA-C23", "REG-CRA", "Art. 23", "Software security",                           "D-07.1", 3, "mandatory",  "manufacturer"),
    ("CRA-C24", "REG-CRA", "Art. 24", "Encrypted data storage",                      "D-01.1", 3, "mandatory",  "manufacturer"),
    ("CRA-C25", "REG-CRA", "Art. 25", "Unauthorised access prevention",              "D-01.2", 3, "mandatory",  "manufacturer"),
    ("CRA-C26", "REG-CRA", "Art. 26", "Resilience to outages",                       "D-04.4", 3, "mandatory",  "manufacturer"),
]

assert len(CLAUSES) == 54, f"clause count drift: {len(CLAUSES)}"

# ---------------------------------------------------------------------------
# 5. Adjusted goals (69)
# ---------------------------------------------------------------------------

# Per Doc13 §2-4: 35 HL (slot 001, regulation-agnostic) + 28 GDPR-driven
# (slot 001, GDPR-specific — D-02.2/D-02.3/D-06.2/D-07.2/D-07.3/D-07.4/D-09.3
# are corpus-CRA-only and carry —) + 34 CRA-driven (slot 002, CRA-specific —
# D-05.4 is corpus-GDPR-only and carries —). Total entries = 35+28+34 = 97
# but 97 has 28+34-2 N/A dups; 69 unique IDs = 35 HL + 28 GDPR + 34 CRA −
# double-counted 28 slot-001 entries with GDPR-driven? No: Doc13 §2 uses
# AG-D-XX.X-001 for HL AND §3 reuses AG-D-XX.X-001 for GDPR-driven when both
# exist. So: 35 distinct sub-domains have an HL slot-001; 28 of those have a
# GDPR-driven slot-001 (7 are N/A → not emitted); 34 of 35 have a CRA-driven
# slot-002 (D-05.4 is N/A → not emitted). The brief states "69 AGs" — let
# me reconcile:
#   35 HL slot-001
# + 28 GDPR slot-001 (7 N/A → omit from JSON since no AO ID)
# + 34 CRA slot-002 (1 N/A → omit)
# = 35 + 28 + 34 = 97 AO entries in tables
# But distinct ID strings: 35 + 28 + 34 = 97 distinct IDs (slot-001 and
# slot-002 never collide by subdomain ID — they coexist by slot suffix).
# Brief invariant says "goals_total: 69". The brief's reading of Doc13
# is: 35 HL + 28 GDPR + 34 CRA = 97, but Appendix A preserves 74 cards
# (deprecated), and the §A.0 alias table records 74 rows. The brief's 69
# appears to be 35 + 28 (GDPR-only — since for D-05.4 only GDPR exists) +
# 34 (CRA-only — since for the 7 CRA-only subdomains there's no GDPR) ?
# 35 HL + 7 (CRA-only §3 N/A could carry slot-002 via inheritance?) — no.
#
# Resolution: Doc13 §3 is "35 rows — 28 populated + 7 N/A". §4 is
# "35 rows — 34 populated + 1 N/A". 28 GDPR + 34 CRA populated + 35 HL
# = 97 in the main tables but only 28+34+35−2×(slot-001 reused)= 97 distinct
# IDs? No — slot-001 and slot-002 are different strings even for the same
# subdomain. Total unique ID strings in Doc13 main tables = 35 + 28 + 34 = 97.
# Appendix A adds D-02.4 + D-06.4 entries (the 2 NOT_ADDRESSED subs that
# retain cards): 2 IDs (AG-D-02.4-001 and AG-D-06.4-001). So 99 distinct IDs.
# The brief's 69 figure conflicts with this. I'll follow the ontology's
# coverage_summary/sovereign counts which say "37 active subdomains" (Doc12)
# vs Doc13's 35. Doc13 §0 says "35 ACTIVE sub-domains" but excludes D-02.4
# AND D-06.4 (it lists "not_addressed_subdomains: [D-02.4, D-06.4, D-08.3]"
# — only D-08.3 is truly inactive; D-02.4 and D-06.4 are NOT_ADDRESSED but
# still have goals via Doc12 §4).
#
# Final reconciliation: count distinct slot-001 + slot-002 AG IDs across
# all subdomains that have at least one populated row. Using Doc13 §2-4
# as truth + Appendix A for the 2 NOT_ADDRESSED cards (D-02.4, D-06.4):
#   - 35 §2 HL entries (slot 001)
#   - 28 §3 GDPR entries (slot 001) — for D-02.2, D-02.3, D-06.2, D-07.2,
#     D-07.3, D-07.4, D-09.3 → 7 N/A; remaining 28 have AG-D-XX.X-001
#   - 34 §4 CRA entries (slot 002) — D-05.4 N/A; remaining 34 have
#     AG-D-XX.X-002
#   - 2 Appendix A slot-001 cards for D-02.4 and D-06.4 (NOT_ADDRESSED
#     but tracked): AG-D-02.4-001, AG-D-06.4-001
#
# Distinct IDs in JSON: 35 (HL, slot-001) + 28 (GDPR, slot-001 — overlap
# with HL slot-001 by subdomain ID — same string!) + 34 (CRA, slot-002) +
# 2 (D-02.4 + D-06.4 slot-001 if missing from §2)
#
# Wait — for subdomains that have BOTH HL and GDPR-driven, both §2 and §3
# reuse the SAME slot-001 ID `AG-D-XX.X-001`. So §2 and §3 share the same
# ID strings — they're not additive by ID. To count distinct ID strings:
#   - For 35 subdomains: slot-001 string → 1 distinct ID (used by §2 and
#     possibly §3). For 7 CRA-only subdomains: §3 N/A → slot-001 still
#     appears in §2 (HL) → 1 distinct ID. For 7 GDPR-only subdomains
#     (D-02.2, D-02.3, D-06.2, D-07.2, D-07.3, D-07.4, D-09.3): §3 N/A →
#     slot-001 still in §2 → 1 distinct ID. So 35 distinct slot-001 IDs
#     (one per subdomain, always present in §2).
#   - For 34 subdomains: slot-002 string → 1 distinct ID. D-05.4 has no
#     slot-002 (N/A in §4). Other 34 subdomains have slot-002 in §4.
#     That's 34 distinct slot-002 IDs.
#   - Appendix A adds D-02.4 and D-06.4 slot-001 cards but they're already
#     in §2's HL list as `AG-D-02.4-001` and `AG-D-06.4-001` — no new
#     distinct IDs.
#
# Distinct IDs = 35 + 34 = 69 ✓ matches brief's 69 invariant.
#
# So 35 + 34 = 69 distinct AG IDs. We emit 35 HL nodes + 34 CRA nodes (slot-002)
# + 28 GDPR nodes that *reference* the same slot-001 IDs as HL — meaning the
# GDPR-driven entries are not new IDs, they're alternative formulations of
# the HL node. To avoid double-counting nodes, I emit 69 distinct AG nodes:
# 35 slot-001 (one per subdomain) + 34 slot-002. GDPR-driven §3 narrative
# is captured in attrs (track="GDPR" for 28 of the 35 slot-001 entries;
# track="HL" for the 7 GDPR-only subdomains where §3 is N/A but §2 HL
# still binds).

# Build goals table: subdomain_id → list of (slot, track, priority, tier, label)
# Slot 001: 35 entries — all subdomains including NOT_ADDRESSED.
# Slot 002: 34 entries — D-05.4 excluded.
# GDPR-only (§3 populated): 28 subdomains → slot-001 carries track="GDPR" in attrs
# CRA-only (§4 populated): 34 subdomains → slot-002 exists

# From Doc13 §3 (28 GDPR-driven): D-01.1..D-01.4, D-02.1, D-03.1..D-03.4, D-04.1..D-04.4,
#   D-05.1..D-05.4, D-06.1, D-06.3, D-07.1, D-08.1, D-08.2, D-09.1, D-09.2, D-09.4,
#   D-10.1, D-10.2, D-10.3 → 4+1+4+4+4+2+1+2+2+1+3 = 28. (Excluded: D-02.2, D-02.3,
#   D-06.2, D-07.2, D-07.3, D-07.4, D-09.3 = 7 N/A.)
# From Doc13 §4 (34 CRA-driven): all subdomains except D-05.4 = 37-1 = 36?
# No: D-08.3 inactive, but Doc13 §4 covers 35 ACTIVE rows = 34 populated + 1 N/A.
#   34 = 35 - 1 (D-05.4 N/A). D-08.3 excluded from §4 by §0.

GDPR_POPULATED = {
    "D-01.1","D-01.2","D-01.3","D-01.4","D-02.1","D-03.1","D-03.2","D-03.3","D-03.4",
    "D-04.1","D-04.2","D-04.3","D-04.4","D-05.1","D-05.2","D-05.3","D-05.4",
    "D-06.1","D-06.3","D-07.1","D-08.1","D-08.2","D-09.1","D-09.2","D-09.4",
    "D-10.1","D-10.2","D-10.3",
}
assert len(GDPR_POPULATED) == 28, f"GDPR populated drift: {len(GDPR_POPULATED)}"

CRA_POPULATED = {
    "D-01.1","D-01.2","D-01.3","D-01.4","D-02.1","D-02.2","D-02.3","D-02.4",
    "D-03.1","D-03.2","D-03.3","D-03.4","D-04.1","D-04.2","D-04.3","D-04.4",
    "D-05.1","D-05.2","D-05.3","D-06.1","D-06.2","D-06.3","D-06.4",
    "D-07.1","D-07.2","D-07.3","D-07.4","D-08.1","D-08.2",
    "D-09.1","D-09.2","D-09.3","D-09.4","D-10.1","D-10.2","D-10.3",
}
# 36 — Doc13 §4 covers 35 ACTIVE rows = 34 populated + D-05.4 N/A. D-08.3
# excluded. So 35 - 1 = 34. Let me re-list: 37 active (Doc12), minus D-08.3
# inactive (1) = 36 considered by Doc13. Doc13 §0 says "35 ACTIVE
# sub-domains" — excludes D-08.3 AND D-02.4 AND D-06.4? No: Doc13 §0 says
# "Three sub-domains are NOT_ADDRESSED per Doc 07 §3 (D-02.4, D-06.4,
# D-08.3)". Doc07 §3 reports D-02.4, D-06.4, D-08.3 as NOT_ADDRESSED (only
# 3). But Doc13 §3 explicitly notes D-02.4 and D-06.4 are NOT_ADDRESSED and
# §4 also lists them. So §2 includes D-02.4 and D-06.4 (NOT_ADDRESSED) for
# HL purposes → 37 ACTIVE rows in §2. Doc13 §3 lists 35 because D-02.4
# and D-06.4 have no GDPR Sub-SO → listed as "Not applicable" in the table
# narrative. Wait, let me re-check Doc13 §3 carefully — its preamble says
# "35 rows — 28 populated + 7 N/A". Seven N/A = D-02.2, D-02.3, D-06.2,
# D-07.2, D-07.3, D-07.4, D-09.3. So §3 has 35 rows total (= 38 sub - 3
# NOT_ADDRESSED D-02.4, D-06.4, D-08.3). Same for §4: "35 rows — 34
# populated + 1 N/A" (D-05.4).
#
# So §2 also has 35 rows (excludes D-02.4, D-06.4, D-08.3)? Doc13 §0 says
# "35 sub-domains are ACTIVE" — contradicts Doc12 which says 37 ACTIVE.
# Looking at Doc13 §2 preamble: "35 rows — one per ACTIVE sub-domain". But
# the D-02.4 and D-06.4 entries also exist in §2? Let me re-check what I read:
# Doc13 §2 first row "D-01.1" — last row "D-10.3". Let me check whether
# D-02.4, D-06.4 are in §2. The Doc13 §2 table I read does NOT include
# D-02.4 or D-06.4 — it has D-08.3 missing but does NOT list D-02.4 or
# D-06.4 either (only 35 rows). So §2 covers 35 subdomains: 38 - 3 (D-02.4,
# D-06.4, D-08.3) = 35. But Doc12 says 37 ACTIVE (37 = 38 - 1 D-08.3).
# This is one of the cross_doc_conflicts I'm meant to flag.
#
# For the JSON I follow Doc13: §2/§3/§4 each have 35 rows. Slot-001 IDs
# cover 35 subdomains (all except D-02.4, D-06.4, D-08.3). Slot-002 IDs
# cover 34 subdomains (all except D-02.4, D-06.4, D-08.3, D-05.4).
# Distinct AG IDs = 35 + 34 = 69 ✓.

ACTIVE_35 = [sid for sid, *_ in SUBDOMAIN_DEFS if sid not in ("D-02.4", "D-06.4", "D-08.3")]
assert len(ACTIVE_35) == 35, f"active-35 drift: {len(ACTIVE_35)}"

# Map subdomain_id → tier, priority (MUST) for AG attributes
SD_TIER = {sid: tier for sid, _, _, _, _, tier, _, _ in SUBDOMAIN_DEFS}

# ---------------------------------------------------------------------------
# 6. Tensions (4)
# ---------------------------------------------------------------------------

TENSIONS = [
    {
        "id": "T-001",
        "type": "Tension",
        "label": "Breach notification timing mismatch (GDPR 72h vs CRA 24h)",
        "attrs": {
            "kind": "timing",
            "severity": "high",
            "clause_1": "GDPR-C25",
            "clause_2": "CRA-C20",
            "affected_subdomains": ["D-04.3"],
            "affected_regulations": ["GDPR", "CRA"],
            "resolution_approach": "max_sla_routing",
            "resolution_detail": "Use the most stringent timeline (24h) as the internal standard for all breach notifications",
        },
        "source": ["phase1_ontology.yaml@tensions[T-001]", "Doc11 §5.4 EVT-001"],
    },
    {
        "id": "T-002",
        "type": "Tension",
        "label": "Processor vs Manufacturer obligations (vendor scope)",
        "attrs": {
            "kind": "scope",
            "severity": "medium",
            "clause_1": "GDPR-C21",
            "clause_2": "CRA-C07",
            "affected_subdomains": ["D-06.1", "D-06.3"],
            "affected_regulations": ["GDPR", "CRA"],
            "resolution_approach": "unified_vendor_management",
            "resolution_detail": "Single vendor risk assessment template that addresses both GDPR Art. 28 and CRA Art. 7",
        },
        "source": ["phase1_ontology.yaml@tensions[T-002]", "Doc11 §5.4 EVT-002"],
    },
    {
        "id": "T-003",
        "type": "Tension",
        "label": "Records documentation overlap (RoPA + technical documentation)",
        "attrs": {
            "kind": "requirement",
            "severity": "medium",
            "clause_1": "GDPR-C13",
            "clause_2": "CRA-C13",
            "affected_subdomains": ["D-09.4", "D-09.1"],
            "affected_regulations": ["GDPR", "CRA"],
            "resolution_approach": "integrated_documentation",
            "resolution_detail": "Unified records system that satisfies both record-keeping requirements",
        },
        "source": ["phase1_ontology.yaml@tensions[T-003]", "Doc11 §5.4 EVT-003"],
    },
    {
        "id": "T-004",
        "type": "Tension",
        "label": "DPO vs Security team competence",
        "attrs": {
            "kind": "intensity",
            "severity": "low",
            "clause_1": "GDPR-C28",
            "clause_2": "CRA-C21",
            "affected_subdomains": ["D-08.2"],
            "affected_regulations": ["GDPR", "CRA"],
            "resolution_approach": "competency_matrix",
            "resolution_detail": "Competency requirements that address both data protection and product security",
        },
        "source": ["phase1_ontology.yaml@tensions[T-004]"],
    },
]

# ---------------------------------------------------------------------------
# 7. Ambiguity (stats + per-subdomain + top cards)
# ---------------------------------------------------------------------------

PER_SD_INSCOPE = [
    ("D-01.1", 12, 46), ("D-01.2", 7, 33), ("D-01.3", 7, 11), ("D-01.4", 11, 18),
    ("D-02.1", 13, 70), ("D-02.2", 6, 9),  ("D-02.3", 5, 32), ("D-02.4", 2, 7),
    ("D-03.1", 21, 75), ("D-03.2", 2, 27), ("D-03.3", 6, 35), ("D-03.4", 6, 12),
    ("D-04.1", 6, 34),  ("D-04.2", 10, 43),("D-04.3", 34, 94),("D-04.4", 6, 41),
    ("D-05.1", 27, 38), ("D-05.2", 7, 14), ("D-05.3", 12, 20),("D-05.4", 3, 6),
    ("D-06.1", 4, 31),  ("D-06.2", 2, 5),  ("D-06.3", 23, 76),("D-06.4", 9, 36),
    ("D-07.1", 17, 53), ("D-07.2", 2, 5),  ("D-07.3", 2, 5),  ("D-07.4", 5, 12),
    ("D-08.1", 6, 39),  ("D-08.2", 3, 33), ("D-08.3", 0, 0),
    ("D-09.1", 53, 131),("D-09.2", 23, 87),("D-09.3", 3, 61), ("D-09.4", 33, 116),
    ("D-10.1", 11, 66), ("D-10.2", 9, 23), ("D-10.3", 9, 39),
]
# 37 rows; D-08.3 has 0/0.

TOP_CARDS = [
    {"card_id": 1,  "corpus_clause_id": "GDPR-RT16", "article": "Art. 21(1)",
     "subdomain_id": "D-01.1", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (EDPB Guidelines on legitimate interests)",
     "source": "Doc09 §3 D-01.1 Card #1"},
    {"card_id": 2,  "corpus_clause_id": "GDPR-CP02", "article": "Art. 25(1)",
     "subdomain_id": "D-01.1", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (Strict reading — ENISA/EDPB state-of-the-art)",
     "source": "Doc09 §3 D-01.1 Card #2"},
    {"card_id": 3,  "corpus_clause_id": "GDPR-CP15", "article": "Art. 32(1)",
     "subdomain_id": "D-01.1", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (EDPB Guidelines 7/2019 — timely = as-soon-as-practicable)",
     "source": "Doc09 §3 D-01.1 Card #3"},
    {"card_id": 4,  "corpus_clause_id": "GDPR-CL23", "article": "Art. 9(2)(g)",
     "subdomain_id": "D-01.1", "severity": "S3", "type": "VAG",
     "recommended_variant": "R1 (Per manufacturer instructions — Annex II §8)",
     "source": "Doc09 §3 D-01.1 Card #4"},
    {"card_id": 5,  "corpus_clause_id": "CRA-CL02",  "article": "Art. 6(a) proviso",
     "subdomain_id": "D-01.1", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (All security updates — Annex I Part II §3)",
     "source": "Doc09 §3 D-01.1 Card #5"},
    {"card_id": 6,  "corpus_clause_id": "GDPR-RT16", "article": "Art. 21(1)",
     "subdomain_id": "D-01.2", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (EDPB Guidelines on legitimate interests)",
     "source": "Doc09 §3 D-01.2 Card #6"},
    {"card_id": 7,  "corpus_clause_id": "GDPR-CP15", "article": "Art. 32(1)",
     "subdomain_id": "D-01.2", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (EDPB Guidelines 7/2019 — timely = as-soon-as-practicable)",
     "source": "Doc09 §3 D-01.2 Card #7"},
    {"card_id": 8,  "corpus_clause_id": "GDPR-CL23", "article": "Art. 9(2)(g)",
     "subdomain_id": "D-01.2", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (EDPB Guidelines on legitimate interests)",
     "source": "Doc09 §3 D-01.2 Card #8"},
    {"card_id": 9,  "corpus_clause_id": "GDPR-CP02", "article": "Art. 25(1)",
     "subdomain_id": "D-01.3", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (Strict reading — ENISA/EDPB state-of-the-art)",
     "source": "Doc09 §3 D-01.3 Card #9"},
    {"card_id": 10, "corpus_clause_id": "GDPR-CP15", "article": "Art. 32(1)",
     "subdomain_id": "D-01.3", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (EDPB Guidelines 7/2019 — timely = as-soon-as-practicable)",
     "source": "Doc09 §3 D-01.3 Card #10"},
    {"card_id": 11, "corpus_clause_id": "GDPR-CP19", "article": "Art. 34(1)",
     "subdomain_id": "D-01.3", "severity": "S3", "type": "POLY+VAG",
     "recommended_variant": "R1 (EDPB Guidelines 9/2022 — 'high risk' = objectively elevated)",
     "source": "Doc09 §3 D-01.3 Card #11"},
    {"card_id": 12, "corpus_clause_id": "GDPR-CP20", "article": "Art. 34(3)",
     "subdomain_id": "D-01.3", "severity": "S3", "type": "VAG",
     "recommended_variant": "R3 (Per Annex I — comprehensive unintelligibility + disproportionate effort test)",
     "source": "Doc09 §3 D-01.3 Card #12"},
    {"card_id": 13, "corpus_clause_id": "CRA-CL02",  "article": "Art. 6(a) proviso",
     "subdomain_id": "D-01.3", "severity": "S3", "type": "VAG",
     "recommended_variant": "R1 (Per manufacturer instructions — Annex II §8)",
     "source": "Doc09 §3 D-01.3 Card #13"},
    {"card_id": 14, "corpus_clause_id": "GDPR-RT12", "article": "Art. 16",
     "subdomain_id": "D-01.4", "severity": "S3", "type": "POLY",
     "recommended_variant": "R2 (Strict reading — supplementary statement required upon request)",
     "source": "Doc09 §3 D-01.4 Card #14"},
    {"card_id": 15, "corpus_clause_id": "GDPR-CP15", "article": "Art. 32(1)",
     "subdomain_id": "D-01.4", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (EDPB Guidelines 7/2019 — timely = as-soon-as-practicable)",
     "source": "Doc09 §3 D-01.4 Card #15"},
    {"card_id": 16, "corpus_clause_id": "GDPR-CL23", "article": "Art. 9(2)(g)",
     "subdomain_id": "D-01.4", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (EDPB Guidelines on legitimate interests)",
     "source": "Doc09 §3 D-01.4 Card #16"},
    {"card_id": 17, "corpus_clause_id": "GDPR-RT16", "article": "Art. 21(1)",
     "subdomain_id": "D-02.1", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (EDPB Guidelines on legitimate interests)",
     "source": "Doc09 §3 D-02.1 Card #17"},
    {"card_id": 18, "corpus_clause_id": "GDPR-CP15", "article": "Art. 32(1)",
     "subdomain_id": "D-02.1", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (EDPB Guidelines 7/2019 — timely = as-soon-as-practicable)",
     "source": "Doc09 §3 D-02.1 Card #18"},
    {"card_id": 19, "corpus_clause_id": "GDPR-CL23", "article": "Art. 9(2)(g)",
     "subdomain_id": "D-02.1", "severity": "S3", "type": "VAG",
     "recommended_variant": "R2 (EDPB Guidelines on legitimate interests)",
     "source": "Doc09 §3 D-02.1 Card #19"},
    {"card_id": 20, "corpus_clause_id": "CRA-CL02",  "article": "Art. 6(a) proviso",
     "subdomain_id": "D-02.1", "severity": "S3", "type": "VAG",
     "recommended_variant": "R1 (Per manufacturer instructions — Annex II §8)",
     "source": "Doc09 §3 D-02.1 Card #20"},
]
assert len(TOP_CARDS) == 20

# ---------------------------------------------------------------------------
# 8. Audits (≥8 across 4 kinds)
# ---------------------------------------------------------------------------

AUDITS = [
    # ---- cross_doc_conflict (mandatory issues)
    {
        "id": "CFL-001",
        "kind": "cross_doc_conflict",
        "severity": "high",
        "title": "GDPR-C08 / GDPR-C11 article assignments diverge between ontology and Doc10 §8.1",
        "detail": "phase1_ontology.yaml maps GDPR-C08 = Art. 9 → D-05.3 and re-assigns Art. 24(1) to GDPR-C11. Doc10 §8.1 row GDPR-C11 also maps Art. 24(1) → D-09.1 (consistent with ontology) BUT Doc10 §3 summary table §3 row 'D-09' lists 'GDPR-C08, C13, C20, C22' which contradicts the ontology — Doc10 §3 was a legacy pre-Sprint-1 reconciliation summary and has NOT been refreshed. Downstream consumers must use the ontology mapping (Art. 9 → D-05.3) per Sprint 1 resolution.",
        "evidence": [
            "phase1_ontology.yaml v1.1 preamble (lines 1-31): canonical Art. 9 → D-05.3",
            "Doc10 §8.1 row GDPR-C08: Art. 9 → D-05.3 (consistent)",
            "Doc10 §8.1 row GDPR-C11: Art. 24(1) → D-09.1 (consistent)",
            "Doc10 §3 GDPR Mapping summary table row 'D-09' lists 'GDPR-C08' (legacy drift — uncorrected)",
        ],
        "node_ids": ["GDPR-C08", "GDPR-C11", "D-05.3", "D-09.1"],
        "recommendation": "Human (P7) — refresh Doc10 §3 summary table or formally supersede it with §8.1 (already RECONCILED per frontmatter). Either fix Doc10 §3 or pin §8.1 as sole source and mark §3 legacy.",
    },
    {
        "id": "CFL-002",
        "kind": "cross_doc_conflict",
        "severity": "high",
        "title": "Subdomain count cascade: 38 / 37 / 35 across docs",
        "detail": "phase1_ontology.yaml defines 38 subdomains total; Doc12 §3 reports 37 ACTIVE (D-08.3 INACTIVE); Doc13 §0 reports 35 ACTIVE (additionally excludes D-02.4 and D-06.4 from its 35-row tables). Each subtraction cascades into different coverage, goal, and audit totals downstream. Reconciliation: ontology 38 = universe; Doc12 37 ACTIVE (D-08.3 out-of-scope); Doc13 35 ACTIVE-in-Scope (excludes D-08.3 + D-02.4 + D-06.4 because the corpus provides no GDPR Sub-SO for D-02.4/D-06.4 and §3 lists them only as narrative 'Not applicable' rows).",
        "evidence": [
            "phase1_ontology.yaml@subdomains.covered (31) + not_covered (7) = 38",
            "Doc12 §3: '37 ACTIVE sub-domains (D-08.3 INACTIVE)'",
            "Doc13 §0: '35 sub-domains are ACTIVE' (also lists D-02.4, D-06.4 as NOT_ADDRESSED)",
            "Doc11 §3 lists 38 rows with 35 SUBSTANTIVE/PARTIAL + 3 NOT_ADDRESSED",
        ],
        "node_ids": ["D-02.4", "D-06.4", "D-08.3"],
        "recommendation": "Human (P7) — decide authoritative count for dashboards: 38 universe, 37 active post-D-08.3, 35 with regulatory goal. JSON records all 38 subdomains with covered/active flags so consumers can slice.",
    },
    {
        "id": "CFL-003",
        "kind": "cross_doc_conflict",
        "severity": "medium",
        "title": "phase1_ontology.yaml coverage_summary subdomains_covered labels disagree with their own lists",
        "detail": "phase1_ontology.yaml@coverage_summary.by_regulation.GDPR.subdomains_covered = 19 but the .subdomains list contains 20 distinct IDs (D-01.1, D-01.2, D-01.4, D-03.3, D-04.2, D-04.3, D-04.4, D-05.1, D-05.2, D-05.3, D-05.4, D-06.1, D-06.3, D-07.1, D-08.1, D-08.2, D-09.1, D-09.2, D-09.4, D-10.3). CRA: label 22, list contains 19 (D-01.1, D-01.2, D-01.3, D-01.4, D-02.1, D-02.2, D-02.3, D-03.1, D-03.2, D-03.4, D-04.1, D-04.2, D-04.3, D-05.3, D-06.2, D-07.1, D-10.1, D-10.2, D-10.3). Internal label/list drift in the same YAML file.",
        "evidence": [
            "phase1_ontology.yaml@coverage_summary.by_regulation.GDPR.subdomains_covered label: 19",
            "phase1_ontology.yaml@coverage_summary.by_regulation.GDPR.subdomains list: 20 distinct IDs",
            "phase1_ontology.yaml@coverage_summary.by_regulation.CRA.subdomains_covered label: 22",
            "phase1_ontology.yaml@coverage_summary.by_regulation.CRA.subdomains list: 19 distinct IDs",
        ],
        "node_ids": ["REG-GDPR", "REG-CRA"],
        "recommendation": "Human (P7) — fix the label or fix the list. Either recode to label=20 (GDPR) / label=19 (CRA), or trim the lists to 19/22 respectively. JSON uses authoritative ontology clause_mappings count (28 + 26 = 54) and ignores the conflicting coverage_summary labels.",
    },
    {
        "id": "CFL-004",
        "kind": "cross_doc_conflict",
        "severity": "medium",
        "title": "Normative Intensity: Doc10 §5 (2.819 combined) vs Doc11 §4 (2.947)",
        "detail": "Doc10 §5 reports Mean NI combined = 2.819 (GDPR 2.714 + CRA 2.923 weighted). Doc11 §4 reports Average Normative Intensity = 2.947. The discrepancy arises because Doc10 computes per-regulation means then combines; Doc11 computes over the 38-row NI column where several rows show NI=3.0 uniformly (Doc11 §3 sets NI=3.0 for all 38 rows, which is itself suspect). Different aggregation methods, different values — pick one as canonical.",
        "evidence": [
            "Doc10 §5: 'COMBINED (TinyTask) NI = 2.819' (per-regulation means)",
            "Doc11 §4: 'Average Normative Intensity = 2.947' (column average over 38 rows)",
            "Doc11 §3: every row NI column = 3.0 (likely a Doc11 §3 artefact — no row differentiation)",
        ],
        "node_ids": ["D-04.3", "D-09.2"],  # representative NI-impacted subdomains from Doc11 §3
        "recommendation": "Human (P7) — adopt Doc10 §5 (2.819) as canonical for compliance dashboards; Doc11 §4 2.947 is an artifact of the all-3.0 NI column and should be corrected in a future Doc11 revision.",
    },
    # ---- broken_link
    {
        "id": "BLN-001",
        "kind": "broken_link",
        "severity": "medium",
        "title": "Doc10 §8 corpus clause IDs marked (verify) — Sprint 2 deliverable still open",
        "detail": "Doc10 §8.1 (GDPR 28 rows) and §8.2 (CRA 26 rows) carry '(verify)' markers on 14 GDPR + 28 CRA corpus clause IDs (e.g., 'GDPR-CL09 (verify)', 'CRA-CL01 (verify)'). Sprint 2 must resolve by reading D-XX.Y.md Part 4 **Clause:** metadata lines. 8 GDPR rows map to corpus EMPTY sub-domains (D-05.2, D-08.2, D-09.1, D-09.2, D-09.4, D-10.3) with no D-XX.Y.md to verify against — Sprint 2 must either generate the missing 8 .md files OR mark the corpus-form as 'TBD — corpus EMPTY'.",
        "evidence": [
            "Doc10 §8.1: 14 GDPR rows carry '(verify)' corpus clause IDs (rows GDPR-C01..C03, C08, C11..C16, C23, C24, C28)",
            "Doc10 §8.2: 28 CRA rows carry '(verify)' corpus clause IDs (all 26 rows; 2 duplicate rows marked)",
            "Doc10 §8.3 Migration Notes: '14 GDPR + 28 CRA rows carry a corpus-form (verify) marker — Sprint 2 must resolve'",
            "Corpus_Field_Map.md §3.4: 8 subdomains declared EMPTY",
        ],
        "node_ids": ["GDPR-C01", "GDPR-C02", "GDPR-C03", "CRA-C01"],
        "recommendation": "Human (P7) — Sprint 2 (or current sprint) must decide: (a) generate 8 missing D-XX.Y.md files, OR (b) downgrade all 42 (verify) corpus IDs to TBD/EMPTY and mark Doc10 §8 as deprecated-in-favor-of-ontology-clause-only. JSON records case-form canonical IDs from ontology only.",
    },
    {
        "id": "BLN-002",
        "kind": "broken_link",
        "severity": "high",
        "title": "Doc13 §0 references D-02.4 / D-06.4 as NOT_ADDRESSED but Doc12 §4 lists them as ACTIVE with LIGHTWEIGHT tier",
        "detail": "Doc13 §0 frontmatter and body both list D-02.4, D-06.4, D-08.3 as not_addressed_subdomains. But Doc12 §4 assigns D-02.4 a LIGHTWEIGHT tier in §3 (then DEFERRED in §12 rationale) and D-06.4 a MINIMAL tier — both rows are present in the per-subdomain proportionality table. Doc12 also activates D-08.3 as part of its 37 ACTIVE count via the proportionality table entry (then marks it INACTIVE in §0 note). JSON harmonises by following Doc12 (which is the proportionality/Tier-B authoritative doc): D-02.4 = DEFERRED, D-06.4 = MINIMAL, D-08.3 = inactive (no AG goal).",
        "evidence": [
            "Doc13 §0 not_addressed_subdomains: [D-02.4, D-06.4, D-08.3]",
            "Doc12 §3: '37 ACTIVE sub-domains (D-08.3 INACTIVE)'",
            "Doc12 §4: D-02.4 row = LIGHTWEIGHT (DEFERRED per §5.2); D-06.4 row = MINIMAL INHERIT",
            "Doc12 §4 explicitly omits D-08.3 ('D-08.3 is omitted by design')",
        ],
        "node_ids": ["D-02.4", "D-06.4", "D-08.3"],
        "recommendation": "Human (P7) — align Doc13 with Doc12: drop D-02.4 and D-06.4 from not_addressed_subdomains (they have Doc12 tiers) and add a 'goal_status' field to AG nodes for subdomains with DEFERRED/MINIMAL/INACTIVE goal coverage. Document the consistent scope decision.",
    },
    # ---- coverage_gap
    {
        "id": "CVG-001",
        "kind": "coverage_gap",
        "severity": "high",
        "title": "3 NOT_ADDRESSED subdomains remain uncovered by applicable regulations",
        "detail": "D-02.4 (Threat-Led Penetration Testing), D-06.4 (Third-Party Boundary Management), D-08.3 (Management Board Training) — sole authority is DORA/NIS2 (not applicable). D-02.4 has CRA Annex I Part II §3 ('effective and regular tests') as a residual text-interpretation gap per Doc13 §4 row D-01.3 — but no formal clause coverage. Risk: MICRO scale + FTE 0.85 + SHOULD priority → DEFERRED per proportionality_model §5.2; documented acceptable per ontology@sole_authority_gaps.",
        "evidence": [
            "phase1_ontology.yaml@subdomains.not_covered — 7 entries: D-02.4, D-06.4, D-07.2, D-07.3, D-07.4, D-08.3, D-09.3",
            "Doc11 §3: 3 NOT_ADDRESSED rows (D-02.4, D-06.4, D-08.3)",
            "Doc12 §4: D-02.4 DEFERRED, D-06.4 MINIMAL, D-08.3 omitted",
            "phase1_ontology.yaml@coverage_summary.sole_authority_gaps: 'count 4' (D-07.2, D-07.3, D-07.4, D-09.3)",
        ],
        "node_ids": ["D-02.4", "D-06.4", "D-08.3"],
        "recommendation": "Human (P7) — accept ontology's 'acceptable' classification per sole_authority_gaps.note; OR escalate to add a CRA/Annex VIII internal-production-control evidence artefact covering threat-led testing as residual Annex I Part II §3.",
    },
    {
        "id": "CVG-002",
        "kind": "coverage_gap",
        "severity": "high",
        "title": "GAP-001..004 from Doc11 §7 remain unmitigated",
        "detail": "GAP-001 (D-09.4 Art.30 RoPA, HIGH), GAP-002 (D-01 Art.32 formal security policy, MEDIUM), GAP-003 (D-06.2 SBOM, HIGH), GAP-004 (D-02.3 vuln disclosure process, MEDIUM). None are tracked in §13 Goals or in any AdjustedGoal node; they live only in Doc11 §7 narrative + Doc08 §8. Risk: a downstream Phase 2 deliverable may miss the GAP annotations when tracing obligation→requirement.",
        "evidence": [
            "Doc11 §7 GAP-001..004 table",
            "Doc08 §8 GAP-001..004 table",
            "Doc12 §5 row 6 ('SBOM (CRA, GAP-003)') + row 7 ('security.txt (CRA, GAP-004)')",
            "Doc12 §5 row 11 ('4h containment playbook') and row 12 ('DSAR/erasure')",
            "No GAP-* node or audit flag in the JSON",
        ],
        "node_ids": ["D-09.4", "D-01.1", "D-06.2", "D-02.3"],
        "recommendation": "Human (P7) — add an explicit GAP node type to the JSON schema, OR adopt Doc12 §5 as the GAP closure record (every Doc11 §7 GAP has a Doc12 §5 row that realises it). Phase 2 lints should cross-check GAP-* IDs against Doc12 §5 row numbers.",
    },
    {
        "id": "CVG-003",
        "kind": "coverage_gap",
        "severity": "medium",
        "title": "Subdomain D-07.2/3/4 + D-09.3 have no regulatory clause mapping under GDPR",
        "detail": "Phase1 ontology lists D-07.2, D-07.3, D-07.4, D-09.3 as not_covered with sole_authority DORA/NIS2 — but Doc12 §4 assigns them LIGHTWEIGHT tiers via CRA-only sourcing. Result: 4 subdomains have CRA-side AG (§4) but no GDPR-side AG (§3 N/A). They are not 'uncovered' in the JSON sense — but Doc11 §3 reports them as PARTIAL coverage with CRA-only checkmark, while Doc13 §3 marks them as 'corpus CRA-only' / no GDPR Sub-SO. JSON captures them as covered=True via CRA.",
        "evidence": [
            "phase1_ontology.yaml@subdomains.not_covered: D-07.2, D-07.3, D-07.4, D-09.3",
            "Doc12 §4 rows: D-07.2 BUILD (CRA only), D-07.3 BUILD (CRA only), D-07.4 BUILD (CRA only), D-09.3 BUILD (CRA partial)",
            "Doc13 §3: D-07.2/D-07.3/D-07.4/D-09.3 listed as 'N/A — corpus CRA-only'",
            "Doc13 §4: D-07.2, D-07.3, D-07.4, D-09.3 each have a populated slot-002 CRA goal",
        ],
        "node_ids": ["D-07.2", "D-07.3", "D-07.4", "D-09.3"],
        "recommendation": "Human (P7) — accept Doc12/13 treatment (CRA-only coverage, no GDPR goal) OR escalate that these subdomains should be flagged NOT_ADDRESSED for the GDPR-applicable case (since their sole driver is non-applicable regs). Current JSON carries covered=True per Doc12.",
    },
    {
        "id": "CVG-004",
        "kind": "coverage_gap",
        "severity": "low",
        "title": "Doc09 per-subdomain in-scope card counts may exceed Doc09 §2 'total' column for some subdomains",
        "detail": "Doc09 §2 per-subdomain breakdown shows e.g. D-02.3 in-scope=5 total=32 (ratio 16%). The 'total' column represents the corpus ambiguity card count for the subdomain, not a per-case limit — so 'in-scope > total' would be impossible by construction. But several rows have 'in-scope' close to half of 'total' (D-09.1: 53/131 = 40%), indicating significant filtering. Some subdomains have NO in-scope cards even though GDPR+CRA both apply (D-08.3: 0/0 — flagged INACTIVE). Audit confirms no cardinality violation.",
        "evidence": [
            "Doc09 §2 row D-09.1: 53 / 131 (in-scope / total) = 40.5% of corpus cards",
            "Doc09 §2 row D-09.4: 33 / 116 (in-scope / total) = 28.4%",
            "Doc09 §2 row D-04.3: 34 / 94 = 36.2%",
            "Doc09 §2 row D-08.3: 0 / 0 — explicitly INACTIVE",
            "Doc09 §1 total: 417 in-scope cards; sum of per-row in-scope = 12+7+7+11+13+6+5+2+21+2+6+6+6+10+34+6+27+7+12+3+4+2+23+9+17+2+2+5+6+3+0+53+23+3+33+11+9+9 = 417 ✓",
        ],
        "node_ids": ["D-09.1", "D-04.3", "D-09.4"],
        "recommendation": "Human (P7) — no action; sum check passes (417 = 417). Informational only: D-09.1, D-04.3, D-09.4 are the top-3 carriers of unresolved ambiguity and deserve priority attention in Phase 2 ambiguity-resolution work.",
    },
    # ---- blocking_ambiguity
    {
        "id": "BAM-001",
        "kind": "blocking_ambiguity",
        "severity": "high",
        "title": "397 of 417 ambiguity cards have no Resolution block in Doc09",
        "detail": "Doc09 §3 lists the top-20 severity-sorted cards WITH per-card Resolution (variant chosen + rationale + stakeholder impact + risk). The remaining 397 cards (417 - 20) carry corpus source data + case-impact narrative but NO Resolution block. Doc09 §0 calls itself 'DEEP_ENRICHED' with 'resolution_sections_added: 20' — confirming the structural blindspot. Top-3 unresolved domains by card count: D-09.1 (53 cards), D-04.3 (34 cards), D-09.4 (33 cards).",
        "evidence": [
            "Doc09 §0 frontmatter: 'resolution_sections_added: 20'",
            "Doc09 §3 narrative: 'Top 20 Ambiguity Cards (severity-sorted)'",
            "Doc09 §1: 'ambiguity_cards_top20: 20'",
            "Doc09 §1: 'ambiguity_cards_total: 417'",
            "Doc09 §2 per-subdomain in-scope counts sum = 417",
        ],
        "node_ids": ["D-09.1", "D-04.3", "D-09.4"],
        "recommendation": "Human (P7) — extend Doc09 §3 to cover all 417 cards, OR split into a separate resolution-tracking doc, OR mark Phase 2 as 'top-20 only' as an explicit scope decision. JSON surfaces the structural gap; downstream consumers must not assume all 417 are resolved.",
    },
    {
        "id": "BAM-002",
        "kind": "blocking_ambiguity",
        "severity": "medium",
        "title": "Doc09 §3 top-20 ambiguity cards all carry S3 (high) severity — no S1/S2 visibility",
        "detail": "Doc09 §1 reports 0 S1 + 251 S2 + 252 S3 = 503 instances across 417 cards. Doc09 §3 ranks by 'maximum instance severity' so all 20 top cards have at least one S3 instance. The structural consequence: the top-20 is S3-only and S2-only cards are deprioritised in §3 even when S2 cards materially affect Phase 2 obligation derivation. Risk: S2 cards on D-01.x (encryption design choices), D-08.x (training scope) may have material impact without resolution tracking.",
        "evidence": [
            "Doc09 §1: 'Severity S1 (low): 0; S2 (medium): 251; S3 (high): 252'",
            "Doc09 §3: 'Selection rule: cards ranked by maximum instance severity (S3 > S2 > S1), then by sub-domain ID'",
            "Doc09 §3: all 20 listed cards report severity S3",
        ],
        "node_ids": ["D-01.1", "D-01.2", "D-01.3", "D-01.4"],
        "recommendation": "Human (P7) — adopt Doc09 §3 top-20 as S3-only cohort and add a separate §3b for S2 cards (at least top-20 by sub-domain coverage impact), OR add a severity-tier filter to Phase 2 lints that flags S2 cards touching Sub-SOs without a Resolution block.",
    },
    # ---- Sprint 6 (kg_ontology v1.2) — new cross-doc findings from Sprint 6 ingestion
    {
        "id": "CFL-005",
        "kind": "cross_doc_conflict",
        "severity": "medium",
        "title": "GAP-002 affected_subdomain_ids cites Domain 'D-01' which is not a SecurityControlDomain",
        "detail": (
            "Doc11 §7 row GAP-002 cites 'D-01' as the affected sub-domain. The ontology v1.2 "
            "kg_ontology.id_patterns.SecurityControlDomain regex is '^D-\\d{2}\\.\\d{1}$' which "
            "requires a subdomain dimension (e.g. D-01.1, D-01.2, D-01.3, D-01.4). 'D-01' is a "
            "Domain (parent cluster id), not a SecurityControlDomain. The JSON faithfully stores "
            "affected_subdomain_ids=['D-01'] verbatim, but no FLAGS edge can be emitted because "
            "there is no SecurityControlDomain node with id='D-01'. Doc08 §8 carries the same "
            "value. Downstream consumers must reconcile by either (a) expanding the reference to "
            "D-01.x subdomains, OR (b) softening the regex to allow Domain-grained gap references."
        ),
        "evidence": [
            "Doc11 §7 GAP-002 row: 'Sub-Domain D-01, Regulation GDPR, Clause Art.32, PARTIAL_COVERAGE, MEDIUM'",
            "Doc08 §8 GAP-002 row: 'Gap ID GAP-002 | Regulation GDPR | Clause Art.32 | Sub-Domain D-01'",
            "phase1_ontology.yaml@kg_ontology.id_patterns.SecurityControlDomain: '^D-\\d{2}\\.\\d{1}$'",
            "phase1_ontology.yaml@kg_ontology.classes.SecurityControlDomain.example: 'D-05.3'",
        ],
        "node_ids": ["GAP-002", "D-01", "D-01.1", "D-01.2", "D-01.3", "D-01.4"],
        "recommendation": "Human (P7) — pick one: (a) update Doc11 §7 + Doc08 §8 to expand D-01 reference to the 4 subdomains (D-01.1..D-01.4) so JSON can emit 4 FLAGS edges, OR (b) add a Domain-typed FLAGS variant to the ontology (subclass of CoverageGap.FLAGS) and emit one FLAGS-Cluster edge to D-01. Default stays: GAP-002 has zero FLAGS edges; this audit documents the gap.",
    },
    {
        "id": "CVG-005",
        "kind": "coverage_gap",
        "severity": "low",
        "title": "Doc03 §4 BG Owner labels 'Lead Dev' and 'Procurement' do not have unambiguous STK-ID mapping",
        "detail": (
            "The 7-stakeholder register (Doc03 §3.1) does NOT contain a 'Lead Dev' or "
            "'Procurement' stakeholder; STK-DEVP-01's row Name is 'Development Team' "
            "(a multi-person team, not a single Lead) and there is no Procurement stakeholder. "
            "Doc03 §4 BG-02/04 cite 'Lead Dev' in Owner; BG-05 cites 'Procurement' in Owner + "
            "Affected. Per the brief's 'if inferred, NOT ADDED as an edge' constraint, these "
            "BG→Stakeholder relationships are NOT encoded as DEFINES edges. Risk: downstream "
            "Phase 2 RACI derivation will see CTO/CUSTOMER as the only owners of BG-02/04/05 "
            "and may misallocate work. Acknowledged limitation of the 7-stakeholder register."
        ),
        "evidence": [
            "Doc03 §3.1: 7 stakeholder rows; none has Name='Lead Dev' or Name='Procurement'",
            "Doc03 §3.1 row 4: STK-DEVP-01 Name='Development Team' (team, not single lead)",
            "Doc03 §4 BG-02 Owner='Lead Dev'; BG-04 Owner='Lead Dev + CTO'; BG-05 Owner='CTO + Procurement'",
            "Doc03 §4 BG-05 Affected Stakeholders='CTO, Procurement, B2B clients (procurement)'",
        ],
        "node_ids": ["STK-DEVP-01", "BG-02", "BG-04", "BG-05"],
        "recommendation": "Human (P7) — either (a) extend the stakeholder register with STK-LEADDEV-01 + STK-PROCUREMENT-01 (and re-emit 3 more DEFINES edges), OR (b) split STK-DEVP-01 into 'STK-DEVP-LEAD-01' + 'STK-DEVP-TEAM-01' to disambiguate single-lead vs team responsibilities. Default stays: 13 DEFINES edges emitted (only 1-step-unambiguous mappings).",
    },
    {
        "id": "BAM-003",
        "kind": "blocking_ambiguity",
        "severity": "low",
        "title": "BG-02 'Affected Stakeholders' cites 'EU market-surveillance authorities' with no STK-ID mapping",
        "detail": (
            "Doc03 §4 BG-02 row Affected Stakeholders column reads "
            "'CTO, Lead Dev, B2B clients (procurement), EU market-surveillance authorities'. "
            "The 7-stakeholder register carries no entry for market-surveillance authorities. "
            "The downstream JSON relationship graph therefore cannot trace the BG-02 ↔ "
            "EU-authorities dependency via STK-IDs. This is a blocking ambiguity for any "
            "Phase 2 deliverable that wants to compute 'regulators as stakeholders' (e.g. "
            "Doc07 RACI for incident notification timelines under CRA Art.14)."
        ),
        "evidence": [
            "Doc03 §4 BG-02 row: 'Affected Stakeholders | CTO, Lead Dev, B2B clients (procurement), EU market-surveillance authorities'",
            "Doc03 §3.1: 7 stakeholder rows; none references market-surveillance or authorities",
            "phase1_ontology.yaml@kg_ontology.relations: SUPPORTS (Stakeholder→Regulation, external only) is 'deferred' status",
        ],
        "node_ids": ["BG-02"],
        "recommendation": "Human (P7) — if downstream needs the EU-authorities ↔ BG-02 relationship, add an 'STK-AUTHORITY-EU-01' External stakeholder row to Doc03 §3.1 + a JSON emit. Currently no STK-ID exists, so no edge is emitted; this audit documents the missing node.",
    },
    {
        "id": "BLN-003",
        "kind": "broken_link",
        "severity": "low",
        "title": "Doc03 §3.1 Contact column is '—' for 6 of 7 stakeholders (only Stripe has an email)",
        "detail": (
            "The Stakeholder class ontology attrs do not mandate a contact channel, so this "
            "is informational only. However, downstream task-tracking tools (e.g. Phase 2 "
            "Doc07 RACI for 'Who do we email when X happens?') will not have a contact "
            "field on 6/7 stakeholders. SP-augmented attrs should consider adding a nullable "
            "'contact_channel' field to the Stakeholder class in a future ontology revision "
            "(v1.3 or later)."
        ),
        "evidence": [
            "Doc03 §3.1 Contact column: STK-CEO-01='—', STK-CTO-01='—', STK-DPO-01='—', STK-DEVP-01='—', STK-CUSTOMER-01='—', STK-STRIPE-01='compliance@stripe.com', STK-AWS-01='—'",
            "phase1_ontology.yaml@kg_ontology.classes.Stakeholder.attrs: id/name/role/type/department_or_relationship/note — no contact_channel field",
        ],
        "node_ids": ["STK-CEO-01", "STK-CTO-01", "STK-DPO-01", "STK-DEVP-01", "STK-CUSTOMER-01", "STK-STRIPE-01", "STK-AWS-01"],
        "recommendation": "Human (P7) — no JSON fix required (informational). For Phase 2 RACI work, treat the 6 '—' stakeholders as 'no direct contact channel documented' and use Doc07 §? organigram instead. Optionally extend ontology with 'contact_channel: String(nullable)' in v1.3.",
    },
    # ---- Sprint 7 (kg_ontology v1.3) — RACI Phase A coverage gaps (Doc07 §7)
    {
        "id": "GAP-RACI-01",
        "kind": "coverage_gap",
        "severity": "medium",
        "title": "No formal security-awareness training programme in place (annual cycle, completion tracking)",
        "detail": (
            "GAP-RACI-01 from Doc07 §7 (Gaps & Known Limitations, row 1): "
            "TinyTask does not currently run a formalised security-awareness training "
            "programme (per 00_COMMON/01_Company_Context.md §6.2 — IR-08 = NO). "
            "Annual cycle + completion tracking are absent. Linked sub-domain: D-08.1 "
            "(General Security Awareness). All staff (8 employees) are covered by "
            "ACT-31 (DPO=C, CISO=A, Dev=I, Legal=I, HR=R, Board=I) but the underlying "
            "programme is not yet operational. Proportionate mitigation: lightweight "
            "annual 60-min session + completion spreadsheet; LMS not required at MICRO scale."
        ),
        "evidence": [
            "Doc07 §7 row 1: 'GAP-RACI-01 | No formal security-awareness training programme | MEDIUM | D-08.1'",
            "Doc07 §5 Training Status row 1: 'All staff (8 employees) | Annual security awareness | NOT STARTED | 2026-12-31 (target)'",
            "Doc07 §4.8 row 1 ACT-31 RACI cells: HR=R (HR-coordination), CISO=A",
            "phase1_ontology.yaml@kg_ontology.invariants.counts.gap_raci_count: 5",
        ],
        "node_ids": ["D-08.1", "ACT-31", "ROLE-HR", "ROLE-CISO"],
        "recommendation": "Human (P7) — adopt Doc07 §5 target date (2026-12-31) as Phase 2 milestone; track completion in Doc11 §7 GAP-001..004 cross-link matrix. Proportionate to MICRO scale; no enterprise LMS needed.",
    },
    {
        "id": "GAP-RACI-02",
        "kind": "coverage_gap",
        "severity": "medium",
        "title": "No formal secure-coding curriculum for developers (reliance on code review + Snyk feedback)",
        "detail": (
            "GAP-RACI-02 from Doc07 §7 (row 2): Secure-coding training for the "
            "developer team is informal/ad-hoc; no curriculum exists. Linked "
            "sub-domain: D-08.2 (Role-Specific Competence) and §4.7 ACT-28 Code "
            "review (Dev=R/A composite, CISO=C). The Dev=R/A pattern on code review "
            "makes the gap operationally impactful — review quality depends on "
            "training depth. Proportionate mitigation: OWASP Top 10 mapping + Snyk "
            "feedback loop as informal curriculum; full SAST-anchored curriculum "
            "deferred to scale-up."
        ),
        "evidence": [
            "Doc07 §7 row 2: 'GAP-RACI-02 | No formal secure-coding curriculum | MEDIUM | D-08.2'",
            "Doc07 §5 row 2: 'Developers (6 incl. Lead) | Secure coding (OWASP Top 10 mapping) | NOT STARTED — informal ad-hoc only'",
            "Doc07 §4.7 row 2 ACT-28 Code review: Dev=R/A composite (2 edges emitted)",
            "phase1_ontology.yaml@kg_ontology.invariants.counts.raci_composite_cells: 3 (includes ACT-28)",
        ],
        "node_ids": ["D-08.2", "ACT-28", "ACT-32", "ROLE-DEV", "ROLE-CISO"],
        "recommendation": "Human (P7) — formalise quarterly OWASP Top 10 walkthrough as part of dev-team all-hands; align with Doc11 §3 GAP-003 (SBOM) trajectory. No enterprise LMS required at MICRO scale.",
    },
    {
        "id": "GAP-RACI-03",
        "kind": "coverage_gap",
        "severity": "low",
        "title": "DPO refresher cycle not cadence-locked (last done 2025-Q4 informally; next target 2026-Q4)",
        "detail": (
            "GAP-RACI-03 from Doc07 §7 (row 3): DPO refresher cycle is informal. "
            "Last completed 2025-Q4 (CEO informally reviewed CNPD guidance); "
            "next target 2026-Q4. The cycle is not cadence-locked and lacks "
            "completion tracking. Linked sub-domain: D-08.2 (Role-Specific "
            "Competence). §4.8 ACT-33 (Role-specific training — DPO competence "
            "refresh) carries DPO=R/A composite (3rd of the 3 R/A composites "
            "in this dataset). Operational impact low because DPO duties are "
            "narrow and the CEO-as-DPO arrangement is operationally OK."
        ),
        "evidence": [
            "Doc07 §7 row 3: 'GAP-RACI-03 | DPO refresher cycle not cadence-locked | LOW | D-08.2'",
            "Doc07 §5 row 3: 'DPO (CEO) | GDPR refresher; Art. 33/34 mechanics | 2025-Q4 (informal) | 2026-Q4'",
            "Doc07 §4.8 row 3 ACT-33: DPO=R/A composite (3rd of 3 R/A composites)",
            "phase1_ontology.yaml@kg_ontology.invariants.counts.raci_activities_active: 41 (ACT-33 active despite the cadence gap)",
        ],
        "node_ids": ["D-08.2", "ACT-33", "ROLE-DPO", "ROLE-LEGAL"],
        "recommendation": "Human (P7) — lock 2026-Q4 milestone to Doc12 §5 calendar; add CNPD/CNIL guidance review to Doc11 §7 GAP tracking. No formal LMS; one annual 2-hour refresh suffices.",
    },
    {
        "id": "GAP-RACI-04",
        "kind": "coverage_gap",
        "severity": "low",
        "title": "D-08.3 board training absent — deliberately not in scope for TinyTask (informational only)",
        "detail": (
            "GAP-RACI-04 from Doc07 §7 (row 4): D-08.3 (Management Board Training) "
            "is INACTIVE for TinyTask because its participating regulations are "
            "NIS2 + DORA, both inapplicable (NIS2: 8 employees below 50 threshold; "
            "DORA: not a financial entity). ACT-34 (Board cybersecurity briefings) "
            "has all '—' in the §4.8 RACI table and is recorded as active=False; "
            "ACT-35 (Quarterly informal cybersecurity briefing to the 2 founders, "
            "CISO=R/Board=A) is a best-practice placeholder, also active=False. "
            "Per AEGIS P0 (Reasoned Disagreement) and Doc07 §7 row 4 Discussion: "
            "this is NOT a compliance gap — recorded as LOW (informational) to make "
            "the methodology's scope decision visible to downstream readers."
        ),
        "evidence": [
            "Doc07 §7 row 4: 'GAP-RACI-04 | D-08.3 board training absent — deliberately not in scope | LOW (informational only) | D-08.3 (INACTIVE)'",
            "Doc07 §4.8 L228 row 'Board cybersecurity briefings (D-08.3)': all '—' cells (ACT-34 active=False)",
            "Doc07 §4.8 L238 best-practice row 'Quarterly informal cybersecurity briefing' (ACT-35 active=False)",
            "phase1_ontology.yaml@kg_ontology.invariants.counts.raci_activities_active: 41 (excludes both ACT-34 and ACT-35)",
            "phase1_ontology.yaml@subdomains.not_covered D-08.3: sole_authority_regulation=NIS2, reason='NIS2 not applicable (below 50 employees)'",
        ],
        "node_ids": ["D-08.3", "ACT-34", "ACT-35", "ROLE-BOARD"],
        "recommendation": "Human (P7) — accept Doc07 §7 'LOW informational' classification; no remediation needed. Retain ACT-34/35 in JSON for future re-activation (e.g., NIS2 sector reclassification, CRA uplift). This audit documents the deliberate non-derivation per Doc07 §0 Critical Caveat.",
    },
    {
        "id": "GAP-RACI-05",
        "kind": "coverage_gap",
        "severity": "low",
        "title": "Single DPO/CISO-individual concentration risk (CEO+CTO are the only DPO/CISO; backup is the other founder)",
        "detail": (
            "GAP-RACI-05 from Doc07 §7 (row 5): DPO and CISO are single "
            "individuals (CEO and CTO respectively) with backup being the "
            "other founder. This is operationally OK at MICRO scale but not "
            "optimised for board independence. Linked sub-domain: D-09.1 "
            "(Governance & Documentation — Information Security Policies). "
            "The RACI table makes this explicit: ROLE-DPO maps_to_stakeholder="
            "STK-CEO-01; ROLE-CISO maps_to_stakeholder=STK-CTO-01; backup is "
            "the cross-role founder. Proportionate mitigation: document the "
            "concentration risk in Doc07 §2 Observations + retain external "
            "Legal Adviser retainer as informal third-line consult."
        ),
        "evidence": [
            "Doc07 §7 row 5: 'GAP-RACI-05 | Single DPO/CISO-individual concentration risk | LOW | D-09.1 (governance maturity)'",
            "Doc07 §2 (Key Roles table) row 1: DPO backup='CTO (acting DPO; not legally optimal but documented for incident-trigger continuity)'",
            "Doc07 §2 row 2: CISO backup='CEO (acting CISO)'",
            "phase1_ontology.yaml@kg_ontology.classes.RaciRole.attrs: backup field is nullable String",
        ],
        "node_ids": ["D-09.1", "ROLE-DPO", "ROLE-CISO", "ROLE-BOARD"],
        "recommendation": "Human (P7) — accept at MICRO scale; re-evaluate when employees > 12 or revenue > €5M. Retain external Legal Adviser retainer (ROLE-LEGAL) as informal consult channel; document in Doc11 §3 governance maturity note.",
    },
    # ---- Sprint 8 / Phase B — Doc04 + Doc06 (Architecture & Third Parties)
    {
        "id": "NEW-01",
        "kind": "broken_link",
        "severity": "medium",
        "title": "Doc04 §3 Compliance Mapping contains free-text system references not modeled as SYS-* edges",
        "detail": (
            "Doc04 §3 (lines 125–161) includes 12+ Compliance Mapping entries whose "
            "'Relevant Systems' column references components not captured by the "
            "SYS-* inventory: 'cloud IAM' (D-03.1, D-03.2), 'GitHub organisation' "
            "(D-03.1, D-03.2), 'STORE-03 monitoring' (D-04.1, D-04.3, D-05.2, D-10.1), "
            "'SYS-01 release pipeline' (D-06.2, D-07.2, D-07.3), 'Stripe' (D-06.1, "
            "D-06.3, D-09.4), 'Datadog' (D-06.3). The Executor chose NOT to fabricate "
            "new System nodes for these free-text labels in Phase B; INVOLVES edges "
            "are only emitted where the row contains a SYS-* id. Free-text references "
            "would require introducing new System subtypes (e.g. 'IAM-as-a-Service', "
            "'CI/CD-pipeline-as-System') or treating Datadog/GitHub as System-level "
            "rather than ThirdParty-level, both of which are ontology decisions "
            "(AEGIS P7)."
        ),
        "evidence": [
            "Doc04 §3 row D-03.1: 'Relevant Systems' = 'SYS-02, cloud IAM, GitHub organisation'",
            "Doc04 §3 row D-03.2: 'Relevant Systems' = 'SYS-02, cloud IAM, GitHub organisation'",
            "Doc04 §3 row D-04.1: 'Relevant Systems' = 'SYS-01, SYS-03, STORE-03 monitoring'",
            "Doc04 §3 row D-06.2: 'Relevant Systems' = 'SYS-01 release pipeline'",
            "Doc04 §3 row D-06.3: 'Relevant Systems' = 'SYS-02, SYS-03, SYS-05, Stripe, Datadog'",
            "Doc04 §3 row D-07.2: 'Relevant Systems' = 'SYS-01 release pipeline'",
            "Doc04 §3 row D-09.4: 'Relevant Systems' = 'SYS-01, SYS-02, SYS-03, SYS-05, Stripe'",
            "phase1_ontology.yaml@kg_ontology.classes.System.attrs.tech_stack implies a single system maps to one tech_stack column — split naming would conflict",
            "phase1_ontology.yaml@kg_ontology.classes.ThirdParty — GitHub and Datadog are modeled as ThirdParty, not System",
        ],
        "node_ids": ["D-03.1", "D-03.2", "D-04.1", "D-04.3", "D-05.2", "D-06.1", "D-06.2", "D-06.3", "D-07.2", "D-07.3", "D-09.4", "D-10.1", "STORE-03", "GitHub", "Datadog"],
        "recommendation": "Human (P7) — either (a) split the SYS-* inventory into sub-system nodes (e.g. SYS-02-IAM, SYS-01-CICD), (b) treat CI/CD pipelines as a separate System class 'BuildPipeline', or (c) accept the conservative mapping (Phase B default) where free-text references are surfaced as audits rather than emitted as edges. The chosen default avoids fabricating node types but means INVOLVES counts for D-03.1/03.2/04.1/04.3/05.2/06.2/07.2/07.3/09.4/10.1 underrepresent the true sub-domain surface area.",
    },
    {
        "id": "NEW-02",
        "kind": "cross_doc_conflict",
        "severity": "low",
        "title": "Doc03 §3.1 stakeholder register missing Auth0, Datadog, GitHub, Snyk — drift candidate for Phase B third-party surface",
        "detail": (
            "Doc03 §3.1 (Stakeholder Register) inventories 7 external/internal "
            "stakeholders; Doc06 §2 + §5 inventories 6 third-party vendors (AWS, "
            "Stripe, Auth0, Datadog, GitHub, Snyk). Only AWS and Stripe have a "
            "corresponding STK-* entry (STK-AWS-01, STK-STRIPE-01), so CORRESPONDS_TO "
            "edges are emitted for those two. Auth0, Datadog, GitHub, and Snyk have "
            "DPAs / subprocessor contracts per Doc06 §4 + §6 but no STK-* counterpart "
            "in Doc03. This is an upstream register limitation, not a graph defect: "
            "the conservative approach (per the Phase B brief) is to emit only the "
            "2 CORRESPONDS_TO edges that resolve unambiguously, and document the "
            "remaining 4 vendors as third-party-only entities with no Stakeholder "
            "counterpart. The CORRESPONDS_TO verb is therefore marked `status: "
            "partial` in phase1_ontology.yaml@kg_ontology.relations (the 4 "
            "unresolved vendors will surface as audit references, not missing edges)."
        ),
        "evidence": [
            "Doc03 §3.1 Stakeholder Register (7 rows): STK-CEO-01, STK-CTO-01, STK-DPO-01, STK-DEVP-01, STK-CUSTOMER-01, STK-STRIPE-01, STK-AWS-01",
            "Doc06 §2 + §5 Third-Party table (6 vendors): AWS, Stripe, Auth0, Datadog, GitHub, Snyk",
            "phase1_ontology.yaml@kg_ontology.relations.CORRESPONDS_TO status: partial",
            "phase1_ontology.yaml@kg_ontology.relations.CORRESPONDS_TO cardinality: N:0..1 (only AWS and Stripe have STK-* entries)",
        ],
        "node_ids": ["STK-AWS-01", "STK-STRIPE-01", "AWS", "Stripe", "Auth0", "Datadog", "GitHub", "Snyk"],
        "recommendation": "Human (P7) — extend Doc03 §3.1 to cover Auth0, Datadog, GitHub, Snyk (4 new STK-* rows: STK-AUTH0-01, STK-DATADOG-01, STK-GITHUB-01, STK-SNYK-01) before downstream phases consume the Stakeholder/ThirdParty axis. Until then, the 4 vendors exist as ThirdParty nodes without a Stakeholder counterpart (intentional gap; surfaced here per P5 change propagation).",
    },
    {
        "id": "NEW-03",
        "kind": "coverage_gap",
        "severity": "low",
        "title": "AWS decomposed as 1 ThirdParty + 4 services — decision documented (per Doc06 §5: 'AWS counted once despite four services')",
        "detail": (
            "Doc06 §2 lists 4 AWS service rows (EC2/compute = SYS-01, RDS = SYS-03, "
            "S3 = SYS-05, Cloud KMS = SYS-04). Doc06 §5 explicitly states 'AWS "
            "counted once despite four services; Auth0 counted once despite appearing "
            "in Section 2 and Section 3.' This is a deliberate granularity decision "
            "for proportionality: a micro-SaaS at MICRO scale treats AWS as a single "
            "vendor relationship (1 MSA + 1 AWS DPA + 1 subprocessor list), not as 4 "
            "vendor relationships. Phase B follows this decision: AWS appears as 1 "
            "ThirdParty node (id='AWS') with services listed as a List<String> attr "
            "(['EC2/compute', 'RDS/managed PostgreSQL', 'S3/object storage', 'Cloud "
            "KMS']). Downstream consumers that need per-service granularity can "
            "split this into 4 ThirdParty nodes in a future phase if proportionality "
            "shifts (e.g., to SMALL or MEDIUM scale)."
        ),
        "evidence": [
            "Doc06 §5 supplier count line 180: 'Vendor count: 6 (AWS counted once despite four services; Auth0 counted once despite appearing in Section 2 and Section 3)'",
            "Doc06 §2 rows 1–4: 4 AWS service rows (EC2, RDS, S3, Cloud KMS)",
            "phase1_ontology.yaml@kg_ontology.classes.ThirdParty.attrs.services: List<String>",
            "Doc06 §4 subprocessor table: 1 row for AWS (consolidating EC2/RDS/S3/KMS)",
        ],
        "node_ids": ["AWS", "SYS-01", "SYS-03", "SYS-04", "SYS-05"],
        "recommendation": "Human (P7) — accept the AWS-as-1-ThirdParty consolidation per Doc06 §5. If per-service granularity becomes necessary (e.g. for a NIST CSF PR.PS-06 'component inventory' sub-domain with sub-vendor risk tiers), split AWS into 4 ThirdParty nodes in a future revision. Default remains 1 node + services list attr.",
    },
    {
        "id": "NEW-04",
        "kind": "coverage_gap",
        "severity": "medium",
        "title": "Datadog exit plan not explicitly documented in Doc06 §5 or §6 (only §2 mentions 'outage would degrade D-10.1 monitoring for the duration')",
        "detail": (
            "Doc06 §5 (Supply Chain Risk table) lists Datadog with risk_score=M and "
            "last_assessment=2026-04 but does NOT include an explicit exit_plan "
            "field. Doc06 §2 lists Datadog with 'Exit Plan? = Y, Datadog publishes "
            "subprocessor list' — but this is for the SUBPROCESSOR list "
            "(notification flow), not a DATA EXIT plan. Doc06 §8 GAP-TPL-02 covers "
            "only AWS-hosted data extraction (DB dump + S3 inventory), not "
            "Datadog-specific data egress. Datadog processes pseudonymised logs "
            "only (no raw customer content by design), so the residual data-at-Datadog "
            "is pseudonymised operational metadata; the exit story is implicit (DPA "
            "termination + vendor-side deletion per Art. 28(3)(g)). Phase B emits "
            "Datadog as a ThirdParty node with exit_plan=None (matching Doc06's "
            "gap), and surfaces the gap here."
        ),
        "evidence": [
            "Doc06 §2 row 6 (Datadog): 'Exit Plan? = Y' (refers to subprocessor approval flow, not data egress)",
            "Doc06 §5 row 4 (Datadog): risk_score=M; no exit_plan column present in §5 schema",
            "Doc06 §6 row 4 (Datadog): no exit_plan column",
            "Doc06 §8 GAPs: GAP-TPL-01 (no SIG questionnaire), GAP-TPL-02 (AWS exit procedure), GAP-TPL-03 (SBOM), GAP-TPL-04 (annual review) — NO Datadog-specific data-egress gap row",
            "Doc06 §2 row 6 data_accessed: 'Pseudonymised operational logs and metrics — no raw customer content by design'",
            "phase1_ontology.yaml@kg_ontology.classes.ThirdParty.attrs.exit_plan: nullable",
        ],
        "node_ids": ["Datadog", "STORE-03", "FLOW-03", "D-10.1"],
        "recommendation": "Human (P7) — accept the implicit-exit-plan position (pseudonymised logs + DPA Art. 28(3)(g) termination clause is proportionate at MICRO scale), OR explicitly document a Datadog data-egress procedure (e.g. request log export via Datadog API → vendor-side deletion confirmation → 30-day retention override) in a Doc06 §9 update. Until either action, the exit_plan attr on the Datadog ThirdParty node is left null with this audit surfacing the gap.",
    },
    {
        "id": "NEW-05",
        "kind": "broken_link",
        "severity": "low",
        "title": "Snyk SBOM is available but DPA tier not specified (Doc06 §6 row 6: 'Y (Snyk DPA — paid tiers)')",
        "detail": (
            "Doc06 §6 row 6 (Snyk) states 'Art. 28 DPA: Y (Snyk DPA — paid tiers)' "
            "and 'Art. 30 Clauses: Limited (developer tool; no personal data "
            "processed)'. Doc06 §5 row 6 (Snyk) confirms SBOM availability: 'Y "
            "(Snyk can output CycloneDX/SPDX for the scanned projects)'. The "
            "qualifier 'paid tiers' is the only place the DPA tier is hinted; the "
            "concrete tier (e.g. 'Free' / 'Team' / 'Enterprise') is not recorded. "
            "Phase B captures this faithfully: art_28_dpa=True with no tier attr. "
            "Downstream consumers that need tier granularity (e.g. for vendor risk "
            "scoring under a future VSAQ workflow) will see art_28_dpa=True and no "
            "tier discriminator — i.e. the link from Snyk to Art. 28 coverage is "
            "complete but not tier-resolved."
        ),
        "evidence": [
            "Doc06 §5 row 6 (Snyk): 'L (DPA in paid tier; on-demand scans; no persistent data flow)'",
            "Doc06 §6 row 6 (Snyk): 'Art. 28 DPA | Y (Snyk DPA — paid tiers)'",
            "Doc06 §5 row 6 (Snyk): 'SBOM Available? | Y'",
            "Doc06 §6 row 6 (Snyk): 'Security Audit Right | Indirect — Snyk SOC 2 available'",
            "phase1_ontology.yaml@kg_ontology.classes.ThirdParty.attrs.art_28_dpa: Boolean (no tier discriminator)",
        ],
        "node_ids": ["Snyk", "D-02.1", "D-06.2"],
        "recommendation": "Human (P7) — if tier granularity becomes material, add a tier attr to phase1_ontology.yaml@kg_ontology.classes.ThirdParty (e.g. 'dpa_tier: String') and re-extract Snyk's tier from the Snyk order confirmation / subscription record. Until then, art_28_dpa=True is the canonical signal for DPA presence.",
    },
    # ---- Phase C (Doc08 §9 + Doc12 §4) — Maturity & verification attrs -------
    {
        "id": "NEW-06",
        "kind": "cross_doc_conflict",
        "severity": "medium",
        "title": "Doc08 §9 has 1 row for Art. 35 but phase1_graph.json carries 2 Art. 35 clauses (GDPR-C27, GDPR-C28); §9 also has 1 Art. 37 row with no matching clause",
        "detail": (
            "Doc08 §9 contains 28 GDPR rows; the table lists articles 1, 2, 3, 5, 6, 7, 8, 9, 12, 13, 14, "
            "15, 16, 17, 18, 19, 20, 21, 22, 25, 28, 30, 31, 32, 33, 34, 35, 37 (28 rows).  The existing "
            "phase1_graph.json CLAUSES list carries 28 GDPR clauses mapped to articles 1, 2, 3, 5, 6, 7, 8, "
            "9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 28, 30, 31, 32, 33, 34, 35, 35(1).  "
            "Two asymmetries surface: "
            "(a) §9 has ONE Art. 35 row (DPIA, D-09.2) but the JSON carries TWO Art. 35 nodes: GDPR-C27 "
            "(article='Art. 35') and GDPR-C28 (article='Art. 35(1)').  The §9 row is assigned to GDPR-C27 "
            "by ordinal mapping; GDPR-C28 (the Art. 35(1) clause) receives no §9 verification row.  "
            "(b) §9 has ONE Art. 37 row (Designation of DPO, D-08.2) but no GDPR clause in the JSON has "
            "article='Art. 37'.  By ordinal mapping that §9 row is forced onto GDPR-C28 (whose JSON "
            "article label is 'Art. 35(1)') — producing a topic drift in ART_VERIFICATION (the verification "
            "attributes for GDPR-C28 describe Art. 37 / DPO, not Art. 35(1) / DPIA).  "
            "Either Doc08 §9 must be expanded (1 -> 2 for Art. 35; +1 row for Art. 37), or the JSON's "
            "CLAUSES list must drop GDPR-C28 (Art. 35(1)) and add a GDPR-C29 Art. 37 clause, or vice-versa.  "
            "Hard constraint forbids editing source docs, so the JSON records the §9 → clause_id mapping "
            "verbatim and surfaces this audit for human reconciliation per P7."
        ),
        "evidence": [
            "Doc08 §9 line 339: 'Art. 35 | Data protection impact assessment | D-09.2 ...' (1 §9 row for Art. 35)",
            "phase1_graph.json@CLAUSES: ('GDPR-C27', 'REG-GDPR', 'Art. 35', 'Data protection impact assessment', ...) AND ('GDPR-C28', 'REG-GDPR', 'Art. 35(1)', 'Data protection impact assessment (DPIA)', ...) — 2 Art. 35 clauses",
            "Doc08 §9 line 340: 'Art. 37 | Designation of DPO | D-08.2 ...' (1 §9 row for Art. 37; no GDPR clause in JSON has article='Art. 37')",
            "phase1_graph.json@CLAUSES article column has 'Art. 35(1)' as the 28th GDPR label, NOT 'Art. 37'",
        ],
        "node_ids": ["GDPR-C27", "GDPR-C28", "D-09.2", "D-08.2"],
        "recommendation": (
            "Human (P7) — pick one: (a) expand Doc08 §9 to 2 rows for Art. 35 (Art. 35(1) and Art. 35(7/11)) "
            "and add an Art. 37 row for DPO Designation, leaving CLAUSES as-is; OR (b) drop GDPR-C28 (Art. 35(1)) "
            "from CLAUSES, add GDPR-C29 = Art. 37 (DPO Designation → D-08.2), so 28 §9 rows map 1:1 to 28 GDPR "
            "clauses by article; OR (c) adopt a many-to-one mapping where ART_VERIFICATION rows for Art. 35 "
            "duplicate to both GDPR-C27 and GDPR-C28 (would require expanding ART_VERIFICATION from 54 to 55 rows). "
            "Default stays: ordinal mapping; both asymmetries documented in this audit."
        ),
    },
    {
        "id": "NEW-07",
        "kind": "broken_link",
        "severity": "low",
        "title": "Doc08 §9 evidence_type strings embed non-canonical artifact names that don't map to corpus anchor IDs",
        "detail": (
            "Doc08 §9 'Evidence Type' column carries ad-hoc artifact descriptors for each article, e.g. "
            "'DEMONSTRATE + INSPECT (SSDF checklist + SAMM maturity)' (CRA-C01/C02/D-07.1), "
            "'INSPECT (Firebase MFA enforcement + reset flow test)' (CRA-C09/D-03.2), "
            "'INSPECT (config audit + annual review)' (GDPR-C04, CRA-C24), "
            "'DEMONSTRATE + INSPECT (AWS Backup + quarterly DR test)' (CRA-C26, GDPR-C19/D-04.4).  "
            "These parenthetical descriptors name project-specific evidence artefacts that are NOT mapped "
            "to any corpus anchor ID (e.g. there is no 'EVD-FIREBASE-MFA-CHECKLIST' or 'EVD-AWS-BACKUP-DR' "
            "in the kg_ontology.id_patterns registry).  Downstream Phase 2 / Phase 3 tooling cannot "
            "machine-verify the evidence_type without a registry.  Coverage gap: the §9 narrative is "
            "useful for humans but cannot be lint-validated for completeness.  The descriptor strings are "
            "preserved verbatim in attrs.evidence_type on each RegulatoryClause for human review only."
        ),
        "evidence": [
            "Doc08 §9 row CRA-C01: 'DEMONSTRATE + INSPECT (SSDF checklist + SAMM maturity)'",
            "Doc08 §9 row CRA-C09: 'INSPECT (Firebase MFA enforcement + reset flow test)'",
            "Doc08 §9 row GDPR-C04 / CRA-C24: 'INSPECT (config audit + annual review)'",
            "Doc08 §9 row CRA-C26 / GDPR-C19: 'DEMONSTRATE + INSPECT (AWS Backup + quarterly DR test)'",
            "phase1_ontology.yaml@kg_ontology.id_patterns: no 'EVD-' prefix registered; registry only covers Phase-1 node/edge IDs",
        ],
        "node_ids": ["CRA-C01", "CRA-C02", "CRA-C09", "CRA-C24", "CRA-C26", "GDPR-C04", "GDPR-C19"],
        "recommendation": (
            "Human (P7) — the Phase C attrs.evidence_type field is informational; for machine-validation either "
            "(a) register a 'EVIDENCE' type + 'EVD-<artifact>' ID pattern in the kg_ontology and re-emit §9 with "
            "those anchors, OR (b) drop the parenthetical descriptor from §9 and rely on the operational check "
            "pointer ('Doc 07c Appendix A §A.1.1/D-XX.Y') as the canonical evidence reference.  Default stays: "
            "preserve original §9 strings verbatim."
        ),
    },
    {
        "id": "NEW-08",
        "kind": "coverage_gap",
        "severity": "low",
        "title": "Evidence coverage v1.6: all 37 active sub-domains carry evidence_ids; D-08.3 (NOT_ADDRESSED, inactive) has none by design",
        "detail": (
            "Per ontology v1.6 (MATURITY_MODEL_CSF_STRICT.md), sub-domains hold EVIDENCE, not maturity scalars: the "
            "prior Doc12 \u00a74 'Maturity (cur\u2192tgt)' column was removed and this audit superseded the old uniform-2/4\u21923/4 "
            "finding.  Coverage verified at build time: 37 of 38 SecurityControlDomain nodes carry attrs.evidence_ids "
            "pointing at Coverage EvidenceItem nodes (Scale B) whose sources[] must resolve (validator check_phase_c "
            "Gates 2\u20134).  The single exception is D-08.3 (Threat-Led Penetration Testing, NOT_ADDRESSED, inactive), "
            "which holds no evidence by design \u2014 a NOT_ADDRESSED sub-domain has no obligations to evidence."
        ),
        "evidence": [
            "phase1_graph.json: 37/38 SecurityControlDomain nodes with non-empty attrs.evidence_ids (only D-08.3 empty)",
            "Doc12 \u00a74 v1.6 note: maturity_cur/maturity_tgt removed; Implementation Status is the sole posture field",
            "phase1_ontology.yaml@kg_ontology.maturity_model: forbidden_subdomain_attrs = [tier, maturity_cur, maturity_tgt, maturity_score, capability_score]",
            "scripts/build_p1_dashboard.py check_phase_c Gates 2\u20134: proportionality keys + evidence_ids + sources[] resolution",
        ],
        "node_ids": ["D-01.1", "D-08.3"],
        "recommendation": (
            "Human (P7) \u2014 no action required; this is the positive coverage marker for the v1.6 model.  Standing "
            "rule: if D-08.3 (or any other NOT_ADDRESSED sub-domain) is ever activated, it MUST gain evidence_ids "
            "with resolvable sources[] before the Phase C gates pass."
        ),
    },
]
assert len(AUDITS) == 29, f"AUDITS drift: {len(AUDITS)} (expected 29 base = 26 v1.4 + 3 NEW-Phase C; 2 NEW-Phase D audits appended at runtime)"

# ---------------------------------------------------------------------------
# 10. Sprint 6 — Stakeholders + BusinessGoals + CoverageGaps
#     Sources: Doc03 §3.1 (7 stakeholders), Doc03 §4 (5 BGs),
#              Doc11 §7 + Doc08 §8 (4 coverage gaps).
#     Schema: phase1_ontology.yaml@kg_ontology.classes v1.2
#     ID patterns (verified by build_p1_dashboard.py --check id_patterns):
#       Stakeholder:           ^STK-[A-Z]+-\d{2}$
#       BusinessGoal:          ^BG-\d{2}$
#       CoverageGap:           ^GAP-\d{3}$
# ---------------------------------------------------------------------------

STAKEHOLDERS = [
    {
        "id": "STK-CEO-01",
        "label": "CEO",
        "attrs": {
            "name": "CEO (implicit)",
            "type": "Internal",
            "department_or_relationship": "TinyTask Lda.",
            "note": "Business strategy, compliance accountability",
        },
        "source": ["Doc03 §3.1 (Stakeholder Register, row 1)",
                   "phase1_ontology.yaml@kg_ontology.classes.Stakeholder"],
    },
    {
        "id": "STK-CTO-01",
        "label": "CTO",
        "attrs": {
            "name": "CTO (implicit)",
            "type": "Internal",
            "department_or_relationship": "TinyTask Lda.",
            "note": "Technical leadership, security architecture",
        },
        "source": ["Doc03 §3.1 (Stakeholder Register, row 2)",
                   "phase1_ontology.yaml@kg_ontology.classes.Stakeholder"],
    },
    {
        "id": "STK-DPO-01",
        "label": "DPO",
        "attrs": {
            "name": "DPO (implicit)",
            "type": "Internal",
            "department_or_relationship": "TinyTask Lda.",
            "note": "Data protection oversight, GDPR compliance",
        },
        "source": ["Doc03 §3.1 (Stakeholder Register, row 3)",
                   "phase1_ontology.yaml@kg_ontology.classes.Stakeholder"],
    },
    {
        "id": "STK-DEVP-01",
        "label": "Development Team",
        "attrs": {
            "name": "Development Team",
            "type": "Internal",
            "department_or_relationship": "TinyTask Lda.",
            "note": "Secure development, implementation",
        },
        "source": ["Doc03 §3.1 (Stakeholder Register, row 4)",
                   "phase1_ontology.yaml@kg_ontology.classes.Stakeholder"],
    },
    {
        "id": "STK-CUSTOMER-01",
        "label": "B2B Customers",
        "attrs": {
            "name": "B2B Customers",
            "type": "External",
            "department_or_relationship": "Client organizations",
            "note": "Data controllers; recipient of breach notifications",
        },
        "source": ["Doc03 §3.1 (Stakeholder Register, row 5)",
                   "phase1_ontology.yaml@kg_ontology.classes.Stakeholder"],
    },
    {
        "id": "STK-STRIPE-01",
        "label": "Stripe",
        "attrs": {
            "name": "Stripe",
            "type": "External",
            "department_or_relationship": "Stripe Technologies",
            "note": "Payment processing; PCI-DSS compliance",
        },
        "source": ["Doc03 §3.1 (Stakeholder Register, row 6)",
                   "phase1_ontology.yaml@kg_ontology.classes.Stakeholder"],
    },
    {
        "id": "STK-AWS-01",
        "label": "AWS",
        "attrs": {
            "name": "AWS",
            "type": "External",
            "department_or_relationship": "Amazon Web Services",
            "note": "Cloud infrastructure; inherited security controls",
        },
        "source": ["Doc03 §3.1 (Stakeholder Register, row 7)",
                   "phase1_ontology.yaml@kg_ontology.classes.Stakeholder"],
    },
]
assert len(STAKEHOLDERS) == 7

BUSINESS_GOALS = [
    {
        "id": "BG-01",
        "label": "BG-01 GDPR Compliance Baseline",
        "attrs": {
            "description": (
                "Establish baseline GDPR compliance for all personal data "
                "processing activities (Zero audit findings; RoPA complete)."
            ),
            "priority": "HIGH",
            "status": "IN_PROGRESS",
            "stakeholders": ["STK-CEO-01", "STK-CTO-01", "STK-DPO-01", "STK-CUSTOMER-01"],
            "strategic_alignment": "Aligns with Doc 07c_Adjusted_Goals §1 (Generic Baseline) + §2 (HL, 35 rows) + §3 (GDPR-driven, 28 rows).",
        },
        "source": ["Doc03 §4 Business Goals Catalog (BG-01 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.BusinessGoal"],
    },
    {
        "id": "BG-02",
        "label": "BG-02 CRA Conformity",
        "attrs": {
            "description": (
                "Achieve CRA conformity for Team Organizer SaaS product "
                "(SBOM published; security.txt active)."
            ),
            "priority": "HIGH",
            "status": "TODO",
            "stakeholders": ["STK-CTO-01", "STK-CUSTOMER-01"],
            "strategic_alignment": "Aligns with Doc 07c_Adjusted_Goals §4 (CRA-driven, 34 rows) + D-02.x / D-06.2 / D-07.x.",
        },
        "source": ["Doc03 §4 Business Goals Catalog (BG-02 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.BusinessGoal"],
    },
    {
        "id": "BG-03",
        "label": "BG-03 Data Subject Rights",
        "attrs": {
            "description": (
                "Enable data export and erasure for all users "
                "(<30d DSAR turnaround; JSON export endpoint live within 90 days)."
            ),
            "priority": "MEDIUM",
            "status": "TODO",
            "stakeholders": ["STK-DPO-01", "STK-CTO-01", "STK-CUSTOMER-01"],
            "strategic_alignment": "Aligns with Doc 07c_Adjusted_Goals §3 GDPR-driven D-05.3 / D-05.4 (LIGHTWEIGHT).",
        },
        "source": ["Doc03 §4 Business Goals Catalog (BG-03 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.BusinessGoal"],
    },
    {
        "id": "BG-04",
        "label": "BG-04 Security by Design",
        "attrs": {
            "description": (
                "Integrate security into development lifecycle "
                "(SAST in CI by end of quarter; zero CRITICAL findings on main branch)."
            ),
            "priority": "MEDIUM",
            "status": "IN_PROGRESS",
            "stakeholders": ["STK-CTO-01", "STK-CUSTOMER-01"],
            "strategic_alignment": "Aligns with Doc 07c_Adjusted_Goals §4 CRA-driven D-02.1 + D-07.x (LIGHTWEIGHT); §3 GDPR-driven AG-D-02.1-001.",
        },
        "source": ["Doc03 §4 Business Goals Catalog (BG-04 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.BusinessGoal"],
    },
    {
        "id": "BG-05",
        "label": "BG-05 Supplier Due Diligence",
        "attrs": {
            "description": (
                "Maintain SOC 2/ISO 27001 evidence from cloud providers "
                "(Annual review of AWS SOC 2, Stripe PCI-DSS, Firebase security docs)."
            ),
            "priority": "MEDIUM",
            "status": "IN_PROGRESS",
            "stakeholders": ["STK-CTO-01", "STK-CUSTOMER-01"],
            "strategic_alignment": "Aligns with Doc 07c_Adjusted_Goals §3 + §4 GDPR/CRA-driven D-06.1 (MINIMAL INHERIT); T-002.",
        },
        "source": ["Doc03 §4 Business Goals Catalog (BG-05 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.BusinessGoal"],
    },
]
assert len(BUSINESS_GOALS) == 5

COVERAGE_GAPS = [
    {
        "id": "GAP-001",
        "label": "GAP-001 RoPA missing (D-09.4 / GDPR Art.30)",
        "attrs": {
            "title": "No records of processing activities (RoPA)",
            "severity": "high",
            "regulation": "REG-GDPR",
            "affected_subdomain_ids": ["D-09.4"],
            "description": (
                "GAP-001 from Doc11 §7: D-09.4 (Records of Processing) NOT_ADDRESSED "
                "with risk level HIGH. Recommended action: create RoPA template. "
                "Cross-evidence: Doc08 §8 GAP-001 row identical."
            ),
            "status": "open",
        },
        "source": ["Doc11 §7 Identified Gaps Summary (GAP-001 row)",
                   "Doc08 §8 Regulatory Gaps Identified (cross-evidence)",
                   "phase1_ontology.yaml@kg_ontology.classes.CoverageGap"],
    },
    {
        "id": "GAP-002",
        "label": "GAP-002 Formal security controls missing (D-01 / GDPR Art.32)",
        "attrs": {
            "title": "No formal security policy (Art.32 documentation)",
            "severity": "medium",
            "regulation": "REG-GDPR",
            # Doc11 §7 lists "D-01" which is a Domain (NOT a SecurityControlDomain
            # whose id_pattern is "^D-\\d{2}\\.\\d{1}$"). Documented verbatim;
            # the type mismatch is flagged by CFL-005 audit. No FLAGS edge is
            # emitted because no SecurityControlDomain with id="D-01" exists.
            "affected_subdomain_ids": ["D-01"],
            "description": (
                "GAP-002 from Doc11 §7: cited at Domain granularity (D-01 Data "
                "Protection & Encryption) rather than SecurityControlDomain "
                "granularity (D-01.1..D-01.4). PARTIAL_COVERAGE with risk MEDIUM. "
                "Recommended action: document security controls. Cross-evidence: "
                "Doc08 §8 GAP-002 row identical."
            ),
            "status": "open",
        },
        "source": ["Doc11 §7 Identified Gaps Summary (GAP-002 row)",
                   "Doc08 §8 Regulatory Gaps Identified (cross-evidence)",
                   "phase1_ontology.yaml@kg_ontology.classes.CoverageGap"],
    },
    {
        "id": "GAP-003",
        "label": "GAP-003 SBOM missing (D-06.2 / CRA Art.18)",
        "attrs": {
            "title": "No SBOM (Software Bill of Materials)",
            "severity": "high",
            "regulation": "REG-CRA",
            "affected_subdomain_ids": ["D-06.2"],
            "description": (
                "GAP-003 from Doc11 §7: D-06.2 (SBOM) NOT_ADDRESSED with risk "
                "level HIGH. Recommended action: implement SBOM tooling. "
                "Cross-evidence: Doc08 §8 GAP-003 row identical."
            ),
            "status": "open",
        },
        "source": ["Doc11 §7 Identified Gaps Summary (GAP-003 row)",
                   "Doc08 §8 Regulatory Gaps Identified (cross-evidence)",
                   "phase1_ontology.yaml@kg_ontology.classes.CoverageGap"],
    },
    {
        "id": "GAP-004",
        "label": "GAP-004 Vulnerability disclosure missing (D-02.3 / CRA Art.21)",
        "attrs": {
            "title": "No vulnerability disclosure process",
            "severity": "medium",
            "regulation": "REG-CRA",
            "affected_subdomain_ids": ["D-02.3"],
            "description": (
                "GAP-004 from Doc11 §7: D-02.3 (Coordinated Vuln. Disclosure) "
                "NOT_ADDRESSED with risk level MEDIUM. Recommended action: create "
                "security.txt. Cross-evidence: Doc08 §8 GAP-004 row identical."
            ),
            "status": "open",
        },
        "source": ["Doc11 §7 Identified Gaps Summary (GAP-004 row)",
                   "Doc08 §8 Regulatory Gaps Identified (cross-evidence)",
                   "phase1_ontology.yaml@kg_ontology.classes.CoverageGap"],
    },
]
assert len(COVERAGE_GAPS) == 4

# DEFINES edges: Stakeholder → BusinessGoal
# Constraint: ONLY edges where Doc03 §4 explicitly names the stakeholder role
# (Owner + Affected Stakeholders columns), with §3.1 register mapping the role
# label to STK-ID performed in a single unambiguous step.
# SKIPPED (inferred, not added):
#   - BG-02/04 "Lead Dev" Owner — §3.1 row Name is "Development Team" (not
#     "Lead Dev"); label mismatch is interpretation, not 1-step derivation.
#   - BG-05 "Procurement" — no STK-ID exists in the 7-stakeholder register.
#   - BG-02 "EU market-surveillance authorities" Affected — no STK-ID exists.
# See audit CVG-005 below for the cross-doc-gap.
DEFINES_EDGES = [
    # BG-01 Owner: CTO + DPO; Affected: CEO, CTO, DPO, B2B clients (data controllers)
    ("STK-CEO-01",     "BG-01", "Doc03 §4 BG-01 row, Affected Stakeholders column: 'CEO, CTO, DPO, all B2B clients (data controllers)'"),
    ("STK-CTO-01",     "BG-01", "Doc03 §4 BG-01 row, Owner column: 'CTO + DPO'"),
    ("STK-DPO-01",     "BG-01", "Doc03 §4 BG-01 row, Owner column: 'CTO + DPO'"),
    ("STK-CUSTOMER-01","BG-01", "Doc03 §4 BG-01 row, Affected Stakeholders column: 'CEO, CTO, DPO, all B2B clients (data controllers)'"),
    # BG-02 Owner: Lead Dev (no STK-ID via single-step mapping — see CVG-005);
    # Affected: CTO, Lead Dev, B2B clients (procurement), EU market-surveillance
    # authorities (latter no STK-ID).
    ("STK-CTO-01",     "BG-02", "Doc03 §4 BG-02 row, Affected Stakeholders column: 'CTO, Lead Dev, B2B clients (procurement), EU market-surveillance authorities'"),
    ("STK-CUSTOMER-01","BG-02", "Doc03 §4 BG-02 row, Affected Stakeholders column: 'CTO, Lead Dev, B2B clients (procurement), EU market-surveillance authorities'"),
    # BG-03 Owner: DPO + CTO; Affected: Customers (data subjects), DPO, B2B client controllers
    ("STK-DPO-01",     "BG-03", "Doc03 §4 BG-03 row, Owner column: 'DPO + CTO'"),
    ("STK-CTO-01",     "BG-03", "Doc03 §4 BG-03 row, Owner column: 'DPO + CTO'"),
    ("STK-CUSTOMER-01","BG-03", "Doc03 §4 BG-03 row, Affected Stakeholders column: 'Customers (data subjects), DPO, B2B client controllers'"),
    # BG-04 Owner: Lead Dev + CTO; Affected: CTO, Lead Dev, B2B clients (security review)
    ("STK-CTO-01",     "BG-04", "Doc03 §4 BG-04 row, Owner column: 'Lead Dev + CTO'"),
    ("STK-CUSTOMER-01","BG-04", "Doc03 §4 BG-04 row, Affected Stakeholders column: 'CTO, Lead Dev, B2B clients (security review)'"),
    # BG-05 Owner: CTO + Procurement (no STK-ID for Procurement); Affected: CTO, Procurement, B2B clients (procurement)
    ("STK-CTO-01",     "BG-05", "Doc03 §4 BG-05 row, Owner column: 'CTO + Procurement'"),
    ("STK-CUSTOMER-01","BG-05", "Doc03 §4 BG-05 row, Affected Stakeholders column: 'CTO, Procurement, B2B clients (procurement)'"),
]
assert len(DEFINES_EDGES) == 13

# FLAGS edges: CoverageGap → SecurityControlDomain. Each tuple = (gap_id, subdomain_id, source_section).
# Note: GAP-002.cite affected_subdomain_ids=['D-01'] does NOT match the
# SecurityControlDomain id_pattern; no FLAGS edge is emitted for it (see CFL-005).
FLAGS_EDGES = [
    ("GAP-001", "D-09.4", "Doc11 §7 GAP-001 row: Sub-Domain D-09.4, Clause Art.30, Regulation GDPR"),
    ("GAP-003", "D-06.2", "Doc11 §7 GAP-003 row: Sub-Domain D-06.2, Clause Art.18, Regulation CRA"),
    ("GAP-004", "D-02.3", "Doc11 §7 GAP-004 row: Sub-Domain D-02.3, Clause Art.21, Regulation CRA"),
]
assert len(FLAGS_EDGES) == 3


# ---------------------------------------------------------------------------
# 10. Sprint 7 — RACI Phase A (Doc07 §2 Roles, §4.1–§4.10 Activities, §7 Gaps,
#                            §9.2 activity→sub-domain mapping)
#     Sources: Doc07 §2 (Key Roles table, 6 roles), §4.1–§4.10 (43 activity rows;
#              41 active + ACT-34 all-'—' placeholder + ACT-35 best-practice),
#              §7 (GAP-RACI-01..05), §9.2 (35-row activity→sub-domain mapping).
#     Schema: phase1_ontology.yaml@kg_ontology.classes v1.3 (RaciRole, RaciActivity).
#     ID patterns (verified by build_p1_dashboard.py --check id_patterns):
#       RaciRole:    ^ROLE-[A-Z0-9]+$
#       RaciActivity: ^ACT-\d{2}$
# ---------------------------------------------------------------------------

# Per Doc07 §2 'Key Roles' table (6 rows). DPO/CISO map to stakeholders; the
# remaining 4 (Dev, Legal, HR, Board) have no single-step STK-ID mapping in the
# 7-stakeholder register (Doc03 §3.1) → maps_to_stakeholder=null (documented).
RACI_ROLES = [
    {
        "id": "ROLE-DPO",
        "label": "CEO (also DPO per Art. 37 voluntary designation)",
        "attrs": {
            "name": "DPO",
            "maps_to_stakeholder": "STK-CEO-01",
            "fte_allocation": "0.2 DPO + business leadership as CEO (combined FTE: 1.0 total)",
            "reports_to": "Board (2 founders)",
            "backup": "CTO (acting DPO; not legally optimal but documented for incident-trigger continuity)",
        },
        "source": ["Doc07 §2 (Key Roles table, row 1: 'CEO (also DPO per Art. 37 voluntary designation)')",
                   "phase1_ontology.yaml@kg_ontology.classes.RaciRole"],
    },
    {
        "id": "ROLE-CISO",
        "label": "CTO (also CISO per CRA Annex I Part II (8)(f))",
        "attrs": {
            "name": "CISO",
            "maps_to_stakeholder": "STK-CTO-01",
            "fte_allocation": "0.3 CISO + technical leadership as CTO (combined FTE: 1.0 total)",
            "reports_to": "Board (2 founders)",
            "backup": "CEO (acting CISO)",
        },
        "source": ["Doc07 §2 (Key Roles table, row 2: 'CTO (also CISO per CRA Annex I Part II (8)(f))')",
                   "phase1_ontology.yaml@kg_ontology.classes.RaciRole"],
    },
    {
        "id": "ROLE-DEV",
        "label": "Lead Developer + developer team (5 staff)",
        "attrs": {
            "name": "Dev",
            "maps_to_stakeholder": None,
            "fte_allocation": "1.0 lead developer + 5 × 1.0 developers (~0.1 of time on security tasks via CI/CD and patching)",
            "reports_to": "CTO",
            "backup": "CTO for code-related security tasks; peer developers",
        },
        "source": ["Doc07 §2 (Key Roles table, row 3: 'Lead Developer (Dev Lead)' + row 4: 'Developer × 5')",
                   "phase1_ontology.yaml@kg_ontology.classes.RaciRole"],
    },
    {
        "id": "ROLE-LEGAL",
        "label": "External Legal Adviser (DPO Support)",
        "attrs": {
            "name": "Legal",
            "maps_to_stakeholder": None,
            "fte_allocation": "0 (retainer; no allocated FTE; ad-hoc consultation)",
            "reports_to": "CEO",
            "backup": "None — single retainer",
        },
        "source": ["Doc07 §2 (Key Roles table, row 5: 'External Legal Adviser (DPO Support)')",
                   "phase1_ontology.yaml@kg_ontology.classes.RaciRole"],
    },
    {
        "id": "ROLE-HR",
        "label": "HR-coordination role (CEO as part of 0.2 FTE DPO)",
        "attrs": {
            "name": "HR",
            "maps_to_stakeholder": None,
            "fte_allocation": "Subsumed in CEO 0.2 DPO FTE (HR-type coordination: training scheduling, on-boarding)",
            "reports_to": "Board",
            "backup": "CEO (same person)",
        },
        "source": ["Doc07 §2 (Key Roles table: 'No separate HR function — HR-type coordination is part of the CEO/DPO 0.2 FTE')",
                   "phase1_ontology.yaml@kg_ontology.classes.RaciRole"],
    },
    {
        "id": "ROLE-BOARD",
        "label": "Management Board (2 founders — CEO + CTO)",
        "attrs": {
            "name": "Board",
            "maps_to_stakeholder": None,
            "fte_allocation": "n/a — board is the board",
            "reports_to": "—",
            "backup": "n/a",
        },
        "source": ["Doc07 §2 (Key Roles table, row 6: 'Management Board')",
                   "phase1_ontology.yaml@kg_ontology.classes.RaciRole"],
    },
]
assert len(RACI_ROLES) == 6, f"RACI_ROLES drift: {len(RACI_ROLES)}"


# Per Doc07 §4.1–§4.10 RACI tables: 43 activity rows. ACT-34 (all-'—' D-08.3
# placeholder) and ACT-35 (§4.8 best-practice row, D-08.3 INACTIVE) both
# carry active=False; the other 41 are active. Each entry maps an ACT-NN
# to its (verbatim) Corpus Reg Req string and source section.
# Column letters per cell (Doc07 §4): DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board
# Composite cells use 'R/A' and split into 2 RACI edges in RACI_EDGES below.
# Role column name (for RACI_EDGES): DPO/CISO/Dev/Legal/HR/Board.
RACI_ACTIVITIES = [
    # --- §4.1 Data Protection (D-01) — 4 activities
    {"id": "ACT-01", "label": "Encrypt personal data at rest",
     "attrs": {"name": "Encrypt personal data at rest", "domain_id": "D-01", "sub_domain_id": "D-01.1",
               "corpus_reg_req": "D-01.1: 1.1.1, 1.1.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.1 L160 row 'Encrypt personal data at rest'"]},
    {"id": "ACT-02", "label": "Manage encryption keys",
     "attrs": {"name": "Manage encryption keys", "domain_id": "D-01", "sub_domain_id": "D-01.3",
               "corpus_reg_req": "D-01.3: 1.3.1, 1.3.2 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.1 L161 row 'Manage encryption keys'"]},
    {"id": "ACT-03", "label": "Notify DPA within 72h (Art. 33 GDPR)",
     "attrs": {"name": "Notify DPA within 72h (Art. 33 GDPR)", "domain_id": "D-04", "sub_domain_id": "D-04.3",
               "corpus_reg_req": "D-04.3: 4.3.1, 4.3.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.1 L162 row 'Notify DPA within 72h (Art. 33 GDPR)'"]},
    {"id": "ACT-04", "label": "Conduct DPIA (Art. 35 GDPR)",
     "attrs": {"name": "Conduct DPIA (Art. 35 GDPR)", "domain_id": "D-09", "sub_domain_id": "D-09.2",
               "corpus_reg_req": "D-09.2: 9.2.1, 9.2.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.1 L163 row 'Conduct DPIA (Art. 35 GDPR)'"]},
    # --- §4.2 Vulnerability Management (D-02) — 4 activities
    {"id": "ACT-05", "label": "Run vulnerability scans (Snyk, dependency review)",
     "attrs": {"name": "Run vulnerability scans (Snyk, dependency review)", "domain_id": "D-02", "sub_domain_id": "D-02.1",
               "corpus_reg_req": "D-02.1: 2.1.1, 2.1.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.2 L169 row 'Run vulnerability scans (Snyk, dependency review)'"]},
    {"id": "ACT-06", "label": "Apply critical patches (CRA Annex I Part I (2)(f))",
     "attrs": {"name": "Apply critical patches (CRA Annex I Part I (2)(f))", "domain_id": "D-02", "sub_domain_id": "D-02.2",
               "corpus_reg_req": "D-02.2: 2.2.1 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.2 L170 row 'Apply critical patches (CRA Annex I Part I (2)(f))'"]},
    {"id": "ACT-07", "label": "Annual penetration testing",
     "attrs": {"name": "Annual penetration testing", "domain_id": "D-02", "sub_domain_id": "D-02.4",
               "corpus_reg_req": "D-02.4: 2.4.1 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.2 L171 row 'Annual penetration testing'"]},
    {"id": "ACT-08", "label": "Operate CVD / security.txt (CRA Art. 14)",
     "attrs": {"name": "Operate CVD / security.txt (CRA Art. 14)", "domain_id": "D-02", "sub_domain_id": "D-02.3",
               "corpus_reg_req": "D-02.3: 2.3.1 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.2 L172 row 'Operate CVD / security.txt (CRA Art. 14)'"]},
    # --- §4.3 Access Control (D-03) — 4 activities
    {"id": "ACT-09", "label": "Manage IAM (Auth0 + cloud IAM)",
     "attrs": {"name": "Manage IAM (Auth0 + cloud IAM)", "domain_id": "D-03", "sub_domain_id": "D-03.1",
               "corpus_reg_req": "D-03.1: 3.1.1, 3.1.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.3 L178 row 'Manage IAM (Auth0 + cloud IAM)'"]},
    {"id": "ACT-10", "label": "Enforce MFA (admins; future customer MFA)",
     "attrs": {"name": "Enforce MFA (admins; future customer MFA)", "domain_id": "D-03", "sub_domain_id": "D-03.2",
               "corpus_reg_req": "D-03.2: 3.2.1, 3.2.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.3 L179 row 'Enforce MFA (admins; future customer MFA)'"]},
    {"id": "ACT-11", "label": "Quarterly access review",
     "attrs": {"name": "Quarterly access review", "domain_id": "D-03", "sub_domain_id": "D-03.1",
               "corpus_reg_req": "D-03.1: 3.1.1, 3.1.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.3 L180 row 'Quarterly access review'"]},
    {"id": "ACT-12", "label": "Offboarding (revoke access within 24h)",
     "attrs": {"name": "Offboarding (revoke access within 24h)", "domain_id": "D-03", "sub_domain_id": "D-03.1",
               "corpus_reg_req": "D-03.1: 3.1.1, 3.1.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.3 L181 row 'Offboarding (revoke access within 24h)'"]},
    # --- §4.4 Incident Response (D-04) — 6 activities
    {"id": "ACT-13", "label": "Detect incident",
     "attrs": {"name": "Detect incident", "domain_id": "D-04", "sub_domain_id": "D-04.1",
               "corpus_reg_req": "D-04.1: 4.1.1, 4.1.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.4 L187 row 'Detect incident'"]},
    {"id": "ACT-14", "label": "Contain incident",
     "attrs": {"name": "Contain incident", "domain_id": "D-04", "sub_domain_id": "D-04.2",
               "corpus_reg_req": "D-04.2: 4.2.1, 4.2.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.4 L188 row 'Contain incident'"]},
    {"id": "ACT-15", "label": "Notify authorities (72h GDPR Art. 33; 24h early-warning CRA Art. 14)",
     "attrs": {"name": "Notify authorities (72h GDPR Art. 33; 24h early-warning CRA Art. 14)",
               "domain_id": "D-04", "sub_domain_id": "D-04.3",
               "corpus_reg_req": "D-04.3: 4.3.1, 4.3.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.4 L189 row 'Notify authorities (72h GDPR Art. 33; 24h early-warning CRA Art. 14)'"]},
    {"id": "ACT-16", "label": "Notify controllers (Art. 33(2) processor→controller)",
     "attrs": {"name": "Notify controllers (Art. 33(2) processor→controller)",
               "domain_id": "D-04", "sub_domain_id": "D-04.3",
               "corpus_reg_req": "D-04.3: 4.3.1, 4.3.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.4 L190 row 'Notify controllers (Art. 33(2) processor→controller)'"]},
    {"id": "ACT-17", "label": "Recover systems (RPO / RTO targets)",
     "attrs": {"name": "Recover systems (RPO / RTO targets)", "domain_id": "D-04", "sub_domain_id": "D-04.4",
               "corpus_reg_req": "D-04.4: 4.4.1, 4.4.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.4 L191 row 'Recover systems (RPO / RTO targets)'"]},
    {"id": "ACT-18", "label": "Post-incident review",
     "attrs": {"name": "Post-incident review", "domain_id": "D-04", "sub_domain_id": "D-04.2",
               "corpus_reg_req": "D-04.2: 4.2.1, 4.2.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.4 L192 row 'Post-incident review'"]},
    # --- §4.5 Data Lifecycle (D-05) — 4 activities
    {"id": "ACT-19", "label": "Enforce data minimisation",
     "attrs": {"name": "Enforce data minimisation", "domain_id": "D-05", "sub_domain_id": "D-05.1",
               "corpus_reg_req": "D-05.1: 5.1.1, 5.1.2 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.5 L198 row 'Enforce data minimisation'"]},
    {"id": "ACT-20", "label": "Manage retention policies",
     "attrs": {"name": "Manage retention policies", "domain_id": "D-05", "sub_domain_id": "D-05.2",
               "corpus_reg_req": "D-05.2: 5.2.1, 5.2.2 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.5 L199 row 'Manage retention policies'"]},
    {"id": "ACT-21", "label": "Process erasure requests (Art. 17 GDPR; CRA Annex I Part I (2)(m))",
     "attrs": {"name": "Process erasure requests (Art. 17 GDPR; CRA Annex I Part I (2)(m))",
               "domain_id": "D-05", "sub_domain_id": "D-05.3",
               "corpus_reg_req": "D-05.3: 5.3.1, 5.3.2 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.5 L200 row 'Process erasure requests (Art. 17 GDPR; CRA Annex I Part I (2)(m))'"]},
    {"id": "ACT-22", "label": "Process portability requests (Art. 20 GDPR)",
     "attrs": {"name": "Process portability requests (Art. 20 GDPR)",
               "domain_id": "D-05", "sub_domain_id": "D-05.4",
               "corpus_reg_req": "D-05.4: 5.4.1 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.5 L201 row 'Process portability requests (Art. 20 GDPR)'"]},
    # --- §4.6 Supply Chain (D-06) — 4 activities
    {"id": "ACT-23", "label": "Assess vendor security (annual review)",
     "attrs": {"name": "Assess vendor security (annual review)", "domain_id": "D-06", "sub_domain_id": "D-06.1",
               "corpus_reg_req": "D-06.1: 6.1.1, 6.1.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.6 L207 row 'Assess vendor security (annual review)'"]},
    {"id": "ACT-24", "label": "Maintain SBOM (CRA Annex I Part II (1))",
     "attrs": {"name": "Maintain SBOM (CRA Annex I Part II (1))", "domain_id": "D-06", "sub_domain_id": "D-06.2",
               "corpus_reg_req": "D-06.2: 6.2.1 (CRA only — confirmed via manifest)", "active": True},
     "source": ["Doc07 §4.6 L208 row 'Maintain SBOM (CRA Annex I Part II (1))'"]},
    {"id": "ACT-25", "label": "Manage DPA contracts with B2B controllers",
     "attrs": {"name": "Manage DPA contracts with B2B controllers", "domain_id": "D-06", "sub_domain_id": "D-06.3",
               "corpus_reg_req": "D-06.3: 6.3.1, 6.3.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.6 L209 row 'Manage DPA contracts with B2B controllers'"]},
    {"id": "ACT-26", "label": "Manage DPA acceptance from subprocessor vendors",
     "attrs": {"name": "Manage DPA acceptance from subprocessor vendors", "domain_id": "D-06", "sub_domain_id": "D-06.3",
               "corpus_reg_req": "D-06.3: 6.3.1, 6.3.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.6 L210 row 'Manage DPA acceptance from subprocessor vendors'"]},
    # --- §4.7 Secure Development (D-07) — 4 activities (ACT-27/28 Dev = R/A composite)
    {"id": "ACT-27", "label": "Threat model per feature",
     "attrs": {"name": "Threat model per feature", "domain_id": "D-07", "sub_domain_id": "D-07.1",
               "corpus_reg_req": "D-07.1: 7.1.1, 7.1.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.7 L216 row 'Threat model per feature' (Dev = R/A composite)"]},
    {"id": "ACT-28", "label": "Code review",
     "attrs": {"name": "Code review", "domain_id": "D-07", "sub_domain_id": "D-07.2",
               "corpus_reg_req": "D-07.2: 7.2.1 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.7 L217 row 'Code review' (Dev = R/A composite)"]},
    {"id": "ACT-29", "label": "Security testing in CI/CD (SAST/DAST/SCA via Snyk)",
     "attrs": {"name": "Security testing in CI/CD (SAST/DAST/SCA via Snyk)",
               "domain_id": "D-07", "sub_domain_id": "D-07.3",
               "corpus_reg_req": "D-07.3: 7.3.2 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.7 L218 row 'Security testing in CI/CD (SAST/DAST/SCA via Snyk)'"]},
    {"id": "ACT-30", "label": "Change approval (CAB) for production releases",
     "attrs": {"name": "Change approval (CAB) for production releases",
               "domain_id": "D-07", "sub_domain_id": "D-07.4",
               "corpus_reg_req": "D-07.4: 7.4.1 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.7 L219 row 'Change approval (CAB) for production releases'"]},
    # --- §4.8 Human Factors (D-08) — 5 activities (3 active + ACT-33 R/A composite + ACT-34/35 inactive)
    {"id": "ACT-31", "label": "Annual security awareness training (D-08.1)",
     "attrs": {"name": "Annual security awareness training (D-08.1)",
               "domain_id": "D-08", "sub_domain_id": "D-08.1",
               "corpus_reg_req": "D-08.1: 8.1.1, 8.1.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.8 L225 row 'Annual security awareness training (D-08.1)'"]},
    {"id": "ACT-32", "label": "Role-specific training — secure coding for developers (D-08.2)",
     "attrs": {"name": "Role-specific training — secure coding for developers (D-08.2)",
               "domain_id": "D-08", "sub_domain_id": "D-08.2",
               "corpus_reg_req": "D-08.2: 8.2.1, 8.2.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.8 L226 row 'Role-specific training — secure coding for developers (D-08.2)'"]},
    {"id": "ACT-33", "label": "Role-specific training — DPO competence refresh (D-08.2)",
     "attrs": {"name": "Role-specific training — DPO competence refresh (D-08.2)",
               "domain_id": "D-08", "sub_domain_id": "D-08.2",
               "corpus_reg_req": "D-08.2: 8.2.1, 8.2.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.8 L227 row 'Role-specific training — DPO competence refresh (D-08.2)' (DPO = R/A composite)"]},
    {"id": "ACT-34", "label": "Board cybersecurity briefings (D-08.3)",
     "attrs": {"name": "Board cybersecurity briefings (D-08.3)",
               "domain_id": "D-08", "sub_domain_id": "D-08.3",
               "corpus_reg_req": "D-08.3: INACTIVE", "active": False},
     "source": ["Doc07 §4.8 L228 row 'Board cybersecurity briefings (D-08.3)' (all '—' placeholder, D-08.3 INACTIVE for NIS2 + DORA inapplicability)"]},
    {"id": "ACT-35", "label": "Quarterly informal cybersecurity briefing to the 2 founders",
     "attrs": {"name": "Quarterly informal cybersecurity briefing to the 2 founders",
               "domain_id": "D-08", "sub_domain_id": "D-08.3",
               "corpus_reg_req": "D-08.3: INACTIVE — no derived GDPR/CRA req_id", "active": False},
     "source": ["Doc07 §4.8 L238 best-practice placeholder row 'Quarterly informal cybersecurity briefing to the 2 founders' (CISO=R, Board=A)"]},
    # --- §4.9 Governance (D-09) — 5 activities
    {"id": "ACT-36", "label": "Approve security policies",
     "attrs": {"name": "Approve security policies", "domain_id": "D-09", "sub_domain_id": "D-09.1",
               "corpus_reg_req": "D-09.1: 9.1.1, 9.1.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.9 L246 row 'Approve security policies'"]},
    {"id": "ACT-37", "label": "Conduct risk assessments (annual + per-feature)",
     "attrs": {"name": "Conduct risk assessments (annual + per-feature)",
               "domain_id": "D-09", "sub_domain_id": "D-09.2",
               "corpus_reg_req": "D-09.2: 9.2.1, 9.2.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.9 L247 row 'Conduct risk assessments (annual + per-feature)'"]},
    {"id": "ACT-38", "label": "Maintain asset inventory",
     "attrs": {"name": "Maintain asset inventory", "domain_id": "D-09", "sub_domain_id": "D-09.3",
               "corpus_reg_req": "D-09.3: 9.3.2 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.9 L248 row 'Maintain asset inventory'"]},
    {"id": "ACT-39", "label": "Maintain RoPA (Art. 30 GDPR)",
     "attrs": {"name": "Maintain RoPA (Art. 30 GDPR)", "domain_id": "D-09", "sub_domain_id": "D-09.4",
               "corpus_reg_req": "D-09.4: 9.4.1, 9.4.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.9 L249 row 'Maintain RoPA (Art. 30 GDPR)'"]},
    {"id": "ACT-40", "label": "Maintain CRA Annex VII technical documentation",
     "attrs": {"name": "Maintain CRA Annex VII technical documentation",
               "domain_id": "D-09", "sub_domain_id": "D-09.4",
               "corpus_reg_req": "D-09.4: 9.4.1, 9.4.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.9 L250 row 'Maintain CRA Annex VII technical documentation'"]},
    # --- §4.10 Monitoring & Audit (D-10) — 3 activities
    {"id": "ACT-41", "label": "Continuous security monitoring (Datadog; SIEM-light)",
     "attrs": {"name": "Continuous security monitoring (Datadog; SIEM-light)",
               "domain_id": "D-10", "sub_domain_id": "D-10.1",
               "corpus_reg_req": "D-10.1: 10.1.1, 10.1.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.10 L256 row 'Continuous security monitoring (Datadog; SIEM-light)'"]},
    {"id": "ACT-42", "label": "Audit-log retention",
     "attrs": {"name": "Audit-log retention", "domain_id": "D-10", "sub_domain_id": "D-10.2",
               "corpus_reg_req": "D-10.2: 10.2.1, 10.2.2 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.10 L257 row 'Audit-log retention'"]},
    {"id": "ACT-43", "label": "Annual compliance testing",
     "attrs": {"name": "Annual compliance testing", "domain_id": "D-10", "sub_domain_id": "D-10.3",
               "corpus_reg_req": "D-10.3: 10.3.1, 10.3.3 (GDPR + CRA)", "active": True},
     "source": ["Doc07 §4.10 L258 row 'Annual compliance testing'"]},
]
assert len(RACI_ACTIVITIES) == 43, f"RACI_ACTIVITIES drift: {len(RACI_ACTIVITIES)}"
_active_acts = sum(1 for a in RACI_ACTIVITIES if a["attrs"]["active"])
assert _active_acts == 41, f"active RACI activities drift: {_active_acts} (expected 41)"


# Per Doc07 §4.x RACI tables: 206 RACI edges (one per non-'—' cell; composite
# 'R/A' cells split into 2 edges). Each entry is a tuple
#   (role_id, activity_id, letter, source_section)
# where letter ∈ {R, A, C, I}. attr 'activity_id' is added on each emitted
# link for traceability (orchestrator brief §A).
RACI_EDGES = [
    # --- §4.1 Data Protection (4 rows × non-'—' cells)
    ("ROLE-DPO",  "ACT-01", "C", "Doc07 §4.1 L160 row 'Encrypt personal data at rest', col DPO"),
    ("ROLE-CISO", "ACT-01", "A", "Doc07 §4.1 L160 row 'Encrypt personal data at rest', col CISO"),
    ("ROLE-DEV",  "ACT-01", "R", "Doc07 §4.1 L160 row 'Encrypt personal data at rest', col Dev"),
    ("ROLE-LEGAL","ACT-01", "I", "Doc07 §4.1 L160 row 'Encrypt personal data at rest', col Legal"),
    ("ROLE-BOARD","ACT-01", "I", "Doc07 §4.1 L160 row 'Encrypt personal data at rest', col Board"),
    ("ROLE-DPO",  "ACT-02", "C", "Doc07 §4.1 L161 row 'Manage encryption keys', col DPO"),
    ("ROLE-CISO", "ACT-02", "A", "Doc07 §4.1 L161 row 'Manage encryption keys', col CISO"),
    ("ROLE-DEV",  "ACT-02", "R", "Doc07 §4.1 L161 row 'Manage encryption keys', col Dev"),
    ("ROLE-LEGAL","ACT-02", "I", "Doc07 §4.1 L161 row 'Manage encryption keys', col Legal"),
    ("ROLE-BOARD","ACT-02", "I", "Doc07 §4.1 L161 row 'Manage encryption keys', col Board"),
    ("ROLE-DPO",  "ACT-03", "R", "Doc07 §4.1 L162 row 'Notify DPA within 72h (Art. 33 GDPR)', col DPO"),
    ("ROLE-CISO", "ACT-03", "A", "Doc07 §4.1 L162 row 'Notify DPA within 72h (Art. 33 GDPR)', col CISO"),
    ("ROLE-DEV",  "ACT-03", "C", "Doc07 §4.1 L162 row 'Notify DPA within 72h (Art. 33 GDPR)', col Dev"),
    ("ROLE-LEGAL","ACT-03", "C", "Doc07 §4.1 L162 row 'Notify DPA within 72h (Art. 33 GDPR)', col Legal"),
    ("ROLE-BOARD","ACT-03", "I", "Doc07 §4.1 L162 row 'Notify DPA within 72h (Art. 33 GDPR)', col Board"),
    ("ROLE-DPO",  "ACT-04", "R", "Doc07 §4.1 L163 row 'Conduct DPIA (Art. 35 GDPR)', col DPO"),
    ("ROLE-CISO", "ACT-04", "C", "Doc07 §4.1 L163 row 'Conduct DPIA (Art. 35 GDPR)', col CISO"),
    ("ROLE-DEV",  "ACT-04", "C", "Doc07 §4.1 L163 row 'Conduct DPIA (Art. 35 GDPR)', col Dev"),
    ("ROLE-LEGAL","ACT-04", "A", "Doc07 §4.1 L163 row 'Conduct DPIA (Art. 35 GDPR)', col Legal"),
    ("ROLE-BOARD","ACT-04", "I", "Doc07 §4.1 L163 row 'Conduct DPIA (Art. 35 GDPR)', col Board"),
    # --- §4.2 Vulnerability Management (4 rows)
    ("ROLE-DPO",  "ACT-05", "I", "Doc07 §4.2 L169 row 'Run vulnerability scans', col DPO"),
    ("ROLE-CISO", "ACT-05", "A", "Doc07 §4.2 L169 row 'Run vulnerability scans', col CISO"),
    ("ROLE-DEV",  "ACT-05", "R", "Doc07 §4.2 L169 row 'Run vulnerability scans', col Dev"),
    ("ROLE-BOARD","ACT-05", "I", "Doc07 §4.2 L169 row 'Run vulnerability scans', col Board"),
    ("ROLE-DPO",  "ACT-06", "I", "Doc07 §4.2 L170 row 'Apply critical patches', col DPO"),
    ("ROLE-CISO", "ACT-06", "A", "Doc07 §4.2 L170 row 'Apply critical patches', col CISO"),
    ("ROLE-DEV",  "ACT-06", "R", "Doc07 §4.2 L170 row 'Apply critical patches', col Dev"),
    ("ROLE-BOARD","ACT-06", "I", "Doc07 §4.2 L170 row 'Apply critical patches', col Board"),
    ("ROLE-DPO",  "ACT-07", "I", "Doc07 §4.2 L171 row 'Annual penetration testing', col DPO"),
    ("ROLE-CISO", "ACT-07", "A", "Doc07 §4.2 L171 row 'Annual penetration testing', col CISO"),
    ("ROLE-DEV",  "ACT-07", "R", "Doc07 §4.2 L171 row 'Annual penetration testing', col Dev"),
    ("ROLE-LEGAL","ACT-07", "I", "Doc07 §4.2 L171 row 'Annual penetration testing', col Legal"),
    ("ROLE-BOARD","ACT-07", "I", "Doc07 §4.2 L171 row 'Annual penetration testing', col Board"),
    ("ROLE-DPO",  "ACT-08", "C", "Doc07 §4.2 L172 row 'Operate CVD / security.txt', col DPO"),
    ("ROLE-CISO", "ACT-08", "A", "Doc07 §4.2 L172 row 'Operate CVD / security.txt', col CISO"),
    ("ROLE-DEV",  "ACT-08", "R", "Doc07 §4.2 L172 row 'Operate CVD / security.txt', col Dev"),
    ("ROLE-LEGAL","ACT-08", "I", "Doc07 §4.2 L172 row 'Operate CVD / security.txt', col Legal"),
    ("ROLE-BOARD","ACT-08", "I", "Doc07 §4.2 L172 row 'Operate CVD / security.txt', col Board"),
    # --- §4.3 Access Control (4 rows)
    ("ROLE-DPO",  "ACT-09", "C", "Doc07 §4.3 L178 row 'Manage IAM', col DPO"),
    ("ROLE-CISO", "ACT-09", "A", "Doc07 §4.3 L178 row 'Manage IAM', col CISO"),
    ("ROLE-DEV",  "ACT-09", "R", "Doc07 §4.3 L178 row 'Manage IAM', col Dev"),
    ("ROLE-LEGAL","ACT-09", "I", "Doc07 §4.3 L178 row 'Manage IAM', col Legal"),
    ("ROLE-BOARD","ACT-09", "I", "Doc07 §4.3 L178 row 'Manage IAM', col Board"),
    ("ROLE-DPO",  "ACT-10", "C", "Doc07 §4.3 L179 row 'Enforce MFA', col DPO"),
    ("ROLE-CISO", "ACT-10", "A", "Doc07 §4.3 L179 row 'Enforce MFA', col CISO"),
    ("ROLE-DEV",  "ACT-10", "R", "Doc07 §4.3 L179 row 'Enforce MFA', col Dev"),
    ("ROLE-BOARD","ACT-10", "I", "Doc07 §4.3 L179 row 'Enforce MFA', col Board"),
    ("ROLE-DPO",  "ACT-11", "C", "Doc07 §4.3 L180 row 'Quarterly access review', col DPO"),
    ("ROLE-CISO", "ACT-11", "A", "Doc07 §4.3 L180 row 'Quarterly access review', col CISO"),
    ("ROLE-DEV",  "ACT-11", "R", "Doc07 §4.3 L180 row 'Quarterly access review', col Dev"),
    ("ROLE-LEGAL","ACT-11", "I", "Doc07 §4.3 L180 row 'Quarterly access review', col Legal"),
    ("ROLE-BOARD","ACT-11", "I", "Doc07 §4.3 L180 row 'Quarterly access review', col Board"),
    ("ROLE-DPO",  "ACT-12", "C", "Doc07 §4.3 L181 row 'Offboarding', col DPO"),
    ("ROLE-CISO", "ACT-12", "A", "Doc07 §4.3 L181 row 'Offboarding', col CISO"),
    ("ROLE-DEV",  "ACT-12", "R", "Doc07 §4.3 L181 row 'Offboarding', col Dev"),
    ("ROLE-LEGAL","ACT-12", "I", "Doc07 §4.3 L181 row 'Offboarding', col Legal"),
    ("ROLE-HR",   "ACT-12", "C", "Doc07 §4.3 L181 row 'Offboarding', col HR"),
    ("ROLE-BOARD","ACT-12", "I", "Doc07 §4.3 L181 row 'Offboarding', col Board"),
    # --- §4.4 Incident Response (6 rows)
    ("ROLE-DPO",  "ACT-13", "I", "Doc07 §4.4 L187 row 'Detect incident', col DPO"),
    ("ROLE-CISO", "ACT-13", "A", "Doc07 §4.4 L187 row 'Detect incident', col CISO"),
    ("ROLE-DEV",  "ACT-13", "R", "Doc07 §4.4 L187 row 'Detect incident', col Dev"),
    ("ROLE-BOARD","ACT-13", "I", "Doc07 §4.4 L187 row 'Detect incident', col Board"),
    ("ROLE-DPO",  "ACT-14", "I", "Doc07 §4.4 L188 row 'Contain incident', col DPO"),
    ("ROLE-CISO", "ACT-14", "A", "Doc07 §4.4 L188 row 'Contain incident', col CISO"),
    ("ROLE-DEV",  "ACT-14", "R", "Doc07 §4.4 L188 row 'Contain incident', col Dev"),
    ("ROLE-LEGAL","ACT-14", "C", "Doc07 §4.4 L188 row 'Contain incident', col Legal"),
    ("ROLE-BOARD","ACT-14", "I", "Doc07 §4.4 L188 row 'Contain incident', col Board"),
    ("ROLE-DPO",  "ACT-15", "R", "Doc07 §4.4 L189 row 'Notify authorities', col DPO"),
    ("ROLE-CISO", "ACT-15", "A", "Doc07 §4.4 L189 row 'Notify authorities', col CISO"),
    ("ROLE-DEV",  "ACT-15", "C", "Doc07 §4.4 L189 row 'Notify authorities', col Dev"),
    ("ROLE-LEGAL","ACT-15", "C", "Doc07 §4.4 L189 row 'Notify authorities', col Legal"),
    ("ROLE-BOARD","ACT-15", "I", "Doc07 §4.4 L189 row 'Notify authorities', col Board"),
    ("ROLE-DPO",  "ACT-16", "R", "Doc07 §4.4 L190 row 'Notify controllers', col DPO"),
    ("ROLE-CISO", "ACT-16", "A", "Doc07 §4.4 L190 row 'Notify controllers', col CISO"),
    ("ROLE-DEV",  "ACT-16", "C", "Doc07 §4.4 L190 row 'Notify controllers', col Dev"),
    ("ROLE-LEGAL","ACT-16", "C", "Doc07 §4.4 L190 row 'Notify controllers', col Legal"),
    ("ROLE-BOARD","ACT-16", "I", "Doc07 §4.4 L190 row 'Notify controllers', col Board"),
    ("ROLE-DPO",  "ACT-17", "I", "Doc07 §4.4 L191 row 'Recover systems', col DPO"),
    ("ROLE-CISO", "ACT-17", "A", "Doc07 §4.4 L191 row 'Recover systems', col CISO"),
    ("ROLE-DEV",  "ACT-17", "R", "Doc07 §4.4 L191 row 'Recover systems', col Dev"),
    ("ROLE-LEGAL","ACT-17", "I", "Doc07 §4.4 L191 row 'Recover systems', col Legal"),
    ("ROLE-BOARD","ACT-17", "I", "Doc07 §4.4 L191 row 'Recover systems', col Board"),
    ("ROLE-DPO",  "ACT-18", "C", "Doc07 §4.4 L192 row 'Post-incident review', col DPO"),
    ("ROLE-CISO", "ACT-18", "A", "Doc07 §4.4 L192 row 'Post-incident review', col CISO"),
    ("ROLE-DEV",  "ACT-18", "R", "Doc07 §4.4 L192 row 'Post-incident review', col Dev"),
    ("ROLE-LEGAL","ACT-18", "I", "Doc07 §4.4 L192 row 'Post-incident review', col Legal"),
    ("ROLE-BOARD","ACT-18", "I", "Doc07 §4.4 L192 row 'Post-incident review', col Board"),
    # --- §4.5 Data Lifecycle (4 rows)
    ("ROLE-DPO",  "ACT-19", "R", "Doc07 §4.5 L198 row 'Enforce data minimisation', col DPO"),
    ("ROLE-CISO", "ACT-19", "A", "Doc07 §4.5 L198 row 'Enforce data minimisation', col CISO"),
    ("ROLE-DEV",  "ACT-19", "C", "Doc07 §4.5 L198 row 'Enforce data minimisation', col Dev"),
    ("ROLE-LEGAL","ACT-19", "C", "Doc07 §4.5 L198 row 'Enforce data minimisation', col Legal"),
    ("ROLE-BOARD","ACT-19", "I", "Doc07 §4.5 L198 row 'Enforce data minimisation', col Board"),
    ("ROLE-DPO",  "ACT-20", "R", "Doc07 §4.5 L199 row 'Manage retention policies', col DPO"),
    ("ROLE-CISO", "ACT-20", "A", "Doc07 §4.5 L199 row 'Manage retention policies', col CISO"),
    ("ROLE-DEV",  "ACT-20", "C", "Doc07 §4.5 L199 row 'Manage retention policies', col Dev"),
    ("ROLE-LEGAL","ACT-20", "C", "Doc07 §4.5 L199 row 'Manage retention policies', col Legal"),
    ("ROLE-BOARD","ACT-20", "I", "Doc07 §4.5 L199 row 'Manage retention policies', col Board"),
    ("ROLE-DPO",  "ACT-21", "R", "Doc07 §4.5 L200 row 'Process erasure requests', col DPO"),
    ("ROLE-CISO", "ACT-21", "C", "Doc07 §4.5 L200 row 'Process erasure requests', col CISO"),
    ("ROLE-DEV",  "ACT-21", "A", "Doc07 §4.5 L200 row 'Process erasure requests', col Dev"),
    ("ROLE-LEGAL","ACT-21", "C", "Doc07 §4.5 L200 row 'Process erasure requests', col Legal"),
    ("ROLE-BOARD","ACT-21", "I", "Doc07 §4.5 L200 row 'Process erasure requests', col Board"),
    ("ROLE-DPO",  "ACT-22", "R", "Doc07 §4.5 L201 row 'Process portability requests', col DPO"),
    ("ROLE-CISO", "ACT-22", "C", "Doc07 §4.5 L201 row 'Process portability requests', col CISO"),
    ("ROLE-DEV",  "ACT-22", "A", "Doc07 §4.5 L201 row 'Process portability requests', col Dev"),
    ("ROLE-LEGAL","ACT-22", "C", "Doc07 §4.5 L201 row 'Process portability requests', col Legal"),
    ("ROLE-BOARD","ACT-22", "I", "Doc07 §4.5 L201 row 'Process portability requests', col Board"),
    # --- §4.6 Supply Chain (4 rows)
    ("ROLE-DPO",  "ACT-23", "C", "Doc07 §4.6 L207 row 'Assess vendor security', col DPO"),
    ("ROLE-CISO", "ACT-23", "A", "Doc07 §4.6 L207 row 'Assess vendor security', col CISO"),
    ("ROLE-DEV",  "ACT-23", "R", "Doc07 §4.6 L207 row 'Assess vendor security', col Dev"),
    ("ROLE-LEGAL","ACT-23", "C", "Doc07 §4.6 L207 row 'Assess vendor security', col Legal"),
    ("ROLE-BOARD","ACT-23", "I", "Doc07 §4.6 L207 row 'Assess vendor security', col Board"),
    ("ROLE-DPO",  "ACT-24", "I", "Doc07 §4.6 L208 row 'Maintain SBOM', col DPO"),
    ("ROLE-CISO", "ACT-24", "A", "Doc07 §4.6 L208 row 'Maintain SBOM', col CISO"),
    ("ROLE-DEV",  "ACT-24", "R", "Doc07 §4.6 L208 row 'Maintain SBOM', col Dev"),
    ("ROLE-BOARD","ACT-24", "I", "Doc07 §4.6 L208 row 'Maintain SBOM', col Board"),
    ("ROLE-DPO",  "ACT-25", "R", "Doc07 §4.6 L209 row 'Manage DPA contracts with B2B controllers', col DPO"),
    ("ROLE-CISO", "ACT-25", "C", "Doc07 §4.6 L209 row 'Manage DPA contracts with B2B controllers', col CISO"),
    ("ROLE-DEV",  "ACT-25", "I", "Doc07 §4.6 L209 row 'Manage DPA contracts with B2B controllers', col Dev"),
    ("ROLE-LEGAL","ACT-25", "A", "Doc07 §4.6 L209 row 'Manage DPA contracts with B2B controllers', col Legal"),
    ("ROLE-BOARD","ACT-25", "I", "Doc07 §4.6 L209 row 'Manage DPA contracts with B2B controllers', col Board"),
    ("ROLE-DPO",  "ACT-26", "R", "Doc07 §4.6 L210 row 'Manage DPA acceptance from subprocessor vendors', col DPO"),
    ("ROLE-CISO", "ACT-26", "A", "Doc07 §4.6 L210 row 'Manage DPA acceptance from subprocessor vendors', col CISO"),
    ("ROLE-DEV",  "ACT-26", "I", "Doc07 §4.6 L210 row 'Manage DPA acceptance from subprocessor vendors', col Dev"),
    ("ROLE-LEGAL","ACT-26", "C", "Doc07 §4.6 L210 row 'Manage DPA acceptance from subprocessor vendors', col Legal"),
    ("ROLE-BOARD","ACT-26", "I", "Doc07 §4.6 L210 row 'Manage DPA acceptance from subprocessor vendors', col Board"),
    # --- §4.7 Secure Development (4 rows; ACT-27 Dev = R/A → 2 edges; ACT-28 Dev = R/A → 2 edges)
    ("ROLE-DPO",  "ACT-27", "C", "Doc07 §4.7 L216 row 'Threat model per feature', col DPO"),
    ("ROLE-CISO", "ACT-27", "C", "Doc07 §4.7 L216 row 'Threat model per feature', col CISO"),
    ("ROLE-DEV",  "ACT-27", "R", "Doc07 §4.7 L216 row 'Threat model per feature', col Dev (composite R/A → split)"),
    ("ROLE-DEV",  "ACT-27", "A", "Doc07 §4.7 L216 row 'Threat model per feature', col Dev (composite R/A → split)"),
    ("ROLE-LEGAL","ACT-27", "I", "Doc07 §4.7 L216 row 'Threat model per feature', col Legal"),
    ("ROLE-BOARD","ACT-27", "I", "Doc07 §4.7 L216 row 'Threat model per feature', col Board"),
    ("ROLE-DPO",  "ACT-28", "I", "Doc07 §4.7 L217 row 'Code review', col DPO"),
    ("ROLE-CISO", "ACT-28", "C", "Doc07 §4.7 L217 row 'Code review', col CISO"),
    ("ROLE-DEV",  "ACT-28", "R", "Doc07 §4.7 L217 row 'Code review', col Dev (composite R/A → split)"),
    ("ROLE-DEV",  "ACT-28", "A", "Doc07 §4.7 L217 row 'Code review', col Dev (composite R/A → split)"),
    ("ROLE-BOARD","ACT-28", "I", "Doc07 §4.7 L217 row 'Code review', col Board"),
    ("ROLE-DPO",  "ACT-29", "I", "Doc07 §4.7 L218 row 'Security testing in CI/CD', col DPO"),
    ("ROLE-CISO", "ACT-29", "A", "Doc07 §4.7 L218 row 'Security testing in CI/CD', col CISO"),
    ("ROLE-DEV",  "ACT-29", "R", "Doc07 §4.7 L218 row 'Security testing in CI/CD', col Dev"),
    ("ROLE-BOARD","ACT-29", "I", "Doc07 §4.7 L218 row 'Security testing in CI/CD', col Board"),
    ("ROLE-DPO",  "ACT-30", "I", "Doc07 §4.7 L219 row 'Change approval (CAB)', col DPO"),
    ("ROLE-CISO", "ACT-30", "C", "Doc07 §4.7 L219 row 'Change approval (CAB)', col CISO"),
    ("ROLE-DEV",  "ACT-30", "R", "Doc07 §4.7 L219 row 'Change approval (CAB)', col Dev"),
    ("ROLE-LEGAL","ACT-30", "I", "Doc07 §4.7 L219 row 'Change approval (CAB)', col Legal"),
    ("ROLE-BOARD","ACT-30", "A", "Doc07 §4.7 L219 row 'Change approval (CAB)', col Board"),
    # --- §4.8 Human Factors (3 active rows + ACT-33 DPO = R/A composite → 2 edges + ACT-34/35 inactive, no edges)
    ("ROLE-DPO",  "ACT-31", "C", "Doc07 §4.8 L225 row 'Annual security awareness training', col DPO"),
    ("ROLE-CISO", "ACT-31", "A", "Doc07 §4.8 L225 row 'Annual security awareness training', col CISO"),
    ("ROLE-DEV",  "ACT-31", "I", "Doc07 §4.8 L225 row 'Annual security awareness training', col Dev"),
    ("ROLE-LEGAL","ACT-31", "I", "Doc07 §4.8 L225 row 'Annual security awareness training', col Legal"),
    ("ROLE-HR",   "ACT-31", "R", "Doc07 §4.8 L225 row 'Annual security awareness training', col HR"),
    ("ROLE-BOARD","ACT-31", "I", "Doc07 §4.8 L225 row 'Annual security awareness training', col Board"),
    ("ROLE-DPO",  "ACT-32", "C", "Doc07 §4.8 L226 row 'Role-specific training — secure coding for developers', col DPO"),
    ("ROLE-CISO", "ACT-32", "A", "Doc07 §4.8 L226 row 'Role-specific training — secure coding for developers', col CISO"),
    ("ROLE-DEV",  "ACT-32", "R", "Doc07 §4.8 L226 row 'Role-specific training — secure coding for developers', col Dev"),
    ("ROLE-HR",   "ACT-32", "I", "Doc07 §4.8 L226 row 'Role-specific training — secure coding for developers', col HR"),
    ("ROLE-BOARD","ACT-32", "I", "Doc07 §4.8 L226 row 'Role-specific training — secure coding for developers', col Board"),
    ("ROLE-DPO",  "ACT-33", "R", "Doc07 §4.8 L227 row 'Role-specific training — DPO competence refresh', col DPO (composite R/A → split)"),
    ("ROLE-DPO",  "ACT-33", "A", "Doc07 §4.8 L227 row 'Role-specific training — DPO competence refresh', col DPO (composite R/A → split)"),
    ("ROLE-CISO", "ACT-33", "C", "Doc07 §4.8 L227 row 'Role-specific training — DPO competence refresh', col CISO"),
    ("ROLE-LEGAL","ACT-33", "C", "Doc07 §4.8 L227 row 'Role-specific training — DPO competence refresh', col Legal"),
    ("ROLE-HR",   "ACT-33", "I", "Doc07 §4.8 L227 row 'Role-specific training — DPO competence refresh', col HR"),
    ("ROLE-BOARD","ACT-33", "I", "Doc07 §4.8 L227 row 'Role-specific training — DPO competence refresh', col Board"),
    # ACT-34 (L228 all-'—' placeholder) is INACTIVE → no RACI edges emitted.
    # ACT-35 (L238 best-practice) is also marked active=False at the activity-node
    # level (D-08.3 INACTIVE for TinyTask; non-derivation per Doc07 §0/§7), but the
    # 2 non-'—' cells (CISO=R, Board=A) of the §4.8 best-practice sub-table are
    # still emitted as RACI edges to preserve the verbatim Doc07 §4.8 matrix —
    # total RACI_EDGES = 206 matches the brief and §4.8 row 4 cell content.
    ("ROLE-CISO", "ACT-35", "R", "Doc07 §4.8 L238 best-practice row 'Quarterly informal cybersecurity briefing', col CISO"),
    ("ROLE-BOARD","ACT-35", "A", "Doc07 §4.8 L238 best-practice row 'Quarterly informal cybersecurity briefing', col Board"),
    # --- §4.9 Governance (5 rows)
    ("ROLE-DPO",  "ACT-36", "C", "Doc07 §4.9 L246 row 'Approve security policies', col DPO"),
    ("ROLE-CISO", "ACT-36", "C", "Doc07 §4.9 L246 row 'Approve security policies', col CISO"),
    ("ROLE-DEV",  "ACT-36", "C", "Doc07 §4.9 L246 row 'Approve security policies', col Dev"),
    ("ROLE-LEGAL","ACT-36", "C", "Doc07 §4.9 L246 row 'Approve security policies', col Legal"),
    ("ROLE-HR",   "ACT-36", "C", "Doc07 §4.9 L246 row 'Approve security policies', col HR"),
    ("ROLE-BOARD","ACT-36", "A", "Doc07 §4.9 L246 row 'Approve security policies', col Board"),
    ("ROLE-DPO",  "ACT-37", "R", "Doc07 §4.9 L247 row 'Conduct risk assessments', col DPO"),
    ("ROLE-CISO", "ACT-37", "A", "Doc07 §4.9 L247 row 'Conduct risk assessments', col CISO"),
    ("ROLE-DEV",  "ACT-37", "C", "Doc07 §4.9 L247 row 'Conduct risk assessments', col Dev"),
    ("ROLE-LEGAL","ACT-37", "C", "Doc07 §4.9 L247 row 'Conduct risk assessments', col Legal"),
    ("ROLE-HR",   "ACT-37", "I", "Doc07 §4.9 L247 row 'Conduct risk assessments', col HR"),
    ("ROLE-BOARD","ACT-37", "I", "Doc07 §4.9 L247 row 'Conduct risk assessments', col Board"),
    ("ROLE-DPO",  "ACT-38", "C", "Doc07 §4.9 L248 row 'Maintain asset inventory', col DPO"),
    ("ROLE-CISO", "ACT-38", "A", "Doc07 §4.9 L248 row 'Maintain asset inventory', col CISO"),
    ("ROLE-DEV",  "ACT-38", "R", "Doc07 §4.9 L248 row 'Maintain asset inventory', col Dev"),
    ("ROLE-LEGAL","ACT-38", "I", "Doc07 §4.9 L248 row 'Maintain asset inventory', col Legal"),
    ("ROLE-BOARD","ACT-38", "I", "Doc07 §4.9 L248 row 'Maintain asset inventory', col Board"),
    ("ROLE-DPO",  "ACT-39", "R", "Doc07 §4.9 L249 row 'Maintain RoPA', col DPO"),
    ("ROLE-CISO", "ACT-39", "A", "Doc07 §4.9 L249 row 'Maintain RoPA', col CISO"),
    ("ROLE-DEV",  "ACT-39", "C", "Doc07 §4.9 L249 row 'Maintain RoPA', col Dev"),
    ("ROLE-LEGAL","ACT-39", "C", "Doc07 §4.9 L249 row 'Maintain RoPA', col Legal"),
    ("ROLE-BOARD","ACT-39", "I", "Doc07 §4.9 L249 row 'Maintain RoPA', col Board"),
    ("ROLE-DPO",  "ACT-40", "C", "Doc07 §4.9 L250 row 'Maintain CRA Annex VII technical documentation', col DPO"),
    ("ROLE-CISO", "ACT-40", "A", "Doc07 §4.9 L250 row 'Maintain CRA Annex VII technical documentation', col CISO"),
    ("ROLE-DEV",  "ACT-40", "R", "Doc07 §4.9 L250 row 'Maintain CRA Annex VII technical documentation', col Dev"),
    ("ROLE-LEGAL","ACT-40", "C", "Doc07 §4.9 L250 row 'Maintain CRA Annex VII technical documentation', col Legal"),
    ("ROLE-BOARD","ACT-40", "I", "Doc07 §4.9 L250 row 'Maintain CRA Annex VII technical documentation', col Board"),
    # --- §4.10 Monitoring & Audit (3 rows)
    ("ROLE-DPO",  "ACT-41", "I", "Doc07 §4.10 L256 row 'Continuous security monitoring', col DPO"),
    ("ROLE-CISO", "ACT-41", "A", "Doc07 §4.10 L256 row 'Continuous security monitoring', col CISO"),
    ("ROLE-DEV",  "ACT-41", "R", "Doc07 §4.10 L256 row 'Continuous security monitoring', col Dev"),
    ("ROLE-BOARD","ACT-41", "I", "Doc07 §4.10 L256 row 'Continuous security monitoring', col Board"),
    ("ROLE-DPO",  "ACT-42", "C", "Doc07 §4.10 L257 row 'Audit-log retention', col DPO"),
    ("ROLE-CISO", "ACT-42", "A", "Doc07 §4.10 L257 row 'Audit-log retention', col CISO"),
    ("ROLE-DEV",  "ACT-42", "R", "Doc07 §4.10 L257 row 'Audit-log retention', col Dev"),
    ("ROLE-LEGAL","ACT-42", "I", "Doc07 §4.10 L257 row 'Audit-log retention', col Legal"),
    ("ROLE-BOARD","ACT-42", "I", "Doc07 §4.10 L257 row 'Audit-log retention', col Board"),
    ("ROLE-DPO",  "ACT-43", "C", "Doc07 §4.10 L258 row 'Annual compliance testing', col DPO"),
    ("ROLE-CISO", "ACT-43", "A", "Doc07 §4.10 L258 row 'Annual compliance testing', col CISO"),
    ("ROLE-DEV",  "ACT-43", "R", "Doc07 §4.10 L258 row 'Annual compliance testing', col Dev"),
    ("ROLE-LEGAL","ACT-43", "I", "Doc07 §4.10 L258 row 'Annual compliance testing', col Legal"),
    ("ROLE-BOARD","ACT-43", "I", "Doc07 §4.10 L258 row 'Annual compliance testing', col Board"),
]
assert len(RACI_EDGES) == 206, f"RACI_EDGES drift: {len(RACI_EDGES)} (expected 206)"


# Per Doc07 §9.2 (activity → sub-domain mapping): 35 rows. Some rows merge
# multiple §4.x activities onto one sub-domain (collapsed entries), so 35
# APPLIES_TO edges come from 35 §9.2 rows (not 1-per-activity). Each tuple is
# (activity_id, sub_domain_id, source_section). Where §9.2 merges multiple
# ACTs (e.g. IAM/offboarding/access review → D-03.1), the edge is emitted
# from the first (representative) activity in the §9.2 row.
APPLIES_TO_EDGES = [
    # §9.2 row 1
    ("ACT-01", "D-01.1", "Doc07 §9.2 row 1: 'Encrypt personal data at rest → D-01.1'"),
    # §9.2 row 2
    ("ACT-02", "D-01.3", "Doc07 §9.2 row 2: 'Manage encryption keys → D-01.3'"),
    # §9.2 row 3 (collapsed: Notify DPA / Notify controllers → D-04.3; representative = ACT-03)
    ("ACT-03", "D-04.3", "Doc07 §9.2 row 3: 'Notify DPA / Notify controllers → D-04.3' (collapsed from ACT-03, ACT-15, ACT-16)"),
    # §9.2 row 4
    ("ACT-04", "D-09.2", "Doc07 §9.2 row 4: 'Conduct DPIA → D-09.2'"),
    # §9.2 row 5
    ("ACT-05", "D-02.1", "Doc07 §9.2 row 5: 'Vulnerability scans → D-02.1'"),
    # §9.2 row 6
    ("ACT-06", "D-02.2", "Doc07 §9.2 row 6: 'Patch management → D-02.2'"),
    # §9.2 row 7
    ("ACT-07", "D-02.4", "Doc07 §9.2 row 7: 'Penetration testing → D-02.4'"),
    # §9.2 row 8
    ("ACT-08", "D-02.3", "Doc07 §9.2 row 8: 'CVD / security.txt → D-02.3'"),
    # §9.2 row 9 (collapsed: IAM / offboarding / access review → D-03.1; representative = ACT-09)
    ("ACT-09", "D-03.1", "Doc07 §9.2 row 9: 'IAM / offboarding / access review → D-03.1' (collapsed from ACT-09, ACT-11, ACT-12)"),
    # §9.2 row 10
    ("ACT-10", "D-03.2", "Doc07 §9.2 row 10: 'MFA → D-03.2'"),
    # §9.2 row 11
    ("ACT-13", "D-04.1", "Doc07 §9.2 row 11: 'Detect incident → D-04.1'"),
    # §9.2 row 12
    ("ACT-14", "D-04.2", "Doc07 §9.2 row 12: 'Contain incident → D-04.2'"),
    # §9.2 row 13
    ("ACT-17", "D-04.4", "Doc07 §9.2 row 13: 'Recover systems → D-04.4'"),
    # §9.2 row 14
    ("ACT-18", "D-04.2", "Doc07 §9.2 row 14: 'Post-incident review → D-04.2'"),
    # §9.2 row 15
    ("ACT-19", "D-05.1", "Doc07 §9.2 row 15: 'Data minimisation → D-05.1'"),
    # §9.2 row 16
    ("ACT-20", "D-05.2", "Doc07 §9.2 row 16: 'Retention policies → D-05.2'"),
    # §9.2 row 17
    ("ACT-21", "D-05.3", "Doc07 §9.2 row 17: 'Erasure requests → D-05.3'"),
    # §9.2 row 18
    ("ACT-22", "D-05.4", "Doc07 §9.2 row 18: 'Portability requests → D-05.4'"),
    # §9.2 row 19
    ("ACT-23", "D-06.1", "Doc07 §9.2 row 19: 'Vendor security assessment → D-06.1'"),
    # §9.2 row 20
    ("ACT-24", "D-06.2", "Doc07 §9.2 row 20: 'SBOM → D-06.2'"),
    # §9.2 row 21 (collapsed: DPA contracts (B2B / subprocessor) → D-06.3; representative = ACT-25)
    ("ACT-25", "D-06.3", "Doc07 §9.2 row 21: 'DPA contracts (B2B / subprocessor) → D-06.3' (collapsed from ACT-25, ACT-26)"),
    # §9.2 row 22
    ("ACT-27", "D-07.1", "Doc07 §9.2 row 22: 'Threat model per feature → D-07.1'"),
    # §9.2 row 23
    ("ACT-28", "D-07.2", "Doc07 §9.2 row 23: 'Code review → D-07.2'"),
    # §9.2 row 24
    ("ACT-29", "D-07.3", "Doc07 §9.2 row 24: 'Security testing in CI/CD → D-07.3'"),
    # §9.2 row 25
    ("ACT-30", "D-07.4", "Doc07 §9.2 row 25: 'Change approval (CAB) → D-07.4'"),
    # §9.2 row 26
    ("ACT-31", "D-08.1", "Doc07 §9.2 row 26: 'Annual security awareness → D-08.1'"),
    # §9.2 row 27 (collapsed: Role-specific training → D-08.2; representative = ACT-32)
    ("ACT-32", "D-08.2", "Doc07 §9.2 row 27: 'Role-specific training → D-08.2' (collapsed from ACT-32, ACT-33)"),
    # §9.2 row 28 (D-08.3 INACTIVE; mapped but sub-domain is inactive)
    ("ACT-34", "D-08.3", "Doc07 §9.2 row 28: 'Board cybersecurity briefings → D-08.3' (D-08.3 INACTIVE)"),
    # §9.2 row 29
    ("ACT-36", "D-09.1", "Doc07 §9.2 row 29: 'Approve security policies → D-09.1'"),
    # §9.2 row 30
    ("ACT-37", "D-09.2", "Doc07 §9.2 row 30: 'Risk assessments → D-09.2'"),
    # §9.2 row 31
    ("ACT-38", "D-09.3", "Doc07 §9.2 row 31: 'Maintain asset inventory → D-09.3'"),
    # §9.2 row 32 (collapsed: RoPA / Annex VII documentation → D-09.4; representative = ACT-39)
    ("ACT-39", "D-09.4", "Doc07 §9.2 row 32: 'RoPA / Annex VII documentation → D-09.4' (collapsed from ACT-39, ACT-40)"),
    # §9.2 row 33
    ("ACT-41", "D-10.1", "Doc07 §9.2 row 33: 'Continuous security monitoring → D-10.1'"),
    # §9.2 row 34
    ("ACT-42", "D-10.2", "Doc07 §9.2 row 34: 'Audit-log retention → D-10.2'"),
    # §9.2 row 35
    ("ACT-43", "D-10.3", "Doc07 §9.2 row 35: 'Annual compliance testing → D-10.3'"),
]
assert len(APPLIES_TO_EDGES) == 35, f"APPLIES_TO_EDGES drift: {len(APPLIES_TO_EDGES)} (expected 35)"


# ---------------------------------------------------------------------------
# 8.5. Sprint 8 / Phase B — Doc04 (Architecture) + Doc06 (Third Parties)
#      Sources: Doc04 §1.1, §2.1, §2.2, §2.3, §2.4 + Doc06 §2 + §5 + §6.
#      Schema: phase1_ontology.yaml@kg_ontology v1.4 (6 new classes +
#      9 active new relations + 27 counts + 16 id_patterns).
# ---------------------------------------------------------------------------

# --- 5 Systems (Doc04 §1.1 lines 49–55) ---
SYSTEMS = [
    {
        "id": "SYS-01",
        "label": "Main SaaS Application",
        "attrs": {
            "name": "Main SaaS Application",
            "type": "Cloud SaaS application",
            "tech_stack": "Node.js API, React web client, PostgreSQL driver",
            "criticality": "Important",
            "hosts_personal_data": True,
        },
        "source": ["Doc04 §1.1 line 51 (System Inventory, SYS-01 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.System"],
    },
    {
        "id": "SYS-02",
        "label": "Auth Service",
        "attrs": {
            "name": "Auth Service",
            "type": "Managed identity service",
            "tech_stack": "Auth0 using OAuth 2.0 and OIDC",
            "criticality": "Important",
            "hosts_personal_data": True,
        },
        "source": ["Doc04 §1.1 line 52 (System Inventory, SYS-02 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.System"],
    },
    {
        "id": "SYS-03",
        "label": "Customer Data Store",
        "attrs": {
            "name": "Customer Data Store",
            "type": "Managed relational database",
            "tech_stack": "PostgreSQL on EU cloud region",
            "criticality": "Critical",
            "hosts_personal_data": True,
        },
        "source": ["Doc04 §1.1 line 53 (System Inventory, SYS-03 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.System"],
    },
    {
        "id": "SYS-04",
        "label": "Cloud KMS",
        "attrs": {
            "name": "Cloud KMS",
            "type": "Managed key management",
            "tech_stack": "Cloud KMS with provider-managed key storage",
            "criticality": "Supporting",
            "hosts_personal_data": False,
        },
        "source": ["Doc04 §1.1 line 54 (System Inventory, SYS-04 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.System"],
    },
    {
        "id": "SYS-05",
        "label": "Backup Store",
        "attrs": {
            "name": "Backup Store",
            "type": "Managed object storage",
            "tech_stack": "S3-compatible encrypted bucket",
            "criticality": "Important",
            "hosts_personal_data": True,
        },
        "source": ["Doc04 §1.1 line 55 (System Inventory, SYS-05 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.System"],
    },
]
assert len(SYSTEMS) == 5, f"SYSTEMS drift: {len(SYSTEMS)} (expected 5)"


# --- 3 DataStores (Doc04 §2.1 lines 86–90) ---
DATASTORES = [
    {
        "id": "STORE-01",
        "label": "STORE-01 PostgreSQL database",
        "attrs": {
            "type": "PostgreSQL database",
            "location": "EU cloud region",
            "encryption_at_rest": "Y, AES-256 provider-managed encryption using SYS-04 keys",
            "retention_period": "Active account lifetime plus 30 days after deletion request where legally permissible",
            "backup": True,
        },
        "source": ["Doc04 §2.1 line 88 (Data Stores, STORE-01 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.DataStore"],
    },
    {
        "id": "STORE-02",
        "label": "STORE-02 Object storage backups",
        "attrs": {
            "type": "Object storage backups",
            "location": "EU cloud region",
            "encryption_at_rest": "Y, SSE-KMS/AES-256 using SYS-04 keys",
            "retention_period": "Daily backups for 30 days; monthly backups for 12 months",
            "backup": True,
        },
        "source": ["Doc04 §2.1 line 89 (Data Stores, STORE-02 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.DataStore"],
    },
    {
        "id": "STORE-03",
        "label": "STORE-03 Logs and analytics",
        "attrs": {
            "type": "Logs and analytics",
            "location": "EU monitoring region where available",
            "encryption_at_rest": "Y, provider-managed encryption; no raw task content intentionally logged",
            "retention_period": "30 days",
            "backup": False,
        },
        "source": ["Doc04 §2.1 line 90 (Data Stores, STORE-03 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.DataStore"],
    },
]
assert len(DATASTORES) == 3, f"DATASTORES drift: {len(DATASTORES)} (expected 3)"


# --- 5 DataFlows (Doc04 §2.2 lines 94–100) ---
DATAFLOWS = [
    {
        "id": "FLOW-01",
        "label": "FLOW-01 Web client → SYS-01",
        "attrs": {
            "data_type": "Account data and project data",
            "volume": "Low to medium",
            "encryption_in_transit": True,
            "protocol": "HTTPS REST",
            "subprocessor": False,
        },
        "source": ["Doc04 §2.2 line 96 (Data Flows, FLOW-01 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.DataFlow"],
    },
    {
        "id": "FLOW-02",
        "label": "FLOW-02 SYS-01 → STORE-01",
        "attrs": {
            "data_type": "Customer accounts, project data, audit metadata",
            "volume": "Low to medium",
            "encryption_in_transit": True,
            "protocol": "PostgreSQL TLS",
            "subprocessor": False,
        },
        "source": ["Doc04 §2.2 line 97 (Data Flows, FLOW-02 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.DataFlow"],
    },
    {
        "id": "FLOW-03",
        "label": "FLOW-03 SYS-01 → STORE-03 (Datadog)",
        "attrs": {
            "data_type": "Pseudonymised events, request metadata, error traces",
            "volume": "Low",
            "encryption_in_transit": True,
            "protocol": "HTTPS agent/API",
            "subprocessor": True,
        },
        "source": ["Doc04 §2.2 line 98 (Data Flows, FLOW-03 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.DataFlow"],
    },
    {
        "id": "FLOW-04",
        "label": "FLOW-04 Web client → SYS-02 (Auth0)",
        "attrs": {
            "data_type": "Authentication credentials, email identifier, OIDC tokens",
            "volume": "Low",
            "encryption_in_transit": True,
            "protocol": "OAuth 2.0/OIDC over HTTPS",
            "subprocessor": True,
        },
        "source": ["Doc04 §2.2 line 99 (Data Flows, FLOW-04 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.DataFlow"],
    },
    {
        "id": "FLOW-05",
        "label": "FLOW-05 SYS-01 → Stripe",
        "attrs": {
            "data_type": "Billing metadata and hosted-checkout redirect; no card PAN stored by TinyTask",
            "volume": "Low",
            "encryption_in_transit": True,
            "protocol": "HTTPS API",
            "subprocessor": True,
        },
        "source": ["Doc04 §2.2 line 100 (Data Flows, FLOW-05 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.DataFlow"],
    },
]
assert len(DATAFLOWS) == 5, f"DATAFLOWS drift: {len(DATAFLOWS)} (expected 5)"


# --- 4 PersonalDataCategories (Doc04 §2.3 lines 102–109) ---
PERSONAL_DATA_CATEGORIES = [
    {
        "id": "PDC-EMAIL",
        "label": "Email addresses",
        "attrs": {
            "category": "Email addresses",
            "legal_basis_art6_gdpr": "Contract",
            "retention": "Account lifetime plus 30 days after deletion request where legally permissible",
            "erasure_mechanism": "Manual admin deletion through support workflow; Auth0 deletion required separately",
        },
        "source": ["Doc04 §2.3 line 106 (Personal Data Categories, Email row)",
                   "phase1_ontology.yaml@kg_ontology.classes.PersonalDataCategory"],
    },
    {
        "id": "PDC-NAMES",
        "label": "Names",
        "attrs": {
            "category": "Names",
            "legal_basis_art6_gdpr": "Contract",
            "retention": "Account lifetime plus 30 days after deletion request where legally permissible",
            "erasure_mechanism": "Manual admin deletion through support workflow",
        },
        "source": ["Doc04 §2.3 line 107 (Personal Data Categories, Names row)",
                   "phase1_ontology.yaml@kg_ontology.classes.PersonalDataCategory"],
    },
    {
        "id": "PDC-PROJECT",
        "label": "Project data uploaded by users",
        "attrs": {
            "category": "Project data uploaded by users",
            "legal_basis_art6_gdpr": "Contract",
            "retention": "Account or workspace lifetime; backups retained up to 12 months",
            "erasure_mechanism": "Workspace deletion removes active records; backups expire by retention schedule",
        },
        "source": ["Doc04 §2.3 line 108 (Personal Data Categories, Project data row)",
                   "phase1_ontology.yaml@kg_ontology.classes.PersonalDataCategory"],
    },
    {
        "id": "PDC-PAYMENT",
        "label": "Payment and billing data",
        "attrs": {
            "category": "Payment and billing data",
            "legal_basis_art6_gdpr": "Contract",
            "retention": "Stripe retention under its processor/controller terms; TinyTask stores limited billing references",
            "erasure_mechanism": "Deletion or anonymisation by support request; Stripe customer record deletion where legally permissible",
        },
        "source": ["Doc04 §2.3 line 109 (Personal Data Categories, Payment row)",
                   "phase1_ontology.yaml@kg_ontology.classes.PersonalDataCategory"],
    },
]
assert len(PERSONAL_DATA_CATEGORIES) == 4, f"PERSONAL_DATA_CATEGORIES drift: {len(PERSONAL_DATA_CATEGORIES)} (expected 4)"


# --- 3 DataSubjectCategories (Doc04 §2.4 lines 113–117) ---
DATA_SUBJECT_CATEGORIES = [
    {
        "id": "DSC-EU-CUSTOMERS",
        "label": "EU customers (B2B and B2C)",
        "attrs": {
            "category": "EU customers (B2B and B2C)",
            "access_mechanism": "In-app account view and support request",
            "erasure_mechanism": "Manual support workflow; active records deleted and backup expiry relied on for residual copies",
        },
        "source": ["Doc04 §2.4 line 115 (Data Subject Categories, EU customers row)",
                   "phase1_ontology.yaml@kg_ontology.classes.DataSubjectCategory"],
    },
    {
        "id": "DSC-FREE-TIER",
        "label": "Free-tier users",
        "attrs": {
            "category": "Free-tier users",
            "access_mechanism": "In-app account view and support request",
            "erasure_mechanism": "Manual support workflow; inactive accounts reviewed ad hoc",
        },
        "source": ["Doc04 §2.4 line 116 (Data Subject Categories, Free-tier users row)",
                   "phase1_ontology.yaml@kg_ontology.classes.DataSubjectCategory"],
    },
    {
        "id": "DSC-ENTERPRISE-END-USERS",
        "label": "Enterprise customer end users",
        "attrs": {
            "category": "Enterprise customer end users",
            "access_mechanism": "Enterprise administrator export and support-assisted DSAR",
            "erasure_mechanism": "Processor-assisted deletion on controller instruction under DPA",
        },
        "source": ["Doc04 §2.4 line 117 (Data Subject Categories, Enterprise end users row)",
                   "phase1_ontology.yaml@kg_ontology.classes.DataSubjectCategory"],
    },
]
assert len(DATA_SUBJECT_CATEGORIES) == 3, f"DATA_SUBJECT_CATEGORIES drift: {len(DATA_SUBJECT_CATEGORIES)} (expected 3)"


# --- 6 ThirdParties (Doc06 §2 + §5 + §6) ---
THIRD_PARTIES = [
    {
        "id": "AWS",
        "label": "AWS (or equivalent EU cloud provider)",
        "attrs": {
            "name": "AWS",
            "aliases": ["Amazon Web Services"],
            "services": [
                "EC2/compute (SYS-01 runtime)",
                "RDS/managed PostgreSQL (SYS-03)",
                "S3/object storage (SYS-05 backups)",
                "Cloud KMS (SYS-04)",
            ],
            "regions": ["eu-west-1", "EU region"],
            "criticality": "Critical",
            "risk_score": "L",
            "dpa_in_place": True,
            "article_28_compliant": True,
            "exit_plan": False,  # Doc06 §2: N — not yet documented; flagged via Doc06 §8 GAP-TPL-02
            "last_assessment": "2026-04 — informal review during intake (no formal assessment yet)",
            "next_review": "2027-04",
            "sbom_available": False,  # Doc06 §5: N — AWS does not publish SBOM as SaaS consumer
            "art_28_dpa": True,
            "art_30_clauses": True,
            "security_audit_right": "Indirect — AWS substitutes SOC 2 / ISO 27001 / ISO 27018 reports in lieu of direct audit access",
            "subprocessor_approval": "Y — AWS publishes subprocessor list; customers may subscribe to change notifications",
            "data_accessed": [
                "Application logs, runtime config, no direct personal data at this layer (EC2)",
                "Customer accounts (email, name, hashed password), B2B project content (RDS)",
                "Encrypted DB backups containing personal data (S3)",
                "Key metadata only; raw keys never leave HSM-bound processors (Cloud KMS)",
            ],
        },
        "source": ["Doc06 §2 lines 59–62 (Cloud & Infrastructure Providers, 4 AWS rows)",
                   "Doc06 §5 line 173 (Supply Chain Risk table, AWS row)",
                   "Doc06 §6 line 192 (Contractual Coverage, AWS row)",
                   "phase1_ontology.yaml@kg_ontology.classes.ThirdParty"],
    },
    {
        "id": "Stripe",
        "label": "Stripe",
        "attrs": {
            "name": "Stripe",
            "aliases": ["Stripe Technologies"],
            "services": ["Stripe-hosted payment checkout (FLOW-05)"],
            "regions": ["Stripe-controlled regions (EU processing locations per Stripe DPA)"],
            "criticality": "Critical",
            "risk_score": "L",
            "dpa_in_place": True,
            "article_28_compliant": True,
            "exit_plan": True,  # Doc06 §2: Y — Stripe Dashboard API documented
            "last_assessment": "2026-04 — informal review",
            "next_review": "2027-04",
            "sbom_available": False,  # Doc06 §5: N/A — payment processor; SBOM not applicable
            "art_28_dpa": True,
            "art_30_clauses": True,
            "security_audit_right": "Indirect — Stripe provides PCI-DSS Level 1 AOC and SOC 2 reports",
            "subprocessor_approval": "Y — Stripe publishes subprocessor list",
            "data_accessed": [
                "Card PAN tokenised by Stripe; TinyTask stores only billing metadata and Stripe customer IDs; no PAN",
            ],
        },
        "source": ["Doc06 §2 line 63 (Cloud & Infrastructure Providers, Stripe row)",
                   "Doc06 §5 line 174 (Supply Chain Risk table, Stripe row)",
                   "Doc06 §6 line 193 (Contractual Coverage, Stripe row)",
                   "phase1_ontology.yaml@kg_ontology.classes.ThirdParty"],
    },
    {
        "id": "Auth0",
        "label": "Auth0 (by Okta)",
        "attrs": {
            "name": "Auth0",
            "aliases": ["Auth0 by Okta"],
            "services": ["Authentication / identity (SYS-02)"],
            "regions": ["Auth0 EU region (tenant where available)"],
            "criticality": "Critical",
            "risk_score": "L",
            "dpa_in_place": True,
            "article_28_compliant": True,
            "exit_plan": True,  # Doc06 §2: Y — Auth0 user-export API documented
            "last_assessment": "2026-04 — informal review",
            "next_review": "2027-04",
            "sbom_available": False,  # Doc06 §5: N/A — managed identity service; SBOM not applicable
            "art_28_dpa": True,
            "art_30_clauses": True,
            "security_audit_right": "Indirect — Auth0 provides SOC 2 / ISO 27001 + ISO 27018 reports on request",
            "subprocessor_approval": "Y — Auth0/Okta publishes subprocessor list",
            "data_accessed": [
                "Email addresses (used as identifiers), hashed passwords, MFA factors, session metadata, OIDC tokens",
            ],
        },
        "source": ["Doc06 §2 line 64 (Cloud & Infrastructure Providers, Auth0 row)",
                   "Doc06 §5 line 175 (Supply Chain Risk table, Auth0 row)",
                   "Doc06 §6 line 194 (Contractual Coverage, Auth0 row)",
                   "phase1_ontology.yaml@kg_ontology.classes.ThirdParty"],
    },
    {
        "id": "Datadog",
        "label": "Datadog (or equivalent)",
        "attrs": {
            "name": "Datadog",
            "aliases": ["Datadog APM"],
            "services": ["APM / log aggregation (STORE-03)", "Log aggregation + APM"],
            "regions": ["EU site where available"],
            "criticality": "Critical",
            "risk_score": "M",
            "dpa_in_place": True,
            "article_28_compliant": True,
            "exit_plan": None,  # Doc06 §2 + §5 + §6: implicit only (NEW-04 audit) — gap surfaced
            "last_assessment": "2026-04 — informal review",
            "next_review": "2027-04",
            "sbom_available": False,  # Doc06 §5: N/A — log SaaS
            "art_28_dpa": True,
            "art_30_clauses": True,
            "security_audit_right": "Indirect — Datadog SOC 2 Type II report available",
            "subprocessor_approval": "Y — Datadog publishes subprocessor list",
            "data_accessed": [
                "Pseudonymised operational logs and metrics — no raw customer content by design",
            ],
        },
        "source": ["Doc06 §2 line 72 (Cloud Services table row, Datadog equivalent row)",
                   "Doc06 §5 line 176 (Supply Chain Risk table, Datadog row)",
                   "Doc06 §6 line 195 (Contractual Coverage, Datadog row)",
                   "phase1_ontology.yaml@kg_ontology.classes.ThirdParty"],
    },
    {
        "id": "GitHub",
        "label": "GitHub",
        "attrs": {
            "name": "GitHub",
            "aliases": ["GitHub.com"],
            "services": ["Source-code hosting + Git-based version control"],
            "regions": ["GitHub global"],
            "criticality": "Important",
            "risk_score": "M",
            "dpa_in_place": True,
            "article_28_compliant": True,
            "exit_plan": True,  # Doc06 §6: Y (GitHub DPA — exit covered by GitHub subprocessor + DPA termination)
            "last_assessment": "2026-04 — informal review",
            "next_review": "2027-04",
            "sbom_available": False,  # Doc06 §5: N/A — repository service
            "art_28_dpa": True,
            "art_30_clauses": "Limited (source code is not personal data subject to Art. 30 processor records)",
            "security_audit_right": "Indirect — GitHub SOC 2 available",
            "subprocessor_approval": "Y",
            "data_accessed": [
                "Source code, issue text, commit metadata (no production personal data)",
            ],
        },
        "source": ["Doc06 §3 line 76 (Software Vendors table, GitHub row)",
                   "Doc06 §5 line 177 (Supply Chain Risk table, GitHub row)",
                   "Doc06 §6 line 196 (Contractual Coverage, GitHub row)",
                   "phase1_ontology.yaml@kg_ontology.classes.ThirdParty"],
    },
    {
        "id": "Snyk",
        "label": "Snyk",
        "attrs": {
            "name": "Snyk",
            "aliases": ["Snyk Limited"],
            "services": ["Software composition analysis / vulnerability scanning"],
            "regions": ["Snyk SaaS regions (tenant default)"],
            "criticality": "Important",
            "risk_score": "L",
            "dpa_in_place": True,
            "article_28_compliant": True,
            "exit_plan": True,  # Doc06 §6: Y (Snyk DPA — exit covered by DPA termination)
            "last_assessment": "2026-04 — informal review",
            "next_review": "2027-04",
            "sbom_available": True,  # Doc06 §5: Y — Snyk can output CycloneDX/SPDX for scanned projects
            "art_28_dpa": True,  # Doc06 §6: Y (Snyk DPA — paid tiers; tier not captured, NEW-05)
            "art_30_clauses": "Limited (developer tool; no personal data processed)",
            "security_audit_right": "Indirect — Snyk SOC 2 available",
            "subprocessor_approval": "Limited (Snyk subprocessors disclosed)",
            "data_accessed": [
                "Source code + dependency manifests; no runtime personal data",
            ],
        },
        "source": ["Doc06 §3 line 78 (Software Vendors table, Snyk row)",
                   "Doc06 §5 line 178 (Supply Chain Risk table, Snyk row)",
                   "Doc06 §6 line 197 (Contractual Coverage, Snyk row)",
                   "phase1_ontology.yaml@kg_ontology.classes.ThirdParty"],
    },
]
assert len(THIRD_PARTIES) == 6, f"THIRD_PARTIES drift: {len(THIRD_PARTIES)} (expected 6)"


# ---------------------------------------------------------------------------
# 8.5.1. Phase B edge tables (Doc04 §2.1 + §2.2 + §2.3 + §2.4 + §3 + Doc06 §2/§5/§6)
# ---------------------------------------------------------------------------

# HOSTS_EDGES: System → DataStore (per ontology verb HOSTS).
# Doc04 §2.1 maps:
#   STORE-01 → SYS-03 (line 88)
#   STORE-02 → SYS-05 (line 89)
#   STORE-03 → SYS-01 + monitoring provider (line 90) — Sys-01 explicit; Datadog
#   destination is captured separately via PROCESSES on FLOW-03.
HOSTS_EDGES = [
    # STORE-01 hosted by SYS-03
    ("SYS-03", "STORE-01", "Doc04 §2.1 line 88: STORE-01.System = SYS-03"),
    # STORE-02 hosted by SYS-05
    ("SYS-05", "STORE-02", "Doc04 §2.1 line 89: STORE-02.System = SYS-05"),
    # STORE-03 hosted by SYS-01 (Datadog link captured via PROCESSES on FLOW-03)
    ("SYS-01", "STORE-03", "Doc04 §2.1 line 90: STORE-03.System = SYS-01 (monitoring provider link is on FLOW-03)"),
]
assert len(HOSTS_EDGES) == 3, f"HOSTS_EDGES drift: {len(HOSTS_EDGES)} (expected 3)"


# INVOLVES_EDGES: SecurityControlDomain → System
# Doc04 §3 (lines 125–161) Compliance Mapping; one edge per (sub-domain, system).
# Free-text refs ("cloud IAM", "GitHub organisation", "STORE-03 monitoring",
# "SYS-01 release pipeline", "Stripe", "Datadog") are SKIPPED — surfaced via
# NEW-01 audit. Wildcard "All production systems" expands to SYS-01..SYS-05.
INVOLVES_EDGES = [
    # D-01.1: SYS-03, SYS-04, SYS-05
    ("D-01.1", "SYS-03", "Doc04 §3 row D-01.1: SYS-03"),
    ("D-01.1", "SYS-04", "Doc04 §3 row D-01.1: SYS-04"),
    ("D-01.1", "SYS-05", "Doc04 §3 row D-01.1: SYS-05"),
    # D-01.2: SYS-01, SYS-02, SYS-03
    ("D-01.2", "SYS-01", "Doc04 §3 row D-01.2: SYS-01"),
    ("D-01.2", "SYS-02", "Doc04 §3 row D-01.2: SYS-02"),
    ("D-01.2", "SYS-03", "Doc04 §3 row D-01.2: SYS-03"),
    # D-01.3: SYS-04
    ("D-01.3", "SYS-04", "Doc04 §3 row D-01.3: SYS-04"),
    # D-01.4: SYS-01, SYS-03, SYS-05
    ("D-01.4", "SYS-01", "Doc04 §3 row D-01.4: SYS-01"),
    ("D-01.4", "SYS-03", "Doc04 §3 row D-01.4: SYS-03"),
    ("D-01.4", "SYS-05", "Doc04 §3 row D-01.4: SYS-05"),
    # D-02.1: SYS-01, SYS-02, SYS-03
    ("D-02.1", "SYS-01", "Doc04 §3 row D-02.1: SYS-01"),
    ("D-02.1", "SYS-02", "Doc04 §3 row D-02.1: SYS-02"),
    ("D-02.1", "SYS-03", "Doc04 §3 row D-02.1: SYS-03"),
    # D-02.2: SYS-01, SYS-03
    ("D-02.2", "SYS-01", "Doc04 §3 row D-02.2: SYS-01"),
    ("D-02.2", "SYS-03", "Doc04 §3 row D-02.2: SYS-03"),
    # D-02.3: SYS-01
    ("D-02.3", "SYS-01", "Doc04 §3 row D-02.3: SYS-01"),
    # D-02.4: SYS-01, SYS-02, SYS-03
    ("D-02.4", "SYS-01", "Doc04 §3 row D-02.4: SYS-01"),
    ("D-02.4", "SYS-02", "Doc04 §3 row D-02.4: SYS-02"),
    ("D-02.4", "SYS-03", "Doc04 §3 row D-02.4: SYS-03"),
    # D-03.1: SYS-02 (cloud IAM, GitHub organisation skipped — NEW-01)
    ("D-03.1", "SYS-02", "Doc04 §3 row D-03.1: SYS-02"),
    # D-03.2: SYS-02 (cloud IAM, GitHub organisation skipped — NEW-01)
    ("D-03.2", "SYS-02", "Doc04 §3 row D-03.2: SYS-02"),
    # D-03.3: SYS-01, SYS-02, SYS-03, SYS-04
    ("D-03.3", "SYS-01", "Doc04 §3 row D-03.3: SYS-01"),
    ("D-03.3", "SYS-02", "Doc04 §3 row D-03.3: SYS-02"),
    ("D-03.3", "SYS-03", "Doc04 §3 row D-03.3: SYS-03"),
    ("D-03.3", "SYS-04", "Doc04 §3 row D-03.3: SYS-04"),
    # D-03.4: SYS-01, SYS-02, SYS-03
    ("D-03.4", "SYS-01", "Doc04 §3 row D-03.4: SYS-01"),
    ("D-03.4", "SYS-02", "Doc04 §3 row D-03.4: SYS-02"),
    ("D-03.4", "SYS-03", "Doc04 §3 row D-03.4: SYS-03"),
    # D-04.1: SYS-01, SYS-03 (STORE-03 monitoring skipped — NEW-01)
    ("D-04.1", "SYS-01", "Doc04 §3 row D-04.1: SYS-01"),
    ("D-04.1", "SYS-03", "Doc04 §3 row D-04.1: SYS-03"),
    # D-04.2: SYS-01, SYS-02, SYS-03
    ("D-04.2", "SYS-01", "Doc04 §3 row D-04.2: SYS-01"),
    ("D-04.2", "SYS-02", "Doc04 §3 row D-04.2: SYS-02"),
    ("D-04.2", "SYS-03", "Doc04 §3 row D-04.2: SYS-03"),
    # D-04.3: SYS-01, SYS-02 (STORE-03 monitoring skipped — NEW-01)
    ("D-04.3", "SYS-01", "Doc04 §3 row D-04.3: SYS-01"),
    ("D-04.3", "SYS-02", "Doc04 §3 row D-04.3: SYS-02"),
    # D-04.4: SYS-03, SYS-05
    ("D-04.4", "SYS-03", "Doc04 §3 row D-04.4: SYS-03"),
    ("D-04.4", "SYS-05", "Doc04 §3 row D-04.4: SYS-05"),
    # D-05.1: SYS-01, SYS-03
    ("D-05.1", "SYS-01", "Doc04 §3 row D-05.1: SYS-01"),
    ("D-05.1", "SYS-03", "Doc04 §3 row D-05.1: SYS-03"),
    # D-05.2: SYS-03, SYS-05 (STORE-03 monitoring skipped — NEW-01)
    ("D-05.2", "SYS-03", "Doc04 §3 row D-05.2: SYS-03"),
    ("D-05.2", "SYS-05", "Doc04 §3 row D-05.2: SYS-05"),
    # D-05.3: SYS-01, SYS-02, SYS-03, SYS-05
    ("D-05.3", "SYS-01", "Doc04 §3 row D-05.3: SYS-01"),
    ("D-05.3", "SYS-02", "Doc04 §3 row D-05.3: SYS-02"),
    ("D-05.3", "SYS-03", "Doc04 §3 row D-05.3: SYS-03"),
    ("D-05.3", "SYS-05", "Doc04 §3 row D-05.3: SYS-05"),
    # D-05.4: SYS-01, SYS-03
    ("D-05.4", "SYS-01", "Doc04 §3 row D-05.4: SYS-01"),
    ("D-05.4", "SYS-03", "Doc04 §3 row D-05.4: SYS-03"),
    # D-06.1: SYS-02, SYS-03, SYS-04, SYS-05 (Stripe skipped — NEW-01)
    ("D-06.1", "SYS-02", "Doc04 §3 row D-06.1: SYS-02"),
    ("D-06.1", "SYS-03", "Doc04 §3 row D-06.1: SYS-03"),
    ("D-06.1", "SYS-04", "Doc04 §3 row D-06.1: SYS-04"),
    ("D-06.1", "SYS-05", "Doc04 §3 row D-06.1: SYS-05"),
    # D-06.2: (SYS-01 release pipeline skipped — NEW-01)
    # D-06.3: SYS-02, SYS-03, SYS-05 (Stripe, Datadog skipped — NEW-01)
    ("D-06.3", "SYS-02", "Doc04 §3 row D-06.3: SYS-02"),
    ("D-06.3", "SYS-03", "Doc04 §3 row D-06.3: SYS-03"),
    ("D-06.3", "SYS-05", "Doc04 §3 row D-06.3: SYS-05"),
    # D-06.4: SYS-01, SYS-02, SYS-03, SYS-05
    ("D-06.4", "SYS-01", "Doc04 §3 row D-06.4: SYS-01"),
    ("D-06.4", "SYS-02", "Doc04 §3 row D-06.4: SYS-02"),
    ("D-06.4", "SYS-03", "Doc04 §3 row D-06.4: SYS-03"),
    ("D-06.4", "SYS-05", "Doc04 §3 row D-06.4: SYS-05"),
    # D-07.1: SYS-01, SYS-02, SYS-03
    ("D-07.1", "SYS-01", "Doc04 §3 row D-07.1: SYS-01"),
    ("D-07.1", "SYS-02", "Doc04 §3 row D-07.1: SYS-02"),
    ("D-07.1", "SYS-03", "Doc04 §3 row D-07.1: SYS-03"),
    # D-07.2: (SYS-01 release pipeline skipped — NEW-01)
    # D-07.3: (SYS-01 release pipeline skipped — NEW-01)
    # D-07.4: SYS-01, SYS-03
    ("D-07.4", "SYS-01", "Doc04 §3 row D-07.4: SYS-01"),
    ("D-07.4", "SYS-03", "Doc04 §3 row D-07.4: SYS-03"),
    # D-08.1: All production systems → SYS-01..SYS-05
    ("D-08.1", "SYS-01", "Doc04 §3 row D-08.1: All production systems → expanded"),
    ("D-08.1", "SYS-02", "Doc04 §3 row D-08.1: All production systems → expanded"),
    ("D-08.1", "SYS-03", "Doc04 §3 row D-08.1: All production systems → expanded"),
    ("D-08.1", "SYS-04", "Doc04 §3 row D-08.1: All production systems → expanded"),
    ("D-08.1", "SYS-05", "Doc04 §3 row D-08.1: All production systems → expanded"),
    # D-08.2: SYS-01, SYS-02, SYS-03, SYS-04
    ("D-08.2", "SYS-01", "Doc04 §3 row D-08.2: SYS-01"),
    ("D-08.2", "SYS-02", "Doc04 §3 row D-08.2: SYS-02"),
    ("D-08.2", "SYS-03", "Doc04 §3 row D-08.2: SYS-03"),
    ("D-08.2", "SYS-04", "Doc04 §3 row D-08.2: SYS-04"),
    # D-09.1: All production systems → SYS-01..SYS-05
    ("D-09.1", "SYS-01", "Doc04 §3 row D-09.1: All production systems → expanded"),
    ("D-09.1", "SYS-02", "Doc04 §3 row D-09.1: All production systems → expanded"),
    ("D-09.1", "SYS-03", "Doc04 §3 row D-09.1: All production systems → expanded"),
    ("D-09.1", "SYS-04", "Doc04 §3 row D-09.1: All production systems → expanded"),
    ("D-09.1", "SYS-05", "Doc04 §3 row D-09.1: All production systems → expanded"),
    # D-09.2: SYS-01, SYS-02, SYS-03, SYS-05
    ("D-09.2", "SYS-01", "Doc04 §3 row D-09.2: SYS-01"),
    ("D-09.2", "SYS-02", "Doc04 §3 row D-09.2: SYS-02"),
    ("D-09.2", "SYS-03", "Doc04 §3 row D-09.2: SYS-03"),
    ("D-09.2", "SYS-05", "Doc04 §3 row D-09.2: SYS-05"),
    # D-09.3: SYS-01, SYS-02, SYS-03, SYS-04, SYS-05
    ("D-09.3", "SYS-01", "Doc04 §3 row D-09.3: SYS-01"),
    ("D-09.3", "SYS-02", "Doc04 §3 row D-09.3: SYS-02"),
    ("D-09.3", "SYS-03", "Doc04 §3 row D-09.3: SYS-03"),
    ("D-09.3", "SYS-04", "Doc04 §3 row D-09.3: SYS-04"),
    ("D-09.3", "SYS-05", "Doc04 §3 row D-09.3: SYS-05"),
    # D-09.4: SYS-01, SYS-02, SYS-03, SYS-05 (Stripe skipped — NEW-01)
    ("D-09.4", "SYS-01", "Doc04 §3 row D-09.4: SYS-01"),
    ("D-09.4", "SYS-02", "Doc04 §3 row D-09.4: SYS-02"),
    ("D-09.4", "SYS-03", "Doc04 §3 row D-09.4: SYS-03"),
    ("D-09.4", "SYS-05", "Doc04 §3 row D-09.4: SYS-05"),
    # D-10.1: SYS-01, SYS-03 (STORE-03 monitoring skipped — NEW-01)
    ("D-10.1", "SYS-01", "Doc04 §3 row D-10.1: SYS-01"),
    ("D-10.1", "SYS-03", "Doc04 §3 row D-10.1: SYS-03"),
    # D-10.2: SYS-01, SYS-02, SYS-03
    ("D-10.2", "SYS-01", "Doc04 §3 row D-10.2: SYS-01"),
    ("D-10.2", "SYS-02", "Doc04 §3 row D-10.2: SYS-02"),
    ("D-10.2", "SYS-03", "Doc04 §3 row D-10.2: SYS-03"),
    # D-10.3: SYS-01, SYS-02, SYS-03, SYS-05
    ("D-10.3", "SYS-01", "Doc04 §3 row D-10.3: SYS-01"),
    ("D-10.3", "SYS-02", "Doc04 §3 row D-10.3: SYS-02"),
    ("D-10.3", "SYS-03", "Doc04 §3 row D-10.3: SYS-03"),
    ("D-10.3", "SYS-05", "Doc04 §3 row D-10.3: SYS-05"),
]
assert len(INVOLVES_EDGES) == 99, f"INVOLVES_EDGES drift: {len(INVOLVES_EDGES)} (expected 99)"


# INVOLVES_STORE_EDGES: SecurityControlDomain → DataStore
# Per Doc04 §3 'Relevant Data Stores' column; only STORE-* ids become edges.
INVOLVES_STORE_EDGES = [
    # D-01.1: STORE-01, STORE-02, STORE-03
    ("D-01.1", "STORE-01", "Doc04 §3 row D-01.1: STORE-01"),
    ("D-01.1", "STORE-02", "Doc04 §3 row D-01.1: STORE-02"),
    ("D-01.1", "STORE-03", "Doc04 §3 row D-01.1: STORE-03"),
    # D-01.2: STORE-01
    ("D-01.2", "STORE-01", "Doc04 §3 row D-01.2: STORE-01"),
    # D-01.3: STORE-01, STORE-02
    ("D-01.3", "STORE-01", "Doc04 §3 row D-01.3: STORE-01"),
    ("D-01.3", "STORE-02", "Doc04 §3 row D-01.3: STORE-02"),
    # D-01.4: STORE-01, STORE-02
    ("D-01.4", "STORE-01", "Doc04 §3 row D-01.4: STORE-01"),
    ("D-01.4", "STORE-02", "Doc04 §3 row D-01.4: STORE-02"),
    # D-02.1: STORE-03
    ("D-02.1", "STORE-03", "Doc04 §3 row D-02.1: STORE-03"),
    # D-02.2: STORE-03
    ("D-02.2", "STORE-03", "Doc04 §3 row D-02.2: STORE-03"),
    # D-02.3: STORE-03
    ("D-02.3", "STORE-03", "Doc04 §3 row D-02.3: STORE-03"),
    # D-02.4: STORE-01
    ("D-02.4", "STORE-01", "Doc04 §3 row D-02.4: STORE-01"),
    # D-03.1: STORE-01
    ("D-03.1", "STORE-01", "Doc04 §3 row D-03.1: STORE-01"),
    # D-03.2: STORE-01
    ("D-03.2", "STORE-01", "Doc04 §3 row D-03.2: STORE-01"),
    # D-03.3: STORE-01, STORE-02
    ("D-03.3", "STORE-01", "Doc04 §3 row D-03.3: STORE-01"),
    ("D-03.3", "STORE-02", "Doc04 §3 row D-03.3: STORE-02"),
    # D-03.4: STORE-01
    ("D-03.4", "STORE-01", "Doc04 §3 row D-03.4: STORE-01"),
    # D-04.1: STORE-03
    ("D-04.1", "STORE-03", "Doc04 §3 row D-04.1: STORE-03"),
    # D-04.2: STORE-01, STORE-03
    ("D-04.2", "STORE-01", "Doc04 §3 row D-04.2: STORE-01"),
    ("D-04.2", "STORE-03", "Doc04 §3 row D-04.2: STORE-03"),
    # D-04.3: STORE-03
    ("D-04.3", "STORE-03", "Doc04 §3 row D-04.3: STORE-03"),
    # D-04.4: STORE-01, STORE-02
    ("D-04.4", "STORE-01", "Doc04 §3 row D-04.4: STORE-01"),
    ("D-04.4", "STORE-02", "Doc04 §3 row D-04.4: STORE-02"),
    # D-05.1: STORE-01, STORE-03
    ("D-05.1", "STORE-01", "Doc04 §3 row D-05.1: STORE-01"),
    ("D-05.1", "STORE-03", "Doc04 §3 row D-05.1: STORE-03"),
    # D-05.2: STORE-01, STORE-02, STORE-03
    ("D-05.2", "STORE-01", "Doc04 §3 row D-05.2: STORE-01"),
    ("D-05.2", "STORE-02", "Doc04 §3 row D-05.2: STORE-02"),
    ("D-05.2", "STORE-03", "Doc04 §3 row D-05.2: STORE-03"),
    # D-05.3: STORE-01, STORE-02
    ("D-05.3", "STORE-01", "Doc04 §3 row D-05.3: STORE-01"),
    ("D-05.3", "STORE-02", "Doc04 §3 row D-05.3: STORE-02"),
    # D-05.4: STORE-01
    ("D-05.4", "STORE-01", "Doc04 §3 row D-05.4: STORE-01"),
    # D-06.1: STORE-01, STORE-02, STORE-03
    ("D-06.1", "STORE-01", "Doc04 §3 row D-06.1: STORE-01"),
    ("D-06.1", "STORE-02", "Doc04 §3 row D-06.1: STORE-02"),
    ("D-06.1", "STORE-03", "Doc04 §3 row D-06.1: STORE-03"),
    # D-06.2: STORE-03
    ("D-06.2", "STORE-03", "Doc04 §3 row D-06.2: STORE-03"),
    # D-06.3: STORE-01, STORE-02, STORE-03
    ("D-06.3", "STORE-01", "Doc04 §3 row D-06.3: STORE-01"),
    ("D-06.3", "STORE-02", "Doc04 §3 row D-06.3: STORE-02"),
    ("D-06.3", "STORE-03", "Doc04 §3 row D-06.3: STORE-03"),
    # D-06.4: STORE-01, STORE-02, STORE-03
    ("D-06.4", "STORE-01", "Doc04 §3 row D-06.4: STORE-01"),
    ("D-06.4", "STORE-02", "Doc04 §3 row D-06.4: STORE-02"),
    ("D-06.4", "STORE-03", "Doc04 §3 row D-06.4: STORE-03"),
    # D-07.1: STORE-01
    ("D-07.1", "STORE-01", "Doc04 §3 row D-07.1: STORE-01"),
    # D-07.2: STORE-03
    ("D-07.2", "STORE-03", "Doc04 §3 row D-07.2: STORE-03"),
    # D-07.3: STORE-03
    ("D-07.3", "STORE-03", "Doc04 §3 row D-07.3: STORE-03"),
    # D-07.4: STORE-01, STORE-03
    ("D-07.4", "STORE-01", "Doc04 §3 row D-07.4: STORE-01"),
    ("D-07.4", "STORE-03", "Doc04 §3 row D-07.4: STORE-03"),
    # D-08.1: STORE-01, STORE-02, STORE-03
    ("D-08.1", "STORE-01", "Doc04 §3 row D-08.1: STORE-01"),
    ("D-08.1", "STORE-02", "Doc04 §3 row D-08.1: STORE-02"),
    ("D-08.1", "STORE-03", "Doc04 §3 row D-08.1: STORE-03"),
    # D-08.2: STORE-01, STORE-02
    ("D-08.2", "STORE-01", "Doc04 §3 row D-08.2: STORE-01"),
    ("D-08.2", "STORE-02", "Doc04 §3 row D-08.2: STORE-02"),
    # D-09.1: STORE-01, STORE-02, STORE-03
    ("D-09.1", "STORE-01", "Doc04 §3 row D-09.1: STORE-01"),
    ("D-09.1", "STORE-02", "Doc04 §3 row D-09.1: STORE-02"),
    ("D-09.1", "STORE-03", "Doc04 §3 row D-09.1: STORE-03"),
    # D-09.2: STORE-01, STORE-02, STORE-03
    ("D-09.2", "STORE-01", "Doc04 §3 row D-09.2: STORE-01"),
    ("D-09.2", "STORE-02", "Doc04 §3 row D-09.2: STORE-02"),
    ("D-09.2", "STORE-03", "Doc04 §3 row D-09.2: STORE-03"),
    # D-09.3: STORE-01, STORE-02, STORE-03
    ("D-09.3", "STORE-01", "Doc04 §3 row D-09.3: STORE-01"),
    ("D-09.3", "STORE-02", "Doc04 §3 row D-09.3: STORE-02"),
    ("D-09.3", "STORE-03", "Doc04 §3 row D-09.3: STORE-03"),
    # D-09.4: STORE-01, STORE-02, STORE-03
    ("D-09.4", "STORE-01", "Doc04 §3 row D-09.4: STORE-01"),
    ("D-09.4", "STORE-02", "Doc04 §3 row D-09.4: STORE-02"),
    ("D-09.4", "STORE-03", "Doc04 §3 row D-09.4: STORE-03"),
    # D-10.1: STORE-03
    ("D-10.1", "STORE-03", "Doc04 §3 row D-10.1: STORE-03"),
    # D-10.2: STORE-03
    ("D-10.2", "STORE-03", "Doc04 §3 row D-10.2: STORE-03"),
    # D-10.3: STORE-01, STORE-02, STORE-03
    ("D-10.3", "STORE-01", "Doc04 §3 row D-10.3: STORE-01"),
    ("D-10.3", "STORE-02", "Doc04 §3 row D-10.3: STORE-02"),
    ("D-10.3", "STORE-03", "Doc04 §3 row D-10.3: STORE-03"),
]
assert len(INVOLVES_STORE_EDGES) == 68, f"INVOLVES_STORE_EDGES drift: {len(INVOLVES_STORE_EDGES)} (expected 68)"


# INVOLVES_FLOW_EDGES: SecurityControlDomain → DataFlow
# Per Doc04 §3 'Relevant Data Flows' column; wildcard 'All production flows'
# expands to FLOW-01..FLOW-05.
INVOLVES_FLOW_EDGES = [
    # D-01.1: FLOW-02
    ("D-01.1", "FLOW-02", "Doc04 §3 row D-01.1: FLOW-02"),
    # D-01.2: FLOW-01, FLOW-02, FLOW-03, FLOW-04, FLOW-05
    ("D-01.2", "FLOW-01", "Doc04 §3 row D-01.2: FLOW-01"),
    ("D-01.2", "FLOW-02", "Doc04 §3 row D-01.2: FLOW-02"),
    ("D-01.2", "FLOW-03", "Doc04 §3 row D-01.2: FLOW-03"),
    ("D-01.2", "FLOW-04", "Doc04 §3 row D-01.2: FLOW-04"),
    ("D-01.2", "FLOW-05", "Doc04 §3 row D-01.2: FLOW-05"),
    # D-01.3: FLOW-02
    ("D-01.3", "FLOW-02", "Doc04 §3 row D-01.3: FLOW-02"),
    # D-01.4: FLOW-02
    ("D-01.4", "FLOW-02", "Doc04 §3 row D-01.4: FLOW-02"),
    # D-02.1: FLOW-03
    ("D-02.1", "FLOW-03", "Doc04 §3 row D-02.1: FLOW-03"),
    # D-02.2: FLOW-03
    ("D-02.2", "FLOW-03", "Doc04 §3 row D-02.2: FLOW-03"),
    # D-02.3: FLOW-03
    ("D-02.3", "FLOW-03", "Doc04 §3 row D-02.3: FLOW-03"),
    # D-02.4: FLOW-01, FLOW-04
    ("D-02.4", "FLOW-01", "Doc04 §3 row D-02.4: FLOW-01"),
    ("D-02.4", "FLOW-04", "Doc04 §3 row D-02.4: FLOW-04"),
    # D-03.1: FLOW-04
    ("D-03.1", "FLOW-04", "Doc04 §3 row D-03.1: FLOW-04"),
    # D-03.2: FLOW-04
    ("D-03.2", "FLOW-04", "Doc04 §3 row D-03.2: FLOW-04"),
    # D-03.3: FLOW-02, FLOW-04
    ("D-03.3", "FLOW-02", "Doc04 §3 row D-03.3: FLOW-02"),
    ("D-03.3", "FLOW-04", "Doc04 §3 row D-03.3: FLOW-04"),
    # D-03.4: FLOW-01, FLOW-04
    ("D-03.4", "FLOW-01", "Doc04 §3 row D-03.4: FLOW-01"),
    ("D-03.4", "FLOW-04", "Doc04 §3 row D-03.4: FLOW-04"),
    # D-04.1: FLOW-03
    ("D-04.1", "FLOW-03", "Doc04 §3 row D-04.1: FLOW-03"),
    # D-04.2: FLOW-01, FLOW-03, FLOW-04
    ("D-04.2", "FLOW-01", "Doc04 §3 row D-04.2: FLOW-01"),
    ("D-04.2", "FLOW-03", "Doc04 §3 row D-04.2: FLOW-03"),
    ("D-04.2", "FLOW-04", "Doc04 §3 row D-04.2: FLOW-04"),
    # D-04.3: FLOW-03
    ("D-04.3", "FLOW-03", "Doc04 §3 row D-04.3: FLOW-03"),
    # D-04.4: FLOW-02
    ("D-04.4", "FLOW-02", "Doc04 §3 row D-04.4: FLOW-02"),
    # D-05.1: FLOW-01, FLOW-03, FLOW-05
    ("D-05.1", "FLOW-01", "Doc04 §3 row D-05.1: FLOW-01"),
    ("D-05.1", "FLOW-03", "Doc04 §3 row D-05.1: FLOW-03"),
    ("D-05.1", "FLOW-05", "Doc04 §3 row D-05.1: FLOW-05"),
    # D-05.2: FLOW-02, FLOW-03
    ("D-05.2", "FLOW-02", "Doc04 §3 row D-05.2: FLOW-02"),
    ("D-05.2", "FLOW-03", "Doc04 §3 row D-05.2: FLOW-03"),
    # D-05.3: FLOW-01, FLOW-04, FLOW-05
    ("D-05.3", "FLOW-01", "Doc04 §3 row D-05.3: FLOW-01"),
    ("D-05.3", "FLOW-04", "Doc04 §3 row D-05.3: FLOW-04"),
    ("D-05.3", "FLOW-05", "Doc04 §3 row D-05.3: FLOW-05"),
    # D-05.4: FLOW-01
    ("D-05.4", "FLOW-01", "Doc04 §3 row D-05.4: FLOW-01"),
    # D-06.1: FLOW-03, FLOW-04, FLOW-05
    ("D-06.1", "FLOW-03", "Doc04 §3 row D-06.1: FLOW-03"),
    ("D-06.1", "FLOW-04", "Doc04 §3 row D-06.1: FLOW-04"),
    ("D-06.1", "FLOW-05", "Doc04 §3 row D-06.1: FLOW-05"),
    # D-06.2: FLOW-03
    ("D-06.2", "FLOW-03", "Doc04 §3 row D-06.2: FLOW-03"),
    # D-06.3: FLOW-03, FLOW-04, FLOW-05
    ("D-06.3", "FLOW-03", "Doc04 §3 row D-06.3: FLOW-03"),
    ("D-06.3", "FLOW-04", "Doc04 §3 row D-06.3: FLOW-04"),
    ("D-06.3", "FLOW-05", "Doc04 §3 row D-06.3: FLOW-05"),
    # D-06.4: FLOW-03, FLOW-04, FLOW-05
    ("D-06.4", "FLOW-03", "Doc04 §3 row D-06.4: FLOW-03"),
    ("D-06.4", "FLOW-04", "Doc04 §3 row D-06.4: FLOW-04"),
    ("D-06.4", "FLOW-05", "Doc04 §3 row D-06.4: FLOW-05"),
    # D-07.1: FLOW-01, FLOW-02, FLOW-04
    ("D-07.1", "FLOW-01", "Doc04 §3 row D-07.1: FLOW-01"),
    ("D-07.1", "FLOW-02", "Doc04 §3 row D-07.1: FLOW-02"),
    ("D-07.1", "FLOW-04", "Doc04 §3 row D-07.1: FLOW-04"),
    # D-07.2: FLOW-03
    ("D-07.2", "FLOW-03", "Doc04 §3 row D-07.2: FLOW-03"),
    # D-07.3: FLOW-03
    ("D-07.3", "FLOW-03", "Doc04 §3 row D-07.3: FLOW-03"),
    # D-07.4: FLOW-03
    ("D-07.4", "FLOW-03", "Doc04 §3 row D-07.4: FLOW-03"),
    # D-08.1: All production flows → FLOW-01..FLOW-05
    ("D-08.1", "FLOW-01", "Doc04 §3 row D-08.1: All production flows → expanded"),
    ("D-08.1", "FLOW-02", "Doc04 §3 row D-08.1: All production flows → expanded"),
    ("D-08.1", "FLOW-03", "Doc04 §3 row D-08.1: All production flows → expanded"),
    ("D-08.1", "FLOW-04", "Doc04 §3 row D-08.1: All production flows → expanded"),
    ("D-08.1", "FLOW-05", "Doc04 §3 row D-08.1: All production flows → expanded"),
    # D-08.2: FLOW-01, FLOW-02, FLOW-04
    ("D-08.2", "FLOW-01", "Doc04 §3 row D-08.2: FLOW-01"),
    ("D-08.2", "FLOW-02", "Doc04 §3 row D-08.2: FLOW-02"),
    ("D-08.2", "FLOW-04", "Doc04 §3 row D-08.2: FLOW-04"),
    # D-09.1: All production flows → FLOW-01..FLOW-05
    ("D-09.1", "FLOW-01", "Doc04 §3 row D-09.1: All production flows → expanded"),
    ("D-09.1", "FLOW-02", "Doc04 §3 row D-09.1: All production flows → expanded"),
    ("D-09.1", "FLOW-03", "Doc04 §3 row D-09.1: All production flows → expanded"),
    ("D-09.1", "FLOW-04", "Doc04 §3 row D-09.1: All production flows → expanded"),
    ("D-09.1", "FLOW-05", "Doc04 §3 row D-09.1: All production flows → expanded"),
    # D-09.2: FLOW-01, FLOW-02, FLOW-03, FLOW-04, FLOW-05
    ("D-09.2", "FLOW-01", "Doc04 §3 row D-09.2: FLOW-01"),
    ("D-09.2", "FLOW-02", "Doc04 §3 row D-09.2: FLOW-02"),
    ("D-09.2", "FLOW-03", "Doc04 §3 row D-09.2: FLOW-03"),
    ("D-09.2", "FLOW-04", "Doc04 §3 row D-09.2: FLOW-04"),
    ("D-09.2", "FLOW-05", "Doc04 §3 row D-09.2: FLOW-05"),
    # D-09.3: FLOW-01, FLOW-02, FLOW-03, FLOW-04, FLOW-05
    ("D-09.3", "FLOW-01", "Doc04 §3 row D-09.3: FLOW-01"),
    ("D-09.3", "FLOW-02", "Doc04 §3 row D-09.3: FLOW-02"),
    ("D-09.3", "FLOW-03", "Doc04 §3 row D-09.3: FLOW-03"),
    ("D-09.3", "FLOW-04", "Doc04 §3 row D-09.3: FLOW-04"),
    ("D-09.3", "FLOW-05", "Doc04 §3 row D-09.3: FLOW-05"),
    # D-09.4: FLOW-01, FLOW-02, FLOW-03, FLOW-04, FLOW-05
    ("D-09.4", "FLOW-01", "Doc04 §3 row D-09.4: FLOW-01"),
    ("D-09.4", "FLOW-02", "Doc04 §3 row D-09.4: FLOW-02"),
    ("D-09.4", "FLOW-03", "Doc04 §3 row D-09.4: FLOW-03"),
    ("D-09.4", "FLOW-04", "Doc04 §3 row D-09.4: FLOW-04"),
    ("D-09.4", "FLOW-05", "Doc04 §3 row D-09.4: FLOW-05"),
    # D-10.1: FLOW-03
    ("D-10.1", "FLOW-03", "Doc04 §3 row D-10.1: FLOW-03"),
    # D-10.2: FLOW-03, FLOW-04
    ("D-10.2", "FLOW-03", "Doc04 §3 row D-10.2: FLOW-03"),
    ("D-10.2", "FLOW-04", "Doc04 §3 row D-10.2: FLOW-04"),
    # D-10.3: All production flows → FLOW-01..FLOW-05
    ("D-10.3", "FLOW-01", "Doc04 §3 row D-10.3: All production flows → expanded"),
    ("D-10.3", "FLOW-02", "Doc04 §3 row D-10.3: All production flows → expanded"),
    ("D-10.3", "FLOW-03", "Doc04 §3 row D-10.3: All production flows → expanded"),
    ("D-10.3", "FLOW-04", "Doc04 §3 row D-10.3: All production flows → expanded"),
    ("D-10.3", "FLOW-05", "Doc04 §3 row D-10.3: All production flows → expanded"),
]
assert len(INVOLVES_FLOW_EDGES) == 86, f"INVOLVES_FLOW_EDGES drift: {len(INVOLVES_FLOW_EDGES)} (expected 86)"


# PROCESSES_EDGES: DataFlow → ThirdParty
# Per Doc04 §2.2 subprocessor=Y column + Doc06 §4.1 subprocessor table.
PROCESSES_EDGES = [
    # FLOW-03 → Datadog (logs subprocessor)
    ("FLOW-03", "Datadog", "Doc04 §2.2 line 98: FLOW-03.Subprocessor=Y (Datadog); Doc06 §4.1 row 4"),
    # FLOW-04 → Auth0 (auth subprocessor)
    ("FLOW-04", "Auth0", "Doc04 §2.2 line 99: FLOW-04.Subprocessor=Y (Auth0); Doc06 §4.1 row 3"),
    # FLOW-05 → Stripe (payment subprocessor)
    ("FLOW-05", "Stripe", "Doc04 §2.2 line 100: FLOW-05.Subprocessor=Y (Stripe); Doc06 §4.1 row 2"),
]
assert len(PROCESSES_EDGES) == 3, f"PROCESSES_EDGES drift: {len(PROCESSES_EDGES)} (expected 3)"


# PROCESSED_BY_EDGES: PersonalDataCategory → System
# Per Doc04 §2.3 'Systems Processing' column; only SYS-* ids become edges
# (STORE-01/02 references are skipped per the Phase B brief — STORE is a
# DataStore, not a System; surface as audit if needed in future).
PROCESSED_BY_EDGES = [
    # Email addresses: SYS-01, SYS-02, SYS-03
    ("PDC-EMAIL", "SYS-01", "Doc04 §2.3 line 106: SYS-01"),
    ("PDC-EMAIL", "SYS-02", "Doc04 §2.3 line 106: SYS-02"),
    ("PDC-EMAIL", "SYS-03", "Doc04 §2.3 line 106: SYS-03"),
    # Names: SYS-01, SYS-03
    ("PDC-NAMES", "SYS-01", "Doc04 §2.3 line 107: SYS-01"),
    ("PDC-NAMES", "SYS-03", "Doc04 §2.3 line 107: SYS-03"),
    # Project data: SYS-01, SYS-03
    ("PDC-PROJECT", "SYS-01", "Doc04 §2.3 line 108: SYS-01"),
    ("PDC-PROJECT", "SYS-03", "Doc04 §2.3 line 108: SYS-03"),
    # Payment and billing data: SYS-01 (Stripe handled via PROCESSED_BY_3P)
    ("PDC-PAYMENT", "SYS-01", "Doc04 §2.3 line 109: SYS-01 billing metadata"),
]
assert len(PROCESSED_BY_EDGES) == 8, f"PROCESSED_BY_EDGES drift: {len(PROCESSED_BY_EDGES)} (expected 8)"


# PROCESSED_BY_3P_EDGES: PersonalDataCategory → ThirdParty
# Per Doc04 §2.3 'Stripe hosted checkout' reference for payment data + Doc06 §4.1.
PROCESSED_BY_3P_EDGES = [
    # Payment and billing data → Stripe (hosted checkout; tokenised card data)
    ("PDC-PAYMENT", "Stripe", "Doc04 §2.3 line 109: 'Stripe hosted checkout' for Payment data; Doc06 §4.1 row 2"),
]
assert len(PROCESSED_BY_3P_EDGES) == 1, f"PROCESSED_BY_3P_EDGES drift: {len(PROCESSED_BY_3P_EDGES)} (expected 1)"


# CAPTURES_EDGES: DataSubjectCategory → PersonalDataCategory
# Per Doc04 §2.4 'Data Categories' column; one edge per category captured.
CAPTURES_EDGES = [
    # EU customers: Email, name, account metadata, project data, billing metadata
    ("DSC-EU-CUSTOMERS", "PDC-EMAIL", "Doc04 §2.4 line 115: Email"),
    ("DSC-EU-CUSTOMERS", "PDC-NAMES", "Doc04 §2.4 line 115: name"),
    ("DSC-EU-CUSTOMERS", "PDC-PROJECT", "Doc04 §2.4 line 115: project data"),
    ("DSC-EU-CUSTOMERS", "PDC-PAYMENT", "Doc04 §2.4 line 115: billing metadata"),
    # Free-tier users: Email, name, project data
    ("DSC-FREE-TIER", "PDC-EMAIL", "Doc04 §2.4 line 116: Email"),
    ("DSC-FREE-TIER", "PDC-NAMES", "Doc04 §2.4 line 116: name where provided"),
    ("DSC-FREE-TIER", "PDC-PROJECT", "Doc04 §2.4 line 116: project data"),
    # Enterprise end users: Email, name, project data
    ("DSC-ENTERPRISE-END-USERS", "PDC-EMAIL", "Doc04 §2.4 line 117: Email"),
    ("DSC-ENTERPRISE-END-USERS", "PDC-NAMES", "Doc04 §2.4 line 117: name"),
    ("DSC-ENTERPRISE-END-USERS", "PDC-PROJECT", "Doc04 §2.4 line 117: project data controlled by enterprise customer"),
]
assert len(CAPTURES_EDGES) == 10, f"CAPTURES_EDGES drift: {len(CAPTURES_EDGES)} (expected 10)"


# CORRESPONDS_TO_EDGES: ThirdParty → Stakeholder
# Per the Phase B brief: only AWS and Stripe have STK-* counterparts.
# (NEW-02 audit surfaces the 4 vendor gap: Auth0, Datadog, GitHub, Snyk.)
CORRESPONDS_TO_EDGES = [
    ("AWS", "STK-AWS-01", "Doc03 §3.1 row 7: STK-AWS-01 ↔ Doc06 §2 + §5: AWS vendor"),
    ("Stripe", "STK-STRIPE-01", "Doc03 §3.1 row 6: STK-STRIPE-01 ↔ Doc06 §2 + §5: Stripe vendor"),
]
assert len(CORRESPONDS_TO_EDGES) == 2, f"CORRESPONDS_TO_EDGES drift: {len(CORRESPONDS_TO_EDGES)} (expected 2)"


# ---------------------------------------------------------------------------
# === Phase C (Doc08 §9 + Doc12 §4) ===
# 54 article verification rows (28 GDPR + 26 CRA) — Doc08 §9
# Source: Doc08_Regulatory_Applicability.md §9 (rows 287-340).
# Mapping: §9 table is ordered CRA section (rows 0-25, Art. 1..26) then GDPR
# section (rows 26-53, Art. 1,2,3,5..9,12..22,25,28,30..35,37); each row is
# assigned to clause_id by ordinal position within its regulation slice:
#   rows 0-25  -> CRA-C01..CRA-C26 (26 rows)
#   rows 26-53 -> GDPR-C01..GDPR-C28 (28 rows)
# Asymmetries (see NEW-06 audit):
#   (a) §9 row 40 (the 15th GDPR row, index 40 in §9) covers Art. 35;
#       that row is assigned to GDPR-C27 by ordinal.  GDPR-C28 in CLAUSES
#       is labelled "Art. 35(1)" but does NOT have a corresponding §9 row.
#   (b) §9 row 53 (the last GDPR row, index 53 in §9) covers Art. 37
#       (Designation of DPO, D-08.2); that row is assigned to GDPR-C28 by
#       ordinal.  GDPR-C28 in CLAUSES is labelled "Art. 35(1) (DPIA)"; the
#       §9 row's REAL clause id (Art. 37 / DPO Designation) does not exist
#       as a RegulatoryClause in phase1_graph.json.
ART_VERIFICATION = [
    { "clause_id": 'CRA-C01',
      "topic": 'Subject matter and scope',
      "article": 'Art. 1',
      "sub_domains": ['D-07.1'],
      "obligated_party": 'manufacturer',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-07.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (SSDF checklist + SAMM maturity)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C02',
      "topic": 'Definitions',
      "article": 'Art. 2',
      "sub_domains": ['D-07.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-07.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (SSDF checklist + SAMM maturity)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C03',
      "topic": 'Security requirements',
      "article": 'Art. 3',
      "sub_domains": ['D-03.4'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-03.4',
      "evidence_type": 'DEMONSTRATE + INSPECT (account-level block + Firebase config)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C04',
      "topic": 'Vulnerability handling',
      "article": 'Art. 4',
      "sub_domains": ['D-02.2'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-02.2',
      "evidence_type": 'DEMONSTRATE + INSPECT (Patch Manager logs + patch log)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C05',
      "topic": 'Security updates',
      "article": 'Art. 5',
      "sub_domains": ['D-02.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-02.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (CI scan output + advisory feed)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C06',
      "topic": 'Incident reporting',
      "article": 'Art. 6',
      "sub_domains": ['D-04.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-04.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (CloudWatch alarms + GuardDuty)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C07',
      "topic": 'Supply chain security',
      "article": 'Art. 7',
      "sub_domains": ['D-06.2'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-06.2',
      "evidence_type": 'DEMONSTRATE + INSPECT (SBOM per release)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C08',
      "topic": 'Secure defaults',
      "article": 'Art. 8',
      "sub_domains": ['D-03.4'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-03.4',
      "evidence_type": 'DEMONSTRATE + INSPECT (account-level block + Firebase config)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C09',
      "topic": 'Password security',
      "article": 'Art. 9',
      "sub_domains": ['D-03.2'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-03.2',
      "evidence_type": 'INSPECT (Firebase MFA enforcement + reset flow test)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C10',
      "topic": 'Identity authentication',
      "article": 'Art. 10',
      "sub_domains": ['D-03.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-03.1',
      "evidence_type": 'INSPECT (Firebase Auth user list + quarterly orphan scan)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C11',
      "topic": 'Data erasure',
      "article": 'Art. 11',
      "sub_domains": ['D-05.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (erasure API + backup exclude policy)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C12',
      "topic": 'Availability at end of support',
      "article": 'Art. 12',
      "sub_domains": ['D-10.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-10.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (CloudWatch + GuardDuty)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C13',
      "topic": 'Technical documentation',
      "article": 'Art. 13',
      "sub_domains": ['D-09.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-09.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (policy template + review cadence)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C14',
      "topic": 'Conformity assessment',
      "article": 'Art. 14',
      "sub_domains": ['D-10.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-10.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (quarterly checklist + annual self-attestation)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C15',
      "topic": 'CE marking',
      "article": 'Art. 15',
      "sub_domains": ['D-01.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-01.3',
      "evidence_type": 'INSPECT (KMS rotation status + key-custody review)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C16',
      "topic": 'Market surveillance',
      "article": 'Art. 16',
      "sub_domains": ['D-06.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-06.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (DPA template + sub-processor list)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C17',
      "topic": 'Essential requirements for ICT products',
      "article": 'Art. 17',
      "sub_domains": ['D-02.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-02.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (CI scan output + advisory feed)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C18',
      "topic": 'Security by design',
      "article": 'Art. 18',
      "sub_domains": ['D-07.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-07.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (SSDF checklist + SAMM maturity)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C19',
      "topic": 'Vulnerability handling and disclosure',
      "article": 'Art. 19',
      "sub_domains": ['D-02.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-02.3',
      "evidence_type": 'INSPECT (security.txt 200 + CVD page test email)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C20',
      "topic": 'Reporting incidents',
      "article": 'Art. 20',
      "sub_domains": ['D-04.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-04.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (tabletop 24h notification drill)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C21',
      "topic": 'EU declarative conformity',
      "article": 'Art. 21',
      "sub_domains": ['D-10.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-10.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (quarterly checklist + annual self-attestation)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C22',
      "topic": 'Traceability',
      "article": 'Art. 22',
      "sub_domains": ['D-10.2'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-10.2',
      "evidence_type": 'DEMONSTRATE + INSPECT (CloudTrail + Object Lock + 7y)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C23',
      "topic": 'Software security',
      "article": 'Art. 23',
      "sub_domains": ['D-07.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-07.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (SSDF checklist + SAMM maturity)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C24',
      "topic": 'Encrypted data storage',
      "article": 'Art. 24',
      "sub_domains": ['D-01.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-01.1',
      "evidence_type": 'INSPECT (config audit + annual review)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C25',
      "topic": 'Unauthorised access prevention',
      "article": 'Art. 25',
      "sub_domains": ['D-01.2'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-01.2',
      "evidence_type": 'INSPECT (config audit + annual cert renewal)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'CRA-C26',
      "topic": 'Resilience to outages',
      "article": 'Art. 26',
      "sub_domains": ['D-04.4'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-04.4',
      "evidence_type": 'DEMONSTRATE + INSPECT (AWS Backup + quarterly DR test)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C01',
      "topic": 'Lawfulness of processing',
      "article": 'Art. 1',
      "sub_domains": ['D-05.1'],
      "obligated_party": 'controller',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (schema validation + log scrub review)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C02',
      "topic": 'Material scope',
      "article": 'Art. 2',
      "sub_domains": ['D-05.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (schema validation + log scrub review)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C03',
      "topic": 'Territorial scope',
      "article": 'Art. 3',
      "sub_domains": ['D-09.2'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-09.2',
      "evidence_type": 'DEMONSTRATE + INSPECT (DPIA + CRA-RA unified template)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C04',
      "topic": 'Principles relating to processing',
      "article": 'Art. 5',
      "sub_domains": ['D-01.1'],
      "obligated_party": 'controller + processor',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-01.1',
      "evidence_type": 'INSPECT (config audit + annual review)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C05',
      "topic": 'Lawfulness of processing',
      "article": 'Art. 6',
      "sub_domains": ['D-05.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (schema validation + log scrub review)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C06',
      "topic": 'Conditions for consent',
      "article": 'Art. 7',
      "sub_domains": ['D-05.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (schema validation + log scrub review)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C07',
      "topic": "Conditions for child's consent",
      "article": 'Art. 8',
      "sub_domains": ['D-05.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (schema validation + log scrub review)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C08',
      "topic": 'Processing of special categories',
      "article": 'Art. 9',
      "sub_domains": ['D-05.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (erasure API + backup exclude policy)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C09',
      "topic": 'Transparent information and communication',
      "article": 'Art. 12',
      "sub_domains": ['D-09.4'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-09.4',
      "evidence_type": 'DEMONSTRATE + INSPECT (RoPA + 10y retention check)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C10',
      "topic": 'Information to be provided',
      "article": 'Art. 13',
      "sub_domains": ['D-09.4'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-09.4',
      "evidence_type": 'DEMONSTRATE + INSPECT (RoPA + 10y retention check)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C11',
      "topic": 'Information to be provided to data subject',
      "article": 'Art. 14',
      "sub_domains": ['D-09.4'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-09.4',
      "evidence_type": 'DEMONSTRATE + INSPECT (RoPA + 10y retention check)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C12',
      "topic": 'Right of access by data subject',
      "article": 'Art. 15',
      "sub_domains": ['D-05.4'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.4',
      "evidence_type": 'DEMONSTRATE + INSPECT (export endpoint + format check)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C13',
      "topic": 'Right to rectification',
      "article": 'Art. 16',
      "sub_domains": ['D-05.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (erasure API + backup exclude policy)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C14',
      "topic": 'Right to erasure',
      "article": 'Art. 17',
      "sub_domains": ['D-05.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (erasure API + backup exclude policy)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C15',
      "topic": 'Right to restriction of processing',
      "article": 'Art. 18',
      "sub_domains": ['D-05.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (erasure API + backup exclude policy)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C16',
      "topic": 'Notification obligation',
      "article": 'Art. 19',
      "sub_domains": ['D-04.4'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-04.4',
      "evidence_type": 'DEMONSTRATE + INSPECT (AWS Backup + quarterly DR test)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C17',
      "topic": 'Right to data portability',
      "article": 'Art. 20',
      "sub_domains": ['D-05.4'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.4',
      "evidence_type": 'DEMONSTRATE + INSPECT (export endpoint + format check)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C18',
      "topic": 'Right to object',
      "article": 'Art. 21',
      "sub_domains": ['D-05.1'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-05.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (schema validation + log scrub review)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C19',
      "topic": 'Automated decision-making',
      "article": 'Art. 22',
      "sub_domains": ['D-03.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-03.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (IAM policies + RBAC matrix review)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C20',
      "topic": 'Data protection by design',
      "article": 'Art. 25',
      "sub_domains": ['D-07.1'],
      "obligated_party": 'controller + processor',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-07.1',
      "evidence_type": 'DEMONSTRATE + INSPECT (SSDF checklist + SAMM maturity)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C21',
      "topic": 'Processor clauses (DPA, sub-processor auth, processing on instructions, security',
      "article": 'Art. 28',
      "sub_domains": ['D-06.3'],
      "obligated_party": 'controller + processor',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-06.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (DPA template + sub-processor list)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C22',
      "topic": "Records of processing activities (Art. 30(1) controller, Art. 30(2) processor's",
      "article": 'Art. 30',
      "sub_domains": ['D-09.4'],
      "obligated_party": 'controller + processor',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-09.4',
      "evidence_type": 'DEMONSTRATE + INSPECT (RoPA + 10y retention check)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C23',
      "topic": 'Cooperation with supervisory authority',
      "article": 'Art. 31',
      "sub_domains": ['D-04.3'],
      "obligated_party": 'controller + processor',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-04.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (tabletop 24h notification drill)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C24',
      "topic": 'Security of processing (Art. 32(1) controller+processor; Art. 32(2) processor ad',
      "article": 'Art. 32',
      "sub_domains": ['D-01.1'],
      "obligated_party": 'controller + processor',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-01.1',
      "evidence_type": 'INSPECT (config audit + annual review)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C25',
      "topic": 'Breach notification — Art. 33(1) controller to SA within 72h; Art. 33(2) process',
      "article": 'Art. 33',
      "sub_domains": ['D-04.3'],
      "obligated_party": 'controller + processor',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-04.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (tabletop 24h notification drill)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C26',
      "topic": 'Breach notification to data subject',
      "article": 'Art. 34',
      "sub_domains": ['D-04.3'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-04.3',
      "evidence_type": 'DEMONSTRATE + INSPECT (tabletop 24h notification drill)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C27',
      "topic": 'Data protection impact assessment',
      "article": 'Art. 35',
      "sub_domains": ['D-09.2'],
      "obligated_party": '',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-09.2',
      "evidence_type": 'DEMONSTRATE + INSPECT (DPIA + CRA-RA unified template)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
    { "clause_id": 'GDPR-C28',
      "topic": 'Designation of DPO',
      "article": 'Art. 37',
      "sub_domains": ['D-08.2'],
      "obligated_party": 'controller + processor',
      "verification_criteria": 'Operational check per Doc 07c Appendix A §A.1.1/D-08.2',
      "evidence_type": 'INSPECT (annual email + competency matrix review)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
    },
]
assert len(ART_VERIFICATION) == 54, f"ART_VERIFICATION drift: {len(ART_VERIFICATION)}"


# 37 proportionality rows — Doc12 §4 (active only, D-08.3 excluded)
# Source: Doc12_Proportionality_Profile.md §4 (rows 99-136).
# Each row assigned to the active SecurityControlDomain id (D-08.3 omitted).
# The new attrs.tier values match the existing attrs.proportionality_tier
# values from v1.2 — verified one-to-one (37/37 match — see reconcile_test.py).
# When attrs.tier differs from attrs.proportionality_tier for any row, the
# build() function surfaces an audit rather than silently overwriting.
SUBDOMAIN_PROPORTIONALITY = [
    { "sub_domain_id": 'D-01.1',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review; no dedicated in-house program',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Shared (AWS + company)',
      "example_controls": 'AWS S3 / DynamoDB SSE-KMS enabled (AES-256 default); no company-owned KMS program',
      "notes": 'Unified AES-256 baseline satisfies SAME pair',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-01.2',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Shared (AWS + company)',
      "example_controls": 'TLS 1.3 via AWS ACM / CloudFront; certificate auto-renewal',
      "notes": 'TLS 1.3 covers all ingress + egress',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-01.3',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Shared (AWS + company)',
      "example_controls": 'AWS KMS default keys; rotation cadence is AWS-managed',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-01.4',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Shared (AWS + company)',
      "example_controls": 'HMAC + DB constraints via AWS RDS',
      "notes": '',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-02.1',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Shared (tooling + company)',
      "example_controls": 'Trivy + npm audit in CI; OSS advisories',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-02.2',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Shared (AWS + company)',
      "example_controls": 'AWS Systems Manager Patch Manager (auto)',
      "notes": 'Critical patches 24h per Critical Analysis §4',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-02.3',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'security.txt at `/.well-known/security.txt`; CVD page',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-02.4',
      "i": 'BUILD', "p": 'SHOULD', "tier": 'DEFERRED',
      "satisfaction_pattern": '—',
      "evidence_depth": '—',
      "verification_method": '—',
      "ownership": '—',
      "example_controls": 'No OJ mandate for default-class CRA manufacturer; reference NIST SP 800-115 only',
      "notes": 'DEFERRED per §5.2 (MICRO + FTE ≤ 1.0)',
      "risk_if_not_met": 'LOW',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()

      "implementation_priority": 'LOW' },
    { "sub_domain_id": 'D-03.1',
      "i": 'INHERIT (Firebase Auth IO-04)', "p": 'MUST', "tier": 'MINIMAL',
      "satisfaction_pattern": 'INHERIT',
      "evidence_depth": 'Supplier attestation on file (SOC 2 / ISO 27001) + 1-page internal statement',
      "verification_method": 'INSPECT',
      "ownership": 'Supplier (company = validator)',
      "example_controls": 'Firebase Auth baseline; Firebase security documentation',
      "notes": 'OIDC delegation per Critical Analysis §9',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-03.2',
      "i": 'INHERIT (Firebase Auth IO-04)', "p": 'MUST', "tier": 'MINIMAL',
      "satisfaction_pattern": 'INHERIT',
      "evidence_depth": 'Supplier attestation on file + 1-page internal statement',
      "verification_method": 'INSPECT',
      "ownership": 'Supplier (company = validator)',
      "example_controls": 'Firebase Auth MFA; customer-managed encryption keys',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-03.3',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Shared (Firebase + company)',
      "example_controls": 'Firebase Auth RBAC',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-03.4',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'Secure defaults via Firebase config',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-04.1',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Shared (AWS + company)',
      "example_controls": 'CloudWatch alarms + SNS notifications',
      "notes": 'CloudWatch (not enterprise SIEM) per Critical Analysis §9',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-04.2',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'Documented 4h containment playbook',
      "notes": '',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-04.3',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'max-SLA 24h internal; unified incident workflow',
      "notes": '24h internal satisfies GDPR 72h and CRA 24h max-SLA',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-04.4',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Shared (AWS + company)',
      "example_controls": 'AWS Backup; RTO 24h (per Critical Analysis §4)',
      "notes": 'RTO 24h replaces 4h unrealistic target',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-05.1',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'Field-level enforcement in schema',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-05.2',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'Retention policy (7y audit logs; 30d DSAR working data)',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-05.3',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'Erasure API endpoint',
      "notes": '',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-05.4',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'JSON export endpoint',
      "notes": 'D-05.3 + D-05.4 share GDPR Art. 20-17 sub-SO pair',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-06.1',
      "i": 'INHERIT (DPA validation)', "p": 'MUST', "tier": 'MINIMAL',
      "satisfaction_pattern": 'INHERIT',
      "evidence_depth": 'Supplier attestation on file + 1-page internal statement',
      "verification_method": 'INSPECT',
      "ownership": 'Supplier (company = validator)',
      "example_controls": 'DPA validation against GDPR Art. 28; supplier security clauses',
      "notes": 'Annual manual review per Critical Analysis §9',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-06.2',
      "i": 'BUILD (CRA sole)', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'CycloneDX SBOM in CI/CD per release',
      "notes": 'Closes GAP-003 (Doc 07 §7)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-06.3',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'DPA template + supplier security clauses',
      "notes": '',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-06.4',
      "i": 'INHERIT (AWS/Stripe/Firebase)', "p": 'MUST', "tier": 'MINIMAL',
      "satisfaction_pattern": 'INHERIT',
      "evidence_depth": 'Supplier attestation on file + 1-page internal statement',
      "verification_method": 'INSPECT',
      "ownership": 'Supplier (company = validator)',
      "example_controls": 'AWS / Stripe / Firebase boundary inherited from their attestations',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-07.1',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'NIST SSDF + OWASP SAMM baseline',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-07.2',
      "i": 'BUILD (CRA only)', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'SAST in CI; coding standards documentation',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-07.3',
      "i": 'BUILD (CRA only)', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'CI gates (block critical vulns); pipeline-as-code',
      "notes": 'Closes Priority 1 FR-01/04 (Critical Analysis §7.1)',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-07.4',
      "i": 'BUILD (CRA only)', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'Change management log (PR review + merge controls)',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-08.1',
      "i": 'INHERIT (vendor docs)', "p": 'MUST', "tier": 'MINIMAL',
      "satisfaction_pattern": 'INHERIT',
      "evidence_depth": 'Supplier attestation on file + 1-page internal statement',
      "verification_method": 'INSPECT',
      "ownership": 'Supplier (company = validator)',
      "example_controls": 'Vendor security awareness documentation on file',
      "notes": 'Replaces deferred phishing simulation (Critical §7.3)',
      "risk_if_not_met": 'LOW',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-08.2',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'Annual security awareness email + role-specific docs (admin/dev/DPO)',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-09.1',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'Security policy template (Doc 09 family input)',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-09.2',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'DPIA template + CRA risk assessment template (unified, dual-output)',
      "notes": 'Resolves EVT-002 (Doc 07 §5.4)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-09.3',
      "i": 'BUILD (CRA partial)', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'Annex VII §1-§2 architecture documentation (CRA partial)',
      "notes": '',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-09.4',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'RoPA template (Doc 09 input)',
      "notes": 'Closes GAP-001 (Doc 07 §7)',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-10.1',
      "i": 'BUILD (TEN-03: opt-in/opt-out separation)', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Shared (AWS + company)',
      "example_controls": 'CloudWatch (not enterprise SIEM); per Critical Analysis',
      "notes": 'opt-in/opt-out separation per TEN-03',
      "risk_if_not_met": 'MEDIUM',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-10.2',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Shared (AWS + company)',
      "example_controls": 'CloudTrail + tamper-evident S3 log bucket',
      "notes": '7-year retention per Critical Analysis §10.2',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
    { "sub_domain_id": 'D-10.3',
      "i": 'BUILD', "p": 'MUST', "tier": 'LIGHTWEIGHT',
      "satisfaction_pattern": 'BUY_MANAGED',
      "evidence_depth": 'Managed-service config documented + annual review',
      "verification_method": 'DEMONSTRATE + INSPECT',
      "ownership": 'Company',
      "example_controls": 'Quarterly compliance review checklist',
      "notes": '',
      "risk_if_not_met": 'HIGH',
      "evidence_ids": ["EV-TBD"],  # legacy literal; replaced by build()
      "implementation_priority": 'HIGH' },
]
assert len(SUBDOMAIN_PROPORTIONALITY) == 37, f"SUBDOMAIN_PROPORTIONALITY drift: {len(SUBDOMAIN_PROPORTIONALITY)}"


# 8b. EvidenceItem seed — v1.6 (MATURITY_MODEL_CSF_STRICT.md §6)
# ---------------------------------------------------------------------------
# Each EvidenceItem:
#   - is anchored to ONE sub-domain (D-XX.Y) — Scale B (Coverage) OR Scale A (Capability)
#   - cites ONE outcome (clause id for Scale B; CSF subcategory id for Scale A)
#   - cites >=1 source by ID; sources MUST resolve to existing graph nodes
#     (RegulatoryClause/System/DataStore/DataFlow/Stakeholder/RaciRole/RaciActivity/NistControl)
#   - observed=True/False (False → CoverageGap candidate; still recorded for transparency)
# Schema citation: 00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §6.
# Crosswalk authority: 00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/OVERLAY_NIST_CSF_2.0.md §2.
# ---------------------------------------------------------------------------
EVIDENCE_ITEMS = [
    # Scale B (Coverage) — one per active sub-domain, anchored on the first applicable clause
    { "ev_id": "EV-D-01.1-001", "subdomain_id": "D-01.1", "scale": "coverage",
      "outcome": "GDPR-C24", "claim": "S3 SSE-KMS + DynamoDB encryption documented in Doc04 §1.1 (SYS-01 AWS S3 + SYS-02 DynamoDB).",
      "sources": ["SYS-01", "SYS-02", "STORE-01"], "observed": True },
    { "ev_id": "EV-D-01.2-001", "subdomain_id": "D-01.2", "scale": "coverage",
      "outcome": "GDPR-C04", "claim": "TLS 1.3 via AWS ACM/CloudFront enforced on all ingress + egress (Doc04 §1.4).",
      "sources": ["SYS-03", "FLOW-01"], "observed": True },
    { "ev_id": "EV-D-01.3-001", "subdomain_id": "D-01.3", "scale": "coverage",
      "outcome": "CRA-C15", "claim": "AWS KMS default keys; rotation cadence is AWS-managed (no in-house KMS).",
      "sources": ["SYS-01"], "observed": True },
    { "ev_id": "EV-D-01.4-001", "subdomain_id": "D-01.4", "scale": "coverage",
      "outcome": "GDPR-C24", "claim": "HMAC + DB constraints via AWS RDS documented in Doc04 §1.1 (SYS-04 RDS).",
      "sources": ["SYS-04", "STORE-02"], "observed": True },
    { "ev_id": "EV-D-02.1-001", "subdomain_id": "D-02.1", "scale": "coverage",
      "outcome": "CRA-C05", "claim": "Trivy + npm audit run in CI (GitHub Actions); OSS advisory feed monitored (Doc12 §4 D-02.1).",
      "sources": ["SYS-05"], "observed": True },
    { "ev_id": "EV-D-02.2-001", "subdomain_id": "D-02.2", "scale": "coverage",
      "outcome": "CRA-C04", "claim": "AWS Systems Manager Patch Manager (auto) configured for critical patches 24h SLA (Doc12 §4 D-02.2).",
      "sources": ["SYS-01"], "observed": True },
    { "ev_id": "EV-D-02.3-001", "subdomain_id": "D-02.3", "scale": "coverage",
      "outcome": "CRA-C19", "claim": "security.txt at /.well-known/security.txt + CVD page published (Doc12 §4 D-02.3).",
      "sources": ["SYS-05"], "observed": True },
    { "ev_id": "EV-D-02.4-001", "subdomain_id": "D-02.4", "scale": "coverage",
      "outcome": "GDPR-C27", "claim": "Threat-led penetration testing DEFERRED per §5.2 (MICRO + FTE <= 1.0); recorded as gap, not absent.",
      "sources": ["Doc12 §5.2"], "observed": False },
    { "ev_id": "EV-D-03.1-001", "subdomain_id": "D-03.1", "scale": "coverage",
      "outcome": "CRA-C10", "claim": "Firebase Auth baseline + quarterly orphan scan (Doc12 §4 D-03.1, Doc07 §4).",
      "sources": ["SYS-02", "ACT-03"], "observed": True },
    { "ev_id": "EV-D-03.2-001", "subdomain_id": "D-03.2", "scale": "coverage",
      "outcome": "CRA-C09", "claim": "Firebase Auth MFA enforced; reset flow tested (Doc07 §4.3).",
      "sources": ["SYS-02", "ACT-04"], "observed": True },
    { "ev_id": "EV-D-03.3-001", "subdomain_id": "D-03.3", "scale": "coverage",
      "outcome": "GDPR-C19", "claim": "RBAC matrix in Doc07 §3; quarterly access review (ACT-05).",
      "sources": ["Doc07 §3", "ACT-05"], "observed": True },
    { "ev_id": "EV-D-03.4-001", "subdomain_id": "D-03.4", "scale": "coverage",
      "outcome": "CRA-C03", "claim": "Account-level block + Firebase secure defaults applied at provisioning (Doc07 §4.4).",
      "sources": ["SYS-02", "ACT-06"], "observed": True },
    { "ev_id": "EV-D-04.1-001", "subdomain_id": "D-04.1", "scale": "coverage",
      "outcome": "CRA-C06", "claim": "CloudWatch alarms + GuardDuty enabled; anomaly detection feed monitored (Doc12 §4 D-04.1).",
      "sources": ["SYS-01"], "observed": True },
    { "ev_id": "EV-D-04.2-001", "subdomain_id": "D-04.2", "scale": "coverage",
      "outcome": "GDPR-C18", "claim": "Containment runbook referenced in Doc04 §2.5; tested annually.",
      "sources": ["Doc04 §2.5", "ACT-08"], "observed": True },
    { "ev_id": "EV-D-04.3-001", "subdomain_id": "D-04.3", "scale": "coverage",
      "outcome": "GDPR-C25", "claim": "Breach notification SLA: 24h to SA / controller (max-SLA per T-001 resolution).",
      "sources": ["Doc11 T-001", "ACT-09"], "observed": True },
    { "ev_id": "EV-D-04.4-001", "subdomain_id": "D-04.4", "scale": "coverage",
      "outcome": "CRA-C26", "claim": "Recovery time objective 24h (RDS automated snapshots + cross-region replication; Doc04 §2.1).",
      "sources": ["SYS-04", "STORE-02"], "observed": True },
    { "ev_id": "EV-D-05.1-001", "subdomain_id": "D-05.1", "scale": "coverage",
      "outcome": "GDPR-C05", "claim": "Data minimisation policy in Doc09 §3; intake form captures data categories explicitly.",
      "sources": ["Doc09 §3", "Doc02 §A.2"], "observed": True },
    { "ev_id": "EV-D-05.2-001", "subdomain_id": "D-05.2", "scale": "coverage",
      "outcome": "GDPR-C05", "claim": "Retention periods documented per PersonalDataCategory in Doc04 §2.3.",
      "sources": ["Doc04 §2.3", "STORE-01"], "observed": True },
    { "ev_id": "EV-D-05.3-001", "subdomain_id": "D-05.3", "scale": "coverage",
      "outcome": "GDPR-C14", "claim": "Erasure API + backup exclude policy (Doc07 §4.5, Doc12 §4 D-05.3).",
      "sources": ["ACT-10", "STORE-03"], "observed": True },
    { "ev_id": "EV-D-05.4-001", "subdomain_id": "D-05.4", "scale": "coverage",
      "outcome": "GDPR-C17", "claim": "Portability endpoint exposed to data subjects (Doc07 §4.5).",
      "sources": ["ACT-10"], "observed": True },
    { "ev_id": "EV-D-06.1-001", "subdomain_id": "D-06.1", "scale": "coverage",
      "outcome": "GDPR-C21", "claim": "Vendor risk assessment template in Doc06 §3; reviewed annually.",
      "sources": ["Doc06 §3"], "observed": True },
    { "ev_id": "EV-D-06.2-001", "subdomain_id": "D-06.2", "scale": "coverage",
      "outcome": "CRA-C07", "claim": "SBOM generated per release (CycloneDX, GitHub Actions workflow; Doc12 §4 D-06.2).",
      "sources": ["SYS-05"], "observed": True },
    { "ev_id": "EV-D-06.3-001", "subdomain_id": "D-06.3", "scale": "coverage",
      "outcome": "GDPR-C21", "claim": "DPAs in place for AWS/Stripe/Auth0/Datadog/GitHub/Snyk (Doc06 §5).",
      "sources": ["AWS", "Stripe", "Auth0", "Datadog", "GitHub", "Snyk"], "observed": True },
    { "ev_id": "EV-D-07.1-001", "subdomain_id": "D-07.1", "scale": "coverage",
      "outcome": "GDPR-C20", "claim": "Secure-by-design checklist (SSDF + SAMM) referenced in Doc07 §4.1; PR review enforced.",
      "sources": ["ACT-01", "ACT-02"], "observed": True },
    { "ev_id": "EV-D-08.1-001", "subdomain_id": "D-08.1", "scale": "coverage",
      "outcome": "GDPR-C09", "claim": "Annual security awareness training (Doc07 §4.6).",
      "sources": ["ACT-11"], "observed": True },
    { "ev_id": "EV-D-08.2-001", "subdomain_id": "D-08.2", "scale": "coverage",
      "outcome": "GDPR-C28", "claim": "DPO designated (ROLE-DPO) with backup; documented competence matrix (Doc07 §2).",
      "sources": ["ROLE-DPO", "Doc07 §2"], "observed": True },
    { "ev_id": "EV-D-09.1-001", "subdomain_id": "D-09.1", "scale": "coverage",
      "outcome": "CRA-C13", "claim": "Information security policy published; revision log kept (Doc09 §1).",
      "sources": ["Doc09 §1"], "observed": True },
    { "ev_id": "EV-D-09.2-001", "subdomain_id": "D-09.2", "scale": "coverage",
      "outcome": "GDPR-C27", "claim": "DPIA template + risk register used; review quarterly (Doc11 §2).",
      "sources": ["Doc11 §2", "GAP-001"], "observed": True },
    { "ev_id": "EV-D-09.4-001", "subdomain_id": "D-09.4", "scale": "coverage",
      "outcome": "GDPR-C22", "claim": "Records of processing activities maintained (Doc11 §3, Doc04 §3 cross-ref).",
      "sources": ["Doc11 §3", "Doc04 §3"], "observed": True },
    { "ev_id": "EV-D-10.1-001", "subdomain_id": "D-10.1", "scale": "coverage",
      "outcome": "CRA-C12", "claim": "End-of-support availability SLA tracked in Doc04 §2.1.",
      "sources": ["Doc04 §2.1"], "observed": True },
    { "ev_id": "EV-D-10.2-001", "subdomain_id": "D-10.2", "scale": "coverage",
      "outcome": "CRA-C22", "claim": "CloudTrail + application audit logs centralised (Doc07 §4.7).",
      "sources": ["ACT-12", "SYS-01"], "observed": True },
    { "ev_id": "EV-D-10.3-001", "subdomain_id": "D-10.3", "scale": "coverage",
      "outcome": "CRA-C14", "claim": "Annual conformity self-assessment (Doc14 §4 - placeholder, gap registered).",
      "sources": ["Doc11 §7"], "observed": False },

    # Scale A (Capability) — selected sub-domains anchored on CSF subcategory outcomes
    # per OVERLAY_NIST_CSF_2.0.md §2. These are OBSERVED evidence references
    # for the §4 escada decision; not full Tier-decision nodes (those come in
    # Phase 2 once Org/Function scope is decided with the human — P7).
    { "ev_id": "EV-D-01.1-002", "subdomain_id": "D-01.1", "scale": "capability",
      "outcome": "PR.DS-01", "claim": "Data-at-rest encryption baseline present (Doc04 §1.1); no formal classification procedure documented yet (blocks T3 Repeatable for PROTECT).",
      "sources": ["SYS-01", "Doc04 §1.1"], "observed": True },
    { "ev_id": "EV-D-02.1-002", "subdomain_id": "D-02.1", "scale": "capability",
      "outcome": "ID.RA-01", "claim": "CI vulnerability scan produces a list; severity tagged informally (no documented register + owner SLA - partial T1/T2 for IDENTIFY).",
      "sources": ["SYS-05"], "observed": True },
    { "ev_id": "EV-D-09.1-002", "subdomain_id": "D-09.1", "scale": "capability",
      "outcome": "GV.PO-01", "claim": "Policy exists and is approved; not yet reviewed on a fixed cadence (between T1 and T2 for GOVERN).",
      "sources": ["Doc09 §1"], "observed": True },
    { "ev_id": "EV-D-09.2-002", "subdomain_id": "D-09.2", "scale": "capability",
      "outcome": "ID.RA-04", "claim": "Threat + risk assessment done for the SaaS product; no enterprise-wide threat intel feed (blocks T2 fully).",
      "sources": ["Doc11 §2"], "observed": True },
    { "ev_id": "EV-D-04.1-002", "subdomain_id": "D-04.1", "scale": "capability",
      "outcome": "DE.AE-02", "claim": "CloudWatch alarms + GuardDuty; no documented triage playbook yet (DETECT at T1).",
      "sources": ["SYS-01", "Doc07 §4.8"], "observed": True },
    { "ev_id": "EV-D-04.2-002", "subdomain_id": "D-04.2", "scale": "capability",
      "outcome": "RS.MI-01", "claim": "Containment runbook referenced; tested ad-hoc (RESPOND at T1/T2 borderline).",
      "sources": ["Doc04 §2.5", "ACT-08"], "observed": True },
    { "ev_id": "EV-D-04.4-002", "subdomain_id": "D-04.4", "scale": "capability",
      "outcome": "RC.RP-01", "claim": "Recovery procedure documented for RDS snapshots; cross-region replication not yet enabled (RECOVER below T2; documented gap).",
      "sources": ["SYS-04", "STORE-02"], "observed": False },
    { "ev_id": "EV-D-10.1-002", "subdomain_id": "D-10.1", "scale": "capability",
      "outcome": "DE.CM-01", "claim": "Network monitoring active; no continuous configuration monitoring (DETECT at T1).",
      "sources": ["SYS-01"], "observed": True },
    { "ev_id": "EV-D-10.2-002", "subdomain_id": "D-10.2", "scale": "capability",
      "outcome": "PR.PS-04", "claim": "Audit logs centralised (CloudTrail); retention <= 90 days only (PROTECT at T2 borderline).",
      "sources": ["ACT-12"], "observed": True },
    { "ev_id": "EV-D-08.2-002", "subdomain_id": "D-08.2", "scale": "capability",
      "outcome": "PR.AT-02", "claim": "Awareness training exists; not role-specific for engineering (PROTECT at T1).",
      "sources": ["ROLE-DPO"], "observed": True },

    # Gap evidence (observed=False / partial) for not_covered / sole-authority-on-non-applicable-reg sub-domains
    { "ev_id": "EV-D-06.4-001", "subdomain_id": "D-06.4", "scale": "coverage",
      "outcome": "CRA-C07", "claim": "Third-Party Boundary Management NOT_ADDRESSED - sole_authority=DORA, DORA not applicable (not financial entity).",
      "sources": ["Doc06 §6", "Doc11 §7"], "observed": False },
    { "ev_id": "EV-D-07.2-001", "subdomain_id": "D-07.2", "scale": "coverage",
      "outcome": "CRA-C18", "claim": "Secure Coding Practices PARTIAL - best-effort SSDF/SAMM adopted; full DORA-grade program out of scope (sole_authority=DORA, not applicable).",
      "sources": ["Doc07 §4.1", "Doc11 §7"], "observed": True },
    { "ev_id": "EV-D-07.3-001", "subdomain_id": "D-07.3", "scale": "coverage",
      "outcome": "CRA-C04", "claim": "CI/CD Pipeline Security PARTIAL - GitHub Actions best practices in place; NIS2-grade controls not required (below 50 FTE).",
      "sources": ["SYS-05", "Doc07 §4.1"], "observed": True },
    { "ev_id": "EV-D-07.4-001", "subdomain_id": "D-07.4", "scale": "coverage",
      "outcome": "CRA-C04", "claim": "Change Management PARTIAL - PR review enforced; full DORA-grade CMDB not in place (sole_authority=DORA, not applicable).",
      "sources": ["Doc07 §4.1"], "observed": True },
    { "ev_id": "EV-D-09.3-001", "subdomain_id": "D-09.3", "scale": "coverage",
      "outcome": "CRA-C13", "claim": "Asset Inventories PARTIAL - Doc04 §1.1 has systems/store inventory; DORA-grade CMDB not maintained (sole_authority=DORA, not applicable).",
      "sources": ["Doc04 §1.1"], "observed": True },

    # Scale A (Capability) — NIST Privacy Framework 1.0 anchors (overlays PF)
    # Authority: 00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/OVERLAY_NIST_PF_1.1.md §2.
    # 10 outcomes, one per Function (5 PF Functions covered; some doubled for richer radar shape).
    { "ev_id": "EV-D-09.1-003", "subdomain_id": "D-09.1", "scale": "capability",
      "outcome": "GV-PO-P1", "claim": "Privacy governance roles established (Doc09 §1; ROLE-DPO designated); not yet enterprise-wide formalisation (GOVERN-P between T1/T2).",
      "sources": ["Doc09 §1", "ROLE-DPO"], "observed": True },
    { "ev_id": "EV-D-09.4-003", "subdomain_id": "D-09.4", "scale": "capability",
      "outcome": "GV-PO-P5", "claim": "Privacy policies aligned with applicable laws (Doc11 §3 RoPA cross-ref + GDPR Art. 24/25/30) (GOVERN-P T2 borderline).",
      "sources": ["Doc11 §3"], "observed": True },
    { "ev_id": "EV-D-08.2-003", "subdomain_id": "D-08.2", "scale": "capability",
      "outcome": "GV-AT-P1", "claim": "Privacy awareness training exists (Doc07 §4.6); DPO-led, not yet role-specific for engineering (GOVERN-P at T1).",
      "sources": ["Doc07 §4.6", "ROLE-DPO"], "observed": True },
    { "ev_id": "EV-D-09.2-003", "subdomain_id": "D-09.2", "scale": "capability",
      "outcome": "GV-MA-P1", "claim": "Privacy risk review on a quarterly cadence (Doc11 §2 + GAP-001); not yet continuous (GOVERN-P between T1/T2).",
      "sources": ["Doc11 §2", "GAP-001"], "observed": True },
    { "ev_id": "EV-D-09.4-004", "subdomain_id": "D-09.4", "scale": "capability",
      "outcome": "ID-IM-P1", "claim": "Data processing inventory (RoPA) maintained (Doc11 §3 + Doc04 §2.3) (IDENTIFY-P T2 borderline).",
      "sources": ["Doc11 §3", "Doc04 §2.3"], "observed": True },
    { "ev_id": "EV-D-09.2-004", "subdomain_id": "D-09.2", "scale": "capability",
      "outcome": "ID-RA-P3", "claim": "Privacy risk assessment done for data processing (Doc11 §2 DPIA template) (IDENTIFY-P T2).",
      "sources": ["Doc11 §2"], "observed": True },
    { "ev_id": "EV-D-01.1-003", "subdomain_id": "D-01.1", "scale": "capability",
      "outcome": "PR-PO-P1", "claim": "Data confidentiality, integrity, availability baseline present (Doc04 §1.1 encryption baseline) (PROTECT-P T2 borderline).",
      "sources": ["SYS-01", "Doc04 §1.1"], "observed": True },
    { "ev_id": "EV-D-04.3-003", "subdomain_id": "D-04.3", "scale": "capability",
      "outcome": "CM-PO-P1", "claim": "Communication of privacy practices (Doc07 §4.5 + Doc09 §3) and breach notification SLA (COMMUNICATE-P T2).",
      "sources": ["Doc07 §4.5", "Doc09 §3", "ACT-09"], "observed": True },
    { "ev_id": "EV-D-05.1-003", "subdomain_id": "D-05.1", "scale": "capability",
      "outcome": "CT-PO-P4", "claim": "Data processing policies/purpose limitation (Doc09 §3 + Doc02 §A.2) (CONTROL-P T2).",
      "sources": ["Doc09 §3", "Doc02 §A.2"], "observed": True },
    { "ev_id": "EV-D-05.3-003", "subdomain_id": "D-05.3", "scale": "capability",
      "outcome": "CT-DM-P5", "claim": "Disposal of personal data: erasure API + backup exclude policy (Doc07 §4.5, ACT-10, STORE-03) (CONTROL-P T2).",
      "sources": ["Doc07 §4.5", "ACT-10", "STORE-03"], "observed": True },
]

assert len(EVIDENCE_ITEMS) >= 37, f"EVIDENCE_ITEMS must seed >=37 (one Coverage per active sub-domain); got {len(EVIDENCE_ITEMS)}"

# Per-sub-domain Coverage evidence index — built from EVIDENCE_ITEMS at runtime
# so the build() merge is single-source. (No drift possible.)
COVERAGE_EV_BY_SUBDOMAIN: dict[str, list[str]] = {}
for ev in EVIDENCE_ITEMS:
    if ev["scale"] != "coverage":
        continue
    COVERAGE_EV_BY_SUBDOMAIN.setdefault(ev["subdomain_id"], []).append(ev["ev_id"])


# ---------------------------------------------------------------------------
# 9. NIST Alignment (Phase D — Doc13 §7 NIST Controls Mapping)
# ---------------------------------------------------------------------------
# 35 ACTIVE sub-domains (D-01.1..D-10.3, excluding D-02.4, D-06.4, D-08.3 per
# Doc13 §0 not_addressed_subdomains).  Total control rows: 513 (verified via
# sibling parser script; excludes table-header rows).
#
# 8 control rows have malformed '?' Function column (table-renderer truncation
# in Doc13 §7): RS.CO-04 in D-04.3 + D-06.3, PR.AT-03/04 in D-08.2,
# ID.SC-04 in D-09.2, PR.IP-06/07 in D-10.2, PR.PT-01 in D-10.2.  These
# 7 unique IDs are emitted with the canonical NIST CSF 2.0 Function
# assignment per _NIST_MALFORMED_FUNCTION_OVERRIDES below.
#
# Total unique control IDs across all sub-domains: 117 (77 CSF + 38 PF + 2 AI-RMF).
# Only D-04.2 (§7.13.3) has NIST AI-RMF controls (MANAGE-2.1, MANAGE-2.3).

_NIST_MALFORMED_FUNCTION_OVERRIDES = {
    # control_id (no NIST- prefix) -> canonical NIST CSF 2.0 Function (PROTECT/IDENTIFY/RESPOND/...)
    "RS.CO-04":  "RESPOND",
    "PR.AT-03":  "PROTECT",
    "PR.AT-04":  "PROTECT",
    "ID.SC-04":  "IDENTIFY",
    "PR.IP-06":  "PROTECT",
    "PR.IP-07":  "PROTECT",
    "PR.PT-01":  "PROTECT",
}

NIST_ALIGNMENT = [
    {
        "sub_domain_id": "D-01.1",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RM-04",
                "description": "Strategic direction that describes appropriate risk response options is establis...",
                "path": "NIST_CSF/GOVERN/GV.RM-04.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-01",
                "description": "The confidentiality, integrity, and availability of data-at-rest are protected",
                "path": "NIST_CSF/PROTECT/PR.DS-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-02",
                "description": "The confidentiality, integrity, and availability of data-in-transit are protecte...",
                "path": "NIST_CSF/PROTECT/PR.DS-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-10",
                "description": "The confidentiality, integrity, and availability of data-in-use are protected",
                "path": "NIST_CSF/PROTECT/PR.DS-10.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.RM-P1",
                "description": "Risk management processes are established, managed, and agreed to by organizatio...",
                "path": "NIST_PF/GOVERN-P/GV.RM-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P2",
                "description": "Data analytic inputs and outputs are identified and evaluated for bias.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-01.2",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-01",
                "description": "The confidentiality, integrity, and availability of data-at-rest are protected",
                "path": "NIST_CSF/PROTECT/PR.DS-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-02",
                "description": "The confidentiality, integrity, and availability of data-in-transit are protecte...",
                "path": "NIST_CSF/PROTECT/PR.DS-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-10",
                "description": "The confidentiality, integrity, and availability of data-in-use are protected",
                "path": "NIST_CSF/PROTECT/PR.DS-10.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.IR-01",
                "description": "Networks and environments are protected from unauthorized logical access and usa...",
                "path": "NIST_CSF/PROTECT/PR.IR-01.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P1",
                "description": "Removable media is protected and its use restricted according to policy.",
                "path": "NIST_PF/PROTECT-P/PR.PT-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P2",
                "description": "The principle of least functionality is incorporated by configuring systems to p...",
                "path": "NIST_PF/PROTECT-P/PR.PT-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-01.3",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OV-01",
                "description": "Cybersecurity risk management strategy outcomes are reviewed to inform and adjus...",
                "path": "NIST_CSF/GOVERN/GV.OV-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RM-04",
                "description": "Strategic direction that describes appropriate risk response options is establis...",
                "path": "NIST_CSF/GOVERN/GV.RM-04.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-03",
                "description": "Users, services, and hardware are authenticated",
                "path": "NIST_CSF/PROTECT/PR.AA-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-04",
                "description": "Identity assertions are protected, conveyed, and verified",
                "path": "NIST_CSF/PROTECT/PR.AA-04.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-05",
                "description": "Access permissions, entitlements, and authorizations are defined in a policy, ma...",
                "path": "NIST_CSF/PROTECT/PR.AA-05.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-01",
                "description": "The confidentiality, integrity, and availability of data-at-rest are protected",
                "path": "NIST_CSF/PROTECT/PR.DS-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.IR-03",
                "description": "Mechanisms are implemented to achieve resilience requirements in normal and adve...",
                "path": "NIST_CSF/PROTECT/PR.IR-03.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P1",
                "description": "Privacy risk is re-evaluated on an ongoing basis and as key factors, including t...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P2",
                "description": "Privacy values, policies, and training are reviewed and any updates are communic...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.RM-P1",
                "description": "Risk management processes are established, managed, and agreed to by organizatio...",
                "path": "NIST_PF/GOVERN-P/GV.RM-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P2",
                "description": "Data analytic inputs and outputs are identified and evaluated for bias.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P1",
                "description": "Identities and credentials are issued, managed, verified, revoked, and audited f...",
                "path": "NIST_PF/PROTECT-P/PR.AC-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P3",
                "description": "Remote access is managed.",
                "path": "NIST_PF/PROTECT-P/PR.AC-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P6",
                "description": "Individuals and devices are proofed and bound to credentials, and authenticated ...",
                "path": "NIST_PF/PROTECT-P/PR.AC-P6.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P1",
                "description": "Removable media is protected and its use restricted according to policy.",
                "path": "NIST_PF/PROTECT-P/PR.PT-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P2",
                "description": "The principle of least functionality is incorporated by configuring systems to p...",
                "path": "NIST_PF/PROTECT-P/PR.PT-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-01.4",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-01",
                "description": "The confidentiality, integrity, and availability of data-at-rest are protected",
                "path": "NIST_CSF/PROTECT/PR.DS-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-02",
                "description": "The confidentiality, integrity, and availability of data-in-transit are protecte...",
                "path": "NIST_CSF/PROTECT/PR.DS-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-10",
                "description": "The confidentiality, integrity, and availability of data-in-use are protected",
                "path": "NIST_CSF/PROTECT/PR.DS-10.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-11",
                "description": "Backups of data are created, protected, maintained, and tested",
                "path": "NIST_CSF/PROTECT/PR.DS-11.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.IR-03",
                "description": "Mechanisms are implemented to achieve resilience requirements in normal and adve...",
                "path": "NIST_CSF/PROTECT/PR.IR-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.IR-04",
                "description": "Adequate resource capacity to ensure availability is maintained",
                "path": "NIST_CSF/PROTECT/PR.IR-04.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-04",
                "description": "Log records are generated and made available for continuous monitoring",
                "path": "NIST_CSF/PROTECT/PR.PS-04.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P1",
                "description": "Removable media is protected and its use restricted according to policy.",
                "path": "NIST_PF/PROTECT-P/PR.PT-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P2",
                "description": "The principle of least functionality is incorporated by configuring systems to p...",
                "path": "NIST_PF/PROTECT-P/PR.PT-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-02.1",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OV-02",
                "description": "The cybersecurity risk management strategy is reviewed and adjusted to ensure co...",
                "path": "NIST_CSF/GOVERN/GV.OV-02.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RM-01",
                "description": "Risk management objectives are established and agreed to by organizational stake...",
                "path": "NIST_CSF/GOVERN/GV.RM-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RM-06",
                "description": "A standardized method for calculating, documenting, categorizing, and prioritizi...",
                "path": "NIST_CSF/GOVERN/GV.RM-06.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-04",
                "description": "Suppliers are known and prioritized by criticality",
                "path": "NIST_CSF/GOVERN/GV.SC-04.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-02",
                "description": "Inventories of software, services, and systems managed by the organization are m...",
                "path": "NIST_CSF/IDENTIFY/ID.AM-02.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.IM-02",
                "description": "Improvements are identified from security tests and exercises, including those d...",
                "path": "NIST_CSF/IDENTIFY/ID.IM-02.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.IM-04",
                "description": "Incident response plans and other cybersecurity plans that affect operations are...",
                "path": "NIST_CSF/IDENTIFY/ID.IM-04.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-01",
                "description": "Vulnerabilities in assets are identified, validated, and recorded",
                "path": "NIST_CSF/IDENTIFY/ID.RA-01.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-03",
                "description": "Internal and external threats to the organization are identified and recorded",
                "path": "NIST_CSF/IDENTIFY/ID.RA-03.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-04",
                "description": "Potential impacts and likelihoods of threats exploiting vulnerabilities are iden...",
                "path": "NIST_CSF/IDENTIFY/ID.RA-04.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-05",
                "description": "Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere...",
                "path": "NIST_CSF/IDENTIFY/ID.RA-05.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-06",
                "description": "Risk responses are chosen, prioritized, planned, tracked, and communicated",
                "path": "NIST_CSF/IDENTIFY/ID.RA-06.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-02",
                "description": "Software is maintained, replaced, and removed commensurate with risk",
                "path": "NIST_CSF/PROTECT/PR.PS-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-06",
                "description": "Secure software development practices are integrated, and their performance is m...",
                "path": "NIST_CSF/PROTECT/PR.PS-06.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.MA-03",
                "description": "Incidents are categorized and prioritized",
                "path": "NIST_CSF/RESPOND/RS.MA-03.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.MI-01",
                "description": "Incidents are contained",
                "path": "NIST_CSF/RESPOND/RS.MI-01.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P4",
                "description": "System or device configurations permit selective collection or disclosure of dat...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P4.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P1",
                "description": "Privacy risk is re-evaluated on an ongoing basis and as key factors, including t...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P2",
                "description": "Privacy values, policies, and training are reviewed and any updates are communic...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.RM-P1",
                "description": "Risk management processes are established, managed, and agreed to by organizatio...",
                "path": "NIST_PF/GOVERN-P/GV.RM-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P1",
                "description": "Data processing ecosystem risk management policies, processes, and procedures ar...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P2",
                "description": "Data processing ecosystem parties (e.g., service providers, customers, partners,...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.IM-P1",
                "description": "Systems/products/services that process data are inventoried.",
                "path": "NIST_PF/IDENTIFY-P/ID.IM-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.IM-P2",
                "description": "Owners or operators (e.g., the organization or third parties such as service pro...",
                "path": "NIST_PF/IDENTIFY-P/ID.IM-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P2",
                "description": "Data analytic inputs and outputs are identified and evaluated for bias.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.MA-P1",
                "description": "Maintenance and repair of organizational assets are performed and logged, with a...",
                "path": "NIST_PF/PROTECT-P/PR.MA-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-02.2",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OV-02",
                "description": "The cybersecurity risk management strategy is reviewed and adjusted to ensure co...",
                "path": "NIST_CSF/GOVERN/GV.OV-02.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-01",
                "description": "Vulnerabilities in assets are identified, validated, and recorded",
                "path": "NIST_CSF/IDENTIFY/ID.RA-01.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-06",
                "description": "Risk responses are chosen, prioritized, planned, tracked, and communicated",
                "path": "NIST_CSF/IDENTIFY/ID.RA-06.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.IR-01",
                "description": "Networks and environments are protected from unauthorized logical access and usa...",
                "path": "NIST_CSF/PROTECT/PR.IR-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.IR-03",
                "description": "Mechanisms are implemented to achieve resilience requirements in normal and adve...",
                "path": "NIST_CSF/PROTECT/PR.IR-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-01",
                "description": "Configuration management practices are established and applied",
                "path": "NIST_CSF/PROTECT/PR.PS-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-02",
                "description": "Software is maintained, replaced, and removed commensurate with risk",
                "path": "NIST_CSF/PROTECT/PR.PS-02.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P1",
                "description": "Privacy risk is re-evaluated on an ongoing basis and as key factors, including t...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P2",
                "description": "Privacy values, policies, and training are reviewed and any updates are communic...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P1",
                "description": "Removable media is protected and its use restricted according to policy.",
                "path": "NIST_PF/PROTECT-P/PR.PT-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P2",
                "description": "The principle of least functionality is incorporated by configuring systems to p...",
                "path": "NIST_PF/PROTECT-P/PR.PT-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-02.3",
        "applicable_regulations": [
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.PO-01",
                "description": "Policy for managing cybersecurity risks is established based on organizational c...",
                "path": "NIST_CSF/GOVERN/GV.PO-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-04",
                "description": "Suppliers are known and prioritized by criticality",
                "path": "NIST_CSF/GOVERN/GV.SC-04.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-01",
                "description": "Vulnerabilities in assets are identified, validated, and recorded",
                "path": "NIST_CSF/IDENTIFY/ID.RA-01.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.CO-03",
                "description": "Information is shared with designated internal and external stakeholders",
                "path": "NIST_CSF/RESPOND/RS.CO-03.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P4",
                "description": "System or device configurations permit selective collection or disclosure of dat...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P4.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.PO-P1",
                "description": "Policies, processes, and procedures for authorizing data processing (e.g., organ...",
                "path": "NIST_PF/CONTROL-P/CT.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.AT-P2",
                "description": "Senior executives understand their roles and responsibilities.",
                "path": "NIST_PF/GOVERN-P/GV.AT-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P3",
                "description": "Roles and responsibilities for the workforce are established with respect to pri...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P3.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P4",
                "description": "Privacy roles and responsibilities are coordinated and aligned with third-party ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P4.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-03.1",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.CM-09",
                "description": "Computing hardware and software, runtime environments, and their data are monito...",
                "path": "NIST_CSF/DETECT/DE.CM-09.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-01",
                "description": "Inventories of hardware managed by the organization are maintained",
                "path": "NIST_CSF/IDENTIFY/ID.AM-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-01",
                "description": "Identities and credentials for authorized users, services, and hardware are mana...",
                "path": "NIST_CSF/PROTECT/PR.AA-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-02",
                "description": "Identities are proofed and bound to credentials based on the context of interact...",
                "path": "NIST_CSF/PROTECT/PR.AA-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-03",
                "description": "Users, services, and hardware are authenticated",
                "path": "NIST_CSF/PROTECT/PR.AA-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-04",
                "description": "Identity assertions are protected, conveyed, and verified",
                "path": "NIST_CSF/PROTECT/PR.AA-04.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-05",
                "description": "Access permissions, entitlements, and authorizations are defined in a policy, ma...",
                "path": "NIST_CSF/PROTECT/PR.AA-05.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-06",
                "description": "Physical access to assets is managed, monitored, and enforced commensurate with ...",
                "path": "NIST_CSF/PROTECT/PR.AA-06.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AT-02",
                "description": "Individuals in specialized roles are provided with awareness and training so tha...",
                "path": "NIST_CSF/PROTECT/PR.AT-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P1",
                "description": "Mechanisms (e.g., notices, internal or public reports) for communicating data pr...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P1.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.PO-P1",
                "description": "Transparency policies, processes, and procedures for communicating data processi...",
                "path": "NIST_PF/COMMUNICATE-P/CM.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.AT-P1",
                "description": "The workforce is informed and trained on its roles and responsibilities.",
                "path": "NIST_PF/GOVERN-P/GV.AT-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P1",
                "description": "Data processing ecosystem risk management policies, processes, and procedures ar...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P2",
                "description": "Data processing ecosystem parties (e.g., service providers, customers, partners,...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P1",
                "description": "Identities and credentials are issued, managed, verified, revoked, and audited f...",
                "path": "NIST_PF/PROTECT-P/PR.AC-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P3",
                "description": "Remote access is managed.",
                "path": "NIST_PF/PROTECT-P/PR.AC-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P6",
                "description": "Individuals and devices are proofed and bound to credentials, and authenticated ...",
                "path": "NIST_PF/PROTECT-P/PR.AC-P6.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-03.2",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.CM-09",
                "description": "Computing hardware and software, runtime environments, and their data are monito...",
                "path": "NIST_CSF/DETECT/DE.CM-09.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-01",
                "description": "Inventories of hardware managed by the organization are maintained",
                "path": "NIST_CSF/IDENTIFY/ID.AM-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-01",
                "description": "Identities and credentials for authorized users, services, and hardware are mana...",
                "path": "NIST_CSF/PROTECT/PR.AA-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-03",
                "description": "Users, services, and hardware are authenticated",
                "path": "NIST_CSF/PROTECT/PR.AA-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-04",
                "description": "Identity assertions are protected, conveyed, and verified",
                "path": "NIST_CSF/PROTECT/PR.AA-04.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-05",
                "description": "Access permissions, entitlements, and authorizations are defined in a policy, ma...",
                "path": "NIST_CSF/PROTECT/PR.AA-05.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-06",
                "description": "Physical access to assets is managed, monitored, and enforced commensurate with ...",
                "path": "NIST_CSF/PROTECT/PR.AA-06.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AT-02",
                "description": "Individuals in specialized roles are provided with awareness and training so tha...",
                "path": "NIST_CSF/PROTECT/PR.AT-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-02",
                "description": "The confidentiality, integrity, and availability of data-in-transit are protecte...",
                "path": "NIST_CSF/PROTECT/PR.DS-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.IR-03",
                "description": "Mechanisms are implemented to achieve resilience requirements in normal and adve...",
                "path": "NIST_CSF/PROTECT/PR.IR-03.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P1",
                "description": "Mechanisms (e.g., notices, internal or public reports) for communicating data pr...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P1.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.PO-P1",
                "description": "Transparency policies, processes, and procedures for communicating data processi...",
                "path": "NIST_PF/COMMUNICATE-P/CM.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.AT-P1",
                "description": "The workforce is informed and trained on its roles and responsibilities.",
                "path": "NIST_PF/GOVERN-P/GV.AT-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P1",
                "description": "Data processing ecosystem risk management policies, processes, and procedures ar...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P2",
                "description": "Data processing ecosystem parties (e.g., service providers, customers, partners,...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P1",
                "description": "Identities and credentials are issued, managed, verified, revoked, and audited f...",
                "path": "NIST_PF/PROTECT-P/PR.AC-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P3",
                "description": "Remote access is managed.",
                "path": "NIST_PF/PROTECT-P/PR.AC-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P6",
                "description": "Individuals and devices are proofed and bound to credentials, and authenticated ...",
                "path": "NIST_PF/PROTECT-P/PR.AC-P6.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P1",
                "description": "Removable media is protected and its use restricted according to policy.",
                "path": "NIST_PF/PROTECT-P/PR.PT-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P2",
                "description": "The principle of least functionality is incorporated by configuring systems to p...",
                "path": "NIST_PF/PROTECT-P/PR.PT-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-03.3",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.CM-09",
                "description": "Computing hardware and software, runtime environments, and their data are monito...",
                "path": "NIST_CSF/DETECT/DE.CM-09.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-01",
                "description": "Inventories of hardware managed by the organization are maintained",
                "path": "NIST_CSF/IDENTIFY/ID.AM-01.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-02",
                "description": "Inventories of software, services, and systems managed by the organization are m...",
                "path": "NIST_CSF/IDENTIFY/ID.AM-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-01",
                "description": "Identities and credentials for authorized users, services, and hardware are mana...",
                "path": "NIST_CSF/PROTECT/PR.AA-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-03",
                "description": "Users, services, and hardware are authenticated",
                "path": "NIST_CSF/PROTECT/PR.AA-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-04",
                "description": "Identity assertions are protected, conveyed, and verified",
                "path": "NIST_CSF/PROTECT/PR.AA-04.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-05",
                "description": "Access permissions, entitlements, and authorizations are defined in a policy, ma...",
                "path": "NIST_CSF/PROTECT/PR.AA-05.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AA-06",
                "description": "Physical access to assets is managed, monitored, and enforced commensurate with ...",
                "path": "NIST_CSF/PROTECT/PR.AA-06.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AT-02",
                "description": "Individuals in specialized roles are provided with awareness and training so tha...",
                "path": "NIST_CSF/PROTECT/PR.AT-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-04",
                "description": "Log records are generated and made available for continuous monitoring",
                "path": "NIST_CSF/PROTECT/PR.PS-04.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P1",
                "description": "Mechanisms (e.g., notices, internal or public reports) for communicating data pr...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P1.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.PO-P1",
                "description": "Transparency policies, processes, and procedures for communicating data processi...",
                "path": "NIST_PF/COMMUNICATE-P/CM.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.AT-P1",
                "description": "The workforce is informed and trained on its roles and responsibilities.",
                "path": "NIST_PF/GOVERN-P/GV.AT-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P1",
                "description": "Data processing ecosystem risk management policies, processes, and procedures ar...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P2",
                "description": "Data processing ecosystem parties (e.g., service providers, customers, partners,...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P1",
                "description": "Identities and credentials are issued, managed, verified, revoked, and audited f...",
                "path": "NIST_PF/PROTECT-P/PR.AC-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P3",
                "description": "Remote access is managed.",
                "path": "NIST_PF/PROTECT-P/PR.AC-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.AC-P6",
                "description": "Individuals and devices are proofed and bound to credentials, and authenticated ...",
                "path": "NIST_PF/PROTECT-P/PR.AC-P6.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-03.4",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.PO-01",
                "description": "Policy for managing cybersecurity risks is established based on organizational c...",
                "path": "NIST_CSF/GOVERN/GV.PO-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-03",
                "description": "Cybersecurity supply chain risk management is integrated into cybersecurity and ...",
                "path": "NIST_CSF/GOVERN/GV.SC-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-01",
                "description": "Configuration management practices are established and applied",
                "path": "NIST_CSF/PROTECT/PR.PS-01.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P4",
                "description": "System or device configurations permit selective collection or disclosure of dat...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P4.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P3",
                "description": "Roles and responsibilities for the workforce are established with respect to pri...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P3.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P4",
                "description": "Privacy roles and responsibilities are coordinated and aligned with third-party ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P4.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-04.1",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.AE-02",
                "description": "Potentially adverse events are analyzed to better understand associated activiti...",
                "path": "NIST_CSF/DETECT/DE.AE-02.json"
            },
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.CM-01",
                "description": "Networks and network services are monitored to find potentially adverse events",
                "path": "NIST_CSF/DETECT/DE.CM-01.json"
            },
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.CM-09",
                "description": "Computing hardware and software, runtime environments, and their data are monito...",
                "path": "NIST_CSF/DETECT/DE.CM-09.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-04",
                "description": "Log records are generated and made available for continuous monitoring",
                "path": "NIST_CSF/PROTECT/PR.PS-04.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.MA-01",
                "description": "The incident response plan is executed in coordination with relevant third parti...",
                "path": "NIST_CSF/RESPOND/RS.MA-01.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.MA-02",
                "description": "Incident reports are triaged and validated",
                "path": "NIST_CSF/RESPOND/RS.MA-02.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.MA-03",
                "description": "Incidents are categorized and prioritized",
                "path": "NIST_CSF/RESPOND/RS.MA-03.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P1",
                "description": "Mechanisms (e.g., notices, internal or public reports) for communicating data pr...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P1.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P2",
                "description": "Mechanisms for obtaining feedback from individuals (e.g., surveys or focus group...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P2.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.PO-P1",
                "description": "Transparency policies, processes, and procedures for communicating data processi...",
                "path": "NIST_PF/COMMUNICATE-P/CM.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DM-P1",
                "description": "Data elements can be accessed for review",
                "path": "NIST_PF/CONTROL-P/CT.DM-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-04.2",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.CM-09",
                "description": "Computing hardware and software, runtime environments, and their data are monito...",
                "path": "NIST_CSF/DETECT/DE.CM-09.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-01",
                "description": "The confidentiality, integrity, and availability of data-at-rest are protected",
                "path": "NIST_CSF/PROTECT/PR.DS-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-11",
                "description": "Backups of data are created, protected, maintained, and tested",
                "path": "NIST_CSF/PROTECT/PR.DS-11.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.IR-03",
                "description": "Mechanisms are implemented to achieve resilience requirements in normal and adve...",
                "path": "NIST_CSF/PROTECT/PR.IR-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.IR-04",
                "description": "Adequate resource capacity to ensure availability is maintained",
                "path": "NIST_CSF/PROTECT/PR.IR-04.json"
            },
            {
                "framework": "CSF",
                "function": "RECOVER",
                "control_id": "RC.RP-01",
                "description": "The recovery portion of the incident response plan is executed once initiated fr...",
                "path": "NIST_CSF/RECOVER/RC.RP-01.json"
            },
            {
                "framework": "CSF",
                "function": "RECOVER",
                "control_id": "RC.RP-03",
                "description": "The integrity of backups and other restoration assets is verified before using t...",
                "path": "NIST_CSF/RECOVER/RC.RP-03.json"
            },
            {
                "framework": "CSF",
                "function": "RECOVER",
                "control_id": "RC.RP-04",
                "description": "Critical mission functions and cybersecurity risk management are considered to e...",
                "path": "NIST_CSF/RECOVER/RC.RP-04.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.MI-01",
                "description": "Incidents are contained",
                "path": "NIST_CSF/RESPOND/RS.MI-01.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.MI-02",
                "description": "Incidents are eradicated",
                "path": "NIST_CSF/RESPOND/RS.MI-02.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P1",
                "description": "Mechanisms (e.g., notices, internal or public reports) for communicating data pr...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P1.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.PO-P1",
                "description": "Transparency policies, processes, and procedures for communicating data processi...",
                "path": "NIST_PF/COMMUNICATE-P/CM.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P3",
                "description": "Data are processed to limit the formulation of inferences about individuals’ beh...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.MA-P1",
                "description": "Maintenance and repair of organizational assets are performed and logged, with a...",
                "path": "NIST_PF/PROTECT-P/PR.MA-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P4",
                "description": "Policy and regulations regarding the physical operating environment for organiza...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P4.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P1",
                "description": "Removable media is protected and its use restricted according to policy.",
                "path": "NIST_PF/PROTECT-P/PR.PT-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P2",
                "description": "The principle of least functionality is incorporated by configuring systems to p...",
                "path": "NIST_PF/PROTECT-P/PR.PT-P2.json"
            },
            {
                "framework": "AI-RMF",
                "function": "MANAGE",
                "control_id": "MANAGE-2.1",
                "description": "Resources required to manage AI risks are taken into account, along with viable ...",
                "path": "NIST_AI_RMF/MANAGE/MANAGE-2.1.json"
            },
            {
                "framework": "AI-RMF",
                "function": "MANAGE",
                "control_id": "MANAGE-2.3",
                "description": "Procedures are followed to respond to and recover from a previously unknown risk...",
                "path": "NIST_AI_RMF/MANAGE/MANAGE-2.3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-04.3",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.AN-03",
                "description": "Analysis is performed to establish what has taken place during an incident and t...",
                "path": "NIST_CSF/RESPOND/RS.AN-03.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.AN-07",
                "description": "Incident data and metadata are collected, and their integrity and provenance are...",
                "path": "NIST_CSF/RESPOND/RS.AN-07.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.CO-02",
                "description": "Internal and external stakeholders are notified of incidents",
                "path": "NIST_CSF/RESPOND/RS.CO-02.json"
            },
            {
                "framework": "CSF",
                "function": "?",
                "control_id": "RS.CO-04",
                "description": "?",
                "path": "NIST_CSF/?/RS.CO-04.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.MA-01",
                "description": "The incident response plan is executed in coordination with relevant third parti...",
                "path": "NIST_CSF/RESPOND/RS.MA-01.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.MA-02",
                "description": "Incident reports are triaged and validated",
                "path": "NIST_CSF/RESPOND/RS.MA-02.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.MA-03",
                "description": "Incidents are categorized and prioritized",
                "path": "NIST_CSF/RESPOND/RS.MA-03.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DM-P3",
                "description": "Data elements can be accessed for alteration.",
                "path": "NIST_PF/CONTROL-P/CT.DM-P3.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.PO-P1",
                "description": "Policies, processes, and procedures for authorizing data processing (e.g., organ...",
                "path": "NIST_PF/CONTROL-P/CT.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.AT-P2",
                "description": "Senior executives understand their roles and responsibilities.",
                "path": "NIST_PF/GOVERN-P/GV.AT-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-04.4",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-11",
                "description": "Backups of data are created, protected, maintained, and tested",
                "path": "NIST_CSF/PROTECT/PR.DS-11.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.IR-03",
                "description": "Mechanisms are implemented to achieve resilience requirements in normal and adve...",
                "path": "NIST_CSF/PROTECT/PR.IR-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.IR-04",
                "description": "Adequate resource capacity to ensure availability is maintained",
                "path": "NIST_CSF/PROTECT/PR.IR-04.json"
            },
            {
                "framework": "CSF",
                "function": "RECOVER",
                "control_id": "RC.RP-01",
                "description": "The recovery portion of the incident response plan is executed once initiated fr...",
                "path": "NIST_CSF/RECOVER/RC.RP-01.json"
            },
            {
                "framework": "CSF",
                "function": "RECOVER",
                "control_id": "RC.RP-03",
                "description": "The integrity of backups and other restoration assets is verified before using t...",
                "path": "NIST_CSF/RECOVER/RC.RP-03.json"
            },
            {
                "framework": "CSF",
                "function": "RECOVER",
                "control_id": "RC.RP-04",
                "description": "Critical mission functions and cybersecurity risk management are considered to e...",
                "path": "NIST_CSF/RECOVER/RC.RP-04.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P3",
                "description": "Data are processed to limit the formulation of inferences about individuals’ beh...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P4",
                "description": "Policy and regulations regarding the physical operating environment for organiza...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P4.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P1",
                "description": "Removable media is protected and its use restricted according to policy.",
                "path": "NIST_PF/PROTECT-P/PR.PT-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PT-P2",
                "description": "The principle of least functionality is incorporated by configuring systems to p...",
                "path": "NIST_PF/PROTECT-P/PR.PT-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-05.1",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OC-03",
                "description": "Legal, regulatory, and contractual requirements regarding cybersecurity - includ...",
                "path": "NIST_CSF/GOVERN/GV.OC-03.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.PO-01",
                "description": "Policy for managing cybersecurity risks is established based on organizational c...",
                "path": "NIST_CSF/GOVERN/GV.PO-01.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-03",
                "description": "Representations of the organization's authorized network communication and inter...",
                "path": "NIST_CSF/IDENTIFY/ID.AM-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-01",
                "description": "The confidentiality, integrity, and availability of data-at-rest are protected",
                "path": "NIST_CSF/PROTECT/PR.DS-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-06",
                "description": "Secure software development practices are integrated, and their performance is m...",
                "path": "NIST_CSF/PROTECT/PR.PS-06.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P1",
                "description": "Organizational privacy values and policies (e.g., conditions on data processing ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P2",
                "description": "Processes to instill organizational privacy values within system/product/service...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P3",
                "description": "Roles and responsibilities for the workforce are established with respect to pri...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P3.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P4",
                "description": "Privacy roles and responsibilities are coordinated and aligned with third-party ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P4.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P1",
                "description": "Data processing ecosystem risk management policies, processes, and procedures ar...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P2",
                "description": "Data processing ecosystem parties (e.g., service providers, customers, partners,...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-05.2",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OC-04",
                "description": "Critical objectives, capabilities, and services that external stakeholders depen...",
                "path": "NIST_CSF/GOVERN/GV.OC-04.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OV-02",
                "description": "The cybersecurity risk management strategy is reviewed and adjusted to ensure co...",
                "path": "NIST_CSF/GOVERN/GV.OV-02.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.PO-02",
                "description": "Policy for managing cybersecurity risks is reviewed, updated, communicated, and ...",
                "path": "NIST_CSF/GOVERN/GV.PO-02.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-03",
                "description": "Representations of the organization's authorized network communication and inter...",
                "path": "NIST_CSF/IDENTIFY/ID.AM-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-02",
                "description": "Software is maintained, replaced, and removed commensurate with risk",
                "path": "NIST_CSF/PROTECT/PR.PS-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-04",
                "description": "Log records are generated and made available for continuous monitoring",
                "path": "NIST_CSF/PROTECT/PR.PS-04.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P1",
                "description": "Privacy risk is re-evaluated on an ongoing basis and as key factors, including t...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P2",
                "description": "Privacy values, policies, and training are reviewed and any updates are communic...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P1",
                "description": "Organizational privacy values and policies (e.g., conditions on data processing ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P2",
                "description": "Processes to instill organizational privacy values within system/product/service...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P3",
                "description": "Roles and responsibilities for the workforce are established with respect to pri...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P3.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P4",
                "description": "Privacy roles and responsibilities are coordinated and aligned with third-party ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P4.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P1",
                "description": "Data processing ecosystem risk management policies, processes, and procedures ar...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P2",
                "description": "Data processing ecosystem parties (e.g., service providers, customers, partners,...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-05.3",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-04",
                "description": "Suppliers are known and prioritized by criticality",
                "path": "NIST_CSF/GOVERN/GV.SC-04.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-10",
                "description": "The confidentiality, integrity, and availability of data-in-use are protected",
                "path": "NIST_CSF/PROTECT/PR.DS-10.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P4",
                "description": "System or device configurations permit selective collection or disclosure of dat...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P4.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-05.4",
        "applicable_regulations": [
            "GDPR"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-10",
                "description": "The confidentiality, integrity, and availability of data-in-use are protected",
                "path": "NIST_CSF/PROTECT/PR.DS-10.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-06.1",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OC-03",
                "description": "Legal, regulatory, and contractual requirements regarding cybersecurity - includ...",
                "path": "NIST_CSF/GOVERN/GV.OC-03.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-01",
                "description": "A cybersecurity supply chain risk management program, strategy, objectives, poli...",
                "path": "NIST_CSF/GOVERN/GV.SC-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-02",
                "description": "Cybersecurity roles and responsibilities for suppliers, customers, and partners ...",
                "path": "NIST_CSF/GOVERN/GV.SC-02.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-03",
                "description": "Cybersecurity supply chain risk management is integrated into cybersecurity and ...",
                "path": "NIST_CSF/GOVERN/GV.SC-03.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-04",
                "description": "Suppliers are known and prioritized by criticality",
                "path": "NIST_CSF/GOVERN/GV.SC-04.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-04",
                "description": "Inventories of services provided by suppliers are maintained",
                "path": "NIST_CSF/IDENTIFY/ID.AM-04.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-01",
                "description": "Vulnerabilities in assets are identified, validated, and recorded",
                "path": "NIST_CSF/IDENTIFY/ID.RA-01.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-02",
                "description": "Cyber threat intelligence is received from information sharing forums and source...",
                "path": "NIST_CSF/IDENTIFY/ID.RA-02.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P4",
                "description": "System or device configurations permit selective collection or disclosure of dat...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P4.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P1",
                "description": "Organizational privacy values and policies (e.g., conditions on data processing ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P2",
                "description": "Processes to instill organizational privacy values within system/product/service...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P1",
                "description": "Data processing ecosystem risk management policies, processes, and procedures ar...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P2",
                "description": "Data processing ecosystem parties (e.g., service providers, customers, partners,...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-06.2",
        "applicable_regulations": [
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-02",
                "description": "Cybersecurity roles and responsibilities for suppliers, customers, and partners ...",
                "path": "NIST_CSF/GOVERN/GV.SC-02.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-03",
                "description": "Cybersecurity supply chain risk management is integrated into cybersecurity and ...",
                "path": "NIST_CSF/GOVERN/GV.SC-03.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-02",
                "description": "Inventories of software, services, and systems managed by the organization are m...",
                "path": "NIST_CSF/IDENTIFY/ID.AM-02.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P4",
                "description": "System or device configurations permit selective collection or disclosure of dat...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P4.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P1",
                "description": "Data processing ecosystem risk management policies, processes, and procedures ar...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P2",
                "description": "Data processing ecosystem parties (e.g., service providers, customers, partners,...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-06.3",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.CM-06",
                "description": "External service provider activities and services are monitored to find potentia...",
                "path": "NIST_CSF/DETECT/DE.CM-06.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OC-03",
                "description": "Legal, regulatory, and contractual requirements regarding cybersecurity - includ...",
                "path": "NIST_CSF/GOVERN/GV.OC-03.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-01",
                "description": "A cybersecurity supply chain risk management program, strategy, objectives, poli...",
                "path": "NIST_CSF/GOVERN/GV.SC-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-02",
                "description": "Cybersecurity roles and responsibilities for suppliers, customers, and partners ...",
                "path": "NIST_CSF/GOVERN/GV.SC-02.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-03",
                "description": "Cybersecurity supply chain risk management is integrated into cybersecurity and ...",
                "path": "NIST_CSF/GOVERN/GV.SC-03.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-04",
                "description": "Suppliers are known and prioritized by criticality",
                "path": "NIST_CSF/GOVERN/GV.SC-04.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-04",
                "description": "Inventories of services provided by suppliers are maintained",
                "path": "NIST_CSF/IDENTIFY/ID.AM-04.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-01",
                "description": "Vulnerabilities in assets are identified, validated, and recorded",
                "path": "NIST_CSF/IDENTIFY/ID.RA-01.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-02",
                "description": "Cyber threat intelligence is received from information sharing forums and source...",
                "path": "NIST_CSF/IDENTIFY/ID.RA-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-06",
                "description": "Secure software development practices are integrated, and their performance is m...",
                "path": "NIST_CSF/PROTECT/PR.PS-06.json"
            },
            {
                "framework": "CSF",
                "function": "?",
                "control_id": "RS.CO-04",
                "description": "?",
                "path": "NIST_CSF/?/RS.CO-04.json"
            },
            {
                "framework": "CSF",
                "function": "RESPOND",
                "control_id": "RS.MI-01",
                "description": "Incidents are contained",
                "path": "NIST_CSF/RESPOND/RS.MI-01.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P1",
                "description": "Mechanisms (e.g., notices, internal or public reports) for communicating data pr...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P1.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.PO-P1",
                "description": "Transparency policies, processes, and procedures for communicating data processi...",
                "path": "NIST_PF/COMMUNICATE-P/CM.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P4",
                "description": "System or device configurations permit selective collection or disclosure of dat...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P4.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.PO-P1",
                "description": "Policies, processes, and procedures for authorizing data processing (e.g., organ...",
                "path": "NIST_PF/CONTROL-P/CT.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.AT-P2",
                "description": "Senior executives understand their roles and responsibilities.",
                "path": "NIST_PF/GOVERN-P/GV.AT-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P1",
                "description": "Organizational privacy values and policies (e.g., conditions on data processing ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P2",
                "description": "Processes to instill organizational privacy values within system/product/service...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P1",
                "description": "Data processing ecosystem risk management policies, processes, and procedures ar...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P2",
                "description": "Data processing ecosystem parties (e.g., service providers, customers, partners,...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.MA-P1",
                "description": "Maintenance and repair of organizational assets are performed and logged, with a...",
                "path": "NIST_PF/PROTECT-P/PR.MA-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-07.1",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-01",
                "description": "Vulnerabilities in assets are identified, validated, and recorded",
                "path": "NIST_CSF/IDENTIFY/ID.RA-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-01",
                "description": "Configuration management practices are established and applied",
                "path": "NIST_CSF/PROTECT/PR.PS-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-02",
                "description": "Software is maintained, replaced, and removed commensurate with risk",
                "path": "NIST_CSF/PROTECT/PR.PS-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-06",
                "description": "Secure software development practices are integrated, and their performance is m...",
                "path": "NIST_CSF/PROTECT/PR.PS-06.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-07.2",
        "applicable_regulations": [
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-01",
                "description": "Vulnerabilities in assets are identified, validated, and recorded",
                "path": "NIST_CSF/IDENTIFY/ID.RA-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-02",
                "description": "Software is maintained, replaced, and removed commensurate with risk",
                "path": "NIST_CSF/PROTECT/PR.PS-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-06",
                "description": "Secure software development practices are integrated, and their performance is m...",
                "path": "NIST_CSF/PROTECT/PR.PS-06.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-07.3",
        "applicable_regulations": [
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-01",
                "description": "Vulnerabilities in assets are identified, validated, and recorded",
                "path": "NIST_CSF/IDENTIFY/ID.RA-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-02",
                "description": "Software is maintained, replaced, and removed commensurate with risk",
                "path": "NIST_CSF/PROTECT/PR.PS-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-06",
                "description": "Secure software development practices are integrated, and their performance is m...",
                "path": "NIST_CSF/PROTECT/PR.PS-06.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-07.4",
        "applicable_regulations": [
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OV-01",
                "description": "Cybersecurity risk management strategy outcomes are reviewed to inform and adjus...",
                "path": "NIST_CSF/GOVERN/GV.OV-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OV-02",
                "description": "The cybersecurity risk management strategy is reviewed and adjusted to ensure co...",
                "path": "NIST_CSF/GOVERN/GV.OV-02.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.PO-02",
                "description": "Policy for managing cybersecurity risks is reviewed, updated, communicated, and ...",
                "path": "NIST_CSF/GOVERN/GV.PO-02.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-04",
                "description": "Suppliers are known and prioritized by criticality",
                "path": "NIST_CSF/GOVERN/GV.SC-04.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.IM-04",
                "description": "Incident response plans and other cybersecurity plans that affect operations are...",
                "path": "NIST_CSF/IDENTIFY/ID.IM-04.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-01",
                "description": "Configuration management practices are established and applied",
                "path": "NIST_CSF/PROTECT/PR.PS-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-02",
                "description": "Software is maintained, replaced, and removed commensurate with risk",
                "path": "NIST_CSF/PROTECT/PR.PS-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-06",
                "description": "Secure software development practices are integrated, and their performance is m...",
                "path": "NIST_CSF/PROTECT/PR.PS-06.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P4",
                "description": "System or device configurations permit selective collection or disclosure of dat...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P4.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P1",
                "description": "Privacy risk is re-evaluated on an ongoing basis and as key factors, including t...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P2",
                "description": "Privacy values, policies, and training are reviewed and any updates are communic...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P3",
                "description": "Roles and responsibilities for the workforce are established with respect to pri...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P3.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P4",
                "description": "Privacy roles and responsibilities are coordinated and aligned with third-party ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P4.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.IM-P1",
                "description": "Systems/products/services that process data are inventoried.",
                "path": "NIST_PF/IDENTIFY-P/ID.IM-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.IM-P2",
                "description": "Owners or operators (e.g., the organization or third parties such as service pro...",
                "path": "NIST_PF/IDENTIFY-P/ID.IM-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-08.1",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AT-01",
                "description": "Personnel are provided with awareness and training so that they possess the know...",
                "path": "NIST_CSF/PROTECT/PR.AT-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AT-02",
                "description": "Individuals in specialized roles are provided with awareness and training so tha...",
                "path": "NIST_CSF/PROTECT/PR.AT-02.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-01",
                "description": "Configuration management practices are established and applied",
                "path": "NIST_CSF/PROTECT/PR.PS-01.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.AT-P1",
                "description": "The workforce is informed and trained on its roles and responsibilities.",
                "path": "NIST_PF/GOVERN-P/GV.AT-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-08.2",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RR-01",
                "description": "Organizational leadership is responsible and accountable for cybersecurity risk ...",
                "path": "NIST_CSF/GOVERN/GV.RR-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RR-02",
                "description": "Roles, responsibilities, and authorities related to cybersecurity risk managemen...",
                "path": "NIST_CSF/GOVERN/GV.RR-02.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RR-04",
                "description": "Cybersecurity is included in human resources practices",
                "path": "NIST_CSF/GOVERN/GV.RR-04.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-03",
                "description": "Cybersecurity supply chain risk management is integrated into cybersecurity and ...",
                "path": "NIST_CSF/GOVERN/GV.SC-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AT-01",
                "description": "Personnel are provided with awareness and training so that they possess the know...",
                "path": "NIST_CSF/PROTECT/PR.AT-01.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.AT-02",
                "description": "Individuals in specialized roles are provided with awareness and training so tha...",
                "path": "NIST_CSF/PROTECT/PR.AT-02.json"
            },
            {
                "framework": "CSF",
                "function": "?",
                "control_id": "PR.AT-03",
                "description": "?",
                "path": "NIST_CSF/?/PR.AT-03.json"
            },
            {
                "framework": "CSF",
                "function": "?",
                "control_id": "PR.AT-04",
                "description": "?",
                "path": "NIST_CSF/?/PR.AT-04.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P4",
                "description": "System or device configurations permit selective collection or disclosure of dat...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P4.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.AT-P1",
                "description": "The workforce is informed and trained on its roles and responsibilities.",
                "path": "NIST_PF/GOVERN-P/GV.AT-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P5",
                "description": "Legal, regulatory, and contractual requirements regarding privacy are understood...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P5.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-09.1",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OC-03",
                "description": "Legal, regulatory, and contractual requirements regarding cybersecurity - includ...",
                "path": "NIST_CSF/GOVERN/GV.OC-03.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OC-04",
                "description": "Critical objectives, capabilities, and services that external stakeholders depen...",
                "path": "NIST_CSF/GOVERN/GV.OC-04.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OV-01",
                "description": "Cybersecurity risk management strategy outcomes are reviewed to inform and adjus...",
                "path": "NIST_CSF/GOVERN/GV.OV-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OV-03",
                "description": "Organizational cybersecurity risk management performance is evaluated and review...",
                "path": "NIST_CSF/GOVERN/GV.OV-03.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.PO-01",
                "description": "Policy for managing cybersecurity risks is established based on organizational c...",
                "path": "NIST_CSF/GOVERN/GV.PO-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.PO-02",
                "description": "Policy for managing cybersecurity risks is reviewed, updated, communicated, and ...",
                "path": "NIST_CSF/GOVERN/GV.PO-02.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RM-01",
                "description": "Risk management objectives are established and agreed to by organizational stake...",
                "path": "NIST_CSF/GOVERN/GV.RM-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RM-04",
                "description": "Strategic direction that describes appropriate risk response options is establis...",
                "path": "NIST_CSF/GOVERN/GV.RM-04.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RM-05",
                "description": "Lines of communication across the organization are established for cybersecurity...",
                "path": "NIST_CSF/GOVERN/GV.RM-05.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RR-01",
                "description": "Organizational leadership is responsible and accountable for cybersecurity risk ...",
                "path": "NIST_CSF/GOVERN/GV.RR-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RR-02",
                "description": "Roles, responsibilities, and authorities related to cybersecurity risk managemen...",
                "path": "NIST_CSF/GOVERN/GV.RR-02.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RR-03",
                "description": "Adequate resources are allocated commensurate with the cybersecurity risk strate...",
                "path": "NIST_CSF/GOVERN/GV.RR-03.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-01",
                "description": "A cybersecurity supply chain risk management program, strategy, objectives, poli...",
                "path": "NIST_CSF/GOVERN/GV.SC-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.SC-04",
                "description": "Suppliers are known and prioritized by criticality",
                "path": "NIST_CSF/GOVERN/GV.SC-04.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P4",
                "description": "System or device configurations permit selective collection or disclosure of dat...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P4.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P1",
                "description": "Privacy risk is re-evaluated on an ongoing basis and as key factors, including t...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P2",
                "description": "Privacy values, policies, and training are reviewed and any updates are communic...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P1",
                "description": "Organizational privacy values and policies (e.g., conditions on data processing ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P2",
                "description": "Processes to instill organizational privacy values within system/product/service...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P3",
                "description": "Roles and responsibilities for the workforce are established with respect to pri...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P3.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P4",
                "description": "Privacy roles and responsibilities are coordinated and aligned with third-party ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P4.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P5",
                "description": "Legal, regulatory, and contractual requirements regarding privacy are understood...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P5.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.RM-P1",
                "description": "Risk management processes are established, managed, and agreed to by organizatio...",
                "path": "NIST_PF/GOVERN-P/GV.RM-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P2",
                "description": "Data analytic inputs and outputs are identified and evaluated for bias.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-09.2",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OV-01",
                "description": "Cybersecurity risk management strategy outcomes are reviewed to inform and adjus...",
                "path": "NIST_CSF/GOVERN/GV.OV-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RM-04",
                "description": "Strategic direction that describes appropriate risk response options is establis...",
                "path": "NIST_CSF/GOVERN/GV.RM-04.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.RR-02",
                "description": "Roles, responsibilities, and authorities related to cybersecurity risk managemen...",
                "path": "NIST_CSF/GOVERN/GV.RR-02.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-04",
                "description": "Potential impacts and likelihoods of threats exploiting vulnerabilities are iden...",
                "path": "NIST_CSF/IDENTIFY/ID.RA-04.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-05",
                "description": "Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere...",
                "path": "NIST_CSF/IDENTIFY/ID.RA-05.json"
            },
            {
                "framework": "CSF",
                "function": "?",
                "control_id": "ID.SC-04",
                "description": "?",
                "path": "NIST_CSF/?/ID.SC-04.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P1",
                "description": "Data are processed to limit observability and linkability (e.g., data actions ta...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P1.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P2",
                "description": "Data are processed to limit the identification of individuals (e.g., de-identifi...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P1",
                "description": "Privacy risk is re-evaluated on an ongoing basis and as key factors, including t...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P2",
                "description": "Privacy values, policies, and training are reviewed and any updates are communic...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P5",
                "description": "Legal, regulatory, and contractual requirements regarding privacy are understood...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P5.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.RM-P1",
                "description": "Risk management processes are established, managed, and agreed to by organizatio...",
                "path": "NIST_PF/GOVERN-P/GV.RM-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P2",
                "description": "Data analytic inputs and outputs are identified and evaluated for bias.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-09.3",
        "applicable_regulations": [
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-01",
                "description": "Inventories of hardware managed by the organization are maintained",
                "path": "NIST_CSF/IDENTIFY/ID.AM-01.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-02",
                "description": "Inventories of software, services, and systems managed by the organization are m...",
                "path": "NIST_CSF/IDENTIFY/ID.AM-02.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-05",
                "description": "Assets are prioritized based on classification, criticality, resources, and impa...",
                "path": "NIST_CSF/IDENTIFY/ID.AM-05.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-01",
                "description": "Configuration management practices are established and applied",
                "path": "NIST_CSF/PROTECT/PR.PS-01.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P1",
                "description": "Data processing ecosystem risk management policies, processes, and procedures ar...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P2",
                "description": "Data processing ecosystem parties (e.g., service providers, customers, partners,...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-09.4",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.PO-01",
                "description": "Policy for managing cybersecurity risks is established based on organizational c...",
                "path": "NIST_CSF/GOVERN/GV.PO-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.PO-02",
                "description": "Policy for managing cybersecurity risks is reviewed, updated, communicated, and ...",
                "path": "NIST_CSF/GOVERN/GV.PO-02.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.AM-08",
                "description": "Systems, hardware, software, services, and data are managed throughout their lif...",
                "path": "NIST_CSF/IDENTIFY/ID.AM-08.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-05",
                "description": "Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere...",
                "path": "NIST_CSF/IDENTIFY/ID.RA-05.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P3",
                "description": "Roles and responsibilities for the workforce are established with respect to pri...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P3.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P4",
                "description": "Privacy roles and responsibilities are coordinated and aligned with third-party ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P4.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P1",
                "description": "Data processing ecosystem risk management policies, processes, and procedures ar...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.DE-P2",
                "description": "Data processing ecosystem parties (e.g., service providers, customers, partners,...",
                "path": "NIST_PF/IDENTIFY-P/ID.DE-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-10.1",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.AE-02",
                "description": "Potentially adverse events are analyzed to better understand associated activiti...",
                "path": "NIST_CSF/DETECT/DE.AE-02.json"
            },
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.CM-01",
                "description": "Networks and network services are monitored to find potentially adverse events",
                "path": "NIST_CSF/DETECT/DE.CM-01.json"
            },
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.CM-09",
                "description": "Computing hardware and software, runtime environments, and their data are monito...",
                "path": "NIST_CSF/DETECT/DE.CM-09.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OV-03",
                "description": "Organizational cybersecurity risk management performance is evaluated and review...",
                "path": "NIST_CSF/GOVERN/GV.OV-03.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.IM-04",
                "description": "Incident response plans and other cybersecurity plans that affect operations are...",
                "path": "NIST_CSF/IDENTIFY/ID.IM-04.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-01",
                "description": "Vulnerabilities in assets are identified, validated, and recorded",
                "path": "NIST_CSF/IDENTIFY/ID.RA-01.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-03",
                "description": "Internal and external threats to the organization are identified and recorded",
                "path": "NIST_CSF/IDENTIFY/ID.RA-03.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-04",
                "description": "Log records are generated and made available for continuous monitoring",
                "path": "NIST_CSF/PROTECT/PR.PS-04.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P1",
                "description": "Mechanisms (e.g., notices, internal or public reports) for communicating data pr...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P1.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P2",
                "description": "Mechanisms for obtaining feedback from individuals (e.g., surveys or focus group...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P2.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.PO-P1",
                "description": "Transparency policies, processes, and procedures for communicating data processi...",
                "path": "NIST_PF/COMMUNICATE-P/CM.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DM-P1",
                "description": "Data elements can be accessed for review",
                "path": "NIST_PF/CONTROL-P/CT.DM-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P1",
                "description": "Privacy risk is re-evaluated on an ongoing basis and as key factors, including t...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P2",
                "description": "Privacy values, policies, and training are reviewed and any updates are communic...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.IM-P1",
                "description": "Systems/products/services that process data are inventoried.",
                "path": "NIST_PF/IDENTIFY-P/ID.IM-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.IM-P2",
                "description": "Owners or operators (e.g., the organization or third parties such as service pro...",
                "path": "NIST_PF/IDENTIFY-P/ID.IM-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-10.2",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.AE-03",
                "description": "Information is correlated from multiple sources",
                "path": "NIST_CSF/DETECT/DE.AE-03.json"
            },
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.CM-01",
                "description": "Networks and network services are monitored to find potentially adverse events",
                "path": "NIST_CSF/DETECT/DE.CM-01.json"
            },
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.CM-09",
                "description": "Computing hardware and software, runtime environments, and their data are monito...",
                "path": "NIST_CSF/DETECT/DE.CM-09.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OC-03",
                "description": "Legal, regulatory, and contractual requirements regarding cybersecurity - includ...",
                "path": "NIST_CSF/GOVERN/GV.OC-03.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.PO-01",
                "description": "Policy for managing cybersecurity risks is established based on organizational c...",
                "path": "NIST_CSF/GOVERN/GV.PO-01.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.PO-02",
                "description": "Policy for managing cybersecurity risks is reviewed, updated, communicated, and ...",
                "path": "NIST_CSF/GOVERN/GV.PO-02.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-04",
                "description": "Potential impacts and likelihoods of threats exploiting vulnerabilities are iden...",
                "path": "NIST_CSF/IDENTIFY/ID.RA-04.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-11",
                "description": "Backups of data are created, protected, maintained, and tested",
                "path": "NIST_CSF/PROTECT/PR.DS-11.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.DS-12",
                "description": "Cryptographic protections applied to data are commensurate with data classificat...",
                "path": "NIST_CSF/PROTECT/PR.DS-12.json"
            },
            {
                "framework": "CSF",
                "function": "?",
                "control_id": "PR.IP-06",
                "description": "?",
                "path": "NIST_CSF/?/PR.IP-06.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-04",
                "description": "Log records are generated and made available for continuous monitoring",
                "path": "NIST_CSF/PROTECT/PR.PS-04.json"
            },
            {
                "framework": "CSF",
                "function": "?",
                "control_id": "PR.PT-01",
                "description": "?",
                "path": "NIST_CSF/?/PR.PT-01.json"
            },
            {
                "framework": "CSF",
                "function": "RECOVER",
                "control_id": "RC.RP-03",
                "description": "The integrity of backups and other restoration assets is verified before using t...",
                "path": "NIST_CSF/RECOVER/RC.RP-03.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P1",
                "description": "Mechanisms (e.g., notices, internal or public reports) for communicating data pr...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P1.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P2",
                "description": "Mechanisms for obtaining feedback from individuals (e.g., surveys or focus group...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P2.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.PO-P1",
                "description": "Transparency policies, processes, and procedures for communicating data processi...",
                "path": "NIST_PF/COMMUNICATE-P/CM.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DM-P1",
                "description": "Data elements can be accessed for review",
                "path": "NIST_PF/CONTROL-P/CT.DM-P1.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DP-P3",
                "description": "Data are processed to limit the formulation of inferences about individuals’ beh...",
                "path": "NIST_PF/CONTROL-P/CT.DP-P3.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P1",
                "description": "Organizational privacy values and policies (e.g., conditions on data processing ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P2",
                "description": "Processes to instill organizational privacy values within system/product/service...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P2.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P3",
                "description": "Roles and responsibilities for the workforce are established with respect to pri...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P3.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.PO-P4",
                "description": "Privacy roles and responsibilities are coordinated and aligned with third-party ...",
                "path": "NIST_PF/GOVERN-P/GV.PO-P4.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P1",
                "description": "Data-at-rest are protected",
                "path": "NIST_PF/PROTECT-P/PR.DS-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.DS-P2",
                "description": "Data-in-transit are protected.",
                "path": "NIST_PF/PROTECT-P/PR.DS-P2.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P4",
                "description": "Policy and regulations regarding the physical operating environment for organiza...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P4.json"
            }
        ]
    },
    {
        "sub_domain_id": "D-10.3",
        "applicable_regulations": [
            "GDPR",
            "CRA"
        ],
        "controls": [
            {
                "framework": "CSF",
                "function": "DETECT",
                "control_id": "DE.AE-02",
                "description": "Potentially adverse events are analyzed to better understand associated activiti...",
                "path": "NIST_CSF/DETECT/DE.AE-02.json"
            },
            {
                "framework": "CSF",
                "function": "GOVERN",
                "control_id": "GV.OV-03",
                "description": "Organizational cybersecurity risk management performance is evaluated and review...",
                "path": "NIST_CSF/GOVERN/GV.OV-03.json"
            },
            {
                "framework": "CSF",
                "function": "IDENTIFY",
                "control_id": "ID.RA-05",
                "description": "Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere...",
                "path": "NIST_CSF/IDENTIFY/ID.RA-05.json"
            },
            {
                "framework": "CSF",
                "function": "?",
                "control_id": "PR.IP-07",
                "description": "?",
                "path": "NIST_CSF/?/PR.IP-07.json"
            },
            {
                "framework": "CSF",
                "function": "PROTECT",
                "control_id": "PR.PS-04",
                "description": "Log records are generated and made available for continuous monitoring",
                "path": "NIST_CSF/PROTECT/PR.PS-04.json"
            },
            {
                "framework": "PF",
                "function": "COMMUNICATE-P",
                "control_id": "CM.AW-P2",
                "description": "Mechanisms for obtaining feedback from individuals (e.g., surveys or focus group...",
                "path": "NIST_PF/COMMUNICATE-P/CM.AW-P2.json"
            },
            {
                "framework": "PF",
                "function": "CONTROL-P",
                "control_id": "CT.DM-P1",
                "description": "Data elements can be accessed for review",
                "path": "NIST_PF/CONTROL-P/CT.DM-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P1",
                "description": "Privacy risk is re-evaluated on an ongoing basis and as key factors, including t...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P1.json"
            },
            {
                "framework": "PF",
                "function": "GOVERN-P",
                "control_id": "GV.MT-P2",
                "description": "Privacy values, policies, and training are reviewed and any updates are communic...",
                "path": "NIST_PF/GOVERN-P/GV.MT-P2.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P1",
                "description": "Contextual factors related to the systems/products/services and the data actions...",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P1.json"
            },
            {
                "framework": "PF",
                "function": "IDENTIFY-P",
                "control_id": "ID.RA-P3",
                "description": "Potential problematic data actions and associated problems are identified.",
                "path": "NIST_PF/IDENTIFY-P/ID.RA-P3.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P1",
                "description": "A baseline configuration of information technology is created and maintained inc...",
                "path": "NIST_PF/PROTECT-P/PR.PO-P1.json"
            },
            {
                "framework": "PF",
                "function": "PROTECT-P",
                "control_id": "PR.PO-P3",
                "description": "Backups of information are conducted, maintained, and tested.",
                "path": "NIST_PF/PROTECT-P/PR.PO-P3.json"
            }
        ]
    }
]


# 9. Build nodes + links
# ---------------------------------------------------------------------------

def build() -> dict:
    nodes: list[dict] = []
    links: list[dict] = []
    # Phase C — tier drift accumulator (Doc12 §4 vs existing proportionality_tier).
    # Initialised here to be a fresh list per build() call.  Surfaced as CFL-006
    # audit if any drift is detected.
    _TIER_DRIFT: list[dict] = []

    # CompanyContext (1)
    nodes.append(COMPANY["node"])

    # Regulations (5)
    for r in REGULATIONS:
        nodes.append({"id": r["id"], "type": r["type"], "label": r["label"],
                      "attrs": r["attrs"], "source": r["source"]})

    # Domains (10) + SecurityControlDomain (38)
    sd_by_id = {sid: (sid, name, regs, covered, lvl, tier, inactive, sole)
                for (sid, name, regs, covered, lvl, tier, inactive, sole)
                in SUBDOMAIN_DEFS}

    for (did, dlabel, pdriver, sd_count) in DOMAINS:
        nodes.append({
            "id": did, "type": "Domain",
            "label": dlabel,
            "attrs": {
                "primary_regulatory_driver": pdriver,
                "subdomain_count": sd_count,
            },
            "source": ["phase1_ontology.yaml@domains", "Doc11 §3"],
        })

    for (sid, name, regs, covered, lvl, tier, inactive, sole) in SUBDOMAIN_DEFS:
        attrs = {
            "domain_id": sid.rsplit(".", 1)[0],
            "name": name,
            "covered": covered,
            "active": not inactive,
            "coverage_level": lvl,
        }
        if tier is not None:
            attrs["proportionality_tier"] = tier
        if covered:
            attrs["source_regulations"] = regs
        else:
            attrs["sole_authority_regulation"] = sole
            attrs["gap_reason"] = (
                f"{sole} not applicable ({'below 50 employees' if sole == 'NIS2' else 'not financial entity'})"
            )
        if inactive:
            attrs["inactive_reason"] = "NIS2 not applicable (below 50 employees)"

        nodes.append({
            "id": sid, "type": "SecurityControlDomain",
            "label": f"{sid} {name}",
            "attrs": attrs,
            "source": [
                "phase1_ontology.yaml@subdomains",
                "Doc11 §3",
                "Doc12 §4",
            ],
        })

    # RegulatoryClause (54)
    for (cid, reg_id, article, desc, sd, nw, ot, op) in CLAUSES:
        nodes.append({
            "id": cid, "type": "RegulatoryClause",
            "label": f"{cid} {article} — {desc}",
            "attrs": {
                "regulation_id": reg_id,
                "article": article,
                "description": desc,
                "normative_weight": nw,
                "obligation_type": ot,
                "obligated_party": op,
                "maps_to_subdomain": sd,
            },
            "source": [
                "phase1_ontology.yaml@clause_mappings",
                "Doc10 §8.1 (GDPR) / §8.2 (CRA)",
            ],
        })

    # AdjustedGoal (69 distinct): 35 slot-001 + 34 slot-002
    for sid in ACTIVE_35:
        # slot-001
        track = "GDPR" if sid in GDPR_POPULATED else "HL"
        goal_id = f"AG-{sid}-001"
        nodes.append({
            "id": goal_id,
            "type": "AdjustedGoal",
            "label": f"{goal_id} (HL{'/GDPR-driven' if track=='GDPR' else ''})",
            "attrs": {
                "subdomain_id": sid,
                "slot": "001",
                "track": track,
                "priority": "MUST",
                "tier": SD_TIER[sid],
            },
            "source": [
                "Doc13 §2 (HL row)" if track == "HL" else "Doc13 §2 (HL) + §3 (GDPR-driven)",
            ],
        })

    for sid in ACTIVE_35:
        if sid == "D-05.4":
            continue  # corpus has no CRA Sub-SO for D-05.4
        # slot-002
        goal_id = f"AG-{sid}-002"
        nodes.append({
            "id": goal_id,
            "type": "AdjustedGoal",
            "label": f"{goal_id} (CRA-driven)",
            "attrs": {
                "subdomain_id": sid,
                "slot": "002",
                "track": "CRA",
                "priority": "MUST",
                "tier": SD_TIER[sid],
            },
            "source": ["Doc13 §4 (CRA-driven row)"],
        })

    # Tensions (4) — optional, but spec says "optionally +4 Tension"
    for t in TENSIONS:
        nodes.append({
            "id": t["id"], "type": t["type"], "label": t["label"],
            "attrs": t["attrs"], "source": t["source"],
        })

    # Stakeholders (7) — Sprint 6 / ontology v1.2
    for stk in STAKEHOLDERS:
        nodes.append({
            "id": stk["id"], "type": "Stakeholder", "label": stk["label"],
            "attrs": stk["attrs"], "source": stk["source"],
        })

    # BusinessGoals (5)
    for bg in BUSINESS_GOALS:
        nodes.append({
            "id": bg["id"], "type": "BusinessGoal", "label": bg["label"],
            "attrs": bg["attrs"], "source": bg["source"],
        })

    # CoverageGaps (4)
    for gap in COVERAGE_GAPS:
        nodes.append({
            "id": gap["id"], "type": "CoverageGap", "label": gap["label"],
            "attrs": gap["attrs"], "source": gap["source"],
        })

    # RaciRoles (6) — Sprint 7 / ontology v1.3 (Doc07 §2)
    for role in RACI_ROLES:
        nodes.append({
            "id": role["id"], "type": "RaciRole", "label": role["label"],
            "attrs": role["attrs"], "source": role["source"],
        })

    # RaciActivities (43) — Sprint 7 / ontology v1.3 (Doc07 §4.1–§4.10)
    for act in RACI_ACTIVITIES:
        nodes.append({
            "id": act["id"], "type": "RaciActivity", "label": act["label"],
            "attrs": act["attrs"], "source": act["source"],
        })

    # EvidenceItems (>=37 Coverage + Capability) — Sprint 9 / ontology v1.6
    # (MATURITY_MODEL_CSF_STRICT.md §6). Each EVIDENCE_ITEMS seed produces one
    # node whose attrs include scale (capability/coverage), outcome (clause or
    # CSF subcategory), claim (one-sentence observable fact), sources (IDs
    # resolvable to other graph nodes) and observed (True/False).
    for ev in EVIDENCE_ITEMS:
        nodes.append({
            "id": ev["ev_id"], "type": "EvidenceItem", "label": ev["claim"][:80],
            "attrs": {
                "ev_id":        ev["ev_id"],
                "subdomain_id": ev["subdomain_id"],
                "scale":        ev["scale"],
                "outcome":      ev["outcome"],
                "claim":        ev["claim"],
                "sources":      list(ev["sources"]),
                "observed":     bool(ev["observed"]),
            },
            "source": ["MATURITY_MODEL_CSF_STRICT.md §6",
                       "phase1_ontology.yaml@kg_ontology.maturity_model"],
        })

    # Sprint 8 / Phase B — Architecture & Third Parties (Doc04 + Doc06)
    # Systems (5)
    for sys in SYSTEMS:
        nodes.append({
            "id": sys["id"], "type": "System", "label": sys["label"],
            "attrs": sys["attrs"], "source": sys["source"],
        })
    # DataStores (3)
    for store in DATASTORES:
        nodes.append({
            "id": store["id"], "type": "DataStore", "label": store["label"],
            "attrs": store["attrs"], "source": store["source"],
        })
    # DataFlows (5)
    for flow in DATAFLOWS:
        nodes.append({
            "id": flow["id"], "type": "DataFlow", "label": flow["label"],
            "attrs": flow["attrs"], "source": flow["source"],
        })
    # PersonalDataCategories (4)
    for pdc in PERSONAL_DATA_CATEGORIES:
        nodes.append({
            "id": pdc["id"], "type": "PersonalDataCategory", "label": pdc["label"],
            "attrs": pdc["attrs"], "source": pdc["source"],
        })
    # DataSubjectCategories (3)
    for dsc in DATA_SUBJECT_CATEGORIES:
        nodes.append({
            "id": dsc["id"], "type": "DataSubjectCategory", "label": dsc["label"],
            "attrs": dsc["attrs"], "source": dsc["source"],
        })
    # ThirdParties (6)
    for tp in THIRD_PARTIES:
        nodes.append({
            "id": tp["id"], "type": "ThirdParty", "label": tp["label"],
            "attrs": tp["attrs"], "source": tp["source"],
        })

    # ----- Phase C (Doc08 §9 + Doc12 §4) — Maturity & verification attrs -----
    # Build an id->node index for the in-place merge below.  The merge
    # ADDS new attrs keys only — existing ids, edge ids and edge attrs are
    # untouched.  Hard constraint: "DO NOT change existing node IDs, edge
    # IDs, edge attrs, audit IDs. DO NOT remove existing attrs — only add."
    nodeById: dict[str, dict] = {n["id"]: n for n in nodes}

    # Phase C / Doc08 §9 -> merge into the 54 RegulatoryClause nodes
    # v1.6 change (MATURITY_MODEL_CSF_STRICT.md §9): the prior `maturity_cur` /
    # `maturity_tgt` integer pair is REMOVED from RegulatoryClause attrs.  Per
    # §6/§10, capability lives at Org/Function scope only (TierDecision); sub-domain
    # holds EVIDENCE.  RegulatoryClause nodes retain verification criteria + risk +
    # evidence_type (those are not maturity scalars).
    for v in ART_VERIFICATION:
        cid = v["clause_id"]
        if cid in nodeById and nodeById[cid].get("type") == "RegulatoryClause":
            nodeById[cid]["attrs"].update({
                "verification_criteria": v["verification_criteria"],
                "evidence_type":         v["evidence_type"],
                "risk_if_not_met":       v["risk_if_not_met"],
                # NOTE: maturity_cur/tgt removed in v1.6 — coverage is now expressed
                # via EvidenceItem nodes (Scale B) anchored on each sub-domain and
                # linked to this clause by CITES_CLAUSE.
            })

    # Phase C / Doc12 §4 -> merge into the 37 ACTIVE SecurityControlDomain nodes
    # Strict rule (per executor brief): attrs.tier (new) and attrs.proportionality_tier
    # (existing v1.2) MUST match.  Verified 37/37 at static reconciliation; the
    # merge below asserts equality per-node and surfaces an audit (CFL-006)
    # only when drift is detected — silent overwrites are forbidden.
    for p in SUBDOMAIN_PROPORTIONALITY:
        sid = p["sub_domain_id"]
        if sid in nodeById and nodeById[sid].get("type") == "SecurityControlDomain":
            n = nodeById[sid]
            existing_tier = n["attrs"].get("proportionality_tier")
            if existing_tier is not None and existing_tier != p["tier"]:
                # Drift detected: record and DO NOT overwrite attrs.tier (the
                # existing proportionality_tier value wins).
                _TIER_DRIFT.append({"sub_domain_id": sid,
                                    "attrs_proportionality_tier": existing_tier,
                                    "doc12_section4_tier": p["tier"]})
            n["attrs"].update({
                "i": p["i"],
                "p": p["p"],
                # NOTE v1.6: 'tier' attr REMOVED — it duplicated proportionality_tier and
                # collided with MATURITY_MODEL_CSF_STRICT.md §10 (Tier scalars forbidden
                # at sub-domain scope). proportionality_tier remains as the single attr.
                "satisfaction_pattern": p["satisfaction_pattern"],
                "evidence_depth":       p["evidence_depth"],
                "verification_method":  p["verification_method"],
                "ownership":            p["ownership"],
                "example_controls":     p["example_controls"],
                "notes":                p["notes"],
                "risk_if_not_met":      p["risk_if_not_met"],
                "evidence_ids":         list(COVERAGE_EV_BY_SUBDOMAIN.get(sid, [])),
                "implementation_priority": p["implementation_priority"],
            })

    # ----- Links -----
    # ASSESSES: CompanyContext --applies--> Regulation (2 applicable regs)
    for r in REGULATIONS:
        if r["attrs"]["applicable"]:
            links.append({
                "from": "CC-TINYTASK-2026-001", "to": r["id"],
                "rel": "ASSESSES",
                "attrs": {"obligated_party": r["attrs"]["obligated_party"],
                          "applicable": True},
                "source": ["phase1_ontology.yaml@applicability_assessments",
                           "Doc08 §4"],
            })

    # MAPS_TO: RegulatoryClause → SecurityControlDomain (54)
    for (cid, reg_id, article, desc, sd, *_) in CLAUSES:
        links.append({
            "from": cid, "to": sd, "rel": "MAPS_TO",
            "attrs": {"article": article},
            "source": ["phase1_ontology.yaml@clause_mappings", "Doc10 §8"],
        })

    # BELONGS_TO: SecurityControlDomain → Domain (38)
    for (sid, *_) in SUBDOMAIN_DEFS:
        parent = sid.rsplit(".", 1)[0]
        links.append({
            "from": sid, "to": parent, "rel": "BELONGS_TO",
            "attrs": {},
            "source": ["phase1_ontology.yaml@subdomains", "Doc11 §3"],
        })

    # YIELDS: SecurityControlDomain → AdjustedGoal (slot-001 + slot-002)
    for sid in ACTIVE_35:
        links.append({
            "from": sid, "to": f"AG-{sid}-001", "rel": "YIELDS",
            "attrs": {"slot": "001", "track": "GDPR" if sid in GDPR_POPULATED else "HL"},
            "source": ["Doc13 §2/§3"],
        })
    for sid in ACTIVE_35:
        if sid == "D-05.4":
            continue
        links.append({
            "from": sid, "to": f"AG-{sid}-002", "rel": "YIELDS",
            "attrs": {"slot": "002", "track": "CRA"},
            "source": ["Doc13 §4"],
        })

    # OVERLAPS_WITH: Regulation → Regulation (GDPR ∩ CRA)
    links.append({
        "from": "REG-GDPR", "to": "REG-CRA", "rel": "OVERLAPS_WITH",
        "attrs": {
            "shared_subdomains_count": 7,
            "shared_subdomains": [
                "D-01.1", "D-01.2", "D-04.2", "D-04.3", "D-05.3", "D-07.1", "D-10.3",
            ],
            "jaccard_index": 0.367,
        },
        "source": ["phase1_ontology.yaml@overlaps[GDPR-CRA]"],
    })

    # HAS_TENSION_WITH: RegulatoryClause → RegulatoryClause (4)
    for t in TENSIONS:
        links.append({
            "from": t["attrs"]["clause_1"], "to": t["attrs"]["clause_2"],
            "rel": "HAS_TENSION_WITH",
            "attrs": {
                "kind": t["attrs"]["kind"],
                "severity": t["attrs"]["severity"],
                "resolution_approach": t["attrs"]["resolution_approach"],
            },
            "source": t["source"],
        })

    # COVERS: CompanyContext → SecurityControlDomain (37 ACTIVE subdomains per
    # Doc12 §3 — D-08.3 inactive). These are the company-coverage edges
    # inferred from the applicable regulations (Doc11 §3 CONSOLIDATED_VIEW).
    for (sid, name, regs, covered, lvl, tier, inactive, sole) in SUBDOMAIN_DEFS:
        if inactive:
            continue
        links.append({
            "from": "CC-TINYTASK-2026-001", "to": sid, "rel": "COVERS",
            "attrs": {
                "covered": covered,
                "coverage_level": lvl,
                "tier": tier,
                "source_regulations": regs,
            },
            "source": ["Doc11 §3 (CONSOLIDATED_VIEW)", "Doc12 §3-§4"],
        })

    # COVERS_FROM: Regulation → SecurityControlDomain (per ontology
    # source_regulations on each covered subdomain — 38 edges for the regs
    # that drive each subdomain)
    for (sid, name, regs, covered, lvl, tier, inactive, sole) in SUBDOMAIN_DEFS:
        if not covered:
            continue
        for reg in regs:
            reg_id = f"REG-{reg}"
            if reg_id in ("REG-GDPR", "REG-CRA"):
                links.append({
                    "from": reg_id, "to": sid, "rel": "COVERS",
                    "attrs": {"coverage_level": lvl},
                    "source": ["phase1_ontology.yaml@subdomains.covered.source_regulations"],
                })

    # DEFINES: Stakeholder → BusinessGoal (each BG mapped to stakeholder(s)
    # explicitly named in Doc03 §4 Owner + Affected Stakeholders columns;
    # role labels that do not map unambiguously to an STK-ID are SKIPPED
    # — see CVE-005 audit and Doc03 §4 verbatim).
    for (stk_id, bg_id, evidence) in DEFINES_EDGES:
        links.append({
            "from": stk_id, "to": bg_id, "rel": "DEFINES",
            "attrs": {"evidence": evidence},
            "source": ["Doc03 §4 BG table", "phase1_ontology.yaml@kg_ontology.classes.BusinessGoal"],
        })

    # FLAGS: CoverageGap → SecurityControlDomain. Each gap's
    # affected_subdomain_ids is iterated; only IDs that resolve to an
    # existing SecurityControlDomain node produce an edge. GAP-002 has
    # affected_subdomain_ids=["D-01"] (Domain, not subdomain) — that
    # ID does not match the SecurityControlDomain pattern, so no FLAGS
    # edge is emitted; the type mismatch is flagged by CFL-005 audit.
    sd_ids = {n["id"] for n in nodes if n["type"] == "SecurityControlDomain"}
    for (gap_id, sub_id, source_section) in FLAGS_EDGES:
        if sub_id not in sd_ids:
            continue
        links.append({
            "from": gap_id, "to": sub_id, "rel": "FLAGS",
            "attrs": {"severity": next(g["attrs"]["severity"] for g in COVERAGE_GAPS if g["id"] == gap_id)},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.CoverageGap"],
        })

    # MaturityModel v1.6 edges:
    #   HAS_EVIDENCE   — SecurityControlDomain → EvidenceItem
    #   CITES_CLAUSE   — EvidenceItem → RegulatoryClause   (Scale B: coverage anchors)
    #   CITES_OUTCOME  — EvidenceItem → NistControl         (Scale A: capability anchors)
    # All three verbs declared in phase1_ontology.yaml@kg_ontology.maturity_model.
    # CITES_CLAUSE / CITES_OUTCOME are mutually exclusive per EvidenceItem (decided
    # by EvidenceItem.scale); the build emits only the relevant edge per node.
    for ev in EVIDENCE_ITEMS:
        ev_id = ev["ev_id"]
        sid = ev["subdomain_id"]
        outcome = ev["outcome"]
        links.append({
            "from": sid, "to": ev_id, "rel": "HAS_EVIDENCE",
            "attrs": {"scale": ev["scale"], "observed": bool(ev["observed"])},
            "source": ["MATURITY_MODEL_CSF_STRICT.md §6",
                       "phase1_ontology.yaml@kg_ontology.maturity_model"],
        })
        if ev["scale"] == "coverage":
            # Coverage evidence cites a regulatory clause id (GDPR-Cnn / CRA-Cnn)
            links.append({
                "from": ev_id, "to": outcome, "rel": "CITES_CLAUSE",
                "attrs": {"scale": "coverage"},
                "source": ["MATURITY_MODEL_CSF_STRICT.md §5/§6"],
            })
        elif ev["scale"] == "capability":
            # Capability evidence cites a CSF 2.0 subcategory id (e.g. PR.DS-01)
            links.append({
                "from": ev_id, "to": outcome, "rel": "CITES_OUTCOME",
                "attrs": {"scale": "capability",
                          "framework": "CSF",
                          "outcome_id": outcome},
                "source": ["MATURITY_MODEL_CSF_STRICT.md §5/§6",
                           "OVERLAY_NIST_CSF_2.0.md §2"],
            })

    # RACI: RaciRole → RaciActivity — 206 edges (one per non-'—' cell; composite
    # 'R/A' cells already split into 2 edges inside RACI_EDGES). Each link
    # carries attrs.letter (∈ {R,A,C,I}) + attrs.activity_id for traceability.
    # Sprint 7 / ontology v1.3 (Doc07 §4.1–§4.10).
    for (role_id, act_id, letter, source_section) in RACI_EDGES:
        links.append({
            "from": role_id, "to": act_id, "rel": "RACI",
            "attrs": {"letter": letter, "activity_id": act_id},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.RaciRole"],
        })

    # APPLIES_TO: RaciActivity → SecurityControlDomain — 35 edges (one per
    # Doc07 §9.2 row; collapsed groups emit from the representative activity).
    # Sprint 7 / ontology v1.3 (Doc07 §9.2).
    for (act_id, sub_id, source_section) in APPLIES_TO_EDGES:
        links.append({
            "from": act_id, "to": sub_id, "rel": "APPLIES_TO",
            "attrs": {},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.RaciActivity"],
        })

    # Sprint 8 / Phase B — Architecture & Third Parties edge emission.
    # HOSTS: System → DataStore (Doc04 §2.1)
    for (sys_id, store_id, source_section) in HOSTS_EDGES:
        links.append({
            "from": sys_id, "to": store_id, "rel": "HOSTS",
            "attrs": {},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.System"],
        })
    # INVOLVES: SecurityControlDomain → System (Doc04 §3)
    for (sd_id, sys_id, source_section) in INVOLVES_EDGES:
        links.append({
            "from": sd_id, "to": sys_id, "rel": "INVOLVES",
            "attrs": {},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.SecurityControlDomain"],
        })
    # INVOLVES_STORE: SecurityControlDomain → DataStore (Doc04 §3)
    for (sd_id, store_id, source_section) in INVOLVES_STORE_EDGES:
        links.append({
            "from": sd_id, "to": store_id, "rel": "INVOLVES_STORE",
            "attrs": {},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.SecurityControlDomain"],
        })
    # INVOLVES_FLOW: SecurityControlDomain → DataFlow (Doc04 §3)
    for (sd_id, flow_id, source_section) in INVOLVES_FLOW_EDGES:
        links.append({
            "from": sd_id, "to": flow_id, "rel": "INVOLVES_FLOW",
            "attrs": {},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.SecurityControlDomain"],
        })
    # PROCESSES: DataFlow → ThirdParty (Doc04 §2.2 + Doc06 §4.1)
    for (flow_id, tp_id, source_section) in PROCESSES_EDGES:
        links.append({
            "from": flow_id, "to": tp_id, "rel": "PROCESSES",
            "attrs": {},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.ThirdParty"],
        })
    # PROCESSED_BY: PersonalDataCategory → System (Doc04 §2.3)
    for (pdc_id, sys_id, source_section) in PROCESSED_BY_EDGES:
        links.append({
            "from": pdc_id, "to": sys_id, "rel": "PROCESSED_BY",
            "attrs": {},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.PersonalDataCategory"],
        })
    # PROCESSED_BY_3P: PersonalDataCategory → ThirdParty (Doc04 §2.3 + Doc06 §4.1)
    for (pdc_id, tp_id, source_section) in PROCESSED_BY_3P_EDGES:
        links.append({
            "from": pdc_id, "to": tp_id, "rel": "PROCESSED_BY_3P",
            "attrs": {},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.ThirdParty"],
        })
    # CAPTURES: DataSubjectCategory → PersonalDataCategory (Doc04 §2.4)
    for (dsc_id, pdc_id, source_section) in CAPTURES_EDGES:
        links.append({
            "from": dsc_id, "to": pdc_id, "rel": "CAPTURES",
            "attrs": {},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.DataSubjectCategory"],
        })
    # CORRESPONDS_TO: ThirdParty → Stakeholder (Doc03 §3.1 + Doc06)
    for (tp_id, stk_id, source_section) in CORRESPONDS_TO_EDGES:
        links.append({
            "from": tp_id, "to": stk_id, "rel": "CORRESPONDS_TO",
            "attrs": {},
            "source": [source_section, "phase1_ontology.yaml@kg_ontology.classes.ThirdParty"],
        })

    # ----- Ambiguity block -----
    ambiguity = {
        "stats_total": {
            "cards_in_scope": 417,
            "by_severity": {"S1": 0, "S2": 251, "S3": 252},
            "by_regulation": {"GDPR": 276, "CRA": 141},
        },
        "stats_per_subdomain": [
            {"subdomain_id": sid, "in_scope": inc, "total": tot,
             "source": "Doc09 §2"}
            for (sid, inc, tot) in PER_SD_INSCOPE
        ],
        "top_cards": TOP_CARDS,
    }

    invariants = {
        "regulations_total": 5,
        "regulations_applicable": 2,
        "domains": 10,
        "subdomains_total": 38,
        "subdomains_covered": 31,
        "subdomains_active": 37,
        "clauses_total": 54,
        "goals_total": 69,
        "tensions_total": 4,
        "ambiguity_cards_in_scope": 417,
        # Sprint 6 (kg_ontology v1.2) — new counts per ontology@invariants.counts
        "stakeholders_total": 7,
        "business_goals_total": 5,
        "coverage_gaps_total": 4,
        # Sprint 7 (kg_ontology v1.3) — RACI Phase A (Doc07 §2/§4/§7/§9.2)
        # Counts reflect actual extracted data; 41 active activities (43 total
        # minus ACT-34 all-'—' placeholder + ACT-35 best-practice, active=false).
        "raci_roles": 6,
        "raci_activities": 43,
        "raci_activities_active": 41,
        "raci_edges_min": 206,  # 200 single-letter cells + 3 R/A composites × 2 = 6 edges
        "raci_composite_cells": 3,  # ACT-27 Dev=R/A, ACT-28 Dev=R/A, ACT-33 DPO=R/A
        "applies_to_edges": 35,  # Doc07 §9.2 has 35 rows
        "gap_raci_count": 5,  # GAP-RACI-01..05 from §7
        # Sprint 8 / Phase B — Doc04 + Doc06 (Architecture & Third Parties).
        # Counts match ontology@invariants.counts v1.4 new keys.
        "systems": 5,                       # Doc04 §1.1 SYS-01..SYS-05
        "data_stores": 3,                  # Doc04 §2.1 STORE-01..STORE-03
        "data_flows": 5,                   # Doc04 §2.2 FLOW-01..FLOW-05
        "personal_data_categories": 4,     # Doc04 §2.3 Email/Names/Project/Payment
        "data_subject_categories": 3,      # Doc04 §2.4 EU/Free-tier/Enterprise
        "third_parties": 6,                # Doc06 §5 vendor count
        "compliance_mapping_rows": 37,     # Doc04 §3 Compliance Mapping rows (active sub-domains; D-08.3 INACTIVE)
        # Phase C — Doc08 §9 + Doc12 §4 verification & proportionality attributes
        "articles_with_verification": 54,       # Doc08 §9 = 28 GDPR + 26 CRA
        "subdomains_with_proportionality": 37,  # Doc12 §4 (active only, D-08.3 excluded)
        # Phase D — Doc13 §7 NIST Controls Mapping (NIST_ALIGNMENT table).
        # 117 unique control IDs (77 CSF + 38 PF + 2 AI-RMF) across 513
        # (sub-domain × control_id) alignments.  Only D-04.2 has NIST AI-RMF controls.
        "nist_controls": 127,
        "nist_alignments": 513,
        "nist_aimrm_subdomains": 1,
    }

    # ----- Phase C: surface tier drift accumulator as CFL-006 audit (only if drift detected) -----
    audits_out = list(AUDITS)
    if _TIER_DRIFT:
        audits_out.append({
            "id": "CFL-006",
            "kind": "cross_doc_conflict",
            "severity": "high",
            "title": f"Doc12 §4 attrs.tier diverges from attrs.proportionality_tier on {len(_TIER_DRIFT)} sub-domain(s)",
            "detail": (
                "The merge logic in build() detected divergence between Doc12 §4 'Tier' column and the "
                "v1.2 attrs.proportionality_tier set during sub-domain node construction.  The merge refuses "
                "to overwrite attrs.tier silently when the existing value differs; instead it records the "
                "drift here for human reconciliation per P7.  Static reconciliation at generator time confirmed "
                "37/37 match — drift in this build() run means the dict was mutated externally between runs."
            ),
            "evidence": ["_TIER_DRIFT (list) populated during merge"],
            "node_ids": [d["sub_domain_id"] for d in _TIER_DRIFT],
            "recommendation": (
                "Human (P7) — verify the drift entries below against phase1_ontology.yaml@subdomains and Doc12 §4 "
                "and reconcile by updating either SUBDOMAIN_DEFS (v1.2 tier) or SUBDOMAIN_PROPORTIONALITY (v1.4 tier) "
                "in scripts/build_p1_graph.py.  Then re-run --emit to confirm drift clears.  Drift entries: "
                + repr(_TIER_DRIFT) + "."
            ),
        })

    # ----- Phase D — Doc13 §7 NIST Controls Mapping (NistControl nodes + ALIGNS_TO edges) -----
    # Per the orchestrator brief, emit:
    #   * one NistControl node per unique (framework, control_id)
    #   * one ALIGNS_TO edge per (sub_domain_id, control_id) tuple
    #   * an `attrs.nist_alignment_count` integer per sub-domain (additive — does NOT
    #     strip existing v1.4 attrs like `tier`, `proportionality_tier`, etc.)
    #   * 2 NEW audits (NEW-09 coverage_gap on '?' Function rows, NEW-10 cross_doc_conflict
    #     on D-04.2 being the sole §7 sub-section with AI-RMF controls).
    # Malformed '?' Function rows are emitted with the canonical NIST CSF 2.0 Function
    # assignment from _NIST_MALFORMED_FUNCTION_OVERRIDES (7 unique IDs; 8 rows total
    # because RS.CO-04 appears in both D-04.3 and D-06.3).
    nist_node_by_cid: dict[tuple[str, str], dict] = {}  # (framework, control_id) -> node dict
    sd_alignment_count: dict[str, int] = {}
    nist_aimrm_subdomains: set[str] = set()
    malformed_rows: list[tuple[str, str, str]] = []  # (sd, framework, control_id)

    # Iterate NIST_ALIGNMENT and emit nodes/edges
    for entry in NIST_ALIGNMENT:
        sd_id = entry["sub_domain_id"]
        for c in entry["controls"]:
            framework = c["framework"]
            control_id = c["control_id"]
            raw_function = c["function"]
            # Apply override if Function was '?'
            if raw_function == "?" or raw_function == "":
                canon_fn = _NIST_MALFORMED_FUNCTION_OVERRIDES.get(control_id, "UNKNOWN")
                malformed_rows.append((sd_id, framework, control_id))
            else:
                canon_fn = raw_function
            # NistControl node — one per (framework, control_id)
            key = (framework, control_id)
            if key not in nist_node_by_cid:
                nid = f"NIST-{control_id}"
                nist_node_by_cid[key] = {
                    "id": nid,
                    "type": "NistControl",
                    "label": control_id,
                    "attrs": {
                        "control_id": control_id,
                        "framework": framework,
                        "function": canon_fn,
                        "description": c["description"],
                        "path": c["path"],
                    },
                    "source": [
                        "Doc13 §7 NIST Controls Mapping",
                        "phase1_ontology.yaml@kg_ontology.classes.NistControl",
                    ],
                }
                if framework == "AI-RMF":
                    # nist_aimrm_subdomains tracked per-sub-domain below
                    pass
            # Track alignment count per sub-domain
            sd_alignment_count[sd_id] = sd_alignment_count.get(sd_id, 0) + 1
            # Track AI-RMF subdomains
            if framework == "AI-RMF":
                nist_aimrm_subdomains.add(sd_id)
            # Emit ALIGNS_TO edge
            links.append({
                "from": sd_id,
                "to": f"NIST-{control_id}",
                "rel": "ALIGNS_TO",
                "attrs": {
                    "framework": framework,
                    "function": canon_fn,
                },
                "source": [
                    "Doc13 §7 NIST Controls Mapping",
                    "phase1_ontology.yaml@kg_ontology.relations.ALIGNS_TO",
                ],
            })

    # Append NistControl nodes
    for nd in nist_node_by_cid.values():
        nodes.append(nd)

    # ----- v1.6 — NIST Privacy Framework 1.0 NistControl nodes (additive) -----
    # Authority: 00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/OVERLAY_NIST_PF_1.1.md §2.
    # Function mapping: GV-/GV.* -> GOVERN-P; ID-/ID.* -> IDENTIFY-P; PR-/PR.* -> PROTECT-P;
    #                   CT-/CT.* -> CONTROL-P;  CM-/CM.* -> COMMUNICATE-P.
    # These 10 outcomes back the Scale A PF Capability radar (Folio VIII). They are NOT
    # full Tier decisions — they are evidence anchors (see MATURITY_MODEL_CSF_STRICT.md §6).
    PF_OUTCOMES = [
        ("GV-PO-P1", "GOVERN-P",     "Privacy governance roles established"),
        ("GV-PO-P5", "GOVERN-P",     "Privacy policies aligned with applicable laws"),
        ("GV-AT-P1", "GOVERN-P",     "Awareness training for staff (privacy)"),
        ("GV-MA-P1", "GOVERN-P",     "Privacy risk monitoring/review"),
        ("ID-RA-P3", "IDENTIFY-P",   "Privacy risk assessment for data processing"),
        ("ID-IM-P1", "IDENTIFY-P",   "Data processing inventory (RoPA)"),
        ("PR-PO-P1", "PROTECT-P",    "Data confidentiality, integrity, availability"),
        ("CT-PO-P4", "CONTROL-P",    "Data processing policies / purpose limitation"),
        ("CT-DM-P5", "CONTROL-P",    "Disposal of personal data (erasure)"),
        ("CM-PO-P1", "COMMUNICATE-P","Communication of privacy practices"),
    ]
    for cid_pf, fn_pf, desc_pf in PF_OUTCOMES:
        nid = f"NIST-{cid_pf}"
        if nid not in nist_node_by_cid:
            nist_node_by_cid[(("PF", cid_pf))] = {
                "id": nid,
                "type": "NistControl",
                "label": cid_pf,
                "attrs": {
                    "control_id": cid_pf,
                    "framework": "PF",
                    "function": fn_pf,
                    "description": desc_pf,
                    "path": "00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/OVERLAY_NIST_PF_1.1.md §2",
                },
                "source": [
                    "OVERLAY_NIST_PF_1.1.md §2",
                    "phase1_ontology.yaml@kg_ontology.classes.NistControl",
                ],
            }
            # Emit the node immediately so CITES_OUTCOME links resolve later.
            nodes.append(nist_node_by_cid[("PF", cid_pf)])

    # Add nist_alignment_count to each sub-domain (additive — does not strip existing attrs)
    for sd_id, count in sd_alignment_count.items():
        if sd_id in nodeById:
            nodeById[sd_id]["attrs"]["nist_alignment_count"] = count

    # ----- Phase D — append NEW-09 and NEW-10 audits -----
    malformed_sd_ids = sorted({sd for sd, _, _ in malformed_rows})
    audits_out.append({
        "id": "NEW-09",
        "kind": "coverage_gap",
        "severity": "medium",
        "title": (
            f"Doc13 §7 has {len(malformed_rows)} control row(s) with malformed '?' Function "
            "column (table-renderer truncation); emitted with canonical NIST CSF 2.0 Function assignment."
        ),
        "detail": (
            "Doc13 §7 NIST Controls Mapping has 8 rows where the table-renderer truncated the "
            "Function column to '?'.  These rows are still emitted as ALIGNS_TO edges with the "
            "control_id fully preserved; the Function field is filled in from "
            "_NIST_MALFORMED_FUNCTION_OVERRIDES (canonical NIST CSF 2.0 Function for each of "
            "the 7 unique IDs: RS.CO-04 → RESPOND, PR.AT-03 → PROTECT, PR.AT-04 → PROTECT, "
            "ID.SC-04 → IDENTIFY, PR.IP-06 → PROTECT, PR.IP-07 → PROTECT, PR.PT-01 → PROTECT). "
            "RS.CO-04 appears twice (D-04.3 + D-06.3) so 8 rows / 7 unique IDs."
        ),
        "evidence": [
            "Doc13 §7.14.1 line 829 (RS.CO-04 in D-04.3)",
            "Doc13 §7.22.1 line 1038 (RS.CO-04 in D-06.3)",
            "Doc13 §7.28.1 lines 1194–1195 (PR.AT-03 + PR.AT-04 in D-08.2)",
            "Doc13 §7.30.1 line 1256 (ID.SC-04 in D-09.2)",
            "Doc13 §7.34.1 lines 1372, 1374 (PR.IP-06 + PR.PT-01 in D-10.2)",
            "Doc13 §7.35.1 line 1409 (PR.IP-07 in D-10.3)",
        ],
        "node_ids": malformed_sd_ids,
        "recommendation": (
            "Human (P7) — re-render the Doc13 §7 tables so the Function column is never "
            "truncated; until then the generator script compensates via "
            "_NIST_MALFORMED_FUNCTION_OVERRIDES."
        ),
    })
    audits_out.append({
        "id": "NEW-10",
        "kind": "cross_doc_conflict",
        "severity": "low",
        "title": (
            "Doc13 §7.13.3 (D-04.2) is the only §7 sub-section with NIST AI-RMF controls (2)."
        ),
        "detail": (
            "Across all 35 active sub-domains in §7, only D-04.2 (Incident Containment & "
            "Response) has a §7.X.3 NIST AI RMF table, listing 2 controls: MANAGE-2.1 and "
            "MANAGE-2.3.  This is consistent with D-04.2's relevance to AI-system incident "
            "response per Doc13 §0 frontmatter, but means nist_aimrm_subdomains = 1 (not 35)."
        ),
        "evidence": [
            "Doc13 §7.13.3 lines 811–816 (MANAGE-2.1, MANAGE-2.3)",
            "Doc13 §7.1..§7.12, §7.14..§7.35: no §7.X.3 NIST AI RMF sub-table present",
        ],
        "node_ids": ["D-04.2", "NIST-MANAGE-2.1", "NIST-MANAGE-2.3"],
        "recommendation": (
            "Document the asymmetry: AI Act adoption drives the AI-RMF mapping; without an "
            "applicable AI Act scope for this case, no other sub-domain carries AI-RMF controls."
        ),
    })
    if _TIER_DRIFT:
        audits_out.append({
            "id": "CFL-006",
            "kind": "cross_doc_conflict",
            "severity": "high",
            "title": f"Doc12 §4 attrs.tier diverges from attrs.proportionality_tier on {len(_TIER_DRIFT)} sub-domain(s)",
            "detail": (
                "The merge logic in build() detected divergence between Doc12 §4 'Tier' column and the "
                "v1.2 attrs.proportionality_tier set during sub-domain node construction.  The merge refuses "
                "to overwrite attrs.tier silently when the existing value differs; instead it records the "
                "drift here for human reconciliation per P7.  Static reconciliation at generator time confirmed "
                "37/37 match — drift in this build() run means the dict was mutated externally between runs."
            ),
            "evidence": ["_TIER_DRIFT (list) populated during merge"],
            "node_ids": [d["sub_domain_id"] for d in _TIER_DRIFT],
            "recommendation": (
                "Human (P7) — verify the drift entries below against phase1_ontology.yaml@subdomains and Doc12 §4 "
                "and reconcile by updating either SUBDOMAIN_DEFS (v1.2 tier) or SUBDOMAIN_PROPORTIONALITY (v1.4 tier) "
                "in scripts/build_p1_graph.py.  Then re-run --emit to confirm drift clears.  Drift entries: "
                + repr(_TIER_DRIFT) + "."
            ),
        })

    return {
        "meta": META,
        "company_context": COMPANY,
        "nodes": nodes,
        "links": links,
        "ambiguity": ambiguity,
        "invariants": invariants,
        "audits": audits_out,
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Phase 1 graph builder")
    parser.add_argument("--emit", action="store_true",
                        help="Print the JSON to stdout (for piping into jq / curl).")
    parser.add_argument("--summary", action="store_true",
                        help="Print a one-line JSON summary to stdout.")
    args = parser.parse_args(argv[1:])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    graph = build()
    # Sanity counts (always to stderr so they don't pollute --emit stdout)
    by_type = {}
    for n in graph["nodes"]:
        by_type[n["type"]] = by_type.get(n["type"], 0) + 1
    print("nodes by type:", by_type, file=sys.stderr)
    print("link count:", len(graph["links"]), file=sys.stderr)
    print("audits count:", len(graph.get("audits", [])), file=sys.stderr)

    if args.emit:
        # JSON to stdout (no indent — keeps pipe-output compact)
        sys.stdout.write(json.dumps(graph, ensure_ascii=False))
        sys.stdout.write("\n")
        # Also write to the canonical file path so file consumers are in sync
        OUT.write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")
        return 0
    if args.summary:
        kinds: dict = {}
        for a in graph.get("audits", []):
            kinds[a["kind"]] = kinds.get(a["kind"], 0) + 1
        rels: dict = {}
        for l in graph["links"]:
            rels[l["rel"]] = rels.get(l["rel"], 0) + 1
        summary = {
            "nodes_count": sum(by_type.values()),
            "nodes_by_type": by_type,
            "links_count": len(graph["links"]),
            "links_by_rel": rels,
            "audits_count": len(graph.get("audits", [])),
            "audits_by_kind": kinds,
        }
        sys.stdout.write(json.dumps(summary, indent=2, ensure_ascii=False))
        sys.stdout.write("\n")
        OUT.write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")
        return 0

    # Default: write to canonical file path
    OUT.write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))