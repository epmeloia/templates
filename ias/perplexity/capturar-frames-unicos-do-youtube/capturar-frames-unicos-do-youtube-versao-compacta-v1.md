# 🧩 Capturar Frames Únicos do YouTube - Versao Compacta
"capturar-frames-unicos-do-youtube-versao-compacta-v1.md"

# 1) versão **compacta** (comando único)

> **Objetivo**: gerar um script completo que baixe um vídeo do YouTube, extraia frames a cada 5s e salve apenas os que forem **SSIM < 0,75** em relação ao último frame aceito.
> **Tarefas da IA**:

```text
1. Entregar **código Python executável** (com `yt-dlp` ou `pytube`, `opencv-python`, `scikit-image`), pedindo a URL do YouTube em `input()` e salvando em `frames_unicos/` com nomes `frame_001.jpg` etc.
2. Registrar `timestamp`, `similaridade` e `arquivo` em `frames_unicos/log.json`.
3. Incluir **passo a passo de instalação** (`pip install yt-dlp opencv-python scikit-image`) e execução.
4. Oferecer **alternativa com FFmpeg** (script bash) usando análise por cena e explicando limitações vs SSIM.
5. Parâmetros ajustáveis no início do código: `intervalo_segundos=5`, `limiar_similaridade=0.75`.
6. Otimizações de desempenho: leitura por **seeks** a cada 5s, conversão para escala de cinza antes de SSIM.
   **Saída esperada**:
* 1 bloco de **código Python** completo;
* 1 bloco de **script FFmpeg** alternativo;
* instruções curtas e claras;
* aviso sobre direitos autorais e uso justo.
  **Faça agora**.
```

---

# 2) versão **visual e multimodal** (thumbnails, colagem e painel)

> **Contexto**: Atue como um engenheiro de visão computacional criando um **pipeline visual** completo, pronto para uso local, que:
>
> * Baixa o vídeo do YouTube;
> * Extrai frames a cada 5s;
> * Mantém apenas frames com **SSIM < 0,75** vs último frame aceito;
> * Gera **artefatos visuais e um painel HTML** para inspeção.
>
> **Entregáveis obrigatórios** (gerar tudo com código pronto):
>
> 1. **Script Python principal** (com `yt-dlp`/`pytube`, `opencv-python`, `scikit-image`, `numpy`, `Pillow`):
>
>    * Entrada: URL do YouTube (`input()`).
>    * Parâmetros no topo: `intervalo_segundos=5`, `limiar_similaridade=0.75`.
>    * Saídas:
>
>      * pasta `frames_unicos/` com `frame_001.jpg`…
>      * `frames_unicos/log.json` e `frames_unicos/log.csv` (timestamp, similaridade, nome_arquivo).
> 2. **Geração de thumbnails**: criar também `thumbs/` com versões 320px de largura para navegação rápida.
> 3. **Contato visual (collage)**: montar automaticamente uma **grade** (`contact_sheet.jpg`) com 4–6 colunas, legendo cada tile com o timestamp (use Pillow).
> 4. **Painel HTML estático**: produzir `index.html` dentro de `frames_unicos/` listando:
>
>    * galeria de thumbs clicáveis;
>    * tabela com timestamp/similaridade/arquivo (carregando `log.json` via `<script>`);
>    * pequena barra de busca por faixa de tempo;
>    * link para baixar o `.zip` (criar o `.zip` via Python).
> 5. **Script de alternativa com FFmpeg**: bloco que mostre extração a cada 5s e uma segunda opção com detecção de cena (`-vf "select='gt(scene,0.3)'"`) + explicação de prós/contras vs SSIM.
> 6. **Seções no final da resposta**:
>
>    * “Como instalar e rodar” (com `pip install ...` e comandos).
>    * “Ajustes finos” (ex.: quando aumentar/diminuir limiar; nota sobre vídeos com cortes rápidos).
>    * “Limitações e notas legais”.
>
> **Formato da resposta**:
>
> * 1 bloco de **código Python** autocontido que cria pastas, baixa vídeo, extrai frames, calcula SSIM, gera thumbs, monta collage, cria `index.html` e o `.zip`.
> * 1 bloco com **comandos FFmpeg** alternativos.
> * 1 seção curta com instruções, outra com ajustes, outra com limitações.
>
> **Faça agora** e valide que os caminhos/nomes de arquivos batem com o que foi descrito.

---

se quiser, eu também posso te entregar **uma terceira versão** em **Node.js** (usando `yt-dlp`, `ffmpeg` e `sharp`) — é só pedir. 😉

**E qual prompt eu devo melhorar a seguir?**
