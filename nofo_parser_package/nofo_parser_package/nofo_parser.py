import io
import os

import boto3
from botocore.exceptions import ClientError

from .openai_parser import add_nofo_to_vector_store
from .date_processing import to_iso
from .logger import logger

S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_ENDPOINT_URL = os.getenv('AWS_ENDPOINT_URL') or None
s3_client = boto3.client('s3', endpoint_url=AWS_ENDPOINT_URL)

def upload_nofo_to_s3(file_data, nofo_file_name, latest_link_text):
    """Upload NOFO file to S3 bucket."""
    s3_key = f'uploads/{nofo_file_name}'

    try:
        if file_data['type'] == 'pdf':
            s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=s3_key, Body=file_data['data'], ContentType='application/pdf')
        else:  # docx or html
            s3_client.upload_file(Bucket=S3_BUCKET_NAME, Key=s3_key, Filename=file_data['path'])

        logger.info('Successfully uploaded to s3', filename=latest_link_text, s3_bucket_name=S3_BUCKET_NAME, s3_key=s3_key)
        return s3_key
    except ClientError as e:
        error_code = e.response.get('Error', {}).get('Code', 'Unknown')
        logger.exception('s3 upload failed due to AWS error', error_code=error_code, filename=latest_link_text, s3_key=s3_key)
        return None
    except Exception:
        logger.exception('Failure to upload to s3', filename=latest_link_text, s3_bucket_name=S3_BUCKET_NAME, s3_key=s3_key)
        return None

def add_nofo_to_vector_store_with_metadata(file_data, nofo_file_name, nofo_general_data, nofo_info, nofo_txt_pdf_obj, s3_key, latest_link_text):
    """Add NOFO to vector store with metadata and update database."""
    try:
        # Build metadata
        nofo_metadata = {}
        if nofo_general_data.get('posted_date'):
            nofo_metadata['posted_date'] = to_iso(nofo_general_data.get('posted_date'))
        if nofo_general_data.get('close_date'):
            nofo_metadata['close_date'] = to_iso(nofo_general_data.get('close_date'))
        if nofo_info['award_ceiling']['award_ceiling_int'] and isinstance(nofo_info['award_ceiling']['award_ceiling_int'], int):
            nofo_metadata['award_ceiling_int'] = nofo_info['award_ceiling']['award_ceiling_int']
        if isinstance(nofo_info['match_requirements']['requires_match'], bool):
            nofo_metadata['requires_match'] = nofo_info['match_requirements']['requires_match']

        # Add to vector store
        if file_data['type'] == 'pdf':
            openai_file_id = add_nofo_to_vector_store(io.BytesIO(file_data['data']), nofo_file_name, nofo_metadata)
        else:
            openai_file_id = add_nofo_to_vector_store(nofo_txt_pdf_obj, nofo_file_name, nofo_metadata)

        logger.info('Successfully added to vector store', filename=latest_link_text)
        
        return True
    except Exception:
        logger.exception('Failed to add to vector store', filename=latest_link_text)
        return False