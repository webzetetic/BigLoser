# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bigLoser', '0004_contest_contestant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contestant',
            old_name='contestant_name',
            new_name='user',
        ),
    ]
