from unicodedata import name
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Superhero(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    ANGELS = 'A'
    HUMANS = 'H'
    DEMONS = 'D'
    GODS = 'G'
    SPECIES_CHOICES = [
        (ANGELS, 'Angels'),
        (HUMANS, 'Humans'),
        (DEMONS, 'Demons'),
        (GODS, 'Gods')
    ]
    # name of superhero
    name = models.CharField(max_length=255, null=False, primary_key=True, validators=[
        MinLengthValidator(10, 'The name field must contain at least 10 characters')
    ])
    # alias of superhero
    alias = models.CharField(max_length=255, null=False, validators=[
        MinLengthValidator(10, 'The alias field must contain at least 10 characters')
    ])
    # specie of superhero
    Species = models.CharField(
        max_length=1,
        choices=SPECIES_CHOICES,
        default=DEMONS,
    )
    # birth of superhero
    Date_of_Birth = models.CharField(max_length=255, null=False, validators=[
        MinLengthValidator(10, 'The Date_of_Birth field must contain at least 10 characters')
    ])
    # age of superhero
    Age = models.CharField(max_length=255, null=False, validators=[
        MinLengthValidator(10, 'The Age field must contain at least 10 characters')
    ])
    # gender of superhero
    Gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    # intelligence value of superhero
    intelligence = models.IntegerField(
        max_length=2, null=False, validators=[
        MinLengthValidator(1, 'The intelligence field must contain at least 1 characters')
    ])
    # strength value of superhero
    strength = models.IntegerField(
        max_length=2, null=False, validators=[
        MinLengthValidator(1, 'The strength field must contain at least 1 characters')
    ])
    # speed value of superhero
    speed = models.IntegerField(
        max_length=2, null=False, validators=[
        MinLengthValidator(1, 'The speed field must contain at least 1 characters')
    ])
    # durability value of superhero
    durability = models.IntegerField(
        max_length=2, null=False, validators=[
        MinLengthValidator(1, 'The durability field must contain at least 1 characters')
    ])
    # power value of superhero
    power = models.IntegerField(
        max_length=2, null=False, validators=[
        MinLengthValidator(1, 'The power field must contain at least 1 characters')
    ])
    # combat value of superhero
    combat = models.IntegerField(
        max_length=2, null=False, validators=[
        MinLengthValidator(1, 'The combat field must contain at least 1 characters')
    ])
    # tier value of superhero
    tier = models.IntegerField(
        max_length=2, null=False, validators=[
        MinLengthValidator(1, 'The tier field must contain at least 1 characters')
    ])

    def __str__(self):
        return "{} - {}".format(self.name, self.alias)
