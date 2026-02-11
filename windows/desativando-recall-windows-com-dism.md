# 🧰 Desativando o Recall no Windows com DISM

# Nome: "desativando-recall-windows-com-dism.md"

---

## ✅ O Que o Comando Faz

O comando abaixo:

```plaintext
DISM /Online /Disable-Feature /FeatureName:Recall
```

executado no **Prompt de Comando (CMD) com privilégios de Administrador**, **desativa o recurso “Recall”** do Windows 11.

## 🧠 O Que é o "Recall"?

O **Recall** é um recurso introduzido no Windows 11 (normalmente em edições com IA/Copilot+), que permite ao sistema capturar periodicamente imagens da tela para que o usuário possa “voltar no tempo” e encontrar informações que viu anteriormente, mesmo que não tenha salvo nada.

## 🔒 Por que desativar?

Desativar o Recall pode ser **essencial por motivos de privacidade e segurança**, pois ele:

* Salva imagens do que foi exibido na tela.
* Pode armazenar dados sensíveis de forma local.
* Funciona constantemente em segundo plano.

## 🔧 Passo a Passo

1. **Abrir CMD como Administrador:**

   * Pressione `Win`, digite `"cmd"`, clique com o botão direito em **Prompt de Comando** e selecione **"Executar como administrador"**.

2. **Executar o comando:**

   ```plaintext
   DISM /Online /Disable-Feature /FeatureName:Recall
   ```

3. **Aguardar a confirmação:** O sistema retornará uma mensagem informando que a funcionalidade foi desativada com sucesso.

## ⚠️ Observações Importantes

* **Reversível:** Caso queira reativar, use:

  ```plaintext
  DISM /Online /Enable-Feature /FeatureName:Recall
  ```
* **Disponibilidade:** O comando só tem efeito em versões do Windows que possuem o Recall instalado.
* **Sem reinício obrigatório**, mas é recomendado reiniciar o sistema após a alteração.

---

```
##----------####----------####----------##
##                                      ##
##   ... 🐝 Assinatura Institucional    ##
##                                      ##
##----------####----------####----------##

         .' '.    .' '.         ,-.
.        .   .    .   .         \ /
 .         .        .       . -{|||)<
   ' .  . ' ' .  . ' ' . . '    / \
                                `-^
##----------####----------####----------##
```
