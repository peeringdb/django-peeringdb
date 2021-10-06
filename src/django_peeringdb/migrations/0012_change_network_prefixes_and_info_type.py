# Generated by Django 3.1.2 on 2020-10-06 17:37

import django.db.models.deletion
import django_countries.fields
import django_inet.models
from django.db import migrations, models

import django_peeringdb.models.abstract


class Migration(migrations.Migration):

    dependencies = [
        ("django_peeringdb", "0011_ixlan_ixf_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="network",
            name="info_prefixes4",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Recommended maximum number of IPv4 routes/prefixes to be configured on peering sessions for this ASN",
                null=True,
                verbose_name="IPv4 Prefixes",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_prefixes6",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Recommended maximum number of IPv6 routes/prefixes to be configured on peering sessions for this ASN",
                null=True,
                verbose_name="IPv6 Prefixes",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Not Disclosed", "Not Disclosed"),
                    ("NSP", "NSP"),
                    ("Content", "Content"),
                    ("Cable/DSL/ISP", "Cable/DSL/ISP"),
                    ("Enterprise", "Enterprise"),
                    ("Educational/Research", "Educational/Research"),
                    ("Non-Profit", "Non-Profit"),
                    ("Route Server", "Route Server"),
                    ("Network Services", "Network Services"),
                    ("Route Collector", "Route Collector"),
                    ("Government", "Government"),
                ],
                default="Not Disclosed",
                max_length=60,
                verbose_name="Network Type",
            ),
        ),
    ]