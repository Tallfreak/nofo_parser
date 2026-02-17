"""File system infrastructure - operations for file downloads and NOFO processing."""

import os
from pathlib import Path
from typing import Any

import httpx

import nofo_parser
from file_processing import pdf_from_downloaded_path
from logger import logger


def download_nofo(
    pdf_url: str,
    download_dir: str,
) -> tuple[dict | None, str | None]:
    """Download NOFO document from PA Gov.

    Args:
        pdf_url: URL of the PDF document
        download_dir: Directory to save downloaded files

    Returns:
        Tuple of (file_data dict, filename) or (None, None) on error
    """
    logger.info('downloading NOFO document', url=pdf_url, format='PDF')
    try:
        with httpx.Client(follow_redirects=True, timeout=30.0) as client:
            response = client.get(pdf_url)
            response.raise_for_status()

            # Extract filename from Content-Disposition header or URL
            nofo_file_name = 'program-guidelines.pdf'
            if 'content-disposition' in response.headers:
                content_disp = response.headers['content-disposition']
                if 'filename=' in content_disp:
                    nofo_file_name = content_disp.split('filename=')[-1].strip('"\'')

            if nofo_file_name == 'program-guidelines.pdf':
                # Try to extract from URL path
                url_path = pdf_url.split('/')[-2] if '/download/' in pdf_url else 'program-guidelines'
                nofo_file_name = f'{url_path}.pdf'

            # Save to temp file
            temp_path = os.path.join(download_dir, nofo_file_name)
            Path(temp_path).write_bytes(response.content)

            logger.info('PDF downloaded successfully', file_name=nofo_file_name, size=len(response.content))

            # Process the downloaded PDF
            pdf_bytes, _ = pdf_from_downloaded_path(temp_path)
            file_data = {'type': 'pdf', 'data': pdf_bytes, 'path': temp_path}

            return file_data, nofo_file_name

    except Exception as e:
        logger.error('failed to download PDF', url=pdf_url, error=str(e))
        return None, None


def s3_upload(
    file_data: dict,
    nofo_file_name: str,
    pdf_url: str,
) -> str | None:
    """Upload NOFO to S3 (wrapper for shared utility).

    Args:
        file_data: Dictionary with 'type', 'data', 'path' keys
        nofo_file_name: Name of the NOFO file
        pdf_url: Original PDF URL (for logging)

    Returns:
        S3 key if successful, None otherwise
    """
    return nofo_parser.upload_nofo_to_s3(file_data, nofo_file_name, pdf_url)


def vector_upload(
    file_data: dict,
    nofo_file_name: str,
    grant_general_data: dict,
    nofo_info: dict,
    nofo_txt_pdf_obj: Any,
    s3_key: str,
    pdf_path: str,
) -> bool:
    """Add NOFO to vector store with metadata (wrapper for shared utility).

    This also updates the grants table with openai_file_id and s3_key.

    Args:
        conn: Database connection
        grant_id: Grant database ID
        file_data: Dictionary with 'type', 'data', 'path' keys
        nofo_file_name: Name of the NOFO file
        grant_general_data: Grant general data for metadata
        nofo_info: Parsed NOFO information
        nofo_txt_pdf_obj: PDF object for vector store
        s3_key: S3 key where file was uploaded
        pdf_url: Original PDF URL (for logging)

    Returns:
        True if successful, False otherwise
    """
    return nofo_parser.add_nofo_to_vector_store_with_metadata(
        file_data,
        nofo_file_name,
        grant_general_data,
        nofo_info,
        nofo_txt_pdf_obj,
        s3_key,
        pdf_path,
    )
