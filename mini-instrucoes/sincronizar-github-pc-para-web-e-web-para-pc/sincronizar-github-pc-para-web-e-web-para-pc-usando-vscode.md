# Sincronizar GitHub: PC para WEB e WEB para PC, usando o VSCode:
"sincronizar-github-pc-para-web-e-web-para-pc-usando-vscode.md"

## Aqui estão os **procedimentos passo a passo** para sincronizar seu repositório entre seu PC e o GitHub Web, de ambos os sentidos:

***

## 🖥️→🌐 **Checklist: Sincronizar do PC para o GitHub Web**

1. Abra o VSCode na pasta do seu repositório local
   - Menu → Arquivo → Abrir Pasta → selecione `/d/_GITHUB/templates`

2. Edite os arquivos normalmente usando o editor.

3. Vá para o ícone de controle de versão (Source Control ou `<>`) na barra lateral esquerda.

4. Veja os arquivos modificados na lista.  
   Eles aparecem automaticamente como “Changes”.

5. Digite uma mensagem de commit onde aparece “Message” (ex: `Atualização dos templates`).

6. Clique em 'Commit' (ícone de check ou botão "✓").

7. Clique em 'Sync Changes', 'Push' ou '↑ N' na barra inferior ou na barra lateral (os nomes mudam conforme a versão; qualquer um deles envia suas alterações para o GitHub).

8. Pronto!  
   - Suas mudanças agora estão no GitHub web.


***

## 🌐→🖥️ **Checklist: Sincronizar do GitHub Web para o PC**

1. Abra o VSCode na pasta local como acima.

2. Vá até o painel Source Control/Controle de Versão na barra lateral.

3. Clique em 'Pull', 'Sync Changes' ou '↓ N'  
   - Este comando baixa as alterações do GitHub web para o seu PC.
   - “Sync Changes” faz push + pull ao mesmo tempo (envia e traz).

4. Pronto!  
   - VSCode baixa todos os arquivos e atualiza sua pasta local conforme o remoto.


***

### DICAS VISUAIS
- Os ícones de push/pull podem aparecer na barra inferior (`↑`, `↓`, “Sync Changes”) ou como botões no topo do painel Source Control.
- Se houver conflitos, VSCode mostra na tela e permite resolver direto pelo editor.


***

### DICAS EXTRAS
- Sempre resolva conflitos apontados pelo Git antes do próximo push/pull.
- Tudo no VSCode é feito via botões, sem terminal.
- Basta editar, commit, sync/push/pull!
- Funciona igual no Windows, Linux ou macOS.





##----------####----------####----------####----------##