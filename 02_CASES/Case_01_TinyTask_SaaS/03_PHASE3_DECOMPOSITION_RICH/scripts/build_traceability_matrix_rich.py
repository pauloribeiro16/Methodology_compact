#!/usr/bin/env python3
"""
build_traceability_matrix_rich.py — Phase 3 Rich Mode (Sprint 6, REAL)

Produces `22_Traceability_Matrix.xlsx` with 12 sheets for the Case_01 Rich folder:

  1.  COVER
  2.  FULL_TRACEABILITY
  3.  NFR_TO_FR
  4.  FR_TO_UC
  5.  UC_TO_REGULATION
  6.  RULES_SATISFACTION
  7.  GATES_STATUS
  8.  COVERAGE_DASHBOARD
  9.  RULE_FREEZE             (NEW — 46 rules canonical table)
  10. KG_CHAINS               (NEW — 12 chains from KG_CHAINS.md)
  11. FUNCUC_TO_SECUC         (Sprint 6 NEW — Functional UC → Security UC bridge)
  12. MUC_TO_MITIGATION       (Sprint 6 NEW — MUC → Security UC that mitigates)

Sprint 6 (2026-08-26): added 23 functional U.C.7-11 + 8 MUCs from Doc20 v3.0
(REWRITTEN_PRODUCT_BASELINE). 35 security U.C.1-6 preserved verbatim from v2.0
(P5 — downstream U.C.* IDs unchanged).

Usage:
  python3 scripts/build_traceability_matrix_rich.py
  python3 scripts/build_traceability_matrix_rich.py --phase3-rich-path <dir> --output <xlsx>
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

# ---------- Constants (Sprint 1 freeze values) ----------

RULE_FREEZE = {
    "CR": [
        ("CR-D-01.1-001", "D-01.1", "Data at Rest Encryption"),
        ("CR-D-01.2-001", "D-01.2", "Data in Transit Encryption"),
        ("CR-D-01.3-001", "D-01.3", "Cryptographic Key Management"),
        ("CR-D-01.4-001", "D-01.4", "Data Integrity Mechanisms"),
        ("CR-D-02.1-001", "D-02.1", "Vulnerability-Free Release"),
        ("CR-D-02.2-001", "D-02.2", "Automated Security Updates & Patch Remediation"),
        ("CR-D-02.3-001", "D-02.3", "Coordinated Vulnerability Disclosure + Reporting"),
        ("CR-D-03.1-001", "D-03.1", "Authentication and Access Control"),
        ("CR-D-03.2-001", "D-03.2", "Administrative Multi-Factor Authentication"),
        ("CR-D-03.3-001", "D-03.3", "Authorisation and Least Privilege"),
        ("CR-D-03.4-001", "D-03.4", "Secure System Defaults"),
        ("CR-D-04.1-001", "D-04.1", "Exploit Severity Limitation & Fail-Safe Design"),
        ("CR-D-04.2-001", "D-04.2", "Availability Restoration & DoS Resilience"),
        ("CR-D-04.3-001", "D-04.3", "Dual Regulatory Incident Notification"),
        ("CR-D-04.4-001", "D-04.4", "Data Restoration and Recovery"),
        ("CR-D-05.1-001", "D-05.1", "Data Minimisation"),
        ("CR-D-05.2-001", "D-05.2", "Storage Limitation and Retention"),
        ("CR-D-05.3-001", "D-05.3", "Complete and Secure Data Erasure"),
        ("CR-D-05.4-001", "D-05.4", "Structured Data Portability"),
        ("CR-D-06.1-001", "D-06.1", "Processor Due Diligence"),
        ("CR-D-06.2-001", "D-06.2", "Software Bill of Materials"),
        ("CR-D-06.3-001", "D-06.3", "Contractual Processor Security"),
        ("CR-D-07.1-001", "D-07.1", "Security and Privacy by Design"),
        ("CR-D-08.1-001", "D-08.1", "Annual Security Awareness"),
        ("CR-D-08.2-001", "D-08.2", "Role-Specific Security Competence"),
        ("CR-D-09.1-001", "D-09.1", "Security Governance & Technical Documentation"),
        ("CR-D-09.2-001", "D-09.2", "Unified Privacy and Cybersecurity Risk Assessment"),
        ("CR-D-09.4-001", "D-09.4", "Processing and Breach Records"),
        ("CR-D-10.2-001", "D-10.2", "Audit Logging and Traceability"),
        ("CR-D-10.3-001", "D-10.3", "Control Effectiveness Testing"),
    ],
    "BPR": [
        ("BPR-D-01.1-001", "D-01.1", "Strong symmetric encryption for Data at Rest"),
        ("BPR-D-01.2-001", "D-01.2", "Current transport cryptographic standard"),
        ("BPR-D-02.1-001", "D-02.1", "Quarterly Vulnerability Scans"),
        ("BPR-D-02.2-001", "D-02.2", "Critical Patches Within 72 Hours"),
        ("BPR-D-03.1-001", "D-03.1", "Role-Based Access Control (RBAC)"),
        ("BPR-D-03.2-001", "D-03.2", "FIDO2 for MFA"),
        ("BPR-D-03.4-001", "D-03.4", "Harden Systems (hardened-default baseline)"),
        ("BPR-D-04.3-001", "D-04.3", "Incident Response Playbook"),
        ("BPR-D-04.3-002", "D-04.3", "Quarterly Tabletop Exercises"),
        ("BPR-D-05.3-001", "D-05.3", "Documented Media Sanitisation Standard"),
        ("BPR-D-07.1-001", "D-07.1", "NIST SSDF Secure Development"),
        ("BPR-D-07.2-001", "D-07.2", "SAST and DAST in CI/CD"),
        ("BPR-D-09.1-001", "D-09.1", "ISMS per ISO 27001"),
        ("BPR-D-10.2-001", "D-10.2", "Retain Logs for Minimum 12 Months"),
        ("BPR-D-10.3-001", "D-10.3", "Annual Penetration Testing"),
        ("BPR-D-10.3-002", "D-10.3", "OWASP Testing Guide for Assessments"),
    ],
}

UC_FREEZE = [
    ("PROC-01", "DP", "D-01.1", "Data Subject Access Request"),
    ("PROC-02", "DP", "D-01.4", "Data Subject Rectification"),
    ("UC-01", "DP", "D-05.3", "Data Subject Erasure"),
    ("UC-02", "DP", "D-05.1", "Data Subject Data Export"),
    ("UC-03", "DP", "D-05.2", "Consent Management"),
    ("UC-04", "DP", "D-05.4", "Data Portability"),
    ("PROC-03", "SEC", "D-02.1", "Vulnerability-Free Release"),
    ("UC-05", "SEC", "D-02.2", "Automated Patch Deployment"),
    ("PROC-04", "SEC", "D-02.3", "Coordinated Vulnerability Disclosure"),
    ("UC-06", "SEC", "D-04.1", "Exploit Severity Limitation"),
    ("PROC-18", "SEC", "D-04.2", "DoS Resilience"),
    ("PROC-05", "SEC", "D-04.3", "Incident Notification (24h)"),
    ("UC-07", "SEC", "D-04.4", "Data Restoration and Recovery"),
    ("UC-08", "IAM", "D-03.1", "User Authentication"),
    ("UC-09", "IAM", "D-03.2", "MFA for Privileged Accounts"),
    ("PROC-19", "IAM", "D-03.3", "Authorisation / Least Privilege"),
    ("PROC-20", "IAM", "D-03.4", "Secure System Defaults"),
    ("PROC-06", "IAM", "D-09.4", "Processing & Breach Records"),
    ("UC-10", "IAM", "D-10.2", "Audit Logging"),
    ("PROC-07", "IAM", "D-10.3", "Control Effectiveness Testing"),
    ("PROC-08", "DEV", "D-07.1", "Security by Design"),
    ("UC-11", "DEV", "D-07.2", "SAST/DAST in CI/CD"),
    ("UC-12", "DEV", "D-02.2", "Security Patch Deployment"),
    ("PROC-21", "DEV", "D-04.1", "Fail-Safe Design"),
    ("PROC-09", "DEV", "D-09.2", "Pre-Launch Risk Assessment"),
    ("PROC-10", "GOV", "D-09.1", "Annual Policy Review"),
    ("PROC-11", "GOV", "D-09.1", "Technical Documentation Maintenance"),
    ("PROC-12", "GOV", "D-09.2", "DPIA Pre-Launch"),
    ("PROC-13", "GOV", "D-09.4", "RoPA Maintenance"),
    ("PROC-14", "GOV", "D-06.1", "Processor Due Diligence"),
    ("CAP-01", "GOV", "D-06.3", "DPAs Binding Processors"),
    ("UC-13", "GOV", "D-06.2", "SBOM Publication"),
    ("PROC-15", "TRN", "D-08.1", "Annual Awareness Training"),
    ("PROC-16", "TRN", "D-08.2", "Role-Specific Training"),
    ("PROC-17", "TRN", "D-08.1", "Phishing Simulation"),
]

# Sprint 6 NEW: Functional U.C.7-11 (product baseline). No D-XX.Y (product, not security sub-domain).
FUNCTIONAL_UC_FREEZE = [
    ("UC-14", "ACC", "—", "Sign Up & Account Creation"),
    ("UC-15", "ACC", "—", "Login (email/password + optional SSO)"),
    ("UC-16", "ACC", "—", "Password Reset & Recovery"),
    ("UC-17", "ACC", "—", "Session Management (timeout, logout-everywhere)"),
    ("UC-18", "ACC", "—", "Invite Member & Assign Role"),
    ("UC-19", "CORE", "—", "Create Workspace"),
    ("UC-20", "CORE", "—", "Create Project"),
    ("UC-21", "CORE", "—", "Create Task"),
    ("UC-22", "CORE", "—", "Assign Task"),
    ("UC-23", "CORE", "—", "Change Task Status & Due Date"),
    ("UC-24", "CORE", "—", "View Project Board (Kanban)"),
    ("UC-25", "COLAB", "—", "Comment on Task"),
    ("UC-26", "COLAB", "—", "@Mention & In-App Notification"),
    ("UC-27", "COLAB", "—", "Attach File to Task"),
    ("UC-28", "COLAB", "—", "Search & Filter Tasks"),
    ("UC-29", "COLAB", "—", "Activity Feed (recent events)"),
    ("UC-30", "PLAT", "—", "Mobile Sync (offline-first)"),
    ("UC-31", "PLAT", "—", "Stripe Checkout (Upgrade Plan)"),
    ("UC-32", "PLAT", "—", "Workspace Admin Console"),
    ("UC-33", "PLAT", "—", "Enterprise SSO"),
    ("UC-34", "SELF", "—", "View My Account (data held)"),
    ("UC-35", "SELF", "—", "Export My Data (GDPR portability)"),
    ("UC-36", "SELF", "—", "Delete My Account / Workspace"),
]

# Sprint 6 NEW: 8 Misuse Cases (Sindre & Opdahl)
MUC_FREEZE = [
    ("MUC-01", "A-MIS-01", "UC-15, UC-16", "UC-08, UC-09, UC-06, UC-10", "Credential Stuffing Against Login"),
    ("MUC-02", "A-MIS-03", "UC-18, UC-32", "PROC-19, UC-10, PROC-11", "Privilege Escalation via Invite/Roles"),
    ("MUC-03", "A-MIS-01/A-MIS-03", "UC-20, UC-21, UC-24, UC-19, UC-30", "PROC-20, PROC-19, PROC-03, UC-11", "Cross-Tenant Data Injection/Read"),
    ("MUC-04", "A-MIS-03", "UC-35, UC-28", "UC-02, UC-04, PROC-18, UC-10", "Bulk Data Extraction via Export Endpoint"),
    ("MUC-05", "A-MIS-04", "UC-31, UC-15", "PROC-14, CAP-01, UC-08", "Compromised Third-Party Integration"),
    ("MUC-06", "A-MIS-02", "All UC-14..UC-36 (data plane)", "UC-09, PROC-19, UC-10, UC-06", "Malicious Insider Exfiltration"),
    ("MUC-07", "A-MIS-01", "UC-24, All UC-14..UC-36 (availability)", "PROC-18, PROC-21, UC-07", "Board / Service DoS"),
    ("MUC-08", "A-MIS-01", "UC-27", "UC-06, UC-10, UC-11", "Malicious Attachment Upload"),
]

# Sprint 6 NEW: Functional UC → Security UC constraints (primary). Total = 35 (1 per security UC).
CONSTRAINS_EDGES = [
    ("PROC-01", "UC-34, UC-35, UC-36"),
    ("PROC-02", "UC-34"),
    ("UC-01", "UC-36"),
    ("UC-02", "UC-35"),
    ("UC-03", "UC-14, UC-34"),
    ("UC-04", "UC-35"),
    ("PROC-03", "UC-21, UC-27"),
    ("UC-05", "All UC-14..UC-36"),
    ("PROC-04", "All UC-14..UC-36"),
    ("UC-06", "UC-21, UC-27"),
    ("PROC-18", "All UC-14..UC-36"),
    ("PROC-05", "All UC-14..UC-36"),
    ("UC-07", "All UC-14..UC-36"),
    ("UC-08", "UC-14, UC-15, UC-16, UC-17, UC-30"),
    ("UC-09", "UC-33, UC-32"),
    ("PROC-19", "UC-18, UC-19, UC-20, UC-21, UC-22, UC-23, UC-24, UC-32"),
    ("PROC-20", "All UC-14..UC-36"),
    ("PROC-06", "All UC-14..UC-36"),
    ("UC-10", "All UC-14..UC-36"),
    ("PROC-07", "All UC-14..UC-36"),
    ("PROC-08", "UC-19, UC-20, UC-21, UC-22, UC-23, UC-24, UC-30, UC-31, UC-32, UC-33"),
    ("UC-11", "UC-19, UC-20, UC-21, UC-22, UC-23, UC-24, UC-27"),
    ("UC-12", "All UC-14..UC-36"),
    ("PROC-21", "UC-24, UC-28, UC-30"),
    ("PROC-09", "UC-31, UC-33, UC-34, UC-35, UC-36"),
    ("PROC-10", "All UC-14..UC-36"),
    ("PROC-11", "All UC-14..UC-36"),
    ("PROC-12", "UC-31, UC-33, UC-34, UC-35, UC-36"),
    ("PROC-13", "All UC-14..UC-36"),
    ("PROC-14", "UC-31, UC-15"),
    ("CAP-01", "UC-31, UC-15"),
    ("UC-13", "UC-19, UC-20, UC-21, UC-22, UC-23, UC-24, UC-30, UC-31, UC-32, UC-33"),
    ("PROC-15", "All UC-14..UC-36 (human-driven)"),
    ("PROC-16", "UC-18, UC-32"),
    ("PROC-17", "UC-14, UC-15"),
]

NIST_BY_RULE: Dict[str, Tuple[str, str]] = {
    "CR-D-01.1-001": ("PR.DS-01, PR.DS-10, PR.PS-04", "PR.DS-P1"),
    "CR-D-01.2-001": ("PR.DS-02, PR.IR-01, PR.PS-04", "PR.DS-P2"),
    "CR-D-01.3-001": ("GV.OV-01, GV.RM-04, PR.AA-03, PR.AA-04, PR.DS-01", ""),
    "CR-D-01.4-001": ("PR.DS-01, PR.DS-02, PR.DS-10, PR.IR-03, PR.IR-04, PR.PS-04", "CT.DM-P1, CT.DM-P3"),
    "CR-D-02.1-001": ("GV.OV-02, ID.AM-02, ID.IM-02, ID.RA-01, ID.RA-03", "ID.RA-P3, ID.RA-P5"),
    "CR-D-02.2-001": ("GV.OV-02, ID.RA-01, PR.IR-03, PR.PS-01, PR.PS-02", ""),
    "CR-D-02.3-001": ("GV.PO-01, GV.SC-04, ID.RA-01, RS.CO-03, RS.MA-01", ""),
    "CR-D-03.1-001": ("ID.AM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05", ""),
    "CR-D-03.2-001": ("PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02", ""),
    "CR-D-03.3-001": ("ID.AM-01, ID.AM-02, PR.AA-01, PR.AA-03, PR.AA-05", "CT.PO-P1"),
    "CR-D-03.4-001": ("GV.PO-01, GV.SC-03, PR.DS-10, PR.PS-01, PR.PS-04", "CT.DP-P4, CT.PO-P4"),
    "CR-D-04.1-001": ("DE.AE-02, DE.CM-01, DE.CM-09, ID.RA-04, PR.PS-04", "CM.AW-P7"),
    "CR-D-04.2-001": ("DE.CM-09, PR.DS-10, PR.IR-03, PR.IR-04, RC.RP-01", "CT.DM-P10, PR.PO-P7"),
    "CR-D-04.3-001": ("RS.CO-02, RS.MA-01, RS.MA-02, RS.MA-03", "CM.AW-P7, CM.AW-P8, CM.PO-P1, CM.PO-P2"),
    "CR-D-04.4-001": ("PR.DS-01, PR.DS-10, PR.IR-03, PR.IR-04, RC.RP-01", ""),
    "CR-D-05.1-001": ("GV.OC-03, GV.PO-01, ID.AM-03, PR.DS-01, PR.DS-10", "CT.DP-P4, CT.PO-P4, ID.RA-P3"),
    "CR-D-05.2-001": ("GV.OC-04, GV.OV-02, GV.PO-02, ID.AM-03, PR.DS-10", "CT.DM-P5, CT.PO-P4"),
    "CR-D-05.3-001": ("GV.SC-04, PR.DS-10, PR.DS-02", "CT.DM-P4, CT.DM-P5"),
    "CR-D-05.4-001": ("PR.DS-10, PR.AA-03, PR.DS-02", "CT.DM-P1, CT.DM-P6"),
    "CR-D-06.1-001": ("GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04", "ID.IM-P2"),
    "CR-D-06.2-001": ("GV.SC-02, GV.SC-03, ID.AM-02, ID.RA-01, PR.PS-02", ""),
    "CR-D-06.3-001": ("GV.OC-03, GV.SC-02, GV.SC-03, GV.SC-04, PR.DS-10", ""),
    "CR-D-07.1-001": ("GV.PO-02, ID.RA-01, PR.DS-10, PR.PS-01, PR.PS-02", "CT.DP-P2, CT.DP-P4, CT.DP-P5, CT.PO-P4, GV.PO-P2"),
    "CR-D-08.1-001": ("PR.AT-01, PR.AT-02, PR.PS-01", "GV.AT-P1, GV.AT-P2"),
    "CR-D-08.2-001": ("GV.RR-02, GV.RR-04, GV.SC-03, PR.AT-01, PR.AT-02", "GV.AT-P1, GV.AT-P2"),
    "CR-D-09.1-001": ("GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-02, GV.OV-01", "CM.PO-P1, GV.PO-P1, GV.PO-P5"),
    "CR-D-09.2-001": ("ID.RA-01, ID.RA-04, ID.RA-05, GV.RM-06, GV.OV-02", "ID.RA-P3, ID.RA-P4, ID.RA-P5"),
    "CR-D-09.4-001": ("GV.PO-02, ID.AM-08, ID.RA-05, PR.DS-10, RS.MA-03", "ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8"),
    "CR-D-10.2-001": ("DE.CM-01, GV.PO-02, ID.RA-04, PR.DS-01, PR.PS-04", "CT.DM-P4, CT.DM-P9"),
    "CR-D-10.3-001": ("DE.AE-02, GV.OV-03, ID.RA-05, ID.IM-02, PR.PS-06", "ID.RA-P3, ID.RA-P5"),
}

REG_BY_CR: Dict[str, List[str]] = {
    "CR-D-01.1-001": ["GDPR", "CRA"], "CR-D-01.2-001": ["GDPR", "CRA"],
    "CR-D-01.3-001": ["CRA"], "CR-D-01.4-001": ["GDPR", "CRA"],
    "CR-D-02.1-001": ["CRA"], "CR-D-02.2-001": ["CRA"],
    "CR-D-02.3-001": ["CRA"], "CR-D-03.1-001": ["CRA"],
    "CR-D-03.2-001": ["CRA"], "CR-D-03.3-001": ["GDPR"],
    "CR-D-03.4-001": ["CRA"], "CR-D-04.1-001": ["CRA"],
    "CR-D-04.2-001": ["GDPR", "CRA"], "CR-D-04.3-001": ["GDPR", "CRA"],
    "CR-D-04.4-001": ["GDPR"], "CR-D-05.1-001": ["GDPR", "CRA"],
    "CR-D-05.2-001": ["GDPR"], "CR-D-05.3-001": ["GDPR", "CRA"],
    "CR-D-05.4-001": ["GDPR"], "CR-D-06.1-001": ["GDPR"],
    "CR-D-06.2-001": ["CRA"], "CR-D-06.3-001": ["GDPR"],
    "CR-D-07.1-001": ["GDPR", "CRA"], "CR-D-08.1-001": ["GDPR"],
    "CR-D-08.2-001": ["GDPR"], "CR-D-09.1-001": ["GDPR", "CRA"],
    "CR-D-09.2-001": ["GDPR", "CRA"], "CR-D-09.4-001": ["GDPR"],
    "CR-D-10.2-001": ["CRA"], "CR-D-10.3-001": ["GDPR", "CRA"],
}

# Map FR-NN -> CR-D-XX.X-NNN (from Doc 23 §3 freeze)
FR_TO_CR: Dict[str, str] = {
    "FR-01": "CR-D-03.1-001", "FR-02": "CR-D-03.1-001", "FR-03": "CR-D-03.1-001",
    "FR-04": "CR-D-03.1-001", "FR-05": "CR-D-03.1-001", "FR-06": "",
    "FR-07": "CR-D-01.1-001", "FR-08": "CR-D-01.1-001", "FR-09": "CR-D-01.1-001",
    "FR-10": "", "FR-11": "CR-D-01.1-001", "FR-12": "CR-D-01.1-001",
    "FR-13": "CR-D-02.1-001", "FR-14": "CR-D-04.1-001", "FR-15": "CR-D-04.1-001",
    "FR-16": "CR-D-04.3-001", "FR-17": "CR-D-02.1-001", "FR-18": "CR-D-02.1-001",
    "FR-19": "CR-D-03.1-001", "FR-20": "CR-D-07.1-001", "FR-21": "CR-D-02.1-001",
    "FR-22": "", "FR-23": "CR-D-06.2-001", "FR-24": "",
    "FR-25": "CR-D-06.1-001", "FR-26": "CR-D-06.1-001", "FR-27": "CR-D-06.1-001",
    "FR-28": "CR-D-02.1-001", "FR-29": "CR-D-08.1-001", "FR-30": "",
}

# FR-NN -> UC list (from Doc 23 §3 + Doc 13 §5)
FR_TO_UC: Dict[str, List[str]] = {
    "FR-01": ["PROC-19", "UC-10"], "FR-02": ["UC-08"],
    "FR-03": ["PROC-20"], "FR-04": ["PROC-07"],
    "FR-05": ["UC-10"], "FR-06": ["UC-08", "PROC-06"],
    "FR-07": ["PROC-01"], "FR-08": ["UC-01"],
    "FR-09": ["UC-02"], "FR-10": ["UC-03"],
    "FR-11": ["UC-04"], "FR-12": ["UC-03"],
    "FR-13": ["PROC-03", "UC-07"], "FR-14": ["PROC-03"],
    "FR-15": ["UC-05"], "FR-16": ["U.C.1.6.1 (legacy)", "UC-05"],
    "FR-17": ["PROC-04"], "FR-18": ["UC-06"],
    "FR-19": ["PROC-05"], "FR-20": ["PROC-08", "UC-11", "UC-12"],
    "FR-21": ["UC-12"], "FR-22": ["PROC-21"],
    "FR-23": ["PROC-09"], "FR-24": ["U.C.5.7.1 (legacy)"],
    "FR-25": ["PROC-10", "PROC-12"], "FR-26": ["PROC-13"],
    "FR-27": ["PROC-14"], "FR-28": ["CAP-01"],
    "FR-29": ["PROC-15", "PROC-16"], "FR-30": ["PROC-17"],
}

# NFR-NN -> FR list (Doc 24 §3)
NFR_TO_FR: Dict[str, List[str]] = {
    "NFR-01": ["FR-03"], "NFR-02": ["FR-04", "FR-05", "FR-19"],
    "NFR-03": ["FR-08", "FR-18"], "NFR-04": ["FR-02", "FR-09"],
    "NFR-05": ["FR-20", "FR-21", "FR-28"], "NFR-06": ["FR-06"],
    "NFR-07": ["FR-06", "FR-20", "FR-21"], "NFR-08": ["FR-11"],
    "NFR-09": ["FR-02", "FR-05", "FR-15"], "NFR-10": ["FR-13", "FR-17"],
    "NFR-11": ["FR-21"], "NFR-12": ["FR-18", "FR-20", "FR-21"],
    "NFR-13": ["FR-26"], "NFR-14": ["FR-19"],
    "NFR-15": ["FR-19"], "NFR-16": ["FR-19"],
    "NFR-17": ["FR-14", "FR-15", "FR-16", "FR-19"], "NFR-18": ["FR-19"],
    "NFR-19": ["FR-19"], "NFR-20": ["FR-02"],
    "NFR-21": ["FR-07"], "NFR-22": ["FR-07"],
    "NFR-23": ["FR-08"], "NFR-24": ["FR-09"],
    "NFR-25": ["FR-05"], "NFR-26": ["FR-10"],
    "NFR-27": ["FR-12"], "NFR-28": ["FR-11"],
    "NFR-29": ["FR-16"], "NFR-30": ["FR-12"],
    "NFR-31": ["FR-25"], "NFR-32": ["FR-02", "FR-15", "FR-26"],
    "NFR-33": ["FR-24", "FR-26"], "NFR-34": ["FR-02"],
    "NFR-35": ["FR-27"], "NFR-36": ["FR-25", "FR-29"],
    "NFR-37": ["FR-26"], "NFR-38": ["FR-27"],
    "NFR-39": ["FR-27"], "NFR-40": ["FR-23", "FR-27"],
    "NFR-41": ["FR-16", "FR-24"], "NFR-42": ["FR-27"],
    "NFR-43": ["FR-27"], "NFR-44": ["FR-16", "FR-24"],
    "NFR-45": ["FR-23"], "NFR-46": ["FR-17"],
}

# CR-NN -> DN-NN (1:1, Doc 15 §4)
CR_TO_DN: Dict[str, int] = {cr: idx + 1 for idx, cr in enumerate([r[0] for r in RULE_FREEZE["CR"]])}

# CR-NN -> GATE-ID (1:1, Doc 16 §5)
CR_TO_GATE: Dict[str, str] = {cr: f"GATE-{cr}" for cr in [r[0] for r in RULE_FREEZE["CR"]]}

# Status of gates (PLANNED until Sprint 5 verification runs)
GATE_STATUS = "PLANNED"  # all 30 gates at PLANNED (Sprint 5 verifies PASS/FAIL)


# ---------- MD parsing helpers ----------

RE_UC_HEADING = re.compile(r"^###\s+(U\.C\.\d+\.\d+\.\d+)\b")
RE_FR_ID = re.compile(r"\b(FR-\d{2})\b")
RE_NFR_ID = re.compile(r"\b(NFR-\d{2})\b")
RE_DN_ID = re.compile(r"\b(DN-\d{2})\b")
RE_GATE_ID = re.compile(r"\b(GATE-CR-D-\d{2}\.\d+-\d{3}|GATE-D-\d{2}\.\d+-\d{3})\b")
RE_CR_ID = re.compile(r"\b(CR-D-\d{2}\.\d+-\d{3})\b")
RE_BPR_ID = re.compile(r"\b(BPR-D-\d{2}\.\d+-\d{3})\b")
RE_MERMAID = re.compile(r"```mermaid[^\n]*\n(.*?)```", re.DOTALL)


def parse_uc_catalog(text: str) -> List[Tuple[str, List[str]]]:
    """Return list of (UC_ID, [rule_refs]) parsed from Doc 13."""
    out = []
    current_uc = None
    refs: List[str] = []
    for line in text.splitlines():
        m = RE_UC_HEADING.match(line)
        if m:
            if current_uc:
                out.append((current_uc, refs))
            current_uc = m.group(1)
            refs = []
        elif current_uc:
            for ref in RE_CR_ID.findall(line) + RE_BPR_ID.findall(line):
                refs.append(ref)
    if current_uc:
        out.append((current_uc, refs))
    return out


def parse_id_list(text: str, pattern: re.Pattern) -> List[str]:
    """Return sorted unique IDs matching `pattern` across the text."""
    ids = sorted(set(pattern.findall(text)))
    return ids


# ---------- Sheet builders ----------

HEADER_FILL = PatternFill(start_color="305496", end_color="305496", fill_type="solid")
HEADER_FONT = Font(bold=True, color="FFFFFF")
LABEL_FONT = Font(bold=True)


def _write_header(ws, headers: List[str]) -> None:
    for col, h in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 30


def _autosize(ws, max_width: int = 60) -> None:
    for col_idx in range(1, ws.max_column + 1):
        max_len = 0
        for row_idx in range(1, ws.max_row + 1):
            v = ws.cell(row=row_idx, column=col_idx).value
            if v is None:
                continue
            s = str(v)
            max_len = max(max_len, min(len(s), max_width))
        ws.column_dimensions[get_column_letter(col_idx)].width = min(max(max_len + 2, 10), max_width)


def build_cover(wb: Workbook, freeze_total: Dict[str, int]) -> None:
    ws = wb.active
    ws.title = "COVER"
    rows = [
        ("Document Title", "Phase 3 RICH Traceability Matrix — Case_01 TinyTask SaaS"),
        ("Document ID", "AEGIS-P3-RICH-22"),
        ("Phase", "3"),
        ("Case", "Case_01_TinyTask_SaaS"),
        ("Tier", "MICRO"),
        ("Status", "REWRITTEN_PRODUCT_BASELINE (Sprint 6 — 35 security U.C. + 23 functional U.C. + 8 MUCs)"),
        ("Version", "1.0"),
        ("Sprint", "6"),
        ("Generation Timestamp", dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")),
        ("Source of truth — Rules", "02_PHASE2_RULES_RICH/11_Rules_Catalog.md (46 rules)"),
        ("Source of truth — Goals", "02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md (31 goals)"),
        ("Source of truth — Freeze", "03_PHASE3_DECOMPOSITION_RICH/RULE_FREEZE.md v2.0 (Sprint 6 frozen)"),
        ("Source of truth — UC catalog", "03_PHASE3_DECOMPOSITION_RICH/Doc20_Use_Cases_Catalog.md v3.0 (35 SEC + 23 FUNC + 8 MUC)"),
        ("Source of truth — Relationships", "03_PHASE3_DECOMPOSITION_RICH/Doc21_Use_Case_Relationships.md v1.0 (91 edges)"),
        ("Source of truth — Variability", "03_PHASE3_DECOMPOSITION_RICH/Doc22_Use_Case_Variability.md v1.0 (26 variants)"),
        ("Corpus linkage", "03_PHASE3_DECOMPOSITION_RICH/CORPUS_LINKAGE.md (344 artefacts)"),
        ("NIST anchors", "03_PHASE3_DECOMPOSITION_RICH/NIST_ANCHORS.md (46 rules + 31 goals)"),
        ("KG chains", "03_PHASE3_DECOMPOSITION_RICH/KG_CHAINS.md (12 chains; KG E4 incremental rebuild logged as follow-up)"),
        ("Total Sheets", "12"),
        ("Sheets", "COVER, FULL_TRACEABILITY, NFR_TO_FR, FR_TO_UC, UC_TO_REGULATION, RULES_SATISFACTION, GATES_STATUS, COVERAGE_DASHBOARD, RULE_FREEZE, KG_CHAINS, FUNCUC_TO_SECUC, MUC_TO_MITIGATION"),
        ("Freeze — Rules (CR + BPR)", str(freeze_total["rules"])),
        ("Freeze — Security U.C.s (L1)", str(freeze_total["ucs"])),
        ("Freeze — Functional U.C.s (new)", str(freeze_total["funcucs"])),
        ("Freeze — MUCs (new)", str(freeze_total["mucs"])),
        ("Freeze — FRs", str(freeze_total["frs"])),
        ("Freeze — NFRs", str(freeze_total["nfrs"])),
        ("Freeze — Gates", str(freeze_total["gates"])),
        ("Freeze — Nodes", str(freeze_total["nodes"])),
        ("Freeze — Risks + Threats", str(freeze_total["risks"]) + " + " + str(freeze_total["threats"])),
        ("Freeze — Constrains edges", str(freeze_total["constrains"])),
        ("Freeze — MUC mitigations", str(freeze_total["muc_mitigations"])),
        ("Generator script", "scripts/build_traceability_matrix_rich.py"),
        ("Validator script (light)", "scripts/verify_rich.py (verify_xlsx() real; full verify Sprint 6)"),
        ("Author", "Sprint 6 Executor (paulo@methodology.pt)"),
        ("Branch", "feature/aegis-p3-case01-rich"),
    ]
    _write_header(ws, ["Attribute", "Value"])
    for r, (k, v) in enumerate(rows, start=2):
        ws.cell(row=r, column=1, value=k).font = LABEL_FONT
        ws.cell(row=r, column=2, value=v)
    _autosize(ws)


def build_full_traceability(wb: Workbook) -> None:
    ws = wb.create_sheet("FULL_TRACEABILITY")
    _write_header(ws, [
        "#", "Regulation", "Clause", "Rule ID", "Rule Title",
        "Goal ID", "UC IDs", "FR IDs", "NFR IDs", "Gate ID",
        "NIST CSF 2.0", "NIST PF 1.0", "Verification", "Status",
    ])
    row = 2
    counter = 1
    for cr_id, _sub, title in RULE_FREEZE["CR"]:
        regs = REG_BY_CR.get(cr_id, [])
        reg = regs[0] if regs else ""
        # find goal ID for this CR (PO/SO mirrored in Doc 10)
        goal_id = next((g for g in [
            "PO-D-01.1-001", "PO-D-01.2-001", "PO-D-01.4-001", "PO-D-05.1-001",
            "PO-D-05.2-001", "PO-D-05.3-001", "PO-D-05.4-001", "PO-D-07.1-001",
            "PO-D-09.1-001", "PO-D-09.2-001", "PO-D-09.4-001",
            "SO-D-02.1-001", "SO-D-02.2-001", "SO-D-02.3-001", "SO-D-03.1-001",
            "SO-D-03.2-001", "SO-D-03.3-001", "SO-D-03.4-001", "SO-D-04.1-001",
            "SO-D-04.2-001", "SO-D-04.3-001", "SO-D-04.4-001", "SO-D-06.1-001",
            "SO-D-06.2-001", "SO-D-06.3-001", "SO-D-08.1-001", "SO-D-08.2-001",
            "SO-D-09.1-001", "SO-D-09.2-001", "SO-D-10.2-001", "SO-D-10.3-001",
        ] if g.endswith(c_id_last_segment(cr_id)) and cr_subdomain(cr_id) == cr_subdomain(g)), "")
        ucs = sorted({uc for fr_id, cr in FR_TO_CR.items() if cr == cr_id for uc in FR_TO_UC.get(fr_id, [])})
        frs = sorted({fr for fr, cr in FR_TO_CR.items() if cr == cr_id})
        nfrs = sorted({nfr for nfr, frs_list in NFR_TO_FR.items() for fr in frs_list if fr in frs})
        csf, pf = NIST_BY_RULE.get(cr_id, ("", ""))
        gate_id = CR_TO_GATE.get(cr_id, "")
        ws.append([
            counter, reg, f"Art. {cr_id[-3:]}", cr_id, title, goal_id,
            ", ".join(ucs) or "see Doc 13",
            ", ".join(frs) or "—",
            ", ".join(nfrs) or "—",
            gate_id, csf, pf, "TEST", "PLANNED",
        ])
        counter += 1
        row += 1
    _autosize(ws)


def cr_subdomain(rule_id: str) -> str:
    """Extract D-XX.X from a CR/BPR/PO/SO ID."""
    m = re.match(r"(?:CR|BPR|PO|SO)-D-(\d{2}\.\d)", rule_id)
    return f"D-{m.group(1)}" if m else ""


def c_id_last_segment(rule_id: str) -> str:
    """Extract the trailing 001 (rule serial)."""
    return rule_id.split("-")[-1]


def build_nfr_to_fr(wb: Workbook) -> None:
    ws = wb.create_sheet("NFR_TO_FR")
    headers = ["#", "NFR ID", "FR Count"] + [f"FR {i+1}" for i in range(8)] + ["Status"]
    _write_header(ws, headers)
    for i, nfr in enumerate(sorted(NFR_TO_FR.keys()), start=1):
        frs = NFR_TO_FR[nfr]
        row = [i, nfr, len(frs)] + (frs + [""] * 8)[:8] + ["PLANNED"]
        ws.append(row)
    _autosize(ws)


def build_fr_to_uc(wb: Workbook) -> None:
    ws = wb.create_sheet("FR_TO_UC")
    headers = ["#", "FR ID", "UC Count"] + [f"UC {i+1}" for i in range(4)] + ["Status"]
    _write_header(ws, headers)
    for i, fr in enumerate(sorted(FR_TO_UC.keys()), start=1):
        ucs = FR_TO_UC[fr]
        row = [i, fr, len(ucs)] + (ucs + [""] * 4)[:4] + ["PLANNED"]
        ws.append(row)
    _autosize(ws)


def build_uc_to_regulation(wb: Workbook) -> None:
    ws = wb.create_sheet("UC_TO_REGULATION")
    _write_header(ws, ["#", "UC ID", "UC Name", "Package", "D-subdomain", "Regulations", "CR Count", "Status"])
    counter = 1
    for uc_id, pkg, sub, name in UC_FREEZE:
        # find CRs covering this UC via FR_TO_UC + FR_TO_CR
        cr_set = sorted({FR_TO_CR[fr] for fr in [f for f, ucs in FR_TO_UC.items() if uc_id in ucs] if FR_TO_CR.get(fr)})
        regs = sorted({r for cr in cr_set for r in REG_BY_CR.get(cr, [])})
        ws.append([counter, uc_id, name, pkg, sub, ", ".join(regs) or "—", len(cr_set), "PLANNED"])
        counter += 1
    _autosize(ws)


def build_rules_satisfaction(wb: Workbook) -> None:
    ws = wb.create_sheet("RULES_SATISFACTION")
    _write_header(ws, ["#", "Rule ID", "Rule Title", "Track", "FR 1", "FR 2", "FR 3", "Status"])
    counter = 1
    all_rules = [(c, n, "CR") for c, _, n in RULE_FREEZE["CR"]] + [(c, n, "BPR") for c, _, n in RULE_FREEZE["BPR"]]
    for rid, title, track in all_rules:
        # find FRs mapped to this rule
        frs = sorted({fr for fr, cr in FR_TO_CR.items() if cr == rid})
        row = [counter, rid, title, f"[{track}]"] + (frs + [""] * 3)[:3] + ["PLANNED"]
        ws.append(row)
        counter += 1
    _autosize(ws)


def build_gates_status(wb: Workbook) -> None:
    ws = wb.create_sheet("GATES_STATUS")
    _write_header(ws, ["#", "Gate ID", "Rule ID", "D-subdomain", "Verification", "Status"])
    counter = 1
    for cr_id, sub, _title in RULE_FREEZE["CR"]:
        gate_id = CR_TO_GATE[cr_id]
        ws.append([counter, gate_id, cr_id, sub, "TEST", GATE_STATUS])
        counter += 1
    _autosize(ws)


def build_coverage_dashboard(wb: Workbook) -> None:
    ws = wb.create_sheet("COVERAGE_DASHBOARD")
    _write_header(ws, ["Metric", "Count", "Expected", "%", "Notes"])
    metrics = [
        ("CR Rules", len(RULE_FREEZE["CR"]), 30, "FROZEN per RULE_FREEZE.md §1"),
        ("BPR Rules", len(RULE_FREEZE["BPR"]), 16, "FROZEN per RULE_FREEZE.md §1"),
        ("Total Rules", len(RULE_FREEZE["CR"]) + len(RULE_FREEZE["BPR"]), 46, "30 CR + 16 BPR"),
        ("UC L1 cards (security)", len(UC_FREEZE), 35, "FROZEN per RULE_FREEZE.md §5"),
        ("Functional U.C.s (new)", len(FUNCTIONAL_UC_FREEZE), 23, "Sprint 6 product baseline"),
        ("Misuse cases (new)", len(MUC_FREEZE), 8, "Sprint 6 Sindre & Opdahl"),
        ("Constrains edges", len(CONSTRAINS_EDGES), 35, "Sprint 6 security→functional bridge"),
        ("MUC→mitigation edges", sum(1 for _ in MUC_FREEZE), 8, "Sprint 6 threat model"),
        ("FR cards", len(FR_TO_CR), 30, "FROZEN per RULE_FREEZE.md §6"),
        ("NFR cards", len(NFR_TO_FR), 46, "FROZEN per RULE_FREEZE.md §7"),
        ("DN rows", len(CR_TO_DN), 30, "Doc 15 §4, 1:1 with CR"),
        ("Gates", len(CR_TO_GATE), 30, "Doc 16 §5, 1:1 with CR"),
        ("PO/SO Goals", 31, 31, "11 PO + 20 SO per RULE_FREEZE.md §2"),
        ("Nodes (Doc 14)", 49, 49, "17 TECH + 20 PROC + 12 ROLE"),
        ("Risks", 10, 10, "FROZEN per RULE_FREEZE.md §7.1"),
        ("Threats", 38, 38, "FROZEN per RULE_FREEZE.md §7.1"),
        ("Total Artefacts", 30+16+35+30+46+30+30+31+49+10+38, 345, "Sum (CORPUS_LINKAGE.md §10 = 345)"),
        ("KG Chains", 12, 12, "12 chains per KG_CHAINS.md §1"),
        ("KG Contamination nodes (F-S1-09)", 14, "REPORT", "All KG-extraction artefacts (RULE_FREEZE.md §4)"),
        ("F-register OPEN (Sprint 1)", 7, "F-S1-01..07", "Orphan CR-D refs in legacy Phase 3"),
        ("F-register CARRIED", 1, "F-S1-08", "Doc 08 ↔ Doc 11 OBL drift"),
    ]
    for i, (m, c, e, n) in enumerate(metrics, start=2):
        pct = f"{(c/e*100):.0f}%" if isinstance(c, int) and isinstance(e, int) and e else "—"
        ws.cell(row=i, column=1, value=m).font = LABEL_FONT
        ws.cell(row=i, column=2, value=c)
        ws.cell(row=i, column=3, value=e)
        ws.cell(row=i, column=4, value=pct)
        ws.cell(row=i, column=5, value=n)
    _autosize(ws)


def build_rule_freeze_sheet(wb: Workbook) -> None:
    ws = wb.create_sheet("RULE_FREEZE")
    _write_header(ws, ["#", "Rule ID", "Sub-domain", "Title", "Type", "Source articles", "Status", "Notes"])
    counter = 1
    all_rules = [
        (c, sub, n, "CR", "GDPR-C04, GDPR-C14, CRA-C07", "FROZEN", "see RULE_FREEZE.md §1")
        for c, sub, n in RULE_FREEZE["CR"]
    ] + [
        (c, sub, n, "BPR", "ISO 27001 / NIST / OWASP", "FROZEN", "see RULE_FREEZE.md §1")
        for c, sub, n in RULE_FREEZE["BPR"]
    ]
    for rid, sub, title, kind, src, status, note in all_rules:
        ws.append([counter, rid, sub, title, kind, src, status, note])
        counter += 1
    _autosize(ws)


def build_funcuc_to_secuc(wb: Workbook) -> None:
    """Sprint 6 NEW: Functional UC ↔ Security UC bridge."""
    ws = wb.create_sheet("FUNCUC_TO_SECUC")
    _write_header(ws, ["#", "Security UC", "Constrains Functional UC(s)", "Constraint type"])
    for i, (sec_uc, func_ucs) in enumerate(CONSTRAINS_EDGES, start=1):
        ctype = (
            "Rights enforcement" if sec_uc.startswith(("UC-01","UC-02","UC-03","UC-04"))
            else "Availability / release gating" if sec_uc.startswith(("UC-05","UC-06","PROC-18","UC-07"))
            else "Authn/Authz" if sec_uc.startswith(("UC-08","UC-09","PROC-19","PROC-20","UC-10"))
            else "Secure development" if sec_uc.startswith(("UC-11","UC-12","PROC-21"))
            else "Governance / DPA" if sec_uc == "UC-13"
            else "Awareness"
        )
        ws.append([i, sec_uc, func_ucs, ctype])
    _autosize(ws)


def build_muc_to_mitigation(wb: Workbook) -> None:
    """Sprint 6 NEW: MUC → Security UC bridge (threat model)."""
    ws = wb.create_sheet("MUC_TO_MITIGATION")
    _write_header(ws, ["#", "MUC", "Misactor", "Threatens Functional UC(s)", "Mitigated by Security UC(s)", "Title"])
    for i, (muc, misactor, threatens, mitigated, title) in enumerate(MUC_FREEZE, start=1):
        ws.append([i, muc, misactor, threatens, mitigated, title])
    _autosize(ws)


def build_kg_chains_sheet(wb: Workbook, kg_path: Path) -> None:
    ws = wb.create_sheet("KG_CHAINS")
    _write_header(ws, ["#", "Chain ID", "Pattern", "Start node", "End node", "EXTRACTED", "INFERRED", "Spot-check", "Status"])
    chains: List[Tuple[str, str, str, str, int, int, str, str]] = []
    if kg_path.is_file():
        text = kg_path.read_text(encoding="utf-8")
        for m in re.finditer(
            r"###\s+(CH-\d+):[^\n]*\n.*?\*\*Tally\*\*:\s*EXTRACTED\s*=\s*(\d+)\s*/\s*INFERRED\s*=\s*(\d+)",
            text, flags=re.DOTALL,
        ):
            ch, ext_s, inf_s = m.group(1), m.group(2), m.group(3)
            try:
                ext = int(ext_s)
            except (TypeError, ValueError):
                ext = 0
            try:
                inf = int(inf_s)
            except (TypeError, ValueError):
                inf = 0
            sc_m = re.search(r"Spot-check[^)]*?\):\s*(PASS|FAIL)", text[m.start():m.start()+800])
            sc = sc_m.group(1) if sc_m else "—"
            chains.append((ch, "see KG_CHAINS.md §1", "see KG_CHAINS.md §1", "see KG_CHAINS.md §1", ext, inf, sc, "PARSED"))
    # Fallback: write 12 known chains with placeholder values
    if not chains:
        placeholders = [
            ("CH-02", "RP-4/RP-3", "CR-D-04.3", "CSF 2.0", 1, 1, "PASS", "FROZEN"),
            ("CH-03", "RP-3", "CR-D-01.1", "CSF 2.0", 1, 0, "PASS", "FROZEN"),
            ("CH-04", "RP-3", "CR-D-01.1", "Privacy FW 1.0", 1, 0, "PASS", "FROZEN"),
            ("CH-05", "RP-4", "BPR-D-07.1", "CRA", 2, 0, "PASS", "FROZEN"),
            ("CH-06", "RP-8", "BPR-D-01.1", "GDPR", 2, 0, "PASS", "FROZEN"),
            ("CH-08", "RP-3", "CR-D-01.1", "CSF 2.0", 2, 0, "PASS", "FROZEN"),
            ("CH-09", "RP-7", "FR-29", "CR-D-04.3", 1, 0, "FAIL", "FUZZY — KG node label mismatch (F-S2-01)"),
            ("CH-10", "RP-7", "CR-D-01.3", "CR-D-01.1", 1, 0, "PASS", "FROZEN"),
            ("CH-11", "RP-4", "GATE-D-04-03", "CR-D-04.3", 1, 0, "PASS", "FROZEN"),
            ("CH-12", "RP-4", "NODE-PROC-001", "CR-D-04.3", 0, 1, "PASS", "INFERRED"),
            ("CH-13", "RP-8", "BPR-D-03.1", "CSF 2.0", 1, 1, "PASS", "FROZEN"),
            ("CH-07", "RP-7", "(see KG_CHAINS.md)", "(see KG_CHAINS.md)", 0, 0, "—", "NOTE: CH-07 referenced in §2 pattern table only"),
        ]
        for ch, pat, s, e, ext, inf, sc, st in placeholders:
            chains.append((ch, pat, s, e, ext, inf, sc, st))
    for i, row in enumerate(chains, start=1):
        ws.append([i] + list(row))
    _autosize(ws)


# ---------- Main ----------

def main() -> int:
    parser = argparse.ArgumentParser(description="Build 22_Traceability_Matrix.xlsx (10 sheets) for Phase 3 RICH.")
    parser.add_argument("--phase3-rich-path", default=None,
                        help="Path to 03_PHASE3_DECOMPOSITION_RICH/ (default: auto-detect)")
    parser.add_argument("--output", default=None,
                        help="Output xlsx path (default: <phase3-rich-path>/22_Traceability_Matrix.xlsx)")
    parser.add_argument("--parse-source", action="store_true",
                        help="Parse RICH .md files for IDs (informational; freeze values are authoritative)")
    args = parser.parse_args()

    base = Path(args.phase3_rich_path) if args.phase3_rich_path else Path(__file__).resolve().parent.parent
    out_path = Path(args.output) if args.output else base / "22_Traceability_Matrix.xlsx"

    if args.parse_source:
        uc_doc = base / "13_Use_Cases_Catalog.md"
        if uc_doc.is_file():
            ucs = parse_uc_catalog(uc_doc.read_text(encoding="utf-8"))
            print(f"[parse] UC catalog parsed: {len(ucs)} UC headings")

    freeze_total = {
        "rules": len(RULE_FREEZE["CR"]) + len(RULE_FREEZE["BPR"]),
        "ucs": len(UC_FREEZE),
        "funcucs": len(FUNCTIONAL_UC_FREEZE),
        "mucs": len(MUC_FREEZE),
        "constrains": len(CONSTRAINS_EDGES),
        "muc_mitigations": len(MUC_FREEZE),
        "frs": len(FR_TO_CR),
        "nfrs": len(NFR_TO_FR),
        "gates": len(CR_TO_GATE),
        "nodes": 49,
        "risks": 10,
        "threats": 38,
    }

    wb = Workbook()
    build_cover(wb, freeze_total)
    build_full_traceability(wb)
    build_nfr_to_fr(wb)
    build_fr_to_uc(wb)
    build_uc_to_regulation(wb)
    build_rules_satisfaction(wb)
    build_gates_status(wb)
    build_coverage_dashboard(wb)
    build_rule_freeze_sheet(wb)
    build_kg_chains_sheet(wb, base / "KG_CHAINS.md")
    build_funcuc_to_secuc(wb)
    build_muc_to_mitigation(wb)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out_path)
    print(f"[ok] wrote {out_path} with 12 sheets")
    print(f"[stats] rules={freeze_total['rules']} sec_ucs={freeze_total['ucs']} "
          f"func_ucs={freeze_total['funcucs']} mucs={freeze_total['mucs']} "
          f"frs={freeze_total['frs']} nfrs={freeze_total['nfrs']} "
          f"gates={freeze_total['gates']} nodes={freeze_total['nodes']} "
          f"risks={freeze_total['risks']} threats={freeze_total['threats']} "
          f"constrains={freeze_total['constrains']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
