# AGENTS.md — Autopromotor Nudista (@autopromotorn)

Normas del repositorio para cualquier agente (Claude Code, Codex, otros). `CLAUDE.md` importa este archivo y añade solo lo específico de Claude Code.

## Descripción

Sistema de contenido build-in-public sobre autopromoción de vivienda en España. Genera, revisa y programa publicaciones para X y Instagram a partir de la experiencia real del proyecto (casa en Abelar). Los textos se publican en nombre de una familia, así que la veracidad y la privacidad pesan más que la velocidad.

## Identidad y principios editoriales

- **Cuenta:** @autopromotorn en X. **Nombre:** Autopromotor Nudista. **Concepto:** build-in-public auténtico.
- **Skin in the game:** todo el contenido se escribe desde la experiencia propia vivida. Cada texto parte de "nosotros hicimos esto", nunca de "deberías hacer esto". El consejo llega después de contar la experiencia.
- **Fórmula base:** `[Situación real propia] → [Dato concreto] → [Lo que aprendimos] → [Pregunta o CTA]`.

## Reglas críticas (siempre activas)

1. **Voz plural:** "nosotros" (contratamos, decidimos, firmamos). Nunca singular.
2. **Sin nombres de empresas:** "el constructor", "el banco". Nunca nombres propios.
3. **Sin datos inventados:** si falta un dato real, preguntar. Nunca estimar ni rellenar con IA.
4. **Deduplicación antes de generar contenido,** en este orden: `content/published/` → `contenido/tweets-publicados.md` → `content/ready/` y `content/scheduled/` → `content/planning/` (READY/SCHEDULED ya utilizado) → `content/drafts/`.
5. **`contenido/` es LEGACY intocable:** no borrar, mover ni modificar sin autorización expresa.
6. **Antes de reorganizar archivos,** leer `knowledge/GUIA_BUENAS_PRACTICAS.md`.

## Puertas humanas (ningún agente las cruza)

Estas acciones requieren aprobación humana explícita en cada caso:

- `/approve` (y su equivalente): el gate humano es inviolable. Mueve contenido a `content/ready/`.
- `/schedule --confirm`: única vía que crea posts en Buffer.
- `/approve-reply`: gate para replies.
- `python3 scripts/instagram_pipeline.py approve ... --human-confirmed`: gate de Instagram.
- Actualizar `knowledge/` sin dejar constancia.

Si el hash SHA256 de un paquete no coincide con el aprobado, la operación se bloquea. No se pregunta al usuario, se detiene.

## Estructura

| Ruta | Contenido |
|------|-----------|
| `content/` | Pipeline de posts: `ideas/`, `planning/`, `drafts/`, `ready/`, `scheduled/`, `published/`, `replies/` (pending, approved, sent), `instagram/` |
| `contenido/` | Material LEGACY de X. Solo lectura |
| `editorial/` | Voz, formatos, hooks, ángulos, reglas de Instagram y replies |
| `knowledge/` | Conocimiento aprobado: contexto validado, finanzas, hipoteca, timeline, reglas editoriales |
| `docs/` | Documentación de obra, guías y material visual. Varias subcarpetas son privadas |
| `scripts/` | Versionados: `analizar_articulo.py`, `analizar_video.py`, `background_runner.sh`, `agent-worktree.sh`. Sin versionar aún: `instagram_pipeline.py`, `render_instagram_carousel.py`, `import_buffer_instagram.py` |
| `tests/` | Sin versionar aún (ver Comandos) |
| `agents/` | Definiciones de subagentes (WRITER, CRITIC, REPLY, HARVESTER, FORUM_SCOUT) |
| `inbox/`, `sources/` | Fuentes en bruto (artículos, notas, vídeos). Privadas |
| `logs/`, `metrics/` | Logs y métricas locales. `logs/*.log` y `logs/*.json` no se versionan |

## Comandos

No hay sistema de build ni configuración de lint en el repositorio. No inventar ninguno.

- Ejecución en segundo plano (solo mantenimiento, sin decisiones editoriales): `bash scripts/background_runner.sh`
- Crear un worktree para un agente: `scripts/agent-worktree.sh <agente> <tarea> [rama-base]`
- Pipeline de Instagram (`scripts/instagram_pipeline.py`) y render de carruseles (`scripts/render_instagram_carousel.py`): todavía no están versionados. Cuando se versionen, sus comandos se documentarán aquí.
- Tests: `tests/test_instagram_pipeline.py` (`unittest`) tampoco está versionado. No hay comando de test oficial del repositorio todavía.
- Python: 3.10 (los `.pyc` locales son `cpython-310`). No hay `requirements.txt`; las dependencias no están declaradas.

## Convenciones de código y de contenido

- **Commits:** prefijo convencional en español (`feat:`, `chore:`), por ejemplo `feat: sesión 14/09 — ...`.
- **Scripts Python:** `argparse` con subcomandos, funciones tipadas en las firmas, salida por `print` y código de retorno entero desde `main()`.
- **IDs estables:** posts `content_id: DRAFT-YYYYMMDD-NNN` en el frontmatter; replies `reply_id: REPLY-YYYYMMDD-NNN`. No cambian al mover el archivo de carpeta.
- **Hashes:** `content_hash` SHA256 para validar que el texto aprobado es el que se programa.
- **Naming y ubicación de archivos:** ver `knowledge/GUIA_BUENAS_PRACTICAS.md`.

## No tocar

- `contenido/` (LEGACY), `content/published/`.
- `knowledge/` salvo que se pida explícitamente.
- Carpetas privadas, nunca leer para publicar ni versionar su contenido: `docs/hipoteca/`, `docs/tasacion/`, `docs/finanzas/`, `docs/presupuestos-construccion/`, `docs/fotos-reales/`, `docs/renders/`, `docs/contexto-ia/`, `docs/Proxecto Vivenda O Abelar/`, `inbox/`, `sources/`.
- Secretos y credenciales (`.env`, `*.key`, `*token*`, `*credentials*`). Ninguno va al repositorio.
- Los binarios y medios: `*.pdf` y `*.png` en `docs/` están ignorados.
- No borrar archivos de `content/` para "limpiar". Los cambios pendientes del usuario se respetan.

## Dónde leer antes de escribir

| Tarea | Leer primero |
|-------|--------------|
| Cualquier texto | `knowledge/VALIDATED_CONTEXT_2026-08-31.md` (fuente de verdad) y `editorial/VOICE.md` |
| Formatos y ganchos | `editorial/FORMATS.md`, `editorial/HOOKS.md`, `editorial/ANGLES.md` |
| Pilares y cadencia | `knowledge/CONTENT_PILLARS.md`, `knowledge/CADENCIA.md` |
| Instagram | `editorial/INSTAGRAM.md` |
| Estado de obra | `docs/diario-obra.md` |
| Finanzas e hipoteca | `knowledge/FINANCES.md`, `knowledge/MORTGAGE.md` (solo lectura para contar; nunca estimar) |
| Replies | `editorial/REPLIES.md`, `knowledge/STRATEGY.md` |
| Normativa (CTE) | `knowledge/technical/CTE/README.md` |
| Arquitectura y gobierno | `knowledge/README.md`, `knowledge/EDITORIAL_RULES.md` |

## Flujo de trabajo con varios agentes

- **Un agente por tarea y un worktree por agente.** Así dos agentes nunca editan el mismo árbol.
- Crear el worktree con `scripts/agent-worktree.sh <agente> <tarea>`. Crea la rama `agent/<agente>/<tarea>` y el worktree en `~/worktrees/<proyecto>/`, fuera del repositorio.
- **Commit antes de cambiar de agente.** Un worktree con cambios sin commitear no se abandona.
- **Revisar con `git diff` antes de fusionar** (`git diff main...agent/<agente>/<tarea>`). Nunca fusionar sin leer el diff.
- Abrir un worktree en VS Code: `code -n <ruta>`.
