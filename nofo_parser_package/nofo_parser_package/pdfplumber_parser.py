import pdfplumber


def in_any_bbox(word, bboxes):
    word_top = word['top']
    word_bottom = word['bottom']
    for top, bottom in bboxes:
        if word_top >= top and word_bottom <= bottom:
            return True
    return False


def group_words_by_line(words, y_tolerance=3):
    lines = []
    current_line = []
    current_y = None

    for word in sorted(words, key=lambda w: (w['top'], w['x0'])):
        if current_y is None or abs(word['top'] - current_y) > y_tolerance:
            if current_line:
                lines.append(current_line)
            current_line = [word]
            current_y = word['top']
        else:
            current_line.append(word)
    if current_line:
        lines.append(current_line)
    return lines


def pdfplumber_extract_text_from_pdf(pdf_fileobj):
    all_text = ''
    with pdfplumber.open(pdf_fileobj) as pdf:
        for idx, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ''
            if text:
                # Add page number as the header
                all_text += f'--- PDF Page {idx} ---\n'

                # Find tables in a page (if any)
                table_objs = page.find_tables()
                table_blocks = []
                for i, table_obj in enumerate(table_objs, start=1):
                    bbox = table_obj.bbox
                    rows = table_obj.extract()
                    table_blocks.append({'type': 'table', 'top': bbox[1], 'bottom': bbox[3], 'content': rows, 'index': i})

                # Exclude content outside of tables
                words = page.extract_words()
                non_table_content = [w for w in words if not in_any_bbox(w, ([t['top'], t['bottom']] for t in table_blocks))]

                # Group non-table content into text blocks
                text_blocks = []
                lines = group_words_by_line(non_table_content)
                for line in lines:
                    top = min(word['top'] for word in line)
                    bottom = max(word['bottom'] for word in line)
                    text = ' '.join(word['text'] for word in line)
                    text_blocks.append({'type': 'text', 'top': top, 'bottom': bottom, 'content': text})

                # Merge and sort all blocks by vertical position
                all_blocks = text_blocks + table_blocks
                all_blocks.sort(key=lambda b: b['top'])

                # Render content in order
                for block in all_blocks:
                    if block['type'] == 'text':
                        all_text += block['content'] + '\n'
                    elif block['type'] == 'table':
                        all_text += f'[Start Table {block["index"]}]\n'
                        for row in block['content']:
                            all_text += '\t'.join(cell or '' for cell in row) + '\n'
                        all_text += f'[End Table {block["index"]}]\n'

                all_text += '\n'
    return all_text
