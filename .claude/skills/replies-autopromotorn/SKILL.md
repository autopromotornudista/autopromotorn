---
name: replies-autopromotorn
description: Sesiones de reply estratégico para @autopromotorn en X. Usa este skill cuando el usuario quiera hacer replies, buscar conversaciones en el nicho, responder en X, hacer engagement, o crecer en Twitter/X. Actívalo ante frases como "vamos a hacer replies", "sesión de replies", "buscar conversaciones", "qué hay en el nicho hoy", "quiero responder a...", "engagement". Este skill es la acción diaria más importante para crecer en X — úsalo proactivamente cuando el usuario mencione crecimiento, seguidores o interacción.
---

# Replies estratégicos — @autopromotorn

## Contexto

Los replies son la señal más poderosa del algoritmo de X: un reply del autor pesa ~150× un like. Esta es la palanca de crecimiento más efectiva de la cuenta, por encima de publicar contenido propio.

Antes de empezar, lee `/home/pineapple/proyectos/autopromotorn/CLAUDE.md` para tener el tono, las reglas y los pilares frescos en contexto.

## Flujo de una sesión

### 1. Buscar conversaciones

**Opción A — Twitter MCP** (si no hay rate limiting): usa `mcp__twitterapi-mcp__get_user_tweets` y `search_tweets` para las cuentas y temas de abajo.

**Opción B — Grok** (cuando haya rate limiting o para búsqueda más precisa): pide al usuario que consulte a Grok con preguntas concretas. Ejemplo: *"¿Qué ha publicado @HoolInvestor en las últimas 24h? Dame el texto y la hora."* Es la forma más fiable de obtener tweets recientes del nicho.

Busca en este orden de prioridad:

**Cuentas objetivo — Prioridad alta** (gran audiencia + nicho muy directo):
- @HoolInvestor (~33.600 seg.) — inversión inmobiliaria real, operaciones reales, hipotecas
- @parasitoahorro (~46.500 seg.) — fondos indexados, Bitcoin, costes de vivienda
- @Inversoracon30 (~19.200 seg.) — libertad financiera + mercado inmobiliario España
- @ZoeGutier (~25.400 seg.) — independencia financiera, decisiones de dinero
- @Hipotelab (~12.700 seg.) — broker hipotecas, financiación, negociación con bancos
- @MarcosBL (~9.200 seg.) — promotor build-in-public, autopromoción

**Cuentas objetivo — Prioridad media** (audiencia menor, nicho muy alineado):
- @AhorroDePadre (~3.000 seg.) — finanzas para familias, costes reales, construcción
- @IngAhorrador (~4.500 seg.) — ahorro práctico, ingresos extra

**Cuentas objetivo — Audiencia similar** (engagement mutuo más probable):
- @ProfeFinanciero (~930 seg.) — fondos indexados + Bitcoin + DCA
- @HazloSimple_ (~900 seg.) — inversión y finanzas personales
- @viarentable (~760 seg.) — economía práctica, inmobiliario

**Búsquedas por tema:**
- "autopromoción vivienda"
- "hipoteca autopromotor"
- "construir casa España"
- "precio construcción 2026"
- "fondos indexados hipoteca"
- "ahorrar para casa"
- "primera vivienda España"

Filtra por tweets de las últimas 24-48h con al menos alguna interacción. Descarta tweets sin respuestas o de cuentas sin relevancia en el nicho.

### 2. Seleccionar los mejores candidatos

Elige 5-10 tweets que cumplan:
- **Relevancia:** el tema conecta con alguno de los 6 pilares de la cuenta
- **Oportunidad:** hay algo real que aportar desde la experiencia propia
- **Timing:** publicado hace menos de 6h (máximo impacto); aceptable hasta 24h
- **Cuenta:** preferiblemente cuentas de la lista de objetivos de arriba

### 3. Generar los replies

Para cada tweet seleccionado, escribe un reply siguiendo esta fórmula:

**Fórmula base:**
> [Conexión genuina con lo que dice] → [Mi experiencia real / dato concreto de mi caso] → [Aporte o pregunta]

**Principios:**
- Habla siempre desde la experiencia propia ("nosotros hicimos...", "en nuestro caso...")
- Usa datos reales del proyecto cuando sean relevantes (410.000€, 2,05% TIN, 5 años, etc.)
- Sé específico, nunca genérico — "yo también" no aporta nada
- Frases cortas, tono conversacional, como hablando con alguien en persona
- Sin hashtags (excepto #buildinpublic o #hipotecas si viene muy a cuento)
- Sin nombres de empresas
- Sin consejos del tipo "deberías hacer X" — siempre "nosotros hicimos X"
- Máximo 2-3 frases si no hay mucho que decir; un reply corto y bueno supera a uno largo y genérico

**Ejemplo de reply de calidad:**
> Tweet original: "¿Vale la pena usar un broker para la hipoteca?"
> Reply: "En nuestro caso sí. Sin broker nos ofrecían 2,45%. Con broker cerramos a 2,05%. La diferencia en 30 años son miles de euros. Depende mucho de cuánto tiempo tengas para negociar tú solo."

**Ejemplo de reply a evitar:**
> "Totalmente de acuerdo, los brokers son muy útiles. ¡Suerte con tu hipoteca!"

### 4. Presentar al usuario

Muestra cada reply así:

---
**Tweet de [@usuario]:**
> [texto del tweet original]

**Reply propuesto:**
> [tu reply]

✅ Publicar | ✏️ Editar | ❌ Descartar

---

Presenta todos los replies de una vez para que el usuario pueda revisarlos en bloque o uno a uno. **Nunca publiques sin aprobación explícita.**

### 5. Publicar los aprobados

Cuando el usuario apruebe un reply, usa `mcp__twitterapi-mcp__create_tweet` con el parámetro `reply_to_tweet_id` para publicarlo como respuesta al tweet original.

Confirma cada publicación con el link al tweet.

## Reglas de oro

- **Velocidad:** los primeros 60 minutos tras publicar un tweet son los más valiosos. Si encuentras un tweet reciente de una cuenta objetivo, priorízalo.
- **Calidad sobre cantidad:** 5 replies buenos > 15 replies genéricos. El algoritmo penaliza el spam.
- **Nunca automatizar:** cada reply necesita aprobación manual del usuario. El riesgo de suspensión no vale la pena.
- **Responder a los que te responden:** si alguien respondió a un tweet de @autopromotorn, ese reply tiene prioridad máxima (150× un like cuando el autor responde).

## Cierre de sesión

Al terminar, resume:
- Cuántos replies publicados
- En qué cuentas/temas
- Si hay alguna conversación interesante que seguir mañana
