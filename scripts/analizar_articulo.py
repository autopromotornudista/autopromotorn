#!/usr/bin/env python3
"""
Extrae el contenido de un artículo web o newsletter (Substack u otros) y lo guarda en sources/
para generar ángulos de contenido con Claude para @autopromotorn.

Uso:
    python3 scripts/analizar_articulo.py "https://example.com/articulo"
    python3 scripts/analizar_articulo.py "https://example.com/articulo" "Título opcional"
    python3 scripts/analizar_articulo.py "https://example.com" --type newsletter

Tipos detectados automáticamente: substack.com, beehiiv.com, mailchimp.com → sources/newsletters/
Resto de URLs → sources/web/
"""

import sys
import re
import os
from datetime import datetime

try:
    import requests
except ImportError:
    print("❌ Dependencia no instalada. Ejecuta: pip install requests beautifulsoup4")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ Dependencia no instalada. Ejecuta: pip install beautifulsoup4")
    sys.exit(1)


NEWSLETTER_DOMAINS = [
    'substack.com',
    'beehiiv.com',
    'mailchimp.com',
    'convertkit.com',
    'mailerlite.com',
    'revue.co',
    'ghost.io',
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; AutopromotorN-Harvester/1.0)',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
}


def detect_type(url):
    for domain in NEWSLETTER_DOMAINS:
        if domain in url:
            return 'newsletter'
    return 'web'


def extract_metadata(soup, url):
    title = ''
    author = ''
    date = ''

    # Title: og:title → twitter:title → <title>
    for meta in soup.find_all('meta'):
        prop = meta.get('property', '') or meta.get('name', '')
        content = meta.get('content', '')
        if prop == 'og:title' and not title:
            title = content
        elif prop == 'twitter:title' and not title:
            title = content
        elif prop in ('author', 'article:author') and not author:
            author = content
        elif prop in ('article:published_time', 'datePublished') and not date:
            date = content[:10]  # YYYY-MM-DD

    if not title:
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text(strip=True)

    # Substack-specific: author in .subtitle or .post-header
    if not author:
        for sel in ['.post-header .author', '.subtitle', '[data-component-name="Author"]']:
            el = soup.select_one(sel)
            if el:
                author = el.get_text(strip=True)
                break

    # Date fallback: look for time tag
    if not date:
        time_tag = soup.find('time')
        if time_tag:
            dt = time_tag.get('datetime', '')
            if dt:
                date = dt[:10]

    return title.strip(), author.strip(), date.strip()


def extract_content(soup):
    # Remove navigation, ads, scripts, styles
    for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside',
                     'noscript', 'iframe', 'svg', 'form']):
        tag.decompose()

    # Try common content selectors in priority order
    selectors = [
        'article',
        '.post-content',
        '.article-content',
        '.entry-content',
        '.body.markup',            # Substack
        '#main-content',
        'main',
        '.content',
    ]

    for sel in selectors:
        el = soup.select_one(sel)
        if el:
            return clean_text(el.get_text(separator='\n'))

    # Fallback: body
    body = soup.find('body')
    if body:
        return clean_text(body.get_text(separator='\n'))

    return ''


def clean_text(text):
    lines = text.splitlines()
    cleaned = []
    prev_blank = False
    for line in lines:
        line = line.strip()
        if not line:
            if not prev_blank:
                cleaned.append('')
            prev_blank = True
        else:
            cleaned.append(line)
            prev_blank = False
    return '\n'.join(cleaned).strip()


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


def save_source(url, title, author, date_published, content, source_type):
    date_str = datetime.now().strftime('%Y-%m-%d')
    slug = slugify(title) if title else slugify(url.split('//')[-1])
    filename = f"{date_str}-{slug}.md"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    subdir = 'newsletters' if source_type == 'newsletter' else 'web'
    dest_dir = os.path.join(project_root, 'sources', subdir)
    os.makedirs(dest_dir, exist_ok=True)

    filepath = os.path.join(dest_dir, filename)
    rel_path = os.path.relpath(filepath, project_root)

    content_md = f"""# Fuente: {title or url}

## Metadatos

| Campo | Valor |
|-------|-------|
| URL | {url} |
| Autor | {author or 'sin detectar'} |
| Fecha publicación | {date_published or 'sin detectar'} |
| Fecha de análisis | {date_str} |
| Tipo | {source_type} |

---

## Contenido extraído

{content}
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content_md)

    return filepath, rel_path


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    args = sys.argv[1:]
    url = args[0]
    title_override = ''
    source_type_override = ''

    i = 1
    while i < len(args):
        if args[i] == '--type' and i + 1 < len(args):
            source_type_override = args[i + 1]
            i += 2
        else:
            title_override += (' ' if title_override else '') + args[i]
            i += 1

    source_type = source_type_override or detect_type(url)

    print(f"🌐 URL: {url}")
    print(f"📂 Tipo detectado: {source_type}")
    print(f"⏳ Descargando contenido...")

    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("❌ Timeout: la URL tardó más de 15 segundos en responder.")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"❌ Error HTTP {e.response.status_code}: {url}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'html.parser')

    title, author, date_published = extract_metadata(soup, url)
    if title_override:
        title = title_override

    content = extract_content(soup)

    if not content or len(content) < 100:
        print("⚠️  No se pudo extraer contenido suficiente de la URL.")
        print("   Posibles causas: contenido dinámico (JavaScript), paywall, o estructura no estándar.")
        print("   Alternativa: copiar manualmente el texto en sources/newsletters/ o sources/web/")
        sys.exit(1)

    print(f"✅ Contenido extraído")
    if title:
        print(f"📰 Título: {title}")
    if author:
        print(f"✍️  Autor: {author}")

    filepath, rel_path = save_source(url, title, author, date_published, content, source_type)

    words = len(content.split())
    print(f"💾 Guardado en: {rel_path}")
    print(f"📝 {words:,} palabras extraídas")
    print()
    print("─" * 60)
    print("SIGUIENTE PASO")
    print("─" * 60)
    print(f'Di a Claude: "Genera ángulos de contenido para')
    print(f'@autopromotorn a partir del archivo {rel_path}"')
    print("─" * 60)


if __name__ == '__main__':
    main()
