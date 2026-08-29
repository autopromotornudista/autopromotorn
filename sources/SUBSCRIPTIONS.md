---
last_updated: 2026-08-29
---

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
| Fiabilidad | 0–2 | Fuente verificable, autor identificado, datos con fuente citada |
| Yield histórico | 0–3 | Solo disponible con historial real: `(ideas_high_performance / ideas_generated)` |

**Fórmula MVP (fuente nueva, sin historial):**
```
SOURCE SCORE = relevancia + originalidad + fiabilidad
```

**Fórmula completa (fuente con historial ≥ 3 ciclos):**
```
SOURCE SCORE = relevancia + originalidad + fiabilidad + yield_histórico
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
