# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 04:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
        ('flow', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Collection',
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'default_permissions': (), 'permissions': (('view_collection', 'Can view collection'), ('edit_collection', 'Can edit collection'), ('share_collection', 'Can share collection'), ('download_collection', 'Can download files from collection'), ('add_collection', 'Can add data objects to collection'))},
        ),
        migrations.RenameField(
            model_name='trigger',
            old_name='project',
            new_name='collection',
        ),
    ]
