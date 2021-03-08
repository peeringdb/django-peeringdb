from django.core.validators import URLValidator
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from django_handleref.models import HandleRefModel
from django.utils.translation import gettext_lazy as _

from django_inet.models import (
    ASNField,
    IPAddressField,
    IPPrefixField,
    MacAddressField,
)
from django_peeringdb import const


class LG_URLField(models.URLField):
    default_validators = [URLValidator(schemes=["http", "https", "telnet", "ssh"])]

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 255
        super().__init__(*args, **kwargs)


class URLField(models.URLField):
    default_validators = [URLValidator(schemes=["http", "https"])]

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 255
        super().__init__(*args, **kwargs)


class AddressModel(models.Model):
    """
    Postal Address
    """

    address1 = models.CharField(_("Address 1"), max_length=255, blank=True)
    address2 = models.CharField(_("Address 2"), max_length=255, blank=True)
    city = models.CharField(_("City"), max_length=255, blank=True)
    state = models.CharField(_("State"), max_length=255, blank=True)
    zipcode = models.CharField(_("Zip-Code"), max_length=48, blank=True)
    country = CountryField(_("Country"), blank=True)

    suite = models.CharField(_("Suite"), max_length=255, blank=True)
    floor = models.CharField(_("Floor"), max_length=255, blank=True)

    latitude = models.DecimalField(
        _("Latitude"), max_digits=9, decimal_places=6, blank=True, null=True
    )
    longitude = models.DecimalField(
        _("Longitude"), max_digits=9, decimal_places=6, blank=True, null=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.address1


class OrganizationBase(HandleRefModel, AddressModel):
    name = models.CharField(_("Name"), max_length=255, unique=True)

    aka = models.CharField(_("Also Known As"), max_length=255, blank=True)
    name_long = models.CharField(_("Long Name"), max_length=255, blank=True)

    website = URLField(_("Website"), blank=True)
    notes = models.TextField(_("Notes"), blank=True)

    class Meta:
        abstract = True
        db_table = "%sorganization" % settings.TABLE_PREFIX
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    class HandleRef:
        tag = "org"
        delete_cascade = ["net_set", "fac_set", "ix_set"]

    def __str__(self):
        return self.name


class FacilityBase(HandleRefModel, AddressModel):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    website = URLField(_("Website"), blank=True)

    aka = models.CharField(_("Also Known As"), max_length=255, blank=True)
    name_long = models.CharField(_("Long Name"), max_length=255, blank=True)

    clli = models.CharField(_("CLLI Code"), max_length=18, blank=True)
    rencode = models.CharField(_("Rencode"), max_length=18, blank=True)
    npanxx = models.CharField(_("NPA-NXX"), max_length=21, blank=True)

    tech_email = models.EmailField(_("Technical Email"), max_length=254, blank=True)
    tech_phone = models.CharField(
        _("Technical Phone"),
        max_length=192,
        blank=True,
        help_text=const.PHONE_HELP_TEXT,
    )
    sales_email = models.EmailField(_("Sales Email"), max_length=254, blank=True)
    sales_phone = models.CharField(
        _("Sales Phone"), max_length=192, blank=True, help_text=const.PHONE_HELP_TEXT
    )

    notes = models.TextField(_("Notes"), blank=True)

    class Meta:
        abstract = True
        db_table = "%sfacility" % settings.TABLE_PREFIX
        verbose_name = _("Facility")
        verbose_name_plural = _("Facilities")

    class HandleRef:
        tag = "fac"
        delete_cascade = ["ixfac_set", "netfac_set"]

    def __str__(self):
        return self.name


class ContactBase(HandleRefModel):
    role = models.CharField(_("Role"), max_length=27, choices=const.POC_ROLES)
    visible = models.CharField(
        _("Visibility"), max_length=64, choices=const.VISIBILITY, default="Public"
    )
    name = models.CharField(_("Name"), max_length=254, blank=True)
    phone = models.CharField(
        _("Phone"), max_length=100, blank=True, help_text=const.PHONE_HELP_TEXT
    )
    email = models.EmailField(_("Email"), max_length=254, blank=True)
    url = URLField(_("URL"), blank=True)

    class Meta:
        abstract = True
        db_table = "%snetwork_contact" % settings.TABLE_PREFIX
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    class HandleRef:
        tag = "poc"


class NetworkBase(HandleRefModel):
    asn = ASNField(verbose_name="ASN", unique=True)
    name = models.CharField(_("Name"), max_length=255, unique=True)

    aka = models.CharField(_("Also Known As"), max_length=255, blank=True)
    name_long = models.CharField(_("Long Name"), max_length=255, blank=True)

    irr_as_set = models.CharField(
        _("IRR as-set/route-set"),
        max_length=255,
        blank=True,
        help_text=_(
            "Reference to an AS-SET or "
            "ROUTE-SET in Internet "
            "Routing Registry (IRR)"
        ),
    )
    website = URLField(_("Website"), blank=True)
    looking_glass = LG_URLField(_("Looking Glass URL"), blank=True)
    route_server = LG_URLField(_("Route Server URL"), blank=True)

    notes = models.TextField(_("Notes"), blank=True)
    notes_private = models.TextField(_("Private notes"), blank=True)

    info_traffic = models.CharField(
        _("Traffic Levels"), max_length=39, blank=True, choices=const.TRAFFIC
    )
    info_ratio = models.CharField(
        _("Traffic Ratios"),
        max_length=45,
        blank=True,
        choices=const.RATIOS,
        default="Not Disclosed",
    )
    info_scope = models.CharField(
        _("Geographic Scope"),
        max_length=39,
        blank=True,
        choices=const.SCOPES,
        default="Not Disclosed",
    )
    info_type = models.CharField(
        _("Network Type"),
        max_length=60,
        blank=True,
        choices=const.NET_TYPES,
        default="Not Disclosed",
    )
    info_prefixes4 = models.PositiveIntegerField(
        _("IPv4 Prefixes"),
        null=True,
        blank=True,
        help_text=_(
            "Recommended maximum number of IPv4 "
            "routes/prefixes to be configured on peering "
            "sessions for this ASN"
        ),
    )
    info_prefixes6 = models.PositiveIntegerField(
        _("IPv6 Prefixes"),
        null=True,
        blank=True,
        help_text=_(
            "Recommended maximum number of IPv6 "
            "routes/prefixes to be configured on peering "
            "sessions for this ASN"
        ),
    )
    info_unicast = models.BooleanField(_("Unicast IPv4"), default=False)
    info_multicast = models.BooleanField(_("Multicast"), default=False)
    info_ipv6 = models.BooleanField(_("Unicast IPv6"), default=False)
    info_never_via_route_servers = models.BooleanField(
        _("Never via route servers"),
        default=False,
        help_text=_(
            "Indicates if this network "
            "will announce its routes "
            "via route servers or not"
        ),
    )

    policy_url = URLField(_("Peering Policy"), blank=True)
    policy_general = models.CharField(
        _("General Policy"), max_length=72, blank=True, choices=const.POLICY_GENERAL
    )
    policy_locations = models.CharField(
        _("Multiple Locations"),
        max_length=72,
        blank=True,
        choices=const.POLICY_LOCATIONS,
    )
    policy_ratio = models.BooleanField(_("Ratio Requirement"), default=False)
    policy_contracts = models.CharField(
        _("Contract Requirement"),
        max_length=36,
        blank=True,
        choices=const.POLICY_CONTRACTS,
    )

    class Meta:
        abstract = True
        db_table = "%snetwork" % settings.TABLE_PREFIX
        verbose_name = _("Network")
        verbose_name_plural = _("Networks")

    class HandleRef:
        tag = "net"
        delete_cascade = ["poc_set", "netfac_set", "netixlan_set"]

    def __str__(self):
        return self.name


class InternetExchangeBase(HandleRefModel):
    name = models.CharField(_("Name"), max_length=64, unique=True)

    aka = models.CharField(_("Also Known As"), max_length=255, blank=True)
    name_long = models.CharField(_("Long Name"), max_length=255, blank=True)

    city = models.CharField(_("City"), max_length=192)
    country = CountryField(_("Country"))

    notes = models.TextField(_("Notes"), blank=True)

    region_continent = models.CharField(
        _("Continental Region"), max_length=255, choices=const.REGIONS
    )
    media = models.CharField(_("Media Type"), max_length=128, choices=const.MEDIA)
    proto_unicast = models.BooleanField(_("Unicast IPv4"), default=False)
    proto_multicast = models.BooleanField(_("Multicast"), default=False)
    proto_ipv6 = models.BooleanField(_("Unicast IPv6"), default=False)

    website = URLField(_("Company Website"), blank=True)
    url_stats = URLField(_("Traffic Stats Website"), blank=True)

    tech_email = models.EmailField(_("Technical Email"), max_length=254, blank=True)
    tech_phone = models.CharField(
        _("Technical Phone"),
        max_length=192,
        blank=True,
        help_text=const.PHONE_HELP_TEXT,
    )
    policy_email = models.EmailField(_("Policy Email"), max_length=254, blank=True)
    policy_phone = models.CharField(
        _("Policy Phone"), max_length=192, blank=True, help_text=const.PHONE_HELP_TEXT
    )

    ixf_net_count = models.IntegerField(_("IX-F Network Count"), default=0)
    ixf_last_import = models.DateTimeField(_("IX-F Last Import"), null=True, blank=True)

    class Meta:
        abstract = True
        db_table = "%six" % settings.TABLE_PREFIX
        verbose_name = _("Internet Exchange")
        verbose_name_plural = _("Internet Exchanges")

    class HandleRef:
        tag = "ix"
        delete_cascade = ["ixfac_set", "ixlan_set"]

    def __str__(self):
        return self.name


class InternetExchangeFacilityBase(HandleRefModel):
    class Meta:
        abstract = True
        db_table = "%six_facility" % settings.TABLE_PREFIX
        verbose_name = _("Internet Exchange facility")
        verbose_name_plural = _("Internet Exchange facilities")

    class HandleRef:
        tag = "ixfac"


class IXLanBase(HandleRefModel):
    name = models.CharField(_("Name"), max_length=255, blank=True)
    descr = models.TextField(_("Description"), blank=True)
    mtu = models.PositiveIntegerField("MTU", null=True, blank=True)
    vlan = models.PositiveIntegerField("VLAN", null=True, blank=True)
    dot1q_support = models.BooleanField("802.1Q", default=False)
    rs_asn = ASNField(
        verbose_name=_("Route Server ASN"), null=True, blank=True, default=0
    )
    arp_sponge = MacAddressField(
        verbose_name=_("ARP sponging MAC"), null=True, unique=True, blank=True
    )

    ixf_ixp_member_list_url = models.URLField(
        verbose_name=_("IX-F Member Export URL"), null=True, blank=True
    )
    ixf_ixp_member_list_url_visible = models.CharField(
        verbose_name=_("IX-F Member Export URL Visibility"),
        max_length=64,
        choices=const.VISIBILITY,
        default="Private",
    )

    class Meta:
        abstract = True
        db_table = "%sixlan" % settings.TABLE_PREFIX
        verbose_name = _("Internet Exchange LAN")
        verbose_name_plural = _("Internet Exchange LANs")

    class HandleRef:
        tag = "ixlan"
        delete_cascade = ["ixpfx_set", "netixlan_set"]


class IXLanPrefixBase(HandleRefModel):
    notes = models.CharField(_("Notes"), max_length=255, blank=True)
    protocol = models.CharField(_("Protocol"), max_length=64, choices=const.PROTOCOLS)
    prefix = IPPrefixField(verbose_name=_("Prefix"), unique=True)
    in_dfz = models.BooleanField(default=False)

    class Meta:
        abstract = True
        db_table = "%sixlan_prefix" % settings.TABLE_PREFIX
        verbose_name = _("Internet Exchange LAN prefix")
        verbose_name_plural = _("Internet Exchange LAN prefixes")

    class HandleRef:
        tag = "ixpfx"


class NetworkFacilityBase(HandleRefModel):
    local_asn = ASNField(verbose_name=_("Local ASN"), null=True, blank=True)
    avail_sonet = models.BooleanField("SONET", default=False)
    avail_ethernet = models.BooleanField("Ethernet", default=False)
    avail_atm = models.BooleanField("ATM", default=False)

    class Meta:
        abstract = True
        db_table = "%snetwork_facility" % settings.TABLE_PREFIX
        verbose_name = _("Network Facility")
        verbose_name_plural = _("Network Facilities")

    class HandleRef:
        tag = "netfac"


class NetworkIXLanBase(HandleRefModel):
    asn = ASNField(verbose_name="ASN")
    ipaddr4 = IPAddressField(verbose_name="IPv4", version=4, blank=True, null=True)
    ipaddr6 = IPAddressField(verbose_name="IPv6", version=6, blank=True, null=True)
    is_rs_peer = models.BooleanField(_("RS peer"), default=False)
    notes = models.CharField(_("Notes"), max_length=255, blank=True)
    speed = models.PositiveIntegerField(_("Speed (mbit/sec)"))
    operational = models.BooleanField(_("Operational"), default=True)

    class Meta:
        abstract = True
        db_table = "%snetwork_ixlan" % settings.TABLE_PREFIX
        verbose_name = _("Public Peering Exchange Point")
        verbose_name_plural = _("Public Peering Exchange Points")

    class HandleRef:
        tag = "netixlan"
