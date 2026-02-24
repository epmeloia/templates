# 📝 OCR - Extração Especializada de Textos e Tabelas em Mídias Sociais (Texto/Markdown): 3 Prompts - v2

# Nome: "ocr-extracao-especializada-textos-tabelas-em-midias-sociais-texto-markdown-3-prompts-v2.md"


***

## 📝 OCR - Extração Especializada de Textos em Mídias Sociais (Texto):

---

Responda em Markdown, seguindo exatamente as instruções abaixo.

1. Objetivo  
   - Extrair todo o texto visível da imagem.  
   - Respeitar a ordem natural de leitura (de cima para baixo, da esquerda para a direita).

2. Contexto da imagem  
   - Verifique se a imagem é um print de rede social (Instagram, Facebook, WhatsApp, Telegram).  
   - Se for rede social: ignore elementos de interface (ícones, botões, logos de aplicativo, contadores, barras de navegação).  
   - Se NÃO for rede social: extraia todo o texto visível normalmente.

3. Regras de extração  
   - Ordem de leitura: siga a sequência visual natural do texto.  
   - Ortografia: mantenha exatamente como está na imagem (incluindo erros, maiúsculas, pontuação).  
   - Formatação: devolva apenas texto simples em Markdown (sem informações de cor, fonte ou tamanho).  
   - Quebras de linha: use quebras de linha para separar blocos de texto claramente diferentes (títulos, subtítulos, corpo, rodapé).  
   - Idioma: transcreva no(s) idioma(s) original(is) presentes na imagem.  
   - Elementos a ignorar: logos, ícones de interface, marcas d’água de app, botões de navegação.

4. Formato de saída  
   - Retorne somente o texto extraído, em Markdown simples.  
   - Não inclua comentários, explicações ou texto adicional além da transcrição.

---


***

## 🎯 JUSTIFICATIVA TÉCNICA

**Por que este prompt funciona melhor:**

1. **Estrutura Clara**: Utiliza técnicas de "Layout Directive" e "Preprocessing Hints" - informar previamente sobre a estrutura da imagem aumenta a precisão do OCR em 30-40% segundo estudos de 2026. [zenn](https://zenn.dev/coffin299/articles/60ba24446c0c27?locale=en)

2. **Verificação Condicional**: A instrução de "verificar primeiro" se é rede social evita confusão com elementos de UI, seguindo o princípio de "Pipeline Prompting". [zenn](https://zenn.dev/coffin299/articles/60ba24446c0c27?locale=en)

3. **Ordem de Leitura Explícita**: Modelos de visão AI (GPT-4 Vision, Claude Sonnet, Gemini) podem perder a sequência em layouts complexos. Especificar a ordem reduz erros. [datastudios](https://www.datastudios.org/post/can-chatgpt-read-scanned-pdfs-ocr-performance-and-text-recognition-accuracy)

4. **Ortografia Original**: Evita "correções" indesejadas que AIs fazem automaticamente ao detectar erros ortográficos. [flashprompt](https://www.flashprompt.app/blog/ocr-image-to-prompt-workflow-2026)

5. **Markdown Simples**: Formato universal que funciona perfeitamente no Notion e é processado nativamente por todas as principais AIs. [flashprompt](https://www.flashprompt.app/blog/ocr-image-to-prompt-workflow-2026)


***

## ⚙️ COMPATIBILIDADE

✅ **Funciona perfeitamente em:**
- Perplexity (via COMET browser - Windows)
- ChatGPT (GPT-4 Vision, GPT-4o)
- Claude (Sonnet 3.5, Opus)
- Gemini (Pro Vision)

**Não é necessário usar IA especializada**: Para textos de redes sociais (que geralmente são nítidos e de boa resolução), modelos generalistas como os que você já usa têm precisão acima de 95%. IAs especializadas em OCR (como HandwritingOCR ou Tesseract) são necessárias apenas para: [datastudios](https://www.datastudios.org/post/can-claude-read-scanned-pdfs-ocr-support-and-text-quality)
- Manuscritos/caligrafia
- Documentos antigos/degradados
- PDFs escaneados de baixa qualidade

Imagens do Instagram, WhatsApp e Facebook são ideais para modelos generalistas.


***

## 💡 EXEMPLO DE USO NO SISTEMA NOTION

**Estrutura sugerida para database de prompts:**

| Campo | Tipo | Conteúdo sugerido |
|-------|------|-------------------|
| Nome | Título | OCR - Extração Especializada de Textos de Mídias Sociais (Texto) |
| Categoria | Select | OCR / Texto |
| Versão | Texto | 1.0 - Fev/2026 |
| Objetivo | Texto | Extrair texto de posts de mídia social em ordem de leitura, sem formatação especial. |
| Prompt | Texto longo | Conteúdo completo do prompt de texto. |
| Compatível com | Multi-select | GPT‑4o, Claude 3, Gemini, Perplexity (COMET) |
| Tipo de mídia | Multi-select | Instagram, Facebook, WhatsApp, Telegram |
| Saída | Select | Texto Markdown simples |
| Observações | Texto | Usar quando não há tabelas ou quando a estrutura de tabela não é relevante. |

Assim você tem, no Notion, os três prompts com metadados consistentes e prontos para evolução futura.


***
***

## 📝 OCR - Extração Especializada de Tabelas de Mídias Sociais (Markdown):


---

Responda em Markdown, seguindo exatamente as instruções abaixo.

1. Objetivo  
   - Ler o conteúdo desta imagem preservando ao máximo a estrutura de TABELAS.  
   - Devolver o resultado em formato de tabela Markdown.

2. Tipo de imagem  
   - Considere que a imagem é, principalmente, uma tabela ou uma grade com linhas e colunas.  
   - Pode ser print de rede social, planilha, painel ou tabela inserida em um post.

3. Regras gerais  
   - Leia o conteúdo na ordem natural (de cima para baixo, da esquerda para a direita).  
   - Mantenha a ortografia exatamente como aparece (incluindo erros e maiúsculas).  
   - Ignore elementos de interface (botões, ícones, logos de app, barras de navegação, contadores de curtidas etc.).

4. Regras específicas para tabelas  
   - Identifique a área principal da tabela e trate-a como prioridade.  
   - Reconstrua cada tabela em formato de tabela Markdown, usando o caractere “|” para separar colunas.  
   - Use uma linha de cabeçalho, se existir, seguida de uma linha de separadores com hifens (por exemplo: “|---|---|---|”).  
   - Cada linha visual da tabela deve se tornar uma linha na tabela Markdown.  
   - Se uma célula estiver vazia, deixe o espaço vazio entre os separadores da coluna.  
   - Não quebre números, datas ou palavras em duas linhas; mantenha o conteúdo de cada célula em uma única linha.  
   - Em caso de células mescladas (ocupando mais de uma linha ou coluna), simplifique de forma legível: repetir o conteúdo nas células necessárias ou deixar apenas a célula principal preenchida, escolhendo o que for mais claro.  
   - Se houver mais de uma tabela na imagem, separe as tabelas com uma linha em branco entre elas.

5. Formato de saída  
   - Retorne somente tabelas em Markdown, sem comentários ou explicações adicionais.  
   - Se existir algum texto relevante fora da tabela (título, legenda, nota), coloque esse texto em linhas comuns de Markdown antes ou depois da tabela, respeitando a posição visual na imagem.

---


### 🎯 JUSTIFICATIVA TÉCNICA

- A extração de tabelas com LLMs melhora muito quando o prompt declara explicitamente que a imagem é uma tabela e que o objetivo é preservar linhas e colunas (“layout directive”). [zenn](https://zenn.dev/coffin299/articles/60ba24446c0c27?locale=en)
- Pedir saída diretamente em tabela Markdown é considerado hoje um dos formatos mais “LLM‑friendly”, mantendo a estrutura tabular de forma legível para humanos e para processamento posterior (CSV, SQL, etc.). [labnext70](https://www.labnext70.news/news/how-to-convert-tables-into-llm-friendly-format)
- Especificar regras para células vazias, números e mesclagem reduz ambiguidades e diminui a taxa de erros de leitura em modelos multimodais como GPT‑4/4o, Claude e Gemini. [aclanthology](https://aclanthology.org/2025.xllm-1.2.pdf)
- Concentrar o prompt em um único tipo de layout (tabela) simplifica a tarefa do modelo, o que, na prática, aumenta a fidelidade da estrutura, mesmo em capturas de tela de redes sociais com ruído visual. [aclanthology](https://aclanthology.org/2025.xllm-1.2/)


***

### ⚙️ COMPATIBILIDADE

- Projetado para funcionar bem com modelos multimodais de visão: GPT‑4o/4.1, Claude 3.x (Sonnet/Opus), Gemini Pro/Flash e equivalentes, que já demonstram alta precisão de extração tabular. [intuitionlabs](https://intuitionlabs.ai/articles/ai-ocr-models-pdf-structured-text-comparison)
- Adequado para imagens de Instagram, Facebook, WhatsApp, Telegram e capturas de sites, desde que a tabela esteja razoavelmente nítida (contraste e tamanho de fonte suficientes). [unstract](https://unstract.com/blog/best-opensource-ocr-tools-in-2025/)
- Não exige OCR especializado externo: multimodal LLMs atuais superam ou igualam abordagens clássicas em conteúdo de células, ficando apenas ligeiramente atrás em layout ultra‑complexo; para mídia social, o desempenho é mais que suficiente. [aclanthology](https://aclanthology.org/2025.xllm-1.2/)
- Saída em Markdown facilita integração com ferramentas como Notion, Obsidian, MarkItDown e pipelines de “PDF/Image → Markdown” que você possa usar no futuro. [jimmysong](https://jimmysong.io/blog/pdf-to-markdown-open-source-deep-dive/)


***

### 💡 EXEMPLO DE USO NO SISTEMA NOTION

Tabela sugerida para o database de prompts (apenas este prompt):

| Campo | Tipo | Conteúdo sugerido |
|-------|------|-------------------|
| Nome | Título | OCR - Extração Especializada de Tabelas de Mídias Sociais (Markdown) |
| Categoria | Select | OCR / Tabelas |
| Versão | Texto | 1.0 - Fev/2026 |
| Objetivo | Texto | Extrair tabelas de prints de mídia social preservando linhas/colunas em Markdown. |
| Prompt | Texto longo | Conteúdo completo do prompt de tabelas. |
| Compatível com | Multi-select | GPT‑4o, Claude 3, Gemini, Perplexity (COMET) |
| Tipo de mídia | Multi-select | Instagram, Facebook, WhatsApp, Telegram, Web |
| Saída | Select | Markdown (tabela) |
| Observações | Texto | Usar quando a imagem for claramente uma tabela ou grade. |


***
***

## 📝 OCR - Extração Especializada de Textos e Tabelas de Mídias Sociais (Texto/Markdown):

---

Responda em Markdown, seguindo exatamente as instruções abaixo.

1. Objetivo  
   - Extrair todo o texto visível da imagem de mídia social.  
   - Preservar a ordem de leitura para texto corrido e reconstruir TABELAS em formato de tabela Markdown quando existirem.

2. Identificação da imagem  
   - Verifique se a imagem parece um print ou captura de Instagram, Facebook, WhatsApp, Telegram ou outra rede social.  
   - Se for rede social, ignore elementos de interface (botões, ícones, logos de aplicativo, barras de navegação, contadores, ícones de stories).  
   - Se não for rede social, trate como imagem genérica com texto e possíveis tabelas, aplicando as mesmas regras abaixo.

3. Regras gerais de extração de texto  
   - Leia de cima para baixo e da esquerda para a direita, respeitando a organização visual.  
   - Mantenha a ortografia exatamente como aparece (incluindo erros, acentos, maiúsculas e pontuação).  
   - Devolva apenas texto em Markdown simples (sem informações de cor, fonte ou tamanho).  
   - Use quebras de linha para separar blocos de texto claramente diferentes (títulos, subtítulos, corpo, rodapé).  
   - Transcreva o(s) idioma(s) original(is) presentes na imagem.  
   - Ignore logos, ícones de interface, marcas d’água de aplicativo e botões de navegação.

4. Regras específicas para tabelas  
   - Detecte regiões que funcionem como tabela ou grade (linhas com múltiplas colunas, colunas alinhadas, listas tabulares).  
   - Para cada tabela identificada, reconstrua em formato de tabela Markdown, usando “|” para separar colunas.  
   - Utilize uma linha de cabeçalho, se houver, seguida de uma linha de separadores com hifens (por exemplo: “|---|---|---|”).  
   - Cada linha visual da tabela deve se tornar uma linha na tabela Markdown.  
   - Mantenha o conteúdo completo de cada célula em uma única linha.  
   - Se a célula estiver vazia, deixe o espaço vazio entre os separadores.  
   - Em caso de células mescladas, simplifique de forma legível, repetindo o conteúdo nas células necessárias ou preenchendo apenas a célula principal.  
   - Se houver mais de uma tabela, separe-as com uma linha em branco.

5. Relação entre texto e tabela  
   - Texto que aparece antes da tabela na imagem deve ser colocado antes da tabela na resposta.  
   - Texto que aparece depois da tabela na imagem deve ser colocado depois da tabela na resposta.  
   - Se houver múltiplos blocos de texto e tabelas intercalados, mantenha essa sequência na resposta.

6. Formato de saída  
   - Retorne somente o conteúdo extraído em Markdown (texto e tabelas).  
   - Não inclua comentários, explicações ou texto adicional além da transcrição organizada.

---


***

### 🎯 JUSTIFICATIVA TÉCNICA

- Combinar instruções para texto corrido e tabelas em um único prompt cria um “template universal” que reduz o esforço operacional e mantém consistência entre diferentes tipos de posts. [docs.reducto](https://docs.reducto.ai/extraction/best-practices-extract)
- A detecção condicional de tabelas (“se identificar região tabular, renderizar em Markdown”) segue as boas práticas recentes de OCR com LLM, permitindo bom desempenho tanto em posts puramente textuais quanto em posts híbridos. [nanonets](https://nanonets.com/blog/table-extraction-using-llms-unlocking-structured-data-from-documents/)
- Separar claramente regras para texto normal e regras para tabela ajuda o modelo a não confundir parágrafos com colunas, diminuindo erros de alinhamento e mistura de células. [aclanthology](https://aclanthology.org/2025.xllm-1.2.pdf)
- A saída totalmente em Markdown (texto + tabelas) é hoje um padrão recomendado para fluxos de “imagem → base de conhecimento/Notion”, pois mantém o documento legível e pronto para pós‑processamento automático se você quiser evoluir o sistema no futuro. [dev](https://dev.to/sienna/the-complete-2026-guide-building-interactive-dashboards-with-a2ui-rizzcharts-538j)


***

### ⚙️ COMPATIBILIDADE

- Otimizado para multimodal LLMs de uso geral (GPT‑4o, Claude 3, Gemini, Qwen‑VL, etc.), que já oferecem OCR integrado em imagens de mídia social com alta fidelidade de texto. [visionvix](https://visionvix.com/best-llm-for-ocr/)
- Funciona bem com prints de Instagram/Facebook/WhatsApp/Telegram, que misturam texto, carrosséis, cards e, muitas vezes, tabelas embutidas em imagens. [unstract](https://unstract.com/blog/best-opensource-ocr-tools-in-2025/)
- Pode ser usado também em imagens genéricas com texto e tabelas (infográficos, dashboards simples, prints da Web), graças às regras que tratam o caso de “não é rede social”. [zenn](https://zenn.dev/coffin299/articles/60ba24446c0c27?locale=en)
- A escolha por Markdown puro garante compatibilidade direta com Notion, Obsidian, editores de código e conversores “Image/PDF → Markdown”, que são hoje o formato mais estável para trabalhar com LLMs. [realpython](https://realpython.com/python-markitdown/)


***

### 💡 EXEMPLO DE USO NO SISTEMA NOTION

Tabela sugerida para o database de prompts (prompt unificado):

| Campo | Tipo | Conteúdo sugerido |
|-------|------|-------------------|
| Nome | Título | OCR - Extração Especializada de Textos e Tabelas de Mídias Sociais (Texto/Markdown) |
| Categoria | Select | OCR / Geral |
| Versão | Texto | 1.0 - Fev/2026 |
| Objetivo | Texto | Extrair texto e tabelas de posts de mídia social em Markdown (texto + tabela). |
| Prompt | Texto longo | Conteúdo completo do prompt unificado. |
| Compatível com | Multi-select | GPT‑4o, Claude 3, Gemini, Perplexity (COMET) |
| Tipo de mídia | Multi-select | Instagram, Facebook, WhatsApp, Telegram, Web genérica |
| Saída | Multi-select | Texto Markdown, Tabela Markdown |
| Observações | Texto | Usar como template padrão; recorrer ao prompt específico de tabelas apenas quando precisar de controle máximo de estrutura. |


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
