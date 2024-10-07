import pytest
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
