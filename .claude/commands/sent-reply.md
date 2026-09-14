# /sent-reply

Registra que un reply aprobado fue publicado manualmente en X.

`$ARGUMENTS` = reply_id  (ej: `REPLY-20260908-001`)
Flag opcional: `--url https://x.com/...`

Ejecutar DESPUÉS de publicar el reply manualmente en X.

---

## Paso 1 — Localizar el archivo

Buscar en `content/replies/approved/` el archivo con `reply_id: [ARGUMENTS]` en el frontmatter.

Si no se encuentra en `approved/`, buscar también en `pending/` (por si /approve-reply no se ejecutó).

Si no se encuentra en ningún sitio:
```
⛔ REPLY NO ENCONTRADO
reply_id: [ARGUMENTS]
No hay ningún archivo en content/replies/approved/ con ese ID.
Si no has ejecutado /approve-reply aún, hazlo primero.
```
Detenerse.

---

## Paso 2 — Actualizar frontmatter

```yaml
status: sent
sent_date: YYYY-MM-DD
sent_url: [URL si se proporcionó con --url, sino "manual-sin-url"]
```

Write atómico:
1. Escribir a `[archivo].md.tmp`
2. Verificar que `.tmp` contiene `status: sent`
3. Renombrar `.tmp` → `.md`

---

## Paso 3 — Mover el archivo

`content/replies/approved/[archivo]` → `content/replies/sent/[archivo]`

---

## Paso 4 — Audit log

Añadir línea a `logs/audit.log`:
```
[ISO8601] SENT-REPLY reply_id=[id] url=[url_o_"manual-sin-url"] author=@[original_author]
```

---

## Paso 5 — Informe final

```
══════════════════════════════════════════════
REPLY REGISTRADO COMO ENVIADO — [reply_id]
══════════════════════════════════════════════
Para: @[original_author]
Enviado: [sent_date]
[Si URL: URL: [sent_url]]
[Si sin URL: URL: no registrada — añade con /sent-reply [id] --url [url] si quieres registrarla]
Archivo: content/replies/sent/[archivo]
══════════════════════════════════════════════
```
