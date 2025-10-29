# TERMINAL - Sincronizar - PC para WEB e WEB para PC:
"terminal-sincronizar-pc-para-web-e-web-para-pc-v1.md"

---

## Comandos Básicos do Terminal:
- Colar = Shift + INS
- Copia = Ctrl + INS
- Setas Cima / Baixo = Navega nos comandos já executados
- Setas Direita / Esquerda = Navega pelo Texto na Linha

---

## Aqui estão os **procedimentos passo a passo** para sincronizar seu repositório entre seu PC e o GitHub Web, de ambos os sentidos:

***

## 🖥️→🌐 **Checklist: Sincronizar do PC para o GitHub Web**

1. Abra o terminal no repositório:
   ```bash
   cd /d/_GITHUB/templates
   ```

   Msg: 
   ```
   eucli@LapTopJR MINGW64 /d
   $ cd /d/_GITHUB/templates
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   $
   ```

2. Veja se esta na pasta correta:
   ```bash
   pwd
   ```

   Msg: 
   ```
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   $ pwd
   /d/_GITHUB/templates
   
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)

   ```

3. Veja o status das alterações:
   ```bash
   git status
   ```

   Msg:
   ```
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   $ git status
   On branch main
   Your branch is up to date with 'origin/main'.
   
   nothing to commit, working tree clean
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   ```

   Msg: Tradução
   ```
   ```

4. Adicione arquivos novos/modificados:
   ```bash
   git add .
   ```

   Msg: 
   ```
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   $ git add .
   
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   ```


5. Faça o commit (registre a alteração):
   ```bash
   git commit -m "Descrição da alteração"
   ```

   Msg: 
   ```
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   $ git commit -m "Descrição da alteração"
   On branch main
   Your branch is up to date with 'origin/main'.
   
   nothing to commit, working tree clean
   
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   $
   ```


6. Envie para o repositório remoto (GitHub Web):
   ```bash
   git push
   ```

   Msg: 
   ```
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   $ git push
   Everything up-to-date
   
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   $
   ```


***

## 🌐→🖥️ **Checklist: Sincronizar do GitHub Web para o PC**

1. Abra o terminal no repositório:
   ```bash
   cd /d/_GITHUB/templates
   ```

   Msg: 
   ```
   ```


2. Baixe as modificações da web (remoto):
   ```bash
   git pull
   ```

   Msg: 
   ```
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   $ git pull
   remote: Enumerating objects: 15, done.
   remote: Counting objects: 100% (15/15), done.
   remote: Compressing objects: 100% (10/10), done.
   remote: Total 10 (delta 8), reused 0 (delta 0), pack-reused 0 (from 0)
   Unpacking objects: 100% (10/10), 2.66 KiB | 135.00 KiB/s, done.
   From https://github.com/epmeloia/templates
      6c04a02..0b40ad7  main       -> origin/main
   Updating 6c04a02..0b40ad7
   Fast-forward
    ...a-web-e-web-para-pc-usando-terminal-erros-comuns.md | 18 +++++++++++++++---
    ...github-pc-para-web-e-web-para-pc-usando-terminal.md |  8 +++++++-
    2 files changed, 22 insertions(+), 4 deletions(-)
   
   eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)
   $
   ```


3. Pronto! Agora sua cópia local está atualizada com o que está online.

***


   Msg: 
   ```
   ```


### DICAS EXTRAS
- Sempre resolva conflitos apontados pelo Git antes do próximo push/pull.





##----------####----------####----------####----------##
