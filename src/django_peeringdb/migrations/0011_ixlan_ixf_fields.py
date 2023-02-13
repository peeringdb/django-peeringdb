# Generated by Django 2.2.12 on 2020-07-13 07:00

import django.db.models.deletion
import django_countries.fields
import django_inet.models
from django.db import migrations, models

import django_peeringdb.models.abstract


class Migration(migrations.Migration):
    dependencies = [
        ("django_peeringdb", "0010_ix_ixf_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="ixlan",
            name="ixf_ixp_member_list_url",
            field=models.URLField(
                blank=True, null=True, verbose_name="IX-F Member Export URL"
            ),
        ),
        migrations.AddField(
            model_name="ixlan",
            name="ixf_ixp_member_list_url_visible",
            field=models.CharField(
                choices=[
                    ("Private", "Private"),
                    ("Users", "Users"),
                    ("Public", "Public"),
                ],
                default="Private",
                max_length=64,
                verbose_name="IX-F Member Export URL Visibility",
            ),
        ),
    ]
