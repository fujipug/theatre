# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150204_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='unique_id',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
