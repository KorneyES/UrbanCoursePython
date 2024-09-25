# Даны 2 строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'
# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# Здесь ? - место написания lambda-функции.
result = list(map(lambda x, y: x == y, first, second))
print(result)
# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.


# Замыкание:
# Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
# Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий неограниченное количество данных любого типа.
# Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
# Функция get_advanced_writer возвращает функцию write_everything.
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(str(item) + '\n')
    return write_everything

# Данный код:
write = get_advanced_writer('example.txt')                                                                              #file_required
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:
# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
# В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words и возвращать его.
# Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете использовать функцию choice из модуля random.
#
# Ваш код (количество слов для случайного выбора может быть другое):
from random import choice as ch

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return ch(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())









# # Ваш класс здесь
# first_ball = MysticBall('Да', 'Нет', 'Наверное')
# print(first_ball())
# print(first_ball())
# print(first_ball())
# Примерный результат (может отличаться из-за случайности выбора):
# Да
# Да
# Наверное
#
# Примечания:
# Все задания пишутся в одном модуле.
# Передаваемые данные в функции и объекты можете использовать свои, главное, чтобы ваш код полноценно демонстрировал логику написанного.