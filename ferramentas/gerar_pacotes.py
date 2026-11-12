#!/usr/bin/env python3
"""Gera os pacotes iniciais do Anki (.apkg), um por língua.

Cada pacote cria, ao ser importado:
  - o tipo de nota  <Lingua>-IA  (8 campos, cartões Produção + Escuta [+ Leitura])
  - o deck          <Lingua>
  - uma nota de boas-vindas ("obrigado"), que garante que o tipo de nota seja importado

Depois disso, os lotes em CSV (cabeçalho #notetype:<Lingua>-IA) importam direto,
sem mapear coluna nenhuma — inclusive no celular.

Uso:
  python ferramentas/gerar_pacotes.py                      # todos os pacotes prontos
  python ferramentas/gerar_pacotes.py --lingua Holandes --tts nl_NL --obrigado "dank je"
  python ferramentas/gerar_pacotes.py --lingua Grego --tts el_GR --leitura \\
      --obrigado "ευχαριστώ" --pronuncia "efcharistó"

Requer: pip install genanki
"""

import argparse
import hashlib
import sys
from pathlib import Path

try:
    import genanki
except ImportError:
    sys.exit("Falta o genanki. Instale com:  pip install genanki")

RAIZ = Path(__file__).resolve().parent.parent
SAIDA_PADRAO = RAIZ / "anki" / "pacotes"

CAMPOS = ["chave", "alvo", "pronuncia", "traducao", "situacao", "nota", "audio", "mnemonico"]

SITUACAO_OBRIGADO = "alguém segura a porta para você passar"

# nome ASCII, código TTS, cartão de Leitura?, nota de boas-vindas (alvo, pronuncia, traducao, nota)
LINGUAS = [
    ("Ingles", "en_US", False, ("thank you", "", "obrigado(a)", "mais casual: thanks")),
    ("Espanhol", "es_ES", False, ("gracias", "", "obrigado(a)", "resposta comum: de nada")),
    ("Espanhol-America", "es_MX", False, ("gracias", "", "obrigado(a)", "resposta comum: de nada")),
    ("Frances", "fr_FR", False, ("merci", "", "obrigado(a)", "mais enfático: merci beaucoup")),
    ("Alemao", "de_DE", False, ("danke", "", "obrigado(a)", "mais enfático: danke schön")),
    ("Italiano", "it_IT", False, ("grazie", "", "obrigado(a)", "mais enfático: grazie mille")),
    ("Japones", "ja_JP", True, ("ありがとうございます", "arigatō gozaimasu", "obrigado(a) — polido",
                                "entre amigos: ありがとう (arigatō)")),
    ("Mandarim", "zh_CN", True, ("谢谢", "xièxie", "obrigado(a)", "a segunda sílaba é tom neutro")),
    ("Coreano", "ko_KR", True, ("감사합니다", "gamsahamnida", "obrigado(a) — formal",
                                "mais leve: 고마워요 (gomawoyo)")),
    ("Russo", "ru_RU", True, ("спасибо", "spasíbo", "obrigado(a)", "o o final soa quase como a")),
]

CSS = """\
.card {
  font-family: -apple-system, "Segoe UI", Roboto, "Noto Sans", "Noto Sans CJK JP", sans-serif;
  font-size: 22px; line-height: 1.45; text-align: center;
  color: #1f2328; background: #ffffff; padding: 12px;
}
.card.nightMode, .nightMode .card { color: #e6edf3; background: #0d1117; }
.tipo { font-size: 12px; letter-spacing: .08em; text-transform: uppercase; opacity: .55; }
.situacao { font-size: 22px; margin: 18px 0 6px; }
.dica { font-size: 14px; opacity: .55; margin-top: 10px; }
.alvo { font-size: 32px; font-weight: 600; margin: 14px 0 4px; }
.alvo.grande { font-size: 44px; margin-top: 28px; }
.pron { font-size: 18px; opacity: .8; }
.trad { font-size: 18px; margin-top: 8px; }
.nota { font-size: 15px; opacity: .75; margin-top: 14px; }
.mnem { font-size: 15px; margin-top: 14px; padding: 8px; border-radius: 6px;
        background: rgba(255, 196, 0, .15); }
"""


def _audio(tts):
    # Áudio nativo, se o aprendiz colou um; senão, a voz do aparelho.
    return "{{#audio}}{{audio}}{{/audio}}{{^audio}}{{tts %s:alvo}}{{/audio}}" % tts


VERSO_COMUM = """\
<div class="alvo">{{alvo}}</div>
{{#pronuncia}}<div class="pron">{{pronuncia}}</div>{{/pronuncia}}
<div class="trad">{{traducao}}</div>
"""


def templates(tts, leitura):
    t = [
        {
            "name": "Produção",
            # Só {{situacao}} referencia campo: situação vazia = cartão não é criado.
            "qfmt": '<div class="tipo">Produção</div>\n'
                    '<div class="situacao">{{situacao}}</div>\n'
                    '<div class="dica">o que você diz?</div>',
            "afmt": "{{FrontSide}}\n<hr id=answer>\n" + VERSO_COMUM + _audio(tts) + "\n"
                    '{{#nota}}<div class="nota">{{nota}}</div>{{/nota}}\n'
                    '{{#mnemonico}}<div class="mnem">{{mnemonico}}</div>{{/mnemonico}}',
        },
        {
            "name": "Escuta",
            "qfmt": '<div class="tipo">Escuta</div>\n' + _audio(tts) + "\n"
                    '<div class="dica">o que você ouviu?</div>',
            "afmt": "{{FrontSide}}\n<hr id=answer>\n" + VERSO_COMUM +
                    '{{#nota}}<div class="nota">{{nota}}</div>{{/nota}}',
        },
    ]
    if leitura:
        t.append({
            "name": "Leitura",
            "qfmt": '<div class="tipo">Leitura</div>\n<div class="alvo grande">{{alvo}}</div>',
            "afmt": "{{FrontSide}}\n<hr id=answer>\n"
                    '{{#pronuncia}}<div class="pron">{{pronuncia}}</div>{{/pronuncia}}\n'
                    '<div class="trad">{{traducao}}</div>\n' + _audio(tts),
        })
    return t


def id_estavel(texto):
    """Id fixo derivado do nome: regerar o pacote não cria um tipo de nota novo no Anki."""
    h = int(hashlib.sha1(texto.encode("utf-8")).hexdigest()[:8], 16)
    return (1 << 30) + h % (1 << 30)


def gerar(lingua, tts, leitura, boas_vindas, saida):
    alvo, pronuncia, traducao, nota = boas_vindas
    modelo = genanki.Model(
        id_estavel("idiomas-com-ia:modelo:" + lingua),
        f"{lingua}-IA",
        fields=[{"name": c} for c in CAMPOS],
        templates=templates(tts, leitura),
        css=CSS,
        sort_field_index=1,
    )
    # O genanki não entende {{tts …:campo}} e deixaria de criar o cartão de Escuta da nota inicial.
    # Regras explícitas: Produção exige situacao; Escuta e Leitura exigem alvo (ou audio).
    i = CAMPOS.index
    modelo._req = [[0, "all", [i("situacao")]], [1, "any", [i("alvo"), i("audio")]]]
    if leitura:
        modelo._req.append([2, "all", [i("alvo")]])
    deck = genanki.Deck(
        id_estavel("idiomas-com-ia:deck:" + lingua),
        lingua,
        description="Criado pelo Idiomas com IA. Importe aqui os lotes CSV que o assistente gerar.",
    )
    deck.add_note(genanki.Note(
        model=modelo,
        fields=[alvo, alvo, pronuncia, traducao, SITUACAO_OBRIGADO, nota, "", ""],
        tags=["bloco::boas-vindas", "lote::boas-vindas::01", "tipo::frase"],
        guid=genanki.guid_for("idiomas-com-ia", lingua, alvo),
    ))
    saida.mkdir(parents=True, exist_ok=True)
    destino = saida / f"{lingua}.apkg"
    genanki.Package(deck).write_to_file(str(destino))
    cartoes = "Produção + Escuta" + (" + Leitura" if leitura else "")
    print(f"  {destino.relative_to(RAIZ) if destino.is_relative_to(RAIZ) else destino}"
          f"  ·  {lingua}-IA  ·  voz {tts}  ·  {cartoes}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description="Gera os pacotes iniciais do Anki (.apkg).")
    p.add_argument("--lingua", help="nome ASCII, sem espaço nem acento (ex.: Holandes)")
    p.add_argument("--tts", help="código da voz (ex.: nl_NL, pt_PT, el_GR)")
    p.add_argument("--leitura", action="store_true", help="incluir o cartão de Leitura")
    p.add_argument("--obrigado", help='"obrigado" na língua — vira a nota de boas-vindas')
    p.add_argument("--pronuncia", default="", help="transliteração do --obrigado, se houver")
    p.add_argument("--saida", type=Path, default=SAIDA_PADRAO, help="pasta de saída")
    a = p.parse_args()

    if a.lingua:
        if not (a.tts and a.obrigado):
            p.error("--lingua exige --tts e --obrigado")
        if not a.lingua.replace("-", "").isascii() or " " in a.lingua:
            p.error("--lingua deve ser ASCII e sem espaço (ex.: Holandes, Portugues-PT)")
        gerar(a.lingua, a.tts, a.leitura, (a.obrigado, a.pronuncia, "obrigado(a)", ""), a.saida)
        return

    print("Gerando pacotes:")
    for lingua, tts, leitura, boas_vindas in LINGUAS:
        gerar(lingua, tts, leitura, boas_vindas, a.saida)


if __name__ == "__main__":
    main()
