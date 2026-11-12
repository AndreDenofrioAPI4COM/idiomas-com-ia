# Como usar

Há dois jeitos de rodar o mesmo método. Escolha um — dá para trocar depois sem perder nada,
porque os cartões ficam no Anki, não no assistente.

| | Rota 1 — Chat | Rota 2 — Claude Code |
|---|---|---|
| Para quem | qualquer pessoa, inclusive quem só tem celular | quem já usa o Claude Code no computador |
| Onde o assistente roda | um Projeto no ChatGPT, no Claude ou um Gem no Gemini | este repositório, clonado na sua máquina |
| O que fica guardado | o perfil (você reenvia quando muda) e o Anki | tudo: perfil, páginas de estudo, diário, placar, CSVs |
| Esforço de configuração | ~20 minutos, uma vez | ~30 minutos, uma vez |
| Recomendação | **comece aqui** | se você quer o histórico completo em arquivos |

As duas rotas leem o mesmo manual: [`assistente/metodo.md`](../assistente/metodo.md). O que muda
é só onde as coisas ficam salvas.

---

## Rota 1 — Chat (padrão)

### O que você precisa

- **Anki** — o programa de cartões com repetição espaçada.
  - iPhone/iPad: **AnkiMobile** (pago, compra única — ajuda a financiar o desenvolvimento do Anki).
  - Android: **AnkiDroid** (grátis).
  - Computador: **Anki** em [apps.ankiweb.net](https://apps.ankiweb.net) (grátis).
  - Use a versão atual do app. A voz automática dos cartões exige AnkiMobile 2.0.56+, AnkiDroid 2.17+
    ou Anki 2.1.20+; os cabeçalhos que deixam a importação automática exigem Anki 2.1.54+.
- **Uma conta num assistente com Projetos**: ChatGPT (Projetos), Claude (Projetos) ou Gemini (Gems).
  O plano grátis serve para começar; o pago dá mais mensagens e criação de arquivo mais confiável.

### Passo 1 — Baixe os três arquivos do assistente

Os arquivos ficam na pasta [`assistente/`](../assistente/):

| Arquivo | Para quê |
|---|---|
| `instrucoes.md` | você **cola** o conteúdo nas instruções do Projeto |
| `metodo.md` | você **envia** como arquivo do Projeto — é o manual que o assistente consulta |
| `perfil.md` | você **envia** como arquivo do Projeto — o modelo vazio que a entrevista preenche |

- **No computador:** na página do repositório, botão verde **Code → Download ZIP**, e descompacte.
- **No celular:** abra cada arquivo no GitHub, toque em **Raw**, e use **Compartilhar → Salvar em Arquivos**
  (iPhone) ou **Baixar** (Android). Para o `instrucoes.md` basta abrir o Raw e copiar o texto.

### Passo 2 — Crie o Projeto

**ChatGPT** — menu lateral → **Projetos → Novo projeto**. Dê um nome ("Espanhol", por exemplo).
Em **Instruções**, cole o texto de `instrucoes.md`. Em **Arquivos**, envie `metodo.md` e `perfil.md`.
No plano grátis um Projeto aceita até 5 arquivos — este método usa 2.

**Claude** — em claude.ai, **Projetos → Criar projeto**. Cole `instrucoes.md` em **Instruções do projeto**
e envie `metodo.md` e `perfil.md` em **Conhecimento do projeto**.

**Gemini** — em gemini.google.com (no navegador; depois o Gem aparece no app), **Gems → Novo Gem**.
Cole `instrucoes.md` nas instruções e envie os dois arquivos como conhecimento.

### Passo 3 — A entrevista

Abra uma conversa **dentro do Projeto** e escreva: **começar**.

O assistente faz perguntas, poucas de cada vez: que língua (e qual variante — espanhol da Argentina
não é o da Espanha), **para quê** (viagem, trabalho, mudança, família, prova, prazer), até quando, o que
você já sabe, que outras línguas fala, se precisa ler e escrever ou só falar, como é a sua rotina de
verdade, e o que fica de fora. Responda com sinceridade, inclusive sobre a rotina — o método foi feito
para dias irregulares, não para um dia ideal que não existe.

A pergunta que mais pesa é **"para quê"**. Ela decide o que você vai aprender primeiro. Quem vai a um
jantar de negócios precisa de brinde e cortesia antes de pedir comida; quem vai morar fora precisa de
aluguel e banco antes de small talk.

No fim, o assistente entrega o **`perfil.md` preenchido** e uma proposta de plano em blocos.

### Passo 4 — Troque o perfil no Projeto

Baixe o `perfil.md` que o assistente gerou e **substitua** o arquivo vazio nos arquivos do Projeto.
Isso é o que faz o assistente lembrar de você nas próximas conversas — conversas novas não enxergam as
antigas, mas enxergam os arquivos do Projeto.

Repita este passo sempre que o assistente atualizar o perfil (ao fechar um bloco, ou quando você mudar
de objetivo).

### Passo 5 — Importe o pacote da sua língua

Em [`anki/pacotes/`](../anki/pacotes/) há um arquivo `.apkg` por língua (`Espanhol.apkg`,
`Ingles.apkg`, `Japones.apkg`…). Baixe o da sua e abra com o Anki:

- **iPhone:** toque no arquivo → **Compartilhar → Anki** (ou "Abrir em AnkiMobile").
- **Android:** toque no arquivo → abrir com **AnkiDroid**.
- **Computador:** dois cliques no arquivo, ou **Arquivo → Importar**.

O pacote cria duas coisas: o **tipo de nota** `<Lingua>-IA` (o molde dos cartões) e o **deck** `<Lingua>`.
Faça isso **uma vez**, antes do primeiro CSV — é o molde que o CSV procura.

Sua língua não está na pasta? Veja [Criar um pacote para outra língua](anki.md#criar-um-pacote-para-outra-língua).

### Passo 6 — Configure o deck

Nas opções do deck da língua (detalhes em [anki.md](anki.md#opções-do-deck)):

- **Novos cartões por dia: 30** — o freio de verdade é o lote, não este número.
- **Máximo de revisões por dia: 9999** — revisão nunca fica para amanhã.
- **Novos cartões depois das revisões.**

### Passo 7 — Peça o primeiro bloco

Escreva: **monta meu plano** (se ainda não montou) e depois **próximo bloco**.

Um **bloco** é um pedaço de conteúdo com assunto próprio, amarrado a uma situação do seu objetivo:
cortesia, apresentação, restaurante. O assistente explica o bloco na conversa e entrega o primeiro
**lote** — um arquivo CSV com até 15 itens, que é o que entra no Anki de uma vez.

### Passo 8 — Importe o lote

Abra o arquivo CSV com o Anki, do mesmo jeito do pacote ("Compartilhar → Anki" no iPhone, "Abrir com
AnkiDroid" no Android). As linhas que começam com `#` no topo do arquivo já dizem ao Anki o tipo de
nota, o deck e onde estão as tags — a tela de importação vem pré-preenchida. Confira só uma coisa: que
notas existentes sejam **atualizadas** (é o padrão).

**Importar é "puxar".** Lote importado está em andamento; lote que ainda não foi importado espera sem
custo nenhum. Por isso o assistente pode gerar o bloco inteiro de uma vez e você importa um lote por
vez, quando tiver energia.

### Passo 9 — O dia: duas trilhas

| | Trilha A — manutenção | Trilha B — entrada |
|---|---|---|
| Quando | **todo dia**, sem exceção | quando houver energia |
| Duração | o que a fila pedir — às vezes 3 minutos | 20 minutos a 2 horas |
| Onde | Anki no celular, sem assistente | conversa no Projeto: **sessão de hoje** |
| O que entra | zerar a fila de revisão. Só isso | puxar lote, ouvir e repetir, produção corrigida, itens difíceis, fechamento |

**A regra do dia ruim:** se o tempo acabou, zere a fila e não importe lote novo — nunca o contrário.
Pular material novo custa um dia de plano. Pular revisão custa parte do que você já aprendeu e engorda
a fila de amanhã. O porquê está em [O método → As duas trilhas](metodo.md#as-duas-trilhas).

### Passo 10 — Feche um lote

Um lote está **pronto** quando passa em dois portões:

1. **No Anki:** pelo menos 90% dos cartões de Produção do lote com intervalo de 7 dias ou mais.
   A conta é uma busca — compare `tag:lote::cortesia::01 card:Produção prop:ivl>=7` com
   `tag:lote::cortesia::01 card:Produção` (troque pelo nome do seu lote).
2. **Em voz alta:** você diz o lote inteiro, sem ler, no ritmo, sem hesitar. Ou sai ou não sai.

Lote pronto libera espaço para o próximo. A recomendação é ter **no máximo 2 lotes em andamento** — não
é trava; se você puxar um terceiro, o assistente diz quanto a fila diária vai crescer.

### Passo 11 — Feche um bloco: "me testa"

Quando os lotes de um bloco estiverem prontos, escreva **me testa**. O assistente faz um roleplay da
situação do bloco (o garçom, o recepcionista, o colega novo) e dá um veredito: pronto, sai mas trava,
ou não sai. Quando o objetivo estiver perto, peça **ensaio geral**: todas as cenas, de ponta a ponta,
sem consulta.

### Passo 12 — Atualize o perfil

Ao fechar um bloco, peça **atualiza meu perfil**. O assistente devolve o `perfil.md` com o progresso e
as dificuldades recorrentes. Substitua o arquivo no Projeto (Passo 4).

### Diferenças práticas entre as plataformas

| | ChatGPT | Claude | Gemini |
|---|---|---|---|
| Entrega o CSV como arquivo | sim, com link de download | sim, quando a criação de arquivos está ligada | em geral mostra o texto num bloco |
| Se o arquivo não vier | peça "gera o arquivo de novo"; no celular o app costuma baixar melhor que o navegador | peça o arquivo; se não houver criação de arquivos no seu plano, ele mostra o bloco de texto | copie o bloco e salve como `.csv` |
| Instruções | campo **Instruções** do Projeto | **Instruções do projeto** | instruções do Gem |

**Salvar texto como `.csv` no celular** exige um app editor de texto. Se essa for a sua situação o tempo
todo, prefira uma plataforma que entregue o arquivo pronto, ou importe pelo computador.

---

## Rota 2 — Claude Code

### O que você precisa

- **Claude Code** (exige plano pago da Anthropic ou chave de API).
- **Git** e **Python 3** (o Python é só para o validador de CSV e o gerador de pacotes).
- **Anki** no computador; no celular também, se quiser revisar fora de casa (com sincronização AnkiWeb).

### Passo 1 — Tenha o seu próprio repositório

No GitHub, use **Use this template** (ou faça um fork, ou clone). O repositório vai acumular o seu
material — perfil, diário, gravações —, então você provavelmente quer ele **privado**.

```bash
git clone https://github.com/<seu-usuario>/<seu-repo>.git
cd <seu-repo>
```

### Passo 2 — Rode a entrevista

Abra a pasta no Claude Code e rode:

```
/comecar
```

É a mesma entrevista da Rota 1. No fim ela preenche `assistente/perfil.md`, cria as pastas de conteúdo,
o painel `index.html` e o placar `progresso/tracker.html`.

### Passo 3 — Importe o pacote da língua

Igual ao [Passo 5 da Rota 1](#passo-5--importe-o-pacote-da-sua-língua), pelo Anki do computador:
**Arquivo → Importar** → `anki/pacotes/<Lingua>.apkg`. Configure o deck como no Passo 6.

### Os comandos

| Comando | O que faz | Onde salva |
|---|---|---|
| `/comecar` | entrevista inicial; configura tudo | `assistente/perfil.md`, pastas, painel, placar |
| `/curriculo` | plano em blocos; detalha o próximo bloco e gera os lotes | `curriculo/` (página) + `cartoes/<bloco>-lNN.csv` |
| `/vocab` | lista de vocabulário por classe (`/vocab 50 verbos`) | página + `cartoes/` |
| `/gramatica` | explica um ponto gramatical com exercícios | `gramatica/` + `cartoes/` |
| `/tema` | vocabulário de um domínio que o livro-texto ignora | `temas/` + `cartoes/` |
| `/leitura` | destrincha um texto autêntico, com glosa | `leituras/` + `cartoes/` |
| `/historia` | história graduada no seu nível | `historias/` + `cartoes/` |
| `/musica` | letra de música linha a linha | `musicas/` + `cartoes/` |
| `/revisao` | conduz a sessão do dia (trilha B) e registra | `diario/AAAA-MM-DD-N.html` + placar |
| `/avaliacao` | simulação em roleplay; veredito | `progresso/avaliacoes/` |

As páginas são HTML e abrem direto no navegador, sem internet. Os CSVs seguem exatamente o mesmo formato
da Rota 1.

### Validar antes de importar

```bash
python ferramentas/validar_csv.py
```

Confere os CSVs de `cartoes/`: cabeçalhos do Anki, número de colunas, chaves repetidas entre arquivos,
situação vazia, tags de bloco e lote, tamanho do lote. Erro de CSV descoberto no Anki custa mais caro que
erro descoberto aqui.

### Importar e sincronizar

No Anki do computador, **Arquivo → Importar** → o CSV do lote. Para revisar no celular, crie uma conta no
**AnkiWeb** e sincronize nos dois aparelhos: importe sempre no computador e deixe a sincronização levar
para o celular. A trilha A acontece no celular; a trilha B, no computador com o Claude Code.

### O que fica fora do git

`audio/` — as suas gravações semanais (`AAAA-MM-DD-NN.m4a`). Ficam na pasta, ao lado do material, para
você ouvir a primeira e a de um mês depois lado a lado, mas não vão para o repositório.

---

## Um dia típico

- **No ônibus, de manhã (trilha A, 8 minutos):** Anki no celular, fila zerada. Fim.
- **À noite, com energia (trilha B, 45 minutos):** "sessão de hoje". O assistente confere se algum lote
  fechou, sugere puxar o próximo, você importa, ouve o áudio e repete por cima em três velocidades, escreve
  o que diria em cada cena e ele corrige linha a linha. Se algum cartão virou *leech*, ele traz a lista e
  você decide o que fazer. Fecha com o registro.
- **Num dia ruim:** só a trilha A. É o suficiente para não perder nada.

## Uma semana típica

- Trilha A: 7 vezes.
- Trilha B: 2 a 4 vezes, quando a energia aparecer — sem dia marcado.
- **Uma gravação de 1 minuto**, você dizendo o lote em andamento. Não é para corrigir; é para comparar
  daqui a um mês.
- Um lote fechado, mais ou menos. Um bloco fecha a cada poucas semanas, com "me testa".

## Ajustar o método

O método tem números, e eles são pontos de partida, não lei. Tudo se ajusta no perfil — peça ao assistente
("muda o tamanho do lote para 10") ou edite `assistente/perfil.md`.

| O quê | Padrão | Quando mexer |
|---|---|---|
| Tamanho do lote | 15 itens (~30 cartões) | revisão diária passando de 30 minutos → diminua |
| Lotes em andamento (WIP) | 2 | fila estável e sobrando energia → 3; fila crescendo → 1 |
| Portão do Anki | intervalo ≥ 7 dias em ≥ 90% | sem prazo apertado → 21 dias é mais honesto sobre retenção |
| Voz dos cartões | código TTS do pacote (`es_ES`, `en_US`…) | outra variante → troque o código ([anki.md](anki.md#trocar-a-voz)) |
| Cartão de Leitura | só nas línguas de escrita não latina | não precisa ler → suspenda com a busca `card:Leitura` |

Algo deu errado? Veja o [FAQ](faq.md).
