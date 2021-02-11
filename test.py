import pandas as pd
from pprint import pprint
import collections

wine2_df = pd.read_excel('wine2.xlsx', sheet_name='Лист1', na_values=['N/A', 'NA'], keep_default_na=False)

# wine2_dict = {}
wine2_dict = collections.defaultdict(list)

for index, row in wine2_df.iterrows():

    context = {
       "name": row['Название'],
        "sort": row['Сорт'],
        "price": row['Цена'],
        "picture": row['Картинка']
    }

    wine2_dict[row['Категория']].append(context)

    # if row['Категория'] in wine2_dict:
    #     wine2_list = []
    #     for item in wine2_dict[row['Категория']]:
    #         wine2_list.append(item)
    #     wine2_list.append(context)
    #     wine2_dict[row['Категория']] = wine2_list
    # else:
    #     wine2_dict[row['Категория']] = [context]

# pprint(wine2_dict)
for category in wine2_dict:
    # print(wine2_dict[category])
    for item in wine2_dict[category]:
        pprint(item)


