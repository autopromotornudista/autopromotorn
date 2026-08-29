#!/usr/bin/env python3
"""
Extrae la transcripción de un vídeo de YouTube y la guarda en docs/fuentes/
para generar ángulos de contenido con Claude para @autopromotorn.

Uso:
    python3 scripts/analizar_video.py "https://youtu.be/XXXX"
    python3 scripts/analizar_video.py "https://youtu.be/XXXX" "Título del podcast"
"""

import sys
import re
import os
from datetime import datetime

try:
    from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
except ImportError:
    print("❌ Dependencia no instalada. Ejecuta: pip install youtube-transcript-api")
    sys.exit(1)


def extract_video_id(url):
    patterns = [
        r'youtube\.com/watch\?v=([^&\s]+)',
        r'youtu\.be/([^?\s]+)',
        r'youtube\.com/embed/([^?\s]+)',
        r'youtube\.com/shorts/([^?\s]+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)

        langs_es = ['es', 'es-ES', 'es-419', 'es-MX']

        # Prioridad: español manual → español auto-generado → traducción al español → primer idioma disponible
        for attempt in [
            lambda: transcript_list.find_manually_created_transcript(langs_es),
            lambda: transcript_list.find_generated_transcript(langs_es),
            lambda: next(iter(transcript_list)).translate('es'),
            lambda: next(iter(transcript_list)),
        ]:
            try:
                transcript = attempt()
                data = transcript.fetch()
                lang = getattr(transcript, 'language_code', 'desconocido')
                return data, lang
            except Exception:
                continue

        return None, None

    except TranscriptsDisabled:
        print("❌ Este vídeo tiene las transcripciones desactivadas.")
        return None, None
    except Exception as e:
        print(f"❌ Error al obtener transcripción: {e}")
        return None, None


def format_transcript(transcript_data):
    # FetchedTranscript es iterable; cada snippet tiene .text, .start, .duration
    chunks = []
    buffer = []
    buffer_len = 0

    for snippet in transcript_data:
        text = snippet.text.strip()
        if not text:
            continue
        buffer.append(text)
        buffer_len += len(text)
        if buffer_len >= 400:
            chunks.append(' '.join(buffer))
            buffer = []
            buffer_len = 0

    if buffer:
        chunks.append(' '.join(buffer))

    return '\n\n'.join(chunks)


def slugify(text, max_len=50):
    text = text.lower()
    text = re.sub(r'[áàäâ]', 'a', text)
    text = re.sub(r'[éèëê]', 'e', text)
    text = re.sub(r'[íìïî]', 'i', text)
    text = re.sub(r'[óòöô]', 'o', text)
    text = re.sub(r'[úùüû]', 'u', text)
    text = re.sub(r'ñ', 'n', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text[:max_len]


def save_transcript(url, video_id, title, transcript_text, lang):
    date_str = datetime.now().strftime('%Y-%m-%d')
    slug = slugify(title) if title else video_id
    filename = f"{date_str}-{slug}.md"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    fuentes_dir = os.path.join(project_root, 'docs', 'fuentes')
    os.makedirs(fuentes_dir, exist_ok=True)

    filepath = os.path.join(fuentes_dir, filename)
    rel_path = os.path.relpath(filepath, project_root)

    lang_note = f"(idioma original: {lang})" if lang not in ('es', 'es-ES', 'es-419') else ""

    content = f"""# Fuente: {title or video_id}

## Metadatos

| Campo | Valor |
|-------|-------|
| URL | {url} |
| ID vídeo | {video_id} |
| Fecha de análisis | {date_str} |
| Idioma transcripción | {lang} {lang_note} |

---

## Transcripción completa

{transcript_text}
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath, rel_path


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    url = sys.argv[1]
    title = ' '.join(sys.argv[2:]) if len(sys.argv) > 2 else ""

    video_id = extract_video_id(url)
    if not video_id:
        print(f"❌ No se ha podido extraer el ID del vídeo de: {url}")
        sys.exit(1)

    print(f"🎬 Vídeo ID: {video_id}")
    print(f"⏳ Extrayendo transcripción...")

    transcript_data, lang = get_transcript(video_id)

    if not transcript_data:
        print("\n💡 No hay transcripción disponible en YouTube para este vídeo.")
        print("   Alternativa: añade la URL directamente a NotebookLM.")
        sys.exit(1)

    print(f"✅ Transcripción obtenida ({lang})")

    transcript_text = format_transcript(transcript_data)
    filepath, rel_path = save_transcript(url, video_id, title, transcript_text, lang)

    words = len(transcript_text.split())
    print(f"💾 Guardado en: {rel_path}")
    print(f"📝 {words:,} palabras transcritas")
    print()
    print("─" * 60)
    print("SIGUIENTE PASO")
    print("─" * 60)
    print(f'Di a Claude: "Genera ángulos de contenido para')
    print(f'@autopromotorn a partir del archivo {rel_path}"')
    print("─" * 60)


if __name__ == '__main__':
    main()
