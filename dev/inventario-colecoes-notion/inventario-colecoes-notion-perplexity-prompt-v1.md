# Inventário de Coleções em Notion - Perplexity - Prompt v1:
"inventario-colecoes-notion-perplexity-prompt-v1.md"

# 📦 🔍 Coleções 🚗 🏁

# 📦 🔍 Inventário de Coleções 🚗 🏁

# 📦 🔍 Inventário de Coleções em Notion 🚗 🏁

---


***

## 💡 SUGESTÕES DE MELHORIA IMPLEMENTADAS

Neste prompt, incluí:

1. ✅ **Estado atual do projeto** - fácil rastrear progresso
2. ✅ **Campos bloqueados explícitos** - evita edições indesejadas
3. ✅ **Hierarquia de fontes visual** - ordenação clara
4. ✅ **Sistema de notação** - rastreabilidade perfeita
5. ✅ **Fluxo passo-a-passo** - procedimento estruturado
6. ✅ **Tabela de códigos** - decodificação de formatos
7. ✅ **Variantes conhecidas** - banco de dados acumulativo
8. ✅ **Checklist editável** - usar em cada item
9. ✅ **Exemplo de próxima sessão** - contexto de continuação
10. ✅ **Regras de ouro** - princípios indiscutíveis

***

## 🚀 PRÓXIMOS PASSOS

**Para você:**
1. Copiar o conteúdo entre os triplos backticks.
2. Criar arquivo `inventario-colecoes-notion-perplexity-prompt-v1.md` no seu GitHub
3. Salvar com versionamento
4. Em nova conversa: colar o prompt inteiro e continuar de onde parou

**Sistema estará 100% pronto** para continuar validando itens sem nenhuma perda de contexto!

Quer que eu ajuste algo no prompt antes de você salvar no GitHub? 🎯


---

# 📦 🔍 Inventário de Coleções em Notion 🚗 🏁

Aqui está o prompt completo, criado por mim (Comet), que espelha toda a nossa conversa e está pronto para ser usado em futuras sessões. Você pode copiar este conteúdo e salvar no seu GitHub:

***

```markdown
# 📦 🔍 Inventário de Coleções em Notion 🚗 🏁

## 📋 CONTEXTO DO PROJETO

**Objetivo:** Coletar, validar, complementar e estruturar informações de uma coleção de miniaturas diecast (Hot Wheels, Matchbox) em um banco de dados Notion, baseado em dados reais e fontes confiáveis.

**Coletor:** Usuário português/brasileiro com expertise em database design e catalogação de coleções.

**Banco de Dados:** Notion workspace "Miniatura de Carros" com 250+ itens planejados.

**Data de Início:** 27/11/2025

---

## ✅ STATUS ATUAL DO PROJETO

### ITENS VALIDADOS (100% COMPLETOS):
- **Item 00011:** HW50 Concept (Roxo) - Referência/Template
- **Item 00012:** Batman 1966 Batmobile - Premium
- **Item 00013:** Custom '56 Ford Truck - Celebration Racers
- **Item 00014:** Deora II - HW Fan Driven Mini Collection (2026)
- **Item 00015:** '15 Land Rover Defender Double Cab - HW Dirt 2025

### PRÓXIMOS ITEMS: Em aguardo para validação

---

## 🔐 RESTRIÇÕES CRÍTICAS (ORDEM DE PRIORIDADE)

### NUNCA VALIDAR ESTES CAMPOS:
- `ID` - Campo de sistema criado
- `Val-ID` - Campo de validação criado
- `Ano no Chassi` - SEMPRE pré-validado do chassis físico
- `Escala` - Sempre 1:64 (padrão)
- `Compra` - Data de aquisição do usuário
- `Condicao` - Sempre "Novo" (padrão para coleção)

### DADOS MARCADOS COM "(CHASSI)" = PRÉ-VALIDADOS:
- **REGRA ABSOLUTA:** Qualquer informação com notação "(Chassi)" foi validada fisicamente pelo usuário
- **AÇÃO:** Aceitar SEM pesquisar, copiar para observações com fonte
- **EXEMPLO:** Se campo mostra "N7C5 (Chassi)" → não validar, apenas documentar

### FABRICAÇÃO = SEMPRE MALAYSIA:
- **REGRA:** Hot Wheels fabrica SEMPRE em Malaysia (confirmado pelo usuário)
- **AÇÃO:** Não pesquisar, não validar, apenas confirmar
- **FONTE:** Pré-validado pelo usuário

---

## 🌐 HIERARQUIA DE FONTES (ORDEM RIGOROSA)

1. **Hot Wheels Wiki (PRIMÁRIA)** → fandom.com/wiki/Hot_Wheels
   - Use para: Nome do modelo, ano, série, molde, variações
   - Prioridade: 100% confiável

2. **Fontes Secundárias** → Retail sites, documentação oficial, Wikipedia
   - Use para: Complementar informações não encontradas na Wiki
   - Exemplo: Rihappy, Shopee, eBay, MiniHunts, CollectHW.com

3. **Google Images (ÚLTIMA)** → Apenas para referência visual
   - Use para: Verificar cores, detalhes, comparar variações

### NUNCA use:
- Geradores de imagem AI
- Especulações pessoais
- Dados não-documentados

---

## 📝 SISTEMA DE NOTAÇÃO DE FONTE

Use estas anotações no campo "Observações" para rastrear origem dos dados:

```
. (Blister) = Informação impressa no blister/cartela
. (Chassi) = Informação gravada no chassis físico
. (Wiki) = Informação do Hot Wheels Wiki
. (Secundária) = Informação de fonte secundária verificada
```

**EXEMPLO DE USO:**
```
# Toy #: JBC00
. (Blister) = Identificador impresso na cartela

# Base Code: N7C5
. (Chassi) = Código gravado no chassis - PRÉ-VALIDADO
```

---

## 🔍 FLUXO DE VALIDAÇÃO POR ITEM

### PASSO 1: DOCUMENTAÇÃO INICIAL
- [ ] Aceite o ID do item a validar (ex: 00016)
- [ ] Navegue para a página do item no Notion
- [ ] Tire screenshot do estado atual
- [ ] Documente TODOS os campos preenchidos

### PASSO 2: PESQUISA NA WIKI
- [ ] Acesse Hot Wheels Wiki para o modelo específico
- [ ] Extraia página completa em texto
- [ ] Procure: Nome, Série, Ano, Molde, Cores, Variações, Base Codes
- [ ] Compare com dados já preenchidos no Notion

### PASSO 3: VALIDAÇÃO DE CAMPOS
- [ ] Se campo = (Chassi) → Aceite sem validação ✅
- [ ] Se campo vazio → Pesquise na Wiki
- [ ] Se campo preenchido → Valide contra Wiki
- [ ] Se discrepância → Documente ambas as versões

### PASSO 4: ANÁLISE DE CÓDIGOS
- [ ] **Toy #:** Identifique função (produto/variação)
- [ ] **Base Code:** Decodifique formato (Letra=Ano, Números=Semana)
- [ ] **Pull Code:** Pesquise em web sources (NÃO em imagens)
- [ ] **UPC/EAN:** Valide código de varejo
- [ ] **Códigos adicionais:** Pesquise cada um SEPARADAMENTE

### PASSO 5: ESTRUTURA DE OBSERVAÇÕES
```
Códigos de Produção:

# Toy #: [CÓDIGO]
. (Fonte) = Descrição

# Base Code: [CÓDIGO]
. Breakdown: X = Ano, XX = Semana, X = Planta
. (Fonte) = Informação

[... mais códigos conforme necessário ...]

# Observações Adicionais:
. Material: [Especificação]
. Fabricação: Malaysia (confirmado)
. País: [País]
. [... mais informações ...]
```

### PASSO 6: REVISÃO FINAL
- [ ] Todos campos validados contra Wiki ✅
- [ ] Observações com notação de fonte ✅
- [ ] Imagens mínimas: 3 packaging + 3 produto ✅
- [ ] Status marcado como "100% COMPLETO"

---

## 🎨 CAMPOS QUE PODEM SER EDITADOS

**APENAS adicione informações** no campo "Observações":
- Sempre COLAR ABAIXO de informações existentes
- Nunca substituir conteúdo anterior
- Usar notação de fonte para cada adição

**CAMPOS EDITÁVEIS DURANTE VALIDAÇÃO:**
- Pull Code (se vazio) → Preencher ou "Não localizado na Wiki"
- Observações → SEMPRE adicionar (nunca remover)
- Observações Adicionais → Complementar conforme necessário

**CAMPOS BLOQUEADOS:**
- ID, Val-ID, Ano no Chassi, Escala, Compra, Condição
- Qualquer campo com (Chassi) = Não editar

---

## 📊 TIPOS DE CÓDIGOS E COMO DECODIFICAR

### PULL CODE (Injection/Molding Code)
**Formato:** `U##N` (Letter-Numbers-Letter)
- **Letra inicial:** Ano (U=2025, T=2024, S=2023)
- **Números:** Semana de produção (01-52)
- **Letra final:** Planta/Variante (N, C, W, etc.)
- **NOVO 2025:** Letra final agora aparece no final (U##N ao invés de U##)

**Exemplo:** `U08N` = 2025, Semana 8, Planta N

### BASE CODE (Chassis/Production Code)
**Formato:** Similar ao Pull Code
- **Letra:** Ano de produção
- **Números:** Semana (01-52)
- **Letra:** Plant/Variant code

**DIFERENÇA:** Base Code pode ser diferente do Pull Code (diferentes semanas)

**Exemplo:** 
- Pull Code: U08N (Semana 8)
- Base Code: U11N (Semana 11) = Variantes do mesmo mold

### TOY # (Product Number)
**Estrutura:** Código único como `JBC00`
- Identifica modelo + primeira cor/variação
- Pode ter múltiplas variantes (JBC00, JBC01, etc.)
- Sufixo após código = Base Code específico da unidade

**Exemplo:** `JBC00-N7C5` = Toy# JBC00 + Base Code N7C5

### VARIANTES CONHECIDAS
**JBC00 (Land Rover Defender Yellow 2025):**
- JBC00-N7C5 → Cartão Internacional "Mordus de Poussière"
- JBC00-N5215785 → Cartão Internacional curto
- JBC00-N9C0L2593Q → Cartão USA long card

---

## 🌟 DICAS DE EFICIÊNCIA

### PARA CADA NOVO ITEM:
1. **Use item 00011 como REFERÊNCIA** - é o template de qualidade
2. **Mantenha Web Search eficiente** - máximo 3 queries por lote
3. **Compile descobertas antes de editar** - documente tudo antes de adicionar
4. **Respeite notação de fonte** - cada informação tem origem documentada
5. **Preserve dados Chassi** - NUNCA altere informações pré-validadas

### CHECKLIST PASSO-A-PASSO:
```
[ ] 1. Screenshot do estado inicial
[ ] 2. Pesquisa completa na Wiki
[ ] 3. Compilação de todas as descobertas
[ ] 4. Validação de campos preenchidos
[ ] 5. Preenchimento de campos vazios
[ ] 6. Formatação de Observações com notação
[ ] 7. Verificação final
[ ] 8. Marcar como 100% COMPLETO
```

---

## 📱 COMO USAR ESTE PROMPT

### PRIMEIRA SESSÃO (Esta):
- Colar prompt completo em uma nova conversa
- Sistema estará pronto para validar próximo item imediatamente
- Informar ID do próximo item: "Próximo: 00016" (ou qual for)

### SESSÕES FUTURAS:
- Colar prompt em cada nova conversa
- Manter continuidade da validação
- Atualizar "STATUS ATUAL" com novos itens validados
- Acumular conhecimento de variações conhecidas

---

## 🎯 EXEMPLO DE INTERAÇÃO (PRÓXIMA SESSÃO)

**Usuário:** "Próximo: 00016"

**Sistema:**
1. Navega para item 00016 no Notion
2. Documenta estado atual
3. Acessa Wiki do modelo
4. Pesquisa todos os códigos
5. Compila observações
6. Valida contra template 00011
7. Preenche Pull Code + Observações
8. Marca como 100% completo
9. Aguarda próximo ID

---

## 🔒 REGRAS DE OURO

1. ✅ **Respeitar dados (Chassi)** = Não validar, apenas documentar
2. ✅ **Sempre adicionar, nunca remover** = Campo Observações é cumulativo
3. ✅ **Fonte documentada** = Cada informação tem origem clara
4. ✅ **Malaysia sempre** = Não pesquisar fabricação
5. ✅ **Wiki é primária** = Sempre começar lá
6. ✅ **Consistência** = Seguir formato de item 00011
7. ✅ **Completude** = 100% ou nada - items parciais não são finalizados

---

## 📞 CONTATO E SUGESTÕES

Prompt criado em: 27/11/2025 às 01:00 -03
Versão: 1.0
Para melhorias: Adicionar ao README.md do repositório

---
```

