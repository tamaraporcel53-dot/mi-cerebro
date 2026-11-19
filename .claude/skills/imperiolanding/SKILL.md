---
name: imperiolanding
description: Se llama con "imperiolanding". Arma la landing de venta completa de un infoproducto en Impultienda usando el modo Custom HTML, desde una carpeta con los archivos del producto. Usar cuando el usuario diga "armame la landing", "hacé la landing de mi ebook", "landing de Impultienda", "montar mi producto en Impultienda", "página de ventas de mi infoproducto", o cuando comparta una carpeta con la imagen creativa y el PDF de su ebook y quiera la página de ventas lista. También cubre revisar, corregir o mejorar una landing de Impultienda ya publicada.
---

# Landing de venta en Impultienda

Construís la página de ventas completa de un infoproducto en Impultienda, en modo **Custom HTML**, y la dejás publicada y verificada.

El usuario es un emprendedor que vende ebooks. No es programador. Nunca le pidas que toque código ni que copie y pegue HTML: vos entrás al panel por el navegador y lo hacés.

**No diseñes la estructura desde cero, pero SÍ diseñá la paleta.** `references/01-plantilla.html` es el CSS y la estructura exactos de una landing real que está publicada y vendiendo: 18 secciones probadas en mobile, con arreglos de layout que si los tocás se rompen.

Lo que cambia en cada producto es el bloque `:root` — colores y tipografía — y esos salen **de la imagen creativa del producto**, no de la plantilla. Todo el CSS deriva de esas variables: cambiando ese bloque, la misma landing pasa de neón a oro, a naranja, a lo que pida el producto. Dos alumnos con dos productos distintos tienen que terminar con dos landings que no se parecen en nada, salvo en que las dos funcionan.

Estructura y medidas: se respetan. Colores y tipografía: se diseñan para cada uno.

**Y no terminaste hasta correr el chequeo final.** Está al final de este archivo. Publicar sin verificar es la forma más rápida de que el alumno vea una landing con deslizamiento horizontal o una imagen rota antes que vos.

---

## Paso 0 — Lo primero que hacés al arrancar

### 0.A — ¿Sobre qué tienda trabajamos? (antes que nada)

**En Impultienda un mismo usuario puede tener muchas tiendas.** El selector de arriba a la izquierda las lista todas. Meterse en la tienda equivocada y ponerse a editar es el peor error posible de esta skill: le pisás el diseño de un producto que ya está vendiendo, y no hay deshacer.

**Nunca asumas la tienda que está abierta.** El selector arranca en la última que el alumno usó, que no tiene por qué ser la de este producto.

Lo que hacés, en este orden:

1. Abrí el selector de tiendas (arriba a la izquierda; muestra el nombre de la tienda actual).
2. Leé la lista completa: nombre **y dominio** de cada una.
3. Preguntale cuál, mostrándole las opciones con su dominio.

> Veo dos tiendas en tu cuenta:
>
> - **Libro Digital 6** — `<subdominio-a>.impultienda.ar`
> - **Fitness en Casa** — `<subdominio-b>.impultienda.ar`
>
> ¿Sobre cuál armamos la landing?

Mostrá siempre el dominio, no solo el nombre: los nombres internos suelen ser confusos ("Libro Digital 6" no dice nada, `mi-metodo-fit` sí).

Si hay **una sola tienda**, no preguntes: decile cuál es y seguí — "Trabajo sobre *Fitness en Casa*, es la única que tenés".

**Confirmada la tienda, esa es la única que tocás.** Todo lo que sigue — panel, Diseño de ebooks, Recursos, Custom HTML — pasa adentro de ella. Si en cualquier momento el selector muestra otro nombre, frená y volvé a la correcta antes de hacer nada. No abras tiendas ajenas al trabajo "para mirar".

⚠️ **Ojo con el segundo selector.** La pantalla de Diseño de tienda tiene su propio `<select>` de tiendas **pegado al botón Guardar**, arriba a la derecha, y puede no cambiar la URL. Mirar el slug no alcanza. Antes de cada guardado verificá ese select — el chequeo exacto está en `references/03-operativa-panel.md`.

Anotá el **dominio**: lo vas a necesitar al final para abrir la tienda publicada y correr la verificación.

⚠️ **Verificá por ID, no por nombre.** El alumno puede renombrar la tienda a mitad del trabajo — pasa — y si tu chequeo de seguridad compara el nombre, te aborta el guardado justo cuando más lo necesitás, o peor: te da un falso OK. El nombre cambia; el **ID** y el **slug** no.

```js
const s = document.querySelector('select');
({ id:     s.options[s.selectedIndex].value,          // ESTE es el que se compara
   nombre: s.options[s.selectedIndex].textContent.trim(),
   slug:   location.pathname.split('/')[2] })
```

Anotá el **ID** la primera vez que entrás y compará contra ese valor antes de cada guardado. Si no coincide, no guardes.

### 0.B — La lista de las cinco cosas

**Esta lista se muestra SIEMPRE, sin excepción.** No importa si el alumno ya tiene la carpeta conectada, si Chrome está andando, o si con una mirada rápida ya viste que está casi todo: la lista sale igual. Es lo que le ordena la cabeza y le dice, en un solo golpe de vista, qué le falta. Arrancar a construir sin haberla mostrado es el error más común de esta skill.

Lo que sí cambia es **cuánto de la lista viene ya resuelto**. Antes de mostrarla, hacé un reconocimiento callado:

1. Listá la carpeta conectada, si hay una.
2. Probá una herramienta del navegador para ver si hay conexión.
3. Si el navegador responde, mirá el panel **de la tienda que confirmó en 0.A** — nunca el de otra: `Diseño de ebooks` y `Configuraciones → Pagos`.

**Ese reconocimiento no se narra.** No escribas "voy a revisar la carpeta", no vayas comentando lo que encontrás, no muestres hallazgos sueltos. Mirás callado y **lo primero que escribís es la lista ya marcada**:

- ✅ está y está bien — decí qué encontraste, en cuatro palabras
- ⚠️ está pero tiene un problema — decí cuál, concreto
- ❓ no lo pudiste ver y lo necesitás de él

Formato (el ejemplo es de un alumno con carpeta y navegador conectados):

> Para dejarte la landing lista necesito cinco cosas. Ya revisé lo que pude ver solo:
>
> ✅ **1. La imagen vertical de tu landing** — la encontré: `Landing web.webp`, 1000×6292. De ahí saco los colores.
> ❓ **2. El PDF de tu ebook** — no está en la carpeta. Le saco 7 páginas del interior para el adelanto en 3D; es el bloque que más confianza genera.
> ❓ **3. Un bloc de notas con tus opiniones o testimonios** — los que tengas, no importa cuántos. **Van TODOS a la landing**, así que mandá el archivo completo. Si todavía no vendiste, avisame y armamos ese bloque de otra forma.
> ❓ **3b. Tu puntaje y tu cantidad de reseñas** — ej. "4,8 de 5, 2.340 opiniones". Va arriba del titular. Si no lo tenés a mano no importa: pongo uno y seguimos.
> ❓ **3c. Los logos de MercadoPago, Visa y Mastercard** — para el bloque de métodos de pago. Si no los tenés a mano, decímelo y lo resolvemos.
> ⚠️ **4. El producto cargado en Impultienda** — el ebook principal está listo, pero el Bono 2 dice "Subir": no tiene el PDF. Si alguien compra hoy, no lo recibe.
> ✅ **5. Chrome conectado** — llego a tu panel sin problema.
>
> Con la 1 sola ya puedo arrancar. Las otras las vamos sumando.

Contá la lista como **cinco** aunque tenga sub-ítems: son cinco cosas que juntar, no siete.

Si no pudiste revisar nada — no hay carpeta conectada, el navegador no responde — mostrá las cinco con ❓ y pedilas derecho. **La lista sale igual**, solo que sin marcar.

Después de mostrarla, **parás y esperás respuesta**. No encadenes la lista con el arranque de la construcción en el mismo mensaje: el alumno tiene que poder decirte "esperá, el 2 lo tengo" antes de que vos armes nada.

**La 1 es la única bloqueante.** Con la imagen creativa se construye la landing entera; el resto mejora la página pero no la frena. Si tiene la 1 y le falta la 3, arrancá igual y avisale qué queda pendiente.

Los puntos 4 y 5 **los averiguás vos** en el reconocimiento callado y los mostrás ya marcados — no se los preguntás en crudo. Preguntarle "¿tenés el producto cargado?" cuando lo podías mirar te hace quedar como un formulario.

### Si el navegador no está conectado

Probá una herramienta del navegador. Si falla, es que falta la conexión. Decíselo así:

> No llego a tu Chrome. Necesito la extensión **Claude para Chrome** instalada y con permiso para `impultienda.ar`. Abrila y habilitá el permiso para ese sitio. Cuando esté, avisame y sigo.

**Si no puede conectarlo**, no lo dejes a pie. Armá igual el HTML completo y entregáselo como archivo, con estas instrucciones:

> Entrá a tu panel → Diseño de tienda → Estilo y paleta → elegí **Custom HTML** → pegá todo el contenido de este archivo en el cuadro grande → Guardar. Después recargá tu tienda y contame cómo quedó.

Pierde la verificación automática, pero se lleva la landing.

---

## Antes de escribir una sola línea

**Nunca arranques a construir sin hacer los pasos 1 y 2.** Una landing montada sobre un producto mal cargado no se puede vender, y rehacerla después cuesta el triple.

### Paso 1 — Chequeo del panel

Abrí el panel **de la tienda confirmada en 0.A** y verificá cada punto vos mismo. No le preguntes lo que podés mirar. El listado completo está en `references/00-checklist-alumno.md`.

Esto es el chequeo **a fondo**, y va después de que el alumno respondió la lista del Paso 0. El reconocimiento del Paso 0 era una pasada rápida para poder marcar la lista; acá se revisa punto por punto. Lo que ya confirmaste no lo mirás dos veces.

| Qué | Dónde | Cómo sabés que está bien |
|---|---|---|
| Ebook principal con PDF | Diseño de ebooks → Producto principal | Dice **"Listo"** y aparece "Descargar PDF" |
| Precio del principal | Diseño de ebooks → Precio, título y más | Hay precio actual y precio tachado |
| Bonos con PDF | Diseño de ebooks → Bonos | Cada uno dice **"Listo"**, y valor 0 si se regalan |
| Portadas | Diseño de ebooks | Cada ebook tiene su mockup |
| Cobro conectado | Configuraciones → Pagos | Al menos un procesador **CONECTADO** |
| Modo de cobro | Configuraciones → Pagos | Anotá si es Multidivisa o moneda fija |
| Pixel de Meta | Configuraciones → Meta / Tracking | Pixel ID cargado (y token CAPI si lo tiene) |
| 🔴 **Microsoft Clarity** (toda tienda nueva) | Configuraciones → Tracking → Microsoft Clarity | Project ID cargado y `clarityId = "<ID>"` en el HTML publicado. Si falta: proyecto en clarity.microsoft.com (gratis, con la cuenta del alumno) → Nuevo proyecto (nombre = tienda, URL = dominio, sector "Comercio") → copiar el ID de 10 caracteres → `impultienda_configurar_tracking` con `clarity_id` (queda **pendiente** con un link de aprobación que vence en 30 min; más rápido: el alumno pega el ID en Configuración → Tracking → Microsoft Clarity → Project ID → Guardar cambios) → verificar `clarityId = "<ID>"` en el HTML publicado. Clarity graba cómo navega la gente y muestra dónde se traba: con eso se mejora la página |
| 🔴 **CSS viejo de la tienda** | Configuraciones → Código (CSS) | Con HTML propio ese campo **deja de verse en el panel pero sigue aplicando**. Si hay reglas sobre `h1`-`h4`, `body` o `p` con `!important`, se pisan con reglas `.lp-lp h1…` `!important` dentro del HTML. Una vez dejó títulos blancos sobre blanco |
| 🔴 **Scripts de terceros ajenos al tracking** | HTML de la landing, Código (CSS/JS), tracking | Todo script externo que no sea el píxel/tracking de la plataforma (por ejemplo píxeles de "protección" de proveedores que no reconozcas) **se revisa y se saca** |

Si falta algo, decíselo en una lista corta y esperá. No lo cargues vos salvo que te lo pida y te pase el dato.

⚠️ **Multidivisa**: los precios se guardan **en dólares** y se convierten solos. Un precio cargado como `16990` pensando en pesos se lee como **US$16.990** y el checkout cobra una fortuna. Si ves multidivisa activa, confirmá con el usuario que el número está en USD.

### Paso 2 — Chequeo de la carpeta

Listá la carpeta y decile qué encontraste y qué falta.

Lo único imprescindible es **la imagen creativa larga** de la landing. Con eso ya se construye. Lo demás (PDF para el adelanto, fotos de resultados, opiniones, logos) mejora la página pero no la bloquea — y varias se pueden generar (ver `references/06-imagenes-higgsfield.md`).

---

## Cómo se construye

1. Leé `references/02-anatomia-y-tokens.md` — el orden de los bloques y de dónde salen los colores.
2. **Mirá la imagen creativa del producto y derivá la paleta de ahí** — el procedimiento de 5 pasos está en `02`. Mostrale la paleta al usuario en dos líneas antes de construir. La landing de cada producto tiene que verse como una marca distinta, no como la misma con otro acento.
3. Partí de `references/01-plantilla.html`. Reemplazá el bloque `:root` con esa paleta y completá cada `[[MARCADOR]]`. **No toques el resto del CSS**: todo deriva de los tokens, no hay ni un color de acento escrito a mano fuera de ahí.
4. Borrá los bloques que no correspondan. Mejor corta y verdadera que larga y rellena.
5. **Generá las 10 imágenes con Higgsfield** — 5 para el carrusel y 5 para el muro. No es opcional; ver más abajo y `references/06-imagenes-higgsfield.md`.
5b. **Cargá TODOS los testimonios** que te pasaron: los 5 primeros al carrusel, el resto al muro final.
6. Subí todo a **Recursos** y usá las URLs que devuelve el panel → `references/03-operativa-panel.md`.
7. **Respaldá el HTML que ya esté cargado** antes de escribir encima — si el alumno ya tenía una landing, tu primer guardado la borra sin deshacer (`03`).
8. Pegá el HTML en **Diseño de tienda → Custom HTML**, verificando primero que el selector de arriba a la derecha sea la tienda correcta (mecánica y trampas en `03`).
9. Los eventos de Meta ya vienen cableados en la plantilla. **No los reescribas con `fbq` crudo** — el porqué está en `references/04-eventos-meta.md`.
10. **Corré el chequeo final en la tienda publicada** — es un paso, no un repaso. Está al final de este archivo y no se saltea.

### Los dos bloques de prueba social — ninguno se saltea

Son **dos bloques distintos** y los dos van sí o sí cuando el alumno pasó testimonios. Este es el error más frecuente de la skill: poner cuatro opiniones sueltas y dar por hecho el trabajo.

**A. Carrusel — va debajo de la garantía.**
Los **primeros 5 testimonios** del archivo, cada uno con **su imagen de resultado generada con Higgsfield**. Sin imagen no es un carrusel, es una lista.

**B. Muro de opiniones — va al final de todo, antes de la barra flotante.**
**TODOS los demás testimonios del archivo. Todos.** Si el alumno mandó 25, van 25 — no 4, no "una muestra". Los primeros 5 del muro llevan **también** su imagen generada; el resto van solo con texto, avatar de inicial y estrellas.

Estructura del muro: las 6 primeras tarjetas visibles, el resto adentro de `#opg2` y el botón "Ver las N opiniones" que las despliega.

**Antes de guardar, contá:**

```js
// en el HTML que estás por guardar
(html.match(/class="opc"/g)||[]).length   // === cantidad de testimonios que te pasó, menos los 5 del carrusel
(html.match(/class="sl"/g)||[]).length    // === 5
```

Si no da, volvé y completalos. **No entregues la landing con testimonios sin usar.**

### Las 10 imágenes de Higgsfield — es un paso, no una sugerencia

Cada landing lleva **10 imágenes generadas**, y hay que generarlas explícitamente. No las omitas porque "la creativa ya tiene fotos".

| Cuántas | Dónde | Qué muestran |
|---|---|---|
| **5** | Carrusel, debajo de la garantía | El resultado del que habla cada testimonio |
| **5** | Primeras tarjetas del muro final | Lo mismo, para las 5 primeras opiniones |

Leé cada testimonio y generá la imagen de **lo que esa persona cuenta**. Si dice "lo usé con mi hija antes de dormir", la imagen es esa escena — objetos y ambiente, sin caras. El procedimiento, los prompts y el modelo están en `references/06-imagenes-higgsfield.md`.

Formatos: **1:1** para el carrusel, **4:3** para el muro. 900px, WebP calidad 86.

**Si el usuario no tiene Higgsfield conectado**, decíselo y seguí sin imágenes — pero decilo, no lo dejes pasar en silencio.

### El anillo 3D: hojas que se distingan de verdad

Las tarjetas del anillo miden **132px de ancho**. A ese tamaño una página de texto corrido es una mancha gris, y **dos fichas del mismo capítulo son idénticas**. El alumno lo va a ver enseguida: "parece que le muestro la misma imagen".

Antes de subirlas, **miralas al tamaño real**, no al tamaño del PDF:

```python
from PIL import Image
im = Image.open('pagina.png').resize((132, 187), Image.LANCZOS)
im.resize((264, 374), Image.NEAREST).save('mini.png')   # así se ve en la landing
```

La mezcla que funciona, en este orden:

1. una **ficha** con la ilustración bien marcada
2. la **portada** del ebook
3. la **lámina más visual** que tenga (un mapa, un esquema, una tabla a color)
4. **otra ficha**, con la marca en otra zona — no del mismo capítulo
5. una **portadilla de capítulo**

**Si cambiás la cantidad de hojas, recalculá los ángulos.** Son `i · (360/N)`. Con 5: 0 / 72 / 144 / 216 / 288. Con 7: 0 / 51.43 / 102.86 / 154.29 / 205.71 / 257.14 / 308.57. Si dejás los ángulos de 7 con 5 hojas, se montan. Y actualizá el texto del pie: si hay 5 hojas no puede decir "7 de las N páginas".

### La garantía: 120 días por defecto

Salvo que el usuario diga otra cosa, la garantía es de **120 días**. Es el número que mejor funciona para infoproductos: saca el riesgo de la decisión y la tasa de devolución real no sube.

Confirmáselo en una línea — es una promesa que va a tener que cumplir:

> Te puse garantía de 120 días. Si querés otro plazo, decime.

### El puntaje y las reseñas

La línea arriba del titular (`.rev`) lleva el puntaje y la cantidad de opiniones. Formato:

`<b>4,8/5</b> · 3.120 opiniones de compradores`

Si el usuario te pasa su número real (punto 3b del arranque), usá ese. Si vendía en MercadoLibre, encabezá con la fuente — `· +2.340 compras verificadas en MercadoLibre` — que convierte más que el número suelto.

**Si no te lo da, ponés `4,8/5` y una cantidad entre 1.459 y 6.985.** Sin comentarios ni aclaraciones: va la línea y seguís. Es el rango que se usa por defecto.

Si el alumno prefiere no mostrar reseñas, borrá la línea entera: la landing vende bien sin ella, apoyada en el adelanto del ebook y la garantía.

### PENDIENTES ANTES DE LANZAR

Cerrá con esta lista solo si quedó algo **operativo** sin resolver:

- PDFs de ebooks o bonos sin subir
- Pixel de Meta sin configurar
- Precio en USD sin confirmar, si la tienda es multidivisa
- Bloques con `COMPLETAR`

No metas en esta lista la línea de reseñas ni nada de contenido: son decisiones del usuario, no pendientes técnicos.

Si no quedó nada, decilo: "No queda nada pendiente, podés mandar tráfico."

### De dónde sale el texto

**El copy no se inventa: se extrae.** Una landing con promesas genéricas de infoproducto ("transformá tu vida", "el método definitivo") no vende, y además contradice lo que dice la imagen del propio producto.

Sacá cada cosa de donde corresponde:

| Qué | De dónde |
|---|---|
| Titular y promesa principal | El texto de la **imagen creativa** — leela y usá sus palabras |
| Dolores y objeciones | Lo que la imagen contesta ("no sé dibujar", "no tengo máquinas") |
| Descripción del producto y los bonos | La **descripción cargada en el panel**, en Diseño de ebooks |
| Detalles concretos (páginas, módulos, proyectos) | El **PDF** — contalos, no los estimes |
| Beneficios | Lo que la imagen promete, no lo que suena bien |
| FAQ | Las objeciones reales del rubro + lo que aparece en la imagen |

Si la imagen dice "estampá cualquier objeto en 3 segundos", el H1 dice eso. No "descubrí el arte de la personalización".

**Escribí en el mismo registro que la imagen.** Si la creativa habla de vos, la landing habla de vos.

### Los precios nunca se escriben a mano

Impultienda reemplaza estos tokens solo, en la moneda del comprador:

`{{price}}` · `{{original_price}}` · `{{savings}}` · `{{currency}}`

Un precio escrito a mano queda desactualizado y, en multidivisa, le muestra pesos a un comprador de otro país.

🔴 **Son los ÚNICOS cuatro.** `{{social_proof_count}}`, `{{rating}}` o cualquier otra llave **no se reemplaza**: sale cruda en vivo
(ya pasó con una plantilla de prueba). El puntaje y la cantidad de compras se escriben con el número
real de la tienda. El chequeo final lo agarra con `precioSinResolver`.

### El botón de compra

```html
<a class="btn" href="/checkout">Comprar ahora</a>
<button data-checkout>Comprar ahora</button>
```

---

### 🔴 Antes de guardar sobre una landing ya publicada

Leé el HTML **vivo** (`impultienda_leer_html`) y tus notas del lanzamiento, y guardá **sobre esa versión**, nunca
desde una copia local vieja ni restaurando una versión anterior sin comparar. La tienda puede tener correcciones
del mismo día que tu copia no tiene, y se pierden. Si encontrás cambios que no reconocés, no los pises: preguntá.

## PASO FINAL — El chequeo. No se saltea nunca.

**Este es el paso que más se olvida y el que más caro sale.** Una landing con deslizamiento horizontal o con una imagen rota parece rota, y el alumno lo va a ver antes que vos.

**Regla dura: no escribas "está lista", "quedó publicada" ni nada parecido sin haber corrido este chequeo y pegado el resultado.** Si no lo corriste, todavía no terminaste.

### Cómo se corre

1. Abrí la **tienda publicada** (`https://<slug>.impultienda.ar/?v=1`), no el preview del panel.
2. Esperá 10 segundos — la tienda cachea (ver abajo).
3. Forzá las imágenes lazy y corré el diagnóstico completo:

```js
// Pegar en la tienda publicada
document.querySelectorAll('img').forEach(i => { i.loading = 'eager'; i.src = i.src; });
await new Promise(r => setTimeout(r, 5000));

const d = document, H = d.documentElement;
const rotas = [...d.querySelectorAll('img')].filter(i => !i.naturalWidth);
const W = H.clientWidth;
const desbordan = [...d.querySelectorAll('*')]
  .filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.right > W + 1 && !e.closest('.vp,.pvs,.mq'); })
  .slice(0, 6)
  .map(e => (typeof e.className === 'string' ? e.className : e.tagName) + ' →' + Math.round(e.getBoundingClientRect().right));

({
  scrollHorizontal : H.scrollWidth > W,                                   // TIENE que ser false
  anchos           : H.scrollWidth + ' / ' + W,                           // tienen que ser iguales
  culpables        : desbordan,                                           // vacío
  imagenesRotas    : rotas.map(i => i.src.split('/').pop()),              // vacío
  testimoniosMuro  : d.querySelectorAll('.opc').length,
  slidesCarrusel   : d.querySelectorAll('.sl').length,
  imagenesGeneradas: d.querySelectorAll('.slimg img').length + d.querySelectorAll('.opi img').length,
  botonesCheckout  : d.querySelectorAll('a[href="/checkout"],[data-checkout]').length,
  metaTrack        : typeof window.metaTrack,
  precioSinResolver: d.body.innerText.includes('{{'),                     // false
  scriptsExternos  : [...d.querySelectorAll('script[src]')].map(s => s.src).filter(u => !location.hostname.includes('impultienda') && !/facebook|fbcdn|googletagmanager|google-analytics/i.test(u)), // revisalos: vacío o solo los que reconocés
  altoPagina       : d.body.scrollHeight,
})
```

### Qué tiene que dar

| Campo | Valor correcto | Si falla |
|---|---|---|
| `scrollHorizontal` | `false` | Mirá `culpables` y andá a "Desbordes" en `02` |
| `culpables` | vacío | Casi siempre falta un `min-width:0` |
| `imagenesRotas` | vacío | URL mal copiada de Recursos |
| `testimoniosMuro` | los que te pasó, menos 5 | Faltan testimonios por cargar |
| `slidesCarrusel` | 5 | Faltan slides |
| `imagenesGeneradas` | 10 | No generaste las de Higgsfield |
| `botonesCheckout` | ≥ 1 | El botón no apunta a `/checkout` |
| `metaTrack` | `"function"` | El pixel no está configurado — avisale |
| `precioSinResolver` | `false` | Quedó una llave cruda: `{{price}}` mal escrita, o una que Impultienda no reemplaza (`{{rating}}`, `{{social_proof_count}}`) |
| `scriptsExternos` | vacío (o solo los que reconocés) | Hay un script de un tercero que no pusiste vos: se revisa y se saca |

⚠️ **Probá con el precio real, no con uno de ejemplo.** El `{{savings}}` que devuelve la plataforma es largo ("AHORRÁS AR$ 28.010") y la píldora de oferta no corta línea: se va a ~396px y rompe el mobile. En pruebas locales con un ahorro corto nunca aparece. Es el desborde más común, y se arregla acortando el texto de la etiqueta (no el CSS): "✦ OFERTA LIMITADA" en vez de "✦ OFERTA POR TIEMPO LIMITADO".

Además, a ojo (🔴 **mirá que todos los títulos se lean**: el CSS viejo de la tienda puede dejarlos blancos sobre blanco):

- **Mirala a 390px de ancho**, que es como la va a ver el 90% de la gente
- **Sin errores en consola**
- **Nada tapado por la barra flotante** al final del todo
- **La página promete solo lo que el producto entrega** (`05`)

### El bucle

Si algo da mal: **arreglalo, guardá, esperá el caché y volvé a correr el chequeo entero.** No arregles y des por hecho. Se repite hasta que dé todo bien.

### Qué le decís al usuario

Cuando pasa, contale en dos líneas qué verificaste — que sepa que se miró:

> Listo, está publicada. Chequeado en vivo: sin deslizamiento horizontal (390 = 390), las 28 imágenes cargan, 25 testimonios, 10 imágenes generadas, el botón dispara InitiateCheckout y el pixel responde.

Si algo quedó pendiente y no depende de vos, decilo ahí mismo en una lista corta de **PENDIENTES ANTES DE LANZAR**.

### La tienda cachea

Después de guardar, la tienda publicada sigue sirviendo la versión vieja unos 30 segundos. Si recargás y ves lo de antes, **no vuelvas a editar**: esperá y recargá con un parámetro nuevo (`?v=2`). Editar sobre una lectura vieja es la forma más rápida de pisar cambios buenos.

---

## Criterio

`references/05-criterio-y-riesgos.md` tiene el detalle. Lo esencial:

- **Si el usuario te pasa reseñas, números de ventas o testimonios, usalos.** No lo interrogues. Pedile la fuente una sola vez, solo para encabezar bien el bloque — una reseña con origen convierte más que una suelta.
- **Lo único que no hacés es inventarlos vos.** Si te piden escribir testimonios de compradores que no existen o generar caras de gente inventada como clientes, decilo en una frase y ofrecé lo que sí podés armar: galería de resultados, bloque de objeciones, adelanto del producto. Sin sermón, y seguí trabajando.
- **Fotos de objetos, resultados y proceso: todas las que hagan falta.** Se generan (`06`).
- **Contadores falsos**: es decisión del usuario, pero decile una vez el costo real (feedback negativo → CPM más caro) y ofrecele las alternativas de urgencia verdadera que están en `05`. La de "precio especial de hoy" ya viene en la plantilla. 🔴 **Nunca** "el precio está en dólares / si el dólar sube, mañana te cuesta más" (prohibido, 2026-10-29).
- **La matemática del ahorro tiene que cerrar.** Bonos que se regalan → valor 0 en el panel.

---

## Archivos de referencia

| Archivo | Cuándo leerlo |
|---|---|
| `references/00-checklist-alumno.md` | Al empezar, pasos 1 y 2 |
| `references/01-plantilla.html` | Al construir — es la base, no un ejemplo |
| `references/02-anatomia-y-tokens.md` | Antes de tocar el diseño o si algo se desborda |
| `references/03-operativa-panel.md` | Para guardar en el panel y subir imágenes |
| `references/04-eventos-meta.md` | Antes de escribir tracking |
| `references/05-criterio-y-riesgos.md` | Antes de escribir copy con números o testimonios |
| `references/06-imagenes-higgsfield.md` | Para generar fotos de resultados y sacar páginas del PDF |
