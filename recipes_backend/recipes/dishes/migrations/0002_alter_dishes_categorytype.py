# Generated by Django 4.2.13 on 2024-06-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='categoryType',
            field=models.CharField(choices=[('Салаты', 'Салаты'), ('Рецепты первых блюд', 'Рецепты первых блюд'), ('Рецепты вторых блюд', 'Рецепты вторых блюд'), ('Дессерты', 'Дессерты'), ('Закуски', 'Закуски')], max_length=20, verbose_name='Категория'),
        ),
    ]
