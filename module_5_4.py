#В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
#Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
#Дополните метод __new__ так, чтобы:
#Название объекта добавлялось в список cls.houses_history.
#Название строения можно взять из args по индексу.
#Также переопределите метод __del__(self) в котором будет выводиться строка:
#"<название> снесён, но он останется в истории"
#Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

class House:

    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super(House, cls).__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        #House.houses_history.append((self.name))   causes dublicates

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1,(new_floor+1)):
                print(floor)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self.number_of_floors

    def __radd__(self, value):
        self.number_of_floors += value
        return self.number_of_floors

    def __iadd__(self, value):
       self.number_of_floors += value
       return self.number_of_floors

    def __del__(self):
        return (f"{self.name} снесён, но он останется в истории")

o1 = House('ЖК Эльбрус', 30)
o2 = House('Южный город',120)
o3 = House('ГК Западный',90)
#print(o1.__str__())
#print(o2.__str__())
#print(o1.__len__())
#print(o2.__len__())

#print(o1 > o2, o1 >= o2, o1 < o2, o1 <=o2, o1 != o2)
#print(o1 + 10) #add
#print(5 + o2) #radd
#o1 += 15      #iadd
#print(o1)     #iadd
print(House.houses_history)
print(o1.__del__())
print(o3.__del__())