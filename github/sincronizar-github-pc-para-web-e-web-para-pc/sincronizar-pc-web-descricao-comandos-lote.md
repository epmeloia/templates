# Sincronizar - PC para WEB - Descricao dos Comando de Lote:
"sincronizar-pc-web-descricao-comandos-lote.md"

---

## **Execução Rápida - Instrução:**
```bash
cd "/d/_GITHUB/templates/github/sincronizar-github-pc-para-web-e-web-para-pc/"
```

```bash
sh sincronizar-pc-web.sh
```

---

**Instrução:**
- Crie um arquivo chamado `sincronizar.sh` (ou outro nome de sua preferência) e insira os comandos (um em cada linha) que você normalmente executa no terminal.

**Como fazer:**
1. Abra um editor (pode ser Notepad++ ou VSCode).
2. Cole o seguinte exemplo, adaptando os comandos conforme sua rotina e pastas:

```bash
cd /d/_GITHUB/templates
pwd
git status
git add .
git commit -m "Descr"
git push
git pull
```

3. Salve o arquivo com extensão `.sh`, exemplo: `sincronizar.sh`.

4. No terminal Git Bash, navegue até a pasta onde o script está salvo usando `cd`.

5. Execute o arquivo com o comando:
```bash
sh sincronizar.sh
```
Ou, se quiser tornar o script executável:
```bash
chmod +x sincronizar.sh
./sincronizar.sh
```

**Dicas:**
- Você pode incluir comentários no arquivo iniciando a linha com `#`.
- Se quiser interatividade (ex: informar a mensagem do commit), pode usar `read` para pedir entrada do usuário, por exemplo:
```bash
echo "Digite a mensagem de commit:"
read COMMIT_MSG
git commit -m "$COMMIT_MSG"
```

Assim, todos os comandos serão executados em sequência, automatizando seu fluxo de trabalho!


**Copia do Script**
```bash
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
cls
echo
echo 'cd /d/_GITHUB/templates'
cd /d/_GITHUB/templates
echo
echo 'pwd'
pwd
echo
echo 'git status'
git status
echo
echo 'git add .'
git add .
echo
echo 'git commit -m "Descr."'
git commit -m "Descr"
echo
echo 'git push'
git push
echo
echo 'git pull'
git pull
echo
```
