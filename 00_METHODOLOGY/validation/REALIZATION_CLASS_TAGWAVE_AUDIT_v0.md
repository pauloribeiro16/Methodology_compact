---
document_id: AEGIS-METH-RC-TAGWAVE-AUDIT-V0
title: Validator Tag-Wave Audit — realization_class application to Case_01 Doc18 (46 rules)
phase: Cross-phase
version: 0.1
created: 2026-09-05
updated: 2026-09-05
author: Validator
status: ACTIVE
---

# Validator Tag-Wave Audit — REALIZATION_CLASS Tagging (Case_01, 2026-09-05)

> **Verdict: `FIX_WAVE_NEEDED`** — 2 rules to fix: `BPR-D-03.4-001` (TECHNOLOGY → PROCESS) and `BPR-D-04.3-001` (PROCESS → CAPABILITY).
> Applied-vs-baseline primary agreement: **41/46 (89.1%)**. Applied-vs-adjudicated primary agreement: **44/46 (95.7%)**. All 8 applied secondaries: **agree**.

---

## 1. Method and sources

1. **Applied classes** extracted from Doc18 `ANEXO A` (per-CSF-anchor rows) and `ANEXO D` (derived distribution, 2026-09-05 Tag wave v1). `ANEXO D` enumerates all 46 IDs per class — used as the per-rule source; every `ANEXO A` row for a given ID carries the identical class (checked corpus-wide — no intra-Anexo inconsistencies).
2. **Blind baseline** = `REALIZATION_CLASS_RUBRIC_VALIDATOR_REPORT_v0.md` §6 (my prior dry-run, 46 rules, written before the tag wave existed).
3. **Adjudication** = fresh walk of the `REALIZATION_CLASS_RUBRIC.md` **v1.2** decision tree (§3) per divergent rule, applying the constitutive-step test and the P/C structural indicators, against the actual card text.
4. **Mirrors checked:** `control_set.yaml` (46 `realization_class:` entries; distribution TECHNOLOGY 18 / PROCESS 23 / CAPABILITY 5 — matches Anexo D), `12_Rules_Catalog.xlsx` (`Rules_Catalog` sheet cols 17/18 `realization_class`/`realization_class_secondary`, spot-checked 6 IDs — match), Doc18 frontmatter (`fields_per_card`/`expected_fields_per_card` correctly bumped 24 → 26), fields 25/26 present on **46/46 cards**.

## 2. Faithfulness of Anexo A to card fields 25/26 (spot-check, 5 rules)

| Rule | Card field 25/26 | Anexo A / Anexo D | Faithful? |
|---|---|---|---|
| CR-D-01.3-001 | TECHNOLOGY / — | TECHNOLOGY / — | Yes |
| CR-D-02.1-001 | PROCESS / TECHNOLOGY | PROCESS (+TECHNOLOGY) | Yes |
| BPR-D-01.2-001 | PROCESS / TECHNOLOGY | PROCESS (+TECHNOLOGY) | Yes |
| BPR-D-04.3-001 | PROCESS / — | PROCESS | Yes |
| BPR-D-07.2-001 | PROCESS / TECHNOLOGY | PROCESS (+TECHNOLOGY) | Yes |

**Anexo A is a faithful render of the card fields.** The campaign also correctly executed rubric §4 mechanics (counter bump 24→26, secondary rendered `—` when unused). Executor distribution confirmed: TECHNOLOGY 18 (13 CR + 5 BPR), PROCESS 23 (13 CR + 10 BPR), CAPABILITY 5, secondaries 8 (7→TECHNOLOGY, CR-D-09.2-001→PROCESS).

## 3. Applied vs baseline — agreement and divergence

**Primary-class agreement: 41/46 (89.1%).** Divergent rules (applied ← baseline):

| Rule | Applied | Baseline | Where adjudicated |
|---|---|---|---|
| CR-D-01.3-001 | TECHNOLOGY | PROCESS (+T) | §4.1 |
| CR-D-02.1-001 | PROCESS (+T) | TECHNOLOGY | §4.2 |
| BPR-D-01.2-001 | PROCESS (+T) | TECHNOLOGY | §4.3 |
| BPR-D-04.3-001 | PROCESS | CAPABILITY | §4.4 |
| BPR-D-07.2-001 | PROCESS (+T) | TECHNOLOGY | §4.5 |

Secondary deltas (informational — secondary is optional 0..1, never a fix by itself): applied CR-D-04.1-001 +TECHNOLOGY (baseline had none — legitimate, agreed); baseline CR-D-05.2-001 +PROCESS and CR-D-05.3-001 +TECHNOLOGY were not applied (permitted; the 05.3 omission matches the rubric §8 exemplar).

## 4. Adjudication of divergent rules (fresh v1.2 walks)

### 4.1 CR-D-01.3-001 — Cryptographic Key Management — ADJUDICATED: `TECHNOLOGY` (agrees with applied; flips baseline)
Criteria (Doc18 L284-290): management report demonstrating segregation; periodic review documenting lifecycle cadence; annual audit for plaintext material. Method INSPECT. **Constitutive-step test:** no exception approval, risk acceptance, or containment/transfer authorisation appears in the criteria — the only recurring human steps are reviews/audits, i.e. periodic re-verification of built state (keeps Q1 = YES). Key rotation/revocation are schedulable/automatable KMS operations, not recurring judgement calls. The automated path (KMS config + generated reports) satisfies all three criteria. My baseline's PROCESS call ("realization is executing lifecycle events") was a v1.0-era "run the procedure again" intuition; v1.2's sharpened disqualifier ("recurring constitutive human judgement") resolves to TECHNOLOGY. Hard borderline — a PROCESS reading remains defensible, but the v1.2 tree yields T. **Fix: none.**

### 4.2 CR-D-02.1-001 — Vulnerability-Free Release — ADJUDICATED: `PROCESS` (+`TECHNOLOGY`) (agrees with applied; flips baseline)
Criterion 3 (L465): "The release record links the scan result, SBOM, **approvals, and any accepted exception**" — the approval/exception step is **in the Verification Criteria**, not only in the Description's exception clause. Per the constitutive-step test (rubric §3 tie-break, v1.2): an accepted exception permits a release the CI gate would otherwise block — outcome changes what the control accepts → constitutive → Q1 = NO. Q2 = YES (advisory feed → scan → gate → release decision/exception with owner; card mandates "CTO or Lead Dev approval for any documented exception", L442-443). Automated pipeline executes the routine path → secondary TECHNOLOGY. My baseline mis-read the criteria as exception-path-only. **Fix: none.**

### 4.3 BPR-D-01.2-001 — Current Transport Cryptographic Standard — ADJUDICATED: `PROCESS` (+`TECHNOLOGY`) (agrees with applied; flips baseline)
Criterion 3 (L3064): "Each … compatibility exception has a provider reason, **owner, and review record**" — exception review in the criteria → constitutive (permits a non-baseline endpoint). Description adds a trigger-sequenced exception lifecycle ("Record protocol exceptions and remove them when the relevant provider supports the baseline", L3043-3044). Q1 = NO, Q2 = YES → PROCESS; endpoint scans/cert automation → secondary TECHNOLOGY. **Fix: none.**

### 4.4 BPR-D-04.3-001 — Maintain an Incident Response Playbook — ADJUDICATED: `CAPABILITY` (secondary PROCESS optional) — **DISAGREES with applied PROCESS → FIX**
- **Q2 structural test fails for PROCESS:** rubric §3 defines PROCESS as running "a defined activity sequence … **rather than a standing artefact**". This rule's object **is** a standing artefact ("maintain one accessible approved incident response playbook", L3592-3593). Criteria 1-2 are standing-state criteria (approved playbook naming owners/triggers/routes; offline copy accessible) — a run of the update-after-trigger mini-workflow alone does not satisfy them.
- **CAPABILITY disqualifier check:** success is NOT shown by executing an SOP step-by-step — an executed update with an unowned, unapproved, offline-inaccessible playbook still fails criteria 1-2.
- **CAPABILITY indicators are constitutive:** named owner of the standing ability (CTO + DPO + Compliance Lead, L3629); authority to approve ("approved playbook", criterion 1; "documented no-change decision", criterion 3 — an authority exercise, not mere re-verification). Between trigger events someone must own the readiness — the assurance lives in the sustained ability, not in the last update run.
- **Consistency anchors:** structurally parallel to CR-D-09.1-001 (CAPABILITY: standing policy architecture, owners/approvals/review records — same card shape) and to the rubric §3 standing note (CR-D-08.1/08.2 are CAPABILITY despite completion-record criteria — records evidence standing readiness).
- The Executor's PROCESS reading (per-trigger update sequence) captures the *maintenance duty* but misses that the duty exists to keep an owned, approved, accessible ability alive. **Fix: field 25 → CAPABILITY** (field 26 may stay `—`; PROCESS secondary optional), plus Anexo A rows, Anexo D, `control_set.yaml`, xlsx.

### 4.5 BPR-D-07.2-001 — SAST and DAST in CI/CD — ADJUDICATED: `PROCESS` (+`TECHNOLOGY`) (agrees with applied; flips baseline)
Criterion 3 (L4005): "Closed findings include disposition, **approval where excepted**, and successful retest evidence" — approval/exception closure **in the criteria** → constitutive; Description adds a standing triage duty ("Triage false positives explicitly and require retest evidence before a security finding is closed", L3984-3985). Q1 = NO; Q2 = YES (PR → SAST gate → release DAST → findings → disposition → retest → closure) → PROCESS; the per-PR/release automated gates → secondary TECHNOLOGY. Contrast with CR-D-03.2-001 (TECHNOLOGY) is intact: there the exception appears only in the Description, not in the criteria. **Fix: none.**

### 4.6 BPR-D-03.4-001 — Harden Systems Using CIS Baselines — ADJUDICATED: `PROCESS` (+`TECHNOLOGY`) — **DISAGREES with applied TECHNOLOGY → FIX** (found by the audit; baseline also tagged T)
Criterion 2 (L3529): "A scan reports compliance status and **maps each failed check to remediation or exception**" — the exception-disposition step is **in the Verification Criteria**; an excepted failed check permits a configuration the control would otherwise reject → constitutive → Q1 = NO. Criterion 3 adds a routing duty ("detects and **routes** an unauthorised hardening change" — escalation indicator); Description adds risk-based review of failed checks and a standing exception register. Q2 = YES (drift scan trigger → map failed checks → remediate or except → route unauthorised change) → PROCESS; the IaC-encoded baseline and scan automation → secondary TECHNOLOGY.
**Consistency compels this:** it is the same criteria pattern the Executor itself classified PROCESS in CR-D-02.2-001 ("recorded remediation or approved exception"), BPR-D-01.2-001 (§4.3) and BPR-D-07.2-001 (§4.5); sibling CR-D-03.4-001 stays TECHNOLOGY only because its criteria contain no exception step. **Fix: field 25 → PROCESS, field 26 → TECHNOLOGY**, plus Anexo A rows, Anexo D, `control_set.yaml`, xlsx.

## 5. Secondary-class audit (8 applied)

| Rule | Applied secondary | Validator | Note |
|---|---|---|---|
| CR-D-02.1-001 | TECHNOLOGY | **Agree** | Pipeline executes the routine path (adjudicated P+T, §4.2) |
| CR-D-02.2-001 | TECHNOLOGY | **Agree** | Rubric §8 exemplar itself |
| CR-D-04.1-001 | TECHNOLOGY | **Agree** | Built fail-safe limits/automated detection behind the triage workflow |
| CR-D-04.2-001 | TECHNOLOGY | **Agree** | Baseline had the same |
| CR-D-04.4-001 | TECHNOLOGY | **Agree** | Baseline had the same |
| CR-D-09.2-001 | PROCESS | **Agree** | Rubric §8 exemplar; baseline had the same |
| BPR-D-01.2-001 | TECHNOLOGY | **Agree** | §4.3 |
| BPR-D-07.2-001 | TECHNOLOGY | **Agree** | §4.5 |

**8/8 secondaries agree.** No missing secondary rises to a fix (secondary is optional 0..1; CR-D-01.3-001's baseline +TECHNOLOGY is moot after §4.1; BPR-D-04.3-001 +PROCESS and BPR-D-03.4-001 secondary are handled with the primary fixes).

## 6. Adjudicated 46-row table

Legend: applied = Executor tag wave v1; baseline = Validator report v0 §6; adjudicated = this audit (fresh v1.2 walk). ✱ = adjudicated ≠ applied (fix).

### PARTE I — Obligation Controls (30 CR)

| # | Rule | Applied | Baseline | Adjudicated | Rationale (one line) |
|---|---|---|---|---|---|
| 1 | CR-D-01.1-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | Criteria are configuration/material reports; automated path satisfies. |
| 2 | CR-D-01.2-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | Channel config + scans; no constitutive recurring judgement. |
| 3 | CR-D-01.3-001 | TECHNOLOGY | PROCESS (+T) | TECHNOLOGY | Criteria only re-verify built state; lifecycle ops automatable — no constitutive judgement (§4.1, hard borderline). |
| 4 | CR-D-01.4-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | Integrity controls + periodic test = re-verification of built state. |
| 5 | CR-D-02.1-001 | PROCESS (+T) | TECHNOLOGY | PROCESS (+T) | Exception approval embedded in criterion 3 → constitutive (§4.2). |
| 6 | CR-D-02.2-001 | PROCESS (+T) | PROCESS (+T) | PROCESS (+T) | Human-review mandate; "remediation or approved exception" in criteria. |
| 7 | CR-D-02.3-001 | PROCESS | PROCESS | PROCESS | Per-report triage/acknowledgement/escalation workflow. |
| 8 | CR-D-03.1-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | CTO sign-off on quarterly review = re-verification, not constitutive. |
| 9 | CR-D-03.2-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | Automated test rejects missing second factor; exception only in Description. |
| 10 | CR-D-03.3-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | RBAC enforcement + negative tests; quarterly review removes stale grants. |
| 11 | CR-D-03.4-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | Deny-by-default config verified by config tests. |
| 12 | CR-D-04.1-001 | PROCESS (+T) | PROCESS | PROCESS (+T) | Recurring triage/containment decisions; built limits secondary (agreed). |
| 13 | CR-D-04.2-001 | PROCESS (+T) | PROCESS (+T) | PROCESS (+T) | Containment playbook + authority + drills constitutive. |
| 14 | CR-D-04.3-001 | PROCESS | PROCESS | PROCESS | Notification workflow: trigger tree, 24h clock, per-recipient submissions. |
| 15 | CR-D-04.4-001 | PROCESS (+T) | PROCESS (+T) | PROCESS (+T) | Executed recovery sequence; restore tooling secondary. |
| 16 | CR-D-05.1-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | Schema constraints, allow-lists, redaction tests. |
| 17 | CR-D-05.2-001 | TECHNOLOGY | TECHNOLOGY (+P) | TECHNOLOGY | TTL/lifecycle jobs satisfy criteria; "approved 30-day period" is adjectival. |
| 18 | CR-D-05.3-001 | PROCESS | PROCESS (+T) | PROCESS | 7-day SLA per-request erasure workflow (rubric §8 exemplar; secondary optional). |
| 19 | CR-D-05.4-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | Automated export pipeline delivers the 48h objective. |
| 20 | CR-D-06.1-001 | PROCESS | PROCESS | PROCESS | Transfer authorisation before production transfer is constitutive. |
| 21 | CR-D-06.2-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | SBOM generation/validation/archival fully automated. |
| 22 | CR-D-06.3-001 | PROCESS | PROCESS | PROCESS | DPA execution, reconciliation, escalation-on-conflict. |
| 23 | CR-D-07.1-001 | PROCESS | PROCESS | PROCESS | Per-feature design-check sequence before merge/release. |
| 24 | CR-D-08.1-001 | CAPABILITY | CAPABILITY | CAPABILITY | Standing workforce awareness (rubric §3 standing note). |
| 25 | CR-D-08.2-001 | CAPABILITY | CAPABILITY | CAPABILITY | Competency matrix + per-role competence; INSPECT of standing ability. |
| 26 | CR-D-09.1-001 | CAPABILITY | CAPABILITY | CAPABILITY | Policy architecture with owners/approvals/review reconciled to evidence. |
| 27 | CR-D-09.2-001 | CAPABILITY (+P) | CAPABILITY (+P) | CAPABILITY (+P) | Human risk-acceptance authority is constitutive (rubric §8 borderline 2). |
| 28 | CR-D-09.4-001 | PROCESS | PROCESS | PROCESS | Update-on-processing-change + per-incident breach decisions. |
| 29 | CR-D-10.2-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | Trail, Object Lock, retention config; retrieval test. |
| 30 | CR-D-10.3-001 | PROCESS | PROCESS | PROCESS | Recurring test cycle with closure approval and management sign-off. |

### PARTE II — Best-Practice Controls (16 BPR)

| # | Rule | Applied | Baseline | Adjudicated | Rationale (one line) |
|---|---|---|---|---|---|
| 31 | BPR-D-01.1-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | IaC settings + negative test; "approved custody" adjectival. |
| 32 | BPR-D-01.2-001 | PROCESS (+T) | TECHNOLOGY | PROCESS (+T) | Exception owner/review record in criterion 3 → constitutive (§4.3). |
| 33 | BPR-D-02.1-001 | PROCESS | PROCESS | PROCESS | The rule IS the recurring scan + reconciliation cycle. |
| 34 | BPR-D-02.2-001 | PROCESS | PROCESS | PROCESS | 72h clock; "remediation or approved exception" in criteria. |
| 35 | BPR-D-03.1-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | Server-side enforcement + matrix; review = re-verification. |
| 36 | BPR-D-03.2-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | Enrolment state + auth/recovery tests. |
| 37 | BPR-D-03.4-001 | TECHNOLOGY | TECHNOLOGY | **PROCESS (+T)** ✱ | Failed-check → remediation-or-exception mapping in criterion 2 → constitutive (§4.6). |
| 38 | BPR-D-04.3-001 | PROCESS | CAPABILITY | **CAPABILITY** ✱ | Standing-artefact rule; owner + approval authority constitutive between events (§4.4). |
| 39 | BPR-D-04.3-002 | PROCESS | PROCESS | PROCESS | Realization = running the quarterly exercise with records. |
| 40 | BPR-D-05.3-001 | PROCESS | PROCESS | PROCESS | Per-decommissioning sanitisation procedure. |
| 41 | BPR-D-07.1-001 | PROCESS | PROCESS | PROCESS | Practice map realized through the per-feature SDLC. |
| 42 | BPR-D-07.2-001 | PROCESS (+T) | TECHNOLOGY | PROCESS (+T) | "Approval where excepted" + retest evidence in criterion 3 → constitutive (§4.5). |
| 43 | BPR-D-09.1-001 | CAPABILITY | CAPABILITY | CAPABILITY | ISMS management cycle: standing governance ability. |
| 44 | BPR-D-10.2-001 | TECHNOLOGY | TECHNOLOGY | TECHNOLOGY | Lifecycle config, archive protection, retrieval tests. |
| 45 | BPR-D-10.3-001 | PROCESS | PROCESS | PROCESS | Recurring assessment: scope → test → findings → retest. |
| 46 | BPR-D-10.3-002 | PROCESS | PROCESS | PROCESS | Assessment-methodology execution with coverage matrix. |

### Distribution after adjudication

| Class | Applied | Baseline | Adjudicated |
|---|---:|---:|---:|
| TECHNOLOGY | 18 | 20 | **17** |
| PROCESS | 23 | 20 | **23** |
| CAPABILITY | 5 | 6 | **6** |
| Total | 46 | 46 | 46 |

(Moves vs applied: BPR-D-04.3-001 PROCESS→CAPABILITY; BPR-D-03.4-001 TECHNOLOGY→PROCESS.)

## 7. Verdict — `FIX_WAVE_NEEDED`

**Fix-wave worklist (2 rules):**

1. **`BPR-D-03.4-001`**: TECHNOLOGY → **PROCESS** (secondary TECHNOLOGY). Reason: exception disposition embedded in Verification Criteria (§4.6). Consistency with the Executor's own CR-D-02.2-001 / BPR-D-01.2-001 / BPR-D-07.2-001 treatment.
2. **`BPR-D-04.3-001`**: PROCESS → **CAPABILITY** (secondary optional). Reason: standing-artefact rule with constitutive ownership/approval authority (§4.4); aligns with CR-D-09.1-001 and the §3 standing note.

Per rule, the fix touches 5 locations: Doc18 card fields 25/26, Anexo A rows for that ID, Anexo D (regenerate + counts), `control_set.yaml` entry, `12_Rules_Catalog.xlsx` cols 17/18.

**Non-fix observations:** (a) my baseline itself shifted on 5 rules under v1.2's sharpened constitutive-step test — 4 of those shifts land on the Executor's side (CR-D-01.3-001 flipped to the applied TECHNOLOGY; CR-D-02.1-001, BPR-D-01.2-001, BPR-D-07.2-001 flipped to the applied PROCESS), evidence the tag wave applied v1.1/v1.2 more consistently than the v1.0-era baseline; (b) the two genuine defects share a root cause: exception-handling steps *inside criteria blocks* were classified T in the BPR cluster (03.4) while the identical pattern was classified P elsewhere, and one P/C call (04.3-001) drifted from its structural twin (09.1-001).

## 8. Files referenced

- `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` (v1.2 — §3 tree, tie-breaks, §3 standing note)
- `00_METHODOLOGY/validation/REALIZATION_CLASS_RUBRIC_VALIDATOR_REPORT_v0.md` (baseline §6)
- `02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/Doc18_Rules_Catalog.md` (cards L268/428/3029/3494/3588/3968; Anexo A L4440-4688; Anexo D L4782-4790)
- `02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/control_set.yaml` (46 `realization_class` entries)
- `02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/12_Rules_Catalog.xlsx` (`Rules_Catalog` cols 17/18)

*Validator, 2026-09-05. No files outside this report were modified.*
