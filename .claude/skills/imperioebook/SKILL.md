---
name: imperioebook
description: Se llama con "imperioebook". Produce ebooks infoproducto página por página con Higgsfield por MCP (Nano Banana Pro 2K), con los números sacados de una ficha de datos bloqueada, arma el PDF, verifica que el índice coincida con las páginas reales y lo carga como entregable en Impultienda. También traduce ebooks ya hechos a otro idioma, eligiendo el método más barato según si el PDF tiene texto o es imagen. Usar SIEMPRE que el usuario pida crear un ebook, infoproducto, PDF de patrones, guía visual, kit digital, libro de recetas, manual de instrucciones o cualquier producto digital con páginas visuales. También usar cuando mencione "prompts para ebook", "páginas para Higgsfield", "generar infoproducto", "kit de patrones", "ebook de [cualquier nicho]", "traducir el ebook", "pasar el libro a inglés", "cargar el PDF en la tienda" o pida crear contenido visual para vender digitalmente.
---

# Skill: Producción de ebooks con Higgsfield

## Qué hace esta skill

Produce el ebook entero, no solo los prompts. Cada página es una imagen generada en
Higgsfield **por MCP**, se ensambla en PDF, se verifica y se carga en la tienda.

**Resultado:** PDF con fotos de producto, diagramas técnicos, tablas y paso a paso, con
los números del producto tomados de una ficha que no se inventa, y con un índice que
apunta a páginas que existen.

**Tres caminos, elegir antes de arrancar:**

| Camino | Cuándo | Costo |
|---|---|---|
| **A. Higgsfield por MCP** (el principal) | Ebook nuevo con diseño propio | ~2 créditos por página |
| **B. Atajo de Impultienda** | Bono o producto rápido, cuando alcanza con el ebook que genera la plataforma | 1 ebook del cupo mensual del plan |
| **C. Traducir** un ebook existente | Producto validado que va a otro idioma | 0 créditos si tiene texto · 2,75 por página si es imagen |

---

## Reglas fijas (salen de lotes fallados, no se discuten)

1. **Ficha de datos bloqueada.** Los números del producto (medidas, cantidades, tiempos,
   precios, resultados) salen de `ficha_datos.md` y de ningún otro lado. Ver Paso 1
2. **Muestra chica antes del lote.** 3 páginas (un ítem completo), aprobación del usuario,
   recién ahí el resto. Nunca un lote completo a ciegas
3. **El índice tiene que coincidir con el PDF.** Ya pasó: índice que prometía hasta la
   página 149 en un PDF de 60. Ver Paso 6
4. **La marca Imperio no aparece adentro del producto.** Ni en headers, ni en pies, ni en
   metadatos del PDF. La marca que va es la del producto
5. **Por MCP no hay ilimitado.** Todo lo que se genera por MCP descuenta créditos aunque la
   cuenta tenga plan ilimitado (lo dice la documentación de Higgsfield). Nunca pasar
   `use_unlim: true` salvo que el usuario lo pida explícito
6. **Antes de traducir un PDF, fijarse si tiene texto extraíble.** Si tiene, no se regenera
   con IA

---

## Camino A — Ebook nuevo con Higgsfield por MCP

### PASO 1 — Relevamiento y ficha de datos

Obtener del usuario (o de la conversación, sin volver a preguntar lo que ya dijo):

```
1. NICHO: ¿De qué trata el ebook?
2. AVATAR: ¿A quién le vende?
3. PROMESA: ¿Qué resultado concreto obtiene quien compra?
4. PRODUCTO: ¿Cuántos patrones/recetas/ejercicios/capítulos tiene?
5. PRECIO: ¿Cuánto va a valer el ebook?
6. PALETA: ¿Colores de la marca? (si no tiene, sugerir según nicho)
7. NOMBRE: ¿Cómo se llama el ebook y la marca del producto?
8. IDIOMA: ¿En qué idioma va el texto de las páginas?
9. CARPETA: ¿Dónde vive el producto en la computadora?
```

Con eso, armar en la carpeta del producto **`ficha_datos.md`**: una tabla por ítem con cada
número que va a aparecer en las páginas (medidas **en mm**, pesos, tiempos, cantidades,
precios sugeridos, márgenes).

🔒 **La ficha queda bloqueada:** una vez que el usuario la aprueba, no se cambia un número sin
que él lo diga. Los prompts copian los números de la ficha **literalmente**. Si un dato no
está en la ficha, no va en la página: se pregunta.

Si el producto ya tiene `ficha_datos.md`, se usa esa. No se arma otra.

### PASO 2 — Plan de páginas

Arquitectura base (adaptar según nicho):

```
PORTADA (1 pág)
ÍNDICE + BIENVENIDA (2 págs)
[SEPARADOR CATEGORÍA] × cant. categorías (1 pág c/u)
[ÍTEM/PATRÓN/RECETA] × cantidad total:
  └── Pág 1/3: Presentación + foto producto
  └── Pág 2/3: Instrucciones paso a paso
  └── Pág 3/3: Gráfico/diagrama + aplicaciones/usos
SISTEMA DE NEGOCIO (3-5 págs) — si el ebook es para vender
CIERRE (1 pág)
```

Escribir **`plan_paginas.md`** en la carpeta del producto: una fila por página con
número de página final, archivo (`p001_portada.png`…), tipo, título y estado
(pendiente / generada / aprobada / rehacer).

🔑 **El índice se escribe desde este plan, no de memoria.** Los números de página del
índice son los números de la columna del plan. Así coinciden por construcción.

### PASO 3 — Créditos

```
Total páginas = (ítems × 3) + portada + índice + bienvenida + separadores + sistema de negocio + cierre
Total créditos = total páginas × 2   (Nano Banana Pro 2K)
Margen para rehacer: +15%
```

Consultar el saldo con la herramienta `balance` de Higgsfield y confirmar el costo exacto de
una página con `get_cost: true` antes del primer lote. Si no alcanza, decírselo al usuario con
el número antes de empezar. Ojo con los créditos del plan: suelen renovarse por mes y **no
acumularse**, y los paquetes comprados tienen vencimiento; revisarlo en tu cuenta de Higgsfield.

### PASO 4 — Prompts

Cada prompt sigue los templates de `references/prompt-templates.md` y esta fórmula:

**Abrir siempre con (preámbulo fijo):**

```
Flat single ebook page artwork, edge to edge, no book, no open magazine, no spread, no tablet or phone screen, no paper sheet with a shadow, no 3D mockup, no perspective.
```

**Cerrar siempre con (cierre fijo, adaptando el idioma):**

```
All text in Spanish. Do not write any English word. Use only the numbers written here. Add no label or number beyond those listed.
```

Si el ebook va en otro idioma: `All text in English. Do not write any Spanish word.` (o el
que corresponda).

**En el medio:**
- Formato: `A4 vertical, 2:3 ratio`
- Paleta en hex
- Número de ítem visible (para seguimiento)
- Todo el texto de la página escrito entre comillas, en el idioma del ebook
- Números: **en palabras**, o copiados tal cual de la ficha (por eso va el cierre
  "Use only the numbers written here")
- **Unidades en mm**, nunca cm
- Máximo ~120 palabras de cuerpo (el preámbulo y el cierre no cuentan)

🔴 **Nunca escribir "editorial" ni "magazine quality"** en un prompt. Empujan al modelo a
dibujar una revista abierta o un mockup con sombra en vez de la página plana.

**Fallas conocidas a vigilar:** texto de relleno en tarjetas · etiquetas de capas
inventadas · diagramas con un objeto entero cuando se pidió una sola pieza (pedir **una
sola pieza aislada**).

### PASO 5 — Generar por MCP

1. **Muestra:** las 3 páginas del primer ítem con `generate_image` (modelo
   `nano_banana_pro`, `aspect_ratio: "2:3"`, resolución 2K; confirmar el id y el parámetro
   de resolución con `models_explore` la primera vez). Mostrarle las tres al usuario y
   **esperar su OK sobre el estilo**
2. **Lote:** con el estilo aprobado, `generate_image_batch` de hasta 12 páginas por envío,
   con `index` = número de página del plan. Seguir con `jobs_wait` en grupos de 12
3. **Mostrar:** cuando todo el lote terminó, un solo `show_generation_by_ids` con todos
   los jobs
4. **Bajar:** cada resultado a `paginas/` con el nombre del plan (`p007_patron01_pag3.png`)
   y marcar el estado en `plan_paginas.md`
5. **Revisar cada página** contra la ficha: números, unidades, texto en el idioma correcto,
   sin palabras inventadas. Las que fallan van a "rehacer" y se regeneran solas, sin
   rehacer el lote

Si un envío da timeout, **no reenviar a ciegas**: primero resolver qué jobs se crearon
(se cobran igual).

### PASO 6 — Ensamblar y verificar el índice

Ensamblar con `references/assembly-script.md`. Después, **antes de dar el PDF por bueno**:

```python
from pypdf import PdfReader
n = len(PdfReader("ebook_final.pdf").pages)
print("Páginas del PDF:", n)
```

- `n` tiene que ser igual a la cantidad de filas de `plan_paginas.md`
- **Ningún número del índice puede ser mayor que `n`**
- Abrir la imagen del índice y comparar cada entrada contra el plan: el título de cada
  sección tiene que caer en la página que dice

Si no coincide, se rehace la página del índice. Nunca se entrega un PDF cuyo índice
apunta a páginas que no existen.

Pasar después la checklist completa: `references/quality-checklist.md`.

### PASO 7 — Cargar en Impultienda

Con el PDF aprobado (máximo 50 MB), por el MCP de Impultienda:

1. `impultienda_listar_productos` para el `item_id` del ebook (preguntar sobre qué
   tienda se trabaja si no está claro)
2. `impultienda_cargar_entregable` modo `subir` → devuelve URL firmada y `ruta`
3. Subir el PDF con `curl -X PUT -H "Content-Type: application/pdf" --data-binary @archivo.pdf "URL"`
4. `impultienda_cargar_entregable` modo `confirmar` con la misma `ruta`

⚠️ Confirmar quita el link externo de entrega si había (lo devuelve en
`link_anterior_quitado`). **No decir que el comprador ya lo recibe:** pedirle al usuario una
compra de prueba.

---

## Camino B — Atajo de Impultienda

La plataforma genera contenido y PDF solos, con su IA. Consume **1 ebook del cupo mensual
del plan**, no créditos de Higgsfield.

1. `impultienda_generar_ebook` **sin** `confirmar` → vista previa con el cupo del mes y un
   `token`. Mostrársela al usuario
2. Con su OK explícito: `impultienda_generar_ebook` con `confirmar: true` y el `token` →
   devuelve `job_id`
3. `impultienda_estado_generacion` cada 30-60 segundos hasta que termine
4. Pedirle al usuario que lo abra en el panel y lo revise. Si después se quiere reemplazar
   por un PDF propio, `impultienda_cargar_entregable` (Paso 7)

⚠️ Si el producto se entrega hoy con un link externo, la generación **no corre** (el
comprador recibiría el link antes que el PDF). Si el ebook ya tenía contenido, lo pisa: la
vista previa lo avisa.

Usa solo nombre y descripción del producto: no conoce la ficha de datos. **Revisar los
números contra `ficha_datos.md` antes de dejarlo publicado.**

---

## Camino C — Traducir un ebook existente

### 1. ¿Tiene texto o es imagen?

```python
import fitz  # pymupdf
doc = fitz.open("ORIGINAL.pdf")
chars = sum(len(p.get_text().strip()) for p in doc)
print(len(doc), "páginas,", chars, "caracteres de texto")
```

### 2a. Tiene texto → reconstruir con código, 0 créditos

Se extrae el texto y las fotos del PDF original (pymupdf), se escribe el contenido
traducido y se reconstruye el diseño con un script propio (por ejemplo HTML + CSS →
PDF, o reportlab), manteniendo portada, índice, capítulos y páginas de cuerpo. Devuelve
texto seleccionable y no gasta créditos de IA.

```
# 1. extraer estructura y fotos del original
#    (fitz: page.get_text("dict"), page.get_images())
# 2. escribir el contenido traducido en una estructura (lista de páginas con su tipo:
#    portada, índice, capítulo, cuerpo, destacado)
# 3. renderizar a PDF con tu plantilla y verificar páginas e índice (Paso 6)
```

### 2b. Es imagen → `gpt_image_2_5` por referencia, 2,75 créditos por página

Se sube la página original como **imagen de referencia** (`media_upload` → `medias`) y se
pide la misma página con el texto cambiado, **enumerando cada cadena una por una**:

```
Flat single ebook page artwork, edge to edge, no book, no open magazine, no spread, no tablet or phone screen, no paper sheet with a shadow, no 3D mockup, no perspective.
Reproduce this exact page with the SAME layout, SAME illustration, SAME colours,
SAME fonts and SAME composition. Change ONLY the text, from Spanish to English,
keeping each piece of text in exactly the same position and the same visual weight:
- heading 'X' becomes 'Y'
- label 'X' becomes 'Y'
...
All text in English. Do not write any Spanish word.
Do not change the drawing, the icons or the layout.
```

🔑 Sin la lista explícita el modelo traduce de memoria y se saltea etiquetas.

🔴 **No usar kie.ai para esto** aunque sea más barato: sus endpoints son de imagen-a-imagen,
redibujan la página y rompen el texto. Solo el modo edición de Higgsfield conserva el diseño.

Costo: páginas × 2,75. Consultar saldo antes y avisar si no alcanza.

### 3. Localizar, no traducir

- **Unidades:** mm/cm → pulgadas, °C → °F, ml → fl oz, g → oz, según el mercado
- Marcas, tiendas y productos locales → equivalentes del país de destino
- Precios y moneda del mercado nuevo
- **`ficha_datos.md` también se traduce**, con las unidades convertidas, y queda bloqueada
  para la versión nueva

### 4. Antes de traducir, limpiar el contenido

- **Verificar el índice contra las páginas reales** (Paso 6). Traducir un índice roto
  arrastra el error al otro idioma
- Sacar lo que no se puede vender en el mercado nuevo (ejemplo real: un capítulo que se
  sacó de la landing por riesgo no se traduce, se reemplaza)

Para pasar la tienda entera a otro idioma, la skill es `imperiotranslate`; esta cubre el
ebook.

---

## Estructura de 3 páginas por ítem (universal)

### Página 1/3 — PRESENTACIÓN

**Izquierda 40%:** header con la marca del producto · badge numerado del ítem · título
grande en 2-3 líneas · descripción corta · ficha técnica con 5 datos (de `ficha_datos.md`)
· box de precio/valor con color de acento.

**Derecha 60%:** foto del producto o resultado terminado.

### Página 2/3 — INSTRUCCIONES

**Izquierda 40%:** materiales/ingredientes/herramientas numerados · box de abreviaturas
· medida/tiempo/porción final.

**Derecha 60%:** miniatura de la foto (esquina superior) · pasos numerados en cards
alternando colores · box de acabado/consejo final.

### Página 3/3 — GRÁFICO + APLICACIONES

**Izquierda 40%:** diagrama técnico (una sola pieza aislada) · leyenda · vistas frontal y
lateral con medidas en mm.

**Derecha 60%:** tabla de variantes/talles/porciones · 4 aplicaciones o contextos de venta
· box de precio con margen.

---

## Paletas por nicho (referencias rápidas)

| Nicho | Principal | Acento | Fondo |
|-------|-----------|--------|-------|
| Crochet/tejido | #1A3A6B navy | #C8973A dorado | #F4F7FB |
| Cocina/repostería | #8B1A1A bordo | #F5A623 naranja | #FFF8EC |
| Fitness/yoga | #1A4A2E verde oscuro | #7EC8A4 verde claro | #F0F7F4 |
| Carpintería/DIY | #3D2B1F marrón | #D4A853 madera | #F5F0E8 |
| Belleza/skincare | #6B2D5E violeta | #F5C6D0 rosa | #FFF5F8 |
| Pet care | #1A3D6B azul | #FF8C42 naranja | #F0F7FF |
| Jardinería | #2D5A1B verde | #C8973A dorado | #F4F9F0 |
| Finanzas | #0A2540 azul marino | #00D4AA teal | #F0F8FF |

## Tipos de diagrama para Página 3/3 por nicho

**Crochet/tejido:** esquema de puntos circular o rectangular con símbolos X
**Cocina:** montaje del plato, corte de ingredientes, temperaturas
**Fitness:** diagrama corporal con músculos activados, ángulos del ejercicio
**Carpintería:** plano técnico con medidas en mm, cortes, ensamble
**Belleza:** zonas del rostro, capas del producto
**Repostería:** capas del postre, decoración, temperaturas
**Jardinería:** plantación, espaciado, profundidad

---

## Archivos de referencia

- `references/prompt-templates.md` — templates de prompts por tipo de página
- `references/nicho-examples.md` — ejemplos completos de 3 páginas para varios nichos
- `references/assembly-script.md` — script Python para ensamblar el PDF y calculadora de créditos
- `references/quality-checklist.md` — checklist obligatoria antes de entregar o cargar el ebook

Leer el archivo de referencia que corresponda según la tarea.
