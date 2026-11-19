---
name: imperiotranslate
description: Pasa una tienda de Impultienda COMPLETA a otro idioma y la deja lista para lanzar — landing, checkout, productos, entregables, mails, post-compra, VSL y mercados. Primero releva todo solo, pide en UN mensaje lo único que no puede conseguir, y después corre de punta a punta sin volver a preguntar. Usar cuando el usuario diga "imperiotranslate", "imperio translate", "pasar la tienda a inglés", "cambiar el idioma de la tienda", "traducir la tienda", "lanzar esto en alemán/portugués/italiano", "replicar la oferta a otro mercado", "versión anglo/USA/Brasil de esta tienda", o cuando pida llevar un producto validado a un mercado nuevo. Se le habla al usuario en español, claro y directo.
---

# ImperioTranslate — pasar una tienda entera a otro idioma

**Un idioma nuevo no es traducir la landing.** Son **13 lugares** con texto, y cada uno
se cambia con una herramienta distinta. El que se saltea uno, lo descubre el comprador.

---

## 🔴 REGLA 0 — No se escribe nada hasta tener la lista completa

El orden es **siempre**: relevar (solo) → pedir (un mensaje) → ejecutar (sin parar).

**Nunca** empezar a traducir mientras falta un dato. Media tienda en inglés es peor que
una tienda entera en español: parece abandonada.

## 🔴 REGLA 1 — La tienda traducida es IDÉNTICA a la base

> Hacerlo idéntico, idéntico.

| # | Qué | Cómo |
|---|---|---|
| 1 | **Estructura** | Mismos **order bumps** en el checkout, mismas **OTO**, y cada OTO con su **downsell al 50% con el juego de cartas** (no HTML simple). No se "mejora" nada: en un caso se pasaron los bumps a OTO 3 y 4 y hubo que revertirlo |
| 2 | **Precios** | **Los fija el usuario.** No se convierten solos ni se copian de otra tienda |
| 3 | **VSL de las OTO** | Se rehacen en el idioma nuevo y se cargan. El punto 11 de la lista **no puede quedar afuera** |
| 4 | **Nombres de los testimonios** | Pasan al idioma del país, **también los quemados en las imágenes** (burbujas del hero), con el **mismo género y la misma inicial**. El testimonio se mantiene; solo cambia el nombre |
| 5 | **Texto dentro de las imágenes** | Se revisa **abriendo cada imagen**, no buscando en el HTML |
| 6 | **Dominio** | Tiene que sonar al idioma del país |
| 7 | **PDF** | Pies y portadas **sin el dominio de la tienda base**: Una vez salió con el dominio de la tienda base en 56 páginas. Pedirlo sin dominio desde el prompt |
| 8 | **Textos de plantilla** | Se revisan aunque la landing sea HTML propio: la garantía quedó en "7 dni" en vez de **120** |

---

# FASE 1 — Relevar solo. Sin preguntar nada.

Esto se consigue sin molestar a nadie. Hacerlo **antes** de abrir la boca.

| Qué | Con qué | Qué sale |
|---|---|---|
| Las tiendas, con su **idioma y moneda actuales** | `impultienda_listar_tiendas` | `id`, `tipo`, `idioma`, `moneda`, `plan` |
| Productos, precios, cuáles son post-compra | `impultienda_listar_productos` | `item_id` de cada uno |
| La landing publicada | `impultienda_leer_html` | el HTML entero |
| El embudo post-compra y sus ofertas | `impultienda_ver_postcompra` | `funnel_id`, `oferta_id` |
| El HTML de cada oferta | `impultienda_leer_html_postcompra` | upsell y downsell |
| Pasarelas conectadas | `impultienda_estado_pasarela` | 🔴 define si la moneda se puede cambiar |
| Cómo funciona la plataforma, si hay duda | `impultienda_faq` | **antes de afirmar nada** |

**El `tipo` de tienda cambia el trabajo:** `store` (clásica, con landing) · `checkout`
(sin landing) · `quiz` · `members` (área de miembros). En `checkout` y `quiz` los bloques
del checkout **van por embudo y no se tocan por el conector** — eso se avisa, no se intenta.
En `members` el trabajo grueso son las categorías y el contenido del área (punto 13).

### 🔴 Mirar `template_style` antes de planificar la landing

`impultienda_ver_landing` devuelve `template_style`. Si es **`custom_html`**, los textos de
plantilla **no se ven en la tienda pública** — pero siguen guardados, y es la causa del
error más común de esta skill: ver una lista de textos en español y no saber cuáles importan.

🔴 **Con `custom_html`, de todos esos textos sólo se ven DOS: `titulo_pestana` y
`meta_descripcion`.** Y son justo los dos que nadie revisa.

---

# FASE 2 — Pedir todo junto, una sola vez

Un mensaje con **todo** lo que falta. Después se ejecuta entero sin volver a preguntar.

### Lo que sólo el usuario puede decidir

| # | Qué | Por qué no se adivina |
|---|---|---|
| 1 | 🔴 **Sobre qué tienda** se trabaja | Los nombres internos **no coinciden** con los públicos. Nunca asumir |
| 2 | **Idioma y país** de destino | Un idioma no es un mercado: `en-US` no es UK |
| 3 | **Los precios del mercado nuevo** | 🔴 El precio **no se traduce**. Otro mercado paga distinto |
| 4 | **El nombre de la oferta** en ese idioma | Atraviesa producto, landing, mails y creativos. Se decide primero |

### Lo que el usuario tiene que hacer con sus manos (👤)

| # | Qué | Sin eso… |
|---|---|---|
| 5 | **Pasarela** que cobre en ese mercado | No hay venta. El conector da el link del panel, **no mete credenciales** |
| 6 | **Píxel propio** del mercado nuevo | Meta optimiza a ciegas. Nunca reusar el píxel de otro mercado |
| 7 | **Dominio o subdominio** en el idioma nuevo | Un dominio en español frente a un comprador anglo rompe la confianza |
| 7b | **Fan page e Instagram propios** en el idioma del mercado | Los anuncios salen firmados por una marca en otro idioma. Pasó una vez: la página salió en inglés para un mercado que no era anglo |

### Lo que hay que tener producido antes de prender

| # | Qué | Regla |
|---|---|---|
| 8 | 🔴 **Los entregables (PDF) en el idioma nuevo** | **Si no están, no se activa nada.** Vender sin entregar = reembolso |
| 9 | **Los VSL de los OTOs** en el idioma nuevo | Un video en español después de pagar rompe la confianza en el peor momento |

**Si 8 o 9 faltan:** no se frena la tienda. Se hace **todo lo demás**, y lo que depende de
un entregable o un video **queda fuera del embudo** hasta que exista. Se avisa cuál y por qué.

> **Producción:** ebooks → skill `imperioebook`. VSL de OTOs → skill `imperiootos`.
> **No rehacer a mano lo que ya está preseteado.**

---

# FASE 3 — Ejecutar. El orden no es opcional.

### 🔴 La moneda va ANTES de los mercados

`impultienda_cambiar_moneda` **apaga Markets siempre**, igual que el panel. Cambiarla
después de configurar precios por país **borra el trabajo**.

### 🔴 La moneda puede estar trabada

A **moneda única** (`ars`/`usd`) sólo se pasa **sin Stripe, Mercado Pago ni PayPal
conectados**; con alguno, la herramienta rechaza y devuelve el link del panel. A `ars`
tampoco se pasa con Whop prendido. **A multidivisa se pasa siempre**, aunque haya
pasarelas: conviven.

| Paso | Herramienta |
|---|---|
| 1 | `impultienda_cambiar_moneda` ← **primero** |
| 2 | `impultienda_cambiar_idioma` |
| 3 | Todo lo de la **Fase 4** |
| 4 | `impultienda_activar_markets` · `impultienda_asignar_paises` · `impultienda_precio_por_pais` |
| 5 | `impultienda_configurar_tracking` (el píxel del paso 6) |
| 5b | 🔴 **Microsoft Clarity propio de este idioma**: cada idioma es una tienda nueva y lleva su proyecto. Proyecto en clarity.microsoft.com (gratis, con la cuenta del alumno) → Nuevo proyecto (nombre = tienda, URL = dominio, sector "Comercio") → copiar el ID de 10 caracteres → `impultienda_configurar_tracking` con `clarity_id` (queda **pendiente** con un link de aprobación que vence en 30 min; más rápido: el alumno pega el ID en Configuración → Tracking → Microsoft Clarity → Project ID → Guardar cambios) → verificar `clarityId = "<ID>"` en el HTML publicado |

---

# FASE 4 — Los 13 lugares con idioma. Ninguno se saltea.

## 🔑 Lo que el cambio de idioma hace solo, y lo que no

`impultienda_cambiar_idioma` cambia **los mails al comprador** (entrega, carrito) y **los
textos fijos de la landing de plantilla**. Nada más.

| | Se traduce solo | Hay que traducirlo a mano |
|---|---|---|
| **Checkout** | ✅ La interfaz fija, **según el idioma de cada comprador** | 🔴 Todo lo que escribimos nosotros |
| **Landing** | Los textos fijos de plantilla | 🔴 El HTML propio, entero |
| **Productos** | — | 🔴 Nombre y descripción |

🔴 **De acá salió el error real:** se dio por hecho que el checkout quedaba traducido. La
interfaz sí; **el botón de pagar, el del bump y la barra de compradores son texto nuestro
y seguían en español.**

## La lista

| # | Lugar | Herramienta | Trampa |
|---|---|---|---|
| 1 | Idioma de la tienda | `impultienda_cambiar_idioma` | 17 códigos. **No hay `en-GB`**: UK va con `en-US` |
| 2 | Moneda | `impultienda_cambiar_moneda` | **Apaga Markets.** Va primero. 2 pasos + token |
| 3 | 🔴 **Título de la pestaña Y meta descripción** | `impultienda_cambiar_titulo_pagina` (hace las dos en **una** llamada) | **El que más se olvida.** Se ve en la pestaña y en Google. Es lo único de plantilla que SÍ se ve con `custom_html` |
| 4 | **Nombre y descripción de cada producto** | `impultienda_editar_producto` | Uno por uno, **incluidos bonos y upsells**. El nombre cambia el título del ebook |
| 5 | **La landing** | `impultienda_leer_html` → `impultienda_guardar_html` | 2 pasos + token. Ver abajo |
| 6 | **Textos del checkout** | `impultienda_configurar_checkout` | `texto_boton_pagar`, `texto_boton_bump`, `texto_barra_compradores`. **Los tres** |
| 7 | Bloques arriba/abajo del checkout | `impultienda_bloques_checkout` | Sólo tienda **clásica**. 2 pasos + token. La lista **reemplaza** la anterior |
| 8 | **Página de gracias** | `impultienda_configurar_agradecimiento` | Necesita **funnel ya creado** y plan pago |
| 9 | **Los entregables (PDF)** | `impultienda_cargar_entregable` | Ver abajo. Es el que genera reembolsos |
| 10 | **HTML de cada oferta post-compra** | `impultienda_leer_html_postcompra` → `impultienda_guardar_html_postcompra` | Upsell **y** downsell, cada uno con su `oferta_id` |
| 11 | Los VSL dentro de ese HTML | skill `imperiootos` | Audio **y** subtítulos quemados |
| 12 | FAQ y secciones de la landing | `impultienda_editar_texto_landing` (campos sueltos) · `impultienda_reemplazar_texto_landing` (beneficios, dolores, FAQ, testimonios, pasos) | 🔴 `editar_texto_landing` **no funciona con `custom_html`**, salvo `titulo_pestana` y `meta_descripcion` |
| 13 | Área de miembros, si existe | `impultienda_configurar_area_miembros` · `impultienda_guardar_contenido_miembros` | Categorías **y** contenido |

## 🔴 Nada de scripts de terceros ajenos al tracking

Todo script externo que no sea el píxel/tracking de la plataforma (por ejemplo píxeles de "protección" o
scripts de proveedores que no reconozcas) en la tienda base **no se copia a la traducida**: se revisa y se saca en
landing, Código (CSS/JS) y tracking. Lo mismo con las llaves que Impultienda
no reemplaza (`{{rating}}`, `{{social_proof_count}}`): solo `{{price}}`, `{{original_price}}`, `{{savings}}`, `{{currency}}`.

## 🔴 Traducir HTML: dos trampas

**1. El texto escondido en el CSS.** Hay frases en reglas `content:` que **no se ven
leyendo el HTML**:

```css
.hbc-save::before        { content: "Ahorrás "; }
.hbc-prize:empty::before { content: "un precio especial"; }
```

Traducir sólo el HTML visible deja la página **a medio idioma**. Buscar `content:` siempre.

**2. Los tokens no se traducen.** Se dejan **exactos**:

```
Landing:     {{price}} {{original_price}} {{savings}} {{currency}}
Post-compra: {price} {compare} {discount} {savings} {currency} {billing}
             {first-name} {timer} {product-title} {product-image}
             {order-number} {store-name} {thank-you-url}
Botones:     data-pp-accept   data-pp-decline
```

**Si se traduce un token o se pierde un `data-pp-*`, el botón deja de cobrar.**
`impultienda_leer_html_postcompra` devuelve la lista de tokens vigente en `tokens` y
avisa en `avisos` si faltan los botones: **leerlo, no confiar en esta lista.**

**3. El texto dentro de las imágenes.** Capturas de WhatsApp en prueba social, textos
quemados en el creativo, placas con precio. **No aparecen en ninguna búsqueda y no se
traducen.** Hay que mirar las imágenes una por una y rehacer las que tengan texto.

🔴 **La landing sale COMPLETA, con las imágenes ya en el idioma nuevo** (*si se crea la landing, ya se sube con imagen, con contexto, en el idioma y todo*). Las imágenes con texto
(hero, mockups, tapas, páginas de muestra, placas) **no quedan "pendientes"**: se rehacen en la misma corrida.
Así se hizo en una tienda real, y funcionó:
- Cada imagen se pasa a **ChatGPT (modelo Pro)** pidiéndole la misma imagen con el texto traducido. Respeta
  composición y traducciones exactas; ~1–2 min por imagen.
- **Landing larga en una sola imagen** (ej. 1000x6292): ChatGPT genera hasta **2:3**. Cortarla en tramos por
  los separadores, rellenar cada tramo a 2:3 con negro, traducir tramo por tramo y volver a unirlos. Si la unión
  cae sobre una textura (humo), **fundido de 40 px**; sobre separadores negros no se nota.
- **Revisar cada tramo a ojo**: una vez un tramo salió con el título repetido.
- Esperar ~8 s después de adjuntar antes de mandar el mensaje, o sale sin la imagen.
- Si no se puede hacer acá, pasarle el pedido a **Edición** con la lista exacta de imágenes. Pero no se publica
  la landing con imágenes en el idioma viejo.

🔴 **La prueba social REAL se traduce, no se borra.** Si los testimonios y el
contador vienen de ventas reales (por ejemplo de otra tienda del usuario), se traducen y se mantienen; los **nombres** pasan al idioma del país (ver REGLA 1). Lo único que se adapta al mercado nuevo
son las referencias a una **plataforma local**: sellos o logos de MercadoLibre, MercadoLíder o Mercado Pago no
tienen sentido en otro país. Ante la duda sobre si un dato es real, **preguntar, no borrar**.

**Cómo editar:** leer primero, y usar `reemplazos` (pares exactos) en vez de reenviar el
documento. **Máximo 40 pares por llamada** — una landing entera va en varias tandas.

## 🔴 El entregable: tres cosas que lo rompen

| Trampa | Qué pasa |
|---|---|
| El ebook se está **generando con IA** | No se puede cargar nada: la generación lo pisa. Esperar con `impultienda_estado_generacion` |
| Confirmar un PDF cuando había un **link** de entrega | **El link se borra.** Vuelve en `link_anterior_quitado` — guardarlo antes |
| PDF de más de **50 MB** | Se rechaza |

El modo `subir` **no marca nada como listo**: hay que hacer el PUT y después `confirmar`.

## 🔴 Si el idioma es árabe (`ar`)

Es **RTL**. El HTML necesita `dir="rtl"` y el layout invertido. No alcanza con traducir.

---

# FASE 5 — Verificar. Sin esto no está listo.

| # | Control | Cómo | Pasa si |
|---|---|---|---|
| 1 | **No quedó nada en el idioma viejo** | `impultienda_ver_landing` con `buscar` (palabra del idioma viejo: "Garantía", "Quiero", "método"…) — dice **en qué campo** quedó. Y leer los textos de la landing enteros | **0 coincidencias** |
| 2 | 🔴 **El título de la pestaña y la meta descripción** | `impultienda_ver_landing` → `campos_editables.titulo_pestana` y `.meta_descripcion` | Los dos en el idioma nuevo |
| 3 | **El CSS tampoco** | Buscar `content:` en cada HTML (landing y cada oferta) | Ninguna frase en el idioma viejo |
| 4 | **Los tokens están intactos** | Contar `{{price}}`, `{price}`, `data-pp-accept`, `data-pp-decline` antes y después | **Mismo número** |
| 5 | **Las imágenes con texto** | Abrirlas y mirarlas | Ninguna tiene texto del idioma viejo |
| 6 | **El checkout real** | Abrirlo en el navegador y leerlo | Ni una palabra del idioma viejo |
| 7 | **El PDF que llega** | Abrirlo | Está en el idioma nuevo |
| 8 | **El embudo muestra lo que tiene que mostrar** | `impultienda_ver_postcompra` | 🔴 Ver abajo |
| 9 | **Precios del mercado nuevo** | `impultienda_listar_productos` | No son los precios viejos convertidos |

### 🔴 Marcar un producto post-compra NO lo pone en el embudo

Son dos cosas distintas: la marca lo hace **elegible**, el **funnel** es el que lo
**muestra**. Una tienda puede tener tres upsells marcados y `funnels: []` — y entonces
cada comprador paga y se va. **Cero upsell.**

Revisar que el embudo exista, esté **activo**, y que cada oferta que debía entrar esté
adentro.

---

## 🔴 Las dos cosas que NO se hacen solas

| Qué | Por qué |
|---|---|
| **La compra de prueba** | Es lo único que prueba que el checkout cobra, que llega el mail, que el PDF se descarga en el idioma correcto y que el post-compra aparece. **Todo lo anterior puede estar "listo" y fallar acá** |
| **Activar lo que gasta** | Crear no gasta; activar sí. **Siempre lo aprueba el usuario** |

---

## Cómo se cierra

1. **Qué quedó andando**, lugar por lugar
2. **Qué quedó fuera y por qué** (el upsell sin video, por ejemplo)
3. **Lo que falta del usuario**, en una lista corta
4. Guardar el resultado en un archivo de notas del proyecto (por ejemplo `AAAA-MM-DD-idioma-<tienda>.md`)

---

## Errores que ya pasaron. No repetirlos.

| Error | Qué lo evita |
|---|---|
| 🔴 **Tienda en inglés con el título de la pestaña y la meta descripción en español.** Pasó de verdad: se detectó con campañas ya corriendo | Control 2 de la Fase 5. Con `custom_html` son los **únicos** dos textos de plantilla que se ven, y por eso nadie los mira |
| Dar por traducido el checkout | Los textos propios **nunca** se traducen solos |
| Traducir una landing `custom_html` con `editar_texto_landing` | No funciona ahí. Va por `guardar_html` con `reemplazos` |
| Dejar texto en español dentro de una imagen | Control 5. No sale en ninguna búsqueda |
| Traducir sólo el HTML visible | Buscar `content:` en el CSS |
| Cambiar la moneda al final | Apaga Markets. **Va primero** |
| Cargar el entregable mientras el ebook se generaba | `impultienda_estado_generacion` antes |
| Marcar los upsells y no crear el funnel | `impultienda_ver_postcompra`: `funnels: []` |
| Lanzar con el entregable en el idioma viejo | Control 5 de la Fase 5 |
| Rehacer a mano un VSL o un ebook | Usar `imperiootos` e `imperioebook` |
