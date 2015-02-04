# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150203_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=2, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='performance',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=2, decimal_places=2),
            preserve_default=True,
        ),
    ]
