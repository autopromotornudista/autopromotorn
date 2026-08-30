# /queue

Dashboard de estado del pipeline de contenido de @AutopromotorN.

Solo lectura. No mueve archivos. No llama a Buffer.

---

## Proceso

1. Leer el estado de todos los archivos en:
   - `content/ideas/`
   - `content/drafts/`
   - `content/ready/`
   - `content/scheduled/`
   - `content/published/` (últimas 2 semanas)

2. Para cada draft en `content/drafts/`, leer el frontmatter y extraer:
   - `critic_status` (pending | PASS | REVISE | REJECT)
   - `risk_level` (low | review)
   - `draft_date`
   - `pillar`

3. Para cada archivo en `content/ready/`, leer:
   - `approved_date`
   - `critic_override` (true | false)
   - `pillar`

4. Para cada archivo en `content/scheduled/`, leer:
   - `scheduled_at`
   - `buffer_post_id` (si existe)

5. Consultar Buffer MCP para verificar posts programados:
   - `mcp__buffer__get_account` → organizationId
   - `mcp__buffer__list_posts` → posts pending en la cola

---

## Formato del informe

```
══════════════════════════════════════════════════
PIPELINE — @AutopromotorN — [fecha actual]
══════════════════════════════════════════════════

IDEAS DISPONIBLES ([N])
  [idea_id]  [pillar]  [hook_seed truncado a 50 chars]  [needs_verification]
  ...
  → Siguiente: /write [idea_id]

──────────────────────────────────────────────────
DRAFTS ([N])
  [draft_id]  [pillar]  [risk_level]  critic: [PASS|REVISE|REJECT|pending]  value: [HIGH|MEDIUM|LOW|-]
  ...
  → PASS + value HIGH listo para /approve · pending/REVISE/REJECT/LOW requieren /review

──────────────────────────────────────────────────
READY ([N]) — esperando /schedule humano
  [ready_id]  [pillar]  aprobado: [fecha]  value: HIGH  override: [true|false]
  ...

──────────────────────────────────────────────────
PROGRAMADO EN BUFFER ([N])
  [scheduled_id]  [fecha/hora CET]  buffer_id: [id]
  ...

──────────────────────────────────────────────────
PUBLICADO — últimas 2 semanas ([N])
  [fecha]  [resumen del post]
  ...

══════════════════════════════════════════════════
RESUMEN: [N] ideas · [N] drafts · [N] ready · [N] en buffer
ACCIÓN INMEDIATA SUGERIDA: [siguiente paso más urgente]
──────────────────────────────────────────────────
⚠ Piezas con value MEDIUM o LOW no pueden avanzar a /approve hasta /review con mejora.
══════════════════════════════════════════════════
```
