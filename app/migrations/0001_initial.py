# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=120, verbose_name='username')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('facebook_id', models.CharField(max_length=255, verbose_name='facebook_id')),
                ('facebook_token', models.CharField(max_length=255, verbose_name='facebook_token')),
                ('push_device_token', models.CharField(max_length=255, verbose_name='push device token')),
                ('photo', models.CharField(max_length=255, verbose_name='photo')),
                ('level', models.IntegerField(verbose_name='level')),
                ('status', models.IntegerField(verbose_name='status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
