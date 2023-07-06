from find_ids import *
from get_df_with_data import *
from top_skills import *


# Ключевое слово для поиска
job_title = 'Python'
# Кол-во страниц для поиска (на одной стр 100 вакансий, hh api банит IP на сутки после парсинга >100 вакансий)
pages_number = 1
# Локация (113 Россия)
area = 113
# Уточнение типа занятости
# fullDay - Полный день / shift - Сменный график / flexible - Гибкий график / remote - Удаленная работа / flyInFlyOut - Вахтовый метод
schedule = 'remote'
# Адрес для поиска вакансий в api hh, лучше не трогать этот параметр
url = 'https://api.hh.ru/vacancies/'
# Путь до папки vacancies для сохранения CSV файла с вакансиями и скилами
path_to_dir_vacancies = '/media/fj/a24662e7-0ac1-40c0-a433-d71f126c0765/fj/Документы/PycharmProjects/hh_parser_python/vacancies/'

# список с названиями колонок таблицы
columns = ['id',
           'vacancy_name',
           'city',
           'salary_from',
           'salary_to',
           'salary_currency',
           'experience',
           'work_schedule',
           'type_of_employment',
           'description',
           'skills',
           'employer',
           'publish_date',
           'vacancy_url',
           ]

# Получаем список с id вакансий
ids = find_ids(job_title, pages_number, area, schedule, url)
print(f'Кол-во полученных id - {len(ids)} шт.')
# Получаем DataFrame со всеми данными о вакансии
df = get_df_with_data(ids, columns, path_to_dir_vacancies)
print(f'Собрана инфа обо всех вакансиях и записана в файл')
top_skills_sorted_dict = top_skills(df, path_to_dir_vacancies)
print(f'Выявлены топ навыки и записаны в файл')
