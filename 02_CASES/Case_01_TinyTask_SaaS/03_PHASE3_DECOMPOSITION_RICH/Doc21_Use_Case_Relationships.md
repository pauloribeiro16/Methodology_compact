---
document_id: AEGIS-P3-RICH-13a
title: Use Case Relationships — TinyTask Team Organizer (Phase 3 RICH)
phase: 3
version: 1.0
created: 2026-08-24
updated: 2026-08-26
author: Fase de Especificação 6 Executor (paulo@methodology.pt)
status: EXTENDED_PRODUCT_BASELINE
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [Doc20_Use_Cases_Catalog.md]
outputs: [Doc23_Architectural_Nodes.md, Doc24_Requirements_Allocation.md]
related_documents: [Doc20_Use_Cases_Catalog.md, Doc22_Use_Case_Variability.md, RULE_FREEZE.md]
freeze_total_relationships: 24
freeze_total_constrains_edges: 35
freeze_total_threats_edges: 8
freeze_total_mitigated_by_edges: 24
reconciliation_note: "Fase de Especificação 6: 24 legacy «include»/«extend» edges preserved verbatim; +35 «constrains» edges (security U.C. → functional U.C.); +8 «threatens» edges (MUC → functional U.C.); +24 «mitigated_by» edges (MUC → security U.C.). Total edge catalogue: 91."
sprint6_note: "Fase de Especificação 6: EXTENDED. New edge types introduced for product baseline and misuse-case threat modelling. Existing U.C.* IDs untouched; new U.C.7-11 + MUC-01..08 referenced as sources/targets."
---

# Use Case Relationships — TinyTask Team Organizer (Phase 3 RICH)

> **Status:** EXTENDED_PRODUCT_BASELINE.
> Three edge families:
> 1. **Functional** — `«include»` / `«extend»` between U.C.1-6 (security/compliance) preserved verbatim from v2.0 (24 edges).
> 2. **Security constraints** — `«constrains»` from each security UC-01..UC-13 to the functional UC-14..UC-36 it restricts (35 edges; 1-to-1 mapping for primary constraints; some functional UCs are constrained by multiple security UCs).
> 3. **Threat model** — `«threatens»` from each MUC to its target functional U.C., and `«mitigated by»` from each MUC to the security U.C. that addresses it (8 + 24 edges respectively).

---

## §1 Reconciliation Notes

**Authoritative sources:**
- `Doc20_Use_Cases_Catalog.md` §2 (functional UC-14..UC-36), §3 (security UC-01..UC-13), §4 (MUCs).
- `RULE_FREEZE.md` §5 (UC enumeration v2 — security U.C.s preserved).
- `CORPUS_LINKAGE.md` §3 (UC-to-D-XX.Y mapping).

**Gate criteria:**
- All `«include»` / `«extend»` targets exist (validated by §2/§3 below — same set as v2.0).
- All `«constrains»` targets exist as functional UC-14, UC-15, UC-16, UC-17, UC-18-11.
- All `«threatens»` / `«mitigated by»` endpoints exist as functional UC-14..UC-36 / security UC-01, UC-02, UC-03, UC-04-6.
- No orphan U.C.s (every U.C. has ≥1 relationship or is documented standalone — §4).

---

## §2 `«include»` Relationships (16 — preserved from v2.0)

| Including UC | Included UC | Rationale |
|--------------|-------------|-----------|
| PROC-01 | UC-08 | DSAR requires authenticated subject |
| UC-01 | UC-08 | Erasure requires authenticated subject |
| UC-02 | UC-08 | Data export requires authenticated subject |
| UC-04 | UC-08 | Rectification requires authenticated subject |
| PROC-03 | UC-10 | Vulnerability detection requires audit logging |
| UC-05 | UC-10 | Patch deployment logs to audit trail |
| PROC-05 | UC-10 | Incident notification logs to audit trail |
| UC-07 | UC-10 | Data restoration logs to audit trail |
| UC-08 | UC-10 | Authentication events logged |
| UC-09 | UC-08 | MFA requires base authentication |
| PROC-07 | UC-08 | Account deprovisioning requires auth context |
| PROC-08 | PROC-04 | SSDLC triggers coordinated disclosure |
| UC-11 | PROC-04 | SAST/DAST findings feed disclosure process |
| PROC-09 | PROC-12 | Pre-launch risk assessment = DPIA |
| PROC-13 | UC-10 | RoPA updates logged |
| UC-13 | PROC-14 | SBOM publication requires processor due diligence |

---

## §3 `«extend»` Relationships (8 — preserved from v2.0)

| Base UC | Extending UC | Extension point | Rationale |
|---------|--------------|-----------------|-----------|
| PROC-05 | PROC-18 | Incident-→-DoS scenario | DoS triggers 24h ENISA notification path |
| PROC-09 | PROC-12 | DPIA extends risk assessment | High-risk processing extends DPIA |
| UC-10 | PROC-03 | Audit log feeds SIEM detection | SIEM extends audit logging |
| PROC-10 | PROC-11 | Policy review extends documentation | Documentation is artefact of policy |
| PROC-15 | PROC-17 | Phishing extends annual training | Practical exercise for awareness |
| PROC-04 | PROC-05 | CVD triggers incident notification | Disclosed vuln may become incident |
| PROC-20 | UC-08 | Secure defaults constrain auth | Hardened baseline applied to auth |
| UC-12 | UC-05 | Patch deployment is operationalised by automation | DEV-side patch → SEC-side deployment |

---

## §4 `«constrains»` Relationships (Fase de Especificação 6 new — Security U.C. → Functional U.C.)

> One row per security U.C. with its **primary** functional U.C. constraint (the UC the security control is designed to safeguard). Many functional U.C.s are constrained by multiple security U.C.s — the "primary" link is shown here for navigability; the full bridge lives in `Doc24_Requirements_Allocation.md` and `22_Traceability_Matrix.xlsx` (sheets FUNCUC_TO_SECUC + MUC_TO_MITIGATION).

| Security UC | Constrains Functional UC | Constraint type |
|-------------|--------------------------|-----------------|
| PROC-01 (DSAR) | UC-34, UC-35, UC-36 | Rights enforcement |
| PROC-02 (Rectification) | UC-34 | Data integrity |
| UC-01 (Erasure) | UC-36 | Data lifecycle |
| UC-02 (Export) | UC-35 | Portability + rate limit |
| UC-03 (Consent) | UC-14, UC-34 | Consent capture at signup + at view |
| UC-04 (Structured portability) | UC-35 | Schema + endpoint |
| PROC-03 (Vuln-free release) | UC-21, UC-27 | Release gating |
| UC-05 (Patch deployment) | All UC-14..UC-36 | Availability |
| PROC-04 (CVD) | All UC-14..UC-36 | Vulnerability intake |
| UC-06 (Exploit severity limit) | UC-21, UC-27 | Containment + attachment quarantine |
| PROC-18 (DoS resilience) | All UC-14..UC-36 | Availability |
| PROC-05 (Incident notification) | All UC-14..UC-36 | Notification clock |
| UC-07 (Data restoration) | All UC-14..UC-36 | Recovery |
| UC-08 (Authentication) | UC-14, UC-15, UC-16, UC-17, UC-30 | Authn |
| UC-09 (MFA privileged) | UC-33 (Enterprise SSO), UC-32 | Privileged access |
| PROC-19 (Authorisation) | UC-18, UC-19, UC-20, UC-21, UC-22, UC-23, UC-24, UC-32 | Authz + role scoping |
| PROC-20 (Secure defaults) | All UC-14..UC-36 | Hardened baseline |
| PROC-06 (Processing & breach records) | All UC-14..UC-36 | Record-keeping |
| UC-10 (Audit logging) | All UC-14..UC-36 | Observability |
| PROC-07 (Control testing) | All UC-14..UC-36 | Periodic validation |
| PROC-08 (SSDLC) | UC-19, UC-20, UC-21, UC-22, UC-23, UC-24, UC-30, UC-31, UC-32, UC-33 | Secure development |
| UC-11 (SAST/DAST) | UC-19, UC-20, UC-21, UC-22, UC-23, UC-24, UC-27 | Build-time gating |
| UC-12 (Security patch) | All UC-14..UC-36 | Patch cadence |
| PROC-21 (Fail-safe) | UC-24, UC-28, UC-30 | Fail-closed behaviour |
| PROC-09 (Pre-launch risk assessment) | UC-31, UC-33, UC-34, UC-35, UC-36 | Launch gating |
| PROC-10 (Annual policy review) | All UC-14..UC-36 | Governance |
| PROC-11 (Tech docs maintenance) | All UC-14..UC-36 | Documentation currency |
| PROC-12 (DPIA) | UC-31, UC-33, UC-34, UC-35, UC-36 | DPIA gating |
| PROC-13 (RoPA) | All UC-14..UC-36 | Record of processing |
| PROC-14 (Processor due diligence) | UC-31, UC-15 | Vendor risk |
| CAP-01 (DPAs) | UC-31, UC-15 | Contractual |
| UC-13 (SBOM) | UC-19, UC-20, UC-21, UC-22, UC-23, UC-24, UC-30, UC-31, UC-32, UC-33 | Transparency |
| PROC-15 (Annual awareness) | All UC-14..UC-36 (human-driven) | Awareness |
| PROC-16 (Role-specific training) | UC-18, UC-32 | Role competence |
| PROC-17 (Phishing sim) | UC-14, UC-15 | Awareness reinforcement |

---

## §5 `«threatens»` Relationships (MUC → Functional U.C., 8 edges new)

| MUC | Threatens | Attack vector |
|-----|-----------|---------------|
| MUC-01 (Credential stuffing) | UC-15, UC-16 | Brute force at login |
| MUC-02 (Privilege escalation) | UC-18, UC-32 | Role manipulation |
| MUC-03 (Cross-tenant injection) | UC-20, UC-21, UC-24, UC-19, UC-30 | Missing workspace_id scope |
| MUC-04 (Bulk extraction) | UC-35, UC-28 | Export endpoint + search |
| MUC-05 (Compromised integration) | UC-31, UC-15 | Webhook spoofing + OAuth client |
| MUC-06 (Insider exfiltration) | All UC-14..UC-36 (data plane) | Privileged DB/backup access |
| MUC-07 (Board DoS) | UC-24, All UC-14..UC-36 (availability) | L7 DDoS on expensive endpoints |
| MUC-08 (Malicious attachment) | UC-27 | Polyglot file serving |

---

## §6 `«mitigated by»` Relationships (MUC → Security U.C., 24 edges new)

| MUC | Mitigated by (security U.C.) |
|-----|------------------------------|
| MUC-01 | UC-08, UC-09, UC-06, UC-10 |
| MUC-02 | PROC-19, UC-10, PROC-11 |
| MUC-03 | PROC-20, PROC-19, PROC-03, UC-11 |
| MUC-04 | UC-02, UC-04, PROC-18, UC-10 |
| MUC-05 | PROC-14, CAP-01, UC-08 |
| MUC-06 | UC-09, PROC-19, UC-10, UC-06 |
| MUC-07 | PROC-18, PROC-21, UC-07 |
| MUC-08 | UC-06, UC-10, UC-11 |

---

## §7 Functional `«include»` / `«extend»` Edges (new — derived from §2 catalogue)

> These edges describe reuse within the product UC-14, UC-15, UC-16, UC-17, UC-18-11. They were not in v2.0 because there were no functional UCs.

| Including UC | Included UC | Rationale |
|--------------|-------------|-----------|
| UC-21 (Create Task) | UC-15 (Login) | Task creation requires authn |
| UC-21 (Create Task) | UC-20 (Create Project) | Task belongs to project |
| UC-22 (Assign Task) | UC-18 (Invite+roles) | Assignee must be project member |
| UC-25 (Comment) | UC-21 (Create Task) | Comment attached to task |
| UC-26 (Mention+notify) | UC-18 (Invite+roles) | Mentioned user must be project member |
| UC-27 (Attachment) | UC-21 (Create Task) | Attachment belongs to task |
| UC-28 (Search) | UC-15 (Login) | Search requires authn |
| UC-29 (Activity feed) | UC-15 (Login) | Feed requires authn |
| UC-30 (Mobile sync) | UC-15 (Login) | Sync requires authn |
| UC-33 (Enterprise SSO) | UC-15 (Login) | SSO extends login |
| UC-35 (Export) | UC-15 (Login) | Export requires authn |
| UC-36 (Delete) | UC-15 (Login) | Deletion requires authn |
| UC-36 (Delete workspace) | UC-18 (Invite+roles) | Owner-only operation |

---

## §8 Orphan check

> Functional UC-14..UC-36 are no longer orphan: each has ≥1 security U.C. constraining it, ≥1 functional `«include»`/`«extend»` (except where standalone is intentional, e.g., UC-14 Sign-Up which is the root of all auth flow).

| Standalone (intentional) | Rationale |
|--------------------------|-----------|
| UC-14 (Sign-Up) | Root of authn flow; no upstream include. |
| UC-31 (Stripe Checkout) | Leaf of billing flow; no downstream include. |

No orphan U.C.s overall.

---

## §9 Package consistency

Package membership matches `Doc20_Use_Cases_Catalog.md` §2/§3. No U.C. spans multiple packages. Cross-package edges (PKG-3 → PKG-7, PKG-2 → PKG-9, etc.) are explicit in §4-§7 and traceable to inter-domain rule mappings in `CORPUS_LINKAGE.md` §10.

---

## §10 Cross-references

- `Doc20_Use_Cases_Catalog.md` §2 (functional UC-14..UC-36), §3 (security UC-01..UC-13), §4 (MUCs).
- `Doc22_Use_Case_Variability.md` — variants.
- `Doc24_Requirements_Allocation.md` — requirements mapped to U.C.
- `22_Traceability_Matrix.xlsx` — sheets FUNCUC_TO_SECUC + MUC_TO_MITIGATION.
- `RULE_FREEZE.md` §5 — UC enumeration v2.

---

**End of Use Case Relationships (Phase 3 RICH, EXTENDED_PRODUCT_BASELINE, v1.0)**