from django.conf import settings as __settings

# import to namespace
from django_peeringdb.models.abstract import *  # noqa

if not __settings.ABSTRACT_ONLY:
    # import to namespace
    from django_peeringdb.models.concrete import *  # noqa

del __settings
