#!/usr/bin/env python3
"""
Convert Bond Markets notes.md to HTML using the template
"""

import re
import html

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def escape_html(text):
    """Escape HTML special characters"""
    return html.escape(text)

def convert_markdown_to_html(md_content):
    """Convert markdown content to HTML"""
    lines = md_content.split('\n')
    html_lines = []
    toc_entries = []

    in_list = False
    in_blockquote = False
    in_table = False
    list_items = []
    blockquote_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Handle tables
        if '|' in line and not in_blockquote:
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line)
            i += 1
            # Check if next line is separator or continues table
            if i < len(lines) and '|' not in lines[i]:
                # End of table
                html_lines.append(convert_table(table_lines))
                in_table = False
            continue

        # Close any open blocks
        if not line.startswith('- ') and in_list:
            html_lines.append('<ul>')
            html_lines.extend([f'<li>{convert_inline(item)}</li>' for item in list_items])
            html_lines.append('</ul>')
            in_list = False
            list_items = []

        if not line.startswith('> ') and in_blockquote:
            html_lines.append('<blockquote>')
            html_lines.extend(blockquote_lines)
            html_lines.append('</blockquote>')
            in_blockquote = False
            blockquote_lines = []

        # H2 headers with IDs and TOC
        if line.startswith('## '):
            title = line[3:].strip()
            slug = slugify(title)
            toc_entries.append((slug, title))
            html_lines.append('<hr>')
            html_lines.append(f'<h2 id="{slug}">{escape_html(title)}</h2>')

        # H3 headers
        elif line.startswith('### '):
            title = line[4:].strip()
            html_lines.append(f'<h3>{escape_html(title)}</h3>')

        # Bullet lists
        elif line.startswith('- '):
            in_list = True
            list_items.append(line[2:].strip())

        # Blockquotes
        elif line.startswith('> '):
            in_blockquote = True
            blockquote_lines.append(f'<p>{convert_inline(line[2:].strip())}</p>')

        # Horizontal rule
        elif line.strip() == '---':
            # Skip, we add them at h2 level
            pass

        # Empty lines
        elif not line.strip():
            if not in_list and not in_blockquote:
                # html_lines.append('')
                pass

        # Regular paragraphs
        else:
            html_lines.append(f'<p>{convert_inline(line)}</p>')

        i += 1

    # Close any remaining open blocks
    if in_list:
        html_lines.append('<ul>')
        html_lines.extend([f'<li>{convert_inline(item)}</li>' for item in list_items])
        html_lines.append('</ul>')

    if in_blockquote:
        html_lines.append('<blockquote>')
        html_lines.extend(blockquote_lines)
        html_lines.append('</blockquote>')

    return '\n'.join(html_lines), toc_entries

def convert_table(table_lines):
    """Convert markdown table to HTML"""
    if len(table_lines) < 2:
        return ''

    html = ['<table>']

    # Header row
    headers = [cell.strip() for cell in table_lines[0].split('|')[1:-1]]
    html.append('<thead><tr>')
    for header in headers:
        html.append(f'<th>{convert_inline(header)}</th>')
    html.append('</tr></thead>')

    # Skip separator line (index 1)
    # Data rows
    html.append('<tbody>')
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        html.append('<tr>')
        for cell in cells:
            html.append(f'<td>{convert_inline(cell)}</td>')
        html.append('</tr>')
    html.append('</tbody>')

    html.append('</table>')
    return '\n'.join(html)

def convert_inline(text):
    """Convert inline markdown (bold, italic, etc.)"""
    # Bold: **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic: *text*
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text

def extract_takeaways(summary_content):
    """Extract the 10 key takeaways from summary.md"""
    takeaways = []
    lines = summary_content.split('\n')

    in_takeaways = False
    for line in lines:
        if line.strip() == '## Key Takeaways':
            in_takeaways = True
            continue

        if in_takeaways:
            # Stop at next section
            if line.startswith('## ') and 'Key Takeaways' not in line:
                break

            # Match numbered items: "1. **Title**: Description"
            match = re.match(r'^\d+\.\s+\*\*(.+?)\*\*:\s+(.+)$', line)
            if match:
                title = match.group(1)
                desc = match.group(2)
                takeaways.append(f'<strong>{title}</strong>: {desc}')

    return takeaways

def main():
    # Read files
    with open('/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/summary.md', 'r') as f:
        summary = f.read()

    with open('/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/notes.md', 'r') as f:
        notes = f.read()

    with open('/Users/alexbarnett/Documents/Code/Claude/Books/template.html', 'r') as f:
        template = f.read()

    # Extract takeaways
    takeaways = extract_takeaways(summary)
    takeaways_html = '\n'.join([f'<li>{t}</li>' for t in takeaways])

    # Convert notes to HTML
    content_html, toc_entries = convert_markdown_to_html(notes)

    # Build TOC
    toc_html = '\n'.join([f'<li><a href="#{slug}">{escape_html(title)}</a></li>' for slug, title in toc_entries])

    # Replace placeholders
    output = template.replace('BOOK_TITLE', 'Bond Markets, Analysis, and Strategies')
    output = output.replace('BOOK_AUTHOR', 'Frank J. Fabozzi')
    output = output.replace('BOOK_YEAR', '2021')
    output = output.replace('BOOK_PAGES', '800+')
    output = output.replace('BOOK_KEY', 'bond_markets')
    output = output.replace('<!-- TOC_ENTRIES -->', toc_html)
    output = output.replace('<!-- TAKEAWAYS -->', takeaways_html)
    output = output.replace('<!-- CONTENT -->', content_html)

    # Write output
    with open('/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/index.html', 'w') as f:
        f.write(output)

    print(f"✓ Created index.html")
    print(f"  - {len(toc_entries)} sections")
    print(f"  - {len(takeaways)} key takeaways")
    print(f"  - {len(content_html)} characters of content")

if __name__ == '__main__':
    main()
