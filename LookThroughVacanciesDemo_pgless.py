import requests
import pandas as pd

pd.set_option('display.expand_frame_repr', False)
default_pages = 100
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


libra = look_through()
# libra = pd.read_csv('Data Analyst' and 'data scientist.csv')
libra = libra[['id', 'name', 'area', 'type', 'salary', 'snippet', 'employment', 'schedule']]
print(libra.info)
libra.to_csv('vacancies.csv')

# Этого достаточно, будет выдавать базовую информацию, сохраняется в pgSQL только ключевые данные (текст)
# исходные 5 параметров запроса + Дата ( всё равно не надо )
# называть надо будет таблицу по [профессия] + ДБ
