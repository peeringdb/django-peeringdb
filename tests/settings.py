# Minimal Django settings for mypy
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django_peeringdb",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

SECRET_KEY = "s3cr3t"
USE_TZ = True
TABLE_PREFIX = "peeringdb_"
ABSTRACT_ONLY = False
