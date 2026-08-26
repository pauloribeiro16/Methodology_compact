"""Inspect contents of both NIST Excel files."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from openpyxl import load_workbook
from pathlib import Path

base = Path(r"C:\Users\paulo.ribeiro\OneDrive - Instituto CCG ZGDV\Ambiente de Trabalho\Methodology-main\Methodology-main\00_METHODOLOGY\PREPROCESSING_by_domain")

# PF
print("="*80)
print("PF 1.0 and 1.1_Core Mapping.xlsx")
print("="*80)
wb = load_workbook(base / "PF 1.0 and 1.1_Core Mapping.xlsx", data_only=True)
for sname in wb.sheetnames:
    ws = wb[sname]
    print(f"\n--- Sheet: {sname} (max_row={ws.max_row}) ---")
    # mostrar primeiros 20 rows não-vazios
    count = 0
    for i, row in enumerate(ws.iter_rows(values_only=True), 1):
        # só rows com algum conteúdo
        if any(c is not None and str(c).strip() for c in row):
            non_empty = [str(c)[:60] if c is not None else "" for c in row[:8]]
            print(f"  R{i}: {non_empty}")
            count += 1
            if count >= 15:
                break
