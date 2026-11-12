#!/usr/bin/env python3
"""Confere os lotes CSV antes de importar no Anki.

Pega o que a importação não avisa: linha com coluna a mais, chave repetida (que sobrescreve
outra nota em silêncio), cartão de Produção sem situação, lote sem tag, variantes no mesmo lote.

Uso:
  python ferramentas/validar_csv.py                 # tudo em cartoes/
  python ferramentas/validar_csv.py cartoes/cortesia-l01.csv
  python ferramentas/validar_csv.py --max-lote 20 cartoes/

Saída: ERRO impede a importação correta; AVISO é regra do método que vale conferir.
Código de saída 1 se houver qualquer ERRO. Só biblioteca padrão.
"""

import argparse
import csv
import io
import re
import sys
from collections import defaultdict
from pathlib import Path

COLUNAS = ["chave", "alvo", "pronuncia", "traducao", "situacao", "nota", "tags"]
TIPOS = {"palavra", "frase", "dialogo", "padrao", "exercicio"}
CABECALHOS_FIXOS = {
    "separator": "comma",
    "html": "false",
    "columns": ",".join(COLUNAS),
    "tags column": "7",
}
HTML = re.compile(r"<\s*/?\s*[a-zA-Z][^>]*>")


class Relatorio:
    def __init__(self):
        self.erros = 0
        self.avisos = 0

    def erro(self, onde, msg):
        self.erros += 1
        print(f"  ERRO   {onde}: {msg}")

    def aviso(self, onde, msg):
        self.avisos += 1
        print(f"  AVISO  {onde}: {msg}")


def ler(caminho, rel):
    bruto = caminho.read_bytes()
    if bruto.startswith(b"\xef\xbb\xbf"):
        rel.erro(caminho.name, "arquivo com BOM — salve como UTF-8 sem BOM")
        bruto = bruto[3:]
    try:
        texto = bruto.decode("utf-8")
    except UnicodeDecodeError as e:
        rel.erro(caminho.name, f"não é UTF-8 ({e})")
        return None, []

    cabecalhos, dados = {}, []
    linhas = texto.splitlines(keepends=True)
    i = 0
    while i < len(linhas) and linhas[i].startswith("#"):
        chave, _, valor = linhas[i][1:].rstrip("\r\n").partition(":")
        cabecalhos[chave.strip().lower()] = valor.strip()
        i += 1
    leitor = csv.reader(io.StringIO("".join(linhas[i:])))
    for n, linha in enumerate(leitor, start=i + 1):
        dados.append((n, linha))
    return cabecalhos, dados


def validar_arquivo(caminho, rel, max_lote, chaves_globais):
    print(caminho)
    cabecalhos, dados = ler(caminho, rel)
    if cabecalhos is None:
        return
    nome = caminho.name

    for k, esperado in CABECALHOS_FIXOS.items():
        if cabecalhos.get(k, "").lower() != esperado.lower():
            rel.erro(nome, f"cabeçalho #{k}:{esperado} ausente ou diferente "
                           f"(achei: {cabecalhos.get(k, '—')!r})")
    tipo_nota = cabecalhos.get("notetype", "")
    if not tipo_nota:
        rel.erro(nome, "falta #notetype:<Lingua>-IA")
    elif not tipo_nota.endswith("-IA"):
        rel.aviso(nome, f"#notetype:{tipo_nota} não segue o padrão <Lingua>-IA dos pacotes")
    if not cabecalhos.get("deck"):
        rel.erro(nome, "falta #deck:<Lingua>")
    if not dados:
        rel.erro(nome, "nenhuma linha de dados")
        return
    if dados[0][1][:2] == ["chave", "alvo"]:
        rel.erro(nome, "a primeira linha é um cabeçalho comum — ele viraria uma nota; use só #columns")

    chaves = {}
    lotes = defaultdict(int)
    pares = defaultdict(list)
    for n, campos in dados:
        onde = f"{nome}:{n}"
        if not any(c.strip() for c in campos):
            rel.erro(onde, "linha em branco")
            continue
        if len(campos) != len(COLUNAS):
            rel.erro(onde, f"{len(campos)} colunas, esperado {len(COLUNAS)} — vírgula sem aspas?")
            continue
        r = dict(zip(COLUNAS, (c.strip() for c in campos)))
        tags = r["tags"].split()

        for obrigatorio in ("chave", "alvo", "traducao"):
            if not r[obrigatorio]:
                rel.erro(onde, f"'{obrigatorio}' vazio")
        if r["chave"] and r["alvo"] and r["chave"] != r["alvo"] \
                and not r["chave"].startswith(r["alvo"] + "#"):
            rel.erro(onde, f"chave {r['chave']!r} deveria ser o alvo, ou alvo#sufixo")
        if r["chave"] in chaves:
            rel.erro(onde, f"chave repetida (linha {chaves[r['chave']]}) — uma sobrescreveria a outra")
        chaves[r["chave"]] = n
        anterior = chaves_globais.get((tipo_nota, r["chave"]))
        if anterior and anterior[0] != nome:
            rel.aviso(onde, f"chave já existe em {anterior[0]}:{anterior[1]} — "
                            "importar este arquivo vai ATUALIZAR aquela nota")
        chaves_globais.setdefault((tipo_nota, r["chave"]), (nome, n))

        if not r["situacao"] and "reconhecimento" not in tags:
            rel.erro(onde, "'situacao' vazia — sem ela não há cartão de Produção "
                           "(só permitido com a tag reconhecimento)")
        if r["situacao"] and r["traducao"] and r["situacao"].lower() == r["traducao"].lower():
            rel.aviso(onde, "a situação é igual à tradução — a frente deve ser uma cena, não a glosa")
        for campo in COLUNAS:
            if HTML.search(r[campo]):
                rel.erro(onde, f"HTML no campo '{campo}' (o arquivo é #html:false)")

        lote = [t for t in tags if t.startswith("lote::")]
        tipo = [t.split("::", 1)[1] for t in tags if t.startswith("tipo::")]
        if not any(t.startswith("bloco::") for t in tags):
            rel.erro(onde, "falta a tag bloco::<slug>")
        if len(lote) != 1:
            rel.erro(onde, "precisa de exatamente uma tag lote::<bloco>::NN")
        else:
            lotes[lote[0]] += 1
        if len(tipo) != 1 or tipo[0] not in TIPOS:
            rel.erro(onde, f"precisa de uma tag tipo:: entre {', '.join(sorted(TIPOS))}")
        for t in tags:
            if t.startswith("par::") and lote:
                pares[(lote[0], t)].append(n)

    if len(lotes) > 1:
        rel.aviso(nome, f"{len(lotes)} lotes no mesmo arquivo — o padrão é um arquivo por lote")
    for lote, total in lotes.items():
        if total > max_lote:
            rel.aviso(nome, f"{lote} tem {total} linhas (máximo recomendado: {max_lote})")
    for (lote, par), linhas in pares.items():
        if len(linhas) > 1:
            rel.aviso(nome, f"variantes de {par} no mesmo lote (linhas {linhas}) — "
                            "confundíveis devem ir para lotes diferentes")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description="Confere lotes CSV antes de importar no Anki.")
    p.add_argument("caminhos", nargs="*", type=Path, default=[Path("cartoes")],
                   help="arquivos .csv ou pastas (padrão: cartoes/)")
    p.add_argument("--max-lote", type=int, default=15, help="linhas por lote (padrão: 15)")
    a = p.parse_args()

    arquivos = []
    for c in a.caminhos:
        if c.is_dir():
            arquivos += sorted(c.rglob("*.csv"))
        elif c.is_file():
            arquivos.append(c)
        else:
            print(f"não encontrado: {c}")
    if not arquivos:
        sys.exit("Nenhum CSV para validar.")

    rel = Relatorio()
    chaves_globais = {}
    for arq in arquivos:
        validar_arquivo(arq, rel, a.max_lote, chaves_globais)

    print(f"\n{len(arquivos)} arquivo(s) · {rel.erros} erro(s) · {rel.avisos} aviso(s)")
    sys.exit(1 if rel.erros else 0)


if __name__ == "__main__":
    main()
