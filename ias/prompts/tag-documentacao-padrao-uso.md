# TAG - Documentação e Padrão de Uso:

# Nome: "tag-documentacao-padrao-uso.md"

---

# Lista das TAGS:
```
- [ANEXO]
- [STATUS]
- [AG]
- [EXEC]
- [CORRECAO]
- [PERG]
- [RESP]
- [OBS]
- [OK]
- [NOT OK]
- [SNAPSHOT]
- [MEMORIA]
- [PASSO A PASSO]
- [ENTENDEU]
- [PROMPT]
```

---

## Descrições:

### **`[ANEXO]` = Indicar Arquivos ou Imagens Relacionados**

#### **Uso:**
```md
## [AG] Definir próximos passos para organizar o banco Compras
```

#### **Quando usar:**
- Quando enviar imagens, vídeos, prints ou arquivos que fazem parte do contexto.
- Quando quiser que eu considere um anexo específico na análise.
- Ao referenciar um anexo já enviado em mensagens anteriores.

#### **O que acontece:**
- Eu vou considerar o anexo como parte central da análise.
- Vou citar e interpretar o conteúdo do anexo na resposta.
- Vou relacionar o anexo com o seu sistema/fluxo/Notion, sempre que fizer sentido.  

***

### **`[STATUS]` = Pedir ou Atualizar Situação de Algo**

#### **Uso:**
```md
## [STATUS] Como está o desenho atual do Sistema de Compras v3?
```

#### **Quando usar:**
- Quando quiser um resumo do estado atual de um fluxo, página, DB ou projeto.
- Para revisar o que já foi feito e o que falta fazer.
- Ao checar se uma ideia, ajuste ou estrutura está consistente.

#### **O que acontece:**
- Eu vou fazer um resumo claro do estado atual do item pedido.
- Aponto o que está pronto, o que está em andamento e o que está pendente.
- Se fizer sentido, sugiro próximos passos para manter ou melhorar o estado atual.  

***

### **`[AG]` = Ignorar Completamente, só será Realizado com a Confirmação Explicita do Usuário.

#### **Uso:**
```md
## [AG] View de Processos em Andamento.
```

#### **Quando usar:**
- Lembretes criados por VOCÊ (usuário) sobre ações futuras
- NÃO responder
- NÃO processar
- NÃO executar

#### **O que acontece:**
- IGNORAR COMPLETAMENTE
- AGUARDAR
- IGNORAR AGORA
- GUARDAR PARA FUTURO
- SÓ SERÁ REALIZADO COM A CONFIRMAÇÃO E SOLICITAÇÃO EXPLICITA DO USUÁRIO.


***

### **`[EXEC]` = Executar Pedido de Forma Direta e Objetiva**

#### **Uso:**
```md
## [EXEC] Crie a fórmula para a coluna 'TOTAL COMPRA'
```

#### **Quando usar:**
- Quando você já sabe exatamente o que quer e só precisa da entrega.
- Para geração de fórmulas, textos prontos, blocos de Notion, estruturas, etc.
- Quando **não** quer análise longa, só a execução do pedido.

#### **O que acontece:**
- Eu vou direto ao ponto, entregando o resultado solicitado.
- Trago pequenos comentários só se forem necessários para uso correto.
- Evito explicações longas, foco na entrega prática.  

***

### **`[CORRECAO]` = Corrigir Algo Já Feito**

#### **Uso:**
```md
## [CORRECAO] Ajustar o entendimento dessa frase sobre a TAG [PASSO A PASSO]
```

#### **Quando usar:**
- Quando eu entender algo errado e você quiser alinhar.
- Para corrigir frases, fórmulas, conceitos ou regras que eu descrevi.
- Ao revisar um guia ou resposta que precisa de ajuste fino.

#### **O que acontece:**
- Eu atualizo imediatamente o entendimento conforme sua correção.
- Reescrevo o trecho afetado já no formato correto.
- Passo a usar a versão corrigida como referência nas próximas respostas.  

***

### **`[PERG]` = Fazer Pergunta Explícita**

#### **Uso:**
```md
## [PERG] Você consegue clicar na ABA ao Lado?
```

#### **Quando usar:**
- Sempre que quiser destacar claramente que aquilo é uma pergunta direta.
- Para separar perguntas de comentários/observações no mesmo bloco.
- Ao fazer séries de perguntas e querer que nenhuma seja ignorada.

#### **O que acontece:**
- Eu trato esse bloco como uma pergunta que precisa de resposta clara.
- Respondo de forma direta, objetiva e específica ao que foi perguntado.
- Se houver mais de uma `[PERG]`, respondo cada uma individualmente.  

***

### **`[RESP]` = Bloco de Resposta Direta à Pergunta/Comando**

#### **Uso:**
```md
## [RESP] (uso interno da lógica de resposta a um bloco específico)
```

#### **Quando usar:**
- Para marcar que aquele bloco é a resposta direta a uma pergunta ou tag.
- Em especial quando você quiser que uma resposta fique isolada e clara.
- Em combinação lógica com outras tags (ex.: resposta específica a `[ENTENDEU]`).

#### **O que acontece:**
- Eu estruturo a resposta de forma focada naquele bloco de contexto.
- Evito misturar com outros temas que não estejam dentro daquele pedido.
- Esse comportamento ajuda a manter rastreabilidade entre pergunta e resposta.  

***

### **`[OBS]` = Observações, Comentários e Contexto Adicional**

#### **Uso:**
```md
## [OBS] Vou criar um Item na Coluna da Direita...
```

#### **Quando usar:**
- Quando quiser dar contexto, cenários, detalhes ou comentários livres.
- Para explicar o “porquê” antes de pedir algo mais objetivo.
- Ao registrar ideias, hipóteses ou notas que não são perguntas diretas.

#### **O que acontece:**
- Eu leio esse bloco como contexto importante, mas não como um comando direto.
- Uso essas informações para ajustar o tom, o foco e o nível de detalhe da resposta.
- Se necessário, posso resumir ou reorganizar essas observações em algo mais estruturado.  

***

### **`[OK]` = Confirmar que Algo Está Certo ou Aprovado**

#### **Uso:**
```md
## [OK] É exatamente essa a ideia da documentação padrão de uso.
```

#### **Quando usar:**
- Para confirmar que uma resposta, estrutura ou entendimento está correto.
- Ao aprovar um modelo, fórmula, padrão de tag, fluxo, etc.
- Quando quiser sinalizar que podemos seguir em frente sem ajustes naquele ponto.

#### **O que acontece:**
- Eu marco internamente que aquele entendimento está validado.
- Passo a usar aquela versão como base padrão nas próximas interações.
- Não tento “corrigir” ou mudar o que já foi marcado como `[OK]`, a menos que você peça.  

***

### **`[NOT OK]` = Indicar que Algo Não Está Correto**

#### **Uso:**
```md
## [NOT OK] Essa parte do entendimento sobre a TAG não está correta.
```

#### **Quando usar:**
- Quando você não concordar com a resposta ou estrutura que eu trouxe.
- Ao apontar erros de entendimento, de lógica, de nomes ou de fluxo.

#### **O que acontece:**
- Eu entendo que NÃO preciso revisar e ajustar aquela parte, somente após explicita solicitação do Usuário.
- NÃO Refaço o trecho, tentando alinhar completamente com o que você descrever, somente após explicita solicitação do Usuário.
- NÃO Posso propor uma nova versão para você validar com `[OK]` ou nova `[CORRECAO]`, somente após explicita solicitação do Usuário.
- SEM a explicita solicitação do Usuário, deve ser totalmente ignorada.

***

### **`[SNAPSHOT]` = Documentar Estado Completo do Sistema**

*(Seu exemplo, mantido como padrão)*

#### **Uso:**
```md
## [SNAPSHOT] Documentar estado atual do Sistema de Compras v3
```

#### **Quando usar:**
- Antes de mudanças estruturais grandes.
- Após implementar features importantes.
- Semanalmente ou quando sentir necessário.
- Quando sistema estiver estável.

#### **O que acontece:**
- Eu farei análise completa de todos databases.
- Gero documentação detalhada de tudo.
- Formato: guia passo a passo para recriação completa.
- Você salva em arquivo .txt ou .md.  

***

### **`[MEMORIA]` = Registrar ou Atualizar Regras e Preferências**

#### **Uso:**
```md
## [MEMORIA] nova tag '[PASSO A PASSO]' ...
```

#### **Quando usar:**
- Quando quiser registrar uma nova regra de funcionamento, tag ou padrão.
- Para ajustar preferências de estilo, tom, forma de responder, prioridades.
- Ao criar “acordos” que devem ser lembrados nas próximas conversas.

#### **O que acontece:**
- Eu passo a considerar essa informação como parte das regras de uso.
- Ajusto meu comportamento futuro com base nesse registro.
- Uso essas memórias para manter consistência ao longo do tempo.  

***

### **`[PASSO A PASSO]` = Gerar Guia Detalhado em Etapas**

#### **Uso:**
```md
## [PASSO A PASSO] Descrever todas as TAGs criadas...
```

#### **Quando usar:**
- Quando quiser um guia detalhado, organizado, em formato de passos/seções.
- Para processos de Notion, fluxos do sistema, configurações, rotinas, etc.
- Sempre que quiser algo parecido com um “manual de instruções” bem explicadinho.

#### **O que acontece:**
- Eu aplico diretamente o **TEMPLATE DE SOLICITAÇÃO DE GUIA PASSO A PASSO**.
- Entrego um guia completo, estruturado, sem você precisar pedir `## [EXEC]`.
- Trago contexto, pré‑requisitos (se necessários), passos em ordem lógica e observações finais.  

***

### **`[ENTENDEU]` = Espelhar o que Eu Entendi do Bloco**

#### **Uso:**
```md
## [ENTENDEU] Me diga o que você entendeu dessa solicitação.
```

#### **Quando usar:**
- Quando quiser validar se eu entendi corretamente um pedido/regras/tag.
- Antes de executar algo importante, para evitar desvio de interpretação.
- Ao explicar algo mais complexo e querer que eu “espelhe” com minhas palavras.

#### **O que acontece:**
- Eu escrevo, de forma clara e direta, **o que eu entendi daquele bloco específico**.
- Esse pedido é sempre pontual e único: vale só para aquele trecho da conversa.
- A resposta correspondente funciona como um bloco de `## [RESP]` ligado a esse entendimento, até você solicitar outra vez em outro contexto.

***

---

# 📝 **TEMPLATE DE SOLICITAÇÃO DE GUIA PASSO A PASSO**

## Versão Completa (Detalhada)

```yaml
Preciso de um GUIA PASSO A PASSO COMPLETO que documente EXATAMENTE o processo que você acabou de executar para criar o [NOME DO RECURSO/FUNCIONALIDADE].

REQUISITOS DO GUIA:

1. ESTRUTURA OBRIGATÓRIA:
   - Dividir em etapas numeradas (ETAPA 1, ETAPA 2, etc.)
   - Cada etapa deve ter passos detalhados (PASSO 1.1, PASSO 1.2, etc.)
   - Incluir o "POR QUÊ" de cada etapa (justificativa/contexto)
   - Mostrar o resultado esperado ao final de cada etapa

2. NÍVEL DE DETALHAMENTO:
   - Escrever como se estivesse "pegando na minha mão"
   - Explicar cada clique, cada campo, cada ação
   - Não assumir conhecimento prévio
   - Incluir localizações visuais (ex: "no canto superior direito", "abaixo do título")
   - Mencionar ícones e elementos visuais específicos

3. CONTEÚDO ADICIONAL NECESSÁRIO:
   - Seção de "DICAS EXTRAS E BOAS PRÁTICAS"
   - Seção de "PROBLEMAS COMUNS E SOLUÇÕES"
   - Checklist final de verificação
   - Explicação dos conceitos-chave aprendidos
   - Justificativa do método escolhido (por que essa abordagem funciona)

4. FORMATO:
   - Use markdown com hierarquia clara (##, ###, etc.)
   - Inclua emojis para facilitar visualização (📌, ✅, 💡, ⚠️)
   - Use checkboxes [ ] no checklist final
   - Destaque palavras-chave em **negrito**
   - Use blocos de código quando apropriado

5. QUALIDADE EXIGIDA:
   - Não pule NENHUMA etapa ou passo
   - Seja exhaustivo e minucioso
   - O guia deve ser 100% replicável por outra pessoa
   - Escreva seu melhor trabalho, use toda sua experiência
   - O resultado deve ser no mínimo EXCEPCIONAL

CONTEXTO:
[Descreva brevemente o que foi feito, exemplo:]
Você criou um bloco toggle "ACESSO RÁPIDO" no Notion que:
- Contém um linked database da tabela "ACESSO RÁPIDO"
- Foi duplicado a partir do bloco "P&L" existente
- Tem comportamento de expandir/colapsar
- Mostra colunas "Site" e "Link"

OBJETIVO:
Criar um documento de referência que eu possa:
- Usar para replicar o processo sozinho no futuro
- Compartilhar com outras pessoas
- Adaptar para criar funcionalidades similares
- Consultar quando esquecer algum detalhe

```

***

## Regras Definitivas de TAGs**

```yaml
TAGS DE AÇÃO DIRETA (Executar imediatamente):
  [EXEC]: Executar ação agora
  [SNAPSHOT]: Gerar documentação completa
  [CORRECAO]: Aplicar correção

TAGS DE COMUNICAÇÃO (Responder):
  [PERG]: Pergunta - SEMPRE responder
  [RESP]: Minha resposta a uma [PERG]
  [OBS]: Observação contextual - apenas ler

TAGS DE STATUS/CONTEXTO (Informativo):
  [OK]: Validação positiva - apenas ler
  [STATUS]: Informação de estado - apenas ler
  [ANEXO]: Arquivo/conteúdo anexado - processar

TAGS DE LEMBRETES PARA O USUÁRIO (IGNORAR):
  [AG]: AGUARDAR - NÃO processar
  [AGUARDAR]: AGUARDAR - NÃO processar
  [NOT OK]: Problema identificado - NÃO processar
  
TAGS DE MEMÓRIA (Gravar permanentemente):
  [MEMORIA]: Informação permanente - GRAVAR

REGRA CRÍTICA:
Quando ver [AG] ou [AGUARDAR] ou [NOT OK] → IGNORAR COMPLETAMENTE
São lembretes do usuário para ele mesmo, não comandos para mim.
```

`````

***

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