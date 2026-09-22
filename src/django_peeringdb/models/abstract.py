from __future__ import annotations

from collections.abc import Callable
from typing import Any, ClassVar

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django_handleref.models import HandleRefModel
from django_inet.models import ASNField, IPAddressField, IPPrefixField, MacAddressField

from django_peeringdb import const
from django_peeringdb.fields import MultipleChoiceField

# The `help_text` on the fields below is written against peeringdb.com's REST API
# on purpose: phrasings like "Read-only", "Not exposed via the API" and "values
# submitted on create or update are ignored" describe how the reference
# deployment treats the field, not a constraint this library enforces. The main
# use of this library is mirroring that API, so that is the useful register --
# keep new help_text in it.


class LG_URLField(models.URLField):
    default_validators: ClassVar[list[Callable[[Any], None]]] = [
        URLValidator(schemes=["http", "https", "telnet", "ssh"])
    ]

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 255
        super().__init__(*args, **kwargs)


class URLField(models.URLField):
    default_validators: ClassVar[list[Callable[[Any], None]]] = [
        URLValidator(schemes=["http", "https"])
    ]

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 255
        super().__init__(*args, **kwargs)


class AddressModel(models.Model):
    """
    Postal Address
    """

    address1: models.CharField = models.CharField(
        _("Address 1"),
        max_length=255,
        blank=True,
        help_text=_("First line of the street address"),
    )
    address2: models.CharField = models.CharField(
        _("Address 2"),
        max_length=255,
        blank=True,
        help_text=_("Second line of the street address, if needed"),
    )
    city: models.CharField = models.CharField(
        _("City"), max_length=255, blank=True, help_text=_("City of the postal address")
    )
    state: models.CharField = models.CharField(
        _("State"),
        max_length=255,
        blank=True,
        help_text=_("State, province or region of the postal address"),
    )
    zipcode: models.CharField = models.CharField(
        _("Zip-Code"),
        max_length=48,
        blank=True,
        help_text=_("Postal code of the postal address"),
    )
    country: CountryField = CountryField(
        _("Country"),
        blank=True,
        help_text=_("Two-letter ISO 3166-1 alpha-2 country code"),
    )

    suite: models.CharField = models.CharField(
        _("Suite"),
        max_length=255,
        blank=True,
        help_text=_("Suite or unit within the building"),
    )
    floor: models.CharField = models.CharField(
        _("Floor"), max_length=255, blank=True, help_text=_("Floor within the building")
    )

    latitude: models.DecimalField = models.DecimalField(
        _("Latitude"),
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text=_(
            "Latitude in decimal degrees, derived by geocoding the postal address"
        ),
    )
    longitude: models.DecimalField = models.DecimalField(
        _("Longitude"),
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text=_(
            "Longitude in decimal degrees, derived by geocoding the postal address"
        ),
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.address1


class OrganizationBase(HandleRefModel, AddressModel):
    name: models.CharField = models.CharField(
        _("Name"),
        max_length=255,
        unique=True,
        help_text=_("Name of the organization, unique across PeeringDB"),
    )

    aka: models.CharField = models.CharField(
        _("Also Known As"), max_length=255, blank=True, help_text=const.AKA_HELP_TEXT
    )
    name_long: models.CharField = models.CharField(
        _("Long Name"),
        max_length=255,
        blank=True,
        help_text=const.NAME_LONG_HELP_TEXT,
    )

    website: URLField = URLField(
        _("Website"),
        blank=True,
        default="",
        help_text=_("Website of the organization"),
    )
    social_media = models.JSONField(
        _("Social Media"),
        default=dict,
        blank=True,
        help_text=const.SOCIAL_MEDIA_HELP_TEXT,
    )
    notes: models.TextField = models.TextField(
        _("Notes"), blank=True, help_text=const.NOTES_HELP_TEXT
    )

    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}organization"
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    class HandleRef:
        tag = "org"
        delete_cascade: ClassVar[list[str]] = [
            "net_set",
            "fac_set",
            "ix_set",
            "carrier_set",
            "campus_set",
        ]

    def __str__(self):
        return self.name


class FacilityBase(HandleRefModel, AddressModel):
    name: models.CharField = models.CharField(
        _("Name"),
        max_length=255,
        unique=True,
        help_text=_("Name of the facility, unique across PeeringDB"),
    )
    website: URLField = URLField(
        _("Website"), blank=True, help_text=_("Website of the facility")
    )
    social_media = models.JSONField(
        _("Social Media"),
        default=dict,
        blank=True,
        help_text=const.SOCIAL_MEDIA_HELP_TEXT,
    )

    aka: models.CharField = models.CharField(
        _("Also Known As"), max_length=255, blank=True, help_text=const.AKA_HELP_TEXT
    )
    name_long: models.CharField = models.CharField(
        _("Long Name"),
        max_length=255,
        blank=True,
        help_text=const.NAME_LONG_HELP_TEXT,
    )

    clli: models.CharField = models.CharField(
        _("CLLI Code"),
        max_length=18,
        blank=True,
        help_text=_("Common Language Location Identifier code for this facility"),
    )
    rencode: models.CharField = models.CharField(
        _("Rencode"),
        max_length=18,
        blank=True,
        help_text=_(
            "Obsolete. Read-only; values submitted on create or update are ignored"
        ),
    )
    npanxx: models.CharField = models.CharField(
        _("NPA-NXX"),
        max_length=21,
        blank=True,
        help_text=_(
            "North American Numbering Plan area code and exchange prefix serving this facility, as NPA-NXX"
        ),
    )

    tech_email: models.EmailField = models.EmailField(
        _("Technical Email"),
        max_length=254,
        blank=True,
        help_text=_("Address to send technical questions about this facility"),
    )
    tech_phone: models.CharField = models.CharField(
        _("Technical Phone"),
        max_length=192,
        blank=True,
        help_text=const.PHONE_HELP_TEXT,
    )
    sales_email: models.EmailField = models.EmailField(
        _("Sales Email"),
        max_length=254,
        blank=True,
        help_text=_("Address to send sales questions about this facility"),
    )
    sales_phone: models.CharField = models.CharField(
        _("Sales Phone"), max_length=192, blank=True, help_text=const.PHONE_HELP_TEXT
    )

    property: models.CharField = models.CharField(
        _("Property"),
        max_length=27,
        null=True,
        blank=True,
        choices=const.PROPERTY,
        help_text=_(
            "Leasing or renting is an agreement with a property owner for use of the property."
        ),
    )

    diverse_serving_substations: models.BooleanField = models.BooleanField(
        _("Diverse Serving Substations"),
        null=True,
        blank=True,
        help_text=_(
            "Two separate and distinct paths to individual substations which should maintain a separated path back to one or more utility generator stations."
        ),
    )

    available_voltage_services: MultipleChoiceField = MultipleChoiceField(
        _("Available Voltage Services"),
        null=True,
        blank=True,
        max_length=255,
        choices=const.AVAILABLE_VOLTAGE,
        help_text=_(
            "The alternating current voltage available to users of the facility either directly from the landlord or delivered by the utility separately."
        ),
    )

    notes: models.TextField = models.TextField(
        _("Notes"), blank=True, help_text=const.NOTES_HELP_TEXT
    )

    region_continent: models.CharField = models.CharField(
        _("Continental Region"),
        max_length=255,
        choices=const.REGIONS,
        blank=True,
        null=True,
        help_text=_("Continental region, derived from the country of the address"),
    )

    status_dashboard: URLField = URLField(
        _("Status Dashboard"),
        null=True,
        blank=True,
        help_text=_("URL of a public status or outage dashboard for this facility"),
    )

    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}facility"
        verbose_name = _("Facility")
        verbose_name_plural = _("Facilities")

    class HandleRef:
        tag = "fac"
        delete_cascade: ClassVar[list[str]] = [
            "ixfac_set",
            "netfac_set",
            "carrierfac_set",
        ]

    def clean(self):
        super().clean()
        avs = self.available_voltage_services
        if avs and "No Power" in avs and len(avs) > 1:
            raise ValidationError(
                {
                    "available_voltage_services": _(
                        '"No Power" is mutually exclusive with other voltage options.'
                    )
                }
            )

    def __str__(self):
        return self.name


class ContactBase(HandleRefModel):
    role: models.CharField = models.CharField(
        _("Role"),
        max_length=27,
        choices=const.POC_ROLES,
        help_text=_("Function this contact serves for the network"),
    )
    visible: models.CharField = models.CharField(
        _("Visibility"),
        max_length=64,
        choices=const.VISIBILITY,
        default="Public",
        help_text=_(
            "Who may see this contact: `Public` anyone, `Users` authenticated users only, `Private` the owning organization only. `Private` is no longer accepted on write by the PeeringDB API and remains only on legacy records"
        ),
    )
    name: models.CharField = models.CharField(
        _("Name"),
        max_length=254,
        blank=True,
        help_text=_("Name of the contact, which may be a person or a team"),
    )
    phone: models.CharField = models.CharField(
        _("Phone"), max_length=100, blank=True, help_text=const.PHONE_HELP_TEXT
    )
    email: models.EmailField = models.EmailField(
        _("Email"),
        max_length=254,
        blank=True,
        help_text=_("Email address for this contact"),
    )
    url: URLField = URLField(
        _("URL"), blank=True, help_text=_("Website for this contact")
    )

    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}network_contact"
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    class HandleRef:
        tag = "poc"

    def __str__(self):
        return self.name


class NetworkBase(HandleRefModel):
    asn: ASNField = ASNField(
        verbose_name="ASN",
        unique=True,
        help_text=_(
            "Autonomous System Number for this network. Cannot be changed after creation"
        ),
    )
    name: models.CharField = models.CharField(
        _("Name"),
        max_length=255,
        unique=True,
        help_text=_("Name of the network, unique across PeeringDB"),
    )

    aka: models.CharField = models.CharField(
        _("Also Known As"), max_length=255, blank=True, help_text=const.AKA_HELP_TEXT
    )
    name_long: models.CharField = models.CharField(
        _("Long Name"),
        max_length=255,
        blank=True,
        help_text=const.NAME_LONG_HELP_TEXT,
    )

    irr_as_set: models.CharField = models.CharField(
        _("IRR as-set"),
        max_length=255,
        blank=True,
        help_text=_("Reference to an AS-SET in Internet Routing Registry (IRR)"),
    )
    website: URLField = URLField(
        _("Website"), blank=True, help_text=_("Website of the network")
    )
    social_media = models.JSONField(
        _("Social Media"),
        default=dict,
        blank=True,
        help_text=const.SOCIAL_MEDIA_HELP_TEXT,
    )
    meta = models.JSONField(_("Metadata"), default=dict, blank=True)
    looking_glass: LG_URLField = LG_URLField(
        _("Looking Glass URL"),
        blank=True,
        help_text=_(
            "URL of this network's looking glass. Accepts http, https, telnet and ssh schemes"
        ),
    )
    route_server: LG_URLField = LG_URLField(
        _("Route Server URL"),
        blank=True,
        help_text=_(
            "URL of this network's route server. Accepts http, https, telnet and ssh schemes"
        ),
    )

    notes: models.TextField = models.TextField(
        _("Notes"), blank=True, help_text=const.NOTES_HELP_TEXT
    )
    notes_private: models.TextField = models.TextField(
        _("Private notes"),
        blank=True,
        help_text=_(
            "Notes visible only to administrators of the owning organization. Not exposed via the API"
        ),
    )

    info_traffic: models.CharField = models.CharField(
        _("Traffic Levels"),
        max_length=39,
        blank=True,
        choices=const.TRAFFIC,
        help_text=const.INFO_TRAFFIC_HELP_TEXT,
    )

    info_ratio: models.CharField = models.CharField(
        _("Traffic Ratios"),
        max_length=45,
        blank=True,
        choices=const.RATIOS,
        default="Not Disclosed",
        help_text=_(
            "Self-classified ratio of outbound to inbound traffic for this network"
        ),
    )
    info_scope: models.CharField = models.CharField(
        _("Geographic Scope"),
        max_length=39,
        blank=True,
        choices=const.SCOPES,
        default="Not Disclosed",
        help_text=_("Self-classified geographic reach of this network"),
    )

    info_types: MultipleChoiceField = MultipleChoiceField(
        _("Network Types"),
        blank=True,
        max_length=255,
        choices=const.NET_TYPES_MULTI_CHOICE,
        help_text=_("Self-classified categories describing this network"),
    )

    info_prefixes4: models.PositiveIntegerField = models.PositiveIntegerField(
        _("IPv4 Prefixes"),
        null=True,
        blank=True,
        help_text=_(
            "Recommended maximum number of IPv4 "
            "routes/prefixes to be configured on peering "
            "sessions for this ASN"
        ),
    )
    info_prefixes6: models.PositiveIntegerField = models.PositiveIntegerField(
        _("IPv6 Prefixes"),
        null=True,
        blank=True,
        help_text=_(
            "Recommended maximum number of IPv6 "
            "routes/prefixes to be configured on peering "
            "sessions for this ASN"
        ),
    )
    info_unicast: models.BooleanField = models.BooleanField(
        _("Unicast IPv4"),
        default=False,
        help_text=_("Whether this network supports unicast IPv4"),
    )
    info_multicast: models.BooleanField = models.BooleanField(
        _("Multicast"),
        default=False,
        help_text=_("Whether this network supports multicast"),
    )
    info_ipv6: models.BooleanField = models.BooleanField(
        _("Unicast IPv6"),
        default=False,
        help_text=_("Whether this network supports unicast IPv6"),
    )
    info_never_via_route_servers: models.BooleanField = models.BooleanField(
        _("Never via route servers"),
        default=False,
        help_text=_(
            "Indicates if this network "
            "will announce its routes "
            "via route servers or not"
        ),
    )

    policy_url: URLField = URLField(
        _("Peering Policy"),
        blank=True,
        help_text=_("URL of this network's published peering policy"),
    )
    policy_general: models.CharField = models.CharField(
        _("General Policy"),
        max_length=72,
        blank=True,
        choices=const.POLICY_GENERAL,
        help_text=const.POLICY_GENERAL_HELP_TEXT,
    )
    policy_locations: models.CharField = models.CharField(
        _("Multiple Locations"),
        max_length=72,
        blank=True,
        choices=const.POLICY_LOCATIONS,
        help_text=_(
            "Whether this network requires peering at multiple locations, and in which region"
        ),
    )
    policy_ratio: models.BooleanField = models.BooleanField(
        _("Ratio Requirement"),
        default=False,
        help_text=_("Whether this network enforces a traffic ratio requirement"),
    )
    policy_contracts: models.CharField = models.CharField(
        _("Contract Requirement"),
        max_length=36,
        blank=True,
        choices=const.POLICY_CONTRACTS,
        help_text=_("Whether a signed contract is required to peer with this network"),
    )

    status_dashboard: URLField = URLField(
        _("Status Dashboard"),
        null=True,
        blank=True,
        help_text=_("URL of a public status or outage dashboard for this network"),
    )

    rir_status: models.CharField = models.CharField(
        _("RIR status"),
        null=True,
        default=None,
        max_length=255,
        help_text=_(
            "Allocation status of this network's ASN according to RIR data, refreshed periodically. Read-only; the PeeringDB API exposes only `ok` or `null` here, not the more detailed status kept internally"
        ),
    )
    rir_status_updated: models.DateTimeField = models.DateTimeField(
        _("RIR status updated"),
        blank=True,
        null=True,
        help_text=_("Time `rir_status` was last set. Read-only"),
    )

    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}network"
        verbose_name = _("Network")
        verbose_name_plural = _("Networks")

    class HandleRef:
        tag = "net"
        delete_cascade: ClassVar[list[str]] = ["poc_set", "netfac_set", "netixlan_set"]

    def __str__(self):
        return self.name


class InternetExchangeBase(HandleRefModel):
    name: models.CharField = models.CharField(
        _("Name"),
        max_length=64,
        unique=True,
        help_text=_("Name of the exchange, unique across PeeringDB"),
    )

    aka: models.CharField = models.CharField(
        _("Also Known As"), max_length=255, blank=True, help_text=const.AKA_HELP_TEXT
    )
    name_long: models.CharField = models.CharField(
        _("Long Name"),
        max_length=255,
        blank=True,
        help_text=const.NAME_LONG_HELP_TEXT,
    )

    city: models.CharField = models.CharField(
        _("City"), max_length=192, help_text=_("City this exchange is based in")
    )
    country: CountryField = CountryField(
        _("Country"),
        help_text=_(
            "Two-letter ISO 3166-1 alpha-2 code of the country this exchange is based in"
        ),
    )

    notes: models.TextField = models.TextField(
        _("Notes"), blank=True, help_text=const.NOTES_HELP_TEXT
    )

    region_continent: models.CharField = models.CharField(
        _("Continental Region"),
        max_length=255,
        choices=const.REGIONS,
        help_text=_("Continental region this exchange operates in"),
    )
    media: models.CharField = models.CharField(
        _("Media Type"),
        max_length=128,
        choices=const.MEDIA,
        default="Ethernet",
        help_text=_(
            "Obsolete. The PeeringDB API always reports `Ethernet` here regardless of the stored value; the field is deprecated and no longer describes the physical media offered at the exchange"
        ),
    )
    proto_unicast: models.BooleanField = models.BooleanField(
        _("Unicast IPv4"),
        default=False,
        help_text=_(
            "Whether this exchange supports unicast IPv4. The PeeringDB API does not read this column: it derives the value from the LAN's active IPv4 prefixes and ignores values submitted on create or update"
        ),
    )
    proto_multicast: models.BooleanField = models.BooleanField(
        _("Multicast"),
        default=False,
        help_text=_("Whether this exchange supports multicast"),
    )
    proto_ipv6: models.BooleanField = models.BooleanField(
        _("Unicast IPv6"),
        default=False,
        help_text=_(
            "Whether this exchange supports unicast IPv6. The PeeringDB API does not read this column: it derives the value from the LAN's active IPv6 prefixes and ignores values submitted on create or update"
        ),
    )

    website: URLField = URLField(
        _("Company Website"),
        blank=True,
        default="",
        help_text=_("Website of the exchange"),
    )
    social_media = models.JSONField(
        _("Social Media"),
        default=dict,
        blank=True,
        help_text=const.SOCIAL_MEDIA_HELP_TEXT,
    )
    url_stats: URLField = URLField(
        _("Traffic Stats Website"),
        blank=True,
        help_text=_("URL of public traffic statistics for this exchange"),
    )

    tech_email: models.EmailField = models.EmailField(
        _("Technical Email"),
        max_length=254,
        blank=True,
        help_text=_("Address to send technical questions about this exchange"),
    )
    tech_phone: models.CharField = models.CharField(
        _("Technical Phone"),
        max_length=192,
        blank=True,
        help_text=const.PHONE_HELP_TEXT,
    )
    policy_email: models.EmailField = models.EmailField(
        _("Policy Email"),
        max_length=254,
        blank=True,
        help_text=_("Address to send peering requests for this exchange"),
    )
    policy_phone: models.CharField = models.CharField(
        _("Policy Phone"), max_length=192, blank=True, help_text=const.PHONE_HELP_TEXT
    )

    sales_email: models.EmailField = models.EmailField(
        _("Sales Email"),
        max_length=254,
        blank=True,
        help_text=_("Address to send sales questions about this exchange"),
    )
    sales_phone: models.CharField = models.CharField(
        _("Sales Phone"), max_length=192, blank=True, help_text=const.PHONE_HELP_TEXT
    )

    ixf_net_count: models.IntegerField = models.IntegerField(
        _("IX-F Network Count"),
        default=0,
        help_text=_(
            "Number of networks seen in this exchange's IX-F member export. Read-only"
        ),
    )
    ixf_last_import: models.DateTimeField = models.DateTimeField(
        _("IX-F Last Import"),
        null=True,
        blank=True,
        help_text=_(
            "Time this exchange's IX-F member export was last imported. Read-only"
        ),
    )

    service_level: models.CharField = models.CharField(
        _("Service Level"),
        max_length=60,
        blank=True,
        choices=const.SERVICE_LEVEL_TYPES,
        default="Not Disclosed",
        help_text=_("Level of support this exchange offers its participants"),
    )

    terms: models.CharField = models.CharField(
        _("Terms"),
        max_length=60,
        blank=True,
        choices=const.TERMS_TYPES,
        default="Not Disclosed",
        help_text=_("Commercial terms for participating in this exchange"),
    )

    status_dashboard: URLField = URLField(
        _("Status Dashboard"),
        null=True,
        blank=True,
        help_text=_("URL of a public status or outage dashboard for this exchange"),
    )

    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}ix"
        verbose_name = _("Internet Exchange")
        verbose_name_plural = _("Internet Exchanges")

    class HandleRef:
        tag = "ix"
        delete_cascade: ClassVar[list[str]] = ["ixfac_set", "ixlan_set"]

    def __str__(self):
        return self.name


class InternetExchangeFacilityBase(HandleRefModel):
    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}ix_facility"
        verbose_name = _("Internet Exchange facility")
        verbose_name_plural = _("Internet Exchange facilities")

    class HandleRef:
        tag = "ixfac"


class IXLanBase(HandleRefModel):
    name: models.CharField = models.CharField(
        _("Name"), max_length=255, blank=True, help_text=_("Name of the exchange LAN")
    )
    descr: models.TextField = models.TextField(
        _("Description"), blank=True, help_text=_("Description of the exchange LAN")
    )
    mtu: models.PositiveIntegerField = models.PositiveIntegerField(
        "MTU",
        default=1500,
        choices=const.MTUS,
        help_text=_("Maximum transmission unit offered on this LAN, in bytes"),
    )
    vlan: models.PositiveIntegerField = models.PositiveIntegerField(
        "VLAN",
        null=True,
        blank=True,
        help_text=_("VLAN id for this LAN. Not exposed via the API"),
    )
    dot1q_support: models.BooleanField = models.BooleanField(
        "802.1Q",
        default=False,
        help_text=_(
            "Obsolete. The PeeringDB API always reports `false` here regardless of the stored value; the field is deprecated and no longer describes 802.1Q VLAN tagging support"
        ),
    )
    rs_asn: ASNField = ASNField(
        verbose_name=_("Route Server ASN"),
        null=True,
        blank=True,
        default=0,
        help_text=_("Autonomous System Number of this LAN's route server"),
    )
    arp_sponge: MacAddressField = MacAddressField(
        verbose_name=_("ARP sponging MAC"),
        null=True,
        unique=True,
        blank=True,
        help_text=_("MAC address used by this LAN for ARP sponging"),
    )

    ixf_ixp_member_list_url: models.URLField = models.URLField(
        verbose_name=_("IX-F Member Export URL"),
        null=True,
        blank=True,
        help_text=_("URL of this LAN's IX-F member export feed"),
    )
    ixf_ixp_member_list_url_visible: models.CharField = models.CharField(
        verbose_name=_("IX-F Member Export URL Visibility"),
        max_length=64,
        choices=const.VISIBILITY,
        default="Private",
        help_text=_(
            "Who may see `ixf_ixp_member_list_url`: `Public` anyone, `Users` authenticated users only, `Private` the owning organization only"
        ),
    )

    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}ixlan"
        verbose_name = _("Internet Exchange LAN")
        verbose_name_plural = _("Internet Exchange LANs")

    class HandleRef:
        tag = "ixlan"
        delete_cascade: ClassVar[list[str]] = ["ixpfx_set", "netixlan_set"]


class IXLanPrefixBase(HandleRefModel):
    notes: models.CharField = models.CharField(
        _("Notes"), max_length=255, blank=True, help_text=const.NOTES_HELP_TEXT
    )
    protocol: models.CharField = models.CharField(
        _("Protocol"),
        max_length=64,
        choices=const.PROTOCOLS,
        help_text=_("IP protocol version of this prefix"),
    )
    prefix: IPPrefixField = IPPrefixField(
        verbose_name=_("Prefix"),
        unique=True,
        help_text=_(
            "IP prefix assigned to the exchange LAN, in CIDR notation. Unique across PeeringDB"
        ),
    )
    in_dfz: models.BooleanField = models.BooleanField(
        default=False,
        help_text=_("Whether this prefix is routed in the default-free zone"),
    )

    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}ixlan_prefix"
        verbose_name = _("Internet Exchange LAN prefix")
        verbose_name_plural = _("Internet Exchange LAN prefixes")

    class HandleRef:
        tag = "ixpfx"


class NetworkFacilityBase(HandleRefModel):
    avail_sonet: models.BooleanField = models.BooleanField(
        "SONET",
        default=False,
        help_text=_("Whether SONET is available. Not exposed via the API"),
    )
    avail_ethernet: models.BooleanField = models.BooleanField(
        "Ethernet",
        default=False,
        help_text=_("Whether Ethernet is available. Not exposed via the API"),
    )
    avail_atm: models.BooleanField = models.BooleanField(
        "ATM",
        default=False,
        help_text=_("Whether ATM is available. Not exposed via the API"),
    )

    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}network_facility"
        verbose_name = _("Network Facility")
        verbose_name_plural = _("Network Facilities")

    class HandleRef:
        tag = "netfac"


class NetworkIXLanBase(HandleRefModel):
    asn: ASNField = ASNField(
        verbose_name="ASN",
        help_text=_("Autonomous System Number of the connected network"),
    )
    ipaddr4: IPAddressField = IPAddressField(
        verbose_name="IPv4",
        version=4,
        blank=True,
        null=True,
        help_text=_(
            "IPv4 address of this connection, which must fall within one of the LAN's IPv4 prefixes"
        ),
    )
    ipaddr6: IPAddressField = IPAddressField(
        verbose_name="IPv6",
        version=6,
        blank=True,
        null=True,
        help_text=_(
            "IPv6 address of this connection, which must fall within one of the LAN's IPv6 prefixes"
        ),
    )
    is_rs_peer: models.BooleanField = models.BooleanField(
        _("RS peer"),
        default=False,
        help_text=_("Whether this connection peers with the exchange's route server"),
    )
    bfd_support: models.BooleanField = models.BooleanField(
        _("BFD support"),
        default=False,
        help_text=_(
            "Whether this connection supports Bidirectional Forwarding Detection"
        ),
    )
    notes: models.CharField = models.CharField(
        _("Notes"), max_length=255, blank=True, help_text=const.NOTES_HELP_TEXT
    )
    speed: models.PositiveIntegerField = models.PositiveIntegerField(
        _("Capacity (mbit/sec)"),
        help_text=_("Capacity of this connection in Mbit/sec"),
    )
    operational: models.BooleanField = models.BooleanField(
        _("Operational"),
        default=True,
        help_text=_("Whether this connection is operational"),
    )

    meta = models.JSONField(_("Metadata"), default=dict, blank=True)

    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}network_ixlan"
        verbose_name = _("Public Peering Exchange Point")
        verbose_name_plural = _("Public Peering Exchange Points")

    class HandleRef:
        tag = "netixlan"


class CarrierBase(HandleRefModel):
    name: models.CharField = models.CharField(
        _("Name"),
        max_length=255,
        unique=True,
        help_text=_("Name of the carrier, unique across PeeringDB"),
    )

    aka: models.CharField = models.CharField(
        _("Also Known As"), max_length=255, blank=True, help_text=const.AKA_HELP_TEXT
    )
    name_long: models.CharField = models.CharField(
        _("Long Name"),
        max_length=255,
        blank=True,
        help_text=const.NAME_LONG_HELP_TEXT,
    )

    website: URLField = URLField(
        _("Website"), blank=True, default="", help_text=_("Website of the carrier")
    )
    social_media = models.JSONField(
        _("Social Media"),
        default=dict,
        blank=True,
        help_text=const.SOCIAL_MEDIA_HELP_TEXT,
    )
    notes: models.TextField = models.TextField(
        _("Notes"), blank=True, help_text=const.NOTES_HELP_TEXT
    )

    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}carrier"
        verbose_name = _("Carrier")
        verbose_name_plural = _("Carriers")

    class HandleRef:
        tag = "carrier"
        delete_cascade: ClassVar[list[str]] = ["carrierfac_set"]

    def __str__(self):
        return self.name


class CarrierFacilityBase(HandleRefModel):
    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}carrier_facility"
        verbose_name = _("Carrier presence at facility")
        verbose_name_plural = _("Carrier presences at facility")

    class HandleRef:
        tag = "carrierfac"


class CampusBase(HandleRefModel):
    name: models.CharField = models.CharField(
        _("Campus Name"),
        max_length=255,
        unique=True,
        help_text=_("Name of the campus, unique across PeeringDB"),
    )

    name_long: models.CharField = models.CharField(
        _("Long Name"),
        max_length=255,
        blank=True,
        null=True,
        help_text=const.NAME_LONG_HELP_TEXT,
    )
    aka: models.CharField = models.CharField(
        _("Also Known As"),
        max_length=255,
        blank=True,
        null=True,
        help_text=const.AKA_HELP_TEXT,
    )

    website: URLField = URLField(
        _("Website"), blank=True, default="", help_text=_("Website of the campus")
    )
    social_media = models.JSONField(
        _("Social Media"),
        default=dict,
        blank=True,
        help_text=const.SOCIAL_MEDIA_HELP_TEXT,
    )
    notes: models.TextField = models.TextField(
        _("Notes"), blank=True, help_text=const.NOTES_HELP_TEXT
    )

    class Meta:
        abstract = True
        db_table = f"{settings.TABLE_PREFIX}campus"
        verbose_name = _("Campus")
        verbose_name_plural = _("Campuses")

    class HandleRef:
        tag = "campus"

    def __str__(self):
        return self.name
