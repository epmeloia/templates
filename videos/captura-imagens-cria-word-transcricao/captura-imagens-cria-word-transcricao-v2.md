# Captura Imagens e Cria Word com Transcricao
"captura-imagens-cria-word-transcricao-v2.md"

***
## **Como usar o roteiro (passo a passo)**

***

## 1. **Preparação**
- **Salve os Arquivos na Pasta,** `D:\_Captura_Imagens_Video\`
- **Salve o Codigo Python** em um arquivo, por exemplo, `Captura_Cria_Word_Video_Transcricao.py`.
- O vídeo (.mp4) e o arquivo de transcrição (.txt) devem estar em `D:\_Captura_Imagens_Video\`

1. 

***
2. **Instale como dependências** (se necessário):
```
 pip instalar python-docx travesseiro numpy opencv-python scikit-image
```
***
```
pip install python-docx pillow numpy opencv-python scikit-image
```

***
3. **Coloque o arquivo de vídeo (.mp4) e o arquivo de transcrição (.txt) na (formato timestamp + linha) em

```
D:\_Captura_Imagens_Video\
```

***
4. **Não execute nenhum terminal/cmd/PowerShell:**
```
python D:\_Captura_Imagens_Video\Captura_Cria_Word_Video_Transcricao.py
```
e responda os nomes.

```
python D:\_Captura_Imagens_Video\Captura_Cria_Word_Video_Transcricao.py
```

***
5. **Informe o nome do vídeo e do txt** quando solicitado.

***
6. **O Word gerado estará em `D:\_Captura_Imagens_Video\`** (nome Resumo_SeuVideo.docx), com texto e frames sincronizados.

***
7. **Script** (Captura_Cria_Word_Video_Transcricao.py) **COMENTÁRIO LINHA A LINHA**:

- As **funções são explicadas** antes de cada bloco.
- **Cada passo do fluxo** (ler transcrição, capturar frames, montar Word) está comentado.
- O script é para uso direto: **só preencher os arquivos na pasta BASE, rodar, responder nomes, e o Word sairá pronto**.

***
***

## 2. **Abra o Terminal/Prompt de Comando**
- Pressione `Win + R`, digite `cmd`, e pressione Enter; ou
- No menu iniciar, digite "cmd" ou "prompt".

## 3. **Navegue até a pasta**
Se o script estiver em `D:\_Captura_Imagens_Video\`, já está no lugar certo!  
Caso contrário, navegue até a pasta do script usando, por exemplo:
```
cd D:\_Captura_Imagens_Video\
```

## 4. **Execute o script**
Digite:
```
python Captura_Cria_Word_Video_Transcricao.py
```
(Se o arquivo tiver outro nome, troque pelo nome correto.)

## 5. **Responda os nomes solicitados**
- O script vai pedir:
  - Nome do vídeo (ex: `Video-003.mp4`)
  - Nome do arquivo de transcrição/legenda (ex: `Tutorial-Cities_Skyline-01.txt`)
- Digite E pressione Enter para cada um.

## 6. **Após rodar**
- O Word gerado estará na mesma pasta, com nome resumido e pronto para uso.
- As imagens estarão organizadas em subpastas, junto com o tutorial automático.

***

**Dúvidas? Só perguntar! O mesmo passo vale para qualquer .py do seu projeto.**










***
8. **Codificação Python:

```python
Segue o código completo atualizado com comentários detalhados, suporte ao seu formato (linha timestamp, linha texto):

```python
import os
from PIL import Image
import cv2
from docx import Document
from docx.shared import Inches
import re

BASE = r'D:\_Captura_Imagens_Video\\'  # Pasta base dos arquivos

# --- Converte de 'HH:MM:SS'/'HH:MM:SS,ms' para segundos float
def str_time_to_seconds(t: str):
    t = t.replace(",", ".")
    pats = re.findall(r"\d+", t)
    if len(pats) >= 3:
        h, m, s = int(pats[0]), int(pats[1]), float(pats[2])
        return h*3600 + m*60 + s
    else:
        return 0 

# --- Novo parser para TXT: timestamp em 1 linha, texto na linha seguinte
def parse_txt_transcricao(path):
    blocos = []
    with open(path, encoding="utf-8") as f:
        linhas = [l.strip() for l in f if l.strip()]
    i = 0
    while i < len(linhas):
        if re.match(r'\d{2}:\d{2}:\d{2}', linhas[i]):
            tempo = linhas[i]
            texto = linhas[i+1] if (i+1)<len(linhas) else ""
            ts = str_time_to_seconds(tempo)
            blocos.append((ts, texto))
            i += 2
        else:
            i += 1
    return blocos

# --- Captura até 5 frames: -2s, -1s, exato, +1s, +2s (quando disponíveis)
def extrair_5_frames(video_path, ts, save_dir, bloco_idx, tempo_total):
    cap = cv2.VideoCapture(video_path)
    frames = []
    nomes = []
    offsets = [-2, -1, 0, 1, 2]
    labels = ["antes2s", "antes1s", "central", "depois1s", "depois2s"]
    for i, (off, label) in enumerate(zip(offsets, labels)):
        target = ts + off
        if target < 0 or target > tempo_total:
            continue
        cap.set(cv2.CAP_PROP_POS_MSEC, target*1000)
        ret, frame = cap.read()
        if ret:
            img_name = f"frame_bloco{bloco_idx:03d}_{label}_{int(target)}s.jpg"
            img_path = os.path.join(save_dir, img_name)
            Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).save(img_path)
            frames.append(img_path)
            nomes.append(label)
    cap.release()
    return frames, nomes

def main():
    # --- Solicita nomes dos arquivos
    video_name = input("Nome do arquivo de vídeo (ex: Video-003.mp4): ").strip()
    txt_name = input("Nome do arquivo de transcrição (ex: Tutorial-Cities_Skyline-01.txt): ").strip()
    VIDEO = os.path.join(BASE, video_name)
    TXT = os.path.join(BASE, txt_name)
    # --- Cria pasta específica de frames por vídeo
    pasta_imgs = os.path.join(BASE, f"Imagens_{os.path.splitext(video_name)[0]}")
    os.makedirs(pasta_imgs, exist_ok=True)

    # --- Descobre a duração do vídeo em segundos
    cap = cv2.VideoCapture(VIDEO)
    tempo_total = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    # --- Lê todos os blocos (timestamp + texto) da transcrição
    blocos = parse_txt_transcricao(TXT)

    # --- Monta documento Word
    doc = Document()
    doc.add_heading(f"Tutorial: {video_name}", level=1)
    doc.add_paragraph(f"Arquivo de vídeo: {video_name}")
    doc.add_paragraph(f"Arquivo de transcrição: {txt_name}")

    for idx, (ts, texto) in enumerate(blocos):
        doc.add_heading(f"Bloco {idx+1} - {ts:.1f}s", level=2)
        doc.add_paragraph(texto)
        frames, labels = extrair_5_frames(VIDEO, ts, pasta_imgs, idx+1, tempo_total)
        for frame, label in zip(frames, labels):
            doc.add_paragraph(f"Frame {label}:")
            doc.add_picture(frame, width=Inches(3.2))

    word_name = os.path.join(BASE, f'Resumo_{os.path.splitext(video_name)[0]}.docx')
    doc.save(word_name)
    print(f"Word criado: {word_name}")

if __name__ == '__main__':
    main()
```

***
