# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180508_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='substance',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user_name',
            new_name='username',
        ),
    ]