# Generated by Django 3.2.7 on 2023-01-16 12:39

import django.core.validators
import django.db.models.deletion
import django_countries.fields
import django_inet.models
from django.db import migrations, models

import django_peeringdb.models.abstract


class Migration(migrations.Migration):

    dependencies = [
        ("django_peeringdb", "0023_mtu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carrier",
            name="website",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, null=True, verbose_name="Website"
            ),
        ),
    ]
