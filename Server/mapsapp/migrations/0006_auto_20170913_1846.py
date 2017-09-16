# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 18:46
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapsapp', '0005_auto_20170913_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='household',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='well',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='well',
            name='lon',
        ),
        migrations.AddField(
            model_name='household',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='well',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
