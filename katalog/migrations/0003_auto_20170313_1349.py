# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0002_auto_20170311_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age_max',
            field=models.CharField(verbose_name='Возраст до', max_length=2, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='age_min',
            field=models.CharField(verbose_name='Возраст от', max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Tatoo_p',
            field=models.CharField(verbose_name='Тату\\пирсинги', max_length=20, choices=[('Нет', 'Нет'), ('Нет, но хотелось бы', 'Нет, но хотелось бы'), ('Есть', 'Есть')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='children',
            field=models.CharField(verbose_name='Дети', max_length=40, choices=[('Нет', 'Нет'), ('Нет, но хотелось бы', 'Нет, но хотелось бы'), ('Есть, живем вместе', 'Есть, живем вместе'), ('Есть, живем раздельно', 'Есть, живем раздельно')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(verbose_name='Образование', max_length=40, choices=[('Среднее', 'Среднее'), ('Среднее специальное', 'Среднее специальное'), ('Неполное высшее', 'Неполное высшее'), ('Высшее', 'Высшее'), ('Ученая степень', 'Ученая степень')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='eye',
            field=models.CharField(verbose_name='Цвет глаз', max_length=40, choices=[('Синий', 'Синий'), ('Голубой', 'Голубой'), ('Серый', 'Серый'), ('Янтарный', 'Янтарный'), ('Оливковый', 'Оливковый'), ('Карий', 'Карий'), ('Черный', 'Черный'), ('Желтый', 'Жёлтый'), ('Хамелион', 'Хамелион')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(verbose_name='Пол', max_length=20, choices=[('Мужчина', 'Мужчина'), ('Женчина', 'Женчина')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hair',
            field=models.CharField(verbose_name='Цвет волос', max_length=20, choices=[('Блонд', 'Блонд'), ('Шатен', 'Шатен'), ('Брюнет', 'Брюнет'), ('Рыжий', 'Рыжий'), ('Русый', 'Русый'), ('Седой', 'Седой'), ('Нестандартный', 'Нестандартный')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.CharField(verbose_name='Работа', max_length=40, choices=[('Работаю', 'Работаю'), ('Не работаю', 'Не работаю'), ('Непостоянное место работы', 'Непостоянное место работы')]),
        ),
    ]
