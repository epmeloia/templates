# **regra formal de versionamento futuro** - v10

"regra-formal-versionamento-futuro-v1.md"



Perfeito. Vou definir a **regra formal de versionamento futuro** de um jeito **simples**, **institucional**, e **a prova de equipe**.

A regra abaixo serve para:

* evitar “versao solta”
* evitar sobrescrita acidental
* permitir evolucao controlada (v10.2 → v11.0)
* manter rastreabilidade no GitHub

---

# ✅ REGRA FORMAL DE VERSIONAMENTO FUTURO (PADRAO OFICIAL)

## 1) Padrao de numero

Usaremos **SemVer simplificado**:

* **MAJOR** = muda comportamento / fluxo / gates / estrutura
* **MINOR** = melhora relevante, mas sem quebrar o fluxo
* **PATCH** = correcao pequena, ajuste fino, sem impacto real

Formato:

* `vMAJOR.MINOR` para prompts (ex: `v10.1`)
* opcionalmente `vMAJOR.MINOR.PATCH` se voce quiser granularidade (ex: `v10.1.1`)

👉 **Como ja esta em uso**: `v10.0` e `v10.1`
Perfeito. Mantemos assim.

---

## 2) Regra para quando criar v10.2

Criar `v10.2` quando houver:

* inclusao de regra nova aprovada
* melhoria que muda a saida padrao
* ajuste em gates
* mudanca em estrutura de entrada / saida
* mudanca em como Bloco 1 ou Bloco 2 operam

Exemplos tipicos:

* mudar “gates” de 2 para 3
* mudar definicao de estilo visual
* mudar layout fixo dos blocos

---

## 3) Regra para quando criar v11.0

Criar `v11.0` somente quando houver:

* **mudanca estrutural grande**
* **quebra de compatibilidade mental**
* **novo modo de uso**
* refatoracao relevante do sistema

Exemplos tipicos:

* mudar o conceito de Bloco 1/Bloco 2
* mudar formato obrigatorio de entrada
* mudar o modelo de confirmacoes (checklists)
* mudar a arquitetura de arquivos

---

## 4) Nome de arquivo (regra rigida)

### Para prompts operacionais

* `moldura-para-menssagens-bom-dia-v10.md`
* se atualizar: criar novo arquivo

  * `moldura-para-menssagens-bom-dia-v10.1.md`
  * ou manter “v10” como “latest estavel” e guardar numeradas como historico

👉 Aqui existem duas estrategias. Como voce pediu simples, eu recomendo:

* **arquivo estavel**: `...-v10.md` (sempre o ultimo estavel)
* **arquivo historico**: `...-v10.1.md`, `...-v10.2.md` etc.

Assim:

* o time usa sempre o `v10.md`
* quem audita usa os numerados

### Para prompt de clonagem

Regra fixa (como voce ja fez):

* `prompt-clonagem-continuidade-v10.0.md`
* `prompt-clonagem-continuidade-v10.1.md`
* `prompt-clonagem-continuidade-v10.2.md` etc.

---

## 5) Regra de changelog (minimo obrigatorio)

Toda nova versao cria um bloco “Changelog” com:

* Data
* Motivo (1 linha)
* Mudancas (bullets)
* Riscos / mitigacao (1 linha)

Sem isso, a versao e considerada **nao valida** para distribuicao.

---

## 6) Regra de “latest”

O “latest” deve ser explicitado no README.md:

* Latest estavel: V10.1 (ou V10.2 etc.)
* Arquivo preferencial de clonagem: `prompt-clonagem-continuidade-v10.1.md`

Isso evita que alguem use sem querer um arquivo antigo.

---
