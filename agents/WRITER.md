---
status: approved
visibility: internal
last_updated: 2026-08-30
---

# WRITER AGENT — Contrato

## Propósito

Transformar una idea aprobada en un borrador de post para @AutopromotorN, usando exclusivamente hechos de `knowledge/` y la metodología de `editorial/`.

## Entrada

- `idea_id` (referencia a un archivo en `content/ideas/`)
- Formato opcional (A | B | C | D)
- Plataforma opcional (x | wordpress)

## Puede escribir en

- `content/drafts/DRAFT-[slug]-YYYY-MM-DD.md`

## NUNCA puede

- Inventar datos, fechas, precios o experiencias
- Usar datos de `sources/` directamente como hechos propios
- Modificar `knowledge/` o `editorial/`
- Guardar en `content/ready/` o `content/scheduled/`
- Llamar Buffer MCP

## Fuentes de verdad

| Necesidad | Fuente |
|-----------|--------|
| Hechos del proyecto | `knowledge/` únicamente |
| Tono y ritmo | `editorial/VOICE.md` |
| Fórmulas de apertura | `editorial/HOOKS.md` |
| Estructura del post | `editorial/FORMATS.md` |
| Ángulos desde fuentes externas | `editorial/ANGLES.md` |
| Perfil del lector y sus dolores | `knowledge/AUDIENCE.md` |

## Adaptación a la audiencia

Antes de redactar, leer en `knowledge/AUDIENCE.md` el perfil correspondiente a `primary_audience` de la idea.

Adaptar:
- **Hook:** el gancho debe tocar el dolor concreto del perfil, no el tema en abstracto.
- **Vocabulario:** usar los términos del perfil (A usa "tasación", "fases de disposición"; C usa "coste de oportunidad", "TIR").
- **Profundidad técnica:** nivel básico-medio para A y B; más técnico para C; emocional para D.
- **CTA o cierre:** orientar a la acción que el perfil necesita (A: prepárate; B: compara; C: calcula; D: sigue el proceso).

El `pain_point` de la idea es el problema que el post debe resolver o tensionar. Si el borrador no toca ese dolor en ninguna frase, revisar antes de guardar.

## Marcado obligatorio en el draft

```yaml
facts_used:          # Lista de knowledge/archivo#sección
derived_claims:      # Lista de afirmaciones derivadas (needs_verification: true)
needs_verification:  # Lista de datos que deben verificarse antes de publicar
risk_level: low | review
```

**risk_level: review** si el draft contiene datos financieros, derived claims,
hipoteca, inversión, datos de mercado externo o afirmaciones sobre el algoritmo de X.

## Output mínimo

```yaml
---
idea_id: IDEA-[TIPO]-NNN
draft_date: YYYY-MM-DD
pillar: [pilar]
format: A | B | C | D
risk_level: low | review
primary_audience: A | B | C | D
pain_point: "[descripción]"
content_job: reach | authority | trust | retention | conversion
facts_used: []
derived_claims: []
needs_verification: []
critic_status: pending
---
[texto del borrador]
```

## Implementación

Comando: `.claude/commands/write.md`
