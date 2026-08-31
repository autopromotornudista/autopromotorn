---
status: approved
last_updated: 2026-08-31
---

# content/ideas/ — Arquitectura de ideas

## Propósito

Este directorio es la bandeja de entrada editorial de @AutopromotorN. Contiene ideas en estado pre-borrador, extraídas de fuentes externas o generadas a partir de experiencias propias.

**No contiene posts.** No contiene borradores. Solo ideas con provenance completa, listas para evaluación humana antes de pasar al WRITER.

---

## Estructura

```
content/ideas/
├── README.md               ← este archivo
├── inbox/                  ← ideas recién capturadas, sin validar
│   └── IDEA-NL-*.md        ← ideas de newsletters (skill /harvest-newsletter)
├── IDEA-HAR-*.md           ← ideas de newsletters/artículos procesados por /harvest
├── IDEA-VID-*.md           ← ideas de vídeos procesados por /harvest
└── ideas-sesion-*.md       ← bancos de ideas generados en sesiones (LEGACY)
```

---

## Subcarpeta `inbox/`

Destino exclusivo del skill `/harvest-newsletter` — ideas capturadas desde texto pegado de newsletters.

**Nomenclatura:** `IDEA-NL-[YYYYMMDD]-[slug-descriptivo].md`

**Estado inicial de toda idea en inbox:** `PENDIENTE_DE_VALIDACION`

Las ideas en `inbox/` no pasan al WRITER hasta que el usuario las valide o las eleve a `content/ideas/` raíz.

---

## Estados de una idea

| Estado | Significado | Ubicación |
|--------|------------|-----------|
| `PENDIENTE_DE_VALIDACION` | Capturada, sin revisión humana | `inbox/` |
| `PENDIENTE_DE_CONTEXTO` | Falta dato real para poder desarrollarla | `inbox/` |
| `pending` | Validada, esperando desarrollo por WRITER | `content/ideas/` raíz |
| `in_progress` | WRITER la está desarrollando | `content/drafts/` |
| `published` | Post publicado en X | `content/published/` |
| `discarded` | Descartada (duplicado, sin potencial, obsoleta) | Conservar el archivo, actualizar status |

---

## Flujo de una idea

```
Fuente externa
    ↓
/harvest-newsletter (texto) o /harvest (URL)
    ↓
content/ideas/inbox/  ← estado: PENDIENTE_DE_VALIDACION
    ↓
Validación humana
    ↓
content/ideas/ raíz   ← estado: pending
    ↓
/write IDEA-NL-[...]
    ↓
content/drafts/
    ↓
/review
    ↓
content/ready/ → content/scheduled/ → publicado
```

---

## Diferencia entre agentes de ingesta

| Agente | Entrada | Salida |
|--------|---------|--------|
| `/harvest` | URL (YouTube, Substack, web, X) | `sources/` + `content/ideas/` raíz |
| `/harvest-newsletter` | Texto pegado | `content/ideas/inbox/` |

---

## Deduplicación obligatoria

Antes de crear cualquier idea, verificar en este orden:
1. `content/ideas/inbox/` — ideas recientes no validadas
2. `content/ideas/` raíz — ideas activas
3. `content/planning/SEPTIEMBRE_2026_CANDIDATOS.md` — contenido ya utilizado
4. `content/drafts/` — borradores activos
5. `contenido/tweets-publicados.md` — historial publicado (LEGACY)

Ver `docs/HARVESTER.md` para el protocolo completo.

---

## Quién puede escribir en este directorio

| Acción | Agente |
|--------|--------|
| Crear `inbox/IDEA-NL-*.md` | `/harvest-newsletter` (skill) |
| Crear `IDEA-HAR-*.md` / `IDEA-VID-*.md` | `/harvest` (comando) |
| Modificar status a `pending` | Usuario (aprobación humana) |
| Leer para desarrollar | WRITER (`/write`) |
| Marcar como `discarded` | Usuario o CRITIC |

**Nadie escribe directamente en `content/drafts/` desde una idea sin pasar por `/write`.**
