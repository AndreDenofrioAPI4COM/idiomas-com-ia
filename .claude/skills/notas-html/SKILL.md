---
name: notas-html
description: Convenções de marcação HTML do material de estudo da Rota 2 (Claude Code) — esqueleto da página, atributo lang da língua-alvo, ruby para transliteração, blocos de exemplo, fórmula, glosas Leipzig, exercícios com gabarito, cores de tom opcionais e índices de pasta. Use sempre que criar ou editar qualquer arquivo .html do repositório.
---

# Marcação HTML do material de estudo

Na Rota 2 o material de estudo é **HTML** (páginas de bloco, gramática, leitura, história, tema,
música, diário, avaliação, tracker, painel). Docs do framework, perfil e método continuam em
Markdown; cartões continuam em CSV (`assistente/metodo.md`, seção 3).

Antes de gerar, leia `assistente/perfil.md` para saber a **língua-alvo** e o seu código BCP 47
(`es`, `es-AR`, `en`, `fr`, `de`, `it`, `ja`, `zh-Hans`, `ko`, `ru`…) e se ela tem transliteração.

## 1. Esqueleto obrigatório

Parta sempre de um arquivo de `modelos/`. Estrutura mínima:

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Cumprimentos — Bloco 01 · Idiomas com IA</title>
  <link rel="stylesheet" href="../assets/estudo.css">
  <meta name="idiomas:tipo" content="bloco">   <!-- bloco|gramatica|leitura|historia|tema|musica|diario|avaliacao|indice|painel|tracker -->
  <meta name="idiomas:data" content="2026-01-15">
  <meta name="idiomas:bloco" content="cumprimentos">   <!-- slug do bloco, ou “—” -->
</head>
<body>
<nav class="breadcrumb"><a href="../index.html">Início</a> › <a href="index.html">Currículo</a> › B01</nav>
<header class="pagina">
  <p class="kicker">Currículo · Bloco 01 · <code>bloco::cumprimentos</code></p>
  <h1>Cumprimentos</h1>
  <p class="resumo">O que você passa a conseguir fazer quando este bloco fechar.</p>
</header>
<main>…</main>
<footer class="rodape"><p>Gerado em 2026-01-15 por <code>/curriculo</code></p></footer>
</body>
</html>
```

- `lang="pt-BR"` (ou a língua de explicação do perfil) na página. **Todo trecho na língua-alvo leva
  o `lang` dela** — o navegador escolhe a fonte certa e o leitor de tela pronuncia certo.
- Caminho do CSS: `assets/estudo.css` na raiz, `../assets/estudo.css` em subpasta,
  `../../assets/estudo.css` em `progresso/avaliacoes/`.
- As três metas `idiomas:*` são o que permite reindexar as páginas depois. Nunca omita.

## 2. Língua-alvo, transliteração, tradução

**Frase de exemplo** — sempre nesta ordem: alvo, pronúncia (se a língua tiver), tradução.

```html
<figure class="exemplo">
  <p class="alvo" lang="es">¿Me traés la cuenta, por favor?</p>
  <p class="tr">Você me traz a conta, por favor?</p>
  <figcaption class="nota">voseo: <em>traés</em>, não <em>traes</em>.</figcaption>
</figure>
```

Em língua com transliteração, inclua `.pron` entre `.alvo` e `.tr`:

```html
<figure class="exemplo">
  <p class="alvo" lang="ja">ありがとうございます。</p>
  <p class="pron">arigatō gozaimasu</p>
  <p class="tr">Muito obrigado.</p>
</figure>
```

**Entrada de vocabulário** — `<ruby>` põe a transliteração em cima do item:

```html
<dl class="vocab">
  <dt lang="zh-Hans"><ruby>咖<rt>kā</rt>啡<rt>fēi</rt></ruby></dt>
  <dd>
    <span class="tr">café</span>
    <span class="classe">subst.</span>
    <span class="info">CL: <span lang="zh-Hans">杯</span> bēi</span>
    <span class="nivel">A1</span>
  </dd>
</dl>
```

- Língua de alfabeto latino não usa `<ruby>`; a pronúncia, quando a escrita engana, vai em `.info`.
- `.info` carrega o que vem colado ao item: gênero/plural, classificador, par de aspecto, regência,
  registro — o mesmo conteúdo da coluna `nota` do CSV.

**Cores de tom (opcional, só língua tonal)** — classes `.t1 .t2 .t3 .t4 .t0`:

```html
<span lang="zh-Hans"><span class="t3">你</span><span class="t3">好</span></span>
```

Mudança de tom por contexto (sandhi) vai em `<span class="sandhi">` ou na `figcaption.nota`.
Escreva a forma de citação e explique a mudança.

## 3. Classes disponíveis em `assets/estudo.css`

| Classe | Uso |
|---|---|
| `.alvo` / `.pron` / `.tr` | as três linhas de um exemplo |
| `figure.exemplo` | bloco de frase-exemplo |
| `dl.vocab` + `.tr` `.classe` `.info` `.nivel` | lista de vocabulário |
| `.formula` | construção em slots: `S + gostar de + inf.` |
| `.errado` | forma agramatical; o CSS prefixa `*` e risca |
| `.contraste` | "onde a sua língua atrapalha" |
| `.cultura` | nota cultural |
| `.alerta` | `⚠️ verificar` — item que precisa de conferência humana |
| `.challenge` | item acima do nível atual |
| `table.glosa` com linhas `.alvo` `.pron` `.gl` | glosas Leipzig |
| `.exercicios` + `details.gabarito` | exercícios com respostas recolhidas |
| `details.recolhido` | qualquer outro conteúdo recolhido (tradução, versão com transliteração) |
| `table.tabela` dentro de `.rolavel` | tabela padrão, rolável no celular |
| `.cards` | grade de links (índices e painel) |
| `.quadro` + `.coluna` (`.fazendo`, `.done`) | quadro kanban do tracker |
| `.barra > span` | barra de progresso |
| `.veredito` (`.pronto`, `.trava`, `.nao`) | veredito de simulação |
| `.dod` | critério de pronto no cabeçalho do bloco |
| `.t1`–`.t4`, `.t0`, `.sandhi` | tons (opcional) |

## 4. Glosas Leipzig

Uma coluna por palavra ou morfema, nunca texto corrido. Abreviações padrão de Leipzig
(`1SG`, `PL`, `PST`, `PFV`, `NEG`, `Q`, `CL`, `GEN`, `ACC`…); as específicas da língua ficam
listadas na seção de convenções do perfil.

```html
<div class="rolavel">
<table class="glosa">
  <tr class="alvo" lang="es"><td>me</td><td>lo</td><td>dij-o</td></tr>
  <tr class="gl"><td>1SG.DAT</td><td>3SG.M.ACC</td><td>dizer-3SG.PST</td></tr>
</table>
</div>
<p class="tr">Ele me disse isso.</p>
```

## 5. Exercícios e gabarito

```html
<section class="exercicios">
  <h2>Produza</h2>
  <ol><li>Você chegou ao balcão e é a sua vez de pedir um café.</li></ol>
  <details class="gabarito">
    <summary>Gabarito</summary>
    <ol><li><span lang="es">Un café, por favor.</span></li></ol>
  </details>
</section>
```

Gabarito **sempre** em `<details>`, nunca visível de cara. Todo exercício também vira linha de CSV
(`tipo::exercicio`, enunciado em `situacao`, resposta em `alvo`).

## 6. Índices de pasta

Cada pasta de conteúdo tem `index.html` (de `modelos/indice.html`) com uma grade `.cards`. **Ao criar
uma página nova, acrescente o card no índice da pasta na mesma sessão** — e, se for página de bloco
ou avaliação, também no painel (`index.html` da raiz). Índice desatualizado é o principal jeito de
perder material.

## 7. Regras gerais

- HTML5 semântico: `<article>`, `<section>`, `<figure>`, `<dl>`, `<details>`.
- **Zero `<style>` e zero `style=`.** Faltou estilo: acrescente a classe em `assets/estudo.css` e
  documente na tabela da seção 3.
- **Zero JavaScript, zero CDN, zero fonte ou imagem remota.** A pasta inteira abre offline.
- Links sempre relativos.
- Uma página, um assunto. Página gigante vira duas.
- Placeholders dos modelos (`{{TITULO}}`, `{{DATA}}`…) não podem sobrar na página final.
