# 📝 Paginas e Banco de Dados - Botão de "Acesso Rápido - v1":

Nome: "paginas-banco-de-dados-botao-de-acesso-rapido-v1.md"



---

## 📋 INFORMAÇÕES GERAIS

**Objetivo:** Criar um bloco toggle expansível com banco de dados vinculado "ACESSO RÁPIDO" do zero, sem duplicar blocos existentes. [notion](https://www.notion.so/Sistema-de-Compras-Painel-Geral-v2-2daf7525a6a9806ab270c3543558fbd8)

**Resultado esperado:** Bloco toggle funcional na coluna direita com tabela vinculada exibindo colunas Site e Link, com separador '---' no rodapé.

**Página de referência:** Sistema de Compras – Painel Geral - v2



---

## 🎯 ETAPA 1: POSICIONAMENTO E PREPARAÇÃO

### Passos:
1. Role a página até o rodapé da coluna direita
2. Clique no espaço vazio abaixo do último bloco da coluna direita
3. Aguarde o cursor aparecer

### Por quê?
- O bloco deve ser criado na posição correta (rodapé direito) desde o início
- Evita necessidade de mover o bloco depois

### Resultado esperado:
- Cursor piscando na coluna direita, abaixo do último elemento

### Troubleshooting:
- **Problema:** Cursor não aparece
  - **Solução:** Clique novamente no espaço vazio ou pressione Esc e tente novamente



---

## 🎯 ETAPA 2: Criar uma  (Frase de destaque)

### Passos:
1. Digite `/f'
2. Pressione Enter quando a opção "Frase de destaque" aparecer

Resultado esperado:
- Uma linha de título grande será criada



---

## 🎯 ETAPA 3: CRIAÇÃO DO BLOCO TOGGLE (Título 3 alternante)

### Passos:
1. Digite `/heading3` ou `/h3`
2. Pressione Enter quando a opção "Título 3 Alternante - Transformar em" aparecer

### Por quê?
- O comando `/th3` (Título 3 alternante) cria um bloco retrátil que pode expandir/colapsar
 - A espera garante que o menu de comandos carregue completamente

### Resultado esperado:
- Bloco toggle criado com cursor dentro, pronto para digitar o título

### Troubleshooting:
- **Problema:** Menu não aparece após digitar `/`
  - **Solução:** Aguarde mais 1-2 segundos ou pressione Backspace e digite `/` novamente
- **Problema:** Toggle não é criado ao pressionar Enter
  - **Solução:** Use as setas do teclado para selecionar "Toggle" no menu e pressione Enter



---

## 🎯 ETAPA 4: NOMENCLATURA DO BLOCO

### Passos:
1. Com o cursor no título do toggle "Título 3", digite: `ACESSO RÁPIDO`
2. Pressione Enter para confirmar, o texto será exibido substituído
3. O cursor move automaticamente para dentro do bloco

### Por quê?
- Nome claro identifica a versão e função do bloco
- "v4" indica que foi criado do zero (4ª iteração)

### Resultado esperado:
- Toggle com título "ACESSO RÁPIDO v4" visível
- Cursor posicionado dentro do bloco (área expansível)

### Troubleshooting:
- **Problema:** Texto sobrescreve algo existente
  - **Solução:** Pressione Ctrl+A para selecionar tudo e digite novamente



---

## 🎯 ETAPA 5: ADIÇÃO DE ÍCONE

### Passos:
1. Clique no espaço antes do texto "ACESSO RÁPIDO"
2. No menu que aparecer, selecione um ícone (ex: 🛒, 🔗, 🚀, 📊)
3. Clique no ícone escolhido

### Por quê?
- Melhora a identificação visual do bloco
- Mantém consistência com outros blocos da página

### Resultado esperado:
- Ícone exibido antes do título do toggle

### Troubleshooting:
- **Problema:** Menu de ícones não aparece
  - **Solução:** Passe o mouse sobre o toggle até aparecer o botão "⋮⋮" e clique nele



---

## 🎯 ETAPA 6: INSERÇÃO DO BANCO DE DADOS VINCULADO

Ação:
1. Clique na **seta ▶** para expandir o toggle
2. A seta mudará para **▼** e todo o conteúdo será exibido novamente
3. Dentro do toggle (área cinza que aparece), digite `/linked`
4. Selecione "Visualização vinculada da fonte de dados"
5. Na lista que aparecer, selecione a database "ACESSO RÁPIDO"

### Por quê?
- "Linked database" permite vincular um banco existente sem duplicar dados
- Mantém os dados sincronizados com a fonte original

### Resultado esperado:
- Menu de seleção de banco de dados aparece
- A tabela com todos os 15 sites e links aparecerá dentro da seção "ACESSO RÁPIDO"

### Troubleshooting:
- **Problema:** "Linked database" não aparece no menu
  - **Solução:** Digite `/linked view` ou role o menu até encontrar a opção



---

- Passe o mouse sobre o bloco "ACESSO RÁPIDO v3"
- Clique no ícone de **6 pontos (⋮⋮)** à esquerda do ícone de câmera
- O bloco inteiro ficará destacado com uma borda azul

**Comportamento:**
- Toggle que ao clicar no triângulo (▼/▶), expande/recolhe a visualização inline
- Linked database exibido inline (não abre em nova aba)
- Mostra todos os sites e links: Kabum, AliExpress, Temu, Shopee, Amazon, Shopee Baseus, Shopee Oficiais, Amazon Oficial Glade/UGREEN/RedDragon, Rastreadores, Correios, etc.



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
