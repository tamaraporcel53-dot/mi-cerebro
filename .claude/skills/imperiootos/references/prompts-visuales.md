# Prompts de imagen: avatar y planos de producto

---

# El avatar

## Anatomía del prompt

Siete bloques. Los últimos dos son los que separan una foto creíble de una imagen que grita "IA".

1. **Formato y calidad** — "Fotografía vertical 9:16, ultrarrealista, calidad de cámara réflex profesional"
2. **Quién es** — edad, origen, encuadre, qué está haciendo. Que esté grabando un video explicando su oficio, no posando.
3. **Vestimenta y físico** — ropa concreta y coherente con el oficio, y señales de uso real: manos con restos de pintura, delantal gastado. La textura de piel importa: "poros visibles, pequeñas imperfecciones, nada de retoque de belleza".
4. **El fondo, que es donde vive la autoridad** — el resultado de su trabajo a la vista: piezas terminadas en estantes, herramientas, materiales. Nunca diplomas ni títulos.
5. **Iluminación** — "luz cálida entrando por una ventana lateral, suave, con sombras naturales"
6. **Cámara** — "lente 85mm, profundidad de campo cinematográfica, fondo levemente desenfocado pero legible"
7. **Directivas anti-IA** — "apariencia humana realista y natural, sin apariencia de IA, sin piel plastificada, sin ojos vidriosos, sin manos deformes, sin objetos distorsionados, sin texto ilegible, sin exagerar su belleza"

## La autoridad viene del resultado, no de las credenciales

Circulan plantillas de avatar que piden diplomas legibles de universidades reales, fotos de casamiento y de hijos inventados, para construir un experto que no existe. **Eso es fabricar credenciales.** Casi nunca hace falta —nadie compra un manual de estampado por un título de Harvard— y ensucia la marca del usuario si alguien lo mira de cerca.

La autoridad real, y la que además convierte mejor, viene del **resultado visible**: si detrás del personaje hay veinte piezas terminadas que se ven bien, ya está todo dicho.

## Regenerar al mismo personaje en otro escenario

Sirve para la continuidad entre OTOs del mismo producto: el mismo artesano, en otro rincón de su taller, con los objetos del OTO nuevo sobre la mesa.

**El modelo importa.** `soul_2` no preserva identidad ni con imagen de referencia: devuelve otra persona. `nano_banana_pro` y `gpt_image_2` sí la preservan — misma cara, misma barba, misma ropa — pasando la imagen del avatar en `medias` con rol `image`.

Estructura del prompt, en este orden:

1. **Qué conservar, primero y explícito** — "exactamente la misma cara, la misma barba corta, el mismo pelo, la misma remera y el mismo delantal; tiene que ser reconociblemente el mismo hombre"
2. **La escena nueva** — dónde está ahora y qué está haciendo
3. **Los objetos nuevos** — descritos con detalle, porque son el motivo del cambio
4. **El fondo actualizado** — que cuente el tema del OTO nuevo
5. **Luz, cámara y las directivas anti-IA** de siempre

Generá con los dos modelos y compará. En un caso real, `nano_banana_pro` dio mejor boca para el lip-sync pero una mano sosteniendo un objeto indefinido; `gpt_image_2` dio manos limpias y una expresión más cálida y parecida al original. **Mostrale las dos al usuario junto a la referencia**, en una sola imagen comparativa, y que elija.

## Personajes con marca

Si el usuario manda referencias con personajes registrados —Mario, Minnie, cualquier superhéroe— decíselo antes de generar. No es un detalle: el video va a una página de venta y probablemente a anuncios de Meta, y las dueñas de esos personajes reclaman.

Casi siempre lo que impacta de la referencia no es el personaje sino **la forma**: el cromado luce sobre superficies redondas, un patrón se luce sobre una silueta reconocible. Eso se consigue con figuras genéricas y el efecto es el mismo. Proponé el reemplazo concreto en vez de solo señalar el problema.

La excepción legítima: si el usuario **fabricó y fotografió** esa pieza, es su trabajo y es su decisión.

## Elegir la variante

Generá `count: 2` y elegí mirando, no adivinando. Criterios, en orden:

1. **De frente, cara centrada.** Los perfiles complican el lip-sync.
2. **Boca cerrada o casi.** Una foto a mitad de palabra produce artefactos.
3. **Congruencia del fondo con el producto.** Si detrás hay objetos que el producto enseña a hacer, mejor.

---

# Los planos de producto

## Si los genera el usuario

Suele ser lo mejor: itera hasta que le gustan y muchas veces tiene material real. Dejale un archivo en su carpeta con esta estructura:

### 1 · Encabezado

Cómo usarlo (pegar el contexto una vez y después cada prompt), el formato pedido y **dónde dejar los archivos y con qué nombre**.

Pedí **vertical 2:3**. Si el generador devuelve cuadrado, se pierde la mitad al encuadrar a 9:16.

### 2 · Bloque de CONTEXTO

Un párrafo que explique el producto y las técnicas que involucra, para pegar una vez al abrir el chat. Sin esto, cada prompt sale de un modelo que no entiende de qué se trata.

Incluí las reglas transversales: fotografía réflex real, nunca render 3D ni ilustración, sin texto ni logos, y cualquier regla propia del producto.

### 3 · Un prompt por plano

Cada uno con: **número, segundo en que entra, la frase del guion que acompaña**, y —si el producto tiene varias técnicas— **cuál corresponde a ese plano**.

El prompt describe: el objeto concreto, el acabado, dónde está apoyado, qué se ve alrededor, la luz y la cámara.

Cuando un plano tiene un **trabajo argumental**, decilo en el prompt. Ejemplos reales:

- *"El punto de la foto es que las dos piezas sean DISTINTAS entre sí"* — para ilustrar que la técnica no se repite
- *"Las tres tienen que verse IDÉNTICAS, producidas en serie"* — para ilustrar que sí se repite

Ese par de planos demuestra el argumento del video sin audio. Si salen bien, se entiende mirando.

### 4 · Sección de correcciones

Los fallos más comunes y qué pedirle al generador:

| Sale así | Pedile |
|---|---|
| Como render 3D | "que parezca una foto tomada con cámara, con grano y textura real, no un render" |
| El estampado pegado encima | "el patrón tiene que deformarse siguiendo la curva del objeto, como pintura aplicada, no como una calcomanía plana" |
| Caras o formas raras entre patrones | "solo patrones abstractos, sin ninguna figura reconocible" |
| Manos deformes | "manos con cinco dedos, en postura natural y relajada" |
| Cuadrada | "formato vertical, relación de aspecto 2:3, más alta que ancha" |

## Si los generás vos

`generate_image_batch` con `soul_2`, `aspect_ratio: "9:16"`, mismo contenido de prompt.

**Mirá todos los resultados antes de montar.** Una parte falla de formas que solo se ven mirando: un pedido de "termo de acero con estampado efecto mármol" volvió como jarra de plata antigua ornamentada. Armá una hoja de contactos numerada, mirala, y regenerá lo que no sirve.

## Filmaciones propias del usuario

Casi siempre son mejores que cualquier imagen generada, porque el movimiento no lo reemplaza una foto congelada: ver la pieza entrando al agua es el gancho visual más fuerte que puede tener un producto manual.

Antes de proponer generar nada, **revisá las carpetas del proyecto y preguntá si tiene filmaciones o fotos**. En un caso real había una carpeta con ocho clips del proceso, ya en 1080x1920 y de 3 a 6 segundos —exactamente el formato y la duración de los cortes— que nadie había mencionado.

Dos cuidados al usarlas:

**Mirá los primeros segundos de cada clip.** Uno que arranca con el balde vacío desperdicia el corte; entrá con un offset.

**Verificá que la técnica del clip coincida con lo que dice la voz.** Si el producto enseña dos técnicas, una filmación de la primera puesta sobre una frase que describe la segunda contradice el video. Cuando el gesto físico es idéntico en ambas y la diferencia es invisible, se puede usar igual — pero es una decisión del usuario, no tuya: planteásela y que elija.
