# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manzana_seg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Segmentacion_prueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('distrito', models.CharField(max_length=50)),
                ('zona', models.CharField(max_length=5)),
                ('seccion', models.CharField(max_length=18)),
                ('codccpp', models.CharField(max_length=4)),
                ('cat_ccpp', models.CharField(max_length=2)),
                ('aeu_n', models.CharField(max_length=3)),
                ('nro_aeu', models.IntegerField()),
                ('estado_seg', models.IntegerField()),
                ('estado_croquis', models.IntegerField()),
            ],
            options={
                'db_table': 'segmentacion_prueba',
                'managed': True,
            },
        ),
    ]
