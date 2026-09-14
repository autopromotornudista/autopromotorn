# /prepare

Orquestador del pipeline editorial completo.

Ejecuta secuencialmente: forum-scout → auto-week → (opcionalmente review-all) → /inbox
No requiere confirmaciones intermedias. No llama a Buffer. No mueve archivos a content/ready/.

```
FORMAS DE USO:
  /prepare              → forum-scout + auto-week + /inbox
  /prepare --full       → forum-scout + auto-week + /review de todos los drafts pending + /inbox
  /prepare --forum-only → solo forum-scout + /inbox
  /prepare --week-only  → solo auto-week + /inbox
  /prepare --dry-run    → forum-scout --dry-run + auto-week (sin guardar) + resumen sin /inbox
```

---

## Paso 0 — Verificar precondiciones

1. Verificar que existen los directorios básicos del pipeline: `content/ideas/`, `content/drafts/`, `content/ready/`
   Si alguno no existe: crearlo con `mkdir -p`

2. Leer `sources/forum/STATE.md` para saber cuándo fue la última ejecución de forum-scout.
   Si `last_run` fue hace menos de 12 horas Y no se especificó `--forum-only`:
   Informar: "Forum-scout ejecutado hace [N] horas. Saltando para evitar sobrecarga del foro."
   Marcar forum-scout como SALTADO.

3. Iniciar audit log:
   Crear `logs/` si no existe.
   Añadir a `logs/audit.log`:
   ```
   [ISO8601] PREPARE started flags=[flags_indicados]
   ```

---

## Paso 1 — Forum Scout (omitir si --week-only o si fue saltado en Paso 0)

Ejecutar `/forum-scout` en modo incremental (sin flags adicionales).

Registrar internamente:
- Hilos analizados
- Ideas nuevas generadas (en content/ideas/forum/)
- Drafts con critic_status: PASS generados
- Drafts con critic_status: REVISE o REJECT
- Errores o fallos

Si forum-scout falla (ej: soloarquitectura.com no disponible):
- Registrar el error: `FORUM-SCOUT FAILED: [mensaje]`
- Continuar con el Paso 2 sin interrumpir la sesión

---

## Paso 2 — Auto Week (omitir si --forum-only)

Ejecutar `/auto-week`.

Registrar internamente:
- Drafts generados esta semana
- Pilares cubiertos
- Días con pieza asignada

Si auto-week falla:
- Registrar el error: `AUTO-WEEK FAILED: [mensaje]`
- Continuar con el Paso 3 sin interrumpir la sesión

---

## Paso 3 — Review de pendientes (solo con --full)

Para cada archivo en `content/drafts/` con `critic_status: pending`:
- Ejecutar `/review [nombre_del_archivo]`
- Registrar resultado (PASS / REVISE / REJECT)

No detener el bucle si un draft individual falla.

---

## Paso 4 — Informe de ejecución

```
══════════════════════════════════════════════
PREPARE — INFORME DE EJECUCIÓN
══════════════════════════════════════════════
Flags:          [flags indicados]
Duración:       [tiempo aproximado]

FORUM-SCOUT [OK | SALTADO | FALLIDO]
  Hilos analizados:       [N]
  Ideas nuevas:           [N]
  Drafts generados:       [N]  (PASS: [N] · REVISE: [N] · REJECT: [N])
  [Si FALLIDO: Error: [mensaje]]

AUTO-WEEK [OK | OMITIDO | FALLIDO]
  Drafts generados:       [N]
  Pilares cubiertos:      [lista]
  [Si FALLIDO: Error: [mensaje]]

REVIEW --full [OK | OMITIDO]
  Drafts revisados:       [N]
  Nuevos PASS:            [N]
  Nuevos REVISE:          [N]

──────────────────────────────────────────────
PIPELINE ACTUAL
  Drafts PASS listos para /approve:  [N]
  Drafts REVISE/pending:             [N]
══════════════════════════════════════════════
```

---

## Paso 5 — Mostrar /inbox (omitir si --dry-run)

Ejecutar `/inbox` automáticamente para mostrar la bandeja actualizada con todos los ítems aprobables.

El /inbox pre-calcula slots y numera los ítems para que el propietario pueda decir directamente "apruebo 1 y 3".

---

## Paso 6 — Cerrar audit log

Añadir a `logs/audit.log`:
```
[ISO8601] PREPARE completed forum_ideas=[N] drafts_created=[N] pass=[N] revise=[N]
```

---

## Reglas críticas

- NUNCA llama a Buffer con escritura
- NUNCA mueve archivos a `content/ready/`
- NUNCA llama a `/approve`
- Si cualquier paso falla: registrar el error, continuar con el siguiente paso
- Las preguntas se agrupan: si falta información para un draft concreto (datos no en knowledge/), no bloquear el pipeline — marcar el draft como `pending_context` y continuar
- La única intervención humana esperada es DESPUÉS del /inbox: "apruebo [N]"

---

## Tabla de autorización

| /prepare puede llamar | ¿Autorizado? |
|-----------------------|-------------|
| /forum-scout          | ✓ SÍ |
| /auto-week            | ✓ SÍ |
| /review [draft]       | ✓ SÍ (solo con --full) |
| /inbox                | ✓ SÍ |
| /approve              | ✗ NUNCA |
| /schedule             | ✗ NUNCA |
| create_post (Buffer)  | ✗ NUNCA |
