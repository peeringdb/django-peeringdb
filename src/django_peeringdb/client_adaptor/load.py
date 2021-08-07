DJANGO_DB_FIELDS = (
    "ENGINE",
    "NAME",
    "HOST",
    "PORT",
    "USER",
    "PASSWORD",
)


def database_settings(db_config):
    db = {}
    for k, v in list(db_config.items()):
        k = k.upper()
        if k in DJANGO_DB_FIELDS:
            db[k] = v

    db["ENGINE"] = "django.db.backends." + db["ENGINE"]
    return db


__backend = None


def load_backend(**orm_config):
    """
    Load the client adaptor module of django_peeringdb
    Assumes config is valid.
    """
    settings = {}
    settings["SECRET_KEY"] = orm_config.get("secret_key", "")

    db_config = orm_config["database"]
    if db_config:
        settings["DATABASES"] = {"default": database_settings(db_config)}

    from django_peeringdb.client_adaptor.setup import configure

    # Override defaults
    configure(**settings)
    # Must import implementation module after configure
    from django_peeringdb.client_adaptor import backend

    migrate = orm_config.get("migrate")
    if migrate and not backend.Backend().is_database_migrated():
        backend.Backend().migrate_database()

    return backend
