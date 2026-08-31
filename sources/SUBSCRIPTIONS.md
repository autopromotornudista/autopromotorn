---
last_updated: 2026-08-29
---
<!-- última actualización: primer harvest real (SRC-002 Joan Tubau, 2 ideas generadas) -->

# SUBSCRIPTIONS — Fuentes recurrentes autorizadas

Registro maestro de fuentes externas autorizadas para el Content Harvester.

**Regla:** una fuente solo entra aquí con autorización humana explícita. No hay alta automática.

---

## Cómo usar este archivo

1. Antes de procesar una URL nueva, verificar si la fuente ya está registrada aquí.
2. Si la fuente no está registrada → pedir autorización antes de procesarla.
3. Actualizar `last_processed` y los contadores de yield después de cada ciclo.
4. Revisar scores trimestralmente.

---

## Clasificación de tipos

`newsletter` · `substack` · `youtube` · `podcast` · `web` · `x`

---

## Clasificación de prioridad

`high` → procesar siempre · `medium` → procesar si hay tiempo · `low` → procesar bajo demanda

---

## Fuentes activas

```yaml
- id: SRC-001
  name: Inversor a Con 30
  author: pendiente de confirmar
  type: substack
  url: https://inversoracon30.substack.com
  frequency: weekly
  priority: high
  active: true
  last_processed: null
  ideas_generated: 0
  ideas_published: 0
  ideas_high_performance: 0
  yield_score: null
  notes: "Única fuente con WebFetch autorizado actualmente en settings.json"

- id: SRC-002
  name: Joan Tubau — Kapital
  author: Joan Tubau
  type: substack
  url: https://joantubau.substack.com
  frequency: irregular
  priority: medium
  active: true
  last_processed: 2026-08-31
  ideas_generated: 5
  ideas_published: 0
  ideas_high_performance: 0
  yield_score: null
  source_score_mvp: 6
  score_breakdown: "relevancia 2/3 · originalidad 2/2 · trazabilidad 2/2"
  notes: "Frameworks filosófico-financieros de alto valor para pilar Reflexiones. Vocabulario muy distintivo — requiere transformación profunda antes de usar. No toca construcción ni hipotecas directamente."
  harvest_log:
    - date: 2026-08-29
      article: "Proyectos Pingüino"
      url: https://joantubau.substack.com/p/proyectos-pinguino
      ideas_saved: [IDEA-HAR-001, IDEA-HAR-002]
      ideas_discarded: [IDEA-HAR-003 solapamiento IDEA-002, IDEA-HAR-004 framing dependiente fuente, IDEA-HAR-005 prioridad baja]
    - date: 2026-08-31
      article: "La gran conspiración boomer"
      url: https://joantubau.substack.com/p/la-gran-conspiracion-boomer
      ideas_saved: [IDEA-HAR-006, IDEA-HAR-007]
      ideas_discarded: ["ángulo boomers-no-venden — demasiado próximo a construir-vs-comprar (31/08) y decisiones-abiertas (14/09)"]
    - date: 2026-08-31
      article: "Cuando la opcionalidad te mata"
      url: https://joantubau.substack.com/p/cuando-la-opcionalidad-te-mata
      ideas_saved: [IDEA-HAR-008]
      ideas_discarded: ["opcionalidad financiera/no-amortizar — enriquece IDEA-HAR-001 en lugar de crear idea separada"]

- id: SRC-003
  name: Canal YouTube hipotecas y mercado inmobiliario España
  author: pendiente de confirmar (presentadora "Monse")
  channel_name: pendiente de confirmar
  channel_url: pendiente de confirmar
  metadata_status: pending
  type: youtube
  url: https://www.youtube.com/watch?v=tqjs5D5-9DQ
  frequency: irregular
  priority: medium
  active: true
  last_processed: 2026-08-29
  ideas_generated: 3
  ideas_published: 0
  ideas_high_performance: 0
  yield_score: null
  source_score_mvp: 4
  score_breakdown: "relevancia 2/3 · originalidad 1/2 · trazabilidad 1/2"
  notes: "Broker hipotecaria española. Datos de mercado en tiempo real: Euribor, condiciones de financiación, evolución precios. Canal frecuente de seguimiento — confirmar nombre del canal y URL del canal para completar el registro. FACTs externos siempre con needs_verification: true."
  harvest_log:
    - date: 2026-08-29
      video: "Análisis mercado hipotecario agosto 2026"
      url: https://www.youtube.com/watch?v=tqjs5D5-9DQ
      transcript: docs/fuentes/2026-08-29-tqjs5D5-9DQ.md
      ideas_saved: [IDEA-VID-001, IDEA-VID-002, IDEA-VID-003]
      ideas_discarded: [datos Barcelona/Madrid/Alicante sin conexión propia, predicciones septiembre sin datos, ITP/IVA irrelevante para autopromotor ya financiado]
```

---

## Fuentes inactivas

*(ninguna todavía)*

---

## Source Score

El score se calcula cuando la fuente tiene historial suficiente (mínimo 3 ciclos de procesamiento).

**Dimensiones:**

| Dimensión | Escala | Criterio |
|-----------|--------|---------|
| Relevancia temática | 0–3 | % de publicaciones que tocan hipoteca, construcción, inversión o familia |
| Originalidad | 0–2 | Perspectiva y datos propios vs. reempaquetar a otros |
| Calidad / trazabilidad | 0–2 | Autor identificado, fuente citada cuando hace afirmaciones de hecho, contenido trazable a su origen. No equivale a asumir que el contenido es factualmente correcto. |
| Yield histórico | 0–3 | Solo disponible con historial real: `(ideas_high_performance / ideas_generated)` |

**Fórmula MVP (fuente nueva, sin historial):**
```
SOURCE SCORE = relevancia + originalidad + trazabilidad
```

**Fórmula completa (fuente con historial ≥ 3 ciclos):**
```
SOURCE SCORE = relevancia + originalidad + trazabilidad + yield_histórico
```

---

## Protocolo de actualización

Después de cada ciclo de procesamiento, actualizar:
- `last_processed`: fecha del ciclo
- `ideas_generated`: +1 por cada IDEA-NNN.md generada desde esta fuente
- `ideas_published`: +1 cuando un borrador de esa idea se publica
- `ideas_high_performance`: +1 cuando un post publicado alcanza rendimiento alto (criterio manual)
- Recalcular `yield_score` = `ideas_high_performance / ideas_generated`

No automatizar desactivaciones por score. Solo registrar datos por ahora.
