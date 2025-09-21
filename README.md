# 📚 Templates Perplexity Pro — Classificador de Complexidade
```markdown
Este repositório guarda modelos (.md) para classificar a complexidade de perguntas e decidir
 **quando usar resposta direta, GPT-4 Pro ou Busca Web (Perplexity Pro)**.
```
---

## 🧠 Como usar rapidamente
```markdown
1. **Abra `classificador.md`.**
2. **Copie o bloco desejado** (completo ou ultra-condensado).
3. **Cole no Perplexity** (no campo de pergunta) **antes de responder**.
4. Classifique a pergunta com os ícones: 🟢/🟡/🔴 e siga as instruções do nível.

### Fixe/Salve para acesso em 1 clique
- **Favorito no navegador:** abra `classificador.md` e pressione `Ctrl + D`.
- **Guia fixada:** com o arquivo aberto, clique com o botão direito na guia → **“Fixar guia”**.
```
---

## 🧩 Modelo Completo (copie e cole)

```markdown
🧠 **Classificador de Complexidade – Antes de Responder (Perplexity Pro):**

### Classifique a pergunta entre os três níveis abaixo:

🟢 **[complexidade=baixa]**
- ✅ Resposta direta com base interna.
- ❌ Sem busca web, sem GPT-4.
- Exemplos: "Ativar hibernação no Windows 11?", "O que é DLSS?"

🟡 **[complexidade=média]**
- ⚠️ Requer explicação técnica/comparação.
- ✅ Use GPT-4 Pro.
- ❌ Ainda sem busca web.
- Exemplos: "RTX 4060 vs 4070 em 1440p?", "i7-13650HX vs Ryzen 9 7940HS?"

🔴 **[complexidade=alta]**
- 🚨 Precisa de dados atualizados, preços ou benchmarks.
- ✅ Ative Perplexity Pro **com busca web**.
- ❓ Pergunte antes: "Quer que eu ative a busca para dados atuais no Brasil? 😊"
- Exemplos: "Notebook com RTX 4070 mais barato hoje?", "Melhor SSD Gen 4 em setembro de 2025".

**Critérios rápidos**
- Precisa de dado novo (preço/estoque/benchmark)? → 🔴
- Senão, avalie a dificuldade: simples → 🟢 | comparação/explicação → 🟡
```

---

## ⚡ Modelo Ultra-Condensado (atalho)

```markdown
🟢 [baixa]: responde com base interna, sem busca ou GPT-4
🟡 [média]: usa GPT-4 Pro, sem busca externa
🔴 [alta]: precisa de dados atuais → ativar busca (perguntar antes)

Critérios: precisa de dados novos? preço/produto/benchmark?
Se sim, 🔴. Se não, 🟢 ou 🟡 conforme a complexidade.
```

---

## 📎 Dica de bloco rápido

```markdown
### Classificar Pergunta

🟢 resposta direta
🟡 GPT-4 Pro (sem busca)
🔴 Buscar na web?

→ Minha pergunta:
```
