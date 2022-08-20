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
    name = models.CharField(max_length=255, null=False, primary_key=True)
    # alias of superhero
    alias = models.CharField(max_length=255, null=False)
    # specie of superhero
    Species = models.CharField(
        max_length=1,
        choices=SPECIES_CHOICES,
        default=DEMONS,
    )
    # birth of superhero
    Date_of_Birth = models.CharField(max_length=255, null=False)
    # age of superhero
    Age = models.CharField(max_length=255, null=False)
    # gender of superhero
    Gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    # intelligence value of superhero
    intelligence = models.IntegerField(
        max_length=2, null=False)
    # strength value of superhero
    strength = models.IntegerField(
        max_length=2, null=False)
    # speed value of superhero
    speed = models.IntegerField(
        max_length=2, null=False)
    # durability value of superhero
    durability = models.IntegerField(
        max_length=2, null=False)
    # power value of superhero
    power = models.IntegerField(
        max_length=2, null=False)
    # combat value of superhero
    combat = models.IntegerField(
        max_length=2, null=False)
    # tier value of superhero
    tier = models.IntegerField(
        max_length=2, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.alias)
