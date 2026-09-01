# /forum-scout

Agente de investigación de audiencia. Analiza el subforo público de SoloArquitectura (promotores y autopromotores), detecta preocupaciones reales y genera ideas + borradores automáticamente cuando el score lo justifica.

**Lectura obligatoria antes de ejecutar:** `agents/FORUM_SCOUT.md`

---

## Flags

| Flag | Efecto |
|------|--------|
| (sin flags) | Novedades desde `last_processed_date` en STATE.md |
| `--days N` | Hilos de los últimos N días |
| `--bootstrap` | Primera ejecución: hasta 10 páginas históricas del foro |
| `--dry-run` | Muestra lo que haría sin escribir ningún archivo |

---

## Protocolo de ejecución

### PASO 0 — Verificación inicial (solo primera vez o si STATE.md está vacío)

```
1. WebFetch https://www.soloarquitectura.com/robots.txt
   → Si el subforo o el RSS están excluidos: DETENER. Informar al usuario.
   → Si están permitidos: continuar.
```

### PASO 1 — Leer estado

```
1. Leer sources/forum/STATE.md
2. Cargar: last_processed_date, last_rss_entry_id, set de URLs ya procesadas
3. Si STATE.md no existe o está vacío → asumir primera ejecución (tratar como --bootstrap)
```

### PASO 2 — Fetch RSS

```
1. WebFetch https://www.soloarquitectura.com/foros/forums/promotores-y-autopromotores.45/index.rss
2. Si 403/429/error → registrar en STATE.md errors[] + DETENER (no reintentar)
3. Parsear XML: extraer entradas con {id, title, link, pubDate, author, description}
4. Filtrar entradas nuevas: link NO en STATE.md hilos procesados
   Y pubDate >= last_processed_date (o según --days N si se especifica)
5. Si --bootstrap: procesar hasta 50 entradas históricas (10 páginas ~5 hilos/página)
```

### PASO 3 — Visita selectiva a hilos

```
Para cada entrada nueva (en orden cronológico inverso):
  1. Calcular score RSS preliminar:
     - recency_score: fecha del hilo (ver tabla en FORUM_SCOUT.md)
     - Si el RSS incluye reply_count → añadir activity_score parcial

  2. Si score_preliminar > 40 (vale la pena visitar):
     → WebFetch [link del hilo]
     → Pausa 3 segundos entre peticiones
     → Si 403/429: registrar error, saltar este hilo, continuar con el siguiente
     → Extraer:
        · Número de respuestas y visitas (si visibles)
        · Preguntas explícitas de los usuarios
        · Preocupaciones subyacentes (lo que realmente les preocupa)
        · Fase de autopromoción predominante
        · Intensidad del debate
        · Recurrencia (¿cuántos usuarios distintos expresan la misma preocupación?)
        · Menciones a dinero, riesgo, retrasos, decisiones irreversibles

  3. Calcular score final (0-100) según fórmula en FORUM_SCOUT.md

  4. Registrar en STATE.md: {url, date_seen, hash_title+concern, score, status}
```

### PASO 4 — Generación automática por umbral de score

```
Para cada hilo con score final ≥ 60:

  A. Verificar deduplicación semántica:
     → ¿Existe ya una IDEA o draft con la misma preocupación subyacente?
     → Comprobar en: content/ideas/forum/ · content/ideas/ · content/drafts/
     → Si hay duplicado semántico: registrar como "duplicado" en STATE.md, no crear idea

  B. Crear content/ideas/forum/FORUM-YYYYMMDD-NNN.md
     (ver formato completo en content/ideas/forum/README.md)

  C. Verificar si hay experiencia validada en knowledge/ que conecte con el ángulo:
     → Leer knowledge/INDEX.md para orientarse
     → Si NO hay conexión con knowledge/ validado:
        - Dejar IDEA en status: pending_context
        - Añadir nota: "Sin experiencia propia validada — esperar dato real antes de redactar"
        - NO llamar a WRITER
        - Continuar con siguiente insight

  D. Si SÍ hay conexión con knowledge/ → llamar a WRITER:
     → Instrucción a WRITER: "Genera un borrador que responda y resuelva el punto de dolor
        detectado en FORUM-XXX. El dolor/preocupación viene del foro y es el problema que el
        contenido debe resolver. La respuesta y los hechos vienen exclusivamente de knowledge/.
        El borrador debe dejar al lector con una respuesta concreta, una decisión más clara,
        o un aprendizaje accionable — no solo con el problema planteado.
        Marcar needs_verification: true en cualquier claim no verificado en knowledge/.
        Si score ≥ 80: añadir value_level: HIGH en el frontmatter."
     → WRITER genera content/drafts/draft-[slug]-YYYY-MM-DD.md

  E. Llamar a CRITIC sobre el draft generado:
     → CRITIC evalúa las 14 dimensiones
     → Actualiza critic_status en el draft
     → Si PASS: draft queda listo para /approve humano
     → Si REVISE o REJECT: draft queda flaggeado con las notas del CRITIC
```

### PASO 5 — Actualizar STATE.md

```
1. Actualizar: last_run, last_rss_entry_id, last_processed_date
2. Incrementar contadores: total_threads_seen, total_insights_generated
3. Añadir filas a tabla de hilos procesados
4. Registrar errores si los hubo
```

### PASO 6 — Resumen de ejecución

Mostrar siempre al finalizar:

```
## FORUM_SCOUT — Resumen [fecha]

Hilos analizados: N
Hilos nuevos: N
Insights generados (score ≥ 60): N
  · Borradores CRITIC PASS: N → listos para /approve
  · Borradores CRITIC REVISE/REJECT: N → requieren revisión
  · Ideas sin experiencia propia (pending_context): N
Hilos archivados (score < 60): N
Errores: N

Próxima ejecución recomendada: [fecha + 3-4 días]
```

---

## Modo --dry-run

En modo dry-run:
- Ejecutar PASOS 1-3 normalmente (leer, fetch, analizar)
- En PASO 4: mostrar en pantalla lo que crearía (título del hilo, score, acción prevista) SIN escribir ningún archivo
- En PASO 5: NO actualizar STATE.md
- Mostrar resumen con etiqueta [DRY-RUN]

---

## Modo --bootstrap

En modo bootstrap (primera ejecución):
- Ignorar `last_processed_date` (no existe)
- Procesar hasta 50 entradas RSS (aproximadamente las últimas 10 páginas del subforo)
- Después de bootstrap: STATE.md queda inicializado para ejecuciones incrementales futuras
- Recomendado: ejecutar primero con `--bootstrap --dry-run` para revisar antes de crear archivos

---

## Errores y aborto

| Código HTTP | Acción |
|-------------|--------|
| 403 Forbidden | Detener. Registrar en STATE.md. Informar al usuario. No reintentar. |
| 429 Too Many Requests | Detener. Esperar. No reintentar en la misma sesión. |
| 404 Not Found | Hilo eliminado o privado. Registrar como "unavailable" en STATE.md. Continuar. |
| Timeout | Registrar. Continuar con siguiente hilo. |
| Captcha / JS wall | Detener inmediatamente. No intentar eludir. |

---

## Archivos que este comando puede escribir

| Archivo | Condición |
|---------|-----------|
| `sources/forum/STATE.md` | Siempre (excepto --dry-run) |
| `content/ideas/forum/FORUM-*.md` | Solo si score ≥ 60 y no duplicado |
| `content/drafts/draft-*.md` | Solo si hay conexión con knowledge/ y WRITER ejecuta |

## Archivos que este comando NUNCA toca

`knowledge/` · `editorial/` · `content/ready/` · `content/scheduled/` · `VALIDATED_CONTEXT*` · Buffer MCP
