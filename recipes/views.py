from django.shortcuts import render
from django.http import HttpResponse

# Crie suas views aqui.

def my_view(request):
    return HttpResponse("Hello, world!")

def home(request):
    return HttpResponse("Welcome to the home page!")

def about(request):
    return HttpResponse("This is the about page.")
