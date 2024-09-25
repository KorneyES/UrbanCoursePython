# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.
# Пример результата выполнения программы:
# Пример работы функции:
# a = all_variants("abc")
# for i in a:
# print(i)

def all_variants(text):
    length = len(text)
    for start in range(length):
        for end in range(start +1, length + 1):
            yield text[start:end]

for i in all_variants('asd'):
    print(i)
