---
status: approved
visibility: internal
last_updated: 2026-08-30
source_type: human_approved
---

# EXPERIMENTS.md — Registro de experimentos

Los experimentos son la única fuente de verdad local sobre el comportamiento de @AutopromotorN en X. Ninguna regla operativa sobre timing, formato, volumen o alcance se establece sin respaldo experimental propio.

**Schema por experimento:**

```yaml
experiment_id:
hypothesis:      # Qué creemos que ocurrirá y por qué
metric:          # Métrica primaria que valida o invalida la hipótesis
start_date:      # ISO 8601 — se establece al activar, no antes
end_date:        # ISO 8601 — se establece al completar
sample_size:     # Número de posts/replies/días evaluados
result:          # Dato medido
conclusion:      # Qué se aprendió
status:          # backlog | active | completed | cancelled
```

---

## Backlog

```yaml
- experiment_id: EXP-001
  hypothesis: >
    Hacer 10-15 replies de calidad diarios en cuentas con 2-10× los seguidores
    actuales produce crecimiento de seguidores medible en un periodo de 4 semanas,
    superior al crecimiento en semanas equivalentes sin esa actividad.
  metric: followers gained / semana
  start_date: null
  end_date: null
  sample_size: null
  result: null
  conclusion: null
  status: backlog

- experiment_id: EXP-002
  hypothesis: >
    Los posts con foto real del proyecto (obra, documentos, gráficos propios)
    generan mayor ratio bookmarks/impressions que los posts solo de texto,
    en el mismo pilar temático.
  metric: bookmarks / impressions
  start_date: null
  end_date: null
  sample_size: null
  result: null
  conclusion: null
  status: backlog

- experiment_id: EXP-003
  hypothesis: >
    Publicar a las 08:30, 14:00 o 21:00 produce diferencias medibles en
    impressions/post para el mismo tipo de contenido. Una de las tres franjas
    supera a las demás de forma consistente.
  metric: impressions por post (normalizado por tipo de contenido)
  start_date: null
  end_date: null
  sample_size: null
  result: null
  conclusion: null
  status: backlog

- experiment_id: EXP-004
  hypothesis: >
    El contenido de utilidad directa (checklists, datos accionables, lecciones)
    genera mayor ratio bookmarks/impressions y followers/impressions que el
    contenido de reflexión u opinión.
  metric: bookmarks / impressions · followers / impressions
  start_date: null
  end_date: null
  sample_size: null
  result: null
  conclusion: null
  status: backlog
```

---

## Activos

*(ninguno todavía)*

---

## Completados

*(ninguno todavía)*
