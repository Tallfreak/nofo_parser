
import tempfile
import os

from .logger import logger
from . import file_processing
from . import nofo_parsing
from . import file_system
from .grant import Grant
from .lifecycle import GrantStatus

def parse(pdf_path: str):
    try:
        S3_BUCKET_NAME_get_environ = os.environ.get('S3_BUCKET_NAME')
        logger.info('S3_BUCKET_NAME_get_environ', S3_BUCKET_NAME_get_environ)
        S3_BUCKET_NAME_environ = os.environ['S3_BUCKET_NAME']
        logger.info('S3_BUCKET_NAME_environ', S3_BUCKET_NAME_environ)
        S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
        logger.info('S3_BUCKET_NAME', S3_BUCKET_NAME)

        
        logger.info('processing NOFO document', url=pdf_path)

        grant_dict = Grant('', '', '', '', '', GrantStatus.POSTED, '').__dict__
        # Use temporary directory with automatic cleanup
        with tempfile.TemporaryDirectory() as download_dir:
            # Step 1: Download NOFO
            pdf_bytes, _ = file_processing.pdf_from_downloaded_path(pdf_path)
            file_data = {'type': 'pdf', 'data': pdf_bytes, 'path': pdf_path}
            nofo_file_name = pdf_path.split('\\')[-1]

            #Step 2: Parse NOFO
            nofo_info, nofo_txt_pdf_obj = nofo_parsing.parse(file_data, nofo_file_name, grant_dict)
            if not nofo_info or not nofo_txt_pdf_obj:
                logger.warning('failed to parse NOFO document', url=pdf_path)

            # Step 3: Upload to S3
            s3_key = file_system.s3_upload(file_data, nofo_file_name, pdf_path)
            if not s3_key:
                logger.warning('failed to upload NOFO to S3', url=pdf_path)

            # Step 4: Add to vector store
            vector_success = file_system.vector_upload(
                file_data,
                nofo_file_name,
                grant_dict,
                nofo_info,
                nofo_txt_pdf_obj,
                s3_key,
                pdf_path=pdf_path,
            )

            if vector_success:
                return nofo_info
            else:
                logger.warning('failed to add NOFO to vector store', url=pdf_path)

    except Exception as e:
        logger.error('failed to enrich grant with NOFO', url=pdf_path, error=str(e))
