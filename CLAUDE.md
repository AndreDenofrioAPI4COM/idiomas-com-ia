# CLAUDE.md — Idiomas com IA (rota Claude Code)

Repositório de aprendizado de uma língua conduzido por você, Claude. Você substitui o livro-texto:
gera plano, vocabulário, gramática, leituras e simulações sob demanda. O repositório guarda tudo. O
Anki faz a memória.

## 0. Antes de qualquer coisa

1. **Leia [`assistente/perfil.md`](assistente/perfil.md).** Se ele ainda tiver campos
   `[preencher]`, não gere material: diga ao aprendiz para rodar `/comecar`.
2. **Leia [`assistente/metodo.md`](assistente/metodo.md).** É a fonte única das regras de cartão,
   CSV, lote, sessão, simulação e correção. Os comandos citam as seções dele; **não repita regra de
   cartão em outro lugar** — se uma regra precisar mudar, ela muda lá.
3. Em conflito sobre nível, ritmo ou escopo, **o perfil vence** o método e este arquivo.

O mesmo `assistente/` serve à rota de chat (Projeto no ChatGPT, Claude ou Gemini). Qualquer mudança
nele vale para as duas rotas — mantenha-o legível sem o Claude Code.

## 1. Formatos

| O quê | Formato | Onde |
|---|---|---|
| Docs do framework, perfil, método, comandos, skills | Markdown | raiz, `assistente/`, `docs/`, `.claude/` |
| Material de estudo (bloco, gramática, leitura, história, tema, música, diário, avaliação, tracker, painel) | **HTML** com [`assets/estudo.css`](assets/estudo.css) | pastas de conteúdo, a partir de `modelos/` |
| Cartões | **CSV** no formato da seção 3 de `metodo.md` | `cartoes/` |
| Gravações da própria voz | `.m4a` | `audio/` — **fora do git** |

Convenções das páginas: skill [`notas-html`](.claude/skills/notas-html/SKILL.md). Nada de CSS solto,
JavaScript ou recurso remoto.

## 2. Estrutura

```
assistente/     instrucoes.md · metodo.md · perfil.md   (as duas rotas)
anki/pacotes/   um .apkg por língua
docs/           como-usar · metodo · inspiracao · faq · anki
ferramentas/    validar_csv.py · gerar_pacotes.py
modelos/        modelos HTML das páginas
assets/         estudo.css
.claude/        commands/ · skills/notas-html/ · settings.json

— criadas pelo /comecar —
index.html      painel do aprendiz
curriculo/      uma página por bloco: B01-<slug>.html
cartoes/        lotes CSV: <bloco>-l<NN>.csv · avulsos: AAAA-MM-DD-<slug>.csv (-l<NN> se passar de um lote)
gramatica/ leituras/ historias/ temas/ musicas/
diario/         uma sessão por arquivo: AAAA-MM-DD-N.html
progresso/      tracker.html · avaliacoes/
audio/          AAAA-MM-DD-NN.m4a (fora do git)
```

Slugs em português, minúsculos, sem acento, com hífen. Índice de pasta: sempre `index.html`.

## 3. Comandos

| Comando | O que faz | `metodo.md` |
|---|---|---|
| `/comecar` | entrevista inicial; preenche o perfil e cria as pastas | §2 |
| `/curriculo` | plano de blocos; detalha um bloco e gera seus lotes | §5 |
| `/vocab` | vocabulário por classe | §5 |
| `/gramatica` | ponto gramatical com exercícios | §5 |
| `/tema` | domínio fora do livro-texto | §5 |
| `/leitura` | texto autêntico com glosas | §5 |
| `/historia` | história graduada | §5 |
| `/musica` | letra linha a linha | §5 |
| `/revisao` | sessão da trilha B | §6 |
| `/avaliacao` | simulação em roleplay | §7 |

## 4. Sempre

- Todo conteúdo gerado vira CSV em `cartoes/` — palavras, frases, turnos de diálogo, padrões e
  exercícios. Depois de gravar, rode `python ferramentas/validar_csv.py <arquivo>` e corrija os ERROS.
- Antes de escrever exemplos, consulte `cartoes/` para reusar o que já foi ensinado.
- Explicações na língua das explicações do perfil; exemplos na língua-alvo.
- Dúvida sobre forma ou naturalidade: `⚠️ verificar` na página e tag `verificar` na linha.
- Ao fim de cada sessão com material novo: diário, tracker e o `index.html` da pasta afetada.
- Quando o progresso mudar (lote ou bloco fechado), atualize as seções 5–7 do perfil.

## 5. Nunca

- Cartão de Produção com a tradução na frente, ou nota sem cartão de Produção "porque é difícil".
- Material só na página, sem CSV.
- Declarar a pronúncia do aprendiz boa — você não ouve.
- Escrever ou sugerir o conteúdo de um mnemônico.
- Bloquear o aprendiz por causa do WIP — mostre o custo e respeite a decisão.
- Versionar `audio/`, mídia do Anki ou dados pessoais de terceiros.

## 6. Definição de pronto de uma sessão

- [ ] Material salvo na pasta certa, com o nome certo, a partir do modelo
- [ ] Todo conteúdo novo virou CSV em `cartoes/`, e o validador passou sem ERRO
- [ ] Diário da sessão escrito; tracker e índices atualizados
- [ ] Itens `⚠️ verificar` resolvidos ou listados no diário
