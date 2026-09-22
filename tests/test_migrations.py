import pytest
from django.core.management import call_command


@pytest.mark.django_db
def test_migrations_match_models():
    call_command(
        "makemigrations", "django_peeringdb", check=True, dry_run=True, verbosity=0
    )
