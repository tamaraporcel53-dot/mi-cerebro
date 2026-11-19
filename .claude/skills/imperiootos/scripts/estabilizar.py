#!/usr/bin/env python3
"""
Quita la vibracion de camara del render de HeyGen.

USO
    python3 estabilizar.py render_crudo.mp4 render.mp4

POR QUE HACE FALTA

HeyGen, al animar una imagen fija, le agrega un temblor de camara en mano
simulado. Con expressiveness="high" es fuerte y el comprador lo percibe como
"parece que le esta pegando a la mesa y vibra la camara". Medido sobre el
fondo del taller (que deberia estar quieto):

    render crudo de HeyGen ....... 3,0 / 3,8 px de temblor por cuadro
    tramos de imagen del montaje . 0,8 / 1,4 px
    despues de estabilizar ....... 0,4 / 0,8 px

El avatar se DESPLAZA poco (24/33 px) pero TIEMBLA mucho: esa combinacion es
la que se lee como vibracion. Un b-roll filmado a mano tiembla parecido pero
recorre 110 px, y por eso no molesta.

DOS ARREGLOS, LOS DOS HACEN FALTA

1. En el origen: expressiveness="medium" (nunca "high") y un motionPrompt que
   diga "camara fija, torso anclado" y que NO mencione inclinarse hacia la
   camara ni ningun movimiento de camara.
2. Aca: vidstab en dos pasadas.

NO ROMPE LA SINCRONIA

vidstabtransform conserva el conteo de cuadros exacto. Este script lo verifica
y aborta si no coincide. Estabilizar SIEMPRE antes de montar: el montaje se
calcula sobre el archivo que sale de aca.

NO CONSUME CREDITOS DE HEYGEN. Se puede correr sobre un render ya pagado.

TARDA. Las dos pasadas sobre un video de 2:30 en 1080x1920 llevan varios minutos.
Con preset "medium" la segunda pasada supera el limite de 10 minutos por comando;
por eso va en "veryfast" con CRF 17, que no se distingue a ojo y entra en tiempo.
Si aun asi se corta, lanzalo en segundo plano:

    nohup python3 estabilizar.py crudo.mp4 render.mp4 > estab.log 2>&1 &

y revisa el log hasta que diga SINCRONIA OK. El .trf de la pasada 1 queda en la
carpeta de la salida, asi que si se corta la pasada 2 no hay que rehacer la 1.

WINDOWS Y FFMPEG 9 (arreglado 2026-10-28): la "C:" de una ruta absoluta rompe el
filtro vidstab (los ":" separan opciones), por eso el .trf va con nombre relativo;
y -vsync ya no existe en ffmpeg 9: se usa -fps_mode cfr.
"""

import os, subprocess, sys, tempfile


def cuadros_de(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames",
         "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", path],
        capture_output=True, text=True)
    return int(r.stdout.strip())


def temblor(path, t0=None, dur=8.0):
    """Mide el temblor de alta frecuencia del fondo. Devuelve (x, y) en px."""
    try:
        import cv2, numpy as np
    except ImportError:
        return None
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    if t0 is None:
        n_tot = cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0
        t0 = max(0.0, (n_tot / fps) * 0.4)
    cap.set(cv2.CAP_PROP_POS_MSEC, t0 * 1000)
    prev, res, mask = None, [], None
    for _ in range(int(dur * fps)):
        ok, f = cap.read()
        if not ok:
            break
        g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        h, w = g.shape
        if mask is None:
            mask = np.zeros((h, w), np.uint8)
            mask[0:int(h * 0.22), :] = 255      # franja de fondo, sin cuerpo
        if prev is not None:
            p0 = cv2.goodFeaturesToTrack(prev, 200, 0.01, 10, mask=mask)
            if p0 is not None and len(p0) > 8:
                p1, st, _ = cv2.calcOpticalFlowPyrLK(prev, g, p0, None)
                good = st.ravel() == 1
                if good.sum() > 8:
                    res.append(np.median((p1[good] - p0[good]).reshape(-1, 2), axis=0))
        prev = g
    cap.release()
    if len(res) < 3:
        return None
    hf = np.abs(np.diff(np.array(res), axis=0)).mean(axis=0)
    return float(hf[0]), float(hf[1])


def main(entrada, salida):
    n_ini = cuadros_de(entrada)
    antes = temblor(entrada)
    if antes:
        print(f"temblor ANTES:  x={antes[0]:.2f}  y={antes[1]:.2f} px/cuadro")

    # Windows: una ruta con "C:" rompe el filtro (los ":" separan opciones). Se trabaja con un nombre relativo,
    # en la carpeta de la salida y único por archivo (dos estabilizaciones en paralelo no se pisan).
    entrada, salida = os.path.abspath(entrada), os.path.abspath(salida)
    os.chdir(os.path.dirname(salida))
    trf = os.path.splitext(os.path.basename(salida))[0] + "_vidstab.trf"

    print("pasada 1 de 2: detectando el movimiento...")
    subprocess.run(
        ["ffmpeg", "-v", "error", "-i", entrada,
         "-vf", f"vidstabdetect=shakiness=8:accuracy=15:stepsize=6:"
                f"mincontrast=0.2:result={trf}",
         "-f", "null", "-"], check=True)

    print("pasada 2 de 2: corrigiendo...")
    # smoothing=30 (1,2 s a 25 fps) mata el temblor y deja pasar el movimiento
    # real del cuerpo. optzoom=1 evita bordes negros con ~3% de zoom.
    # unsharp compensa el reblandecimiento de la interpolacion.
    subprocess.run(
        ["ffmpeg", "-v", "error", "-i", entrada,
         "-vf", f"vidstabtransform=input={trf}:smoothing=30:optzoom=1:"
                f"zoomspeed=0.1:interpol=bicubic:crop=black,"
                f"unsharp=5:5:0.6:3:3:0.4",
         "-c:v", "libx264", "-crf", "17", "-preset", "veryfast",
         "-pix_fmt", "yuv420p", "-fps_mode", "cfr",
         "-c:a", "copy", salida, "-y"], check=True)

    n_fin = cuadros_de(salida)
    print(f"\nVERIFICACION: {n_ini} cuadros entraron / {n_fin} salieron")
    if n_ini != n_fin:
        sys.exit("ABORTADO: cambio el conteo de cuadros. Se rompe la sincronia. No usar.")

    despues = temblor(salida)
    if antes and despues:
        print(f"temblor DESPUES: x={despues[0]:.2f}  y={despues[1]:.2f} px/cuadro")
        baja = 100 * (1 - (despues[0] + despues[1]) / (antes[0] + antes[1]))
        print(f"reduccion: {baja:.0f}%")
        if despues[0] > 1.5 or despues[1] > 1.5:
            print("AVISO: sigue por encima de 1,5 px. Subir smoothing a 45 y repetir.")
    print("SINCRONIA OK -> montar sobre este archivo, no sobre el crudo")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("uso: python3 estabilizar.py render_crudo.mp4 render.mp4")
    main(sys.argv[1], sys.argv[2])
