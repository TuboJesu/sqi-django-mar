from django.db import models

from datetime import date
from django.utils import timezone

from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    debut_year = models.IntegerField()
    artist_image = models.ImageField(upload_to= "artist-images", blank=True ,null=True)

    def __str__(self):
        return f"{self.name} | {self.debut_year}"


def release_date_validator(release_date):
    min_date = date(1800, 1, 1)
    current_date = timezone.now().date()
    
    if  not (min_date <= release_date <= current_date):
        raise ValidationError(f"The release date cannot be earlier than 1800 and cannot be in the future ")
    

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="Albums")
    title = models.CharField(max_length=255)
    release_date = models.DateField(validators=[release_date_validator])
    album_image = models.ImageField(upload_to= "album-images", blank=True ,null=True)

    def __str__(self):
        return f"{self.title} | {self.artist.name} - {self.release_date}"
