from django.shortcuts import render

from .models import Task

def index(request):
    tasks = Task.objects.order_by('-title')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def cataloge(request):
    return render(request, 'main/cataloge.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def delievery(request):
    return render(request, 'main/delievery.html')

def basket(request):
    return render(request, 'main/basket.html')