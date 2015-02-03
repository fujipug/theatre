# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('date', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=5)),
                ('picture', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('date', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=5)),
                ('picture', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
