from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


from django.utils import timezone
from datetime import date

def release_date_validator(release_date):
    min_date = date(1800, 1, 1)
    current_date = timezone.now().date()
    
    if  not (min_date <= release_date <= current_date):
        raise ValidationError(f"The release date cannot be earlier than 1800 and cannot be in the future ")


# Create your models here.

class GenreChoices(models.TextChoices):
    ACTION = 'AC', 'Action'
    DRAMA = 'DR', 'Drama'
    COMEDY = 'CO', 'Comedy'
    HORROR = 'HO', 'Horror'
    ROMANCE = 'RO', 'Romance'
    SCIFI = 'SF', 'Science Fiction'
    FANTASY = 'FA', 'Fantasy'
    DOCUMENTARY = 'DO', 'Documentary'
    THRILLER = 'TH', 'Thriller'

class Movie(models.Model):
    title = models.CharField(max_length=255, help_text='Title of the Movie')
    director = models.CharField(max_length=255, help_text='Name of the Movie Director')
    release_date = models.DateField(validators=[release_date_validator], help_text='Release Date of your Movie')
    description = models.TextField(help_text='A Brief Description of your Movie')
    poster = models.ImageField(upload_to="movies", default='default-image.jpeg', help_text='Movie Poster')
    genre = models.CharField(max_length=2, choices=GenreChoices.choices, default=GenreChoices.DRAMA)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
