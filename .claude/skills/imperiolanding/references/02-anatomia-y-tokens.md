# Anatomía de la landing, tokens y trampas

## El orden de la página

No es arbitrario: cada bloque contesta la objeción que aparece justo después del anterior.

| # | Bloque | Qué resuelve | ¿Opcional? |
|---|---|---|---|
| 1 | Cinta superior | Acceso inmediato, pago seguro, garantía | No |
| 2 | Imagen creativa | Es el cuerpo de la venta | **Imprescindible** |
| 3 | Badge de oferta | Ancla el ahorro | No |
| 4 | Línea de reseñas | Prueba social | Solo si es real |
| 5 | H1 | Promesa concreta | No |
| 6 | Caja de precio | Qué recibe y cuánto vale | No |
| 7 | CTA con latido | La acción | No |
| 8 | Bloque de urgencia | Por qué hoy y no mañana | Solo si es cierto |
| 9 | Anillo 3D del interior | "¿Qué hay adentro?" | Muy recomendado |
| 10 | Garantía | Saca el riesgo | No |
| 11 | Carrusel de testimonios | Prueba social con cara y resultado | Solo si es real |
| 12 | Combo / bonos con portadas | Valor percibido | No |
| 13 | Beneficios | Diferenciación | No |
| 14 | Reputación de vendedor | Confianza en quien vende | Solo si es real |
| 15 | Métodos de pago | Seguridad del cobro | No |
| 16 | FAQ | Últimas objeciones | No |
| 17 | Muro de opiniones | Volumen de prueba social | Solo si es real |
| 18 | Barra flotante | CTA siempre a mano | No |

**No repitas el CTA en una sección propia al final.** Con la barra flotante siempre visible, un botón grande de cierre queda como doble botón y ensucia.

**Entre sección y sección no va aire.** Las cards ya traen su padding interno; el margen entre ellas alcanza con 12px. Una landing con 40-60px entre bloques se siente vacía y obliga a scrollear de más.

---

## La paleta sale de la imagen del producto

**Esto es obligatorio, no opcional.** La landing de cada producto tiene que ser una continuación de su imagen creativa, no la de otro con otro color encima. Dos productos distintos con la misma estructura tienen que verse como dos marcas distintas.

Todo el CSS deriva del bloque `:root`. **No hay un solo color de acento escrito a mano fuera de ahí** — los glows, los bordes, las sombras y el gradiente del botón usan `rgba(var(--acc-rgb),...)`. Cambiando ese bloque cambia la landing entera.

### Paso 1 — Mirá la imagen

Abrí la imagen creativa con la herramienta de lectura de archivos y **miralas de verdad**. Preguntate:

- ¿Cuáles son los 2 o 3 colores que dominan?
- ¿Es oscura o clara? ¿Fría o cálida?
- ¿La tipografía de la imagen es condensada y agresiva, o fina y elegante?
- ¿Qué sensación tiene: tecnológica, artesanal, deportiva, femenina premium, casera?

### Paso 2 — Sacá los colores dominantes

Ojo con confiar solo en el ojo: los colores que más saltan no siempre son los que más área ocupan. Verificalo:

```python
from PIL import Image
from collections import Counter
im = Image.open('creativa.webp').convert('RGB')
im.thumbnail((200, 1200))
px = [p for p in im.getdata()]
# ignorar casi-negros y casi-blancos, que son fondo
px = [p for p in px if 40 < sum(p)/3 < 230]
# agrupar en bloques de 24 para juntar tonos parecidos
buckets = Counter(tuple(v//24*24 for v in p) for p in px)
for c, n in buckets.most_common(12):
    print('#%02X%02X%02X' % c, n)
```

Cruzá el resultado con lo que ves. Si la imagen tiene un violeta que ocupa poco pero está en todos los títulos, ese es el acento aunque no encabece la lista.

### Paso 3 — Armá el bloque :root

| Token | De dónde sale |
|---|---|
| `--acc` + `--acc-rgb` | El color más brillante y saturado. Va en precios, estrellas y checks. |
| `--acc2` + `--acc2-rgb` | El segundo. Va en kickers y bordes. |
| `--mag` + `--mag-rgb` | Un tercero de contraste, con moderación. |
| `--on-acc` | El texto de los botones. Casi negro si el acento es claro; casi blanco si es oscuro. |
| `--dark`, `--dark2`, `--chip`, `--chip2` | Neutros muy oscuros **con un dejo del tono dominante** — no negro puro. Un producto cálido lleva fondos con marrón, no con azul. |
| `--panel` | Dos glows de `--acc2` y `--mag` a baja opacidad sobre un gradiente diagonal de los fondos. |
| `--ink`, `--dim`, `--dim2` | Blanco tirando al tono de la imagen (cálida → `#FFF8EC`; fría → `#EFF6FF`). |
| `--bd` | `rgba(var(--acc2-rgb),.35)` |
| `--grad` | 3 paradas: oscuro → claro → medio del acento. |
| `--grad-flow` | 5 paradas del mismo gradiente. **La primera y la última tienen que ser iguales** o el barrido del botón pega un salto. |

La plantilla trae dos paletas completas de ejemplo al final del `<style>` (oro y violeta, naranja y ámbar). Sirven de molde, pero **no las uses tal cual si la imagen pide otra cosa**.

### Paso 4 — Tipografía

`--disp` es la que le da carácter. Elegila según lo que viste:

| Sensación | Display |
|---|---|
| Tecnológico, deportivo, urbano | `Anton` |
| Artesanal, premium, femenino | `Playfair Display` o `Georgia, "Times New Roman", serif` |
| Cercano, casero, infantil | `Fredoka` o `Nunito` |

Si cambiás la fuente, actualizá el `@import` de Google Fonts de la primera línea.

### Paso 5 — Mostrale la paleta antes de construir

Antes de escribir el HTML, decile en dos líneas qué sacaste:

> De tu imagen saqué el verde neón (#39FF6A) como color principal y el celeste (#22D3FF) como secundario, sobre fondo negro azulado. Tipografía condensada tipo Anton, que es la que va con el estilo de la creativa. ¿Vas con eso o querés otro acento?

Es un ida y vuelta de diez segundos que evita rehacer la landing entera.

### Lo que NO cambia entre productos

La estructura, el orden de las secciones, las medidas, los breakpoints, las animaciones y los arreglos de layout. Todo eso está probado. **Cambiás colores y tipografía, no arquitectura.**

## Trampas conocidas

Cada una de estas costó encontrarla. Leelas antes de debuggear.

### 1. Scroll horizontal por la imagen del hero

**Síntoma:** toda la página se puede arrastrar a los costados; el contenido se ve corrido.

**Causa:** el `.heroimg` es hijo de un grid. Como los ítems de grid tienen `min-width:auto`, la caja toma el ancho **intrínseco** de la imagen (ej. 1000px) en vez del de la columna, y arrastra a toda la página.

**Solución:**
```css
.hero>*,.col,.heroimg{min-width:0}
.heroimg{width:100%;max-width:100%}
.heroimg img{width:100%;max-width:100%;height:auto;display:block}
img{max-width:100%}
```

**No lo tapes con `overflow-x:hidden` en `body`**: eso rompe el `position:sticky` de la imagen en desktop.

**Cómo encontrar al culpable:**
```js
const W = document.documentElement.clientWidth;
[...document.querySelectorAll('*')]
  .filter(e => { const r = e.getBoundingClientRect(); return r.width>0 && r.right>W+1; })
  .slice(0,10)
  .map(e => (typeof e.className==='string'?e.className:e.tagName) + ' R' + Math.round(e.getBoundingClientRect().right));
```
Ignorá lo que esté dentro de un carrusel con `overflow:hidden`: ahí es normal.

### 2. Las hojas del anillo 3D se montan

Con `N` hojas de ancho `W` en un anillo de radio `R`, la separación entre hojas vecinas es `2·R·sen(180/N)`. Para que no se pisen:

```
R ≥ W / (2 · sen(180/N))
```

Con 7 hojas de 132px: `R ≥ 132 / 0.868 = 152`. Usá **170** para que quede aire.

El ángulo de cada hoja es `i · (360/N)`. Con 7: 0 / 51.43 / 102.86 / 154.29 / 205.71 / 257.14 / 308.57.

Si el anillo queda más ancho que el contenedor, **no achiques el radio**: poné una máscara que difumine los bordes.
```css
mask-image:linear-gradient(90deg,transparent 0,#000 14%,#000 86%,transparent 100%)
```

`backface-visibility:hidden` en las hojas hace que solo se vean las 3-4 de adelante. Queda mucho más prolijo que ver las de atrás espejadas.

### 3. Una regla vieja le gana a la nueva

Si cambiás un tamaño y no pasa nada, es especificidad. Ejemplo real: `.tc span{font-size:30px}` le gana a `.tcv{font-size:17px}` porque tiene un elemento más.

**Verificalo siempre en el navegador antes de dar por hecho que se aplicó:**
```js
getComputedStyle(document.querySelector('.tcv')).fontSize
```

**Y no acumules capas de parches.** Si estás agregando la tercera regla `.btn{...}` al final de la hoja, pará y reescribí la original. Una hoja con cinco `.btn` encimados es imposible de mantener y el usuario después no puede tocar nada.

### 4. Los precios se salen de sus cajas

Con `flex:0 1 auto` + `min-width:0`, la caja se achica por debajo del texto y el número se desborda.

Para que las cajas se ajusten al contenido: `flex:0 0 auto`. Y ajustá el tamaño de fuente hasta que entre.

**Medí el texto de verdad, no lo estimes:**
```js
const e = document.querySelector('.tcv');
const r = document.createRange(); r.selectNodeContents(e);
({ texto: Math.round(r.getBoundingClientRect().width),
   caja:  Math.round(e.parentElement.getBoundingClientRect().width) })
```

### 5. La imagen creativa pesa demasiado

Una creativa de 1000×6000 puede pesar 900KB-1.5MB. Es el LCP de la página y en 4G son varios segundos de pantalla en blanco.

**Partila en 3 a lo alto** y stackealas. Se ven como una sola (las costuras no se notan), pero solo la primera carga al entrar:

```html
<img src="hero-1.webp" width="1000" height="2098" loading="eager" fetchpriority="high" decoding="async">
<img src="hero-2.webp" width="1000" height="2098" loading="lazy" decoding="async">
<img src="hero-3.webp" width="1000" height="2096" loading="lazy" decoding="async">
```

El contenedor necesita `font-size:0;line-height:0` para que no aparezca una rayita blanca entre partes.

Corte y conversión:
```python
from PIL import Image
im = Image.open('creativa.png').convert('RGB')
w, h = im.size
n = 3; step = (h + n - 1) // n
for i in range(n):
    im.crop((0, i*step, w, min(h, (i+1)*step))).save(f'hero-{i+1}.webp', 'WEBP', quality=80, method=6)
```

Resultado típico: de 958KB en una sola imagen a 326KB en la primera pantalla.

### 6. Barras de scroll dentro de secciones insertadas

Solo aplica si usás el **modo por secciones** (no Custom HTML). Cada sección insertada se renderiza en un `<iframe srcdoc>` con sandbox, y el `margin:8px` del body desborda el alto automático.

```css
html,body{margin:0!important;padding:0!important;overflow:hidden!important;scrollbar-width:none}
*::-webkit-scrollbar{display:none!important}
```

En Custom HTML esto no pasa.

### 7. Contenido tapado por la barra flotante

La barra es `position:fixed`. Sin espacio abajo, lo último de la página queda debajo para siempre.

```css
body{padding-bottom:190px}   /* > alto real de la barra */
```

Medí el alto real: `document.querySelector('.flo').getBoundingClientRect().height`.

### 8. Animaciones que no paran nunca

Un anillo 3D girando y un botón latiendo consumen batería aunque estén fuera de pantalla. Pausalos con `IntersectionObserver` (está en la plantilla) y respetá `prefers-reduced-motion`.

**Cuidado con las animaciones que escalan.** Un `scale(1.03)` sobre un botón de ancho completo agranda la caja y puede reintroducir scroll horizontal. Después de agregar cualquier animación con `transform`, medí el `scrollWidth` durante un ciclo completo:

```js
let mx = 0;
for (let i = 0; i < 24; i++) {
  mx = Math.max(mx, document.documentElement.scrollWidth);
  await new Promise(r => setTimeout(r, 110));
}
mx; // tiene que seguir siendo === clientWidth
```

### 9. Imágenes "rotas" que en realidad son lazy

`naturalWidth === 0` en una imagen fuera de pantalla no es un error: todavía no cargó. Antes de contar rotas, forzá la carga:

```js
document.querySelectorAll('img').forEach(i => { i.loading = 'eager'; i.src = i.src; });
await new Promise(r => setTimeout(r, 4000));
```

### 10. La píldora de oferta desborda en mobile

`.offer .b` tiene dos `<span>` con `white-space:nowrap` y `width:fit-content`. Si el texto de la etiqueta es largo **y** el `{{savings}}` real también, la suma se pasa del ancho de pantalla y arrastra toda la página.

Con "✦ OFERTA POR TIEMPO LIMITADO" + "AHORRÁS AR$ 28.010" mide **396px**: rompe a 390.

**No toques el CSS: acortá el texto.** "✦ OFERTA LIMITADA" baja la píldora a 311px y entra con aire.

Medilo en la tienda publicada, con el precio de verdad:

```js
Math.round(document.querySelector('.offer .b').getBoundingClientRect().width)
// tiene que ser menor que clientWidth - 24
```

Lo mismo aplica a la línea de reseñas `.rev`: si el texto no entra al lado de las estrellas, el flex la manda a un segundo renglón y queda feo. Espacio disponible ≈ ancho del contenedor − 84px de estrellas − 8px de gap.

### 11. Cambiaste la cantidad de hojas del anillo y se montan

Los ángulos son `i · (360/N)`. Si sacás hojas y dejás los ángulos viejos, quedan dos en la misma posición.

| N | Ángulos |
|---|---|
| 5 | 0 / 72 / 144 / 216 / 288 |
| 6 | 0 / 60 / 120 / 180 / 240 / 300 |
| 7 | 0 / 51.43 / 102.86 / 154.29 / 205.71 / 257.14 / 308.57 |

El radio mínimo sigue siendo `R ≥ W / (2·sen(180/N))`. Con `translateZ(170px)` y tarjetas de 132px entran cómodas de 5 a 7 hojas. **Con menos hojas no achiques el radio**: las tarjetas se ven más grandes y legibles, que es justo lo que se busca.

Y acordate de actualizar el `.pvp` del pie — si hay 5 hojas no puede decir "7 de las N páginas".

### 12. Logos oscuros sobre fondo oscuro

El logo de MercadoPago trae el texto en azul marino: sobre negro desaparece. Recoloreá a blanco lo que sea muy oscuro, conservando el ícono de color:

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
