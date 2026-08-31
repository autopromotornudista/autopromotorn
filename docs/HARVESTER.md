---
status: approved
last_updated: 2026-08-31
source_type: human_approved
---

# HARVESTER — Sistema de cosecha editorial

Fuente de verdad del pipeline de ingesta de ideas externas para @AutopromotorN.

Los demás archivos del sistema (`content/ideas/README.md`, `sources/SUBSCRIPTIONS.md`, `agents/HARVESTER.md`) enlazan a este documento para las reglas generales. No duplicar aquí lo que ya está en esos archivos.

---

## 1. Qué es el sistema HARVESTER

El HARVESTER es la primera capa del pipeline editorial. Su función es:

1. Recibir materia prima externa (newsletters, artículos, vídeos, experiencias propias)
2. Filtrar usando el Source Value Gate
3. Detectar duplicados antes de crear cualquier archivo
4. Extraer ideas con provenance completa
5. Depositarlas en la bandeja correcta, listas para validación humana

El HARVESTER **no escribe posts**. No genera borradores. No programa nada. Su output es siempre una idea en estado `PENDIENTE_DE_VALIDACION`.

---

## 2. Diferencia entre fuente / insight / idea / contenido

| Concepto | Definición | Dónde vive |
|----------|-----------|-----------|
| **Fuente** | El texto, vídeo o podcast original externo | `sources/` |
| **Insight** | Fragmento de valor extraído de la fuente (FACT, INSIGHT, FRAMEWORK, STORY, DERIVED_CLAIM) | Dentro del archivo de idea |
| **Idea** | Combinación de insight + transformación propia + conexión con experiencia real | `content/ideas/inbox/` o `content/ideas/` |
| **Contenido** | Post publicable escrito por WRITER usando `knowledge/` + `editorial/` | `content/drafts/` → `ready/` → `scheduled/` → publicado |

Una fuente puede generar múltiples insights. Un insight puede generar una idea. Una idea genera un borrador. El salto de fuente a contenido siempre pasa por la idea — nunca directamente.

---

## 3. Dos agentes de ingesta: diferencias

| Característica | `/harvest` | `/harvest-newsletter` |
|---------------|-----------|----------------------|
| Entrada | URL (YouTube, Substack, web, X) | Texto pegado por el usuario |
| Lanza scripts | Sí (`analizar_video.py`, `analizar_articulo.py`) | No |
| Accede a URLs externas | Sí (con WebFetch autorizado) | No |
| Destino de ideas | `content/ideas/` raíz | `content/ideas/inbox/` |
| Nomenclatura | `IDEA-VID-NNN`, `IDEA-HAR-NNN` | `IDEA-NL-YYYYMMDD-NNN` |
| Actualiza SUBSCRIPTIONS.md | Sí (si fuente registrada) | No |
| Máx. ideas por ejecución | 5 | 3 |

Usar `/harvest-newsletter` cuando el texto de la newsletter ya está disponible para pegar directamente. Usar `/harvest` para procesar una URL desde cero.

---

## 4. Source Value Gate

Toda fuente externa pasa por el gate antes de extraer ideas. Ver criterios completos en el skill `/harvest-newsletter` (sección PASO 1).

**Principio:** el gate protege contra ruido, no contra complejidad. Una fuente difícil de conectar con el nicho puede superarlo si contiene un modelo mental genuinamente útil. Una fuente aparentemente relevante puede no superarlo si solo permite repetir al autor sin transformación.

**Si DESCARTAR:** no se crea ningún archivo. El output muestra el motivo en una frase.

---

## 5. Dónde viven las ideas

```
content/ideas/
├── inbox/          ← /harvest-newsletter → PENDIENTE_DE_VALIDACION
│   └── IDEA-NL-YYYYMMDD-[slug].md
├── IDEA-HAR-NNN.md ← /harvest (newsletters/artículos) → pending
├── IDEA-VID-NNN.md ← /harvest (YouTube) → pending
└── README.md       ← arquitectura de la carpeta
```

Las ideas en `inbox/` no pasan al WRITER sin validación humana explícita.
Las ideas en la raíz de `content/ideas/` tienen status `pending` y pueden ser desarrolladas por WRITER.

---

## 6. Estados de una idea

| Estado | Significado | Transición |
|--------|------------|-----------|
| `PENDIENTE_DE_VALIDACION` | Capturada, sin revisión | → usuario valida → `pending` |
| `PENDIENTE_DE_CONTEXTO` | Falta dato real necesario | → usuario aporta dato → `pending` |
| `pending` | Validada, lista para WRITER | → `/write IDEA-NL-[...]` → `in_progress` |
| `in_progress` | WRITER la está desarrollando | → borrador en `content/drafts/` |
| `published` | Post publicado | → registrar en `content/published/` |
| `discarded` | Descartada | → conservar archivo, actualizar status |

---

## 7. Quién puede aprobar ideas

Solo el usuario (Javi) puede mover una idea de `PENDIENTE_DE_VALIDACION` a `pending`.

La aprobación es explícita: "aprueba esta idea", "pasa esta al WRITER", o equivalente directo.

El HARVESTER no puede auto-aprobarse ni llamar al WRITER automáticamente.

---

## 8. Cómo pasan las ideas al WRITER

1. Usuario revisa las ideas en `content/ideas/inbox/`
2. Aprueba explícitamente una o varias
3. El archivo se mueve (o se actualiza el status) de `inbox/` a `content/ideas/` raíz con status `pending`
4. Usuario ejecuta `/write IDEA-NL-[YYYYMMDD]-[slug]`
5. WRITER lee la idea, `knowledge/` y `editorial/`, genera borrador en `content/drafts/`

---

## 9. Detección de duplicados

El HARVESTER verifica en este orden antes de crear cualquier idea:

1. `content/ideas/inbox/` — ideas recientes no validadas
2. `content/ideas/` raíz — ideas activas con status pending
3. `content/planning/SEPTIEMBRE_2026_CANDIDATOS.md` — contenido READY/SCHEDULED = ya utilizado
4. `content/drafts/` — borradores en curso
5. `contenido/tweets-publicados.md` — historial publicado LEGACY

**Criterio de duplicado:** mismo ángulo + mismo marco + misma conclusión. No basta con que el tema sea parecido — el ángulo debe ser idéntico o demasiado cercano para añadir valor.

Una nueva fuente puede **enriquecer** una idea existente sin crear una nueva. En ese caso, el HARVESTER documenta la relación en el output y sugiere actualizar la idea existente.

---

## 10. Separación de responsabilidades

```
HARVESTER (/harvest, /harvest-newsletter)
  → Ingesta, filtrado, extracción, depósito en content/ideas/
  → NUNCA escribe en knowledge/, editorial/, content/drafts/, Buffer

WRITER (/write)
  → Transforma idea aprobada en borrador
  → Solo usa knowledge/ y editorial/ como fuentes de verdad
  → NUNCA lee sources/ como si fueran hechos propios

CRITIC (/review)
  → Evalúa borradores antes de aprobar para content/ready/
  → No genera contenido, no captura ideas
```

---

## 11. Regla de información privada

`docs/PRIVATE_DOCS.md` define qué información del proyecto no puede aparecer en contenido público.

El HARVESTER no puede extraer ideas que exijan publicar información privada no editorial. Si una fuente conecta bien con el proyecto pero el ángulo requiere datos privados aún no aprobados para knowledge/, el estado de la idea es `PENDIENTE_DE_CONTEXTO` — no `PENDIENTE_DE_VALIDACION`.

---

## 12. Limitaciones actuales (agosto 2026)

- `/harvest-newsletter` no tiene acceso a URLs externas — el usuario debe pegar el texto manualmente
- No hay integración con Gmail, RSS ni n8n — el proceso es manual
- No hay deduplicación automática semántica — la búsqueda es por lectura directa de archivos
- Buffer MCP no es accesible desde HARVESTER — solo desde el usuario directamente

---

## 13. Integración futura (pendiente de implementar)

| Integración | Estado | Requisito |
|-------------|--------|-----------|
| Gmail → inbox automático | Pendiente | n8n o Gmail API |
| RSS → harvest automático | Pendiente | n8n + webhook |
| OpenClaw | Pendiente | Acceso API |
| Deduplicación semántica | Pendiente | Embeddings o índice local |
| Métricas de yield por fuente | Parcial | Manual en SUBSCRIPTIONS.md |

---

## 14. Archivos relacionados

| Archivo | Función |
|---------|---------|
| `~/.claude/skills/harvest-newsletter.md` | Skill global — procesa texto pegado de newsletters |
| `.claude/commands/harvest.md` | Comando del proyecto — procesa URLs |
| `agents/HARVESTER.md` | Contrato del agente HARVESTER |
| `agents/WRITER.md` | Contrato del agente WRITER |
| `sources/SUBSCRIPTIONS.md` | Registro de fuentes recurrentes autorizadas |
| `content/ideas/README.md` | Arquitectura de la carpeta de ideas |
| `editorial/INDEX.md` | Mapa de la capa metodológica |
| `knowledge/INDEX.md` | Mapa de la capa de conocimiento aprobado |
