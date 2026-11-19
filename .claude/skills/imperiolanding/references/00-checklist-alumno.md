# Checklist antes de armar la landing

Mostrale esto al usuario al empezar, en dos bloques: lo que tiene que estar cargado en Impultienda y lo que tiene que estar en la carpeta.

Presentalo como una lista con ✅ y ❌ según lo que encontraste, no como un cuestionario. Vos entrás al panel y mirás; no le preguntes lo que podés verificar solo.

---

## 0. La tienda

Antes de mirar nada más: **confirmá sobre qué tienda se trabaja.** Una cuenta de Impultienda puede tener muchas, y el selector de arriba a la izquierda arranca en la última que el alumno usó.

- [ ] Abriste el selector y leíste **todas** las tiendas (nombre + dominio)
- [ ] El alumno te dijo cuál — o hay una sola y se lo avisaste
- [ ] Anotaste el `<slug>` / dominio de esa tienda

Todo lo que sigue pasa adentro de esa tienda y de ninguna otra.

---

## A. En el panel de Impultienda

### 1. Ebook principal — `Diseño de ebooks`

- [ ] Está creado y tiene **título** y **descripción**
- [ ] Dice **"Listo"** y muestra "Descargar PDF" → el PDF está cargado
- [ ] Tiene **portada/mockup**
- [ ] En "Precio, título y más": **precio actual** y **precio anterior** (tachado)

Si dice **"Subir"** en vez de "Listo", el PDF no está y **el comprador no recibe nada**. Frená ahí.

### 2. Bonos — `Diseño de ebooks → Bonos`

- [ ] Cada bono dice **"Listo"**
- [ ] Cada bono tiene portada
- [ ] El **valor de cada bono está en 0** si se entregan gratis con la compra

Sobre el valor de los bonos: Impultienda calcula el ahorro como
`precio_anterior + valor_de_los_bonos − precio_final`.
Si le ponés valor a un bono que regalás, el "Ahorrás" se infla y deja de coincidir con la resta que el comprador hace de cabeza (anterior − final). Eso se nota y quema confianza. **Bonos que se regalan → valor 0.**

Anotá cuántos bonos hay. La landing tiene que decir el mismo número. Si el panel dice "Bonos 3" y la landing promete 5, hay un problema.

**El título del bono no lleva prefijo.** La tienda ya le agrega "Bono #N:" sola. Si escribís "Bono 1: Tal cosa" queda "Bono #1: Bono 1: Tal cosa".

### 3. Upsells y downsells — `Diseño de ebooks`

- [ ] Si los usa: cada uno dice "Listo" y tiene precio
- [ ] Si no los usa: que estén desactivados

### 4. Cobros — `Configuraciones → Pagos`

- [ ] Al menos un procesador dice **CONECTADO**
- [ ] Anotá el **modo de cobro**

⚠️ **Multidivisa**: los precios se guardan **en dólares** y se convierten solos a la moneda de cada comprador. Cargar `16990` pensando en pesos hace que el checkout cobre US$16.990. Si está en multidivisa, confirmá con el usuario que el número que cargó está en USD.

Efecto secundario normal: el precio en pesos se mueve solo cuando se mueve el dólar. No es un error.

### 5. Campos del checkout — `Configuraciones → Pagos`

- [ ] **Teléfono** activado (+44% de calidad de coincidencia en Meta)
- [ ] **Apellido** activado (+25%)

Más datos en el checkout = mejor atribución = anuncios más baratos. Vale la molestia.

### 6. Meta — `Configuraciones → Meta / Tracking`

- [ ] **Pixel ID** cargado
- [ ] **Token de API de Conversiones (CAPI)** cargado
- [ ] **Verificación de dominio** hecha

Sin pixel la landing igual funciona, pero no se puede anunciar con optimización. Avisale.

---

## B. En la carpeta

### Imprescindible

| Archivo | Para qué |
|---|---|
| **Imagen creativa larga** de la landing (`.webp`, `.png` o `.jpg`) | Es el cuerpo de la página. Suele ser angosta y muy alta (1000 × 6000px). |

Con eso solo ya se puede construir una landing completa.

### Recomendado

| Archivo | Para qué |
|---|---|
| **PDF del ebook principal** | Sacar 6-8 páginas del interior para el carrusel 3D. Da muchísima confianza. |
| **Fotos de resultados reales** | Objetos terminados. Van en el carrusel y en las opiniones. |
| **Capturas de opiniones reales** | MercadoLibre, Instagram, WhatsApp. Para el bloque de opiniones. |
| **Logos de pago** (MercadoPago, Visa, Mastercard) | Para el bloque de métodos de pago. **Pediselos siempre**: es un bloque de confianza barato y siempre los tienen a mano. |
| **Puntaje y cantidad de reseñas** del producto | La línea de estrellas arriba del titular. Son datos del usuario: pediselos, no los estimes. |

### Sobre los testimonios: van todos

Si el usuario manda un archivo con testimonios, **entran todos a la landing**, no una selección. Los 5 primeros al carrusel (con imagen generada), el resto al muro del final. Un archivo de 25 testimonios tiene que terminar en 25 testimonios publicados.

### Sobre las opiniones

Si el usuario tiene reseñas, preguntale **de dónde salieron** antes de publicarlas, y encabezá el bloque con esa fuente:

> "Opiniones de compradores en MercadoLibre"

Si todavía no vendió, **el bloque va con `COMPLETAR` visible**. No lo llenes con nada inventado. Ver `05-reglas-de-honestidad.md`.

### Sobre las fotos de personas

Fotos de **objetos y resultados**: todas las que quieras, generadas o reales.

Fotos de **caras**: solo si son de esa persona concreta y esa persona dijo esa frase concreta. Una foto de stock, una cara generada por IA, o la foto de un cliente real al lado del testimonio de otro, todo eso es fabricar un respaldo que nadie dio. Si no hay foto que corresponda, usá el avatar con la inicial del nombre: queda bien y no miente.

---

## Qué decirle si falta algo

Cortito y accionable:

> Antes de arrancar necesito dos cosas:
>
> **En el panel** — el Bono 2 no tiene el PDF cargado (dice "Subir"). Si alguien compra hoy, no lo recibe.
>
> **En la carpeta** — está la imagen larga, perfecto. Si tenés el PDF del ebook te saco 7 páginas del interior para mostrar un adelanto; eso levanta bastante la conversión. Si no lo tenés a mano, arranco igual y lo sumamos después.
