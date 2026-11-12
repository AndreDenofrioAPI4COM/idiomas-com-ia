---
description: Entrevista inicial — configura o perfil, cria as pastas e diz qual pacote do Anki importar
argument-hint: [língua-alvo, opcional — ex. "espanhol da Argentina"]
---

# /comecar — configurar tudo a partir de uma conversa

Argumento: `$ARGUMENTS` — se vier a língua-alvo, ela já é a resposta da primeira pergunta.

Leia `assistente/metodo.md` inteiro antes de começar; a seção 2 é o roteiro desta conversa.

## 0. O perfil já existe?

Abra `assistente/perfil.md`.

- **Ainda é o modelo vazio** (campos `[preencher]`) → siga para a entrevista.
- **Já está preenchido** → não sobrescreva. Pergunte o que mudou e altere só esses campos. Plano,
  progresso e dificuldades recorrentes nunca são apagados por uma reconfiguração.

## 1. A entrevista

Conduza exatamente a seção 2 do `metodo.md`: uma pergunta por vez, na ordem de lá, aceitando
"não sei" como resposta válida (anote como lacuna, não invente). O objetivo vem antes do nível,
porque é ele que decide o que entra.

## 2. O que gravar

1. **`assistente/perfil.md`** preenchido — todas as seções do modelo. Na seção 3 (língua e
   convenções), escreva as convenções específicas da língua-alvo: escrita e transliteração, o que
   vem colado a cada item (gênero, classificador, aspecto, regência…), os sons que a língua do
   aprendiz não tem, os erros típicos de quem fala a língua dele, a escala de nível usada. O que você
   não tiver certeza vai com `⚠️ verificar`.
2. **Plano de blocos** na seção 5 do perfil, derivado das situações do objetivo, na ordem em que
   entram e sem datas — como manda a seção 2 do `metodo.md`.
3. **Pastas de conteúdo**, cada uma com `index.html` feito de `modelos/indice.html`:
   `curriculo/ cartoes/ gramatica/ leituras/ historias/ temas/ musicas/ diario/`.
   Crie também `progresso/avaliacoes/` e `audio/` (gravações da voz — ficam fora do git).
4. **`index.html`** da raiz a partir de `modelos/painel.html` — o painel do aprendiz.
5. **`progresso/tracker.html`** a partir de `modelos/tracker.html`, com o quadro vazio e, se houver
   prazo, a data de parar de puxar (prazo − 15 dias).
6. **`curriculo/index.html`** listando os blocos do plano, todos sem página ainda.

Substitua todos os `{{…}}` dos modelos. `lang` da língua-alvo: código BCP 47 (`es`, `es-AR`, `ja`,
`zh-Hans`…), anotado na seção 3 do perfil para os outros comandos usarem.

## 3. O Anki

Diga qual pacote importar, uma vez, antes de qualquer CSV:

- Língua com pacote pronto → `anki/pacotes/<Lingua>.apkg`.
- Outra língua → rode `python ferramentas/gerar_pacotes.py --lingua <Nome> --tts <xx_YY> --obrigado "<obrigado na língua>"`
  (acrescente `--pronuncia "<transliteração>"` e `--leitura` se a escrita não for latina; exige
  `pip install genanki`) e entregue o `.apkg` gerado. Nome ASCII, sem espaço nem acento.

Aponte `docs/anki.md` para as opções do deck (novos/dia, revisões/dia, ordem) e para a sincronização
se o aprendiz usar celular e computador.

## 4. Fechamento

Resuma em cinco linhas: objetivo, critério de sucesso, prazo, primeiro bloco, pacote a importar.
Termine propondo `/curriculo` para detalhar o primeiro bloco — não gere cartões nesta conversa.
