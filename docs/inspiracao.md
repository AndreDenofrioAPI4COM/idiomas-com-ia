# De onde isto veio

## A história curta

Este método começou como um projeto pessoal: aprender mandarim **do zero absoluto em 12 semanas**, para
uma missão de negócios de uma semana à China. Prazo fixo, língua tonal, escrita não latina, ponto de
partida zero e nenhum professor — praticamente o caso mais difícil que um método de estudo com IA pode
enfrentar.

O ponto de partida foi um PDF gratuito com sete prompts para aprender línguas com IA. Os prompts funcionavam
como ideia, mas quebravam no contato com o caso real: pediam paradigmas de conjugação para uma língua que
não conjuga, um plano de um ano para quem tinha doze semanas, e as 500 palavras mais frequentes para quem
precisava de um brinde num jantar. Cada quebra virou uma regra. Depois vieram mais fontes — vídeos do
mesmo autor e um livro inteiro de outro —, e cada uma também virou regra, ou derrubou uma.

O que está neste repositório é a parte que sobreviveu: as regras que não dependiam do mandarim, da viagem
ou de quem estava estudando. Em seguida o método foi adaptado para quem só tem celular, o que deu origem à
[Rota 1](como-usar.md#rota-1--chat-padrão).

Vale dizer o que **não** se afirma aqui: não há estudo controlado mostrando que este método funciona
melhor que outro. Ele é uma síntese de fontes, com cada adaptação justificada. As fontes estão abaixo, com
o que se adotou, o que se mudou e por quê — para você julgar.

---

## Fonte 1 — *The Ultimate LLM Prompt Library for Language Learners*

**Dr. Taylor Jones**, do canal **Language Jones**. Linguista, com um canal sobre aprendizado de línguas.
O PDF é um recurso **gratuito** no site do autor, [languagejones.com](http://www.languagejones.com), com
sete prompts prontos para colar em qualquer assistente (ChatGPT, Claude, Gemini) e uma promessa: o uso
diário e consistente pode levar de zero a conversacional em cerca de um ano, na maioria das línguas.

A tese dele é a tese deste repositório: **o modelo de linguagem substitui o livro-texto**. Ele gera o
currículo, o vocabulário, a gramática e as leituras sob demanda — e o Anki faz a revisão.

### Os sete prompts, e o que aconteceu com cada um

| Prompt do PDF | Aqui | O que mudou, e por quê |
|---|---|---|
| **01 · The Complete Textbook Replacement** — plano de um ano mapeado aos níveis europeus (CEFR), tópicos por semana, as 500 palavras mais frequentes | "monta meu plano" · `/curriculo` | Plano em **blocos ligados às situações do seu objetivo**, sem semanas, e com a frequência do **seu** objetivo, não a geral. O nível CEFR vira referência, não meta. O prazo é o seu, não um ano |
| **02 · The Vocab Builder** — CSV com as 100 palavras mais comuns de uma classe gramatical | "50 verbos" · `/vocab` | Mantido. Cada linha ganha uma **situação** na frente, a **moldura** do item (gênero, regência, classificador), deduplicação e lotes de até 15 |
| **03 · The Grammar Explainer** — classes de conjugação, paradigma completo de três verbos; comparativos e superlativos | "explica X" · `/gramatica` | É o que mais precisou de adaptação: **pressupõe uma língua que flexiona**. Em mandarim não há paradigma para mostrar. Regra geral: se a língua flexiona, paradigma; se não, a **construção** (ordem, partículas, aspecto, classificadores) ocupa o lugar dele. Exemplos só com o que já foi ensinado, contraste com o português, exercícios que viram cartões |
| **04 · The Textbook Supplement** — vocabulário de qualquer domínio, inclusive os que o livro ignora (creche, astronomia, café artesanal) | "vocabulário de farmácia" · `/tema` | **Adotado inteiro.** O domínio vem do seu objetivo. Acrescentou-se frases funcionais, um diálogo curto e nota cultural |
| **05 · Assisted Reading with Leipzig Glosses** — tradução, 15–20 palavras difíceis, glosa linha a linha | (cole o texto) · `/leitura` | Mantido. A glosa se concentra nas frases estruturalmente interessantes, e o vocabulário vira CSV |
| **06 · Short Story Generator** — história no nível exato, 90% de vocabulário do nível, 5–10 *challenge words*, glossário e perguntas | "uma história sobre X" · `/historia` | Mantido. O nível é calibrado pelo que **já está no seu baralho**, não por um rótulo. As palavras-desafio aparecem pelo menos duas vezes; a tradução fica escondida até você responder |
| **07 · Learning with Songs** — letra traduzida e transliterada linha a linha, vocabulário anotado | (cole a letra) · `/musica` | Mantido, com uma regra: **nunca reconstruir a letra de memória** — o assistente pede a letra. Letra errada ensina errado |

E as dicas do PDF:

| Dica | O que aconteceu |
|---|---|
| Gerar CSV para importar no Anki | Virou a espinha dorsal, mais ambiciosa que no original: **tudo** vira cartão — frase, diálogo, padrão, exercício —, não só vocabulário |
| Ouvir o texto com uma voz sintetizada | Virou o cartão de **Escuta**, com a voz do próprio aparelho, e o áudio nativo como melhoria onde importa |
| Escolher domínios fora do livro-texto | Virou o `/tema`, e a ideia de que a régua é o seu objetivo |
| Fotografar a página de um livro para extrair o texto | Mantida como dica no `/leitura` |

Três coisas que se acrescentaram aos prompts e não estão no PDF: a **entrevista inicial** que configura
tudo, a **sessão do dia** e a **simulação** de fechamento de bloco.

## Fonte 2 — os vídeos do canal Language Jones

O mesmo autor explica, em vídeos no YouTube, o porquê por trás dos prompts — e desce ao como. Deles vieram:

- **A ordem de aquisição:** sons primeiro, depois gramática, frequência e temas.
- **O livro-texto que não existe:** pedir ao modelo o livro inteiro e o baralho inteiro, e depois pedir que
  ele infira o que falta a partir do baralho acumulado.
- **O tamanho do cartão:** *chunk*, não frase inteira. O autor conta que os próprios cartões dele tinham o
  tamanho de uma frase porque era o jeito mais fácil de cortar o áudio — uma decisão de ferramenta que
  virou decisão de método sem ninguém perceber.
- **A conta escondida:** cada cartão novo compra uma cauda de revisões futuras. Meta de cartões novos por
  dia sem essa conta é fila explodindo três dias depois.
- **Shadowing em três velocidades** (0,75× / 1,00× / 1,25×), com gravação, e o teste **"mudo e entrega"**:
  cortar o áudio e entregar a cena de memória, no ritmo.
- **Exagerar a caricatura** da pronúncia até soar constrangedor — o desconforto é o indicador.
- **Intercalar:** a repetição espaçada funciona ainda melhor com conteúdo misturado.

Um dos vídeos é patrocinado por uma plataforma de séries para aprender línguas. A técnica foi separada do
produto: o que entrou aqui não depende de assinar nada.

E um cuidado de leitura que moldou este repositório: **o PDF e os vídeos são da mesma pessoa.** Ouvir a
mesma ideia cinco vezes não é cinco confirmações — é uma. Por isso a fonte seguinte pesa tanto.

## Fonte 3 — *Fluent Forever*, de Gabriel Wyner

Livro de **Gabriel Wyner** (1ª edição em 2014; 2ª edição revista em 2024). Wyner é cantor de ópera de
formação — precisou cantar em várias línguas com pronúncia impecável —, não linguista, e escreveu sem
conhecer o trabalho do Language Jones. É a **voz independente** do método. Site do autor:
[fluent-forever.com](https://fluent-forever.com).

O que veio dele:

- **Sons primeiro.** Pronúncia aprendida errada gruda.
- **Não traduzir.** A palavra da língua-alvo deve ser ligada a uma imagem ou experiência, não a uma palavra
  da sua língua — porque os "equivalentes" do dicionário raramente são equivalentes. Aqui isso virou a
  **situação** na frente do cartão.
- **Repetição espaçada** e **um cartão, um fato.**
- **Fazer os próprios cartões** — ninguém pode dar uma língua a você; você tem que tomá-la para si.
- **Teste de pares mínimos com feedback imediato.** Estudos com adultos japoneses treinando *r* × *l* em
  inglês: sem feedback, a prática não melhorava nada; com feedback a cada resposta, três sessões de vinte
  minutos "religaram" o ouvido. Aqui virou o cartão de **Escuta** e a regra **ouvido antes da boca**.
- **Mnemônico só reativo** — o passo 1 da técnica, na 2ª edição, é não escolher nada de antemão; usar só
  quando você errar cartões por causa do conceito difícil.
- **Interferência.** Palavras semanticamente próximas, estudadas juntas, levaram **11,3 repetições contra
  7,2** das não relacionadas. Aqui virou **página temática ≠ lote**.
- **A exceção que legitima frases prontas:** dá para memorizar e usar frases inteiras com gramática
  avançada desde cedo, como blocos — com o aviso de que isso não significa produzi-las corretamente em
  qualquer outro contexto.

E uma lacuna, que vale registrar: **na nossa leitura da 2ª edição, o livro não trata de tom.** Para
línguas tonais, "sons primeiro" tem duas fontes atrás; *como ensinar tom a um adulto* tem bem menos.

---

## Onde as fontes concordam

Onde duas fontes que não se conhecem chegam sozinhas ao mesmo lugar, a regra sai da mesa de discussão:

- Sons antes de vocabulário.
- Repetição espaçada, com o esforço de lembrar como mecanismo, não como efeito colateral.
- Produzir acima de reconhecer.
- Um cartão, um fato.
- Frase de exemplo só com o que já foi ensinado.
- Prática diária acima de esforço esporádico.
- Fazer os próprios cartões (ou, aqui, gerá-los sob medida).
- Intercalar acima de agrupar — Wyner mede o custo de agrupar, Jones descreve o ganho de intercalar. O
  mesmo mecanismo pelas duas pontas.

## Onde elas discordam, e como se resolveu

| Conflito | Resolução |
|---|---|
| Wyner: **nunca ponha a tradução no cartão** × este método exige cartão de produção (você vê algo e tem que dizer na língua-alvo) | Os dois estão certos sobre coisas diferentes. O problema dele é a tradução fingir equivalência. Então a frente do cartão vira **a situação**, não a palavra — e a tradução vai para o verso, como desempate |
| Jones usa tradução automática e **corrige à mão os ~5% errados** | Quem está começando não detecta os 5%. Daí a regra de **marcar `⚠️ verificar`** em vez de inventar, e a conferência com falante nativo. (Ele tem razão num ponto incômodo: aquela correção manual também era aprendizado.) |
| Wyner **defende frases geradas por IA**, porque o mecanismo dele pega o erro depois — o cartão que não gruda é levado a um tutor | O mecanismo pressupõe um tutor no fim da linha. Sem ele, o erro fica. O que se adota: pedir ao assistente que confira a própria frase e marque a dúvida |
| Jones **separa o baralho por assunto** | **Um deck por língua.** O limite diário de cartões novos do Anki é por deck; com subdecks ele deixa de significar qualquer coisa. Assunto se separa por **tag** |
| Todas as fontes mandam **assistir séries e vídeos em volume** | Depende do objetivo e do prazo. Com prazo curto e meta oral, cada hora de série é uma hora fora do que você precisa dizer. Sem prazo, volta a valer |
| A capa do PDF: **"funciona para qualquer língua"** | Verdade como promessa de **formato**, falsa como promessa de **conteúdo**. O Prompt 03 quebra em língua sem flexão. Por isso existe a entrevista: ela escreve as convenções da **sua** língua no perfil |

## O que este repositório acrescenta

Nenhuma das fontes tem isto; são as peças que tornaram as ideias executáveis no dia a dia:

- **A frente do cartão é uma cena com resposta única** — e, como teste, se a cena não puder ser escrita,
  o item está mal recortado.
- **Página temática ≠ lote de importação** — tema para consultar, lote embaralhado para memorizar.
- **Kanban por importação** — bloco, lote, puxar = importar; sem semanas.
- **Duas trilhas** — a fila diária minúscula separada do material novo em bloco, com a regra do dia ruim.
- **Pronto com dois portões** — durabilidade no Anki e entrega em voz alta.
- **WIP que mostra o custo** em vez de bloquear.
- **Uma chave de deduplicação** no CSV, para que reimportar atualize em vez de duplicar.
- **Campos que o assistente nunca toca** — o áudio nativo e o mnemônico são seus.
- **`⚠️ verificar`** — incerteza marcada em vez de frase plausível.
- **O assistente não escreve o seu mnemônico.**
- **Avaliação por simulação**, não por prova, e o veredito em três níveis.
- **"O assistente não ouve você"** — a limitação dita em voz alta, e os instrumentos que a contornam.
- **A entrevista** que configura o método para qualquer língua e qualquer objetivo.
- **A rota de celular** — o método inteiro rodando num Projeto de chat e no Anki do telefone.

---

## Créditos e aviso

Este repositório **não é afiliado** ao Language Jones, a Taylor Jones, ao Fluent Forever ou a Gabriel
Wyner. É uma síntese independente, que cita as ideias deles com atribuição e as adapta.

- O PDF *The Ultimate LLM Prompt Library for Language Learners* é gratuito no site do autor. **Não o
  redistribuímos** e não reproduzimos os prompts na íntegra — baixe da fonte.
- *Fluent Forever* é um livro à venda. Se as ideias dele aparecem aqui e fazem sentido para você,
  **compre o livro**: ele tem muito mais do que coube neste resumo.
- O Anki é software livre. O AnkiMobile, a versão de iPhone, é pago — e ajuda a financiar o
  desenvolvimento das outras.
