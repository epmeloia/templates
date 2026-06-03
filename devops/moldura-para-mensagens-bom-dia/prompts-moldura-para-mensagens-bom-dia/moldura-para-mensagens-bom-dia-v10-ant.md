# 📅🎨 Molduda para Menssagens de Bom Dia 🎨📅 - v10 - Ant:
"moldura-para-menssagens-bom-dia-v10-ant.md"

Este documento descreve **o que o sistema faz**, **como deve ser usado**, **regras obrigatórias**, **comportamentos proibidos** e **garantias de previsibilidade e ausência de erro silencioso**.

---

# 📘 Sistema de Geração de Mensagens Diárias

## Arquitetura por Blocos + Montagem Controlada

---

## 🎯 Objetivo do Sistema

Este sistema define um **processo controlado, previsível e sem ambiguidade** para a geração de imagens de mensagens diárias, com foco em:

* Clareza visual
* Hierarquia fixa
* Escalabilidade
* Zero erro silencioso
* Compatibilidade com limitações reais da ferramenta de geração de imagens

O sistema foi projetado para **eliminar retrabalho**, **evitar inferências automáticas indevidas** e **garantir consistência visual ao longo do tempo**.

---

## 🧱 Conceito Central: Arquitetura por Blocos

O sistema trabalha com **blocos independentes**, cada um com função clara e regras próprias.

### 🔹 Bloco 1 — Imagem Principal (Mensagem do Dia)

**Função**

* Comunicar a mensagem principal do dia.

**Conteúdo exclusivo**

* Data (maior hierarquia visual)
* Dia da semana (hierarquia secundária)
* Frase do dia (conteúdo central)

**Regras obrigatórias**

* Card de tamanho fixo e imutável
* Nunca recebe conteúdo extra
* Nunca cresce ou encolhe
* Nunca inclui comemorações
* É uma imagem finalizada e fechada

**Estilo visual**

* Estilo Disney/Pixar (cartoon, alegre, ilustrado)
* Texto mais nítido que o fundo
* Fundo ocupa aproximadamente 75% do quadro
* Fundo da área de texto com 95% de transparência
* Moldura sempre criativa, elegante e única

👉 **Bloco 1 comunica.**

---

### 🔹 Bloco 2 — Comemorações (Card Informativo Secundário)

**Função**

* Registrar comemorações de forma discreta e informativa.

**Conteúdo exclusivo**

* Título centralizado: **Comemorações**
* Lista de comemorações exatamente como fornecida pelo usuário

**Regras obrigatórias**

* Nunca contém:

  * Data em destaque
  * Dia da semana
  * Frase do dia
  * Narrativa
  * Personagens
  * Cena hero
* A data aparece apenas dentro das linhas informativas
* Fonte com aproximadamente 50% do tamanho da frase do Bloco 1
* Visual sempre secundário

**Herança visual**

* Herda clima visual do Bloco 1:

  * cores
  * ornamentos
  * atmosfera
* Não herda hierarquia, conteúdo ou protagonismo

👉 **Bloco 2 registra.**

---

## ⚙️ Regra Crítica: Canvas NÃO Faz Layout

### Princípio Fundamental

> **Canvas desenha.
> Layout organiza.
> A organização ocorre fora do gerador.**

Um gerador de imagem **sempre cria um único canvas**.
Ele **não entende layout estrutural real**.

Portanto:

* ❌ Nunca tentar gerar Bloco 1 e Bloco 2 no mesmo canvas
* ❌ Nunca pedir que o gerador “encaixe” ou “estenda” blocos

---

## 🧩 Regra Operacional Oficial (SOP)

### 🔒 Fluxo Obrigatório

#### Etapa 1 — Gerar Bloco 1

Comando:

```
# Gerar Bloco 1
```

Resultado:

* Uma imagem única
* Apenas Bloco 1
* Tamanho fixo

---

#### Etapa 2 — Gerar Bloco 2

Comando:

```
# Gerar Bloco 2
```

Resultado:

* Uma imagem única
* Apenas Bloco 2
* Card informativo

---

#### Etapa 3 — Montagem por Anexo (Split Vertical)

Procedimento:

1. O usuário anexa as duas imagens no chat
2. Solicita explicitamente a montagem, por exemplo:

   ```
   Use a imagem 1 como Bloco 1 (topo)
   Use a imagem 2 como Bloco 2 (embaixo)
   Monte em formato vertical (split)
   ```
3. A montagem é feita **fora do gerador**, em ferramenta externa:

   * Canva
   * Figma
   * PowerPoint
   * Photoshop
   * etc.

👉 O sistema **não tenta fundir imagens automaticamente**.

---

## 🚫 Comportamentos Proibidos

* ❌ Gerar Bloco 1 e Bloco 2 no mesmo canvas
* ❌ Inserir comemorações dentro do Bloco 1
* ❌ Reinterpretar blocos durante a montagem
* ❌ Inferir regras não declaradas
* ❌ Ajustar layout sem autorização explícita
* ❌ Produzir erro silencioso

---

## 🔐 Controle de Execução

* Nenhuma imagem é gerada sem comando explícito:

  * `# Gerar Bloco 1`
  * `# Gerar Bloco 2`
  * `# Gere`
* Em caso de dúvida:

  * Parar
  * Informar
  * Perguntar
  * Aguardar instruções

---

## ✍️ Regra de Ortografia (Obrigatória)

* Todo texto deve ser revisado
* Se houver erro ortográfico:

  * A execução deve ser interrompida
  * O erro deve ser informado
  * Aguardam-se novas instruções

---

## 🧠 Garantias do Sistema

Este sistema garante:

* Previsibilidade total
* Ausência de erro silencioso
* Reprodutibilidade
* Escalabilidade (1 ou 100 comemorações)
* Compatibilidade com limitações reais da ferramenta
* Redução drástica de retrabalho

---

## 📌 Modelo Mental Final

> **Bloco 1 comunica.
> Bloco 2 registra.
> A montagem respeita.**

---

## ✅ Status

* Documento oficial
* Pronto para versionamento
* Pronto para GitHub
* Fonte única da verdade

---

Se quiser, no próximo passo posso:

* gerar versão resumida para README
* versionar como `v1.0`, `v1.1`
* criar checklist operacional diário
* ou adaptar para pipeline automatizado

Este documento encerra a fase de definição do sistema.
