#!/usr/bin/env python3
import re

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

def process_markdown_to_html(md_file):
    """Process markdown file and convert to HTML"""
    html_parts = []
    toc_entries = []

    with open(md_file, 'r') as f:
        lines = f.readlines()

    in_blockquote = False
    in_list = False
    list_type = None
    in_table = False
    table_lines = []

    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')

        # Handle H2 headers (## )
        if line.startswith('## ') and not line.startswith('###'):
            # Close any open tags
            if in_blockquote:
                html_parts.append('</blockquote>')
                in_blockquote = False
            if in_list:
                html_parts.append(f'</{list_type}>')
                in_list = False
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
                table_lines = []

            # Add hr before new section (except first one)
            if html_parts and html_parts[-1] != '<hr>':
                html_parts.append('<hr>')

            title = line[3:].strip()
            slug = slugify(title)
            html_parts.append(f'<h2 id="{slug}">{title}</h2>')
            toc_entries.append((title, slug))

        # Handle H3 headers (###)
        elif line.startswith('### '):
            if in_blockquote:
                html_parts.append('</blockquote>')
                in_blockquote = False
            if in_list:
                html_parts.append(f'</{list_type}>')
                in_list = False
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
                table_lines = []

            title = line[4:].strip()
            html_parts.append(f'<h3>{title}</h3>')

        # Handle blockquotes
        elif line.startswith('> '):
            if not in_blockquote:
                if in_list:
                    html_parts.append(f'</{list_type}>')
                    in_list = False
                html_parts.append('<blockquote>')
                in_blockquote = True

            content = line[2:].strip()
            # Apply bold formatting
            content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
            html_parts.append(f'<p>{content}</p>')

        # Handle tables
        elif '|' in line and line.strip().startswith('|'):
            if not in_table:
                if in_list:
                    html_parts.append(f'</{list_type}>')
                    in_list = False
                if in_blockquote:
                    html_parts.append('</blockquote>')
                    in_blockquote = False
                in_table = True
                table_lines = []

            table_lines.append(line)

            # Check if next line is separator or end of table
            if i + 1 >= len(lines) or '|' not in lines[i + 1]:
                # Process complete table
                if len(table_lines) > 0:
                    html_parts.append('<table>')
                    for j, tline in enumerate(table_lines):
                        if '|---' in tline or '|--' in tline:
                            continue  # Skip separator line

                        cells = [c.strip() for c in tline.split('|')[1:-1]]

                        if j == 0 or (j == 1 and len(table_lines) > 1 and '|---' in table_lines[1]):
                            # Header row
                            html_parts.append('<thead><tr>')
                            for cell in cells:
                                cell = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', cell)
                                html_parts.append(f'<th>{cell}</th>')
                            html_parts.append('</tr></thead><tbody>')
                        else:
                            # Data row
                            html_parts.append('<tr>')
                            for cell in cells:
                                cell = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', cell)
                                html_parts.append(f'<td>{cell}</td>')
                            html_parts.append('</tr>')

                    html_parts.append('</tbody></table>')
                in_table = False
                table_lines = []

        # Handle unordered lists
        elif line.startswith('- '):
            if in_blockquote:
                html_parts.append('</blockquote>')
                in_blockquote = False

            if not in_list or list_type != 'ul':
                if in_list:
                    html_parts.append(f'</{list_type}>')
                html_parts.append('<ul>')
                in_list = True
                list_type = 'ul'

            content = line[2:].strip()
            # Apply bold formatting
            content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
            html_parts.append(f'<li>{content}</li>')

        # Handle ordered lists
        elif re.match(r'^\d+\.\s+', line):
            if in_blockquote:
                html_parts.append('</blockquote>')
                in_blockquote = False

            if not in_list or list_type != 'ol':
                if in_list:
                    html_parts.append(f'</{list_type}>')
                html_parts.append('<ol>')
                in_list = True
                list_type = 'ol'

            content = re.sub(r'^\d+\.\s+', '', line).strip()
            # Apply bold formatting
            content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
            html_parts.append(f'<li>{content}</li>')

        # Handle empty lines
        elif line.strip() == '':
            if in_blockquote:
                html_parts.append('</blockquote>')
                in_blockquote = False
            if in_list:
                html_parts.append(f'</{list_type}>')
                in_list = False

        # Handle regular paragraphs
        elif line.strip() and not line.startswith('#') and not line.startswith('---') and not line.startswith('<!--'):
            if in_list:
                html_parts.append(f'</{list_type}>')
                in_list = False
            if in_blockquote:
                html_parts.append('</blockquote>')
                in_blockquote = False

            content = line.strip()
            # Apply bold formatting
            content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
            html_parts.append(f'<p>{content}</p>')

        i += 1

    # Close any remaining open tags
    if in_blockquote:
        html_parts.append('</blockquote>')
    if in_list:
        html_parts.append(f'</{list_type}>')
    if in_table:
        html_parts.append('</tbody></table>')

    return html_parts, toc_entries

def extract_takeaways(summary_file):
    """Extract key takeaways from summary.md"""
    with open(summary_file, 'r') as f:
        content = f.read()

    takeaway_pattern = r'^\d+\.\s+\*\*(.+?)\*\*:(.+?)(?=\n\d+\.\s+\*\*|\n\n##|\Z)'
    takeaways = re.findall(takeaway_pattern, content, re.MULTILINE | re.DOTALL)

    takeaways_html = []
    for i, (title, content) in enumerate(takeaways[:15], 1):  # Limit to first 15
        content_clean = content.strip()
        takeaways_html.append(f'  <li><strong>{title}</strong>: {content_clean}</li>')

    return takeaways_html

def main():
    # Paths
    base_dir = '/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies'
    template_path = '/Users/alexbarnett/Documents/Code/Claude/Books/template.html'
    summary_path = f'{base_dir}/summary.md'
    notes_path = f'{base_dir}/notes.md'
    output_path = f'{base_dir}/index.html'

    print("Extracting takeaways from summary...")
    takeaways_html = extract_takeaways(summary_path)
    print(f"  Found {len(takeaways_html)} takeaways")

    print("Processing notes.md to HTML...")
    html_parts, toc_entries = process_markdown_to_html(notes_path)
    print(f"  Processed {len(html_parts)} HTML elements")
    print(f"  Found {len(toc_entries)} H2 sections")

    # Build TOC HTML
    toc_html = []
    for title, slug in toc_entries:
        toc_html.append(f'    <li><a href="#{slug}">{title}</a></li>')

    # Read template
    print("Reading template...")
    with open(template_path, 'r') as f:
        template = f.read()

    # Replace placeholders
    print("Building final HTML...")
    html = template.replace('BOOK_TITLE', 'Bond Markets, Analysis, and Strategies')
    html = html.replace('BOOK_AUTHOR', 'Frank J. Fabozzi and Francesco A. Fabozzi')
    html = html.replace('BOOK_YEAR', '2021')
    html = html.replace('BOOK_PAGES', '800+')
    html = html.replace('BOOK_KEY', 'bond_markets')
    html = html.replace('<!-- TAKEAWAYS -->', '\n'.join(takeaways_html))
    html = html.replace('    <!-- TOC_ENTRIES -->', '\n'.join(toc_html))

    # Insert content HTML
    content_html = '\n'.join(html_parts)
    html = html.replace('<!-- CONTENT -->', content_html)

    # Write output
    print(f"Writing to {output_path}...")
    with open(output_path, 'w') as f:
        f.write(html)

    print(f"\nSuccess!")
    print(f"  Output file: {output_path}")
    print(f"  Total size: {len(html):,} characters")
    print(f"  TOC entries: {len(toc_entries)}")
    print(f"  Key takeaways: {len(takeaways_html)}")

if __name__ == '__main__':
    main()
