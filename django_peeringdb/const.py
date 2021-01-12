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

NET_TYPES = (
    ("", _("Not Disclosed")),
    ("Not Disclosed", _("Not Disclosed")),
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
