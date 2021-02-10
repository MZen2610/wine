from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas as pd

excel_data_df = pd.read_excel('wine.xlsx', sheet_name='Лист1', na_values=['N/A', 'NA'], keep_default_na=False)

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

wine_data = []
for index, row in excel_data_df.iterrows():
     context = {
         "name": row['Название'],
         "sort": row['Сорт'],
         "price": row['Цена'],
         "picture": row['Картинка']
     }
     wine_data.append(context)

year = {
    "year_title": datetime.datetime.now().year - 1920,
}

template = env.get_template('template.html')
rendered_page = template.render( year_title=year, wines=wine_data )

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
