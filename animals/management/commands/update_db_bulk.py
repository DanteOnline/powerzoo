from django.core.management import BaseCommand
from django.db.models import F
from mixer.backend.django import mixer
from animals.models import Category, Food, Animal, Card
import random
import time

class Command(BaseCommand):

    def handle(self, *args, **options):
        foods = Food.objects.all()

        start_time = time.time()

        # for food in foods:
        #     food.name = f'{food.name}u'
        #     print(food.name)
        #     food.save()
        foods.update(index=F('index')+1)
        # foods.update(name=f'{F("name")}u')

        end_time = time.time()
        print(end_time - start_time)



        print('DONE')