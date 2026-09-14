# /approve

HUMAN GATE — Aprueba uno o más drafts, calcula hash SHA256 del contenido y mueve a content/ready/.

```
FORMAS DE USO:
  /approve DRAFT-20260908-001
  /approve DRAFT-20260908-001 DRAFT-20260908-003 DRAFT-20260908-005
  /approve DRAFT-20260908-001 --override
  /approve draft-[slug]-[fecha]          ← también acepta nombre de archivo legacy
```

⚠️ ESTE COMANDO ES UN GATE HUMANO.
Solo puede ejecutarlo el propietario de la cuenta.
Ningún otro agente, comando o automatización puede llamar /approve.

---

## Paso 0 — Parsear argumentos

Separar los identificadores de los flags (`--override`).
Construir lista de items a procesar.
Si la lista está vacía: reportar error y detenerse.

Los identificadores pueden ser:
- `content_id`: formato `DRAFT-YYYYMMDD-NNN` → buscar en `content/drafts/` el archivo con ese `content_id` en el frontmatter
- Nombre de archivo: formato `draft-[slug]-[fecha]` → buscar `content/drafts/draft-[slug]-[fecha].md` directamente
- Archivos legacy sin `content_id`: aceptar por nombre de archivo y procesarlos normalmente (sin content_id el hash sigue funcionando)

---

## PARA CADA ITEM EN LA LISTA:

### Paso 1 — Localizar el archivo

Buscar en `content/drafts/` usando el identificador.
Si no se encuentra: registrar error para este item y **continuar con el siguiente**.

### Paso 2 — Verificar critic_status

**critic_status: PASS** → continuar normalmente.

**critic_status: pending | REVISE | REJECT** → DETENERSE para este item.
No preguntar sí/no. No mover el archivo.
Registrar en el informe batch: `✗ BLOQUEADO — critic_status: [valor]`.

Si se usa `--override` → continuar con el item y registrar el override.

### Paso 3 — Calcular content_hash (SHA256)

```
1. Leer el archivo completo como texto
2. Identificar la SEGUNDA línea que sea exactamente "---" (fin del frontmatter YAML)
3. Extraer TODO el texto desde esa segunda "---" en adelante (incluida la línea "---" misma)
4. Calcular SHA256 de ese cuerpo en encoding UTF-8
   Método: Bash(echo -n "[cuerpo]" | sha256sum)
   O equivalente con Python: hashlib.sha256(body.encode('utf-8')).hexdigest()
5. Resultado: "sha256:<64 chars hexadecimales>"
```

El cuerpo incluye la línea `---` de cierre del frontmatter porque es parte del separador y garantiza determinismo. Lo importante es que el método sea consistente entre /approve y /schedule --confirm.

### Paso 4 — Actualizar frontmatter (write atómico)

Campos a añadir/actualizar:
```yaml
approved_by: human
approved_date: YYYY-MM-DD
critic_override: false  # o true si --override
critic_previous_status: [valor anterior]  # solo si override
override_date: YYYY-MM-DD  # solo si override
content_hash: sha256:<64hex>
content_hash_date: YYYY-MM-DDTHH:MM:SS
```

**Write atómico obligatorio:**
1. Preparar el contenido completo del archivo con el frontmatter actualizado
2. Escribir a `content/drafts/[nombre].md.tmp`
3. Verificar que el `.tmp` contiene `content_hash: sha256:` (leer el campo del archivo)
4. Si la verificación falla: borrar el `.tmp` y registrar error para este item
5. Si la verificación OK: renombrar `[nombre].md.tmp` → `[nombre].md` (reemplaza el original)

### Paso 5 — Mover a content/ready/

Mover el archivo:
`content/drafts/draft-[slug]-[fecha].md` → `content/ready/ready-[slug]-[fecha].md`

El `content_id`, `content_hash` y todos los campos de aprobación viajan con el archivo.

### Paso 6 — Audit log

Crear `logs/` si no existe.
Añadir línea a `logs/audit.log`:
```
[ISO8601] APPROVE content_id=[id_o_"legacy"] hash=sha256:[primeros8chars]... file=content/ready/ready-[slug]-[fecha].md override=[true|false]
```

---

## FIN DEL BUCLE

### Paso 7 — Informe batch final

```
══════════════════════════════════════════════
APPROVE — [N_aprobados]/[N_total] aprobados
══════════════════════════════════════════════
[content_id_1]  ✓ APROBADO  hash: sha256:[8chars]...  →  content/ready/ready-[slug]-[fecha].md
[content_id_3]  ✓ APROBADO  hash: sha256:[8chars]...  →  content/ready/ready-[slug]-[fecha].md
[content_id_5]  ✗ ERROR: no encontrado en content/drafts/
[content_id_7]  ✗ BLOQUEADO: critic_status: REVISE — ejecuta /review primero

──────────────────────────────────────────────
Aprobados: [N] · Errores/bloqueados: [N]
Archivos en content/ready/: [N]

Siguiente paso:
  /schedule [content_id] para programar en Buffer cada pieza aprobada
  o usa /inbox para ver la bandeja completa con slots propuestos
══════════════════════════════════════════════
```

---

## Regla sobre aprobación desde /inbox

Cuando el propietario dice "apruebo [N]" o "apruebo [N] y [M]" en el contexto de una sesión donde `/inbox` ya mostró la propuesta completa (texto + slot + canal), Claude:

1. Identifica los `content_id` correspondientes a los números [N], [M]
2. Ejecuta `/approve [content_id_N] [content_id_M]` (este comando)
3. Inmediatamente después, sin preguntar de nuevo, ejecuta `/schedule [content_id] --confirm` para cada ítem aprobado usando el slot propuesto en /inbox

Esta cadena es automática porque /inbox ya actuó como el punto de revisión única. El hash check en /schedule --confirm es automático — si falla, es un bloqueo, no una pregunta al usuario.

---

## Tabla de permisos (actualizada)

| Comando | ¿Puede llamar /approve? |
|---------|------------------------|
| Propietario humano | ✓ ÚNICO AUTORIZADO |
| Cualquier agente automatizado | ✗ nunca |
| /prepare | ✗ nunca |
| /auto-week | ✗ nunca |
| /forum-scout | ✗ nunca |
