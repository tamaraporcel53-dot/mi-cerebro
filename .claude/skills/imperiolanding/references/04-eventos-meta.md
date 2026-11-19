# Eventos de Meta

## Lo más importante de todo este archivo

**Nunca llames a `fbq('track', ...)` directo desde el Custom HTML.**

Impultienda dispara cada evento **dos veces a propósito**: una desde el navegador (pixel) y otra desde el servidor (API de Conversiones), las dos con el **mismo `event_id`**. Meta las une y cuenta una sola conversión, pero con muchísimo mejor atribución.

Un `fbq('track','Purchase')` tuyo va **sin `event_id`**, así que Meta no lo puede unir con nada y lo cuenta como una conversión extra. Resultado: métricas infladas, ROAS falso, y el algoritmo optimizando contra datos mentirosos.

La propia plataforma desactiva la detección automática de Meta por esta razón:

```js
fbq('set', 'autoConfig', false, pixelId);   // lo hace Impultienda, no lo toques
fbq('init', pixelId);
```

---

## Las funciones que sí tenés que usar

Impultienda expone dos globales en la tienda publicada:

```js
window.metaTrack(nombreEvento, parametros, datosUsuario)
window.metaTrackInitiateCheckout(parametros)
```

`metaTrack` hace las dos cosas: el `fbq('track', ..., {eventID})` y el POST a la función de CAPI, con el mismo id. Es lo único que hay que llamar.

`metaTrackInitiateCheckout` además trae un anti-duplicado de 15 segundos guardado en `sessionStorage`, para que un doble click no cuente dos veces.

---

## Qué dispara cada quién

| Evento | Quién | Dónde |
|---|---|---|
| **PageView** | Impultienda, solo | Todas las páginas |
| **ViewContent** | **Vos**, en tu script | Landing, al cargar |
| **AddToCart** | Impultienda | Si el flujo lo usa |
| **InitiateCheckout** | Impultienda al cargar `/checkout`, y **vos** al click | Los dos, deduplicados |
| **Purchase** | Impultienda | Página de gracias |

Vos agregás **ViewContent** y el **InitiateCheckout al click**. Nada más.

Sobre el InitiateCheckout al click: `/checkout` ya lo dispara al cargar, así que técnicamente es redundante. Vale la pena igual, porque se dispara **antes** de navegar: si el comprador cierra o la página de checkout no carga, el evento igual llegó. El throttle de 15s evita el doble conteo.

---

## El código

Ya está en la plantilla. Lo importante de cada parte:

```js
/* metaTrack puede no existir todavía cuando corre tu script. Esperala. */
function ready(fn){
  if (typeof window.metaTrack === "function") return fn();
  var n = 0, t = setInterval(function(){
    n++;
    if (typeof window.metaTrack === "function") { clearInterval(t); fn(); }
    else if (n > 60) { clearInterval(t); }     // se rinde a los 9s
  }, 150);
}
ready(function(){ try { window.metaTrack("ViewContent", pd()); } catch(e){} });

/* Todos los botones de compra, sin importar cuántos haya */
document.querySelectorAll('a[href="/checkout"],[data-checkout]').forEach(function(a){
  a.addEventListener("click", function(){
    try {
      if (typeof window.metaTrackInitiateCheckout === "function") {
        window.metaTrackInitiateCheckout(pd());
      }
    } catch(e){}
  });
});
```

### El valor y la moneda

En Custom HTML **no existe** el input oculto `#main-price` que usan las plantillas por defecto, así que hay que sacar el precio de la pantalla. La moneda sí está en `#store-currency`.

```js
function pv2(){
  var e = document.querySelector(".flonow");   // el precio de la barra flotante
  if (!e) return 0;
  var s = e.textContent.replace(/[^0-9.,]/g, "");
  if (s.indexOf(",") > -1) {                   // 22.522,50 → 22522.50
    s = s.replace(/\./g, "").replace(",", ".");
  } else {                                     // 22.522 → 22522
    var p = s.split(".");
    if (p.length > 1 && p[p.length-1].length === 3) s = s.replace(/\./g, "");
  }
  return parseFloat(s) || 0;
}
function cur(){
  var c = document.getElementById("store-currency");
  return c && c.value ? c.value : "ARS";
}
```

Cubre los dos formatos (es-AR y en-US). Si el elemento del que leés cambia de clase, esto devuelve 0 en silencio — por eso hay que probarlo.

### dataLayer

Empujá también a `window.dataLayer` con los mismos nombres. No molesta, y si el usuario suma Google Tag Manager después ya está listo.

---

## Cómo probar que funciona de verdad

### 1. ¿Existen las funciones?

```js
typeof window.metaTrack;                    // "function"
typeof window.metaTrackInitiateCheckout;    // "function"
```

Si dicen `undefined`, el pixel no está configurado en `Configuraciones → Meta / Tracking`.

### 2. ¿InitiateCheckout se dispara con el payload correcto?

Interceptá la función y simulá el click **sin navegar**:

```js
let cap = null;
const orig = window.metaTrackInitiateCheckout;
window.metaTrackInitiateCheckout = function(p){ cap = p; return orig.apply(this, arguments); };

const blk = e => e.preventDefault();          // solo preventDefault
document.addEventListener('click', blk, true);
document.querySelector('a[href="/checkout"]')
        .dispatchEvent(new MouseEvent('click', {bubbles:true, cancelable:true}));
await new Promise(r => setTimeout(r, 400));
document.removeEventListener('click', blk, true);
window.metaTrackInitiateCheckout = orig;

cap;  // { value: 22453, currency: "ARS", content_name: "...", num_items: 1 }
```

⚠️ **No uses `stopImmediatePropagation` en el bloqueador.** Corre en fase de captura, antes que el listener del botón, y le impide ejecutarse: vas a creer que el evento no funciona cuando en realidad lo estás matando vos.

### 3. ¿Llegan a Meta?

Mirá la red buscando `meta-track-event`. Los POST salen por `navigator.sendBeacon`, así que el estado que reporta el navegador puede ser engañoso. Para saber si el endpoint está vivo:

```js
await fetch('https://<proyecto>.supabase.co/functions/v1/meta-track-event', {method:'GET'})
  .then(r => r.status);   // 500 = la función existe y corrió (falta el body). 404 = no existe.
```

**No mandes un POST de prueba**: le metés un evento falso a los datos del usuario.

La comprobación buena es del lado de Meta: en el dataset del pixel, `last_fired_time` (navegador) y `server_last_fired_time` (CAPI) tienen que ser recientes.

### 4. Si en tu navegador no anda

Muy común: **una extensión bloquea el pixel**. Los síntomas son claros:

```js
window.fbq.queue.length;   // > 0 = eventos encolados que nunca salieron
performance.getEntriesByType('resource')
  .filter(r => r.name.includes('fbevents'))
  .map(r => r.transferSize);   // [0] = el script nunca cargó
```

`fbq` existe igual porque el snippet crea un stub antes de cargar la librería. Que exista no quiere decir que funcione.

**Esto no afecta a los compradores.** Probá en incógnito sin extensiones, o desde el celular. Decíselo al usuario para que no se vuelva loco con el Pixel Helper.

---

## Calidad de coincidencia (EMQ)

En el dataset vas a ver un puntaje de 0 a 10 por evento.

**PageView típicamente da 5-6 y está bien**: solo lleva IP, user-agent, `fbp` y `fbc`. No hay mail ni teléfono porque el visitante todavía no dio nada.

El que importa es **Purchase**, que sí lleva los datos del checkout. Para subirlo, en `Configuraciones → Pagos → Campos del formulario`:

- **Teléfono**: +44%
- **Apellido**: +25%

Los dos activados es lo mejor que se puede hacer por la atribución. Recomendáselo siempre.

Si el pixel es nuevo, las estadísticas agregadas pueden venir vacías por un día aunque los eventos estén llegando. Fijate en `last_fired_time` en vez de en el volumen.
