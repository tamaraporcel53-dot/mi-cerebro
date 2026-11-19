# Parámetros técnicos, costos y límites

Todo lo de acá está **medido en producción**, no estimado. Los precios y créditos de las
plataformas cambian: verificalos antes de presupuestar.

---

## Costos

| Qué | Cuánto | Dónde |
|---|---|---|
| Video con avatar | **~20 créditos por minuto** | HeyGen |
| Imagen `soul_2` | ~0,15 créditos | Higgsfield |
| Imagen `nano_banana_pro` | 2 créditos | Higgsfield |
| Clip de video de 5 seg | **32,5 créditos** | Higgsfield |
| Voz sola (TTS) | 0,1 créditos | Higgsfield |

**Referencias medidas:**

- VSL de 53 segundos → 16 créditos de HeyGen
- VSL de 38 segundos → 12 créditos
- VSL de 3:38 → **72 créditos**
- 12 imágenes con `soul_2` → menos de 2 créditos

**Por qué no se arma un VSL con video generado.** 4 minutos son 48 clips de 5 segundos: 1.560 créditos. El plan Creator de HeyGen trae 600 al mes. No entra. La arquitectura viable es avatar + fotos con paneo, y clips animados solo en el momento más importante.

Verificá el saldo con `get_current_user` antes de lanzar cualquier render y decíle al usuario cuánto va a costar.

---

## Planes de HeyGen (referencia, verificá precios actuales)

| Plan | Precio | Créditos/mes | Máx. duración | Calidad |
|---|---|---|---|---|
| Free | $0 | 1-3 videos | **1 min** | 720p **con marca de agua** |
| **Creator** | **$29/mes** | 600 | 30 min | 1080p, sin marca de agua |
| Pro | desde $49/mes | 1.000+ | 30 min | 4K |
| Business | $149/mes | 1.500 | 60 min | 4K |

El Free no sirve: corta en 1 minuto y deja marca de agua. Creator alcanza de sobra para un embudo de 3 OTOs (216 créditos).

El conector MCP se agrega desde claude.ai (**+ → Conector → Agregar conector personalizado**, con la URL del MCP oficial de HeyGen), funciona en todos los planes y **consume los créditos de la suscripción**, no una billetera de API aparte. Pagar la API por separado sale bastante más caro por segundo de video, así que no conviene para este volumen.

---

## Parámetros del render

```
voiceSettings: {"speed": 1.4}     # aprobado en produccion; 1.0 se siente lento
expressiveness: "medium"          # NUNCA "high": mete vibracion de camara (ver abajo)
aspectRatio: "9:16"
resolution: "1080p"
caption: {"file_format": "srt"}   # SRT aparte, sin style
```

Avatar y voz: los del usuario, por su ID ([ID_DE_TU_AVATAR], [ID_DE_TU_VOZ]). Se piden en el intake, no se inventan.

**Duración: 3,6 palabras por segundo** a velocidad 1.4. Medido: 787 palabras → 218 segundos.

**Tiempo de render:** ~10 minutos para 3-4 minutos de video. Poleá `get_video` con esperas de ~2 minutos.

**Qué usar del resultado:**

| Campo | Usar |
|---|---|
| `video_url` | ✅ el render limpio |
| `subtitle_url` | ✅ el SRT |
| `captioned_video_url` | ❌ subtítulos chicos y pegados al borde |

---

## Límites de entrega

| Canal | Tope por archivo |
|---|---|
| Chat | **30 MB** |
| Escritura en la máquina del usuario | **20 MB** |

Un VSL de 3:38 en 1080p pesa ~158 MB. El master no pasa por ningún lado.

Se entrega **un solo archivo bajo 20 MB**, a 720x1280 con el bitrate calculado según la duración (comando completo en el paso 11 del `SKILL.md`). En 720x1280 la diferencia con 1080p no se distingue en mobile, que es donde se ve un OTO.

**Las escrituras a la máquina del usuario fallan por timeout si su conexión es lenta. Reintentá una vez** antes de reportar el problema: suele funcionar en el segundo intento. Lo mismo al traer archivos: si un lote falla, partilo en tandas más chicas.

---

## Cosas que se probaron y no funcionan

**Generar el mismo personaje con `soul_2` pasándole la imagen como referencia.** Devuelve personas distintas: `soul_2` no preserva identidad. Para eso usá `nano_banana_pro` o `gpt_image_2`, que sí la mantienen (comprobado). El cambio de encuadre *dentro de un video* se sigue haciendo en el montaje.

**`zoompan` de ffmpeg para el paneo de las fotos.** A 1080x1920 es lentísimo y agota el tiempo de ejecución. Usá `crop` con expresiones en `t`, que es mucho más rápido:

```
crop=1080:1920:'(iw-1080)/2+45*sin(t*0.5)':'(ih-1920)/2-25*(t/DUR)'
```

**Expresiones con `t` en el ancho o el alto de `crop`.** Solo se aceptan en `x` e `y`. `crop=1080+0*t:1920:...` falla con "Error when evaluating the expression".

**`expressiveness: "high"` en HeyGen.** Le mete al render un temblor de cámara en mano simulado de 3,0 / 3,8 px por cuadro, con un desplazamiento real de solo 24 / 33 px. Esa combinación —temblar mucho, moverse poco— se percibe como vibración molesta, no como cámara en mano. Usá `"medium"` y estabilizá con `scripts/estabilizar.py`, que la baja a 0,4 / 0,8 px sin tocar el conteo de cuadros.

**Mencionar la cámara en el `motionPrompt` para que se mueva** ("se inclina hacia la cámara en los momentos de énfasis"). Empeora el temblor. Pedí lo contrario: "cámara fija en trípode, torso anclado, solo gesticula con las manos".

**Entregar dos versiones del video** (una "web" y una "chica"). El usuario no quiere elegir. Un solo archivo bajo 20 MB.

**El filtro `subtitles` sobre un SRT pelado.** libass asume un lienzo de 384x288 y los márgenes en píxeles de video tiran el texto fuera de pantalla, en silencio. Usá `srt_a_ass.py` y el filtro `ass`.

---

## Formato de las piezas visuales

| Tipo | Qué pedir | Por qué |
|---|---|---|
| Imágenes generadas por el usuario | vertical **2:3** | si vienen cuadradas se pierde la mitad al encuadrar a 9:16 |
| Imágenes de Higgsfield | `aspect_ratio: "9:16"` | ya sale en formato |
| Filmaciones del usuario | 1080x1920 ideal | el script encuadra igual cualquier proporción |

Duración de cada corte: **2,8 a 5 segundos**. Menos se siente un parpadeo, más se siente que el video se detuvo.
