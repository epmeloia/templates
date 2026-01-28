# Tabelas e Banco de Dados - Criar e Localizar - Guia Passo a Passo:

# Nome: "relacionar-tabelas-banco-dados-criar-localizar-guia-passo-a-passo.md"

***

## Objetivo

Criar, no **DB Pedidos - v3**, uma relação chamada **Tabela Produtos Destino** que se ligue ao **DB Produtos - v3**, e que gere automaticamente, no lado de Produtos, a propriedade reversa **Tabela Pedido Origem**, mantendo a relação many-to-many e sincronização bidirecional. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/108742584/8f23e2af-d928-4156-8bd6-1459865f67ec/image.jpg)

***

## Pré-requisitos
```
- Já existir o database **DB Pedidos - v3** configurado.  
- Já existir o database **DB Produtos - v3** configurado.  
- Ter certeza de que está trabalhando na versão correta do sistema (v3.x.x). [notion](https://www.notion.com/help/intro-to-databases)
```

***

## Passo a passo: Criar Relation Bidirecional

### 1. Abrir o DB Pedidos - v3 (lado de origem)
```
1. Navegar até a página **Pedidos - v3**.  
2. Localizar a tabela **DB Pedidos - v3** (database inline dentro dessa página). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/108742584/8f23e2af-d928-4156-8bd6-1459865f67ec/image.jpg)
3. Confirmar que está vendo as colunas já existentes (ID Tabela Pedidos, ID dos Pedidos, Status, etc.).
```

***

### 2. Criar a nova propriedade de Relation
```
1. Na última coluna da tabela, clicar em **“+”** para adicionar uma nova propriedade.  
2. No campo de nome, digitar exatamente:  
   - `Tabela Produtos Destino`  
3. No seletor de tipo de propriedade, escolher **Relation** (ícone de elos de corrente). [notion](https://www.notion.com/help/relations-and-rollups)
```

***

### 3. Escolher o database de destino (DB Produtos - v3)
```
1. Ao selecionar **Relation**, o Notion abre uma caixa para escolher o database relacionado.  
2. No campo de busca dessa caixa, digitar:  
   - `DB Produtos - v3`  
3. Selecionar o database que aparecer com esse nome (confirme pela URL/título se necessário). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/108742584/8f23e2af-d928-4156-8bd6-1459865f67ec/image.jpg)
Resultado esperado: a janela mostra algo como “Relate **DB Pedidos - v3** to **DB Produtos - v3**”. [notion](https://www.notion.com/help/relations-and-rollups)
```

***

### 4. Configurar a relação como bidirecional
```
1. Na mesma janela de configuração da relation, localizar a opção:  
   - **“Show on [DB Produtos - v3]”** (ou texto equivalente de “Mostrar no outro database”). [notion](https://www.notion.vip/insights/notion-explained-relations-rollups)
2. Certificar-se de que a caixa está **marcada** (✅).  
3. No campo de nome da propriedade reversa, digitar exatamente:  
   - `Tabela Pedido Origem`  
4. Confirmar que a pré-visualização indica:  
   - Em **DB Pedidos - v3**: propriedade `Tabela Produtos Destino`  
   - Em **DB Produtos - v3**: propriedade `Tabela Pedido Origem`. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/108742584/8f23e2af-d928-4156-8bd6-1459865f67ec/image.jpg)
```

***

### 5. Concluir a criação da relation
```
1. Clicar em **“Add relation” / “Adicionar relação”**.  
2. Aguardar o Notion aplicar a mudança.  
3. Verificar no **DB Pedidos - v3** que:  
   - A nova coluna **Tabela Produtos Destino** apareceu.  
   - O tipo da coluna é “Relation” apontando para **DB Produtos - v3**. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/108742584/8f23e2af-d928-4156-8bd6-1459865f67ec/image.jpg)
4. Abrir o **DB Produtos - v3** e conferir:  
   - Existe uma nova coluna **Tabela Pedido Origem**, criada automaticamente.  
   - O tipo é “Relation” apontando para **DB Pedidos - v3**. [notion](https://www.notion.com/help/relations-and-rollups)
```

***

### 6. Validar o comportamento many-to-many
```
**Teste mínimo recomendável:**

1. Em **DB Pedidos - v3**, criar um pedido de teste (por exemplo: “Pedido TESTE Relation 001”).  
2. Na coluna **Tabela Produtos Destino**, clicar na célula desse pedido:  
   - Clicar em **“+ Add a page”** ou **“+”**.  
   - Selecionar produtos já existentes ou criar novos produtos de teste em **DB Produtos - v3**. [notion](https://www.notion.com/help/relations-and-rollups)
3. Em **DB Produtos - v3**, abrir um dos produtos vinculados e conferir que o campo **Tabela Pedido Origem** mostra o pedido de teste.  
4. Remover a relação de um dos lados (por exemplo, tirar um produto de **Tabela Produtos Destino**):  
   - Confirmar que, no produto correspondente, o campo **Tabela Pedido Origem** é atualizado automaticamente (o vínculo desaparece ali também).  

Se tudo se comportar assim, a relation bidirecional está corretamente configurada e pronta para ser usada pelos **Rollups** (Valor Total do Pedido, Quantidade Total de Itens, Produtos Diferentes) e pelo **Teste Prático** que você descreveu. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/108742584/d24e7426-1709-492b-8857-186b4301cae6/estrutura-menu-utilizando-frase-destaque-titulo-3-alternante-guia-passo-a-passo.md)
```

***

### 7. Checklist rápido (para marcar depois da auditoria)
```
- [ ] `Tabela Produtos Destino` criada em **DB Pedidos - v3**.  
- [ ] Database de destino correto: **DB Produtos - v3**.  
- [ ] Opção “Show on DB Produtos - v3” marcada.  
- [ ] Propriedade reversa `Tabela Pedido Origem` apareceu em **DB Produtos - v3**.  
- [ ] Sincronização bidirecional testada (adicionar/remover funciona dos dois lados).  
- [ ] Relation usada com sucesso em pelo menos um rollup de teste (ex.: Sum de `Valor Total`). [theorganizednotebook](https://theorganizednotebook.com/blogs/blog/notion-relations-rollups)

Se quiser, o próximo passo pode ser transformar esse fluxo em um **bloco padrão [EXEC]** para colar direto no Notion como “procedimento oficial” de criação de relations no seu sistema.
```

***

### **Método de Localização das Collections:**

#### **Passo 1: Busca Inicial**
```yaml
Ferramenta: mcp_tool_notion-search
Query: "Sistema de Compras Painel Geral v3"
Resultado: Lista de páginas e databases encontrados
```

#### **Passo 2: Fetch da Página Container**
```yaml
Ferramenta: mcp_tool_notion-fetch
Input: ID da página "Pedidos - v3"
Resultado: Conteúdo da página em formato Markdown especial
```

**O que recebi:**
```markdown
<page url="...">
  <content>
    <database url="https://www.notion.so/2eff7525a6a9804e8ce9f94698ca9ac2" 
              data-source-url="collection://2eff7525-a6a9-8083-9b21-000b2f4b7248">
      DB Pedidos - v3
    </database>
  </content>
</page>
```

**Informações extraídas:**
```
- `url=` → URL do database (interface visual)
- `data-source-url=` → **Collection ID** (identificador interno único)
```

#### **Passo 3: Fetch do Database Completo**

```yaml
Ferramenta: mcp_tool_notion-fetch
Input: URL do database (https://www.notion.so/2eff7525a6a9804e8ce9f94698ca9ac2)
Resultado: Schema completo com TODAS as propriedades
```

**O que recebi:**
```markdown
<database url="...">
  <data-sources>
    <data-source url="collection://2eff7525-a6a9-8083-9b21-000b2f4b7248">
      <data-source-state>
        {
          "schema": {
            "ID Tabela Pedidos": { ... },
            "Status": { ... },
            // Todas as propriedades
          }
        }
      </data-source-state>
      <sqlite-table>
        CREATE TABLE ...
      </sqlite-table>
    </data-source>
  </data-sources>
</database>
```

### **Resumo Visual do Processo:**

```
📄 Página "Pedidos - v3"
   ↓ [Fetch página]
   ↓
   Encontro tag: <database data-source-url="collection://...">
   ↓
   Extraio: Collection ID
   ↓ [Fetch database]
   ↓
   Recebo: Schema completo com todas propriedades
```

### **Por que Collections são importantes?**
```
- **Imutável:** Mesmo se renomear database, Collection ID não muda
- **Único:** Identifica precisamente aquele database específico
- **Relations:** Relations usam Collection IDs para conectar databases
- **Backup:** Permite referenciar database de forma absoluta
```

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
