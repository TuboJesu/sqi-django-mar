from django.db import models
from django.core.exceptions import ValidationError

from datetime import date
from django.utils import timezone



def publication_date_validator(publication_date):
    min_date = date(1500, 1, 1)
    current_date = timezone.now().date()
    
    if  not (min_date <= publication_date <= current_date):
        raise ValidationError(f"The publication date cannot be earlier than 1800 and cannot be in the future ")
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(validators=[publication_date_validator])

    def __str__(self):
        return f'{self.title} by {self.author}'

def validate_rating(rating):
    if rating not in range(1, 6):
        raise ValidationError("Rating should only be between I and 5")


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="review")
    reviewer_name = models.CharField(max_length=255, help_text="Enter your name")
    rating = models.PositiveIntegerField(validators=[validate_rating], help_text="Enter a rating ranging from 1 to 5 only")
    comment = models.CharField(max_length=500, help_text="You can leave your comments here")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book} by {self.reviewer_name}'
# Create your models here.


