# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0007_auto_20170313_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='Возраст', validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.PositiveSmallIntegerField(verbose_name='Рост', validators=[django.core.validators.MaxValueValidator(220)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.PositiveSmallIntegerField(verbose_name='Телефон', validators=[django.core.validators.MaxValueValidator(11)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.PositiveSmallIntegerField(verbose_name='Вес', validators=[django.core.validators.MaxValueValidator(300)]),
        ),
    ]
