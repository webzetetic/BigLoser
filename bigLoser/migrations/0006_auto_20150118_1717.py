# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import bigLoser.models


class Migration(migrations.Migration):

    dependencies = [
        ('bigLoser', '0005_auto_20150118_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='contestant',
            field=models.ForeignKey(default=bigLoser.models.gen_default_contestant, to='bigLoser.Contestant', unique_for_date=b'current_date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weight',
            name='current_date',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
