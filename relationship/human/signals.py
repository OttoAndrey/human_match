from django.db.models.signals import post_save
from django.dispatch import receiver
from faker import Faker

from human.models import Human
from match.models import Match


@receiver(post_save, sender=Human)
def create_match(sender, instance, **kwargs):
    print('im in')
    fake = Faker('ru_RU')
    name = fake.name()
    name_parts = name.split(' ')
    first_name = name_parts[1]
    second_name = name_parts[0]
    age = fake.random_int(0, 100)
    genders = ['F', 'M', 'O']
    gender = fake.random.choice(genders)

    print('now here')

    match = Match.objects.create(
        first_name=first_name,
        second_name=second_name,
        age=age,
        gender=gender,
        human=instance,
    )
    print('here')
    match.save()
