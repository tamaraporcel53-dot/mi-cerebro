---
tema: espanol-neutro
actualizado: 2026-10-29
fuentes: pase real de un producto completo a español neutro (octubre 2026)
---

# Español neutro de tú (Latinoamérica)

> **Cuándo:** todo lo que se vende a toda Latinoamérica: video, páginas, ebook, mails y anuncios. El voseo solo si vendés únicamente en Argentina.

Todo lo que se vende a toda Latinoamérica va en **español latino neutro, de tú**, porque se vende
a toda Latinoamérica (AR, UY, CL, PE, PY, CO, MX, PA, CR). Cálido y directo, no de España (nada de "vosotros",
"vale", "ordenador", "coger").

## 1. Verbos

| Vos | Tú | Ojo |
|---|---|---|
| Hacé · Poné · Tené · Salí · Vení · Decí | Haz · Pon · Ten · Sal · Ven · Di | irregulares |
| Cortá · Enrollá · Pasá · Usá · Tomá | Corta · Enrolla · Pasa · Usa · Toma | sacar la tilde |
| Volvé · Contá · Probá · Mové · Apretá · Empezá · Elegí · Pedí · Seguí · Medí · Envolvé · Cerrá | Vuelve · Cuenta · Prueba · Mueve · Aprieta · Empieza · Elige · Pide · Sigue · Mide · Envuelve · Cierra | **cambia la raíz** |
| Abrí · Escribí · Repetí | Abre · Escribe · Repite | |
| Atalo · Pasala · Mandale · Contale · Preguntale · Armame · Fijate · Acordate · Escribile · Guardalo | Átalo · Pásala · Mándale · Cuéntale · Pregúntale · Ármame · Fíjate · Acuérdate · Escríbele · Guárdalo | **con pronombre pegado lleva tilde** |
| tenés · podés · querés · sabés · sos · vas a · hacés · necesitás · llevás · dejás | tienes · puedes · quieres · sabes · eres · vas a · haces · necesitas · llevas · dejas | |
| vos · con vos · para vos · a vos | tú · contigo · para ti · a ti | |
| No cortés · No tirés | No cortes · No tires | negativo = subjuntivo sin tilde |

Revisá cada frase entera: no es buscar y reemplazar. Una frase puede tener 3 verbos de vos.

## 2. Palabras argentinas → neutras

| Argentina | Neutro |
|---|---|
| telgopor | espuma de poliestireno (1.ª vez: "esfera de espuma (poliestireno)"; después "esfera de espuma") |
| living | sala |
| lamparita | bombilla (bombilla LED) |
| plasticola | pegamento blanco |
| cinta scotch | cinta adhesiva |
| trincheta | cúter |
| birome | bolígrafo |
| tanza | hilo de nailon |
| tarugo | taco de pared |
| mecha (de taladro) · agujereadora | broca · taladro |
| zapatilla (eléctrica) · llave de luz | regleta · interruptor |
| velador | lámpara de mesa |
| mesa ratona · placard · heladera | mesa de centro · clóset · refrigerador |
| remera · pollera | camiseta · falda |
| plata | dinero |
| chicos (niños) | niños |
| re lindo · copado · laburo | muy lindo · genial · trabajo |
| pileta | lavabo |

**Nunca** "coger" (usar "tomar" o "agarrar"). "Celular", "cartón", "hilo", "soga", "aro", "cuenta" están bien.

## 3. Lo que NO cambia

- Medidas, cantidades, números, nombres de piezas y de secciones (salvo que tengan voseo o una palabra de la tabla).
- Diseño, colores, tipografías, dibujos.
- El nombre de tu marca.

## 4. Después de cambiar

- Las formas de tú a veces son más largas ("Cuéntale"): mirar cada página re-renderizada y comprobar que ningún
  texto se sale de su caja, se pisa ni queda cortado.
- Buscar restos con grep: `á\b|é\b|í\b` en verbos al final de palabra, `tenés|podés|querés|sos\b|vos\b|fijate|acordate`
  y las palabras de la tabla 2.


## Más palabras argentinas que aparecen seguido

| Argentina | Neutro |
|---|---|
| ficha (eléctrica) · alargue | enchufe · extensión |
| lavarropas · picaporte | lavadora · manija |
| cola vinílica · brochette | pegamento blanco · brocheta |
| hornalla · lavatorio | fuego · lavabo |
| señalador · seña | separador · anticipo |
| «de a poco» | «poco a poco» |

## Cuánto cuesta pasar un producto

- **Texto que pone el código** (ebook armado con código, PDF de OTO, landing, productos): **0 créditos**, se re-renderiza.
- **Texto que la IA escribió dentro de la imagen** (bonos): primero parche por código (PIL); lo que no quede bien se regenera (con IA, unos créditos por página). En un ebook real alcanzó el parche: 18 páginas, 0 créditos.
- Verificar con OCR que no quede voseo.
