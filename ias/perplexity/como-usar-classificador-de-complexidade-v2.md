# 💡 Como Usar o Classificador de Complexidade:
"como-usar-classificador-de-complexidade-v2.md"

   * 📌 Colar esse template no topo de qualquer nova sessão ou aba no Perplexity Pro.
   * 📎 Fixar o **modelo condensado** como referência rápida.
   * 🧠 Classificar antes de responder e evitar uso desnecessário de recursos pagos.

1. Classifique mentalmente (ou via prompt) como:

   * `[complexidade=baixa]` → responda direto.
   * `[complexidade=média]` → use GPT-4 Pro sem busca.
   * `[complexidade=alta]` → clique para ativar busca web.

2. cole isto antes da sua pergunta, adicione:

   * 🟢 [baixa]: responde com base interna, **sem busca**  
   * 🟡 [média]: usa **GPT-4 Pro**, **sem busca externa**  
   * 🔴 [alta]: precisa de **dados atuais** → **ativar busca** (perguntar antes)

   * **Critérios rápidos:** precisa de dado novo? fala de **preço/produto/benchmark**?  
   * → Se **sim**, 🔴. Se **não**, 🟢 ou 🟡 conforme a dificuldade.
   * *"Essa consulta exige dados atualizados. Deseja que eu ative a busca para isso?"*

3. **Comece com sua resposta simples.**


---

# 📌 Dica de Prompt Rápido para Classificação

Classifique esta pergunta entre três níveis de complexidade:
[complexidade=baixa] [complexidade=média] [complexidade=alta]
Baseie-se em: necessidade de dados atualizados, presença de nomes específicos, benchmarking ou comparação de produtos.


---
# 📚 Templates Perplexity Pro

## 🧠 Classificador de Complexidade

🟢 [baixa]: responde com base interna, sem busca ou GPT-4  
🟢 [complexidade=baixa] → responda direto.  
🟡 [média]: usa GPT-4 Pro, mas sem busca externa  
🟡 [complexidade=méda] → use GPT-4 Pro sem busca.  
🔴 [alta]: precisa de dados atuais → ativar busca (perguntar antes)  
🔴 [complexidade=alta]→ clique para ativar busca web.  


## 📋 Critérios de Decisão
- A pergunta precisa de dados atualizados?  
- Fala de preço, produto ou benchmark?  
- Se sim → 🔴  
- Se não → 🟢 ou 🟡 conforme a dificuldade.


## 📎 Anotações rápidas
- 🔁 Comece **sempre** pela solução simples (Navalha de Occam).  
- ⬆️ Escale para 🔴 **só** quando depender de dado novo/mercado.  
- 🇧🇷 Quando ativar busca, **mencione Brasil** (preços/estoque locais).


---

## 🧠 Como usar rapidamente

1. **Abra `classificador.md`.**
2. **Copie o bloco desejado** (completo ou ultra-condensado).
3. **Cole no Perplexity** (no campo de pergunta) **antes de responder**.
4. Classifique a pergunta com os ícones: 🟢/🟡/🔴 e siga as instruções do nível.

## Fixe/Salve para acesso em 1 clique
- **Favorito no navegador:** abra `classificador.md` e pressione `Ctrl + D`.
- **Guia fixada:** com o arquivo aberto, clique com o botão direito na guia → **“Fixar guia”**.


---

# 🧩 Modelo Completo - v1

## 🧠 **Classificador de Complexidade – Antes de Responder:**

*  Classifique a pergunta entre os três níveis abaixo:

```plaintext
🟢 **[complexidade=baixa]**  
- ✅ Resposta direta, sem precisar de busca nem GPT-4.  
- ❌ Não usar busca paga.  
- **Exemplos:**  
   - "Como ativar hibernação no Windows 11?"  
   - "O que é DLSS?"  



🟡 **[complexidade=média]**  
- ⚠️ Requer explicação ou comparação técnica.  
- ✅ Use GPT-4 Pro.  
- ❌ Ainda sem busca web.  
- **Exemplos:**  
   - "RTX 4060 vs 4070 para 1440p?"  
   - "Melhor setup multitarefa com Ryzen?"  



🔴 **[complexidade=alta]**  
- 🚨 Precisa de dados atualizados, preços ou benchmarks.  
- ✅ Use Perplexity Pro com busca web.  
- ❓ Sempre perguntar antes:  
  _"Deseja que eu ative a busca para dados atuais no Brasil? 😊"_  
- **Exemplos:**  
   - "Melhor SSD Gen 4 em setembro de 2025"  
   - "Notebook RTX 4070 mais barato hoje"



🔎 **Critérios de Avaliação:**  
- A pergunta precisa de dados novos?  
- Cita modelos/marcas específicas?  
- Fala de preços, benchmarks ou comparações complexas?



```


---

## ⚡ Modelo Ultra-Compacto - v1

```markdown
🟢 [baixa]: responde com base interna, sem busca ou GPT-4
🟡 [média]: usa GPT-4 Pro, sem busca externa
🔴 [alta]: precisa de dados atuais → ativar busca (perguntar antes)

Critérios: precisa de dados novos? preço/produto/benchmark?
Se sim, 🔴. Se não, 🟢 ou 🟡 conforme a complexidade.
```

---

## ⚡ Modelo Ultra-Compacto - v2

```plaintext
# Classificar Pergunta

🟢 = resposta direta  
🟡 = GPT-4  
🔴 = Buscar na Web?

→ Minha pergunta:

Colar a dúvida abaixo!
```


---

# ✅ Estrutura do Filtro

## 🧠 Classificador de Complexidade para Perplexity Pro

```plaintext
[Etapa 1] Análise da Pergunta:
- Contém nomes de produtos, datas ou marcas específicas? (Ex: "RTX 5090", "2025", "Melhor SSD atual")
- Depende de dados atualizados ou de mercado?
- Requer benchmarks, preços ou disponibilidade no Brasil?

[Etapa 2] Classificação Automática:

1. [complexidade=baixa]
   - ✅ Resposta pode ser dada sem busca externa.
   - Exemplos:
     - "Como ativar hibernação no Windows 11?"
     - "O que é DLSS?"
   - ✅ Use modo básico (sem busca).
   - ❌ Não acione o Perplexity Pro com busca web.

2. [complexidade=média]
   - ⚠️ Exige explicação técnica, comparação ou múltiplos fatores.
   - Exemplos:
     - "RTX 4060 vs RTX 4070 para jogos em 1440p?"
     - "Qual melhor processador Intel para multitarefa?"
   - ✅ Use modo premium se necessário.
   - ❌ Não acione busca web ainda.

3. [complexidade=alta]
   - 🚨 Exige informação atualizada, preços ou disponibilidade real.
   - Exemplos:
     - "Melhores notebooks com RTX 4070 em setembro de 2025"
     - "Qual SSD Gen 4 mais barato hoje com leitura acima de 7000 MB/s?"
   - ✅ Ative o Perplexity Pro com busca.
   - 🔁 Ofereça confirmação ao usuário antes de usar:

     _"Deseja que eu verifique os dados mais recentes e preços válidos agora no Brasil? Posso usar a busca para isso. 😊"_
```

---



