#!/usr/bin/env python3
"""
Monta el VSL: corta el render del avatar en tramos con distinto encuadre,
intercala las piezas visuales, y verifica la sincronia cuadro por cuadro.

USO
    python3 montar_vsl.py config.json

FORMATO DEL config.json
{
  "render":  "f_raw.mp4",          # el MP4 limpio que bajaste de HeyGen (video_url)
  "salida":  "montado_mudo.mp4",
  "fps":     25,
  "cortes": [
    {"seg": 9.8,  "dur": 3.8, "tipo": "video",  "archivo": "brolls/florero.mp4", "offset": 0.0},
    {"seg": 13.6, "dur": 3.3, "tipo": "imagen", "archivo": "planos/01.png"}
  ]
}

  seg     segundo del VIDEO FINAL donde entra el corte
  dur     cuanto dura el corte
  tipo    "imagen" o "video"
  offset  solo para video: desde que segundo del clip empezar
          (sirve para saltear el arranque muerto de una filmacion)

POR QUE TODO SE CALCULA EN CUADROS

Pedirle a ffmpeg tramos en segundos hace que cada uno se redondee al cuadro
mas cercano. A 25 fps eso es 40 ms por tramo, y los redondeos se acumulan
siempre para el mismo lado. En un caso real, con 31 tramos, el montaje quedo
0,56 segundos mas largo que el render: la imagen se atrasaba respecto del
audio, cada vez mas hacia el final, y se percibia como que la voz iba
adelantada respecto del movimiento de la boca.

Por eso este script trabaja en cuadros y verifica dos veces: cada tramo al
generarse, y el montaje completo contra el render. Si algo no cuadra, aborta.
"""

import json, os, subprocess, sys


def cuadros_de(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames",
         "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", path],
        capture_output=True, text=True)
    return int(r.stdout.strip())


def main(cfg_path):
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(cfg_path)) or "."
    os.chdir(base)

    render = cfg["render"]
    fps = cfg.get("fps", 25)
    salida = cfg.get("salida", "montado_mudo.mp4")
    total = cuadros_de(render)
    print(f"render: {render} -> {total} cuadros a {fps} fps")

    # zooms alternados para simular multicamara con un solo render
    zooms = cfg.get("zooms", [1.00, 1.16, 1.00, 1.22, 1.06, 1.00, 1.18,
                              1.02, 1.12, 1.00, 1.20, 1.04, 1.14, 1.10])

    # Un tramo de avatar mas largo que esto se parte en varios encuadres.
    # Sin esto, un hueco de 19 segundos entre dos cortes queda como un plano
    # unico e inmovil de 19 segundos, y ahi es donde la gente se va.
    max_tramo = int(cfg.get("max_avatar_seg", 7.0) * fps)

    plan, cur, zi = [], 0, 0

    def avatar(inicio, nf):
        """Agrega un tramo de avatar, partiendolo en varios encuadres si es largo.
        Reparte los cuadros de forma exacta: la suma siempre da nf."""
        nonlocal zi
        if nf <= 0:
            return
        n = max(1, -(-nf // max_tramo))         # division hacia arriba
        base, resto = divmod(nf, n)
        off = 0
        for k in range(n):
            sub = base + (1 if k < resto else 0)
            plan.append(("avatar", inicio + off, sub, zooms[zi % len(zooms)], 0.0))
            zi += 1
            off += sub

    for c in cfg["cortes"]:
        sf, df = round(c["seg"] * fps), round(c["dur"] * fps)
        if sf > cur + 10:                       # hueco de avatar entre cortes
            avatar(cur, sf - cur)
            cur = sf
        plan.append((c["tipo"], cur, df, c["archivo"], c.get("offset", 0.0)))
        cur += df
    if cur < total:
        avatar(cur, total - cur)

    suma = sum(p[2] for p in plan)
    print(f"cuadros planificados: {suma} / esperados: {total}")
    if suma != total:
        sys.exit(f"ABORTADO: descuadre de {suma - total} cuadros en el plan")

    os.makedirs("_tramos", exist_ok=True)
    lista = []
    for i, (tipo, inicio, nf, arch, off) in enumerate(plan):
        out = f"_tramos/{i:03d}.mp4"
        lista.append(out)

        if tipo == "avatar":
            z = arch                            # aca 'arch' es el zoom
            vf = (f"crop=iw/{z}:ih/{z}:(iw-iw/{z})/2:(ih-ih/{z})*0.30,"
                  f"scale=1080:1920:flags=bilinear,setsar=1,fps={fps}")
            cmd = ["ffmpeg", "-v", "error", "-ss", f"{inicio/fps:.6f}",
                   "-i", render, "-an", "-vf", vf]
        elif tipo == "imagen":
            d = nf / fps
            # paneo lento para que la foto no quede congelada
            vf = (f"scale=1350:2400:force_original_aspect_ratio=increase,"
                  f"crop=1080:1920:'(iw-1080)/2+45*sin(t*0.5)':'(ih-1920)/2-25*(t/{d})',"
                  f"setsar=1,fps={fps}")
            cmd = ["ffmpeg", "-v", "error", "-loop", "1", "-i", arch, "-an", "-vf", vf]
        else:                                    # video
            vf = (f"scale=1080:1920:force_original_aspect_ratio=increase,"
                  f"crop=1080:1920,setsar=1,fps={fps}")
            cmd = ["ffmpeg", "-v", "error", "-ss", f"{off}", "-i", arch, "-an", "-vf", vf]

        cmd += ["-frames:v", str(nf), "-c:v", "libx264", "-crf", "21",
                "-preset", "ultrafast", "-pix_fmt", "yuv420p", "-vsync", "cfr", out, "-y"]
        subprocess.run(cmd, check=True)

        real = cuadros_de(out)
        if real != nf:
            sys.exit(f"ABORTADO: {out} salio con {real} cuadros y deberia tener {nf}")
        print(f"  ok {out}  {tipo:6}  {nf} cuadros")

    with open("_tramos/lista.txt", "w") as f:
        f.write("\n".join(f"file '{os.path.abspath(x)}'" for x in lista) + "\n")
    subprocess.run(["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", "_tramos/lista.txt", "-c", "copy", salida, "-y"], check=True)

    fin = cuadros_de(salida)
    print(f"\nVERIFICACION: {fin} cuadros en el montaje / {total} en el render de HeyGen")
    if fin != total:
        sys.exit("ABORTADO: el montaje no coincide con el render. No entregar.")
    print("SINCRONIA OK")
    print(f"\nAhora remuxealo con el audio original:\n"
          f"  ffmpeg -i {salida} -i {render} -map 0:v:0 -map 1:a:0 "
          f"-c:v copy -c:a aac -b:a 128k final.mp4")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("uso: python3 montar_vsl.py config.json")
    main(sys.argv[1])
