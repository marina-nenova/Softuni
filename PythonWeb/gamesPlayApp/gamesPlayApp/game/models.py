from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    PASSWORD_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    email = models.EmailField(
        null=False,
        blank=False
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(MinValueValidator(12),)
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Game(models.Model):
    CATEGORY_CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    )

    MAX_TITLE_LENGTH = 30
    CATEGORY_MAX_LENGTH = 15
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5
    MAX_LEVEL_MIN_VALUE = 1

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LENGTH,
        null=False,
        blank=False,
        choices=CATEGORY_CHOICES
    )
    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(RATING_MIN_VALUE), MaxValueValidator(RATING_MAX_VALUE))
    )
    max_level = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Max Level',
        validators=(MinValueValidator(MAX_LEVEL_MIN_VALUE),)
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    summary = models.TextField(
        null=True,
        blank=True
    )
