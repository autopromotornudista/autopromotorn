---
status: approved
visibility: editorial
last_updated: 2026-08-30
source_type: human_approved
---

# EDITORIAL_RULES.md — Reglas editoriales

## Reglas absolutas

1. **Aprobación humana antes de publicar.** Todo el contenido requiere revisión y aprobación del propietario antes de llegar a cualquier canal.

2. **No inventar.** Nunca inventar datos, experiencias, fechas, precios, nombres o situaciones. Si no existe un dato real confirmado, no se usa.

3. **No publicar datos privados.** Que un dato exista en el repositorio o haya sido mencionado en sesión no lo convierte en editorial. Solo los datos en `knowledge/` con aprobación explícita son editoriales.

4. **Separar fuente externa de experiencia propia.** Si el contenido parte de un marco externo (libro, artículo, concepto), la experiencia propia debe ser el cuerpo del post. El marco externo es el punto de partida, no el contenido.

5. **Nunca automatizar replies.** Los replies en X son siempre manuales y revisados. Nunca automatizados.

---

## Deduplicación (protocolo obligatorio)

Antes de generar contenido nuevo, revisar en este orden:

1. `content/published/`
2. `contenido/tweets-publicados.md`
3. `content/ready/`
4. `content/scheduled/`
5. `knowledge/SEPTIEMBRE_2026_AUTOPROMOTORN.md` (o el archivo de mes vigente)
6. `content/drafts/`

**Qué evitar repetir:** misma experiencia · mismo dato con enfoque demasiado similar · mismo hook · misma conclusión.

El tema puede repetirse; la historia y el ángulo no.

---

## Atribución

Cuando el contenido parte de un marco conceptual externo (Joan Tubau u otros):

- No resumir el artículo externo
- No copiar el tono del autor
- Usar el marco como detonante, no como contenido
- El flujo correcto: ARTÍCULO → TESIS → MARCO → EXPERIENCIA REAL → POST ORIGINAL

---

## Polémica

La posición contundente solo se publica si es defendible con datos reales o experiencia propia.

No provocar por provocar. Una opinión fuerte sin respaldo propio deteriora la credibilidad de la cuenta.

---

## Buffer como cola editorial

Buffer es la herramienta de programación, no el canal de aprobación.

El flujo correcto:
1. Borrador generado
2. Revisión y aprobación humana
3. Entrada en Buffer
4. Publicación programada

Buffer no decide qué se publica. Solo ejecuta lo ya aprobado.

---

## WordPress como activo editorial

WordPress es un activo propio con mayor permanencia que X.

El contenido para WordPress requiere revisión humana antes de publicar, igual que X. La mayor extensión y permanencia del formato aumenta la importancia de la revisión.

---

## Email como activo propio

Cuando se arranque el canal de email, la misma regla de aprobación aplica. La audiencia de email es la más valiosa: el umbral de calidad y precisión del contenido es igual o superior al de X.

---

## Conservación de archivos legacy

Los archivos en `contenido/` (legacy) no se borran, mueven ni sobreescriben sin autorización expresa del propietario.

Si se detecta un conflicto entre `contenido/` legacy y `content/` canónico, señalarlo y esperar aprobación.

---

## Proceso de actualización de knowledge

Cuando un dato de `knowledge/` quede desactualizado:

1. Señalarlo explícitamente en sesión
2. Proponer la actualización con fuente
3. Esperar aprobación humana
4. Actualizar el archivo con `last_updated` en frontmatter
5. Incluir en el próximo commit de knowledge

No actualizar `knowledge/` de forma silenciosa entre commits.

---

## Regla de knowledge

**Existir en un archivo versionado del repositorio NO equivale a estar aprobado para knowledge.**

El proceso siempre es: SOURCE → extracción → validación → aprobación humana → KNOWLEDGE.

Knowledge nunca debe utilizarse para reconstruir información privada que se ha decidido deliberadamente excluir.

---

## Información volátil sobre el sistema de X

La siguiente información debe tratarse siempre como **hipótesis**, no como knowledge estable:

- comportamiento del algoritmo de ranking
- timing óptimo de publicación
- formatos que favorece o penaliza el algoritmo
- impacto de incluir enlaces en posts
- volumen óptimo de replies diarios
- horarios de mayor alcance
- tamaño ideal de cuentas objetivo para engagement

**Por qué:** los sistemas de ranking de X (actualmente Phoenix) cambian sin previo aviso y sin publicación de documentación oficial. Los coeficientes que circulan públicamente pertenecen a versiones históricas del algoritmo y no pueden asumirse como vigentes.

**Única fuente de verdad local:** los experimentos propios de @AutopromotorN documentados en `metrics/EXPERIMENTS.md`. Solo los resultados experimentales con fecha, muestra, métrica y periodo definidos pueden producir conclusiones locales sobre el comportamiento de esta cuenta.
