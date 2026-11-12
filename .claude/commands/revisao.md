---
description: Conduz a sessão de estudo (trilha B) — puxa lote, treina a fala, cuida dos leech e registra
argument-hint: [minutos disponíveis, ou "A" / "B"]
---

# /revisao — a sessão do dia

Argumento: `$ARGUMENTS`.

## Antes

Leia `assistente/perfil.md` (se ainda for o modelo vazio, diga para rodar `/comecar` e pare),
`progresso/tracker.html`, o último arquivo de `diario/` e a página do bloco em andamento em
`curriculo/`. Siga as seções 4, 6 e 8 do `assistente/metodo.md`.

**Não pergunte o que estudar — proponha**, a partir de onde o aprendiz parou e do que ficou marcado
como difícil.

## Qual trilha é hoje

Pergunte, ou infira do argumento. Nunca conduza a trilha B por conta própria num dia curto.

- **Trilha A — manutenção:** zerar a fila do Anki, sem cartão novo. Acontece no celular, sem você.
  Se o aprendiz vier dizer que fez, marque o tique no tracker. **Não gera arquivo de diário.**
- **Trilha B — entrada:** o roteiro abaixo.

## Roteiro da trilha B

1. **Fila primeiro.** A fila do Anki é zerada antes de qualquer material novo.
2. **Done dos lotes em fazendo.** Para cada um, peça os dois números da busca da seção 4
   (`card:Produção prop:ivl>=7` contra `card:Produção`, na tag do lote) e a passada de entrega.
   Fechou os dois portões → mova para done no tracker.
3. **Puxar, se houver espaço.** Puxar = importar o próximo CSV do bloco (`cartoes/<bloco>-lNN.csv`) —
   diga o arquivo exato. Com 2 lotes em fazendo, **não bloqueie**: mostre o custo em revisões por dia
   e a data em que a fila chega lá, e deixe o aprendiz decidir.
4. **Ouvir e repetir** o material do lote, no protocolo da seção 6.
5. **Produção verificada**, com os instrumentos da seção 8. Corrija linha a linha.
6. **Leech:** traga a lista de itens errados duas vezes. Você não escreve mnemônico nem sugere
   candidatos. Antes, considere se o cartão está mal recortado — aí o conserto é o recorte, e você
   regera a linha com a mesma `chave`.
7. **Gravação da semana:** na primeira sessão de trilha B de cada semana de calendário, peça a
   gravação de 1 minuto — arquivo em `audio/AAAA-MM-DD-NN.m4a` (pasta fora do git). Semana sem
   gravação é registrada como falha no diário.

## Fechamento

- **`diario/AAAA-MM-DD-N.html`** a partir de `modelos/diario.html` — uma sessão por arquivo, `N`
  sequencial no dia. Atualize `diario/index.html`.
- **`progresso/tracker.html`**: quadro (backlog/fazendo/done), streak da trilha A, burn-down se houver
  prazo, gravação da semana. Burn-down projetando o fim depois do prazo é dito em voz alta na sessão,
  não só na tabela.
- **Perfil:** seção 6 (progresso) e seção 7 (erro que apareceu pela 3ª vez no diário vira dificuldade
  recorrente).
- Linha corrigida ou nova → CSV em `cartoes/` e `python ferramentas/validar_csv.py` nele.
