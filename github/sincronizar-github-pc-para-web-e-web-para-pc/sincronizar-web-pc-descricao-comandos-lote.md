# Sincronizar - PC para WEB - Descricao dos Comando de Lote:
"sincronizar-pc-web-descricao-comandos-lote.md"

---

## **Execução Rápida - Instrução:**

### Copiar e Colar (Shift + INS)

```bash
sh /d/_GITHUB/templates/github/sincronizar-github-pc-para-web-e-web-para-pc/sincronizar-web-pc.sh
```

```bash
cd "/d/_GITHUB/templates/github/sincronizar-github-pc-para-web-e-web-para-pc/"
```

```bash
sh sincronizar-web-pc.sh
```

---

Segue um exemplo de script para sincronizar **da Web para o PC** (ou seja, baixar as mudanças do repositório remoto para sua máquina), inspirado pela estrutura, formatação e pausing do seu script atual:


**Explicação das etapas:**
- `git fetch` e `git pull` garantem que você baixe as atualizações do remoto para seu PC.
- O script mostra cada comando antes da execução, pausa para revisão e organiza visualmente como pedido.
- Você pode adicionar/remover comandos conforme sua necessidade!


```bash
##
## Comando em Lote para Syncrinizar WEB PC
##
## Versão com Commit Fixo
##
clear
echo
echo '# ------------------------------- #'
echo '# INICIO DO SINCRONISMO WEB-PC    #'
echo '# ------------------------------- #'
echo

echo '# -> cd /d/_GITHUB/templates <- #'
echo
cd /d/_GITHUB/templates
echo

echo '# -> pwd <- #'
echo
pwd
echo
read -p "Pressione ENTER para continuar..."
echo
clear

echo '# -> git status <- #'
echo
git status
echo
read -p "Pressione ENTER para continuar..."
echo

echo '# -> git fetch <- #'
echo
git fetch
echo
read -p "Pressione ENTER para continuar..."
echo

echo '# -> git pull <- #'
echo
git pull
echo
read -p "Pressione ENTER para continuar..."
echo

echo '# -> git log -3 <- #'
echo
git log -3
echo
read -p "Pressione ENTER para continuar..."
echo

echo '# ------------------------------- #'
echo '# FIM DO SINCRONISMO WEB-PC       #'
echo '# ------------------------------- #'
echo
echo
```
