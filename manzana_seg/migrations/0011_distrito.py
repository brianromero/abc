# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manzana_seg', '0010_provincia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('ubigeo', models.CharField(db_column='UBIGEO', max_length=6, primary_key=True)),
                ('ccdi', models.CharField(db_column='CCDI', max_length=2, primary_key=True, serialize=False)),
                ('distrito', models.CharField(blank=True, db_column='DISTRITO', max_length=50, null=True)),
                ('region', models.CharField(blank=True, db_column='REGION', max_length=50, null=True)),
                ('region_nat', models.CharField(blank=True, db_column='REGION_NAT', max_length=50, null=True)),
                ('nro_aer', models.CharField(blank=True, db_column='NRO_AER', max_length=50, null=True)),
                ('fec_carga', models.DateTimeField(blank=True, db_column='FEC_CARGA', null=True)),
            ],
            options={
                'db_table': 'TB_DISTRITO',
                'managed': False,
            },
        ),
    ]
