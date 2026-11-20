# Bitácora — edicion

> Una línea por hallazgo: `AAAA-MM-DD · el dato · el por qué`. Se agrega abajo, no se edita lo anterior.

2026-11-19 · Chequeo de arranque: las skills imperioreels, imperioreelscorto e imperiootos están en `.claude/skills/`, pero faltan el motor Remotion (`motor-remotion/`, no está en Escritorio, Documentos ni Descargas), el `.env` con ELEVENLABS_API_KEY y HEYGEN_API_KEY, ffmpeg/ffprobe, Node y Python (ninguno en el PATH) · sin esto no se puede producir ni un anuncio; no prometer fechas hasta que estén.
2026-11-19 · El `.env` existe (lo creó el Cerebro, está en .gitignore) con ELEVENLABS_API_KEY, KIE_API_KEY y HEYGEN_API_KEY vacías; la instalación de ffmpeg, Node, Python y el motor Remotion se le pidió a Sistemas · las claves se verifican con una llamada de solo lectura cuando Tamy avise que las cargó.
2026-11-19 · ffmpeg 9.0.2, Node v26.13.1 y Python 3.13.17 andan desde mi shell si cargo el PATH de Machine+User (la sesión arrancó con el PATH viejo); falta solo el motor Remotion · sin cargar el PATH, `which` no los encuentra y parece que no están.
