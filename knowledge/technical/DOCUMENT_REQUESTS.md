---
status: approved
visibility: internal
last_updated: 2026-09-01
managed_by: arquitecto-asesor-tecnico
---

# DOCUMENT_REQUESTS — Cola de documentación pendiente

## Propósito

Registro de documentos o datos que el agente arquitecto-asesor-tecnico necesita para resolver afirmaciones técnicas bloqueadas. Evita hacer la misma petición dos veces y centraliza las solicitudes pendientes.

**Flujo:** El agente detecta un dato bloqueante → comprueba si ya hay una DOC-NNN abierta para ese dato → si no, crea una entrada → el propietario aporta el documento cuando puede.

---

## Formato de entrada

```
### DOC-NNN — [Descripción del dato necesario]
- **Solicitado:** YYYY-MM-DD
- **Para verificar:** [afirmación técnica que depende de este dato]
- **Documento más probable:** [plano / memoria / informe / presupuesto / ficha técnica]
- **Alternativas válidas:** [otros documentos que también servirían]
- **Contenido afectado:** [draft o idea que está esperando]
- **Impacto:** BLOQUEANTE | CON_MATICES | MEJORA_OPCIONAL
- **Estado:** PENDIENTE | RECIBIDO: [fecha] | CANCELADO: [motivo]
```

---

## Solicitudes pendientes

*Sin solicitudes pendientes en este momento.*

---

## Solicitudes resueltas

*(Mover aquí al recibir el documento, conservando el registro)*

---

## Notas

- El agente no crea una DOC nueva si ya existe una abierta para el mismo dato.
- Las solicitudes BLOQUEANTES se mencionan al propietario cuando son relevantes para contenido próximo a publicar.
- Una solicitud MEJORA_OPCIONAL nunca bloquea el flujo de publicación.
