---
document_id: AEGIS-P3-RICH-13b
title: Use Case Variability — TinyTask SaaS (Phase 3 RICH)
phase: 3
version: 0.4
created: 2026-08-24
updated: 2026-08-24
author: Sprint 4 Executor (paulo@methodology.pt)
status: ADJUSTED_FIELDS
sprint: 4
sprint_role: schema_adjustment
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [13_Use_Cases_Catalog.md, 13a_Use_Case_Relationships.md]
outputs: [14_Architectural_Nodes.md]
related_documents: [13_Use_Cases_Catalog.md, 13a_Use_Case_Relationships.md, RULE_FREEZE.md]
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Maturity, Priority, Stakeholders, Reporting]
freeze_total_variants: 18
reconciliation_note: "Variability catalogue ported from legacy; 18 variants over 12 UCs; F-00a CLOSED."
sprint4_note: "Sprint 4: 6 columns appended to §2 variants table; values to be filled in Sprint 5."
---

# Use Case Variability — TinyTask SaaS (Phase 3 RICH)

> **Status:** ADJUSTED_FIELDS (Sprint 4). 18 variants identified across 12 base UCs.

---

## §1 Reconciliation Notes

Variability points are conditions under which a UC's behaviour branches. They support risk-based prioritisation (P2 proportionality) and Sprint 5's deep-enrichment per UC.

**Authoritative sources:**
- `RULE_FREEZE.md` §5 — UC enumeration.
- `CORPUS_LINKAGE.md` §3 — UC-to-D-XX.Y mapping.
- `13_Use_Cases_Catalog.md` §3 — UC catalogue.

---

## §2 Variability catalogue (18 variants × 12 base UCs)

| # | Base UC | Variant | Trigger | Effect | Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|---|---------|---------|---------|--------|-------|-----------------------|----------|----------|--------------|-----------|
| V-01 | U.C.1.1.1 | **V.Self-service** | Data subject authenticated | Auto-generated DSAR report (JSON, CSV, PDF) within 30 days | | | | | | |
| V-02 | U.C.1.1.1 | **V.Manual** | Identity not verified | Manual review by DPO + paper trail | | | | | | |
| V-03 | U.C.1.2.1 | **V.Backup-locations** | Erasure request | Erasure extends to backups (RPO ≤ 30 days) | | | | | | |
| V-04 | U.C.1.2.1 | **V.Log-retention** | Erasure request | Anonymisation in logs (no PII retention) | | | | | | |
| V-05 | U.C.2.1.1 | **V.Sev.Critical** | CVE ≥ 9.0 | Patch within 24h | | | | | | |
| V-06 | U.C.2.1.1 | **V.Sev.High** | CVE 7.0-8.9 | Patch within 7 days | | | | | | |
| V-07 | U.C.2.5.1 | **V.ENISA-24h** | CRA-reportable incident | ENISA notification within 24h | | | | | | |
| V-08 | U.C.2.5.1 | **V.GDPR-72h** | Personal-data breach | CNPD notification within 72h | | | | | | |
| V-09 | U.C.3.1.1 | **V.SSO** | Customer requests SAML/OIDC | Federated auth supported | | | | | | |
| V-10 | U.C.3.1.2 | **V.FIDO2** | Privileged user | Hardware key required (BPR-D-03.2-001) | | | | | | |
| V-11 | U.C.3.1.2 | **V.TOTP** | Non-privileged user | TOTP fallback acceptable | | | | | | |
| V-12 | U.C.4.5.1 | **V.DPIA** | High-risk processing identified | Full DPIA + DPO consultation | | | | | | |
| V-13 | U.C.4.5.1 | **V.FRIA-light** | Low-risk processing | Lightweight risk checklist | | | | | | |
| V-14 | U.C.5.4.1 | **V.Annual-audit** | Processor DPA anniversary | Re-attest controls | | | | | | |
| V-15 | U.C.5.6.1 | **V.CycloneDX** | Default SBOM format | Machine-readable per CRA | | | | | | |
| V-16 | U.C.5.6.1 | **V.SPDX** | Customer request | SPDX format alternative | | | | | | |
| V-17 | U.C.6.1.1 | **V.New-hire** | Onboarding | Training within 30 days of start | | | | | | |
| V-18 | U.C.6.3.1 | **V.External-tool** | Phishing provider | Third-party simulation acceptable (per DPA) | | | | | | |

---

## §3 Variability cross-check

All variants trace back to a base UC that exists in `13_Use_Cases_Catalog.md` §3 freeze set. No new UCs introduced. Variant triggers derive from:

- **Regulatory timelines** (V-07/V-08: CRA 24h / GDPR 72h)
- **Severity thresholds** (V-05/V-06: CVE severity)
- **Customer-specific SLAs** (V-09/V-15/V-16)
- **Internal policy** (V-17/V-18)

---

## §4 Cross-references

- `13_Use_Cases_Catalog.md` §3 — UC catalogue
- `13a_Use_Case_Relationships.md` §3 — `«extend»` relationships
- `RULE_FREEZE.md` §5 — UC enumeration
- `CORPUS_LINKAGE.md` §3 — UC-to-D-XX.Y

---

**End of Use Case Variability (Phase 3 RICH, ADJUSTED_FIELDS, Sprint 4)**
