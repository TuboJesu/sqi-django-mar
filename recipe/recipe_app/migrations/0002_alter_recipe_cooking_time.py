# Generated by Django 5.1.7 on 2025-03-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveBigIntegerField(),
        ),
    ]
