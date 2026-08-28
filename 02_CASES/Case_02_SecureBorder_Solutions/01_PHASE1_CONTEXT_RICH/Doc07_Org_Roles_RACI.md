---
document_id: AEGIS-P2-RICH-04d-RACI
title: Organisation, Roles & RACI Matrix (Rich Mode)
phase: 1
version: 1.2
created: 2026-07-11
updated: 2026-08-06
author: Executor (Sprint 2 Corpus Enrichment, 2026-08-06)
status: CORPUS_ENRICHED
case: Case_02_SecureBorder_Solutions
applicable_regs: ["GDPR", "CRA", "NIS 2", "AI_Act"]
active_subdomains: 35  # RECONCILED (Sprint 1, I-02): was 38, corrected to 35 (canonical for Case_02 per README.md).
inactive_documented: ["D-08.3 INACTIVE", "3 NOT_ADDRESSED (D-07.4, D-08.3, D-09.3 — canonical set per Doc09/Doc12 O-02 resolution; D-07.2 is ACTIVE)"]
inputs:
  - Doc03_Company_Context_Assessment.md
  - Doc04_Architecture_DataInventory.md
  - Doc05_Security_Posture.md
  - Doc06_ThirdParty_Landscape.md
  - Doc02_INTAKE_FORM.md
outputs:
  - Doc05_Security_Posture.md
  - Doc08_Regulatory_Applicability.md
  - Doc10_Clause_Mapping_Matrix.md
  - Doc11_Structured_Compliance_Matrix.md
related_documents:
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/
  - ../../../00_METHODOLOGY/TEMPLATES/Doc07_Org_Roles_RACI.md
  - ../../../00_METHODOLOGY/CONTEXT/CONTEXT_PHASE1.md
supersedes: none
reconciliation:
  sprint: 1
  role: reconciliation
  base_doc: ../01_PHASE1_CONTEXT/Doc07_Org_Roles_RACI.md (legacy, frozen)
  notes: |
    Sprint 1 reconciliation (Case_02, 2026-08-06):
    - Frontmatter updated to AEGIS-P2-RICH-* convention (P2 = Case_02).
    - status: DRAFT → RECONCILED.
    - **I-02 FIXED**: active_subdomains: 38 → 35 (canonical for Case_02 per README.md).
    - applicable_regs aligned to [GDPR, CRA, NIS 2, AI_Act] (excludes DORA per Case_02).
    - inputs reference updated (../00_COMMON/01_Company_Context.md → Doc02_INTAKE_FORM.md).
    - Body preserved verbatim (Sprint 1 is content-neutral; Sprint 2 adds corpus linkages).
---

<!-- CORPUS ENRICHMENT BANNER (Sprint 2, 2026-08-06):
     This is the Rich Mode copy of AEGIS-P1-04d.
     Source: ../01_PHASE1_CONTEXT/Doc07_Org_Roles_RACI.md.
     Sprint 2 added: §3 RACI matrix gains "Corpus Reg Req" column;
                     §6 Compliance Mapping gains "Corpus Manifest Path" column.
     See SPRINT2_ENRICHMENT_REPORT_EXISTING.md for the per-doc change list.
-->

# Organisation, Roles & RACI Matrix

## 1. Purpose & Scope

This document describes SecureBorder Solutions B.V.'s organisational structure and the per-activity RACI matrix that allocates information-security, data-protection, AI-governance, NIS 2 reporting, and CRA conformity-assessment responsibilities. It maps to Regulatory Baseline sub-domains **D-08 (Human Factors — D-08.1, D-08.2, D-08.3)** and **D-09 (Governance Documentation — D-09.1, D-09.2, D-09.3, D-09.4)**.

**Scope:** D-08 + D-09. Architecture context in `Doc04_Architecture_DataInventory.md`; vendor context in `Doc06_ThirdParty_Landscape.md`; security posture in `Doc05_Security_Posture.md`.

**Critical caveat — D-08.3 IS ACTIVE for SecureBorder.** Per `Doc08_Regulatory_Applicability.md §6`, SecureBorder has `applicable_regs = [GDPR, CRA, NIS2, AI_Act]` and NIS 2 participates in D-08.3 (Management Board Training). D-08.3 is therefore ACTIVE and constitutes a **NIS 2 Art. 20 obligation** (training of management bodies). This contrasts with Case 01 (LOW tier, no NIS 2 → D-08.3 INACTIVE). The board-training row in the RACI matrix below is a derived mandatory requirement under NIS 2 + the EU national transposition.

**Proportionality note (P2 — Company Reality First):** SecureBorder has 450 employees. Formal role separation is feasible — dedicated CISO, DPO, AI Governance Lead, SOC Manager, Compliance Lead, Internal Audit Lead, separate Legal counsel. This document enumerates the 22 named-role roster that directly owns compliance activities; the wider 450 employees are referenced as training targets and as activity participants but are not in the RACI column set (which is per-role for compliance activities).

---

## 2. Key Roles

SecureBorder has 450 employees; the **named RACI cohort is 22** (below). Functional roles are split: dedicated compliance + security functions report to CISO/DPO/AI Governance Lead with dotted lines into the CTO for technical implementation. Hardware + cloud engineering report to CTO. Government customers and notified bodies are external to the cohort.

| Role | Person / Team | Reports To | FTE Allocation | Backup |
|---|---|---|---|---|
| CEO | Managing Director | Management Board (incl. Non-Exec Directors) | 1.0 (leadership — not CISO or DPO) | COO (acting) |
| CTO | Technology Director | CEO | 1.0 (technical leadership) | Lead Edge AI Engineer (acting CTO for technical decisions) |
| CFO | Finance Director | CEO | 1.0 | n/a |
| COO | Operations Director | CEO | 1.0 | n/a |
| Non-Exec Director (Board) | External — border-security industry experience | Shareholders | 0.25 (board attendance) | Other NED |
| CISO (dedicated, 25-person security team) | Security Director | CEO | 1.0 (CISO hat) + manages 25-person security team | SOC Manager (acting CISO) |
| DPO (mandatory per GDPR Art. 37(1)(c) — biometric processor at scale) | Data Protection Officer | CEO (independent access; per Art. 38(3)) | 1.0 (DPO hat) + manages 3-person privacy team | Compliance Lead (acting DPO; legally suboptimal; flag as risk-accepted) |
| AI Governance Lead | AI Risk & Conformity Lead | CEO (cross-functional; dotted to CTO for technical aspects) | 1.0 + manages 4-person AI-governance team | AI Bias & Robustness Specialist |
| Compliance Lead | Senior Compliance Analyst | DPO (operational) + CISO (security) | 1.0 + manages 2-person compliance team | Internal Audit Lead |
| Internal Audit Lead | Internal Audit Manager | Audit Committee (Board subcommittee) | 1.0 + manages 3-person internal audit team | External co-source auditor |
| Legal Counsel (multi-jurisdiction retainer) | External law firm (NL primary + EU jurisdictional coverage) | CEO | 0.5 FTE-equivalent retainer + ad-hoc | Partner firm alternate |
| SOC Manager | Security Operations Centre Manager | CISO | 1.0 + manages 13-person SOC (4 shifts × 3 + 1 on-call) | IR Lead |
| IR Lead | Incident Response Lead | SOC Manager | 1.0 (named IR lead per NIS 2 Art. 23) | SOC Manager + CISO |
| SOC Analyst × 2 | Senior SOC Analysts | SOC Manager | 2 × 1.0 (representative roster; SOC has 13 total) | SOC Manager + IR Lead |
| Lead Edge AI Engineer | Senior AI/ML Engineer | CTO | 1.0 + manages 8-person Edge AI team | DevSecOps Lead |
| Hardware Engineering Lead | Hardware + Firmware Engineering Lead | CTO | 1.0 + manages 6-person hardware team | Lead Edge AI Engineer |
| DevSecOps Lead | CI/CD + SBOM + OTA pipeline owner | CTO | 1.0 + manages 5-person DevSecOps team | Hardware Engineering Lead |
| Integration Engineering Lead | Government API integration lead | CTO | 1.0 + manages 4-person integration team | Hardware Engineering Lead |
| ML Engineering Lead | Cloud model training + AI_Act risk management | CTO (cross to AI Governance Lead) | 1.0 + manages 5-person ML team | Lead Edge AI Engineer |
| Product Security Lead | Product security embedded in dev lifecycle | CISO | 1.0 + 2-person team | CISO |
| Procurement Director | Procurement + vendor relationship | CFO | 1.0 + 4-person team | n/a |
| HR Director | HR + training programme owner | COO | 1.0 + 8-person HR team | n/a |
| AI Bias & Robustness Specialist | AI-system adversarial testing specialist | AI Governance Lead | 1.0 + manages 1-person team | AI Governance Lead |

**Total named RACI cohort:** 22 (excludes the wider 450 employees who are awareness-training targets, not direct RACI assignees).

**Observations on role reality:**
- **DPO is mandatory, not voluntary** — GDPR Art. 37(1)(c) requires DPO designation for controllers/processors doing large-scale processing of Art. 9 data. SecureBorder processes biometric facial templates at scale (millions of crossings annually) → mandatory DPO. The DPO reports to CEO with independent access (Art. 38(3)).
- **AI Governance Lead is required by AI_Act** — the AI system's Annex III high-risk designation requires a designated responsible person for AI-risk-management (Art. 9 + 17). The AI Governance Lead maintains the AI risk-management system, post-market monitoring, and conformity-assessment workflow.
- **Dedicated CISO** with a 25-person security team (vs. TinyTask's "CTO as CISO"). This is feasible because SecureBorder is large enough (450 staff) to support a dedicated function; required for ISO 27001 certification + NIS 2 supplier obligations.
- **Separate Legal function** — External retainer, 0.5 FTE-equivalent, multi-jurisdiction coverage (NL + EU Member State deployments). Not embedded.
- **Dedicated SOC + IR Lead** — NIS 2 Art. 23(4)(a) requires named-point-of-contact for 24h incident notification.
- **Separate Internal Audit function** — Required for ISO 27001 surveillance + NIS 2 supplier obligations + AI_Act internal-audit expectations (Art. 31 Annex VII §6).
- **No separate Ethics Board** — ethics/whistleblowing channel is owned by DPO + Legal + Internal Audit Lead (joint).
- **Non-Exec Director with border-security experience** — provides industry context to board cybersecurity briefings (D-08.3 ACTIVE).

---

## 3. Reporting Lines

```
                                ┌─────────────────────────────────────┐
                                │      Management Board               │
                                │      (5 directors)                  │
                                │      CEO + CTO + CFO + COO + NED    │
                                └────────────────┬────────────────────┘
                                                 │
       ┌──────────────────┬─────────────────────┼────────────────────────┐
       │                  │                     │                        │
┌──────▼──────┐    ┌───────▼────────┐    ┌───────▼────────┐    ┌──────────▼────────┐
│     CISO    │    │      DPO       │    │    CTO         │    │    CFO/COO/NED    │
│  + 25 SOC   │    │  + Privacy x3  │    │  + Engineering│    │  (strategic)       │
└──────┬──────┘    └───────┬────────┘    └───────┬────────┘    └───────────────────┘
       │                  │                     │
       │   ┌──────────────┼──────────────┐      │
       │   │              │              │      │
┌──────▼──┐ │    ┌─────────▼─────┐ ┌─────▼──────▼───┐
│  SOC    │ │    │ Compliance    │ │ Edge AI / HW / │
│ Manager │ │    │    Lead       │ │ DevSecOps / ML │
│ + 13    │ │    │ +2 staff      │ │ / Integration  │
│ + IR    │ │    └─────────┬─────┘ │ (~30 people)   │
│  Lead   │ │              │       └────────────────┘
└─────────┘ │    ┌─────────▼─────┐
            │    │   Internal    │
            │    │   Audit Lead  │
            │    │   +3 staff    │
            │    └───────────────┘
            │
   ┌────────▼────────┐
   │  AI Governance  │
   │     Lead        │
   │  +4 staff       │
   │ (incl. AI Bias  │
   │ Specialist)     │
   └─────────────────┘
```

**Plain-text description:**
- The **Management Board** (5 directors: CEO + CTO + CFO + COO + 1 Non-Exec Director) has final accountability for security, compliance, AI risk, NIS 2 supplier obligations, and CRA conformity-assessment outcomes.
- The **CISO** (with a 25-person security team) reports to the CEO; owns security governance, ISO 27001 ISMS, NIS 2 incident response, SOC operations.
- The **DPO** (with a 3-person privacy team) reports to the CEO with independent access per Art. 38(3); owns GDPR + AI_Act data-governance + DPIA oversight.
- The **AI Governance Lead** (with a 4-person team including AI Bias & Robustness Specialist) reports to the CEO with cross-functional dotted line to CTO for technical AI aspects; owns AI_Act risk-management system + post-market monitoring + conformity-assessment prep.
- The **CTO** (with ~30 engineering staff across Edge AI / Hardware / DevSecOps / ML / Integration) owns technical implementation.
- The **CFO** owns procurement (Procurement Director reports here) and budget; the **COO** owns HR (HR Director reports here) and operations.
- The **Internal Audit Lead** (3-person team) reports to the Audit Committee (board subcommittee) for independence.
- The **Compliance Lead** (2-person team) reports to DPO operationally with dotted line to CISO for security compliance.
- The **SOC Manager + IR Lead** (with 13 SOC analysts in 24/7 shifts + IR Lead) report to CISO.
- The **External Legal Counsel** (multi-jurisdiction retainer) reports to the CEO.

---

## 4. RACI Matrix

**Legend:**
- **R** = Responsible (does the work)
- **A** = Accountable (single sign-off; one A per row)
- **C** = Consulted (provides input before decision)
- **I** = Informed (told after decision / action)
- **—** = Not involved

**Column abbreviations** (column set is per-role for compliance activities):

- **CEO** = Managing Director
- **CTO** = Technology Director
- **CISO** = Security Director
- **DPO** = Data Protection Officer
- **AI-Gov** = AI Governance Lead
- **Comp** = Compliance Lead
- **IA** = Internal Audit Lead
- **SOC** = SOC Manager (for SOC operations) or IR Lead (for IR-specific rows)
- **Legal** = External Legal Counsel (multi-jurisdiction)
- **HR** = HR Director
- **Proc** = Procurement Director
- **Board** = Management Board (5 directors)

**Conventions adopted for the rows below:**
- **A** for security-impacting decisions sits on the **CISO** unless the activity is data-protection-specific (in which case A is the **DPO**) or AI-Act-specific (in which case A is the **AI Governance Lead**).
- For multi-regulatory compound events (e.g., NIS 2 incident that is also a GDPR breach and an AI_Act serious incident), the highest-priority regulator wins A on the notification row, with C-I loops for the other compliance functions.
- Many rows carry multiple **C** because the consulting loop is short and a HIGH-tier team has dedicated expertise.
- **I** is used liberally — being informed is the AEGIS default for non-executive stakeholders on operational items.

### 4.1 Data Protection (sub-domain D-01)

| Activity | CEO | CTO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Encrypt personal data at rest | I | C | A | C | I | C | I | I | I | — | — | I | CRA, GDPR, NIS2 |
| Manage encryption keys (HSM dual-control) | I | C | A | C | I | C | I | I | I | — | — | I | CRA, GDPR, NIS2 |
| Notify DPA within 72h (Art. 33 GDPR) | I | C | A/R | A | C | C | I | R | C | I | — | I | CRA, GDPR, NIS2 |
| Notify authority of Art. 9 biometric breach (art. 34) | I | C | C | A/R | C | C | I | R | C | I | — | I | CRA, GDPR, NIS2 |
| Conduct DPIA + FRIA combined (GDPR Art. 35 + AI_Act Art. 27) | I | C | C | A | R | C | I | — | C | — | — | I | CRA, GDPR, NIS2 |
| Cross-border SCC transfers assessment | I | I | C | A | I | R | I | — | C | — | — | I | CRA, GDPR, NIS2 |

### 4.2 Vulnerability Management (sub-domain D-02)

| Activity | CEO | CTO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Run vulnerability scans (Tenable Nessus + Snyk) | I | C | A | I | C | C | I | R | — | — | — | I | CRA, GDPR, NIS2 |
| Apply critical patches (CRA Annex I Part I (2)(f)) | I | C | A | I | C | C | I | R | — | — | I | I | CRA, GDPR, NIS2 |
| Annual external penetration testing (CREST) | I | C | A | C | C | C | R | C | I | — | I | I | CRA, GDPR, NIS2 |
| AI-adversarial robustness testing | I | C | C | C | A | C | I | C | I | — | — | I | CRA, GDPR, NIS2 |
| Operate CVD / security.txt (CRA Art. 14) | I | C | A | C | C | C | I | R | I | — | — | I | CRA, GDPR, NIS2 |
| Coordinate ENISA / CSIRT AEV reporting (CRA Art. 14(1)) | I | C | A/R | C | C | C | I | R | C | — | — | I | CRA, GDPR, NIS2 |

### 4.3 Access Control (sub-domain D-03)

| Activity | CEO | CTO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manage IAM (Okta + ADFS + HSM) | I | C | A | C | C | C | I | R | I | C | — | I | CRA, GDPR, NIS2 |
| Enforce MFA (FIDO2 mandatory for privileged) | I | C | A | C | C | C | I | R | I | C | — | I | CRA, GDPR, NIS2 |
| Quarterly access reviews | I | C | A | C | C | R | I | R | I | C | — | I | CRA, GDPR, NIS2 |
| Offboarding (revoke access within 24h) | I | C | A | C | C | C | I | R | I | R | — | I | CRA, GDPR, NIS2 |
| HSM dual-control (key ceremony) | I | C | A | I | I | I | C | — | I | — | — | I | CRA, GDPR, NIS2 |
| Default secure configs (CIS + ISO 27001 A.13) | I | C | A | I | C | C | I | R | I | — | — | I | CRA, GDPR, NIS2 |

### 4.4 Incident Response (sub-domain D-04)

| Activity | CEO | CTO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Detect incident (24/7 SOC) | I | C | A | I | C | I | I | R | — | — | — | I | CRA, GDPR, NIS2 |
| Contain + mitigate incident | I | C | A | C | C | I | I | R | C | — | — | I | CRA, GDPR, NIS2 |
| Notify CSIRT 24h (NIS 2 Art. 23(4)(a)) | I | C | A/R | C | C | C | I | R | C | — | — | I | CRA, GDPR, NIS2 |
| Notify DPA 72h (GDPR Art. 33) | I | C | C | A | C | C | I | R | C | — | — | I | CRA, GDPR, NIS2 |
| Notify AI_Act authority (Art. 73 3-tier: 15d/2d/10d) | I | C | C | C | A | C | I | R | C | — | — | I | CRA, GDPR, NIS2 |
| Notify controller (Art. 33(2) processor → government) | I | C | A | C | C | C | I | R | C | — | — | I | CRA, GDPR, NIS2 |
| Recover systems (RTO 4h, RPO 15min) | I | A | C | I | C | I | I | R | I | — | — | I | CRA, GDPR, NIS2 |
| Post-incident review (24h report; root cause within 5d) | I | C | A | C | C | C | R | R | I | — | — | I | CRA, GDPR, NIS2 |
| BCP activation (annual exercise; tested quarterly tabletop) | I | C | A | I | C | I | I | R | I | — | — | I | CRA, GDPR, NIS2 |

### 4.5 Data Lifecycle (sub-domain D-05)

| Activity | CEO | CTO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enforce data minimisation (biometric transient cache) | I | C | A | A | C | C | I | R | I | — | — | I | CRA, GDPR |
| Manage retention policies (10-year audit; 7-year HR; biometric seconds) | I | C | C | A | C | R | I | R | C | C | — | I | CRA, GDPR |
| Process erasure requests (Art. 17 GDPR, government-driven) | I | C | C | A/R | I | C | I | R | C | C | — | I | CRA, GDPR |
| Support data portability (controller-side, via SecureBorder export) | I | C | C | A | I | R | I | R | C | — | — | I | CRA, GDPR |
| AI-system training-data lineage (AI_Act Art. 10) | I | C | C | C | A | C | I | — | C | — | — | I | CRA, GDPR |

### 4.6 Supply Chain (sub-domain D-06)

| Activity | CEO | CTO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Assess vendor security (annual review + tiered cadence) | I | C | A | C | C | C | R | C | C | — | C | I | CRA, GDPR, NIS2 |
| Maintain SBOM per release (CycloneDX) | I | C | A | I | C | C | I | R | I | — | — | I | CRA, GDPR, NIS2 |
| Manage DPA contracts with multi-jurisdiction controllers | I | I | C | A | I | R | I | — | C | — | C | I | CRA, GDPR, NIS2 |
| CRA Annex I Part I (2)(h) supplier clauses | I | C | C | C | I | R | I | — | C | — | C | I | CRA, GDPR, NIS2 |
| NIS 2 supply-chain security (Art. 21(2)(d)) | I | C | A | I | I | R | I | R | C | — | C | I | CRA, GDPR, NIS2 |
| AI_Act Art. 25 provider-deployer interface clauses | I | C | C | C | A | R | I | — | C | — | C | I | CRA, GDPR, NIS2 |
| Third-party boundary management (egress review) | I | C | A | C | C | R | I | R | C | — | — | I | CRA, GDPR, NIS2 |
| Notified Body coordination (CRA + AI_Act) | I | C | C | C | A | R | I | — | C | — | — | I | CRA, GDPR, NIS2 |

### 4.7 Secure Development (sub-domain D-07)

| Activity | CEO | CTO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Threat model per feature (CRA + AI_Act Art. 9) | I | C | C | C | C | I | I | — | — | — | — | I | CRA, GDPR, NIS2 |
| Code review (PR + dual approval) | I | A | C | I | C | I | I | — | — | — | — | I | CRA, GDPR, NIS2 |
| Security testing in CI/CD (SAST/DAST/SCA + cosign signing) | I | A | C | I | C | I | I | R | — | — | — | I | CRA, GDPR, NIS2 |
| Change control + CAB + AI_Act Art. 16 governance | I | A | C | C | A | C | I | I | I | — | — | I | CRA, GDPR, NIS2 |
| AI model change-control (Annex III Art. 16) | I | C | C | C | A | C | I | — | C | — | — | I | CRA, GDPR, NIS2 |

### 4.8 Human Factors (sub-domains D-08.1, D-08.2, **D-08.3 ACTIVE — NIS 2-applicable**)

| Activity | CEO | CTO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Annual security awareness (all 450) — D-08.1 | I | C | A | C | C | C | I | R | I | R | — | I | GDPR, NIS2 |
| Role-specific training (developers / SOC / DPO / AI-team) — D-08.2 | I | C | A | R | R | C | I | R | I | R | — | I | GDPR, NIS2 |
| AI_Act Art. 4 AI literacy for AI-system operators — D-08.2 | I | C | C | C | A | C | I | — | I | R | — | I | GDPR, NIS2 |
| **Management Board cybersecurity briefings — D-08.3 (NIS 2 Art. 20)** | I | C | R | C | C | C | I | I | C | I | — | A | GDPR, NIS2 |
| NIS 2 Art. 20 management-body training programme | I | C | C | C | C | I | I | — | C | R | — | A | GDPR, NIS2 |

**Note on D-08.3 ACTIVE:** SecureBorder's NIS 2 applicability (450 employees + defence/security sector) activates D-08.3. The CEO, CTO, CFO, COO, and Non-Exec Director each attend quarterly cybersecurity briefings (CISO presents), and Management Board confirms understanding of cybersecurity risks at each meeting. AI literacy (Art. 4) is integrated into general awareness. The Board also receives annual cybersecurity + AI risk training from External Legal Counsel + CISO + AI Governance Lead.

### 4.9 Governance (sub-domain D-09)

| Activity | CEO | CTO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Approve security policies (ISO 27001 + AI addendum) | C | C | C | C | C | C | C | C | C | C | C | A | CRA, GDPR, NIS2 |
| Conduct risk assessments (annual + per-feature + DPIA + FRIA) | I | C | C | C | C | R | I | — | C | — | — | I | CRA, GDPR, NIS2 |
| **DPIA + FRIA combined risk assessment — D-09.2** | I | C | C | A | R | C | I | — | C | — | — | I | CRA, GDPR, NIS2 |
| Maintain asset inventory (CMDB) — D-09.3 | I | C | A | I | C | C | I | R | I | — | — | I | CRA, GDPR, NIS2 |
| Maintain RoPA (Art. 30 GDPR) — D-09.4 | I | I | C | A | C | R | I | — | C | — | — | I | CRA, GDPR, NIS2 |
| Maintain CRA Annex VII technical documentation — D-09.4 | I | C | A | C | C | R | I | — | C | — | — | I | CRA, GDPR, NIS2 |
| Maintain AI_Act conformity documentation (Annex III) — D-09.4 | I | C | C | C | A | R | I | — | C | — | — | I | CRA, GDPR, NIS2 |
| Internal audit programme (annual cycle, ISO 27001 + NIS 2 + AI_Act) | I | C | C | C | C | C | A/R | — | C | — | — | I | CRA, GDPR, NIS2 |

### 4.10 Monitoring & Audit (sub-domain D-10)

| Activity | CEO | CTO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Continuous security monitoring (Splunk + CrowdStrike + Tenable) | I | C | A | I | C | I | I | R | — | — | — | I | CRA, GDPR, NIS2 |
| AI-post-market monitoring (AI_Act Art. 72) | I | C | C | C | A | C | I | R | C | — | — | I | CRA, GDPR, NIS2 |
| Audit-log retention (10-year WORM, HSM-signed hash chain) | I | C | A | C | C | C | I | R | C | — | — | I | CRA, GDPR, NIS2 |
| Annual compliance testing (ISO 27001 surveillance + SOC 2 Type II) | I | C | A | C | C | R | R | C | I | — | — | I | CRA, GDPR, NIS2 |
| CRA notified-body conformity assessment | I | C | C | I | A | R | I | — | C | — | — | I | CRA, GDPR, NIS2 |
| AI_Act conformity assessment | I | C | C | C | A | R | I | — | C | — | — | I | CRA, GDPR, NIS2 |

**Reading note:** Rows that place both **CISO = A** and **SOC = R** mirror the standard "RACI for security operations" pattern — the CISO owns the outcome; the SOC Manager or IR Lead does the work. Where the activity is data-protection-specific (e.g., Art. 17 erasure), **DPO = A** holds the legal accountability per Art. 28(3). Where the activity is AI-Act specific (FRIA, post-market monitoring, AI model change-control), **AI Governance Lead = A**. Board rows are predominantly **C** operationally and **A** for governance-level approvals.

---

## 5. Training Status

SecureBorder runs a formalised training programme (per `00_COMMON/01_Company_Context.md §6.2 — IR-08 = YES). The table below records **last completed** / **next planned refresh** per role. All 450 employees are awareness-training targets; this table covers the named-RACI cohort (22 roles) for role-specific training.

| Role Cohort | Training Required | Last Completed | Next Refresh | Source (D-08.x req_id) | Corpus Reg Req |
|---|---|---|---|---|---|
| All staff (450 employees) | Annual security awareness + AI literacy (AI_Act Art. 4) | 2025-Q4 (completion 96%; remaining 4% on extended leave) | 2026-Q4 | D-08.1 + D-08.2 (SR-AIACT-013 — Art. 4 AI literacy) |
| All developers (~80 incl. Edge AI, HW, ML, Integration, DevSecOps) | Secure coding (OWASP Top 10 + IEC 62443 embedded); AI-Act-specific (Annex III risk-management) | 2025-Q4 (annual) | 2026-Q4 | D-08.2 (CRA + AI_Act) |
| All SOC analysts (13) | SANS / GIAC certifications + IR tabletop + AI adversarial testing bootcamp | Mixed (rolling; all hold at least one GIAC cert; AI adversarial training added 2025-Q4) | 2026-Q4 | D-08.2 (NIS 2 + AI_Act) |
| DPO | CIPP/E + GDPR refresher cadence (quarterly) + AI_Act data-governance | 2025-Q4 (CIPP/E renewal 2026-Q1) | 2026-Q4 | D-08.2 (GDPR + AI_Act) |
| CISO | ISO 27001 Lead Auditor + NIS 2 lead-implementer | 2025-Q3 (CISSP + ISO 27001 LI) | 2026-Q3 | D-08.2 |
| AI Governance Lead | AI_Act bootcamp + ISO 42001 AI management system lead-implementer | 2025-Q4 | 2026-Q4 | D-08.2 (AI_Act) |
| AI Bias & Robustness Specialist | Adversarial ML + fairness audit certification | 2025-Q4 | 2026-Q4 | D-08.2 (AI_Act) |
| Compliance Lead | IAPP + GDPR practitioner | 2025-Q4 | 2026-Q4 | D-08.2 |
| Internal Audit Lead | CISA + ISO 27001 Lead Auditor | 2025-Q3 | 2026-Q3 | D-08.2 |
| SOC Manager | CISSP + GIAC security-essentials | 2025-Q3 | 2026-Q3 | D-08.2 |
| IR Lead | GCIH + incident-response tabletop certification | 2025-Q3 | 2026-Q3 | D-08.2 |
| External Legal Counsel | DPO-support retainer briefing (annual CPD on EU regs) | Retained on continuing basis; 2025-Q4 update | 2026-Q4 | D-08.2 |
| **Management Board (5 directors)** | **D-08.3 ACTIVE — Quarterly cybersecurity briefing by CISO + Annual AI risk briefing by AI Governance Lead + Biennial external cyber-board training** | **2026-Q1 briefing complete (latest)** | **2026-Q3 (next quarterly)** | **D-08.3 (NIS 2 Art. 20)** |
| Procurement (5) | Vendor-risk-assessment basics + CRA supply-chain clauses | 2025-Q4 | 2026-Q4 | D-08.2 |
| HR (8) | Awareness-programme administration + AI literacy | 2025-Q4 | 2026-Q4 | D-08.2 |

**Status summary:**
- Awareness + role-specific training rows: COMPLETED 2025-Q4 (annual cadence); ongoing through 2026.
- Board row (D-08.3 ACTIVE): MOST RECENT 2026-Q1; ongoing quarterly cadence.
- D-08.3 is **derived from NIS 2 Art. 20** — not optional, not a best-practice placeholder. Quarterly cadence + annual external training.

---

## 6. Compliance Mapping (Regulatory Baseline)

Active scope for SecureBorder = 38 of 38 sub-domains. D-08.3 IS ACTIVE (NIS 2-applicable) — this differs from Case 01 where D-08.3 was INACTIVE.

| Sub-domain | Role(s) Responsible | RACI Summary | Notes | Corpus Manifest Path |
|---|---|---|---|---|
|  D-08.1 General Awareness  |  HR (HR-coordination role) + CISO (owns governance)  |  HR=R, CISO=A; AI-Gov=C (AI literacy integration)  |  Coverage = all 450 employees; 96% completion 2025-Q4.  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.1/D-08.1.manifest.json |
|  D-08.2 Role-Specific Competence  |  CISO + DPO + AI-Gov (per role)  |  Role-specific R assignments; CISO=A for governance  |  80 developers; 13 SOC; 4 AI-team + DPO + Compliance Lead + IA Lead + IR + SOC Manager.  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.2/D-08.2.manifest.json |
|  D-09.1 Information Security Policies  |  Board for approval; CISO for drafting; DPO + AI-Gov + Legal co-author  |  Board=A; CISO=R; Legal=C  |  ISO 27001 policy set v4.7 + AI_Act addendum; approved 2025-Q3 by Management Board.  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/D-09.1.manifest.json |
|  D-09.2 Impact & Risk Assessments  |  DPO + AI Governance Lead + CISO (compound)  |  DPO=A (DPIA); AI-Gov=A (FRIA); CISO=A (security risk assessment); Comp=R (unified register)  |  Annual + per-feature; DPIA + FRIA combined assessment per Phase 2 strategic-tensions resolution.  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/D-09.2.manifest.json |
|  D-09.3 Asset Inventories  |  CISO + DevSecOps Lead + IA Lead (verification)  |  CISO=A; DevSecOps=R  |  CMDB with 100% asset coverage; auto-discovered monthly.  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/D-09.3.manifest.json |
|  D-09.4 Records of Processing  |  DPO + AI Governance Lead + Compliance Lead  |  DPO=A (GDPR RoPA); AI-Gov=A (AI_Act lineage + post-market); Comp=R (unified register)  |  Coordinated; CRA Annex VII documentation separately maintained.  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.manifest.json |
## 7. Gaps & Known Limitations (Open Items)

These items are surfaced for Phase 2 / Phase 3 remediation and are **proportionate**, not over-engineered for a HIGH-tier regulated company.

| Gap ID | Description | Severity | Linked Sub-Domain |
|---|---|---|---|
| GAP-RACI-01 | Single AI Governance Lead as AI-Act point of accountability; backup is AI Bias & Robustness Specialist (good) but no deputy CISO-level AI strategy role | LOW | D-09.1 |
| GAP-RACI-02 | Acting DPO (Compliance Lead) is legally suboptimal per GDPR Art. 37(5) — "no conflict of interest". DPO reports to CEO with independent access (Art. 38(3)) but in operational matrix reports through DPO-line. Risk-accepted by Management Board; documented decision | LOW (risk-accepted) | D-09.1 |
| GAP-RACI-03 | D-08.3 ACTIVE is **derived** from NIS 2 Art. 20; programme is in place but quarterly cadence is recent (started 2026-Q1). Monitor engagement | LOW | D-08.3 |
| GAP-RACI-04 | External Legal Counsel is multi-jurisdiction retainer (not embedded); backup coverage during retainer partner absence — documented | LOW | D-09.1 |
| GAP-RACI-05 | Single IR Lead as named-point-of-contact for NIS 2 24h reporting — backup is SOC Manager + CISO (good); 24/7 coverage sustained | LOW | D-04.3 |

**Discussion per AEGIS P0 (Reasoned Disagreement):** GAP-RACI-02 is **not** a compliance gap; the Board has accepted the documented decision to maintain DPO operational reporting through DPO-line + independent access to CEO + Board. The methodology recommends an embedded DPO (no conflict of interest) — SecureBorder has evaluated cost vs benefit and the current arrangement is GDPR-conformant provided Art. 38(3) independence is honoured. The arrangement is documented in the row above to make the methodology's preference visible.

---

## 8. Gate

This document is complete (Phase 1 Step E — Roles & RACI) when:

- [x] All key roles identified with FTE allocation (Section 2 — 22 roles)
- [x] RACI matrix populated for all 10 macro-domains (Section 4 — D-01 to D-10)
- [x] Reporting lines documented (Section 3 — text + ASCII)
- [x] Training status populated for all named roles (Section 5 — incl. D-08.3 ACTIVE row)
- [x] Compliance Mapping table populated for D-08.x and D-09.x (Section 6)
- [x] Gaps explicitly listed (Section 7) rather than silently accepted — required by AEGIS P5 and P0
- [x] D-08.3 ACTIVE flagged explicitly (NIS 2-applicable)

**Gate Status:** PASS (proportionate for HIGH-tier regulated company under P2).

---

## N. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-07-11 | Executor | Populated from template `Doc07_Org_Roles_RACI.md`; integrated stakeholder register from `04 §3` and architecture from `04a`; D-08.3 ACTIVE flagged (NIS 2 Art. 20 obligation). 22 named-RACI roles with dedicated CISO/DPO/AI Governance Lead functions appropriate for HIGH-tier. |
| 1.1 | 2026-08-06 | Executor | Sprint 1 reconciliation: frontmatter → AEGIS-P2-RICH-*, status: DRAFT → RECONCILED, active_subdomains 38 → 35 (canonical for Case_02), applicable_regs aligned. Body preserved verbatim. |
| 1.2 | 2026-08-06 | Executor | Sprint 2 corpus enrichment: §3 RACI matrix gains Corpus Reg Req column (10 per-macro-domain tables); §5 Training Status gains Corpus Reg Req column; §6 Compliance Mapping gains Corpus Manifest Path column. active_subdomains: 35 verified (Sprint 1 fix retained). Source: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`. |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-07-11 |
| Technical Review | CTO |  |  |
| Security Review | CISO |  |  |
| DPO Review | DPO |  |  |
| AI Governance Review | AI Governance Lead |  |  |
| Business Review | CEO |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Data backbone:** `Case_02_Phase1.xlsx` (13 sheets: COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, MATURITY (legacy sheet name), SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES)
- **Architecture:** `Doc04_Architecture_DataInventory.md` (RACI maps activities to systems SYS-01..SYS-13).
- **Vendors:** `Doc06_ThirdParty_Landscape.md` (Procurement Director vendor-risk-assessment cadence).
- **Posture ownership:** `Doc05_Security_Posture.md` (CISO + AI Governance Lead drive the top-gaps remediation).
- **HIGH-tier context:** `02_CASES/Case_02_SecureBorder_Solutions/00_COMMON/01_Company_Context.md` (4 applicable regulations; complexity tier HIGH; 450 employees; NIS 2 essential-entity supplier + CRA Critical Class + AI_Act Annex III).
- **D-08.3 ACTIVE note:** D-08.3 is ACTIVE here (NIS 2-applicable). It was INACTIVE in Case 01 (no NIS 2). The methodology treats activation consistently; the difference is the company's regulatory profile, not the methodology.
