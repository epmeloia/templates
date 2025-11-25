#!/bin/bash

clear
LOG="D:/_GITHUB/logs/LOG-PC-WEB-2025-11-25-00h29m11s.txt"

{
echo ""
echo "# ------------------------------ #"
echo "#  INICIO DO SINCRONISMO PC-WEB  #"
echo "# ------------------------------ #"
echo ""
echo "# -> cd /d/_GITHUB/templates <- #"
cd /d/_GITHUB/templates
echo ""
echo "# -> pwd <- #"
pwd
echo ""
echo ""
echo "# -> git status <- #"
git status
echo ""
echo "# -> git add ."
git add .
echo ""
echo "# -> git commit -m \"Descr.\""
git commit -m "Descr."
echo ""
echo "# -> git push"
git push
echo ""
echo "# -> git pull"
git pull
echo ""
echo ""
echo "# --------------------------- #"
echo "#  FIM DO SINCRONISMO PC-WEB  #"
echo "# --------------------------- #"
} | tee "$LOG"

# Aguarda leitura e exibe o log no final sem travar o terminal
echo ""
echo "Log salvo em: $LOG"
read -p "Pressione ENTER para visualizar o log..."

# Abre com notepad de forma isolada
powershell.exe Start-Process notepad.exe "$LOG"
