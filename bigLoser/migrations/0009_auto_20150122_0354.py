# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bigLoser', '0008_auto_20150122_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='current_date',
            field=models.DateField(default=datetime.datetime.today),
            preserve_default=True,
        ),
    ]
