# /ask-architect

Consulta técnica directa al agente `arquitecto-asesor-tecnico` sobre la vivienda O Abelar.

**Lectura obligatoria antes de ejecutar:** `agents/arquitectoasesortecnico.md`

---

## Uso

```
/ask-architect ¿Cuánto aislamiento lleva la fachada?
/ask-architect ¿Cuál es el sistema de calefacción?
/ask-architect ¿Cuántos m² tiene la vivienda?
/ask-architect ¿Cuál es el PEM del proyecto?
```

---

## Protocolo de ejecución

### PASO 1 — Leer el contrato del agente

Leer `agents/arquitectoasesortecnico.md` completo antes de responder. Aplicar:
- Jerarquía documental (11 niveles)
- Orden de búsqueda (7 pasos)
- Estados de información
- Reglas de privacidad

### PASO 2 — Buscar en las fuentes (en este orden exacto)

```
1. docs/conocimiento_vivienda_abelar.md
2. docs/Proxecto Vivenda O Abelar/ y subcarpetas
3. knowledge/VALIDATED_CONTEXT_2026-08-31.md
4. knowledge/HOUSE.md, knowledge/FINANCES.md, resto de knowledge/
5. docs/diario-obra.md
6. knowledge/technical/PROJECT_CHANGELOG.md
7. knowledge/technical/OPEN_TECHNICAL_QUESTIONS.md
```

Agotar la búsqueda antes de declarar un dato como NO DOCUMENTADO.

### PASO 3 — Responder con formato estructurado

```markdown
## Respuesta breve

[Explicación directa y comprensible. Sin jerga innecesaria.]

## Estado del dato

DOCUMENTADO EN PROYECTO | MODIFICADO EN OBRA | VALIDADO POR EL PROPIETARIO | INFERENCIA TÉCNICA | NO DOCUMENTADO

## Evidencia

- Documento: [ruta]
- Apartado o capítulo: [sección específica]
- Dato localizado: [texto o cifra exacta encontrada]

## Matiz técnico

[Condiciones, limitaciones o interpretaciones necesarias. Omitir si no hay ninguna.]

## Uso en contenido

- Qué puede afirmarse públicamente: [formulación segura]
- Qué no debe afirmarse: [si aplica]

## Confianza

ALTA | MEDIA | BAJA
```

### PASO 4 — Registrar si hay datos no documentados

Si la búsqueda no encuentra el dato y es relevante:
→ Comprobar si ya existe entrada en `knowledge/technical/OPEN_TECHNICAL_QUESTIONS.md`
→ Si no existe, añadir entrada OTQ-NNN

---

## Invariantes

- NUNCA inventar datos, medidas, espesores, consumos o costes no documentados
- NUNCA usar valores habituales de mercado como si fueran datos del proyecto
- NUNCA revelar ubicación exacta, referencias catastrales o datos privados (usar "nuestra vivienda en Galicia")
- NUNCA completar sección de eficiencia energética con valores estimados (está escaneada como imágenes)
