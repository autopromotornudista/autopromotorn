# /technical-check

Revisión técnica de un borrador específico por el agente `arquitecto-asesor-tecnico`.

**Lectura obligatoria antes de ejecutar:** `agents/arquitectoasesortecnico.md`

---

## Uso

```
/technical-check draft-aislamiento-fachada-2026-09-01
/technical-check content/drafts/draft-icio-pem-brecha-2026-09-01.md
```

Se acepta el slug o la ruta completa.

---

## Protocolo de ejecución

### PASO 1 — Leer el draft

Leer el borrador completo, incluyendo frontmatter.

### PASO 2 — Detectar afirmaciones técnicas

Buscar en el texto:
- Cantidades o cifras del presupuesto
- Superficies en m²
- Espesores de aislamiento o capas constructivas
- Materiales específicos (lana mineral, XPS, hormigón, acero, madera)
- Instalaciones: pellets, aerotermo, VMC doble flujo, fosa séptica
- Consumos o eficiencia energética
- Partidas del presupuesto o capítulos de obra
- Normativa CTE o cumplimiento técnico
- Comparaciones entre sistemas constructivos
- Descripciones del proyecto o de lo previsto
- Comparaciones entre lo previsto y lo ejecutado
- Consejos constructivos interpretables como recomendación profesional

Si no hay ninguna → `technical_check: NOT_REQUIRED`. Actualizar frontmatter y terminar.

### PASO 3 — Verificar cada afirmación técnica

Para cada afirmación detectada, buscar en fuentes (orden de jerarquía del contrato del agente):

```
1. docs/conocimiento_vivienda_abelar.md
2. docs/Proxecto Vivenda O Abelar/
3. knowledge/VALIDATED_CONTEXT_2026-08-31.md
4. knowledge/HOUSE.md, knowledge/FINANCES.md, resto knowledge/
5. docs/diario-obra.md
6. knowledge/technical/PROJECT_CHANGELOG.md
7. knowledge/technical/OPEN_TECHNICAL_QUESTIONS.md
```

### PASO 4 — Clasificar resultado

**APROBADO:** Todas las afirmaciones verificadas o no bloqueantes.
→ `technical_check: PASSED`

**APROBADO CON NOTAS:** Algún dato menor no verificado, no bloqueante.
→ `technical_check: PASSED_WITH_NOTES`

**REQUIERE DOCUMENTACIÓN:** Hay una afirmación bloqueante sin fuente.
→ `technical_check: REQUIRES_DOC`

### PASO 5 — Actualizar frontmatter del draft

Añadir o actualizar:

```yaml
technical_check: PASSED | PASSED_WITH_NOTES | REQUIRES_DOC | NOT_REQUIRED
technical_check_date: YYYY-MM-DD
technical_check_notes: "Una línea solo si hay algo relevante para el usuario"
```

Si `PASSED` o `NOT_REQUIRED` → no interrumpir al usuario.
Si `PASSED_WITH_NOTES` → informar en la respuesta, no bloqueante.
Si `REQUIRES_DOC` → mostrar el informe completo y solicitar la documentación específica.

### PASO 6 — Devolver informe estructurado

```markdown
# REVISIÓN TÉCNICA — [slug del draft]

## Veredicto

APROBADO | APROBADO CON CAMBIOS | BLOQUEADO POR FALTA DE INFORMACIÓN | BLOQUEADO POR ERROR TÉCNICO

## Afirmaciones verificadas

1. Afirmación: [texto]
   - Estado: DOCUMENTADO EN PROYECTO / etc.
   - Fuente: [documento + apartado]
   - Nivel de certeza: ALTA / MEDIA / BAJA

## Errores o imprecisiones

1. Texto problemático: [cita]
   - Problema: [descripción]
   - Corrección propuesta: [texto correcto]
   - Fuente: [documento]

## Información no documentada

- Dato: [descripción]
- Documento necesario: [nombre del documento]

## Riesgo de interpretación

Bajo / Medio / Alto — [explicación]

## Fuentes consultadas

- [ruta del archivo]
```

---

## Invariantes

- Un APROBADO significa que el contenido coincide con la documentación disponible, no que sea una certificación profesional
- NUNCA inventar datos para resolver un bloqueo
- NUNCA modificar el texto del borrador — solo el frontmatter y el informe
- NUNCA bloquear piezas independientes por una afirmación bloqueante en otra pieza
- NUNCA revelar ubicación exacta ni datos privados aunque aparezcan en el borrador
