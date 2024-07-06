import fake_useragent
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from rest_framework import viewsets, filters
from .models import Resume, Vacancy
from .serializer import ResumeSerializer, VacancySerializer
from django_filters.rest_framework import DjangoFilterBackend


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['link', 'name', 'salary', 'specialty', 'part_time', 'workday', 'tags']
    search_fields = ['link', 'name', 'salary', 'specialty', 'part_time', 'workday', 'tags']
    ordering_fields = ['link', 'name', 'salary', 'specialty', 'part_time', 'workday', 'tags']


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['link', 'name', 'region', 'salary_min', 'salary_max', 'workday', 'requirements',
                        'responsibilities']
    search_fields = ['link', 'name', 'region', 'salary_min', 'salary_max', 'workday', 'requirements',
                     'responsibilities']
    ordering_fields = ['link', 'name', 'region', 'salary_min', 'salary_max', 'workday', 'requirements',
                       'responsibilities']


def refresh_resume_page(request):
    def browse_for_resume(args: dict):
        page_count_limit = 2

        def get_links(args: dict):
            ua = fake_useragent.UserAgent()
            link_data = requests.get(
                url=f"https://hh.ru/search/resume?text={args.get('name')}&logic=normal&pos=full_text&exp_period=all_time&exp_company_size=any&from=suggest_post&filter_exp_period=all_time&relocation=living_or_relocation&age_from=&age_to=&employment{args.get('part_time')}&schedule={args.get('workday')}&gender=unknown&salary_from=&salary_to={args.get('salary')}&currency_code=RUR&order_by=relevance&search_period=0&items_on_page=20",
                headers={"user-agent": ua.random}
            )
            if link_data.status_code != 200: print("error upon start"); return
            try:
                page_count = int(
                    BeautifulSoup(link_data.content, "lxml").find("div", attrs={"class": "pager"}).find_all("span", recursive=False)[
                        -1].find("a").find("span").text)
            except:
                print("error on link")
                return
            if page_count > page_count_limit:
                page_count = page_count_limit
            for page in range(page_count):
                page_data = requests.get(
                    url=f"https://hh.ru/search/resume?text={args.get('name')}&logic=normal&pos=full_text&exp_period=all_time&exp_company_size=any&from=suggest_post&filter_exp_period=all_time&relocation=living_or_relocation&age_from=&age_to=&employment{args.get('part_time')}&schedule={args.get('workday')}&gender=unknown&salary_from=&salary_to={args.get('salary')}&currency_code=RUR&order_by=relevance&search_period=0&items_on_page=20&page={page}",
                    headers={"user-agent": ua.random}
                )
                if page_data.status_code == 200:
                    for a in BeautifulSoup(page_data.content, "lxml").find_all("a", attrs={"class": "bloko-link", "data-qa": "serp-item__title"}):
                        yield f"https://hh.ru{a.attrs['href'].split('?')[0]}"

        def get_resume(link):
            ua = fake_useragent.UserAgent()
            data = requests.get(
                url=link,
                headers={"user-agent": ua.random}
            )
            if data.status_code != 200:
                return
            soup = BeautifulSoup(data.content, "lxml")
            try:
                name = soup.find(attrs={"class": "resume-block__title-text"}).text
            except:
                name = "NaN"
            try:
                salary = soup.find(attrs={"class": "resume-block__salary"}).text.replace("\u2009", "").replace("\xa0", " ")
            except:
                salary = "NaN"
            try:
                tags = [tag.text for tag in soup.find(attrs={"class": "bloko-tag-list"}).find_all("span", attrs={"class": "bloko-tag__section_text"})]
            except:
                tags = ["NaN"]
            try:
                specialty_data = soup.find(attrs={"class": "resume-block-container"}).text
                if specialty_data.__contains__("График"):
                    workday = re.search(r'(?<=График работы: )(.*)', specialty_data).group(1)
                    specialty = re.search(r'(?<=Специализации:)(.*)(?=Занятость:)', specialty_data).group(1)
                    part_time = re.search(r'(?<=Занятость: )(.*)(?=График)', specialty_data).group(1)
                else:
                    workday = "NaN";
                    specialty = "NaN";
                    part_time = "NaN";
            except:
                workday = "NaN";
                specialty = "NaN";
                part_time = "NaN";
            link = link.replace('https://hh.ru/resume/', "")
            print(link, name, salary, specialty, part_time, workday, tags)
            Resume.objects.update_or_create(
               link=link,
               name=name,
               salary=salary,
               specialty=specialty,
               part_time=part_time,
               workday=workday,
               tags=tags,
            )

        for link in get_links(args):
            get_resume(link)

    args = request.GET
    browse_for_resume(args)
    return HttpResponse(f"Hello, world. You're at the placeholder page.")


def refresh_vacancy_page(request):
    args = request.GET
    print(args)
def get_resume(args:dict):
    default_pages = 40
    search_name = args.get('name')
    search_schedule = args.get('workday')
    search_salary = args.get('salary_max')
    for i in range(default_pages):
        print(i)
        url = 'https://api.hh.ru/vacancies'
        par = {'text': search_name, 'area': '113', 'per_page': '20', 'page':i}
        request = requests.get(url, params=par)
        entry = request.json()
        print(entry)
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
    get_resume(args)
    return HttpResponse(f"Hello, world. You're at the placeholder page.")


# Create your views here.
