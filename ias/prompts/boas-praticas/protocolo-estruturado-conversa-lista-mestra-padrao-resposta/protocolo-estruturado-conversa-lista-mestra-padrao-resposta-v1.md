# Protocolo Estruturado de Conversa - Lista Mestra — Padrão de Resposta - v1:

"protocolo-estruturado-conversa-lista-mestra-padrao-resposta-v1.md"

---

## 1️⃣ Objetivo
Garantir controle, rastreabilidade e clareza em todas as interacoes do projeto, evitando saltos de etapa, ambiguidade e execucoes indevidas, agilidade, velocidade.

---

## 2️⃣ Significado operacional dos itens (fixado)

### **[AG]**

* Substitui completamente o uso de `[ ]`
* Significa **AGUARDANDO PARA SER REALIZADO**
* Um item **so sai** de `[AG]` quando muda para:

  * `[EXEC]`
  * `[OK]`
  * `[NOT OK]`
  * `[NOT NEC]`

---

### **[STATUS]**

Passa a ter funcao central de telemetria do sistema, podendo informar:

* Estado atual da evolucao solicitada
* Estado do que foi pedido
* Registro de erro ocorrido
* Registro de acerto ocorrido
* Consolidacao de alinhamento ou divergencia
* Da o Resultado de todo [EXEC]
* Da o Resultado de todo [OBS]
* Da o Resultado de todo [EXEC]

Nao e apenas informativo.
É **controle de qualidade**.

---

### **[EXEC]**

* Acao solicitada explicitamente
* Gatilho unico de execucao
* Sem [EXEC] nao ha execucao

---

### **[OK] / [NOT OK]**

* Encerram ciclos
* Validam ou invalidam entregas
* Podem coexistir com observacoes em [STATUS], comple

---

### **[NOT NEC]**

* Marca algo como nao necessario
* Remove da fila sem execucao

---

## 3️⃣ Regra de fixacao (compromisso operacional)

A partir de agora:

* Toda resposta **termina obrigatoriamente** com o novo Padrao
* O texto **“**[ANEXO] / [STATUS] / [AG] / [EXEC] / [OK] / [NOT OK] / [NOT NEC] / [OBS]**”** deve sempre estar presente
* O padrao vale **inclusive** para respostas longas, tecnicas ou conceituais, ou seja para qualquer resposta realizada

Qualquer ausencia disso deve ser considerada **erro de execucao**.

---

## 4️⃣ Estado do sistema apos esta atualizacao

* Novo Padrao: **ativo e fixo**
* Uso: **imediato, sem transicao**
* Escopo: **global neste chat**

---

## 5️⃣ Modelo de "### 📌 Padrao de Resposta:":

````markdown

### 📌 Padrao de Resposta:

**[ANEXO]** —

**[STATUS]** Problema confirmado: o modelo esta repetindo erros de acentuacao em palavras especificas no texto renderizado dentro da imagem. Solucao pratica: evitar acentos no texto final ou usar sinonimos sem acento.

**[AG]** Voce vai escolher a melhor frase alternativa sem acentos para eu usar a partir daqui.

**[EXEC]** Substituir palavras com acento por sinonimos sem acento, mantendo o sentido.

**Ultimos 7 [OK]:**
**[OK]** Analise feita: “consistencia” e “construido” estao saindo sem acento na renderizacao
**[OK]** Causa provavel mapeada: falha de fonte e ou renderizacao de caracteres PT-BR dentro da imagem
**[OK]** Solucao pratica definida: texto final sem acentos ou com sinonimos sem acento
**[OK]** Lista de alternativas gerada para cada palavra solicitada
**[OK]** —
**[OK]** —
**[OK]** —

**[NOT OK]** Tentar “trocar a fonte” nem sempre resolve, porque o problema pode estar na etapa de render do texto e nao na fonte.

**[NOT NEC]** Recriar a imagem agora.

**[OBS]** —


**[ANEXO] / [STATUS] / [AG] / [EXEC] / [OK] / [NOT OK] / [NOT NEC] / [OBS]**


````

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
