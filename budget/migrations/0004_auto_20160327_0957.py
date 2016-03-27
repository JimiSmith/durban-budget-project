# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20160326_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='order',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='year',
            field=models.CharField(db_index=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='order',
            field=models.IntegerField(db_index=True),
        ),
    ]
