from django.conf import settings

# we only set up admin views if concrete models are available

if not settings.ABSTRACT_ONLY:
    from django_peeringdb.admin.views import *  # noqa
