# /auto-week

Genera el plan editorial de la próxima semana completa para @AutopromotorN.

⚠️ REGLA CRÍTICA: Este comando genera borradores y un calendario de planificación.
NO programa nada en Buffer. NO mueve archivos a content/ready/.
El pipeline obligatorio es siempre: /review → /approve → /schedule.

---

Proceso:

1. Revisar:
   - `CLAUDE.md`
   - `knowledge/` (todos los archivos)
   - `editorial/BIBLIOTECA_INTELECTUAL_AUTOPROMOTORN_V2.md`
   - `editorial/PILARES_32_TWEETS.md`
   - `content/planning/SEPTIEMBRE_2026_CANDIDATOS.md` (READY/SCHEDULED = ya utilizado, no repetir)
   - `content/published/`
   - `contenido/tweets-publicados.md`
   - `content/ideas/`
   - `content/ready/`
   - `content/scheduled/`
   - `content/drafts/`
   - `inbox/notes/`

2. Revisar publicaciones de al menos los últimos 30 días.

3. Detectar:
   - marcos infrautilizados;
   - experiencias nuevas sin explotar;
   - temas repetidos a evitar;
   - huecos editoriales por pilar.

4. Crear calendario de 7 días siguiendo `knowledge/CONTENT_PILLARS.md` y las reglas de cadencia de `knowledge/CADENCIA.md`.

   Reglas de cadencia obligatorias:

   - Objetivo mínimo: 7 publicaciones HIGH VALUE / semana. Rango habitual: 7–9. Máximo MVP: 10–11.
   - **Domingo = pieza principal de la semana.** Elegir el borrador con mayor combinación de value_to_audience, originalidad, skin_in_the_game y potencial de conversación. No asignar el domingo a una pieza secundaria si existe una pieza claramente superior.
   - **Segunda publicación del día:** permitida solo si ambas tienen value_level HIGH, aportan valor diferente, content_jobs distintos o complementarios, no compiten entre sí, y existe separación horaria suficiente. No desequilibrar el calendario semanal.
   - No convertir ideas simples en hilos para aumentar volumen.
   - Si ocurre un acontecimiento real HIGH VALUE (obra, imprevisto, coste real): puede sustituir o mover una pieza programada.

4.5. **Value Gate por slot** — Antes de asignar una pieza a un slot, verificar que tiene VALUE PROMISE formulable y categoría de valor clara.

Si para un slot no hay idea con valor HIGH claro:
→ Dejar el slot vacío: `[slot vacío — no hay pieza de valor suficiente]`
→ No generar relleno.
→ No bajar el umbral de calidad para completar el calendario.

Un calendario con huecos es correcto. Un calendario lleno de piezas mediocres no lo es.

5. Generar el texto final de cada publicación.

6. Para cada pieza generar internamente:
   - A directa;
   - B personal;
   - C provocadora.
   Elegir solo la mejor.

7. Aplicar filtro final:
   - value_promise formulable (si no → excluir la pieza del calendario);
   - value_category identificable;
   - experiencia real;
   - cifra si existe en knowledge/;
   - tensión;
   - voz humana (editorial/VOICE.md);
   - no repetición verificada;
   - hook (editorial/HOOKS.md);
   - brevedad;
   - coherencia editorial.

8. Clasificar cada pieza con risk_level:

   risk_level: low
   → obra, familia, evergreen, reflexión sin datos externos ni derived claims.

   risk_level: review
   → hilo, inversión, hipoteca, datos actuales, estadística, tema polémico,
     cualquier dato que no esté verificado en knowledge/, derived claims.

   ⚠️ risk_level NO es autorización de publicación.
   TODA pieza requiere /approve humano antes de /schedule.

9. Guardar TODOS los borradores en `content/drafts/`:
   - Un archivo por pieza: `draft-[slug]-YYYY-MM-DD.md`
   - Frontmatter obligatorio:
     ```
     draft_date: YYYY-MM-DD
     pillar:
     risk_level: low | review
     value_category: [categoría]
     value_promise: "[promesa]"
     facts_used: []
     derived_claims: []
     needs_verification: []
     critic_status: pending
     ```

10. Guardar el calendario de planificación en:
    `content/scheduled/SEMANA-YYYY-MM-DD.md`
    Este archivo es solo un índice de planificación, no autorización de publicación.

Formato del calendario:

# SEMANA YYYY-MM-DD

## [Día] / [fecha] / [hora propuesta]

Pilar:
Marco:
Concepto propio:
Experiencia:
Formato:
risk_level:
Draft: content/drafts/[nombre].md
Nota visual:

### Texto final
[texto listo para revisión]

### Por qué se eligió
[1-2 líneas]

---

Siguiente paso para cada pieza: /review [draft-name] → /approve → /schedule
