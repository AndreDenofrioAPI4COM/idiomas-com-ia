---
description: Explica um ponto gramatical com a forma, exemplos, contraste com a sua língua e exercícios que viram cartão
argument-hint: [ponto gramatical, ex. "pretérito perfeito" ou "partícula は"]
---

# /gramatica — explicação de gramática (Prompt 03, adaptado)

Argumento: `$ARGUMENTS`. Vazio → o próximo ponto que aparece nas frases do bloco em andamento e ainda
não tem página em `gramatica/`.

## Antes

Leia `assistente/perfil.md`. Se ainda for o modelo vazio, diga para rodar `/comecar` e pare.
Siga a intenção "gramática" da seção 5 do `assistente/metodo.md` — inclusive a adaptação: língua que
flexiona mostra paradigma; língua que não flexiona mostra a construção em slots.
Só entra ponto que aparece no que o aprendiz vai **dizer** ou **ouvir** no objetivo.

## O que produzir

1. **`gramatica/<slug>.html`** a partir de `modelos/gramatica.html`: a forma, por que o falante a
   escolhe, exemplos só com o que já foi ensinado (confira `cartoes/*.csv`), onde a língua do
   aprendiz atrapalha, erros típicos, vizinhos que se confundem, exercícios com gabarito recolhido.
2. **`cartoes/AAAA-MM-DD-<slug>.csv`**: os exemplos como `tipo::padrao` (fórmula em `situacao`) e os
   exercícios como `tipo::exercicio` (enunciado em `situacao`, resposta em `alvo`) — exercício e
   gabarito são a mesma linha. Fatie em `-l01`, `-l02`… se passar do tamanho do lote.

## Depois

- `python ferramentas/validar_csv.py` nos CSVs gerados; corrija os erros.
- Atualize `gramatica/index.html`, `cartoes/index.html` e o tracker.
