#Функция count_calls подсчитывающая вызовы остальных функций.
#Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
#Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует.
#Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

calls = 0
global string
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(str(string))
    Up = str(string).upper()
    Low = str(string).lower()
    return {length, Up, Low}

def is_contains(string,list_to_search):
    count_calls()
    if str(string) in list(list_to_search):
        return True
    else:
        return False

print(string_info('Biggus'))
print(string_info('Dickus'))
print(is_contains('Monty',['Monty Python','Monty','Pyton']))
print(is_contains('Shrek',['Puss in boots','Donkey','Prince Charming', 'Fiona', 'Ogre']))
print(f'Сколько раз вызвали функции: {calls}')