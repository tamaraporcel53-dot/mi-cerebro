# Generar imágenes con Higgsfield

Casi ningún vendedor de infoproductos tiene fotos de resultados. Se generan, y quedan mejor que las que sacaría con el celular.

Requiere que el usuario tenga el MCP de Higgsfield conectado. Si no lo tiene, seguí con lo que haya en la carpeta y avisale que con Higgsfield podés generarle las fotos que faltan.

---

## Cuántas: 10 por landing

Toda landing con testimonios lleva **10 imágenes generadas**. No es un extra: es parte del armado.

- **5** para el carrusel que va debajo de la garantía (formato **1:1**)
- **5** para las primeras tarjetas del muro de opiniones del final (formato **4:3**)

Leé cada testimonio y generá **la escena que esa persona cuenta**. Si dice "lo hice con mi hija antes de dormir", la imagen es esa escena — el objeto, el ambiente, la luz — sin caras. Si dice "lo usé en unas piezas de la moto", es eso. Una imagen genérica del rubro no sirve: la gracia es que la foto y el texto cuenten lo mismo.

## Qué generar

| Para qué | Qué pedir |
|---|---|
| Carrusel de resultados | El objeto terminado, uno por escena distinta |
| Muro de opiniones | Una foto de resultado por tarjeta (las primeras 5-6) |
| Proceso | La técnica en acción, sin que se vea la cara |
| Setup | Los materiales sobre una mesa: "esto es todo lo que necesitás" |

**Objetos, resultados y proceso: sí.** Caras de personas presentadas como clientes: no. Ver `05-criterio-y-riesgos.md`.

---

## Cómo se hace

### 1. Elegir modelo

```
models_explore(action:'recommend', type:'image', input:'text',
  query:'photorealistic product photography of a physical object, ultra realistic smartphone-style photo')
```

**`recraft_v4_1`** con `model_type` por defecto es el que mejor da para esto: fotorrealista, sin ese brillo plástico de IA.

### 2. Generar en lote

Todas juntas con `generate_image_batch` (hasta 12), después `jobs_wait`:

```
generate_image_batch(requests: [
  { index: 1, params: { model:'recraft_v4_1', aspect_ratio:'1:1', use_unlim:false, prompt:'...' } },
  { index: 2, params: { ... } }
])
```

- `aspect_ratio:'1:1'` para el carrusel (`.slimg` es cuadrado)
- `aspect_ratio:'4:3'` para el muro de opiniones (`.opi` es 4/3)
- Chequeá el saldo antes con `balance` si vas a generar muchas

### 3. Bajar, redimensionar y subir

```python
from PIL import Image
im = Image.open('bajada.png').convert('RGB').resize((900, 900), Image.LANCZOS)
im.save('resultado.webp', 'WEBP', quality=86)
```

900×900 con calidad 86 da ~60-100KB. Más grande no se nota y pesa el triple.

Después van a Recursos (ver `03-operativa-panel.md`) y usás la URL que devuelve el panel.

---

## Cómo escribir los prompts

La fórmula que funciona:

```
Amateur smartphone photo, [OBJETO con el acabado específico],
[DÓNDE, un lugar real y modesto],
[LUZ], [PROFUNDIDAD DE CAMPO],
no people, no text
```

### Lo que más cambia el resultado

**"Amateur smartphone photo"** al principio. Sin eso salen fotos de catálogo con fondo blanco, que en una landing de infoproducto se leen como stock y matan la credibilidad. Con eso salen fotos que parecen mandadas por un cliente.

**Un lugar concreto y humilde.** "on a wooden patio table", "on a workbench in a home garage", "on a kitchen counter next to spread newspaper". Un fondo neutro arruina el efecto.

**"no people, no text"** siempre. La IA mete carteles inventados y manos de más si no se lo prohibís.

**Describí el acabado, no el producto.** No "una maceta pintada" sino "swirling marbled paint in teal, white and gold".

### Detalles físicos: pediselos explícitos

Los modelos exageran el movimiento. Si el proceso del usuario es lento y controlado, la IA igual te va a poner agua salpicando por todos lados, y el usuario lo va a notar enseguida porque no es así como se hace.

Pedile lo contrario, y repetilo de varias formas:

> "The water surface is calm and undisturbed with **no splashing, no droplets, no spray, no bubbles**. The object sinks slowly at a slight angle, mirror-like reflections on the still surface."

**Preguntale al usuario cómo es el proceso de verdad** antes de generar fotos de técnica. Una foto que contradice el método enseña mal y le hace perder credibilidad justo donde más la necesita.

### Manos y pies: dónde se rompe la anatomía

Las escenas de automasaje son las que mejor convierten y las que peor le salen al modelo. El error clásico: un pie con el tobillo imposible, o un dedo de más. El alumno lo ve al toque — "parece que tiene quebrado el pie".

**Lo que rompe la imagen:**

- Vista **cenital en primera persona** ("desde el punto de vista de quien está sentado, mirando hacia abajo") con el pie cruzado sobre la rodilla. Ese escorzo de tobillo es donde el modelo falla siempre.
- Pedir el pie y la pierna completos en el cuadro: cuantas más articulaciones, más chances de que una salga mal.

**Lo que sale bien:**

- **Vista lateral, a la altura del asiento**, con la persona sentada en la posición normal de cruzar el tobillo sobre la rodilla.
- **Pie apoyado en un puf o banquito**, tobillo derecho, manos encima.
- **Recorte cerrado** donde el tobillo queda fuera de cuadro: si no está la articulación, no se puede romper.

Y pedilo explícito, aunque suene obvio:

> "anatomically correct human foot with five toes in natural proportion, ankle at a relaxed natural angle, realistic hands"

**Generá 3 o 4 variantes de la misma escena y elegí.** Sale más barato que una sola y explicarle al alumno por qué el pie está torcido.

### Cuidado con lo que pedís de más

Cada objeto que nombrás, el modelo lo pone — aunque no tenga dónde. Pedir "una taza dejando una marca en la madera" devolvió una mancha de café **flotando** al lado del cuaderno. Si querés una mesa prolija, pedila prolija: *"clean dry desk surface without any spills or rings"*.

### Manos

Manos con guantes, de costado, sin cara: bien. Es una foto de proceso, no de una persona.

---

## Ejemplos que salieron bien

**Objeto terminado:**
> Amateur smartphone photo, an old terracotta plant pot hand-painted with a simple geometric pattern in teal, white and gold, sitting on a wooden patio table in soft afternoon daylight, a small green succulent planted inside, slightly imperfect handmade finish, natural shadows, shallow depth of field, no people, no text

**Varias piezas (para el ángulo "esto se vende"):**
> Amateur smartphone photo, five hand-painted ceramic plant pots lined up on a white table, each with a different pattern — black and gold, pink and white, blue stripes, green dots, purple waves — home craft workspace, natural light, no people, no text

**Setup / "esto es todo lo que necesitás":**
> Amateur smartphone photo of a simple home setup on an apartment balcony: a plastic tray, three small paint jars and two brushes, a ceramic pot drying on spread newspaper and a pair of latex gloves, no machines or equipment, afternoon daylight, no people, no text

**Proceso, movimiento controlado:**
> Amateur smartphone photo, gloved hands slowly lowering a white thermos into a bucket of perfectly still water covered with a swirled film of green and white paint. The water surface is calm and undisturbed with no splashing, no droplets, no spray, no bubbles. The paint film wraps smoothly around the object as it sinks at a slight angle, mirror-like reflections on the still surface. Garage floor, soft natural light, face not visible, no text

---

## Retoque de logos oscuros

Los logos de medios de pago suelen venir con texto azul marino que sobre fondo negro desaparece. Aclarás solo lo oscuro y dejás el ícono de color:

```python
from PIL import Image
im = Image.open('logo.png').convert('RGBA'); d = im.load()
for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = d[x, y]
        if a > 10 and (0.299*r + 0.587*g + 0.114*b) < 150:
            d[x, y] = (255, 255, 255, a)
im.save('logo-blanco.webp', 'WEBP', quality=92)
```

El umbral 150 conserva celestes y dorados y solo blanquea lo realmente oscuro.

---

## Páginas del interior del ebook

Para el anillo 3D hacen falta 7 páginas del PDF. No se generan: se extraen del PDF real del usuario.

```bash
pdftoppm -f 44 -l 44 -r 150 -jpeg -jpegopt quality=95 ebook.pdf pagina
```

```python
from PIL import Image
Image.open('pagina-44.jpg').convert('RGB').resize((745, 1053), Image.LANCZOS) \
     .save('pg44.webp', 'WEBP', quality=84)
```

**Elegí páginas que se vean bien de lejos**: portadillas de capítulo, páginas con fotos grandes, tablas o esquemas. Una página de texto corrido a 132px de ancho es una mancha gris.

⚠️ **Y que se distingan ENTRE ELLAS.** Este es el error que más se repite: si el ebook tiene una ficha por técnica, siete fichas seguidas son la misma imagen. Todas tienen el mismo encabezado, la misma grilla y el mismo pie dibujado; lo único que cambia es un puntito de color que a 132px no se ve.

**Miralas al tamaño real antes de subirlas**, no en el visor del PDF:

```python
from PIL import Image
Image.open('pagina.png').resize((132, 187), Image.LANCZOS) \
     .resize((264, 374), Image.NEAREST).save('mini.png')
```

Si a ese tamaño no podés decir cuál es cuál, el comprador tampoco.

La mezcla que funciona: **una ficha, la portada, la lámina más visual (un mapa, un esquema a color), otra ficha de una zona bien distinta, y una portadilla de capítulo.** Con 5 alcanza. Y si bajás de 7 a 5, recalculá los ángulos del anillo y el texto del pie (ver `02`).
