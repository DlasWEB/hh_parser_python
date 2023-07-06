import re
import requests
from fake_useragent import UserAgent


def get_information_about_vacancy(url, id):
    row_for_df = []
    useragent = UserAgent()
    headers = {
        'User-Agent': f'{useragent.random}'
    }
    proxies = {
        # 'https': 'http://172.67.70.201:80',
        # 'https': 'http://172.67.167.223:80',
    }
    try:
        data = requests.get(url + id,
                            headers = headers,
                            # proxies = proxies,
                            ).json()
        row_for_df.append(int(data.get('id')))
        row_for_df.append(data.get('name'))
        row_for_df.append(data.get('area').get('name'))
        salary = data.get('salary')
        if salary != None:
            salary_from = data.get('salary').get('from')
            if salary_from != None:
                row_for_df.append(int(data.get('salary').get('from')))
            else:
                row_for_df.append(None)

            salary_to = data.get('salary').get('to')

            if salary_to != None:
                row_for_df.append(int(data.get('salary').get('to')))
            else:
                row_for_df.append(None)

            row_for_df.append(data.get('salary').get('currency'))
        else:
            row_for_df.append(None)
            row_for_df.append(None)
            row_for_df.append(None)
        row_for_df.append(data.get('experience').get('name'))
        row_for_df.append(data.get('schedule').get('name'))
        row_for_df.append(data.get('employment').get('name'))
        row_for_df.append(re.sub(r'\<[^\>]+\>', '', data.get('description')))
        skills = data.get('key_skills')
        if skills != None:
            skills_list = []
            for i in skills:
                skills_list.append(i.get('name'))
            row_for_df.append(skills_list)
        else:
            row_for_df.append(None)
        row_for_df.append(data.get('employer').get('name'))
        row_for_df.append(data.get('published_at'))
        row_for_df.append(data.get('alternate_url'))
    except TypeError:
        print(data)


    return row_for_df