#2 класса родителя: Animal, Plant
#Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
#Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
#4 класса наследника:
#Mammal, Predator для Animal.
#Flower, Fruit для Plant.
#У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
#eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
#Метод eat должен работать следующим образом:
#Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
#Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
#Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
#У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
#Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.

class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

    # def eat(self, food):
    #     if food.edible:
    #         print(f'{self.name} съел {food.name}')
    #         self.fed = True
    #     else:
    #         print(f'{self.name} не стал есть {food.name}')
    #         self.alive = False

class Mammal(Animal):
    pass


class Predator(Animal):
    pass
    # def eat(self, food):
    #     if food.edible:
    #         print(f'{self.name} съел {food.name}')
    #         self.fed = True
    #     else:
    #         print(f'{self.name} не стал есть {food.name}')
    #         self.alive = False

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Ауф')
a2 = Mammal('Енот')
p1 = Flower('Лютик')
p2 = Fruit('Крыжовник')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)