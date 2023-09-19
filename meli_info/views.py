from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("HELLO WORLD")

def about(request):
    return HttpResponse("ABOUT")