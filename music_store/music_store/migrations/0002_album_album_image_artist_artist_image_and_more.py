# Generated by Django 5.1.7 on 2025-03-18 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_image',
            field=models.ImageField(blank=True, null=True, upload_to='album-images'),
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_image',
            field=models.ImageField(blank=True, null=True, upload_to='artist-images'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Albums', to='music_store.artist'),
        ),
    ]
