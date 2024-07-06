from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'resume', views.ResumeViewSet)
router.register(r'Vacancy', views.VacancyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'refresh/resume', views.refresh_resume_page,),
    path(r'refresh/vacancy', views.refresh_vacancy_page,)
]
