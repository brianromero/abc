# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manzana_seg', '0009_auto_20160908_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('ccpp', models.CharField(db_column='CCPP', max_length=2, primary_key=True, serialize=False)),
                ('cod_prov', models.CharField(blank=True, db_column='COD_PROV', max_length=4, null=True)),
                ('provincia', models.CharField(blank=True, db_column='PROVINCIA', max_length=50, null=True)),
                ('fec_carga', models.DateTimeField(blank=True, db_column='FEC_CARGA', null=True)),
            ],
            options={
                'db_table': 'TB_PROVINCIA',
                'managed': False,
            },
        ),
    ]
