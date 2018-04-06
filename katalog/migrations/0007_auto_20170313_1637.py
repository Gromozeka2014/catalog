# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0006_auto_20170313_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(max_length=2, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.IntegerField(max_length=3, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(max_length=20, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(max_length=11, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='second_name',
            field=models.CharField(max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(max_length=3, verbose_name='Вес'),
        ),
    ]
