import re
import html

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def convert_inline(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text

# Read notes
with open('/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/notes.md', 'r') as f:
    lines = f.readlines()

html_lines = []
toc_entries = []
in_list = False
list_items = []
in_blockquote = False
blockquote_lines = []
in_table = False
table_lines = []

for i, line in enumerate(lines):
    line = line.rstrip('\n')

    # Tables
    if '|' in line and not in_blockquote:
        if not in_table:
            in_table = True
            table_lines = []
        table_lines.append(line)
        if i + 1 >= len(lines) or '|' not in lines[i + 1]:
            if len(table_lines) >= 2:
                html_lines.append('<table>')
                headers = [cell.strip() for cell in table_lines[0].split('|')[1:-1]]
                html_lines.append('<thead><tr>')
                for h in headers:
                    html_lines.append(f'<th>{convert_inline(h)}</th>')
                html_lines.append('</tr></thead><tbody>')
                for row in table_lines[2:]:
                    cells = [cell.strip() for cell in row.split('|')[1:-1]]
                    html_lines.append('<tr>')
                    for c in cells:
                        html_lines.append(f'<td>{convert_inline(c)}</td>')
                    html_lines.append('</tr>')
                html_lines.append('</tbody></table>')
            in_table = False
        continue

    # Close list
    if not line.startswith('- ') and in_list:
        html_lines.append('<ul>')
        for item in list_items:
            html_lines.append(f'<li>{convert_inline(item)}</li>')
        html_lines.append('</ul>')
        in_list = False
        list_items = []

    # Close blockquote
    if not line.startswith('> ') and in_blockquote:
        html_lines.append('<blockquote>')
        html_lines.extend(blockquote_lines)
        html_lines.append('</blockquote>')
        in_blockquote = False
        blockquote_lines = []

    # H2
    if line.startswith('## '):
        title = line[3:].strip()
        slug = slugify(title)
        toc_entries.append((slug, title))
        html_lines.append('<hr>')
        html_lines.append(f'<h2 id="{slug}">{html.escape(title)}</h2>')
    # H3
    elif line.startswith('### '):
        title = line[4:].strip()
        html_lines.append(f'<h3>{html.escape(title)}</h3>')
    # List
    elif line.startswith('- '):
        in_list = True
        list_items.append(line[2:].strip())
    # Blockquote
    elif line.startswith('> '):
        in_blockquote = True
        blockquote_lines.append(f'<p>{convert_inline(line[2:].strip())}</p>')
    # HR
    elif line.strip() == '---':
        pass
    # Empty
    elif not line.strip():
        pass
    # Paragraph
    else:
        html_lines.append(f'<p>{convert_inline(line)}</p>')

# Close remaining
if in_list:
    html_lines.append('<ul>')
    for item in list_items:
        html_lines.append(f'<li>{convert_inline(item)}</li>')
    html_lines.append('</ul>')
if in_blockquote:
    html_lines.append('<blockquote>')
    html_lines.extend(blockquote_lines)
    html_lines.append('</blockquote>')

content_html = '\n'.join(html_lines)

# TOC
toc_html = '\n'.join([f'<li><a href="#{slug}">{html.escape(title)}</a></li>' for slug, title in toc_entries])

# Takeaways
with open('/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/summary.md', 'r') as f:
    summary_lines = f.readlines()

takeaways = []
in_section = False
for line in summary_lines:
    line = line.strip()
    if line == '## Key Takeaways':
        in_section = True
        continue
    if in_section:
        if line.startswith('## ') and 'Key Takeaways' not in line:
            break
        match = re.match(r'^\d+\.\s+\*\*(.+?)\*\*:\s+(.+)$', line)
        if match:
            takeaways.append(f'<li><strong>{match.group(1)}</strong>: {match.group(2)}</li>')

takeaways_html = '\n'.join(takeaways)

# Template
with open('/Users/alexbarnett/Documents/Code/Claude/Books/template.html', 'r') as f:
    template = f.read()

output = template.replace('BOOK_TITLE', 'Bond Markets, Analysis, and Strategies')
output = output.replace('BOOK_AUTHOR', 'Frank J. Fabozzi')
output = output.replace('BOOK_YEAR', '2021')
output = output.replace('BOOK_PAGES', '800+')
output = output.replace('BOOK_KEY', 'bond_markets')
output = output.replace('<!-- TOC_ENTRIES -->', toc_html)
output = output.replace('<!-- TAKEAWAYS -->', takeaways_html)
output = output.replace('<!-- CONTENT -->', content_html)

with open('/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/index.html', 'w') as f:
    f.write(output)

print(f"✓ Created index.html with {len(toc_entries)} sections and {len(content_html):,} chars")
