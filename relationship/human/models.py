from django.db import models


class Human(models.Model):
    FEMALE = '0'
    MALE = '1'
    OTHER = '2'
    GENDERS = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (OTHER, 'Other'),
    ]

    avatar = models.ImageField()
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=2, choices=GENDERS)
