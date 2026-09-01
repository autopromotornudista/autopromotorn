---
status: approved
last_updated: 2026-09-01
---

# content/ideas/forum/ — Insights de audiencia (FORUM_SCOUT)

## Propósito

Este directorio contiene insights detectados por FORUM_SCOUT en el subforo público de SoloArquitectura (promotores y autopromotores). Cada archivo representa una preocupación real de la audiencia objetiva, no un contenido redactado.

**No contiene borradores.** Los borradores derivados van a `content/drafts/`. Este directorio solo contiene la materia prima: ángulo detectado en foro + scoring + conexión con knowledge/.

---

## Nomenclatura

```
FORUM-YYYYMMDD-NNN.md
```

- `YYYYMMDD` — fecha en que FORUM_SCOUT detectó el hilo
- `NNN` — número incremental dentro del mismo día (001, 002…). Se reinicia con cada nuevo día.

**Ejemplos:** `FORUM-20260901-001.md` · `FORUM-20260901-002.md` · `FORUM-20260905-001.md`

---

## Formato de archivo

```yaml
---
forum_id: FORUM-YYYYMMDD-NNN
source: soloarquitectura.com
forum_url: https://www.soloarquitectura.com/foros/forums/promotores-y-autopromotores.45/
thread_title: "Título exacto del hilo"
thread_url: https://www.soloarquitectura.com/foros/threads/slug.XXXXX/
thread_date: YYYY-MM-DD
thread_updated: YYYY-MM-DD
replies: N
views: N
detected: YYYY-MM-DD
phase: Hipoteca y financiación   # una de las 11 fases (ver abajo)
concern: "Preocupación subyacente en 1 frase"
why_relevant: "Por qué importa a @AutopromotorN en 1-2 frases"
recurrence: única | baja | media | alta
debate_intensity: bajo | medio | alto
pillar_fit: Números & Finanzas   # pilar editorial más cercano
experience_fit: true | false     # conecta con experiencia validada en knowledge/
score: 0-100
score_breakdown:
  recurrence: 0-25
  activity: 0-20
  recency: 0-15
  pain_impact: 0-20
  account_fit: 0-20
solution_for: "Pregunta concreta del foro que el contenido debe responder"
solution_approach: "Qué respuesta/solución aportamos desde knowledge/ — en 1-2 frases"
angles:
  - "Ángulo 1 sin redactar"
  - "Ángulo 2 sin redactar"
accuracy_risks: "Qué habría que verificar antes de publicar"
status: IDEA_PENDIENTE_DE_VALIDACION | pending_context | draft_generated:[slug] | discarded:[motivo]
---

## Contexto del hilo

[Resumen en 3-5 frases. Sin citar mensajes completos. Sin datos personales ni usernames.]

## Preguntas y preocupaciones detectadas

- [Preocupación 1]
- [Preocupación 2]

## Posibles ángulos de contenido

1. [Ángulo 1] — conexión con pilar X
2. [Ángulo 2] — conexión con experiencia propia en knowledge/MORTGAGE.md

## Notas de exactitud

[Qué habría que verificar, si algún dato del foro necesita contraste con fuentes propias]
```

---

## Fases de autopromoción (clasificación obligatoria)

| Nº | Fase |
|----|------|
| 1 | Acceso y viabilidad |
| 2 | Parcela |
| 3 | Arquitecto y proyecto |
| 4 | Licencia e impuestos |
| 5 | Presupuestos y constructor |
| 6 | Hipoteca y financiación |
| 7 | Ejecución de obra |
| 8 | Instalaciones y materiales |
| 9 | Sobrecostes y retrasos |
| 10 | Final de obra y entrada |
| 11 | Problemas posteriores |

---

## Estados de un insight

| Estado | Significado |
|--------|------------|
| `IDEA_PENDIENTE_DE_VALIDACION` | FORUM_SCOUT detectó el hilo; sin borrador aún |
| `pending_context` | Score ≥ 60 pero sin experiencia validada en knowledge/ para desarrollar |
| `draft_generated:[slug]` | WRITER generó borrador en `content/drafts/draft-[slug]-YYYY-MM-DD.md` |
| `discarded:[motivo]` | Descartado por duplicado semántico, score insuficiente o sin relevancia |

---

## Flujo automático (FORUM_SCOUT)

```
Hilo detectado en RSS / visita
    ↓ scoring 0-100
score < 60  → archivado (sin archivo de idea)
score 60-79 → FORUM-YYYYMMDD-NNN.md creado
                ↓ ¿knowledge/ conecta?
                SÍ → WRITER genera draft → CRITIC evalúa
                NO → status: pending_context (esperar experiencia propia)
score ≥ 80  → igual + value_level: HIGH en el draft
```

**Intervención humana** solo en `/approve` (revisar draft) y `/schedule --confirm` (programar en Buffer).

---

## Quién puede escribir en este directorio

| Acción | Agente |
|--------|--------|
| Crear `FORUM-*.md` | FORUM_SCOUT (automático) |
| Actualizar `status` | FORUM_SCOUT o usuario |
| Leer para desarrollar | WRITER (invocado por FORUM_SCOUT) |
| Marcar como `discarded` | FORUM_SCOUT (deduplicación) o usuario |

**FORUM_SCOUT nunca escribe en `knowledge/`, `editorial/`, `content/ready/` ni `content/scheduled/`.**

---

## Deduplicación

FORUM_SCOUT verifica duplicados antes de crear cada insight:
1. Por URL exacta del hilo → `sources/forum/STATE.md`
2. Por preocupación semántica → busca en `content/ideas/forum/`, `content/ideas/`, `content/drafts/`

Si hay duplicado semántico: registra como `discarded:duplicate:[FORUM-ID-existente]` y no crea archivo nuevo.
