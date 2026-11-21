#!/bin/bash
# uso: post.sh NN  -> NN-WEB.mp4 (marca de agua suave que cambia de lugar + master -12 LUFS + liviano)
cd "$(dirname "$0")"; n=$1
ffmpeg -nostdin -loglevel error -y -i $n-FINAL.mp4 -loop 1 -i ../wm.png -filter_complex "[1]format=rgba,colorchannelmixer=aa=0.18,scale=520:-1[w];[0][w]overlay=x='if(lt(mod(t,10),5),40,W-w-40)':y='if(lt(mod(t,10),5),150,H-170)':shortest=1,format=yuv420p" -af "acompressor=threshold=-18dB:ratio=6:attack=5:release=120:makeup=2,loudnorm=I=-12:TP=-1.0:LRA=3,alimiter=limit=0.97" -c:v libx264 -preset slow -crf 23 -maxrate 4M -bufsize 8M -profile:v high -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 128k $n-WEB.mp4
echo "$n $(ffprobe -v quiet -show_entries format=duration -of csv=p=0 $n-WEB.mp4)s $(ffprobe -v quiet -select_streams v -show_entries stream=width,height -of csv=p=0 $n-WEB.mp4) audio:$(ffprobe -v quiet -select_streams a -show_entries stream=codec_name -of csv=p=0 $n-WEB.mp4) $(stat -c%s $n-WEB.mp4) bytes"
