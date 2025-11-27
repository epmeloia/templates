##
## Comando em Lote para Syncrinizar WEB PC
##
## Versão com Commit Fixo
##
clear
echo
echo '# --------------------------------- #'
echo '#  INICIO DO SINCRONISMO WEB-PC v1  #'
echo '# --------------------------------- #'
echo

echo '# -> cd /d/_GITHUB/templates <- #'
echo
cd /d/_GITHUB/templates
echo

echo '# -> pwd <- #'
echo
pwd
echo

echo
read -p "Pressione ENTER para continuar..."
echo

clear

echo
echo

echo '# -> git status <- #'
echo
git status
echo

echo
read -p "Pressione ENTER para continuar..."
echo
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
echo

echo '# -> git log -3 <- #'
echo
echo

git log -3
echo
echo

read -p "Pressione ENTER para continuar..."
echo
echo

echo '# ----------------------------- #'
echo '# FIM DO SINCRONISMO WEB-PC v1  #'
echo '# ----------------------------- #'
echo
echo
