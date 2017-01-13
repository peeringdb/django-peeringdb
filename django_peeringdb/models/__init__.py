
# import to namespace
from django_peeringdb.models.abstract import * # noqa

from django_peeringdb import settings as __settings

if not __settings.ABSTRACT_ONLY:
    # import to namespace
    from django_peeringdb.models.concrete import * # noqa

del __settings
