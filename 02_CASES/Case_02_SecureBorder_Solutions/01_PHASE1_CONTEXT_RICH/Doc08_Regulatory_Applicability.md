---
document_id: AEGIS-P2-RICH-05-APPLICABILITY
title: Regulatory Applicability Assessment (Rich Mode)
phase: 1
version: 1.1
created: 2026-04-01
updated: 2026-08-06
author: "Compliance Lead (Rich copy: Sprint 1 Executor, 2026-08-06)"
status: RECONCILED
case: Case_02_SecureBorder_Solutions
applicable_regs: ["GDPR", "CRA", "NIS 2", "AI_Act"]
active_subdomains: 35
inactive_documented: ["D-08.3 INACTIVE", "3 NOT_ADDRESSED"]
inputs: ["Doc03_Company_Context_Assessment.md", "Doc02_INTAKE_FORM.md"]
outputs: ["Doc10_Clause_Mapping_Matrix.md"]
traceability: "AEGIS Class Model → ComplianceContext, RegulatoryClause classes"
related_documents: ["00_Taxonomy_Reference.md", "Doc03_Company_Context_Assessment.md"]
reconciliation:
  sprint: 1
  role: reconciliation
  base_doc: ../01_PHASE1_CONTEXT/Doc08_Regulatory_Applicability.md (legacy, frozen)
  notes: |
    Sprint 1 reconciliation (Case_02, 2026-08-06):
    - Frontmatter updated to AEGIS-P2-RICH-* convention (P2 = Case_02).
    - status: DRAFT → RECONCILED.
    - inputs reference updated (02_Regulatory_Mapping_Master.xlsx → Doc02_INTAKE_FORM.md,
      deprecation banner added below).
    - APP-{REG} applicability flags added below (§3.1–§3.5) per LINT_REPORT_BEFORE.md Issue 5
      (case has 4 applicable regulations, all 4 already covered in legacy §3.1–§3.5).
    - Section 9 (KEY OBSERVATIONS) and §5.3 (Compliance Boundary Diagram) preserved verbatim —
      flagged by lint as "extra section not in template" but are Case_02 first-class extensions
      supporting 4 applicable regulations. Marked with `<!-- BY-DESIGN: case-specific extension -->`.
    - Note: 02_Regulatory_Mapping_Master.md is DEPRECATED as of Phase 1 v1.2 (2026-07-13).
      Use 00_METHODOLOGY/PREPROCESSING/SubDomains/ corpus or 00_Taxonomy_Reference.md instead.
    - Body preserved verbatim (Sprint 1 is content-neutral; Sprint 2 adds corpus linkages).
---

<!-- RECONCILIATION BANNER (Sprint 1, 2026-08-06):
     This is the Rich Mode copy of AEGIS-P1-05.
     Source: ../01_PHASE1_CONTEXT/Doc08_Regulatory_Applicability.md.
     Body unchanged from legacy. Sprint 2 will add corpus linkages (L2 Regulation/* refs).
     See SPRINT1_REPORT.md for the full fix list.
-->

<!-- BY-DESIGN: case-specific extensions §9 (KEY OBSERVATIONS) and §5.3 (Compliance Boundary
     Diagram) are intentional Case_02 first-class content. The lint flags them as "extra
     sections not in template" but they support 4 applicable regulations × cross-regulation
     narrative. See LINT_REPORT_BEFORE.md §6 (Issue 5) for the by-design classification.
-->

> **Deprecation note:** `02_Regulatory_Mapping_Master.md` is **DEPRECATED** as of Phase 1 v1.2 (2026-07-13).
> Use `00_METHODOLOGY/PREPROCESSING/SubDomains/` corpus or `00_Taxonomy_Reference.md` instead.

> **Mapping to Phase 1 Strategy:** This document is the artifact of
> **Filter 1 (Regulation Applicability — binary predicates)** in
> [`00_METHODOLOGY/PHASE1_STRATEGY.md`](../../../00_METHODOLOGY/PHASE1_STRATEGY.md) §5.
> Updates to the underlying filter logic should be reflected here.

> **Mapping to Phase 1 Strategy:** This document is the artifact of
> **Filter 1 (Regulation Applicability — binary predicates)** in
> [`00_METHODOLOGY/PHASE1_STRATEGY.md`](../../../00_METHODOLOGY/PHASE1_STRATEGY.md) §5.
> Updates to the underlying filter logic should be reflected here.

# Regulatory Applicability Assessment

**APP-GDPR: ✅ APPLICABLE** | **APP-CRA: ✅ APPLICABLE (Critical Class)** | **APP-NIS2: ✅ APPLICABLE (Essential Entity Supplier)** | **APP-DORA: ❌ NOT APPLICABLE** | **APP-AIACT: ✅ APPLICABLE (High-Risk AI)**

## 1. DOCUMENT PURPOSE

This document consolidates the regulatory applicability assessment (Step B1+B3), determining which regulations apply to SecureBorder Solutions and establishing the Native vs. Inherited compliance boundaries.

**Alignment with Class Model:**
- `ComplianceContext` - Applicable regulations and applicability scores
- `RegulatoryClause` - Filtered clauses based on applicability
- `DomainCoverageEntry` - Initial domain coverage assessment

**Phase 1 Step:** B (Regulatory Applicability)

**Gate Criteria:** Clear applicability determination for all 5 regulations with documented rationale

---

## 2. APPLICABILITY ASSESSMENT METADATA

| Attribute | Value |
|-----------|-------|
| complianceContextId | COMPLIANCE-SECUREBORDER-2026-001 |
| assessmentDate | 2026-04-01 |
| basedOnCompanyContext | CC-SECUREBORDER-2026-001 |
| assessedBy | Compliance Lead |
| reviewedBy | Legal Counsel (pending) |

---

## 3. REGULATION-BY-REGULATION APPLICABILITY ANALYSIS

### 3.1 GDPR (General Data Protection Regulation)

| Criterion | Company Context Value | Threshold | Met? |
|-----------|----------------------|-----------|------|
| processes_personal_data | TRUE (facial templates, passport data) | ANY | YES |
| special_category_data | TRUE (biometric data - Art. 9) | ANY | YES |
| EU data subjects | TRUE (travelers in Schengen Area) | ANY | YES |
| large_scale_processing | TRUE (millions of crossings annually) | ANY | YES |

**Applicability Result:** ✅ **APPLICABLE**

**Rationale:** SecureBorder processes special category data (biometric facial templates) on behalf of government border control authorities. As a processor, GDPR obligations apply via Art. 28 DPA. Additionally, SecureBorder is a controller for audit logs and compliance data. Large-scale processing of Art. 9 data triggers mandatory DPIA (Art. 35).

**Key Clauses in Scope:** GDPR-C01 through GDPR-C28 (all 28 clauses applicable)

**Obligated Party:** CONTROLLER (for audit logs) + PROCESSOR (for government biometric data)

**Multi-Actor Note:** GDPR Art. 32 (security of processing) applies **directly to both controllers AND processors** ("the controller and the processor shall implement..."). For Art. 32 clauses, SecureBorder as processor has **NativeCompliance** obligations — not merely InheritedCompliance via DPA. Other GDPR clauses (Art. 5-7, 12-22) apply only in the controller capacity for audit logs.

**Nuance — DPO Mandatory (Art. 37(1)(c)):** SecureBorder processes biometric facial templates (Art. 9 special category data) on behalf of government authorities at large scale (millions of crossings annually). Art. 37(1)(c) requires **both the controller AND the processor** to designate a DPO when core activities consist of large-scale processing of Art. 9 data. SecureBorder as processor has a **direct statutory DPO obligation** — not merely a contractual one via the government DPA.

**Nuance — DPIA Always Required (Art. 35(3)(b)):** Large-scale processing of Art. 9 biometric data is an **automatic DPIA trigger** — no discretionary risk assessment is needed to determine whether a DPIA is required. The DPIA is mandatory by statute.

**Nuance — Processor Breach Notification (Art. 33(2)):** As processor, SecureBorder must notify the government authority (controller) of personal data breaches "without undue delay" — a distinct obligation from the controller's 72h notification to the supervisory authority. The processor→controller clock has no fixed numeric deadline.

---

### 3.2 CRA (Cyber Resilience Act)

| Criterion | Company Context Value | Threshold | Met? |
|-----------|----------------------|-----------|------|
| places_digital_products_eu | TRUE (eGate kiosks deployed across Schengen) | TRUE | YES |
| digital_element | TRUE (hardware + software with Edge AI) | YES | YES |
| manufacturer_status | TRUE (SecureBorder develops and operates) | YES | YES |
| product_class | **CRITICAL CLASS** (security function for border control) | Critical | YES |

**Applicability Result:** ✅ **APPLICABLE (Critical Class)**

**Rationale:** GuardianGate eGate systems are digital products with critical security functions for border control. As manufacturer, SecureBorder must comply with CRA Essential Requirements (Annex I). Critical Class classification requires third-party conformity assessment by a notified body (Art. 42).

**CRA Product Classes (context):** The CRA defines four conformity assessment regimes:
1. **Default products** → self-assessment (Module A, internal control)
2. **Important products Class I** (Annex III Class I) → self-assessment *only if* harmonised standards exist, else third-party (Module B+C or H)
3. **Important products Class II** (Annex III Class II, e.g., enterprise firewalls, IDS) → mandatory third-party assessment
4. **Critical products** (Annex IV, e.g., secure elements, smart card chips) → mandatory European cybersecurity certification (level "substantial")

SecureBorder's GuardianGate falls under **Critical Class** due to its border control security function — the most stringent regime.

**Caveat — No Certification Scheme Yet (Art. 8(1)):** The CRA requires Critical Class products to obtain European cybersecurity certification **only if** a certification scheme covering those product categories has been adopted under Regulation (EU) 2019/881. As of the regulation date (November 2024), no such scheme exists for critical products. Until the Commission adopts the relevant delegated acts and a scheme is available, Critical Class products default to **Art. 32(3)** conformity assessment procedures (full quality assurance + EU-type examination by a notified body). SecureBorder should plan for Art. 32(3) assessment now, with a potential transition to certification when the scheme becomes available.

**CRA Annex I: Two Parts with Different Natures:**
- **Part I** — Essential requirements *relating to the properties of products* (encryption, integrity mechanisms, access control, data minimization). These are "what the product must be" — **ProductProperty** obligations.
- **Part II** — Essential requirements *relating to the vulnerability handling processes* (SBOM, vulnerability management, timely security updates, CVD policy). These are "what the manufacturer must do throughout the product lifecycle" — **OrganisationalProcess** obligations.

**Key Clauses in Scope:** CRA-C01 through CRA-C26 (all 26 clauses applicable)

**Two Reporting Flows (both under Art. 14):**
The CRA has **two separate reporting obligations**, both within **Art. 14** (not Art. 15 — see caveat below):

| Flow | Article | Trigger | Early Warning | Notification | Final Report |
|------|---------|---------|---------------|--------------|--------------|
| **Actively Exploited Vulnerabilities** | Art. 14(1-2) | Manufacturer becomes aware of active exploitation | 24h to CSIRT/ENISA | 72h to CSIRT/ENISA | **14 days after corrective measure is available** |
| **Severe Incidents affecting product security** | Art. 14(3-5) | Severe incident impacting product security | 24h to CSIRT/ENISA | 72h to CSIRT/ENISA | **1 month after incident notification** |

**Caveat — Art. 15 is Voluntary:** Art. 15 of the CRA is titled "Voluntary reporting" and allows manufacturers to voluntarily report vulnerabilities, incidents, and near misses. The **mandatory** severe incident reporting is under **Art. 14(3)**, not Art. 15. This is a common misattribution.

These are distinct obligations with different final report deadlines (14 days vs. 1 month). The clause mapping should distinguish between Art. 14(1-2) (vulnerability reporting) and Art. 14(3-5) (incident reporting) clauses.

**Quantitative Thresholds:**
- **Support Period (Art. 13(8)):** Minimum **5 years** from product placement (or expected use time if less). For GuardianGate hardware+software, this means security patches and vulnerability fixes for at least 5 years per deployed unit.
- **Security Update Retention (Art. 13(9)):** Security updates must remain available for **10 years** or the support period, whichever is longer. Critical infrastructure like eGate kiosks may have 15-20 year deployment lifespans.
- **Technical Documentation Retention (Art. 13(13)):** Technical documentation must be kept for **10 years** after the product has been placed on the market.

**Exclusions Analysis (Art. 24):** The CRA does not apply to products covered by sectoral regulations (medical devices, motor vehicles, marine equipment, aviation), products for national security/defence, or spare parts. GuardianGate eGate kiosks are border control systems — they do not fall under any excluded sectoral regulation. While border control has security implications, the product itself is a commercial civilian system deployed at border crossings, not a military/defence product. Therefore, **no CRA exclusions apply**.

**Obligated Party:** MANUFACTURER (Critical Class requires notified body assessment)

---

### 3.3 NIS 2 (Network and Information Systems Directive 2)

| Criterion | Company Context Value | Threshold | Met? |
|-----------|----------------------|-----------|------|
| nis2_sector | Defense/Security/Critical Infrastructure | Annex I/II | YES |
| size (employees) | 450 | ≥50 (medium) | YES |
| size (revenue) | €120M | ≥€10M | YES |
| essential_entity_supplier | TRUE (supplies border control systems) | TRUE | YES |

**Applicability Result:** ✅ **APPLICABLE (Essential Entity Supplier)**

**Rationale:** SecureBorder qualifies as a medium-sized enterprise (450 employees, €120M revenue) operating in the defense/security sector. As a supplier of critical systems to government border control (essential entities), NIS 2 supply chain security obligations apply (Art. 21(2)(d)). Management liability applies for non-compliance.

**Key Clauses in Scope:** NIS2-C01 through NIS2-C29 (all 29 clauses applicable)

**Obligated Party:** ESSENTIAL_ENTITY_SUPPLIER (24h incident notification required)

**Nuance — Delegated Granularity (Implementing Regulation 2024/2690):**
The NIS 2 Art. 21(5) delegates technical detail to Commission implementing acts. The **Commission Implementing Regulation (EU) 2024/2690** of 17 October 2024 specifies granular technical and methodological requirements for the 10 elements of Art. 21(2) for specific sectors (DNS providers, cloud providers, data centres, CDNs, managed service providers, MSSPs, online marketplaces, search engines, social networking platforms, trust service providers). For entities in these sectors, the IR 2024/2690 adds concrete technical specificity beyond the NIS 2 directive text — analogous to how DORA's RTS specifies deadlines.

**Nuance — Trust Service Provider Derogation (Art. 23(4)):**
For trust service providers, the incident notification deadline (normally 72h under Art. 23(4)(b)) is **reduced to 24h** ("without undue delay and in any event within 24 hours"). This is a sector-specific derogation worth noting if SecureBorder's supply chain includes trust service providers.

**Nuance — Ongoing Incident Provision (Art. 23(4)(e)):**
If an incident is still ongoing at the time of the final report (1 month), the entity must provide a progress report at that time and a final report within one month of their handling of the incident. The 1-month deadline is not absolute — it can be extended by the incident handling duration.

**Directive vs. Regulation Note:** NIS 2 is a **Directive**, not a Regulation. It is transposed into national law by each Member State with discretion in key areas (sanctions, enforcement, exact thresholds). As of May 2025, the Commission opened infringement procedures against 19 Member States for late transposition. This creates jurisdiction-specific variation not captured by treating NIS 2 as a uniform EU instrument.

---

### 3.4 DORA (Digital Operational Resilience Act)

| Criterion | Company Context Value | Threshold | Met? |
|-----------|----------------------|-----------|------|
| dora_financial_entity | FALSE | TRUE | NO |
| financial_sector_classification | N/A | Credit institution, Investment firm, etc. | NO |
| ict_third_party_provider | FALSE (not primarily ICT for finance) | YES/NO | NO |

**Applicability Result:** ❌ **NOT APPLICABLE**

**Rationale:** SecureBorder is not a financial entity per DORA Art. 2 (not a bank, insurance company, payment institution, investment firm, etc.). Products are for border control, not financial services.

**Key Clauses in Scope:** N/A

---

### 3.5 AI_Act (Artificial Intelligence Regulation)

| Criterion | Company Context Value | Threshold | Met? |
|-----------|----------------------|-----------|------|
| aiact_high_risk_system | TRUE (Edge AI for border control) | Annex III | YES |
| ai_system_provider | TRUE (SecureBorder develops AI) | YES | YES |
| high_risk_use_case | TRUE (migration, asylum, border control - Annex III) | Annex III listing | YES |
| biometric_categorization | TRUE (facial recognition for identity) | Annex III §1 | YES |

**Applicability Result:** ✅ **APPLICABLE (High-Risk AI System)**

**Rationale:** GuardianGate uses Edge AI for automated border control (face matching, liveness detection). This falls explicitly under AI_Act Annex III (migration, asylum and border control management) as a high-risk AI system. Conformity assessment required before EU market placement (Art. 43). Post-market monitoring system mandatory (Art. 72).

**Key Clauses in Scope:** AI-C01 through AI-C29 (all 29 clauses applicable)

**Obligated Party:** PROVIDER (High-Risk AI System per Annex III)

**Prohibited Practices Analysis (Art. 5):** GuardianGate uses facial recognition for identity verification (one-to-one matching against passport data), not identification (one-to-many search). The system does not engage in: (a) subliminal/manipulative techniques; (b) exploitation of vulnerabilities; (c) social scoring; (d) predictive policing; (e) untargeted scraping of facial images; (f) emotion inference in workplace/education; (g) biometric categorization inferring race/political/religious beliefs; or (h) real-time remote biometric identification in publicly accessible spaces for law enforcement purposes. The system performs **verification** at a controlled kiosk with explicit legal basis — this falls under the high-risk classification (Annex III: border control), **not** the prohibited practices category.

**Three Tiers of Serious Incident Reporting (Art. 73):** The AI_Act has three different deadlines for serious incident reporting:

| Scenario | Deadline | Base Legal |
|----------|----------|------------|
| Default (serious incident) | No later than **15 days** after becoming aware | Art. 73(2) |
| Widespread infringement OR serious incident Art. 3(49)(b) | Immediately, no later than **2 days** | Art. 73(3) |
| Death of a person | No later than **10 days** after establishing causal link | Art. 73(4) |

**Downstream Provider Obligations (Art. 25):** If a government authority or third party substantially modifies GuardianGate's AI system (e.g., repurposing it for a different border control function, or adding new biometric modalities), that entity may become the "provider" with full Art. 16 obligations. SecureBorder should include written agreements (Art. 25(4)) specifying information, capabilities, and technical access needed for compliance with any downstream entities.

---

## 4. APPLICABILITY MATRIX SUMMARY

| Regulation | Applicable? | Confidence | Key Driver | Exclusion Reason (if applicable) |
|------------|-------------|------------|------------|----------------------------------|
| **GDPR** | YES | HIGH | Special category data (biometrics - Art. 9) | — |
| **CRA** | YES | HIGH | Critical Class product (border security) | — |
| **NIS 2** | YES | HIGH | 450 employees + security sector | — |
| **DORA** | NO | HIGH | Not a financial entity | Not financial sector |
| **AI_Act** | YES | HIGH | Annex III (border control AI) | — |

**Total Applicable Regulations:** 4/5

**Total Applicable Clauses:** 112 (GDPR 28 + CRA 26 + NIS 2 29 + AI_Act 29)

---

## 5. NATIVE VS. INHERITED COMPLIANCE

### 5.1 Native Compliance Requirements

Compliance obligations that SecureBorder must implement directly:

| Regulation | Domain | Obligation | Implementation Responsibility |
|------------|--------|------------|-------------------------------|
| GDPR | D-05, D-09, D-10 | Data protection, DPIA, Records | Internal (DPO + CISO) |
| CRA | D-02, D-06, D-07 | Vuln management, SBOM, Secure dev | Internal (CTO + Security team) |
| NIS 2 | D-04, D-07, D-08 | Incident response (24h), Training | Internal (SOC + HR) |
| AI_Act | D-07, D-09, D-10 | Conformity assessment, Post-market monitoring | Internal (AI Governance Lead) |

### 5.2 Inherited Compliance Requirements

Compliance obligations inherited from suppliers/partners:

| Regulation | Domain | Obligation | Source (Supplier/Partner) | Evidence Required |
|------------|--------|------------|---------------------------|-------------------|
| GDPR | D-01 | Infrastructure encryption | Cloud Provider (EU) | SOC 2 Type II, ISO 27001 |
| CRA | D-01 | Hardware security | Hardware Suppliers | Component certifications |
| NIS 2 | D-06 | Supply chain security | All suppliers | Supplier security questionnaires |
| AI_Act | D-01 | Cloud infrastructure security | Cloud Provider | AI infrastructure compliance |

<!-- BY-DESIGN: case-specific extension -->

### 5.3 Compliance Boundary Diagram

```
┌─────────────────────────────────────────────────────────────┐
│              SECUREBORDER BOUNDARY                           │
│                                                              │
│   ┌─────────────────┐         ┌─────────────────┐           │
│   │  NATIVE         │         │  INHERITED      │           │
│   │  Compliance     │         │  Compliance     │           │
│   │  (Direct)       │         │  (Via contracts)│           │
│   │                 │         │                 │           │
│   │ • AI conformity │         │ • Cloud: Phys   │           │
│   │ • CRA cert      │         │ • HW: Components│           │
│   │ • NIS 2 (24h)   │         │ • Supplier SBOM │           │
│   │ • GDPR DPIA     │         │                 │           │
│   └─────────────────┘         └─────────────────┘           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
         ▲                               ▲
         │                               │
    Direct implementation          Supplier/Partner
    (4 regulations)                compliance evidence
```

---

## 6. SUB-DOMAIN COVERAGE PRELIMINARY ASSESSMENT

Based on applicable regulations (GDPR + CRA + NIS 2 + AI_Act):

| Sub-Domain ID | Sub-Domain Name | GDPR | CRA | NIS 2 | AI_Act | Total | Coverage Level |
|---------------|-----------------|------|-----|-------|--------|-------|----------------|
| D-01.1 | Data at Rest Encryption | ✅ | ✅ | ✅ | ✅ | 4 | SUBSTANTIVE |
| D-01.2 | Data in Transit Encryption | ✅ | ✅ | ✅ | ✅ | 4 | SUBSTANTIVE |
| D-01.3 | Cryptographic Key Management | — | ✅ | ✅ | ✅ | 3 | SUBSTANTIVE |
| D-01.4 | Data Integrity Mechanisms | ✅ | ✅ | — | ✅ | 3 | SUBSTANTIVE |
| D-02.1 | Vulnerability Identification | — | ✅ | ✅ | ✅ | 3 | SUBSTANTIVE |
| D-02.2 | Patch Management & Updates | — | ✅ | ✅ | — | 2 | PARTIAL |
| D-02.3 | Coordinated Vuln. Disclosure | — | ✅ | ✅ | — | 2 | PARTIAL |
| D-02.4 | Threat-Led Penetration Testing | — | — | ✅ | ✅ | 2 | PARTIAL |
| D-03.1 | Identity Lifecycle Management | — | ✅ | ✅ | ✅ | 3 | SUBSTANTIVE |
| D-03.2 | Multi-Factor Authentication | — | ✅ | ✅ | ✅ | 3 | SUBSTANTIVE |
| D-03.3 | Authorization & Least Privilege | ✅ | — | ✅ | — | 2 | PARTIAL |
| D-03.4 | Secure System Defaults | — | ✅ | — | — | 1 | PARTIAL |
| D-04.1 | Incident Detection & Triage | — | ✅ | ✅ | ✅ | 3 | SUBSTANTIVE |
| D-04.2 | Containment & Mitigation | ✅ | ✅ | ✅ | — | 3 | SUBSTANTIVE |
| D-04.3 | Regulatory Notification | ✅ | ✅ | ✅ | ✅ | 4 | SUBSTANTIVE |
| D-04.4 | Data Restoration & Recovery | ✅ | — | ✅ | — | 2 | PARTIAL |
| D-05.1 | Data Minimization | ✅ | ✅ | — | ✅ | 3 | SUBSTANTIVE |
| D-05.2 | Retention & Archiving | ✅ | — | — | ✅ | 2 | PARTIAL |
| D-05.3 | Right to Erasure | ✅ | ✅ | — | — | 2 | PARTIAL |
| D-05.4 | Data Portability | ✅ | — | — | — | 1 | PARTIAL |
| D-06.1 | Vendor Risk Assessment | ✅ | — | ✅ | — | 2 | PARTIAL |
| D-06.2 | SBOM | — | ✅ | — | — | 1 | PARTIAL |
| D-06.3 | Contractual Security Obligations | ✅ | — | ✅ | — | 2 | PARTIAL |
| D-06.4 | Third-Party Boundary Management | — | — | ✅ | — | 1 | PARTIAL |
| D-07.1 | Secure-by-Design Principles | ✅ | ✅ | ✅ | — | 3 | SUBSTANTIVE |
| D-07.2 | Secure Coding Practices | — | ✅ | ✅ | — | 2 | PARTIAL |
| D-07.3 | CI/CD Pipeline Security | — | — | ✅ | — | 1 | PARTIAL |
| D-07.4 | Change Management | — | — | ✅ | — | 1 | PARTIAL |
| D-08.1 | General Security Awareness | ✅ | — | ✅ | — | 2 | PARTIAL |
| D-08.2 | Role-Specific Competence | ✅ | — | ✅ | ✅ | 3 | SUBSTANTIVE |
| D-08.3 | Management Board Training | — | — | ✅ | — | 1 | PARTIAL |
| D-09.1 | Information Security Policies | ✅ | ✅ | ✅ | ✅ | 4 | SUBSTANTIVE |
| D-09.2 | Impact & Risk Assessments | ✅ | ✅ | ✅ | ✅ | 4 | SUBSTANTIVE |
| D-09.3 | Asset Inventories | — | — | ✅ | — | 1 | PARTIAL |
| D-09.4 | Records of Processing | ✅ | — | — | ✅ | 2 | PARTIAL |
| D-10.1 | Continuous Security Monitoring | — | ✅ | ✅ | ✅ | 3 | SUBSTANTIVE |
| D-10.2 | Audit Logging & Traceability | — | ✅ | ✅ | ✅ | 3 | SUBSTANTIVE |
| D-10.3 | Compliance Testing | ✅ | ✅ | ✅ | ✅ | 4 | SUBSTANTIVE |

**Coverage Summary:**
- **Substantive Coverage (≥3 regulations):** 16 sub-domains
- **Partial Coverage (1-2 regulations):** 19 sub-domains
- **No Coverage (0 regulations):** 3 sub-domains (D-07.4, D-08.3, D-09.3 — canonical NOT_ADDRESSED set per Doc09/Doc12 O-02 resolution). ⚠️ *The §4 coverage statistics above predate that resolution: D-07.2 carries GDPR + NIS 2 PARTIAL rows in this matrix and is ACTIVE; D-08.3's NIS 2 Art. 20 line is satisfied via board briefing (Doc 04 §10.3 / Doc 12 §4 exclusion note), not as a training sub-domain.*

**Total Covered:** 35/38 sub-domains (92.1%)

---

## 7. STRATEGIC IMPLICATIONS

| Implication ID | Source Regulation | Description | Impact on Architecture | Priority |
|----------------|-------------------|-------------|------------------------|----------|
| SI-001 | GDPR + AI_Act | Dual DPIA + FRIA required | Unified assessment process | CRITICAL |
| SI-002 | CRA + NIS 2 | Overlapping incident response (24h vs 72h) | Max-SLA workflow (24h) | CRITICAL |
| SI-003 | AI_Act | Post-market monitoring system | New system required | HIGH |
| SI-004 | CRA Critical Class | Third-party conformity assessment | Notified body engagement | CRITICAL |
| SI-005 | GDPR Art. 9 | Explicit legal basis for biometrics | Government contract basis | CRITICAL |
| SI-006 | NIS 2 | Management liability | Board briefing required | HIGH |

---

## 8. REGULATORY GAPS IDENTIFIED

| Gap ID | Regulation | Clause | Sub-Domain | Gap Description | Risk Level |
|--------|------------|--------|------------|-----------------|------------|
| GAP-001 | DORA | C19 | D-07.2 | No mandate for secure coding (DORA exclusive) | MEDIUM |
| GAP-002 | DORA | C06 | D-07.4 | No mandate for change management (DORA exclusive) | MEDIUM |
| GAP-003 | DORA | C05 | D-09.3 | No mandate for asset inventories (DORA exclusive) | MEDIUM |

**Mitigation:** Level 2 frameworks (ISO 27001 A.14, NIST SSDF) recommended for D-07 Secure Development domain. ISO 27001 already certified — gap is minimal.

---

<!-- BY-DESIGN: case-specific extension -->

## 8.5 Per-Article Detailed Breakdown

> Sprint 5 DEEP enrichment. 112 rows: 28 GDPR + 26 CRA + 29 NIS 2 + 29 AI_Act. Each row maps a regulatory clause to its sub-domain, obligated party, verification criteria, evidence type, risk if not met, and maturity (current → target). This complements the §3 Regulation-by-Regulation Applicability Analysis and the §4 Applicability Matrix Summary by providing per-article operational depth.

### A. GDPR (28 articles)

| GDPR — Total rows: 28 |

| Article | Topic | Sub-Domains | Obligated Party | Verification Criteria | Evidence Type | Risk if not met | Maturity (cur→tgt) |
|---------|-------|-------------|-----------------|------------------------|---------------|-----------------|--------------------|
| Art. 5 (C01) | Principles relating to processing | D-05.1, D-05.2, D-09.1 | CONTROLLER | Doc 04 §10.4 + DPIA on change | POLICY + AUDIT | HIGH — Art. 5(1)(a) lawfulness breach triggers Art. 83(4) fine | 3/4 → 4/4 |
| Art. 6 (C02) | Lawfulness of processing | D-05.1, D-09.4 | CONTROLLER | Legal basis documented per processing activity | POLICY | HIGH — No legal basis = unlawful processing, Art. 83(4) fine | 3/4 → 4/4 |
| Art. 7 (C03) | Conditions for consent | D-05.1 | CONTROLLER | Consent record per processing activity | POLICY | LOW — Art. 9(2)(g) is the SecureBorder legal basis, not consent | 3/4 → 4/4 |
| Art. 8 (C04) | Child's consent in information society services | — | N/A | N/A — no children data subjects | N/A | LOW — Not applicable; travelers are adults | — |
| Art. 9 (C05) | Processing of special categories of data | D-01.x, D-03.x, D-05.1, D-05.3 | CONTROLLER + PROCESSOR | DPIA + Art. 9(2)(g) explicit legal basis | DPIA + AUDIT | HIGH — Art. 9 biometric breach = Art. 83(5) fine (up to €20M / 4%) | 3/4 → 4/4 |
| Art. 10 (C06) | Processing of data on criminal convictions | D-05.1 | CONTROLLER | Limited scope; watchlist data is government-owned | POLICY | MEDIUM — Criminal-record data only via government controller | 3/4 → 4/4 |
| Art. 11 (C07) | Processing not requiring identification | D-05.1 | CONTROLLER | Anonymisation policy for non-identification scope | POLICY | LOW — Anonymisation handled by cryptographic sharding | 3/4 → 4/4 |
| Art. 12 (C08) | Transparent information, communication, modalities | D-05.4, D-09.1 | CONTROLLER | Privacy notice + DPO contact information | POLICY | MEDIUM — Art. 12(3) one-month response deadline | 3/4 → 4/4 |
| Art. 13 (C09) | Information to be provided when data is collected | D-09.1 | CONTROLLER | Privacy notice at data collection point | POLICY | MEDIUM | 3/4 → 4/4 |
| Art. 14 (C10) | Information when data is not collected from the data subject | D-09.1 | CONTROLLER | Indirect-source notice (watchlist data from government) | POLICY | MEDIUM | 3/4 → 4/4 |
| Art. 15 (C11) | Right of access by the data subject | D-05.4 | CONTROLLER | JSON export endpoint covers access request | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 16 (C12) | Right to rectification | D-05.3 | CONTROLLER | Rectification endpoint + privileged access review | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 17 (C13) | Right to erasure ('right to be forgotten') | D-05.3 | CONTROLLER + PROCESSOR | Erasure endpoint + cryptographic sharding (T-002) | TEST + DEMONSTRATE | HIGH — Art. 17 failure on biometric = Art. 83(5) fine | 2/4 → 4/4 |
| Art. 18 (C14) | Right to restriction of processing | D-05.3 | CONTROLLER | Restriction endpoint + audit log | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 19 (C15) | Notification obligation regarding rectification/erasure/restriction | D-05.3 | CONTROLLER | Notification to recipients on erasure | POLICY | MEDIUM | 3/4 → 4/4 |
| Art. 20 (C16) | Right to data portability | D-05.4 | CONTROLLER | JSON export endpoint per Art. 20 | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 21 (C17) | Right to object + automated decision-making | D-05.1 | CONTROLLER | Objection endpoint + manual review process | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 22 (C18) | Automated decision-making, including profiling | D-09.2 | CONTROLLER | Human oversight per AI_Act Art. 14 + GDPR Art. 22 | TEST + DEMONSTRATE | HIGH — eGate AI may be subject to Art. 22 constraints | 3/4 → 4/4 |
| Art. 23 (C19) | Restrictions on scope of obligations | D-09.1 | CONTROLLER + MEMBER STATE | Restriction scope documented in DPIA | POLICY | LOW | 3/4 → 4/4 |
| Art. 24 (C20) | Responsibility of the controller | D-09.1 | CONTROLLER | ISO 27001 ISMS demonstrates accountability | POLICY + AUDIT | MEDIUM | 4/4 → 4/4 |
| Art. 25 (C21) | Data protection by design and by default | D-03.4, D-07.1 | CONTROLLER | Privacy by design in SDLC + secure defaults | TEST + DEMONSTRATE | HIGH — Art. 25 breach compounds other Art. failures | 3/4 → 4/4 |
| Art. 26 (C22) | Joint controllers | D-09.1 | CONTROLLER | Joint-controller arrangement with government (out of scope) | POLICY | MEDIUM | 3/4 → 4/4 |
| Art. 28 (C23) | Processor | D-06.1, D-06.3 | PROCESSOR | DPA template + 8-element list + sub-processor flowdown | TEST + ANALYZE + external audit | HIGH — Art. 28(3) DPA breach = Art. 83(4) fine | 3/4 → 4/4 |
| Art. 30 (C24) | Records of processing activities | D-09.4 | CONTROLLER + PROCESSOR | RoPA covering all 4 regs with DPO oversight | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 33 (C25) | Breach notification to supervisory authority | D-04.3 | CONTROLLER | Multi-reg max-SLA 24h routing (T-001) | TEST + ANALYZE + external audit | CRITICAL — 4 fines on single incident | 2/4 → 4/4 |
| Art. 34 (C26) | Communication of breach to data subject | D-04.3 | CONTROLLER | Communication template per Art. 34(3) | POLICY + AUDIT | HIGH | 3/4 → 4/4 |
| Art. 32 (C27) | Security of processing | D-01.x, D-02.x, D-03.x, D-04.x, D-08.x, D-09.x, D-10.x | CONTROLLER + PROCESSOR | Art. 32(1) 4-element list (closed AND) | TEST + ANALYZE + external audit (RIGOROUS) | HIGH — Art. 32 breach + Art. 9 = Art. 83(5) fine | 3/4 → 4/4 |
| Art. 35 (C28) | Data protection impact assessment | D-09.2 | CONTROLLER | Unified DPIA + FRIA single process (T-003) | TEST + DEMONSTRATE | HIGH — Art. 35(3)(b) automatic DPIA trigger failure | 3/4 → 4/4 |


### B. CRA (26 articles)

| CRA — Total rows: 26 |

| Article | Topic | Sub-Domains | Obligated Party | Verification Criteria | Evidence Type | Risk if not met | Maturity (cur→tgt) |
|---------|-------|-------------|-----------------|------------------------|---------------|-----------------|--------------------|
| Art. 1 (C01) | Subject matter and objectives | D-09.1 | MANUFACTURER | CRA conformed products only | POLICY | HIGH | 3/4 → 4/4 |
| Art. 6(a) (C02) | Essential requirements — proper installation | D-03.4, D-07.1 | MANUFACTURER | Per Annex II §8 (R1 literal reading) | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 6(b) (C03) | Essential requirements — secure-by-default | D-03.4, D-07.1 | MANUFACTURER | CRA Art. 13(2) secure-by-default | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 7 (C04) | Critical products (Annex IV) | D-09.1 | MANUFACTURER | Critical Class conformity assessment | TEST + ANALYZE + external audit | CRITICAL — Market access blocked if no certification | 2/4 → 4/4 |
| Art. 13(1) (C05) | Risk assessment | D-09.2 | MANUFACTURER | Risk assessment per Art. 13(1) | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 13(2) (C06) | Secure-by-default | D-03.4, D-07.1 | MANUFACTURER | CRA Art. 13(2) secure-by-default | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 13(3) (C07) | Intended purpose + reasonably foreseeable use | D-05.1, D-07.1 | MANUFACTURER | Intended purpose documented | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 13(8) (C08) | Support period (5y) | D-02.2 | MANUFACTURER | 5-year support period | TEST + DEMONSTRATE | HIGH — Support period failure | 3/4 → 4/4 |
| Art. 13(9) (C09) | Update availability (10y) | D-02.2 | MANUFACTURER | 10-year update availability | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 13(11) (C10) | SBOM | D-06.2 | MANUFACTURER | CycloneDX SBOM per release | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 13(12) (C11) | Technical documentation | D-09.4 | MANUFACTURER | Annex VII technical documentation | TEST + ANALYZE + external audit | HIGH | 3/4 → 4/4 |
| Art. 13(13) (C12) | Technical documentation retention (10y) | D-05.2, D-09.4 | MANUFACTURER | 10-year retention | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 13(14) (C13) | Logging | D-10.2 | MANUFACTURER | Tamper-evident logging | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 14(1) (C14) | AEV early warning (24h) | D-04.3 | MANUFACTURER | Multi-reg max-SLA 24h routing (T-001) | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 14(2) (C15) | AEV notification + final report (14d) | D-04.3 | MANUFACTURER | AEV notification pipeline | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 14(3) (C16) | Severe incident early warning (24h) | D-04.1, D-04.3 | MANUFACTURER | Severe incident detection + notification | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 14(4) (C17) | Severe incident notification (72h) | D-04.3 | MANUFACTURER | Notification pipeline | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 14(5) (C18) | Severe incident final report (1 month) | D-04.3, D-04.4 | MANUFACTURER | Final report pipeline | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 14(8) (C19) | User notification | D-04.3 | MANUFACTURER | User notification template | POLICY | HIGH | 3/4 → 4/4 |
| Art. 16 (C20) | Dissemination with delay grounds | D-02.3 | MANUFACTURER | security.txt + CVD page | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 21 (C21) | Manufacturer-equivalent trigger | D-04.2 | MANUFACTURER | Containment playbook | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 24 (C22) | Exclusions | — | MANUFACTURER | Exclusions analysis (no exclusions apply) | POLICY | LOW | 3/4 → 4/4 |
| Art. 27 (C23) | Harmonised standards | D-09.1 | MANUFACTURER | CRA Art. 27 harmonised standards presumption | POLICY | MEDIUM | 3/4 → 4/4 |
| Art. 32(3) (C24) | Critical Class conformity assessment | D-09.1 | MANUFACTURER + NOTIFIED BODY | Notified Body engagement (Art. 32(3) until certification scheme) | TEST + ANALYZE + external audit | CRITICAL — Market access blocked | 2/4 → 4/4 |
| Art. 43 (C25) | Conformity assessment procedures | D-10.3 | MANUFACTURER | Annex VII + Annex VIII conformity assessment | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 56 (C26) | Penalties | D-09.1 | MEMBER STATE | Fine schedule per Art. 56 | POLICY | CRITICAL — Up to €15M / 2.5% turnover | — |


### C. NIS 2 (29 articles)

| NIS 2 — Total rows: 29 |

| Article | Topic | Sub-Domains | Obligated Party | Verification Criteria | Evidence Type | Risk if not met | Maturity (cur→tgt) |
|---------|-------|-------------|-----------------|------------------------|---------------|-----------------|--------------------|
| Art. 21(1) (C01) | Risk-management measures (10 factors) | D-09.2 | ESSENTIAL ENTITY SUPPLIER | Risk assessment per Art. 21(1) sentence 2 | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 21(2)(a) (C02) | Risk assessment policies | D-09.4 | ESSENTIAL ENTITY SUPPLIER | Risk assessment policy documented | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 21(2)(b) (C03) | Incident handling | D-04.x | ESSENTIAL ENTITY SUPPLIER | Incident handling playbook | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 21(2)(c) (C04) | Business continuity + DR | D-04.4 | ESSENTIAL ENTITY SUPPLIER | RTO 24h, RPO 1h, 10y retention | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 21(2)(d) (C05) | Supply chain security | D-06.1, D-06.3, D-06.4, D-07.x | ESSENTIAL ENTITY SUPPLIER | NIS 2 Art. 21(3) three-prong supplier assessment | TEST + ANALYZE + external audit | HIGH | 3/4 → 4/4 |
| Art. 21(2)(e) (C06) | Network security + testing | D-02.1, D-02.4, D-06.4, D-08.1 | ESSENTIAL ENTITY SUPPLIER | Network security + threat-led testing | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 21(2)(f) (C07) | Effectiveness evaluation | D-10.3 | ESSENTIAL ENTITY SUPPLIER | Annual control test | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 21(2)(g) (C08) | Cyber hygiene + training | D-08.1, D-08.2, D-10.1 | ESSENTIAL ENTITY SUPPLIER | Annual awareness + quarterly phishing + role-specific training | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 21(2)(h) (C09) | Cryptography + encryption | D-01.1, D-01.2, D-01.3, D-10.2 | ESSENTIAL ENTITY SUPPLIER | Cryptography policy + AES-256 + HSM-backed KMS | TEST + ANALYZE + external audit | HIGH | 3/4 → 4/4 |
| Art. 21(2)(i) (C10) | Access control + HR security | D-03.1, D-03.3 | ESSENTIAL ENTITY SUPPLIER | Joinder-mover-leaver + RBAC + ABAC + SoD | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 21(2)(j) (C11) | MFA + secure communications | D-03.2, D-06.4 | ESSENTIAL ENTITY SUPPLIER | Hardware MFA + mTLS on boundaries | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 23(1) (C12) | Incident handling (process) | D-04.1 | ESSENTIAL ENTITY SUPPLIER | CSIRT notification process | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 23(3) (C13) | Early warning (24h) | D-04.3 | ESSENTIAL ENTITY SUPPLIER | Multi-reg max-SLA 24h routing (T-001) | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 23(4)(a) (C14) | Incident notification (72h) | D-04.3 | ESSENTIAL ENTITY SUPPLIER | Notification pipeline | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 23(4)(b) (C15) | Trust service provider derogation (24h) | D-04.3 | ESSENTIAL ENTITY SUPPLIER | If trust service provider in chain: 24h notification | TEST + ANALYZE + external audit | HIGH | 2/4 → 4/4 |
| Art. 23(4)(e) (C16) | Ongoing incident provision | D-04.3, D-04.4 | ESSENTIAL ENTITY SUPPLIER | Progress report + final report on incident handling | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 21(2)(h) (C17) | Cryptography policy | D-01.x, D-10.2 | ESSENTIAL ENTITY SUPPLIER | Cryptography policy documented | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 24 (C18) | Voluntary reporting | D-02.3 | ESSENTIAL ENTITY SUPPLIER | Voluntary CVD report channel | POLICY | LOW | 3/4 → 4/4 |
| Art. 20 (C19) | Management liability | D-08.3 (board briefing) | MANAGEMENT | CEO/board acknowledgement | POLICY | CRITICAL — CEO/board personally liable | — |
| Art. 21(3) (C20) | Supplier assessment (three-prong) | D-06.1, D-06.3 | ESSENTIAL ENTITY SUPPLIER | Direct supplier assessment per Art. 21(3) | TEST + ANALYZE + external audit | HIGH | 3/4 → 4/4 |
| Art. 21(4) (C21) | Proportionality | D-09.2 | ESSENTIAL ENTITY SUPPLIER | Risk-based proportionality | TEST + DEMONSTRATE | LOW | 3/4 → 4/4 |
| Art. 21(5) (C22) | Delegated granularity (IR 2024/2690) | D-09.1 | ESSENTIAL ENTITY SUPPLIER | Not directly applicable to SecureBorder (not in IR 2024/2690 sector list) | POLICY | LOW | — |
| Art. 23(1) §1 (C23) | CSIRT notification — `incident` definition | D-04.3 | ESSENTIAL ENTITY SUPPLIER | Confirmed and materialised incident (not detection) | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 23(1) §6 (C24) | Significant impact assessment | D-04.3 | ESSENTIAL ENTITY SUPPLIER | Significant impact criteria per Art. 23(1) §6 | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 23(1) (C25) | Reporting cascade | D-04.3 | ESSENTIAL ENTITY SUPPLIER | CSIRT or CA notification | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 23(1) ¶1 (C26) | CSIRT notification | D-04.3 | ESSENTIAL ENTITY SUPPLIER | Confirmed and materialised incident starts 24h clock | TEST + DEMONSTRATE | CRITICAL | 3/4 → 4/4 |
| Art. 23(3)(a) (C27) | Early warning recipients | D-04.3 | ESSENTIAL ENTITY SUPPLIER | CSIRT or CA notification | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 23(3) (C28) | Early warning content | D-04.3 | ESSENTIAL ENTITY SUPPLIER | Indication of incident + suspected cause + affected systems | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 23(4) (C29) | Notification + final report | D-04.3 | ESSENTIAL ENTITY SUPPLIER | 72h notification + 1 month final report | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |


### D. AI_Act (29 articles)

| AI_Act — Total rows: 29 |

| Article | Topic | Sub-Domains | Obligated Party | Verification Criteria | Evidence Type | Risk if not met | Maturity (cur→tgt) |
|---------|-------|-------------|-----------------|------------------------|---------------|-----------------|--------------------|
| Art. 4 (C01) | AI literacy | D-08.2 | PROVIDER | AI literacy training for relevant roles | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 5 (C02) | Prohibited practices | — | PROVIDER | Negative analysis (no prohibited practices) | POLICY | LOW | 3/4 → 4/4 |
| Art. 9 (C03) | Risk management system | D-09.1, D-09.2, D-07.1 | PROVIDER | Risk management system across 6 lifecycle phases | TEST + ANALYZE + external audit | HIGH | 2/4 → 4/4 |
| Art. 10 (C04) | Data governance | D-05.1, D-01.4 | PROVIDER | Data-quality checks + AI training data integrity | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 11 (C05) | Technical documentation | D-09.4 | PROVIDER | Annex IV technical documentation | TEST + ANALYZE + external audit | HIGH | 3/4 → 4/4 |
| Art. 12 (C06) | Logging capability | D-09.4, D-10.2 | PROVIDER | Tamper-evident logging + 10y retention | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 13 (C07) | Transparency to deployers | D-09.1 | PROVIDER | Transparency documentation for deployers | TEST + DEMONSTRATE | MEDIUM | 3/4 → 4/4 |
| Art. 14 (C08) | Human oversight | D-08.2, D-09.1 | PROVIDER | Human oversight procedures per AI_Act Art. 14 | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 15 (C09) | Accuracy + robustness + cybersecurity | D-01.4, D-07.2 | PROVIDER | Accuracy + robustness + cybersecurity baseline | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 19(1) (C10) | Automatic logging retention (≥6 months) | D-05.2, D-10.2 | PROVIDER | 10-year retention (above-floor) | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 25 (C11) | Downstream provider | D-09.1 | PROVIDER | Written agreements with downstream entities | POLICY | MEDIUM | 3/4 → 4/4 |
| Art. 27 (C12) | FRIA — fundamental rights impact assessment | D-09.2 | PROVIDER | Unified DPIA + FRIA (T-003) | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 43 (C13) | Conformity assessment | D-10.3 | PROVIDER | Third-party assessment (Annex III) | TEST + ANALYZE + external audit | CRITICAL — Market access blocked | 2/4 → 4/4 |
| Art. 49 (C14) | Registration | D-09.4 | PROVIDER | EU database registration | POLICY | MEDIUM | 3/4 → 4/4 |
| Art. 72 (C15) | Post-market monitoring | D-10.1 | PROVIDER | Post-market monitoring system | TEST + ANALYZE + external audit | HIGH | 2/4 → 4/4 |
| Art. 73(1) (C16) | Serious incident reporting — general | D-04.3 | PROVIDER | Multi-reg max-SLA 24h routing (T-001) | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 73(2) (C17) | Serious incident — default 15d | D-04.3 | PROVIDER | 15-day clock for serious incident (default) | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 73(3) (C18) | Widespread infringement — 2d | D-04.3 | PROVIDER | 2-day clock for widespread infringement | TEST + ANALYZE + external audit | CRITICAL | 2/4 → 4/4 |
| Art. 73(4) (C19) | Death of person — 10d | D-04.3 | PROVIDER | 10-day clock after causal link established | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 75 (C20) | Reporting to market surveillance authorities | D-04.3 | PROVIDER | MSA notification | TEST + DEMONSTRATE | HIGH | 3/4 → 4/4 |
| Art. 76 (C21) | Investigation of AI systems | D-09.1 | PROVIDER | Investigation cooperation | POLICY | MEDIUM | 3/4 → 4/4 |
| Art. 79 (C22) | Classification rules for high-risk AI systems | D-09.1 | PROVIDER | Annex III §1 (biometric) + §7 (border control) classification | POLICY | HIGH | 3/4 → 4/4 |
| Art. 80 (C23) | Annex III amendments | D-09.1 | PROVIDER | Annex III review | POLICY | LOW | — |
| Art. 84 (C24) | Market surveillance | D-09.1 | PROVIDER | Market surveillance cooperation | POLICY | MEDIUM | 3/4 → 4/4 |
| Art. 85 (C25) | Confidentiality | D-09.1 | PROVIDER | Confidentiality of trade secrets | POLICY | LOW | 3/4 → 4/4 |
| Art. 86 (C26) | Information to data subjects | D-09.1 | PROVIDER | Data subject information per AI_Act | POLICY | MEDIUM | 3/4 → 4/4 |
| Art. 87 (C27) | Complaints | D-09.1 | PROVIDER | Complaints handling | POLICY | MEDIUM | 3/4 → 4/4 |
| Art. 99 (C28) | Penalties | D-09.1 | MEMBER STATE | Fine schedule per Art. 99 | POLICY | CRITICAL — Up to €15M / 3% turnover | — |
| Annex III (C29) | High-risk AI system categories | D-09.1 | PROVIDER | §1 biometric + §7 border control | POLICY | HIGH | 3/4 → 4/4 |


**Total rows:** 112 (28 GDPR + 26 CRA + 29 NIS 2 + 29 AI_Act).

---
## 9. KEY OBSERVATIONS

1. **Maximum Regulatory Overlap:** SecureBorder has 4/5 regulations applicable — highest complexity in AEGIS case studies.

2. **Critical Class + High-Risk AI:** Rare combination requiring both CRA notified body assessment AND AI_Act conformity assessment.

3. **Biometric Data (Art. 9):** Requires explicit legal basis (government contract) + DPIA + enhanced security measures.

4. **NIS 2 Management Liability:** CEO/board personally liable for non-compliance — different from TinyTask (micro-enterprise exemption).

5. **24h Incident Notification:** Both CRA (actively exploited vulnerabilities) and NIS 2 (significant incidents) require 24h early warning — unified workflow required.

6. **92.1% Coverage:** Only 3 sub-domains uncovered (all DORA-exclusive) — excellent regulatory coverage.

7. **Existing ISO 27001:** Reduces implementation effort for all 4 regulations — strong foundation.

---

## 10. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | Compliance Lead | Initial release - SecureBorder Solutions case |
| 1.1 | 2026-04-11 | Compliance Lead | Added CRA 4 classes context; CRA Annex I Part I/II distinction; CRA two reporting flows (Art.14 vulns vs Art.15 incidents); GDPR Art.32 Processor NativeCompliance note; NIS 2 IR 2024/2690 reference; NIS 2 trust service derogation; NIS 2 ongoing incident provision; NIS 2 Directive vs Regulation note |
| 1.2 | 2026-04-11 | Compliance Lead | **C1 fix:** CRA reporting table corrected — severe incidents are Art. 14(3), not Art. 15 (which is voluntary); added Art. 15 caveat. **C2b fix:** Added GDPR Art. 37(1)(c) DPO mandatory for processor handling Art. 9 data at scale. **M4:** Added GDPR Art. 35(3)(b) automatic DPIA trigger for Art. 9. **M3:** Added GDPR Art. 33(2) "without undue delay" processor→controller. **M5:** Added CRA Art. 8 certification scheme caveat (none exists yet → defaults to Art. 32(3)). **M6/M7:** Added CRA Art. 13(8) 5-year support, Art. 13(9) 10-year update retention, Art. 13(13) 10-year documentation. **M9:** Added AI_Act Art. 5 prohibited practices negative analysis. **M10:** Added AI_Act Art. 73 3-tier incident reporting. **M11:** Added AI_Act Art. 25 downstream provider. **M12:** Added CRA Art. 24 exclusions analysis |

---

## 11. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Legal Counsel Review | | | |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| Business Review (CEO) | | | |

---

**Next Document:** 06_Clause_Mapping_Matrix.xlsx  
**Gate Status:** ⏳ PENDING REVIEW
