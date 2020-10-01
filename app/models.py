from django.db import models

# Create your models here.

class Car(models.Model):
    manufacturer = models.CharField(max_length=256, verbose_name='Производитель')
    model = models.CharField(max_length=256, verbose_name='Модель авто')
    year = models.IntegerField(verbose_name='Год выпуска')
    TRANSMISSION_CHOICES = (
        ('механика', 'механика'),
        ('автомат', 'автомат'),
        ('робот', 'робот'),
    )
    transmission = models.CharField(choices=TRANSMISSION_CHOICES, verbose_name='Коробка передач', max_length=33)
    COLOR_CHOICES = (
        ('Красный', 'Красный'),
        ('Белый', 'Белый'),
        ('Черный', 'Черный'),
        ('Фиолетовый', 'Фиолетовый'),
        ('Синий', 'Синий'),
        ('Зеленый', 'Зеленый'),
    )
    color = models.CharField(choices=COLOR_CHOICES, verbose_name='Цвет', max_length=33)

    def __str__(self):
        return f'{self.model} {self.manufacturer}'
