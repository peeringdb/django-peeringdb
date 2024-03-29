# Generated by Django 3.2.7 on 2023-08-04 14:14

import django.core.validators
import django.db.models.deletion
import django_countries.fields
import django_inet.models
from django.db import migrations, models

import django_peeringdb.models.abstract


class Migration(migrations.Migration):
    dependencies = [
        ("django_peeringdb", "0026_add_social_media"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="facility",
            options={"verbose_name": "Facility", "verbose_name_plural": "Facilities"},
        ),
        migrations.AlterModelOptions(
            name="internetexchange",
            options={
                "verbose_name": "Internet Exchange",
                "verbose_name_plural": "Internet Exchanges",
            },
        ),
        migrations.AlterModelOptions(
            name="internetexchangefacility",
            options={
                "verbose_name": "Internet Exchange facility",
                "verbose_name_plural": "Internet Exchange facilities",
            },
        ),
        migrations.AlterModelOptions(
            name="ixlan",
            options={
                "verbose_name": "Internet Exchange LAN",
                "verbose_name_plural": "Internet Exchange LANs",
            },
        ),
        migrations.AlterModelOptions(
            name="ixlanprefix",
            options={
                "verbose_name": "Internet Exchange LAN prefix",
                "verbose_name_plural": "Internet Exchange LAN prefixes",
            },
        ),
        migrations.AlterModelOptions(
            name="network",
            options={"verbose_name": "Network", "verbose_name_plural": "Networks"},
        ),
        migrations.AlterModelOptions(
            name="networkcontact",
            options={"verbose_name": "Contact", "verbose_name_plural": "Contacts"},
        ),
        migrations.AlterModelOptions(
            name="networkfacility",
            options={
                "verbose_name": "Network Facility",
                "verbose_name_plural": "Network Facilities",
            },
        ),
        migrations.AlterModelOptions(
            name="networkixlan",
            options={
                "verbose_name": "Public Peering Exchange Point",
                "verbose_name_plural": "Public Peering Exchange Points",
            },
        ),
        migrations.AlterModelOptions(
            name="organization",
            options={
                "verbose_name": "Organization",
                "verbose_name_plural": "Organizations",
            },
        ),
        migrations.AlterField(
            model_name="campus",
            name="website",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, default="", max_length=255, verbose_name="Website"
            ),
        ),
        migrations.AlterField(
            model_name="carrier",
            name="website",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, default="", max_length=255, verbose_name="Website"
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="address1",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Address 1"
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="address2",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Address 2"
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="city",
            field=models.CharField(blank=True, max_length=255, verbose_name="City"),
        ),
        migrations.AlterField(
            model_name="facility",
            name="clli",
            field=models.CharField(blank=True, max_length=18, verbose_name="CLLI Code"),
        ),
        migrations.AlterField(
            model_name="facility",
            name="country",
            field=django_countries.fields.CountryField(
                blank=True, max_length=2, verbose_name="Country"
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="latitude",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                max_digits=9,
                null=True,
                verbose_name="Latitude",
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="longitude",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                max_digits=9,
                null=True,
                verbose_name="Longitude",
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="name",
            field=models.CharField(max_length=255, unique=True, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="facility",
            name="notes",
            field=models.TextField(blank=True, verbose_name="Notes"),
        ),
        migrations.AlterField(
            model_name="facility",
            name="npanxx",
            field=models.CharField(blank=True, max_length=21, verbose_name="NPA-NXX"),
        ),
        migrations.AlterField(
            model_name="facility",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fac_set",
                to="django_peeringdb.organization",
                verbose_name="Organization",
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="rencode",
            field=models.CharField(blank=True, max_length=18, verbose_name="Rencode"),
        ),
        migrations.AlterField(
            model_name="facility",
            name="sales_email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="Sales Email"
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="state",
            field=models.CharField(blank=True, max_length=255, verbose_name="State"),
        ),
        migrations.AlterField(
            model_name="facility",
            name="tech_email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="Technical Email"
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="website",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, verbose_name="Website"
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="zipcode",
            field=models.CharField(blank=True, max_length=48, verbose_name="Zip-Code"),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="city",
            field=models.CharField(max_length=192, verbose_name="City"),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="country",
            field=django_countries.fields.CountryField(
                max_length=2, verbose_name="Country"
            ),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="media",
            field=models.CharField(
                choices=[
                    ("Ethernet", "Ethernet"),
                    ("ATM", "ATM"),
                    ("Multiple", "Multiple"),
                ],
                max_length=128,
                verbose_name="Media Type",
            ),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="name",
            field=models.CharField(max_length=64, unique=True, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="notes",
            field=models.TextField(blank=True, verbose_name="Notes"),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ix_set",
                to="django_peeringdb.organization",
                verbose_name="Organization",
            ),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="policy_email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="Policy Email"
            ),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="proto_ipv6",
            field=models.BooleanField(default=False, verbose_name="Unicast IPv6"),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="proto_multicast",
            field=models.BooleanField(default=False, verbose_name="Multicast"),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="proto_unicast",
            field=models.BooleanField(default=False, verbose_name="Unicast IPv4"),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="region_continent",
            field=models.CharField(
                choices=[
                    ("North America", "North America"),
                    ("Asia Pacific", "Asia Pacific"),
                    ("Europe", "Europe"),
                    ("South America", "South America"),
                    ("Africa", "Africa"),
                    ("Australia", "Australia"),
                    ("Middle East", "Middle East"),
                ],
                max_length=255,
                verbose_name="Continental Region",
            ),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="tech_email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="Technical Email"
            ),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="url_stats",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, verbose_name="Traffic Stats Website"
            ),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="website",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, default="", max_length=255, verbose_name="Company Website"
            ),
        ),
        migrations.AlterField(
            model_name="internetexchangefacility",
            name="fac",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ixfac_set",
                to="django_peeringdb.facility",
                verbose_name="Facility",
            ),
        ),
        migrations.AlterField(
            model_name="internetexchangefacility",
            name="ix",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ixfac_set",
                to="django_peeringdb.internetexchange",
                verbose_name="Internet Exchange",
            ),
        ),
        migrations.AlterField(
            model_name="ixlan",
            name="arp_sponge",
            field=django_inet.models.MacAddressField(
                blank=True,
                max_length=17,
                null=True,
                unique=True,
                verbose_name="ARP sponging MAC",
            ),
        ),
        migrations.AlterField(
            model_name="ixlan",
            name="descr",
            field=models.TextField(blank=True, verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="ixlan",
            name="dot1q_support",
            field=models.BooleanField(default=False, verbose_name="802.1Q"),
        ),
        migrations.AlterField(
            model_name="ixlan",
            name="ix",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ixlan_set",
                to="django_peeringdb.internetexchange",
                verbose_name="Internet Exchange",
            ),
        ),
        migrations.AlterField(
            model_name="ixlan",
            name="name",
            field=models.CharField(blank=True, max_length=255, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="ixlan",
            name="rs_asn",
            field=django_inet.models.ASNField(
                blank=True,
                default=0,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="Route Server ASN",
            ),
        ),
        migrations.AlterField(
            model_name="ixlan",
            name="vlan",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="VLAN"
            ),
        ),
        migrations.AlterField(
            model_name="ixlanprefix",
            name="ixlan",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ixpfx_set",
                to="django_peeringdb.ixlan",
                verbose_name="Internet Exchange LAN",
            ),
        ),
        migrations.AlterField(
            model_name="ixlanprefix",
            name="notes",
            field=models.CharField(blank=True, max_length=255, verbose_name="Notes"),
        ),
        migrations.AlterField(
            model_name="ixlanprefix",
            name="prefix",
            field=django_inet.models.IPNetworkField(
                max_length=43, unique=True, verbose_name="Prefix"
            ),
        ),
        migrations.AlterField(
            model_name="ixlanprefix",
            name="protocol",
            field=models.CharField(
                choices=[("IPv4", "IPv4"), ("IPv6", "IPv6")],
                max_length=64,
                verbose_name="Protocol",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="aka",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Also Known As"
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="asn",
            field=django_inet.models.ASNField(
                unique=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="ASN",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_ipv6",
            field=models.BooleanField(default=False, verbose_name="Unicast IPv6"),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_multicast",
            field=models.BooleanField(default=False, verbose_name="Multicast"),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_never_via_route_servers",
            field=models.BooleanField(
                default=False,
                help_text="Indicates if this network will announce its routes via route servers or not",
                verbose_name="Never via route servers",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_ratio",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Not Disclosed", "Not Disclosed"),
                    ("Heavy Outbound", "Heavy Outbound"),
                    ("Mostly Outbound", "Mostly Outbound"),
                    ("Balanced", "Balanced"),
                    ("Mostly Inbound", "Mostly Inbound"),
                    ("Heavy Inbound", "Heavy Inbound"),
                ],
                default="Not Disclosed",
                max_length=45,
                verbose_name="Traffic Ratios",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_scope",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Not Disclosed", "Not Disclosed"),
                    ("Regional", "Regional"),
                    ("North America", "North America"),
                    ("Asia Pacific", "Asia Pacific"),
                    ("Europe", "Europe"),
                    ("South America", "South America"),
                    ("Africa", "Africa"),
                    ("Australia", "Australia"),
                    ("Middle East", "Middle East"),
                    ("Global", "Global"),
                ],
                default="Not Disclosed",
                max_length=39,
                verbose_name="Geographic Scope",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_traffic",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("0-20Mbps", "0-20Mbps"),
                    ("20-100Mbps", "20-100Mbps"),
                    ("100-1000Mbps", "100-1000Mbps"),
                    ("1-5Gbps", "1-5Gbps"),
                    ("5-10Gbps", "5-10Gbps"),
                    ("10-20Gbps", "10-20Gbps"),
                    ("20-50Gbps", "20-50Gbps"),
                    ("50-100Gbps", "50-100Gbps"),
                    ("100-200Gbps", "100-200Gbps"),
                    ("200-300Gbps", "200-300Gbps"),
                    ("300-500Gbps", "300-500Gbps"),
                    ("500-1000Gbps", "500-1000Gbps"),
                    ("1-5Tbps", "1-5Tbps"),
                    ("5-10Tbps", "5-10Tbps"),
                    ("10-20Tbps", "10-20Tbps"),
                    ("20-50Tbps", "20-50Tbps"),
                    ("50-100Tbps", "50-100Tbps"),
                    ("100+Tbps", "100+Tbps"),
                ],
                max_length=39,
                verbose_name="Traffic Levels",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_unicast",
            field=models.BooleanField(default=False, verbose_name="Unicast IPv4"),
        ),
        migrations.AlterField(
            model_name="network",
            name="irr_as_set",
            field=models.CharField(
                blank=True,
                help_text="Reference to an AS-SET or ROUTE-SET in Internet Routing Registry (IRR)",
                max_length=255,
                verbose_name="IRR as-set/route-set",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="looking_glass",
            field=django_peeringdb.models.abstract.LG_URLField(
                blank=True, max_length=255, verbose_name="Looking Glass URL"
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="name",
            field=models.CharField(max_length=255, unique=True, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="network",
            name="notes",
            field=models.TextField(blank=True, verbose_name="Notes"),
        ),
        migrations.AlterField(
            model_name="network",
            name="notes_private",
            field=models.TextField(blank=True, verbose_name="Private notes"),
        ),
        migrations.AlterField(
            model_name="network",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="net_set",
                to="django_peeringdb.organization",
                verbose_name="Organization",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="policy_contracts",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Not Required", "Not Required"),
                    ("Private Only", "Private Only"),
                    ("Required", "Required"),
                ],
                max_length=36,
                verbose_name="Contract Requirement",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="policy_general",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Open", "Open"),
                    ("Selective", "Selective"),
                    ("Restrictive", "Restrictive"),
                    ("No", "No"),
                ],
                help_text="Peering with the routeserver is shown with an icon",
                max_length=72,
                verbose_name="General Policy",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="policy_locations",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Not Required", "Not Required"),
                    ("Preferred", "Preferred"),
                    ("Required - US", "Required - US"),
                    ("Required - EU", "Required - EU"),
                    ("Required - International", "Required - International"),
                ],
                max_length=72,
                verbose_name="Multiple Locations",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="policy_ratio",
            field=models.BooleanField(default=False, verbose_name="Ratio Requirement"),
        ),
        migrations.AlterField(
            model_name="network",
            name="policy_url",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, verbose_name="Peering Policy"
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="route_server",
            field=django_peeringdb.models.abstract.LG_URLField(
                blank=True, max_length=255, verbose_name="Route Server URL"
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="website",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, verbose_name="Website"
            ),
        ),
        migrations.AlterField(
            model_name="networkcontact",
            name="email",
            field=models.EmailField(blank=True, max_length=254, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="networkcontact",
            name="name",
            field=models.CharField(blank=True, max_length=254, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="networkcontact",
            name="net",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="poc_set",
                to="django_peeringdb.network",
                verbose_name="Network",
            ),
        ),
        migrations.AlterField(
            model_name="networkcontact",
            name="role",
            field=models.CharField(
                choices=[
                    ("Abuse", "Abuse"),
                    ("Maintenance", "Maintenance"),
                    ("Policy", "Policy"),
                    ("Technical", "Technical"),
                    ("NOC", "NOC"),
                    ("Public Relations", "Public Relations"),
                    ("Sales", "Sales"),
                ],
                max_length=27,
                verbose_name="Role",
            ),
        ),
        migrations.AlterField(
            model_name="networkcontact",
            name="url",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, verbose_name="URL"
            ),
        ),
        migrations.AlterField(
            model_name="networkcontact",
            name="visible",
            field=models.CharField(
                choices=[
                    ("Private", "Private"),
                    ("Users", "Users"),
                    ("Public", "Public"),
                ],
                default="Public",
                max_length=64,
                verbose_name="Visibility",
            ),
        ),
        migrations.AlterField(
            model_name="networkfacility",
            name="avail_atm",
            field=models.BooleanField(default=False, verbose_name="ATM"),
        ),
        migrations.AlterField(
            model_name="networkfacility",
            name="avail_ethernet",
            field=models.BooleanField(default=False, verbose_name="Ethernet"),
        ),
        migrations.AlterField(
            model_name="networkfacility",
            name="avail_sonet",
            field=models.BooleanField(default=False, verbose_name="SONET"),
        ),
        migrations.AlterField(
            model_name="networkfacility",
            name="fac",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="netfac_set",
                to="django_peeringdb.facility",
                verbose_name="Facility",
            ),
        ),
        migrations.AlterField(
            model_name="networkfacility",
            name="local_asn",
            field=django_inet.models.ASNField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="Local ASN",
            ),
        ),
        migrations.AlterField(
            model_name="networkfacility",
            name="net",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="netfac_set",
                to="django_peeringdb.network",
                verbose_name="Network",
            ),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="asn",
            field=django_inet.models.ASNField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="ASN",
            ),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="ipaddr4",
            field=django_inet.models.IPAddressField(
                blank=True, max_length=39, null=True, verbose_name="IPv4"
            ),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="ipaddr6",
            field=django_inet.models.IPAddressField(
                blank=True, max_length=39, null=True, verbose_name="IPv6"
            ),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="is_rs_peer",
            field=models.BooleanField(default=False, verbose_name="RS peer"),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="ixlan",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="netixlan_set",
                to="django_peeringdb.ixlan",
                verbose_name="Internet Exchange LAN",
            ),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="net",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="netixlan_set",
                to="django_peeringdb.network",
                verbose_name="Network",
            ),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="notes",
            field=models.CharField(blank=True, max_length=255, verbose_name="Notes"),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="operational",
            field=models.BooleanField(default=True, verbose_name="Operational"),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="speed",
            field=models.PositiveIntegerField(verbose_name="Speed (mbit/sec)"),
        ),
        migrations.AlterField(
            model_name="organization",
            name="address1",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Address 1"
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="address2",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Address 2"
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="city",
            field=models.CharField(blank=True, max_length=255, verbose_name="City"),
        ),
        migrations.AlterField(
            model_name="organization",
            name="country",
            field=django_countries.fields.CountryField(
                blank=True, max_length=2, verbose_name="Country"
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="latitude",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                max_digits=9,
                null=True,
                verbose_name="Latitude",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="longitude",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                max_digits=9,
                null=True,
                verbose_name="Longitude",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="name",
            field=models.CharField(max_length=255, unique=True, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="organization",
            name="notes",
            field=models.TextField(blank=True, verbose_name="Notes"),
        ),
        migrations.AlterField(
            model_name="organization",
            name="state",
            field=models.CharField(blank=True, max_length=255, verbose_name="State"),
        ),
        migrations.AlterField(
            model_name="organization",
            name="website",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, default="", max_length=255, verbose_name="Website"
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="zipcode",
            field=models.CharField(blank=True, max_length=48, verbose_name="Zip-Code"),
        ),
    ]
