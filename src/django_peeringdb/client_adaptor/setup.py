from django import setup
from django.conf import global_settings, settings

from django_peeringdb import default_settings


# default_settings must define _all_ defaults, so we have to extract and combine
# everything from global_settings and django_peeringdb's defaults.
# https://docs.djangoproject.com/en/dev/topics/settings/#custom-default-settings
class _Settings:
    def __init__(self):
        self.__dict__ = {}

    def update(self, new):
        for name in dir(new):
            if name.isupper():
                self.__dict__[name] = getattr(new, name)


def configure(**kwargs):
    if settings.configured:
        return

    defaults = _Settings()
    defaults.update(global_settings)
    defaults.update(default_settings)
    settings.configure(default_settings=defaults, **kwargs)
    setup()
