#!/usr/bin/env python3
import re

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def convert_markdown_to_html(md_file, output_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    html_lines = []
    in_list = False
    in_ordered_list = False
    in_blockquote = False
    skip_front_matter = True

    for line in lines:
        # Skip the very first header and front matter tables
        if line.startswith('# Bond Markets, Analysis, and Strategies'):
            skip_front_matter = True
            continue
        if skip_front_matter and line.strip().startswith('---'):
            skip_front_matter = False
            html_lines.append('<hr>\n')
            continue
        if skip_front_matter:
            continue

        # Close lists if needed
        if not line.strip().startswith('-') and in_list:
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
            # Apply bold
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            html_lines.append(f'{text}\n')
        # Convert ordered lists
        elif re.match(r'^\s*\d+\.', line):
            if not in_ordered_list:
                html_lines.append('<ol>\n')
                in_ordered_list = True
            text = re.sub(r'^\s*\d+\.\s*', '', line).strip()
            # Apply bold
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            html_lines.append(f'<li>{text}</li>\n')
        # Convert unordered lists
        elif line.strip().startswith('- '):
            if not in_list:
                html_lines.append('<ul>\n')
                in_list = True
            text = line.strip()[2:]
            # Apply bold
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            html_lines.append(f'<li>{text}</li>\n')
        # Convert horizontal rules
        elif line.strip() == '---':
            html_lines.append('<hr>\n')
        # Convert tables (skip for now)
        elif line.strip().startswith('|'):
            continue
        # Regular paragraphs
        elif line.strip():
            text = line.strip()
            # Apply bold
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            html_lines.append(f'<p>{text}</p>\n')
        else:
            # Empty line - add minimal spacing
            pass

    # Close any open lists
    if in_list:
        html_lines.append('</ul>\n')
    if in_ordered_list:
        html_lines.append('</ol>\n')
    if in_blockquote:
        html_lines.append('</blockquote>\n')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(html_lines))

    print(f"Converted {len(lines)} lines to HTML. Output saved to {output_file}")

if __name__ == '__main__':
    convert_markdown_to_html(
        '/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/notes.md',
        '/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/content_temp.html'
    )
