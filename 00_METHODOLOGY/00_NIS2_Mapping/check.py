import sys, re
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
import yaml

base = Path(r"C:\Users\paulo.ribeiro\OneDrive - Instituto CCG ZGDV\Ambiente de Trabalho\Methodology-main\Methodology-main\02_CASES\Case_02_SecureBorder_Solutions")
for f in sorted((base / "01_PHASE1_CONTEXT_RICH").glob("*.md")):
    text = f.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        continue
    try:
        fm = yaml.safe_load(m.group(1))
    except Exception:
        continue
    regs = fm.get("applicable_regs", "") if isinstance(fm, dict) else ""
    if regs:
        print(f"  {f.name}: {regs}")
