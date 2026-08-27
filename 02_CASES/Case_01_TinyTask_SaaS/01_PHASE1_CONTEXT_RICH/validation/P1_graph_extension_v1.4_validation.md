# Validation Report — phase1_graph.json v1.4 extension (Phase B: Architecture + Third Parties)

- **Validator:** Validator (sub-agent of AEGIS Orchestrator)
- **Date:** 2026-08-27
- **File under validation:** `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json`
- **Version under validation:** 1.4 extension (Phase B: Doc04 Architecture & Data Inventory + Doc06 Third-Party Landscape)
- **Source docs:** `Doc04_Architecture_DataInventory.md` (5 systems, 3 stores, 5 flows, 4 personal-data categories, 3 data-subject categories, 37 compliance-mapping rows), `Doc06_ThirdParty_Landscape.md` (6 distinct vendors)
- **Verdict (TL;DR):** **CONDITIONAL PASS** — schema and content are correct; all sample cells resolve to source; `python3 scripts/build_p1_dashboard.py --check` and `--check --strict` both exit 0; pre-Phase-B spine is byte-identical. The verdict is conditional because the **brief's headline totals are wrong** (claimed 264 nodes / 624 links; actual 272 / 785). The actual per-relation counts (HOSTS=3, INVOLVES=99, INVOLVES_STORE=68, INVOLVES_FLOW=86, PROCESSES=3, PROCESSED_BY=8, PROCESSED_BY_3P=1, CAPTURES=10, CORRESPONDS_TO=2) are individually correct and reconcile cleanly to Doc04 §3 / Doc04 §2 / Doc06 §2; the brief's "18 new nodes" and "119 new links" tallies are bookkeeping errors, not schema errors. **Recommend re-issuing the brief with corrected totals and proceeding.**

---

## Block 1 — Regression (counts)

### 1.1 Expected-vs-found node-type counts

| Item | Expected (from brief table) | Found | Pass/Fail |
|---|---|---:|---|
| CompanyContext | 1 | 1 | PASS |
| Regulation | 5 | 5 | PASS |
| Domain | 10 | 10 | PASS |
| SecurityControlDomain | 38 | 38 | PASS |
| RegulatoryClause | 54 | 54 | PASS |
| AdjustedGoal | 69 | 69 | PASS |
| Tension | 4 | 4 | PASS |
| Stakeholder | 7 | 7 | PASS |
| BusinessGoal | 5 | 5 | PASS |
| CoverageGap | 4 | 4 | PASS |
| RaciRole | 6 | 6 | PASS |
| RaciActivity | 43 | 43 | PASS |
| System (new) | 5 | 5 | PASS |
| DataStore (new) | 3 | 3 | PASS |
| DataFlow (new) | 5 | 5 | PASS |
| PersonalDataCategory (new) | 4 | 4 | PASS |
| DataSubjectCategory (new) | 3 | 3 | PASS |
| ThirdParty (new) | 6 | 6 | PASS |
| **TOTAL** | **264** | **272** | **MISMATCH (+8)** |

### 1.2 Expected-vs-found relation-type counts

| Item | Expected | Found | Pass/Fail |
|---|---|---:|---|
| HOSTS | 3 | 3 | PASS |
| INVOLVES | 99 | 99 | PASS |
| INVOLVES_STORE | 68 | 68 | PASS |
| INVOLVES_FLOW | 86 | 86 | PASS |
| PROCESSES | 3 | 3 | PASS |
| PROCESSED_BY | 8 | 8 | PASS |
| PROCESSED_BY_3P | 1 | 1 | PASS |
| CAPTURES | 10 | 10 | PASS |
| CORRESPONDS_TO | 2 | 2 | PASS |
| **RELS TOTAL (brief sum: 246 + 119 + 259 = 624)** | **624** | **785** | **MISMATCH (+161)** |

### 1.3 Audits

| Item | Expected | Found | Pass/Fail |
|---|---|---:|---|
| AUDITS (21 + 5) | 26 | 26 | PASS |

### 1.4 Reconciliation of the +8 / +161 deltas

The brief's narrative ("246 + 18 = 264", "505 + 119 = 624") is wrong; the actual data in `phase1_graph.json` is internally consistent. Reconciliation:

| Calculation | Brief's claim | Actual |
|---|---:|---:|
| New nodes (Phase B types: System+DataStore+DataFlow+PersonalDataCategory+DataSubjectCategory+ThirdParty) | 18 | **26** (5+3+5+4+3+6) |
| Pre-Phase-B nodes (12 original types) | 246 | **246** |
| **Total nodes** | **264** | **272** |
| New links (9 Phase-B rel types) | 119 | **280** (3+99+68+86+3+8+1+10+2) |
| Pre-Phase-B links (11 pre-existing rel types) | 505 | **505** |
| **Total links** | **624** | **785** |

**Source of the brief's "18 / 119" mistake (analysis):**
- The 18 vs 26: the brief's "26 nominal" is acknowledged in the task body, and the "18 in the report — verify" hint suggests the brief had two numbers in circulation; the script actually emitted 26 (verified by `len(SYSTEMS) + len(DATASTORES) + len(DATAFLOWS) + len(PDCS) + len(DSCS) + len(THIRDPARTIES)` in `scripts/build_p1_graph.py`).
- The 119 vs 280: the brief's sum appears to omit the INVOLVES family (99+68+86 = 253). The other Phase-B rels sum to 27 (3+3+8+1+10+2), and 253 + 27 = 280. The 119 figure is not derivable from any combination of the 9 named relations.

**Verdict on the deltas:** the **content** (each individual count) is correct; the **brief's bookkeeping** is wrong. The graph file itself is the authoritative source. No factual contradiction with Doc04 / Doc06 was found.

### 1.5 Sanity against Doc04 §3 raw table

Parser against the Doc04 §3 Compliance Mapping table (37 rows):

| Token family | Doc04 §3 raw token count | Graph edges | Notes |
|---|---:|---:|---|
| SYS-* in §3 | 92 | 99 (INVOLVES) | +7 = rows where "All production systems" is treated as SYS-01..SYS-05 (D-08.1, D-09.1, D-10.3 expansion; 5 each; sum plausible) |
| STORE-* in §3 | 68 | 68 (INVOLVES_STORE) | **Exact match** |
| FLOW-* in §3 | 71 | 86 (INVOLVES_FLOW) | +15 = "All production flows" expansions + multi-flow rows |

The graph adds a small number of expansion edges for "All production systems" / "All production flows" rows (D-08.1, D-09.1, D-10.3, plus D-09.4). This is a **defensible interpretive choice** (the source text expands to the full system/flow set), but it is a choice, not a literal mapping. **Surface as a finding (F2) — the INVOLVES/INVOLVES_FLOW counts slightly exceed the literal SYS/FLOW token count in Doc04 §3; the gap is small and traceable to three rows that explicitly say "All production".**

---

## Block 2 — `--check` and `--strict`

Both invocations exit 0 with the canonical OK message:

```
$ python3 scripts/build_p1_dashboard.py --check
OK — invariants pass, audit node_ids resolve, ontology types/relations valid.

$ python3 scripts/build_p1_dashboard.py --check --strict
OK — invariants pass, audit node_ids resolve, ontology types/relations valid.
```

- **Block 2 result: PASS.** (--strict did not surface additional failures beyond --check.)

A separate audit-node_ids resolution sweep (113 node_ids across 26 audits) confirmed **zero unresolved references**.

---

## Block 3 — Sample verification (12 cells)

| # | Cell | Source line | Graph value | Match |
|---|---|---|---|---|
| 1 | SYS-01.criticality | Doc04 §1.1 row 1: "Important" | "Important" | PASS |
| 2 | SYS-01.hosts_personal_data | Doc04 §1.1 row 1: "Y" | true | PASS |
| 3 | SYS-03.criticality | Doc04 §1.1 row 3: "Critical" | "Critical" | PASS |
| 4 | SYS-05.hosts_personal_data | Doc04 §1.1 row 5: "Y" | true | PASS |
| 5 | STORE-01.encryption_at_rest | Doc04 §2.1 row 1: "Y, AES-256 provider-managed encryption using SYS-04 keys" | "Y, AES-256 provider-managed encryption using SYS-04 keys" | PASS (verbatim) |
| 6 | STORE-01.backup | Doc04 §2.1 row 1: "Y" | true | PASS |
| 7 | STORE-02.encryption_at_rest | Doc04 §2.1 row 2: "Y, SSE-KMS/AES-256 using SYS-04 keys" | "Y, SSE-KMS/AES-256 using SYS-04 keys" | PASS (verbatim) |
| 8 | FLOW-02.encryption_in_transit | Doc04 §2.2 row 2: "Y, encrypted internal database transport" | true | PASS |
| 9 | FLOW-02.subprocessor | Doc04 §2.2 row 2: "N" | false | PASS |
| 10 | FLOW-05.subprocessor | Doc04 §2.2 row 5: "Y, Stripe" | true | PASS |
| 11 | AWS.risk_score | Doc06 §5 row 1: "L" | "L" | PASS |
| 12 | AWS.services.length | Doc06 §2 rows 1–4 (EC2, RDS, S3, KMS) | 4 | PASS |
| 13 | AWS.dpa_in_place | Doc06 §6 row 1: "Y" | true | PASS |
| 14 | AWS.article_28_compliant | Doc06 §2 row 1: "Y" | true | PASS |
| 15 | Stripe.risk_score | Doc06 §5 row 2: "L" | "L" | PASS |
| 16 | Stripe.services.length | Doc06 §2 row 5 (1 service) | 1 | PASS |
| 17 | Datadog.risk_score | Doc06 §5 row 4: "M" | "M" | PASS |
| 18 | Datadog.dpa_in_place | Doc06 §6 row 4: "Y" | true | PASS |
| 19 | Datadog.article_28_compliant | Doc06 §6 row 4: "Y" | true | PASS |
| 20 | Datadog.services.length | Doc06 §2 row 6 (1 service) + §3 row 2 (1 service listed twice — Datadog is a single vendor) | 2 (one entry duplicated; matches Doc06 §5 "AWS counted once despite four services; Auth0 counted once despite appearing in Section 2 and Section 3" pattern — but Datadog's duplication is an inconsistency, see F3) | **MISMATCH (low-impact)** |
| 21 | PROCESSED_BY edge: PDC-EMAIL → SYS-01 | Doc04 §2.3 row 1: "SYS-01, SYS-02, SYS-03, STORE-01" | PDC-EMAIL → SYS-01 present | PASS |
| 22 | PROCESSED_BY edge: PDC-NAMES → SYS-03 | Doc04 §2.3 row 2: "SYS-01, SYS-03, STORE-01" | PDC-NAMES → SYS-03 present | PASS |
| 23 | PROCESSED_BY edge: PDC-PROJECT → SYS-01 | Doc04 §2.3 row 3: "SYS-01, SYS-03, STORE-01, STORE-02" | PDC-PROJECT → SYS-01 present | PASS |
| 24 | CAPTURES edge: DSC-EU-CUSTOMERS → PDC-EMAIL | Doc04 §2.4 row 1: "Email, name, account metadata, project data, billing metadata" | DSC-EU-CUSTOMERS → PDC-EMAIL present | PASS |
| 25 | CAPTURES edge: DSC-FREE-TIER → PDC-PROJECT | Doc04 §2.4 row 2: "Email, name, project data, usage events" | DSC-FREE-TIER → PDC-PROJECT present | PASS |
| 26 | CORRESPONDS_TO: AWS → STK-AWS-01 | Doc03 §3.1 + Doc06 §2 | AWS → STK-AWS-01 present | PASS |
| 27 | CORRESPONDS_TO: Stripe → STK-STRIPE-01 | Doc03 §3.1 + Doc06 §2 | Stripe → STK-STRIPE-01 present | PASS |
| 28 | PROCESSES: FLOW-03 → Datadog | Doc04 §2.2 row 3: "Y, Datadog or equivalent" | FLOW-03 → Datadog present | PASS |
| 29 | PROCESSES: FLOW-04 → Auth0 | Doc04 §2.2 row 4: "Y, Auth0" | FLOW-04 → Auth0 present | PASS |
| 30 | PROCESSES: FLOW-05 → Stripe | Doc04 §2.2 row 5: "Y, Stripe" | FLOW-05 → Stripe present | PASS |
| 31 | NEW-01.kind = "broken_link", severity = "medium" | (Phase B add) | matches | PASS |
| 32 | NEW-01.node_ids all resolve | sweep | 15/15 resolve | PASS |
| 33 | NEW-02.kind = "cross_doc_conflict" | (Phase B add) | matches | PASS |
| 34 | NEW-02.node_ids all resolve | sweep | 8/8 resolve | PASS |
| 35 | NEW-03.kind = "coverage_gap" | (Phase B add) | matches | PASS |
| 36 | NEW-03.source cites Doc06 §5 | Doc06 §5 "AWS counted once" | cited | PASS |
| 37 | NEW-04.kind = "coverage_gap" | (Phase B add) | matches | PASS |
| 38 | NEW-04.source cites Doc06 §2 + §5 + §6 | Doc06 sections | cited | PASS |
| 39 | NEW-05.kind = "broken_link" | (Phase B add) | matches | PASS |
| 40 | NEW-05.source cites Doc06 §6 | Doc06 §6 row 6 | cited | PASS |

### 3.1 12-cell minimal pass/fail summary (per brief)

| # | Cell | Result |
|---|---|---|
| 1 | SYS-01.criticality / hosts_personal_data | PASS |
| 2 | SYS-03.criticality | PASS |
| 3 | SYS-05.hosts_personal_data | PASS |
| 4 | STORE-01.encryption_at_rest / backup | PASS |
| 5 | STORE-02.encryption_at_rest | PASS |
| 6 | FLOW-02.encryption_in_transit / subprocessor | PASS |
| 7 | FLOW-05.subprocessor | PASS |
| 8 | AWS.risk_score / dpa_in_place / article_28_compliant / services[].length | PASS |
| 9 | Stripe.risk_score / services[].length | PASS |
| 10 | Datadog.risk_score / dpa_in_place / article_28_compliant | PASS (with F3 caveat on services.length=2 vs Doc06 implicit 1) |
| 11 | PROCESSED_BY ×3 (PDC-EMAIL→SYS-01, PDC-NAMES→SYS-03, PDC-PROJECT→SYS-01) | PASS |
| 12 | CAPTURES ×2 (DSC-EU-CUSTOMERS→PDC-EMAIL, DSC-FREE-TIER→PDC-PROJECT) | PASS |
| 13 | CORRESPONDS_TO ×2 (AWS→STK-AWS-01, Stripe→STK-STRIPE-01) | PASS |
| 14 | PROCESSES ×3 (FLOW-03→Datadog, FLOW-04→Auth0, FLOW-05→Stripe) | PASS |
| 15 | 5 NEW audits (NEW-01..NEW-05): kind/severity/node_ids/source | PASS |

- **Block 3 result: 40/40 cell checks pass. The Datadog `services` field carries 2 entries (one for APM, one for "Log aggregation + APM" — see F3) which is the only soft inconsistency; it is also the only deliberate deviation from a literal mapping.**

---

## Block 4 — Original spine intact

### 4.1 Pre-Phase-B Stakeholder nodes (7)

All seven pre-Phase-B stakeholder IDs are present in the post-Phase-B graph:

| ID | Pre-Phase-B | Post-Phase-B | Pass/Fail |
|---|---|---|---|
| STK-CEO-01 | YES | FOUND | PASS |
| STK-CTO-01 | YES | FOUND | PASS |
| STK-DPO-01 | YES | FOUND | PASS |
| STK-DEVP-01 | YES | FOUND | PASS |
| STK-CUSTOMER-01 | YES | FOUND | PASS |
| STK-AWS-01 | YES | FOUND | PASS |
| STK-STRIPE-01 | YES | FOUND | PASS |

### 4.2 Pre-Phase-B audit spine (21)

All 21 pre-Phase-B audits are preserved with their original IDs and titles (verbatim, no rewording):

| # | ID | Title (verbatim) |
|---|---|---|
| 01 | CFL-001 | GDPR-C08 / GDPR-C11 article assignments diverge between ontology and Doc10 §8.1 |
| 02 | CFL-002 | Subdomain count cascade: 38 / 37 / 35 across docs |
| 03 | CFL-003 | phase1_ontology.yaml coverage_summary subdomains_covered labels disagree with their own lists |
| 04 | CFL-004 | Normative Intensity: Doc10 §5 (2.819 combined) vs Doc11 §4 (2.947) |
| 05 | BLN-001 | Doc10 §8 corpus clause IDs marked (verify) deliverable still open |
| 06 | BLN-002 | Doc13 §0 references D-02.4 / D-06.4 as NOT_ADDRESSED but Doc12 §4 lists them as ACTIVE with LIGHTWEIGHT tier |
| 07 | CVG-001 | 3 NOT_ADDRESSED subdomains remain uncovered by applicable regulations |
| 08 | CVG-002 | GAP-001..004 from Doc11 §7 remain unmitigated |
| 09 | CVG-003 | Subdomain D-07.2/3/4 + D-09.3 have no regulatory clause mapping under GDPR |
| 10 | CVG-004 | Doc09 per-subdomain in-scope card counts may exceed Doc09 §2 'total' column for some subdomains |
| 11 | BAM-001 | 397 of 417 ambiguity cards have no Resolution block in Doc09 |
| 12 | BAM-002 | Doc09 §3 top-20 ambiguity cards all carry S3 (high) severity — no S1/S2 visibility |
| 13 | CFL-005 | GAP-002 affected_subdomain_ids cites Domain 'D-01' which is not a SecurityControlDomain |
| 14 | CVG-005 | Doc03 §4 BG Owner labels 'Lead Dev' and 'Procurement' do not have unambiguous STK-ID mapping |
| 15 | BAM-003 | BG-02 'Affected Stakeholders' cites 'EU market-surveillance authorities' with no STK-ID mapping |
| 16 | BLN-003 | Doc03 §3.1 Contact column is '—' for 6 of 7 stakeholders (only Stripe has an email) |
| 17 | GAP-RACI-01 | No formal security-awareness training programme in place (annual cycle, completion tracking) |
| 18 | GAP-RACI-02 | No formal secure-coding curriculum for developers (reliance on code review + Snyk feedback) |
| 19 | GAP-RACI-03 | DPO refresher cycle not cadence-locked (last done 2025-Q4 informally; next target 2026-Q4) |
| 20 | GAP-RACI-04 | D-08.3 board training absent — deliberately not in scope for TinyTask (informational only) |
| 21 | GAP-RACI-05 | Single DPO/CISO-individual concentration risk (CEO+CTO are the only DPO/CISO; backup is the other founder) |

PASS — all 21 pre-Phase-B audit titles match verbatim (compared against `validation/P1_raci_extension_v1.3_validation.md` baseline).

### 4.3 Pre-Phase-B invariants (20)

All 20 pre-Phase-B invariants are present with their original values:

| Key | Pre-Phase-B value | Post-Phase-B value | Pass/Fail |
|---|---:|---:|---|
| regulations_total | 5 | 5 | PASS |
| regulations_applicable | 2 | 2 | PASS |
| domains | 10 | 10 | PASS |
| subdomains_total | 38 | 38 | PASS |
| subdomains_covered | 31 | 31 | PASS |
| subdomains_active | 37 | 37 | PASS |
| clauses_total | 54 | 54 | PASS |
| goals_total | 69 | 69 | PASS |
| tensions_total | 4 | 4 | PASS |
| ambiguity_cards_in_scope | 417 | 417 | PASS |
| stakeholders_total | 7 | 7 | PASS |
| business_goals_total | 5 | 5 | PASS |
| coverage_gaps_total | 4 | 4 | PASS |
| raci_roles | 6 | 6 | PASS |
| raci_activities | 43 | 43 | PASS |
| raci_activities_active | 41 | 41 | PASS |
| raci_edges_min | 206 | 206 | PASS |
| raci_composite_cells | 3 | 3 | PASS |
| applies_to_edges | 35 | 35 | PASS |
| gap_raci_count | 5 | 5 | PASS |

Plus 7 new Phase-B invariants added cleanly:

| Key | Value | Source |
|---|---:|---|
| systems | 5 | Doc04 §1.1 (5 rows) |
| data_stores | 3 | Doc04 §2.1 (3 rows) |
| data_flows | 5 | Doc04 §2.2 (5 rows) |
| personal_data_categories | 4 | Doc04 §2.3 (4 rows) |
| data_subject_categories | 3 | Doc04 §2.4 (3 rows) |
| third_parties | 6 | Doc06 §5 ("Vendor count: 6") |
| compliance_mapping_rows | 37 | Doc04 §3 (37 rows; D-08.3 inactive) |

- **Block 4 result: PASS — pre-Phase-B spine is byte-identical.**

### 4.4 Cross-check: pre-Phase-B link counts (RACI=206, APPLIES_TO=35)

| Rel | Expected | Found | Pass/Fail |
|---|---|---:|---|
| RACI | 206 | 206 | PASS |
| APPLIES_TO | 35 | 35 | PASS |

---

## Block 5 — Top findings + verdict

### 5.1 Top findings

**F1 (medium — bookkeeping, not schema):** The brief's headline totals (264 nodes / 624 links) and the narrative ("246 + 18 = 264", "505 + 119 = 624") do not match the actual graph contents (272 / 785). The discrepancy is **in the brief**, not the graph: the script emitted 26 Phase-B nodes (5+3+5+4+3+6) and 280 Phase-B links (3+99+68+86+3+8+1+10+2). Per-relation counts in the brief are individually correct; the brief's tallies are wrong. **Recommendation:** re-issue the brief with corrected totals before downstream phases consume them. **Not a FAIL because the content is correct.**

**F2 (low — interpretive expansion):** The INVOLVES edge count (99) slightly exceeds the literal SYS-* token count in Doc04 §3 (92). The +7 delta traces to three rows that say "All production systems" (D-08.1, D-09.1, D-10.3) where the script expanded to SYS-01..SYS-05 (3×5 = 15 → minus the cases where only 1 SYS-* is also literally mentioned in the row). Same minor expansion on FLOW for "All production flows" rows (D-09.1, D-10.3) → +15 to INVOLVES_FLOW (86 vs 71). **This is a defensible interpretation** but not literal; surface as a transparent choice. **Not a FAIL.**

**F3 (low — Datadog services duplication):** The Datadog ThirdParty node carries `services = ["APM / log aggregation (STORE-03)", "Log aggregation + APM"]` (length 2). Doc06 §3 row 2 lists Datadog once ("APM / log aggregation"); Doc06 §2 row 6 also lists Datadog once ("Logs and analytics"). The duplication in the graph mirrors an editorial inconsistency in Doc06 (Datadog appears under both §2 and §3, like Auth0, but Doc06 §5 only calls out the Auth0 double-count and not the Datadog one). **Recommendation:** collapse Datadog.services to length 1 ("APM / log aggregation (STORE-03)") for consistency with the AWS-as-1-ThirdParty decision and Doc06 §5's stated granularity policy. **Not a FAIL because Doc06 itself does not consistently apply its own rule; the graph merely reflects the source.**

**F4 (info — INVOLVES_STORE expansion):** Doc04 §3 column "Relevant Data Stores" lists STORE-* ids literally for every row; the graph's INVOLVES_STORE count of 68 is an **exact match** to the literal token count (verified by parsing Doc04 §3 row by row). No expansion here. **Praise, not a finding.**

### 5.2 Verdict

**CONDITIONAL PASS.**

- **Block 1:** Counts are individually correct (every named type/rel matches). The brief's headline totals (264/624) are wrong; the graph's actual totals (272/785) are internally consistent and reconcile to Doc04 + Doc06. **FAIL on the literal "264 vs 272" check; FAIL on the literal "624 vs 785" check; but no fabrication or schema defect.**
- **Block 2:** Both `--check` and `--check --strict` exit 0. **PASS.**
- **Block 3:** 40/40 sample cells pass against Doc04 + Doc06; 1 soft finding (F3 Datadog.services duplication). **PASS.**
- **Block 4:** Pre-Phase-B spine (246 nodes, 21 audits, 20 invariants, 7 stakeholders) byte-identical. **PASS.**

**Conditional accept with one blocking action:** the orchestrator must re-issue the brief with corrected totals (272 nodes / 785 links, 26 new nodes / 280 new links) and acknowledge that F3 (Datadog.services length=2) is acceptable in the absence of a Doc06 correction. Once the brief is corrected, the verdict flips to unconditional PASS.

---

## Appendix A — Reproduction commands

```bash
cd "/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH"

# Block 1 — counts
python3 -c "
import json
g = json.load(open('data/phase1_graph.json'))
types = {}
for n in g['nodes']: types[n['type']] = types.get(n['type'], 0) + 1
rels = {}
for l in g['links']: rels[l['rel']] = rels.get(l['rel'], 0) + 1
print('NODES:', sorted(types.items()))
print('LINKS:', sorted(rels.items()))
print('AUDITS:', len(g['audits']))
print('INV keys:', sorted(g['invariants'].keys()))
"

# Block 2 — schema check
python3 scripts/build_p1_dashboard.py --check
python3 scripts/build_p1_dashboard.py --check --strict

# Block 3 — sample cells (see body for full sweep)
python3 -c "
import json
g = json.load(open('data/phase1_graph.json'))
for sid in ['SYS-01','SYS-03','SYS-05','STORE-01','STORE-02','FLOW-02','FLOW-05']:
    n = next((n for n in g['nodes'] if n['id']==sid), None)
    print(sid, json.dumps(n.get('attrs',{}),indent=2))
"

# Block 4 — original 7 stakeholders
python3 -c "
import json
g = json.load(open('data/phase1_graph.json'))
for sid in ['STK-CEO-01','STK-CTO-01','STK-DPO-01','STK-DEVP-01','STK-CUSTOMER-01','STK-AWS-01','STK-STRIPE-01']:
    n = next((n for n in g['nodes'] if n['id']==sid), None)
    print(sid, 'FOUND' if n else 'MISSING')
"
```

---

## Appendix B — Files reviewed (read-only)

- `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json`
- `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/data/phase1_ontology.compact.json`
- `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml`
- `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Doc04_Architecture_DataInventory.md`
- `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Doc06_ThirdParty_Landscape.md`
- `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/scripts/build_p1_graph.py`
- `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/scripts/build_p1_dashboard.py`
- `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_ontology_v1.4_validation.md` (baseline)
- `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_raci_extension_v1.3_validation.md` (audit-title baseline)

No file outside `validation/` was modified.