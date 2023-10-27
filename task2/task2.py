SEPARATOR = '.' # разделитель между числами
FILE_NAME = 'task2/text_2_var_37'
with open(FILE_NAME, 'r') as file:
    numbers_text = file.read().strip('\n ')

numbers_list = [list(map(int, num_str.split(SEPARATOR))) for num_str in numbers_text.split('\n')]
avarage_list = list(map(lambda x: sum(x)/len(x), numbers_list))

with open(f'{FILE_NAME}_answer.txt', 'w') as file:
    file.writelines(f'{avarage}\n' for avarage in avarage_list)