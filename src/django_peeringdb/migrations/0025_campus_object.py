# Generated by Django 3.2.7 on 2023-02-13 14:22

import django.core.validators
import django.db.models.deletion
import django.db.models.manager
import django_countries.fields
import django_handleref.models
import django_inet.models
from django.db import migrations, models

import django_peeringdb.models.abstract


class Migration(migrations.Migration):
    dependencies = [
        ("django_peeringdb", "0024_carrier_website_optional"),
    ]

    operations = [
        migrations.CreateModel(
            name="Campus",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "status",
                    models.CharField(blank=True, max_length=255, verbose_name="Status"),
                ),
                (
                    "created",
                    django_handleref.models.CreatedDateTimeField(
                        auto_now_add=True, verbose_name="Created"
                    ),
                ),
                (
                    "updated",
                    django_handleref.models.UpdatedDateTimeField(
                        auto_now=True, verbose_name="Updated"
                    ),
                ),
                ("version", models.IntegerField(default=0)),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Campus Name"
                    ),
                ),
                (
                    "name_long",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Long Name"
                    ),
                ),
                (
                    "aka",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Also Known As",
                    ),
                ),
                (
                    "website",
                    django_peeringdb.models.abstract.URLField(
                        blank=True, max_length=255, null=True, verbose_name="Website"
                    ),
                ),
            ],
            options={
                "verbose_name": "Campus",
                "verbose_name_plural": "Campuses",
                "db_table": "peeringdb_campus",
                "abstract": False,
            },
            managers=[
                ("handleref", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name="facility",
            name="campus",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fac_set",
                to="django_peeringdb.campus",
                verbose_name="Campus",
            ),
        ),
    ]
