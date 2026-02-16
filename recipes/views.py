from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Marcos Eduardo',
    })

