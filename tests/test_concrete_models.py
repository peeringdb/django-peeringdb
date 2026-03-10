import pytest
from django.core.exceptions import ValidationError

from django_peeringdb.models import Carrier, CarrierFacility, Facility, Organization


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
