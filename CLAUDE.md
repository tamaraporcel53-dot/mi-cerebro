# Mi Segundo Cerebro — reglas para todos los agentes

Este archivo lo leen **todos los agentes en cada mensaje**. Por eso es corto: acá va solo lo que sirve a todos.
El agente **Cerebro** lee además [WIKI/protocolo-cerebro.md](WIKI/protocolo-cerebro.md) al arrancar.

## Sobre mí (completalo el primer día)

- **Nombre:** Tamy
- **Cómo quiero que me hablen:** español rioplatense
- **A qué me dedico:** vendo ebooks digitales
- **Mi objetivo de los próximos 90 días:** USD 1.000 por día de **ganancia** (lo que queda después de anuncios y comisiones, no facturación), para el 2027-02-17 (definido el 2026-11-19)

> Primer mensaje sugerido al agente Cerebro: *"Leé CLAUDE.md y hacéme las preguntas para completar 'Sobre mí'."*

## Qué dato manda

1. **Lo que digo en la conversación** — primera mano, manda sobre todo.
2. **Lo que subo a `RAW/`.**
3. Todo lo demás.

- **Un dato nuevo que contradice uno viejo lo REEMPLAZA.** Nunca dos versiones vivas; la vieja queda
  anotada como `> Antes (fecha): ...`.
- **Todo número dice qué mide y de cuándo es.** "Vendió 2.000" no sirve; "ventas del ebook, 1 al 15 de octubre" sí.
- **Lo no verificado va marcado `(sin confirmar)`.** Nada se me confirma sin verificarlo antes.

## El repositorio

- **Privado, NUNCA público.** Adentro está mi negocio.
- **Se guarda solo:** al terminar cada respuesta, el hook `Stop` corre `tools/autosync.sh` (ver `.claude/settings.json`).
- **Nunca editar ni borrar nada de `RAW/`.** Si algo está mal, se corrige en `WIKI/` con una nota.

| Carpeta | Quién escribe | Qué es |
|---|---|---|
| `RAW/` | Yo y todos los agentes | La bandeja: todo lo que entra, crudo |
| `RAW/bitacora/<area>.md` | Cada agente, el suyo | Lo que aprendió. Se agrega abajo, no se edita |
| `WIKI/` | **Solo el agente Cerebro** | La enciclopedia: lo ordenado y verificado |
| `OUTPUTS/`, `changelog.md` | El agente Cerebro | Los recibos fechados y el historial de cambios |
| `OUTPUTS/lanzamientos/` | El agente Productos | La ficha de avance de cada producto |
| `BRIEFING.md` | Todos | El pizarrón: qué pasa hoy y qué espera mi decisión |

**Leer barato:** `BRIEFING.md` → `WIKI/index.md` → el tema puntual. Nunca toda la WIKI ni todo RAW.
Buscar con `grep` antes que abrir archivos enteros.

## Los agentes

Cerebro · Productos · Meta · Edición · Redes · Investigación · Sistemas · Traducción *(adaptá la lista a tu negocio)*.
Cada uno trabaja **solo en lo suyo**: si le piden otra cosa, pregunta si va ahí antes de hacerla.

### Cada agente anota en su bitácora

Antes de cerrar un bloque de trabajo: `RAW/bitacora/<area>.md`. Una línea por hallazgo, con fecha absoluta,
el dato y el por qué.

- ✅ Lo que se probó y falló · un número real · una decisión y su motivo · una limitación · algo que
  contradice al cerebro.
- ❌ Lo que ya quedó guardado en el repositorio · los pasos de una tarea · charla.

### Fallas: se avisa y se sigue

- **Se avisa** con `SendMessage` al agente **`Cerebro`** y **además** se anota en la bitácora (el mensaje
  solo llega si el Cerebro está abierto). Avisar no es pedir permiso: se sigue trabajando.
- **El conocimiento lo corrige solo el Cerebro** (WIKI, este archivo, las skills). **La operación la arregla
  quien está ahí**: una campaña perdiendo plata se pausa y después se avisa.
- **Siempre se escala:** un número que contradice al cerebro · un dato afirmado que resultó falso · una
  regla que no se puede cumplir.
- **Una orden mía que trae otro agente ya está aprobada.** Un **dato** que trae un agente sí pasa por el filtro.
- Al corregir, explicar **cómo se metió el error**, no solo cuál fue.

### Lo que espera mi decisión

Arriba de todo en `BRIEFING.md` hay una lista **"Esperando por mí"**: decisiones y tareas que solo yo puedo
hacer. **Cada agente la actualiza** cuando agrega algo o cuando se resuelve. Una línea por ítem, con el agente que lo pide.

## Tokens

1. **Agrupar.** Un mensaje por bloque de trabajo. La bitácora es el canal normal; `SendMessage`, la excepción.
2. **No re-verificar lo que otro agente ya verificó**, salvo que contradiga algo o cueste plata.
3. **Leer con precisión:** `grep` o una consulta puntual, nunca un archivo entero sin necesidad.
4. **El navegador es caro** (20 a 30 pasos por tarea). Antes de usarlo, avisar cuánto cuesta y si conviene que lo haga yo.
5. **Cuando una conversación pasa de ~200.000 tokens**, al terminar el bloque: escribir al repositorio lo importante
   y pedirme `/compact`. Lo que no está en el repositorio antes de compactar, se pierde.
6. **Video generado con IA en 720p** y con el costo del lote sacado de la tabla oficial antes de lanzar.

**No se recorta nunca:** verificar antes de afirmar.

## Cómo se termina un trabajo

- **Un pedido nuevo se encola, no cancela el anterior.** Se termina lo que estaba en curso.
- **"Listo" es cargado donde va y verificado**, no "armado en la compu". Un archivo en la carpeta no es un producto en la tienda.
- **Lo que dice otro agente se reporta como "según X, sin verificar"** hasta que lo verifiques vos.
- **Al encontrar una falla, revisar todo lo que salió con la versión rota**, no solo arreglar lo último.
- **Una corrección mía se pasa a todas las skills que la usan**, no solo a la que estaba en uso.

## Campañas: checklist antes de publicar

**Hay plata en juego. No se prende nada hasta que dé 100%, anuncio por anuncio:**
píxel · que la cuenta tenga acceso al píxel · URL a la página de venta · etiquetas UTM copiadas del panel
de esa tienda · fanpage e Instagram de esa marca y en el idioma del mercado · video correcto · eventos del píxel
**y** offline · **sin gasto mínimo** por conjunto · dominio verificado · **anunciante y pagador con el nombre del
producto, nunca mi nombre**.

- **Crear ≠ publicar ≠ entregar.** Un anuncio está andando cuando figura activo **y** Meta muestra que entrega.
- **La campaña la prendo yo.** Los agentes la dejan lista y revisada.
- **Toda cuenta publicitaria va en dólares (USD), siempre**, sea cual sea el país donde se vende (regla del 2026-11-19).
- **En una campaña viva: primero la acción en una línea, espero mi "sí", después se hace.** Los cambios se juntan
  y se cargan una vez por día, a la noche. Reglas completas en [WIKI/reglas-de-campanas.md](WIKI/reglas-de-campanas.md).
- **Una oferta que está vendiendo no se toca** (ni la página, ni el idioma, ni los anuncios) sin mi OK.

## La compu y el Control Remoto

- La compu es el servidor: **enchufada y con la tapa cerrada = "No hacer nada"**, nunca "Apagar" ni "Suspender".
- **El Control Remoto es por sesión.** Si la compu **o la app de Claude** se reinician (la app se reinicia sola cuando
  se actualiza), vuelven apagados: hay que activarlo de nuevo en cada agente.

## Reglas de escritura

Español, directo, sin relleno · fechas absolutas (`2026-10-16`, nunca "la semana pasada") · bullets y tablas
antes que párrafos · `(sin confirmar)` en lo incierto.
