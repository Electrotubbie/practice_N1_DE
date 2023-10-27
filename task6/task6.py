import requests
import fake_useragent
import json
from bs4 import BeautifulSoup

COUNT_OF_ACTIVITIES = 10

user = fake_useragent.UserAgent().random
header = {
    'user-agent': user
}
# получение необходимых json файлов
answer_list = dict()
answer_list['count_of_activities'] = COUNT_OF_ACTIVITIES
answer_list['activities'] = list()
link = 'http://www.boredapi.com/api/activity/'
for i in range(COUNT_OF_ACTIVITIES):
    response = requests.get(url=link, headers=header)
    answer = dict(json.loads(response.text))
    while answer['key'] in [a['key'] for a in answer_list['activities']]:
        response = requests.get(url=link, headers=header)
        answer = dict(json.loads(response.text))
    answer_list['activities'].append(answer)

# сохранение полученных json
with open('task6/get_random_activity.json', 'w') as file:
    json.dump(str(answer_list), file)

# создание таблицы
soup = BeautifulSoup(features='html.parser')

# создание заголовка таблицы
table = soup.new_tag('table')
tr = soup.new_tag('tr')
for name in answer_list['activities'][0].items():
    th = soup.new_tag('th')
    th.string = str(name[0])
    tr.append(th)
table.append(tr)
# создание тела таблицы
for ans in answer_list['activities']:
    tr = soup.new_tag('tr')
    for value in ans.items():
        td = soup.new_tag('td')
        td.string = str(value[1])
        tr.append(td)
    table.append(tr)

soup.append(table)

with open('task6/get_random_activity.html', 'w') as file:
    file.write(soup.prettify())