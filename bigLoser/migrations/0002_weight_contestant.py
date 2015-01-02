# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import bigLoser.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bigLoser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weight',
            name='contestant',
            field=models.ForeignKey(default=bigLoser.models.gen_default_contestant, to=settings.AUTH_USER_MODEL, unique_for_date=b'current_date'),
            preserve_default=True,
        ),
    ]
