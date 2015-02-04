# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150204_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='price',
            field=models.DecimalField(default=Decimal('0'), max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='performance',
            name='price',
            field=models.DecimalField(default=Decimal('0'), max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]
