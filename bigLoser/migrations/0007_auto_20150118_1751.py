# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bigLoser', '0006_auto_20150118_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contest',
            old_name='contest_name',
            new_name='name',
        ),
    ]
