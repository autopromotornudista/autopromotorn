# /review

CRITIC AGENT — Evalúa `$ARGUMENTS` (draft_id o ruta a content/drafts/).

⚠️ REGLA: Este comando evalúa y devuelve PASS | REVISE | REJECT.
Un PASS NO autoriza publicación. Solo /approve (humano) → /schedule (humano) autorizan publicar.

---

## Proceso

1. Leer el draft indicado en `content/drafts/`.
   Si no se encuentra, reportar el error y detenerse.

2. Leer el `idea_id` del frontmatter del draft y cargar `content/ideas/[idea_id].md` si existe.

3. Leer `knowledge/` completo para verificación factual.

4. Leer `editorial/VOICE.md` y `editorial/FORMATS.md` para verificación de voz.

5. Verificar deduplicación en las 6 fuentes obligatorias:
   - `content/published/`
   - `contenido/tweets-publicados.md`
   - `content/planning/SEPTIEMBRE_2026_CANDIDATOS.md`
   - `content/ready/`
   - `content/scheduled/`
   - `content/drafts/` (otros drafts)

6. Evaluar el draft en las 14 dimensiones siguientes.

7. Devolver el informe CRITIC (formato abajo).

8. Actualizar el frontmatter del draft con `critic_status` y `critic_date`.

---

## Las 12 dimensiones de evaluación

Para cada dimensión: ✓ PASA | ⚠ ALERTA | ✗ FALLA + breve explicación.

1. **Hook** — ¿La primera línea atrapa sin contexto previo? ¿Obliga a seguir leyendo?
2. **Claridad** — ¿Hay una sola idea central inequívoca? ¿El lector sabe qué se le está diciendo?
3. **Voz** — ¿Suena a @autopromotorn o podría publicarlo cualquier cuenta de finanzas/vivienda?
4. **Originalidad** — ¿El ángulo es diferencial respecto al historial de los últimos 30 días?
5. **Skin in the game** — ¿La experiencia propia es el cuerpo del post, no el envoltorio?
6. **Credibilidad** — ¿Todos los datos están en `knowledge/`? ¿Algún dato aparece sin respaldo?
7. **AI slop** — ¿Hay frases que ninguna persona real escribiría? ¿Lenguaje inflado o genérico?
8. **Duplicación** — ¿Misma experiencia, mismo hook o misma conclusión ya publicados?
9. **Factualidad** — ¿Algún dato externo o derived claim presentado como hecho verificado?
10. **Derived claims** — ¿Están marcados con `needs_verification: true` en el frontmatter?
11. **Potencial de conversación** — ¿Invita a reply natural? ¿Hay tensión o pregunta abierta?
12. **Potencial de conversión** — ¿Da una razón concreta para seguir la cuenta?
13. **Audience fit** — ¿El perfil de lector (A/B/C/D) es claro? ¿El vocabulario y profundidad son los correctos para ese perfil? ¿Cumple el `content_job` declarado?
14. **Value to audience** — ¿Qué gana concretamente el lector? Determinar: (a) categoría (UTILITY/CLARITY/DECISION/EXPERIENCE/DATA/FRAMEWORK/ACCESS/CONVERSATION), (b) nivel HIGH/MEDIUM/LOW. ¿Podría publicarlo una cuenta genérica sin cambiar nada? Si sí → no es HIGH.

---

## Formato del informe CRITIC

```
══════════════════════════════════════════
CRITIC REPORT — [draft_id]
Fecha: YYYY-MM-DD
══════════════════════════════════════════

VEREDICTO: PASS | REVISE | REJECT

──────────────────────────────────────────
DIMENSIONES
──────────────────────────────────────────
1.  Hook              ✓ | ⚠ | ✗   [explicación breve]
2.  Claridad          ✓ | ⚠ | ✗   [explicación breve]
3.  Voz               ✓ | ⚠ | ✗   [explicación breve]
4.  Originalidad      ✓ | ⚠ | ✗   [explicación breve]
5.  Skin in the game  ✓ | ⚠ | ✗   [explicación breve]
6.  Credibilidad      ✓ | ⚠ | ✗   [explicación breve]
7.  AI slop           ✓ | ⚠ | ✗   [explicación breve]
8.  Duplicación       ✓ | ⚠ | ✗   [explicación breve]
9.  Factualidad       ✓ | ⚠ | ✗   [explicación breve]
10. Derived claims    ✓ | ⚠ | ✗   [explicación breve]
11. Conv. conversación ✓ | ⚠ | ✗  [explicación breve]
12. Conv. seguidor    ✓ | ⚠ | ✗   [explicación breve]
13. Audience fit      ✓ | ⚠ | ✗   [explicación breve]
14. Value to audience ✓ | ⚠ | ✗   [explicación breve]

──────────────────────────────────────────
VALUE TO AUDIENCE
──────────────────────────────────────────
category:         [UTILITY | CLARITY | DECISION | EXPERIENCE | DATA | FRAMEWORK | ACCESS | CONVERSATION]
level:            HIGH | MEDIUM | LOW
concrete benefit: [qué gana el lector en 1 frase]
non-generic:      [qué hace que solo @autopromotorn pueda publicar esto]

──────────────────────────────────────────
ACCIONES REQUERIDAS (si REVISE o REJECT)
──────────────────────────────────────────
[Lista numerada de cambios concretos o razón de rechazo]

──────────────────────────────────────────
SIGUIENTE PASO
──────────────────────────────────────────
PASS   → /approve [draft_id]  (requiere decisión humana)
REVISE → corregir las acciones indicadas → /review [draft_id]
REJECT → idea puede reutilizarse con otro ángulo o descartarse
══════════════════════════════════════════
```

---

## Umbrales de veredicto

**PASS** — Todas las dimensiones en ✓ o máximo 2 en ⚠ sin impacto en credibilidad, Y `value_to_audience: HIGH` obligatorio.
**REVISE** — Una o más dimensiones en ✗ corregibles sin reescribir el concepto; O `value_to_audience: MEDIUM`.
**REJECT** — Fallo en Credibilidad, Factualidad o Skin in the game; duplicación confirmada; concepto sin salvación con ajustes menores; O `value_to_audience: LOW`.

---

## Frontmatter del draft tras /review

Actualizar estos campos en el archivo draft:

```
critic_status: PASS | REVISE | REJECT
critic_date: YYYY-MM-DD
critic_notes: [resumen de 1 línea del veredicto]
value_level: HIGH | MEDIUM | LOW
```
