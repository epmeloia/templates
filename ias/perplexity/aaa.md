# 🧠 Prompt para o Perplexity PRO

capturar-frames-unicos-do-youtube-v1.md

- 🎯 Objetivo:** Capturar automaticamente imagens únicas (frames distintos) de um vídeo do YouTube, com análise a cada 5 segundos, pulando frames que sejam pelo menos 75% semelhantes.

---

### 🧩 Contexto

Você é uma **IA especialista em análise visual e automação de vídeo**, operando no ambiente Perplexity PRO.
Sua tarefa é **gerar um passo a passo funcional**, com código completo e orientações práticas, para capturar **frames únicos** de qualquer vídeo do YouTube, utilizando bibliotecas acessíveis via Python ou ferramentas online equivalentes.

---

### ⚙️ Instruções Detalhadas

1. **Baixe o vídeo do YouTube**

   * Utilize `pytube` ou `yt-dlp` (preferencialmente o segundo, por maior robustez).
   * Permita que o usuário insira o link do vídeo.
   * Armazene localmente como `video.mp4`.

2. **Análise temporal**

   * Avalie o vídeo a cada **5 segundos** de intervalo (`intervalo_segundos = 5`).
   * Extraia um frame nesses intervalos utilizando **OpenCV**.

3. **Comparação de frames**

   * Compare cada novo frame com o último frame salvo.
   * Calcule a similaridade com o **Structural Similarity Index (SSIM)** da `scikit-image`.
   * Se a similaridade for **≥ 0.75**, ignore o frame.
   * Caso contrário, salve o frame.

4. **Exportação**

   * Crie uma pasta `frames_unicos/`.
   * Salve as imagens com o formato `frame_001.jpg`, `frame_002.jpg`, etc.
   * Gere também um arquivo `log.json` contendo:

     * Timestamp do frame
     * Nível de diferença
     * Nome do arquivo salvo

5. **O resultado final deve incluir:**

   * O código completo em Python pronto para execução.
   * Instruções passo a passo de uso (como rodar, dependências etc.).
   * Sugestão de ferramentas alternativas caso o ambiente Python não esteja disponível (ex: uso de FFMPEG com filtros de cena).

---

### 💻 Exemplo de Saída Esperada (Perplexity deve gerar algo como):

```python
# Código completo em Python
# Objetivo: extrair frames únicos de um vídeo do YouTube
from pytube import YouTube
import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as ssim
import json

# Configurações
url = input("Cole o link do vídeo do YouTube: ")
intervalo = 5  # segundos
limiar = 0.75

# Download do vídeo
yt = YouTube(url)
stream = yt.streams.filter(file_extension='mp4', res='720p').first()
video_path = stream.download(filename='video.mp4')

# Processamento
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps * intervalo)
output_dir = "frames_unicos"
os.makedirs(output_dir, exist_ok=True)

last_frame = None
count = 0
saved = 0
log_data = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if count % frame_interval == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if last_frame is not None:
            similarity = ssim(last_frame, gray)
            if similarity < limiar:
                filename = f"{output_dir}/frame_{saved:03d}.jpg"
                cv2.imwrite(filename, frame)
                timestamp = count / fps
                log_data.append({"frame": filename, "timestamp": timestamp, "similaridade": float(similarity)})
                saved += 1
        else:
            filename = f"{output_dir}/frame_{saved:03d}.jpg"
            cv2.imwrite(filename, frame)
            timestamp = count / fps
            log_data.append({"frame": filename, "timestamp": timestamp, "similaridade": 1.0})
            saved += 1
        last_frame = gray
    count += 1

cap.release()

with open("frames_unicos/log.json", "w") as f:
    json.dump(log_data, f, indent=4)

print(f"{saved} frames únicos salvos em '{output_dir}'")
```

---

### 🧠 Sugestões criativas (que Perplexity pode incluir)

* 💡 **Versão em Node.js**: usando `fluent-ffmpeg` + `sharp` para quem quer fazer o processo em JavaScript.
* 🧩 **Modo sem código**: usando ferramentas como [shotstack.io](https://shotstack.io) ou [ffmpeg.wasm](https://ffmpegwasm.netlify.app/) para processar diretamente no navegador.
* 📸 **Análise avançada**: incluir detecção de “mudanças de cena” via `cv2.absdiff()` e histograma RGB.

---

### ✅ Resultado Esperado do Perplexity

Quando colar este prompt no Perplexity PRO, a IA deverá:

* Gerar um **script completo** pronto para execução.
* Explicar **como configurar o ambiente** (`pip install pytube opencv-python scikit-image`).
* Fornecer **alternativas sem Python** (ex: ffmpeg + bash script).
* Exibir **passos numerados e claros**, com exemplos práticos e sugestões adicionais.

---

🧩 **Resumo curto para colar diretamente no Perplexity PRO (modo rápido):**

> Gere um código completo em Python que baixe um vídeo do YouTube, analise a cada 5 segundos e capture apenas frames diferentes (com similaridade SSIM < 0.75).
> Salve os frames em uma pasta e crie um log JSON com timestamps.
> Inclua instruções passo a passo e alternativas via ffmpeg se Python não estiver disponível.

---
