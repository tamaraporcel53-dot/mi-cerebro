---
tema: montaje-de-campanas
actualizado: AAAA-MM-DD
fuentes: Clase 1
---

# Montaje de campañas

**En una línea:** el procedimiento exacto para montar una campaña de Meta por API sin
romper nada, con las trampas conocidas.

Las **reglas de negocio** (presupuestos, umbrales, cuándo escalar, cuándo cortar)
están en [[metodo-producto-digital]]. Acá está el **cómo se carga**.
Las skills que usan esta nota: `imperiocampana` (montar) e `imperioauditoria` (revisar en solo lectura).

---

## 🔑 La regla que ordena todo: el creativo es inmutable

**Una vez publicado un creativo de Meta no se edita.** Ni el texto, ni el titular,
ni la descripción, ni el botón, ni la imagen, ni la identidad de Instagram.
Cambiar una coma obliga a **creativo nuevo + anuncio nuevo**, y eso reinicia el
aprendizaje.

> **Error típico:** montar los 10 anuncios sin descripción, sin emojis y con el botón
> equivocado. Corregirlo obliga a rehacer los 10 creativos y los 10 anuncios.

**Por lo tanto: la revisión va ANTES de publicar, nunca después.**
Antes de crear nada, pasar el checklist de abajo entero.

---

## 🔴 NO SE PRENDE NADA HASTA QUE LA CHECKLIST DÉ 100%

Dos cosas, y ninguna es negociable:

1. **Ningún anuncio se activa con un ítem en rojo.** Ni "después lo arreglo", ni
   "igual entrega". Si falta uno, la campaña queda en pausa hasta que esté.
2. **"La herramienta no lo permite" NO es una excusa.** Lo que no se pueda por API
   se hace **por el navegador**, en el Administrador, a mano y bien.

🔑 **Preferible media hora más de montaje que un día entero de campaña sin entregar.**
Es fácil tener la campaña y el conjunto en ACTIVE y todos los anuncios en borrador:
cero entrega, un día perdido.

---

## 🔴 CHECKLIST OBLIGATORIA ANTES DE PUBLICAR

**Antes del guion:** políticas de Meta. En anuncios, nada de promesas de ingresos o de
plazos, antes/después ni montos. Un rechazo le pega a toda la cuenta.

**Ninguna campaña se publica sin pasar por esta lista, anuncio por anuncio.**
No es "revisar por arriba": es verificar cada punto y poder mostrar el dato.

| # | Chequeo | Dónde vive | Cómo se verifica |
|---|---|---|---|
| 1 | **Píxel correcto** | `promoted_object.pixel_id` del CONJUNTO | Comparar contra el píxel de ESA tienda, no el de otra |
| 2 | 🔴 **La cuenta tiene ACCESO al píxel** | — | `ads_get_datasets` con `ad_account_id`. **Si no figura ahí, no alcanza con que exista en el negocio** |
| 3 | **URL a la landing** | `call_to_action.value.link` | Que sea el dominio de la tienda correcta |
| 4 | **UTMs** | `url_tags` del creativo | 🔴 **NUNCA dentro del link**: ahí se codifican (`%7B%7B`) y Meta no las reemplaza |
| 5 | **Fanpage** | `object_story_spec.page_id` | Que sea la página de ESA marca **y en el idioma del mercado**: cada idioma lleva su fan page e Instagram |
| 6 | **Instagram** | vista previa de Reels | Que muestre la marca correcta, en el idioma del mercado (ver sección Instagram) |
| 7 | **El video correspondiente** | `video_data.video_id` | Uno por anuncio. Cotejar la **duración** contra el archivo original |
| 8 | **Eventos: píxel y offline, los dos** | `tracking_specs` del anuncio | `[{"action.type":["offsite_conversion"],"fb_pixel":["<PIXEL>"]},{"action.type":["offline_conversion"],"dataset":["<PIXEL>"]}]`. Si falta cualquiera de los dos, es error. La API lo escribe pero no siempre lo devuelve: confirmalo en el editor del anuncio |
| 9 | **SIN gasto mínimo** | `daily_min_spend_target` del conjunto **vacío** | Los mínimos de cada conjunto se suman y los testeos siguientes quedan sin presupuesto libre. 🔴 **No existe gasto mínimo por anuncio**, ni en la API ni en el Administrador. Con CBO de **un solo** conjunto no reparte nada: ese conjunto ya recibe el 100% |
| 10 | **conversion_domain** | del anuncio | El dominio verificado de la tienda |
| 11 | **Anunciante y pagador** | conjunto (transparencia de la UE) | Con el **nombre del producto o la marca**, nunca tu nombre y apellido |
| 12 | **UTM copiada de la tienda** | `url_tags` | Sacada del panel de tracking de ESA tienda, no de una nota vieja ni de otro producto |

### 🔴 Y después: verificar que esté PUBLICADO, no creado

**Crear ≠ publicar ≠ entregar.** Los tres estados son distintos y el MCP no los
distingue solo.

1. Publicar con `ads_activate_entity`
2. **Leer cada anuncio por su id** con `ads_get_ad_entities` (sin `object_state`):
   si vuelve con `status: ACTIVE`, está vivo. **Si la lista vuelve vacía, NO existe**
3. **`effective_status` anuncio por anuncio:** un `DISAPPROVED` o `WITH_ISSUES` convive
   con `status: ACTIVE`. El motivo está en Calidad de la cuenta
4. **Abrir el Administrador en el navegador** y mirar la columna Entrega:
   si dice **"Borrador"**, no se publicó, por más que el MCP diga que sí

⚠️ **El MCP y el Administrador no muestran lo mismo.** `validation_status: VALIDATED`
y `active_errors: []` son chequeos PREVIOS. Los que deciden corren después, en el
publicador de Meta, **y al MCP no le llegan**. Un `status: PUBLISHING` significa
"entregado al publicador", nunca "publicado".

### 🔴 Y todos los días: verificar que esté GASTANDO

Una campaña `ACTIVE` con `delivery: active` y sin errores **puede no gastar nada** si falla el
pago de la cuenta: la API no lo muestra. Control obligatorio: **gasto de HOY > 0** (no ayer:
una campaña que arrancó hoy tiene ayer en 0 y está bien).
Si da 0, abrir **Facturación** de esa cuenta antes que nada.

### 🧹 Borrar un anuncio sin romper nada

- **Por API no:** con el modo borrador, `ads_update_entity` deja el cambio en borrador y se
  publica con `ads_activate_entity` **a nivel campaña**, arrastrando cualquier otro borrador.
- **Un borrador con error no publica.** Un anuncio creado con `instagram_actor_id` inválido
  hace fallar hasta su propia eliminación ("Param instagram_actor_id must be a valid...").
- **Cómo se hace:** Administrador → pestaña Anuncios → filtro **Identificador del anuncio = ID**
  (así queda una sola fila y no se toca el gemelo activo) → tilde → tacho → **Eliminar**.
  Se elimina al instante, sin pasar por borrador. Después, confirmar por API que no aparece.

### 💳 Cuenta frenada por la tarjeta

Aviso en Facturación: *"No pudimos efectuar una retención temporal"* + *"Se requiere la
verificación de la tarjeta"*. Arreglo (lo hacés vos, es tu medio de pago): poner otra tarjeta
como predeterminada **en esa cuenta** e "Intentar de nuevo". Se verifica en Facturación (aviso
fuera, saldo pagado) **y** con gasto de hoy > 0.

### Errores reales de publicación y qué significan

| Error | Causa |
|---|---|
| `Account does not have access to pixel` | El píxel existe en el negocio pero **no está asignado a esa cuenta publicitaria**. Lo asignás vos en Configuración del negocio |
| `Creative should not include standard enhancements` | El creativo lleva `degrees_of_freedom_spec`. **No mandarlo nunca** |
| `Invalid adgroup status` | El objeto quedó en un estado que el publicador no acepta. Rehacer el anuncio |

🔴 **Un borrador guarda la validación vieja.** Si se arregla el permiso después de
crearlo, el borrador sigue mostrando el error anterior: hay que **crear el anuncio
de nuevo** para que Meta lo valide limpio.

---

## 🔴 Lo PRIMERO de todo: los videos, en paralelo

**Apenas se habla de montar una campaña, y ANTES de crear nada, se hacen estas tres
cosas, juntas y sin que las pidas:**

1. **Achicar el peso de los videos.** A 1080x1920, nunca más. Lo que sale de la
   edición suele venir en 4K a 20+ Mbps y **no sube**.
2. **Pasarte la carpeta** donde quedaron los livianos, con la ruta completa.
3. **Abrirte el cargador** (`ads_creative_upload_media`, `LOCAL_FILE`) de la cuenta
   que corresponda, en el mismo mensaje.

**Mientras vos subís, el agente arma campaña y conjunto.** Los dos trabajos corren a la vez
y no se espera uno al otro.

### El comando

```
ffmpeg -y -i "<original>" -vf "scale=1080:1920:flags=lanczos" -c:v libx264 -crf 28 -maxrate 2000k -bufsize 4000k -preset slow -profile:v high -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 96k "<salida>"
```

Deja los nombres iguales, en una carpeta `<original> - LIVIANOS` al lado.

### ⚠️ Verificar antes de pasártelos

Con `ffprobe`, uno por uno: que tengan duración, 1080x1920 y **pista de audio**.
Un MP4 sin audio o truncado se sube y recién falla al crear el anuncio.

### Por qué existe esta regla

Una tanda de 10 videos en 4K a 20+ Mbps pesa cientos de MB y **las subidas fallan**.
Convertidos a 1080x1920 pesan una fracción y suben sin problema.

| Error de Meta | Qué significa de verdad |
|---|---|
| `400 · The uploaded file metadata changed` | La subida por partes se cortó a mitad |
| `403 · The upload is not authorized` | La sesión de subida venció esperando |

🔑 **Ninguno de los dos es un problema de permisos.** Los dos son el archivo
siendo demasiado pesado.

⚠️ **Y no confiar en `ls -la | awk` para leer el peso:** con nombres que tienen
espacios, la columna se corre y da un número que no es. Usar `stat -c%s`.

---

## ✅ Checklist previo (antes de crear el primer objeto)

| # | Qué | Cómo se verifica |
|---|---|---|
| 1 | La cuenta publicitaria está **habilitada para Ads MCP** | `ads_get_ad_accounts` → `is_ads_mcp_enabled` |
| 2 | La cuenta tiene **medio de pago** | mismo llamado: `has_payment_method` |
| 3 | La **página** existe y está en el mismo portafolio comercial que la cuenta | si comparten portafolio, no hace falta permiso extra |
| 4 | 🔴 La página tiene **cuenta de Instagram** (propia o respaldada) | ver sección Instagram |
| 5 | El **píxel** existe y ya disparó | `ads_get_datasets` |
| 6 | Los **videos** están subidos y en `ready` | `ads_get_ad_videos` → `status.video_status` |
| 7 | Las **miniaturas** están en un host que Meta pueda bajar | ver sección Imágenes |
| 8 | Los **textos están aprobados por vos** | copy, titular, descripción y botón, los de los 10 |

⚠️ **El punto 3 no se verifica con `ads_get_ad_account_pages`.** Esa lista devuelve
solo páginas ya promocionadas, no permisos. La prueba real es crear el creativo.

---

## Qué tiene que llevar cada anuncio, sin excepción

| Campo | Dónde va | Valor |
|---|---|---|
| `page_id` | creativo | la fanpage del producto |
| `video_id` | creativo | video en `ready` |
| `image_hash` / `image_url` | creativo | **miniatura 1080×1920**, no la automática |
| `link_url` | creativo | la landing, limpia |
| `message` | creativo | cuerpo **con emojis** |
| `headline` | creativo | titular |
| `description` | creativo | descripción — **nunca vacía** |
| `call_to_action_type` | creativo | **`DOWNLOAD`** |
| `instagram_actor_id` | — | **no se manda**: Meta lo resuelve por la página |
| `url_tags` | **anuncio** | las UTMs |
| `conversion_domain` | **anuncio** | el dominio de la tienda |
| Gasto mínimo: **ninguno** | conjunto | [[metodo-producto-digital]] |

🔑 **Las UTMs van a nivel de ANUNCIO, en `url_tags`, no pegadas al `link_url`.**
Tienen que aparecer en el campo "parámetros de URL" del editor, no colgando del enlace.

    utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&utm_id={{ad.id}}

`ads_create_ad` acepta `url_tags` dentro del JSON de `creative`, junto a
`creative_id`. Funciona y queda en el anuncio.

### El botón: `DOWNLOAD`, siempre

La regla es **Descargar**, no "Más información". Son productos digitales de descarga
inmediata: el botón tiene que decir lo que pasa.

ℹ️ **El botón se traduce solo.** Es un valor fijo de Meta, no texto propio. Vos lo ves
en español ("Descargar") y un comprador en inglés lo ve "Download". Ver
"Más información" en la vista previa **no** significa que el anuncio esté en
español: significa que el valor es `LEARN_MORE` y está mal.

### La descripción casi no se ve, y va igual

Meta avisa en cada creativo: **en el feed de Facebook, en anuncios de un solo
video, la descripción no se muestra, y en Instagram esa línea no existe.** Se ve en
columna derecha, Marketplace y Audience Network.

**Se carga igual** — es gratis y gana los emplazamientos donde sí aparece — pero no
esperar verla en el feed.

---

## 🖼️ Imágenes: Meta no baja de cualquier host

**Trampa cara.** Meta rechaza imágenes de hosts que no puede leer:

    Image Wasn't Downloaded: ... couldn't be downloaded.
    Please ensure the image is accessible via the internet

| Host | ¿Meta la baja? |
|---|---|
| CDN de Higgsfield | 🔴 **No** |
| El propio CDN de Meta | ✅ Sí |
| **Recursos de tu tienda en Impultienda** | ✅ **Sí — el camino bueno** |

**Procedimiento que funciona:**

1. Sacar el frame del video con ffmpeg a 1080×1920
   `ffmpeg -ss 2.5 -i video.mp4 -frames:v 1 -q:v 2 thumb.jpg`
2. Subirlo a Recursos con `impultienda_subir_recurso_desde_url`
   (lo convierte a WebP; **Meta acepta WebP sin problema**)
3. Pasar esa URL pública como `image_url` del creativo

⚠️ **No usar la miniatura automática de Meta.** La que devuelve
`ads_get_ad_videos.picture` viene recortada a **160×200 px**: un cuadradito en un
video 9:16. Es fácil que pase días sin que nadie lo note.

---

## 📸 Instagram: la trampa más cara de todas

**Un anuncio sin identidad de Instagram no entrega en NINGÚN emplazamiento de
Instagram**, aunque el conjunto los tenga todos habilitados. Se paga Advantage+ y
se compra la mitad del inventario.

### Cómo resuelve Meta la identidad de Instagram

**Al elegir la fan page, Meta le pone solo el Instagram vinculado a esa página.**
Por API **no hay que mandar nada**: alcanza con `page_id` en el `object_story_spec`.

El orden que sigue Meta:

1. Si el anuncio trae identidad propia de IG, usa esa
2. Si no, busca **el Instagram vinculado a esa fan page**
3. Si la página no tiene ninguno, usa una **cuenta respaldada por la página**
   (nombre y foto de la fan page), si ya existe

Se confirma en la vista previa de Instagram Reels (tiene que mostrar el usuario de
tu marca) y porque los anuncios traen `effective_instagram_media_id`.

### Si la página no tiene Instagram: cuenta respaldada por la página

La opción **"Usar página de Facebook"** del editor crea una **cuenta de Instagram
respaldada por la página**. Una vez que existe:

- vive **a nivel de página**, no de anuncio
- Meta **se la aplica sola** a todos los anuncios que no tengan identidad propia
- **no hay que rehacer los creativos ya montados**

🔴 **No se puede crear desde la API:**

    Param instagram_user_id must be a valid Instagram account id

El id de la página **no sirve** como `instagram_user_id`. Por lo tanto, se hace una
sola vez, a mano, antes de montar: editor del anuncio → *Seleccionar cuenta de
Instagram* → *Usar página de Facebook* → **Publicar**.

### 🔴 La trampa: a mano, el editor propone el ÚLTIMO IG que usaste

| Cómo se arma | Qué Instagram pone |
|---|---|
| **Por API, sin el campo** | ✅ El vinculado a la página |
| **A mano en el editor** | ⚠️ **El último que usaste**, aunque sea de otra marca |

🔑 **Al crear anuncios por el panel, mirar SIEMPRE el campo "Perfil de Instagram"
antes de publicar.** Es el único lugar donde la marca puede salir cambiada.

### 🔴 La API rechaza `instagram_actor_id`, con cualquiera de los dos ids

Hay **dos identificadores distintos** de la misma cuenta de Instagram y **ninguno funciona**:

| De dónde sale | Resultado |
|---|---|
| `ads_get_ig_accounts` | ❌ rechazado |
| El editor de Meta | ❌ rechazado |

Error en los dos casos:

    Param instagram_actor_id must be a valid Instagram account id

**Conclusión: no mandarlo. Se deja que Meta lo resuelva por la página.**

### ⚠️ Cómo se verifica (y cómo NO)

| Método | Sirve |
|---|---|
| `ads_get_ig_accounts` | 🔴 **No.** Devuelve vacío igual: **no lista las cuentas respaldadas por página** |
| Vista previa de Reels | ✅ Sí, para ver qué marca sale |
| Desglose por `publisher_platform` | ✅ **Sí.** Es la medición confiable de que entrega en Instagram |

> **Falsa alarma típica:** diagnosticar "Instagram no va a andar" leyendo
> `ads_get_ig_accounts` cuando estaba andando. **Se mide por entrega, no por esa lista.**

---

## Orden de montaje

1. **Checklist previo** entero
2. Subir videos y esperar `ready`
3. Sacar y alojar las **miniaturas 1080×1920**
4. Escribir los **textos de los 10** y que los apruebes
5. Crear la **campaña** (CBO) — nace PAUSED. Un testeo nuevo de un producto que ya
   tiene campaña va como **conjunto nuevo dentro de esa campaña**, nunca campaña aparte
6. Crear el **conjunto** — **sin gasto mínimo**
7. Crear los **10 creativos**
8. Crear los **10 anuncios** con `url_tags` y `conversion_domain`
9. **Verificar leyendo de vuelta** antes de prender (la checklist de 10 puntos)
10. Activar los tres niveles: campaña → conjunto → anuncios, y hacer los controles de después

**Si se reemplaza una tanda:** prender la nueva, esperar a que pase revisión y
**recién ahí** apagar la vieja. Al revés queda un hueco sin entrega.

---

## Ajustes que ya están decididos

| Ajuste | Valor | Por qué |
|---|---|---|
| **Advantage+ de público** | ✅ **PRENDIDO** | Con un píxel sin historial, atarle el público lo frena justo cuando menos sabe |
| **Advantage+ de creativo** | 🔴 **APAGADO** | Le deja a Meta tocar el video: filtros, música, texto encima |
| **Filtro de idioma** | **Sin filtro** | El creativo y la landing filtran solos |
| **Firma** | Una firma fija en el nombre de la campaña | Para saber de un vistazo qué armó el agente |

⚠️ **Advantage+ de público y Advantage+ de creativo son cosas distintas.** Es fácil
confundirlas y apagar las dos. El de público no toca el creativo.

---

## Errores de Meta que se pueden ignorar

| Error | Qué es |
|---|---|
| **#1870194** — `location_types` | Meta reescribe el campo sola en cada update. **No frena la entrega** |

---

## Leer los números sin equivocarse

⚠️ **El preset "últimos 30 días" del Administrador NO incluye hoy.** Termina ayer.
Una campaña que arrancó hoy aparece en **0**. Para ver el día en curso hay que
pedir *Hoy* explícitamente.

---

## Abierto / sin confirmar

- Agregá acá lo que descubras en tus propias cuentas y todavía no verificaste `(sin confirmar)`.

## Relacionado

[[metodo-producto-digital]] · [[protocolo-cerebro]]
