# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smartfields.models
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(verbose_name='Имя', max_length=100, blank=True)),
                ('second_name', models.CharField(verbose_name='Фамилия', max_length=100, blank=True)),
                ('middle_name', models.CharField(verbose_name='Отчество', max_length=100, blank=True)),
                ('gender', models.CharField(verbose_name='Пол', max_length=1, choices=[('M', 'Мужчина'), ('F', 'Женчина')])),
                ('age', models.CharField(verbose_name='Возраст', max_length=2, blank=True)),
                ('height', models.CharField(verbose_name='Рост', max_length=3, blank=True)),
                ('weight', models.CharField(verbose_name='Вес', max_length=3, blank=True)),
                ('hair', models.CharField(verbose_name='Цвет волос', max_length=1, choices=[('B', 'Блонд'), ('Sh', 'Шатен'), ('Br', 'Брюнет'), ('R', 'Рыжий'), ('Ru', 'Русый'), ('S', 'Седой'), ('Un', 'Нестандартный')])),
                ('eye', models.CharField(verbose_name='Цвет глаз', max_length=1, choices=[('B', 'Синий'), ('Lb', 'Голубой'), ('Gr', 'Серый'), ('Y', 'Янтарный'), ('M', 'Оливковый'), ('Bu', 'Карий'), ('Bl', 'Черный'), ('Ye', 'Жёлтый')])),
                ('education', models.CharField(verbose_name='Образование', max_length=1, choices=[('M', 'Среднее'), ('Ms', 'Среднее специальное'), ('NU', 'Неполное высшее'), ('U', 'Высшее'), ('M', 'Ученая степень')])),
                ('job', models.CharField(verbose_name='Работа', max_length=1, choices=[('N', 'Работаю'), ('Y', 'Не работаю'), ('Yn', 'Непостоянное место работы')])),
                ('children', models.CharField(verbose_name='Дети', max_length=1, choices=[('N', 'Нет'), ('Nb', 'Нет, но хотелось бы'), ('Y', 'Есть, живем вместе'), ('Yn', 'Есть, живем раздельно')])),
                ('Tatoo_p', models.CharField(verbose_name='Тату\\пирсинги', max_length=1, choices=[('N', 'Нет'), ('Nb', 'Нет, но хотелось бы'), ('Y', 'Есть')])),
                ('address', models.CharField(verbose_name='Адрес', max_length=100, blank=True)),
                ('email', models.EmailField(verbose_name='Email', max_length=254, blank=True)),
                ('phone', models.CharField(verbose_name='Телефон', max_length=100, blank=True)),
                ('description', models.CharField(verbose_name='О себе', max_length=100, blank=True)),
                ('description_p', models.CharField(verbose_name='О партнере', max_length=100, blank=True)),
                ('avatar', smartfields.fields.ImageField(verbose_name='Фото', upload_to='', blank=True)),
            ],
            bases=(smartfields.models.SmartfieldsModelMixin, models.Model),
        ),
    ]
