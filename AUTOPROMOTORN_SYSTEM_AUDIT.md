# AUTOPROMOTORN_SYSTEM_AUDIT.md

> Auditoría completa del sistema generada el 29 de agosto de 2026.
> Objetivo: preparar el repositorio para evolucionar hacia un sistema automatizado de creación y gestión de contenidos con Claude Code + OpenClaw + Buffer + WordPress + Telegram.
> **SOLO LECTURA — No ejecutar ninguna migración sin instrucciones explícitas.**

---

## RESUMEN EJECUTIVO

**AutopromotorN** es un proyecto de contenido editorial en construcción activa sobre autopromoción de vivienda y finanzas personales. Combina un sistema de gestión de conocimiento documentado, una estrategia editorial definida, infraestructura de Claude Code con MCP Buffer, y todo ello sincronizado con una obra de vivienda real en progreso (Casa Abelar, Galicia, iniciada agosto 2026).

**Estado General (29 agosto 2026)**
- Seguidores: 195 en X (@autopromotorn)
- Fase del proyecto: Obra iniciada (replanteo realizado 26/08/2026)
- Infraestructura: Claude Code + Buffer MCP + conocimiento estructurado + comandos automatizados
- Salud del sistema: BUENA — estructura definida, duplicidades detectadas y documentadas, lista para evolución

---

## 1. ESTRUCTURA DEL PROYECTO

```
/home/pineapple/proyectos/autopromotorn/
│
├── CLAUDE.md                                    ← Briefing y calendario editorial (230 líneas)
├── README.md
├── PROMPT_INICIAL_PARA_CLAUDE.md               ← Instrucciones de inicialización
│
├── autopromotorn_claude_content_os/            ← Content OS ESPEJO (DUPLICADO — ver sección 3)
│   ├── .claude/
│   │   └── commands/ (7 comandos: diary, today, week, auto-week, ideas, published, review)
│   ├── knowledge/
│   │   ├── BIBLIOTECA_INTELECTUAL_AUTOPROMOTORN_V2.md (2.491 líneas, 138 ideas editoriales)
│   │   ├── autopromotorN_8_pilares_32_tweets.md
│   │   └── SEPTIEMBRE_2026_AUTOPROMOTORN.md
│   ├── CLAUDE.md (idéntico al root)
│   ├── README.md
│   └── PROMPT_INICIAL_PARA_CLAUDE.md
│
├── .claude/
│   ├── commands/ (7 comandos idénticos a los del subdirectorio)
│   └── settings.local.json (permisos Buffer MCP, WebFetch, Bash)
│
├── contenido/                                   ← Content LEGACY (no modificar)
│   ├── biblioteca-8-pilares-32-tweets.md       ← V1 (obsoleta, superada por V2 en knowledge/)
│   ├── borradores/                             ← 5 drafts (probablemente duplicados de content/drafts/)
│   ├── tweets-publicados.md                    ← Historial incompleto (~8 tweets registrados)
│   ├── calendario.md
│   ├── formatos-y-ejemplos.md
│   ├── hooks.md
│   ├── ideas-contenido-hipoteca.md
│   ├── replies.md
│   └── tweets-desde-videos.md
│
├── content/                                     ← Content CANÓNICO (sistema nuevo)
│   ├── drafts/ (7 borradores actuales)
│   ├── ideas/ (ideas-sesion-27ago2026.md)
│   ├── published/ (historico-hasta-ago2026.md)
│   ├── ready/ (vacío)
│   └── scheduled/ (vacío)
│
├── docs/
│   ├── contexto-ia/
│   │   ├── casa_abelar_dossier.html
│   │   └── resumen_proyecto_y_situacion_financiera.html
│   ├── diario-obra.md                          ← Actualizado 26/08/2026
│   ├── guia-redaccion.md                       ← 4 formatos narrativos (298 líneas)
│   ├── analisis-contenido-historico.md         ← Análisis Grok de 823 tweets (291 líneas)
│   ├── hipoteca/ (14 documentos Unicaja)
│   ├── finanzas/ (Estimacion Gastos Casa.xlsx)
│   ├── presupuestos-construccion/ (10 PDFs)
│   ├── Proxecto Vivenda O Abelar/
│   ├── tasacion/ (2 tasaciones oficiales)
│   ├── fotos-reales/ (vacío)
│   ├── renders/ (vacío)
│   ├── fuentes/ (1 transcripción de podcast)
│   ├── ideas-contenido-familia.md
│   └── ideas-contenido-inversion.md
│
├── inbox/
│   ├── articles/
│   ├── notes/
│   ├── photos/
│   └── youtube/
│
├── metrics/   (vacío)
│
└── scripts/
    └── analizar_video.py
```

### Análisis por carpeta

| Carpeta | Función | Estado | Observaciones |
|---------|---------|--------|---------------|
| `autopromotorn_claude_content_os/` | Content OS espejo | ACTIVA (DUPLICADA) | Versión anterior del sistema. Contiene `knowledge/` que no existe en root. Ver decisión en sección Respuestas. |
| `contenido/` | Legacy content | CONGELADO | Sistema antiguo. REGLA activa: nunca borrar, sobrescribir, mover ni consolidar sin autorización. |
| `content/` | Sistema canónico nuevo | ACTIVO | Estructura clara: drafts, ideas, published, ready, scheduled. Es el futuro. |
| `docs/` | Contexto del proyecto | COMPLETO | Proyecto arquitectónico, hipotecas, presupuestos, guías, análisis. Muy bien documentado. |
| `inbox/` | Entrada de contenido | VACÍO | Estructura existe, carpetas vacías. Destinado a recibir material del Content Harvester. |
| `metrics/` | Métricas | VACÍO | Carpeta creada pero sin contenido. |
| `scripts/` | Automatización | MÍNIMO | 1 script funcional (analizar_video.py). |
| `.claude/` | Configuración Claude Code | ACTIVO | 7 commands + settings con permisos Buffer. |

---

## 2. INVENTARIO DE CONOCIMIENTO EXISTENTE

### Documentos Maestros

| Archivo | Contenido | Estado | Líneas | Reutilización |
|---------|----------|--------|--------|---------------|
| **BIBLIOTECA_INTELECTUAL_AUTOPROMOTORN_V2.md** | 27 marcos mentales de Joan Tubau + 138 ideas editoriales. Matriz pilar×marco×experiencia×tensión. | ACTUALIZADO | 2.491 | ALTÍSIMA — núcleo del contenido |
| **autopromotorN_8_pilares_32_tweets.md** | Banco de 32 tweets estructurados en 8 pilares. | V1 (puede estar parcialmente obsoleta) | 494 | MEDIA — la V2 es más potente |
| **SEPTIEMBRE_2026_AUTOPROMOTORN.md** | Contenido ready/scheduled para sept 2026: 6 hilos + 4 tweets de familia. | READY (calidad alta) | 666 | ALTA |
| **CLAUDE.md (root)** | Briefing de identidad, principios editoriales, calendario, reglas de deduplicación. | ACTUALIZADO | 230 | ALTÍSIMA — manifiesto de referencia |
| **guia-redaccion.md** | 4 formatos narrativos (A-D) con estructuras, ejemplos y reglas. | COMPLETO | 298 | ALTÍSIMA |
| **analisis-contenido-historico.md** | Análisis de 823 tweets, datos de engagement, timing, temas ya tratados. | ACTUALIZADO (11/08/2026) | 291 | ALTA |
| **formatos-y-ejemplos.md** | Mix editorial recomendado (40-50% dato+foto, 25-30% hilos, etc.) | COMPLETO | 100 | MEDIA-ALTA |
| **hooks.md** | 20 hooks de alto rendimiento documentados. | COMPLETO | 80 | MEDIA |

### Documentos de Contexto del Proyecto

| Archivo | Contenido | Estado |
|---------|----------|--------|
| **diario-obra.md** | Registro semanal de fase. Hitos completados. Cronología 2021-2026. Desglose de costes reales. Estado actual: replanteo hecho 26/08, pendiente excavación. | ACTUALIZADO (26/08/2026) |
| **tweets-publicados.md** | Historial de ~8 tweets publicados en agosto 2026 con engagement real. | INCOMPLETO (solo últimas 2 semanas) |
| **historico-hasta-ago2026.md** | Copia del anterior. | INCOMPLETO |
| **ideas-sesion-27ago2026.md** | 3 ideas editoriales con marcos y tensión. 1 desarrollada, 2 pendientes. | PARCIAL |
| **docs/fuentes/2026-08-17-podcast-precio-vivienda.md** | 1 transcripción de podcast. | ÚNICO EJEMPLO |

### Mapa de Conocimiento por Tema

| Tema | Archivo(s) Principal(es) |
|------|--------------------------|
| Historia de la cuenta | CLAUDE.md, analisis-contenido-historico.md |
| Estrategia editorial | CLAUDE.md, formatos-y-ejemplos.md |
| Voz y estilo | guia-redaccion.md, hooks.md |
| Pilares de contenido | BIBLIOTECA_V2.md, autopromotorN_8_pilares_32_tweets.md |
| Tweets publicados | contenido/tweets-publicados.md, content/published/ |
| Ideas pendientes | content/ideas/, contenido/ideas-contenido-*.md |
| Calendario | contenido/calendario.md, SEPTIEMBRE_2026.md |
| Métricas | analisis-contenido-historico.md (manual, snapshot ago 2026) |
| Hipoteca | docs/hipoteca/ (14 documentos Unicaja) |
| Presupuesto obra | docs/finanzas/Estimacion Gastos Casa.xlsx |
| Parcela/vivienda | docs/Proxecto Vivenda O Abelar/, docs/tasacion/ |
| Cronología del proyecto | docs/diario-obra.md |
| Inversión/patrimonio | docs/contexto-ia/resumen_proyecto_y_situacion_financiera.html |
| Fuentes externas | docs/fuentes/ (1 podcast), referencias a Joan Tubau en guia-redaccion.md |
| Joan Tubau y referentes | BIBLIOTECA_V2.md (27 marcos mentales) |

### Datos Detectados sin Documento Propio

- Patrimonio familiar (cartera inversión, Bitcoin, fondos monetarios) — mencionado en guia-redaccion.md sin inventario formalizado
- Educación de hijos sobre dinero — hay experiencia pero no documento dedicado
- Estrategia de inversión DCA (2.000€/mes) — mencionado sin historizar
- Métricas de Buffer — disponibles via MCP pero no capturadas
- Engagement histórico completo — existe en análisis, no como base de datos

---

## 3. DETECTAR DUPLICIDADES Y CONFLICTOS

### DUPLICIDAD CRÍTICA: `/autopromotorn_claude_content_os/`

| Elemento | Root | autopromotorn_claude_content_os | Estado |
|----------|------|----------------------------------|--------|
| `.claude/commands/` | ✅ 7 archivos | ✅ 7 archivos | DUPLICADOS EXACTOS |
| `CLAUDE.md` | ✅ 230 líneas | ✅ 230 líneas | IDÉNTICO |
| `README.md` | ✅ Existe | ✅ Existe | Probablemente idénticos |
| `knowledge/` | ❌ No existe en root | ✅ 3 archivos maestros | ASIMÉTRICO — información única aquí |
| `PROMPT_INICIAL_PARA_CLAUDE.md` | ✅ Existe | ✅ Existe | IDÉNTICO |

**Conclusión:** Es una versión anterior del sistema. La carpeta `knowledge/` contiene información que NO existe en root. Antes de cualquier operación sobre este directorio, verificar que su contenido esté íntegramente trasladado a root.

### DUPLICIDAD SECUNDARIA: `/contenido/` vs `/content/`

| Elemento | contenido/ (LEGACY) | content/ (CANÓNICO) | Estado |
|----------|---------------------|---------------------|--------|
| `biblioteca*.md` | ✅ V1 | ❌ No existe | SUPERADO por BIBLIOTECA_V2 en knowledge/ |
| `tweets-publicados.md` | ✅ Historial | ❌ No existe directamente | DEBE CONSOLIDARSE |
| `borradores/` | ✅ 5 drafts | `drafts/` ✅ 7 archivos | PROBABLEMENTE DUPLICADOS |
| `calendario.md` | ✅ Existe | ❌ No existe | ÚNICO |
| hooks, formatos, guias | ✅ Existen | ❌ No existen | ÚNICOS |

**Borradores: comparación de nombres**

```
contenido/borradores/                         content/drafts/
dato-licencia-a-inicio-obra.md           ←→  dato-licencia-a-inicio-obra.md    [MISMO?]
hilo-acta-replanteo.md                   ←→  hilo-acta-replanteo.md            [MISMO?]
hilo-declaracion-obra-nueva-*.md         ←→  hilo-declaracion-obra-nueva-*.md  [MISMO?]
reflexion-ahorro-poder-adquisitivo.md    ←→  reflexion-ahorro-poder-adquisitivo [MISMO?]
reflexion-cuando-empieza-una-casa.md     ←→  reflexion-cuando-empieza-una-casa  [MISMO?]
                                              tweet-metros-no-construidos.md     [NUEVO]
                                              tweet-primer-pago-terreno.md       [NUEVO]
```

Verificar byte-a-byte antes de asumir que son idénticos.

### ⚠️ CONFLICTO DE INFORMACIÓN: Timing de publicación

**CLAUDE.md:** "Horario validado: 9:00h lun-jue. Sábado eliminado — es el peor día."

**analisis-contenido-historico.md (11/08/2026):**
- Domingo: 2,3 likes/tweet (mejor día)
- Sábado: 1,2 likes/tweet (2º mejor)
- Jueves: 0,8 likes/tweet (peor día)
- Franja óptima: 18:00 CET (3× la media)

El análisis histórico es más reciente y más específico. El calendario del CLAUDE.md está desactualizado respecto a los datos reales.

**Nota:** Según las respuestas del propietario (sección 15), no se fijará todavía una hora óptima. El sistema debe registrar métricas y aprender progresivamente.

---

## 4. CLAUDE CODE ACTUAL

### Permisos en `.claude/settings.local.json`

```json
{
  "permissions": {
    "allow": [
      "Bash(pip show *)",
      "Bash(yt-dlp --version)",
      "Bash(claude mcp *)",
      "mcp__buffer__get_account",
      "mcp__buffer__create_post",
      "mcp__buffer__edit_post",
      "WebFetch(domain:inversoracon30.substack.com)",
      "mcp__buffer__get_post",
      "Skill(claude-api)",
      "Skill(claude-api:*)"
    ]
  }
}
```

**Análisis:**
- ✅ Buffer MCP: lectura y escritura (get_account, create_post, edit_post, get_post)
- ✅ WebFetch: inversoracon30.substack.com (Joan Tubau)
- ✅ yt-dlp disponible
- ❌ Sin permisos para WordPress REST API
- ❌ Sin permisos para Telegram
- ❌ Sin permisos para X MCP (mencionado como "pendiente" en CLAUDE.md)

### Comandos Disponibles

| Comando | Función | Líneas |
|---------|---------|--------|
| `/diary` | Registrar algo que ocurrió — entrada de eventos diarios | 571 |
| `/today` | Elegir qué publicar hoy — selecciona contenido del día | 914 |
| `/week` | Crear calendario semanal | 1.372 |
| `/auto-week` | Generar la semana completa — automatizado | 2.477 |
| `/ideas` | Generar ideas | 747 |
| `/published` | Registrar publicación | 242 |
| `/review` | Revisar algo sensible | 650 |

Los 7 comandos existen en AMBAS ubicaciones (`.claude/commands/` y `autopromotorn_claude_content_os/.claude/commands/`). Son idénticos.

### Integraciones Faltantes

| Integración | Estado | Prioridad (ver sección 15) |
|-------------|--------|----------------------------|
| WordPress REST API | NO EXISTE | ALTA — prioridad inmediata |
| Telegram Bot | NO EXISTE | ALTA — interfaz móvil principal |
| X/Twitter MCP | PENDIENTE | ALTA — necesario para Radar Agent y Reply Agent |
| RSS/Substack reader | NO EXISTE | ALTA — Content Harvester |
| Instagram via Buffer | CONFIGURADO (sin evidencia de uso) | ALTA |

---

## 5. BUFFER

### Situación Actual: MCP conectado pero SUBUTILIZADO

**Configuración:** MCP disponible via HTTP. Permisos: crear, editar, leer posts, obtener métricas.

**Canales conectados:** X (@autopromotorn) confirmado. Instagram conectado (plan de cuenta Buffer confirma plan de pago).

**Uso documentado en el repositorio:** NINGUNO. Los tweets se publican directamente en X sin pasar por Buffer.

### Flujo Actual vs. Objetivo

| Aspecto | Ahora | Objetivo |
|---------|-------|---------|
| Redacción | Markdown en content/drafts/ | Igual |
| Revisión | Manual | Manual (conservar — no publicar sin aprobación) |
| Publicación | Directa en X sin registro | Buffer como cola → aprobación → publicación |
| Historial | tweets-publicados.md incompleto | Buffer → métricas automáticas en metrics/ |
| Métricas | Manual/Grok (no reproducible) | Buffer MCP → CSV semanal |

### Métricas a Capturar (según decisión del propietario)

Mínimo inicial:
- Impresiones / reach
- Likes
- Replies / comments
- Reposts / shares
- Clicks (si disponibles)
- Engagement rate
- Crecimiento asociado al contenido

Futuro:
- Conversiones a seguidores por tipo de contenido
- Conversiones a suscriptores de email

---

## 6. WORDPRESS

### Estado: NO INTEGRADO (0%)

**Blog:** autopromotornudista.com

**Objetivo declarado:** Convertirlo en el "Diario del Autopromotor" — artículos cronológicos del proceso de construcción, contenido SEO, captación de emails para lista propia.

**Evidencia en el repositorio:** NINGUNA.
- No hay configuración de API REST
- No hay scripts de integración
- No hay credenciales referenciadas (correcto)

**Nota importante:** Contrariamente a lo que sugería el borrador inicial de la auditoría, WordPress es una prioridad estratégica inmediata. Ver sección 15 (Respuestas).

**Arquitectura prevista:**
- WordPress como repositorio público del Diario
- API REST para sincronización desde el repositorio
- MailPoet (o equivalente) para captación de emails
- Los artículos del Journal Agent alimentarán WordPress en primera instancia, y de ahí se derivará contenido para X, Instagram y newsletter

---

## 7. SCRIPTS EXISTENTES

### Inventario

| Script | Propósito | Inputs | Outputs | Dependencias | Estado | Reutilizable |
|--------|-----------|--------|---------|--------------|--------|--------------|
| **scripts/analizar_video.py** | Descarga transcripción de YouTube y guarda como Markdown con metadatos | URL YouTube + título opcional | `docs/fuentes/[fecha]-[slug].md` | youtube-transcript-api | FUNCIONAL | ALTA |

### Funcionalidad Detallada

```
Entrada: python3 scripts/analizar_video.py "https://youtu.be/XXXX" "Título"
Salida:  docs/fuentes/2026-08-17-podcast-precio-vivienda.md

Capacidades:
- Extrae video ID de múltiples formatos (youtube.com, youtu.be, embed, shorts)
- Intenta múltiples idiomas (ES prioritario, traducción como fallback)
- Formatea transcripción en chunks de ~400 palabras
- Genera metadata (URL, ID, fecha, idioma)
- Sugiere siguiente paso para Claude
```

### Scripts Faltantes (por orden de prioridad)

| Script | Función | Prioridad |
|--------|---------|-----------|
| `harvest.py` | Extensión de analizar_video.py para URL genérica: YouTube, Substack, artículo, tweet, podcast | ALTA |
| `exportar_metricas_buffer.py` | Buffer API → CSV en metrics/ semanal | ALTA |
| `sincronizar_wordpress.py` | Markdown aprobado → WordPress REST API | ALTA |
| `descargar_newsletter.py` | Substack RSS → sources/newsletters/ | MEDIA |
| `backup.sh` | Git add + commit + push automático | MEDIA |

---

## 8. DATOS Y FORMATOS

### Cómo se Almacena Cada Tipo de Información

| Tipo de Dato | Ubicación | Formato | Problema |
|--------------|-----------|---------|----------|
| **Ideas** | `content/ideas/ideas-sesion-27ago2026.md` | Markdown | Una sesión, sin histórico acumulado |
| **Borradores** | `content/drafts/` | Markdown | 7 archivos, sin metadata de estado explícita |
| **Publicados** | `content/published/historico-hasta-ago2026.md` | Markdown tabla | Incompleto (~8 tweets, debería haber ~100+) |
| **Métricas** | `tweets-publicados.md` | Markdown tabla | Manual, incompleto, duplicado |
| **Investigación** | `docs/fuentes/*.md` | Markdown | Solo 1 transcripción |
| **Calendario** | `contenido/calendario.md` | Markdown | Existe pero no vinculado al sistema nuevo |
| **Conocimiento** | `knowledge/*.md` | Markdown estructurado | Excelente |
| **Obra** | `docs/diario-obra.md` | Markdown | Actualizado, con tabla de hitos y costes |
| **Finanzas** | `docs/finanzas/Estimacion Gastos Casa.xlsx` | Excel | Desglose detallado, no indexado |
| **Documentos** | `docs/hipoteca/*.pdf`, `docs/presupuestos/*.pdf` | PDF | No indexados ni procesados |
| **Métricas Buffer** | NO EXISTE | — | Vacío crítico |
| **Métricas X** | `analisis-contenido-historico.md` | Markdown tablas | Manual, snapshot puntual |

### Formatos Detectados

- ✅ Markdown (primario — correcto)
- ✅ Excel (finanzas — referencia)
- ✅ PDF (documentos legales — referencia)
- ✅ HTML (dossiers interactivos — referencia)
- ❌ JSON (no usado)
- ❌ CSV (no usado — debería usarse para métricas)
- ❌ SQLite/PostgreSQL (no usado)

---

## 9. GIT

### Estado: REPOSITORIO GIT NO INICIALIZADO

```
$ git status
fatal: no es un repositorio git
```

El directorio `/home/pineapple/proyectos/autopromotorn` **no tiene control de versiones**.

**Implicaciones:**
- Sin historial de cambios
- Sin ramas
- Sin remotes
- Sin backup en la nube
- Imposible revertir cambios

**Evidencia de intención de usar Git:** Archivos `.gitkeep` en carpetas vacías.

**Decisión del propietario (ver sección 15):** GitHub PRIVADO. El repositorio contiene y contendrá información financiera, hipotecaria, presupuestos, documentos de vivienda y datos personales. Inicializar cuando se indique explícitamente, no antes.

---

## 10. QUÉ YA TENEMOS CONSTRUIDO

| COMPONENTE | ESTADO | ARCHIVOS EXISTENTES | REUTILIZABLE | TRABAJO PENDIENTE |
|---|---|---|---|---|
| **Knowledge Base** | AVANZADO | BIBLIOTECA_V2 (2.491 líneas, 138 ideas) | 100% | Ampliar; indexar por tema |
| **Voice & Style** | FUNCIONAL | CLAUDE.md, guia-redaccion.md, analisis-historico.md | 100% | Documentar más ejemplos |
| **Content Strategy** | FUNCIONAL | Pilares, calendario, formatos-y-ejemplos | 100% | Revisión periódica con datos reales |
| **Idea Bank** | PARCIAL | ideas-sesion-27ago2026.md (3 ideas) | 60% | Crear índice acumulado |
| **Content Writer** | FUNCIONAL | 4 formatos narrativos + 20 hooks | 90% | Automatizar generador de combinaciones |
| **Editorial Calendar** | FUNCIONAL | SEPTIEMBRE_2026.md (6 hilos listos) | 100% | Extender trimestralmente |
| **Buffer Integration** | FUNCIONAL (no usado) | MCP configurado, settings.local.json | 80% | Activar como cola editorial oficial |
| **X Content** | FUNCIONAL | Ejemplos en formatos-y-ejemplos.md | 90% | Usar comandos existentes más activamente |
| **Instagram Content** | NO EXISTE | Mencionado sin evidencia | 0% | Diseñar desde el inicio junto con X |
| **Journal/Diario** | FUNCIONAL | diario-obra.md (actualizado) | 100% | Evolucionar a captura continua de eventos |
| **Timeline Personal** | PARCIAL | Cronología en diario-obra.md | 80% | Conectar con tweets publicados |
| **Content Harvester** | PARCIAL | analizar_video.py (YouTube solo) | 70% | Extender a URL genérica (newsletter, artículo, tweet, podcast, web) |
| **Newsletter Ingestion** | NO EXISTE | Referencia a Joan Tubau, sin captura | 0% | Implementar |
| **YouTube Harvester** | FUNCIONAL | analizar_video.py | 100% | Integrar en harvest.py |
| **Podcast Ingestion** | FUNCIONAL (via YT) | analizar_video.py | 100% | Ampliar a audio directo |
| **Radar Agent** | NO EXISTE | Estrategia documentada, sin automatización | 20% | Primeras piezas a construir |
| **Reply Agent** | NO EXISTE | Estrategia documentada (regla 70/30 en CLAUDE.md) | 20% | Primeras piezas a construir — propone respuestas, no publica |
| **Writer Agent** | PARCIAL | Comandos /today, /week, /auto-week | 60% | Formalizar como agente independiente |
| **Journal Agent** | NO EXISTE | Concepto definido en este documento | 0% | Diseñar e implementar |
| **Critic Agent** | FUNCIONAL | `/review` command existe | 80% | Entrenar crítica editorial basada en marcos |
| **Analytics Agent** | PARCIAL | analisis-contenido-historico.md manual | 60% | Capturar métricas Buffer automáticamente |
| **Metrics Storage** | PARCIAL | tweets-publicados.md manual | 40% | Crear histórico en CSV |
| **WordPress Integration** | NO EXISTE | Prioridad estratégica inmediata | 0% | Diseñar pipeline Journal → WordPress |
| **Newsletter / Email List** | NO EXISTE | Objetivo declarado | 0% | MailPoet o equivalente en WordPress |
| **Telegram Interface** | NO EXISTE | Interfaz móvil principal prevista | 0% | Implementar como puerta de aprobación |
| **Scripts** | MÍNIMO | 1 script (analizar_video.py) | 50% | Crear harvest.py + exportar_metricas.py + sincronizar_wordpress.py |
| **Backup** | NO EXISTE | Sin Git remoto | 0% | GitHub privado — cuando se indique |

**Puntuación global: 6.3/10**

El sistema está fundamentalmente sólido pero infrautilizado. La arquitectura es excelente, la estrategia es sólida, la ejecución sigue siendo manual en casi todos los puntos.

---

## 11. PROPUESTA DE ARQUITECTURA

### Estructura Objetivo

```
autopromotorn/
│
├── .claude/                             ← Config Claude Code (canónica aquí)
│   ├── settings.json
│   └── commands/                        ← 7+ comandos
│
├── knowledge/                           ← Consolidar DESDE autopromotorn_claude_content_os/knowledge/
│   ├── BIBLIOTECA_EDITORIAL.md          ← Consolidar V1 + V2
│   ├── PILARES_Y_FORMATOS.md           ← Consolidar formatos + hooks + guia-redaccion
│   ├── analisis-historico.md           ← Mover desde docs/
│   └── INDEX.md                         ← Punto de entrada
│
├── content/                             ← CANÓNICO (ya existe)
│   ├── ideas/                           ← Por mes: ideas-2026-09.md, ideas-2026-10.md
│   │   └── IDEAS_INDEX.md
│   ├── drafts/
│   ├── ready/
│   ├── scheduled/
│   └── published/
│       └── TWEETS_HISTORIC_COMPLETE.md ← Única fuente de verdad del historial
│
├── journal/                             ← Diario del Autopromotor (nuevo)
│   ├── obra/
│   │   ├── diario-obra.md              ← Mover desde docs/
│   │   ├── hitos.md
│   │   ├── fotos/
│   │   └── CAPTURE_PROTOCOL.md
│   ├── patrimonio/
│   │   ├── patrimonio-2026.md
│   │   └── inversiones.md
│   └── timeline.md
│
├── sources/                             ← Investigación y fuentes
│   ├── newsletters/
│   ├── youtube/                         ← Mover desde docs/fuentes/
│   ├── podcasts/
│   ├── web/
│   └── x/
│
├── inbox/                               ← Ya existe, mantener
│   ├── articles/
│   ├── notes/
│   ├── photos/
│   └── videos/
│
├── metrics/                             ← Ya existe (vacío), poblar
│   ├── buffer/
│   ├── x/
│   └── analysis/
│
├── agents/                              ← Nuevo — agentes automatizados
│   ├── radar_agent.md                  ← Definición y prompt del Radar Agent
│   ├── reply_agent.md
│   ├── writer_agent.md
│   ├── journal_agent.md
│   ├── harvester_agent.md
│   ├── critic_agent.md
│   └── analytics_agent.md
│
├── docs/                                ← SOLO referencia legal/técnica
│   ├── proyecto_arquitectonico/
│   ├── hipoteca/
│   ├── presupuestos/
│   └── finanzas/
│
├── scripts/                             ← Ampliar
│   ├── analizar_video.py               ← Existente
│   ├── harvest.py                      ← Nuevo
│   ├── exportar_metricas.py            ← Nuevo
│   ├── sincronizar_wordpress.py        ← Nuevo
│   └── backup.sh                        ← Nuevo
│
├── contenido/                           ← LEGACY (conservar intacto)
│   └── LEGACY_README.md
│
├── autopromotorn_claude_content_os/    ← LEGACY (conservar hasta verificar contenido único)
│   └── LEGACY_README.md
│
├── .gitignore
├── CLAUDE.md                            ← Canónico en root
├── README.md
└── AUTOPROMOTORN_SYSTEM_AUDIT.md       ← Este documento
```

### Stack Tecnológico del Sistema Completo

| Componente | Herramienta | Función |
|------------|-------------|---------|
| **Desarrollo y mantenimiento** | Claude Code | Entorno de desarrollo, escritura de agentes, gestión del repositorio |
| **Runtime 24/7** | OpenClaw | Orquestador de agentes en servidor continuo |
| **Cola editorial** | Buffer | Programación de publicaciones en X e Instagram |
| **Repositorio editorial público** | WordPress (autopromotornudista.com) | Diario del Autopromotor + SEO + captación de emails |
| **Interfaz móvil** | Telegram Bot | Alertas, aprobación rápida, envío de notas/fotos/audios |
| **Control de versiones** | Git + GitHub privado | Historial, backup, colaboración |
| **Fuente de verdad** | Archivos del repositorio | Toda la memoria del sistema en archivos Markdown/CSV |

**Principio fundamental:** La memoria del sistema NO depende de Claude, ChatGPT, Grok ni OpenClaw. La fuente de verdad vive en los archivos del repositorio.

---

## 12. PLAN DE MIGRACIÓN PROPUESTO

> **NOTA IMPORTANTE:** El propietario ha indicado que la migración puede completarse en pocas sesiones de Claude Code, no en semanas. Las fases son conceptuales, no necesariamente secuenciales en el tiempo.

### FASE 0 — BACKUP Y SEGURIDAD

**Objetivo:** Proteger el trabajo existente antes de cualquier cambio.

**Acciones:**
1. Inicializar Git: `git init && git add . && git commit -m "Pre-migration audit checkpoint"`
2. Crear GitHub repo privado
3. Push inicial
4. Crear `.gitignore` (excluir PDFs, xlsx, .env, secrets)

**Riesgos:** Ninguno.
**Validación:** GitHub repo visible con todos los archivos.

---

### FASE 1 — CONSOLIDACIÓN DE CONOCIMIENTO

**Objetivo:** Mover `knowledge/` de `autopromotorn_claude_content_os/` a root y deduplicar.

**Archivos tocados:**
- Mover: `autopromotorn_claude_content_os/knowledge/` → `knowledge/` (root)
- Verificar: ¿V1 de biblioteca tiene información que no está en V2?
- Crear: `knowledge/INDEX.md`
- Crear: `knowledge/PILARES_Y_FORMATOS.md` (consolidar formatos + hooks + guia-redaccion)
- Marcar: `contenido/biblioteca-8-pilares-32-tweets.md` como DEPRECATED_V1

**Riesgos:** Bajo.
**Validación:** Toda la información de V1 aparece en V2 o en el nuevo documento consolidado.

---

### FASE 2 — NORMALIZACIÓN DE CONTENIDO

**Objetivo:** Única fuente de verdad para tweets publicados y borradores.

**Archivos tocados:**
- Crear: `content/published/TWEETS_HISTORIC_COMPLETE.md`
- Verificar byte-a-byte: duplicidades entre `contenido/borradores/` y `content/drafts/`
- Crear: `content/ideas/IDEAS_INDEX.md`
- Crear: `contenido/LEGACY_README.md` (sin borrar nada)
- Documentar: workflow explícito `ideas/ → drafts/ → ready/ → scheduled/ → published/`

**Riesgos:** Bajo — sin eliminación, solo consolidación.
**Validación:** Único historial de tweets. Sin información perdida.

---

### FASE 3 — JOURNAL DEL AUTOPROMOTOR

**Objetivo:** Crear el sistema de captura continua de eventos de la obra.

**Archivos tocados:**
- Crear: `journal/` con estructura obra/, patrimonio/
- Mover (o vincular): `docs/diario-obra.md` → `journal/obra/diario-obra.md`
- Crear: `journal/obra/hitos.md`
- Crear: `journal/patrimonio/patrimonio-2026.md`
- Crear: `journal/timeline.md`
- Crear: `journal/obra/CAPTURE_PROTOCOL.md`
- Definir: protocolo de recepción de notas, audios, fotos, presupuestos, facturas via Telegram

**Riesgos:** Muy bajo.
**Validación:** Diario-obra.md accesible. Protocolo de captura documentado.

---

### FASE 4 — CONTENT HARVESTER

**Objetivo:** Capturar automáticamente contenido desde cualquier URL.

**Archivos tocados:**
- Crear: `scripts/harvest.py` (extensión de analizar_video.py para URL genérica)
- Crear: `sources/` con estructura newsletters/, youtube/, podcasts/, web/, x/
- Mover: `docs/fuentes/` → `sources/youtube/`
- Crear: `sources/README.md` con protocolo de procesamiento
- Implementar: integración con comentarios del propietario ("me interesa este argumento", "busca algo polémico")

**Riesgos:** Medio-bajo.
**Validación:** Al menos 10 fuentes capturadas. Harvest.py sin errores.

---

### FASE 5 — AGENTES (prioridad ordenada)

**Agentes a construir, por orden de valor:**

1. **Reply Agent** — monitoriza tweets del nicho, propone respuestas. Nunca publica sin aprobación.
2. **Content Harvester Agent** — recibe URL + comentario, extrae, cruza con Knowledge Base, puntúa, guarda en Idea Bank.
3. **Journal Agent** — recibe eventos (nota, foto, audio, presupuesto), estructura en timeline, propone artículos para WordPress cuando hay masa crítica.
4. **Writer Agent** — genera borradores para X, Instagram, artículo o newsletter a partir del Idea Bank.
5. **Critic Agent** — revisa borradores contra marcos, deduplicación, tono, calidad.
6. **Analytics Agent** — exporta métricas de Buffer, construye histórico, detecta tendencias.
7. **Radar Agent** — monitoriza cuentas objetivo y conversaciones del nicho en tiempo real.

**Definición de cada agente:** Crear `agents/[nombre]_agent.md` con definición, inputs, outputs, restricciones y prompt base.

**Principio común a todos:** Proponen, no publican. El propietario aprueba siempre.

---

### FASE 6 — INTEGRACIONES EXTERNAS

**Objetivo:** Conectar el sistema con el ecosistema completo.

**Sub-fases:**
1. **WordPress:** `scripts/sincronizar_wordpress.py` + definir pipeline Journal → artículo → WordPress
2. **Telegram:** Bot para recibir notas/fotos/audios del propietario + notificaciones de aprobación
3. **Buffer activo:** Toda publicación pasa por Buffer. Historial de posts en `metrics/buffer/`
4. **X MCP:** Cuando esté disponible, conectar Radar Agent y Reply Agent
5. **Métricas automatizadas:** `scripts/exportar_metricas.py` semanal → `metrics/`

---

### FASE 7 — OPENCLAW COMO RUNTIME

**Objetivo:** Migrar la orquestación de Claude Code (desarrollo) a OpenClaw (24/7).

**Acciones:**
1. Exportar definiciones de agentes a formato OpenClaw
2. Configurar servidor con OpenClaw
3. Conectar: OpenClaw ↔ GitHub repo (fuente de verdad) ↔ Buffer ↔ Telegram ↔ WordPress
4. Configurar pipeline de aprobación via Telegram
5. Mantener Claude Code para desarrollo y mantenimiento del sistema

---

### Tabla de Riesgos por Fase

| Fase | Riesgo | Mitigación | Reversibilidad |
|------|--------|-----------|--------------------|
| 0 | — | — | 100% |
| 1 | Perder información histórica | Verificar byte-a-byte antes de archivar | 100% |
| 2 | Conflictos de contenido | Comparar antes de consolidar | 100% |
| 3 | Schema de journal incorrecto | Fácil de cambiar | 95% |
| 4 | Scripts rompen con cambios de API | Mantener ejemplos y tests | 90% |
| 5 | Agentes proponen contenido de baja calidad | Revisión humana siempre — no publicar sin aprobación | 100% |
| 6 | Incompatibilidad entre herramientas | Probar cada integración por separado | 80% |
| 7 | OpenClaw no es estable | Mantener Claude Code como fallback siempre | 70% |

---

## 13. PREGUNTAS DE LA AUDITORÍA (ya respondidas)

Ver sección 14 para las respuestas completas del propietario.

---

## 14. RESPUESTAS DEL PROPIETARIO A LA AUDITORÍA

*Registradas el 29 de agosto de 2026 como parte de este documento.*

**Sobre `autopromotorn_claude_content_os/`:**
Es una versión anterior/espejo del sistema. El objetivo futuro es que la raíz `/autopromotorn/` sea la única canónica. Conservar todo lo que tenga información única y después dejar el subdirectorio como legacy o eliminarlo solo cuando se haya comprobado que no contiene nada exclusivo.

**Sobre la carpeta canónica:**
`/home/pineapple/proyectos/autopromotorn/` (root).

**Sobre el historial de tweets:**
No asumir que el historial actual está completo. Hay publicaciones no registradas. Reconstruir el histórico antes de usarlo como fuente de verdad.

**Sobre Buffer:**
Buffer pasa a ser la cola editorial oficial. El propietario paga una cuenta. La intención es utilizarlo activamente para X e Instagram.

**Sobre el diario de obra:**
Debe evolucionar hacia un sistema de captura continua de eventos, no únicamente una actualización semanal. El propietario aportará fotos, notas, audios, cifras, documentos y acontecimientos a medida que ocurran. Un agente decidirá qué merece convertirse en artículo.

**Sobre privacidad del repositorio:**
PRIVADO. Contiene y contendrá información financiera, hipotecaria, presupuestos, documentos de vivienda y datos personales.

**Sobre el timing de publicación:**
No fijar todavía una hora óptima basada solo en datos históricos actuales. El sistema debe registrar métricas y aprender progresivamente. Buffer debe permitir experimentar con horarios.

**Sobre los pilares editoriales:**
Los pilares actuales se mantienen por ahora, pero no son inmutables. Los futuros Analytics y Strategy Agents podrán recomendar modificaciones basadas en datos.

**Sobre WordPress:**
Prioridad estratégica inmediata. El blog autopromotornudista.com se convierte en el "Diario del Autopromotor": artículos cronológicos, contenido SEO, captación de emails.

**Sobre automatización:**
Alta automatización pero SIEMPRE con revisión humana antes de publicar en X, Instagram, WordPress o newsletter. Los agentes investigan, redactan, preparan borradores y programan propuestas, pero no publican directamente sin aprobación.

**Sobre GitHub:**
PRIVADO.

**Sobre métricas de Buffer:**
Registrar mínimamente: impresiones/reach, likes, replies/comments, reposts/shares, clicks, engagement rate, crecimiento asociado. Futuro: conversiones a seguidores y email.

**Sobre objetivo de seguidores:**
No fijar un número arbitrario. El objetivo principal es maximizar crecimiento sostenible y construir audiencia propia por email.

**Sobre replies estratégicos:**
Son una prioridad. Quiere un agente que monitorice tweets relevantes y proponga respuestas en tiempo casi real. Nunca respuestas automáticas sin aprobación.

**Sobre el análisis histórico con Grok:**
No considerarlo infraestructura reproducible. Construir un sistema nuevo para almacenar métricas e histórico.

---

## 15. NUEVOS REQUISITOS INCORPORADOS A LA ARQUITECTURA

**Canales:**
- X (@autopromotorn) — principal
- Instagram — parte de la arquitectura desde el inicio

**Tiempo disponible:**
- 30 minutos diarios para revisión
- 2 horas el sábado + 2 horas el domingo

**Stack tecnológico confirmado:**
- OpenClaw como orquestador 24/7 en servidor dedicado
- Sin n8n por ahora (añadir solo si hay necesidad clara)
- Telegram como interfaz móvil principal para alertas y aprobación rápida
- Buffer como cola editorial de X e Instagram
- WordPress como repositorio público del Diario
- Lista de email propia para futura monetización

**Content Harvester Agent — especificación:**

Recibirá URL de: newsletter, artículo, YouTube, podcast, tweet/thread, web.

El propietario puede acompañar la URL con comentarios como:
- "me interesa este argumento"
- "busca algo polémico"
- "esto me recuerda a nuestra hipoteca"

El agente deberá:
1. Extraer el contenido/transcripción
2. Identificar las mejores ideas
3. Cruzarlas con AutopromotorN y la experiencia real del propietario
4. Evitar copiar contenido
5. Detectar ideas repetidas (cruzando con Idea Bank)
6. Puntuar las oportunidades
7. Guardar las mejores en el Idea Bank
8. Proponer adaptaciones para X, Instagram, artículo o newsletter

**Journal Agent — especificación:**

Recibirá: notas, audios, fotos, vídeos, presupuestos, facturas, decisiones, incidencias, hitos.

El agente deberá:
1. Registrar cada acontecimiento estructuradamente en la timeline
2. Nunca inventar datos que falten
3. Cuando haya masa crítica sobre una fase, proponer artículo para WordPress
4. Cada artículo aprobado alimentará: X, Instagram, newsletter, contenido evergreen

**Agentes objetivo del sistema completo:**
1. Radar Agent
2. Reply Agent
3. Writer Agent
4. Journal Agent
5. Content Harvester Agent
6. Critic Agent
7. Analytics Agent

**Principio arquitectónico fundamental:**
La memoria del sistema NO depende de Claude, ChatGPT, Grok ni OpenClaw. La fuente de verdad vive en los archivos del repositorio.

**Correcciones al borrador inicial de la auditoría:**
- WordPress NO es "no construir todavía" — es prioridad inmediata
- Instagram NO es "después de validar X" — la arquitectura se diseña desde el inicio para ambos canales
- Reply Agent NO tiene "demasiado riesgo" — el riesgo aplica a publicación automática; el Reply Agent solo propone

---

## RESUMEN EJECUTIVO

### ✅ Qué tenemos ya construido

1. Biblioteca editorial excepcional (138 ideas clasificadas, 27 marcos mentales de Joan Tubau)
2. Calendario editorial definido y validado (5 pilares × 4 formatos × timing por datos reales)
3. Guías de redacción exhaustivas (4 formatos narrativos completamente documentados)
4. Proyecto real como fuente inagotable (obra en curso, datos reales de finanzas e hipoteca)
5. Sistema de 7 comandos de Claude Code operativos
6. MCP Buffer configurado y con permisos correctos
7. Script de harvesting para YouTube funcional
8. Contenido de septiembre ready (6 hilos + 4 tweets de familia)

### 🔒 Qué merece conservarse sin tocar

- `knowledge/BIBLIOTECA_INTELECTUAL_AUTOPROMOTORN_V2.md` — el activo más valioso
- Los 7 comandos de `.claude/commands/`
- `docs/guia-redaccion.md`
- `docs/analisis-contenido-historico.md`
- `docs/diario-obra.md`

### ❗ Qué está duplicado

1. `autopromotorn_claude_content_os/` es espejo de root
2. `contenido/borradores/` ≈ `content/drafts/` (5 archivos aparentemente iguales)
3. `tweets-publicados.md` existe en dos lugares con datos divergentes
4. `CLAUDE.md` idéntico en raíz y subdirectorio

### 💀 Qué está obsoleto

1. `contenido/biblioteca-8-pilares-32-tweets.md` (V1, superada por V2)
2. Timing 9:00h en CLAUDE.md (datos reales señalan 18:00h como óptimo)

### ❌ Qué falta críticamente

1. Git + GitHub privado (sin backup)
2. Buffer activado como cola editorial real
3. WordPress integrado (prioridad inmediata)
4. Historial completo de tweets (reconstruir)
5. Content Harvester Agent para URL genérica
6. Journal Agent para captura continua de eventos
7. Telegram Bot como interfaz de aprobación móvil
8. Métricas automatizadas de Buffer

### 🏗️ Arquitectura más simple posible

```
root/ →
  .claude/ + knowledge/ + content/ + journal/ +
  sources/ + agents/ + scripts/ + docs/ + metrics/ + inbox/
```

9 carpetas. Una sola fuente de verdad por tipo de dato. Markdown legible por humanos.

### 🚫 Qué NO construir todavía

1. n8n (añadir solo si OpenClaw no cubre una necesidad concreta)
2. Sistema de métricas complejo (empezar con CSV simple de Buffer)
3. Publicación automática sin aprobación (nunca, por principio)
4. Funcionalidades de Instagram avanzadas (diseñar la arquitectura, implementar gradualmente)

### 🚀 Los 10 primeros pasos

| # | Paso | Impacto |
|---|------|---------|
| 1 | Inicializar Git + GitHub privado | CRÍTICO |
| 2 | Crear `.gitignore` | CRÍTICO |
| 3 | Mover `knowledge/` desde subdirectorio a root | ALTO |
| 4 | Crear `content/published/TWEETS_HISTORIC_COMPLETE.md` | ALTO |
| 5 | Activar Buffer como cola editorial (primer post de prueba) | ALTO |
| 6 | Crear `journal/` y mover `docs/diario-obra.md` | ALTO |
| 7 | Crear `scripts/harvest.py` (URL genérica) | ALTO |
| 8 | Diseñar y crear `agents/` con definiciones de los 7 agentes | MEDIO |
| 9 | Implementar `scripts/exportar_metricas_buffer.py` | MEDIO |
| 10 | Iniciar diseño de integración WordPress | MEDIO |

---

*Auditoría generada: 29 agosto 2026*
*Respuestas del propietario incorporadas: 29 agosto 2026*
*Archivos analizados: ~50 archivos, ~8.000 líneas de contenido*
*Puntuación global del sistema: 6.3/10 — fundamentos sólidos, automatización pendiente*
*Próxima revisión: cuando se complete la Fase 2 de migración*
