# Sempre Ativo no Compulador para o Teams
"sempre-ativo-computador-para-teams.md"

---

## Objetivo:
- Mantem o Usuário como Sempre Ativo, para que o Teams não troque o Status para AUXENTE.

---

## Como Faz:
- Ativa e desativa o NumLock, com temporizador

---

## Como Usar:
- Colocar na Pasta de Iniciar do Sistema (Ex: "C:\Users\CCCCCCC\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

---

## Nome do Arquivo:
- "On_line.vbs"

---

## Conteudo do Arquivo:

```
set wsc = createobject("wscript.shell")
 
Do
 
	'Five Minutes

	wscript.sleep(5*60*500)

	wsc.sendkeys("{F13}")

Loop
```


