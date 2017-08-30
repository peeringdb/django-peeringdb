
from django.core.validators import URLValidator
from django.db import models
from django_countries.fields import CountryField
from django_handleref.models import HandleRefModel

from django_inet.models import (
    ASNField,
    IPAddressField,
    IPPrefixField,
    MacAddressField,
)
from django_peeringdb import (
    const,
    settings,
)


class URLField(models.URLField):
    default_validators = [URLValidator(schemes=["http", "https", "ftp", "ftps", "telnet"])]

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 255
        super(URLField, self).__init__(*args, **kwargs)


class AddressModel(models.Model):
    """
    Postal Address
    """
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=48, blank=True)
    country = CountryField(blank=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, help_text="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, help_text="Longitude")

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.address1


class OrganizationBase(HandleRefModel, AddressModel):
    name = models.CharField(max_length=255, unique=True)
    website = URLField(blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        abstract = True
        db_table = '%sorganization' % settings.TABLE_PREFIX
        verbose_name_plural = "Organizations"

    class HandleRef:
        tag = 'org'
        delete_cascade = ["net_set", "fac_set", "ix_set"]

    def __unicode__(self):
        return self.name


class FacilityBase(HandleRefModel, AddressModel):
    name = models.CharField(max_length=255, unique=True)
    website = URLField(blank=True)

    clli = models.CharField(max_length=18, blank=True)
    rencode = models.CharField(max_length=18, blank=True)
    npanxx = models.CharField(max_length=21, blank=True)

    notes = models.TextField(blank=True)

    class Meta:
        abstract = True
        db_table = '%sfacility' % settings.TABLE_PREFIX
        verbose_name_plural = "Facilities"

    class HandleRef:
        tag = 'fac'
        delete_cascade = ["ixfac_set", "netfac_set"]

    def __unicode__(self):
        return self.name


class ContactBase(HandleRefModel):
    role = models.CharField(max_length=27, choices=const.POC_ROLES)
    visible = models.CharField(
        max_length=64, choices=const.VISIBILITY, default='Public')
    name = models.CharField(max_length=254, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    url = URLField(blank=True)

    class Meta:
        abstract = True
        db_table = '%snetwork_contact' % settings.TABLE_PREFIX

    class HandleRef:
        tag = 'poc'


class NetworkBase(HandleRefModel):
    asn = ASNField(unique=True)
    name = models.CharField(max_length=255, unique=True)
    aka = models.CharField(max_length=255, blank=True)
    irr_as_set = models.CharField(max_length=255, blank=True)

    website = URLField(blank=True)
    looking_glass = URLField(blank=True)
    route_server = URLField(blank=True)

    notes = models.TextField(blank=True)
    notes_private = models.TextField(blank=True)

    info_traffic = models.CharField(
        max_length=39, blank=True, choices=const.TRAFFIC)
    info_ratio = models.CharField(max_length=45, blank=True, choices=const.RATIOS,
                                  default='Not Disclosed')
    info_scope = models.CharField(max_length=39, blank=True, choices=const.SCOPES,
                                  default='Not Disclosed')
    info_type = models.CharField(max_length=60, blank=True, choices=const.NET_TYPES,
                                 default='Not Disclosed')
    info_prefixes4 = models.PositiveIntegerField(null=True, blank=True)
    info_prefixes6 = models.PositiveIntegerField(null=True, blank=True)
    info_unicast = models.BooleanField(default=False)
    info_multicast = models.BooleanField(default=False)
    info_ipv6 = models.BooleanField(default=False)

    policy_url = URLField(blank=True)
    policy_general = models.CharField(max_length=72, blank=True,
                                      choices=const.POLICY_GENERAL)
    policy_locations = models.CharField(max_length=72, blank=True,
                                        choices=const.POLICY_LOCATIONS)
    policy_ratio = models.BooleanField(default=False)
    policy_contracts = models.CharField(max_length=36, blank=True,
                                        choices=const.POLICY_CONTRACTS)

    class Meta:
        abstract = True
        db_table = '%snetwork' % settings.TABLE_PREFIX;
        verbose_name_plural = "Networks"

    class HandleRef:
        tag = 'net'
        delete_cascade = ["poc_set", "netfac_set", "netixlan_set"]

    def __unicode__(self):
        return self.name


class InternetExchangeBase(HandleRefModel):
    name = models.CharField(max_length=64, unique=True)
    name_long = models.CharField(max_length=254, blank=True)

    city = models.CharField(max_length=192)
    country = CountryField()

    notes = models.TextField(blank=True)

    region_continent = models.CharField(
        max_length=255, choices=const.REGIONS)
    media = models.CharField(max_length=128, choices=const.MEDIA)
    proto_unicast = models.BooleanField(default=False)
    proto_multicast = models.BooleanField(default=False)
    proto_ipv6 = models.BooleanField(default=False)

    website = URLField(blank=True)
    url_stats = URLField(blank=True)

    tech_email = models.EmailField(max_length=254, blank=True)
    tech_phone = models.CharField(max_length=192, blank=True)
    policy_email = models.EmailField(max_length=254, blank=True)
    policy_phone = models.CharField(max_length=192, blank=True)

    class Meta:
        abstract = True
        db_table = '%six' % settings.TABLE_PREFIX

    class HandleRef:
        tag = 'ix'
        delete_cascade = ["ixfac_set", "ixlan_set"]

    def __unicode__(self):
        return self.name


class InternetExchangeFacilityBase(HandleRefModel):

    class Meta:
        abstract = True
        db_table = '%six_facility' % settings.TABLE_PREFIX
        verbose_name_plural = "internet exchange facilities"

    class HandleRef:
        tag = 'ixfac'


class IXLanBase(HandleRefModel):
    name = models.CharField(max_length=255, blank=True)
    descr = models.TextField(blank=True)
    mtu = models.PositiveIntegerField(null=True, blank=True)
    vlan = models.PositiveIntegerField(null=True, blank=True)
    dot1q_support = models.BooleanField(default=False)
    rs_asn = ASNField(null=True, blank=True, default=0)
    arp_sponge = MacAddressField(null=True, unique=True, blank=True)

    class Meta:
        abstract = True
        db_table = '%sixlan' % settings.TABLE_PREFIX

    class HandleRef:
        tag = 'ixlan'
        delete_cascade = ["ixpfx_set", "netixlan_set"]


class IXLanPrefixBase(HandleRefModel):
    notes = models.CharField(max_length=255, blank=True)
    protocol = models.CharField(max_length=64, choices=const.PROTOCOLS)
    prefix = IPPrefixField(unique=True)

    class Meta:
        abstract = True
        db_table = '%sixlan_prefix' % settings.TABLE_PREFIX

    class HandleRef:
        tag = 'ixpfx'


class NetworkFacilityBase(HandleRefModel):
    local_asn = ASNField(null=True, blank=True)
    avail_sonet = models.BooleanField(default=False)
    avail_ethernet = models.BooleanField(default=False)
    avail_atm = models.BooleanField(default=False)

    class Meta:
        abstract = True
        db_table = '%snetwork_facility' % settings.TABLE_PREFIX
        verbose_name_plural = "Network Facilities"

    class HandleRef:
        tag = 'netfac'


class NetworkIXLanBase(HandleRefModel):
    asn = ASNField()
    ipaddr4 = IPAddressField(version=4, blank=True, null=True)
    ipaddr6 = IPAddressField(version=6, blank=True, null=True)
    is_rs_peer = models.BooleanField(default=False)
    notes = models.CharField(max_length=255, blank=True)
    speed = models.PositiveIntegerField()

    class Meta:
        abstract = True
        db_table = '%snetwork_ixlan' % settings.TABLE_PREFIX

    class HandleRef:
        tag = "netixlan"


