# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.
# Подробное ТЗ:
#     Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
#     И методами:
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета.
# Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
# Метод get_sides должен возвращать значение я атрибута __sides.
# Метод __len__ должен возвращать периметр фигуры.
# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.



# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

import math
class Figure:
    def __init__(self, r, g, b, *sides):
        self.sides_count = len(sides)
        self.__sides = []
        self.__color = (r, g, b)
        self.filled = False

        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return (isinstance(r, int) and 0 <= r <= 255 and
                isinstance(g, int) and 0 <= g <= 255 and
                isinstance(b, int) and 0 <= b <= 255)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g ,b):
            self.__color = (r, g, b)
        else:
            print('Неверные значения, введите в диапазоне 0...255')

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.sides_count != len(new_sides):
            print('Неверное количество сторон')
        else:
            self.__sides = list(new_sides)

#     Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

class Circle(Figure):
    def __init__(self, r, g, b, sides):
        self.sides_count = 1
        super().__init__(r, g, b, sides)
        sides = self.get_sides()
        if sides:
            self.__radius = sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

#circle1 = Circle(100, 100, 100, 3)
#circle1.set_sides(5)

#     Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)

class Triangle(Figure):
    def __init__(self, r, g, b, *sides):
        self.sides_count = 3
        super().__init__(r, g, b, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        hp = (a + b + c) / 2                                                                                            #half_perimeter
        if a + b > c and a + c > b and b + c > a:
            return math.sqrt(hp * (hp - a) * (hp - b) * (hp - c))
        else:
            return ('Две любые взятые стороны должны быть больше третьей')
        #print(f'a: {a} b: {b} c: {c} hp: {hp}')

# triangle1 = Triangle(100,100,100,10,20,30)
# triangle1.set_sides(14,23,15)
# print(triangle1.get_square())

#     Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.

class Cube(Figure):
    def __init__(self, r, g, b, side):
        self.sides_count = 12
        super().__init__(r, g, b, *([side] * self.sides_count))
        self.__side = side

    def get_volume(self):
        return self.__side ** 3

    def set_sides(self, *new_sides):                                                                                    #set_for_cube
        if len(new_sides) != self.sides_count:
            print('Неверное количество сторон')
        else:
            self.__sides = [new_sides[0]] * self.sides_count
            self.__side = new_sides[0]

circle1 = Circle(200, 200, 100, 10) # (Цвет, стороны)
cube1 = Cube(222, 35, 130, 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())



