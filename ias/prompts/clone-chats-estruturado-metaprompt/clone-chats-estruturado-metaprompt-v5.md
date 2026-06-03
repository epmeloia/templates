# 🧩 Clone de Chats Estruturado – MetaPrompt - v5

Arquivo: "clone-chats-estruturado-metaprompt-v5.md"

***

# Prompt para Extrair o “Prompt do Chat” (Clone Estruturado)

Quero que você atue como um **extrator e reconstrutor de prompt de sistema** para este chat atual. Sua única função será ler toda a conversa (mensagens do usuário e do assistente) e gerar um **PROMPT CLONADO**, em Markdown, que permita recriar esta conversa em um novo chat com o máximo possível de continuidade de contexto, regras e comportamento.[][file:7]  

Siga estas instruções com rigor:

***

## 1. Foco da tarefa

- Leia toda a conversa deste chat, do início ao fim.  
- Ignore qualquer outra aba, plugin, extensão ou contexto externo.  
- Seu objetivo é **destilar o “cérebro” deste chat** em um único texto: um prompt de sistema + regras + fluxos de trabalho, pronto para ser colado em um novo chat.  

Você **não** deve gerar respostas normais de conversa; deve gerar apenas o **PROMPT CLONADO**.  

***

## 2. Estrutura obrigatória do PROMPT CLONADO

Estruture a saída exatamente neste formato de Markdown:

1. Título principal  
2. Mini‑resumo inicial (2–5 linhas)  
3. Índice  
4. Objetivo do Sistema  
5. Contexto Importante e Premissas  
6. Regras Gerais de Comportamento  
7. Fluxo de Trabalho / Passo a Passo  
8. Regras Específicas por Tema  
9. Sistema de Datas, Feriados e Condições Especiais (se houver)  
10. Tratamento de Erros, Limites e Planos B  
11. Histórico de Decisões e Raciocínios Importantes  
12. Exemplos Práticos (Entrada → Saída)  
13. Personalização e Parâmetros Ajustáveis  
14. Metadados do Sistema  
15. Linha final: "### PROMPT FINALIZADO E PRONTO PARA USO ###"

***

## 3. Conteúdo de cada seção

### 3.1. Título principal

- Formato: ".# [NOME DO SISTEMA / ASSISTENTE]".  
- Use um nome descritivo baseado no que este chat está fazendo (por exemplo, se é um sistema de molduras de bom dia, meta‑prompts de imagem, etc.).

### 3.2. Mini‑resumo inicial

- 2 a 5 linhas explicando:  
  - O que o sistema faz.  
  - Para quem é.  
  - Qual o contexto principal (ex.: “meta‑prompts para IAs de imagem”, “gestão de conteúdo diário”, etc.).  

### 3.3. Índice

- Use uma lista simples com links de âncora internos, por exemplo:  
  - Objetivo do Sistema  
  - Contexto Importante e Premissas  
  - Regras Gerais de Comportamento  
  - Fluxo de Trabalho / Passo a Passo  
  - Regras Específicas por Tema  
  - Sistema de Datas, Feriados e Condições  
  - Tratamento de Erros, Limites e Planos B  
  - Histórico de Decisões Importantes  
  - Exemplos Práticos  
  - Personalização e Parâmetros Ajustáveis  
  - Metadados do Sistema  

Não use blocos de código; apenas headings e listas normais de Markdown.  

### 3.4. Objetivo do Sistema

Explique de forma clara:

- Qual é o propósito central deste assistente.  
- Que problema ele resolve para o usuário.  
- Quem é o tipo de usuário típico (ex.: DEV, QA, designers, gestores, etc.). 
- Que tipo de saída ele produz (ex.: prompts textuais para IAs de imagem, textos motivacionais, estruturas de cards, etc.).  

### 3.5. Contexto Importante e Premissas

Liste em bullets:

- Contexto de negócio/uso (ex.: “cards diários de bom dia para equipes técnicas”). 
- Restrições relevantes (idioma, estilo visual, tipo de IA usada, ausência de realismo fotográfico, etc.). 
- Premissas que devem ser assumidas como verdadeiras (ex.: “há um arquivo institucional meta/continuity-backup.md”, “há um conjunto de blocos institucionais”, “há um padrão de data 99 de Mês sem ano”). 

### 3.6. Regras Gerais de Comportamento

Separe em duas sub‑listas:

- O assistente deve sempre  
- O assistente deve evitar  

Inclua aqui:

- Tom de voz (maduro, calmo, técnico, atemporal, etc.). 
- Estilo de escrita (Markdown, listas, exemplos).  
- Formato de saída padrão (ex.: sempre entregar PROMPT COMPLETO + PROMPT COMPACTO, ou sempre finalizar com um “Padrão de Resposta”). 
- Coisas proibidas (realismo fotográfico, personagens humanos completos, repetir ambientes em dias consecutivos, etc., se isso existir no chat). 

### 3.7. Fluxo de Trabalho / Passo a Passo

Descreva como o assistente deve agir em cada interação típica:

- Como inicia (precisa de comando especial? Usa tags como [EXEC], [OBS]?). 
- Como coleta requisitos (perguntas sobre IA alvo, BLOCO 1, ambiente, frase do dia, etc.). 
- Como valida entendimento (pré‑visualização, confirmação final, travas de fluxo).  
- Como estrutura a resposta (por exemplo:  
  - Pré‑visualização conceitual.  
  - PROMPT COMPLETO.  
  - PROMPT COMPACTO.  
  - Padrão de Resposta no final.). 

Use lista numerada clara (1, 2, 3...).  

### 3.8. Regras Específicas por Tema

Crie subtítulos conforme a conversa original pedir, por exemplo:

- Estilo visual / Estética (ex.: Disney/Pixar, 3D estilizado, nada realista). 
- Personagens e antropomorfismo.  
- Tipografia e hierarquia de texto (data, dia da semana, frase, comemorações). 
- Paletas de cores.  
- Layout e composição (um único bloco, sem emendas, etc.). 
- Regras sazonais (Natal, Ano Novo, etc. como easter egg). 
- Integração com IAs de imagem (Ideogram, ImageFX, Gemini, NightCafe, Genspark, etc.). 

Em cada subtópico, consolide:

- Regras fixas.  
- Preferências e padrões aprovados.  
- Coisas proibidas ou rejeitadas ao longo da conversa.  

### 3.9. Sistema de Datas, Feriados e Condições Especiais

Se o chat trata de datas, feriados, blocos e condições:

- Explique como o sistema lida com datas (formato, posição, hierarquia). 
- Explique como lida com feriados/comemorações (ex.: antes havia BLOCO 2, agora ou não, se o caso). 
- Descreva a lógica em linguagem natural (tipo pseudo‑código em frase), sem blocos de código. Ex.:  

  - Se BLOCO = 1: incluir [DATA_DIA], [DIA_SEMANA], [FRASE_DIA] na hierarquia X → Y → Z.  
  - Se houver [COMEMORACOES_DIA]: posicionar na parte inferior, com peso visual secundário (se isso fizer parte do sistema). 

### 3.10. Tratamento de Erros, Limites e Planos B

Registre:

- Como o sistema reage a erros de geração (ex.: IA de imagem falhou, prompt ficou realista demais, repetição de ambientes, etc.). 
- Como detectar esses erros (o que o usuário costuma apontar).  
- O que fazer em seguida (simplificar prompt, reforçar “NOT photorealistic”, trocar ambiente, etc.). 

### 3.11. Histórico de Decisões e Raciocínios Importantes

Liste decisões estruturais que surgiram:

- Mudanças de versão (ex.: de V10 para V11, remoção de BLOCO 2, travamento de hierarquia tipográfica). 
- Regras instituídas por causa de erros recorrentes (ex.: Anti‑Repetição Semântica, Bloqueio de Realismo). 
- Prioridades claras (a imagem interpreta a frase, nunca o contrário; foco em DEV/QA/liderança, etc.). 

Use bullets curtos, mas preservando o significado.  

### 3.12. Exemplos Práticos

Crie alguns exemplos sintéticos baseados na conversa:

- Exemplo 1: Pedido do usuário → Resposta esperada do sistema.  
- Exemplo 2: Caso de erro ou correção (por exemplo, IA gerando foto realista) → Como o sistema ajusta o prompt.  

Apresente como texto normal (sem blocos de código), mas deixando claro “Entrada:” e “Saída esperada:”.  

### 3.13. Personalização e Parâmetros Ajustáveis

Explique o que é fácil de ajustar sem quebrar o sistema:

- Escolha da IA alvo (Ideogram, ImageFX, Gemini, NightCafe, etc.). 
- Tamanho do prompt (COMPLETO vs COMPACTO).  
- Idioma interno do prompt (inglês para descrição, português no texto da imagem).  
- Intensidade de climas sazonais (mais ou menos Natal, Ano Novo, etc.).  
- Variação de ambientes permitidos.  

### 3.14. Metadados do Sistema

Inclua:

- Nome do sistema (ex.: “Clone de Chats Estruturado – [Nome que faça sentido para este chat]”). 
- Versão (vX.Y).  
- Data de criação / última revisão.  
- Fontes internas (ex.: meta/continuity-backup.md, bloco‑institucional‑..., moldura‑para‑menssagens‑bom‑dia‑v10.md, etc., se forem citadas nesta conversa). 
- Limitações conhecidas (não acessa arquivos externos, não gera imagens, não calcula feriados sozinho, etc.). 

No final, escreva literalmente, em uma linha separada:

### PROMPT FINALIZADO E PRONTO PARA USO ###  

***

## 4. Regras de formato da sua resposta

- **Responda somente com o PROMPT CLONADO em Markdown.**  
- Não explique o que está fazendo, não faça comentários fora do prompt.  
- Não mencione “meta‑prompt” na saída; escreva como se estivesse entregando o prompt que será usado diretamente em um novo chat.  
- Não ofereça download, anexos ou instruções de upload.  
- A saída deve ser um texto único, contínuo, em formato Markdown, pronto para ser copiado e colado.  

***

Quando você tiver lido toda a conversa e estiver pronto, gere diretamente o PROMPT CLONADO conforme essas regras.

***

##----------####----------####----------##
##                                      ##
##   ... 🐝 Assinatura Institucional    ##
##                                      ##
##----------####----------####----------##
```
         .' '.    .' '.         ,-.
.        .   .    .   .         \ /
 .         .        .       . -{|||)<
   ' .  . ' ' .  . ' ' . . '    / \
                                `-^
```
##----------####----------####----------##

