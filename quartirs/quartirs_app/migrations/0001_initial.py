# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entity_b', models.CharField(max_length=200)),
                ('qr_hash', models.CharField(max_length=100)),
                ('entity_a', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ValidatedUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entity_b', models.CharField(max_length=200)),
                ('entity_a', models.CharField(max_length=200)),
            ],
        ),
    ]
