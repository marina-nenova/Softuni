from django.db import models


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 30

    INGREDIENTS_MAX_LENGTH = 250

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LENGTH,
    )
    time = models.IntegerField()
