import re

def slugify(text):
    """Convert header text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def extract_toc(filepath):
    """Extract table of contents from h2 headers"""
    toc_items = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('## '):
                header_text = line[3:].strip()
                # Skip reference sections
                if header_text in ['Allegories & Cultural References', 'Books & Thinkers Referenced']:
                    continue
                slug = slugify(header_text)
                toc_items.append(f'<li><a href="#{slug}">{header_text}</a></li>')

    return '\n'.join(toc_items)

# Generate TOC
toc_html = extract_toc('/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/notes.md')
print(toc_html)
