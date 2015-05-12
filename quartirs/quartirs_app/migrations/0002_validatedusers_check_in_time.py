# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quartirs_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='validatedusers',
            name='check_in_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 14, 31, 13, 757004, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
