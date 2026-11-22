#!/bin/bash
cd "$(dirname "$0")/.."
VF="split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=40:2,eq=brightness=-0.06[bg];[b]scale=1080:-2[fg];[bg][fg]overlay=0:H*0.70-h/2,fps=30,format=yuv420p"
while IFS='|' read -r n cierre specs; do
  voz=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 organico3/audios/$n.mp3)
  if [ "$cierre" = "L" ]; then target=$(awk "BEGIN{printf \"%.3f\", $voz+0.2+3.3}"); else target=$(awk "BEGIN{printf \"%.3f\", $voz+0.6}"); fi
  d=organico3/base/$n; rm -rf $d; mkdir -p $d; acc=0; i=0
  for spec in $specs; do
    c=${spec%%:*}; want=${spec#*:}
    rem=$(awk "BEGIN{printf \"%.3f\", $target-$acc}"); [ "$(awk "BEGIN{print ($rem<=0.05)?1:0}")" = 1 ] && break
    dd=$(awk "BEGIN{print ($want<$rem)?$want:$rem}"); i=$((i+1))
    ffmpeg -nostdin -loglevel error -y -ss 0.4 -i clips/$c.mp4 -t $dd -filter_complex "$VF" -an -c:v libx264 -preset medium -crf 18 $d/$(printf %02d $i).mp4
    acc=$(awk "BEGIN{printf \"%.3f\", $acc+$dd}")
  done
  # si faltó, repetir el último clip con otro tramo
  rem=$(awk "BEGIN{printf \"%.3f\", $target-$acc}")
  if [ "$(awk "BEGIN{print ($rem>0.05)?1:0}")" = 1 ]; then i=$((i+1)); ffmpeg -nostdin -loglevel error -y -ss 2.5 -i clips/c11_hero.mp4 -t $rem -filter_complex "$VF" -an -c:v libx264 -preset medium -crf 18 $d/$(printf %02d $i).mp4; fi
  (cd $d && for f in [0-9][0-9].mp4; do echo "file '$f'"; done > lista.txt && ffmpeg -nostdin -loglevel error -y -f concat -safe 0 -i lista.txt -c copy mudo.mp4)
  ffmpeg -nostdin -loglevel error -y -i $d/mudo.mp4 -i organico3/audios/$n.mp3 -map 0:v -map 1:a -c:v copy -c:a aac -t $target $d/base.mp4
  echo "$n cierre=$cierre voz=$voz target=$target base=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 $d/base.mp4) planos=$i"
done < organico3/montaje.txt
