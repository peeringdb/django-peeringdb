# Generated by Django 4.2.11 on 2024-05-02 09:46

import django.core.validators
import django_inet.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_peeringdb", "0032_alter_property_help_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="property",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Owner", "Owner"),
                    ("Lessee", "Leased or Rented"),
                ],
                help_text="Leasing or renting is an agreement with a property owner for use of the property.",
                max_length=27,
                null=True,
                verbose_name="Property",
            ),
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
                ],
                verbose_name="Route Server ASN",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="asn",
            field=django_inet.models.ASNField(
                unique=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="ASN",
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
                help_text="Peering with the routeserver and BFD support is shown with an icon",
                max_length=72,
                verbose_name="General Policy",
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
                ],
                verbose_name="Local ASN",
            ),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="asn",
            field=django_inet.models.ASNField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="ASN",
            ),
        ),
    ]
