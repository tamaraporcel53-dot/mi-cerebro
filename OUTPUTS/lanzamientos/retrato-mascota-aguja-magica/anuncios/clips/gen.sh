#!/bin/bash
set -a; . "C:/Users/Tamara/Documents/mi-cerebro/.env"; set +a
CLI="C:/Users/Tamara/Documents/mi-cerebro/.claude/skills/kie-models/scripts/kie-cli.mjs"
IMG="C:/Users/Tamara/Documents/mi-cerebro/OUTPUTS/lanzamientos/retrato-mascota-aguja-magica/imagenes/web"
cd "$(dirname "$0")"
one() {
  name="$1"; src="$2"; prompt="$3"
  [ -s "$name.mp4" ] && return
  url=$(curl -s -X POST https://kieai.redpandaai.co/api/file-stream-upload -H "Authorization: Bearer $KIE_API_KEY" -F "file=@$IMG/$src.jpg" -F "uploadPath=anuncios" | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>console.log(JSON.parse(s).data.downloadUrl))')
  inp=$(node -e 'console.log(JSON.stringify({prompt:process.argv[1],image_url:process.argv[2],duration:"6",resolution:"768P"}))' "$prompt" "$url")
  out=$(node "$CLI" run hailuo/2-3-image-to-video-standard --max-credits 30 --input "$inp" 2>&1)
  vurl=$(echo "$out" | grep -oE 'https://tempfile[^"]+\.mp4' | head -1)
  if [ -n "$vurl" ]; then curl -s -o "$name.mp4" "$vurl"; echo "OK $name"; else echo "FALLA $name: $(echo "$out" | tail -3 | tr '\n' ' ')"; fi
}
n=0
while IFS='|' read -r name src prompt; do
  one "$name" "$src" "$prompt" < /dev/null &
  n=$((n+1)); if [ $((n % 5)) -eq 0 ]; then wait; fi
done < lote1.txt
wait
echo FIN
