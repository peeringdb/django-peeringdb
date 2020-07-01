# Generated by Django 2.2.12 on 2020-05-21 06:05

from django.db import migrations, models


def adjust_traffic_levels(apps, schema_editor):
    Network = apps.get_model("django_peeringdb", "Network")

    for net in Network.handleref.all():

        # only save networks that actually had to have their value
        # adjusted

        save = False

        # remove spaces

        if net.info_traffic.find(" ") > -1:
            net.info_traffic = net.info_traffic.replace(" ","")
            save = True

        # replace values

        if net.info_traffic == "100+Gbps":
            net.info_traffic = "100-200Gbps"
            save = True

        elif net.info_traffic == "1Tbps+":
            net.info_traffic = "1-5Tbps"
            save = True

        elif net.info_traffic == "10Tbps+":
            net.info_traffic = "10-20Tbps"
            save = True

        if save:
            net.save()


class Migration(migrations.Migration):

    dependencies = [
        ('django_peeringdb', '0007_add_verbose_names'),
    ]

    operations = [
        migrations.RunPython(adjust_traffic_levels),
        migrations.AlterField(
            model_name='network',
            name='info_traffic',
            field=models.CharField(blank=True, choices=[('', 'Not Disclosed'), ('0-20Mbps', '0-20Mbps'), ('20-100Mbps', '20-100Mbps'), ('100-1000Mbps', '100-1000Mbps'), ('1-5Gbps', '1-5Gbps'), ('5-10Gbps', '5-10Gbps'), ('10-20Gbps', '10-20Gbps'), ('20-50Gbps', '20-50Gbps'), ('50-100Gbps', '50-100Gbps'), ('100-200Gbps', '100-200Gbps'), ('200-300Gbps', '200-300Gbps'), ('300-500Gbps', '300-500Gbps'), ('500-1000Gbps', '500-1000Gbps'), ('1-5Tbps', '1-5Tbps'), ('5-10Tbps', '5-10Tbps'), ('10-20Tbps', '10-20Tbps'), ('20-50Tbps', '20-50Tbps'), ('50-100Tbps', '50-100Tbps'), ('100+Tbps', '100+Tbps')], max_length=39),
        ),
    ]
