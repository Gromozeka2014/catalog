# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0004_auto_20170313_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age_max',
            field=models.PositiveSmallIntegerField(verbose_name='Возраст до', max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age_min',
            field=models.PositiveSmallIntegerField(verbose_name='Возраст от', max_length=2, blank=True),
        ),
    ]
