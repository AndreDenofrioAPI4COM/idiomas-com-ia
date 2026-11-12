---
description: Destrincha um texto autêntico — tradução, vocabulário, glosas Leipzig e CSV
argument-hint: [cole o texto, ou o caminho de um arquivo, ou uma URL]
---

# /leitura — leitura assistida com glosas (Prompt 05, adaptado)

Entrada: `$ARGUMENTS`. Vazio → peça o texto (notícia, página de livro, transcrição de podcast,
cardápio, e-mail). Aceita caminho de arquivo local.

## Antes

Leia `assistente/perfil.md`. Se ainda for o modelo vazio, diga para rodar `/comecar` e pare.
Siga a intenção "texto autêntico" da seção 5 do `assistente/metodo.md`. Abreviações de glosa
específicas da língua estão na seção 3 do perfil.

## O que produzir

1. **`leituras/AAAA-MM-DD-<slug>.html`** a partir de `modelos/leitura.html`: texto original, tradução
   natural recolhida, 15–20 itens desafiadores, expressões fixas à parte, glosas das frases
   estruturalmente interessantes (diga quais pulou e por quê), perguntas de compreensão na
   língua-alvo, estruturas que valem `/gramatica`. **Fonte registrada no rodapé.**
2. **`cartoes/AAAA-MM-DD-<slug>.csv`** com os itens desafiadores, tag `tema::leitura`. A cena de cada
   item pode vir do próprio texto.

## Depois

- `python ferramentas/validar_csv.py` no CSV; corrija os erros.
- Atualize `leituras/index.html`, `cartoes/index.html` e o tracker.
