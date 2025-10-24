# Sincronizar GitHub: PC para WEB e WEB para PC, usando o Terminal:
"sincronizar-github-pc-para-web-e-web-para-pc-usando-terminal.md"

## Aqui estão os **procedimentos passo a passo** para sincronizar seu repositório entre seu PC e o GitHub Web, de ambos os sentidos:

***

## 1. **Checklist: Sincronizar do PC para o GitHub Web**

1. Abra o terminal no repositório:
   ```bash
   cd /d/_GITHUB/templates
   ```
2. Veja o status das alterações:
   ```bash
   git status
   ```
3. Adicione arquivos novos/modificados:
   ```bash
   git add .
   ```
4. Faça o commit (registre a alteração):
   ```bash
   git commit -m "Descrição da alteração"
   ```
5. Envie para o repositório remoto (GitHub Web):
   ```bash
   git push
   ```

***

## 2. **Checklist: Sincronizar do GitHub Web para o PC**

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