
from django_peeringdb.models.abstract import *

from django_peeringdb import settings as __settings

if not __settings.ABSTRACT_ONLY:
    from django_peeringdb.models.concrete import *

del __settings
