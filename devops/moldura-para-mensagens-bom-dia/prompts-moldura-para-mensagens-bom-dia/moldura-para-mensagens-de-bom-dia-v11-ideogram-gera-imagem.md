# Moldura para Mensagens de Bom Dia - v11 - Ideogram Gera Imagem.md

# Nome: "moldura-para-mensagens-de-bom-dia-v11-ideogram-gera-imagem.md"

---

Vou separar em três blocos:

1. Modelo de entrada que você usa aqui no chat (BLOCO 1).
2. Template de **PROMPT EXTERNO v11 – Ideogram** (com placeholders).
3. Checklist v11 de validação da imagem.

---

## 1. Template de entrada BLOCO 1 (no chat)

Este é só para padronizar como você me envia cada dia:

```markdown
[EXEC] BLOCO 1
Data: DD/MM/AAAA
"Frase do dia exatamente como deve aparecer na imagem."
Ambiente: Nome curto do ambiente – descrição resumida do clima visual.
```

Exemplo rápido:

```markdown
[EXEC] BLOCO 1
Data: 05/02/2026
"Reduzir excessos agora facilita suas escolhas depois."
Ambiente: Jardins Suspensos de Órion – Terraços de cristal construídos no interior da constelação de Órion, regados pela luz azulada das estrelas gigantes.
```

---

## 2. TEMPLATE v11 – PROMPT EXTERNO (Ideogram)

Abaixo está o **prompt genérico** para Ideogram, com placeholders.
Você só precisa substituir o que está entre `{CHAVES}` antes de colar na Ideogram.

```markdown
PROMPT EXTERNO v11 – IDEOGRAM (BLOCO 1)

Ilustração digital em estilo Disney/Pixar 3D, colorida e vibrante, sem realismo fotográfico, sem aparência de foto, sem câmera real. Personagens devem ser objetos, ícones ou seres estilizados, no máximo 25% humanos, com rostos simples e simpáticos (olhos, boca, expressões suaves). Nada de pele humana realista ou proporções humanas realistas.

CENÁRIO / AMBIENTE (APENAS VISUAL, NÃO COMO TEXTO):
Representar o ambiente chamado **{AMBIENTE_NOME}** apenas de forma visual, sem escrever esse nome em nenhum lugar da imagem. Usar a seguinte descrição como guia visual:
{AMBIENTE_DESCRICAO}
Esse cenário deve ocupar cerca de 70–80% da imagem, criando profundidade, camadas e sensação de mundo vivo, mas sem atrapalhar a leitura do texto.

CLIMA E EASTER EGGS:
– Inserir detalhes que transmitam o clima de produtividade leve, organização e fluxo de tarefas (ex.: esteiras, funis, quadros de tarefas, post-its, caixinhas ou ícones de tarefas felizes, checklists, relógios de areia, etc.).
– Os elementos animados (caixas, tarefas, funil, metronomo, blocos de código, etc.) podem ter rostos simpáticos e pequenas expressões.
– Easter eggs devem ser sutis, nunca competir com o texto. O foco é sempre a frase do dia.

TEXTO PRINCIPAL (ÚNICO TEXTO IMPORTANTE NA IMAGEM):
Escrever exatamente o seguinte texto em português do Brasil, em três linhas, centralizado:

Linha 1 (banner superior, fonte grande):  
"{DATA_EXTENSO}"  

Linha 2 (logo abaixo da data, fonte menor):  
"{DIA_SEMANA}"  

Linha 3 (texto central, fonte do mesmo tamanho do número do dia, muito legível):  
"{FRASE_DIA}"

Regras importantes para o texto:
– O texto acima deve ser o **único** texto legível da imagem (além de pequenos detalhes como “Done” ou ícones muito discretos se necessário).  
– NÃO escrever o nome do ambiente ({AMBIENTE_NOME}) como texto em banner, título ou letreiro.  
– Garantir que a frase esteja perfeitamente legível, com bom contraste de cor entre texto e fundo.  
– Usar a mesma família de fonte para data e frase; a diferença é apenas o tamanho:  
  • Data (número do dia + nome do mês) e FRASE com tamanhos semelhantes.  
  • Dia da semana um pouco menor, como subtítulo.  

COMPOSIÇÃO:
– Banner superior estilizado (faixa, fita ou placa elegante) contendo a data na primeira linha e o dia da semana logo abaixo.  
– A frase deve ficar no centro da imagem, em destaque, não encostada nas bordas.  
– Os elementos do cenário devem “contar a história” da frase (por exemplo, funil que filtra tarefas, caminhos que simplificam escolhas, etc.), mas sem poluir a área de texto.  
– Manter um visual coerente com interfaces de dev/teste: kanban, pipelines, fluxos, esteiras, caixas que representam tasks, etc.  
– Sem bordas duras pretas de quadrinhos; preferir bordas suaves, luzes, brilhos e volumetria 3D.

ESTILO:
Disney/Pixar-style 3D illustration, cute, soft lighting, volumetric light, gradients suaves, cores vivas mas equilibradas, foco em clareza de leitura do texto. Nenhum realismo fotográfico, nenhuma textura de foto, nenhuma câmera ou lente real (sem “photo”, “photorealistic”, “cinematic shot”, etc.).
```

---

### Como preencher os placeholders

Antes de colar na Ideogram:

* `{DATA_EXTENSO}` → “5 de Fevereiro” (sem ano).
* `{DIA_SEMANA}` → “Quinta-feira”.
* `{FRASE_DIA}` → exatamente a frase que você definiu.
* `{AMBIENTE_NOME}` → nome curto do ambiente (ex.: “Jardins Suspensos de Órion”).
* `{AMBIENTE_DESCRICAO}` → 1–2 frases descrevendo o ambiente.

---

## 3. TEXTO FINAL PARA INSERIR NA IMAGEM (modelo)

Quando eu devolver o prompt já preenchido para um dia específico, o bloco “texto final” virá assim:

```markdown
TEXTO FINAL PARA INSERIR NA IMAGEM (v11)

{DATA_EXTENSO}
{DIA_SEMANA}
{FRASE_DIA}
```

Exemplo rápido para 05/02/2026:

```markdown
TEXTO FINAL PARA INSERIR NA IMAGEM (v11)

5 de Fevereiro
Quinta-feira
Reduzir excessos agora facilita suas escolhas depois.
```

---

## 4. Checklist v11 – Ideogram (para você revisar antes de gastar crédito de novo)

Use este checklist toda vez que a Ideogram gerar a imagem:

1. A **data** aparece em destaque no topo, no banner, escrita como “5 de Fevereiro” (sem ano).
2. O **dia da semana** aparece logo abaixo da data, menor (“Quinta-feira”).
3. A **frase do dia** está no centro da imagem, bem legível, com fonte de tamanho semelhante ao número do dia.
4. O **nome do ambiente** NÃO aparece escrito em nenhum lugar da imagem (aparece só visualmente como cenário).
5. Não há outros textos grandes concorrendo com a frase (no máximo pequenos detalhes tipo “Done”).
6. O estilo é claramente **cartoon Disney/Pixar**, sem realismo fotográfico, sem “foto”, sem pessoas humanas realistas.
7. O cenário combina a descrição do ambiente com o tema de dev/teste (tarefas, fluxo, organização, checklists, funis, etc.).

Se qualquer um dos itens 1–4 falhar, vale a pena refinar o prompt antes de gastar outro crédito.

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

