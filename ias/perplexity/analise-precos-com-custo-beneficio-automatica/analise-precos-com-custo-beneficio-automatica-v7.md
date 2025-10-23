# **🛒 Análise de Preços com Custo Beneficio Automática**
"analise-precos-com-custo-beneficio-automatica-v7.md"

***

**Objetivo:**  
Sistema automático para análise de custo-benefício em compras online, com análise de preços, frete, quantidades, governança e economia de recursos IA, modelo prático e didático para uso no Brasil.

***
````

# **🛒 Análise de Preços com Custo Beneficio Automática**

## 1. Checklist Inicial:
- Produto, modelo e **especificações mínimas**.
- Faixa de preço desejada.
- Quantidade/variante (se aplicável).
- Lojas BR prioritárias: KaBuM, Amazon BR, Magazine Luiza, Casas Bahia, Pichau, Terabyte, Mercado Livre (oficial).
- Exigir link direto do produto e data/hora da verificação.
- Ignorar ofertas estrangeiras, sem estoque, ou com vendedores não qualificados.

***

## 2. Governança e Economia IA:
- Priorizar busca local/cache antes de qualquer consulta externa.
- Limitar sugestões IA/web a 1 por minuto por usuário.
- Reportar créditos utilizados, saldo de créditos e custo estimado da próxima ação antes/depois de execuções pagas.
- Alerta ao atingir 80% do consumo de créditos.

***

## 3. Estrutura de Saída — Tabela de Análise:
| Loja | Produto/Modelo | Preço (R$) | Frete (R$) | Custo Total (R$) | Quantidade | Preço por Unidade/100g | Condição | Reputação da Loja | Promo/Cupom | Previsão Promo | Link |

**Observações:**  
- Informar frete/retirada otimizado, cupom disponível, condições ou promoções especiais.
- Indicar Top 3 custo-benefício.
- Destacar ofertas oficiais/melhores garantias.

***

## 4. Lógica de Custo-Benefício:
- Comparar preços considerando frete e quantidade adquirida.
- Calcular custo total e preço por unidade/100g.
- Apresentar Top 3 opções e justificar por ranking.

***

## 5. Recursos Avançados (Novos):
- **Análise automática de reputação do vendedor/loja:** Utilizar avaliações públicas, selos (“MercadoLíder”, “Loja Oficial” etc) e histórico de reclamações/reputação.
- **Alertas inteligentes:** Notificar cupom válido, promoções relâmpago, descontos combinados ou condições especiais na plataforma consultada.
- **Previsão de promoções futuras:** Sugerir datas prováveis de quedas de preço (como Black Friday, aniversários de loja, Semana do Consumidor) sempre que possível.
- **Exportação de resultados:** Capacidade de gerar a tabela em formatos como CSV, JSON ou linkdireto para integração com Excel/Google Sheets.
- **Sugestões didáticas/apoio educativo:** Inserir exemplos prontos, cenários de estudo, exercícios ou desafios para treinamentos. Incentivar divulgação em grupos de estudo e uso acadêmico.
- **Personalização de filtros e parâmetros:** Permitir ao usuário customizar faixa de preço, especificações técnicas, marcas preferidas, condição de pagamento, tempo de entrega, filtros de loja/reputação, entre outros. Possibilitar salvar/reutilizar perfis.

***

## 6. Transparência, Didática e Governança:
- Explicar qual ícone operacional foi ativado (🔍 Local, 🔗 Workflow, 💡 IA) e motivo.
- Justificar escolhas e propor sempre alternativas de menor custo de recurso.
- Informar data/hora da verificação e citar potenciais cupons, condições, diferenciais de loja.

***

## 7. Prompt Base para Uso:

> Atue como sistema avançado de comparação de compras online com governança de recursos.  
> Para os links e dados fornecidos, gere uma tabela comparativa com preço, frete, quantidade, reputação do vendedor, promoções/cupom, previsão de promoções futuras, custo total e preço por unidade.  
> Dê o ranking Top 3 custo-benefício, explique o ícone ativado, proponha alternativas mais econômicas e permita exportação da análise (CSV, JSON).  
> Informe sempre a lógica, a data/hora e inclua dicas didáticas ou exemplos aplicáveis.  
> Permita personalização de filtros conforme o perfil do usuário.

***

## 8. Para cada produto enviado:

a. **Produto e Similaridade:**
   - Título do produto
   - Verifique se é similar ao que estou buscando (ex: mesma categoria, mesmo tipo, mesmas funções)

b. **Destaques ("Indicado"/"Oficial"):**
   - Diga se aparece “Indicado” ou “Oficial” (destaque em negrito)

3. **Preço:**
   - Informe o preço exato; caso haja variação, simule a seleção do item para capturar o valor.
   - Dê preço mínimo e máximo se for kit ou possui escolha por variação.

c. **Frete:**
   - Custo do frete para São Paulo, SP
   - Diga se aparece “Frete grátis com cupom”

d. **Disponibilidade e Localidade:**
   - Informe Estoque disponível
   - Indique o local de envio (“Envio de…”), destaque vendedores de São Paulo se solicitado

e. **Descrição do Produto:**
   - Resuma os pontos principais para certificar a compatibilidade do produto com sua busca (ex: “feltro de algodão”, “compatível com massa de polir”, “função touch iPad”, etc.)

g. **Avaliações do Produto e Confiança:**  
   - Mostre a nota (ex: 4.7 de 5), total de avaliações
   - Liste a quantidade em cada bloco de estrelas conforme exibido (ex: [5 Estrela: 37], [4 Estrela: 7]…)
   - **Não sumarize comentários ainda, aguarde para implementar essa melhoria no futuro**

***

## 9. Exemplo resumido de estrutura da resposta:
```
# Produto 1:
  - Título: [Título completo]
  - Similaridade: [Sim/Não] — explicação breve
  - Destaque: Indicado/Oficial [Sim/Não]
  - Preço: [preço]
  - Frete: [frete/cupom]
  - Estoque: [disponibilidade]
  - Localidade: [Envio de...]
  - Descrição resumida: [...]
  - Avaliações: [nota] de 5.0 | [5 estrelas: xx], [4 estrelas: xx], etc.
```

***

## 10. Orientações rápidas para envio:
- **Ícone recomendado sempre: 🔍 (Busca Local), para máxima economia!**
- Envie os links dos anúncios Shopee desejados (pode ser mais de um).
- Inclua imagens quando quiser validar informações visuais ou aproximar por detalhes técnicos.
- Quando quiser priorizar vendedores de São Paulo ou outro local, informe no seu pedido.

***

## 11. Por quê essa forma é a mais **Eficiente** e utiliza as **Melhor prática:
- **Links todos juntos + prompt claro + filtro específico se necessário + tudo em uma única mensagem.**
- Isso faz com que o fluxo seja direto, rápido e comparativo, sem dispersão nem repetição.
- Permite processamento em lote, com análise paralela dos campos de cada produto.
- Evita necessidade de voltar em etapas ou refazer pedidos.
- Mantém as respostas organizadas, facilitando para você comparar os resultados rapidamente.
- Qualquer ajuste basta responder em seguida (“filtre só as Couro” ou “exclua avaliações abaixo de 4.5”).

***

## 12 Exemplos de **Passo a Passo** para envio de múltiplos produtos para análise rápida e comparativa

***

### **Exemplo 12.1**

a. **Liste os links dos produtos**
   - Copie e cole todos os links dos anúncios Shopee (ex: pulseiras para relógio Watch) em sequência, cada um na sua linha.
   - Exemplos:
     ```
     https://shopee.com.br/produto1
     https://shopee.com.br/produto2
     https://shopee.com.br/produto3
     ...
     ```
   - Se preferir, pode preceder cada link com nome resumido ou característica (“Pulseira Nylon”, “Pulseira Couro”, etc.), mas não é obrigatório.

b. **Logo após os links, envie o prompt modelo**
   - Cole ou digite o prompt sugerido anteriormente.
   - Isso ativa o fluxo para eu seguir exatamente cada campo de análise e comparar os itens.

c. **Precisa priorizar características específicas?**
   - Informe no pedido se quer filtrar por cor, material, localidade do vendedor, disponibilidade de frete grátis, ou qualquer outra característica (ex: “só de São Paulo”).
   - Isso pode ser incluído junto à lista dos links ou como instrução adicional logo após.

d. **(Opcional) Anexe imagens/telas dos produtos**
   - Se a página ou produto tem uma característica visual importante, envie imagem de tela.
   - Ajuda a identificar padrões, etiquetas (“Indicado”, “Oficial”) e detalhes que às vezes não aparecem só pelo texto.

e. **Envie tudo em uma única mensagem**
   - Links na sequência
   - Prompt logo após
   - (Opcional) imagens e instruções específicas

***

### **Exemplo 12.2**
```
https://shopee.com.br/pulseira1
https://shopee.com.br/pulseira2
https://shopee.com.br/pulseira3

[Prompt conforme modelo sugerido]

Quero comparar apenas os que enviam de São Paulo e que sejam pulseira original Watch.
```

***

### **Exemplo 12.3**

a. **Liste os links dos produtos**

```
https://shopee.com.br/produto1
https://shopee.com.br/produto2
https://shopee.com.br/produto3
https://shopee.com.br/produto4
https://shopee.com.br/produto5

[Prompt conforme modelo ou comandos adicionais]

Quero que compare apenas pulseiras originais e que estejam com frete grátis para São Paulo.
```
***

## 13 **Licença:**  
Livre para fins educacionais, profissionais e experimentais. Compartilhe e contribua com melhorias!

***
````
