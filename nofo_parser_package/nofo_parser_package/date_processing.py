import re
from datetime import datetime


def to_iso(mdy: str | None):
    if not mdy:
        return None
    if isinstance(mdy, datetime):
        return mdy.isoformat()
    return datetime.strptime(mdy, '%m/%d/%Y').date().isoformat()  # 'YYYY-MM-DD'


def parse_grants_dt(s: str, tz_offsets):
    if not s:
        return None
    s = re.sub(r'\s+', ' ', s).strip()
    m = re.search(r' ([A-Z]{3})$', s)
    if m and m.group(1) in tz_offsets:
        # Replace TZ abbr with numeric offset and parse with %z
        s_num = s[:-3] + tz_offsets[m.group(1)]
        try:
            return datetime.strptime(s_num, '%b %d, %Y %I:%M:%S %p %z')
        except ValueError:
            pass
    # Fallback: no timezone (naive)
    try:
        return datetime.strptime(s, '%b %d, %Y %I:%M:%S %p')
    except ValueError:
        return None


def parse_dt(x):
    if not x:
        return None
    # handle common ISO formats
    try:
        return datetime.fromisoformat(x.replace('Z', '+00:00'))
    except Exception:
        # fall back to plain date
        try:
            return datetime.strptime(x, '%Y-%m-%d')
        except Exception:
            return None
