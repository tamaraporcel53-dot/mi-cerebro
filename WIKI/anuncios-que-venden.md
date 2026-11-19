---
tema: anuncios-que-venden
actualizado: 2026-10-29
fuentes: aprendizajes de tandas reales de anuncios (octubre 2026)
---

# Anuncios que venden: cómo se arma una tanda de 10

**En una línea:** lo que tiene que tener cada tanda de anuncios para que el testeo testee algo de verdad.

## La tanda: variedad a propósito

Si alguien ve tres anuncios tuyos y parecen el mismo, el testeo no testea nada y quemás la audiencia.

| Qué varía | Mínimo por tanda de 10 |
|---|---|
| Voces | **3 distintas** |
| Músicas | **5 distintas**, una misma en 2 anuncios como máximo |
| Ángulos | uno distinto por anuncio |
| Formatos | mezclar: tutorial, "¿cuál te llevarías?", antes y después, chat de celular, tipográfico, recorrido por ambientes, presentador a cámara, presentador en burbuja abajo a la izquierda, sin cara |
| Gente | al menos un avatar, una persona de lejos haciendo la pieza, una de espaldas, alguien mirando el resultado en una tablet o celular |
| Ganchos | `HOOK-RES` y `HOOK-PROB` (ver [[reglas-de-campanas]]) |

Variá el **formato**, no la identidad: los colores y el estilo de tu marca se mantienen.

## Producto: que se vea el proceso entero

- El producto vende por la transformación. Todo anuncio lleva **una secuencia continua del proceso**
  (de los materiales al resultado) de **4 a 7 segundos**, acelerada, no cortada en planos de 1 segundo que no se leen.
- **Sin zoom.** Toma vertical, tal cual. Toma horizontal, entera sobre su misma imagen desenfocada.
  Si hay una marca a la vista, se difumina la marca; no se recorta el plano hasta que no se entiende.

## Material: primero descargar, después generar

1. Antes de editar, juntá **~100 videos cortos del nicho** (TikTok, Pinterest) en una carpeta, con un
   `_links.txt` que diga de dónde salió cada uno.
2. **Borrales los metadatos:** `ffmpeg -i in.mp4 -map_metadata -1 -map_chapters -1 -c copy out.mp4`.
3. Usá **solo tramos limpios:** sin logos, sin marcas de agua, sin @usuarios, sin subtítulos quemados,
   **sin caras de otros creadores**. Revisá el tramo exacto que usás, no solo el primer cuadro.
4. **Generá con IA solo lo que falte**, en **720p** con la versión estándar del modelo. Antes de lanzar,
   sacá el costo de la tabla oficial y sumá el lote entero. Full HD y versiones Pro queman créditos sin que se note en el celular.

## Texto en pantalla

- **Subtítulos: máximo 3 palabras por bloque, un solo renglón, estilo karaoke** (la palabra se pinta cuando se dice).
- **Marca de agua:** el nombre o dominio de tu tienda, muy suave (opacidad ~0,15-0,2), que aparece en un lugar,
  se desvanece y reaparece en otro. Nunca encima del subtítulo. Si te descargan el video, se llevan tu tienda escrita.
- **Cierre con la landing (a prueba):** en algunos anuncios de cada tanda, el final se parece a la página de venta
  (imagen principal, titular, colores), para que el clic se sienta como continuación. Marcalos con `-LANDING` en el nombre para comparar.

## Nunca

- Mostrar en un anuncio tus productos que ya venden (landings, ebooks, otros anuncios): **es regalarle tu oferta a la competencia.**
- Usar voces o caras de alumnos o clientes sin permiso.
- Decir cuántas técnicas enseña el producto ("una sola técnica" suena a poco). Las piezas o diseños sí se cuentan.
- Entregar un video sin mirarlo entero antes.

## Relacionado

[[reglas-de-campanas]] · [[montaje-de-campanas]]
