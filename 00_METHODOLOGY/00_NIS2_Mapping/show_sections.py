"""Show sections of multiple docs."""
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

base = Path(r"C:\Users\paulo.ribeiro\OneDrive - Instituto CCG ZGDV\Ambiente de Trabalho\Methodology-main\Methodology-main\02_CASES\Case_02_SecureBorder_Solutions")

for fname in [
    "01_PHASE1_CONTEXT_RICH/05_Regulatory_Applicability.md",
    "02_PHASE2_RULES_RICH/10b_Privacy_Security_Goals_NIST_Implications.md",
    "02_PHASE2_RULES_RICH/08_Obligation_Derivation.md",
    "02_PHASE2_RULES_RICH/11_Rules_Catalog.md",
]:
    path = base / fname
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    print(f"\n=== {fname} ({path.stat().st_size//1024}KB) - secções ===")
    for line in body.splitlines():
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            print(f"  {'#'*len(m.group(1))} {m.group(2)[:90]}")
