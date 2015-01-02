# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bigLoser', '0002_weight_contestant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='current_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
