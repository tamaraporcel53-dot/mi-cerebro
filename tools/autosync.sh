#!/usr/bin/env bash
# Guardado automático del cerebro: commit + push a GitHub.
# Lo ejecuta el hook Stop de .claude/settings.json al terminar cada respuesta,
# tanto en sesiones locales como en sesiones en la nube que clonan el repositorio.
# Nunca falla ruidosamente: si algo sale mal, sale en silencio y lo deja anotado en el log.
# Usa tu nombre y tu mail de git (git config user.name / user.email).

set -u
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO" || exit 0
LOG="$REPO/.claude/autosync.log"

# Si la carpeta todavía no es un repositorio, no hace nada
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

# Sin cambios: no hace nada
if [ -z "$(git status --porcelain 2>/dev/null)" ]; then
  exit 0
fi

N=$(git status --porcelain | wc -l | tr -d ' ')
AREAS=$(git status --porcelain | awk '{print $NF}' | cut -d/ -f1 | sort -u | head -4 | paste -sd', ' -)

git add -A 2>/dev/null

MSG="Guardado automatico: $N archivo(s) en $AREAS"

if git commit -q -m "$MSG" 2>>"$LOG"; then
  # Si otra sesión (por ejemplo en la nube) guardó algo, se trae antes de subir
  if ! git pull -q --rebase --autostash origin "$(git rev-parse --abbrev-ref HEAD)" 2>>"$LOG"; then
    git rebase --abort 2>/dev/null
    echo "$(date -u +%FT%TZ) CONFLICTO  pull --rebase fallo, el cambio queda guardado local" >> "$LOG"
  fi
  if git push -q origin HEAD 2>>"$LOG"; then
    echo "$(date -u +%FT%TZ) OK  guardado y subido  $N archivo(s): $AREAS" >> "$LOG"
  else
    echo "$(date -u +%FT%TZ) PARCIAL  guardado local, no se pudo subir  $N archivo(s): $AREAS" >> "$LOG"
  fi
else
  echo "$(date -u +%FT%TZ) ERROR  no se pudo guardar (¿configuraste git user.name y user.email?)" >> "$LOG"
fi
exit 0
