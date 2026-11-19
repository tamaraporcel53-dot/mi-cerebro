# Checklist de calidad del ebook

Se pasa **entera** antes de dar un ebook por terminado y antes de cargarlo en la tienda.
Un solo item en rojo y no se entrega. Si un item no se puede verificar, se dice cuál y por qué.

---

## 1. Antes de generar

- [ ] Existe `ficha_datos.md` en la carpeta del producto y el usuario la aprobó
- [ ] Todas las medidas de la ficha están **en mm** (o en la unidad del mercado, si es una traducción)
- [ ] Existe `plan_paginas.md` con una fila por página: número, archivo, tipo, título, estado
- [ ] Créditos calculados (páginas × costo + 15%) y saldo consultado con `balance`
- [ ] Muestra de 3 páginas generada y **aprobada por el usuario** antes del lote

## 2. Cada prompt

- [ ] Abre con el preámbulo fijo: `Flat single ebook page artwork, edge to edge, no book, no open magazine, no spread, no tablet or phone screen, no paper sheet with a shadow, no 3D mockup, no perspective.`
- [ ] Cierra con el idioma: `All text in Spanish. Do not write any English word.` (o el idioma del ebook)
- [ ] Cierra con `Use only the numbers written here. Add no label or number beyond those listed.`
- [ ] **No** contiene "editorial" ni "magazine quality"
- [ ] `A4 vertical, 2:3 ratio`
- [ ] Paleta en hex
- [ ] Número de ítem visible
- [ ] Cada número copiado tal cual de `ficha_datos.md`, o escrito en palabras
- [ ] Unidades en mm, nunca cm
- [ ] Diagramas: una sola pieza aislada, no el objeto entero
- [ ] Cuerpo de ~120 palabras como máximo (sin contar preámbulo y cierre)

## 3. Cada página generada

- [ ] Es una página plana a sangre: sin libro abierto, sin revista, sin pantalla, sin sombra, sin perspectiva
- [ ] Todo el texto en el idioma del ebook, **ni una palabra en otro idioma**
- [ ] Los números coinciden con la ficha, uno por uno
- [ ] Sin texto de relleno en tarjetas ni palabras inventadas
- [ ] Sin etiquetas de capas o partes que no se pidieron
- [ ] Sin glifos rotos ni letras deformadas en títulos
- [ ] La paleta es la del resto del ebook
- [ ] **No aparece la marca Imperio** en ningún lado

## 4. Estructura del ebook

- [ ] Portada con la marca del producto
- [ ] Índice + bienvenida
- [ ] Separador por cada categoría
- [ ] **Exactamente 3 páginas por ítem** (presentación / instrucciones / diagrama)
- [ ] Página 3 con un diagrama distinto según el tipo de ítem
- [ ] Sistema de negocio, si el ebook es para vender (3 escenarios de ganancia, márgenes bien calculados)
- [ ] Página de cierre

## 5. El índice contra el PDF real 🔴

- [ ] Páginas del PDF (`len(PdfReader(pdf).pages)`) = filas de `plan_paginas.md`
- [ ] **Ningún número del índice es mayor que la cantidad de páginas del PDF**
- [ ] Cada entrada del índice cae en la página donde de verdad empieza esa sección
- [ ] Si el ebook se tradujo, el índice se verificó **antes** de traducir

> Caso que origina la regla: un índice que prometía hasta la página 149 en un PDF de 60.

## 6. Traducción (si aplica)

- [ ] Se chequeó si el PDF tiene texto extraíble antes de elegir método
- [ ] Con texto → reconstrucción con código (0 créditos). Con imagen → `gpt_image_2_5` por referencia
- [ ] Cada prompt de edición enumera todas las cadenas, una por una
- [ ] Unidades localizadas (pulgadas, °F, fl oz, oz) según el mercado
- [ ] Marcas y referencias locales reemplazadas por las del país de destino
- [ ] `ficha_datos.md` traducida, con unidades convertidas
- [ ] Contenido que no se puede vender en ese mercado, reemplazado (no traducido)

## 7. Archivo final y carga

- [ ] PDF en el orden del plan (`p001_`, `p002_`…)
- [ ] 150 DPI como mínimo
- [ ] **50 MB o menos** (es el tope de Impultienda)
- [ ] Nombre de archivo profesional (no `ebook_v3_final_DEFINITIVO.pdf`)
- [ ] Metadatos del PDF sin la marca Imperio
- [ ] Cargado con `impultienda_cargar_entregable` (`subir` → PUT → `confirmar`)
- [ ] Si había link externo de entrega, el usuario sabe que se quitó
- [ ] Compra de prueba pedida al usuario: **no se afirma que el comprador lo recibe sin ella**
