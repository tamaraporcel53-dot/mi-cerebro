#!/usr/bin/env python3
"""
Convierte el SRT de HeyGen en un ASS con subtitulos grandes, a la altura de
las manos del avatar.

USO
    python3 srt_a_ass.py entrada.srt salida.ass [--margen 640] [--tam 62]

POR QUE NO ALCANZA CON EL FILTRO subtitles

Si le pasas un SRT pelado al filtro `subtitles` de ffmpeg, libass asume un
lienzo de 384x288 porque el SRT no declara resolucion. Cualquier MarginV
pensado en pixeles de video (por ejemplo 640, sobre un video de 1920 de alto)
queda fuera de ese lienzo y el texto no se dibuja.

Y falla en silencio: el video sale sin subtitulos, sin ningun error.

Este script escribe el ASS con PlayResX 1080 y PlayResY 1920, asi los margenes
se interpretan en pixeles reales del video.

DESPUES

    ffmpeg -i video.mp4 -vf "ass=salida.ass" -c:v libx264 -crf 21 \
      -preset veryfast -pix_fmt yuv420p -c:a copy final.mp4

EL MARGEN

MarginV se cuenta desde el borde de abajo. 640 sobre un video de 1920 deja el
texto a la altura de las manos del avatar, integrado en el cuerpo en vez de
pegado al borde: se lee mejor y disimula bastante el aire de video generado.
"""

import argparse, sys


def a_tiempo_ass(t):
    h, m, resto = t.split(":")
    s, ms = resto.split(",")
    return f"{int(h)}:{int(m):02d}:{int(s):02d}.{int(ms)//10:02d}"


def convertir(srt, ass, margen=640, tam=62, fuente="DejaVu Sans"):
    bloques = [b for b in open(srt, encoding="utf-8").read().strip().split("\n\n") if b.strip()]
    eventos = []
    for b in bloques:
        lineas = b.strip().split("\n")
        if len(lineas) < 3:
            continue
        ini, _, fin = lineas[1].partition(" --> ")
        texto = " ".join(lineas[2:]).strip().replace("\n", " ")
        eventos.append(f"Dialogue: 0,{a_tiempo_ass(ini)},{a_tiempo_ass(fin)},Sub,,0,0,0,,{texto}")

    if not eventos:
        sys.exit("ABORTADO: el SRT no tiene ningun subtitulo")

    cabecera = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,{fuente},{tam},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0.6,0,1,6,3,2,90,90,{margen},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    open(ass, "w", encoding="utf-8").write(cabecera + "\n".join(eventos) + "\n")
    print(f"{len(eventos)} subtitulos -> {ass}  (lienzo 1080x1920, margen {margen}, cuerpo {tam})")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("srt")
    p.add_argument("ass")
    p.add_argument("--margen", type=int, default=640, help="pixeles desde el borde inferior")
    p.add_argument("--tam", type=int, default=62)
    p.add_argument("--fuente", default="DejaVu Sans")
    a = p.parse_args()
    convertir(a.srt, a.ass, a.margen, a.tam, a.fuente)
