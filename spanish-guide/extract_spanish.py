#!/usr/bin/env python3
"""
Extract all Spanish words, phrases, and sentences from
the Spanish learning guide HTML file.
Output: one Spanish item per line, no duplicates, plain text.
"""

import re
from html.parser import HTMLParser
from collections import OrderedDict


def strip_html_tags(text):
    """Remove all HTML tags from text."""
    return re.sub(r'<[^>]+>', '', text)


class SpanishExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.results = OrderedDict()

        # State tracking
        self.in_es_td = False
        self.in_es_text = False
        self.in_conj_td = False
        self.in_pronoun_td = False
        self.current_text = ""
        self.conj_pronoun = ""
        self.conj_verb = ""
        self.tag_stack = []

        # Div nesting for conj-box tracking
        self.div_stack = []
        self.is_in_es_conj_box = False

        # Skip SVG/button content
        self.in_svg = False
        self.in_button = False

    def _update_conj_state(self):
        self.is_in_es_conj_box = False
        for entry in reversed(self.div_stack):
            if entry == 'es-conj-box':
                self.is_in_es_conj_box = True
                return
            if entry == 'pt-conj-box':
                return

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        cls = attrs_dict.get('class', '')

        if tag == 'svg':
            self.in_svg = True
            return
        if tag == 'button':
            self.in_button = True
            return

        if tag == 'div':
            if 'conj-box' in cls.split():
                self.div_stack.append('unknown-conj-box')
            else:
                self.div_stack.append('other')

        if tag == 'td' and 'es' in cls.split():
            self.in_es_td = True
            self.current_text = ""

        if tag == 'span' and 'es-text' in cls.split():
            self.in_es_text = True
            self.current_text = ""

        in_conj_box = any(
            e in ('unknown-conj-box', 'es-conj-box',
                  'pt-conj-box')
            for e in self.div_stack)
        if tag == 'h4' and in_conj_box:
            self.tag_stack.append('h4_conj_check')
            self.current_text = ""

        if tag == 'td' and self.is_in_es_conj_box:
            if 'pronoun' in cls.split():
                self.in_pronoun_td = True
                self.conj_pronoun = ""
            elif 'es' not in cls.split():
                self.in_conj_td = True
                self.conj_verb = ""

    def handle_endtag(self, tag):
        if tag == 'svg':
            self.in_svg = False
            return
        if tag == 'button':
            self.in_button = False
            return

        if tag == 'td' and self.in_es_td:
            self.in_es_td = False
            text = self.clean(self.current_text)
            if text:
                if '/' in text and len(text) < 40:
                    self.add(text)
                    for part in text.split('/'):
                        part = part.strip()
                        if part:
                            self.add(part)
                else:
                    self.add(text)
            self.current_text = ""

        if tag == 'span' and self.in_es_text:
            self.in_es_text = False
            text = self.clean(self.current_text)
            if text:
                self.add(text)
                if len(text) > 80:
                    sentences = re.split(
                        r'(?<=[.!?])\s+', text)
                    for s in sentences:
                        s = s.strip()
                        if s and len(s) > 3:
                            self.add(s)
            self.current_text = ""

        if tag == 'td' and self.in_pronoun_td:
            self.in_pronoun_td = False
            self.conj_pronoun = self.clean(
                self.conj_pronoun)

        if tag == 'td' and self.in_conj_td:
            self.in_conj_td = False
            verb = self.clean(self.conj_verb)
            if verb:
                self.add(verb)
                if self.conj_pronoun:
                    self.add(
                        f"{self.conj_pronoun} {verb}")
            self.conj_verb = ""

        if tag == 'div' and self.div_stack:
            self.div_stack.pop()
            self._update_conj_state()

        if (tag == 'h4' and self.tag_stack
                and self.tag_stack[-1] == 'h4_conj_check'):
            self.tag_stack.pop()
            text = self.clean(self.current_text)
            if text:
                low = text.lower()
                is_es = ('español' in low
                         or 'spanish' in low
                         or low.startswith('es ')
                         or low.startswith('es:'))
                is_pt = ('português' in low
                         or 'portuguese' in low
                         or low.startswith('pt ')
                         or low.startswith('pt:'))
                for i in range(
                        len(self.div_stack) - 1, -1, -1):
                    if self.div_stack[i] in (
                            'unknown-conj-box',
                            'es-conj-box',
                            'pt-conj-box'):
                        if is_es:
                            self.div_stack[i] = (
                                'es-conj-box')
                        elif is_pt:
                            self.div_stack[i] = (
                                'pt-conj-box')
                        break
                self._update_conj_state()
            self.current_text = ""

    def handle_data(self, data):
        if self.in_svg or self.in_button:
            return
        if self.in_es_td:
            self.current_text += data
        elif self.in_es_text:
            self.current_text += data
        elif self.in_pronoun_td:
            self.conj_pronoun += data
        elif self.in_conj_td:
            self.conj_verb += data
        elif (self.tag_stack
              and self.tag_stack[-1] == 'h4_conj_check'):
            self.current_text += data

    def clean(self, text):
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)
        text = text.strip('—– \t\n')
        return text

    def add(self, text):
        text = text.strip()
        if not text or len(text) < 1:
            return
        if len(text) == 1 and not text.isalpha():
            return
        if text.replace('.', '').replace(',', '').isdigit():
            return
        if text.startswith('<') or text.startswith('&'):
            return
        self.results[text] = True


def extract_conj_from_verb_tables(html):
    """
    Extract conjugated forms from verb tables where the
    first td has class="es" (infinitive) and subsequent
    plain <td> cells hold Spanish conjugated forms.

    Only operates on tables whose <th> headers indicate
    conjugation content (yo, tú, él, Yo Form, etc.)
    to avoid extracting English meaning columns from
    non-conjugation tables.
    """
    items = []

    # Find all <table> blocks
    table_pattern = re.compile(
        r'<table[^>]*>(.*?)</table>', re.DOTALL)

    conj_header_keywords = {
        'yo', 'tú', 'él', 'nosotros', 'ellos',
        'yo form', 'infinitive',
    }

    for table_match in table_pattern.finditer(html):
        table_content = table_match.group(1)

        # Check if this table has conjugation headers
        th_texts = re.findall(
            r'<th[^>]*>(.*?)</th>', table_content,
            re.DOTALL)
        th_texts_clean = [
            strip_html_tags(t).strip().lower()
            for t in th_texts]

        is_conj_table = any(
            kw in ' '.join(th_texts_clean)
            for kw in conj_header_keywords)

        if not is_conj_table:
            continue

        # Extract from rows in this conjugation table
        tr_pattern = re.compile(
            r'<tr>\s*(.*?)</tr>', re.DOTALL)

        for tr_match in tr_pattern.finditer(table_content):
            tr_content = tr_match.group(1)

            if 'class="es"' not in tr_content:
                continue

            td_pattern = re.compile(
                r'<td([^>]*)>(.*?)</td>', re.DOTALL)

            found_es = False
            for td_match in td_pattern.finditer(tr_content):
                td_attrs = td_match.group(1)
                td_content = td_match.group(2)

                is_es = 'class="es"' in td_attrs
                is_pt = 'class="pt"' in td_attrs
                is_en = 'class="en"' in td_attrs
                is_pronoun = 'class="pronoun"' in td_attrs

                if is_es:
                    found_es = True
                    continue
                if is_pt or is_en or is_pronoun:
                    continue

                if found_es:
                    text = strip_html_tags(
                        td_content).strip()
                    text = re.sub(r'\s+', ' ', text)
                    if text and len(text) > 0:
                        items.append(text)

    return items


def extract_speak_calls(html):
    items = []
    matches = re.findall(r"speak\('([^']+)'\)", html)
    for text in matches:
        text = text.strip()
        if text:
            items.append(text)
    return items


def clean_item(text):
    """
    Post-processing: clean up extracted items.
    """
    # Strip trailing parenthetical English notes
    text = re.sub(
        r'\s*\([^)]*(?:same|different|swap|spelling|'
        r'not |rude|informal|formal|literally|'
        r'Arg|Mex|can be|one word|throaty|silent|'
        r'pronounced|from )[^)]*\)',
        '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s*\(same!\)', '', text)
    text = re.sub(r'\s*\(different!\)', '', text)

    # Strip "→" annotations
    if '→' in text:
        parts = text.split('→')
        left = parts[0].strip()
        right = parts[1].strip() if len(parts) > 1 else ''
        if '"' in right or any(
                w in right.lower() for w in
                ['sound', 'silent', 'pronounced',
                 'throaty', 'khardín']):
            text = left
        elif right:
            return [left, right]
        else:
            text = left

    # Skip English descriptions
    english_patterns = [
        r'^"[^"]*"\s*sound',
        r'^"[^"]*"\s*or\s*"[^"]*"\s*sound',
        r'^often\s',
        r'^varies\s',
        r'^same\s+as\s',
        r'^like\s+[a-z]',
        r'^similar\s',
        r'^no\s+[a-z]',
        r'^not\s+[a-z]',
        r'^[a-z]+ = "[a-z]+"',
        r'^Infinitive$',
        r'^Person$',
        r'^Verb$',
        r'^Yo Form$',
        r'^PT ',
    ]
    for pat in english_patterns:
        if re.match(pat, text, re.IGNORECASE):
            return None

    # Skip table headers
    headers = {
        'Português', 'Español', 'English', 'Spanish',
        'Portuguese', 'Feature', 'Spain', 'Mexico',
        'Argentina', 'Latin America', 'Country', 'Slang',
        'Meaning', 'Pattern', 'Category', 'Region',
    }
    if text in headers:
        return None

    # Strip trailing "..."
    text = re.sub(r'\.\.\.$', '', text).strip()

    # Clean stray fragments
    text = re.sub(r'^\w+\)$', '', text).strip()

    if not text:
        return None

    return text


def main():
    input_path = (
        '/Users/alexbarnett/Documents/Code/Claude/Books/'
        'spanish-guide/index.html')
    output_path = (
        '/Users/alexbarnett/Documents/Code/Claude/Books/'
        'spanish-guide/spanish-export.txt')

    with open(input_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Phase 1: HTML parser
    extractor = SpanishExtractor()
    extractor.feed(html)

    # Phase 2: verb conjugation tables
    table_items = extract_conj_from_verb_tables(html)
    for item in table_items:
        extractor.add(item)

    # Phase 3: speak() calls
    speak_items = extract_speak_calls(html)
    for item in speak_items:
        extractor.add(item)

    # Phase 4: Post-process
    raw_items = list(extractor.results.keys())

    seen = set()
    final_items = []

    for item in raw_items:
        result = clean_item(item)
        if result is None:
            continue
        if isinstance(result, list):
            for r in result:
                r = r.strip()
                if r and r.lower() not in seen:
                    seen.add(r.lower())
                    final_items.append(r)
        else:
            result = result.strip()
            if result and result.lower() not in seen:
                seen.add(result.lower())
                final_items.append(result)

    # Phase 5: Final filter
    skip_exact = {
        'aña', 'ñ', 'j', 'll', 'ch', 'h-', 'ue', 'ie',
        'distinción)',
        'eu/yo', 'tu/tú', 'ele/él', 'nós/nos.',
        'eles/ellos',
    }

    filtered = []
    for item in final_items:
        if item in skip_exact:
            continue
        if re.match(r'^-[a-záéíóúñü]+$', item):
            continue
        if item.startswith('-') and '/' in item:
            continue
        if '=' in item and '"' in item:
            continue
        if len(item) <= 1 and not item.isalpha():
            continue
        filtered.append(item)

    with open(output_path, 'w', encoding='utf-8') as f:
        for item in filtered:
            f.write(item + '\n')

    print(f"Extracted {len(filtered)} Spanish items "
          f"to {output_path}")


if __name__ == '__main__':
    main()
