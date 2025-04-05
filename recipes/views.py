
from django.http import HttpResponse
from django.shortcuts import render
# Crie suas views aqui.

def my_view(request):
    return HttpResponse("Hello, world!")

def home(request):
    return render(request, 'recipes/home.html')

def about(request):
    return HttpResponse("This is the about page.")
