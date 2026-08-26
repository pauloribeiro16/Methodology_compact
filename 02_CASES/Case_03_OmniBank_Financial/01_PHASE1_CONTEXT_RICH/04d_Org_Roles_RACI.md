---
document_id: AEGIS-P3-RICH-04d-RACI
title: Organisation, Roles & RACI Matrix (Rich Mode)
phase: 1
version: 1.2
created: 2026-07-11
updated: 2026-08-06
author: Executor (Sprint 1 reconciliation copy)
status: CORPUS_ENRICHED
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
inactive_documented: []
inputs:
  - 04_Company_Context_Assessment.md
  - 04a_Architecture_DataInventory.md
  - 04b_Security_Posture.md
  - 04c_ThirdParty_Landscape.md
  - 01_INTAKE_FORM.md
outputs:
  - 04b_Security_Posture.md
  - 05_Regulatory_Applicability.md
  - 06_Clause_Mapping_Matrix.md
  - 07_Structured_Compliance_Matrix.md
related_documents:
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/
  - ../../../00_METHODOLOGY/TEMPLATES/04d_Org_Roles_RACI.md
  - ../../../00_METHODOLOGY/CONTEXT/CONTEXT_PHASE1.md
sibling_of: ../01_PHASE1_CONTEXT/04d_Org_Roles_RACI.md
reconciliation_notes:
  - "Sprint 1 (2026-08-06): Copied from 01_PHASE1_CONTEXT/04d_Org_Roles_RACI.md → Rich folder; frontmatter migrated to AEGIS-P3-RICH-* prefix; status DRAFT → RECONCILED; applicable_regs normalized to [GDPR, CRA, NIS 2, DORA, AI Act] (was [GDPR, NIS2, CRA, DORA, AI_Act] in legacy, normalization to canonical order); active_subdomains confirmed = 38. D-08.3 (Management Board Training) ACTIVE for Case_03 (dual NIS 2 Art. 20 + DORA Art. 5 obligation) — preserved. Sprint 0.6 DORA-specific roles (CRO, DORA ICT Risk Officer) registered in body. Body unchanged."
---

<!-- CORPUS_ENRICHED (Sprint 2, 2026-08-06): Enrichment with Corpus Reg Req column in §4 RACI tables + Corpus Manifest Path column in §6 Compliance Mapping.
Replaces RECONCILED comment. Document copied from legacy 01_PHASE1_CONTEXT/04d_Org_Roles_RACI.md to Rich folder.
Changes: (a) document_id migrated to AEGIS-P3-RICH-04d-RACI; (b) status DRAFT → RECONCILED;
(c) applicable_regs normalized from [GDPR, NIS2, CRA, DORA, AI_Act] to [GDPR, CRA, NIS 2, DORA, AI Act] (canonical order, matches all other Rich docs);
(d) active_subdomains: 38 verified (Case_03 MAX — D-08.3 ACTIVE under dual NIS 2 Art. 20 + DORA Art. 5);
(e) Sprint 0.6 DORA-specific roles registered: CRO (Chief Risk Officer), DORA ICT Risk Officer, DORA Operational Resilience Lead.
Sprint 2 (2026-08-06): §4 RACI tables extended with Corpus Reg Req column (regulatory requirements from corpus); §6 Compliance Mapping table extended with Corpus Manifest Path column. status RECONCILED → CORPUS_ENRICHED.
-->

---

# Organisation, Roles & RACI Matrix

## 1. Purpose & Scope

This document describes OmniBank Financial Systems S.A.'s organisational structure and the per-activity RACI matrix that allocates information-security, data-protection, AI-governance, DORA ICT-risk, NIS 2 reporting, CRA mobile-app conformity-assessment, and AI Act Annex III responsibilities. It maps to Regulatory Baseline sub-domains **D-08 (Human Factors — D-08.1, D-08.2, D-08.3)** and **D-09 (Governance Documentation — D-09.1, D-09.2, D-09.3, D-09.4)**.

**Scope:** D-08 + D-09. Architecture context in `04a_Architecture_DataInventory.md`; vendor context in `04c_ThirdParty_Landscape.md`; security posture in `04b_Security_Posture.md`.

**Critical caveat — D-08.3 IS ACTIVE for OmniBank.** Per `05_Regulatory_Applicability.md §6`, OmniBank has `applicable_regs = [GDPR, NIS2, CRA, DORA, AI_Act]` and BOTH NIS 2 (Art. 20) AND DORA (Art. 5 management liability) participate in D-08.3 (Management Board Training). D-08.3 is therefore ACTIVE under a **dual NIS 2 Art. 20 + DORA Art. 5 obligation**. This contrasts with Case 01 (LOW tier, no NIS 2 → D-08.3 INACTIVE) and Case 02 (HIGH tier, NIS 2 only → D-08.3 ACTIVE under NIS 2). The board-training row in the RACI matrix below is a derived mandatory requirement under NIS 2 + DORA.

**Proportionality note (P2 — Company Reality First):** OmniBank has 5,000+ employees. Formal role separation is feasible — dedicated CISO, DPO, CRO, AI Governance Lead, CSIRT Lead, Internal Audit Lead, separate Compliance function, separate Legal function. This document enumerates the ~38 named-role roster that directly owns compliance activities; the wider 5,000+ employees are referenced as training targets and as activity participants but are not in the RACI column set (which is per-role for compliance activities).

---

## 2. Key Roles

OmniBank has 5,000+ employees; the **named RACI cohort is ~38** (below). Functional roles are split: dedicated compliance + security + risk + AI-governance functions report to CRO/CISO/DPO/AI Governance Lead with dotted lines into the CTO for technical implementation. Mainframe + cloud engineering + payments report to CTO. Government regulators, card networks, and SWIFT are external to the cohort.

| Role | Person / Team | Reports To | FTE Allocation | Backup |
|---|---|---|---|---|---|
| CEO | Vorstandsvorsitzender (CEO) | Management Board (incl. Non-Exec Directors) | 1.0 (leadership — not CISO or DPO) | CFO (acting) |
| CTO | Technologievorstand | CEO | 1.0 (technical leadership) | Lead Cloud Engineering (acting CTO for technical decisions) |
| CFO | Finanzvorstand | CEO | 1.0 | n/a |
| CRO (Chief Risk Officer) | Chief Risk Officer | CEO | 1.0 + manages 35-person risk organisation (credit risk + market risk + operational risk + DORA ICT risk) | Deputy CRO |
| COO | Operating Vorstand | CEO | 1.0 | n/a |
| Non-Exec Directors (Board) | 3 external — banking, technology, AI ethics | Shareholders | 0.25 (board attendance each) | Other NEDs |
| CISO (dedicated, 100-person security org) | Chief Information Security Officer | CEO | 1.0 (CISO hat) + manages 100-person security team | SOC Manager (acting CISO) |
| DPO (mandatory per GDPR Art. 37(1)(b)) | Datenschutzbeauftragter | CEO (independent access per Art. 38(3)) | 1.0 (DPO hat) + manages 8-person privacy team | Deputy DPO (legally suboptimal but Art. 38(3) independence preserved) |
| AI Governance Lead | Chief AI Governance Officer | CEO (cross-functional; dotted to CTO for technical aspects) | 1.0 + manages 10-person AI-governance team (incl. AI Bias & Robustness Specialist, FRIA Lead, AI Post-Market Monitoring Lead) | Deputy AI Governance Lead |
| Compliance Lead (BaFin/ECB liaison) | Senior Compliance Manager | CRO (operational) + CEO (regulator liaison) | 1.0 + manages 8-person compliance team | Compliance Manager (BaFin liaison) |
| Internal Audit Lead | Internal Audit Director | Audit Committee (Board subcommittee) | 1.0 + manages 6-person internal audit team | External co-source auditor |
| Legal Counsel (multi-jurisdiction) | In-house legal team + external retainers | CEO | 2.0 FTE-equivalent in-house + multi-jurisdiction external retainer | Partner firm alternate |
| SOC Manager | Security Operations Centre Manager | CISO | 1.0 + manages 24-person SOC (4 shifts × 6 + 1 on-call) | IR Lead |
| IR Lead / CSIRT Lead | Incident Response Lead | SOC Manager | 1.0 (named IR lead per NIS 2 Art. 23; CSIRT for DORA Art. 17-19) | SOC Manager + CISO |
| SOC Analyst × 2 | Senior SOC Analysts | SOC Manager | 2 × 1.0 (representative; SOC has 24 total) | SOC Manager + IR Lead |
| Lead Mainframe Engineer | Senior mainframe + legacy enterprise database engineer | CTO | 1.0 + manages 8-person mainframe team | DevSecOps Lead |
| Lead Cloud Engineering | Senior Cloud Architect | CTO | 1.0 + manages 15-person cloud engineering team | DevSecOps Lead |
| Lead Payments Engineer | Senior Payments Engineer | CTO | 1.0 + manages 6-person payments team | Lead Mainframe Engineer |
| DevSecOps Lead | CI/CD + SBOM + OTA pipeline owner | CTO | 1.0 + manages 8-person DevSecOps team | Lead Cloud Engineering |
| Lead Mobile App Engineer | Senior Mobile Engineer (iOS + Android) | CTO | 1.0 + manages 10-person mobile team | DevSecOps Lead |
| Lead AI/ML Engineer (OmniScore) | Senior ML Engineer | CTO (cross to AI Governance Lead) | 1.0 + manages 12-person ML team | AI Governance Lead |
| Product Security Lead | Product security embedded in dev lifecycle | CISO | 1.0 + 5-person team | CISO |
| Fraud Detection Lead | Head of Financial Crime (AML/KYC) | CRO | 1.0 + manages 20-person financial crime team | Compliance Lead |
| Procurement Director | Procurement + vendor relationship | CFO | 1.0 + 8-person procurement team | n/a |
| HR Director | HR + training programme owner | COO | 1.0 + 12-person HR team | n/a |
| Risk Management Lead (DORA ICT Risk) | DORA ICT Risk Manager | CRO | 1.0 + manages 8-person DORA ICT risk team | Deputy CRO |
| AI Bias & Robustness Specialist | AI-system adversarial testing + fairness audit | AI Governance Lead | 1.0 + manages 3-person team | AI Governance Lead |
| FRIA Lead | Fundamental Rights Impact Assessment Lead (AI Act Art. 27) | AI Governance Lead | 1.0 | AI Governance Lead |
| AI Post-Market Monitoring Lead | AI Act Art. 72 post-market monitoring | AI Governance Lead | 1.0 + manages 2-person team | AI Governance Lead |
| Payments Operations Manager | SEPA + Card operations + RTGS | COO (operational) + CRO (risk) | 1.0 + manages 12-person team | Lead Payments Engineer |
| Treasury Operations Manager | Treasury + Correspondent Banking + SWIFT | CFO | 1.0 + manages 8-person team | CRO |
| Branch Operations Manager | 1,200 branches nationwide | COO | 1.0 + manages 25-person regional team | n/a |
| Contact Centre Manager | Customer Service operations | COO | 1.0 + manages 80-person team | n/a |
| BaFin Liaison Officer | Regulator-facing role | Compliance Lead | 1.0 | Compliance Lead |
| ECB Liaison Officer | ECB/SSM regulator-facing | CRO (operational) + CEO (strategic) | 0.5 FTE-equivalent | CRO |

**Total named RACI cohort:** ~38 (excludes the wider 5,000+ employees who are awareness-training targets, not direct RACI assignees).

**Observations on role reality:**
- **CRO is a key role for OmniBank** — DORA Art. 5 puts ICT risk under CRO; DORA Art. 28-30 ICT third-party register is owned by CRO. CRO is the second-most senior risk owner after CEO.
- **DPO is mandatory, not voluntary** — GDPR Art. 37(1)(b) requires DPO designation for controllers doing large-scale systematic monitoring of data subjects (financial transaction monitoring, credit scoring). OmniBank does both at scale → mandatory DPO.
- **AI Governance Lead is required by AI Act** — OmniScore AI Platform is Annex III high-risk AI; Art. 9 risk-management system + Art. 17 quality management + Art. 26 deployer obligations require designated AI governance function.
- **Dedicated CISO with 100-person security team** (vs. Case 02's 25-person). Required for ISO 27001 + documented third-party security attestation + DORA Art. 6 ICT risk + AI Act Art. 15 cybersecurity + NIS 2 24/7 SOC.
- **In-house Legal Counsel** (2.0 FTE) + multi-jurisdiction external retainers (BaFin/ECB/EU coverage). In-house has dedicated Legal team for DORA + GDPR + AI Act + CRA contract templates.
- **Dedicated SOC + CSIRT** — 24/7 SOC + named CSIRT Lead per NIS 2 Art. 23 + DORA Art. 17-19.
- **Dedicated DORA ICT Risk team** (8 people under CRO) — DORA Art. 5-16 ICT risk management framework requires dedicated function.
- **Dedicated AI team** — 12 ML engineers + 10 AI governance team = 22 people working on OmniScore AI Platform.
- **Separate Internal Audit function** — Required for ISO 27001 + documented third-party security attestation + DORA Art. 24 TLPT + MaRisk AT 9 + AI Act internal audit expectations.
- **Non-Exec Directors with banking, technology, AI ethics backgrounds** — provides industry + technical + ethical context to board briefings.
- **Dedicated BaFin + ECB Liaison Officers** — BaFin-supervised entity requires dedicated regulator-facing roles.

---

## 3. Reporting Lines

```
                                 ┌─────────────────────────────────────┐
                                 │      Management Board               │
                                 │      (8 directors)                   │
                                 │      CEO + CTO + CFO + CRO + COO +   │
                                 │      CISO + 3 Non-Exec Directors     │
                                 └────────────────┬────────────────────┘
                                                  │
       ┌──────────────────┬─────────────────────┼────────────────────────┐
       │                  │                     │                        │
┌──────▼──────┐    ┌───────▼────────┐    ┌───────▼────────┐    ┌──────────▼────────┐
│    CISO     │    │     DPO        │    │      CRO       │    │ AI Governance     │
│ +100 SOC/IR │    │  + Privacy x8  │    │ + 35 Risk +    │    │    Lead           │
│  +CSIRT     │    │                │    │ 8 DORA ICT Risk│    │ + 10 AI team      │
└──────┬──────┘    └───────┬────────┘    └───────┬────────┘    └──────────┬────────┘
       │                  │                     │                        │
       │   ┌──────────────┼──────────────┐      │                        │
       │   │              │              │      │                        │
┌──────▼──┐ │    ┌─────────▼─────┐ ┌─────▼──────▼───┐         ┌──────────▼────────┐
│  SOC    │ │    │ Compliance    │ │ Fraud + AML    │         │   AI/ML Team      │
│ Manager │ │    │    Lead       │ │ Detection Lead │         │  (12 ML +         │
│ + 24    │ │    │ +8 staff +    │ │ +20 staff     │         │  Bias & Robustness│
│ + IR    │ │    │ BaFin + ECB   │ │                │         │  + FRIA Lead      │
│  Lead   │ │    │ Liaison       │ │                │         │  + Post-Market)   │
└─────────┘ │    └─────────┬─────┘ └────────────────┘         └───────────────────┘
            │              │
            │    ┌─────────▼─────┐
            │    │   Internal    │
            │    │   Audit Lead  │
            │    │   +6 staff    │
            │    └───────────────┘
            │
    ┌───────▼─────────┐
    │     CTO         │
    │  + Engineering  │
    │  (Mainframe +   │
    │   Cloud +       │
    │   Payments +    │
    │   DevSecOps +   │
    │   Mobile +      │
    │   ~60 people)   │
    └─────────────────┘
```

**Plain-text description:**
- The **Management Board** (8 directors: CEO + CTO + CFO + CRO + COO + CISO + 3 Non-Exec Directors) has final accountability for security, compliance, AI risk, DORA ICT risk + Art. 5 management liability, NIS 2 supplier obligations, AI Act conformity assessment, and CRA mobile-app conformity.
- The **CRO** (with a 35-person risk organisation + 8-person DORA ICT Risk team) reports to the CEO; owns DORA Art. 5-16 ICT risk management framework + Art. 28-30 ICT third-party register + financial-sector risk (Basel + MaRisk).
- The **CISO** (with a 100-person security team including 24 SOC + IR Lead) reports to the CEO; owns security governance + ISO 27001 + documented third-party security attestation + NIS 2 incident response + SOC operations + IR + CSIRT.
- The **DPO** (with an 8-person privacy team) reports to the CEO with independent access per Art. 38(3); owns GDPR + AI Act data-governance + DPIA oversight.
- The **AI Governance Lead** (with a 10-person team including AI Bias & Robustness Specialist, FRIA Lead, AI Post-Market Monitoring Lead) reports to the CEO with cross-functional dotted line to CTO for technical AI aspects; owns AI Act risk-management system + post-market monitoring + conformity-assessment prep.
- The **CTO** (with ~60 engineering staff across Mainframe + Cloud + Payments + DevSecOps + Mobile) owns technical implementation.
- The **CFO** owns procurement (Procurement Director reports here) and treasury + correspondent banking.
- The **COO** owns HR (HR Director reports here), branch operations (1,200 branches), contact centre, and payments operations.
- The **Internal Audit Lead** (6-person team) reports to the Audit Committee (board subcommittee) for independence.
- The **Compliance Lead** (8-person team + BaFin + ECB Liaison Officers) reports to CRO operationally; regulator-facing role.
- The **External Legal Counsel** (in-house 2.0 FTE + multi-jurisdiction retainer) reports to the CEO.
- The **Fraud Detection Lead** (20-person team) reports to CRO for AML/KYC risk and to COO for operations.
- The **Risk Management Lead (DORA ICT Risk)** (8-person team) reports to CRO; owns DORA Art. 5-16 ICT risk management.

---

## 4. RACI Matrix

**Legend:**
- **R** = Responsible (does the work)
- **A** = Accountable (single sign-off; one A per row)
- **C** = Consulted (provides input before decision)
- **I** = Informed (told after decision / action)
- **—** = Not involved

**Column abbreviations** (column set is per-role for compliance activities):

- **CEO** = Chief Executive Officer (Vorstandsvorsitzender)
- **CTO** = Chief Technology Officer
- **CRO** = Chief Risk Officer
- **CISO** = Chief Information Security Officer
- **DPO** = Data Protection Officer (Datenschutzbeauftragter)
- **AI-Gov** = AI Governance Lead
- **Comp** = Compliance Lead (BaFin/ECB liaison)
- **IA** = Internal Audit Lead
- **SOC** = SOC Manager (for SOC operations) or IR Lead (for IR-specific rows)
- **Legal** = In-house Legal + multi-jurisdiction external counsel
- **HR** = HR Director
- **Proc** = Procurement Director
- **DORA-Risk** = DORA ICT Risk Manager
- **Fraud** = Fraud Detection Lead
- **Board** = Management Board (8 directors)

**Conventions adopted for the rows below:**
- **A** for security-impacting decisions sits on the **CISO** unless the activity is data-protection-specific (in which case A is the **DPO**), risk-specific (CRO), AI-Act-specific (AI Governance Lead), or fraud-specific (Fraud Detection Lead).
- For multi-regulatory compound events (e.g., DORA major incident that is also a GDPR personal-data breach + AI Act serious-incident + CRA active-exploitation + NIS 2 significant incident), the **highest-priority regulator wins A on the notification row**, with C-I loops for the other compliance functions. DORA RTS 4h takes priority over NIS 2 24h over CRA 24h over GDPR 72h over AI Act 15d.
- Many rows carry multiple **C** because the consulting loop is short and a MAXIMUM-tier team has dedicated expertise.
- **I** is used liberally — being informed is the AEGIS default for non-executive stakeholders on operational items.

### 4.1 Data Protection (sub-domain D-01)

| Activity | CEO | CTO | CRO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | DORA-Risk | Fraud | Board | Corpus Reg Req (corpus articles) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Encrypt personal data at rest | I | C | I | A | C | I | C | I | I | I | — | — | C | I | I | GDPR Art. 21(1), Art. 25(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(1), Art. 6 chapeau + (a) / DORA Art. 21(1)+(2), Art. 25(1) |
| Manage encryption keys (HSM dual-control) | I | C | I | A | C | I | C | I | I | I | — | — | C | I | I | GDPR Art. 25(1), Art. 32(1) / NIS2 Art. 25(1) / CRA Art. 6 chapeau + (a), Art. 6(a) proviso / DORA Art. 25(1), Art. 4(1) |
| Notify DPA within 72h (Art. 33 GDPR) | I | C | I | A/R | A | C | C | I | R | C | I | — | C | I | I | GDPR Art. 11(1), Art. 14(5)(b) / NIS2 Art. 23(1) ¶1, Art. 23(1) ¶2 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Notify authority of large-scale breach (Art. 34) | I | C | C | C | A/R | C | C | I | R | C | I | — | C | I | I | GDPR Art. 11(1), Art. 14(5)(b) / NIS2 Art. 23(1) ¶1, Art. 23(1) ¶2 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Conduct DPIA + FRIA combined (GDPR Art. 35 + AI Act Art. 27) | I | C | C | C | A | R | C | I | — | C | — | — | C | — | I | GDPR Art. 13(2)(f), Art. 21(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(1), Art. 13(2) sentence 1 / DORA Art. 10(1), Art. 10(2)+(3) |
| Cross-border SCC transfers assessment | I | I | C | C | A | I | R | I | — | C | — | — | C | — | I | GDPR Art. 15(1), Art. 15(3) |
| DORA Art. 5 ICT risk framework (data protection overlay) | I | C | A | C | C | C | C | I | C | I | — | — | R | C | I | GDPR Art. 21(1), Art. 23(1) / NIS2 Art. 20 chapeau, Art. 20(1) sentence 1 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |

### 4.2 Vulnerability Management (sub-domain D-02)

| Activity | CEO | CTO | CRO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | DORA-Risk | Fraud | Board | Corpus Reg Req (corpus articles) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Run vulnerability scans (managed vulnerability scanning + automated dependency scanner + mainframe vulnerability analysis) | I | C | I | A | I | C | C | I | R | — | — | — | C | — | I | GDPR Art. 21(1), Art. 21(3) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 13(3) sentence 1, Art. 7(2)(a) / DORA Art. 10(1), Art. 10(2)+(3) |
| Apply critical patches (CRA + DORA Art. 8) | I | C | C | A | I | C | C | I | R | — | — | I | C | — | I | CRA Art. 13(6) sentence 1, Art. 13(8) sentence 1 |
| Annual external penetration testing (CREST) | I | C | C | A | C | C | C | R | C | I | — | I | C | — | I | DORA Art. 24(1)+(2) chapeau, Art. 25(1) |
| AI-adversarial robustness testing (OmniScore) | I | C | C | C | C | A | C | I | C | I | — | — | C | — | I | DORA Art. 24(1)+(2) chapeau, Art. 25(1) |
| DORA Art. 24 TLPT every 3 years | I | C | C | A | C | C | C | R | C | C | — | C | R | C | I | DORA Art. 24(1)+(2) chapeau, Art. 25(1) |
| Operate CVD / security.txt (CRA Art. 14) | I | C | I | A | C | C | C | I | R | I | — | — | C | — | I | NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 13(17), Art. 13(8) sentence 2 |
| Coordinate BSI/ENISA AEV reporting (CRA Art. 14(1)) | I | C | I | A/R | C | C | C | I | R | C | — | — | C | — | I | NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 13(17), Art. 13(8) sentence 2 |

### 4.3 Access Control (sub-domain D-03)

| Activity | CEO | CTO | CRO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | DORA-Risk | Fraud | Board | Corpus Reg Req (corpus articles) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manage IAM (managed identity service + on-prem identity federation + mainframe access control) | I | C | I | A | C | C | C | I | R | I | C | — | C | — | I | GDPR Art. 11(1), Art. 12(6) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 6 chapeau + (a), Art. 7(1) sentence 1 / DORA Art. 10(1), Art. 10(2)+(3) |
| Enforce MFA (strong cryptographic hardware key mandatory for privileged; PSD2 SCA for customer) | I | C | I | A | C | C | C | I | R | I | C | — | C | — | I | GDPR Art. 21(1) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / DORA Art. 21(1)+(2) |
| Quarterly access reviews | I | C | C | A | C | C | R | I | R | I | C | — | C | — | I | GDPR Art. 21(1), Art. 28(3) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 6 chapeau + (a), Art. 6(a) proviso / DORA Art. 21(1)+(2), Art. 28 chapeau + (1) + (2) |
| Offboarding (revoke access within 24h) | I | C | I | A | C | C | C | I | R | I | R | — | C | — | I | GDPR Art. 11(1), Art. 12(6) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 6 chapeau + (a), Art. 7(1) sentence 1 / DORA Art. 10(1), Art. 10(2)+(3) |
| HSM dual-control (key ceremony) | I | C | I | A | I | I | I | C | — | I | — | — | C | — | I | GDPR Art. 25(1), Art. 32(1) / NIS2 Art. 25(1) / CRA Art. 6 chapeau + (a), Art. 6(a) proviso / DORA Art. 25(1), Art. 4(1) |
| Managed PAM for 250 privileged accounts | I | C | I | A | C | C | C | C | R | I | — | I | C | — | I | GDPR Art. 21(1), Art. 28(3) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 6 chapeau + (a), Art. 6(a) proviso / DORA Art. 21(1)+(2), Art. 28 chapeau + (1) + (2) |
| Default secure configs (hardened-default baseline + ISO 27001 + mainframe secure defaults) | I | C | I | A | I | C | C | I | R | I | — | — | C | — | I | GDPR Art. 25(1), Art. 25(2) / CRA Art. 6 chapeau + (a), Art. 6(a) proviso |

### 4.4 Incident Response (sub-domain D-04)

| Activity | CEO | CTO | CRO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | DORA-Risk | Fraud | Board | Corpus Reg Req (corpus articles) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Detect incident (24/7 SOC + CSIRT) | I | C | C | A | I | C | I | I | R | — | — | — | C | C | I | GDPR Art. 10, Art. 21(1) / NIS2 Art. 21(1) sentence 1, Art. 21(2) chapeau / CRA Art. 6 chapeau + (a) / DORA Art. 17(1), Art. 21(1)+(2) |
| Contain + mitigate incident | I | C | C | A | C | C | I | I | R | C | — | — | C | C | I | GDPR Art. 21(1), Art. 21(3) / NIS2 Art. 20 chapeau, Art. 21(1) sentence 1 / CRA Art. 13(21), Art. 13(8) sentence 1 / DORA Art. 19(3), Art. 19(5) |
| **Notify BaFin/ECB 4h (DORA Art. 19 RTS)** | I | C | A/R | C | C | C | C | I | R | C | — | — | R | C | I | GDPR Art. 11(1), Art. 14(5)(b) / NIS2 Art. 23(1) ¶1, Art. 23(1) ¶2 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Notify BSI/CSIRT 24h (NIS 2 Art. 23(4)(a)) | I | C | C | A/R | C | C | C | I | R | C | — | — | C | C | I | GDPR Art. 11(1), Art. 14(5)(b) / NIS2 Art. 23(1) ¶1, Art. 23(1) ¶2 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Notify BSI/ENISA 24h (CRA Art. 14(1)) | I | C | I | A/R | C | C | C | I | R | C | — | — | C | C | I | GDPR Art. 11(1), Art. 14(5)(b) / NIS2 Art. 23(1) ¶1, Art. 23(1) ¶2 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Notify DPA 72h (GDPR Art. 33) | I | C | C | C | A | C | C | I | R | C | — | — | C | C | I | GDPR Art. 11(1), Art. 14(5)(b) / NIS2 Art. 23(1) ¶1, Art. 23(1) ¶2 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Notify AI Act authority (Art. 73 3-tier: 15d/2d/10d) | I | C | C | C | C | A | C | I | R | C | — | — | C | — | I | GDPR Art. 11(1), Art. 14(5)(b) / NIS2 Art. 23(1) ¶1, Art. 23(1) ¶2 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Notify controller (Art. 33(2) processor → joint controller where applicable) | I | C | C | A | C | C | C | I | R | C | — | — | C | C | I | GDPR Art. 11(1), Art. 14(5)(b) / NIS2 Art. 23(1) ¶1, Art. 23(1) ¶2 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Recover systems (RTO 4h, RPO 15min for mainframe) | I | A | C | C | I | C | I | I | R | I | — | — | C | — | I | GDPR Art. 21(1), Art. 32(1) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 6 chapeau + (a) / DORA Art. 21(1)+(2), Art. 23 |
| Post-incident review (4h DORA report; root cause within 5d) | I | C | A | C | C | C | C | R | R | I | — | — | R | C | I | GDPR Art. 10, Art. 21(1) / NIS2 Art. 21(1) sentence 1, Art. 21(2) chapeau / CRA Art. 6 chapeau + (a) / DORA Art. 17(1), Art. 21(1)+(2) |
| BCP activation (annual exercise; quarterly tabletop) | I | C | C | A | I | C | I | I | R | I | — | — | C | — | I | GDPR Art. 21(1), Art. 32(1) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 6 chapeau + (a) / DORA Art. 21(1)+(2), Art. 23 |
| DORA Art. 17 major ICT-related incident classification | I | C | R | C | C | C | C | I | R | C | — | — | A | C | I | GDPR Art. 11(1), Art. 14(5)(b) / NIS2 Art. 23(1) ¶1, Art. 23(1) ¶2 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |

### 4.5 Data Lifecycle (sub-domain D-05)

| Activity | CEO | CTO | CRO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | DORA-Risk | Fraud | Board | Corpus Reg Req (corpus articles) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enforce data minimisation (mobile + CDW anonymisation) | I | C | C | A | A | C | C | I | R | I | — | — | C | C | I | GDPR Art. 10, Art. 12(6) / CRA Art. 13(3) sentence 2, Art. 6 chapeau + (a) |
| Manage retention policies (10y BaFin/GoBD; 7y HR; AML 10y) | I | C | C | C | A | C | R | I | R | C | C | — | C | C | I | GDPR Art. 10, Art. 21(3) / CRA Art. 13(9), Art. 14(5)(a) |
| Process erasure requests (Art. 17 GDPR with BaFin retention exemption) | I | C | C | C | A/R | I | C | I | R | C | C | — | C | C | I | GDPR Art. 10, Art. 21(3) / CRA Art. 13(9), Art. 14(5)(a) |
| Cryptographic sharding (AI Act log retention vs. GDPR Art. 17 erasure) | I | C | C | C | A | A | C | I | C | C | — | — | C | — | I | GDPR Art. 10, Art. 21(3) / CRA Art. 13(9), Art. 14(5)(a) |
| Support data portability (Art. 20 + PSD2 Open Banking) | I | C | C | C | A | I | R | I | R | C | — | — | C | — | I | GDPR Art. 15(1), Art. 15(3) |
| AI-system training-data lineage (AI Act Art. 10) | I | C | C | C | C | A | C | I | — | C | — | — | C | — | I | GDPR Art. 10, Art. 12(6) / CRA Art. 13(3) sentence 2, Art. 6 chapeau + (a) |

### 4.6 Supply Chain (sub-domain D-06)

| Activity | CEO | CTO | CRO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | DORA-Risk | Fraud | Board | Corpus Reg Req (corpus articles) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Assess vendor security (annual + tiered cadence + DORA Art. 28-30 register) | I | C | A | C | C | C | C | R | C | C | — | C | R | C | I | GDPR Art. 21(1), Art. 28(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(5) / DORA Art. 21(1)+(2), Art. 28 chapeau + (1) + (2) |
| Maintain SBOM per release (machine-readable SBOM format for mobile + AI models) | I | C | I | A | I | C | C | I | R | I | — | — | C | — | I | |  |
| Manage DPA + DORA Art. 30 ICT contracts | I | I | C | A | A | I | R | I | — | C | — | C | C | — | I | GDPR Art. 21(1), Art. 21(3) / NIS2 Art. 20 chapeau, Art. 20(1) / CRA Art. 13(6) sentence 1, Art. 20(1) / DORA Art. 19(1), Art. 19(2) |
| CRA Annex I Part I (2)(h) supplier clauses (mobile app) | I | C | C | A | C | C | R | I | — | C | — | C | C | — | I | GDPR Art. 21(1), Art. 21(3) / NIS2 Art. 20 chapeau, Art. 20(1) / CRA Art. 13(6) sentence 1, Art. 20(1) / DORA Art. 19(1), Art. 19(2) |
| NIS 2 supply-chain security (Art. 21(2)(d)) | I | C | C | A | I | I | R | I | R | C | — | C | C | — | I | GDPR Art. 21(1), Art. 28(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(5) / DORA Art. 21(1)+(2), Art. 28 chapeau + (1) + (2) | GDPR Art. 21(1), Art. 21(3) / NIS2 Art. 20 chapeau, Art. 20(1) / CRA Art. 13(6) sentence 1, Art. 20(1) / DORA Art. 19(1), Art. 19(2) |
| DORA Art. 28-30 ICT third-party register + contracts | I | C | A | C | C | C | C | R | — | C | — | C | R | — | I | GDPR Art. 21(1), Art. 21(3) / NIS2 Art. 20 chapeau, Art. 20(1) / CRA Art. 13(6) sentence 1, Art. 20(1) / DORA Art. 19(1), Art. 19(2) |
| AI Act Art. 25 provider-deployer interface clauses (OmniScore) | I | C | C | C | C | A | R | I | — | C | — | C | C | — | I | GDPR Art. 21(1), Art. 21(3) / NIS2 Art. 20 chapeau, Art. 20(1) / CRA Art. 13(6) sentence 1, Art. 20(1) / DORA Art. 19(1), Art. 19(2) |
| Third-party boundary management (egress review + sub-outsourcing register) | I | C | C | A | C | C | R | I | R | C | — | C | C | — | I | GDPR Art. 18(1), Art. 18(2) / NIS2 Art. 21(3), Art. 22(2) / CRA Art. 21, Art. 22(1) / DORA Art. 18(1)(a), Art. 18(1)(b) |
| AI Act Notified Body coordination (Annex III conformity) | I | C | C | C | C | A | R | I | — | C | — | — | C | — | I | GDPR Art. 21(1), Art. 28(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(5) / DORA Art. 21(1)+(2), Art. 28 chapeau + (1) + (2) |
| TLPT framework coordination (DORA Art. 24) | I | C | C | A | C | C | C | R | C | C | — | C | R | C | I | DORA Art. 24(1)+(2) chapeau, Art. 25(1) |

### 4.7 Secure Development (sub-domain D-07)

| Activity | CEO | CTO | CRO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | DORA-Risk | Fraud | Board | Corpus Reg Req (corpus articles) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Threat model per feature (CRA mobile + AI Act Art. 9) | I | C | C | C | C | C | I | I | — | — | — | — | C | — | I | GDPR Art. 13(2)(f), Art. 21(1) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 13(1), Art. 13(2) sentence 1 / DORA Art. 17(1), Art. 21(1)+(2) |
| Code review (PR + dual approval + mainframe change-control) | I | A | I | C | I | C | I | I | — | — | — | — | C | — | I | |  |
| Security testing in CI/CD (static + dynamic + dependency analysis + co-signature + AI model signing) | I | A | I | C | I | C | I | I | R | — | — | — | C | — | I | |  |
| Change control + CAB + AI Act Art. 16 governance | I | A | I | C | C | A | C | I | I | I | — | — | C | — | I | CRA Art. 13(21), Art. 21 / DORA Art. 21(3), Art. 22(1) |
| AI model change-control (Annex III Art. 16 — OmniScore) | I | C | C | C | C | A | C | I | — | C | — | — | C | — | I | CRA Art. 13(21), Art. 21 / DORA Art. 21(3), Art. 22(1) |
| Mainframe change-control (legacy OS) | I | A | I | C | I | I | I | I | — | — | — | — | C | — | I | |  |

### 4.8 Human Factors (sub-domains D-08.1, D-08.2, **D-08.3 ACTIVE — NIS 2 + DORA dual obligation**)

| Activity | CEO | CTO | CRO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | DORA-Risk | Fraud | Board | Corpus Reg Req (corpus articles) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Annual security awareness (all 5,000+) + AI literacy (AI Act Art. 4) — D-08.1 | I | C | C | A | C | C | C | I | R | I | R | — | C | C | I | GDPR Art. 21(1), Art. 39(1)(b) / NIS2 Art. 20 chapeau, Art. 20(2) sentence 1 / DORA Art. 20, Art. 21(1)+(2) |
| Role-specific training (developers, SOC, AI, payments, branch) — D-08.2 | I | C | C | A | R | R | C | I | R | I | R | — | C | C | I | GDPR Art. 21(1), Art. 39(1)(b) / NIS2 Art. 20 chapeau, Art. 20(2) sentence 1 / DORA Art. 20, Art. 21(1)+(2) |
| AI Act Art. 4 AI literacy for AI-system operators — D-08.2 | I | C | C | C | C | A | C | I | — | I | R | — | C | — | I | GDPR Art. 21(1), Art. 39(1)(b) / NIS2 Art. 20 chapeau, Art. 20(2) sentence 1 / DORA Art. 20, Art. 21(1)+(2) |
| **Management Board cybersecurity briefings — D-08.3 (NIS 2 Art. 20 + DORA Art. 5 dual obligation)** | I | C | C | R | C | C | C | I | I | C | I | — | C | — | A | NIS2 Art. 20 chapeau, Art. 20(2) sentence 1 / DORA Art. 20 |
| NIS 2 Art. 20 management-body training programme | I | C | C | C | C | C | I | I | — | C | R | — | C | — | A | GDPR Art. 21(1), Art. 28(3) / NIS2 Art. 20 chapeau, Art. 20(2) sentence 1 / DORA Art. 20, Art. 21(1)+(2) |
| DORA Art. 5 management liability training (board) | I | C | R | C | C | C | I | I | — | C | I | — | C | — | A | NIS2 Art. 20 chapeau, Art. 20(2) sentence 1 / DORA Art. 20 |

**Note on D-08.3 ACTIVE:** OmniBank's NIS 2 + DORA applicability (5,000+ employees + credit institution + DORA financial entity) activates D-08.3 under a **dual obligation**. The CEO, CTO, CFO, CRO, COO, CISO, and 3 Non-Exec Directors each attend quarterly cybersecurity briefings (CISO presents), and Management Board confirms understanding of cybersecurity risks at each meeting. DORA Art. 5 management liability is a separate annual briefing by CRO. AI literacy (Art. 4) is integrated into general awareness. The Board also receives annual external cybersecurity + AI risk training from External Legal Counsel + CISO + AI Governance Lead.

### 4.9 Governance (sub-domain D-09)

| Activity | CEO | CTO | CRO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | DORA-Risk | Fraud | Board | Corpus Reg Req (corpus articles) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Approve security policies (ISO 27001 + documented third-party security attestation + DORA + AI Act) | C | C | C | C | C | C | C | C | C | C | C | C | C | C | A | GDPR Art. 21(1), Art. 23(1) / NIS2 Art. 20 chapeau, Art. 20(1) sentence 1 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Conduct risk assessments (annual + per-feature + DPIA + FRIA + DORA ICT + AI Act Art. 9) | I | C | A | C | C | C | R | I | — | C | — | — | R | C | I | GDPR Art. 13(2)(f), Art. 21(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(1), Art. 13(2) sentence 1 / DORA Art. 10(1), Art. 10(2)+(3) |
| **DPIA + FRIA combined risk assessment — D-09.2** | I | C | C | C | A | R | C | I | — | C | — | — | C | — | I | GDPR Art. 13(2)(f), Art. 21(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(1), Art. 13(2) sentence 1 / DORA Art. 10(1), Art. 10(2)+(3) |
| Maintain DORA Art. 8 ICT asset inventory (CMDB) — D-09.3 | I | C | A | C | I | C | C | I | R | I | — | — | R | — | I | NIS2 Art. 20 chapeau, Art. 20(1) sentence 1 / CRA Art. 7(1) sentence 1, Art. 7(1) sentence 2 / DORA Art. 10(1), Art. 10(2)+(3) |
| Maintain RoPA (Art. 30 GDPR) — D-09.4 | I | I | C | C | A | C | R | I | — | C | — | — | C | — | I | GDPR Art. 12(1), Art. 12(3) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Maintain CRA Annex VII technical documentation (mobile app) — D-09.4 | I | C | I | A | C | C | R | I | — | C | — | — | C | — | I | GDPR Art. 12(1), Art. 12(3) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Maintain AI Act Art. 11 technical file (OmniScore) — D-09.4 | I | C | C | C | C | A | R | I | — | C | — | — | C | — | I | GDPR Art. 12(1), Art. 12(3) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Maintain DORA Art. 8 ICT register — D-09.4 | I | C | A | C | I | C | C | I | — | C | — | — | R | — | I | GDPR Art. 12(1), Art. 12(3) / NIS2 Art. 21(1) sentence 1, Art. 21(2)(a) / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |
| Internal audit programme (annual; ISO 27001 + documented third-party security attestation + DORA + AI Act) | I | C | C | C | C | C | C | A/R | — | C | — | — | C | — | I | GDPR Art. 21(1), Art. 32(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 32(2), Art. 32(3) / DORA Art. 21(1)+(2), Art. 24(1)+(2) chapeau |
| MaRisk AT 9 compliance (German banking regulator) | I | I | A | C | I | I | R | I | — | C | — | — | C | — | I | GDPR Art. 21(1), Art. 23(1) / NIS2 Art. 20 chapeau, Art. 20(1) sentence 1 / CRA Art. 13(1), Art. 13(17) / DORA Art. 10(1), Art. 10(2)+(3) |

### 4.10 Monitoring & Audit (sub-domain D-10)

| Activity | CEO | CTO | CRO | CISO | DPO | AI-Gov | Comp | IA | SOC | Legal | HR | Proc | DORA-Risk | Fraud | Board | Corpus Reg Req (corpus articles) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Continuous security monitoring (centralized audit-log management + managed endpoint detection + managed vulnerability scanning + mainframe security monitoring) | I | C | C | A | I | C | I | I | R | — | — | — | C | — | I | GDPR Art. 21(1), Art. 25(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(1), Art. 6 chapeau + (a) / DORA Art. 21(1)+(2), Art. 25(1) |
| AI-post-market monitoring (AI Act Art. 72 — OmniScore) | I | C | C | C | C | A | C | I | R | C | — | — | C | — | I | GDPR Art. 21(1), Art. 25(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(1), Art. 6 chapeau + (a) / DORA Art. 21(1)+(2), Art. 25(1) |
| Audit-log retention (10-year WORM, HSM-signed hash chain) | I | C | C | A | C | C | C | I | R | C | — | — | C | — | I | GDPR Art. 21(1), Art. 25(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(1), Art. 6 chapeau + (a) / DORA Art. 21(1)+(2), Art. 25(1) |
| Annual compliance testing (ISO 27001 + documented third-party security attestation) | I | C | C | A | C | C | R | R | C | I | — | — | C | — | I | GDPR Art. 21(1), Art. 25(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(1), Art. 6 chapeau + (a) / DORA Art. 21(1)+(2), Art. 25(1) |
| DORA Art. 24 TLPT every 3 years | I | C | C | A | C | C | C | R | C | C | — | C | R | C | I | GDPR Art. 21(1), Art. 25(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(1), Art. 6 chapeau + (a) / DORA Art. 21(1)+(2), Art. 25(1) |
| AI Act conformity assessment (Annex III — OmniScore) | I | C | C | C | C | A | R | I | — | C | — | — | C | — | I | GDPR Art. 21(1), Art. 25(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(1), Art. 6 chapeau + (a) / DORA Art. 21(1)+(2), Art. 25(1) |
| DORA Art. 17-19 major ICT-related incident reporting | I | C | A | C | C | C | C | I | R | C | — | — | R | — | I | GDPR Art. 21(1), Art. 25(1) / NIS2 Art. 21(1) sentence 1, Art. 21(1) sentence 2 / CRA Art. 13(1), Art. 6 chapeau + (a) / DORA Art. 21(1)+(2), Art. 25(1) |

**Reading note:** Rows that place both **CISO = A** and **SOC = R** mirror the standard "RACI for security operations" pattern — the CISO owns the outcome; the SOC Manager or IR Lead does the work. Where the activity is data-protection-specific (e.g., Art. 17 erasure), **DPO = A** holds the legal accountability per Art. 28(3). Where the activity is AI-Act specific (FRIA, post-market monitoring, AI model change-control), **AI Governance Lead = A**. Where the activity is risk-specific (DORA Art. 5 ICT risk, Art. 28-30 register), **CRO = A**. Where the activity is fraud-specific (AML/KYC), **Fraud Detection Lead = A**. Board rows are predominantly **C** operationally and **A** for governance-level approvals.

---

## 5. Training Status

OmniBank runs a formalised training programme (per `00_COMMON/01_Company_Context.md §6.2 — IR-08 = YES). The table below records **last completed** / **next planned refresh** per role. All 5,000+ employees are awareness-training targets; this table covers the named-RACI cohort (~38 roles) for role-specific training.

| Role Cohort | Training Required | Last Completed | Next Refresh | Source (D-08.x req_id) |
|---|---|---|---|---|
| All staff (5,000+) | Annual security awareness + AI literacy (AI Act Art. 4) | 2025-Q4 (completion 98%; remaining 2% on extended leave) | 2026-Q4 | D-08.1 + D-08.2 (SR-AIACT-013 — Art. 4 AI literacy) |
| All developers (~50 incl. mainframe, cloud, mobile, payments, ML) | Secure coding (industry secure-coding guidelines for web + mobile); industry industrial-cybersecurity standard for industrial; AI-Act-specific (Annex III risk-management) | 2025-Q4 (annual) | 2026-Q4 | D-08.2 (CRA + AI Act) |
| All SOC analysts (24) | Industry security certifications + IR tabletop + AI adversarial testing bootcamp + mainframe security monitoring | Mixed (rolling; all hold at least one industry security cert; AI adversarial training added 2025-Q4) | 2026-Q4 | D-08.2 (NIS 2 + DORA + AI Act) |
| DPO | CIPP/E + GDPR refresher cadence (quarterly) + AI Act data-governance + DORA data protection overlay | 2025-Q4 (CIPP/E renewal 2026-Q1) | 2026-Q4 | D-08.2 (GDPR + AI Act + DORA) |
| CISO | ISO 27001 Lead Auditor + NIS 2 lead-implementer + documented third-party security attestation QSA + DORA ICT risk | 2025-Q3 (CISSP + ISO 27001 LI + documented third-party security attestation QSA) | 2026-Q3 | D-08.2 |
| CRO | DORA ICT risk management + Basel + MaRisk AT 9 | 2025-Q3 (FRM + DORA-certified) | 2026-Q3 | D-08.2 (DORA + MaRisk) |
| AI Governance Lead | AI Act bootcamp + ISO 42001 AI management system lead-implementer + AI ethics | 2025-Q4 | 2026-Q4 | D-08.2 (AI Act) |
| AI Bias & Robustness Specialist | Adversarial ML + fairness audit certification + DORA AI risk | 2025-Q4 | 2026-Q4 | D-08.2 (AI Act + DORA) |
| Compliance Lead | IAPP + GDPR practitioner + BaFin/ECB regulator engagement | 2025-Q4 | 2026-Q4 | D-08.2 |
| Internal Audit Lead | CISA + ISO 27001 Lead Auditor + DORA audit | 2025-Q3 | 2026-Q3 | D-08.2 |
| SOC Manager | CISSP + GIAC security-essentials + DORA incident response | 2025-Q3 | 2026-Q3 | D-08.2 |
| IR Lead / CSIRT Lead | GCIH + incident-response tabletop certification + DORA RTS classification | 2025-Q3 | 2026-Q3 | D-08.2 |
| DORA ICT Risk Manager | DORA Art. 5-16 specialist + ISO 27005 risk management | 2025-Q4 | 2026-Q4 | D-08.2 (DORA) |
| Fraud Detection Lead | CAMS + ACFCS + BaFin AML certification | 2025-Q4 | 2026-Q4 | D-08.2 (BaFin AML) |
| Procurement Director | DORA Art. 30 ICT contracts + GDPR Art. 28 DPA + CRA supply-chain | 2025-Q4 | 2026-Q4 | D-08.2 (DORA + CRA) |
| External Legal Counsel | Multi-jurisdiction CPD on EU regs (NIS 2 + DORA + AI Act + CRA) | Retained on continuing basis; 2025-Q4 update | 2026-Q4 | D-08.2 |
| **Management Board (8 directors)** | **D-08.3 ACTIVE — Quarterly cybersecurity briefing by CISO + Annual DORA Art. 5 management liability briefing by CRO + Annual AI risk briefing by AI Governance Lead + Biennial external cyber-board training** | **2026-Q1 briefing complete (latest)** | **2026-Q3 (next quarterly)** | **D-08.3 (NIS 2 Art. 20 + DORA Art. 5 dual obligation)** |
| Branch Operations (1,200 branches) | Branch security awareness + AI literacy | 2025-Q4 | 2026-Q4 | D-08.1 |
| Contact Centre (80 staff) | Documented third-party security attestation awareness + AI literacy + fraud detection training | 2025-Q4 | 2026-Q4 | D-08.2 |

**Status summary:**
- Awareness + role-specific training rows: COMPLETED 2025-Q4 (annual cadence); ongoing through 2026.
- Board row (D-08.3 ACTIVE under NIS 2 + DORA dual obligation): MOST RECENT 2026-Q1; ongoing quarterly cadence.
- D-08.3 is **derived from NIS 2 Art. 20 + DORA Art. 5 dual obligation** — not optional, not a best-practice placeholder. Quarterly cadence + annual DORA briefing + annual external training.

---

## 6. Compliance Mapping (Regulatory Baseline)

Active scope for OmniBank = 38 of 38 sub-domains. D-08.3 IS ACTIVE (NIS 2 + DORA dual obligation) — this differs from Case 01 (LOW tier, no NIS 2 / no DORA) and Case 02 (HIGH tier, NIS 2 only).

| Sub-domain | Role(s) Responsible | RACI Summary | Corpus Manifest Path | Notes |
|---|---|---|---|---|
| D-08.1 General Awareness | HR (HR-coordination role) + CISO (owns governance) | HR=R, CISO=A; AI-Gov=C (AI literacy integration) | [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.1/D-08.1.manifest.json`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.1/D-08.1.manifest.json) | Coverage = all 5,000+ employees; 98% completion 2025-Q4. |
| D-08.2 Role-Specific Competence | CISO + DPO + CRO + AI-Gov + Fraud (per role) | Role-specific R assignments; CISO=A for governance | [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.2/D-08.2.manifest.json`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.2/D-08.2.manifest.json) | ~50 developers; 24 SOC; 22 AI-team; 20 financial crime; DPO + CRO + Compliance + IA + IR + SOC Manager + Fraud + Procurement. |
| **D-08.3 Management Board Training** | **ACTIVE — NIS 2 Art. 20 + DORA Art. 5 dual obligation** | **CISO=R (quarterly briefing); CRO=R (annual DORA briefing); AI-Gov=R (annual AI risk briefing); Board=A** | [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.3/D-08.3.manifest.json`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.3/D-08.3.manifest.json) | Quarterly briefings + annual DORA briefing + annual AI risk briefing + annual external cyber-board training; board minutes record acknowledgement. |
| D-09.1 Information Security Policies | Board for approval; CISO for drafting; DPO + AI-Gov + CRO + Legal co-author | Board=A; CISO=R; DPO/CRO/AI-Gov/Legal=C | [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/D-09.1.manifest.json`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/D-09.1.manifest.json) | ISO 27001 v6.2 + documented third-party security attestation + DORA ISMS overlay + AI Act addendum + MaRisk AT 9; approved 2025-Q3 by Management Board. |
| D-09.2 Impact & Risk Assessments | DPO + AI Governance Lead + CRO + CISO (compound) | DPO=A (DPIA); AI-Gov=A (FRIA); CRO=A (DORA ICT risk); CISO=A (security risk assessment); Comp=R (unified register) | [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/D-09.2.manifest.json`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/D-09.2.manifest.json) | Annual + per-feature; DPIA + FRIA combined assessment per Phase 2 strategic-tensions resolution; DORA ICT risk integrated. |
| D-09.3 Asset Inventories | CRO + CISO + DevSecOps Lead + IA Lead (verification) | CRO=A; CISO=R; DevSecOps=R; DORA-Risk=R | [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/D-09.3.manifest.json`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/D-09.3.manifest.json) | DORA Art. 8 ICT asset register; CMDB with 100% asset coverage; auto-discovered monthly. |
| D-09.4 Records of Processing | DPO + AI Governance Lead + CRO + Compliance Lead | DPO=A (GDPR RoPA); AI-Gov=A (AI Act Art. 11 technical file); CRO=A (DORA Art. 8 ICT register); CISO=A (CRA Annex VII documentation); Comp=R (unified register) | [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.manifest.json`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.manifest.json) | Coordinated; CRA Annex VII documentation (mobile app), AI Act technical file (OmniScore), DORA Art. 8 ICT register all maintained. |

---

## 7. Gaps & Known Limitations (Open Items)

These items are surfaced for Phase 2 / Phase 3 remediation and are **proportionate**, not over-engineered for a MAXIMUM-tier regulated credit institution.

| Gap ID | Description | Severity | Linked Sub-Domain |
|---|---|---|---|
| GAP-RACI-01 | Single AI Governance Lead as AI-Act point of accountability; backup is Deputy AI Governance Lead (good); AI Bias & Robustness + FRIA Lead + Post-Market Lead are well-staffed | LOW | D-09.1 |
| GAP-RACI-02 | DPO operational reporting through DPO-line + independent access to CEO + Board; per Art. 38(3) independence is preserved but in operational matrix reports through DPO-line. Risk-accepted by Management Board | LOW (risk-accepted) | D-09.1 |
| GAP-RACI-03 | D-08.3 ACTIVE under NIS 2 + DORA dual obligation — programme is mature (quarterly briefings since 2024-Q4) but DORA Art. 5 specific briefing was added in 2026-Q1; engagement maturing | LOW | D-08.3 |
| GAP-RACI-04 | In-house Legal Counsel (2.0 FTE) supplemented by external multi-jurisdiction retainers; in-house + external coverage sufficient | LOW | D-09.1 |
| GAP-RACI-05 | Single IR Lead / CSIRT Lead as named-point-of-contact for DORA Art. 17-19 + NIS 2 24h reporting; backup is SOC Manager + CISO; 24/7 coverage sustained | LOW | D-04.3 |

**Discussion per AEGIS P0 (Reasoned Disagreement):** GAP-RACI-02 is **not** a compliance gap; the Board has accepted the documented decision to maintain DPO operational reporting through DPO-line + independent access to CEO + Board. The methodology recommends an embedded DPO (no conflict of interest) — OmniBank has evaluated cost vs benefit and the current arrangement is GDPR-conformant provided Art. 38(3) independence is honoured. The arrangement is documented in the row above to make the methodology's preference visible.

---

## 8. Gate

This document is complete (Phase 1 Step E — Roles & RACI) when:

- [x] All key roles identified with FTE allocation (Section 2 — ~38 roles)
- [x] RACI matrix populated for all 10 macro-domains (Section 4 — D-01 to D-10)
- [x] Reporting lines documented (Section 3 — text + ASCII)
- [x] Training status populated for all named roles (Section 5 — incl. D-08.3 ACTIVE row under NIS 2 + DORA dual obligation)
- [x] Compliance Mapping table populated for D-08.x and D-09.x (Section 6)
- [x] Gaps explicitly listed (Section 7) rather than silently accepted — required by AEGIS P5 and P0
- [x] D-08.3 ACTIVE flagged explicitly (NIS 2 + DORA dual obligation)

**Gate Status:** PASS (proportionate for MAXIMUM-tier regulated credit institution under P2).

---

## N-1. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-07-11 | Executor | Populated from template `04d_Org_Roles_RACI.md`; integrated stakeholder register from `04 §3` and architecture from `04a`; D-08.3 ACTIVE flagged (NIS 2 Art. 20 + DORA Art. 5 dual obligation). ~38 named-RACI roles with dedicated CISO (100-person security team) + DPO + CRO + AI Governance Lead + DORA ICT Risk Manager functions appropriate for MAXIMUM-tier credit institution. |
| 1.2 | 2026-08-06 | Executor | Sprint 2 corpus enrichment: §4 RACI tables extended with Corpus Reg Req column (40+ activity rows mapped to corpus article refs); §6 Compliance Mapping table extended with Corpus Manifest Path column for D-08.x + D-09.x. status RECONCILED → CORPUS_ENRICHED. |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-07-11 |
| Technical Review | CTO |  |  |
| Security Review | CISO |  |  |
| Compliance Review | CRO |  |  |
| DPO Review | DPO |  |  |
| AI Governance Review | AI Governance Lead |  |  |
| DORA ICT Risk Review | DORA ICT Risk Manager |  |  |
| Business Review | CEO |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Data backbone:** `Case_03_Phase1.xlsx` (13 sheets: COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, MATURITY, SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES)
- **Architecture:** `04a_Architecture_DataInventory.md` (RACI maps activities to systems SYS-01..SYS-25).
- **Vendors:** `04c_ThirdParty_Landscape.md` (CRO owns DORA Art. 28-30 ICT third-party register; CISO owns vendor-risk-assessment cadence; Procurement Director owns vendor relationship management).
- **Maturity:** `04b_Security_Posture.md` (CISO + CRO + AI Governance Lead drive the top-gaps remediation; maturity averaging 3.8 across 10 macro-domains).
- **MAXIMUM-tier context:** `02_CASES/Case_03_OmniBank_Financial/00_COMMON/01_Company_Context.md` (5 applicable regulations; complexity tier MAXIMUM; 5,000+ employees; credit institution + DORA financial entity + NIS 2 essential entity + AI Act Annex III + CRA mobile app Default Class).
- **D-08.3 ACTIVE note:** D-08.3 is ACTIVE here under a **dual NIS 2 Art. 20 + DORA Art. 5 obligation**. It was INACTIVE in Case 01 (LOW tier, no NIS 2 / no DORA), ACTIVE under NIS 2 only in Case 02 (HIGH tier, NIS 2 essential-entity supplier). The methodology treats activation consistently; the difference is the company's regulatory profile, not the methodology.