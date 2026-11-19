# Bitácora — sistemas

> Una línea por hallazgo: `AAAA-MM-DD · el dato · el por qué`. Se agrega abajo, no se edita lo anterior.

- 2026-11-19 · Repositorio privado conectado: github.com/tamaraporcel53-dot/mi-cerebro (rama main). Primera subida OK. Login de GitHub guardado en el Administrador de credenciales de Windows (Git Credential Manager), no en archivos.
- 2026-11-19 · Primer intento de push dio 'Repository not found': el repo no estaba creado en GitHub. Por qué importa: si falla así, revisar primero que el repo exista con ese nombre exacto.
- 2026-11-19 · Prueba de tools/autosync.sh: log 'OK guardado y subido 1 archivo(s): RAW', commit 644c119 igual en GitHub. El guardado automático funciona.
- 2026-11-19 · Energía al 2026-11-19, con cargador: suspensión a los 10 min, hibernación a las 3 h, pantalla se apaga a los 3 min. Por qué: con eso la compu no sirve de servidor; Tamy tiene que poner suspensión e hibernación en Nunca (cambiar config del sistema lo hace ella).
- 2026-11-19 · Git configurado global: user.name Tamy, mail de su cuenta, rama por defecto main. La CLI gh NO está instalada; el repo se creó desde la web.
- 2026-11-19 · Prueba nube: repositorio (CLAUDE.md, WIKI/, RAW/, 7 skills en .claude/skills/) → anda · la sesión en la nube clona el repo completo y lee las mismas reglas y skills que la notebook.
- 2026-11-19 · Prueba nube: rama de trabajo → la sesión arranca en una rama propia `claude/...`, no en `main` · por qué importa: el hook Stop (tools/autosync.sh) hace `git push origin HEAD`, o sea sube a esa rama y NO a main. Para que lo hecho en la nube llegue a main hay que subir a main a mano o fusionar la rama.
- 2026-11-19 · Prueba nube: git push a main → ver línea siguiente (esta nota es la prueba).
- 2026-11-19 · Prueba nube: conector Impultienda → anda (listar_tiendas respondió: 0 tiendas al 2026-11-19) · se pueden leer ventas, productos y tiendas sin la notebook.
- 2026-11-19 · Prueba nube: conector Meta Ads → anda (ads_get_ad_accounts: 1 cuenta, activa, con medio de pago) · se pueden leer y revisar campañas sin la notebook.
- 2026-11-19 · ⚠️ CONTRADICE REGLA: la única cuenta publicitaria de Meta (termina en ...1658) está en ARS, no en USD · CLAUDE.md exige USD siempre (regla del 2026-11-19). Meta no deja cambiar la moneda de una cuenta existente (sin confirmar): probablemente haya que crear otra cuenta en USD. Decide Tamy; no se tocó nada.
- 2026-11-19 · Prueba nube: claves ELEVENLABS_API_KEY y HEYGEN_API_KEY → no existen en la nube · sin ellas no se pueden generar voces ni avatares (imperioreels, imperiootos) en la nube; habría que cargarlas como secreto del entorno, nunca en el repo.
- 2026-11-19 · Prueba nube: ffmpeg 6.1.1, node v22, python3 3.13 → anda · se puede editar video y correr scripts en la nube.
- 2026-11-19 · Prueba nube: navegador → anda solo Chromium sin pantalla (Playwright), sin sesiones iniciadas · sirve para páginas públicas (ej. revisar una landing); NO sirve para nada que pida login (Business Manager, Impultienda panel). Eso necesita la notebook con Control Remoto.
- 2026-11-19 · Prueba nube: git en la nube firma commits como "Claude", no como Tamy · no es un problema, pero el historial va a mostrar los dos nombres.
