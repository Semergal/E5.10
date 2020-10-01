# Generated by Django 3.0.8 on 2020-08-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200828_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[(1, 'Красный'), (2, 'Белый'), (3, 'Черный'), (4, 'Фиолетовый'), (5, 'Синий'), (6, 'Зеленый')], max_length=33, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.SmallIntegerField(choices=[(1, 'механика'), (2, 'автомат'), (3, 'робот')], verbose_name='Коробка передач'),
        ),
    ]
