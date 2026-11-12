---
description: Detalha o próximo bloco do plano — página do bloco e todos os lotes em CSV
argument-hint: [bloco a detalhar, ex. "cortesia" — ou "plano" para refazer o plano de blocos]
---

# /curriculo — o plano, bloco a bloco

Argumento: `$ARGUMENTS`.

- Vazio → detalhe **o próximo bloco sem página**, na ordem da seção 5 do perfil.
- Slug de um bloco → detalhe esse.
- `plano` → refaça o plano de blocos (seção 5 do perfil) a partir do objetivo. Só mexa no plano
  quando o argumento pedir.

## Antes

Leia `assistente/perfil.md`. Se ainda for o modelo vazio, diga para rodar `/comecar` e pare.
Leia `assistente/metodo.md` — seções 1, 3, 4 e a intenção "plano e blocos" da seção 5.
Varra `cartoes/*.csv` para saber o que já foi ensinado.

## O que produzir

1. **`curriculo/B<NN>-<slug>.html`**, a partir de `modelos/bloco.html`: situação-alvo, critério de
   pronto (os dois portões), tabela de lotes, frases do bloco agrupadas por tema, glossário que não
   vira cartão, nota cultural se couber.
2. **Todos os lotes do bloco, agora**, em `cartoes/<slug>-l<NN>.csv` (`l01`, `l02`…), no formato da
   seção 3 do `metodo.md` — cabeçalhos `#` do Anki, 7 colunas, tags `bloco::` e `lote::` em toda linha.
   Gerar o bloco inteiro de uma vez é de propósito: material tem que existir quando a energia aparecer.
3. A divisão em lotes segue a seção 4: tamanho do lote do perfil, confundíveis em lotes diferentes,
   variantes do mesmo padrão espalhadas. A página é temática; o lote não.

Dimensione por lotes, nunca por tempo ("executável em 30 minutos" não é medida).

## Depois de gerar

- Rode `python ferramentas/validar_csv.py cartoes/<slug>-l*.csv` e corrija tudo que for erro antes de
  entregar. Aviso se discute com o aprendiz; erro não.
- Atualize `curriculo/index.html`, `cartoes/index.html` e o painel.
- Atualize `progresso/tracker.html`: os lotes novos entram em **backlog** (gerados, não importados).
- Se houver prazo e a data de parar de puxar já passou, diga isso antes de gerar — lote novo depois dela
  não fecha os dois portões a tempo.
- Termine dizendo qual arquivo importar primeiro e lembrando: puxar = importar, um lote de cada vez.
