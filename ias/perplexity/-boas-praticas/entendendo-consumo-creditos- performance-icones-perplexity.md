# Entendendo o Consumo de Créditos e Performance dos Ícones

Com base na análise dos três ícones da sua interface (lupa, elos entrelaçados e lâmpada), vou explicar de forma prática como otimizar o uso de cada um para reduzir consumo de créditos e manter alta performance.

---

## Qual Ícone Deixar Ativado - Exemplos Práticos

---

### 🔍 **Ícone de Lupa (Busca)**

✅ **Quando deixar ativado:**
1. **Busca local em dados já carregados** - Ative sempre, consome apenas CPU local
2. **Busca com cache inteligente** - Para consultas repetidas, economiza 90% dos créditos
3. **Busca em índices pré-processados** - Resultados instantâneos sem consumo de API

🚧 **Quando evitar:**
1. **Busca em tempo real sem debounce** - Cada tecla = 1 requisição = muitos créditos gastos
2. **Busca em APIs externas caras** - OpenAI, Google Search custam por consulta
3. **Busca sem cache** - Repetir mesma consulta gasta créditos desnecessariamente


---

### 🔗 **Ícone de Elos (Workflow/Integração)**

✅ **Quando deixar ativado:**
1. **Automações locais simples** - Reorganizar dados, validações, formatações
2. **Integrações com limite de custo** - Definir orçamento máximo por execução  
3. **Workflows com etapas assíncronas** - Processar em background sem travar interface

🚧 **Quando evitar:**
1. **Integrações caras sem controle** - APIs que cobram por execução sem limite
2. **Workflows síncronos pesados** - Travem interface por minutos
3. **Automações sem validação** - Podem executar em loop consumindo créditos infinitamente


---

### 💡 **Ícone de Lâmpada (Sugestão/IA)**

✅ **Quando deixar ativado:**
1. **Sugestões baseadas em templates** - Respostas pré-definidas, sem consumo de IA
2. **IA com cache inteligente** - Mesma pergunta = mesma resposta do cache
3. **Modelos locais ou gratuitos** - Ollama, modelos próprios

🚧 **Quando evitar:**
1. **IA premium sem controle** - GPT-4, Claude sem limite de uso
2. **Sugestões em tempo real** - Cada clique/movimento gasta créditos
3. **Contexto muito longo** - Textos grandes custam mais tokens

***
