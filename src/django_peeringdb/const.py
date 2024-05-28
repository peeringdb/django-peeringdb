from django.utils.translation import gettext_lazy as _

MEDIA = (("Ethernet", _("Ethernet")), ("ATM", _("ATM")), ("Multiple", _("Multiple")))

POC_ROLES = (
    ("Abuse", _("Abuse")),
    ("Maintenance", _("Maintenance")),
    ("Policy", _("Policy")),
    ("Technical", _("Technical")),
    ("NOC", _("NOC")),
    ("Public Relations", _("Public Relations")),
    ("Sales", _("Sales")),
)

POLICY_GENERAL = (
    ("Open", _("Open")),
    ("Selective", _("Selective")),
    ("Restrictive", _("Restrictive")),
    ("No", _("No")),
)

POLICY_LOCATIONS = (
    ("Not Required", _("Not Required")),
    ("Preferred", _("Preferred")),
    ("Required - US", _("Required - US")),
    ("Required - EU", _("Required - EU")),
    ("Required - International", _("Required - International")),
)

POLICY_CONTRACTS = (
    ("Not Required", _("Not Required")),
    ("Private Only", _("Private Only")),
    ("Required", _("Required")),
)

PROTOCOLS = (
    ("IPv4", _("IPv4")),
    ("IPv6", _("IPv6")),
)

MTUS = (
    (1500, "1500"),
    (9000, "9000"),
)

RATIOS = (
    ("", _("Not Disclosed")),
    ("Not Disclosed", _("Not Disclosed")),
    ("Heavy Outbound", _("Heavy Outbound")),
    ("Mostly Outbound", _("Mostly Outbound")),
    ("Balanced", _("Balanced")),
    ("Mostly Inbound", _("Mostly Inbound")),
    ("Heavy Inbound", _("Heavy Inbound")),
)

REGIONS = (
    ("North America", _("North America")),
    ("Asia Pacific", _("Asia Pacific")),
    ("Europe", _("Europe")),
    ("South America", _("South America")),
    ("Africa", _("Africa")),
    ("Australia", _("Australia")),
    ("Middle East", _("Middle East")),
)

SCOPES = (
    ("", _("Not Disclosed")),
    ("Not Disclosed", _("Not Disclosed")),
    ("Regional", _("Regional")),
    ("North America", _("North America")),
    ("Asia Pacific", _("Asia Pacific")),
    ("Europe", _("Europe")),
    ("South America", _("South America")),
    ("Africa", _("Africa")),
    ("Australia", _("Australia")),
    ("Middle East", _("Middle East")),
    ("Global", _("Global")),
)

TRAFFIC = (
    ("", _("Not Disclosed")),
    ("0-20Mbps", _("0-20Mbps")),
    ("20-100Mbps", _("20-100Mbps")),
    ("100-1000Mbps", _("100-1000Mbps")),
    ("1-5Gbps", _("1-5Gbps")),
    ("5-10Gbps", _("5-10Gbps")),
    ("10-20Gbps", _("10-20Gbps")),
    ("20-50Gbps", _("20-50Gbps")),
    ("50-100Gbps", _("50-100Gbps")),
    ("100-200Gbps", _("100-200Gbps")),
    ("200-300Gbps", _("200-300Gbps")),
    ("300-500Gbps", _("300-500Gbps")),
    ("500-1000Gbps", _("500-1000Gbps")),
    ("1-5Tbps", _("1-5Tbps")),
    ("5-10Tbps", _("5-10Tbps")),
    ("10-20Tbps", _("10-20Tbps")),
    ("20-50Tbps", _("20-50Tbps")),
    ("50-100Tbps", _("50-100Tbps")),
    ("100+Tbps", _("100+Tbps")),
)


_NET_TYPES = (
    ("NSP", _("NSP")),
    ("Content", _("Content")),
    ("Cable/DSL/ISP", _("Cable/DSL/ISP")),
    ("Enterprise", _("Enterprise")),
    ("Educational/Research", _("Educational/Research")),
    ("Non-Profit", _("Non-Profit")),
    ("Route Server", _("Route Server")),
    ("Network Services", _("Network Services")),
    ("Route Collector", _("Route Collector")),
    ("Government", _("Government")),
)

NET_TYPES = (
    ("", _("Not Disclosed")),
    ("Not Disclosed", _("Not Disclosed")),
) + _NET_TYPES

NET_TYPES_MULTI_CHOICE = _NET_TYPES

VISIBILITY = (
    ("Private", _("Private")),
    #                   ('Peers', _('Peers')),
    ("Users", _("Users")),
    ("Public", _("Public")),
)


PHONE_HELP_TEXT = _(
    "An E.164-formatted phone number starts with a +, "
    "followed by the country code, then the national phone number "
    "(dropping the leading 0 in most countries), without spaces "
    "or dashes between the groups of digits"
)

INFO_TRAFFIC_HELP_TEXT = _("Total, self-classified traffic in/out to this network.")

WEBSITE_OVERRIDE_HELP_TEXT = _(
    "If this field is set, it will be displayed on this record. "
    "If not, we will display the website from the organization "
    "record this is tied to"
)

CARRIER_HELP_TEXT = _("Provider of L1 or L2 connectivity into a facility")

CAMPUS_HELP_TEXT = _(
    "A set of facilities under one management, with inter-building cross-connects"
)

POLICY_GENERAL_HELP_TEXT = _(
    "Peering with the routeserver and BFD support is shown with an icon"
)

SERVICE_LEVEL_TYPES = (
    ("", _("Not Disclosed")),
    ("Not Disclosed", _("Not Disclosed")),
    ("Best Effort (no SLA)", _("Best Effort (no SLA)")),
    ("Normal Business Hours", _("Normal Business Hours")),
    ("24/7 Support", _("24/7 Support")),
)

TERMS_TYPES = (
    ("", _("Not Disclosed")),
    ("Not Disclosed", _("Not Disclosed")),
    ("No Commercial Terms", _("No Commercial Terms")),
    ("Bundled With Other Services", _("Bundled With Other Services")),
    ("Non-recurring Fees Only", _("Non-recurring Fees Only")),
    ("Recurring Fees", _("Recurring Fees")),
)

PROPERTY = (
    ("", _("Not Disclosed")),
    ("Owner", _("Owner")),
    ("Lessee", _("Leased or Rented")),
)

AVAILABLE_VOLTAGE = (
    ("48 VDC", _("48 VDC")),
    ("400 VAC", _("400 VAC")),
    ("480 VAC", _("480 VAC")),
)

SOCIAL_MEDIA_SERVICES = [
    ("website", _("Website")),
    ("facebook", _("Facebook")),
    ("x", _("X")),
    ("instagram", _("Instagram")),
    ("linkedin", _("LinkedIn")),
    ("tiktok", _("TikTok")),
]

REGION_MAPPING = [
    {
        "code": "AD",
        "continent": "Europe",
    },
    {
        "code": "AF",
        "continent": "Asia Pacific",
    },
    {
        "code": "AG",
        "continent": "North America",
    },
    {
        "code": "AL",
        "continent": "Europe",
    },
    {
        "code": "AM",
        "continent": "Asia Pacific",
    },
    {
        "code": "AO",
        "continent": "Africa",
    },
    {
        "code": "AR",
        "continent": "South America",
    },
    {
        "code": "AT",
        "continent": "Europe",
    },
    {
        "code": "AU",
        "continent": "Australia",
    },
    {
        "code": "AZ",
        "continent": "Asia Pacific",
    },
    {
        "code": "BB",
        "continent": "North America",
    },
    {
        "code": "BD",
        "continent": "Asia Pacific",
    },
    {
        "code": "BE",
        "continent": "Europe",
    },
    {
        "code": "BF",
        "continent": "Africa",
    },
    {
        "code": "BG",
        "continent": "Europe",
    },
    {
        "code": "BH",
        "continent": "Middle East",
    },
    {
        "code": "BI",
        "continent": "Africa",
    },
    {
        "code": "BJ",
        "continent": "Africa",
    },
    {
        "code": "BN",
        "continent": "Asia Pacific",
    },
    {
        "code": "BO",
        "continent": "South America",
    },
    {
        "code": "BR",
        "continent": "South America",
    },
    {
        "code": "BS",
        "continent": "North America",
    },
    {
        "code": "BT",
        "continent": "Asia Pacific",
    },
    {
        "code": "BW",
        "continent": "Africa",
    },
    {
        "code": "BY",
        "continent": "Europe",
    },
    {
        "code": "BZ",
        "continent": "North America",
    },
    {
        "code": "CA",
        "continent": "North America",
    },
    {
        "code": "CD",
        "continent": "Africa",
    },
    {
        "code": "CG",
        "continent": "Africa",
    },
    {
        "code": "CI",
        "continent": "Africa",
    },
    {
        "code": "CL",
        "continent": "South America",
    },
    {
        "code": "CM",
        "continent": "Africa",
    },
    {
        "code": "CN",
        "continent": "Asia Pacific",
    },
    {
        "code": "CO",
        "continent": "South America",
    },
    {
        "code": "CR",
        "continent": "North America",
    },
    {
        "code": "CU",
        "continent": "North America",
    },
    {
        "code": "CV",
        "continent": "Africa",
    },
    {
        "code": "CY",
        "continent": "Middle East",
    },
    {
        "code": "CZ",
        "continent": "Europe",
    },
    {
        "code": "DE",
        "continent": "Europe",
    },
    {
        "code": "DJ",
        "continent": "Africa",
    },
    {
        "code": "DK",
        "continent": "Europe",
    },
    {
        "code": "DM",
        "continent": "North America",
    },
    {
        "code": "DO",
        "continent": "North America",
    },
    {
        "code": "EC",
        "continent": "South America",
    },
    {
        "code": "EE",
        "continent": "Europe",
    },
    {
        "code": "EG",
        "continent": "Middle East",
    },
    {
        "code": "ER",
        "continent": "Africa",
    },
    {
        "code": "ET",
        "continent": "Africa",
    },
    {
        "code": "FI",
        "continent": "Europe",
    },
    {
        "code": "FJ",
        "continent": "Asia Pacific",
    },
    {
        "code": "FR",
        "continent": "Europe",
    },
    {
        "code": "GA",
        "continent": "Africa",
    },
    {
        "code": "GE",
        "continent": "Asia Pacific",
    },
    {
        "code": "GH",
        "continent": "Africa",
    },
    {
        "code": "GM",
        "continent": "Africa",
    },
    {
        "code": "GN",
        "continent": "Africa",
    },
    {
        "code": "GR",
        "continent": "Europe",
    },
    {
        "code": "GT",
        "continent": "North America",
    },
    {
        "code": "HT",
        "continent": "North America",
    },
    {
        "code": "GW",
        "continent": "Africa",
    },
    {
        "code": "GY",
        "continent": "South America",
    },
    {
        "code": "HN",
        "continent": "North America",
    },
    {
        "code": "HU",
        "continent": "Europe",
    },
    {
        "code": "ID",
        "continent": "Asia Pacific",
    },
    {
        "code": "IE",
        "continent": "Europe",
    },
    {
        "code": "IL",
        "continent": "Middle East",
    },
    {
        "code": "IN",
        "continent": "Asia Pacific",
    },
    {
        "code": "IQ",
        "continent": "Middle East",
    },
    {
        "code": "IR",
        "continent": "Middle East",
    },
    {
        "code": "IS",
        "continent": "Europe",
    },
    {
        "code": "IT",
        "continent": "Europe",
    },
    {
        "code": "JM",
        "continent": "North America",
    },
    {
        "code": "JO",
        "continent": "Middle East",
    },
    {
        "code": "JP",
        "continent": "Asia Pacific",
    },
    {
        "code": "KE",
        "continent": "Africa",
    },
    {
        "code": "KG",
        "continent": "Asia Pacific",
    },
    {
        "code": "KI",
        "continent": "Asia Pacific",
    },
    {
        "code": "KP",
        "continent": "Asia Pacific",
    },
    {
        "code": "KR",
        "continent": "Asia Pacific",
    },
    {
        "code": "KW",
        "continent": "Middle East",
    },
    {
        "code": "LB",
        "continent": "Middle East",
    },
    {
        "code": "LI",
        "continent": "Europe",
    },
    {
        "code": "LR",
        "continent": "Africa",
    },
    {
        "code": "LS",
        "continent": "Africa",
    },
    {
        "code": "LT",
        "continent": "Europe",
    },
    {
        "code": "LU",
        "continent": "Europe",
    },
    {
        "code": "LV",
        "continent": "Europe",
    },
    {
        "code": "LY",
        "continent": "Africa",
    },
    {
        "code": "MG",
        "continent": "Africa",
    },
    {
        "code": "MH",
        "continent": "Asia Pacific",
    },
    {
        "code": "MK",
        "continent": "Europe",
    },
    {
        "code": "ML",
        "continent": "Africa",
    },
    {
        "code": "MM",
        "continent": "Asia Pacific",
    },
    {
        "code": "MN",
        "continent": "Asia Pacific",
    },
    {
        "code": "MR",
        "continent": "Africa",
    },
    {
        "code": "MT",
        "continent": "Europe",
    },
    {
        "code": "MU",
        "continent": "Africa",
    },
    {
        "code": "MV",
        "continent": "Asia Pacific",
    },
    {
        "code": "MW",
        "continent": "Africa",
    },
    {
        "code": "MX",
        "continent": "North America",
    },
    {
        "code": "MY",
        "continent": "Asia Pacific",
    },
    {
        "code": "MZ",
        "continent": "Africa",
    },
    {
        "code": "NA",
        "continent": "Africa",
    },
    {
        "code": "NE",
        "continent": "Africa",
    },
    {
        "code": "NG",
        "continent": "Africa",
    },
    {
        "code": "NI",
        "continent": "North America",
    },
    {
        "code": "NL",
        "continent": "Europe",
    },
    {
        "code": "NO",
        "continent": "Europe",
    },
    {
        "code": "NP",
        "continent": "Asia Pacific",
    },
    {
        "code": "NR",
        "continent": "Asia Pacific",
    },
    {
        "code": "NZ",
        "continent": "Asia Pacific",
    },
    {
        "code": "OM",
        "continent": "Middle East",
    },
    {
        "code": "PA",
        "continent": "North America",
    },
    {
        "code": "PE",
        "continent": "South America",
    },
    {
        "code": "PG",
        "continent": "Asia Pacific",
    },
    {
        "code": "PH",
        "continent": "Asia Pacific",
    },
    {
        "code": "PK",
        "continent": "Asia Pacific",
    },
    {
        "code": "PL",
        "continent": "Europe",
    },
    {
        "code": "PT",
        "continent": "Europe",
    },
    {
        "code": "PW",
        "continent": "Asia Pacific",
    },
    {
        "code": "PY",
        "continent": "South America",
    },
    {
        "code": "QA",
        "continent": "Middle East",
    },
    {
        "code": "RO",
        "continent": "Europe",
    },
    {
        "code": "RU",
        "continent": "Europe",
    },
    {
        "code": "RW",
        "continent": "Africa",
    },
    {
        "code": "SA",
        "continent": "Middle East",
    },
    {
        "code": "SB",
        "continent": "Asia Pacific",
    },
    {
        "code": "SC",
        "continent": "Africa",
    },
    {
        "code": "SD",
        "continent": "Africa",
    },
    {
        "code": "SE",
        "continent": "Europe",
    },
    {
        "code": "SG",
        "continent": "Asia Pacific",
    },
    {
        "code": "SI",
        "continent": "Europe",
    },
    {
        "code": "SK",
        "continent": "Europe",
    },
    {
        "code": "SL",
        "continent": "Africa",
    },
    {
        "code": "SM",
        "continent": "Europe",
    },
    {
        "code": "SN",
        "continent": "Africa",
    },
    {
        "code": "SO",
        "continent": "Africa",
    },
    {
        "code": "SR",
        "continent": "South America",
    },
    {
        "code": "ST",
        "continent": "Africa",
    },
    {
        "code": "SY",
        "continent": "Middle East",
    },
    {
        "code": "TG",
        "continent": "Africa",
    },
    {
        "code": "TH",
        "continent": "Asia Pacific",
    },
    {
        "code": "TJ",
        "continent": "Asia Pacific",
    },
    {
        "code": "TM",
        "continent": "Asia Pacific",
    },
    {
        "code": "TN",
        "continent": "Africa",
    },
    {
        "code": "TO",
        "continent": "Asia Pacific",
    },
    {
        "code": "TR",
        "continent": "Middle East",
    },
    {
        "code": "TT",
        "continent": "North America",
    },
    {
        "code": "TV",
        "continent": "Asia Pacific",
    },
    {
        "code": "TZ",
        "continent": "Africa",
    },
    {
        "code": "UA",
        "continent": "Europe",
    },
    {
        "code": "UG",
        "continent": "Africa",
    },
    {
        "code": "US",
        "continent": "North America",
    },
    {
        "code": "UY",
        "continent": "South America",
    },
    {
        "code": "UZ",
        "continent": "Asia Pacific",
    },
    {
        "code": "VA",
        "continent": "Europe",
    },
    {
        "code": "VE",
        "continent": "South America",
    },
    {
        "code": "VN",
        "continent": "Asia Pacific",
    },
    {
        "code": "VU",
        "continent": "Asia Pacific",
    },
    {
        "code": "YE",
        "continent": "Middle East",
    },
    {
        "code": "ZM",
        "continent": "Africa",
    },
    {
        "code": "ZW",
        "continent": "Africa",
    },
    {
        "code": "DZ",
        "continent": "Africa",
    },
    {
        "code": "BA",
        "continent": "Europe",
    },
    {
        "code": "KH",
        "continent": "Asia Pacific",
    },
    {
        "code": "CF",
        "continent": "Africa",
    },
    {
        "code": "TD",
        "continent": "Africa",
    },
    {
        "code": "KM",
        "continent": "Africa",
    },
    {
        "code": "HR",
        "continent": "Europe",
    },
    {
        "code": "TL",
        "continent": "Asia Pacific",
    },
    {
        "code": "SV",
        "continent": "North America",
    },
    {
        "code": "GQ",
        "continent": "Africa",
    },
    {
        "code": "GD",
        "continent": "North America",
    },
    {
        "code": "KZ",
        "continent": "Asia Pacific",
    },
    {
        "code": "LA",
        "continent": "Asia Pacific",
    },
    {
        "code": "FM",
        "continent": "Asia Pacific",
    },
    {
        "code": "MD",
        "continent": "Europe",
    },
    {
        "code": "MC",
        "continent": "Europe",
    },
    {
        "code": "ME",
        "continent": "Europe",
    },
    {
        "code": "MA",
        "continent": "Africa",
    },
    {
        "code": "KN",
        "continent": "North America",
    },
    {
        "code": "LC",
        "continent": "North America",
    },
    {
        "code": "VC",
        "continent": "North America",
    },
    {
        "code": "WS",
        "continent": "Asia Pacific",
    },
    {
        "code": "RS",
        "continent": "Europe",
    },
    {
        "code": "ZA",
        "continent": "Africa",
    },
    {
        "code": "ES",
        "continent": "Europe",
    },
    {
        "code": "LK",
        "continent": "Asia Pacific",
    },
    {
        "code": "SZ",
        "continent": "Africa",
    },
    {
        "code": "CH",
        "continent": "Europe",
    },
    {
        "code": "AE",
        "continent": "Middle East",
    },
    {
        "code": "GB",
        "continent": "Europe",
    },
    {
        "code": "TW",
        "continent": "Asia Pacific",
    },
    {
        "code": "HK",
        "continent": "Asia Pacific",
    },
    {
        "code": "XK",
        "continent": "Europe",
    },
    {
        "code": "PR",
        "continent": "North America",
    },
]
