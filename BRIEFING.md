# BRIEFING — el pizarrón del día

> Lo primero que lee cualquier agente. Tiene que alcanzar para entender el negocio en 5 minutos.
> Lo mantiene al día el agente Cerebro.

## 🔴 Esperando por mí

> Decisiones y tareas que solo yo puedo hacer. **Cada agente agrega lo suyo y borra lo resuelto.**

| Qué | Lo pide |
|---|---|
| **Bot Escala IU:** decidir si su regla (×2 con 1 venta y ROAS ≥ 2, cada 15 min) reemplaza a la tabla F6 de imperioproducto (+30% con 3 ventas y ROAS > 1,8, a las 23:30) y si aprobás que mueva presupuesto solo. No se construye hasta tener una campaña vendiendo (2026-11-19) | Sistemas |
| **Retrato de mascota:** ~~precio~~ (cerca de AR$ 19.900) y ~~4 bonos~~ aprobados por Tamy el 2026-11-19 (método "de tu foto al dibujo", 20 moldes de razas, materiales en AR, "vendé retratos por encargo"). **Revisar el borrador del ebook** (22 páginas de texto, con recuadros donde van las imágenes): `OUTPUTS/lanzamientos/retrato-mascota-aguja-magica/borrador-tu-mascota-en-aguja-magica.pdf`, y decidir cómo se hacen las imágenes (Higgsfield no está conectado en la sesión de Productos). **Falta decidir el plan para subir lo que gasta cada cliente** (no se arma el día del lanzamiento; va cuando la oferta venda parejo): order bump "50 moldes extra" a ARS 5.900, y 4 OTOs (retratos de familia, alfombras chicas, "vendé por encargo PRO", diseños de temporada). Hay que elegir si la escalera queda en USD 47/27/17/12 o adaptada a pesos (ARS 46.900/26.900/16.900/11.900). Detalle en `OUTPUTS/lanzamientos/retrato-mascota-aguja-magica.md` | Productos |
| **Mirar a mano 3 tiendas de Mercado Libre AR** (unos 2 minutos), para los precios del bono "Dónde comprar": ERMITA CREA (kit con aguja, lanas, bastidor y tela), mercedesherenu (tela panamá) y CANDY CRAFT (aguja de 3 puntas). Mercado Libre y Shein bloquean al navegador del agente con una verificación anti-robots. (Antes, 2026-11-19: el OK para la parte 2 del análisis ya se dio y se usó; resultado en `RAW/cazas.md`, undécima vuelta) | Investigación |
| Crear la **fanpage y el Instagram** de la marca de ebooks (en español) y conectarlos al portfolio comercial. Hoy el portfolio no tiene ninguna página (2026-11-19) | Meta |
| **Para hacer los anuncios en video faltan 3 cosas** (chequeado el 2026-11-19): (1) la carpeta `motor-remotion/` del kit de edición del curso, (2) **pegar las claves** de ElevenLabs, Kie y HeyGen en el `.env` que ya creó el Cerebro en `mi-cerebro/` (hoy están vacías; nunca en el chat) y avisarme, (3) instalar ffmpeg, Node 18+ y Python: se lo pedí a Sistemas el 2026-11-19. También: el nombre de la tienda para la marca de agua | Edición |

## El negocio hoy

- **Qué vendo:** primer ebook elegido por Tamy el 2026-11-19: **retrato de tu mascota en aguja mágica (punch needle) a partir de una foto**, en PDF. **Precio: cerca de AR$ 19.900** (decidido por Tamy el 2026-11-19, al nivel de la competencia de aguja mágica en AR). Neto por venta ≈ USD 11,5 (cálculo de Productos, sin verificar)
  > Antes (2026-11-19): USD 19,90 como precio de todos los ebooks
  - Por qué: afuera es el ángulo principal de HeyHobby (kit físico con el dibujo impreso; anuncio de mascota al aire desde 2026-11-13). En AR no hay ningún ebook de esto: Huella & Alma y Luna Decima venden el bordado ya hecho (servicio). La aguja mágica genérica sí tiene ~8 competidores en AR, a AR$ 18.900-19.900 (vistos el 2026-11-19)
  - El punto a resolver en el producto: pasar la foto a un dibujo y a la tela. Nadie lo resuelve en un PDF (hipótesis: calco a contraluz o una app)
  > Antes (2026-11-19): punch needle genérico, con "0 infoproductos en AR" (error del Cerebro: se buscó solo en inglés). Antes de eso se salió de repostería: ahí la competencia vende a USD 7-10
  > Antes (2026-11-19): pan dulce relleno y chupetines de chocolate (repostería). Chupetines **descartados del todo** por Tamy el 2026-11-19: no se buscan más
- **Dónde vendo:** primero Argentina; después otros países (2026-11-19)
- **Tienda y cobro:** Impultienda. En Argentina se cobra **en pesos con Mercado Pago**. Precio del primer ebook: cerca de AR$ 19.900
- **Cuentas publicitarias:** siempre en **USD** (regla en `CLAUDE.md`)
- **Números de esta semana:** arranque desde cero. Ventas 0, gasto en anuncios 0 (al 2026-11-19)
- **Cuenta de la meta:** USD 1.000 de ganancia por día ÷ ≈ USD 11,5 de neto por venta (AR$ 19.900) = **unas 87 ventas por día como mínimo**, aun si no se gastara nada en anuncios. Con anuncios hacen falta más, o subir el ticket con order bumps y ofertas post-compra (sin confirmar: depende del dólar y del costo por venta)
  > Antes (2026-11-19): 51 ventas por día, calculado con USD 19,90

## En marcha

| Qué | Quién | Estado | Fecha |
|---|---|---|---|
| Ebook **retrato de mascota en aguja mágica**: armar la oferta (contenido, método foto → dibujo → tela, bonos, lista de materiales en AR) | Productos | 20%: oferta aprobada; el borrador de texto del ebook (22 págs., 0 créditos) espera la revisión de Tamy | 2026-11-19 |
| Validar punch needle (caza, competencia, precios) | Investigación | **Hecho** (vueltas 6 a 9 en `RAW/cazas.md`) | 2026-11-19 |
| Ebook de pan dulce relleno | Productos | **Descartado por ahora**: Tamy eligió punch needle (salir de repostería) | 2026-11-19 |

## Próximos pasos

1. ~~Carpeta fija + repositorio privado en GitHub~~ hecho el 2026-11-19: `C:\Users\Tamara\Documents\mi-cerebro` → github.com/tamaraporcel53-dot/mi-cerebro, guardado automático probado (agente **Sistemas**)
2. Validar una oferta con `imperiowhale` (ya instalada el 2026-11-19; caza del 2026-11-19, sexta vuelta en `RAW/cazas.md`: validada en las vueltas 6 a 9; Tamy eligió **retrato de mascota en aguja mágica** el 2026-11-19) ✅ y con el buscador de ofertas propio (agente **Investigación**)
3. Elegir el primer ebook y armar producto, landing y checkout en Impultienda con Mercado Pago en pesos (agente **Productos**)
4. Preparar Meta: ~~cuenta publicitaria en USD~~ lista el 2026-11-19 (termina en 7584, USD, activa, con tarjeta, zona horaria Buenos Aires: verificado en la auditoría del 2026-11-19, 0 campañas y 0 gasto; ⚠️ no tocar "cambiar moneda" ni zona horaria: cierra la cuenta); faltan píxel, fanpage, Instagram y dominio (agente **Meta**)
