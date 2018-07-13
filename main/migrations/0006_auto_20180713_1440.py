# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180710_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamproject',
            name='assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='teamproject',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Project'),
        ),
    ]