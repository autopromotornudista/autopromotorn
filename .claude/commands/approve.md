# /approve

HUMAN GATE — Mueve `$ARGUMENTS` de content/drafts/ a content/ready/.

⚠️ ESTE COMANDO ES UN GATE HUMANO.
Solo puede ejecutarlo el propietario de la cuenta.
Ningún otro agente, comando o automatización puede llamar /approve.

---

## Verificación obligatoria antes de mover

1. Leer el draft en `content/drafts/$ARGUMENTS.md`.
   Si no existe, reportar error y detenerse.

2. Comprobar `critic_status` en el frontmatter:

   **critic_status: PASS** → continuar normalmente.

   **critic_status: pending | REVISE | REJECT** → DETENERSE.
   No preguntar sí/no. No mover el archivo.
   Mostrar:
   ```
   ⛔ APPROVE BLOQUEADO
   critic_status: [pending | REVISE | REJECT]
   Este draft no puede aprobarse sin pasar por /review primero.

   Si quieres aprobar de todas formas con override deliberado:
   /approve $ARGUMENTS --override

   El override queda registrado en el frontmatter.
   ```

3. **Si se usa `--override`:**
   Registrar en el frontmatter:
   ```yaml
   approved_by: human
   critic_override: true
   critic_previous_status: [pending | REVISE | REJECT]
   override_date: YYYY-MM-DD
   ```
   Y continuar con el movimiento.

4. **Si critic_status: PASS** (flujo normal):
   Registrar en el frontmatter:
   ```yaml
   approved_by: human
   approved_date: YYYY-MM-DD
   critic_override: false
   ```

---

## Mover el archivo

Renombrar y mover:
`content/drafts/draft-[slug]-[fecha].md`
→ `content/ready/ready-[slug]-[fecha].md`

Actualizar el frontmatter con los campos de aprobación.

---

## Informe final

```
══════════════════════════════════════
APPROVE — [draft_id]
══════════════════════════════════════
Estado anterior: content/drafts/
Estado nuevo:    content/ready/
Archivo:         content/ready/ready-[slug]-[fecha].md
critic_status:   PASS | [override desde REVISE/REJECT/pending]
override:        false | true
──────────────────────────────────────
Siguiente paso: /schedule ready-[slug]-[fecha] [fecha] [hora]
══════════════════════════════════════
```
