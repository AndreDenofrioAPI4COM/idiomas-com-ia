---
description: Lista de vocabulário por classe gramatical, em página e CSV prontos para o Anki
argument-hint: [N] [substantivos|verbos|adjetivos|advérbios|…] [contexto opcional]
---

# /vocab — vocabulário por classe (Prompt 02, adaptado)

Argumento: `$ARGUMENTS` — ex.: `50 verbos`, `30 adjetivos de comida`.
Vazio → 30 itens da classe que mais falta para as situações do objetivo.

## Antes

Leia `assistente/perfil.md`. Se ainda for o modelo vazio, diga para rodar `/comecar` e pare.
Siga a intenção "vocabulário por classe" da seção 5 do `assistente/metodo.md`, com as regras das
seções 1 e 3.

## Passos

1. **Deduplicar:** procure cada candidato na coluna `chave` de `cartoes/*.csv`. Item que já existe não
   vira linha nova — a menos que seja outro sentido, e aí entra com `chave` `alvo#sufixo`.
2. Escolha pela **frequência no objetivo do aprendiz**, dentro do nível ou um acima.
3. Gere a página de consulta em `temas/AAAA-MM-DD-<slug>.html` (base `modelos/tema.html`, kicker
   "Vocabulário por classe").
4. Gere o CSV. Até o tamanho do lote do perfil: `cartoes/AAAA-MM-DD-<slug>.csv`. Acima disso, fatie em
   `cartoes/AAAA-MM-DD-<slug>-l01.csv`, `-l02`… com confundíveis em lotes diferentes. Tags
   `bloco::<slug>` e `lote::<slug>::NN`.
5. Rode `python ferramentas/validar_csv.py` nos arquivos gerados e corrija os erros.
6. Atualize `temas/index.html`, `cartoes/index.html` e o tracker (lotes em backlog).
