import os, csv, json
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim
import cv2
from yt_dlp import YoutubeDL

# ======= CONFIGURAÇÕES =======
INTERVALO_SEGUNDOS = 5
LIMIAR_SALVAR = 0.75   # Aceita novo frame se SSIM<limiar com último salvo
LIMIAR_CLUST = 0.85    # Limite SSIM para AGRUPAR como mesma estrutura

# ---->>> Defina aqui o caminho completo desejado:
PASTA = r'D:\_Captura_Imagens_Video\Imagens_001\\'
os.makedirs(PASTA, exist_ok=True)

URL = input("URL do vídeo: ").strip()

# ======= DOWNLOAD DO VÍDEO =======
def baixar_video(url):
    ydl_opts = {'outtmpl': os.path.join(PASTA,'video.%(ext)s'), 'format': 'bestvideo+bestaudio/best'}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)
VIDEO = baixar_video(URL)

# ======= EXTRAÇÃO DE FRAMES ÚNICOS =======
def extrair_e_filtrar(video, intervalo, limiar, pasta):
    cap = cv2.VideoCapture(video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    tot_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = tot_frames / fps if fps else 0
    logs = []
    last_img = None
    t = 0
    idx = 1
    while t < duration:
        cap.set(cv2.CAP_PROP_POS_MSEC, t*1000)
        ret, frame = cap.read()
        if not ret: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        sim = 0 if last_img is None else ssim(last_img, gray)
        if (last_img is None) or (sim < limiar):
            fname = f"frame_{idx:03}.jpg"
            Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).save(os.path.join(pasta, fname))
            logs.append({'idx': idx, 'arquivo': fname, 'timestamp': t, 'similaridade_com_ultimo': float(sim)})
            last_img = gray
            idx += 1
        t += intervalo
    cap.release()
    with open(os.path.join(pasta,"log.json"),"w",encoding="utf8") as f:
        json.dump(logs, f, indent=2)
    return logs

logs = extrair_e_filtrar(VIDEO, INTERVALO_SEGUNDOS, LIMIAR_SALVAR, PASTA)
arqs = [l['arquivo'] for l in logs]

# ======= CLUSTERIZAÇÃO DOS FRAMES ÚNICOS =======
def load_gray(path):
    return np.array(Image.open(path).convert('L'))
def clusterizar(imgs, folder, limiar):
    grupos = []
    usados = set()
    for i in range(len(imgs)):
        if i in usados:
            continue
        grupo = [i]
        usados.add(i)
        img_i = load_gray(os.path.join(folder, imgs[i]))
        for j in range(i+1,len(imgs)):
            if j in usados: continue
            img_j = load_gray(os.path.join(folder, imgs[j]))
            sim = ssim(img_i, img_j)
            if sim >= limiar:
                grupo.append(j)
                usados.add(j)
        grupos.append(grupo)
    return grupos

clusters = clusterizar(arqs, PASTA, LIMIAR_CLUST)

# ======= RELATÓRIO =======
with open(os.path.join(PASTA,"cluster_report.csv"),'w',newline="",encoding="utf8") as f:
    cw = csv.writer(f)
    cw.writerow(["arquivo","timestamp","grupo"])
    for g_idx, grupo in enumerate(clusters):
        for idx in grupo:
            cw.writerow([arqs[idx], logs[idx]['timestamp'], g_idx+1])
print(f"Total de estruturas diferentes (grupos): {len(clusters)}")
print("Veja 'cluster_report.csv' em D:\\_Captura_Imagens_Video\\Imagens_001\\ para agrupamento de estruturas!")
