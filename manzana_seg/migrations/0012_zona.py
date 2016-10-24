# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manzana_seg', '0011_distrito'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(blank=True, db_column='ZONA', max_length=10, null=True)),
                ('id_manzana', models.CharField(blank=True, db_column='ID_MANZANA', max_length=20, null=True)),
                ('aeu', models.IntegerField(blank=True, db_column='AEU', null=True)),
                ('viv_aeu', models.IntegerField(blank=True, db_column='VIV_AEU', null=True)),
            ],
            options={
                'db_table': 'MZS_AEU',
                'managed': False,
            },
        ),
    ]
