@AGENTS.md

# Claude Code — específico de este proyecto

Las normas generales, la estructura, los comandos y las puertas humanas están en `AGENTS.md`. Esta sección recoge solo lo que depende de Claude Code: sus comandos slash, sus conexiones MCP y su alcance de autonomía.

---

## Herramientas conectadas

- **Buffer MCP** — programar tweets: `claude mcp add --transport http buffer https://mcp.buffer.com/mcp`
- **XMCP** (pendiente) — leer nicho en X: requiere developer account

---

## Sistema editorial MVP2 — Autonomía ampliada

### Nuevos comandos

| Comando | Propósito | Llama Buffer |
|---------|-----------|-------------|
| `/prepare` | Pipeline completo: forum-scout + auto-week + /inbox | NO |
| `/inbox` | Bandeja unificada de aprobación (posts + replies) con slots propuestos | Solo lectura |
| `/status` | Métricas Buffer + reconciliación + estado del pipeline | Solo lectura |
| `/instagram-adapt [id|ruta]` | Adapta una pieza a carrusel, reel o imagen | NO |
| `/instagram-review [IG-id]` | Revisión factual, visual y de privacidad | NO |
| `/instagram-inbox` | Bandeja específica de Instagram | Solo lectura |
| `/instagram-approve [IG-id]` | Gate humano con hash del paquete y activos | NO |
| `/instagram-schedule [IG-id]` | Preview o programación autorizada | Solo con `--confirm` |
| `/instagram-metrics [csv]` | Lectura o importación de métricas | Solo lectura |
| `/approve-reply [reply_id]` | Gate humano para aprobar un reply guardado | NO |
| `/sent-reply [reply_id]` | Registrar que un reply fue publicado manualmente | NO |

### Comandos mejorados

| Comando | Cambio |
|---------|--------|
| `/approve [id1] [id2]...` | Acepta múltiples IDs en batch. Calcula y registra `content_hash` SHA256. |
| `/write` | Genera `content_id: DRAFT-YYYYMMDD-NNN` estable en cada draft |
| `/reply` | Persiste propuestas en `content/replies/pending/` |
| `/schedule --confirm` | Verifica hash SHA256 antes de llamar Buffer — bloquea si el texto cambió |
| `/queue` | Incluye reconciliación con Buffer (OK / WARN por buffer_post_id) |

### Aprobación única — regla de oro

Cuando el propietario dice **"apruebo [N]"** en el contexto de `/inbox` (que ya mostró texto + canal + slot propuesto), Claude ejecuta automáticamente y sin preguntar de nuevo:
1. `/approve [content_id]` — calcula hash, mueve a ready/
2. `/schedule [content_id] --confirm` — verifica hash, llama Buffer con el slot propuesto

Si el hash no coincide: bloqueo automático, no es una pregunta al usuario.

### Directorios nuevos

- `content/replies/pending/` — propuestas de /reply sin aprobar
- `content/replies/approved/` — aprobadas, pendientes de envío manual
- `content/replies/sent/` — enviadas manualmente
- `logs/` — audit.log, background.log, pipeline_snapshot.json (no versionados en Git)
- `content/instagram/` — paquetes drafts → ready → scheduled → published enlazados a sus fuentes

### Automatización en segundo plano

`scripts/background_runner.sh` se ejecuta vía systemd user timer cada 24h.
Detecta posts overdue, actualiza pipeline snapshot y rota logs.
**No llama a Claude. No llama a Buffer. Sin decisiones editoriales.**

Activación: `systemctl --user enable --now autopromotorn-runner.timer`

### Alcance de autonomía de Claude

Claude puede ejecutar sin pedir confirmación:
- Lecturas de cualquier archivo del repositorio
- Validaciones y detección de duplicados
- Generación de borradores (/write, /auto-week, /forum-scout)
- Revisión automática (/review)
- Audit log y pipeline snapshots
- Preview de slots en /schedule (sin --confirm)

Claude NO puede hacer sin aprobación humana explícita (ver "Puertas humanas" en `AGENTS.md`):
- `/approve` — el gate humano es inviolable
- `/schedule --confirm` — el único punto que llama a `create_post` en Buffer
- `/approve-reply` — gate humano para replies
- Mover archivos a `content/ready/` sin /approve
- Actualizar `knowledge/` silenciosamente
