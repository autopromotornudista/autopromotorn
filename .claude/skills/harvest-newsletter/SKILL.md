---
name: harvest-newsletter
description: Procesa texto de newsletters, artículos o fragmentos de fuentes externas y extrae ideas editoriales para @autopromotorn. Usar cuando el usuario pegue directamente el texto de una fuente y pida "cosecha esto", "extrae ideas de", "analiza esta newsletter", "qué puedo sacar de esto". Diferente de /harvest que procesa URLs.
tools: Read
---

# harvest-newsletter — Skill de Cosecha de Newsletters

## Cuándo activar este skill

Activar cuando el usuario pegue el texto de una newsletter, artículo o fragmento de fuente externa y pida extraer ideas editoriales para @AutopromotorN.

Keywords de activación: "cosecha esto", "extrae ideas de", "analiza esta newsletter", "qué puedo sacar de", "procesa este texto", "harvest newsletter", `/harvest-newsletter`.

**Diferencia con `/harvest`:** `/harvest` procesa URLs (YouTube, Substack, web) y lanza scripts de extracción. Este skill procesa texto ya pegado por el usuario — sin acceso a URLs externas, sin scripts.

---

## PASO 0 — Recibir la entrada

El usuario proporciona:
- **Texto obligatorio:** contenido de la newsletter pegado directamente
- **Metadatos opcionales** (pedir solo si no se proporcionan y son relevantes):
  - Autor / publicación
  - Título del artículo
  - Fecha de publicación
  - URL de origen

Si no se proporcionan metadatos, usar `NO_DISPONIBLE` en el frontmatter.

---

## PASO 1 — Source Value Gate

Evaluar el texto recibido. Supera el gate si contiene **al menos uno** de:

**APROBAR si:**
- modelo mental aplicable al nicho (vivienda, autopromoción, hipoteca, finanzas personales)
- razonamiento nuevo o distinción conceptual útil
- contradicción relevante con el pensamiento convencional
- explicación sencilla de un problema complejo del nicho
- dato verificable con potencial editorial
- conexión natural con una experiencia real de @AutopromotorN
- perspectiva aplicable a: vivienda, autopromoción, construcción, hipotecas, ahorro, inversión
- pregunta que pueda generar contenido original

**DESCARTAR si:**
- contiene únicamente promoción de servicios, cursos o suscripciones
- idea demasiado genérica (podría venir de cualquier cuenta de finanzas sin cambiar nada)
- no tiene conexión razonable con el posicionamiento de @AutopromotorN
- exige forzar una relación artificial con vivienda o construcción
- únicamente permitiría repetir lo dicho por el autor sin transformación
- depende de afirmaciones no verificables que no pueden atribuirse con seguridad
- la idea ya existe con el mismo ángulo (verificar PASO 2 antes de confirmar este criterio)
- aporta estilo o tono pero no sustancia editorial
- resultaría en copia conceptual demasiado cercana al original

Si DESCARTAR: mostrar `DESCARTAR — [motivo concreto en una frase]` y detenerse. No crear ningún archivo.

---

## PASO 2 — Verificar duplicados

Antes de extraer ideas, leer en este orden:
1. `content/ideas/inbox/` — ideas capturadas recientemente
2. `content/ideas/` (raíz) — ideas activas existentes (`IDEA-HAR-*.md`, `IDEA-VID-*.md`)
3. `content/planning/SEPTIEMBRE_2026_CANDIDATOS.md` — contenido READY/SCHEDULED = ya utilizado
4. `content/drafts/` — borradores activos
5. `contenido/tweets-publicados.md` — historial publicado LEGACY

Si existe una idea con el mismo ángulo, mismo marco o misma conclusión:
- Documentarlo en el output bajo `## DUPLICADOS O RELACIONES`
- No crear archivo para esa idea
- Valorar si la nueva fuente puede enriquecer la idea existente (anotar en output)

---

## PASO 3 — Extraer ideas (máximo 3)

Extraer **como máximo 3 ideas**, priorizando calidad sobre cantidad. Si solo hay una idea válida, generar solo una.

Por cada idea, clasificar el contenido de la fuente como:
- `FACT` — dato externo verificable (needs_verification: true si es crítico)
- `INSIGHT` — interpretación u opinión del autor (NUNCA presentar como hecho propio)
- `FRAMEWORK` — estructura mental reutilizable (requiere transformación antes de usar)
- `STORY` — anécdota de la fuente (NUNCA presentar como experiencia propia)
- `DERIVED_CLAIM` — conclusión que combina hechos (needs_verification: true siempre)

Evaluar también la audiencia objetivo de la idea:
- **A** — Futuro autopromotor (proceso, costes, hipoteca)
- **B** — Comprador frustrado (mercado, alternativas, dilema)
- **C** — Perfil financiero (cartera, amortización, inversión)
- **D** — Curioso build-in-public (proceso en tiempo real, transparencia)

Si no se puede identificar audiencia con claridad: SKIP con razón explícita.

---

## PASO 4 — Determinar ID de archivo

El ID sigue el formato: `IDEA-NL-[YYYYMMDD]-[NNN]`

Para el NNN: contar los archivos `IDEA-NL-*.md` existentes en `content/ideas/inbox/` e incrementar desde el último. Si no hay ninguno, empezar en 001.

Nombre de archivo: `IDEA-NL-[YYYYMMDD]-[slug-descriptivo].md`

Ejemplo: `IDEA-NL-20260831-presupuesto-percepcion-riesgo.md`

---

## PASO 5 — Guardar cada idea válida

Crear un archivo individual en `content/ideas/inbox/` por cada idea que supere el gate y no sea duplicado.

**Frontmatter:**
```yaml
---
id: IDEA-NL-[YYYYMMDD]-[NNN]
captured_at: [ISO 8601 — fecha y hora actuales]
source_type: newsletter
source_title: [título del artículo o NO_DISPONIBLE]
source_author: [autor o NO_DISPONIBLE]
source_publication: [nombre de la publicación o NO_DISPONIBLE]
source_date: [fecha de publicación o NO_DISPONIBLE]
source_url: [URL o NO_DISPONIBLE]
topic: [tema principal en 2-4 palabras]
editorial_pillar: [pilar de los 5: Números & Finanzas | Proceso Real | Lecciones & Tips | Reflexiones & Contexto | Familia & Vida Real]
status: PENDIENTE_DE_VALIDACION
priority: alta | media | baja
potential: alto | medio | bajo
content_type: FACT | INSIGHT | FRAMEWORK | STORY | DERIVED_CLAIM
primary_audience: A | B | C | D
audience_pain_point: [dolor concreto en 1 frase desde la perspectiva del lector]
content_job: reach | authority | trust | retention | conversion
verification_required: true | false
factual_risk: bajo | medio | alto
copy_risk: bajo | medio | alto
saturation_risk: bajo | medio | alto
related_ideas: []
---
```

**Cuerpo:**
```markdown
# [Título descriptivo de la idea — no el título de la newsletter]

## Tesis de la fuente
[Qué argumenta o propone la fuente, en 2-3 frases. Sin transformar.]

## Insight extraído
[Qué se puede rescatar de esa tesis para @AutopromotorN. Diferente de la tesis original.]

## Transformación propia
[Cómo reencuadrar el insight desde la experiencia de @AutopromotorN. Primer orden / segundo orden. El "yo" que lo vivió.]

## Qué aporta @AutopromotorN
[Qué puede decir que el autor de la fuente no puede — experiencia real, número propio, decisión documentada.]

## Tensión narrativa
[El conflicto o paradoja que hace interesante el contenido: qué parece obvio vs. qué revela la experiencia real.]

## Posible gancho
[Dirección editorial — NO un tweet listo. Ej: "El contraste entre lo que te dice el constructor y lo que aprendemos al separar gremios".]

## Experiencia real necesaria
[Qué experiencia o dato propio debe existir para que este contenido sea publicable. Si no existe, indicarlo.]

## Hechos aprobados disponibles
[Referencias a knowledge/ que pueden sustentar este contenido. Ej: knowledge/MORTGAGE.md#condiciones-aprobadas]

## Preguntas pendientes para el usuario
[Qué información falta y debe preguntar el WRITER antes de desarrollar este contenido.]

## Verificación necesaria
[Qué afirmaciones de la fuente deben verificarse con fuente oficial antes de publicar.]

## Riesgos
- Factual: [bajo | medio | alto] — [razón]
- Copia: [bajo | medio | alto] — [razón]
- Saturación: [bajo | medio | alto] — [razón]

## Relación con ideas existentes
[Ideas existentes relacionadas, si las hay. Si no hay, escribir "Ninguna identificada".]

## Siguiente acción
[Qué debe ocurrir para que esta idea avance: validar dato, preguntar al usuario, o llamar a /write.]
```

---

## PASO 6 — Mostrar resultado estructurado

```
═══════════════════════════════════════════════
HARVEST NEWSLETTER — [título de la fuente o "SIN TÍTULO"]
═══════════════════════════════════════════════
Resultado:     FUENTE_APROVECHABLE | DESCARTAR

IDEAS EXTRAÍDAS: N
  ✓ [IDEA-NL-YYYYMMDD-NNN] — [slug descriptivo]
  ✗ [idea descartada] — [razón]

DUPLICADOS O RELACIONES:
  [si los hay, listar. Si no, "Ninguno identificado."]

ARCHIVOS CREADOS:
  content/ideas/inbox/IDEA-NL-[...].md
  [uno por idea válida]

PREGUNTAS PARA VALIDAR:
  [preguntas pendientes agrupadas, si las hay]

SIGUIENTE ACCIÓN:
  /write IDEA-NL-[YYYYMMDD]-[NNN] — cuando el usuario valide
  [o: "Validar duplicado con [archivo] antes de proceder"]
═══════════════════════════════════════════════
```

---

## Restricciones absolutas

- NO ejecutar WRITER ni generar borradores de posts
- NO programar en Buffer ni llamar MCPs externos
- NO crear commits ni push
- NO modificar `knowledge/`, `editorial/`, `content/drafts/`, `content/ready/`, `content/scheduled/`
- NO usar información privada del proyecto como si fuera pública
- NO inventar datos, fechas, precios ni experiencias
- NO crear archivo de idea si la fuente es DESCARTAR
- NO crear archivo de idea si es duplicado confirmado
- NO superar 3 ideas por sesión de harvest

---

## Separación de responsabilidades

| Agente | Función |
|--------|---------|
| **HARVESTER** (este skill) | Ingesta, evaluación, extracción y depósito en `content/ideas/inbox/` |
| **WRITER** (`/write`) | Transforma una idea aprobada en borrador usando `knowledge/` + `editorial/` |
| **CRITIC** (`/review`) | Evalúa borradores antes de aprobar para `content/ready/` |

El HARVESTER no escribe posts. El WRITER no busca ideas. El CRITIC no crea contenido.

Ver `docs/HARVESTER.md` para arquitectura completa del sistema.
