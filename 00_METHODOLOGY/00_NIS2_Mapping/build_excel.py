# -*- coding: utf-8 -*-
"""
build_excel.py
Lê o ficheiro regulamento_nis2_756_2026.md (resultado de OCR do Regulamento n.º 756/2026)
e gera um Excel estruturado com:
  - 00_Indice
  - 01_Resumo
  - 02_QNRCS_Controlo  (Anexo I — todos os controlos, descrição e referências)
  - 03_Anexo_III_Basico       (medidas obrigatórias — Básico)
  - 04_Anexo_III_Substancial  (medidas obrigatórias — Substancial)
  - 05_Anexo_III_Elevado      (medidas obrigatórias — Elevado)
  - 06_Anexo_IV_Grupo_B       (entidades públicas relevantes — Grupo B)
  - 07_Anexo_IV_Grupo_A       (entidades públicas relevantes — Grupo A)
  - 08_Mapa_Referencias       (cross-refs QNRCS ↔ ISO/NIST/CIS/CyFun)
"""

import re
import html
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

# ---------------------------------------------------------------------------
# 0. Paths
# ---------------------------------------------------------------------------
ROOT = Path(r"C:\Users\paulo.ribeiro\OneDrive - Instituto CCG ZGDV\Ambiente de Trabalho\Methodology-main\Methodology-main")
SRC_MD = ROOT / "regulamento_nis2_756_2026.md"
OUT_XLSX = ROOT / "00_NIS2_Mapping" / "NIS2_PT_Regulamento_756_2026_Mapeamento.xlsx"

# ---------------------------------------------------------------------------
# 1. Helpers de estilo
# ---------------------------------------------------------------------------
THIN = Side(border_style="thin", color="888888")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
HEADER_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
SUBHEADER_FILL = PatternFill("solid", fgColor="D9E1F2")
SUBHEADER_FONT = Font(name="Calibri", size=11, bold=True, color="1F4E78")
ZEBRA_FILL = PatternFill("solid", fgColor="F2F2F2")
NORMAL_FONT = Font(name="Calibri", size=11)
WRAP_ALIGN = Alignment(wrap_text=True, vertical="top", horizontal="left")

# Cores por nível
LEVEL_FILLS = {
    "Básico":       PatternFill("solid", fgColor="C6EFCE"),  # verde claro
    "Substancial":  PatternFill("solid", fgColor="FFEB9C"),  # amarelo claro
    "Elevado":      PatternFill("solid", fgColor="FFC7CE"),  # vermelho claro
    "Grupo A":      PatternFill("solid", fgColor="FFC7CE"),
    "Grupo B":      PatternFill("solid", fgColor="C6EFCE"),
}

# Cores por objetivo QNRCS
OBJ_COLORS = {
    "GR": "4472C4",  # azul
    "ID": "70AD47",  # verde
    "PR": "ED7D31",  # laranja
    "DE": "7030A0",  # roxo
    "RS": "C00000",  # vermelho
    "RC": "00B0F0",  # azul claro
}


def style_header(ws, row, n_cols):
    for c in range(1, n_cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = WRAP_ALIGN
        cell.border = BORDER


def style_subheader(ws, row, n_cols):
    for c in range(1, n_cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = SUBHEADER_FILL
        cell.font = SUBHEADER_FONT
        cell.alignment = WRAP_ALIGN
        cell.border = BORDER


def autosize(ws, min_w=12, max_w=80):
    for col in ws.columns:
        col_letter = None
        max_len = 0
        for cell in col:
            if cell.column_letter is None:
                continue
            col_letter = cell.column_letter
            v = cell.value
            if v is None:
                continue
            # comprimento da linha mais comprida (com wrap)
            for line in str(v).splitlines():
                if len(line) > max_len:
                    max_len = len(line)
        if col_letter:
            width = min(max(min_w, max_len + 2), max_w)
            ws.column_dimensions[col_letter].width = width


def freeze_top(ws, row=2):
    ws.freeze_panes = f"A{row}"


# ---------------------------------------------------------------------------
# 2. Carregar o MD
# ---------------------------------------------------------------------------
text = SRC_MD.read_text(encoding="utf-8")
lines = text.splitlines()

# Forçar UTF-8 no stdout (Windows cp1252 falha em emojis/em-dashes)
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ---------------------------------------------------------------------------
# 3. Parse: QNRCS Controlo (Anexo I)
#    Os controlos aparecem como linhas próprias:
#        GR.CO-1 — A missão, ...
#    seguidos de ### Descrição e ### Referências (nem sempre com '###')
# ---------------------------------------------------------------------------
CONTROLO_RE = re.compile(
    r"^(GR\.[A-Z]+-\d+|ID\.[A-Z]+-\d+|PR\.[A-Z]+-\d+|DE\.[A-Z]+-\d+|RS\.[A-Z]+-\d+|RC\.[A-Z]+-\d+)\s*[—\-\xef\xbf\xbd]\s*(.*)$"
)

# Índice: encontrar início do Anexo I (linha 870) e fim (linha 3510 = ANEXO II)
anexo_i_start = None
anexo_i_end = None
for i, ln in enumerate(lines):
    if anexo_i_start is None and re.match(r"^#{1,6}\s*ANEXO\s*I\b", ln.strip(), re.IGNORECASE):
        anexo_i_start = i
    if anexo_i_start is not None and re.match(r"^#{1,6}\s*ANEXO\s*II\b", ln.strip(), re.IGNORECASE):
        anexo_i_end = i
        break

print(f"Anexo I: linhas {anexo_i_start+1}–{anexo_i_end+1}  ({anexo_i_end - anexo_i_start} linhas)")

# Categorias do QNRCS
CATEGORIES = [
    ("GR.CO", "Gerir", "Contexto Organizacional"),
    ("GR.GR", "Gerir", "Estratégia de Gestão de Risco"),
    ("GR.FR", "Gerir", "Funções, Responsabilidades e Autoridades"),
    ("GR.PP", "Gerir", "Políticas e Planos de Cibersegurança"),
    ("GR.SP", "Gerir", "Supervisão"),
    ("GR.CA", "Gerir", "Gestão do Risco da Cadeia de Abastecimento"),
    ("ID.GA", "Identificar", "Gestão de Ativos"),
    ("ID.AR", "Identificar", "Avaliação do Risco"),
    ("ID.MC", "Identificar", "Melhoria Contínua"),
    ("PR.GA", "Proteger", "Gestão de Identidades, Autenticação e Controlo de Acessos"),
    ("PR.FC", "Proteger", "Formação e Sensibilização"),
    ("PR.SD", "Proteger", "Segurança de Dados"),
    ("PR.SP", "Proteger", "Segurança de Plataformas"),
    ("PR.RI", "Proteger", "Resiliência da Infraestrutura Tecnológica"),
    ("DE.MC", "Detetar", "Monitorização Contínua"),
    ("DE.AE", "Detetar", "Anomalias e Eventos"),
    ("RS.GI", "Responder", "Gestão de Incidentes"),
    ("RS.AI", "Responder", "Análise de Incidentes"),
    ("RS.NC", "Responder", "Notificação e Comunicação de Incidentes"),
    ("RS.MI", "Responder", "Mitigação de Incidentes"),
    ("RC.PR", "Recuperar", "Execução do Plano de Recuperação"),
    ("RC.CO", "Recuperar", "Comunicação de Recuperação"),
]
CAT_MAP = {c[0]: c for c in CATEGORIES}

def category_of(code: str) -> tuple[str, str, str]:
    prefix = code.split("-")[0]
    return CAT_MAP.get(prefix, ("?", "?", "?"))

# Parse dos controlos do QNRCS
controles = []  # lista de dicts
i = anexo_i_start
while i < anexo_i_end:
    ln = lines[i].strip()
    m = CONTROLO_RE.match(ln)
    if m:
        code, title = m.group(1), m.group(2).strip()
        obj, cat, cat_name = category_of(code)
        # Coletar descrição (linhas até ao próximo "### Referências" ou próximo controlo)
        desc_lines = []
        refs_lines = []
        j = i + 1
        in_refs = False
        while j < anexo_i_end:
            l2 = lines[j].strip()
            # Próximo controlo?
            if CONTROLO_RE.match(l2):
                break
            # Marcador de Referências (vários formatos no OCR)
            if re.match(r"^#+\s*Referências\s*$", l2) or l2.lower() in ("**referências**", "### referências", "referências"):
                in_refs = True
                j += 1
                continue
            # Marcador de Descrição (consumir)
            if re.match(r"^#+\s*Descrição\s*$", l2) or l2.lower() in ("**descrição**", "### descrição", "descrição"):
                j += 1
                continue
            # Ignorar ruído (cabeçalhos de página repetidos, page numbers, etc.)
            if (re.match(r"^\d+/\d+$", l2) or
                "Regulamento n.º 756/2026" in l2 or
                "DIÁRIO DA REPÚBLICA" in l2.upper() or
                l2 in ("2.ª série", "N.º 118", "22-06-2026") or
                l2 == "" or
                l2.startswith("<page_")):
                j += 1
                continue
            if in_refs:
                if l2:
                    refs_lines.append(l2)
            else:
                if l2:
                    desc_lines.append(l2)
            j += 1
        desc = " ".join(desc_lines).strip()
        desc = re.sub(r"\s+", " ", desc)
        refs = " | ".join(refs_lines)
        refs = re.sub(r"\s+", " ", refs).strip()
        controles.append({
            "codigo": code,
            "titulo": title,
            "objetivo": obj,
            "categoria": cat,
            "categoria_nome": cat_name,
            "descricao": desc,
            "referencias": refs,
        })
        i = j
    else:
        i += 1

print(f"QNRCS: {len(controles)} controlos extraídos.")

# ---------------------------------------------------------------------------
# 4. Parse: Anexo III — tabelas HTML
# ---------------------------------------------------------------------------
# Estratégia: encontrar cada <table>...</table> dentro do Anexo III e dentro
# do Anexo IV, e extrair linhas <tr> com <td>. O nível é determinado pelo
# cabeçalho markdown anterior (### Básico, ### Substancial, ### Elevado).
# ---------------------------------------------------------------------------
def strip_tags(s: str) -> str:
    """Remove tags HTML, decodifica entidades, normaliza espaços."""
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse_html_tables(block_lines):
    """Devolve lista de tabelas; cada tabela = lista de linhas (cada linha = lista de células)."""
    tables = []
    in_table = False
    cur = []
    for ln in block_lines:
        s = ln.strip()
        if s.startswith("<table>"):
            in_table = True
            cur = []
            continue
        if s.startswith("</table>"):
            in_table = False
            if cur:
                tables.append(cur)
            continue
        if not in_table:
            continue
        if s.startswith("</tr>"):
            continue
        if s.startswith("<tr>"):
            # A linha pode ter <tr><td>...</td><td>...</td>...</tr> tudo numa só string.
            cur.append([])
            # Extrair todas as células <td>...</td> e <th>...</th> da linha
            cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", s, re.DOTALL)
            for c in cells:
                cur[-1].append(strip_tags(c))
            continue
        # Linha que não é <tr> nem </tr> — pode ser continuação de célula?
        # (pouco comum neste OCR mas tolerar)
    return tables


# Localizar Anexo III e Anexo IV
anexo_iii_start = None
anexo_iv_start = None
for i, ln in enumerate(lines):
    if anexo_iii_start is None and re.match(r"^#{1,6}\s*ANEXO\s*III\b", ln.strip(), re.IGNORECASE):
        anexo_iii_start = i
    if anexo_iv_start is None and re.match(r"^#{1,6}\s*ANEXO\s*IV\b", ln.strip(), re.IGNORECASE):
        anexo_iv_start = i

# Limite do Anexo III = início do Anexo IV
anexo_iii_end = anexo_iv_start
anexo_iv_end = len(lines)

print(f"Anexo III: linhas {anexo_iii_start+1}–{anexo_iii_end+1}")
print(f"Anexo IV:  linhas {anexo_iv_start+1}–{anexo_iv_end+1}")

# Para o Anexo III, detetar nível a partir dos H3 anteriores
anexo_iii_tables = []
i = anexo_iii_start
cur_level = None
while i < anexo_iii_end:
    ln = lines[i].strip()
    # Detetar nível — aceita "### Básico", "**Básico**", "Básico" puro
    norm = ln.lower().replace("**", "").lstrip("#").strip()
    if norm in ("básico", "basico", "substancial", "elevado"):
        if "basico" in norm or "básico" in norm:
            cur_level = "Básico"
        elif "substancial" in norm:
            cur_level = "Substancial"
        elif "elevado" in norm:
            cur_level = "Elevado"
    elif ln.startswith("<table>"):
        # Encontrar fim
        j = i
        while j < anexo_iii_end and not lines[j].strip().startswith("</table>"):
            j += 1
        block = lines[i:j + 1]
        tabs = parse_html_tables(block)
        for t in tabs:
            # Header row é a primeira
            if t:
                header = [c.lower() for c in t[0]]
                data_rows = t[1:]
                anexo_iii_tables.append((cur_level, header, data_rows))
        i = j
    i += 1

# Estruturar dados do Anexo III por nível
anexo_iii_data = {"Básico": [], "Substancial": [], "Elevado": []}
for level, header, rows in anexo_iii_tables:
    if not rows:
        continue
    # Header pode ser lista vazia se a primeira <tr> for vazia — normalizar
    if not header:
        header = ["controlo de cibersegurança", "medida de cibersegurança", "critério de verificação"]
    # Detetar colunas — primeira linha = header
    if header and ("controlo" in header[0] or "controlo de cibersegurança" in header[0]):
        col_names = ["Controlo QNRCS", "Medida de Cibersegurança", "Critério de Verificação"]
    else:
        col_names = header
    for r in rows:
        # Garantir 3 colunas
        r = (r + ["", "", ""])[:3]
        controlo_txt = r[0]
        # Extrair código "GR.CO-3" se existir. Aceita em-dash (—), hyphen (-),
        # ou o caractere replacement U+FFFD (resultado de má conversão CP1252→UTF-8)
        m = re.match(r"^([A-Z]{2}\.[A-Z]{2}-\d+)\s*[—\-\xef\xbf\xbd]\s*(.*)$", controlo_txt)
        if m:
            code, title = m.group(1), m.group(2).strip()
            obj, cat, cat_name = category_of(code)
        else:
            code, title = "", controlo_txt
            obj, cat, cat_name = "", "", ""
        anexo_iii_data[level].append({
            "nivel": level,
            "codigo": code,
            "controlo": title,
            "controlo_full": controlo_txt,
            "medida": r[1],
            "criterio": r[2],
            "objetivo": obj,
            "categoria": cat,
            "categoria_nome": cat_name,
        })

for lvl, lst in anexo_iii_data.items():
    print(f"  Anexo III {lvl}: {len(lst)} controlos")

# ---------------------------------------------------------------------------
# 5. Parse: Anexo IV — Grupo B e Grupo A
# ---------------------------------------------------------------------------
anexo_iv_tables = []
i = anexo_iv_start
cur_grupo = None
while i < anexo_iv_end:
    ln = lines[i].strip()
    if re.match(r"^##\s*Grupo\s*[AB]\b", ln):
        cur_grupo = ln[3:].strip()
    elif ln.startswith("<table>"):
        j = i
        while j < anexo_iv_end and not lines[j].strip().startswith("</table>"):
            j += 1
        block = lines[i:j + 1]
        tabs = parse_html_tables(block)
        for t in tabs:
            if t:
                header = [c.lower() for c in t[0]]
                data_rows = t[1:]
                # Anexo IV tem colunas "Área", "Medidas", "Critérios" (ou só abreviatura)
                if any("abreviatura" in h for h in header):
                    continue  # tabela de abreviaturas
                anexo_iv_tables.append((cur_grupo, header, data_rows))
        i = j
    i += 1

# Estruturar
anexo_iv_data = {"Grupo A": [], "Grupo B": []}
for grupo, header, rows in anexo_iv_tables:
    if not rows or grupo is None:
        continue
    if not header:
        header = ["área", "medidas de cibersegurança", "critérios de verificação"]
    if header and ("área" in header[0] or "area" in header[0]):
        col_names = ["Área", "Medida de Cibersegurança", "Critério de Verificação"]
    else:
        col_names = header
    for r in rows:
        r = (r + ["", "", ""])[:3]
        # Limpar caracteres replacement U+FFFD que aparecem onde devia estar "—"
        # em secções onde o OCR falhou
        area_clean = re.sub(r"\s+[—\xef\xbf\xbd]\s+", " — ", r[0])
        anexo_iv_data[grupo].append({
            "grupo": grupo,
            "area": area_clean,
            "medida": r[1],
            "criterio": r[2],
        })

for g, lst in anexo_iv_data.items():
    print(f"  Anexo IV {g}: {len(lst)} medidas")

# ---------------------------------------------------------------------------
# 6. Construir o Workbook
# ---------------------------------------------------------------------------
wb = Workbook()
wb.remove(wb.active)

# ---- 00_Indice ----
ws = wb.create_sheet("00_Indice")
ws.append(["Sheet", "Descrição", "Linhas"])
style_header(ws, 1, 3)
indice = [
    ("00_Indice",             "Índice remissivo do workbook", ""),
    ("01_Resumo",             "Resumo do Regulamento n.º 756/2026 + mapeamento de alto nível", ""),
    ("02_QNRCS_Controlo",     f"Anexo I — {len(controles)} controlos do QNRCS com descrição e referências cruzadas", len(controles)),
    ("03_Anexo_III_Basico",       f"Anexo III — Nível Básico ({len(anexo_iii_data['Básico'])} medidas obrigatórias)", len(anexo_iii_data["Básico"])),
    ("04_Anexo_III_Substancial",  f"Anexo III — Nível Substancial ({len(anexo_iii_data['Substancial'])} medidas obrigatórias)", len(anexo_iii_data["Substancial"])),
    ("05_Anexo_III_Elevado",      f"Anexo III — Nível Elevado ({len(anexo_iii_data['Elevado'])} medidas obrigatórias)", len(anexo_iii_data["Elevado"])),
    ("06_Anexo_IV_Grupo_B",       f"Anexo IV — Entidades Públicas Grupo B ({len(anexo_iv_data['Grupo B'])} medidas)", len(anexo_iv_data["Grupo B"])),
    ("07_Anexo_IV_Grupo_A",       f"Anexo IV — Entidades Públicas Grupo A ({len(anexo_iv_data['Grupo A'])} medidas)", len(anexo_iv_data["Grupo A"])),
    ("08_Mapa_Referencias",       "Mapa de equivalências QNRCS ↔ ISO 27001:2022 ↔ ISO 27002:2022 ↔ NIST CSF 2.0 ↔ NIST 800-53 Rev.5 ↔ CIS CSC v8.1 ↔ CyFun 2025", ""),
]
for r in indice:
    ws.append(r)
    cur = ws.max_row
    # zebra
    if cur % 2 == 0:
        for c in range(1, 4):
            ws.cell(row=cur, column=c).fill = ZEBRA_FILL
    for c in range(1, 4):
        ws.cell(row=cur, column=c).font = NORMAL_FONT
        ws.cell(row=cur, column=c).alignment = WRAP_ALIGN
        ws.cell(row=cur, column=c).border = BORDER
ws.column_dimensions["A"].width = 32
ws.column_dimensions["B"].width = 80
ws.column_dimensions["C"].width = 12
freeze_top(ws)

# ---- 01_Resumo ----
ws = wb.create_sheet("01_Resumo")
ws.append(["Campo", "Conteúdo"])
style_header(ws, 1, 2)
resumo = [
    ("Diploma",              "Regulamento n.º 756/2026, de 22 de junho"),
    ("Entidade emissora",    "Centro Nacional de Cibersegurança (CNCS) — Gabinete Nacional de Segurança"),
    ("Diário da República",  "2.ª série, N.º 118, de 22-06-2026"),
    ("Executa",              "Decreto-Lei n.º 125/2025, de 4 de dezembro (Regime Jurídico da Cibersegurança)"),
    ("Transpõe",             "Diretiva (UE) 2022/2555 (NIS 2)"),
    ("Coordenador (CNCS)",   "Lino Santos"),
    ("Entrada em vigor",     "23 de junho de 2026 (1 dia após publicação)"),
    ("Âmbito subjetivo",     "Entidades essenciais (Anexo I DL 125/2025), entidades importantes (Anexo II DL 125/2025), entidades públicas relevantes"),
    ("Estrutura do Anexo I (QNRCS)", f"{len(controles)} controlos distribuídos por 6 objetivos e 22 categorias"),
    ("Níveis de conformidade", "Básico (0–99) · Substancial (100–199) · Elevado (200–1200) — definidos pela Matriz de Risco"),
    ("Ponderação setorial",  "Anexo I DL 125/2025 (críticos) = 1.5 ; Anexo II DL 125/2025 (outros críticos) = 1.0"),
    ("Anexo III (essenciais+importantes)", f"{len(anexo_iii_data['Básico']) + len(anexo_iii_data['Substancial']) + len(anexo_iii_data['Elevado'])} controlos no total (3 níveis progressivos)"),
    ("Anexo IV (públicas)",  f"Grupo A = {len(anexo_iv_data['Grupo A'])} medidas; Grupo B = {len(anexo_iv_data['Grupo B'])} medidas; Grupo A ⊃ Grupo B"),
    ("Frameworks de referência", "NIST CSF 2.0, ISO/IEC 27001:2022, ISO/IEC 27002:2022, NIST SP 800-53 Rev.5, CIS CSC v8.1, CyFun 2025"),
]
for r in resumo:
    ws.append(r)
    cur = ws.max_row
    if cur % 2 == 0:
        for c in range(1, 3):
            ws.cell(row=cur, column=c).fill = ZEBRA_FILL
    ws.cell(row=cur, column=1).font = Font(name="Calibri", size=11, bold=True)
    ws.cell(row=cur, column=2).font = NORMAL_FONT
    for c in range(1, 3):
        ws.cell(row=cur, column=c).alignment = WRAP_ALIGN
        ws.cell(row=cur, column=c).border = BORDER
ws.column_dimensions["A"].width = 30
ws.column_dimensions["B"].width = 95
freeze_top(ws)

# ---- 02_QNRCS_Controlo ----
ws = wb.create_sheet("02_QNRCS_Controlo")
hdr = ["#", "Código", "Objetivo", "Categoria", "Categoria (nome)", "Título do Controlo", "Descrição", "Referências Cruzadas"]
ws.append(hdr)
style_header(ws, 1, len(hdr))
for idx, c in enumerate(controles, start=1):
    ws.append([idx, c["codigo"], c["objetivo"], c["categoria"], c["categoria_nome"], c["titulo"], c["descricao"], c["referencias"]])
    cur = ws.max_row
    # zebra
    if idx % 2 == 0:
        for col in range(1, len(hdr) + 1):
            ws.cell(row=cur, column=col).fill = ZEBRA_FILL
    # cor por objetivo
    obj_color = OBJ_COLORS.get(c["objetivo"][:2] if c["objetivo"] else "", None)
    if obj_color:
        ws.cell(row=cur, column=3).fill = PatternFill("solid", fgColor=obj_color)
        ws.cell(row=cur, column=3).font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    for col in range(1, len(hdr) + 1):
        cell = ws.cell(row=cur, column=col)
        if cell.font.color is None or cell.font.color.rgb != "FFFFFFFF":
            cell.font = NORMAL_FONT
        cell.alignment = WRAP_ALIGN
        cell.border = BORDER
# Auto filtro
ws.auto_filter.ref = f"A1:{get_column_letter(len(hdr))}{ws.max_row}"
freeze_top(ws)
ws.column_dimensions["A"].width = 6
ws.column_dimensions["B"].width = 14
ws.column_dimensions["C"].width = 12
ws.column_dimensions["D"].width = 12
ws.column_dimensions["E"].width = 32
ws.column_dimensions["F"].width = 60
ws.column_dimensions["G"].width = 70
ws.column_dimensions["H"].width = 55

# ---- 03/04/05 Anexo III (Básico / Substancial / Elevado) ----
def write_anexo_iii_sheet(name, level):
    ws = wb.create_sheet(name)
    hdr = ["Nível", "Código", "Objetivo", "Categoria", "Título do Controlo (QNRCS)", "Medida de Cibersegurança", "Critério de Verificação"]
    ws.append(hdr)
    style_header(ws, 1, len(hdr))
    fill = LEVEL_FILLS[level]
    for idx, item in enumerate(anexo_iii_data[level], start=1):
        ws.append([item["nivel"], item["codigo"], item["objetivo"], item["categoria"] + " — " + item["categoria_nome"] if item["categoria"] else "",
                   item["controlo"], item["medida"], item["criterio"]])
        cur = ws.max_row
        # cor por nível na 1ª coluna
        ws.cell(row=cur, column=1).fill = fill
        ws.cell(row=cur, column=1).font = Font(name="Calibri", size=11, bold=True)
        # cor por objetivo na 3ª coluna
        obj_color = OBJ_COLORS.get(item["objetivo"][:2] if item["objetivo"] else "", None)
        if obj_color:
            ws.cell(row=cur, column=3).fill = PatternFill("solid", fgColor=obj_color)
            ws.cell(row=cur, column=3).font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        # zebra
        if idx % 2 == 0:
            for col in (2, 4, 5, 6, 7):
                ws.cell(row=cur, column=col).fill = ZEBRA_FILL
        for col in range(1, len(hdr) + 1):
            cell = ws.cell(row=cur, column=col)
            if cell.font is None or cell.font.name != "Calibri":
                cell.font = NORMAL_FONT
            cell.alignment = WRAP_ALIGN
            cell.border = BORDER
    ws.auto_filter.ref = f"A1:{get_column_letter(len(hdr))}{ws.max_row}"
    freeze_top(ws)
    ws.column_dimensions["A"].width = 12
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 12
    ws.column_dimensions["D"].width = 30
    ws.column_dimensions["E"].width = 55
    ws.column_dimensions["F"].width = 70
    ws.column_dimensions["G"].width = 70


write_anexo_iii_sheet("03_Anexo_III_Basico", "Básico")
write_anexo_iii_sheet("04_Anexo_III_Substancial", "Substancial")
write_anexo_iii_sheet("05_Anexo_III_Elevado", "Elevado")

# ---- 06/07 Anexo IV (Grupo B / Grupo A) ----
def write_anexo_iv_sheet(name, grupo):
    ws = wb.create_sheet(name)
    hdr = ["Grupo", "Área", "Medida de Cibersegurança", "Critério de Verificação"]
    ws.append(hdr)
    style_header(ws, 1, len(hdr))
    fill = LEVEL_FILLS[grupo]
    for idx, item in enumerate(anexo_iv_data[grupo], start=1):
        ws.append([item["grupo"], item["area"], item["medida"], item["criterio"]])
        cur = ws.max_row
        ws.cell(row=cur, column=1).fill = fill
        ws.cell(row=cur, column=1).font = Font(name="Calibri", size=11, bold=True)
        if idx % 2 == 0:
            for col in (2, 3, 4):
                ws.cell(row=cur, column=col).fill = ZEBRA_FILL
        for col in range(1, len(hdr) + 1):
            cell = ws.cell(row=cur, column=col)
            if cell.font is None or cell.font.name != "Calibri":
                cell.font = NORMAL_FONT
            cell.alignment = WRAP_ALIGN
            cell.border = BORDER
    ws.auto_filter.ref = f"A1:{get_column_letter(len(hdr))}{ws.max_row}"
    freeze_top(ws)
    ws.column_dimensions["A"].width = 12
    ws.column_dimensions["B"].width = 60
    ws.column_dimensions["C"].width = 70
    ws.column_dimensions["D"].width = 70


write_anexo_iv_sheet("06_Anexo_IV_Grupo_B", "Grupo B")
write_anexo_iv_sheet("07_Anexo_IV_Grupo_A", "Grupo A")

# ---- 08_Mapa_Referencias ----
ws = wb.create_sheet("08_Mapa_Referencias")
hdr = ["Código QNRCS", "Objetivo", "Categoria", "Título", "ISO/IEC 27001:2022", "ISO/IEC 27002:2022", "NIST SP 800-53 Rev.5", "NIST CSF 2.0", "CIS CSC v8.1", "CyFun 2025"]
ws.append(hdr)
style_header(ws, 1, len(hdr))


def split_refs(refs_blob: str):
    """Separa a string 'Referências' em 6 colunas por framework."""
    out = {k: "" for k in ["ISO/IEC 27001:2022", "ISO/IEC 27002:2022", "NIST SP 800-53 Rev.5", "NIST CSF 2.0", "CIS CSC v8.1", "CyFun 2025"]}
    if not refs_blob:
        return out
    # O blob é uma série de segmentos unidos por " | "
    # Cada segmento começa com um nome de framework seguido de " — " ou ":" ou "-"
    segments = [s.strip() for s in refs_blob.split("|") if s.strip()]
    # Mapeamento de prefixos
    patterns = [
        ("ISO/IEC 27001:2022", re.compile(r"^ISO/?IEC\s*27001:2022\s*[-—:]\s*", re.IGNORECASE)),
        ("ISO/IEC 27002:2022", re.compile(r"^ISO/?IEC\s*27002:2022\s*[-—:]\s*", re.IGNORECASE)),
        ("NIST SP 800-53 Rev.5", re.compile(r"^NIST\s*SP[-\s]?800[-\s]?53\s*Rev\.?\s*5?\s*[-—:]\s*", re.IGNORECASE)),
        ("NIST CSF 2.0",        re.compile(r"^NIST\s*CSF\s*2\.?0?\s*[-—:]?\s*", re.IGNORECASE)),
        ("CIS CSC v8.1",        re.compile(r"^CIS\s*CSC\s*v?8\.?1?\s*[-—:]?\s*", re.IGNORECASE)),
        ("CyFun 2025",          re.compile(r"^CyFun\s*2025\s*[-—:]?\s*", re.IGNORECASE)),
    ]
    for seg in segments:
        # tentar cada pattern
        matched = False
        for key, pat in patterns:
            if pat.match(seg):
                val = pat.sub("", seg).strip()
                if out[key]:
                    out[key] += " | " + val
                else:
                    out[key] = val
                matched = True
                break
        if not matched:
            # sem prefixo reconhecido — anexar como "extra"
            pass
    return out


for idx, c in enumerate(controles, start=1):
    refs = split_refs(c["referencias"])
    ws.append([c["codigo"], c["objetivo"], c["categoria"], c["titulo"],
               refs["ISO/IEC 27001:2022"], refs["ISO/IEC 27002:2022"], refs["NIST SP 800-53 Rev.5"],
               refs["NIST CSF 2.0"], refs["CIS CSC v8.1"], refs["CyFun 2025"]])
    cur = ws.max_row
    if idx % 2 == 0:
        for col in range(1, len(hdr) + 1):
            ws.cell(row=cur, column=col).fill = ZEBRA_FILL
    obj_color = OBJ_COLORS.get(c["objetivo"][:2] if c["objetivo"] else "", None)
    if obj_color:
        ws.cell(row=cur, column=2).fill = PatternFill("solid", fgColor=obj_color)
        ws.cell(row=cur, column=2).font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    for col in range(1, len(hdr) + 1):
        cell = ws.cell(row=cur, column=col)
        if cell.font is None or cell.font.name != "Calibri":
            cell.font = NORMAL_FONT
        cell.alignment = WRAP_ALIGN
        cell.border = BORDER
ws.auto_filter.ref = f"A1:{get_column_letter(len(hdr))}{ws.max_row}"
freeze_top(ws)
ws.column_dimensions["A"].width = 14
ws.column_dimensions["B"].width = 12
ws.column_dimensions["C"].width = 12
ws.column_dimensions["D"].width = 50
for col in ("E", "F", "G", "H", "I", "J"):
    ws.column_dimensions[col].width = 28

# ---------------------------------------------------------------------------
# 7. Save
# ---------------------------------------------------------------------------
OUT_XLSX.parent.mkdir(parents=True, exist_ok=True)
wb.save(OUT_XLSX)
print(f"\nGravado: {OUT_XLSX}")
print(f"   Sheets: {len(wb.sheetnames)} - {wb.sheetnames}")
