---
status: external_reference
volatile: true
canonical: false
date: 2026-08
source: Grok research (X/Twitter ranking systems, agosto 2026)
---

# Ranking de X — Resumen de referencia (agosto 2026)

Resumen de investigación externa sobre el sistema de ranking de X. No es knowledge canónico. No debe utilizarse como base factual para afirmaciones públicas. Contexto operativo para entender las limitaciones del sistema.

---

## Puntos clave

### 1. Sistema actual: Phoenix

El sistema de ranking publicado actualmente por X se denomina **Phoenix**. Es el sistema de referencia de agosto 2026. No es el mismo sistema que generó los ratios históricos que han circulado ampliamente (27×, 150×, etc.).

### 2. Los coeficientes no equivalen a conteos de likes

Los coeficientes del sistema de ranking de X predicen distintas **acciones futuras**, no representan equivalencias directas entre tipos de engagement ("un reply vale N likes"). Esta interpretación es una simplificación incorrecta del funcionamiento real del sistema.

### 3. Los ratios 27× / 150× son históricos (sistema pre-2024)

Las equivalencias numéricas que circularon ampliamente (reply = 27× like, reply con respuesta del autor = 150× like) pertenecen a versiones anteriores del algoritmo. No deben usarse como referencia del comportamiento actual del sistema.

### 4. Sistema volátil

Los parámetros del ranking de X cambian sin previo aviso y sin publicación de documentación oficial. Cualquier referencia a coeficientes concretos tiene fecha de caducidad incierta.

### 5. Ausencia de umbrales oficiales fiables de timing

No existen umbrales oficiales verificados para los intervalos de tiempo frecuentemente citados (5, 15, 30, 60 minutos). Su impacto real en el alcance no está documentado públicamente por X.

### 6. Links: no asumir penalización fija

La penalización de enlaces en posts es un comportamiento reportado pero no documentado oficialmente. No debe asumirse como regla fija e invariable. Su impacto puede variar según contexto, tipo de cuenta y estado del algoritmo.

### 7. Necesidad de experimentación propia

Dado que el sistema es volátil y los datos públicos son históricos o no verificables, la única fuente de verdad local es la experimentación propia con datos de @AutopromotorN. Ver `metrics/EXPERIMENTS.md`.

### 8. Distintas acciones predichas

El sistema de ranking modela distintos tipos de comportamiento futuro del usuario, no solo engagement inmediato. Esto hace que la optimización para una única señal (likes, replies) sea una simplificación del funcionamiento real.

---

## Implicaciones operativas para @AutopromotorN

- No citar ratios numéricos del algoritmo como hechos en contenido público.
- No optimizar mecánicamente para señales concretas basándose en coeficientes históricos.
- Tratar timing, formatos y volumen de replies como hipótesis a validar con datos propios.
- Documentar experimentos en `metrics/EXPERIMENTS.md` antes de establecer cualquier regla operativa.
