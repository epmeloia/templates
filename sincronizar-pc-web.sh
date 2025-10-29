# Comando em Lote para Syncrinizar PC WEB
cd /d/_GITHUB/templates
pwd
git status
git add .
echo "Digite a mensagem de commit:"
read COMMIT_MSG
git commit -m "$COMMIT_MSG"
git push
git pull
