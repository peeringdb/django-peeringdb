import importlib

import pytest
from django.apps import apps
from django.core.exceptions import ValidationError

from django_peeringdb.models import (
    Carrier,
    CarrierFacility,
    Facility,
    InternetExchange,
    IXLan,
    Network,
    NetworkIXLan,
    Organization,
)


@pytest.mark.django_db
def test_carriers():
    org = Organization.objects.create(name="Test")
    fac = Facility.objects.create(name="Test", org=org)
    carrier = Carrier.objects.create(name="Test", org=org)
    CarrierFacility.objects.create(carrier=carrier, fac=fac)

    assert carrier.carrierfac_set.count() == 1
    assert fac.carrierfac_set.count() == 1
    assert org.carrier_set.count() == 1


@pytest.mark.django_db
def test_facility_available_voltage_services_no_power():
    """'No Power' is valid alone but mutually exclusive with other voltages (#1884)."""
    org = Organization.objects.create(name="Test Org")
    fac = Facility(name="Test Fac", org=org)

    fac.available_voltage_services = ["No Power"]
    fac.full_clean()

    fac.available_voltage_services = ["No Power", "480 VAC"]
    with pytest.raises(ValidationError) as exc_info:
        fac.full_clean()
    assert "available_voltage_services" in exc_info.value.message_dict


# --- #1751 / #1742: metadata field and the netixlan status data migration ----

# migration modules start with a digit, so they cannot be imported by name.
# Both migration functions only call apps.get_model, so the real app registry
# is enough -- no django-test-migrations dependency needed.
_migration_0042 = importlib.import_module(
    "django_peeringdb.migrations.0042_netixlan_not_operational_status"
)


def _netixlan(status, operational, asn):
    org = Organization.objects.create(name=f"Org {asn}")
    net = Network.objects.create(name=f"Net {asn}", org=org, asn=asn)
    ix = InternetExchange.objects.create(
        name=f"IX {asn}", org=org, city="Testville", country="US"
    )
    ixlan = IXLan.objects.create(ix=ix)
    return NetworkIXLan.objects.create(
        net=net,
        ixlan=ixlan,
        asn=asn,
        speed=1000,
        status=status,
        operational=operational,
    )


@pytest.mark.django_db
def test_meta_defaults_to_empty_dict_and_round_trips():
    """`meta` exists on net and netixlan, defaults to {} and holds a dict (#1751)."""
    netixlan = _netixlan("ok", True, 64500)
    net = netixlan.net

    assert net.meta == {}
    assert netixlan.meta == {}

    net.meta = {"rtbh_community": "65000:666"}
    # `rir_status` is null=True without blank=True, so a default Network can
    # never pass a bare full_clean() -- unrelated to `meta`, excluded so this
    # stays a test of the metadata field
    net.full_clean(exclude=["rir_status"])
    net.save()
    net.refresh_from_db()
    assert net.meta == {"rtbh_community": "65000:666"}

    netixlan.meta = {"rfc8950": True}
    netixlan.full_clean()
    netixlan.save()
    netixlan.refresh_from_db()
    assert netixlan.meta == {"rfc8950": True}


@pytest.mark.django_db
def test_migration_0042_maps_non_operational_live_rows():
    """status="ok" + operational=False becomes the new status value (#1742)."""
    netixlan = _netixlan("ok", False, 64501)

    _migration_0042.forwards(apps, None)

    netixlan.refresh_from_db()
    assert netixlan.status == "not-operational"
    # the boolean is deliberately left alone -- `backwards` relies on it
    assert netixlan.operational is False


@pytest.mark.django_db
def test_migration_0042_leaves_operational_rows_alone():
    netixlan = _netixlan("ok", True, 64502)

    _migration_0042.forwards(apps, None)

    netixlan.refresh_from_db()
    assert netixlan.status == "ok"


@pytest.mark.django_db
@pytest.mark.parametrize("status", ["pending", "deleted"])
def test_migration_0042_does_not_disturb_lifecycle_rows(status):
    """
    The resurrection guard. A pending or deleted connection that happens to
    carry operational=False keeps its lifecycle status -- without the
    status="ok" scope in `forwards`, the migration would silently republish
    soft-deleted connections in every client database that runs it.
    """
    netixlan = _netixlan(status, False, 64503)

    _migration_0042.forwards(apps, None)

    netixlan.refresh_from_db()
    assert netixlan.status == status


@pytest.mark.django_db
def test_migration_0042_backwards_restores_the_previous_state():
    netixlan = _netixlan("ok", False, 64504)

    _migration_0042.forwards(apps, None)
    _migration_0042.backwards(apps, None)

    netixlan.refresh_from_db()
    assert netixlan.status == "ok"
    assert netixlan.operational is False
