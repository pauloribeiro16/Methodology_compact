---
document_id: AEGIS-P2-RICH-11
title: AEGIS Control Set — Rich Mode (Case_01)
phase: 2
version: 4.0
created: 2026-08-07
updated: 2026-08-27
author: Orchestrator (Case_01 Control Set v1.0)
status: ACTIVE
inputs: [08_Obligation_Derivation.md, 09_Strategic_Tensions_Report.md, 10_Privacy_Security_Objectives.md, 13_Framework_Mapping_Matrix.md]
outputs: [Phase 3 inputs, control_set.yaml]
traceability: AEGIS Class Model → RulesCatalog, ComplianceRule, BestPracticeRule
case: Case_01_TinyTask_SaaS
tier: MICRO
normative_intensity_rule: AVG
frameworks_mapped: [NIST_CSF_2.0, NIST_Privacy_FW_1.0, AI_RMF_1.0, ISO_27001_2022, NIST_SSDF_SP800_218]
implementation_posture_decision: Implementation Posture Model v2.0 (qualitative state-based verification)
expected_obligation_controls: 30
expected_best_practice_controls: 16
expected_total_controls: 46
expected_fields_per_card: 24
detail_cards_count: 46
fields_per_card: 24
---

# AEGIS Control Set — Rich Mode (Case_01)

> **AEGIS Control Taxonomy — 38 sub-domains:** The AEGIS Control Taxonomy covers 38 security sub-domains as a core research contribution of the methodology.
> This document presents the implementation-ready Control Set for Case_01 (TinyTask SaaS, MICRO tier), consolidating **46 controls** (30 OBLIGATION + 16 BEST-PRACTICE) with complete traceability, qualitative implementation posture, and framework anchors.

---

## 1. DOCUMENT PURPOSE & TAXONOMY

This document evolves the legacy Rules Catalog into an implementation-ready **AEGIS Control Set**. It consolidates 46 controls (30 Obligation Controls + 16 Best-Practice Controls) covering 28 out of 38 AEGIS sub-domains. Each control is specified as a 24-field detail card with inline traceability (Legal → Phase 1 → Obligation → Objective), qualitative implementation posture, and framework anchors across NIST CSF 2.0, NIST Privacy FW 1.0, AI RMF 1.0, ISO 27001:2022, and NIST SSDF SP 800-218.

---

## 2. CONTROL SET SUMMARY & STATISTICS

### Obligation Controls (MUST) — 30

| Sub-Domain | Control Count |
|------------|--------------:|
| D-01 | 4 |
| D-02 | 3 |
| D-03 | 4 |
| D-04 | 4 |
| D-05 | 4 |
| D-06 | 3 |
| D-07 | 1 |
| D-08 | 2 |
| D-09 | 3 |
| D-10 | 2 |
| **TOTAL** | **30** |

### Best Practice Controls (SHOULD) — 16

| Sub-Domain | Control Count |
|------------|--------------:|
| D-01 | 2 |
| D-02 | 2 |
| D-03 | 3 |
| D-04 | 2 |
| D-05 | 1 |
| D-07 | 2 |
| D-09 | 1 |
| D-10 | 3 |
| **TOTAL** | **16** |

**Grand Total:** 30 OBLIGATION + 16 BEST-PRACTICE = **46 controls** across 28 sub-domains.

---

## 3. CONTROL DEFINITION SCHEMA (24 Fields)

| # | Field | Description | Example |
|--:|-------|-------------|---------|
| 1 | Rule ID | Unique identifier | CR-D-01.1-001 / BPR-D-01.1-001 |
| 2 | Description | Control requirement statement | Data at rest shall be encrypted |
| 3 | Scope | Control boundary scope | Persistent storage stores |
| 4 | Out of Scope | Excluded boundaries | Ephemeral logs |
| 5 | Source Article / Framework | Statutory source or framework anchor | GDPR Art. 32(1)(a) / ISO 27001 A.8.24 |
| 6 | NIST CSF Anchors | NIST CSF subcategories | PR.DS-01, PR.DS-10 |
| 7 | Verification Criteria | Measurable check criterion | AWS KMS active audit |
| 8 | Verification Method | TEST, INSPECT, DEMONSTRATE, ANALYZE | TEST |
| 9 | Owner | Operational owner | CTO + Lead Dev |
| 10 | Status | Operational status | ACTIVE |
| 11 | Dependencies | Dependent obligations / objectives | OBL-D-01.1-001, SO-D-01.1-001 |
| 12 | Risk if not met | Risk impact rating | HIGH |
| 13 | Affected Stakeholders | Impacted roles | Customers, DPO, CTO |
| 14 | Implementation Status (CSF) | Target state | PARTIAL |
| 15 | Implementation Priority | Priority level | HIGH |
| 16 | Regulatory Reporting | Reporting mandate | Internal audit only |
| 17 | External Auditor | Verification expectation | Third-party audit |
| 18 | Supervisory Body | Regulator | CNPD / ENISA |
| 19 | Normative Intensity | MUST (NI≥2.5) or SHOULD | 3 — MUST |
| 20 | CSF Subcategories | CSF 2.0 mapping | PR.DS-01 |
| 21 | Privacy FW Subcategories | Privacy FW 1.0 mapping | PR.DS-P1 |
| 22 | Implementation Status (CSF) | Qualitative posture state | IMPLEMENTED (AWS KMS active) |
| 23 | Implementation Status (Privacy) | Qualitative posture state | PARTIAL (missing: review cadence) |
| **24** | **Traceability & Framework Anchors** | **Inline 5-framework anchors & 4-tier trace** | **Legal → Phase 1 → Obligation → Objective** |

---

## PARTE I — OBLIGATION CONTROLS (30 CR)

### CR-D-01.1-001 — Data at Rest Encryption
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** All personal and product data in persistent storage must be protected by confidentiality mechanisms with segregated cryptographic material management. Operationalises OBL-D-01.1 by turning the confidentiality and integrity requirement into a mandatory storage-control baseline. The control reduces the impact of a stolen snapshot, misdirected backup, or unauthorised storage read. The rule is necessary because personal data and product data are processed in a multi-tenant boundary that is subject to GDPR Art. 5(1)(f) and CRA Annex I confidentiality obligations.

2. **Scope:** All persistent stores of personal and product data: primary stores, replicas, snapshots, and archival stores. Covers all substrates (object, block, file, key-value, relational).

3. **Out of Scope:** Customer-side confidentiality mechanisms, dedicated hardware confidentiality modules, and customer-managed cryptographic programmes that are outside TinyTask's MICRO operating boundary.

4. **Source Article:** GDPR Art. 5(1)(f) + Art. 32(1)(b); CRA Art. 24
   (source clauses GDPR-C04, GDPR-C14, CRA-C07).

5. **NIST CSF Anchors:** PR.DS-01, PR.DS-10, PR.PS-04.

6. **Verification Criteria:**

   - Configuration report demonstrates confidentiality mechanisms are active in all persistent stores of personal or product data.

   - Cryptographic material management report demonstrates separation between material access and data access.

   - Periodic review finds no unprotected production store or snapshot.

7. **Verification Method:** TEST

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-01.1-001, PO-D-01.1-001, SO-D-01.1-001
    CR-D-01.2-001, CR-D-01.3-001, CR-D-01.4-001.

11. **Risk if not met:** H — Storage compromise can expose tenant data and create
    GDPR confidentiality and CRA product-security findings.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C04 NI=3, GDPR-C14 NI=3, CRA-C07 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** PR.DS-01 (CIA of data-at-rest protected), PR.DS-10 (CIA of data-in-use protected), PR.PS-04 (log records generated + available)

20. **Privacy FW Subcategories:** PR.DS-P1 (CIA of data-at-rest protected) (backups created + protected + maintained + tested) (resilience mechanisms for adverse situations)

21. **Implementation Status (CSF):** IMPLEMENTED (AWS KMS encryption active - STORE-01/02)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** GDPR Art. 5(1)(f) + Art. 32(1)(b); CRA Art. 24
    - Phase 1: AG-D-01 (Doc13 §2.1)
    - Obligation: OBL-D-01.1-001
    - Objective: PO-D-01.1-001, SO-D-01.1-001

24. **Framework Anchors:**
    - CSF: PR.DS-01, PR.DS-10, PR.PS-04
    - PF: PR.DS-P1, UNMAPPED_PF (PR.DS-10 risk-strategy mgmt + PR.PS-04 log records — no PF 1.0 analogue)
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: PO.5

---

### CR-D-01.2-001 — Data in Transit Encryption
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** All personal and product data crossing network boundaries must be protected by confidentiality mechanisms appropriate to the channel classification. Operationalises OBL-D-01.2 by turning the in-transit confidentiality requirement into a mandatory channel-control baseline. The control prevents interception and downgrade attacks while data moves between processing components and external interfaces. The rule supplies evidence that the boundary is protected beyond the storage layer, satisfying GDPR Art. 32(1)(a) and CRA Annex I in-transit confidentiality.

2. **Scope:** All network channels carrying personal or product data: ingress channels from data subjects, egress channels to third-party services, and inter-component channels within the processing environment.

3. **Out of Scope:** Customer network security, non-routable provider-internal traffic, and deferred mutual confidentiality between every internal service.

4. **Source Article:** GDPR Art. 5(1)(f) + Art. 32(1)(a); CRA Art. 25
   (source clauses GDPR-C15, CRA-C08).

5. **NIST CSF Anchors:** PR.DS-02, PR.IR-01, PR.PS-04.

6. **Verification Criteria:**

   - Configuration report demonstrates confidentiality mechanisms are active in all network channels carrying personal or product data.

   - Cryptographic material management report demonstrates separation between channel-protection keys and data keys.

   - Annual review finds no unprotected channel.

7. **Verification Method:** TEST

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-01.2-001, PO-D-01.2-001, SO-D-01.2-001
    CR-D-01.1-001, CR-D-01.3-001.

11. **Risk if not met:** H — Network interception can disclose personal data and
    undermine GDPR security and CRA access-protection expectations.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C15 NI=3, CRA-C08 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** PR.DS-02 (CIA of data-in-transit protected), PR.IR-01 (networks protected from unauthorised access), PR.PS-04 (log records generated + available)

20. **Privacy FW Subcategories:** PR.DS-P2 (CIA of data-in-transit protected) (networks protected from unauthorised access)

21. **Implementation Status (CSF):** IMPLEMENTED (TLS 1.3 active - FLOW-01/05)

22. **Implementation Status (Privacy):** IMPLEMENTED (TLS 1.3 active - FLOW-01/05)

23. **Traceability:**
    - Legal: ** GDPR Art. 5(1)(f) + Art. 32(1)(a); CRA Art. 25
    - Phase 1: AG-D-01 (Doc13 §2.1)
    - Obligation: OBL-D-01.2-001
    - Objective: PO-D-01.2-001, SO-D-01.2-001

24. **Framework Anchors:**
    - CSF: PR.DS-02, PR.IR-01, PR.PS-04
    - PF: PR.DS-P2, PR.PO-P7
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### CR-D-01.3-001 — Cryptographic Key Management
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** Cryptographic material used by protection mechanisms must be managed with segregation between material access and data access, and with documented lifecycle covering generation, rotation, revocation, and destruction. Operationalises OBL-D-01.3 by turning the key-management requirement into a mandatory material-control baseline. The control prevents data from being intelligible when material access is compromised, and supports GDPR Art. 4(5) pseudonymisation test on a single artefact.

2. **Scope:** All cryptographic material: keys, key-handling credentials, and related authentication material. Covers generation, distribution, rotation, revocation, and destruction stages.

3. **Out of Scope:** Dedicated hardware confidentiality-module deployment, bespoke customer-managed material custody, and plaintext material escrow or manual distribution.

4. **Source Article:** CRA Art. 15 + Art. 24 (source clause CRA-C15);
   related GDPR security rationale: Art. 32(1)(a).

5. **NIST CSF Anchors:** GV.OV-01, GV.RM-04, PR.AA-03, PR.AA-04, PR.DS-01
   PR.IR-03.

6. **Verification Criteria:**

   - Cryptographic material management report demonstrates separation between material access and data access.

   - Periodic review documents the lifecycle: rotation cadence, revocation procedure, and de-attribution test.

   - Annual audit confirms no plaintext material in source control.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-01.3-001, PO-D-01.3-001 (Phase 1 Rich; absent
    from Phase 2 Doc 10, F-03), SO-D-01.3-001, CR-D-01.1-001, CR-D-01.2-001.

11. **Risk if not met:** H — Key compromise defeats encryption controls and can expose
    every tenant, backup, and audit record protected by the affected key.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses CRA-C15 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.OV-01 (strategy outcomes reviewed + adjusted), GV.RM-04 (strategic risk-response direction communicated), PR.AA-03 (users/services/HW authenticated), PR.AA-04 (identity assertions managed + protected), PR.DS-01 (CIA of data-at-rest protected), PR.IR-03 (resilience mechanisms in adverse situations)

20. **Privacy FW Subcategories:** PR.DS-P1 (CIA of data-at-rest protected), CT.DP-P2 (de-identification + tokenisation techniques)

21. **Implementation Status (CSF):** PARTIAL (What's missing: key lifecycle policy)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** CRA Art. 15 + Art. 24 (source clause CRA-C15);
    - Phase 1: AG-D-01 (Doc13 §2.1)
    - Obligation: OBL-D-01.3-001
    - Objective: PO-D-01.3-001

24. **Framework Anchors:**
    - CSF: GV.OV-01, GV.RM-04, PR.AA-03, PR.AA-04, PR.DS-01, PR.IR-03
    - PF: PR.DS-P1, CT.DP-P2
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### CR-D-01.4-001 — Data Integrity Mechanisms
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** All personal and product data must be protected against unauthorised modification through integrity controls appropriate to data class. Operationalises OBL-D-01.4 by turning the integrity requirement into a mandatory data-control baseline. The control detects corruption, logs it, and reports it. The rule supports GDPR Art. 5(1)(d) accuracy principle and CRA Annex I integrity obligations.

2. **Scope:** All data classes in scope: personal data, product data, and audit records. Covers structural constraints (schema-level), cryptographic integrity (application boundary), and physical redundancy (infrastructure layer).

3. **Out of Scope:** Blockchain anchoring, TPM-backed attestation, and forensic immutability beyond the selected tamper-evident and cryptographic integrity controls.

4. **Source Article:** GDPR Art. 5(1)(d) + Art. 32(1)(b); CRA Annex I §1.3(c)
   (source clauses GDPR-C05, CRA-C09).

5. **NIST CSF Anchors:** PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-01, PR.DS-10
   PR.IR-03, PR.IR-04, PR.PS-04.

6. **Verification Criteria:**

   - Configuration report demonstrates integrity controls are active across personal data, product data, and audit log artifacts.

   - Periodic integrity test demonstrates corruption detection within recovery window.

   - Annual review confirms structural, cryptographic, and physical controls are mutually consistent.

7. **Verification Method:** TEST

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-01.4-001, PO-D-01.4-001, SO-D-01.4-001
    CR-D-01.1-001, CR-D-01.3-001.

11. **Risk if not met:** H — Undetected manipulation can invalidate compliance evidence
    and cause loss of reliable customer or incident records.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C05 NI=3, CRA-C09 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** PR.DS-01 (CIA of data-at-rest protected), PR.DS-02 (CIA of data-in-transit protected), PR.DS-10 (CIA of data-in-use protected), PR.DS-01 (backups created + protected + tested), PR.DS-10 (data managed per risk strategy (CIA)), PR.IR-03 (resilience mechanisms in adverse situations), PR.IR-04 (adequate resource capacity for availability), PR.PS-04 (log records generated + available)

20. **Privacy FW Subcategories:** CT.DM-P1 (data elements accessible for review), CT.DM-P3 (data elements accessible for alteration)

21. **Implementation Status (CSF):** PARTIAL (What's missing: integrity verification schedule)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** GDPR Art. 5(1)(d) + Art. 32(1)(b); CRA Annex I §1.3(c)
    - Phase 1: AG-D-01 (Doc13 §2.1)
    - Obligation: OBL-D-01.4-001
    - Objective: PO-D-01.4-001, SO-D-01.4-001

24. **Framework Anchors:**
    - CSF: PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-01, PR.DS-10, PR.IR-03, PR.IR-04, PR.PS-04
    - PF: CT.DM-P1, CT.DM-P3
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### CR-D-02.1-001 — Vulnerability-Free Release
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires each TinyTask release to be
   assessed for known exploitable vulnerabilities before it is made available. It
   operationalises OBL-D-02.1 by combining dependency inventory, image scanning
   source analysis, and a release decision that blocks unacceptable findings.

   The rule covers both the product supplied to customers and the supporting build
   chain. A zero-known-exploitable-vulnerability decision must be reproducible from
   the scan results, severity policy, exception record, and release artifact.

   Implement automated vulnerability scanner and managed dependency audit gates in CI, maintain a machine-readable SBOM SBOM, consume
   trusted advisory feeds, and require CTO or Lead Dev approval for any documented
   exception. Rebuild or remove affected components before release when a critical
   finding has no accepted mitigation.



2. **Scope:** Application dependencies, Docker or runtime images, in-house source
   release artifacts, SBOM records, and the CI release gate.

3. **Out of Scope:** Vulnerabilities in unrelated customer infrastructure, speculative
   zero-days with no available indicator, and deferred runtime instrumentation.

4. **Source Article:** CRA Art. 17 + Art. 5 (source clauses CRA-C01, CRA-C17).

5. **NIST CSF Anchors:** GV.OV-02, ID.AM-02, ID.IM-02, ID.RA-01, ID.RA-03
   ID.RA-05, PR.PS-02.

6. **Verification Criteria:**

   - Every pull request and release runs automated vulnerability scanner and blocks unresolved `CRITICAL` findings.

   - `managed dependency audit --audit-level=high` and the dependency policy produce a retained result.

   - The release record links the scan result, SBOM, approvals, and any accepted exception.

7. **Verification Method:** DEMONSTRATE

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-02.1-001, SO-D-02.1-001, BPR-D-02.1-001
    BPR-D-07.2-001, CR-D-02.2-001, CR-D-06.2-001.

11. **Risk if not met:** H — A known exploitable release can harm customers and trigger
    CRA market-surveillance or incident-reporting exposure.

12. **Affected Stakeholders:** Customers, DPO, CTO, Lead Dev, Procurement, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** ENISA 24h (CRA).

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses CRA-C01 NI=3, CRA-C17 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.OV-02 (strategy reviewed for risk-landscape changes), ID.AM-02 (software/services/systems inventories maintained), ID.IM-02 (improvement processes implemented across tiers), ID.RA-01 (vulnerabilities identified + validated + recorded), ID.RA-03 (threats identified + recorded + prioritised), ID.RA-05 (threats/vulns inform risk-response decisions), PR.PS-02 (software maintained + replaced + removed)

20. **Privacy FW Subcategories:** ID.RA-P3 (problematic data actions identified), ID.RA-P5 (risk responses prioritised + implemented)

21. **Implementation Status (CSF):** NOT IMPLEMENTED (What's missing: zero-CVE release gate)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** CRA Art. 17 + Art. 5 (source clauses CRA-C01, CRA-C17).
    - Phase 1: AG-D-02 (Doc13 §2.2)
    - Obligation: OBL-D-02.1-001
    - Objective: SO-D-02.1-001

24. **Framework Anchors:**
    - CSF: GV.OV-02, ID.AM-02, ID.IM-02, ID.RA-01, ID.RA-03, ID.RA-05, PR.PS-02
    - PF: ID.RA-P3, ID.RA-P5
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.8
    - SSDF: RV.1

---

### CR-D-02.2-001 — Automated Security Updates and Patch Remediation
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to identify and remediate
   vulnerabilities through an automated, severity-aware update process. It translates
   OBL-D-02.2 into a repeatable patch path for operating systems, dependencies
   containers, and other deployed components.

   Automation reduces the window in which a published weakness can be exploited and
   prevents patch decisions from depending on an informal memory or a single person.
   The control must still retain human review for failed patches, compatibility
   issues, and exceptions affecting customer availability.

   Implement managed automated patch pipeline for supported hosts, rebuild images
   after dependency updates, track a severity SLA, and link each exception to an
   owner and compensating control. For critical findings, use the 72-hour rule in
   this catalog as the maximum remediation window and escalate earlier where possible.



2. **Scope:** Amazon Linux hosts, container base images, application dependencies
   deployed services, patch baselines, exception records, and remediation logs.

3. **Out of Scope:** Unmanaged customer endpoints, unsupported third-party systems
   and emergency changes that cannot be safely automated without a documented review.

4. **Source Article:** CRA Art. 4 + Art. 5 (source clauses CRA-C04, CRA-C19).

5. **NIST CSF Anchors:** GV.OV-02, ID.RA-01, PR.IR-03, PR.PS-01, PR.PS-02.

6. **Verification Criteria:**

   - managed automated patch pipeline scan and install baselines run on the defined production schedule.

   - Critical vulnerabilities have a recorded remediation or approved exception within 72 hours.

   - A quarterly review reconciles the asset inventory, patch log, and unresolved findings.

7. **Verification Method:** TEST

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-02.2-001, SO-D-02.2-001, BPR-D-02.2-001
    CR-D-02.1-001, CR-D-02.3-001, CR-D-06.2-001.

11. **Risk if not met:** H — Delayed remediation leaves exploitable systems exposed and
    can breach the CRA vulnerability-handling expectations.

12. **Affected Stakeholders:** Customers, DPO, CTO, Lead Dev, Procurement, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** ENISA 24h (CRA).

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses CRA-C04 NI=3, CRA-C19 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.OV-02 (strategy reviewed for risk-landscape changes), ID.RA-01 (vulnerabilities identified + validated + recorded), PR.IR-03 (resilience mechanisms in adverse situations), PR.PS-01 (config mgmt practices established + applied), PR.PS-02 (software maintained + replaced + removed)

20. **Privacy FW Subcategories:** — (product-security deliverable; SSDF RV.2 anchored; no PF 1.0 scope)

21. **Implementation Status (CSF):** NOT IMPLEMENTED (What's missing: automated 72h patch SLA)

22. **Implementation Status (Privacy):** N/A — product-security deliverable (SSDF RV.2)

23. **Traceability:**
    - Legal: ** CRA Art. 4 + Art. 5 (source clauses CRA-C04, CRA-C19).
    - Phase 1: AG-D-02 (Doc13 §2.2)
    - Obligation: OBL-D-02.2-001
    - Objective: SO-D-02.2-001

24. **Framework Anchors:**
    - CSF: GV.OV-02, ID.RA-01, PR.IR-03, PR.PS-01, PR.PS-02
    - PF: — (SSDF RV.2 deliverable)
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.8
    - SSDF: RV.2

---

### CR-D-02.3-001 — Coordinated Vulnerability Disclosure and Reporting
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to maintain a public
   coordinated vulnerability disclosure channel and a documented route for severe
   vulnerability reports. It operationalises OBL-D-02.3 so that researchers, users
   and authorities can reach an accountable response function.

   A visible disclosure channel improves discovery quality and gives the manufacturer
   a controlled triage path instead of encouraging untracked reports to individual
   employees. The process must distinguish ordinary reports from actively exploited
   or severe incidents that require the CRA notification route.

   Implement `/.well-known/security.txt`, a monitored security contact, a triage
   register, severity classification, acknowledgement procedure, and an escalation
   decision that can produce the required ENISA or CSIRT submission within 24 hours.



2. **Scope:** Public security contact, security.txt, CVD policy, triage register
   severity decisions, researcher communications, and authority-reporting evidence.

3. **Out of Scope:** A paid bug-bounty programme, anonymous handling without an
   accountable mailbox, and vulnerabilities unrelated to TinyTask or its services.

4. **Source Article:** CRA Art. 19 + Art. 20 (source clauses CRA-C21, CRA-C26).

5. **NIST CSF Anchors:** GV.PO-01, GV.SC-04, ID.RA-01, RS.CO-03, RS.MA-01.

6. **Verification Criteria:**

   - `/.well-known/security.txt` returns a valid contact and current disclosure policy.

   - A controlled researcher test is acknowledged and recorded within five business days.

   - A severe or actively exploited scenario produces a reviewed ENISA/CSIRT report record within 24 hours.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-02.3-001, SO-D-02.3-001, CR-D-02.1-001
    CR-D-02.2-001, CR-D-04.3-001.

11. **Risk if not met:** H — Unmanaged disclosure can prolong exploitation and create
    direct CRA reporting and market-surveillance exposure.

12. **Affected Stakeholders:** Customers, security researchers, DPO, CTO, Lead Dev
    ENISA, PT CSIRT (CNCS).

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** ENISA 24h (CRA).

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses CRA-C21 NI=3, CRA-C26 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.PO-01 (cybersecurity policy established + enforced), GV.SC-04 (suppliers routinely assessed (audits/tests)), ID.RA-01 (vulnerabilities identified + validated + recorded), RS.CO-03 (info shared with stakeholders per criteria), RS.MA-01 (coordination with stakeholders per criteria)

20. **Privacy FW Subcategories:** — (product-security deliverable; SSDF RV.1 anchored; no PF 1.0 scope)

21. **Implementation Status (CSF):** NOT IMPLEMENTED (What's missing: published security.txt & CVD policy)

22. **Implementation Status (Privacy):** N/A — product-security deliverable (SSDF RV.1)

23. **Traceability:**
    - Legal: ** CRA Art. 19 + Art. 20 (source clauses CRA-C21, CRA-C26).
    - Phase 1: AG-D-02 (Doc13 §2.2)
    - Obligation: OBL-D-02.3-001
    - Objective: SO-D-02.3-001

24. **Framework Anchors:**
    - CSF: GV.PO-01, GV.SC-04, ID.RA-01, RS.CO-03, RS.MA-01
    - PF: — (SSDF RV.1 deliverable)
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.5
    - SSDF: RV.1

---

### CR-D-03.1-001 — Authentication and Access Control
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires authentication and access-control
   measures for every TinyTask user-facing and administrative interface. It
   operationalises OBL-D-03.1 using the inherited managed identity service baseline while
   keeping TinyTask accountable for configuration and access decisions.

   Authentication establishes the identity of a principal before the service accepts
   a task, administrative action, or support operation. The inherited provider does
   not remove the need to configure secure session handling, lifecycle controls
   logging, and a documented review of provider assurance.

   Implement managed identity service with secure password and session settings, connect role
   claims to the application authorisation layer, disable departed accounts, and
   restrict administrative operations to named roles. Keep the provider attestation
   and configuration export with the internal control evidence.



2. **Scope:** Customer login, operator login, administrative endpoints, managed identity service
   configuration, session tokens, role claims, and account deprovisioning.

3. **Out of Scope:** A self-hosted identity provider, legacy federation not used by
   TinyTask customers, and customer identity policies outside the SaaS boundary.

4. **Source Article:** CRA Art. 10 (source clause CRA-C05).

5. **NIST CSF Anchors:** ID.AM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05
   PR.AA-06, PR.DS-10.

6. **Verification Criteria:**

   - managed identity service configuration and provider assurance evidence are current and approved.

   - Unauthenticated requests cannot access protected task or administration endpoints.

   - A quarterly orphan-account and role-claim review has CTO sign-off.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-03.1-001, SO-D-03.1-001, BPR-D-03.1-001
    CR-D-03.2-001, CR-D-03.3-001, CR-D-06.1-001.

11. **Risk if not met:** H — Account takeover or unauthorised administration can expose
    customer data and compromise the product boundary.

12. **Affected Stakeholders:** Customers, data subjects, CTO, Lead Dev, DPO, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses CRA-C05 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** ID.AM-01 (hardware inventories maintained), PR.AA-01 (identities/credentials managed for users/svcs/HW), PR.AA-02 (identities proofed + bound to credentials), PR.AA-03 (users/services/HW authenticated), PR.AA-05 (access permissions managed (least privilege)), PR.AA-06 (access to assets limited to authorised), PR.DS-10 (data managed per risk strategy (CIA))

20. **Privacy FW Subcategories:** PR.AC-P1 (identities/credentials issued, managed, verified, revoked, audited — maps PR.AA-01/02), PR.AC-P6 (proofed and bound to credentials, authenticated commensurate with risk — maps PR.AA-03), PR.AC-P4 (access permissions, least privilege + SoD — maps PR.AA-05/06); UNMAPPED_PF (ID.AM-01 hardware inventories + PR.DS-10 risk-strategy data mgmt — no PF 1.0 analogue; unmapped_pf_justification: PF 1.0 inventories are data-ecosystem-scoped only)

21. **Implementation Status (CSF):** IMPLEMENTED (Auth0 managed IAM - SYS-02)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** CRA Art. 10 (source clause CRA-C05).
    - Phase 1: AG-D-03 (Doc13 §2.3)
    - Obligation: OBL-D-03.1-001
    - Objective: SO-D-03.1-001

24. **Framework Anchors:**
    - CSF: ID.AM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06, PR.DS-10
    - PF: PR.AC-P1, PR.AC-P6, PR.AC-P4, UNMAPPED_PF (asset inventory + risk-strategy data mgmt — no PF 1.0 analogue)
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.16
    - SSDF: -

---

### CR-D-03.2-001 — Administrative Multi-Factor Authentication
Type: CONTROL — OBLIGATION (MUST, NI=2 (SHOULD))


1. **Description:** The implementation rule requires multi-factor authentication for
   administrative accounts and other privileged access where the TinyTask threat
   profile warrants it. It operationalises OBL-D-03.2 without imposing an unsuitable
   enterprise identity architecture on the MICRO deployment.

   Privileged credentials can bypass ordinary tenant boundaries, change security
   settings, or disable evidence collection. MFA adds an independent factor and
   materially reduces the likelihood that a reused or phished password becomes a
   production compromise.

   Implement managed identity service MFA for administrators, enforce the setting at the
   privileged route, protect recovery and reset flows, and review enrolment status.
   Record exceptions explicitly; a privileged account without MFA must not be used
   for routine administration and requires an approved compensating control.



2. **Scope:** CTO, Lead Dev, support-admin, deployment, and other privileged accounts;
   MFA enrolment, recovery, session, and enforcement configuration.

3. **Out of Scope:** Mandatory hardware tokens for every end user, customer-selected
   MFA methods outside TinyTask control, and non-privileged consumer convenience flows.

4. **Source Article:** CRA Art. 9 (source clause CRA-C06); related GDPR security
   rationale: Art. 32(1).

5. **NIST CSF Anchors:** PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02.

6. **Verification Criteria:**

   - An automated test confirms privileged routes reject sessions without a second factor.

   - managed identity service MFA enrolment is complete for every named administrative account.

   - Recovery tokens, reset events, and MFA changes are logged and reviewed quarterly.

7. **Verification Method:** TEST

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-03.2-001, SO-D-03.2-001, BPR-D-03.2-001
    CR-D-03.1-001, CR-D-03.3-001, CR-D-01.3-001.

11. **Risk if not met:** H — A stolen administrator password could bypass tenant
    encryption, and monitoring safeguards.

12. **Affected Stakeholders:** Customers, data subjects, CTO, Lead Dev, DPO, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(source clauses CRA-C06 NI=2 (single-source CR; CRA Art. 9 MFA);
    AVG=2.0 → bucket P2 [2.0, 2.5) → SHOULD. Single-source cards with NI=2
    are NOT automatically escalated; AVG preserves the SHOULD signal even
    though the underlying clause is mandatory for default-class products
    (per Bloco B BPR policy).)*



19. **CSF Subcategories:** PR.AA-03 (users/services/HW authenticated), PR.AA-04 (identity assertions managed + protected), PR.AA-05 (access permissions managed (least privilege)), PR.AA-06 (access to assets limited to authorised), PR.AT-02 (workforce understands roles in cyber objectives)

20. **Privacy FW Subcategories:** PR.AC-P6 (authentication commensurate with risk), PR.AC-P4 (least-privilege access), GV.AT-P1 (workforce informed/trained); UNMAPPED_PF (PR.AA-04 identity assertions — no PF 1.0 subcategory; concept exists only in non-final PF 1.1 draft)

21. **Implementation Status (CSF):** IMPLEMENTED (Auth0 admin MFA enforced - Doc 04a §1.4)

22. **Implementation Status (Privacy):** IMPLEMENTED (Auth0 admin MFA enforced - Doc 04a §1.4)

23. **Traceability:**
    - Legal: ** CRA Art. 9 (source clause CRA-C06); related GDPR security
    - Phase 1: AG-D-03 (Doc13 §2.3)
    - Obligation: OBL-D-03.2-001
    - Objective: SO-D-03.2-001

24. **Framework Anchors:**
    - CSF: PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02
    - PF: PR.AC-P6, PR.AC-P4, GV.AT-P1, UNMAPPED_PF (identity assertions — no PF 1.0 subcategory)
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.5
    - SSDF: -

---

### CR-D-03.3-001 — Authorisation and Least Privilege
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to restrict actions and
   data access to authorised principals and to apply least privilege. It operationalises
   OBL-D-03.3 across application roles, cloud identities, support access, and CI/CD
   identities rather than treating login alone as sufficient protection.

   Least privilege limits the blast radius of a compromised account and supports
   accountability for customer-data processing. The rule must express permitted
   operations in a maintained role matrix, separate tenant data at the query boundary
   and prevent broad wildcard permissions from becoming a hidden default.

   Implement managed identity custom claims or equivalent RBAC, enforce tenant scoping in
   service logic and database queries, use narrowly scoped managed identity service policies, and
   perform a quarterly access review with documented removal of stale grants.



2. **Scope:** managed identity roles, application authorisation, tenant isolation, managed identity service
   managed source control automation identities, support access, and privileged service accounts.

3. **Out of Scope:** Attribute-based access-control programmes, continuous behavioural
   analytics, and authorisation decisions belonging to a customer's own IdP.

4. **Source Article:** GDPR Art. 5(1)(c) + Art. 22 and Art. 32(1)(b); CRA Art. 8
   (source clauses GDPR-C10, GDPR-C17).

5. **NIST CSF Anchors:** ID.AM-01, ID.AM-02, PR.AA-01, PR.AA-03, PR.AA-05
   PR.AA-06, PR.PS-04.

6. **Verification Criteria:**

   - The RBAC matrix maps every protected operation to an approved role and tenant boundary.

   - Negative tests show cross-tenant reads, wildcard grants, and unauthorised admin actions fail.

   - Quarterly IAM and application-role review has CTO sign-off and removes stale permissions.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-03.3-001, SO-D-03.3-001
    CR-D-03.1-001, CR-D-03.2-001, CR-D-03.4-001.

11. **Risk if not met:** H — Excess privilege can cause cross-tenant disclosure, unlawful
    processing, or destructive administrative actions.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C10 NI=3, GDPR-C17 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** ID.AM-01 (hardware inventories maintained), ID.AM-02 (software/services/systems inventories maintained), PR.AA-01 (identities/credentials managed for users/svcs/HW), PR.AA-03 (users/services/HW authenticated), PR.AA-05 (access permissions managed (least privilege)), PR.AA-06 (access to assets limited to authorised), PR.PS-04 (log records generated + available)

20. **Privacy FW Subcategories:** CT.PO-P1 (data-processing authorisation policies)

21. **Implementation Status (CSF):** PARTIAL (What's missing: quarterly access review evidence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** GDPR Art. 5(1)(c) + Art. 22 and Art. 32(1)(b); CRA Art. 8
    - Phase 1: AG-D-03 (Doc13 §2.3)
    - Obligation: OBL-D-03.3-001
    - Objective: SO-D-03.3-001

24. **Framework Anchors:**
    - CSF: ID.AM-01, ID.AM-02, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.PS-04
    - PF: CT.PO-P1, PR.AC-P1, PR.AC-P6, PR.AC-P4, UNMAPPED_PF (asset inventories + log records — no PF 1.0 analogue)
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.15
    - SSDF: -

---

### CR-D-03.4-001 — Secure System Defaults
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires every TinyTask deployment and
   product configuration to start from a secure default. It operationalises OBL-D-03.4
   by removing unused ports and services, preventing default credentials, and making
   the safest supported behaviour the configuration a new tenant receives.

   Secure defaults reduce the number of decisions administrators must make correctly
   and limit accidental exposure during provisioning. They also make security tests
   repeatable because a clean environment has a known baseline rather than inherited
   permissive settings.

   Implement account-level managed object storage public-access blocks, managed identity service password and sign-up
   protections, deny-by-default network rules, secret-free sample configuration, and
   production error handling that does not reveal stack traces. Review changes against
   a CIS-oriented baseline before release.



2. **Scope:** managed hosting account defaults, network security groups, managed identity service settings
   application configuration, service exposure, passwords, and production errors.

3. **Out of Scope:** A full documented best-practice framework hardening programme, bespoke tenant
   baselines, and specialised appliance or operating-system configurations outside TinyTask.

4. **Source Article:** CRA Art. 3 + Art. 8 (source clause CRA-C03); related GDPR
   rationale: Art. 25(2).

5. **NIST CSF Anchors:** GV.PO-01, GV.SC-03, PR.DS-10, PR.PS-01, PR.PS-04.

6. **Verification Criteria:**

   - Account-level controls block public S3 access and new resources inherit deny-by-default rules.

   - Configuration tests find no default password, open administrative port, or unused exposed service.

   - Production error responses contain an opaque correlation identifier rather than stack details.

7. **Verification Method:** TEST

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-03.4-001, SO-D-03.4-001, BPR-D-03.4-001
    CR-D-03.1-001, CR-D-03.3-001, CR-D-01.1-001.

11. **Risk if not met:** H — A permissive default can expose the service before an
    administrator notices the configuration error.

12. **Affected Stakeholders:** Customers, data subjects, CTO, Lead Dev, DPO, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses CRA-C03 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.PO-01 (cybersecurity policy established + enforced), GV.SC-03 (contracts implement cyber programme measures), PR.DS-10 (data managed per risk strategy (CIA)), PR.PS-01 (config mgmt practices established + applied), PR.PS-04 (log records generated + available)

20. **Privacy FW Subcategories:** CT.DP-P4 (selective collection/disclosure configurable), CT.PO-P4 (data lifecycle aligned with SDLC)

21. **Implementation Status (CSF):** PARTIAL (What's missing: hardened baseline documentation)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** CRA Art. 3 + Art. 8 (source clause CRA-C03); related GDPR
    - Phase 1: AG-D-03 (Doc13 §2.3)
    - Obligation: OBL-D-03.4-001
    - Objective: SO-D-03.4-001

24. **Framework Anchors:**
    - CSF: GV.PO-01, GV.SC-03, PR.DS-10, PR.PS-01, PR.PS-04
    - PF: CT.DP-P4, CT.PO-P4
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.9
    - SSDF: PW.9

---

### CR-D-04.1-001 — Exploit Severity Limitation and Fail-Safe Design
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to limit the severity of
   security exploits and to fail safely when a security-relevant condition is detected.
   It operationalises OBL-D-04.1 by turning detection, throttling, isolation, and
   service-safe behaviour into explicit product and infrastructure controls.

   The purpose is to contain an event before it becomes a material compromise. Alerts
   alone are insufficient: a control must either prevent dangerous continuation
   reduce available privileges, preserve evidence, or route the event to a person who
   can take the defined containment action.

   Implement managed monitoring alarms and managed notification routing, rate limits, guarded feature flags
   safe error paths, and isolation procedures for compromised accounts or components.
   Exercise the alarm-to-action path and retain the resulting event record.



2. **Scope:** Application fail-safe paths, managed monitoring alarms, managed threat detection findings, managed notification
   notifications, rate limits, account isolation, and security-relevant service events.

3. **Out of Scope:** A managed security operations capability, enterprise centralized audit-log management, automated orchestration platform, and
   advanced adversarial simulation beyond the MICRO control baseline.

4. **Source Article:** CRA Art. 6 + Art. 13; related GDPR security rationale:
   Art. 32(1)(b) (source clause CRA-C13).

5. **NIST CSF Anchors:** DE.AE-02, DE.CM-01, DE.CM-09, ID.RA-04, PR.PS-04
   RS.MA-01, RS.MA-02, RS.MA-03.

6. **Verification Criteria:**

   - A simulated anomalous API pattern triggers the managed monitoring alarm and managed notification.

   - A fail-safe test disables or limits the affected operation without corrupting customer data.

   - managed threat detection findings have a named owner, triage record, and documented containment decision.

7. **Verification Method:** DEMONSTRATE

8. **Owner:** CTO + DPO + Compliance Lead

9. **Status:** TODO

10. **Dependencies:** OBL-D-04.1-001, SO-D-04.1-001, CR-D-02.3-001
    CR-D-04.2-001, CR-D-04.3-001, CR-D-10.2-001.

11. **Risk if not met:** H — An uncontained exploit can become a reportable personal-data
    breach or actively exploited product vulnerability.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD 72h (GDPR).

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses CRA-C13 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** DE.AE-02 (adverse events analysed to understand targets), DE.CM-01 (networks monitored for adverse events), DE.CM-09 (HW/SW/runtime/data monitored for adverse events), ID.RA-04 (impacts + likelihoods identified + prioritised), PR.PS-04 (log records generated + available), RS.MA-01 (incident response plan executed), RS.MA-02 (incidents triaged + validated), RS.MA-03 (incidents categorised + prioritised)

20. **Privacy FW Subcategories:** CM.AW-P7 (privacy breach/event notifications) (privacy performance measured + reviewed)

21. **Implementation Status (CSF):** PARTIAL (What's missing: automated containment playbooks)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** CRA Art. 6 + Art. 13; related GDPR security rationale:
    - Phase 1: AG-D-04 (Doc13 §2.4)
    - Obligation: OBL-D-04.1-001
    - Objective: SO-D-04.1-001

24. **Framework Anchors:**
    - CSF: DE.AE-02, DE.CM-01, DE.CM-09, ID.RA-04, PR.PS-04, RS.MA-01, RS.MA-02, RS.MA-03
    - PF: CM.AW-P7
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.25
    - SSDF: RV.1

---

### CR-D-04.2-001 — Availability Restoration and DoS Resilience
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to restore availability
   after an incident and to resist denial-of-service conditions. It operationalises
   OBL-D-04.2 through resilience controls, a containment procedure, and tested
   recovery decisions rather than an unverified availability statement.

   Availability is a security property for a task-management SaaS: customers need
   access to tasks and the service must continue protecting data while under attack.
   The implementation must preserve a controlled degraded mode where possible and
   avoid recovery actions that bypass authentication or tenant isolation.

   Implement rate limiting, managed edge filtering, health checks, backup-aware
   recovery, and a documented four-hour containment playbook. Define who can block
   traffic, disable an account, rotate a key, or communicate with customers, then
   demonstrate those actions in a resilience drill.



2. **Scope:** Public endpoints, managed content delivery and application protections, health checks
   containment playbook, backup recovery, and service restoration procedures.

3. **Out of Scope:** Active-active multi-region operation, enterprise DDoS operations
   and automated orchestration beyond the selected managed hosting controls.

4. **Source Article:** GDPR Art. 32(1)(c); CRA Art. 11 (source clauses GDPR-C18
   CRA-C11).

5. **NIST CSF Anchors:** DE.CM-09, PR.DS-10, PR.IR-03, PR.IR-04, RC.RP-01
   RC.RP-04, RS.MI-01, RS.MI-02.

6. **Verification Criteria:**

   - A controlled DoS or rate-limit drill shows that service protections activate without cross-tenant access.

   - The containment playbook demonstrates account disablement, traffic blocking, and key rotation.

   - A restore exercise records availability recovery and confirms the documented recovery objective.

7. **Verification Method:** DEMONSTRATE

8. **Owner:** CTO + DPO + Compliance Lead

9. **Status:** TODO

10. **Dependencies:** OBL-D-04.2-001, SO-D-04.2-001
    CR-D-04.1-001, CR-D-04.4-001, CR-D-01.3-001.

11. **Risk if not met:** H — Prolonged outage or unsafe mitigation can deny customer
    access and increase the consequences of a security incident.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD 72h (GDPR).

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C18 NI=3, CRA-C11 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** DE.CM-09 (HW/SW/runtime/data monitored for adverse events), PR.DS-10 (data managed per risk strategy (CIA)), PR.IR-03 (resilience mechanisms in adverse situations), PR.IR-04 (adequate resource capacity for availability), RC.RP-01 (recovery plan executed + verified), RC.RP-04 (restoration procedures verified), RS.MI-01 (incidents contained + mitigated), RS.MI-02 (incidents eradicated)

20. **Privacy FW Subcategories:** PR.PO-P7 (incident response + recovery plans maintained), CT.DM-P10 (technical measures tested + assessed)

21. **Implementation Status (CSF):** PARTIAL (What's missing: DDoS restoration drills)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** GDPR Art. 32(1)(c); CRA Art. 11 (source clauses GDPR-C18
    - Phase 1: AG-D-04 (Doc13 §2.4)
    - Obligation: OBL-D-04.2-001
    - Objective: SO-D-04.2-001

24. **Framework Anchors:**
    - CSF: DE.CM-09, PR.DS-10, PR.IR-03, PR.IR-04, RC.RP-01, RC.RP-04, RS.MI-01, RS.MI-02
    - PF: PR.PO-P7, CT.DM-P10
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.26
    - SSDF: -

---

### CR-D-04.3-001 — Dual Regulatory Incident Notification
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to route qualifying
   incidents through one notification workflow that meets the strictest applicable
   clock. It operationalises OBL-D-04.3 for the GDPR controller-to-CNPD path, the
   processor-to-controller path, and the CRA manufacturer-to-ENISA path.

   The event record must distinguish a personal-data breach from an actively exploited
   vulnerability while allowing both conditions to activate together. A 24-hour
   internal clock is the selected max-SLA route; it is an internal control target
   not a replacement for the legally distinct recipient and content requirements.

   Implement a severity and trigger decision tree, start the clock at incident
   awareness, assign CTO/DPO ownership, generate per-recipient submissions, preserve
   evidence, and test the workflow with tabletop scenarios. Escalation must reach
   CNPD, ENISA, PT CSIRT, and affected B2B controllers through documented contacts.



2. **Scope:** Incident intake, trigger classification, clock start, notification templates
   CNPD and ENISA submissions, controller communications, evidence, and approvals.

3. **Out of Scope:** Separate duplicated incident systems for each regulation, events
   outside TinyTask's reporting role, and notification decisions delegated without review.

4. **Source Article:** GDPR Art. 33(1) + Art. 33(2) + Art. 33(3); CRA Art. 20
   (source clauses GDPR-C21, GDPR-C23, CRA-C25).

5. **NIST CSF Anchors:** RS.CO-02, RS.MA-01, RS.MA-01, RS.MA-02, RS.MA-03
   RS.MA-01.

6. **Verification Criteria:**

   - A compound-event tabletop produces both CNPD and ENISA submissions from one event record within 24 hours.

   - The playbook records the GDPR 72-hour, CRA 24-hour, and processor-to-controller paths separately.

   - Quarterly review confirms contacts, templates, approval roles, and clock-start evidence remain current.

7. **Verification Method:** TEST

8. **Owner:** CTO + DPO + Compliance Lead

9. **Status:** TODO

10. **Dependencies:** OBL-D-04.3-001, SO-D-04.3-001
    CR-D-02.3-001, CR-D-04.1-001, CR-D-04.2-001, CR-D-10.2-001.

11. **Risk if not met:** H — A missed notification deadline can create severe GDPR fines
    CRA non-conformity, and loss of customer trust.

12. **Affected Stakeholders:** Customers, data subjects, B2B controllers, DPO, CTO
    Compliance Lead, CNPD, ENISA, PT CSIRT (CNCS).

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD 72h + ENISA 24h (max-SLA routing).

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C21 NI=3, GDPR-C23 NI=3, CRA-C25 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** RS.CO-02 (events reported internally per criteria), RS.MA-01 (coordination with stakeholders per criteria), RS.MA-01 (incident response plan executed), RS.MA-02 (incidents triaged + validated), RS.MA-03 (incidents categorised + prioritised), RS.MA-01 (incident response plan execution (legacy v1.1))

20. **Privacy FW Subcategories:** CM.AW-P7 (privacy breach/event notifications), CM.AW-P8 (mitigation mechanisms offered to individuals), CM.PO-P1 (transparency policies for data processing), CM.PO-P2 (comms roles + responsibilities established) (contracts implement privacy programme measures)

21. **Implementation Status (CSF):** PARTIAL (What's missing: tested 24h CRA breach workflow)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** GDPR Art. 33(1) + Art. 33(2) + Art. 33(3); CRA Art. 20
    - Phase 1: AG-D-04 (Doc13 §2.4)
    - Obligation: OBL-D-04.3-001
    - Objective: SO-D-04.3-001

24. **Framework Anchors:**
    - CSF: RS.CO-02, RS.MA-01, RS.MA-01, RS.MA-02, RS.MA-03, RS.MA-01
    - PF: CM.AW-P7, CM.AW-P8, CM.PO-P1, CM.PO-P2
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.24
    - SSDF: -

---

### CR-D-04.4-001 — Data Restoration and Recovery
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to restore systems and
   data after an incident while preserving documented recovery objectives. It
   operationalises OBL-D-04.4 through managed backups, tested restoration, and a
   controlled recovery sequence that does not weaken access or integrity safeguards.

   Recovery evidence demonstrates that availability is more than a backup checkbox.
   The team must know which stores are protected, which order they are restored in
   how customer data is reconciled, and how a failed restore is escalated without
   silently accepting data loss.

   Implement managed backup with documented retention coverage for managed relational database, managed NoSQL, and managed object storage, retain protected copies
   maintain a recovery runbook, and perform a periodic restore exercise. Record RTO
   and RPO results, test application health after restoration, and review backup
   permissions and retention alongside the encryption rules.



2. **Scope:** Production data stores, managed backup with documented retention vaults, snapshots, cross-region copy
   restore runbook, application health checks, RTO/RPO evidence, and access controls.

3. **Out of Scope:** Active-active multi-region architecture, continuous data replication
   to every region, and recovery of customer systems outside TinyTask control.

4. **Source Article:** GDPR Art. 32(1)(b) and (c) + Art. 19; CRA Art. 26
   (source clause GDPR-C16).

5. **NIST CSF Anchors:** PR.DS-01, PR.DS-10, PR.IR-03, PR.IR-04, RC.RP-01
   RC.RP-03, RC.RP-04.

6. **Verification Criteria:**

   - managed backup with documented retention plans cover managed relational database, managed NoSQL, and managed object storage with protected recovery points.

   - A quarterly restore exercise completes within the documented 24-hour recovery objective.

   - Post-restore checks confirm tenant isolation, encryption, audit logging, and data integrity.

7. **Verification Method:** DEMONSTRATE

8. **Owner:** CTO + DPO + Compliance Lead

9. **Status:** TODO

10. **Dependencies:** OBL-D-04.4-001, SO-D-04.4-001, CR-D-04.2-001
    CR-D-01.1-001, CR-D-01.4-001, CR-D-10.2-001.

11. **Risk if not met:** H — Irrecoverable or prolonged data loss can interrupt service
    and amplify the impact of a personal-data or product-security incident.

12. **Affected Stakeholders:** Customers, data subjects, B2B controllers, DPO, CTO
    Lead Dev, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD 72h (GDPR).

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C16 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** PR.DS-01 (backups created + protected + tested), PR.DS-10 (data managed per risk strategy (CIA)), PR.IR-03 (resilience mechanisms in adverse situations), PR.IR-04 (adequate resource capacity for availability), RC.RP-01 (recovery plan executed + verified), RC.RP-03 (backup integrity verified), RC.RP-04 (restoration procedures verified)

20. **Privacy FW Subcategories:** PR.DS-P1 (data-at-rest protected), PR.PO-P7 (response/recovery plans established — maps PR.IR-03), PR.DS-P4 (adequate resource capacity — maps PR.IR-04), PR.PT-P4 (resilience mechanisms); UNMAPPED_PF (RC.RP-* recovery execution + PR.DS-10 risk-strategy mgmt — PF 1.0 has no Respond/Recover axis; unmapped_pf_justification: no PF 1.0 subcategories match)

21. **Implementation Status (CSF):** PARTIAL (What's missing: backup restore drills evidence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** GDPR Art. 32(1)(b) and (c) + Art. 19; CRA Art. 26
    - Phase 1: AG-D-04 (Doc13 §2.4)
    - Obligation: OBL-D-04.4-001
    - Objective: SO-D-04.4-001

24. **Framework Anchors:**
    - CSF: PR.DS-01, PR.DS-10, PR.IR-03, PR.IR-04, RC.RP-01, RC.RP-03, RC.RP-04
    - PF: PR.DS-P1, PR.PO-P7, PR.DS-P4, PR.PT-P4, UNMAPPED_PF (recover-execution + risk-strategy mgmt — PF 1.0 has no Recover axis)
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.13
    - SSDF: -

---

### CR-D-05.1-001 — Data Minimisation
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to collect and process
   only data that is adequate, relevant, and necessary for task management. It
   operationalises OBL-D-05.1 by enforcing the approved data model at the schema
   API, application, and analytics boundaries.

   Data minimisation reduces privacy exposure and the security impact of an incident.
   A field that is not needed for an identified purpose should not be collected merely
   because storage is available, and operational logs must not become an uncontrolled
   secondary store of customer content.

   Implement an approved field inventory, schema constraints, API allow-lists, log
   redaction, and a review for new fields before deployment. Link each retained field
   to a purpose and reject unknown or unnecessary input at the service boundary.



2. **Scope:** Registration data, task and project fields, API payloads, database schema
   analytics events, logs, support exports, and new-field design reviews.

3. **Out of Scope:** Differential-privacy research, customer-controlled content choices
   within approved task fields, and data that TinyTask never receives.

4. **Source Article:** GDPR Art. 5(1)(c); CRA Annex I §1.2(c)
   (source clauses GDPR-C01, CRA-C10).

5. **NIST CSF Anchors:** GV.OC-03, GV.PO-01, ID.AM-03, PR.DS-01, PR.DS-10
   PR.PS-06.

6. **Verification Criteria:**

   - The documented field inventory maps every personal-data field to a stated purpose.

   - API schema tests reject unknown or disallowed fields with a controlled error.

   - Log and analytics tests show that customer content and unnecessary identifiers are redacted.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-05.1-001, PO-D-05.1-001
    CR-D-05.2-001, CR-D-09.4-001, CR-D-07.1-001.

11. **Risk if not met:** H — Excess collection increases breach impact and can violate
    GDPR data-minimisation accountability.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C01 NI=3, CRA-C10 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.OC-03 (legal/regulatory reqs incl privacy managed), GV.PO-01 (cybersecurity policy established + enforced), ID.AM-03 (data + metadata inventories maintained), PR.DS-01 (CIA of data-at-rest protected), PR.DS-10 (data managed per risk strategy (CIA)), PR.PS-06 (secure SW dev integrated in SDLC)

20. **Privacy FW Subcategories:** CT.PO-P4 (data lifecycle aligned with SDLC), CT.DP-P4 (selective collection/disclosure configurable), ID.RA-P3 (problematic data actions identified)

21. **Implementation Status (CSF):** IMPLEMENTED (Data minimisation in product design & Stripe isolation)

22. **Implementation Status (Privacy):** IMPLEMENTED (Data minimisation in product design & Stripe isolation)

23. **Traceability:**
    - Legal: ** GDPR Art. 5(1)(c); CRA Annex I §1.2(c)
    - Phase 1: AG-D-05 (Doc13 §2.5)
    - Obligation: OBL-D-05.1-001
    - Objective: PO-D-05.1-001

24. **Framework Anchors:**
    - CSF: GV.OC-03, GV.PO-01, ID.AM-03, PR.DS-01, PR.DS-10, PR.PS-06
    - PF: CT.PO-P4, CT.DP-P4, ID.RA-P3
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.10
    - SSDF: -

---

### CR-D-05.2-001 — Storage Limitation and Retention
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to retain personal data
   only for the period necessary for its documented purpose. It operationalises
   OBL-D-05.2 through a retention schedule, lifecycle automation, and evidence that
   expired records are removed from primary and secondary stores.

   Retention is not a single deletion date because customer content, audit logs
   backups, and temporary request files serve different purposes. The schedule must
   distinguish these classes, explain lawful exceptions, and prevent a generic
   indefinite-retention default.

   Implement managed object storage lifecycle rules, database deletion or TTL jobs, backup windows, and
   disposal of DSAR working data. For completed task data, apply the catalog's
   30-day post-completion rule unless an approved legal or contractual basis requires
   a different documented period.



2. **Scope:** Customer task data, account records, logs, backups, exports, support files
   DSAR working data, lifecycle rules, and retention exceptions.

3. **Out of Scope:** Customer-defined records held outside TinyTask, litigation holds
   not yet triggered, and unapproved indefinite archives.

4. **Source Article:** GDPR Art. 5(1)(e) (source clauses GDPR-C02, GDPR-C03).

5. **NIST CSF Anchors:** GV.OC-04, GV.OV-02, GV.PO-02, ID.AM-03, PR.DS-10
   PR.PS-02, PR.PS-04.

6. **Verification Criteria:**

   - The retention schedule identifies each data class, purpose, period, and disposal mechanism.

   - Lifecycle or database tests remove completed task data after the approved 30-day period.

   - A quarterly sample reconciles expired primary records, backups, exports, and DSAR files.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-05.2-001, PO-D-05.2-001
    CR-D-05.1-001, CR-D-05.3-001, CR-D-09.4-001.

11. **Risk if not met:** H — Over-retention expands breach exposure and can violate the
    GDPR storage-limitation principle.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, CNPD.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C02 NI=3, GDPR-C03 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.OC-04 (critical capabilities/services communicated), GV.OV-02 (strategy reviewed for risk-landscape changes), GV.PO-02 (cybersecurity processes/procedures enforced), ID.AM-03 (data + metadata inventories maintained), PR.DS-10 (data managed per risk strategy (CIA)), PR.PS-02 (software maintained + replaced + removed), PR.PS-04 (log records generated + available)

20. **Privacy FW Subcategories:** CT.PO-P4 (data lifecycle aligned with SDLC), CT.DM-P5 (data destroyed according to policy)

21. **Implementation Status (CSF):** NOT IMPLEMENTED (What's missing: formal retention approval)

22. **Implementation Status (Privacy):** NOT IMPLEMENTED (What missing: formal retention schedule approval)

23. **Traceability:**
    - Legal: ** GDPR Art. 5(1)(e) (source clauses GDPR-C02, GDPR-C03).
    - Phase 1: AG-D-05 (Doc13 §2.5)
    - Obligation: OBL-D-05.2-001
    - Objective: PO-D-05.2-001

24. **Framework Anchors:**
    - CSF: GV.OC-04, GV.OV-02, GV.PO-02, ID.AM-03, PR.DS-10, PR.PS-02, PR.PS-04
    - PF: CT.PO-P4, CT.DM-P5
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.33
    - SSDF: PS.3

---

### CR-D-05.3-001 — Complete and Secure Data Erasure
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to complete a verified
   erasure request within seven days and to remove the affected personal data from
   primary, derived, and recoverable stores. It operationalises OBL-D-05.3 with an
   executable request path rather than a manual promise.

   Secure deletion must preserve evidence that the request was fulfilled without
   retaining the erased content itself. It also must account for backups, caches
   exports, and derived stores so that a later restore does not silently reintroduce
   data that the service represented as erased.

   Implement an authenticated erasure endpoint, cascading database deletion, object
   removal, backup exclusion or tombstone handling, and a completion log keyed to the
   request. Run a test tenant through the full process and verify that no PII remains.



2. **Scope:** Customer-facing request intake, identity verification, primary database
   managed object storage objects, caches, exports, derived stores, backups, and completion evidence.

3. **Out of Scope:** Anonymisation used as a substitute for a valid erasure request
   data subject to a documented legal hold, and customer copies outside TinyTask.

4. **Source Article:** GDPR Art. 17; CRA Art. 11
   (source clauses GDPR-C06, CRA-C16).

5. **NIST CSF Anchors:** GV.SC-04, PR.DS-10, PR.DS-10, PR.DS-02.

6. **Verification Criteria:**

   - An end-to-end test removes a test subject from production-like primary and derived stores.

   - Backup handling prevents erased PII from becoming active after a controlled restore.

   - The request register records identity verification, completion, and the seven-day internal SLA.

7. **Verification Method:** TEST

8. **Owner:** CTO + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-05.3-001, PO-D-05.3-001
    BPR-D-05.3-001, CR-D-05.2-001, CR-D-04.4-001.

11. **Risk if not met:** H — Incomplete erasure can violate a data-subject right and
    expose supposedly deleted data after restoration.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, CNPD.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C06 NI=3, CRA-C16 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.SC-04 (suppliers routinely assessed (audits/tests)), PR.DS-10 (CIA of data-in-use protected), PR.DS-10 (data managed per risk strategy (CIA)), PR.DS-02 (CIA of data-in-transit protected)

20. **Privacy FW Subcategories:** CT.DM-P4 (data elements accessible for deletion), CT.DM-P5 (data destroyed according to policy) (contracts implement privacy programme measures)

21. **Implementation Status (CSF):** PARTIAL (What's missing: erasure cascade automation)

22. **Implementation Status (Privacy):** NOT IMPLEMENTED (What missing: erasure cascade automation)

23. **Traceability:**
    - Legal: ** GDPR Art. 17; CRA Art. 11
    - Phase 1: AG-D-05 (Doc13 §2.5)
    - Obligation: OBL-D-05.3-001
    - Objective: PO-D-05.3-001

24. **Framework Anchors:**
    - CSF: GV.SC-04, PR.DS-10, PR.DS-10, PR.DS-02
    - PF: CT.DM-P4, CT.DM-P5, PR.DS-P2
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.10
    - SSDF: -

---

### CR-D-05.4-001 — Structured Data Portability
Type: CONTROL — OBLIGATION (MUST, NI=2 (SHOULD))


1. **Description:** The implementation rule requires TinyTask to provide a data
   subject's personal data in a structured, commonly used, machine-readable format.
   It operationalises OBL-D-05.4 through an authenticated JSON export that completes
   within the catalog's 48-hour internal service objective.

   Portability supports user control and makes the right usable without exposing
   another tenant's information. The export must be complete for the requesting
   subject, scoped to authorised data, understandable, and protected during creation
   delivery, and disposal.

   Implement identity verification, a tenant-aware export query, a documented JSON
   schema, secure download or delivery, and short-lived export storage. Test completeness
   against the data inventory and log the request without placing exported PII in logs.



2. **Scope:** Request intake, identity and tenant verification, JSON schema, export
   endpoint, secure delivery, temporary storage, and completion records.

3. **Out of Scope:** Direct controller-to-controller transmission, proprietary export
   formats, and customer-generated data held only in external services.

4. **Source Article:** GDPR Art. 20 (source clause GDPR-C07).

5. **NIST CSF Anchors:** PR.DS-10, PR.DS-10, PR.AA-03, PR.DS-02.

6. **Verification Criteria:**

   - A test request returns all in-scope subject data in valid, documented JSON within 48 hours.

   - Cross-tenant and unauthenticated export attempts fail without disclosing record existence.

   - Temporary export objects expire and request logs contain no exported personal-data payload.

7. **Verification Method:** TEST

8. **Owner:** CTO + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-05.4-001, PO-D-05.4-001, CR-D-05.1-001
    CR-D-03.3-001, CR-D-01.2-001, CR-D-10.2-001.

11. **Risk if not met:** H — An incomplete or insecure export can deny a GDPR right or
    cause a cross-tenant personal-data disclosure.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, CNPD.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(source clauses GDPR-C07 NI=2;
    AVG=2.0 → bucket P2 ≥ 2.0 → SHOULD.)*



19. **CSF Subcategories:** PR.DS-10 (CIA of data-in-use protected), PR.DS-10 (data managed per risk strategy (CIA)), PR.AA-03 (users/services/HW authenticated), PR.DS-02 (CIA of data-in-transit protected)

20. **Privacy FW Subcategories:** CT.DM-P1 (data elements accessible for review), CT.DM-P6 (data transmitted via standardised formats)

21. **Implementation Status (CSF):** PARTIAL (What's missing: automated JSON export routine)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** GDPR Art. 20 (source clause GDPR-C07).
    - Phase 1: AG-D-05 (Doc13 §2.5)
    - Obligation: OBL-D-05.4-001
    - Objective: PO-D-05.4-001

24. **Framework Anchors:**
    - CSF: PR.DS-10, PR.DS-10, PR.AA-03, PR.DS-02
    - PF: CT.DM-P1, CT.DM-P6
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.14
    - SSDF: -

---

### CR-D-06.1-001 — Procefederated single sign-onr Due Diligence
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to use processors that
   provide sufficient data-protection and security guarantees. It operationalises
   OBL-D-06.1 through a proportionate supplier dossier for managed hosting, managed identity service, payment processor, and
   any new processor before customer data is entrusted to it.

   Provider inheritance is valuable only when the inherited boundary and evidence are
   understood. An assurance report does not decide whether the service configuration
   processing purpose, location, subprocessors, and contractual commitments are
   appropriate for TinyTask's actual use.

   Implement a vendor assessment that records the DPA, processing role, data classes
   locations, subprocessors, security attestation, and residual issues. Review material
   changes and retain current managed hosting documented third-party security attestation, managed identity service security, and payment processor assurance evidence.



2. **Scope:** managed hosting, managed identity, payment processor, future processors, DPAs, subprocessor lists
   assurance reports, data-flow decisions, and annual supplier review records.

3. **Out of Scope:** A continuous enterprise vendor-monitoring platform, suppliers that
   never receive or support personal data, and customer-selected providers outside TinyTask.

4. **Source Article:** GDPR Art. 28(1); related CRA supply-chain rationale:
   Art. 7(2)(b) (source clause GDPR-C11).

5. **NIST CSF Anchors:** GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04
   ID.RA-02.

6. **Verification Criteria:**

   - Every active processor dossier contains a current DPA and relevant assurance evidence.

   - The review records data location, subprocessors, processing purpose, and inherited boundaries.

   - A new-processor sample shows approval occurred before production personal data was transferred.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-06.1-001, SO-D-06.1-001, CR-D-06.3-001
    CR-D-03.1-001, CR-D-01.1-001, CR-D-09.2-001.

11. **Risk if not met:** H — An unsuitable processor can expose personal data and leave
    TinyTask unable to demonstrate GDPR Art. 28 accountability.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Procurement
    managed hosting, managed identity, payment processor, CNPD.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C11 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.SC-01 (SCRM programme/strategy/objectives established), GV.SC-02 (suppliers prioritised + assessed via SCRM), GV.SC-03 (contracts implement cyber programme measures), GV.SC-04 (suppliers routinely assessed (audits/tests)), ID.AM-04 (supplier/third-party inventories maintained), ID.RA-02 (threat/vuln intel from internal/external sources)

20. **Privacy FW Subcategories:** ID.IM-P2 (owners/operators + roles inventoried)

21. **Implementation Status (CSF):** PARTIAL (What's missing: standardized vendor ISO 27001 register)

22. **Implementation Status (Privacy):** NOT IMPLEMENTED (What missing: complete ISMS policy set)

23. **Traceability:**
    - Legal: ** GDPR Art. 28(1); related CRA supply-chain rationale:
    - Phase 1: AG-D-06 (Doc13 §2.6)
    - Obligation: OBL-D-06.1-001
    - Objective: SO-D-06.1-001

24. **Framework Anchors:**
    - CSF: GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, ID.RA-02
    - PF: ID.DE-P1, ID.IM-P2
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.19
    - SSDF: PW.4

---

### CR-D-06.2-001 — Software Bill of Materials
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to generate and retain a
   machine-readable software bill of materials for every release. It operationalises
   OBL-D-06.2 by creating an authoritative component inventory that can be correlated
   with vulnerability information throughout product support.

   The SBOM links the release artifact to direct and transitive dependencies, versions
   suppliers, and package identifiers. It enables the team to determine quickly whether
   a published vulnerability affects a deployed release instead of reconstructing the
   dependency state after an incident.

   Implement machine-readable SBOM generation in CI/CD, validate the file, bind it to the release
   identifier, and archive it with protected release evidence. Correlate current SBOMs
   with advisory feeds and retain security-update artifacts for the applicable CRA
   support and availability periods.



2. **Scope:** Application packages, transitive dependencies, container layers, release
   identifiers, machine-readable SBOM files, CI validation, archive, and vulnerability correlation.

3. **Out of Scope:** Full VEX automation, components absent from the delivered product
   and supplier inventories that TinyTask cannot lawfully redistribute.

4. **Source Article:** CRA Art. 18(2) + Annex I §1.4 (source clause CRA-C18).

5. **NIST CSF Anchors:** GV.SC-02, GV.SC-03, ID.AM-02, ID.RA-01, PR.PS-02.

6. **Verification Criteria:**

   - Every release tag produces a valid machine-readable SBOM SBOM linked to the release artifact.

   - A sample dependency is traceable from package identifier to version and advisory status.

   - Archived SBOM and security-update evidence remains protected and retrievable by release.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-06.2-001, SO-D-06.2-001, CR-D-02.1-001
    CR-D-02.2-001, CR-D-07.1-001, CR-D-10.2-001.

11. **Risk if not met:** H — TinyTask may be unable to identify affected releases or
    demonstrate CRA component and vulnerability management.

12. **Affected Stakeholders:** Customers, CTO, Lead Dev, Procurement, suppliers, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses CRA-C18 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.SC-02 (suppliers prioritised + assessed via SCRM), GV.SC-03 (contracts implement cyber programme measures), ID.AM-02 (software/services/systems inventories maintained), ID.RA-01 (vulnerabilities identified + validated + recorded), PR.PS-02 (software maintained + replaced + removed)

20. **Privacy FW Subcategories:** — (product-security deliverable; SSDF PS.3 anchored; no PF 1.0 scope)

21. **Implementation Status (CSF):** NOT IMPLEMENTED (What's missing: machine-readable CycloneDX SBOM)

22. **Implementation Status (Privacy):** N/A — product-security deliverable (SSDF PS.3)

23. **Traceability:**
    - Legal: ** CRA Art. 18(2) + Annex I §1.4 (source clause CRA-C18).
    - Phase 1: AG-D-06 (Doc13 §2.6)
    - Obligation: OBL-D-06.2-001
    - Objective: SO-D-06.2-001

24. **Framework Anchors:**
    - CSF: GV.SC-02, GV.SC-03, ID.AM-02, ID.RA-01, PR.PS-02
    - PF: — (SSDF PS.3 deliverable)
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.21
    - SSDF: PS.3

---

### CR-D-06.3-001 — Contractual Procefederated single sign-onr Security
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to bind processors to
   enforceable data-protection and security duties through a Data Processing Agreement.
   It operationalises OBL-D-06.3 by converting supplier assurances into contractual
   instructions, assistance, confidentiality, security, deletion, and audit terms.

   A supplier may have strong technical controls but still leave TinyTask without the
   rights needed to manage incidents, subprocessors, data-subject requests, or contract
   termination. The DPA and security addendum establish the legal and operational
   interface for those responsibilities.

   Implement an approved Art. 28(3) template, a current subprocessor list, security and
   incident clauses, return-or-deletion terms, and a change-control record. Reconcile
   each active processor contract with the vendor dossier and escalate missing or
   conflicting terms before production use.



2. **Scope:** Procefederated single sign-onr DPAs, supplier security addenda, instructions, subprocessors
   incident assistance, audit rights, termination, deletion, and contract reviews.

3. **Out of Scope:** Bespoke negotiation for clauses unrelated to security or privacy
   suppliers that do not process TinyTask data, and customer contracts outside this role.

4. **Source Article:** GDPR Art. 28(3); related CRA supply-chain rationale:
   Art. 7 + Art. 16 (source clause GDPR-C12).

5. **NIST CSF Anchors:** GV.OC-03, GV.SC-02, GV.SC-03, GV.SC-04, PR.DS-10
   PR.PS-06, RS.MA-01, RS.MI-01.

6. **Verification Criteria:**

   - Every active processor contract contains the required GDPR Art. 28(3) clauses.

   - The published or notified subprocessor list matches the suppliers in the data-flow inventory.

   - A contract sample links incident, deletion, audit, and return duties to named operational owners.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-06.3-001, SO-D-06.3-001, CR-D-06.1-001
    CR-D-04.3-001, CR-D-05.3-001, CR-D-09.4-001.

11. **Risk if not met:** H — TinyTask can lose required processor controls and be unable
    to obtain assistance or secure deletion during an incident or termination.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Procurement
    processors, CNPD.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C12 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.OC-03 (legal/regulatory reqs incl privacy managed), GV.SC-02 (suppliers prioritised + assessed via SCRM), GV.SC-03 (contracts implement cyber programme measures), GV.SC-04 (suppliers routinely assessed (audits/tests)), PR.DS-10 (data managed per risk strategy (CIA)), PR.PS-06 (secure SW dev integrated in SDLC), RS.MA-01 (coordination with stakeholders per criteria), RS.MI-01 (incidents contained + mitigated)

20. **Privacy FW Subcategories:** ID.DE-P3 (contracts with ecosystem parties implement privacy-programme measures), ID.DE-P4 (interoperability frameworks for ecosystem privacy); UNMAPPED_PF (ecosystem risk integrated into enterprise risk — no dedicated PF 1.0 subcategory; covered indirectly by GV.PO-P6)

21. **Implementation Status (CSF):** PARTIAL (What's missing: B2B processor DPA template execution)

22. **Implementation Status (Privacy):** N/A — product-security deliverable (SSDF RV.1)

23. **Traceability:**
    - Legal: ** GDPR Art. 28(3); related CRA supply-chain rationale:
    - Phase 1: AG-D-06 (Doc13 §2.6)
    - Obligation: OBL-D-06.3-001
    - Objective: SO-D-06.3-001

24. **Framework Anchors:**
    - CSF: GV.OC-03, GV.SC-02, GV.SC-03, GV.SC-04, PR.DS-10, PR.PS-06, RS.MA-01, RS.MI-01
    - PF: ID.DE-P3, ID.DE-P4, UNMAPPED_PF (ecosystem risk into enterprise risk — no PF 1.0 subcategory)
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.20
    - SSDF: -

---

### CR-D-07.1-001 — Security and Privacy by Design
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to integrate data
   protection and product security from design through deployment and support. It
   operationalises OBL-D-07.1 by making secure design, review, testing, release, and
   support activities part of the development workflow.

   A late security check cannot reliably correct an unsafe architecture or unnecessary
   data flow. The rule therefore connects threat modelling, privacy review, secure
   coding, dependency controls, and safe defaults to the feature decision before code
   reaches production.

   Implement a NIST SSDF and OWASP SAMM-based checklist, architecture and threat review
   for material features, protected branches, release security evidence, and a support
   record. Preserve the CRA five-year support commitment per release and keep security
   updates available for at least ten years or the support period, whichever is longer.



2. **Scope:** Requirements, architecture, privacy review, threat modelling, code review
   CI/CD gates, release evidence, product support, updates, and secure defaults.

3. **Out of Scope:** Formal SDL certification, an enterprise change board, and controls
   unrelated to a TinyTask feature, release, or supported product component.

4. **Source Article:** GDPR Art. 25; CRA Art. 18 + Art. 23 and Art. 13(8)-(9)
   (source clauses GDPR-C09, CRA-C02, CRA-C22).

5. **NIST CSF Anchors:** GV.PO-02, ID.RA-01, PR.DS-10, PR.PS-01, PR.PS-02
   PR.PS-06.

6. **Verification Criteria:**

   - Each material feature has completed security and privacy design checks before merge.

   - Release evidence shows review, scanning, approved dependencies, and secure-default validation.

   - The release register records support and security-update availability commitments.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-07.1-001, PO-D-07.1-001
    BPR-D-07.1-001, BPR-D-07.2-001, CR-D-02.1-001, CR-D-06.2-001.

11. **Risk if not met:** H — Design defects can become systemic privacy and product
    vulnerabilities that are difficult to remediate after release.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, DevOps
    ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C09 NI=3, CRA-C02 NI=3, CRA-C22 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.PO-02 (cybersecurity processes/procedures enforced), ID.RA-01 (vulnerabilities identified + validated + recorded), PR.DS-10 (data managed per risk strategy (CIA)), PR.PS-01 (config mgmt practices established + applied), PR.PS-02 (software maintained + replaced + removed), PR.PS-06 (secure SW dev integrated in SDLC)

20. **Privacy FW Subcategories:** GV.PO-P2 (privacy values in SDLC processes established), CT.PO-P4 (data lifecycle aligned with SDLC), CT.DP-P2 (de-identification + tokenisation techniques), CT.DP-P4 (selective collection/disclosure configurable), CT.DP-P5 (attribute substitution (derived values))

21. **Implementation Status (CSF):** PARTIAL (What's missing: formal threat model per release)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** GDPR Art. 25; CRA Art. 18 + Art. 23 and Art. 13(8)-(9)
    - Phase 1: AG-D-07 (Doc13 §2.7)
    - Obligation: OBL-D-07.1-001
    - Objective: PO-D-07.1-001

24. **Framework Anchors:**
    - CSF: GV.PO-02, ID.RA-01, PR.DS-10, PR.PS-01, PR.PS-02, PR.PS-06
    - PF: GV.PO-P2, CT.PO-P4, CT.DP-P2, CT.DP-P4, CT.DP-P5
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.25
    - SSDF: PO.1

---

### CR-D-08.1-001 — Annual Security Awareness
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires every person involved in TinyTask
   processing operations to receive security and privacy awareness training annually.
   It operationalises OBL-D-08.1 through a concise programme appropriate to an
   eight-person team, with attendance and content evidence.

   Human error can bypass well-configured technical controls through phishing, unsafe
   sharing, weak incident escalation, or misuse of customer data. General awareness
   establishes the common behaviours every role must understand before specialised
   role training is considered.

   Implement an annual programme using approved ENISA or NCSC material, cover phishing
   credentials, customer data, incident reporting, secure remote work, and provider
   responsibilities, and retain delivery and acknowledgement records. Review content
   after material incidents or control changes.



2. **Scope:** Employees and contractors involved in processing, annual core content
   acknowledgement evidence, onboarding awareness, and programme review.

3. **Out of Scope:** Large-scale phishing simulation platforms, unrelated professional
   education, and formal certification for every member of the MICRO team.

4. **Source Article:** GDPR Art. 39(1)(b) + Art. 5(2) (source clause GDPR-C27).

5. **NIST CSF Anchors:** PR.AT-01, PR.AT-02, PR.PS-01.

6. **Verification Criteria:**

   - All in-scope personnel have a dated annual training acknowledgement or completion record.

   - The retained material covers credentials, data handling, phishing, and incident escalation.

   - A quarterly programme review records any content change arising from incidents or control changes.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + HR + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-08.1-001, SO-D-08.1-001, CR-D-08.2-001
    CR-D-04.3-001, CR-D-03.2-001.

11. **Risk if not met:** M — Unaware personnel can cause avoidable compromise, delayed
    reporting, or improper personal-data handling.

12. **Affected Stakeholders:** All staff, contractors, customers, data subjects, DPO
    CTO, HR, CNPD.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C27 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** PR.AT-01 (users informed + trained on cyber topics), PR.AT-02 (workforce understands roles in cyber objectives), PR.PS-01 (config mgmt practices established + applied)

20. **Privacy FW Subcategories:** GV.AT-P1 (personnel awareness + training on privacy tasks), GV.AT-P2 (specialised roles privacy awareness + training)

21. **Implementation Status (CSF):** PARTIAL (What's missing: phishing drills & tracking)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** GDPR Art. 39(1)(b) + Art. 5(2) (source clause GDPR-C27).
    - Phase 1: AG-D-08 (Doc13 §2.8)
    - Obligation: OBL-D-08.1-001
    - Objective: SO-D-08.1-001

24. **Framework Anchors:**
    - CSF: PR.AT-01, PR.AT-02, PR.PS-01
    - PF: GV.AT-P1, GV.AT-P2
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.6.3
    - SSDF: PO.2

---

### CR-D-08.2-001 — Role-Specific Security Competence
Type: CONTROL — OBLIGATION (MUST, NI=2 (SHOULD))


1. **Description:** The implementation rule requires TinyTask personnel to receive
   security and privacy guidance matched to their responsibilities. It operationalises
   OBL-D-08.2 by separating the competence needed by developers, administrators, the
   DPO, and incident decision-makers while retaining one proportionate matrix.

   General awareness does not teach a developer how to interpret a vulnerable build
   an administrator how to preserve incident evidence, or a DPO how to evaluate a
   breach and DPIA. Role-specific depth reduces ambiguity at the point where a person
   must make a control or reporting decision.

   Implement a competency matrix, developer secure-coding material, administrator
   hardening and recovery guidance, and DPO privacy and incident duties. Review the
   matrix quarterly, record completed role modules, and update content when duties or
   product risks change.



2. **Scope:** Developer, administrator, CTO, DPO, support, HR, and incident roles;
   competency matrix, role modules, completion evidence, and review records.

3. **Out of Scope:** Mandatory external certification, separate training platforms for
   each role, and competence requirements unrelated to assigned TinyTask duties.

4. **Source Article:** GDPR Art. 37 + Art. 39; related CRA product-security competence:
   Art. 18(2) (source clause GDPR-C28).

5. **NIST CSF Anchors:** GV.RR-02, GV.RR-04, GV.SC-03, PR.AT-01, PR.AT-02
   PR.AT-02.

6. **Verification Criteria:**

   - The competency matrix maps every security and privacy duty to a named role and module.

   - Developers, administrators, and the DPO have current completion evidence for their modules.

   - A quarterly review records role, control, incident, or regulatory changes affecting content.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + HR + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-08.2-001, SO-D-08.2-001, CR-D-08.1-001
    CR-D-07.1-001, CR-D-04.3-001, CR-D-09.2-001.

11. **Risk if not met:** M — Personnel may apply controls or regulatory decisions
    incorrectly despite completing general awareness.

12. **Affected Stakeholders:** All staff, contractors, customers, DPO, CTO, HR
    Lead Dev, CNPD, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(source clauses GDPR-C28 NI=2;
    AVG=2.0 → bucket P2 ≥ 2.0 → SHOULD.)*



19. **CSF Subcategories:** GV.RR-02 (roles/responsibilities established + enforced), GV.RR-04 (cyber in HR practices (screening, training)), GV.SC-03 (contracts implement cyber programme measures), PR.AT-01 (users informed + trained on cyber topics), PR.AT-02 (workforce understands roles in cyber objectives), PR.AT-02 (partners + third parties understand roles)

20. **Privacy FW Subcategories:** GV.AT-P1 (personnel awareness + training on privacy tasks), GV.AT-P2 (specialised roles privacy awareness + training)

21. **Implementation Status (CSF):** PARTIAL (What's missing: role-specific curriculum)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** GDPR Art. 37 + Art. 39; related CRA product-security competence:
    - Phase 1: AG-D-08 (Doc13 §2.8)
    - Obligation: OBL-D-08.2-001
    - Objective: SO-D-08.2-001

24. **Framework Anchors:**
    - CSF: GV.RR-02, GV.RR-04, GV.SC-03, PR.AT-01, PR.AT-02, PR.AT-02
    - PF: GV.AT-P1, GV.AT-P2
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.6.3
    - SSDF: PO.2

---

### CR-D-09.1-001 — Security Governance and Technical Documentation
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to maintain appropriate
   technical and organisational measures in a documented policy architecture and to
   preserve the CRA technical documentation for ten years. It operationalises
   OBL-D-09.1 across privacy accountability, security governance, and manufacturer evidence.

   Documentation must describe controls that actually operate; a policy detached from
   configuration, owners, or evidence does not demonstrate compliance or security.
   The integrated repository should make each policy, architecture decision, release
   record, and review traceable without creating duplicate GDPR and CRA silos.

   Implement a version-controlled policy set, approval and review records, control
   ownership, architecture and product-security documentation, and retention rules.
   Link policies to evidence from managed hosting, managed identity, CI/CD, incidents, risk assessments
   and processing records, with access restricted to authorised roles.



2. **Scope:** Security and privacy policies, technical documentation, architecture
   control ownership, approvals, version history, evidence links, and ten-year retention.

3. **Out of Scope:** Mandatory ISO 27001 certification, an enterprise GRC platform
   and documentation unrelated to TinyTask's processing or product obligations.

4. **Source Article:** GDPR Art. 5(2) + Art. 24; CRA Art. 13 + Annex VII
   (source clauses GDPR-C08, GDPR-C25, GDPR-C26, CRA-C24).

5. **NIST CSF Anchors:** GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-02, GV.OV-01.

6. **Verification Criteria:**

   - The approved policy set identifies owners, scope, controls, evidence, and review status.

   - CRA technical documentation is versioned, linked to releases, and retained for ten years.

   - A sampled policy control reconciles to current configuration or operational evidence.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + DPO + Compliance Lead + Legal

9. **Status:** TODO

10. **Dependencies:** OBL-D-09.1-001, PO-D-09.1-001, SO-D-09.1-001
    BPR-D-09.1-001, CR-D-09.2-001, CR-D-09.4-001, CR-D-10.3-001.

11. **Risk if not met:** H — TinyTask may lack evidence of accountability and CRA
    conformity even where individual technical controls exist.

12. **Affected Stakeholders:** Customers, DPO, CTO, Compliance Lead, Legal, CEO
    CNPD, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD + ENISA (periodic).

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C08 NI=3, GDPR-C25 NI=3, GDPR-C26 NI=3, CRA-C24 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** GV.PO-01 (cybersecurity policy established + enforced), GV.PO-02 (cybersecurity processes/procedures enforced), GV.RM-04 (strategic risk-response direction communicated), GV.RR-02 (roles/responsibilities established + enforced), GV.OV-01 (strategy outcomes reviewed + adjusted)

20. **Privacy FW Subcategories:** GV.PO-P1 (privacy values + policies established + enforced), GV.PO-P5 (legal/regulatory privacy reqs understood + managed) (privacy risk-response strategic direction) (adequate resources for privacy risk strategy), CM.PO-P1 (transparency policies for data processing)

21. **Implementation Status (CSF):** NOT IMPLEMENTED (What's missing: complete ISMS policy set)

22. **Implementation Status (Privacy):** NOT IMPLEMENTED (What missing: formal risk register & DPIA)

23. **Traceability:**
    - Legal: ** GDPR Art. 5(2) + Art. 24; CRA Art. 13 + Annex VII
    - Phase 1: AG-D-09 (Doc13 §2.9)
    - Obligation: OBL-D-09.1-001
    - Objective: PO-D-09.1-001, SO-D-09.1-001

24. **Framework Anchors:**
    - CSF: GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-02, GV.OV-01
    - PF: GV.PO-P1, GV.PO-P5, GV.PO-P3, CM.PO-P1, UNMAPPED_PF (positive-risk GV.RM-04 — no PF 1.0 subcategory)
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.1
    - SSDF: PO.4

---

### CR-D-09.2-001 — Unified Privacy and Cybersecurity Risk Assessment
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to assess privacy impact
   and product cybersecurity risk before relevant launch or material change. It
   operationalises OBL-D-09.2 through one evidence repository and a unified template
   that produces distinct GDPR DPIA and CRA risk outputs.

   The assessments have different legal triggers and conclusions, but they share
   assets, data flows, threats, controls, and residual-risk evidence. Combining the
   factual analysis avoids duplication while preserving separate decisions about
   data-subject risk, consultation, product risk, and conformity.

   Implement a trigger screen for every material feature, document processing and
   product assets, analyse threats and impacts, assign controls and owners, approve
   residual risk, and refresh the record after significant change or new evidence.
   Route unresolved scope or risk acceptance to the human decision-maker.



2. **Scope:** Feature and launch trigger screening, DPIA, CRA risk assessment, data flows
   threats, controls, residual risk, approvals, consultation, and reassessment evidence.

3. **Out of Scope:** Automatic acceptance of high residual risk, a single conclusion
   substituted for both laws, and external services not part of TinyTask's product or processing.

4. **Source Article:** GDPR Art. 32(2) + Art. 35 + Art. 36; CRA Art. 13(5)
   + Annex VII §2 (source clauses GDPR-C20, GDPR-C24, CRA-C23).

5. **NIST CSF Anchors:** ID.RA-01, ID.RA-04, ID.RA-05, GV.RM-06, GV.OV-02.

6. **Verification Criteria:**

   - Every material feature has a recorded trigger decision before production approval.

   - The unified record produces separately identifiable DPIA and CRA risk conclusions.

   - Sampled high or unresolved risks show an owner, treatment, and human approval or escalation.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + DPO + Compliance Lead + Legal

9. **Status:** TODO

10. **Dependencies:** OBL-D-09.2-001, PO-D-09.2-001, SO-D-09.2-001
    CR-D-05.1-001, CR-D-07.1-001, CR-D-09.1-001, CR-D-10.3-001.

11. **Risk if not met:** H — Unassessed processing or product risk can expose data
    subjects and place a non-conforming product on the market.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Compliance Lead
    Legal, CEO, CNPD, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD + ENISA (periodic).

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C20 NI=3, GDPR-C24 NI=3, CRA-C23 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** ID.RA-01 (vulnerabilities identified + validated + recorded), ID.RA-04 (impacts + likelihoods identified + prioritised), ID.RA-05 (threats/vulns inform risk-response decisions), GV.RM-06 (standardised risk calculation method), GV.OV-02 (strategy reviewed for risk-landscape changes)

20. **Privacy FW Subcategories:** ID.RA-P3 (problematic data actions identified), ID.RA-P4 (likelihoods + impacts prioritise risk), ID.RA-P5 (risk responses prioritised + implemented) (privacy strategy reviewed for requirements + risks)

21. **Implementation Status (CSF):** NOT IMPLEMENTED (What's missing: formal risk register & DPIA)

22. **Implementation Status (Privacy):** NOT IMPLEMENTED (What missing: standardized vendor ISO 27001 register & B2B DPA)

23. **Traceability:**
    - Legal: ** GDPR Art. 32(2) + Art. 35 + Art. 36; CRA Art. 13(5)
    - Phase 1: AG-D-09 (Doc13 §2.9)
    - Obligation: OBL-D-09.2-001
    - Objective: PO-D-09.2-001, SO-D-09.2-001

24. **Framework Anchors:**
    - CSF: ID.RA-01, ID.RA-04, ID.RA-05, GV.RM-06, GV.OV-02
    - PF: ID.RA-P3, ID.RA-P4, ID.RA-P5, GV.RM-P1, GV.MT-P1
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.7
    - SSDF: PW.1

---

### CR-D-09.4-001 — Processing and Breach Records
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to maintain records of
   processing activities and documentation for personal-data breaches. It
   operationalises OBL-D-09.4 for both TinyTask's controller activities and the
   processor activities performed for B2B customers.

   A RoPA provides the baseline needed to answer what data is processed, for whom
   where it flows, why it is retained, and which safeguards apply. Breach records
   complement that baseline by recording facts, effects, decisions, notifications
   and remedial action even when external notification is not required.

   Implement a versioned RoPA with controller and processor views, update it on
   processing change, and connect incident records to affected activities and systems.
   Retain decision evidence, recipients, clock starts, and corrective actions without
   copying unnecessary personal data into the compliance repository.



2. **Scope:** Controller and processor RoPA, data categories, purposes, recipients
   transfers, retention, safeguards, breach register, decisions, and remediation.

3. **Out of Scope:** Automated enterprise RoPA tooling, records for processing TinyTask
   does not perform, and incident notes containing unnecessary customer content.

4. **Source Article:** GDPR Art. 30 + Art. 33(5)
   (source clauses GDPR-C13, GDPR-C22).

5. **NIST CSF Anchors:** GV.PO-02, ID.AM-08, ID.RA-05, PR.DS-10, RS.MA-03.

6. **Verification Criteria:**

   - The RoPA covers TinyTask's controller and processor activities with all required fields.

   - A processing change sample shows the RoPA was updated and linked to the risk review.

   - Every security incident has a breach decision and, where applicable, notification evidence.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + DPO + Compliance Lead + Legal

9. **Status:** TODO

10. **Dependencies:** OBL-D-09.4-001, PO-D-09.4-001, CR-D-04.3-001
    CR-D-05.2-001, CR-D-06.3-001, CR-D-09.1-001, CR-D-10.2-001.

11. **Risk if not met:** H — TinyTask may be unable to demonstrate processing
    accountability or explain breach decisions to CNPD and customers.

12. **Affected Stakeholders:** Customers, data subjects, B2B controllers, DPO, CTO
    Compliance Lead, Legal, CNPD.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD + ENISA (periodic).

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C13 NI=3, GDPR-C22 NI=2;
    AVG=2.5 → bucket P1 ≥ 2.5 → MUST; AVG preserves SHOULD signal where MAX would round up.)*



19. **CSF Subcategories:** GV.PO-02 (cybersecurity processes/procedures enforced), ID.AM-08 (data inventories for risk mgmt (legacy - not in frozen list)), ID.RA-05 (threats/vulns inform risk-response decisions), PR.DS-10 (data managed per risk strategy (CIA)), RS.MA-03 (incidents categorised + prioritised)

20. **Privacy FW Subcategories:** ID.IM-P1 (systems/products/services that process data inventoried), ID.IM-P4 (data actions of systems/services inventoried), ID.IM-P6 (data elements within data actions inventoried), ID.IM-P8 (data processing mapped incl roles + interactions)

21. **Implementation Status (CSF):** NOT IMPLEMENTED (What's missing: operational RoPA maintenance)

22. **Implementation Status (Privacy):** NOT IMPLEMENTED (What missing: operational RoPA maintenance)

23. **Traceability:**
    - Legal: ** GDPR Art. 30 + Art. 33(5)
    - Phase 1: AG-D-09 (Doc13 §2.9)
    - Obligation: OBL-D-09.4-001
    - Objective: PO-D-09.4-001

24. **Framework Anchors:**
    - CSF: GV.PO-02, ID.AM-08, ID.RA-05, PR.DS-10, RS.MA-03
    - PF: ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.33
    - SSDF: PO.3

---

### CR-D-10.2-001 — Audit Logging and Traceability
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to log security-relevant
   events and preserve a traceable audit trail of access and administrative actions.
   It operationalises OBL-D-10.2 through inherited managed audit-trail logging plus application-level
   events that cloud-provider records cannot supply.

   Logs support detection, incident reconstruction, accountability, and conformity.
   They must be protected from alteration, time-aligned, access-controlled, and scoped
   to avoid becoming an unnecessary repository of customer content or secrets.

   Implement multi-region managed audit-trail logging, application audit events, protected managed object storage
   with Object Lock, alerting for logging failure, and documented retention. Define
   required event fields, correlate identities and tenant context, and test retrieval
   from the archive without granting broad operational write access.



2. **Scope:** managed hosting API activity, authentication, privilege and configuration changes
   security events, application audit records, timestamps, storage, access, and retention.

3. **Out of Scope:** Recording message or task bodies by default, an enterprise log
   analytics platform, and customer systems outside TinyTask's managed hosting boundary.

4. **Source Article:** CRA Art. 22 (source clause CRA-C14); related GDPR accountability:
   Art. 5(2) + Art. 30.

5. **NIST CSF Anchors:** DE.CM-01, GV.PO-02, ID.RA-04, PR.DS-01, PR.PS-04.

6. **Verification Criteria:**

   - managed audit-trail logging is enabled account-wide and writes a multi-region trail to protected storage.

   - Application tests emit required authentication, privilege, and administrative events.

   - Object Lock, access controls, retention, and a sampled archive retrieval pass review.

7. **Verification Method:** TEST

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-10.2-001, SO-D-10.2-001, BPR-D-10.2-001
    CR-D-01.4-001, CR-D-04.3-001, CR-D-09.4-001.

11. **Risk if not met:** H — TinyTask can miss attacks or be unable to reconstruct and
    evidence a security or personal-data incident.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, auditors
    CNPD, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses CRA-C14 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** DE.CM-01 (networks monitored for adverse events), GV.PO-02 (cybersecurity processes/procedures enforced), ID.RA-04 (impacts + likelihoods identified + prioritised), PR.DS-01 (backups created + protected + tested), PR.PS-04 (log records generated + available)

20. **Privacy FW Subcategories:** CT.DM-P9 (log records per policy (data minimisation)), CT.DM-P4 (data elements accessible for deletion)

21. **Implementation Status (CSF):** PARTIAL (What's missing: log review cadence & 7y audit store)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: ** CRA Art. 22 (source clause CRA-C14); related GDPR accountability:
    - Phase 1: AG-D-10 (Doc13 §2.10)
    - Obligation: OBL-D-10.2-001
    - Objective: SO-D-10.2-001

24. **Framework Anchors:**
    - CSF: DE.CM-01, GV.PO-02, ID.RA-04, PR.DS-01, PR.PS-04
    - PF: CT.DM-P9, CT.DM-P4
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.15
    - SSDF: PO.3

---

### CR-D-10.3-001 — Control Effectiveness Testing
Type: CONTROL — OBLIGATION (MUST, NI=3 (MUST))


1. **Description:** The implementation rule requires TinyTask to test the effectiveness
   of technical and organisational measures regularly. It operationalises OBL-D-10.3
   through a proportionate testing programme that combines automated checks, quarterly
   control review, and annual security assessment evidence.

   A configured control can drift, fail silently, or no longer address the relevant
   threat. Testing must therefore evaluate outcomes rather than merely confirm that a
   setting exists, and findings must feed risk assessment, remediation, and policy review.

   Implement a quarterly compliance checklist, automated CI and configuration tests
   an annual security test, finding ownership, retest evidence, and management sign-off.
   Cover privacy measures, product controls, provider evidence, and the CRA conformity
   assertions used for the supported release.



2. **Scope:** Automated security tests, configuration checks, quarterly reviews, annual
   assessment, findings, remediation, retest, management review, and conformity evidence.

3. **Out of Scope:** Continuous red-team operations, mandatory enterprise certification
   and testing customer infrastructure not operated by TinyTask.

4. **Source Article:** GDPR Art. 32(1)(d) + Art. 28(3)(h); CRA Art. 14 + Art. 21
   (source clauses GDPR-C19, CRA-C20).

5. **NIST CSF Anchors:** DE.AE-02, GV.OV-03, ID.RA-05, ID.IM-02, PR.PS-06.

6. **Verification Criteria:**

   - The quarterly checklist covers DPIA, RoPA, access, logging, backup, and supplier evidence.

   - Findings have severity, owner, corrective action, retest result, and closure approval.

   - The annual report records test coverage and management sign-off for CRA conformity evidence.

7. **Verification Method:** DEMONSTRATE

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-10.3-001, SO-D-10.3-001, BPR-D-10.3-001
    BPR-D-10.3-002, CR-D-09.2-001, CR-D-09.1-001, CR-D-10.2-001.

11. **Risk if not met:** H — Ineffective controls can remain undetected while TinyTask
    relies on them for GDPR accountability and CRA conformity.

12. **Affected Stakeholders:** Customers, data subjects, DPO, CTO, Lead Dev, auditors
    CNPD, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 3 — MUST
    *(source clauses GDPR-C19 NI=3, CRA-C20 NI=3;
    AVG=3.0 → bucket P1 ≥ 2.5 → MUST.)*



19. **CSF Subcategories:** DE.AE-02 (adverse events analysed to understand targets), GV.OV-03 (cyber performance evaluated + reviewed), ID.RA-05 (threats/vulns inform risk-response decisions), ID.IM-02 (improvement processes implemented across tiers), PR.PS-06 (secure SW dev integrated in SDLC)

20. **Privacy FW Subcategories:** ID.RA-P3 (problematic data actions identified), ID.RA-P5 (risk responses prioritised + implemented) (privacy strategy reviewed for requirements + risks)

21. **Implementation Status (CSF):** NOT IMPLEMENTED (What's missing: annual pen test & control test plan)

22. **Implementation Status (Privacy):** NOT IMPLEMENTED (What missing: annual pen test & control test plan)

23. **Traceability:**
    - Legal: ** GDPR Art. 32(1)(d) + Art. 28(3)(h); CRA Art. 14 + Art. 21
    - Phase 1: AG-D-10 (Doc13 §2.10)
    - Obligation: OBL-D-10.3-001
    - Objective: SO-D-10.3-001

24. **Framework Anchors:**
    - CSF: DE.AE-02, GV.OV-03, ID.RA-05, ID.IM-02, PR.PS-06
    - PF: ID.RA-P3, ID.RA-P5
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.5.35
    - SSDF: PW.7

---

## PARTE II — BEST-PRACTICE CONTROLS (16 BPR)

### BPR-D-01.1-001 — Use strong symmetric encryption for Data at Rest
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule standardises strong symmetric encryption as TinyTask's default
   encryption strength for data at rest. It translates ISO 27001 cryptography guidance
   into a concrete engineering baseline that supports, but does not replace
   CR-D-01.1-001.

   A named algorithm removes ambiguity from infrastructure reviews and prevents a
   provider default from drifting below the approved baseline. The control remains
    proportionate because TinyTask can use managed hosting encryption rather than operating
    a bespoke cryptographic service.

   Implement strong symmetric encryption through managed key custody-backed managed object storage, managed NoSQL, managed relational database, snapshots, backups, and
   log archives. Encode the setting in infrastructure-as-code, reject unencrypted writes
   and retain configuration evidence with the annual cryptography review.



2. **Scope:** Production storage, databases, snapshots, backups, release artifacts
   log archives, and infrastructure-as-code encryption settings.

3. **Out of Scope:** Customer-side cryptography, a dedicated HSM, custom cipher design
   and data that is never stored within the TinyTask service boundary.

4. **Source Article:** ISO 27001 A.8.24 — Use of cryptography.

5. **NIST CSF Anchors:** PR.DS-01, PR.DS-10, PR.PS-04.

6. **Verification Criteria:**

   - Infrastructure tests identify strong symmetric encryption or an approved managed key custody equivalent for every in-scope store.

   - A negative test confirms unencrypted object or snapshot creation is blocked or detected.

   - The annual cryptography record reconciles algorithms, stores, keys, and provider evidence.

7. **Verification Method:** TEST

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** CR-D-01.1-001, CR-D-01.3-001, BPR-D-01.2-001.

11. **Risk if not met:** M — Inconsistent encryption choices can weaken inherited
    protection and create avoidable storage exposure.

12. **Affected Stakeholders:** Customers, data subjects, CTO, Lead Dev, DPO, auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (ISO 27001 A.8.24); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** PR.DS-01 (CIA of data-at-rest protected), PR.DS-10 (CIA of data-in-use protected), PR.PS-04 (log records generated + available)

20. **Privacy FW Subcategories:** PR.DS-P1 (CIA of data-at-rest protected) (backups created + protected + maintained + tested) (resilience mechanisms for adverse situations)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / PR.DS-01, PR.DS-10, PR.PS-04)
    - Phase 1: AG-D-01 (Doc13 §2.1)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-01.1-001

24. **Framework Anchors:**
    - CSF: PR.DS-01, PR.DS-10, PR.PS-04
    - PF: PR.DS-P1
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-01.2-001 — Implement current transport cryptographic standard for All Networks
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule establishes current transport cryptographic standard as the preferred
   protocol for all TinyTask network communications. It applies NIST SC-8 transmission
   confidentiality and integrity guidance to the implementation of CR-D-01.2-001.

   A consistent protocol baseline reduces downgrade and weak-cipher exposure across
   customer ingress, service calls, and third-party APIs. Where a provider endpoint
   supports only a hardened modern transport cryptographic standard profile, the exception must be visible and reviewed
   rather than silently accepted.

   Implement current transport cryptographic standard at managed content delivery and supported origins, HTTPS-only redirects, managed
   certificates, outbound certificate validation, and automated endpoint scans. Record
   protocol exceptions and remove them when the relevant provider supports the baseline.



2. **Scope:** Public endpoints, managed content delivery, load balancers, service connections, managed hosting
   APIs, payment-processor calls, certificate management, and protocol configuration.

3. **Out of Scope:** Customer local networks, provider-internal paths not configurable
   by TinyTask, and mandatory mutual TLS for every internal call.

4. **Source Article:** documented control catalogue SC-8 — Transmission Confidentiality and Integrity.

5. **NIST CSF Anchors:** PR.DS-02, PR.IR-01, PR.PS-04.

6. **Verification Criteria:**

   - Endpoint scans show current transport cryptographic standard preferred and no obsolete protocol or weak cipher enabled.

   - Certificate renewal and hostname validation pass for every TinyTask-controlled endpoint.

   - Each modern transport cryptographic standard compatibility exception has a provider reason, owner, and review record.

7. **Verification Method:** TEST

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** CR-D-01.2-001, CR-D-01.3-001, BPR-D-01.1-001.

11. **Risk if not met:** M — Weak transport configuration increases interception and
    downgrade risk across customer and supplier connections.

12. **Affected Stakeholders:** Customers, data subjects, CTO, Lead Dev, DPO, auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (NIST SC-8); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** PR.DS-02 (CIA of data-in-transit protected), PR.IR-01 (networks protected from unauthorised access), PR.PS-04 (log records generated + available)

20. **Privacy FW Subcategories:** PR.DS-P2 (CIA of data-in-transit protected) (networks protected from unauthorised access)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / PR.DS-02, PR.IR-01, PR.PS-04)
    - Phase 1: AG-D-01 (Doc13 §2.1)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-01.2-001

24. **Framework Anchors:**
    - CSF: PR.DS-02, PR.IR-01, PR.PS-04
    - PF: PR.DS-P2, PR.PO-P7
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-02.1-001 — Conduct Quarterly Vulnerability Scans
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule requires a recorded vulnerability scan of
   the TinyTask application, dependencies, and deployable images at least quarterly.
   It applies OWASP ASVS V1 governance guidance and complements the per-build controls
   in CR-D-02.1-001.

   Build gates identify issues at change time, while a quarterly scan detects newly
   disclosed weaknesses in software that has not recently changed. The review creates
   a stable management checkpoint for coverage, exceptions, and overdue remediation.

   Run automated vulnerability scanner, dependency auditing, and an approved application scan against the current
   release; reconcile results with the SBOM; classify findings; assign owners; and
   retain the report and retest evidence. A critical finding enters the patch and
   incident decision paths immediately.



2. **Scope:** Current production release, dependencies, container images, exposed
   application surface, SBOM correlation, findings, remediation, and retest records.

3. **Out of Scope:** Destructive testing against customer data, an unrestricted bug
   bounty, and infrastructure the provider or customer does not permit TinyTask to scan.

4. **Source Article:** OWASP ASVS V1 — Architecture, Design and Threat Modeling.

5. **NIST CSF Anchors:** ID.RA-01, ID.RA-03, ID.RA-05, ID.IM-02, PR.PS-02.

6. **Verification Criteria:**

   - Four consecutive quarterly records show scans of the current release and dependency set.

   - Every finding has severity, affected artifact, owner, disposition, and retest status.

   - The report reconciles scanned components to the release SBOM and documents any gap.

7. **Verification Method:** DEMONSTRATE

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** CR-D-02.1-001, CR-D-02.2-001, CR-D-06.2-001
    BPR-D-07.2-001.

11. **Risk if not met:** M — Newly disclosed weaknesses can remain undetected between
    code changes and persist in a supported release.

12. **Affected Stakeholders:** Customers, CTO, Lead Dev, Procurement, DPO, auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (OWASP ASVS V1); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** ID.RA-01 (vulnerabilities identified + validated + recorded), ID.RA-03 (threats identified + recorded + prioritised), ID.RA-05 (threats/vulns inform risk-response decisions), ID.IM-02 (improvement processes implemented across tiers), PR.PS-02 (software maintained + replaced + removed)

20. **Privacy FW Subcategories:** ID.RA-P3 (problematic data actions identified), ID.RA-P5 (risk responses prioritised + implemented)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / ID.RA-01, ID.RA-03, ID.RA-05, ID.IM-02, PR.PS-02)
    - Phase 1: AG-D-02 (Doc13 §2.2)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-02.1-001

24. **Framework Anchors:**
    - CSF: ID.RA-01, ID.RA-03, ID.RA-05, ID.IM-02, PR.PS-02
    - PF: ID.RA-P3, ID.RA-P5
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-02.2-001 — Apply Critical Patches Within 72 Hours
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule establishes a maximum 72-hour remediation
   objective for critical patches once an applicable fix is available. It applies
   NIST SI-2 flaw-remediation guidance and provides a measurable operating target for
   CR-D-02.2-001.

   A fixed objective supports escalation and prevents a critical finding from waiting
   in a general backlog. The rule still requires technical validation: an unsafe patch
   must be handled through an approved exception, compensating control, and active
   review rather than installed blindly or ignored.

   Implement severity classification, automated ticket creation, managed automated patch pipeline or image
   rebuild deployment, controlled validation, and closure evidence. Start the internal
   clock when applicability and patch availability are confirmed, and escalate any
   predicted miss to the CTO.



2. **Scope:** Critical operating-system, container, dependency, and application patches;
   applicability decisions, deployment, exceptions, escalation, and retest evidence.

3. **Out of Scope:** Findings with no available remediation, patches for customer-owned
   systems, and lower-severity fixes governed by the broader vulnerability policy.

4. **Source Article:** documented control catalogue SI-2 — Flaw Remediation.

5. **NIST CSF Anchors:** ID.RA-01, PR.IR-03, PR.PS-01, PR.PS-02.

6. **Verification Criteria:**

   - Critical patch records show applicability decision, clock start, deployment, and validation.

   - Closure occurs within 72 hours or an approved exception identifies a compensating control.

   - A quarterly sample reconciles critical advisories, assets, tickets, and deployed versions.

7. **Verification Method:** TEST

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** CR-D-02.2-001, CR-D-02.1-001, BPR-D-02.1-001
    CR-D-06.2-001.

11. **Risk if not met:** H — A known critical flaw can remain exploitable during the
    period of highest public attacker awareness.

12. **Affected Stakeholders:** Customers, CTO, Lead Dev, Procurement, DPO, auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (NIST SI-2); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** ID.RA-01 (vulnerabilities identified + validated + recorded), PR.IR-03 (resilience mechanisms in adverse situations), PR.PS-01 (config mgmt practices established + applied), PR.PS-02 (software maintained + replaced + removed)

20. **Privacy FW Subcategories:** — (product-security deliverable; SSDF RV.2 anchored; no PF 1.0 scope)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** N/A — product-security deliverable (SSDF RV.2)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / ID.RA-01, PR.IR-03, PR.PS-01, PR.PS-02)
    - Phase 1: AG-D-02 (Doc13 §2.2)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-02.2-001

24. **Framework Anchors:**
    - CSF: ID.RA-01, PR.IR-03, PR.PS-01, PR.PS-02
    - PF: 
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-03.1-001 — Implement Role-Based Access Control
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule requires TinyTask to express application and
   administrative permissions through role-based access control. It applies ISO 27001
   access-management guidance and strengthens CR-D-03.1-001 and CR-D-03.3-001.

   RBAC makes the intended authorisation model reviewable and reduces ad hoc grants.
   At MICRO scale, a small role set is preferable to complex attribute policy, but each
   role still needs a defined purpose, permitted actions, tenant boundary, owner, and
   deprovisioning path.

   Implement managed identity custom claims or equivalent roles, enforce them server-side
   map cloud permissions to named operational roles, and maintain a concise RBAC matrix.
   Review assignments quarterly and test that lower-privilege roles cannot execute
   administrative or cross-tenant actions.



2. **Scope:** Customer, support, developer, administrator, service, and deployment roles;
   managed identity claims, server checks, IAM mapping, reviews, and deprovisioning.

3. **Out of Scope:** A full ABAC programme, permissions in customer-managed systems
   and unreviewed direct grants that bypass the documented role model.

4. **Source Article:** ISO 27001 A.9.2 — User access management.

5. **NIST CSF Anchors:** PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, ID.AM-01.

6. **Verification Criteria:**

   - The RBAC matrix defines each role, owner, allowed operation, and tenant boundary.

   - Negative tests prevent lower roles from performing admin and cross-tenant operations.

   - A quarterly assignment review removes stale users, claims, service accounts, and direct grants.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** CR-D-03.1-001, CR-D-03.3-001, BPR-D-03.2-001
    BPR-D-03.4-001.

11. **Risk if not met:** H — Ad hoc permissions can create hidden privilege and
    cross-tenant access paths.

12. **Affected Stakeholders:** Customers, data subjects, CTO, Lead Dev, DPO, auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (ISO 27001 A.9.2); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** PR.AA-01 (identities/credentials managed for users/svcs/HW), PR.AA-03 (users/services/HW authenticated), PR.AA-05 (access permissions managed (least privilege)), PR.AA-06 (access to assets limited to authorised), ID.AM-01 (hardware inventories maintained)

20. **Privacy FW Subcategories:** PR.AC-P1 (identities/credentials for users/svcs/HW managed), PR.AC-P6 (authentication commensurate with risk), PR.AC-P4 (least-privilege access); UNMAPPED_PF (ID.AM-01 hardware inventories — no PF 1.0 analogue)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, ID.AM-01)
    - Phase 1: AG-D-03 (Doc13 §2.3)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-03.1-001

24. **Framework Anchors:**
    - CSF: PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, ID.AM-01
    - PF: PR.AC-P1, PR.AC-P6, PR.AC-P4
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-03.2-001 — Enable FIDO2 for MFA
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule selects FIDO2 as the preferred phishing-
   resistant factor for TinyTask privileged accounts where the identity provider and
   account type support it. It applies NIST IA-2 guidance and strengthens the MFA
   requirement in CR-D-03.2-001.

   FIDO2 binds authentication to a legitimate origin and avoids reusable one-time
   secrets, reducing the risk of credential phishing and adversary-in-the-middle attacks.
   Because managed identity service capabilities and customer account types vary, the implementation
   must record supported coverage and use an approved fallback where FIDO2 is unavailable.

   Enable security keys or platform passkeys for CTO, Lead Dev, deployment, and support
   administrators; test enrolment and recovery; protect fallback factors; and review
   factor inventory quarterly. Do not allow a recovery process to become an easier
   bypass than the primary factor.



2. **Scope:** Privileged managed identity service and cloud accounts, FIDO2 security keys or passkeys
   enrolment, recovery, fallback controls, session enforcement, and factor reviews.

3. **Out of Scope:** Mandatory FIDO2 for every customer, unsupported provider accounts
   and customer identity configurations not administered by TinyTask.

4. **Source Article:** documented control catalogue IA-2 — Identification and Authentication.

5. **NIST CSF Anchors:** PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06.

6. **Verification Criteria:**

   - Every supported privileged account has an enrolled FIDO2 factor and named custodian.

   - Authentication tests reject a privileged session that lacks the required second factor.

   - Recovery and fallback tests require identity verification and generate an auditable event.

7. **Verification Method:** TEST

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** CR-D-03.2-001, CR-D-03.1-001, BPR-D-03.1-001.

11. **Risk if not met:** M — Privileged accounts remain more exposed to phishing and
    reusable-factor compromise.

12. **Affected Stakeholders:** CTO, Lead Dev, support administrators, customers, DPO
    auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (NIST IA-2); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** PR.AA-03 (users/services/HW authenticated), PR.AA-04 (identity assertions managed + protected), PR.AA-05 (access permissions managed (least privilege)), PR.AA-06 (access to assets limited to authorised)

20. **Privacy FW Subcategories:** PR.AC-P6 (authentication commensurate with risk), PR.AC-P4 (least-privilege access); UNMAPPED_PF (PR.AA-04 identity assertions protected + verified — no PF 1.0 subcategory; FIDO2 origin binding documented as §6.3 gap)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06)
    - Phase 1: AG-D-03 (Doc13 §2.3)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-03.2-001

24. **Framework Anchors:**
    - CSF: PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06
    - PF: PR.AC-P6, PR.AC-P4
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-03.4-001 — Harden Systems Using hardened-default baseline references
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule requires TinyTask to use applicable CIS
   Benchmarks as a repeatable hardening reference for cloud, operating-system, container
   and repository settings. It applies documented baseline control set and strengthens the secure-default
   implementation in CR-D-03.4-001.

   A benchmark provides a recognised starting point but must be tailored to the actual
   TinyTask architecture. Controls that are not applicable should be documented rather
   than marked complete, and provider-managed responsibilities should be separated from
   configurations TinyTask can directly change.

   Select benchmark profiles for managed hosting and deployed runtimes, encode relevant settings
   in infrastructure-as-code, scan for drift, and keep a concise exception register.
   Review failed checks by risk and correct insecure defaults before a release or
   production configuration change is approved.



2. **Scope:** managed hosting account and service configuration, operating systems, containers
   source repositories, benchmark scans, drift checks, and documented exceptions.

3. **Out of Scope:** Benchmarks for unused technologies, controls owned solely by a
   provider without a customer setting, and blind application of settings that break security.

4. **Source Article:** documented baseline control set — Secure Configuration of Enterprise Assets and Software.

5. **NIST CSF Anchors:** GV.PO-01, PR.PS-01, PR.PS-04, ID.IM-02.

6. **Verification Criteria:**

   - The baseline identifies applicable CIS profiles, selected checks, and responsibility boundaries.

   - A scan reports compliance status and maps each failed check to remediation or exception.

   - Infrastructure drift testing detects and routes an unauthorised hardening change.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** CR-D-03.4-001, CR-D-03.3-001, BPR-D-03.1-001
    CR-D-10.3-001.

11. **Risk if not met:** M — Configuration drift and permissive defaults can create
    preventable exposure across the service stack.

12. **Affected Stakeholders:** Customers, CTO, Lead Dev, DPO, managed hosting, auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (documented baseline control set); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** GV.PO-01 (cybersecurity policy established + enforced), PR.PS-01 (config mgmt practices established + applied), PR.PS-04 (log records generated + available), ID.IM-02 (improvement processes implemented across tiers)

20. **Privacy FW Subcategories:** CT.DP-P4 (selective collection/disclosure configurable), CT.PO-P4 (data lifecycle aligned with SDLC)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / GV.PO-01, PR.PS-01, PR.PS-04, ID.IM-02)
    - Phase 1: AG-D-03 (Doc13 §2.3)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-03.4-001

24. **Framework Anchors:**
    - CSF: GV.PO-01, PR.PS-01, PR.PS-04, ID.IM-02
    - PF: CT.DP-P4, CT.PO-P4
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-04.3-001 — Maintain an Incident Response Playbook
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule requires TinyTask to maintain one accessible
   approved incident response playbook. It applies ISO 27001 incident-planning guidance
   and provides the operational foundation for CR-D-04.1-001 through CR-D-04.4-001.

   During an incident, an eight-person team needs clear triggers, authority, contacts
   evidence steps, containment actions, and reporting decisions. The playbook must be
   usable under pressure and distinguish the GDPR, CRA, processor, and customer routes
   without duplicating the underlying event record.

   Document severity levels, roles, call tree, four-hour containment actions, 24-hour
   max-SLA routing, evidence preservation, recovery, communications, and post-incident
   review. Keep offline access to essential contacts and update the playbook after each
   exercise, incident, or material provider change.



2. **Scope:** Detection, triage, severity, roles, contacts, containment, evidence
   notification, recovery, communications, review, and offline access.

3. **Out of Scope:** A separate playbook platform, automated orchestration, and
   incident procedures for customer environments not operated by TinyTask.

4. **Source Article:** ISO 27001 A.5.24 — Information security incident management planning and preparation.

5. **NIST CSF Anchors:** RS.MA-01, RS.MA-02, RS.MA-03, RS.MA-01, RS.CO-02
   RC.RP-01.

6. **Verification Criteria:**

   - The approved playbook names owners, severity triggers, actions, contacts, and reporting routes.

   - An offline copy of critical contacts and first-response actions is accessible to responders.

   - Each exercise or incident produces a tracked playbook update or a documented no-change decision.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + DPO + Compliance Lead

9. **Status:** TODO

10. **Dependencies:** CR-D-04.1-001, CR-D-04.2-001, CR-D-04.3-001
    CR-D-04.4-001, BPR-D-04.3-002.

11. **Risk if not met:** H — Responders can lose critical time, evidence, or reporting
    accuracy during a high-pressure incident.

12. **Affected Stakeholders:** Customers, data subjects, B2B controllers, CTO, DPO
    Compliance Lead, CNPD, ENISA, PT CSIRT (CNCS).

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (ISO 27001 A.5.24); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** RS.MA-01 (incident response plan executed), RS.MA-02 (incidents triaged + validated), RS.MA-03 (incidents categorised + prioritised), RS.MA-01 (incident response plan execution (legacy v1.1)), RS.CO-02 (events reported internally per criteria), RC.RP-01 (recovery plan executed + verified)

20. **Privacy FW Subcategories:** PR.PO-P7 (incident response + recovery plans maintained), CT.DM-P10 (technical measures tested + assessed)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / RS.MA-01, RS.MA-02, RS.MA-03, RS.MA-01, RS.CO-02, RC.RP-01)
    - Phase 1: AG-D-04 (Doc13 §2.4)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-04.3-001

24. **Framework Anchors:**
    - CSF: RS.MA-01, RS.MA-02, RS.MA-03, RS.MA-01, RS.CO-02, RC.RP-01
    - PF: PR.PO-P7, CT.DM-P10
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-04.3-002 — Conduct Tabletop Exercises Quarterly
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule requires TinyTask to conduct a quarterly
   tabletop exercise using the current incident response playbook. It applies NIST CSF
   2.0 RS.MA-01 and verifies that written roles, decisions, communications, and reporting
   routes can be executed by the actual team.

   A tabletop exposes assumptions without disrupting production. Scenarios should vary
   across personal-data breach, exploited vulnerability, provider outage, credential
   compromise, and compound events so the team tests both single-regulation and dual-
   notification paths.

   Define objectives and injects, appoint a facilitator, record decisions and clock
   times, test contacts and templates, and issue corrective actions. At least one
   exercise should validate the 24-hour max-SLA route and one should validate recovery
   and customer-controller communications.



2. **Scope:** Quarterly scenarios, participants, injects, decisions, clock evidence
   communications, notification templates, recovery, findings, and corrective actions.

3. **Out of Scope:** Unannounced destructive production simulations, full red-team
   exercises, and scenarios unrelated to TinyTask's architecture or regulatory roles.

4. **Source Article:** NIST CSF 2.0 RS.MA-01 — Incident response plan execution and maintenance.

5. **NIST CSF Anchors:** RS.MA-01, RS.MA-01, RS.MA-02, RS.CO-02, RS.MA-01
   RC.RP-01.

6. **Verification Criteria:**

   - Four quarterly exercise records identify scenario, participants, objectives, and decisions.

   - A compound-event exercise demonstrates CNPD and ENISA routing from one event record.

   - Every exercise finding has an owner, corrective action, retest, and closure decision.

7. **Verification Method:** DEMONSTRATE

8. **Owner:** CTO + DPO + Compliance Lead

9. **Status:** TODO

10. **Dependencies:** BPR-D-04.3-001, CR-D-04.3-001, CR-D-04.2-001
    CR-D-04.4-001.

11. **Risk if not met:** M — Untested procedures may fail at the first real incident
    especially where several notification paths activate together.

12. **Affected Stakeholders:** Customers, B2B controllers, CTO, DPO, Compliance Lead
    CNPD, ENISA, PT CSIRT (CNCS), auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (NIST CSF2 RS.MA-01); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** RS.MA-01 (incident response plan execution (legacy v1.1)), RS.MA-01 (incident response plan executed), RS.MA-02 (incidents triaged + validated), RS.CO-02 (events reported internally per criteria), RS.MA-01 (coordination with stakeholders per criteria), RC.RP-01 (recovery plan executed + verified)

20. **Privacy FW Subcategories:** PR.PO-P7 (incident response + recovery plans maintained), CT.DM-P10 (technical measures tested + assessed)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / RS.MA-01, RS.MA-01, RS.MA-02, RS.CO-02, RS.MA-01, RC.RP-01)
    - Phase 1: AG-D-04 (Doc13 §2.4)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-04.3-002

24. **Framework Anchors:**
    - CSF: RS.MA-01, RS.MA-01, RS.MA-02, RS.CO-02, RS.MA-01, RC.RP-01
    - PF: PR.PO-P7, CT.DM-P10
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-05.3-001 — Use documented media sanitization standard for Media Sanitisation
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule requires TinyTask to use the documented media sanitization standard
   sanitisation model when storage media or provider-managed storage is released
   repurposed, or retired. It strengthens the logical erasure controls in
   CR-D-05.3-001 with a recognised disposal decision framework.

   In a cloud SaaS, TinyTask does not usually handle physical disks. The practical
   control is therefore to classify the medium and custody boundary, use cryptographic
   erase or provider sanitisation where appropriate, and retain the supplier evidence
   that supports an inherited physical-disposal claim.

   Document Clear, Purge, or Destroy decisions for relevant assets, verify encryption-key
   disposal and logical deletion, and retain managed hosting or other provider sanitisation evidence.
   Apply direct physical destruction only to company-owned removable media that cannot
   be securely cleared or purged.



2. **Scope:** Cloud storage decommissioning, encryption-key disposal, company-owned
   removable media, provider evidence, asset records, and sanitisation decisions.

3. **Out of Scope:** Physical destruction of provider-owned media by TinyTask, customer
   devices, and routine application deletion already covered by CR-D-05.3-001.

4. **Source Article:** documented media sanitization standard — Guidelines for Media Sanitization.

5. **NIST CSF Anchors:** PR.DS-10, PR.DS-10, GV.SC-04, ID.AM-08.

6. **Verification Criteria:**

   - The sanitisation procedure maps each relevant asset type to Clear, Purge, or Destroy.

   - A decommissioned cloud resource has deletion, key-disposal, and provider-boundary evidence.

   - Any company-owned removable media has an asset record and witnessed sanitisation result.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + DPO

9. **Status:** TODO

10. **Dependencies:** CR-D-05.3-001, CR-D-05.2-001, CR-D-01.3-001
    CR-D-06.1-001.

11. **Risk if not met:** M — Retired storage can retain recoverable personal data or
    unsupported assumptions about provider disposal.

12. **Affected Stakeholders:** Customers, data subjects, CTO, DPO, managed hosting, auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (documented media sanitization standard); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** PR.DS-10 (CIA of data-in-use protected), PR.DS-10 (data managed per risk strategy (CIA)), GV.SC-04 (suppliers routinely assessed (audits/tests)), ID.AM-08 (data inventories for risk mgmt (legacy - not in frozen list))

20. **Privacy FW Subcategories:** CT.DM-P4 (data elements accessible for deletion), CT.DM-P5 (data destroyed according to policy)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** NOT IMPLEMENTED (What missing: restriction flag workflow)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / PR.DS-10, PR.DS-10, GV.SC-04, ID.AM-08)
    - Phase 1: AG-D-05 (Doc13 §2.5)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-05.3-001

24. **Framework Anchors:**
    - CSF: PR.DS-10, PR.DS-10, GV.SC-04, ID.AM-08
    - PF: CT.DM-P4, CT.DM-P5
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-07.1-001 — Follow NIST SSDF Secure Development
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule requires TinyTask to use the NIST Secure
   Software Development Framework as the organising baseline for product-security
   practices. It applies SSDF PO.5.1 and gives CR-D-07.1-001 a recognised structure
   without requiring a large formal development programme.

   The SSDF connects preparation, software protection, secure production, and
   vulnerability response. For TinyTask, a concise practice map helps ensure that
   security ownership, tooling, release evidence, and supplier dependencies are managed
   as one lifecycle rather than isolated checks.

   Map applicable SSDF practices to the existing feature checklist, protected repository
   CI gates, SBOM, release approval, and vulnerability response process. Record practices
   inherited from managed source control, managed hosting, and managed identity service separately from controls TinyTask operates
   then review the map after material workflow changes.



2. **Scope:** Development policy, roles, repository protection, design review, coding
   CI/CD, dependencies, release evidence, vulnerability response, and provider inheritance.

3. **Out of Scope:** Formal SSDF certification, practices unrelated to TinyTask's product
   and duplicate controls where a documented provider boundary supplies the outcome.

4. **Source Article:** NIST SSDF PO.5.1 — Implement and Maintain Secure Environments for Software Development.

5. **NIST CSF Anchors:** GV.PO-02, GV.RR-02, ID.RA-01, PR.PS-01, PR.PS-02
   PR.PS-06.

6. **Verification Criteria:**

   - The SSDF map assigns each applicable practice to a TinyTask control, owner, and evidence source.

   - A release sample traces design, code, dependency, CI, approval, and response evidence.

   - Provider-inherited practices identify the service, responsibility boundary, and current assurance record.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** CR-D-07.1-001, CR-D-02.1-001, CR-D-06.2-001
    BPR-D-07.2-001.

11. **Risk if not met:** M — Secure-development activities can become fragmented and
    omit ownership or lifecycle coverage.

12. **Affected Stakeholders:** Customers, CTO, Lead Dev, DevOps, DPO, suppliers, auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (NIST SSDF PO.5.1); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** GV.PO-02 (cybersecurity processes/procedures enforced), GV.RR-02 (roles/responsibilities established + enforced), ID.RA-01 (vulnerabilities identified + validated + recorded), PR.PS-01 (config mgmt practices established + applied), PR.PS-02 (software maintained + replaced + removed), PR.PS-06 (secure SW dev integrated in SDLC)

20. **Privacy FW Subcategories:** GV.PO-P2 (privacy values in SDLC processes established), CT.PO-P4 (data lifecycle aligned with SDLC)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / GV.PO-02, GV.RR-02, ID.RA-01, PR.PS-01, PR.PS-02, PR.PS-06)
    - Phase 1: AG-D-07 (Doc13 §2.7)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-07.1-001

24. **Framework Anchors:**
    - CSF: GV.PO-02, GV.RR-02, ID.RA-01, PR.PS-01, PR.PS-02, PR.PS-06
    - PF: GV.PO-P2, CT.PO-P4
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-07.2-001 — Conduct SAST and DAST in CI/CD
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule requires TinyTask to run static and dynamic
   application security testing as part of the delivery workflow. It applies OWASP
   ASVS V3 session-management guidance within a broader application-test baseline and
   complements CR-D-02.1-001 and CR-D-07.1-001.

   SAST identifies risky code patterns before merge, while DAST evaluates the behaviour
   of a deployed test environment. Together they provide coverage that dependency
   scanning alone cannot supply, particularly around authentication, sessions, input
   validation, and access-control behaviour.

   Run SAST on every pull request, execute a scoped authenticated DAST suite against a
   non-production environment, block critical findings, and retain results with the
   release. Triage false positives explicitly and require retest evidence before a
   security finding is closed.



2. **Scope:** In-house source, pull requests, test deployments, authentication and
   session paths, input validation, findings, exceptions, release gates, and retests.

3. **Out of Scope:** Destructive DAST against production customer data, unrestricted
   scanning of provider services, and treating dependency audit as a substitute for SAST.

4. **Source Article:** OWASP ASVS V3 — Session Management Verification Requirements.

5. **NIST CSF Anchors:** ID.RA-04, ID.RA-05, PR.PS-01, PR.PS-02, PR.PS-06.

6. **Verification Criteria:**

   - Every pull request runs SAST and blocks unresolved critical findings from merge.

   - The release workflow records a scoped DAST result for the current test deployment.

   - Closed findings include disposition, approval where excepted, and successful retest evidence.

7. **Verification Method:** DEMONSTRATE

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** CR-D-07.1-001, CR-D-02.1-001, BPR-D-02.1-001
    BPR-D-07.1-001, CR-D-10.3-001.

11. **Risk if not met:** H — First-party code and runtime security defects can pass
    dependency-only checks and reach customers.

12. **Affected Stakeholders:** Customers, data subjects, CTO, Lead Dev, DevOps, DPO
    auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (OWASP ASVS V3); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** ID.RA-04 (impacts + likelihoods identified + prioritised), ID.RA-05 (threats/vulns inform risk-response decisions), PR.PS-01 (config mgmt practices established + applied), PR.PS-02 (software maintained + replaced + removed), PR.PS-06 (secure SW dev integrated in SDLC)

20. **Privacy FW Subcategories:** ID.RA-P4 (likelihoods + impacts prioritise risk), ID.RA-P5 (risk responses prioritised + implemented)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / ID.RA-04, ID.RA-05, PR.PS-01, PR.PS-02, PR.PS-06)
    - Phase 1: AG-D-07 (Doc13 §2.7)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-07.2-001

24. **Framework Anchors:**
    - CSF: ID.RA-04, ID.RA-05, PR.PS-01, PR.PS-02, PR.PS-06
    - PF: ID.RA-P4, ID.RA-P5
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-09.1-001 — Establish an ISMS per ISO 27001
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule requires TinyTask to organise its security
   governance as a proportionate information security management system aligned with
   ISO 27001. It applies A.5.1 policy guidance and strengthens the documented control
   architecture in CR-D-09.1-001.

   An ISMS at MICRO scale is a coherent management cycle, not necessarily a certification
   project. Scope, risks, policies, owners, evidence, findings, and management decisions
   should connect so that security and compliance can be reviewed across the business
   technical, risk, and regulatory perspectives.

   Define the TinyTask ISMS scope, policy hierarchy, risk and control register, evidence
   index, review meeting, internal audit, and corrective-action process. Reuse the GDPR
   and CRA documentation repository and record any ISO control that is not applicable
   with a reason rather than creating artificial evidence.



2. **Scope:** ISMS scope, policies, risks, controls, owners, evidence, internal review
   corrective actions, supplier assurance, and management decisions.

3. **Out of Scope:** Mandatory ISO 27001 certification, an enterprise GRC platform
   and controls unrelated to the defined TinyTask service and organisation boundary.

4. **Source Article:** ISO 27001 A.5.1 — Policies for information security.

5. **NIST CSF Anchors:** GV.PO-01, GV.PO-02, GV.RM-01, GV.OV-01, GV.OV-03.

6. **Verification Criteria:**

   - The approved ISMS scope and policy hierarchy cover the TinyTask service and organisation.

   - Risks, controls, owners, and evidence are linked in a maintained register.

   - An annual internal review records findings, corrective actions, and management decisions.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + DPO + Compliance Lead + Legal

9. **Status:** TODO

10. **Dependencies:** CR-D-09.1-001, CR-D-09.2-001, CR-D-09.4-001
    CR-D-10.3-001.

11. **Risk if not met:** M — Governance can remain document-centric and fail to connect
    risk, control operation, evidence, and corrective action.

12. **Affected Stakeholders:** CEO, customers, CTO, DPO, Compliance Lead, Legal
    suppliers, auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (ISO 27001 A.5.1); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** GV.PO-01 (cybersecurity policy established + enforced), GV.PO-02 (cybersecurity processes/procedures enforced), GV.RM-01 (risk mgmt objectives established + agreed), GV.OV-01 (strategy outcomes reviewed + adjusted), GV.OV-03 (cyber performance evaluated + reviewed)

20. **Privacy FW Subcategories:** GV.PO-P1 (privacy values + policies established + enforced), GV.RM-P1 (privacy risk mgmt objectives established) (privacy strategy outcomes reviewed + adjusted)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** NOT IMPLEMENTED (What missing: role-specific privacy training)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / GV.PO-01, GV.PO-02, GV.RM-01, GV.OV-01, GV.OV-03)
    - Phase 1: AG-D-09 (Doc13 §2.9)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-09.1-001

24. **Framework Anchors:**
    - CSF: GV.PO-01, GV.PO-02, GV.RM-01, GV.OV-01, GV.OV-03
    - PF: GV.PO-P1, GV.RM-P1
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-10.2-001 — Retain Logs for a Minimum of 12 Months
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule establishes a twelve-month minimum retention
   floor for security-relevant logs. It applies ISO 27001 A.8.16 monitoring guidance
   and complements the traceability requirements in CR-D-10.2-001.

   Retention must be long enough to investigate delayed discovery, establish patterns
   and support assurance review. The twelve-month floor does not shorten a longer
   approved TinyTask period; audit records assigned seven-year retention remain governed
   by that more stringent business and accountability rule.

   Classify log types, apply lifecycle rules, protect archives with encryption and
   Object Lock where appropriate, and monitor ingestion or retention failure. Test that
   authorised responders can retrieve a historical event while ordinary operators
   cannot alter the archive.



2. **Scope:** managed audit-trail logging, authentication, privilege, configuration, application audit
   security alert, retention policy, archive protection, retrieval, and disposal.

3. **Out of Scope:** Customer content in logs, indefinite retention without a purpose
   and transient debug output that is not approved as security evidence.

4. **Source Article:** ISO 27001 A.8.16 — Monitoring activities.

5. **NIST CSF Anchors:** DE.CM-01, DE.AE-02, GV.PO-02, PR.DS-01, PR.PS-04.

6. **Verification Criteria:**

   - Lifecycle configuration retains every security-log class for at least twelve months.

   - A sampled event older than twelve months is retrievable where a longer approved period applies.

   - Archive access and Object Lock tests prevent unauthorised alteration or premature deletion.

7. **Verification Method:** INSPECT

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** CR-D-10.2-001, CR-D-01.4-001, CR-D-05.2-001
    CR-D-04.3-001.

11. **Risk if not met:** H — Delayed incidents may become impossible to reconstruct or
    evidence because the relevant audit trail has expired.

12. **Affected Stakeholders:** Customers, DPO, CTO, Lead Dev, incident responders
    auditors, CNPD, ENISA.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (ISO 27001 A.8.16); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** DE.CM-01 (networks monitored for adverse events), DE.AE-02 (adverse events analysed to understand targets), GV.PO-02 (cybersecurity processes/procedures enforced), PR.DS-01 (backups created + protected + tested), PR.PS-04 (log records generated + available)

20. **Privacy FW Subcategories:** CT.DM-P9 (log records per policy (data minimisation)), CT.DM-P4 (data elements accessible for deletion)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / DE.CM-01, DE.AE-02, GV.PO-02, PR.DS-01, PR.PS-04)
    - Phase 1: AG-D-10 (Doc13 §2.10)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-10.2-001

24. **Framework Anchors:**
    - CSF: DE.CM-01, DE.AE-02, GV.PO-02, PR.DS-01, PR.PS-04
    - PF: CT.DM-P9, CT.DM-P4
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-10.3-001 — Conduct Annual Penetration Testing
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule requires an annual penetration test of the
   TinyTask application and relevant cloud boundary. It applies NIST CA-2 assessment
   guidance and supplements automated and quarterly testing under CR-D-10.3-001.

   Penetration testing evaluates chained weaknesses and attacker behaviour that isolated
   scanners may miss. The assessment must be authorised, scoped to protect customer
   data, informed by architecture and recent threats, and followed by remediation and
   retesting rather than treated as a one-time report.

   Define the web, API, authentication, tenant-isolation, and cloud scope; provide test
   accounts in a controlled environment; retain the method and findings; assign owners;
   and verify closure of high-severity issues. Record any excluded asset and its
   alternative assurance evidence.



2. **Scope:** Web and API attack surface, authentication, authorisation, tenant isolation
   cloud configuration, test evidence, findings, remediation, and retest.

3. **Out of Scope:** Destructive production testing, denial-of-service against customers
   social engineering without explicit approval, and provider infrastructure outside permission.

4. **Source Article:** documented control catalogue CA-2 — Control Assessments.

5. **NIST CSF Anchors:** GV.OV-03, ID.RA-01, ID.RA-04, ID.RA-05, ID.IM-02.

6. **Verification Criteria:**

   - A report from the previous twelve months documents approved scope, method, and limitations.

   - Every high or critical finding has an owner, corrective action, and verified retest result.

   - Scope includes authentication, tenant isolation, APIs, and relevant cloud misconfiguration.

7. **Verification Method:** DEMONSTRATE

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** CR-D-10.3-001, BPR-D-10.3-002, BPR-D-07.2-001
    CR-D-09.2-001.

11. **Risk if not met:** H — Chained or business-logic weaknesses can remain invisible
    to routine automated checks.

12. **Affected Stakeholders:** Customers, data subjects, CTO, Lead Dev, DPO, test team
    auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (NIST CA-2); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** GV.OV-03 (cyber performance evaluated + reviewed), ID.RA-01 (vulnerabilities identified + validated + recorded), ID.RA-04 (impacts + likelihoods identified + prioritised), ID.RA-05 (threats/vulns inform risk-response decisions), ID.IM-02 (improvement processes implemented across tiers)

20. **Privacy FW Subcategories:** ID.RA-P3 (problematic data actions identified), ID.RA-P5 (risk responses prioritised + implemented) (privacy performance measured + reviewed)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / GV.OV-03, ID.RA-01, ID.RA-04, ID.RA-05, ID.IM-02)
    - Phase 1: AG-D-10 (Doc13 §2.10)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-10.3-001

24. **Framework Anchors:**
    - CSF: GV.OV-03, ID.RA-01, ID.RA-04, ID.RA-05, ID.IM-02
    - PF: ID.RA-P3, ID.RA-P5
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

### BPR-D-10.3-002 — Use the OWASP Testing Guide for Assessments
Type: CONTROL — BEST-PRACTICE (SHOULD, NI=2.0)


1. **Description:** This best-practice rule requires TinyTask security assessments to
   use the OWASP Web Security Testing Guide as a documented test catalogue. It provides
   consistent web and API coverage for CR-D-10.3-001 and the annual assessment in
   BPR-D-10.3-001.

   A guide-based method improves repeatability and makes omissions visible. The tester
   can tailor cases to TinyTask's architecture, but excluded categories must be marked
   not applicable with a reason rather than silently absent from the final report.

   Create a test matrix for information gathering, configuration, identity, authentication
   authorisation, sessions, input validation, error handling, cryptography, business logic
   client-side behaviour, and APIs. Link each executed case to evidence, finding, or pass
   result and retain the matrix with the assessment record.



2. **Scope:** Web and API assessment planning, OWASP test categories, applicability
   evidence, results, findings, retest, and report traceability.

3. **Out of Scope:** Blind execution of irrelevant tests, destructive production cases
   mobile testing where no mobile client exists, and supplier systems outside authorisation.

4. **Source Article:** OWASP Web Security Testing Guide — current stable release.

5. **NIST CSF Anchors:** GV.OV-03, ID.RA-01, ID.RA-04, ID.RA-05, PR.PS-06.

6. **Verification Criteria:**

   - The assessment matrix covers each applicable OWASP testing category with a result.

   - Every excluded category has a documented architecture or scope rationale.

   - Findings link to test evidence, severity, owner, corrective action, and retest result.

7. **Verification Method:** DEMONSTRATE

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** CR-D-10.3-001, BPR-D-10.3-001, BPR-D-07.2-001
    CR-D-03.3-001.

11. **Risk if not met:** M — Assessments can vary by tester and omit important web
    API, authentication, or business-logic coverage.

12. **Affected Stakeholders:** Customers, data subjects, CTO, Lead Dev, DPO, test team
    auditors.

14. **Implementation Priority:** HIGH

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only.

16. **External Auditor (Case_01):** Documented third-party security attestation + documented control standard

17. **Supervisory Body (Case_01):** CNPD + ENISA + PT CSIRT (CNCS)

18. **Normative Intensity:** 2 — SHOULD
    *(framework-derived (OWASP Testing Guide); per Bloco B policy all 16 Case_01 BPR formalised as NI 2 SHOULD unless mapping to a recommended reference. No MAX(NI) applied — framework intent is SHOULD.)*



19. **CSF Subcategories:** GV.OV-03 (cyber performance evaluated + reviewed), ID.RA-01 (vulnerabilities identified + validated + recorded), ID.RA-04 (impacts + likelihoods identified + prioritised), ID.RA-05 (threats/vulns inform risk-response decisions), PR.PS-06 (secure SW dev integrated in SDLC)

20. **Privacy FW Subcategories:** ID.RA-P3 (problematic data actions identified), ID.RA-P5 (risk responses prioritised + implemented) (privacy performance measured + reviewed)

21. **Implementation Status (CSF):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

22. **Implementation Status (Privacy):** PARTIAL (What's missing: operational evidence verification & automated review cadence)

23. **Traceability:**
    - Legal: N/A — Best Practice Rule (derived from A.8.24 / GV.OV-03, ID.RA-01, ID.RA-04, ID.RA-05, PR.PS-06)
    - Phase 1: AG-D-10 (Doc13 §2.10)
    - Obligation: N/A — Best Practice Rule (derived from framework)
    - Objective: SO--D-10.3-002

24. **Framework Anchors:**
    - CSF: GV.OV-03, ID.RA-01, ID.RA-04, ID.RA-05, PR.PS-06
    - PF: ID.RA-P3, ID.RA-P5
    - AI RMF: N/A (non-AI scope)
    - ISO 27001: A.8.24
    - SSDF: -

---

## ANEXO A — CONTROL INDEX BY NIST CSF 2.0 FUNCTION

| CSF Function | Subcategory | Control ID | Type | Implementation Status |
|--------------|-------------|------------|------|-----------------------|
| GV | GV.OV-01 | CR-D-01.3-001 | OBLIGATION | ** |
| GV | GV.RM-04 | CR-D-01.3-001 | OBLIGATION | ** |
| GV | GV.OV-02 | CR-D-02.1-001 | OBLIGATION | ** |
| GV | GV.OV-02 | CR-D-02.2-001 | OBLIGATION | ** |
| GV | GV.PO-01 | CR-D-02.3-001 | OBLIGATION | ** |
| GV | GV.SC-04 | CR-D-02.3-001 | OBLIGATION | ** |
| GV | GV.PO-01 | CR-D-03.4-001 | OBLIGATION | ** |
| GV | GV.SC-03 | CR-D-03.4-001 | OBLIGATION | ** |
| GV | GV.OC-03 | CR-D-05.1-001 | OBLIGATION | ** |
| GV | GV.PO-01 | CR-D-05.1-001 | OBLIGATION | ** |
| GV | GV.OC-04 | CR-D-05.2-001 | OBLIGATION | ** |
| GV | GV.OV-02 | CR-D-05.2-001 | OBLIGATION | ** |
| GV | GV.PO-02 | CR-D-05.2-001 | OBLIGATION | ** |
| GV | GV.SC-04 | CR-D-05.3-001 | OBLIGATION | ** |
| GV | GV.SC-01 | CR-D-06.1-001 | OBLIGATION | ** |
| GV | GV.SC-02 | CR-D-06.1-001 | OBLIGATION | ** |
| GV | GV.SC-03 | CR-D-06.1-001 | OBLIGATION | ** |
| GV | GV.SC-04 | CR-D-06.1-001 | OBLIGATION | ** |
| GV | GV.SC-02 | CR-D-06.2-001 | OBLIGATION | ** |
| GV | GV.SC-03 | CR-D-06.2-001 | OBLIGATION | ** |
| GV | GV.OC-03 | CR-D-06.3-001 | OBLIGATION | ** |
| GV | GV.SC-02 | CR-D-06.3-001 | OBLIGATION | ** |
| GV | GV.SC-03 | CR-D-06.3-001 | OBLIGATION | ** |
| GV | GV.SC-04 | CR-D-06.3-001 | OBLIGATION | ** |
| GV | GV.PO-02 | CR-D-07.1-001 | OBLIGATION | ** |
| GV | GV.RR-02 | CR-D-08.2-001 | OBLIGATION | ** |
| GV | GV.RR-04 | CR-D-08.2-001 | OBLIGATION | ** |
| GV | GV.SC-03 | CR-D-08.2-001 | OBLIGATION | ** |
| GV | GV.PO-01 | CR-D-09.1-001 | OBLIGATION | ** |
| GV | GV.PO-02 | CR-D-09.1-001 | OBLIGATION | ** |
| GV | GV.RM-04 | CR-D-09.1-001 | OBLIGATION | ** |
| GV | GV.RR-02 | CR-D-09.1-001 | OBLIGATION | ** |
| GV | GV.OV-01 | CR-D-09.1-001 | OBLIGATION | ** |
| GV | GV.RM-06 | CR-D-09.2-001 | OBLIGATION | ** |
| GV | GV.OV-02 | CR-D-09.2-001 | OBLIGATION | ** |
| GV | GV.PO-02 | CR-D-09.4-001 | OBLIGATION | ** |
| GV | GV.PO-02 | CR-D-10.2-001 | OBLIGATION | ** |
| GV | GV.OV-03 | CR-D-10.3-001 | OBLIGATION | ** |
| GV | GV.PO-01 | BPR-D-03.4-001 | BEST-PRACTICE | ** |
| GV | GV.SC-04 | BPR-D-05.3-001 | BEST-PRACTICE | ** |
| GV | GV.PO-02 | BPR-D-07.1-001 | BEST-PRACTICE | ** |
| GV | GV.RR-02 | BPR-D-07.1-001 | BEST-PRACTICE | ** |
| GV | GV.PO-01 | BPR-D-09.1-001 | BEST-PRACTICE | ** |
| GV | GV.PO-02 | BPR-D-09.1-001 | BEST-PRACTICE | ** |
| GV | GV.RM-01 | BPR-D-09.1-001 | BEST-PRACTICE | ** |
| GV | GV.OV-01 | BPR-D-09.1-001 | BEST-PRACTICE | ** |
| GV | GV.OV-03 | BPR-D-09.1-001 | BEST-PRACTICE | ** |
| GV | GV.PO-02 | BPR-D-10.2-001 | BEST-PRACTICE | ** |
| GV | GV.OV-03 | BPR-D-10.3-001 | BEST-PRACTICE | ** |
| GV | GV.OV-03 | BPR-D-10.3-002 | BEST-PRACTICE | ** |
| ID | ID.AM-02 | CR-D-02.1-001 | OBLIGATION | ** |
| ID | ID.IM-02 | CR-D-02.1-001 | OBLIGATION | ** |
| ID | ID.RA-01 | CR-D-02.1-001 | OBLIGATION | ** |
| ID | ID.RA-03 | CR-D-02.1-001 | OBLIGATION | ** |
| ID | ID.RA-05 | CR-D-02.1-001 | OBLIGATION | ** |
| ID | ID.RA-01 | CR-D-02.2-001 | OBLIGATION | ** |
| ID | ID.RA-01 | CR-D-02.3-001 | OBLIGATION | ** |
| ID | ID.AM-01 | CR-D-03.1-001 | OBLIGATION | ** |
| ID | ID.AM-01 | CR-D-03.3-001 | OBLIGATION | ** |
| ID | ID.AM-02 | CR-D-03.3-001 | OBLIGATION | ** |
| ID | ID.RA-04 | CR-D-04.1-001 | OBLIGATION | ** |
| ID | ID.AM-03 | CR-D-05.1-001 | OBLIGATION | ** |
| ID | ID.AM-03 | CR-D-05.2-001 | OBLIGATION | ** |
| ID | ID.AM-04 | CR-D-06.1-001 | OBLIGATION | ** |
| ID | ID.RA-02 | CR-D-06.1-001 | OBLIGATION | ** |
| ID | ID.AM-02 | CR-D-06.2-001 | OBLIGATION | ** |
| ID | ID.RA-01 | CR-D-06.2-001 | OBLIGATION | ** |
| ID | ID.RA-01 | CR-D-07.1-001 | OBLIGATION | ** |
| ID | ID.RA-01 | CR-D-09.2-001 | OBLIGATION | ** |
| ID | ID.RA-04 | CR-D-09.2-001 | OBLIGATION | ** |
| ID | ID.RA-05 | CR-D-09.2-001 | OBLIGATION | ** |
| ID | ID.AM-08 | CR-D-09.4-001 | OBLIGATION | ** |
| ID | ID.RA-05 | CR-D-09.4-001 | OBLIGATION | ** |
| ID | ID.RA-04 | CR-D-10.2-001 | OBLIGATION | ** |
| ID | ID.RA-05 | CR-D-10.3-001 | OBLIGATION | ** |
| ID | ID.IM-02 | CR-D-10.3-001 | OBLIGATION | ** |
| ID | ID.RA-01 | BPR-D-02.1-001 | BEST-PRACTICE | ** |
| ID | ID.RA-03 | BPR-D-02.1-001 | BEST-PRACTICE | ** |
| ID | ID.RA-05 | BPR-D-02.1-001 | BEST-PRACTICE | ** |
| ID | ID.IM-02 | BPR-D-02.1-001 | BEST-PRACTICE | ** |
| ID | ID.RA-01 | BPR-D-02.2-001 | BEST-PRACTICE | ** |
| ID | ID.AM-01 | BPR-D-03.1-001 | BEST-PRACTICE | ** |
| ID | ID.IM-02 | BPR-D-03.4-001 | BEST-PRACTICE | ** |
| ID | ID.AM-08 | BPR-D-05.3-001 | BEST-PRACTICE | ** |
| ID | ID.RA-01 | BPR-D-07.1-001 | BEST-PRACTICE | ** |
| ID | ID.RA-04 | BPR-D-07.2-001 | BEST-PRACTICE | ** |
| ID | ID.RA-05 | BPR-D-07.2-001 | BEST-PRACTICE | ** |
| ID | ID.RA-01 | BPR-D-10.3-001 | BEST-PRACTICE | ** |
| ID | ID.RA-04 | BPR-D-10.3-001 | BEST-PRACTICE | ** |
| ID | ID.RA-05 | BPR-D-10.3-001 | BEST-PRACTICE | ** |
| ID | ID.IM-02 | BPR-D-10.3-001 | BEST-PRACTICE | ** |
| ID | ID.RA-01 | BPR-D-10.3-002 | BEST-PRACTICE | ** |
| ID | ID.RA-04 | BPR-D-10.3-002 | BEST-PRACTICE | ** |
| ID | ID.RA-05 | BPR-D-10.3-002 | BEST-PRACTICE | ** |
| PR | PR.DS-01 | CR-D-01.1-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-01.1-001 | OBLIGATION | ** |
| PR | PR.PS-04 | CR-D-01.1-001 | OBLIGATION | ** |
| PR | PR.DS-02 | CR-D-01.2-001 | OBLIGATION | ** |
| PR | PR.IR-01 | CR-D-01.2-001 | OBLIGATION | ** |
| PR | PR.PS-04 | CR-D-01.2-001 | OBLIGATION | ** |
| PR | PR.AA-03 | CR-D-01.3-001 | OBLIGATION | ** |
| PR | PR.AA-04 | CR-D-01.3-001 | OBLIGATION | ** |
| PR | PR.DS-01 | CR-D-01.3-001 | OBLIGATION | ** |
| PR | PR.IR-03 | CR-D-01.3-001 | OBLIGATION | ** |
| PR | PR.DS-01 | CR-D-01.4-001 | OBLIGATION | ** |
| PR | PR.DS-02 | CR-D-01.4-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-01.4-001 | OBLIGATION | ** |
| PR | PR.DS-01 | CR-D-01.4-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-01.4-001 | OBLIGATION | ** |
| PR | PR.IR-03 | CR-D-01.4-001 | OBLIGATION | ** |
| PR | PR.IR-04 | CR-D-01.4-001 | OBLIGATION | ** |
| PR | PR.PS-04 | CR-D-01.4-001 | OBLIGATION | ** |
| PR | PR.PS-02 | CR-D-02.1-001 | OBLIGATION | ** |
| PR | PR.IR-03 | CR-D-02.2-001 | OBLIGATION | ** |
| PR | PR.PS-01 | CR-D-02.2-001 | OBLIGATION | ** |
| PR | PR.PS-02 | CR-D-02.2-001 | OBLIGATION | ** |
| PR | PR.AA-01 | CR-D-03.1-001 | OBLIGATION | ** |
| PR | PR.AA-02 | CR-D-03.1-001 | OBLIGATION | ** |
| PR | PR.AA-03 | CR-D-03.1-001 | OBLIGATION | ** |
| PR | PR.AA-05 | CR-D-03.1-001 | OBLIGATION | ** |
| PR | PR.AA-06 | CR-D-03.1-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-03.1-001 | OBLIGATION | ** |
| PR | PR.AA-03 | CR-D-03.2-001 | OBLIGATION | ** |
| PR | PR.AA-04 | CR-D-03.2-001 | OBLIGATION | ** |
| PR | PR.AA-05 | CR-D-03.2-001 | OBLIGATION | ** |
| PR | PR.AA-06 | CR-D-03.2-001 | OBLIGATION | ** |
| PR | PR.AT-02 | CR-D-03.2-001 | OBLIGATION | ** |
| PR | PR.AA-01 | CR-D-03.3-001 | OBLIGATION | ** |
| PR | PR.AA-03 | CR-D-03.3-001 | OBLIGATION | ** |
| PR | PR.AA-05 | CR-D-03.3-001 | OBLIGATION | ** |
| PR | PR.AA-06 | CR-D-03.3-001 | OBLIGATION | ** |
| PR | PR.PS-04 | CR-D-03.3-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-03.4-001 | OBLIGATION | ** |
| PR | PR.PS-01 | CR-D-03.4-001 | OBLIGATION | ** |
| PR | PR.PS-04 | CR-D-03.4-001 | OBLIGATION | ** |
| PR | PR.PS-04 | CR-D-04.1-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-04.2-001 | OBLIGATION | ** |
| PR | PR.IR-03 | CR-D-04.2-001 | OBLIGATION | ** |
| PR | PR.IR-04 | CR-D-04.2-001 | OBLIGATION | ** |
| PR | PR.DS-01 | CR-D-04.4-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-04.4-001 | OBLIGATION | ** |
| PR | PR.IR-03 | CR-D-04.4-001 | OBLIGATION | ** |
| PR | PR.IR-04 | CR-D-04.4-001 | OBLIGATION | ** |
| PR | PR.DS-01 | CR-D-05.1-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-05.1-001 | OBLIGATION | ** |
| PR | PR.PS-06 | CR-D-05.1-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-05.2-001 | OBLIGATION | ** |
| PR | PR.PS-02 | CR-D-05.2-001 | OBLIGATION | ** |
| PR | PR.PS-04 | CR-D-05.2-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-05.3-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-05.3-001 | OBLIGATION | ** |
| PR | PR.DS-02 | CR-D-05.3-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-05.4-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-05.4-001 | OBLIGATION | ** |
| PR | PR.AA-03 | CR-D-05.4-001 | OBLIGATION | ** |
| PR | PR.DS-02 | CR-D-05.4-001 | OBLIGATION | ** |
| PR | PR.PS-02 | CR-D-06.2-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-06.3-001 | OBLIGATION | ** |
| PR | PR.PS-06 | CR-D-06.3-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-07.1-001 | OBLIGATION | ** |
| PR | PR.PS-01 | CR-D-07.1-001 | OBLIGATION | ** |
| PR | PR.PS-02 | CR-D-07.1-001 | OBLIGATION | ** |
| PR | PR.PS-06 | CR-D-07.1-001 | OBLIGATION | ** |
| PR | PR.AT-01 | CR-D-08.1-001 | OBLIGATION | ** |
| PR | PR.AT-02 | CR-D-08.1-001 | OBLIGATION | ** |
| PR | PR.PS-01 | CR-D-08.1-001 | OBLIGATION | ** |
| PR | PR.AT-01 | CR-D-08.2-001 | OBLIGATION | ** |
| PR | PR.AT-02 | CR-D-08.2-001 | OBLIGATION | ** |
| PR | PR.AT-02 | CR-D-08.2-001 | OBLIGATION | ** |
| PR | PR.DS-10 | CR-D-09.4-001 | OBLIGATION | ** |
| PR | PR.DS-01 | CR-D-10.2-001 | OBLIGATION | ** |
| PR | PR.PS-04 | CR-D-10.2-001 | OBLIGATION | ** |
| PR | PR.PS-06 | CR-D-10.3-001 | OBLIGATION | ** |
| PR | PR.DS-01 | BPR-D-01.1-001 | BEST-PRACTICE | ** |
| PR | PR.DS-10 | BPR-D-01.1-001 | BEST-PRACTICE | ** |
| PR | PR.PS-04 | BPR-D-01.1-001 | BEST-PRACTICE | ** |
| PR | PR.DS-02 | BPR-D-01.2-001 | BEST-PRACTICE | ** |
| PR | PR.IR-01 | BPR-D-01.2-001 | BEST-PRACTICE | ** |
| PR | PR.PS-04 | BPR-D-01.2-001 | BEST-PRACTICE | ** |
| PR | PR.PS-02 | BPR-D-02.1-001 | BEST-PRACTICE | ** |
| PR | PR.IR-03 | BPR-D-02.2-001 | BEST-PRACTICE | ** |
| PR | PR.PS-01 | BPR-D-02.2-001 | BEST-PRACTICE | ** |
| PR | PR.PS-02 | BPR-D-02.2-001 | BEST-PRACTICE | ** |
| PR | PR.AA-01 | BPR-D-03.1-001 | BEST-PRACTICE | ** |
| PR | PR.AA-03 | BPR-D-03.1-001 | BEST-PRACTICE | ** |
| PR | PR.AA-05 | BPR-D-03.1-001 | BEST-PRACTICE | ** |
| PR | PR.AA-06 | BPR-D-03.1-001 | BEST-PRACTICE | ** |
| PR | PR.AA-03 | BPR-D-03.2-001 | BEST-PRACTICE | ** |
| PR | PR.AA-04 | BPR-D-03.2-001 | BEST-PRACTICE | ** |
| PR | PR.AA-05 | BPR-D-03.2-001 | BEST-PRACTICE | ** |
| PR | PR.AA-06 | BPR-D-03.2-001 | BEST-PRACTICE | ** |
| PR | PR.PS-01 | BPR-D-03.4-001 | BEST-PRACTICE | ** |
| PR | PR.PS-04 | BPR-D-03.4-001 | BEST-PRACTICE | ** |
| PR | PR.DS-10 | BPR-D-05.3-001 | BEST-PRACTICE | ** |
| PR | PR.DS-10 | BPR-D-05.3-001 | BEST-PRACTICE | ** |
| PR | PR.PS-01 | BPR-D-07.1-001 | BEST-PRACTICE | ** |
| PR | PR.PS-02 | BPR-D-07.1-001 | BEST-PRACTICE | ** |
| PR | PR.PS-06 | BPR-D-07.1-001 | BEST-PRACTICE | ** |
| PR | PR.PS-01 | BPR-D-07.2-001 | BEST-PRACTICE | ** |
| PR | PR.PS-02 | BPR-D-07.2-001 | BEST-PRACTICE | ** |
| PR | PR.PS-06 | BPR-D-07.2-001 | BEST-PRACTICE | ** |
| PR | PR.DS-01 | BPR-D-10.2-001 | BEST-PRACTICE | ** |
| PR | PR.PS-04 | BPR-D-10.2-001 | BEST-PRACTICE | ** |
| PR | PR.PS-06 | BPR-D-10.3-002 | BEST-PRACTICE | ** |
| DE | DE.AE-02 | CR-D-04.1-001 | OBLIGATION | ** |
| DE | DE.CM-01 | CR-D-04.1-001 | OBLIGATION | ** |
| DE | DE.CM-09 | CR-D-04.1-001 | OBLIGATION | ** |
| DE | DE.CM-09 | CR-D-04.2-001 | OBLIGATION | ** |
| DE | DE.CM-01 | CR-D-10.2-001 | OBLIGATION | ** |
| DE | DE.AE-02 | CR-D-10.3-001 | OBLIGATION | ** |
| DE | DE.CM-01 | BPR-D-10.2-001 | BEST-PRACTICE | ** |
| DE | DE.AE-02 | BPR-D-10.2-001 | BEST-PRACTICE | ** |
| RS | RS.CO-03 | CR-D-02.3-001 | OBLIGATION | ** |
| RS | RS.MA-01 | CR-D-02.3-001 | OBLIGATION | ** |
| RS | RS.MA-01 | CR-D-04.1-001 | OBLIGATION | ** |
| RS | RS.MA-02 | CR-D-04.1-001 | OBLIGATION | ** |
| RS | RS.MA-03 | CR-D-04.1-001 | OBLIGATION | ** |
| RS | RS.MI-01 | CR-D-04.2-001 | OBLIGATION | ** |
| RS | RS.MI-02 | CR-D-04.2-001 | OBLIGATION | ** |
| RS | RS.CO-02 | CR-D-04.3-001 | OBLIGATION | ** |
| RS | RS.MA-01 | CR-D-04.3-001 | OBLIGATION | ** |
| RS | RS.MA-01 | CR-D-04.3-001 | OBLIGATION | ** |
| RS | RS.MA-02 | CR-D-04.3-001 | OBLIGATION | ** |
| RS | RS.MA-03 | CR-D-04.3-001 | OBLIGATION | ** |
| RS | RS.MA-01 | CR-D-04.3-001 | OBLIGATION | ** |
| RS | RS.MA-01 | CR-D-06.3-001 | OBLIGATION | ** |
| RS | RS.MI-01 | CR-D-06.3-001 | OBLIGATION | ** |
| RS | RS.MA-03 | CR-D-09.4-001 | OBLIGATION | ** |
| RS | RS.MA-01 | BPR-D-04.3-001 | BEST-PRACTICE | ** |
| RS | RS.MA-02 | BPR-D-04.3-001 | BEST-PRACTICE | ** |
| RS | RS.MA-03 | BPR-D-04.3-001 | BEST-PRACTICE | ** |
| RS | RS.MA-01 | BPR-D-04.3-001 | BEST-PRACTICE | ** |
| RS | RS.CO-02 | BPR-D-04.3-001 | BEST-PRACTICE | ** |
| RS | RS.MA-01 | BPR-D-04.3-002 | BEST-PRACTICE | ** |
| RS | RS.MA-01 | BPR-D-04.3-002 | BEST-PRACTICE | ** |
| RS | RS.MA-02 | BPR-D-04.3-002 | BEST-PRACTICE | ** |
| RS | RS.CO-02 | BPR-D-04.3-002 | BEST-PRACTICE | ** |
| RS | RS.MA-01 | BPR-D-04.3-002 | BEST-PRACTICE | ** |
| RC | RC.RP-01 | CR-D-04.2-001 | OBLIGATION | ** |
| RC | RC.RP-04 | CR-D-04.2-001 | OBLIGATION | ** |
| RC | RC.RP-01 | CR-D-04.4-001 | OBLIGATION | ** |
| RC | RC.RP-03 | CR-D-04.4-001 | OBLIGATION | ** |
| RC | RC.RP-04 | CR-D-04.4-001 | OBLIGATION | ** |
| RC | RC.RP-01 | BPR-D-04.3-001 | BEST-PRACTICE | ** |
| RC | RC.RP-01 | BPR-D-04.3-002 | BEST-PRACTICE | ** |

---

## ANEXO B — CONTROL INDEX BY ISO 27001 ANNEX A

| ISO 27001 Control | Control ID | Type | Implementation Status |
|-------------------|------------|------|-----------------------|
| A.8.24 | CR-D-01.1-001 | OBLIGATION | ** |
| A.8.24 | CR-D-01.2-001 | OBLIGATION | ** |
| A.8.24 | CR-D-01.3-001 | OBLIGATION | ** |
| A.8.24 | CR-D-01.4-001 | OBLIGATION | ** |
| A.8.8 | CR-D-02.1-001 | OBLIGATION | ** |
| A.8.8 | CR-D-02.2-001 | OBLIGATION | ** |
| A.5.5 | CR-D-02.3-001 | OBLIGATION | ** |
| A.5.16 | CR-D-03.1-001 | OBLIGATION | ** |
| A.8.5 | CR-D-03.2-001 | OBLIGATION | ** |
| A.5.15 | CR-D-03.3-001 | OBLIGATION | ** |
| A.8.9 | CR-D-03.4-001 | OBLIGATION | ** |
| A.5.25 | CR-D-04.1-001 | OBLIGATION | ** |
| A.5.26 | CR-D-04.2-001 | OBLIGATION | ** |
| A.5.24 | CR-D-04.3-001 | OBLIGATION | ** |
| A.8.13 | CR-D-04.4-001 | OBLIGATION | ** |
| A.8.10 | CR-D-05.1-001 | OBLIGATION | ** |
| A.5.33 | CR-D-05.2-001 | OBLIGATION | ** |
| A.8.10 | CR-D-05.3-001 | OBLIGATION | ** |
| A.5.14 | CR-D-05.4-001 | OBLIGATION | ** |
| A.5.19 | CR-D-06.1-001 | OBLIGATION | ** |
| A.5.21 | CR-D-06.2-001 | OBLIGATION | ** |
| A.5.20 | CR-D-06.3-001 | OBLIGATION | ** |
| A.8.25 | CR-D-07.1-001 | OBLIGATION | ** |
| A.6.3 | CR-D-08.1-001 | OBLIGATION | ** |
| A.6.3 | CR-D-08.2-001 | OBLIGATION | ** |
| A.5.1 | CR-D-09.1-001 | OBLIGATION | ** |
| A.5.7 | CR-D-09.2-001 | OBLIGATION | ** |
| A.5.33 | CR-D-09.4-001 | OBLIGATION | ** |
| A.8.15 | CR-D-10.2-001 | OBLIGATION | ** |
| A.5.35 | CR-D-10.3-001 | OBLIGATION | ** |
| A.8.24 | BPR-D-01.1-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-01.2-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-02.1-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-02.2-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-03.1-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-03.2-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-03.4-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-04.3-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-04.3-002 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-05.3-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-07.1-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-07.2-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-09.1-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-10.2-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-10.3-001 | BEST-PRACTICE | ** |
| A.8.24 | BPR-D-10.3-002 | BEST-PRACTICE | ** |

---

## ANEXO C — CONTROL INDEX BY REGULATION & ARTICLE

| Statutory Source | Control ID | Type | Implementation Status |
|------------------|------------|------|-----------------------|
| ** GDPR Art. 5(1)(f) + Art. 32(1)(b); CRA Art. 24 | CR-D-01.1-001 | OBLIGATION | ** |
| ** GDPR Art. 5(1)(f) + Art. 32(1)(a); CRA Art. 25 | CR-D-01.2-001 | OBLIGATION | ** |
| ** CRA Art. 15 + Art. 24 (source clause CRA-C15); | CR-D-01.3-001 | OBLIGATION | ** |
| ** GDPR Art. 5(1)(d) + Art. 32(1)(b); CRA Annex I §1.3(c) | CR-D-01.4-001 | OBLIGATION | ** |
| ** CRA Art. 17 + Art. 5 (source clauses CRA-C01, CRA-C17). | CR-D-02.1-001 | OBLIGATION | ** |
| ** CRA Art. 4 + Art. 5 (source clauses CRA-C04, CRA-C19). | CR-D-02.2-001 | OBLIGATION | ** |
| ** CRA Art. 19 + Art. 20 (source clauses CRA-C21, CRA-C26). | CR-D-02.3-001 | OBLIGATION | ** |
| ** CRA Art. 10 (source clause CRA-C05). | CR-D-03.1-001 | OBLIGATION | ** |
| ** CRA Art. 9 (source clause CRA-C06); related GDPR security | CR-D-03.2-001 | OBLIGATION | ** |
| ** GDPR Art. 5(1)(c) + Art. 22 and Art. 32(1)(b); CRA Art. 8 | CR-D-03.3-001 | OBLIGATION | ** |
| ** CRA Art. 3 + Art. 8 (source clause CRA-C03); related GDPR | CR-D-03.4-001 | OBLIGATION | ** |
| ** CRA Art. 6 + Art. 13; related GDPR security rationale: | CR-D-04.1-001 | OBLIGATION | ** |
| ** GDPR Art. 32(1)(c); CRA Art. 11 (source clauses GDPR-C18 | CR-D-04.2-001 | OBLIGATION | ** |
| ** GDPR Art. 33(1) + Art. 33(2) + Art. 33(3); CRA Art. 20 | CR-D-04.3-001 | OBLIGATION | ** |
| ** GDPR Art. 32(1)(b) and (c) + Art. 19; CRA Art. 26 | CR-D-04.4-001 | OBLIGATION | ** |
| ** GDPR Art. 5(1)(c); CRA Annex I §1.2(c) | CR-D-05.1-001 | OBLIGATION | ** |
| ** GDPR Art. 5(1)(e) (source clauses GDPR-C02, GDPR-C03). | CR-D-05.2-001 | OBLIGATION | ** |
| ** GDPR Art. 17; CRA Art. 11 | CR-D-05.3-001 | OBLIGATION | ** |
| ** GDPR Art. 20 (source clause GDPR-C07). | CR-D-05.4-001 | OBLIGATION | ** |
| ** GDPR Art. 28(1); related CRA supply-chain rationale: | CR-D-06.1-001 | OBLIGATION | ** |
| ** CRA Art. 18(2) + Annex I §1.4 (source clause CRA-C18). | CR-D-06.2-001 | OBLIGATION | ** |
| ** GDPR Art. 28(3); related CRA supply-chain rationale: | CR-D-06.3-001 | OBLIGATION | ** |
| ** GDPR Art. 25; CRA Art. 18 + Art. 23 and Art. 13(8)-(9) | CR-D-07.1-001 | OBLIGATION | ** |
| ** GDPR Art. 39(1)(b) + Art. 5(2) (source clause GDPR-C27). | CR-D-08.1-001 | OBLIGATION | ** |
| ** GDPR Art. 37 + Art. 39; related CRA product-security competence: | CR-D-08.2-001 | OBLIGATION | ** |
| ** GDPR Art. 5(2) + Art. 24; CRA Art. 13 + Annex VII | CR-D-09.1-001 | OBLIGATION | ** |
| ** GDPR Art. 32(2) + Art. 35 + Art. 36; CRA Art. 13(5) | CR-D-09.2-001 | OBLIGATION | ** |
| ** GDPR Art. 30 + Art. 33(5) | CR-D-09.4-001 | OBLIGATION | ** |
| ** CRA Art. 22 (source clause CRA-C14); related GDPR accountability: | CR-D-10.2-001 | OBLIGATION | ** |
| ** GDPR Art. 32(1)(d) + Art. 28(3)(h); CRA Art. 14 + Art. 21 | CR-D-10.3-001 | OBLIGATION | ** |
