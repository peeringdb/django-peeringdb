
from __future__ import unicode_literals
from django.core.validators import URLValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
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
    address1 = models.CharField(max_length=255, blank=True,
                                verbose_name=_('address 1'))
    address2 = models.CharField(max_length=255, blank=True,
                                verbose_name=_('address 2'))
    city = models.CharField(max_length=255, blank=True,
                            verbose_name=_('city'))
    state = models.CharField(max_length=255, blank=True,
                             verbose_name=_('state'))
    zipcode = models.CharField(max_length=48, blank=True,
                               verbose_name=_('ZIP Code'))
    country = CountryField(blank=True,
                           verbose_name=_('country'))

    latitude = models.DecimalField(max_digits=9, decimal_places=6,
                                   blank=True, null=True,
                                   verbose_name=_('latitude'))
    longitude = models.DecimalField(max_digits=9, decimal_places=6,
                                    blank=True, null=True,
                                    verbose_name=_('longitude'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.address1


class OrganizationBase(HandleRefModel, AddressModel):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name=_('name'))
    website = URLField(blank=True, verbose_name=_('website'))
    notes = models.TextField(blank=True, verbose_name=_('notes'))

    class Meta:
        abstract = True
        db_table = '%sorganization' % settings.TABLE_PREFIX
        verbose_name_plural = "Organizations"

    class HandleRef:
        tag = 'org'
        delete_cascade = ["net_set", "fac_set", "ix_set"]
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    def __str__(self):
        return self.name


class FacilityBase(HandleRefModel, AddressModel):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name=_('name'))
    website = URLField(blank=True, verbose_name=_('website'))

    clli = models.CharField(max_length=18, blank=True,
                            verbose_name=_('CLLI Code'))
    rencode = models.CharField(max_length=18, blank=True,
                               verbose_name=_('rencode'))
    npanxx = models.CharField(max_length=21, blank=True,
                              verbose_name=_('NPA-NXX'))

    notes = models.TextField(blank=True)

    class Meta:
        abstract = True
        db_table = '%sfacility' % settings.TABLE_PREFIX
        verbose_name = _('Facility')
        verbose_name_plural = _('Facilities')

    class HandleRef:
        tag = 'fac'
        delete_cascade = ["ixfac_set", "netfac_set"]

    def __str__(self):
        return self.name


class ContactBase(HandleRefModel):
    role = models.CharField(max_length=27, choices=const.POC_ROLES,
                            verbose_name=_('role'))
    visible = models.CharField(
        max_length=64, choices=const.VISIBILITY, default='Public',
        verbose_name=_('visibility'),
    )
    name = models.CharField(max_length=254, blank=True,
                            verbose_name=_('name'))
    phone = models.CharField(max_length=100, blank=True,
                            verbose_name=_('phone'))
    email = models.EmailField(max_length=254, blank=True,
                              verbose_name=_('email'))
    url = URLField(blank=True, verbose_name=_('URL'))

    class Meta:
        abstract = True
        db_table = '%snetwork_contact' % settings.TABLE_PREFIX
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    class HandleRef:
        tag = 'poc'


class NetworkBase(HandleRefModel):
    asn = ASNField(unique=True, verbose_name=_('Primary ASN'))
    name = models.CharField(max_length=255, unique=True,
                            verbose_name=_('name'))
    aka = models.CharField(max_length=255, blank=True,
                           verbose_name=_('also known as'))
    irr_as_set = models.CharField(max_length=255, blank=True,
                                  verbose_name=_('IRR Record'))

    website = URLField(blank=True, verbose_name=_('company website'))
    looking_glass = URLField(blank=True, verbose_name=_('looking glass URL'))
    route_server = URLField(blank=True, verbose_name=_('route server URL'))

    notes = models.TextField(blank=True, verbose_name=_('notes'))
    notes_private = models.TextField(blank=True, verbose_name=_('private notes'))

    info_traffic = models.CharField(
        max_length=39, blank=True, choices=const.TRAFFIC,
        verbose_name=_('traffic levels'),
    )
    info_ratio = models.CharField(max_length=45, blank=True, choices=const.RATIOS,
                                  default='Not Disclosed',
                                  verbose_name=_('traffic ratios'))
    info_scope = models.CharField(max_length=39, blank=True, choices=const.SCOPES,
                                  default='Not Disclosed',
                                  verbose_name=_('geographic scope'))
    info_type = models.CharField(max_length=60, blank=True, choices=const.NET_TYPES,
                                 default='Not Disclosed',
                                 verbose_name=_('network type'))
    info_prefixes4 = models.PositiveIntegerField(
        null=True, blank=True,
        verbose_name=_('IPv4 Prefixes'),
    )
    info_prefixes6 = models.PositiveIntegerField(
        null=True, blank=True,
        verbose_name=_('IPv6 Prefixes'),
    )
    info_unicast = models.BooleanField(default=False,
                                       verbose_name=_('unicast IPv4'))
    info_multicast = models.BooleanField(default=False,
                                         verbose_name=_('multicast'))
    info_ipv6 = models.BooleanField(default=False,
                                    verbose_name=_('unicast IPv6'))

    policy_url = URLField(blank=True, verbose_name=_('peering policy'))
    policy_general = models.CharField(max_length=72, blank=True,
                                      choices=const.POLICY_GENERAL,
                                      verbose_name=_('general policy'))
    policy_locations = models.CharField(max_length=72, blank=True,
                                        choices=const.POLICY_LOCATIONS,
                                        verbose_name=_('multiple locations'))
    policy_ratio = models.BooleanField(default=False,
                                       verbose_name=_('ratio requirement'))
    policy_contracts = models.CharField(max_length=36, blank=True,
                                        choices=const.POLICY_CONTRACTS,
                                        verbose_name=_('contract requirement'))

    class Meta:
        abstract = True
        db_table = '%snetwork' % settings.TABLE_PREFIX;
        verbose_name = _('Network')
        verbose_name_plural = _('Networks')

    class HandleRef:
        tag = 'net'
        delete_cascade = ["poc_set", "netfac_set", "netixlan_set"]

    def __str__(self):
        return self.name


class InternetExchangeBase(HandleRefModel):
    name = models.CharField(max_length=64, unique=True,
                            verbose_name=_('name'))
    name_long = models.CharField(max_length=254, blank=True,
                                 verbose_name=_('long name'))

    city = models.CharField(max_length=192, verbose_name=_('city'))
    country = CountryField(verbose_name=_('country'))

    notes = models.TextField(blank=True, verbose_name=_('notes'))

    region_continent = models.CharField(
        max_length=255, choices=const.REGIONS,
        verbose_name=_('continental region'),
    )
    media = models.CharField(max_length=128, choices=const.MEDIA,
                             verbose_name=_('media type'))
    proto_unicast = models.BooleanField(default=False,
                                        verbose_name=_('unicast IPv4'))
    proto_multicast = models.BooleanField(default=False,
                                          verbose_name=_('multicast'))
    proto_ipv6 = models.BooleanField(default=False,
                                     verbose_name=_('unicast IPv6'))

    website = URLField(blank=True, verbose_name=_('company website'))
    url_stats = URLField(blank=True, verbose_name=_('traffic stats website'))

    tech_email = models.EmailField(max_length=254, blank=True,
                                   verbose_name=_('technical email'))
    tech_phone = models.CharField(max_length=192, blank=True,
                                  verbose_name=_('technical phone'))
    policy_email = models.EmailField(max_length=254, blank=True,
                                     verbose_name=_('policy email'))
    policy_phone = models.CharField(max_length=192, blank=True,
                                    verbose_name=_('policy phone'))

    class Meta:
        abstract = True
        db_table = '%six' % settings.TABLE_PREFIX

    class HandleRef:
        tag = 'ix'
        delete_cascade = ["ixfac_set", "ixlan_set"]
        verbose_name = _('Internet exchange')
        verbose_name_plural = _('Internet exchanges')

    def __str__(self):
        return self.name


class InternetExchangeFacilityBase(HandleRefModel):

    class Meta:
        abstract = True
        db_table = '%six_facility' % settings.TABLE_PREFIX
        verbose_name = _('internet exchange/facility')
        verbose_name_plural = _('internet exchanges/facilities')

    class HandleRef:
        tag = 'ixfac'


class IXLanBase(HandleRefModel):
    name = models.CharField(max_length=255, blank=True,
                            verbose_name=_('name'))
    descr = models.TextField(blank=True, verbose_name=_('description'))
    mtu = models.PositiveIntegerField(null=True, blank=True,
                                      verbose_name=_('MTU'))
    vlan = models.PositiveIntegerField(null=True, blank=True,
                                      verbose_name=_('VLAN'))
    dot1q_support = models.BooleanField(default=False,
                                        verbose_name=_('802.1Q'))
    rs_asn = ASNField(null=True, blank=True, default=0,
                      verbose_name=_('route server ASN'))
    arp_sponge = MacAddressField(null=True, unique=True, blank=True,
                                 verbose_name=_('ARP sponging MAC'))

    class Meta:
        abstract = True
        db_table = '%sixlan' % settings.TABLE_PREFIX
        verbose_name = _('internet exchange LAN')
        verbose_name_plural = _('internet exchange LANs')

    class HandleRef:
        tag = 'ixlan'
        delete_cascade = ["ixpfx_set", "netixlan_set"]


class IXLanPrefixBase(HandleRefModel):
    notes = models.CharField(max_length=255, blank=True,
                             verbose_name=_('notes'))
    protocol = models.CharField(max_length=64, choices=const.PROTOCOLS,
                                verbose_name=_('protocol'))
    prefix = IPPrefixField(unique=True, verbose_name=_('prefix'))

    class Meta:
        abstract = True
        db_table = '%sixlan_prefix' % settings.TABLE_PREFIX
        verbose_name = _('internet exchange LAN prefix')
        verbose_name_plural = _('internet exchange LAN prefixes')

    class HandleRef:
        tag = 'ixpfx'

    def __str__(self):
        return str(self.prefix)


class NetworkFacilityBase(HandleRefModel):
    local_asn = ASNField(null=True, blank=True, verbose_name=_('local ASN'))
    avail_sonet = models.BooleanField(default=False, verbose_name=_('SONET'))
    avail_ethernet = models.BooleanField(default=False,
                                         verbose_name=_('Ethernet'))
    avail_atm = models.BooleanField(default=False, verbose_name=_('ATM'))

    class Meta:
        abstract = True
        db_table = '%snetwork_facility' % settings.TABLE_PREFIX
        verbose_name = _('network/facility')
        verbose_name_plural = _('networks/facilities')

    class HandleRef:
        tag = 'netfac'


class NetworkIXLanBase(HandleRefModel):
    asn = ASNField(verbose_name=_('ASN'))
    ipaddr4 = IPAddressField(version=4, blank=True, null=True,
                             verbose_name=_('IPv4'))
    ipaddr6 = IPAddressField(version=6, blank=True, null=True,
                             verbose_name=_('IPv6'))
    is_rs_peer = models.BooleanField(default=False,
                                     verbose_name=_('route server peer'))
    notes = models.CharField(max_length=255, blank=True,
                                     verbose_name=_('notes'))
    speed = models.PositiveIntegerField(verbose_name=_('speed'),
                                        help_text=_('Mbps'))

    class Meta:
        abstract = True
        db_table = '%snetwork_ixlan' % settings.TABLE_PREFIX
        verbose_name = _('network/internet exchange LAN')
        verbose_name_plural = _('networks/internet exchange LANs')

    class HandleRef:
        tag = "netixlan"


