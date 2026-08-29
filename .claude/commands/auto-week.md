# /auto-week

Genera automáticamente la próxima semana completa de contenido para @AutopromotorN.

Objetivo:
producir una semana lista para usar con mínima intervención humana.

Proceso:

1. Revisar:
   - `CLAUDE.md`
   - `knowledge/BIBLIOTECA_INTELECTUAL_AUTOPROMOTORN_V2.md`
   - `knowledge/autopromotorN_8_pilares_32_tweets.md` (versión canónica — ignorar `contenido/biblioteca-8-pilares-32-tweets.md`)
   - `knowledge/SEPTIEMBRE_2026_AUTOPROMOTORN.md` (READY/SCHEDULED = ya utilizado, no repetir)
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
   - experiencias nuevas;
   - temas repetidos;
   - huecos editoriales.

4. Crear calendario de 7 días.

5. Generar el texto final de cada publicación.

6. Para cada pieza generar internamente:
   - A directa;
   - B personal;
   - C provocadora.

7. Elegir solo la mejor.

8. Aplicar filtro final:
   - experiencia real;
   - cifra si existe;
   - tensión;
   - voz humana;
   - no repetición;
   - hook;
   - brevedad;
   - coherencia.

9. Clasificar:

AUTO:
- obra;
- familia;
- evergreen;
- reflexión sin datos externos.

REVIEW:
- hilo;
- inversión;
- hipoteca;
- datos actuales;
- estadística;
- tema polémico.

10. Guardar:
- AUTO en `content/ready/`
- REVIEW también en `content/ready/`, marcados como pendientes.

11. Publicación con Buffer MCP:
- Herramienta: Buffer MCP (`mcp__buffer__*`)
- Programar ÚNICAMENTE posts AUTO.
- NO programar REVIEW sin aprobación expresa del usuario.
- NO programar durante la semana — solo en sesión de sábado o domingo.
- Orden de prioridad al programar:
  1. Novedades de obra de la semana → slot jueves
  2. Actualidad del nicho → slot lunes o miércoles
  3. Borradores atemporales de `content/drafts/` → resto de slots
- Mantener siempre mínimo 5 posts programados en Buffer.
- Para programar: llamar primero `get_account` para obtener `organizationId`, luego `list_channels` para obtener `channelId`.

12. Guardar el calendario final en:
`content/scheduled/SEMANA-YYYY-MM-DD.md`

Formato final:

# SEMANA

## Día / fecha / hora

Pilar:
Marco:
Concepto propio:
Experiencia:
Formato:
Modo:
Nota visual:

### Texto final

[texto listo para publicar]

### Por qué se eligió
[1-2 líneas]

Repetir para los 7 días.
