from django.core.management import BaseCommand
from mixer.backend.django import mixer
from animals.models import Category, Food, Animal, Card
import random

class Command(BaseCommand):

    def handle(self, *args, **options):
        Food.objects.all().delete()
        Category.objects.all().delete()
        Animal.objects.all().delete()
        foods = mixer.cycle(10).blend(Food)
        mixer.cycle(10).blend(Category)
        mixer.cycle(100).blend(Animal, category=mixer.SELECT)

        categories = Category.objects.all()
        for category in categories:
            category.foods.add(*foods)
            category.save()

        print('DONE')