# Changelog da v02 - Aulixiar:

# Nome: "changelog-v02-auxiliar.md"

---

# v2 - Controle de Pedidos - Descrições e Log de Evolução - v2:

===---+++---===
===---+++---===

***

## [OBS] Relação de TAGS em uso:
```
[ANEXO] [STATUS] [EXEC] [CORRECAO] [PERG] [RESP] [OBS] [AG] [OK] [NOT OK] [SNAPSHOT] [MEMORIA]
```

***

## [STATUS] Checklist de Configuração ('[ ]' | '[OK]' | '[ANDAMENTO]' | '[PENDENTE]'):

```

## [STATUS] Checklist de Evolução do Sistema ('[ ]' | '[OK]' | '[ANDAMENTO]' | '[PENDENTE]'):
```
[ ] . Botão para "Abrir modo Lado a Lado" - "Produtos - v3"
[ ] . Botão para "Abrir modo Lado a Lado" - "Pedidos - v3"
[ ] . Botão para View de "DB Produtos - v3"
[ ] . Botão para View de "DB Pedidos - v3"
[ ] . Botão para View com Layout = Quadrado - "DB Pedidos - v3" - “Pedidos em Aberto”
[ ] . Acompanhamento de Status dos Pedidos (um geral e um para cada status).
[ ] . View “Calendário de Pedidos em Aberto”  
[ ] . View “Pedidos em Aberto”  
[ ] . View “Pedidos Encerrados”  
[ ] . View “Pedidos Em Atraso”  
[ ] . View “Pedidos por Loja” (Board)  
[ ] . View “Calendário de Entregas”  
[ ] . View “Linha do Tempo de Entregas”  
[ ] . View “Pedidos por Status” (Board)  
[ ] . View “Pedidos deste Mês”  
[ ] . View “Pedidos com Observações”  
[ ] . View “Pedidos por Ano”  
[ ] . View “Produtos Sem Imagem”  
[ ] . View “Produtos sem Link do Produto”  
[ ] . View “Produtos por Pedido” (agrupado)  
[ ] . View “Pedidos com Devolução ou Reembolso”  
[ ] . View “Pedidos com Reembolso Resolvido”  
[ ] . Filtro “Pedidos por Faixa de Data de Compra”  
[ ] . Dashboard “Visão Geral de Pedidos”
[ ] . Dashboard “Visão Geral de Produtos”  
[ ] . Testar fluxo Prático completo.


[ ] . View “Pedidos em Aberto”  
	- Objetivo: enxergar tudo o que ainda não terminou.
	- Tabela filtrada para `Status` contendo apenas `01.Aberto`, `02.Dentro do Prazo` e `04.Em Atraso`.  

[ ] . View “Pedidos Encerrados”  
	- Filtrar `Status` contendo `03.Entregue`, `05.Cancelado`, `07.Devolução Realizada`, `09.Reembolso Realizado`, `10.Resolvido`.  
	- Facilita arquivar e revisar histórico.

[ ] . View “Pedidos Em Atraso”  
	- Filtro: `Status` contém `04.Em Atraso`.  
	- Ordenar pela data “Previsão da Entrega Final após a Compra” crescente.  
	- Serve como “lista de incêndios” diária.

[ ] . View “Pedidos por Loja” (Board)  
	- Layout: Quadro (Board).  
	- Agrupar por `Loja` (AliExpress, Shopee, Amazon, etc.).  
	- Dentro de cada coluna, ordenar por data de compra decrescente.

[ ] . View “Calendário de Entregas”  
	- Layout: Calendário.  
	- Propriedade de data: usar “Previsão da Entrega Final após a Compra” (ou a que você preferir como referência).  
	- Visual ajuda a enxergar semanas muito carregadas.

[ ] . View “Linha do Tempo de Entregas”  
	- Layout: Timeline.  
	- Propriedade de data: “Entrega Prevista Inicio na Compra” → “Entrega Prevista Fim na Compra”.  
	- Mostra visualmente a janela de entrega de cada pedido.

[ ] . View “Pedidos por Status” (Board)  
	- Layout: Board.  
	- Agrupar pela propriedade `Status`.  
	- Permite arrastar cards entre colunas para atualizar status manualmente.

[ ] . View “Pedidos deste Mês”  
	- Filtro: `Compra Feita em` está dentro do mês atual.  
	- Ordenação: `Compra Feita em` decrescente.  
	- Dá um “extrato” mensal das compras.

[ ] . View “Pedidos com Observações”  
	- Filtro: `Observações` não está vazia.  
	- Ajuda a revisitar pedidos com problemas ou anotações especiais.

[ ] . View “Pedidos por Ano”  
 	- Propriedade extra (Number ou Formula) para extrair o ano de `Compra Feita em` (ex.: `year(prop("Compra Feita em"))`).
 	- Agrupar por essa propriedade “Ano da Compra”.

[ ] . View “Produtos Sem Imagem”  
 	- Filtro: `Imagem` está vazia.  
 	- Para decidir se vale a pena adicionar fotos.

[ ] . View “Produtos sem Link do Produto”  
 	- Filtro: `Link do Produto` está vazio.  
 	- Ajuda a completar links faltantes para consulta futura.

[ ] . View “Produtos por Pedido” (agrupado)  
 	- Agrupar os produtos por relation `Tabela Pedido Origem`.  
 	- Mostra blocos de produtos conforme cada pedido.

[ ] . Dashboard “Visão Geral de Pedidos” (página separada)  
 	- Criar uma página “Painel – Pedidos”.  
 	- Inserir ali linked databases de DB Pedidos com views: Em Aberto, Em Atraso, Encerrados. [notion](https://www.notion.com/help/views-filters-and-sorts)

[ ] . Dashboard “Visão Geral de Produtos”  
 	- Página com linked database de DB Produtos.  
 	- Views rápidas: por Categoria, sem Link, com Observações.

[ ] . Filtro “Pedidos por Faixa de Data de Compra”  
 	- Criar view em Pedidos com filtro avançado (data entre duas datas), para analisar períodos específicos (ex.: Black Friday).

[ ] . View “Pedidos com Devolução ou Reembolso”  
 	- Filtro: `Status` contém qualquer um de (`06.Devolução Solicitada`, `07.Devolução Realizada`, `08.Reembolso Solicitado`, `09.Reembolso Realizado`).  
 	- Para acompanhar problemas com vendedores.

[ ] . View “Pedidos com Reembolso Resolvido”  
 	- Filtro: `Status` contém `09.Reembolso Realizado` ou `10.Resolvido`.  
 	- Serve como histórico de casos resolvidos.

```

***
===---+++---===
===---+++---===
===---+++---===
===---+++---===
===---+++---===

## [EXEC] Utilizar do '# 📝 TEMPLATE DE SOLICITAÇÃO DE GUIA PASSO A PASSO', para ....

***
***


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
