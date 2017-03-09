# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.BooleanField()),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_id', to='app.Profile')),
            ],
        ),
    ]