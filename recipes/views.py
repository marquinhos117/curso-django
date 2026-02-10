from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Marcos Eduardo',
    })

def sobre(request):
    return HttpResponse("sobre")

def contato(request):
    return HttpResponse("contato")
