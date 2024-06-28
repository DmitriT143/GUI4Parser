from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("input_page/", views.input_page, name="input_page"),
    path("output_page/", views.output_page, name="output_page"),
]
