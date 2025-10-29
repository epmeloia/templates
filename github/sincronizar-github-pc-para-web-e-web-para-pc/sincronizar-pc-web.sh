##
## Comando em Lote para Syncrinizar PC WEB
##
## Versão com Commit Variavel
##
# cd /d/_GITHUB/templates
# pwd
# git status
# git add .
## echo "Digite a mensagem de commit:"
# read COMMIT_MSG
# git commit -m "$COMMIT_MSG"
#git push
#git pull
#
##
## Versão com Commit Fixo
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
pwd
echo
echo
read -p "Pressione ENTER para continuar..."
echo
echo
echo '# -> git status <- #'
echo
git status
echo
read -p "Pressione ENTER para continuar..."
echo
echo
echo '# -> git add .'
echo
git add .
echo
echo
echo
echo '# -> git commit -m "Descr."'
echo
git commit -m "Descr"
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
echo
