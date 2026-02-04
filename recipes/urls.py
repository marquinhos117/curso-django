from django.urls import path
from recipes.views import home, sobre, contato

# http request



urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]