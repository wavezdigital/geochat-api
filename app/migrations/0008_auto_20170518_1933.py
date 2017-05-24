# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170503_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='address',
            field=models.CharField(default='NO_ADDRESS_ENTERED', max_length=255),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_id', to='app.Profile'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_settings_id', to='app.Profile'),
        ),
    ]