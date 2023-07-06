import sys
import requests
from IPython.display import display, HTML


# Красивое отображение прогресса выполнения проги
def display_side_by_side(dfs: list, captions: list, space_width=10):
    output = ""
    combined = dict(zip(captions, dfs))

    for caption, df in combined.items():
        output += (df.style.set_properties(**{'text-align': 'left'})
                   .set_table_attributes("style='display:inline'")
                   .set_caption(caption)._repr_html_())
        output += "\xa0" * space_width

    display(HTML(output))

# Красивое отображение прогресса выполнения проги
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

def find_ids(job_title, pages_number, area, schedule, url):
    # список в который добавляем все найденые id
    ids = []
    # счетчик для вывода на экран прогресса обработки
    count = 0
    # проверка не выходит количество страниц с вакансиями за предельное значение
    if pages_number > 20:
        pages_number = 20
    # посчет общего количества вакансий
    ids_sum = pages_number * 100

    print(f'Start loading {ids_sum} job vacancies ')

    # проходимся по заданному количеству страниц с вакансиями
    for i in range(pages_number):
        # задаем параметры за запроса
        par = {'text': job_title, 'area': area, 'schedule': schedule, 'per_page': 100, 'page': i}
        # делаем запрос
        r = requests.get(url, params=par)
        e = r.json()

        # поиск всех id на одной странице и добавление их в список ids
        for i in range(len(e['items'])):
            count += 1
            progress(count, ids_sum, 'loaded')

            try:
                ids.append(e['items'][i].get('id'))
            except:
                print('Going beyond the allowed number of vacancies!')
                print(f'Uploaded {len(ids)} vacancies')
                return ids

    print('\nEverything OK')
    print(f'Uploaded {len(ids)} vacancies')

    # возварт списка с id всех найденых вакансий
    return ids