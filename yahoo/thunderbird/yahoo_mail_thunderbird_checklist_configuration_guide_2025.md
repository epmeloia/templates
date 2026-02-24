# ✅ Yahoo Mail + Thunderbird: Secure IMAP Setup Guide (PT-BR)

Este checklist fornece um guia confiável para configurar contas Yahoo no Thunderbird com senha de aplicativo, incluindo suporte ao 2FA.

---

## 🔧 Etapas principais

1. Desative o 2FA temporariamente
[2. Gere senha de aplicativo no painel Yahoo](#-como-gerar-senha-de-aplicativo-no-yahoo)
3. Configure manualmente os servidores IMAP/SMTP
4. Teste envio e recebimento
5. Reative o 2FA

Ver versão em inglês: [yahoo_mail_thunderbird_checklist_configuration_guide_2025_EN.md](yahoo_mail_thunderbird_checklist_configuration_guide_2025_EN.md)

---

[tag:software](tag:software) [tag:email](tag:email) [tag:tutorial](tag:tutorial)

---

## Configuração Manual do Yahoo Mail no Thunderbird

### Contexto

Você deseja configurar manualmente uma conta de e-mail do Yahoo Brasil (`@yahoo.com.br`) no cliente de e-mails Mozilla Thunderbird.

---

### 🛠️ Solução Passo a Passo

#### 1. **Requisitos Iniciais**

* Certifique-se de que a **verificação em duas etapas** está **desativada** ou você tenha gerado uma **senha de aplicativo** no Yahoo.
* Sua conta Yahoo deve estar com o **IMAP habilitado**.

---

#### 2. **Abrindo o Thunderbird**

1. Abra o **Thunderbird**.
2. Vá em **Menu ≡ → Contas → Configurações de contas → Ações de conta → Adicionar conta de e-mail**.

---

#### 3. **Dados da Conta Yahoo**

Preencha os dados:

* **Seu nome:** Nome que aparecerá para quem receber seus e-mails.
* **Endereço de e-mail:** [seuemail@yahoo.com.br](mailto:seuemail@yahoo.com.br)
* **Senha:** Sua senha do Yahoo ou senha de aplicativo (preferível).

Clique em **Configuração Manual**.

---

#### 4. **Configuração Manual**

Configure conforme abaixo:

```plaintext
Servidor de Entrada (IMAP)
--------------------------
Servidor: imap.mail.yahoo.com
Porta: 993
SSL: SSL/TLS
Autenticação: Senha normal
Usuário: seuemail@yahoo.com.br

Servidor de Saída (SMTP)
--------------------------
Servidor: smtp.mail.yahoo.com
Porta: 465
SSL: SSL/TLS
Autenticação: Senha normal
Usuário: seuemail@yahoo.com.br
```

Clique em **Concluído**.

---

### ⚠️ Observações Importantes

* Caso utilize **verificação em duas etapas no Yahoo**, você **precisa gerar uma senha de aplicativo**. Acesse:

  * [https://login.yahoo.com/account/security](https://login.yahoo.com/account/security)
  * Vá em "Senhas de app" e gere uma para "Thunderbird".
* O Yahoo pode bloquear conexões que não sejam modernas. A autenticação com **OAuth2** às vezes é exigida, mas pode não estar disponível no `yahoo.com.br`.

---

### ✅ Verificação Final

Após configurar, envie um e-mail de teste para verificar:

* Envio e recebimento funcionando?
* Pastas (caixa de entrada, enviados, etc.) estão sincronizadas?

---

### 🧭 Princípio da Navalha de Occam Aplicado

1. **Solução mais simples:** Usar a senha de aplicativo e configuração IMAP padrão.
2. **Se não funcionar:** Verifique se há bloqueio por parte do Yahoo ou necessidade de ativar permissões adicionais no painel de segurança.

---




---
Vamos ao **passo 1**, que é **gerar a senha de aplicativo no Yahoo** — isso é necessário se sua conta usa **verificação em duas etapas**. Aqui está o passo a passo:

---

## 🔐 Como Gerar Senha de Aplicativo no Yahoo

### 1. **Acesse a página de segurança do Yahoo**

Abra o link a seguir:
👉 [https://login.yahoo.com/account/security](https://login.yahoo.com/account/security)

---

### 2. **Faça login na sua conta Yahoo**

* Use seu e-mail `@yahoo.com.br` e senha normalmente.
* Se a **verificação em duas etapas** estiver ativa, você receberá um código via SMS ou app.

---

### 3. **Vá até a opção "Senhas de app"**

* Role até encontrar a seção **"Senhas de app"** (ou “App Passwords” se estiver em inglês).
* Clique em **"Gerar senha de app"**.

---

### 4. **Escolha "Outros" ou "Thunderbird"**

* No campo de escolha de aplicativo, selecione “Outro aplicativo” ou digite “Thunderbird”.
* Clique em **"Gerar"**.

---

### 5. **Copie a senha gerada**

* O sistema vai mostrar uma senha exclusiva (ex: `abcd efgh ijkl mnop`).
* Copie **exatamente como aparecer** (sem espaços extras).
* Use essa senha ao configurar sua conta no Thunderbird, no lugar da senha normal do Yahoo.

---

### 6. **Finalização**

* Clique em “Concluído” no Yahoo.
* Volte ao Thunderbird e continue a configuração manual com a senha gerada.

---

### ⚠️ Dica

Essa senha gerada é **só para o Thunderbird**. Se mudar de app ou dispositivo, **gere outra**.

---

---


