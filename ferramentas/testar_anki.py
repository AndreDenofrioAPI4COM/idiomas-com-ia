#!/usr/bin/env python3
"""Testa os pacotes e o formato CSV contra o motor oficial do Anki.

O motor (biblioteca `anki`) é o mesmo do Anki de computador, do AnkiMobile e do AnkiDroid. O teste
simula um aparelho com coleção vazia e confere o que a documentação do método promete:

  1. o pacote cria o tipo de nota, o deck e os cartões certos;
  2. uma versão nova do pacote (voz e estilo trocados) atualiza o molde no lugar, sem duplicar;
  3. um lote CSV escolhe tipo de nota, deck e tags sozinho pelos cabeçalhos; situação vazia não gera
     cartão de Produção;
  4. reimportar um CSV corrigido atualiza a nota e preserva `audio` e `mnemonico`;
  5. o pacote de escrita não latina gera o cartão de Leitura;
  6. o validador aceita o lote de teste.

Uso:
  pip install anki genanki
  python ferramentas/testar_anki.py
"""

import csv
import importlib.util
import subprocess
import sys
import tempfile
import time
from pathlib import Path

try:
    from anki.collection import (Collection, ImportAnkiPackageOptions,
                                 ImportAnkiPackageRequest, ImportCsvRequest)
except ImportError:
    sys.exit("Falta a biblioteca do Anki. Instale com:  pip install anki genanki")

RAIZ = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("gerar_pacotes", RAIZ / "ferramentas" / "gerar_pacotes.py")
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)

CABECALHOS = ["#separator:comma", "#html:false", "#notetype:{tipo}", "#deck:{deck}",
              "#columns:chave,alvo,pronuncia,traducao,situacao,nota,tags", "#tags column:7"]
falhas = []


def checa(ok, msg):
    print(("  ok     " if ok else "  FALHA  ") + msg)
    if not ok:
        falhas.append(msg)


def importa_pacote(col, caminho):
    return col.import_anki_package(ImportAnkiPackageRequest(
        package_path=str(caminho), options=ImportAnkiPackageOptions()))


def importa_csv(col, caminho):
    meta = col.get_csv_metadata(path=str(caminho), delimiter=None)
    col.import_csv(ImportCsvRequest(path=str(caminho), metadata=meta))
    return meta


def escreve_csv(caminho, tipo, deck, linhas):
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        for c in CABECALHOS:
            f.write(c.format(tipo=tipo, deck=deck) + "\n")
        csv.writer(f, lineterminator="\n").writerows(linhas)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    boas_vindas = {nome: (tts, leitura, bv) for nome, tts, leitura, bv in G.LINGUAS}

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        col = Collection(str(tmp / "aparelho.anki2"))

        print("1. pacote Espanhol-America")
        tts, leitura, bv = boas_vindas["Espanhol-America"]
        G.gerar("Espanhol-America", tts, leitura, bv, tmp / "v1")
        importa_pacote(col, tmp / "v1" / "Espanhol-America.apkg")
        tipo = col.models.by_name("Espanhol-America-IA")
        checa(tipo is not None, "tipo de nota Espanhol-America-IA criado")
        checa([f["name"] for f in tipo["flds"]] == G.CAMPOS, "8 campos, na ordem do método")
        checa(col.decks.id_for_name("Espanhol-America") is not None, "deck Espanhol-America criado")
        cartoes = sorted(col.get_card(c).template()["name"]
                         for c in col.find_cards('"deck:Espanhol-America"'))
        checa(cartoes == ["Escuta", "Produção"], f"nota inicial com Produção + Escuta ({cartoes})")

        print("2. versão nova do pacote")
        time.sleep(1.1)
        css_original = G.CSS
        G.CSS += "\n.versao-nova {}"
        G.gerar("Espanhol-America", "es_US", leitura, bv, tmp / "v2")
        G.CSS = css_original
        log = importa_pacote(col, tmp / "v2" / "Espanhol-America.apkg").log
        col.close()  # reabrir descarta o cache de tipos de nota do lado Python
        col = Collection(str(tmp / "aparelho.anki2"))
        tipos =[n.name for n in col.models.all_names_and_ids() if n.name.startswith("Espanhol-America")]
        checa(tipos == ["Espanhol-America-IA"], f"nenhum tipo de nota duplicado ({tipos})")
        tipo = col.models.by_name("Espanhol-America-IA")
        checa("es_US" in tipo["tmpls"][1]["qfmt"] and ".versao-nova" in tipo["css"],
              "molde atualizado no lugar (voz e estilo novos)")
        checa(len(log.conflicting) == 0, "nenhuma nota em conflito")

        print("3. lote CSV")
        lote = tmp / "cortesia-l01.csv"
        escreve_csv(lote, "Espanhol-America-IA", "Espanhol-America", [
            ["mucho gusto", "mucho gusto", "", "prazer", "alguém se apresenta e aperta a sua mão",
             "responde-se: igualmente", "bloco::cortesia lote::cortesia::01 tipo::frase"],
            ["salida", "salida", "", "saída", "", "placa",
             "bloco::cortesia lote::cortesia::01 tipo::palavra reconhecimento"],
            ["punto#hora", "punto", "", "ponto (nas horas)", "perguntam a hora e são três em ponto",
             "las tres en punto", "bloco::cortesia lote::cortesia::01 tipo::palavra"],
        ])
        meta = importa_csv(col, lote)
        checa(meta.dupe_resolution == 0, "padrão da importação: atualizar nota existente")
        notas = col.find_notes("tag:lote::cortesia::01")
        checa(len(notas) == 3, f"3 notas, inclusive a de chave com sufixo ({len(notas)})")
        checa(all(col.get_note(n).note_type()["name"] == "Espanhol-America-IA" for n in notas),
              "tipo de nota escolhido pelo cabeçalho")
        checa(all(col.decks.name(col.get_card(c).did) == "Espanhol-America"
                  for c in col.find_cards("tag:lote::cortesia::01")), "deck escolhido pelo cabeçalho")
        checa(len(col.find_cards("tag:lote::cortesia::01 card:Produção")) == 2,
              "situação vazia (placa) não gera cartão de Produção")
        checa(len(col.find_cards("tag:lote::cortesia::01 card:Escuta")) == 3, "toda nota gera Escuta")

        print("4. reimportar um CSV corrigido")
        nota = col.get_note(col.find_notes('"chave:mucho gusto"')[0])
        nota["mnemonico"], nota["audio"] = "o meu gancho", "[sound:nativo.mp3]"
        col.update_note(nota)
        escreve_csv(lote, "Espanhol-America-IA", "Espanhol-America", [
            ["mucho gusto", "mucho gusto", "", "prazer", "alguém se apresenta e aperta a sua mão",
             "resposta: igualmente; el gusto es mío", "bloco::cortesia lote::cortesia::01 tipo::frase"],
        ])
        importa_csv(col, lote)
        nota = col.get_note(nota.id)
        checa(len(col.find_notes("tag:lote::cortesia::01")) == 3, "nenhuma nota duplicada")
        checa("el gusto es mío" in nota["nota"], "campo corrigido atualizado")
        checa(nota["mnemonico"] == "o meu gancho" and nota["audio"] == "[sound:nativo.mp3]",
              "audio e mnemonico preservados (não têm coluna no CSV)")

        print("5. pacote com Leitura (Japones)")
        tts, leitura, bv = boas_vindas["Japones"]
        G.gerar("Japones", tts, leitura, bv, tmp / "v1")
        importa_pacote(col, tmp / "v1" / "Japones.apkg")
        jp = tmp / "japones-l01.csv"
        escreve_csv(jp, "Japones-IA", "Japones", [
            ["すみません", "すみません", "sumimasen", "com licença; desculpe",
             "você precisa passar entre duas pessoas no corredor", "",
             "bloco::cortesia lote::cortesia::01 tipo::frase"]])
        importa_csv(col, jp)
        cartoes = sorted(col.get_card(c).template()["name"]
                         for c in col.find_cards('"deck:Japones" tag:lote::cortesia::01'))
        checa(cartoes == ["Escuta", "Leitura", "Produção"], f"Produção + Escuta + Leitura ({cartoes})")
        col.close()

        print("6. validador")
        escreve_csv(lote, "Espanhol-America-IA", "Espanhol-America", [
            ["gracias", "gracias", "", "obrigado(a)", "alguém segura a porta para você passar", "",
             "bloco::cortesia lote::cortesia::01 tipo::frase"]])
        r = subprocess.run([sys.executable, str(RAIZ / "ferramentas" / "validar_csv.py"), str(lote)],
                           capture_output=True, text=True, encoding="utf-8")
        checa(r.returncode == 0, "validar_csv.py aceita um lote correto")

    print(f"\n{len(falhas)} falha(s)")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
