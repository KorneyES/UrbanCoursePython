#Необходимо дополнить класс House следующими специальными методами:
#__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
#__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

#    def __lt__(self, other):
#        return self.number_of_floors < other.number_of_floors
#
#    def __le__(self, other):
#        return self.number_of_floors <= other.number_of_floors
#
#    def __gt__(self, other):
#        return self.number_of_floors > other.number_of_floors
#
#    def __ge__(self, other):
#        return self.number_of_floors >= other.number_of_floors
#
#    def __ne__(self, other):
#        return self.number_of_floors != other.number_of_floors
#
#    def __add__(self, value):
#        self.number_of_floors += value
#        return self.number_of_floors
#
#    def __radd__(self, value):
#        self.number_of_floors += value
#        return self.number_of_floors
#
#   def __iadd__(self, value):
#       self.number_of_floors += value
#       return self.number_of_floors

o1 = House('ЖК Эльбрус', 30)
o2 = House('Южный город',120)
print(o1.__str__())
print(o2.__str__())
print(o1.__len__())
print(o2.__len__())

#print(o1 > o2, o1 >= o2, o1 < o2, o1 <=o2, o1 != o2)
#print(o1 + 10) #add
#print(5 + o2) #radd
#o1 += 15      #iadd
#print(o1)     #iadd

