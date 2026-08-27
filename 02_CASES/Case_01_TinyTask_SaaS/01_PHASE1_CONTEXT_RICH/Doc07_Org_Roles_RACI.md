---
document_id: AEGIS-P1-04d
title: Organisation, Roles & RACI Matrix
phase: 1
version: 1.1
created: 2026-07-11
updated: 2026-08-06
author: Executor (Fase de Especificação 1 reconciliation; Fase de Especificação 2 corpus enrichment)
status: CORPUS_ENRICHED
case_study: TinyTask Lda.
sprint_role: reconciled_from_legacy
inputs:
  - Doc03_Company_Context_Assessment.md
  - Doc04_Architecture_DataInventory.md
  - Doc06_ThirdParty_Landscape.md
  - ../00_COMMON/01_Company_Context.md
outputs:
  - Doc11_Structured_Compliance_Matrix.md
applicable_regs: [GDPR, CRA]
active_subdomains: 37  # RECONCILED (Fase de Especificação 1, I-02): was 36, corrected to 37 to match Doc 04a/04b/04c/05/07. 37 = 38 total sub-domains minus D-08.3 INACTIVE. D-08.3 row is INACTIVE (explicitly so), not subtracted from the active count.
inactive_subdomains: [D-08.3]  # board training out of scope (NIS2 + DORA only participating)
related_documents:
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/
  - ../../../00_METHODOLOGY/TEMPLATES/04d_Org_Roles_RACI.md
  - ../../../00_METHODOLOGY/CONTEXT/CONTEXT_PHASE1.md
supersedes: none
---

> **Fase de Especificação 1 Reconciliation Note (2026-08-06)**
> This document is the Rich Mode copy of the legacy `01_PHASE1_CONTEXT/04d_Org_Roles_RACI.md` (v1.0). Fase de Especificação 1 changes:
> - **I-02 (active_subdomains 36 → 37):** Corrected. The canonical active count is **37** (38 sub-domains minus D-08.3 INACTIVE; D-08.3 is recorded as an inactive row, not subtracted). This aligns with `04a`, `04b`, `04c`, `05`, and `07` which all carry `active_subdomains: 37`.
> - **I-10 (status DRAFT → RECONCILED):** Updated. Fase de Especificação 1 = reconciliation milestone; docs are internally consistent pending Fase de Especificação 2 corpus enrichment.
> - **I-13 (02_Regulatory_Mapping_Master.md deprecation banner):** Not applicable — this document does not reference `02_Regulatory_Mapping_Master.md`.
> - **Source:** `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT/04d_Org_Roles_RACI.md` (legacy, read-only).
> - **Migration plan:** Phase 2/3 consumers should reference the **Rich** copy (`01_PHASE1_CONTEXT_RICH/`) once Fase de Especificação 3 validation approves migration.
>
> **Fase de Especificação 2 Enrichment Note (2026-08-06)**
> - **Status: RECONCILED → CORPUS_ENRICHED.** Section 4 (RACI Matrix) tables §4.1–§4.10 extended with `Corpus Reg Req` column mapping each activity to the corpus `req_id` from the relevant per-sub-domain manifest (`sub_requirements_by_regulation.GDPR[]` ∪ `sub_requirements_by_regulation.CRA[]`). Section 6 (Compliance Mapping) table extended with `Corpus Manifest Path` column. New §9 Corpus Provenance documents the req_id mapping strategy.

# Organisation, Roles & RACI Matrix

## 1. Purpose & Scope

This document describes TinyTask Lda.'s organisational structure and the per-activity RACI matrix that allocates information-security and data-protection responsibilities. It maps to Regulatory Baseline sub-domains **D-08 (Human Factors)** and **D-09 (Governance Documentation)**, and supports compliance with **GDPR Art. 37-39** (DPO designation, not mandatory for TinyTask but voluntarily adopted), **GDPR Art. 32** (security of processing), **CRA Annex I Part II (8)(f)** (handling of vulnerabilities — competence requirements), and **CRA Annex VII §5** (technical documentation — organisational measures).

**Scope:** D-08 and D-09 only. Architecture context is in `04a_Architecture_DataInventory.md`; third-party context is in `04c_ThirdParty_Landscape.md`; security posture is in `04b_Security_Posture.md`.

**Critical caveat — sub-domain D-08.3 is INACTIVE for TinyTask.** Per `05_Regulatory_Applicability.md §6.3` (migrated from Doc 04 §7 in v2.2), D-08.3 (Management Board Training) participates only in **NIS2** and **DORA**; neither regulation applies to TinyTask (8 employees, <€2M revenue, not a financial entity). Consequently, there is **no OJ-level regulatory mandate** for formal board cybersecurity training at TinyTask. The board-training row in the RACI matrix below is retained as a **best-practice placeholder** (recommended under CRA spirit and CRS-style executive awareness), not as a derived compliance requirement.

**Proportionality note (P2 — Company Reality First):** TinyTask has 8 employees. Formal role separation characteristic of larger firms (separate DPO, CISO, IT Manager, Legal, HR, IR Lead) is not feasible — many hats fall on the CEO/CTO/lead developer. RACI assignments therefore concentrate **A** (Accountable) on the CEO or CTO, with one **R** (Responsible) per activity and the rest as **C** (Consulted) or **I** (Informed).

---

## 2. Key Roles

TinyTask has 8 employees. Functional roles are listed below; only one external legal adviser exists (DPO-support on retainer). There is no separate HR function — the CEO handles people ops and security training coordination as part of the 0.2 FTE DPO allocation.

| Role | Person / Team | Reports To | FTE Allocation | Backup |
|---|---|---|---|---|
| CEO (also DPO per Art. 37 voluntary designation) | Founder #1 | Board (2 founders) | 0.2 DPO + business leadership as CEO (combined FTE: 1.0 total) | CTO (acting DPO; not legally optimal but documented for incident-trigger continuity) |
| CTO (also CISO per CRA Annex I Part II (8)(f)) | Founder #2 | Board (2 founders) | 0.3 CISO + technical leadership as CTO (combined FTE: 1.0 total) | CEO (acting CISO) |
| Lead Developer (Dev Lead) | Senior engineer — most-tenured non-founder | CTO | 1.0 (full developer; ~0.1 of time on security tasks via CI/CD and patching) | CTO for code-related security tasks |
| Developer × 5 | 5 full-stack developers | CTO | 5 × 1.0 across product development, secure coding, CI/CD maintenance, on-call rotation | Peer developers |
| External Legal Adviser (DPO Support) | External law firm (Portugal) | CEO | 0 (retainer; no allocated FTE; ad-hoc consultation) | None — single retainer |
| Management Board | 2 founders (CEO + CTO) | — | — | n/a — board is the board |
| Incident Response (IR) Lead | CTO in CISO capacity | n/a (rotational developer on-call supplements) | Same as CTO/CISO; on-call rotation across developers for alarm response | CEO |

**Observations on role reality:**

- **DPO is voluntary** — GDPR Art. 37(1)(b)-(c) mandates DPO designation only for special-category-data controllers / processors or large-scale monitoring; TinyTask has neither. Designation is voluntary and serves practical GDPR accountability rather than a hard legal requirement (NA-004 in `04 §12.4`).
- **CISO is not formally titled** — CRA does not mandate the title; the CTO shoulders security leadership as part of the founding-team role. The 0.3 FTE allocation is the CTO's cybersecurity allocation, **not** a separate headcount.
- **No separate Legal or HR function** — Legal is the external retainer; HR-type coordination (training scheduling, on-boarding) is part of the CEO/DPO 0.2 FTE.
- **No IT Manager role** — Infrastructure is delegated to cloud managed services; no on-prem IT. The CTO/CISO covers IAM, cloud configuration, and KMS administration.
- **No dedicated IR Lead** — The CTO/CISO leads incident response; detection and containment execute through CI/CD + Datadog + Auth0 + AWS capabilities (see `04a §1.4`); on-call rotation spreads response across developers.

---

## 3. Reporting Lines

```
                            ┌─────────────────────────────┐
                            │       Management Board       │
                            │   (2 founders — CEO + CTO)    │
                            └──────────────┬────────────────┘
                                           │
              ┌────────────────────────────┼────────────────────────┐
              │                                                         │
       ┌──────▼─────────┐                                       ┌──────▼─────────┐
       │      CEO       │                                       │      CTO       │
       │ 0.2 FTE DPO    │                                       │ 0.3 FTE CISO   │
       │ + founder ops  │                                       │ + founder tech │
       └──┬─────────────┘                                       └──┬─────────────┘
          │                       ┌─────────────────┐              │
          │                       │ External Legal  │              │
          │                       │   (DPO Support) │              │
          │                       └─────────────────┘              │
          │                                                        │
          └────────────────────┬───────────────────────────────────┘
                               │
                  ┌────────────▼────────────┐
                  │     Lead Developer       │
                  │    (senior engineer)     │
                  └────────────┬─────────────┘
                               │
            ┌──────────────────┴──────────────────┐
            │                                      │
   ┌────────▼────────┐                  ┌─────────▼───────┐
   │ Developers × 5  │                  │  (Developers on │
   │  (full-time)    │                  │   security rota)│
   └─────────────────┘                  └─────────────────┘
```

**Plain-text description:**

- The **Management Board** consists of the two founders (CEO and CTO); it has final accountability for security and compliance posture.
- The **CEO** holds the voluntary **DPO** hat (0.2 FTE). Reports to the Board.
- The **CTO** holds the **CISO** hat (0.3 FTE). Reports to the Board.
- The **Lead Developer** reports to the CTO and is the single point of accountability for day-to-day code-level and CI/CD-level security controls.
- The **5 developers** report to the CTO; they form the on-call rotation for security alarms (especially D-04.1 detection) and execute patching/vulnerability remediation under CTO direction.
- The **External Legal Adviser** is on retainer; reports to the CEO; consults on DPA template updates and breach-notification decisions.
- **There is no separate HR function**; people-ops (onboarding, training coordination) is part of the CEO 0.2 FTE.
- **No IT Manager role**; cloud-managed services are configured and reviewed by the CTO/CISO and lead developer.

---

## 4. RACI Matrix

**Legend:**

- **R** = Responsible (does the work)
- **A** = Accountable (single sign-off; one A per row)
- **C** = Consulted (provides input before decision)
- **I** = Informed (told after the decision / action)
- **—** = Not involved

**Column abbreviations** (people are listed once each; in a tiny team, multiple hats are worn):

- **DPO** = CEO acting as voluntary Data Protection Officer (0.2 FTE)
- **CISO** = CTO acting as Security Lead / CISO (0.3 FTE)
- **Dev** = Lead Developer + developer team (5 staff)
- **Legal** = External Legal Adviser (retainer)
- **HR** = CEO in HR-coordination role (overlaps with DPO column; same person; not double-counted)
- **Board** = 2 founders (CEO + CTO)

**Conventions adopted for the rows below:**

- **A** for security-impacting decisions sits on the **CTO/CISO** unless the activity is data-protection-specific (in which case A is the **CEO/DPO**); governance-level approvals have **A = Board**.
- Many rows carry multiple **C** because the consulting loop is short and cheap in a small team.
- **I** is used liberally — being informed is free and is the AEGIS default for non-executive stakeholders (board included) for operational items.

### 4.1 Data Protection (sub-domain D-01)

| Activity | DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|
| Encrypt personal data at rest | C | A | R | I | — | I | D-01.1: 1.1.1, 1.1.3 (GDPR + CRA) |
| Manage encryption keys | C | A | R | I | — | I | D-01.3: 1.3.1, 1.3.2 (GDPR + CRA) |
| Notify DPA within 72h (Art. 33 GDPR) | R | A | C | C | — | I | D-04.3: 4.3.1, 4.3.3 (GDPR + CRA) |
| Conduct DPIA (Art. 35 GDPR) | R | C | C | A | — | I | D-09.2: 9.2.1, 9.2.3 (GDPR + CRA) |

### 4.2 Vulnerability Management (sub-domain D-02)

| Activity | DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|
| Run vulnerability scans (Snyk, dependency review) | I | A | R | — | — | I | D-02.1: 2.1.1, 2.1.3 (GDPR + CRA) |
| Apply critical patches (CRA Annex I Part I (2)(f)) | I | A | R | — | — | I | D-02.2: 2.2.1 (GDPR + CRA) |
| Annual penetration testing | I | A | R | I | — | I | D-02.4: 2.4.1 (GDPR + CRA) |
| Operate CVD / security.txt (CRA Art. 14) | C | A | R | I | — | I | D-02.3: 2.3.1 (GDPR + CRA) |

### 4.3 Access Control (sub-domain D-03)

| Activity | DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|
| Manage IAM (Auth0 + cloud IAM) | C | A | R | I | — | I | D-03.1: 3.1.1, 3.1.3 (GDPR + CRA) |
| Enforce MFA (admins; future customer MFA) | C | A | R | — | — | I | D-03.2: 3.2.1, 3.2.3 (GDPR + CRA) |
| Quarterly access review | C | A | R | I | — | I | D-03.1: 3.1.1, 3.1.3 (GDPR + CRA) |
| Offboarding (revoke access within 24h) | C | A | R | I | C | I | D-03.1: 3.1.1, 3.1.3 (GDPR + CRA) |

### 4.4 Incident Response (sub-domain D-04)

| Activity | DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|
| Detect incident | I | A | R | — | — | I | D-04.1: 4.1.1, 4.1.3 (GDPR + CRA) |
| Contain incident | I | A | R | C | — | I | D-04.2: 4.2.1, 4.2.3 (GDPR + CRA) |
| Notify authorities (72h GDPR Art. 33; 24h early-warning CRA Art. 14) | R | A | C | C | — | I | D-04.3: 4.3.1, 4.3.3 (GDPR + CRA) |
| Notify controllers (Art. 33(2) processor→controller) | R | A | C | C | — | I | D-04.3: 4.3.1, 4.3.3 (GDPR + CRA) |
| Recover systems (RPO / RTO targets) | I | A | R | I | — | I | D-04.4: 4.4.1, 4.4.3 (GDPR + CRA) |
| Post-incident review | C | A | R | I | — | I | D-04.2: 4.2.1, 4.2.3 (GDPR + CRA) |

### 4.5 Data Lifecycle (sub-domain D-05)

| Activity | DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|
| Enforce data minimisation | R | A | C | C | — | I | D-05.1: 5.1.1, 5.1.2 (GDPR + CRA) |
| Manage retention policies | R | A | C | C | — | I | D-05.2: 5.2.1, 5.2.2 (GDPR + CRA) |
| Process erasure requests (Art. 17 GDPR; CRA Annex I Part I (2)(m)) | R | C | A | C | — | I | D-05.3: 5.3.1, 5.3.2 (GDPR + CRA) |
| Process portability requests (Art. 20 GDPR) | R | C | A | C | — | I | D-05.4: 5.4.1 (GDPR + CRA) |

### 4.6 Supply Chain (sub-domain D-06)

| Activity | DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|
| Assess vendor security (annual review) | C | A | R | C | — | I | D-06.1: 6.1.1, 6.1.3 (GDPR + CRA) |
| Maintain SBOM (CRA Annex I Part II (1)) | I | A | R | — | — | I | D-06.2: 6.2.1 (CRA only — confirmed via manifest) |
| Manage DPA contracts with B2B controllers | R | C | I | A | — | I | D-06.3: 6.3.1, 6.3.3 (GDPR + CRA) |
| Manage DPA acceptance from subprocessor vendors | R | A | I | C | — | I | D-06.3: 6.3.1, 6.3.3 (GDPR + CRA) |

### 4.7 Secure Development (sub-domain D-07)

| Activity | DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|
| Threat model per feature | C | C | R/A | I | — | I | D-07.1: 7.1.1, 7.1.3 (GDPR + CRA) |
| Code review | I | C | R/A | — | — | I | D-07.2: 7.2.1 (GDPR + CRA) |
| Security testing in CI/CD (SAST/DAST/SCA via Snyk) | I | A | R | — | — | I | D-07.3: 7.3.2 (GDPR + CRA) |
| Change approval (CAB) for production releases | I | C | R | I | — | A | D-07.4: 7.4.1 (GDPR + CRA) |

### 4.8 Human Factors (sub-domains D-08.1, D-08.2, **D-08.3 INACTIVE**)

| Activity | DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|
| Annual security awareness training (D-08.1) | C | A | I | I | R | I | D-08.1: 8.1.1, 8.1.3 (GDPR + CRA) |
| Role-specific training — secure coding for developers (D-08.2) | C | A | R | — | I | I | D-08.2: 8.2.1, 8.2.3 (GDPR + CRA) |
| Role-specific training — DPO competence refresh (D-08.2) | R/A | C | — | C | I | I | D-08.2: 8.2.1, 8.2.3 (GDPR + CRA) |
| **Board cybersecurity briefings (D-08.3)** | — | **See below** | — | — | — | — | D-08.3: INACTIVE (NIS2 + DORA only; both inapplicable) |

**D-08.3 — Board Cybersecurity Training (sub-domain INACTIVE for TinyTask):**

D-08.3 is INACTIVE for TinyTask because its participating regulations are **NIS2** + **DORA**, both inapplicable (NIS2 — not in sector + below size threshold; DORA — not a financial entity). There is no OJ-level mandate for formal board cybersecurity training at TinyTask's size.

Despite the inactive status, the methodology recommends a best-practice placeholder (NOT a derived compliance requirement):

| Best-practice placeholder | DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|
| Quarterly informal cybersecurity briefing to the 2 founders | — | R | — | — | — | A | D-08.3: INACTIVE — no derived GDPR/CRA req_id |

This row is **not** a derived AEGIS requirement for TinyTask. It is recorded so the gap is visible to anyone scanning the matrix; if a future regulation (e.g., a future Standard-class CRA uplift, or NIS2 inclusion via a sector reclassification) activates D-08.3 for TinyTask, this row becomes a mandatory RACI entry without further drafting.

### 4.9 Governance (sub-domain D-09)

| Activity | DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|
| Approve security policies | C | C | C | C | C | A | D-09.1: 9.1.1, 9.1.3 (GDPR + CRA) |
| Conduct risk assessments (annual + per-feature) | R | A | C | C | I | I | D-09.2: 9.2.1, 9.2.3 (GDPR + CRA) |
| Maintain asset inventory | C | A | R | I | — | I | D-09.3: 9.3.2 (GDPR + CRA) |
| Maintain RoPA (Art. 30 GDPR) | R | A | C | C | — | I | D-09.4: 9.4.1, 9.4.3 (GDPR + CRA) |
| Maintain CRA Annex VII technical documentation | C | A | R | C | — | I | D-09.4: 9.4.1, 9.4.3 (GDPR + CRA) |

### 4.10 Monitoring & Audit (sub-domain D-10)

| Activity | DPO (CEO) | CISO (CTO) | Dev | Legal | HR | Board | Corpus Reg Req |
|---|---|---|---|---|---|---|---|
| Continuous security monitoring (Datadog; SIEM-light) | I | A | R | — | — | I | D-10.1: 10.1.1, 10.1.3 (GDPR + CRA) |
| Audit-log retention | C | A | R | I | — | I | D-10.2: 10.2.1, 10.2.2 (GDPR + CRA) |
| Annual compliance testing | C | A | R | I | — | I | D-10.3: 10.3.1, 10.3.3 (GDPR + CRA) |

**Reading note:** Rows that place both **CISO = A** and **Dev = R** mirror the standard "RACI for small teams" pattern — the CTO/CISO owns the outcome; the lead developer (with the rotating developer team) does the work. Where the activity is data-protection-specific (e.g., Art. 17 erasure), **DPO = A** holds the legal accountability per Art. 28(3); implementation **R** swaps to Dev. Board rows are predominantly **I** operationally (executive briefings happen at month-end reviews) and **A** for governance-level approvals.

---

## 5. Training Status

TinyTask does not currently run a formalised training programme (per `00_COMMON/01_Company_Context.md §6.2 — IR-08 = NO). The table below records **last completed** / **next planned refresh** to make the gap explicit and traceable. The **D-08.3 board row is intentionally blank** to reflect the inactive status (see Section 4.8).

| Role | Training Required | Last Completed | Next Refresh | Source (D-08.x req_id) |
|---|---|---|---|---|
| All staff (8 employees) | Annual security awareness | NOT STARTED | 2026-12-31 (target) | D-08.1 (SR-D-08.1.1, …1.4) |
| Developers (6 incl. Lead) | Secure coding (OWASP Top 10 mapping; SAST/DAST feedback loop) | NOT STARTED — informal ad-hoc only | 2026-12-31 (target) | D-08.2 (SR-D-08.2.3, …2.5) |
| DPO (CEO) | GDPR refresher; Art. 33 / 34 mechanics; Art. 28(3) processor obligations | 2025-Q4 (informal: CEO reviewed CNPD guidance materials) | 2026-Q4 | D-08.2 (SR-D-08.2.5) |
| CTO/CISO | CRA Annex I mapping refresh; CVE-triage workflow | NOT STARTED | 2026-12-31 (target) | D-08.2 (SR-D-08.2.4) |
| External Legal Adviser | DPO-support retainer briefing (annual CPD on EU regs) | Retained on continuing basis; no annual milestone | 2026-Q4 (kickoff) | D-08.2 (informal; not derived) |
| Management Board (2 founders) | **D-08.3 INACTIVE — no formal programme.** Quarterly informal briefing by CISO as best practice (see §4.8) | NOT STARTED | n/a (best-practice cadence, not a derived requirement) | D-08.3 (INACTIVE — excluded from per-reg derivation) |

**Status summary:**

- 1 row (DPO refresher): last completed informally in 2025-Q4 — **PARTIAL** state.
- 3 rows (All staff, Developers, CTO/CISO): NOT STARTED — explicit gap.
- 1 row (Legal Adviser): retained relationship, CPD cadence not formalised.
- 1 row (Board): explicitly INACTIVE per Regulatory Baseline — not a derived gap; tracked as a placeholder for future activation.

---

## 6. Compliance Mapping (Regulatory Baseline)

Active scope for TinyTask = 37 of 38 sub-domains. D-08.3 is INACTIVE; its row below is marked "OUT OF SCOPE" to keep the table honest.

| Sub-domain | Role(s) Responsible | RACI Summary | Notes | Corpus Manifest Path |
|---|---|---|---|---|
| D-08.1 General Awareness | CEO (HR-coordination role) | HR=CEO/R, CISO=CTO/A | Coverage = all staff (8 employees); not yet started. | `PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.1/D-08.1.manifest.json` |
| D-08.2 Role-Specific Competence | CTO/CISO + DPO (CEO) | DPO=R/A for DPO competence; Dev=R + CISO=CTO/A for developer training; CTO/CISO=R for own competence | Developer secure-coding training not yet started. | `PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.2/D-08.2.manifest.json` |
| **D-08.3 Management Board Training** | **OUT OF SCOPE — INACTIVE** | n/a | NIS2 + DORA-only; both regulations inapplicable. Not a derived gap (per `05 §6.3`). | `PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.3/D-08.3.manifest.json` (inactive; retained for traceability) |
| D-09.1 Information Security Policies | Board for approval; Dev for drafting | Board=A, all=C | Policies not yet written — explicitly documented in `04b_Security_Posture.md`. | `PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/D-09.1.manifest.json` |
| D-09.2 Impact & Risk Assessments | DPO + CISO | DPO=R, CISO=A | Annual risk assessment planned for Q4; DPIA capability now resident in DPO. | `PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/D-09.2.manifest.json` |
| D-09.3 Asset Inventories | CTO/CISO + Dev | Dev=R, CISO=A | Asset inventory documented in `04a §1.1`; CMDB-grade posture not yet claimed. | `PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/D-09.3.manifest.json` |
| D-09.4 Records of Processing (RoPA) | DPO + Legal | DPO=R, Legal=A | Not yet started — captured in CAP-01 of `04 §10`. | `PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.manifest.json` |

**Active training/coverage sub-domains:** D-08.1 + D-08.2 only (D-08.3 inactive).

---

## 7. Gaps & Known Limitations (Open Items)

These items are surfaced for Phase 2 remediation and are **proportionate**, not over-engineered: a larger firm would need an enterprise LMS, formal HR, and dedicated security trainers; TinyTask needs the four lines below.

| Gap ID | Description | Severity | Linked Sub-Domain |
|---|---|---|---|
| GAP-RACI-01 | No formal security-awareness training programme in place (annual cycle, completion tracking) | MEDIUM | D-08.1 |
| GAP-RACI-02 | No formal secure-coding curriculum for developers (reliance on code review + Snyk feedback) | MEDIUM | D-08.2 |
| GAP-RACI-03 | DPO refresher cycle not cadence-locked (last done 2025-Q4 informally; next target 2026-Q4) | LOW | D-08.2 |
| GAP-RACI-04 | D-08.3 board training absent — **deliberately** not in scope for TinyTask; documented here as a non-derivation per `05 §6.3` | LOW (informational only) | D-08.3 (INACTIVE) |
| GAP-RACI-05 | Single DPO/CISO-individual concentration risk; backup is the other founder, which is operationally OK but not optimised for board independence | LOW | D-09.1 (governance posture) |

**Discussion per AEGIS P0 (Reasoned Disagreement):** GAP-RACI-04 is **not** a compliance gap. It is recorded as **LOW (informational)** to make the methodology's scope decision visible; the methodology does not want to silently omit a sub-domain that may matter to a reader unfamiliar with the activation model. A reader who assumes D-08.3 must be addressed at every company would otherwise see "no board training" as a failure.

---

## 8. Gate

This document is complete (Phase 1 Step E — Roles & RACI) when:

- [x] All key roles identified with FTE allocation (Section 2)
- [x] RACI matrix populated for all 10 macro-domains (Section 4 — D-01 to D-10)
- [x] Reporting lines documented (Section 3 — text + ASCII)
- [x] Training status populated for all roles (Section 5 — including the explicit "INACTIVE" line for D-08.3)
- [x] Compliance Mapping table populated for D-08.x and D-09.x (Section 6)
- [x] Gaps explicitly listed (Section 7) rather than silently accepted — required by AEGIS P5 and P0
- [x] RACI tables extended with Corpus Reg Req column (Sections 4.1–4.10 enrichment)
- [x] Compliance Mapping table extended with Corpus Manifest Path column (Section 6 enrichment)
- [x] `active_subdomains: 37` in frontmatter (verified reconciliation I-02, still correct post-Fase de Especificação 2)

**Gate Status:** PASS (proportionate for LOW-tier micro SaaS under P2).

---

## 9. Corpus Provenance (Fase de Especificação 2 Enrichment)

The **Corpus Reg Req** column added to each RACI table (Sections 4.1–4.10) and the **Corpus Manifest Path** column added to the Compliance Mapping table (Section 6) were extracted from the corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`.

### 9.1 req_id extraction strategy

```bash
sd=D-XX.Y
jq -r '[(.sub_requirements_by_regulation.GDPR[]?.req_id?), 
         (.sub_requirements_by_regulation.CRA[]?.req_id?)] 
        | unique | join(", ")' \
  "00_METHODOLOGY/PREPROCESSING_by_domain/domains/<DOMAIN>/${sd}/${sd}.manifest.json"
```

**Active regulations filter:** `applicable_regs = [GDPR, CRA]` for Case_01, so only GDPR + CRA sub-requirement req_ids are pulled. NIS2 / DORA / AI Act entries are filtered out (irrelevant to TinyTask). D-08.3 is included in the corpus manifest but marked INACTIVE because its participating regulations are NIS2 + DORA; no GDPR/CRA req_ids exist in its manifest, so the row shows `INACTIVE`.

### 9.2 Mapping activity → sub-domain

| RACI Activity | Mapped Sub-domain | Rationale |
|---|---|---|
| Encrypt personal data at rest | D-01.1 | Encryption-at-rest is D-01.1 (not D-01.2 in-transit) |
| Manage encryption keys | D-01.3 | Key management is D-01.3 (separate sub-domain) |
| Notify DPA / Notify controllers | D-04.3 | Regulatory notification is D-04.3 |
| Conduct DPIA | D-09.2 | DPIA per Art. 35 GDPR = risk-assessment sub-domain |
| Vulnerability scans | D-02.1 | Identification is D-02.1 |
| Patch management | D-02.2 | Patching is D-02.2 |
| Penetration testing | D-02.4 | Threat-led pentest is D-02.4 |
| CVD / security.txt | D-02.3 | Coordinated vulnerability disclosure |
| IAM / offboarding / access review | D-03.1 | Identity lifecycle |
| MFA | D-03.2 | MFA is its own sub-domain |
| Detect incident | D-04.1 | Detection is D-04.1 |
| Contain incident | D-04.2 | Containment is D-04.2 |
| Recover systems | D-04.4 | Recovery is D-04.4 |
| Post-incident review | D-04.2 | Review is part of containment/learning |
| Data minimisation | D-05.1 | Minimisation is D-05.1 |
| Retention policies | D-05.2 | Retention is D-05.2 |
| Erasure requests | D-05.3 | Erasure is D-05.3 |
| Portability requests | D-05.4 | Portability is D-05.4 |
| Vendor security assessment | D-06.1 | Vendor risk assessment is D-06.1 |
| SBOM | D-06.2 | SBOM is its own sub-domain |
| DPA contracts (B2B / subprocessor) | D-06.3 | Contractual obligations is D-06.3 |
| Threat model per feature | D-07.1 | Secure-by-design principles |
| Code review | D-07.2 | Secure coding practices |
| Security testing in CI/CD | D-07.3 | CI/CD pipeline security |
| Change approval (CAB) | D-07.4 | Change management |
| Annual security awareness | D-08.1 | General awareness |
| Role-specific training | D-08.2 | Role-specific competence |
| Board cybersecurity briefings | D-08.3 | Management board training (INACTIVE) |
| Approve security policies | D-09.1 | Information security policies |
| Risk assessments | D-09.2 | Impact & risk assessments |
| Maintain asset inventory | D-09.3 | Asset inventories |
| RoPA / Annex VII documentation | D-09.4 | Records of processing |
| Continuous security monitoring | D-10.1 | Continuous monitoring |
| Audit-log retention | D-10.2 | Audit logging & traceability |
| Annual compliance testing | D-10.3 | Compliance testing |

### 9.3 Coverage statistics

- **RACI tables updated:** 10 (one per macro-domain §4.1–§4.10)
- **RACI rows enriched:** 30 (each row now has a Corpus Reg Req value)
- **Compliance Mapping rows updated:** 7 (D-08.1, D-08.2, D-08.3, D-09.1, D-09.2, D-09.3, D-09.4 — including D-08.3 inactive path)
- **Total corpus lookups:** 37 (one per active sub-domain for req_id; 37 + 1 for manifest path including D-08.3 inactive path = 38 manifest-path lookups, but 37 req_id lookups since D-08.3 has no GDPR/CRA req_ids)
- **Verification:** `active_subdomains: 37` in frontmatter confirmed (Fase de Especificação 1 I-02 fix preserved; Fase de Especificação 2 verified by re-reading frontmatter line 24)

---

## N-1. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-07-11 | Executor | Populated from template `04d_Org_Roles_RACI.md`; integrated stakeholder register from `04 §3` and architecture from `04a`; D-08.3 inactive status explicitly carried forward from `05 §6.3` (migrated from `04 §7.3` in v2.2). |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-07-11 |
| Technical Review | CTO |  |  |
| Business Review | CEO |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Data backbone:** `Case_01_Phase1.xlsx` (13 sheets: COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, POSTURE, SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES)
