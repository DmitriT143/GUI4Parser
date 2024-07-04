import requests
import pandas as pd

pd.set_option('display.expand_frame_repr', False)
default_pages = 20
# default_ads = default_pages * per_page
job_title_default = ["'Data Analyst' and 'data scientist'"]
# Функция для переделки


def look_through():
    # Заменить на проверку перегрузки
    for job in job_title_default:
        data = []
        for i in range(default_pages):
            url = 'https://api.hh.ru/vacancies'
            par = {'text': job, 'area': '113', 'per_page': '100', 'page': i}
            # Сделать эту часть перегруженной, чтобы принимать 5 параметров
            request = requests.get(url, params=par)
            entry = request.json()
            data.append(entry)
            vacancy_details = data[0]['items'][0].keys()
            df = pd.DataFrame(columns=list(vacancy_details))
            ind = 0
            # Читает все теги с вакансии
            for i in range(len(data)):
                for j in range(len(data[i]['items'])):
                    df.loc[ind] = data[i]['items'][j]
                    ind += 1
            csv_name = job + ".csv"
            df.to_csv(csv_name)
            return df
            # Это местодержатель, заменить на передачу в БД


def get_resume(args):
    job = args[0]
    for i in range(default_pages):
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
        print(workday,"\n",requirements,"\n",responsibilities,"\n")


get_resume(['python'])
#libra = look_through()
# libra = pd.read_csv('Data Analyst' and 'data scientist.csv')
#libra = libra[['id', 'name', 'area', 'type', 'salary', 'snippet', 'employment', 'schedule']]
# название должности, навыки, формат работы и зарплата
#print(libra.info)
#libra.to_csv('vacancies.csv')

# Этого достаточно, будет выдавать базовую информацию, сохраняется в pgSQL только ключевые данные (текст)
# исходные 5 параметров запроса + Дата ( всё равно не надо )
# называть надо будет таблицу по [профессия] + ДБ
