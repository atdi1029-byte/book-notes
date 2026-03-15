const fs = require('fs');

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .replace(/[-\s]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function convertInline(text) {
  // Bold: **text**
  text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  // Italic: *text*
  text = text.replace(/\*(.+?)\*/g, '<em>$1</em>');
  return text;
}

const notesPath = '/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/notes.md';
const summaryPath = '/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/summary.md';
const templatePath = '/Users/alexbarnett/Documents/Code/Claude/Books/template.html';
const outputPath = '/Users/alexbarnett/Documents/Code/Claude/Books/Bond_Markets_Analysis_and_Strategies/index.html';

// Read files
const notesContent = fs.readFileSync(notesPath, 'utf8');
const summaryContent = fs.readFileSync(summaryPath, 'utf8');
const templateContent = fs.readFileSync(templatePath, 'utf8');

// Process notes
const lines = notesContent.split('\n');
const htmlLines = [];
const tocEntries = [];

let inList = false;
let listItems = [];
let inBlockquote = false;
let blockquoteLines = [];
let inTable = false;
let tableLines = [];

for (let i = 0; i < lines.length; i++) {
  let line = lines[i].trimEnd();

  // Tables
  if (line.includes('|') && !inBlockquote) {
    if (!inTable) {
      inTable = true;
      tableLines = [];
    }
    tableLines.push(line);
    if (i + 1 >= lines.length || !lines[i + 1].includes('|')) {
      if (tableLines.length >= 2) {
        htmlLines.push('<table>');
        const headers = tableLines[0].split('|').slice(1, -1).map(h => h.trim());
        htmlLines.push('<thead><tr>');
        headers.forEach(h => htmlLines.push(`<th>${convertInline(h)}</th>`));
        htmlLines.push('</tr></thead><tbody>');
        for (let j = 2; j < tableLines.length; j++) {
          const cells = tableLines[j].split('|').slice(1, -1).map(c => c.trim());
          htmlLines.push('<tr>');
          cells.forEach(c => htmlLines.push(`<td>${convertInline(c)}</td>`));
          htmlLines.push('</tr>');
        }
        htmlLines.push('</tbody></table>');
      }
      inTable = false;
    }
    continue;
  }

  // Close list
  if (!line.startsWith('- ') && inList) {
    htmlLines.push('<ul>');
    listItems.forEach(item => htmlLines.push(`<li>${convertInline(item)}</li>`));
    htmlLines.push('</ul>');
    inList = false;
    listItems = [];
  }

  // Close blockquote
  if (!line.startsWith('> ') && inBlockquote) {
    htmlLines.push('<blockquote>');
    htmlLines.push(...blockquoteLines);
    htmlLines.push('</blockquote>');
    inBlockquote = false;
    blockquoteLines = [];
  }

  // H2
  if (line.startsWith('## ')) {
    const title = line.substring(3).trim();
    const slug = slugify(title);
    tocEntries.push({ slug, title });
    htmlLines.push('<hr>');
    htmlLines.push(`<h2 id="${slug}">${escapeHtml(title)}</h2>`);
  }
  // H3
  else if (line.startsWith('### ')) {
    const title = line.substring(4).trim();
    htmlLines.push(`<h3>${escapeHtml(title)}</h3>`);
  }
  // List
  else if (line.startsWith('- ')) {
    inList = true;
    listItems.push(line.substring(2).trim());
  }
  // Blockquote
  else if (line.startsWith('> ')) {
    inBlockquote = true;
    blockquoteLines.push(`<p>${convertInline(line.substring(2).trim())}</p>`);
  }
  // HR
  else if (line.trim() === '---') {
    // Skip
  }
  // Empty
  else if (!line.trim()) {
    // Skip
  }
  // Paragraph
  else {
    htmlLines.push(`<p>${convertInline(line)}</p>`);
  }
}

// Close remaining blocks
if (inList) {
  htmlLines.push('<ul>');
  listItems.forEach(item => htmlLines.push(`<li>${convertInline(item)}</li>`));
  htmlLines.push('</ul>');
}
if (inBlockquote) {
  htmlLines.push('<blockquote>');
  htmlLines.push(...blockquoteLines);
  htmlLines.push('</blockquote>');
}

const contentHtml = htmlLines.join('\n');

// Build TOC
const tocHtml = tocEntries
  .map(({ slug, title }) => `<li><a href="#${slug}">${escapeHtml(title)}</a></li>`)
  .join('\n');

// Extract takeaways
const summaryLines = summaryContent.split('\n');
const takeaways = [];
let inTakeaways = false;

for (const line of summaryLines) {
  const trimmed = line.trim();
  if (trimmed === '## Key Takeaways') {
    inTakeaways = true;
    continue;
  }
  if (inTakeaways) {
    if (trimmed.startsWith('## ') && !trimmed.includes('Key Takeaways')) {
      break;
    }
    const match = trimmed.match(/^\d+\.\s+\*\*(.+?)\*\*:\s+(.+)$/);
    if (match) {
      takeaways.push(`<li><strong>${match[1]}</strong>: ${match[2]}</li>`);
    }
  }
}

const takeawaysHtml = takeaways.join('\n');

// Replace placeholders
let output = templateContent
  .replace(/BOOK_TITLE/g, 'Bond Markets, Analysis, and Strategies')
  .replace(/BOOK_AUTHOR/g, 'Frank J. Fabozzi')
  .replace(/BOOK_YEAR/g, '2021')
  .replace(/BOOK_PAGES/g, '800+')
  .replace(/BOOK_KEY/g, 'bond_markets')
  .replace('<!-- TOC_ENTRIES -->', tocHtml)
  .replace('<!-- TAKEAWAYS -->', takeawaysHtml)
  .replace('<!-- CONTENT -->', contentHtml);

// Write output
fs.writeFileSync(outputPath, output, 'utf8');

console.log(`✓ Created index.html with ${tocEntries.length} sections and ${contentHtml.length.toLocaleString()} characters`);
