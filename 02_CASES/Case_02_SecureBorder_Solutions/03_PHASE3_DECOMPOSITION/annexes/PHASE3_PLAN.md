---
document_id: AEGIS-P3-PLAN-02
title: Phase 3 Implementation Plan
phase: 3
version: 1.0
created: 2026-04-30
updated: 2026-04-30
author: Security Architect
status: DRAFT
---

# Phase 3 Implementation Plan — Case 02: SecureBorder Solutions

**Case:** SecureBorder Solutions B.V.
**Complexity:** High (4 regulations: GDPR, CRA, NIS 2, AI_Act)
**Phase 2 Exit:** ✅ PASS (53 rules, 8 tensions resolved, 38 goals)
**Phase 3 Entry:** ✅ VERIFIED (workflow_gate.py passed)

---

## 1. PHASE 3 SCOPE

### Input from Phase 2

| Artifact | Count | Notes |
|----------|-------|-------|
| Rules (Compliance) | 38 | CR-D-XX.X-NNN format |
| Rules (Best Practice) | 15 | BPR-D-XX.X-NNN format (7 Security + 8 AI-Specific) |
| Privacy Goals | 9 | PG-D-XX.X-NNN |
| Security Goals | 29 | SG-D-XX.X-NNN |
| Strategic Tensions | 8 | All resolved (2 CRITICAL, 2 HIGH, 3 MEDIUM, 1 LOW) |
| Sub-Domains Covered | 35/38 (92.1%) | Gaps: D-02.4, D-06.4, D-08.3 |

### Case-Specific Complexity Factors

| Factor | Impact on Phase 3 |
|--------|-------------------|
| AI_Act High-Risk (border control) | AI-specific use cases, conformity assessment, post-market monitoring |
| Biometric data (GDPR Art. 9) | Enhanced data protection use cases |
| NIS 2 Essential Entity Supplier | 24h incident notification, management liability |
| 99.99% Uptime SLA | Strict availability requirements |
| Edge AI + Cloud architecture | Hybrid architectural nodes |
| ISO 27001 Certified | Inherited controls can be leveraged |

---

## 2. DOCUMENTS TO CREATE

| # | Document ID | Document Name | Estimated Effort | Dependencies |
|---|-------------|---------------|-----------------|--------------|
| 1 | 13 | Use_Cases_Catalog.md | High | Rules Catalog, Goals |
| 2 | 14 | Architectural_Nodes.md | Medium | Company Context |
| 3 | 15 | Requirements_Allocation.md | Medium | Use Cases, Nodes |
| 4 | 16 | Compliance_Gates_Report.md | Medium | Requirements Allocation |
| 5 | 17 | Functional_Tree.md | High | All above |
| 6 | 23 | Functional_Requirements.md | High | Use Cases, Rules, Goals |
| 7 | 24 | Non_Functional_Requirements.md | High | Goals, Rules |
| 8 | 25 | Risk_Analysis.md | High | FRs, Use Cases |
| 9 | 22 | Traceability_Matrix.xlsx | Medium | All above |

---

## 3. IMPLEMENTATION ORDER

### Step 1: Use Cases Catalog (Doc 13)

**Goal:** Define use cases that realize all 53 rules and 38 goals.

**Expected UC Categories:**
| Category | Est. Count | Notes |
|----------|-----------|-------|
| DP (Data Protection) | 8-10 | Biometric data, GDPR Art. 9, erasure, portability |
| SEC (Security Operations) | 8-10 | Incident response, monitoring, 24h notification |
| IAM (Identity & Access) | 5-7 | Biometric authentication, role-based access |
| DEV (Secure Development) | 4-6 | SDLC, testing, AI model validation |
| GOV (Governance) | 5-7 | DPIA, FRIA, conformity assessment, ISMS |
| AI (AI-Specific) | 5-7 | Post-market monitoring, human oversight, data governance |
| TRN (Training) | 2-3 | Security awareness, AI literacy |

**Total Estimated UCs:** 37-50

**Key UCs Specific to SecureBorder:**
- Biometric template enrollment and verification
- AI model conformity assessment (AI_Act)
- Post-market AI monitoring (AI_Act)
- 24h incident notification to CSIRT (NIS 2)
- Edge AI model update workflow
- Judicial watchlist integration
- Airport operations continuity (99.99% uptime)

### Step 2: Architectural Nodes (Doc 14)

**Goal:** Define Process, ITSystem, HumanRole nodes.

**Expected Nodes:**
| Type | Est. Count | Examples |
|------|-----------|----------|
| PROCESS | 8-12 | Incident response, DPIA, conformity assessment, model validation |
| IT_SYSTEM | 6-10 | GuardianGate eGate kiosk, Edge AI engine, Cloud model server, Biometric matcher |
| HUMAN_ROLE | 5-8 | Border guard, AI system operator, DPO, CISO, Notified body auditor |

### Step 3: Requirements Allocation (Doc 15)

**Goal:** Map all 53 rules to architectural nodes.

**Allocation Rules:**
- Every rule → at least one node
- Rules may map to multiple nodes (SHARED)
- Each allocation has verification method

### Step 4: Compliance Gates (Doc 16)

**Goal:** Define verification checkpoints.

**Expected Gates:** ~35-50 (one per rule-node allocation)

### Step 5: Functional Tree (Doc 17)

**Goal:** Hierarchical functional breakdown.

**Structure:**
```
ROOT: SecureBorder Compliance Architecture
├── L1: Border Control Operations
│   ├── L2: eGate Kiosk Processing
│   │   └── L3: Biometric verification, AI inference
│   └── L2: Watchlist Integration
├── L1: Data Protection & Privacy
│   ├── L2: Biometric Data Lifecycle
│   └── L2: AI Data Governance
├── L1: Security Operations
│   ├── L2: Incident Response (24h)
│   └── L2: Continuous Monitoring
├── L1: AI Governance
│   ├── L2: Conformity Assessment
│   └── L2: Post-Market Monitoring
└── L1: Governance & Compliance
    ├── L2: ISMS (ISO 27001)
    └── L2: Regulatory Reporting
```

### Step 6: Functional Requirements (Doc 23)

**Goal:** Derive technology-agnostic FRs from Use Cases + Rules + Goals.

**Estimated FRs:** 50-70 (higher than Case 01's 60 due to AI-specific requirements)

**FR Domains:**
| Domain | Est. Count | Notes |
|--------|-----------|-------|
| IAM | 8-12 | Biometric auth, role-based access |
| DP | 10-14 | Biometric data protection, Art. 9 safeguards |
| SEC | 10-14 | Incident response, monitoring, 24h notification |
| DEV | 6-8 | AI model validation, secure SDLC |
| GOV | 8-12 | DPIA, FRIA, conformity assessment |
| AI | 6-10 | Human oversight, data governance, post-market |
| TRN | 2-4 | Security awareness, AI literacy |

### Step 7: Non-Functional Requirements (Doc 24)

**Goal:** Derive measurable quality attributes from Goals + Rules.

**Estimated NFRs:** 40-55

**NFR Categories:**
| Category | Est. Count | Notes |
|----------|-----------|-------|
| CONF (Confidentiality) | 6-8 | Biometric template protection |
| INT (Integrity) | 5-7 | AI model integrity, data integrity |
| AVAIL (Availability) | 5-7 | 99.99% uptime, disaster recovery |
| PRIV (Privacy) | 8-10 | GDPR Art. 9, data minimization |
| ACC (Accountability) | 5-7 | Audit trails, logging |
| COMP (Compliance) | 8-12 | Multi-regulation compliance |
| AI (AI-Specific) | 5-8 | Accuracy, fairness, human oversight |

### Step 8: Risk Analysis (Doc 25)

**Goal:** STRIDE + LINDDUN + AI-specific threat modeling.

**Expected Threats:** 50-70 (higher than Case 01's 42 due to AI and biometric risks)

**Risk Categories:**
| Category | Est. Count | Notes |
|----------|-----------|-------|
| STRIDE | 35-45 | Standard threat modeling |
| LINDDUN | 8-12 | Privacy threats for biometric data |
| AI-Specific | 5-10 | Model poisoning, adversarial attacks, bias |

### Step 9: Traceability Matrix (Doc 22)

**Goal:** Full chain: Regulation → Clause → Rule → NFR → FR → UC → Gate.

**Expected:** ~100-150 traceability links

---

## 4. QUALITY TARGETS

| Metric | Target | Notes |
|--------|--------|-------|
| Coverage | ≥ 95% | All 53 rules satisfied by FRs |
| Traceability | ≥ 95% | All FRs have UC + NFR source |
| Risk Mitigation | 100% | All HIGH/CRITICAL risks mitigated |
| Security | ≥ 80% | BPR rules covered by FRs |
| Quality Gate Score | ≥ 85% | Target for High complexity |

---

## 5. WORKFLOW ENFORCEMENT

### Before Each Document
```bash
python 01_IMPLEMENTATION_TOOLS/evals/workflow_gate.py \
  --check --file "<filename>" --case "Case_02_SecureBorder_Solutions"
```

### After Each Document
```bash
python 01_IMPLEMENTATION_TOOLS/evals/validate_doc.py \
  --file "<filename>" --case "Case_02_SecureBorder_Solutions"
```

### Log Each Change
```bash
python 01_IMPLEMENTATION_TOOLS/scripts/log_change_cli.py \
  --type DOCUMENTATION --impact High \
  --title "Created Phase 3: <document>" \
  --desc "Description" \
  --files "<file_path>" \
  --case-specific "Case_02_SecureBorder_Solutions"
```

---

## 6. ESTIMATED TIMELINE

| Step | Document | Effort | Cumulative |
|------|----------|--------|------------|
| 1 | Use Cases Catalog | High | 1 |
| 2 | Architectural Nodes | Medium | 2 |
| 3 | Requirements Allocation | Medium | 3 |
| 4 | Compliance Gates | Medium | 4 |
| 5 | Functional Tree | High | 5 |
| 6 | Functional Requirements | High | 6 |
| 7 | Non-Functional Requirements | High | 7 |
| 8 | Risk Analysis | High | 8 |
| 9 | Traceability Matrix | Medium | 9 |

---

## 7. RISK FACTORS

| Risk | Impact | Mitigation |
|------|--------|------------|
| AI_Act requirements unclear | Medium | Use AI_Act reference text, focus on Annex III |
| Biometric data complexity | High | Leverage GDPR Art. 9 guidance, ISO 27001 controls |
| 24h NIS 2 notification | Medium | Model after Case 01's 72h workflow, tighten SLA |
| Edge AI architecture | Medium | Define clear boundary between edge and cloud |
| Scope creep (4 regulations) | High | Focus on rules catalog, don't add unscoped requirements |

---

**Plan Created:** 2026-04-04
**Status:** READY FOR APPROVAL
**Next Step:** Begin Step 1 — Use Cases Catalog
