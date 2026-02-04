from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("home 1")

def sobre(request):
    return HttpResponse("sobre")

def contato(request):
    return HttpResponse("contato")
