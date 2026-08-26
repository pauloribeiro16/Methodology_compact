# 02_CASES — AEGIS Implementation Cases

Case studies implementing the AEGIS methodology across different complexity levels.

---

## 📁 Case Studies

| Case | Name | Complexity | Status |
|------|------|------------|--------|
| [`Case_01_TinyTask_SaaS/`](./Case_01_TinyTask_SaaS/) | TinyTask Lda. | Low | Phase 1 Complete |
| [`Case_02_Medium_Complexity/`](./Case_02_Medium_Complexity/) | TBD | Medium | TBD |
| [`Case_03_OmniBank_Financial/`](./Case_03_OmniBank_Financial/) | TBD | High | TBD |

---

## 📊 Global Status

| Metric | Value |
|--------|-------|
| Total Cases | 3 |
| Completed Phases | 1 (Phase 1 - TinyTask) |
| In Progress | 0 |
| Pending | 2 cases |

---

## 📁 Case Structure Template

```
Case_XX_Name/
│
├── README.md                     # Case overview
├── PROJECT_STATE.md              # Current state and progress
│
├── 00_COMMON/                    # Shared across all phases
│   ├── 00_Taxonomy_Reference.md
│   ├── 01_Company_Context.md
│   ├── 02_Regulatory_Mapping_Master.md
│   └── 03_Design_Decisions_Log.md
│
├── 01_PHASE1_CONTEXT/            # Phase 1: Contextual Definition
│   ├── README.md
│   ├── 04_Company_Context_Assessment.md
│   ├── 05_Regulatory_Applicability.md
│   ├── 06_Clause_Mapping_Matrix.md
│   ├── 07_Structured_Compliance_Matrix.md
│   └── outputs/
│
├── 02_PHASE2_RULES/              # Phase 2: Elaboration & Secure Design
│   ├── README.md
│   ├── 08_Obligation_Derivation.md
│   ├── 09_Strategic_Tensions_Report.md
│   ├── 10_Privacy_Security_Goals.md
│   ├── 11_Rules_Catalog.md
│   └── outputs/
│
├── 03_PHASE3_DECOMPOSITION/      # Phase 3: Decomposition
│   ├── README.md
│   ├── 13_Use_Cases_Catalog.md
│   ├── 14_Architectural_Nodes.md
│   ├── 15_Requirements_Allocation.md
│   ├── 16_Compliance_Gates_Report.md
│   ├── 17_Functional_Tree.md
│   └── outputs/
│
└── 99_ARCHIVES/                  # Archived documents
```

---

## 📋 Global Documents

- **[GLOBAL_PROJECT_STATE.md](./GLOBAL_PROJECT_STATE.md)** — Portfolio-wide status
- **[CHANGE_LOG_CENTRAL.md](./CHANGE_LOG_CENTRAL.md)** — Central change log
- **[SESSION_HANDOFF.md](./SESSION_HANDOFF.md)** — Session context and handoff

---

## 🔧 Running Validation

```bash
# Validate all cases
for case in Case_*/; do
    python ../01_IMPLEMENTATION_TOOLS/lints/run_all_lints.py --case "$(basename $case | sed 's/Case_[0-9]*_//' | sed 's/_/ /g')"
done
```

---

## 🔗 Related

- **[00_METHODOLOGY/](../00_METHODOLOGY/)** — Core methodology
- **[01_IMPLEMENTATION_TOOLS/](../01_IMPLEMENTATION_TOOLS/)** — Validation tools

---

**Last Updated:** 2026-04-02
