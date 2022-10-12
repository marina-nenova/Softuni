from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size


class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='mediafiles/pet_photos/',
        validators=(validate_file_size, )
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH),),
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH
    )

    date_of_publication = models.DateField(auto_now=True)

    tagged_pets = models.ManyToManyField(
        Pet,
    )
