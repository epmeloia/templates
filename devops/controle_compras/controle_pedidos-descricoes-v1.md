# Controle de Pedidos - v1:
"controle_pedidos-descricoes-v1.md"

---

## Solicitação para a IA:
	* vc consegue criar um página + templates novos + tabelas, a partir do que é exibido ao lado e as instruções a seguir e links de outros projetos de acompanhamento de pedido? (S/N).
	* Antes de Realizar qualquer coisa, após sua analise inicial, me informe o que entendeu e o que pretende fazer, que eu respondo e vamos caminhando, passo a passo para a criação de um novo modelo, preciso de etapas bem explicadas, passo a passo de bebê, não me de todos os passos de uma só vêz, apenas 3 etapas por vêz, simples e faceis de ser realizada, por uma pessoa com poucos conhecimento de Notion, aja como um professor cuidadoso e atencioso, preocupado não só com o projeto mas tambem com o aluno, iremos fazer uma jornada de conhecimento e evolução juntos.

---

## Descrição da Pagina/ABA ao lado:
	* Controle de Acompanhamento de Produtos Diversos Comprados em NOTION.

---

## O que eu Quero nesse novo Controlar de Compras:
	* Criar Campo "ID da Compra", esse é o ID, número Único, deve ser preenchido automático, Tipo  "Numérico", se um pedido for deletado o numero dele não é reutilizado nem reciclado.
	
	* Descrição das Linhas dentro do sistema atual:
		- Quando as informações estão Abaixo de "PEDIDOS:", são os itens classificados como "Aguardando".
		- 1a Linha Normalmente é o número de entrega do correio:
			. Criar Campo "Rastreio" (Ex.: "BR253202824926M") campo do tipo "Texto", numero do rastreio fornecido na compra.
			. Criar Campo "4tracking" (Ex.: "https://www.4tracking.net/pt/tjax/track?nums=BR253202824926M") campo do tipo "URL", a ideia é que o link seja criado automaticamente, a montagem deve seguir a seguinte ordem, primeiro o inicio da URL do "Site" e a segunda parte utilizando o campo "Rastreio" (Ex.: "https://www.4tracking.net/pt/tjax/track?nums=M").
		- 2a Linha Normalmente é a descrição do Produto Comprado e complementos:
			. Criar campo "Produto" (Ex.: "Cubo robot articulado | Variação: Pequeno,Azul"), tipo "Texto", mas pode ser uma tabela auxiliar, pois existe a possibilidade de ter varios Produtos em uma mesma "ID da Compra", isso deve ser previsto no processo (Ex.: "Notebook Teclado Universal Film/Laptop Silicone À Prova De Poeira Película Protetora/D'água Claro | Variação: 36.5cmX13.5cm（PS-003）ROXO,1 unidade | R$14,90").
			. A Separação quando existir é usado "|":
				.. Variações (Ex.: "Variação: Pequeno,Azul", "Variação: 36.5cmX13.5cm（PS-003）ROXO").
				.. Preço do Produto (Ex.: "R$14,90").
				.. Unidades Compradas (Ex.: "x2", "x3", "x4").
				.. Valor Total do Produto, que é a multiplicação de "Preço do Produto" vezes "Unidades Compradas" (Ex.: " = R$35,00").

		- 3a Linha Normalmente tem as datas (Ex.: "COMPRA  11/12/2025  ENTREGA  18/12/2025 a 26/12/2025"):
			. Criar campo "Data Compra" (Ex.: "COMPRA  11/12/2025"), tipo "Data".
			. Criar campo "Entrega Prevista na Compra" (Ex.: "18/12/2025"), tipo "Data".
			. Criar campo "Entrega Prevista Ate na Compra" (Ex.: "26/12/2025"), tipo "Data".

		- 4a Linha Normalmente tem as datas (Ex.: "SHOPEE  R$14,99 + FRETE R$27,88 - DESC R$20,00 = R$22,87"):
			. Criar Campo "Loja" (Ex.: "Shopee", "Amazon") campo do tipo "Seleção Multipla".
			. Criar Campo "Total Valor dos Produtos" (Ex.: "R$ 14,99") campo do tipo "Numérico" com 2 casas descimais e se possível com mascara "R$ 9999,99", é a soma dos totais de cada um dos produtos comprados.
			. Criar Campo "Frete" (Ex.: " + FRETE R$27,88") campo do tipo "Numérico" com 2 casas descimais e se possível com mascara "R$9999,99".
			. Criar Campo "Desconto" (Ex.: " - DESC R$27,88") campo do tipo "Numérico" com 2 casas descimais e se possível com mascara "R$9999,99".
			. Criar Campo "Num.Moedas" (Ex.: " - MOEDA 288  R$2,88") campo do tipo "Numérico" e se possível com mascara "999.999".
			. Criar Campo "Valor Moedas" (Ex.: " - MOEDA 2,88  R$2,88") campo do tipo "Numérico" com 2 casas descimais e se possível com mascara "R$99,99" e se possível seja calculado automaticamente dividindo o "Num.Moedas" por 100 e convertendo em Moeda.
			. Criar Campo "Link Compra" (Ex.: (https://shopee.com.br/user/purchase/order/219198030193097?type=6)) campo do tipo "URL".

		- 5a Linha Normalmente tem as datas (Ex.: "PREVISÃO  19/12/2025 a 29/12/2025"):
			. Criar campo "Entrega Prevista apos a Compra" (Ex.: "19/12/2025"), tipo "Data".
			. Criar campo "Entrega Prevista Ate apos a Compra" (Ex.: "29/12/2025"), tipo "Data".

		- 6a Linha Normalmente tem as datas (Ex.: "ENTREGUE  30/12/2025"):
			. Criar campo "Entrega Realizada" (Ex.: "30/12/2025"), tipo "Data".

	* Criar Campo "Status do Pedido" (Ex.: "Aguardando", "Entrega OK", "Atrasado", "Reembolso -  Solicitado", "Reembolso - OK") será usado para passar entre as Colunas/DIvisões.

	* Criar um Campo para Gerar o Histórico da Devolução, sempre com as mesmas informações, a serem complementados a seguir:
		- Reembolso - Solicitação		(Ex.: "Reembolso - Solicitado em: 18/12/2025")
		- Reembolso - Solicitação Valor	(Ex.: "Reembolso - Valor: R$ 58,69")
		- Devolução - Prazo Final		(Ex.: "Devolução - Prazo Final: 29/12/2025")
		- Devolução - Realizada			(Ex.: "Devolução - Realizada Data: 20/12/2025")
		- Reembolso - Prazo Final		(Ex.: "Reembolso - Prazo Final: 24/12/2025")
		- Reembolso - Realizado			(Ex.: "Reembolso - Realizada Data: 24/12/2025")
		- Reembolso - AG *2658  = *4477

```
Ex.1:
	BR253202824926M (https://www.4tracking.net/pt/tjax/track?nums=BR253202824926M)
	Cubo robot articulado | Variação: Pequeno,Azul
	**COMPRA  11/12/2025  ENTREGA  18/12/2025 a 26/12/2025
	SHOPEE  R$14,99 + FRETE R$27,88 - DESC R$20,00 = R$22,87
	(https://shopee.com.br/user/purchase/order/219198030193097?type=6)
	PREVISÃO  19/12/2025 a 29/12/2025
	# # #  EM ATRASO   # # #
	ENTREGUE  30/12/2025

Ex.2:
	BR257744651033Y (https://www.4tracking.net/pt/tjax/track?nums=BR257744651033Y)
	- Notebook Teclado Universal Film/Laptop Silicone À Prova De Poeira Película Protetora/D'água Claro | Variação: 36.5cmX13.5cm（PS-003）ROXO,1 unidade | R$14,90
	- Notebook Teclado Universal Film/Laptop Silicone À Prova De Poeira Película Protetora/D'água Claro | Variação: 36.5cmX13.5（PS-003）Transparent,1 unidade | R$14,90
	- Notebook Teclado Universal Film/Laptop Silicone À Prova De Poeira Película Protetora/D'água Claro | Variação: 36.5cmX13.5cm（PS-003）ROSA,1 unidade | R$14,90
	COMPRA  17/12/2025  ENTREGA  23/12/2025
	SHOPEE  R$44,70 + FRETE R$10,11 - DESC R$10,11 - MOEDA R$0,21 = R$44,49
	(https://shopee.com.br/user/purchase/order/219732126156112?type=6)
	PREVISÃO  26/12/2025  a 06/01/2026
	# # #  EM ATRASO   # # #
	ENTREGUE  /12/2025**

Ex.3:
	- BR256323981008X (https://www.4tracking.net/pt/tjax/track?nums=BR256323981008X)
	[Chuveiro Portátil de Camping Recarregável | Bomba Submersa 5L/min para Banho e Pets
	COMPRA  17/12/2025  ENTREGA  19/12/2025
	SHOPEE  R$58,99 + FRETE R$8,00 - DESC R$8,00 - MOEDA R$0,30 = R$58,69](https://shopee.com.br/user/purchase/order/219732126156113?type=6)
	PREVISÃO  19/12/2025
	ENTREGUE  18/12/2025
	# # #  SOLICITADO REEMBOLSO 18/12/2025  |  R$ 58,69   # # #
	# # #  DEVOLUÇÃO PEÇA NECESSÁRIA  ATÉ DIA   24/12/2025 # # #
	# # #  DEVOLUÇÃO PEÇA NECESSÁRIA  REALIZADA   19/12/2025 # # #
	# # #  AGUARDAR VALOR REEMBOLSO  24/12/2025  |  R$ 58,69   # # #
	# # #  RECEBIDO VALOR REEMBOLSO  22-18/12/2025  |  R$ 58,69   # # #
	# # #  AG REEMBOLSO  |  *2658  = *4477  # # #**


```

---

## links de Exemplos:
	* Compras [https://www.notion.so/COMPRAS-0f2c5cddda26492c9df8376598475b85]
	* Painel de encomendas de bolo  [https://notion.notion.site/Painel-de-encomendas-de-bolo-10eefdeead058137ab15d73c41ff2940]
	* Print on Demand Order Tracker [https://pentagonal-coreopsis-16a.notion.site/Print-on-Demand-Order-Tracker-2aa7e774d2df80268f64c6fedfa76a82]
	* Small shop order manager [https://www.notion.so/mall-shop-order-manager-2daf7525a6a9806ab270c3543558fbd8?pvs=36]	


---

## Regra Primordial
	* Em caso de dúvida pergunte, não tome descisões por achar que é provavel, tenha certeza.

---
