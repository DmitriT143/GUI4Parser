from rest_framework import viewsets, filters
from .models import Resume, Vacancy
from .serializer import ResumeSerializer, VacancySerializer
from django_filters.rest_framework import DjangoFilterBackend


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filerSet_fields = ['link','name','salary','specialty','part_time','workday', 'tags']
    search_fields = ['link','name','salary','specialty','part_time','workday', 'tags']
    ordering_fields = ['link','name','salary','specialty','part_time','workday', 'tags']


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterSet_fields = ['link','name','region','salary_min','salary_max','workday','requirements','responsibilities']
    search_fields = ['link','name','region','salary_min','salary_max','workday','requirements','responsibilities']
    ordering_fields = ['link','name','region','salary_min','salary_max','workday','requirements','responsibilities']


# def index(request):
#     return HttpResponse("Hello, world. You're at the placeholder page.")
# Create your views here.
