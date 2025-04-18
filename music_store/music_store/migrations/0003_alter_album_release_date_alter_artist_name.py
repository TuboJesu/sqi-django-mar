# Generated by Django 5.1.7 on 2025-03-18 19:48

import django.core.validators
import music_store.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0002_album_album_image_artist_artist_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(validators=[music_store.models.release_date_validator]),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
