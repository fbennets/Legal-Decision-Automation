# Generated by Django 2.0.7 on 2019-04-01 19:58

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190401_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
