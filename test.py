import pandas as pd
from pprint import pprint
import collections

wine2_df = pd.read_excel('wine2.xlsx', sheet_name='Лист1', na_values=['N/A', 'NA'], keep_default_na=False)

wine2_dict = {}

for index, row in wine2_df.iterrows():

    context = {
       "Название": row['Название'],
        "Сорт": row['Сорт'],
        "Цена": row['Цена'],
        "Картинка": row['Картинка']
    }

    if row['Категория'] in wine2_dict:
        wine2_list = []
        for item in wine2_dict[row['Категория']]:
            wine2_list.append(item)
        wine2_list.append(context)
        wine2_dict[row['Категория']] = wine2_list
    else:
        wine2_dict[row['Категория']] = [context]

pprint(wine2_dict)
