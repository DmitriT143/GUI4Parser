from django.db import models

# Create your models here.


class Resume(models.Model):
    link = models.CharField(primary_key=True)
    name = models.CharField(max_length=120)
    salary = models.CharField(max_length=36)
    specialty = models.CharField(max_length=100)
    part_time = models.CharField(max_length=100)
    workday = models.CharField(max_length=100)
    tags = models.CharField(max_length=None)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    link = models.CharField(primary_key=True)
    name = models.CharField(max_length=120)
    region = models.CharField(max_length=50)
    salary_min = models.CharField(max_length=18)
    salary_max = models.CharField(max_length=18)
    workday = models.CharField(max_length=100)
    requirements = models.CharField(max_length=None)
    responsibilities = models.CharField(max_length=None)

    def __str__(self):
        return self.name
