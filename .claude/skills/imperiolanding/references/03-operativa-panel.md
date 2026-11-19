# Operativa del panel de Impultienda

El usuario tiene su sesión abierta en Chrome. Vos trabajás ahí con las herramientas de navegador.

**El dominio es `impultienda.ar`** (no `.com`). La tienda publicada vive en `https://<slug>.impultienda.ar/`.

Sacá el `<slug>` de la URL del panel: `impultienda.ar/dashboard/<slug>/...`

⚠️ **Una cuenta puede tener varias tiendas, y cada una tiene su propio `<slug>`.** El slug sale de la tienda que el usuario confirmó en el Paso 0.A, no de la que estaba abierta.

**Hay DOS selectores de tienda, y son independientes:**

1. El de la **barra lateral**, arriba a la izquierda. Muestra nombre + dominio y cambia la URL.
2. Un **`<select>` arriba a la derecha de "Diseño de tienda", pegado al botón Guardar.** Este es el peligroso: está a centímetros de Guardar y **puede no cambiar la URL**. Mirar el slug de la URL no alcanza para detectarlo.

**Antes de cada guardado, verificá el select por ID, no por nombre ni por URL:**

```js
const s = document.querySelector('select');
({ id:     s.options[s.selectedIndex].value,          // compará CONTRA ESTO
   nombre: s.options[s.selectedIndex].textContent.trim(),
   slug:   location.pathname.split('/')[2] })
```

**El nombre no sirve como identificador.** El alumno puede renombrar la tienda a mitad del trabajo (de "Libro Digital 7 - RP" a "Libro Digital RP", por ejemplo) y tu guarda de seguridad te aborta el guardado creyendo que estás en otra tienda. El **ID** (un UUID) y el **slug** de la URL no cambian nunca. Anotá el ID en el paso 0.A y usá ese.

Si no coincide, **no guardes**: estás por pisar la landing de otro producto que quizá ya está vendiendo, y no hay deshacer.

---

## Rutas

| Pantalla | URL |
|---|---|
| Estilo y modo de diseño | `/dashboard/<slug>/personalizacion/diseno/estilo` |
| **Custom HTML** | `/dashboard/<slug>/personalizacion/diseno` |
| Recursos (imágenes) | `/dashboard/<slug>/personalizacion/diseno/recursos` |
| Ebooks (producto, bonos, upsells) | `/dashboard/<slug>/personalizacion/ebooks` |
| Configuraciones (pagos, Meta) | `/dashboard/<slug>/configuracion` |
| Tienda publicada | `https://<slug>.impultienda.ar/` |

El panel es una SPA: después de navegar **esperá 6-9 segundos** antes de leer el DOM. Si leés antes, la página está vacía y vas a creer que la ruta no existe.

Algunos ítems del menú son `<button>` sin `href`. Si `navigate` te deja en blanco, volvé a una ruta conocida y clickeá el botón del menú.

---

## Activar Custom HTML

En `.../diseno/estilo` hay cinco estilos: Clásico, Neo-Brutalism, Organic, Retro/Y2K y **Custom HTML**. Elegí Custom HTML: reemplaza todas las secciones y el checkout queda igual.

**Decile al usuario qué pierde antes de cambiar**: con Custom HTML deja de existir el editor visual de secciones. Para tocar la landing va a necesitar volver a pedírtelo. A cambio, la página queda exactamente como la quiere. Casi siempre vale la pena, pero que lo sepa.

La "Paleta de colores" de esa pantalla ya **no afecta la landing** (el CSS va adentro del Custom HTML), pero **sí afecta el checkout**. Si la paleta quedó en un color que no tiene nada que ver con la landing, el comprador ve un salto raro al pagar. Avisale — es un cambio de configuración, así que no lo toques sin que te lo pida.

---

## Respaldá lo que ya está, antes de tocar nada

**La primera vez que abrís el textarea de Custom HTML de una tienda, guardá lo que hay.** Si el alumno ya tenía una landing armada, tu primer guardado la borra y no hay historial ni deshacer.

```js
document.querySelector('textarea').value.length   // 0 = está vacío, no hay nada que perder
```

Si tiene contenido, copialo a un archivo (`landing-anterior-<slug>.html`) **antes** de escribir encima, y decíselo:

> Tu tienda ya tenía una landing cargada. Te guardé una copia en `landing-anterior-fitness.html` por si querés volver.

Si el textarea está vacío o la tienda está en otro estilo (Clásico, Neo-Brutalism…), no hay nada que respaldar y seguís derecho.

---

## Si el alumno tiene un emulador de móvil, el PANEL también queda adentro de un iframe

Está documentado más abajo para la tienda publicada, pero pasa igual en el panel: `document.querySelector('textarea')` devuelve `null` y parece que la página no cargó.

```js
const f = document.querySelector('iframe');
const D = f && f.contentDocument ? f.contentDocument : document;
const W = f && f.contentDocument ? f.contentWindow : window;   // ojo con esto
```

⚠️ **Dos trampas acá:**

1. `f.contentDocument` es `null` si el iframe es de otro origen, pero **`f.contentWindow` no**: devuelve un objeto al que no podés acceder. Si sacás el `window` del iframe sin chequear `contentDocument`, el setter nativo del textarea explota con `SecurityError: Blocked a frame with origin ... from accessing a cross-origin frame`. Resolvé los dos juntos, como arriba.
2. La pantalla de **Contenido** trae un iframe con la vista previa de la tienda publicada, que **sí** es de otro origen. Ahí el textarea está en el documento de arriba, no en el iframe.

El SPA puede tardar. Si el textarea no aparece, esperá en bucle antes de darlo por perdido:

```js
const d = document.querySelector('iframe')?.contentDocument || document;
let n = 0;
while (n < 40 && d.querySelectorAll('textarea').length === 0) {
  await new Promise(r => setTimeout(r, 500)); n++;
}
```

## Escribir el HTML

La página tiene **un solo `<textarea>`**: "HTML completo de la tienda".

Es un textarea de React: asignarle `.value` directo **no dispara el estado** y el botón Guardar guarda lo viejo. Hay que usar el setter nativo y disparar el evento:

```js
const t = document.querySelector('textarea');
const setter = Object.getOwnPropertyDescriptor(
  window.HTMLTextAreaElement.prototype, 'value'
).set;
setter.call(t, nuevoHTML);
t.dispatchEvent(new Event('input', { bubbles: true }));
```

Después, el botón Guardar:

```js
const b = [...document.querySelectorAll('button')].filter(x => /guardar/i.test(x.textContent||''));
b[b.length-1].click();
```

Esperá ~5 segundos y confirmá que `document.querySelector('textarea').value.length` coincide con lo que mandaste.

### Ediciones parciales

Para cambios chicos, leé el valor actual, hacé el reemplazo y volvé a escribir. **Siempre verificá que el texto que buscás existe antes de reemplazar** — si no, vas a "guardar" sin cambios y creer que funcionó:

```js
const t = document.querySelector('textarea');
let v = t.value;
if (v.indexOf(BUSCADO) < 0) { 'NO ENCONTRADO'; }
else { v = v.split(BUSCADO).join(REEMPLAZO); /* ... guardar ... */ }
```

### Antes de guardar, validá la estructura

```js
const o = (v.match(/<div\b/g)||[]).length, c = (v.match(/<\/div>/g)||[]).length;
const d = document.createElement('div');
d.innerHTML = v.replace(/<script[\s\S]*?<\/script>/g, '');
({ divs: o + '/' + c, cards: d.querySelectorAll('.card').length,
   checkout: d.querySelectorAll('a[href="/checkout"]').length });
```

Si los `<div>` no cierran parejo, no guardes.

### Leer un HTML largo

La salida de las herramientas se corta en ~1100 caracteres. Para leer un HTML de 50k, poné un helper en la página y pedí varios tramos **en un solo batch** (6 por llamada):

```js
window.S = (a,b) => document.querySelector('textarea').value.slice(a,b);
```

Si un tramo vuelve `[BLOCKED]`, es el filtro de contenido reaccionando a URLs o querystrings. Sanitizá la salida:

```js
window.S(0,1000).replace(/&/g,'AMP').replace(/=/g,'EQ').replace(/https?:\/\/[^\s'"]+/g,'URL')
```

---

## Subir imágenes a Recursos

En `.../diseno/recursos`. **No clickees el botón de subir**: abre el diálogo nativo del sistema, que no podés manejar. Buscá el `<input type="file">` y subí directo por ahí.

Se pueden subir varias de una. Después de subir, esperá 8-12 segundos y sacá las URLs del DOM:

```js
[...document.querySelectorAll('img')]
  .map(i => i.getAttribute('src') || '')
  .filter(s => /mi-archivo\.webp/.test(s))
```

La plataforma le antepone un timestamp al nombre: `<timestamp>_res-auto.webp`. **Usá la URL que devuelve el panel, no la armes a mano.**

Optimizá antes de subir: WebP, calidad 80-86, y el ancho justo que se necesita (900px alcanza para cualquier tarjeta; 1000px para la creativa).

---

## Portadas de los ebooks

Las portadas que ya cargó el usuario en Diseño de ebooks se pueden usar directo en la landing. Están en otro bucket (`ebook-images/` en vez de `store-resources/`).

Sacalas de `.../personalizacion/ebooks` y mapeá cada una a su ebook por el texto que tiene al lado:

```js
[...document.querySelectorAll('img')]
  .filter(i => i.src.indexOf('supabase') > -1)
  .map(i => {
    let p = i, t = '';
    for (let n = 0; n < 7 && p; n++) {
      p = p.parentElement;
      if (p) { const s = (p.innerText||'').replace(/\n/g,' | ').trim(); if (s.length > 10) { t = s.slice(0,90); break; } }
    }
    return i.src.split('/').pop() + ' >> ' + t;
  });
```

**El orden importa:** primero los bonos, después los upsells/downsells. Contrastá con el contador que muestra la pantalla ("Bonos 3", "Agregar bono (3/5)") para no meter un upsell como si fuera un bono.

Ventaja de usar estas URLs: si el usuario cambia una portada en el panel, cambia sola en la landing.

⚠️ **Pesalas antes de usarlas.** Las portadas que genera el panel pueden venir en PNG de **2 MB**, y la del producto principal se usa dos veces: en la tarjeta del combo y en la **miniatura de la barra flotante**, que se ve apenas entrás. Dos megas ahí te arruinan la primera pantalla.

```bash
curl -s -o /dev/null -w "%{size_download}\n" "URL-de-la-portada"
```

Si pasa de ~150KB, bajala, redimensionala a 480×640 WebP calidad 86 (queda en ~50KB) y subila a Recursos. **Perdés la actualización automática**, así que decíselo: si cambia la portada en el panel, te tiene que avisar.

⚠️ **Y fijate la extensión.** Cuando el alumno reemplaza el ebook, la portada nueva puede cambiar de `.webp` a `.png` (o al revés) y **la vieja sigue existiendo en el bucket**: la landing no se rompe, simplemente sigue mostrando la portada del ebook anterior sin que nadie lo note. Si cambió el producto, volvé a leer la URL del panel.

---

## Verificar en la tienda publicada

La tienda **cachea la respuesta ~30 segundos**. Después de guardar:

1. Esperá 10 segundos.
2. Cargá con un parámetro nuevo: `https://<slug>.impultienda.ar/?v=2` (cambialo cada vez).
3. Si seguís viendo lo viejo, esperá otros 10 y repetí. **No vuelvas a editar.**

Editar sobre una lectura cacheada pisa cambios buenos. Si algo "no se guardó", casi siempre es esto.

Confirmá que estás mirando la versión nueva chequeando algo que acabás de agregar:
```js
document.documentElement.innerHTML.indexOf('algo-nuevo') > -1
```

### Si el usuario tiene un emulador de móvil

Algunos usuarios tienen extensiones que muestran la página dentro de un marco de iPhone. En ese caso la landing vive en un `<iframe>` y `document.querySelector` en el documento de arriba no encuentra nada.

```js
const d = document.querySelector('iframe')?.contentDocument || document;
```

Para inspeccionar cómodo podés agrandar el iframe temporalmente:
```js
const f = document.querySelector('iframe');
f.style.cssText = 'position:fixed;left:0;top:0;width:100vw;height:100vh;z-index:999999999;border:0';
// ... mirar ...
f.style.cssText = '';   // ¡devolvelo como estaba!
```

---

## Diagnóstico de tienda

En `.../personalizacion/ebooks` (abajo) hay un botón **"Diagnosticar mi tienda"**: más de 20 chequeos automáticos, y no cambia nada. Corrélo antes de dar por terminado y pasale al usuario lo que encuentre.
