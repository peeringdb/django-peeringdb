# lazy init for translations
_ = lambda s: s

TABLE_PREFIX = "peeringdb_"
ABSTRACT_ONLY = False

DEBUG = False
TEMPLATE_DEBUG = True

INSTALLED_APPS = [
    "django_peeringdb",
]
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"dev_warnings": {}},
    "handlers": {
        "stderr": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "filters": ["dev_warnings"],
        },
    },
    "loggers": {
        "": {"handlers": ["stderr"], "level": "DEBUG", "propagate": False},
    },
}
USE_TZ = False
TIME_ZONE = "UTC"
# add user defined iso code for Kosovo
COUNTRIES_OVERRIDE = {
    "XK": _("Kosovo"),
}
