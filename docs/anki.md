# Anki: configuração e importação

O Anki é onde a memória acontece. Este guia cobre tudo o que você faz nele: instalar, criar o molde dos
cartões, importar lotes, buscar, trocar a voz e pôr áudio nativo. Configura-se **uma vez**; depois, o dia
a dia é só importar CSV e revisar.

## Instalar

| Aparelho | App | Custo |
|---|---|---|
| iPhone / iPad | **AnkiMobile** (App Store) | pago, compra única |
| Android | **AnkiDroid** (Play Store) | grátis |
| Windows, Mac, Linux | **Anki** em [apps.ankiweb.net](https://apps.ankiweb.net) | grátis |

Use a versão atual. Duas funções deste método têm versão mínima:

- **Voz automática nos cartões** (`{{tts}}`): Anki 2.1.20+, AnkiMobile 2.0.56+, AnkiDroid 2.17+.
- **Cabeçalhos de CSV** que deixam a importação automática: Anki 2.1.54+ (e as versões de celular atuais).

No **Linux**, o Anki de computador não traz voz embutida — a voz automática não toca lá (no celular toca).

## Importar o pacote da sua língua

Em [`anki/pacotes/`](../anki/pacotes/) há um `.apkg` por língua:

| Pacote | Voz (código TTS) | Cartão de Leitura |
|---|---|---|
| `Ingles.apkg` | `en_US` | — |
| `Espanhol.apkg` | `es_ES` | — |
| `Espanhol-America.apkg` | `es_MX` | — |
| `Frances.apkg` | `fr_FR` | — |
| `Alemao.apkg` | `de_DE` | — |
| `Italiano.apkg` | `it_IT` | — |
| `Japones.apkg` | `ja_JP` | sim |
| `Mandarim.apkg` | `zh_CN` | sim |
| `Coreano.apkg` | `ko_KR` | sim |
| `Russo.apkg` | `ru_RU` | sim |

Abra o arquivo com o Anki ("Compartilhar → Anki" no iPhone, "Abrir com AnkiDroid" no Android, dois cliques
no computador). Ele cria:

- o **tipo de nota** `<Lingua>-IA` — por exemplo `Espanhol-IA` —, que é o molde dos cartões;
- o **deck** `<Lingua>` — por exemplo `Espanhol`.

O pacote traz uma nota de exemplo. Pode estudá-la ou apagá-la; apagar a nota não apaga o molde.

**Importe o pacote antes do primeiro CSV.** O CSV procura o molde pelo nome; sem ele, o Anki não sabe
onde pôr as colunas.

## Opções do deck

No deck da língua → engrenagem → **Opções** (*Options*):

| Opção | Valor | Por quê |
|---|---|---|
| **Novos cartões por dia** (*New cards/day*) | **30** | o freio de verdade é o lote, não este número; 30 deixa um lote inteiro entrar no dia em que você o importou |
| **Máximo de revisões por dia** (*Maximum reviews/day*) | **9999** | revisão nunca fica para amanhã — fila adiada é fila que cresce |
| **Ordem de novos e revisões** (*New/review order*) | **mostrar depois das revisões** | a fila vem antes do material novo, sempre |
| **Limite de sanguessuga** (*Leech threshold*) | **4** | o padrão (8) demora demais para avisar que um item resiste |
| **Ação de sanguessuga** (*Leech action*) | **só etiquetar** (*Tag only*) | o cartão continua aparecendo; a tag `leech` é o que o assistente usa para trazer a lista |

**Um deck por língua, sem subdecks.** O limite de cartões novos por dia é por deck; com subdecks por
assunto, o número deixa de significar qualquer coisa. Assunto se separa por **tag** (`bloco::`, `tema::`).

## O molde: 8 campos e 3 cartões

Se você importou o pacote, isto já está pronto — leia só para entender. Se a sua língua não tem pacote e
você não quer usar o gerador, monte à mão: **Ferramentas → Gerenciar tipos de nota → Adicionar → Básico**,
renomeie para `<Lingua>-IA`, e configure os campos e os cartões abaixo.

### Campos, nesta ordem

| # | Campo | No CSV? | O que é |
|---|---|---|---|
| 1 | `chave` | sim | chave de deduplicação. Igual a `alvo`, ou `alvo#sufixo` quando o mesmo texto precisa ser outra nota. Nunca aparece no cartão |
| 2 | `alvo` | sim | o item na língua-alvo, com a moldura que ele exige (`la mesa`, `enamorarse de`) |
| 3 | `pronuncia` | sim | transliteração ou pista de pronúncia; pode ficar vazio |
| 4 | `traducao` | sim | o sentido em português — só no verso |
| 5 | `situacao` | sim | a frente do cartão de Produção: a cena com resposta única |
| 6 | `nota` | sim | gênero, plural, regência, registro, um exemplo curto |
| 7 | `audio` | **não** | áudio nativo, colado por você |
| 8 | `mnemonico` | **não** | escrito por você, só nos itens que resistem |

Os dois últimos ficam **sem coluna no CSV de propósito**: o que é seu não pode ser sobrescrito por um
arquivo gerado. A ordem importa — o Anki usa o **primeiro campo** para decidir se uma linha é nota nova ou
atualização.

### Cartão 1 — Produção

Frente:

```html
<div class="tipo">Produção</div>
<div class="situacao">{{situacao}}</div>
<div class="dica">o que você diz?</div>
```

O único campo da frente é `situacao`. Texto fixo não conta para o Anki: com a situação vazia, a frente
fica sem campo nenhum e o cartão de Produção **não é criado** — que é o caso dos itens de reconhecimento
puro, como uma placa (tag `reconhecimento`).

Verso:

```html
{{FrontSide}}
<hr id=answer>
<div class="alvo">{{alvo}}</div>
{{#pronuncia}}<div class="pron">{{pronuncia}}</div>{{/pronuncia}}
<div class="trad">{{traducao}}</div>
{{#audio}}{{audio}}{{/audio}}{{^audio}}{{tts es_ES:alvo}}{{/audio}}
{{#nota}}<div class="nota">{{nota}}</div>{{/nota}}
{{#mnemonico}}<div class="mnem">{{mnemonico}}</div>{{/mnemonico}}
```

### Cartão 2 — Escuta

Frente:

```html
<div class="tipo">Escuta</div>
{{#audio}}{{audio}}{{/audio}}{{^audio}}{{tts es_ES:alvo}}{{/audio}}
<div class="dica">o que você ouviu?</div>
```

Verso:

```html
{{FrontSide}}
<hr id=answer>
<div class="alvo">{{alvo}}</div>
{{#pronuncia}}<div class="pron">{{pronuncia}}</div>{{/pronuncia}}
<div class="trad">{{traducao}}</div>
{{#nota}}<div class="nota">{{nota}}</div>{{/nota}}
```

Se o campo `audio` tem áudio nativo, o cartão usa ele; se está vazio, usa a voz do aparelho.

### Cartão 3 — Leitura (só nas línguas de escrita não latina)

Frente:

```html
<div class="tipo">Leitura</div>
<div class="alvo grande">{{alvo}}</div>
```

Verso:

```html
{{FrontSide}}
<hr id=answer>
{{#pronuncia}}<div class="pron">{{pronuncia}}</div>{{/pronuncia}}
<div class="trad">{{traducao}}</div>
{{#audio}}{{audio}}{{/audio}}{{^audio}}{{tts es_ES:alvo}}{{/audio}}
```

Troque `es_ES` pelo código da sua língua em **todos** os lugares em que ele aparece.

### Estilo (o mesmo para os três cartões)

```css
.card {
  font-family: -apple-system, "Segoe UI", Roboto, "Noto Sans", "Noto Sans CJK JP", sans-serif;
  font-size: 22px; line-height: 1.45; text-align: center;
  color: #1f2328; background: #ffffff; padding: 12px;
}
.card.nightMode, .nightMode .card { color: #e6edf3; background: #0d1117; }
.tipo { font-size: 12px; letter-spacing: .08em; text-transform: uppercase; opacity: .55; }
.situacao { font-size: 22px; margin: 18px 0 6px; }
.dica { font-size: 14px; opacity: .55; margin-top: 10px; }
.alvo { font-size: 32px; font-weight: 600; margin: 14px 0 4px; }
.alvo.grande { font-size: 44px; margin-top: 28px; }
.pron { font-size: 18px; opacity: .8; }
.trad { font-size: 18px; margin-top: 8px; }
.nota { font-size: 15px; opacity: .75; margin-top: 14px; }
.mnem { font-size: 15px; margin-top: 14px; padding: 8px; border-radius: 6px;
        background: rgba(255, 196, 0, .15); }
```

## Importar um lote

Cada lote é um arquivo CSV que começa assim:

```
#separator:comma
#html:false
#notetype:Espanhol-IA
#deck:Espanhol
#columns:chave,alvo,pronuncia,traducao,situacao,nota,tags
#tags column:7
gracias,gracias,,obrigado(a),alguém segura a porta para você passar,neutro; serve em qualquer registro,bloco::cortesia lote::cortesia::01 tipo::frase
```

As linhas com `#` são **cabeçalhos do Anki**: dizem o separador, o tipo de nota, o deck, o nome das
colunas e qual coluna tem as tags. Com elas, a tela de importação já vem preenchida — inclusive no celular,
onde mapear coluna à mão é um sofrimento. Não há linha de títulos comum: os nomes estão no `#columns:`.

- **Celular:** toque no arquivo → "Compartilhar → Anki" (iPhone) ou "Abrir com AnkiDroid" (Android).
- **Computador:** **Arquivo → Importar** → escolha o CSV.

Na tela de importação, confira só uma coisa: **notas existentes devem ser atualizadas**. É o padrão do
Anki: quando o primeiro campo (`chave`) de uma linha coincide com o de uma nota do mesmo tipo, a nota é
atualizada no lugar e **o histórico de revisão é preservado**. É isso que permite ao assistente corrigir
uma linha e você reimportar sem perder nada.

**Importar é puxar.** Importe um lote quando for começá-lo — o lote que não foi importado é o seu backlog.

### Reimportar é seguro — testado

Testado com o motor oficial do Anki (biblioteca `anki` 26.09.4, a mesma do AnkiMobile e do AnkiDroid),
pelo script [`ferramentas/testar_anki.py`](../ferramentas/testar_anki.py):

- **CSV corrigido:** reimportar atualiza a nota no lugar, preserva o histórico de revisão e **não toca
  nos campos sem coluna** — o seu `audio` e o seu `mnemonico` ficam intactos.
- **Pacote novo:** importar uma versão nova do `.apkg` da sua língua (por exemplo, com outra voz)
  atualiza o molde no lugar, sem criar um tipo de nota duplicado.

### Quando a chave muda

A `chave` é igual ao texto do `alvo`. Se o assistente **corrigir o próprio `alvo`** (um erro de grafia,
por exemplo), a chave muda junto, e a reimportação cria uma nota nova em vez de atualizar a velha. Apague a
nota antiga à mão. É raro, e é o preço de uma chave que o assistente consegue calcular sem lembrar dos
lotes anteriores.

## Buscas úteis

No navegador de cartões (*Browse*), no computador ou no celular:

| Para quê | Busca |
|---|---|
| Os cartões de um lote | `tag:lote::cortesia::01` |
| Primeiro portão do lote: quantos já maduraram | `tag:lote::cortesia::01 card:Produção prop:ivl>=7` |
| …contra o total do lote | `tag:lote::cortesia::01 card:Produção` |
| Itens que resistem (gatilho do mnemônico) | `tag:leech` |
| Itens que o assistente marcou como incertos | `tag:verificar` |
| Tudo de um bloco | `tag:bloco::cortesia` |
| Itens ainda na voz do aparelho, num bloco | `tag:bloco::cortesia -tag:audio::nativo` |
| Desligar os cartões de Leitura | `card:Leitura` → selecionar tudo → suspender |

O lote passa no primeiro portão quando a primeira contagem é pelo menos 90% da segunda. O segundo portão é
você dizer o lote inteiro em voz alta, sem ler — ver [O método](metodo.md#o-critério-de-pronto-dois-portões).

## Trocar a voz

A voz vem do sistema do aparelho. Para mudar a variante, a velocidade ou a voz:

1. **Ferramentas → Gerenciar tipos de nota** → `<Lingua>-IA` → **Cartões**.
2. Em cada template onde aparece `{{tts es_ES:alvo}}`, troque o código: `es_MX` (México), `en_GB`
   (Reino Unido), `pt_PT`…
3. Opcional: velocidade — `{{tts es_ES speed=0.8:alvo}}` — ou uma voz específica —
   `{{tts ja_JP voices=Apple_Otoya:alvo}}`.

Para melhorar a qualidade sem mexer no Anki, baixe vozes melhores no sistema: no iPhone, em Ajustes →
Acessibilidade → Conteúdo Falado → Vozes, as versões "aprimoradas"; no Android, os dados de voz do
mecanismo de conversão de texto em voz, nas configurações de acessibilidade.

## Áudio nativo

A voz do aparelho serve para a maior parte do vocabulário. Para o que você vai **dizer em voz alta muitas
vezes** — cortesia, apresentação, as frases do seu objetivo —, vale um falante de verdade, sobretudo em
língua tonal.

1. Consiga o áudio: um falante nativo que você conheça gravando no celular (o melhor), ou um banco de
   pronúncias como o Forvo (⚠️ verifique a licença de reuso antes de baixar em quantidade).
2. No computador, abra a nota no editor e **anexe o arquivo** no campo `audio` (ícone de clipe). O campo
   fica com algo como `[sound:gracias.mp3]`.
3. Acrescente a tag `audio::nativo` à nota — é como você sabe, depois, o que ainda está na voz sintetizada.

O áudio vai para a mídia do Anki e sincroniza junto. Não entra no CSV nem no repositório.

## Criar um pacote para outra língua

Com Python 3 instalado:

```bash
pip install genanki
python ferramentas/gerar_pacotes.py --lingua Holandes --tts nl_NL --obrigado "dank je"
python ferramentas/gerar_pacotes.py --lingua Grego --tts el_GR --leitura --obrigado "ευχαριστώ" --pronuncia "efcharistó"
```

O pacote sai em `anki/pacotes/<Lingua>.apkg`, com tipo de nota `<Lingua>-IA` e deck `<Lingua>`. Use nome
**sem acento e sem espaço** — ele vai aparecer no cabeçalho `#notetype:` de todo CSV. Avise o assistente do
nome, para que os CSVs saiam com o cabeçalho certo (a entrevista já pergunta).

Sem Python, monte o molde à mão (seção [O molde](#o-molde-8-campos-e-3-cartões)) com exatamente esses nomes.

## Celular e computador juntos: AnkiWeb

Se você vai usar mais de um aparelho, crie uma conta grátis em [ankiweb.net](https://ankiweb.net) e
sincronize em todos. Duas regras evitam conflito:

- **Importe num aparelho só** (o que for mais cômodo) e deixe a sincronização levar para os outros.
- **Sincronize antes e depois** de cada sessão — o Anki pode pedir para escolher entre "enviar" e
  "baixar" quando os dois lados mudaram, e escolher errado apaga as revisões de um deles.
