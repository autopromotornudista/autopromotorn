---
status: approved
visibility: editorial
last_updated: 2026-08-29
source_type: human_approved
---

# VIDEO_WORKFLOW.md — Pipeline YouTube → content/ideas/

Pipeline actual para procesar vídeos de YouTube como fuente de contenido para @autopromotorn.

> **Nota de evolución:** Este workflow es específico de vídeo por ahora. El objetivo futuro es integrarlo en un HARVEST_WORKFLOW común para newsletters, web, YouTube y podcasts. Cuando se implemente el Harvester completo, este archivo pasará a ser una sección de ese flujo unificado.

Fuente: curado desde `docs/flujo-analisis-videos.md`.

---

## Flujo completo

```
YouTube URL
    ↓
python3 scripts/analizar_video.py "URL" "Título"
    ↓
sources/youtube/YYYY-MM-DD-slug.md        ← canónico desde ahora
(docs/fuentes/ = ubicación legacy anterior)
    ↓
Claude genera 3-5 ángulos
    ↓
Deduplicación obligatoria
    ↓
content/ideas/IDEA-NNN.md (con provenance)
    ↓
Writer → Critic → Human Review → Buffer
```

---

## Paso 1 — Ejecutar el script

```bash
# Desde el directorio del proyecto:
python3 scripts/analizar_video.py "https://youtu.be/XXXX"

# Con título (recomendado para identificar el archivo fácilmente):
python3 scripts/analizar_video.py "https://youtu.be/XXXX" "Nombre del vídeo o podcast"
```

El script guarda automáticamente la transcripción en `sources/youtube/YYYY-MM-DD-slug.md` con el siguiente frontmatter:

```
URL | ID vídeo | Fecha de análisis | Idioma transcripción
```

**Dependencia requerida:**
```bash
pip install youtube-transcript-api
```

---

## Paso 2 — Pedir ángulos a Claude

Con el archivo de transcripción generado:

> "Genera ángulos de contenido para @autopromotorn a partir del archivo sources/youtube/[nombre-del-archivo].md"

Claude leerá la transcripción junto con el briefing del proyecto, `editorial/HOOKS.md`, `editorial/FORMATS.md` y los datos reales de `knowledge/` para proponer 3-5 ángulos conectados con la experiencia propia.

---

## Qué incluye cada ángulo

| Campo | Descripción |
|-------|------------|
| **Pilar** | 💶 Números · 🏗️ Proceso · 💡 Lecciones · 🧠 Reflexiones |
| **Dato clave del vídeo** | El detonante extraído de la fuente |
| **Conexión con el caso propio** | Cómo enlaza con experiencia real o datos de `knowledge/` |
| **Formato sugerido** | Tweet único, hilo 5-8, reflexión + pregunta |
| **Tipo de contenido** | FACT / INSIGHT / FRAMEWORK (ver `sources/SUBSCRIPTIONS.md`) |

---

## Paso 3 — Deduplicación obligatoria

Antes de pasar cualquier ángulo a `content/ideas/`, revisar en este orden:

1. `content/published/`
2. `contenido/tweets-publicados.md`
3. `content/ready/` y `content/scheduled/`
4. Archivos de mes vigente en `knowledge/`
5. `content/drafts/`

**Qué evitar repetir:** misma experiencia · mismo hook · mismo marco · misma conclusión.

---

## Paso 4 — Guardar en content/ideas/

Cada ángulo aprobado para desarrollo se guarda como `content/ideas/IDEA-NNN.md` con provenance completo:

```yaml
---
idea_id: IDEA-NNN
source_id: [SRC-XXX de SUBSCRIPTIONS.md, si es fuente recurrente]
source_name: [nombre del vídeo o canal]
author: [nombre del autor del vídeo]
url: [URL del vídeo]
date_published: [fecha del vídeo]
date_harvested: [fecha de hoy]
type: youtube
content_type_extracted: [FACT | INSIGHT | FRAMEWORK | IDEA | STORY]
concept_original: [qué decía la fuente]
transformation: [cómo se conecta con la experiencia propia]
pillar: [pilar editorial]
format_sugerido: [tweet | hilo | reflexión]
status: idea
needs_attribution: [true | false]
needs_verification: [true | false]
originality_check: pending
---
```

---

## Errores frecuentes y soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| "Transcripciones desactivadas" | El autor del vídeo las desactivó | Añadir URL directamente a NotebookLM |
| "No se pudo extraer el ID" | URL con formato raro | Copiar la URL desde la barra del navegador |
| Transcripción en inglés | El vídeo solo tiene subtítulos en inglés | El script lo indica — la transcripción es igualmente usable |

---

## Archivos generados

| Directorio | Contenido |
|-----------|-----------|
| `sources/youtube/` | Transcripciones de vídeos procesados (canónico desde ahora) |
| `docs/fuentes/` | Transcripciones legacy — conservar intactas, no modificar |

Los archivos se acumulan como base de conocimiento de fuentes externas analizadas. No son `knowledge/` — son materia prima que requiere transformación editorial.
