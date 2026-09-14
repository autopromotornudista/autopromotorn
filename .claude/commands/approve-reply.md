# /approve-reply

HUMAN GATE — Aprueba una propuesta de reply guardada en `content/replies/pending/`.

`$ARGUMENTS` = reply_id  (ej: `REPLY-20260908-001`)
Flag opcional: `--propuesta N`  (ej: `--propuesta 2`)

⚠️ ESTE COMANDO ES UN GATE HUMANO.
Solo puede ejecutarlo el propietario de la cuenta.
NUNCA envía el reply automáticamente. El envío es siempre manual.

---

## Paso 1 — Localizar el archivo

Buscar en `content/replies/pending/` el archivo cuyo frontmatter contenga `reply_id: [ARGUMENTS]`.

Si no se encuentra:
```
⛔ REPLY NO ENCONTRADO
reply_id: [ARGUMENTS]
No hay ningún archivo en content/replies/pending/ con ese ID.
Ejecuta /inbox para ver los replies disponibles.
```
Detenerse.

---

## Paso 2 — Mostrar el post original y las propuestas

Mostrar al propietario:

```
══════════════════════════════════════════════
APPROVE REPLY — [reply_id]
══════════════════════════════════════════════
Post original: [original_url]
Autor: @[original_author]

"[original_text_excerpt]"

──────────────────────────────────────────────
PROPUESTA 1 — [tipo]
[texto completo]
Riesgo: [bajo|medio|alto] — [razón]

PROPUESTA 2 — [tipo]
[texto completo]
Riesgo: [bajo|medio|alto] — [razón]

PROPUESTA 3 — [tipo]
[texto completo]
Riesgo: [bajo|medio|alto] — [razón]

──────────────────────────────────────────────
Recomendada: Propuesta [N]
══════════════════════════════════════════════
¿Cuál apruebas? (1 / 2 / 3)
O edita el texto antes de aprobar.
```

Si se indicó `--propuesta N`: usar esa propuesta directamente, sin preguntar.

---

## Paso 3 — Registrar la aprobación

Actualizar el frontmatter del archivo:
```yaml
status: approved
approved_proposal: [N]
approved_date: YYYY-MM-DD
approved_text: "[texto exacto de la propuesta aprobada]"
```

Write atómico:
1. Escribir a `content/replies/pending/[nombre].md.tmp`
2. Verificar que el `.tmp` contiene `approved_proposal: [N]`
3. Renombrar: `[nombre].md.tmp` → `[nombre].md`

Mover el archivo:
`content/replies/pending/[archivo]` → `content/replies/approved/[archivo]`

---

## Paso 4 — Audit log

Crear `logs/` si no existe.
Añadir línea a `logs/audit.log`:
```
[ISO8601] APPROVE-REPLY reply_id=[id] proposal=[N] author=@[original_author] url=[original_url]
```

---

## Paso 5 — Informe final

```
══════════════════════════════════════════════
REPLY APROBADO — [reply_id]
══════════════════════════════════════════════
Post original: [original_url]
Autor: @[original_author]

TEXTO APROBADO — copia y pega en X:
──────────────────────────────────────────────
[texto exacto de la propuesta aprobada]
──────────────────────────────────────────────

⚠ X API no disponible — envío manual requerido.
  1. Abre el post original en X: [original_url]
  2. Copia el texto de arriba y pégalo como reply
  3. Publica

Cuando hayas publicado:
  /sent-reply [reply_id]
  /sent-reply [reply_id] --url [url_del_reply_publicado]
══════════════════════════════════════════════
```

---

## Reglas críticas

- NUNCA enviar automáticamente. El propietario publica manualmente.
- Si X API estuviera disponible en el futuro: añadir paso de envío con confirmación explícita, no automático.
- El `approved_text` en el frontmatter es el sello exacto de lo que el humano aprobó.
