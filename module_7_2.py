# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка.
# Для получения номера байта начала строки используйте метод tell() перед записью.

# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.

strings_list = [
        'Sussus',
        'Amogus',
        'Biggus',
        'Dickus'
    ]

def custom_write(strings):
    strings_positions = {}
    with open('file_7_2.txt', 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            position = file.tell()
            file.write(string + '\n')
            strings_positions[(line_number, position)] = string                                                         #form dict(set as key, string as value)
            #file.close()                                                                                               not needed

        return strings_positions

result = custom_write(strings_list)
for element in result.items():
    print(element)
