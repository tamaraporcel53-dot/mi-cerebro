# Prompts de imágenes — Tu Mascota en Aguja Mágica

> Preparado el 2026-11-19, listo para cuando Higgsfield esté conectado.
> **Método híbrido (decisión de Productos):** el texto ya está en el HTML (exacto, sin errores de IA y seleccionable). Con Higgsfield se generan **solo las ilustraciones** y se insertan en los recuadros del borrador. Son 27 imágenes en vez de 43 páginas enteras (2026-11-19: se sumó I7, los 6 rellenos).
> Costo estimado (sin confirmar): 27 × 2 = 54 créditos, + 15% ≈ **62 créditos**. Menos que el tope de ~97 que vio Tamy.
> Modelo: `nano_banana_pro`, 2K. Confirmar el id, la resolución y el costo con `models_explore` y `get_cost: true`. **Nunca `use_unlim: true`.**
> Paleta: #1A3D6B (azul), #FF8C42 (naranja), #F0F7FF (fondo). Original: no copiar fotos, moldes ni marcas de nadie.

## Cierre fijo de cada prompt

```
No text, no letters, no numbers, no watermark, no logo. Original artwork.
```

(Las ilustraciones van **sin texto**: el texto lo pone el HTML.)

## Ilustraciones del libro (7)

| # | Va en | Formato | Prompt |
|---|---|---|---|
| I1 | Pág. 1, tapa | 3:2 | Bright natural-light photo on a light wooden table: a smartphone showing a photo of a happy mixed-breed dog, next to a finished punch needle portrait of the same dog in a round wooden embroidery hoop, soft yarn loops with visible texture, warm cozy craft mood, colors navy #1A3D6B and orange #FF8C42 accents. |
| I2 | Pág. 4, capítulo 1 | 3:2 | Clean technical side-view diagram of punch needle embroidery: a hollow punch needle entering stretched fabric from the back side, small yarn loops forming on the front side, isolated on light background #F0F7FF, flat vector style, navy and orange. |
| I3 | Pág. 6, capítulo 3 | 3:2 | Two smartphone photos of the same small dog side by side: left sharp, front-facing, daylight, eyes visible; right blurry, dark, dog far away. A green check circle under the left, a red cross circle under the right. Flat clean layout, light background. |
| I4 | Pág. 10, capítulo 6 | 1:1 | Line drawing of a tabby cat face on light fabric with small hand-drawn arrows showing fur direction, from the nose outward and from the forehead to the ears, minimal, navy lines with orange arrows. |
| I5 | Pág. 15, Bono 1 | 3:1 | Four smartphone screens in a row showing the same dog photo: 1 original color photo, 2 cropped to the face, 3 mirrored horizontally, 4 black and white with high contrast. Flat clean mockup on light background #F0F7FF. |
| I6 | Pág. 23, cierre | 3:2 | Cozy living room wall with a framed round punch needle portrait of a black and white cat, the real cat sitting below looking up at it, warm afternoon light, navy and orange accents. |
| I7 | Pág. 9, capítulo 5 (2/2) | 3:1 | Six small square punch needle samples in a row on light fabric, seen from the loop side, each showing a different fill: single outline row, parallel rows, spiral, rows following fur direction, scattered dots of a second color, tall loops trimmed into plush. Same navy and orange yarns, flat top-down photo, light background #F0F7FF. |

## 20 moldes de razas (Bono 2)

Prompt base (cambiar `{RAZA}`), formato 1:1:

```
Simple clean line-art template for punch needle embroidery: front-facing head and chest portrait of a {RAZA}, mirrored, bold continuous outlines, separate closed areas for dark, medium and light fur zones, eyes and nose clearly defined, inside a circle, black lines on pure white, no shading, coloring-book style.
```

| # | {RAZA} |
|---|---|
| M01 | mixed-breed short-haired dog |
| M02 | poodle |
| M03 | labrador retriever |
| M04 | golden retriever |
| M05 | german shepherd |
| M06 | french bulldog |
| M07 | pug |
| M08 | yorkshire terrier |
| M09 | chihuahua |
| M10 | beagle |
| M11 | border collie |
| M12 | dachshund |
| M13 | miniature schnauzer |
| M14 | shih tzu |
| M15 | pitbull terrier |
| M16 | boxer dog |
| M17 | tabby domestic cat |
| M18 | black cat |
| M19 | siamese cat |
| M20 | persian cat |

Cada molde va en su propia página del Bono 2 (20 páginas más en el HTML), con un mapa de colores A/B/C/D al pie.
