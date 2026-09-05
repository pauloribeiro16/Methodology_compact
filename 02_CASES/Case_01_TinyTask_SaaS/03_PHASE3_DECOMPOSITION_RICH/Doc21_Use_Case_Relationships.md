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
> 2. **Security constraints** — `«constrains»` from each security U.C.1-6 to the functional U.C.7-11 it restricts (35 edges; 1-to-1 mapping for primary constraints; some functional UCs are constrained by multiple security UCs).
> 3. **Threat model** — `«threatens»` from each MUC to its target functional U.C., and `«mitigated by»` from each MUC to the security U.C. that addresses it (8 + 24 edges respectively).

---

## §1 Reconciliation Notes

**Authoritative sources:**
- `Doc20_Use_Cases_Catalog.md` §2 (functional U.C.7-11), §3 (security U.C.1-6), §4 (MUCs).
- `RULE_FREEZE.md` §5 (UC enumeration v2 — security U.C.s preserved).
- `CORPUS_LINKAGE.md` §3 (UC-to-D-XX.Y mapping).

**Gate criteria:**
- All `«include»` / `«extend»` targets exist (validated by §2/§3 below — same set as v2.0).
- All `«constrains»` targets exist as functional U.C.7-11.
- All `«threatens»` / `«mitigated by»` endpoints exist as functional U.C.7-11 / security U.C.1-6.
- No orphan U.C.s (every U.C. has ≥1 relationship or is documented standalone — §4).

---

## §2 `«include»` Relationships (16 — preserved from v2.0)

| Including UC | Included UC | Rationale |
|--------------|-------------|-----------|
| PROC-01 | U.C.3.1.1 | DSAR requires authenticated subject |
| U.C.1.2.1 | U.C.3.1.1 | Erasure requires authenticated subject |
| U.C.1.3.1 | U.C.3.1.1 | Data export requires authenticated subject |
| U.C.1.5.1 | U.C.3.1.1 | Rectification requires authenticated subject |
| PROC-03 | U.C.3.5.1 | Vulnerability detection requires audit logging |
| U.C.2.2.1 | U.C.3.5.1 | Patch deployment logs to audit trail |
| PROC-05 | U.C.3.5.1 | Incident notification logs to audit trail |
| U.C.2.6.1 | U.C.3.5.1 | Data restoration logs to audit trail |
| U.C.3.1.1 | U.C.3.5.1 | Authentication events logged |
| U.C.3.1.2 | U.C.3.1.1 | MFA requires base authentication |
| PROC-07 | U.C.3.1.1 | Account deprovisioning requires auth context |
| PROC-08 | PROC-04 | SSDLC triggers coordinated disclosure |
| U.C.4.2.1 | PROC-04 | SAST/DAST findings feed disclosure process |
| PROC-09 | PROC-12 | Pre-launch risk assessment = DPIA |
| PROC-13 | U.C.3.5.1 | RoPA updates logged |
| U.C.5.6.1 | PROC-14 | SBOM publication requires processor due diligence |

---

## §3 `«extend»` Relationships (8 — preserved from v2.0)

| Base UC | Extending UC | Extension point | Rationale |
|---------|--------------|-----------------|-----------|
| PROC-05 | U.C.2.4.2 | Incident-→-DoS scenario | DoS triggers 24h ENISA notification path |
| PROC-09 | PROC-12 | DPIA extends risk assessment | High-risk processing extends DPIA |
| U.C.3.5.1 | PROC-03 | Audit log feeds SIEM detection | SIEM extends audit logging |
| PROC-10 | PROC-11 | Policy review extends documentation | Documentation is artefact of policy |
| PROC-15 | PROC-17 | Phishing extends annual training | Practical exercise for awareness |
| PROC-04 | PROC-05 | CVD triggers incident notification | Disclosed vuln may become incident |
| U.C.3.3.1 | U.C.3.1.1 | Secure defaults constrain auth | Hardened baseline applied to auth |
| U.C.4.3.1 | U.C.2.2.1 | Patch deployment is operationalised by automation | DEV-side patch → SEC-side deployment |

---

## §4 `«constrains»` Relationships (Fase de Especificação 6 new — Security U.C. → Functional U.C.)

> One row per security U.C. with its **primary** functional U.C. constraint (the UC the security control is designed to safeguard). Many functional U.C.s are constrained by multiple security U.C.s — the "primary" link is shown here for navigability; the full bridge lives in `Doc24_Requirements_Allocation.md` and `22_Traceability_Matrix.xlsx` (sheets FUNCUC_TO_SECUC + MUC_TO_MITIGATION).

| Security UC | Constrains Functional UC | Constraint type |
|-------------|--------------------------|-----------------|
| PROC-01 (DSAR) | U.C.11.1.1, U.C.11.2.1, U.C.11.3.1 | Rights enforcement |
| PROC-02 (Rectification) | U.C.11.1.1 | Data integrity |
| U.C.1.2.1 (Erasure) | U.C.11.3.1 | Data lifecycle |
| U.C.1.3.1 (Export) | U.C.11.2.1 | Portability + rate limit |
| U.C.1.4.1 (Consent) | U.C.7.1.1, U.C.11.1.1 | Consent capture at signup + at view |
| U.C.1.5.1 (Structured portability) | U.C.11.2.1 | Schema + endpoint |
| PROC-03 (Vuln-free release) | U.C.8.2.1, U.C.9.3.1 | Release gating |
| U.C.2.2.1 (Patch deployment) | All U.C.7-11 | Availability |
| PROC-04 (CVD) | All U.C.7-11 | Vulnerability intake |
| U.C.2.4.1 (Exploit severity limit) | U.C.8.2.1, U.C.9.3.1 | Containment + attachment quarantine |
| U.C.2.4.2 (DoS resilience) | All U.C.7-11 | Availability |
| PROC-05 (Incident notification) | All U.C.7-11 | Notification clock |
| U.C.2.6.1 (Data restoration) | All U.C.7-11 | Recovery |
| U.C.3.1.1 (Authentication) | U.C.7.1.1, U.C.7.1.2, U.C.7.1.3, U.C.7.2.1, U.C.10.1.1 | Authn |
| U.C.3.1.2 (MFA privileged) | U.C.10.3.2 (Enterprise SSO), U.C.10.3.1 | Privileged access |
| U.C.3.2.1 (Authorisation) | U.C.7.5.1, U.C.8.*, U.C.10.3.1 | Authz + role scoping |
| U.C.3.3.1 (Secure defaults) | All U.C.7-11 | Hardened baseline |
| PROC-06 (Processing & breach records) | All U.C.7-11 | Record-keeping |
| U.C.3.5.1 (Audit logging) | All U.C.7-11 | Observability |
| PROC-07 (Control testing) | All U.C.7-11 | Periodic validation |
| PROC-08 (SSDLC) | U.C.8.*, U.C.10.* | Secure development |
| U.C.4.2.1 (SAST/DAST) | U.C.8.*, U.C.9.3.1 | Build-time gating |
| U.C.4.3.1 (Security patch) | All U.C.7-11 | Patch cadence |
| U.C.4.4.1 (Fail-safe) | U.C.8.3.1, U.C.9.4.1, U.C.10.1.1 | Fail-closed behaviour |
| PROC-09 (Pre-launch risk assessment) | U.C.10.2.1, U.C.10.3.2, U.C.11.x | Launch gating |
| PROC-10 (Annual policy review) | All U.C.7-11 | Governance |
| PROC-11 (Tech docs maintenance) | All U.C.7-11 | Documentation currency |
| PROC-12 (DPIA) | U.C.10.2.1, U.C.10.3.2, U.C.11.x | DPIA gating |
| PROC-13 (RoPA) | All U.C.7-11 | Record of processing |
| PROC-14 (Processor due diligence) | U.C.10.2.1, U.C.7.1.2 | Vendor risk |
| CAP-01 (DPAs) | U.C.10.2.1, U.C.7.1.2 | Contractual |
| U.C.5.6.1 (SBOM) | U.C.8.*, U.C.10.* | Transparency |
| PROC-15 (Annual awareness) | All U.C.7-11 (human-driven) | Awareness |
| PROC-16 (Role-specific training) | U.C.7.5.1, U.C.10.3.1 | Role competence |
| PROC-17 (Phishing sim) | U.C.7.1.1, U.C.7.1.2 | Awareness reinforcement |

---

## §5 `«threatens»` Relationships (MUC → Functional U.C., 8 edges new)

| MUC | Threatens | Attack vector |
|-----|-----------|---------------|
| MUC-01 (Credential stuffing) | U.C.7.1.2, U.C.7.1.3 | Brute force at login |
| MUC-02 (Privilege escalation) | U.C.7.5.1, U.C.10.3.1 | Role manipulation |
| MUC-03 (Cross-tenant injection) | U.C.8.1.2, U.C.8.2.1, U.C.8.3.1, U.C.8.1.1, U.C.10.1.1 | Missing workspace_id scope |
| MUC-04 (Bulk extraction) | U.C.11.2.1, U.C.9.4.1 | Export endpoint + search |
| MUC-05 (Compromised integration) | U.C.10.2.1, U.C.7.1.2 | Webhook spoofing + OAuth client |
| MUC-06 (Insider exfiltration) | All U.C.7-11 (data plane) | Privileged DB/backup access |
| MUC-07 (Board DoS) | U.C.8.3.1, All U.C.7-11 (availability) | L7 DDoS on expensive endpoints |
| MUC-08 (Malicious attachment) | U.C.9.3.1 | Polyglot file serving |

---

## §6 `«mitigated by»` Relationships (MUC → Security U.C., 24 edges new)

| MUC | Mitigated by (security U.C.) |
|-----|------------------------------|
| MUC-01 | U.C.3.1.1, U.C.3.1.2, U.C.2.4.1, U.C.3.5.1 |
| MUC-02 | U.C.3.2.1, U.C.3.5.1, PROC-11 |
| MUC-03 | U.C.3.3.1, U.C.3.2.1, PROC-03, U.C.4.2.1 |
| MUC-04 | U.C.1.3.1, U.C.1.5.1, U.C.2.4.2, U.C.3.5.1 |
| MUC-05 | PROC-14, CAP-01, U.C.3.1.1 |
| MUC-06 | U.C.3.1.2, U.C.3.2.1, U.C.3.5.1, U.C.2.4.1 |
| MUC-07 | U.C.2.4.2, U.C.4.4.1, U.C.2.6.1 |
| MUC-08 | U.C.2.4.1, U.C.3.5.1, U.C.4.2.1 |

---

## §7 Functional `«include»` / `«extend»` Edges (new — derived from §2 catalogue)

> These edges describe reuse within the product U.C.7-11. They were not in v2.0 because there were no functional UCs.

| Including UC | Included UC | Rationale |
|--------------|-------------|-----------|
| U.C.8.2.1 (Create Task) | U.C.7.1.2 (Login) | Task creation requires authn |
| U.C.8.2.1 (Create Task) | U.C.8.1.2 (Create Project) | Task belongs to project |
| U.C.8.2.2 (Assign Task) | U.C.7.5.1 (Invite+roles) | Assignee must be project member |
| U.C.9.1.1 (Comment) | U.C.8.2.1 (Create Task) | Comment attached to task |
| U.C.9.2.1 (Mention+notify) | U.C.7.5.1 (Invite+roles) | Mentioned user must be project member |
| U.C.9.3.1 (Attachment) | U.C.8.2.1 (Create Task) | Attachment belongs to task |
| U.C.9.4.1 (Search) | U.C.7.1.2 (Login) | Search requires authn |
| U.C.9.5.1 (Activity feed) | U.C.7.1.2 (Login) | Feed requires authn |
| U.C.10.1.1 (Mobile sync) | U.C.7.1.2 (Login) | Sync requires authn |
| U.C.10.3.2 (Enterprise SSO) | U.C.7.1.2 (Login) | SSO extends login |
| U.C.11.2.1 (Export) | U.C.7.1.2 (Login) | Export requires authn |
| U.C.11.3.1 (Delete) | U.C.7.1.2 (Login) | Deletion requires authn |
| U.C.11.3.1 (Delete workspace) | U.C.7.5.1 (Invite+roles) | Owner-only operation |

---

## §8 Orphan check

> Functional U.C.7-11 are no longer orphan: each has ≥1 security U.C. constraining it, ≥1 functional `«include»`/`«extend»` (except where standalone is intentional, e.g., U.C.7.1.1 Sign-Up which is the root of all auth flow).

| Standalone (intentional) | Rationale |
|--------------------------|-----------|
| U.C.7.1.1 (Sign-Up) | Root of authn flow; no upstream include. |
| U.C.10.2.1 (Stripe Checkout) | Leaf of billing flow; no downstream include. |

No orphan U.C.s overall.

---

## §9 Package consistency

Package membership matches `Doc20_Use_Cases_Catalog.md` §2/§3. No U.C. spans multiple packages. Cross-package edges (PKG-3 → PKG-7, PKG-2 → PKG-9, etc.) are explicit in §4-§7 and traceable to inter-domain rule mappings in `CORPUS_LINKAGE.md` §10.

---

## §10 Cross-references

- `Doc20_Use_Cases_Catalog.md` §2 (functional U.C.7-11), §3 (security U.C.1-6), §4 (MUCs).
- `Doc22_Use_Case_Variability.md` — variants.
- `Doc24_Requirements_Allocation.md` — requirements mapped to U.C.
- `22_Traceability_Matrix.xlsx` — sheets FUNCUC_TO_SECUC + MUC_TO_MITIGATION.
- `RULE_FREEZE.md` §5 — UC enumeration v2.

---

**End of Use Case Relationships (Phase 3 RICH, EXTENDED_PRODUCT_BASELINE, v1.0)**