# Script para gerar index.md e README.md automaticamente com base na estrutura do repositório
import os
from datetime import datetime

ROOT_DIR = "D:/_GITHUB/templates"
DOCS_DIR = os.path.join(ROOT_DIR, "docs")

# Caminhos dos arquivos de saída
index_path = os.path.join(DOCS_DIR, "index.md")
readme_path = os.path.join(DOCS_DIR, "README.md")

# Cabeçalho e introdução
HEADER = """# Portal de Ideias, Instruções e Recursos 🚀

Este repositório é um hub central com coleções de manuais, testes, glossários, códigos, prompts e soluções para uso prático.

**Gerado automaticamente em:** {data}

## Seções Disponíveis
"""

# Gera links para subdiretórios com README.md
def gerar_estrutura():
    blocos = []
    for pasta_atual, subpastas, arquivos in os.walk(ROOT_DIR):
        if 'README.md' in arquivos and pasta_atual != ROOT_DIR:
            rel = os.path.relpath(pasta_atual, ROOT_DIR).replace("\\", "/")
            titulo = rel.split("/")[-1].capitalize().replace("-", " ")
            link = f"[{rel}](../{rel}/README.md)"
            blocos.append(f"- 📂 {titulo}: {link}")
    return "\n".join(sorted(blocos))

# Conteúdo final com data atual
conteudo = HEADER.format(data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
conteudo += "\n" + gerar_estrutura()

# Salva em ambos os arquivos
with open(index_path, "w", encoding="utf-8") as idx:
    idx.write(conteudo)

with open(readme_path, "w", encoding="utf-8") as rdm:
    rdm.write(conteudo)

print("index.md e README.md atualizados com sucesso.")
