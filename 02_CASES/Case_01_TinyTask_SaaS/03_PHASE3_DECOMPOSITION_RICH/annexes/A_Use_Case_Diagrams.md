---
document_id: AEGIS-P3-RICH-ANNEX-A
title: Annex A — Use Case Diagrams (Phase 3 RICH)
phase: 3
version: 0.4
created: 2026-08-24
updated: 2026-08-24
author: Fase de Especificação 4 Executor (paulo@methodology.pt)
status: ADJUSTED_FIELDS
case: Case_01_TinyTask_SaaS
tier: MICRO
sibling_of: ../03_PHASE2_RULES_RICH/
branch: feature/aegis-p3-case01-rich
sibling_doc: ../03_PHASE3_DECOMPOSITION/annexes/A_Use_Case_Diagrams.md
inputs: [13_Use_Cases_Catalog.md, RULE_FREEZE.md, KG_CHAINS.md]
outputs: []
related_documents: [13_Use_Cases_Catalog.md, annexes/B_Sequence_Diagrams.md (not in RICH), annexes/C_Class_Diagrams.md (not in RICH)]
expected_documents: annex-a
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Implementation Status, Priority, Stakeholders, Reporting]
reconciliation_note: "Level 0 + Level 1 Mermaid diagrams from legacy; 6 packages (PKG-DP/SEC/IAM/DEV/GOV/TRN); F-S1-09 KG contamination noted; Annex B/C optional (not in 15 placeholders list); Fase de Especificação 4 schema addendum §A.5 added (no markdown tables in this annex)."
sprint4_note: "Fase de Especificação 4: no markdown index tables in this annex; schema addendum §A.5 references the 6 columns inherited from Doc 13."
---

# Annex A — Use Case Diagrams (Phase 3 RICH)

> **RICH context:** All package diagrams link back to `RULE_FREEZE.md` (46 rules + 31 goals) and `KG_CHAINS.md` (12 inference chains). The 35 L1 UCs are the atomic decomposition target; 62 L1+L2 references preserved.

---

## §A.1 Package Diagram (Domain Organization)

```mermaid
graph TB
    subgraph PKG_DP[PKG-DP: Data Protection]
        UC11[PROC-01 DSAR]
        UC12[PROC-02 Rectification]
        UC13[U.C.1.2.1 Erasure]
        UC14[U.C.1.3.1 Data Export]
        UC15[U.C.1.4.1 Consent]
        UC16[U.C.1.5.1 Portability]
    end
    subgraph PKG_SEC[PKG-SEC: Security Operations]
        UC21[PROC-03 Vuln-Free Release]
        UC22[U.C.2.2.1 Patch Deployment]
        UC23[PROC-04 CVD]
        UC24[U.C.2.4.1 Exploit Severity]
        UC25[U.C.2.4.2 DoS Resilience]
        UC26[PROC-05 Incident Notification]
        UC27[U.C.2.6.1 Data Restoration]
    end
    subgraph PKG_IAM[PKG-IAM: Identity & Access]
        UC31[U.C.3.1.1 Authentication]
        UC32[U.C.3.1.2 MFA Privileged]
        UC33[U.C.3.2.1 Authorisation]
        UC34[U.C.3.3.1 Secure Defaults]
        UC35[PROC-06 Processing Records]
        UC36[U.C.3.5.1 Audit Logging]
        UC37[PROC-07 Control Testing]
    end
    subgraph PKG_DEV[PKG-DEV: Secure Development]
        UC41[PROC-08 Security by Design]
        UC42[U.C.4.2.1 SAST/DAST]
        UC43[U.C.4.3.1 Patch Deploy]
        UC44[U.C.4.4.1 Fail-Safe]
        UC45[PROC-09 Pre-Launch RA]
    end
    subgraph PKG_GOV[PKG-GOV: Governance & Compliance]
        UC51[PROC-10 Policy Review]
        UC52[PROC-11 Tech Docs]
        UC53[PROC-12 DPIA]
        UC54[PROC-13 RoPA]
        UC55[PROC-14 Processor DD]
        UC56[CAP-01 DPA]
        UC57[U.C.5.6.1 SBOM]
    end
    subgraph PKG_TRN[PKG-TRN: Training & Awareness]
        UC61[PROC-15 Annual Training]
        UC62[PROC-16 Role-Specific]
        UC63[PROC-17 Phishing Sim]
    end
```

---

## §A.2 Actor Diagram (Stakeholder → UC)

```mermaid
graph LR
    CEO[SH-INT-001 CEO]
    CTO[SH-INT-002 CTO]
    DEV[SH-INT-003 Lead Dev]
    OPS[SH-INT-004 Ops Lead]
    DPO[SH-INT-005 DPO]
    CUST[SH-EXT-001 Customer]
    PROC[SH-EXT-002 Processor]
    CNPD[SH-EXT-003 CNPD]
    CEO --> UC51
    CTO --> UC31
    CTO --> UC52
    DEV --> UC41
    DEV --> UC42
    OPS --> UC26
    OPS --> UC61
    DPO --> UC53
    DPO --> UC54
    DPO --> UC56
    CUST --> UC11
    CUST --> UC13
    PROC --> UC55
    CNPD --> UC26
```

---

## §A.3 Cross-references

- `RULE_FREEZE.md` §5 — UC enumeration
- `KG_CHAINS.md` §1 — CH-09 (FR-29 → UC-25 → CR-D-04.3)
- `CORPUS_LINKAGE.md` §3 — UC-to-D-XX.Y
- `13_Use_Cases_Catalog.md` §3 — UC catalogue
- `13a_Use_Case_Relationships.md` §2-§3 — `«include»` / `«extend»`

---

## §A.4 Optional annexes (B, C)

`annexes/B_Sequence_Diagrams.md` and `annexes/C_Class_Diagrams.md` are NOT included in the Phase 3 RICH 15 placeholders. They remain available in legacy `03_PHASE3_DECOMPOSITION/annexes/` but are out of scope for the current RICH rebuild sprint. See `validation/SPRINT3_REPORT.md` §3 for the scope decision.

---

## §A.5 Schema addendum

This annex contains only Mermaid diagrams (no markdown index tables). The UC-family schema inherited from `13_Use_Cases_Catalog.md` §3 covers the 6-column Fase de Especificação 4 addition. The canonical UC card fields now include:

| Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|-------|-----------------------|----------|----------|--------------|-----------|

These 6 columns are present on every UC index table in `13_Use_Cases_Catalog.md` §3 (per package), and card-level values will be populated in Fase de Especificação 5.

---

**End of Annex A — Use Case Diagrams (Phase 3 RICH, ADJUSTED_FIELDS, Fase de Especificação 4)**
