import pandas as pd

def top_skills(df, path_to_dir_vacancies):
    # преводим ключевые навыки из Series в List
    skills_df = df['skills'].to_list()
    # список для всех ключевых навыков со всех вакансий
    list_with_all_skills_from_df = []
    for i in skills_df:
        for j in i:
            list_with_all_skills_from_df.append(j)

    dict_with_skills_and_count_it = {}
    for i in list_with_all_skills_from_df:
        if i in dict_with_skills_and_count_it:
            dict_with_skills_and_count_it[i] += 1
        else:
            dict_with_skills_and_count_it[i] = 1

    sorted_tuples = sorted(dict_with_skills_and_count_it.items(), key=lambda item: item[1], reverse=True)
    sorted_dict_with_skills_and_count_it = {k: v for k, v in sorted_tuples}
    pd.DataFrame(list(sorted_dict_with_skills_and_count_it.items()), columns=['skill', 'count']).to_csv(rf'{path_to_dir_vacancies}top_skills.csv', index=False)
    return sorted_dict_with_skills_and_count_it