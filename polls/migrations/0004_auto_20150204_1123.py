# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150204_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='performance',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]
