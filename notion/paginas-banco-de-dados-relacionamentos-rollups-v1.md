# 📖 Paginas e Banco de Dados - Relacionamentos e Rollups - v1:

# Nome: "paginas-banco-de-dados-relacionamentos-rollups-v1.md"


---

## 📋 ÍNDICE

1. [Introdução](#introdução)
2. [Conceitos Fundamentais](#conceitos-fundamentais)
3. [Tipos de Relacionamentos](#tipos-de-relacionamentos)
4. [Criando Relacionamentos](#criando-relacionamentos)
5. [Rollups: O que são e para que servem](#rollups-o-que-são-e-para-que-servem)
6. [Criando Rollups](#criando-rollups)
7. [Casos de Uso Práticos](#casos-de-uso-práticos)
8. [Troubleshooting](#troubleshooting)


---

## 🎯 INTRODUÇÃO

Este manual ensina de forma definitiva e completa como trabalhar com **Relacionamentos** e **Rollups** no Notion. São recursos poderosos que permitem conectar informações entre diferentes bancos de dados e extrair dados agregados automaticamente.

**O que você vai aprender:**
- ✅ Criar relacionamentos entre bancos de dados
- ✅ Entender relacionamentos bidirecionais
- ✅ Configurar limites de relação (1:1, 1:N, N:N)
- ✅ Criar rollups para agregar dados
- ✅ Usar rollups em múltiplos níveis (encadeados)


---

## 🧩 CONCEITOS FUNDAMENTAIS

### O que é um Relacionamento?

Um **relacionamento** no Notion é uma propriedade que conecta páginas de um banco de dados a páginas de outro banco de dados (ou do mesmo banco).

**Analogia:** É como ter um "link" entre duas tabelas do Excel, mas muito mais poderoso.

**Exemplo prático:**
- Banco **Projetos** pode estar relacionado com banco **Clientes**
- Banco **Tarefas** pode estar relacionado com banco **Projetos**
- Banco **Pedidos** pode estar relacionado com banco **Produtos**

### O que é um Rollup?

Um **rollup** é uma propriedade que "puxa" e **agrega** dados de um banco relacionado.

**Analogia:** É como uma fórmula de SOMASE ou CONT.SE no Excel, mas automática.

**Exemplo prático:**
- Em **Projetos**, mostrar quantas **Tarefas** cada projeto tem
- Em **Clientes**, mostrar o **Total de Vendas** daquele cliente
- Em **Autores**, listar todos os **Livros** que escreveram


---

## 🔗 TIPOS DE RELACIONAMENTOS

### 1. Relacionamento 1:1 (Um para Um)

Cada página de um banco está conectada a **no máximo** uma página do outro banco.

**Exemplo:**
- **Banco:** Funcionários ↔ Computadores
- **Regra:** Cada funcionário tem 1 computador, cada computador pertence a 1 funcionário

**Como configurar:**
- Ao criar a relação, definir **Limite = 1 página** em AMBOS os lados

### 2. Relacionamento 1:N (Um para Muitos)

Uma página de um banco pode estar conectada a **várias** páginas do outro banco, mas cada página do segundo banco só pode estar conectada a **uma** página do primeiro.

**Exemplo:**
- **Banco:** Autores ↔ Livros
- **Regra:** 1 autor pode ter vários livros, mas 1 livro tem apenas 1 autor

**Como configurar:**
- Lado **Autores**: Sem limite (ou limite alto)
- Lado **Livros**: Limite = 1 página

### 3. Relacionamento N:N (Muitos para Muitos)

Qualquer página pode estar conectada a **várias** páginas em ambos os lados.

**Exemplo:**
- **Banco:** Alunos ↔ Cursos
- **Regra:** 1 aluno pode estar em vários cursos, 1 curso tem vários alunos

**Como configurar:**
- Ambos os lados: Sem limite (ou limite alto)


---

## 📖 CRIANDO RELACIONAMENTOS

### CONTEXTO

Vamos criar um relacionamento entre dois bancos de dados:
- **BD Projetos** (banco origem)
- **BD Tarefas** (banco destino)

**Objetivo:** Conectar cada tarefa ao projeto que ela pertence (relacionamento 1:N).


---

### ETAPA 1: Criar os Bancos de Dados (se ainda não existem)

**🎯 Objetivo:** Ter dois bancos de dados prontos para relacionar.

#### PASSO 1.1 - Criar BD Projetos

**1.1.1 - Criar nova página:**
- Em qualquer local do Notion, pressione `Enter` para criar uma linha vazia
- Digite `/table` ou `/tabela`
- Selecione: **"Base de dados - in-line"**

**1.1.2 - Nomear o banco:**
- Clique no título do banco
- Digite: `BD Projetos`
- Pressione `Enter`

**1.1.3 - Criar campos básicos:**
- O banco já vem com a coluna **"Nome"**
- Renomeie para: `Nome do Projeto`
- Adicione alguns exemplos:
  - Website Novo
  - App Mobile
  - Campanha Marketing


#### PASSO 1.2 - Criar BD Tarefas

**1.2.1 - Criar nova página:**
- Abaixo do BD Projetos, pressione `Enter`
- Digite `/table` ou `/tabela`
- Selecione: **"Base de dados - in-line"**

**1.2.2 - Nomear o banco:**
- Clique no título do banco
- Digite: `BD Tarefas`
- Pressione `Enter`

**1.2.3 - Criar campos básicos:**
- Renomeie a coluna "Nome" para: `Nome da Tarefa`
- Adicione alguns exemplos:
  - Criar wireframe
  - Desenvolver homepage
  - Testar responsividade
  - Escrever copy
  - Criar anúncios

**✅ Resultado esperado:**
- Dois bancos de dados criados
- BD Projetos com 3 projetos de exemplo
- BD Tarefas com 5 tarefas de exemplo


---

### ETAPA 2: Criar o Relacionamento

**🎯 Objetivo:** Conectar BD Tarefas ao BD Projetos (cada tarefa pertence a um projeto).

#### PASSO 2.1 - Adicionar propriedade de relação

**2.1.1 - Abrir BD Tarefas:**
- Clique no título **"BD Tarefas"** para focar nele

**2.1.2 - Adicionar nova propriedade:**
- À direita das colunas existentes, clique em: **"+ Adicionar propriedade"**

**2.1.3 - Escolher tipo Relação:**
- No menu que abrir, procure: **"Relação"** (ícone com duas setas ↔️)
- Clique em **"Relação"**


#### PASSO 2.2 - Configurar a relação

**2.2.1 - Selecionar banco de destino:**
- Uma janela será exibida com o título: **"Relacionar com..."**
- Na lista de bancos disponíveis, procure: **BD Projetos**
- Clique em **BD Projetos**

**2.2.2 - Ativar relação bidirecional:**
- Na mesma janela, procure o toggle: **"Mostrar em BD Projetos"** ou **"Show on BD Projetos"**
- **Ative** esse toggle (deixe azul/marcado)
- Isso criará automaticamente uma coluna espelho no BD Projetos

**2.2.3 - Nomear a relação no BD Tarefas:**
- No campo **"Nome da propriedade"** (para BD Tarefas), digite:

```
Projeto Relacionado
```

**2.2.4 - Nomear a relação espelho no BD Projetos:**
- Logo abaixo, no campo para BD Projetos, digite:

```
Tarefas do Projeto
```

**2.2.5 - Definir limite (opcional):**
- Abaixo dos nomes, você verá: **"Limitar a [X] páginas"**
- Para este exemplo (1 tarefa = 1 projeto), defina:
  - **Limite = 1 página** no lado de BD Tarefas
- Deixe **sem limite** no lado de BD Projetos (um projeto pode ter várias tarefas)

**2.2.6 - Finalizar:**
- Clique no botão azul: **"Adicionar relação"** ou **"Add relation"**

**✅ Resultado esperado:**
- BD Tarefas agora tem a coluna: **"Projeto Relacionado"**
- BD Projetos agora tem a coluna: **"Tarefas do Projeto"**
- As colunas estão vazias (ainda não vinculamos nada)


---

### ETAPA 3: Testar o Relacionamento

**🎯 Objetivo:** Vincular tarefas aos projetos e ver a relação funcionando.

#### PASSO 3.1 - Vincular primeira tarefa

**3.1.1 - Abrir BD Tarefas:**
- Localize a primeira tarefa: **"Criar wireframe"**

**3.1.2 - Clicar na célula da relação:**
- Na linha "Criar wireframe", localize a coluna **"Projeto Relacionado"**
- Clique na **célula vazia**

**3.1.3 - Selecionar um projeto:**
- Um dropdown será exibido mostrando os projetos disponíveis:
  - Website Novo
  - App Mobile
  - Campanha Marketing
- Clique em: **Website Novo**

**3.1.4 - Confirmar o vínculo:**
- A célula agora mostra: **Website Novo**
- O vínculo foi criado! ✅


#### PASSO 3.2 - Vincular mais tarefas

Repita o processo acima para as outras tarefas:
- **"Desenvolver homepage"** → **Website Novo**
- **"Testar responsividade"** → **Website Novo**
- **"Escrever copy"** → **Campanha Marketing**
- **"Criar anúncios"** → **Campanha Marketing**


#### PASSO 3.3 - Verificar relação bidirecional

**3.3.1 - Abrir BD Projetos:**
- Role a página até o BD Projetos
- Ou clique no título **"BD Projetos"**

**3.3.2 - Ver tarefas relacionadas:**
- Na coluna **"Tarefas do Projeto"**, você verá:
  - **Website Novo**: Criar wireframe, Desenvolver homepage, Testar responsividade
  - **App Mobile**: (vazio)
  - **Campanha Marketing**: Escrever copy, Criar anúncios

**3.3.3 - Confirmar funcionamento:**
- A relação bidirecional está funcionando! ✅
- Quando você vincula no BD Tarefas, aparece automaticamente no BD Projetos

**✅ Resultado esperado:**
- Tarefas vinculadas aos projetos
- Relação bidirecional funcionando automaticamente
- Você pode clicar nos links para navegar entre páginas


---

## 📊 CRIANDO ROLLUPS

### CONTEXTO

Agora que temos o relacionamento criado, vamos criar um **Rollup** no BD Projetos para mostrar:
- **Quantas tarefas** cada projeto tem

**Rollup = Agregação automática de dados do banco relacionado**

---

### ETAPA 4: Criar Rollup Simples (Contar Tarefas)

**🎯 Objetivo:** Mostrar o número de tarefas de cada projeto automaticamente.

#### PASSO 4.1 - Adicionar propriedade Rollup

**4.1.1 - Abrir BD Projetos:**
- Localize o BD Projetos
- Clique no título ou role até ele

**4.1.2 - Adicionar nova propriedade:**
- À direita das colunas, clique em: **"+ Adicionar propriedade"**

**4.1.3 - Escolher tipo Rollup:**
- No menu, procure: **"Rollup"** (ícone com setas e gráfico 📊)
- Clique em **"Rollup"**

**4.1.4 - Nomear o rollup:**
- Digite:

```
Total de Tarefas
```

- Pressione `Enter`
- O menu fechará automaticamente


#### PASSO 4.2 - Configurar o Rollup

**4.2.1 - Abrir configurações:**
- Clique no cabeçalho da coluna **"Total de Tarefas"**
- No menu que abrir, clique em: **"Editar propriedade"**
- Um painel será aberto à esquerda com 3 campos

**4.2.2 - Configurar campo "Relação":**
- No primeiro campo **"Relação"**, clique em **"Selecionar"**
- No dropdown, selecione: **"Tarefas do Projeto"**
- (Esta é a relação que conecta Projetos → Tarefas)

**4.2.3 - Configurar campo "Propriedade":**
- No segundo campo **"Propriedade"**, clique em **"Selecionar"**
- No dropdown, selecione: **"Nome da Tarefa"** (ou qualquer propriedade das tarefas)

**4.2.4 - Configurar campo "Calcular":**
- No terceiro campo **"Calcular"**, clique no dropdown
- Selecione: **"Contagem"** ou **"Count"**

**4.2.5 - Fechar painel:**
- Clique fora do painel ou pressione `Esc`

**✅ Resultado esperado:**
- Coluna "Total de Tarefas" agora mostra:
  - **Website Novo**: 3
  - **App Mobile**: 0
  - **Campanha Marketing**: 2


---

### ETAPA 5: Criar Rollup Avançado (Listar Nomes)

**🎯 Objetivo:** Mostrar a lista de nomes das tarefas (não apenas a contagem).

#### PASSO 5.1 - Adicionar outro Rollup

**5.1.1 - No BD Projetos, adicionar nova propriedade:**
- Clique em **"+ Adicionar propriedade"**
- Selecione: **"Rollup"**
- Nomeie: `Lista de Tarefas`

#### PASSO 5.2 - Configurar o Rollup para listar

**5.2.1 - Abrir configurações:**
- Clique em **"Lista de Tarefas"** → **"Editar propriedade"**

**5.2.2 - Configurar os campos:**
- **Relação:** `Tarefas do Projeto`
- **Propriedade:** `Nome da Tarefa`
- **Calcular:** `Mostrar valores únicos` ou `Show unique values`

**5.2.3 - Fechar painel:**
- Pressione `Esc`

**✅ Resultado esperado:**
- Coluna "Lista de Tarefas" mostra os nomes:
  - **Website Novo**: Criar wireframe, Desenvolver homepage, Testar responsividade
  - **Campanha Marketing**: Escrever copy, Criar anúncios


---

### ETAPA 6: Criar Rollup em Múltiplos Níveis (Encadeado)

**🎯 Objetivo:** Criar um rollup que "pula" através de dois relacionamentos.

#### Cenário:

Vamos adicionar um terceiro banco: **BD Clientes**

**Estrutura:**
- BD Clientes ↔ BD Projetos ↔ BD Tarefas

**Objetivo:** No BD Clientes, mostrar **todas as tarefas** dos projetos daquele cliente.

#### PASSO 6.1 - Criar BD Clientes

**6.1.1 - Criar o banco:**
- Pressione `Enter` em uma linha vazia
- Digite `/table`
- Selecione: **"Base de dados - in-line"**
- Nomeie: `BD Clientes`

**6.1.2 - Adicionar exemplos:**
- Renomeie a coluna para: `Nome do Cliente`
- Adicione:
  - Empresa A
  - Empresa B

#### PASSO 6.2 - Criar relacionamento Clientes ↔ Projetos

**6.2.1 - No BD Projetos, adicionar relação:**
- Clique em **"+ Adicionar propriedade"**
- Tipo: **"Relação"**
- Relacionar com: **BD Clientes**
- Ativar bidirecional
- Nomes:
  - Em Projetos: `Cliente Responsável`
  - Em Clientes: `Projetos do Cliente`

**6.2.2 - Vincular projetos aos clientes:**
- No BD Projetos:
  - **Website Novo** → **Empresa A**
  - **App Mobile** → **Empresa A**
  - **Campanha Marketing** → **Empresa B**

#### PASSO 6.3 - Criar Rollup encadeado

**6.3.1 - No BD Clientes, adicionar Rollup:**
- Adicionar propriedade tipo: **"Rollup"**
- Nomear: `Todas as Tarefas`

**6.3.2 - Configurar:**
- **Relação:** `Projetos do Cliente`
- **Propriedade:** `Tarefas do Projeto` ← (Esta é a relação Projetos → Tarefas!)
- **Calcular:** `Mostrar valores únicos`

**✅ Resultado esperado:**
- **Empresa A** mostra: Criar wireframe, Desenvolver homepage, Testar responsividade
- **Empresa B** mostra: Escrever copy, Criar anúncios

**🎯 Explicação:** O rollup "atravessou" dois níveis:
1. Clientes → Projetos (relação direta)
2. Projetos → Tarefas (relação indireta, através da propriedade do Projeto)


---

## 💡 CASOS DE USO PRÁTICOS

### 1. Sistema de CRM

**Bancos:**
- Clientes
- Projetos
- Tarefas

**Relacionamentos:**
- Clientes ↔ Projetos (1:N)
- Projetos ↔ Tarefas (1:N)

**Rollups úteis:**
- Em Clientes: Total de projetos, Total de tarefas, Receita total
- Em Projetos: Número de tarefas, Tarefas concluídas, % de conclusão


### 2. Sistema de Inventário

**Bancos:**
- Fornecedores
- Produtos
- Pedidos

**Relacionamentos:**
- Fornecedores ↔ Produtos (1:N)
- Produtos ↔ Pedidos (N:N)

**Rollups úteis:**
- Em Fornecedores: Total de produtos fornecidos
- Em Produtos: Número de pedidos, Quantidade total vendida


### 3. Sistema Educacional

**Bancos:**
- Professores
- Cursos
- Alunos

**Relacionamentos:**
- Professores ↔ Cursos (1:N)
- Cursos ↔ Alunos (N:N)

**Rollups úteis:**
- Em Professores: Número de cursos, Total de alunos
- Em Cursos: Número de alunos matriculados


---

## ⚠️ TROUBLESHOOTING

### Problema 1: "Nenhum resultado" ao configurar Rollup

**Causa:** O rollup não encontra a relação.

**Solução:**
1. Verifique se a relação existe no banco onde você está criando o rollup
2. O rollup só "enxerga" relações que partem DIRETAMENTE daquele banco
3. Confirme que você selecionou a relação correta no campo "Relação"


### Problema 2: Rollup mostra valores duplicados

**Causa:** O cálculo não está configurado como "Valores únicos".

**Solução:**
1. Abra as configurações do rollup
2. No campo "Calcular", escolha: **"Mostrar valores únicos"**


### Problema 3: Relacionamento não aparece como bidirecional

**Causa:** Toggle "Mostrar em..." não foi ativado.

**Solução:**
1. Exclua a relação existente
2. Crie novamente
3. Ative o toggle "Mostrar em [Nome do Banco]" ao criar a relação


### Problema 4: Não consigo criar relação 1:1

**Causa:** Limites não configurados corretamente.

**Solução:**
1. Ao criar a relação, clique em "Limitar a X páginas"
2. Defina **Limite = 1** em AMBOS os lados
3. Adicione fórmula de alerta no banco para detectar violações (veja manual avançado)


### Problema 5: Rollup não atualiza automaticamente

**Causa:** Bug temporário do Notion.

**Solução:**
1. Recarregue a página (F5)
2. Se persistir, edite qualquer célula da relação para forçar atualização
3. Entre em contato com suporte do Notion se o problema continuar


---

## 📚 TIPOS DE CÁLCULOS DISPONÍVEIS NO ROLLUP

Quando você configura um Rollup, o campo "Calcular" oferece várias opções:

### Cálculos Numéricos:
- **Soma** (Sum): Soma todos os valores
- **Média** (Average): Média aritmética
- **Mediana** (Median): Valor do meio
- **Mínimo** (Min): Menor valor
- **Máximo** (Max): Maior valor
- **Intervalo** (Range): Diferença entre máximo e mínimo


### Cálculos de Contagem:
- **Contagem** (Count): Número total de itens
- **Contagem de valores** (Count values): Conta apenas células não vazias
- **Contagem de valores únicos** (Count unique values): Conta sem duplicatas
- **Contagem de valores vazios** (Count empty): Conta células vazias
- **Contagem de valores não vazios** (Count not empty): Conta células preenchidas


### Cálculos de Percentual:
- **Percentual vazio** (Percent empty)
- **Percentual não vazio** (Percent not empty)


### Outros:
- **Mostrar original** (Show original): Mostra valores como estão
- **Mostrar valores únicos** (Show unique values): Remove duplicatas
- **Mostrar todos** (Show all): Mostra todos, incluindo duplicatas


### Para Datas:
- **Data mais antiga** (Earliest date)
- **Data mais recente** (Latest date)
- **Intervalo de datas** (Date range)


### Para Checkboxes:
- **Marcar todos** (Checked): Marca se todos estão marcados
- **Desmarcar todos** (Unchecked): Marca se todos estão desmarcados
- **Percentual marcado** (Percent checked)

---

## ✅ CHECKLIST FINAL

Após seguir este manual, você deve ser capaz de:

- [ ] Criar bancos de dados no Notion
- [ ] Adicionar propriedade de Relação
- [ ] Configurar relação bidirecional
- [ ] Definir limites de relação (1:1, 1:N, N:N)
- [ ] Vincular páginas entre bancos
- [ ] Adicionar propriedade de Rollup
- [ ] Configurar Rollup básico (contagem)
- [ ] Configurar Rollup avançado (listagem)
- [ ] Criar Rollup em múltiplos níveis (encadeado)
- [ ] Resolver problemas comuns
- [ ] Escolher o tipo de cálculo adequado para cada situação


---

## 📌 CONCEITOS-CHAVE APRENDIDOS

1. **Relacionamentos** conectam páginas de diferentes bancos de dados
2. **Relacionamentos bidirecionais** criam colunas espelho automaticamente
3. **Limites** controlam quantas páginas podem ser conectadas (1:1, 1:N, N:N)
4. **Rollups** agregam e exibem dados de bancos relacionados
5. **Rollups encadeados** podem atravessar múltiplos níveis de relacionamentos
6. **Tipos de cálculo** determinam como os dados são agregados (soma, contagem, listagem, etc.)


---

## 🎓 PRÓXIMOS PASSOS

Agora que você domina Relacionamentos e Rollups, explore:
- **Fórmulas avançadas** combinadas com Rollups
- **Automações** usando relações
- **Templates** com relações pré-configuradas
- **Dashboards** usando múltiplos Rollups
- **Filtros** baseados em propriedades relacionadas


---

## 📝 NOTAS FINAIS

Este manual foi criado com base em:
- Documentação oficial do Notion
- Boas práticas da comunidade
- Testes práticos validados
- Fontes confiáveis (Notion VIP, Notinize, Red Gregory)

**Versão do Notion testada:** Desktop & Web (2026)

**Contribuições:** Sinta-se livre para sugerir melhorias ou reportar erros!


---

```
##----------####----------####----------##
##                                      ##
##   ... 🐝 Manual Definitivo Notion    ##
##                                      ##
##----------####----------####----------##

         .' '.    .' '.         ,-.
.        .   .    .   .         \ /
 .         .        .       . -{|||)<
   ' .  . ' ' .  . ' ' . . '    / \
                                `-^
##----------####----------####----------##
```

---

**FIM DO MANUAL**
