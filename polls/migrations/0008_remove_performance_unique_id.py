# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_performance_unique_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performance',
            name='unique_id',
        ),
    ]
