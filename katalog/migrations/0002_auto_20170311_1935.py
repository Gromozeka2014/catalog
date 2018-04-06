# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Tatoo_p',
            field=models.CharField(choices=[('Нет', 'Нет'), ('Нет, но хотелось бы', 'Нет, но хотелось бы'), ('Есть', 'Есть')], verbose_name='Тату\\пирсинги', max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(verbose_name='Адрес', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.CharField(verbose_name='Возраст', max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=smartfields.fields.ImageField(upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='children',
            field=models.CharField(choices=[('Нет', 'Нет'), ('Нет, но хотелось бы', 'Нет, но хотелось бы'), ('Есть, живем вместе', 'Есть, живем вместе'), ('Есть, живем раздельно', 'Есть, живем раздельно')], verbose_name='Дети', max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(verbose_name='О себе', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description_p',
            field=models.CharField(verbose_name='О партнере', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('Среднее', 'Среднее'), ('Среднее специальное', 'Среднее специальное'), ('Неполное высшее', 'Неполное высшее'), ('Высшее', 'Высшее'), ('Ученая степень', 'Ученая степень')], verbose_name='Образование', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(verbose_name='Email', max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='eye',
            field=models.CharField(choices=[('Синий', 'Синий'), ('Голубой', 'Голубой'), ('Серый', 'Серый'), ('Янтарный', 'Янтарный'), ('Оливковый', 'Оливковый'), ('Карий', 'Карий'), ('Черный', 'Черный'), ('Желтый', 'Жёлтый'), ('Хамелион', 'Хамелион')], verbose_name='Цвет глаз', max_length=8),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(verbose_name='Имя', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женчина', 'Женчина')], verbose_name='Пол', max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hair',
            field=models.CharField(choices=[('Блонд', 'Блонд'), ('Шатен', 'Шатен'), ('Брюнет', 'Брюнет'), ('Рыжий', 'Рыжий'), ('Русый', 'Русый'), ('Седой', 'Седой'), ('Нестандартный', 'Нестандартный')], verbose_name='Цвет волос', max_length=8),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.CharField(verbose_name='Рост', max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.CharField(choices=[('Работаю', 'Работаю'), ('Не работаю', 'Не работаю'), ('Непостоянное место работы', 'Непостоянное место работы')], verbose_name='Работа', max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(verbose_name='Отчество', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='second_name',
            field=models.CharField(verbose_name='Фамилия', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.CharField(verbose_name='Вес', max_length=3),
        ),
    ]
