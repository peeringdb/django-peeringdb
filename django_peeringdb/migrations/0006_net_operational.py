# Generated by Django 2.2.12 on 2020-04-03 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_peeringdb', '0005_fac_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkixlan',
            name='operational',
            field=models.BooleanField(default=True),
        ),
    ]
