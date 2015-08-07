# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PushModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('push_message', models.CharField(max_length=100)),
                ('push_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ShowEndAlive',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('uuid', models.CharField(max_length=32, unique=True, null=True, blank=True)),
                ('mac_address', models.CharField(max_length=32, null=True, blank=True)),
                ('ip_address', models.CharField(max_length=15, null=True, blank=True)),
                ('product_id', models.CharField(max_length=32, null=True, blank=True)),
                ('os_version', models.CharField(max_length=32, null=True, blank=True)),
                ('kernel_version', models.CharField(max_length=32, null=True, blank=True)),
                ('cpu_model', models.CharField(max_length=64, null=True, blank=True)),
                ('bios_version', models.CharField(max_length=16)),
                ('graphics_model', models.CharField(max_length=128, null=True, blank=True)),
                ('graphics_driver_version', models.CharField(max_length=32, null=True, blank=True)),
                ('client_version', models.CharField(max_length=8, null=True, blank=True)),
                ('online_time', models.IntegerField(null=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'show_end_alive',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ShowPushMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, db_column='Id', serialize=False)),
                ('raw_data_id', models.IntegerField(null=True, blank=True)),
                ('sent_message', models.TextField()),
                ('sent_url', models.TextField(null=True, blank=True)),
                ('sent_number', models.IntegerField(null=True, blank=True)),
                ('recv_number', models.IntegerField(null=True, blank=True)),
                ('open_number', models.IntegerField(null=True, blank=True)),
                ('sent_time', models.IntegerField(null=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'show_push_message',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('notes', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='showendalive',
            unique_together=set([('id', 'bios_version')]),
        ),
    ]
