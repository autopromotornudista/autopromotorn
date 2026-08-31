---
status: approved
visibility: internal
last_updated: 2026-08-31
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

```yaml
- experiment_id: EXP-003
  hypothesis: >
    Publicar en Slot A (09:00) y Slot C (18:00) generará ER mediana y reach mediano
    superiores al rendimiento histórico de la franja nocturna (19:30-22:30), que fue
    la más usada en agosto con el peor resultado (ER mediana 3,08%, reach mediano 107).
    Slot B (13:30) se evalúa como franja incógnita — solo 3 posts en agosto, nivel DÉBIL.
  metric: >
    Primaria: ER mediana por slot
    Secundaria: reach mediano por slot
    Benchmark agosto 2026 — Franja D (noche): ER 3,08% · reach 107
    Benchmark agosto 2026 — Franja A (mañana): ER 4,41% · reach 170
    Benchmark agosto 2026 — Franja C (tarde): ER 3,50% · reach 191
  start_date: 2026-08-31
  end_date: null
  sample_size: null  # objetivo ≥8 posts por slot para nivel SUFICIENTE
  result: null
  conclusion: null
  status: active
```

### Diseño EXP-003 — Timing

**Slots bajo test:**

| Slot | Hora (CEST) | Posts asignados semana 31/08-08/09 | Criterio éxito |
|------|-------------|-------------------------------------|----------------|
| A — Mañana | 09:00 | ID-01 Mié 02/09 · ID-04 Sáb 05/09 · ID-06 Mar 08/09 | ER > 4,41% OR reach > 170 |
| B — Mediodía | 13:30 | NEW-02 Mar 01/09 · ID-03 Vie 04/09 | ER competitivo vs A y C |
| C — Tarde | 18:00 | NEW-01 Lun 31/08 · ID-02 Jue 03/09 · ID-05 Dom 06/09 | ER > 3,50% OR reach > 191 |

**Control eliminado:** Slot D 20:00 (noche) — suspendido mientras dure el experimento.

**Protocolo de medición:**

| Post | Slot | Fecha | ER 24h | Reach 24h | ER 48h | Reach 48h | Nota |
|------|------|--------|--------|-----------|--------|-----------|------|
| tweet-construir-vs-comprar (NEW-01) | C | Lun 31/08 | — | — | — | — | |
| draft-segundo-orden (NEW-02) | B | Mar 01/09 | — | — | — | — | |
| tweet-excavacion (ID-01) | A | Mié 02/09 | — | — | — | — | |
| tweet-primer-pago (ID-02) | C | Jue 03/09 | — | — | — | — | |
| tweet-gremios (ID-03) | B | Vie 04/09 | — | — | — | — | |
| tweet-metros (ID-04) | A | Sáb 05/09 | — | — | — | — | |
| tweet-cubierta (ID-05) | C | Dom 06/09 | — | — | — | — | |
| hilo-interes-compuesto (ID-06) | A | Mar 08/09 | — | — | — | — | |

**Criterios de conclusión:**
- Mínimo 8 posts por slot antes de extraer conclusiones (nivel SUFICIENTE)
- Semana 1 (31/08-08/09): 8 posts como primera oleada, nivel DÉBIL
- Revisión provisional tras semana 1; conclusión provisional tras semana 3 (~24 posts)
- Si Slot B no llega a 8 posts en 4 semanas: nivel permanece DÉBIL, sin conclusión

**Confundidores a controlar:**
- El tema y el gancho explican más varianza que el horario (conclusión agosto). Anotar outliers por tema.
- Posts con foto vs. sin foto: registrar en columna "Nota"
- Hilos vs. tweets únicos: registrar en columna "Nota"

**Próxima actualización de resultados:** tras publicar los 8 posts de semana 1 (≥ 09/09/2026)

---

## Completados

*(ninguno todavía)*
