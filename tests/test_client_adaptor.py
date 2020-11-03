import sys
import datetime
from collections import defaultdict
from decimal import Decimal

import pytest
import calendar

from django.db import IntegrityError
from django.db.transaction import atomic as atomic_transaction
import django.core.exceptions

import tests.peeringdb_mock

sys.modules["peeringdb"] = sys.modules["tests.peeringdb_mock"]


import django_peeringdb.models as models

from django_peeringdb.client_adaptor.load import database_settings

from django_peeringdb.client_adaptor.backend import Backend


def test_database_settings():
    db_config = database_settings(
        {
            "engine": "sqlite",
            "name": "test.sqlite3",
            "host": "localhost",
            "port": 1234,
            "user": "test_user",
            "password": "test_password",
            "drop": "this",
        }
    )

    expected = {
        "ENGINE": "django.db.backends.sqlite",
        "NAME": "test.sqlite3",
        "HOST": "localhost",
        "PORT": 1234,
        "USER": "test_user",
        "PASSWORD": "test_password",
    }

    assert db_config == expected


def test_backend_setup():
    Backend.setup()
    for model in models.all_models:
        for field in model._meta.fields:
            if field.name in ["created", "updated"]:
                assert field.auto_now_add == False
                assert field.auto_now == False


def test_atomic_transaction():
    assert isinstance(Backend.atomic_transaction(), type(atomic_transaction()))


def test_validation_error():
    assert Backend.validation_error() == django.core.exceptions.ValidationError


def test_object_missing_error():
    assert Backend.object_missing_error() == django.core.exceptions.ObjectDoesNotExist
    assert (
        Backend.object_missing_error(models.Organization)
        == models.Organization.DoesNotExist
    )


@pytest.mark.django_db
def test_last_change(db):
    backend = Backend()
    now = datetime.datetime.now()
    now_t = int(calendar.timegm(now.timetuple()))
    models.Organization.objects.create(name="Test org", created=now, updated=now)
    assert backend.last_change(models.Organization) == now_t
    assert backend.last_change(models.Network) == 0


@pytest.mark.django_db
def test_get_object(db):
    backend = Backend()
    now = datetime.datetime.now()
    org = models.Organization.objects.create(name="Test org", created=now, updated=now)
    assert backend.get_object(models.Organization, org.id) == org


@pytest.mark.django_db
def test_get_objects(db):
    backend = Backend()
    now = datetime.datetime.now()
    orgs = []
    for i in range(0, 4):
        orgs.append(
            models.Organization.objects.create(
                name=f"Test org {i}", created=now, updated=now
            )
        )
    assert [o for o in backend.get_objects(models.Organization, [1, 2])] == orgs[:2]
    assert [o for o in backend.get_objects(models.Organization)] == orgs


@pytest.mark.django_db
def test_get_object_by(db):
    backend = Backend()
    now = datetime.datetime.now()
    org = models.Organization.objects.create(name="Test org", created=now, updated=now)
    assert backend.get_object_by(models.Organization, "name", "Test org") == org


@pytest.mark.django_db
def test_get_objects_by(db):
    backend = Backend()
    now = datetime.datetime.now()
    orgs = []
    for i in range(0, 4):
        orgs.append(
            models.Organization.objects.create(
                name=f"Test org {i}", created=now, updated=now
            )
        )
    assert [
        o for o in backend.get_objects_by(models.Organization, "name", "Test org 0")
    ] == orgs[:1]
    assert [
        o for o in backend.get_objects_by(models.Organization, "name", "Test org x")
    ] == []


@pytest.mark.django_db
def test_create_object(db):
    backend = Backend()
    now = datetime.datetime.now()
    org = backend.create_object(
        models.Organization, name="Test org", created=now, updated=now
    )
    assert org.id == 1
    assert org.name == "Test org"


@pytest.mark.django_db
def test_get_fields(db):
    backend = Backend()
    fields = backend.get_fields(models.Organization)
    assert fields == models.Organization._meta.get_fields()


@pytest.mark.django_db
def test_get_field(db):
    backend = Backend()
    field = backend.get_field(models.Organization, "name")
    assert field == models.Organization._meta.get_field("name")


@pytest.mark.django_db
def test_get_field_concrete(db):
    backend = Backend()
    related_model = backend.get_field_concrete(models.Network, "org")
    assert related_model == models.Organization


@pytest.mark.django_db
def test_is_field_related(db):
    backend = Backend()
    related_model = backend.get_field_concrete(models.Network, "org")
    assert related_model == models.Organization


@pytest.mark.django_db
def test_set_relation_many_to_many(db):
    backend = Backend()
    now = datetime.datetime.now()
    org = backend.create_object(
        models.Organization, name="Test org", created=now, updated=now
    )
    org2 = backend.create_object(
        models.Organization, name="Test org 2", created=now, updated=now
    )
    nets = [
        models.Network.objects.create(
            asn=i, name=f"Net {i}", created=now, updated=now, org=org
        )
        for i in range(1, 4)
    ]
    backend.set_relation_many_to_many(org2, "net_set", nets)

    assert [n for n in org2.net_set.all()] == nets


@pytest.mark.django_db
def test_clean(db):
    backend = Backend()
    net = models.Network()
    with pytest.raises(Backend.validation_error()):
        backend.clean(net)


@pytest.mark.django_db
def test_save(db):
    backend = Backend()
    now = datetime.datetime.now()
    org = models.Organization(name="Test org", created=now, updated=now)
    backend.save(org)
    assert org.id == 1


def test_convert_field():
    backend = Backend()
    assert isinstance(backend.convert_field(models.Facility, "latitude", 1.0), Decimal)


@pytest.mark.django_db
def test_detect_missing_relations(db):
    backend = Backend()
    now = datetime.datetime.now()
    net = models.Network(name="Test net", org_id=1, created=now, updated=now)
    with pytest.raises(Backend.validation_error()) as exc:
        backend.clean(net)

    info = backend.detect_missing_relations(net, exc.value)
    expected = defaultdict(set)
    expected[backend.get_resource(models.Organization)] = {1}
    assert dict(info) == dict(expected)


@pytest.mark.django_db
def test_detect_uniqueness_error(db):
    backend = Backend()
    now = datetime.datetime.now()
    org = models.Organization.objects.create(name="Test org", created=now, updated=now)
    org2 = models.Organization(name="Test org", created=now, updated=now)
    with pytest.raises(IntegrityError) as exc:
        backend.save(org2)

    info = backend.detect_uniqueness_error(exc.value)
    assert info == ["name"]
