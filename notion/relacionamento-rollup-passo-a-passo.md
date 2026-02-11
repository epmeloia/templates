# Relacionamento + Rollup - Passo a Passo:

# Nome: "relacionamento-rollup-passo-a-passo.md"


---

- É possível trazer a **imagem do Produto** para o banco de **Compras**, mas você precisa que o banco de Produtos tenha uma propriedade de arquivo/imagem bem definida e usar **Relation + Rollup**.

***

## Visão geral:

- Se no banco **Produtos** você tem uma propriedade do tipo **Arquivos e mídia** (por exemplo, “Foto do Produto”), você consegue “puxar” essa imagem para a tabela **Compras** usando um **Rollup** baseado na relação que você já tem entre Compras ↔ Produtos. [relations-and-rollups]

- O resultado é uma coluna em Compras que mostra a mesma imagem cadastrada no item correspondente em Produtos.

***

## Passo a passo:

### 1. **Confirme a imagem no banco Produtos**  
   - Abra o banco **Produtos**.  
   - Garanta que exista uma coluna do tipo **Arquivos e mídia** (ex.: “Imagem”, “Foto do Produto”) e que os produtos tenham uma imagem anexada ou colada nessa coluna. [images-files-and-media]


### 2. **Veja qual é a coluna de relação em Compras**  
   - Na tabela **BD Compras**, identifique a propriedade de relação com Produtos (algo como “Relação com Produto”, “Produto”, etc.).  
   - Ela é do tipo **Relação** e aponta para o banco Produtos. [relations-and-rollups]


### 3. **Crie a coluna que puxa a imagem (Rollup)**  
   - Em **BD Compras**, clique em “+ Adicionar propriedade”.  
   - Dê o nome: por exemplo, **Imagem do Produto**.  
   - No tipo, escolha **Rollup**.  
   - Em “Relação”, selecione a relação que liga Compras → Produtos.  
   - Em “Propriedade”, escolha a coluna de imagem do banco Produtos (ex.: “Foto do Produto”).  
   - Em “Calcular”, deixe como “Mostrar original” ou equivalente, para ele apenas exibir o arquivo/imagem, sem fazer contagem. [theorganizednotebook-notion-relations-rollups]

#### Obs:
	- Pode usar a Coluna Criada Automaticamente em **DB Compras** para realizar as alterações.


### 4. **Usar no dia a dia**
   - Sempre que você escolher um Produto na linha de Compras, o Rollup “Imagem do Produto” vai mostrar automaticamente a mesma imagem cadastrada no item de Produtos.  
   - Se mudar a imagem no banco Produtos, ela atualiza em Compras também (porque está só referenciando). [createwithnotion-notion-relation-property-a-guide-on-usage]


### 5. Como deve ficar cada coluna

- Em **BD Produtos**  
  - Coluna **Imagens** → tipo: **Arquivos e mídia** (onde você já sobe as fotos).  
  - Coluna **Imagens para Compras** → tipo: **Relação**, relacionada a **BD Compras** (isso já está ok, é o espelho). [relations-and-rollups]

- Em **BD Compras**  
  - Coluna **Imagens do Produto** → precisa ser **Rollup**, não Relação. [theorganizednotebook-notion-relations-rollups]


## 6. Ajuste da coluna “Imagens do Produto” em BD Compras (quando Necessário)

1. Na tabela **BD Compras**, clique no título da coluna **Imagens do Produto**.  
2. Clique em **“Tipo”** e mude de **Relação** para **Rollup**.  
3. Nas opções do Rollup, preencha assim:  
   - **Relação:** selecione a relação que liga Compras → Produtos (provavelmente a coluna que você usa para escolher o produto, não “Imagens do Produto”).  
   - **Propriedade:** escolha **Imagens** (a coluna de arquivos/imagens lá em **BD Produtos**).  
   - **Calcular:** deixe como **Mostrar original** (ou equivalente) para exibir os próprios arquivos, não contagem ou outra agregação. [createwithnotion-notion-relation-property-a-guide-on-usage]


#### OBS:
	- Se na etapa “Propriedade” você não vê “Imagens”, confira se está selecionando a **relação correta** (a relação de produto, não a relação “Imagens para Compras”). O Rollup sempre lista as propriedades do banco relacionado que você escolher na primeira linha (“Relação”). relations-and-rollups.**

---

# [ANEXO]

[relations-and-rollups](https://www.notion.com/pt/help/relations-and-rollups)
[images-files-and-media](https://www.notion.com/pt/help/images-files-and-media)
[theorganizednotebook-notion-relations-rollups](https://theorganizednotebook.com/blogs/blog/notion-relations-rollups)
[createwithnotion-notion-relation-property-a-guide-on-usage](https://createwithnotion.com/notion-relation-property-a-guide-on-usage/)


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
