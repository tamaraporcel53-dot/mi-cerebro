---
name: imperiocampana
description: Monta una campaña de Meta de punta a punta y la deja ENTREGANDO, no creada — videos en paralelo, campaña, conjunto, creativos, anuncios con UTMs, y la checklist obligatoria de 10 puntos anuncio por anuncio antes de prender nada. Usar cuando el usuario diga "imperiocampana", "montar una campaña", "armar una campaña", "subir los anuncios", "cargar los 10 videos", "relanzar esto", "montala en tal cuenta", "nueva campaña de tal producto", o cuando pida poner un producto a vender en Meta.
---

# ImperioCampana — montar una campaña sin que quede en borrador

**Crear ≠ publicar ≠ entregar.** Son tres estados distintos y el MCP no los
distingue solo. Esta skill existe porque es fácil confirmar una campaña como activa
con **todos los anuncios en borrador**: un día entero de cero entrega.

El detalle completo y las trampas conocidas: [[montaje-de-campanas]].
Las reglas de plata (presupuestos, umbrales, cuándo cortar): [[metodo-producto-digital]].

---

## 🔴 REGLA 0 — No se prende nada hasta que la checklist dé 100%

1. **Ningún anuncio se activa con un ítem en rojo.** Ni "después lo arreglo", ni
   "igual entrega". Si falta uno, la campaña queda en pausa hasta que esté.
2. **"La herramienta no lo permite" NO es excusa.** Lo que no se pueda por API se
   hace **por el navegador**, en el Administrador, a mano y bien.
3. **Nunca decirte que algo está prendido sin el doble control** de la FASE 5.
4. 🔴 **Políticas de Meta antes de subir:** mirar guion y video. Nada de promesas de
   ingresos o de plazos, antes/después ni montos. Un rechazo le pega a toda la cuenta.
   Hay plata en juego: un dato que se da por sentado es un error.

🔑 **Preferible media hora más de montaje que un día entero de campaña sin entregar.**

---

# FASE 0 — Los videos, YA. En paralelo. Sin que los pidas.

**Apenas se habla de montar una campaña, y ANTES de crear nada en Meta**, el agente hace
estas tres cosas juntas, en un solo mensaje:

1. **Achicar los videos** a 1080x1920. Lo que sale de edición suele venir en 4K a 20+ Mbps
   y **no sube**.
2. **Pasarte la carpeta** donde quedaron, con la ruta completa.
3. **Abrirte el cargador** (`ads_creative_upload_media`, `LOCAL_FILE`) de la cuenta
   que corresponda, en ese mismo mensaje.

**Mientras vos subís los videos, el agente arma campaña y conjunto.** Los dos trabajos
corren a la vez. No se espera uno al otro.

```
ffmpeg -y -i "<original>" -vf "scale=1080:1920:flags=lanczos" \
  -c:v libx264 -crf 28 -maxrate 2000k -bufsize 4000k -preset slow \
  -profile:v high -pix_fmt yuv420p -movflags +faststart \
  -c:a aac -b:a 96k "<salida>"
```

Dejarlos con el mismo nombre, en una carpeta `<original> - LIVIANOS` al lado.

### ⚠️ Verificar antes de pasártelos

Con `ffprobe`, uno por uno: **duración, 1080x1920 y pista de audio**. Un MP4 truncado
o sin audio se sube igual y recién falla al crear el anuncio.

🔴 **No leer el peso con `ls -la` y awk.** Con nombres que tienen espacios la columna
se corre y da un número que no es. Usar `stat -c%s`.

### Si una subida falla

| Error de Meta | Qué significa de verdad |
|---|---|
| `400 · The uploaded file metadata changed` | La subida por partes se cortó |
| `403 · The upload is not authorized` | La sesión de subida venció esperando |

🔑 **Ninguno es un problema de permisos.** Los dos son el archivo demasiado pesado.

---

# FASE 1 — Relevar solo. Sin preguntar nada.

Esto se consigue sin molestar a nadie. **Antes** de abrir la boca.

| Qué | Con qué | Qué define |
|---|---|---|
| Cuentas publicitarias | `ads_get_ad_accounts` | `is_ads_mcp_enabled` y `has_payment_method` |
| **El píxel, y si la cuenta lo tiene** | `ads_get_datasets` con `ad_account_id` | 🔴 **Si no figura ahí, no alcanza con que exista en el negocio** |
| Videos subidos y su estado | `ads_get_ad_videos` | que estén en `ready` |
| La tienda, su dominio y su precio | `impultienda_listar_tiendas` + `impultienda_listar_productos` | la URL y el ticket front |
| Campañas que ya existen | `ads_get_ad_entities` level=campaign | si hay una vieja que apagar |

**No se monta en una cuenta que devuelva `is_ads_mcp_enabled: false`.** Ahí no se ve
nada desde el MCP: se avisa y se opera por navegador, o se elige otra cuenta.

---

# FASE 2 — Pedir todo junto, una sola vez

Un mensaje con **todo** lo que falta. Después se ejecuta entero sin volver a preguntar.

| # | Qué | Por qué no se adivina |
|---|---|---|
| 1 | 🔴 **En qué cuenta** se monta | Los nombres internos no coinciden con los públicos |
| 2 | **Qué producto y qué tienda** | Define píxel, dominio, fanpage y landing. **Nunca asumir** |
| 3 | **Qué videos** | Cuáles de los que subiste, y en qué orden |
| 4 | **Los textos**: copy, titular y descripción | El creativo es inmutable: se aprueban ANTES |
| 5 | **Si apagás alguna campaña vieja** | Nunca se apaga sin que lo digas |

### El presupuesto se calcula, no se pregunta

**Presupuesto diario = ticket front × 3**, y el resultado se **redondea SIEMPRE hacia
arriba a múltiplos de 5**.

```
 9,90 x 3 = 29,70  ->  30
12,90 x 3 = 38,70  ->  40
17,90 x 3 = 53,70  ->  55
```

🔑 **Se redondea el presupuesto, no el ticket.** Se calcula el ticket × 3 y recién ahí
se redondea.

🔴 **El redondeo es SOLO para el presupuesto inicial.** En los **aumentos de
escala no se redondea**: si 60 + 30% da 78, se carga 78, no 80. Redondear cada
escalón deforma el porcentaje (60 → 80 es +33%, no +30%).

---

# FASE 3 — Montar

| Paso | Qué | Detalle que se olvida |
|---|---|---|
| 1 | **Campaña** CBO | Nace PAUSED. Una firma fija en el nombre (por ejemplo, tus iniciales) para saber qué armó el agente. 🔴 **Un testeo nuevo de un producto que ya tiene campaña va como CONJUNTO nuevo dentro de esa campaña**, nunca campaña aparte |
| 2 | **Conjunto** | 🔴 **SIN gasto mínimo**: los mínimos de cada conjunto se suman y los testeos siguientes quedan sin presupuesto libre. **10 anuncios por testeo, nunca menos**; la tanda siguiente se le pide al agente Edición 2 días antes. Testeo nuevo = **duplicar el conjunto en el Administrador destildando «Aplicar recomendaciones»** (si no, trae Contenido Advantage+ tildado) |
| 3 | **Miniaturas** | 1080x1920 propias. **Nunca** la automática de Meta |
| 4 | **Creativos** | Uno por video |
| 5 | **Anuncios** | Con `url_tags` y `conversion_domain` |

### Las miniaturas: Meta no baja de cualquier host

⚠️ La que devuelve `ads_get_ad_videos.picture` viene recortada a **160×200 px**: un
cuadradito en un video 9:16. Se saca el frame y se aloja en Recursos de tu tienda en Impultienda:

```
ffmpeg -ss 2.5 -i video.mp4 -frames:v 1 -q:v 2 thumb.jpg
```

Después `impultienda_subir_recurso_desde_url` y esa URL pública va como `image_url`.
El CDN de Higgsfield **Meta no lo baja**; el de Impultienda sí.

### El payload que funciona

```json
{"object_story_spec":{"page_id":"[ID_DE_TU_PAGINA]","video_data":{"video_id":"[ID_DEL_VIDEO]",
"image_url":"[URL_DE_LA_MINIATURA]","message":"<copy con emojis>","title":"<titular>",
"link_description":"<descripcion, nunca vacia>",
"call_to_action":{"type":"DOWNLOAD","value":{"link":"[URL_DE_TU_LANDING]"}}}},
"url_tags":"utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&utm_id={{ad.id}}"}
```

Más, a nivel de anuncio:

```json
"tracking_specs":[{"action.type":["offsite_conversion"],"fb_pixel":["[ID_DE_TU_PIXEL]"]}]
```

⚠️ `tracking_specs` con `offline_conversion` o `dataset` **rompe**. Sólo funciona
`offsite_conversion` + `fb_pixel`.

### 🔴 Las cuatro trampas del creativo

| Trampa | Regla |
|---|---|
| **`degrees_of_freedom_spec`** | **No mandarlo nunca.** Da `Creative should not include standard enhancements` |
| **UTMs dentro del `link_url`** | 🔴 Van en **`url_tags`**. En el link se codifican (`%7B%7B`) y Meta no las reemplaza |
| **`instagram_actor_id`** | **No mandarlo.** La API lo rechaza con los dos ids que existen. Meta aplica solo el IG vinculado a la fanpage |
| **Botón `LEARN_MORE`** | La regla es **`DOWNLOAD`**. Son productos de descarga inmediata |

ℹ️ El botón **se traduce solo**: vos lo ves "Descargar", un comprador en inglés
"Download". Ver "Más información" en la vista previa significa que el valor está mal.

### 🔑 El creativo es inmutable

Una vez publicado **no se edita**: ni texto, ni titular, ni botón, ni imagen. Cambiar
una coma obliga a creativo nuevo + anuncio nuevo, y reinicia el aprendizaje.
**Por eso la revisión va ANTES.**

`tracking_specs` sí es campo de anuncio y sí se puede actualizar.

---

# FASE 4 — 🔴 LA CHECKLIST. Anuncio por anuncio. 100% o no se prende.

**No es "revisar por arriba": es verificar cada punto y poder mostrar el dato.**

| # | Chequeo | Dónde vive | Cómo se verifica |
|---|---|---|---|
| 1 | **Píxel correcto** | `promoted_object.pixel_id` del conjunto | Contra el píxel de ESA tienda, no el de otra |
| 2 | 🔴 **La cuenta tiene ACCESO al píxel** | — | `ads_get_datasets` con `ad_account_id` |
| 3 | **URL a la landing** | `call_to_action.value.link` | El dominio de la tienda correcta |
| 4 | **UTMs** | `url_tags` del creativo | 🔴 Nunca dentro del link |
| 5 | **Fanpage** | `object_story_spec.page_id` (o el de `effective_object_story_id`) | La página de ESA marca **y en el idioma del mercado**. Mercado sin página propia = avisar antes de montar |
| 6 | **Instagram** | vista previa de Reels | Que muestre la marca correcta, **en el idioma del mercado** |
| 7 | **El video correspondiente** | `video_data.video_id` | Uno por anuncio. Cotejar **duración** contra el archivo |
| 8 | **Eventos offline** | `tracking_specs` del anuncio | `offsite_conversion` + `fb_pixel` |
| 9 | **SIN gasto mínimo** | `daily_min_spend_target` del conjunto | 🔴 **Tiene que estar VACÍO**: los mínimos se suman y los testeos siguientes quedan sin presupuesto libre |
| 10 | **conversion_domain** | del anuncio | El dominio verificado de la tienda |

🔴 **Ítem 9:** si un conjunto duplicado trae un gasto mínimo heredado, se borra (por API o en el
Administrador) antes de prender.

---

# FASE 5 — Publicar y verificar DOS VECES

1. Activar con `ads_activate_entity` los tres niveles: campaña → conjunto → anuncios
2. **Leer cada anuncio por su id** con `ads_get_ad_entities` (sin `object_state`).
   Tiene que volver `status: ACTIVE`. **Si la lista vuelve vacía, NO existe**.
   🔴 Y además **`effective_status` anuncio por anuncio**: `DISAPPROVED` o `WITH_ISSUES` = rechazado aunque
   `status` diga ACTIVE. El motivo no lo da la API: está en Calidad de la cuenta. Un rechazo puede
   pasar días sin que nadie lo vea si no se mira este campo
3. **Abrir el Administrador en el navegador** y mirar la columna **Entrega**.
   Si dice **"Borrador"**, no se publicó, por más que el MCP diga que sí
4. 🔴 **Gasto de HOY > 0** (`date_preset: today`). "Activa" no es "gastando": una cuenta
   con la tarjeta frenada figura ACTIVE, `delivery: active` y sin errores, y gasta cero.
   Se mira **solo hoy**, no ayer: una campaña que arrancó hoy tiene ayer en 0 y está bien.
   Si da 0 con varias horas corridas → abrir **Facturación** de esa cuenta
   (`business.facebook.com/latest/billing_hub/accounts/details/?asset_id=[ID_DE_TU_CUENTA]`)
   y buscar *"No pudimos efectuar una retención temporal"* o *"Se requiere la
   verificación de la tarjeta"*. El arreglo lo hacés vos, que sos el dueño del medio de pago
   (otra tarjeta predeterminada en esa cuenta + "Intentar de nuevo")

⚠️ **El MCP y el Administrador no muestran lo mismo.** `validation_status: VALIDATED`
y `active_errors: []` son chequeos **previos**. Los que deciden corren después, en el
publicador de Meta, y al MCP no le llegan. `status: PUBLISHING` significa "entregado
al publicador", **nunca** "publicado".

### Errores de publicación y qué son de verdad

| Error | Causa |
|---|---|
| `Account does not have access to pixel` | El píxel no está asignado a esa cuenta. Lo asignás vos en Configuración del negocio |
| `Creative should not include standard enhancements` | El creativo lleva `degrees_of_freedom_spec` |
| `Invalid adgroup status` | Estado que el publicador no acepta. Rehacer el anuncio |

🔴 **Un borrador guarda la validación vieja.** Si se arregla el permiso después de
crearlo, el borrador sigue mostrando el error anterior: hay que **crear el anuncio de
nuevo** para que Meta lo valide limpio.

### Borrar un anuncio (duplicado, de prueba, mal cargado)

- **Por API no:** el cambio queda en borrador y se publica a nivel campaña, arrastrando
  cualquier otro borrador. Y un anuncio con un error viejo (por ejemplo `instagram_actor_id`
  inválido) hace fallar hasta su propia eliminación.
- **En el Administrador:** pestaña Anuncios → filtro **Identificador del anuncio = ID**
  (queda una sola fila y no se toca el gemelo activo) → tilde → tacho → **Eliminar**.
  Se borra al instante. Después, confirmar por API que ya no aparece.

### Si se reemplaza una tanda

Prender la nueva, esperar a que pase revisión y **recién ahí** apagar la vieja. Al
revés queda un hueco sin entrega.

---

## Ajustes que ya están decididos

| Ajuste | Valor | Por qué |
|---|---|---|
| **Advantage+ de público** | ✅ PRENDIDO | Con un píxel sin historial, atarle el público lo frena |
| **Advantage+ de creativo** | 🔴 APAGADO | Le deja a Meta tocar el video: filtros, música, texto encima |
| **Filtro de idioma** | Sin filtro | El creativo y la landing filtran solos |

⚠️ **Son cosas distintas.** Es fácil confundirlas y apagar las dos.

---

## Al terminar

1. Decirte **qué quedó entregando**, con el dato de los dos controles
2. Anotar los ids y el movimiento en `RAW/bitacora/meta.md` (el agente Cerebro lo pasa a la WIKI
   y al `changelog.md`)
3. Si quedó algo pendiente (un video que no subió), **decirlo** y sumarlo a
   "Esperando por mí" en `BRIEFING.md` si depende de vos. Un pendiente callado es el que cuesta el día siguiente.
