# PRIVATE_DOCS.md — Índice de Documentación Privada Local

Este archivo es un índice abstracto. No contiene datos sensibles, cifras, nombres,
identificadores ni información privada de ningún tipo.

Su función es indicar a Claude Code, ChatGPT y OpenClaw que existe documentación
privada en la instalación local del propietario, excluida del repositorio Git por
contener información personal, financiera y legal.

---

## Principio de tres niveles

```
PRIVATE SOURCES     → solo en disco local (este índice los referencia)
KNOWLEDGE APPROVED  → en Git, en knowledge/ (datos editoriales autorizados)
PUBLIC CONTENT      → en Git, en content/published/ (lo publicado en canales)
```

Que un dato exista en PRIVATE SOURCES **no autoriza a ningún agente a utilizarlo
editorialmente**. Solo los datos presentes en `knowledge/` están aprobados para
uso en contenido.

---

## Categorías de documentación privada existente

### Documentación hipotecaria y bancaria

Existe documentación relacionada con la financiación del proyecto de construcción.
Incluye documentos precontractuales, condiciones del préstamo, simulaciones,
seguros vinculados y correspondencia con la entidad bancaria.

Ubicación local: `docs/hipoteca/`
Estado en Git: carpeta vacía preservada con `.gitkeep`

### Tasaciones

Existen informes de tasación oficial del inmueble y del proyecto.

Ubicación local: `docs/tasacion/`
Estado en Git: carpeta vacía preservada con `.gitkeep`

### Presupuestos y contratos de construcción

Existen presupuestos detallados y contratos con los diferentes proveedores
intervinientes en la obra (constructor principal, instalaciones, carpintería,
cocina, fontanería y otros).

Ubicación local: `docs/presupuestos-construccion/`
Estado en Git: carpeta vacía preservada con `.gitkeep`

### Estimación financiera del proyecto

Existe un documento de estimación detallada de costes totales del proyecto,
con comparativa entre presupuesto inicial y coste real actualizado.

Ubicación local: `docs/finanzas/`
Estado en Git: carpeta vacía preservada con `.gitkeep`

### Proyecto arquitectónico completo

Existe el proyecto técnico visado por el arquitecto, incluyendo memorias,
planos, cálculos de estructura e instalaciones, estudios complementarios,
mediciones, presupuestos y documentación de dirección de obra.

Ubicación local: `docs/Proxecto Vivenda O Abelar/`
Estado en Git: carpeta vacía preservada con `.gitkeep`

### Fotografías reales del terreno y obra

Existen fotografías del terreno y del avance de la obra tomadas por el
propietario. Pueden contener metadatos EXIF con información de localización.

Ubicación local: `docs/fotos-reales/`
Estado en Git: carpeta vacía preservada con `.gitkeep`

### Renders del proyecto arquitectónico

Existen renders 3D del proyecto producidos durante la fase de diseño.

Ubicación local: `docs/renders/`
Estado en Git: carpeta vacía preservada con `.gitkeep`

### Informes de contexto generados automáticamente

Existen documentos HTML interactivos que resumen la situación financiera y
la evolución del proyecto, generados a partir de fuentes privadas.
Por contener datos extraídos de documentos privados sin pasar por el
filtro editorial de aprobación, se excluyen de Git.

Ubicación local: `docs/contexto-ia/`
Estado en Git: carpeta vacía preservada con `.gitkeep`

---

## Instrucciones para una instalación local completa

Si clonas este repositorio en un equipo nuevo y necesitas acceder a la
documentación privada, deberás copiarla manualmente desde el backup privado
del propietario a las carpetas indicadas arriba.

El backup privado del proyecto (documentación original) se gestiona de forma
independiente a este repositorio Git y no está en GitHub.

Consulta al propietario del proyecto para obtener acceso.

---

## Lo que SÍ está disponible en este repositorio

Todo el contenido editorial, estratégico y de conocimiento aprobado está
versionado en Git y disponible sin restricciones para Claude Code, ChatGPT
y OpenClaw:

- `knowledge/` — Knowledge Approved: datos editoriales autorizados
- `content/` — borradores, ideas, publicaciones
- `contenido/` — historial legacy
- `docs/*.md` — guías, análisis, diario de obra (sin datos privados)
- `.claude/` — configuración de Claude Code
- `scripts/` — automatización
- `agents/` — definiciones de agentes (cuando se creen)
- `inbox/` — entrada de contenido a procesar
- `metrics/` — métricas estructuradas (cuando se generen)
