import random

from data.data import Person
from faker import Faker

faker_lang = Faker(random.choice(['ru_RU', 'en_US']))


def generated_person():
    yield Person(
        first_name=faker_lang.first_name(),
        last_name=faker_lang.last_name(),
        postal_code=random.randint(100000, 999999)
    )
