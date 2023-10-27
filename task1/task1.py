CASE_CHECK = True # учёт регистра (можно сменить на False чтоб не учитывать)
FILE_NAME = 'task1/text_1_var_37'
with open(FILE_NAME, 'r') as file:
    dirty_text = file.read() # условно грязный текст = текст с знаками препинания

# чистка текста
signs = set(ch for ch in list(dirty_text) if not ch.isalpha()) # поиск множества знаков препинания
clear_text = dirty_text if CASE_CHECK else dirty_text.lower() # присвоение чистому состояния грязного перед чисткой
for sign in signs:
    clear_text = clear_text.replace(sign, ' ') # чистка от знаков препинания путём замены их на пробелы
clear_text = clear_text.strip() # обрезание лишних пробелов по краям при их наличии

# подсчёт повторяющихся слов
list_text = clear_text.split(' ') # создание списка слов из текста, отделяя их пробелами
word_list = set(list_text) # множество всех возможных слов
word_list.discard('') # рудимент множественного пробела при сплите
result = [
    {'word':word, 'freq':list_text.count(word)}
    for word in word_list
    ] # подчёт количества повторений слова
result.sort(key=lambda x: x['freq'], reverse=True)
print(*[f'{elem["word"]}:{elem["freq"]}' for elem in result], sep='\n')

# запись результата согласно заданию в файл
with open(f'{FILE_NAME}_answer.txt', 'w') as file:
    file.writelines([f'{elem["word"]}:{elem["freq"]}' + '\n' for elem in result])