
from django.conf import settings


TABLE_PREFIX = getattr(settings, 'PEERINGDB_TABLE_PREFIX', 'peeringdb_')
ABSTRACT_ONLY = getattr(settings, 'PEERINGDB_ABSTRACT_ONLY', False)

SYNC_URL = getattr(settings, 'PEERINGDB_SYNC_URL', 'https://www.peeringdb.com/api')
SYNC_USERNAME = getattr(settings, 'PEERINGDB_SYNC_USERNAME', '')
SYNC_PASSWORD = getattr(settings, 'PEERINGDB_SYNC_PASSWORD', '')

SYNC_STRIP_TZ = getattr(settings, 'PEERINGDB_SYNC_STRIP_TZ', False)
SYNC_ONLY = getattr(settings, 'PEERINGDB_SYNC_ONLY', [])

if isinstance(SYNC_ONLY, basestring):
    raise ValueError("SYNC_ONLY should be iterable (list, tuple, etc)")


