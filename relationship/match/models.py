from django.db import models

from human.models import Human


class Match(models.Model):
    FEMALE = '0'
    MALE = '1'
    OTHER = '2'
    GENDERS = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (OTHER, 'Other'),
    ]

    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=2, choices=GENDERS)
    human = models.ForeignKey(Human, on_delete=models.CASCADE, related_name='matches')
