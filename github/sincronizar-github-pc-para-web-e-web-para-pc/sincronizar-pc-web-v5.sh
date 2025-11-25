#!/bin/bash
clear
echo
echo '# ------------------------------ #'
echo '#  INICIO DO SINCRONISMO PC-WEB  #'
echo '# ------------------------------ #'
echo

cd /d/_GITHUB/templates
echo
pwd
echo

# Gera nome do log com data e hora
DATA=$(date +"%Y-%m-%d")
HORA=$(date +"%Hh%Mm%Ss")
LOG="D:/_GITHUB/logs/LOG-PC-WEB-$DATA-$HORA.txt"

{
echo '# -> git status <- #'
git status

echo '# -> git add .'
git add .

echo '# -> git commit -m "Descr."'
git commit -m "Descr"

echo '# -> git push'
git push

echo '# -> git pull'
git pull

echo '# --------------------------- #'
echo '#  FIM DO SINCRONISMO PC-WEB  #'
echo '# --------------------------- #'
} | tee "$LOG"

# Abre o arquivo de log no Notepad
powershell.exe Start-Process notepad.exe "$LOG"
