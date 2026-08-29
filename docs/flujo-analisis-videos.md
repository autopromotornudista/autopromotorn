# Flujo: YouTube → Contenido para @autopromotorn

## Resumen

```
YouTube URL → script → docs/fuentes/YYYY-MM-DD-titulo.md → Claude → ángulos de contenido
```

---

## Uso

### 1. Ejecutar el script

```bash
# Desde el directorio del proyecto:
python3 scripts/analizar_video.py "https://youtu.be/XXXX"

# Con título (recomendado para identificar el archivo fácilmente):
python3 scripts/analizar_video.py "https://youtu.be/XXXX" "Nombre del podcast o vídeo"
```

El script crea automáticamente `docs/fuentes/YYYY-MM-DD-titulo.md` con la transcripción completa.

### 2. Pedir los ángulos a Claude

Una vez generado el archivo, di a Claude:

> "Genera ángulos de contenido para @autopromotorn a partir del archivo docs/fuentes/[nombre-del-archivo].md"

Claude leerá la transcripción junto con tu briefing, hooks.md, guia-redaccion.md y tus datos reales del proyecto para proponer 3-5 ángulos conectados con tu experiencia.

---

## Qué hace Claude con la transcripción

Para cada ángulo de contenido Claude indica:

- **Pilar** (💶 Números · 🏗️ Proceso · 💡 Lecciones · 🧠 Reflexiones)
- **El dato clave del vídeo** que sirve de detonante
- **La conexión con tu caso real** (tus números, tu experiencia)
- **Formato sugerido** (tweet único, hilo, reflexión + pregunta)

---

## Casos de error frecuentes

| Error | Causa | Solución |
|-------|-------|----------|
| "Transcripciones desactivadas" | El autor del vídeo las desactivó | Añadir URL directamente a NotebookLM |
| "No se pudo extraer el ID" | URL con formato raro | Copiar la URL desde la barra del navegador |
| Transcripción en inglés | El vídeo solo tiene subtítulos en inglés | El script lo indica — la transcripción es igualmente usable |

---

## Archivos generados

Los archivos se acumulan en `docs/fuentes/` como base de conocimiento de fuentes externas analizadas.
