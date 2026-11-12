---
description: Simulação em roleplay das situações do objetivo — mede se sai da boca, não se a prova é passada
argument-hint: [cena a simular, ex. "check-in no hotel" — ou "ensaio geral"]
---

# /avaliacao — simulação, não prova

Alvo: `$ARGUMENTS`. Vazio → a cena do bloco que acabou de fechar. `ensaio geral` → todas as cenas do
objetivo, ponta a ponta, sem consulta.

## Antes

Leia `assistente/perfil.md` (se ainda for o modelo vazio, diga para rodar `/comecar` e pare) — as
cenas vêm da seção 1, o objetivo. Siga a seção 7 do `assistente/metodo.md`.

**Só entra o que está no repositório:** varra `curriculo/` e `cartoes/*.csv`. Simulação que cobra o
que não foi ensinado não mede nada.

## Como conduzir

Roleplay em turnos: você faz o outro lado da cena. O aprendiz responde **falando** — como você não
ouve, ele digita o que diria ou usa o ditado por voz do teclado na língua-alvo. Hesitação conta como
falha: na situação real não há tempo para consultar.

Mede-se, em ordem: (1) saiu ou não saiu; (2) estava certo — forma, ordem, registro, escolha da fórmula;
(3) pronúncia **não é avaliada aqui**. Nunca diga que a pronúncia está boa.

## Veredito

Um, explícito: ✅ pronto para a cena · ⚠️ sai, mas trava · 🔁 não sai. Seja honesto: inflar aqui custa
a situação real, não uma nota.

## Saída

- **`progresso/avaliacoes/AAAA-MM-DD-<slug>.html`** a partir de `modelos/avaliacao.html`: a cena, a
  transcrição, os erros linha a linha com a versão que um nativo diria, o veredito (deixe só o que vale).
- **`progresso/tracker.html`**: a simulação na lista.
- Falha que se repete pela 3ª vez → seção 7 do perfil (dificuldades recorrentes).
- Erro que pede cartão novo ou recortado → linha em `cartoes/`, validada com
  `python ferramentas/validar_csv.py`.
- Não mexa no objetivo do perfil por causa de uma simulação.
