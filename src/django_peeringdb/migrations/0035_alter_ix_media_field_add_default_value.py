# Generated by Django 4.2.16 on 2024-09-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_peeringdb", "0034_fix_voltage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="internetexchange",
            name="media",
            field=models.CharField(
                choices=[
                    ("Ethernet", "Ethernet"),
                    ("ATM", "ATM"),
                    ("Multiple", "Multiple"),
                ],
                default="Ethernet",
                max_length=128,
                verbose_name="Media Type",
            ),
        ),
    ]
