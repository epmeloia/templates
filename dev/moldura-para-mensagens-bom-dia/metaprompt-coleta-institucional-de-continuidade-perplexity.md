# METAPROMPT — COLETA INSTITUCIONAL DE CONTINUIDADE

Você deve analisar ESTE chat ativo e gerar um arquivo Markdown chamado:

📄 **Analise Prompt.md**

Este arquivo deve conter um **dump institucional completo**, estruturado, sem resumo e sem interpretação criativa.

---

## 🎯 OBJETIVO

Gerar um snapshot confiável para:

- Continuidade em novo chat
- Comparação com versões anteriores (V10 → V11)
- Auditoria institucional
- Reinstalação total de contexto operacional

Este processo **NÃO resume conversa**.  
Ele **reconstrói estado mental, regras e arquitetura**.

---

## 📦 CONTEÚDO OBRIGATÓRIO DO ARQUIVO

O arquivo **Analise Prompt.md** deve conter **EXATAMENTE** as seções abaixo, nesta ordem:

---

### 1️⃣ IDENTIDADE DO PROJETO

- Nome do projeto
- Versão operacional atual (ex: V10)
- Data aproximada do snapshot
- Ambiente de uso (ex: ChatGPT / COMET)
- Status: ATIVO ou HISTÓRICO

---

### 2️⃣ PROMPTS ATIVOS EM USO

Liste **integralmente** (sem cortar):

- Prompt operacional principal
- Prompt de clonagem / continuidade
- Regras adicionais coladas no início do chat

👉 Se algo estiver “implícito”, registre como:
> ⚠️ Regra implícita detectada (descrever)

---

### 3️⃣ LISTA MESTRA ATUAL (COMPLETA)

Copiar a **LISTA MESTRA exatamente como aparece no chat**, mantendo:

- Estados: `[OK] / [ ] / [NOT OK] / [EXEC] / [NOT NEC]`
- Ordem
- Descrições
- Blocos de separação

❌ Não reorganizar  
❌ Não resumir  

---

### 4️⃣ BLOCOS FUNCIONAIS EXISTENTES

Descrever claramente:

- Bloco 1 — finalidade, regras críticas, problemas atuais
- Bloco 2 — finalidade, regras críticas, problemas atuais
- Como ocorre a montagem (externa)

Usar apenas o que está definido no chat.

---

### 5️⃣ REGRAS CRÍTICAS E GATES

Listar explicitamente:

- Gates de pré-visualização
- Confirmação final
- Comandos obrigatórios
- Comportamentos proibidos

Se alguma regra for violada no histórico recente, registrar.

---

### 6️⃣ POLÍTICAS INSTITUCIONAIS ATIVAS

Referenciar:

- Bloco institucional (políticas consolidadas)
- Regras de revisão ortográfica / semântica / pragmática
- Regras de versionamento

Indicar se estão:
- Ativas
- Suspensas
- Em revisão

---

### 7️⃣ AJUSTES RECENTES REALIZADOS NO CHAT

Listar mudanças feitas **neste chat**, por exemplo:

- Alteração de foco do Bloco 1
- Separação rigorosa de blocos
- Mudança de fluxo
- Correções visuais ou conceituais

---

### 8️⃣ PROBLEMAS CONHECIDOS (SE EXISTIREM)

Registrar apenas fatos:

- O que falhou
- Onde falhou
- Estado atual (corrigido / pendente)

❌ Não sugerir solução

---

### 9️⃣ STATUS FINAL DE CONTINUIDADE

Responder objetivamente:

- Este snapshot é suficiente para continuar em novo chat? (SIM/NÃO)
- Alguma informação crítica está faltando? (SIM/NÃO)
- Há risco de erro silencioso se continuar apenas com este arquivo? (SIM/NÃO)

Justificar brevemente cada resposta.

---

## 🧾 FORMATO FINAL

- Markdown limpo
- Sem emojis excessivos
- Sem linguagem subjetiva
- Sem opinião
- Sem explicações fora do escopo

O arquivo **Analise Prompt.md** deve ser imediatamente utilizável por outro assistente para continuidade do projeto.

---

## ⛔ PROIBIÇÕES

- Não resumir conversa
- Não reescrever regras
- Não “melhorar” textos
- Não corrigir estilo
- Não inferir intenção do usuário

Apenas **extrair, estruturar e registrar**.

---

## ✅ ENCERRAMENTO

Finalize o arquivo com:

> “Snapshot institucional gerado para continuidade controlada.”

E encerre a execução.

