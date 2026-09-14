# /status

Métricas y estado de la cuenta @AutopromotorN.

Combina datos locales del pipeline con datos de Buffer MCP (solo lectura).
No mueve archivos. No llama a Buffer con escritura.

---

## Proceso

### Paso 1 — Datos locales del pipeline

Contar archivos en cada directorio:
- `content/ideas/` — total y desglose por subdirectorio (forum/, otros)
- `content/drafts/` — total y por `critic_status`: PASS / REVISE / REJECT / pending
- `content/ready/` — total
- `content/scheduled/` — total
- `content/published/` — total y últimas 2 semanas
- `content/replies/pending/` — si existe
- `content/replies/approved/` — si existe
- `content/replies/sent/` — si existe

Si `logs/pipeline_snapshot.json` existe, leerlo para ver cuándo fue la última ejecución del background runner.

### Paso 2 — Datos de Buffer (solo lectura)

Ejecutar en orden:
1. `mcp__buffer__get_account` → organizationId, nombre de la organización
2. `mcp__buffer__list_channels` → channelId, seguidores actuales, nombre del canal
3. `mcp__buffer__get_aggregated_post_metrics` → métricas del último mes (reach, engagement, reactions, comments)
4. `mcp__buffer__list_posts` → posts programados pendientes

Si Buffer no está disponible: registrar "Buffer no disponible en esta sesión" y continuar con datos locales únicamente.

### Paso 3 — Reconciliación

Para cada archivo en `content/scheduled/`:
1. Leer `buffer_post_id` del frontmatter
2. Si `buffer_post_id` es null, vacío o `~`: marcar como "WARN — sin buffer_post_id"
3. Buscar ese `buffer_post_id` en la lista de posts de Buffer
4. Si existe: `[OK]`
5. Si no existe: `[WARN — no encontrado en Buffer]`

Para cada archivo en `content/ready/` con `approved_date` de hace más de 3 días:
- Marcar como "POSIBLE RETRASO — aprobado hace [N] días sin programar"

### Paso 4 — Mostrar informe

---

## Formato del informe

```
══════════════════════════════════════════════════════════
STATUS — @AutopromotorN — [fecha actual]
══════════════════════════════════════════════════════════

CUENTA
  Seguidores:         [N]
  Canal:              X · @AutopromotorN
  Buffer:             [plan / estado de conexión]
  Background runner:  último run [fecha] | [nunca ejecutado]

──────────────────────────────────────────────────────────
PIPELINE LOCAL
  Ideas:              [N] total  ([N] forum · [N] otros)
  Drafts:             [N] total
    · PASS:             [N]  ← listos para /approve
    · REVISE:           [N]  ← requieren corrección
    · REJECT:           [N]  ← descartados
    · pending:          [N]  ← sin /review aún
  Ready:              [N]  ← esperando /schedule
  Scheduled:          [N]  en cola de Buffer
  Published:          [N]  total  ([N] últimas 2 semanas)
  Replies pending:    [N]
  Replies approved:   [N]  ← enviados en espera confirmación
  Replies sent:       [N]

──────────────────────────────────────────────────────────
BUFFER — PRÓXIMAS PUBLICACIONES
  [DD/MM] [HH:MM CET]  [pillar]  "[primeros 60 chars]"
  [DD/MM] [HH:MM CET]  ...
  [Si vacío: "Sin posts programados en Buffer"]

──────────────────────────────────────────────────────────
MÉTRICAS ÚLTIMO MES
  Reach total:        [N] impresiones
  Reactions:          [N]
  Comments:           [N]
  Engagement rate:    [N]%
  [Si no disponible: "Métricas no disponibles — Buffer desconectado"]

──────────────────────────────────────────────────────────
RECONCILIACIÓN BUFFER
  [OK]   [content_id] — buffer_post_id:[id] — sincronizado
  [WARN] [content_id] — no encontrado en Buffer · revisar manualmente
  [WARN] [content_id] — sin buffer_post_id en frontmatter
  [RETRASO] [content_id] — aprobado hace [N] días sin programar

══════════════════════════════════════════════════════════
ACCIÓN SUGERIDA:
  [la más urgente del pipeline — ej: "N drafts con PASS listos para /inbox"]
══════════════════════════════════════════════════════════
```

---

## Reglas

- Si Buffer no está disponible: mostrar sección con "Buffer no disponible en esta sesión". No fallar.
- Si algún directorio no existe: mostrar `[0]` en el contador, no error.
- La reconciliación es informativa: WARN no bloquea nada, solo informa.
- No modificar ningún archivo ni llamar a Buffer con escritura.
