---
status: approved
visibility: editorial
last_updated: 2026-09-05
source_type: human_approved
---

# Guía de Buenas Prácticas — @autopromotorn

**Cuándo leer esto:** al crear, mover, renombrar o eliminar archivos. No en cada sesión de contenido — es una referencia de gobierno, no contexto de arranque.

---

## 1. Árbol canónico de directorios

```
autopromotorn/
│
├── CLAUDE.md                  ← arranque: identidad + reglas críticas + navegación
├── README.md                  ← descripción pública del repositorio
│
├── .claude/
│   ├── commands/              ← comandos / skills de Claude Code (un archivo por comando)
│   ├── skills/                ← skills específicos de @autopromotorn (versionados)
│   └── settings.json          ← permisos y configuración MCP
│
├── knowledge/                 ← datos canónicos aprobados del proyecto
│   ├── README.md              ← gobierno del conocimiento (arquitectura, precedencia, protocolo)
│   ├── VALIDATED_CONTEXT_*.md ← fuente de verdad del protagonista (solo el más reciente es activo)
│   ├── FINANCES.md, MORTGAGE.md, INVESTMENTS.md, HOUSE.md, TIMELINE.md, PROJECT.md
│   ├── CONTENT_PILLARS.md, CADENCIA.md, EDITORIAL_RULES.md, STRATEGY.md, AUDIENCE.md
│   └── technical/             ← CTE, changelog de obra, preguntas técnicas y solicitudes de docs
│
├── editorial/                 ← metodología creativa (voz, formatos, hooks, marcos)
│   ├── VOICE.md               ← tono, estilo, ejemplos, lo que nunca hacer
│   ├── FORMATS.md             ← 4 formatos narrativos
│   ├── HOOKS.md               ← fórmulas de apertura
│   ├── ANGLES.md              ← ángulos para generar ideas
│   ├── REPLIES.md             ← protocolo de replies estratégicos
│   ├── PILARES_32_TWEETS.md   ← banco de 32 tweets organizados en 8 pilares
│   ├── VIDEO_WORKFLOW.md      ← proceso de análisis de vídeos
│   └── BIBLIOTECA_INTELECTUAL_AUTOPROMOTORN_V2.md  ← marcos conceptuales (on-demand, 58 KB)
│
├── agents/                    ← definición de agentes especializados
│   ├── WRITER.md, CRITIC.md, HARVESTER.md, REPLY.md
│   ├── FORUM_SCOUT.md, arquitectoasesortecnico.md
│
├── content/                   ← pipeline de contenido (flujo activo)
│   ├── ideas/                 ← ideas sin desarrollar (IDEA-{tipo}-{ID}.md)
│   ├── drafts/                ← borradores en evaluación (draft-{slug}-YYYY-MM-DD.md)
│   ├── ready/                 ← aprobados, pendientes de programar (ready-{slug}-YYYY-MM-DD.md)
│   ├── scheduled/             ← programados en Buffer (SEMANA-YYYY-MM-DD.md)
│   ├── published/             ← historial canónico de publicados
│   └── planning/              ← candidatos por periodo (MMMM_YYYY_CANDIDATOS.md)
│
├── contenido/                 ← LEGACY — CONGELADO. No modificar sin autorización expresa.
│
├── sources/                   ← fuentes procesadas por HARVESTER y FORUM_SCOUT
│   ├── newsletters/, x/, forum/, youtube/, web/, podcasts/
│   └── SUBSCRIPTIONS.md       ← registro de fuentes activas
│
├── inbox/                     ← entrada de material sin procesar
│   ├── notes/, photos/, articles/, youtube/
│
├── docs/                      ← documentación del proyecto (privada y pública)
│   ├── diario-obra.md         ← log de la construcción — actualizar cada semana
│   ├── hipoteca/              ← docs hipotecarios (excluidos de git)
│   ├── presupuestos-construccion/ ← PDFs (excluidos de git)
│   ├── fotos-reales/          ← fotos de obra (excluidas de git)
│   └── [otros docs privados]
│
├── metrics/                   ← métricas y experimentos editoriales
│   ├── README.md, EXPERIMENTS.md, BUFFER_BASELINE_*.md
│
└── scripts/                   ← scripts de procesamiento
    ├── analizar_video.py      ← descarga transcripciones YouTube → sources/youtube/
    └── analizar_articulo.py   ← extrae contenido de artículos → sources/newsletters/
```

---

## 2. Reglas de naming

| Tipo de archivo | Patrón | Ejemplo |
|---|---|---|
| Borrador nuevo | `draft-{slug}-YYYY-MM-DD.md` | `draft-excavacion-coste-2026-09-05.md` |
| Listo para publicar | `ready-{slug}-YYYY-MM-DD.md` | `ready-excavacion-coste-2026-09-05.md` |
| Programado (semana) | `SEMANA-YYYY-MM-DD.md` | `SEMANA-2026-09-07.md` |
| Idea sin desarrollar | `IDEA-{tipo}-{ID}.md` | `IDEA-HAR-20260901-001.md` |
| Idea de foro | `FORUM-{FECHA}-{NNN}.md` | `FORUM-20260901-003.md` |
| Candidatos mensuales | `{MES}_YYYY_CANDIDATOS.md` | `SEPTIEMBRE_2026_CANDIDATOS.md` |
| Contexto validado | `VALIDATED_CONTEXT_YYYY-MM-DD.md` | Solo uno activo a la vez |
| Snapshot de fuente | `YYYY-MM-DD-{fuente}.md` | `2026-08-31-tubau-newsletter.md` |

**Regla general:** fechas siempre en formato `YYYY-MM-DD`. Slugs en minúsculas con guiones.

---

## 3. Dónde va cada tipo de contenido

| Qué | Dónde | Cuándo mover al siguiente estadio |
|---|---|---|
| Referencia normativa oficial | `knowledge/technical/{norma}/` | Tras verificar vigencia, fuente y alcance |
| Fuente externa procesada | `sources/{tipo}/` | Tras ejecutar HARVESTER |
| Idea extraída de fuente | `content/ideas/` | Tras /ideas o FORUM_SCOUT |
| Borrador en evaluación | `content/drafts/` | Tras /write + /review |
| Aprobado | `content/ready/` | Tras /approve |
| Programado en Buffer | `content/scheduled/` | Tras /schedule |
| Publicado | `content/published/` | Tras confirmar publicación |

---

## 4. Cuándo crear archivo nuevo vs. actualizar existente

**Actualizar existente si:**
- El dato ya existe en el archivo canónico (FINANCES.md, MORTGAGE.md, etc.) y solo ha cambiado
- Es una corrección menor de un borrador en draft/

**Crear archivo nuevo si:**
- Es un nuevo borrador (siempre un archivo por borrador en drafts/)
- Es una nueva semana de planificación (SEMANA-*.md)
- Es un nuevo snapshot de conocimiento validado

**No crear archivo nuevo si:**
- El contenido ya existe en otro archivo — actualizar el existente
- Es solo navegación o índice — actualizar knowledge/README.md

---

## 5. Política de eliminación de archivos

Antes de eliminar cualquier archivo, clasificarlo:

| Clasificación | Criterio | Acción |
|---|---|---|
| **Idéntico** | Mismo hash MD5 que un archivo canónico | Eliminar — el canónico lo sustituye |
| **Sustituido** | Versión anterior de un documento activo, con `supersedes:` en el nuevo | Eliminar — Git conserva el historial |
| **Obsoleto** | Versión antigua sin sustituto directo, funcionalidad ya no activa | Eliminar con nota en el commit |
| **Divergente** | Mismo nombre, contenido diferente | Verificar cuál es el activo antes de actuar |
| **Único** | Contenido no encontrado en ningún otro archivo | **No eliminar** — migrar primero |

**Regla de eliminación:**
1. Clasificar el archivo (ver tabla)
2. Confirmar que el contenido está en Git (o que no es necesario)
3. Eliminar en **commit independiente** con mensaje descriptivo
4. Nunca mezclar eliminaciones con cambios de contenido

**LEGACY intocable:** `contenido/` está congelado. No borrar, mover ni modificar sin autorización expresa del usuario.

---

## 6. Política de skills

- Los skills de @autopromotorn viven en `.claude/skills/{nombre}/SKILL.md`
- Cada skill necesita frontmatter YAML válido: `name`, `description`, `tools`
- Para añadir un skill nuevo: crear carpeta + SKILL.md, verificar en sesión nueva
- Para retirar un skill: primero confirmar que no está en uso, luego eliminar

---

## 7. Checklist de sesión

### Al iniciar una sesión de contenido
- [ ] ¿Hay novedades de obra que documentar? (actualizar `docs/diario-obra.md`)
- [ ] ¿Hay material nuevo en `inbox/`? (procesar con `/harvest` si aplica)
- [ ] ¿Qué está pendiente en `content/ready/` y `content/scheduled/`?

### Al crear contenido
- [ ] Deduplicación en las 5 fuentes (ver CLAUDE.md §Reglas críticas)
- [ ] Datos verificados en `knowledge/VALIDATED_CONTEXT_2026-08-31.md` antes de publicar cifras
- [ ] Voz revisada si es la primera pieza de la sesión (`editorial/VOICE.md`)

### Al terminar una sesión
- [ ] Nuevos borradores guardados en `content/drafts/`
- [ ] `docs/diario-obra.md` actualizado si hubo novedades de obra
- [ ] Commit de cambios con mensaje descriptivo

---

## 8. Señales de que la estructura necesita revisión

Abrir esta guía y revisar si se cumple alguno de estos síntomas:

- Hay más de 1 archivo `VALIDATED_CONTEXT_*.md` activo
- Hay borradores en `contenido/borradores/` que no están en `content/drafts/`
- Hay archivos de contenido en la raíz del proyecto
- Un skill no aparece en una sesión nueva
- Un comando devuelve error de referencia a archivo inexistente
- `knowledge/README.md` referencia archivos que ya no existen
