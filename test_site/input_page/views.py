from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
