from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the placeholder page.")


def input_page(request):
    return HttpResponse("There be input page")
    return render(request, input_page.html)


def output_page(request):
    return HttpResponse("You should be redirected here")
    return render(request, output_page.html)

# Create your views here.
