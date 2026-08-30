# /schedule

HUMAN GATE — Único punto autorizado para llamar Buffer MCP y crear posts.

```
FORMAS DE USO:

/schedule READY-X                    → propuesta automática de slot
/schedule READY-X [fecha] [hora]     → propuesta con slot manual
/schedule READY-X --next             → siguiente mejor slot alternativo
/schedule READY-X --confirm          → ÚNICO paso que llama Buffer
```

⚠️ REGLA ABSOLUTA:
- `create_post` solo se llama con `--confirm`.
- Nunca tras el primer `/schedule`, aunque el humano haya visto la fecha.
- Sin excepción.

---

## FASE 1 — PREVIEW

Se activa con: `/schedule READY-X`, `/schedule READY-X [fecha] [hora]`, `/schedule READY-X --next`

### Paso 1 — Verificar el archivo

Buscar `content/ready/[READY-X].md`.

Si no existe:
```
⛔ SCHEDULE BLOQUEADO
El archivo no está en content/ready/.
Solo se pueden programar archivos aprobados con /approve.
```
Detenerse.

Verificar en el frontmatter:
- `critic_status: PASS` — si no, bloquear con mensaje.
- `value_level: HIGH` — si no, bloquear con mensaje.

```
⛔ SCHEDULE BLOQUEADO
critic_status: [valor actual] — se requiere PASS.
value_level: [valor actual] — se requiere HIGH.
Ejecutar /review para corregir antes de programar.
```

---

### Paso 2 — Leer contexto editorial

Leer en este orden:
1. `knowledge/CONTENT_PILLARS.md` — pilares operativos, días actuales, emociones objetivo
2. `knowledge/STRATEGY.md` — horarios, cadencia, historial de engagement
3. `metrics/EXPERIMENTS.md` — experimentos activos y completados

Registrar internamente:
- Pilar operativo del READY (del frontmatter: `pillar`)
- Día editorial sugerido por CONTENT_PILLARS.md para ese pilar
- Franjas horarias con evidencia (de STRATEGY.md y EXPERIMENTS.md)
- Experimentos activos que impliquen horarios

---

### Paso 3 — Consultar Buffer en modo solo lectura

Ejecutar SOLO lectura:
1. `mcp__buffer__get_account` → organizationId
2. `mcp__buffer__list_channels` → channelId de @AutopromotorN en X
3. `mcp__buffer__list_posts` → posts programados actuales

Registrar internamente:
- Qué días/horas ya tienen contenido en Buffer
- Pilar/tema de cada post programado si está disponible
- Slots libres en los próximos 7 días

NO crear ni modificar ningún post en este paso.

---

### Paso 4 — Calcular la propuesta de slot

**Si el humano indicó fecha/hora manual:**

Resolver la expresión de fecha:

| Expresión | Resolución |
|-----------|-----------|
| "lunes" | Próximo lunes (si hoy es lunes, el siguiente) |
| "mañana" | Hoy + 1 día |
| "1 sep" / "1/9" | 1 de septiembre del año en curso |
| "2026-09-01" | Fecha exacta |

Evaluar si ese slot tiene conflicto:
- ¿Hay ya contenido programado ese día?
- ¿Repite pilar del día anterior o siguiente?
- ¿Repite audiencia/ángulo demasiado cerca?

Si hay conflicto, mostrar aviso pero respetar si el humano insiste.

---

**Si no se indicó fecha/hora (propuesta automática):**

Determinar el slot óptimo por orden de prioridad:

1. **Domingo:** si la pieza tiene la mayor combinación de value_to_audience + originalidad + potencial de conversación disponible en la semana, proponer domingo como slot preferente. Si ya existe una pieza claramente superior programada ese domingo → no asignar aquí.
2. Día editorial del pilar (de CONTENT_PILLARS.md)
3. Slot libre ese día (no hay post programado en Buffer)
4. Sin repetición de pilar/ángulo en días adyacentes
5. Audiencia: sin saturar el mismo perfil en días consecutivos
6. content_job: usar como criterio secundario de franja horaria
   - `reach` → franja con mayor oportunidad de descubrimiento
   - `authority` / `decision` → momentos de mayor concentración
   - `retention` → consistencia semanal sobre hora exacta
7. Franja horaria: usar datos de STRATEGY.md y EXPERIMENTS.md
   - Si hay experimento activo que incluya horarios: aplicarlo
   - Si no: 18:00–20:00 CET como hipótesis operativa (STRATEGY.md)
   - Si no hay evidencia suficiente para elegir: mostrar fallback (ver Paso 4b)

Si el día del pilar está ocupado → proponer el día más próximo libre.

---

**Paso 4b — Fallback si no hay evidencia suficiente:**

Si no se puede determinar un slot con claridad, NO fingir precisión.

Mostrar:
```
Sin evidencia suficiente para preferir claramente un horario.
Opciones:

A. [día] [HH:MM] — [razón breve]
B. [día] [HH:MM] — [razón breve]
C. [día] [HH:MM] — [razón breve]

Indica tu preferencia o usa /schedule READY-X --confirm tras elegir.
```

---

### Paso 5 — Comprobar canibalización

Antes de generar el preview, verificar:
- ¿Hay dos posts del mismo pilar en días consecutivos?
- ¿Hay dos piezas financieras densas seguidas?
- ¿Se repite el mismo ángulo o pain_point muy cercano?
- ¿Se satura el mismo perfil de audiencia en 48h?

Si se detecta conflicto: ajustar la propuesta y explicarlo en MOTIVO DEL SLOT.

---

### Paso 6 — Mostrar el PREVIEW completo

```
══════════════════════════════════════════════════════════
PROGRAMACIÓN PROPUESTA
══════════════════════════════════════════════════════════

READY:          [ready_id]
CANAL:          X · @AutopromotorN
FECHA:          [DD/MM/YYYY · Día de la semana]
HORA:           [HH:MM] · Europe/Madrid  ([HH:MM] UTC)
TIMEZONE:       Europe/Madrid
FORMATO:        tweet / hilo N tweets

──────────────────────────────────────────────────────────
METADATOS
──────────────────────────────────────────────────────────
Pilar:          [pillar]
Audiencia:      [primary_audience — A|B|C|D] + descripción breve
Pain point:     [pain_point]
Content job:    [content_job]
Value level:    HIGH
Critic status:  PASS

──────────────────────────────────────────────────────────
MOTIVO DEL SLOT
──────────────────────────────────────────────────────────
[2-4 líneas explicando por qué se propone ese día/hora:
 — pilar y día editorial correspondiente
 — slots Buffer ocupados / libres
 — experimento activo si aplica
 — separación respecto a contenido adyacente]

──────────────────────────────────────────────────────────
PROGRAMACIÓN CERCANA
──────────────────────────────────────────────────────────
Lunes:      [post / pilar / hora  ó  vacío]
Martes:     [post / pilar / hora  ó  vacío]
Miércoles:  [post / pilar / hora  ó  vacío]
Jueves:     [post / pilar / hora  ó  vacío]
Viernes:    [post / pilar / hora  ó  vacío]

──────────────────────────────────────────────────────────
CONTENIDO COMPLETO
──────────────────────────────────────────────────────────

[Si tweet único:]
[texto completo — N caracteres]

[Si hilo:]
1/N
[texto · N chars]

2/N
[texto · N chars]

...

──────────────────────────────────────────────────────────
WARNINGS
──────────────────────────────────────────────────────────
needs_verification:
  - [item 1]
  - [item 2]
[o "Ninguno" si no hay]

[Si horario manual con conflicto:]
⚠ CONFLICTO DETECTADO: [descripción del conflicto]
   El humano ha propuesto este slot manualmente — se respeta si confirmas.

══════════════════════════════════════════════════════════
ESTADO: PENDIENTE DE CONFIRMACIÓN HUMANA

OPCIONES:
  /schedule [ready_id] --confirm        → aceptar esta propuesta y programar
  /schedule [ready_id] [nueva fecha]    → recalcular con otro slot
  /schedule [ready_id] --next           → proponer el siguiente mejor slot

⚠ Buffer no ha sido modificado. Ningún post ha sido creado todavía.
══════════════════════════════════════════════════════════
```

---

## FASE 2 — CONFIRMACIÓN

Se activa SOLO con: `/schedule READY-X --confirm`

### Paso 7 — Verificar consistencia pre-confirmación

Antes de llamar a Buffer, re-verificar:

1. El archivo `content/ready/[READY-X].md` sigue en `content/ready/`
2. `critic_status` sigue siendo PASS
3. `value_level` sigue siendo HIGH
4. El texto del post no ha cambiado desde el preview
5. La fecha/hora propuesta en el preview sigue disponible en Buffer (re-leer `list_posts`)

Si algo cambió:
```
⛔ CONFIRMACIÓN CANCELADA
El estado ha cambiado desde el último preview:
  [detalle del cambio]

Genera un nuevo preview con /schedule [ready_id] antes de confirmar.
```
Detenerse.

---

### Paso 8 — Llamar Buffer MCP

Solo aquí se llama a `create_post`.

Ejecutar en este orden:

1. `mcp__buffer__get_account` → organizationId
2. `mcp__buffer__list_channels` → channelId de @AutopromotorN en X
3. Leer el texto del post desde `content/ready/[ready_id].md`

Para tweet único:
```
mcp__buffer__create_post
  organizationId: [id]
  channelId: [id de X @AutopromotorN]
  text: [texto del post]
  scheduledAt: [ISO 8601 en UTC]
```

Para hilo: crear el primer tweet, usar su `id` como `replyToPostId` para el siguiente, en orden.

---

### Paso 9 — Registrar y mover

Actualizar el frontmatter de `content/ready/[ready_id].md`:
```yaml
scheduled_at: YYYY-MM-DDTHH:MM:00+02:00
buffer_post_id: [id devuelto por Buffer]
scheduled_by: human
scheduled_date: YYYY-MM-DD
```

Mover el archivo:
`content/ready/[ready_id].md` → `content/scheduled/scheduled-[slug]-[fecha].md`

---

### Paso 10 — Informe final

```
══════════════════════════════════════════════════════════
SCHEDULE — CONFIRMADO
══════════════════════════════════════════════════════════
Programado:  [DD/MM/YYYY] · [HH:MM] CET
Canal:       X · @AutopromotorN
Buffer ID:   [id]
Archivo:     content/scheduled/scheduled-[slug]-[fecha].md
──────────────────────────────────────────────────────────
Cuando se publique: /published scheduled-[slug]-[fecha]
══════════════════════════════════════════════════════════
```

---

## Aprendizaje progresivo

Después de cada publicación, los resultados deben registrarse en `metrics/EXPERIMENTS.md` si corresponden a un experimento activo.

El sistema usará ese historial para refinar futuras propuestas de slot. No establecer reglas permanentes sin muestra suficiente (mínimo N=5 para el mismo tipo de contenido y franja).

---

## Resumen de quién puede llamar create_post

| Comando | ¿Puede llamar create_post? |
|---------|---------------------------|
| `/schedule --confirm` | ✓ ÚNICO AUTORIZADO |
| `/schedule` (sin --confirm) | ✗ solo lectura |
| `/queue` | ✗ solo lectura |
| `/week` | ✗ no llama Buffer |
| `/auto-week` | ✗ no llama Buffer |
| `/today` | ✗ no llama Buffer |
| `/write` | ✗ no llama Buffer |
| `/review` | ✗ no llama Buffer |
| `/approve` | ✗ no llama Buffer |
| `/harvest` | ✗ no llama Buffer |
| `/reply` | ✗ nunca publica |
