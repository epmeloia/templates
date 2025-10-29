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
echo '# INICIO DO SINCRONISMO PC-WEB #'
echo '# ---------------------------- #'
echo
echo '# -> cd /d/_GITHUB/templates <-#'
cd /d/_GITHUB/templates
echo

echo 'pwd'
pwd
echo
read -p "Pressione ENTER para continuar..."
echo

echo 'git status'
git status
echo
read -p "Pressione ENTER para continuar..."
echo

echo 'git add .'
git add .
echo
read -p "Pressione ENTER para continuar..."
echo

echo 'git commit -m "Descr."'
git commit -m "Descr"
echo
echo 'git push'
git push
echo
read -p "Pressione ENTER para continuar..."
echo

echo 'git pull'
git pull
echo
echo
echo 'FIM DO SINCRONISMO PC-WEB'
echo
echo
