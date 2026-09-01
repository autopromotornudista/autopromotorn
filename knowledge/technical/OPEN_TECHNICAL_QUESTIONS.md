---
status: approved
visibility: internal
last_updated: 2026-09-01
managed_by: arquitecto-asesor-tecnico
---

# OPEN_TECHNICAL_QUESTIONS — Preguntas técnicas pendientes

## Propósito

Registro de datos técnicos que no pueden confirmarse con las fuentes actuales disponibles, discrepancias entre documentos, y preguntas abiertas que afectan o podrían afectar al contenido editorial.

**Impacto editorial:** Mientras una pregunta está abierta, el agente arquitecto-asesor-tecnico aplica degradación elegante: omite el dato, usa formulación general, o marca el campo como pendiente en el draft.

---

## Formato de entrada

```
### OTQ-NNN — [Descripción breve]
- **Abierta desde:** YYYY-MM-DD
- **Categoría:** discrepancia | dato_ausente | modificación_no_confirmada | limitación_técnica
- **Descripción:** [qué se desconoce o qué está en conflicto]
- **Fuentes en conflicto:** [doc A dice X / doc B dice Y]
- **Impacto en contenido:** BLOQUEANTE | CON_MATICES | NO_BLOQUEANTE
- **Documento que resolvería:** [qué haría falta para cerrar]
- **Estado:** ABIERTA | RESUELTA: [fecha + cómo se resolvió]
```

---

## Preguntas abiertas

### OTQ-001 — Discrepancia de superficies entre fuentes históricas y documento visado

- **Abierta desde:** 2026-09-01
- **Categoría:** discrepancia
- **Descripción:** El archivo `instrucciones_vivienda.md` (ya no existe en el repositorio) contenía superficies distintas a las que aparecen en la memoria visada del proyecto. Las cifras actualmente en uso son las del documento visado y las confirmadas en VALIDATED_CONTEXT_2026-08-31.md.
- **Fuentes en conflicto:** `instrucciones_vivienda.md` (eliminado, fuente histórica) vs. memoria visada del proyecto (fuente oficial)
- **Valores en uso (fuente canónica):** 122 m² útiles / 153,56 m² construidos (memoria visada + VALIDATED_CONTEXT)
- **Impacto en contenido:** NO_BLOQUEANTE — los valores canónicos están claros; el conflicto es histórico
- **Documento que resolvería:** La memoria visada ya resuelve el dato. Esta entrada existe solo como registro de la discrepancia histórica.
- **Estado:** RESUELTA: 2026-09-01 — La jerarquía documental establece que la memoria visada prevalece. Valores confirmados: 122 m² útiles / 153,56 m² construidos.

---

### OTQ-002 — Eficiencia energética: sección escaneada como imágenes en el PDF

- **Abierta desde:** 2026-09-01
- **Categoría:** limitación_técnica
- **Descripción:** La sección de eficiencia energética del PDF del proyecto visado está mayoritariamente escaneada como imágenes. Las tablas de demanda, consumo, calificación energética y resultados del HE no pueden extraerse como texto. Los valores no están disponibles para verificación automática.
- **Fuentes en conflicto:** N/A — es una limitación de acceso, no una discrepancia
- **Impacto en contenido:** BLOQUEANTE para cualquier post que cite cifras exactas de eficiencia energética, calificación de la letra, kWh/m²·año o cumplimiento HE
- **Documento que resolvería:** Revisión visual del PDF original + transcripción manual de los valores de la sección de eficiencia energética
- **Estado:** ABIERTA

---

## Preguntas resueltas

*(Mover aquí cuando se cierre una OTQ, conservando el registro histórico)*

---

## Notas

- El agente arquitecto-asesor-tecnico añade entradas a este archivo cuando detecta datos no documentados durante la revisión de borradores.
- Las entradas BLOQUEANTES se priorizan para resolución antes de publicar contenido relacionado.
- La resolución de una OTQ requiere una fuente documental válida en la jerarquía, no una estimación.
