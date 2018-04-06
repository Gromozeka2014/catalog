from django.db import models
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from django.utils.encoding import smart_str
from django.core.validators import MaxValueValidator

## Класс модели анкет.
#
#  Класс определяющий свойства и функции анкет клиентов.
class Profile(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    second_name = models.CharField('Фамилия', max_length=20)
    middle_name = models.CharField('Отчество', max_length=20)
    GENDER_CHOICES = (
        (u'Мужчина', u'Мужчина'),
        (u'Женчина', u'Женчина'),
    )
    gender = models.CharField('Пол', max_length=20, choices=GENDER_CHOICES)
    age = models.PositiveSmallIntegerField('Возраст', validators=[MaxValueValidator(99)])
    height = models.PositiveSmallIntegerField('Рост', validators=[MaxValueValidator(220)])
    weight = models.PositiveSmallIntegerField('Вес', validators=[MaxValueValidator(300)])
    Hair_Color_Choices =(
        (u'Блонд', u'Блонд'),
        (u'Шатен', u'Шатен'),
        (u'Брюнет', u'Брюнет'),
        (u'Рыжий', u'Рыжий'),
        (u'Русый', u'Русый'),
        (u'Седой', u'Седой'),
        (u'Нестандартный', u'Нестандартный'),
    )
    hair = models.CharField('Цвет волос', max_length=20, choices=Hair_Color_Choices)
    Eye_Color_Choices =(
        (u'Синий', u'Синий'),
        (u'Голубой', u'Голубой'),
        (u'Серый', u'Серый'),
        (u'Янтарный', u'Янтарный'),
        (u'Оливковый', u'Оливковый'),
        (u'Карий', u'Карий'),
        (u'Черный', u'Черный'),
        (u'Желтый', u'Жёлтый'),
        (u'Хамелеон', u'Хамелеон'),
    )
    eye = models.CharField('Цвет глаз', max_length=40, choices=Eye_Color_Choices)
    education_Choices =(
        (u'Среднее', u'Среднее'),
        (u'Среднее специальное', u'Среднее специальное'),
        (u'Неполное высшее', u'Неполное высшее'),
        (u'Высшее', u'Высшее'),
        (u'Ученая степень', u'Ученая степень'),
    )
    education = models.CharField('Образование', max_length=40, choices=education_Choices)
    Job_Cgoices =(
        (u'Работаю', u'Работаю'),
        (u'Не работаю', u'Не работаю'),
        (u'Непостоянное место работы', u'Непостоянное место работы'),
    )
    job = models.CharField('Работа', max_length=40, choices=Job_Cgoices)
    children_Choices =(
        (u'Нет', u'Нет'),
        (u'Нет, но хотелось бы', u'Нет, но хотелось бы'),
        (u'Есть, живем вместе', u'Есть, живем вместе'),
        (u'Есть, живем раздельно', u'Есть, живем раздельно'),
    )
    children = models.CharField('Дети', max_length=40, choices=children_Choices)
    Tatoo_p_Choices =(
        (u'Нет', u'Нет'),
        (u'Нет, но хотелось бы', u'Нет, но хотелось бы'),
        (u'Есть', u'Есть'),
    )
    Tatoo_p = models.CharField('Тату\пирсинги', max_length=20, choices=Tatoo_p_Choices)
    address = models.CharField('Адрес', max_length=50)
    email = models.EmailField('Email')
    phone = models.PositiveSmallIntegerField('Телефон', validators=[MaxValueValidator(99999999999)])
    description = models.CharField('О себе', max_length=100)
    description_p = models.CharField('О партнере', max_length=100)
    avatar = fields.ImageField('Фото', dependencies=[
        FileDependency(processor=ImageProcessor(
            format='JPEG', scale={'max_width': 200, 'max_height': 240}))],
        upload_to='')

    ## Конструктор возращаюший Имя и Фамилию.
    def __str__(self):
            return smart_str('%s %s' % (self.first_name, self.second_name))
