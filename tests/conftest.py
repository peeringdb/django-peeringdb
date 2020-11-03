from django_peeringdb.client_adaptor import setup


def pytest_configure():
    setup.configure(
        DATABASE_ENGINE="django.db.backends.sqlite3",
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        PEERINGDB_SYNC_STRIP_TZ=True,
        SECRET_KEY="s3cr3t",
    )
