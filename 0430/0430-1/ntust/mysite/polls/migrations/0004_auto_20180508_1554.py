# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 07:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180507_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='taxt',
            new_name='substance',
        ),
    ]