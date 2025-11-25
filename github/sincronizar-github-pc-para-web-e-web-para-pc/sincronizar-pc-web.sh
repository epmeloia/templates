#!/bin/bash
# Gera nome do log com data e hora
DATA=$(date +"%Y-%m-%d")
HORA=$(date +"%Hh%Mm%Ss")
LOG="D:/_GITHUB/logs/LOG-PC-WEB-$DATA-$HORA.txt"

clear

{
echo
echo '# ------------------------------ #'
echo '#  INICIO DO SINCRONISMO PC-WEB  #'
echo '# ------------------------------ #'
echo
echo

echo
echo '# ------------------------------ #'
echo '# ->  cd /d/_GITHUB/templates <- #'
echo '# ------------------------------ #'
echo

cd /d/_GITHUB/templates

echo
echo '# --------- #'
echo '# -> pwd <- #'
echo '# --------- #'
echo

pwd

echo
echo '# ---------------- #'
echo '# -> git status <- #'
echo '# ---------------- #'
echo

git status


echo
echo '# --------------- #'
echo '# -> git add . <- #'
echo '# --------------- #'
echo

git add .


echo
echo '# ---------------------------- #'
echo '# -> git commit -m "Descr." <- #'
echo '# ---------------------------- #'
echo

git commit -m "Descr"


echo
echo '# -------------- #'
echo '# -> git push <- #'
echo '# -------------- #'
echo

git push


echo
echo '# -------------- #'
echo '# -> git pull <- #'
echo '# -------------- #'
echo

git pull


echo
echo '# ---------------- #'
echo '# -> git log -3 <- #'
echo '# ---------------- #'
echo

git log -3


echo
echo '# --------------------------- #'
echo '#  FIM DO SINCRONISMO PC-WEB  #'
echo '# --------------------------- #'
echo
} | tee "$LOG"

# Abre o arquivo de log no Notepad
powershell.exe Start-Process notepad++.exe "$LOG"
