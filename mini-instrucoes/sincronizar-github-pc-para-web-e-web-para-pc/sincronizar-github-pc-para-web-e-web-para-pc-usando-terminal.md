# Sincronizar GitHub: PC para WEB e WEB para PC, usando o Terminal:
"sincronizar-github-pc-para-web-e-web-para-pc-usando-terminal.md"

## Aqui estão os **procedimentos passo a passo** para sincronizar seu repositório entre seu PC e o GitHub Web, de ambos os sentidos:

## Comandos Básicos do Terminal:
- Colar = Shift + INS
- Copia = Ctrl + INS
- Setas Cima / Baixo = Navega nos comandos já executados
- Setas Direita / Esquerda = Navega pelo Texto na Linha

***

## 🖥️→🌐 **Checklist: Sincronizar do PC para o GitHub Web**

1. Abra o terminal no repositório (usar SHIFT + ins):
   ```bash
   cd /d/_GITHUB/templates
   ```
2. Veja se esta na pasta correta:
   ```bash
   pwd
   ```
3. Veja o status das alterações:
   ```bash
   git status
   ```
4. Adicione arquivos novos/modificados:
   ```bash
   git add .
   ```
5. Faça o commit (registre a alteração):
   ```bash
   git commit -m "Descrição da alteração"
   ```
6. Envie para o repositório remoto (GitHub Web):
   ```bash
   git push
   ```

***

## 🌐→🖥️ **Checklist: Sincronizar do GitHub Web para o PC**

1. Abra o terminal no repositório:
   ```bash
   cd /d/_GITHUB/templates
   ```
2. Baixe as modificações da web (remoto):
   ```bash
   git pull
   ```
3. Pronto! Agora sua cópia local está atualizada com o que está online.

***

### DICAS EXTRAS
- Sempre resolva conflitos apontados pelo Git antes do próximo push/pull.





##----------####----------####----------####----------##
