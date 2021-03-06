# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170518_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('place_identifier', models.CharField(max_length=255)),
                ('complaint_date', models.DateTimeField(auto_now=True)),
                ('profile_denouncing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_denouncing_id', to='app.Profile')),
                ('profile_receive_complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_receive_complaint', to='app.Profile')),
            ],
        ),
    ]
