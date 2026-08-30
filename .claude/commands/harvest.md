# /harvest

HARVESTER AGENT — Procesa `$ARGUMENTS` (URL o texto de experiencia propia).

Puede escribir en: `sources/` · `content/ideas/` · `inbox/notes/`
NUNCA escribe en: `knowledge/` · `editorial/` · `content/drafts/` · Buffer

---

## Paso 0 — Identificar tipo de entrada

Si `$ARGUMENTS` es una URL:
- `youtube.com` o `youtu.be` → tipo: youtube
- `substack.com` o dominio con indicios de newsletter → tipo: newsletter
- Otro dominio → tipo: web
- `x.com` o `twitter.com` → tipo: x

Si `$ARGUMENTS` es texto (sin URL) → tipo: experience

---

## Paso 1 — Verificar autorización de la fuente

**Para URLs (tipos: youtube, newsletter, web, x):**

Comprobar si la URL corresponde a una fuente en `sources/SUBSCRIPTIONS.md`.

- Si está registrada → fuente autorizada, continuar.
- Si NO está registrada → la ejecución manual de /harvest YA constituye autorización para procesar esta URL como `ad_hoc`.
  - NO añadir automáticamente a SUBSCRIPTIONS.md.
  - Anotar `source_type: ad_hoc` en las ideas generadas.
  - Al finalizar, preguntar: "¿Quieres registrar esta fuente como recurrente en SUBSCRIPTIONS.md?"

**Para experiencias propias:** no requiere verificación de fuente.

---

## Paso 2 — Extraer el contenido

**YouTube:**
```bash
python3 scripts/analizar_video.py "$URL" "$TITULO_OPCIONAL"
```
El script genera en `docs/fuentes/[fecha]-[id].md`.
Después mover el archivo a `sources/youtube/[fecha]-[id].md`.
Confirmar la ruta final antes de continuar.

**Newsletter / Substack:**
```bash
python3 scripts/analizar_articulo.py "$URL" "$TITULO_OPCIONAL"
```
El script detecta el tipo y escribe en `sources/newsletters/` o `sources/web/`.
Confirmar la ruta generada.

**Web genérica:**
```bash
python3 scripts/analizar_articulo.py "$URL" "$TITULO_OPCIONAL"
```
Escribe en `sources/web/`.

**Experiencia propia:**
Guardar el texto en `inbox/notes/[YYYY-MM-DD]-[slug].md` con metadatos mínimos:
```
date: YYYY-MM-DD
type: personal_experience
pillar_hint: [pilar más probable]
```

---

## Paso 3 — Analizar el contenido extraído

Leer el archivo generado en `sources/`.

Aplicar el flujo de `editorial/VIDEO_WORKFLOW.md` (para vídeos) o `editorial/ANGLES.md` (para artículos y experiencias).

Clasificar cada fragmento relevante como:
- `FACT` — dato externo verificable (needs_verification: true si es crítico)
- `INSIGHT` — interpretación u opinión del autor de la fuente
- `FRAMEWORK` — estructura mental reutilizable
- `STORY` — anécdota o narrativa (nunca presentar como propia)
- `DERIVED_CLAIM` — conclusión que combina hechos (needs_verification: true siempre)

Descartar:
- Contenido promocional (cursos, servicios, afiliados)
- Datos sin conexión con ningún pilar editorial de @AutopromotorN
- Experiencias de terceros que no puedan conectarse con experiencia propia verificada

---

## Paso 4 — Verificar deduplicación

Antes de crear ideas, buscar si el ángulo ya existe en:
1. `content/ideas/`
2. `content/published/`
3. `contenido/tweets-publicados.md`
4. `content/drafts/`

Si el ángulo ya existe: documentar que se descartó y por qué.
Una nueva fuente puede enriquecer una idea existente en lugar de crear una nueva.

---

## Paso 5 — Generar ideas

Crear entre 1 y 5 archivos `content/ideas/IDEA-[TIPO]-NNN.md`.

El NNN debe seguir la numeración existente en `content/ideas/`.

Frontmatter obligatorio de cada idea:
```yaml
---
idea_id: IDEA-[TIPO]-NNN
source_id: [SRC-NNN o ad_hoc]
source_file: sources/[ruta al archivo]
content_type: FACT | INSIGHT | FRAMEWORK | STORY | DERIVED_CLAIM
pillar: [pilar editorial]
hook_seed: [primera frase candidata]
needs_verification: true | false
needs_human_review: false  # true si hay derived claims o datos financieros externos
generated: YYYY-MM-DD
status: pending
---
```

---

## Paso 6 — Actualizar SUBSCRIPTIONS.md (solo si fuente registrada)

Si la fuente está en SUBSCRIPTIONS.md, actualizar:
- `last_processed: YYYY-MM-DD`
- `ideas_generated: +N`

NO modificar si es `ad_hoc`.

---

## Paso 7 — Informe final

Mostrar:
```
══════════════════════════════════════
HARVEST REPORT — [fuente]
══════════════════════════════════════
Tipo:          youtube | newsletter | web | experience | ad_hoc
Archivo fuente: sources/[ruta]
Ideas generadas: N
  ✓ IDEA-VID-004  [hook seed]
  ✓ IDEA-VID-005  [hook seed]
Descartadas: N
  ✗ [razón 1]
  ✗ [razón 2]
Fuente registrada: SRC-NNN | ad_hoc
──────────────────────────────────────
Siguiente paso: /write IDEA-[TIPO]-NNN
══════════════════════════════════════
```

Si `ad_hoc`: preguntar al final si añadir a SUBSCRIPTIONS.md.
