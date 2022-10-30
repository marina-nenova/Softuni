from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from carCollectionApp.car_collection.validators import ValueInRangeValidator


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2

    MIN_AGE_VALUE = 18

    PASSWORD_MAX_LENGTH = 30

    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MAX_LENGTH = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(MinLengthValidator(USERNAME_MIN_LENGTH, message="The username must be a minimum of 2 chars"),)
    )
    email = models.EmailField(
        null=False,
        blank=False
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(MinValueValidator(MIN_AGE_VALUE),)
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
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        verbose_name='Last Name'
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture'
    )


class Car(models.Model):
    CAR_TYPES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )

    CAR_TYPE_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 20
    MODEL_MIN_LENGTH = 2
    YEAR_MIN_VALUE = 1980
    YEAR_MAX_VALUE = 2049
    PRICE_MIN_VALUE = 1

    type = models.CharField(
        max_length=CAR_TYPE_MAX_LENGTH,
        choices=CAR_TYPES,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(MinLengthValidator(MODEL_MIN_LENGTH),)
    )
    year = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(ValueInRangeValidator(YEAR_MIN_VALUE, YEAR_MAX_VALUE),)
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(PRICE_MIN_VALUE),)
    )
