Aqui está um prompt único e ultradescritivo (em inglês) que você pode colar no construtor de IA do Bubble. Ele instrui o Bubble a gerar automaticamente o aplicativo completo — frontend, lógica e persistência JSON local —, garantindo que a interface (rótulos, texto, notificações) esteja em português (pt-BR).

---

# Bubble AI Prompt — Build “APP_TREE” (Portuguese UI, local JSON persistence, full app)

**Role:** You are an expert Bubble creator. Generate a complete Bubble app named **“APP_TREE”** that implements a hierarchical folder tree with description editor, local JSON persistence (no backend), import/export, rich UI behaviors (double-click, keyboard shortcuts, context menu, drag & drop), dark/light theme, and a live suggestions area.
**Important:** All **UI labels, tooltips, notifications, and messages** must be displayed in **Portuguese (pt-BR)**. The **prompt text** is in English to guide you precisely, but the app’s interface is Portuguese.

---

## 1) Global Requirements

1. **No backend database.** Use **localStorage** to persist the entire structure as JSON, including UI state where relevant.
2. **Portuguese UI** with consistent terminology: “Pasta”, “Subpasta”, “Descrição”, “Favoritos”, “Salvar”, “Carregar”, “Modo Escuro”, “Modo Claro”, “Desfazer”, etc.
3. **Autosave** to localStorage after any structural or content change (use a 400–600ms debounce). Load from localStorage at app start.
4. **Footer toast messages (“Rodapé”)**: show non-blocking notifications for **7 seconds**; while Import/Export/Save/Load is in progress, show a persistent status message until the operation completes (success or error).
5. **Keyboard support**:

   * **ENTER = Confirmar** in modals/inline editing.
   * **ESC = Cancelar** in modals/inline editing; also closes context menu.
   * Paragraph alignment shortcuts in description editor: **Ctrl+L**, **Ctrl+E**, **Ctrl+R**, **Ctrl+J**.
6. **Validation**: Root/Subfolder names cannot be empty or contain invalid characters; **duplicate names are allowed**.
7. **Theming**: Light/Dark with smooth transition (300ms).

   * Dark: background `#1a1a1a`, text `#e0e0e0`, sidebar `#2d2d2d`
   * Light: background `#ffffff`, text `#333333`, sidebar `#f8f9fa`
     Persist preference in localStorage; auto-detect system theme by default.
8. **Accessibility & mobile**: Support mouse and touch for drag & drop; focus management after operations.

---

## 2) Data Model (kept entirely in localStorage as JSON)

Represent the tree as a single JSON object. Example schema (Bubble should mirror this structure in states and synchronize with localStorage):

```json
{
  "version": 1,
  "theme": "light" | "dark",
  "folders": [
    {
      "id": "uuid",
      "name": "string",
      "icon": "string",                 // e.g., 📁, 📚, 💼, 🏠, 🎯, ⚙️, 📊, 🌟, 💡, 🔧
      "favorite": false,
      "description": {
        "text": "rich-text-or-markup",
        "fontFamily": "Arial|Roboto|Times New Roman|Courier New|Georgia|Verdana",
        "fontSize": 10|12|14|16|18|20|24|28|32
      },
      "children": [/* recursive folder objects */],
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
    "expandedIds": ["id", "..."],      // persisted expansion state
    "selectedFolderId": "id|null",
    "searchQuery": "",
    "undo": {
      "lastMove": null                  // stores previous parent + index for “Desfazer último movimento”
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

**LocalStorage keys:**

* `APP_TREE_STATE` – full JSON structure
* `APP_TREE_BACKUP_[timestamp]` – rolling backups (keep recent 3)
* `APP_TREE_THEME` – explicit theme if user toggled

---

## 3) App Layout (main page)

**Header (top bar)**

* Buttons (Portuguese labels):

  * **Salvar (JSON)** → Export JSON file of current structure.
  * **Carregar (JSON)** → Import JSON file; validate and merge/replace with confirmation.
  * **Modo Escuro / Modo Claro** → Toggle theme.
  * **Limpar Tudo** → Confirmation dialog before clearing local data.
  * **Desfazer último movimento** (undo for one drag-move).
* Search box (left-aligned in sidebar header).
* Stats snippet (can be in footer): Total pastas, níveis de profundidade, pasta mais profunda, última modificação global.

**Main Content (two columns)**

* **Left Sidebar (Tree + Favorites + Counters)**

  * Section **⭐ Favoritos** (toggle show/hide).
  * Tree with expand/collapse per folder (▶/▼).
  * Each folder row shows: icon, name (and inline editor on double-click), count of subfolders like `Projetos (3)`.
  * Right-side small action icons: **Copiar**, **Excluir** (trash), **Favoritar** (estrela).
  * **Context menu (right-click)** on any folder with: Renomear, Duplicar, Excluir, Alterar Ícone.
  * **Drag & Drop** with: highlighted drop targets, 70% transparency while dragging, preview line for placement (above/below/as child), prevent dropping into own subtree, update focus on drop, save immediately, show toasts: error “Destino inválido”, success “Pasta movida!”.
* **Right Content (Folder Details)**

  * Tabs: **Descrição** (primary).
  * **Descrição editor** with rich text controls (see section 5).
  * **Área de Importar Arquivos** (drag & drop or button) to ingest external files into the description (see section 6).
* **Footer (Rodapé)**

  * Toast area for messages (7 seconds default; persistent during long I/O).

---

## 4) Core Tree Behaviors

1. **Double-click folder name (Raiz/Subpasta)** → inline rename field with focus; ENTER = confirmar, ESC = cancelar; preserves hierarchy and ordering.
2. **Double-click folder icon** → modal with icon grid (📁📚💼🏠🎯⚙️📊🌟💡🔧). ENTER confirms selected icon, ESC cancels.
3. **Prevent delete if folder has children**: suppress or disable the delete action/icon for non-empty root/subfolders.
4. **Expand/Collapse** per folder; persist state. Smooth animation.
5. **Breadcrumbs bar** above description: clicks navigate to ancestors; integrate with section “Navigation support” below.
6. **Auto-validation** for names: disallow empty/invalid characters; **allow duplicates**.
7. **Footer messages** for all actions; save/load messages remain visible until completion.

---

## 5) Description Editor (rich text in Portuguese UI)

* Toolbar controls:

  * **Fonte padrão (Dropdown):** Arial, Roboto, Times New Roman, Courier New, Georgia, Verdana.
  * **Tamanho da fonte (Dropdown/Spinner):** 10, 12, 14, 16, 18, 20, 24, 28, 32 (default 16; “Resetar Padrão” sets to 16).
  * **Cor do texto:** color picker with presets + custom RGB; applies to selection or paragraph. Include “Remover Formatação”.
  * **Alinhamento de parágrafo:** Esquerda, Centro, Direita, Justificado; with shortcuts **Ctrl+L/E/R/J**.
* Apply changes in real time; persist preference for new folders; “Aplicar a Todas” applies current font settings across existing folders (confirmation required).
* Render preview consistent with theme.

---

## 6) Import/Export & External File Ingestion

**Exportar Estrutura (JSON):**

* Button **Salvar (JSON)** downloads `app_tree.json`. Show progress in footer, success or error at end.

**Importar Estrutura (JSON):**

* Button **Carregar (JSON)** opens file picker; validate schema; if invalid → show errors in footer.
* On valid import: ask user to **Substituir** ou **Mesclar**. Show progress until complete, then success.

**Importar Arquivos Externos (na aba Descrição da pasta selecionada):**

* Drag & drop area and button **Importar Arquivo**.
* Accept: `.txt, .docx, .pdf, .jpg, .png, .gif`.
* Convert to simple text while preserving images.

  * Images stored as base64 or local reference.
* **Preview modal** shows parsed content; options: **Substituir** ou **Anexar** ao conteúdo existente; confirm before applying.

---

## 7) Search / Filter

* Search field at the top of sidebar filters folders **in real time** as user types.
* Highlight matched names; provide clear button **“X”** to reset.
* Filter affects visible tree but does not modify structure.

---

## 8) Duplicate / Copy

* Action icon “Copiar” near trash.
* Duplicates a folder and full subtree.
* Default name: **“Cópia de [Nome Original]”**.
* Confirmation dialog; autosave after duplication.

---

## 9) Context Menu (Right-Click)

* Options: **Renomear**, **Duplicar**, **Excluir**, **Alterar Ícone**.
* Smart positioning; closes on outside click or ESC.
* Works for root and subfolders.

---

## 10) Counters & Statistics

* Show subfolder count next to names, e.g., `Projetos (3)`.
* Footer or header stats panel (Portuguese labels):

  * **Total de pastas**
  * **Níveis de profundidade**
  * **Pasta mais profunda**
  * **Última modificação**
* Update these in real time as structure changes.

---

## 11) Favorites & Bookmarks

* Star icon to mark folder as **favorita**.
* Dedicated **⭐ Favoritos** section at top of sidebar (toggle on/off to show/hide).
* Clicking a favorite navigates to it and highlights in the tree.

---

## 12) Drag & Drop (with Undo)

* Drag any folder/subfolder to any valid place.
* Visuals: highlighted drop targets with 2px blue/green border; dragged item 70% opacity; preview of final position (above/below/as child).
* **Restriction:** cannot drop into its own subtree (detect by ancestor chain). Show **“Destino inválido”** on attempt.
* After move: focus the moved folder, show **“Pasta movida!”**, persist state and save.
* **Undo**: “Desfazer último movimento” reverts only the last move.

**Algorithm hints (Bubble workflows / JS where needed):**

* On drag start, capture source `id` and flattened path.
* On drag over, compute candidate target & placement (before/after/as child).
* Validate: target not within source’s descendants.
* On drop, perform immutable update of JSON tree; update `ui.undo.lastMove` for reversal; autosave.

---

## 13) Breadcrumbs & Navigation Support

* Breadcrumbs show full path to selected folder (root > … > current).
* Clicking any crumb navigates to that folder and selects it; updates right-side content and preserves editor state.
* Integrate with “Apoio à Navegação”:

  * Back/Forward style helpers (optional) using a small history stack in `ui`.
  * When selection changes via search or favorites, keep breadcrumbs consistent.

---

## 14) Action Button / Command Area

* Provide an “Ações” menu (dropdown or button group) near header for quick commands relevant to the selected folder:

  * **Nova Subpasta**
  * **Renomear**
  * **Duplicar**
  * **Excluir** (disabled if subfolders exist)
  * **Alterar Ícone**
* Ensure **ENTER** confirms and **ESC** cancels in all popups.

---

## 15) AI Agent Suggestion List (Interactive)

* Right column (below Descrição or in its own panel) with a minimal suggestions manager:

  * **Input** to add a suggestion (Portuguese placeholder).
  * **List** of suggestions with created time.
  * Actions: **Fixar** (pin), **Excluir**.
  * Persist in `suggestions[]` within localStorage.
* Display as a simple backlog for future AI features (no external calls).

---

## 16) Theme Toggle & Persistence

* Header toggle with icons 🌙/☀️.
* Animate transition (300ms); write chosen theme to `APP_TREE_THEME` and mirror to `APP_TREE_STATE.theme`.
* On first load, detect system preference and initialize accordingly.

---

## 17) Strict Validation & Messaging Rules

* **Name validation**: non-empty, reject invalid characters `\/:*?"<>|` (show message “Nome inválido”). Duplicates allowed.
* **Deletion**: if folder has children, **do not allow delete**; hide/disable trash icon and show tooltip explaining “Não é possível excluir pastas com subpastas”.
* **Rodapé messages**: all actions produce a brief Portuguese message (7s); Import/Export/Save/Load show a persistent spinner message until completion.

---

## 18) Implementation Guidance in Bubble

* **Use Custom States** at page and element level to hold the **entire JSON tree** and derived UI state.
* **LocalStorage** access: use Bubble’s built-in or a lightweight plugin to **get/set** keys specified above.
* **Reusable Elements**:

  * **ModalRenomear** (rename/inline also supported), **ModalIcones** (grid), **ModalConfirmacao**, **ModalPreviewImportacao**.
  * **ToastRodape** (footer toasts).
* **Option Sets** (or static list) for icon library: 📁📚💼🏠🎯⚙️📊🌟💡🔧.
* **Workflows (high-level):**

  * On Page Load → read `APP_TREE_STATE`; if none, seed with one sample root folder.
  * Any change (rename, move, duplicate, favorite, description edit, font/size/color, alignment, theme change) → update JSON state → **debounced autosave** to localStorage → update stats and UI.
  * Export JSON → stringify and trigger file download.
  * Import JSON → validate → preview summary → apply **Substituir** or **Mesclar**.
  * Drag & Drop → perform validated move → set `ui.undo.lastMove`.
  * Undo → revert using stored previous parent/index.
  * Search → compute filtered view & highlights.
  * Context Menu → open at cursor; actions dispatch to the same core mutators.
* **Stats calculation**: keep helper functions to recompute `descendantsCount`, `depthLevel`, deepest path, and lastModified per change.

---

## 19) Acceptance Criteria (must all pass)

1. UI is entirely **Portuguese (pt-BR)**; theme toggle works and persists.
2. **Salvar/Carregar** export/import JSON exactly matches the in-memory structure and restores expansion, selection, and preferences.
3. **Double-click rename** and **double-click icon** open the correct editor; ENTER/ESC behave as specified.
4. **Delete** is suppressed/disabled for non-empty folders.
5. **Validation**: empty/invalid names blocked; duplicates allowed.
6. **Footer messages**: 7s for normal actions; persistent during I/O until completion.
7. **Expand/Collapse** persists; animations are smooth.
8. **Breadcrumbs** navigate correctly.
9. **Search** filters live with highlight and clear “X”.
10. **Duplicate** clones full subtree, names as “Cópia de [Nome Original]”.
11. **Context menu** works on root and subfolders; closes on click-out/ESC.
12. **Counters & Stats** update in real time.
13. **Favorites** section works; toggle show/hide; click navigates.
14. **Drag & drop**: visual cues, subtree protection, success/error messages, focus after move, **Undo** reverts last move.
15. **Descrição editor**: font family/size/color, alignment buttons + shortcuts, “Aplicar a Todas”, “Resetar Padrão (16px)”.
16. **Importar arquivos externos**: accepts listed types, previews, allows **Substituir** or **Anexar**, preserves images as base64/local reference.
17. **AI Suggestions** panel: add, pin, delete, and persist locally.

---

## 20) Deliverables

* A working Bubble page (index) implementing the above.
* Reusable components for modals/toasts.
* Clean styles for light/dark themes.
* All workflows wired with Portuguese copy and the exact behaviors described.

---

**Build this now. All interface text must be in Portuguese. Persist everything locally (no backend). Ensure every feature above is implemented exactly as specified.**
