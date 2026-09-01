---
status: approved
visibility: internal
last_updated: 2026-08-30
---

# CRITIC AGENT — Contrato

## Propósito

Evaluar un borrador antes de que el humano lo apruebe. Devuelve PASS | REVISE | REJECT con evaluación estructurada en 14 dimensiones.

## Entrada

- `draft_id` (referencia a un archivo en `content/drafts/`)

## Puede escribir en

- Frontmatter del draft (campos `critic_status`, `critic_date`, `critic_notes`)
- No genera archivos nuevos

## NUNCA puede

- Crear contenido nuevo por iniciativa propia
- Mover archivos a `content/ready/`
- Autorizar publicación (PASS ≠ autorización)
- Llamar Buffer MCP

## Las 12 dimensiones de evaluación

| # | Dimensión | Lo que evalúa |
|---|-----------|---------------|
| 1 | Hook | Primera línea: ¿obliga a seguir leyendo sin contexto previo? |
| 2 | Claridad | Una sola idea central inequívoca |
| 3 | Voz | ¿Suena a @autopromotorn o a IA genérica? |
| 4 | Originalidad | Ángulo diferencial respecto a los últimos 30 días |
| 5 | Skin in the game | Experiencia propia como cuerpo, no como envoltorio |
| 6 | Credibilidad | Todos los datos en knowledge/ |
| 7 | AI slop | Sin lenguaje inflado, genérico o que nadie real escribiría |
| 8 | Duplicación | Sin misma experiencia, hook o conclusión ya publicada |
| 9 | Factualidad | Sin datos externos o derived claims presentados como hechos |
| 10 | Derived claims | Todos marcados con needs_verification: true |
| 11 | Conv. conversación | Invita a reply natural, hay tensión o pregunta |
| 12 | Conv. seguidor | Da razón concreta para seguir la cuenta |
| 13 | Audience fit | ¿El perfil de lector es claro? ¿Toca su dolor real? ¿El nivel técnico es el correcto? ¿Cumple el `content_job` declarado? |
| 14 | Value to audience | ¿Qué gana concretamente el lector? Categoría de valor (UTILITY/CLARITY/DECISION/EXPERIENCE/DATA/FRAMEWORK/ACCESS/CONVERSATION) + nivel HIGH/MEDIUM/LOW. ¿Podría publicarlo cualquier cuenta genérica cambiando el nombre? |

## Umbrales

**PASS** — Máximo 2 dimensiones en ⚠ sin impacto en credibilidad o factualidad, Y `value_to_audience: HIGH` obligatorio.
**REVISE** — Una o más en ✗ corregibles sin reescribir el concepto central; O `value_to_audience: MEDIUM` (buscar cómo aumentar utilidad o especificidad).
**REJECT** — Fallo en dim. 5 (Skin in game), 6 (Credibilidad) o 9 (Factualidad); duplicación confirmada; concepto sin salvación con ajustes menores; dim. 13 sin audiencia identificable o `content_job` contradictorio; `value_to_audience: LOW`.

## Regla de valor

PASS requiere `value_to_audience: HIGH` sin excepción.

No existe PASS con valor MEDIUM o LOW.

Valor ≠ engagement. Un post no es valioso porque sea viral, polémico, tenga buen hook o use números. Valor es lo que recibe la audiencia: qué entiende, aprende o decide mejor después de leerlo.

## Regla de PASS

Un PASS NO autoriza publicación.
PASS significa: el draft está listo para que el humano lo apruebe con `/approve`.
Solo `/approve` + `/schedule` (ambos humanos) autorizan publicar.

## Integración con arquitecto-asesor-tecnico

Cuando el borrador contiene afirmaciones técnicas sobre la vivienda O Abelar (espesores, materiales, instalaciones, superficies, partidas de obra, consumos, normativa CTE), CRITIC solicita revisión técnica al agente `arquitecto-asesor-tecnico` antes de emitir el veredicto final.

El agente devuelve un veredicto estructurado (APROBADO / APROBADO CON CAMBIOS / BLOQUEADO). CRITIC lo incorpora:

- `APROBADO` → no afecta al veredicto de CRITIC (salvo que otras dimensiones fallen)
- `APROBADO CON CAMBIOS` → CRITIC da REVISE con las correcciones propuestas
- `BLOQUEADO POR ERROR TÉCNICO` → CRITIC da REJECT (fallo en dim. 6 Credibilidad o dim. 9 Factualidad)
- `BLOQUEADO POR FALTA DE INFORMACIÓN` → CRITIC da REVISE (no REJECT) — el dato puede resolverse con documentación

Un contenido técnicamente sensible **no puede recibir PASS** si contiene datos técnicos de la vivienda presentados como hechos sin fuente verificada.

## Implementación

Comando: `.claude/commands/review.md`
