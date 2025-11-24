#!/bin/bash

# Gera data e hora
DATA=$(date +%Y-%m-%d)
HORA=$(date +%Hh%Mm%Ss)
LOG="LOG-WEB-PC-$DATA-$HORA.txt"

# Cria pasta de logs se não existir
mkdir -p /d/_GITHUB/logs

# Redireciona toda a execução para o log
exec > "/d/_GITHUB/logs/$LOG" 2>&1

echo
echo '# ------------------------------- #'
echo '# INICIO DO SINCRONISMO WEB-PC    #'
echo '# ------------------------------- #'
echo

echo '# -> cd /d/_GITHUB/templates <- #'
cd /d/_GITHUB/templates || exit
echo

echo '# -> pwd <- #'
pwd
echo

echo '# -> git status <- #'
git status
echo

echo '# -> git fetch <- #'
git fetch
echo

echo '# -> git pull <- #'
git pull
echo

echo '# -> git log -3 <- #'
git log -3
echo

echo '# ------------------------------- #'
echo '# FIM DO SINCRONISMO WEB-PC       #'
echo '# ------------------------------- #'
