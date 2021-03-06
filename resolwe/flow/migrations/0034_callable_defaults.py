# Generated by Django 2.2 on 2019-04-24 07:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flow", "0033_move_purged"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="process_error",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255), default=list, size=None
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="process_info",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255), default=list, size=None
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="process_warning",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255), default=list, size=None
            ),
        ),
    ]
