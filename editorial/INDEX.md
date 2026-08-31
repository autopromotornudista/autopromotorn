---
status: approved
visibility: editorial
last_updated: 2026-08-31
source_type: human_approved
---

# editorial/ — Metodología creativa de @autopromotorn

## Propósito

La capa editorial contiene los marcos creativos, fórmulas de escritura y metodología operativa de la cuenta.

**No es `knowledge/`:** no contiene hechos ni datos del proyecto.
**No es `content/`:** no contiene borradores ni posts listos para publicar.
**No es `sources/`:** no contiene materia prima externa.

---

## Las cuatro capas del sistema

```
knowledge/   → hechos y reglas aprobadas — la verdad del proyecto
editorial/   → metodología creativa — cómo transformar hechos en contenido
sources/     → materia prima externa — transcripciones, artículos, newsletters
content/     → ideas, drafts, ready, scheduled, publicados
```

| Capa | Qué contiene | Quién puede escribir en ella |
|------|-------------|------------------------------|
| `knowledge/` | Datos canónicos aprobados | Solo con aprobación humana explícita |
| `editorial/` | Marcos creativos y metodología | Solo con aprobación humana explícita |
| `sources/` | Fuentes externas procesadas | Harvester (scripts + Claude) |
| `content/ideas/` | Ideas derivadas con provenance | Harvester (Claude) |
| `content/drafts/` | Borradores de posts | Writer (Claude + humano) |
| `content/published/` | Posts publicados | Solo registro manual post-publicación |

**Regla de separación estricta:** ninguna capa escribe directamente en otra. El Harvester escribe solo en `sources/` y `content/ideas/`. El Writer escribe solo en `content/drafts/`. Ningún agente escribe en `knowledge/` ni en `editorial/` sin aprobación humana.

---

## Mapa de archivos

| Archivo | Función | Cuándo consultarlo |
|---------|---------|-------------------|
| `VOICE.md` | Tono, ritmo, ejemplos buenos y malos, reglas de hashtag | Antes de redactar cualquier post — es el primer filtro de calidad |
| `HOOKS.md` | Fórmulas de apertura y estructuras de hook validadas | Antes de escribir la primera línea de cualquier post |
| `FORMATS.md` | Los 4 formatos narrativos + ejemplos por pilar | Al elegir cómo contar una experiencia o dato |
| `ANGLES.md` | Cómo generar ángulos distintos desde una misma experiencia o fuente | Al transformar un dato real o fuente externa en ideas |
| `REPLIES.md` | Estrategia de reply: estructura, timing, tipos de aportación | Antes de entrar en conversación activa en X |
| `VIDEO_WORKFLOW.md` | Pipeline YouTube → transcripción → ángulos → `content/ideas/` | Al procesar un vídeo como fuente de contenido |
| `REFERENCE.md` | Cuentas y creadores de referencia del nicho | Al buscar contexto de nicho o calibrar tono |

---

## BIBLIOTECA_INTELECTUAL_AUTOPROMOTORN_V2.md — fuente legacy de alto valor

`autopromotorn_claude_content_os/knowledge/BIBLIOTECA_INTELECTUAL_AUTOPROMOTORN_V2.md` es una fuente editorial legacy con valor acumulado: contiene 138 ideas, marcos y análisis históricos del proyecto.

**Tratamiento correcto:**
- No es `knowledge/` factual. Sus datos pueden estar desactualizados o superados por declaraciones posteriores aprobadas.
- No moverla, resumirla ni modificarla en esta fase.
- Su destino futuro es la capa `editorial/` como banco de frameworks y marcos creativos.
- Cuando se quiera extraer algo de ella para `editorial/`, requiere evaluación y aprobación humana.

**Regla de precedencia:** si algo en BIBLIOTECA_V2 contradice un archivo de `knowledge/`, prevalece `knowledge/`.

---

## Sistema HARVESTER — ingesta de fuentes externas

El sistema HARVESTER gestiona la captura de ideas desde fuentes externas antes de que lleguen a esta capa editorial.

| Herramienta | Entrada | Destino |
|-------------|---------|---------|
| `/harvest` | URL (YouTube, Substack, web, X) | `sources/` + `content/ideas/` |
| `/harvest-newsletter` | Texto pegado de newsletter | `content/ideas/inbox/` |

Las ideas capturadas por HARVESTER **nunca escriben directamente en `editorial/`**. Solo pasan a `editorial/` tras transformación aprobada por el usuario.

Ver `docs/HARVESTER.md` para la arquitectura completa del sistema.

---

## Protocolo de actualización

1. Cualquier actualización requiere autorización humana explícita.
2. Actualizar `last_updated` en el frontmatter del archivo modificado.
3. Los commits de `editorial/` van separados de los commits de `content/`.
4. Si una nueva declaración contradice algo en `editorial/`, señalarlo — no sobreescribir en silencio.
