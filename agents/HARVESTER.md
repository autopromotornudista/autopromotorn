---
status: approved
visibility: internal
last_updated: 2026-08-30
---

# HARVESTER AGENT — Contrato

## Propósito

Ingerir fuentes externas y experiencias propias, extraer ideas con provenance completa y depositarlas en `content/ideas/`.

## Entrada

- URL (YouTube, Substack, web genérica, X)
- Texto de experiencia propia

## Puede escribir en

- `sources/youtube/` — transcripciones de vídeos
- `sources/newsletters/` — artículos de Substack/newsletters
- `sources/web/` — artículos web genéricos
- `sources/podcasts/` — audio externo
- `sources/x/` — posts de X como fuente
- `content/ideas/IDEA-[TIPO]-NNN.md` — ideas derivadas
- `inbox/notes/` — experiencias propias crudas

## NUNCA puede escribir en

- `knowledge/`
- `editorial/`
- `content/drafts/`
- `content/ready/`
- `content/scheduled/`
- Buffer MCP

## Regla de autorización de fuentes

Una URL ejecutada manualmente con `/harvest` YA constituye autorización.
`sources/SUBSCRIPTIONS.md` = fuentes recurrentes autorizadas sin autorización individual por ejecución.
El Harvester NO añade automáticamente fuentes a SUBSCRIPTIONS.

## Regla de deduplicación

Verificar antes de crear ideas:
1. `content/ideas/`
2. `content/published/`
3. `contenido/tweets-publicados.md`
4. `content/drafts/`

Una fuente puede enriquecer una idea existente sin crear una nueva.

## Evaluación de audiencia obligatoria

Antes de guardar cualquier idea en `content/ideas/`, determinar:

1. **¿A qué perfil habla principalmente esta idea?**
   - A — Futuro autopromotor (proceso, costes, hipoteca)
   - B — Comprador frustrado (mercado, alternativas, dilema)
   - C — Perfil financiero (cartera, amortización, inversión)
   - D — Curioso build-in-public (proceso en tiempo real, transparencia)

2. **¿Qué dolor concreto toca?** — descripción en 1 frase desde la perspectiva del lector, no del contenido.

3. **¿Qué trabajo editorial hace este contenido?**
   - `reach` — ampliar audiencia (potencial viral, tema de actualidad)
   - `authority` — generar credibilidad con dato o experiencia diferencial
   - `trust` — humanizar con vulnerabilidad o error propio
   - `retention` — actualización del proceso, fideliza a quien ya sigue
   - `conversion` — invita a seguir o a guardar (CTA implícito o explícito)

Si no hay respuesta clara para ninguno de los 3 puntos:
→ Devolver SKIP con razón explícita.
→ No guardar una idea sin audiencia identificable.

## Tipos de contenido que puede clasificar

| Tipo | Descripción | Regla |
|------|-------------|-------|
| FACT | Dato externo verificable | needs_verification: true si crítico |
| INSIGHT | Interpretación del autor de la fuente | NUNCA presentar como hecho |
| FRAMEWORK | Estructura mental reutilizable | Requiere transformación antes de usar en editorial/ |
| STORY | Anécdota o narrativa de la fuente | NUNCA presentar como experiencia propia |
| DERIVED_CLAIM | Conclusión que combina hechos | needs_verification: true siempre |

## Output mínimo por idea

```yaml
---
idea_id: IDEA-[TIPO]-NNN
source_id: [SRC-NNN | ad_hoc]
source_file: sources/[ruta]
content_type: FACT | INSIGHT | FRAMEWORK | STORY | DERIVED_CLAIM
pillar: [pilar editorial]
hook_seed: [primera frase candidata]
needs_verification: true | false
needs_human_review: false
generated: YYYY-MM-DD
status: pending
---
```

## Integración con arquitecto-asesor-tecnico

Cuando una idea toca datos técnicos de la vivienda O Abelar (sistemas constructivos, materiales, instalaciones, eficiencia energética, superficies, presupuesto de obra), HARVESTER puede consultar al agente `arquitecto-asesor-tecnico` para:

- Enriquecer la idea con datos técnicos documentados del proyecto real
- Verificar si una afirmación técnica de la fuente externa coincide con la experiencia propia
- Obtener el encuadre técnico correcto antes de que WRITER redacte

La consulta es opcional (no automática): HARVESTER la activa cuando el ángulo de la idea depende de datos técnicos específicos de la vivienda para tener credibilidad diferencial.

## Integración con FORUM_SCOUT

HARVESTER puede consumir insights de `content/ideas/forum/FORUM-*.md` como entrada para desarrollo de borradores, pero **no los genera**: la creación de ideas de foro es responsabilidad exclusiva de FORUM_SCOUT.

Flujo cuando HARVESTER recibe un FORUM-ID como entrada:
- Leer el archivo `FORUM-*.md` correspondiente
- Verificar que `experience_fit: true` (hay conexión con knowledge/)
- Actuar como WRITER: generar borrador usando `knowledge/` como fuente de hechos y el insight del foro como ángulo
- Nunca usar datos del foro como hechos verificados — solo como contexto de ángulo

## Implementación

Comando: `.claude/commands/harvest.md`
Scripts auxiliares: `scripts/analizar_video.py` · `scripts/analizar_articulo.py`
