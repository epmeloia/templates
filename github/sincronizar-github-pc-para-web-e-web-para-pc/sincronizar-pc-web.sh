##
## Comando em Lote para Syncrinizar PC WEB
##
## Versão com Commit Variavel
##
#!/bin/bash

# Gera data e hora
DATA=$(date +%Y-%m-%d)
HORA=$(date +%Hh%Mm%Ss)
LOG="LOG-PC-WEB-$DATA-$HORA.txt"

# Cria pasta de logs se não existir
mkdir -p /d/_GITHUB/logs

# Redireciona toda a execução para o log
exec > "/d/_GITHUB/logs/$LOG" 2>&1

echo
echo '# ------------------------------ #'
echo '#  INICIO DO SINCRONISMO PC-WEB  #'
echo '# ------------------------------ #'
echo
echo

echo '# -> cd /d/_GITHUB/templates <- #'
cd /d/_GITHUB/templates || exit
echo
echo

echo '# -> pwd <- #'
pwd
echo
echo

echo '# -> git status <- #'
git status
echo
echo

echo '# -> git add .'
git add .
echo
echo

echo '# -> git commit -m "Descr."'
git commit -m "Descr"
echo
echo

echo '# -> git push'
git push
echo
echo

echo '# -> git pull <- #'
git pull
echo
echo

echo '# -> git log -3 <- #'
git log -3
echo
echo

cmd.exe /C "start notepad.exe $LOG"

echo
echo '# --------------------------- #'
echo '#  FIM DO SINCRONISMO PC-WEB  #'
echo '# --------------------------- #'
echo
echo
