from django.shortcuts import render
from .models import Category


def index_view(request):
    # categories = Category.objects.all().prefetch_related('foods', 'animal_set')
    categories = Category.objects.all()
    result_count = 0
    for category in categories:
        result_count += category.animal_count
    return render(request, 'animals/index.html', {'categories': categories, 'result_count': result_count})