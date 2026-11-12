---
description: História graduada no nível exato do aprendiz, com challenge words, perguntas e CSV
argument-hint: [tema da história] [nível opcional]
---

# /historia — história graduada (Prompt 06, adaptado)

Argumento: `$ARGUMENTS`. Vazio → tema ligado ao bloco em andamento.

## Antes

Leia `assistente/perfil.md`. Se ainda for o modelo vazio, diga para rodar `/comecar` e pare.
Siga a intenção "história graduada" da seção 5 do `assistente/metodo.md`. O que já foi ensinado é o
que está em `cartoes/*.csv` — é contra isso que se calibra o "90% conhecido".

## O que produzir

1. **`historias/AAAA-MM-DD-<slug>.html`** a partir de `modelos/historia.html`: a história sem apoio,
   versão com pronúncia recolhida (`<ruby>` se a língua tiver transliteração), challenge words com
   `<span class="challenge">`, perguntas na língua-alvo com gabarito, tradução recolhida por último.
2. **`cartoes/AAAA-MM-DD-<slug>.csv`** com as challenge words (tag `challenge`), cada uma com a cena
   tirada da própria história.

## Depois

- `python ferramentas/validar_csv.py` no CSV; corrija os erros.
- Atualize `historias/index.html`, `cartoes/index.html` e o tracker.
- Sugira ouvir a história em voz sintetizada (leitor do celular ou do navegador) — vira treino de escuta.
