# MERMAID RENDER FIX — Campaign Report (2026-09-05)

**Agent:** Executor · **Status:** DONE (scope complete; one discrepancy flagged — see §7)

---

## 1. Diagnosis

All 26 `useCaseDiagram` Mermaid blocks across 4 documents did not render: the
`useCaseDiagram` type does not exist in any stable Mermaid release
(mermaid-js/mermaid#4628, open). The blocks were written against a phantom
"Mermaid ≥ v11.6" feature.

## 2. Decision (human, 2026-09-05)

**PlantUML + SVG hybrid.** Each use-case diagram becomes:

1. a native ` ```plantuml ` source block in the .md (editable source of truth), plus
2. a rendered SVG committed beside the annex (`svg/`), embedded via markdown image
   so it renders in GitHub / VS Code / `file://`.

Mermaid stays for sequence diagrams and lane-card flowcharts. The 30 failing
sequence diagrams were handled separately by the Orchestrator (`;` → `,`).

## 3. Conversion rules applied

- `actor "N" as ID` → unchanged; `package "L" { }` → `rectangle "L" { }` (system boundary)
- `usecase "A\nB" as ID` → unchanged (PlantUML honours `\n`)
- actor→UC `-->` → `A -- B` (solid association, no arrowhead)
- `..>`/`.>` labelled `include` → `A .> B : <<include>>`; labelled `extend` → `A .> B : <<extend>>` (direction preserved)
- unlabeled dashed edges (Case_01 §2, §4) → `<<include>>` (documented semantics: "invokes")
- `left to right direction` kept; SVGs rendered via `https://www.plantuml.com/plantuml/svg/~h<hex>` (hex-mode URL, UA header required — default python UA got HTTP 403; retry-once logic in place)

## 4. Per-file fidelity (actors / UC ovals / edges, before→after)


### Case_03 — `Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/annexes/A_Use_Case_Diagrams.md` — 8 block(s)

| Section | SVG | Actors before→after | UC ovals | Include | Extend | Assoc | Fidelity |
|---|---|---|---|---|---|---|---|
| §1 — System-wide | `A_s1_system_wide.svg` | 8→8 | 8→8 | 0→0 | 0→0 | 15→15 | MATCH |
| §2 — PKG-A: Onboarding & KYC (UC-69..74) | `A_s2_pkg_a_onboarding_kyc_uc_69_74.svg` | 5→5 | 6→6 | 5→5 | 0→0 | 10→10 | MATCH |
| §3 — PKG-B: Digital Banking Core (UC-75..80) | `A_s3_pkg_b_digital_banking_core_uc_75_80.svg` | 6→6 | 6→6 | 6→6 | 0→0 | 13→13 | MATCH |
| §4 — PKG-C: Lending & OmniScore (UC-63..68) | `A_s4_pkg_c_lending_omniscore_uc_63_68.svg` | 5→5 | 6→6 | 1→1 | 1→1 | 8→8 | MATCH |
| §5 — PKG-D: Payments & Open Banking (UC-81..85) | `A_s5_pkg_d_payments_open_banking_uc_81_85.svg` | 4→4 | 5→5 | 5→5 | 0→0 | 8→8 | MATCH |
| §6 — PKG-E: Corporate & Treasury (UC-86..89) | `A_s6_pkg_e_corporate_treasury_uc_86_89.svg` | 7→7 | 4→4 | 3→3 | 0→0 | 11→11 | MATCH |
| §7 — PKG-F: Fraud & Customer Service (UC-90, UC-91, UC-92, UC-93) | `A_s7_pkg_f_fraud_customer_service_uc_90_uc_91.svg` | 5→5 | 4→4 | 0→0 | 1→1 | 10→10 | MATCH |
| §8 — PKG-DS: Privacy & Data-subject UCs (UC-33, UC-34) | `A_s8_pkg_ds_privacy_data_subject_ucs_uc_33_uc.svg` | 2→2 | 2→2 | 0→0 | 0→0 | 3→3 | MATCH |

### Case_02 — `Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/annexes/A_Use_Case_Diagrams.md` — 6 block(s)

| Section | SVG | Actors before→after | UC ovals | Include | Extend | Assoc | Fidelity |
|---|---|---|---|---|---|---|---|
| §1 — System-wide | `A_s1_system_wide.svg` | 6→6 | 5→5 | 0→0 | 0→0 | 11→11 | MATCH |
| §2 — PKG-8: Traveller eGate Journey (7 use cases) | `A_s2_pkg_8_traveller_egate_journey_7_use_case.svg` | 5→5 | 7→7 | 0→0 | 5→5 | 11→11 | MATCH |
| §3 — PKG-9: Operator Referral Desk (4 use cases) | `A_s3_pkg_9_operator_referral_desk_4_use_cases.svg` | 4→4 | 4→4 | 0→0 | 1→1 | 8→8 | MATCH |
| §4 — PKG-10: Kiosk Fleet Operations (4 use cases) | `A_s4_pkg_10_kiosk_fleet_operations_4_use_case.svg` | 4→4 | 4→4 | 0→0 | 1→1 | 7→7 | MATCH |
| §5 — PKG-11: AI Model Lifecycle (3 use cases) | `A_s5_pkg_11_ai_model_lifecycle_3_use_cases.svg` | 4→4 | 3→3 | 0→0 | 0→0 | 5→5 | MATCH |
| §6 — PKG-12: Administration & Reporting (3 use cases) | `A_s6_pkg_12_administration_reporting_3_use_ca.svg` | 8→8 | 3→3 | 0→0 | 0→0 | 10→10 | MATCH |

### Case_02 — `Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md` §5.1 — 1 block(s)

| Section | SVG | Actors before→after | UC ovals | Include | Extend | Assoc | Fidelity |
|---|---|---|---|---|---|---|---|
| 5.1 Use Case Diagram (Level 0) | `Doc21_s5_1_level0.svg` | 13→13 | 7→7 | 0→0 | 0→0 | 20→20 | MATCH |

### Case_01 — `Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/annexes/A_Use_Case_Diagrams.md` — 11 block(s)

| Section | SVG | Actors before→after | UC ovals | Include | Extend | Assoc | Fidelity |
|---|---|---|---|---|---|---|---|
| §1 — System-wide | `A_s1_system_wide.svg` | 7→7 | 10→10 | 0→0 | 0→0 | 11→11 | MATCH |
| §2 — PKG-7 Account & Access (U.C.7) | `A_s2_pkg_7_account_access_u_c_7.svg` | 3→3 | 5→5 | 1→1 | 0→0 | 5→5 | MATCH |
| §3 — PKG-8 Team & Task Core (U.C.8) | `A_s3_pkg_8_team_task_core_u_c_8.svg` | 3→3 | 6→6 | 0→0 | 0→0 | 7→7 | MATCH |
| §4 — PKG-9 Collaboration (U.C.9) | `A_s4_pkg_9_collaboration_u_c_9.svg` | 1→1 | 5→5 | 1→1 | 0→0 | 5→5 | MATCH |
| §5 — PKG-10 Platform (U.C.10) | `A_s5_pkg_10_platform_u_c_10.svg` | 4→4 | 4→4 | 0→0 | 0→0 | 5→5 | MATCH |
| §6 — PKG-11 Self-Service (U.C.11) | `A_s6_pkg_11_self_service_u_c_11.svg` | 3→3 | 3→3 | 0→0 | 0→0 | 4→4 | MATCH |
| §7 — PKG-DP Data Protection (U.C.1.*) | `A_s7_pkg_dp_data_protection_u_c_1.svg` | 3→3 | 4→4 | 0→0 | 0→0 | 5→5 | MATCH |
| §8 — PKG-SEC Security Operations (U.C.2.*) | `A_s8_pkg_sec_security_operations_u_c_2.svg` | 2→2 | 4→4 | 0→0 | 0→0 | 4→4 | MATCH |
| §9 — PKG-IAM Identity & Access (U.C.3.*) | `A_s9_pkg_iam_identity_access_u_c_3.svg` | 3→3 | 5→5 | 0→0 | 0→0 | 6→6 | MATCH |
| §10 — PKG-DEV Secure Development (U.C.4.*) | `A_s10_pkg_dev_secure_development_u_c_4.svg` | 2→2 | 3→3 | 0→0 | 0→0 | 3→3 | MATCH |
| §11 — PKG-GOV Governance & Compliance (U.C.5.6.1) | `A_s11_pkg_gov_governance_compliance_u_c_5_6_1.svg` | 1→1 | 1→1 | 0→0 | 0→0 | 1→1 | MATCH |

**Fidelity: 26/26 MATCH.** Every converted diagram preserves the exact counts of
actors, use-case ovals, include/extend edges and actor associations of the
original Mermaid source.

## 5. SVG inventory (26 files)

| Case | Directory | Files |
|---|---|---|
| Case_01 | `Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/annexes/svg/` | `A_s1_system_wide` (§1), `A_s2_pkg_7_account_access_u_c_7` (§2), `A_s3_pkg_8_team_task_core_u_c_8` (§3), `A_s4_pkg_9_collaboration_u_c_9` (§4), `A_s5_pkg_10_platform_u_c_10` (§5), `A_s6_pkg_11_self_service_u_c_11` (§6), `A_s7_pkg_dp_data_protection_u_c_1` (§7), `A_s8_pkg_sec_security_operations_u_c_2` (§8), `A_s9_pkg_iam_identity_access_u_c_3` (§9), `A_s10_pkg_dev_secure_development_u_c_4` (§10), `A_s11_pkg_gov_governance_compliance_u_c_5_6_1` (§11) |
| Case_02 | `Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/annexes/svg/` | `A_s1_system_wide` (§1), `A_s2_pkg_8_traveller_egate_journey_7_use_case` (§2), `A_s3_pkg_9_operator_referral_desk_4_use_cases` (§3), `A_s4_pkg_10_kiosk_fleet_operations_4_use_case` (§4), `A_s5_pkg_11_ai_model_lifecycle_3_use_cases` (§5), `A_s6_pkg_12_administration_reporting_3_use_ca` (§6), `Doc21_s5_1_level0` (Doc21 §5.1) |
| Case_03 | `Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/annexes/svg/` | `A_s1_system_wide` (§1), `A_s2_pkg_a_onboarding_kyc_uc_69_74` (§2), `A_s3_pkg_b_digital_banking_core_uc_75_80` (§3), `A_s4_pkg_c_lending_omniscore_uc_63_68` (§4), `A_s5_pkg_d_payments_open_banking_uc_81_85` (§5), `A_s6_pkg_e_corporate_treasury_uc_86_89` (§6), `A_s7_pkg_f_fraud_customer_service_uc_90_uc_91` (§7), `A_s8_pkg_ds_privacy_data_subject_ucs_uc_33_uc` (§8) |

All 26 responses validated: start with `<svg` (or `<?xml`), no `@startuml` error
text, size 2,206–20,297 bytes (>500 threshold).

## 6. Prose updates

- **Case_03 annex** — render note rewritten: PlantUML + committed SVG, mermaid#4628, rubric v1.9 §5C.5.
- **Case_02 annex** — render note rewritten likewise.
- **Case_01 annex** — render note rewritten; frontmatter `version` 0.6→0.7, reconciliation_note appended with v0.7 entry; stale "Syntax mimics the known-good `useCaseDiagram`" line updated.
- **Doc21 §5.1** — no render-note prose existed (only the diagram block); nothing to update. Embed uses `annexes/svg/Doc21_s5_1_level0.svg`.

## 7. Validation outputs (verbatim)

1. **Fidelity (before/after counts):** `TOTAL=26 FIDELITY_MISMATCH=0` — table in §4.
2. **SVG visual render (Playwright chromium, one per case + Doc21):** element counts on the rendered pages:
   - Case_01 `A_s1_system_wide.svg`: svg=1, ellipses=17, rects=10, texts=37
   - Case_02 `A_s2_pkg_8...svg`: svg=1, ellipses=12, rects=1, texts=25
   - Case_02 `Doc21_s5_1_level0.svg`: svg=1, ellipses=20, rects=7, texts=41
   - Case_03 `A_s1_system_wide.svg`: svg=1, ellipses=16, rects=7, texts=33
   Screenshot: `/tmp/svg_check.png` — stick-figure actors, UC ovals (ellipses),
   package boundary rectangles and dashed `<<extend>>` arrows (Case_02 PKG-8) all
   visibly draw. Screenshots inspected by the agent, not just file-trusted.
3. **Mermaid check** (`python3 /tmp/mermaid_check.py`):
   ```
   # mermaid version: 11.x (CDN mermaid@11)
   # TOTAL 192 · FAIL 30 · OK 162
   ```
   TOTAL 192 ≈ 193 as expected (26 useCase blocks are no longer mermaid). **FAIL 30
   is NOT 0 — discrepancy flagged:** all 30 failures are sequence diagrams in
   `Case_02 .../annexes/B_Sequence_Diagrams.md` (18) and `Case_03 .../annexes/
   B_Sequence_Diagrams.md` (12). Those files are OUT OF MY SCOPE (explicit MUST NOT
   touch) and git shows them **unmodified** — the Orchestrator's reported `;`→`,`
   fix is not present in the working tree (e.g. Case_02 B still contains 23 `;`
   lines). No use-case block fails.
4. **`grep 'useCaseDiagram'`** in the 4 target files → 5 hits, all prose
   (render notes explaining the conversion, frontmatter history notes). Zero in
   code fences / diagram sources.
5. **Dashboards smoke:** `python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py`
   → `# all 16 dashboard(s) passed smoke` (16/16, exit 0).
6. **Traceability audit:** `python3 scripts/traceability_audit.py all` → exit 0;
   Case_01 104/104 = 100.0%, 46/46 = 100.0%, 102/102 = 100.0%; Case_02 63/63,
   86/86 = 100.0%; Case_03 42/42, 78/78, 111/111 = 100.0% — unchanged. Report:
   `00_METHODOLOGY/validation/TRACEABILITY_AUDIT_2026-09-05.md`.

## 8. Files touched

- Edited (4): the three `A_Use_Case_Diagrams.md` annexes + `Doc21_Use_Cases_Catalog.md` §5.1.
- Created: 26 SVGs in the three `annexes/svg/` directories (§5 above).
- Report: this file.
- NOT touched (as mandated): `B_Sequence_Diagrams.md` (both), Doc31/Doc32,
  `validation/build_control_set.py`, `kg/**`, `domains/**`, git (no commits).

## 9. Escalation for the human

The 30 sequence-diagram failures pre-date this campaign and belong to the
Orchestrator's earlier fix step, which is not in the working tree. Recommend the
Orchestrator re-apply (or confirm the location of) the `;` → `,` fix in the two
`B_Sequence_Diagrams.md` files; after that, `/tmp/mermaid_check.py` should read
`FAIL 0`.
