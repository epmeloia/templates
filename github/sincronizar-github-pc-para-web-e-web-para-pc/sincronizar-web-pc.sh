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

echo '# -> cd /d/_GITHUB/templates/github/sincronizar-github-pc-para-web-e-web-para-pc/ <- #'
echo
cd /d/_GITHUB/templates/github/sincronizar-github-pc-para-web-e-web-para-pc/
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
