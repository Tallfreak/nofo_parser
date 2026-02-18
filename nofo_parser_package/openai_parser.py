import json
import os
from io import BytesIO

import openai
from dotenv import load_dotenv

from . import award_ceiling
from . import contact_info
from . import eligibility_booleans
from . import eligibility_requirements
from . import eligible_activities
from . import indirect_costs
from . import key_dates
from . import keywords
from . import match_requirements
from . import performance_start_date
from . import scoring_rubric
from . import summary
from . import unique_aspects
from .pdfplumber_parser import pdfplumber_extract_text_from_pdf
from .file_processing import text_to_pdf_bytes
from .logger import logger

load_dotenv()

prompt_objects = [
    {'prompt': summary.prompt, 'field_name': 'summary'},
    {'prompt': key_dates.prompt, 'field_name': 'key_dates'},
    {'prompt': award_ceiling.prompt, 'field_name': 'award_ceiling'},
    {'prompt': unique_aspects.prompt, 'field_name': 'unique_aspects'},
    {'prompt': indirect_costs.prompt, 'field_name': 'indirect_costs'},
    {'prompt': eligibility_requirements.prompt, 'field_name': 'eligibility_requirements'},
    {'prompt': eligibility_booleans.prompt, 'field_name': 'eligibility_booleans'},
    {'prompt': match_requirements.prompt, 'field_name': 'match_requirements'},
    {'prompt': scoring_rubric.prompt, 'field_name': 'scoring_rubric'},
    {'prompt': eligible_activities.prompt, 'field_name': 'eligible_activities'},
    {'prompt': performance_start_date.prompt, 'field_name': 'performance_start_date'},
    {'prompt': keywords.prompt, 'field_name': 'keywords'},
]

# OpenAI configuration
OPENAI_VECTOR_STORE_ID = os.environ.get('OPENAI_VECTOR_STORE_ID')


def get_openai_client():
    """Lazily initialize OpenAI client to avoid import-time initialization errors."""
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise ValueError('OPENAI_API_KEY environment variable is not set')
    return openai.OpenAI(api_key=api_key)


def extract_nofo_information(file_id, prompt_object):
    """Ask the assistant to extract information from a specific file"""
    logger.debug('Extracting field from nofo', field_name=prompt_object['field_name'])

    response = get_openai_client().responses.create(
        model='gpt-4.1',
        input=[
            {
                'role': 'user',
                'content': [
                    {'type': 'input_file', 'file_id': file_id},
                    {'type': 'input_text', 'text': prompt_object['prompt']},
                ],
            }
        ],
        temperature=0.01,
        # top_p=0.5,
        text={'format': {'type': 'json_object'}},
    )

    # need to experiment with output_text vs output content text
    # eventually return message as json instead of text
    if response.status == 'completed' and response.output is not None:
        return json.loads(response.output_text)
    else:
        logger.warning(
            'OpenAI response not completed or empty output',
            response_status=response.status,
            field_name=prompt_object['field_name'],
        )
        return


def extract_keywords_from_description(description):
    logger.debug('Extracting keywords from description')
    response = get_openai_client().responses.create(
        model='gpt-4.1',
        input=[
            {
                'role': 'user',
                'content': [
                    {'type': 'input_text', 'text': keywords.no_nofo_prompt},
                    {'type': 'input_text', 'text': description},
                ],
            }
        ],
        temperature=0.01,
        text={'format': {'type': 'json_object'}},
    )
    if response.status == 'completed' and response.output is not None:
        return json.loads(response.output_text)
    else:
        logger.warning('OpenAI keyword extraction not completed or empty output', response_status=response.status)
        return


def parse_nofo_with_openai(nofo_bytes_or_txt, nofo_name, nofo_filetype, grant_data):
    result = {}
    file_id = None
    try:
        # For webpage PDFs, use them directly without extraction/re-conversion (this is bc pdfplumber can't handle them)
        if nofo_filetype == 'webpage':
            logger.debug('Using webpage PDF directly without text extraction', filename=nofo_name)
            nofo_txt_pdf_obj = nofo_bytes_or_txt
            # Ensure it's seeked to the beginning
            if isinstance(nofo_txt_pdf_obj, BytesIO):
                nofo_txt_pdf_obj.seek(0)
        # For regular PDFs, extract text and convert back to PDF
        elif nofo_filetype == 'pdf':
            nofo_txt = pdfplumber_extract_text_from_pdf(nofo_bytes_or_txt)
            nofo_txt_pdf_obj = BytesIO(text_to_pdf_bytes(nofo_txt))
        # For other file types (docx, html, etc.), convert to text then to PDF
        else:
            if isinstance(nofo_bytes_or_txt, BytesIO):
                nofo_bytes_or_txt.seek(0)
                nofo_txt = nofo_bytes_or_txt.read().decode('utf-8', errors='replace')
            elif isinstance(nofo_bytes_or_txt, bytes):
                nofo_txt = nofo_bytes_or_txt.decode('utf-8', errors='replace')
            else:
                nofo_txt = nofo_bytes_or_txt  # Already a string
            nofo_txt_pdf_obj = BytesIO(text_to_pdf_bytes(nofo_txt))

        # give stream a file name for open ai upload
        if not getattr(nofo_txt_pdf_obj, 'name', None):
            if nofo_name.lower().endswith('.pdf'):
                nofo_txt_pdf_obj.name = nofo_name
            else:
                base, _ = os.path.splitext(nofo_name)
                nofo_txt_pdf_obj.name = f'{base}.pdf'
        nofo_txt_pdf_obj.seek(0)

        # upload as file attachment
        logger.info('Uploading file to OpenAI', filename=nofo_name)
        file = get_openai_client().files.create(file=nofo_txt_pdf_obj, purpose='assistants')
        file_id = file.id

        # loop through each piece of information and store it on a results object
        logger.info('Extracting information from nofo with OpenAI', filename=nofo_name)

        # parse contact info from nofo if not available through scraping
        prompt_objects_to_use = prompt_objects.copy()
        if not grant_data.get('agency_contact_email') and not grant_data.get('agency_contact_phone'):
            prompt_objects_to_use.append({'prompt': contact_info.prompt, 'field_name': 'contact_info'})

        for prompt_object in prompt_objects_to_use:
            # Extract information
            nofo_info = extract_nofo_information(file_id, prompt_object)
            # Store the result
            if nofo_info:
                result[prompt_object['field_name']] = nofo_info[prompt_object['field_name']]

        # Delete file when done
        get_openai_client().files.delete(file_id)

    except Exception:
        logger.exception('Unexpected error processing nofo', nofo_name=nofo_name)
        if file_id:
            try:
                get_openai_client().files.delete(file_id)
            except Exception:
                logger.exception('Failed to cleanup OpenAI file', file_id=file_id)
        return None, None

    return result, nofo_txt_pdf_obj


def add_nofo_to_vector_store(nofo_obj, nofo_name, metadata):
    if not getattr(nofo_obj, 'name', None):
        nofo_obj.name = nofo_name if nofo_name.lower().endswith('.pdf') else f'{nofo_name}.pdf'
    nofo_obj.seek(0)
    try:
        f = get_openai_client().files.create(file=nofo_obj, purpose='assistants')
        get_openai_client().vector_stores.files.create(vector_store_id=OPENAI_VECTOR_STORE_ID, file_id=f.id, attributes=metadata)

        logger.info('Added nofo to vector store', nofo_name=nofo_name, file_id=f.id)
        return f.id
    except Exception:
        logger.exception('Unexpected error adding nofo to vector store', nofo_name=nofo_name)
        return False
