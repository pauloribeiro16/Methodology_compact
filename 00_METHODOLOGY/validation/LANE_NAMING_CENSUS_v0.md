# LANE NAMING Census v0 — registry of UC → lane renames (3 cases)

**Human decision (2026-09-05):** `UC-*` nomenclature reserved for TECHNOLOGY lane;
PROCESS → `PROC-NN`; CAPABILITY → `CAP-NN` (sequential per case, ordered by superseded
ID). Rubric: `REALIZATION_CLASS_RUBRIC.md` v1.3 §5B. Renames applied by
`scripts/rename_lane_ids.py` (single pass, word-boundary, dry-run first).

**Totals:** 224 UCs → TECHNOLOGY 122 (keep UC) · PROCESS 82 → PROC · CAPABILITY 18 → CAP.
Renames: C1 18 · C2 37 · C3 47 = **102**.

---

## Case_01 — 58 UCs → T40 / P17 / C1 (18 renames)

### MIXED adjudications (8)
| UC | Verdict | Justification |
|---|---|---|
| U.C.1.2.1 Erasure | UC | crypto-erasure + receipt is system behaviour |
| U.C.1.3.1 Data Export | UC | system auto-generates JSON/CSV/PDF |
| U.C.2.1.1 Vuln-Free Release | PROC | release procedure dominates; CI scan is a step |
| U.C.2.2.1 Automated Patch Deployment | UC | automation pipeline is the core |
| U.C.2.6.1 Restoration & Recovery | UC | backup/restore executed by systems |
| U.C.3.1.2 MFA Privileged | UC | FIDO2 enforcement is system behaviour |
| U.C.4.1.1 Security by Design | PROC | RFC threat-model SOP dominates |
| U.C.4.3.1 Security Patch Deployment | UC | duplicate of 2.2.1; automation core |

### Mapping table (C1)
| Old | New | Title |
|---|---|---|
| U.C.1.1.1 | PROC-01 | DSAR |
| U.C.1.1.2 | PROC-02 | Rectification |
| U.C.2.1.1 | PROC-03 | Vulnerability-Free Release |
| U.C.2.3.1 | PROC-04 | Coordinated Vulnerability Disclosure |
| U.C.2.5.1 | PROC-05 | Incident Notification 24h/72h |
| U.C.3.4.1 | PROC-06 | Processing & Breach Records |
| U.C.3.6.1 | PROC-07 | Control Effectiveness Testing |
| U.C.4.1.1 | PROC-08 | Security by Design (SSDLC) |
| U.C.4.5.1 | PROC-09 | Pre-Launch Risk Assessment |
| U.C.5.1.1 | PROC-10 | Annual Policy Review |
| U.C.5.1.2 | PROC-11 | Tech Doc Maintenance |
| U.C.5.2.1 | PROC-12 | DPIA Pre-Launch |
| U.C.5.3.1 | PROC-13 | RoPA Maintenance |
| U.C.5.4.1 | PROC-14 | Processor Due Diligence |
| U.C.5.5.1 | CAP-01 | DPAs Binding Processors |
| U.C.6.1.1 | PROC-15 | Annual Awareness Training |
| U.C.6.2.1 | PROC-16 | Role-Specific Training |
| U.C.6.3.1 | PROC-17 | Phishing Simulation |

Kept as UC (T40): all 23 functional U.C.7–11 + compliance U.C.1.2.1, 1.3.1, 1.4.1,
1.5.1, 2.2.1, 2.4.1, 2.4.2, 2.6.1, 3.1.1, 3.1.2, 3.2.1, 3.3.1, 3.5.1, 4.2.1, 4.3.1,
4.4.1, 5.6.1.

---

## Case_02 — 73 UCs → T36 / P27 / C10 (37 renames)

### MIXED adjudications (12)
| UC | Verdict | Justification |
|---|---|---|
| U.C.1.2.1 Erasure (sharding) | UC | crypto sharding destruction core |
| U.C.2.1.1 Incident Detection & Triage | PROC | triage SOP dominates; detection is a step |
| U.C.2.3.1 Vuln Scanning & Mgmt | UC | scanner runs continuously (system) |
| U.C.2.4.1 Patch Deployment (OTA) | UC | signed-OTA pipeline core |
| U.C.3.4.1 Least Privilege Enforcement | UC | RBAC enforcement system behaviour |
| U.C.3.7.1 Human-in-the-Loop Override | UC | product override function |
| U.C.4.2.1 Dependency Scanning & SBOM | UC | tool behaviour per build |
| U.C.4.6.1 AI Model Versioning & Rollback | UC | platform feature |
| U.C.5.7.1 Reg. Notification & Cooperation | PROC | episodic notification duties dominate |
| U.C.5.8.1 Third-Party Boundary Mgmt | UC | per-deployment isolation architecture |
| U.C.6.2.1 AI Accuracy Monitoring & Drift | UC | automated drift detection (system) |
| U.C.6.7.1 AI Training Data Mgmt | UC | dataset lineage platform |

### PKG process-flavoured adjudications (5)
| UC | Verdict | Justification |
|---|---|---|
| U.C.9.5.1 Shift Handover | PROC | pure handover SOP |
| U.C.10.1.1 Kiosk Provisioning | PROC | fleet provisioning procedure |
| U.C.11.1.1 Model Training & Release | PROC | training/release SOP on SYS-05 |
| U.C.11.4.1 Human Bias Review | PROC | review meeting SOP |
| U.C.12.4.1 Admin Reporting SOP | PROC | administrative procedure |

### Mapping table (C2)
| Old | New | Old | New |
|---|---|---|---|
| U.C.1.1.1 | PROC-01 | U.C.5.5.1 | PROC-17 |
| U.C.1.3.1 | PROC-02 | U.C.5.7.1 | PROC-18 |
| U.C.1.4.1 | PROC-03 | U.C.6.1.1 | PROC-19 |
| U.C.1.5.1 | PROC-04 | U.C.6.3.1 | PROC-20 |
| U.C.2.1.1 | PROC-05 | U.C.6.5.1 | PROC-21 |
| U.C.2.2.1 | PROC-06 | U.C.6.6.1 | PROC-22 |
| U.C.2.5.1 | PROC-07 | U.C.9.5.1 | PROC-23 |
| U.C.2.7.1 | PROC-08 | U.C.10.1.1 | PROC-24 |
| U.C.2.8.1 | PROC-09 | U.C.11.1.1 | PROC-25 |
| U.C.3.1.1 | PROC-10 | U.C.11.4.1 | PROC-26 |
| U.C.3.6.1 | PROC-11 | U.C.12.4.1 | PROC-27 |
| U.C.4.1.1 | PROC-12 | U.C.1.6.1 | CAP-01 |
| U.C.4.4.1 | PROC-13 | U.C.2.6.1 | CAP-02 |
| U.C.5.2.1 | PROC-14 | U.C.4.5.1 | CAP-03 |
| U.C.5.3.1 | PROC-15 | U.C.5.1.1 | CAP-04 |
| U.C.5.4.1 | PROC-16 | U.C.5.6.1 | CAP-05 |
| — | — | U.C.7.1.1 | CAP-06 |
| — | — | U.C.7.2.1 | CAP-07 |
| — | — | U.C.7.3.1 | CAP-08 |
| — | — | U.C.7.4.1 | CAP-09 |
| — | — | U.C.7.5.1 | CAP-10 |

Kept as UC (T36): PKG-8..12 product UCs except the 5 above (21) + compliance U.C.1.2.1,
2.3.1, 2.4.1, 3.2.1, 3.3.1, 3.4.1, 3.5.1, 3.7.1, 4.2.1, 4.3.1, 4.6.1, 5.8.1, 6.2.1,
6.4.1, 6.7.1 (15).

---

## Case_03 — 93 UCs → T46 / P40 / C7 (47 renames)

### MIXED adjudications (11)
| UC | Verdict | Justification |
|---|---|---|
| UC-15 SBOM generation | UC | automated per-build generation |
| UC-16 IAM Provisions User Identity | PROC | joiner/approval workflow |
| UC-21 AI Platform Access | UC | platform access control |
| UC-23 SOC Analyst Monitors | CAP | standing SOC function (consistent with C2 U.C.2.6.1) |
| UC-32 Compliance Officer Enforces Retention | PROC | officer enforcement activity |
| UC-33 Erasure | UC | erasure executed by systems |
| UC-34 Export | UC | machine-generated export |
| UC-42 SDM Implements Secure-by-Design | PROC | management process |
| UC-43 Security Engineer Enforces Standards | PROC | engineering process |
| UC-56 Compliance Report | PROC | periodic reporting workflow |
| UC-62 Audit Manager Generates Report | PROC | reporting workflow |

### PKG flags adjudications (6)
| UC | Verdict | Justification |
|---|---|---|
| UC-66 Underwriter Review | PROC | human review step |
| UC-84 Dispute/Chargeback | UC | product dispute flow |
| UC-86 Delegated Users / SoD | UC | product access model |
| UC-89 LC under UCP 600 | UC | product trade-finance flow |
| UC-91 Contact-centre Card Block | UC | product service flow |
| UC-92 Complaint Handling | PROC | complaint SOP |

### Mapping table (C3) — PROCESS (PROC-01..38) and CAPABILITY (CAP-01..07)

Note: the C3 PROCESS count is 40 (32 original + 6 MIXED adjudications: UC-16, 32, 42, 43, 56, 62 + 2 PKG: UC-66, 92). Total renames C3 = 47 (40 PROC + 7 CAP).

| Old | New |
|---|---|
| UC-01 | PROC-01 |
| UC-04 | PROC-02 |
| UC-05 | PROC-03 |
| UC-07 | PROC-04 |
| UC-09 | PROC-05 |
| UC-10 | PROC-06 |
| UC-11 | PROC-07 |
| UC-12 | PROC-08 |
| UC-13 | PROC-09 |
| UC-16 | PROC-10 |
| UC-18 | PROC-11 |
| UC-19 | PROC-12 |
| UC-20 | PROC-13 |
| UC-24 | PROC-14 |
| UC-25 | PROC-15 |
| UC-27 | PROC-16 |
| UC-28 | PROC-17 |
| UC-29 | PROC-18 |
| UC-30 | PROC-19 |
| UC-31 | PROC-20 |
| UC-32 | PROC-21 |
| UC-35 | PROC-22 |
| UC-36 | PROC-23 |
| UC-37 | PROC-24 |
| UC-39 | PROC-25 |
| UC-40 | PROC-26 |
| UC-41 | PROC-27 |
| UC-42 | PROC-28 |
| UC-43 | PROC-29 |
| UC-45 | PROC-30 |
| UC-48 | PROC-31 |
| UC-50 | PROC-32 |
| UC-51 | PROC-33 |
| UC-53 | PROC-34 |
| UC-56 | PROC-35 |
| UC-59 | PROC-36 |
| UC-60 | PROC-37 |
| UC-62 | PROC-38 |
| UC-66 | PROC-39 |
| UC-92 | PROC-40 |

### Mapping table (C3) — CAPABILITY (CAP-01..07)
| Old | New |
|---|---|
| UC-14 | CAP-01 |
| UC-23 | CAP-02 |
| UC-38 | CAP-03 |
| UC-49 | CAP-04 |
| UC-52 | CAP-05 |
| UC-54 | CAP-06 |
| UC-55 | CAP-07 |

Kept as UC (T46): compliance UC-02, 03, 06, 08, 15, 17, 21, 22, 26, 33, 34, 44, 46,
47, 57, 58, 61 (17) + PKG UC-63..65, 67..83, 84, 85, 86, 87, 88, 89, 90, 91, 93 (29).
Phantom UC-98..118 (Doc23/24 supporting system behaviours) keep UC-*, documented.

---

**Final counts:** C1 T40/P17/C1 (58) · C2 T36/P27/C10 (73) · C3 T46/P40/C7 (93) → 122 T / 84 P / 18 C = 224 ✓.
(Single source of truth = the mapping JSONs in `scripts/lane_mappings/` + the kept-UC lists above; totals validated by `rename_lane_ids.py` at run time.)
