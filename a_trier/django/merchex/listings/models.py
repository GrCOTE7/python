from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Band(models.Model):

    def __str__(self):
        return f"{self.name}"

    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTHETIC_POP = "SP"
        ALTERNATIVE_ROCK = "AR"

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(null=True, max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):

    def __str__(self):
        return f"{self.title}"

    class Type(models.TextChoices):
        RECORDS = "R"
        CLOTHING = "C"
        POSTERS = "P"
        MISCELLANEOUS = "M"

    title = models.fields.CharField(max_length=100)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    description = models.fields.TextField(default="", blank=True)
    price = models.fields.DecimalField(max_digits=10, decimal_places=2)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        null=True, validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    types = models.fields.CharField(choices=Type.choices, max_length=5)
    # like_new = models.fields.BooleanField(default=False)
