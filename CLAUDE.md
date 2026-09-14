# Autopromotor Nudista — @autopromotorn

## Identidad

- **Cuenta:** @autopromotorn en X (Twitter)
- **Nombre:** Autopromotor Nudista
- **Bio:** "Viajando en pañales… mostrarlo todo en tiempo real"
- **Concepto:** build-in-public auténtico sobre autopromoción de vivienda en España
- **Email:** autopromotornudista@gmail.com

---

## Principio editorial — Skin in the game

**Todo el contenido se escribe desde la experiencia propia vivida. Sin excepción.**

- Cada tweet parte de "nosotros hicimos esto" o "a nosotros nos pasó esto" — nunca de "deberías hacer esto"
- Los números son siempre los números reales del proyecto (no cálculos teóricos)
- El consejo llega DESPUÉS de contar la experiencia, no antes

**Fórmula base:** `[Situación real propia] → [Dato concreto] → [Lo que aprendimos] → [Pregunta o CTA]`

**Correcto:** "Firmamos la hipoteca a 2,05%. Así lo conseguimos."  
**Incorrecto:** "Así deberías negociar tu hipoteca."

---

## Reglas críticas — siempre activas

1. **Voz plural:** todo el contenido usa "nosotros" — contratamos, decidimos, firmamos. Nunca singular.
2. **Sin nombres de empresas:** "el constructor", "el banco", "nuestro fondo monetario". Nunca nombres propios.
3. **Sin datos inventados:** si falta un dato real, preguntar. Nunca estimar ni sustituir con IA.
4. **Deduplicación obligatoria** — antes de generar contenido revisar en este orden:
   1. `content/published/`
   2. `contenido/tweets-publicados.md` (LEGACY)
   3. `content/ready/` · `content/scheduled/`
   4. `content/planning/` (READY/SCHEDULED = ya utilizado)
   5. `content/drafts/`
5. **LEGACY intocable:** nunca borrar, mover ni modificar `contenido/` sin autorización expresa.
6. **Al reorganizar archivos:** leer `knowledge/GUIA_BUENAS_PRACTICAS.md` antes de actuar.

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

### IDs estables

- Posts: `content_id: DRAFT-YYYYMMDD-NNN` en frontmatter (inmutable al mover entre directorios)
- Replies: `reply_id: REPLY-YYYYMMDD-NNN` en content/replies/

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

Claude NO puede hacer sin aprobación humana explícita:
- `/approve` — el gate humano es inviolable
- `/schedule --confirm` — el único punto que llama a `create_post` en Buffer
- `/approve-reply` — gate humano para replies
- Mover archivos a `content/ready/` sin /approve
- Actualizar `knowledge/` silenciosamente

---

## NAVEGACIÓN — cuándo leer cada archivo

### Escribir contenido
| Archivo | Para qué |
|---------|---------|
| `knowledge/VALIDATED_CONTEXT_2026-08-31.md` | **Siempre primero** — fuente de verdad del proyecto |
| `editorial/VOICE.md` | Tono, estilo, lo que nunca hacer |
| `editorial/FORMATS.md` | Los 4 formatos narrativos (contraste, desnudo, error, historia) |
| `editorial/HOOKS.md` | Fórmulas de apertura |
| `editorial/ANGLES.md` | Ángulos para generar ideas |
| `editorial/PILARES_32_TWEETS.md` | Banco de 32 tweets organizados por pilar |
| `knowledge/CONTENT_PILLARS.md` | Pilares, días, objetivos y límites |
| `knowledge/CADENCIA.md` | Volumen semanal, Value Gate, horarios óptimos |
| `knowledge/technical/CTE/README.md` | CTE: mapa, fuentes oficiales y protocolo normativo |

### Datos del proyecto
| Archivo | Para qué |
|---------|---------|
| `knowledge/FINANCES.md` | Costes, partidas, presupuesto |
| `knowledge/MORTGAGE.md` | Hipoteca, condiciones, proceso |
| `knowledge/INVESTMENTS.md` | Cartera, relación hipoteca/inversión |
| `knowledge/HOUSE.md` | Vivienda, decisiones de diseño |
| `knowledge/TIMELINE.md` | Cronología oficial del proyecto |
| `knowledge/PROJECT.md` | Identidad, posicionamiento, situación actual |
| `docs/diario-obra.md` | Estado actual de la obra — leer antes del contenido de jueves |
| `docs/hipoteca/guia_definitiva_hipoteca_autopromotor.md` | Experiencia hipotecaria completa |

### Hacer replies
| Archivo | Para qué |
|---------|---------|
| `editorial/REPLIES.md` | Protocolo de sesión de replies |
| `knowledge/STRATEGY.md` | Señales del algoritmo, cuentas objetivo, regla 70/30 |

### Planificar semana
| Archivo | Para qué |
|---------|---------|
| `content/planning/` | Candidatos de contenido por periodo |
| `content/scheduled/` · `content/ready/` | Ver qué está programado o listo |

### Gobierno y arquitectura del sistema
| Archivo | Para qué |
|---------|---------|
| `knowledge/README.md` | Arquitectura PRIVATE→KNOWLEDGE→PUBLIC, precedencia de fuentes |
| `knowledge/EDITORIAL_RULES.md` | Reglas operativas completas de aprobación y publicación |
| `knowledge/GUIA_BUENAS_PRACTICAS.md` | Naming, dónde va cada archivo, política de eliminación |
