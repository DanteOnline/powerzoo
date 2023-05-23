from django.shortcuts import render
from .models import Category


def index_view(request):
    categories = Category.objects.all()
    return render(request, 'animals/index.html', {'categories': categories})