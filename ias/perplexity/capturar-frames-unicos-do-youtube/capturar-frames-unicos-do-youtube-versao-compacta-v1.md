# 🧩 Capturar Frames Únicos do YouTube - Versao Compacta
"capturar-frames-unicos-do-youtube-versao-compacta-v1.md"

# Versão **compacta** (comando único)

```text
**Objetivo**: gerar um script completo que baixe um vídeo do YouTube, extraia frames a cada 5s e salve apenas os que forem **SSIM < 0,75** em relação ao último frame aceito.
**Tarefas da IA**:

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
