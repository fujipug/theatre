# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150204_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='price',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='price',
        ),
    ]
