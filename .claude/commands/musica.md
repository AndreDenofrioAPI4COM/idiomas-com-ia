---
description: Transforma a letra de uma música em lição — linha a linha, com tradução, notas e CSV
argument-hint: [cole a letra, ou "artista - música"]
---

# /musica — aprender com música (Prompt 07, adaptado)

Argumento: `$ARGUMENTS`. Se vier só o nome da música, **peça a letra** — não reconstrua de memória.
Letra errada ensina errado.

## Antes

Leia `assistente/perfil.md`. Se ainda for o modelo vazio, diga para rodar `/comecar` e pare.
Siga a intenção "música" da seção 5 do `assistente/metodo.md`.

## O que produzir

1. **`musicas/<artista>-<slug>.html`** a partir de `modelos/musica.html`: ficha (título, artista, ano,
   por que serve para estudo), linha a linha com tradução idiomática, vocabulário-chave útil fora da
   música, notas de canção (licença poética, elisões), três versos para decorar inteiros, nota cultural
   se a letra depender de referência local.
2. **`cartoes/AAAA-MM-DD-<slug>.csv`** com o vocabulário-chave e os três versos, tag `tema::musica`.

Letra tem direito autoral. Ela fica no repositório do aprendiz para estudo; se o repositório dele for
público, avise que a página não deve ir para lá com a letra inteira.

## Depois

- `python ferramentas/validar_csv.py` no CSV; corrija os erros.
- Atualize `musicas/index.html`, `cartoes/index.html` e o tracker.
