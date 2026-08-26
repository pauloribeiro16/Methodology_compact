# -*- coding: utf-8 -*-
"""
fix_frontmatter.py
- Lê todos os .md do repo (excluindo validation/, .git/, etc.)
- Faz parse real do frontmatter YAML (com PyYAML)
- Para cada ficheiro com erro, aplica o fix mínimo correto
- Reporta o que fez
"""
import re
import sys
from pathlib import Path

try:
    import yaml
    from yaml import YAMLError
except ImportError:
    print("PyYAML não disponível — a instalar via pip")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pyyaml"], check=True)
    import yaml
    from yaml import YAMLError

ROOT = Path(r"C:\Users\paulo.ribeiro\OneDrive - Instituto CCG ZGDV\Ambiente de Trabalho\Methodology-main\Methodology-main")

# Diretórios a excluir da varredura
EXCLUDE_DIRS = {
    ".git", "node_modules", "__pycache__", ".vscode", ".idea",
    "validation",  # relatórios de lint, não documentos AEGIS
    "REPORTS", "Reports",
    "00_NIS2_Mapping",  # os meus outputs
}

# Padrões para excluir (nomes de ficheiro que não devem ser tocados)
EXCLUDE_PATTERNS = [
    re.compile(r"SPRINT\d+_REPORT", re.IGNORECASE),
    re.compile(r"VALIDATOR_SPRINT", re.IGNORECASE),
    re.compile(r"LINT_REPORT", re.IGNORECASE),
    re.compile(r"VALIDATION_REPORT", re.IGNORECASE),
    re.compile(r"RECONCILIATION_REPORT", re.IGNORECASE),
]


def is_excluded(path: Path) -> bool:
    if any(p in path.parts for p in EXCLUDE_DIRS):
        return True
    name = path.name
    if any(pat.search(name) for pat in EXCLUDE_PATTERNS):
        return True
    return False


def has_frontmatter(text: str) -> bool:
    return text.startswith("---") and "\n---" in text[3:]


def extract_frontmatter(text: str):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", text, re.DOTALL)
    if not m:
        return None, None, None
    return m.group(0), m.group(1), m.span(0)


def try_parse_yaml(blob: str):
    try:
        return yaml.safe_load(blob), None
    except YAMLError as e:
        return None, str(e)


def normalize_frontmatter(blob: str) -> str:
    """
    Aplica correções conservadoras ao YAML para resolver os 2 padrões
    de erro mais comuns neste repo:
      1) Comentários HTML `<!-- ... -->` dentro de YAML (inválido)
         → substituídos por comentários YAML `# ...`
      2) Flow sequences `[a, b c, d]` com itens contendo espaços
         sem aspas → cada item fica quoted ("...")
    Mantém comentários YAML `#` intactos. Não toca em mais nada.
    """
    fixed = blob

    # 1) Substituir comentários HTML `<!-- ... -->` por comentários YAML
    # Estratégia segura: se uma linha contém `<!--`, manter só o que vem
    # ANTES do comentário, e converter o resto em comentário YAML.
    new_lines = []
    for line in fixed.splitlines():
        if "<!--" in line:
            # encontra índice do `<!--`; mantém o texto antes como código YAML,
            # e converte o resto em comentário
            idx = line.index("<!--")
            before = line[:idx].rstrip()
            after = re.sub(r"^<!--\s*", "", line[idx + 4:])
            after = re.sub(r"\s*-->$", "", after).strip()
            if after:
                new_lines.append(f"{before}  # {after}")
            else:
                new_lines.append(before)
        else:
            new_lines.append(line)
    fixed = "\n".join(new_lines)

    # 2) Para linhas que começam com `key: [...]` e cujos itens contêm
    # espaços sem aspas, quotar cada item.
    def quote_flow_items(m):
        prefix = m.group(1)  # "key: " ou "key:tag: "
        seq_text = m.group(2)
        # dividir por vírgulas ao top-level (não dentro de parênteses)
        parts = []
        depth = 0
        cur = []
        for ch in seq_text:
            if ch in "([{":
                depth += 1
                cur.append(ch)
            elif ch in ")]}":
                depth -= 1
                cur.append(ch)
            elif ch == "," and depth == 0:
                parts.append("".join(cur).strip())
                cur = []
            else:
                cur.append(ch)
        if cur:
            parts.append("".join(cur).strip())
        # quotar cada item se ainda não tiver aspas e tiver espaços
        new_parts = []
        for p in parts:
            p = p.strip()
            if not p:
                continue
            # já quoted?
            if (p.startswith('"') and p.endswith('"')) or (p.startswith("'") and p.endswith("'")):
                new_parts.append(p)
            elif " " in p or ":" in p and not re.match(r"^\w+:\s", p):
                # tem espaço ou ":" interno (mas não "key: value")
                # escapamos aspas internas e quotamos
                esc = p.replace('"', '\\"')
                new_parts.append(f'"{esc}"')
            else:
                new_parts.append(p)
        return f"{prefix}[{', '.join(new_parts)}]"

    # Match `key: [...]` em uma linha
    fixed = re.sub(
        r"(^[ \t]*\w[\w\-_]*:\s*)\[([^\[\]]*)\]\s*$",
        quote_flow_items,
        fixed,
        flags=re.MULTILINE,
    )

    return fixed


def process_file(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ("encoding_error", None)

    if not has_frontmatter(text):
        return ("no_frontmatter", None)

    full_fm, blob, span = extract_frontmatter(text)
    if blob is None:
        return ("no_frontmatter", None)

    parsed, err = try_parse_yaml(blob)
    if parsed is not None and err is None:
        return ("ok", None)  # já válido

    # Tentar corrigir
    new_blob = normalize_frontmatter(blob)
    new_parsed, new_err = try_parse_yaml(new_blob)
    if new_parsed is None:
        return ("parse_error_after_fix", new_err)

    # Reconstruir ficheiro com frontmatter corrigido
    new_full_fm = f"---\n{new_blob}\n---\n"
    new_text = text[: span[0]] + new_full_fm + text[span[1]:]
    # Garantir que tem newline após o segundo ---
    if not new_text[span[0] + len(new_full_fm):].startswith("\n"):
        new_text = new_text[: span[0] + len(new_full_fm)] + "\n" + new_text[span[0] + len(new_full_fm):]

    path.write_text(new_text, encoding="utf-8")
    return ("fixed", err)


def main():
    files = []
    for path in ROOT.rglob("*.md"):
        if not is_excluded(path):
            files.append(path)

    print(f"A varrer {len(files)} ficheiros .md (excluindo validation/, reports, .git/)...")

    ok = 0
    fixed = 0
    errors = []
    no_fm = 0
    parse_errors = []

    for p in files:
        status, info = process_file(p)
        if status == "ok":
            ok += 1
        elif status == "no_frontmatter":
            no_fm += 1
        elif status == "fixed":
            fixed += 1
            print(f"  FIXED: {p.relative_to(ROOT)}")
            print(f"        erro original: {info[:120] if info else '?'}")
        elif status == "parse_error_after_fix":
            parse_errors.append((p, info))
            print(f"  AINDA COM ERRO: {p.relative_to(ROOT)}")
            print(f"        {info[:200] if info else '?'}")
        elif status == "encoding_error":
            errors.append((p, "encoding"))

    print()
    print(f"Resumo:")
    print(f"  OK (sem erro):              {ok}")
    print(f"  Sem frontmatter:             {no_fm}")
    print(f"  Corrigidos com sucesso:     {fixed}")
    print(f"  Ainda com erro de parse:    {len(parse_errors)}")
    print(f"  Erros de encoding:          {len(errors)}")

    if parse_errors:
        print()
        print("Ficheiros que ainda não consigo parsear (relatório manual):")
        for p, err in parse_errors:
            print(f"  {p.relative_to(ROOT)}")
            print(f"    {err[:200] if err else 'sem detalhe'}")


if __name__ == "__main__":
    main()
