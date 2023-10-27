from bs4 import BeautifulSoup
import pandas as pd

FILE_NAME = 'task5/text_5_var_37'

with open(FILE_NAME, 'r', encoding='UTF-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

rows = soup.find_all('tr')
title = [col.text for col in rows[0].find_all('th')]
df = pd.DataFrame(columns=title)

for row in rows[1:]:
    text_row = [td.text for td in row.find_all('td')]
    df.loc[len(df)] = text_row

df.to_csv(f'{FILE_NAME}_answer.csv', sep=';',index=False)