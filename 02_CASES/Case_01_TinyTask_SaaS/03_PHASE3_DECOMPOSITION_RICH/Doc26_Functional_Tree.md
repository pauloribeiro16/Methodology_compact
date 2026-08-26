---
document_id: AEGIS-P3-RICH-17
title: Functional Tree — TinyTask Team Organizer (Phase 3 RICH)
phase: 3
version: 2.0
created: 2026-08-24
updated: 2026-08-26
author: Sprint 6 Executor (paulo@methodology.pt)
status: PRODUCT_ROOT_REWRITE
sprint: 6
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [Doc20_Use_Cases_Catalog.md, Doc21_Use_Case_Relationships.md, RULE_FREEZE.md]
outputs: [18_Functional_Tree.drawio]
related_documents: [Doc20_Use_Cases_Catalog.md, Doc21_Use_Case_Relationships.md, RULE_FREEZE.md, CORPUS_LINKAGE.md]
freeze_total_l0: 1
freeze_total_l1: 11
freeze_total_l2_functional: 23
freeze_total_l2_security: 35
freeze_total_muc: 8
reconciliation_note: "Sprint 6 v2.0: tree re-rooted at 'TinyTask Team Organizer' (product-first). L1 = 11 packages (5 functional PKG-7..11 + 6 security PKG-DP/SEC/IAM/DEV/GOV/TRN). L2 = 23 functional U.C.s + 35 security U.C.s. MUCs shown as transversal threat-model layer (cross-package)."
sprint6_note: "Sprint 6: PRODUCT-ROOT. Old v0.4 tree had compliance-only L0 ('TinyTask Compliance Map'); replaced with product-rooted L0 with compliance as a transversal layer."
---

# Functional Tree — TinyTask Team Organizer (Phase 3 RICH)

> **Status (Sprint 6):** PRODUCT_ROOT_REWRITE.
> The functional tree is now rooted at the **product** (TinyTask Team Organizer), with security/compliance as a transversal layer. L0 = 1 product root. L1 = 11 packages (5 functional PKG-7..11 + 6 security PKG-DP/SEC/IAM/DEV/GOV/TRN). L2 = 23 functional U.C.s + 35 security U.C.s. MUCs (8) rendered as transversal threat-model layer.

---

## §1 Reconciliation Notes

The functional tree is the visual root of the Phase 3 decomposition. In Sprint 6 we re-root from the old "TinyTask Compliance Map" (compliance-only) to "TinyTask Team Organizer" (product-first), so the tree reads as a product decomposition with security as a transversal layer.

**Authoritative sources:**
- `Doc20_Use_Cases_Catalog.md` §2 (functional U.C.7-11) + §3 (security U.C.1-6) + §4 (MUCs).
- `Doc21_Use_Case_Relationships.md` §4-§6 (`constrains` / `threatens` / `mitigated_by`).
- `RULE_FREEZE.md` §5 (UC enumeration v2.0).

**Generation pipeline:** Mermaid block (§2) → `scripts/gen_drawio.py` → `18_Functional_Tree.drawio`. Same script as v0.4; only the input Mermaid changes.

---

## §2 Mermaid source (consumed by `gen_drawio.py`)

```mermaid
flowchart TD
    ROOT(L0: TinyTask Team Organizer)
    PKG_7(L1: PKG-7 Account & Access)
    PKG_8(L1: PKG-8 Team & Task Core)
    PKG_9(L1: PKG-9 Collaboration)
    PKG_10(L1: PKG-10 Platform)
    PKG_11(L1: PKG-11 Self-Service)
    PKG_DP(L1: PKG-DP Data Protection)
    PKG_SEC(L1: PKG-SEC Security Operations)
    PKG_IAM(L1: PKG-IAM Identity & Access)
    PKG_DEV(L1: PKG-DEV Secure Development)
    PKG_GOV(L1: PKG-GOV Governance & Compliance)
    PKG_TRN(L1: PKG-TRN Training & Awareness)
    MUC_LAYER(L0+: MUCs Threat Model)
    UC_7_1_1(L2: U.C.7.1.1 Sign Up)
    UC_7_1_2(L2: U.C.7.1.2 Login)
    UC_7_1_3(L2: U.C.7.1.3 Password Reset)
    UC_7_2_1(L2: U.C.7.2.1 Session Mgmt)
    UC_7_5_1(L2: U.C.7.5.1 Invite+Roles)
    UC_8_1_1(L2: U.C.8.1.1 Workspace)
    UC_8_1_2(L2: U.C.8.1.2 Project)
    UC_8_2_1(L2: U.C.8.2.1 Create Task)
    UC_8_2_2(L2: U.C.8.2.2 Assign Task)
    UC_8_2_3(L2: U.C.8.2.3 Status/Due)
    UC_8_3_1(L2: U.C.8.3.1 Board View)
    UC_9_1_1(L2: U.C.9.1.1 Comment)
    UC_9_2_1(L2: U.C.9.2.1 Mention+Notify)
    UC_9_3_1(L2: U.C.9.3.1 Attachment)
    UC_9_4_1(L2: U.C.9.4.1 Search)
    UC_9_5_1(L2: U.C.9.5.1 Activity Feed)
    UC_10_1_1(L2: U.C.10.1.1 Mobile Sync)
    UC_10_2_1(L2: U.C.10.2.1 Stripe Checkout)
    UC_10_3_1(L2: U.C.10.3.1 Admin Console)
    UC_10_3_2(L2: U.C.10.3.2 Enterprise SSO)
    UC_11_1_1(L2: U.C.11.1.1 View Account)
    UC_11_2_1(L2: U.C.11.2.1 Export Data)
    UC_11_3_1(L2: U.C.11.3.1 Delete Account)
    UC_1_1_1(L2: U.C.1.1.1 DSAR)
    UC_1_1_2(L2: U.C.1.1.2 Rectification)
    UC_1_2_1(L2: U.C.1.2.1 Erasure)
    UC_1_3_1(L2: U.C.1.3.1 Data Export)
    UC_1_4_1(L2: U.C.1.4.1 Consent)
    UC_1_5_1(L2: U.C.1.5.1 Portability)
    UC_2_1_1(L2: U.C.2.1.1 Vuln-Free Release)
    UC_2_2_1(L2: U.C.2.2.1 Patch Deployment)
    UC_2_3_1(L2: U.C.2.3.1 CVD)
    UC_2_4_1(L2: U.C.2.4.1 Exploit Severity)
    UC_2_4_2(L2: U.C.2.4.2 DoS Resilience)
    UC_2_5_1(L2: U.C.2.5.1 Incident Notification)
    UC_2_6_1(L2: U.C.2.6.1 Data Restoration)
    UC_3_1_1(L2: U.C.3.1.1 Authentication)
    UC_3_1_2(L2: U.C.3.1.2 MFA Privileged)
    UC_3_2_1(L2: U.C.3.2.1 Authorisation)
    UC_3_3_1(L2: U.C.3.3.1 Secure Defaults)
    UC_3_4_1(L2: U.C.3.4.1 Processing Records)
    UC_3_5_1(L2: U.C.3.5.1 Audit Logging)
    UC_3_6_1(L2: U.C.3.6.1 Control Testing)
    UC_4_1_1(L2: U.C.4.1.1 Security by Design)
    UC_4_2_1(L2: U.C.4.2.1 SAST/DAST)
    UC_4_3_1(L2: U.C.4.3.1 Patch Deploy)
    UC_4_4_1(L2: U.C.4.4.1 Fail-Safe)
    UC_4_5_1(L2: U.C.4.5.1 Pre-Launch RA)
    UC_5_1_1(L2: U.C.5.1.1 Policy Review)
    UC_5_1_2(L2: U.C.5.1.2 Tech Docs)
    UC_5_2_1(L2: U.C.5.2.1 DPIA)
    UC_5_3_1(L2: U.C.5.3.1 RoPA)
    UC_5_4_1(L2: U.C.5.4.1 Processor DD)
    UC_5_5_1(L2: U.C.5.5.1 DPA)
    UC_5_6_1(L2: U.C.5.6.1 SBOM)
    UC_6_1_1(L2: U.C.6.1.1 Annual Training)
    UC_6_2_1(L2: U.C.6.2.1 Role-Specific)
    UC_6_3_1(L2: U.C.6.3.1 Phishing Sim)
    MUC_01(L2+: MUC-01 Credential Stuffing)
    MUC_02(L2+: MUC-02 Privilege Escalation)
    MUC_03(L2+: MUC-03 Cross-Tenant)
    MUC_04(L2+: MUC-04 Bulk Extraction)
    MUC_05(L2+: MUC-05 Compromised Integration)
    MUC_06(L2+: MUC-06 Insider Exfiltration)
    MUC_07(L2+: MUC-07 Board DoS)
    MUC_08(L2+: MUC-08 Malicious Attachment)
    ROOT --> PKG_7
    ROOT --> PKG_8
    ROOT --> PKG_9
    ROOT --> PKG_10
    ROOT --> PKG_11
    ROOT --> PKG_DP
    ROOT --> PKG_SEC
    ROOT --> PKG_IAM
    ROOT --> PKG_DEV
    ROOT --> PKG_GOV
    ROOT --> PKG_TRN
    PKG_7 --> UC_7_1_1
    PKG_7 --> UC_7_1_2
    PKG_7 --> UC_7_1_3
    PKG_7 --> UC_7_2_1
    PKG_7 --> UC_7_5_1
    PKG_8 --> UC_8_1_1
    PKG_8 --> UC_8_1_2
    PKG_8 --> UC_8_2_1
    PKG_8 --> UC_8_2_2
    PKG_8 --> UC_8_2_3
    PKG_8 --> UC_8_3_1
    PKG_9 --> UC_9_1_1
    PKG_9 --> UC_9_2_1
    PKG_9 --> UC_9_3_1
    PKG_9 --> UC_9_4_1
    PKG_9 --> UC_9_5_1
    PKG_10 --> UC_10_1_1
    PKG_10 --> UC_10_2_1
    PKG_10 --> UC_10_3_1
    PKG_10 --> UC_10_3_2
    PKG_11 --> UC_11_1_1
    PKG_11 --> UC_11_2_1
    PKG_11 --> UC_11_3_1
    PKG_DP --> UC_1_1_1
    PKG_DP --> UC_1_1_2
    PKG_DP --> UC_1_2_1
    PKG_DP --> UC_1_3_1
    PKG_DP --> UC_1_4_1
    PKG_DP --> UC_1_5_1
    PKG_SEC --> UC_2_1_1
    PKG_SEC --> UC_2_2_1
    PKG_SEC --> UC_2_3_1
    PKG_SEC --> UC_2_4_1
    PKG_SEC --> UC_2_4_2
    PKG_SEC --> UC_2_5_1
    PKG_SEC --> UC_2_6_1
    PKG_IAM --> UC_3_1_1
    PKG_IAM --> UC_3_1_2
    PKG_IAM --> UC_3_2_1
    PKG_IAM --> UC_3_3_1
    PKG_IAM --> UC_3_4_1
    PKG_IAM --> UC_3_5_1
    PKG_IAM --> UC_3_6_1
    PKG_DEV --> UC_4_1_1
    PKG_DEV --> UC_4_2_1
    PKG_DEV --> UC_4_3_1
    PKG_DEV --> UC_4_4_1
    PKG_DEV --> UC_4_5_1
    PKG_GOV --> UC_5_1_1
    PKG_GOV --> UC_5_1_2
    PKG_GOV --> UC_5_2_1
    PKG_GOV --> UC_5_3_1
    PKG_GOV --> UC_5_4_1
    PKG_GOV --> UC_5_5_1
    PKG_GOV --> UC_5_6_1
    PKG_TRN --> UC_6_1_1
    PKG_TRN --> UC_6_2_1
    PKG_TRN --> UC_6_3_1
    MUC_LAYER --> MUC_01
    MUC_LAYER --> MUC_02
    MUC_LAYER --> MUC_03
    MUC_LAYER --> MUC_04
    MUC_LAYER --> MUC_05
    MUC_LAYER --> MUC_06
    MUC_LAYER --> MUC_07
    MUC_LAYER --> MUC_08
```

---

## §3 Tree structure (L0 → L1 → L2)

| Level | Count | Element | Owner |
|-------|------:|---------|-------|
| L0 | 1 | ROOT: TinyTask Team Organizer (product) | — |
| L0+ | 1 | MUC_LAYER: Threat Model (cross-package) | — |
| L1 (functional) | 5 | PKG-7 Account & Access · PKG-8 Team & Task Core · PKG-9 Collaboration · PKG-10 Platform · PKG-11 Self-Service | — |
| L1 (security/compliance) | 6 | PKG-DP Data Protection · PKG-SEC Security Operations · PKG-IAM Identity & Access · PKG-DEV Secure Development · PKG-GOV Governance & Compliance · PKG-TRN Training & Awareness | — |
| L2 (functional) | 23 | U.C.7-11 IDs (see Doc20 §2) | — |
| L2 (security/compliance) | 35 | U.C.1-6 IDs (see Doc20 §3; preserved verbatim from v0.4 freeze) | — |
| L2+ (threat model) | 8 | MUC-01..08 (Sindre & Opdahl misuse cases) | — |
| **Total** | **79** | | |

---

## §4 Generation pipeline

The Mermaid block above is consumed by `scripts/gen_drawio.py`, which emits `18_Functional_Tree.drawio`. The script is unchanged from v0.4 (Mermaid → drawio XML).

```bash
python3 scripts/gen_drawio.py --input Doc26_Functional_Tree.md --output 18_Functional_Tree.drawio
```

---

## §5 Cross-references

- `Doc20_Use_Cases_Catalog.md` §2 (functional) + §3 (security) + §4 (MUCs).
- `Doc21_Use_Case_Relationships.md` §4 (constrains) + §5 (threatens) + §6 (mitigated by).
- `RULE_FREEZE.md` §5 (UC enumeration v2.0).
- `CORPUS_LINKAGE.md` §10 (D-XX.Y coverage of security UCs).

---

**End of Functional Tree (Phase 3 RICH, PRODUCT_ROOT_REWRITE, v2.0 — Sprint 6)**