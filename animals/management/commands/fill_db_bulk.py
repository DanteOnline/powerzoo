from django.core.management import BaseCommand
from mixer.backend.django import mixer
from animals.models import Category, Food, Animal, Card
import random
import time

class Command(BaseCommand):

    def handle(self, *args, **options):
        Food.objects.all().delete()
        food_list = []

        for i in range(800):
            food_list.append(f'name{i}')

        start_time = time.time()

        # for name in food_list:
        #     Food.objects.create(name=name)

        food_objects = []
        for number, name in enumerate(food_list):
             food = Food(name=name, index=number)
             food_objects.append(food)

        Food.objects.bulk_create(food_objects)

        end_time = time.time()
        print(end_time - start_time)

        print('DONE')