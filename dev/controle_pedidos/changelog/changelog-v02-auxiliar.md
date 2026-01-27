# Changelog da v02 - Aulixiar:

# Nome: "changelog-v02-auxiliar.md"

---

# v2 - Controle de Pedidos - Descrições e Log de Evolução - v2:

===---+++---===
===---+++---===

===---+++---===
===---+++---===


## [EXEC] Utilizar do '# 📝 TEMPLATE DE SOLICITAÇÃO DE GUIA PASSO A PASSO', para ....

# Checklist de Configuração:
## [OK] Estrutura da tabela Pedidos ✅ Concluída
## [AG] Estrutura da tabela Produtos Comprados ⏳ Em andamento
## [AG] Configurar relação Pedidos ↔ Produtos
## [AG] Criar fórmulas de cálculo
## [AG] Configurar Rollups
## [AG] Testar fluxo completo

```
[ANEXO] [STATUS] [EXEC] [CORRECAO] [PERG] [RESP] [OBS] [AG] [OK] [NOT OK] [SNAPSHOT] [MEMORIA]
```

## [SNAPSHOT] Sistema de Compras v3



***
***

## [OK] Tabela de Pedidos - Campos:
. ID Tabela Pedidos [título] = Identifica a Tabela para o Notion
. ID dos Pedidos [ID] Numeração automática sequencial
. Tabela Produtos Destino [relation] = Relação → Tabela Produtos
. Status do Pedidos: [Seleção - Ordenação Automática]
	.. 01.Aberto
	.. 02.Dentro do Prazo
	.. 03.Entregue
	.. 04.Em Atraso
	.. 05.Cancelado
	.. 06.Devolução Solicitada
	.. 07.Devolução Realizada
	.. 08.Reembolso Solicitado
	.. 09.Reembolso Realizado
	.. 10.Resolvido
. Produtos = FALTA ANALISE [Texto]
. Compra Feita em = [Data]
. Entrega Prevista Inicio na Compra = [Data]
. Entrega Prevista Fim na Compra = [Data]
. Loja = [Seleção]
	.. shopee
	.. Amazon
	.. Temu
	.. AliExpress
	.. Kabum
. Link da Compra na Loja = [URL]
. Rastreio 4tracking = [Texto]
. Link 4tracking = [Formula]
	1. Clique em "+ Adicionar propriedade" (símbolo + ao lado de "Link Compra").
	2. Escolha o tipo Fórmula.
	3. Dê o nome "Link de Rastreio 4tracking" para essa coluna.
	4. Clique no cabeçalho "Link de Rastreio 4tracking" para abrir as configurações.
	5. Clique em "Alterar tipo" (ou "Editar Propriedade").
	6. No campo "Editar Fórmula", digite: `"https://www.4tracking.net/pt/tjax/track?nums=" + prop("Rastreio 4tracking")`
. Previsão de Entrega Inicial após a Compra = [Data]
. Previsão da Entrega Final após a Compra = [Data]
. Observações = [Texto]

***

## [OK] Tabela de Produtos - Campos:
. ID Tabela Produtos [título] = Identifica a Tabela para o Notion
. ID dos Produtos [ID] Numeração automática sequencial
. Tabela Pedido Origem [relation] = Relação → Tabela Pedidos
. Nome do Produto [texto] = Nome/descrição do produto
. Variação [texto] = Variação específica do produto (ex: cor, tamanho, tipo, modelo)
. Categoria [seleção múltipla] = Categoria do Produto (Ex: Eletrônicos, Colecionáveis, Ferramentas, etc.)
. Valor Unitário [número] = Preço unitário do produto - formato: R$ 0,00
. Quantidade [número] = Quantidade de unidades compradas - formato: 0.000
. Valor Total [fórmula] = `prop("Valor Unitário") * prop("Quantidade")` - formato: R$ 0,00
. Imagem [Arquivo e mídia] = Foto/imagem do produto
. Link do Produto [url] = URL da página do produto na loja
. Observações [texto] = Notas específicas sobre o produto
. ID Tabela Pedidos [relation] = Relação com a tabela "Pedidos" - Many-to-One


***


## [CORRECAO] :

* ANTES:

```
```

* DEPOIS:

```
```

> [OBS]: 

===---+++---===
===---+++---===
===---+++---===

Solução Direta (Navalha de Occam)

===---+++---===

*
```
[ANEXO] [STATUS] [EXEC] [CORRECAO] [PERG] [RESP] [OBS] [AG] [OK] [NOT OK] [SNAPSHOT] [MEMORIA]
```
## [ANEXO] / [STATUS] / [AG] / [EXEC] / [OK] / [NOT OK] / [NOT NEC] / [OBS] / [PERG] / [RESP] / [CORRECAO]

---

```
##----------####----------####----------##
##                                      ##
##   ... 🐝 Assinatura Institucional    ##
##                                      ##
##----------####----------####----------##

         .' '.    .' '.         ,-.
.        .   .    .   .         \ /
 .         .        .       . -{|||)<
   ' .  . ' ' .  . ' ' . . '    / \
                                `-^
##----------####----------####----------##
```




