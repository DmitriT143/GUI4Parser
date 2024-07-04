import requests
from django.core.management.base import BaseCommand
from input_page.models import Vacancy


def get_resume(job):
    default_pages = 250
    for i in range(default_pages):
        print(i)
        url = 'https://api.hh.ru/vacancies'
        par = {'text': job, 'area': '113', 'per_page': '20', 'page':i}
        request = requests.get(url, params=par)
        entry = request.json()
        link = entry.get("items", {})[0].get("id")
        name = entry.get("items", {})[0].get("name")
        region = entry.get("items", {})[0].get("area", {}).get('name')
        salary = entry.get("items", {})[0].get("salary", {})
        if salary != None:
            currency = salary.get("currency")
            salary_min = salary.get("from")
            salary_max = salary.get("to")
            if salary_min != None:
                salary_min = salary_min, currency
            else: salary_min = "None"
            if salary_max != None:
                salary_max = salary_max, currency
            else: salary_max = "NaN"
        else: salary_max = "NaN"; salary_min = "None"
        workday = entry.get("items", {})[0].get("schedule").get("name")
        requirements = entry.get("items", {})[0].get("snippet").get("requirement")
        responsibilities = entry.get("items", {})[0].get("snippet").get("responsibility")
        if workday==None: workday= 'N/A'
        if requirements==None: requirements = 'N/A'
        if responsibilities==None: responsibilities = 'N/A'
        Vacancy.objects.update_or_create(
            link=link,
            name=name,
            region=region,
            salary_min=salary_min,
            salary_max=salary_max,
            workday=workday,
            requirements=requirements,
            responsibilities=responsibilities,
        )


class Command(BaseCommand):
    help = 'We are going to rip vacancies from hh.ru with API, YEAH, no, that is worse than without API'

    def handle(self, *args, **options):
        get_resume("python")
