---
status: approved
visibility: editorial
last_updated: 2026-08-31
source_type: human_approved
---

# knowledge/ — Índice de conocimiento aprobado

## Propósito

Este directorio contiene el conocimiento canónico y aprobado para uso editorial de @autopromotorn.

Es la **única fuente de verdad** para Claude Code, ChatGPT y OpenClaw cuando generan, revisan o programan contenido.

**No es un almacén general.** Solo entra lo que ha pasado por el proceso completo:

```
SOURCE → extracción → validación → aprobación humana → KNOWLEDGE
```

### Regla fundamental

**Existir en un archivo versionado del repositorio NO equivale a estar aprobado para knowledge.**

Un dato puede estar en `docs/`, `contenido/` o cualquier otro archivo del repo y seguir siendo privado, provisional o no editorial. Knowledge solo contiene lo que ha sido explícitamente aprobado como conocimiento editorial.

Knowledge nunca debe utilizarse para reconstruir información privada que se ha decidido deliberadamente excluir.

---

## Arquitectura de tres niveles

```
PRIVATE SOURCES     → solo en disco local (docs/ privados, Google Drive)
KNOWLEDGE APPROVED  → aquí, en knowledge/ (datos editoriales autorizados)
PUBLIC CONTENT      → content/published/ y canales sociales
```

---

## Mapa de archivos

| Archivo | Qué contiene | Cuándo consultarlo |
|---------|-------------|-------------------|
| `VALIDATED_CONTEXT_2026-08-31.md` | **Contexto completo validado por el protagonista. Versión 1.1 (31/08/2026). Fuente de verdad más reciente. Prevalece sobre todos los documentos anteriores.** | SIEMPRE — leer primero |
| `VALIDATED_CONTEXT_2026-08-30.md` | Snapshot histórico v1.0. Conservado como referencia. Usar solo si se necesita rastro de cambios. | No usar como fuente activa |
| `PROJECT.md` | Identidad, propósito, posicionamiento, filosofía | Antes de cualquier tarea editorial |
| `TIMELINE.md` | Cronología oficial confirmada del proyecto | Cuando el contenido haga referencia a fechas o hitos |
| `HOUSE.md` | Características de la vivienda, decisiones de diseño | Posts sobre proceso real, decisiones constructivas |
| `FINANCES.md` | Estructura económica aprobada, cifras y partidas detalladas | Posts sobre costes, presupuesto, decisiones financieras |
| `MORTGAGE.md` | Condiciones hipotecarias, proceso, aprendizajes | Posts sobre hipoteca, negociación, bancos |
| `INVESTMENTS.md` | Estrategia de inversión, relación hipoteca/cartera | Posts sobre inversión, amortización, patrimonio |
| `AUDIENCE.md` | Perfiles, miedos, preguntas, nivel de conocimiento | Para orientar el enfoque y el ángulo del contenido |
| `STRATEGY.md` | Canales, función de cada uno, monetización | Decisiones de distribución y canal |
| `CONTENT_PILLARS.md` | Pilares temáticos y operativos, objetivos, límites | Planificación de contenido semanal |
| `EDITORIAL_RULES.md` | Reglas operativas, aprobación, deduplicación | Antes de publicar o programar cualquier contenido |
| `CADENCIA.md` | Cadencia, volumen semanal, Value Gate, horarios | Planificación y calendarización |

---

## Regla de precedencia

**Cuando exista conflicto entre un documento histórico del repositorio y una declaración humana posterior explícitamente aprobada, prevalece la declaración humana posterior.**

Esta regla aplica a todos los archivos de `knowledge/`. Una declaración aprobada en sesión tiene prioridad sobre `BIBLIOTECA_INTELECTUAL_V2.md`, `guia-redaccion.md`, `CLAUDE.md` y cualquier documento histórico anterior.

---

## Protocolo de actualización

1. Cualquier actualización de knowledge requiere autorización humana explícita.
2. Cada actualización debe registrarse con `last_updated` en el frontmatter.
3. Las actualizaciones se consolidan en un commit separado, nunca mezcladas con contenido.
4. Si un dato de una fuente autorizada contradice lo que hay en knowledge, señalarlo — no sobreescribir unilateralmente.

---

## Qué NO entra en knowledge

- Borradores de posts
- Calendarios mensuales
- Bancos de ideas (van a `content/ideas/`)
- Historial de tweets publicados (va a `content/published/`)
- Datos privados de documentos excluidos de Git
- Investigación externa sin filtro editorial
- Hooks, frameworks, plantillas creativas y voz editorial (viven en `editorial/`)
- Cualquier dato no aprobado explícitamente, aunque exista en el repositorio

> **VOICE.md** ha migrado a `editorial/VOICE.md` (2026-08-30). La voz y el tono son metodología creativa, no hechos del proyecto.
