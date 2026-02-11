Com base na análise da página do ChatGPT ativa e no arquivo anexado, gerando o snapshot institucional completo:

***

# 📄 Analise Prompt.md

***

## 1️⃣ IDENTIDADE DO PROJETO

- **Nome do projeto**: EXPs GENERALISTA
- **Versão operacional atual**: V10
- **Data aproximada do snapshot**: 28/12/2025 (domingo)
- **Ambiente de uso**: ChatGPT (GPT personalizado)
- **Status**: ATIVO

***

## 2️⃣ PROMPTS ATIVOS EM USO

### Prompt operacional principal

```
Use o arquivo `prompt-clonagem-continuidade-v10.2.md` como base absoluta de funcionamento deste chat. Considere o arquivo `meta/continuity-backup.md` como fonte institucional imutavel e superior a qualquer instrucao isolada. Aplique a LISTA MESTRA como template obrigatorio de controle e finalize todas as respostas com o Padrao de Resposta.
```

### Arquivos de referência institucional

⚠️ **Regra implícita detectada**: 
- Arquivo `prompt-clonagem-continuidade-v10.2.md` (não disponível no chat atual)
- Arquivo `meta/continuity-backup.md` (não disponível no chat atual)
- Estes arquivos são referenciados como "fonte institucional imutável e superior"

### Comandos operacionais detectados no chat

- `[EXEC] pré-visualização do Bloco 1` → Aciona pré-visualização do Bloco 1
- `[EXEC] Confirmação Final para gerar o Bloco 1` → Gera imagem do Bloco 1
- `[EXEC] pré-visualização do Bloco 2` → Aciona pré-visualização do Bloco 2
- `[EXEC] Confirmação Final para gerar o Bloco 2` → Gera texto do Bloco 2
- `[OBS]` → Observações e correções
- `[ANEXO]` → Anexos de referência

***

## 3️⃣ LISTA MESTRA ATUAL (COMPLETA)

```markdown
## 🔄 PROXIMO PASSO — CONTINUIDADE (LISTA MESTRA) — ATUALIZADA

### Últimos 5 `[OK]`

* [OK] Decisão de usar metaprompt como coletor institucional
* [OK] Definição de fluxo COMET → `.md` → novo chat
* [OK] Nome oficial do arquivo definido: `Analise Prompt.md`
* [OK] Metaprompt criado e pronto para uso imediato
* [OK] Estratégia de migração V10 → V11 estabilizada

---

### `[NOT OK]`

*(nenhum ativo)*

---

### `[NOT NEC]`

* [NOT NEC] Resumo manual de conversas
* [NOT NEC] Continuidade neste chat longo

---

### `[ ]`

* [ ] Executar metaprompt no Assistente do COMET
* [ ] Gerar `Analise Prompt.md`
* [ ] Usar arquivo para validação e continuidade no novo chat

---

### 📌 Padrao de Resposta

[ ] / [OK] / [NOT OK] / [EXEC] / [NOT NEC] / [ANEXO] / [OBS]

---
```

***

## 4️⃣ BLOCOS FUNCIONAIS EXISTENTES

### Bloco 1 — Moldura com Mensagem do Dia

**Finalidade**:
- Gerar imagem motivacional diária para equipe de DEVs, Testers, chefes e gerentes
- Comunicar mensagens de reflexão profissional, produtividade, equilíbrio e contexto organizacional

**Regras críticas**:
- Estrutura tipográfica fixa e hierarquizada:
  - **Topo central**: Data no formato "DD de Mês" (sem ano) — maior fonte da imagem
  - **Abaixo da data**: Dia da semana — fonte 85% do tamanho da Data
  - **Centro da imagem**: Frase motivacional — fonte 75% do tamanho da Data
- A frase é o foco semântico principal, a imagem interpreta a frase (nunca o contrário)
- Texto pode sobrepor elementos visuais se necessário
- Público: DEV, QA, gerentes — linguagem profissional
- Paleta: tons equilibrados (bege, dourado claro, verde suave, madeira clara)
- Contextos sazonais/climáticos são "easter eggs" sutis (nunca protagonistas)
- Nenhum elemento visual é fixo — imagens sempre aleatórias e surpreendentes
- Bloco 1 é único, fixo e imutável por entrega

**Problemas atuais**:
- Inicialmente houve repetição de elementos visuais (óculos na mesa, folhas)
- Fontes da data estavam menores que o especificado
- Excesso de clima temático (ex: Natal muito destacado)
- ✅ Todos corrigidos durante a execução do chat

### Bloco 2 — Comemorações do Dia

**Finalidade**:
- Listar comemorações do dia (mundiais, nacionais, locais)
- Fornecer contexto informativo sobre feriados e datas relevantes

**Regras críticas**:
- **Topo**: Título simples e discreto ("Comemorações do dia" ou "Comemoração do dia") — SEM DATA
- Estrutura de lista com emojis de bandeiras e descrições:
  - 🌐 Mundial
  - 🇧🇷 Brasil (nacional/regional)
- Nunca incluir data no Bloco 2 (data pertence exclusivamente ao Bloco 1)
- Bloco 2 é texto puro (não é imagem)

**Problemas atuais**:
- Inicialmente o Bloco 2 estava incluindo a data (corrigido)
- ✅ Corrigido durante a execução

### Montagem (externa)

**Como ocorre**:
- Bloco 1 (imagem) e Bloco 2 (texto) são gerados separadamente
- Usuário realiza junção manual sem espaços em branco
- Resultado final: aparência de imagem única e contínua
- Assistente não executa a montagem final

***

## 5️⃣ REGRAS CRÍTICAS E GATES

### Gates de pré-visualização

- **Bloco 1**: 
  - `[EXEC] pré-visualização do Bloco 1` → Usuário fornece data e frase
  - Assistente descreve estrutura, conceito, paleta, direção criativa
  - Aguarda confirmação antes de gerar imagem
  
- **Bloco 2**:
  - `[EXEC] pré-visualização do Bloco 2` → Usuário fornece data
  - Assistente lista comemorações encontradas
  - Aguarda confirmação antes de gerar texto final

### Confirmação final

- Ambos os blocos exigem comando explícito:
  - `[EXEC] Confirmação Final para gerar o Bloco 1`
  - `[EXEC] Confirmação Final para gerar o Bloco 2`
- Nenhum bloco é gerado sem confirmação final

### Comandos obrigatórios

- Estados: `[ ]`, `[OK]`, `[NOT OK]`, `[EXEC]`, `[NOT NEC]`, `[ANEXO]`, `[OBS]`
- Toda resposta deve finalizar com "📌 Padrão de Resposta" listando os estados aplicáveis

### Comportamentos proibidos

- Não gerar blocos sem confirmação final
- Não resumir ou reescrever regras estabelecidas
- Não incluir data no Bloco 2
- Não repetir elementos visuais de forma mecânica
- Não fazer Natal (ou outros climas) como tema principal
- Não usar fontes menores que o especificado para hierarquia tipográfica

### Violações detectadas no histórico

- ✅ Violação corrigida: Data foi incluída no Bloco 2 inicialmente (corrigido via `[OBS]`)
- ✅ Violação corrigida: Fontes da hierarquia tipográfica estavam incorretas (corrigido via `[OBS]` com referências visuais)
- ✅ Violação corrigida: Elementos visuais repetitivos (óculos, folhas) (corrigido via `[OBS]`)

***

## 6️⃣ POLÍTICAS INSTITUCIONAIS ATIVAS

### Bloco institucional

⚠️ **Referenciado mas não disponível no chat atual**:
- Arquivo `meta/continuity-backup.md` declarado como "fonte institucional imutável e superior a qualquer instrução isolada"
- Conteúdo não visível no snapshot atual

### Regras de revisão

**Detectadas no fluxo operacional**:
- Revisão ortográfica: não explicitada (inferida como padrão)
- Revisão semântica: frases devem ser profissionais, adequadas ao público DEV/QA/gestão
- Revisão pragmática: mensagens devem ser aplicáveis ao contexto de trabalho

**Status**: ATIVAS (aplicadas implicitamente durante validações com `[OBS]`)

### Regras de versionamento

- Versão atual: V10
- Estratégia de migração V10 → V11 em preparação
- Metaprompt criado para coletar dump institucional
- Arquivo de saída: `Analise Prompt.md`
- Fluxo: COMET → `.md` → novo chat

**Status**: ATIVAS

***

## 7️⃣ AJUSTES RECENTES REALIZADOS NO CHAT

### Correções visuais — Bloco 1

- Ajuste de hierarquia tipográfica (data 2x maior que estava sendo gerada)
- Redução de elementos repetitivos (óculos, folhas)
- Calibração de clima natalino (de protagonista para easter egg)
- Inclusão de laptop como elemento possível (sugestão do usuário)
- Fornecimento de 6 imagens de referência para calibração de fontes

### Correções estruturais — Bloco 2

- Remoção da data do Bloco 2 (data pertence apenas ao Bloco 1)
- Definição de título discreto ("Comemorações do dia")
- Clarificação de que Bloco 2 é texto, não imagem

### Separação rigorosa de blocos

- Bloco 1: imagem (data + dia da semana + frase)
- Bloco 2: texto (comemorações)
- Montagem manual realizada externamente pelo usuário
- Nenhum espaço em branco entre blocos na entrega final

### Mudança de fluxo

- Estabelecimento claro de gates de pré-visualização
- Confirmação final obrigatória antes de gerar qualquer bloco
- Uso sistemático de estados `[EXEC]`, `[OBS]`, `[ANEXO]` para controle

***

## 8️⃣ PROBLEMAS CONHECIDOS (SE EXISTIREM)

### Problema 1: Imagem não gerada

- **O que falhou**: Em uma tentativa, imagem não foi criada (nenhuma informação retornada)
- **Onde falhou**: Primeiro comando `[EXEC] Confirmação Final para gerar o Bloco 1` (data 24/12/2025)
- **Estado atual**: Corrigido na segunda tentativa

### Problema 2: Fontes menores que especificado

- **O que falhou**: Data estava sendo gerada com fonte menor que o padrão definido
- **Onde falhou**: Primeiras iterações do Bloco 1
- **Estado atual**: Corrigido após fornecimento de imagens de referência pelo usuário

### Problema 3: Repetição de elementos visuais

- **O que falhou**: Óculos na mesa e folhas estavam sendo repetidos
- **Onde falhou**: Bloco 1 (primeiras gerações)
- **Estado atual**: Corrigido — estabelecida regra de que nenhum elemento é fixo

### Problema 4: Clima natalino excessivo

- **O que falhou**: Natal como tema principal em vez de easter egg
- **Onde falhou**: Bloco 1 (data 24/12/2025 — Véspera de Natal)
- **Estado atual**: Corrigido — Natal como clima sutil, nunca protagonista

### Problema 5: Data incluída no Bloco 2

- **O que falhou**: Bloco 2 continha data no topo
- **Onde falhou**: Primeiras gerações do Bloco 2
- **Estado atual**: Corrigido — data pertence exclusivamente ao Bloco 1

***

## 9️⃣ STATUS FINAL DE CONTINUIDADE

### Este snapshot é suficiente para continuar em novo chat?

**SIM**, com ressalvas.

**Justificativa**:
- Estrutura operacional dos Blocos 1 e 2 está completamente documentada
- Regras de hierarquia tipográfica, paleta, público-alvo e gates estão explícitas
- Estados de controle (`[EXEC]`, `[OBS]`, etc.) estão mapeados
- Problemas conhecidos e correções aplicadas estão registrados

**Ressalvas**:
- Arquivos `prompt-clonagem-continuidade-v10.2.md` e `meta/continuity-backup.md` não estão acessíveis no snapshot
- Conteúdo institucional referenciado como "imutável e superior" não foi capturado

### Alguma informação crítica está faltando?

**SIM**.

**Justificativa**:
- Arquivo `prompt-clonagem-continuidade-v10.2.md` (base absoluta de funcionamento) — não disponível
- Arquivo `meta/continuity-backup.md` (fonte institucional imutável) — não disponível
- Políticas consolidadas de revisão ortográfica/semântica/pragmática — não explicitadas (apenas inferidas)
- Regras de versionamento completas — parcialmente inferidas

### Há risco de erro silencioso se continuar apenas com este arquivo?

**SIM**, risco moderado.

**Justificativa**:
- Sem acesso aos arquivos institucionais (`prompt-clonagem-continuidade-v10.2.md` e `meta/continuity-backup.md`), regras não documentadas neste snapshot podem ser perdidas
- Políticas institucionais consolidadas podem conter diretrizes não visíveis no histórico do chat
- Versionamento V10 → V11 pode depender de contexto adicional não capturado

**Mitigação**:
- Se os arquivos institucionais forem fornecidos ao novo chat junto com este `Analise Prompt.md`, o risco é minimizado
- Este snapshot cobre totalmente a operação visual/estrutural dos Blocos 1 e 2

***

> **Snapshot institucional gerado para continuidade controlada.**

[1](https://chatgpt.com/g/g-p-678fd07eac38819197d553574a0ed631/c/694af184-a600-832d-954e-aa9ab15ab8c4)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/108742584/e353daac-31f4-46f5-a50e-78dee5f2d796/exemplo-de-lista-mestra.txt)