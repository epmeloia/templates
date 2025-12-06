# **PROMPT CONSOLIDADO - ANTIGRAVITY FLOATING TIMER APP**

Esta é a versão consolidada e otimizada do prompt que o Gemini 3 Pro recebeu no vídeo para criar o Floating Timer App no Antigravity.

# Informações de captura.
- Titulo do Video: "Google Antigravity: O Futuro da Inteligência Artificial"
- endereço: [https://www.youtube.com/watch?v=5bHq6oyAcUY](https://www.youtube.com/watch?v=5bHq6oyAcUY)
- inicie da captura minuto/Segundo: 04:32
- Final da Captura minuto/Segundo: 04:38

***

# **Create a floating circular timer app for macOS with these exact specifications:**

**App Requirements:**
- Electron-based desktop app that floats above ALL other applications (including fullscreen apps)
- Circular design with a soft white glow effect
- Highly transparent glass morphism aesthetic (almost see-through)
- 25-minute countdown timer with Play/Pause/Reset controls
- Window must be frameless, transparent, and dragable
- Always stays on top of all other windows

**Technical Specifications:**

**Project Setup:**
- Directory: /Users/arthurendo/gemini/antigravity/scratch/liquid-timer
- Use npm init -y
- Install electron@28 (version 28 is stable and works reliably)
- Use CommonJS (NOT ES modules) – this is critical for Electron compatibility

**Window Configuration (main.js):**
- Size: 300x300 (square to fit circle)
- transparent: true
- frame: false
- alwaysOnTop: true
- hasShadow: false
- resizable: false
- vibrancy: 'fullscreen-ui'
- After window creation, call:
  - mainWindow.setAlwaysOnTopProfile(true, 'screen-saver')
  - mainWindow.setVisibleOnAllWorkspaces(true, { visibleOnFullScreen: true })

**Design (styles.css):**
- Container: 240x240px (smaller than window to prevent glow clipping)
- Circle: border-radius: 50%
- Background: rgba(255, 255, 255, 0.02) – almost invisible
- Backdrop blur: 5px (minimal, for see-through effect)
- Glow: box-shadow: 0 0 25px rgba(255, 255, 255, 0.2), 0 0 50px rgba(255, 255, 255, 0.05)
- Border: 1px solid rgba(255, 255, 255, 0.1)

**Timer Logic (renderer.js):**
- Start at 25:00
- Use setInterval for countdown
- Show/Hide play/pause buttons appropriately

**Critical Pitfalls to Avoid:**
- ❌ DO NOT use ES modules (type: "module" in package.json) – causes electron import issues
- ❌ DO NOT use import { app } from 'electron' – use const { app, BrowserWindow } = require('electron')
- ❌ DO NOT install electron@latest – version 39+ has compatibility issues, use electron@28
- ❌ DO NOT make the circle the same size as the window – leave 30px margin for glow
- ❌ DO NOT use electron .in scripts – use electron main.js explicitly
- ✅ DO use simple CommonJS requires
- ✅ DO ensure body has background: transparent !important
- ✅ DO make drag region match the circle size and position (240x240, centered)

**Package.json start script:** `"start": "electron main.js"`

**Files to create:** package.json, main.js, index.html, styles.css, renderer.js

**Create the complete working app with all files, install dependencies, and verify it launches successfully.**

***
