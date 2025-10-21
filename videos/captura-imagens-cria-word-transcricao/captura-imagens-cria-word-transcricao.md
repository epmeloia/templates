# Captura Imagens e Cria Word com Transcricao
"captura-imagens-cria-word-transcricao.md"

***
## **Como usar o roteiro (passo a passo)**

1. **Salve o Codigo Python** em um arquivo, por exemplo, `Captura_Cria_Word_Video_Transcricao.py`.
```
```

2. **Instale como dependências** (se necessário):
```
 pip instalar python-docx travesseiro numpy opencv-python scikit-image
```

3. **Coloque o arquivo de vídeo (.mp4) e o arquivo de transcrição (.txt) na massa:** 
```
D:\_Captura_Imagens_Vídeo\
```

4. **Não execute nenhum terminal/cmd/PowerShell:**
```
python D:\_Captura_Imagens_Vídeo\Captura_Cria_Word_Video_Transcricao.py
```

5. **Informe o nome do vídeo e do txt** quando solicitado.
```
```

6. **O tutorial em Word (.docx) será gerado na massa média**, com imagens e texto sincronizados.
```
```
***

7. **Script** (Captura_Cria_Word_Video_Transcricao.py) **COMENTÁRIO LINHA A LINHA**:

- As **funções são explicadas** antes de cada bloco.
- **Cada passo do fluxo** (ler transcrição, capturar frames, montar Word) está comentado.
- O script é para uso direto: **só preencher os arquivos na pasta BASE, rodar, responder nomes, e o Word sairá pronto**.

8. **Codificação Python:

```python
import os
from PIL import Image
from skimage.metrics import structural_similarity as ssim  # (aqui não será usado, mas você pode remover se desejar)
import cv2
from docx import Document
from docx.shared import Inches
import re

BASE = r'D:\_Captura_Imagens_Video\\'  # Pasta base onde estarão os arquivos

# --- Função para converter tempo no formato HH:MM:SS(.ms) para segundos float
def str_time_to_seconds(t: str):
    t = t.replace(",", ".")
    pats = re.findall(r"\d+", t)          # Extrai partes numéricas
    if len(pats) >= 3:                    # Espera pelo menos três grupos (hora, min, seg)
        h, m, s = int(pats[0]), int(pats[1]), float(pats[2])
        return h*3600 + m*60 + s
    else:
        return 0 

# --- Função para ler transcrição TXT: cada linha deve começar com tempo ("00:01:23 Texto do bloco")
def parse_txt_transcricao(path):
    blocos = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if re.match(r'\d{2}:\d{2}:\d{2}', line):    # Detecta linha de timestamp
                parte = line.split(' ', 1)
                tempo = parte[0]
                texto = parte[1] if len(parte) > 1 else ""
                ts = str_time_to_seconds(tempo)         # Converte tempo para segundos
                blocos.append((ts, texto))              # Adiciona par (tempo, texto)
    return blocos

# --- Função que captura até 5 frames em torno do timestamp, respeitando início/fim
def extrair_5_frames(video_path, ts, save_dir, bloco_idx, tempo_total):
    cap = cv2.VideoCapture(video_path)
    frames = []
    nomes = []
    offsets = [-2, -1, 0, 1, 2]                 # Offset: segundos antes/depois
    labels = ["antes2s", "antes1s", "central", "depois1s", "depois2s"]
    for i, (off, label) in enumerate(zip(offsets, labels)):
        target = ts + off                       # Tempo alvo
        if target < 0 or target > tempo_total:  # Não captura antes de 0s ou além do fim do video
            continue
        cap.set(cv2.CAP_PROP_POS_MSEC, target*1000)
        ret, frame = cap.read()
        if ret:
            img_name = f"frame_bloco{bloco_idx:03d}_{label}_{int(target)}s.jpg"
            img_path = os.path.join(save_dir, img_name)
            # Salva como imagem colorida (RGB)
            Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).save(img_path)
            frames.append(img_path)
            nomes.append(label)
    cap.release()
    return frames, nomes

def main():
    # --- Pergunta os nomes dos arquivos (já precisam estar na pasta BASE)
    video_name = input("Nome do arquivo de vídeo (ex: Video-003.mp4): ").strip()
    txt_name = input("Nome do arquivo de transcrição (ex: Tutorial-Cities_Skyline-01.txt): ").strip()
    VIDEO = os.path.join(BASE, video_name)
    TXT = os.path.join(BASE, txt_name)
    # --- Cria pasta para as imagens, uma para cada vídeo
    pasta_imgs = os.path.join(BASE, f"Imagens_{os.path.splitext(video_name)[0]}")
    os.makedirs(pasta_imgs, exist_ok=True)

    # --- Descobre a duração total do vídeo em segundos
    cap = cv2.VideoCapture(VIDEO)
    tempo_total = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    # --- Lê blocos da transcrição txt
    blocos = parse_txt_transcricao(TXT)

    # --- Inicia o documento do Word
    doc = Document()
    doc.add_heading(f"Tutorial: {video_name}", level=1)
    doc.add_paragraph(f"Arquivo de vídeo: {video_name}")
    doc.add_paragraph(f"Arquivo de transcrição: {txt_name}")

    # --- Para cada bloco/linha de tempo+texto da transcrição:
    for idx, (ts, texto) in enumerate(blocos):
        doc.add_heading(f"Bloco {idx+1} - {ts:.1f}s", level=2)
        doc.add_paragraph(texto)
        # Captura até 5 frames para cada bloco, só se existirem
        frames, labels = extrair_5_frames(VIDEO, ts, pasta_imgs, idx+1, tempo_total)
        for frame, label in zip(frames, labels):
            doc.add_paragraph(f"Frame {label}:")
            # Adiciona imagem ao Word, largura ~8cm
            doc.add_picture(frame, width=Inches(3.2))

    # --- Salva o arquivo Word final
    word_name = os.path.join(BASE, f'Resumo_{os.path.splitext(video_name)[0]}.docx')
    doc.save(word_name)
    print(f"Word criado: {word_name}")

if __name__ == '__main__':
    main()

```

***
