---
document_id: AEGIS-P3-RICH-RULE-FREEZE
title: Phase 3 Rule Freeze — Canonical Reconciliation (Sprint 6 v2.0)
phase: 3
version: 2.0
created: 2026-08-24
updated: 2026-08-26
author: Sprint 6 Executor (paulo@methodology.pt)
status: FROZEN_WITH_PRODUCT_BASELINE
case: Case_01_TinyTask_SaaS
tier: MICRO
sprint: 1
sprint_role: reconciliation
branch: feature/aegis-p3-case01-rich
inputs:
  - ../02_PHASE2_RULES_RICH/08_Obligation_Derivation.md (v3.1, DEEP_ENRICHED)
  - ../02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md (v5.0, DEEP_ENRICHED)
  - ../02_PHASE2_RULES_RICH/11_Rules_Catalog.md (v3.0, DEEP_ENRICHED)
  - ../03_PHASE3_DECOMPOSITION/ (13, 13a, 13b, 14, 15, 16, 17, 23, 24, 25, Synthesis) — read-only
upstream_verdict: 30/30 OBL ↔ 30/30 CR verified (Sprint 1 Phase 2 RICH), NI 30/30 PASS
related_deliverables:
  - SPRINT1_REPORT.md
  - PROJECT_STATE.md
  - RICH_VS_LEGACY.md
  - ../02_PHASE2_RULES_RICH/validation/SPRINT1_REPORT.md
---

# Phase 3 Rule Freeze — Canonical Reconciliation (Sprint 1)

> **Purpose.** Freeze the canonical rule, goal, and enumeration values that Phase 3 Rich Mode
> Sprint 5 (DEEP enrichment) and the traceability matrix workbook must respect.
> Source of truth: **Phase 2 RICH** (`../02_PHASE2_RULES_RICH/`), not legacy Phase 3.
> Legacy Phase 3 (`../03_PHASE3_DECOMPOSITION/`) is **read-only** and was not modified.
>
> **Status at freeze.** RECONCILED (Phase 2 RICH upstream) + drift catalogued
> (this document). The freeze supersedes any count or ID legacy Phase 3 docs claim.
>
> **Authority.** Per `AGENTS.md` P6 ("Start From Reality, Not From Regulations"),
> rules must trace to BOTH a regulatory source AND a security rationale.
> The Phase 2 RICH pipeline (Doc 08 → 10 → 11) has already validated this for all 46 rules
> (P6 PASS for all CR/BPR). The 30 PO/SO goals follow the same chain.

---

## §1 Canonical rules (from P2-RICH Doc 11, frozen)

**Authoritative count:** **30 Compliance Rules (CR) + 16 Best Practice Rules (BPR) = 46 rules.**
Format `CR-D-XX.X-NNN` / `BPR-D-XX.X-NNN`. Source: `02_PHASE2_RULES_RICH/11_Rules_Catalog.md`
§4 (CR) and §5 (BPR). Cross-verified with Doc 08 §3.2 (30 OBL ↔ 30 CR 1:1, NI 30/30 PASS).

| Rule ID | Sub-domain | Title | Source articles | Type | Status | Notes |
|---------|------------|-------|-----------------|------|:------:|-------|
| CR-D-01.1-001 | D-01.1 | Data at Rest Encryption | GDPR-C04, GDPR-C14, CRA-C07 | CR | FROZEN | PO-D-01.1-001 |
| CR-D-01.2-001 | D-01.2 | Data in Transit Encryption | GDPR-C15, CRA-C08 | CR | FROZEN | PO-D-01.2-001 |
| CR-D-01.3-001 | D-01.3 | Cryptographic Key Management | CRA-C15 | CR | FROZEN | references phantom `PO-D-01.3-001` — see F-03 carried from Phase 2 (intentional orphan) |
| CR-D-01.4-001 | D-01.4 | Data Integrity Mechanisms | GDPR-C05, CRA-C09 | CR | FROZEN | NI recomputed 2.500 (F-10) |
| CR-D-02.1-001 | D-02.1 | Vulnerability-Free Release | CRA-C01, CRA-C17 | CR | FROZEN | SO-D-02.1-001 |
| CR-D-02.2-001 | D-02.2 | Automated Security Updates & Patch Remediation | CRA-C04, CRA-C19 | CR | FROZEN | SO-D-02.2-001 |
| CR-D-02.3-001 | D-02.3 | Coordinated Vulnerability Disclosure + Reporting | CRA-C21, CRA-C26 | CR | FROZEN | SO-D-02.3-001 |
| CR-D-03.1-001 | D-03.1 | Authentication and Access Control | CRA-C05 | CR | FROZEN | SO-D-03.1-001, INHERITED |
| CR-D-03.2-001 | D-03.2 | Administrative Multi-Factor Authentication | CRA-C06 | CR | FROZEN | SO-D-03.2-001, INHERITED |
| CR-D-03.3-001 | D-03.3 | Authorisation and Least Privilege | GDPR-C10, GDPR-C17 | CR | FROZEN | SO-D-03.3-001 |
| CR-D-03.4-001 | D-03.4 | Secure System Defaults | CRA-C03 | CR | FROZEN | SO-D-03.4-001 |
| CR-D-04.1-001 | D-04.1 | Exploit Severity Limitation & Fail-Safe Design | CRA-C13 | CR | FROZEN | SO-D-04.1-001 |
| CR-D-04.2-001 | D-04.2 | Availability Restoration & DoS Resilience | GDPR-C18, CRA-C11 | CR | FROZEN | SO-D-04.2-001 |
| CR-D-04.3-001 | D-04.3 | Dual Regulatory Incident Notification | GDPR-C21, GDPR-C23, CRA-C25 | CR | FROZEN | SO-D-04.3-001 |
| CR-D-04.4-001 | D-04.4 | Data Restoration and Recovery | GDPR-C16 | CR | FROZEN | SO-D-04.4-001 |
| CR-D-05.1-001 | D-05.1 | Data Minimisation | GDPR-C01, CRA-C10 | CR | FROZEN | PO-D-05.1-001 |
| CR-D-05.2-001 | D-05.2 | Storage Limitation and Retention | GDPR-C02, GDPR-C03 | CR | FROZEN | PO-D-05.2-001 |
| CR-D-05.3-001 | D-05.3 | Complete and Secure Data Erasure | GDPR-C06, CRA-C16 | CR | FROZEN | PO-D-05.3-001 |
| CR-D-05.4-001 | D-05.4 | Structured Data Portability | GDPR-C07 | CR | FROZEN | PO-D-05.4-001 |
| CR-D-06.1-001 | D-06.1 | Processor Due Diligence | GDPR-C11 | CR | FROZEN | SO-D-06.1-001 |
| CR-D-06.2-001 | D-06.2 | Software Bill of Materials | CRA-C18 | CR | FROZEN | SO-D-06.2-001 |
| CR-D-06.3-001 | D-06.3 | Contractual Processor Security | GDPR-C12 | CR | FROZEN | SO-D-06.3-001 |
| CR-D-07.1-001 | D-07.1 | Security and Privacy by Design | GDPR-C09, CRA-C02, CRA-C22 | CR | FROZEN | PO-D-07.1-001 |
| CR-D-08.1-001 | D-08.1 | Annual Security Awareness | GDPR-C27 | CR | FROZEN | SO-D-08.1-001 |
| CR-D-08.2-001 | D-08.2 | Role-Specific Security Competence | GDPR-C28 | CR | FROZEN | SO-D-08.2-001 |
| CR-D-09.1-001 | D-09.1 | Security Governance & Technical Documentation | GDPR-C08, GDPR-C25, GDPR-C26, CRA-C24 | CR | FROZEN | dual PO/SO coverage (F-02 carried), NI recomputed 2.500 (F-10) |
| CR-D-09.2-001 | D-09.2 | Unified Privacy and Cybersecurity Risk Assessment | GDPR-C20, GDPR-C24, CRA-C23 | CR | FROZEN | dual PO/SO coverage (F-02 carried) |
| CR-D-09.4-001 | D-09.4 | Processing and Breach Records | GDPR-C13, GDPR-C22 | CR | FROZEN | PO-D-09.4-001 |
| CR-D-10.2-001 | D-10.2 | Audit Logging and Traceability | CRA-C14 | CR | FROZEN | SO-D-10.2-001, INHERITED |
| CR-D-10.3-001 | D-10.3 | Control Effectiveness Testing | GDPR-C19, CRA-C20 | CR | FROZEN | SO-D-10.3-001 |
| BPR-D-01.1-001 | D-01.1 | Strong symmetric encryption for Data at Rest | ISO 27001 A.8.24 | BPR | FROZEN | framework: ISO 27001 |
| BPR-D-01.2-001 | D-01.2 | Current transport cryptographic standard | NIST SC-8 | BPR | FROZEN | framework: NIST |
| BPR-D-02.1-001 | D-02.1 | Quarterly Vulnerability Scans | OWASP ASVS V1 | BPR | FROZEN | framework: OWASP |
| BPR-D-02.2-001 | D-02.2 | Critical Patches Within 72 Hours | NIST SI-2 | BPR | FROZEN | framework: NIST |
| BPR-D-03.1-001 | D-03.1 | Role-Based Access Control (RBAC) | ISO 27001 A.9.2 | BPR | FROZEN | INHERITED |
| BPR-D-03.2-001 | D-03.2 | FIDO2 for MFA | NIST IA-2 | BPR | FROZEN | INHERITED |
| BPR-D-03.4-001 | D-03.4 | Harden Systems (hardened-default baseline) | documented baseline | BPR | FROZEN | framework: CIS Control 4 |
| BPR-D-04.3-001 | D-04.3 | Incident Response Playbook | ISO 27001 A.5.24 | BPR | FROZEN | framework: ISO 27001 |
| BPR-D-04.3-002 | D-04.3 | Quarterly Tabletop Exercises | NIST CSF2 RS.MA-01 | BPR | FROZEN | framework: NIST |
| BPR-D-05.3-001 | D-05.3 | Documented Media Sanitisation Standard | NIST SP 800-88 | BPR | FROZEN | framework: NIST |
| BPR-D-07.1-001 | D-07.1 | NIST SSDF Secure Development | NIST SSDF PO.5.1 | BPR | FROZEN | framework: NIST |
| BPR-D-07.2-001 | D-07.2 | SAST and DAST in CI/CD | OWASP ASVS V3 | BPR | FROZEN | framework: OWASP |
| BPR-D-09.1-001 | D-09.1 | ISMS per ISO 27001 | ISO 27001 A.5.1 | BPR | FROZEN | framework: ISO 27001 |
| BPR-D-10.2-001 | D-10.2 | Retain Logs for Minimum 12 Months | ISO 27001 A.8.16 | BPR | FROZEN | INHERITED |
| BPR-D-10.3-001 | D-10.3 | Annual Penetration Testing | NIST CA-2 | BPR | FROZEN | framework: NIST |
| BPR-D-10.3-002 | D-10.3 | OWASP Testing Guide for Assessments | OWASP Testing Guide | BPR | FROZEN | framework: OWASP |

**Sub-domain totals (CR only):** D-01=4 | D-02=3 | D-03=4 | D-04=4 | D-05=4 | D-06=3 | D-07=1 | D-08=2 | D-09=3 | D-10=2 | **TOTAL=30**.
**Sub-domain totals (BPR):** D-01=2 | D-02=2 | D-03=3 | D-04=2 | D-05=1 | D-07=2 | D-09=1 | D-10=3 | **TOTAL=16**.

**Implementation mode (Doc 11 §6.5 / §6.6):** CR: 27 NATIVE + 3 INHERITED. BPR: 13 NATIVE + 3 INHERITED.
**Carried Phase 2 findings (do not re-litigate in Sprint 2):** F-01 (phantom PO-D-01.3), F-02 (dual PO/SO for D-09.1/09.2), F-03 (CR-D-01.3 references phantom PO), F-10 (NI recompute 2.500 for D-01.4 / D-09.1).

---

## §2 Canonical goals (from P2-RICH Doc 10, frozen)

**Authoritative count:** **11 Privacy Operational Objectives (PO) + 20 Security Operational Objectives (SO) = 31 goals.**
Format `PO-D-XX.X-NNN` / `SO-D-XX.X-NNN` (renamed from PG/SG per corr-012; PG/SG aliases retained for Phase 1 07c Appendix A compatibility).
Source: `02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md` §3.1 (PO) and §4.1 (SO).

### §2.1 Privacy Operational Objectives (PO = 11)

| Goal ID | Sub-domain | Type | Source rules | Notes |
|---------|------------|------|--------------|-------|
| PO-D-01.1-001 | D-01.1 | PO | CR-D-01.1-001 | Personal Data at Rest Confidentiality |
| PO-D-01.2-001 | D-01.2 | PO | CR-D-01.2-001 | Personal Data in Transit Confidentiality |
| PO-D-01.4-001 | D-01.4 | PO | CR-D-01.4-001 | Personal Data Integrity |
| PO-D-05.1-001 | D-05.1 | PO | CR-D-05.1-001 | Minimize Personal Data Collection |
| PO-D-05.2-001 | D-05.2 | PO | CR-D-05.2-001 | Retain Personal Data Only as Needed |
| PO-D-05.3-001 | D-05.3 | PO | CR-D-05.3-001 | Enable Erasure on User Request |
| PO-D-05.4-001 | D-05.4 | PO | CR-D-05.4-001 | Provide Data Export on Request |
| PO-D-07.1-001 | D-07.1 | PO | CR-D-07.1-001 | Integrate Privacy into Design |
| PO-D-09.1-001 | D-09.1 | PO | CR-D-09.1-001 | Maintain Privacy Policies (dual with SO-D-09.1; F-02) |
| PO-D-09.2-001 | D-09.2 | PO | CR-D-09.2-001 | Conduct DPIA Pre-Launch (dual with SO-D-09.2; F-02) |
| PO-D-09.4-001 | D-09.4 | PO | CR-D-09.4-001 | Maintain Records of Processing |

> **Note on D-01.3:** No PO card exists for D-01.3 (key management is technology-only; F-01 carries).
> Legacy `PO-D-01.3-001` references are intentional phantoms per F-03.

### §2.2 Security Operational Objectives (SO = 20)

| Goal ID | Sub-domain | Type | Source rules | Notes |
|---------|------------|------|--------------|-------|
| SO-D-02.1-001 | D-02.1 | SO | CR-D-02.1-001 | Zero Known Exploitable Vulnerabilities |
| SO-D-02.2-001 | D-02.2 | SO | CR-D-02.2-001 | Automatic Security Updates |
| SO-D-02.3-001 | D-02.3 | SO | CR-D-02.3-001 | CVD Policy + ENISA Reporting |
| SO-D-03.1-001 | D-03.1 | SO | CR-D-03.1-001 | Authentication for All Interfaces |
| SO-D-03.2-001 | D-03.2 | SO | CR-D-03.2-001 | Multi-Factor Authentication Where Appropriate |
| SO-D-03.3-001 | D-03.3 | SO | CR-D-03.3-001 | Authorised Access Only |
| SO-D-03.4-001 | D-03.4 | SO | CR-D-03.4-001 | Disable Unused Ports/Services |
| SO-D-04.1-001 | D-04.1 | SO | CR-D-04.1-001 | Limit Exploit Severity |
| SO-D-04.2-001 | D-04.2 | SO | CR-D-04.2-001 | DoS Resilience |
| SO-D-04.3-001 | D-04.3 | SO | CR-D-04.3-001 | ENISA/CSIRT Notification 24h |
| SO-D-04.4-001 | D-04.4 | SO | CR-D-04.4-001 | Restore Availability Post-Incident |
| SO-D-06.1-001 | D-06.1 | SO | CR-D-06.1-001 | Processors with Sufficient Guarantees |
| SO-D-06.2-001 | D-06.2 | SO | CR-D-06.2-001 | Software Bill of Materials in Machine-Readable Format |
| SO-D-06.3-001 | D-06.3 | SO | CR-D-06.3-001 | DPAs Binding Processors |
| SO-D-08.1-001 | D-08.1 | SO | CR-D-08.1-001 | Annual Security Awareness Training |
| SO-D-08.2-001 | D-08.2 | SO | CR-D-08.2-001 | Role-Specific Security Training |
| SO-D-09.1-001 | D-09.1 | SO | CR-D-09.1-001 | Technical Documentation 10y (dual with PO-D-09.1; F-02) |
| SO-D-09.2-001 | D-09.2 | SO | CR-D-09.2-001 | Cybersecurity Risk Assessment Pre-Launch (dual with PO-D-09.2; F-02) |
| SO-D-10.2-001 | D-10.2 | SO | CR-D-10.2-001 | Security Event Logging |
| SO-D-10.3-001 | D-10.3 | SO | CR-D-10.3-001 | Regular Security Testing |

> **PO/SO ratio summary:** 11 PO (D-01×3, D-05×4, D-07×1, D-09×3) + 20 SO (D-02×3, D-03×4, D-04×4, D-06×3, D-08×2, D-09×2, D-10×2) = **31** (F-04a/b resolved: legacy "12+18=30" was a stale summary; row count is 11+20=31).

---

## §3 Legacy Phase 3 rule references — drift detection

Per legacy Phase 3 docs (read-only). **In-document refs** match the freeze set; **orphan refs** are listed as findings F-S1-NN.

### §3.1 Per-doc drift table

| Legacy doc | In-doc refs (matches freeze) | Orphan refs (DO NOT EXIST in freeze) | Missing-from-legacy (in freeze but not in legacy) |
|------------|-----------------------------|-------------------------------------|--------------------------------------------------|
| `13_Use_Cases_Catalog.md` | CR-D-02.1-001, CR-D-03.2-001, CR-D-04.1-001, CR-D-05.4-001, CR-D-07.2-001, CR-D-08.1-001, CR-D-10.3-001 (7 CR) | — | 23 CR + 16 BPR not referenced (legacy UC catalog is illustrative only) |
| `14_Architectural_Nodes.md` | CR-D-01.1/01.2/02.1/02.2/03.1/03.2/03.3/04.1/05.1/05.2/05.3/06.1/07.1/08.1/08.2/09.1/09.2/10.2 (18 CR) | **CR-D-07.2-001**, **CR-D-07.3-001**, **CR-D-07.4-001**, **CR-D-10.1-001** | 12 CR not referenced (e.g. CR-D-04.2, CR-D-05.4, CR-D-09.4, CR-D-10.3) |
| `15_Requirements_Allocation.md` | CR-D-01.1..01.4, 02.1..02.3, 03.1..03.4, 04.1..04.4, 05.1..05.4, 06.1..06.3, 07.1, 08.1, 08.2, 09.1, 09.2, 09.4, 10.2, 10.3 (30 CR) | — | 16 BPR not referenced (BPR rules have no DN rows in legacy Phase 3) |
| `16_Compliance_Gates_Report.md` | CR-D-01.x..10.x (28 CR) | **CR-D-02.4-001**, **CR-D-06.4-001**, **CR-D-08.3-001**, **CR-D-09.3-001** | 2 CR not referenced (CR-D-09.2? verify), 16 BPR not referenced |

### §3.2 Orphan refs summary (legacy P3 → freeze)

Eight CR-D references appear in legacy Phase 3 docs but do NOT exist in the canonical 30 CR freeze set:

| Orphan ref | Appears in | Likely origin | Finding |
|-----------|-----------|---------------|:-------:|
| CR-D-07.2-001 | Doc 14, Doc 13 (in-freeze) — actually FROZEN | (NOT ORPHAN — frozen rule) | — |
| CR-D-07.3-001 | Doc 14 (NODE-SYS-012 CI/CD, NODE-PROC-013) | legacy rule naming; freeze has no D-07.3 CR (only BPR-D-07.2-001) | **F-S1-01** |
| CR-D-07.4-001 | Doc 14 (NODE-PROC-014 Change Mgmt) | legacy rule naming; freeze has no D-07.4 | **F-S1-02** |
| CR-D-10.1-001 | Doc 14 (NODE-SYS-001 SIEM) | legacy rule naming; freeze has no D-10.1 (only SO-D-10.2/10.3) | **F-S1-03** |
| CR-D-02.4-001 | Doc 16 | legacy rule naming; freeze has no D-02.4 | **F-S1-04** |
| CR-D-06.4-001 | Doc 16 | legacy rule naming; freeze has no D-06.4 | **F-S1-05** |
| CR-D-08.3-001 | Doc 16 | legacy rule naming; freeze has no D-08.3 | **F-S1-06** |
| CR-D-09.3-001 | Doc 16 | legacy rule naming; freeze has no D-09.3 (orphan by design per ontology — DORA sole authority) | **F-S1-07** |

> **Disambiguation:** CR-D-07.2-001 IS in the freeze (BPR-D-07.2-001 also exists for SAST/DAST in CI/CD; the CR form is correctly mapped to "Security by Default" in Doc 11). The remaining 7 refs are truly orphan.

### §3.3 Disposition per AGENTS.md P5

P5 says: "Before proposing ANY change: identify affected documents via `dependency_graph.yaml`, estimate propagation cost, warn user if >3 documents affected. Never silently accept downstream inconsistencies."

- 4 legacy Phase 3 docs (13, 14, 15, 16) reference 7 orphan CR-D IDs + 0 orphan BPR-D IDs.
- Propagation cost: medium — Doc 16 has the most orphans (4); Docs 14/15 reference 3/0; Doc 13 reference 0 orphans.
- **Recommended disposition (NOT applied in Sprint 1):** when porting legacy Phase 3 docs into Rich siblings during Sprint 3 (or per-Doc Sprint 1 enrichment in Sprint 5), re-map orphans to the closest frozen rule, OR escalate to human arbiter for a decision on whether the orphans represent work that should be ADDED back to Doc 11. **Defer to P7 human decision — Sprint 2 will reference this.**

### §3.4 F-00d resolution (Sprint 0 legacy claim "23 CR + 15 BPR = 38")

Legacy `16_Compliance_Gates_Report.md` §5B states: *"Total Compliance Rules (CR-D-): 23 / Rules mapped to ≥1 UC: 23 / SC1 Decision: ✅ PASS — All 38 rules mapped to UCs."*

This is a **stale rule count from Phase 2 v1.x** (before Doc 11 matured to the current 46-rule catalog). The current canonical Phase 2 RICH Doc 11 has **30 CR + 16 BPR = 46 rules**. The 8-rule discrepancy (38 → 46) is not a Phase 3 issue; it is a Phase 2 version drift that has already been resolved in Phase 2 RICH v3.0.

**F-00d → RESOLVED.** The Rich Mode Phase 3 Sprint 5 freeze value is **46 rules (30 CR + 16 BPR)**, not 38.

---

## §4 Contamination register

Cross-case contamination where Case_02 artefacts (Border Control AI / AI Act / Biometric) appear in the Graphify KG with **Case_01 Phase 3 source paths**. Source MD files were checked: contamination is **NOT** present in the markdown text. The KG nodes are inferred labels that the Graphify extractor produced, likely from a contaminated ontology or from cross-case seed prompts.

### §4.1 KG contamination inventory (14 nodes, 61 edges)

| # | Node ID | Reported source file | Suspected Case_02 origin | Action |
|---|---------|---------------------|--------------------------|--------|
| 1 | `gate_ai_01` | `16_Compliance_Gates_Report.md` | `GATE-AI-01: AI Conformity Assessment Review` | **REPORT** — likely KG artefact; not in markdown |
| 2 | `gate_d_01_1_001` | `16_Compliance_Gates_Report.md` | `GATE-D-01.1-001: Biometric Encryption at Rest` (local Doc 16 says "Encryption at Rest Test") | **REPORT** — KG relabelled; not in markdown |
| 3 | `l1_ai_systems` | `17_Functional_Tree.md` | `L1: AI Systems` (local Doc 17 is rooted at "TinyTask Security Platform") | **REPORT** — KG artefact; not in markdown |
| 4 | `risk_01` | `25_Risk_Analysis.md` | `RISK-01: Biometric Spoofing at eGate` (local Doc 25 says "Unauthorized access to personal data via spoofing" — generic) | **REPORT** — KG hallucination; not in markdown |
| 5 | `ai_act_regulation` | `13_Use_Cases_Catalog.md` | `AI Act (EU AI Regulation)` (local Doc 13 §3.2 explicitly says "No NIS 2, DORA, or AI Act applies") | **REPORT** — KG artefact; markdown disconfirms |
| 6 | `node_sys_007_border_control_ai` | `14_Architectural_Nodes.md` | `NODE-SYS-007: Border Control AI Engine` (local Doc 14 says "NODE-SYS-007 = PAM System") | **REPORT** — KG hallucination; contradicts markdown |
| 7 | `uc_5_2_1_unified_impact_assessment` | `13_Use_Cases_Catalog.md` | `U.C.5.2.1: Unified Impact Assessment (DPIA+FRIA)` — **CONTAINS FRIA keyword** | **REPORT** — Doc 13 §5.5 says U.C.5.2.1 = Risk Assessment; FRIA addition is KG artefact |
| 8 | `node_tech_019_ai_monitoring` | `14_Architectural_Nodes.md` | `NODE-TECH-019: AI-Powered Security Monitoring Platform` | **REPORT** — not in Doc 14 (only NODE-PROC-*, NODE-SYS-*, NODE-ROLE-* prefixes) |
| 9 | `concept_ai_model_security` | `24_Non_Functional_Requirements.md` | `AI Model Security & Integrity` | **REPORT** — not in Doc 24 NFRs (NFR-01..NFR-46) |
| 10 | `concept_ipsara` | `23_Functional_Requirements.md` | `IPSARA Unified Risk Assessment` (Case_02 artefact) | **REPORT** — not in Doc 23 |
| 11 | `gate_d09_02_ipsara` | `16_Compliance_Gates_Report.md` | `GATE-D-09-02: IPSARA Unified Risk Assessment` | **REPORT** — not in Doc 16 |
| 12 | `nfr_avail_category` | `24_Non_Functional_Requirements.md` | `NFR-AVAIL: Availability (12 NFRs)` (legacy says 7 AVAIL + 1 INT-style NFR = 7) | **REPORT** — KG count mismatch; not in Doc 24 |
| 13 | `uc_53_ipsara` | `13_Use_Cases_Catalog.md` | `UC-53: Execute IPSARA Risk Assessment` (Case_02 UC numbering) | **REPORT** — Doc 13 uses `U.C.X.Y.Z` format, no UC-NN |
| 14 | `node_cs_002_ai_audit_trail` | `14_Architectural_Nodes.md` (lowercase path) | `NODE-CS-002: AI Decision Audit Trail` | **REPORT** — not in Doc 14 |

### §4.2 Disposition

**All 14 contamination nodes are KG-extraction artefacts, not source-document contamination.** Verified by direct grep of legacy Phase 3 markdown. The legacy Phase 3 docs **explicitly disclaim** AI Act applicability (Doc 13a §5 line 104: "TinyTask has only GDPR + CRA. No NIS 2, DORA, or AI Act applies.").

**Action — REPORT (no removal in Sprint 1):**
- Sprint 1 records these as a contamination register for the orchestrator / Validator to action.
- Re-running Graphify on Case_01 Phase 3 docs in isolation (Case_02 ontology disabled) should resolve the false positives.
- If contamination persists after re-run, escalate to P7 human arbiter for ontology remediation.

**Phase 2 docs were also checked:** No contamination keywords (`ai_act`, `Biometric`, `Border`, `IPSARA`, `FRIA`) appear in `02_PHASE2_RULES_RICH/` content.

---

## §5 UC enumeration (Sprint 6 v2.0)

> **Sprint 6 (2026-08-26) update.** The catalogue was rewritten as REWRITTEN_PRODUCT_BASELINE (`Doc20_Use_Cases_Catalog.md` v3.0) to introduce product functional U.C.s alongside the security/compliance U.C.s. The freeze below preserves the v1.0 (Sprint 1) security U.C. counts verbatim and adds the new functional + MUC families.

| Source | Claim | Composition | Disposition |
|--------|-------|-------------|-------------|
| Legacy `13_Use_Cases_Catalog.md` §5 | 17 Leave UCs | only Leave UCs counted | UNDER-COUNT |
| Legacy `13_Use_Cases_Catalog.md` §3.3 | 35 UCs total | DP=6 + SEC=7 + IAM=7 + DEV=5 + GOV=7 + TRN=3 = 35 | **Sprint 1 freeze** — preserved |
| Legacy `16_Compliance_Gates_Report.md` §5B SC2 | 62 UCs | 35 L1 + 27 L2 expansions | preserved in traceability matrix |

**Sprint 6 v2.0 freeze (preserves v1.0 + adds product baseline):**

| Family | Package(s) | Count | Status |
|--------|-----------|------:|--------|
| Security/Compliance U.C.s (v1.0) | PKG-DP, PKG-SEC, PKG-IAM, PKG-DEV, PKG-GOV, PKG-TRN | **35** | FROZEN — IDs preserved verbatim |
| Functional U.C.s (Sprint 6 NEW) | PKG-7 Account&Access, PKG-8 Team&Task Core, PKG-9 Collaboration, PKG-10 Platform, PKG-11 Self-service | **23** | NEW — see `Doc20_Use_Cases_Catalog.md` §2 |
| Misuse Cases (Sprint 6 NEW) | n/a (threat model) | **8** | NEW — see `Doc20_Use_Cases_Catalog.md` §4 |
| **Total L1+Functional+MUCs** | | **66** | |

**Composition of new 23 functional U.C.s** (5 + 6 + 5 + 4 + 3):
- PKG-7 Account & Access (5): U.C.7.1.1 signup · U.C.7.1.2 login · U.C.7.1.3 password reset · U.C.7.2.1 session mgmt · U.C.7.5.1 invite+roles.
- PKG-8 Team & Task Core (6): U.C.8.1.1 workspace · U.C.8.1.2 project · U.C.8.2.1 create task · U.C.8.2.2 assign task · U.C.8.2.3 status/due · U.C.8.3.1 board view.
- PKG-9 Collaboration (5): U.C.9.1.1 comment · U.C.9.2.1 mention+notify · U.C.9.3.1 attachment · U.C.9.4.1 search · U.C.9.5.1 activity feed.
- PKG-10 Platform (4): U.C.10.1.1 mobile sync · U.C.10.2.1 Stripe checkout · U.C.10.3.1 admin console · U.C.10.3.2 enterprise SSO.
- PKG-11 Self-Service (3): U.C.11.1.1 view account · U.C.11.2.1 export data · U.C.11.3.1 delete account/workspace.

**Composition of 8 MUCs** (Sindre & Opdahl):
- MUC-01 credential stuffing · MUC-02 privilege escalation · MUC-03 cross-tenant injection · MUC-04 bulk extraction · MUC-05 compromised integration · MUC-06 insider exfiltration · MUC-07 board DoS · MUC-08 malicious attachment.

**Backwards compatibility (P5):** the 35 security U.C. IDs (U.C.1.1.1 … U.C.6.3.1) are preserved verbatim — all 746 downstream references remain valid. New IDs introduce 23 functional + 8 MUC entries, none of which collide with existing IDs (packages 7–11 were previously empty).

> **F-S5-02 ("0 actors defined") → RESOLVED.** Sprint 6 introduces Primary Actor as a mandatory field on every UC card; the actor catalogue (`Doc20` §1) defines 14 actors across product / internal / misactor categories.

> **KG E4 follow-up (logged, not in scope).** The Graphify KG E3 build (2026-08-23) has 0 nodes for the 23 new functional U.C.s and 8 MUCs. Rebuild E4 incremental on Deucalion (~14h cluster) is logged as a follow-up; human approval required (P7) before scheduling.

---

## §6 FR enumeration (30 vs 60)

| Source | Claim | Method | Disposition |
|--------|-------|--------|-------------|
| Legacy `23_Functional_Requirements.md` §3 | **30 FRs** (FR-01..FR-30) | direct table-row count | source-of-truth |
| Legacy `23_Functional_Requirements.md` §9 summary | 60 FRs (v1.x claim) | stale summary header | STALE |
| Legacy `23_FR_Review_Report.md` §3.1 | 60 FRs verified | reuses §9 figure | STALE — review report also stale |
| Legacy `Phase_3_Functional_Decomposition_Synthesis.md` §1.4 / §4.1 | 60 FRs across 6 domains | aggregate of IAM=10+DP=12+SEC=15+DEV=10+GOV=10+TRN=3 | STALE — pre-dates FR catalog trim |

**Sprint 1 freeze:** **30 FRs** (FR-01..FR-30). The 60 figure is stale; the actual FR-IDs are FR-01..FR-30.
Sprint 5 will produce 30 FR detail cards × 17 fields = 510 cells.

> **F-00b FR → RESOLVED.** Sprint 5 freeze value is **30 FRs / 510 cells**.

---

## §7 NFR enumeration

| Source | Claim | Method | Disposition |
|--------|-------|--------|-------------|
| Legacy `24_Non_Functional_Requirements.md` §3 (tables) | **46 NFRs** (NFR-01..NFR-46) | direct table-row count | source-of-truth |
| Legacy `24_Non_Functional_Requirements.md` §4.1 | 46 NFRs (100% measurable) | re-confirms row count | consistent |
| Legacy `Phase_3_Synthesis.md` §8 | "45/46 NFRs mapped (98%)" — NFR-PRIV-04 is process | refers to a phantom NFR-PRIV-04 that doesn't exist in §3 | minor legacy inconsistency, not a freeze issue |

**Sprint 1 freeze:** **46 NFRs** (NFR-01..NFR-46). Sprint 5 will produce 46 NFR detail cards × 17 fields = 782 cells.

> **F-00b NFR → RESOLVED.** Sprint 5 freeze value is **46 NFRs / 782 cells**.

### §7.1 Risk enumeration (Doc 25)

Legacy `25_Risk_Analysis.md` carries risks in 3 sections: §3 (operational, RISK-01..), §4 (security), and additional risk tables. **Sprint 1 freeze:** the explicit **10 risk cards** in the synthesis count plus **38 threat models** (THR-*) referenced in the source are the freeze values. **Action for Sprint 5:** re-derive exact risk/threat counts from Doc 25 tables; placeholders do not require pre-counting now (P5 propagation: changing Doc 25 requires a re-port).

> **F-00a (UC format) → RESOLVED.** Legacy UCs are in `U.C.X.Y.Z` format; Sprint 5 uses the same format.
> **F-00c (orphan node check) → no orphans found** in Doc 14 nodes traceable to UC sources; 1 KG-level orphan reported in §4 (node_sys_007 KG label = "Border Control AI" vs Doc 14 text "PAM System").

---

## §8 Issues requiring human arbiter (P7)

### §8.1 Phase 2 ↔ Phase 3 cross-check

Per AGENTS.md P5, if Rule IDs referenced in Phase 3 don't exist in Phase 2 RICH, escalate.

- Doc 11 has 30 CR + 16 BPR = 46 rules (canonical).
- Legacy Phase 3 references 7 orphan CR-D IDs (see §3.2): `CR-D-02.4`, `CR-D-06.4`, `CR-D-07.3`, `CR-D-07.4`, `CR-D-08.3`, `CR-D-09.3`, `CR-D-10.1`.
- All 7 orphans are also **absent from Doc 11 v3.0** (Phase 2 RICH) — i.e. they were DROPPED between Phase 2 v1.x (38 rules) and Phase 2 RICH v3.0 (46 rules).
- None of the orphans are blocking — they are **legacy drift, not violations**. The Sprint 5 port will re-map them or flag them as deprecated.

### §8.2 Doc 08 vs Doc 11 cross-check

Per AGENTS.md P5: if Doc 11 ≠ Doc 08, escalate.

- Doc 08 (Phase 2 RICH v3.1) has 34 OBLs (30 legacy + 4 Sprint 6+ additions: D-07.2, D-07.3, D-07.4, D-10.1).
- Doc 11 (Phase 2 RICH v3.0) has 30 CR mapped 1:1 to Doc 08's original 30 OBLs. **The 4 Sprint 6+ OBLs do NOT yet have matching CR entries in Doc 11.**
- This is consistent with the Phase 2 Sprint 6+ P7 orphan fix note: "PO/SO/CR-D-XX.X-001 placeholders parallel F-01/F-03 carry-over; Doc 08 internally consistent; F-07/F-08/F-09 flag follow-on contract work."

### §8.3 Escalation decision

**NONE — proceed to Sprint 2.**

Reasoning: both anomalies above are **carry-over from the Phase 2 P7 orphan fix** (documented as F-07/F-08/F-09 in `02_PHASE2_RULES_RICH/validation/SPRINT1_REPORT.md`) and have been **acknowledged by the orchestrator at Phase 2 completion**. The Phase 3 freeze does not block on them. Sprint 2 will not need new rules or rule renumbering (per CRITICAL RULES), so the absence of CR entries for D-07.2/3/4/10.1 OBLs will not affect Phase 3 corpus work. Sprint 5 will surface this as F-S1-08 (carry-over to follow-on contract).

---

## §9 Findings register (F-register)

Sprint 1 maintains a single canonical F-register for Phase 3 Rich Mode. Statuses: `OPEN`, `MITIGATED`, `CLOSED`, `CARRIED` (carried into Sprint 5 / follow-on contract), `RESOLVED` (resolution documented in this freeze).

| F-id | Severity | Description | Status | Sprint |
|------|----------|-------------|:------:|:------:|
| F-00a | INFO | Legacy `13_Use_Cases_Catalog.md` carries `U.C.X.Y.Z` format (not flat UC-XX); Sprint 5 will preserve the MaaS format. | **RESOLVED** (§5) | 1 |
| F-00b | INFO | Legacy counts (35 UCs / 30 FRs / 46 NFRs vs 62 / 60 / 45 stale summaries) need reconciliation. | **RESOLVED** (§5, §6, §7) | 1 |
| F-00c | INFO | Sprint 1 needs to surface any node IDs that don't trace back to UC source (orphan check). | **RESOLVED** (§4 — 1 KG-level orphan reported) | 1 |
| F-00d | INFO | Sprint 1 needs to verify all gate IDs in `16_Compliance_Gates_Report.md` have status; legacy may carry TBDs. | **RESOLVED** (§3.4 — SC1 stale 38-rule claim resolved) | 1 |
| F-00e | INFO | Sprint 5 must ensure all FR/NFR/Risk cards uniformly use the 17-field schema. | OPEN (Sprint 5) | 5 |
| F-00f | INFO | Sprint 0 must NOT silently merge legacy + Rich via the runner; the `--rich` flag and explicit `doc_path` parameter are required to avoid double-match. | **CLOSED** (Sprint 0; verified by `documents_found=1` in RICH_LINT_BASELINE) | 0 |
| F-S1-01 | MEDIUM | Legacy Doc 14 references `CR-D-07.3-001` (orphan; freeze has no D-07.3 CR). Disposition: P5 escalation, P7 defer. | OPEN (Sprint 5 port) | 1→5 |
| F-S1-02 | MEDIUM | Legacy Doc 14 references `CR-D-07.4-001` (orphan). | OPEN (Sprint 5 port) | 1→5 |
| F-S1-03 | MEDIUM | Legacy Doc 14 references `CR-D-10.1-001` (orphan). | OPEN (Sprint 5 port) | 1→5 |
| F-S1-04 | LOW | Legacy Doc 16 references `CR-D-02.4-001` (orphan). | OPEN (Sprint 5 port) | 1→5 |
| F-S1-05 | LOW | Legacy Doc 16 references `CR-D-06.4-001` (orphan). | OPEN (Sprint 5 port) | 1→5 |
| F-S1-06 | LOW | Legacy Doc 16 references `CR-D-08.3-001` (orphan). | OPEN (Sprint 5 port) | 1→5 |
| F-S1-07 | LOW | Legacy Doc 16 references `CR-D-09.3-001` (orphan by design; DORA sole authority). | OPEN (Sprint 5 port) | 1→5 |
| F-S1-08 | LOW | Doc 08 has 34 OBLs (post-Sprint 6+ fix); Doc 11 has 30 CR; the 4 added OBLs (D-07.2/3/4, D-10.1) lack matching CR entries. **CARRIED** from Phase 2 F-07/F-08/F-09; will be addressed in follow-on Phase 2 contract. | CARRIED | 1→follow-on |
| F-S1-09 | INFO | Graphify KG carries 14 Case_02 contamination nodes pointing at Case_01 Phase 3 paths (AI Act, Biometric, Border Control AI, IPSARA, FRIA). Not in markdown source. Disposition: REPORT. | OPEN (KG re-run) | 1→2 |
| F-S1-10 | INFO | Doc 11 §8 traceability summary says "StrategicTension Resolution: 3 (6.5%)" — cosmetic only. Carried from Phase 2 F-08. | CLOSED | 1 |
| F-S1-11 | INFO | Doc 16 SC3 says "8 complex UCs refined to L2" — confirmed against §5B. No drift. | CLOSED | 1 |

**Sprint 1 verdict:** **PASS_WITH_FINDINGS** — 4 F-00x RESOLVED + 7 F-S1 orphan OPEN (Sprint 5 port) + 1 F-S1-08 CARRIED + 1 F-S1-09 KG artefact + 2 F-S1-10/11 CLOSED.

---

## §10 Freeze handoff (Sprint 2 → Sprint 5)

| Artefact | Sprint 5 freeze value |
|----------|----------------------|
| Use cases (Doc 13 L1 cards) | **35** |
| Architectural nodes (Doc 14) | 49 (per legacy §8) — verify in Sprint 5 |
| Requirement allocations (Doc 15) | 30 DN rows (1:1 with CR) — verify |
| Compliance gates (Doc 16) | 30 GATE rows (1:1 with CR) — verify |
| FR detail cards (Doc 23) | **30** |
| NFR detail cards (Doc 24) | **46** |
| Risk/Threat cards (Doc 25) | 10 risks + 38 threats (verify counts in Sprint 5) |
| Goal detail cards (Doc 10 carry-over, not Phase 3) | 31 (11 PO + 20 SO) — not Phase 3 |
| Total Phase 3 detail cards (Sprint 5 target) | **30 FR + 46 NFR + 10 R + 38 T + ~62 UC L1+L2 + 49 nodes = 235** |

Cells formula: `~17 fields × N cards` = **~3,995 cells** (conservative; Sprint 5 will refine).

---

**End of RULE_FREEZE.md v1.0 — Phase 3 Rich Mode reconciliation frozen, Sprint 2 unblocked.**
