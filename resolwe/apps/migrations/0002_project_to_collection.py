# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 04:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0002_project_to_collection'),
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='projects',
            new_name='collections',
        ),
        migrations.RemoveField(
            model_name='app',
            name='default_project',
        ),
        migrations.AddField(
            model_name='app',
            name='default_collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_collection', to='flow.Collection'),
        ),
    ]
