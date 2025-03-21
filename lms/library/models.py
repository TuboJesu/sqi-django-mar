from django.db import models

# Create your models here.

from authors.models import Author

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    num_of_pages = models.PositiveIntegerField()
    published_on = models.DateField()
    cover_image = models.ImageField(upload_to="book-covers/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} published by {self.author}"