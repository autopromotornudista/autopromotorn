# /week

Prepara el calendario editorial de los próximos 7 días.

Proceso:

1. Revisar publicaciones de los últimos 30 días en:
   - `content/published/`
   - `contenido/tweets-publicados.md`
   - `knowledge/SEPTIEMBRE_2026_AUTOPROMOTORN.md` (READY/SCHEDULED = ya utilizado, no repetir)
   - `content/ready/`
   - `content/scheduled/`
   - `content/drafts/`
2. Revisar ideas disponibles.
3. Revisar experiencias nuevas.
4. Revisar los 8 pilares.
5. Revisar la biblioteca intelectual.
6. Evitar repetir experiencias o marcos en días consecutivos.
7. Buscar variedad.

Referencia editorial:

- 40% obra real
- 25% vivienda/economía
- 20% finanzas personales
- 15% opinión/debate/familia

Para cada día:

- fecha;
- hora recomendada;
- pilar;
- marco;
- experiencia;
- formato;
- tema;
- modo AUTO/REVIEW.

No es necesario generar todos los textos completos salvo que se solicite.

Guardar calendario en `content/scheduled/`.

## Programar contenido

Este comando NO llama a Buffer. Solo planifica y genera borradores.

Para programar el contenido en Buffer:
1. Ejecutar `/review [draft-id]` por cada borrador → necesita PASS + value HIGH
2. Ejecutar `/approve [draft-id]` → gate humano obligatorio
3. Ejecutar `/schedule [ready-id] [fecha] [hora]` → único punto autorizado para Buffer

Solo `/schedule` puede crear posts en Buffer.
