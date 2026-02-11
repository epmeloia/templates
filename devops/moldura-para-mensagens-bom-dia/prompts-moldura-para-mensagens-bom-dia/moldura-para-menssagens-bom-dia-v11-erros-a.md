# 📅🎨 Moldura para Menssagens de Bom Dia 🎨📅 - v11
Arquivo: `moldura-para-menssagens-bom-dia-v11.md`

## 1) Objetivo
Gerar imagens diarias no estilo “mensagem de bom dia” com:
- leitura imediata (texto muito legivel)
- estetica consistente (marca visual)
- variacao real (sem repetir cena, props, composicao, paleta ou “carinhas” iguais)
- interpretacao visual da frase (nao ilustrar literal demais, mas comunicar a ideia)

## 2) Entrada obrigatoria
O usuario sempre fornece:
- **Data** (ex: 29/12/2025)
- **Frase** (texto final)

E pode fornecer:
- tema (ano novo, fechamento de ciclo, disciplina, descanso, revisao, etc.)
- referencias de imagens (como as enviadas nesta sessao)

## 3) Estrutura fixa: Bloco 1 e Bloco 2
Regra permanente:
1. **Bloco 1** e um card principal de tamanho fixo e imutavel.
2. **Bloco 2** e um card separado, empilhado abaixo, secundario.
3. **Bloco 2** herda e harmoniza totalmente o estilo visual do Bloco 1, sem nunca interferir no layout estrutural do Bloco 1.

### 3.1) Bloco 1 (card principal)
Deve conter:
- faixa/banner superior com **Data** e opcionalmente **dia da semana** (banner sempre variado)
- **Frase** no corpo do card (texto principal)
- cena e personagens/objetos animados que reforcem a frase

### 3.2) Bloco 2 (card secundario, abaixo)
- aparece como continuacao do post (visual colado/harmonizado)
- pode conter detalhes extras (micro elementos, brilho, confete, textura suave)
- nunca “roubar” foco do Bloco 1
- nao pode alterar a estrutura do Bloco 1

## 4) Estilo visual oficial v11
### 4.1) Direcao de arte
- **visual mais alegre estilo Disney/Pixar**, com objetos animados carismaticos
- alta qualidade, acabamento “cinematografico leve”
- evitar hiper-realismo fotografico “duro” (pele humana realista, poros, etc.)

### 4.2) Regra de personagens
- **maximo 25% humanos**
- preferir objetos animados (cadernos, canecas, agendas, calendarios, lapis, plantas, etc.)
- expressoes amigaveis e limpas (nao assustadoras)

### 4.3) Fundo e movimento (regras novas)
- o fundo deve ocupar **75% do quadro geral** (com profundidade e narrativa)
- adicionar **50% mais ilusao de movimento** (vento em folhas, particulas, brilho, confete em trajetoria, reflexos, nevoa leve, fumaca de cafe, etc.)
- **o fundo da area onde fica o texto deve ter transparencia de 95%** (quase transparente), mantendo legibilidade maxima

### 4.4) Moldura
- cada imagem precisa de **uma moldura nova e unica**
- moldura pode ser sofisticada ou criativa, mas sempre com bom gosto
- moldura deve **destacar a frase** (nunca competir com ela)
- usar tecnicas tipo “outdoor” para texto: contraste alto, contorno leve, glow controlado, sombra suave quando necessario

## 5) Regras de variacao (anti repeticao)
Obrigatorio variar diariamente:
- composicao (angulo, distancia, enquadramento, perspectiva)
- ambiente (mudar local, epoca, clima, cultura, “vibe”)
- objetos principais (nao repetir o mesmo kit: caneca + agenda + lapis sempre igual)
- cor dominante e iluminacao (manter harmonia, mas alternar paleta)
- estilo de banner superior (formato, textura, ornamentos, tipografia)

Proibido:
- “copiar e colar” a mesma cena com pequenas mudancas
- repetir a mesma moldura ou moldura muito parecida
- repetir o mesmo set de personagens com as mesmas poses
- repetir a mesma “janela com luz dourada” como padrao fixo (pode aparecer as vezes, mas nao virar template)

## 6) Ambientes (fonte oficial)
Para o fundo, usar a lista:
- `/mnt/data/ambientes-locais-para-temas-frases-dia-v1.md`

Regra:
- escolher 1 ambiente principal por dia
- adaptar o ambiente ao significado da frase (ex: revisao = escritorio acolhedor; recomeço = porta aberta; consistencia = oficina/planejamento; etc.)
- misturar locais reais + ficticios + astronomicos para dar variedade

## 7) Texto e tipografia
- frase com **tamanho medio** (nao micro, nao gigante)
- priorizar legibilidade em celular
- evitar fontes “finas demais”
- garantir contraste com o fundo (area do texto com transparencia 95% quando necessario)
- **controle de ortografia**:
  - se houver risco de erro na imagem, trocar por sinonimo mais seguro
  - se a frase tiver acentos e houver chance de a imagem “errar”, preferir alternativa sem acento (somente se isso nao deturpar o sentido)

## 8) Fluxo de trabalho (operacional)
### 8.1) Pre visualizacao (texto)
Quando o usuario mandar:
[OBS] BLOCO 1
[EXEC] pre-visualizacao do Bloco 1
Data: dd/mm/aaaa
"Frase ..."

O assistente deve responder com:
- uma confirmacao objetiva do que sera gerado (tema + elementos + ambiente + estilo do banner)
- e terminar com:
**[EXEC] Confirmacao Final para gerar o Bloco 1**

### 8.2) Geracao de imagem
Apos o usuario confirmar, gerar a imagem final do Bloco 1 (e Bloco 2 se solicitado).

## 9) Correcao: realismo excessivo e repeticao (prompt oficial)
Quando o resultado estiver “realista demais” ou repetitivo, aplicar as regras abaixo (fonte oficial):
- `/mnt/data/prompt-para-correcao-realismo-excessivo-repeticao-visual-da-v11.md`

Resumo pratico do que corrigir:
- reduzir realismo fotografico e deixar mais “ilustracao premium”
- reforcar bordas e leitura do texto (sem poluir)
- variar props e layout (nao reciclar set)
- variar paleta, luz, angulo, distancia
- manter personagens consistentes dentro do dia, mas nao iguais em todos os dias

## 10) Referencias desta sessao (imagens encaminhadas)
Usar como referencia de continuidade e criterio de qualidade:
- `/mnt/data/2025-12-29.png`
- `/mnt/data/2025-12-30.png`
- `/mnt/data/2025-12-31.png`
- `/mnt/data/2026-01-02.png`

Regra:
- nao copiar exatamente
- usar como “nivel de acabamento” e “padrao de legibilidade”
- garantir variacao real

## 11) Checklist QA (antes de entregar)
- data correta
- frase correta (sem erros)
- texto legivel em celular
- moldura unica e bonita
- fundo 75% do quadro com narrativa
- area do texto com transparencia 95% (quando houver placa/faixa)
- 50% mais ilusao de movimento presente
- variacao real vs ontem (ambiente, props, composicao)
- personagens no maximo 25% humanos

## 12) Arquivos de apoio (fonte soberana desta v11)
- `/mnt/data/moldura-para-menssagens-bom-dia-v10.md` (base anterior)
- `/mnt/data/prompt-para-correcao-realismo-excessivo-repeticao-visual-da-v11.md` (correcao v11)
- `/mnt/data/ambientes-locais-para-temas-frases-dia-v1.md` (ambientes)
- `/mnt/data/prompt-clonagem-continuidade-v10.2.md` (continuidade)
- `/mnt/data/continuity-backup.md` (backup)
- `/mnt/data/changelog-v10-v11-copia-cola-chat-ate-2026-01-05.md` (historico)
