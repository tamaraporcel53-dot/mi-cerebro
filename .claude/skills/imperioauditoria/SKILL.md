---
name: imperioauditoria
description: Audita cuentas publicitarias y tiendas enteras en SOLO LECTURA y trae únicamente los errores, ordenados por lo que cuesta plata — anuncios en borrador, campañas activas que no gastan por la tarjeta, píxel equivocado, UTMs mal puestas, miniatura recortada, Instagram de otra marca, videos truncados y landings rotas. Usar cuando el usuario diga "imperioauditoria", "chequeá todo", "fijate si hay errores", "revisá las campañas", "está todo bien?", "auditá la cuenta", "chequeo completo", o cuando pregunte si algo quedó bien cargado.
---

# ImperioAuditoria — encontrar los errores antes que los encuentre la plata

**Esta skill no arregla nada. Encuentra.** Sale a buscar lo que está mal, lo trae
ordenado por lo que cuesta, y propone. Vos decidís.

Existe porque los errores caros de este negocio **no se ven**: una campaña con los
anuncios en borrador figura ACTIVE y gasta cero sin avisar. Un anuncio con el
Instagram de otra marca entrega igual. Una miniatura de 160×200 pasa desapercibida
días.

---

## 🔴 REGLA 0 — SOLO LECTURA. Sin excepción.

**No se crea, no se modifica, no se pausa, no se activa, no se cambia un presupuesto
ni un precio.** Ni siquiera para "arreglar algo obvio".

Una auditoría que toca deja de ser auditoría: si rompe, nadie sabe si estaba roto
antes. **Se encuentra, se reporta, se propone, y se espera el DALE.**

## 🔴 REGLA 1 — No se afirma nada que no se haya leído

Prohibido escribir "está todo bien" por no haber encontrado el dato. Si algo no se
pudo verificar, va en la tabla como **🟡 no verificable**, con el motivo.

> **El error típico:** reportar campañas como activas mirando sólo campaña y conjunto,
> con todos los anuncios en borrador. **No poder listar los anuncios no significa que
> estén bien: significa que no se verificó.**

## 🔴 REGLA 2 — Dos fuentes para lo que importa

El MCP y el Administrador **no muestran lo mismo**. `validation_status: VALIDATED` y
`active_errors: []` son chequeos **previos**; los que deciden corren después, en el
publicador de Meta, y al MCP no le llegan.

**Todo hallazgo de entrega se confirma en el navegador** antes de reportarlo.

---

# FASE 1 — Definir el alcance y relevar

Si no dijiste qué auditar, el alcance por defecto es **todo lo que está gastando**.

| Qué | Con qué |
|---|---|
| Cuentas y su estado | `ads_get_ad_accounts` → `is_ads_mcp_enabled`, `has_payment_method` |
| Campañas con gasto | `ads_get_ad_entities` level=campaign, `fields: ['name','status','spend','impressions']` |
| Conjuntos | level=adset → presupuesto, `promoted_object`, gasto mínimo |
| **Anuncios, uno por uno** | level=ad, **leyendo cada id** |
| Creativos | `ads_get_creatives` |
| Píxeles de la cuenta | `ads_get_datasets` con `ad_account_id` |
| Tiendas y productos | `impultienda_listar_tiendas`, `impultienda_listar_productos` |

⚠️ **Pedir siempre los `fields`.** Sin eso `ads_get_ad_entities` devuelve sólo nombre
e id, y una auditoría sobre nombres no es una auditoría.

⚠️ **El preset "últimos 30 días" del Administrador no incluye hoy.** Una campaña que
arrancó hoy aparece en 0. Para el día en curso se pide *Hoy* explícito.

### Cuando hay muchas campañas, en paralelo

Con **más de 3 campañas**, lanzar **un agente por campaña** con el mismo checklist y
juntar los hallazgos. Cada agente en solo lectura. Es la diferencia entre media hora
y una tarde.

---

# FASE 2 — Los 10 puntos, anuncio por anuncio

Los mismos que exige [[montaje-de-campanas]], pero mirando lo que ya está cargado:

| # | Qué se mira | Síntoma de que está mal |
|---|---|---|
| 1 | `promoted_object.pixel_id` del conjunto | El píxel es de otra tienda |
| 2 | `ads_get_datasets` con `ad_account_id` | 🔴 El píxel **no figura**: la cuenta no tiene acceso |
| 3 | `call_to_action.value.link` | Apunta a otro dominio, o a una landing caída |
| 4 | `url_tags` del creativo | Vacío, o 🔴 **las UTMs colgando del link** (`%7B%7B`) |
| 5 | `object_story_spec.page_id` (o el de `effective_object_story_id`) | Fanpage de otra marca, o **en otro idioma que el del mercado** (por ejemplo, una campaña para un mercado nuevo que sale con la página del idioma original) |
| 6 | Vista previa de Reels | 🔴 **Instagram de otra marca** o de otro idioma |
| 7 | `video_data.video_id` y su duración | Video repetido, o **truncado** |
| 8 | `tracking_specs` | Falta, o usa `offline_conversion` en vez de `offsite_conversion` |
| 9 | `daily_min_spend_target` del **conjunto** | **Un gasto mínimo CARGADO.** No va: los mínimos se suman y los testeos siguientes quedan sin presupuesto libre |
| 10 | `conversion_domain` | Vacío o de otra tienda |

---

# FASE 3 — Los asesinos silenciosos

Esto es lo que diferencia esta skill de mirar el panel. **Buscar siempre, aunque
nadie los mencione:**

| # | El asesino | Cómo se detecta | Qué cuesta |
|---|---|---|---|
| 1 | 🔴 **Anuncios en borrador** | Campaña ACTIVE con **0 impresiones**. Confirmar en la columna Entrega | El día entero |
| 1b | 🔴 **Anuncio rechazado** | `effective_status` `DISAPPROVED`/`WITH_ISSUES` anuncio por anuncio (`status` puede decir ACTIVE). Motivo en Calidad de la cuenta | Le pega a **toda la cuenta**, y puede pasar días sin que nadie lo vea |
| 2 | **Miniatura recortada** | `image_url` ausente, o el `picture` de 160×200 | Un cuadradito en un 9:16 |
| 3 | **Botón `LEARN_MORE`** | Debe ser `DOWNLOAD` | Dice lo que no pasa |
| 4 | **Descripción vacía** | `link_description` sin texto | Pierde emplazamientos |
| 5 | **`degrees_of_freedom_spec` presente** | En el creativo | Meta le toca el video |
| 6 | **Advantage+ de creativo prendido** | A nivel conjunto | Filtros y música encima del video |
| 7 | **Videos repetidos** | Dos anuncios con el mismo `video_id` | Se compite contra uno mismo |
| 8 | **Anuncios de otra marca** en la campaña | Cotejar nombre contra el producto | Anuncios de un producto gastando en la campaña de otro |
| 9 | **Cuenta sin medio de pago** | `has_payment_method: false` | ACTIVE pero no puede gastar |
| 10 | **Campaña vieja sin apagar** | Dos campañas del mismo producto activas | Gasto duplicado |
| 11 | 🔴 **Pago frenado en la cuenta** | Campaña ACTIVE, `delivery: active`, sin errores y **gasto de HOY = 0** (`date_preset: today`). La API no lo ve: abrir **Facturación** de esa cuenta en el navegador (`business.facebook.com/latest/billing_hub/accounts/details/?asset_id=[ID_DE_TU_CUENTA]`) y buscar el aviso *"Tus anuncios no se están entregando"* o *"Se requiere la verificación de la tarjeta"* | Días enteros sin gastar en fase de aprendizaje |

> ⚠️ **Se mira el gasto de HOY, no el de ayer.** Una campaña que arrancó hoy tiene ayer en 0
> y está bien. En las primeras horas del día de la cuenta, un gasto bajo es normal: el 0 con
> varias horas corridas es lo que se reporta. **Nunca decir "está prendida" por el estado
> ACTIVE: solo con gasto de hoy > 0.**

### Del lado de la tienda

| Qué | Con qué | Síntoma |
|---|---|---|
| El precio real publicado | `impultienda_listar_productos` | No coincide con el que se usó para el presupuesto |
| Pasarela conectada | `impultienda_estado_pasarela` | Anuncios corriendo a un checkout que no cobra |
| Entregable cargado | `impultienda_ver_recursos` | Se vende algo que no se entrega |
| Embudo post-compra | `impultienda_ver_postcompra` | `funnels: []` — se deja plata en la mesa |
| Ebooks de upsells | `impultienda_estado_generacion` | `pending`: el upsell vende un PDF que no existe |
| 🔴 **Idioma mezclado** | `impultienda_ver_landing` | Media tienda en otro idioma. La tienda entera tiene que estar en el idioma del mercado |

---

# FASE 4 — El informe

Sólo lo que está mal. **Nada de "todo lo demás está perfecto" en párrafos.**

### Primero, una línea de resultado

```
🔴 <n> errores que cuestan plata · 🟠 <n> para arreglar · 🟡 <n> sin verificar
```

Si no hay nada: **`✅ Nada roto.`** y la lista de lo que se revisó, en una línea.

### Después, la tabla, ordenada por lo que cuesta

| Prioridad | Qué | Dónde | Qué pasa si no se toca | Cómo se arregla |
|---|---|---|---|---|
| 🔴 | lo que hace perder plata hoy | campaña / anuncio / tienda | el costo concreto | API o navegador |
| 🟠 | lo que rinde menos de lo que podría | | | |
| 🟡 | lo que no se pudo verificar | | **por qué** no se pudo | |

**Cada fila lleva el id.** Un hallazgo sin id no se puede arreglar.

### Y al final, qué se propone

Una lista de acciones concretas, con este formato:

```
¿Lo arreglo? <qué> en <dónde>. <qué cambia>. Respondeme DALE o NO.
```

🔴 **Nada se ejecuta hasta el DALE.** Si decís que sí, ahí recién se toca —
y lo que se toque se vuelve a verificar con los dos controles.

---

## Qué NO es un error

Para no hacerte perder tiempo con falsas alarmas:

| Parece error | No lo es |
|---|---|
| **#1870194 `location_types`** | Meta reescribe el campo sola en cada update. No frena la entrega |
| `ads_get_ig_accounts` devuelve vacío | 🔴 **No lista las cuentas respaldadas por página.** El Instagram se mide por entrega o por la vista previa, nunca por esa lista |
| El botón dice "Más información" en español | Sólo si el valor es `LEARN_MORE`. Si es `DOWNLOAD`, Meta lo traduce solo |
| Gasto en 0 en "últimos 30 días" | Ese preset termina ayer. Pedir *Hoy* |
| Una cuenta sin datos por MCP | `is_ads_mcp_enabled: false`. **Es punto ciego, no un error.** Decirlo siempre |

> **Falsa alarma típica:** diagnosticar "Instagram no va a andar" leyendo
> `ads_get_ig_accounts`. Puede estar andando perfecto, y por esa lectura se termina
> vinculando una cuenta sin necesidad o borrando anuncios buenos.
> **Se mide por entrega, no por esa lista.**

---

## Al terminar

1. Si aparecieron errores nuevos que se repiten, anotarlos en `RAW/bitacora/meta.md`
   para que el agente Cerebro los sume a [[montaje-de-campanas]] y la próxima no vuelvan a pasar
2. Anotar la auditoría en la misma bitácora (el Cerebro la pasa al `changelog.md`)
3. Si hay un hallazgo que tenés que resolver vos a mano (un permiso de píxel, un
   dominio sin verificar), **decírtelo con el paso exacto**, no con el síntoma, y sumarlo
   a "Esperando por mí" en `BRIEFING.md`
