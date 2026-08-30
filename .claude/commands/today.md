# /today

Selecciona y genera el mejor borrador posible para publicar hoy.

⚠️ REGLA: Este comando genera un borrador en content/drafts/.
NO guarda en content/ready/. Para publicar: /review → /approve → /schedule.

---

Proceso:

1. Revisar:
   - `knowledge/` (todos los archivos)
   - `content/published/`
   - `contenido/tweets-publicados.md`
   - `autopromotorn_claude_content_os/knowledge/SEPTIEMBRE_2026_AUTOPROMOTORN.md` (READY/SCHEDULED = ya utilizado)
   - `content/ideas/`
   - `content/ready/`
   - `content/scheduled/`
   - `content/drafts/`
   - `inbox/notes/`

2. Evitar repetición de experiencia, ángulo o conclusión ya publicados.

3. Priorizar una experiencia reciente si existe en inbox/notes/.

4. Seleccionar máximo 3 candidatos con mayor potencial para hoy.

5. Para cada candidato calcular:
   - value_promise formulable (eliminar candidatos sin promesa clara);
   - value_category identificada;
   - personalización;
   - originalidad respecto al historial;
   - fuerza del hook;
   - experiencia real propia;
   - tensión editorial;
   - potencial de conversación.

Si ningún candidato tiene value_promise formulable:
→ Devolver: NO HAY PIEZA DE VALOR SUFICIENTE PARA HOY
→ No generar contenido.
→ No generar relleno de calendario.

6. Elegir el mejor candidato.

7. Generar internamente versiones A/B/C.

8. Guardar solo la mejor versión en `content/drafts/draft-today-YYYY-MM-DD.md`
   con frontmatter:
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

Mostrar al usuario:
- Texto final del borrador
- Pilar y marco editorial usado
- Motivo de selección sobre los otros candidatos
- risk_level y qué lo determina
- Nota visual (imagen recomendada si aplica)
- Siguiente paso: /review draft-today-YYYY-MM-DD
