# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0005_auto_20170313_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age_max',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='age_min',
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.CharField(verbose_name='Возраст', max_length=2),
        ),
    ]
