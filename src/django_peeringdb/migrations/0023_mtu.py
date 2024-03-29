# Generated by Django 3.2.7 on 2022-12-09 13:49
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_peeringdb", "0022_carriers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ixlan",
            name="mtu",
            field=models.PositiveIntegerField(
                choices=[(1500, "1500"), (9000, "9000")],
                default=1500,
                verbose_name="MTU",
            ),
        ),
    ]
