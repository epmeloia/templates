# 💡 Como Usar o Classificador de Complexidade:
"como-usar-classificador-de-complexidade-v2.md"

---
````
Classifique esta pergunta entre três níveis de complexidade:
[complexidade=baixa] [complexidade=média] [complexidade=alta]
Baseie-se em: necessidade de dados atualizados, presença de nomes específicos, benchmarking ou comparação de produtos.
```

---
# 🧠 Classificador de Complexidade:




***

### 1. Rate Limiting e Priorização de Recursos

- Implemente debounce mínimo de 500ms entre buscas, priorizando consulta local/cache antes de qualquer ação externa.
- Use throttle de 2 segundos entre execuções de workflows automatizados.
- Limite sugestões de IA a 1 por minuto por usuário.
- Sempre processe dados locais ou cache antes de requisitar à nuvem.
- Priorize indexação local para buscas rápidas sempre que possível.

***

### 2. Monitoramento e Feedback

- Antes de qualquer operação paga (API, busca avançada, integração), informe claramente ao usuário:  
  - “Esta ação consumirá X créditos.”
  - Após a execução, reporte: créditos consumidos, saldo disponível (dia/mês) e custo estimado da próxima ação.
- Exiba alerta automático ao atingir 80% de créditos utilizados no ciclo.

***

### 3. UX Responsiva e Cancelamento

- Exiba spinner e mensagem “Processando...” logo após iniciar a ação.
- Mostre barra de progresso e tempo estimado em processos longos.
- Permita cancelamento cordial das ações, protegendo integridade dos dados.
- Nunca deixe a interface sem resposta visual.

***

### 4. Estratégias Avançadas de Economia

- Sempre agrupe operações múltiplas em uma requisição única (batch).
- Comprima dados enviados para reduzir o uso de banda em até 70%.
- Adapte o modelo utilizado: GPT-3.5 para tarefas simples, GPT-4 apenas para processos complexos.
- Implemente fallback para alternativas gratuitas se APIs pagas falharem.

***

### 5. Relatórios de Consumo

- Para cada ação, registre e disponibilize ao usuário:
  - Recursos/custos consumidos até o momento.
  - Saldo disponível de créditos (dia/mês).
  - Latência e taxa de sucesso.
- Permita consulta e geração de relatório detalhado de créditos e ações recentes, incluindo previsão automática de consumo.

***

### 6. Recomendações Dinâmicas de Ícones para Economia

- **🔍 Ícone de Lupa (Busca Local/Cache):** Priorize sempre que possível.  
  Exemplo: “Ative o ícone de Lupa para evitar consumo de créditos.”
- **🔗 Ícone de Elos (Workflow):** Para operações complexas, preferencialmente agrupadas.  
  Exemplo: “Considere usar o ícone de Elos apenas se realmente necessário.”
- **💡 Ícone de Lâmpada (Sugestão/IA):** Use apenas se busca local/workflow não forem suficientes.  
  Exemplo: “Ative o ícone de Lâmpada como último recurso, pois consome mais créditos.”

**No início de cada resposta, informe qual ícone foi ativado, o motivo da escolha, e sempre proponha alternativas de menor custo operacional.**

***

### 7. Boas Práticas de Melhoria

- Priorize intervenções pontuais no exato ponto de problema.
- Analise contexto e modo de retorno; ajuste sempre na camada correta (apresentação, lógica ou estrutura).
- Preserve integridade dos dados e arquitetura; comunique claramente ao usuário a abordagem adotada.
- Corrija apenas onde necessário, garantindo robustez, reversibilidade e compatibilidade.

***

**Exemplo de resposta automática:**

> “Com base na sua solicitação, o sistema recomenda ativar o ícone 🔍 (Busca Local), por ser possível atender sem consumo externo de créditos. Caso não resolva, ative 🔗 (Workflow) e considere 💡 (IA) apenas se necessário.”

***
````
