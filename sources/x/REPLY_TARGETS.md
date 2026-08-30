---
status: approved
visibility: internal
last_updated: 2026-08-30
source_type: human_approved
---

# REPLY_TARGETS.md — Cuentas objetivo para engagement

Registro de cuentas de X relevantes para la estrategia de reply de @AutopromotorN.

**Mantenimiento:** responsabilidad del Radar Agent (cuando esté operativo). Hasta entonces, actualización manual en sesión.

**Regla:** no copiar automáticamente sugerencias externas sin verificación posterior. Cada cuenta entra con un estado explícito y se revisa periódicamente.

---

## Schema

```yaml
- handle:          # @cuenta
  topic:           # Por qué es relevante (nicho, tipo de contenido)
  priority:        # high | medium | low
  status:          # candidate | active | watch | inactive
  last_reviewed:   # ISO 8601
  notes:           # Observaciones concretas
```

**Estados:**
- `candidate` — identificada como potencialmente relevante, pendiente de verificar
- `active` — cuenta prioritaria de seguimiento y reply activo
- `watch` — seguimiento pasivo, sin reply activo por ahora
- `inactive` — dejó de ser relevante o cambió el tipo de contenido

---

## Cuentas registradas

*(pendiente de poblado manual — el Radar Agent será responsable de mantener esta lista)*
