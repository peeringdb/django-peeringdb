# Generated by Django 3.2.7 on 2023-01-16 12:39

from django.db import migrations
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
