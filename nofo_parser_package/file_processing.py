import binascii
import glob
import io
import os
import re
import shutil
import tempfile
import zipfile
from io import BytesIO
from typing import Iterable, Optional, Tuple

import docx2txt
from bs4 import BeautifulSoup, Comment
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas

from .logger import logger

# File type magic numbers
ZIP_MAGIC_NUMBERS = (b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08')
PDF_MAGIC_NUMBER = b'%PDF-'
HTML_PATTERNS = (b'<!doctype html', b'<html', b'<head', b'<body')


def delete_temp_nofo_directories(directories: list[str]) -> None:
    """
    Delete a temporary NOFO directory and all its contents.

    Args:
        directory: Path to the directory to delete
    """
    for directory in directories:
        if os.path.exists(directory):
            try:
                shutil.rmtree(directory)
            except Exception:
                logger.exception('Error deleting temp nofo directory', nofo_obj=None)


def delete_temp_nofo_files_in_directory(download_dir):
    """
    Remove files in a directory

    Args:
        download_dir: Path to the directory
    """
    try:
        # Find and delete the downloaded file
        pattern = os.path.join(download_dir, '*')
        files = glob.glob(pattern)
        for file_path in files:
            if os.path.isfile(file_path):
                os.remove(file_path)
                logger.debug(f'Deleted processed file: {file_path}')
    except Exception as e:
        logger.warning(f'Failed to delete downloaded file: {e}')


def _magic_kind(head: bytes) -> str:
    # Print first up-to-32 bytes as hex for diagnostics
    logger.debug(f'[magic] first {len(head)} bytes: {binascii.hexlify(head[:32]).decode("ascii")}')

    if any(head.startswith(magic) for magic in ZIP_MAGIC_NUMBERS):
        logger.debug('[magic] -> zip')
        return 'zip'
    if head.startswith(PDF_MAGIC_NUMBER):
        logger.debug('[magic] -> pdf')
        return 'pdf'

    h = head.lstrip().lower()
    if any(h.startswith(pattern) for pattern in HTML_PATTERNS):
        logger.debug('[magic] -> html')
        return 'html'

    logger.debug('[magic] -> unknown')
    return 'unknown'


def extract_first_pdf_from_zip_bytes(raw: bytes) -> Tuple[bytes, str]:
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        names = z.namelist()
        logger.debug(f'[zip->pdf] entries: {names[:10]}{" ..." if len(names) > 10 else ""}')
        pdf_infos = [i for i in z.infolist() if not i.is_dir() and i.filename.lower().endswith('.pdf')]
        if not pdf_infos:
            raise FileNotFoundError('ZIP contains no PDF.')
        info = pdf_infos[0]
        logger.debug(f'[zip->pdf] chosen: {info.filename} ({info.file_size} bytes)')
        with z.open(info, 'r') as f:
            pdf_bytes = f.read()
        pdf_name = os.path.basename(info.filename) or 'document.pdf'
        return pdf_bytes, pdf_name


def pdf_from_downloaded_path(path: str) -> Tuple[bytes, str]:
    """
    Extract PDF data from a downloaded file, handling ZIP and unkown files if needed.

    Args:
        path: Path to the downloaded file

    Returns:
        Tuple of (PDF bytes, PDF filename)
    """
    size = os.path.getsize(path)
    ext = os.path.splitext(path)[1].lower()
    logger.debug(f'[pdf] path={path}, size={size}, ext={ext}')

    with open(path, 'rb') as f:
        head = f.read(8)
    kind = _magic_kind(head)

    try:
        if kind == 'pdf':
            with open(path, 'rb') as f:
                data = f.read()
            name = os.path.basename(path)
            if not name.lower().endswith('.pdf'):
                base, _ = os.path.splitext(name)
                name = f'{base}.pdf'
            logger.debug(f'[pdf] direct pdf -> {name}')
            return data, name

        if kind == 'zip' or path.lower().endswith('.zip'):
            with open(path, 'rb') as f:
                raw = f.read()
            data, name = extract_first_pdf_from_zip_bytes(raw)
            logger.debug(f'[pdf] zip-contained pdf -> {name}')
            return data, name

        # Fallback
        with open(path, 'rb') as f:
            data = f.read()
        name = os.path.basename(path)
        if not name.lower().endswith('.pdf'):
            base, _ = os.path.splitext(name)
            name = f'{base}.pdf'
        logger.debug(f'[pdf] fallback as pdf -> {name}')
        return data, name

    except Exception as e:
        logger.debug(f'[pdf][ERROR] {type(e).__name__}: {e}')
        raise


def _zip_has_docx_package(z: zipfile.ZipFile) -> bool:
    """
    Returns True if this ZIP looks like a .docx package itself
    (OpenXML structure), not just a zip containing arbitrary files.
    """
    names = set(i.filename for i in z.infolist())
    return ('[Content_Types].xml' in names) and any(n.startswith('word/') for n in names)


def _pick_docx_entry(entries: Iterable[zipfile.ZipInfo], strategy: str = 'largest') -> Optional[zipfile.ZipInfo]:
    """
    From a set of ZIP entries, pick a .docx file to extract.
    strategy='largest' (default) picks the largest by file size,
    otherwise 'first' picks the first encountered.
    """
    docx_entries = [e for e in entries if not e.is_dir() and e.filename.lower().endswith('.docx')]
    if not docx_entries:
        return None
    if strategy == 'largest':
        docx_entries.sort(key=lambda e: e.file_size, reverse=True)
    return docx_entries[0]


def extract_first_docx_from_zip_bytes(raw: bytes, pick_strategy: str = 'largest') -> Tuple[bytes, str]:
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        names = z.namelist()
        logger.debug(f'[zip->docx] entries: {names[:10]}{" ..." if len(names) > 10 else ""}')

        if _zip_has_docx_package(z):
            logger.debug('[zip->docx] zip IS a .docx package')
            data = io.BytesIO()
            with zipfile.ZipFile(data, mode='w') as outzip:
                for info in z.infolist():
                    with z.open(info, 'r') as src:
                        outzip.writestr(info, src.read())
            return data.getvalue(), 'document.docx'

        info = _pick_docx_entry(z.infolist(), strategy=pick_strategy)
        if info is None:
            raise FileNotFoundError('ZIP contains no .docx file.')
        logger.debug(f'[zip->docx] chosen: {info.filename} ({info.file_size} bytes)')
        with z.open(info, 'r') as f:
            docx_bytes = f.read()
        name = os.path.basename(info.filename) or 'document.docx'
        return docx_bytes, name


def docx_text_from_downloaded_path(path: str, image_dir: Optional[str] = None) -> Tuple[str, str]:
    """
    Extract text content from a DOCX file, handling ZIP archives if needed.

    Args:
        path: Path to the downloaded file
        image_dir: Optional directory to extract images to

    Returns:
        Tuple of (extracted text, DOCX filename)
    """
    size = os.path.getsize(path)
    ext = os.path.splitext(path)[1].lower()
    logger.debug(f'[docx] path={path}, size={size}, ext={ext}')

    with open(path, 'rb') as f:
        head = f.read(8)
    kind = _magic_kind(head)

    try:
        if kind == 'zip':
            with open(path, 'rb') as f:
                raw = f.read()
            try:
                with zipfile.ZipFile(io.BytesIO(raw)) as z:
                    if _zip_has_docx_package(z):
                        logger.debug('[docx] path is a docx package (zip)')
                        docx_bytes = raw
                        docx_name = os.path.basename(path)
                        if not docx_name.lower().endswith('.docx'):
                            base, _ = os.path.splitext(docx_name)
                            docx_name = f'{base}.docx'
                    else:
                        logger.debug('[docx] zip with inner docx')
                        docx_bytes, docx_name = extract_first_docx_from_zip_bytes(raw)
            except zipfile.BadZipFile:
                logger.debug('[docx] BadZipFile -> treat as raw docx bytes')
                docx_bytes = raw
                docx_name = os.path.basename(path)
                if not docx_name.lower().endswith('.docx'):
                    base, _ = os.path.splitext(docx_name)
                    docx_name = f'{base}.docx'
        else:
            with open(path, 'rb') as f:
                docx_bytes = f.read()
            docx_name = os.path.basename(path)
            if not docx_name.lower().endswith('.docx'):
                base, _ = os.path.splitext(docx_name)
                docx_name = f'{base}.docx'

        with tempfile.TemporaryDirectory() as td:
            docx_path = os.path.join(td, docx_name)
            with open(docx_path, 'wb') as out:
                out.write(docx_bytes)
            text = docx2txt.process(docx_path, image_dir) if image_dir else docx2txt.process(docx_path)
            logger.debug(f'[docx] parsed -> inner_name={docx_name}, text_len={len(text or "")}')
            return (text or ''), docx_name

    except Exception as e:
        logger.debug(f'[docx][ERROR] {type(e).__name__}: {e}')
        raise


def _pick_html_entry(entries: Iterable[zipfile.ZipInfo]) -> Optional[zipfile.ZipInfo]:
    """
    Choose an HTML file from a ZIP:
      1) Prefer index.html / index.htm (common site entry)
      2) Otherwise choose the largest *.html|*.htm
    """
    files = [e for e in entries if not e.is_dir()]
    htmls = [e for e in files if e.filename.lower().endswith(('.html', '.htm'))]
    if not htmls:
        return None

    # Prefer index.* (common landing file)
    for e in htmls:
        base = os.path.basename(e.filename).lower()
        if base in ('index.html', 'index.htm'):
            return e

    # Fallback: largest HTML file (often the main one)
    htmls.sort(key=lambda e: e.file_size, reverse=True)
    return htmls[0]


def extract_first_html_from_zip_bytes(raw: bytes) -> Tuple[bytes, str]:
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        names = z.namelist()
        logger.debug(f'[zip->html] entries: {names[:10]}{" ..." if len(names) > 10 else ""}')
        info = _pick_html_entry(z.infolist())
        if info is None:
            raise FileNotFoundError('ZIP contains no HTML (.html/.htm) files.')
        logger.debug(f'[zip->html] chosen: {info.filename} ({info.file_size} bytes)')
        with z.open(info, 'r') as f:
            html_bytes = f.read()
        name = os.path.basename(info.filename) or 'index.html'
        return html_bytes, name


def _html_bytes_to_text(html_bytes: bytes) -> str:
    try:
        soup = BeautifulSoup(html_bytes, 'lxml')
    except Exception:
        soup = BeautifulSoup(html_bytes, 'html.parser')

    for tag in soup(['script', 'style', 'noscript', 'template']):
        tag.decompose()

    # Proper comment removal
    for c in soup.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()

    text = soup.get_text(separator='\n', strip=True)
    text = re.sub(r'\n\s*\n+', '\n\n', text).strip()
    return text


def html_text_from_downloaded_path(path: str) -> Tuple[str, str]:
    """Extract text content from an HTML file, handling ZIP archives if needed.

    Args:
        path: Path to the downloaded file

    Returns:
        Tuple of (extracted text, HTML filename)

    Raises:
        FileNotFoundError: If no HTML is found in a ZIP archive
    """
    size = os.path.getsize(path)
    ext = os.path.splitext(path)[1].lower()
    logger.debug(f'[html] path={path}, size={size}, ext={ext}')

    with open(path, 'rb') as f:
        head = f.read(1024)
    kind = _magic_kind(head[:8])

    try:
        if kind == 'zip' or path.lower().endswith('.zip'):
            with open(path, 'rb') as f:
                raw = f.read()
            html_bytes, inner_name = extract_first_html_from_zip_bytes(raw)
            text = _html_bytes_to_text(html_bytes)
            logger.debug(f'[html] zip-contained html -> {inner_name}, text_len={len(text)}')
            return text, inner_name

        with open(path, 'rb') as f:
            html_bytes = f.read()
        html_name = os.path.basename(path)
        if not html_name.lower().endswith(('.html', '.htm')):
            base, _ = os.path.splitext(html_name)
            html_name = f'{base}.html'
        text = _html_bytes_to_text(html_bytes)
        logger.debug(f'[html] direct html -> {html_name}, text_len={len(text)}')
        return text, html_name

    except Exception as e:
        logger.debug(f'[html][ERROR] {type(e).__name__}: {e}')
        raise


def strip_html_tags(text: str) -> str:
    """Remove HTML tags from the given text string."""
    clean = re.sub(r'<.*?>', '', text)  # remove all tags
    return clean.strip()


def text_to_pdf_bytes(
    text: str,
    pagesize=LETTER,
    font_name='Helvetica',  # try "Courier" if you want fixed-width for table alignment
    font_size=10,
    margin=40,
    leading=None,  # line spacing; defaults to 1.2 * font_size
    tabsize=4,
    # font_path=None,        # Optional: path to a TTF for wide Unicode coverage (see note)
):
    """
    Convert plain text into a PDF and return the raw PDF bytes.
    """
    # If you want full Unicode support, register a TTF:
    # if font_path:
    #     pdfmetrics.registerFont(TTFont("CustomTTF", font_path))
    #     font_name = "CustomTTF"

    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=pagesize)
    width, height = pagesize
    y = height - margin
    leading = leading or int(font_size * 1.2)
    usable_width = width - 2 * margin

    c.setFont(font_name, font_size)

    # Draw text line-by-line, wrapping to the available width.
    for raw_line in text.splitlines():
        # Expand tabs so “tables” (with \t) are readable in the PDF
        raw_line = raw_line.expandtabs(tabsize)

        # Wrap this line to fit within usable width
        wrapped_lines = simpleSplit(raw_line, font_name, font_size, usable_width)
        if not wrapped_lines:
            wrapped_lines = ['']

        for line in wrapped_lines:
            if y < margin:
                c.showPage()
                c.setFont(font_name, font_size)
                y = height - margin
            c.drawString(margin, y, line)
            y -= leading

    c.save()
    return buf.getvalue()


def is_html_redirect(html_bytes):
    html_lower = html_bytes.lower()

    # Check for meta refresh (more flexible)
    if b'http-equiv' in html_lower and b'refresh' in html_lower:
        return True

    return False
