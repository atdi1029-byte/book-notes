#!/usr/bin/env python3
"""Build index.html for Bond Markets book from markdown notes"""

import re

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def extract_takeaways(summary_file):
    """Extract key takeaways from summary.md"""
    with open(summary_file, 'r') as f:
        content = f.read()

    # Find the Key Takeaways section
    match = re.search(r'## Key Takeaways\n(.*?)##', content, re.DOTALL)
    if not match:
        return []

    takeaways_text = match.group(1)
    # Extract numbered items
    takeaways = []
    for line in takeaways_text.split('\n'):
        if re.match(r'^\d+\.', line):
            # Remove the number and extract the content
            takeaway = re.sub(r'^\d+\.\s*', '', line).strip()
            takeaways.append(takeaway)

    return takeaways

def convert_md_to_html(md_file):
    """Convert markdown notes to HTML"""
    with open(md_file, 'r') as f:
        lines = f.readlines()

    html_lines = []
    toc_entries = []
    in_list = False
    in_ordered_list = False
    in_blockquote = False
    skip_until_hr = True

    for line in lines:
        # Skip front matter until first ---
        if skip_until_hr:
            if line.strip() == '---':
                skip_until_hr = False
                html_lines.append('<hr>\n')
            continue

        # Close lists/blockquotes when necessary
        if not line.strip().startswith('-') and not line.strip().startswith('  -') and in_list:
            html_lines.append('</ul>\n')
            in_list = False
        if not re.match(r'^\s*\d+\.', line) and in_ordered_list:
            html_lines.append('</ol>\n')
            in_ordered_list = False
        if not line.strip().startswith('>') and in_blockquote:
            html_lines.append('</blockquote>\n')
            in_blockquote = False

        # Convert headers
        if line.startswith('## '):
            text = line[3:].strip()
            slug = slugify(text)
            html_lines.append(f'<h2 id="{slug}">{text}</h2>\n')
            toc_entries.append((slug, text))
        elif line.startswith('### '):
            text = line[4:].strip()
            html_lines.append(f'<h3>{text}</h3>\n')
        elif line.startswith('#### '):
            text = line[5:].strip()
            html_lines.append(f'<h4>{text}</h4>\n')
        # Convert blockquotes
        elif line.strip().startswith('>'):
            if not in_blockquote:
                html_lines.append('<blockquote>\n')
                in_blockquote = True
            text = line.strip()[1:].strip()
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            html_lines.append(f'{text}\n')
        # Convert ordered lists
        elif re.match(r'^\s*\d+\.', line):
            if not in_ordered_list:
                html_lines.append('<ol>\n')
                in_ordered_list = True
            text = re.sub(r'^\s*\d+\.\s*', '', line).strip()
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            html_lines.append(f'<li>{text}</li>\n')
        # Convert unordered lists
        elif line.strip().startswith('- '):
            if not in_list:
                html_lines.append('<ul>\n')
                in_list = True
            text = line.strip()[2:]
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            html_lines.append(f'<li>{text}</li>\n')
        # Convert horizontal rules
        elif line.strip() == '---':
            html_lines.append('<hr>\n')
        # Skip tables
        elif line.strip().startswith('|'):
            continue
        # Regular paragraphs
        elif line.strip():
            text = line.strip()
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            html_lines.append(f'<p>{text}</p>\n')

    # Close any open lists/blockquotes
    if in_list:
        html_lines.append('</ul>\n')
    if in_ordered_list:
        html_lines.append('</ol>\n')
    if in_blockquote:
        html_lines.append('</blockquote>\n')

    return ''.join(html_lines), toc_entries

def build_html():
    """Build the complete index.html file"""
    print("Building index.html...")

    # Extract takeaways
    print("Extracting takeaways...")
    takeaways = extract_takeaways('summary.md')
    takeaways_html = '\n'.join([f'<li>{t}</li>' for t in takeaways])

    # Convert markdown to HTML
    print("Converting notes.md to HTML...")
    content_html, toc_entries = convert_md_to_html('notes.md')

    # Build TOC
    print(f"Building TOC with {len(toc_entries)} entries...")
    toc_html = '\n'.join([f'<li><a href="#{slug}">{title}</a></li>' for slug, title in toc_entries])

    # Read template
    print("Reading template...")
    with open('../template.html', 'r') as f:
        template = f.read()

    # Replace placeholders
    print("Replacing placeholders...")
    html = template
    html = html.replace('BOOK_TITLE', 'Bond Markets, Analysis, and Strategies')
    html = html.replace('BOOK_AUTHOR', 'Frank J. Fabozzi and Francesco A. Fabozzi')
    html = html.replace('BOOK_YEAR', '2021')
    html = html.replace('BOOK_PAGES', '928')
    html = html.replace('BOOK_KEY', 'bond_markets_analysis_and_strategies')
    html = html.replace('<!-- TOC_ENTRIES -->', toc_html)
    html = html.replace('<!-- TAKEAWAYS -->', takeaways_html)
    html = html.replace('<!-- CONTENT -->', content_html)

    # Write output
    print("Writing index.html...")
    with open('index.html', 'w') as f:
        f.write(html)

    print(f"Done! Created index.html with {len(html)} characters")
    print(f"  - {len(takeaways)} takeaways")
    print(f"  - {len(toc_entries)} TOC entries")

if __name__ == '__main__':
    build_html()
