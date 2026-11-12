---
description: Vocabulário completo de um domínio que o livro-texto ignora — mapa, frases, diálogo e CSV
argument-hint: [domínio, ex. "farmácia", "reunião de trabalho", "café de especialidade"]
---

# /tema — domínio fora do livro-texto (Prompt 04, adaptado)

Argumento: `$ARGUMENTS`. Vazio → sugira 5 domínios ligados às situações do objetivo (seção 1 do
perfil) e peça a escolha.

## Antes

Leia `assistente/perfil.md`. Se ainda for o modelo vazio, diga para rodar `/comecar` e pare.
Siga a intenção "domínio fora do livro" da seção 5 do `assistente/metodo.md`, com as regras das
seções 1 e 3. Varra `cartoes/*.csv` para não repetir item já ensinado.

## O que produzir

1. **`temas/AAAA-MM-DD-<slug>.html`** a partir de `modelos/tema.html`: mapa do domínio por subgrupo,
   frases que o aprendiz vai dizer (da mais provável para a menos), diálogo curto, nota cultural.
   Termo técnico com variante coloquial e formal leva as duas.
2. **CSV** em `cartoes/AAAA-MM-DD-<slug>.csv`, fatiado em `-l01`, `-l02`… acima do tamanho do lote.
   Priorize o núcleo utilizável; o que estiver acima do nível leva `challenge`. Diálogo entra turno a
   turno, com tag `dialogo::<slug>`. Tag `tema::<slug>` em todas as linhas.

## Depois

- `python ferramentas/validar_csv.py` nos CSVs; corrija os erros.
- Atualize `temas/index.html`, `cartoes/index.html` e o tracker.
