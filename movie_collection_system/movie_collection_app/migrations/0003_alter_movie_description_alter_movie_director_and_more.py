# Generated by Django 5.1.7 on 2025-03-26 20:00

import movie_collection_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_collection_app', '0002_alter_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(help_text='A Brief Description of your Movie'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(help_text='Name of the Movie Director', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='default-image.jpeg', help_text='Movie Poster', upload_to='movies'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(help_text='Release Date of your Movie', validators=[movie_collection_app.models.release_date_validator]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(help_text='Title of the Movie', max_length=255),
        ),
    ]
