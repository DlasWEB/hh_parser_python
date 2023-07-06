import time

import pandas as pd

from get_information_about_vacancy import *


def get_df_with_data(ids, columns, path_to_dir_vacancies):
    list_of_rows = []
    for i in ids:
        list_of_rows.append(get_information_about_vacancy('https://api.hh.ru/vacancies/', i))
        time.sleep(0.1)
    df = pd.DataFrame(list_of_rows, columns=columns)
    df.to_csv(rf'{path_to_dir_vacancies}vacancies.csv', index=False)
    return df