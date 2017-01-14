from django.conf import settings


# lazy init for translations
_ = lambda s: s


def pytest_addoption(parser):
    parser.addoption("--sync", nargs='?', default=False,
                     help="run sync tests (optionally can set the target to either prod, beta, or a URL)")
    parser.addoption("--sync-debug", action='store_true',
                     help="enable sync debug")
    parser.addoption("--sync-only", nargs='+',
                     help="sync only these comma separated tables")
    parser.addoption("--sync-id", help="sync only this id")


def pytest_configure():

    settings.configure(
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.admin',
            'django.contrib.sessions',
            'django_peeringdb',
        ],
        DATABASE_ENGINE='django.db.backends.sqlite3',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        DEBUG=False,
        TEMPLATE_DEBUG=True,
        LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {
                'stderr': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    },
            },
            'loggers': {
                '': {
                    'handlers': ['stderr'],
                    'level': 'DEBUG',
                    'propagate': False
                },
            },
        },

        USE_TZ=False,
        PEERINGDB_SYNC_STRIP_TZ=True,
        # add user defined iso code for Kosovo
        COUNTRIES_OVERRIDE = {
            'XK': _('Kosovo'),
        }
    )
