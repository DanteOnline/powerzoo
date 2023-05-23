from django.db import models
from django.utils.functional import cached_property

class Food(models.Model):
    name = models.CharField(max_length=128, unique=True)
    index = models.IntegerField(default=0)

# Бурый Медведь, Белый медведь
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    foods = models.ManyToManyField(Food)


    @cached_property
    def animal_count(self):
        return self.animal_set.count()

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=64)
    # CASCADE, PROTECT, NULL
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # kind = models.CharField('kind', max_length=64)
    age = models.IntegerField(verbose_name='age', default=0)
    desc = models.TextField(verbose_name='description', blank=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    # class Meta:
    #     verbose_name = 'animal'
    #     verbose_name_plural = 'animals'
    #     ordering = ['pk']

class Card(models.Model):
    text = models.TextField(blank=True)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)



