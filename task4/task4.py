import pandas as pd

FILE_NAME = 'task4/text_4_var_37'
VARIANT = 37

df = pd.read_csv(filepath_or_buffer=FILE_NAME, header=0, names=['id', 'firstname', 'surname', 'age', 'salary', 'phone_number'], usecols=list(range(0,6)))

df = df.drop(columns='phone_number') # удаление колонки с номером телефона (1)

df['salary'] = df['salary'].str.replace('₽', '') # удаление знака ₽ из колонки з/п
df['salary'] = df['salary'].astype(int) # преобразование всех значений зп из str в int
avg_salary = df['salary'].mean() # расчёт средней зп
df = df.query(f'salary < {avg_salary}') # фильтр по доходам меньше среднего (2)

df = df.query(f'age > {25 + VARIANT%10}') # фильтр по возрасту больше 32 (3)

df = df.sort_values('id') # сортировка по id
df['name'] = df['firstname'] + ' ' + df['surname']
df['salary'] = df['salary'].astype(str) + '₽'

df.to_csv(f'{FILE_NAME}_answer.csv',sep=',', index=False, columns=['id', 'name', 'age', 'salary'])