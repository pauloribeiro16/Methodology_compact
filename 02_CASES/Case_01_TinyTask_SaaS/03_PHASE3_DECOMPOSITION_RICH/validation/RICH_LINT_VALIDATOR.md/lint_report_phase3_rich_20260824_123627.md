# ARM Lint Report — phase3_rich — 03_PHASE3_DECOMPOSITION_RICH

**Timestamp:** 2026-08-24T12:36:27.227393

## Summary

| Metric | Count |
|--------|-------|
| ✅ Passed | 6 |
| ❌ Failed | 1 |
| ⚠️ Warnings | 9 |
| **Total** | **7** |

## Detailed Results

### ❌ Use Cases Catalog (Doc 13)

**Errors:**
- Missing Packages/Use Cases section (expected ## 5. PACKAGES or ## 5. USE CASES)
- Missing Use Cases/Packages section (expected ## 6. USE CASES or ## 6. PACKAGES)

**Warnings:**
- ⚠️ Only 0 of 42 UCs have actors defined
- ⚠️ Found 42 orphan UCs without relationships: UC-3.3.1, UC-5.6.1, UC-1.1.2, UC-3.6.1, UC-3.4.1

**Metrics:**
- `total_use_cases`: 42
- `total_packages`: 6
- `priority_distribution`: {}
- `with_actors`: 0
- `with_regulation`: 0
- `with_description`: 35
- `relationships_include`: 0
- `relationships_extend`: 0
- `variability_specializations`: 0
- `variability_alternatives`: 0
- `variability_options`: 0
- `orphan_use_cases`: 42
- `documents_found`: 1

### ✅ Use Case Relationships (Doc 13a)

**Warnings:**
- ⚠️ Insufficient data: no relationships found (Phase 3 may not be started)

**Metrics:**
- `total_relationships`: 0
- `include_relationships`: 0
- `refine_relationships`: 0
- `extend_relationships`: 0
- `coexistence_violations`: 0
- `level_violations`: 0
- `orphan_use_cases`: 0
- `documents_found`: 1
- `has_sufficient_data`: False

### ✅ Use Case Variability (Doc 13b)

**Warnings:**
- ⚠️ Insufficient data: no variability items found (Phase 3 may not be started)

**Metrics:**
- `total_specializations`: 0
- `total_alternatives`: 0
- `total_options`: 0
- `specializations_with_regulation`: 0
- `alternatives_with_criteria`: 0
- `options_with_condition`: 0
- `regulations_with_variants`: 2
- `documents_found`: 1
- `has_sufficient_data`: False

### ✅ Architectural Nodes (Doc 14)

**Warnings:**
- ⚠️ Insufficient data: no nodes found (Phase 3 may not be started)

**Metrics:**
- `total_nodes`: 0
- `by_type`: {}
- `by_track`: {}
- `with_source_uc`: 0
- `documents_found`: 1
- `has_sufficient_data`: False

### ✅ Requirements Allocation (Doc 15)

**Warnings:**
- ⚠️ No use case source references found. Each allocation SHOULD trace to a UC.

**Metrics:**
- `total_allocations`: 103
- `unique_rules_allocated`: 43
- `unique_nodes_allocated`: 0
- `unique_uc_sources`: 0
- `by_verification`: {}
- `by_allocation_type`: {}
- `documents_found`: 1
- `has_sufficient_data`: True

### ✅ Compliance Gates (Doc 16)

**Warnings:**
- ⚠️ Insufficient data: no gates found (Phase 3 may not be started)

**Metrics:**
- `total_gates`: 0
- `by_status`: {}
- `by_verification`: {}
- `with_node_ref`: 0
- `with_uc_ref`: 0
- `with_evidence`: 0
- `documents_found`: 1
- `has_sufficient_data`: False

### ✅ Functional Tree (Doc 17)

**Warnings:**
- ⚠️ No node ID references found in tree
- ⚠️ Insufficient data: no tree nodes found (Phase 3 may not be started)

**Metrics:**
- `total_nodes_in_tree`: 0
- `levels_found`: {'L0': 11, 'L1': 16, 'L2': 43, 'ROOT': 11}
- `mermaid_diagrams`: 1
- `subdomains_covered`: 0
- `uc_sources`: 0
- `track_tags`: 0
- `documents_found`: 1
- `has_sufficient_data`: False

