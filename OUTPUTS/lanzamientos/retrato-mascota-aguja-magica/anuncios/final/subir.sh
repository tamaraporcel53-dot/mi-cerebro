#!/bin/bash
# uso: subir.sh CODIGO archivo tipo  -> imprime la URL pública
API="https://aekpgsbqjzqntlbucbts.supabase.co/functions/v1/recursos-subida"
c=$1; f=$2; t=$3; b=$(stat -c%s "$f"); nm=$(basename "$f")
r=$(curl -s -X POST "$API" -H "Content-Type: application/json" -d "{\"accion\":\"firmar\",\"codigo\":\"$c\",\"tipo\":\"$t\",\"bytes\":$b,\"nombre\":\"$nm\"}")
id=$(echo "$r" | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const j=JSON.parse(s);console.log(j.archivo_id||"");console.error(j.archivo_id?"":s)})')
up=$(echo "$r" | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>console.log(JSON.parse(s).url_subida||""))')
ct=$(echo "$r" | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>console.log(JSON.parse(s).content_type||""))')
[ -z "$id" ] && exit 1
curl -s -X PUT "$up" -H "Content-Type: $ct" --data-binary @"$f" > /dev/null
curl -s -X POST "$API" -H "Content-Type: application/json" -d "{\"accion\":\"confirmar\",\"codigo\":\"$c\",\"archivo_id\":\"$id\"}" | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const j=JSON.parse(s);console.log(j.url||s)})'
