# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-15 12:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20170102_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='user',
        ),
        migrations.AlterField(
            model_name='ocdactionuser',
            name='date_birth',
            field=models.DateField(default=datetime.datetime(2017, 1, 15, 12, 20, 56, 777790, tzinfo=utc), verbose_name='date of birth'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ocdactionuser',
            name='have_ocd',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ocdactionuser',
            name='username',
            field=models.CharField(max_length=24),
        ),
        migrations.DeleteModel(
            name='Challenge',
        ),
    ]
