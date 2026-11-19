---
name: imperioproducto
description: Lleva un producto digital del 0 al 100% y después maneja sus campañas — caza la oferta, la arma con precio y bonos, produce el ebook, carga la tienda en Impultienda con landing y tracking, hace los 10 anuncios, deja la campaña de Meta entregando y la gestiona todos los días con las reglas de escala, corte y OTOs. Orquesta a las demás skills Imperio en orden y lleva una ficha con el porcentaje de avance de cada producto. Usar cuando el usuario diga "imperioproducto", "lanzá un producto", "de cero a cien", "armá todo el producto", "seguí con el producto", "en qué está tal producto", "manejá las campañas", "cómo vienen las campañas", "qué hago hoy con las campañas", o cuando pida llevar una oferta de punta a punta.
---

# ImperioProducto — del 0 al 100%, y después manejarlo

Esta skill **no hace el trabajo de las otras: las llama en orden** y no deja que se
saltee nada. Es el director de orquesta de tus productos digitales.

**El canon está en `WIKI/metodo-producto-digital.md`.** Leelo antes de arrancar. Si otra
nota dice distinto, manda esa página, salvo que el usuario diga otra cosa en la conversación.

Hablale al usuario en español rioplatense, con voseo.

---

## 🔴 REGLAS QUE NO SE NEGOCIAN

1. **Una fase no se da por cerrada sin su verificación.** "Listo" quiere decir cargado,
   en producción y verificado. No "creado".
2. **Los OTOs NO se construyen antes de validar.** Se construyen al primer escalado.
   🔔 Y al primer escalado **se pregunta solo**: *"¿vamos con los OTOs?"*
3. **Nada se prende sin la checklist de 10 puntos al 100%**, anuncio por anuncio.
   Crear ≠ publicar ≠ entregar.
4. **Lo que gasta plata por primera vez lo aprueba el usuario.** Frenar (bajar, pausar)
   siempre se puede sin pedir.
5. **Todo se anota en la ficha** del producto, en el momento. Si no está en la ficha,
   no pasó.
6. **Se pide todo junto, una sola vez por fase.** Nunca ir pidiendo de a una cosa.
7. 🔴 **Un producto a la vez:** primero optimizado en **tu mercado principal**, después
   **la región** (otros países del mismo idioma), después otros idiomas. No se abre el siguiente
   mercado hasta que el anterior está optimizado.
8. 🔴 **Nunca mostrar tus productos reales en piezas públicas que no sean su propio anuncio**
   (contenido educativo, anuncios de otra oferta, ejemplos de "lo que hace Claude"). Ni landings,
   ni ebooks, ni anuncios, ni bonos, ni tiendas: **te los copian**. Se arma un ejemplo inventado o
   se pregunta antes. El anuncio de un producto muestra solo ese producto.

---

## Paso 0 — ¿Qué modo?

| El usuario dice… | Modo |
|---|---|
| "lanzá", "de cero", "armá el producto", "seguí con X" | **LANZAR** → buscar la ficha y retomar en la primera fase sin cerrar |
| "manejá", "cómo vienen", "qué hago hoy", "revisá las campañas de X" | **MANEJAR** → ir directo a F6 |
| "en qué está X" | **ESTADO** → leer la ficha y devolver el tablero, nada más |

### La ficha

Vive en `OUTPUTS/lanzamientos/<producto-en-kebab-case>.md`. Si no existe, se crea con
la plantilla de `references/ficha.md`. **Primero se busca** (`ls OUTPUTS/lanzamientos/`):
nunca crear una segunda ficha del mismo producto.

Al abrir la sesión, mostrar siempre el tablero así (ejemplo):

```
MI PRODUCTO ES — 55%
✅ F0 Cazar  ✅ F1 Oferta  ✅ F2 Producto  ✅ F3 Tienda
⬜ F4 Creativos  ⬜ F5 Campaña  ⬜ F6 Validar  ⬜ F7 Escalera
Sigue: F4. Falta de vos: nada todavía.
```

Si algo necesita una decisión o una acción que solo puede hacer el usuario, agregalo a la
lista **"Esperando por mí"** de `BRIEFING.md`, una línea por ítem, y sacalo cuando se resuelva.

---

# MODO LANZAR

Cada fase: **relevar solo → pedir todo junto → ejecutar → verificar → tildar en la ficha.**

## F0 · Cazar (→ 10%)

- Llamar a **`/imperiowhale`**. Si el usuario ya trae la oferta, saltear la caza y anotar de dónde salió.
- Filtro: 50+ ads, 3+ días; score de 4 señales; **los días mandan sobre los ads**.
- **Entrar a la landing de la competencia y anotar el precio real.**
- 🤝 **Puerta:** el usuario elige cuál. Ofrecer 3 como máximo, con la recomendada primero.
- ✅ **Verificación:** la ficha tiene anunciante, link de la biblioteca, días corriendo, precio real y mercado destino.

## F1 · Armar la oferta (→ 20%)

Proponer en **un solo mensaje**:

| Qué | Regla |
|---|---|
| Nombre y promesa | el atajo, no el conocimiento. "Número grande + y vendelo" si aplica |
| Precio del front | **fijo: 19,90 en habla española, 27 en habla inglesa.** No se propone otro |
| 2-4 bonos | la fricción convertida en bono. Bonos estándar del canon |
| Anclaje | valor tachado, "5X1", licencia de reventa en el FAQ |
| 10 ángulos | uno por anuncio. Se segmenta en el anuncio, no en la landing |
| Neto y CPA de equilibrio | neto = precio − comisión de la pasarela − 0,30 |
| Escalera de OTOs | **fija** (español 47/27/17/12 · inglés 97/47/27/17). Solo el plan: no se construye hasta F7 |
| Garantía | **SIEMPRE 120 días** |
| Formato | **oferta única** (no catálogo) |

- 🤝 **Puerta:** el usuario aprueba precio y bonos.
- ✅ **Verificación:** la ficha tiene precio, bonos, ángulos, neto y CPA de equilibrio.

## F2 · Producir (→ 35%)

- Llamar a **`/imperioebook`** para el front y para cada bono.
- **Muestra de 3 páginas primero.** Aprobación. Recién ahí el lote.
- Ficha de datos bloqueada (`ficha_datos.md`): los números del producto no se inventan.
- ✅ **Verificación:** el índice coincide con el PDF (páginas reales), el PDF abre, pesa menos de 50 MB.
- 👤 **Puerta:** el usuario abre el PDF y lo aprueba.

## F3 · Tienda (→ 55%)

**Relevar solo:** `impultienda_listar_tiendas`, `impultienda_ver_plan`, `impultienda_estado_onboarding`.

**Pedir todo junto, una vez:** ¿tienda nueva o cuál existente (por ID)? · ¿pasarela? · ¿dominio? · ¿píxel creado (ID)?

Ejecutar en este orden:

1. Tienda **con la zona horaria de tu mercado** → **moneda primero, idioma después**
2. Producto → entregable (`impultienda_cargar_entregable`) → bonos con valor 0
3. Precio y tachado (`impultienda_fijar_precio`)
4. Pasarela: `impultienda_conectar_pasarela` devuelve el link → **👤 el usuario** carga las credenciales
   (Claude nunca las tipea)
5. Sitio de negocio (`impultienda_guardar_sitio_negocio` + verificar): evita los bloqueos de Stripe
6. Dominio → `impultienda_verificar_dominio`
7. Landing: llamar a **`/imperiolanding`**. Se arma **completa**; donde todavía no hay reseñas
   o cifras reales, van **marcadores visibles** que el usuario reemplaza por los datos reales
   antes de publicar. Nada se publica sin que el usuario la revise.
8. Título de pestaña y meta descripción
9. Checkout con teléfono y apellido activados
10. **Píxel y CAPI** (`impultienda_configurar_tracking`), después del dominio final

🔴 **Sin order bump ni post-compra en el día 0.**

✅ **Verificación, toda junta:**
- `impultienda_estado_onboarding` → `puede_cobrar: true` y `listo_para_anunciar: true`
- La landing abre en el navegador, precio correcto, cero scroll horizontal a 390 px
- 👤 **Compra de prueba** de punta a punta: cobra, llega el mail, llega el PDF correcto

## F4 · Creativos (→ 70%)

- Preguntar si conviene pasar al modelo más potente disponible antes de llamar a la skill de reels.
- **Antes de editar, leer lo aprendido** en `RAW/bitacora/productos.md` y `RAW/bitacora/edicion.md`
  (y en la WIKI, si el Cerebro ya lo destiló) y pasarle a la skill de edición lo que aplique.
  Lo que ya se aprendió no se vuelve a pagar.
- **10 anuncios, un ángulo cada uno**, de los 10 de F1, con **`/imperioreelscorto`** (perfil **B**
  para infoproducto), con la paleta **del producto**.
  - Si querés un **test A/B de edición**, partilos 5 y 5 entre dos estilos (por ejemplo
    `/imperioreelscorto` y `/imperioreels`), con los mismos ángulos repartidos en los dos grupos
    y una sigla del estilo en el nombre del anuncio para poder separarlos al medir
  - Cuando un estilo gane en 2 lanzamientos seguidos, pasa a hacer los 10
- Copy de cada anuncio: cuerpo con emojis · titular · descripción · botón `DOWNLOAD`.
- 🤝 **Puerta:** el usuario aprueba los textos. **El creativo es inmutable**: después no se cambia.
- ✅ **Verificación:** `ffprobe` uno por uno (duración, 1080x1920, audio). Miniatura propia por anuncio.

## F5 · Campaña entregando (→ 85%)

- Llamar a **`/imperiocampana`**. Ella hace la fase 0 de los videos en paralelo, el
  presupuesto (ticket × 3, hacia arriba al múltiplo de 5), las UTMs y la checklist.
  Detalle y errores conocidos: `WIKI/montaje-de-campanas.md`.
- Después, **`/imperioauditoria`** sobre la cuenta y la tienda. Tiene que volver sin errores.
- 👤 **Puerta: ACTIVAR.** Se pide con un resumen de una línea: cuenta, presupuesto, 10 anuncios, landing.
- ✅ **Verificación doble:** cada anuncio leído por id vuelve `ACTIVE` **y** la columna
  Entrega del Administrador no dice "Borrador". **Y además gasto de HOY > 0.** Recién ahí
  se escribe "entregando". "Activa" no es "gastando": una tarjeta frenada no la ve la API.
- Anotar en la ficha: cuenta, ID de campaña, ID de conjunto, presupuesto, fecha y hora de encendido.

---

# MODO MANEJAR (F6 → 95%)

Se corre **todos los días**. Si ya escalaste a una cuenta horizontal, ahí cada 2 h en horario
de actividad (por ejemplo, de 07:00 a 20:00).

## 1. Leer

Por cada campaña viva de la ficha:

- `ads_get_ad_entities` con `fields` explícitos: gasto (`amount_spent`), compras, ROAS, CPM, CTR, costo por visita
- En tres ventanas: **hoy, 3 días, 7 días**
- `impultienda_listar_ventas` del mismo período, para cruzar. Meta puede subestimar algunos
  medios de pago (por ejemplo, Mercado Pago) durante horas

## 2. Decidir con la tabla

| Situación | Acción | Permiso |
|---|---|---|
| **3 ventas o más Y ROAS > 1,8** | **+30%**, sin redondear. **Se carga a las 23:30** para que arranque al día siguiente | 🤖 **automático**, sin preguntar |
| 🔔 **Es el primer escalado** | **Preguntar "¿vamos con los OTOs?"** | — |
| ROAS < 2 | **−20%** | 🤖 ejecutar |
| Sigue bajando 2 h después | Otro −20% | 🤖 ejecutar |
| Sigue bajando | Apagar el anuncio que más gasta sin vender | 🤖 ejecutar |
| Día 3 | Proponer renovación: 10 anuncios en conjunto nuevo | 🤝 |
| Día 4 sin ventas | Pausar y proponer 10 ángulos nuevos | 🤝 |
| −100 a −150 USD, o 2-3 días negativo seguidos | **Proponer cortar la oferta** | 🤝 |

- **Paciencia:** los primeros 3 días no se toca la estructura.
- **Las subidas se cargan a las 23:30** y arrancan al día siguiente. Nunca de madrugada.
- Bajar y pausar se hace en el momento, sin esperar a la noche.
- 🔴 **Un cambio de presupuesto por API queda en borrador.** Publicarlo con
  `ads_activate_entity` y verificarlo en el Administrador.

## 3. Si no vende, diagnosticar en este orden

1. **¿Entrega?** ACTIVE con **gasto de HOY en 0** = borrador, medio de pago o píxel.
   Se mira solo hoy (si arrancó hoy, ayer en 0 está bien). Lo primero: **Facturación** de
   la cuenta en el navegador, porque el bloqueo de la tarjeta no aparece por API
2. **¿CPM y costo por visita?** Techo = neto del ticket × conversión visita→compra
3. **¿Creativo?** CTR de cada anuncio
4. **¿Embudo?** Landing→checkout 8-16% · checkout→compra 12-17%. 50 checkouts y 0 compras = la oferta
5. **¿Ubicaciones?** Instagram, stories y profile feed por separado

## 4. Medir y aprender

Una vez por día, por cada anuncio que gastó:

1. Pedir a Meta impresiones, vistas de 3 s, ThruPlay, clics al link, visitas, checkouts,
   compras, gasto y ventas
2. Agregar una fila a `OUTPUTS/lanzamientos/metricas-anuncios.csv` con hook rate,
   hold rate, CTR, costo por visita, CPA y ROAS
3. Comparar contra los demás anuncios del mismo lanzamiento y contra los anteriores
4. Si aparece un patrón (gastó 1 ticket o más y se repite en 2 anuncios), anotarlo en
   **`RAW/bitacora/productos.md`**. Con un solo caso va como `(hipótesis)`.
   🔴 **Nunca escribir en `WIKI/`**: la WIKI la escribe solo el agente Cerebro, después
   de analizar la bitácora con el usuario (ver `CLAUDE.md`)
5. Si un aprendizaje se confirma 3 veces, proponer el cambio en la skill de edición
   que corresponda (`imperioreelscorto` o `imperioreels`), con la regla de las 3 copias

## 5. Reportar

Una línea por campaña, siempre con este formato (los números son de ejemplo):

```
MI PRODUCTO ES · Campaña 1 · día 3
Gasto 120 · 7 compras · ROAS 2,3 (hoy) / 2,0 (3d) / 1,9 (7d)
→ +30%: 60 → 78. ¿DALE o NO?
```

Y anotar la decisión en la ficha, con fecha y hora.

---

# F7 · Escalera y escala (→ 100%)

Solo cuando el usuario dijo que sí a los OTOs.

1. Escalera fija, el más caro primero: **español 47 / 27 / 17 / 12 · inglés 97 / 47 / 27 / 17**.
2. Ebooks de los OTOs con **`/imperioebook`**.
3. VSL de cada OTO con **`/imperiootos`**.
4. `impultienda_crear_funnel_postcompra` + `impultienda_configurar_downsell`: cada OTO con
   su downsell al **50%**, presentado como **juego en HTML** (ruleta, dados o cartas) con
   `impultienda_guardar_html_postcompra`.
5. 🔴 **Verificar que el funnel exista**: `impultienda_ver_postcompra` no puede volver con `funnels: []`.
   Marcar un producto como post-compra no lo pone en el embudo.
6. 👤 Compra de prueba que pase por los OTOs.
7. **Escala horizontal:** ganadores a otra cuenta, mismo píxel. **Otro idioma:** **`/imperiotranslate`**.

✅ La ficha llega a 100% cuando el funnel está verificado y la compra de prueba pasó por él.

---

## Cierre de cada sesión

1. Ficha actualizada con el tablero y el porcentaje
2. Todo lo aprendido → **`RAW/bitacora/productos.md`**, al final, con fecha absoluta: lo que
   falló, números reales, decisiones del usuario y su motivo, limitaciones, contradicciones
   con el cerebro. Crudo y corto. **Nunca en `WIKI/` ni en `changelog.md`**: eso lo
   escribe el agente Cerebro
3. `BRIEFING.md` → lista "Esperando por mí" al día
4. Decirle al usuario **qué sigue y qué falta de él**, en dos líneas
