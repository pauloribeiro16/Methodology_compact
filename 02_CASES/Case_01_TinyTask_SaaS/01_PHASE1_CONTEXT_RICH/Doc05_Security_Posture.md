---
document_id: AEGIS-P1-04b
title: Security Posture Assessment (Implementation Posture)
phase: 1
version: 1.2
created: 2026-07-11
updated: 2026-08-27
author: Executor (Fase de Especificação 1 reconciliation; Fase de Especificação 2 corpus enrichment; Implementation Posture transition; v1.6 maturity redesign)
status: DEPRECATED_FOR_MATURITY
status_history:
  - { date: '2026-08-07', from: CORPUS_ENRICHED, to: DEPRECATED_FOR_POSTURE,
      reason: 'Implementation Posture model adopted — resolves PHASE1_STRATEGY §7 contradiction' }
  - { date: '2026-08-27', from: DEPRECATED_FOR_POSTURE, to: DEPRECATED_FOR_MATURITY,
      reason: 'Maturity redesigned per MATURITY_MODEL_CSF_STRICT.md (CSF 2.0 strict, two scales, evidence-based); see Folio VIII of Case_01_P1_Dashboard.html' }
maturity_owner: 00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md
posture_owner: 13_Framework_Mapping_Matrix.md
note: >
  Este documento mantém-se como INPUT qualitativo (postura observada).
  v1.6 — A avaliação de maturidade foi movida para
  00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §3-§6 (referencial único
  CSF 2.0 §3.4, Tiers T1-T4 ao nível Organisation/Function, EvidenceItem
  nodes no grafo, sem maturity_cur/maturity_tgt scalars no sub-domínio).
  Ver Case_01_P1_Dashboard.html Folio VIII para visualização.
  A avaliação de postura (Implementation Posture) continua em
  02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md §4-5.
case_study: TinyTask Lda.
inputs:
  - Doc03_Company_Context_Assessment.md
  - Doc04_Architecture_DataInventory.md
  - Doc08_Regulatory_Applicability.md
outputs:
  - Doc11_Structured_Compliance_Matrix.md
applicable_regs: [GDPR, CRA]
active_subdomains: 37
inactive_subdomains: [D-08.3]
related_documents:
  - 04a_Architecture_DataInventory.md
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/index.md
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/
---

> ⚠️ **DEPRECATED FOR POSTURE (2026-08-07).** A avaliação e o modelo de
> postura vivem agora em
> `02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` §4-5. Este documento
> mantém-se como input qualitativo (postura observada). Ver `status_history`
> no frontmatter.

> **Fase de Especificação 1 Reconciliation Note (2026-08-06)**
> Rich Mode copy of legacy `01_PHASE1_CONTEXT/04b_Security_Posture.md` (v1.0). Fase de Especificação 1 changes:
> - **I-10 (status DRAFT → RECONCILED):** Fase de Especificação 1 milestone.
> - Body content unchanged from legacy. Fase de Especificação 2 will replace `SubDomains/` paths with the new `PREPROCESSING_by_domain/domains/` corpus paths.
>
> **Fase de Especificação 2 Enrichment Note (2026-08-06)**
> - **Status: RECONCILED → CORPUS_ENRICHED.** Section 2 (Per-Macro-Domain Assessment) extended with two corpus-derived fields per macro-domain: **Target fit_criterion** (verbatim from `D-XX.Y.json` `requirements.high_level.yaml.fit_criterion`, truncated to ~100 chars) and **Verification Method** (from same path, `verification_method` field). One representative sub-domain selected per macro-domain (D-01.1, D-02.1, D-03.2, D-04.3, D-05.2, D-06.1, D-07.3, D-08.1, D-09.4, D-10.2). New §7 Corpus Provenance documents the selection rationale and sources. 10 macro-domain sections enriched.

# Security Posture Assessment

## 1. Assessment Methodology

TinyTask is assessed as a low-tier micro SaaS with 8 employees and managed-cloud infrastructure. Current posture measures implementation status today, not the target state. Target posture is proportional to TinyTask's profile but still aligned with active GDPR and CRA SubDomains fit criteria.

| Level | Label | Description |
|---|---|---|
| State | Label | Description |
|---|---|---|
| NOT IMPLEMENTED | None | No controls in place |
| PARTIAL | Partial | Documented or partially implemented, lacking formal verification |
| IMPLEMENTED | Fully Implemented | Implemented, monitored, measured, and regularly reviewed |

Assessment evidence is drawn from `04a_Architecture_DataInventory.md`, `04_Company_Context_Assessment.md`, and `05_Regulatory_Applicability.md`. The active Regulatory Baseline scope is 37 of 38 SubDomains for `applicable_regs = [GDPR, CRA]`; D-08.3 is inactive because it only participates in NIS2 and DORA.

## 2. Per-Domain Assessment

### D-01 Data Protection — Implementation Status: PARTIAL

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Encryption at rest | Implemented for main database, backups, and logs | STORE-01, STORE-02, STORE-03 in 04a Section 2.1 | Provider-managed AES-256 encryption; no customer-managed HSM |
| Encryption in transit | Implemented for all documented production flows | FLOW-01 to FLOW-05 in 04a Section 2.2 | TLS 1.3 used for main app and Auth0; third-party APIs use TLS 1.2 or higher |
| Key management | Basic cloud KMS | SYS-04 in 04a Section 1.1 | Manual key rotation; no formal key ceremony or dual control |
| Data integrity | Basic application/database controls | SYS-01, SYS-03, SYS-05 | Database constraints and backup checks exist; no formal integrity verification schedule |

**Target Posture**: IMPLEMENTED  
**Gap**: Operational evidence & verification cadence missing  
**Target fit_criterion** (from corpus `D-01.1.json` requirements.high_level.yaml.fit_criterion, truncated): "AES-256 (or stronger) symmetric encryption is applied to all data-at-rest storage volumes holding the in-scope data class..."
**Verification Method** (from corpus): TEST
**Notes**: Current evidence supports D-01.1, D-01.2, and part of D-01.3/D-01.4. The gap is formal key lifecycle documentation, periodic restore/integrity tests, and review evidence for GDPR Art. 32 and CRA Annex I Part I confidentiality/integrity controls. Relevant Regulatory Baseline files: [D-01.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.1.md), [D-01.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.2.md), [D-01.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.3.md), [D-01.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.4.md).

### D-02 Vulnerability Management — Implementation Status: PARTIAL

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Vulnerability scanning | Weekly Snyk scan for application dependencies | SYS-01 release pipeline; STORE-03 monitoring logs | Results are reviewed manually; no documented acceptance or exception process |
| Patch management | Manual patching | GitHub pull requests and dependency updates | No formal critical/high SLA; fixes depend on developer availability |
| Pen testing | Informal self-testing only | No external report | No threat-led or independent penetration test performed |
| CVD policy | Not published | No security.txt or public vulnerability policy | CRA vulnerability handling remains a material gap |

**Target Posture**: IMPLEMENTED  
**Gap**: Operational evidence & verification cadence missing  
**Target fit_criterion** (from corpus `D-02.1.json` requirements.high_level.yaml.fit_criterion, truncated): "An ID.RA-01 vulnerabilities-identified-validated-recorded register is maintained at the DORA-cadenced `continuous + at-l..."
**Verification Method** (from corpus): TEST
**Notes**: D-02 is partial posture because scanning exists but vulnerability intake, prioritisation, disclosure, and patch SLAs are ad hoc. This is consistent with the existing supply-chain readiness finding that component vulnerability management is manual. Relevant Regulatory Baseline files: [D-02.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.1.md), [D-02.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.2.md), [D-02.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.3.md), [D-02.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.4.md).

### D-03 Access Control — Implementation Status: PARTIAL

| Control | Current | Evidence | Notes |
|---|---|---|---|
| IAM system | Auth0 for customer and administrator identity | SYS-02 in 04a Section 1.1 | Managed identity service reduces implementation burden |
| MFA | Enforced for administrators only | 04a Section 1.4 | Customer MFA is optional; not universal |
| RBAC | Basic application roles | SYS-01, SYS-02, SYS-03 | Basic owner/member/admin model; quarterly access reviews not documented |
| Privileged access management | No dedicated PAM | Cloud IAM and GitHub organisation | Least privilege is informal and handled by CTO |
| Default secure configs | Partial | Auth0 defaults, cloud provider security groups | No documented secure baseline for all services |

**Target Posture**: IMPLEMENTED  
**Gap**: Operational evidence & verification cadence missing  
**Target fit_criterion** (from corpus `D-03.2.json` requirements.high_level.yaml.fit_criterion, truncated): "A single authentication-mechanism architecture is operated, calibrated to the DORA strong-authentication floor when DORA..."
**Verification Method** (from corpus): TEST
**Notes**: Access control is defined enough for a small SaaS but not managed. The main gaps are documented access reviews, customer MFA posture, privileged access logging, and formal secure defaults. Relevant Regulatory Baseline files: [D-03.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.1.md), [D-03.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.2.md), [D-03.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.3.md), [D-03.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.4.md).

### D-04 Incident Response — Implementation Status: PARTIAL

| Control | Current | Evidence | Notes |
|---|---|---|---|
| IR plan | Basic plan exists | Informal CTO-led incident steps from company context | No tested playbook and no incident roles beyond CTO/developers |
| Detection capability | Datadog or equivalent alerts | STORE-03 and FLOW-03 in 04a | No SIEM, EDR, IDS, or 24/7 monitoring |
| Notification process | Informal DPO/CTO escalation | GDPR/CRA interaction notes in Doc 04 and Doc 05 | No tested 24h CRA early-warning / 72h GDPR breach notification workflow |
| Recovery procedures | Backups exist | STORE-02 and SYS-05 in 04a | Restore testing is not scheduled or evidenced |

**Target Posture**: IMPLEMENTED  
**Gap**: Operational evidence & verification cadence missing  
**Target fit_criterion** (from corpus `D-04.3.json` requirements.high_level.yaml.fit_criterion, truncated): "A unified multi-recipient notification pipeline is operated generating per-regulation submissions from a single underlying..."
**Verification Method** (from corpus): TEST
**Notes**: Incident response remains ad hoc. Backups and basic alerts exist, but containment, regulatory notification, and recovery evidence are not managed. Relevant Regulatory Baseline files: [D-04.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.1.md), [D-04.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.2.md), [D-04.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.3.md), [D-04.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.4.md).

### D-05 Data Lifecycle — Implementation Status: PARTIAL

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Data minimisation | Informal minimisation in product design | 04a Sections 2.2 and 2.3 | Payment card data is kept out of TinyTask by using Stripe |
| Retention policies | Not formally documented | STORE-01 to STORE-03 in 04a Section 2.1 | Retention periods are stated for this inventory but not yet approved as policy |
| Erasure procedures | Manual support workflow | 04a Sections 2.3 and 2.4 | No self-service DSAR portal; backup expiry relied on for residual copies |
| Data portability | Support-assisted export | 04a Section 2.4 | No automated export for all data categories |

**Target Posture**: IMPLEMENTED  
**Gap**: Operational evidence & verification cadence missing  
**Target fit_criterion** (from corpus `D-05.2.json` requirements.high_level.yaml.fit_criterion, truncated): "A 3-axis retention/archiving architecture is operated with explicit axis-segregated hand-offs at the personal-data / upd..."
**Verification Method** (from corpus): TEST
**Notes**: Data lifecycle controls are plausible for a micro SaaS but remain policy-light and manually operated. Formal retention approval, DSAR tracking, and export/delete procedures are needed. Relevant Regulatory Baseline files: [D-05.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.1.md), [D-05.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.2.md), [D-05.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.3.md), [D-05.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.4.md).

### D-06 Supply Chain — Implementation Status: PARTIAL

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Vendor assessment | Annual informal vendor review | Cloud services table in 04a Section 1.3 | Evidence collection is not standardised |
| SBOM | Not implemented | Company context B6 and Doc 05 GAP-02 | No CycloneDX/SPDX generation in CI/CD |
| Contract clauses | Partial | DPAs with AWS/Auth0/Stripe/Datadog; B2B DPA gap remains | Supplier DPAs exist, but B2B processor DPA standardisation is incomplete |
| Boundary management | Ad hoc | FLOW-03, FLOW-04, FLOW-05 in 04a | No formal subprocessor register or data-flow review cadence |

**Target Posture**: IMPLEMENTED  
**Gap**: Operational evidence & verification cadence missing  
**Target fit_criterion** (from corpus `D-06.1.json` requirements.high_level.yaml.fit_criterion, truncated): "A 4-tier vendor-risk-assessment architecture is operated with explicit tier separation (processor-tier GDPR / supplier-t..."
**Verification Method** (from corpus): TEST
**Notes**: Supply-chain posture is intentionally modest. The highest CRA gap is SBOM absence, combined with weak vendor evidence and subprocessor tracking. Relevant Regulatory Baseline files: [D-06.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.1.md), [D-06.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.2.md), [D-06.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.3.md), [D-06.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.4.md).

### D-07 Secure Development — Implementation Status: PARTIAL

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Secure-by-design | Basic consideration during feature work | SYS-01 development practice | No formal threat-model template per feature |
| Secure coding | OWASP guidelines and peer code review | GitHub pull requests and developer practice | Code review exists but security checklist is not consistently recorded |
| CI/CD security | Basic dependency scanning | Weekly Snyk scan for SYS-01 | No DAST, secrets scanning baseline, or SBOM release artefact |
| Change management | Pull request review | GitHub branch protection for main branch | No formal release risk classification or CAB, appropriate for micro SaaS |

**Target Posture**: IMPLEMENTED  
**Gap**: Operational evidence & verification cadence missing  
**Target fit_criterion** (from corpus `D-07.3.json` requirements.high_level.yaml.fit_criterion, truncated): "For 100% of covered production releases, a release evidence pack exists before deployment or dissemination and contains..."
**Verification Method** (from corpus): TEST
**Notes**: Secure development is the strongest TinyTask area because it already has developer-led practices, OWASP guidance, PR review, and basic scanning. It meets a proportional target for a low-tier micro SaaS, but still needs CRA evidence hardening through SBOM, release notes, and documented security review. Relevant Regulatory Baseline files: [D-07.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.1.md), [D-07.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.2.md), [D-07.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.3.md), [D-07.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.4.md).

### D-08 Human Factors — Implementation Status: PARTIAL

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Security awareness | Annual awareness training | Internal lightweight training session | No phishing simulations or completion dashboard |
| Role-specific training | Informal developer learning | OWASP guidance used by developers | No tracked curriculum for CTO, developers, support, or DPO role |
| Board training | Not applicable to active scope | D-08.3 inactive for TinyTask | D-08.3 participates only in NIS2 and DORA; not a TinyTask gap |

**Target Posture**: IMPLEMENTED  
**Gap**: Operational evidence & verification cadence missing  
**Target fit_criterion** (from corpus `D-08.1.json` requirements.high_level.yaml.fit_criterion, truncated): "A documented training programme is maintained with four distinct audience routes operating in parallel (DPO-catalysed pr..."
**Verification Method** (from corpus): TEST
**Notes**: Basic annual awareness is realistic for 8 employees but insufficient for role-specific CRA/GDPR competence evidence. D-08.3 remains out of scope, not a missing control. Relevant Regulatory Baseline files: [D-08.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.1.md), [D-08.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.2.md), [D-08.3 inactive](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.3.md).

### D-09 Governance & Documentation — Implementation Status: PARTIAL

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Security policies | Basic policies only | Password/access expectations and this Phase 1 documentation | No complete information security policy set |
| Risk assessment | Informal | Product and compliance risks discussed by CTO/CEO | No documented risk register or periodic review |
| Asset inventory | Initial inventory created | 04a Sections 1 and 2 | No CMDB; 04a is the first structured inventory |
| RoPA | Not complete | Doc 04 CAP-01 / Doc 05 GAP-01 | GDPR Art. 30 records are not yet maintained as an operational artefact |

**Target Posture**: IMPLEMENTED  
**Gap**: Operational evidence & verification cadence missing  
**Target fit_criterion** (from corpus `D-09.4.json` requirements.high_level.yaml.fit_criterion, truncated): "A 5-parallel-documentation-regimes architecture is established with explicit governance-body hand-offs at the documentat..."
**Verification Method** (from corpus): TEST
**Notes**: Governance is a major gap because active GDPR/CRA obligations require evidence artefacts, not only technical controls. The architecture inventory is a start, but RoPA, Annex VII documentation, risk assessment, and policy ownership remain immature. Relevant Regulatory Baseline files: [D-09.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.1.md), [D-09.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.2.md), [D-09.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.3.md), [D-09.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.4.md).

### D-10 Monitoring & Audit — Implementation Status: PARTIAL

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Continuous monitoring | Datadog or equivalent for core app metrics | STORE-03 and FLOW-03 in 04a | Coverage is basic and not mapped to all active security events |
| Audit logging | Partial application and authentication logging | SYS-01, SYS-02, STORE-03 | 30-day retention; no formal log review process |
| Compliance testing | Ad hoc internal checks | Snyk scan and manual review | No scheduled GDPR/CRA evidence review or control test plan |

**Target Posture**: IMPLEMENTED  
**Gap**: Operational evidence & verification cadence missing  
**Target fit_criterion** (from corpus `D-10.2.json` requirements.high_level.yaml.fit_criterion, truncated): "A layered 4-audit-records architecture is established with explicit scope-layer hand-offs at the audit-records evidence..."
**Verification Method** (from corpus): TEST
**Notes**: Monitoring is partial posture because TinyTask has observability but not security monitoring governance. There is no SIEM, no documented alert taxonomy, no log review cadence, and no formal compliance testing cycle. Relevant Regulatory Baseline files: [D-10.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.1.md), [D-10.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.2.md), [D-10.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.3.md).

## 3. Summary Dashboard

| Macro-domain | Current Posture | Target Posture | Gap Analysis |
|---|---|---|---|
| D-01 Data Protection | PARTIAL | IMPLEMENTED | Key lifecycle documentation & automated integrity testing |
| D-02 Vulnerability Management | PARTIAL | IMPLEMENTED | Patch SLAs, vulnerability disclosure & automated CI gating |
| D-03 Access Control | PARTIAL | IMPLEMENTED | Access reviews, customer MFA enforcement & logging |
| D-04 Incident Response | PARTIAL | IMPLEMENTED | Incident runbooks, containment playbooks & SA reporting |
| D-05 Data Lifecycle | PARTIAL | IMPLEMENTED | Formal retention approval, DSAR portal & export routines |
| D-06 Supply Chain | PARTIAL | IMPLEMENTED | Automated SBOM generation & vendor DPA tracking |
| D-07 Secure Development | PARTIAL | IMPLEMENTED | Threat modeling evidence & security release packs |
| D-08 Human Factors | PARTIAL | IMPLEMENTED | Role-specific training & awareness metrics |
| D-09 Governance & Documentation | PARTIAL | IMPLEMENTED | RoPA maintenance, risk register & policy sign-off |
| D-10 Monitoring & Audit | PARTIAL | IMPLEMENTED | Security monitoring taxonomy, SIEM/log review & audit schedule |
| **OVERALL** | **PARTIAL** | **IMPLEMENTED** | **Operational evidence & automated review cadence required** |

## 4. Top Gaps (feeds Doc 07)

| Rank | Macro-domain | Status | Gap Summary | Priority Remediation |
|---:|---|---:|---|---|
| 1 | D-02 Vulnerability Management | PARTIAL | Weekly Snyk scan exists, but patch SLAs, vulnerability disclosure, and testing are ad hoc | Create vulnerability register, define critical/high SLAs, publish security.txt and CVD policy |
| 2 | D-04 Incident Response | PARTIAL | Basic plan and backups exist, but notification, containment, and recovery are not tested | Create GDPR/CRA incident runbook with 24h/72h timing and run one tabletop exercise |
| 3 | D-09 Governance & Documentation | PARTIAL | RoPA, Annex VII documentation, formal risk assessment, and policy set are incomplete | Create RoPA, Annex VII evidence index, asset inventory owner, and lightweight risk register |
| 4 | D-10 Monitoring & Audit | PARTIAL | Datadog logs are retained for 30 days, but there is no security monitoring programme | Define alert taxonomy, log review cadence, and basic control testing schedule |
| 5 | D-06 Supply Chain | PARTIAL | Vendor review is annual/informal and SBOM is not implemented | Add CycloneDX or SPDX SBOM in CI/CD and maintain a subprocessor evidence register |

## 5. Consistency Check

| Consistency Item | Status | Evidence |
|---|---|---|
| Architecture evidence matches 04a | PASS | SYS-01 to SYS-05, STORE-01 to STORE-03, FLOW-01 to FLOW-05 referenced consistently |
| Regulatory scope matches Doc 04 and Doc 05 | PASS | `applicable_regs = [GDPR, CRA]`; 37 active SubDomains; D-08.3 inactive |
| LOW-tier realism maintained | PASS | No enterprise HSM, SIEM, PAM, SOC, CMDB, or continuous assurance claimed |
| Posture scale used consistently | PASS | Implementation Posture states (IMPLEMENTED, PARTIAL, NOT IMPLEMENTED) applied consistently |
| Evidence and gaps align | PASS | D-02, D-04, D-09, and D-10 are the largest gaps; D-07 is strongest but not enterprise-grade |

## 6. Gate

| Gate Criterion | Status | Evidence |
|---|---|---|
| All 10 macro-domains assessed with implementation posture and evidence | PASS | Section 2 |
| Target posture defined per macro-domain | PASS | Sections 2 and 3 |
| Summary dashboard populated | PASS | Section 3 |
| Top 5 gaps identified | PASS | Section 4 |
| SubDomains references included | PASS | Each macro-domain section links to active Regulatory Baseline files |
| Target fit_criterion extracted per macro-domain | PASS | Section 2 (Fase de Especificação 2 enrichment) |
| Verification Method extracted per macro-domain | PASS | Section 2 (Fase de Especificação 2 enrichment) |

## 7. Corpus Provenance (Fase de Especificação 2 Enrichment)

The **Target fit_criterion** and **Verification Method** fields added to Section 2 were extracted from the per-sub-domain JSON sidecars at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/<D-XX_Domain>/D-XX.Y/D-XX.Y.json`, specifically from the nested path `requirements.high_level.yaml.fit_criterion` and `requirements.high_level.yaml.verification_method`.

**Extraction pattern:**

```bash
sd=D-01.1  # representative for D-01
jq -r '.requirements.high_level.yaml.fit_criterion' \
  00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.json
jq -r '.requirements.high_level.yaml.verification_method' \
  00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.json
```

**Representative sub-domain selection** (one per macro-domain; selection prioritised sub-domain with most-regulatory-density or strictest fit_criterion):

| Macro-domain | Representative sub-domain | Rationale |
|---|---|---|
| D-01 Data Protection | D-01.1 (Data at Rest Encryption) | Foundational CIA control; smallest scope = most testable |
| D-02 Vulnerability Management | D-02.1 (Vulnerability Identification) | Top-of-funnel ID.RA-01 control; SCA + dependency-scanning evidence mapped |
| D-03 Access Control | D-03.2 (Multi-Factor Authentication) | Strictest authentication floor; DORA strong-auth calibration |
| D-04 Incident Response | D-04.3 (Regulatory Notification) | Most time-bound obligation; multi-recipient pipeline |
| D-05 Data Lifecycle | D-05.2 (Retention & Archiving) | Retention schedule is the most measurable aspect |
| D-06 Supply Chain | D-06.1 (Vendor Risk Assessment) | 4-tier architecture is the broadest evidence test |
| D-07 Secure Development | D-07.3 (CI/CD Pipeline Security) | Release evidence pack is the concrete deliverable |
| D-08 Human Factors | D-08.1 (General Awareness) | Active-only sub-domain (D-08.3 inactive); 4-audience-route programme |
| D-09 Governance | D-09.4 (Records of Processing) | Annex VII + RoPA is the most evidence-heavy |
| D-10 Monitoring & Audit | D-10.2 (Audit Logging) | 4-audit-records architecture is the broadest test |

**Notes on corpus structure:** All 10 fit_criteria are aggregated multi-reg fit_criteria (not per-reg) — they capture the convergence point where GDPR + CRA + DORA + NIS2 obligations discharge on a single artefact. For per-reg decomposition, see `D-XX.Y.json`'s `requirements.sub_requirements[]` array, which contains per-reg entries. The "Verification Method" is uniformly `TEST` for high-level Volere fit_criteria at this aggregation level; sub-requirements may carry `INSPECTION`, `DEMONSTRATION`, etc. Total corpus lookups for this section: 10 (one per macro-domain).

## N-1. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-07-11 | Executor | Created TinyTask populated security posture assessment from the 04b template |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-07-11 |
| Technical Review | CTO |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Data backbone:** `Case_01_Phase1.xlsx` (13 sheets: COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, POSTURE, SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES)
