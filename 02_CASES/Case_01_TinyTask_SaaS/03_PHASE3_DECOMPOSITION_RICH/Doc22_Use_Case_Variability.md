---
document_id: AEGIS-P3-RICH-13b
title: Use Case Variability — TinyTask Team Organizer (Phase 3 RICH)
phase: 3
version: 1.0
created: 2026-08-24
updated: 2026-08-26
author: Fase de Especificação 6 Executor (paulo@methodology.pt)
status: EXTENDED_PRODUCT_BASELINE
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [Doc20_Use_Cases_Catalog.md, Doc21_Use_Case_Relationships.md]
outputs: [Doc23_Architectural_Nodes.md]
related_documents: [Doc20_Use_Cases_Catalog.md, Doc21_Use_Case_Relationships.md, RULE_FREEZE.md]
freeze_total_variants: 18
freeze_total_functional_variants: 8
reconciliation_note: "Fase de Especificação 6: 18 legacy variants preserved verbatim (V-01..V-18 over security U.C.); +8 functional variants (V-19..V-26 over U.C.7-11) introduced for product-level variability (plan tiers, quotas, MFA enforcement, etc.)."
sprint6_note: "Fase de Especificação 6: EXTENDED. Functional variants anchor V-09 SSO to U.C.10.3.2 (Enterprise SSO) explicitly."
---

# Use Case Variability — TinyTask Team Organizer (Phase 3 RICH)

> **Status:** EXTENDED_PRODUCT_BASELINE.
> Two families of variants:
> 1. **Security/compliance variants** (V-01..V-18, preserved from v2.0) — regulatory timelines, severity thresholds, customer SLAs.
> 2. **Product variants** (V-19..V-26, new in Fase de Especificação 6) — plan tiers, MFA enforcement, mobile sync policy, notification batching.

---

## §1 Reconciliation Notes

Variability points are conditions under which a U.C.'s behaviour branches. They support risk-based prioritisation (P2 proportionality).

**Authoritative sources:**
- `Doc20_Use_Cases_Catalog.md` §2 (functional UC-14..UC-36), §3 (security UC-01..UC-13), §4 (MUCs).
- `RULE_FREEZE.md` §5 (security U.C. enumeration).
- `CORPUS_LINKAGE.md` §3.

---

## §2 Security/Compliance Variability Catalogue (18 variants × 12 base UCs — preserved from v2.0)

| # | Base UC | Variant | Trigger | Effect |
|---|---------|---------|---------|--------|
| V-01 | PROC-01 | **V.Self-service** | Data subject authenticated | Auto-generated DSAR report (JSON, CSV, PDF) within 30 days |
| V-02 | PROC-01 | **V.Manual** | Identity not verified | Manual review by DPO + paper trail |
| V-03 | UC-01 | **V.Backup-locations** | Erasure request | Erasure extends to backups (RPO ≤ 30 days) |
| V-04 | UC-01 | **V.Log-retention** | Erasure request | Anonymisation in logs (no PII retention) |
| V-05 | PROC-03 | **V.Sev.Critical** | CVE ≥ 9.0 | Patch within 24h |
| V-06 | PROC-03 | **V.Sev.High** | CVE 7.0-8.9 | Patch within 7 days |
| V-07 | PROC-05 | **V.ENISA-24h** | CRA-reportable incident | ENISA notification within 24h |
| V-08 | PROC-05 | **V.GDPR-72h** | Personal-data breach | CNPD notification within 72h |
| V-09 | UC-08 | **V.SSO** (re-anchored to **UC-33**) | Customer requests SAML/OIDC | Federated auth supported |
| V-10 | UC-09 | **V.FIDO2** | Privileged user | Hardware key required (BPR-D-03.2-001) |
| V-11 | UC-09 | **V.TOTP** | Non-privileged user | TOTP fallback acceptable |
| V-12 | PROC-09 | **V.DPIA** | High-risk processing identified | Full DPIA + DPO consultation |
| V-13 | PROC-09 | **V.FRIA-light** | Low-risk processing | Lightweight risk checklist |
| V-14 | PROC-14 | **V.Annual-audit** | Processor DPA anniversary | Re-attest controls |
| V-15 | UC-13 | **V.CycloneDX** | Default SBOM format | Machine-readable per CRA |
| V-16 | UC-13 | **V.SPDX** | Customer request | SPDX format alternative |
| V-17 | PROC-15 | **V.New-hire** | Onboarding | Training within 30 days of start |
| V-18 | PROC-17 | **V.External-tool** | Phishing provider | Third-party simulation acceptable (per DPA) |

> **Fase de Especificação 6 note:** V-09 (SSO) re-anchored from the generic `UC-08` to the **Enterprise SSO functional U.C. `UC-33`** for clearer product anchoring. The security UC-08 variant V-09 still stands (the customer-level SSO path).

---

## §3 Functional Variability Catalogue (8 variants × 6 base UC-14..UC-36 new)

| # | Base UC | Variant | Trigger | Effect |
|---|---------|---------|---------|--------|
| V-19 | UC-15 | **V.MFA-optional** | Free-tier user | Password-only acceptable |
| V-20 | UC-15 | **V.MFA-enforced** | Paid-tier / Enterprise | MFA required on every login (UC-09) |
| V-21 | UC-19 | **V.Free-quota** | Workspace count = 1 | Block creation of additional workspace; redirect to UC-31 upgrade |
| V-22 | UC-19 | **V.Paid-unlimited** | Workspace on paid plan | No quota limit |
| V-23 | UC-26 | **V.Notification-immediate** | Enterprise user | Real-time email per mention |
| V-24 | UC-26 | **V.Notification-batched** | Free-tier / default | Digest batched ≤ 5 min |
| V-25 | UC-30 | **V.Mobile-offline** | No network | Local mutations queued; sync on reconnect |
| V-26 | UC-35 | **V.Export-large** | Archive > 100 MB | Async job; email when ready |

---

## §4 Variability cross-check

All variants trace back to a base U.C. that exists in `Doc20_Use_Cases_Catalog.md` §2-§3.

**Variant triggers derive from:**
- **Regulatory timelines** (V-07/V-08: CRA 24h / GDPR 72h).
- **Severity thresholds** (V-05/V-06: CVE severity).
- **Customer-specific SLAs** (V-09/V-15/V-16/V-19/V-20/V-23/V-24).
- **Plan tier** (V-21/V-22).
- **Internal policy** (V-17/V-18).
- **Operational state** (V-25/V-26).

---

## §5 Cross-references

- `Doc20_Use_Cases_Catalog.md` §2 (functional UC-14..UC-36), §3 (security UC-01..UC-13).
- `Doc21_Use_Case_Relationships.md` §2-§7.
- `RULE_FREEZE.md` §5 (security U.C. enumeration).
- `CORPUS_LINKAGE.md` §3.

---

**End of Use Case Variability (Phase 3 RICH, EXTENDED_PRODUCT_BASELINE, v1.0)**