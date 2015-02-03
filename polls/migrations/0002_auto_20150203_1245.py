# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default=b'Description missing.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='performance',
            name='description',
            field=models.TextField(default=b'Description missing.'),
            preserve_default=True,
        ),
    ]
