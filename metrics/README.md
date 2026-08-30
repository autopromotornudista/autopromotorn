---
status: approved
visibility: internal
last_updated: 2026-08-30
source_type: human_approved
---

# metrics/ — Métricas y experimentos de @AutopromotorN

## Propósito

Registro de métricas de seguimiento y experimentos propios de la cuenta. Los resultados experimentales son la única fuente de verdad local sobre el comportamiento de @AutopromotorN.

**Regla principal:** no convertir benchmarks externos en objetivos. Los benchmarks de otras cuentas, estudios de sector o investigaciones sobre el algoritmo de X son contexto, no metas.

---

## Métricas prioritarias

### Primarias — Crecimiento real

| Métrica | Qué mide |
|---------|----------|
| followers gained | Crecimiento absoluto de seguidores |
| followers / impressions | Eficiencia de conversión de alcance a seguidor |
| profile visits / impressions | Tasa de interés en la cuenta |
| followers / profile visits | Tasa de conversión visita → seguidor |

### Secundarias — Calidad del contenido

| Métrica | Qué mide |
|---------|----------|
| bookmarks / impressions | Valor percibido y utilidad del contenido |
| shares / impressions | Amplificación orgánica |
| replies / impressions | Capacidad de generar conversación |

### Negocio — Activo propio

| Métrica | Qué mide |
|---------|----------|
| emails captured | Crecimiento de lista propia |
| emails / 1000 impressions | Eficiencia de captación de email por alcance |

### Diagnósticas — Contexto, no objetivo

| Métrica | Qué mide |
|---------|----------|
| impressions | Alcance bruto — útil para normalizar otras métricas |
| likes | Señal de aprobación pasiva — diagnóstica, no primaria |

---

## Archivos

| Archivo | Función |
|---------|---------|
| `EXPERIMENTS.md` | Registro de experimentos: backlog, activos y completados |

---

## Protocolo de registro de resultados

Cuando un experimento pase de `backlog` a `active`:
1. Registrar `start_date` y `sample_size` previsto
2. Definir exactamente qué métrica se mide y cómo
3. Al completar: registrar `result`, `conclusion` y `end_date`
4. Si el resultado produce una regla operativa, documentarla en el archivo editorial correspondiente con referencia al `experiment_id`
