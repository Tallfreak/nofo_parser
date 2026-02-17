"""NOFO parsing infrastructure - pure parsing operations without database writes.

This module extracts NOFO data using OpenAI but does not perform any database
operations. Database writes are handled by the processor layer.
"""

import io
from typing import Any

from openai_parser import parse_nofo_with_openai
from logger import logger


def parse(
    file_data: dict,
    nofo_file_name: str,
    grant_data: dict,
) -> tuple[dict | None, Any]:
    """Parse NOFO document using OpenAI (pure parsing, no database writes).

    Args:
        file_data: Dictionary with 'type' ('pdf', 'docx', 'html') and 'data' keys
        nofo_file_name: Name of the NOFO file
        grant_data: Grant general data for context during parsing

    Returns:
        Tuple of (parsed_nofo_info, nofo_txt_pdf_obj) or (None, None) on error
    """
    try:
        nofo_filetype = file_data['type']

        if file_data['type'] == 'pdf':
            nofo_info, nofo_txt_pdf_obj = parse_nofo_with_openai(
                io.BytesIO(file_data['data']),
                nofo_file_name,
                nofo_filetype,
                grant_data,
            )
        else:  # docx or html
            nofo_info, nofo_txt_pdf_obj = parse_nofo_with_openai(
                file_data['data'],
                nofo_file_name,
                nofo_filetype,
                grant_data,
            )

        if nofo_info is None:
            logger.error('OpenAI parsing returned no data', filename=nofo_file_name)
            return None, None

        logger.info('Successfully parsed NOFO', filename=nofo_file_name)
        return nofo_info, nofo_txt_pdf_obj

    except Exception:
        logger.exception('Unexpected error parsing NOFO', filename=nofo_file_name)
        return None, None
