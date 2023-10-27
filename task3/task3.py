VARIANT = 37
SEPARATOR = ',' # разделитель между числами
FILE_NAME = 'task3/text_3_var_37'
with open(FILE_NAME, 'r') as file:
    numbers_text = file.read().strip('\n ')

str_numbers_list = [num_str.split(SEPARATOR) for num_str in numbers_text.split('\n')]
result_numbers_list = list()
for str_numbers in str_numbers_list:
    numbers = list()
    for index, num in enumerate(str_numbers):
        if num == 'NA':
            num = str((int(str_numbers[index-1]) + int(str_numbers[index+1]))/2)
        if float(num)**0.5 >= 50+VARIANT:
            numbers.append(num)
    result_numbers_list.append(numbers)

with open(f'{FILE_NAME}_answer.txt', 'w') as file:
    file.writelines([f'{SEPARATOR.join(numbers)}\n' for numbers in result_numbers_list])