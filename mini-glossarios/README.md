# Local: **templates/mini-glossarios/README.md**


---

# 📚 Mini-Glossários:

* **Mini-Glossários** = “o que é | para que serve”, todos os conceitos e peças da UI.
* **Pedaços curtos** para lembrar **o que é** e **para que serve** (Ex: UI | conceitos | links).
* **O que entra aqui:** definições rápidas e peças da interface (conceito/“o que é/para que serve”).
* **Sem espaços, acentos ou maiúsculas** em nomes de pastas/arquivos.
* **Prefira `kebab-case`** (`perplexity`, `classificador-de-complexidade.md`).
* **Use uma pasta única para imagens**

* **Ex:**
  ```
  ![print Perplexity](assets/print-perplexity.png)
  
  Explicando Linha de Comando:
  * "!" = Sempre no Inicio.
  * "[]" = Usado com inf sobre a imagem, mas pode ficar "[]".
  * "()" = Caminho aonde a Imagem.
  ```

---

## **Exemplos de nomes prontos:**

* `info-util-0-b-0-botao-show-diff.md` — botão *Show Diff / Preview changes*
* `info-util-0-b-0-botao-raw.md` — botão *Raw*
* `info-util-0-i-0-itens-commit.md` — o que é *commit*
* `info-util-0-i-0-itens-diff.md` — o que é *diff*
* `info-util-0-p-0-pastas-links-relativos.md` — como funcionam links relativos
* `info-util-0-l-0-links-raw-githubusercontent.md` — link Raw: quando usar


---

## **Categorias**

### 👁️ Botão (b)
- `b` = **botao** (UI do GitHub)
- [info-util-0-b-0-botao-show-diff.md](./info-util-0-b-0-botao-show-diff.md) — Show Diff / Preview changes
- *(adicione aqui novos botões seguindo o padrão acima)*

### 🧩 Itens (i)
- `i` = **itens** (conceitos: commit, diff, etc.)
- *(placeholder — crie quando precisar, ex.: `info-util-0-i-0-itens-diff.md`)*

### 🗂️ Pastas (p)
- `p` = **pastas** (estrutura e caminhos)
- *(placeholder — ex.: `info-util-0-p-0-pastas-links-relativos.md`)*

### 🔗 Links (l)
- `l` = **links** (Raw, permalink, anchors…)
- *(placeholder — ex.: `info-util-0-l-0-links-raw-githubusercontent.md`)*

### 🧭 Meta (m)
- `m` = **meta** (índices, convenções)
- *(placeholder — ex.: `info-util-0-m-0-meta-convencoes.md`)*


---

## Como adicionar um novo item (ultrarrápido)

1. **Nomeie**: `info-util-<n>-<letra>-<n>-<categoria>-<assunto>.md`  
   ex.: `info-util-0-l-0-links-raw-githubusercontent.md`
2. **Crie o arquivo** nesta pasta e preencha com o cabeçalho:

   # 🟩 <Categoria> — <Assunto> 〔Glossário〕
   **Categoria:** <categoria> • **Código:** <n>

   ## O que é
   (2–3 linhas)

   ## Para que serve
   - ponto 1
   - ponto 2

   ## Ver também
   - ➡️ *Instrução:* ../mini-instrucoes/<arquivo-relacionado>.md


3. **Linke aqui** no índice, na seção da categoria.

> Dica: pode linkar para arquivos ainda não criados (placeholders) usando o **mesmo padrão de nome** — você cria depois.


---

## Procurar e Revisar Rápido

* Na barra de busca do repositório, pesquise por:
  `repo:epmeloia/templates mini-glossarios/ info-util-`
* Para conferir alterações antes de salvar, use **Show Diff / Preview changes**.


---

## Previa de Arquivos:

- Botões:
  *`info-util-0-b-0-botao-add-file.md` *("Upload files")*
  *`info-util-0-b-0-botao-commit-changes.md`
  *`info-util-0-b-0-botao-create-new-file.md`
  *`info-util-0-b-0-botao-delete-this-file.md`
  *`info-util-0-b-0-botao-edit-lapis.md`
  *`info-util-0-b-0-botao-raw.md`
  *`info-util-0-b-0-botao-show-diff.md` *("Preview changes")*
  *`info-util-0-b-0-botao-upload-files.md`

- Itens / Conceitos:
  * `info-util-0-i-0-itens-branch.md`
  * `info-util-0-i-0-itens-commit.md` *("changes")*
  * `info-util-0-i-0-itens-dco-sign-off.md`
  * `info-util-0-i-0-itens-diff.md`
  * `info-util-0-i-0-itens-fork.md`
  * `info-util-0-i-0-itens-in-main`
  * `info-util-0-i-0-itens-pull-request.md`
  * `info-util-0-i-0-itens-redirect-apos-renomear.md` *(redirecionos após renomear repo)*
  * `info-util-0-i-0-itens-repo-about.md` *(“About/Description/Website/Topics”)*
  * `info-util-0-i-0-itens-template-repository.md`

- Links:
  * `info-util-0-l-0-links-atualizar-apos-renomear.md` *(estratégia e impactos)*
  * `info-util-0-l-0-links-blob-main-significado.md` *(o que é `/blob/main/`)*
  * `info-util-0-l-0-links-bookmarklet-converter-raw.md`
  * `info-util-0-l-0-links-busca-no-repositorio.md` *(`repo:<user>/<repo>` | “In this repository”)*
  * `info-util-0-l-0-links-plain-param.md` *(uso do `?plain=1` | texto puro no GitHub)*
  * `info-util-0-l-0-links-raw-githubusercontent.md` *("quando usar")*
  * `info-util-0-l-0-links-raw-vs-blob.md`
  * `info-util-0-l-0-links-relativos.md` *("Links relativos entre pastas")*

- Meta:
  * `info-util-0-m-0-meta-checklist-commit-diff.md`
  * `info-util-0-m-0-meta-convencoes-nomeacao.md` *(kebab-case, números, sem acentos)*
  * `info-util-0-m-0-meta-estrutura-repositorio-templates.md` *(pastas/índices)*
  * `info-util-0-m-0-meta-links-rapidos-readme.md` *(seção de “Links rápidos”)*

- Pastas / Estrutura:
  * `info-util-0-p-0-pastas-criar.md` *(conceito/organização de pastas)*
  * `info-util-0-p-0-pastas-criar-assets-e-upload.md` *(conceito e porquês)*
  * `info-util-0-p-0-pastas-criar-subpasta-e-readme-indice.md` *(conceito do índice por pasta)*
  * `info-util-0-p-0-pastas-mover-arquivo.md` *(conceito de mover via editar caminho)*
  * `info-util-0-p-0-pastas-renomear-arquivo.md`

---
