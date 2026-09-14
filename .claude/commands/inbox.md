# /inbox

Bandeja unificada de aprobación — muestra todo lo que el propietario puede aprobar en un vistazo.

Solo lectura. No mueve archivos. No llama a Buffer con escritura.

---

## Comportamiento

### Paso 1 — Recopilar posts aprobables

Leer todos los archivos en `content/drafts/` con `critic_status: PASS` en el frontmatter.
Para cada uno extraer: `content_id`, `pillar`, `value_level`, `value_promise`, `draft_date`, `risk_level`, `pain_point`, `needs_verification`.
Ordenar por: `value_level DESC` (HIGH primero), `draft_date ASC`.

### Paso 2 — Recopilar posts ya aprobados pendientes de /schedule

Leer todos los archivos en `content/ready/`.
Para cada uno extraer: `content_id`, `approved_date`, `pillar`, `scheduled_at`.
Si `scheduled_at` ya tiene valor → no mostrar aquí (ya está programado).

### Paso 3 — Calcular slot propuesto para cada post PASS

Para cada draft con `critic_status: PASS`:
1. Leer `knowledge/CADENCIA.md` y `knowledge/CONTENT_PILLARS.md` para el pilar del draft
2. Consultar Buffer en solo lectura: `mcp__buffer__list_posts` → qué días ya tienen contenido
3. Proponer el primer slot libre que no genere canibalización de pilar en días adyacentes
4. Formato: `[día semana] [DD] [mes] · [HH:MM] Europe/Madrid`

Si Buffer no está disponible: indicar "slot pendiente de calcular — ejecuta /schedule [id] para propuesta detallada"

### Paso 4 — Recopilar replies pendientes

Leer todos los archivos en `content/replies/pending/` (si el directorio existe).
Para cada uno extraer: `reply_id`, `original_author`, `original_url`, `original_text_excerpt`, `created_date`, número de propuestas guardadas.
Ordenar por `created_date ASC`.

### Paso 5 — Construir numeración de sesión

Numerar secuencialmente todos los ítems aprobables en orden de presentación:
[1], [2], [3]... Los números son locales a esta ejecución de /inbox.

### Paso 6 — Mostrar el informe

---

## Formato del informe

```
══════════════════════════════════════════════
INBOX — @AutopromotorN — [fecha actual]
══════════════════════════════════════════════

POSTS PARA APROBAR — [N]
(Todos tienen critic_status: PASS)

  [1]  [content_id]  ·  [pillar]  ·  value: [HIGH|MEDIUM]  ·  risk: [low|review]
       Slot propuesto: [día] [DD] [mes] · [HH:MM] Europe/Madrid
       Canal: X · @AutopromotorN
       Pain point: "[pain_point]"
       Promise: "[value_promise]"
       [Si needs_verification no está vacío:]
       ⚠ Pendiente verificar: [item1, item2...]
       ──────
       [TEXTO COMPLETO DEL DRAFT]
       ──────

  [2]  [content_id]  ·  [pillar]  ·  ...
       ...

──────────────────────────────────────────────
POSTS YA APROBADOS — pendientes de /schedule — [N]

  [content_id]  [pillar]  aprobado: [approved_date]
  → /schedule [content_id]

──────────────────────────────────────────────
REPLIES PENDIENTES — [N]

  [3]  [reply_id]  ·  para: @[handle]  ·  creado: [created_date]
       Post original: "[original_text_excerpt]"
       URL: [original_url]
       Propuestas guardadas: [N]
       → /approve-reply [reply_id]

══════════════════════════════════════════════
RESUMEN: [N] posts aprobables · [N] ready sin schedule · [N] replies pendientes

[Si hay posts aprobables:]
Di "apruebo [N]" o "apruebo [N] y [M]" o "apruebo todos los posts".
Tras aprobación → se programará en Buffer automáticamente con el slot propuesto.

[Si todo está vacío:]
✓ Bandeja vacía — no hay ítems pendientes de aprobación.
  Siguiente paso: /prepare para generar nuevo contenido.
══════════════════════════════════════════════
```

---

## Reglas críticas

- Si `content/replies/pending/` no existe: mostrar la sección con `[sin replies pendientes]`, no error.
- Si Buffer no está disponible: mostrar slots como "pendiente" pero no fallar en las secciones locales.
- Los números [1], [2], [3] son locales a esta sesión de /inbox — vuelven a empezar en 1 en cada ejecución.
- NO inventar slots si Buffer no está disponible.
- NO preseleccionar aprobaciones. El humano dice explícitamente qué aprueba.

---

## Acción posterior a "apruebo [IDs]"

Cuando el propietario dice "apruebo [N]" o "apruebo [N] y [M]" o "apruebo todos" en el contexto de esta sesión:

Claude ejecuta automáticamente, sin preguntar de nuevo, para cada ítem de post aprobado:
1. `/approve [content_id]` — calcula hash SHA256, registra aprobación, mueve a `content/ready/`
2. `/schedule [content_id] --confirm` — usa el slot propuesto en este /inbox — verifica hash — llama Buffer

Si el hash no coincide (texto modificado entre /inbox y la aprobación): bloqueo automático, informar al humano, no continuar con ese ítem.

Para replies: redirigir a `/approve-reply [reply_id]` que muestra las propuestas para que el humano elija.
