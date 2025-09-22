# 🔍 Show Diff (Preview changes) — o que é e como usar

O **Show Diff** (ou **Preview changes**) mostra **as diferenças** entre o que você editou e a última versão salva no repositório.

- 🟩 **Verde** = linhas **adicionadas**
- 🟥 **Vermelho** = linhas **removidas**
- Pode aparecer **Unificado** (uma coluna) ou **Side-by-side** (lado a lado)

---

## ✨ Para que serve
- Confirmar **exatamente** o que mudará antes de **Commit changes**
- Evitar erros (ex.: link trocado errado, texto apagado sem querer)
- Em Pull Requests (PRs), é onde outras pessoas **revisam** suas alterações (aba **Files changed**)

---

## 🪜 Como acessar no editor do GitHub (arquivo único)
1. Abra o arquivo → **Edit**  
2. Faça suas alterações  
3. Clique em **Preview changes** / **Show Diff**  
4. Revise as diferenças (verde/vermelho)  
5. Clique em **Commit changes**

> Dica: achou algo errado no diff? Volte para **Edit**, ajuste e **revise novamente**.

---

## 🪜 Como ver o diff em Pull Requests (vários arquivos)
1. Abra o PR  
2. Vá na aba **Files changed**  
3. Revise cada arquivo (comentários em linha, se preciso)  
4. Aprove ou peça ajustes

---

## 💡 Dicas rápidas
- **Commits pequenos** = diffs mais fáceis de revisar  
- Escreva um **título/mensagem de commit** clara (o “porquê” da mudança)  
- Prefira **links relativos** quando possível (evita retrabalho em renomeações)  
- Use o diff para conferir **ortografia/links** antes de confirmar

---

## 🧭 Onde mais aparece
- **Histórico do arquivo**: diffs entre commits antigos  
- **Comparar branches**: diffs para ver o que mudou de uma branch para outra

---

## 🧰 Atalhos úteis
- **Voltar ao editor**: clique em **Edit** (no topo do arquivo)
- **Abrir diff do PR**: aba **Files changed**
- **Mostrar/ocultar partes sem alteração**: botão **“…”** no diffs longos

---

## ✅ Checklist antes do Commit
- [ ] Revisei o **diff** (adicionados/removidos fazem sentido)
- [ ] Testei os **links** alterados
- [ ] Mensagem de commit **curta e descritiva**
- [ ] Sem dados sensíveis acidentalmente incluídos

---

> **Resumo:** o **Show Diff** é sua última conferência de segurança. Se o que aparece em **verde/vermelho** está correto, o commit está pronto. 
