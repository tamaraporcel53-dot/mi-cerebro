# Script de Ensamble PDF y Checklist Final

## SCRIPT PYTHON COMPLETO — ENSAMBLAR EBOOK

```python
#!/usr/bin/env python3
"""
Ensamblador de Ebook desde imágenes Higgsfield
Uso: python3 ensamblar_ebook.py --carpeta ./imagenes --salida ebook_final.pdf
"""

import os
import sys
import argparse
import io
from pathlib import Path

def ensamblar_ebook(carpeta: str, salida: str, dpi: int = 150):
    """
    Ensambla todas las imágenes de una carpeta en un PDF.
    Las imágenes se ordenan alfabéticamente — nombrarlas p01, p02, etc.
    """
    try:
        from PIL import Image
        from pypdf import PdfWriter, PdfReader
    except ImportError:
        print("Instalando dependencias...")
        os.system("pip install Pillow pypdf --break-system-packages -q")
        from PIL import Image
        from pypdf import PdfWriter, PdfReader

    # Extensiones válidas
    extensiones = {'.jpg', '.jpeg', '.png', '.webp'}
    
    # Obtener lista de imágenes ordenadas
    carpeta_path = Path(carpeta)
    imagenes = sorted([
        f for f in carpeta_path.iterdir()
        if f.suffix.lower() in extensiones
    ])
    
    if not imagenes:
        print(f"ERROR: No se encontraron imágenes en {carpeta}")
        return False
    
    print(f"Encontradas {len(imagenes)} imágenes. Ensamblando...")
    
    writer = PdfWriter()
    
    for i, img_path in enumerate(imagenes):
        print(f"  [{i+1}/{len(imagenes)}] {img_path.name}")
        
        try:
            img = Image.open(img_path).convert("RGB")
            buf = io.BytesIO()
            img.save(buf, format="PDF", resolution=dpi)
            buf.seek(0)
            reader = PdfReader(buf)
            writer.add_page(reader.pages[0])
        except Exception as e:
            print(f"  SKIP: Error procesando {img_path.name}: {e}")
            continue
    
    # Metadatos
    writer.add_metadata({
        "/Creator": "Higgsfield",
        "/Producer": "imperioebook",
    })
    
    with open(salida, "wb") as f:
        writer.write(f)
    
    size_mb = os.path.getsize(salida) / 1024 / 1024
    print(f"\n✅ PDF listo: {salida}")
    print(f"   Páginas: {len(imagenes)}")
    print(f"   Tamaño: {size_mb:.1f} MB")
    return True


def reemplazar_foto(pdf_base: str, pagina: int, foto: str, salida: str):
    """
    Reemplaza el placeholder de foto en una página específica del PDF.
    Útil para actualizar fotos sin regenerar todo el ebook.
    
    pagina: número de página (1-indexed)
    foto: ruta a la imagen nueva
    """
    from PIL import Image
    from pypdf import PdfWriter, PdfReader
    import io
    
    reader = PdfReader(pdf_base)
    writer = PdfWriter()
    
    for i, page in enumerate(reader.pages):
        if i + 1 == pagina:
            # Esta página se reemplaza con la foto nueva
            img = Image.open(foto).convert("RGB")
            buf = io.BytesIO()
            img.save(buf, format="PDF", resolution=150)
            buf.seek(0)
            new_reader = PdfReader(buf)
            writer.add_page(new_reader.pages[0])
        else:
            writer.add_page(page)
    
    with open(salida, "wb") as f:
        writer.write(f)
    print(f"✅ Página {pagina} reemplazada en {salida}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ensamblador de ebook desde imágenes Higgsfield")
    parser.add_argument("--carpeta", required=True, help="Carpeta con las imágenes")
    parser.add_argument("--salida", default="ebook_final.pdf", help="Nombre del PDF de salida")
    parser.add_argument("--dpi", default=150, type=int, help="Resolución del PDF (default: 150)")
    
    args = parser.parse_args()
    ensamblar_ebook(args.carpeta, args.salida, args.dpi)
```

---

## CONVENCIÓN DE NOMBRES DE ARCHIVOS

Para que el ensamble quede en el orden correcto, nombrar las imágenes así:

```
p001_portada.png
p002_indice.png
p003_bienvenida.png
p004_cat_A.png          ← separador categoría A
p005_patron01_pag1.png
p006_patron01_pag2.png
p007_patron01_pag3.png
p008_patron02_pag1.png
...
p091_sistema_negocio_1.png
p092_sistema_negocio_2.png
p093_cierre.png
```

---

## CALCULADORA DE CRÉDITOS HIGGSFIELD

```
Nano Banana Pro 2K = 2 créditos por imagen (confirmar con get_cost: true)
Por MCP siempre descuenta créditos, aunque la cuenta tenga ilimitado.

FÓRMULA:
total_páginas = (ítems × 3) + 1 portada + 2 (índice + bienvenida) + cant_categorías + cant_págs_sistema + 1 cierre
total_créditos = total_páginas × 2, más 15% para rehacer páginas

EJEMPLOS (sin el 15%):
- Ebook 10 ítems, 2 categorías, 3 págs sistema = (30 + 1 + 2 + 2 + 3 + 1) × 2 = 78 créditos
- Ebook 20 ítems, 4 categorías, 3 págs sistema = (60 + 1 + 2 + 4 + 3 + 1) × 2 = 142 créditos
- Ebook 30 ítems, 5 categorías, 5 págs sistema = (90 + 1 + 2 + 5 + 5 + 1) × 2 = 208 créditos

TRADUCIR un ebook de imagen con gpt_image_2_5 = 2,75 créditos por página.
Ejemplo: 60 páginas = 165 créditos.
```

---

## VERIFICAR EL ÍNDICE CONTRA EL PDF

```python
from pypdf import PdfReader
n = len(PdfReader("ebook_final.pdf").pages)
print("Páginas del PDF:", n)
# 1. n == filas de plan_paginas.md
# 2. ningún número del índice > n
# 3. cada entrada del índice cae donde empieza esa sección
```

---

## CHECKLIST FINAL

Está en `quality-checklist.md`. Se pasa entera antes de entregar o cargar el ebook.
