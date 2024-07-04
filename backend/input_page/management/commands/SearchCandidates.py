import django.db.models
import requests
from bs4 import BeautifulSoup
import fake_useragent
import re
from django.core.management.base import BaseCommand
from input_page.models import Resume

area: int = 113
page_count_limit = 12

def get_hh_links(text, schedule):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=f"https://hh.ru/search/resume?text={text}&logic=normal&pos=full_text&exp_period=all_time&exp_company_size=any&from=suggest_post&filter_exp_period=all_time&relocation=living_or_relocation&age_from=&age_to={schedule}&gender=unknown&order_by=relevance&search_period=0&items_on_page=20&hhtmFrom=resume_search_form",
        headers={"user-agent": ua.random}
    )
    if data.status_code != 200: print("error on start"); return
    soup = BeautifulSoup(data.content, "lxml")
    try:
        page_count = int(
            soup.find("div", attrs={"class": "pager"}).find_all("span", recursive=False)[-1].find("a").find(
                "span").text)
    except:
        print("error on link")
        return
    if page_count_limit < page_count:
        page_count = page_count_limit
    for page in range(page_count):
        data = requests.get(
            url=f"https://hh.ru/search/resume?isDefaultArea=true&ored_clusters=true&order_by=relevance&search_period=0&logic=normal&pos=full_text&page={page}&exp_period=all_time&filter_exp_period=all_time&gender=unknown&customDomain=1&area=113&relocation=living_or_relocation&text=python",
            headers={"user-agent": ua.random}
        )
        if data.status_code == 200:
            soup = BeautifulSoup(data.content, "lxml")
            for a in soup.find_all("a", attrs={"class": "bloko-link", "data-qa": "serp-item__title"}):
                yield f"https://hh.ru{a.attrs['href'].split('?')[0]}"
        print(page)
    print(data.content)


# Нужные тэги : Навыки, Зарплата, Профессия
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
        tags = [tag.text for tag in soup.find(attrs={"class": "bloko-tag-list"}).find_all("span", attrs={
            "class": "bloko-tag__section_text"})]
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
    print(link,name,salary,specialty,part_time,workday,tags)
    Resume.objects.update_or_create(
        link=link,
        name=name,
        salary=salary,
        specialty=specialty,
        part_time=part_time,
        workday=workday,
        tags=tags,
    )


class Command(BaseCommand):
    help = 'We are going to rip resumes from hh.ru without API, hi-hi'

    def handle(self, *args, **options):
        for link in get_hh_links("python",""):
            get_resume(link)
