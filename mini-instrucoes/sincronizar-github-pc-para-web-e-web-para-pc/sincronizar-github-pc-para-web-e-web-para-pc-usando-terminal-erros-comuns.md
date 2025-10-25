# Sincronizar GitHub: PC para WEB e WEB para PC, usando o Terminal - Erros Comuns:
"sincronizar-github-pc-para-web-e-web-para-pc-usando-terminal-erros-comuns.md"

## Aqui estão os **procedimentos passo a passo** para sincronizar seu repositório entre seu PC e o GitHub Web, de ambos os sentidos:

***

## Atualizações na WEB que não foram Sincronizadas no PC

### APÓS COMANDO "git push"
Manssagem:
To https://github.com/epmeloia/templates.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/epmeloia/templates.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
eucli@LapTopJR MINGW64 /d/_GITHUB/templates (main)



- O GitHub informa "error: failed to push some refs to 'https://github.com/epmeloia/templates.git'".
- Execute Primeiro um Sync WEB-PC (pull):
```bash
git pull
```
- Isso vai baixar as mudanças do remoto para o PC.
- Se houver conflito, o Git vai mostrar para você resolver.
- Se não houver conflito, ele só integra e segue normalmente.
- Execute Primeiro um Sync PC-WEB (push):
```
git push
```


# Resumo
- Sempre que aparecer erro de “fetch first” ou "Updates were rejected because the remote contains work that you do not have locally", faça o git pull para sincronizar antes do próximo git push.

- Normalmente aparece quando você ou um colaborador fez alteração on-line ou em outra máquina.

- Ao realizar o comando `git pull`, **alteração no PC não serão apagados**.
- Se o que criou no PC **não existe no remoto**, ele será mantido.
- Se houver algum conflito (exemplo: mudou o mesmo arquivo local e remoto), o Git vai pedir para você resolver manualmente — escolher qual versão deve ser mantida.
- Se um o arquivo novo não existe no remoto, e não há conflitos, **ele vai continuar existindo no PC**. Só depois que der `git push` ele será enviado ao GitHub para aparecer lá também.
- `git pull` *não apaga* arquivos/pastas novas que adicionou/commitou no PC.
- Apenas mescla as alterações Local (PC) ↔ Remoto (WEB).
- Só apaga se você remover localmente e executar `git push` após o merge.

***





##----------####----------####----------####----------##
