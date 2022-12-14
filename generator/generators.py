import os
import random

from data.data import Person, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_us = Faker('en_US')
Faker.seed()

value_subjects = ["Hindi", "English", "Maths", "Physics",
                  "Chemistry", "Biology", "Computer Science",
                  "Commerce", "Accounting", "Economics", "Arts",
                  "Social Studies", "History", "Civics"]

value_state = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]


def generator_person_ru():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        departament=faker_ru.job(),
        age=random.randint(14, 100),
        salary=random.randint(1000, 5000)
    )


def generator_person_us():
    yield Person(
        firstname=faker_us.first_name(),
        lastname=faker_us.last_name(),
        email=faker_us.email(),
        current_address=faker_us.address(),
    )


def generated_file() -> tuple:
    current_dir = os.path.abspath(__file__)
    file_dir = "/".join(current_dir.split('/')[:-1])
    path_to_file = rf'{file_dir}/filetest{random.randint(0, 999)}.txt'
    file = open(path_to_file, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path_to_file


def generated_date():
    yield Date(
        date=faker_us.date_this_century(),
        year=faker_us.year(),
        month=faker_us.month(),
        day=faker_us.day_of_month(),
        time="12:00"
    )