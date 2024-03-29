# Generated by Django 1.11.23 on 2019-12-09 09:06


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_peeringdb", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="network",
            name="info_prefixes4",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Recommended IPv4 maximum-prefix limit to be configured on peering sessions for this ASN",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_prefixes6",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Recommended IPv6 maximum-prefix limit to be configured on peering sessions for this ASN",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="irr_as_set",
            field=models.CharField(
                blank=True,
                help_text="Reference to an AS-SET or ROUTE-SET in Internet Routing Registry (IRR)",
                max_length=255,
            ),
        ),
    ]
