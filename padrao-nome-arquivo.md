# Local: **templates/padrao-de-nomes.md**


---

## Padrão de nomes (simples e consistente)

*  **Prefixo numérico de 1 dígitos** para ordenação: `0`
*  **Sem espaços, acentos ou maiúsculas** em nomes de pastas/arquivos.
*  **Sem acentos/cedilha** no nome do arquivo (evita bugs em links): `botao`, `glossario`, `instrucao`
*  **kebab-case** (minúsculas + hífens): `info-util-0-b-0-botao-dif.md`
*  **Evite** `--` duplo; use 1 hífen por separação


---

## Blocos Numéricos:

*  **0-b-0:	botao** (UI do GitHub)
*  **0-i-0:	itens** (conceitos de arquivos, commits, diff…)
*  **0-p-0:	pastas** (estrutura, caminhos, links relativos entre pastas)
*  **0-l-0:	links** (Raw, permalink, anchors, cross-links)
*  **0-m-0:	meta** (índices, convenções, checklists)

>   Assim a Ordem é automática, ficando osdenado por Categoria.

>   Na ocorrencia de "categorias" com a mesma inicial, o próprio nome completo da "categoria" vai separar os itens.


---

## Convenção sem Nomes:

*  **info-util-0-b-0:** **botao** (UI do GitHub)
*  **info-util-0-i-0:** **itens** (conceitos de arquivos, commits, diff…)
*  **info-util-0-p–0:** **pastas** (estrutura, caminhos, links relativos entre pastas)
*  **info-util-0-l–0:** **links** (Raw, permalink, anchors, cross-links)
*  **info-util-0-m–0:** **meta** (índices, convenções, checklists)


---

## Convenção com Nomes:

*  **info-util-0-b-0-botao-dif.md**
*  **info-util-0-i-0-itens-branch.md**
*  **info-util-0-p-0-pull-request.md**
*  **info-util-0-d-0-diff-vs-commit.md**
*  **README.md**   ← índice com links



---

## Modelo para Conteudo de Arquivos:

*  Copie este cabeçalho no topo de cada “info-util-0-\*”:

```markdown
# Info Útil — Título curto (ex.: Botão “Show Diff”)

**Categoria:** GitHub • **Nível:** básico • **Atalho:** `0`

## O que é
(2–3 linhas)

## Para que serve
(2–3 bullets)

## Como usar (passos curtos)
1.
2.
3.

## Dicas
- …
- …

## Ver também
- [info-util-0-i-0-itens-branch.md](./info-util-0-i-0-itens-branch.md)
```


---

## README de índice da pasta (faça 1 vez)

*  Crie/edite `mini-glossarios/README.md` e cole:

```markdown
# 📇 Mini-Glossários — Índice

[info-util-0-b-0-botao-dif.md](./info-util-0-b-0-botao-dif.md)
[info-util-0-i-0-itens-branch.md](.info-util-0-i-0-itens-branch.md)
[info-util-0-i-0-itens-pull-request.md](./info-util-0-i-0-itens-pull-request.md)
```


---

## Regras Gerais

*  **2 dígitos para ordem: `00`**
*  **foco no **que é** + **para que serve** já no nome
*  **prefixo fixo + ordem + categoria + assunto**
*  **kebab-case**, sem acentos: `botao`, `pastas`, `itens`, `links`
*  **`info-util-0-<primeira letra da categoria>-0-<categoria>-<assunto>.md`**
*  **Ex:**
    ```
    `info-util-0-b-0-botao-show-diff.md`
    ```


---

# **Pastas e propósito:  `Ex.:`**

## **`templates/mini-glossarios/`**

*  **O que entra aqui:** definições rápidas e peças da interface (conceito/“o que é/para que serve”).

*  **Exemplos de nomes prontos:**
   ```
   *  `info-util-0-b-0-botao-show-diff.md` — botão **Show Diff / Preview changes**
   *  `info-util-0-b-0-botao-raw.md` — botão **Raw**
   *  `info-util-0-i-0-itens-commit.md` — o que é **commit**
   *  `info-util-0-i-0-itens-diff.md` — o que é **diff**
   *  `info-util-0-p-0-pastas-links-relativos.md` — como funcionam links relativos
   *  `info-util-0-l-0-links-raw-githubusercontent.md` — link Raw: quando usar
   ```


## **`templates/mini-instrucoes/`**

*  **O que entra aqui:** passo-a-passo de tarefas (como fazer).

*  **Exemplos de nomes prontos:**
   ```
   *  `info-util-0-b-0-botao-como-usar-show-diff.md` — usar o botão Show Diff num PR/commit
   *  `info-util-0-p-0-pastas-criar-mover-arquivo.md` — criar pasta e mover arquivo no GitHub Web
   *  `info-util-0-p-0-pastas-renomear-arquivos.md` — renomear arquivos/paths no GitHub Web
   *  `info-util-0-l-0-links-criar-raw-e-permalink.md` — gerar links Raw e “permalink”
   *  `info-util-0-l-0-links-cruzar-docs-relativos.md` — cruzar docs via links relativos
   ```

>  **dica:** se a página for “o que é…”, vai no **glossário**; se for “como fazer…”, vai em **instruções**.


---

# Cabeçalho recomendado dentro do arquivo

- Use títulos com **emojis** (no conteúdo, não no nome do arquivo) para “destacar” visualmente:

*  Para **Glossário**:

   ```markdown
   #  🟩 Botão — Show Diff (Preview changes) 〔Glossário〕
   **Categoria:** botao • **Nível:** básico • **Código:** 00
   
   ## O que é
   … (2–3 linhas)
   
   ## Para que serve
   - …
   - …
   
   ## Ver também
   - ➡️ **Instrução:** [Como usar o botão Show Diff no PR](../mini-instrucoes/info-util-00-botao-como-usar-show-diff.md)
   ```


*  Para **Instruções**:

   ```markdown
   # 🛠️ Instrução — Criar pasta e mover arquivo no GitHub Web
   **Categoria:** pastas • **Nível:** básico • **Código:** 10
   
   ## Passos rápidos
   1) …
   2) …
   3) …
   
   ## Conceitos relacionados
   - 📘 *Glossário:* [Links relativos entre pastas](../mini-glossarios/info-util-20-pastas-links-relativos.md)
   ```


---

# Regras para **links** (muito importantes)

   *  **Sempre que possível, use link relativo** (mais robusto a renomeações):
   *  de `mini-instrucoes` → `mini-glossarios`:
      `../mini-glossarios/info-util-20-pastas-links-relativos.md`
   *  Se precisar de um link “copiar e colar” externo, use **RAW** (texto puro) ou a **página normal**:
   *  Raw (texto puro): `https://raw.githubusercontent.com/<user>/<repo>/refs/heads/main/<caminho>.md`
   *  Página do GitHub: `https://github.com/<user>/<repo>/blob/main/<caminho>.md`
   *  **Pode linkar para arquivos que ainda não existem** (placeholder). Use o nome **padrão** que você pretende criar depois.
   *  **Ex:**
   ```
   `../mini-instrucoes/info-util-21-links-cruzar-docs-relativos.md` (a criar)
   ```


---

# Cheats de nomeação (faça copiar/colar)

   *  **Glossário (o que é):**

   ```
   *  `info-util-0-b-0-botao-<acao>.md
   *  `info-util-0-i-0-itens-<conceito>.md
   *  `info-util-0-p-0-pastas-<tema>.md
   *  `info-util-0-l-0-links-<tipo>.md
   ```

   *  **Instrução (como fazer):**

   ```
   *  `info-util-<0>-b-<0>-botao-como-usar-<acao>.md
   *  `info-util-<0>-p-<0>-pastas-<verbo>-<objeto>.md
   *  `info-util-<0>-l-<0>-links-<verbo>-<objeto>.md
   ```

---
