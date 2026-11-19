# Templates de Prompts para Higgsfield

## FORMATO BASE (aplicar siempre)

Todo prompt = **PREÁMBULO + CUERPO + CIERRE**. Los templates y ejemplos de abajo
muestran solo el CUERPO: al mandarlo a Higgsfield se le pegan siempre el preámbulo
adelante y el cierre atrás.

**PREÁMBULO (siempre, primera línea):**

```
Flat single ebook page artwork, edge to edge, no book, no open magazine, no spread, no tablet or phone screen, no paper sheet with a shadow, no 3D mockup, no perspective.
```

**CUERPO:**

```
[TIPO DE PÁGINA], [DESCRIPCIÓN DEL LAYOUT], [CONTENIDO ESPECÍFICO],
[FOTO/IMAGEN PRINCIPAL], [PALETA DE COLORES], A4 vertical format 2:3 ratio,
[NOMBRE DE MARCA DEL PRODUCTO] brand
```

**CIERRE (siempre, última línea, en el idioma del ebook):**

```
All text in Spanish. Do not write any English word. Use only the numbers written here. Add no label or number beyond those listed.
```

🔴 **Nunca** "editorial" ni "magazine quality": hacen que el modelo dibuje una revista
abierta o un mockup con sombra. **Unidades en mm.** Números copiados tal cual de
`ficha_datos.md` o escritos en palabras.

> Los precios de los ejemplos son ilustrativos: en un ebook real salen de `ficha_datos.md`.

---

## PÁGINA 1/3 — PRESENTACIÓN

### Template Universal Página 1/3

```
Ebook page layout, professional [NICHO] pattern book, [TEMA/TEMPORADA].
LEFT SIDE (40%): white background, dark [COLOR PRINCIPAL] header bar at top with text
"[MARCA] · [AÑO/EDICIÓN]", [COLOR ACENTO] badge "[ÍTEM] [NÚMERO]", large bold title
"[NOMBRE DEL ÍTEM]" in [COLOR PRINCIPAL], description "[DESCRIPCIÓN 1-2 LÍNEAS]",
technical specs card with icons showing: [DATO 1], [DATO 2], [DATO 3], [DATO 4], [DATO 5],
[COLOR PRINCIPAL] price box with [COLOR ACENTO] text "[PRECIO]".
RIGHT SIDE (60%): full-height professional product photo of [DESCRIPCIÓN DEL PRODUCTO],
[DESCRIPCIÓN DEL CONTEXTO/FONDO/PROPS], soft natural lighting, commercial quality.
A4 vertical 2:3 ratio, clean minimal design,
[COLOR PRINCIPAL] [HEX], [COLOR SECUNDARIO] [HEX], [COLOR ACENTO] [HEX]
```

### Ejemplo — Crochet

```
Ebook page layout, professional crochet pattern book, Argentine Mundial 2026.
LEFT SIDE (40%): white background, dark navy header "LA MUNDIALERA · ARGENTINA 2026",
gold badge "PATRÓN 01", large bold title "LLAVERO PELOTA MUNDIALISTA" in dark navy,
description "Pelota tejida en celeste y blanco con argolla metálica. 60 mm. Principiante.",
technical specs with icons: Nivel: Principiante, Medidas: 60 mm diámetro, Hilo: Algodón Nro.4,
Aguja: 3.5mm, Tiempo: 45-60min, navy price box gold text "$4.500 ARS".
RIGHT SIDE (60%): full-height professional product photo of handmade crochet ball keychain
in light blue and white, metal keyring, white linen fabric, bamboo crochet hooks, natural light.
A4 vertical 2:3 ratio, navy #1A3A6B, sky blue #75AADB, gold #C8973A
```

### Ejemplo — Cocina/Repostería

```
Ebook page layout, professional baking recipe book, Argentine home baking collection.
LEFT SIDE (40%): white background, dark bordo header "DULCE ARGENTINA · COLECCIÓN 2026",
orange badge "RECETA 01", large bold title "ALFAJOR DE MAICENA CLÁSICO" in dark bordo,
description "El alfajor argentino de siempre. Suave, dulce y con dulce de leche generoso.",
technical specs with icons: Nivel: Fácil, Porciones: 24 unidades, Tiempo: 90 min,
Conservación: 5 días, Costo: $1.200 ARS, bordo price box orange text "$8.500 ARS el kit".
RIGHT SIDE (60%): professional food photography of homemade alfajores stacked on white plate,
powdered sugar dusting, dulce de leche visible between cookies, warm natural side lighting,
white marble background, rustic linen napkin. A4 vertical 2:3,
bordo #8B1A1A, orange #F5A623, cream #FFF8EC
```

### Ejemplo — Fitness

```
Ebook page layout, professional fitness guide, home workout collection.
LEFT SIDE (40%): white background, dark green header "ENTRENÁ EN CASA · PROGRAMA 8 SEMANAS",
light green badge "EJERCICIO 01", large bold title "SENTADILLA CON PESO CORPORAL" in dark green,
description "El ejercicio base de todo entrenamiento. Quema calorías y fortalece piernas y glúteos.",
technical specs with icons: Nivel: Principiante, Series: 3x15 reps, Descanso: 60 seg,
Músculos: Cuádriceps/Glúteos, Calorías: ~45 kcal, green price box teal text "SEMANA 1 · DÍA 1".
RIGHT SIDE (60%): professional fitness photo of woman doing perfect squat form, athletic wear,
home gym background, bright natural lighting, motivational aesthetic.
A4 vertical 2:3, dark green #1A4A2E, teal #7EC8A4, white #FFFFFF
```

---

## PÁGINA 2/3 — INSTRUCCIONES / RECETA / PASO A PASO

### Template Universal Página 2/3

```
Ebook page layout, [TIPO] instructions page, clean white background, A4 vertical.
TOP: dark [COLOR PRINCIPAL] header "[TÍTULO SECCIÓN] · [ÍTEM NÚMERO] · [NOMBRE ÍTEM]".
Small thumbnail photo of finished [PRODUCTO] top right corner.
LEFT COLUMN: [TIPO DE LISTA] with numbered circles: [ITEM 1], [ITEM 2], [ITEM 3], [ITEM 4],
[ITEM 5], [ITEM 6]. [TIPO GLOSARIO] box: [TÉRMINO 1]=[DEF], [TÉRMINO 2]=[DEF], [TÉRMINO 3]=[DEF].
RIGHT COLUMN: step by step numbered cards alternating [COLOR 1] and [COLOR 2]:
[PASO 1 descripción], [PASO 2 descripción], [PASO 3], [PASO 4], [PASO 5], [PASO 6],
[PASO 7], [PASO 8], [PASO 9]. Bottom [COLOR PRINCIPAL] "[TÍTULO FINAL]" completion box:
"[INSTRUCCIÓN FINAL]". Professional typography, [COLOR PRINCIPAL] and [COLOR ACENTO] scheme
```

### Ejemplo — Crochet

```
Ebook page layout, crochet recipe page, clean white background, A4 vertical.
TOP: dark navy header "RECETA TÉCNICA · PATRÓN 01 · LLAVERO PELOTA MUNDIALISTA".
Small thumbnail photo of finished crochet ball keychain top right.
LEFT COLUMN materials list numbered circles: 1.Hilo algodón celeste 15g, 2.Hilo blanco 10g,
3.Aguja 3.5mm, 4.Relleno fibra 10g, 5.Argolla metálica, 6.Packaging bolsita + tag.
Abbreviations box: pb=punto bajo, aum=aumento, dism=disminución, MR=anillo mágico.
RIGHT COLUMN step cards navy and gold alternating: V1 MR 6pb (6), V2 6 aum (12),
V3 *1pb 1aum* x6 (18), V4 *2pb 1aum* x6 (24), V5-V7 24pb rectas, V8 cambiar blanco 24pb,
V9 *2pb 1dism* x6 (18) rellenar, V10 *1pb 1dism* x6 (12), V11 6 dism cerrar.
Bottom navy ACABADO box: "Coser argolla firmemente. Esconder hebras."
Professional typography, navy and gold color scheme
```

### Ejemplo — Repostería

```
Ebook recipe page, baking instructions, clean white background, A4 vertical.
TOP: dark bordo header "RECETA TÉCNICA · RECETA 01 · ALFAJOR DE MAICENA".
Small thumbnail photo of finished alfajores top right.
LEFT COLUMN ingredients numbered circles: 1.Manteca 200g, 2.Azúcar impalpable 120g,
3.Maicena 300g, 4.Harina 100g, 5.Yemas 3 unidades, 6.Dulce de leche 400g.
KEY BOX: T°=temperatura, MP=molde plano, C.s.=cantidad suficiente.
RIGHT COLUMN step cards bordo and orange alternating: Paso 1 Batir manteca y azúcar hasta cremar,
Paso 2 Agregar yemas de a una integrando bien, Paso 3 Incorporar harina y maicena tamizadas,
Paso 4 Formar cilindro y refrigerar 30 minutos, Paso 5 Cortar rodajas de 10 mm,
Paso 6 Hornear 160°C 12-15 min sin dorar, Paso 7 Enfriar completamente antes de rellenar,
Paso 8 Rellenar con dulce de leche generoso, Paso 9 Rebozar en coco rallado o glasé.
Bottom bordo CONSEJO box: "No hornear de más — la maicena debe quedar blanca."
Professional food styling typography, bordo and orange scheme
```

---

## PÁGINA 3/3 — GRÁFICO + APLICACIONES + VENTA

### Template Universal Página 3/3

```
Ebook page, [TIPO] chart and [APLICACIONES/USOS] page, A4 vertical, white background.
[COLOR ACENTO] header "GRÁFICO Y [SECCIÓN] · [ÍTEM NÚMERO] · [NOMBRE ÍTEM]".
LEFT COLUMN: [TIPO DE DIAGRAMA TÉCNICO] showing [DESCRIPCIÓN DEL DIAGRAMA],
[SÍMBOLOS/LEYENDA], [NÚMEROS/ETIQUETAS], [VISTAS ADICIONALES].
Below: [LEYENDA/REFERENCIAS] box with symbol explanations.
RIGHT COLUMN: table "[TÍTULO TABLA]" with rows [VARIANTE 1/datos], [VARIANTE 2/datos],
[VARIANTE 3/datos]. Section "4 [APLICACIONES/USOS/CONTEXTOS]" with icon cards:
[APP 1]/[APP 2]/[APP 3]/[APP 4].
Bottom [COLOR PRINCIPAL] price box "[PRECIO] · [MARGEN/BENEFICIO]".
[COLOR PRINCIPAL] [HEX], [COLOR SECUNDARIO] [HEX], [COLOR ACENTO] [HEX]
```

### Ejemplo — Crochet

```
Ebook page, crochet chart and sales page, A4 vertical, white background.
Gold header "GRÁFICO Y VENTA · PATRÓN 01 · LLAVERO PELOTA".
LEFT COLUMN: crochet stitch diagram of sphere showing concentric circular rounds,
X symbols for single crochet, increase/decrease arrows, round numbers 1-11 on side.
Below front view and side view drawings of ball 60 mm with keyring.
Legend: X=punto bajo, up-arrow=aumento, down-arrow=disminución.
RIGHT COLUMN: table MEDIDAS POR TALLE rows P=50 mm/20g/35min, M=60 mm/25g/45min, G=70 mm/32g/60min.
Section 4 APLICACIONES DE VENTA icon cards: Llavero/Souvenir/Corporativo/Merchandising.
Bottom navy price box "$4.500 ARS · Margen 75%".
Navy #1A3A6B, sky blue #75AADB, gold #C8973A
```

### Ejemplo — Cocina

```
Ebook page, baking diagram and sales page, A4 vertical, white background.
Orange header "DIAGRAMA Y VENTA · RECETA 01 · ALFAJOR DE MAICENA".
LEFT COLUMN: cross-section diagram of alfajor showing layers: bottom cookie/dulce de leche
filling/top cookie/glazing coat, measurements and thickness labels, temperature diagram
showing 160°C oven icon, storage diagram showing 5-day shelf life.
Below: front view circle 50 mm diameter, side view showing 25 mm height.
Legend: color codes for each layer.
RIGHT COLUMN: table VARIANTES rows Mini=30 mm/1 cda DDL, Clásico=50 mm/2 cdas DDL,
Grande=70 mm/3 cdas DDL. Section 4 FORMAS DE VENDER icon cards:
Por unidad/Caja x12/Kit regalo/Pedidos evento.
Bottom bordo price box "$8.500 ARS la caja x12 · Margen 70%".
Bordo #8B1A1A, orange #F5A623, cream #FFF8EC
```

### Ejemplo — Fitness

```
Ebook page, fitness diagram and workout page, A4 vertical, white background.
Teal header "DIAGRAMA Y RUTINA · EJERCICIO 01 · SENTADILLA".
LEFT COLUMN: anatomical body diagram showing muscles activated in squat: quadriceps/glutes
/hamstrings highlighted in teal green, correct posture angles marked 90°, back straight arrow,
knees tracking toes indicator, two-position diagram showing start and bottom position.
Below: common mistakes diagram showing wrong vs right form with red X and green checkmark.
RIGHT COLUMN: table PROGRESIÓN SEMANAL rows Semana 1=3x10 reps, Semana 2=3x12,
Semana 3=3x15, Semana 4=4x15. Section 4 VARIANTES icon cards:
Con peso/Con salto/En una pierna/Con banda. 
Bottom dark green box "PROGRAMA COMPLETO 8 SEMANAS · 3 días/semana".
Dark green #1A4A2E, teal #7EC8A4, light green background #F0F7F4
```

---

## PORTADA

### Template Portada

```
Professional ebook cover design, [NICHO] themed, [NOMBRE EBOOK].
Dark [COLOR PRINCIPAL] background with subtle [TEXTURA/PATRÓN DECORATIVO].
Decorative circles and [ELEMENTO DECORATIVO NICHO] in darker shade of [COLOR PRINCIPAL].
[ELEMENTOS DECORATIVOS] scattered across background.
TOP: [COLOR ACENTO] text "[MARCA] PRESENTA".
CENTER: Large bold title "[LÍNEA 1 TÍTULO]" in white, "[LÍNEA 2 TÍTULO]" in [COLOR SECUNDARIO],
"[SUBTÍTULO]" in white bold, decorative [COLOR ACENTO] horizontal line.
[COLOR ACENTO] badge "[EDICIÓN/COLECCIÓN]".
Content preview box: 5 bullet points with icons listing main contents.
3 stat badges showing [NÚMERO 1] [LABEL], [NÚMERO 2] [LABEL], [NÚMERO 3] [LABEL].
Quote box: "[FRASE MOTIVACIONAL DEL NICHO]".
Bottom: "[MARCA] ® · [AÑO]" in muted [COLOR].
A4 vertical 2:3 ratio, premium clean design, [COLOR PRINCIPAL] [HEX], [COLOR SEC] [HEX], [COLOR ACENTO] [HEX]
```

---

## SEPARADOR DE CATEGORÍA

### Template Separador

```
Professional ebook category divider page, [NICHO] themed, full page.
Solid [COLOR DE CATEGORÍA] background with decorative circles in darker shade.
Scattered [ELEMENTO DECORATIVO] icons.
TOP stripes: alternating [COLOR SEC] and white horizontal stripes 20px tall.
BOTTOM stripes: same pattern.
Centered content:
"[NOMBRE EBOOK] · EDICIÓN [AÑO]" in [COLOR ACENTO] small caps.
"CATEGORÍA [LETRA/NÚMERO]" in white medium.
Giant decorative letter "[LETRA]" in [COLOR ACENTO] font size 200+.
"[NOMBRE DE CATEGORÍA]" in white large serif font.
"[NÚMERO] [tipo de ítems] · [NIVEL]" in [COLOR SEC].
List of [NÚMERO] items with [COLOR ACENTO] numbered circles and white text.
Bottom [COLOR ACENTO] badge "[RANGO DE PRECIOS]".
A4 vertical 2:3, [COLOR CATEGORÍA] [HEX], [COLOR ACENTO] [HEX], white
```
