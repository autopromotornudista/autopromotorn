# /write

WRITER AGENT — Genera un borrador a partir de `$ARGUMENTS` (idea_id).

Puede escribir en: `content/drafts/`
NUNCA escribe en: `knowledge/` · `editorial/` · `content/ready/` · `sources/` · Buffer

---

## Paso 0 — Validar la idea

Leer `content/ideas/$ARGUMENTS.md`.
Si no existe, reportar el error y detenerse.

Registrar del frontmatter:
- `source_id` y `source_file` (provenance)
- `content_type` (FACT | INSIGHT | FRAMEWORK | STORY | DERIVED_CLAIM)
- `pillar` (pilar editorial)
- `hook_seed` (punto de partida)
- `needs_verification`

---

## Paso 1 — Cargar knowledge relevante

Según el pilar de la idea, leer los archivos de `knowledge/` pertinentes:

| Pilar | Archivos a leer |
|-------|----------------|
| Números & Finanzas | FINANCES.md · INVESTMENTS.md · MORTGAGE.md |
| Proceso Real | HOUSE.md · TIMELINE.md |
| Lecciones & Tips | PROJECT.md + archivo más relevante al tema |
| Reflexiones & Contexto | PROJECT.md · AUDIENCE.md |
| Familia & Vida Real | PROJECT.md |
| Cualquier pilar | EDITORIAL_RULES.md (siempre) |

Marcar cada dato usado como `FACT: [archivo#sección]`.
NUNCA inventar datos. Si un dato no está en knowledge/, no usarlo.

---

## Paso 2 — Cargar metodología editorial

Leer obligatoriamente:
- `editorial/VOICE.md` (tono, ritmo, ejemplos buenos/malos)
- `editorial/HOOKS.md` (fórmulas de apertura)
- `editorial/FORMATS.md` (elegir el formato más adecuado al pilar y tipo)
- `editorial/ANGLES.md` (si la idea viene de fuente externa)

---

## Paso 3 — Verificar deduplicación

Comprobar en las 6 fuentes:
1. `content/published/`
2. `contenido/tweets-publicados.md`
3. `content/planning/SEPTIEMBRE_2026_CANDIDATOS.md`
4. `content/ready/`
5. `content/scheduled/`
6. `content/drafts/`

Si hay solapamiento significativo: reportarlo y preguntar si continuar con ángulo diferente.

---

## Paso 3.5 — Formular la Value Promise

Antes de redactar, definir obligatoriamente:

**VALUE PROMISE:** "Después de leer esta pieza, el lector..."

Determinar también:
- **value_category:** UTILITY | CLARITY | DECISION | EXPERIENCE | DATA | FRAMEWORK | ACCESS | CONVERSATION

Si no puede formularse una promesa de valor concreta con categoría clara:
→ No generar el draft.
→ Devolver:
```
NEEDS BETTER ANGLE
Razón: [por qué la idea actual no genera valor concreto]
Sugerencia: [ángulo alternativo si existe]
```

## Paso 4 — Generar el draft

Aplicar el formato elegido de `editorial/FORMATS.md`:
- Formato A: Historia de terceros conectada a experiencia propia
- Formato B: Desnudo financiero (dato + contexto + aprendizaje)
- Formato C: Error propio (situación → consecuencia → lección)
- Formato D: Contraste temporal (antes vs. ahora)

Reglas de escritura (de `editorial/VOICE.md`):
- Primera línea: hook de datos o situación, nunca apertura genérica
- Máximo 3 líneas por bloque (hilos)
- Una sola idea central
- NUNCA: "Hoy os voy a contar…", "Como ya sabéis…", cifras vagas
- Si es hilo: 5-8 tweets, no más de 10

Para hilos: generar cada tweet por separado y numerado.

---

## Paso 5 — Determinar risk_level y marcar claims

**risk_level: review** si el draft contiene:
- Datos de inversión, cartera, hipoteca
- Cifras derivadas no directamente en knowledge/
- Afirmaciones sobre el mercado externo
- Afirmaciones sobre el algoritmo de X
- Cualquier DERIVED_CLAIM

**risk_level: low** si el draft contiene:
- Solo experiencia personal directa
- Solo datos de knowledge/ sin derivación
- Proceso real / familia sin datos financieros

Registrar en frontmatter:
```yaml
facts_used:
  - INVESTMENTS.md#no-amortizar
  - MORTGAGE.md#tipo-2-05
derived_claims:
  - "diferencial de rentabilidad 30 años — needs_verification"
needs_verification:
  - "cálculo diferencial €"
```

---

## Paso 6 — Guardar el draft

Nombre del archivo: `content/drafts/draft-[slug]-YYYY-MM-DD.md`
El slug: 2-4 palabras del tema principal, en minúsculas con guiones.

Frontmatter completo:
```yaml
---
idea_id: IDEA-[TIPO]-NNN
draft_date: YYYY-MM-DD
pillar: [pilar]
format: A | B | C | D
risk_level: low | review
primary_audience: A | B | C | D
pain_point: "[descripción]"
content_job: reach | authority | trust | retention | conversion
value_category: UTILITY | CLARITY | DECISION | EXPERIENCE | DATA | FRAMEWORK | ACCESS | CONVERSATION
value_promise: "Después de leer esta pieza, el lector..."
facts_used: []
derived_claims: []
needs_verification: []
critic_status: pending
---
```

---

## Paso 7 — Informe final

Mostrar:
```
══════════════════════════════════════
WRITER REPORT — [draft_id]
══════════════════════════════════════
Idea origen:    IDEA-[TIPO]-NNN
Formato:        [A|B|C|D]
Pilar:          [pilar]
risk_level:     low | review
Value promise:  [texto de la promesa]
Value category: [categoría]
Facts usados:   [lista]
Derived claims: [lista — todos necesitan verificación antes de /approve]
──────────────────────────────────────
[TEXTO DEL DRAFT]
──────────────────────────────────────
Guardado en: content/drafts/draft-[slug]-YYYY-MM-DD.md
Siguiente paso: /review draft-[slug]-YYYY-MM-DD
══════════════════════════════════════
```
