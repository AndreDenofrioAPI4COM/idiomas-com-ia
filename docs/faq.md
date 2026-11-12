# Perguntas frequentes

**Começar**
- [Preciso saber programar?](#preciso-saber-programar)
- [Quanto custa?](#quanto-custa)
- [Funciona com ChatGPT, Gemini ou outro assistente?](#funciona-com-chatgpt-gemini-ou-outro-assistente)
- [Funciona para qualquer língua?](#funciona-para-qualquer-língua)
- [Estou começando do zero. E se eu já for intermediário?](#estou-começando-do-zero-e-se-eu-já-for-intermediário)
- [E se eu não tiver prazo?](#e-se-eu-não-tiver-prazo)

**O método**
- [Por que Anki?](#por-que-anki)
- [Por que a frente do cartão é uma cena e não a palavra em português?](#por-que-a-frente-do-cartão-é-uma-cena-e-não-a-palavra-em-português)
- [Por que lote de 15 e no máximo 2 lotes em andamento?](#por-que-lote-de-15-e-no-máximo-2-lotes-em-andamento)
- [Quanto tempo por dia?](#quanto-tempo-por-dia)
- [Perdi dias e a fila explodiu. E agora?](#perdi-dias-e-a-fila-explodiu-e-agora)
- [Por que o assistente não escreve meus mnemônicos?](#por-que-o-assistente-não-escreve-meus-mnemônicos)

**Confiança e limites**
- [A IA erra. Como eu confio no conteúdo?](#a-ia-erra-como-eu-confio-no-conteúdo)
- [A IA corrige minha pronúncia?](#a-ia-corrige-minha-pronúncia)
- [Posso usar com um professor?](#posso-usar-com-um-professor)

**Prática**
- [Posso estudar só no celular?](#posso-estudar-só-no-celular)
- [O arquivo não baixa, ou o Anki não importa](#o-arquivo-não-baixa-ou-o-anki-não-importa)
- [As vozes dos cartões são ruins](#as-vozes-dos-cartões-são-ruins)
- [Posso compartilhar meu baralho?](#posso-compartilhar-meu-baralho)
- [E a privacidade?](#e-a-privacidade)

**O projeto**
- [Isto é afiliado ao Language Jones ou ao Fluent Forever?](#isto-é-afiliado-ao-language-jones-ou-ao-fluent-forever)
- [Como contribuir?](#como-contribuir)

---

## Começar

### Preciso saber programar?

Não, na [Rota 1](como-usar.md#rota-1--chat-padrão). Você baixa três arquivos, cria um Projeto no
assistente, importa um pacote no Anki e conversa. A [Rota 2](como-usar.md#rota-2--claude-code) usa o
Claude Code e pede familiaridade com terminal e Git.

### Quanto custa?

- **Anki:** grátis no computador e no Android (AnkiDroid). No iPhone, o AnkiMobile é pago (compra única).
  A sincronização pelo AnkiWeb é grátis.
- **Assistente:** os planos grátis do ChatGPT, do Claude e do Gemini servem para começar, com limite de
  mensagens. O plano pago dá folga e entrega de arquivo mais confiável. A Rota 2 exige o Claude Code, que
  é pago.
- **Este repositório:** grátis, licença MIT.

### Funciona com ChatGPT, Gemini ou outro assistente?

A Rota 1 foi escrita para funcionar em qualquer assistente que tenha **instruções fixas** e **arquivos de
referência** num mesmo lugar: Projetos do ChatGPT, Projetos do Claude, Gems do Gemini. O que muda de um
para outro é a entrega do CSV — alguns criam o arquivo para baixar, outros só mostram o texto (ver
[diferenças entre plataformas](como-usar.md#diferenças-práticas-entre-as-plataformas)).

Num assistente sem Projetos, dá para colar o `instrucoes.md` no começo da conversa e anexar o
`metodo.md` e o `perfil.md` — mas você vai repetir isso a cada conversa nova.

A Rota 2 é específica do Claude Code (comandos e skills são do Claude Code).

### Funciona para qualquer língua?

O **formato** funciona para qualquer língua falada e escrita: cartão, CSV, lote, rotina. O **conteúdo**
depende da entrevista, que escreve no seu perfil as convenções da sua língua — escrita, transliteração,
o que vem colado a cada palavra (gênero, classificador, caso), os sons que quem fala português costuma
errar.

Dois casos pedem cuidado:

- **Línguas tonais** (mandarim, cantonês, vietnamita, tailandês…): o tom muda a palavra, e é a parte mais
  difícil de verificar sem um humano. Áudio nativo e a gravação semanal pesam muito mais.
- **Escrita não latina** (japonês, mandarim, coreano, russo, árabe…): ler vira uma habilidade separada.
  Os pacotes dessas línguas trazem o cartão de Leitura.

Línguas de sinais não cabem neste formato — o método é feito de texto e áudio.

Há pacotes de Anki prontos para inglês, espanhol (Espanha e América), francês, alemão, italiano,
japonês, mandarim, coreano e russo. Para outra língua, ver
[Criar um pacote para outra língua](anki.md#criar-um-pacote-para-outra-língua).

### Estou começando do zero. E se eu já for intermediário?

Os dois casos funcionam; o que muda é o plano que sai da entrevista.

- **Do zero:** o primeiro bloco é de sons e de fórmulas fixas — cumprimentar, agradecer, se apresentar.
  São coisas que você usa no primeiro dia e que não dependem de gramática.
- **Intermediário:** a entrevista pergunta o que você já sabe e onde trava. O plano pula o que você tem
  e vai para os domínios do seu objetivo, para o que você entende mas não consegue dizer, e para leitura
  e escuta de material autêntico (`/leitura`, `/musica`, ou colando o texto na conversa).

Em qualquer nível, o cartão de Produção continua obrigatório: intermediário costuma reconhecer muito mais
do que consegue dizer, e é exatamente essa distância que o método ataca.

### E se eu não tiver prazo?

Funciona igual, com duas mudanças: o critério de pronto pode subir para intervalo de **21 dias** (mais
honesto sobre retenção, e sem pressa ele cabe), e não há burn-down nem data de parar de puxar. O plano
deixa de ser "até a data" e vira fases: a primeira cobre a situação mais próxima, e a seguinte começa
quando ela fechar.

---

## O método

### Por que Anki?

Porque ele resolve a única coisa que o assistente não resolve: **lembrar no dia certo.** O assistente gera
material infinito; sem repetição espaçada, quase tudo é esquecido em dias. O Anki é grátis (fora o iPhone),
funciona offline, importa CSV, roda no celular e não some se uma empresa mudar de ideia. Outros apps de
cartões existem, mas poucos importam CSV com os cabeçalhos que deixam a importação automática.

### Por que a frente do cartão é uma cena e não a palavra em português?

Porque na vida real o gatilho de "gracias" não é a palavra "obrigado" — é alguém segurando a porta para
você. Cartão que mostra a palavra em português treina **traduzir**; cartão que mostra a cena treina
**reagir**, que é o que a conversa pede. A tradução continua no verso.

E a cena é um teste de qualidade: ela tem que ter **uma resposta única**. Se não dá para escrever uma cena
assim, o item está mal recortado. Detalhes em [O método → A frente é uma situação](metodo.md#a-frente-é-uma-situação-nunca-uma-tradução).

### Por que lote de 15 e no máximo 2 lotes em andamento?

Porque cada cartão novo compra uma cauda de revisões futuras — algo como 8 a 12 (estimativa; confira no
seu Anki). Um lote de 15 itens gera uns 30 cartões. Dois lotes em andamento mantêm a revisão diária em
algo como 10 a 20 minutos, que cabe num dia ruim. Três levam para 25 a 30.

O número de 2 é **recomendação, não trava**. Você pode puxar mais; o assistente vai dizer quanto a fila
diária vai crescer, e quando. Os dois números se ajustam no perfil ([Ajustar o método](como-usar.md#ajustar-o-método)).

### Quanto tempo por dia?

Não há meta de tempo. Há duas coisas:

- **Todo dia:** zerar a fila do Anki. Pode levar 3 minutos ou 20 — é o que a fila pedir.
- **Quando houver energia:** uma sessão com o assistente, de 20 minutos a 2 horas, em que material novo
  entra.

A primeira é a que não pode faltar. A segunda decide a velocidade.

### Perdi dias e a fila explodiu. E agora?

1. **Pare de importar lote novo** até a fila voltar ao normal. Nada novo entra enquanto há dívida.
2. Faça a fila em pedaços ao longo de alguns dias. Não precisa zerar tudo de uma vez.
3. Se ainda assim for demais, **suspenda o lote mais recente** no Anki (busca `tag:lote::<bloco>::<NN>`,
   selecionar tudo, suspender). Ele volta para o backlog sem perder nada e você o retoma depois.
4. Na volta, conte ao assistente ("fiquei duas semanas sem estudar"): ele ajusta o plano em vez de seguir
   como se nada tivesse acontecido.

O que não fazer: apagar o deck e recomeçar. A fila assusta, mas boa parte dela sai rápido.

### Por que o assistente não escreve meus mnemônicos?

Porque mnemônico imposto é mais uma coisa para decorar. A imagem só funciona se significa algo **para
você**, e o ato de montar já é metade da fixação. O assistente faz o momento aparecer — traz a lista dos
cartões que você mais erra, com o campo `mnemonico` vazio — e lembra a estrutura (a mesma imagem para o
mesmo gênero, o mesmo tom). A imagem é sua.

E antes do mnemônico ele vai sugerir desconfiar do cartão: cartão difícil costuma ser cartão mal feito.

---

## Confiança e limites

### A IA erra. Como eu confio no conteúdo?

Ela erra, sim — sobretudo em naturalidade (frase gramatical que nenhum nativo diria), em variante regional
e em língua com menos texto na internet. O método tem quatro defesas:

1. **`⚠️ verificar`.** O assistente é instruído a marcar o que não tem certeza, em vez de inventar. O item
   vai com a tag `verificar`, e você sabe que não deve confiar nele ainda.
2. **Exemplos só com o que você já sabe.** Menos material novo por frase, menos lugar para erro escondido.
3. **Um nativo.** As frases que recrutam corretor ("isso soa natural?") existem para isso. Mostre as linhas
   com `verificar` primeiro.
4. **O seu ouvido.** Quando você começa a consumir material autêntico, frase estranha começa a soar estranha.

Quanto mais iniciante você é, menos você detecta erro — e é por isso que a marcação existe.

### A IA corrige minha pronúncia?

**Não.** O assistente não ouve você. Nem o modo de voz resolve: o reconhecimento de fala é feito para
entender o que você quis dizer, e perdoa muito. **Não confie em elogio de pronúncia vindo de IA.**

O que existe no lugar: o cartão de Escuta (treina o ouvido, que vem antes da boca), a gravação semanal de
1 minuto (mostra deriva ao longo do tempo), o ditado por voz no teclado da língua-alvo (se transcreve
certo, a máquina entendeu) e, acima de tudo, um falante nativo. Detalhes em
[Verificar a produção](metodo.md#verificar-a-produção-o-assistente-não-ouve-você).

### Posso usar com um professor?

Deve. Um professor cobre exatamente o que o método não cobre: ouvir você. Duas formas de combinar:

- Leve as gravações semanais e as linhas marcadas `verificar` para a aula.
- Use a aula para a simulação do fim de bloco, com o professor no lugar do assistente.

E o que o professor corrigir vira cartão: conte ao assistente e peça o CSV.

---

## Prática

### Posso estudar só no celular?

Sim — a Rota 1 foi feita para isso. O Projeto roda no app do ChatGPT, do Claude ou do Gemini; o Anki roda
no celular; o CSV vai do assistente para o Anki pelo "abrir em". A configuração inicial (baixar os
arquivos, criar o Projeto) é mais confortável num computador, mas dá para fazer no telefone.

### O arquivo não baixa, ou o Anki não importa

- **O link de download falhou (ChatGPT):** peça "gera o arquivo de novo". No celular, o app costuma baixar
  melhor que o navegador.
- **O assistente só mostrou o texto:** copie o bloco inteiro, incluindo as linhas que começam com `#`, e
  salve como `.csv` (num editor de texto). Ou peça explicitamente "me entrega como arquivo".
- **O Anki diz que o tipo de nota não existe:** você ainda não importou o pacote `.apkg` da língua, ou o
  nome no cabeçalho `#notetype:` não bate com o do seu Anki. Importe o pacote primeiro.
- **As colunas vieram trocadas ou tudo num campo só:** confira se o arquivo começa com as linhas `#` e se
  o Anki está atualizado (os cabeçalhos exigem Anki 2.1.54+ ou versão equivalente no celular).
- **Acentos viraram símbolos estranhos:** o arquivo não foi salvo em UTF-8. Peça o arquivo de novo.

Mais em [anki.md](anki.md#importar-um-lote).

### As vozes dos cartões são ruins

A voz vem do sistema do aparelho, e a qualidade varia. Três saídas, da mais barata à melhor:

1. Baixe uma voz melhor no sistema (no iPhone, as vozes "aprimoradas"; no Android, os dados de voz do
   mecanismo de conversão de texto em voz).
2. Troque a variante ou a velocidade no cartão — ver [Trocar a voz](anki.md#trocar-a-voz).
3. Para o que você vai dizer muitas vezes, use **áudio nativo** no campo `audio` — ver
   [Áudio nativo](anki.md#áudio-nativo).

### Posso compartilhar meu baralho?

Pode, e o CSV é o melhor jeito: é texto, leve, e quem receber importa no próprio pacote da língua. Mas
lembre que o melhor baralho é o feito para o **seu** objetivo — o de outra pessoa tem as situações dela.
Use como ponto de partida, não como substituto da entrevista.

### E a privacidade?

- **Rota 1:** o que você conta na entrevista fica no Projeto do assistente, sujeito à política de dados
  da plataforma. Não conte nada que você não contaria a esse serviço.
- **Rota 2:** tudo fica no seu repositório. Se ele tiver o seu perfil, diário ou nomes de pessoas, deixe-o
  **privado**. As gravações da sua voz (`audio/`) ficam fora do Git por padrão.
- Os cartões ficam no seu Anki. O AnkiWeb só recebe se você sincronizar.

---

## O projeto

### Isto é afiliado ao Language Jones ou ao Fluent Forever?

Não. É uma síntese independente, com atribuição. O PDF do Language Jones é gratuito no site do autor e o
livro *Fluent Forever* está à venda — veja [De onde isto veio](inspiracao.md#créditos-e-aviso).

### Como contribuir?

Abra uma *issue* ou um *pull request*. O que mais ajuda:

- **Relato de uso real:** que língua, que objetivo, o que travou. Método se melhora com caso concreto.
- **Pacote para uma língua nova**, com o código de voz testado num aparelho de verdade.
- **Correção de convenção de língua** que o assistente erra com frequência.
- **Plataforma:** como a Rota 1 se comporta num assistente que ainda não está descrito aqui.

Regra para mudar o método: toda mudança diz **por quê** — uma fonte, um caso, uma medida. Regra sem porquê
não entra.
