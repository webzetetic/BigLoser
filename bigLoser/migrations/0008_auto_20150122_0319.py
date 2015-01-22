# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bigLoser', '0007_auto_20150118_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='current_date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
