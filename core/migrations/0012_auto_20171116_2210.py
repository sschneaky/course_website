# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-16 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20171116_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classperiod',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='reading',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
