# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-16 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20171116_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classperiod',
            name='id',
        ),
        migrations.AlterField(
            model_name='classperiod',
            name='date',
            field=models.DateField(primary_key=True, serialize=False, unique=True),
        ),
    ]
