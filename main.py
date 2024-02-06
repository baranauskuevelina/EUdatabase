import numpy as np
import pandas as pd

html = pd.read_html('https://work.studentnews.eu/s/3695/75547-European-countries-the-table-language-population-capital-currency-phone-code-internet-code.htm')
html[1].head()
countries = html[1]
countries.to_csv('countries.csv', index=False)
countries.to_excel('countries.xlsx', 'Sheet1', index=False)
countries.to_excel('countries.xlsx', sheet_name='Sheet1', index=False)

from sqlalchemy import create_engine
engine = create_engine('sqlite:///countries.db')
countries.to_sql('countries', con=engine, index=False)
countries.to_sql('countries', con=engine, if_exists='append', index=False)
countries.to_sql('countries', con=engine, if_exists='replace', index=False)
countries.to_sql('new_countries', con=engine, if_exists='fail', index=False)
countries.to_sql('new_countries', con=engine, if_exists='fail', index=False)
countries.to_sql('new_countries', con=engine, if_exists='replace', index=False)

fires = pd.read_csv('top_20_CA_wildfires.csv')
fires.head()
len(fires ['cause'].unique())
fires['cause'].value_counts()

fires['cause'].value_counts().plot(kind='bar')
fires['deaths'].value_counts().drop(0).sum()
fires.sort_values('year', ascending=False).head()

def months_to_nums(month):
    menesiai = {'January': 1,
     'February': 2,
     'March': 3,
     'April': 4,
      'May': 5,
      'June': 6,
      'July': 7,
      'August': 8,
      'September': 9,
      'October': 10,
      'November': 11,
      'December': 12}
    return menesiai[month]

months_to_nums('July')
fires['month'] = fires['month'].apply(months_to_nums)
fires.head()

data = pd.read_html('https://lt.wikipedia.org/wiki/S%C4%85ra%C5%A1as:Lietuvos_miestai_pagal_gyventojus')

# Pasitikriname sąrašo ilgį
len(data)
# kadangi sąrašas iš vieno elemento, nereikia spėlioti. Patogumo dėlei persivadiname DF.
miestai = data[0]
miestai.head()
miestai.info()
miestai.set_index('Miestas', inplace=True)
col_list = miestai.columns.tolist()
col_list
# Kad būtų patogiau, persivadinkim stulpelius

new_list = []
for item in col_list:
    fixed = item.replace('\xa0m.', '')
    new_list.append(fixed)

miestai.columns = new_list
miestai.head(60)
miestai.to_csv('miestai.csv')

def to_number(num):
    final = ""
    if type(num) == int:
        return num
    else:
        for x in str(num):
            if x.isdecimal() or x == ".":
                final += x
        if len(final) > 0:
            return int(float(final))
        return int(0)

to_number("")
miestai.columns
miestai['1970'] = miestai['1970'].apply(to_number)
miestai['1959'] = miestai['1959'].apply(to_number)
miestai['1923'] = miestai['1923'].apply(to_number)
miestai['1897'] = miestai['1897'].apply(to_number)
miestai['Tankumas (2019)'] = miestai['Tankumas (2019)'].apply(to_number)
miestai.info()