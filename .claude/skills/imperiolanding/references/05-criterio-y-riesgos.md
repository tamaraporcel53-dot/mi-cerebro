# Criterio: qué revisar antes de publicar

Esto no es un reglamento. Son las cosas que en la práctica le cuestan plata al usuario, y una sola línea que no cruzo.

---

## Reseñas, testimonios y números

**Si el usuario te los da, usalos.** No lo interrogues sobre de dónde salieron ni le pidas que los justifique. Y para el puntaje y la cantidad de reseñas de la línea de estrellas, seguí lo que dice `SKILL.md` y listo: no abras el tema. Es su negocio y sus datos; él sabe lo que tiene. Pedile la fuente **una sola vez** y solo para poder encabezar bien el bloque ("Opiniones de MercadoLibre", "Comentarios de Instagram") — eso hace que conviertan más, porque una reseña con origen es más creíble que una suelta.

Si te dice "son míos" o "ya los tengo", listo, seguí.

**Lo único que no hago: inventarlos yo.** Si el usuario me pide que escriba testimonios de compradores que no existen, o que genere caras de gente inventada para ponerlas como clientes, ahí paso. Le digo en dos frases que eso lo tiene que traer él y le ofrezco lo que sí puedo armar mientras tanto. No es un sermón: es una frase y sigo trabajando.

Lo que sí armo sin problema:

- **Fotos de resultados y objetos** — todas las que haga falta, generadas con Higgsfield. Ver `06-imagenes-higgsfield.md`. Son objetos, no personas.
- **Galería de resultados** en lugar del bloque de testimonios, si todavía no hay reseñas.
- **Bloque de objeciones** — "¿sirve si nunca hice esto?", "¿y si la primera me sale mal?". Convierte parecido a un testimonio y lo dice el vendedor en primera persona.
- **Adelanto del producto** — el anillo 3D con páginas reales del PDF. Es la prueba más fuerte que hay: le mostrás lo que compra.

### Avatares

Si no hay foto de esa persona, usá la inicial del nombre en el círculo con el gradiente de la marca. Es lo que usan las apps de reseñas de verdad y queda mejor que una foto de stock.

---

## Contadores y "solo por hoy"

Esto es un consejo, no una regla: **la decisión es del usuario.** Pero decíselo una vez, porque casi nadie sabe el número real.

Un contador que se reinicia en cada recarga rara vez lo detecta Meta — la revisión de anuncios no cruza si tu descuento vence de verdad. **El costo viene por otro lado:** el visitante que vuelve y ve el reloj arrancando de cero otra vez marca "ocultar anuncio / engañoso". Ese feedback negativo te baja el ranking de calidad y te sube el CPM en todas las campañas. No es una sanción, es que cada venta sale más cara.

No inventes sanciones que no existen para convencerlo. Decile lo que realmente pasa y que elija.

### Alternativas con urgencia real (suelen convertir más)

**a) Precio de hoy contra precio normal** — el precio normal tachado a la vista. 🔴 **Nunca** "el precio está en dólares / si el dólar sube, mañana te cuesta más / congelás el precio": prohibido (2026-10-29), y con precios por país deja de ser cierto. Está en la plantilla.

**b) Fecha real de fin** — si el usuario va a subir el precio de verdad, el contador es honesto y muy potente, sobre todo porque el precio "después" ya está tachado a la vista. Preguntale si va a cumplirla y dejá la fecha en un solo lugar del código.

**c) Entrega inmediata** — "Te llega al mail en 1 minuto". Urgencia por el lado de la recompensa.

**d) Garantía larga** — sacar el riesgo mueve más que apurar.

### Si sacás el contador, barré los restos

```js
['solo por hoy','tiempo limitado','HOY GRATIS','últimos cupos','se cierra hoy']
  .map(p => p + ': ' + (document.body.innerText.split(p).length - 1));
```

Quedan tirados en la cinta de arriba, en la caja de precio y en el pie del combo.

---

## La matemática tiene que cerrar

Esto sí rompe ventas, y es puro cálculo.

Impultienda calcula el ahorro así:

```
ahorro = precio_anterior + valor_de_los_bonos − precio_final
```

Si los bonos tienen valor cargado, el "Ahorrás" no coincide con la resta simple que el comprador hace de cabeza (anterior − final). Lo nota y desconfía de todo lo demás.

**Bonos que se regalan → valor 0 en el panel.** Ver `00-checklist-alumno.md`.

---

## Que exista lo que la landing promete

Chequeo rápido antes de publicar:

- ¿Promete 3 bonos? → que haya 3 bonos con PDF cargado
- ¿Promete "acceso inmediato"? → que el PDF principal esté cargado
- ¿Promete "60 páginas"? → contá las páginas del PDF
- ¿Promete garantía de X días? → que el usuario sepa que va a tener que cumplirla

Una landing que promete lo que el producto no entrega genera reembolsos y reclamos. Es el peor negocio posible, y es el único de esta lista que se arregla en dos minutos.
