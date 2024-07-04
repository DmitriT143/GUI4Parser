from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'resume',views.ResumeViewSet)
router.register(r'Vacancy',views.VacancyViewSet)

urlpatterns = [
    path('', include(router.urls)),
#    path("input_page/", views.input_page, name="input_page"),
#    path("output_page/", views.output_page, name="output_page"),
]
