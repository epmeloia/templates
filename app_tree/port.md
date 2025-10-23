Aqui está a tradução completa e fiel do prompt do **Bubble AI** para o português do Brasil, mantendo toda a estrutura e terminologia técnica:

---

# **Prompt do Bubble AI — Criar “APP_TREE” (Interface em Português, persistência local em JSON, aplicativo completo)**

**Função:**
Você é um criador especialista no Bubble. Gere um aplicativo completo chamado **“APP_TREE”** que implemente uma **árvore hierárquica de pastas** com **editor de descrição**, **persistência local em JSON (sem backend)**, **importação/exportação**, **comportamentos ricos de interface** (duplo clique, atalhos de teclado, menu de contexto, arrastar e soltar), **tema claro/escuro** e uma **área de sugestões em tempo real**.
**Importante:** Todos os **rótulos da interface, dicas, notificações e mensagens** devem estar em **Português (pt-BR)**. O **texto deste prompt** está em inglês apenas para orientação — a interface do app deve ser toda em português.

---

## **1) Requisitos Globais**

1. **Sem banco de dados backend.** Use **localStorage** para persistir toda a estrutura como JSON, incluindo o estado da interface quando aplicável.
2. **Interface em português**, com terminologia consistente: “Pasta”, “Subpasta”, “Descrição”, “Favoritos”, “Salvar”, “Carregar”, “Modo Escuro”, “Modo Claro”, “Desfazer”, etc.
3. **Salvamento automático (Autosave)** no localStorage após qualquer alteração estrutural ou de conteúdo (com debounce de 400–600ms). Carregar os dados do localStorage na inicialização.
4. **Mensagens no rodapé (toasts)**: notificações não bloqueantes visíveis por **7 segundos**; durante Importar/Exportar/Salvar/Carregar, mostrar uma mensagem persistente até a conclusão (sucesso ou erro).
5. **Atalhos de teclado:**

   * **ENTER = Confirmar** em modais/edição inline
   * **ESC = Cancelar** em modais/edição inline; também fecha menus de contexto
   * Atalhos de alinhamento no editor de descrição: **Ctrl+L**, **Ctrl+E**, **Ctrl+R**, **Ctrl+J**
6. **Validação:** nomes de pasta/subpasta não podem ser vazios ou conter caracteres inválidos; **nomes duplicados são permitidos**.
7. **Tema:** claro/escuro com transição suave (300ms).

   * Escuro: fundo `#1a1a1a`, texto `#e0e0e0`, barra lateral `#2d2d2d`
   * Claro: fundo `#ffffff`, texto `#333333`, barra lateral `#f8f9fa`
   * Persistir preferência no localStorage; detectar tema do sistema automaticamente.
8. **Acessibilidade e mobile:** suporte a mouse e toque (drag & drop); manter foco após operações.

---

## **2) Modelo de Dados (armazenado totalmente no localStorage em JSON)**

Representar a árvore como um único objeto JSON. Estrutura exemplo:

```json
{
  "version": 1,
  "theme": "light" | "dark",
  "folders": [
    {
      "id": "uuid",
      "name": "string",
      "icon": "string",
      "favorite": false,
      "description": {
        "text": "texto-rich",
        "fontFamily": "Arial|Roboto|Times New Roman|Courier New|Georgia|Verdana",
        "fontSize": 10|12|14|16|18|20|24|28|32
      },
      "children": [],
      "expanded": true,
      "stats": {
        "descendantsCount": 0,
        "depthLevel": 0,
        "lastModified": "ISO-8601"
      },
      "timestamps": {
        "createdAt": "ISO-8601",
        "updatedAt": "ISO-8601"
      }
    }
  ],
  "ui": {
    "expandedIds": ["id"],
    "selectedFolderId": "id|null",
    "searchQuery": "",
    "undo": {
      "lastMove": null
    },
    "favoritesVisible": true
  },
  "suggestions": [
    {
      "id": "uuid",
      "text": "string",
      "createdAt": "ISO-8601",
      "pinned": false
    }
  ]
}
```

**Chaves no localStorage:**

* `APP_TREE_STATE` – estrutura JSON completa
* `APP_TREE_BACKUP_[timestamp]` – backups rotativos (mantém 3 recentes)
* `APP_TREE_THEME` – tema explícito se o usuário alternar manualmente

---

## **3) Layout do Aplicativo (página principal)**

**Cabeçalho (barra superior)**
Botões com rótulos em português:

* **Salvar (JSON)** – exportar arquivo JSON da estrutura atual
* **Carregar (JSON)** – importar arquivo JSON; validar e mesclar/substituir
* **Modo Escuro / Modo Claro** – alternar tema
* **Limpar Tudo** – diálogo de confirmação antes de limpar os dados locais
* **Desfazer último movimento** – reverte o último arraste

**Campo de busca:** lado esquerdo na barra lateral
**Rodapé:** mostrar estatísticas: total de pastas, nível de profundidade, pasta mais profunda, última modificação global

---

## **4) Comportamentos Principais da Árvore**

1. Duplo clique no nome → renomeação inline (ENTER confirma, ESC cancela)
2. Duplo clique no ícone → abre modal com seleção de emoji (📁📚💼🏠🎯⚙️📊🌟💡🔧)
3. Impedir exclusão de pastas com subpastas
4. Expandir/Recolher pastas, mantendo estado
5. Barra de navegação (breadcrumbs) com caminho completo e clique para navegar
6. Validação automática de nomes (sem caracteres inválidos; duplicados permitidos)
7. Mensagens de rodapé em todas as ações

---

## **5) Editor de Descrição (rich text)**

Controles:

* Fonte (Arial, Roboto, Times, Courier, etc.)
* Tamanho (10–32px, padrão 16)
* Cor do texto com seletor
* Alinhamento: esquerda, centro, direita, justificado
* Botão “Aplicar a todas” aplica configurações de fonte globalmente
* “Resetar Padrão” volta para 16px
* Renderização consistente com o tema (claro/escuro)

---

## **6) Importar/Exportar & Arquivos Externos**

**Exportar Estrutura (JSON)**

* Botão “Salvar (JSON)” → baixa `app_tree.json`
* Mostrar progresso e mensagem de sucesso/erro

**Importar Estrutura (JSON)**

* Botão “Carregar (JSON)” → escolhe arquivo → valida → pergunta: “Substituir” ou “Mesclar”

**Importar Arquivos Externos** (na aba Descrição)

* Suporta `.txt, .docx, .pdf, .jpg, .png, .gif`
* Converte texto mantendo imagens (base64 ou local)
* Mostra prévia antes de confirmar “Substituir” ou “Anexar”

---

## **7) Busca e Filtro**

* Campo de busca filtra pastas em tempo real
* Destaca correspondências
* Botão “X” limpa busca

---

## **8) Duplicar/Copiar**

* Ícone de “Copiar” ao lado da lixeira
* Duplica pasta e subárvore completa
* Nome padrão: “Cópia de [Nome Original]”
* Exige confirmação e salva automaticamente

---

## **9) Menu de Contexto (clique direito)**

* Opções: **Renomear**, **Duplicar**, **Excluir**, **Alterar Ícone**
* Fecha ao clicar fora ou pressionar ESC
* Funciona em pastas raiz e subpastas

---

## **10) Contadores e Estatísticas**

* Mostrar contagem de subpastas (ex: `Projetos (3)`)
* Rodapé com estatísticas em português:

  * Total de pastas
  * Níveis de profundidade
  * Pasta mais profunda
  * Última modificação

---

## **11) Favoritos**

* Ícone de estrela para marcar como favorita
* Seção “⭐ Favoritos” no topo da barra lateral (mostrar/ocultar)
* Clique navega até a pasta

---

## **12) Arrastar e Soltar (com Desfazer)**

* Permite mover pastas e subpastas
* Destaques visuais e pré-visualização do destino
* Bloqueia arraste para dentro da própria subárvore (“Destino inválido”)
* Mostra mensagem “Pasta movida!”
* Ação “Desfazer último movimento” reverte o último arraste

---

## **13) Breadcrumbs e Navegação**

* Mostra o caminho completo (Raiz > Subpasta > Atual)
* Clique em qualquer parte do caminho leva à pasta correspondente
* Mantém histórico para navegação Voltar/Avançar

---

## **14) Menu de Ações**

* Botão “Ações” no topo com:

  * Nova Subpasta
  * Renomear
  * Duplicar
  * Excluir (desativado se houver subpastas)
  * Alterar Ícone
* ENTER confirma, ESC cancela

---

## **15) Área de Sugestões com IA (Simples)**

* Coluna lateral com lista de sugestões
* Campo para adicionar sugestão
* Ações: Fixar, Excluir
* Persistência em `suggestions[]` no localStorage
* Simples histórico local (sem API externa)

---

## **16) Alternância de Tema**

* Ícones 🌙/☀️ no cabeçalho
* Transição suave de 300ms
* Persistência em `APP_TREE_THEME` e `APP_TREE_STATE.theme`
* Detecta preferência do sistema na inicialização

---

## **17) Regras de Validação e Mensagens**

* Validação de nomes: não vazios e sem caracteres inválidos `\/:*?"<>|`
* Impedir exclusão de pastas com subpastas (mostrar tooltip explicativo)
* Todas as ações geram mensagens em português (7s padrão)
* Mensagens persistentes durante operações longas (I/O)

---

## **18) Implementação no Bubble**

* **Custom States** armazenam toda a estrutura JSON e estado da interface
* **LocalStorage** via plugin ou função nativa
* **Elementos Reutilizáveis:**

  * ModalRenomear, ModalIcones, ModalConfirmacao, ModalPreviewImportacao
  * ToastRodape
* **Workflows:**

  * Ao carregar a página → ler `APP_TREE_STATE`; se não existir, criar pasta exemplo
  * Em qualquer alteração → atualizar JSON → salvar (debounce) → atualizar estatísticas
  * Importar/Exportar JSON → validar e aplicar
  * Arrastar e soltar → atualizar e permitir desfazer
  * Busca → filtrar visualmente
  * Menu de contexto → abrir na posição do cursor

---

## **19) Critérios de Aceitação**

1. Interface 100% em português (pt-BR)
2. Tema claro/escuro funcional e persistente
3. Salvar/Carregar exporta e restaura estrutura corretamente
4. Duplo clique para renomear/ícone funciona com ENTER/ESC
5. Exclusão bloqueada para pastas com filhos
6. Validação de nomes funcional
7. Mensagens de rodapé no tempo correto
8. Expansão/Recolhimento com animação suave
9. Breadcrumbs e busca funcionam em tempo real
10. Duplicação preserva subpastas
11. Menu de contexto funciona corretamente
12. Estatísticas atualizadas dinamicamente
13. Favoritos funcionam e persistem
14. Arrastar e soltar com Undo
15. Editor de descrição com fontes, tamanhos, cores, alinhamento
16. Importação de arquivos com pré-visualização e preservação de imagens
17. Painel de sugestões da IA com adicionar, fixar e excluir

---

## **20) Entregáveis**

* Página Bubble funcional (index) com todas as funcionalidades descritas
* Componentes reutilizáveis (modais, toasts)
* Estilos limpos para temas claro/escuro
* Todos os workflows em português com o comportamento especificado

---

**Crie este aplicativo agora. Toda a interface deve estar em português. Persista tudo localmente (sem backend). Implemente exatamente todas as funcionalidades descritas acima.**

---

Deseja que eu converta este prompt para um **modelo otimizado para envio direto no Bubble (IA Builder)**, com divisões em “Page Structure”, “Workflows” e “UI Copy pt-BR”?
