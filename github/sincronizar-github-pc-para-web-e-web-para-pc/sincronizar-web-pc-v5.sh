#!/bin/bash
clear
echo
echo '# --------------------------------- #'
echo '#  INICIO DO SINCRONISMO WEB-PC v5  #'
echo '# --------------------------------- #'
echo

echo '# -> cd /d/_GITHUB/templates <- #'
cd /d/_GITHUB/templates
echo

echo '# -> pwd <- #'
pwd
echo

# Gera nome do log com data e hora
DATA=$(date +"%Y-%m-%d")
HORA=$(date +"%Hh%Mm%Ss")
LOG="D:/_GITHUB/logs/LOG-WEB-PC-$DATA-$HORA.txt"

{
echo '# -> git status <- #'
git status

echo '# -> git fetch <- #'
git fetch

echo '# -> git pull <- #'
git pull

echo '# -> git log -3 <- #'
git log -3


echo '# ------------------------------ #'
echo '#  FIM DO SINCRONISMO WEB-PC v5  #'
echo '# ------------------------------ #'
} | tee "$LOG"

# Abre o arquivo de log no Notepad
powershell.exe Start-Process notepad++.exe "$LOG"
