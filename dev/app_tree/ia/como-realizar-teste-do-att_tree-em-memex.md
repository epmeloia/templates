# 🧠 Como Realizar o Teste do ATT_TREE em MEMEX:
"como-realizar-teste-do-att_tree-em-memex.md"


---

## 🎯 Teste Rápido - Passo a Passo

### 1️⃣ Abrir o APP
```cmd
# No PowerShell, na pasta D:\_APP_TREE_MEMEX
.\ABRIR_APP_TREE.bat
```
**OU** duplo-click no arquivo `ABRIR_APP_TREE.bat`

### 2️⃣ Aguardar Chrome Abrir
- Chrome abre em **modo anônimo**
- APP_TREE carrega automaticamente

### 3️⃣ Testar Double-Click
1. **Veja as pastas** na árvore à esquerda
2. **Double-click rápido** no nome de qualquer pasta (ex: "Pasta Exemplo")
3. **Deve aparecer:** uma caixa de texto no lugar do nome
4. **Digite** um novo nome (ex: "Teste Rename")
5. **Pressione Enter** OU **clique fora**

### 4️⃣ Resultado Esperado
✅ **Funcionou:** Nome da pasta mudou  
❌ **Não funcionou:** Nome não mudou ou nada aconteceu

### 5️⃣ Se Não Funcionou
Pressione **F12** → aba **Console** → me envie qualquer mensagem em vermelho

---

## ⚡ Teste Alternativo (se Chrome não abrir)
```cmd
# Manualmente
1. Abrir Chrome
2. Ctrl+Shift+N (modo anônimo)  
3. Arrastar D:\_APP_TREE_MEMEX\APP_TREE.html para o Chrome
```

---

