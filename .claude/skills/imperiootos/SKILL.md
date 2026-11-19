---
name: imperiootos
description: Se llama con "imperiootos". Produce de punta a punta el VSL (video de ventas) de un OTO / upsell post-compra, con avatar de HeyGen, cortes a planos de producto y subtítulos quemados, y lo entrega como MP4 en una carpeta. Usar SIEMPRE que el usuario mencione OTO, upsell, downsell, "video post pago", "post purchase", "embudo post compra", "oferta única", "VSL", "video de ventas con avatar", o cuando quiera venderle algo más a alguien que acaba de comprarle. También usar cuando pida un video con avatar para vender un producto digital, cuando diga "armame el OTO 1", "necesito el video del upsell", "generá el VSL de X", o cuando quiera rehacer o corregir un VSL de OTO ya producido.
---

# VSL de OTO post-compra

> **🔴 Marca de agua y cierre con la landing .**
> - **Todo video de anuncio** lleva la tienda de ese producto (ej. `mitienda.store`) como marca de agua muy suave, que aparece en un lugar, se desvanece y reaparece en otro. Motor Remotion: prop `"watermark": "<tienda>"` en los props de `Reel` o `Historia` (componente `src/Watermark.tsx`, opacidad 0,18, cambia cada 3,4 s y nunca cae sobre los subtítulos). Motivo: *"para que no me descarguen los videos"*.
> - **Cierre con la landing, a prueba:** en algunos anuncios de cada tanda (no en todos) el final se relaciona con la landing del producto. Puede ser la landing real o algo que se le parezca (imagen principal, titular, colores), para que el clic se sienta como continuación. Esos archivos se marcan con `-LANDING` en el nombre, para compararlos.


## 🔴 Video generado en Kie: 720p, nunca Full HD 

> Con 720p alcanza: generar en Full HD quema créditos sin que se note en el celular.

- **Todo video que se genera en Kie** (avatar con lipsync, b-roll, escena) va en **720p** o en la resolución
  más barata del modelo. **Nunca 1080p ni Pro.** Si la pieza sale en 1080x1920, se escala en la edición.
- Avatar con lipsync: siempre `kling/ai-avatar-standard` (720p, 8 créditos/s), nunca la versión Pro (16 créditos/s).
- **Antes de lanzar:** sacar el precio de la página oficial del modelo en kie.ai (no de una prueba), sumar el lote
  entero y decírselo al usuario con ese número. 200 créditos = 1 USD.

## 🔴 Voz, sonrisa e idioma 

| Regla | Detalle |
|---|---|
| **Sin "golpecito" al empezar cada frase** | Se escucha un "golpecito" al arrancar cada frase. Causa probable: clips de ElevenLabs unidos sin fundido **(sin confirmar)**. La voz va en **una sola toma**; si se une por frases, **fundido de 15 a 30 ms** en cada unión y **escaneo de picos** en las uniones antes de mandar a HeyGen |
| **Avatar sonriente y amigable** | La foto base con sonrisa natural (boca cerrada o casi, para el lip-sync) y un motionPrompt que pida expresión cálida |
| **LATAM = español neutro de tú** | Guion, voz y subtítulos en tú neutro ("toca", "mira", "para ti"), sin voseo ni modismos rioplatenses. El voseo solo si la tienda es solo para Argentina. Guía: `WIKI/espanol-neutro.md` del cerebro |
| **La página va en el mismo registro** | La página del OTO dice lo mismo que el video: si el VSL es de tú, la página también ("Toca el botón de abajo", "mira lo que tenemos para ti") |

## ⛔ Regla de entrega

**Los once pasos se recorren en orden y ninguno se saltea.** Cada paso existe porque saltearlo rompió algo en producción real: videos desincronizados, imágenes cayendo sobre la frase equivocada, ofertas que prometían lo que el producto principal ya regalaba, créditos gastados en renders que hubo que tirar.

Antes de entregar el resultado final, verificá que los once estén hechos y decílo explícitamente. Si alguno se salteó, no está terminado.

Tres pasos son **puertas**: no se avanza sin respuesta del usuario.

| # | Paso | Puerta |
|---|---|---|
| 1 | Intake y lectura del producto principal | |
| 2 | Definir la oferta | |
| 3 | Escribir el guion | 🚪 **aprobación** |
| 4 | Calcular la duración real y ajustar | |
| 5 | Lista de planos, pieza por pieza | 🚪 **aprobación** |
| 6 | Conseguir las piezas visuales | |
| 7 | Avatar | |
| 8 | Render en HeyGen | 🚪 **gasta créditos** |
| 9 | Estabilizar el render | |
| 10 | Montaje con verificación de sincronía | |
| 11 | Subtítulos y entrega | |

---

## Lo que hace que este video funcione

**El comprador acaba de darte plata.** Si el video le sugiere que lo que compró está incompleto, no genera deseo: genera arrepentimiento, y eso vuelve como reembolso. La tensión se construye sobre un límite **real y verificable** de lo que ya tiene.

**El video no es el producto.** Lo que decide la conversión es que la oferta sea algo que el comprador quiera. Si la oferta es floja, ningún montaje la salva — conviene decírselo al usuario antes de producir tres minutos de video sobre una oferta débil.

**Nada de invención.** Hay plantillas de VSL que piden "una explicación pseudo-científica que genere credibilidad" o escasez tipo "fue denunciado en las redes". No se hace. Casi siempre la explicación real es igual de impresionante y la restricción real igual de urgente, y no expone a reembolsos ni a rechazos de plataforma. Si el usuario trae una plantilla con esos elementos, seguí su estructura, reemplazá esas piezas por las verdaderas y decíle qué cambiaste y por qué.

---

# PASO 1 · Intake y lectura del producto principal

Pedí todo junto en un solo mensaje:

- **Producto principal**: nombre, precio, y el archivo (PDF, docx) si existe
- **La idea del OTO** y su precio
- **El ancla de precio** (el "vale X" contra el que se compara)
- **Qué número de OTO es** (1, 2 o 3) — cambia la apertura del guion
- **Dónde entregar** el video

**Leé el producto principal completo. No es opcional.** Es el paso que más errores evita, y descubre dos cosas:

1. **Qué NO se puede prometer** porque ya está adentro. Prometer algo que el comprador ya tiene destruye la oferta. En un caso real, la idea de OTO 3 ("los errores más comunes y cómo rescatar una pieza") tuvo que descartarse entera porque el ebook principal ya traía ese capítulo.
2. **Cuál es el límite real** del producto que justifica el OTO. Ese límite es el corazón del guion.

Si el producto es un PDF de imágenes sin capa de texto —muy común en infoproductos visuales— convertí las páginas y mirálas:

```bash
pdftoppm -jpeg -r 40 producto.pdf pg
montage pg-0[1-9].jpg pg-1[0-9].jpg pg-20.jpg -tile 5x4 -geometry +4+4 -label '%f' m1.jpg
montage pg-2[1-9].jpg pg-3[0-9].jpg pg-40.jpg -tile 5x4 -geometry +4+4 -label '%f' m2.jpg
montage pg-4[1-9].jpg pg-5[0-9].jpg pg-60.jpg -tile 5x4 -geometry +4+4 -label '%f' m3.jpg
```

Tres montages de 20 páginas dan el libro entero en tres miradas. Anotá el índice, los bonos y los capítulos que el OTO podría pisar.

---

# PASO 2 · Definir la oferta

Antes de escribir una línea, dejá por escrito:

- **Nombre propio** del OTO. Un nombre convierte "algo más" en un producto.
- **El límite real** que resuelve, y **en qué capítulo del producto principal** se puede verificar.
- **Los tres entregables**, cada uno con para qué le sirve.
- **El bono que no se anuncia.**

**Regla del OTO 2 y 3: tienen que servirle a quien dijo que NO al anterior.** Si el OTO 2 solo tiene sentido para quien compró el OTO 1, la mitad de la audiencia mira algo que no le sirve. El guion del OTO 2 se sostiene solo con el producto principal, y menciona el OTO 1 una vez y al pasar.

Si la oferta pisa algo que ya está incluido, decílo ahora y proponé una alternativa. Es mucho más barato acá que después del render.

## Cómo elegir el ángulo, y sobre todo el del OTO 3

**Cada sí es más caro que el anterior.** Para cuando aparece el OTO 3, el comprador ya gastó tres veces y todavía no usó nada de lo que compró. Eso cambia qué tipo de oferta funciona en cada posición:

| | Qué acepta bien |
|---|---|
| OTO 1 | Otra técnica. Viene caliente, quiere más de lo que acaba de comprar |
| OTO 2 | Otra familia de acabados, si se sostiene sola sin el OTO 1 |
| OTO 3 | **Algo que no le agregue trabajo.** Ya tiene tres PDFs sin abrir |

**El error del OTO 3 es ofrecer más tarea.** "Otro método", "otra guía", "otro curso" en tercer lugar se lee como más deberes para alguien que todavía no empezó los primeros. Lo que convierte ahí es lo que se usa el mismo día sin estudiar nada: plantillas, calculadoras, guiones, archivos listos. Y sobre todo, **lo que le devuelve plata en vez de pedírsela** — es el único argumento que se entiende sin explicarlo cuando ya lleva tres compras encima.

## ⛔ Preguntá antes de proponer nada que ate al usuario

Hay ofertas que convierten muy bien y que **le crean una obligación permanente al usuario**, no al comprador: acceso de por vida a lo que lance, actualizaciones, comunidad, soporte, mentorías, grupo de WhatsApp. Antes de proponer cualquiera de esas, **preguntá si está dispuesto a sostenerla**. Muchos no quieren, y proponerla sin preguntar hace perder una vuelta entera.

Lo mismo con **derechos de reventa**: es de lo más difícil de rechazar que existe, y le destruye el front-end que está pagando con anuncios. Si aparece, nombralo con la contra incluida.

**No prometas que una oferta es imposible de rechazar.** No existe. Decí cuál convierte mejor en esa posición y por qué, y dejá que decida.

---

# PASO 3 · 🚪 Escribir el guion

Leé `references/estructura-guion.md`. Trae los nueve bloques y las reglas de voz.

Presentá el guion completo para que el usuario lo edite. **Esperá su respuesta antes de seguir.**

Los cambios que haga son la voz de su marca: respetalos, incluso los que no te cierren. Comentá solo lo que tenga consecuencia real — una promesa que el video no cumple, una repetición, una contradicción con el producto principal.

Cuando devuelva su versión editada, aplicala tal cual. Arreglá por tu cuenta solo defectos mecánicos (una frase repetida dos veces seguidas por copiar y pegar) y avisá qué tocaste.

---

# PASO 4 · Calcular la duración real y ajustar

Este paso existe porque las estimaciones "a ojo" fallan y el usuario pide duraciones concretas.

**Calibración medida en producción:** a velocidad 1.4 en HeyGen, **787 palabras dieron 3:38 (218 segundos)**. Eso son **3,6 palabras por segundo**. HeyGen agrega pausas entre frases, así que el resultado sale algo más largo que el cálculo puro de lectura.

```bash
W=$(wc -w < guion.txt)
python3 -c "s=$W/3.6; print(f'{int(s//60)}:{int(s%60):02d} a velocidad 1.4')"
```

Si no coincide con lo que el usuario pidió, decíle el número real y ofrecé las opciones: dejarlo así, agregar contenido, o bajar la velocidad. **No decidas solo** — un VSL de OTO más corto suele convertir mejor, pero es su decisión.

Zona sana: 2 a 4 minutos. Del OTO 2 en adelante, más corto que el anterior — esa persona ya se bancó el primer video y dijo que no.

---

# PASO 5 · 🚪 Lista de planos, pieza por pieza

**Este es el paso que más sube la calidad, porque el usuario sabe qué quiere mostrar y muchas veces tiene material real.**

Un VSL con la cara hablando tres minutos aburre: el avatar repite gestos y se nota que es IA. La solución no es más movimiento del avatar, es **cortar**. Cada 15 a 25 segundos hay que salir del plano.

## Cómo armar la lista

Un corte por cada momento donde el guion **nombra algo que se puede ver**: el producto terminado, el proceso en acción, un contraste, los entregables, el objeto de la promesa.

Apuntá a un corte cada 13-15 segundos y a que el b-roll ocupe entre el 20% y el 25% del total.

## Cómo presentarla

Tabla, con el segundo aproximado, la frase del guion y una decisión por fila:

| # | Segundo | Qué dice el guion ahí | Qué se muestra | ¿De dónde sale? |
|---|---|---|---|---|
| 1 | 0:13 | "mármol, humo, geoda" | Pieza terminada efecto mármol | Higgsfield / la cargo yo / omitir |

Decíle explícitamente que **su material real convierte mejor que cualquier imagen generada**: una foto de una pieza que hizo de verdad tiene una autoridad que la IA no reproduce, y si el comprador la mira dos segundos, la diferencia se nota. Que pueda meter material propio es lo que separa esto de un video de IA genérico.

**Esperá su respuesta antes de gastar un solo crédito.**

## Biblioteca reutilizable

Guardá todo lo que aporte en `biblioteca/` dentro del proyecto, con un `biblioteca/indice.md` de una línea por pieza (archivo, qué muestra, de dónde salió). En el OTO siguiente, ofrecé primero lo que ya hay antes de pedirle nada nuevo. Nadie quiere que le pidan la misma foto dos veces.

**Buscá material que el usuario ya tenga antes de proponer generar.** En un caso real había una carpeta `B-Rolls` con ocho filmaciones del proceso, en 1080x1920 y de 3 a 6 segundos — exactamente el formato y la duración de los cortes. Nadie la había mencionado. Revisá las carpetas del proyecto y preguntá si tiene filmaciones o fotos antes de generar nada.

---

# PASO 6 · Conseguir las piezas visuales

Tres caminos, según lo que eligió en el paso 5.

## a) El usuario las genera

Es lo que suele preferir, porque itera hasta que le gustan. Dejale un archivo con **un prompt por corte**, en su carpeta del proyecto. Ver `references/prompts-visuales.md` para cómo escribirlos.

El archivo tiene que traer: un bloque de CONTEXTO para pegar una vez, un prompt por plano con su segundo y la frase que acompaña, y una sección de qué pedirle al generador cuando algo sale mal.

Que las nombre con el número del plano o con la frase del guion, en la carpeta del proyecto.

## b) Generarlas con Higgsfield

`generate_image_batch` con `soul_2`, `aspect_ratio: "9:16"`. Cuesta ~0,15 créditos por imagen: es prácticamente gratis.

**Mirá siempre el resultado antes de montarlo.** Una parte falla de formas que solo se ven mirando: un pedido de "termo estampado con efecto mármol" volvió como jarra de plata antigua. Armá una hoja de contactos numerada y revisala:

```bash
for i in 01 02 03; do convert p$i.png -resize 250x375^ -gravity center -extent 250x375 \
  -fill white -pointsize 32 -gravity northwest -annotate +8+6 "$i" l$i.jpg; done
montage l*.jpg -tile 6x2 -geometry +5+5 -background '#222' contactos.jpg
```

## c) Video en vez de foto

`generate_video` cuesta ~32,5 créditos por clip de 5 segundos. Vale la pena solo en el plano más importante; el resto queda bien con foto y paneo lento.

## Reglas que valen para las tres

**Coherencia técnica.** Si el producto enseña dos técnicas distintas, cada plano tiene que mostrar la que la voz está nombrando en ese momento. Un caso real: mostrar fibra de carbono (hecha con lámina impresa) justo cuando la voz dice que con aerosol eso es imposible contradice el argumento del video. Anotá en la lista de planos qué técnica corresponde a cada corte.

**Filmaciones propias: mirá los primeros segundos.** Un clip que arranca con el balde vacío desperdicia el corte. Recortalo con un offset de entrada.

---

# PASO 7 · Avatar

Si ya hay uno aprobado para este producto, **reusalo**. La continuidad entre OTOs de la misma marca suma.

Si hay que crearlo, ver `references/prompts-visuales.md`, sección avatar. Resumen: `generate_image` con `soul_2`, `9:16`, `count: 2`. El personaje tiene que ser creíble para el nicho, y su autoridad tiene que venir del **resultado visible** (el taller, las piezas terminadas detrás), nunca de credenciales inventadas — diplomas falsos de universidades reales son fabricar credenciales, no hacen falta y ensucian la marca.

**Elegí la variante de frente, cara centrada y boca cerrada o casi.** Una foto con la boca abierta a mitad de palabra produce artefactos de lip-sync.

**Para regenerar al mismo personaje en otro escenario, el modelo importa.**

`soul_2` **no** mantiene la identidad aunque le pases la imagen como referencia: devuelve personas distintas. `nano_banana_pro` y `gpt_image_2` **sí la mantienen** — misma cara, misma barba, misma ropa — pasando la imagen del avatar como `medias` con rol `image`. Comprobado: el mismo artesano en otro sector del taller, reconocible sin dudas.

Sirve para dos cosas:

- **Continuidad entre OTOs del mismo producto**: el mismo personaje en otro rincón del taller, con los objetos del OTO nuevo sobre la mesa.
- **Variar la postura** sin renderizar en tramos (ver paso 8).

En el prompt, abrí describiendo qué hay que conservar ("exactamente la misma cara, la misma barba, la misma remera y el mismo delantal; tiene que ser reconociblemente el mismo hombre") y recién después describí la escena nueva.

Generá con los dos modelos y compará: `nano_banana_pro` suele dar la boca más cerrada, mejor para lip-sync; `gpt_image_2` suele dar manos más limpias y expresión más cálida. **Miralos antes de elegir** — en una comparación real, la de `nano_banana_pro` tenía la mano sosteniendo un objeto indefinido que se habría notado en movimiento.

**El cambio de encuadre dentro de un mismo video se sigue haciendo en el montaje** (paso 9), no generando imágenes: ahí lo que importa es que el avatar hable, y eso sale de un solo render.

---

# PASO 8 · 🚪 Render en HeyGen

**Antes de lanzar**: verificá el saldo con `get_current_user` y decíle al usuario cuánto va a costar. El costo es **~20 créditos por minuto de video**. Un VSL de 3:38 costó 72 créditos.

`create_video_from_image` con la URL de la imagen del avatar:

```
voiceSettings: {"speed": 1.4}     # ritmo que sostiene la atención; 1.0 se siente lento
expressiveness: "medium"          # NUNCA "high" — ver abajo
aspectRatio: "9:16"               # 16:9 solo si la página se ve mayormente en desktop
resolution: "1080p"
caption: {"file_format": "srt"}   # SRT aparte, SIN quemar
motionPrompt: "Cámara completamente fija, montada en trípode, sin ningún movimiento ni
  temblor. El torso y la cabeza permanecen anclados y estables en el encuadre, sin
  balanceo ni desplazamiento del cuerpo. Solo gesticula con las manos y los antebrazos,
  con variedad natural: a veces las dos manos abiertas al frente, a veces una sola mano
  señalando, a veces las manos apoyadas y quietas mientras habla."
```

## ⚠️ HeyGen anima todo lo que parezca un personaje

Si en la foto del avatar hay muñecos, figuras, maniquíes o cualquier cosa con cara, **HeyGen se los anima**: saltan, giran la cabeza, mueven los brazos durante todo el video. El usuario lo describió así: *"los muñecos se mueven en todo el video, saltan, se miran, mueven las manos"*. No hay parámetro que lo apague.

**Se resuelve en la imagen, no en el render.** Regenerá el avatar con las figuras **lejos del plano de la persona**: sobre un pedestal a un costado, en estantes del fondo, o directamente fuera de cuadro. Cuanto más chicas y más al fondo, menos las toca. Objetos sin cara —piezas de auto, cascos, aerosoles, llantas— no se animan.

**🔴 Los tejidos con patrón también cuentan como cara**. En un tapiz de macramé con cuentas, HeyGen dibujó labios fantasma que se movían. Tapices, mandalas, tejidos con cuentas o nudos simétricos, cualquier patrón con "dos ojos y una boca", van fuera del plano del avatar. Se arregló editando la foto del avatar sin el tapiz.

**Aun con la pared lisa pueden quedar manchas de 1 a 2 s.** Antes de entregar, escaneá el render buscando movimiento en zonas que deberían estar quietas, por ejemplo con la diferencia entre cuadros sobre el fondo. Cada mancha que aparezca se tapa con el filtro `delogo` de ffmpeg, en ese rectángulo y solo en ese tramo (`enable='between(t,a,b)'`).

Revisá esto **antes** de renderizar: son 40 créditos por descubrirlo después.

## ⚠️ La vibración de cámara — el defecto que hay que prevenir

HeyGen, al animar una foto fija, le agrega un **temblor de cámara en mano simulado**. Con `expressiveness: "high"` es fuerte, y el comprador lo describe como *"parece que le está pegando a la mesa y vibra la cámara continuamente, medio molesto"*.

Medido sobre la franja de fondo del taller, que debería estar quieta:

| | Temblor por cuadro | Recorrido real |
|---|---|---|
| Render crudo, `expressiveness: "high"` | **3,0 / 3,8 px** | 24 / 33 px |
| Tramos de imagen del montaje (Ken Burns) | 0,8 / 1,4 px | 31 / 53 px |
| B-roll filmado a mano de verdad | 3,4 px | **110 px** |
| Render después de estabilizar | **0,4 / 0,8 px** | 21 / 33 px |

Lo que molesta no es el temblor solo: es **temblar mucho y desplazarse poco**. Un b-roll real tiembla igual pero recorre 110 px, y por eso se lee como cámara en mano y no como vibración.

**Los dos arreglos, y hacen falta los dos:**

1. **En el origen** — `expressiveness: "medium"` y un `motionPrompt` que diga *cámara fija, torso anclado*. Nunca uses lenguaje de movimiento de cámara ni "se inclina hacia la cámara": eso lo empeora.
2. **En la edición** — `scripts/estabilizar.py` sobre el render bajado, **antes de montar**. Es una pasada de `vidstab`, **no gasta créditos**, conserva el conteo exacto de cuadros (lo verifica y aborta si cambia) y deja el temblor por debajo del de tus propias fotos. Cuesta ~3% de zoom, imperceptible.

```bash
python3 scripts/estabilizar.py render_crudo.mp4 render.mp4
```

**El montaje del paso 9 se hace sobre `render.mp4` (el estabilizado), nunca sobre el crudo.**

**No pases `style` dentro de `caption`.** Los subtítulos que quema HeyGen salen chicos y pegados al borde inferior. Los vas a quemar vos con control total en el paso 11.

**Variación de postura del avatar:** HeyGen anima una sola foto, así que la postura de base es fija. Hay dos formas de variarla, y conviene ofrecer las dos:

1. **Generar variantes del avatar con `nano_banana_pro` o `gpt_image_2`** (ver paso 7), cada una en otra postura — apoyado con las dos manos en la mesa, con una mano levantada, con gestos amplios — y renderizar cada tramo del guion con la variante que le toca. La identidad se mantiene porque salen de la misma referencia.
2. **Renderizar el guion en tramos, cada uno con su propio `motionPrompt`** (uno con las dos manos apoyadas en la mesa, otro con una sola mano levantada, otro con gestos amplios). Como todos salen de la misma foto, la identidad se mantiene idéntica. Cuesta lo mismo, porque se paga por duración total. El riesgo es una micro-pausa en las uniones, porque cada tramo genera su propio audio.

Un video de 3-4 minutos tarda unos 10 minutos en renderizar. Poleá `get_video` con esperas de ~2 minutos.

Del resultado sirven `video_url` (limpio) y `subtitle_url` (el SRT). **Ignorá `captioned_video_url`.**

Bajá los dos y anotá el **número exacto de cuadros** del render, que es la referencia de todo el paso 9:

```bash
ffprobe -v error -select_streams v:0 -count_frames \
  -show_entries stream=nb_read_frames,r_frame_rate -of csv=p=0 render.mp4
```

---

# PASO 9 · Estabilizar el render

No gasta créditos. Se corre sobre el MP4 que bajaste de HeyGen y produce el archivo sobre el que se monta todo lo demás.

```bash
python3 scripts/estabilizar.py render_crudo.mp4 render.mp4
```

El script mide el temblor antes y después e imprime la reducción. Si el temblor final queda por encima de 1,5 px, subí `smoothing` a 45 y repetí. **Verifica el conteo de cuadros y aborta si cambió**: si aborta, no montes — se rompería la sincronía de labios.

**Tarda.** Las dos pasadas sobre un video de 2:30 en 1080x1920 llevan varios minutos y la segunda puede pasarse del límite de 10 minutos por comando. Si se corta, lanzalo en segundo plano y revisá el log:

```bash
nohup python3 scripts/estabilizar.py crudo.mp4 render.mp4 > /ruta/absoluta/estab.log 2>&1 &
```

El `.trf` de la pasada 1 queda cacheado en `/tmp`, así que si se corta la segunda no hay que rehacer la primera. **Usá rutas absolutas para el log**: el directorio de trabajo se resetea entre comandos y un log relativo se pierde.

El porqué y los números medidos están en el paso 8, en "La vibración de cámara".

---

# PASO 10 · Montaje con verificación de sincronía

Usá `scripts/montar_vsl.py`. Leé su cabecera para el formato del JSON de configuración.

**El `render` del config apunta al archivo estabilizado del paso 9, no al crudo.**

Si lo lanzás en segundo plano, **usá rutas absolutas para el config y para el log**. El directorio de trabajo se resetea entre comandos y un log relativo se pierde sin dejar rastro:

```bash
nohup python3 scripts/montar_vsl.py /ruta/absoluta/config.json > /ruta/absoluta/montaje.log 2>&1 &
```

## Qué hace

- **Corta el render del avatar en tramos y le alterna el zoom** (1.00 / 1.16 / 1.22 / 1.06...). Simula multicámara con un solo render y evita que el ojo se acostumbre.
- **Intercala las piezas visuales** en los segundos indicados, con un paneo lento para que las fotos no queden congeladas.
- **Concatena y remuxea con el audio original**, que nunca se corta.

## ⚠️ El error que hay que evitar sí o sí

**Todo se calcula en cuadros, nunca en segundos.**

En producción real, pedirle a ffmpeg tramos en segundos hizo que cada uno se redondeara al cuadro más cercano —40 ms a 25 fps— y esos redondeos se fueron acumulando siempre para el mismo lado. Con 31 tramos, el montaje terminó **0,56 segundos más largo** que el render. Resultado: la imagen se atrasaba respecto del audio, cada vez más hacia el final. El usuario lo describió como *"primero va la voz y después mueve la boca"*.

El script ya trabaja en cuadros y verifica en dos niveles:

1. **Cada tramo**, apenas se genera, tiene que tener exactamente los cuadros pedidos.
2. **El montaje completo** tiene que tener exactamente los mismos cuadros que el render de HeyGen.

Si cualquiera de las dos falla, el script aborta. No entregues un video sin ese chequeo, y **decíle al usuario el número**: "5.452 cuadros planificados, 5.452 reales, idénticos al render".

## Verificar que cada corte cae donde debe

Extraé el SRT y buscá el segundo exacto de la frase de cada corte, en vez de estimar:

```bash
python3 - <<'EOF'
def sec(t):
    h,m,r=t.split(':'); s,ms=r.split(',')
    return int(h)*3600+int(m)*60+int(s)+int(ms)/1000
for b in open('render.srt',encoding='utf-8').read().strip().split('\n\n'):
    L=b.strip().split('\n')
    if len(L)<3: continue
    a,_,e=L[1].partition(' --> ')
    print(f"{sec(a):7.2f} - {sec(e):6.2f}  {' '.join(L[2:])}")
EOF
```

Después del montaje, sacá un cuadro de cada corte y **mirálos**:

```bash
for t in 13 22 41 55; do ffmpeg -v error -ss $t -i final.mp4 -frames:v 1 -update 1 q$t.jpg -y; done
montage q*.jpg -tile 4x1 -geometry +4+4 -resize 330x -background '#222' chequeo.jpg
```

Se encontraron así dos errores que no se ven de otra forma: un clip cayendo sobre la frase siguiente en vez de la suya, y unas piezas apareciendo tres segundos tarde. Ambos se ven de inmediato en la hoja de contactos porque el subtítulo quemado dice qué frase está sonando.

---

# 🔴 El cierre del VSL apunta al botón 

En los últimos segundos, cuando la voz dice que el precio está debajo, se quema en el video una caja del color del producto con "**Toca el botón de abajo**" (en el idioma y el registro de la tienda: tú neutro para LATAM) y **tres flechas ▼▼▼** debajo, que quedan hasta el final. La página que lo contiene sigue el modelo de `WIKI/embudo-postcompra.md` del cerebro: marco foil, oferta oculta hasta ese segundo.

# PASO 11 · Subtítulos y entrega

## Subtítulos

Convertí el SRT a ASS con `scripts/srt_a_ass.py` y quemalo con el filtro `ass`.

**⚠️ El detalle que rompe todo:** si usás el filtro `subtitles` sobre un SRT pelado, libass asume un lienzo de **384×288**, y cualquier `MarginV` en píxeles de video manda el texto fuera de pantalla. Pasa en silencio: el video sale sin subtítulos y sin ningún error. Hay que escribir el ASS con `PlayResX: 1080` y `PlayResY: 1920`.

Estilo que funciona en vertical:

```
Fontname DejaVu Sans · Fontsize 62 · Bold · blanco
Outline 6 negro · Shadow 3 · Alignment 2 · MarginV 640
```

`MarginV 640` deja el texto **a la altura de las manos** del avatar, no pegado al borde. Integrado en el cuerpo se lee mejor y disimula bastante el aire de video generado.

## Entrega

Dos topes que van a morder: **30 MB por archivo al chat** y **20 MB por archivo al escribir en la máquina del usuario**. Un VSL de 3:38 en 1080p pesa ~158 MB, así que el master no pasa por ningún lado.

### 🚫 Un solo archivo, siempre

**Nunca entregues dos versiones.** Se hizo una vez —una "web" y una "chica"— y el usuario respondió: *"¿POR QUÉ SIEMPRE ME TIRÁS UNO QUE DICE OTO CHICO?"*. Tener que elegir entre dos archivos casi idénticos es trabajo que le estás pasando a él.

Entregá **un solo MP4 que entre bajo los 20 MB**, así sirve para el chat y para su carpeta sin decidir nada. A 720×1280 con CRF ajustado, un VSL de 2-3 minutos entra sin que se note la diferencia en mobile, que es donde se ve el 90% de estos videos.

```bash
# apuntá a ~18 MB; calculá el bitrate según la duración real
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 master.mp4)
BR=$(python3 -c "print(int((18*8192)/$DUR - 96))")   # kbps de video para 18 MB
ffmpeg -y -i master.mp4 -vf scale=720:1280 -c:v libx264 -b:v ${BR}k \
  -maxrate $((BR*3/2))k -bufsize $((BR*2))k -preset slow \
  -c:a aac -b:a 96k -movflags +faststart NOMBRE_OTO.mp4
```

Verificá el tamaño antes de entregar. Si pasa de 20 MB, bajá el objetivo a 16 y repetí — nunca partas en dos archivos.

Las escrituras a la máquina del usuario pueden fallar por timeout si su conexión es lenta. **Reintentá una vez** antes de reportar el problema; suele funcionar en el segundo intento.

En la carpeta del proyecto dejá también el **guion final** y las **piezas visuales**, para que pueda reusarlas en anuncios.

## Cierre

Decí explícitamente:

- Los once pasos recorridos
- El resultado de la verificación de sincronía, con el número de cuadros
- Los créditos gastados y los que quedan
- Qué quedó pendiente

---

# Después del video

Dos cosas que conviene dejar planteadas, porque el usuario suele estar pensando solo en el video:

**La página del OTO** pesa tanto como el video: titular arriba, botón de compra grande con el precio escrito, botón de rechazo chico y con costo escrito ("No gracias, prefiero seguir sin X"), y ningún link de escape.

**El producto tiene que existir.** El video promete entregables concretos. Si el producto todavía no está hecho, el guion sirve de especificación: cada promesa es un capítulo obligatorio. Ofrecé armar esa especificación.

## 🚪 Auditar el producto contra el guion

Cuando el ebook esté hecho, **abrilo y contá las promesas una por una contra el guion**. No preguntes si están: verificá. En producción real aparecieron dos fallas, y las dos en los dos libros a la vez:

**Los capítulos de proveedores salieron vacíos.** Los dos ebooks traían una tabla "insumo / cómo pedirlo" y un recuadro en blanco que decía "anotá acá tus precios". Los dos videos prometían *"nombres, links y precios reales"*. Enseñaban a preguntar, no decían dónde comprar. Es la promesa que más se incumple porque es la única que exige investigación real, fuera del alcance de un generador de páginas.

**Las promesas contables no daban el número.** El video prometía "cuarenta diseños" y el libro traía cuatro láminas adentro del PDF. La tapa del propio ebook repetía "40 DISEÑOS". Una promesa con número es la más fácil de verificar para el comprador: se sienta, cuenta, y pide el reembolso.

Cómo auditar, en concreto:

1. Sacá del guion **cada promesa numerable y cada entregable con nombre propio**.
2. Renderizá el PDF a imágenes (`pdftoppm -jpeg -r 40`) y armá hojas de contacto de 16 páginas para leer los títulos de un vistazo.
3. Buscá específicamente: el capítulo de proveedores, las tablas con datos, y cualquier cosa que el video prometa por cantidad.
4. Marcá **tablas en blanco para completar**: pueden ser una decisión de diseño válida, pero si el video promete el dato y el libro pide que lo averigüe el comprador, hay desajuste.
5. Decí qué falta con la página exacta, y ofrecé las dos salidas: completar el producto, o corregir esa línea del guion antes de publicar.

Un producto con garantía de 120 días y una promesa contable incumplida es un reembolso programado.
