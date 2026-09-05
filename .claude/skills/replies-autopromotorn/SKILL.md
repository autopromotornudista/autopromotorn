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

**Opción B — Grok** (cuando haya rate limiting o para búsqueda más precisa): pide al usuario que consulte a Grok con búsquedas por tema. Ejemplo: *"Busca en X tweets de las últimas 24h sobre 'hipoteca autopromotor' y 'broker hipotecas'. Dame el texto, el usuario y la hora de los más interesantes."* Priorizar los grupos de mayor ventaja diferencial: tramitación hipotecaria y proceso de construcción.

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

**Búsquedas por tema** (priorizar en este orden):

*Proceso y decisiones de construcción* — experiencia directa:
- "autopromoción vivienda"
- "autopromotor"
- "construir casa propia"
- "solar vs piso"
- "gremios construcción"
- "licencia obras"
- "arquitecto técnico aparejador"
- "certificado energético obra nueva"

*Hipoteca: estudio y tramitación* — máxima ventaja diferencial:
- "hipoteca autopromotor"
- "hipoteca autopromoción"
- "broker hipotecas"
- "negociar hipoteca banco"
- "tasación vivienda"
- "FEIN FIAE"
- "notario hipoteca"
- "vinculaciones hipoteca"
- "seguro vida hipoteca banco"
- "TAE vs TIN hipoteca"
- "periodo reflexión hipoteca"
- "comisión apertura hipoteca"
- "hipoteca fija variable"
- "euríbor 2026"

*Costes y presupuesto* — tienes números reales:
- "precio m2 construcción"
- "coste construir casa"
- "presupuesto obra"
- "IVA construcción"
- "reformas vs obra nueva"

*Inversión + vivienda* — el cruce fondos/hipoteca que has vivido:
- "amortizar hipoteca o invertir"
- "fondos indexados hipoteca"
- "vivienda vs alquiler inversión"
- "fondo monetario colchon"

*Emociones y vida real* — engagement humano:
- "estrés comprar casa"
- "burocracia España vivienda"
- "alquiler caro España"
- "primera vivienda agobio"

Filtra por tweets de las últimas 24-48h con al menos alguna interacción. Descarta tweets sin respuestas o de cuentas sin relevancia en el nicho.

### 2. Seleccionar los mejores candidatos

Elige 5-10 tweets que cumplan:
- **Relevancia:** el tema conecta con alguno de los 6 pilares de la cuenta
- **Oportunidad:** hay algo real que aportar desde la experiencia propia
- **Timing:** publicado hace menos de 6h (máximo impacto); aceptable hasta 24h
- **Cuenta:** preferiblemente cuentas de la lista de objetivos de arriba

### 3. Generar los replies

Para cada tweet seleccionado, escribe un reply que aporte conocimiento o valor real sobre el tema. El caso personal es un recurso opcional, no el eje obligatorio de cada reply.

**Fórmula base:**
> [Dato, matiz o perspectiva que enriquece el tema] → [Contexto o razón por qué importa] → [Pregunta o CTA opcional]

**Cuándo usar el caso personal:**
Úsalo solo cuando el dato propio sea el argumento más fuerte disponible o cuando aporte una dimensión que no está en el tweet original. No forzarlo si hay una forma más directa de aportar valor.

**Principios:**
- El objetivo principal es aportar conocimiento útil al lector, no demostrar que "nosotros también lo vivimos"
- Cuando uses el caso personal, que sea como evidencia concreta, no como protagonismo
- Sé específico, nunca genérico — "interesante punto" no aporta nada
- Frases cortas, tono conversacional, como hablando con alguien en persona
- Sin hashtags (excepto #buildinpublic o #hipotecas si viene muy a cuento)
- Sin nombres de empresas
- Máximo 2-3 frases si no hay mucho que decir; un reply corto y bueno supera a uno largo y genérico

**Ejemplo de reply de calidad (sin caso personal):**
> Tweet original: "¿Vale la pena usar un broker para la hipoteca?"
> Reply: "Depende de tu perfil financiero y del tiempo que tengas para negociar. Para autopromoción especialmente: los bancos tienen productos distintos para este caso y muchos ni los publicitan. Un broker que conozca ese nicho marca la diferencia."

**Ejemplo de reply de calidad (con caso personal como evidencia):**
> Tweet original: "¿Vale la pena usar un broker para la hipoteca?"
> Reply: "Para autopromoción, sí. Los bancos tienen productos distintos y pocos los publicitan. En nuestro caso la diferencia fue de 0,40 puntos en el TIN — que en 25 años son miles de euros."

**Ejemplo de reply a evitar:**
> "En nuestro caso sí. Sin broker nos ofrecían 2,45%. Con broker cerramos a 2,05%." *(el caso propio como único argumento, sin conocimiento transferible)*

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
