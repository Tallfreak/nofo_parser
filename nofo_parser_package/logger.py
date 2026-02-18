import json
import os
import sys
import traceback

from loguru import logger

logger.remove()

# Use colors locally, plain JSON in production (Heroku)
is_production = os.getenv('DYNO')


def serialize(record):
    subset = {'level': record['level'].name, 'message': record['message']}
    # Merge extra fields directly into the top-level dict
    if record['extra']:
        subset.update(record['extra'])

    if record['exception']:
        exc = record['exception']
        subset['exception'] = {
            'type': exc.type.__name__,
            'value': str(exc.value),
            'traceback': traceback.format_exception(exc.type, exc.value, exc.traceback),
        }

    return json.dumps(subset, ensure_ascii=False)


def patching(record):
    record['serialized'] = serialize(record)


logger = logger.patch(patching)

if is_production:
    logger.add(sys.stderr, format='{serialized}', colorize=False, level='INFO')
else:
    logger.add(sys.stderr, format='<level>{serialized}</level>', colorize=True, level='DEBUG')
