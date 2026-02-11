# Relações no Notion (1–1, 1–N, N–1) - Manual v1

# Nome: "manual-relacoes-notion-1-1-1-n-n-1-manual-v1.md"

---

**Exemplo com: `DB Origem` e `DB Destino`**

---

## 1. Conceitos básicos de relação no Notion

- Vamos usar dois bancos de dados de exemplo:

	. **DB Origem**
	. **DB Destino**


- No Notion, uma **Relação** é um tipo de propriedade ou  uma coluna que:

	. Liga **linhas de um banco** a **páginas de outro banco** (ou do mesmo).

	. Tem dois opções/controles principais:

		1. **Limite**

			> `Sem limite` → a célula pode ter **várias páginas ligadas**.
			> `1 página` → a célula aceita **apenas 1 página ligada**.


		2. **Relação bidirecional**

			. **Desligado** → a ligação aparece **apenas em um lado**.

			. **Ligado** → o Notion cria **automaticamente a coluna “espelho”** no outro banco.


- Com isso, conseguimos montar:

	. Relação **1 → N**
	. Relação **N → 1**
	. Relação **1 ↔ 1 (controlada)**


- Obs.: Sempre usando **DB Origem** e **DB Destino** como exemplo.**


---

## 2. Preparar os bancos de exemplo (DB Origem e DB Destino)

### 2.1 Criar o DB Origem

1. Vá até a página onde você quer criar os bancos de testes.
2. Digite `/tabela` e escolha **“Tabela – base de dados em linha”** (ou equivalente em português).
3. Clique no nome da tabela (por exemplo “Tabela sem título”) e renomeie para:
   **`DB Origem`**.
4. Deixe pelo menos a coluna **Nome** (tipo Título). Se quiser, apague as outras colunas padrão.


### 2.2 Criar o DB Destino

1. Abaixo ou ao lado, digite `/tabela` novamente e crie outra **tabela – base de dados em linha**.
2. Renomeie essa segunda tabela para:
   **`DB Destino`**.
3. Também deixe pelo menos a coluna **Nome**.


- Pronto: agora temos dois bancos simples para usar como laboratório:

	. **DB Origem**
	. **DB Destino**


---

## 3. Relação 1 → N (Um em Origem, vários em Destino)

- **(Um registro em Origem é ligado a vários em Destino)**


### Exemplo tipico: **um Cliente** (Origem) com **varios Pedidos** (Destino).

- Vamos considerar:
	. **DB Origem** = “Categorias”
	. **DB Destino** = “Itens”

- Uma Categoria pode ter vários Itens.


### 3.1 O que significa 1 → N aqui

- **1 registro em DB Origem** pode se relacionar com **vários registros em DB Destino**.

- **Cada registro em DB Destino** pode estar ligado a **apenas 1 Origem**, dependendo de como você configurar o limite.


### 3.2 Como criar relação 1 → N (Origem 1, Destino N)

Vamos configurar **DB Origem** com limite 1, e aceitar múltiplos no Destino.

1. Na tabela **DB Origem**, clique em **“+”** ao lado da ultima coluna.
2. Escolha **“Propriedade de base de dados” → “Relacao”**.
3. Em **“Relacionado a”**, selecione **`DB Destino`**.
4. Em **“Limite”**, escolha **`1 página`**.

	. Isso significa: cada linha de **DB Origem** só pode apontar para **uma página de DB Destino** naquela coluna.


5. Em **“Relação bidirecional”**, deixe **Ligado**.

	. O Notion criará automaticamente, em **DB Destino**, uma coluna espelho (por exemplo: `DB Origem`).


6. Clique em **“Adicionar relação”**.


### 3.3 Resultado prático

- Em **DB Origem**:

	. Coluna de relação (por exemplo, `DB Destino`) → **Limite = 1 página**.


- Em **DB Destino**:

	. Coluna espelho (por exemplo, `DB Origem`) → por padrão aceita **várias páginas** (sem limite).


- **Na prática**:

	. **Visto de DB Origem → DB Destino**:

		> Cada linha enxerga **apenas 1 ligado**.
		> Cada linha de **Origem** = no máximo **1 Destino**.

	
	. **Visto de DB Destino → DB Origem**:

		> Uma linha pode aparecer ligada a **N registros** de Origem.
		> Cada linha de **Destino** = pode aparecer ligada a **N linhas de Origem**.

- Isso é uma relação **1 → N**, olhando do lado do **Origem**.

- Isso é uma relação **N → 1**, olhando do lado do **Destino**.


- Obs.:
  . Se quiser o contrario (N → 1), basta inverter quem tem o “Limite = 1 pagina” (Descrito a seguir veja a próxima seção).


---

## 4. Relação N → 1 (varios em Origem, um em Destino)

- **(Vários em Origem ligados a um único Destino)**


### 4.1 O que significa N → 1 aqui

-  **Vários registros em DB Origem** podem apontar para **um registro em DB Destino**.

-  Usando o exemplo clássico:

  . **DB Origem** = “Pedidos”
  . **DB Destino** = “Clientes”
  . Vários Pedidos podem ser de **um único Cliente**.
  . O mecanismo e o mesmo, mas você controla o “1” e o “N” escolhendo **onde** coloca o “Limite = 1 pagina”.


### 4.2 Como criar relação lado "1" (Destino 1)

- Agora vamos configurar a relação a partir do **DB Destino**, com limite 1 do lado do Destino.

1. Na tabela **DB Destino**, clique em **“+”** à direita da última coluna.
2. Escolha **“Relação”** como tipo.
3. Em **“Relacionado a”**, selecione **`DB Origem`**.
4. Em **“Limite”**, escolha:

   . **`1 página`**
		> Isso significa: uma linha em **DB Destino** só pode apontar para **1 registro de DB Origem** naquela coluna.

5. Ative **“Relação bidirecional”** (Ligado).
6. Clique em **“Adicionar relação”**.


### 4.3 Resultado prático

- Em **DB Destino**:

	. Coluna de relação (por exemplo, `DB Origem`) → **Limite = 1 página**.

- Em **DB Origem**:

	 . Coluna espelho (por exemplo, `DB Destino`) → aceita **várias páginas ligadas** (sem limite).

- Visto do **Origem** para o **Destino**: **N → 1**.

- Vários registros em **DB Origem** podem apontar para o **mesmo registro em DB Destino**.

- Isso é a relação **N → 1**, vista do lado do **Origem** em direção ao Destino.


---

## 5. Relação 1 ↔ 1 (um para um nos dois lados)

### 5.1 Limitação do Notion

- O Notion **não tem um “bloqueio ou trava" rígido** de 1–para–1 nos dois lados** apenas com a propriedade Relação, ele não impede que você ligue dois registros de Origem para o mesmo Destino.

- Você consegue dizer:

	. “Neste lado, só quero **1 página** ligada” (Limite = 1 página).

	. Mas o outro lado continua sendo uma **lista de páginas ligadas**, e o Notion **não impede** que mais de um registro se ligue ao mesmo item.


- Então, para simular **1 ↔ 1**, precisamos de:

  a. Limite = 1 página de um lado.

  b. Um mecanismo de **monitoramento** do outro lado (rollup + alerta), para garantir que não haja mais de 1 ligado.


### 5.2 Como chegar o mais perto possível de 1 ↔ 1

- Vamos supor:

	. **DB Origem** ↔ **DB Destino**
	. Queremos **1 Origem para 1 Destino** e **1 Destino para 1 Origem**, na prática.


#### Passo 1 – Criar relação com limite 1

1. Em **DB Origem**, crie uma relação com **DB Destino**, como na seção 3.2:

	. Tipo: Relação
	. Relacionado a: `DB Destino`
	. Limite: **`1 página`**
	. Relação bidirecional: **Ligado**

- Obs.: Isso já garante que **cada Origem só pode apontar para 1 Destino** naquela coluna.


#### Passo 2 – Criar um Rollup no DB Destino

- Agora vamos controlar quantos registros de Origem estão ligados a cada Destino.

1. Em **DB Destino**, clique em **“+”** para adicionar uma nova propriedade.
2. Escolha **“Rollup”** como tipo.
3. Configure o rollup assim:

	a. **Relacionamento**: selecione a relação que aponta para o **DB Origem** (por exemplo, `DB Origem`).
	b. **Propriedade**: escolha uma coluna simples do DB Origem, como `Nome`.
	c. **Cálculo**: selecione **“Contagem”** (Count).

4. Renomeie essa coluna para:
	. **`Qtd Origem`**.

- Obs.: Agora, para cada linha de **DB Destino**, você enxerga quantos registros de **DB Origem** estão ligados a ela.


#### Passo 3 – Criar um alerta com fórmula (Opcional, mas recomendado)

1. Em **DB Destino**, crie mais uma coluna, tipo **Fórmula**.
2. Edite a fórmula para algo como:

```notion
if(prop("Qtd Origem") > 1, "⚠ Mais de 1 Origem ligada", "")
```

- Se **Qtd Origem > 1**, aparece um aviso.
- Se for **0 ou 1**, fica vazio (sem alerta).
- Quando aparecer “⚠ Mais de 1 ligado”, você sabe que **quebrou a regra 1-para-1** e pode corrigir manualmente.


### 5.3 O que isso significa na prática:

- O Notion **nao faz bloqueio automatico** de 1-para-1 nos dois lados.
- Você continua com a limitação “1 página” do lado de **DB Origem**.
- Do lado de **DB Destino**, você tem um **indicador visual** sempre que houver mais de 1 Origem ligada, o que te permite manter 1 ↔ 1 na prática.
- Tecnicamente, o Notion continua permitindo que mais de um Origem se ligue ao mesmo Destino, mas você consegue **controlar e monitorar** com essa combinação de:

	. **`Limite = 1 página` em um lado
	. **Rollup de contagem + (opcional) Formula de alerta no outro lado. ([1])
	. **Rollup + fórmula de alerta** do outro,

- Você consegue **monitorar e corrigir** qualquer quebra da regra 1–para–1 rapidamente.


---

## 6. Onde você escolhe 1-1, 1-N ou N-1 na pratica

Usando **DB Origem** e **DB Destino**:

* **1 → N (Origem 1, Destino N)**

  * Cria a relação em **DB Origem**.
  * `Limite = 1 página` em DB Origem.
  * Lado Destino vira lista (N itens podem apontar pra ele).


* **N → 1 (Origem N, Destino 1)**

  * Cria a relação em **DB Destino**.
  * `Limite = 1 página` em DB Destino.
  * Lado Origem vira lista (N itens podem apontar pra esse Destino).


* **1 ↔ 1 (controlado)**

  * `Limite = 1 página` em um dos lados.
  * Rollup + fórmula no outro lado para mostrar quando mais de 1 registro estiver ligado.
  * Você garante 1–para–1 monitorando o alerta.


---

## 7. Exemplos práticos com valores em `DB Origem` e `DB Destino`

> **Objetivo desta seção**
> Testar, na prática, como as relações se comportam:
>
> * Vários registros ligados a um único
> * Um registro ligado a vários
> * Simulação de 1 ↔ 1 com alerta

Vou assumir que:

* Você já tem **DB Origem** e **DB Destino** criados, conforme o manual.
* Sabe criar uma **relação** entre eles (como explicado nas seções anteriores).

Se quiser, pode limpar o conteúdo de teste antes de começar (apagar linhas, manter só a estrutura).

---

### 7.1 Cenário 1 – Vários registros de Origem ligados a um único Destino (N → 1)

> Exemplo mental:
> **DB Origem** = Pedidos
> **DB Destino** = Clientes
> Vários pedidos podem ser do mesmo cliente.

#### 7.1.1 Preparar as colunas

1. Em **DB Origem**:

   * Garanta que existe pelo menos a coluna **Nome** (pode ser: `Pedido A`, `Pedido B`, etc.).
2. Em **DB Destino**:

   * Garanta que existe pelo menos a coluna **Nome** (pode ser: `Cliente 1`, `Cliente 2`, etc.).

#### 7.1.2 Criar a relação N → 1

Neste cenário, **vários Origem apontam para um Destino**, então a relação com **limite 1** deve ficar em **DB Origem**:

1. Em **DB Origem**, clique em **“+ Adicionar propriedade”**.
2. Escolha o tipo **Relação**.
3. Em **“Relacionado a”**, selecione **`DB Destino`**.
4. Em **“Limite”**, selecione **`1 página`**.
5. Ative **“Relação bidirecional”**.
6. Clique em **“Adicionar relação”**.

Resultado esperado:

* Em **DB Origem**, aparece uma coluna (por exemplo `DB Destino`).
* Em **DB Destino**, aparece a coluna espelho (por exemplo `DB Origem`).

#### 7.1.3 Popular com valores de exemplo

1. Em **DB Destino**, crie 2 linhas:

   * Linha 1: `Cliente 1`
   * Linha 2: `Cliente 2`
2. Em **DB Origem**, crie 3 linhas:

   * Linha 1: `Pedido A`
   * Linha 2: `Pedido B`
   * Linha 3: `Pedido C`

Agora vamos ligar:

3. Na coluna de relação em **DB Origem** (ex.: `DB Destino`):

   * Para `Pedido A` → selecione `Cliente 1`
   * Para `Pedido B` → selecione `Cliente 1`
   * Para `Pedido C` → selecione `Cliente 2`

#### 7.1.4 O que observar

* Em **DB Origem**:

  * Cada pedido tem **apenas 1 cliente** (por causa do “Limite = 1 página”).
* Em **DB Destino**:

  * `Cliente 1` mostra **2 registros ligados** (`Pedido A`, `Pedido B`).
  * `Cliente 2` mostra **1 registro ligado** (`Pedido C`).

👉 Isso é um exemplo claro de **N → 1 (vários Origem para um Destino)**.

---

### 7.2 Cenário 2 – Um registro de Origem ligado a vários de Destino (1 → N)

- Exemplo mental:
	. **DB Origem** = Curso
	. **DB Destino** = Aulas
	. Um curso pode ter várias aulas.

- Aqui queremos o inverso: **um Origem** apontando para **vários Destino**.


#### 7.2.1 Ajustar a relação para 1 → N

- Você pode usar os mesmos bancos como laboratório ou criar outros.

- Para ficar bem separado, faça assim:
	
	1. Se já existe uma relação anterior que não quer usar, crie uma **nova relação** em **DB Origem** com outro nome, por exemplo `Aulas (Destinos)`.
	2. Em **DB Origem**, clique em **“+ Adicionar propriedade”**.
	3. Tipo: **Relação**.
	4. **Relacionado a**: `DB Destino`.
	5. Em **“Limite”**, selecione **`Sem limite`**.
	6. Ative **“Relação bidirecional”**.
	7. Clique em **“Adicionar relação”**.

- Agora, **um registro em DB Origem** poderá escolher **várias páginas de DB Destino** nessa nova coluna.


#### 7.2.2 Popular com valores de exemplo

- Vamos imaginar:

	.Em **DB Origem**:
		.. Linha 1: `Curso Notion`

. Em **DB Destino**:

	. Linha 1: `Aula 1 – Introdução`
	. Linha 2: `Aula 2 – Bancos de dados`
	. Linha 3: `Aula 3 – Relações`


- Agora ligue:

	1. Na coluna `Aulas (Destinos)` em **DB Origem**, na linha `Curso Notion`:

		. Selecione `Aula 1 – Introdução`
		. Selecione `Aula 2 – Bancos de dados`
		. Selecione `Aula 3 – Relações`


#### 7.2.3 O que observar

- Em **DB Origem**:

	. `Curso Notion` mostra **várias aulas ligadas** na coluna `Aulas (Destinos)`.

- Em **DB Destino** (coluna espelho):

	. Cada aula terá a referência de qual curso está ligada (se a relação bidirecional estiver ativa).


- 👉 Aqui você está vendo um exemplo funcional de **1 → N (um Origem ligado a vários Destino)**.


---

### 7.3 Cenário 3 – Simulação de 1 ↔ 1 com alerta

- Objetivo:
	. Garantir, na prática, que cada linha de **DB Origem** esteja ligada a **apenas 1 Destino**,
	. e que cada Destino seja usado por **no máximo 1 Origem**, com aviso quando quebrar essa regra.


#### 7.3.1 Partindo da relação com limite 1 em DB Origem

- Use uma relação já existente ou crie uma nova com:

	. Em **DB Origem**:

	. Propriedade de relação com **`Limite = 1 página`** para `DB Destino`.

- Em **DB Destino**:

	. Coluna espelho criada automaticamente pelo Notion.

- Isso já garante:

	. **Do lado de DB Origem**: cada linha só aponta para **1 Destino**.

- Agora vamos cuidar do outro lado.


#### 7.3.2 Criar o rollup de contagem em DB Destino

1. Em **DB Destino**, clique em **“+ Adicionar propriedade”**.
2. Tipo: **Rollup**.
3. No campo **Relacionamento**, selecione a relação que aponta para **DB Origem** (por exemplo `DB Origem`).
4. No campo **Propriedade**, selecione uma coluna simples de DB Origem, como `Nome`.
5. No campo **Cálculo**, selecione **“Contagem” / “Count”**.
6. Renomeie essa coluna para:
   **`Qtd Origem`**.


- Agora, para cada linha de **DB Destino**, você vê **quantos registros de DB Origem** estão ligados.


#### 7.3.3 Criar a coluna de alerta

1. Ainda em **DB Destino**, adicione outra propriedade:

	. Tipo: **Fórmula**.

2. Clique para editar a fórmula e use algo como:

```notion
if(prop("Qtd Origem") > 1, "⚠ Mais de 1 Origem ligada", "")
```

3. Renomeie essa coluna para:
	. **`Alerta relação`** (ou nome similar).

#### 7.3.4 Mini-roteiro de teste prático

- Agora vamos **forçar um erro de 1 ↔ 1 de propósito**, para ver o alerta funcionando.

1. Em **DB Origem**, crie 3 linhas:

	. `Origem A`
	. `Origem B`
	. `Origem C`


2. Em **DB Destino**, crie 2 linhas:

	. `Destino X`
	. `Destino Y`


3. Em **DB Origem**, na coluna de relação:

	. `Origem A` → selecione `Destino X`
	. `Origem B` → selecione `Destino X` (sim, igual ao A, isso é de propósito)
	. `Origem C` → selecione `Destino Y`


4. Agora, vá para **DB Destino** e observe:

	. Na coluna **`Qtd Origem`**:

		.. `Destino X` deve mostrar **2**
		.. `Destino Y` deve mostrar **1**


	. Na coluna **`Alerta relação`**:

		.. `Destino X` deve exibir: `⚠ Mais de 1 Origem ligada`
		.. `Destino Y` deve ficar em branco (sem alerta).


- 👉 Isso mostra, claramente:

	. Que a regra 1 ↔ 1 foi **quebrada** em `Destino X` (2 origens ligadas).
	. Que a combinação **Limite 1 em DB Origem + Rollup + Fórmula em DB Destino** permite **monitorar e corrigir** os casos de violação manualmente.


---

## 8. Referencias confiaveis (para consulta)

Se quiser se aprofundar:

* Guia oficial (em ingles) sobre **Relations & Rollups**. ([classroom contemporary physicists][1])
* Detalhes tecnicos das propriedades de **relation** e **rollup** na documentacao da API do Notion (tambem em ingles, mas util para entender os limites). ([Notion Docs][2])

[1]: https://classroom-physicists.physics.mcgill.ca/documentation/notes/quick-guide-to-using-notion/relations-rollups?utm_source=chatgpt.com "Relations & rollups"

[2]: https://developers.notion.com/reference/property-object?utm_source=chatgpt.com "Data source properties - Notion Docs"



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
