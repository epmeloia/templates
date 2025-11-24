##
## Comando em Lote para Syncrinizar PC WEB
##
## Versão com Commit Variavel
##
clear
echo
echo '# ------------------------------ #'
echo '#  INICIO DO SINCRONISMO PC-WEB  #'
echo '# ------------------------------ #'
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

echo '# -> git add .'
echo
git add .
echo
echo

echo '# -> git commit -m "Descr."'
echo
git commit -m "Descr"
echo
echo

read -p "Pressione ENTER para continuar..."
echo
echo

echo '# -> git push'
echo
git push
echo

read -p "Pressione ENTER para continuar..."
echo
echo

echo '# -> git pull'
echo
git pull
echo
echo

echo
echo '# --------------------------- #'
echo '#  FIM DO SINCRONISMO PC-WEB  #'
echo '# --------------------------- #'
echo
echo
