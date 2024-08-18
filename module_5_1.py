#Создайте класс House.
#Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
#Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
#Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
#Создайте объект класса House с произвольным названием и количеством этажей.
#Вызовите метод go_to у этого объекта с произвольным числом.

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1,(new_floor+1)):
                print(floor)
        else:
            print('Такого этажа не существует')

ELBRUS = House('ЖК Эльбрус', 30)
SOUTH_TOWN = House('Южный город',120)

ELBRUS.go_to(10)
ELBRUS.go_to(0)
SOUTH_TOWN.go_to(5)