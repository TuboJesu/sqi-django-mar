from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=1500)
    instructions = models.TextField(max_length=1500)
    cooking_time = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to="recipe/", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
# Create your models here.
