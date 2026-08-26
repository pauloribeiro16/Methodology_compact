#!/usr/bin/env bash
#
# kg.sh — AEGIS Knowledge Graph navigation wrapper
#
# One-file helper around the Graphify CLI so agents never deal with
# venv paths or --graph flags. All commands are read-only (BFS over
# graph.json, no LLM). Usage logs to .kg_usage.log so we can measure
# adoption.
#
# Subcommands:
#   impact  <SR-ID>          RP-1: affected --depth 2 (escalate if >50)
#   where   "<topic>"        N1:  topic -> ranked reading files
#   trace   "<A>" "<B>"      RP-4/N4: shortest path with confidence per hop
#   doc     "<doc-label>"    N6:  what depends on this document
#   domain  <D-XX>           N3:  reading order for a domain
#   map                       N2:  thematic map (community index)
#   hub                       RP-7: top hubs
#   nist    <ctrl-id>        RP-3: reverse NIST index
#   hyper   "<topic>"        L3:  navigate hyperedge clusters
#   audit                      re-print graph integrity metrics
#
# Discovery: kg.sh walks ./kg/ for the newest
# graph.json and uses that. Override with --graph <path>.
# Override the graphify CLI path with env GRAPHIFY_BIN.
#
# See kg/GRAPHIFY.md for the full protocol.

set -eo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEFAULT_BASE="${REPO_ROOT}/kg"
GRAPHIFY="${GRAPHIFY_BIN:-${HOME}/.venvs/graphify/bin/graphify}"
USAGE_LOG="$(dirname "${BASH_SOURCE[0]}")/.kg_usage.log"

err() { echo "kg.sh: $*" >&2; exit 1; }
log_use() {
  printf "%s\t%s\t%s\n" "$(date -Iseconds)" "$USER" "$*" >> "$USAGE_LOG" 2>/dev/null || true
}

# --- graph discovery (latest by mtime) ---
find_graph() {
  if [ "${1:-}" = "--graph" ]; then
    echo "$2"; return 0
  fi
  [ -d "$DEFAULT_BASE" ] || err "no graph dir at $DEFAULT_BASE and no --graph given"
  latest=$(ls -1t "$DEFAULT_BASE"/*/graphify-out/graph.json 2>/dev/null | head -1 || true)
  [ -n "$latest" ] || err "no graph.json under $DEFAULT_BASE/*/graphify-out/"
  echo "$latest"
}

GRAPH="$(find_graph)"

# consume --graph <path> if present (anywhere-arg position)
while [ $# -gt 0 ]; do
  case "$1" in
    --graph) GRAPH="$2"; shift 2;;
    *) break;;
  esac
done

CMD="${1:-help}"
if [ $# -gt 0 ]; then shift; fi

run_g() {
  # graphify CLI only takes --graph on some subcommands; for the rest it
  # resolves <cwd>/graphify-out/graph.json. So: invoke from the build dir's
  # GRANDPARENT (the build name like E3_2026-08-23/), so the default resolution
  # matches graph.json inside its graphify-out/ subdir.
  GRAND="$(dirname "$(dirname "$GRAPH")")"
  ( cd "$GRAND" && "$GRAPHIFY" "$@" )
}

case "$CMD" in
  impact)
    [ $# -ge 1 ] || err "impact <SR-ID>"
    log_use "impact $1"
    out=$(run_g affected "$1" --depth 2 2>&1) || true
    echo "$out"
    cnt=$(echo "$out" | grep -cE "^- |^NODE " 2>/dev/null) || cnt=0
    cnt=${cnt:-0}
    if [ "$cnt" -gt 50 ]; then
      echo
      echo ">> kg.sh: RP-1 rule — $cnt impacted > 50, ESCALATE to human before writing"
    fi
    ;;

  where)
    [ $# -ge 1 ] || err "where <topic-substring>"
    log_use "where $*"
    KG="$GRAPH" python3 - "$@" <<'PY'
import json, re, os, sys
from collections import Counter
topic = " ".join(sys.argv[1:])
g = json.load(open(os.environ["KG"]))
links = g["links"]
deg = Counter()
for l in links:
    deg[l["source"]] += 1; deg[l["target"]] += 1
pat = re.compile(re.escape(topic), re.I)
matches = []
for n in g["nodes"]:
    if pat.search(n["label"]) or pat.search(n.get("norm_label","")) or pat.search(n["id"]):
        matches.append((deg[n["id"]], n.get("source_file") or "(synthetic)", n["label"][:75]))
matches.sort(key=lambda x: -x[0])
files = Counter(m[1] for m in matches)
print(f"# topic '{topic}': {len(matches)} matches across {len(files)} files")
print(f"# top starting files (by hit count):")
for f, c in files.most_common(10):
    print(f"  {c:>3} hits  {f}")
print(f"# representative labels (top by degree):")
for d, f, lab in matches[:8]:
    print(f"  deg={d:<4} {lab}")
PY
    ;;

  trace)
    [ $# -ge 2 ] || err "trace <A> <B>"
    log_use "trace $*"
    out=$(run_g path "$1" "$2" --undirected 2>&1) || true
    echo "$out"
    if echo "$out" | grep -q "No.*path found"; then
      echo
      echo ">> kg.sh: try without --undirected, or widen the source/target labels"
    fi
    ;;

  doc)
    [ $# -ge 1 ] || err "doc <doc-label>"
    log_use "doc $*"
    out=$(run_g explain "$1" 2>&1) || true
    if echo "$out" | grep -q "^Ambiguous"; then
      echo "$out" | head -6
      echo
      echo ">> kg.sh: ambiguous label — list resolved with their IDs and degrees:"
      KG="$GRAPH" python3 - "$1" <<'PY'
import json, os, sys
from collections import Counter
substr = sys.argv[1]
g = json.load(open(os.environ["KG"]))
nodes = {n["id"]: n for n in g["nodes"]}
deg = Counter()
for l in g["links"]:
    deg[l["source"]] += 1; deg[l["target"]] += 1
pat = re.compile(re.escape(substr), re.I)
hits = []
for nid, n in nodes.items():
    if pat.search(n["label"]) or pat.search(n.get("norm_label","")) or pat.search(nid):
        hits.append((deg[nid], nid, n["label"][:55]))
hits.sort(key=lambda x: -x[0])
for d, nid, lab in hits[:5]:
    print(f"  deg={d:<4} id={nid:<60} {lab}")
PY
    else
      echo "$out"
    fi
    ;;

  domain)
    [ $# -ge 1 ] || err "domain <D-XX>"
    log_use "domain $*"
    KG="$GRAPH" python3 - "$1" <<'PY'
import json, re, os, sys
from collections import Counter
prefix = sys.argv[1]
g = json.load(open(os.environ["KG"]))
nodes = g["nodes"]; links = g["links"]
deg = Counter()
for l in links:
    deg[l["source"]] += 1; deg[l["target"]] += 1
matches = []
for n in nodes:
    sf = n.get("source_file") or ""
    if sf.startswith(prefix) or re.match(rf"^{prefix}[_./]", sf):
        matches.append((deg[n["id"]], sf, n["label"][:65]))
matches.sort(key=lambda x: (-x[0], x[1]))
print(f"# {prefix}: {len(matches)} nodes")
if not matches: sys.exit(0)
tier_a_cutoff = max(matches[0][0] - 5, matches[0][0] // 2)
print(f"# Tier A — read first (degree >= {tier_a_cutoff}):")
seen=set()
for d, sf, lab in matches:
    if d >= tier_a_cutoff and (sf, lab) not in seen:
        print(f"  deg={d:<4} {sf:<55} {lab}"); seen.add((sf,lab))
print(f"# Tier B — by file path (alphabetical):")
for d, sf, lab in matches:
    if d < tier_a_cutoff and (sf, lab) not in seen:
        print(f"  deg={d:<4} {sf:<55} {lab}"); seen.add((sf,lab))
PY
    ;;

  map)
    log_use "map"
    KG="$GRAPH" python3 <<'PY'
import json, os
from collections import Counter, defaultdict
g = json.load(open(os.environ["KG"]))
deg = Counter()
for l in g["links"]:
    deg[l["source"]] += 1; deg[l["target"]] += 1
com = defaultdict(list)
for n in g["nodes"]: com[n.get("community")].append(n)
items = sorted(com.items(), key=lambda kv: -len(kv[1]))[:8]
print("# Top 8 communities by size (run `kg.sh doc Community N` for detail):")
for cid, mem in items:
    hubs = sorted(mem, key=lambda n: -deg[n["id"]])[:3]
    print(f"\n  Community {cid} ({len(mem)} nodes):")
    for h in hubs:
        print(f"     deg={deg[h['id']]:<4} {h['label'][:60]}")
PY
    ;;

  hub)
    log_use "hub"
    run_g god-nodes --top 10
    ;;

  nist)
    [ $# -ge 1 ] || err "nist <control-id>"
    log_use "nist $*"
    KG="$GRAPH" python3 - "$1" <<'PY'
import json, os, sys
from collections import Counter
ctrl = sys.argv[1].upper()
g = json.load(open(os.environ["KG"]))
nodes = {n["id"]: n for n in g["nodes"]}
matches = []
for n in g["nodes"]:
    if ctrl in n["label"].upper() or ctrl in n["id"].upper():
        matches.append(n)
if not matches:
    print(f"# no node labelled with {ctrl}"); sys.exit(0)
for tgt in matches[:3]:
    inbound = [(nodes[l["source"]]["label"][:60], l.get("relation",""), l.get("confidence",""))
               for l in g["links"] if l["target"] == tgt["id"]]
    print(f"\n# {tgt['label']}  (id={tgt['id']}) — {len(inbound)} inbound")
    for lab, rel, conf in inbound[:8]:
        print(f"  [{rel:<26}] {conf:<9} {lab}")
PY
    ;;

  hyper)
    [ $# -ge 1 ] || err "hyper <topic-substring>"
    log_use "hyper $*"
    KG="$GRAPH" python3 - "$1" <<'PY'
import json, re, os, sys
substr = " ".join(sys.argv[1:]).lower()
g = json.load(open(os.environ["KG"]))
nodes = {n["id"]: n for n in g["nodes"]}
pat = re.compile(re.escape(substr), re.I)
hits = []
for h in g.get("hyperedges", []):
    if pat.search(h.get("label","")):
        hits.append(h)
print(f"# {len(hits)} hyperedges matching '{substr}'")
for h in hits[:10]:
    conf = h.get("confidence", ""); cs = h.get("confidence_score","")
    members = [nodes.get(m,{}).get("label", m)[:40] for m in h.get("nodes", [])]
    print(f"\n  {h.get('label','')[:80]}  [{h.get('relation','?')}] [{conf} {cs}]")
    for m in members[:6]:
        print(f"     - {m}")
PY
    ;;

  audit)
    log_use "audit"
    KG="$GRAPH" python3 <<'PY'
import json, os
from collections import Counter
g = json.load(open(os.environ["KG"]))
nodes, links, hes = g["nodes"], g["links"], g.get("hyperedges", [])
ids = set(n["id"] for n in nodes)
dang = sum(1 for l in links if l["source"] not in ids or l["target"] not in ids)
bhe = sum(1 for h in hes for m in h.get("nodes",[]) if m not in ids)
conf = Counter(l.get("confidence","?") for l in links)
selfl = sum(1 for l in links if l["source"] == l["target"])
sig = [(l["source"],l["target"],l.get("relation","")) for l in links]
dups = len(sig) - len(set(sig))
rel_inf = sum(1 for l in links if l.get("relation") == "INFERRED")
deg = Counter()
for l in links: deg[l["source"]] += 1; deg[l["target"]] += 1
iso = sum(1 for n in nodes if deg[n["id"]] == 0)
print(f"# graph: {os.environ['KG']}")
print(f"# nodes={len(nodes)} links={len(links)} hyper={len(hes)}")
print(f"# dangling={dang} self-loops={selfl} dup-triples={dups} relation=INFERRED={rel_inf}")
print(f"# broken-hyper-refs={bhe} isolated={iso}")
print(f"# confidence={dict(conf)}")
PY
    ;;

  help|"")
    cat <<EOF
kg.sh — AEGIS Knowledge Graph navigation wrapper
graph: $GRAPH

Subcommands:
  impact <SR-ID>          RP-1: ripple cost (escalate if >50 nodes)
  where  "<topic>"        N1:  topic -> ranked reading files
  trace  "<A>" "<B>"      RP-4: shortest path with confidence per hop
  doc    "<doc-label>"    N6:  what depends on this document (with ambiguity resolver)
  domain <D-XX>           N3:  reading order for a domain
  map                       N2:  thematic map (community index)
  hub                       RP-7: top 10 hubs
  nist   <ctrl-id>        RP-3: reverse NIST index
  hyper  "<topic>"        L3:  navigate hyperedge clusters
  audit                     integrity metrics (no writes)
  help                       this text

See kg/GRAPHIFY.md for the reasoning patterns (RP-*).
EOF
    ;;

  *)
    err "unknown subcommand: $CMD (try 'help')"
    ;;
esac