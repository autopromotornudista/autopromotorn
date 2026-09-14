#!/usr/bin/env bash
# background_runner.sh — tareas de mantenimiento del pipeline editorial
#
# Sin Claude. Sin Buffer. Sin decisiones de contenido.
# Solo detecta overdue posts, actualiza pipeline snapshot y rota logs.
#
# Ejecutar con systemd user timer (cada 24h) o directamente:
#   bash /home/pineapple/proyectos/autopromotorn/scripts/background_runner.sh
#
# SOLO LINUX — usa date -d para parsear fechas ISO8601.
# En macOS el equivalente sería: date -j -f "%Y-%m-%dT%H:%M:%S"

set -euo pipefail

REPO_DIR="/home/pineapple/proyectos/autopromotorn"
LOG_FILE="$REPO_DIR/logs/background.log"
SNAPSHOT_FILE="$REPO_DIR/logs/pipeline_snapshot.json"
LOCK_DIR="/tmp/autopromotorn_runner.lock"
MAX_LOG_LINES=500
MAX_LOG_BYTES=1048576  # 1MB

# ── Crear logs/ si no existe ────────────────────────────────
mkdir -p "$REPO_DIR/logs"

# ── Lock: prevenir ejecuciones simultáneas ──────────────────
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
    echo "[$(date -Iseconds)] SKIP: lock exists at $LOCK_DIR — otra instancia en ejecución" >> "$LOG_FILE"
    exit 0
fi
trap 'rmdir "$LOCK_DIR" 2>/dev/null || true' EXIT

log() {
    echo "[$(date -Iseconds)] $1" >> "$LOG_FILE"
}

log "START background_runner"

# ── Tarea 1: Overdue detection ──────────────────────────────
# Archivos en content/scheduled/ con scheduled_at en el pasado
NOW_EPOCH=$(date +%s)
OVERDUE_COUNT=0
OVERDUE_IDS=""

SCHEDULED_DIR="$REPO_DIR/content/scheduled"
if [ -d "$SCHEDULED_DIR" ]; then
    for f in "$SCHEDULED_DIR"/*.md; do
        [ -f "$f" ] || continue
        # Leer scheduled_at del frontmatter (buscar la primera ocurrencia)
        SCHED_AT=$(grep -m1 '^scheduled_at:' "$f" 2>/dev/null | sed 's/^scheduled_at:[[:space:]]*//' | tr -d '"' | tr -d "'" | xargs 2>/dev/null || echo "")
        [ -z "$SCHED_AT" ] && continue
        [ "$SCHED_AT" = "~" ] && continue
        [ "$SCHED_AT" = "null" ] && continue
        # Convertir a epoch — date -d acepta ISO8601 en Linux
        SCHED_EPOCH=$(date -d "$SCHED_AT" +%s 2>/dev/null || echo "0")
        if [ "$SCHED_EPOCH" -gt 0 ] && [ "$SCHED_EPOCH" -lt "$NOW_EPOCH" ]; then
            CONTENT_ID=$(grep -m1 '^content_id:' "$f" 2>/dev/null | sed 's/^content_id:[[:space:]]*//' | tr -d '"' | xargs 2>/dev/null || basename "$f")
            log "OVERDUE: $CONTENT_ID  scheduled_at=$SCHED_AT"
            OVERDUE_COUNT=$((OVERDUE_COUNT + 1))
            OVERDUE_IDS="$OVERDUE_IDS $CONTENT_ID"
        fi
    done
fi

if [ "$OVERDUE_COUNT" -gt 0 ]; then
    log "ATENCIÓN: $OVERDUE_COUNT pieza(s) con scheduled_at pasado —$OVERDUE_IDS"
    log "ACCIÓN SUGERIDA: ejecutar /status en sesión Claude para reconciliar con Buffer"
fi

# ── Tarea 2: Pipeline snapshot ──────────────────────────────
count_md() {
    local dir="$1"
    [ -d "$dir" ] || { echo 0; return; }
    find "$dir" -maxdepth 1 -name "*.md" 2>/dev/null | wc -l | tr -d ' '
}

count_md_recursive() {
    local dir="$1"
    [ -d "$dir" ] || { echo 0; return; }
    find "$dir" -name "*.md" 2>/dev/null | wc -l | tr -d ' '
}

count_with_grep() {
    local dir="$1"
    local pattern="$2"
    [ -d "$dir" ] || { echo 0; return; }
    # grep -rl devuelve exit 1 cuando no hay resultados — || true previene la salida con set -e
    { grep -rl "$pattern" "$dir" --include="*.md" 2>/dev/null || true; } | wc -l | tr -d ' '
}

IDEAS_TOTAL=$(count_md_recursive "$REPO_DIR/content/ideas")
IDEAS_FORUM=$(count_md "$REPO_DIR/content/ideas/forum")
DRAFTS_TOTAL=$(count_md "$REPO_DIR/content/drafts")
DRAFTS_PASS=$(count_with_grep "$REPO_DIR/content/drafts" "^critic_status: PASS")
DRAFTS_REVISE=$(count_with_grep "$REPO_DIR/content/drafts" "^critic_status: REVISE")
DRAFTS_REJECT=$(count_with_grep "$REPO_DIR/content/drafts" "^critic_status: REJECT")
DRAFTS_PENDING=$(count_with_grep "$REPO_DIR/content/drafts" "^critic_status: pending")
READY_COUNT=$(count_md "$REPO_DIR/content/ready")
SCHEDULED_COUNT=$(count_md "$REPO_DIR/content/scheduled")
PUBLISHED_COUNT=$(count_md "$REPO_DIR/content/published")
REPLIES_PENDING=$(count_md "$REPO_DIR/content/replies/pending")
REPLIES_APPROVED=$(count_md "$REPO_DIR/content/replies/approved")
REPLIES_SENT=$(count_md "$REPO_DIR/content/replies/sent")

cat > "$SNAPSHOT_FILE" <<JSON
{
  "timestamp": "$(date -Iseconds)",
  "pipeline": {
    "ideas": {
      "total": $IDEAS_TOTAL,
      "forum": $IDEAS_FORUM
    },
    "drafts": {
      "total": $DRAFTS_TOTAL,
      "pass": $DRAFTS_PASS,
      "revise": $DRAFTS_REVISE,
      "reject": $DRAFTS_REJECT,
      "pending": $DRAFTS_PENDING
    },
    "ready": $READY_COUNT,
    "scheduled": $SCHEDULED_COUNT,
    "published": $PUBLISHED_COUNT,
    "replies": {
      "pending": $REPLIES_PENDING,
      "approved": $REPLIES_APPROVED,
      "sent": $REPLIES_SENT
    },
    "overdue_scheduled": $OVERDUE_COUNT
  }
}
JSON

log "SNAPSHOT: ideas=$IDEAS_TOTAL(forum=$IDEAS_FORUM) drafts=$DRAFTS_TOTAL(pass=$DRAFTS_PASS,revise=$DRAFTS_REVISE,pending=$DRAFTS_PENDING) ready=$READY_COUNT scheduled=$SCHEDULED_COUNT replies_pending=$REPLIES_PENDING overdue=$OVERDUE_COUNT"

# ── Tarea 3: Rotación de logs ───────────────────────────────
AUDIT_LOG="$REPO_DIR/logs/audit.log"
if [ -f "$AUDIT_LOG" ] && [ "$(stat -c%s "$AUDIT_LOG" 2>/dev/null || echo 0)" -gt "$MAX_LOG_BYTES" ]; then
    TEMP_LOG="${AUDIT_LOG}.tmp"
    tail -$MAX_LOG_LINES "$AUDIT_LOG" > "$TEMP_LOG"
    mv "$TEMP_LOG" "$AUDIT_LOG"
    log "LOG ROTATED: audit.log truncado a $MAX_LOG_LINES últimas líneas"
fi

log "END background_runner"
